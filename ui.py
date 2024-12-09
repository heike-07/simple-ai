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

# 设置页面标题
st.set_page_config(page_title="与智谱AI模型聊天", page_icon="🤖", layout="wide")
st.title("与智谱AI聊天")

# 自定义样式
st.markdown("""
    <style>
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        background-color: #f7f7f7;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .user-message {
        background-color: #e1f7d5;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: auto;
        word-wrap: break-word;
        text-align: right;
    }

    .assistant-message {
        background-color: #d3f4fe;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: auto;
        word-wrap: break-word;
        text-align: left;
    }

    .message-container {
        max-height: 400px;
        overflow-y: auto;
        margin-bottom: 20px;
    }

    .input-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .input-container input {
        width: 80%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    .input-container button {
        padding: 10px 15px;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
        border: none;
    }

    </style>
""", unsafe_allow_html=True)

# 显示历史对话
with st.container():
    #st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    # 显示消息
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 用户输入框
user_input = st.text_input("请输入消息：", "")

# 按钮用于提交用户输入并与模型交互
if st.button("提交") and user_input:
    # 将用户输入添加到消息历史
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 调用 API 获取模型的响应
    response = client.chat.completions.create(
        model="glm-4-flash",  # 使用的模型
        messages=st.session_state.messages  # 传递对话历史
    )

    # 提取并打印模型的响应
    model_response = response.choices[0].message.content  # 确保这个路径正确

    # 将模型的响应添加到消息历史
    st.session_state.messages.append({"role": "assistant", "content": model_response})

    # 清空输入框并刷新页面
    st.rerun()

# 防止页面被刷新时丢失内容
# if not user_input:
#     st.warning("请输入消息进行对话。")
