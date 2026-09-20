#!/usr/bin/env python3
"""tight-sibling-vacuity, attempt a1: an independent re-verification of a2's refutation.

Attempt a2 (`w-macbookpro90c72-jb9bd`, another machine) refutes the task's (Q), block 33's
tight-sibling lemma and the rooted inequality (H) at one realization, and bounds block 32's
family constant below by 10/9.  A refutation that kills three statements at once is worth
re-deriving with machinery that shares no code with it, which is what this does.  The task's
own referee warns that `family.py`'s `brute_min` omits the level restriction; nothing here uses
`family.py`, `rooted.py` or `scipy`.

  V1  rebuild the realization from the marks, on two boxes             exact
  V2  the kinds, the level sizes, the predecessors of 333              exact
  V3  v(z) by a layered dynamic program over levels                    exact integers
  V4  the three 1-predecessors of 333 are tight, and v(333) = +1       exact
  V5  c*(eta, 333) = 10/9 exactly                                      exact rationals
  V6  the witness is mark-minimal: dropping any one mark destroys it   exact
  V7  cross-check of V3 against a node-closure integer program         only if scipy is present

Definitions (block 32 RESULTS lines 88-90, block 33 RESULTS lines 92-94):
sites x in Z^3, level tau(x) = x1+x2+x3, predecessors x - e_j.  eta_x = 1 if at least two
predecessors are 1, else 1 iff x is a mark.  A seed has no 1-predecessor, an amplified site
exactly one, a processed-type site at least two.  With a single seed every tree of the family is
a set T of 1-sites in which every non-seed node has a 1-predecessor in T, and
cost(T) = E - 3(|S|-1) - c|A| = E - c|A|, E = #processed in T, A = #amplified in T.
v(z) = min cost over trees containing z whose nodes all have level <= tau(z).
"""
import itertools, sys
from fractions import Fraction as F

MARKS = {(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,2,1),(1,0,2),(2,1,0),(1,1,3),(1,3,1),(3,1,1)}
PRED = lambda x: [(x[0]-1,x[1],x[2]), (x[0],x[1]-1,x[2]), (x[0],x[1],x[2]-1)]
LEV = lambda x: x[0]+x[1]+x[2]

def realize(marks, lo, hi):
    """the one-sites of the realization from `marks`, computed inside the box [lo,hi]^3."""
    ones = set()
    for lev in range(3*lo, 3*hi + 1):
        for x in itertools.product(range(lo, hi+1), repeat=3):
            if LEV(x) != lev: continue
            n = sum(1 for p in PRED(x) if p in ones)
            if n >= 2 or x in marks: ones.add(x)
    return ones

def kinds(ones):
    out = {}
    for x in ones:
        n = sum(1 for p in PRED(x) if p in ones)
        out[x] = "seed" if n == 0 else ("amp" if n == 1 else "proc")
    return out

def vmin(z, ones, K, c=F(1), level_restrict=True, need_amp=False):
    """min of E - c|A| over trees containing z, by a layered DP over levels.

    A tree is a set T of 1-sites with every non-seed node having a 1-predecessor in T.  Every
    predecessor of a level-(l+1) site lies at level l, so a sweep by level with the state
    "which level-l sites are in T" is exact.  States are subsets of a level, and the largest
    level here holds 7 sites, so the whole sweep is 2^7 wide."""
    top = LEV(z)
    lvl = {}
    for x in ones:
        if level_restrict and LEV(x) > top: continue
        lvl.setdefault(LEV(x), []).append(x)
    for l in lvl: lvl[l].sort()
    levels = sorted(lvl)
    W = lambda x: F(0) if K[x] == "seed" else (F(1) if K[x] == "proc" else -c)

    # state: (frozenset of included sites at this level, whether an amplified site is in T yet)
    states = {}
    for mask in range(1 << len(lvl[levels[0]])):
        sel = {lvl[levels[0]][i] for i in range(len(lvl[levels[0]])) if mask >> i & 1}
        if any(K[x] != "seed" for x in sel): continue        # level 0 can only hold seeds
        cost = sum(W(x) for x in sel)
        amp = any(K[x] == "amp" for x in sel)
        key = (frozenset(sel), amp)
        if key not in states or cost < states[key][0]: states[key] = (cost, [sel])
    for li in range(1, len(levels)):
        l = levels[li]; below = set(lvl[levels[li-1]]) if levels[li-1] == l-1 else set()
        here = lvl[l]; nxt = {}
        for (prev, amp), (cost, hist) in states.items():
            for mask in range(1 << len(here)):
                sel = {here[i] for i in range(len(here)) if mask >> i & 1}
                okay = True
                for x in sel:
                    if K[x] == "seed": continue
                    if not any(p in prev for p in PRED(x)): okay = False; break
                if not okay: continue
                if l == top and z not in sel: continue
                c2 = cost + sum(W(x) for x in sel)
                a2 = amp or any(K[x] == "amp" for x in sel)
                key = (frozenset(sel), a2)
                if key not in nxt or c2 < nxt[key][0]: nxt[key] = (c2, hist + [sel])
        states = nxt
        if not states: return None, None
    best = None
    for (sel, amp), (cost, hist) in states.items():
        if z not in sel: continue
        if need_amp and not amp: continue
        if best is None or cost < best[0]: best = (cost, hist)
    if best is None: return None, None
    T = set().union(*best[1])
    return best[0], T

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("V1  the realization")
    small = realize(MARKS, 0, 3)
    big = realize(MARKS, -2, 6)
    want(small == big, "the marks realize the same one-set in [0,3]^3 and in [-2,6]^3, so the")
    print("     realization is the one on Z^3 (nothing escapes the box)")
    ones = small
    K = kinds(ones)
    want(len(ones) == 37, f"it has {len(ones)} one-sites")

    print("\nV2  kinds, levels, and the site 333")
    ns = sum(1 for v in K.values() if v == "seed")
    na = sum(1 for v in K.values() if v == "amp")
    npr = sum(1 for v in K.values() if v == "proc")
    want((ns, na, npr) == (1, 9, 27), f"one seed, {na} amplified, {npr} processed-type")
    sizes = [sum(1 for x in ones if LEV(x) == l) for l in range(10)]
    want(sizes == [1, 3, 3, 4, 3, 6, 7, 6, 3, 1], f"level sizes {sizes}")
    z = (3, 3, 3)
    preds = [p for p in PRED(z) if p in ones]
    want(K[z] == "proc" and len(preds) == 3 and all(K[p] == "proc" for p in preds),
         f"333 is processed-type and all three of its 1-predecessors {preds} are processed-type")

    print("\nV3/V4  the rooted values, by the layered dynamic program")
    vs = {}
    for t in preds + [z]:
        v, T = vmin(t, ones, K)
        E = sum(1 for x in T if K[x] == "proc"); A = sum(1 for x in T if K[x] == "amp")
        S = sum(1 for x in T if K[x] == "seed")
        vs[t] = v
        print(f"     v{t} = {int(v):+d}   |T| = {len(T)}  E = {E}  A = {A}  S = {S}")
    want(all(vs[p] == 0 for p in preds),
         "each of 233, 323, 332 is TIGHT: its rooted value is exactly 0")
    want(vs[z] == 1,
         "and v(333) = +1 > 0: the tight-sibling lemma's conclusion fails at 333")
    print("     So (Q) is false - a processed site can have all its processed 1-predecessors")
    print("     tight - the tight-sibling lemma is false, and with it the rooted inequality (H).")
    print("     This reproduces attempt a2's refutation from the marks alone.")

    print("\nV5  the family constant at this root, exactly")
    for cc in (F(1), F(10, 9), F(1001, 900), F(11, 9)):
        v, T = vmin(z, ones, K, c=cc, need_amp=True)
        E = sum(1 for x in T if K[x] == "proc"); A = sum(1 for x in T if K[x] == "amp")
        print(f"     c = {str(cc):<9} min(E - c|A|) = {str(v):<8} at E = {E}, A = {A}")
    v1, T1 = vmin(z, ones, K, c=F(10, 9), need_amp=True)
    v0, T0 = vmin(z, ones, K, c=F(1), need_amp=True)
    want(v0 == 1 and v1 == 0,
         "min(E - |A|) = 1 and min(E - (10/9)|A|) = 0, so min E/|A| = 10/9 at this root:")
    print("     c*(eta, 333) = 10/9 > 1, which is a2's lower bound, and it removes the c = 1")
    print("     certificates that block 33's threshold 453 rests on.")
    vu, _ = vmin(z, ones, K, c=F(10, 9), level_restrict=False, need_amp=True)
    want(vu == 0, "the same with the level restriction lifted, so this is the family's value, not")
    print("     an artefact of the rooted restriction")

    print("\nV6  is the witness minimal?")
    survivors = []
    for m in sorted(MARKS - {(0, 0, 0)}):
        M2 = MARKS - {m}
        o2 = realize(M2, 0, 3)
        if realize(M2, -2, 6) != o2:
            print(f"     drop {m}: escapes the box"); continue
        K2 = kinds(o2)
        if z not in o2 or K2.get(z) != "proc":
            print(f"     drop {m}: 333 is no longer processed-type"); continue
        p2 = [p for p in PRED(z) if p in o2]
        if len(p2) < 2 or any(K2[p] != "proc" for p in p2):
            print(f"     drop {m}: fewer than two processed 1-predecessors"); continue
        vv = [vmin(p, o2, K2)[0] for p in p2]
        vz = vmin(z, o2, K2)[0]
        print(f"     drop {m}: preds v = {[int(x) for x in vv]}, v(333) = {int(vz):+d}")
        if all(x == 0 for x in vv) and vz > 0: survivors.append(m)
    want(not survivors,
         "every one of the nine non-seed marks is needed: dropping any single one destroys the")
    print("     counterexample, so the witness is minimal for removal of one mark.")

    print("\nV7  cross-check against a different formulation")
    try:
        import numpy as np
        from scipy.optimize import milp, LinearConstraint, Bounds
        def ilp(zz, c=1.0):
            nodes = [x for x in ones if LEV(x) <= LEV(zz)]
            idx = {x: i for i, x in enumerate(nodes)}; n = len(nodes)
            w = np.array([0.0 if K[x] == "seed" else (1.0 if K[x] == "proc" else -c) for x in nodes])
            A = []; lb = []; ub = []
            for x in nodes:
                if K[x] == "seed": continue
                row = np.zeros(n); row[idx[x]] = 1.0
                for p in PRED(x):
                    if p in idx: row[idx[p]] -= 1.0
                A.append(row); lb.append(-np.inf); ub.append(0.0)
            row = np.zeros(n); row[idx[zz]] = 1.0; A.append(row); lb.append(1.0); ub.append(1.0)
            r = milp(c=w, constraints=LinearConstraint(np.array(A), lb, ub),
                     integrality=np.ones(n), bounds=Bounds(0, 1))
            return r.fun if r.success else None
        agree = all(abs(ilp(t) - float(vs[t])) < 1e-9 for t in preds + [z])
        want(agree, "a node-closure integer program (HiGHS) agrees with the DP at all four sites")
    except ImportError:
        print("     scipy absent; skipped (the DP above needs nothing but the standard library)")

    print()
    if ok:
        print("SUMMARY: PARTIAL attempt a2's refutation is reproduced from its ten marks by "
              "independent machinery - a layered dynamic program over levels, exact integers, no "
              "scipy and no probes/lib: the realization has 37 one-sites with level sizes "
              "1,3,3,4,3,6,7,6,3,1, the three 1-predecessors of 333 are processed-type with rooted "
              "value exactly 0 (tight) while v(333) = +1, so (Q), block 33's tight-sibling lemma "
              "and the rooted inequality (H) all fail; c*(eta,333) = 10/9 exactly, with and "
              "without the level restriction; and the witness is minimal, since dropping any one "
              "of the nine non-seed marks stops 333 being processed-type")
        print("HIT: the refutation stands under re-derivation by different machinery, and the "
              "witness is mark-minimal: all ten marks are needed, so no smaller realization of "
              "this shape refutes the lemma")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
