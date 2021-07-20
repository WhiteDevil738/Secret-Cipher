while True:
    Alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    Split = Alpha.split(",")
    a = []
    def Secret(user,key):
        for i in user:
            index = Alpha.index(i)
            code = index+key
            a.append(Alpha[code])
            x = "".join(a)
        return x

    
    user = input("Pwd: ").upper()
    key = int(input("Key: "))
    x = Secret(user,key)
    print(x)
    print("to break press 1")
    Quit = int(input("Quit: "))
    if Quit == 1:
        break
    else:
        pass

