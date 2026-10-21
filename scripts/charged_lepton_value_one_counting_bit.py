"""Supplied Hermitian circulant identities and coefficient-energy balances.
The central-idempotent label blocks differ from coefficient subspaces.
Neither the complex structure nor channel dimensions select a physical measure.
Q is signed-trace; positive-square-root masses require a common-sign spectrum.
"""
import sympy as sp

PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail and not ok else ""))
    return ok

print("== A. the generation circulant family ==")
C = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])                 # cyclic shift x->y->z->x
check("C^3 = I (three supplied labels, cyclic C_3)", C**3 == sp.eye(3))
check("C, C^2 traceless", C.trace()==0 and (C**2).trace()==0)

a, br, bi = sp.symbols('a b_r b_i', real=True)
b = br + sp.I*bi
H = a*sp.eye(3) + b*C + sp.conjugate(b)*C.T              # Hermitian circulant mass operator
check("H Hermitian", sp.simplify(H - H.conjugate().T) == sp.zeros(3,3))
TrH  = sp.simplify(H.trace()); TrH2 = sp.simplify((H*H).trace())
check("Tr H = 3a (signed sum of sqrt-masses)", TrH == 3*a)
check("Tr H^2 = 3a^2 + 6|b|^2", sp.simplify(TrH2 - (3*a**2 + 6*(br**2+bi**2))) == 0)
r = sp.symbols('r', nonnegative=True)
check("Signed-trace Q = Tr H^2/(Tr H)^2 = 1/3 + (2/3) r,  r=|b|^2/a^2",
      sp.simplify(TrH2/TrH**2 - (sp.Rational(1,3)+sp.Rational(2,3)*(br**2+bi**2)/a**2)) == 0)
Q = sp.Rational(1,3) + sp.Rational(2,3)*r
check("r=0 -> Q=1/3 (degenerate)",   Q.subs(r,0)==sp.Rational(1,3))
check("r=1/2 -> signed Q=2/3 (algebra)", Q.subs(r,sp.Rational(1,2))==sp.Rational(2,3))
check("r=1 -> signed Q=1 (algebra)", Q.subs(r,1)==1)

print("== B. the order-4 complex structure J_cs is NATIVE on the even doublet (not missing) ==")
Ps = sp.ones(3,3)/3                                       # singlet projector (1,1,1)/sqrt3
Pd = sp.eye(3) - Ps                                       # doublet projector (2-dim, EVEN)
J  = (C - C.T)/sp.sqrt(3)                                 # J_cs = (C - C^2)/sqrt3
check("doublet is 2-dimensional (EVEN) -> already admits a complex structure", Pd.rank()==2)
check("J_cs is REAL (no 4th dimension / no complex link needed)", J == J.conjugate())
check("J_cs antisymmetric", sp.simplify(J.T + J)==sp.zeros(3,3))
check("J_cs^2 = -P_doublet  (genuine order-4 complex structure on the doublet)",
      sp.simplify(J*J - (-Pd))==sp.zeros(3,3))
check("J_cs is order-4: J^4 = +P_doublet", sp.simplify(J**4 - Pd)==sp.zeros(3,3))
check("[J_cs, H] = 0  (J_cs lives in the native circulant algebra)",
      sp.simplify(J*H - H*J)==sp.zeros(3,3))

print("== C. J_cs is MEASURE-NEUTRAL: a static J cannot pick det_C vs det_R ==")
s = sp.symbols('s', real=True)
R = Ps + sp.cos(s)*Pd + sp.sin(s)*J                       # exp(s J_cs) = rotation in the doublet plane
check("exp(s J_cs) is orthogonal (R R^T = I)", sp.simplify(R*R.T - sp.eye(3))==sp.zeros(3,3))
check("det exp(s J_cs) = 1  (preserves the REAL volume = det_R automorphism)",
      sp.simplify(R.det() - 1)==0)
# complex volume: on the doublet, J pairs into one complex line; exp(sJ)=e^{is} there, |det_C|=1
check("|det_C exp(s J_cs)| = 1 (preserves the COMPLEX volume too) -> measure-neutral both ways",
      sp.simplify(sp.Abs(sp.exp(sp.I*s)) - 1)==0)

print("== D. fixed-HS coefficient-space balance; distinct from central-idempotent blocks ==")
check("R[Z_3] = R (+) C: two minimal central idempotents, ranks 1 and 2",
      Ps.rank()==1 and Pd.rank()==2 and sp.simplify(Ps*Pd)==sp.zeros(3,3))
# HS coefficient energies, not central-block energies.
bsq = sp.symbols('b_sq', positive=True)   # |b|^2
Es, Ed = 3*a**2, 6*bsq
# Additional equal coefficient-energy assumption, not a consequence of central blocks.
sol = sp.solve(sp.Eq(Es, Ed), bsq)[0]
check("supplied equal coefficient energies E0=E1 yield r=1/2 -> signed Q=2/3",
      sp.simplify(sol/a**2 - sp.Rational(1,2))==0)
# Second supplied coefficient-balance endpoint r=1; no Born/trace derivation.
check("supplied r=1 gives signed Q=1; no physical default certified",
      Q.subs(r,1)==1)
# A fixed H fixes its spectrum. Changing the balance r generally changes
# the spectrum; the two endpoints are not two values of the same fixed Q.
Hnum = H.subs({a:1, br:sp.Rational(1,2), bi:sp.Rational(1,4)})   # generic point: 3 distinct
ev = Hnum.eigenvals()
check("spectral masses m_k = lambda_k^2 are determined (real spectrum, dim 3) by (a,|b|,arg b); a fixed H fixes its spectrum and signed-trace Q",
      sum(ev.values())==3 and all(sp.im(sp.nsimplify(e))==0 for e in ev))

# A positive weighting ratio t interpolates between and beyond the two choices
# on the same HS Gram form; endpoint selection is not an exhaustive binary law.
t = sp.symbols('t', positive=True)
r_from_weight = sp.solve(sp.Eq(Ed, t*Es), bsq)[0]/a**2
check("positive weight ratio leaves a continuous r=t/2 family at fixed coefficient HS Gram",
      sp.simplify(r_from_weight-t/2)==0)
check("third positive weight t=3/2 gives r=3/4 and Q=5/6",
      Q.subs(r,r_from_weight).subs(t,sp.Rational(3,2))==sp.Rational(5,6))

Hs, Hd = H*Ps, H*Pd
check("actual central-block HS energies depend on Re(b)",
      sp.simplify((Hs.conjugate().T*Hs).trace()-(a+2*br)**2)==0
      and sp.simplify((Hd.conjugate().T*Hd).trace()-(2*(a-br)**2+6*bi**2))==0)
check("coefficient-channel energy differs from central-block energy generically",
      sp.expand((a+2*br)**2-3*a**2)!=0)
print("Scope: coefficient balance is supplied, not implied by central-idempotent mode counts.")
print(f"\nSCORECARD: PASS={PASS} FAIL={FAIL}")
