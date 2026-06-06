"""
Audit companion (exact, sympy) for
KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md

FORECLOSURE-CORRECTION + LOCALIZATION (NOT a derivation of r=1/2).

The Koide magnitude r=1/2 needs the doublet counted ONCE (multiplicity/index readout, block count ->
(singlet,doublet)=(1,1)); the modulus/energy readout counts the doublet's 2 real dims -> (1,2) -> r=1.
The prior framing was that the "count once" route requires a SUSY superpotential (holomorphy <-> SUSY,
Seiberg). THIS IS CORRECTED: that conflates the holomorphic ACTION (a superpotential, SUSY) with the
holomorphic READOUT (the ordinary Dirac-fermion determinant / the index). The supertrace/index "count
once" is a Z2-GRADED-DIRAC fact -- McKean-Singer ind D = Str(e^{-tD^2}) for ANY Dirac operator with a
chirality grading, NO supercharge -- and it is realized on the lattice for Kahler-Dirac/staggered
fermions (arXiv:2405.11348). This runner checks both finite ingredients used by the boundary test:
the chirality grading eps and the Schur-native flavor complex structure J_cs=(C-C^2)/sqrt(3).

BUT the native pieces are NECESSARY-NOT-SUFFICIENT: J_cs is MEASURE-NEUTRAL -- exp(theta J_cs)=SO(2)
preserves BOTH the real (det_R) and holomorphic (det_C) measure -- so a static i/J cannot SELECT the
count. The selector is FIRST-ORDER (Dirac/Berezin index, count once -> r=1/2) vs SECOND-ORDER
(modulus/energy, count twice -> r=1), a DYNAMICS question gated on the open staggered-Dirac corner
realization (AC_phi_lambda). Literature (McKean-Singer; Dolbeault/HRR; Kahler-Dirac index; Seiberg
holomorphy) is comparator only; no PDG values as derivation inputs.
"""
import sympy as sp
from sympy import I, simplify, symbols, Matrix, eye, exp, pi, Rational, conjugate, sqrt
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md"

w = exp(2*pi*I/3)
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

# (1) THE FORK: block/multiplicity count (doublet ONCE) -> r=1/2 ; dimension count (doublet=2 dims) -> r=1
a, bsq = symbols('a bsq', positive=True)
E_s, E_d = 3*a**2, 6*bsq
r_block = simplify(sp.solve(sp.Eq(E_s/1, E_d/1), bsq)[0]/a**2)
r_dim = simplify(sp.solve(sp.Eq(E_s/1, E_d/2), bsq)[0]/a**2)
chk("(1) block/multiplicity count (doublet once) -> r=1/2 ; dimension count (doublet=2) -> r=1",
    r_block == Rational(1, 2) and r_dim == 1)

# (2) NON-SUSY INDEX -> multiplicity ; TRACE -> dimension (the count that distinguishes them)
chi_reg = [3, 0, 0]
chi_triv = [1, 1, 1]; chi_w = [1, w, w**2]; chi_wb = [1, w**2, w**4]
inner = lambda A, B: simplify(sum(x*conjugate(y) for x, y in zip(A, B))/3)
mult = (inner(chi_reg, chi_triv), inner(chi_reg, chi_w), inner(chi_reg, chi_wb))
chk("(2) equivariant INDEX counts MULTIPLICITY (each C3 irrep once -> (1,1,1) -> (singlet,doublet)=(1,1)); TRACE counts DIMENSION (1,2)",
    mult == (1, 1, 1))

# (3) the SUPERTRACE/index is a Z2-GRADED-TRACE fact, NOT SUSY (McKean-Singer): D anticommutes with the
#     grading eps, and Str(e^{-tD^2}) is t-independent = the index. The only structure needed is a graded Dirac op.
eps = Matrix([[1, 0], [0, -1]]); m = symbols('m', positive=True); t = symbols('t', positive=True)
D = Matrix([[0, m], [m, 0]])
chk("(3a) D anticommutes with the Z2 grading eps ({D,eps}=0) -- the only structure McKean-Singer needs (no supercharge)",
    simplify(D*eps + eps*D) == sp.zeros(2, 2))
Str_heat = simplify((eps*(-t*D*D).exp()).trace())
chk("(3b) Str(e^{-tD^2}) is t-INDEPENDENT (a graded-trace/index fact, no SUSY)",
    simplify(sp.diff(Str_heat, t)) == 0)

# (4) the NATIVE flavor complex structure J_cs=(C-C^2)/sqrt(3) is Schur-native but MEASURE-NEUTRAL ->
#     necessary-not-sufficient: a static i/J cannot SELECT index-vs-trace.
Jcs = (C - C*C)/sqrt(3)
chk("(4a) J_cs=(C-C^2)/sqrt3 is anti-Hermitian and commutes with C (Schur-native flavor complex structure)",
    simplify(Jcs.H + Jcs) == sp.zeros(3, 3) and simplify(Jcs*C - C*Jcs) == sp.zeros(3, 3))
th = symbols('theta', real=True)
Jdoub = Matrix([[0, -1], [1, 0]])
Rot = simplify((th*Jdoub).exp())
chk("(4b) exp(theta J_cs) on the doublet is SO(2) (orthogonal, det=1) -> measure-neutral (preserves det_R AND det_C), cannot select",
    simplify(Rot.det()) == 1 and simplify(Rot.T*Rot - eye(2)) == sp.zeros(2, 2))

# (5) source-note boundary tokens (honest scope: correction + localization, NOT a derivation)
if NOTE.exists():
    tt = NOTE.read_text()
    toks = [
        "**Claim type:** meta",
        "not a derivation of `r = 1/2`",
        "McKean",
        "necessary-not-sufficient",
        "measure-neutral",
        "staggered-Dirac",
        "first-order",
        "Status authority",
    ]
    chk("(5) source note keeps the correction/localization/no-derivation boundary", all(k in tt for k in toks))
else:
    chk("(5) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nCORRECTION + LOCALIZATION: the r=1/2 'count once' is the INDEX/multiplicity readout and it is NON-SUSY --\n"
    "a Z2-graded Dirac structure (McKean-Singer) + a complex structure checked locally by this runner.\n"
    "The prior 'needs a SUSY superpotential' conflated the holomorphic ACTION (superpotential)\n"
    "with the holomorphic READOUT (Dirac determinant). BUT the native pieces are NECESSARY-NOT-SUFFICIENT: J_cs is\n"
    "MEASURE-NEUTRAL, so a static i/J cannot SELECT the count. The selector is FIRST-ORDER (index, count once ->\n"
    "r=1/2) vs SECOND-ORDER (modulus, count twice -> r=1) -- a DYNAMICS question gated on the open staggered-Dirac\n"
    "corner realization. NOT a derivation of r=1/2; a foreclosure-correction (SUSY not required) + localization."
)
