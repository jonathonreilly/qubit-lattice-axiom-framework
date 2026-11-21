#!/usr/bin/env python3
"""Field inequality (5.5) on the final map D3 (hard-core--independent, Text 5.1, 5.4).

Map tested. Psi_y(z; x_0) = path(y -> x_0) * Mean_{x in B(y), orders}[ R(x_0, x) R_mu(x, z) ], T_u = Psi_y(u^-) u Psi_{y'}(u^+)^{-1}, M = Mean_u T_u.
x_0 = y if s(y) <= s_rule, otherwise a minimiser of s, with s(x_0) = sum over rule-rough plaquettes p in B(y) of f_p W_0(p; x_0), W_0 the weight of a star of axial paths (Text 5.4).
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
  ADDED BEFORE THE SEARCH RUN. The rule now uses threshold eps_0 = 0.05 and not 0.5, and s is weighted by f_p with the axial star weight W_0 (Text 5.4). SEARCH: hill climbing on Ratio over link fields at L = 3, restarts from flat, a sheet, a Haar patch, TUNED2.
  Each move changes one link in the hull, to a Haar element or a small rotation, and is kept if Ratio grows. Ratio is computed only when the denominator exceeds 1e-6.
  PASS-SEARCH: best Ratio <= 12 sqrt(log L) = 12.6 at L = 3. FAIL-SEARCH: above it, which would need a larger C_OS, or a counterexample to (5.5). The value of the best Ratio is the output.
  ADDED BEFORE ITS FIRST RUN. COUNTTRAP tests the claim in Text 5.4 that an unweighted count is wrong: in block y, noise of size a just above threshold on all links except near a site x_d, plus a large defect at x_d (links out of x_d in directions +-e_0, +-e_1 rotated by pi).
  The old count rule (base=count: unweighted, isotropic star) should move x_0 next to the defect. CRITERION: TRAP-CONFIRMED if the count rule puts x_0 within distance 1 of x_d and has min|m| below half of that of the weighted rule, or Ratio above twice that of the weighted rule, on at least one of 3 seeds. TRAP-NOT-SHOWN otherwise, and then the claim is reasoned only.
  ADDED BEFORE ITS FIRST RUN. Environment variable HC_EPS sets eps_0 in the rule and in the right side, to test nearer the regime eps_0 L^2 << 1 of Step 5. The same PASS-55 and PASS-SEARCH criteria apply.
  ADDED BEFORE ITS FIRST RUN. SEARCH2: the single-link hill climb never improved on the sheet, so it is weak. SEARCH2 uses coordinated moves: rotate by a random element all links crossing a random box-shaped 3-dimensional face (a sheet of any size and place in the hull), or a random line, or a random 2-dimensional patch of links, or multiply the rotation of the last accepted move by a factor; with restarts from several sheets and from a sheet combined with a Haar patch at a block centre or at a corner of P.
  It maximises Ratio by simulated-annealing acceptance at low temperature. PASS-SEARCH2: best Ratio <= 12 sqrt(log L) = 12.6 at L = 3. FAIL-SEARCH2: above it. The best Ratio and the move type that produced it are the output. A best Ratio above 1 by a clear margin is itself a result, since it measures C_OS from below.
  ADDED BEFORE ITS FIRST RUN. SEARCH2 from a random start stays far below the sheet, so with HC_START=sheet it starts from the sheet of Ratio 1, with temperature HC_T = 0.001, to test whether coordinated moves can raise Ratio above 1. Same PASS-SEARCH2 criterion; the best Ratio is the output.
  Flat-background and small-sample limits: this can falsify (5.5) on these families. It cannot confirm it on all fields.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import itertools, math, random, resource, sys

DIM = 4
ONE = (1.0, 0.0, 0.0, 0.0)
EPS_RULE = float(os.environ.get("HC_EPS", "0.05"))
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
                f = qdist1(field.plaq(x, mu, nu))
                if f > EPS_RULE:
                    out.append((x, mu, nu, f))
    return out


def base_point(field, y, L, base):
    if base == "fixed":
        return y
    rough = rough_plaquettes(field, y, L)
    if not rough:
        return y
    if base == "count":
        def count(x0):
            tot = 0.0
            for p, mu, nu, f in rough:
                d2 = sum((p[i] - x0[i]) ** 2 for i in range(DIM))
                tot += min(1.0, 1.0 / d2) if d2 > 0 else 1.0
            return tot
        if count(y) <= S_RULE:
            return y
        return min(block_sites(y, L), key=lambda x: (count(x), x))

    def s(x0):
        tot = 0.0
        for p, mu, nu, f in rough:
            same = [p[i] == x0[i] for i in range(DIM) if i not in (mu, nu)]
            tot += f * ((1.0 if all(same) else 0.0) + sum(same) / L)
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


def rhs(field, L, eps=None):
    eps = EPS_RULE if eps is None else eps
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


def trap(L):
    o = (L - 1) // 2
    y = (0, 0, 0, 0)
    xd = (o, o, o, o)
    print(f"L={L}: COUNTTRAP eps={EPS_RULE}, x_d={xd}", flush=True)
    rows = []
    best = False
    for seed in (1, 2, 3):
        for a in (1.5 * EPS_RULE,):
            r2 = random.Random(1000 * L + seed)
            noise = {}

            def get(s, mu, a=a, noise=noise, r2=r2):
                k = (s, mu)
                if k not in noise:
                    near = max(abs(s[i] - xd[i]) for i in range(DIM)) <= 1
                    if near or max(abs(s[i]) for i in range(DIM)) > o:
                        noise[k] = ONE
                    else:
                        g = [r2.gauss(0, 1) * a for _ in range(3)]
                        t = math.sqrt(sum(x * x for x in g))
                        noise[k] = (math.cos(t), *(x * math.sin(t) / t for x in g)) if t > 0 else ONE
                q = noise[k]
                if s == xd and mu in (0, 1):
                    return qmul(rot(math.pi), q)
                if mu in (0, 1) and s == shift(xd, mu, -1):
                    return qmul(q, qconj(rot(math.pi)))
                return q
            f = Field(get)
            x_count = base_point(f, y, L, "count")
            x_rule = base_point(f, y, L, "rule")
            dc = max(abs(x_count[i] - xd[i]) for i in range(DIM))
            dr = max(abs(x_rule[i] - xd[i]) for i in range(DIM))
            print(f"  seed={seed} a={a}: x_0(count)={x_count} dist to defect {dc}; x_0(rule)={x_rule} dist {dr}", flush=True)
            c1, m1 = plaquette_W(f, L, "count")
            c2, m2 = plaquette_W(f, L, "rule")
            r, l1, l2 = rhs(f, L)
            print(f"    count: |W-1|={c1:.5f} min|m|={m1:.3f} Ratio={c1 / r:.3f}; rule: |W-1|={c2:.5f} min|m|={m2:.3f} Ratio={c2 / r:.3f}; l1={l1:.3f} l2={l2:.4f}", flush=True)
            if dc <= 1 and (m1 < m2 / 2 or c1 / r > 2 * c2 / r):
                best = True
            check_rss()
    print(f"L={L}: {'TRAP-CONFIRMED' if best else 'TRAP-NOT-SHOWN'}", flush=True)


def search2(L, moves, seed):
    rng = random.Random(seed)
    o = (L - 1) // 2
    lo = [-o, -o, -o, -o]
    hi = [L + o, L + o, o, o]

    def box_sites(fixed_axis):
        ranges = []
        for i in range(DIM):
            if i == fixed_axis:
                v = rng.randint(lo[i], hi[i])
                ranges.append((v, v))
            else:
                a = rng.randint(lo[i], hi[i])
                b = rng.randint(a, hi[i])
                ranges.append((a, b))
        return itertools.product(*[range(a, b + 1) for a, b in ranges])

    def rand_rot(scale):
        g = [rng.gauss(0, scale) for _ in range(3)]
        t = math.sqrt(sum(x * x for x in g))
        return (math.cos(t), *(x * math.sin(t) / t for x in g)) if t > 0 else ONE

    def move():
        kind = rng.choice(("sheet", "sheet", "line", "patch", "link"))
        scale = rng.choice((0.1, 0.3, 1.0, 3.0))
        q = rand_rot(scale)
        new = {}
        if kind == "sheet":
            ax = rng.randrange(DIM)
            for s_ in box_sites(ax):
                new[(s_, ax)] = q
        elif kind == "line":
            ax = rng.randrange(DIM)
            lin = rng.randrange(DIM)
            s0 = [rng.randint(lo[i], hi[i]) for i in range(DIM)]
            for t in range(rng.randint(1, 2 * L)):
                s_ = list(s0)
                s_[lin] += t
                new[(tuple(s_), ax)] = q
        elif kind == "patch":
            ax = rng.randrange(DIM)
            a, b = rng.sample(range(DIM), 2)
            s0 = [rng.randint(lo[i], hi[i]) for i in range(DIM)]
            for t1 in range(rng.randint(1, L)):
                for t2 in range(rng.randint(1, L)):
                    s_ = list(s0)
                    s_[a] += t1
                    s_[b] += t2
                    new[(tuple(s_), ax)] = q
        else:
            s_ = tuple(rng.randint(lo[i], hi[i]) for i in range(DIM))
            new[(s_, rng.randrange(DIM))] = q
        return kind, new

    best_all = (0.0, "none", 0)
    if os.environ.get("HC_START") == "sheet":
        q0 = rot(3.1)
        base = lambda s, mu: q0 if (mu == 0 and s[0] == 1 and s[1] >= 2) else ONE
    else:
        base = lambda s, mu: ONE
    temp = float(os.environ.get("HC_T", "0.02"))
    for restart in range(4):
        d = {}
        cur = 0.0
        # start from one random sheet, or from the base sheet alone
        if os.environ.get("HC_START") != "sheet":
            for _ in range(1 + restart):
                kind, new = move()
                d.update(new)
        cur, _, _ = ratio_of(overlay(base, d), L)
        print(f"  restart {restart}: start Ratio {cur:.4f}", flush=True)
        if cur > best_all[0]:
            best_all = (cur, "start", -1)
        best = cur
        for it in range(moves):
            kind, new = move()
            old = {k: d.get(k) for k in new}
            for k, q in new.items():
                c = d.get(k, base(k[0], k[1]))
                d[k] = qmul(q, c)
            val, _, m = ratio_of(overlay(base, d), L)
            if val >= cur or rng.random() < math.exp(-(cur - val) / temp):
                cur = val
                if val > best:
                    best = val
                if val > best_all[0]:
                    best_all = (val, kind, it)
            else:
                for k, q in old.items():
                    if q is None:
                        del d[k]
                    else:
                        d[k] = q
            if it % 100 == 0:
                print(f"    restart {restart} it={it} cur={cur:.4f} best={best:.4f} links={len(d)}", flush=True)
            check_rss()
        print(f"  end restart {restart}: best {best:.4f}", flush=True)
    bound = 12 * math.sqrt(math.log(L))
    print(f"L={L}: SEARCH2 best Ratio = {best_all[0]:.4f} by move {best_all[1]} at it={best_all[2]}, bound {bound:.2f}: {'PASS-SEARCH2' if best_all[0] <= bound else 'FAIL-SEARCH2'}", flush=True)


def overlay(base, d):
    return Field(lambda s, mu: d.get((s, mu)) if (s, mu) in d else base(s, mu))


def ratio_of(field, L, base="rule"):
    curv, m = plaquette_W(field, L, base)
    r, l1, l2 = rhs(field, L)
    if r < 1e-6:
        return 0.0, curv, m
    return curv / r, curv, m


def search(L, moves, seed):
    rng = random.Random(seed)
    o = (L - 1) // 2
    starts = {
        "flat": lambda s, mu: ONE,
        "sheet": (lambda q: (lambda s, mu: q if (mu == 0 and s[0] == 1 and s[1] >= 2) else ONE))(rot(1.0)),
        "tuned": (lambda q: (lambda s, mu: q if (mu in (0, 1) and (s == (0, 0, 0, 0) or s == shift((0, 0, 0, 0), mu, -1))) else ONE))(rot(math.pi)),
    }
    best_all = (0.0, None)
    for name, base in starts.items():
        d = {}
        cur, _, _ = ratio_of(overlay(base, d), L)
        print(f"  start {name}: Ratio {cur:.4f}", flush=True)
        for it in range(moves):
            s = tuple(rng.randint(-o, L + o) if i < 2 else rng.randint(-o, o) for i in range(DIM))
            mu = rng.randrange(DIM)
            old = d.get((s, mu))
            if rng.random() < 0.5:
                d[(s, mu)] = haar(rng)
            else:
                g = [rng.gauss(0, 0.3) for _ in range(3)]
                t = math.sqrt(sum(x * x for x in g))
                dq = (math.cos(t), *(x * math.sin(t) / t for x in g))
                c = old if old is not None else base(s, mu)
                d[(s, mu)] = qmul(dq, c)
            new, curv, m = ratio_of(overlay(base, d), L)
            if new > cur:
                cur = new
            else:
                if old is None:
                    del d[(s, mu)]
                else:
                    d[(s, mu)] = old
            if it % 50 == 0:
                print(f"    {name} it={it} best={cur:.4f} links={len(d)}", flush=True)
            check_rss()
        print(f"  end {name}: best Ratio {cur:.4f}, changed links {len(d)}", flush=True)
        best_all = max(best_all, (cur, name), key=lambda r: r[0])
    bound = 12 * math.sqrt(math.log(L))
    print(f"L={L}: SEARCH best Ratio = {best_all[0]:.4f} from {best_all[1]}, bound {bound:.2f}: {'PASS-SEARCH' if best_all[0] <= bound else 'FAIL-SEARCH'}", flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "search":
        search(int(sys.argv[2]), int(sys.argv[3]), 20261030)
    elif sys.argv[1] == "search2":
        search2(int(sys.argv[2]), int(sys.argv[3]), 20261031)
    elif sys.argv[1] == "trap":
        trap(int(sys.argv[2]))
    else:
        for arg in sys.argv[1:]:
            run(int(arg), quick=int(arg) >= 5)
