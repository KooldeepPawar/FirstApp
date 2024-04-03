import streamlit as st 
import pandas as pd
import seaborn as sns 
from datetime import datetime
import matplotlib.pyplot as plt
# Containers

header = st.container()
dataset = st.container()
features = st.container()
model = st.container()

with header :
    st.title("My First Streamlit Project")
    st.text("Lets Start")

with dataset :
    st.header("Displaying Data")
    st.text("Lets Start")

    # import data
    # df = sns.load_dataset("titanic")
    # st.write(df.head(10))
    df=pd.read_csv('BFL Jira.CSV')
    df[['Summary','Issue key','Issue Type','Status','Priority','Resolution','Assignee','Reporter','Creator','Created','Updated','Last Viewed','Resolved','Component/s','Labels']]
    
    st.bar_chart(df["Issue Type"].value_counts())
    st.line_chart(df["Issue Type"].value_counts())

with features :
    st.header("See the features")
    st.text("Hey lets do it")

with model :
    st.header("Check the model")
    st.text("I am happy")


# https://www.youtube.com/watch?v=hy0A6wxlBuM