# Numeric-jet comparison: exact degree-2 bracket vs truncated degree-2 bracket vs GR G-side at degree 2.
import sympy as sp, random
x,K,a=sp.symbols('x K a',positive=True)
s=sp.Symbol('s')
h=[sp.Function(n)(x) for n in ('hx','hy','hz')]; Q=[sp.Function(n)(x) for n in ('Px','Py','Pz')]
N,M=[sp.Function(n)(x) for n in ('N','M')]
D=lambda f,n=1: sp.diff(f,x,n)
Xc=[x,sp.Symbol('y'),sp.Symbol('z')]
def build(sc):
    gg=[1+sc*hh for hh in h]
    gm=sp.diag(*gg); gi=sp.diag(*[1/g_ for g_ in gg])
    def Gm(a_,b,c): return sum(gi[a_,d]*(sp.diff(gm[d,b],Xc[c])+sp.diff(gm[d,c],Xc[b])-sp.diff(gm[b,c],Xc[d])) for d in range(3))/2
    def Rm(a_,b,c,d):
        r=sp.diff(Gm(a_,b,d),Xc[c])-sp.diff(Gm(a_,b,c),Xc[d])
        r+=sum(Gm(a_,c,e)*Gm(e,b,d)-Gm(a_,d,e)*Gm(e,b,c) for e in range(3)); return r
    Rc=sp.Matrix(3,3,lambda b,d: sum(Rm(a_,b,a_,d) for a_ in range(3)))
    Rs=sum(gi[b,d]*Rc[b,d] for b in range(3) for d in range(3))
    sg=sp.sqrt(gg[0]*gg[1]*gg[2])
    Tf=(sum(g_**2*(sc*p_)**2 for g_,p_ in zip(gg,Q))-sp.Rational(1,2)*sum(g_*sc*p_ for g_,p_ in zip(gg,Q))**2)/sg/(4*a)
    return sg*Rs, Tf
SR,TF=build(s)
def vd(L,f):
    tot=0
    for n in range(0,4):
        fn=D(f,n) if n>0 else f
        tot+=(-1)**n*D(sp.diff(L,fn),n)
    return tot
def PB(A,B): return sum(vd(A,h[i])*vd(B,Q[i])-vd(A,Q[i])*vd(B,h[i]) for i in range(3))
# random jets
random.seed(3)
def rp(): return sum(sp.Rational(random.randint(-3,3),random.randint(1,4))*x**k for k in range(4))
jets={f:rp() for f in h+Q+[N,M]}
vals={K:sp.Rational(3,5),a:sp.Rational(2,7)}
x0=sp.Rational(1,3)
def ev(expr):
    e=expr.subs(jets).doit()
    return sp.nsimplify(e.subs(vals).subs(x,x0))
# truncated densities: keep series in s to given order (s is the bookkeeping = field degree)
def trunc(expr,order):
    return sp.expand(sp.series(expr,s,0,order+1).removeO())
V=trunc(SR,4); T=trunc(TF,5)
V_by=[V.coeff(s,k) for k in range(5)]; T_by=[T.coeff(s,k) for k in range(6)]
print("built")
# bracket of C_full[N], C_full[M] where each is N*(T_k + K V_k) restricted to pairs (k,m) with total degree condition
tot={}
for k in range(0,5):
    for m in range(0,6):
        pass
def dens_part(L,vk,tk): return L*(tk+K*vk)
# degree-2 part of bracket = sum over pairs (a,b) of homogeneous pieces with a+b-2 == 2
def piece(k): 
    return (T_by[k] if k<6 else 0)+ (K*V_by[k] if k<5 else 0)
acc=0
for i in range(1,4):
    j=4-i
    A=N*piece(i); B=M*piece(j)
    acc+= PB(A,B)
print("degree-2 bracket (pieces (1,3),(2,2),(3,1)) evaluated:", ev(acc))
xi0=(K/(4*a))*(D(N)*M-N*D(M))
Gd=lambda xi: xi*(Q[0]*D(h[0])-2*D((1+h[0])*Q[0])+Q[1]*D(h[1])+Q[2]*D(h[2]))
# EL-equivalence needed; compare by evaluating variational derivatives of both sides at the jets
def EL_all(expr): return [ev(vd(expr,f)) for f in h+Q]
# GR side at degree 2: Gd(xi0*(1-hx)) degree-2 part; use scaling
sc=sp.Symbol('sc')
G2=sp.expand(Gd(xi0*(1-h[0])).subs({f:sc*f for f in h+Q},simultaneous=True).doit()).coeff(sc,2)
print("EL(bracket deg2 - G2):",EL_all(acc-G2))
print("EL(bracket deg2):",EL_all(acc))
print("EL(G2):",EL_all(G2))
