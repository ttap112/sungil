import random

#첫번째 플레이어
player1 = random.sample(range(1, 13), 3)

total_one = []

for i in range(3):
    total_one.append(player1[i])

result_one=(sum(total_one))

#두번째 플레이어
player2 = random.sample(range(1, 13), 3)

total_two = []

for i in range(3):
    total_two.append(player2[i])
    
result_two=(sum(total_two))

# 출력값

print("     플레이어1의 수     |     플레이어2의 수")
print("-" * 50)

print("    첫번째 숫자 : ?", end=" ")
print("    |", end=" ")
print("    첫번째 숫자 : ?")

print("    두번째 숫자 : ?", end=" ")
print("    |", end=" ")
print("    두번째 숫자 : ?")

print("    세번째 숫자 : ?", end=" ")
print("    |", end=" ")
print("    세번째 숫자 : ?")
print("-" * 50)

print("        세가지의 숫자를 덱에 저장합니다.")
print("-" * 50)

print("      각 플레이어의 첫번째 수를 공개합니다")
print("-" * 50)

# 첫번째 카드 공개
print("    플레이어1의 수      |    플레이어2의 수")
print("-" * 50)

for j in range(1):
    player1_value = total_one[j]
    player2_value = total_two[j]

    print(f'    {j+1}번째 수 : {player1_value:>2}       |    {j+1}번째 수 : {player2_value:>2}')

print("    2번째 수 : ?", end=" ")
print("       |", end=" ")
print("   2번째 수 : ?")

print("    3번째 수 : ?", end=" ")
print("       |", end=" ")
print("   3번째 수 : ?")


#두번째 

print("-" * 50)
print("      각 플레이어의 두번째 수를 공개합니다")
print("-" * 50)

print("    플레이어1의 수      |    플레이어2의 수")
print("-" * 50)

for j in range(2):
    player1_value = total_one[j]
    player2_value = total_two[j]

    print(f'    {j+1}번째 수 : {player1_value:>2}       |    {j+1}번째 수 : {player2_value:>2}')

print("    3번째 수 : ?", end=" ")
print("       |", end=" ")
print("   3번째 수 : ?")
print("-" * 50)

# 세번째

print("      각 플레이어의 세번째 수를 공개합니다")
print("-" * 50)

print("    플레이어1의 수      |    플레이어2의 수")
print("-" * 50)

for j in range(3):
    player1_value = total_one[j]
    player2_value = total_two[j]

    print(f'    {j+1}번째 수 : {player1_value:>2}       |    {j+1}번째 수 : {player2_value:>2}')


print("-" * 50)
print("      각 플레이어의 수들을 합하는 중입니다")
print("-" * 50)

if result_one > result_two:
    print("        첫번째 플레이어가 우승하였습니다.")
    print("-" * 50)
elif result_one < result_two:
    print("        두번째 플레이어가 우승하였습니다.")
    print("-" * 50)
else:
    print("         서로의 수가 같아 비겼습니다.")
    print("-" * 50)





