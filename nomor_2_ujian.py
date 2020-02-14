# nomor 2

kata = input('Masukkan Kata').replace(" ","")
panjang = len(kata)
count = 0
hitung = 0
while panjang > 0:
    panjang-=count
    count+=1
    if panjang == 0:
        for row in range(1,count):
            for col in range(row):
                print(kata[hitung],end=" ")
                hitung+=1
            print("\n", end="")
    elif panjang<0:
        print('Maaf kata anda tidak memenuhi syarat')



# import xlsxwriter

# book = xlsxwriter.Workbook('Purwadhika dotpy/Week 2/Excel To Python copy.xlsx')
# sheet = book.add_worksheet('Database')

# data = [
#     [1, 'Andi', 'Jakarta'],
#     [2, 'Budi', 'Jakarta'],
# ]

# row = 0

# for no, nama, kota in data:
#     sheet.write(row, 0, no)
#     sheet.write(row, 1, nama)
#     sheet.write(row, 2, kota)
#     row += 1