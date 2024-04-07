import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title='RMP Interactive Data Explorer', page_icon='📚')
st.title('📚 RMP Interactive Data Explorer')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the ratings for the professors at Michigan')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app,\n 1. Select genres of your interest in the drop-down selection box and then \n2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')
  
st.subheader('Sentiment Analysis Results')

# Load data
df = pd.read_csv('data/course_review_polarity_emotion_merged.csv')

# Input widgets
## Course selection
course_list = df["class"].unique()
class_selection = st.multiselect('Select class', course_list)

df_selection = df[df["class"].isin(class_selection)]

st.dataframe(df_selection, height= 400, use_container_width= True)



