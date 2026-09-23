#!/usr/bin/env python3
"""No fixed local formation order for the declared finite torus ice law.

Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. Constant-record coordinator sites remain in the declared neighbour graph; the tests do not classify all altered graphs or all maximal sets.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from itertools import product

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


N = 4


def dist(a, b):
    return sum(min((x - y) % N, (y - x) % N) for x, y in zip(a, b))


def cheb(a, b):
    return max(min((x - y) % N, (y - x) % N) for x, y in zip(a, b))


PTS = list(product(range(N), repeat=3))
ODD = lambda p: sum(c % 2 for c in p)
V = [p for p in PTS if ODD(p) == 0]
LK = [p for p in PTS if ODD(p) == 1]
PQ = [p for p in PTS if ODD(p) == 2]
CB = [p for p in PTS if ODD(p) == 3]
LIDX = {l: k for k, l in enumerate(LK)}
STAR = {v: [LIDX[l] for l in LK if dist(v, l) == 1] for v in V}


def ice_states():
    """All link patterns with exactly 3 of each vertex's 6 links occupied (backtracking)."""
    link_verts = {k: [v for v in V if k in STAR[v]] for k in range(len(LK))}
    occ, cnt, seen, out = [0] * len(LK), {v: 0 for v in V}, {v: 0 for v in V}, []

    def rec(k):
        if k == len(LK):
            if all(cnt[v] == 3 for v in V):
                out.append(tuple(occ))
            return
        for val in (0, 1):
            if any(cnt[v] + val > 3 or cnt[v] + val + (6 - seen[v] - 1) < 3 for v in link_verts[k]):
                continue
            occ[k] = val
            for v in link_verts[k]:
                cnt[v] += val
                seen[v] += 1
            rec(k + 1)
            for v in link_verts[k]:
                cnt[v] -= val
                seen[v] -= 1
        occ[k] = 0

    rec(0)
    return out


def build(states, scheme=None):
    sites = [("V", v) for v in V] + [("L", l) for l in LK] + [("P", p) for p in PQ] + [("C", c) for c in CB]
    n = len(sites)
    nb = [set() for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if dist(sites[a][1], sites[b][1]) == 1:
                nb[a].add(b)
                nb[b].add(a)
    bits = np.array(states, dtype=np.int64)
    codes, K = [], []
    for t, s in sites:
        if t == "L":
            own = [LIDX[s]]
        elif t == "V":
            own = STAR[s]
        elif t == "P":
            own = [LIDX[l] for l in LK if dist(s, l) == 1]
        else:
            own = [LIDX[l] for l in LK if cheb(s, l) == 1 and dist(s, l) == 2]
        if t != "L" and (scheme or {}).get(t) == "nothing":
            own = []
        c = np.zeros(len(states), dtype=np.int64)
        for j, e in enumerate(own):
            c |= bits[:, e] << j
        codes.append(c)
        K.append(1 << len(own))
    return {"sites": sites, "nb": nb, "codes": codes, "K": K, "M": len(states)}


def dense(keys):
    u, inv = np.unique(keys, return_inverse=True)
    return inv.astype(np.int64).ravel(), len(u)


def group_of(win, idxs):
    g = np.zeros(win["M"], dtype=np.int64)
    for s in sorted(idxs):
        g, _ = dense(g * win["K"][s] + win["codes"][s])
    return g


def admissible(win, gF, x, S):
    """Equal weights: the conditional of x given the formed groups equals its conditional given S."""
    h = group_of(win, S)
    cx, Kx = win["codes"][x], win["K"][x]
    _, first, ga = np.unique(gF * Kx + cx, return_index=True, return_inverse=True)
    ga = ga.ravel()
    ha, _ = dense(h * Kx + cx)
    Wga, Wg = np.bincount(ga), np.bincount(gF)
    Wh, Wha = np.bincount(h), np.bincount(ha)
    lhs = Wga.astype(object) * Wh[h[first]].astype(object)
    rhs = Wha[ha[first]].astype(object) * Wg[gF[first]].astype(object)
    return bool(np.all(lhs == rhs))


def closed_search(win, budget=5000):
    n, memo, seen, best = len(win["sites"]), {}, set(), [0]
    fn = lambda x, F: frozenset(k for k in win["nb"][x] if F >> k & 1)

    def is_function(y, S):
        if (y, S) not in memo:
            g = group_of(win, S)
            _, G = dense(g)
            _, P = dense(g * win["K"][y] + win["codes"][y])
            memo[(y, S)] = P == G
        return memo[(y, S)]

    def close(F):
        changed = True
        while changed:
            changed = False
            for y in range(n):
                if not F >> y & 1 and is_function(y, fn(y, F)):
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
            if not F >> x & 1 and admissible(win, gF, x, fn(x, F)):
                g2, _ = dense(gF * win["K"][x] + win["codes"][x])
                if dfs(F | (1 << x), g2):
                    return True
        return False

    try:
        found = dfs(0, np.zeros(win["M"], dtype=np.int64))
    except OverflowError:
        return None, len(seen), best[0]
    return found, len(seen), best[0]


def composition(win, F):
    comp = {}
    for k, (t, s) in enumerate(win["sites"]):
        if F >> k & 1:
            comp[t] = comp.get(t, 0) + 1
    return comp


print("A. the landed torus measure")
ICE = ice_states()
check("the 2 x 2 x 2 torus: 8 vertices, 24 links, 24 plaquette sites, 8 cube sites; 9600 ice states, as in the landed note",
      (len(V), len(LK), len(PQ), len(CB)) == (8, 24, 24, 8) and len(ICE) == 9600
      and all(len(STAR[v]) == 6 for v in V),
      "every vertex has 6 links; every state has exactly 3 occupied at every vertex")

print("B. a control with an order")
prod_states = [tuple(a) + (0,) * 12 for a in product((0, 1), repeat=12)]
ctl = build(prod_states)
cf, cs, cb = closed_search(ctl)
check("control: twelve independent fair links with the other twelve fixed are formed in order",
      cf is True and len(prod_states) == 4096, f"{cs} closed sets visited before completion")

print("C. the uniform ice measure, every coordinator present")
win = build(ICE)
f, s_, b = closed_search(win)
comp = composition(win, b)
check("no local formation order reproduces the landed measure, with all 24 plaquette and 8 cube sites",
      f is False and s_ == 65 and comp == {"L": 12, "P": 6, "C": 1},
      f"{s_} closed sets; the largest formed set has {bin(b).count('1')} sites: one cube site, its 6 plaquettes "
      "and its 12 edges, and no vertex, since every vertex star reaches outside any one cube")

print("D. coarser records and no coordinators")
rows = []
for sch in [{"V": "nothing"}, {"P": "nothing", "C": "nothing"}, {"V": "nothing", "P": "nothing", "C": "nothing"}]:
    f2, s2, b2 = closed_search(build(ICE, sch))
    rows.append((sch, f2, s2, bin(b2).count("1")))
check("vertex records carrying nothing, no coordinators, or links alone: no order either",
      all(r[1] is False for r in rows),
      "; ".join(f"{'+'.join(sorted(r[0]))} nothing: {r[2]} closed sets, largest {r[3]}" for r in rows))

print('per_element: Integer configurations, weights and conditional cross-products are exact within the stated finite alphabets; floating spectral estimates are labelled.')
print('per_site: Site and unit tests use the declared records, neighbour graph, boundary conditions and fixed formation orders only.')
print('per_mode: Transfer and walk modes refer to supplied finite matrices; numerical estimates do not establish untested physical or infinite-cross-section limits.')
print('per_block: This bounded support result retains its explicit controls, parameter values and search caps; alternative rules and records remain outside scope.')
print('lattice_wide: Finite windows do not establish universal formation impossibility; infinite-height statements apply only to the specified fixed-cross-section transfer model.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
