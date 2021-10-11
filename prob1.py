def func(n):
    if n > 0:
        arr = []
        while n > 0:
            n = int(input("Enter Number: "))
            arr.append(n)

        arr2 = []
        for num in arr:
            if num >= 100:
                arr2.append(num)

        if len(arr2) != 0:
            print(len(arr2))
        return func(n)
    else:
        return 0
    
func(1)