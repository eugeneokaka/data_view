import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# st.write("hello ")
# st.write({"key":["one","two"]})
st.title("simple Data dashbord")
uploadef_file=st.file_uploader("choose a csv file",type="csv")

if uploadef_file is not None:
    df=pd.read_csv(uploadef_file)
    st.subheader("Data privew")
    st.write(df.head())
    # st.dataframe(df)
    st.subheader('Data summary')
    st.write(df.describe())
    st.subheader("filter Data")
    columns=df.columns.tolist()
    
    selected_coulum=st.selectbox("select column",columns)
    # st.write(columns)
    # st.write(selected_coulum)
    unique_values=df[selected_coulum].unique()
    selected_value=st.selectbox('select value',unique_values)
    filterd_df=df[df[selected_coulum]==selected_value]
    st.write(filterd_df)
    st.subheader('plot data')
    x=st.selectbox('select x-axis',columns)
    y=st.selectbox('select y-axis',columns)
    if st.button("Generate Plot"):
        st.line_chart(filterd_df.set_index(x)[y])
    else:
        st.write("waiting on file upload..")
    
