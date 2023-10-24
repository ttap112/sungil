import time

for i in range(100, -1, -1):  # 100부터 0까지
    print('\r경계 게이지 : {0} {1}%'.format('█'*(i//5), i), end='')
    time.sleep(0.1)


