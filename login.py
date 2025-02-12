import streamlit as st
st.title("detect durian")

col1, col2 = st.columns(2)
with col1:
    st.image("https://www.foodie.com/img/gallery/what-is-durian-and-how-do-you-eat-it/l-intro-1703105258.jpg")
with col2:
    st.write(" ")
    username = st.text_input("ชื่อผู้ใช้")
    password = st.text_input("รหัสผ่าน", type="password")

col1, col2 , col3 , col4 = st.columns(4)
with col1:
    st.write(" ")
with col2:
    st.write(" ")
with col3:
    if st.button("เข้าสู่ระบบ"):
        st.switch_page("pages/detect.py")

@st.dialog("ลงทะเบียนสำหรับผู้ใช้ใหม่")
def register():
    username = st.text_input("ชื่อผู้ใช้", key="username")
    email = st.text_input("Email", key="email")
    password = st.text_input("รหัสผ่าน", type="password", key="password")

    if st.button("Submit"):
        if not username:
            st.error("กรุณากรอกชื่อผู้ใช้")
        if not email:
            st.error("กรุณากรอก Email")
        if not password:
            st.error("กรุณากรอกรหัสผ่าน")
        if username and email and password:
            st.write(f"ลงทะเบียนเสร็จสิ้นสำหรับ {username} ({email})")

with col4:
    if st.button("ลงทะเบียน"):
        register()
