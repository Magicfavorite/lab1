a = int(input("enter the start number"))
b = int(input("enter the last number"))
for i in range(a,b + 1):
    if(i % 2 == 0): #Если остаток деления на 2 равен нулю то операция выполняется
        print(i)