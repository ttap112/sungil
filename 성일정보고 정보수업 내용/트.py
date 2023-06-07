print(" "*11+("@"))
for i in range(1,12*2,2):
    print((" "*((12*2-1-i)//2))+("*"*i))
print(" "*10+("|||"))
print("")
print("-------------------------------")
print("")

n=int(input("수를 입력하시오 : "))
print("")
print("-------------------------------")
print("")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(i*2-1))
for j in range(n-1, 0, -1):
    print(" "*(n-j)+"*"*(j*2-1))

print("")