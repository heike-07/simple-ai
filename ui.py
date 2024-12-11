import streamlit as st
from zhipuai import ZhipuAI

# 读取 API 密钥
def read_api_key(file_path="GLM4-Flash.key"):
    with open(file_path, "r") as file:
        api_key = file.read().strip()  # 读取并去掉多余的空白字符
    return api_key

# 使用读取到的 API 密钥初始化客户端
api_key = read_api_key("GLM4-Flash.key")  # 根据实际路径调整文件名
client = ZhipuAI(api_key=api_key)

# 用来存储对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

if "input" not in st.session_state:
    st.session_state.input = ""  # 初始化输入框内容

# 设置页面标题
st.set_page_config(page_title="AI-@heike07", page_icon="🤖", layout="wide")
st.title("与AI-@heike07聊天")
st.markdown(
    '<p style="color:gray;">作者(Author)：heike07 & GPT4o 项目源码：<a href="https://github.com/heike-07/simple-ai" style="color:gray; text-decoration:none;">GitHub</a></p>',
    unsafe_allow_html=True
)

# 自定义样式
st.markdown("""
    <style>
    .user-message {
        background-color: #e1f7d5;  /* 绿色背景 */
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        width: auto;  /* 宽度根据内容自适应 */
        word-wrap: break-word;  /* 自动换行 */
        text-align: left;  /* 文字左对齐 */
        display: inline-block;  /* 使框根据内容自动调整宽度 */
        float: right;  /* 将框显示在右侧 */
    }
    .assistant-message {
        background-color: #d3f4fe;  /* 蓝色背景 */
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        width: auto;  /* 宽度根据内容自适应 */
        word-wrap: break-word;  /* 自动换行 */
        text-align: left;  /* 左对齐 */
        display: inline-block;  /* 使框根据内容自动调整宽度 */
    }
    </style>
""", unsafe_allow_html=True)

# 显示历史对话
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)




# 提交逻辑
def on_submit():
    user_input = st.session_state.input.strip()
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 调用 API 获取模型的响应
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=st.session_state.messages
        )
        model_response = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": model_response})

        # 清空输入框内容
        st.session_state.input = ""

# 输入框和按钮
st.text_input(
    "请输入消息：",
    value=st.session_state.input,
    on_change=on_submit,
    key="input",
    placeholder="在此输入消息，然后按回车发送..."
)





