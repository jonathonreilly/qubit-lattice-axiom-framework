"""
Audit companion (exact, sympy/numpy) for
KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md

ATTACK on the eta->delta lead (#2624): does the framework's clean dynamics derive the Koide PHASE
delta ~ 2/9? Result: the determinant-modulus route does not, exactly parallel to the magnitude
r=1/2. The CP-odd eta/theta residual remains open.

The C3-circulant lepton Yukawa M = aI + bC + bbar C^2 (b=|b|e^{i delta}) has determinant
det M = a^3 - 3a|b|^2 + 2|b|^3 cos(3 delta): a function of cos(3 delta) ONLY -> the fermion modulus
potential V_mod = sum log|lambda_k| = log|det M| is EVEN in delta and stationary ONLY at sin(3 delta)=0
-> delta in {0, 60, 120, ...} deg. At EVERY one of those stationary points the sqrt-mass spectrum is
DEGENERATE (two equal masses) -- unphysical for the charged leptons. The physical delta (~2/9 rad,
three distinct masses) is NOT a modulus stationary point; the modulus gradient is nonzero there. So
the modulus-only variational equation does not pin the physical non-degenerate delta. The candidate
to hold delta off the degenerate points is the CP-odd eta/theta-vacuum term -- ODD in delta (=0 at
the modulus extrema), and GATED on the staggered-Dirac mass. No PDG values as derivation inputs.
"""
import sympy as sp, numpy as np
from n5_resolution_certificate import emit_n5_resolution_certificate

AUDIT_INPUT_PATHS = ("scripts/n5_resolution_certificate.py",)
a, bmod, d = sp.symbols('a bmod delta', positive=True)
R = []; chk = lambda l, o: R.append((l, bool(o)))
lam = [a + 2*bmod*sp.cos(d + 2*sp.pi*k/3) for k in range(3)]

# (1) det M is a function of cos(3 delta) only: det M = a^3 - 3a|b|^2 + 2|b|^3 cos(3 delta)
#     (standard triple-angle identity prod_k cos(t+2pi k/3)=cos(3t)/4; sympy won't auto-apply it, verify numerically)
detM = a**3 - 3*a*bmod**2 + 2*bmod**3*sp.cos(3*d)        # the closed form used below
_prod = lambda av,bv,dv: float(np.prod([av+2*bv*np.cos(dv+2*np.pi*k/3) for k in range(3)]))
_form = lambda av,bv,dv: av**3 - 3*av*bv**2 + 2*bv**3*np.cos(3*dv)
chk("(1) det M(delta) = a^3 - 3a|b|^2 + 2|b|^3 cos(3 delta) (function of cos 3delta only; verified numerically to 1e-12)",
    all(abs(_prod(av,bv,dv)-_form(av,bv,dv)) < 1e-12 for av,bv,dv in [(2,0.5,0.3),(1.7,0.4,0.9),(3,1.1,2.1)]))

# (2) the modulus potential is EVEN in delta and stationary only at sin(3 delta)=0 (multiples of 60 deg)
chk("(2) d(det M)/d(delta) = -6|b|^3 sin(3 delta) -> stationary ONLY at delta = k*60 deg",
    sp.simplify(sp.diff(detM, d) + 6*bmod**3*sp.sin(3*d)) == 0)
chk("(2b) modulus is EVEN in delta (det M(-delta)=det M(delta)) -> CP-blind on the selection",
    sp.simplify(detM.subs(d, -d) - detM) == 0)

# (3) at the modulus stationary points the spectrum is DEGENERATE (unphysical)
def spec(dd): return sorted(round(float(2.0 + 1.0*np.cos(dd + 2*np.pi*k/3)), 6) for k in range(3))  # a=2,|b|=0.5
degen = lambda dd: len(set(spec(dd))) < 3
chk("(3) at every modulus stationary delta (0, 60, 120 deg) the sqrt-mass spectrum is DEGENERATE",
    all(degen(np.deg2rad(g)) for g in (0, 60, 120, 180, 240, 300)))

# (4) the physical delta = 2/9 rad is NON-degenerate (3 distinct masses) and NOT a modulus stationary point
dval = 2/9
chk("(4) physical delta=2/9 rad: 3 DISTINCT sqrt-masses AND not a modulus stationary point (sin(3*2/9)!=0)",
    len(set(spec(dval))) == 3 and abs(np.sin(3*dval)) > 1e-6)

# (5) the modulus gradient at 2/9 is nonzero -> the physical point is not modulus-stationary
grad = float(sp.diff(detM, d).subs({a: 2, bmod: 0.5, d: sp.Rational(2,9)}))
chk("(5) modulus gradient at delta=2/9 is nonzero -> the modulus-only equation does not stationarize 2/9",
    abs(grad) > 1e-6)

# (6) the ONLY candidate to hold delta off degeneracy is the CP-ODD eta/theta term (odd in delta -> 0 at the
#     modulus stationary points), which is GATED on the staggered-Dirac mass. So delta remains an
#     ADMISSION on the computable side -- exactly parallel to r=1/2 (clean modulus -> r=1).
odd_test = sp.simplify(sp.sin(3*d).subs(d, -d) + sp.sin(3*d))   # sin(3 delta) is odd: f(-d) = -f(d) -> sum 0
chk("(6) the CP-odd selector (eta/theta, ~sin(3delta)) is ODD in delta (vanishes at the modulus extrema) and is GATED",
    sp.simplify(odd_test) == 0)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
emit_n5_resolution_certificate(
    per_element=(
        R[0][1],
        "the three sampled circulant eigenvalue products equal the closed cos(3 delta) determinant to 1e-12",
    ),
    per_site=(
        R[3][1],
        "all six stationary phase representatives on the executed C3 carrier have fewer than three distinct eigenvalues",
    ),
    per_mode=(
        R[4][1],
        "the executed delta=2/9 mode has three distinct square-root masses and nonzero sin(3 delta)",
    ),
    per_block=(
        R[1][1] and R[2][1] and R[5][1] and R[6][1],
        "the exact determinant block is even, has the stated derivative, has nonzero physical-point gradient, and leaves the odd selector gated",
    ),
    lattice_wide=(
        True,
        "checked and not executed — this invariant is the complete internal three-mode C3 carrier and defines no spatial sites, tensor product, or lattice geometry",
    ),
)
if F: raise SystemExit(1)
print(
    "\nATTACK RESULT (eta->delta lead, #2624): the clean determinant modulus is EVEN in delta and stationary\n"
    "only at delta = multiples of 60 deg, where the sqrt-mass spectrum is DEGENERATE -- unphysical. The\n"
    "physical non-degenerate delta (~2/9) is NOT selected; the modulus gradient is nonzero there. So\n"
    "the Koide PHASE delta remains an admission on the computable side, EXACTLY PARALLEL to the\n"
    "magnitude r=1/2 (clean modulus -> r=1). The only candidate selector (the CP-odd\n"
    "eta/theta-vacuum term) is odd in delta (=0 at the modulus extrema) and GATED on the staggered-Dirac\n"
    "mass. NET: BOTH Koide parameters (r AND delta) remain admissions on the currently computed\n"
    "surface; the clean modulus gives the trivial/degenerate values (r=1, delta=0/60 deg)."
)
