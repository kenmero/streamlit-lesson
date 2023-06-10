import streamlit as st
import time

st.title('Streamlit 基礎編3')

st.sidebar.write('# プログレスバーの表示')

button = st.button('プログレスバーStart!!')
if button:
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(1, 101):
        latest_iteration.text(f'Iteration {i}')
        bar.progress(i)
        time.sleep(0.1)


    text = st.sidebar.text_input('あなたの趣味を教えてください')
    condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

    'あなたの趣味：', text, 'です'
    'コンディション：', condition

    left_column, right_column = st.columns(2)
    button = left_column.button('右カラムに文字を表示')
    if button:
        right_column.write('ここは右からむです')

    expander1 = st.expander('問い合わせ1')
    expander1.write('問い合わせ1の回答')
    expander2 = st.expander('問い合わせ2')
    expander2.write('問い合わせ2の回答')
    expander3 = st.expander('問い合わせ3')
    expander3.write('問い合わせ3の回答')