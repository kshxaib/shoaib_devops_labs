import streamlit as st

st.title("Chai Maker App")
if st.button("Make chai"):
    st.write("Chai is ready")

add_masala = st.checkbox("Milk")

if add_masala:
    st.write("Masala added")


tea_type = st.radio("Tea Type", ["Green", "Black", "Masala"])
st.write(f"You selected: {tea_type}")

flavour = st.selectbox("Flavour", ["Mint", "Cardamom", "Vanilla"])
st.write(f"You selected: {flavour}")

sugar = st.slider("Sugar", 0, 5, 2)
st.write(f"You selected: {sugar}")

st.number_input("How many cups",1, 10, 1)
st.write(f"You selected: {sugar}")

name = st.text_input("Name", "Enter your name")
if name:
    st.write(f"Welcome {name}! Your order is on the way!")

dob = st.date_input("Date of Birth")
