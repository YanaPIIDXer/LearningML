import numpy as np

##
# 行列の作成
##
print("・行列の作成")
A = np.array([[1, 2, 3], [4, 5, 6]])
# [[1, 2, 3]
#  [4, 5, 6]]
print(A)

##
# 行列の演算（積）
##
print("・行列の演算（積）")
B = np.array([[1, 2], [3, 4], [5, 6]])
# [[22, 28
#   49, 64]]
print(np.dot(A, B))

##
# 行列の転置
##
print("・行列の転置")
# [[1 4]
#  [2 5]
#  [3 6]]
print(A.T)

##
# 逆行列
##
print("・逆行列")
C = np.array([[1, 2], [3, 4]])
# [[-2 1
#   1.5 -0.5]]
print(np.linalg.inv(C))
