from ast import Return
from ntpath import join
import re
import json

f = open('sorular.txt','r',encoding="utf-8")   #Dosyamızı çektik ve Türkçe karakter sorununu çözdük.
x = open('stopwords.txt','r',encoding="utf-8")
sorular = f.read().lower()
yasakliKelimeler = x.read().lower()

list1 = []
list1 = sorular.split("\n")
list2 = []
list2 = yasakliKelimeler.split("\n")
list3 = []
sayac = 0

for cumleler in list1:
    list1[sayac] = re.sub(r'[^\w\s]','', cumleler)
    kelimeler= list1[sayac].split(" ")
    for kelime in kelimeler:
        if kelime not in list2:        
            list3.append(kelime)
    sayac +=1

###Kelime Sayma
wordcount={}
for word in list3:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
sort_orders = sorted(wordcount.items(),key= lambda x: x[1],reverse=True)
#kelime sayma


list4 = []
for i in sort_orders: #en çok tekrar eden kelimeleri listeye aktarma
    list4.append(f"{i[0]}")
dictOfWords = { list4[i] : i for i in range(0, 101) }# ilk 100 kelimeyi sözlüğe çevirme
dictOfWords["OOV"] = 101

al = input("lutfen cumle girisi yapiniz: ").split(" ")
vektor = []
for z in al:
    arr=[]
    arr = [0 for i in range(101)]
    print(len(arr))
    if z in dictOfWords:
        vektor.append(dictOfWords[z])
        arr[dictOfWords[z]] = 1
    else:
        vektor.append(dictOfWords["OOV"])
        arr[dictOfWords["OOV"]-1] = 1
    print(arr) # her kelimenin liste şeklinde indisini veren belirteç

print(vektor) 
