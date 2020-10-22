import numpy as np

np1 = np.array([1, 2, 3, 4])
x = type(np1)
print(x)
print(np1)
Mat1 = np.array([[1, 2], [3, 4]])
print(Mat1)
print(np1.shape)
print(Mat1.shape)
print(Mat1.dtype)  # here i have to continue with numpy tutorial
print(Mat1[0, 0])
Mat1[0, 0] = 5
print(Mat1)
Mat2 = np.arange(0, 10, 1)
print(Mat2)
Mat3 = np.linspace(0, 10, 20)
print(Mat3)
print(Mat3.shape)  # this a one dimensional  array and not a matrix
Mat4 = np.random.rand(5, 5)
print(Mat4)
Mat5 = np.random.randn(5, 5)
print(Mat5)
print(Mat5[0:3, :])
# getting all the rows with index 0,1,2 excluding 3 amd colon with no parameters means all the columns
