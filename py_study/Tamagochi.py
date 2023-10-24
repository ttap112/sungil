import random
import time
import sys

# 초기화 및 기본 설정


class Tamagochi:
    def __init__(self, name):

        # 이름
        self.name = name

        # 배고픔
        self.hungry = 50

        # 스트레스
        self.stress = 50

        # 피곤함
        self.tired = 50

        # 행복도
        self.happiness = 50

        # 나이
        self.age = 0

        # 친밀도
        self.intimacy = 0

        # 질병
        self.disease = 0

    # 이름 문자열 변환
    def __str__(self):
        return self.name

    # 먹이
    def feed(self):
        self.hungry -= random.randint(5, 10)
        self.happiness += random.randint(-3, 5)
        self.stress += random.randint(-3, 5)
        self.tired += random.randint(-2, 5)
        self.intimacy += random.randint(1, 3)
        self.disease += random.randint(-10, 5)
        if self.disease < 0:
            self.disease = 0

    # 놀이
    def play(self):
        self.hungry -= random.randint(1, 5)
        self.happiness += random.randint(1, 3)
        self.stress += random.randint(1, 4)
        self.tired += random.randint(-5, 2)
        self.intimacy += random.randint(1, 3)
        self.disease += random.randint(-10, 8)
        if self.disease < 0:
            self.disease = 0

    # 잠
    def sleep(self):
        self.hungry += random.randint(-5, -1)
        self.happiness += random.randint(1, 3)
        self.stress += random.randint(1, 2)
        self.tired += random.randint(1, 5)
        self.intimacy += random.randint(1)
        self.disease += random.randint(-5, -1)
        if self.disease < 0:
            self.disease = 0

    # 샤워
    def wash(self):
        self.hungry += random.randint(-3, -1)
        self.happiness += random.randint(1, 2)
        self.stress += random.randint(1, 3)
        self.tired += random.randint(-3, 1)
        self.intimacy += random.randint(1, 2)
        self.disease += random.randint(-10, 0)
        if self.disease < 0:
            self.disease = 0

    # 영화
    def movie(self):

        self.hungry += random.randint(-3, 3)
        self.happiness += random.randint(1, 5)
        self.stress += random.randint(1, 3)
        self.tired += random.randint(-3, 1)
        self.intimacy += random.randint(1, 3)
        self.disease += random.randint(-10, 8)
        if self.disease < 0:
            self.disease = 0

    # 스텟 확인
    def stats(self):
        print(f'이름 : {self.name} \n나이 : {self.age} \n배고픔 : {self.hungry} \n스트레스 : {self.stress} \n피곤함 : {self.tired} \n행복도 : {self.happiness} \n친밀도 : {self.intimacy} \n질병 감염도 : {self.disease}')


# 게임 시작

print(" 이 게임은 다마고치라는 게임입니다")

pet_name = input("당신의 다마고치 이름을 설정 해주세요. : ")
pet = Tamagochi(pet_name)
time.sleep(0.5)

Year = 0
Month = 0
Day = 0

while True:

    print(f'오늘은 {Year}년 {Month}월 {Day}일 입니다.')
    time.sleep(1)
    print(f'당신의 {pet.name}이 태어났습니다.')
    time.sleep(1)

    #선택
    print("\n어떤것을 하시겠습니까.")
    print("1. 밥 주기")
    print("2. 놀기")
    print("3. 영화 ")
    print("4. 잠자기")
    print("5. 샤워")
    print("6. 상태 확인")
    print("7. 종료")


    while True:
        try:
            print("-" * 50)
            choice = input("선택 하십시오 : ")
            print("-"*50)
            if choice == '1':
                pet.feed()
                break
            elif choice == '2':
                pet.play()
                break
            elif choice == '3':
                pet.movie()
                break
            elif choice == '4':
                pet.sleep()
                break
            elif choice == '5':
                pet.wash()
                break
            elif choice == '6':
                pet.stats()
                break
            elif choice == '7':
                sys.exit("다마고치를 종료합니다.")
            else:
                print("올바른 선택지를 선택 하십시오")
        except ValueError:
            print("올바른 선택지를 선택 하십시오")

    #하루 경과
    pet.happiness -= random.randint(1,3)
    pet.tired += random.randint(1,5)
    pet.hungry += random.randint(1,5)
    pet.stress += random.randint(1,5)

    #시간 경과
    Day += 1
    if Day == 30:
        Month += 1
        Day = 0
        if Month == 12:
            Year += 1
            Month = 0



    time.sleep(1)




