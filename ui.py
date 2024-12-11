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
st.title("AI-@heike07")
st.markdown(
    '<p style="color:gray;">作者(Author)：heike07 & GPT4o 项目源码：<a href="https://github.com/heike-07/simple-ai" style="color:gray; text-decoration:none;">GitHub</a></p>',
    unsafe_allow_html=True
)

# 自定义样式
st.markdown("""
    <style>
    body {
        background-color: black;  /* 设置页面背景为黑色 */
        color: white;  /* 设置字体颜色为白色 */
    }

    .user-message {
        background: linear-gradient(135deg, #00c6ff, #0072ff);  /* 蓝色渐变 */
        padding: 15px;
        border-radius: 20px;
        margin: 12px 0;
        width: auto;
        word-wrap: break-word;
        text-align: left;
        display: inline-block;
        float: right;
        box-shadow: 0 8px 30px rgba(0, 114, 255, 0.3);  /* 强化阴影 */
        color: white;
        border: 2px solid rgba(0, 114, 255, 0.6);  /* 边框 */
    }
    .assistant-message {
        background: linear-gradient(135deg, #00b09b, #96c93d);  /* 绿色渐变 */
        padding: 15px;
        border-radius: 20px;
        margin: 12px 0;
        width: auto;
        word-wrap: break-word;
        text-align: left;
        display: inline-block;
        box-shadow: 0 8px 30px rgba(0, 255, 123, 0.3);  /* 强化阴影 */
        color: white;
        border: 2px solid rgba(0, 255, 123, 0.6);  /* 边框 */
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
    "请向我提问：",
    value=st.session_state.input,
    on_change=on_submit,
    key="input",
    placeholder="在此输入消息，然后按回车发送..."
)
