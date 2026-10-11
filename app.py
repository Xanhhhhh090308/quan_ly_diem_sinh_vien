#1 tạo data Frame
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Ho_ten' : [ 'Tuyền', 'Linh', 'Anh', 'Tâm', 'Phương', 'Hương', 'Tuấn', 'Khang', 'Đại', 'Hưng' ],
    'chuyen_can' : [2.0, 9.0, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.5],
    'giua_ky' : [5.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'cuoi_ky' : [3.0, 8.5, 6.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.5]
}
df = pd.DataFrame(data)
print(" bảng dữ liệu ban đầu ")
print(df)
#2 tính điểm tổng kết
df['tong_ket'] = (0.2*df['chuyen_can']) + (0.3*df['giua_ky']) + (0.5*df['cuoi_ky'])
df['tong_ket'] = df['tong_ket'].round(2)

print("Bảng dữ liệu kèm điểm tổng kết:")
print(df)
#3. xếp loại sinh viên
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
print("bảng dữ liệu sau khi xếp loại")
print(df)
#4. thống kê điểm
diem_tb_lop = df['tong_ket'].sum()/10
print(f"Điểm tổng kết trung bình của lớp: {diem_tb_lop}")
sv_max = df[df['tong_ket'] == df['tong_ket'].max()]
sv_min = df[df['tong_ket'] == df['tong_ket'].min()]
print("sinh viên cao điểm nhất:")
print(sv_max)
print("sinh viên thấp điểm nhất:")
print(sv_min)
#5 vẽ biểu đồ
plt.figure(figsize=(10, 5))
plt.bar(df['Ho_ten'], df['tong_ket'], color='skyblue', edgecolor='black')
plt.xlabel('Tên Sinh Viên')
plt.ylabel('Điểm Tổng Kết')
plt.title('Biểu đồ Điểm Tổng Kết của Sinh Viên')
plt.ylim(0, 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
st.write("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "Người tạo: Đỗ Xuân Anh - MSSV: 034208005068 </p>",
    unsafe_allow_html=True,
)
