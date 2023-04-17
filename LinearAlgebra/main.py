import numpy as np

##
#  ベクトルの作成
##
print("・ベクトルの作成")
a = np.array([1, 2, 3])
print(a)  # [1, 2, 3]

##
#  ベクトルの演算
##
print("・ベクトルの演算")
b = np.array([4, 5, 6])

# ベクトル同士の演算
# 同じ軸の数値同士で演算を行う
print("（ベクトル同士の演算）")
print(a + b)    # [5, 7, 9]

# スカラー倍
# 全ての軸に対してスカラー値を乗算する
print("（スカラー倍）")
print(2 * a)    # [2, 4, 6]

##
# ベクトルの内積
# 内積：２つのベクトルの積の総和
##
print("・ベクトルの内積")
print(np.dot(a, b))   # 32

##
# ベクトルの外積
# 外積：２つのベクトルに垂直なベクトルを求める
##
print("・ベクトルの外積")
print(np.cross(a, b)) # [-3  6 -3]
