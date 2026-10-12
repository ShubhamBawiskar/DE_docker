# pyrefly: ignore [missing-import]
import streamlit as st

st.set_page_config(page_title="Streamlit App", page_icon="🚀", layout="centered")

st.title("🚀 Welcome to Streamlit!")
st.write("This is a simple dummy Streamlit app running inside Docker.")

# Input example
name = st.text_input("Enter your name:", value="World")

# Interactive button and slider
slider_val = st.slider("Select a number", min_value=1, max_value=100, value=42)

if st.button("Say Hello"):
    st.success(f"Hello, {name}! 🎉")
    st.info(f"You selected the number: {slider_val}")

# Metrics display
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Status", value="Active", delta="Ready")
with col2:
    st.metric(label="Value", value=slider_val)
