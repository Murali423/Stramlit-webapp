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

img = st.file_uploader('Upload image',type=['.png','.jpg'])

if img is not None:
    st.image(img)

vid = st.file_uploader('Upload your video',type=".mp4")

if vid is not None:
    st.video(vid)

st.slider("This is slider")

val = st.slider('this is test slider',min_value=0,max_value=150,value=60)
print(val)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


txt = st.text_input('the current value:')
print(txt)


# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)

number = st.number_input('Please enter the number')
print(number)

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write(txt)

dat = st.date_input('Plese enter your DOB:')
st.write(dat)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

#progress bar
def converter(val):
    m,s,ms = val.split(":")
    t_s = int(m)*60+int(s)+int(ms)/1000
    return t_s

val = st.time_input('Set Timer', value = time(0,0,0))
print(type(val))
if str(val) == "00:00:00":
    st.write("please set timer")
else:
    st.write('performing the function')
    t = converter(str(val))
    bar = st.progress(0)
    per = t/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i)+" %")
        ts.sleep(per)