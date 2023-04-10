import streamlit as st


st.title("Hi I am Streamlit first web application")
st.subheader('I am your subheader')
st.header('I am header')
st.caption('This is a string that explains something above.')

st.text('Hi i am from text function programmer uses me paragraph text')

st.markdown('**Hello!** World')
st.markdown('**Hello!** *World*')

st.markdown('[Google](https://www.google.co.in/)')
json = {'a':"1,2,3","b":"2.3.4"}
st.json(json)

code = """
print("Hello World")
def fun():
    return a

"""
st.code(code,language='python')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')