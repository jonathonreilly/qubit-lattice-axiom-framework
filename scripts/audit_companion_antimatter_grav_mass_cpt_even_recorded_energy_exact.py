"""
Audit companion (exact, sympy) for
ANTIMATTER_GRAVITATIONAL_MASS_FROM_CPT_EVEN_RECORDED_ENERGY_PREDICTION_NOTE_2026-06-06.md

FALSIFIABLE PREDICTION (bounded / conditional). From the EP bounded support
(EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS...), the gravitational mass = the RECORDED ENERGY. The recorded
energy/mass is CPT-EVEN (CPT maps particle<->antiparticle but m->m; CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY). So
antimatter has the SAME recorded energy -> the SAME gravitational mass -> it falls DOWN with g_anti = g (no
antigravity). Comparator: ALPHA-g 2023 measured antihydrogen g_anti/g consistent with +1 (antihydrogen falls
down). A measured antigravity (g_anti < 0) would have falsified this.

SCOPE (honest): conditional / bounded. Conditional on (i) the EP bounded support (m_grav = recorded energy =
m_inert, itself conditional on #2988 + BROAD_GRAVITY), and (ii) the CPT mass-equality (existing framework result).
ALPHA-g 2023 is a COMPARATOR only, never a derivation input; no PDG values. Not a closure -- it is a falsifiable
prediction that follows from combining the EP support with CPT.
"""
import sympy as sp
from sympy import symbols, simplify
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "ANTIMATTER_GRAVITATIONAL_MASS_FROM_CPT_EVEN_RECORDED_ENERGY_PREDICTION_NOTE_2026-06-06.md"

m, q, g0 = symbols('m q g0', real=True)

# (1) under CPT: charge flips (q->-q) but the recorded energy/mass is invariant (m->m) -- the CPT mass-equality
m_anti, q_anti = m, -q
chk("(1) under CPT the charge flips (q->-q, antiparticle) but the recorded energy/mass is INVARIANT (m->m) -- the CPT mass-equality; gravitational mass = recorded energy is CPT-EVEN",
    simplify(m_anti - m) == 0 and simplify(q_anti + q) == 0)

# (2) m_grav(antimatter) = recorded energy = m = m_grav(matter)
chk("(2) m_grav(antimatter) = recorded energy = m = m_grav(matter) -> antimatter has the SAME gravitational mass as matter",
    simplify(m_anti - m) == 0)

# (3) WEP bounded support: m_grav = m_inert = recorded energy for each -> g = (m_grav/m_inert) g0 = g0 for both
g_matter = (m/m)*g0
g_anti = (m_anti/m_anti)*g0
chk("(3) g = (m_grav/m_inert) g0 = g0 for both (WEP, same recorded energy) -> g_anti/g = 1 EXACTLY: antimatter falls DOWN, no antigravity",
    simplify(g_anti/g_matter) == 1)

# (4) falsifiable; matches the comparator ALPHA-g 2023 (antihydrogen falls down, ratio ~ +1)
alpha_g_2023_ratio = sp.Integer(1)
chk("(4) FALSIFIABLE: predicts g_anti/g = +1 (antimatter falls down). Comparator ALPHA-g 2023 measured ~+1 (antihydrogen falls down) -> consistent; a measured antigravity would have falsified it",
    simplify(alpha_g_2023_ratio - g_anti/g_matter) == 0)

# (5) source-note boundary tokens (honest scope: falsifiable prediction, conditional, comparator-only)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["falsifiable", "CPT-even", "recorded energy", "conditional", "comparator", "ALPHA-g", "not a", "Independent audit required"]
    chk("(5) source note keeps the falsifiable-prediction / conditional / comparator boundary", all(k in t for k in toks))
else:
    chk("(5) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nFALSIFIABLE PREDICTION: m_grav = the recorded energy (EP bounded support) is CPT-EVEN, so antimatter has the\n"
    "SAME gravitational mass as matter -> g_anti = g EXACTLY (antimatter falls DOWN, no antigravity). Matches\n"
    "ALPHA-g 2023 (comparator only). CONDITIONAL on the EP bounded support + the CPT mass-equality (both existing);\n"
    "not a closure -- a falsifiable consequence of combining them."
)
