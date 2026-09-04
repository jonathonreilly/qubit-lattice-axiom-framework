"""T34c - UNIQUENESS OF THE ENDPOINT-SYMMETRIC HOP, tested on the RIGHT family.
T34/T34b failed because they dropped the transport U -- they tested
alpha*Gamma(s) + beta*Gamma(r), which is not Result 3's object at all.  The
actual family is
      Lambda_(s<-r) = alpha * Gamma_d(s) U_(s<-r)  +  beta * U_(s<-r) Gamma_d(r)
with U the carrier isometry from D_r to D_s.  Result 3 exhibits alpha=beta=1/2
as A solution; the review correctly notes that is not a uniqueness proof.
Solve the constraint D K + K^T D = 0 for the exact (alpha,beta) SOLUTION SET,
on the same variable-metric torus Result 3 used."""
import sympy as sp
BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}
def eps(a):
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
L=4; N=L*L
sites=[(x,y) for x in range(L) for y in range(L)]; sid={s:i for i,s in enumerate(sites)}
def wrap(s): return (s[0]%L, s[1]%L)
vals=[1, sp.Rational(3,2), 2, sp.Rational(5,4), 1, sp.Rational(7,4), sp.Rational(3,2), 1,
      2, 1, sp.Rational(5,4), sp.Rational(3,2), 1, 1, 2, 1]
lam={s:(sp.Integer(vals[i]) if isinstance(vals[i],int) else vals[i]) for i,s in enumerate(sites)}
def Ds(s):  l=lam[s]; return sp.diag(l**2, sp.Integer(1), sp.Integer(1), l**-2)
def Gam(s,a): return sp.Matrix(sp.expand(eps(a)+iota(a, sp.eye(2)/lam[s]**2)))
def U(s,r): q=lam[r]/lam[s]; return sp.diag(q, sp.Integer(1), sp.Integer(1), 1/q)
def Lam(s,r,a):
    Us=U(s,r); return al*Gam(s,a)*Us + be*Us*Gam(r,a)
K=sp.zeros(4*N,4*N)
def put(blk,s,r,sgn):
    i,j=sid[s]*4, sid[r]*4
    for p in range(4):
        for q in range(4): K[i+p,j+q]+=sgn*blk[p,q]
for s in sites:
    for a in range(2):
        rp=wrap((s[0]+(a==0), s[1]+(a==1))); rm=wrap((s[0]-(a==0), s[1]-(a==1)))
        put(sp.Rational(1,2)*Lam(s,rp,a), s, rp, +1)
        put(sp.Rational(1,2)*Lam(s,rm,a), s, rm, -1)
Dg=sp.zeros(4*N,4*N)
for s in sites:
    i=sid[s]*4; Db=Ds(s)
    for p in range(4):
        for q in range(4): Dg[i+p,i+q]=Db[p,q]
Rm=sp.expand(Dg*K+K.T*Dg)
conds=set()
for i in range(Rm.rows):
    for j in range(Rm.cols):
        e=sp.simplify(Rm[i,j])
        if e!=0: conds.add(sp.expand(sp.numer(sp.together(e))))
print(f"T34c: {len(conds)} nonzero skew-adjointness conditions on (alpha,beta)")
print(f"   endpoint-symmetric alpha=beta=1/2 satisfies all: "
      f"{all(sp.simplify(c.subs({al:sp.Rational(1,2),be:sp.Rational(1,2)}))==0 for c in conds)}")
print(f"   naive one-sided alpha=1,beta=0 satisfies all: "
      f"{all(sp.simplify(c.subs({al:1,be:0}))==0 for c in conds)}")
print(f"   other one-sided alpha=0,beta=1 satisfies all: "
      f"{all(sp.simplify(c.subs({al:0,be:1}))==0 for c in conds)}")
sol=sp.solve(list(conds),[al,be],dict=True)
print(f"   EXACT SOLUTION SET over (alpha,beta): {sol}")
if conds:
    print(f"   sample conditions: {[str(sp.factor(c)) for c in list(conds)[:5]]}")
print()
print("   Reading: if the solution set is the line alpha=beta, the endpoint-symmetric")
print("   form is forced UP TO NORMALISATION within this family -- which is the honest")
print("   necessity claim.  Wider cross-form families are still not covered.")
