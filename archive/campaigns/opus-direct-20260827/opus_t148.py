"""T148 - VERIFYING THE CLAIM THAT KILLS R82.

The overlap lane reports: the framework's chirality obstruction is TASTE COUNTING,
not reality, and complexifying the structure constants buys nothing.  Its decisive
move is that the SAME real operator carries a second grading -- the CLIFFORD
chirality CL = Gamma_1...Gamma_d -- whose index is 2^{d/2} n rather than 0, while
the GRADE chirality G = diag((-1)^k) gives 0 because it is the taste-ANTISYMMETRIC
grading and the per-taste indices (-n and +n) cancel.

If true, R82's axiom proposal is dead: the fix needs no complexification.  So the
load-bearing algebra gets checked here, independently, with exact integer matrices:

  (i)   is CL = Gamma_1...Gamma_d REAL in d=4?  (if yes, no complexification needed)
  (ii)  does CL anticommute with every Gamma_a, square to +-1, and have zero trace?
        (those are exactly the conditions for it to BE a chirality)
  (iii) the mechanism: G should be CL times the TASTE generator T = Gb_1...Gb_d,
        which is what makes G taste-antisymmetric and CL taste-singlet.
  (iv)  does T commute with every Gamma_a?  (i.e. is it really a taste operator,
        living in the commutant measured in T138 as dimension 2^d)"""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t138 import setup

print("T148  is the Clifford chirality real, and is it a legitimate chirality?")
for d in (2,4):
    NF,G,Gb=setup(d)
    CL=np.eye(NF)
    for a in range(d): CL=CL@G[a]
    T=np.eye(NF)
    for a in range(d): T=T@Gb[a]
    GRADE=np.diag([(-1)**len(S) for S in
        [tuple(c) for k in range(d+1) for c in itertools.combinations(range(d),k)]]).astype(float)
    print(f"\n   d={d}, fibre {NF}")
    print(f"      Gamma_a real?                      max|Im| = {np.abs(np.imag(np.array(G))).max():.1e}")
    print(f"      CL = Gamma_1..Gamma_d real?        max|Im| = {np.abs(np.imag(CL)).max():.1e}"
          f"   {'REAL -- no complexification needed' if np.abs(np.imag(CL)).max()<1e-14 else ''}")
    print(f"      CL^2 = +-I ?                       CL^2 - (+1)I: {np.abs(CL@CL-np.eye(NF)).max():.1e}"
          f"    CL^2 + I: {np.abs(CL@CL+np.eye(NF)).max():.1e}")
    ac=max(np.abs(CL@G[a]+G[a]@CL).max() for a in range(d))
    print(f"      {{CL, Gamma_a}} = 0 ?                max = {ac:.1e}   {'ANTICOMMUTES' if ac<1e-12 else 'FAILS'}")
    print(f"      Tr CL = {np.trace(CL):+.1f}   (a chirality must be traceless)")
    print(f"      Tr GRADE = {np.trace(GRADE):+.1f}")
    # the mechanism: GRADE vs CL and the taste generator
    tc=max(np.abs(T@G[a]-G[a]@T).max() for a in range(d))
    print(f"      T = Gb_1..Gb_d commutes with all Gamma_a?  max|[T,Gamma]| = {tc:.1e}"
          f"   {'-> T IS a taste operator' if tc<1e-12 else ''}")
    for lab,M in (("CL*T",CL@T),("T*CL",T@CL)):
        for s,nm in ((1,'+'),(-1,'-'),(1j,'+i'),(-1j,'-i')):
            if np.abs(s*M-GRADE).max()<1e-12:
                print(f"      GRADE == {nm} {lab}   (this is why GRADE is taste-antisymmetric)")
    print(f"      CL and GRADE commute? max|[CL,GRADE]| = {np.abs(CL@GRADE-GRADE@CL).max():.1e}")
print()
print("   CL real in d=4 with all chirality properties = the 0 -> 2^{d/2} n fix uses")
print("   the framework's EXISTING real structure, and R82's complexification is")
print("   not needed for chirality.")
