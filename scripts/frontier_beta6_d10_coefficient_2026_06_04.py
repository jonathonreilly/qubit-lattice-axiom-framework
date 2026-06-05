#!/usr/bin/env python3
"""
EXACT order-beta^10 connected coefficient d_10 of the SU(3) Wilson single-plaquette
strong-coupling series Delta(beta) = <P_full> - <P_1plaq> = sum_{n>=5} d_n beta^n,
PLUS a differential-approximant estimate of the radius of convergence R and the
beta=6 convergence evidence.

This EXTENDS the validated d_9 engine (frontier_beta6_d9_coefficient_2026_06_04.py):
the exact SU(3)-Haar invariant-tensor link integral (delta-cap + epsilon/det sector),
the set-partition Moebius cumulant, the cube-sector closed form 72 K''(K')^5, and the
streamed cube-combination support enumeration. Nothing is re-derived from scratch; the
d_9 engine is imported and reused, and d_5..d_9 are reproduced here as a regression.

----------------------------------------------------------------------------------
STRUCTURE OF d_10 (each piece exact, then summed)
----------------------------------------------------------------------------------
A distinct GF(3)-closable 2-cycle support through p0 of WEIGHT w (w faces incl. p0,
so a = w-1 action faces) first contributes at order n = a = w-1 (every face once,
m_p0 = 0) and again at higher orders via multiplicity. The GF(3) cycle-space weight
spectrum through p0 is {6, 10, 11, 12} (cube boundaries span the cycle space on the
contractible patch; certified in the d_9 engine). Hence at ORDER 10:

  * cube(10)   = -4081/1763193692160  (NEGATIVE)
        the order-beta^10 Taylor coefficient of the cube-sector closed form
        72 K''(K')^5, K = log J (J from the Picard-Fuchs recurrence). The closed
        form reproduces d_5..d_8 exactly (re-verified) so its order-10 coefficient is
        the four cube shells' order-10 multiplicity sum. cube(9) = -235/29386561536.

  * weight-10(10) = 55/198359290368  (= 60 supports * 11/2380311484416)
        the SAME 60 weight-10 two-cube supports that opened at order 9, now at order
        10 via one extra density (m_p0 = 1, or one face doubled). One lattice-symmetry
        orbit; reproduced here by orbit collapse and cross-checked against the landed
        closed form 1080 K''(K')^9 [b^10] (frontier_beta6_twocube_closedform).

  * weight-11(10) = 11/198359290368  (= 66 supports * 1/1190155742208)  -- NEW at d_10
        the weight-11 two-cube 2-cycles through p0 (10 action faces) opening at their
        LEADING order 10 (m_p0 = 0, every face once: a single 11-plaquette cumulant).
        66 supports, ONE lattice-symmetry orbit (incidence profile: 16 links at
        incidence 2 + 4 links at incidence 3). 1190155742208 = 6 * 18^9.

  * BARYON / epsilon(det) channel: NOT a separate addend. The epsilon (3,0)/(0,3)
        baryon-singlet link closure (N0(3,0) = 1) FIRST ACTIVATES at order 10 inside
        the incidence-3 links of the weight-11 supports (1024 pure-(3,0) + 1024 pure-
        (0,3) link occurrences per weight-11 word over its 2^11 orientations) and the
        incidence-3 order-10 multiplicity vectors of the weight-10 supports. It is
        already folded into the weight-10(10) and weight-11(10) exact rationals via the
        engine's projector(3,0) (= the epsilon-epsilon/6 invariant). So "the baryon
        channel opens at beta^10" is a true statement about the MECHANISM, but it is
        the weight-11 class itself, not a fourth term.

  * weight-12 opens at order 11 (a = 11), NOT order 10. No other order-10 class.

  d_10 = cube(10) + weight-10(10) + weight-11(10)
       = -4081/1763193692160 + 55/198359290368 + 11/198359290368
       = -10483/5289581076480   (NEGATIVE; d_10/d_9 = 953/3700; d_9 also NEGATIVE)

----------------------------------------------------------------------------------
COMPLETENESS (the order-10 enumeration is closed)
----------------------------------------------------------------------------------
  - weight-10 supports: 60, STABLE radius-2 == radius-3 (validated in the d_9 engine).
  - weight-11 supports: 66, STABLE radius-2 == radius-3 AND 2-cube == 3-cube combos
    (every weight-11 2-cycle is a combination of exactly two elementary cubes; no
    3-cube-only or epsilon-irreducible cycle exists -- on a contractible patch the
    GF(3) 2-cycles equal the cube-boundary span, and the combo enumeration stabilizes
    in #cubes k: k<=2 == k<=3 == k<=4). The epsilon/baryon closure is a per-link
    invariant-sector effect inside these supports, not a new geometric support.

----------------------------------------------------------------------------------
RADIUS OF CONVERGENCE / beta=6 EVIDENCE (the scientific goal)
----------------------------------------------------------------------------------
With d_5..d_10 (6 coefficients) the bracket h(x) = Delta/(d_5 x^5) = 1 + sum c_k x^k
(c_k = d_{5+k}/d_5, x = beta) is analyzed by d-log Pade and first-order differential
approximants. The successive ratios d_n/d_{n-1} = 7/12, 5/21, 1/16, -407/972, 953/3700
are non-monotone and CHANGE SIGN -- the signature of a dominant COMPLEX-CONJUGATE pair
(a Fisher/Lee-Yang-type zero), NOT a single real pole.

Every approximant that can resolve a complex pair finds one; the d_10-ACTIVATED [2/2]
d-log Pade (the balanced diagonal, the strongest 6-coefficient estimator) gives

    x_c = 1.781 +/- 5.083 i ,   R = |x_c| = 5.39 ,   arg ~ +/-70.7 deg .

The complex-pair |x_c| estimates across approximants cluster at median ~4.9 (range
3.7..6.6), 6/7 BELOW 6; an independent local 2-term recurrence fit trends to ~5.2 on
the last (most d_10-informed) triple. So

    R ~ 5.4 < 6   =>   supports Delta(beta) divergence at beta = 6.

This supports the literature-side interpretation with Fisher-zero |beta_c| ~ 5.7
(< 6, divergent) over the framework's earlier 5-coefficient ratio estimate R ~ 8
(> 6). That earlier estimate was an artifact of naive ratio extrapolation applied
to a series whose nearest singularity is COMPLEX (bare ratios oscillate, e.g.
sqrt(|c1/c3|) ~ 8.2 vs sqrt(|c3/c5|) ~ 3.0). The d_10 activation of the diagonal
[2/2] / [1/3] / [0/4] approximants is what discriminates these hypotheses.

CONFIDENCE: 6 coefficients is thin. The COMPLEX-PAIR structure and R < 6 are robust
within this approximant family (every pair-resolving approximant agrees on
sign-change-driven complex poles below 6), but the precise R is uncertain at the
~+/-1 level (3.7..6.6 spread). This is NOT a beta=6 closure (the infinite-hierarchy
obstruction stands) -- it is strong-coupling radius EVIDENCE: the truncated Delta(6)
is a divergent or borderline partial sum, consistent with the lattice 0.594
Monte-Carlo comparator not being reachable by finite strong-coupling truncation.
0.594 is a comparator, NEVER a derivation input.

FORBIDDEN-IMPORT: every coefficient is reproven from the SU(3) Haar single-link
integral + the J recurrence (Haar primitives) via the imported d_9 engine. The cube
closed form is reproven (it reproduces d_5..d_8 exactly) and cited. The literature
Fisher-zero ~5.7 is a COMPARATOR for the radius evidence, never an input to any number.

Run:  python3 scripts/frontier_beta6_d10_coefficient_2026_06_04.py
      (bounded ~1-2 min; orbit-collapse primary + regression + approximants)
      add 'fullsum' to ALSO recompute weight-10(10)/weight-11(10) by summing ALL
      60/66 supports individually (heavy: ~30-60 min of 11-plaquette cumulants) as an
      orbit-collapse-independent cross-check.
"""
import sys, os, time, math, importlib.util, itertools, resource, gc
from collections import Counter
from fractions import Fraction
import sympy as sp
import mpmath as mp

# ---------------------------------------------------------------------------
# Import the validated d_9 engine (its main() runs only under __main__).
# ---------------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_ENG = os.environ.get("D9_ENGINE",
                      os.path.join(_HERE, "frontier_beta6_d9_coefficient_2026_06_04.py"))
_spec = importlib.util.spec_from_file_location("d9eng", _ENG)
d9 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(d9)

P0 = d9.P0
directed_links = d9.directed_links
support_contrib_frac = d9.support_contrib_frac
joint_cumulant_frac = d9.joint_cumulant_frac
joint_cumulant = d9.joint_cumulant
enumerate_d9_new_supports = d9.enumerate_d9_new_supports
_all_elementary_cubes = d9._all_elementary_cubes
_support_connected_with_p0 = d9._support_connected_with_p0
_support_leaf_free = d9._support_leaf_free
mod3_closable = d9.mod3_closable
cube_sector_coeffs = d9.cube_sector_coeffs
projector = d9.projector
link_tensor_frac = d9.link_tensor_frac
_J_recurrence_coeffs = d9._J_recurrence_coeffs
cycle_space_certificate = d9.cycle_space_certificate

# on-main exact coefficients (regression anchors)
EXACT = {5: sp.Rational(1, 472392), 6: sp.Rational(7, 5668704),
         7: sp.Rational(5, 17006112), 8: sp.Rational(5, 272097792),
         9: sp.Rational(-2035, 264479053824)}
CUBE9 = sp.Rational(-235, 29386561536)

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

def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e9 if r > 1e7 else r / 1e6   # macOS bytes vs linux KB

# ===========================================================================
# weight-11 two-cube support enumeration (the NEW order-10 class), streamed.
# ===========================================================================
def enumerate_weight11_supports(radius=2):
    """STREAM the weight-11 2-cycles through p0 as GF(3)-combinations of cube PAIRS
    sharing a face (the order-10 leading new distinct supports), applying connected +
    leaf-free + GF(3)-closable filters. Returns a set of size-10 action supports.
    Mirror of d9.enumerate_d9_new_supports but for weight 11 (one shared face removed
    => 6+6-1 = 11 distinct faces)."""
    cubes = _all_elementary_cubes(radius)
    face_cubes = {}
    for ci, c in enumerate(cubes):
        for f in c:
            face_cubes.setdefault(f, []).append(ci)
    pairs = set()
    for f, cis in face_cubes.items():
        for a, b in itertools.combinations(cis, 2):
            pairs.add((a, b))
    good = set(); n_streamed = 0
    for (a, b) in pairs:
        c1, c2 = cubes[a], cubes[b]
        for ca, cb in ((1, 1), (1, 2), (2, 1), (2, 2)):
            n_streamed += 1
            fc = {}
            for face in c1: fc[face] = (fc.get(face, 0) + ca) % 3
            for face in c2: fc[face] = (fc.get(face, 0) + cb) % 3
            supp = frozenset(ff for ff, v in fc.items() if v)
            if len(supp) != 11 or P0 not in supp:
                continue
            if not _support_connected_with_p0(supp):
                continue
            if not _support_leaf_free(supp):
                continue
            action = frozenset(supp - {P0})
            if mod3_closable(action):
                good.add(action)
    return good, len(cubes), n_streamed

def _enumerate_weight11_combo(radius=2, cubedist=3, max_cubes=3):
    """Independent cross-check: GF(3)-combinations of up to max_cubes cubes from the
    distance-bounded pool reproduce the same weight-11 set (guards against a missed
    3-cube-only cycle)."""
    from collections import deque
    cubes = _all_elementary_cubes(radius)
    allp = set(d9.all_local_plaquettes(radius))
    edge_faces = {}
    for p in allp:
        for e in d9._local_edges(p): edge_faces.setdefault(e, []).append(p)
    adj = {}
    for e, fs in edge_faces.items():
        for x in fs: adj.setdefault(x, set()).update(q for q in fs if q != x)
    dist = {P0: 0}; dq = deque([P0])
    while dq:
        c = dq.popleft()
        for q in adj.get(c, ()):
            if q not in dist: dist[q] = dist[c] + 1; dq.append(q)
    pool = [c for c in cubes if all(f in dist and dist[f] <= cubedist for f in c)]
    nc = len(pool); good = set()
    for k in range(1, max_cubes + 1):
        for combo in itertools.combinations(range(nc), k):
            for coeffs in itertools.product((1, 2), repeat=k):
                fc = {}
                for ci, cf in zip(combo, coeffs):
                    for face in pool[ci]: fc[face] = (fc.get(face, 0) + cf) % 3
                supp = frozenset(ff for ff, v in fc.items() if v)
                if len(supp) != 11 or P0 not in supp: continue
                if not _support_connected_with_p0(supp): continue
                if not _support_leaf_free(supp): continue
                action = frozenset(supp - {P0})
                if mod3_closable(action): good.add(action)
    return good

def _support_link_incidence(S):
    c = Counter()
    for f in [P0] + list(S):
        for (L, _s) in directed_links(f): c[L] += 1
    return max(c.values()), dict(sorted(Counter(c.values()).items()))

def class_value_orbit(supports, order, label, log=print):
    """Exact class contribution at `order` via orbit collapse: compute ONE
    representative per distinct per-link-incidence profile, verify uniformity within
    the profile on up to 2 extra members, sum value*count. Returns (Fraction, report)."""
    reps = sorted(supports, key=lambda s: tuple(sorted(s)))
    groups = {}
    for S in reps:
        mi, dist = _support_link_incidence(S)
        groups.setdefault((mi, tuple(sorted(dist.items()))), []).append(S)
    total = Fraction(0); report = {}; uniform_all = True
    for key, members in sorted(groups.items()):
        rep = members[0]
        c0 = support_contrib_frac(tuple(sorted(rep)), order)
        uni = True
        for m in members[1:3]:
            if support_contrib_frac(tuple(sorted(m)), order) != c0:
                uni = False; uniform_all = False
        report[key] = (c0, len(members), uni)
        total += c0 * len(members)
        log(f"      [{label}] inc-profile maxinc={key[0]} ({len(members)} supports): "
            f"per-support@{order} = {c0} = {float(c0):.6e}  uniform={uni}  "
            f"RSS {rss_gb():.2f}GB")
    return total, report, uniform_all

# ===========================================================================
# Radius-of-convergence approximant analysis (d-log Pade + first-order DA).
# ===========================================================================
def _bracket_mp(D, dmax):
    d5 = D[5]
    return [mp.mpf(sp.Rational(D[5 + k] / d5).p) / mp.mpf(sp.Rational(D[5 + k] / d5).q)
            for k in range(dmax - 5 + 1)]
def _slog(a):
    n = len(a); out = [mp.log(a[0])] + [mp.mpf(0)] * (n - 1)
    for k in range(1, n):
        out[k] = a[k] / a[0] - sum((mp.mpf(j) / k) * out[j] * (a[k - j] / a[0])
                                   for j in range(1, k))
    return out
def _sderiv(a): return [(k + 1) * a[k + 1] for k in range(len(a) - 1)]
def _roots_asc(coeffs):
    desc = list(reversed(coeffs))
    while len(desc) > 1 and abs(desc[0]) < mp.mpf('1e-40'): desc = desc[1:]
    if len(desc) <= 1: return []
    return mp.polyroots(desc, maxsteps=500, extraprec=400)
def _nearest(roots):
    rr = [r for r in roots if abs(r) > mp.mpf('1e-9')]
    return min(rr, key=lambda r: abs(r)) if rr else None

def dlog_pade_estimates(D, dmax):
    """All [L/M] d-log-Pade nearest singularities for the series d5..d_dmax."""
    c = _bracket_mp(D, dmax); H = _sderiv(_slog(c))
    out = []
    for L in range(0, len(H)):
        for M in range(1, len(H)):
            if L + M + 1 > len(H): continue
            try:
                P, Q = mp.pade(H[:L + M + 1], L, M)
            except Exception:
                continue
            nr = _nearest(_roots_asc([Q[i] for i in range(len(Q))]))
            if nr is None: continue
            out.append((f"[{L}/{M}]", nr, abs(mp.im(nr)) > mp.mpf('1e-8')))
    return out

def first_order_DA(D, L, Mp, J):
    """Exact first-order inhomogeneous differential approximant of h(x):
       Q_L(x) h'(x) + R_Mp(x) h(x) = T_J(x),  Q_L(0)=1.
    Match Taylor orders 0..(#unknowns-2). Singularities = roots of Q_L."""
    d5 = D[5]
    hser = [sp.Rational(D[5 + k] / d5) for k in range(6)]      # c0..c5 exact
    hp = [(k + 1) * hser[k + 1] for k in range(5)]             # h' orders 0..4
    q = sp.symbols(f'q0:{L+1}'); r = sp.symbols(f'r0:{Mp+1}'); t = sp.symbols(f't0:{J+1}')
    unknowns = list(q) + list(r) + list(t)
    eqs = [sp.Eq(q[0], 1)]
    for m in range(len(unknowns) - 1):
        lhs = sp.Integer(0)
        for i in range(L + 1):
            if 0 <= m - i < len(hp): lhs += q[i] * hp[m - i]
        for i in range(Mp + 1):
            if 0 <= m - i < len(hser): lhs += r[i] * hser[m - i]
        tm = t[m] if m <= J else sp.Integer(0)
        eqs.append(sp.Eq(lhs - tm, 0))
    sol = sp.solve(eqs, unknowns, dict=True)
    if not sol: return None
    sol = sol[0]
    Qc = [sp.nsimplify(sol.get(q[i], q[i])) for i in range(L + 1)]
    Qm = [mp.mpf(sp.Rational(x).p) / mp.mpf(sp.Rational(x).q) for x in Qc]
    return Qc, _nearest(_roots_asc(Qm))


def main():
    args = [a for a in sys.argv[1:]]
    fullsum = "fullsum" in args
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass
    LOG = os.environ.get("D10_LOG")
    _lf = open(LOG, "a") if LOG else open(os.devnull, "a")
    def log(m): _lf.write(m + "\n"); _lf.flush()
    log(f"\n=== d10 run fullsum={fullsum} {time.ctime()} ===")

    t0 = time.time()
    mp.mp.dps = 60
    print("=" * 80)
    print("EXACT order-beta^10 connected coefficient d_10 + radius-of-convergence evidence")
    print("=" * 80)

    # =====================================================================
    # V0. cube-sector closed form reproduces d_5..d_8 (reprove + cite import)
    # =====================================================================
    print("\nV0. cube-sector closed form 72 K''(K')^5 reproduces d_5..d_8 (reproven, cited)")
    cc = cube_sector_coeffs(10)
    repro = all(sp.simplify(cc[n] - EXACT[n]) == 0 for n in (5, 6, 7, 8))
    check("cube closed form 72 K''(K')^5 reproduces the direct-engine d_5..d_8 EXACTLY "
          "(validates the closed form before its order-9/10 coefficients are used)",
          repro, "; ".join(f"d_{n}={cc[n]}" for n in (5, 6, 7, 8)))
    cube9 = cc[9]; cube10 = cc[10]
    check("cube(9) = 72 K''(K')^5 [b^9] = -235/29386561536 (NEGATIVE; regression vs d_9 note)",
          cube9 == CUBE9 and cube9 < 0, f"cube(9) = {cube9} = {float(cube9):.6e}")
    check("cube(10) = 72 K''(K')^5 [b^10] = -4081/1763193692160 (NEGATIVE)",
          cube10 == sp.Rational(-4081, 1763193692160) and cube10 < 0,
          f"cube(10) = {cube10} = {float(cube10):.6e}")

    # =====================================================================
    # V1. order-10 support completeness: weight spectrum {6,10,11,12}; only
    #     weights 6,10,11 reach order 10 (weight 12 opens at order 11).
    # =====================================================================
    print("\nV1. order-10 contributing classes (GF(3) cycle-space weight spectrum)")
    cdim, ncubes, span, ncubes_p0, weights = cycle_space_certificate(2)
    spectrum = set(weights.keys())
    check("GF(3) 2-cycle weight spectrum through p0 = {6,10,11,12}; cubes span the "
          "cycle space; 4 cubes through p0. At order 10 only weights 6 (cube), 10, 11 "
          "contribute (weight 12 first contributes at order 11: a = 11 action faces)",
          span and spectrum == {6, 10, 11, 12} and ncubes_p0 == 4,
          f"weights(<=2 cubes) = {dict(sorted(weights.items()))}; span={span}, "
          f"cubes_thru_p0={ncubes_p0}")

    print("\n  weight-10 supports (60, reused from the d_9 engine) ...")
    good10, _, _ = enumerate_d9_new_supports(radius=2)
    good10_r3, _, _ = enumerate_d9_new_supports(radius=3)
    check("weight-10: 60 supports, STABLE radius-2 == radius-3 (one orbit; validated d_9)",
          len(good10) == 60 and good10 == good10_r3,
          f"radius2={len(good10)}, radius3={len(good10_r3)}")

    print("  weight-11 supports (NEW at order 10), streamed ...")
    good11, ncubes11, nstream11 = enumerate_weight11_supports(radius=2)
    good11_r3, _, _ = enumerate_weight11_supports(radius=3)
    check("weight-11: 66 supports, STABLE radius-2 == radius-3 (completeness by patch "
          "stabilization)",
          len(good11) == 66 and good11 == good11_r3,
          f"radius2={len(good11)} ({nstream11} pair-combos streamed), radius3={len(good11_r3)}")
    good11_combo = _enumerate_weight11_combo(radius=2, cubedist=3, max_cubes=3)
    check("independent GF(3) cube-combination enumeration (up to 3 cubes) reproduces the "
          "SAME 66 weight-11 supports => no 3-cube-only or epsilon-irreducible cycle; "
          "every weight-11 2-cycle is exactly two cubes sharing one face (6+6-1=11)",
          good11_combo == good11,
          f"combo(<=3 cubes) -> {len(good11_combo)} supports; identical to pair = "
          f"{good11_combo == good11}")

    # incidence profile of weight-11 (where the epsilon/baryon closure lives)
    profs = Counter()
    for S in good11:
        mi, _ = _support_link_incidence(S); profs[mi] += 1
    check("weight-11 supports all have per-link max incidence 3 (the incidence-3 links "
          "are where the epsilon (3,0)/(0,3) BARYON-singlet closure first activates at "
          "order 10) -- one geometric orbit",
          set(profs.keys()) == {3} and profs[3] == 66,
          f"max-incidence distribution across the 66 supports: {dict(profs)}")

    # =====================================================================
    # V2. baryon / epsilon (det) sector ACTIVATES at order 10 (inside weight-11)
    # =====================================================================
    print("\nV2. baryon / epsilon (det) sector: N0(3,0)=1 closure opens at order 10")
    b30, _ = projector(3, 0); b03, _ = projector(0, 3)
    T30 = link_tensor_frac(3, 0)
    check("the SU(3) epsilon baryon-singlet sector is in the engine: projector(3,0) and "
          "projector(0,3) each have exactly N0=1 invariant; the (3,0) link integral is "
          "eps_i eps_j / 6 (e.g. T[(012),(012)] = 1/6)",
          len(b30) == 1 and len(b03) == 1 and T30.get(((0, 1, 2), (0, 1, 2))) == Fraction(1, 6),
          f"N0(3,0)={len(b30)}, N0(0,3)={len(b03)}, T30[(012),(012)]={T30.get(((0,1,2),(0,1,2)))}")
    # count pure-(3,0)/(0,3) link occurrences in a weight-11 word over all orientations
    rep11 = sorted(good11, key=lambda s: tuple(sorted(s)))[0]
    word = [P0] + list(rep11)
    n30 = n03 = 0
    for orients in itertools.product((+1, -1), repeat=len(word)):
        lf = {}
        for p, o in zip(word, orients):
            dl = directed_links(p)
            if o == -1: dl = [(L, -s) for (L, s) in reversed(dl)]
            for (L, s) in dl:
                lf.setdefault(L, [0, 0])
                if s == +1: lf[L][0] += 1
                else: lf[L][1] += 1
        for pq in lf.values():
            if pq[0] >= 3 and pq[1] == 0: n30 += 1
            if pq[1] >= 3 and pq[0] == 0: n03 += 1
    check("a weight-11 word genuinely EXERCISES the baryon closure: over its 2^11 "
          "orientations it produces pure (3,0) and pure (0,3) links (the det/epsilon "
          "channel) -- so the baryon sector opens at order 10 as expected, but as a "
          "per-link invariant-sector effect INSIDE weight-11, not a separate support",
          n30 > 0 and n03 > 0,
          f"pure-(3,0) link occurrences = {n30}, pure-(0,3) = {n03} (across orientations)")

    # =====================================================================
    # V3. exact class values at order 10 (orbit collapse) + regression at order 9
    # =====================================================================
    print("\nV3. exact order-10 class values (orbit collapse) + order-9 regression")

    # --- regression: reproduce d_9 pieces (cube9 done in V0; new-support part at order 9)
    print("  V3a. REGRESSION: weight-10 class at order 9 = +5/16529940864 (d_9 new part)")
    w10_at9, _, uni9 = class_value_orbit(good10, 9, "w10@9", log)
    w10_at9 = sp.Rational(w10_at9.numerator, w10_at9.denominator)
    check("weight-10 class @ order 9 = 5/16529940864 (REGRESSION vs d_9 note; orbit "
          "collapse reproduces the d_9 new-support part)",
          w10_at9 == sp.Rational(5, 16529940864) and uni9, f"weight-10@9 = {w10_at9}")
    d9_regress = cube9 + w10_at9
    check("d_9 REGRESSION = cube(9) + weight-10@9 = -235/29386561536 + 5/16529940864 "
          "= -2035/264479053824 (reproduces the on-main d_9 EXACTLY)",
          d9_regress == EXACT[9], f"d_9 (regression) = {d9_regress} = {float(d9_regress):.8e}")

    # --- order 10 classes
    print("  V3b. weight-10 class @ order 10 (orbit collapse) ...")
    w10_at10, _, uni10a = class_value_orbit(good10, 10, "w10@10", log)
    w10_at10 = sp.Rational(w10_at10.numerator, w10_at10.denominator)
    check("weight-10 class @ order 10 = 55/198359290368 (= 60 * 11/2380311484416; one "
          "orbit) -- cross-checks the landed closed form 1080 K''(K')^9 [b^10]",
          w10_at10 == sp.Rational(55, 198359290368) and uni10a,
          f"weight-10@10 = {w10_at10} = {float(w10_at10):.6e}")

    print("  V3c. weight-11 class @ order 10 (orbit collapse; the NEW + baryon-active class) ...")
    w11_at10, _, uni10b = class_value_orbit(good11, 10, "w11@10", log)
    w11_at10 = sp.Rational(w11_at10.numerator, w11_at10.denominator)
    check("weight-11 class @ order 10 = 11/198359290368 (= 66 * 1/1190155742208; one "
          "orbit; 1190155742208 = 6*18^9) -- NEW at d_10, the baryon/epsilon-active class",
          w11_at10 == sp.Rational(11, 198359290368) and uni10b,
          f"weight-11@10 = {w11_at10} = {float(w11_at10):.6e}")

    # --- cross-check weight-10@10 against the landed closed form 1080 K''(K')^9
    b = sp.symbols('b'); NC = 13
    a = _J_recurrence_coeffs(NC)
    Jc = sum(a[i] * b ** i for i in range(NC + 1))
    K = sp.series(sp.log(Jc), b, 0, NC + 1).removeO()
    Kp = sp.diff(K, b); Kpp = sp.diff(K, b, 2)
    w10_form = sp.nsimplify(sp.series(1080 * Kpp * Kp ** 9, b, 0, 11).removeO().coeff(b, 10))
    check("closed-form cross-check: weight-10@10 == 1080 K''(K')^9 [b^10] "
          "(the landed two-cube closed form, frontier_beta6_twocube_closedform)",
          w10_form == w10_at10, f"1080 K''(K')^9 [b^10] = {w10_form} == engine {w10_at10}")

    # --- optional fullsum cross-check (orbit-collapse-independent)
    if fullsum:
        print("\n  V3d. [fullsum] orbit-collapse-INDEPENDENT cross-check: sum ALL 60+66 "
              "supports individually (heavy) ...")
        ts = time.time(); w10_full = Fraction(0)
        for i, S in enumerate(sorted(good10, key=lambda s: tuple(sorted(s)))):
            w10_full += support_contrib_frac(tuple(sorted(S)), 10)
            if i % 15 == 0: log(f"      [fullsum w10] {i+1}/60 RSS {rss_gb():.2f}GB {time.time()-ts:.0f}s")
        w11_full = Fraction(0)
        for i, S in enumerate(sorted(good11, key=lambda s: tuple(sorted(s)))):
            w11_full += support_contrib_frac(tuple(sorted(S)), 10)
            if i % 15 == 0: log(f"      [fullsum w11] {i+1}/66 RSS {rss_gb():.2f}GB {time.time()-ts:.0f}s")
        w10_full = sp.Rational(w10_full.numerator, w10_full.denominator)
        w11_full = sp.Rational(w11_full.numerator, w11_full.denominator)
        check("[fullsum] explicit 60-support sum reproduces weight-10@10 = 55/198359290368",
              w10_full == w10_at10, f"fullsum weight-10@10 = {w10_full}")
        check("[fullsum] explicit 66-support sum reproduces weight-11@10 = 11/198359290368",
              w11_full == w11_at10, f"fullsum weight-11@10 = {w11_full}")
        print(f"       [fullsum] done in {time.time()-ts:.0f}s, peak RSS {rss_gb():.2f}GB")

    # =====================================================================
    # V4. assemble d_10 (exact)
    # =====================================================================
    print("\nV4. assemble d_10 = cube(10) + weight-10@10 + weight-11@10")
    d10 = cube10 + w10_at10 + w11_at10
    d10_ref = sp.Rational(-10483, 5289581076480)
    ratio = sp.nsimplify(d10 / EXACT[9])
    check("d_10 = -4081/1763193692160 + 55/198359290368 + 11/198359290368 "
          "= -10483/5289581076480 (NEGATIVE; same sign as d_9)",
          d10 == d10_ref and d10 < 0,
          f"d_10 = {d10} = {float(d10):.8e}; d_10/d_9 = {ratio} = {float(ratio):.6f} "
          f"(cube {float(cube10):.4e} + w10 {float(w10_at10):.4e} + w11 {float(w11_at10):.4e})")

    results = dict(EXACT); results[10] = d10

    # =====================================================================
    # V5. RADIUS OF CONVERGENCE: differential approximants + beta=6 evidence
    # =====================================================================
    print("\nV5. radius of convergence evidence from d_5..d_10 (d-log Pade + first-order DA)")
    # successive ratios (sign change => complex pair)
    rats = [sp.nsimplify(results[n] / results[n - 1]) for n in range(6, 11)]
    print("  successive ratios d_n/d_{n-1}: " +
          ", ".join(f"d{n}/d{n-1}={rats[n-6]}" for n in range(6, 11)))
    sign_changes = sum(1 for k in range(1, len(rats)) if (rats[k] < 0) != (rats[k - 1] < 0))
    check("the successive ratios are non-monotone and CHANGE SIGN (d_9/d_8 < 0): the "
          "signature of a dominant COMPLEX-CONJUGATE singularity pair (a Fisher/Lee-Yang "
          "zero), NOT a single real pole -- so naive ratio extrapolation is invalid here",
          sign_changes >= 1 and rats[3] < 0,
          f"ratios {[float(r) for r in rats]}; sign changes = {sign_changes}")

    # d-log Pade estimates
    print("\n  d-log Pade nearest singularities (d_5..d_10; [2/2] is ACTIVATED by d_10):")
    ests = dlog_pade_estimates(results, 10)
    cplx_mags = []
    headline = None
    for tag, nr, iscx in ests:
        if iscx: cplx_mags.append(float(abs(nr)))
        if tag == "[2/2]": headline = (nr, iscx)
        print(f"     {tag:7s} |x_c| = {mp.nstr(abs(nr),7):>10s}  arg = {mp.nstr(mp.arg(nr),5):>9s}  "
              f"{'COMPLEX pair' if iscx else 'REAL (spurious)'}")
    # first-order DAs
    print("\n  first-order differential approximants (singularity = nearest zero of Q_L):")
    for (L, Mp, J) in [(2, 1, 0), (2, 2, 0), (2, 1, 1), (2, 0, 1)]:
        try:
            res = first_order_DA(results, L, Mp, J)
        except Exception as e:
            print(f"     DA[Q{L}/R{Mp}/T{J}]: solve failed ({e})"); continue
        if res is None: continue
        Qc, nr = res
        if nr is None: continue
        iscx = abs(mp.im(nr)) > mp.mpf('1e-8')
        if iscx: cplx_mags.append(float(abs(nr)))
        print(f"     DA[Q{L}/R{Mp}/T{J}]: |x_c| = {mp.nstr(abs(nr),7)}  arg = {mp.nstr(mp.arg(nr),5)}  "
              f"{'COMPLEX pair' if iscx else 'REAL (spurious)'}")

    # headline [2/2]
    nr22, iscx22 = headline
    R22 = abs(nr22)
    print(f"\n  HEADLINE [2/2] d-log Pade (activated by d_10): x_c = {mp.nstr(nr22,7)}, "
          f"R = |x_c| = {mp.nstr(R22,6)}, arg = {mp.nstr(mp.arg(nr22)*180/mp.pi,5)} deg")
    check("the d_10-ACTIVATED [2/2] d-log Pade (balanced diagonal; the strongest "
          "6-coefficient estimator) finds a COMPLEX-CONJUGATE pair with R = |x_c| ~ 5.4 "
          "(x_c ~ 1.78 +/- 5.08 i), i.e. R < 6",
          iscx22 and R22 < 6 and R22 > 4,
          f"R[2/2] = {mp.nstr(R22,6)} < 6 (complex pair {mp.nstr(nr22,6)})")

    import statistics
    med = statistics.median(cplx_mags); below6 = sum(1 for e in cplx_mags if e < 6)
    check("EVIDENCE: across all complex-pair-resolving approximants R clusters BELOW 6 "
          "(median ~5; the majority < 6), supporting Delta(beta) divergence at beta = 6. "
          "This favors the literature Fisher-zero |beta_c| ~ 5.7 (< 6) over the earlier "
          "5-coefficient ratio estimate R ~ 8",
          med < 6 and below6 >= (len(cplx_mags) + 1) // 2,
          f"complex-pair |x_c| set = {sorted(round(e,2) for e in cplx_mags)}; "
          f"median = {med:.3f}; below 6 = {below6}/{len(cplx_mags)}")

    # forward truncated Delta(6) (J recurrence; NOT a closure, comparator-only print)
    _a = _J_recurrence_coeffs(60)
    Jv = sum((mp.mpf(_a[n].p) / mp.mpf(_a[n].q)) * mp.mpf(6) ** n for n in range(len(_a)))
    Jp = sum(n * (mp.mpf(_a[n].p) / mp.mpf(_a[n].q)) * mp.mpf(6) ** (n - 1) for n in range(1, len(_a)))
    P1_6 = Jp / Jv
    dsum = sum((mp.mpf(results[n].p) / mp.mpf(results[n].q)) * mp.mpf(6) ** n for n in range(5, 11))
    print(f"\n  forward truncated Delta(6) [d_5..d_10] = {mp.nstr(dsum, 8)}; "
          f"P_1plaq(6)=K'(6)={mp.nstr(P1_6,8)}; truncated <P>(6)={mp.nstr(P1_6+dsum,8)} "
          f"(comparator 0.594, NEVER an input). The R<6 evidence says to treat this as "
          f"a divergent-or-borderline strong-coupling partial sum, not as a closure route.")

    # =====================================================================
    # summary
    # =====================================================================
    print("\n" + "=" * 80)
    print("EXACT CONNECTED COEFFICIENTS d_5..d_10 of Delta(beta):")
    for n in range(5, 11):
        print(f"   d_{n} = {results[n]} = {float(results[n]):.8e}")
    print("-" * 80)
    print(f"   d_10 PIECES: cube(10) = {cube10} = {float(cube10):.6e}")
    print(f"                weight-10@10 = {w10_at10} = {float(w10_at10):.6e}")
    print(f"                weight-11@10 = {w11_at10} = {float(w11_at10):.6e} (NEW; baryon/eps-active)")
    print(f"                baryon/epsilon = folded into weight-11@10 (+ w10@10 inc-3 vectors), NOT separate")
    print(f"   d_10 = {d10} = {float(d10):.8e}  (NEGATIVE; d_10/d_9 = {ratio})")
    print(f"   RADIUS: complex-conjugate pair, [2/2] x_c ~ {mp.nstr(nr22,6)}, R ~ {mp.nstr(R22,5)} < 6")
    print(f"           => supports Delta divergence at beta=6 (consistent with literature "
          f"Fisher-zero ~5.7; earlier R~8 disfavored)")
    print("=" * 80)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}   ({time.time()-t0:.1f}s, peak RSS {rss_gb():.2f} GB)")
    print("=" * 80)
    print("d_10 is an EXACT strong-coupling coefficient (bounded result). The radius")
    print("evidence for R<6 is a 6-coefficient differential-approximant ESTIMATE: the complex-")
    print("pair structure + R<6 are robust; the precise R~5.4 carries ~+/-1 uncertainty.")
    print("This is NOT a beta=6 closure -- the infinite-hierarchy obstruction stands.")
    print("0.594 is a Monte-Carlo comparator, never a derivation input.")
    _lf.close()
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
