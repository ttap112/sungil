import random

queue = []
result = []

print("-"*50)

for i in range(0,3):
    queue.append(random.randint(1,10))


print("1번 플레이어가 뽑은 세 가지 숫자는",queue[0],queue[1],queue[2],"입니다.")
print("숫자의 총합은",queue[0]+queue[1]+queue[2],"입니다.")
print("카드 뭉치에",queue[0],queue[1],queue[2],"를 추가합니다.")
print("-"*50)


for i in range(0,3):
    queue.append(random.randint(1,10))

result.append(queue)

print(result)


# 덱에는 3가지의 숫자가 앤덤으로 주어지고 그 숫자를 그대로 뽑아 그리고 자신의 덱에 올려 또 다시 카드를 다른 덱에서 뽑아 그리고 그걸 다시 내 덱에 올려 그리고 그 과정을 3번 반복하고
# 자신의 덱에서 순서대로 뽑아서 값을 더하고 그 값의 합이 높은 사람이 쇼리다.