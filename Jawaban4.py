def jualan():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = 10/100
    total = capucino*ppn + capucino
    print(total)

def teh():
    te = "memilih TEH"
    print(te)
    teh = int(input("masukkan harga : "))
    ppn = 10/100
    total = teh*ppn + teh
    print(total)

def welcome():
    nim = 20210801304
    nama = "Muhammad Ryan Novandi"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")
