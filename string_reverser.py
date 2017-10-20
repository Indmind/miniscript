def reverse(text):
    # inisialisasi
    reversed = ''
    # loop setiap huruf
    for i in range(len(text)):
        # reversed = reversed + kata pada index panjang kata dikurangi 1 dikurangi 'i'
        reversed += text[len(text) - 1 - i]

    # return kata yang sudah di reverse
    return reversed

# masukan user
text = input("Masukan kalimat: ")
# reverse
output = reverse(text)
# print output
print(output)
