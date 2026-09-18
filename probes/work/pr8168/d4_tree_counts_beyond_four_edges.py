#!/usr/bin/env python3
"""J:falsifier:PR8168 - block 25 (PR #8168), falsifier bullet D4: "a tree count above the recursion's coefficient, two trees with the same
lift, or a coefficient disagreeing with the direct enumeration".  The runner counts the subtrees of G with at most four edges (66103);
here the count runs to K_MAX edges, with an enumerator of our own:

Objects (the note's).  G on Z^3: arrows {x, x - e_j} and forks {x, x + e_i - e_j} (i != j); degree 12.  The family counted in T5: subtrees
of G containing the origin with at most one arrow to a predecessor at each node (an arrow {v, v - e_j} is an arrow of v to a predecessor).
a = #arrows, f = #forks.  The typed tree: words in the twelve types (down j, up j, fork (i,j)) with no letter followed by its reversal;
admissible subtrees: a vertex entered by an up letter has no down child, every other vertex (root included) at most one down child.
The recursion D_{h+1} = (1 + t U_h)^2 (1 + 3t D_h)(1 + s F_h)^6, U_{h+1} = (1 + t U_h)^3 (1 + s F_h)^6,
F_{h+1} = (1 + t U_h)^3 (1 + 3t D_h)(1 + s F_h)^5, R = (1 + t U)^3 (1 + 3t D)(1 + s F)^6 counts the admissible subtrees by t^a s^f.

Machinery.  (1) The coefficients of R up to total degree K_MAX by iterating the recursion on truncated bivariate polynomials (exact
integers).  (2) The lattice subtrees enumerated as rooted embedded trees: the root is the origin; each node, processed in breadth-first
order, chooses the set of its child edges among its free slots (the edge types other than the one back to its parent), subject to the
predecessor-arrow condition (#down children + [entered by an up letter] <= 1), the edge budget, and injectivity (every child site new and
distinct); every subtree of G containing the origin arises exactly once (its children sets are forced).  The same enumerator without the
injectivity condition counts the admissible subtrees of the typed tree directly (a check of (1)); the lift of each lattice tree (its
set of words, stored as a 128-bit digest) is collected for the smaller sizes and tested for collisions (a digest collision would be
reported as a lift collision; its probability is below 10^-25).
HIT if a lattice count exceeds the coefficient at some (a, f), two lattice trees share a lift, or the direct typed count differs from the
recursion's coefficient.  Deterministic, exact integers.
"""
import hashlib
import sys
import time
from collections import defaultdict

K_MAX = 6            # total edges a + f
K_LIFT = 5           # lifts collected (and tested for collisions) up to this many edges

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
TYPES = []           # (name, displacement, kind, reversal index)
for j in range(3):
    TYPES.append((f"down{j}", tuple(-c for c in E[j]), "down"))
for j in range(3):
    TYPES.append((f"up{j}", E[j], "up"))
for i in range(3):
    for j in range(3):
        if i != j:
            TYPES.append((f"fork{i}{j}", tuple(E[i][k] - E[j][k] for k in range(3)), "fork"))
REV = {}
for a, (na, da, ka) in enumerate(TYPES):
    for b, (nb, db, kb) in enumerate(TYPES):
        if all(x == -y for x, y in zip(da, db)) and (ka, kb) in (("down", "up"), ("up", "down"), ("fork", "fork")):
            REV[a] = b
assert len(TYPES) == 12 and len(REV) == 12


# ------------------------------------------------------------------------------------------------------------------ (1) the recursion
def pmul(A, B, K):
    C = defaultdict(int)
    for (a1, f1), c1 in A.items():
        for (a2, f2), c2 in B.items():
            if a1 + a2 + f1 + f2 <= K:
                C[(a1 + a2, f1 + f2)] += c1 * c2
    return dict(C)


def ppow(A, n, K):
    R = {(0, 0): 1}
    for _ in range(n):
        R = pmul(R, A, K)
    return R


def padd(*As):
    C = defaultdict(int)
    for A in As:
        for k, v in A.items():
            C[k] += v
    return dict(C)


def shift(A, da, df, c, K):
    return {(a + da, f + df): v * c for (a, f), v in A.items() if a + da + f + df <= K}


def recursion_coefficients(K):
    one = {(0, 0): 1}
    D = U = F = dict(one)
    for _ in range(K + 1):                      # height K suffices for total degree K
        tU = padd(one, shift(U, 1, 0, 1, K))
        tD = padd(one, shift(D, 1, 0, 3, K))
        sF = padd(one, shift(F, 0, 1, 1, K))
        D2 = pmul(pmul(ppow(tU, 2, K), tD, K), ppow(sF, 6, K), K)
        U2 = pmul(ppow(tU, 3, K), ppow(sF, 6, K), K)
        F2 = pmul(pmul(ppow(tU, 3, K), tD, K), ppow(sF, 5, K), K)
        D, U, F = D2, U2, F2
    tU = padd(one, shift(U, 1, 0, 1, K))
    tD = padd(one, shift(D, 1, 0, 3, K))
    sF = padd(one, shift(F, 0, 1, 1, K))
    return pmul(pmul(ppow(tU, 3, K), tD, K), ppow(sF, 6, K), K)


# ------------------------------------------------------------------------------------------------------------------ (2) enumeration
def enumerate_trees(K, injective, collect_lifts=0):
    """count rooted trees (lattice-embedded if injective) by (a, f) up to K edges; optionally collect lifts (frozensets of words)."""
    counts = defaultdict(int)
    lifts = defaultdict(set)
    lift_collisions = 0
    origin = (0, 0, 0)

    def children_choices(entry_type, budget):
        """all admissible child-type sets for a node entered by entry_type (None for the root), size <= budget."""
        banned = REV[entry_type] if entry_type is not None else None
        slots = [ti for ti in range(12) if ti != banned]
        entered_up = entry_type is not None and TYPES[entry_type][2] == "up"
        out = []

        def rec(i, chosen, downs):
            if i == len(slots):
                out.append(tuple(chosen))
                return
            rec(i + 1, chosen, downs)
            if len(chosen) < budget:
                ti = slots[i]
                if TYPES[ti][2] == "down":
                    if entered_up or downs >= 1:
                        return
                    chosen.append(ti)
                    rec(i + 1, chosen, downs + 1)
                    chosen.pop()
                else:
                    chosen.append(ti)
                    rec(i + 1, chosen, downs)
                    chosen.pop()
        rec(0, [], 0)
        return out

    cache = {}

    def choices(entry, budget):
        key = (entry, budget)
        if key not in cache:
            cache[key] = children_choices(entry, budget)
        return cache[key]

    def expand(queue, qi, used, edges, a, f, words):
        # queue: list of (site, entry_type, word); process node queue[qi]
        if qi == len(queue):
            counts[(a, f)] += 1
            if collect_lifts and a + f <= collect_lifts:
                lifts[(a, f)].add(hashlib.blake2b(repr(sorted(words)).encode(), digest_size=16).digest())   # 128-bit digest of the word set
            return
        site, entry, word = queue[qi]
        budget = K - edges
        for ch in choices(entry, budget):
            new_sites = []
            ok = True
            na, nf = a, f
            for ti in ch:
                d = TYPES[ti][1]
                ns = (site[0] + d[0], site[1] + d[1], site[2] + d[2])
                if injective and (ns in used or ns in new_sites):
                    ok = False
                    break
                new_sites.append(ns)
                if TYPES[ti][2] == "fork":
                    nf += 1
                else:
                    na += 1
            if not ok:
                continue
            added = [(ns, ti, word + (ti,)) for ns, ti in zip(new_sites, ch)]
            for ns in new_sites:
                used.add(ns) if injective else None
            queue.extend(added)
            expand(queue, qi + 1, used, edges + len(ch), na, nf, words + [w for _, _, w in added] if collect_lifts else words)
            del queue[len(queue) - len(added):]
            if injective:
                for ns in new_sites:
                    used.discard(ns)

    expand([(origin, None, ())], 0, {origin}, 0, 0, 0, [()])
    if collect_lifts:
        total = sum(counts[k] for k in counts if k[0] + k[1] <= collect_lifts)
        distinct = sum(len(v) for v in lifts.values())
        lift_collisions = total - distinct
    return dict(counts), lift_collisions


def main():
    t0 = time.time()
    coef = recursion_coefficients(K_MAX)
    print(f"== (1) recursion coefficients up to total degree {K_MAX} ({time.time() - t0:.1f}s)")
    t1 = time.time()
    typed, _ = enumerate_trees(min(K_MAX, 5), injective=False)
    agree_typed = all(typed.get(k, 0) == coef.get(k, 0) for k in set(typed) | {k for k in coef if sum(k) <= min(K_MAX, 5)})
    print(f"[1] direct enumeration of admissible typed subtrees up to {min(K_MAX, 5)} edges vs the recursion: agree at every (a, f): {agree_typed} "
          f"({sum(typed.values())} typed subtrees, {time.time() - t1:.1f}s)")
    t2 = time.time()
    lat, collisions = enumerate_trees(K_MAX, injective=True, collect_lifts=K_LIFT)
    print(f"== (2) lattice subtrees of G containing the origin with at most one arrow to a predecessor per node, up to {K_MAX} edges "
          f"({time.time() - t2:.0f}s)")
    over = []
    for k in range(K_MAX + 1):
        tot_l = sum(v for (a, f), v in lat.items() if a + f == k)
        tot_c = sum(v for (a, f), v in coef.items() if a + f == k)
        cells = sorted((a, f) for (a, f) in set(lat) | set(coef) if a + f == k)
        for c in cells:
            if lat.get(c, 0) > coef.get(c, 0):
                over.append((c, lat.get(c, 0), coef.get(c, 0)))
        ratio = tot_l / tot_c if tot_c else 1.0
        print(f"[2] {k} edges: {tot_l} lattice trees vs {tot_c} typed (recursion) = ratio {ratio:.4f}; by (a, f): "
              + ", ".join(f"({a},{f}): {lat.get((a, f), 0)}/{coef.get((a, f), 0)}" for a, f in cells))
    cum4 = sum(v for (a, f), v in lat.items() if a + f <= 4)
    print(f"[2] cumulative lattice trees with at most four edges: {cum4} (the note: 66103); lifts collected up to {K_LIFT} edges: "
          f"{collisions} collisions")
    print(f"[time] {time.time() - t0:.0f}s")
    if over:
        print(f"HIT: D4 - lattice tree count above the recursion's coefficient at {over[:6]}")
    if collisions:
        print(f"HIT: D4 - {collisions} pairs of lattice trees share a lift")
    if not agree_typed:
        print("HIT: D4 - the direct typed enumeration disagrees with the recursion's coefficients")
    print(f"SUMMARY: D4 beyond four edges: lattice subtree counts up to {K_MAX} edges ({sum(lat.values())} trees; {cum4} with <= 4 edges, note 66103) "
          f"never exceed the recursion's coefficients ({len(over)} cells above); lift collisions up to {K_LIFT} edges: {collisions}; typed enumeration "
          f"matches the recursion to {min(K_MAX, 5)} edges: {agree_typed}; falsifier {'FIRES' if (over or collisions or not agree_typed) else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
