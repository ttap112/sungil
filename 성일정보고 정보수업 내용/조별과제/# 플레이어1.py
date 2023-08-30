# 플레이어1

import random
import time

MyDeck1 = []
RandomDeck1 = random.sample(range(1, 11), 10)

print("게임을 시작합니다.")
print("-"*50)
time.sleep(1)


print("□ □ □ □ □")
print("□ □ □ □ □")
print("-"*50)
time.sleep(1)

for i in range(1,4) :
    #print("10개의 숫자 중 뽑을 숫자을 선택해주세요.")
    time.sleep(1)
    choise = int(input("10개의 숫자 중 뽑을 숫자을 선택해주세요. : "))
    print("-"*50)
    if choise > 10 :
        print("올바른 숫자를 입력해주세요.")
        print("-"*50)
        time.sleep(1)
    MyDeck1.append(RandomDeck1[choise-1])

num1 = MyDeck1.pop()
num2 = MyDeck1.pop()
num3 = MyDeck1.pop()

time.sleep(1)
print("당신이 뽑은 세 가지의 숫자를 공개합니다.")
print("-"*50)
time.sleep(1)
print("첫 번째 숫자 :",num1)
time.sleep(1)
print("두 번째 숫자 :",num2)
time.sleep(1)
print("세 번째 숫자 :",num3)
print("-"*50)
time.sleep(1)
print("세 숫자의 총합은",num1 + num2 + num3,"입니다.")
time.sleep(1.5)
print("-"*50)
total1=num1+num2+num3

#플레이어2
time.sleep(1)
print("□ □ □ □ □")
print("□ □ □ □ □")
time.sleep(1)
MyDeck2 = []
RandomDeck2 = random.sample(range(1, 11), 10)
print("-"*50)

for i in range(1,4) :
    #print("10개의 숫자 중 뽑을 숫자을 선택해주세요.")
    time.sleep(1)
    choise = int(input("10개의 숫자 중 뽑을 숫자을 선택해주세요. : "))
    print("-"*50)
    if choise > 10 :
        print("올바른 숫자를 입력해주세요.")
        print("-"*50)
        time.sleep(1)
    MyDeck2.append(RandomDeck2[choise-1])

num4 = MyDeck2.pop()
num5 = MyDeck2.pop()
num6 = MyDeck2.pop()

print("당신이 뽑은 세 가지의 숫자를 공개합니다.")
print("-"*50)
time.sleep(1)
print("첫 번째 숫자 :",num4)
time.sleep(1)
print("두 번째 숫자 :",num5)
time.sleep(1)
print("세 번째 숫자 :",num6)
print("-"*50)
time.sleep(1)
print("세 숫자의 총합은",num4 + num5 + num6,"입니다.")

total2=num4+num5+num6

# 플레이어 합 계산후 승패 결정

if total1>total2:
    time.sleep(1)
    print("-"*50)
    print("1번 승리")
elif total1<total2:
    time.sleep(1)
    print("-"*50)
    print("2번 승리")
else:
    time.sleep(1)
    print("-"*50)
    print("무승부")