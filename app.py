import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title(':sunglasses:')

df = pd.read_csv('./titanic_train.csv')

st.subheader('타이타닉 데이터셋')
st.write(df)

st.subheader('세대별 남여 승객수')
# Stacked bar chart
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women') # bottom속성

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

st.pyplot(fig)