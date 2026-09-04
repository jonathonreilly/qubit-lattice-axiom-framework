"""T34 - HOW UNIQUE IS THE ENDPOINT-SYMMETRIC HOP?  (narrowing Result 3)
The review is right that Result 3 as stated did not prove uniqueness.  Solve
for the whole two-endpoint linear family instead:
     Lambda_(s<-r) = alpha Gamma_d(s) + beta Gamma_d(r)
and impose weighted skew-adjointness  D K + K^T D = 0  with a genuinely
site-varying metric.  Report the exact solution SET, not one solution."""
import sympy as sp
BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}
def epsm(a):
    M=sp.zeros(4,4)
    for Sx in BAS:
        if a in Sx: continue
        T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
    return M
def iota(a,gi):
    M=sp.zeros(4,4)
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
    return M
al,be=sp.symbols('alpha beta')
L=3
sites=[(t,x) for t in range(L) for x in range(L)]; sid={s:i for i,s in enumerate(sites)}
ms={s:sp.Symbol(f'm_{s[0]}{s[1]}',positive=True) for s in sites}     # conformal factor per site
def carrier(s):
    v=ms[s]; return sp.diag(v, v/ms[s], v/ms[s], 1/v)                 # rho-uniform D on the locus
GI={s: sp.eye(2)/ms[s] for s in sites}
GAM={s:[sp.Matrix(epsm(a)+iota(a,GI[s])) for a in range(2)] for s in sites}
D=sp.zeros(4*len(sites),4*len(sites))
for s in sites:
    Ds=sp.diag(1, ms[s], ms[s], ms[s]**2)          # Lambda(g^-1) weights, uniform density
    for p in range(4): D[sid[s]*4+p, sid[s]*4+p]=Ds[p,p]
K=sp.zeros(4*len(sites),4*len(sites))
for s in sites:
    for a in range(2):
        for sgn,r in ((+1,((s[0]+(a==0))%L,(s[1]+(a==1))%L)),(-1,((s[0]-(a==0))%L,(s[1]-(a==1))%L))):
            blk=sgn*(al*GAM[s][a]+be*GAM[r][a])
            for p in range(4):
                for q in range(4): K[sid[s]*4+p, sid[r]*4+q]+=blk[p,q]
Rm=sp.expand(D*K+K.T*D)
conds=set()
for i in range(Rm.rows):
    for j in range(Rm.cols):
        e=sp.simplify(sp.together(Rm[i,j]))
        if e!=0: conds.add(sp.expand(sp.numer(sp.together(e))))
print(f"T34: {len(conds)} nonzero skew-adjointness conditions on (alpha,beta)")
sol=sp.solve(list(conds),[al,be],dict=True)
print(f"   exact solution set over (alpha,beta): {sol}")
print(f"   endpoint-symmetric (alpha=beta) satisfies all: "
      f"{all(sp.simplify(c.subs({al:sp.Rational(1,2),be:sp.Rational(1,2)}))==0 for c in conds)}")
print(f"   naive one-sided (alpha=1,beta=0) satisfies all: "
      f"{all(sp.simplify(c.subs({al:1,be:0}))==0 for c in conds)}")
gen=[sp.factor(c) for c in list(conds)[:4]]
print(f"   sample conditions: {[str(x) for x in gen]}")
print()
print("   HONEST SCOPE: this settles the two-endpoint LINEAR family only.  Wider")
print("   cross-form families (repo Blocks 215-216) are not covered by this test.")
