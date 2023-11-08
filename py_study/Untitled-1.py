# 틀 만들기
import random
import time

first = ['게임설명','설명','설명해','설명해줘','게임 설명','게임 설명해줘']
secend = ['시작','게임 시작','게임시작','게임시작 해줘','시작해','ㄱㄱ','ㄱ']

length = 0

# 난이도
def diff():
    global length
    print("난이도를 설정합니다.")
    print("-"*30)
    time.sleep(0.5)
    while True:
        try:
            select = input("쉬움 | 보통 | 어려움 \n선택하십시오 : ")
            print("-"*30)
            if select == "쉬움":
                print("쉬움을 선택하였습니다.")
                print("-"*30)
                length = 10
                break
            elif select == "보통":
                print("보통을 선택하였습니다.")
                print("-"*30)
                length = 20
                break
            elif select == "어려움":
                print("어려움을 선택하였습니다.")
                print("-"*30)
                length = 40
                break
            else:
                raise ValueError
        except ValueError:
            print("잘못된 선택을 하였습니다")
            print("-"*30)
            time.sleep(0.3)
            print("난이도를 다시 설정합니다.")
            print("-"*30)

def DNA_RNA_random():
    global length
    #DNA 랜덤 생성
    DNA=["A","T","G","C"]
    DNA_list =[]

    for i in range(length+1):
        DNA_random = random.choices(DNA)
        DNA_list.append(*DNA_random)

    # RNA 랜덤
    RNA=["A","U","G","C"]
    RNA_list=[]
    for i in range(length+1):
        if DNA_list[i] == "A":
            RNA_list.append(RNA[1])
        elif DNA_list[i] == "T":
            RNA_list.append(RNA[0])
        elif DNA_list[i] == "G":
            RNA_list.append(RNA[3])
        elif DNA_list[i] == "C":
            RNA_list.append(RNA[2])
        

# 게임 시작
print("------|RNA Puzzle|------")
while True:
    try:
        time.sleep(0.5)
        selectFirst = input("설명을 듣겠습니까 아니면 게임을 시작하겠습니까 \n선택하십시오 : ")
        print("-"*30)
        if selectFirst in first:
            time.sleep(0.3)
            print("설명을 시작합니다.")
            print("-"*30)
            time.sleep(1)
            print("이 게임은 핵산을 구조를 활용하여 DNA를 보며 공백에 있는 RNA를 맞추는 게임입니다.")
            time.sleep(1)
            print("이 게임의 목표는 주어진 DNA염기서열을 보고 공백에 있는 RNA을 브릭을 통하여 올바른 염기서열로 맞추는 것입니다.")
            time.sleep(1)
            print("DNA, RNA의 염기의 구성이 이렇게 됩니다.")
            time.sleep(1)
            print("DNA : 아데닌(A), 타이민(T), 구아닌(G), 사이토신(C)")
            time.sleep(1)
            print("RNA : 아데닌(A), 우라실(U), 구아닌(G) 사이토신(C)")
            print("-"*30)

        elif selectFirst in secend:
            print("게임을 시작합니다.")
            print("-"*30)
            diff()
            time.sleep(0.3)
            DNA_RNA_random()

        
        else:
            raise ValueError
    except ValueError:
        time.sleep(0.5)
        print("게임 시작 또는 설명을 선택하지 않고 다른걸 선택하셨거나 \n잘못된 선택을 하였습니다.")
        print("-"*30)



done()
