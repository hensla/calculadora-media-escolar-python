cp1 = float(input("Digite sua CP1: "))
while cp1 < 0 or cp1 > 10:
    cp1 = float(input("Digite sua CP1: "))

cp2 = float(input("Digite sua CP2: "))
while cp2 < 0 or cp2 > 10:
    cp2 = float(input("Digite sua CP2: "))

cp3 = float(input("Digite sua CP3: "))
while cp3 < 0 or cp3 > 10:
    cp3 = float(input("Digite sua CP3: "))

if cp1 < cp2 and cp1 < cp3:
    cp1 = cp3
elif cp2 < cp1 and cp2 < cp3:
    cp2 = cp3

media = (cp1 + cp2) / 2

print(media)