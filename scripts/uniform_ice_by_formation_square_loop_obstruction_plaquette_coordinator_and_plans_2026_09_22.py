#!/usr/bin/env python3
"""Uniform ice by formation: on the square window, no nearest-neighbour
formation with local records reproduces the uniform ice measure without an
unrecorded site, in any fixed external order with fresh conditional draws and any local rule; the plaquette site, which
neighbours the square's four links, coordinates them and reproduces it
exactly; non-local records ("plans") also reproduce it.  Exact and finite.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic; no floating point.

Declared objects
  * the square window: four vertices of one coarse plaquette, their twenty
    links, and optionally the plaquette site at the centre, which is the
    nearest neighbour of the square's four links;
  * the uniform ice measure on the window: link occupations with exactly 3
    of each vertex's 6 links occupied, each configuration equally likely;
  * local records: a vertex records the occupations of its six links, a link
    its own occupation; formation reading, where a site's law depends on its
    formed nearest neighbours only, and hole semantics;
  * the sweep order of open PR 8667 (each vertex after the links it shares
    with earlier vertices), a plaquette-first order, and plan records (a
    vertex records a whole window configuration, copied along).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 120
from fractions import Fraction as Fr
from itertools import combinations, product
from math import comb

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


V = [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)]
STAR = {v: [add(v, d) for d in DIRS] for v in V}
LINKS = sorted({l for v in V for l in STAR[v]})
SHARED = [(1, 0, 0), (2, 1, 0), (1, 2, 0), (0, 1, 0)]
P = (1, 1, 0)
CYC = [V[0], SHARED[0], V[1], SHARED[1], V[2], SHARED[2], V[3], SHARED[3]]
ICE = [dict(zip(LINKS, bits)) for bits in product((0, 1), repeat=len(LINKS))
       if all(sum(dict(zip(LINKS, bits))[l] for l in STAR[v]) == 3 for v in V)]


def rec(n, s):
    return tuple(n[l] for l in STAR[s]) if s in STAR else n[s]


def graph(with_p):
    nodes = V + LINKS + ([P] if with_p else [])
    edges = {frozenset((v, l)) for v in V for l in STAR[v]}
    if with_p:
        edges |= {frozenset((P, l)) for l in SHARED}
    return nodes, edges


def cyclomatic(nodes, edges):
    parent = {x: x for x in nodes}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    comps = len(nodes)
    for e in edges:
        a, b = tuple(e)
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            comps -= 1
    return len(edges) - len(nodes) + comps


def dependent(pairs):
    joint, pa, pb, tot = {}, {}, {}, 0
    for x, y in pairs:
        joint[(x, y)] = joint.get((x, y), 0) + 1
        pa[x] = pa.get(x, 0) + 1
        pb[y] = pb.get(y, 0) + 1
        tot += 1
    return any(Fr(joint.get((x, y), 0), tot) != Fr(pa[x], tot) * Fr(pb[y], tot) for x in pa for y in pb)


# ---------- A. the window ----------
print("A. the square window")
T = [[comb(4, 3 - (x + y)) for y in (0, 1)] for x in (0, 1)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


T4 = matmul(matmul(T, T), matmul(T, T))
check("ice configurations on the window: 10016 = tr T^4 with T = [[4,6],[6,4]]",
      len(ICE) == 10016 == T4[0][0] + T4[1][1] and len(LINKS) == 20, "4 vertices, 20 links, 4 of them shared")

# ---------- B. the loop obstruction ----------
print("B. local records, no plaquette site")
nodes, edges = graph(False)
forest = all(cyclomatic([x for x in nodes if x != c], {e for e in edges if c not in e}) == 0 for c in CYC)
check("the incidence graph has exactly one loop, the square; removing any of its 8 sites leaves a forest",
      cyclomatic(nodes, edges) == 1 and forest)
rows = []
for k, c in enumerate(CYC):
    path = CYC[k + 1:] + CYC[:k]
    a, b = path[0], path[-1]
    marg = dependent((rec(n, a), rec(n, b)) for n in ICE)
    inner = []
    for m in path[1:-1]:
        groups = {}
        for n in ICE:
            groups.setdefault(rec(n, m), []).append((rec(n, a), rec(n, b)))
        inner.append(any(dependent(g) for g in groups.values()))
    rows.append((marg, sum(inner), inner[2]))
check("for each choice of the last square site, the path's ends are dependent marginally and given the middle site",
      all(r[0] and r[2] for r in rows),
      f"dependent given {min(r[1] for r in rows)}-{max(r[1] for r in rows)} of 5 inner sites; a collider forces "
      "marginal independence, no collider forces independence given every inner site")


def form(order, rule):
    layer = {(): Fr(1)}
    for k, s in enumerate(order):
        nxt = {}
        for part, mass in layer.items():
            formed = dict(zip(order[:k], part))
            nb = {t: formed[t] for t in formed if t in NB[s]}
            probs = rule(s, nb)
            tot = Fr(0)
            for val, p in probs.items():
                key = part + (val,)
                nxt[key] = nxt.get(key, Fr(0)) + mass * p
                tot += p
            if tot < 1:
                key = part + ("unrecorded",)
                nxt[key] = nxt.get(key, Fr(0)) + mass * (1 - tot)
        layer = nxt
    return layer


NB = {s: set() for s in V + LINKS + [P]}
for v in V:
    for l in STAR[v]:
        NB[v].add(l)
        NB[l].add(v)
for l in SHARED:
    NB[P].add(l)
    NB[l].add(P)
MU4 = {pat: Fr(1, 1) for pat in product((0, 1), repeat=4)}
for pat in MU4:
    w = 1
    for i in range(4):
        w *= comb(4, 3 - (pat[i - 1] + pat[i]))
    MU4[pat] = Fr(w, 10016)


def local_rule(s, nb):
    if s == P:
        return dict(MU4) if not nb else {}
    if s in STAR:
        stars = [t for t in product((0, 1), repeat=6) if sum(t) == 3
                 and all(t[STAR[s].index(l)] == x for l, x in nb.items())]
        return {t: Fr(1, len(stars)) for t in stars} if stars else {}
    told = set()
    for t, x in nb.items():
        told.add(x[SHARED.index(s)] if t == P else x[STAR[t].index(s)])
    if len(told) > 1:
        return {}
    return {told.pop(): Fr(1)} if told else {0: Fr(1, 2), 1: Fr(1, 2)}


def link_law(order, law):
    out = {}
    for st, m in law.items():
        if "unrecorded" in st:
            continue
        val = dict(zip(order, st))
        key = tuple(val[l] for l in LINKS)
        out[key] = out.get(key, Fr(0)) + m
    return out


sweep = []
for v in V:
    sweep.append(v)
    sweep += [l for l in STAR[v] if l not in sweep]
sw = link_law(sweep, form(sweep, local_rule))
check("the sweep order of open PR 8667 completes without an unrecorded site but not uniformly",
      sum(sw.values()) == 1 and len(sw) == 10016 and set(sw.values()) == {Fr(1, 8000), Fr(1, 12000)},
      "masses 1/8000 or 1/12000, the theorem excludes exact uniformity for fixed-order local-record laws")

# ---------- C. the plaquette coordinator ----------
print("C. the plaquette site as coordinator")
nodes_p, edges_p = graph(True)
check("with the plaquette site, removing any square site still leaves a loop through the plaquette",
      all(cyclomatic([x for x in nodes_p if x != c], {e for e in edges_p if c not in e}) >= 1 for c in CYC),
      f"{cyclomatic(nodes_p, edges_p)} independent loops")
d4 = [(lambda p, r=r: tuple(p[(i + r) % 4] for i in range(4))) for r in range(4)]
d4 += [(lambda p, r=r: tuple(p[(r - i) % 4] for i in range(4))) for r in range(4)]
check("the coordinator's law on its four links is invariant under the 8 symmetries of the square",
      all(MU4[g(p)] == MU4[p] for g in d4 for p in MU4) and sum(MU4.values()) == 1,
      "its law is the ice measure's marginal on the shared links")
pfirst = [P] + SHARED + V + [l for l in LINKS if l not in SHARED]
pl = link_law(pfirst, form(pfirst, local_rule))
check("plaquette first, then its links, then vertices: no unrecorded site and exactly the uniform ice law",
      sum(pl.values()) == 1 and len(pl) == 10016 and set(pl.values()) == {Fr(1, 10016)})

GRID_V = [(x, y, 0) for x in (0, 2, 4) for y in (0, 2)]
GRID_E = sorted({add(v, d) for v in GRID_V for d in DIRS[:4]
                 if add(add(v, d), d) in GRID_V})
DANG = {v: 6 - sum(1 for d in DIRS if add(v, d) in GRID_E) for v in GRID_V}
two = {}
for bits in product((0, 1), repeat=len(GRID_E)):
    e = dict(zip(GRID_E, bits))
    w = 1
    for v in GRID_V:
        k = 3 - sum(e[add(v, d)] for d in DIRS if add(v, d) in GRID_E)
        w *= comb(DANG[v], k) if 0 <= k <= DANG[v] else 0
    if w:
        two[bits] = w
MID = (2, 1, 0)
SQ1 = [(1, 0, 0), (1, 2, 0), (0, 1, 0)]
SQ2 = [(3, 0, 0), (3, 2, 0), (4, 1, 0)]
groups = {}
for bits, w in two.items():
    e = dict(zip(GRID_E, bits))
    groups.setdefault(e[MID], []).extend([(tuple(e[l] for l in SQ1), tuple(e[l] for l in SQ2))] * w)
check("two squares sharing a link: each square's other links depend on the other square's given the shared link",
      len(GRID_E) == 7 and sum(two.values()) == 501632 and all(dependent(g) for g in groups.values()),
      f"{sum(two.values())} ice configurations; a second coordinator seeing only the shared link cannot supply them")

# ---------- D. plans ----------
print("D. non-local records")
plan_choices = {tuple(n[l] for l in LINKS): Fr(1, len(ICE)) for n in ICE}


def plan_rule(s, nb):
    if not nb:
        return plan_choices
    values = set(nb.values())
    return {next(iter(values)): Fr(1)} if len(values) == 1 else {}


plan_history = form(sweep, plan_rule)
plan_law = {}
consistent = True
for history, mass in plan_history.items():
    consistent = consistent and len(set(history)) == 1 and "unrecorded" not in history
    if "unrecorded" not in history:
        plan = history[0]
        plan_law[plan] = plan_law.get(plan, Fr(0)) + mass
check("a uniform whole-window plan actually propagates through the connected order",
      consistent and len(plan_history) == 10016 and plan_law == plan_choices,
      "10016 complete propagated histories; every site carries the same plan")

print("per_element: checked 10016 square configurations, exact marginal dependences, and 10016 propagated plan histories")
print("per_site: checked each of the eight last-cycle-site choices and the declared local formation rules")
print("per_mode: not executed; no continuum, Fourier or spectral mode computation is claimed")
print("per_block: checked one square with twenty links and the two-square weighted count 501632")
print("lattice_wide: not executed; no infinite-lattice formation or universal coordinator requirement is inferred")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
