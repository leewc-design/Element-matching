# 🧪 元素記憶學習工具（Streamlit App）

這是一個使用 [Streamlit](https://streamlit.io) 製作的互動式學習工具，幫助學生記憶化學元素的中文名稱與符號。支援 Flashcard 模式與測驗模式，並可記錄學生答題結果。

## 📦 功能特色

- Flashcard 模式：隨機顯示元素符號，點擊按鈕顯示中文名稱。
- 測驗模式：選擇題形式，學生需選出正確的中文名稱。
- 學生姓名輸入：每次答題都會記錄學生姓名。
- 答題記錄匯出：可下載 CSV 檔案，包含時間、姓名、題目、答案與是否答對。

## 🚀 使用方式

### 方法一：本機執行

1. 安裝 Python 與 Streamlit：
   pip install streamlit pandas

2. 執行程式：
   streamlit run app.py

3. 在瀏覽器開啟 http://localhost:8501

### 方法二：部署到 Streamlit Cloud

1. 建立 GitHub repo 並上傳本專案。
2. 前往 streamlit.io/cloud 登入並連接 GitHub。
3. 點選您的 repo → 點選「Deploy」。
4. 即可獲得公開網址，學生可直接使用！

## 📁 檔案說明

- app.py：主程式。
- README.md：專案說明。
- requirements.txt：依賴套件。
- .gitignore：排除不必要的檔案（如 quiz_log.csv）。

## 👨‍🏫 適用對象

- 高中化學課程
- 自主學習學生
- 教師課堂互動輔助工具
