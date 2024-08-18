import streamlit as st
import requests

# ฟังก์ชันสำหรับตรวจสอบข้อมูลเข้าสู่ระบบ
def login(username, password):
    url = "http://wastebuy-d.com/oho-planet-waste-buy-api/security/login/login"  # เปลี่ยน URL เป็น URL ของ API ของคุณ
    data = {"user_name": username, "pass_word": password}
    response = requests.post(url, json=data)
    return response.json()

# ตั้งค่า UI
st.title("Login Page")

# ส่วนของฟอร์มการเข้าสู่ระบบ
with st.form(key='login_form'):
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    submit_button = st.form_submit_button(label='Login')

    if submit_button:
        # ตรวจสอบข้อมูลเข้าสู่ระบบ
        result = login(username, password)
        if result.get("success"):  # ตรวจสอบข้อมูลผลลัพธ์ที่รับจาก API
            st.session_state.logged_in = True
            st.session_state.username = username
            st.write("Login successful! Redirecting to home page...")
            st.experimental_set_query_params(page="home")
            st.success("loin Success")
        else:
            st.error("Login failed. Please check your username and password.")
