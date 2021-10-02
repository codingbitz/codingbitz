from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Wrong time"
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid Hour"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid Min"
        elif int(alarm_time[6:8]) > 59:
            return "Invalid Sec"
        else:
            return "ok"

while True:
    alarm = input("enter hh:mm:ss am/pm format: ")

    validate = validate_time(alarm.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"setting alarm time for {alarm}")
        break

alarmH = alarm[0:2]
alarmM = alarm[3:5]
alarmS = alarm[6:8]
alarmP = alarm[9:].upper()

while True:
    now = datetime.now()

    currH = now.strftime("%I")
    currM = now.strftime("%M")
    currS = now.strftime("%S")
    currP = now.strftime("%p")

    if alarmP == currP:
        if alarmH == currH:
            if alarmM == currM:
                if alarmS == currS:
                    print("WakeUp")
                    playsound('alarm.wav')
                    break