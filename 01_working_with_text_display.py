import streamlit as st
st.title("Bangladesh is a small country")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is a Text Data")
st.write("This is a stupid idea")

#markdown
st.markdown("This is a markdown")
st.markdown("# This is a markdown heading")
st.markdown("## second heading")
st.markdown("### third heading")
st.markdown("**third heading** this is a bold text")
st.markdown("[MarkDown CheatSheet](https://www.markdownguide.org/cheat-sheet/)")
st.markdown(
    """
1. First item
2. Second item
3. Third item

- First item
- Second item
- Third item

`print("hello world")`

    """
    
)

#Emojis
st.markdown("[Streamlit_Emojis](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)")
st.markdown(":white_check_mark:")
st.markdown(":heavy_plus_sign: :smile:")

st.markdown("## HTML Code")

html_code="""
<!DOCTYPE html>
<html>
<head>
<style>
body {background-color: powderblue;}
h1   {color: darkorange;}
p    {color: navy;}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>

"""
st.markdown(html_code,unsafe_allow_html=True)
st.markdown("---")
st.markdown("# Latex Code")
st.divider()
st.latex("a² – b² = ( a + b ) (a – b)")
st.latex("( a + b )² = a² + 2 ab + b²")
st.latex("( a+ b + c ) ² = a² + b²+ c² + 2ab +2bc + 2ac")
st.latex("( a- b +-c ) ² = a² + b²+ c² – 2ab – 2bc + 2ac")
st.latex("( a + b )³ = a³+ 3a²b + 3b²a + b³")