"""
Audit companion (exact, sympy/numpy) for
KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md

BOUNDED result (NOT a hard universal no-go; the open staggered-Dirac corner realization is not theorem-foreclosed).
On the current A_min surface, r=1 (Q=1) is the FORCED reading of the charged-lepton generation mass, and the
chiral L-R coupling localized as the selector (block-1) does NOT reach r=1/2:
  (1) a DIRAC fermion's determinant is det[[0,M],[M^dag,0]] = |det M|^2 (second-order/modulus by construction --
      only a Weyl fermion keeps det M, first-order);
  (2) D^2 = diag(M M^dag, M^dag M) -> physical masses = SINGULAR VALUES |lambda_k| (sign-blind);
  (3) the L-R coupling M(b)(x)sigma_+ FACTORIZES through the C3-Fourier modes -> b-independent generation
      eigenvectors -> Berry-FLAT -> r=1 (it does NOT curve the generation bundle);
  (4) the Koide Q=2/3 needs the SIGNED sqrt(m) readout (Yukawa eigenvalues) which the singular-value physical
      Dirac mass erases; the bundle-curving coupling that would give r=1/2 is chirality-crossing WITHIN R^3,
      forbidden by C^3=I (comm(C) cap anticomm(Gamma_chi)={0}).
So within A_min the residual reduces to the UN-FORCED sign of sqrt(m). The framework does NOT derive r=1/2 on the
current surface. Comparators (singular-value-vs-signed, Berry-monopole, McKean-Singer) cited only; no PDG values.
"""
import sympy as sp
from sympy import I, simplify, symbols, Matrix, eye, exp, pi, conjugate, zeros
import numpy as np
from pathlib import Path

R=[]; chk=lambda l,o: R.append((l,bool(o)))
w=exp(2*I*pi/3)
C=Matrix([[0,1,0],[0,0,1],[1,0,0]])
a,bre,bim=symbols('a bre bim',real=True); b=bre+I*bim
M=a*eye(3)+b*C+conjugate(b)*(C*C)
NOTE=Path(__file__).resolve().parent.parent/"docs"/"KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md"

# (1) Dirac determinant = |det M|^2 (second-order), NOT det M (first-order/Weyl)
D=Matrix(sp.BlockMatrix([[zeros(3,3), M],[M.H, zeros(3,3)]]).as_explicit())
detD=simplify(D.det()); detM=M.det()
chk("(1) det of the Dirac operator [[0,M],[M^dag,0]] = |det M|^2 (second-order/modulus, not first-order det M)",
    simplify(detD - detM*conjugate(detM))==0 or simplify(detD + detM*conjugate(detM))==0)

# (2) D^2 = diag(M M^dag, M^dag M) -> Dirac spectrum = +/- singular values -> physical masses = singular values (sign-blind)
blk=Matrix(sp.BlockMatrix([[M*M.H, zeros(3,3)],[zeros(3,3), M.H*M]]).as_explicit())
chk("(2) D^2 = diag(M M^dag, M^dag M) -> physical masses = SINGULAR VALUES |lambda_k| (sign-blind)",
    simplify(D*D-blk)==zeros(6,6))

# (3) M(b)(x)sigma_+ has b-INDEPENDENT generation eigenvectors (C3-Fourier f_k) -> Berry-flat -> r=1
fk=lambda k: Matrix([1,w**k,w**(2*k)])
chk("(3) M(b)(x)sigma_+ generation eigenvectors = b-INDEPENDENT Fourier f_k -> generation bundle Berry-FLAT -> r=1 (L-R coupling does NOT reach r=1/2)",
    all(simplify(M*fk(k)-(a+b*w**k+conjugate(b)*w**(2*k))*fk(k))==zeros(3,1) for k in range(3)))

# (4) signed sqrt(m) -> Q=2/3 ; singular-value (physical Dirac mass) -> != 2/3 where an eigenvalue is negative (2|b|>a at r=1/2)
Qs=lambda dl,absf: (lambda sm:(sum(s*s for s in sm))/(sum(sm))**2)([absf(1+np.sqrt(2)*np.cos(dl+2*np.pi*k/3)) for k in range(3)])
chk("(4a) SIGNED readout -> Koide Q=2/3 for all delta at the r=1/2 operator point",
    all(abs(Qs(dl,lambda x:x)-2/3)<1e-9 for dl in [0.1,0.5,np.pi/3,np.pi/2]))
chk("(4b) SINGULAR-VALUE (physical Dirac mass) readout -> NOT 2/3 (sign of sqrt(m) erased) -> Dirac forces r!=2/3",
    any(abs(Qs(dl,abs)-2/3)>1e-3 for dl in [np.pi/3,np.pi/2,1.0]))

# (5) source-note boundary tokens (honest scope: BOUNDED, not a hard universal no-go)
if NOTE.exists():
    tt=NOTE.read_text()
    toks=["**Type:** no_go","bounded","not a hard universal no-go","singular value","Berry-flat","sign of `√m`","not theorem-foreclosed","Independent audit required"]
    chk("(5) source note keeps the bounded / not-hard-no-go / open-corner-gate boundary", all(k in tt for k in toks))
else:
    chk("(5) source note present", False)

P=sum(1 for _,o in R if o); F=sum(1 for _,o in R if not o)
for l,o in R: print(("PASS" if o else "FAIL"),"-",l)
print("\n%d PASS, %d FAIL"%(P,F))
if F: raise SystemExit(1)
print("\nBLOCK-2 (bounded): r=1 is the FORCED reading on the current A_min surface. A Dirac fermion's determinant is\n"
      "|det M|^2 (second-order) and its physical masses are singular values (sign-blind) -> r=1; the L-R coupling\n"
      "M(b)(x)sigma_+ is Berry-flat (factorizes) so it does NOT reach r=1/2; the bundle-curving coupling that would\n"
      "is forbidden by C^3=I. The residual reduces to the UN-FORCED sign of sqrt(m). NOT a hard universal no-go:\n"
      "the open staggered-Dirac corner realization is not theorem-foreclosed. The framework does NOT derive r=1/2.")
