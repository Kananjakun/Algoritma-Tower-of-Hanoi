def hanoi(n, asal, bantuan, tujuan):
    if n == 1:
        print("pindahkan cakram 1, dari tiang {}, ke tiang {}." .format( asal, tujuan))
        return
    hanoi(n - 1, asal, tujuan, bantuan)
    print("Pindahkan Cakram {}, Dari tiang {}, ke tiang {}.".format(n, asal, tujuan))
    hanoi(n - 1, bantuan, asal, tujuan)

n = int(input("Masukan Jumlah n :"))
hanoi(n, "A", "B", "C")