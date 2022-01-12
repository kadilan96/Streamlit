import streamlit as st
import pandas as pd
import numpy as np

st.title('20171234 박상현')

st.header("Test Header")
st.subheader("Test Subheader")

st.write("Pandas table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

option = st.selectbox(
    '당신의 직책을 선택해주세요.',
     pd.Series(['CEO', 'AI Engineer', 'Intern', 'Product Manager']))
