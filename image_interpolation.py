import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 讀取圖片
image_path = r"C:\Users\88691\image_interpolation\64.jpg"  # 替換為你的圖片路徑
image = cv2.imread(image_path)

# 獲取原始圖片的尺寸
original_height, original_width = image.shape[:2]

# 設置放大的尺寸
new_size = (1280, 1280)

# 使用三種插值方法進行放大
nearest_neighbor = cv2.resize(image, new_size, interpolation=cv2.INTER_NEAREST)
bilinear = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)
bicubic = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)

# 顯示圖片比較
plt.figure(figsize=(20, 15))  # 增加整體圖片大小

# 原始圖片
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image (64x64)')
plt.axis('off')

# 最近鄰插值
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(nearest_neighbor, cv2.COLOR_BGR2RGB))
plt.title('Nearest Neighbor Interpolation')
plt.axis('off')

# 雙線性插值
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(bilinear, cv2.COLOR_BGR2RGB))
plt.title('Bilinear Interpolation')
plt.axis('off')

# 雙三次插值
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(bicubic, cv2.COLOR_BGR2RGB))
plt.title('Bicubic Interpolation')
plt.axis('off')

# 添加註解
plt.figtext(0.5, -0.05, '64x64 Image Resized to 1280x1280', ha='center', va='center', fontsize=12)

# 顯示圖表
plt.tight_layout()
plt.subplots_adjust(bottom=0.05, hspace=0.1)  # 調整底部邊距和垂直間距
plt.show()

# 創建 output 資料夾（如果不存在）
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

# 保存結果到 output 資料夾
cv2.imwrite(os.path.join(output_folder, 'nearest_neighbor.png'), nearest_neighbor)
cv2.imwrite(os.path.join(output_folder, 'bilinear.png'), bilinear)
cv2.imwrite(os.path.join(output_folder, 'bicubic.png'), bicubic)

print("Images saved to the 'output' folder.")
