def shyam():
    # this is the calculator mile to kilometer and km to mile
    print("type 1 to convert mile to km")
    print("type 2 to covert km to mile")
    x = int(input("enter your number here..........."))
    if x == 1:
        g = eval(input("enter your mile number number which you want to convert it into km"))
        print("1 mile =1.609\n", "*" * 12)
        km = g * 1.609
        print("your kilometer is..", km)
        t=input("do you want to continuee???")
        if t=="y":
            shyam()
        else:
            print("thanks for using this.....")



    elif x == 2:
        # this is for km to miles
        value = eval(input("enter your kilometer number which i convert...."))
        print("1 mile=1.609\n","*"*22)
        output=value/1.609
        print("this is your mile:=",output)
        ho=input("do you want to continuee..?")
        if ho=="y":
            shyam()
        else:
            print("thanks for using")


    else:
        print("wrong input")
shyam()