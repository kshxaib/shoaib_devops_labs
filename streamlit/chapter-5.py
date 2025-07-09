import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter the amount in INR", min_value=1)

selected_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][selected_currency]
        converted = rate * amount
        st.success(f"{amount} INR is equal to {converted} {selected_currency}")
    else:
        st.error("Failed to fetch exchange rates")