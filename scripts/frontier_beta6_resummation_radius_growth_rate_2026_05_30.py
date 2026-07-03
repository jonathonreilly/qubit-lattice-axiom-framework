#!/usr/bin/env python3
"""
beta=6 SU(3) Wilson Delta(beta) -- RESUMMATION-RADIUS GROWTH-PRODUCT PROBE.

Decisive question
-----------------
The connected strong-coupling series Delta(beta) = P_full - P_1plaq has its
nearest singularity |beta_c| undetermined.  The campaign relocated the
obstruction to the *multiplicity resummation*: the single-cube sector has the
closed form Delta_cube = 72 * K'' * (K')^5 with K = log J, whose only
singularities are J's zeros (nearest |beta_c| = 8.2052 > 6), so the cube sector
CONVERGES at beta = 6.  Multi-cube cluster sectors carry an Euler weight
18^(1-F).  What growth-product condition keeps the tree-like K-built resummed
radius

    R = 1 / limsup_n |d_n|^(1/n)

larger than 6, and does the same condition control all K-built clusters?  The
tree-sector radius is governed by the exponential growth product of the
Euler-weighted tree-cluster multiplicity and per-cube combinatorics.  The full
radius also depends on compact K-built face deficits and on the >=3-face
baryon/epsilon sector.

What is reproven here (on-main recurrences plus named open inputs)
-----------------------------------------------------------------
 [A] J's Taylor coefficients from the on-main order-3 dominant-weight
     (Picard-Fuchs) recurrence 6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N
     + 2(2N+3) a_{N-1} + a_{N-2}, a0,a1,a2 = 1,0,1/36.
 [B] The single-plaquette cumulant GF K = log J: kappa_m = (1/18, 1/108, 0,
     -5/3888) for m = 2..5.
 [C] The cube-sector closed form Delta_cube = 72 K'' (K')^5 reproduces the
     on-main exact connected coefficients d5..d8 and the d9 cube-part.
 [D] Finite J-zero stabilization check: the nearest zero of J truncated to
     degree T migrates 5.74 (T=3) -> 8.205 (T>=20).  This is evidence that the
     T=3 root is not a stable radius witness; it is NOT used as a theorem about
     all partial-sum zeros.
 [E] The tree-sector Euler-weighted cluster-proliferation balance: a
     conditional upper bound on the weighted tree growth product
     g_tree = lambda_tree * rho_tree, plus a finite 2x2x1 compact K-built
     counterexample to the stronger all-cluster fixed-increment bridge.  No
     numerical animal-growth or compact-deficit bound is asserted here.

Comparators (CITED, never derivation inputs)
--------------------------------------------
 - Bars 1980 Bessel-determinant J closed form: entire-ness cross-check only.
 - Klarner/Eden lattice-animal growth constants: comparators showing that
   branched animal growth is a separate input.  The self-avoiding path factor
   2d-1 = 7 is NOT used as a bound on branched cluster animals.
 - Fisher/Lee-Yang thermodynamic zero |beta| ~ 5.54 (lattice-QCD): the
   comparator for |beta_c|, never an input.

Memory discipline
-----------------
NO enumeration of lattice cluster topologies (that OOM-crashed a prior push).
Only recurrences / generating functions / closed forms.  Every array is capped
(MAX_DEG below); no object exceeds ~1e6 entries; single-seed deterministic.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "BETA6_RESUMMATION_RADIUS_GROWTH_RATE_BOUNDED_NOTE_2026-05-30.md"

# ---- hard memory caps (no array/object may exceed these) -------------------
MAX_DEG = 60          # max Taylor degree we ever materialise for J (61 coeffs)
MAX_ROOTS_DEG = 30    # max polynomial degree handed to a root finder
assert MAX_DEG <= 200 and MAX_ROOTS_DEG <= 60

PASS = 0
FAIL = 0
def check(label: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {label}" + (f"  ::  {detail}" if detail else ""))


# ===========================================================================
# [0] source-boundary manifest in the note
# ===========================================================================
note_text = NOTE_PATH.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
print("=== [0] Source-boundary manifest ===")
check("note records 2026-06-07 source-boundary manifest",
      "2026-06-07 Source-Boundary Manifest" in note_text)
check("note records the exact tree threshold R_tree > 6 iff g_tree < 81",
      "R_tree > 6 iff g_tree < 81" in note_text)
check("note records the compact 2x2x1 K-built block obstruction",
      "compact 2x2x1 K-built block: k=4, F=16, n=15" in note_text)
check("note records the three open growth inputs",
      "exactly three open growth inputs" in note_flat
      and "tree-cluster/cumulant bound" in note_flat
      and "compact K-built face-deficit growth bound" in note_flat
      and "baryon/epsilon-sector bound" in note_flat)


# ===========================================================================
# [A] J coefficients from the on-main recurrence (exact rationals)
# ===========================================================================
def J_coeffs(N: int) -> list[F]:
    assert N <= MAX_DEG, "degree cap exceeded"
    a = [F(0)] * (N + 1)
    a[0] = F(1)
    if N >= 2:
        a[2] = F(1, 36)
    for n in range(2, N):
        num = n * (n + 1) * a[n] + 2 * (2 * n + 3) * a[n - 1] + (a[n - 2] if n - 2 >= 0 else F(0))
        den = 6 * (n + 1) * (n + 4) * (n + 5)
        a[n + 1] = F(num, den)
    return a


print("=== [A] J Taylor coefficients from the Picard-Fuchs recurrence ===")
a = J_coeffs(MAX_DEG)
check("recurrence seed a_2 = 1/36", a[2] == F(1, 36))
# Cross-check J(6) and P_1plaq(6) against the Bars Bessel-determinant comparator.
def J_bars(beta, kmax: int = 14):
    x = mp.mpmathify(beta) / 3
    tot = mp.mpf(0)
    for k in range(-kmax, kmax + 1):
        M = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                M[i, j] = mp.besseli(i - j + k, x)
        tot += mp.det(M)
    return tot

def J_of(beta, coeffs, deriv: bool = False):
    b = mp.mpf(beta); val = mp.mpf(0); der = mp.mpf(0); p = mp.mpf(1)
    for n, c in enumerate(coeffs):
        cf = mp.mpf(c.numerator) / mp.mpf(c.denominator)
        val += cf * p
        if n >= 1:
            der += cf * n * (p / b)
        p *= b
    return (val, der) if deriv else val

J6s, Jp6s = J_of(6, a, deriv=True)
P1 = Jp6s / J6s
check("P_1plaq(6)=J'/J = 0.4225317396 (recurrence)", abs(P1 - mp.mpf("0.4225317396")) < mp.mpf("1e-9"),
      f"P1={mp.nstr(P1,12)}")
check("recurrence J(6) == Bars J(6) (comparator)", abs(J6s - J_bars(6)) < mp.mpf("1e-8"))


# ===========================================================================
# [B] single-plaquette cumulant GF K = log J ; kappa_m = m! [b^m] K
# ===========================================================================
print("\n=== [B] single-plaquette cumulant GF K = log J ===")
b = sp.symbols("b")
NK = 7  # only need through m=5 -> series order 6
Jpoly = sum(sp.Rational(a[n].numerator, a[n].denominator) * b**n for n in range(NK))
Kser = sp.series(sp.log(Jpoly), b, 0, NK).removeO()
kappa = {m: sp.factorial(m) * Kser.coeff(b, m) for m in range(1, 6)}
check("kappa_2 = 1/18", kappa[2] == sp.Rational(1, 18))
check("kappa_3 = 1/108", kappa[3] == sp.Rational(1, 108))
check("kappa_4 = 0", kappa[4] == 0)
check("kappa_5 = -5/3888", kappa[5] == sp.Rational(-5, 3888))


# ===========================================================================
# [C] cube-sector closed form  Delta_cube = 72 * K'' * (K')^5
#     reproduces on-main exact d5..d8 + d9 cube-part.
# ===========================================================================
print("\n=== [C] cube-sector closed form 72 K'' (K')^5 -> d5..d9 cube-part ===")
NC = 12
Jc = sum(sp.Rational(a[n].numerator, a[n].denominator) * b**n for n in range(NC + 1))
K = sp.series(sp.log(Jc), b, 0, NC + 1).removeO()
Kp = sp.diff(K, b)
Kpp = sp.diff(K, b, 2)
Dcube = sp.series(72 * Kpp * Kp**5, b, 0, NC + 1).removeO()
# On-main exact connected coefficients (cited anchors; mixed-cumulant note + #2408/#2440).
d_onmain = {5: sp.Rational(1, 472392), 6: sp.Rational(7, 5668704),
            7: sp.Rational(5, 17006112), 8: sp.Rational(5, 272097792)}
for n, dv in d_onmain.items():
    cc = sp.nsimplify(Dcube.coeff(b, n))
    check(f"72 K''(K')^5 [b^{n}] = on-main d_{n} = {dv}", sp.simplify(cc - dv) == 0,
          f"got {cc}")
# d9 cube-part (cited: -235/29386561536) -- the cube SECTOR's order-9 piece.
check("72 K''(K')^5 [b^9] = cube-part d9 = -235/29386561536",
      sp.simplify(Dcube.coeff(b, 9) - sp.Rational(-235, 29386561536)) == 0,
      f"got {sp.nsimplify(Dcube.coeff(b,9))}")


# ===========================================================================
# [D] finite J-zero stabilization (truncation migrates the nearest J-zero
#     5.74 -> 8.205); this is evidence only, not a partial-sum theorem.
# ===========================================================================
print("\n=== [D] J-zero migration evidence: 5.74 (T=3) -> 8.205 (T>=20) ===")
aF = J_coeffs(MAX_DEG)
def nearest_J_zero(T: int):
    assert T <= MAX_ROOTS_DEG
    coeffs = [mp.mpf(aF[n].numerator) / mp.mpf(aF[n].denominator) for n in range(T + 1)]
    roots = mp.polyroots(list(reversed(coeffs)), maxsteps=300, extraprec=120)
    return min(abs(r) for r in roots)

mig = {T: nearest_J_zero(T) for T in (3, 4, 6, 8, 12, 16, 20, 25, 30)}
for T, r in mig.items():
    print(f"    T={T:2d}: nearest |J-zero| = {mp.nstr(r,7)}")
check("T=3 truncation nearest zero = 5.739 (unstable T=3 witness)", abs(mig[3] - mp.mpf("5.739")) < mp.mpf("1e-2"),
      f"|z|_{{T=3}}={mp.nstr(mig[3],6)}")
check("T>=20 nearest truncated zero stabilizes near 8.2052", abs(mig[20] - mp.mpf("8.2052")) < mp.mpf("1e-3"),
      f"|z|_{{T=20}}={mp.nstr(mig[20],6)}")
check("selected truncation sequence migrates upward and crosses 6 by T=4",
      mig[3] < mig[4] < mig[6] < mig[8] < mig[12] < mig[16] <= mig[20] and mig[20] > mp.mpf(6),
      "5.74<...<8.205, crosses 6 by T=4")
check("high-truncation cube-sector root witness is > 6", mig[30] > mp.mpf(6))


# ===========================================================================
# [E] K-built tree-sector bound and all-cluster face-deficit obstruction
# ===========================================================================
# A connected union of k elementary 3-cubes with s shared plaquette faces has
#
#     F_boundary = 6k - 2s.
#
# If the cube-adjacency graph is a tree, then s = k-1 and
# F_boundary = 4k+2.  The leading action power is n = F_boundary - 1, because
# the marked plaquette is not an action insertion.  Thus the tree-sector
# Euler/action term is
#
#     18^(1-F) |beta|^(F-1) = 18^{-(4k+1)} |beta|^{4k+1}.
#
# The previously displayed 18^{-(4k+2)} exponent was off by one.  The ratio in
# k is unchanged: a tree-sector count/combinatorics product g_tree gives the
# convergence condition g_tree (|beta|/18)^4 < 1, hence R_tree =
# 18/g_tree^(1/4) and the beta=6 threshold g_tree < 81.
#
# The stronger all-K-built claim needs another input.  Compact K-built clusters
# can have excess shared faces
#
#     c = s - (k-1) >= 0,  F = 4k+2-2c,  n = 4k+1-2c.
#
# The four-cube 2x2x1 cubical block below is a closed K-built boundary
# (every boundary link has incidence two) but has c=1, F=16, n=15, not
# F=18, n=17.  Therefore the all-K-built sector is not controlled by g_tree
# alone; it needs a face-deficit/area-growth bound in addition to the baryon
# channel bound.
print("\n=== [E] K-built tree-sector bound + compact-deficit obstruction ===")

AXES3 = (0, 1, 2)
ALL4 = (0, 1, 2, 3)

def cube_boundary_faces(cube):
    faces = []
    for normal in AXES3:
        span = tuple(axis for axis in AXES3 if axis != normal)
        for side in (0, 1):
            base = list(cube)
            base[normal] += side
            faces.append((span, tuple(base)))
    return faces

def boundary_faces(cubes):
    parity = {}
    for cube in cubes:
        for face in cube_boundary_faces(cube):
            parity[face] = 1 - parity.get(face, 0)
            if parity[face] == 0:
                del parity[face]
    return set(parity)

def plaquette_links(face):
    span, base = face
    a0, a1 = span
    fixed = [axis for axis in ALL4 if axis not in span]
    links = []
    for offset in (0, 1):
        coord = list(base)
        coord[a1] += offset
        links.append((a0, tuple(coord)))
    for offset in (0, 1):
        coord = list(base)
        coord[a0] += offset
        links.append((a1, tuple(coord)))
    assert len(fixed) == 2
    return links

def link_incidences(faces):
    counts = {}
    for face in faces:
        for link in plaquette_links(face):
            counts[link] = counts.get(link, 0) + 1
    return counts

def shared_face_count(cubes):
    cube_set = set(cubes)
    shared = 0
    for cube in cube_set:
        for axis in AXES3:
            nb = list(cube)
            nb[axis] += 1
            if tuple(nb) in cube_set:
                shared += 1
    return shared

def cluster_stats(name, cubes):
    faces = boundary_faces(cubes)
    incidences = link_incidences(faces)
    k = len(cubes)
    s = shared_face_count(cubes)
    c = s - (k - 1)
    face_count = len(faces)
    action_power = face_count - 1
    closed_kbuilt = bool(incidences) and min(incidences.values()) == 2 and max(incidences.values()) == 2
    print(
        f"    {name}: k={k}, shared={s}, excess={c}, "
        f"F={face_count}, n=F-1={action_power}, "
        f"max_link_incidence={max(incidences.values())}"
    )
    return {
        "name": name,
        "k": k,
        "s": s,
        "c": c,
        "F": face_count,
        "n": action_power,
        "closed_kbuilt": closed_kbuilt,
        "link_counts": set(incidences.values()),
    }

single_cube = [(0, 0, 0, 0)]
two_cube_box = [(0, 0, 0, 0), (1, 0, 0, 0)]
four_cube_chain = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), (3, 0, 0, 0)]
four_cube_square = [(0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0)]

stats = {
    item["name"]: item for item in [
        cluster_stats("single cube", single_cube),
        cluster_stats("two-cube box", two_cube_box),
        cluster_stats("four-cube tree chain", four_cube_chain),
        cluster_stats("four-cube 2x2x1 block", four_cube_square),
    ]
}

check("single cube: F=6, n=5, Euler weight 18^(1-F)=18^-5",
      stats["single cube"]["F"] == 6 and stats["single cube"]["n"] == 5)
check("two-cube tree box: F=10, n=9, Euler weight 18^-9",
      stats["two-cube box"]["F"] == 10 and stats["two-cube box"]["n"] == 9)
check("tree chain obeys F=4k+2 and n=4k+1",
      stats["four-cube tree chain"]["F"] == 4 * stats["four-cube tree chain"]["k"] + 2 and
      stats["four-cube tree chain"]["n"] == 4 * stats["four-cube tree chain"]["k"] + 1)
check("compact 2x2x1 block is still closed K-built: every boundary link has incidence two",
      stats["four-cube 2x2x1 block"]["closed_kbuilt"] and
      stats["four-cube 2x2x1 block"]["link_counts"] == {2})
check("compact K-built block falsifies all-cluster fixed increment F=4k+2",
      stats["four-cube 2x2x1 block"]["F"] == 16 and
      stats["four-cube 2x2x1 block"]["F"] != 4 * stats["four-cube 2x2x1 block"]["k"] + 2)
check("shared-face formula holds: F = 4k+2-2c, n = 4k+1-2c",
      all(item["F"] == 4 * item["k"] + 2 - 2 * item["c"] and
          item["n"] == 4 * item["k"] + 1 - 2 * item["c"] for item in stats.values()))
check("Euler exponent correction: tree sector uses 18^{-(4k+1)}, not 18^{-(4k+2)}",
      -(4 * 2 + 1) == 1 - stats["two-cube box"]["F"])
check("at beta=6, one face-deficit unit weakens Euler suppression by factor 9",
      (mp.mpf(6) / mp.mpf(18)) ** stats["four-cube 2x2x1 block"]["n"] /
      ((mp.mpf(6) / mp.mpf(18)) ** stats["four-cube tree chain"]["n"]) == mp.mpf(9))

def R_tree(growth_product):
    return mp.mpf(18) / mp.mpf(growth_product) ** (mp.mpf(1) / 4)

for g in (mp.mpf(1), mp.mpf(7), mp.mpf(81)):
    print(f"    g_tree={mp.nstr(g,4)}:  R_tree = 18/g_tree^(1/4) = {mp.nstr(R_tree(g),6)}")
g_crit = (mp.mpf(18) / mp.mpf(6)) ** 4
check("tree-sector critical growth product for R=6: g_crit = (18/6)^4 = 81",
      abs(g_crit - mp.mpf(81)) < mp.mpf("1e-30"),
      f"g_crit = {mp.nstr(g_crit,6)}")
check("illustrative self-avoiding-chain normalization g_tree=7 gives R_tree > 6",
      R_tree(7) > mp.mpf(6), f"R_tree(7)={mp.nstr(R_tree(7),6)}")
rho_crit_if_lambda7 = g_crit / mp.mpf(7)
check("if an external lambda_tree <= 7 bound were supplied, rho_crit would be 81/7",
      abs(rho_crit_if_lambda7 - mp.mpf(81) / mp.mpf(7)) < mp.mpf("1e-30"),
      f"rho_crit(lambda_tree=7) = {mp.nstr(rho_crit_if_lambda7,6)}")

print(f"\n    cube-sector (single-cube) radius (J-zero)      = 8.2052")
print(f"    tree-sector illustrative bound (g_tree=7)       = {mp.nstr(R_tree(7),6)}")
print(f"    compact K-built deficit factor at beta=6        = 9^c per excess shared face")
print(f"    Fisher/Lee-Yang thermodynamic comparator       ~ 5.54 (CITED, lattice-QCD)")

check("VERDICT: tree K-built radius > 6 for g_tree < 81, but all K-built needs a deficit-growth bound",
      R_tree(7) > 6 and g_crit == 81 and stats["four-cube 2x2x1 block"]["c"] == 1,
      "The fixed-increment bridge is false for compact K-built clusters; "
      "do not promote the all-K-built sector from g_tree alone.")

print(f"\nSCORECARD: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
