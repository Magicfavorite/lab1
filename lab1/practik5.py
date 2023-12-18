a = int(input("enter the start number"))
b = int(input("enter the last number"))
if a > b:
    for i in range(b,a+1):
        if i % 2 != 0: #Если остаток деления на 2 не равен нулю то операция выполняется
            print(i)
    else:
        for i in range(a,b +1):
            print(i)

