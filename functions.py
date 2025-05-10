def daftarBarang():
    print("==================== INDOMARET ====================")
    print("- semakin banyak belanja, semakin besar diskonnya - \n")
    print(" DAFTAR BARANG")
    print(" 1. Susu Rp 12,000      |   5. Minyak Rp 23,000")
    print(" 2. Gula Rp 8,000       |   6. Sabun Rp 3,000")
    print(" 3. Tepung Rp 20,000    |   7. Air putih Rp 2,000")
    print(" 4. Beras Rp 50,000     |   8. Telur Rp 17,000")

def getProduk(kodeProduk):
    match kodeProduk:
        case 1:
            return "Susu"
        case 2:
            return "Gula"
        case 3:
            return "Tepung"
        case 4:
            return "Beras"
        case 5:
            return "Minyak"
        case 6:
            return "Sabun"
        case 7:
            return "Air putih"
        case 8:
            return "Telur"

def getHarga(kodeProduk):
    match kodeProduk:
        case 1:
            return 12000
        case 2:
            return 8000
        case 3:
            return 20000
        case 4:
            return 50000
        case 5:
            return 23000
        case 6:
            return 3000
        case 7:
            return 2000
        case 8:
            return 17000

def totalPerProduk(produk, jumlah):
    match produk:
        case 1:
            hasil = 12000 * jumlah
            return hasil
        case 2:
            hasil = 8000 * jumlah
            return hasil
        case 3:
            hasil = 20000 * jumlah
            return hasil
        case 4:
            hasil = 50000 * jumlah
            return hasil
        case 5:
            hasil = 23000 * jumlah
            return hasil
        case 6:
            hasil = 3000 * jumlah
            return hasil
        case 7:
            hasil = 2000 * jumlah
            return hasil
        case 8:
            hasil = 17000 * jumlah
            return hasil
            
