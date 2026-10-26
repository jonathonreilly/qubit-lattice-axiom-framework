import sympy as sp
e=sp.symbols('e',positive=True)
k=sp.symbols('k1:4',real=True)
s=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
I2=sp.eye(2)
def layers(order_choice='cyclic'):
    L=[]
    for j in range(3):
        X=s[j]; Y=s[(j+1)%3]
        gA=sp.cos(k[j])*X-sp.sin(k[j])*Y
        gB=sp.cos(k[j])*X+sp.sin(k[j])*Y
        L+= [gA,gB]
    return L
def lay(g,a): return sp.cos(a)*I2-sp.I*sp.sin(a)*g
L=layers()
# palindromic: L1(e/2)..L5(e/2) L6(e) L5(e/2)..L1(e/2)
S=I2
for g in L[:5]: S=S*lay(g,e/2)
S=S*lay(L[5],e)
for g in reversed(L[:5]): S=S*lay(g,e/2)
S=S.applyfunc(sp.expand)
ht=sp.simplify(((S.trace())/2))
ht=sp.simplify(sp.expand(ht))
print(ht)
# series in e
import sys
c=[sp.cos(x) for x in k]
ser=sp.series(ht,e,0,6).removeO()
print(sp.simplify(ser))
