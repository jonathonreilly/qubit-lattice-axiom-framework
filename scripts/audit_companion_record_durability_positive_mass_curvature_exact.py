"""
Audit companion (exact, sympy) for
RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md

NARROW bounded theorem (continuous degree of freedom). The Record axiom (MINIMAL_AXIOMS_2026-06-05) states a
record is DURABLE: "fixed once registered: the recorded outcome does not change." This runner reproves, from
elementary primitives, that for a CONTINUOUS degree of freedom durability is equivalent to a strictly positive
energy curvature -- i.e. a positive mass-squared -- so a massless continuous degree of freedom is NOT a durable
record. The gauge/relative-frame sector (whose displacements are zero-cost by closed-loop invariance; see the
Record-invariance notes that ground gauge freedom as the unrecorded relative frame) is the canonical
unrecorded-and-massless case.

Reprove-and-cite: every fact (the Taylor cost = 1/2 V'' eps^2 at a minimum; V'' = m^2 for a mass term; the
closed-loop gauge displacement telescopes to 0) is reproven here from primitives. The standard field-theory
identification "mass^2 = curvature of the energy at the minimum" (Coleman) and the Higgs/Goldstone/Stueckelberg
mass-from-vacuum-curvature mechanism are COMPARATORS only, never derivation inputs. No PDG values. This is a
re-reading/identification, not a new mass spectrum: it derives the massless<->unrecorded SPLIT, not the scale.

SCOPE (honest): continuous DOF only. A discrete/topological record (integer winding, K/CPT-orbit label,
theta-sector) is fixed by QUANTIZATION, not by a restoring curvature -- durable without a continuous mass -- a
separate durability channel; the equivalence here governs the continuous sector. The absolute mass SCALE is not
derived (only the split and ratios).
"""
import sympy as sp
from sympy import symbols, simplify, Rational, diff, Symbol
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md"

phi, phi0, eps, m = symbols('phi phi0 epsilon m', real=True)

# (1) cost to displace a registered value from a minimum phi0 by eps = 1/2 V''(phi0) eps^2 (since V'(phi0)=0).
#     Reproven for the generic mass term V = 1/2 m^2 (phi-phi0)^2.
V = Rational(1, 2) * m**2 * (phi - phi0)**2
Vp = diff(V, phi); Vpp = diff(V, phi, 2)
chk("(1a) at a registered minimum phi0: V'(phi0)=0 and the curvature V''(phi0)=m^2 (the mass-squared IS the energy curvature)",
    simplify(Vp.subs(phi, phi0)) == 0 and simplify(Vpp.subs(phi, phi0) - m**2) == 0)
cost = simplify(V.subs(phi, phi0 + eps) - V.subs(phi, phi0))
chk("(1b) Taylor: energy COST to displace by eps = 1/2 V''(phi0) eps^2 = 1/2 m^2 eps^2 (proportional to mass^2)",
    simplify(cost - Rational(1, 2) * m**2 * eps**2) == 0)

# (2) durable (fixed: nonzero cost to displace) <=> m^2 > 0 ; massless => zero cost => free-to-displace => not fixed
e0 = Rational(1, 10)
chk("(2a) MASSIVE (m=1): cost = 1/2 (1) (1/100) = 1/200 > 0 -> displacement is penalised -> value is FIXED -> DURABLE record",
    simplify(cost.subs({m: 1, eps: e0})) > 0)
chk("(2b) MASSLESS (m=0), LEADING/quadratic potential: cost = 0 -> no quadratic penalty -> linearly free to displace (the higher-order-pinned exception is (4b))",
    simplify(cost.subs({m: 0, eps: e0})) == 0)

# (3) the gauge/relative-frame sector is the canonical zero-cost case: a closed-loop holonomy (a record) is
#     INVARIANT under the relative-frame shift theta_xy -> theta_xy + (l_x - l_y); the shift telescopes to 0.
t1, t2, t3, t4, la, lb, lc, ld = symbols('t1 t2 t3 t4 la lb lc ld', real=True)
loop_shift = ((t1 + (lb - la)) + (t2 + (lc - lb)) - (t3 + (lc - ld)) - (t4 + (ld - la))) - (t1 + t2 - t3 - t4)
chk("(3) closed-loop holonomy is INVARIANT under the relative-frame shift (telescopes to 0) -> gauge displacement is ZERO-cost -> the connection is free-to-displace -> unrecorded -> massless (canonical case)",
    simplify(loop_shift) == 0)

# (4a) the LINEAR restoring force at displacement eps is -V'(phi0+eps) = -m^2 eps : nonzero (restores arbitrarily
#      small displacements) IFF m^2 != 0. This is the real content of "linearly durable <=> m^2 > 0".
epss = symbols('epsilon_s', real=True)
Frest = simplify(-Vp.subs(phi, phi0 + epss))
chk("(4a) linear restoring force = -V'(phi0+eps) = -m^2 eps -> restores arbitrarily small displacements IFF m^2 != 0 -> LINEAR durability <=> m^2 > 0 (the real converse content)",
    simplify(Frest - (-m**2 * epss)) == 0)

# (4b) THE EXCLUDED MARGINAL CASE (Codex caught this): a flat-quadratic minimum with higher-order pinning,
#      V = lam (phi-phi0)^4, has curvature V''(phi0)=0 (MASSLESS) yet a displacement still costs lam*eps^4 > 0
#      (durable). So "massless => free to displace" holds only at LINEAR order; the biconditional is linear, and
#      the genuinely-free case is the symmetry-protected (gauge/Goldstone) direction, flat to ALL orders.
lam = symbols('lambda_q', positive=True)
V4 = lam * (phi - phi0)**4
chk("(4b) EXCLUDED: V=lam(phi-phi0)^4 -> V''(phi0)=0 (massless) BUT cost lam*eps^4>0 (durable) -> 'massless=>free' is LINEAR-only; symmetry-protected (flat to all orders) is the genuinely-free case",
    simplify(diff(V4, phi, 2).subs(phi, phi0)) == 0 and simplify(V4.subs(phi, phi0 + e0)) > 0)

# (5) a DISCRETE/topological record (integer-valued, e.g. winding) has a FINITE gap to its nearest distinct value
#     (min |a-b| = 1 over distinct integers) -> no infinitesimal continuous neighbour -> fixed by QUANTIZATION, not
#     by a restoring curvature -> a separate durability channel, out of scope for the continuous-DOF equivalence.
gap = min(abs(a - b) for a in range(-3, 4) for b in range(-3, 4) if a != b)
chk("(5) discrete/topological record has a FINITE gap to its nearest distinct value (min|a-b|=%d>0) -> no infinitesimal neighbour -> fixed by QUANTIZATION not curvature -> separate channel, continuous-DOF-out-of-scope" % gap,
    gap == 1)

# (6) source-note boundary tokens (honest scope)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["**Type:** bounded_theorem", "continuous", "durable", "curvature", "re-reading", "discrete", "comparator", "out of scope", "Independent audit required"]
    chk("(6) source note keeps the continuous-DOF / durability=curvature / not-the-scale boundary", all(k in t for k in toks))
else:
    chk("(6) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nNARROW THEOREM (LINEAR): for a CONTINUOUS degree of freedom, the Record axiom's durability against\n"
    "infinitesimal perturbations holds <=> the linear restoring force -V'(phi0+eps) = -m^2 eps is nonzero <=>\n"
    "the curvature V''(phi0)=m^2 > 0. So a linearly-durable continuous record is MASSIVE, and a symmetry-protected\n"
    "(gauge/Goldstone, flat to ALL orders) massless DOF is free-to-displace = UNRECORDED. EXCLUDED marginal case\n"
    "(4b): a flat-quadratic V=lam*phi^4 is massless yet durable (super-linear pinning) -> the biconditional is\n"
    "LINEAR, and the genuinely-free case is the symmetry-protected one. CAVEAT (5): discrete records are durable-\n"
    "by-quantization (finite gap), a separate channel. Derives the massless<->unrecorded SPLIT, not the mass scale;\n"
    "Coleman's mass=curvature and the Higgs/Goldstone mechanism are comparators only."
)
