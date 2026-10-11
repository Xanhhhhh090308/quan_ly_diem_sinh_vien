import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="Quản lý Điểm Sinh Viên", page_icon="📚", layout="centered")

st.title("📊 Ứng dụng Quản lý & Thống kê Điểm Sinh Viên")
st.write("Trang web hiển thị bảng điểm, xếp loại tự động và biểu đồ trực quan của lớp.")

# 1. Tạo Data Frame
data = {
    'Ho_ten': ['Tuyền', 'Linh', 'Anh', 'Tâm', 'Phương', 'Hương', 'Tuấn', 'Khang', 'Đại', 'Hưng'],
    'chuyen_can': [2.0, 9.0, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.5],
    'giua_ky': [5.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'cuoi_ky': [3.0, 8.5, 6.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.5]
}
df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df['tong_ket'] = (0.2 * df['chuyen_can']) + (0.3 * df['giua_ky']) + (0.5 * df['cuoi_ky'])
df['tong_ket'] = df['tong_ket'].round(2)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return 'giỏi'
    elif diem >= 7.0:
        return 'khá'
    elif diem >= 5.0:
        return 'trung bình'
    else:
        return 'yếu'

df['xep_loai'] = df['tong_ket'].apply(xep_loai)

# Hiển thị bảng dữ liệu lên giao diện web
st.subheader("📋 Bảng điểm chi tiết và Xếp loại")
st.dataframe(df, use_container_width=True)

# 4. Thống kê điểm
diem_tb_lop = df['tong_ket'].mean() # Dùng hàm .mean() chuẩn xác hơn tính tổng chia 10

st.subheader("📈 Thống kê chung")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Điểm TB toàn lớp", value=f"{diem_tb_lop:.2f}")

sv_max = df[df['tong_ket'] == df['tong_ket'].max()]
sv_min = df[df['tong_ket'] == df['tong_ket'].min()]

with col2:
    max_score = sv_max['tong_ket'].values[0]
    st.metric(label="Điểm cao nhất lớp", value=f"{max_score}")

st.write("**🌟 Sinh viên cao điểm nhất:**")
st.dataframe(sv_max, use_container_width=True)

st.write("**⚠️ Sinh viên thấp điểm nhất:**")
st.dataframe(sv_min, use_container_width=True)

# 5. Vẽ biểu đồ hiển thị lên web
st.subheader("📊 Biểu đồ Điểm Tổng Kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Ho_ten'], df['tong_ket'], color='skyblue', edgecolor='black')
ax.set_xlabel('Tên Sinh Viên', fontsize=12)
ax.set_ylabel('Điểm Tổng Kết', fontsize=12)
ax.set_title('Biểu đồ Điểm Tổng Kết của Sinh Viên', fontsize=14)
ax.set_ylim(0, 10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Đưa biểu đồ vào Streamlit
st.pyplot(fig)

# Footer thông tin người tạo
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 14px; font-weight: bold;'>"
    "Người tạo: Đỗ Xuân Anh - MSSV: 034208005068</p>", 
    unsafe_allow_html=True
)
