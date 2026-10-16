# Rigorous PSD/rank check at positive roots of det(Q)=0 via interval arithmetic on rational isolating intervals
import sympy as sp, pickle, mpmath as mp, itertools, numpy as np
b0,b1,b2,u=sp.symbols('b0 b1 b2 u',real=True)
Q=pickle.load(open('Q.pkl','rb'))
Qp=Q.subs({b0:sp.Rational(11,30),b2:sp.Rational(3,20)})
P=sp.Poly(259200000000*u**4 - 453744000000*u**3 + 12644840000*u**2 + 1185396800*u - 39225499,u)
print("irreducible over Q:",P.is_irreducible, " Q(det) check:", sp.expand(Qp.det().subs(b1,sp.sqrt(u))*259200000000-P.as_expr())==0)
mp.mp.dps=60
for (lo,hi),m in P.intervals(eps=sp.Rational(1,10**45)):
    if hi<=0: continue
    U=mp.iv.mpf([mp.mpf(sp.Rational(lo).p)/sp.Rational(lo).q, mp.mpf(sp.Rational(hi).p)/sp.Rational(hi).q])
    for s in (1,-1):
        B1=s*mp.iv.sqrt(U)
        def ev(e):
            acc=mp.iv.mpf(0)
            for cf in sp.Poly(e,b1).all_coeffs():
                cf=sp.Rational(cf); acc=acc*B1+mp.iv.mpf(cf.p)/cf.q
            return acc
        found=None
        for perm in itertools.permutations(range(4),3):
            ms=[ev(sp.expand(Qp.extract(list(perm[:k]),list(perm[:k])).det())) for k in (1,2,3)]
            if all(x.a>0 for x in ms): found=perm; break
        M=np.array(Qp.subs(b1,s*sp.sqrt(sp.Float(lo,50))).evalf(30),dtype=float)
        print(f"u in [{float(lo):.12f},{float(hi):.12f}] b1 sign {s:+d}: certified PD 3x3 nested block {found}; eig {np.round(np.linalg.eigvalsh(M),9)}")
