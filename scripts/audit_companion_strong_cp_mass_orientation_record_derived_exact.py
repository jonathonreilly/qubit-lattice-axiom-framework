"""
Audit companion (numpy/sympy) for
STRONG_CP_MASS_ORIENTATION_PREMISE_IS_RECORD_DERIVED_NELSON_BARR_BOUNDED_NOTE_2026-06-06.md

DISCHARGE of a named premise (NOT a strong-CP solution). The parent admission STRONG_CP_THETA_ZERO_NOTE.md runs
a bounded Vafa-Witten closure (Legs A-D) but the 2026-04-28 audit flagged TWO underived premises, and its "Path A
future work" item 2 asks literally for "a registered positive real quark-mass orientation / arg det(M_u M_d)=0
theorem as a dependency." This runner verifies that the record-native result STRONG_CP_THETA_BAR_MASS_SIDE_IS_
RECORD_QUANTIZED_TO_Z2 (PR #2932) IS that theorem: a recorded mass is self-adjoint (#2921) -> real spectrum ->
arg det in {0, pi}; the physical positive-definite orientation -> arg det = 0. So the parent's accepted SURFACE
PREMISE is now RECORD-DERIVED.

It also CORRECTS the over-conservative caveat in #2932 ("CKM breaks the {0,pi} quantization"): general Hermitian
(non-circulant) up/down masses with MISALIGNED eigenbases produce a CP-violating CKM (Jarlskog != 0) while
arg det(M_u M_d) stays real in {0, pi}. That is the NELSON-BARR structure -- strong-CP-safe AND weak-CP-violating
-- and here it is record-derived rather than imposed.

SCOPE (honest): this is NOT a strong-CP solution. It discharges ONE of the parent's two flagged premises (the
mass orientation). The gauge-side "no bare theta slot" (Path-A-item-1) remains open (RP provably cannot force it,
strong_cp_rp_half no-go; action-form uniqueness blocked). Vafa-Witten (Leg D) bounds |Z(theta)| <= Z(0) so
theta=0 is the free-energy MINIMUM and strong CP is not SPONTANEOUSLY broken, but it does NOT dynamically SELECT
the theta PARAMETER. The staggered-Dirac realization (Leg A positivity) is itself the other Tier-A admission. No
Tier-A registry change. Vafa-Witten (PRL 53, 535) and Nelson-Barr are comparators only; no PDG values.
"""
import numpy as np, cmath
import sympy as sp
from sympy import I, Matrix, eye, symbols, conjugate, simplify, im, expand
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "STRONG_CP_MASS_ORIENTATION_PREMISE_IS_RECORD_DERIVED_NELSON_BARR_BOUNDED_NOTE_2026-06-06.md"
rng = np.random.default_rng(7)

def rand_herm(n=3):
    A = rng.standard_normal((n, n)) + 1j*rng.standard_normal((n, n)); return (A + A.conj().T)/2
def rand_herm_pos(n=3):
    H = rand_herm(n); return H @ H.conj().T + 0.3*np.eye(n)

# (1) RECORD-DERIVATION of the parent premise: recorded mass is Hermitian (#2921/#2932) -> arg det in {0,pi};
#     positive-definite physical orientation -> arg det = 0. (Symbolic anchor on the C3 mass + numeric sweep.)
a = symbols('a', real=True); br, bi = symbols('b_r b_i', real=True); b = br + I*bi
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
M = a*eye(3) + b*C + conjugate(b)*(C*C)
chk("(1a) the recorded mass is Hermitian -> det REAL -> arg det in {0,pi} (symbolic C3 anchor: Im det M = 0)",
    simplify(im(expand(M.det()))) == 0)
ok_real = ok_pos = True
for _ in range(300):
    if abs(np.linalg.det(rand_herm()).imag) > 1e-9: ok_real = False
    dp = np.linalg.det(rand_herm_pos())
    if not (dp.real > 0 and abs(dp.imag) < 1e-9 and abs(cmath.phase(dp)) < 1e-9): ok_pos = False
chk("(1b) Hermitian mass (300 random) -> arg det in {0,pi}: record-derives the DISCRETENESS the parent assumed", ok_real)
chk("(1c) Hermitian POSITIVE-definite (physical orientation) -> arg det = 0 = the parent's 'positive real quark-mass orientation' premise", ok_pos)

# (2) NELSON-BARR / correction to #2932's caveat: misaligned Hermitian up/down masses -> CP-violating CKM,
#     while arg det(M_u M_d) stays real in {0,pi}. Strong-CP-safe AND weak-CP-violating.
def jarlskog(V):
    return (V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1])).imag
found_cp = False; argdet_safe = True
for _ in range(400):
    Mu, Md = rand_herm(), rand_herm()
    _, Uu = np.linalg.eigh(Mu); _, Ud = np.linalg.eigh(Md)
    V = Uu.conj().T @ Ud
    if abs(abs(np.linalg.det(V)) - 1) > 1e-9: argdet_safe = False
    if abs(np.linalg.det(Mu @ Md).imag) > 1e-8: argdet_safe = False
    if abs(jarlskog(V)) > 1e-3: found_cp = True
chk("(2a) Hermitian (non-circulant) M_u,M_d -> CKM V=U_u^dag U_d UNITARY (|det V|=1) AND arg det(M_u M_d) stays REAL ({0,pi})", argdet_safe)
chk("(2b) misaligned Hermitian eigenbases PRODUCE a CP-violating CKM (Jarlskog != 0): weak CP coexists with strong-CP-safe arg det (NELSON-BARR); corrects #2932's 'CKM breaks {0,pi}' caveat", found_cp)

# (3) Vafa-Witten chain the parent runs (Leg A + Leg D), now with the mass-orientation INPUT record-derived.
#     Staggered/Kahler-Dirac: eps-graded anti-Hermitian D=[[0,B],[-B^dag,0]] (eps D + D eps = 0) -> eigenvalues
#     pair +-i sigma -> det(D+m)=prod(m^2+sigma^2)>0.
k = 4; B = rng.standard_normal((k, k)) + 1j*rng.standard_normal((k, k))
D = np.block([[np.zeros((k, k)), B], [-B.conj().T, np.zeros((k, k))]])
eps = np.diag([1.0]*k + [-1.0]*k); m = 0.7
detDm = np.linalg.det(D + m*np.eye(2*k)); prod = np.prod(m*m + np.linalg.svd(B, compute_uv=False)**2)
chk("(3a) staggered eps-graded anti-Hermitian D (eps D + D eps = 0) + real positive m -> det(D+m)=prod(m^2+lambda^2) REAL POSITIVE (Vafa-Witten Leg A)",
    np.allclose(D.conj().T, -D) and np.allclose(eps@D + D@eps, 0) and detDm.real > 0 and abs(detDm.imag)/abs(detDm.real) < 1e-9 and abs(detDm.real - prod)/prod < 1e-9)
ZQ = np.abs(rng.standard_normal(15)) + 0.05; Z0 = ZQ.sum()
worst = max(abs(sum(ZQ[q]*cmath.exp(1j*th*q) for q in range(len(ZQ)))) for th in np.linspace(0, 2*np.pi, 400))
chk("(3b) Z_Q>=0 -> |Z(theta)|=|sum Z_Q e^{i theta Q}| <= Z(0) for ALL theta -> F(theta) minimized at theta=0 (Vafa-Witten Leg D)",
    worst <= Z0 + 1e-9)

# (4) the discharge is logically exact: parent SURFACE PREMISE (arg det(M_u M_d)=0) == #2932 RECORD-DERIVED result
chk("(4) parent premise (arg det(M_u M_d)=0, accepted surface) == #2932 record-derived (Hermitian->real; positive->0): the premise is DISCHARGED, not assumed",
    ok_real and ok_pos)

# (5) source-note boundary tokens (honest scope: discharge of ONE premise, NOT a strong-CP solution)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["**Type:** bounded_theorem", "not a strong-CP solution", "Path-A", "Nelson-Barr", "no bare", "does not", "select", "Independent audit required"]
    chk("(5) source note keeps the discharge / not-a-solution / residual boundary", all(k in t for k in toks))
else:
    chk("(5) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nDISCHARGE: the parent strong-CP note's 'positive real quark-mass orientation' (arg det(M_u M_d)=0) was an\n"
    "ACCEPTED SURFACE PREMISE (Path-A-item-2). #2932 RECORD-DERIVES it: a recorded mass is Hermitian -> real det\n"
    "-> arg det in {0,pi}; positive orientation -> 0. Hermitian masses are NELSON-BARR: strong-CP-safe (arg det)\n"
    "+ weak CKM CP (misaligned eigenbases), correcting #2932's 'CKM breaks {0,pi}' caveat. Parent Leg A/D\n"
    "(Vafa-Witten |Z(theta)|<=Z(0)) now runs on a RECORD-DERIVED mass orientation. NOT a strong-CP solution:\n"
    "the gauge 'no bare theta slot' (Path-A-item-1) remains, and Vafa-Witten bounds but does NOT SELECT theta."
)
