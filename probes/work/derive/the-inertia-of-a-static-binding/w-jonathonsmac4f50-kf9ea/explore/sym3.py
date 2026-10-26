import sympy as sp
d=sp.symbols('delta',positive=True); m=sp.symbols('m',positive=True); s=sp.symbols('s',positive=True)
def S(x,n): return sp.series(x,d,0,n).removeO()
z=-1+d
E=S(sp.sqrt(4*m**2+d**2/(-1+d)),5)
q=S((1+d)/E,4)
t=S((q+sp.sqrt(q**2+16*m**2))/2,4)
c=S(-(d)/E,5); w1=S(-1/E,4)
N=S(w1**2+(1+c**2)/(1-z**2)+4*m**2*(1/t**2+z**2/(E**2*(1-z**2))),1)  # N ~ A/delta
V=sp.simplify(S(E-t,3))
wr2=S((1+(2*m/t)**2)/(N),3)
U=S(V*wr2,3)
def tos(expr):
    expr=expr.subs(sp.sqrt(64*m**4+1),s)
    return expr
def reduce_s(e):
    e=sp.together(tos(e)); num,den=sp.fraction(e)
    def red(p):
        P=sp.Poly(sp.expand(p),s); out=0
        for (k,),co in P.terms(): out+=co*(64*m**4+1)**(k//2)*s**(k%2)
        return sp.expand(out)
    num=red(num);den=red(den)
    Pd=sp.Poly(den,s); B=Pd.coeff_monomial(s); A=Pd.coeff_monomial(1)
    if B==0: return sp.factor(num/den)
    num2=red(sp.expand(num*(A-B*s))); den2=sp.expand(A**2-B**2*(64*m**4+1))
    return sp.factor(sp.simplify(num2/den2))
u1=sp.simplify(sp.diff(U,d).subs(d,0)) if False else sp.simplify(sp.limit(U/d,d,0))
print('U/delta ->',reduce_s(u1))
alpha=(16*m**2+3-s)/(8*m**2)
u1s=reduce_s(u1)
# static: -(T-U/2)/m with T=-U at leading order => (3/2)U/m... W_static-1 = U/(2m)-T/m = 3U/(2m) (T=-U+O(d^2))
stat=sp.simplify(-(sp.Rational(3,2))*u1s/m)   # coefficient of delta in (1-Ws)
print('static coeff',stat)
R=sp.simplify(alpha/stat)
Rn=lambda mv: sp.N(R.subs(s,sp.sqrt(64*m**4+1)).subs(m,mv),12)
print('R=',sp.factor(R))
for mv in [4,sp.Rational(4,5),sp.Rational(1,10),sp.Rational(1,100)]: print(mv,Rn(mv))
# lambda*: W=W0+lambda*E0*U => 1 = 1 - alpha d + lambda*2m*u1 d  => lambda = alpha/(2 m u1)  (u1<0 => lambda<0)
lam=sp.simplify(alpha/(2*m*u1s))
print('lambda*=',sp.factor(lam))
for mv in [4,sp.Rational(4,5),sp.Rational(1,10)]: print(mv,sp.N(lam.subs(s,sp.sqrt(64*m**4+1)).subs(m,mv),12))
