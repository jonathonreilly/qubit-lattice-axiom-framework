"""
Audit companion (exact, sympy/numpy) for
KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md

NARROWED BOUNDED result (not a hard universal no-go; the open staggered-Dirac corner realization remains outside
this theorem's claim). For the declared C3-circulant Dirac current-surface mass operator M(b) and factor-crossing
L-R coupling M(b)(x)sigma_+, this runner checks algebraic sign-blindness and Berry flatness only:
  (1) the declared Dirac block has det[[0,M],[M^dag,0]] = |det M|^2 up to the fixed block sign;
  (2) D^2 = diag(M M^dag, M^dag M) carries singular-value data, hence the declared readout is sign-blind;
  (3) M(b)(x)sigma_+ factorizes through the C3-Fourier modes, with b-independent generation eigenvectors, hence
      the generation bundle is Berry-flat;
  (4) at the declared r=1/2 Koide dial point, signed and absolute-value readouts differ when a sqrt(m) eigenvalue
      is negative.
This does not prove a physical readout->branch-selection theorem, does not claim r=1 is physically selected, and
does not claim r=1/2 is physically excluded. r=0, r=1/2, and r=1 are distinct framework locations; r=1/2 is a
stable dial setting, never forced by this runner. The named open target is READOUT_TO_BRANCH_SELECTION_BRIDGE.
Comparators (singular-value-vs-signed, Berry-monopole, McKean-Singer) are cited only; no PDG values.
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

# (1) Declared Dirac block determinant = |det M|^2 up to the fixed block sign.
D=Matrix(sp.BlockMatrix([[zeros(3,3), M],[M.H, zeros(3,3)]]).as_explicit())
detD=simplify(D.det()); detM=M.det()
chk("(1) declared Dirac block det[[0,M],[M^dag,0]] = |det M|^2 up to fixed block sign",
    simplify(detD - detM*conjugate(detM))==0 or simplify(detD + detM*conjugate(detM))==0)

# (2) D^2 = diag(M M^dag, M^dag M) -> singular-value data -> sign-blind declared readout.
blk=Matrix(sp.BlockMatrix([[M*M.H, zeros(3,3)],[zeros(3,3), M.H*M]]).as_explicit())
chk("(2) D^2 = diag(M M^dag, M^dag M) -> singular-value data is sign-blind",
    simplify(D*D-blk)==zeros(6,6))

# (3) M(b)(x)sigma_+ has b-independent generation eigenvectors (C3-Fourier f_k) -> Berry-flat.
fk=lambda k: Matrix([1,w**k,w**(2*k)])
chk("(3) M(b)(x)sigma_+ generation eigenvectors are b-independent Fourier f_k -> Berry-flat",
    all(simplify(M*fk(k)-(a+b*w**k+conjugate(b)*w**(2*k))*fk(k))==zeros(3,1) for k in range(3)))

# (4) signed sqrt(m) -> Q=2/3; absolute-value readout -> != 2/3 where an eigenvalue is negative.
Qs=lambda dl,absf: (lambda sm:(sum(s*s for s in sm))/(sum(sm))**2)([absf(1+np.sqrt(2)*np.cos(dl+2*np.pi*k/3)) for k in range(3)])
chk("(4a) signed readout -> Koide Q=2/3 for all sampled delta at the declared r=1/2 dial point",
    all(abs(Qs(dl,lambda x:x)-2/3)<1e-9 for dl in [0.1,0.5,np.pi/3,np.pi/2]))
chk("(4b) absolute-value readout -> not Q=2/3 for sampled deltas with erased sqrt(m) sign",
    any(abs(Qs(dl,abs)-2/3)>1e-3 for dl in [np.pi/3,np.pi/2,1.0]))

# (5) source-note boundary tokens (honest narrowed scope: algebraic flatness, open bridge, dial firewall).
if NOTE.exists():
    tt=NOTE.read_text()
    toks=[
        "**Type:** no_go",
        "bounded",
        "not a hard universal no-go",
        "algebraic flatness",
        "sign-blindness",
        "READOUT_TO_BRANCH_SELECTION_BRIDGE",
        "`r = 1/2` is a stable dial setting, never forced",
        "does not claim `r=1` is physically selected",
        "Independent audit required",
    ]
    chk("(5) source note keeps narrowed algebraic-flatness / open-bridge / dial-firewall boundary", all(k in tt for k in toks))
else:
    chk("(5) source note present", False)

P=sum(1 for _,o in R if o); F=sum(1 for _,o in R if not o)
for l,o in R:
    print(("PASS:" if o else "FAIL:"), l)
print("\nNARROWED RESULT: the runner proves algebraic sign-blindness and Berry flatness for the declared "
      "C3-circulant Dirac current-surface L-R coupling. READOUT_TO_BRANCH_SELECTION_BRIDGE remains open; "
      "no physical r=1 selection or r=1/2 exclusion is claimed.")
print(f"TOTAL: PASS={P}, FAIL={F}")
if F:
    raise SystemExit(1)
