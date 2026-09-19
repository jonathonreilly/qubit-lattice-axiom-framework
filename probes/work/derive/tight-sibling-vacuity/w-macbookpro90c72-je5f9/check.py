#!/usr/bin/env python3
"""J:derive:tight-sibling-vacuity:a4 -- independent re-derivation.

Every object is rebuilt from the block-33 note's definitions in this file.
probes/lib is used ONLY as an optional final cross-check (block X), never as
the source of a value.  Rooted values are certified TWO-SIDEDLY:
  lower bound: exhaustive minimisation over level-restricted CLOSED node sets
               (every family tree's node set is closed, and cost depends only
               on the node set, so this is a valid lower bound);
  upper bound: an explicit family tree, verified against the definition here.
When the two coincide the rooted value is exact and needs no other authority.
"""
import sys
from fractions import Fraction as Fr
from itertools import product, combinations

E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK = set(tuple(E3[a][i] - E3[b][i] for i in range(3))
           for a in range(3) for b in range(3) if a != b)
def lev(z): return z[0] + z[1] + z[2]
def preds(z): return [tuple(z[i] - e[i] for i in range(3)) for e in E3]
WT = {"proc": 1, "amp": -1, "seed": -3}          # cost(N) = 3 + sum WT over N

P = F = 0
def ck(ok, msg):
    global P, F
    P, F = P + (1 if ok else 0), F + (0 if ok else 1)
    print(("ok   " if ok else "FAIL ") + msg)

# ---------------------------------------------------------------- automaton
def realize(marks, L):
    """eta on {z >= 0, level(z) <= L}; sites with a negative coordinate are 0
    (block A1 below).  eta[z] = 1 iff (>=2 one-predecessors) or marked."""
    sites = sorted([p for p in product(range(L + 1), repeat=3) if lev(p) <= L], key=lev)
    eta = {}
    for z in sites:
        eta[z] = 1 if (sum(eta.get(p, 0) for p in preds(z)) >= 2 or z in marks) else 0
    ones = set(z for z in sites if eta[z])
    kind = {}
    for z in ones:
        n = len([p for p in preds(z) if p in ones])
        kind[z] = "seed" if n == 0 else ("amp" if n == 1 else "proc")
    return ones, kind

def layers(ones, L):
    U = {}
    for w in ones:
        if lev(w) <= L: U.setdefault(lev(w), []).append(w)
    for l in U: U[l].sort()
    return U

# ------------------------------------------------- lower bound over closed sets
def closed_min(ones, kind, z, want=False):
    L = lev(z); U = layers(ones, L); dp = {}
    for r in range(len(U.get(L, [])) + 1):
        for X in combinations(U[L], r):
            if z in X: dp[X] = (sum(WT[kind[w]] for w in X), (X,))
    for l in range(L, 0, -1):
        low = U.get(l - 1, []); nd = {}
        for r in range(len(low) + 1):
            for Y in combinations(low, r):
                Ys = set(Y); best = None
                for X, (val, tr) in dp.items():
                    if all(kind[w] == "seed" or any(p in Ys for p in preds(w)) for w in X):
                        if best is None or val < best[0]: best = (val, tr)
                if best is not None:
                    nd[Y] = (best[0] + sum(WT[kind[w]] for w in Y), best[1] + (Y,))
        dp = nd
        if not dp: return None
    val, tr = min(dp.values(), key=lambda t: t[0])
    if not want: return 3 + val
    N = set()
    for lay in tr: N |= set(lay)
    return 3 + val, N

# ------------------------------------------------ explicit tree + verification
def build_tree(ones, kind, z, N):
    """arrows: every non-seed -> a 1-pred in N.  forks: span the arborescences."""
    S = [w for w in N if kind[w] == "seed"]
    arrows, root_of = [], {}
    for w in sorted(N, key=lev):
        if kind[w] == "seed": root_of[w] = w
        else:
            ps = [p for p in preds(w) if p in N]
            if not ps: return None
            arrows.append((w, ps[0])); root_of[w] = root_of[ps[0]]
    forks, seen = [], {S[0]}
    while len(seen) < len(S):
        add = None
        for u in N:
            for off in FORK:
                v = tuple(u[i] + off[i] for i in range(3))
                if v in N and (root_of[u] in seen) != (root_of[v] in seen):
                    add = (u, v); break
            if add: break
        if not add: return None
        forks.append(add); seen |= {root_of[add[0]], root_of[add[1]]}
    return N, arrows, forks

def verify_tree(ones, kind, z, N, arrows, forks):
    """checked against the note's definition, written from scratch here."""
    S = [w for w in N if kind[w] == "seed"]
    if z not in N: return None
    if any(w not in ones or lev(w) > lev(z) for w in N): return None
    if len(arrows) != len(N) - len(S): return None
    if any(p not in preds(u) or p not in N or u not in N for u, p in arrows): return None
    if any(u not in N or v not in N or
           tuple(v[i] - u[i] for i in range(3)) not in FORK for u, v in forks): return None
    if len(forks) != len(S) - 1: return None
    edges = list(arrows) + list(forks)
    if len(edges) != len(N) - 1: return None
    adj = {w: [] for w in N}
    for a, b in edges: adj[a].append(b); adj[b].append(a)
    seen, st = {z}, [z]
    while st:
        c = st.pop()
        for d in adj[c]:
            if d not in seen: seen.add(d); st.append(d)
    if seen != set(N): return None
    E = sum(1 for w in N if kind[w] == "proc"); A = sum(1 for w in N if kind[w] == "amp")
    return E - 3 * (len(S) - 1) - A

def rooted_exact(ones, kind, z):
    """returns (value, lower, upper) with lower == upper == value when certified."""
    r = closed_min(ones, kind, z, want=True)
    if r is None: return None
    lo, N = r
    t = build_tree(ones, kind, z, N)
    if t is None: return (None, lo, None)
    up = verify_tree(ones, kind, z, *t)
    return (lo if up == lo else None, lo, up)

# =============================================================== the witness
MARKS = frozenset({(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,2,1),(1,0,2),
                   (2,1,0),(1,1,3),(1,3,1),(3,1,1)})
Z = (3, 3, 3); TOP = 9
ones, kind = realize(MARKS, TOP)

print("== A  realization ==")
# A1: a site with a negative coordinate is 0 -- induction on level: its
# predecessors all keep that negative coordinate, and no mark has one.
ck(all(min(m) >= 0 for m in MARKS), "A1 no mark has a negative coordinate => eta=0 off the octant")
ck(len(ones) == 37, "A2 |{eta=1, level<=9}| = 37 (= %d)" % len(ones))
ck(all(max(w) <= 3 for w in ones), "A3 every 1-site lies in the cube [0,3]^3")
seeds = [w for w in ones if kind[w] == "seed"]
ck(seeds == [(0,0,0)], "A4 exactly one seed, at the origin")
cen = tuple(sum(1 for w in ones if kind[w] == k) for k in ("proc","amp","seed"))
ck(cen == (27, 9, 1), "A5 kind census (proc,amp,seed) = (27,9,1) = %s" % (cen,))
ck(max(lev(w) for w in ones) == 9 and Z in ones, "A6 top level is 9 and 333 is a 1-site")

print("== B  the C3 symmetry ==")
sig = lambda z: (z[1], z[2], z[0])
ck(set(map(sig, MARKS)) == set(MARKS), "B1 sigma(x,y,z)=(y,z,x) fixes the mark set")
ck(all(sig(w) in ones and kind[sig(w)] == kind[w] for w in ones),
   "B2 hence sigma fixes eta and preserves every kind")
PR = tuple(sorted(preds(Z)))
ck(PR == ((2,3,3),(3,2,3),(3,3,2)), "B3 the 1-preds of 333 are 233,323,332")
ck({sig((2,3,3)), sig(sig((2,3,3)))} == {(3,3,2),(3,2,3)},
   "B4 they form ONE sigma-orbit: verifying 233 gives the other two free")

print("== C  rooted values, certified two-sidedly ==")
vals = {}
for w in [(2,3,3),(3,2,3),(3,3,2),Z]:
    v, lo, up = rooted_exact(ones, kind, w)
    vals[w] = v
    ck(v is not None and lo == up,
       "C %s: closed-set lower %s == verified-tree upper %s => v = %s" % (w, lo, up, v))
ck(all(kind[p] == "proc" for p in PR), "C1 all three 1-preds of 333 are PROCESSED")
ck(all(vals[p] == 0 for p in PR), "C2 all three are TIGHT (rooted value exactly 0)")
ck(kind[Z] == "proc" and vals[Z] == 1, "C3 333 is processed with v(333) = 1")

print("== D  what this refutes ==")
ck(len(PR) >= 2 and all(kind[p] == "proc" and vals[p] == 0 for p in PR),
   "D1 the tight-sibling HYPOTHESIS is satisfiable (contra the a4 conjecture)")
ck(vals[Z] > 0, "D2 its CONCLUSION fails here: no tree at 333 has cost <= 0")
ck(vals[Z] > 0, "D3 hence the rooted inequality (H) fails at a processed site")
bad = [(w, vals.get(w)) for w in ones if kind[w] == "proc" and closed_min(ones, kind, w) > 0]
ck(bad == [(Z, 1)], "D4 333 is the ONLY site of the realization violating (H)")
tset = sorted([w for w in ones if kind[w] == "proc" and closed_min(ones, kind, w) == 0])
ck(tset == [(2,3,3),(3,2,3),(3,3,2)], "D5 the tight processed sites are exactly those three")

print("== E  the exact budget c* ==")
def pareto(ones, kind, z):
    L = lev(z); U = layers(ones, L)
    w2 = lambda S: (sum(1 for w in S if kind[w]=="proc"), sum(1 for w in S if kind[w]=="amp"))
    def trim(Q):
        Q = sorted(set(Q))
        return [(e,a) for e,a in Q if not any(e2<=e and a2>=a and (e2,a2)!=(e,a) for e2,a2 in Q)]
    dp = {}
    for r in range(len(U[L]) + 1):
        for X in combinations(U[L], r):
            if z in X: dp[X] = [w2(X)]
    for l in range(L, 0, -1):
        low = U.get(l - 1, []); nd = {}
        for r in range(len(low) + 1):
            for Y in combinations(low, r):
                Ys = set(Y); acc = []
                for X, Q in dp.items():
                    if all(kind[w]=="seed" or any(p in Ys for p in preds(w)) for w in X): acc += Q
                if acc:
                    de, da = w2(Y); nd[Y] = trim([(e+de, a+da) for e, a in acc])
        dp = nd
    return trim([p for Q in dp.values() for p in Q])
PF = pareto(ones, kind, Z)
ck(PF == [(6,5),(7,6),(8,7),(9,8),(10,9)], "E1 Pareto (E,A) frontier at 333 = %s" % (PF,))
cstar = min(Fr(e, a) for e, a in PF if a > 0)
ck(cstar == Fr(10, 9), "E2 c*(eta,333) = min E/A = %s exactly" % cstar)
ck(min((Fr(e,a), e, a) for e, a in PF if a > 0)[1:] == (10, 9) and PF[0] == (6, 5),
   "E3 the budget-critical set (10,9) is NOT the c=1 cost-minimiser (6,5)")
ck(cstar > 1, "E4 so the unit budget c = 1 is not admissible at this realization")

print("== F  the witness is minimal ==")
surv = []
for k in range(len(MARKS)):
    for sub in combinations(sorted(MARKS), k):
        o2, k2 = realize(frozenset(sub), TOP)
        if Z in o2 and k2[Z] == "proc":
            pr = [p for p in preds(Z) if p in o2]
            if len(pr) >= 2 and all(k2[p] == "proc" for p in pr): surv.append(frozenset(sub))
ck(len(surv) <= 2, "F1 of the 1023 proper subsets only %d keep 333 processed with >=2 proc preds" % len(surv))
ck(surv == [frozenset(MARKS - {(0,0,0)})], "F2 the one survivor is MARKS minus the origin mark")
bad2 = []
for sub in surv:
    o2, k2 = realize(sub, TOP)
    ns = len([w for w in o2 if k2[w] == "seed"])
    pr = [p for p in preds(Z) if p in o2]
    tri = [rooted_exact(o2, k2, p) for p in pr]
    ck(all(t[0] is not None and t[1] == t[2] for t in tri),
       "F3 its %d-seed values also certify two-sidedly (fork-spanned trees, not just bounds)" % ns)
    ck(all(t[0] != 0 for t in tri),
       "F4 and its preds have v = %s != 0, so they are NOT tight: not a violation" % [t[0] for t in tri])
    if all(t[0] == 0 for t in tri): bad2.append(sub)
ck(bad2 == [], "F5 hence every one of the 10 marks is load-bearing")

print("== G  no-go for the depth<=3 route ==")
M2 = MARKS | {(2, 2, 0)}
o3, k3 = realize(M2, TOP)
W0 = (2, 3, 3)
diff = [w for w in (ones | o3) if (w in ones) != (w in o3)
        or (w in ones and w in o3 and kind[w] != k3[w])]
ck(diff == [(2, 2, 0)], "G1 adding the single mark (2,2,0) changes exactly one site")
ck(lev(diff[0]) == 4, "G2 that site sits at level 4")
ck(all(lev(w) < 5 for w in diff), "G3 so eta and kind agree on EVERY site of level >= 5")
ck(lev(W0) == 8, "G4 233 is at level 8, so levels 5..8 hold its whole depth-3 cone")
v2, lo2, up2 = rooted_exact(o3, k3, W0)
ck(v2 is not None and lo2 == up2, "G5 v'(233) certified two-sidedly: lower %s == upper %s" % (lo2, up2))
ck(vals[W0] == 0 and v2 == -1, "G6 v(233) = 0 but v'(233) = -1 on an IDENTICAL depth-3 cone")
ck(True, "G7 => tightness is not a function of the depth<=3 cone; that census cannot decide it")

print("== X  cross-check against probes/lib (not used above) ==")
try:
    sys.path.insert(0, "probes")
    from lib.rooted import rooted as lib_rooted
    from lib.family import run_automaton as lib_auto
    sites = sorted([p for p in product(range(TOP+1), repeat=3) if lev(p) <= TOP], key=lev)
    le = lib_auto(sites, {m: 1 for m in MARKS})
    ck(set(z for z, v in le.items() if v == 1) == ones, "X1 lib run_automaton reproduces eta")
    for w in [(2,3,3), (3,2,3), (3,3,2), Z]:
        lv, cert = lib_rooted(le, w, 1.0)
        ck(int(round(float(lv))) == vals[w] and cert["kind"][w] == kind[w],
           "X2 lib MILP rooted%s = %s == mine %s (kind %s)" % (w, lv, vals[w], kind[w]))
    _, cz = lib_rooted(le, Z, 1.0)
    ck((cz["E"], cz["A"]) == PF[0],
       "X3 lib optimum (E,A) = (%d,%d) = my Pareto minimum %s" % (cz["E"], cz["A"], PF[0]))
except Exception as e:
    print("skip (%s: %s)" % (type(e).__name__, e))

print("TOTAL: PASS=%d FAIL=%d" % (P, F))
if F == 0:
    print("HIT: block 33's tight-sibling lemma and the rooted inequality (H) are both FALSE. Marks {000,001,010,100,021,102,210,113,131,311} give a sigma-cyclic one-seed realization with 37 one-sites in [0,3]^3 where 333 is processed, its 1-preds 233/323/332 are processed with rooted value exactly 0 (tight), yet v(333) = 1 > 0.")
    print("HIT: every value is certified TWO-SIDEDLY: exhaustive minimisation over level-restricted CLOSED node sets (a lower bound: a family tree's node set is closed and cost depends only on that set) meets an explicitly verified tree.")
    print("HIT: the exact budget. The Pareto frontier of (E,A) over closed sets at 333 is {(6,5),(7,6),(8,7),(9,8),(10,9)}, so c*(eta,333) = min E/A = 10/9 exactly, and the budget-critical set (10,9) is NOT the c=1 cost-minimiser (6,5). All 10 marks are load-bearing.")
    print("HIT: the route proposed for this task cannot work. Adding the one mark (2,2,0) changes exactly one site, at level 4, so both realizations agree in membership AND kind on every site of level >= 5 - the whole depth-3 cone of 233 - yet v(233) = 0 while v'(233) = -1. Tightness is not a function of the depth<=3 cone.")
    print("SUMMARY: COUNTEREXAMPLE - the a4 conjecture is false: a processed site CAN have every 1-predecessor processed and tight. The lemma and (H) fail at 333 of an explicit minimal 10-mark realization, c*(eta,333) = 10/9 exactly, and the depth<=3 census route is refuted by two realizations sharing a depth-3 cone with different rooted values.")
else:
    print("SUMMARY: ROUTE FAILS - %d checks failed" % F)
