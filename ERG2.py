import random
sum=0
for z in range(0,100):
    #List
    a = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    flag=0
    while flag==0:
        #input
        size = random.randint(0,2)
        loc = random.randint(0,8)
        #number after input
        if a[loc] < size:
            a[loc] = size
            sum=sum+1
            #how to win
            for i in range(0,8,3):
                if a[i]==a[i+1]==a[i+2]!=-1:
                    flag=1
            for i in range(0,3):
                if a[i]==a[i+3]==a[i+6]!=-1:
                    flag=1
            if a[0]==a[4]==a[8]!=-1 or a[6]==a[4]==a[2]!=-1:
                flag=1
            for i in range(0,8,3):
                if a[i]<a[i+1]<a[i+2]!=-1 or a[i]>a[i+1]>a[i+2]!=-1:
                    flag=1
            for i in range(0,3):
                if a[i]<a[i+3]<a[i+6]!=-1 or a[i]>a[i+3]>a[i+6]!=-1:
                    flag=1
            if a[0]<a[4]<a[8]!=-1 or a[6]<a[4]<a[2]!=-1 or a[0]>a[4]>a[8]!=-1 or a[6]>a[4]>a[2]!=-1:
                flag=1
print("Ο μεσος ορος βημαατων για 100 πααιχνιδια ειναι:",sum/100)  