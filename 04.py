a=[0,1,2,3,4,5,6]
print(a[:5]) #from 0 to less than 5th index
print(a[0:5])

print(a[2:]) #onwards 2nd index
print(a[1:5])
print(a[-1])
print(a[-1:]) #onwards from -1th index (nothing here )

print(a[-2:]) #onwards from -2nd index

print(a[:-1]) # from 0 till before -1th index


# output :
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [2, 3, 4, 5, 6]
# [1, 2, 3, 4]
# 6
# [6]
# [5, 6]
# [0, 1, 2, 3, 4, 5]
