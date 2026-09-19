#!/usr/bin/env python3
"""causal-clauses, attempt 1 (worker w-macbookpro90c72-jc4f8, model claude-opus-5).

Level-ordered windows of Z^3, six-axis menu, product rule (p, q, r).  mu_D is the
product of the rule's kernels given in-window parents.  (a) readiness-gated clocks,
history-dependent orders and antichain units all give mu_D; (b) the block 14/15/24
clause candidates against mu_D on the smallest windows; (c) the unrecorded-site
clause under causality; (d) the open items, measured.  Exact Fractions throughout.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product

RULES = [(3, 1, 2), (5, 2, 4), (2, 1, 2)]
R0 = RULES[0]
AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
IDX = {d: i for i, d in enumerate(AX)}
S0 = (1, 1, 1)
PASSES = FAILS = 0


class Stall(Exception):
    pass


def check(tag, ok, msg):
    global PASSES, FAILS
    PASSES += bool(ok)
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


def add(x, d):
    return tuple(a + b for a, b in zip(x, d))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def parents(x, s):
    return [tuple(x[c] - (s[k] if c == k else 0) for c in range(3)) for k in range(3)]


def phi(a, b, pqr):
    return pqr[0] if a == b else (pqr[1] if a == b ^ 1 else pqr[2])


_K = {}


def kernel(pv, pqr):
    """The rule's kernel: r(a | parent values) proportional to prod phi(u, a); uniform for no parent."""
    key = (tuple(sorted(pv)), pqr)
    if key not in _K:
        w = [1] * 6
        for a in range(6):
            for u in pv:
                w[a] *= phi(u, a, pqr)
        _K[key] = [F(x, sum(w)) for x in w]
    return _K[key]


class Win:
    def __init__(self, sites, s=S0):
        self.sites = [tuple(x) for x in sites]
        self.n = len(self.sites)
        pos = {x: i for i, x in enumerate(self.sites)}
        self.adj = [[pos[add(x, d)] for d in AX if add(x, d) in pos] for x in self.sites]
        self.bonds = [(i, j) for i in range(self.n) for j in self.adj[i] if i < j]
        self.pa = [[pos[y] for y in parents(x, s) if y in pos] for x in self.sites]


class Graph:  # an abstract graph, for block 24's Q4(a) witness
    def __init__(self, n, bonds):
        self.n, self.bonds = n, bonds


def mu_D(w, pqr):
    out = {}
    for v in product(range(6), repeat=w.n):
        pr = F(1)
        for i in range(w.n):
            pr *= kernel([v[j] for j in w.pa[i]], pqr)[v[i]]
        out[v] = pr
    return out


def static(w, pqr):
    wt = {}
    for v in product(range(6), repeat=w.n):
        x = 1
        for i, j in w.bonds:
            x *= phi(v[i], v[j], pqr)
        wt[v] = x
    z = sum(wt.values())
    return {v: F(x, z) for v, x in wt.items()}


def tv(a, b):
    return sum((abs(a.get(k, 0) - b.get(k, 0)) for k in set(a) | set(b)), F(0)) / 2


def marg(law, keep):
    out = {}
    for v, pr in law.items():
        k = tuple(v[i] for i in keep)
        out[k] = out.get(k, F(0)) + pr
    return out


def marg_elim(w, pqr, keep):
    """The marginal of mu_D on keep by exact variable elimination (the 8-site cube is too big to enumerate)."""
    facs = []
    for i in range(w.n):
        sc = tuple(w.pa[i]) + (i,)
        facs.append((sc, {v: kernel(list(v[:-1]), pqr)[v[-1]] for v in product(range(6), repeat=len(sc))}))
    for e in [i for i in range(w.n) if i not in keep]:
        inv = [f for f in facs if e in f[0]]
        sc = tuple(sorted(set().union(*(set(f[0]) for f in inv)) - {e}))
        t = {}
        for v in product(range(6), repeat=len(sc)):
            asg = dict(zip(sc, v))
            tot = F(0)
            for a in range(6):
                asg[e] = a
                p = F(1)
                for fs, ft in inv:
                    p *= ft[tuple(asg[k] for k in fs)]
                tot += p
            t[v] = tot
        facs = [f for f in facs if e not in f[0]] + [(sc, t)]
    out = {}
    for v in product(range(6), repeat=len(keep)):
        asg = dict(zip(keep, v))
        p = F(1)
        for fs, ft in facs:
            p *= ft[tuple(asg[k] for k in fs)]
        out[v] = p
    return out


def joint(w, U, mask, vals, pqr):
    """Joint formation of U: bonds inside U and bonds to recorded outside neighbours."""
    inner = [(i, j) for i, j in w.bonds if i in U and j in U]
    outer = [(i, vals[j]) for i in U for j in w.adj[i] if j not in U and mask >> j & 1]
    wt = {}
    for uv in product(range(6), repeat=len(U)):
        val = dict(zip(U, uv))
        x = 1
        for i, j in inner:
            x *= phi(val[i], val[j], pqr)
        for i, b in outer:
            x *= phi(val[i], b, pqr)
        wt[uv] = x
    z = sum(wt.values())
    return {uv: F(x, z) for uv, x in wt.items()}


def fixed_units(w, pqr, seq):
    """Units formed in a fixed sequence (singletons = a sequential order)."""
    layer = {(0, (-1,) * w.n): F(1)}
    for U in seq:
        nxt = {}
        for (mask, vals), pr in layer.items():
            for uv, q in joint(w, U, mask, vals, pqr).items():
                nv = list(vals)
                for i, a in zip(U, uv):
                    nv[i] = a
                key = (mask | sum(1 << i for i in U), tuple(nv))
                nxt[key] = nxt.get(key, F(0)) + pr * q
        layer = nxt
    return {v: pr for (m, v), pr in layer.items()}


def ordered_partitions(xs):
    """Every sequence of disjoint nonempty units covering xs (13 for three sites)."""
    if not xs:
        yield []
        return
    for k in range(1, len(xs) + 1):
        for U in combinations(xs, k):
            for tail in ordered_partitions([x for x in xs if x not in U]):
                yield [U] + tail


def is_causal(w, seq):
    """Every site's in-window parents lie in strictly earlier units."""
    done = set()
    for U in seq:
        if any(p not in done for i in U for p in w.pa[i]):
            return False
        done |= set(U)
    return True


def reform(w, law, i, pqr):
    """Re-form site i from the rule given all its neighbours' records (heat bath)."""
    out = {}
    for v, pr in law.items():
        k = kernel([v[j] for j in w.adj[i]], pqr)
        for a in range(6):
            u = v[:i] + (a,) + v[i + 1:]
            out[u] = out.get(u, F(0)) + pr * k[a]
    return out


def nrec(w, i, mask):
    return [j for j in w.adj[i] if mask >> j & 1]


def clocks(w, pqr, rate, gate=False, post=False):
    """Memoryless clocks: the next site is x w.p. rate / total; x records from the kernel given
    its recorded neighbours.  gate: only ready sites (in-window parents recorded) run.
    post: block-14 clocks conditioned on the realized order being causal.  Returns (law, P(causal order))."""
    layer = {(0, (-1,) * w.n): F(1)}
    for _ in range(w.n):
        nxt = {}
        for (mask, vals), pr in layer.items():
            free = [i for i in range(w.n) if not mask >> i & 1]
            ready = {i for i in free if all(mask >> j & 1 for j in w.pa[i])}
            run = [i for i in free if i in ready] if gate else free
            lam = {i: F(rate(w, i, mask, vals)) for i in run}
            tot = sum(lam.values())
            if tot == 0:
                raise Stall
            for i in run:
                if not lam[i] or (post and i not in ready):
                    continue
                rec = nrec(w, i, mask)
                if gate or post:
                    assert sorted(rec) == sorted(w.pa[i])  # N(x) cap S = pa(x) on a down-set
                ker = kernel([vals[j] for j in rec], pqr)
                base = pr * lam[i] / tot
                for a in range(6):
                    key = (mask | 1 << i, vals[:i] + (a,) + vals[i + 1:])
                    nxt[key] = nxt.get(key, F(0)) + base * ker[a]
        layer = nxt
    out = {v: pr for (m, v), pr in layer.items()}
    z = sum(out.values(), F(0))
    if post and z:
        out = {v: pr / z for v, pr in out.items()}
    return out, z


def uniform(w, i, mask, vals):
    return 1


def seeded(w, i, mask, vals):
    return 1 if mask == 0 or nrec(w, i, mask) else 0


def attracting(w, i, mask, vals):
    return 1 + len(nrec(w, i, mask))


def parallel(w, i, mask, vals):
    x = w.sites[i]
    return 1 + any(vals[j] == IDX[sub(x, w.sites[j])] for j in nrec(w, i, mask))


def eps_law(e):
    return lambda w, i, mask, vals: 1 if not nrec(w, i, mask) else e


LAWS = [("uniform", uniform), ("seeded", seeded), ("attracting", attracting), ("parallel", parallel)]


def hsh(*xs):
    h = 1469598103934665603
    for x in xs:
        h = ((h ^ (x & 0xFFFFFFFF)) * 1099511628211) % (1 << 64)
    return h


def rnd_rate(seed):  # any rates: site-, set- and value-dependent, not covariant
    return lambda w, i, mask, vals: 1 + hsh(seed, i, mask, *vals) % 9


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def rot(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


ROT = [M for perm in permutations(range(3)) for sg in product((1, -1), repeat=3)
       for M in [[[sg[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)]] if det3(M) == 1]


def cov_rate(seed):
    """A random rate law covariant under translations and proper rotations: a function of the
    recorded set and its values seen from x, up to rotation."""
    def f(w, i, mask, vals):
        x = w.sites[i]
        loc = [(sub(w.sites[j], x), AX[vals[j]]) for j in range(w.n) if mask >> j & 1]
        canon = min(tuple(sorted((rot(M, d), rot(M, v)) for d, v in loc)) for M in ROT)
        return 1 + hsh(seed, len(loc), *[c for d, v in canon for c in d + v]) % 9
    return f


def flat(hist):
    out = []
    for U, uv in hist:
        out += list(U) + [9] + list(uv) + [8]
    return out


def state_of(w, hist):
    mask, vals = 0, [-1] * w.n
    for U, uv in hist:
        for i, a in zip(U, uv):
            mask |= 1 << i
            vals[i] = a
    return mask, tuple(vals)


def rnd_choose(seed):
    return lambda w, hist, moves: [1 + hsh(seed, *flat(hist), 7, *U) % 9 for U in moves]


def onehot_choose(seed):  # a deterministic, history- and value-dependent order (or unit) rule
    def f(w, hist, moves):
        hs = [hsh(seed, *flat(hist), 7, *U) for U in moves]
        return [int(h == min(hs)) for h in hs]
    return f


def clock_choose(rate):
    def f(w, hist, moves):
        mask, vals = state_of(w, hist)
        return [rate(w, U[0], mask, vals) for U in moves]
    return f


def histories(w, pqr, choose, units=False):
    """Every gated history, with its probability.  A move is one ready site, or (units) any
    non-empty set of ready sites formed jointly; choose(w, hist, moves) gives the weights."""
    full = (1 << w.n) - 1
    layer = {((), 0, (-1,) * w.n): F(1)}
    done = {}
    while layer:
        nxt = {}
        for (hist, mask, vals), pr in layer.items():
            if mask == full:
                done[hist] = pr
                continue
            ready = [i for i in range(w.n) if not mask >> i & 1 and all(mask >> j & 1 for j in w.pa[i])]
            moves = [U for k in range(1, len(ready) + 1 if units else 2) for U in combinations(ready, k)]
            wts = choose(w, hist, moves)
            tot = sum(wts)
            if tot == 0:
                raise Stall
            for U, wt in zip(moves, wts):
                if not wt:
                    continue
                for uv, q in joint(w, U, mask, vals, pqr).items():
                    nv = list(vals)
                    for i, a in zip(U, uv):
                        nv[i] = a
                    key = (hist + ((U, uv),), mask | sum(1 << i for i in U), tuple(nv))
                    nxt[key] = nxt.get(key, F(0)) + pr * F(wt) / tot * q
        layer = nxt
    return done


def hist_law(w, done):
    out = {}
    for hist, pr in done.items():
        v = state_of(w, hist)[1]
        out[v] = out.get(v, F(0)) + pr
    return out


V3 = [(-1, 0, 0), (0, 0, 0), (0, -1, 0)]  # collider: two parents, one child
PLAQ = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
T4 = [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
T5 = T4 + [(1, 0, 0)]
X5 = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
P5 = PLAQ + [(0, 0, 1)]
SLAB = [(x, y, 0) for x in range(2) for y in range(3)]
CLASSES = ["straight", "fork", "collider", "bent"]


def three_windows():
    """The 15 connected 3-site windows with the middle m at the origin (index 1)."""
    out = []
    for d1, d2 in combinations(AX, 2):
        t = sum(d1) + sum(d2)
        cls = "straight" if add(d1, d2) == (0, 0, 0) else ("fork" if t == 2 else ("collider" if t == -2 else "bent"))
        out.append((cls, Win([d1, (0, 0, 0), d2])))
    return out


def sec_a():
    wins = [Win(V3), Win(PLAQ), Win(T4), Win(T5), Win(X5), Win(P5), Win(SLAB), Win(PLAQ, (-1, 1, 1))]
    gated = [uniform, attracting, parallel, eps_law(F(1, 10)), rnd_rate(5), cov_rate(6)]
    n_ok = n_all = 0
    for pqr in RULES:
        for w in wins:
            muD = mu_D(w, pqr)
            for rate in gated:
                n_all += 1
                n_ok += clocks(w, pqr, rate, gate=True)[0] == muD
    check("A1", n_ok == n_all, f"readiness-gated clocks = mu_D exactly: {n_ok}/{n_all} (8 windows, 6 rate laws, 3 rules)")
    n_ok = n_all = 0
    for pqr in RULES:
        for w in wins[:3]:
            muD = mu_D(w, pqr)
            for units in (False, True):
                for ch in (rnd_choose(1), rnd_choose(2), onehot_choose(3), onehot_choose(4)):
                    n_all += 1
                    n_ok += hist_law(w, histories(w, pqr, ch, units)) == muD
    check("A2", n_ok == n_all, f"history/value-dependent random and deterministic orders, antichain units = mu_D: {n_ok}/{n_all}")
    ok = True
    for pqr in RULES:
        for cls, w in three_windows() + [(None, Win(PLAQ)), (None, Win(T4))]:
            muD = mu_D(w, pqr)
            for rate in (uniform, seeded, attracting, eps_law(F(1, 10))):
                law, z = clocks(w, pqr, rate, post=True)
                ok &= z == 0 or law == muD
    bent = Win([(0, 0, 0), (1, 0, 0), (1, 1, 0)])
    k_bent = tv(clocks(bent, R0, parallel, post=True)[0], mu_D(bent, R0))
    k_two = max(tv(clocks(Win([(0, 0, 0), d]), R0, parallel, post=True)[0], mu_D(Win([(0, 0, 0), d]), R0)) for d in AX)
    check("A3", ok and k_bent == F(5, 114) and k_two == 0,
          f"reading K (block-14 clocks conditioned on a causal order): value-blind laws give mu_D; parallel growth on the bent chain TV={k_bent}; 2-site 0")


def sec_b():
    wins = three_windows()
    Vc = Win(V3)
    tpc = [tv(static(Vc, r), mu_D(Vc, r)) for r in RULES]
    check("B0", tpc == [F(1, 72), F(29, 3174), F(5, 726)], "collider: TV(P, C) = 1/72, 29/3174, 5/726 at (3,1,2), (5,2,4), (2,1,2)")
    t0 = tpc[0]
    laws = LAWS + [("eps=1/10", eps_law(F(1, 10)))]
    tab, const = {}, True
    for lname, rate in laws:
        for cls in CLASSES:
            got = {(tv(clocks(w, R0, rate)[0], mu_D(w, R0)), clocks(w, R0, rate, post=True)[1]) for c, w in wins if c == cls}
            const &= len(got) == 1
            tab[lname, cls] = got.pop()
    print("(b) block-14 clocks, 3-site windows, (3,1,2): TV(law, mu_D)|P(causal order)")
    print("  law        " + "".join(f"{c:>15}" for c in CLASSES))
    for lname, _ in laws:
        print(f"  {lname:<11}" + "".join(f"{str(tab[lname, c][0]) + '|' + str(tab[lname, c][1]):>15}" for c in CLASSES))
    exp = {("uniform", "straight"): F(1, 216), ("uniform", "collider"): F(1, 108), ("seeded", "straight"): 0,
           ("seeded", "collider"): t0, ("attracting", "straight"): F(1, 324), ("attracting", "collider"): F(7, 648),
           ("eps=1/10", "collider"): F(13, 2376)}
    check("B1", const and all(tab[k][0] == v for k, v in exp.items()) and all(tab["uniform", c][0] == F(1, 216) for c in ("fork", "bent")),
          "TV constant on each class; uniform 1/216,1/108; seeded 0,1/72; attracting 1/324,7/648; eps collider 13/2376")
    ok = True
    for r, tp in zip(RULES, tpc):
        for lname, rate in laws + [(f"cov{k}", cov_rate(k)) for k in range(1, 7)] + [("eps1/100", eps_law(F(1, 100)))]:
            for cls, w in wins:
                t = tv(clocks(w, r, rate)[0], mu_D(w, r))
                ok &= (tp / 3 <= t <= tp) if cls == "collider" else (t <= 2 * tp / 3)
                if lname == "uniform":
                    ok &= t == (2 * tp / 3 if cls == "collider" else tp / 3)
        ok &= tv(clocks(Vc, r, eps_law(F(1, 100)))[0], mu_D(Vc, r)) == F(103, 303) * tp
    check("B2", ok, "12 covariant clock laws, 15 windows, 3 rules, t = TV(P,C): collider TV in [t/3, t], others <= 2t/3; "
          "uniform: collider 2t/3, others t/3")
    ok, stalls = True, 0
    for d in [d for d in product(range(-2, 3), repeat=3) if 0 < sum(map(abs, d)) <= 2]:
        w = Win([(0, 0, 0), d])
        for lname, rate in laws + [("cov", cov_rate(3)), ("rnd", rnd_rate(4))]:
            try:
                ok &= tv(clocks(w, R0, rate)[0], mu_D(w, R0)) == 0
            except Stall:
                stalls += 1
                ok &= lname == "seeded" and not w.bonds
    for extra in [(3, 0, 0), (0, 2, 0), (1, 1, 1)]:
        w = Win([(0, 0, 0), (1, 0, 0), extra])
        for rate in (rnd_rate(7), cov_rate(8), parallel):
            ok &= tv(clocks(w, R0, rate)[0], mu_D(w, R0)) == 0
    check("B3", ok and stalls == 18, "all 24 two-site windows TV=0 for every law (seeded stalls on the 18 unbonded); bond + far site TV=0")
    ok, n, moved, cnt = True, 0, {c: 0 for c in CLASSES}, {c: 0 for c in CLASSES}
    for r, tp in zip(RULES, tpc):
        for cls, w in wins:
            muD = mu_D(w, r)
            for seq in ordered_partitions([0, 1, 2]):
                n += 1
                t = tv(fixed_units(w, r, seq), muD)
                ok &= t == (tp if (seq[-1] == (1,)) != (cls == "collider") else 0)
                ok &= t == 0 or not is_causal(w, seq)
                if r == R0 and w is next(x for c, x in wins if c == cls):
                    moved[cls] += t > 0
                    cnt[cls] += is_causal(w, seq)
    for d in [d for d in product(range(-2, 3), repeat=3) if 0 < sum(map(abs, d)) <= 2]:
        w = Win([(0, 0, 0), d])
        for seq in ([(0,), (1,)], [(1,), (0,)], [(0, 1)]):
            ok &= tv(fixed_units(w, R0, seq), mu_D(w, R0)) == 0
    ok &= [moved[c] for c in CLASSES] == [3, 3, 10, 3] and [cnt[c] for c in CLASSES] == [1, 3, 3, 1]
    check("B4", ok and n == 585, "block 15, 13 unit sequences x 15 three-site windows x 3 rules: TV(law, mu_D) = TV(P,C) iff "
          "[middle alone last] xor [collider], else 0; moving 3, 3, 10, 3 of 13, none causal; 2-site windows 0")
    pl = Win(PLAQ)
    t_pl = tv(static(pl, R0), mu_D(pl, R0))
    ok = tv(fixed_units(pl, R0, [(0,), (1, 2), (3,)]), mu_D(pl, R0)) == 0 and t_pl == F(455, 31176)
    ok &= fixed_units(pl, R0, [(0, 1, 2, 3)]) == static(pl, R0) and fixed_units(Vc, R0, [(0, 1, 2)]) == static(Vc, R0)
    check("B5", ok, f"a whole window as one unit is the static law; plaquette: level-set units give mu_D, the whole unit TV {t_pl}")
    ok = True
    for r in RULES:
        for w in (Vc, pl):
            st, md = static(w, r), mu_D(w, r)
            ok &= all(reform(w, st, i, r) == st for i in range(w.n)) and any(reform(w, md, i, r) != md for i in range(w.n))
        ok &= reform(Vc, reform(Vc, mu_D(Vc, r), 0, r), 2, r) == static(Vc, r)
    check("B6", ok, "re-forming a site given all its neighbours fixes the static law, not mu_D (collider, "
          "plaquette, 3 rules); re-forming the collider's parents maps mu_D to it")
    return tpc


def etype(W, e, s=S0):
    par = [e in parents(x, s) for x in W]
    chi = [x in parents(e, s) for x in W]
    if all(p or c for p, c in zip(par, chi)):
        return "common parent" if all(par) else ("common child" if all(chi) else "middle of a chain")
    k = 0 if par[0] or chi[0] else 1
    if chi[k]:
        return "child of one"
    if sum(abs(a - b) for a, b in zip(*W)) == 1:
        return "second parent of W's child" if W[1 - k] in parents(W[k], s) else "parent of W's root"
    return "parent of one (W unbonded)"


def sec_c():
    rows, ok_past = {}, True
    for d in [d for d in product(range(-2, 3), repeat=3) if 0 < sum(map(abs, d)) <= 2]:
        W = [(0, 0, 0), d]
        for e in sorted({add(x, a) for x in W for a in AX} - set(W)):
            f = Win(W + [e])
            tc = tv(mu_D(Win(W), R0), marg(mu_D(f, R0), [0, 1]))
            ts = tv(static(Win(W), R0), marg(static(f, R0), [0, 1]))
            ok_past &= tc == 0 or any(e in parents(x, S0) for x in W)
            r = rows.setdefault(etype(W, e), [0, set(), set()])
            r[0] += 1
            r[1].add(tc)
            r[2].add(ts)
    print("(c) |W|=2 (0<|d|_1<=2), E = one adjacent site, 246 pairs, (3,1,2): causal TV, static TV")
    for k, (n, tc, ts) in rows.items():
        print(f"  {k:<27} n={n:<3} {','.join(map(str, sorted(tc))):<7} {','.join(map(str, sorted(ts)))}")
    sp = rows["second parent of W's child"][1]
    check("C1", ok_past and sum(r[0] for r in rows.values()) == 246 and rows["common child"][1] == {0} and rows["common child"][2] == {F(1, 72)}
          and rows["common parent"][1] == rows["middle of a chain"][1] == {F(1, 72)} and len(sp) == 1 and 0 not in sp and rows["second parent of W's child"][2] == {0},
          "causal TV nonzero only for exterior ancestors; common child: static 1/72, causal 0; second parent: static 0, causal nonzero")
    sp_all, dia = [], []
    W = [(0, 0, 0), (1, 0, 0)]
    for r in RULES:
        sp_all.append(tv(mu_D(Win(W), r), marg(mu_D(Win(W + [(1, -1, 0)]), r), [0, 1])))
        dia.append(tv(mu_D(Win(W), r), marg(mu_D(Win(W + [(1, -1, 0), (0, -1, 0)]), r), [0, 1])))
    check("C2", all(t > 0 for t in sp_all) and dia == [0, 0, 0],
          "W = bond (0,0,0)-(1,0,0): second parent (1,-1,0) moves W's law at 3 rules; adding common parent "
          "(0,-1,0) closes a diamond: TV 0")
    ori = list(product((1, -1), repeat=3))
    top = [(0, 0, 1), (1, 0, 1)]
    edge, ok = {}, True
    for s in ori:
        w = Win(PLAQ + top, s)
        m = marg(mu_D(w, R0), range(4))
        ok &= m == marg_elim(w, R0, [0, 1, 2, 3])
        edge[s] = tv(mu_D(Win(PLAQ, s), R0), m)
    e_nz = {edge[s] for s in ori if s[2] == -1 and s[1] == -1}
    check("C3", ok and all(edge[s] == 0 for s in ori if s[2] == 1 or s[1] == 1) and len(e_nz) == 1 and 0 not in e_nz,
          "plaquette + edge above c0,c1, 8 orientations: TV 0 if the edge is future (s3=+1) or closes a "
          "diamond (s2=+1), one nonzero value for s=(+-1,-1,-1); enumeration = elimination")
    face = [add(x, (0, 0, 1)) for x in PLAQ]
    cube = {s: tv(mu_D(Win(PLAQ, s), R0), marg_elim(Win(PLAQ + face, s), R0, [0, 1, 2, 3])) for s in ori}
    c_nz = {cube[s] for s in ori if s[2] == -1}
    cst = cube_static_tv(R0)
    check("C4", all(cube[s] == 0 for s in ori if s[2] == 1) and len(c_nz) == 1 and 0 not in c_nz and cst == F(9778807, 1312253264),
          "cube, W, E = bottom, top face (block 24 Q4(b)): causal TV 0 for the 4 orientations with E future, one "
          "nonzero value for the 4 with E past; static 9778807/1312253264 as in block 24")
    nbr = lambda x: {add(x, d) for d in AX}
    kinds = {}
    for e in sorted(set().union(*(nbr(x) for x in PLAQ)) - set(PLAQ)):
        ch = [x for x in PLAQ if e in parents(x, S0)]
        k = "child" if not ch else ("parent of the root" if ch == [PLAQ[0]] else ("third parent of the sink" if ch == [PLAQ[3]] else "second parent"))
        r = kinds.setdefault(k, [0, set(), set()])
        r[0] += 1
        r[1].add(tv(mu_D(Win(PLAQ), R0), marg(mu_D(Win(PLAQ + [e]), R0), range(4))))
        r[2].add(tv(static(Win(PLAQ), R0), marg(static(Win(PLAQ + [e]), R0), range(4))))
    got = {k: (n, tuple(sorted(c)), tuple(s)) for k, (n, c, s) in kinds.items()}
    check("C5", got == {"child": (8, (0,), (0,)), "parent of the root": (3, (0,), (0,)), "second parent": (4, (sp_all[0],), (0,)),
                        "third parent of the sink": (1, (F(437, 102960),), (0,))},
          "plaquette, 16 one-site exteriors (all pendant, static TV 0): causal TV 0 for 8 children, 3 root parents; "
          "5/1716 for 4 second parents; 437/102960 for the sink's third parent")
    return sp_all, e_nz.pop(), c_nz.pop()


def cube_static_tv(pqr):
    """Block 24 Q4(b): static TV between the free bottom face and its marginal under the unit cube, by the transfer trace."""
    M = [[phi(a, b, pqr) for b in range(6)] for a in range(6)]
    r1, r2 = {}, {}
    for b in product(range(6), repeat=4):  # cycle order (0,0,0), (1,0,0), (1,1,0), (0,1,0); the top face above it
        cyc = 1
        for i in range(4):
            cyc *= phi(b[i], b[(i + 1) % 4], pqr)
        T = [[int(i == j) for j in range(6)] for i in range(6)]
        for i in range(4):
            T = [[sum(T[x][y] * phi(b[i], y, pqr) * M[y][z] for y in range(6)) for z in range(6)] for x in range(6)]
        r1[b], r2[b] = cyc, cyc * sum(T[x][x] for x in range(6))
    z1, z2 = sum(r1.values()), sum(r2.values())
    return tv({k: F(v, z1) for k, v in r1.items()}, {k: F(v, z2) for k, v in r2.items()})


def sec_d(tpc):
    Pset = {tuple(-c for c in (s[0] * (k == 0), s[1] * (k == 1), s[2] * (k == 2))) for k in range(3) for s in [S0]}

    def orient(M):
        img = [rot(M, v) for v in Pset]
        return tuple(-sum(v[k] for v in img) for k in range(3))
    orbit = {orient(M) for M in ROT}
    stab = sum(orient(M) == S0 for M in ROT)
    Rf = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
    flip = tv(mu_D(Win(V3, S0), R0), mu_D(Win(V3, (-1, -1, -1)), R0))
    check("D1", len(ROT) == 24 and len(orbit) == 8 and stab == 3 and det3(Rf) == 1 and orient(Rf) == (-1, -1, -1) and flip == tpc[0],
          "8 orientations, one orbit of the 24 rotations, stabilizer C3; {m-e1,m,m-e2}: collider under s, fork under -s, TV 1/72")
    ok = True
    for sites in (PLAQ, T4, X5, SLAB):
        w = Win(sites)
        md = mu_D(w, R0)
        for v, pr in md.items():
            bw = 1
            for i, j in w.bonds:
                bw *= phi(v[i], v[j], R0)
            npa = 1
            for i in range(w.n):
                npa *= sum(eval_w(v, w.pa[i], a) for a in range(6))
            ok &= pr * npa == bw
    forest = all(mu_D(w, R0) == static(w, R0) for c, w in three_windows() if c != "collider")
    check("D2", ok and forest, "mu_D = prod_bonds phi / prod_x N_pa(x) (plaquette, T4, cross, 2x3 slab); = static on chains and forks")
    mix = []
    for r in RULES:
        z1 = r[0] + r[1] + 4 * r[2]
        w = Win(V3)
        lm = {v: F(1, 36) * F(phi(v[0], v[1], r) + phi(v[2], v[1], r), 2 * z1) for v in product(range(6), repeat=3)}
        mix.append(tv(lm, mu_D(w, r)))
    check("D3", all(m > 0 for m in mix), f"collider, product vs mixture kernel: TV = {', '.join(map(str, mix))}")
    al = []
    for r in RULES + [(40, 1, 1)]:
        best = F(0)
        for B in combinations_with_replacement(range(6), 2):
            for a1, a2 in combinations(range(6), 2):
                ka, kb = kernel(list(B) + [a1], r), kernel(list(B) + [a2], r)
                best = max(best, sum(abs(x - y) for x, y in zip(ka, kb)) / 2)
        al.append(best)
    check("D4", all(3 * a < 1 for a in al[:3]) and 3 * al[3] >= 1,
          f"alpha_3 = {', '.join(map(str, al[:3]))} (3 alpha_3 < 1 at the three rules); at (40,1,1) 3 alpha_3 = {3 * al[3]}")
    pl = Win(PLAQ)
    st = []
    for rate in (uniform, parallel):
        done = histories(pl, R0, clock_choose(rate))
        st.append((hist_law(pl, done) == mu_D(pl, R0), sum(p for h, p in done.items() if h[1][0] == (1,) and h[0][1] == (0,))))
    check("D5", st[0][0] and st[1][0] and (st[0][1], st[1][1]) == (F(1, 12), F(1, 9)),
          "plaquette, gated uniform vs parallel growth: same law mu_D; P(second=(1,0,0), v_0=+e1) = 1/12 vs 1/9")
    return mix, al


def eval_w(v, pa, a):
    x = 1
    for j in pa:
        x *= phi(v[j], a, R0)
    return x


def sec_q4():
    c = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    cyc = [(0, 1), (1, 2), (2, 3), (3, 0)]
    exp = [F(78621, 4563820), F(675203620, 64463986907), F(221667, 30063356)]
    tri = [tv(static(Graph(4, cyc), r), marg(static(Graph(5, cyc + [(0, 4), (1, 4)]), r), range(4))) for r in RULES]
    nbr = lambda x: {add(x, d) for d in AX}
    no_tri = all(not (nbr(x) & nbr(add(x, d))) for x in c for d in AX)
    pend = [e for e in set().union(*(nbr(x) for x in c)) - set(c)]
    pend_ok = all(sum(e in nbr(x) for x in c) == 1 for e in pend) and all(
        tv(static(Win(c), R0), marg(static(Win(c + [e]), R0), range(4))) == 0 for e in pend)
    rep = [tv(static(Win(c), r), marg(static(Win(c + [(0, 0, 1), (1, 0, 1)]), r), range(4))) for r in RULES]
    check("E1", tri == exp and no_tri and len(pend) == 16 and pend_ok and all(t > 0 for t in rep),
          "block 24 Q4(a) values = the triangle graph's; Z^3 has no triangle; 16 one-site exteriors pendant (TV 0)")
    return rep


def main():
    sec_a()
    tpc = sec_b()
    sp_all, edge, cube = sec_c()
    mix, al = sec_d(tpc)
    rep = sec_q4()
    print(f"second parent (causal TV) at the three rules: {', '.join(map(str, sp_all))}")
    print(f"Q4(a) in Z^3, E = edge above c0c1, static TV: {', '.join(map(str, rep))}")
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT a finite check - {FAILS} FAIL tags")
        return 1
    print("HIT: (a) on every finite level-ordered window of Z^3, every readiness-gated, non-stalling formation (clocks of any "
          "rates, history- or value-dependent random or deterministic orders, antichain units) gives the one law "
          "mu_D = prod r(v_x|v_pa(x)) (frozen-order identity); conditioning ungated clocks "
          "on a causal order instead reweights by value-dependent rates (bent chain 5/114)")
    print("HIT: (b) block 14's clocks let a site record before its parents: under every translation-covariant clock law the "
          "collider's law is C + g(P-C) with g(v_a,v_c) in [1/3,1], TV in [TV(P,C)/3, TV(P,C)] (1/72 at (3,1,2)); uniform "
          "rates 1/216, collider 1/108; block 15: each of the 13 unit sequences on a 3-site window gives P, or C if the middle "
          "forms alone after both ends: TV(P,C) iff [middle alone last] xor [collider], else 0 (whole collider as one unit "
          "1/72); 2-site windows 0")
    print(f"HIT: (c) under gating a site unrecorded when W completes is no ancestor of W and drops out exactly (marginal of "
          f"mu_D(W u E) on W = mu_D(W)): summing it = omitting it; static and causal criteria cross: common child static 1/72 "
          f"causal 0, second parent static 0 causal {sp_all[0]}; recorded exterior ancestors move W's law (edge {edge}, cube "
          f"{cube}), except a root's lone parent and a diamond-closing parent")
    print(f"HIT: block 24 Q4(a) witness 78621/4563820 is computed on a triangle (x adjacent to adjacent corners c0,c1), not a "
          f"Z^3 window; in Z^3 every one-site exterior of a plaquette is pendant (static TV 0); two-site replacement {rep[0]}")
    print("SUMMARY: PROVED (a) every readiness-gated, non-stalling rate, order or antichain-unit clause gives mu_D on finite "
          "level-ordered Z^3 windows; (b) block 14's covariant clocks (collider 1/216 to 1/72 at (3,1,2)) and block 15's "
          "sequences with [middle alone last] xor [collider] (1/72) move 3-site laws, never 2-site; (c) settled for unrecorded "
          "sites (they drop out), not for the recorded past; (d) open: gating itself, orientation, multi-parent kernel form, "
          "extent of the past, timing statistics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
