#기본
import random
import time

result1=[]
result2=[]

MyDeck1 = []
RandomDeck1 = random.sample(range(1, 11), 10)

MyDeck2 = []
RandomDeck2 = random.sample(range(1, 11), 10)

#카드

card = r""" 
 -----   -----   -----   -----   -----    
|     | |     | |     | |     | |     |
|  1  | |  2  | |  3  | |  4  | |  5  |
|     | |     | |     | |     | |     |
 -----   -----   -----   -----   -----
|     | |     | |     | |     | |     |
|  6  | |  7  | |  8  | |  9  | |  j  |
|     | |     | |     | |     | |     |
 -----   -----   -----   -----   -----
 """

cards = [
    r"""
 _____
|A    |
|  ♠  |
|    A|
 -----
""",
    r"""
 _____
|2    |
|  ♠  |
|    2|
 -----
""",
    r"""
 _____
|3    |
|  ♠  |
|    3|
 -----
""",
    r"""
 _____
|4    |
|  ♠  |
|    4|
 -----
""",
    r"""
 _____
|5    |
|  ♠  |
|    5|
 -----
""",
    r"""
 _____
|6    |
|  ♠  |
|    6|
 -----
""",
    r"""
 _____
|7    |
|  ♠  |
|    7|
 -----
""",
    r"""
 _____
|8    |
|  ♠  |
|    8|
 -----
""",
    r"""
 _____
|9    |
|  ♠  |
|    9|
 -----
""",
    r"""
 _____
|10   |
|  ♠  |
|   10|
 -----
""",
    r"""
 _____
|J    |
|  ♠  |
|    J|
 -----
""",
    r"""
 _____
|Q    |
|  ♠  |
|    Q|
 -----
""",
    r"""
 _____
|K    |
|  ♠  |
|    K|
 -----
"""
]

 #랜덤한 숫자

# 플레이어 1
print("게임을 시작합니다.")
print("-" * 50)
time.sleep(1)

print(card)

print("-" * 50)
time.sleep(1)


# 카드를 선택하여 중복값 여부 확인후 카드를 덱에 추가
while len(MyDeck1) < 3:
    choise = input("10개의 숫자 중 뽑을 숫자을 선택해주세요. : ")
    print("-" * 50)
    try:
        choise = int(choise)  # 입력값을 정수로 변환
        if choise in RandomDeck1 and choise not in MyDeck1:  # 중복된 값이 없을 때만 추가
            MyDeck1.append(choise)
        else:
            print("유효하지 않거나 이미 입력된 숫자입니다. 다른 숫자를 입력하세요.")
            print("-" * 50)
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        print("-" * 50)

# 덱에 있는 카드를 차례대로 출력
for index in MyDeck1:
    if 0 <= index < len(cards):  # 입력한 숫자가 유효한 인덱스 범위 내에 있는지 확인
        MyDeck1 = cards[index]
        print(MyDeck1) 
        print("-"*50)
        time.sleep(0.5)

# 덱에 있는 카드(수)들을 합산
for i in range(3):
    result1.append(MyDeck1[i])

num1 = result1.pop()
print(num1)
num2 = result1.pop()
print(num2)
num3 = result1.pop()
print(num3)

total1=num1+num2+num3

#플레이어2
print("게임을 시작합니다.")
print("-" * 50)
time.sleep(1)

print(card)

print("-" * 50)
time.sleep(1)

# 카드를 선택하여 중복값 여부 확인후 카드를 덱에 추가
while len(MyDeck2) < 3:
    choise = input("10개의 숫자 중 뽑을 숫자을 선택해주세요. : ")
    print("-" * 50)
    try:
        choise = int(choise)  # 입력값을 정수로 변환
        if choise in RandomDeck2 and choise not in MyDeck2:  # 중복된 값이 없을 때만 추가
            MyDeck2.append(choise)
        else:
            print("유효하지 않거나 이미 입력된 숫자입니다. 다른 숫자를 입력하세요.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

# 덱에 있는 카드를 차례대로 출력
for index in MyDeck2:
    if 0 <= index < len(cards):  # 입력한 숫자가 유효한 인덱스 범위 내에 있는지 확인
        MyDeck2 = cards[index]
        print(MyDeck2) 
        print("-"*50)
        time.sleep(0.5)

# 덱에 있는 카드(수)들을 합산
for i in range(3):
    result2.append(MyDeck2[i])

num4 = result2.pop()
print(num4)
num5 = result2.pop()
print(5)
num6 = result2.pop()
print(6)

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