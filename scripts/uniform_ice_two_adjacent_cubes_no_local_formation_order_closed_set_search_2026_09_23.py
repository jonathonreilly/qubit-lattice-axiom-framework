#!/usr/bin/env python3
"""Closed-set formation search on two adjacent cubes.

Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. The recorded attaining set does not classify all maximal sets.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
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


SQ = [(0, 0, 0), (2, 0, 0), (0, 2, 0), (2, 2, 0)]
RECT = [(2 * i, 2 * j, 0) for i in range(3) for j in range(2)]
CUBE = [(2 * i, 2 * j, 2 * k) for i in range(2) for j in range(2) for k in range(2)]
CUBE_P = sorted({(x, y, z) for x in range(3) for y in range(3) for z in range(3) if sum(c % 2 for c in (x, y, z)) == 2})
TWO = [(2 * i, 2 * j, 2 * k) for i in range(3) for j in range(2) for k in range(2)]
TWO_P = sorted({(x, y, z) for x in range(5) for y in range(3) for z in range(3) if sum(c % 2 for c in (x, y, z)) == 2})
TWO_C = [(1, 1, 1), (3, 1, 1)]

print("A. the closed-set search against the plain search of open PR 8715")
rows = []
for name, V, P, C, sch, bfs in [("square", SQ, [], [], None, True), ("square + P", SQ, [(1, 1, 0)], [], None, True),
                                ("2x1 + P", RECT, [(1, 1, 0), (3, 1, 0)], [], None, True),
                                ("2x1 + P, V nothing", RECT, [(1, 1, 0), (3, 1, 0)], [], {"V": "nothing"}, True),
                                ("cube", CUBE, CUBE_P, [], None, True), ("cube + C", CUBE, CUBE_P, [(1, 1, 1)], None, False)]:
    win = build(V, P, C, sch)
    cf, cs, cb = closed_search(win, 1000)
    pf, ps, pb = plain_search(win, 5000) if bfs else (None, None, None)
    rows.append((name, cf, pf, cs, ps, bin(cb).count("1"), pb))
agree = all(r[1] is r[2] and r[5] == r[6] for r in rows if r[2] is not None)
known = [(r[1], r[5]) for r in rows] == [(False, 3), (True, 9), (False, 7), (False, 11), (False, 5), (True, 27)]
check("the closed-set search reproduces the plain search: same verdicts and the same largest formed sets",
      agree and known,
      "; ".join(f"{r[0]}: {'order' if r[1] else 'none'}, {r[3]} closed / {r[4] if r[4] else '-'} plain sets, largest {r[5]}" for r in rows))

if not RESULTS[-1]:
    print("the closed-set search failed its check against the plain search; the two-cube sections are not run")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
    sys.exit(1)

print("B. the two-cube window")
two = build(TWO, TWO_P, TWO_C)
n_edges, coeff = generating_weight([(i, j, k) for i in range(3) for j in range(2) for k in range(2)])
check("two cubes sharing a face: 45 sites, 20 grid links, weight 3985518592 = generating-function coefficient",
      len(two["sites"]) == 45 and n_edges == 20 and int(two["w"].sum()) == coeff == 3985518592,
      f"{len(two['w'])} grid patterns carry weight")

print("C. no order, with both cube sites")
found, states, bestF = closed_search(two, 1000)
got = {two["sites"][k] for k in range(45) if bestF >> k & 1}
one_cube = [{t for t in two["sites"] if max(abs(a - b) for a, b in zip(t[1], c)) <= 1 and (t[0] != "V" or t[1][0] != 2)}
            for c in TWO_C]
check("full local records: no complete order; a recorded largest formed set has the stated cube shape",
      found is False and states == 46 and got in one_cube and len(got) == 23,
      f"{states} closed sets; largest {len(got)} of 45: one cube site, its 6 plaquettes, 12 links and 4 outer vertices")

print("D. coarser record schemes")
out = []
for sch in [{"V": "nothing"}, {"P": "nothing"}, {"V": "nothing", "P": "nothing"}]:
    f, s_, b = closed_search(build(TWO, TWO_P, TWO_C, sch), 1000)
    out.append((sch, f, s_, bin(b).count("1")))
check("vertex records nothing, plaquette records nothing, or both nothing: no complete order",
      all(r[1] is False for r in out) and [(r[2],r[3]) for r in out] == [(34,31),(35,16),(23,24)],
      "; ".join(f"{','.join(k + ' ' + v for k, v in r[0].items())}: {r[2]} closed sets, largest {r[3]}" for r in out))

print("E. why the other cube cannot follow")
c1, c2 = two["sites"].index(("C", TWO_C[0])), two["sites"].index(("C", TWO_C[1]))
p0 = two["sites"].index(("P", (2, 1, 1)))
beyond = not admissible(two, group_of(two, [c1, p0]), c2, frozenset([p0]))
coupling = [[comb(2, 3 - (1 + e1 + e2)) for e2 in (0, 1)] for e1 in (0, 1)]
check("the other cube site depends on the formed cube beyond the shared plaquette",
      beyond and coupling == [[1, 2], [2, 1]] and coupling[0][0] * coupling[1][1] != coupling[0][1] * coupling[1][0],
      "at a shared vertex with one face link occupied the weights C(2, 2 - e1 - e2) of the two cubes' "
      "perpendicular edges form [[1, 2], [2, 1]], rank 2")

print('per_element: Integer configurations, weights and conditional cross-products are exact within the stated finite alphabets; floating spectral estimates are labelled.')
print('per_site: Site and unit tests use the declared records, neighbour graph, boundary conditions and fixed formation orders only.')
print('per_mode: Transfer and walk modes refer to supplied finite matrices; numerical estimates do not establish untested physical or infinite-cross-section limits.')
print('per_block: This bounded support result retains its explicit controls, parameter values and search caps; alternative rules and records remain outside scope.')
print('lattice_wide: Finite windows do not establish universal formation impossibility; infinite-height statements apply only to the specified fixed-cross-section transfer model.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
