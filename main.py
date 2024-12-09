from zhipuai import ZhipuAI

# 初始化 ZhipuAI 客户端，替换为你自己的 API Key
client = ZhipuAI(api_key="e8709e6c1fcb2517ff50f4f45732ccac.IDVcvnMTLhfcAv43")

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
        model_response = response.choices[0].message.content
        print(f"模型：{model_response}")
        
        # 将模型的响应添加到消息历史
        messages.append({"role": "assistant", "content": model_response})

if __name__ == "__main__":
    print("欢迎与模型聊天！输入 'exit' 结束对话。")
    chat_with_model()
