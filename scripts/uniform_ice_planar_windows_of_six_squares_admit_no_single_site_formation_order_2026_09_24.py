#!/usr/bin/env python3
"""Uniform ice by single sites: no induced window of six squares admits a fixed local formation order.

Landed PR 8735 swept the induced vertex/link windows of free polyominoes of one
to five squares, with a plaquette coordinator on every enclosed square, and
found a fixed single-site formation order only for the lone square. Its
boundary names larger windows as untested. This runner applies the same
criterion (landed PR 8715), the same closed-set search with its closure lemma
(landed PR 8719) and the same record weights to every window spanned by a
free hexomino that no smaller polyomino spans. Uniform ice is a supplied
finite model; the results are exact finite computations on the stated
windows with full local records.

Checks:

A. The closed-set search reproduces the plain search on five small windows
   (the check of landed PR 8735, unchanged).
B. Free hexominoes number 35 and span 32 new windows, with 13 or 14 vertices
   and 6 or 7 coordinators; every window's total weight equals an independent
   generating-function coefficient.
C. With full local records and every coordinator, none of the 32 windows
   admits a fixed single-site order; every search finishes within its budget.
D. In every window one recorded maximum-size formed set is a plaquette with
   its four links and its unshared corners, for a square with the fewest
   shared corners, and no site outside it is admissible.

Coarser record schemes, adaptive orders and polyomino generators of seven or more squares
are not tested.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_BY_SINGLE_SITES_NO_PLANAR_WINDOW_OF_SIX_SQUARES_ADMITS_A_LOCAL_FORMATION_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_BY_FORMATION_TWO_PLANAR_SQUARES_ADMIT_NO_LOCAL_ORDER_AND_ONE_CUBE_NEEDS_ITS_CUBE_SITE_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/UNIFORM_ICE_BY_FORMATION_TWO_ADJACENT_CUBES_ADMIT_NO_LOCAL_ORDER_EVEN_WITH_BOTH_CUBE_SITES_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_BY_SINGLE_SITES_NO_PLANAR_WINDOW_OF_TWO_TO_FIVE_SQUARES_ADMITS_A_LOCAL_FORMATION_ORDER_BOUNDED_THEOREM_NOTE_2026-09-23.md')
from math import comb

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def build(V, P, C, scheme=None):
    """Sites, nearest-neighbour sets, record codes, code ranges and weights."""
    Vs = set(V)
    grid = sorted({add(v, d) for v in V for d in DIRS if add(add(v, d), d) in Vs})
    gidx = {l: i for i, l in enumerate(grid)}
    sites = [("V", v) for v in V] + [("L", l) for l in grid] + [("P", p) for p in P] + [("C", c) for c in C]
    n = len(sites)
    nb = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if sum(abs(a - b) for a, b in zip(sites[i][1], sites[j][1])) == 1:
                nb[i].add(j)
                nb[j].add(i)
    own = []
    for t, s in sites:
        if t == "L":
            own.append([gidx[s]])
        elif t in "VP":
            own.append([gidx[add(s, d)] for d in DIRS if add(s, d) in gidx])
        else:
            own.append([gidx[l] for l in grid if max(abs(a - b) for a, b in zip(l, s)) == 1])
    E = len(grid)
    bits = (np.arange(1 << E, dtype=np.int64)[:, None] >> np.arange(E, dtype=np.int64)) & 1
    w = np.ones(1 << E, dtype=np.int64)
    for v in V:
        inc = [gidx[add(v, d)] for d in DIRS if add(v, d) in gidx]
        priv = 6 - len(inc)
        table = np.array([comb(priv, 3 - k) if 0 <= 3 - k <= priv else 0 for k in range(len(inc) + 1)], dtype=np.int64)
        assert int(w.max()) * int(table.max()) < 2**63
        w *= table[bits[:, inc].sum(axis=1)]
    keep = w > 0
    bits, w = bits[keep], w[keep]
    assert sum(map(int, w)) < 2**53 and np.all(w > 0)
    codes, K = [], []
    for (t, _), r in zip(sites, own):
        mode = "pattern" if t == "L" else (scheme or {}).get(t, "pattern")
        if mode == "pattern":
            c = np.zeros(len(w), dtype=np.int64)
            for j, e in enumerate(r):
                c |= bits[:, e] << j
            codes.append(c)
            K.append(1 << len(r))
        elif mode == "count":
            codes.append(bits[:, r].sum(axis=1).astype(np.int64))
            K.append(len(r) + 1)
        else:
            codes.append(np.zeros(len(w), dtype=np.int64))
            K.append(1)
    return {"sites": sites, "nb": nb, "codes": codes, "K": K, "w": w, "own": own}


def dense(keys):
    u, inv = np.unique(keys, return_inverse=True)
    return inv.astype(np.int64).ravel(), len(u)


def group_of(win, idxs):
    g = np.zeros(len(win["w"]), dtype=np.int64)
    for s in sorted(idxs):
        g, _ = dense(g * win["K"][s] + win["codes"][s])
    return g


def is_function(win, y, S, memo):
    """Is y's record a function of the records of the sites in S?"""
    key = (y, S)
    if key not in memo:
        g = group_of(win, S)
        _, G = dense(g)
        _, P = dense(g * win["K"][y] + win["codes"][y])
        memo[key] = P == G
    return memo[key]


def admissible(win, gF, x, S):
    """Does x's conditional given the formed set (groups gF) equal its conditional given S?"""
    wf = win["w"].astype(np.float64)
    cx, Kx = win["codes"][x], win["K"][x]
    h = group_of(win, S)
    _, first, ga = np.unique(gF * Kx + cx, return_index=True, return_inverse=True)
    ga = ga.ravel()
    ha, _ = dense(h * Kx + cx)
    Wga = np.bincount(ga, weights=wf)
    Wg, Wh, Wha = np.bincount(gF, weights=wf), np.bincount(h, weights=wf), np.bincount(ha, weights=wf)
    lhs = Wga * Wh[h[first]]
    rhs = Wha[ha[first]] * Wg[gF[first]]
    if np.any(np.abs(lhs - rhs) > 1e-9 * np.maximum(lhs, rhs)):
        return False
    as_int = lambda a: a.astype(np.int64).astype(object)
    return bool(np.all(as_int(Wga) * as_int(Wh[h[first]]) == as_int(Wha[ha[first]]) * as_int(Wg[gF[first]])))


def formed_neighbours(win, x, F):
    return frozenset(k for k in win["nb"][x] if F >> k & 1)


def closed_search(win, budget):
    """Depth-first search over closed formed sets; (found, states, largest set) or found None at the budget."""
    n, memo, seen, best = len(win["sites"]), {}, set(), [0]

    def close(F):
        changed = True
        while changed:
            changed = False
            for y in range(n):
                if not F >> y & 1 and is_function(win, y, formed_neighbours(win, y, F), memo):
                    F |= 1 << y
                    changed = True
        return F

    def dfs(F, gF):
        F = close(F)
        if bin(F).count("1") > bin(best[0]).count("1"):
            best[0] = F
        if F == (1 << n) - 1:
            return True
        if F in seen:
            return False
        if len(seen) >= budget:
            raise OverflowError
        seen.add(F)
        for x in range(n):
            if not F >> x & 1 and admissible(win, gF, x, formed_neighbours(win, x, F)):
                g2, _ = dense(gF * win["K"][x] + win["codes"][x])
                if dfs(F | (1 << x), g2):
                    return True
        return False

    try:
        found = dfs(0, np.zeros(len(win["w"]), dtype=np.int64))
    except OverflowError:
        return None, len(seen), best[0]
    return found, len(seen), best[0]


def plain_search(win, budget):
    """Breadth-first search over all formed sets (the method of open PR 8715)."""
    n = len(win["sites"])
    seen, frontier = {0}, [0]
    while frontier:
        nxt = []
        for F in frontier:
            gF = group_of(win, [k for k in range(n) if F >> k & 1])
            for x in range(n):
                G = F | (1 << x)
                if F >> x & 1 or G in seen:
                    continue
                if admissible(win, gF, x, formed_neighbours(win, x, F)):
                    seen.add(G)
                    nxt.append(G)
                    if len(seen) > budget:
                        return None, len(seen), None
        frontier = nxt
    return (1 << n) - 1 in seen, len(seen), max(bin(F).count("1") for F in seen)


def generating_weight(U):
    """Coefficient of prod_v x_v^3 in prod_v (1 + x_v)^(6 - deg v) prod_edges (1 + x_u x_v), unit
    coordinates; a vertex's private factor is applied, and its exponent cleared, after its last edge."""
    edges = [(a, b) for a in range(len(U)) for b in range(a + 1, len(U)) if sum(abs(x - y) for x, y in zip(U[a], U[b])) == 1]
    deg = [sum(1 for e in edges if v in e) for v in range(len(U))]
    last = {v: max(i for i, e in enumerate(edges) if v in e) for v in range(len(U))}
    poly = {(0,) * len(U): 1}
    for i, (a, b) in enumerate(edges):
        out = {}
        for e, c in poly.items():
            out[e] = out.get(e, 0) + c
            f = list(e)
            f[a] += 1
            f[b] += 1
            if f[a] <= 3 and f[b] <= 3:
                out[tuple(f)] = out.get(tuple(f), 0) + c
        for v in (a, b):
            if last[v] == i:
                fin = {}
                for e, c in out.items():
                    f = list(e)
                    k, f[v] = f[v], 0
                    fin[tuple(f)] = fin.get(tuple(f), 0) + c * comb(6 - deg[v], 3 - k)
                out = fin
        poly = out
    return len(edges), sum(poly.values())



def canon(cells):
    best = None
    for sx, sy, swap in [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (False, True)]:
        pts = [((y, x) if swap else (x, y)) for x, y in cells]
        pts = [(sx * x, sy * y) for x, y in pts]
        mx, my = min(p[0] for p in pts), min(p[1] for p in pts)
        key = tuple(sorted((x - mx, y - my) for x, y in pts))
        best = key if best is None or key < best else best
    return best


def polyominoes(n):
    out = {1: {canon([(0, 0)])}}
    for k in range(2, n + 1):
        out[k] = {canon(list(P) + [(x + dx, y + dy)]) for P in out[k - 1] for x, y in P
                  for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) not in P}
    return out


def window(cells):
    V = sorted({(2 * (x + a), 2 * (y + b), 0) for x, y in cells for a in (0, 1) for b in (0, 1)})
    Vs = set(V)
    near = {(x + a, y + b) for x, y in cells for a in (-1, 0, 1) for b in (-1, 0, 1)}
    squares = sorted(s for s in near if all((2 * (s[0] + a), 2 * (s[1] + b), 0) in Vs for a in (0, 1) for b in (0, 1)))
    return V, [(2 * x + 1, 2 * y + 1, 0) for x, y in squares]


def square_sites(p):
    corners = {(p[0] + a, p[1] + b, 0) for a in (-1, 1) for b in (-1, 1)}
    links = {(p[0] + a, p[1] + b, 0) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))}
    return corners, links


SQ = [(0, 0, 0), (2, 0, 0), (0, 2, 0), (2, 2, 0)]
RECT = [(2 * i, 2 * j, 0) for i in range(3) for j in range(2)]
LTRI_V, LTRI_P = window([(0, 0), (1, 0), (0, 1)])

print("A. the closed-set search against the plain search of open PR 8715")
rows = []
for name, V, P, sch in [("square", SQ, [], None), ("square + P", SQ, [(1, 1, 0)], None),
                        ("2x1 + P", RECT, [(1, 1, 0), (3, 1, 0)], None),
                        ("2x1 + P, V nothing", RECT, [(1, 1, 0), (3, 1, 0)], {"V": "nothing"}),
                        ("L tromino + P", LTRI_V, LTRI_P, None)]:
    win = build(V, P, [], sch)
    cf, cs, cb = closed_search(win, 1000)
    pf, ps, pb = plain_search(win, 20000)
    rows.append((name, cf, pf, cs, ps, bin(cb).count("1"), pb))
agree = all(r[1] is r[2] and r[5] == r[6] for r in rows)
known = [(r[1], r[5]) for r in rows[:4]] == [(False, 3), (True, 9), (False, 7), (False, 11)]
check("the closed-set search reproduces the plain search: same verdicts and the same largest formed sets",
      agree and known,
      "; ".join(f"{r[0]}: {'order' if r[1] else 'none'}, {r[3]} closed / {r[4]} plain sets, largest {r[5]}" for r in rows))

if not RESULTS[-1]:
    print("the closed-set search failed its check against the plain search; the window sweep is not run")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
    sys.exit(1)

print("B. the six-square windows")
polys = polyominoes(6)
OLD = set()
for k in range(1, 6):
    for cells in polys[k]:
        V, P = window(cells)
        OLD.add(canon([(v[0] // 2, v[1] // 2) for v in V]))
WINDOWS = {}
for cells in sorted(polys[6]):
    V, P = window(cells)
    key = canon([(v[0] // 2, v[1] // 2) for v in V])
    if key not in OLD:
        WINDOWS.setdefault(key, (6, cells, V, P))
nv = sorted({len(w[2]) for w in WINDOWS.values()})
npl = {}
for w in WINDOWS.values():
    npl[len(w[3])] = npl.get(len(w[3]), 0) + 1
check("free hexominoes number 35 and span 32 windows that no smaller polyomino spans, with 13 or 14 vertices and 6 or 7 coordinators",
      len(polys[6]) == 35 and len(WINDOWS) == 32 and nv == [13, 14] and npl == {6: 29, 7: 3},
      f"{len(polys[6])} free hexominoes, {len(WINDOWS)} new windows; " + ", ".join(f"{c} with {p} coordinators" for p, c in sorted(npl.items())))
if not RESULTS[-1]:
    print("the window set failed its check; the sweep is not run")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
    sys.exit(1)

TOT = {}
for key, (k, cells, V, P) in WINDOWS.items():
    TOT[key] = (int(build(V, P, [])["w"].sum()), generating_weight([(v[0] // 2, v[1] // 2, 0) for v in V])[1])
check("every window's total weight equals its generating-function coefficient",
      all(t == c for t, c in TOT.values()),
      f"{sum(t == c for t, c in TOT.values())} of {len(TOT)}; totals from {min(t for t, c in TOT.values())} to {max(t for t, c in TOT.values())}")
if not RESULTS[-1]:
    print("the window weights failed their check; the sweep is not run")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
    sys.exit(1)

# one window at a time: build, search, inspect, discard (a 14-vertex window's search holds about 1.5 GB)
REC = {}
for key, (k, cells, V, P) in WINDOWS.items():
    win = build(V, P, [])
    found, nsets, F = closed_search(win, 5000)
    got = {win["sites"][i] for i in range(len(win["sites"])) if F >> i & 1}
    options = []
    for p in P:
        corners, links = square_sites(p)
        shared = {c for c in corners if any(c in square_sites(q)[0] for q in P if q != p)}
        options.append({("P", p)} | {("L", l) for l in links} | {("V", c) for c in corners - shared})
    best = max(len(o) for o in options)
    shape = len(got) == best and got in [o for o in options if len(o) == best]
    gF = group_of(win, [i for i in range(len(win["sites"])) if F >> i & 1])
    dead = not any(admissible(win, gF, x, formed_neighbours(win, x, F)) for x in range(len(win["sites"])) if not F >> x & 1)
    REC[key] = (found, nsets, bin(F).count("1"), shape, dead)
    del win, gF
print("C. no order on any six-square window")
sizes = {}
for r in REC.values():
    sizes[r[2]] = sizes.get(r[2], 0) + 1
check("full local records with every coordinator: none of the 32 windows admits an order, and every search finishes",
      all(r[0] is False and 38 <= r[1] <= 42 and r[2] == 7 for r in REC.values()),
      f"closed sets per search {min(r[1] for r in REC.values())} to {max(r[1] for r in REC.values())}; largest formed set "
      + ", ".join(f"{s} sites in {c} windows" for s, c in sorted(sizes.items())))

print("D. where every search stops")
check("each search records one maximum-size square set with its unshared corners, for a square with the fewest shared corners",
      all(r[3] and r[4] for r in REC.values()),
      f"in {sum(r[3] and r[4] for r in REC.values())} of {len(REC)} windows one recorded maximum-size formed set is that square set, "
      "and no site outside it has a conditional that depends only on its formed neighbours")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
