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


print("게임 시작 및 설명을 앞서 먼저 자신의 펫 이름을 정해주십시오.")
print("-"*50)
time.sleep(0.5)

# 이름 선택
while True:
    pet_name = input("당신의 다마고치 이름을 설정 해주세요. : ")
    print("-"*50)
    pet = Tamagochi(pet_name)

    time.sleep(0.5)
    cho = 0

    # 이름 결정
    while True:
        try:
            print(f'정말로 {pet.name} 으로 하시겠습니다     Y/N')
            Choice = input("Yes | No : ")
            print("-"*50)
            if Choice == "Yes":
                print(f'당신의 다마고치의 이름은 {pet.name} 입니다')
                print("-"*50)
                time.sleep(0.5)
                cho += 1
                break
            elif Choice == "No":
                print("펫 이름을 다시 설정합니다. ")
                print("-"*50)
                time.sleep(0.5)
                cho = 0
                break
            else:
                raise ValueError("잘못 입력하였습니다.")
        except ValueError:
            print("잘못입력하였습니다. 다시 입력하시오.")
            print("-"*50)
    if cho == 1:
        break

time.sleep(0.5)

#게임 설명
while True:
    try:
        start_choice = input("게임 설명을 들을 실거면 1. \n게임 시작을 하실거면 2. \n선택 : ")
        print("-"*50)
        time.sleep(0.3)
        
        # 게임 규칙
        if start_choice == "1":
            time.sleep(0.5)
            print("-"*50)
            print("다마고치는 펫 육성 시물레이션 게임이며 \n자신이 입력한 명령에 따라 펫이 그에 대한  \n출력을 하여 텍스트로 보여줍니다 \n그리고 행복도, 감염도, 배고픔, 스트레스 \n나이, 친밀도에 따라 여러 이벤트가 나오며 \n특정한 조건을 달성하면 펫이 죽을 수 도 있습니다.")
            print("-"*50)
            time.sleep(3)

        # 게임 시작
        elif start_choice == "2":
            Year = 0
            Month = 0
            Day = 0
            break
        else:
            raise ValueError("에러 발생")
    except ValueError:
        print("잘못 입력하였습니다.")
        print("-"*50)

#게임 시작
while True:
    print("-"*50)
    print(f' {Year}년 {Month}월 {Day}일 경과 ')
    print("-"*50)
    time.sleep(0.5)
    Day += 1

    # 날짜 경과
    if Day == 30:
        Month += 1
        Day = 0
        if Month == 12:
            Year += 1
            Month = 0

    # 부화
    if Day == 15:

        print("알이 부화하였습니다.")
        print("-"*50)
        time.sleep(0.3)
        print(f'{pet.name}은 세상에 처음 나와 당황하고 있습니다.')
        print("-"*50)
        time.sleep(0.3)
        print(f'{pet.name} 위해 무엇을 하시겠습니까.')
        print("-"*50)
        time.sleep(0.3)
        choice1 = input("1. 지켜보기 2. 조심스레 만져보기 \n선택 : ")
        print("-"*50)

        # 선택
        if choice1 == '1':
            time.sleep(0.3)
            print(f'당신은 {pet.name}을 관찰하고 있습니다.')
            print("-"*50)
            time.sleep(0.3)
            print(f'{pet.name}은 당신을 보호자라고 생각하는 중입니다.')
            print("-"*50)
            time.sleep(0.3)
            break
        elif choice1 == '2':
            time.sleep(0.3)
            print(f'당신은 {pet.name}을 조심스레 만져보기로 했습니다')
            print("-"*50)
            time.sleep(0.3)
            break


# 이벤트

# 친밀도에 따른 이벤트

# 행복도에 따른 이벤트
