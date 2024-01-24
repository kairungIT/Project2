import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns(3)




with col1:
   st.header("Versicolor")
   st.image("https://c.pxhere.com/photos/f2/77/iris_flower_purple-1401467.jpg!d")

with col2:
   st.header("Verginica")
   st.image("https://www.fs.usda.gov/wildflowers/beauty/iris/Blue_Flag/images/iris_virginica/iris_virginica_virginica_lg.jpg")

with col3:
   st.header("Setosa")
   st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg")

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