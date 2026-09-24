#!/usr/bin/env python3
"""The record gas chessboard threshold: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-jfc7a (claude-opus-5-5).

Object (block 81, PR #8626): arrangements of records with six-axis contents on Z^3, weight z^N g^B Z0, Z0 = sum over contents of the
product over recorded bonds of M = c0*omega (M = J + 6 l1 P1 + 6 l2 P2), c = g c0. With zeta = 6z and W = Z0/6^N the occupancy law is
zeta^N g^B W. Staggered variable sigma_x = +1 iff x agrees with the A-chessboard (A = even sites); a bond is unlike iff sigma_x != sigma_y
(both occupied or both empty). Route: Dobrushin's translation map (no reflection positivity). All families exact (integers, Fractions).
"""
from __future__ import annotations

import itertools
import json
import random
import subprocess
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from math import comb

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


NOTES = [
    ("b81", "3b67807c6e", "docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_NEVER_MAKES_THE_CHESSBOARD_A_REST_MASS_NEEDS_BINDING_GROWS_ONLY_AROUND_"
     "LOOPS_CONTENT_ORDER_GIVES_THE_WALK_NO_GAP_BOUNDED_THEOREM_NOTE_2026-09-22.md",
     ["the weight of `η` at scale `g` is `z^{|η|} g^{|bonds|} Z₀(η)`",
      "`c = g·c₀`, `c₀ = 6/(p + q + 4r)` (block 40)",
      "`M = c₀ω = J + 6λ₁P₁ + 6λ₂P₂`",
      "If `x` and `y` lie in different components of `η`, `t₁ = t₂ = 0` and the factor is exactly `1` (or `g`)"]),
    ("a1", "2937d301c3", "probes/work/derive/the-record-gas-chessboard-threshold/w-jonathonsmac4f50-j2e73/ATTEMPT.md",
     ["`g* = 8.0·10⁻¹⁰` without contents", "**A direct Peierls argument would do better.**"]),
    ("ref", "f576541b43", "probes/work/derive/the-record-gas-chessboard-threshold/referee_w-macbookpro90c72-je490/REPORT.md",
     ["With contents this symmetry is not claimed, and neither is the canonical ensemble."]),
]
TASK_Q = ["do contents help or hurt the chessboard?", "HIT: a proof with an explicit g*."]
TASK_ID = "J:derive:the-record-gas-chessboard-threshold:a2"


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == TASK_ID), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, "block 81 (PR head), attempt 1 and its referee (ai/probes) and the task quoted verbatim (9 lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def isA(x):
    return (x[0] + x[1] + x[2]) % 2 == 0


def Mmatrix(p, q, r):
    T = p + q + 4 * r
    axes = NB
    def om(a, b):
        return p if a == b else (q if all(x == -y for x, y in zip(a, b)) else r)
    return [[Fr(6 * om(a, b), T) for b in axes] for a in axes]


# ---------------------------------------------------------------- a framed box with the A-chessboard outside
class Box:
    def __init__(self, L):
        self.S = {(i, j, k) for i in range(L) for j in range(L) for k in range(L)}
        self.sites = sorted(self.S)
        self.frame = {add(x, d) for x in self.sites for d in NB} - self.S
        self.bonds = sorted({tuple(sorted((x, add(x, d)))) for x in self.sites for d in NB})

    def occ(self, n, x):
        return n[x] if x in self.S else (1 if isA(x) else 0)

    def sig(self, n, x):
        return 1 if self.occ(n, x) == (1 if isA(x) else 0) else -1


def unlike(box, n):
    return sum(1 for x, y in box.bonds if box.sig(n, x) != box.sig(n, y))    # both occupied or both empty


def cluster_V(box, n, x0):
    C, st = {x0}, [x0]
    while st:
        x = st.pop()
        for d in NB:
            y = add(x, d)
            if y in box.S and y not in C and box.sig(n, y) == -1:
                C.add(y)
                st.append(y)
    V, seen = set(C), set()
    for s in box.sites:
        if s in C or s in seen:
            continue
        comp, st, touches = {s}, [s], False
        while st:
            x = st.pop()
            for d in NB:
                y = add(x, d)
                if y not in box.S:
                    touches = True
                elif y not in C and y not in comp:
                    comp.add(y)
                    st.append(y)
        seen |= comp
        if not touches:
            V |= comp
    return C, V


def shift(box, n, V, d):
    Vd = {add(y, d) for y in V}
    back = V - Vd
    n2 = dict(n)
    for x in Vd:
        if x in box.S:
            n2[x] = box.occ(n, sub(x, d))
    for x in back:
        n2[x] = 1 if isA(x) else 0
    return n2, Vd, back


def graph(box, n):
    recs = {x for x in box.S | box.frame if box.occ(n, x) == 1}
    edges = {frozenset((x, y)) for x in recs for dd in NB for y in [add(x, dd)] if y in recs}
    return recs, edges


def W_of(recs, edges, Mm, cap=6):
    """W = Z0/6^N. Removing a leaf removes a bridge (factor exactly 1, block 81 T1), so W is W of the 2-core, summed by brute force."""
    adj = defaultdict(set)
    for e in edges:
        a, b = tuple(e)
        adj[a].add(b)
        adj[b].add(a)
    core = {v: set(adj[v]) for v in recs}
    leaves = [v for v in core if len(core[v]) <= 1]
    while leaves:
        v = leaves.pop()
        if v not in core:
            continue
        for u in core.pop(v):
            core[u].discard(v)
            if len(core[u]) <= 1:
                leaves.append(u)
    seen, W = set(), Fr(1)
    for r0 in core:
        if r0 in seen:
            continue
        comp, st = [r0], [r0]
        seen.add(r0)
        while st:
            x = st.pop()
            for y in core[x]:
                if y not in seen:
                    seen.add(y)
                    comp.append(y)
                    st.append(y)
        if len(comp) > cap:
            return None
        idx = {v: i for i, v in enumerate(comp)}
        es = sorted({(min(idx[a], idx[b]), max(idx[a], idx[b])) for a in comp for b in core[a]})
        Z = sum((prod_M(Mm, s, es) for s in itertools.product(range(6), repeat=len(comp))), Fr(0))
        W *= Z / Fr(6) ** len(comp)
    return W


def prod_M(Mm, s, es):
    t = Fr(1)
    for i, j in es:
        t *= Mm[s[i]][s[j]]
    return t


def family_i_t() -> None:
    rnd = random.Random(11)
    box = Box(6)
    Mm = Mmatrix(3, 1, 2)
    Lam, m = max(max(rw) for rw in Mm), min(min(rw) for rw in Mm)
    # (I) at zeta = g^-3 the occupancy weight is g^(#unlike/2) up to a constant: B - 3N = (#unlike - #bonds)/2 + (frame ends)/2
    okI = True
    for _ in range(40):
        n = {x: rnd.randint(0, 1) for x in box.sites}
        B = sum(1 for x, y in box.bonds if box.occ(n, x) and box.occ(n, y))
        N = sum(n.values())
        fe = sum(box.occ(n, y) for x, y in box.bonds for y in (x, y) if y not in box.S)
        okI &= Fr(2 * B - 6 * N - fe) == Fr(unlike(box, n) - len(box.bonds))
    # (T) the translation map on random framed configurations, all six directions
    tried = okU = okN = okInj = okG = 0
    wt = okW = 0
    c = (2, 3, 3)
    for trial in range(70):
        n = {x: (1 if isA(x) else 0) for x in box.sites}
        for x in box.sites:
            if rnd.random() < 0.03:
                n[x] ^= 1
        blob = {c}
        for _ in range(rnd.randint(0, 7)):
            b = rnd.choice(sorted(blob))
            nb = add(b, rnd.choice(NB))
            if nb in box.S:
                blob.add(nb)
        for x in blob:
            n[x] = 0 if isA(x) else 1
        C, V = cluster_V(box, n, c)
        bd = [(y, add(y, d)) for y in V for d in NB if add(y, d) not in V]
        k = len(bd)
        u1 = unlike(box, n)
        R1, E1 = graph(box, n)
        G11 = [(y, z) for y, z in bd if box.occ(n, y) == 1 and box.occ(n, z) == 1]
        for d in NB:
            if any(add(y, d) not in box.S and add(y, d) not in box.frame for y in V):
                continue
            tried += 1
            n2, Vd, back = shift(box, n, V, d)
            okU += (u1 - unlike(box, n2) == k)
            front = Vd - V
            okN += (sum(n2.values()) - sum(n.values()) == sum(isA(x) for x in back) - sum(isA(x) for x in front))
            rec = dict(n2)
            for y in V:
                rec[y] = box.occ(n2, add(y, d))
            okInj += (rec == n)
            R2, E2 = graph(box, n2)
            F = [(y, z) for y, z in G11 if z == add(y, d)]
            Fmap = {z: y for y, z in F}
            def img(v):
                return sub(v, d) if v in Vd else (("new", v) if v in back else v)
            E2i = {frozenset((img(a), img(b))) for e in E2 for a, b in [tuple(e)]}
            Dset = {frozenset(b) for b in G11 if b not in F}
            Fset = {frozenset(b) for b in F}
            E1r = {frozenset((Fmap.get(a, a), Fmap.get(b, b))) for e in E1 if e not in Dset and e not in Fset for a, b in [tuple(e)]}
            okG += (E2i == E1r)
            if wt < 60:
                W1, W2 = W_of(R1, E1, Mm), W_of(R2, E2, Mm)
                if W1 is not None and W2 is not None:
                    wt += 1
                    okW += (W1 / W2 <= Lam ** len(G11) * (Lam / m) ** (5 * len(F)))
    ok = okI and tried > 200 and okU == okN == okInj == okG == tried and wt > 20 and okW == wt
    check("T", ok, f"framed 6^3 box, A-chessboard outside: B - 3N = (#unlike - #bonds)/2 + const (40 random), so at zeta = g^-3 the "
          f"weight is g^(#unlike/2) W; translation of the filled minus-cluster V by each unit d ({tried} maps): #unlike drops by "
          f"exactly |dV|, N changes by #(back in A) - #(front in A), the map is injective given V and d, and the recorded-bond graph "
          f"becomes (G - D)/F plus isolated records (F = occupied wall bonds along d, D = the other occupied wall bonds); "
          f"W ratio <= Lam^|occ wall| (Lam/m)^(5|F|) exact at (3,1,2) on {wt} maps with small clusters")


# ---------------------------------------------------------------- content algebra on small graphs (exact)
def Z0(nv, es, Mm):
    return sum((prod_M(Mm, s, es) for s in itertools.product(range(6), repeat=nv)), Fr(0))


def family_k() -> None:
    rnd = random.Random(5)
    ok = True
    worst = Fr(0)
    for (p, q, r) in ((3, 1, 2), (12, 1, 2), (5, 2, 4)):
        Mm = Mmatrix(p, q, r)
        Lam, m = max(max(rw) for rw in Mm), min(min(rw) for rw in Mm)
        for _ in range(12):
            nv = rnd.randint(3, 5)
            es = sorted({tuple(sorted(rnd.sample(range(nv), 2))) for _ in range(rnd.randint(2, 6))})
            W = Z0(nv, es, Mm) / Fr(6) ** nv
            # add a bond: factor 1 if it joins components, in [m, Lam] if it closes a cycle
            a, b = sorted(rnd.sample(range(nv), 2))
            if (a, b) in es:
                continue
            comps = components(nv, es)
            W2 = Z0(nv, es + [(a, b)], Mm) / Fr(6) ** nv
            if comps[a] != comps[b]:
                ok &= W2 == W
            else:
                ok &= m <= W2 / W <= Lam
            # identify vertices a and b (merge): factor 1 across components, 6 P(s_a = s_b) >= (m/Lam)^deg(b) within
            Z = Z0(nv, es, Mm)
            Zeq = sum((prod_M(Mm, s, es) for s in itertools.product(range(6), repeat=nv) if s[a] == s[b]), Fr(0))
            merged = [(min(x if x != b else a, y if y != b else a), max(x if x != b else a, y if y != b else a)) for x, y in es]
            relabel = {v: i for i, v in enumerate([v for v in range(nv) if v != b])}
            mes = [(relabel[x], relabel[y]) for x, y in merged if x != y]
            Wm = Z0(nv - 1, mes, Mm) / Fr(6) ** (nv - 1)
            ok &= Wm == W * 6 * Zeq / Z
            degb = sum(1 for x, y in es if b in (x, y))
            if comps[a] != comps[b]:
                ok &= Wm == W
            else:
                ok &= 6 * Zeq / Z >= (m / Lam) ** degb
                worst = max(worst, Z / (6 * Zeq))
    check("K", ok, "exact on random small graphs at (3,1,2), (12,1,2), (5,2,4): adding a bond multiplies W = Z0/6^N by exactly 1 across "
          "components and by a factor in [m, Lam] = [min M, max M] around a cycle (block 81 T1); identifying two records multiplies W "
          "by 6 P(s_u = s_v): exactly 1 across components, and at least (m/Lam)^deg within one")


def components(nv, es):
    par = list(range(nv))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for a, b in es:
        par[f(a)] = f(b)
    return [f(v) for v in range(nv)]


# ---------------------------------------------------------------- geometry of the walls
def polycubes(nmax):
    res = defaultdict(set)
    o = (0, 0, 0)
    def rec(poly, untried, forb):
        res[len(poly)].add(poly)
        if len(poly) == nmax:
            return
        untried = list(untried)
        while untried:
            c = untried.pop()
            newpoly = poly | {c}
            newforb = set(forb)
            nu = list(untried)
            for d in NB:
                nb = add(c, d)
                if nb not in newforb and nb not in poly and not nb < o and all(add(nb, e) not in poly for e in NB) and nb not in untried:
                    nu.append(nb)
                    newforb.add(nb)
            rec(newpoly, nu, newforb | {c})
            forb = forb | {c}
    su = [add(o, d) for d in NB if not add(o, d) < o]
    rec(frozenset({o}), su, set(su) | {o})
    return res


def pverts(p):
    x, a = p
    b, c = [i for i in range(3) if i != a]
    out = set()
    for sb in (-1, 1):
        for sc in (-1, 1):
            v = [2 * xi for xi in x]
            v[a] += 1
            v[b] += sb
            v[c] += sc
            out.add(tuple(v))
    return out


def pedges(p):
    vs = sorted(pverts(p))
    return {frozenset((u, w)) for u, w in itertools.combinations(vs, 2) if sum(abs(i - j) for i, j in zip(u, w)) == 2}


def conn(items, key):
    keys = [key[i] for i in items]
    seen, st = {0}, [0]
    while st:
        i = st.pop()
        for j in range(len(items)):
            if j not in seen and keys[i] & keys[j]:
                seen.add(j)
                st.append(j)
    return len(seen) == len(items)


def family_g():
    p0 = ((0, 0, 0), 0)
    cand = [((i, j, k), a) for i in range(-2, 3) for j in range(-2, 3) for k in range(-2, 3) for a in range(3)]
    dv = sum(1 for p in cand if p != p0 and pverts(p) & pverts(p0))
    de = sum(1 for p in cand if p != p0 and pedges(p) & pedges(p0))
    res = polycubes(7)
    fixed = [len(res[n]) for n in range(1, 8)]
    counts = Counter()
    badv = bade = badray = 0
    for n in range(1, 7):
        for P in res[n]:
            for c in P:
                V = frozenset(sub(x, c) for x in P)
                B = [(min(x, add(x, d)), [i for i in range(3) if d[i]][0]) for x in V for d in NB if add(x, d) not in V]
                k = len(B)
                counts[k] += 1
                kv = {p: pverts(p) for p in B}
                ke = {p: pedges(p) for p in B}
                badv += not conn(B, kv)
                bade += not conn(B, ke)
                mm = 0
                while (mm + 1, 0, 0) in V:
                    mm += 1
                badray += not (4 * (mm + 1) <= k)
    min7 = min(6 * 7 - 2 * sum(1 for x in P for d in NB if add(x, d) in P) // 2 for P in res[7])
    ck = {k: v for k, v in sorted(counts.items()) if k <= 22}
    ok = dv == 32 and de == 12 and fixed == [1, 3, 15, 86, 534, 3481, 23502] and badv == 0 and badray == 0 and min7 == 24
    check("G", ok, f"a plaquette meets {dv} others at a vertex ({de} along an edge); fixed polycubes {fixed} (n = 1..7); every V "
          f"containing the origin with at most 6 cells: boundary vertex-connected, the e1-ray exits within |dV|/4 sites; "
          f"edge-disconnected boundaries: {bade}; 7 cells need |dV| >= {min7}, so the counts of V around a site are complete to 22: "
          f"{ck}")
    return ck


# ---------------------------------------------------------------- tree counts of connected plaquette sets
def rk(D, k):
    return 1 if k == 1 else Fr(D * comb((D - 1) * k, k - 2), k - 1)


def family_r():
    ok = True
    for D in (32, 12):
        K = 30
        U = [0] * (K + 1)
        for _ in range(K + 1):
            P = [1] + [0] * K
            base = [1] + U[1:]
            for _ in range(D - 1):
                P = [sum(P[i] * base[n - i] for i in range(n + 1)) for n in range(K + 1)]
            U = [0] + P[:K]
        P = [1] + [0] * K
        base = [1] + U[1:]
        for _ in range(D):
            P = [sum(P[i] * base[n - i] for i in range(n + 1)) for n in range(K + 1)]
        R = [0] + P[:K]
        ok &= all(R[k] == rk(D, k) for k in range(1, K + 1))
        mu = Fr((D - 1) ** (D - 1), (D - 2) ** (D - 2))
        ok &= all(rk(D, k + 1) <= mu * rk(D, k) for k in range(1, 12))
        # for k >= 12 (t = 1/k <= 1/12): sum_{i<=D-1} i/(D-1+it) <= D/2 < (sum_{i=3}^{D} i)/(D-2+D t) at t = 1/12, so the ratio
        # r_{k+1}/r_k = prod(D-1+i t)/prod(D-2+i t) (t = 1/k) increases to mu as t decreases
        sN = Fr(sum(range(3, D + 1)), 1) / (D - 2 + Fr(D, 12))
        ok &= Fr(D, 2) < sN
    check("R", ok, "connected sets of k plaquettes through a given one, counted by breadth-first trees (root 32 slots, others 31): "
          "r_k = (D/(k-1)) C((D-1)k, k-2), equal to the tree series for k <= 30 (D = 32 and 12); r_{k+1} <= mu r_k with "
          "mu = (D-1)^(D-1)/(D-2)^(D-2) (82.90 for D = 32), exact for k < 12 and by a monotone ratio beyond")


# ---------------------------------------------------------------- Peierls certificates
TRIPLES = {"(3,1,2)": (3, 1, 2), "(5,2,4)": (5, 2, 4), "(12,1,2)": (12, 1, 2), "(9,8,8)": (9, 8, 8)}
G_ORDER = {"(3,1,2)": Fr(1, 10 ** 5), "(5,2,4)": Fr(18, 10 ** 6), "(12,1,2)": Fr(19, 10 ** 8), "(9,8,8)": Fr(97, 10 ** 6)}
G_HALF = {"(3,1,2)": Fr(15, 10 ** 8), "(5,2,4)": Fr(34, 10 ** 8), "(12,1,2)": Fr(16, 10 ** 11), "(9,8,8)": Fr(69, 10 ** 7),
          "content-less": Fr(5, 10 ** 6)}


def gf_bound(D, x0, Up, ck):
    """upper bound of sum_{V around a site} x0^|dV| = exact counts to 22 + generating-function tail from 24."""
    assert x0 * (1 + Up) ** (D - 1) <= Up
    den = 1 - x0 * (D - 1) * (1 + Up) ** (D - 2)
    assert den > 0
    Rp = (1 + Up) ** D + x0 * D * (1 + Up) ** (D - 1) * ((1 + Up) ** (D - 1) / den)
    tail = x0 / 4 * Rp - sum(Fr(k, 4) * rk(D, k) * x0 ** k for k in range(1, 24))
    return sum(c * x0 ** k for k, c in ck.items()) + tail


def geo_tail(D, x, K=24):
    mu = Fr((D - 1) ** (D - 1), (D - 2) ** (D - 2))
    qq = mu * x
    assert qq < 1
    return rk(D, K) * x ** K / 4 * (Fr(K) / (1 - qq) + qq / (1 - qq) ** 2)


def family_p(ck):
    x0, Up = Fr(3, 250), Fr(31, 1000)
    S = gf_bound(32, x0, Up, ck)
    ok = S < Fr(1, 2)
    lines = []
    for name, (p, q, r) in TRIPLES.items():
        Mv = [Fr(6 * p, p + q + 4 * r), Fr(6 * q, p + q + 4 * r), Fr(6 * r, p + q + 4 * r)]
        Lam, m = max(Mv), min(Mv)
        g = G_ORDER[name]
        # x = g^(1/2) Lam (Lam/m)^(5/6) <= x0  <=>  g^3 Lam^6 (Lam/m)^5 <= x0^6
        ok &= g ** 3 * Lam ** 6 * (Lam / m) ** 5 <= x0 ** 6
        lines.append(f"{name} {float(g):.2g}")
    x12, U12 = Fr(347, 10000), Fr(88, 1000)
    S12 = gf_bound(12, x12, U12, ck)
    ok &= S12 < Fr(1, 2)
    check("P", ok, f"Peierls sum around a site at x0 = 3/250 (below 30^30/31^31 = 0.012062): at most {float(S):.4f} < 1/2 "
          f"(exact counts to |dV| = 22, then tree counts through U+ = 31/1000 >= U(x0)); so the chessboard is ordered for "
          f"x = g^(1/2) Lam (Lam/m)^(5/6) H^(1/6) <= 3/250: content-less at zeta = g^-3 for g <= 9/62500 = 1.44e-4, with contents at "
          f"zeta = g^-3 for g <= " + ", ".join(lines) + f"; if walls are edge-connected (all V to 6 cells above): x0 = 347/10000, "
          f"sum <= {float(S12):.3f}, g <= 1.2e-3 content-less")


def family_h(ck):
    ok = True
    rep = []
    x0 = Fr(3, 250)
    items = list(TRIPLES.items()) + [("content-less", None)]
    for name, trip in items:
        if trip:
            p, q, r = trip
            Mv = [Fr(6 * p, p + q + 4 * r), Fr(6 * q, p + q + 4 * r), Fr(6 * r, p + q + 4 * r)]
            Lam, m = max(Mv), min(Mv)
        else:
            Lam = m = Fr(1)
        g = G_HALF[name]
        # window: H+ with H+^2 m^5 >= (11/10)^2, H- with H-^2 Lam^5 <= (9/10)^2 (rational choices)
        Hp = rational_above((Fr(11, 10) ** 2 / m ** 5), 2)
        Hm = rational_below((Fr(9, 10) ** 2 / Lam ** 5), 2)
        Hmax = max(Hp, 1 / Hm)
        # per-plaquette bound x = g^(1/2) Lam (Lam/m)^(5/6) Hmax^(1/6): take a rational xr with xr^6 >= g^3 Lam^6 (Lam/m)^5 Hmax
        target = g ** 3 * Lam ** 6 * (Lam / m) ** 5 * Hmax
        xr = rational_above(target, 6)
        T = sum(c * xr ** k for k, c in ck.items() if k >= 10) + geo_tail(32, xr)
        g3 = g ** 3
        lB = g3 * Hp * m ** 5 / (1 + g3 * Hp * m ** 5)
        uA = g3 / Hp + T
        lA = g3 / (g3 + Hm)
        uB = g3 * Hm * Lam ** 5 + T
        ok &= lB > uA and lA > uB and xr <= x0 and g * Lam <= 1
        rep.append(f"{name} {float(g):.2g}")
    check("H", ok, "half filling: on every framed box the density exceeds 1/2 at zeta = g^-3 H+ (an occupied B-site has probability "
          ">= g^3 H m^5/(1 + g^3 H m^5), a vacant A-site at most g^3/H + T) and falls below 1/2 at g^-3 H- (vacant A >= g^3/(g^3 + H), "
          "occupied B <= g^3 H Lam^5 + T), T = sum over V of >= 2 cells from exact counts and a geometric tree tail; the density rises "
          "with zeta, so the half-filling fugacity lies in [H-, H+] g^-3, where the Peierls bound holds: ordered at half filling for "
          "g <= " + ", ".join(rep))


def rational_above(v, root):
    """a rational y with y^root >= v, close to v^(1/root)."""
    y = Fr(float(v) ** (1.0 / root)).limit_denominator(10 ** 9)
    while y ** root < v:
        y *= Fr(1000001, 1000000)
    return y


def rational_below(v, root):
    y = Fr(float(v) ** (1.0 / root)).limit_denominator(10 ** 9)
    while y ** root > v:
        y *= Fr(999999, 1000000)
    return y


def main() -> None:
    t0 = time.time()
    family_q()
    family_i_t()
    family_k()
    ck = family_g()
    family_r()
    family_p(ck)
    family_h(ck)
    print("\n".join(OUT))
    print(f"families Q T K G R P H (all exact): {len(OUT) - len(FAILS)}/{len(OUT)} ok, {time.time() - t0:.0f} s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PROVED (translation route, no reflection positivity; imported: the wall's connectedness by Mayer-Vietoris) "
          "chessboard order of block 81's record gas in 3D with explicit g*: without contents at zeta = g^-3 (its half filling) for "
          "g <= 9/62500; with contents at zeta = g^-3 for g <= 1e-5 (3,1,2), 1.8e-5 (5,2,4), 1.9e-7 (12,1,2), 9.7e-5 (9,8,8), and at "
          "half filling on every framed box for g <= 1.5e-7, 3.4e-7, 1.6e-10, 6.9e-6; contents act only through occupied wall bonds")
    print("HIT: in block 81's record gas, translating the filled region of the other chessboard phase by one site (a symmetry of the "
          "gas with contents) removes exactly its |dV| unlike wall bonds, so with the A-chessboard outside a box each site is in the "
          "B phase with probability at most sum_V x^|dV| <= 0.0896 when x = g^(1/2) Lam (Lam/m)^(5/6) max(H,1/H)^(1/6) <= 3/250 at "
          "zeta = g^-3 H: without contents the chessboard is ordered at zeta = g^-3, where that gas is half filled, for g <= 9/62500 "
          "= 1.44e-4 (attempt 1: 8.0e-10); with contents at zeta = g^-3 for g <= 1e-5 at (3,1,2), and at the half-filling fugacity of "
          "every framed box for g <= 1.5e-7 at (3,1,2); contents act only through occupied wall bonds and can only raise the bound")


if __name__ == "__main__":
    main()
