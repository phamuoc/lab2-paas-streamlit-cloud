import streamlit as st

st.title("Cloud PaaS Demo")

st.write("Ứng dụng này được xây dựng bằng Python và Streamlit.")

# Tạo ô nhập liệu tên
name = st.text_input("Nhập tên của bạn")

# Kiểm tra nếu người dùng đã nhập tên thì hiển thị lời chào
if name:
    st.write(f"Xin chào {name}!")

st.subheader("Ý nghĩa cloud")
st.write("khi triển khai lên Streamlit Cloud, ứng dụng này sẽ chạy trên nền tảng PaaS")