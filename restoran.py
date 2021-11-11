import time


print('SELAMAT DATANG DI RESTORAN BILEK')
print('============================')
print('1. Mie ayam 14k')
print('2. Bakso 15k')
print('3. Bubur ayam 12k')
print('4. Pizza 50k')
print('5. Nasi uduk 10k')
print('============================')
a = int(input('Pilih Pesanan : '))

if (a == 1):
    print('Anda memesan mie ayam.')
    print('Makanan sedang di buat, Silahkan tunggu ...')
    time.sleep(5)
    print('Makanan telah siap')
    time.sleep(3)
    print('Totalnya Rp 14000')
    harga_1 = 14000
    bayar_1 = int(input('Silahkan bayar : '))
    if (bayar_1 == harga_1):
        print('Terima kasih Selamat Makan :)')
    elif(bayar_1 < harga_1):
        print('Maaf Uang anda kurang')
    elif(bayar_1 > harga_1):
        kembalian_1 = bayar_1 - harga_1
        print('Kembaliannya : ', kembalian_1)    
elif(a == 2):
    print('Anda memesan bakso')
    print('Makanana sedang di buat, silahkan tunggu ...')
    time.sleep(5)
    print('Makanan telah siap')
    time.sleep(3)
    print('Totalnya Rp 15000')
    harga_2 = 15000
    bayar_2 = int(input('Silahkan bayar : '))
    if (bayar_2 == harga_2):
        print('Terima kasih selamat makan')
    elif (bayar_2 < harga_2):
        print('Maaf Uang anda kurang')
    elif (bayar_2 > harga_2):
        kembalian_2 = bayar_2 - harga_2
        print('Kembaliannya : ', kembalian_2)
elif(a == 3):
    print('Anda memesan mie ayam')
    print('Makanana sedang di buat, silahkan tunggu ...')
    time.sleep(5)
    print('Makanan telah siap')
    time.sleep(3)
    print('Totalnya Rp 12000')
    harga_3 = 12000
    bayar_3 = int(input('Silahkan bayar : '))
    if (bayar_3 == harga_3):
        print('Terima kasih selamat makan')
    elif (bayar_3 < harga_3):
        print('Maaf Uang anda kurang')
    elif (bayar_3 > harga_3):
        kembalian_3 = bayar_3 - harga_3
        print('Kembaliannya : ', kembalian_3)
elif(a == 4):
    print('Anda memesan pizza')
    print('Makanana sedang di buat, silahkan tunggu ...')
    time.sleep(5)
    print('Makanan telah siap')
    time.sleep(3)
    print('Totalnya Rp 50000')
    harga_4 = 50000
    bayar_4 = int(input('Silahkan bayar : '))
    if (bayar_4 == harga_4):
        print('Terima kasih selamat makan')
    elif (bayar_4 < harga_4):
        print('Maaf Uang anda kurang')
    elif (bayar_4 > harga_4):
        kembalian_4 = bayar_4 - harga_4
        print('Kembaliannya : ', kembalian_4)
elif(a == 5):
    print('Anda memesan nasi uduk')
    print('Makanana sedang di buat, silahkan tunggu ...')
    time.sleep(5)
    print('Makanan telah siap')
    time.sleep(3)
    print('Totalnya Rp 10000')
    harga_5 = 10000
    bayar_5 = int(input('Silahkan bayar : '))
    if (bayar_5 == harga_5):
        print('Terima kasih selamat makan')
    elif (bayar_5 < harga_5):
        print('Maaf Uang anda kurang')
    elif (bayar_5 > harga_5):
        kembalian_5 = bayar_5 - harga_5
        print('Kembaliannya : ', kembalian_5)
elif(a > 5):
    print('Menu tidak tersedia')
