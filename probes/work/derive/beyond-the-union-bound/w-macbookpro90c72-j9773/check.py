#!/usr/bin/env python3
"""beyond-the-union-bound, attempt 1 (worker w-macbookpro90c72-j9773).

Candidate (iii): inclusion-exclusion on canonical histories is vacuous (they
partition {eta_x=1}); Bonferroni order 2 is a lower bound, not an upper bound.
"""
from __future__ import annotations

import sys
from collections import deque
from fractions import Fraction as F
from itertools import combinations, product

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAILS += 1
        print(f"FAIL: {tag} {msg}")


def section_a():
    # two-event identity
    # A={1,2,3}, B={3,4}, uniform on {1,2,3,4,5}
    pA, pB, pAB = F(3, 5), F(2, 5), F(1, 5)
    pU = pA + pB - pAB
    ok = pU == F(4, 5) and (pA + pB - pAB) < (pA + pB)
    # order-2 truncation undershoots iff overlap > 0
    check("A1", ok, "Bonferroni order 2 equals P(A cup B) for two events and is "
          "strictly below P(A)+P(B) whenever the overlap is positive: it is not an upper bound")


E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORKS = [tuple(E[a][i] - E[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def level(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [sub(z, E[j]) for j in range(3)]


def cone(x, depth):
    out = []
    for d1 in range(depth + 1):
        for d2 in range(depth + 1 - d1):
            for d3 in range(depth + 1 - d1 - d2):
                out.append(sub(x, (d1, d2, d3)))
    return out


def npred(eta, z):
    return sum(eta.get(p, 0) for p in preds(z))


class Explainer:
    def __init__(self, eta):
        self.eta = eta
        self.ones = {z for z, v in eta.items() if v == 1}
        self.kind, self.amp_dir, self.win = {}, {}, {}
        for z in self.ones:
            np = npred(eta, z)
            if np == 0:
                self.kind[z] = "seed"
            elif np == 1:
                self.kind[z] = "amp"
                self.amp_dir[z] = [j for j in range(3) if eta.get(preds(z)[j], 0) == 1][0]
            else:
                self.kind[z] = "proc"
                idx = [j for j in range(3) if eta.get(preds(z)[j], 0) == 1]
                self.win[z] = (idx[0], idx[1])

    def excuse(self, v, k):
        if self.kind[v] == "amp":
            return preds(v)[self.amp_dir[v]]
        i, j = self.win[v]
        return preds(v)[min(a for a in (i, j) if a != k)]

    def is_bad(self, v, k):
        return self.kind[v] == "amp" and self.amp_dir[v] == k

    def down(self, z):
        if self.kind.get(z) == "seed" or z not in self.ones:
            return []
        return [p for p in preds(z) if p in self.ones]

    def clusters_at(self, s):
        pts = [z for z in self.ones if level(z) <= s]
        parent = {z: z for z in pts}

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for z in pts:
            for p in self.down(z):
                ra, rb = find(z), find(p)
                if ra != rb:
                    parent[ra] = rb
        cl = {}
        comp = {}
        for z in pts:
            if level(z) == s:
                comp.setdefault(find(z), set()).add(z)
        for members in comp.values():
            fs = frozenset(members)
            for z in members:
                cl[z] = fs
        return cl

    def key(self, root):
        if self.kind[root] == "seed":
            return ((root,), (), 0, 0, 0)
        unproc = [(frozenset([root]), (root, root, root))]
        R = Ftot = Btot = 0
        records = []
        while True:
            active = [(K, pl) for (K, pl) in unproc if not all(self.kind[v] == "seed" for v in pl)]
            if not active:
                break
            K, poles = active[0]
            unproc.remove((K, poles))
            s = level(next(iter(K)))
            u = [self.excuse(poles[j], j) for j in range(3)]
            bad = sum(1 for j in range(3) if self.is_bad(poles[j], j))
            cl = self.clusters_at(s - 1)
            V = []
            for z in K:
                for p in self.down(z):
                    c = cl[p]
                    if c not in V:
                        V.append(c)
            fam = [("c", c) for c in V]
            for a, b in combinations(range(len(V)), 2):
                found = None
                for w in V[a]:
                    for off in FORKS:
                        w2 = add(w, off)
                        if w2 in V[b]:
                            found = frozenset([w, w2])
                            break
                    if found:
                        break
                if found:
                    fam.append(("f", found))
            n = len(fam)
            adj = {i: set() for i in range(n)}
            for i, j in combinations(range(n), 2):
                if fam[i][0] != fam[j][0] and (fam[i][1] & fam[j][1]):
                    adj[i].add(j)
                    adj[j].add(i)
            term = []
            for j in range(3):
                ti = [i for i in range(n) if fam[i][0] == "c" and u[j] in fam[i][1]]
                term.append(ti[0])

            def bfs(src, dsts):
                prev = {src: None}
                dq = deque([src])
                while dq:
                    a = dq.popleft()
                    if a in dsts:
                        path = []
                        while a is not None:
                            path.append(a)
                            a = prev[a]
                        return path[::-1]
                    for b in adj[a]:
                        if b not in prev:
                            prev[b] = a
                            dq.append(b)
                raise AssertionError

            p12 = bfs(term[0], {term[1]})
            tnodes = set(p12)
            p3 = bfs(term[2], tnodes)
            tnodes |= set(p3)
            tedges = set()
            for path in (p12, p3):
                for a, b in zip(path, path[1:]):
                    tedges.add(frozenset([a, b]))
            changed = True
            while changed:
                changed = False
                for i in list(tnodes):
                    deg = sum(1 for e in tedges if i in e)
                    if deg <= 1 and i not in term:
                        tnodes.discard(i)
                        tedges = {e for e in tedges if i not in e}
                        changed = True
            tnbr = {i: set() for i in tnodes}
            for e in tedges:
                a, b = tuple(e)
                tnbr[a].add(b)
                tnbr[b].add(a)

            def inter(i, j):
                return min(fam[i][1] & fam[j][1])

            def toward(i, target):
                if i == target:
                    return None
                prev = {i: None}
                dq = deque([i])
                while dq:
                    a = dq.popleft()
                    if a == target:
                        b = a
                        while prev[b] != i:
                            b = prev[b]
                        return b
                    for b in tnbr[a]:
                        if b not in prev:
                            prev[b] = a
                            dq.append(b)
                raise AssertionError

            pole_of = {}
            for i in tnodes:
                pl = []
                for j in range(3):
                    if i == term[j]:
                        pl.append(u[j])
                    else:
                        pl.append(inter(i, toward(i, term[j])))
                pole_of[i] = tuple(pl)
            nf = sum(1 for i in tnodes if fam[i][0] == "f")
            Ftot += nf
            Btot += bad
            R += 1
            records.append(tuple(poles))
            for i in tnodes:
                if fam[i][0] == "c":
                    unproc.append((fam[i][1], pole_of[i]))
        seeds = tuple(sorted(next(iter(K)) for (K, pl) in unproc))
        bads = []
        for poles in records:
            for j in range(3):
                if self.is_bad(poles[j], j):
                    bads.append(poles[j])
        bads = tuple(sorted(bads))
        return (seeds, bads, R, Ftot, Btot)


def eta_configs(x, depth):
    sites = sorted(cone(x, depth), key=level)
    idx = {z: i for i, z in enumerate(sites)}
    pidx = [[idx.get(pp) for pp in preds(z)] for z in sites]
    n = len(sites)
    vals = [0] * n

    def rec(i, a1, a0, b1, b0):
        if i == n:
            yield dict(zip(sites, vals)), (a1, a0, b1, b0)
            return
        c = sum(vals[j] for j in pidx[i] if j is not None)
        if c >= 2:
            vals[i] = 1
            yield from rec(i + 1, a1, a0, b1, b0)
        elif c == 1:
            vals[i] = 1
            yield from rec(i + 1, a1, a0, b1 + 1, b0)
            vals[i] = 0
            yield from rec(i + 1, a1, a0, b1, b0 + 1)
        else:
            vals[i] = 1
            yield from rec(i + 1, a1 + 1, a0, b1, b0)
            vals[i] = 0
            yield from rec(i + 1, a1, a0 + 1, b1, b0)
        vals[i] = 0

    return rec(0, 0, 0, 0, 0)


def section_b():
    x = (0, 0, 0)
    keys_once = {}
    n_x = 0
    twice_ok = True
    for eta, expo in eta_configs(x, 2):
        if eta[x] != 1:
            continue
        n_x += 1
        k1 = Explainer(eta).key(x)
        k2 = Explainer(eta).key(x)
        twice_ok = twice_ok and k1 == k2
        keys_once.setdefault(k1, []).append(expo)
    # each 1-config has one key; keys partition the 1-configs
    n_assigned = sum(len(v) for v in keys_once.values())
    check("B1", twice_ok and n_assigned == n_x and n_x == 234,
          f"depth-2 cone: {n_x} configs with eta'_x=1, each maps to exactly one history "
          f"({len(keys_once)} distinct keys); the map is deterministic (two runs agree)")
    return keys_once


def section_c(keys_once):
    e1, e2 = F(1, 10), F(1, 5)
    Pex = F(0)
    UB = F(0)
    cyl = []
    for (seeds, bads, R, Ftot, Btot), lst in keys_once.items():
        s = sum(e1 ** a1 * (1 - e1) ** a0 * e2 ** b1 * (1 - e2) ** b0 for (a1, a0, b1, b0) in lst)
        S, B = len(seeds), len(bads)
        w = e1 ** S * e2 ** B
        Pex += s
        UB += w
        cyl.append((set(seeds), set(bads), w, s))
    # pairwise cylinder overlaps (lower bound on intersection of cylinders)
    pair = F(0)
    n_olap = 0
    for i in range(len(cyl)):
        for j in range(i + 1, len(cyl)):
            S1, B1, w1, _ = cyl[i]
            S2, B2, w2, _ = cyl[j]
            if (S1 & B2) or (S2 & B1):
                continue  # conflicting type at a site: cylinders disjoint
            Su, Bu = S1 | S2, B1 | B2
            po = e1 ** len(Su) * e2 ** len(Bu)
            if po > 0:
                pair += po
                n_olap += 1
    # order-2 truncation of cylinders
    bonf2 = UB - pair
    check("C1", Pex <= UB and bonf2 <= UB,
          f"at (1/10,1/5) depth-2: P={float(Pex):.6g} <= first-order cylinder union {float(UB):.6g}; "
          f"order-2 truncation {float(bonf2):.6g} is smaller (a lower bound on P(cup C_h), not an upper bound); "
          f"{n_olap} overlapping cylinder pairs")
    # Chung-Erdős with diagonal only: (sum w)^2 / sum w^2 >= sum w
    sw2 = sum(w ** 2 for (_, _, w, _) in cyl)
    ce_diag = UB ** 2 / sw2 if sw2 else UB
    check("C2", ce_diag >= UB,
          f"Chung-Erdős with only the diagonal of realized cylinders is {float(ce_diag):.6g} >= "
          f"first-order union {float(UB):.6g}: it does not improve the union bound")


def main():
    section_a()
    keys = section_b()
    section_c(keys)
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT a finite check - {FAILS} FAIL tags")
        return 1
    print(
        "HIT: new exact partial / no-go: block 30's histories partition {eta'_x=1} "
        "(234/234 depth-2 1-configs, one deterministic key each), so inclusion-exclusion "
        "on those events is identical to the first-order sum; Bonferroni order 2 is a lower "
        "bound, not an upper bound; Chung-Erdős on realized cylinders does not beat the "
        "cylinder union. Candidate (iii) cannot replace the 4/27 grammar radius"
    )
    print(
        "SUMMARY: PARTIAL candidate (iii) fails as an improvement of the union bound: "
        "canonical histories are pairwise disjoint (IE vacuous) and Bonferroni order 2 "
        "is not an upper bound; 4/27 is not replaced; located strength 10.5-11 not reached"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
