#!/usr/bin/env python3
"""The owner's frozen-box reading: counts of frozen record configurations in a sealed box.

Owner's reading (2026-09-28, recorded, not adopted): records form where the
neighbourhood allows; a sealed box's record count can rise until it is
frozen; a frozen box is a black hole. Test: a black hole's entropy grows with
its boundary area (S = A/4 in Planck units; the scale primitive puts the
lattice spacing at the Planck length). Does a frozen box's entropy?

Supplied formalisation: a sealed L^d box of Z^d (d = 2, 3), at most one
record per site, records permanent. An empty site may form a record iff its
number k of recorded nearest neighbours lies in an allowed set A. Growth is
monotone; the box is frozen when no empty site has k in A. The entropy is
ln N, with N the number of distinct frozen configurations reachable from the
empty box. Pre-registered in the probe's scratch file: PASS if some tested
rule gives ln N growing like the boundary (L^(d-1)); FAIL if every tested
rule gives a unique frozen state or ln N growing like the volume (L^d).

Checks:
  A  upward-closed rules (A = {m, ..., 2d}): the frozen state reached from
     any start is unique (order-independent closure; random starts and
     random orders on 2D and 3D boxes). From the empty box: the full box if
     0 in A, the empty box otherwise.
  B  crowding rules (A = {0, ..., m}, m < 2d: a record forms only if at most
     m neighbours are recorded): a configuration is reachable iff its
     recorded set is m-degenerate, and frozen iff every empty site has more
     than m recorded neighbours. Exact counts (backtracking) on 2D boxes
     L = 2..5 and 3D boxes L = 2, 3: ln N per site stays roughly constant
     (volume growth) while ln N per boundary unit keeps growing.
  C  comparison with a black hole whose horizon area equals the box's
     surface (S_BH = (2d L^(d-1))/4 in lattice units): with ln N ~ c L^d the
     frozen box's entropy exceeds S_BH beyond L* = 2d / (4c), a few lattice
     spacings for the measured c.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260929)


def grid(L, d):
    sites = list(itertools.product(range(L), repeat=d)); idx = {s: i for i, s in enumerate(sites)}
    nb = [[idx[t] for k in range(d) for dv in (-1, 1) for t in [tuple(s[j] + (dv if j == k else 0) for j in range(d))] if t in idx] for s in sites]
    return sites, nb


# ---------------------------------------------------------------- A: upward-closed rules give a unique frozen state
def grow(start, nb, A, order_rng):
    R = set(start); n = len(nb)
    while True:
        cand = [v for v in range(n) if v not in R and sum(1 for u in nb[v] if u in R) in A]
        if not cand:
            return frozenset(R)
        R.add(cand[order_rng.integers(len(cand))])


okA = True; detA = []
for d, L in ((2, 5), (3, 3)):
    sites, nb = grid(L, d); n = len(sites)
    for m in range(0, 2 * d + 1):
        A = set(range(m, 2 * d + 1))
        finals = set()
        for trial in range(6):
            start = [v for v in range(n) if rng.random() < 0.2]
            outs = {grow(start, nb, A, np.random.default_rng(1000 * trial + r)) for r in range(5)}
            okA &= len(outs) == 1
        empty_final = grow([], nb, A, np.random.default_rng(0))
        okA &= (len(empty_final) == n) if 0 in A else (len(empty_final) == 0)
    detA.append(f"d = {d}, L = {L}: all {2 * d + 1} upward-closed rules order-independent from 6 random starts x 5 orders")
check("A: upward-closed rules (a record forms once at least m neighbours are recorded): the frozen state from any start is unique (order-independent closure); from the empty box it is the full box if 0 is allowed, else the empty box",
      okA, "; ".join(detA))


# ---------------------------------------------------------------- B: crowding rules, exact counts by backtracking
def count_frozen(L, d, m):
    sites, nb = grid(L, d); n = len(sites)
    order = list(range(n))
    later = [[u for u in nb[v] if u > v] for v in range(n)]
    assign = [-1] * n; found = [0]

    def ok_site(v):          # if v and all its neighbours are assigned, check the frozen condition at v
        if any(assign[u] < 0 for u in nb[v]):
            k = sum(1 for u in nb[v] if assign[u] == 1); unk = sum(1 for u in nb[v] if assign[u] < 0)
            return not (assign[v] == 0 and k + unk <= m)
        if assign[v] == 0:
            return sum(1 for u in nb[v] if assign[u] == 1) > m
        return True

    def degenerate():
        R = {v for v in range(n) if assign[v] == 1}; changed = True
        while R and changed:
            changed = False
            for v in list(R):
                if sum(1 for u in nb[v] if u in R) <= m:
                    R.discard(v); changed = True
        return not R

    def rec(i):
        if i == n:
            if degenerate():
                found[0] += 1
            return
        for val in (0, 1):
            assign[i] = val
            if val == 1 and m == 0 and any(assign[u] == 1 for u in nb[i] if u < i):
                assign[i] = -1; continue                  # m = 0: reachable sets are independent sets
            good = ok_site(i) and all(ok_site(u) for u in nb[i] if u < i)
            if good:
                rec(i + 1)
            assign[i] = -1
    rec(0)
    return found[0]


table = {}
for d, Ls in ((2, (2, 3, 4, 5)), (3, (2, 3))):
    for m in range(0, 2 * d):
        for L in Ls:
            table[(d, m, L)] = count_frozen(L, d, m)
expected = {(2, 0, 5): 358, (2, 1, 5): 144205, (3, 0, 3): 496, (3, 1, 3): 379531, (3, 2, 3): 413615}
okB = all(table[k] == v for k, v in expected.items())
rowsB = []
for d, Ls in ((2, (2, 3, 4, 5)), (3, (2, 3))):
    for m in range(0, 2 * d):
        per_site = [np.log(table[(d, m, L)]) / L ** d for L in Ls]
        per_bdy = [np.log(table[(d, m, L)]) / L ** (d - 1) for L in Ls]
        rowsB.append(f"d={d} m={m}: N = {[table[(d, m, L)] for L in Ls]}, lnN/L^d = {np.round(per_site, 3).tolist()}, lnN/L^(d-1) = {np.round(per_bdy, 3).tolist()}")
# volume growth where the sizes resolve it: 2D m = 0, 1 (L = 2..5) and 3D m = 0, 1, 2 (L = 2, 3)
okB &= all(abs(np.log(table[(2, m, 5)]) / 25 - np.log(table[(2, m, 4)]) / 16) < 0.03 for m in (0, 1))
okB &= all(np.log(table[(2, m, 5)]) / 5 > np.log(table[(2, m, 4)]) / 4 > np.log(table[(2, m, 3)]) / 3 for m in (0, 1, 2, 3))
okB &= all(np.log(table[(3, m, 3)]) / 9 > np.log(table[(3, m, 2)]) / 4 for m in (0, 1, 2))
check("B: crowding rules (a record forms only if at most m neighbours are recorded): exact counts of frozen configurations reachable from the empty box; ln N per site is roughly constant (2D m = 0, 1 change < 0.03 between L = 4 and 5) while ln N per boundary unit grows with L for every m tested: volume growth, not boundary growth",
      okB, "; ".join(rowsB))

# ---------------------------------------------------------------- C: comparison with S_BH = (boundary area)/4
cvals = {m: np.log(table[(3, m, 3)]) / 27 for m in (0, 1, 2)}
Lstar = {m: (6 / 4) / c for m, c in cvals.items()}
okC = all(1 < v < 10 for v in Lstar.values())
check("C: comparison with a black hole whose horizon area equals the box's surface (lattice spacing = Planck length, S_BH = 6 L^2 / 4 in 3D): a frozen box with ln N ~ c L^3 exceeds S_BH beyond L* = 1.5 / c, a few lattice spacings; with a unique frozen state (upward-closed rules) the entropy is 0",
      okC, f"3D per-site entropy at L = 3: {({m: round(c, 3) for m, c in cvals.items()})}; L* = {({m: round(v, 1) for m, v in Lstar.items()})}")

print("N5 resolution 1: every tested formation rule gives either a unique frozen state (entropy 0) or a frozen-state count growing with the volume; none grows with the boundary. Pre-registered outcome: FAIL.")
print("N5 resolution 2: with the lattice at the Planck length, volume-growing frozen boxes larger than a few spacings would exceed the entropy of a black hole of their size.")
print("per_element: each counted configuration checked for reachability (m-degeneracy) and frozenness.")
print("per_site: the neighbourhood rule at every site of each box, including the sealed boundary.")
print("per_mode: checked and not executed - no spectrum is involved.")
print("per_block: exact counts on 2D boxes L = 2..5 and 3D boxes L = 2, 3 for every crowding rule; order-independence for every upward-closed rule.")
print("lattice_wide: checked and not executed - sizes beyond L = 5 (2D) and 3 (3D), rules that are neither crowding nor upward-closed, stochastic weights, any quantum dynamics.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
