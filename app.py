import streamlit as st

'''
st.title("掛け算アプリ")

# 数値入力
a = st.number_input("1つ目の数を入力してください", value=1)
b = st.number_input("2つ目の数を入力してください", value=1)

# 計算
result = a * b

# 結果表示
st.write(f"結果: {a} × {b} = {result}")
'''

import streamlit as st

count = 0
if st.button("カウントアップ"):
    count += 1
st.write("カウント:", count)