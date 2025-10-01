import streamlit as st

# Title and subtitle
st.title("🌟 My First Streamlit App")
st.subheader("A simple example without pandas or numpy")

# Text input
name = st.text_input("What's your name?", "Guest")

# Number input
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)

# Checkbox
if st.checkbox("Show greeting"):
    st.write(f"Hello, **{name}**! 👋 You are {age} years old.")

# Button
if st.button("Click me"):
    st.success("🎉 You clicked the button!")

# Select box
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])
st.write(f"Your favorite color is: {color}")
