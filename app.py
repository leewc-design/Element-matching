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

# 答題記錄
if "log" not in st.session_state:
    st.session_state.log = []

st.title("🧪 元素記憶學習工具")

student_name = st.text_input("請輸入學生姓名")

mode = st.radio("選擇模式", ["Flashcard 模式", "測驗模式"])

if mode == "Flashcard 模式":
    element = df.sample(1).iloc[0]
    st.write(f"### 元素符號：**{element['Symbol']}**")
    if st.button("顯示中文名稱"):
        st.write(f"### 中文名稱：**{element['ChineseName']}**")

elif mode == "測驗模式":
    correct = df.sample(1).iloc[0]
    options = df.sample(3)
    options = pd.concat([options, pd.DataFrame([correct])]).sample(frac=1).reset_index(drop=True)

    st.write(f"### 元素符號：**{correct['Symbol']}**")
    choice = st.radio("請選擇正確的中文名稱", options['ChineseName'].tolist())

    if st.button("提交答案"):
        is_correct = choice == correct['ChineseName']
        st.success("✅ 正確！" if is_correct else f"❌ 錯誤，正確答案是：{correct['ChineseName']}")
        st.session_state.log.append({
            "時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "學生姓名": student_name,
            "元素符號": correct['Symbol'],
            "學生選擇": choice,
            "正確答案": correct['ChineseName'],
            "是否答對": "是" if is_correct else "否"
        })

if st.button("匯出答題記錄"):
    log_df = pd.DataFrame(st.session_state.log)
    st.download_button("下載 CSV", log_df.to_csv(index=False), file_name="quiz_log.csv")
