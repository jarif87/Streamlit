import streamlit as st

st.title("Streamlit Text Input Examples")

# Text Input
name = st.text_input("Enter your Name: ")
feedback = st.text_area("Enter your Feedback: ")

# Numeric Input
age = st.number_input("Enter your Age: ")

# Date and Time Input
date = st.date_input("Select a Date: ")
time = st.time_input("Pick a Time: ")

# Color Picker
color = st.color_picker("Pick a Color: ")

# Display inputs
st.write("Name: ", name)
st.write("Feedback: ", feedback)
st.write("Age: ", age)
st.write("Date: ", date)
st.write("Time: ", time)
st.write("Color: ", color)

# HTML code with dynamic color
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{ background-color: powderblue; }}
h1 {{ color: {color}; }}
p {{ color: {color}; }}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
"""

# Render HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)
