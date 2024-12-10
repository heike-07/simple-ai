# Simple AI - 简单AI

## 项目简介

`Simple AI` 这是一个基于 Streamlit 和智谱AI（GLM4-Flash 模型）的交互式聊天应用。用户可以与 AI 进行实时对话，应用界面简洁且功能易用。

## 项目功能

- **与 AI 实时聊天**：支持通过输入消息与 AI 进行自然语言对话。
- **对话历史记录**：每次对话都会保存，方便用户查看完整的交互记录。
- **回车键提交**：支持用户输入后按回车键提交消息，简化操作流程。
- **自定义界面样式**：通过 CSS 优化了对话气泡和整体界面布局，提供更好的用户体验。

## 技术栈

- **Python 3.10+**：作为后端开发语言。
- **Streamlit**：用于构建Web应用的框架。
- **zhipu**：清华智谱SDK。
- **Docker**：项目容器化部署。

## 快速使用

如果你不想编译只想用可以访问我的官方地址，也是我自用的。

```bash
https://ai.heike07.cn/
```

## 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/heike07/simple-ai.git
cd simple-ai
```

### 2. 安装依赖

```bash
# 创建虚拟环境（如果没有安装venv，可以先安装）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/MacOS:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3.启动应用

```bash
streamlit run ui.py
```

### 4.运行 Docker 镜像（可选）

如果你希望使用 Docker 运行该应用，可以按以下步骤操作：

#### 构建镜像

```bash
docker build -t simple-ai .
```

#### 运行容器

```bash
docker run -p 8501:8501 simple-ai
```

访问 `http://localhost:8501` 即可在浏览器中看到应用。

## 使用说明

* 输入你要提出的问题，回车即可

## 项目开发

如果你想对该项目进行修改或贡献，可以按照以下步骤进行开发：

1. Fork 本仓库并克隆到本地。
2. 在 `ui.py` 文件中修改功能或界面。
3. 提交 Pull Request

## 联系方式

* ​**GitHub**​: [https://github.com/heike07/simple-ai](https://github.com/heike07/copy-judgment)
* **Email**: dbj2008@yeah.net











