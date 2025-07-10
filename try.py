import streamlit as st
from datetime import datetime

# 页面配置

st.set_page_config(
    page_title="ChatApp",
    page_icon="💬",
    layout="wide",
)


# 显示标题
st.title("鸡鸡歪的专属ai聊天机器人")

# 纪念日计算
start_date = datetime(2024, 6, 1)
today = datetime.today()
days_together = (today - start_date).days

# 计算到下一个6月1日的天数
if today.month < 6 or (today.month == 6 and today.day < 1):
    next_anniversary = datetime(today.year, 6, 1)
else:
    next_anniversary = datetime(today.year + 1, 6, 1)

days_until_next_anniversary = (next_anniversary - today).days

# 左侧栏展示图片
with st.sidebar:
    st.markdown(f"### 在一起已经 {days_together} 天 (*^_^*)")
    st.markdown(f"### 距离下一次周年纪念日还有 {days_until_next_anniversary} 天")
    st.markdown("## 记录甜蜜瞬间")
    st.image("picture/11.png", caption="图片 1")
    st.image("picture/12.png", caption="图片 2")
    st.image("picture/13.png", caption="图片 3")
    st.image("picture/14.png", caption="图片 4")
    st.image("picture/14.png", caption="图片 4")  # 可替换为不同图

# 初始化聊天历史
if "history" not in st.session_state:
    st.session_state.history = []

# 添加自定义CSS样式
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7f6;
    }
    h1 {
        color: #009688;
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 30px;
    }
    .chat-message {
        border-radius: 15px;
        padding: 12px;
        margin-bottom: 12px;
        width: auto;
        min-width: 160px;
        max-width: 85%;
        word-wrap: break-word;
        white-space: normal;
        font-size: 1rem;
        line-height: 1.5;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background-color: #e1f5fa;
        border: 1px solid #b3e5fc;
        color: #01579a;
        align-self: flex-start;
        font-family: 'Tahoma', sans-serif;
    }
    .assistant-message {
        background-color: #f1f8e9;
        border: 1px solid #c5e1a5;
        color: #33691e;
        align-self: flex-end;
        font-family: 'Verdana', sans-serif;
    }
    .stChatInput input {
        border-radius: 25px;
        border: 1px solid #00796b;
        padding-left: 15px;
        font-size: 1rem;
    }
    .user-name, .assistant-name {
        font-size: 14px;
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
    }
    .user-name {
        color: #00796b;
    }
    .assistant-name {
        color: #33691e;
    }
    .footer-text {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 12px;
        color: #888888;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 5px;
        border-radius: 5px;
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True
)

# 显示历史消息
for message in st.session_state.history:
    with st.chat_message(message["role"], avatar="picture/1.jpg" if message["role"] == "user" else "picture/2.jpg"):
        if message["role"] == "user":
            st.markdown('<div class="user-name">我(*´∀`*)（季婧雯）</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="assistant-name">宝宝(*^_^*)（常郅坤）</div>', unsafe_allow_html=True)
        
        role_class = "user-message" if message["role"] == "user" else "assistant-message"
        st.markdown(f'<div class="chat-message {role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# 模拟响应函数
def get_response_material(query, history):
    return "1", "这部分是模拟的检索内容"

# 用户输入处理
if user_input := st.chat_input("请输入消息..."):
    with st.chat_message("user", avatar="picture/1.jpg"):
        st.markdown('<div class="user-name">我(*´∀`*)（季婧雯）</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-message user-message">{user_input}</div>', unsafe_allow_html=True)

    response, material = get_response_material(user_input, st.session_state.history)

    with st.sidebar:
        st.markdown(':balloon::tulip::cherry_blossom::rose: :green[**检索内容：**] :hibiscus::sunflower::blossom::balloon:')
        st.info(material)

    st.session_state.history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant", avatar="picture/2.jpg"):
        st.markdown('<div class="assistant-name">宝宝(*^_^*)（常郅坤）</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-message assistant-message">{response}</div>', unsafe_allow_html=True)

    st.session_state.history.append({"role": "assistant", "content": response})

    if len(st.session_state.history) > 20:
        st.session_state.history = st.session_state.history[-20:]

# 页脚
st.markdown(
    '<div class="footer-text">本聊天ai机器人基于Deepseek_R1基座采用常郅坤与季婧雯聊天语料微调生成，知识产权为二者共有，侵权必追究法律责任</div>',
    unsafe_allow_html=True
)
