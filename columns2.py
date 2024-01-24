import streamlit as st
import pandas as pd

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python") 

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("https://en.m.wikipedia.org/wiki/File:Iris_versicolor_3.jpg")

with col2:
   st.header("Verginica")
   st.image("https://uk.m.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Iris_virginica.jpg")

with col3:
   st.header("Setosa")
   st.image("https://en.m.wikipedia.org/wiki/File:Iris_setosa.JPG")

#import pandas as pd
df=pd.read_csv("./data/iris.csv")

if(st.button("แสดงข้อมูลตัวอย่าง")):
    st.write(df.head(10))
    st.button("ไม่แสดงข้อมูลตัวอย่าง")
else:
    st.button("ไม่แสดงข้อมูลตัวอย่าง")

if(st.button("แสดงข้อมูลสถิติ")):
    #สรุปตามค่าเฉลี่ย กราฟแท่ง
    st.write(df.groupby('variety').mean())
    #chart_data=df.groupby('variety').mean()
    #chart_data.columns
    chart_data = pd.DataFrame(
    {
        "ประเภทดอกไม้": df['variety'],
        "ความกว้าง": df['sepal.width'],
        "ความยาว": df['sepal.length']    
        }
    )
    st.bar_chart(chart_data, x="ประเภทดอกไม้", y=["ความกว้าง","ความยาว"], color=["#FF0000", "#0000FF"])
    st.button("ไม่แสดงข้อมูลสถิติ")
else:
    st.button("ไม่แสดงข้อมูลสถิติ")

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'sepal.width', 'sepal.length', 'petal.width', 'petal.length'
x1=df['sepal.width'].mean()
x2=df['sepal.length'].mean()
x3=df['petal.width'].mean()
x4=df['petal.length'].mean()
sizes = [x1, x2, x3, x4]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

chart = alt.Chart(df).mark_tick().encode(
        x='Horsepower:Q',
        y='Cylinders:O'
    )

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)