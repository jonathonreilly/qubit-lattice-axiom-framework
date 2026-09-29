#!/usr/bin/env python3
"""The owner's frozen-box reading: counts of frozen record configurations under count-threshold formation rules.

Owner's reading (2026-09-28, recorded, not adopted): records form where the
neighbourhood allows; a sealed box's record count can rise until it is
frozen; a frozen box is a black hole. The axioms do not supply a formation
rule: Admissibility governs which possibility a forming record locks,
conditional on formation, not where or when records form. The rules below
are a supplied formalisation of the owner's reading, not of the axioms.

Supplied formalisation: a sealed L^d box of Z^d (d = 2, 3), at most one
record per site, records permanent. An empty site may form a record iff its
number k of recorded nearest neighbours lies in an allowed set A (two
families: upward-closed A = {m, ..., 2d}; crowding A = {0, ..., m}). Growth
is monotone; the box is frozen when no empty site has k in A. N counts the
distinct frozen occupation sets reachable from the empty box (a flat count,
not the outcome distribution of any process). Revised after the first
referee's FAILS verdict: the scaling, no-go and black-hole conclusions are
withdrawn to the exact lemmas and finite tables.

Checks:
  A  upward-closed rules: the frozen state from any start is the unique
     least closure (order-independent); from the empty box it is the full
     box if 0 is in A, else the empty box (checked for every m on 5^2 and
     3^3 boxes with random starts and orders).
  B  crowding rules: a configuration is reachable iff its recorded set is
     m-degenerate (reverse an addition order), and frozen iff every empty
     site has more than m recorded neighbours. All 28 exact counts on 2D
     boxes L = 2..5 and 3D boxes L = 2, 3 are pinned. For m = 0 the counts
     are the maximal-independent-set counts of the grid (2D: 2, 10, 42, 358,
     as in OEIS A197054).
  C  volume law for every crowding rule (the Fable referee's sealed-block
     lemma, third version): frozen reachable states of sealed b^d blocks at
     gap 1 survive any completion in the corridors, so
     N_L >= N_b^(floor((L+1)/(b+1))^d); per-site lower bounds for every
     m <= 2d - 1; the conditional comparison with the area count.
  D  two exact facts: for m >= d every configuration is m-degenerate; for
     m = 2d - 1, N is the number of independent sets of the (L - 2)^d
     interior.
  E  another count-threshold rule (2D, A = {0, 2, 3, 4}): N = 1, 7, 13 for
     L = 2, 3, 4; its empty sites need not touch the boundary (the
     second-round referee's L = 5 example, checked frozen and reachable).
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
expected = {(2, 0, 2): 2, (2, 0, 3): 10, (2, 0, 4): 42, (2, 0, 5): 358, (2, 1, 2): 6, (2, 1, 3): 57, (2, 1, 4): 1699, (2, 1, 5): 144205,
            (2, 2, 2): 1, (2, 2, 3): 17, (2, 2, 4): 305, (2, 2, 5): 22398, (2, 3, 2): 1, (2, 3, 3): 2, (2, 3, 4): 7, (2, 3, 5): 63,
            (3, 0, 2): 6, (3, 0, 3): 496, (3, 1, 2): 40, (3, 1, 3): 379531, (3, 2, 2): 34, (3, 2, 3): 413615, (3, 3, 2): 1, (3, 3, 3): 12274,
            (3, 4, 2): 1, (3, 4, 3): 65, (3, 5, 2): 1, (3, 5, 3): 2}
okB = len(expected) == 28 and all(table[k] == v for k, v in expected.items())
rowsB = []
for d, Ls in ((2, (2, 3, 4, 5)), (3, (2, 3))):
    for m in range(0, 2 * d):
        per_site = [np.log(table[(d, m, L)]) / L ** d for L in Ls]
        per_bdy = [np.log(table[(d, m, L)]) / L ** (d - 1) for L in Ls]
        rowsB.append(f"d={d} m={m}: N = {[table[(d, m, L)] for L in Ls]}, lnN/L^d = {np.round(per_site, 3).tolist()}, lnN/L^(d-1) = {np.round(per_bdy, 3).tolist()}")
check("B: crowding rules (a record forms only if at most m neighbours are recorded): reachable iff m-degenerate, frozen iff every empty site has more than m recorded neighbours; all 28 exact counts on 2D boxes L = 2..5 and 3D boxes L = 2, 3 pinned; the m = 0 counts are the grid's maximal-independent-set counts",
      okB, "; ".join(rowsB))

# ---------------------------------------------------------------- C: volume lower bound for every crowding rule (sealed-block lemma)
def degenerate_set(R, nb, m):
    R = set(R); changed = True
    while R and changed:
        changed = False
        for v in list(R):
            if sum(1 for u in nb[v] if u in R) <= m:
                R.discard(v); changed = True
    return not R


def frozen_set(R, nb, m, n):
    return all(sum(1 for u in nb[v] if u in R) > m for v in range(n) if v not in R)


def list_frozen(L, d, m):        # all reachable frozen occupation sets of a sealed L^d box (small L only)
    sites, nb = grid(L, d); n = len(sites); out = []
    for mask in range(1 << n):
        R = {v for v in range(n) if mask >> v & 1}
        if frozen_set(R, nb, m, n) and degenerate_set(R, nb, m):
            out.append(R)
    return sites, out


def block_states(L, d, m, b, sample=None):
    sites, nb = grid(L, d); idx = {s: i for i, s in enumerate(sites)}; n = len(sites)
    bsites, bstates = list_frozen(b, d, m)
    nbl = (L + 1) // (b + 1); origins = list(itertools.product(range(nbl), repeat=d))
    blockmap = [[idx[tuple(o[j] * (b + 1) + s[j] for j in range(d))] for s in bsites] for o in origins]
    choices = list(itertools.product(range(len(bstates)), repeat=len(origins))) if sample is None else [tuple(rng.integers(len(bstates), size=len(origins))) for _ in range(sample)]
    finals = set(); ok = True; inblock = set(v for bm in blockmap for v in bm)
    for ch in choices:
        R = set()
        for bm, c in zip(blockmap, ch):
            R |= {bm[v] for v in bstates[c]}
        ok &= degenerate_set(R, nb, m)                          # the blocks are built first (they are not adjacent)
        order = np.random.default_rng(len(finals)).permutation(n); grew = True
        while grew:                                              # then greedy growth in the corridors, random order
            grew = False
            for v in order:
                if v not in R and sum(1 for u in nb[v] if u in R) <= m:
                    R.add(v); grew = True
        target = set()
        for bm, c in zip(blockmap, ch):
            target |= {bm[v] for v in bstates[c]}
        ok &= (R & inblock) == target and frozen_set(R, nb, m, n) and degenerate_set(R, nb, m)
        finals.add(frozenset(R))
    return ok, len(bstates), len(origins), len(finals), len(choices)


rowsC = []; okC = True
for (d, m, L, b, smp) in ((2, 0, 5, 2, None), (2, 1, 5, 2, None), (2, 0, 7, 3, None), (2, 2, 7, 3, 400), (3, 0, 5, 2, 300)):
    ok, Nb, nblk, nfin, nch = block_states(L, d, m, b, smp)
    okC &= ok and nfin == nch and (smp is not None or nfin == Nb ** nblk)
    rowsC.append(f"d={d} m={m} L={L} b={b}: {Nb} block states, {nblk} blocks, {nfin} distinct frozen reachable states from {nch} {'sampled ' if smp else ''}block choices")
rates = []
for d, bs in ((2, (2, 3, 4, 5)), (3, (2, 3))):
    for m in range(0, 2 * d):
        best = max((np.log(table[(d, m, b)]) / (b + 1) ** d, b) for b in bs)
        okC &= best[0] > 0
        rates.append(f"d={d} m={m}: c >= {best[0]:.4f} (b={best[1]})")
# conditional comparison: flat count against the area count 6 L^2 / 4 (3D, m = 0), smallest L0 beyond which the proved bound always exceeds it
def lower3(L):
    return max(np.log(table[(3, 0, b)]) * ((L + 1) // (b + 1)) ** 3 for b in (2, 3))
L0 = next(L for L in range(2, 400) if all(lower3(Lp) > 1.5 * Lp ** 2 for Lp in range(L, 400)))
okC &= all(np.log(table[(3, 0, 3)]) * ((L - 2) / 4) ** 3 > 1.5 * L ** 2 for L in range(400, 2000, 97))
check("C: volume law for every crowding rule (the Fable referee's sealed-block lemma): frozen reachable states of a sealed b^d box, placed in floor((L+1)/(b+1))^d blocks at gap 1 and completed by any growth in the corridors, stay intact, so N_L >= N_b^(floor((L+1)/(b+1))^d) and ln N >= c L^d asymptotically with c = ln N_b/(b+1)^d > 0 for every m <= 2d - 1 (upper bound L^d ln 2)",
      okC, "; ".join(rowsC) + "; per-site lower bounds " + ", ".join(rates) + f"; if S = ln N (with a = l_P, the box surface a horizon and the quarter coefficient imported), the proved 3D m = 0 bound exceeds the area count 6L^2/4 for every L >= {L0}")

# ---------------------------------------------------------------- D: two exact facts (m >= d; m = 2d - 1)
okD = True
for d, L, trials in ((2, 5, 3000), (3, 3, 3000)):
    sites, nb = grid(L, d); n = len(sites)
    for _ in range(trials):
        R = {v for v in range(n) if rng.random() < rng.random()}
        okD &= degenerate_set(R, nb, d)                          # the lexicographically least site of R has at most d recorded neighbours
def count_independent(k, d):
    if k <= 0:
        return 1
    sites, nb = grid(k, d); n = len(sites); cnt = 0
    for mask in range(1 << n):
        if all(not (mask >> v & 1 and mask >> u & 1) for v in range(n) for u in nb[v] if u > v):
            cnt += 1
    return cnt
indep = {(2, L): count_independent(L - 2, 2) for L in (2, 3, 4, 5)} | {(3, L): count_independent(L - 2, 3) for L in (2, 3)}
okD &= all(table[(d, 2 * d - 1, L)] == indep[(d, L)] for (d, L) in indep)
check("D: two exact facts: for m >= d every configuration is m-degenerate, so every frozen set is reachable (the lexicographically least recorded site has at most d recorded neighbours); for m = 2d - 1 a frozen set has a full boundary and an independent set of empty interior sites, so N equals the number of independent sets of the (L - 2)^d interior",
      okD, f"random subsets d-degenerate (2D L=5, 3D L=3, 3000 each): {okD}; m = 2d - 1 counts equal interior independent-set counts: " + ", ".join(f"d={d} L={L}: {indep[(d, L)]}" for (d, L) in indep))

# ---------------------------------------------------------------- E: another count-threshold rule, outside the two families
def reach_frozen_bfs(L, d, A):
    sites, nb = grid(L, d); n = len(sites); nbm = [sum(1 << u for u in nb[v]) for v in range(n)]
    seen = {0}; frontier = [0]; frozen = set()
    while frontier:
        new = []
        for M in frontier:
            moved = False
            for v in range(n):
                if not M >> v & 1 and bin(M & nbm[v]).count("1") in A:
                    moved = True; N = M | 1 << v
                    if N not in seen:
                        seen.add(N); new.append(N)
            if not moved:
                frozen.add(M)
        frontier = new
    return sites, frozen
countsE = [len(reach_frozen_bfs(L, 2, {0, 2, 3, 4})[1]) for L in (2, 3, 4)]
# the second-round referee's L = 5 state: columns x = 0, 3, 4 recorded, x = 1, 2 empty; frozen, and reachable (search over addition orders
# inside the target set, memoised on subsets)
sites5, nb5 = grid(5, 2); n5 = len(sites5); target = [i for i, s_ in enumerate(sites5) if s_[0] in (0, 3, 4)]
tmask = sum(1 << v for v in target); AE = {0, 2, 3, 4}
frozen5 = all(sum(1 for u in nb5[v] if tmask >> u & 1) not in AE for v in range(n5) if not tmask >> v & 1)
seen5 = set()
def reach5(M):
    if M == tmask:
        return True
    if M in seen5:
        return False
    seen5.add(M)
    return any(reach5(M | 1 << v) for v in target if not M >> v & 1 and sum(1 for u in nb5[v] if M >> u & 1) in AE)
reach_ok = reach5(0)
interior_empty = any(not tmask >> i & 1 and min(min(c, 4 - c) for c in s_) == 2 for i, s_ in enumerate(sites5))
okE = countsE == [1, 7, 13] and frozen5 and reach_ok and interior_empty
check("E: another count-threshold rule, outside both families (2D, A = {0, 2, 3, 4}: exactly one recorded neighbour blocks formation): exact counts N = 1, 7, 13 for L = 2, 3, 4 (27 at L = 5 by two referees' enumerations); the empty sites need not touch the boundary: at L = 5 the state with columns 0, 3, 4 recorded is frozen and reachable and has an empty site at distance 2 from the boundary",
      okE, f"N = {countsE}; L = 5 state (columns 0, 3, 4 recorded) frozen: {frozen5}, reachable: {reach_ok}, empty site at boundary distance 2: {interior_empty}")

print("N5 resolution 1: upward-closed count rules freeze a sealed box into one state (the least closure); every crowding rule with m <= 2d - 1 freezes it into a number of states growing like exp(c L^d), c > 0 proved by the sealed-block lemma (upper bound L^d ln 2); other count-threshold rules grow much more slowly on small boxes (E).")
print("N5 resolution 2: no entropy identification and no black-hole comparison is claimed; the only comparison is conditional (if S = ln N, with a = l_P, the box surface a horizon and the quarter coefficient imported, the proved 3D m = 0 bound exceeds the area count for L >= 19).")
print("per_element: each counted configuration checked for reachability (m-degeneracy) and frozenness.")
print("per_site: the neighbourhood rule at every site of each box, including the sealed boundary.")
print("per_mode: checked and not executed - no spectrum is involved.")
print("per_block: exact counts on 2D boxes L = 2..5 and 3D boxes L = 2, 3 for every crowding rule; order-independence for every upward-closed rule; the sealed-block construction on five box sizes; rule E on L = 2..4 and one L = 5 state.")
print("lattice_wide: resolves the structural lemmas (unique closure; m-degenerate reachability; the sealed-block volume bound; the m >= d and m = 2d - 1 facts) for every box; checked and not executed - the exact asymptotic rate, other rules in general, outcome weights, any entropy identification.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
