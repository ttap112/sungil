# 덱에는 3가지의 숫자가 앤덤으로 주어지고 그 숫자를 그대로 뽑아 그리고
# 자신의 덱에 올려 또 다시 카드를 다른 덱에서 뽑아 그리고
# 그걸 다시 내 덱에 올려 그리고 그 과정을 3번 반복하고
# 자신의 덱에서 순서대로 뽑아서 값을 더하고 그 값의 합이 높은 사람이 쇼리다.

import random

# 첫번째 플레이어의 3가지 숫자
plyaer1 = random.sample(range(1, 13), 3)

total1 = []

print("-" * 50)
print(" " * 13, "플레이어1 의 숫자")
print(
    f"                첫번쨰 수 : {plyaer1[0]} \n                두번째 수 : {plyaer1[1]} \n                세번쨰 수 : {plyaer1[2]} "
)

# 두번째 플레이어의 3가지 숫자
player2 = random.sample(range(1, 13), 3)

total2 = []

print("-" * 50)
print(" " * 13, "플레이어2 의 숫자")
print(
    f"                첫번쨰 수 : {player2[0]} \n                두번째 수 : {player2[1]} \n                세번쨰 수 : {player2[2]} "
)

# 서로의 카드를 3번 반복하여 뽑기

for i in range(0, 4):
    total1.append(player2[i])


print(total1)


# 뽑은 카드를 순서대로 더하여 합한 수가 높은 사람이 승리
