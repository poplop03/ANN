import numpy as np

# Khởi tạo trọng số và dữ liệu
w = np.array([-1, 0.5, -0.3])  # [w0, w1, w2]
n = 1.0  # Tốc độ học
epochs = 100  # Số epoch tối đa
d = np.array([1, 0, 1, 1])  # Đầu ra mong muốn
x = np.array([  # Đầu vào (đã thêm bias)
    [-1, 0, 0],
    [-1, 0, 1],
    [-1, 1, 0],
    [-1, 1, 1]
])

# Huấn luyện
for epoch in range(epochs):
    E = 0  # Reset sai số mỗi epoch
    print(f"\nEpoch {epoch + 1}:")

    for i in range(len(x)):
        # Lan truyền thuận
        net = np.dot(x[i], w)
        y = 1 if net > 0 else 0  # Hàm step

        # Cập nhật trọng số
        error = d[i] - y
        w += n * error * x[i]

        # Tính sai số tích lũy
        E = E + 0.5 * (error ** 2)
        print(f"Mẫu {i+1}: Weights = {np.round(w, 2)}, Sai số = {error}")

    # Kiểm tra hội tụ
    if E == 0:
        print("\nHuấn luyện thành công!")
        print(f"Trọng số cuối: {w}")
        break
else:
    print("\nHuấn luyện không hội tụ sau 100 epochs!")