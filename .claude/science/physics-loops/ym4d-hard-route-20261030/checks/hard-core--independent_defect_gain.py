#!/usr/bin/env python3
"""Defect gain of the quaternion-mean block average (hard-core--independent, Text 1 and 4.2).

Question. In an otherwise flat level-k field, one link is rotated by angle theta. Its plaquettes have
curvature f = |exp(i theta n.sigma) - 1|, and it touches 2(d-1) = 6 plaquettes, so ||f||_1 = 6 f. By (R7) the
linearised coarse curvature is at most L^-2 ||f||_1. What does the nonlinear map do, at every position?

PRE-STATED CRITERIA (written before the first run).
  G(pos, theta, L) := max over coarse plaquettes P of |W(dP) - 1| / (L^-2 * 6 f).
  PASS-GENERIC: for positions at distance >= 2 from every block centre, max G <= 10 for L = 3, 5, 7 and all theta,
                and max G does not grow from L=5 to L=7 by more than a factor 1.25.
  FAIL-GENERIC: otherwise. That would falsify (4.1) as written at generic positions.
  CENTRE REPORT: for links touching a block centre, report the absolute coarse curvature R(theta, L) = max_P |W(dP)-1|.
                 PASS-CENTRE-LINEAR: R -> <= L^-2 * 6 f * 10 for theta <= 0.1 (the linear statement).
                 CENTRE-RESIDUAL: the value of R at large theta, as a function of L, decides whether (4.1) needs a
                 centre term. No threshold is claimed: this column is what the run measures.
ADDED AFTER THE FIRST L=3 RUN, BEFORE ANY SHEET RUN. A single link has six plaquette fluxes that cancel in the coarse
sum, so it gives curvature of order theta L^-3 and never stresses (4.1). The saturating defect is a thin vortex sheet: rotate
by theta every direction-0 link at x_0 = a with x_1 >= b, with x_2, x_3 over a box much larger than the hull. Then F_01 = theta on the
plaquettes at (a, b) for all (x_2, x_3), which is the same sign across L^2 plaquettes per coarse plaquette.
  S(a, b, theta, L) := |W(dP) - 1| / (L^-2 ||f||_1 over the hull of P), maximised over coarse 01-plaquettes P near the sheet.
  PASS-SHEET: max S <= 10 for L = 3, 5, 7 and does not grow from L=5 to L=7 by more than a factor 1.25.
  FAIL-SHEET: otherwise.
  The linear prediction is |F'| = theta * tri(a) * tri(b) <= theta, with ||f||_1 / L^2 = f * (number of sheet plaquettes in the hull) / L^2.
Only the flat background is tested. This cannot confirm (4.1) on rough backgrounds, only falsify it here.
"""
import itertools, math, os, resource, sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
RSS_LIMIT_GB = 2.0
DIM = 4


def check_rss():
    gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3  # bytes on Darwin
    if gb > RSS_LIMIT_GB:
        sys.exit(f"RSS {gb:.2f} GB above limit")


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def qconj(a):
    return (a[0], -a[1], -a[2], -a[3])


ONE = (1.0, 0.0, 0.0, 0.0)


def qdist1(a):
    """Operator-norm distance of a unit quaternion from 1."""
    return math.sqrt((a[0] - 1.0) ** 2 + a[1] ** 2 + a[2] ** 2 + a[3] ** 2)


def qmean(items):
    s = [0.0, 0.0, 0.0, 0.0]
    for q in items:
        for i in range(4):
            s[i] += q[i]
    n = len(items)
    s = [x / n for x in s]
    r = math.sqrt(sum(x * x for x in s))
    if r < 1e-12:
        return items[0], r
    return tuple(x / r for x in s), r


class Field:
    """Links default to the identity. links[(site, mu)] is the element from site to site + e_mu."""

    def __init__(self, links):
        self.links = links
        self.touched = set(links)

    def step(self, site, mu, sign):
        """Element for one step from site along sign*e_mu; returns (element, new site)."""
        if sign > 0:
            q = self.links.get((site, mu), ONE)
            nxt = tuple(site[i] + (1 if i == mu else 0) for i in range(DIM))
            return q, nxt
        nxt = tuple(site[i] - (1 if i == mu else 0) for i in range(DIM))
        q = self.links.get((nxt, mu), ONE)
        return qconj(q), nxt

    def walk(self, site, moves):
        g = ONE
        for mu, sign in moves:
            q, site = self.step(site, mu, sign)
            if q is not ONE:
                g = qmul(g, q)
        return g, site


def axial_means(field, y, x):
    """P(y, x): quaternion mean over axial orders of axial paths from y to x. Returns element."""
    disp = [x[i] - y[i] for i in range(DIM)]
    dirs = [i for i in range(DIM) if disp[i] != 0]
    if not dirs:
        return ONE
    if not any(True for _ in field.touched):
        return ONE
    items = []
    for order in itertools.permutations(dirs):
        moves = []
        for mu in order:
            moves += [(mu, 1 if disp[mu] > 0 else -1)] * abs(disp[mu])
        g, _ = field.walk(y, moves)
        items.append(g)
    return qmean(items)[0]


def coarse_link(field, y, mu, L):
    """M(V, (y, y + L e_mu)) with the line-averaged prefix and suffix of Text 1.2. Returns (element, |m|)."""
    o = (L - 1) // 2
    yp = tuple(y[i] + (L if i == mu else 0) for i in range(DIM))
    transverse = [i for i in range(DIM) if i != mu]
    Ts = []
    for t in itertools.product(range(-o, o + 1), repeat=DIM - 1):
        base = list(y)
        for k, i in enumerate(transverse):
            base[i] += t[k]
        prefixes, suffixes = [], []
        for s in range(-o, o + 1):
            x = list(base)
            x[mu] += s
            x = tuple(x)
            p = axial_means(field, y, x)
            g, um = field.walk(x, [(mu, 1)] * (o - s))
            prefixes.append(qmul(p, g))
            xp = tuple(x[i] + (L if i == mu else 0) for i in range(DIM))
            up = list(base)
            up[mu] += o + 1
            up = tuple(up)
            g2, _ = field.walk(up, [(mu, 1)] * (L - o - 1 + s))
            p2 = axial_means(field, yp, xp)
            suffixes.append(qmul(g2, qconj(p2)))
        a, _ = qmean(prefixes)
        b, _ = qmean(suffixes)
        um = list(base)
        um[mu] += o
        um = tuple(um)
        u = field.links.get((um, mu), ONE)
        Ts.append(qmul(qmul(a, u), b))
    return qmean(Ts)


def max_coarse_curvature(field, L, centres_mu):
    """Largest |W(dP) - 1| over coarse plaquettes touching the tubes that contain a defect link."""
    best, bestm = 0.0, 1.0
    cache = {}

    active = set(centres_mu)

    def W(y, mu):
        key = (y, mu)
        if key not in cache:
            cache[key] = coarse_link(field, y, mu, L) if key in active else (ONE, 1.0)
        return cache[key]

    for y, mu in centres_mu:
        for nu in range(DIM):
            if nu == mu:
                continue
            for sgn in (+1, -1):
                y1 = y
                y2 = tuple(y[i] + (L if i == mu else 0) for i in range(DIM))
                y3 = tuple(y2[i] + (sgn * L if i == nu else 0) for i in range(DIM))
                y4 = tuple(y[i] + (sgn * L if i == nu else 0) for i in range(DIM))
                a, ma = W(y1, mu)
                if sgn > 0:
                    b, mb = W(y2, nu)
                    bconj = b
                else:
                    b, mb = W(y3, nu)
                    bconj = qconj(b)
                c, mc = W(y4, mu)
                if sgn > 0:
                    d, md = W(y1, nu)
                    dconj = qconj(d)
                else:
                    d, md = W(y4, nu)
                    dconj = d
                g = qmul(qmul(qmul(a, bconj), qconj(c)), dconj)
                best = max(best, qdist1(g))
                bestm = min(bestm, ma, mb, mc, md)
    return best, bestm


def in_block(site, y, L):
    o = (L - 1) // 2
    return all(abs(site[i] - y[i]) <= o for i in range(DIM))


def tubes_and_blocks(site, mu0, L):
    """Exactly the coarse bonds whose two blocks contain both ends of the defect link."""
    end = tuple(site[i] + (1 if i == mu0 else 0) for i in range(DIM))
    c0 = tuple(round(site[i] / L) * L for i in range(DIM))
    bonds = set()
    for shift in itertools.product((-1, 0, 1), repeat=DIM):
        y = tuple(c0[i] + shift[i] * L for i in range(DIM))
        for mu in range(DIM):
            yp = tuple(y[i] + (L if i == mu else 0) for i in range(DIM))
            if (in_block(site, y, L) or in_block(site, yp, L)) and (in_block(end, y, L) or in_block(end, yp, L)):
                bonds.add((y, mu))
    return bonds


def run(L, thetas, positions):
    rows = []
    for pos, mu0 in positions:
        for theta in thetas:
            # rotation about a fixed axis: the abelian direction is the worst case for coherent addition
            defect = (math.cos(theta), math.sin(theta), 0.0, 0.0)
            field = Field({(pos, mu0): defect})
            f = qdist1(defect)
            curv, m = max_coarse_curvature(field, L, tubes_and_blocks(pos, mu0, L))
            rows.append((pos, mu0, theta, curv, curv / (6 * f / L ** 2), m))
            check_rss()
    return rows


def positions_for(L):
    o = (L - 1) // 2
    centre = [((0, 0, 0, 0), 0), ((0, 0, 0, 0), 1), ((-1, 0, 0, 0), 0)]
    generic = []
    # all positions at distance >= 2 from every centre, in a sample that visits the crossing face and block interior
    for s1 in sorted({-o, -1, 1, o} | {2 if o >= 2 else 1}):
        for s2 in sorted({0, 1, o}):
            for mu in (0, 1):
                p = (s1, s2, 1, 0)
                if sum(abs(q) for q in p) >= 2:
                    generic.append((p, mu))
    return centre, generic


class SheetField(Field):
    """Direction-0 links at x_0 = a with x_1 >= b are rotated. Links default to the identity."""

    def __init__(self, a, b, q):
        self.a, self.b, self.q = a, b, q
        self.links = {}
        self.touched = {0}

    def _get(self, site, mu):
        if mu == 0 and site[0] == self.a and site[1] >= self.b:
            return self.q
        return ONE

    def step(self, site, mu, sign):
        if sign > 0:
            q = self._get(site, mu)
            nxt = tuple(site[i] + (1 if i == mu else 0) for i in range(DIM))
            return q, nxt
        nxt = tuple(site[i] - (1 if i == mu else 0) for i in range(DIM))
        return qconj(self._get(nxt, mu)), nxt


def sheet_coarse_link(field, y, mu, L):
    o = (L - 1) // 2
    yp = tuple(y[i] + (L if i == mu else 0) for i in range(DIM))
    transverse = [i for i in range(DIM) if i != mu]
    Ts = []
    for t in itertools.product(range(-o, o + 1), repeat=DIM - 1):
        base = list(y)
        for k, i in enumerate(transverse):
            base[i] += t[k]
        prefixes, suffixes = [], []
        for s in range(-o, o + 1):
            x = list(base)
            x[mu] += s
            x = tuple(x)
            p = axial_means(field, y, x)
            g, _ = field.walk(x, [(mu, 1)] * (o - s))
            prefixes.append(qmul(p, g))
            xp = tuple(x[i] + (L if i == mu else 0) for i in range(DIM))
            up = list(base)
            up[mu] += o + 1
            g2, _ = field.walk(tuple(up), [(mu, 1)] * (o + s))
            p2 = axial_means(field, yp, xp)
            suffixes.append(qmul(g2, qconj(p2)))
        a, _ = qmean(prefixes)
        b, _ = qmean(suffixes)
        um = list(base)
        um[mu] += o
        q, _ = field.step(tuple(um), mu, 1)
        Ts.append(qmul(qmul(a, q), b))
    return qmean(Ts)


def sheet_scan(L, thetas):
    o = (L - 1) // 2
    out = []
    # coarse 01-plaquette at corners (0,0), (L,0), (L,L), (0,L) in the (x_0,x_1) plane, x_2 = x_3 = 0
    for a in sorted({-o, 0, o, L // 2 + 1, L - 1, L}):
        for b in sorted({1 - o, 1, o, o + 1, L}):
            for theta in thetas:
                q = (math.cos(theta), math.sin(theta), 0.0, 0.0)
                field = SheetField(a, b, q)
                c = {}
                def W(y, mu):
                    k = (y, mu)
                    if k not in c:
                        c[k] = sheet_coarse_link(field, y, mu, L)
                    return c[k]
                A, m1 = W((0, 0, 0, 0), 0)
                B, m2 = W((L, 0, 0, 0), 1)
                C, m3 = W((0, L, 0, 0), 0)
                D, m4 = W((0, 0, 0, 0), 1)
                g = qmul(qmul(qmul(A, B), qconj(C)), qconj(D))
                curv = qdist1(g)
                f = qdist1(q)
                # sheet plaquettes in the hull: (x_2, x_3) over the transverse width 3L of the hull in each direction is an overestimate;
                # the weighted count is what enters: the L^2 plaquettes with weight <= L^-2. Use the sharp count L^2.
                l1 = f * L ** 2
                out.append((a, b, theta, curv, curv / (l1 / L ** 2), min(m1, m2, m3, m4)))
                check_rss()
    return out


def main():
    Ls = [int(a) for a in sys.argv[1:] if a != "sheet"] or [3, 5]
    if "sheet" in sys.argv:
        for L in Ls:
            rows = sheet_scan(L, [0.1, 1.0, 2.0, 3.0, 3.1])
            w = max(rows, key=lambda r: r[4])
            print(f"L={L} sheet: max S={w[4]:.3f} at a={w[0]} b={w[1]} theta={w[2]} curv={w[3]:.4f}; min|m|={min(r[5] for r in rows):.3f}", flush=True)
            for th in (0.1, 1.0, 2.0, 3.0, 3.1):
                sub = [r for r in rows if r[2] == th]
                print(f"   theta={th}: max S={max(r[4] for r in sub):.3f} max curv={max(r[3] for r in sub):.4f}", flush=True)
        return
    thetas_small = [0.05, 0.1]
    thetas_all = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.1]
    for L in Ls:
        centre, generic = positions_for(L)
        print(f"L={L}: {len(centre)} centre links, {len(generic)} generic links", flush=True)
        gen = run(L, thetas_all, generic)
        worst = max(gen, key=lambda r: r[4])
        print(f"  generic max G = {worst[4]:.3f} at pos={worst[0]} mu={worst[1]} theta={worst[2]} curv={worst[3]:.4f} min|m|={min(r[5] for r in gen):.3f}", flush=True)
        for th in thetas_all:
            sub = [r for r in gen if r[2] == th]
            print(f"    theta={th}: max G={max(r[4] for r in sub):.3f} max curv={max(r[3] for r in sub):.5f}", flush=True)
        cen = run(L, thetas_small + thetas_all, centre)
        for th in thetas_small + thetas_all:
            sub = [r for r in cen if r[2] == th]
            print(f"  centre theta={th}: max curv R={max(r[3] for r in sub):.5f}  G={max(r[4] for r in sub):.3f}", flush=True)


if __name__ == "__main__":
    main()
