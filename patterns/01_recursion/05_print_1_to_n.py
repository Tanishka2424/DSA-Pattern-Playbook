def printNum(n):

    if n == 0:
        return 0


    
    printNum(n - 1)  
    print(n)

printNum(5)    