#!/usr/bin/env python3
"""Uniform ice by joint cell units: rows yes, the 2 x 2 block no.

A joint unit forms several sites at once with a joint law.  Take cell units:
each unit forms every not-yet-formed site of one closed square (its
plaquette site, its four links and its four vertices, vertices recording
their full grid pattern) jointly.  Such a formation reproduces the uniform
ice measure exactly, with no unrecorded site, iff some order of the units
has each unit's joint conditional, given everything formed before it,
depend only on the formed sites adjacent to the unit's new sites (the unit
form of the criterion of open PR 8715).  On planar windows, every unit
order is checked with exact conditional laws: one square and two squares,
every order; a row of three, the four orders that never form both ends
before the middle; the 2 x 2 block, no order.  Units that are whole rows of
the 2 x 3 window form a chain and are exact in exactly the orders that do
not form both end rows first.  In three dimensions, two cubes are exact in
both orders (enumeration), and on the 2 x 2 x 1 slab of cubes every ordered
pair of first units fails at the second unit (exact counterexamples).
Row units wrapped into a loop (a cylinder of three rows) have no exact
order: layers must be formed as a chain along an open axis.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * windows in doubled coordinates: nx x ny coarse squares in a plane,
    their vertices, grid links and plaquette sites; each vertex's other
    links private to it; nearest neighbours are sites at distance 1;
  * the uniform ice measure: 3 of each vertex's 6 links occupied; on grid
    links it weighs a pattern by prod_v C(private links, 3 - grid sum);
  * records: links their occupation, vertices and plaquettes the pattern of
    their own grid links;
  * cell units as above, formed in a declared order.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import permutations, product
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


def window(nx, ny):
    V = [(2 * i, 2 * j, 0) for i in range(nx + 1) for j in range(ny + 1)]
    Vs = set(V)
    grid = sorted({add(v, d) for v in V for d in DIRS[:4] if add(add(v, d), d) in Vs})
    P = [(2 * i + 1, 2 * j + 1, 0) for i in range(nx) for j in range(ny)]
    sites = [("V", v) for v in V] + [("L", l) for l in grid] + [("P", p) for p in P]
    n = len(sites)
    nb = [set() for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if sum(abs(x - y) for x, y in zip(sites[a][1], sites[b][1])) == 1:
                nb[a].add(b)
                nb[b].add(a)
    gidx = {l: k for k, l in enumerate(grid)}
    configs = []
    for bits in product((0, 1), repeat=len(grid)):
        w = 1
        for v in V:
            inc = [gidx[add(v, d)] for d in DIRS if add(v, d) in gidx]
            k = 3 - sum(bits[e] for e in inc)
            priv = 6 - len(inc)
            w *= comb(priv, k) if 0 <= k <= priv else 0
        if w:
            recs = [bits[gidx[s]] if t == "L" else tuple(bits[gidx[add(s, d)]] for d in DIRS if add(s, d) in gidx)
                    for t, s in sites]
            configs.append((tuple(recs), w))
    cells = [[k for k, (t, s) in enumerate(sites) if max(abs(x - y) for x, y in zip(s, p)) <= 1] for p in P]
    return sites, nb, configs, cells


def cond_equal(configs, formed, new, adj):
    """Is the joint law of `new` given `formed` a function of the records in `adj` (a subset of formed)?"""
    fl, al = sorted(formed), sorted(adj)
    by_f, by_a = {}, {}
    for recs, w in configs:
        kf, ka, kn = tuple(recs[k] for k in fl), tuple(recs[k] for k in al), tuple(recs[k] for k in new)
        d = by_f.setdefault(kf, [ka, {}])[1]
        d[kn] = d.get(kn, 0) + w
        e = by_a.setdefault(ka, {})
        e[kn] = e.get(kn, 0) + w
    for kf, (ka, d) in by_f.items():
        tf, ta = sum(d.values()), sum(by_a[ka].values())
        for kn in set(d) | set(by_a[ka]):
            if Fr(d.get(kn, 0), tf) != Fr(by_a[ka].get(kn, 0), ta):
                return False
    return True


def exact_orders(nx, ny):
    sites, nb, configs, cells = window(nx, ny)
    good, first_fail = [], {}
    for order in permutations(range(len(cells))):
        formed, ok = set(), True
        for step, u in enumerate(order):
            new = [k for k in cells[u] if k not in formed]
            adj = {k for k in formed if any(k in nb[x] for x in new)}
            if not cond_equal(configs, formed, new, adj):
                ok = False
                first_fail[order] = step
                break
            formed |= set(new)
        if ok:
            good.append(order)
    return sites, configs, cells, good, first_fail


print("A. the windows")
W = {}
for nx, ny in [(1, 1), (2, 1), (3, 1), (2, 2)]:
    W[(nx, ny)] = exact_orders(nx, ny)
weights = {k: sum(w for _, w in v[1]) for k, v in W.items()}
check("uniform ice weights: 10016 (one square), 501632 (2 x 1), 25123328 (3 x 1), 125836800 (2 x 2)",
      weights == {(1, 1): 10016, (2, 1): 501632, (3, 1): 25123328, (2, 2): 125836800},
      "; ".join(f"{k[0]}x{k[1]}: {len(W[k][0])} sites, {len(W[k][1])} grid patterns" for k in W))

print("B. rows")
row3 = W[(3, 1)]
ends_first = {o for o in permutations(range(3)) if o.index(1) == 2}
check("one square and two squares: every unit order is exact; a row of three: exactly the orders that do not form both ends first",
      len(W[(1, 1)][3]) == 1 and len(W[(2, 1)][3]) == 2 and set(row3[3]) == set(permutations(range(3))) - ends_first,
      f"row of three: {len(row3[3])} of 6 orders exact; the failing ones form cells 0 and 2 before cell 1")

print("C. the 2 x 2 block")
blk = W[(2, 2)]
steps = sorted(set(blk[4].values()))
check("the 2 x 2 block: no unit order is exact",
      len(blk[3]) == 0 and len(blk[4]) == 24,
      f"all 24 orders fail, first at unit step {', '.join(str(s + 1) for s in steps)} "
      "(counting from 1): the unformed cells close a loop around the centre")

print("D. row units")
sites23, nb23, configs23, cells23 = window(2, 3)
P23 = [s for t, s in sites23 if t == "P"]
rows23 = [sorted({k for c, p in zip(cells23, P23) if p[1] == 2 * j + 1 for k in c}) for j in range(3)]
row_exact = []
for order in permutations(range(3)):
    formed, ok = set(), True
    for u in order:
        new = [k for k in rows23[u] if k not in formed]
        adj = {k for k in formed if any(k in nb23[x] for x in new)}
        ok = ok and cond_equal(configs23, formed, new, adj)
        formed |= set(new)
    if ok:
        row_exact.append(order)
check("row units on the 2 x 3 window: exact in exactly the orders that do not form both end rows first",
      set(row_exact) == set(permutations(range(3))) - {o for o in permutations(range(3)) if o.index(1) == 2}
      and sorted(set().union(*map(set, rows23))) == list(range(len(sites23))),
      f"{len(row_exact)} of 6 orders exact; {len(configs23)} grid patterns; each unit is a whole row of two cells, "
      "so the units form a chain, as a sweep's layers do")

print("E. two cubes")


def cube_window(V, P, C):
    """Numpy form: sites, neighbours, record codes, code ranges, integer weights, own edges, edge list."""
    Vs = set(V)
    grid = sorted({add(v, d) for v in V for d in DIRS if add(add(v, d), d) in Vs})
    gidx = {l: k for k, l in enumerate(grid)}
    sites = [("V", v) for v in V] + [("L", l) for l in grid] + [("P", q) for q in P] + [("C", c) for c in C]
    n = len(sites)
    nb = [set() for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if sum(abs(x - y) for x, y in zip(sites[a][1], sites[b][1])) == 1:
                nb[a].add(b)
                nb[b].add(a)
    own = []
    for t, q in sites:
        if t == "L":
            own.append([gidx[q]])
        elif t in "VP":
            own.append([gidx[add(q, d)] for d in DIRS if add(q, d) in gidx])
        else:
            own.append([gidx[l] for l in grid if max(abs(x - y) for x, y in zip(l, q)) == 1])
    return sites, nb, own, grid, gidx


def ndense(keys):
    u, inv = np.unique(keys, return_inverse=True)
    return inv.astype(np.int64).ravel(), len(u)


def unit_exact_np(bits, w, own, F, new, adj):
    """Exact unit test by enumeration: is the joint law of `new` given `F` a function of `adj`?"""
    def group(idxs):
        g = np.zeros(len(w), dtype=np.int64)
        for k in sorted(idxs):
            code = np.zeros(len(w), dtype=np.int64)
            for j, e in enumerate(own[k]):
                code |= bits[:, e] << j
            g, _ = ndense(g * (1 << len(own[k])) + code)
        return g
    wf = w.astype(np.float64)
    gF, gN, gA = group(F), group(new), group(adj)
    KN = int(gN.max()) + 1
    _, first, gFN = np.unique(gF * KN + gN, return_index=True, return_inverse=True)
    gFN = gFN.ravel()
    gAN, _ = ndense(gA * KN + gN)
    WFN, WF, WA, WAN = (np.bincount(gFN, weights=wf), np.bincount(gF, weights=wf),
                        np.bincount(gA, weights=wf), np.bincount(gAN, weights=wf))
    lhs, rhs = WFN * WA[gA[first]], WAN[gAN[first]] * WF[gF[first]]
    if np.any(np.abs(lhs - rhs) > 1e-9 * np.maximum(lhs, rhs)):
        return False
    as_int = lambda a: a.astype(np.int64).astype(object)
    return bool(np.all(as_int(WFN) * as_int(WA[gA[first]]) == as_int(WAN[gAN[first]]) * as_int(WF[gF[first]])))


TV = [(2 * i, 2 * j, 2 * k) for i in range(3) for j in range(2) for k in range(2)]
TP = sorted({(x, y, z) for x in range(5) for y in range(3) for z in range(3) if sum(c % 2 for c in (x, y, z)) == 2})
TC = [(1, 1, 1), (3, 1, 1)]
tsites, tnb, town, tgrid, tgidx = cube_window(TV, TP, TC)
E2 = len(tgrid)
tbits = (np.arange(1 << E2, dtype=np.int64)[:, None] >> np.arange(E2, dtype=np.int64)) & 1
tw = np.ones(1 << E2, dtype=np.int64)
for v in TV:
    inc = [tgidx[add(v, d)] for d in DIRS if add(v, d) in tgidx]
    table = np.array([comb(6 - len(inc), 3 - k) if 0 <= 3 - k <= 6 - len(inc) else 0 for k in range(len(inc) + 1)], dtype=np.int64)
    tw *= table[tbits[:, inc].sum(axis=1)]
keep = tw > 0
tbits, tw = tbits[keep], tw[keep]
tcells = [[k for k, (t, q) in enumerate(tsites) if max(abs(x - y) for x, y in zip(q, c)) <= 1] for c in TC]
two_ok = []
for u1, u2 in ((0, 1), (1, 0)):
    F = set(tcells[u1])
    new = [k for k in tcells[u2] if k not in F]
    adj = {k for k in F if any(k in tnb[x] for x in new)}
    two_ok.append(unit_exact_np(tbits, tw, town, F, new, adj) and len(adj) < len(F)
                  and not unit_exact_np(tbits, tw, town, F, new, set()))
check("two cubes sharing a face: cell units are exact in both orders",
      all(two_ok) and int(tw.sum()) == 3985518592,
      f"{len(tw)} grid patterns of weight 3985518592 (as in open PR 8719); the second cube, given the first cube's "
      "sites with their full vertex records, depends only on the sites it touches, and does depend on them")

print("F. the 2 x 2 x 1 slab of cubes")
SV = [(2 * i, 2 * j, 2 * k) for i in range(3) for j in range(3) for k in range(2)]
SC = [(1, 1, 1), (3, 1, 1), (1, 3, 1), (3, 3, 1)]
SP = sorted({(x, y, z) for x in range(5) for y in range(5) for z in range(3) if sum(c % 2 for c in (x, y, z)) == 2
             and any(max(abs(a - b) for a, b in zip((x, y, z), c)) <= 1 for c in SC)})
ssites, snb, sown, sgrid, sgidx = cube_window(SV, SP, SC)
sinc = {v: [sgidx[add(v, d)] for d in DIRS if add(v, d) in sgidx] for v in SV}


def sweight(e):
    w = 1
    for v in SV:
        k = 3 - sum(e[i] for i in sinc[v])
        pv = 6 - len(sinc[v])
        if not 0 <= k <= pv:
            return 0
        w *= comb(pv, k)
    return w


def law_new(fixed, free_new, rest):
    """Exact law of the new free edges given fixed edge values, summing the remaining edges."""
    out, e = {}, [None] * len(sgrid)
    for k, v in fixed.items():
        e[k] = v
    for a in product((0, 1), repeat=len(free_new)):
        for k, v in zip(free_new, a):
            e[k] = v
        tot = 0
        for b in product((0, 1), repeat=len(rest)):
            for k, v in zip(rest, b):
                e[k] = v
            tot += sweight(e)
        if tot:
            out[a] = tot
    z = sum(out.values())
    return {a: Fr(v, z) for a, v in out.items()} if z else None


scells = [[k for k, (t, q) in enumerate(ssites) if max(abs(x - y) for x, y in zip(q, c)) <= 1] for c in SC]
rng = random.Random(1)
witness = {}
for u1 in range(4):
    for u2 in range(4):
        if u1 == u2:
            continue
        F = set(scells[u1])
        new = [k for k in scells[u2] if k not in F]
        adj = {k for k in F if any(k in snb[x] for x in new)}
        EF = sorted({e for k in F for e in sown[k]})
        Eadj = {e for k in adj for e in sown[k]}
        free_new = sorted({e for k in new for e in sown[k]} - set(EF))
        rest = sorted(set(range(len(sgrid))) - set(EF) - set(free_new))
        for trial in range(200):
            f1 = {e: rng.randint(0, 1) for e in EF}
            L1 = law_new(f1, free_new, rest)
            if L1 is None:
                continue
            hit = None
            for e in EF:
                if e in Eadj:
                    continue
                f2 = dict(f1)
                f2[e] ^= 1
                L2 = law_new(f2, free_new, rest)
                if L2 is not None and L2 != L1:
                    hit = e
                    break
            if hit is not None:
                witness[(u1, u2)] = (hit, f1, L1, free_new, rest, Eadj)
                break


def law_new_np(fixed, free_new, rest):
    """The same law by vectorised enumeration with a weight table, for an independent recomputation."""
    m = len(free_new) + len(rest)
    grid_e = np.zeros((1 << m, len(sgrid)), dtype=np.int64)
    for k, v in fixed.items():
        grid_e[:, k] = v
    cols = free_new + rest
    for j, k in enumerate(cols):
        grid_e[:, k] = (np.arange(1 << m) >> j) & 1
    w = np.ones(1 << m, dtype=np.int64)
    for v in SV:
        pv = 6 - len(sinc[v])
        table = np.array([comb(pv, 3 - k) if 0 <= 3 - k <= pv else 0 for k in range(len(sinc[v]) + 1)], dtype=np.int64)
        w *= table[grid_e[:, sinc[v]].sum(axis=1)]
    key = np.zeros(1 << m, dtype=np.int64)
    for j in range(len(free_new)):
        key |= ((np.arange(1 << m) >> j) & 1) << j
    tot = np.bincount(key, weights=w.astype(np.float64), minlength=1 << len(free_new)).astype(np.int64)
    z = int(tot.sum())
    return {tuple((idx >> j) & 1 for j in range(len(free_new))): Fr(int(tot[idx]), z) for idx in range(len(tot)) if tot[idx]}


agree = True
for (u1, u2), (hit, f1, L1, free_new, rest, Eadj) in witness.items():
    f2 = dict(f1)
    f2[hit] ^= 1
    agree = agree and hit not in Eadj and law_new_np(f1, free_new, rest) == L1 \
        and law_new_np(f2, free_new, rest) != L1 and law_new_np(f2, free_new, rest) == law_new(f2, free_new, rest)
check("the 2 x 2 x 1 slab: for every ordered pair of first units, the second unit depends on formed sites it does not touch",
      len(witness) == 12 and len(ssites) == 75 and len(sgrid) == 33 and agree,
      f"{len(ssites)} sites, {len(sgrid)} grid links; 12 of 12 ordered pairs have two formed patterns that agree on "
      "every site adjacent to the second unit and give different exact laws for it (recomputed by vectorised "
      "enumeration), so every one of the 24 orders fails at the second unit")

print("G. rows around a loop")
NYC = 6


def ydist(a, b):
    d = (a - b) % NYC
    return min(d, NYC - d)


def cdist(p, q):
    return abs(p[0] - q[0]) + ydist(p[1], q[1]) + abs(p[2] - q[2])


CV = [(2 * i, 2 * j, 0) for i in range(3) for j in range(3)]
CG = sorted({(2 * i + 1, 2 * j, 0) for i in range(2) for j in range(3)} | {(2 * i, 2 * j + 1, 0) for i in range(3) for j in range(3)})
CGI = {l: k for k, l in enumerate(CG)}
CP = [(2 * i + 1, 2 * j + 1, 0) for i in range(2) for j in range(3)]
csites = [("V", v) for v in CV] + [("L", l) for l in CG] + [("P", q) for q in CP]
cnb = [set() for _ in range(len(csites))]
for a_ in range(len(csites)):
    for b_ in range(a_ + 1, len(csites)):
        if cdist(csites[a_][1], csites[b_][1]) == 1:
            cnb[a_].add(b_)
            cnb[b_].add(a_)
cinc = {v: [CGI[l] for l in CG if cdist(v, l) == 1] for v in CV}
cconfigs = []
for bits in product((0, 1), repeat=len(CG)):
    w = 1
    for v in CV:
        k = 3 - sum(bits[e] for e in cinc[v])
        w *= comb(6 - len(cinc[v]), k) if 0 <= k <= 6 - len(cinc[v]) else 0
    if w:
        cconfigs.append((tuple(bits[CGI[q]] if t == "L" else tuple(bits[CGI[l]] for l in CG if cdist(q, l) == 1)
                              for t, q in csites), w))
crows = [sorted({k for k, (t, q) in enumerate(csites) for p in CP if p[1] == 2 * j + 1
                 and abs(q[0] - p[0]) <= 1 and ydist(q[1], p[1]) <= 1}) for j in range(3)]
loop_exact = []
for order in permutations(range(3)):
    formed, ok = set(), True
    for u in order:
        new = [k for k in crows[u] if k not in formed]
        adj = {k for k in formed if any(k in cnb[x] for x in new)}
        ok = ok and cond_equal(cconfigs, formed, new, adj)
        formed |= set(new)
    if ok:
        loop_exact.append(order)
check("row units around a loop (a cylinder, three rows wrapped): no order is exact",
      not loop_exact and len(cconfigs) == 21888 and sorted(set().union(*map(set, crows))) == list(range(len(csites))),
      f"{len(cconfigs)} grid patterns of weight {sum(w for _, w in cconfigs)}; the open 2 x 3 window has 4 exact orders, "
      "the wrapped one none: layers must be formed as a chain along an open axis")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
