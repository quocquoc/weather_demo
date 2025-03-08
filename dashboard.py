import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đặt tiêu đề cho ứng dụng
st.title("Dashboard Phân Tích Dữ Liệu")

# Tạo widget để tải file lên
uploaded_file = st.file_uploader("Chọn một file CSV", type=["csv"])

# Xử lý khi có file được tải lên
if uploaded_file is not None:
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(uploaded_file)
    
    # Hiển thị preview dữ liệu
    st.subheader("Xem Trước Dữ Liệu")
    st.write(df.head())
    
    # Hiển thị thông tin tổng quan
    st.subheader("Thông Tin Tổng Quan")
    st.write(df.describe())
    
    # Lọc dữ liệu theo cột
    st.subheader("Lọc Dữ Liệu")
    
    # Lấy danh sách các cột
    columns = df.columns.tolist()
    
    # Tạo selectbox để chọn cột
    selected_column = st.selectbox("Chọn cột để lọc:", columns)
    
    # Lấy các giá trị duy nhất trong cột đã chọn
    unique_values = df[selected_column].unique()
    
    # Tạo selectbox để chọn giá trị
    selected_value = st.selectbox("Chọn giá trị:", unique_values)
    
    # Lọc dữ liệu
    filtered_df = df[df[selected_column] == selected_value]
    
    # Hiển thị dữ liệu đã lọc
    st.write(filtered_df)
    
    # Vẽ biểu đồ
    st.subheader("Vẽ Biểu Đồ")
    
    # Tạo selectbox để chọn cột cho trục x và y
    x_column = st.selectbox("Chọn cột cho trục X:", columns, key="x_axis")
    y_column = st.selectbox("Chọn cột cho trục Y:", columns, key="y_axis")
    
    # Tạo nút để vẽ biểu đồ
    if st.button("Vẽ Biểu Đồ"):
        # Vẽ biểu đồ line_chart dựa trên dữ liệu đã lọc
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Đang chờ tải file lên...")