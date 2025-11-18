import time
total_time=int(input("Enter time in seconds: "))
for i in range(total_time,0,-1):
    days = i // 86400
    hours = (i % 86400) // 3600
    minutes = (i % 3600) // 60
    seconds = i % 60
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is up!")
    