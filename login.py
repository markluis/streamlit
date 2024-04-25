import streamlit as st
from time import sleep
from cryptography.fernet import Fernet
from time import sleep

st.title("Login Page")

st.write("Please log in to access data.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

aws_checkbox_result = st.checkbox("Connect to AWS DB", value=True)

if st.button("Log In", type="primary"):

    # if checked, use AWS db
    if aws_checkbox_result:

        conn = st.connection("mysql", type="sql")
        df = conn.query("SELECT * FROM users WHERE username = :username AND password = :password;", ttl=600, params={"username":username, "password":password})

        if df.shape[0] > 0:
            st.session_state.logged_in = True
            st.success("Log in success!")
            sleep(0.5)
            st.switch_page("pages/0_streamlit_main.py")
            
        else:
            st.error("Incorrect username or password!")

    else:
        if (username == 'admin' and password == 'admin'):
            st.session_state.logged_in = True
            sleep(0.5)
            st.switch_page("pages/0_streamlit_main.py")
        else:
            st.error("Incorrect username or password!")


st.markdown("---")
st.write("Powered by Streamlit: A faster way to build and share data apps (https://streamlit.io/)")

        
