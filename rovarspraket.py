class Rova:
    # merubah text menjadi rovarspraket
    def encode(self, text):
        # huruf vokal
        vowels = 'aiueo'
        # merubah text menjadi list
        text = list(text)
        # loop setiap kata
        for i, s in enumerate(text):
            # jika huruf dalah konsonan
            if s not in vowels and s is not ' ':
                # ubah menjadi NoN, misal huruf 'y' maka menjadi 'yoy'
                text[i] = s + 'o' + s
        # ubah list menjadi string dan return
        return ''.join(text)

    # decode masih belajar... hehe
    def decode(self, rov):
        # bla bla bla
        test = 'test'

# membuat objek Rova
rova = Rova()
# mendapat user inout
text = input('Masukan text yang akan di encode ke rovarspraket: ')
# encode input
output = rova.encode(text)
# tampilkan output
print(output)
