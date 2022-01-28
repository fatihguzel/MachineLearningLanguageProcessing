from ast import Return
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
sayac1= 0
id = 0
for cumleler in list1:
    list1[sayac] = re.sub(r'[^\w\s]','', cumleler)
    kelimeler= list1[sayac].split(" ")
    for kelime in kelimeler:
        while(id<len(kelimeler)):
            if(kelime == list2[id]):
                kelimeler.remove(f"{kelime}")
                break
            list3 = list3 + kelimeler
            id+=1

        # for yasak in list2:          #buradaki döngülerde bazı yasaklı kelimelerin silme islemini kaciriyor
        #     if(kelime == yasak):
        #         kelimeler.remove(f"{kelime}")
        #         list3 = list3 +  kelimeler
                 
    sayac +=1
#print(list3)
list4 = []
###Kelime Sayma
wordcount={}
for word in list3:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
sort_orders = sorted(wordcount.items(),key= lambda x: x[1],reverse=True)
#kelime sayma

sayac2 = 0
for i in sort_orders: #en çok tekrar eden kelimeleri listeye aktarma
    #print(i[0])  
    list4.append(f"{i[0]}")
# print(list4)

dictOfWords = { i : list4[i] for i in range(0, 101) }# ilk 100 kelimeyi sözlüğe çevirme
dictOfWords[101] = "OOV"
print(dictOfWords)

        
