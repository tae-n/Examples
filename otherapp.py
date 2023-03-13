import streamlit as st
import plotly_express as px
import pandas as pd
import matplotlib.pyplot as plt


st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Data Visualization App")

st.sidebar.subheader("Visualization Settings")

uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])

if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot', 'Piechart']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Lineplots':
    st.sidebar.subheader("Line Plot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.histogram(x=x, data_frame=df, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        y = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.box(data_frame=df, y=y, x=x, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Piechart':
    st.sidebar.subheader("Piechart Settings")
    try:
        wedge = st.sidebar.selectbox("Wedge", options=non_numeric_columns)
        size = st.sidebar.selectbox("Size", options=numeric_columns)
     #   fig, ax = plt.subplots()
        wedge_list = df[wedge].tolist()
        size_list = df[size].tolist()
        #ax.pie(size_list, labels=wedge_list, autopct='%1.1f%%', startangle=90)
        #ax.axis('equal')
        #st.pyplot(fig)
        #st.write(wedge)
        df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
        fig = px.pie(df, values=size_list, names=wedge_list)
        fig.show()
    except Exception as e:
        print(e)
 
