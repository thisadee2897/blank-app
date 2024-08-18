import streamlit as st


if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.write("Please log in first.")
    st.experimental_set_query_params(page="login")  # เปลี่ยนเส้นทางไปยังหน้า login

# ตั้งค่า UI
st.title("Home Page")
st.write(f"Welcome, {st.session_state.username}!")

# เพิ่มเนื้อหาอื่นๆ ที่คุณต้องการในหน้า home
