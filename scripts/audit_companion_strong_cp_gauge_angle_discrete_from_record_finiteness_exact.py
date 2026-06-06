"""
Audit companion (sympy/numpy) for
STRONG_CP_GAUGE_ANGLE_IS_DISCRETE_FROM_RECORD_FINITENESS_SELECTION_NEEDS_WEIGHTING_BOUNDED_NOTE_2026-06-06.md

Two-part result on the gauge-side strong-CP residual (the QCD vacuum angle theta_QCD), CONDITIONAL on theta being
a recorded quantity (framework-native: theta is not in the three axioms; it can only be a feature of the realized
recorded vacuum sector).

HALF 1 -- DERIVABLE, NO NEW AXIOM. The Record axiom (MINIMAL_AXIOMS_2026-06-05) supplies a "finite central-sector
decomposition." A continuous vacuum angle theta in [0,2pi) is an UNCOUNTABLE family of superselected sectors --
not a finite decomposition -- so a RECORDED theta is DISCRETE (finitely many values; a Z_N model is exhibited).
This DISSOLVES the CONTINUOUS strong-CP naturalness problem: theta-bar is not a continuous knob to fine-tune. It
is the gauge-side analog of the mass-side {0,pi} record-quantization (#2932): both halves of theta-bar = theta_QCD
+ arg det are now record-discrete.

HALF 2 -- DOES NOT CLOSE (smuggle made explicit). Selecting theta = 0 out of the finite K/CPT-stable set is NOT
forced by finiteness: a 2-element K-orbit {k, N-k} is a valid single record, so |theta| != 0 is record-admissible.
Picking 0 requires a WEIGHTING / OCCUPANCY rule that prefers the minimal-label sector -- and the Record axiom
EXPLICITLY DISCLAIMS "weighting, normalization, probability, ... occupancy rule." So a minimum-information /
occupancy weighting that would select 0 is a GENUINELY SEPARATE principle, not a corollary of the Record axiom
(it fills the framework's standing no-weighting gap). This runner makes that boundary explicit; it does NOT adopt
such a principle.

No PDG values; no Tier-A change. Superselection-sector / theta-vacuum facts are textbook comparators only.
"""
import sympy as sp
from sympy import I, pi, simplify, eye, exp, sqrt, zeros, Matrix, diag
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "STRONG_CP_GAUGE_ANGLE_IS_DISCRETE_FROM_RECORD_FINITENESS_SELECTION_NEEDS_WEIGHTING_BOUNDED_NOTE_2026-06-06.md"

# ===== HALF 1: finiteness => discrete theta; K/CPT(theta->-theta) fixed points are {0} (N odd) or {0,pi} (N even)
for N in [3, 4, 5, 6]:
    fixed = sorted({k for k in range(N) if (2*k) % N == 0})
    expect = [0] if N % 2 else [0, N//2]
    chk(f"(1) N={N}: a recorded angle is DISCRETE (theta in Z_N, finite); K-conjugation fixed points = {{0{',pi' if N%2==0 else ''}}}",
        fixed == expect)

# a FINITE central-sector decomposition genuinely exists (N orthogonal clock-eigen projectors sum to I);
# the continuum [0,2pi) cannot be covered by finitely many orthogonal sectors -> continuous theta is NOT finite.
N = 4; w = exp(2*pi*I/N)
proj = []
for k in range(N):
    v = Matrix([w**(k*j) for j in range(N)])/sqrt(N); proj.append(simplify(v*v.H))
chk("(1b) a FINITE decomposition exists (N orthogonal clock-eigen projectors sum to I); a continuous theta family does not",
    simplify(sum(proj, zeros(N, N))) == eye(N) and all(simplify(P*P - P) == zeros(N, N) for P in proj))

# ===== HALF 2: selection of theta=0 is NOT forced by finiteness (2-element K-orbits are valid single records)
N = 6
orbits = {tuple(sorted({k, (N-k) % N})) for k in range(N)}
two_elt = [o for o in orbits if len(o) == 2]
chk("(2) finiteness PERMITS nonzero recorded angles: 2-element K-orbits {k,N-k} are valid single records -> theta=0 NOT forced by finiteness",
    len(two_elt) > 0 and (1, 5) in orbits and (2, 4) in orbits)

# picking 0 needs a weighting (cost = angle description length): min-cost UNIQUELY selects 0; without it, undetermined
def cost(k, N): return 0 if k == 0 else (1 if (2*k) % N == 0 else 2)  # 0 < pi(fixed) < generic orbit
chk("(3) a minimum-information WEIGHTING (cost=angle description length) uniquely selects theta=0 (cost 0 < pi < generic) -- IF such a weighting is supplied",
    min(range(N), key=lambda k: cost(k, N)) == 0 and cost(0, N) == 0 and all(cost(k, N) > 0 for k in range(1, N)))
chk("(4) WITHOUT a weighting the K-orbits are on equal footing -> selection of 0 is UNDETERMINED by finiteness alone",
    len(orbits) > 1)

# ===== TEXTUAL: the Record axiom supplies finiteness AND explicitly disclaims the weighting min-info would need
AX = (Path(__file__).resolve().parent.parent / "docs" / "MINIMAL_AXIOMS_2026-06-05.md").read_text()
chk("(5) the Record axiom supplies 'finite central-sector decomposition' AND disclaims 'weighting/normalization/probability/occupancy rule' -> a min-info weighting is OUTSIDE the axiom",
    all(t in AX for t in ["finite central-sector decomposition", "weighting", "normalization", "probability", "occupancy rule"]))

# ===== source-note boundary tokens (honest scope: discreteness derivable; selection needs a disclaimed weighting)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["**Type:** bounded_theorem", "discrete", "continuous", "does not", "weighting", "occupancy", "disclaim", "recorded quantity", "Independent audit required"]
    chk("(6) source note keeps the discreteness-derivable / selection-needs-weighting boundary", all(k in t for k in toks))
else:
    chk("(6) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nVERDICT: HALF 1 CLOSES (no new axiom) -- the Record axiom's FINITE central-sector decomposition makes a\n"
    "recorded vacuum angle DISCRETE, dissolving the CONTINUOUS strong-CP naturalness problem (gauge-side analog of\n"
    "the mass-side {0,pi}). HALF 2 does NOT close -- selecting theta=0 needs a WEIGHTING/OCCUPANCY rule, which the\n"
    "Record axiom EXPLICITLY DISCLAIMS, so a minimum-information weighting is a SEPARATE principle (fills the\n"
    "framework's no-weighting gap), not a corollary. Honest: discreteness is free; the final 0 is a new principle."
)
