import streamlit as st

st.set_page_config(
    page_title="AI HR",  # or "wide"
    initial_sidebar_state="auto",
)

st.title("AI HR")

first_name = st.text_input("Enter First Name")
last_name = st.text_input("Enter Last Name")
email = st.text_input("Enter Email")
department = st.selectbox("Select Your Department",["Frontend","Backend"])
is_manager = st.checkbox("Manager")


if st.button("Send"):
    st.markdown("Hello")