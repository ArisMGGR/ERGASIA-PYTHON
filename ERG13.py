import requests

random1 = requests.get('https://drand.cloudflare.com/public/latest')
random1 = random1.text
random1 = random1.replace('"',' ')
random1 = random1.split(' ')
random2 = random1[5]
random2 = str(random2)
del random1
random1 = []
for index in range(0,len(random2),2):
    random1.append(random2[index :index + 2])
del random2
random2 = []
for i in range(0,len(random1)):
    temp = int(random1[i], 16)
    random2.insert(i,temp)
for i in range(0,len(random2)):
    random2[i]=random2[i] % 80
del random1


kino = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
kino = kino.text

kino = kino.replace('[',' ')
kino = kino.replace(']',' ')
kino = kino.split(' ')
kino1=kino[3]
del kino
kino1 = kino1.replace(',',' ')
kino1 = kino1.split(' ')
for i in range(0,len(kino1)):
    kino1[i]=int(kino1[i])
    

sum=0
print('Αριθμοι που πετυχες:')
for i in range(0,len(kino1)):
    for j in range(0,len(random2)):
        if len(kino1)-1==i and kino1[i]==random2[j]:
            sum+=1
            print('Πετυχες το Κινο bonus: ',random2[j])
            break
        elif kino1[i]==random2[j]:
            sum+=1
            print(random2[j])
            break
print('Πετυχες',sum,'αριθμους στο Κινο')



  

