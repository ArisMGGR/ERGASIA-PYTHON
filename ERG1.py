import random
sum=0
for z in range(0,100):
    #List
    a = [[0,0,0] ,[0,0,0] ,[0,0,0] ,[0,0,0] ,[0,0,0] ,[0,0,0] ,[0,0,0] ,[0,0,0] ,[0,0,0]]
    flag=0
    while flag==0:
        #input
        size = random.randint(0,2)
        loc = random.randint(0,8)
        #number after input
        if a[loc][size] == 0:
            a[loc][size] = 1
            sum=sum+1
           
           
            #how to win
            for x in range(0,3):
                for i in range(0,8,3):
                    if a[i][x]==a[i+1][x]==a[i+2][x]!=0:
                        flag=1
                for i in range(0,3):
                    if a[i][x]==a[i+3][x]==a[i+6][x]!=0:
                        flag=1
                if a[0][x]==a[4][x]==a[8][x]!=0 or a[6][x]==a[4][x]==a[2][x]!=0:
                    flag=1
            for i in range(0,8,3):
                if a[i][0]==a[i+1][1]==a[i+2][2]!=0 or a[i][2]==a[i+1][1]==a[i+2][0]!=0:
                    flag=1
            for i in range(0,3):
                if a[i][0]==a[i+3][1]==a[i+6][2]!=0 or a[i][2]==a[i+3][1]==a[i+6][0]!=0:
                    flag=1
            if a[0][0]==a[4][1]==a[8][2]!=0 or a[6][0]==a[4][1]==a[2][2]!=0 or a[0][2]==a[4][1]==a[8][0]!=0 or a[6][2]==a[4][1]==a[2][0]!=0:
                flag=1
print("Ο μεσος ορος βημαατων για 100 πααιχνιδια ειναι:",sum/100)                