import sympy as sp, pickle
c1,c2,c3,s1,s2,s3,C,Sn=sp.symbols('c1 c2 c3 s1 s2 s3 C Sn')
q0,qv=pickle.load(open('S_pal.pkl','rb'))
e=sp.symbols('e')
def ser(x,n=6):
    y=x.subs({C:sp.cos(e/2),Sn:sp.sin(e/2)})
    return sp.series(y,e,0,n).removeO()
def redk(x):
    x=sp.expand(x)
    p=sp.Poly(x,s1,s2,s3)
    out=0
    for mon,co in p.terms():
        a,b,cc=mon
        out+=co*(1-c1**2)**(a//2)*s1**(a%2)*(1-c2**2)**(b//2)*s2**(b%2)*(1-c3**2)**(cc//2)*s3**(cc%2)
    return sp.expand(out)
Q0=sp.expand(ser(q0,7)); 
print('q0 series coefficients')
for n in range(0,7):
    co=sp.factor(redk(Q0.coeff(e,n)))
    print(n,co)
print('vector series')
for i in range(3):
    Qi=sp.expand(ser(qv[i],6))
    for n in range(0,6):
        print(i,n,sp.factor(redk(Qi.coeff(e,n))))
