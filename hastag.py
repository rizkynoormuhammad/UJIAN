#output=How
#x="Hello there how are you doing"
def hastag (s):
    while ' ' in s:
        s=s.replace(' ','')
    count = 0
    arr =[]
    for char in s:
        arr.append(char)
        count +=1
    arr.insert(0, '#') #menmbhkan fungsi Hastag didepan huruf
    for i in range(0, len(arr)):
        arr[i] = arr[i].lower()
    if s== '':
        return False
    if count > 140:
        return False
    arr[1]=arr[1].upper()#setiap huruf pada kata awal akan menjadi huruf besar.

    i=0
    for char in arr:
        if char.isspace():#menghilangkan spasi pada setiap kalimat
            del arr[i]
            arr[i]=arr[i].upper()
        i+=1
    return ''.join(arr)
print(hastag("Hello there how are you doing"))
print(hastag("   Hello  Word"))
print(hastag(""))




    