import random
import time
N = random.randint(2,10)
time.sleep(N)
print("agora!")
tempo1 = time.time()
input()
tempo2 = time.time()
x = tempo2 - tempo1
print("se passaram",x, "seg")