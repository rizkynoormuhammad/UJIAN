n = int(input('enter number:')) #masukan jumlah yang inginkan

for row in range (1,n+1): #untuk baris dengan (start,stop) (1,)
    for col in range (1,2*n): # untuk colom yang akan di input
        if row==n or row+col==n+1 or col-row==n-1: #jika persyaratan nya berhasil akan keluar (#)
            print('#',end='')
        else: #jika persyaratan If nya gagal akan keluar hasil (_)
            print(end='_')
    print()
