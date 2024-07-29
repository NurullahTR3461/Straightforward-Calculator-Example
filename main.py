def add(num4,num5):
    return num4 + num5

def subsract(num4,num5):
    return num4 - num5

def divide(num4,num5):
    return num4/num5

def multiply(num4,num5):
    return num4*num5

print("Please decide for the choice")
print("1.add")
print("2.substract")
print("3.divide")
print("4.multiply")

select = input("Please you need to pick(1/2/3/4):")

num4 = int(input("please enter your number"))
num5 = int(input("please you need to put your another number"))

if select == "1":
    print(num4,"+",num5,"=",add(num4,num5))
elif select == "2":
    print(num4,"-",num5,"=",subsract(num4,num5))
elif select == "3":
    print(num4,"/",num5,"=",divide(num4,num5))
elif select == "4":
    print(num4,"*",num5,"=",multiply(num4,num5))
else:
    print("you wrote false values")
