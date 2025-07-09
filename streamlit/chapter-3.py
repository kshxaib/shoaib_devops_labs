import streamlit as st

st.title("Chai Taste Poll App")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote for Adrak Chai")

if vote1:
    st.success("Thanks for voting masala chai")
elif vote2: 
    st.success("Thanks for voting adrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala Chai", "Adrak Chai"])
st.write(f"Hello {name}, you selected {tea} chai")

with st.expander("Show chai making instructions"):
    st.write("""
    1. Boil water
    2. Add chai powder
    3. Add milk
    4. Add sugar
    5. Enjoy    
""")
    
st.markdown('### Welcome to Chai App')