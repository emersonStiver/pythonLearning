counterRows= 0
counterColums=0
alertRows = True
alertColums = True
for i in range(11): #colums
    if alertColums:
        print("+",end=" ")
        counterColums=0
        alertColums=False
    else:
        print("|",end=" ")
        counterColums=counterColums+1
    if counterColums == 4:
        alertColums=True

    for x in range(10): #rows:
        if alertRows:
            if x >=1 and x<4 or x>=6 and x <=8:
                print(" ",end=" ")
                counterRows = counterRows + 1
            else:
                print("-",end=" ")
                counterRows = counterRows+1
        else:
            print("+",end=" ")
            counterRows = 0
            alertRows = True
            if x == 9:
                print("\n")
        if counterRows == 4:
            alertRows=False


