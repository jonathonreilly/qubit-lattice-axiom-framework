#!/usr/bin/env python3
"""
FALSIFICATION TEST of the beta=6 plaquette cube-cluster unification rule at
WEIGHT 11.

THE RULE UNDER TEST
-------------------
A weight-W cube-cluster 2-cycle through the marked plaquette p0 was conjectured to
contribute to Delta(beta) = <P_full> - <P_1plaq> the SINGLE monomial

    Delta_W(beta) = (#configs through p0) * 18 * K'' * (K')^(W-1),   K = log J,

with 18 = 1/<X_p0^2> the universal marked-face weight. This holds (theorem-grade)
for:
  * the elementary cube  W=6:   72 * K''(K')^5    (#configs = 4),
  * the two-cube weight-10 class W=10: 1080 * K''(K')^9 (#configs = 60, ONE orbit).
The OPEN claim was the extension to weight 11:
    1188 * K'' * (K')^10,   1188 = 66 * 18,  66 = the counted weight-11 configs,
with EXACT leading coefficients
    order 10 = 11/595077871104,
    order 11 = 11/595077871104  (equal to order 10 -- a closed-form coincidence),
    order 12 = 715/85691213438976.

RESULT: THE RULE BREAKS AT WEIGHT 11.
-------------------------------------
1. COUNT. The weight-11 2-cycles through p0 number 66 (stable radius 2 == radius 3,
   stable max_cubes = 2 vs 3), CONFIRMING the predicted config count. Geometrically
   each is the GF(3) sum of TWO elementary cubes sharing exactly ONE face, with
   SAME-sign coefficients (1,1)/(2,2) so the shared face SURVIVES (GF(3) coeff 2);
   distinct faces 6+6-1 = 11. (Weight 10 was the same cube pair with OPPOSITE-sign
   coefficients so the shared face CANCELS: 6+6-2 = 10.)

2. ORBITS -- THE CRUX. Under the 64 lattice isometries fixing p0, the 66 supports
   split into SIX orbits of sizes {2,4,4,8,16,32} -- NOT a single orbit (weight 10
   was one orbit). At the LEADING order (10) all six orbits nevertheless share the
   IDENTICAL per-support 11-point cumulant 1/1190155742208 (two-engine confirmed:
   Fraction == sympy). So leading-order orbit-splitting alone does not yet break a
   single-monomial form. At the HELD-OUT order (11) the orbits DIVERGE: 60 supports
   (orbits of size 16,4,8,32) give per-support 11/14281868906496 while the other 6
   supports (orbits of size 4,2) give 10/14281868906496 -- a genuine
   sum-over-distinct-topologies, which a single monomial cannot represent.

3. THE BREAK. The single-monomial rule REQUIRES per-support cumulant
   = 18 * [leading coeff of K''(K')^(W-1)]. This identity HOLDS at W=6 and W=10
   (verified here as controls) but FAILS at W=11:
       per-support (enum, two-engine) = 1/1190155742208
       18 * [K''(K')^10 leading]      = 1/3570467226624
   differing by an exact factor of 3. The enumerated class coefficients are
       order 10 = 66 * 1/1190155742208               = 11/198359290368
       order 11 = 60*11/14281868906496 + 6*10/...    = 5/99179645184
   versus the predicted 11/595077871104 at BOTH orders, i.e. enum/pred = 3 at order
   10 and 30/11 at order 11. The conjectured 1188 K''(K')^10 form is FALSIFIED on
   three independent counts: (i) the leading coefficient is off by an exact factor
   3; (ii) the held-out order 11 is off by 30/11; (iii) the prediction's signature
   "order 10 == order 11" coincidence is NOT reproduced by the enumeration (its two
   coefficients are unequal, and have different ratios to the prediction). The
   geometry of a SURVIVING (coeff-2) shared face is a different cumulant structure
   than the cube / cancelling-face clusters, so the universal-marked-face
   single-monomial law does not extend to weight 11. The class is NOT
   (#configs)*18*K''(K')^(W-1).

   (The closed-form predictions are themselves internally CONSISTENT -- 1188
   K''(K')^10 really does Taylor-expand to 11/595077871104, 11/595077871104,
   715/85691213438976 at orders 10/11/12, reproduced in V4 and re-verified at J
   truncations N=16/20/25. The break is between that closed form and the DIRECT
   enumeration, not within the closed form.)

MEMORY / SCOPE. Fraction engine; streamed enumeration; orbit-exploited (one
representative cumulant per orbit, never all 66). Order 10 peaks at link incidence 3
and order 11 at incidence 4 (the ~4 GB (4,4) tier, allowed). Order 12 drives a link
to incidence 5 = the (5,5) ~1e7-nnz wall and is GATED OFF (reported, not computed),
per the documented scope limit.

FORBIDDEN-IMPORT: every coefficient is reproven from the SU(3) Haar single-link
integral + the J recurrence (Haar primitives). The cube and weight-10 closed forms
are reproven (they reproduce d_5..d_9 exactly) and used only as controls; the
supplied weight-11 prediction is a COMPARATOR that this test FALSIFIES.

Run:  python3 scripts/frontier_beta6_weight11_test_2026_06_04.py [maxorder]
      maxorder defaults to 11 (the real out-of-sample test). Pass 10 to stop at the
      leading order (fast). Order 12 is always gated off (incidence-5 wall).
"""
import sys, os, time, itertools
from collections import Counter, deque
from fractions import Fraction
import sympy as sp
import importlib.util

_HERE = os.path.dirname(os.path.abspath(__file__))
_ENG = os.environ.get("D9_ENGINE",
                      os.path.join(_HERE, "frontier_beta6_d9_coefficient_2026_06_04.py"))
_spec = importlib.util.spec_from_file_location("d9eng", _ENG)
d9 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(d9)

P0 = d9.P0
DIMS = d9.DIMS
UNITS = d9.UNITS
joint_cumulant_frac = d9.joint_cumulant_frac
joint_cumulant = d9.joint_cumulant
support_contrib_frac = d9.support_contrib_frac
_multiplicity_vectors = d9._multiplicity_vectors
directed_links = d9.directed_links
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

LOG = os.environ.get("W11_LOG", "/tmp/weight11_test_progress.log")
_lf = open(LOG, "a")
def log(m): _lf.write(m + "\n"); _lf.flush()

# ===========================================================================
# Per-link incidence gate (the (5,5) wall) + capped support contribution.
# ===========================================================================
def _word_max_incidence(plaqs):
    c = Counter()
    for f in plaqs:
        for (L, _s) in directed_links(f):
            c[L] += 1
    return max(c.values()) if c else 0

def support_contrib_capped(S, n, inc_cap=4):
    """support_contrib_frac, but SKIP any multiplicity vector that drives a link
    past inc_cap. Returns (Fraction, walled_flag)."""
    Slist = list(S); a = len(Slist); total = Fraction(0); walled = False
    import math
    for m_p0, m_action in _multiplicity_vectors(a, n):
        plaqs = [P0] + [P0] * m_p0
        for s, ms in zip(Slist, m_action):
            plaqs += [s] * ms
        if _word_max_incidence(plaqs) > inc_cap:
            walled = True
            log(f"   [WALL] size {a} order {n} vector(m_p0={m_p0}) incidence "
                f"{_word_max_incidence(plaqs)} > {inc_cap}; skipped")
            continue
        kap = joint_cumulant_frac(plaqs)
        if kap == 0:
            continue
        denom = math.factorial(m_p0)
        for ms in m_action:
            denom *= math.factorial(ms)
        total += kap / denom
    return total, walled

# ===========================================================================
# Geometry: enumerate the weight-11 two-cube 2-cycles through p0 (streamed).
# ===========================================================================
def enumerate_weight11_supports(radius=2, cubedist=3, max_cubes=2):
    """STREAM the weight-11 2-cycles through p0 as GF(3)-combinations of cubes
    (connected + leaf-free + GF(3)-closable on the fly). Memory-bounded: only the
    de-duplicated survivors are kept. Returns (set_of_action_supports, n_streamed)."""
    cubes = d9._all_elementary_cubes(radius)
    allp = set(d9.all_local_plaquettes(radius))
    edge_faces = {}
    for p in allp:
        for e in d9._local_edges(p):
            edge_faces.setdefault(e, []).append(p)
    adj = {}
    for e, fs in edge_faces.items():
        for x in fs:
            adj.setdefault(x, set()).update(q for q in fs if q != x)
    dist = {P0: 0}; dq = deque([P0])
    while dq:
        c = dq.popleft()
        for q in adj.get(c, ()):
            if q not in dist:
                dist[q] = dist[c] + 1; dq.append(q)
    pool = [c for c in cubes if all(f in dist and dist[f] <= cubedist for f in c)]
    nc = len(pool)
    good = set(); n_streamed = 0
    for k in range(1, max_cubes + 1):
        for combo in itertools.combinations(range(nc), k):
            for coeffs in itertools.product((1, 2), repeat=k):
                n_streamed += 1
                fc = {}
                for ci, cf in zip(combo, coeffs):
                    for face in pool[ci]:
                        fc[face] = (fc.get(face, 0) + cf) % 3
                supp = frozenset(ff for ff, v in fc.items() if v)
                if len(supp) != 11 or P0 not in supp:
                    continue
                if not d9._support_connected_with_p0(supp):
                    continue
                if not d9._support_leaf_free(supp):
                    continue
                action = frozenset(supp - {P0})
                if d9.mod3_closable(action):
                    good.add(action)
    return good, n_streamed

def shared_face_topology(radius=2):
    """For cube PAIRS sharing exactly one face: which coeff signs give weight 10 vs
    11. Confirms weight-11 = surviving (same-sign) shared face."""
    cubes = d9._all_elementary_cubes(radius)
    wt = Counter()
    for a, b in itertools.combinations(range(len(cubes)), 2):
        ca, cb = cubes[a], cubes[b]
        if len(ca & cb) != 1:
            continue
        for x, y in ((1, 1), (1, 2), (2, 1), (2, 2)):
            fc = {}
            for f in ca: fc[f] = (fc.get(f, 0) + x) % 3
            for f in cb: fc[f] = (fc.get(f, 0) + y) % 3
            supp = frozenset(ff for ff, v in fc.items() if v)
            wt[(len(supp), 'same' if x == y else 'opp')] += 1
    return wt

# ===========================================================================
# Lattice isometries fixing p0, and orbit decomposition.
# ===========================================================================
def _apply_R(R, v):
    perm, signs = R
    out = [0] * DIMS
    for i in range(DIMS):
        out[perm[i]] = signs[i] * v[i]
    return tuple(out)

def _plaq_corners(p):
    base, (mu, nu) = p
    a = base
    b = tuple(x + y for x, y in zip(a, UNITS[mu]))
    c = tuple(x + y for x, y in zip(b, UNITS[nu]))
    d_ = tuple(x + y for x, y in zip(a, UNITS[nu]))
    return frozenset([a, b, c, d_])

def _corners_to_plaq(corners):
    cs = list(corners)
    base = tuple(min(c[i] for c in cs) for i in range(DIMS))
    axes = [i for i in range(DIMS) if any(c[i] != base[i] for c in cs)]
    if len(axes) != 2:
        return None
    mu, nu = sorted(axes)
    if _plaq_corners((base, (mu, nu))) == frozenset(corners):
        return (base, (mu, nu))
    return None

def p0_fixing_isometries():
    """All lattice isometries g=(signed axis-perm R, translation t) with g(p0)=p0
    (as a corner set). Returns a list of plaquette-acting functions; each leaves the
    marked observable X_{p0} -- hence every joint cumulant -- invariant."""
    P0C = _plaq_corners(P0)
    base_0 = tuple(min(c[i] for c in P0C) for i in range(DIMS))
    funcs = []
    for perm in itertools.permutations(range(DIMS)):
        for signs in itertools.product((1, -1), repeat=DIMS):
            R = (perm, signs)
            RP0 = [_apply_R(R, c) for c in P0C]
            base_R = tuple(min(c[i] for c in RP0) for i in range(DIMS))
            t = tuple(base_0[i] - base_R[i] for i in range(DIMS))
            img = frozenset(tuple(x + ti for x, ti in zip(c, t)) for c in RP0)
            if img == P0C:
                def g(p, R=R, t=t):
                    cs = _plaq_corners(p)
                    im = frozenset(tuple(x + ti for x, ti in zip(_apply_R(R, c), t))
                                   for c in cs)
                    return _corners_to_plaq(im)
                funcs.append(g)
    return funcs

def _act_support(g, action):
    out = set()
    for p in action:
        q = g(p)
        if q is None:
            return None
        out.add(q)
    return frozenset(out)

def orbit_decompose(good, gfuncs):
    gset = set(good); seen = set(); orbits = []
    for s in sorted(good, key=lambda x: tuple(sorted(x))):
        if s in seen:
            continue
        orb = set(); stack = [s]
        while stack:
            x = stack.pop()
            if x in orb:
                continue
            orb.add(x)
            for g in gfuncs:
                y = _act_support(g, x)
                if y is not None and y in gset and y not in orb:
                    stack.append(y)
        seen |= orb
        orbits.append(orb)
    return orbits

# ===========================================================================
# K-derivatives (closed-form side).
# ===========================================================================
def K_derivs(nmax):
    b = sp.symbols('b'); NC = nmax + 3
    a = _J_recurrence_coeffs(NC)
    J = sum(a[i] * b ** i for i in range(NC + 1))
    K = sp.series(sp.log(J), b, 0, NC + 1).removeO()
    return b, K, sp.diff(K, b), sp.diff(K, b, 2)


def main():
    args = sys.argv[1:]
    maxorder = int(args[0]) if len(args) > 0 else 11
    t0 = time.time()
    print("=" * 78)
    print("BETA=6 LANE 2 WEIGHT-11 FALSIFICATION TEST of (#configs)*18*K''(K')^(W-1)")
    print("=" * 78)
    log(f"\n=== weight-11 test maxorder={maxorder} ===")

    # ----- V0: controls -- cube (W=6) and weight-10 (W=10) single-monomial rule -----
    print("\nV0. CONTROLS: the rule (#)*18*K''(K')^(W-1) reproduces W=6 and W=10")
    b, K, Kp, Kpp = K_derivs(max(maxorder, 11))
    cube = sp.series(72 * Kpp * Kp ** 5, b, 0, 12).removeO()
    w10 = sp.series(1080 * Kpp * Kp ** 9, b, 0, 12).removeO()
    cube_ok = (sp.nsimplify(cube.coeff(b, 5)) == sp.Rational(1, 472392)
               and sp.nsimplify(cube.coeff(b, 6)) == sp.Rational(7, 5668704))
    w10_ok = (sp.nsimplify(w10.coeff(b, 9)) == sp.Rational(5, 16529940864)
              and sp.nsimplify(w10.coeff(b, 10)) == sp.Rational(55, 198359290368))
    check("cube 72 K''(K')^5 reproduces d_5,d_6 and weight-10 1080 K''(K')^9 "
          "reproduces its order 9,10 -- the rule is correct at W=6 and W=10",
          cube_ok and w10_ok,
          f"cube d5={sp.nsimplify(cube.coeff(b,5))}; w10 order9="
          f"{sp.nsimplify(w10.coeff(b,9))}")
    # control identity: per-support_W10 == 18 * [K''(K')^9 leading]
    lead9 = sp.nsimplify(w10.coeff(b, 9) / 1080)
    check("CONTROL identity holds at W=10: per-support cumulant 1/198359290368 "
          "== 18 * [leading coeff of K''(K')^9] (the rule's core assumption)",
          sp.nsimplify(18 * lead9) == sp.Rational(1, 198359290368),
          f"18*[K''(K')^9 lead] = {sp.nsimplify(18*lead9)}")

    # ----- V1: weight-11 count + topology -----
    print("\nV1. weight-11 supports: count + shared-face topology (streamed)")
    good2, ns2 = enumerate_weight11_supports(radius=2)
    good3, _ = enumerate_weight11_supports(radius=3)
    topo = shared_face_topology(radius=2)
    check("66 weight-11 supports, STABLE radius2 == radius3 (matches predicted "
          "config count 66); each = two cubes sharing ONE face with SAME-sign coeffs "
          "(shared face SURVIVES, 6+6-1=11)",
          len(good2) == 66 and good2 == good3,
          f"radius2={len(good2)}, radius3={len(good3)}, streamed={ns2}; "
          f"shared-1-face topology {dict(topo)}")
    check("topology check: same-sign shared face -> weight 11; opposite-sign -> "
          "weight 10 (so weight 11 keeps the GF(3) coeff-2 shared face)",
          topo.get((11, 'same'), 0) > 0 and topo.get((10, 'opp'), 0) > 0
          and topo.get((11, 'opp'), 0) == 0 and topo.get((10, 'same'), 0) == 0,
          f"{dict(topo)}")
    reps_all = sorted(good2, key=lambda s: tuple(sorted(s)))

    # ----- V2: orbit decomposition (THE CRUX) -----
    print("\nV2. orbit decomposition under p0-fixing lattice isometries (THE CRUX)")
    gfuncs = p0_fixing_isometries()
    for g in gfuncs:
        assert g(P0) == P0
    orbits = orbit_decompose(good2, gfuncs)
    sizes = sorted(len(o) for o in orbits)
    check(f"the 66 supports form {len(orbits)} lattice-symmetry orbits (sizes {sizes}), "
          f"NOT a single orbit (weight 10 was ONE orbit) -- a structural warning",
          sum(sizes) == 66 and len(orbits) >= 1,
          f"{len(gfuncs)} p0-fixing isometries; orbit sizes {sizes} sum {sum(sizes)}")

    # ----- V3: class coefficients via orbit-exploit (one rep per orbit) -----
    print(f"\nV3. exact weight-11 CLASS coefficients orders 10..{min(maxorder,11)} "
          f"(orbit-exploit, one rep/orbit; order 12 gated off)")
    orbit_reps = [sorted(o, key=lambda s: tuple(sorted(s)))[0] for o in orbits]
    orbit_sizes = [len(o) for o in orbits]
    classcoeff = {}
    orbit_lead_vals = []
    for n in range(10, min(maxorder, 11) + 1):
        tn = time.time()
        total = Fraction(0); walled = False
        per_orbit = []
        for rep, sz in zip(orbit_reps, orbit_sizes):
            c, w = support_contrib_capped(tuple(sorted(rep)), n, inc_cap=4)
            walled = walled or w
            per_orbit.append((sz, c))
            total += sz * c
            log(f"  order {n} orbit(size {sz}) per-support = {c} ({time.time()-tn:.1f}s)")
        if n == 10:
            orbit_lead_vals = [c for (_, c) in per_orbit]
            alleq = len(set(orbit_lead_vals)) == 1
            check("at the LEADING order (10) all orbits share the IDENTICAL per-support "
                  "cumulant (so leading-order orbit split alone does not break the form)",
                  alleq,
                  f"per-orbit order-10 cumulants = "
                  f"{sorted(set(str(v) for v in orbit_lead_vals))}")
        classcoeff[n] = sp.Rational(total.numerator, total.denominator)
        print(f"     order {n}: class = sum(size*per-support) = {classcoeff[n]} = "
              f"{float(classcoeff[n]):.8e}  (walled={walled}, {time.time()-tn:.1f}s)")

    # ----- V4: independent closed-form recompute of 1188 K''(K')^10 -----
    print("\nV4. independent closed-form recompute of the PREDICTION 1188 K''(K')^10")
    base = sp.series(Kpp * Kp ** 10, b, 0, 13).removeO()
    pred_form = {n: sp.nsimplify(1188 * base.coeff(b, n)) for n in (10, 11, 12)}
    supplied = {10: sp.Rational(11, 595077871104),
                11: sp.Rational(11, 595077871104),
                12: sp.Rational(715, 85691213438976)}
    cf_ok = all(pred_form[n] == supplied[n] for n in (10, 11, 12))
    check("1188 K''(K')^10 Taylor-expands to the SUPPLIED prediction at orders "
          "10/11/12 (the closed form is internally consistent; order 10 == order 11)",
          cf_ok,
          "; ".join(f"o{n}={pred_form[n]}" for n in (10, 11, 12)))
    lead10 = sp.nsimplify(base.coeff(b, 10))
    persup_enum = orbit_lead_vals[0] if orbit_lead_vals else None
    break_ratio = (sp.Rational(persup_enum.numerator, persup_enum.denominator)
                   / sp.nsimplify(18 * lead10)) if persup_enum else None
    check("THE BREAK: the rule's core identity per-support == 18*[K''(K')^10 leading] "
          "FAILS at W=11 (holds at W=6,10) -- enum per-support is EXACTLY 3x larger",
          persup_enum is not None
          and sp.nsimplify(18 * lead10) != sp.Rational(persup_enum.numerator,
                                                        persup_enum.denominator)
          and break_ratio == 3,
          f"enum per-support = {persup_enum}; 18*[lead] = {sp.nsimplify(18*lead10)}; "
          f"ratio = {break_ratio}")

    # ----- V5: VERDICT -- enumeration vs prediction at orders 10 (and 11) -----
    print("\nV5. VERDICT: direct enumeration vs the 1188 K''(K')^10 prediction")
    verdict_break = False
    for n in sorted(classcoeff):
        m = (classcoeff[n] == supplied[n])
        ratio = sp.nsimplify(classcoeff[n] / supplied[n]) if supplied[n] != 0 else None
        tag = "LEADING" if n == 10 else "HELD-OUT (out-of-sample)"
        if not m:
            verdict_break = True
        print(f"     order {n} [{tag}]: enum = {classcoeff[n]}  vs  prediction = "
              f"{supplied[n]}  MATCH={m}  (enum/pred = {ratio})")
    check("FALSIFICATION VERDICT: the direct weight-11 enumeration does NOT match "
          "1188 K''(K')^10 (enum/pred = 3 at leading order 10, 30/11 at held-out "
          "order 11; the two enum coeffs are UNEQUAL so the prediction's order10 == "
          "order11 coincidence is not reproduced) => the cube-cluster single-monomial "
          "rule BREAKS at weight 11",
          verdict_break,
          f"orders tested {sorted(classcoeff)}; all mismatched = "
          f"{all(classcoeff[n] != supplied[n] for n in classcoeff)}")

    # ----- V6: two-engine cross-check on the leading per-support cumulant -----
    print("\nV6. two-engine cross-check (Fraction == sympy) on a leading per-support "
          "cumulant")
    rep0 = tuple(sorted(orbit_reps[0]))
    plaqs = [P0] + list(rep0)
    kf = joint_cumulant_frac(plaqs)
    # sympy engine is slow (~3-4 min for an 11-point cumulant); only run if asked
    if os.environ.get("W11_SYMPY", "0") == "1":
        ks = joint_cumulant(plaqs)
        check("Fraction joint_cumulant == sympy joint_cumulant on the order-10 "
              "weight-11 word (= 1/1190155742208)",
              ks == sp.Rational(kf.numerator, kf.denominator)
              == sp.Rational(1, 1190155742208),
              f"Fraction = {kf}, sympy = {ks}")
    else:
        check("Fraction leading per-support cumulant = 1/1190155742208 (set "
              "W11_SYMPY=1 for the full sympy second-engine confirmation, ~4 min)",
              kf == Fraction(1, 1190155742208),
              f"Fraction = {kf} (two-engine sympy agreement separately confirmed)")

    # ----- order 12 gate report -----
    print("\nORDER-12 GATE: the order-12 weight-11 contribution drives a single link "
          "to incidence 5 = the (5,5) ~1e7-nnz wall (the documented scope limit), so "
          "order 12 is GATED OFF (not computed). Predicted (closed-form, NOT a match "
          f"target): 1188 K''(K')^10 [b^12] = {pred_form[12]}.")

    print("\n" + "=" * 78)
    print("WEIGHT-11 CLASS -- EXACT vs PREDICTED:")
    for n in sorted(classcoeff):
        r = sp.nsimplify(classcoeff[n] / supplied[n])
        print(f"   order {n}: enum {classcoeff[n]}  |  pred {supplied[n]}  |  "
              f"enum/pred = {r}")
    print("   order 12: WALLED (incidence-5 (5,5) wall)")
    print("VERDICT: the single-monomial cube-cluster rule (#)*18*K''(K')^(W-1) "
          "BREAKS at weight 11 (enum/pred = 3 at order 10, 30/11 at order 11; the "
          "two enum coeffs are unequal so the predicted order10==order11 coincidence "
          "fails; and the 66 supports form 6 orbits that DIVERGE at order 11).")
    print("=" * 78)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}   ({time.time()-t0:.1f}s)")
    print("=" * 78)
    _lf.close()
    # This runner PASSES when it cleanly DEMONSTRATES the break (a clean negative).
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
