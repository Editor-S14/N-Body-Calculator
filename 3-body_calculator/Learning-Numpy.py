import numpy as np

array = np.array([1,2,3,4])

array = array*2
print(array)

print(type(array))
#---------------------------------------------#

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                   [['S','T','U'],['V','W','X'],['Y','Z','!']]])
print(array.ndim)
print(array.shape)
print(array[0][2][1])
print(array[0][1][1])
print(array[1][0][2])
print(array[1][0][2])
print(array[1][1][2])
print(array[2][2][2])
word = array[0,2,1] + array[0,1,1] + array[1,0,2] + array[1,0,2] + array[1,1,2] + array[2,2,2]
print(word)

#---------------------------------------------#

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
#array[start:end:step]
print(array[0:2,2:4])