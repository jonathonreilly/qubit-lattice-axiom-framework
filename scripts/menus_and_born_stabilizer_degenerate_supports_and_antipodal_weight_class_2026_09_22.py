#!/usr/bin/env python3
"""Menus and Born: stabiliser-degenerate covariant supports and the antipodal
weight class, exact and finite.

Wave B (menus-and-Born) of the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic throughout; no floating point enters any
check.

Declared objects
  * rotations as 3x3 rational matrices: the proper cubic group O (the 24
    signed permutation matrices of determinant +1) and rational SO(3)
    elements outside O built from Pythagorean triples and quadruples;
  * analytic values on the real unit sphere; exact rational unit witnesses;
    normalized integer directions for the finite cube alphabets;
  * neighbour configurations as maps position -> recorded value, acted on
    under the soldered reading (one rotation moves positions and values) and
    under the unsoldered reading (a lattice rotation moves positions, an
    independent internal rotation moves values);
  * antipodal-menu weight functions f(t), t = p.q, as exact polynomials in t:
    Born (1+t)/2, the cubic witness (1+t^3)/2, the monotone witness
    (1+t)/2 + t(1-t^2)/8;
  * Haar-uniform relative orientation: t uniform on [-1, 1] with density
    dt/2, integrated exactly; and the finite soldered alphabets (6, 8, 12
    point cube orbits) with their exact O-orbit structure on ordered pairs.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from fractions import Fraction as Fr
from itertools import permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------- exact linear algebra
def V(*xs):
    return tuple(Fr(x) for x in xs)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fr(0))


def neg(a):
    return tuple(-x for x in a)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scl(c, a):
    c = Fr(c)
    return tuple(c * x for x in a)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def Mx(rows):
    return tuple(tuple(Fr(x) for x in r) for r in rows)


I3 = Mx([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def mv(A, v):
    return tuple(dot(r, v) for r in A)


def mm(A, B):
    return tuple(tuple(sum((A[i][k] * B[k][j] for k in range(3)), Fr(0)) for j in range(3)) for i in range(3))


def tr(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


def det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def is_rot(A):
    return mm(A, tr(A)) == I3 and det(A) == 1


def rot180(n):
    """180-degree rotation about the rational unit vector n: 2 n n^T - I."""
    assert dot(n, n) == 1
    return tuple(tuple(2 * n[i] * n[j] - (1 if i == j else 0) for j in range(3)) for i in range(3))


def frame(u, v, w):
    """Matrix with columns u, v, w: it maps e_x, e_y, e_z to u, v, w."""
    cols = (u, v, w)
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))


def cubic_group():
    """Proper cubic rotations: signed permutation matrices of determinant +1."""
    G = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            A = [[Fr(0)] * 3 for _ in range(3)]
            for i in range(3):
                A[i][perm[i]] = Fr(signs[i])
            A = tuple(tuple(r) for r in A)
            if det(A) == 1:
                G.append(A)
    return G


EX, EY, EZ = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
SIX_AXES = (EX, neg(EX), EY, neg(EY), EZ, neg(EZ))

# rational SO(3) elements outside the cubic group, and rational unit vectors
RZ345 = Mx([[Fr(3, 5), Fr(-4, 5), 0], [Fr(4, 5), Fr(3, 5), 0], [0, 0, 1]])   # rotation about z
Q_GEN = V(Fr(3, 13), Fr(4, 13), Fr(12, 13))      # generic rational unit vector
U_GEN = V(Fr(4, 5), Fr(-3, 5), 0)                # rational unit vector orthogonal to Q_GEN
Q_XZ = V(Fr(3, 5), 0, Fr(4, 5))                  # in the mirror plane q_y = 0
N_XZ = V(Fr(4, 5), 0, Fr(-3, 5))                 # unit, orthogonal to Q_XZ
Q_XY = V(Fr(3, 5), Fr(4, 5), 0)                  # in no mirror plane of the z-swappers
Q_DIAG = V(Fr(2, 3), Fr(2, 3), Fr(1, 3))         # in the mirror plane q_x = q_y
Q_BIS = V(Fr(2, 3), Fr(1, 3), Fr(-2, 3))         # orthogonal to (1,0,1): q_x + q_z = 0
Q_NBIS = V(Fr(2, 3), Fr(1, 3), Fr(2, 3))         # not orthogonal to (1,0,1)


# ---------------------------------------------------------------- exact polynomials in t
def P(d):
    return {k: Fr(v) for k, v in d.items() if Fr(v) != 0}


def pev(p, t):
    t = Fr(t)
    return sum((c * t ** k for k, c in p.items()), Fr(0))


def padd(p, q):
    r = dict(p)
    for k, c in q.items():
        r[k] = r.get(k, Fr(0)) + c
    return P(r)


def pscl(c, p):
    return P({k: Fr(c) * v for k, v in p.items()})


def pmul(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i + j] = r.get(i + j, Fr(0)) + a * b
    return P(r)


def pneg_arg(p):
    """p(-t)."""
    return P({k: (c if k % 2 == 0 else -c) for k, c in p.items()})


def pderiv(p):
    return P({k - 1: k * c for k, c in p.items() if k > 0})


def pdeg(p):
    return max(p.keys()) if p else -1


def haar(p):
    """Integral of p(t) dt/2 over [-1, 1]: t = p.q under Haar-uniform relative orientation."""
    return sum((c / (k + 1) for k, c in p.items() if k % 2 == 0), Fr(0))


def even_quadratic_min_on_unit_interval(p):
    """Exact minimum on [-1, 1] of a + b t^2 (asserts that shape)."""
    assert set(p.keys()) <= {0, 2}, p
    a, b = p.get(0, Fr(0)), p.get(2, Fr(0))
    return min(a, a + b)


ONE = P({0: 1})
T = P({1: 1})
BORN = P({0: Fr(1, 2), 1: Fr(1, 2)})                 # (1 + t)/2
CUBIC = P({0: Fr(1, 2), 3: Fr(1, 2)})                # (1 + t^3)/2
EPS = Fr(1, 8)


def mono_witness(eps):
    return padd(BORN, pscl(eps, P({1: 1, 3: -1})))   # (1 + t)/2 + eps t (1 - t^2)


MONO = mono_witness(EPS)
WITNESSES = (("Born", BORN), ("cubic", CUBIC), ("mono", MONO))


def signed_stat(f):
    """2 f(t) - 1: the conditional signed record statistic E[s.q | t] / t on {p, -p}."""
    return padd(pscl(2, f), pscl(-1, ONE))


def corr_poly(f, k=1):
    """t^k (2 f(t) - 1): E[(s.q)^k | t] on the antipodal menu {p, -p} for odd k."""
    return pmul(P({k: 1}), signed_stat(f))


# ---------------------------------------------------------------- configurations and actions
def act_soldered(g, cfg):
    """One rotation moves neighbour positions and recorded values together."""
    return {mv(g, pos): mv(g, rec) for pos, rec in cfg.items()}


def act_unsoldered(g_lat, r_int, cfg):
    """A lattice rotation moves positions; an independent internal rotation moves values."""
    return {mv(g_lat, pos): mv(r_int, rec) for pos, rec in cfg.items()}


def soldered_fixers(cfg, G):
    return [g for g in G if act_soldered(g, cfg) == cfg]


def forces_fair_coin(fixers, q):
    """Some configuration-fixing symmetry sends q to -q, hence w(q) = w(-q)."""
    return any(mv(g, q) == neg(q) for g in fixers)


def orbits_on_pairs(points, G, key):
    """Orbits of G on ordered pairs of points, reported as {key(pair): orbit sizes}."""
    pts = list(points)
    seen = set()
    out = {}
    for a in pts:
        for b in pts:
            if (a, b) in seen:
                continue
            orb = set()
            stack = [(a, b)]
            while stack:
                x, y = stack.pop()
                if (x, y) in orb:
                    continue
                orb.add((x, y))
                for g in G:
                    stack.append((mv(g, x), mv(g, y)))
            seen |= orb
            out.setdefault(key(a, b), []).append(len(orb))
    return out


# ================================================================ section 1: census helpers
def rodrigues(q, c=Fr(3, 5), s=Fr(4, 5)):
    """Rational rotation about the rational unit vector q with cos = c, sin = s (3-4-5)."""
    assert dot(q, q) == 1 and c * c + s * s == 1
    K = Mx([[0, -q[2], q[1]], [q[2], 0, -q[0]], [-q[1], q[0], 0]])
    return tuple(tuple(c * I3[i][j] + s * K[i][j] + (1 - c) * q[i] * q[j] for j in range(3)) for i in range(3))


def orbit(v, G):
    return frozenset(mv(g, v) for g in G)


def orbits(points, G):
    out, seen = [], set()
    for p in points:
        if p in seen:
            continue
        o = orbit(p, G)
        seen |= o
        out.append(o)
    return out


def cfg_key(c):
    return frozenset(c.items())


def cfg_orbit_reps(cfgs, G, act):
    reps, seen = [], set()
    for c in cfgs:
        if cfg_key(c) in seen:
            continue
        imgs = {cfg_key(act(g, c)) for g in G}
        seen |= imgs
        reps.append((c, len(imgs)))
    return reps


def free_params_soldered(cfgs, alphabet, G):
    """Free weights of an O-covariant law w(p | cfg) on a finite alphabet, after
    normalisation: sum over configuration orbits of (#stabiliser orbits on the alphabet - 1)."""
    total, rows = 0, []
    for c, osize in cfg_orbit_reps(cfgs, G, act_soldered):
        stab = soldered_fixers(c, G)
        n = len(orbits(alphabet, stab))
        rows.append((osize, len(stab), n))
        total += n - 1
    return total, rows


def free_params_by_pairs(cfgs, alphabet, G):
    """Independent recount: #O-orbits on (cfg, p) pairs minus #O-orbits on cfgs."""
    pair_seen, npairs = set(), 0
    for c in cfgs:
        for p in alphabet:
            k = (cfg_key(c), p)
            if k in pair_seen:
                continue
            imgs = {(cfg_key(act_soldered(g, c)), mv(g, p)) for g in G}
            pair_seen |= imgs
            npairs += 1
    return npairs - len(cfg_orbit_reps(cfgs, G, act_soldered))


def moving_rotation(F):
    """A rational SO(3) element g with g F != F, for a finite nonempty set of directions F."""
    F = frozenset(F)
    for q in F:
        for axis in (EZ, EX):
            if cross(q, axis) == (0, 0, 0):
                continue
            R = rodrigues(axis)
            Rk = R
            for _ in range(3 * len(F) + 3):
                if mv(Rk, q) not in F:
                    return Rk
                Rk = mm(Rk, R)
    return None


O = cubic_group()
RX180 = rot180(EX)
RY180 = rot180(EY)
BISECTOR_XZ = Mx([[0, 0, 1], [0, -1, 0], [1, 0, 0]])   # 180 degrees about (1,0,1): (x,y,z) -> (z,-y,x)
P35 = add(scl(Fr(3, 5), Q_GEN), scl(Fr(4, 5), U_GEN))  # unit, at inner product 3/5 with Q_GEN

print("== 1. Stabiliser-degenerate covariant supports: census ==")
check("cubic group O: 24 exact proper rotations; bisector swap and axis flips lie in O",
      len(O) == 24 and all(is_rot(g) for g in O) and all(g in O for g in (RX180, RY180, BISECTOR_XZ)))
check("rational data: Q_GEN, U_GEN, P35 unit; U_GEN orthogonal to Q_GEN; P35.Q_GEN = 3/5",
      dot(Q_GEN, Q_GEN) == 1 and dot(U_GEN, U_GEN) == 1 and dot(P35, P35) == 1
      and dot(Q_GEN, U_GEN) == 0 and dot(P35, Q_GEN) == Fr(3, 5))

# (a) no recorded neighbour: q = 0, the stabiliser is everything
cube_orbits = {6: orbit(EZ, O), 8: orbit(V(1, 1, 1), O), 12: orbit(V(1, 1, 0), O), 24: orbit(V(1, 2, 3), O)}
check("(a) soldered, no neighbour: O-orbit menus of sizes 6, 8, 12, 24 with stabilisers 4, 3, 2, 1",
      all(len(cube_orbits[k]) == k for k in cube_orbits)
      and [len([g for g in O if mv(g, r) == r]) for r in (EZ, V(1, 1, 1), V(1, 1, 0), V(1, 2, 3))] == [4, 3, 2, 1])
moved = {k: moving_rotation(F) for k, F in cube_orbits.items()}
check("(a) unsoldered, no neighbour: every cube-orbit menu is moved by a rational SO(3) element",
      all(g is not None and is_rot(g) and frozenset(mv(g, x) for x in F) != F
          for (k, F), g in zip(cube_orbits.items(), moved.values())),
      "no finite nonempty subset of S^2 is SO(3)-invariant")

# (b) one recorded neighbour q: stabiliser SO(2)_q
def mpow(A, k):
    R = I3
    for _ in range(k):
        R = mm(R, A)
    return R

RQ = rodrigues(Q_GEN)
check("(b) R_q: exact rotation fixing q, powers 1 through 24 are nonidentity (infinite order proved in note)",
      is_rot(RQ) and mv(RQ, Q_GEN) == Q_GEN and all(mpow(RQ, k) != I3 for k in range(1, 25)))


# ---------------------------------------------------------------- chunk 3 helpers
def rot180_any(n):
    """180-degree rotation about the direction of a nonzero rational vector n:
    2 n n^T / (n.n) - I.  Rational for every rational n; no unit normalisation."""
    nn = dot(n, n)
    assert nn != 0
    return tuple(tuple(2 * n[i] * n[j] / nn - (1 if i == j else 0) for j in range(3)) for i in range(3))


def perp_partner(q):
    """Rational unit vector orthogonal to the rational unit q (q != -e_z):
    the image of e_x under the 180-degree rotation about e_z + q, which swaps e_z and q."""
    return mv(rot180_any(add(EZ, q)), EX)


def anti_cfg(q):
    return {EZ: q, neg(EZ): neg(q)}


def rows_hist(rows):
    """Compact multiset print of census rows (orbit size, stabiliser order, alphabet orbits)."""
    out = {}
    for r in rows:
        out[r] = out.get(r, 0) + 1
    return " ".join(str(k) + "x" + str(v) for k, v in sorted(out.items()))


LATS = []
for n in range(1, 9):
    t_n = Fr(n * n - 1, n * n + 1)
    r_n = Fr(2 * n, n * n + 1)
    LATS.append((t_n, r_n, add(scl(t_n, Q_GEN), scl(r_n, U_GEN))))

check("(b) latitudes t_n = (n^2-1)/(n^2+1), n = 1..8: p_n unit, p_n.q = t_n, strictly increasing",
      all(dot(p, p) == 1 and dot(p, Q_GEN) == t for t, r, p in LATS)
      and all(LATS[i][0] < LATS[i + 1][0] for i in range(7)))
check("(b) transverse radius^2 = 1 - t_n^2 = (2n/(n^2+1))^2 strictly decreasing over the eight tested latitudes",
      all(1 - t * t == r * r for t, r, p in LATS) and all(LATS[i][1] > LATS[i + 1][1] for i in range(7)))
imgs_b = [LATS[0][2]]
for _ in range(24):
    imgs_b.append(mv(RQ, imgs_b[-1]))
check("(b) R_q preserves every latitude; the R_q-orbit of the equator point p_1 = U_GEN exceeds 24 points",
      all(dot(mv(RQ, p), Q_GEN) == t for t, r, p in LATS) and len(set(imgs_b)) == 25,
      "finite invariant menus stay inside {q, -q}")

print()
print("-- (c) the antiparallel ordered pair {+z: q, -z: -q} --")
ANTI_SAMPLES = ((Q_GEN, U_GEN), (Q_XZ, N_XZ), (Q_XY, U_GEN), (Q_DIAG, V(Fr(2, 3), Fr(-1, 3), Fr(-2, 3))))
check("(c) unsoldered: (RX180, rot180(u)) with u orthogonal to q fixes the pair and flips q -> -q, all 4 sampled q",
      all(dot(q, u) == 0 and dot(u, u) == 1 and mv(rot180(u), q) == neg(q)
          and act_unsoldered(RX180, rot180(u), anti_cfg(q)) == anti_cfg(q) for q, u in ANTI_SAMPLES),
      "covariance alone forces w(q) = w(-q) = 1/2; no slot-symmetry assumption enters")
check("(c) unsoldered: a perpendicular partner exists for every rational unit q != -e_z: u = rot180(e_z + q) e_x",
      all(dot(perp_partner(q), perp_partner(q)) == 1 and dot(perp_partner(q), q) == 0
          and mv(rot180_any(add(EZ, q)), EZ) == q for q, u in ANTI_SAMPLES))
check("(c) unsoldered: (I, R_q) also fixes the antiparallel pair, so the stabiliser exceeds the flip Z2",
      act_unsoldered(I3, RQ, anti_cfg(Q_GEN)) == anti_cfg(Q_GEN))
RD_MINUS = Mx([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])   # 180 degrees about (1,-1,0): (x,y,z) -> (-y,-x,-z)
RD_PLUS = rot180_any(V(1, 1, 0))                      # 180 degrees about (1,1,0):  (x,y,z) -> (y,x,-z)
crit_ok = True
for q in (Q_XZ, Q_DIAG, Q_XY, Q_GEN, Q_BIS):
    forced = forces_fair_coin(soldered_fixers(anti_cfg(q), O), q)
    crit_ok = crit_ok and (forced == (q[0] * q[1] * (q[0] * q[0] - q[1] * q[1]) == 0))
check("(c) soldered: exactly 4 cubic rotations invert e_z; fair coin forced iff q_x q_y (q_x^2 - q_y^2) = 0",
      set(g for g in O if mv(g, EZ) == neg(EZ)) == {RX180, RY180, RD_PLUS, RD_MINUS} and crit_ok,
      "orthogonal to one of x, y, (1,1,0), (1,-1,0); 5 sampled q agree")
check("(c) soldered detail: Q_XZ forced by RY180, Q_DIAG by (x,y,z) -> (-y,-x,-z); Q_XY, Q_GEN have fixers {I}",
      RY180 in soldered_fixers(anti_cfg(Q_XZ), O) and mv(RY180, Q_XZ) == neg(Q_XZ)
      and RD_MINUS in soldered_fixers(anti_cfg(Q_DIAG), O) and mv(RD_MINUS, Q_DIAG) == neg(Q_DIAG)
      and len(soldered_fixers(anti_cfg(Q_XY), O)) == 1 and len(soldered_fixers(anti_cfg(Q_GEN), O)) == 1)
check("(c) product rule on the antipodal menu: f(1) f(-1) = 0 for all 3 witnesses; symmetrised sum rule gives 1/2",
      all(pev(f, 1) * pev(f, -1) == 0 and padd(f, pneg_arg(f)) == ONE for name, f in WITNESSES),
      "zero product mass at both menu points: a graded zero, not a law")

print()
print("-- (d) the parallel pair {+z: q, -z: q} --")
par_cfg = {EZ: Q_GEN, neg(EZ): Q_GEN}
check("(d) unsoldered: (RX180, I) and (I, R_q) fix the parallel pair; (RX180, rot180(u)) does not",
      act_unsoldered(RX180, I3, par_cfg) == par_cfg and act_unsoldered(I3, RQ, par_cfg) == par_cfg
      and act_unsoldered(RX180, rot180(U_GEN), par_cfg) != par_cfg,
      "no fixer flips q: nothing beyond the one-neighbour constraint")

print()
print("-- (e) triples: the cross-product lemma and frame attachment --")
PAIRS_E = ((Q_GEN, U_GEN), (EX, EY), (Q_XZ, Q_XY), (Q_DIAG, Q_BIS))
check("(e) cross-product equivariance g(a x b) = (ga) x (gb): all 24 of O plus R_q and R_z(3/5), 4 vector pairs",
      all(mv(g, cross(a, b)) == cross(mv(g, a), mv(g, b)) for g in list(O) + [RQ, RZ345] for a, b in PAIRS_E))
check("(e) frame lemma: det(frame(q1, q2, q1 x q2)) != 0 for (Q_GEN, U_GEN) and (Q_GEN, P35); only I fixes both q1, q2",
      det(frame(Q_GEN, U_GEN, cross(Q_GEN, U_GEN))) != 0 and det(frame(Q_GEN, P35, cross(Q_GEN, P35))) != 0
      and [g for g in list(O) + [RQ, RZ345] if mv(g, Q_GEN) == Q_GEN and mv(g, U_GEN) == U_GEN] == [I3],
      "two non-collinear fixed values force the identity")
tri_orth = {EZ: Q_GEN, neg(EZ): neg(Q_GEN), EX: U_GEN}
check("(e) antiparallel pair + orthogonal third at +x: (RX180, rot180(u)) still fixes the triple: the flip Z2 survives",
      act_unsoldered(RX180, rot180(U_GEN), tri_orth) == tri_orth,
      "fair coin on {q, -q} still forced; the support stays flip-invariant")
V_FORCED = add(scl(Fr(3, 2), Q_GEN), U_GEN)
check("(e) + non-orthogonal third P35: lattice part must be RX180, and the value part would need r u = (3/2) q + u",
      [g for g in O if mv(g, EX) == EX and mv(g, EZ) == neg(EZ)] == [RX180] and dot(V_FORCED, V_FORCED) == Fr(13, 4),
      "13/4 != 1: no rotation flips q while fixing P35")
own_cfg = {EX: EX, EY: EY, EZ: EZ}
fx_own = soldered_fixers(own_cfg, O)
check("(e) soldered own-axis triple {x: x, y: y, z: z}: stabiliser C3 (order 3); six-axis orbits 2, so 1 free parameter",
      len(fx_own) == 3 and all(mpow(g, 3) == I3 for g in fx_own) and len(orbits(SIX_AXES, fx_own)) == 2)

print()
print("-- six-axis free-parameter census (soldered), two independent counts --")
one_cfgs = [{p: v} for p in SIX_AXES for v in SIX_AXES]
tot1, rows1 = free_params_soldered(one_cfgs, SIX_AXES, O)
check("census, one neighbour: 36 configs in orbits 6 + 6 + 24; free parameters 2 + 2 + 5 = 9, both counts agree",
      sorted(o for o, s, n in rows1) == [6, 6, 24] and sorted(n - 1 for o, s, n in rows1) == [2, 2, 5]
      and tot1 == 9 and free_params_by_pairs(one_cfgs, SIX_AXES, O) == 9,
      "rows " + rows_hist(rows1))
opp_cfgs = [{EZ: a, neg(EZ): b} for a in SIX_AXES for b in SIX_AXES]
tot2, rows2 = free_params_soldered(opp_cfgs, SIX_AXES, O)
fx_anti6 = soldered_fixers({EZ: EZ, neg(EZ): neg(EZ)}, O)
check("census, antiparallel aligned pair {+z: e_z, -z: -e_z}: stabiliser D4 (order 8), 2 orbits: 1 free, coin forced",
      len(fx_anti6) == 8 and len(orbits(SIX_AXES, fx_anti6)) == 2 and forces_fair_coin(fx_anti6, EZ))
fx_par6 = soldered_fixers({EZ: EZ, neg(EZ): EZ}, O)
check("census, parallel aligned pair {+z: e_z, -z: e_z}: stabiliser C4 (order 4), 3 orbits: 2 free, no forced coin",
      len(fx_par6) == 4 and len(orbits(SIX_AXES, fx_par6)) == 3 and not forces_fair_coin(fx_par6, EZ))
check("census, opposite pairs: the two independent free-parameter counts agree",
      free_params_by_pairs(opp_cfgs, SIX_AXES, O) == tot2 == 24 and len(rows2) == 9,
      "total " + str(tot2) + " over " + str(len(rows2)) + " config orbits; rows " + rows_hist(rows2))
adj_cfgs = [{EZ: a, EX: b} for a in SIX_AXES for b in SIX_AXES]
tot3, rows3 = free_params_soldered(adj_cfgs, SIX_AXES, O)
check("census, adjacent pairs {+z, +x}: the two independent free-parameter counts agree",
      free_params_by_pairs(adj_cfgs, SIX_AXES, O) == tot3 == 87 and len(rows3) == 21,
      "total " + str(tot3) + " over " + str(len(rows3)) + " config orbits; rows " + rows_hist(rows3))

print()
print("== 2. The antipodal weight class f(p.q) ==")


def habs(p):
    """Integral of |t| p(t) dt/2 over [-1, 1]."""
    return sum((c / (k + 2) for k, c in p.items() if k % 2 == 0), Fr(0))


G_MOVE = mm(frame(Q_GEN, U_GEN, cross(Q_GEN, U_GEN)), tr(frame(EZ, EX, EY)))
P_SRC = V(Fr(4, 5), 0, Fr(3, 5))
check("(2a) transitivity at t = 3/5: a rational rotation carries ((4/5,0,3/5), e_z) to (P35, Q_GEN)",
      is_rot(G_MOVE) and mv(G_MOVE, EZ) == Q_GEN and mv(G_MOVE, P_SRC) == P35,
      "pairs at equal p.q lie on one orbit: the weight is a function of p.q alone")
swap_ok = True
for a in SIX_AXES:
    for b in SIX_AXES:
        if a == b:
            continue
        n_sw = len([g for g in O if mv(g, a) == b and mv(g, b) == a])
        n_st = len([g for g in O if mv(g, a) == a and mv(g, b) == b])
        swap_ok = swap_ok and n_sw == (4 if b == neg(a) else 1) and n_st == (4 if b == neg(a) else 1)
check("(2b) slot exchange is rotational: every ordered position pair is swapped inside O",
      swap_ok, "opposite pairs: 4 swappers, stabiliser C4; adjacent pairs: 1 swapper, trivial stabiliser")
two_cfg = {EZ: Q_GEN, EX: P35}
two_swapped = {EZ: P35, EX: Q_GEN}
check("(2b) unsoldered: (BISECTOR_XZ, I) maps {+z: q, +x: p} to {+z: p, +x: q}: weights are position-blind",
      act_unsoldered(BISECTOR_XZ, I3, two_cfg) == two_swapped)
check("(2b) the value-attached menu {v(+z), -v(+z)} breaks under the swap; the four-point menu survives",
      frozenset((two_swapped[EZ], neg(two_swapped[EZ]))) != frozenset((two_cfg[EZ], neg(two_cfg[EZ])))
      and frozenset(x for v in two_swapped.values() for x in (v, neg(v)))
      == frozenset(x for v in two_cfg.values() for x in (v, neg(v))))
check("(2b) soldered: the swap rotates values: BISECTOR_XZ q = (12/13, -4/13, 3/13) != q: exchange is separate",
      mv(BISECTOR_XZ, Q_GEN) == V(Fr(12, 13), Fr(-4, 13), Fr(3, 13)) and mv(BISECTOR_XZ, Q_GEN) != Q_GEN)
M_K = tuple(tuple(RQ[i][j] - I3[i][j] for j in range(3)) for i in range(3))
minor_ok = any(M_K[i][j] * M_K[k][l] - M_K[i][l] * M_K[k][j] != 0
               for i in range(3) for k in range(3) for j in range(3) for l in range(3) if i < k and j < l)
check("(2c) ker(R_q - I) = span(q): det = 0, some 2x2 minor is nonzero, and (R_q - I) q = 0",
      det(M_K) == 0 and minor_ok and mv(M_K, Q_GEN) == V(0, 0, 0),
      "affinity plus covariance leaves f = (1 + c t)/2")
AFFINE = {c: P({0: Fr(1, 2), 1: Fr(c, 2)}) for c in (Fr(0), Fr(1, 4), Fr(1), Fr(-1))}
check("(2c) the affine family (1 + c t)/2 at c = 0, 1/4, 1, -1: normalised and positive on [-1, 1]",
      all(padd(f, pneg_arg(f)) == ONE and pev(f, 1) >= 0 and pev(f, -1) >= 0 for f in AFFINE.values()))
check("(2c) same-label repeat certainty f(1) = 1 selects c = 1 alone; c = -1 is certain for the flipped label",
      [c for c, f in AFFINE.items() if pev(f, 1) == 1] == [Fr(1)] and pev(AFFINE[Fr(-1)], -1) == 1,
      "the Born coefficient is bought by repeat certainty")
check("(2d) cubic and mono witnesses: derivative nonnegative on [-1, 1], endpoints 0 and 1: monotone, positive",
      pderiv(CUBIC) == P({2: Fr(3, 2)}) and even_quadratic_min_on_unit_interval(pderiv(MONO)) == Fr(1, 4)
      and all(pev(f, -1) == 0 and pev(f, 1) == 1 for f in (CUBIC, MONO)))
check("(2d) affinity fails at t = 1, 0, midpoint: cubic 9/16 and mono 51/64 against the affine value 3/4",
      pev(CUBIC, Fr(1, 2)) == Fr(9, 16) and pev(MONO, Fr(1, 2)) == Fr(51, 64)
      and all((pev(f, 1) + pev(f, 0)) / 2 == Fr(3, 4) for f in (CUBIC, MONO)),
      "affinity is the separating clause")
MIX = padd(pscl(Fr(1, 2), BORN), pscl(Fr(1, 2), CUBIC))
check("(2e) E[s.q] separates the class: Born 1/3, cubic 1/5, mono 11/30, midpoint mixture 4/15",
      {name: haar(corr_poly(f, 1)) for name, f in WITNESSES} == {"Born": Fr(1, 3), "cubic": Fr(1, 5), "mono": Fr(11, 30)}
      and haar(corr_poly(MIX, 1)) == Fr(4, 15),
      "the class is convex")
check("(2e) affine class: E[s.q] = c/3 in [-1/3, 1/3]; the step law 1_{t>0} gives E[s.q] = E|t| = 1/2",
      all(haar(corr_poly(f, 1)) == c / 3 for c, f in AFFINE.items()) and habs(ONE) == Fr(1, 2),
      "Born is neither extremal nor singled out by this statistic")
check("(2e) the second moment is blind: E[(s.q)^2] = 1/3 for every normalised f",
      all(haar(pmul(P({2: 1}), padd(f, pneg_arg(f)))) == Fr(1, 3) for name, f in WITNESSES)
      and haar(P({2: 1})) == Fr(1, 3))
check("(2e) the third moment separates again: E[(s.q)^3] = 1/5 Born, 1/7 cubic, 3/14 mono",
      {name: haar(corr_poly(f, 3)) for name, f in WITNESSES}
      == {"Born": Fr(1, 5), "cubic": Fr(1, 7), "mono": Fr(3, 14)})

print()
print("== 3. Soldered finite alphabets against the continuum ==")
ORB8 = orbit(V(1, 1, 1), O)
ORB12 = orbit(V(1, 1, 0), O)


def tset(w0, F):
    n = dot(w0, w0)
    return frozenset(dot(w0, p) / n for p in F)


def quartic_sum(w):
    return (w[0] ** 4 + w[1] ** 4 + w[2] ** 4) / dot(w, w) ** 2


check("(3) soldered menus quantise t: six axes {0, +-1}; 8-orbit {+-1/3, +-1}; 12-orbit {0, +-1/2, +-1}",
      tset(EZ, SIX_AXES) == frozenset((Fr(-1), Fr(0), Fr(1)))
      and tset(V(1, 1, 1), ORB8) == frozenset((Fr(-1), Fr(-1, 3), Fr(1, 3), Fr(1)))
      and tset(V(1, 1, 0), ORB12) == frozenset((Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1))))
check("(3) invariant p_x^4 + p_y^4 + p_z^4: 1 six axes, 1/3 8-orbit, 1/2 12-orbit; Haar mean 3/5",
      quartic_sum(EZ) == 1 and quartic_sum(V(1, 1, 1)) == Fr(1, 3) and quartic_sum(V(1, 1, 0)) == Fr(1, 2)
      and all(quartic_sum(p) == Fr(1, 3) for p in ORB8) and 3 * haar(P({4: 1})) == Fr(3, 5),
      "matches B1: separates the soldered menus from the continuum")
check("(3) 24-point orbits carry a modulus: (1,2,3) gives 1/2 while (1,2,4) gives 13/21",
      len(orbit(V(1, 2, 3), O)) == 24 and len(orbit(V(1, 2, 4), O)) == 24
      and quartic_sum(V(1, 2, 3)) == Fr(1, 2) and quartic_sum(V(1, 2, 4)) == Fr(13, 21))

print()
print('per_element: Exact finite arithmetic verifies the declared algebraic identities and explicit model comparisons; it does not select physical axioms.')
print('per_site: The supplied finite windows, alphabets and conditional rules fix the scope; other local laws and representations remain unclassified.')
print('per_mode: Analytic statements require the explicit assumptions and proofs in the note; finite sample checks alone do not establish a universal theorem.')
print('per_block: The fresh runner output certifies the implemented finite controls; historical author mutation tables are provenance rather than fresh review evidence.')
print('lattice_wide: No continuum limit, physical field identification, universal law selection or retained audit status is established by this finite certificate.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
