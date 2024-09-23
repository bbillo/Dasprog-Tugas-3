masuk = input()
masuk = masuk.split()
n = int(masuk[0])
kata = masuk[1].lower()

if kata == "aku":
    for i in range(1, n + 1):
        baris =[]
        for j in range(1,i+1):
            if (i + j) % 2 == 0:
                baris.append("I")
            else:
                baris.append("U")
        print(" ".join(baris))
elif kata == "kamu":
    for i in range(1, n + 1):
        spasi = "  " * (n-i)
        baris =[]
        for j in range(1,i+1):
            if (i + j) % 2 == 0:
                baris.append("I")
            else:
                baris.append("U")
        print(spasi +" ".join(baris))
