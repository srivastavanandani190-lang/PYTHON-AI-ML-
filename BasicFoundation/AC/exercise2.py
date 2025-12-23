import time
timestamp=time.strftime('%H : %M :%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour<12):
    print("good morning")
elif(hour>=12 and hour<16):
    print("good afternoon")

elif(hour>=16 and hour<19):
    print("good evening")
else: 
    print("good night")              