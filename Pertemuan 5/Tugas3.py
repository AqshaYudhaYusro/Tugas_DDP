soal =int(input('''Silahkan pilih nomor berikut?
                
                1.untuk menghitung luas persegi
                2.untuk menghitung luas lingkaran
                3.untuk menghitung luas segitiga
                
                apa piihanmu?'''))

match soal:
    case 1:
        print('kamu memilih luas persegi')
        sisi = int(input('sisi='))
        print('untuk luas persegidengan sisi', sisi, 'adalah', sisi*sisi)
    case 2:
        print('kamu memilih luas lingkaran')
        r = int(input('r='))
        LuasL = 3.14*r*r
        print('untuk luas lingkaran dengan r', r, 'adalah', LuasL )
    case 3:
        print('kamu memilih luas segitiga')
        alas = int(input('alas='))
        tinggi = int(input('tinggi='))
        LuasS = alas*tinggi/2
        print('untuk luas segitiga dengan alas', alas, 'dan tinggi', tinggi, 'adalah', LuasS )
    case _:
        print('pilihan kamu salah')