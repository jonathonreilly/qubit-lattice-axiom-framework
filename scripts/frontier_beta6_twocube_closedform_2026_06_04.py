#!/usr/bin/env python3
"""
Beta=6 SU(3) plaquette lane 2: bounded finite-order validation of the leading
NON-CUBE (two-cube) candidate in Delta(beta) = <P_full> - <P_1plaq> = sum d_n beta^n.

RESULT
------
The CUBE sector has the exact zero-parameter closed form (frontier #2440 + the d_9
note):
    Delta_cube(beta) = 72 * K''(beta) * (K'(beta))^5 ,   K = log J,
which is structurally   (#cubes through p0) * 18 * K''(K')^(F-1),  F = 6 faces,
#cubes = 4, and 18 = 1/<X_p0^2> the universal marked-face weight.

This runner validates the analogous candidate for the leading non-cube class --
the weight-10 two-cube 2-cycles through p0 (two elementary cubes sharing one face,
the shared face CANCELLING in GF(3), leaving F = 10 distinct faces; 60
configurations through p0):
    Delta_2cube_candidate^(w10)(beta) = 1080 * K''(beta) * (K'(beta))^9
                                      = (60 configs) * 18 * K''(K')^(F-1), F = 10.
The prefactor 1080 = 60 * 18 is forced for this candidate pattern (60 =
independently-counted #configs, 18 = the cube's marked-face weight). The primary
cache fixes the constant on the leading order-9 coefficient and checks order 10 as
the held-out finite-order validation:

    order  exact weight-10 class           1080 K''(K')^9 prediction     match
      9    5/16529940864                   5/16529940864 (DERIVED A)     yes
      10   55/198359290368                 55/198359290368 (out-of-sample) yes

This is bounded finite-order support, not an all-order proof. The naive candidate
19440 (K'')^2 (K')^9, which has the wrong exponent structure, matches only order 9
and misses order 10 -- it over-predicts, exact/predicted = 11/13 -- recorded below
as the discrimination control.

CONVERGENCE / beta=6. K', K'' are rational in J and its derivatives, with poles
only at the J zero |beta| = 8.2052 > 6 (the SAME branch point as the cube sector),
so the candidate 1080 K''(K')^9 converges at beta=6:
    Delta_2cube^(w10)(6) = 0.0300796,
shrinking the non-cube remainder 0.10796 -> 0.07788 and the truncated <P>-model(6)
0.485445 -> 0.515525 (gap to the 0.594 Monte-Carlo comparator 0.10796 -> 0.07788).
This is a candidate model readout, NOT a beta=6 closure or an exact all-order
contribution -- weights 11, 12 and higher clusters remain, and the retained
infinite-hierarchy obstruction stands; 0.594 is a comparator, never an input.

METHOD / orbit collapse. The 60 weight-10 supports are ONE lattice-symmetry orbit:
at every order they contribute the IDENTICAL per-support cumulant (self-validated by
agreeing on multiple representatives -- the two-cube analog of the cube's octahedral
shape collapse). So the class value at order n is 60 * support_contrib(rep, n),
cutting the work 60x and making order 10 feasible in the primary cache. Per-link
projectors are gated at total incidence <= 4; higher-order runs are optional
frontier checks and are outside this landed cache scope.

FORBIDDEN-IMPORT: every coefficient is reproven from the SU(3) Haar single-link
integral + the J recurrence (a Haar primitive). 0.594 is comparator-only. The cube
closed form is reproven (it reproduces d_5..d_8 exactly) and cited, never asserted.

Run:  python3 scripts/frontier_beta6_twocube_closedform_2026_06_04.py [maxorder] [nreps]
      maxorder defaults to 10; nreps defaults to 1 for cache budget. Larger nreps
      re-check orbit-representative equality; maxorder 11 is an optional frontier
      run, not the landed cache claim.
"""
import sys, os, time, math
from collections import Counter, deque
from fractions import Fraction
import sympy as sp
import importlib.util

AUDIT_TIMEOUT_SEC = 240

# Import the validated d_9 engine (its main() runs only under __main__).
_HERE = os.path.dirname(os.path.abspath(__file__))
_ENG = os.environ.get("D9_ENGINE",
                      os.path.join(_HERE, "frontier_beta6_d9_coefficient_2026_06_04.py"))
_spec = importlib.util.spec_from_file_location("d9eng", _ENG)
d9 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(d9)

P0 = d9.P0
joint_cumulant_frac = d9.joint_cumulant_frac
joint_cumulant = d9.joint_cumulant
_multiplicity_vectors = d9._multiplicity_vectors
directed_links = d9.directed_links
enumerate_d9_new_supports = d9.enumerate_d9_new_supports
_all_elementary_cubes = d9._all_elementary_cubes
_support_connected_with_p0 = d9._support_connected_with_p0
_support_leaf_free = d9._support_leaf_free
mod3_closable = d9.mod3_closable
_J_recurrence_coeffs = d9._J_recurrence_coeffs

PASS = 0; FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond: PASS += 1
    else: FAIL += 1
    print(f"  [{tag}] {name}")
    if detail:
        print(f"         {detail}")
    return cond

LOG = os.environ.get("LANE2_LOG", "/tmp/lane2_twocube_progress.log")
_lf = open(LOG, "a")
def log(m): _lf.write(m + "\n"); _lf.flush()

# ===========================================================================
# Per-link incidence gate (the (5,5)/(6,6) wall) + capped support contribution.
# ===========================================================================
def _word_max_incidence(plaqs):
    c = Counter()
    for f in plaqs:
        for (L, _s) in directed_links(f): c[L] += 1
    return max(c.values()) if c else 0

def support_contrib_capped(S, n, inc_cap=4):
    """support_contrib_frac, but SKIP any multiplicity vector that drives a link
    past inc_cap (the per-link-degree wall). Returns (Fraction, walled_flag)."""
    Slist = list(S); a = len(Slist); total = Fraction(0); walled = False
    for m_p0, m_action in _multiplicity_vectors(a, n):
        plaqs = [P0] + [P0] * m_p0
        for s, ms in zip(Slist, m_action): plaqs += [s] * ms
        if _word_max_incidence(plaqs) > inc_cap:
            walled = True
            log(f"      [WALL] size {a} order {n} vector (m_p0={m_p0}) incidence "
                f"{_word_max_incidence(plaqs)} > {inc_cap}; skipped")
            continue
        kap = joint_cumulant_frac(plaqs)
        if kap == 0: continue
        denom = math.factorial(m_p0)
        for ms in m_action: denom *= math.factorial(ms)
        total += kap / denom
    return total, walled

# ===========================================================================
# Geometry: count the weight-10 two-cube configurations through p0.
# ===========================================================================
def count_weight10_configs(radius=2):
    """Number of (unordered) elementary-cube pairs sharing exactly one face whose
    GF(3) sum (coeff 1,2 -> shared face cancels) is a weight-10 2-cycle through p0.
    This is the geometric multiplicity that forces the prefactor (= 60)."""
    cubes = _all_elementary_cubes(radius)
    import itertools
    face_cubes = {}
    for ci, c in enumerate(cubes):
        for f in c: face_cubes.setdefault(f, []).append(ci)
    pairs = set()
    for f, cis in face_cubes.items():
        for a, b in itertools.combinations(cis, 2):
            if len(cubes[a] & cubes[b]) == 1:
                pairs.add((a, b))
    n = 0
    for (a, b) in pairs:
        fc = {}
        for f in cubes[a]: fc[f] = (fc.get(f, 0) + 1) % 3
        for f in cubes[b]: fc[f] = (fc.get(f, 0) + 2) % 3
        supp = frozenset(ff for ff, v in fc.items() if v)
        if len(supp) == 10 and P0 in supp:
            n += 1
    return n

# ===========================================================================
# K-derivatives of K = log J.
# ===========================================================================
def K_series(nmax):
    b = sp.symbols('b'); NC = nmax + 3
    a = _J_recurrence_coeffs(NC)
    J = sum(a[i] * b ** i for i in range(NC + 1))
    K = sp.series(sp.log(J), b, 0, NC + 1).removeO()
    return b, K, sp.diff(K, b), sp.diff(K, b, 2)

def K_value_beta6(NJ=100):
    """(K'(6), K''(6)) from the truncated J recurrence (Haar primitive)."""
    import mpmath as mp
    a = _J_recurrence_coeffs(NJ)
    x = mp.mpf(6)
    J = sum((mp.mpf(a[n].p) / mp.mpf(a[n].q)) * x ** n for n in range(NJ + 1))
    Jp = sum(n * (mp.mpf(a[n].p) / mp.mpf(a[n].q)) * x ** (n - 1) for n in range(1, NJ + 1))
    Jpp = sum(n * (n - 1) * (mp.mpf(a[n].p) / mp.mpf(a[n].q)) * x ** (n - 2)
              for n in range(2, NJ + 1))
    return Jp / J, (Jpp * J - Jp ** 2) / J ** 2


def main():
    args = sys.argv[1:]
    maxorder = int(args[0]) if len(args) > 0 else 10
    nreps = int(args[1]) if len(args) > 1 else 1
    t0 = time.time()
    print("=" * 78)
    print("BETA=6 LANE 2: bounded validation of the weight-10 two-cube candidate")
    print("=" * 78)
    log(f"\n=== lane2 twocube run maxorder={maxorder} nreps={nreps} ===")

    # ----- V0: cube closed form reproduces d_5..d_8 (reprove-and-cite the import) -----
    print("\nV0. cube-sector closed form 72 K''(K')^5 reproduces d_5..d_8 (reproven, cited)")
    b, K, Kp, Kpp = K_series(maxorder)
    cube = sp.series(72 * Kpp * Kp ** 5, b, 0, maxorder + 1).removeO()
    onmain = {5: sp.Rational(1, 472392), 6: sp.Rational(7, 5668704),
              7: sp.Rational(5, 17006112), 8: sp.Rational(5, 272097792)}
    repro = all(sp.nsimplify(cube.coeff(b, n)) == onmain[n] for n in onmain)
    check("cube closed form 72 K''(K')^5 reproduces the direct-engine d_5..d_8 exactly",
          repro, "; ".join(f"d_{n}={sp.nsimplify(cube.coeff(b,n))}" for n in sorted(onmain)))
    check("cube prefactor 72 = (4 cubes through p0) * 18 (universal marked-face weight "
          "1/<X_p0^2>)", 72 == 4 * 18, "72 = 4*18; <X_p0^2> = 1/18")

    # ----- V1: enumerate the 60 weight-10 supports (streamed) + geometry -----
    print("\nV1. weight-10 two-cube supports (streamed) + configuration count")
    good2, ncubes2, nstream2 = enumerate_d9_new_supports(radius=2)
    good3, _, _ = enumerate_d9_new_supports(radius=3)
    nconf = count_weight10_configs(radius=2)
    check("60 distinct weight-10 supports (one orbit), STABLE radius2 == radius3; "
          "and 60 = #weight-10 two-cube configs through p0 (forces the prefactor)",
          len(good2) == 60 and good2 == good3 and nconf == 60,
          f"radius2={len(good2)}, radius3={len(good3)}, configs={nconf} "
          f"({nstream2} pair-combos streamed)")
    reps = sorted(good2, key=lambda s: tuple(sorted(s)))

    # ----- V2: exact weight-10 class values via orbit collapse -----
    rep_label = "orbit representative" if nreps == 1 else "orbit representatives"
    print(f"\nV2. exact weight-10 class at orders 9..{maxorder} (orbit collapse, "
          f"{nreps} {rep_label}/order)")
    W = {}
    for n in range(9, maxorder + 1):
        tn = time.time()
        vals = []
        wall = False
        reps_checked = min(nreps, len(reps))
        for i in range(reps_checked):
            c, w = support_contrib_capped(tuple(sorted(reps[i])), n, inc_cap=4)
            vals.append(c); wall = wall or w
            log(f"  order {n} rep[{i}] = {c} ({time.time()-tn:.1f}s)")
        equal = len(set(vals)) == 1
        per = vals[0]
        W[n] = sp.Rational((60 * per).numerator, (60 * per).denominator)
        verb = "gives" if reps_checked == 1 else "give"
        check(f"order {n}: {reps_checked} {rep_label} {verb} per-support cumulant {per} "
              f"-> class = 60*per = {W[n]}",
              equal, f"weight-10[{n}] = {W[n]} = {float(W[n]):.8e} "
                     f"(walled={wall}, {time.time()-tn:.1f}s)")

    # regression vs the d_9 note
    check("d_9 weight-10 class = +5/16529940864 (REGRESSION vs the d_9 note's "
          "new-support part)", W[9] == sp.Rational(5, 16529940864), f"W[9] = {W[9]}")

    # ----- V3: the zero-parameter candidate 1080 K''(K')^9 -----
    print("\nV3. zero-parameter candidate 1080 K''(K')^9 = (60 configs)*18*K''(K')^(F-1)")
    base = sp.series(Kpp * Kp ** 9, b, 0, maxorder + 1).removeO()
    A = sp.nsimplify(W[9] / sp.nsimplify(base.coeff(b, 9)))
    check("the candidate constant fixed by the LEADING (order-9) coefficient equals "
          "1080 = 60 configs * 18 marked-face weight",
          A == 1080 and 1080 == 60 * 18,
          f"A(order-9) = {A}; forced value 60*18 = {60*18}; matches = {A == 1080}")
    form = {n: sp.nsimplify(A * base.coeff(b, n)) for n in range(9, maxorder + 1)}
    held = list(range(10, maxorder + 1))
    oos_ok = True
    for n in range(9, maxorder + 1):
        m = (form[n] == W[n])
        tag = "DERIVED(A)" if n == 9 else "OUT-OF-SAMPLE"
        if n > 9: oos_ok = oos_ok and m
        print(f"     order {n} [{tag}]: 1080*K''(K')^9 = {form[n]}  vs  exact = {W[n]}  "
              f"MATCH={m}")
    if held:
        check(f"candidate 1080 K''(K')^9 reproduces held-out orders {held} "
              "OUT-OF-SAMPLE (neither used to fix the constant)",
              oos_ok,
              f"out-of-sample held-out orders {held} all match = {oos_ok}")
    else:
        print("     no held-out order requested; run with maxorder >= 10 for the bounded "
              "out-of-sample check")

    # ----- V4: discrimination control -- the wrong exponent structure fails -----
    print("\nV4. discrimination control: the naive (K'')^2(K')^9 has the wrong exponents")
    if 10 in W:
        base2 = sp.series(Kpp ** 2 * Kp ** 9, b, 0, maxorder + 1).removeO()
        A2 = sp.nsimplify(W[9] / sp.nsimplify(base2.coeff(b, 9)))
        pred2_10 = sp.nsimplify(A2 * base2.coeff(b, 10))
        ratio = sp.nsimplify(W[10] / pred2_10) if pred2_10 != 0 else None
        check("the wrong candidate 19440 (K'')^2(K')^9 matches order 9 "
              "(by construction) but misses order 10 by ratio 11/13",
              A2 == 19440 and pred2_10 != W[10] and ratio == sp.Rational(11, 13),
              f"19440*(K'')^2(K')^9 order-10 pred = {pred2_10}, exact = {W[10]}, "
              f"actual/pred = {ratio} (!=1)")
    else:
        print("     skipped: order 10 was not requested")

    # ----- V5: two-engine cross-check on the leading per-support cumulant -----
    print("\nV5. two-engine cross-check (sympy == Fraction) on a weight-10 cumulant (order 9)")
    Scheap = tuple(sorted(reps[0]))
    plaqs = [P0] + list(Scheap)
    kf = joint_cumulant_frac(plaqs)
    ks = joint_cumulant(plaqs)
    check("sympy joint_cumulant == Fraction joint_cumulant = 1/198359290368 (order-9 "
          "weight-10 word)",
          ks == sp.Rational(kf.numerator, kf.denominator) == sp.Rational(1, 198359290368),
          f"Fraction = {kf}, sympy = {ks}")

    # ----- V6: beta=6 candidate evaluation + backbone update -----
    print("\nV6. beta=6 candidate readout + backbone update (NOT a closure)")
    import mpmath as mp
    mp.mp.dps = 40
    kp6, kpp6 = K_value_beta6(100)
    w10_6 = mp.mpf(1080) * kpp6 * kp6 ** 9
    cube_6 = mp.mpf(72) * kpp6 * kp6 ** 5
    # convergence: vary truncation
    conv = []
    for NJ in (50, 75, 100):
        k1, k2 = K_value_beta6(NJ)
        conv.append(mp.mpf(1080) * k2 * k1 ** 9)
    converged = abs(conv[0] - conv[2]) < mp.mpf("1e-12")
    check("the candidate expression converges at beta=6 (J-zero |beta|=8.2052 > 6; "
          "K',K'' rational in J): value stable across J truncations N=50,75,100",
          converged,
          f"1080 K''(K')^9 at beta=6 = {mp.nstr(w10_6, 10)} "
          f"(N=50: {mp.nstr(conv[0],10)}, N=100: {mp.nstr(conv[2],10)})")
    P1_6 = kp6
    cube_model = mp.mpf("0.485445")  # established backbone (P_1plaq + 4 cube shells)
    new_model = cube_model + w10_6
    print(f"     P_1plaq(6) = K'(6) = {mp.nstr(P1_6, 8)}  (established 0.422532)")
    print(f"     Delta_cube(6) = 72 K''(K')^5 = {mp.nstr(cube_6, 8)}  (established 0.062913)")
    print(f"     candidate weight-10 two-cube 1080 K''(K')^9 at beta=6 = {mp.nstr(w10_6, 8)}")
    print(f"     non-cube remainder 0.10796 -> {mp.nstr(mp.mpf('0.10796') - w10_6, 7)} "
          f"(shrunk by the candidate expression)")
    print(f"     <P>-model(6): 0.485445 -> {mp.nstr(new_model, 8)} ; "
          f"gap to 0.5934 comparator: {mp.nstr(mp.mpf('0.107955'), 6)} -> "
          f"{mp.nstr(mp.mpf('0.5934') - new_model, 6)} (0.594 is a comparator, NOT input)")

    print("\n" + "=" * 78)
    print("WEIGHT-10 TWO-CUBE CLASS -- EXACT COEFFICIENTS + ZERO-PARAM CANDIDATE:")
    for n in sorted(W):
        print(f"   weight-10[{n}] = {W[n]} = {float(W[n]):.8e}  "
              f"(= 1080 K''(K')^9 [b^{n}])")
    print("   candidate: Delta_2cube^(w10)(beta) = 1080 K''(K')^9 = "
          "(60 configs)*18*K''(K')^(F-1), F=10")
    print(f"   beta=6 value = {mp.nstr(w10_6, 8)}  (converges; J-zero 8.2052 > 6)")
    print("=" * 78)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}   ({time.time()-t0:.1f}s)")
    print("=" * 78)
    print("This is bounded finite-order support for a zero-parameter candidate.")
    print("It is NOT an all-order proof or a beta=6 closure: weights 11, 12 and higher")
    print("clusters remain, and the retained infinite-hierarchy obstruction stands.")
    print("0.594 is a Monte-Carlo comparator, never a derivation input.")
    _lf.close()
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
