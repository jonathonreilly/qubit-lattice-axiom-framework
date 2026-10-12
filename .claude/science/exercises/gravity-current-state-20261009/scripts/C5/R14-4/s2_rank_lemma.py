# R14-4 s2: the rank lemma.  V(k) = sum_i c_i I_i(k,h) (the 6 O-invariants of s1), as a 5x5 symmetric matrix on
# traceless h.  Question: can V be PSD for all k, have rank <= 2 for ALL k (no propagating partners at leading order,
# in every direction), and be positive definite on TT at k = z-hat (two linear TT polarizations)?
# (1) exact: impose rank <= 2 (all 3x3 minors = 0) at several rational directions; solve for c (sympy).
# (2) exhibit the axis-only counterexample F = sum_i k_i^2 Phi_i(h) (PSD, axis conditions met, rank 4 off-axis).
import sympy as sp, itertools, random
from s1_invariants import kx,ky,kz,K,hv,H,BAS
a,b,c,d,e=hv
h=H; k=K; hk=h*k
I=[ (k.dot(k))*sum(h[i,j]**2 for i in range(3) for j in range(3)),
    hk.dot(hk),
    sum(k[i]**2*h[i,i]**2 for i in range(3)),
    sum(k[i]**2*(h*h)[i,i] for i in range(3)),
    sum(k[i]*k[j]*h[i,j]*h[i,i] for i in range(3) for j in range(3)),
    (k.dot(k))*sum(h[i,i]**2 for i in range(3)) ]
I=[sp.expand(x) for x in I]
C=sp.symbols('c1:7')
Q=sp.expand(sum(ci*Ii for ci,Ii in zip(C,I)))
def Vmat(kv):
    q=Q.xreplace({kx:kv[0],ky:kv[1],kz:kv[2]})
    return sp.Matrix(5,5,lambda i,j: sp.Rational(1,2)*sp.diff(q,hv[i],hv[j]))
Vz=Vmat((0,0,1))
print("V(z-hat) =",Vz)
# axis sector values (basis order a=T1(TT1), b=S, c=X(TT2), d=Y(vec), e=Z(vec))
TT1,S,TT2,VEC=Vz[0,0],Vz[1,1],Vz[2,2],Vz[3,3]
print("TT1 =",TT1,"; TT2 =",TT2,"; S =",S,"; VEC =",VEC)
# ---- (1) rank <= 2 everywhere ----
random.seed(1)
dirs=[(1,1,0),(1,0,1),(0,1,1),(1,1,1),(1,2,0),(2,1,3),(1,-1,2),(3,1,2),(1,2,5)]
eqs=[]
for kv in dirs:
    V=Vmat(kv)
    for r in itertools.combinations(range(5),3):
        for cc in itertools.combinations(range(5),3):
            m=sp.expand(V.extract(list(r),list(cc)).det())
            if m!=0: eqs.append(m)
print("number of 3x3 minor equations:",len(eqs))
# axis conditions first (linear): VEC = 0, S = 0
lin=sp.solve([VEC,S],[C[0],C[5]],dict=True)[0]
print("axis conditions solved:",lin)
eqs2=list({sp.factor(sp.expand(q.xreplace(lin))) for q in eqs})
eqs2=[q for q in eqs2 if q!=0]
G=sp.groebner([sp.expand(q) for q in eqs2],*[x for x in C if x not in lin],order='grevlex')
print("Groebner basis (in remaining c's):")
for g in G.exprs: print("   ",sp.factor(g))
sols=sp.solve(G.exprs,[x for x in C if x not in lin],dict=True)
print("solutions of rank<=2 at the sampled directions:",sols)
for s in sols:
    full={**{x:x for x in C},**lin}; full={x:sp.simplify(full[x].xreplace(s)) for x in C}
    print("   c =",[full[x] for x in C],"  TT1 =",sp.simplify(TT1.xreplace(full)),"TT2 =",sp.simplify(TT2.xreplace(full)))
# ---- (2) axis-only counterexample ----
Phi=lambda i: sp.Rational(1,2)*(h[(i+1)%3,(i+1)%3]-h[(i+2)%3,(i+2)%3])**2+2*h[(i+1)%3,(i+2)%3]**2
F=sp.expand(sum(k[i]**2*Phi(i) for i in range(3)))
coef=sp.solve(sp.Poly(sp.expand(F-Q),kx,ky,kz,*hv).coeffs(),C,dict=True)
print("F = sum_i k_i^2 Phi_i(h)  in the invariant basis: c =",coef)
for kv in [(0,0,1),(1,1,0),(1,1,1)]:
    q=F.xreplace({kx:kv[0],ky:kv[1],kz:kv[2]})
    M=sp.Matrix(5,5,lambda i,j: sp.Rational(1,2)*sp.diff(q,hv[i],hv[j]))
    print("   F at k =",kv,": eigenvalues",[sp.nsimplify(x) for x in M.eigenvals(multiple=True)],"rank",M.rank())
