soda={
    "콜라":1900,
    "밀키스":1010,
    "몬스터":2300,
    "사이다":1700
    }
aa,ss,dd,qq,ww,ee,rr,tt,yy=10000,5000,1000,500,100,50,10,5,1
a,s,d,q,w,e,r,t,y=0,0,0,0,0,0,0,0,0

min_money=min(soda.values())

roading=0
time=0

print("자판기를 실행합니다")
print("--------------------------------------")
while True:
    try:
        print("어서오세요 천재와 멍청이들의 자판기입니다")
        print("--------------------------------------")
        start=input('자판기를 사용하실거면 1번 입력하시고 종료하실거면 2번을 입력해주세요 ')
        
        if start=="1":
            
            print("--------------------------------------")
            cc=int(input("구매하실거면 1번 입력하시오 "))
                
            if cc==9630: 
                print("관리자로 접근합니다")
                print("--------------------------------------")
                while roading<=100:
                    print(roading,"로딩중")
                    roading+=1
                print("--------------------------------------")
                print("로딩완료")
                print("--------------------------------------")
                while True: 
                    try:
                        admin_password=int(input("수정을 하실거면 120 추가 하실거면 110 초기화 하실거면 100 종료하실거면 140 입력하세요 "))
                        print("--------------------------------------")
                        if admin_password==100:
                            soda={
                        "콜라":1900,
                        "밀키스":1010,
                        "몬스터":2300,
                        "사이다":1700
                            }
                            for i in soda:
                                print(i,soda[i])
                            print("--------------------------------------")

                        elif admin_password == 120 :
                            print("수정")
                            for i in soda:
                                print(i, soda[i])
                            ab = input("중에 어떤걸 수정하시겠습니까 ")
                            if ab in soda:
                                aa = input("메뉴 이름을 바꾸시겠습니까 아니면 가격을 바꾸겠습니까? ")
                                if aa == "메뉴":
                                    me = str(input("바꾸고 싶은 이름 "))
                                    if me not in soda:
                                        soda[me] = soda.pop(ab)
                                elif aa == "가격":
                                    mm = int(input("변경할 가격 금액 "))
                                    soda[ab] = mm
  
                        elif admin_password== 110:
                            print("")
                            add_soda=input("음료수 이름을 입력하세요 ")
                            add_soda_m=int(input("가격을 입력하세요 "))
                            soda[add_soda]=add_soda_m
                
                            print("--------------------------------------")
                            print(add_soda,add_soda_m ,end='을 추가했습니다')
                            print(" ")
                            for i in soda:
                                print(i,soda[i])
                            print(" ")
                            print("추가 완료")
                            print("--------------------------------------")
                        
                        elif admin_password==140:
                            print("관리자 접근을 해제합니다")
                            print("--------------------------------------")
                            print(" ")
                            break
                    
                        elif admin_password !=110 or admin_password !=120 or admin_password!=130:
                            print("")
                            print("관리자 코드에 없는 수를 입력하엿습니다")
                            print("--------------------------------------")
                    except:
                        print("이상한 수를 입력 하였습니다 처음부터 다시 시작합니다")
                        print("--------------------------------------")
                                 
            elif cc==1:
                print("------------------메뉴-------------------")
                for i in soda:
                    print(i,soda[i]) 
                print("--------------------------------------")
                
                while True:
                    try:
                        money=int(input("돈을 넣으세요  "))
                        if money>=min_money:
                            print("--------------------------------------")
                            menu=input("어떤걸 드시겠습니까  ")
                            if menu in soda:
                                li=int(input("몇개나 구매 하시겠습니까 "))
                                lili=li*soda[menu]
                                if menu in soda:
                                    if lili<=money:
                                        print("--------------------------------------")
                                        print("구매 완료")
                                        print(" ")
                                        total = money-lili
                                        while total>0:
                                            a += total // aa
                                            total%= aa

                                            s += total // ss
                                            total%= ss

                                            d += total // dd
                                            total%= dd
                                            
                                            q += total // qq
                                            total%= qq

                                            w += total // ww
                                            total%= ww

                                            e += total // ee
                                            total%= ee

                                            r += total // rr
                                            total%= rr

                                            t += total // tt
                                            total%= tt

                                            y += total // yy
                                            total%= yy
                                        
                                        print(" 10000원",a,"개\n","5000원",s,"개\n","1000원",d,"개\n","500원은",q,"개\n","100원은",w,"개\n","50원은",e,"개\n","10원은",t,"개\n","1원은",y,"개\n")
                                        print("총합",(10000*a)+(5000*s)+(1000*d)+(500*q)+(100*w)+(50*e)+(10*r)+(5*t)+(1*y),"원입니다")
                                        print("--------------------------------------")
                                        
                                        total+=0
  
                                        break
                        
                                    elif lili>money:
                                        print("구매 실패")
                                        print(lili-money,"원 만큼 부족합니다")
                                        print("")

                        elif money<min_money:
                                print("지출한 금액이 부족합니다")
                    except:
                        print("잘못 입력하였습니다 다시 하십시오")
                        print("")
        elif start=="2":
            print("실행을 종료합니다")
            break

        elif start !="1" or start !="2":
            print("")
            print("1번 2번 중에 다른걸 선택하였습니다")
            print("--------------------------------------")
            
    except :
        print("잘못된 수를 입력하였습니다")
        print("처음부터 다시 시작합니다")
        print("--------------------------------------")
        print("")
