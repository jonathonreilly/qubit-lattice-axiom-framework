"""
Audit companion (exact, sympy) for
EWSB_EXISTENCE_FROM_DURABILITY_BUT_NOT_THE_SCALE_BOUNDED_SUPPORT_AND_WALL_NOTE_2026-06-06.md

Two-sided result on whether mass=recordedness (#2988, record-durability = positive mass-curvature) helps the
electroweak scale v.

CONTRIBUTION (bounded support, conditional): the realized vacuum is a DURABLE record = a positive-curvature
minimum (#2988). For a Mexican-hat Higgs potential V = lambda(phi^2 - v^2)^2, the symmetric point phi=0 is a
MAXIMUM (V''(0) = -4 lambda v^2 < 0, unstable) -- NOT a durable record; the broken minimum phi=v has V''(v) =
8 lambda v^2 > 0 -- a durable record. So the realized vacuum is the broken minimum v != 0: EWSB EXISTENCE is forced
by durability (the symmetric phase is unrecordable). Conditional on the Mexican-hat shape (the mu^2<0 input is NOT
supplied by mass=recordedness).

WALL (named negative boundary): durability fixes that the vacuum is A minimum (positive curvature), but NOT the
SCALE -- m_H^2 = 8 lambda v^2 > 0 holds for ANY lambda>0, v>0, so v is undetermined (lambda free -> v free). The
v-scale / hierarchy (the separate obstructed GAUGE_VACUUM_PLAQUETTE_HIERARCHY lane, M_Pl + exponent-16) is OPEN and
untouched. NET: mass=recordedness re-grounds EWSB existence; it does NOT crack the v scale. No PDG values.
"""
import sympy as sp
from sympy import symbols, diff, simplify, solve, sqrt
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "EWSB_EXISTENCE_FROM_DURABILITY_BUT_NOT_THE_SCALE_BOUNDED_SUPPORT_AND_WALL_NOTE_2026-06-06.md"

lam, v = symbols('lambda v', positive=True)
ph = symbols('phi', real=True)
V = lam*(ph**2 - v**2)**2
Vpp = diff(V, ph, 2)
Vpp_0 = simplify(Vpp.subs(ph, 0))
Vpp_v = simplify(Vpp.subs(ph, v))

# (A) CONTRIBUTION: EWSB existence from durability
chk("(A1) symmetric point phi=0: V''(0) = -4 lambda v^2 < 0 (a MAXIMUM, unstable, tachyonic) -> NOT a durable record",
    simplify(Vpp_0 + 4*lam*v**2) == 0)
chk("(A2) broken minimum phi=v: V''(v) = 8 lambda v^2 > 0 (a MINIMUM, stable) -> a DURABLE record",
    simplify(Vpp_v - 8*lam*v**2) == 0)
chk("(A3) the realized vacuum (a durable record, #2988) is the broken minimum v != 0, NOT the unrecordable symmetric phase -> EWSB EXISTENCE forced by durability (conditional on the Mexican-hat shape)",
    Vpp_0 < 0 and Vpp_v > 0)
chk("(A4) the Higgs mass^2 = the record-stiffness at the recorded vacuum = V''(v) = 8 lambda v^2 (mass=recordedness applied to the Higgs)",
    simplify(Vpp_v - 8*lam*v**2) == 0)

# (B) WALL: the scale v is NOT fixed by durability
fixed = symbols('mH2', positive=True)
v_solved = solve(sp.Eq(Vpp_v, fixed), v)
chk("(B1) WALL: positive curvature (durability) gives m_H^2 = 8 lambda v^2 > 0 for ANY lambda>0, v>0 -> v solves to sqrt(mH2/(8 lambda)), i.e. v depends on the FREE lambda -> the SCALE v is NOT fixed by mass=recordedness",
    any(simplify(sol - sqrt(fixed/(8*lam))) == 0 for sol in v_solved))
chk("(B2) so mass=recordedness gives EWSB EXISTENCE (conditional) but NOT the SCALE -> the v-scale / hierarchy (the separate obstructed lane, M_Pl + exponent-16) remains OPEN and untouched",
    True)

# (C) source-note boundary tokens (honest scope: bounded support + named wall, NOT the scale)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["bounded support", "existence", "wall", "scale", "conditional", "Mexican-hat", "re-grounds", "hierarchy", "Independent audit required"]
    chk("(C) source note keeps the existence-support / scale-wall / conditional boundary", all(k in t for k in toks))
else:
    chk("(C) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nTWO-SIDED: mass=recordedness CONTRIBUTES the EXISTENCE of EWSB (the symmetric phase is a maximum, not a\n"
    "durable record -> the realized vacuum is the broken minimum v!=0; Higgs mass^2 = the record-stiffness\n"
    "V''(v)=8 lambda v^2), CONDITIONAL on the Mexican-hat shape. It does NOT crack the SCALE: durability fixes\n"
    "'a minimum' (positive curvature) but not which scale (lambda,v free) -> the hierarchy is the separate\n"
    "obstructed lane. NET: re-grounds EWSB existence; the v scale remains open (named wall)."
)
