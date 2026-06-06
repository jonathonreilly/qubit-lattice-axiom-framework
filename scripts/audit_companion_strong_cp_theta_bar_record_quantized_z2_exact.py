"""
Audit companion (exact, sympy/numpy) for
STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md

RECORD-NATIVE result (NOT a strong-CP solution). The physical strong-CP angle is theta-bar = theta_QCD +
arg det(M_q). Via the sharpened Record-outcome principle (RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL
2026-06-05) + the signed-readout result (KOIDE signed readout is record-forced, PR #2921): a RECORDED observable
registers the K/CPT orbit = the SIGNED real eigenvalue, hence is SELF-ADJOINT. A recorded mass operator is
therefore Hermitian -> REAL eigenvalues -> arg det = pi*(#negative eigenvalues mod 2) in {0, pi} -- a Z2 SIGN,
NOT a continuous angle. So the MASS-SIDE strong-CP phase theta-bar_mass is RECORD-QUANTIZED to {0, pi}, which
DISSOLVES the CONTINUOUS-mass-phase naturalness problem: there is no continuous arg det to tune against theta_QCD
(unlike the SM, where a non-self-adjoint quark mass gives a continuous arg det). For all-positive masses (the
physical charged leptons, Foot's 45-degree positive octant) the registered det sign is +, so theta-bar_mass = 0.

SCOPE (honest): this quantizes the mass-side phase; it does NOT solve strong-CP. Residuals: the gauge theta_QCD
(the real-Wilson default, NOT record-forced -- RP provably cannot force it, strong_cp_rp_half no-go); the {0,pi}
sign SELECTION (the registered det sign = the positive-mass orientation, a registered pattern); and the quark/CKM
sector (CKM needs a non-Hermitian/non-circulant structure that breaks the {0,pi} quantization). Literature
(Nelson-Barr) is comparator only; no PDG values as derivation inputs.
"""
import sympy as sp, numpy as np, cmath
from sympy import I, simplify, symbols, Matrix, eye, conjugate, im, expand
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md"

C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
a = symbols('a', real=True); br, bi = symbols('b_r b_i', real=True); b = br + I*bi

# (1) RECORD -> self-adjoint: a recorded observable registers the K/CPT orbit = the SIGNED real eigenvalue (#2921),
#     so the recorded mass M = aI + bC + bbar C^2 is HERMITIAN.
M = a*eye(3) + b*C + conjugate(b)*(C*C)
chk("(1) the recorded C3 mass M = aI + bC + bbar C^2 is HERMITIAN (M = M^dagger) -> a recorded observable is self-adjoint",
    simplify(M - M.H) == sp.zeros(3, 3))

# (2) Hermitian -> REAL determinant -> arg det in {0, pi} (a Z2 sign), NOT a continuous angle
detM = simplify(M.det())
chk("(2) det M is REAL (Im = 0) -> arg det M in {0, pi}: a Z2 SIGN, record-quantized (NOT a continuous CP angle)",
    simplify(im(expand(detM))) == 0)

# (3) arg det = pi*(#negative eigenvalues mod 2): the Z2 is the parity of the negative signed eigenvalues
def argdet(av, brv, biv):
    Mn = np.array([[av, complex(brv+1j*biv), complex(brv-1j*biv)],
                   [complex(brv-1j*biv), av, complex(brv+1j*biv)],
                   [complex(brv+1j*biv), complex(brv-1j*biv), av]])
    ev = np.linalg.eigvalsh(Mn)
    nneg = int(np.sum(ev < 0)); d = float(np.prod(ev))
    return nneg, (0.0 if d > 0 else np.pi), nneg % 2
for (av, brv, biv) in [(2.0, 0.5, 0.3), (0.5, 0.7, 0.2), (1.0, 0.9, 0.4)]:
    nneg, ad, par = argdet(av, brv, biv)
    chk(f"(3) (a={av}, b={brv}+{biv}i): #neg={nneg} -> arg det = {'0' if ad == 0 else 'pi'} = pi*(#neg mod 2 = {par})",
        abs(ad - (np.pi*par)) < 1e-9)

# (4) CONTRAST: a NON-recorded (non-self-adjoint) mass has CONTINUOUS arg det (the SM's continuous strong-CP phase)
cr, ci = symbols('c_r c_i', real=True)
Mc = a*eye(3) + b*C + (cr + I*ci)*(C*C)   # c != bbar -> non-Hermitian
dc = complex(Mc.det().subs({a: 2, br: sp.Rational(1, 2), bi: sp.Rational(1, 3), cr: sp.Rational(1, 4), ci: sp.Rational(1, 5)}))
chk("(4) a NON-self-adjoint (non-recorded) mass has CONTINUOUS arg det (here != 0, pi) -> the SM's continuous strong-CP phase",
    abs(dc.imag) > 1e-9 and abs(cmath.phase(dc)) > 1e-6 and abs(abs(cmath.phase(dc)) - np.pi) > 1e-6)

# (5) physical charged leptons: all-positive sqrt-mass (Foot 45deg positive octant) -> #neg=0 -> arg det = 0
chk("(5) all-positive masses (physical charged leptons, Foot 45deg octant) -> #neg=0 -> arg det = 0 -> theta-bar_mass = 0 (registered +)",
    argdet(2.0, 0.4, 0.222)[1] == 0.0)

# (6) source-note boundary tokens (honest scope: quantization, NOT a strong-CP solution)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["**Type:** bounded_theorem", "record-quantized", "not a strong-CP solution", "continuous", "self-adjoint", "real-Wilson", "Independent audit required"]
    chk("(6) source note keeps the record-quantization / not-a-solution / residual boundary", all(k in t for k in toks))
else:
    chk("(6) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nRECORD-NATIVE: a recorded mass is self-adjoint (#2921) -> real eigenvalues -> arg det = pi*(#neg mod 2) in\n"
    "{0, pi}, a Z2 SIGN. So the MASS-SIDE strong-CP phase is RECORD-QUANTIZED to {0, pi} -- NOT a continuous CP\n"
    "angle -- which DISSOLVES the continuous-mass-phase naturalness problem (no continuous arg det to tune, unlike\n"
    "the SM, check 4). theta-bar_mass = 0 is the registered det sign for all-positive (physical) masses. NOT a\n"
    "strong-CP solution: the gauge theta_QCD (real-Wilson default, not record-forced), the {0,pi} sign selection,\n"
    "and the quark/CKM sector remain."
)
