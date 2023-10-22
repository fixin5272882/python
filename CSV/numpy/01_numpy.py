import numpy as np

# 創建一個 NumPy 數組
numpy_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 使用 numpy.savetxt() 函數將數組寫入 CSV 文件
np.savetxt('data.csv', numpy_data, delimiter=',')
# 打印數據
print(numpy_data)


