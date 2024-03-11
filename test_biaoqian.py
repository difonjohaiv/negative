# 比较两种方法（传统的双重循环与利用NumPy的广播和高级索引）在执行速度上的差距
import numpy as np
import time

labels = np.random.randint(0, 8, size=18000)  # 假设有1000个标签

# 方法1: 使用传统的Python循环
start_time = time.time()
n = len(labels)
matrix_loop = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        matrix_loop[i, j] = labels[i] == labels[j]
if np.allclose(matrix_loop, matrix_loop.T):
    print("是对称矩阵")
else:
    print("不是对称矩阵!!!!!!!!!")
time_loop = time.time() - start_time

# 方法2: 使用NumPy的广播
start_time = time.time()
matrix_np = labels[:, np.newaxis] == labels
time_np = time.time() - start_time
if np.allclose(matrix_np, matrix_np.T):
    print("是对称矩阵")
else:
    print("不是对称矩阵!!!!!!!!!")


print(f"Loop method took {time_loop:.4f} seconds")
print(f"NumPy method took {time_np:.4f} seconds")
print("速度比:", time_loop / time_np)

