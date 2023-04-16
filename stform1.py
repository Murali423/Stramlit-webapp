import streamlit as st
import time as ts
from  datetime import time
import datetime 

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
    st.write("Entered deatils are :",d)