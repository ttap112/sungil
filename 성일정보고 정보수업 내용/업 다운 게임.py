import random 

rd=random.randrange(1,101,1)
c=0

while True:
    cnt=int(input())
    c+=1
    if cnt==rd:
        print(f'총 {c}를 시도하여 {rd}를 맞췄습니다')
        break
    elif cnt<rd:
        print("UP")
    elif cnt>rd:
        print("DOWN")

