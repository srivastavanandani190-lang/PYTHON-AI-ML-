import time
count=int(input("Enter the counter number:"))
print("Countdown starts Now:")
for i in range(count,0,-1):
    print(count)
    count-=1
time.sleep(1)
print("\n Wahoo! Happy New Year...")    