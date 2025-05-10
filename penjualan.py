import functions

selesai = False
subtotal = 0
pesanan = []

functions.daftarBarang()
while selesai == False:
    produk = int(input("\n = silahkan pilih produk yang ingin dibeli: "))

    if produk > 0 and produk < 9:
        print(f" = memilih produk {functions.getProduk(produk)} Rp {functions.getHarga(produk):,}")
        jumlah = int(input(" = silahkan masukan jumlah produk: "))
        if jumlah < 1:
            print(" = error, jumlah produk tidak valid. \n")
            break

        pesanan += [[produk, jumlah]]
        subtotal += functions.totalPerProduk(produk, jumlah)

        status = input("\n = ingin memesan produk lagi? (y/n): ")
        if status == "y" or status == "Y":
            continue
        elif status == "n" or status == "N":
            selesai = True
        else:
            print(" = error, kondisi tidak tersedia. \n")
            break

    else: #if cek produk
        print(" = error, produk tidak ditemukan \n")
        break

else: #while
    if subtotal >= 100000 and subtotal < 200000:
        diskon = "10%"
        total = subtotal - (10/100 * subtotal)
        potongan = subtotal - total
    elif subtotal >= 200000 and subtotal <= 300000:
        diskon = "20%"
        total = subtotal - (20/100 * subtotal)
        potongan = subtotal - total
    elif subtotal >= 300000:
        diskon = "35%"
        total = subtotal - (35/100 * subtotal)
        potongan = subtotal - total
    else: 
        diskon = "-"
        total = subtotal
        potongan = 0
    
    print("\n\n================= PESANAN SELESAI =================\n")
    nomer = -1
    for dataPesanan in pesanan:
        order = nomer + 1
        totalPerProduk = functions.totalPerProduk([dataPesanan][order][0], [dataPesanan][order][1])
        print(f" = Rp {totalPerProduk:,} ... {[dataPesanan][order][1]}x {functions.getProduk([dataPesanan][order][0])}")

    print(f"\n = Subtotal : Rp {subtotal:,}")
    print(f" = Diskon : {diskon}")
    print(f" = Potongan harga : -Rp {potongan:,}")
    print(f" = Total : Rp {total:,}")
    print("\n========== TERIMA KASIH TELAH BERBELANJA ==========\n")
    
