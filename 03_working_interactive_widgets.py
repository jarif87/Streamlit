import streamlit as st

st.title("Working with Interactive Widget")
st.divider()
button=st.button("Click Me")
if button:
    st.write("You Clicked Me")

checkbox=st.checkbox("Check Me Here For Enable Something")
if checkbox:
    st.write("Checkbox is Clicked")
    
radio=st.radio("Choose an option :",["NLP","ML","DL","CNN","RNN"])
st.write("You have selected: ",radio)
st.divider()
box=st.selectbox("Choose an option :",["NLP","ML","DL","CNN","RNN"])
st.write("You have selected: ",box)
st.divider()
multiselect=st.multiselect("Choose Multiple option :",["NLP","ML","DL","CNN","RNN"])
st.write("You have selected: ",multiselect)

rating=st.slider("select your rating: ",min_value=1.0,max_value=5.0,step=0.5)
st.write("Your rating is: ",rating)

st.divider()
select_slider=st.select_slider("Choose a value :",["NLP","ML","DL","CNN","RNN"])
st.write("You have selected: ",select_slider)