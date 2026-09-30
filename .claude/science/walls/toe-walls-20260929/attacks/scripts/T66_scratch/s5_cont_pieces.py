# Build continuum reference pieces (T2,T3,V1,V2) by exact scaling-expansion; verify the degree-2 identity with the truncated pieces.
import sympy as sp, pickle
x,K,a,s=sp.symbols('x K a s',positive=True)
h=[sp.Function(n)(x) for n in ('hx','hy','hz')]; Q=[sp.Function(n)(x) for n in ('Px','Py','Pz')]
N,M=[sp.Function(n)(x) for n in ('N','M')]
D=lambda f,n=1: sp.diff(f,x,n)
Xc=[x,sp.Symbol('y'),sp.Symbol('z')]
gg=[1+s*hh for hh in h]
gm=sp.diag(*gg); gi=sp.diag(*[1/g_ for g_ in gg])
def Gm(a_,b,c): return sum(gi[a_,d]*(sp.diff(gm[d,b],Xc[c])+sp.diff(gm[d,c],Xc[b])-sp.diff(gm[b,c],Xc[d])) for d in range(3))/2
def Rm(a_,b,c,d):
    r=sp.diff(Gm(a_,b,d),Xc[c])-sp.diff(Gm(a_,b,c),Xc[d])
    r+=sum(Gm(a_,c,e)*Gm(e,b,d)-Gm(a_,d,e)*Gm(e,b,c) for e in range(3)); return r
Rc=sp.Matrix(3,3,lambda b,d: sum(Rm(a_,b,a_,d) for a_ in range(3)))
Rs=sum(gi[b,d]*Rc[b,d] for b in range(3) for d in range(3))
sg=sp.sqrt(gg[0]*gg[1]*gg[2])
sgR=sp.expand(sp.series(sg*Rs,s,0,3).removeO())
V1=sgR.coeff(s,1); V2=sgR.coeff(s,2)
Tf=(sum(g_**2*(s*p_)**2 for g_,p_ in zip(gg,Q))-sp.Rational(1,2)*sum(g_*s*p_ for g_,p_ in zip(gg,Q))**2)/sg/(4*a)
Tser=sp.expand(sp.series(Tf,s,0,4).removeO())
T2=Tser.coeff(s,2); T3=Tser.coeff(s,3)
print("V1 =",V1); print("V2 =",V2); print("T2 =",T2); print("T3 =",sp.simplify(T3))
pickle.dump(dict(V1=V1,V2=V2,T2=T2,T3=T3),open('cont_pieces.pkl','wb'))
def vd(L,f):
    tot=0
    for n in range(0,4):
        fn=D(f,n) if n>0 else f
        tot+=(-1)**n*D(sp.diff(L,fn),n)
    return sp.expand(tot)
def PB(A,B): return sp.expand(sum(vd(A,h[i])*vd(B,Q[i])-vd(A,Q[i])*vd(B,h[i]) for i in range(3)))
CN=lambda L: L*(T2+T3+K*(V1+V2))
br=PB(CN(N),CN(M))
sc=sp.Symbol('sc')
def degpart(e,d):
    sub={f:sc*f for f in h+Q}
    return sp.expand(e.subs(sub,simultaneous=True).doit()).coeff(sc,d)
br1=degpart(br,1); br2=degpart(br,2)
xi0=(K/(4*a))*(D(N)*M-N*D(M))
Gd=lambda xi: xi*(Q[0]*D(h[0])-2*D((1+h[0])*Q[0])+Q[1]*D(h[1])+Q[2]*D(h[2]))
G1=degpart(sp.expand(Gd(xi0)),1)
G2=degpart(sp.expand(Gd(xi0*(1-h[0]))),2)
for name,dd in (("deg1",br1-G1),("deg2",br2-G2)):
    print(name,[sp.simplify(vd(sp.expand(dd),f)) for f in h+Q])

print("---- add higher orders to see which piece completes the identity")
sgR3=sgR  # only up to s^2 currently
sgR_hi=sp.expand(sp.series(sg*Rs,s,0,5).removeO())
V3=sgR_hi.coeff(s,3); V4=sgR_hi.coeff(s,4)
Tser_hi=sp.expand(sp.series(Tf,s,0,6).removeO())
T4=Tser_hi.coeff(s,4); T5=Tser_hi.coeff(s,5)
for label,dens in (("+V3",lambda L: L*(T2+T3+K*(V1+V2+V3))),("+T4",lambda L: L*(T2+T3+T4+K*(V1+V2))),("+V3+T4+V4+T5",lambda L: L*(T2+T3+T4+T5+K*(V1+V2+V3+V4)))):
    b=PB(dens(N),dens(M)); b2=degpart(b,2)
    print(label,[sp.simplify(vd(sp.expand(b2-G2),f)) for f in h+Q][:3])
