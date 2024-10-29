import streamlit as st
import pandas as pd


st.title(':sunglasses:')

df = pd.read_csv('./titanic_train.csv')

st.subheader('타이타닉 데이터셋')
st.write(df)