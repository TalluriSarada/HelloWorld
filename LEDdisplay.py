import os
clear =lambda: os.system('cls')
clear()

data = {
    '0':('###','# #','# #','# #','###'),
    '1':('#####'),
    '2':('###','  #','###','#  ','###'),
    '3':('###','  #','###','  #','###'),
    '4':('# #','# #','###','  #','  #'),
    '5':('###','#  ','###','  #','###'),
    '6':('###','#  ','###','# #','###'),
    '7':('###','  #','  #','  #','  #'),
    '8':('###','# #','###','# #','###'),
    '9':('###','# #','###','  #','###')
}
def fun_PrintNums(angka):
    if angka < 0 or angka % 1 >0 or type(angka)!=int:
        return "Data tidak valid"
    else:
        for deret in range(len(data['0'])):
            baris = []
            for i in str(angka):
                baris.append(data[i][deret])
            print(' '.join(baris))
print(fun_PrintNums(int(input("Masukkan angka: "))))
 
