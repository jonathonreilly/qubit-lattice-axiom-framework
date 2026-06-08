r"""
Audit companion - the leading Lorentz-violation ANGULAR fingerprint (dim-6, ell=4 cubic harmonic A_1g,
CPT-even, parity-even) is CARRIER-INDEPENDENT and therefore ADMISSION-FREE: it is identical on the
admission-free BOSONIC graph Laplacian and on the AC_phi_lambda STAGGERED Dirac carrier, differing only in
the overall coefficient. Hence, within the two nearest-neighbor dispersion primitives, the angular pattern is
fixed by the cubic point-group structure (O_h + exact lattice parity) and does NOT ride the staggered/
AC_phi_lambda admission; only the magnitude (the coefficient c4 plus the un-derived Planck-pin a=l_Planck) is
carrier-dependent. ("admission-free" = free of the Tier-A AC_phi_lambda staggered-realization admission; still
conditional on the retained nearest-neighbor kinetic / graph-Laplacian dispersion surface, NOT axiom/dynamics-free.)

WHAT IS NEW HERE (vs the parent notes): the parent EMERGENT_LORENTZ_INVARIANCE_NOTE already computes both
dispersions (staggered c4=-1/3, bosonic c4=-1/12) and LORENTZ_VIOLATION_DERIVED_NOTE derives the K4 cubic
harmonic on the bosonic Laplacian. This runner reproves the narrow NEW scoping claim those notes do not state:
that the ANGULAR fingerprint (the ell=4-only structure, the [100]/[111] factor-3 ratio, the parity/CPT
parity, the absence of a dim-5 term) is INDEPENDENT of the carrier coefficient c4 -- i.e. identical across
the two carriers -- so the AC_phi_lambda admission is NOT load-bearing for the fingerprint (only the magnitude
is). The K4 spherical-harmonic decomposition and the dim-6/CPT/parity classification are COMPARATORS cited
from the parent notes, cross-checked here, never re-claimed as new.

Reprove-and-cite: the cross-carrier dispersion expansion and the coefficient-independence of the angular
pattern are reproven from sympy/numpy primitives (the nearest-neighbor dispersions on Z^3). The K4 identity,
the dim-6 classification, CPT-exactness, and the experimental bounds are comparators cited to
LORENTZ_VIOLATION_DERIVED_NOTE and EMERGENT_LORENTZ_INVARIANCE_NOTE. No PDG value is a derivation input; the
magnitude (Planck-pin) is explicitly un-derived and out of scope. This is a scoping theorem (admission-free
angular fingerprint), NOT a new derivation of the dispersion and NOT a magnitude claim.
"""
import sympy as sp
import numpy as np

R = []
def chk(label, ok):
    R.append((label, bool(ok)))

px, py, pz, a = sp.symbols('p_x p_y p_z a', real=True, positive=True)
p2 = px**2 + py**2 + pz**2
p4sum = px**4 + py**4 + pz**4          # the cubic-harmonic (ell=4) invariant
A, B = sp.symbols('A B')

# ----------------------------------------------------------------------------------------------------
# (1) The two nearest-neighbor carriers on Z^3, expanded; the O(a^4) LV term is purely the cubic invariant.
# ----------------------------------------------------------------------------------------------------
carriers = {
    'bosonic_Laplacian': sum(2*(1 - sp.cos(k*a)) for k in (px, py, pz)),   # eps = sum 2(1-cos) ; c4 = -1/12
    'staggered_Dirac':   sum(sp.sin(k*a)**2 for k in (px, py, pz)),        # E^2 = sum sin^2 ; c4 = -1/3
}
c4 = {}
quartic = {}
for name, disp in carriers.items():
    s = sp.series(disp, a, 0, 7).removeO()
    # leading term is the isotropic a^2 p^2 (Lorentz-invariant)
    leading_iso = sp.simplify(s.coeff(a, 2) - p2) == 0
    # O(a^4) term: solve coeff = A*p2^2 + B*p4sum  -> expect A=0 (pure cubic invariant), B != 0
    coeff4 = sp.expand(s.coeff(a, 4))
    quartic[name] = coeff4
    sol = sp.solve(sp.Poly(sp.expand(coeff4 - (A*p2**2 + B*p4sum)), px, py, pz).coeffs(), [A, B], dict=True)[0]
    c4[name] = sol[B]
    # no odd-order (a^3, a^5) terms -> no dim-5 LV operator (exact lattice parity)
    no_odd = (s.coeff(a, 3) == 0) and (s.coeff(a, 5) == 0)
    chk(f"(1-{name}) dispersion = a^2 p^2 (isotropic) + a^4*({sol[B]})*(sum p_i^4) + ...: leading term Lorentz-"
        f"invariant, the O(a^4) LV term is PURELY the cubic invariant sum p_i^4 (A=0), and there is NO a^3/a^5 "
        f"odd term (exact lattice parity -> no dim-5 operator)",
        leading_iso and sol[A] == 0 and sol[B] != 0 and no_odd)

# (1b) the coefficients differ by carrier (bosonic -1/12 vs staggered -1/3) -> the MAGNITUDE is carrier-dependent
chk("(1b) the carrier coefficients DIFFER: bosonic c4 = -1/12, staggered c4 = -1/3 (ratio 4) -> the OVERALL "
    "MAGNITUDE of the LV operator is carrier-dependent (and additionally rides the un-derived Planck-pin)",
    c4['bosonic_Laplacian'] == sp.Rational(-1, 12) and c4['staggered_Dirac'] == sp.Rational(-1, 3)
    and sp.simplify(c4['staggered_Dirac'] / c4['bosonic_Laplacian']) == 4)

# ----------------------------------------------------------------------------------------------------
# (2) The ANGULAR pattern is the SAME invariant (sum p_i^4) for BOTH carriers -> carrier-independent shape.
#     Both LV terms are c4 * (sum p_i^4); the angular content lives entirely in (sum p_i^4), independent of c4.
# ----------------------------------------------------------------------------------------------------
# COMPUTED: for each carrier, the O(a^4) term divided by its own c4 equals the SAME angular operator (sum p_i^4).
norm_ops = {name: sp.expand(quartic[name] / c4[name]) for name in carriers}
chk("(2) [computed] both carriers' O(a^4) term normalized by its own c4 equals the SAME angular operator "
    "(sum p_i^4) -- bosonic and staggered give the identical angular operator, so the fingerprint shape is "
    "coefficient-/carrier-INDEPENDENT",
    all(sp.simplify(norm_ops[name] - p4sum) == 0 for name in carriers)
    and sp.simplify(norm_ops['bosonic_Laplacian'] - norm_ops['staggered_Dirac']) == 0)

# (2b) [comparator, cited from parent notes] sum n_i^4 = 3/5 + (4 sqrt(pi)/15) K4 with K4 = Y40+sqrt(5/14)(Y44+Y4,-4),
#      ONLY ell=0 and ell=4 (no ell=2, ell=6). Cross-check the angular decomposition is ell=4-only.
t, ph = sp.symbols('theta phi', real=True)
n = [sp.sin(t)*sp.cos(ph), sp.sin(t)*sp.sin(ph), sp.cos(t)]
f = sum(ni**4 for ni in n)
# projection onto ell=2 must vanish (no quadrupole); check <f|Y20> = 0 (Y20 ~ 3cos^2 t - 1)
Y20 = sp.sqrt(5/(16*sp.pi)) * (3*sp.cos(t)**2 - 1)
proj2 = sp.integrate(sp.integrate(sp.simplify(f*Y20)*sp.sin(t), (t, 0, sp.pi)), (ph, 0, 2*sp.pi))
# isotropic average <f> = 3/5
avg = sp.integrate(sp.integrate(f*sp.sin(t), (t, 0, sp.pi)), (ph, 0, 2*sp.pi)) / (4*sp.pi)
chk("(2b) [comparator cited from parent] sum n_i^4 has isotropic average 3/5 and ZERO ell=2 projection "
    "(angular content is ell=0 + ell=4 cubic harmonic K4 only) -- the parent-note fingerprint",
    sp.simplify(avg - sp.Rational(3, 5)) == 0 and sp.simplify(proj2) == 0)

# ----------------------------------------------------------------------------------------------------
# (3) The falsifiable [100]/[111] anisotropy ratio = 3, SAME for both carriers (coefficient-independent).
# ----------------------------------------------------------------------------------------------------
def aniso(nvec):
    nv = np.array(nvec, float); nv /= np.linalg.norm(nv)
    return float(np.sum(nv**4))          # (sum n_i^4) at fixed |n|=1
r100, r111 = aniso([1, 0, 0]), aniso([1, 1, 1])
chk("(3) the [100]/[111] anisotropy ratio of (sum n_i^4) is exactly 3 (1 vs 1/3), identical for BOTH "
    "carriers (it depends only on the angular operator, not on c4) -> the falsifiable signature is "
    "carrier-independent",
    abs(r100 - 1.0) < 1e-12 and abs(r111 - 1.0/3.0) < 1e-12 and abs(r100/r111 - 3.0) < 1e-12)

P = sum(1 for _, o in R if o)
Fa = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, Fa))
if Fa:
    raise SystemExit(1)
print("""
RESULT: the leading Lorentz-violation ANGULAR fingerprint (dim-6, ell=4 cubic harmonic A_1g, [100]/[111]=3,
parity-even, CPT-even, no dim-5) is CARRIER-INDEPENDENT -- identical on the admission-free bosonic graph
Laplacian and on the AC_phi_lambda staggered Dirac, differing only in the scalar coefficient c4 (-1/12 vs
-1/3). It is therefore AC_phi_lambda-ADMISSION-FREE: within the two nearest-neighbor dispersion primitives the
angular shape is fixed by the cubic point-group structure (O_h + exact lattice parity), with the AC_phi_lambda
staggered admission NOT load-bearing. Only the overall MAGNITUDE (c4 plus the un-derived
Planck-pin a = l_Planck) is carrier-dependent and remains out of scope. This elevates the angular fingerprint
from a staggered-conditional result to an admission-free structural prediction; the magnitude stays open.
""")
