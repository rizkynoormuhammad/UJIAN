num = [5,3,2,8,1,4]
even = []
odd = []
result_odd = []
result_even = []
1.
class Solution:
    def solve (num):
        for i in num:
            if i%2==0 : #fungsi untuk memisahkan bilangan genap 
                even.append(i)
            else : #fungsi untuk memisahkan ganjil
                odd.append(i)
        even.sort(reverse=True) #mengurutkan dari besar ke kecil
        odd.sort()
        even_i = 0
        odd_i = 0
        for i in range (len(num)): #memasuka fungsi ke dalam range
            if num[i]%2==0 :
                num[i]=even[even_i]
                even_i+=1
            else:
                num[i] = odd[odd_i]
                odd_i += 1
        for i in range(len(num)):
            check=num[i]
            if check in odd :
                result_odd.append(check)
                odd.pop(odd.index(check)) #menghapus bilangin yang bukan ganjil diganti dengan ' '
                result_even.append(' ')
            else :
                result_even.append(check)
                even.pop(even.index(check)) #mengahpus bilangan yang bukan genap di dlam baris dengan spasi
                result_odd.append(' ')
        return num #mengembalikan fungsi list yang diatas
ob = Solution
print(ob.solve([5,3,2,8,1,4])) #untuk hasil pemisahan 
print(result_odd)
print(result_even)


        

