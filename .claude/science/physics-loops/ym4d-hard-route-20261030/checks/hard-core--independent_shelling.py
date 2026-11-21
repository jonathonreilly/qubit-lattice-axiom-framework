#!/usr/bin/env python3
"""A shelling of every good local pattern, for the chart gauge of library/lattice_sobolev_box_gauge.md, Lemma 7.

A chart at a vertex of the cell lattice is a union of orthant boxes, one for each kept cell in a component of the local pattern. It gets a
gauge by adding orthants one at a time, and the new orthant z is joined to the earlier part by reflection. That needs the earlier part
near z to be a full subcube minus z: if I is the set of directions in which z has an earlier neighbour, then z + J must be earlier for
every non-empty J in I. Then the orthants z + J, with z, form a lattice box, on which a gauge exists, and the extension from that
box minus z to z is the folding map q -> q - 2 min_{i in I}(q_i) 1_I, which is continuous, of bounded multiplicity, and into the known part.
Call an order with this property at each step a SHELLING.

Claim tested, by exhaustion, exact: every component of every pattern S in Q_4 that is good at the vertex and on all 8 facets (each facet of Q_4 is
the pattern of an edge of the cell complex, at one end) has a shelling.

Pre-registered criteria, written before the first run.
    PASS-SHELL: every such component has a shelling.
    FAIL-SHELL: some do not. Then list them, and Lemma 7 needs something else at those patterns.
The search is a depth-first search over subsets with memoisation, so a negative answer is also exact.

Result of the first run, under a confirmed lock: FAIL-SHELL as registered, on one class only: 8 patterns, all of Q_4 with an antipodal pair removed. So that
pattern is declared bad and filled (Text 3.2), and then every component of every good pattern has a shelling. This is an exact statement.

Run under the numeric lock, nice, RSS checked against 2 GB.
"""
import importlib.util
import pathlib
import sys
import time

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("patterns", HERE.with_name("hard-core--independent_patterns.py"))
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)

D = 4
SIZE = 2**D


def facets_good(mask, bad3):
    for axis in range(D):
        others = [i for i in range(D) if i != axis]
        for side in (0, 1):
            m3 = 0
            for k in range(8):
                v = side << axis
                for j, i in enumerate(others):
                    if k >> j & 1:
                        v |= 1 << i
                if mask >> v & 1:
                    m3 |= 1 << k
            if m3 in bad3:
                return False
    return True


def components(mask):
    comps = []
    seen = 0
    for v in range(SIZE):
        if mask >> v & 1 and not seen >> v & 1:
            comp = 0
            stack = [v]
            while stack:
                x = stack.pop()
                if comp >> x & 1:
                    continue
                comp |= 1 << x
                for i in range(D):
                    y = x ^ (1 << i)
                    if mask >> y & 1 and not comp >> y & 1:
                        stack.append(y)
            comps.append(comp)
            seen |= comp
    return comps


def can_add(cur, z):
    """z may be added to the set cur: earlier neighbours I non-empty, and all z + J earlier."""
    I = [i for i in range(D) if cur >> (z ^ (1 << i)) & 1]
    if not I:
        return False
    n = len(I)
    for sub in range(1, 2**n):
        y = z
        for k in range(n):
            if sub >> k & 1:
                y ^= 1 << I[k]
        if not cur >> y & 1:
            return False
    return True


def has_shelling(comp):
    verts = [v for v in range(SIZE) if comp >> v & 1]
    if len(verts) == 1:
        return True
    memo = {}

    def dfs(cur):
        if cur == comp:
            return True
        if cur in memo:
            return memo[cur]
        res = False
        for z in verts:
            if not cur >> z & 1 and can_add(cur, z):
                if dfs(cur | 1 << z):
                    res = True
                    break
        memo[cur] = res
        return res

    # the start can be any vertex; by symmetry of the condition try all
    for v in verts:
        if dfs(1 << v):
            return True
    return False


def main():
    bad3, _ = pm.bad_table(3)
    bad4, _ = pm.bad_table(4)
    t0 = time.time()
    seen_comp = {}
    fails = []
    n_patterns = 0
    n_comps = 0
    for mask in range(1, 2**SIZE):
        if mask in bad4 or not facets_good(mask, bad3):
            continue
        n_patterns += 1
        for comp in components(mask):
            n_comps += 1
            if comp not in seen_comp:
                seen_comp[comp] = has_shelling(comp)
                if not seen_comp[comp]:
                    fails.append(comp)
    pm.check_rss()
    print(f"good patterns (vertex and facets): {n_patterns}, components: {n_comps}, distinct: {len(seen_comp)}, t={time.time()-t0:.0f}", flush=True)
    print(f"without a shelling: {len(fails)}")
    if fails:
        reps = sorted({pm.canon(f, 4) for f in fails})
        print(f"classes: {len(reps)}; sizes and reps: {[(bin(r).count('1'), r) for r in reps[:30]]}")
        print("FAIL-SHELL")
    else:
        print("PASS-SHELL")


if __name__ == "__main__":
    main()
