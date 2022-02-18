import random
#wp=white points  bp=black points
#flag2 stops searching 4 the queen
wp=0
bp=0
for x in range(0,100):
    a=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#tower=1   bishop=2   queen=3
    flag1=0
    flag2=0
#input tower    
    toweri=random.randint(0,7)
    towerj=random.randint(0,7)
    a[towerj][toweri]=1
#input bishop
    while flag1==0:
        bishopi=random.randint(0,7)
        bishopj=random.randint(0,7)
        if a[bishopj][bishopi]==0:
            a[bishopj][bishopi]=2
            flag1=1
    flag1=0
#input queen    
    while flag1==0:
        queeni=random.randint(0,7)
        queenj=random.randint(0,7)
        if a[queenj][queeni]==0:
            a[queenj][queeni]=3
            flag1=1
    flag1=0
    
    #game

    #tower
    if queenj==towerj:
        if towerj==bishopj:
            if toweri>queeni>bishopi or toweri<queeni<bishopi:
                wp=wp+1
                flag2=1
        else:
            wp=wp+1
            flag2=1
    if flag2==0:
        if queeni==toweri:
            if toweri==bishopi:
                if towerj>queenj>bishopj or towerj<queenj<bishopj:
                    wp=wp+1
            else:
                wp=wp+1
    
    flag2=0
    #bishop
    flag3=0
    
    #A

    j=bishopj
    i=bishopi
    if i!=0 and j!=0:
        while flag3==0:
            i=i-1
            j=j-1
            if a[j][i]==1:
                flag3=1
            if a[j][i]==3:
                wp=wp+1
                flag3=1
                flag2=1
            if i==0 or j==0:
                flag3=1

    #C
    if flag2==0:
        j=bishopj
        i=bishopi
        flag3=0
        if i!=7 and j!=7:
            while flag3==0:
                i=i+1
                j=j+1
                if a[j][i]==1:
                    flag3=1
                if a[j][i]==3:
                    wp=wp+1
                    flag3=1
                    flag2=1
                if i==7 or j==7:
                    flag3=1

    #B
    if flag2==0:
        j=bishopj
        i=bishopi
        flag3=0
        if i!=7 and j!=0:
            while flag3==0:
                i=i+1
                j=j-1
                if a[j][i]==1:
                    flag3=1
                if a[j][i]==3:
                    wp=wp+1
                    flag3=1
                    flag2=1
                if i==7 or j==0:
                    flag3=1

    #D
    if flag2==0:
        j=bishopj
        i=bishopi
        flag3=0
        if i!=0 and j!=7:
            while flag3==0:
                i=i-1
                j=j+1
                if a[j][i]==1:
                    flag3=1
                if a[j][i]==3:
                    wp=wp+1
                    flag3=1
                    flag2=1
                if i==0 or j==7:
                    flag3=1
    
    #YASSS QUEEN

    flag4=0
    if queenj==towerj==bishopj:
        if (queeni>toweri and queeni>bishopi) or (queeni<toweri and queeni<bishopi) :
            bp=bp+1
            flag4=flag4+1
        elif toweri>queeni>bishopi or toweri<queeni<bishopi:
            bp=bp+2
            flag4=flag4+2
    elif queenj==towerj or queenj==bishopj:
        bp=bp+1
    if flag4!=2:
        if queeni==toweri==bishopi:
            if (queenj>towerj and queenj>bishopj) or (queenj<towerj and queenj<bishopj) :
                bp=bp+1
                flag4=flag4+1
            elif towerj>queenj>bishopj or towerj<queenj<bishopj:
                bp=bp+2
                flag4=flag4+2
        elif queeni==toweri or queeni==bishopi:
            bp=bp+1
        
    
    #A

    if flag4!=2:
        flag3=0
        j=queenj
        i=queeni
        if i!=0 and j!=0:
            while flag3==0:
                i=i-1
                j=j-1
                if a[j][i]==1:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if a[j][i]==2:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if i==0 or j==0:
                    flag3=1

    #C
    
    if flag4!=2:
        j=queenj
        i=queeni
        flag3=0
        if i!=7 and j!=7:
            while flag3==0:
                i=i+1
                j=j+1
                if a[j][i]==1:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if a[j][i]==2:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if i==7 or j==7:
                    flag3=1
    
    #B

    if flag4!=2:
        j=queenj
        i=queeni
        flag3=0
        if i!=7 and j!=0:
            while flag3==0:
                i=i+1
                j=j-1
                if a[j][i]==1:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if a[j][i]==2:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if i==7 or j==0:
                    flag3=1

    #D

    if flag4!=2:
        j=queenj
        i=queeni
        flag3=0
        if i!=0 and j!=7:
            while flag3==0:
                i=i-1
                j=j+1
                if a[j][i]==1:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if a[j][i]==2:
                    flag3=1
                    flag4=flag4+1
                    bp=bp+1
                if i==0 or j==7:
                    flag3=1
print('Black Player: ',bp,' || White Player: ',wp)
