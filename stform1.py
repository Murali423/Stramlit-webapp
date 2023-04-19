import streamlit as st
import time as ts
from  datetime import time
import datetime 
from matplotlib import pyplot as plt
import numpy as np

st.markdown("""
<style>
.css-9s5bis.edgvbvh3
{
    visibility:hidden;
}
</style>
""",unsafe_allow_html=True)
st.markdown("""
<h1> User Registration Form </h1>
""",unsafe_allow_html=True)

st.sidebar.write('Hello this is my sidebar')

form = st.form('form1')
name = form.text_input("first name")
sub = form.form_submit_button('Submit')

if sub:
    st.write('Enter values is: ',name)

with st.form('myform'):
    d = {}
    col1,col2 = st.columns(2)
    d['first Name']=col1.text_input('First Name')
    d['second name']=col2.text_input('Second Name')
    d['email']=st.text_input('EMail')
    d['password']=st.text_input('Password')
    d['confirm password']=st.text_input('Confirm password')
    su = st.form_submit_button('submit')
    if su:
        if d['first Name']=="" and d['second name']=="":
            st.warning('Please fill the fields')
        else:
            st.success('successfully submitted')
opt = st.sidebar.radio("select any graph",options=('Line','Bar','H-Bar'))
bar_x = np.array([1,2,3,4,5,6])
x = np.linspace(0,10,100)
if opt == 'Line':
    st.markdown("<h1 style='text-align: center';>Line Graph</h1>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    st.write(fig)
elif opt == "Bar":
    st.markdown("<h1 style='text-align: center';>Bar Graph</h1>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.bar(bar_x,bar_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align: center';>Horizantal Graph</h1>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.barh(bar_x*10,bar_x)
    st.write(fig)