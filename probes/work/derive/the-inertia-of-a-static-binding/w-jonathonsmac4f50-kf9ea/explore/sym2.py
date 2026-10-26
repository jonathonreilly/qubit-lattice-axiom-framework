import sympy as sp
d=sp.symbols('delta',positive=True); m=sp.symbols('m',positive=True)
# series by truncated polynomial arithmetic in d with rational function coefficients in m
def ser(expr,n=3):
    return sp.series(expr,d,0,n).removeO()
z=-1+d
E2=4*m**2+d**2/(-1+d)
E=ser(sp.sqrt(E2),4)
E=sp.simplify(E)
print('E=',E)
q=ser((1+d)/E,3)
t=ser((q+sp.sqrt(q**2+16*m**2))/2,3)
print('t0',sp.simplify(t.subs(d,0)))
def S(x,n=3): return sp.series(x,d,0,n).removeO()
c=S(-(d)/E,4)
w1=S(-1/E,3)
N=S(w1**2+(1+c**2)/(1-z**2)+4*m**2*(1/t**2+z**2/(E**2*(1-z**2))),2)
S1=S(-1/E+c/(1-z),2)
Q=S((2*m/t)**2+(2*m)**2*(z/E-1/t)**2+(2*m/E)**2*z**2*(1-z)/(1+z),2)
W=S((E*S1+Q)/(2*N),2)
W=sp.simplify(W)
print(W)
a1=sp.simplify(-W.coeff(d,1)); a0=sp.simplify(W.coeff(d,0))
print('W0',a0); print('alpha',sp.factor(a1))
for mv in [4,sp.Rational(4,5),sp.Rational(1,10)]:
    print(mv, sp.N(a1.subs(m,mv),12))

print('----')
W0=sp.simplify(W.subs(d,0)); print('W0=',W0)
al=-sp.diff(W,d).subs(d,0)
s=sp.symbols('s',positive=True)
al=al.subs(sp.sqrt(64*m**4+1),s)
al=sp.together(al)
num,den=sp.fraction(al)
# reduce modulo s^2=64m^4+1
def red(p):
    p=sp.expand(p)
    P=sp.Poly(p,s)
    out=0
    for (k,),co in P.terms():
        out+=co*(64*m**4+1)**(k//2)*s**(k%2)
    return sp.expand(out)
num=red(num);den=red(den)
# rationalize: den=A+B s -> multiply by A-B s
Pd=sp.Poly(den,s); B=Pd.coeff_monomial(s); A=Pd.coeff_monomial(1)
num2=red(sp.expand(num*(A-B*s))); den2=sp.expand(A**2-B**2*(64*m**4+1))
res=sp.factor(sp.simplify(num2/den2))
print('alpha=',res)
resN=res.subs(s,sp.sqrt(64*m**4+1))
for mv in [4,sp.Rational(4,5),sp.Rational(1,10)]:
    print(mv, sp.N(resN.subs(m,mv),12))
