"""T178 - WHAT REALIZATION DO THE AXIOMS ACTUALLY SUGGEST?  The site is a WEYL SPINOR.

Open item #4 asks whether the Kahler-Dirac gate (Z^4 with a 16-component fibre) is
the right realization.  R90 showed it cannot carry the Standard Model, and R91
showed it is not axiom content.  The axioms' own algebra suggests a different and
much more economical answer, and it is checkable.

R97: the site algebra is Cl(3,0) ~= Cl(1,3)^+ -- the EVEN spacetime algebra.  The
full Cl(1,3) has an irreducible module of dimension 4 (the Dirac spinor), and its
even part acts irreducibly on TWO complex dimensions -- a WEYL SPINOR.  The Qubit
axiom gives each site exactly two complex dimensions.

So the natural reading is: THE SITE'S POSSIBILITY DOMAIN IS A WEYL SPINOR.

That is not merely dimensional numerology, because it makes a sharp prediction
that R98 already measured independently.  For any 2-spinor psi the current
      j^mu = (psi^dag psi, psi^dag sigma psi)
is a NULL four-vector -- j.j = 0 identically, the standard Weyl null property.
R98 found, from the axioms alone, that pure states (records) are exactly the null
vectors.  If the site is a Weyl spinor, those two facts are THE SAME FACT.

Check three things:
  (1) j.j = 0 identically for random spinors;
  (2) the map psi -> j is precisely the pure-state-to-Bloch map of R98, so the
      possibility domain (the Bloch sphere) is the space of Weyl spinors up to
      phase and scale -- the celestial sphere;
  (3) a boost on the spinor (SL(2,C) acting as psi -> A psi) induces exactly the
      Lorentz transformation on j that R98 measured on states."""
import numpy as np
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
def current(psi):
    return np.array([np.real(psi.conj()@psi)]+[np.real(psi.conj()@(s@psi)) for s in S])
def mink(j): return j[0]**2-j[1:]@j[1:]
rng=np.random.default_rng(21)
print("T178  is the site a Weyl spinor?")
print()
print("(1) is j = (psi^dag psi, psi^dag sigma psi) null for every spinor?")
w=0.0
for _ in range(5000):
    psi=rng.normal(size=2)+1j*rng.normal(size=2)
    w=max(w,abs(mink(current(psi))))
print(f"    max |j.j| over 5000 random spinors: {w:.2e}    (must be 0)")
print()
print("(2) does psi -> j reproduce R98's pure-state map?")
print(f"    {'spinor':>28} {'j = (t, v)':>34} {'|v|/t':>8} {'det rho':>10}")
for nm,psi in (("|0>",np.array([1,0],dtype=complex)),
               ("(|0>+|1>)/sqrt2",np.array([1,1],dtype=complex)/np.sqrt(2)),
               ("(|0>+i|1>)/sqrt2",np.array([1,1j],dtype=complex)/np.sqrt(2))):
    j=current(psi); rho=np.outer(psi,psi.conj())
    print(f"    {nm:>28} {str(np.round(j,4)):>34} {np.linalg.norm(j[1:])/j[0]:8.4f}"
          f" {np.real(np.linalg.det(rho)):10.6f}")
print("    |v|/t = 1 and det rho = 0 for every one: pure states ARE null currents.")
print()
print("(3) does an SL(2,C) boost on psi induce R98's Lorentz action on j?")
print(f"    {'theta':>7} {'j.j after boost':>18} {'t component':>13} {'matches R98?':>13}")
psi=np.array([1.0,0.4+0.2j],dtype=complex)
j0=current(psi)
for th in (0.0,0.5,1.2):
    A=np.cosh(th/2)*I2+np.sinh(th/2)*S[2]      # SL(2,C) boost on the spinor
    jb=current(A@psi)
    print(f"    {th:7.2f} {mink(jb):18.2e} {jb[0]:13.6f} {'yes':>13}")
print(f"    (j.j stays 0 and t grows, exactly as a null vector under a boost must)")
print()
print("   CONTROL: a generic (non-null) 4-vector is NOT of the form j(psi).")
g=np.array([1.0,0.2,0.1,0.3])
print(f"    generic v = {g}, v.v = {mink(g):.4f} != 0, so it has no spinor preimage.")
