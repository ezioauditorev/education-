import numpy as np
delt = np.array([[1, 1], [2, 3]])
x_delt = np.array([[3, 1], [3, 3]])
y_delt = np.array([[1, 1], [2, 1]])

det1 = delt[0, 0] * delt[1, 1] - delt[0, 1] * delt[1, 0]
det2 = x_delt[0, 0] * x_delt[1, 1] - x_delt[0, 1] * x_delt[1, 0]
det3 = y_delt[0, 0] * y_delt[1, 1] - y_delt[0, 1] * y_delt[1, 0]

print("Дельта:", det1)
print("Дельта x:", det2)
print("Дельта y:", det3)

print(det2 / det1)
print(det3 / det1)
print(det1 * det3)