import streamlit as st

st.title("Hello streamlit app")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first streamlit app")
st.write("Choose your favorite chai")

chai = st.selectbox("Your fav chai: ", ["Masala chai", "Red chai", "Green chai", "Black chai"])
st.write("You selected: ", chai)

st.success("Success message")