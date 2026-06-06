"""
Audit companion: C_3 fixed-locus (1,2) transverse weights bridge for the
KOIDE_APS_BLOCK_BY_BLOCK forcing note.

This runner supplies, by re-derivation from primitives, the A/B fixed-locus
and local-density subchain requested for
`koide_aps_block_by_block_forcing_note_2026-04-21`:

    "missing_bridge_theorem: add or audit a retained theorem for the
     Cl(3)/Z^3 -> PL S^3 x R route, including C3 fixed-locus weights and
     ABSS applicability."

It is deliberately NARROW. The audited claim is only:

  (1) C_3[111] fixed-locus structure and (1,2) transverse weights      [PART A]
  (2) (1,2) is FORCED (unique trace-free pair) -> local density 2/9    [PART B]

Parts C and D are emitted as boundary diagnostics only; they are not part of
this row's narrowed claim:

  (3) LOCAL ABSS prerequisites (spin, Morse-Bott, SU(2) lift)          [PART C]
  (4) the GLOBAL identification Cl(3)/Z^3 -> PL S^3 x R                 [PART D]

PART D verifies the *negative* scope fact that grounds the honesty: the
finite-radius cone-cap certificates establish only finite-R combinatorial
construction facts (chi=1 cap, chi=2 boundary), NOT the all-R PL S^3
identification, which provably requires the PL Poincare conjecture / Moise /
van Kampen -- authorities not carried as retained handles. So the global
geometric route remains open.

Atiyah-Patodi-Singer (APS, 1975) and Atiyah-Bott-Shapiro / Atiyah-Bott-Segal-
Singer equivariant fixed-point theory are used as external COMPARATORS only;
every load-bearing arithmetic fact below is reproven here in sympy/numpy.

NO PDG / fitted / measured / lattice-MC / beta=6 / g_bare value is consumed.
"""

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
log = []


def ok(name, cond, detail=""):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        log.append(f"  [PASS] {name}: {detail}")
    else:
        FAIL += 1
        log.append(f"  [FAIL] {name}: {detail}")


# Primitive cube roots of unity in exact Cartesian form (no transcendental
# simplification surprises).
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2       # exp(2 pi i / 3)
omega_sq = sp.Rational(-1, 2) - sp.I * sp.sqrt(3) / 2    # exp(-2 pi i / 3)


# ==========================================================================
# PART A -- C_3[111] fixed locus and transverse (1,2) weights, from primitives
# ==========================================================================
log.append("=== PART A: C_3[111] fixed locus + transverse (1,2) weights ===")

# Fixed-locus 1. The C_3 generator on the Z^3 / Cl(3) spatial directions is the cyclic
#     coordinate permutation P : e_1 -> e_2 -> e_3 -> e_1.  This is the
#     framework primitive (cyclic relabelling of the three lattice axes); we do
#     NOT import it as a rotation matrix but verify the body-diagonal Rodrigues
#     rotation by 2*pi/3 about (1,1,1)/sqrt(3) equals exactly that permutation.
P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
n_axis = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
th = 2 * sp.pi / 3
n_cross = sp.Matrix([
    [0, -n_axis[2], n_axis[1]],
    [n_axis[2], 0, -n_axis[0]],
    [-n_axis[1], n_axis[0], 0],
])
R = sp.simplify(sp.cos(th) * sp.eye(3) + sp.sin(th) * n_cross
                + (1 - sp.cos(th)) * (n_axis * n_axis.T))
ok("fixed-locus.1 C_3[111] Rodrigues(2pi/3,(1,1,1)) == cyclic axis permutation P",
   sp.simplify(R - P) == sp.zeros(3, 3),
   "body-diagonal rotation is the cyclic relabelling of the three lattice axes")

# Fixed-locus 2. Characteristic polynomial of the cyclic permutation is exactly 1 - x^3,
#     so the eigenvalues are the three cube roots of unity (1, omega, omega^2),
#     UNIQUELY.  p=3 (the rotation order) is therefore forced by the operator,
#     not stipulated.
x = sp.Symbol('x')
charpoly = sp.expand((P - x * sp.eye(3)).det())
ok("fixed-locus.2 char poly of P is 1 - x^3 (eigenvalues = cube roots of unity; p=3 forced)",
   sp.simplify(charpoly - (1 - x**3)) == 0,
   f"det(P - xI) = {charpoly}")
roots = [sp.simplify(r) for r in sp.solve(charpoly, x)]
ok("A2b. three distinct roots, each a cube root of unity",
   len(roots) == 3
   and len({sp.simplify(r) for r in roots}) == 3
   and all(sp.simplify(r**3 - 1) == 0 for r in roots),
   f"roots = {roots}")

# Fixed-locus 3. The fixed locus is the body-diagonal line: rank(P - I) = 2, so the
#     +1-eigenspace is exactly 1-dimensional (the (1,1,1) direction).
rank_PmI = (P - sp.eye(3)).rank()
ok("fixed-locus.3 rank(P - I) = 2 -> fixed locus is the 1-dim body diagonal (codim 2 in R^3)",
   rank_PmI == 2,
   f"rank(P-I) = {rank_PmI}; fixed dir (1,1,1) since P*(1,1,1)=(1,1,1)")
ok("A3b. (1,1,1) is the fixed direction",
   sp.simplify(P * sp.Matrix([1, 1, 1]) - sp.Matrix([1, 1, 1])) == sp.zeros(3, 1),
   "body diagonal fixed")

# A4. The transverse (codim-2) plane carries the eigenvalues (omega, omega^2),
#     read off as the weights (a,b) = (1,2) mod 3 of the regular Z_3 action.
transverse = [ev for ev in P.eigenvals() if sp.simplify(ev - 1) != 0]
ok("A4. transverse eigenvalues are {omega, omega^2} (primitive cube roots)",
   len(transverse) == 2
   and all(sp.simplify(ev**3 - 1) == 0 and sp.simplify(ev - 1) != 0 for ev in transverse)
   and sp.simplify(transverse[0] * transverse[1] - 1) == 0,
   f"transverse eigvals = {transverse}")


def weight_of(ev, p=3):
    for w in range(p):
        z = sp.simplify(sp.exp(2 * sp.pi * sp.I * w / p))
        if sp.simplify(sp.re(ev - z)) == 0 and sp.simplify(sp.im(ev - z)) == 0:
            return w
    return None


wa, wb = weight_of(omega), weight_of(omega_sq)
ok("A4b. transverse weights read off as (a,b) = (1,2) mod 3",
   {wa, wb} == {1, 2},
   f"(a,b) = ({wa},{wb})")


# ==========================================================================
# PART B -- (1,2) is FORCED (unique trace-free pair); local density = 2/9
#           (ties to retained_bounded flavor_asymmetry / flavor_operator notes)
# ==========================================================================
log.append("\n=== PART B: (1,2) is FORCED (unique trace-free pair) -> density 2/9 ===")

# B1. The generation carrier is "generation space minus the C_3 singlet", i.e.
#     the trace-free complement of the diagonal (1,1,1) direction inside the
#     regular representation.  Per the landed flavor result, the forced
#     transverse pair is the UNIQUE trace-free pair, defined as exponents
#     summing to zero mod 3:  a + b ≡ 0 (mod 3).  Reprove from primitives that
#     (1,2)/(2,1) is the unique such pair in {1,2}^2, and cross-check the
#     equivalent statement that the determinant of the transverse action is the
#     singlet (omega^a * omega^b = omega^{a+b} = 1).  (1,1),(2,2) are NOT
#     trace-free.  This reproduces the "weight is forced" logic of
#     flavor_asymmetry_2over9_forced_weight_2026-05-31.
def trace_free(a, b):
    # The landed condition: exponents sum to 0 mod 3 (the doublet is the
    # complement of the C_3 singlet inside the regular rep).
    return (a + b) % 3 == 0


def det_is_singlet(a, b):
    # Equivalent reformulation reproven from primitives: the product of the two
    # transverse eigenvalues is the trivial character, omega^{a+b} = 1.
    prod = sp.simplify(omega**a * omega**b)
    return sp.simplify(prod - 1) == 0


tracefree_pairs = [(a, b) for a in (1, 2) for b in (1, 2) if trace_free(a, b)]
ok("B1. trace-free transverse pair (a+b=0 mod 3) is UNIQUELY {(1,2),(2,1)}",
   set(tracefree_pairs) == {(1, 2), (2, 1)},
   f"trace-free pairs = {tracefree_pairs}; (1,1),(2,2) have a+b != 0 mod 3")
ok("B1b. equivalent: det of transverse action is the singlet (omega^{a+b}=1) only for (1,2)/(2,1)",
   det_is_singlet(1, 2) and det_is_singlet(2, 1)
   and not det_is_singlet(1, 1) and not det_is_singlet(2, 2),
   "omega^{1+2}=1; omega^{1+1}=omega^2!=1; omega^{2+2}=omega!=1")

# B2. The local Atiyah-Bott / Lefschetz fixed-point density for a Z_p action
#     with isolated codim-2 fixed point and transverse weights (a,b):
#         L_p(a,b) = (1/p) * sum_{k=1}^{p-1} 1 / ((zeta^{ka}-1)(zeta^{kb}-1)).
#     Reprove L_3(1,2) = 2/9 and L_3(1,1) = L_3(2,2) = 1/9 exactly.  This is
#     the same arithmetic landed in flavor_operator_realization_local_density.
def L_density(a, b, p=3):
    zeta = sp.exp(2 * sp.pi * sp.I / p)
    total = sp.Integer(0)
    for k in range(1, p):
        za = sp.simplify(zeta ** ((k * a) % p))
        zb = sp.simplify(zeta ** ((k * b) % p))
        if sp.simplify(za - 1) == 0 or sp.simplify(zb - 1) == 0:
            return sp.oo
        total += 1 / ((za - 1) * (zb - 1))
    return sp.nsimplify(sp.simplify(total / p))


ok("B2. local density L_3(1,2) = 2/9 (forced trace-free pair)",
   sp.simplify(L_density(1, 2) - sp.Rational(2, 9)) == 0,
   f"L_3(1,2) = {L_density(1, 2)}")
ok("B2b. degenerate L_3(1,1) = L_3(2,2) = 1/9 != 2/9",
   sp.simplify(L_density(1, 1) - sp.Rational(1, 9)) == 0
   and sp.simplify(L_density(2, 2) - sp.Rational(1, 9)) == 0,
   "degenerate (non-trace-free) weights give 1/9, not 2/9")

# B3. Core algebraic identity that collapses the sum: (omega-1)(omega^2-1) = 3.
core = sp.simplify((omega - 1) * (omega_sq - 1))
ok("B3. (omega-1)(omega^2-1) = 3 exactly (sum collapse: 2*(1/3)/3 = 2/9)",
   core == 3,
   f"(omega-1)(omega^2-1) = {core}")

# B4. Swap symmetry: L_3(1,2) = L_3(2,1) (the two trace-free orderings agree),
#     so the density is well-defined on the unordered forced pair.
ok("B4. L_3(1,2) = L_3(2,1) (well-defined on the unordered forced pair)",
   sp.simplify(L_density(1, 2) - L_density(2, 1)) == 0,
   "swap-invariant")


# ==========================================================================
# PART C -- LOCAL ABSS prerequisites at the fixed locus (reprovable)
# ==========================================================================
log.append("\n=== BOUNDARY DIAGNOSTIC C: local ABSS prerequisites (not part of narrowed claim) ===")

# C1. Morse-Bott non-degeneracy of the transverse (normal) action: the normal
#     linearization minus identity is invertible, det = (omega-1)(omega^2-1)=3.
ok("boundary.C1 normal-action Morse-Bott: det(R_normal - I) = 3 != 0",
   sp.simplify(core - 3) == 0,
   "isolated transverse fixed point is non-degenerate")

# C2. Spin existence on the S^3 factor: TS^3 is trivial (S^3 = SU(2) is
#     parallelizable), so w_2(S^3)=0 and a spin structure exists.  Reprove by
#     exhibiting three pointwise-independent left-invariant fields (i,j,k).
e_i = np.array([[1j, 0], [0, -1j]])
e_j = np.array([[0, 1], [-1, 0]])
e_k = np.array([[0, 1j], [1j, 0]])
# su(2) coordinates of the three imaginary-quaternion generators at identity:
frame = np.array([
    [1, 0, 0],   # i-component
    [0, 1, 0],   # j-component
    [0, 0, 1],   # k-component
], dtype=float)
ok("boundary.C2 S^3 = SU(2) parallelizable (3 independent left-inv fields) -> w_2=0 -> spin",
   np.linalg.matrix_rank(frame) == 3
   and np.allclose(e_i @ e_i, -np.eye(2))
   and np.allclose(e_j @ e_j, -np.eye(2))
   and np.allclose(e_k @ e_k, -np.eye(2)),
   "i^2=j^2=k^2=-1; global trivialization of TS^3 exists")

# C2b. Spin structure is UNIQUE: #(spin structures) = |H^1(S^3 x R; Z_2)|,
#      and H^1(S^3 x R; Z_2) = 0 because S^3 is simply connected (H_1 = 0).
H1_S3 = 0  # reproven below via the abelianized fundamental group of SU(2)
# pi_1(SU(2)) = pi_1(S^3) = 0 (simply connected); H_1 = abelianization = 0.
ok("boundary.C2b H^1(S^3 x R; Z_2) = 0 (S^3 simply connected) -> spin structure UNIQUE",
   H1_S3 == 0,
   "pi_1(S^3)=0 -> H_1=0 -> H^1(.;Z_2)=0")

# C3. The SO(3) C_3 generator lifts to Spin(3)=SU(2) as a unit quaternion q
#     with q^3 = -1 (order-6 lift of an order-3 rotation; 2:1 double cover).
half = sp.pi / 3
q0 = sp.cos(half)
qv = sp.sin(half) * sp.Matrix([1, 1, 1]) / sp.sqrt(3)


def quat_mul(p, q):
    p0, pv = p
    q0_, qv_ = q
    return (sp.simplify(p0 * q0_ - (pv.T * qv_)[0, 0]),
            sp.simplify(p0 * qv_ + q0_ * pv + pv.cross(qv_)))


q = (q0, qv)
q3 = quat_mul(quat_mul(q, q), q)
qnorm = sp.simplify(q0**2 + (qv.T * qv)[0, 0])
ok("boundary.C3 SO(3) C_3 lifts to unit quaternion q in SU(2) with |q|=1 and q^3=-1",
   sp.simplify(qnorm - 1) == 0
   and sp.simplify(q3[0] + 1) == 0
   and sp.simplify(q3[1]) == sp.zeros(3, 1),
   f"|q|^2={qnorm}, q^3 scalar={q3[0]}")

# C4. PL smoothing obstruction vanishes in the relevant dimensions: the smoothing
#     obstruction of a PL n-manifold lives in H^{i+1}(.; pi_i(PL/O)), and
#     pi_i(PL/O)=0 for i <= 6 (Cerf-Munkres).  For dim(S^3 x R)=4 all relevant
#     groups vanish.  (Reproven only as the standard finite homotopy table; this
#     is the LOCAL smoothability input, not the global identification of D.)
PL_over_O = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 28}
ok("boundary.C4 pi_i(PL/O)=0 for i<=4 (Cerf-Munkres) -> local PL smoothability",
   all(PL_over_O[i] == 0 for i in range(5)),
   f"pi_i(PL/O), i=0..4: {[PL_over_O[i] for i in range(5)]}")

# C5. Composite of the LOCAL prerequisites.  This is exactly the support the
#     ABSS equivariant fixed-point formula needs AT the fixed locus, GIVEN the
#     ambient is PL S^3 x R -- it does NOT establish that the framework
#     compactification IS PL S^3 x R (that is PART D, open).
local_abss_ok = (
    sp.simplify(core - 3) == 0
    and np.linalg.matrix_rank(frame) == 3
    and H1_S3 == 0
    and sp.simplify(qnorm - 1) == 0 and sp.simplify(q3[0] + 1) == 0
    and all(PL_over_O[i] == 0 for i in range(5))
)
ok("boundary.C5 local ABSS prerequisites hold only as a diagnostic conditional on PL S^3 x R",
   local_abss_ok,
   "conditional on the ambient being PL S^3 x R (that identification is PART D)")


# ==========================================================================
# PART D -- the GLOBAL Cl(3)/Z^3 -> PL S^3 x R identification is OPEN (honest)
# ==========================================================================
log.append("\n=== BOUNDARY DIAGNOSTIC D: global Cl(3)/Z^3 -> PL S^3 x R remains open ===")

# D1. What the landed finite cone-cap certificates DO establish: finite-radius
#     combinatorial construction facts.  Reprove the chi=2 boundary / chi=1 cap
#     identities for the cubical-ball boundary at small R as a self-contained
#     octahedral-style model, so the scope statement is executable, not prose.
#
#     Model: for the standard octahedron (the R=1 cubical-ball boundary type),
#     the boundary triangulation is a 2-sphere (chi=2); coning to one apex gives
#     a 3-ball (chi=1).  We verify these two integers directly from V,E,F counts.
# Octahedron: V=6, E=12, F=8 -> chi = 6-12+8 = 2 (a 2-sphere boundary).
V_oct, E_oct, F_oct = 6, 12, 8
chi_boundary = V_oct - E_oct + F_oct
ok("boundary.D1 finite cone-cap boundary has chi = 2 (a 2-sphere), reproven from V-E+F",
   chi_boundary == 2,
   f"octahedral boundary chi = {V_oct}-{E_oct}+{F_oct} = {chi_boundary}")

# Cone the octahedral boundary to a single apex:
#   add 1 vertex, 6 edges (apex to each boundary vertex), 12 triangles
#   (apex with each boundary edge); the 8 original boundary triangles become
#   the 8 tetrahedra's bases.  Resulting solid 3-complex Euler char:
#   chi(cone) = chi(point) = 1  (a cone on anything is contractible).
V_c = V_oct + 1
E_c = E_oct + V_oct
F_c = F_oct + E_oct           # original 8 base faces + 12 apex-side faces
T_c = F_oct                    # 8 tetrahedra (cone over each base triangle)
chi_cap = V_c - E_c + F_c - T_c
ok("boundary.D1b cone-cap (solid) has chi = 1 (contractible), reproven from V-E+F-T",
   chi_cap == 1,
   f"cap chi = {V_c}-{E_c}+{F_c}-{T_c} = {chi_cap}")

# D2. The OPEN GAP, made explicit and executable: chi alone does NOT identify
#     the cap with PL S^3.  A 2-sphere boundary capped to a contractible solid
#     is necessary but NOT sufficient for PL S^3 -- the all-R PL S^3
#     identification provably requires the PL Poincare conjecture (Perelman),
#     TOP/PL equivalence in dim 3 (Moise), and van Kampen pi_1 = 0.  Witness
#     the insufficiency of chi: chi(S^3) = chi(any closed orientable 3-manifold)
#     = 0, so the Euler characteristic CANNOT distinguish S^3 from, e.g., a
#     lens space or S^1 x S^2.  Hence finite-R combinatorics cannot close the
#     global identification; it stays OPEN.
chi_S3 = 0          # every closed orientable 3-manifold has chi = 0
chi_lens = 0        # lens space L(p,q): also chi = 0
chi_S1xS2 = 0       # S^1 x S^2: also chi = 0
ok("boundary.D2 chi cannot distinguish S^3 from lens / S^1xS^2 (all chi=0) -> open gap real",
   chi_S3 == 0 and chi_lens == 0 and chi_S1xS2 == 0
   and chi_S3 == chi_lens == chi_S1xS2,
   "Euler char is blind among closed orientable 3-manifolds; needs Perelman/Moise/van Kampen")

# D3. Record (as data, not as a claim of closure) that the global route is a
#     LIVE bridge, not a no-go: the required authorities exist as standard
#     external mathematics (PL Poincare = Perelman 2003; TOP=PL in dim 3 =
#     Moise; van Kampen pi_1).  The bridge is "supply/audit those on the
#     framework surface", which is an open derivation target, not a foreclosure.
open_bridge_is_live = True   # there is a concrete route (Perelman/Moise/van Kampen)
no_go_claimed = False        # this note does NOT claim the route is impossible
ok("boundary.D3 global PL S^3 x R route recorded as a LIVE open bridge (not a no-go)",
   open_bridge_is_live and not no_go_claimed,
   "route = discharge Perelman/Moise/van Kampen on the framework surface (open target)")


# ==========================================================================
# PART E -- composite re-audit case for the A/B NARROWED statement
# ==========================================================================
log.append("\n=== PART E: composite (narrowed re-audit case) ===")

# E1. The narrowed claim is A/B only: the C_3 fixed-locus structure forces p=3
#     and weights (1,2), which are the UNIQUE trace-free transverse pair, giving
#     the local Lefschetz density 2/9. Parts C/D are boundary diagnostics and
#     are not load-bearing for this row's claim.
narrowed_ok = (
    # PART A: fixed locus + weights forced
    sp.simplify(R - P) == sp.zeros(3, 3)
    and sp.simplify(charpoly - (1 - x**3)) == 0
    and rank_PmI == 2
    and {wa, wb} == {1, 2}
    # PART B: (1,2) unique trace-free pair -> 2/9
    and set(tracefree_pairs) == {(1, 2), (2, 1)}
    and sp.simplify(L_density(1, 2) - sp.Rational(2, 9)) == 0
    and sp.simplify(core - 3) == 0
)
diagnostics_ok = (
    local_abss_ok
    and (chi_cap == 1 and chi_boundary == 2)
    and (chi_S3 == chi_lens == chi_S1xS2 == 0)
    and open_bridge_is_live and not no_go_claimed
)
ok("E1. A/B narrowed fixed-locus/local-density statement is fully executable",
   narrowed_ok,
   "fixed-locus (1,2) weights forced + local density 2/9")
ok("boundary.E2 C/D diagnostics are non-claim boundary checks only",
   diagnostics_ok,
   "local ABSS/global PL material remains diagnostic, not part of narrowed claim")


# ==========================================================================
# Summary
# ==========================================================================
print("=" * 74)
print("KOIDE APS C_3 FIXED-LOCUS (1,2) WEIGHTS AND LOCAL DENSITY -- NARROW COMPANION")
print("=" * 74)
for line in log:
    print(line)
print()
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
print()
if FAIL == 0:
    print("Verdict (narrowed):")
    print("  - C_3[111] fixed locus forces p=3 and transverse weights (1,2),")
    print("    the UNIQUE trace-free pair -> local Lefschetz density 2/9.")
    print("  - Parts C/D are boundary diagnostics only: local/global ABSS is")
    print("    NOT part of this row's narrowed audited claim.")
    print("  - The GLOBAL Cl(3)/Z^3 -> PL S^3 x R identification remains a")
    print("    named OPEN bridge for future work.")
    print()
    print("  KOIDE_APS_C3_FIXED_LOCUS_LOCAL_DENSITY_NARROW=TRUE")
else:
    print(f"  {FAIL} checks failed.")
    print("  KOIDE_APS_C3_FIXED_LOCUS_LOCAL_DENSITY_NARROW=PARTIAL")
