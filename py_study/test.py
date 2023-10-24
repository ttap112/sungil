hour = 0
miniute = 0

def 시간경과():
    global hour, minute
    if minute >= 60:
        hour += 1
        minute = 0
        if hour >= 24:
            hour = 0
    return hour, minute

