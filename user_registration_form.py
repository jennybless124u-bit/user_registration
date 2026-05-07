import streamlit as st


st.title("User Registration")

cities_in_ghana = [
    "Accra",
    "Kumasi",
    "Tamale",
    "Takoradi",
    "Cape Coast",
    "Tema",
    "Ashaiman",
    "Obuasi",
    "Sunyani",
    "Ho",
    "Koforidua",
    "Bolgatanga",
    "Sekondi-Takoradi",
]

first_name = st.text_input(
    label="First name",
    placeholder="Enter your first name",
)


last_name = st.text_input(
    label="Last name",
    placeholder="Enter your last name",
)

email = st.text_input(
    label="Email",
    placeholder="Enter your email",
)


city = st.selectbox(
    label="City",
    options=cities_in_ghana,
    placeholder="Select your city",
)

mobile_number = st.text_input(
    label="Mobile number",
    placeholder="Enter your mobile number",
)

if st.button("Register"):
    st.success("Registration successful!")
     