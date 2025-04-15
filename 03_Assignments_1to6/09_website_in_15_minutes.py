
import streamlit as st

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# --- Home Page ---
if page == "Home":
    st.title("Welcome to My Streamlit Website 👋")
    st.write("This is a simple website built using Python and Streamlit.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)
    st.success("You can build websites like this in just 15 minutes!")

# --- About Page ---
elif page == "About":
    st.title("About This App")
    st.write("""
    This website is made with [Streamlit](https://streamlit.io).
    It's a Python framework that helps you build interactive web apps super fast.

    **Features of this project**:
    - Built in Python
    - Runs in the browser
    - Supports text, images, inputs
    """)

# --- Contact Page ---
elif page == "Contact":
    st.title("Contact Us 📩")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been received.")
        else:
            st.warning("Please fill all the fields.")
