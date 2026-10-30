#!/usr/bin/env python3
"""Field inequality (5.5) on the final map D3 (hard-core--independent, Text 5.1, 5.4).

Map tested. Psi_y(z; x_0) = path(y -> x_0) * Mean_{x in B(y), orders}[ R(x_0, x) R_mu(x, z) ], T_u = Psi_y(u^-) u Psi_{y'}(u^+)^{-1}, M = Mean_u T_u.
x_0 = y if s(y) <= s_rule, otherwise a minimiser of s, with s(x_0) = sum over rule-rough plaquettes in B(y) of min(1, dist(p, x_0)^-2).
Option base=fixed forces x_0 = y, to measure what the rule buys.

PRE-STATED CRITERIA (written before the first run on this map; L=3 and L=5).
  For a coarse 01-plaquette P at corners (0,0), (L,0), (L,L), (0,L), with hull = plaquettes of the blocks of its four corners:
  Ratio(field) = |W(dP) - 1| / ( L^-2 ||f||_{l^1(f > eps)} + ||f||_{l^2(f <= eps)} ), eps = 0.05.
  Families:
    SHEET: thin vortex sheet, as in the first script.
    TUNED: at corner y of P, rotate the first links out of y in directions +e_0, +e_1 by angle theta.
    CHARGE: rotate all eight links out of y by the same angle theta, a pure gauge transformation at y. W(dP) must be unchanged: exact check to 1e-9.
    PATCH: Haar random links on a cube of side r = 1, 2 at a random place in the hull, flat elsewhere (seeded).
    SMOOTH: small random smooth-ish field: each link exp(i A) with A independent of size a = 0.02 (regular, reg term dominates).
  PASS-55: max Ratio <= C_OS_max = 12 sqrt(log L) over all families, for the rule map, at L = 3 and 5.
  FAIL-55: above that. A failure by a factor growing with L falsifies (5.5).
  RULE-EFFECT: report TUNED with base=fixed against base=rule, at theta = pi and at theta near a cancellation. The rule is justified only if fixed is worse or if it shows |m| small.
  ADDED AFTER THE FIRST L=3 RUN, BEFORE ANY RUN OF THIS FAMILY. On a flat exterior the star is an exact common factor, so TUNED gives W = 1 with or
  without the rule and does not test it. TUNED2: rotate by theta = pi the links out of y in directions +-e_0, +-e_1, so that half of all first steps change sign and
  Xi_bar is small, on top of independent noise of size a = 0.02 on every link. RULE-EFFECT: compare |W-1| and Ratio for base=fixed and base=rule, at equal noise.
  The redesign of 5.4 is justified if Ratio(fixed) is much larger than Ratio(rule), or if min|m| is near zero for fixed only. If they agree, the rule buys nothing here, and that gets recorded.
  Flat-background and small-sample limits: this can falsify (5.5) on these families. It cannot confirm it on all fields.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import itertools, math, random, resource, sys

DIM = 4
ONE = (1.0, 0.0, 0.0, 0.0)
EPS_RULE = 0.5
S_RULE = 0.25


def check_rss():
    gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3
    if gb > 2.0:
        sys.exit(f"RSS {gb:.2f} GB above limit")


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def qconj(a):
    return (a[0], -a[1], -a[2], -a[3])


def qdist1(a):
    return math.sqrt((a[0] - 1.0) ** 2 + a[1] ** 2 + a[2] ** 2 + a[3] ** 2)


def qnorm(m):
    r = math.sqrt(sum(x * x for x in m))
    return (tuple(x / r for x in m) if r > 1e-12 else ONE), r


def shift(s, mu, d):
    return tuple(s[i] + (d if i == mu else 0) for i in range(DIM))


class Field:
    def __init__(self, get):
        self.get = get

    def step(self, site, mu, sign):
        if sign > 0:
            return self.get(site, mu), shift(site, mu, 1)
        nxt = shift(site, mu, -1)
        return qconj(self.get(nxt, mu)), nxt

    def walk(self, site, moves):
        g = ONE
        for mu, sign in moves:
            q, site = self.step(site, mu, sign)
            if q is not ONE:
                g = qmul(g, q)
        return g, site

    def plaq(self, x, mu, nu):
        g, _ = self.walk(x, [(mu, 1), (nu, 1), (mu, -1), (nu, -1)])
        return g


def axial_moves(a, b, dirs_order):
    moves = []
    for mu in dirs_order:
        d = b[mu] - a[mu]
        moves += [(mu, 1 if d > 0 else -1)] * abs(d)
    return moves


def block_sites(y, L):
    o = (L - 1) // 2
    for t in itertools.product(range(-o, o + 1), repeat=DIM):
        yield tuple(y[i] + t[i] for i in range(DIM))


def rough_plaquettes(field, y, L):
    out = []
    for x in block_sites(y, L):
        for mu in range(DIM):
            for nu in range(mu + 1, DIM):
                xp = shift(x, mu, 1)
                xpn = shift(xp, nu, 1)
                # inside the block only
                if any(max(abs(c[i] - y[i]) for i in range(DIM)) > (L - 1) // 2 for c in (xp, shift(x, nu, 1), xpn)):
                    continue
                if qdist1(field.plaq(x, mu, nu)) > EPS_RULE:
                    out.append(x)
    return out


def base_point(field, y, L, base):
    if base == "fixed":
        return y
    rough = rough_plaquettes(field, y, L)
    if not rough:
        return y

    def s(x0):
        tot = 0.0
        for p in rough:
            d2 = sum((p[i] - x0[i]) ** 2 for i in range(DIM))
            tot += min(1.0, 1.0 / d2) if d2 > 0 else 1.0
        return tot
    if s(y) <= S_RULE:
        return y
    return min(block_sites(y, L), key=lambda x: (s(x), x))


def mean_paths(field, x0, x):
    """Unnormalised average over axial orders of the path from x0 to x."""
    dirs = [i for i in range(DIM) if x[i] != x0[i]]
    if not dirs:
        return ONE
    s = [0.0, 0.0, 0.0, 0.0]
    n = 0
    for order in itertools.permutations(dirs):
        g, _ = field.walk(x0, axial_moves(x0, x, order))
        for i in range(4):
            s[i] += g[i]
        n += 1
    return tuple(c / n for c in s)


def R_mu(field, x, z, mu):
    """Unnormalised average: transverse from x to (z_perp, x_mu) over orders, then straight along mu to z."""
    corner = tuple(z[i] if i != mu else x[i] for i in range(DIM))
    trans = [i for i in range(DIM) if i != mu and corner[i] != x[i]]
    s = [0.0, 0.0, 0.0, 0.0]
    n = 0
    tail, _ = field.walk(corner, axial_moves(corner, z, [mu]))
    for order in (itertools.permutations(trans) if trans else [()]):
        g, _ = field.walk(x, axial_moves(x, corner, order))
        g = qmul(g, tail)
        for i in range(4):
            s[i] += g[i]
        n += 1
    return tuple(c / n for c in s)


def psi(field, y, z, mu, L, base, cache):
    """Psi_y^mu(z). Returns (element, |m|)."""
    key = (y, base)
    if key not in cache:
        x0 = base_point(field, y, L, base)
        star, _ = field.walk(y, axial_moves(y, x0, [i for i in range(DIM) if x0[i] != y[i]])) if x0 != y else (ONE, y)
        cache[key] = (x0, star, {x: mean_paths(field, x0, x) for x in block_sites(y, L)})
    x0, star, S = cache[key]
    m = [0.0, 0.0, 0.0, 0.0]
    cnt = 0
    for x, sx in S.items():
        g = qmul(sx, R_mu(field, x, z, mu))
        for i in range(4):
            m[i] += g[i]
        cnt += 1
    el, r = qnorm(tuple(c / cnt for c in m))
    return qmul(star, el), r


def coarse_link(field, y, mu, L, base, cache):
    o = (L - 1) // 2
    yp = shift(y, mu, L)
    transverse = [i for i in range(DIM) if i != mu]
    m = [0.0, 0.0, 0.0, 0.0]
    n = 0
    rmin = 1.0
    for t in itertools.product(range(-o, o + 1), repeat=DIM - 1):
        base_site = list(y)
        for k, i in enumerate(transverse):
            base_site[i] += t[k]
        um = list(base_site)
        um[mu] += o
        um = tuple(um)
        up = shift(um, mu, 1)
        a, ra = psi(field, y, um, mu, L, base, cache)
        b, rb = psi(field, yp, up, mu, L, base, cache)
        g = qmul(qmul(a, field.get(um, mu)), qconj(b))
        for i in range(4):
            m[i] += g[i]
        n += 1
        rmin = min(rmin, ra, rb)
    el, r = qnorm(tuple(c / n for c in m))
    return el, min(r, rmin)


def plaquette_W(field, L, base):
    cache = {}
    y = (0, 0, 0, 0)
    A, m1 = coarse_link(field, y, 0, L, base, cache)
    B, m2 = coarse_link(field, (L, 0, 0, 0), 1, L, base, cache)
    C, m3 = coarse_link(field, (0, L, 0, 0), 0, L, base, cache)
    D, m4 = coarse_link(field, y, 1, L, base, cache)
    return qdist1(qmul(qmul(qmul(A, B), qconj(C)), qconj(D))), min(m1, m2, m3, m4)


def rhs(field, L, eps=0.05):
    o = (L - 1) // 2
    l1, l2 = 0.0, 0.0
    seen = set()
    for c in ((0, 0, 0, 0), (L, 0, 0, 0), (L, L, 0, 0), (0, L, 0, 0)):
        for x in block_sites(c, L):
            for mu in range(DIM):
                for nu in range(mu + 1, DIM):
                    k = (x, mu, nu)
                    if k in seen:
                        continue
                    seen.add(k)
                    f = qdist1(field.plaq(x, mu, nu))
                    if f > eps:
                        l1 += f
                    else:
                        l2 += f * f
    return l1 / L ** 2 + math.sqrt(l2), l1, math.sqrt(l2)


def rot(theta, axis=1):
    q = [math.cos(theta), 0.0, 0.0, 0.0]
    q[axis] = math.sin(theta)
    return tuple(q)


def links_field(d):
    return Field(lambda s, mu: d.get((s, mu), ONE))


def sheet_field(a, b, q):
    return Field(lambda s, mu: q if (mu == 0 and s[0] == a and s[1] >= b) else ONE)


def haar(rng):
    v = [rng.gauss(0, 1) for _ in range(4)]
    return qnorm(tuple(v))[0]


def report(name, field, L, base, row):
    curv, m = plaquette_W(field, L, base)
    r, l1, l2 = rhs(field, L)
    ratio = curv / r if r > 1e-14 else (0.0 if curv < 1e-12 else float("inf"))
    row.append((name, base, curv, m, l1, l2, ratio))
    print(f"  {name:28s} base={base:5s} |W-1|={curv:.5f} min|m|={m:.3f} l1={l1:.3f} l2={l2:.4f} Ratio={ratio:.3f}", flush=True)
    check_rss()


def run(L, quick):
    o = (L - 1) // 2
    rows = []
    rng = random.Random(20261030 + L)
    y = (0, 0, 0, 0)
    print(f"L={L}: CHARGE, exact check", flush=True)
    for th in (1.0, 3.1):
        q = rot(th)
        d = {}
        for mu in range(DIM):
            d[(y, mu)] = q
            d[(shift(y, mu, -1), mu)] = qconj(q)
        report(f"CHARGE th={th}", links_field(d), L, "rule", rows)
    print(f"L={L}: TUNED", flush=True)
    for th in (math.pi, 2.0, 1.0):
        d = {(y, 0): rot(th), (y, 1): rot(th)}
        for base in ("fixed", "rule"):
            report(f"TUNED th={th:.3f}", links_field(d), L, base, rows)
    print(f"L={L}: TUNED2 on noise", flush=True)
    for a, seed in ((0.02, 1), (0.02, 2), (0.005, 3)):
        for base in ("fixed", "rule"):
            r2 = random.Random(1000 * L + seed)
            noise = {}

            def get2(s, mu, noise=noise, r2=r2, a=a):
                k = (s, mu)
                if k not in noise:
                    g = [r2.gauss(0, 1) * a for _ in range(3)]
                    t = math.sqrt(sum(x * x for x in g))
                    noise[k] = (math.cos(t), *(x * math.sin(t) / t for x in g)) if t > 0 else ONE
                q = noise[k]
                if s == y and mu in (0, 1):
                    return qmul(rot(math.pi), q)
                if mu in (0, 1) and s == shift(y, mu, -1):
                    return qmul(q, qconj(rot(math.pi)))
                return q
            report(f"TUNED2 a={a} seed={seed}", Field(get2), L, base, rows)
    print(f"L={L}: SHEET", flush=True)
    for a, b in ([(1, 2), (0, 1)] if quick else [(1, 2), (0, 1), (o, 1), (L // 2 + 1, o + 1)]):
        for th in (1.0, 3.1):
            report(f"SHEET a={a} b={b} th={th}", sheet_field(a, b, rot(th)), L, "rule", rows)
    print(f"L={L}: PATCH", flush=True)
    for r in (1, 2):
        for trial in range(2 if quick else 4):
            c = tuple(rng.randint(-o, L + o) if i < 2 else rng.randint(-o, o) for i in range(DIM))
            d = {}
            for t in itertools.product(range(r), repeat=DIM):
                s = tuple(c[i] + t[i] for i in range(DIM))
                for mu in range(DIM):
                    d[(s, mu)] = haar(rng)
            report(f"PATCH r={r} at {c}", links_field(d), L, "rule", rows)
    print(f"L={L}: SMOOTH", flush=True)
    a = 0.02
    cache = {}

    def get(s, mu):
        k = (s, mu)
        if k not in cache:
            g = [rng.gauss(0, 1) * a for _ in range(3)]
            t = math.sqrt(sum(x * x for x in g))
            cache[k] = (math.cos(t), *(x * math.sin(t) / t for x in g)) if t > 0 else ONE
        return cache[k]
    report("SMOOTH a=0.02", Field(get), L, "rule", rows)
    worst = max((r for r in rows if r[1] == "rule" and not r[0].startswith("CHARGE")), key=lambda r: r[6])
    bound = 12 * math.sqrt(math.log(L))
    print(f"L={L}: max Ratio (rule) = {worst[6]:.3f} [{worst[0]}], bound 12 sqrt(log L) = {bound:.2f}: {'PASS-55' if worst[6] <= bound else 'FAIL-55'}", flush=True)
    charges = [r[2] for r in rows if r[0].startswith("CHARGE")]
    print(f"L={L}: CHARGE max |W-1| = {max(charges):.2e} ({'PASS' if max(charges) < 1e-9 else 'FAIL'} exact check)", flush=True)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        run(int(arg), quick=int(arg) >= 5)
