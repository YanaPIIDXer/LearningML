import numpy as np

# ベクトルの作成
print("・ベクトルの作成")
a = np.array([1, 2, 3])
print(a)  # [1, 2, 3]

# ベクトルの演算
print("・ベクトルの演算")
b = np.array([4, 5, 6])
print("（ベクトル同士の演算）")
print(a + b)    # [5, 7, 9]
print("（スカラー倍）")
print(2 * a)    # [2, 4, 6]

# ベクトルの内積
print("・ベクトルの内積")
print(np.dot(a, b))   # 32
