while True:    
    try:    
        def add(a,b):
            return a+b

        def sub(a,b):
            return a-b

        def mul(a,b):
            return a*b

        def div(a,b):
            return a/b

        print("Addtion\t Subtraction\t Multiplication\t Division")
        while True:
            print("*********************")
            a=int(input("Enter the First value: "))
            c=input("Enter the operation: ")
            
        # if c in['1','2','3','4']:
            if c=="+":
                
                b=int(input("Enter the second value: "))
                sum=add(a,b)
                print(f"{a}+{b}={sum}")

            elif c=="-":
                
                b=int(input("Enter the second value: "))
                subtra=sub(a,b)
                print(f"{a}-{b}={subtra}")

            elif c=="*":
                
                b=int(input("Enter the second value: "))
                multi=mul(a,b)
                print(f"{a}x{b}={multi}")

            elif c=="/":
                
                b=int(input("Enter the second value: "))
                di=div(a,b)
                print(f"{a}/{b}={di}")

            else:
                print(f"{c} is operation is available!\nsorry, for inconvince.")
    except Exception as e:
        print("Error is ",e)
