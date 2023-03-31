def iteracije(N):
    suma=0
    br=5
    for i in range(N):
        suma+=1/3
        br-=1/3
    print(suma,br)

iteracije(200)
iteracije(2000)
iteracije(20000)
print('Jer python racuna s aproksimacijama i za sve veće sume odstupanja od ocekivanih vrijednosti su veca')