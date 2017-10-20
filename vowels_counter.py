def countVowels(text):
    # huruf vokal
    vowels_dat = 'aiueo'

    # data yang akan di return
    data = {
        "hasVowels": False,
        "vowels": {'a': 0, 'i': 0, 'u': 0, 'e': 0, 'o': 0},
        "sum": 0
    }

    # loop semua huruf dalam kata
    for i in text:
        # jika huruf terdapat di list huruf vokal
        if i in vowels_dat:
            # mempunyai huruf vokal = true
            data['hasVowels'] = True
            # jumblah berapa kali huruf vokal muncul
            data['vowels'][i] += 1
    
    # total keseluruhan jumlah huruf vokal muncul
    data['sum'] = sum([data['vowels'][key] for key in data['vowels']])

    # mengembalikan data
    return data

# masukan user
text = input("Masukan kalimat: ")
# hitung
counted = countVowels(text)
# tampilkan / output
print(counted['hasVowels'])
print('Huruf "a" muncul sebanyak', counted['vowels']['a'], 'kali')
print('Total huruf vokal muncul: ', counted['sum'])
