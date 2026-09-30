import sympy as sp
exec(open('s4_continuum_identity.py').read().split("print(\"---- debug")[0].split("ok=True")[0])
# now br2 (truncated) is available; build exact quantities from s4b in same variables
gx,gy,gz=1+hx,1+hy,1+hz
Xc=[x,sp.Symbol('y'),sp.Symbol('z')]
gm=sp.diag(gx,gy,gz); gi=sp.diag(1/gx,1/gy,1/gz)
def Gm(a_,b,c): return sum(gi[a_,d]*(sp.diff(gm[d,b],Xc[c])+sp.diff(gm[d,c],Xc[b])-sp.diff(gm[b,c],Xc[d])) for d in range(3))/2
def Rm(a_,b,c,d):
    r=sp.diff(Gm(a_,b,d),Xc[c])-sp.diff(Gm(a_,b,c),Xc[d])
    r+=sum(Gm(a_,c,e)*Gm(e,b,d)-Gm(a_,d,e)*Gm(e,b,c) for e in range(3)); return r
Rc=sp.Matrix(3,3,lambda b,d: sum(Rm(a_,b,a_,d) for a_ in range(3)))
Rex=sp.simplify(sum(gi[b,d]*Rc[b,d] for b in range(3) for d in range(3)))
sgex=sp.sqrt(gx*gy*gz)
Tex=(sum(g_**2*p_**2 for g_,p_ in zip((gx,gy,gz),P))-sp.Rational(1,2)*sum(g_*p_ for g_,p_ in zip((gx,gy,gz),P))**2)/sgex/(4*a)
def dex(L): return L*(Tex+K*sgex*Rex)
brex=PB(dex(N),dex(M))
brex2=deg_part(brex,2)
print("truncated br2 vs exact br2 (EL of difference):")
dd=sp.expand(br2-brex2)
print([sp.simplify(var_deriv(dd,f)) for f in H+P])
# compare pieces
print("sgR1 check:", sp.simplify(sgR1 - sp.series(sgex*Rex.subs({hx:t*hx,hy:t*hy,hz:t*hz}).doit() if False else 0,t,0,2).removeO()) if False else "")
