Alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
Split = Alpha.split(",")
user = input("Pwd: ").upper()
key = int(input("Key: "))
for i in user:
    index = Alpha.index(i)
    code = index+key
    print(Alpha[code],end="")
