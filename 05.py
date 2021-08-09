# Printing "n" no of fruits :

# method 1

f1=input("enter the fruit1:")
f2=input("enter the fruit2:")
f3=input("enter the fruit3:")
f4=input("enter the fruit4:")
f5=input("enter the fruit5:")
f6=input("enter the fruit6:")
f7=input("enter the fruit7:")
my_fruit=[f1,f2,f3,f4,f5,f6,f7]
print(my_fruit)

# method 2:

lst=[]
x=int(input("enter the number of fruits: "))
for i in range(x):
	f=input(f"enter the fruit {i+1}:")
	lst.append(f)
print(f"list of fruits are {lst}")
