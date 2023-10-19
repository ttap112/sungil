import random
import time

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

print("이 게임은 다마고치라는 게임입니다")
print("먼저 캐릭터 이름을 설정해주세요")
time.sleep(0.5)

while True:
    pet_name = input("당신의 다마고치 이름을 설정 해주세요. : ")
    pet = Tamagochi(pet_name)
    
    time.sleep(0.5)
    
    print(f'정말로 {pet.name} 으로 하시겠습니다     Y/N')
    Choice = input("Yes | No ")
    
    if Choice == "Yes":
        print(f'당신의 다마고치의 이름은 {pet.name} 입니다')
        time.sleep(0.5)
        break
    elif Choice == "No":
        print("펫 이름을 다시 설정합니다")
        time.sleep(0.5)
    
