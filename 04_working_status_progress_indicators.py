import streamlit as st
import time

st.title(" Working with Status and Progress Indicators")
empty=st.empty()
empty.text("english is international language")
time.sleep(5)
empty.text("bangladesh is a poor country")

st.divider()

progress=st.progress(0)
status_text=st.empty()
for i in range(101):
    time.sleep(0.1)
    progress.progress(i)
    status_text.text("progress {}".format(i))
    
status_text.text("Progress is:  {}".format("Done"))

st.divider()

with st.spinner("Writting......"):
    time.sleep(2)
    
st.success("Process is Done")
st.divider()
st.warning("This is wrong")
st.error("this is error")
st.info("this  is a good information")

st.snow()
st.balloons()