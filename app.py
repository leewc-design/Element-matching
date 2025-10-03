import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 元素資料
data = {
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
               'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
               'Br', 'I'],
    'ChineseName': ['氫', '氦', '鋰', '鈹', '硼', '碳', '氮', '氧', '氟', '氖',
                    '鈉', '鎂', '鋁', '矽', '磷', '硫', '氯', '氬', '鉀', '鈣',
                    '溴', '碘']
}
df = pd.DataFrame(data)

# 初始化 session state
if "log" not in st.session_state:
    st.session_state.log = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "options" not in st.session_state:
    st.session_state.options = None
if "answered" not in st.session_state:
    st.session_state.answered = False

st.title("🧪 元素記憶學習工具")

student_name = st.text_input("請輸入學生姓名")

mode = st.radio("選擇模式", ["Flashcard 模式", "測驗模式"])

if mode == "Flashcard 模式":
    element = df.sample(1).iloc[0]
    st.write(f"### 元素符號：**{element['Symbol']}**")
    if st.button("顯示中文名稱"):
        st.write(f"### 中文名稱：**{element['ChineseName']}**")

elif mode == "測驗模式":
    if not st.session_state.answered:
        st.session_state.current_question = df.sample(1).iloc[0]
        options = df.sample(3)
        st.session_state.options = pd.concat([options, pd.DataFrame([st.session_state.current_question])]).sample(frac=1).reset_index(drop=True)

    st.write(f"### 元素符號：**{st.session_state.current_question['Symbol']}**")
    choice = st.radio("請選擇正確的中文名稱", st.session_state.options['ChineseName'].tolist(), key="quiz_choice")

    if st.button("提交答案") and not st.session_state.answered:
        correct = st.session_state.current_question['ChineseName']
        is_correct = choice == correct
        st.session_state.answered = True
        st.session_state.total += 1
        if is_correct:
            st.session_state.score += 1
            st.success("✅ 正確！")
        else:
            st.error(f"❌ 錯誤，正確答案是：{correct}")
        st.session_state.log.append({
            "時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "學生姓名": student_name,
            "元素符號": st.session_state.current_question['Symbol'],
            "學生選擇": choice,
            "正確答案": correct,
            "是否答對": "是" if is_correct else "否"
        })

    if st.session_state.answered:
        if st.button("下一題"):
            st.session_state.answered = False

    st.write(f"目前答對：{st.session_state.score} / {st.session_state.total}")

    if st.button("重設分數"):
        st.session_state.score = 0
        st.session_state.total = 0
        st.session_state.log = []
        st.session_state.answered = False
        st.success("✅ 分數已重設")

    if st.button("匯出答題記錄"):
        log_df = pd.DataFrame(st.session_state.log)
        st.download_button("下載 CSV", log_df.to_csv(index=False), file_name="quiz_log.csv")

    if st.session_state.log:
        st.write("📋 歷史答題記錄")
        st.dataframe(pd.DataFrame(st.session_state.log))
