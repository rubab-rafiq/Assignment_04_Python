import time

# User se seconds input lena
seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    print("Time left:", seconds, "seconds")
    time.sleep(1)  # 1 second rukta hai
    seconds -= 1   # 1 second kam karta hai

print("Time's up!")