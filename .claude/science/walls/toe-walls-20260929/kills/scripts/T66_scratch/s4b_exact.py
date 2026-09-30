# Exact (untruncated) check of the planar diagonal ADM identity {C[N],C[M]} = G[xi], to find out whether the
# truncated degree-2 bookkeeping in s4 has a bug or the reduced sector formula is off.
import sympy as sp
x,K,a=sp.symbols('x K a',positive=True)
ga,gb,gc=[sp.Function(n)(x) for n in ('ga','gb','gc')]   # full metric components g_xx,g_yy,g_zz  (g = 1 + h)
Pa,Pb,Pc,N,M=[sp.Function(n)(x) for n in ('Pa','Pb','Pc','N','M')]
D=lambda f,n=1: sp.diff(f,x,n)
G=[ga,gb,gc]; P=[Pa,Pb,Pc]
# planar diag metric ds^2 = ga dx^2 + gb dy^2 + gc dz^2
X=[x,sp.Symbol('y'),sp.Symbol('z')]
g=sp.diag(ga,gb,gc); ginv=sp.diag(1/ga,1/gb,1/gc)
def Gam(a_,b,c): return sum(ginv[a_,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(3))/2
def Riem(a_,b,c,d):
    r=sp.diff(Gam(a_,b,d),X[c])-sp.diff(Gam(a_,b,c),X[d])
    r+=sum(Gam(a_,c,e)*Gam(e,b,d)-Gam(a_,d,e)*Gam(e,b,c) for e in range(3)); return r
Ric=sp.Matrix(3,3,lambda b,d: sum(Riem(a_,b,a_,d) for a_ in range(3)))
R=sp.simplify(sum(ginv[b,d]*Ric[b,d] for b in range(3) for d in range(3)))
sg=sp.sqrt(ga*gb*gc)
T=(sum(G[i]**2*P[i]**2 for i in range(3))-sp.Rational(1,2)*sum(G[i]*P[i] for i in range(3))**2)/sg/(4*a)
def dens(L): return L*(T+K*sg*R)
def var_deriv(L,f):
    res=0
    for n in range(0,4):
        fn=D(f,n) if n>0 else f
        res+=(-1)**n*D(sp.diff(L,fn),n)
    return res
def PB(A,B):
    return sum(var_deriv(A,G[i])*var_deriv(B,P[i])-var_deriv(A,P[i])*var_deriv(B,G[i]) for i in range(3))
br=PB(dens(N),dens(M))
xi=(K/(4*a))*(D(N)*M-N*D(M))/ga
# G[xi] = int xi [ Pa ga' - 2 (ga Pa)' + Pb gb' + Pc gc' ]
Gd=xi*(Pa*D(ga)-2*D(ga*Pa)+Pb*D(gb)+Pc*D(gc))
res=br-Gd
# evaluate the residual's variational derivatives at random numeric jets to test if identically zero (total derivative)
import random
random.seed(1)
funcs=G+P+[N,M]
def rand_poly():
    return sum(sp.Rational(random.randint(-3,3),random.randint(1,3))*x**k for k in range(4))
subs={}
for f in G: subs[f]=1+sp.Rational(1,7)*rand_poly()*x**0
for f in P+[N,M]: subs[f]=rand_poly()
ok=True
for f in G+P:
    vd=var_deriv(res,f)
    val=vd.subs(subs).doit()
    val=sp.simplify(val.subs({K:sp.Rational(3,5),a:sp.Rational(2,7)}).subs(x,sp.Rational(1,3)))
    print(f,val)
    ok=ok and val==0
print("exact planar-diagonal identity holds at random jets:",ok)

print("---- order-by-order")
s=sp.Symbol('s')
# rescale fields: g=1+s*h, P -> s*P.  Take the residual in exact form and expand in s to order 2.
h=[sp.Function(n)(x) for n in ('hx_','hy_','hz_')]
Q=[sp.Function(n)(x) for n in ('Qx_','Qy_','Qz_')]
sub={ga:1+s*h[0],gb:1+s*h[1],gc:1+s*h[2],Pa:s*Q[0],Pb:s*Q[1],Pc:s*Q[2]}
r_s=res.subs(sub).doit()
for order in (0,1,2):
    co=sp.series(r_s,s,0,order+1).removeO().coeff(s,order)
    co=sp.expand(co)
    # check variational derivatives vanish: use var_deriv wrt h,Q
    def vd2(L,f):
        tot=0
        for n in range(0,4):
            fn=D(f,n) if n>0 else f
            tot+=(-1)**n*D(sp.diff(L,fn),n)
        return sp.simplify(tot)
    print("order",order,[vd2(co,f) for f in h+Q])

print("---- compare with truncated pieces")
br_s=br.subs(sub).doit()
co_ex=sp.expand(sp.series(br_s,s,0,3).removeO().coeff(s,2))
Gd_s=Gd.subs(sub).doit()
co_G=sp.expand(sp.series(Gd_s,s,0,3).removeO().coeff(s,2))
print("exact br2 - exact G2 EL:",[vd2(sp.expand(co_ex-co_G),f) for f in h+Q])
# now rebuild truncated br2 from exact-expanded densities
def dens_s(L): return sp.series(dens(L).subs(sub).doit(),s,0,4).removeO()
CNs=sp.expand(dens_s(N)); CMs=sp.expand(dens_s(M))
def PBs(A,B): return sum(vd_raw(A,h[i])*vd_raw(B,Q[i])-vd_raw(A,Q[i])*vd_raw(B,h[i]) for i in range(3))
def vd_raw(L,f):
    tot=0
    for n in range(0,4):
        fn=D(f,n) if n>0 else f
        tot+=(-1)**n*D(sp.diff(L,fn),n)
    return sp.expand(tot)
brs=sp.expand(PBs(CNs,CMs))
# the density in the scaled variables: fields scaled by s, but PB above uses derivatives wrt h,Q (unscaled) -> factor s^(-?)
print("degree parts of truncated bracket (in s):")
for k in range(0,5):
    print(k, sp.simplify(brs.coeff(s,k))==0 if False else len(sp.Add.make_args(brs.coeff(s,k))))
