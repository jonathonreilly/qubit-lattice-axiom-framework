#!/usr/bin/env python3
"""J:attack-g:PR8150 — brute-force the normalizer lemma and the cycle lemma.

Not the executed flip-count census (already an attack-c script).

Normalizer lemma (re-proved in the note, used by X1): for k>=2,
  K_k(b,...,b) - K_k(-b,b,...,b) = ((p-q)/Z1) * ((p/Z1)^{k-1} - (q/Z1)^{k-1})
  K_k(b,...,b) - K_k(c,b,...,b)  = [ (p-r)(p^{k-1}-r^{k-1}) + (q-r)(q^{k-1}-r^{k-1}) ] / Z1^k
with K_k(a,b,...,b) = Σ_s K(a,s) K(b,s)^{k-1}, K=φ/Z1.

Cycle lemma (X2 corollary): on a window containing a cycle, every order has
a site with |A_x|>=2 (the last cycle vertex to form, which already has both
cycle-neighbours recorded). Z^3 is bipartite: no triangles.

HIT if a closed form fails at any k=2..8, or any order on a cyclic window
has all |A_x|<=1, or the last vertex of a simple cycle does not record both
cycle neighbours, or a cycle-free path has no qualifying order.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def K(s, t, p, q, r, Z1):
    return phi(s, t, p, q, r) / Z1


def Kk(rec, p, q, r, Z1):
    tot = Fraction(0)
    for s in AXES:
        w = Fraction(1)
        for a in rec:
            w *= K(a, s, p, q, r, Z1)
        tot += w
    return tot


def normalizer_checks():
    hits = []
    triples = [(3, 1, 2), (5, 2, 4), (7, 3, 5), (4, 4, 1), (10, 1, 2)]
    b = AXES[0]
    mb = AXES[1]
    c = AXES[2]
    for p, q, r in triples:
        p, q, r = Fraction(p), Fraction(q), Fraction(r)
        Z1 = p + q + 4 * r
        assert Z1 == sum(phi(b, s, p, q, r) for s in AXES)
        for k in range(2, 9):
            rec_b = (b,) * k
            rec_m = (mb,) + (b,) * (k - 1)
            rec_c = (c,) + (b,) * (k - 1)
            left_m = Kk(rec_b, p, q, r, Z1) - Kk(rec_m, p, q, r, Z1)
            right_m = ((p - q) / Z1) * ((p / Z1) ** (k - 1) - (q / Z1) ** (k - 1))
            if left_m != right_m:
                hits.append(f"HIT: antipodal normalizer k={k} {(p,q,r)} {left_m} vs {right_m}")
                print("HIT:", hits[-1])
            left_c = Kk(rec_b, p, q, r, Z1) - Kk(rec_c, p, q, r, Z1)
            right_c = (
                (p - r) * (p ** (k - 1) - r ** (k - 1))
                + (q - r) * (q ** (k - 1) - r ** (k - 1))
            ) / Z1 ** k
            if left_c != right_c:
                hits.append(f"HIT: ortho normalizer k={k} {(p,q,r)} {left_c} vs {right_c}")
                print("HIT:", hits[-1])
            if p != q and left_m <= 0:
                hits.append(f"HIT: antipodal gap not >0 at k={k} {(p,q,r)} {left_m}")
                print("HIT:", hits[-1])
            if not (p == q == r) and left_c <= 0:
                hits.append(f"HIT: ortho gap not >0 at k={k} {(p,q,r)} {left_c}")
                print("HIT:", hits[-1])
        print(f"normalizer lemma (3,1,2)-style {(p,q,r)} k=2..8: gaps and closed forms checked")
    return hits


def neighbors_from_pos(pos):
    sites = list(pos)
    nb = {i: [] for i in sites}
    for i, j in product(sites, repeat=2):
        if i >= j:
            continue
        d = sum(abs(pos[i][k] - pos[j][k]) for k in range(3))
        if d == 1:
            nb[i].append(j)
            nb[j].append(i)
    return nb


def recorded(order, nb):
    pos = {x: i for i, x in enumerate(order)}
    return {x: [y for y in nb[x] if pos[y] < pos[x]] for x in order}


def simple_cycles(nb):
    """Undirected simple cycles of length >=4 (bipartite)."""
    sites = list(nb)
    found = set()
    def dfs(start, cur, path, seen):
        for nxt in nb[cur]:
            if nxt == start and len(path) >= 4:
                # canonical rotation/reflection
                rot = tuple(path)
                cand = min(rot[i:] + rot[:i] for i in range(len(rot)))
                rev = tuple(reversed(rot))
                cand_r = min(rev[i:] + rev[:i] for i in range(len(rev)))
                found.add(min(cand, cand_r))
            elif nxt not in seen and nxt >= start:
                dfs(start, nxt, path + [nxt], seen | {nxt})
    for s in sites:
        dfs(s, s, [s], {s})
    return found


def cycle_lemma_window(name, pos, expect_cycle):
    hits = []
    nb = neighbors_from_pos(pos)
    sites = list(pos)
    cycles = simple_cycles(nb)
    has_cycle = bool(cycles)
    if has_cycle != expect_cycle:
        hits.append(f"HIT: {name} cycle presence {has_cycle} vs expected {expect_cycle}")
        print("HIT:", hits[-1])
    n_qual = 0
    n_ord = 0
    last_fail = 0
    for order in permutations(sites):
        n_ord += 1
        A = recorded(order, nb)
        qual = all(len(A[x]) <= 1 for x in sites)
        if qual:
            n_qual += 1
        rank = {x: i for i, x in enumerate(order)}
        for cyc in cycles:
            last = max(cyc, key=lambda x: rank[x])
            i = cyc.index(last)
            n1, n2 = cyc[(i - 1) % len(cyc)], cyc[(i + 1) % len(cyc)]
            if n1 not in A[last] or n2 not in A[last]:
                last_fail += 1
                if last_fail <= 3:
                    hits.append(
                        f"HIT: {name} last vertex {last} of cycle {cyc} does not record both neighbours {n1,n2} in order {order}"
                    )
                    print("HIT:", hits[-1])
    if expect_cycle and n_qual:
        hits.append(f"HIT: {name} has a cycle but {n_qual}/{n_ord} orders qualify (all |A|<=1)")
        print("HIT:", hits[-1])
    if (not expect_cycle) and n_qual == 0:
        hits.append(f"HIT: {name} is cycle-free but no order qualifies")
        print("HIT:", hits[-1])
    print(f"{name}: sites={len(sites)} orders={n_ord} cycles={len(cycles)} qualifying={n_qual} last-fails={last_fail}")
    return hits, n_qual, n_ord


def main():
    hits = normalizer_checks()

    # path of 3 (cycle-free): 4 of 6 qualify
    path = {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0)}
    h, nq, no = cycle_lemma_window("path3", path, False)
    hits.extend(h)
    if nq != 4 or no != 6:
        hits.append(f"HIT: path3 qualifying {nq}/{no} != 4/6")
        print("HIT:", hits[-1])

    # four-leaf star: 48 of 120
    star = {0: (0, 0, 0), 1: (1, 0, 0), 2: (-1, 0, 0), 3: (0, 1, 0), 4: (0, -1, 0)}
    h, nq, no = cycle_lemma_window("star4", star, False)
    hits.extend(h)
    if nq != 48 or no != 120:
        hits.append(f"HIT: star4 qualifying {nq}/{no} != 48/120")
        print("HIT:", hits[-1])

    # plaquette C4
    plaq = {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0)}
    h, nq, no = cycle_lemma_window("plaquette", plaq, True)
    hits.extend(h)
    if nq != 0 or no != 24:
        hits.append(f"HIT: plaquette qualifying {nq}/{no} (want 0/24)")
        print("HIT:", hits[-1])

    # 2x3 grid
    grid = {i: (i % 3, i // 3, 0) for i in range(6)}
    h, nq, no = cycle_lemma_window("grid2x3", grid, True)
    hits.extend(h)
    if nq != 0:
        hits.append(f"HIT: 2x3 qualifying {nq}/{no} (want 0)")
        print("HIT:", hits[-1])

    # cube
    cube = {i: ((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)}
    h, nq, no = cycle_lemma_window("cube", cube, True)
    hits.extend(h)
    if nq != 0:
        hits.append(f"HIT: cube qualifying {nq}/{no} (want 0)")
        print("HIT:", hits[-1])

    if hits:
        print("SUMMARY: normalizer lemma or cycle lemma fails under brute force")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the normalizer lemma closed "
        "forms hold exactly for k=2..8 at five weight triples, and the cycle lemma "
        "holds on the plaquette (0/24 qualify), 2x3 and cube (0 qualify; last cycle "
        "vertex always records both neighbours), while the path of three (4/6) and "
        "four-leaf star (48/120) have qualifying orders as stated"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
