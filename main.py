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
messages = []

def chat_with_model():
    while True:
        # 获取用户输入
        user_input = input("你：")

        if user_input.lower() == "exit":
            print("退出对话")
            break

        # 将用户输入添加到消息历史
        messages.append({"role": "user", "content": user_input})

        # 调用 API 获取模型的响应
        response = client.chat.completions.create(
            model="glm-4-flash",  # 使用的模型
            messages=messages  # 传递对话历史
        )

        # 提取并打印模型的响应
        model_response = response.choices[0].message.content  # 修正此行
        print(f"模型：{model_response}")
        
        # 将模型的响应添加到消息历史
        messages.append({"role": "assistant", "content": model_response})

if __name__ == "__main__":
    print("欢迎与自然语言模型聊天！输入 'exit' 结束对话。")
    chat_with_model()
