input_time = input()
hour = input_time.find("시간")
minute = input_time.find("분")

if hour == -1:
    answer = int(input_time[minute-2:minute])
elif minute == -1:
    answer = int(input_time[0:hour])*60
else:
    answer = int(input_time[0:hour])*60+int(input_time[minute-2:minute])
print(answer)
