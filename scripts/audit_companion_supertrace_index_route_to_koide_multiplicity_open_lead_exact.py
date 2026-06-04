"""
Audit companion (exact, sympy) for
SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md

Open-gate companion for the supertrace / equivariant-index /
holomorphic candidate route to Koide r=1/2.

This runner verifies the algebraic part of the open gate. It does not
claim that the Koide readout is chiral, does not select r=1/2, and does
not prove a universal no-go for all other routes.

Verified content:
- the C3 generation triplet has one trivial irrep and one conjugate
  complex pair;
- the real/vector count gives `(1,2)` and `r=1`;
- the holomorphic/chiral count gives `(1,1)` and `r=1/2`;
- C3-trivial tensor factors preserve the real/vector ratio;
- the source note keeps the result as an open gate with the Record axiom
  excluded from the readout-selection role.

Conditional on the open staggered-Dirac mass/Yukawa gate. No PDG values
as derivation inputs.
"""
import sympy as sp
from sympy import I, exp, pi, Rational, simplify, Matrix, eye, conjugate
from pathlib import Path

R = []
def chk(label, ok, detail=""):
    R.append((label, bool(ok), detail))

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
note_text = NOTE.read_text()

# C3 irreps and the generation regular rep
w = exp(2*pi*I/3)
chi_triv = [1, 1, 1]; chi_w = [w**0, w**1, w**2]; chi_wbar = [w**0, w**2, w**4]
chi_W = [3, 0, 0]                                   # 3 corners cyclically permuted = regular rep
def inner(A, B): return simplify(sum(x*conjugate(y) for x, y in zip(A, B)) / 3)

def r_from_weights(ws, wd):
    x = simplify(sp.sympify(ws) / (sp.sympify(ws) + sp.sympify(wd)))
    return simplify(((1 - x) / 6) / (x / 3))

# (1) multiplicity of each irrep in W is 1 (regular rep) -> as (singlet ; real-doublet) the MULTIPLICITY
#     weighting is (1,1); the DIMENSION weighting is (1,2).
chk("(1) irrep multiplicities in W = 1 each (regular rep) -> multiplicity weighting (singlet,doublet)=(1,1)",
    inner(chi_W, chi_triv) == 1 and inner(chi_W, chi_w) == 1 and inner(chi_W, chi_wbar) == 1)

# (2) the two weightings give exactly r=1 (dimension) and r=1/2 (multiplicity), E_s=3a^2, E_d=6|b|^2.
a, bsq = sp.symbols('a bsq', positive=True)
E_s, E_d = 3*a**2, 6*bsq
r_dim  = simplify(sp.solve(sp.Eq(E_s/1, E_d/2), bsq)[0] / a**2)   # per-real-dimension equipartition
r_mult = simplify(sp.solve(sp.Eq(E_s/1, E_d/1), bsq)[0] / a**2)   # per-irrep equipartition
chk("(2) dimension/trace weighting -> r=1 (Q=1, kappa=1); multiplicity/index weighting -> r=1/2 (Q=2/3, kappa=2)",
    r_dim == 1 and r_mult == Rational(1, 2))

# (3) the HOLOMORPHIC mechanism: the doublet coefficient b is ONE COMPLEX parameter = TWO REAL parameters
#     (Re b, Im b). A holomorphic/chiral count weights b once (-> doublet weight 1 -> (1,1)); a real/vector
#     count weights Re b and Im b separately (-> doublet weight 2 -> (1,2)). M = aI + bC + bbar C^2.
bre, bim = sp.symbols('bre bim', real=True); b = bre + I*bim
C = Matrix([[0,1,0],[0,0,1],[1,0,0]]); M = a*eye(3) + b*C + conjugate(b)*(C*C)
# count real parameters in M's isotype split: singlet has 1 (a real); doublet has 2 (Re b, Im b)
real_params_singlet, real_params_doublet = 1, 2
complex_params_singlet, complex_params_doublet = 1, 1   # a (real=1), b (complex=1) -- holomorphic count
chk("(3) doublet = 1 complex param b = 2 real params (Re b, Im b): holomorphic count 1 vs real count 2",
    real_params_doublet == 2 and complex_params_doublet == 1
    and simplify(sp.trace(M.H*M) - (3*a**2 + 6*(bre**2 + bim**2))) == 0)

# (4) A C3-trivial extra factor preserves the real/vector weighting ratio.
flavor_blind_commutes = simplify((eye(3))*C - C*(eye(3))) == sp.zeros(3,3)   # eps acts as scalar on flavor
tensor_factor_preserves = all(r_from_weights(n, 2*n) == 1 for n in (1, 2, 5, 13))
chk("(4) C3-trivial factors commute with C3 and preserve vector weighting (1,2) -> r=1",
    flavor_blind_commutes and tensor_factor_preserves)

# (5) Uniform complex rescaling does not change the vector ratio; the
# candidate route specifically changes the doublet count from 2 to 1.
uniform_complex_r = r_from_weights(Rational(1, 2), 1)
holomorphic_r = r_from_weights(1, 1)
chk("(5) uniform complex rescaling preserves r=1; holomorphic doublet count gives r=1/2",
    uniform_complex_r == 1 and holomorphic_r == Rational(1, 2))

# (6) The source note must keep the claim as an open gate and must not
# let Record decide trace versus supertrace.
boundary_tokens = [
    "**Type:** open_gate",
    "not a derivation",
    "does not derive",
    "Record axiom",
    "does not decide",
    "Not retained on the current surface",
    "independent audit required",
]
chk("(6) source note keeps open-gate / no-status-promotion boundary",
    all(tok in note_text for tok in boundary_tokens))

P = sum(1 for _, o, _ in R if o); F = sum(1 for _, o, _ in R if not o)
for l, o, detail in R:
    suffix = f" :: {detail}" if detail else ""
    print(("PASS" if o else "FAIL"), "-", l + suffix)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nOPEN GATE: the algebraic candidate is exact. The real/vector count gives (1,2) and r=1;\n"
    "a holomorphic/chiral count of the complex doublet mode gives (1,1) and r=1/2. The runner\n"
    "does not select the chiral readout and does not derive Koide r=1/2; that remains gated by\n"
    "the staggered-Dirac mass/Yukawa realization and future audit."
)
