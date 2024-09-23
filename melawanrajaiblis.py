U = int(input())
K = int(input())
M = int(input())

SM = M//2
SK = K//2
RI = 100

G1 = U - (SK*2)
G2 = G1 - ((SM*5))*5
G3 = G2 - (RI * 10)

if G3 > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {G3}")

else:
    print("Yah! Ucup Meninggoy.")

x1, y1 = map(int, input().split())    #x1,y1 adalah titik awal raja
x2, y2 = map(int, input().split())    #x2,y2 adalah titik tujuan raja
x3, y3 = map(int, input().split())    #x3,y3 adalah titik pusat lingkaran

#menghitung jarak antara dua titik
def jarak_kuadrat(x1, y1, x2, y2):     
    return(x2 - x1)*2 + (y2 - y1)*2

#hitung jarak kuadrat dari titik awal dan titik tujuan ke pusat lingkaran
jarak_awal = jarak_kuadrat(x1, y1, x3, y3)
jarak_tujuan = jarak_kuadrat(x2, y2, x3, y3)

#hitung jarak kuadrat antara TITIK AWAL RAJA dan TITIK TUJUAN RAJA
jarak_perjalanan = jarak_kuadrat(x1,y1,x2,y2)

if jarak_awal > jarak_perjalanan and jarak_tujuan > jarak_perjalanan:
    print("Yes")
else:
    print("No")