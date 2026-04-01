# kafe = ["nes", "turska", "espreso"]

# for kafa in kafe:
#     print(kafa)

# kafe.remove("nes")
# print(kafe)

kafe = open("kafe.txt", "a+")
proizvod = kafe.readline()
kafe.seek(0) #- vraca kursor na pocetak

# podaci = proizvod.strip().split(",")
# print(podaci)
# print("Proizvod:",podaci[0])
# print("Cena:",podaci[1])

svi_proizvodi = kafe.readlines()
print(svi_proizvodi)

for proizvod in svi_proizvodi:
    podaci = proizvod.strip().split(",")
    print(f"Proizvod: {podaci[0]}")
    print(f"Cena: {podaci[1]} RSD")
    print()

kafe.write("\nice,300\n")