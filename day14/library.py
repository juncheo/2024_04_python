import math
import random

print(random.randint(0,10000))


Lotto = []

while True:
    num = random.randint(1,46)
    if Lotto.count(num) == 0:
        Lotto.append(num)
        if len(Lotto) == 6:
            break
Lotto.sort()
print(Lotto)





# print(random.choice(["사과","바나나","집에 가고 싶다"]))







Lotto = []

while True:
    num = random.randint(1,46)
    if Lotto.count(num) == 0:
        Lotto.append(num)
        if len(Lotto) == 6:
            break




yourNumber = [int(input(f"{x}. 번호 입력:")) for x in range(6)]

rank = 6
for x in Lotto:
    if yourNumber.count(x) > 0:
        rank -= 1
print(f"로또: {Lotto}")
print(f"당신: {yourNumber}")
print(f"{rank}등 축하드립니다!")