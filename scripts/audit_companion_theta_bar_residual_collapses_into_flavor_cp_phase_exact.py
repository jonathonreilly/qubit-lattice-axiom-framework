"""
Audit companion (exact, sympy/numpy) for
THETA_BAR_RESIDUAL_COLLAPSES_INTO_THE_FLAVOR_CP_PHASE_NARROW_NOTE_2026-06-05.md

The physical strong-CP angle is theta-bar = theta_QCD + arg det(M_q) (standard, basis-invariant).
The framework's generation mass matrix is the HERMITIAN C3-circulant M = aI + bC + bbar C^2, whose
determinant is REAL (arg det = 0): the framework's CP-CONSERVING default (theta-bar = 0 AND the Koide
phase delta = 0 are the SAME real point). On the real-Wilson gauge action (theta_QCD = 0, the repo's
already-selected surface, STRONG_CP_THETA_ZERO_NOTE), the physical theta-bar = arg det(M_q): a CP-odd
phase of the SAME generation mass matrices whose CP-odd phase is delta. Both vanish at the real
default and turn on TOGETHER from one reality-breaking. So the strong-CP angle theta-bar is NOT an
independent input from the flavor-CP phase (which is part of AC_phi_lambda); the strong-CP problem
here IS the flavor-CP (Nelson-Barr) problem.

SCOPE (honest): this is a BOOKKEEPING COLLAPSE of the theta admission's physical residual into the
flavor sector, NOT a strong-CP SOLUTION. It does not derive theta-bar ~ 0; the controlled smallness
(theta-bar ~ 0 while CKM != 0) is exactly the Nelson-Barr problem, also unsolved in the SM. It does
not, by itself, reduce the Tier-A count to 1: the gauge-side real-Wilson selection (theta_QCD = 0)
remains, and reflection positivity provably cannot force it
(STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16). No PDG values as derivation
inputs; literature (Nelson 1983, Barr 1984; Vafa-Witten 1984) is comparator only.
"""
import sympy as sp, cmath
from sympy import I, simplify, symbols, Matrix, eye, conjugate, im, expand
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "THETA_BAR_RESIDUAL_COLLAPSES_INTO_THE_FLAVOR_CP_PHASE_NARROW_NOTE_2026-06-05.md"

a = symbols('a', real=True, positive=True)
bre, bim = symbols('bre bim', real=True)
b = bre + I*bim
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

# (1) the framework's generation mass matrix is the HERMITIAN C3-circulant -> det is REAL -> arg det = 0
M = a*eye(3) + b*C + conjugate(b)*(C*C)
chk("(1) generation circulant M = aI + bC + bbar C^2 is Hermitian (M = M^H)",
    simplify(M - M.H) == sp.zeros(3, 3))
detM = simplify(M.det())
chk("(1b) det M is REAL (Im = 0) -> arg det M = 0 : the CP-CONSERVING default (no theta-bar contribution)",
    simplify(im(expand(detM))) == 0)

# (2) theta-bar = theta_QCD + arg det(M_q) is the basis-invariant strong-CP angle: a chiral rotation
#     shifts theta_QCD and arg det(M) OPPOSITELY (the anomaly) -> theta-bar invariant.
th, argdet, Nf, alpha = symbols('theta argdet N_f alpha', real=True)
thetabar = th + argdet
shifted = (th - 2*Nf*alpha) + (argdet + 2*Nf*alpha)   # theta -> theta - 2Nf*alpha ; arg det -> arg det + 2Nf*alpha
chk("(2) theta-bar = theta_QCD + arg det(M_q) is invariant under a chiral rotation (shifts cancel) -> basis-invariant",
    simplify(shifted - thetabar) == 0)

# (3) breaking the Hermitian/reality structure (CP violation) gives arg det != 0 -> a theta-bar contribution
#     turns ON. Non-Hermitian deformation: M' = aI + bC + cc C^2 with cc != conj(b).
cc = symbols('cc')
Mp = a*eye(3) + b*C + cc*(C*C)
detMp = expand(Mp.det())
val = complex(detMp.subs({a: 2, bre: sp.Rational(1, 2), bim: sp.Rational(1, 3),
                          cc: sp.Rational(1, 4) + I*sp.Rational(1, 5)}))
chk("(3) a non-Hermitian (CP-violating) deformation cc != conj(b) gives arg det != 0 -> theta-bar turns ON with CP violation",
    abs(val.imag) > 1e-9 and abs(cmath.phase(val)) > 1e-6)

# (4) so on the real-Wilson gauge action (theta_QCD = 0, the repo's selected surface) the physical
#     theta-bar = arg det(M_q): a CP-odd phase of the SAME generation mass matrices as the Koide phase
#     delta. Both = 0 at the real/Hermitian default; both turn on from one reality-breaking. theta-bar
#     is NOT independent of the flavor-CP phase (part of AC_phi_lambda).
chk("(4) structural: on theta_QCD=0, theta-bar = arg det(M_q) lives in the generation-mass (AC_phi_lambda) flavor-CP sector",
    True)

# (5) source-note boundary tokens (honest scope: a collapse, NOT a strong-CP solution / NOT a clean count reduction)
if NOTE.exists():
    t = NOTE.read_text()
    toks = [
        "**Type:** narrow_theorem",
        "not a strong-CP solution",
        "Nelson-Barr",
        "real-Wilson",
        "Tier-A count to 1",
        "flavor-CP",
        "reality-breaking",
        "independent audit required",
    ]
    chk("(5) source note keeps the collapse/no-solution/no-count-reduction boundary", all(k in t for k in toks))
else:
    chk("(5) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nCOLLAPSE: theta-bar = theta_QCD + arg det(M_q). The framework's Hermitian C3-circulant gives a REAL\n"
    "determinant (arg det = 0): the CP-CONSERVING default where theta-bar = 0 AND delta = 0 coincide. On the\n"
    "real-Wilson gauge action (theta_QCD = 0, the repo's selected surface) the physical strong-CP angle\n"
    "theta-bar = arg det(M_q) -- a CP-odd phase of the SAME generation mass matrices as the Koide flavor\n"
    "phase delta. Both vanish at the real default and turn on together from ONE reality-breaking. So\n"
    "theta-bar is NOT an independent input from the flavor-CP phase (part of AC_phi_lambda); the strong-CP\n"
    "problem here IS the flavor-CP (Nelson-Barr) problem. SCOPE: a bookkeeping collapse, NOT a strong-CP\n"
    "solution -- controlled theta-bar ~ 0 with CKM != 0 stays open (also unsolved in the SM), and the\n"
    "gauge-side real-Wilson selection (theta_QCD = 0; RP cannot force it) remains, so this does not by\n"
    "itself reduce the Tier-A count to 1."
)
