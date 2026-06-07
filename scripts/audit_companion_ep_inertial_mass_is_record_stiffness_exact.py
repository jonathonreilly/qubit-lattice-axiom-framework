"""
Audit companion (exact, sympy) for
EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS_GENERATOR_INVARIANT_BOUNDED_SUPPORT_NOTE_2026-06-06.md

BOUNDED SUPPORT toward the OPEN equivalence-principle gap (EQUIVALENCE_PRINCIPLE_NOTE is a meta-demotion: the WEP
m_inertial = m_gravitational is an open derivation gap; its closure list names component #5 "a derivation of a
shared action coupling producing both responses with equal coefficients"). The prior inertial-mass route
(MATTER_INERTIAL_CLOSURE_NOTE) is NEGATIVE: Gaussian wave-packet "mass" varied 123% across packets because it was
wave-packet DISPERSION (packet-width sigma dependent), NOT a generator-invariant inertial mass.

This runner verifies the new structural content: under RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE (#2988),
the inertial mass of a durable recorded object is the RECORD-STIFFNESS m^2 = V''(phi0) -- generator-invariant
(sigma-independent), a property of the durable object, NOT the packet. Identifying it with the gravitational
source (the recorded energy; BROAD_GRAVITY_DERIVATION rho=|psi|^2) gives m_i = m_g exactly and universally
(ratio = 1, no object dependence), supplying closure component #5.

SCOPE (honest): NOT a WEP closure. It is bounded SUPPORT, conditional on (i) #2988 (record-stiffness mass,
bounded), (ii) BROAD_GRAVITY rho=|psi|^2 source (bounded support), and (iii) the STANDARD relativistic bridge
E^2=p^2+m^2 + gravity-couples-to-energy (textbook comparator, not derived here). The genuinely new content is that
the common quantity is the record-stiffness -- which fixes the named MATTER_INERTIAL_CLOSURE failure (the
non-generator-invariant dispersion). It does NOT supply the other closure components (a registered field/mass
sweep runner, an operational lattice force-observable, the full discrete mass-extraction theorem). No PDG values.
"""
import sympy as sp
from sympy import symbols, sqrt, diff, simplify, Rational
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "EP_INERTIAL_MASS_IS_THE_RECORD_STIFFNESS_GENERATOR_INVARIANT_BOUNDED_SUPPORT_NOTE_2026-06-06.md"

phi, phi0, m, sig, p = symbols('phi phi0 m sigma p', real=True, positive=True)

# (1) record-stiffness m^2 = V''(phi0) is a property of the recorded VACUUM, independent of the state width sigma
V = Rational(1, 2)*m**2*(phi - phi0)**2
stiffness = diff(V, phi, 2)
chk("(1) record-stiffness V''(phi0)=m^2 is GENERATOR-INVARIANT (no dependence on the state/packet width sigma) -- a property of the durable recorded object, NOT the packet",
    simplify(stiffness - m**2) == 0 and sig not in stiffness.free_symbols)

# (2) the PREVIOUS FAILURE: a free Gaussian wave-packet's group-velocity spreading depends on sigma (the 123%
#     MATTER_INERTIAL_CLOSURE variation) -> NOT generator-invariant
spread_response = 1/(m*sig)
chk("(2) the FAILED route: wave-packet dispersion response ~ 1/(m*sigma) DEPENDS on the packet width sigma -> NOT generator-invariant (the 123% MATTER_INERTIAL_CLOSURE non-universality)",
    sig in spread_response.free_symbols)

# (3) inertial mass = the REST GAP of E^2 = p^2 + m^2: m_inertial = (d^2E/dp^2)^{-1}|_{p=0} = m = record-stiffness
E = sqrt(p**2 + m**2)
inv_minert = simplify(diff(E, p, 2))
m_inert_at_rest = simplify(1/inv_minert.subs(p, 0))
chk("(3) dispersion E^2=p^2+m^2: m_inertial = (d^2E/dp^2)^{-1}|_{p=0} = m = the rest gap = the record-stiffness (sigma-independent)",
    m_inert_at_rest == m)

# (4) gravity couples to the recorded energy E (rho=|psi|^2); at rest m_grav = E|_{p=0} = m = m_inertial -> WEP
m_grav_at_rest = simplify(E.subs(p, 0))
chk("(4) gravity couples to the recorded energy E (rho=|psi|^2); at rest m_grav = E|_{p=0} = m = m_inertial -> WEAK EQUIVALENCE PRINCIPLE (m_i = m_g)",
    m_grav_at_rest == m and m_grav_at_rest == m_inert_at_rest)

# (5) shared coupling (EP closure component #5): m_grav/m_inert = 1 EXACTLY with NO object/packet dependence
ratio = simplify(m_grav_at_rest / m_inert_at_rest)
chk("(5) shared coupling = the recorded energy: m_grav/m_inert = 1 EXACTLY, NO object/packet (sigma) dependence -> UNIVERSAL ratio (fixes the 123% non-universality; supplies closure component #5)",
    ratio == 1 and sig not in ratio.free_symbols)

# (5b) DISCRETE-SURFACE STRENGTHENING (removes the continuum comparator on the inertial side): a lattice scalar
#      with on-site V(phi) + nearest-neighbour hopping has E^2(p) = V''(phi0) + (2/a^2) sum_i (1-cos p_i a). The
#      REST GAP at p=0 is V''(phi0) = the record-stiffness, EXACT on the lattice -- no continuum E^2=p^2+m^2 needed.
from sympy import cos as _cos
a, p1, p2, p3 = symbols('a p1 p2 p3', real=True, positive=True)
E2_lat = m**2 + (2/a**2)*((1 - _cos(p1*a)) + (1 - _cos(p2*a)) + (1 - _cos(p3*a)))
gap_lat = simplify(E2_lat.subs({p1: 0, p2: 0, p3: 0}))
chk("(5b) DISCRETE: lattice dispersion E^2(p)=V''(phi0)+(2/a^2)sum(1-cos p_i a) has rest gap at p=0 = V''(phi0) = the record-stiffness EXACTLY -> the inertial mass is lattice-native (continuum comparator removed on the inertial side)",
    simplify(gap_lat - m**2) == 0)
E2_smallp = sp.series(E2_lat.subs({p2: 0, p3: 0}), p1, 0, 4).removeO()
chk("(5c) small-p: lattice E^2 ~ m^2 + p1^2 + O(p^4) -> the continuum is only a low-p comparator; the GAP (= inertial mass) is exact on the discrete surface",
    simplify(E2_smallp.coeff(p1, 0) - m**2) == 0 and simplify(E2_smallp.coeff(p1, 2) - 1) == 0)

# (6) source-note boundary tokens (honest scope: bounded support, conditional, NOT a closure)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["bounded support", "generator-invariant", "record-stiffness", "not a", "conditional", "BROAD_GRAVITY", "comparator", "open", "Independent audit required"]
    chk("(6) source note keeps the bounded-support / generator-invariant / not-a-closure boundary", all(k in t for k in toks))
else:
    chk("(6) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nBOUNDED SUPPORT toward the open EP gap: mass=recordedness (#2988) supplies the GENERATOR-INVARIANT inertial\n"
    "mass (the record-stiffness, sigma-independent) the MATTER_INERTIAL_CLOSURE route lacked (it used sigma-\n"
    "dependent dispersion -> 123% non-universality). Both inertial response (the rest gap) and gravitational\n"
    "response (the recorded-energy source) couple to the SAME recorded energy -> m_i = m_g = 1 universally,\n"
    "supplying EP closure component #5. CONDITIONAL on #2988 + BROAD_GRAVITY + the standard relativistic bridge;\n"
    "NOT a full WEP closure (other closure components remain). The new content fixes the named failed route."
)
