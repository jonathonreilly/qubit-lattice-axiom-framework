#!/usr/bin/env python3
"""J:derive:tight-sibling-vacuity:a2 -- exact check of one realization at which the tight-sibling lemma of block 33
(PR #8177) and its rooted inequality (H) fail, and of c*(eta, 333) = 10/9 there (block 32, PR #8176).

Every PASS is decided by integer / Fraction arithmetic.  probes/lib/family.py is imported only as an independent
cross-check (run_automaton, kinds, single_seed_min, verify_tree, tree_counts).  probes/lib/rooted.py (scipy MILP,
floating point) prints INFO lines only and decides nothing.  Definitions: see ATTEMPT.md (quoted from the notes)."""
import os
import sys
from fractions import Fraction as Fr
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", "lib")))
import family as fam  # noqa: E402

PASSES, FAILS = [], []


def check(name, ok, msg):
    (PASSES if ok else FAILS).append(name)
    print(("PASS: " if ok else "FAIL: ") + name + " " + msg)


def s(x):
    return "".join(str(c) for c in x)


# ---------------------------------------------------------------- the realization (block 32's box rule)
MARKS = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 2, 1), (1, 0, 2), (2, 1, 0), (1, 1, 3), (1, 3, 1), (3, 1, 1)]
MSET = set(MARKS)
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def lev(x):
    return x[0] + x[1] + x[2]


def prd(x):
    return [tuple(x[i] - e[i] for i in range(3)) for e in E3]


def sig(x):  # the cyclic coordinate shift (a,b,c) -> (c,a,b)
    return (x[2], x[0], x[1])


def realize(lo, hi):
    """eta on the box [lo,hi]^3, level by level; sites outside the box read 0."""
    eta = {}
    for x in sorted(product(range(lo, hi + 1), repeat=3), key=lev):
        n = sum(eta.get(p, 0) for p in prd(x))
        eta[x] = 1 if (n >= 2 or x in MSET) else 0
    return eta


eta3 = realize(0, 3)
ONE = sorted((x for x, v in eta3.items() if v), key=lambda x: (lev(x), x))
ONESET = set(ONE)
ONE_big = sorted((x for x, v in realize(-2, 6).items() if v), key=lambda x: (lev(x), x))
check("A1", ONE == ONE_big and len(ONE) == 37,
      "box [0,3]^3 and box [-2,6]^3 give the same 37 one-sites (all inside [0,3]^3)")
eta_f = fam.run_automaton(list(product(range(0, 4), repeat=3)), {m: 1 for m in MARKS})
check("A2", {x for x, v in eta_f.items() if v} == ONESET, "probes/lib/family.run_automaton gives the same one-set")
fixed = all((((sum(p in ONESET for p in prd(x)) >= 2) or x in MSET) == (x in ONESET))
            for x in product(range(-1, 5), repeat=3))
check("A3", fixed and MSET <= ONESET,
      "1 on the 37 sites, 0 elsewhere satisfies the rule at every site of [-1,4]^3 (outside [0,4]^3 no site has a 1-predecessor)")

# ---------------------------------------------------------------- kinds
NP = {x: [p for p in prd(x) if p in ONESET] for x in ONE}
KIND = {x: "seed" if not NP[x] else "amp" if len(NP[x]) == 1 else "proc" for x in ONE}
ROW = {}
for x in ONE:
    ROW.setdefault(lev(x), []).append(x)
SEED = (0, 0, 0)
seeds = [x for x in ONE if KIND[x] == "seed"]
amps = {x for x in ONE if KIND[x] == "amp"}
procs = [x for x in ONE if KIND[x] == "proc"]
sizes = [len(ROW[l]) for l in sorted(ROW)]
_, npf, kf = fam.kinds(eta3)
check("B1", seeds == [SEED] and amps == MSET - {SEED} and len(procs) == 27 and kf == KIND
      and sizes == [1, 3, 3, 4, 3, 6, 7, 6, 3, 1] and ROW[9] == [(3, 3, 3)],
      "one seed 000; the nine other marks are exactly the amplified sites; 27 processed; level sizes 1,3,3,4,3,6,7,6,3,1; 333 alone at level 9")
check("B2", NP[(3, 3, 3)] == [(2, 3, 3), (3, 2, 3), (3, 3, 2)] and all(KIND[u] == "proc" for u in NP[(3, 3, 3)]),
      "333 is processed; its 1-predecessors 233,323,332 are processed")

# ---------------------------------------------------------------- exact rooted values (level DP over node sets)
PI = [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 2), (1, 2, 1), (2, 1, 1)]
PISET = set(PI)


def triples(z):
    """the exact set of (E, A, k) over the node sets N of the trees of the family containing z with all levels <= lev(z).
    One seed, so every tree has S = 1, F = 0, and N is such a node set iff SEED, z in N and every non-seed node of N has
    a 1-predecessor in N (ATTEMPT.md S3).  E = #processed, A = #amplified, k = |N & PI|.  State = N & row(l)."""
    L = lev(z)
    states = {frozenset([SEED]): {(0, 0, 0)}}
    for l in range(1, L + 1):
        nxt = {}
        for X, tots in states.items():
            cand = [y for y in ROW.get(l, []) if any(p in X for p in NP[y])]
            for mask in range(1 << len(cand)):
                Y = frozenset(cand[i] for i in range(len(cand)) if mask >> i & 1)
                if l == L and z not in Y:
                    continue
                dE = sum(KIND[y] == "proc" for y in Y)
                dA = sum(KIND[y] == "amp" for y in Y)
                dk = sum(y in PISET for y in Y)
                nxt.setdefault(Y, set()).update((e + dE, a + dA, k + dk) for (e, a, k) in tots)
        states = nxt
    return set().union(*states.values()) if states else set()


TR = {z: triples(z) for z in ONE}
V = {z: min(e - a for (e, a, k) in TR[z]) for z in ONE}   # cost at c = 1 (S = 1): E - A
tab = " | ".join(f"{l}:" + " ".join(f"{s(x)}{KIND[x][0]}{V[x]}" for x in ROW[l]) for l in sorted(ROW))
print("v at c=1 by level (s/a/p = seed/amplified/processed): " + tab)
H_rest = all(V[x] <= 0 for x in procs if x != (3, 3, 3)) and all(V[x] <= -1 for x in amps)
check("C1", V[(3, 3, 3)] == 1 and all(V[u] == 0 for u in NP[(3, 3, 3)]) and H_rest,
      "v(333) = 1 while v(233) = v(323) = v(332) = 0; (H) holds at the other 36 one-sites")
tight = sorted(x for x in procs if V[x] == 0)
check("C2", tight == [(2, 3, 3), (3, 2, 3), (3, 3, 2)], "the tight processed sites are exactly 233, 323, 332")

# independent cross-check: the library's top-down single-seed DP on eta truncated at the root's level (the level cap)
ok = True
for z in ONE:
    trunc = {x: v for x, v in eta3.items() if lev(x) <= lev(z)}
    best, sd, nodes = fam.single_seed_min(trunc, z, 1)
    ok = ok and sd == [SEED] and best == V[z]
check("D1", ok, "probes/lib/family.single_seed_min on eta truncated at level(z) equals v(z) at all 37 sites")

# ---------------------------------------------------------------- explicit optimal trees
T233 = ["000", "001", "010", "100", "101", "102", "112", "113", "123", "133", "233"]
A233 = [("001", "000"), ("010", "000"), ("100", "000"), ("101", "100"), ("102", "101"), ("112", "102"),
        ("113", "112"), ("123", "113"), ("133", "123"), ("233", "133")]
T333 = ["000", "001", "010", "100", "011", "101", "110", "021", "102", "210", "112", "121", "211", "113", "131",
        "311", "123", "133", "233", "333"]
A333 = [("001", "000"), ("010", "000"), ("100", "000"), ("011", "001"), ("101", "100"), ("110", "010"),
        ("021", "011"), ("102", "101"), ("210", "110"), ("112", "102"), ("121", "021"), ("211", "210"),
        ("113", "112"), ("131", "121"), ("311", "211"), ("123", "113"), ("133", "123"), ("233", "133"), ("333", "233")]


def t(w):
    return tuple(int(ch) for ch in w)


def tree_ok(root, nodes, arrows, f=lambda x: x):
    ns = [f(t(w)) for w in nodes]
    ar = [(f(t(a)), f(t(b))) for a, b in arrows]
    good = fam.verify_tree(eta3, f(t(root)), ns, ar, []) and max(lev(x) for x in ns) <= lev(f(t(root)))
    return good, fam.tree_counts(eta3, ns)


res = [tree_ok("233", T233, A233, f) for f in (lambda x: x, sig, lambda x: sig(sig(x)))]
check("E1", all(g and c == (5, 5, 1) for g, c in res),
      "tree at 233 (and its images at 323, 332 under (a,b,c)->(c,a,b)): valid, level-capped, (E,A,S) = (5,5,1), cost 0")
g333, c333 = tree_ok("333", T333, A333)
check("E2", g333 and c333 == (10, 9, 1), "tree at 333: valid, (E,A,S) = (10,9,1), cost 1, E/A = 10/9")

# ---------------------------------------------------------------- premises of the hand lower bound (ATTEMPT.md S5)
up = sorted(a for a in amps if lev(a) > 1)
prem = (all(KIND[p] == "proc" for p in PI) and {lev(p) for p in PI} == {2, 4}
        and all(NP[a] == [SEED] for a in amps if lev(a) == 1) and len([a for a in amps if lev(a) == 1]) == 3
        and sorted(NP[a][0] for a in up) == sorted(PI) and len(up) == 6
        and all(KIND[x] == "proc" and x not in PISET for l in (6, 7, 8, 9) for x in ROW[l]))
check("F1", prem, "PI = {011,101,110,112,121,211} processed at levels 2,4; amplified 001,010,100 -> 000; the other six "
      "amplified sites -> distinct members of PI (a bijection); levels 6-9 hold processed sites only, none in PI")
b333 = all(e >= k + 4 and a <= k + 3 for (e, a, k) in TR[(3, 3, 3)])
b8 = all(e >= k + 3 and a <= k + 3 for u in ROW[8] for (e, a, k) in TR[u])
check("F2", b333 and b8, "on the exact DP output: E >= k+4, A <= k+3 at 333 and E >= k+3, A <= k+3 at level 8")

# ---------------------------------------------------------------- the family's value at (eta, 333)
P333 = {(e, a) for (e, a, k) in TR[(3, 3, 3)]}
ratios = [Fr(e, a) for (e, a) in P333 if a >= 1]
cstar = min(ratios)
no_A0 = all(e >= 4 for (e, a) in P333 if a == 0)
c_lo = Fr(10, 9) - Fr(1, 1000)
check("G1", cstar == Fr(10, 9) and (10, 9) in P333 and no_A0
      and min(e - Fr(10, 9) * a for (e, a) in P333) == 0 and min(e - c_lo * a for (e, a) in P333) > 0
      and max(lev(x) for x in ONE) == 9,
      f"c*(eta,333) = min E/A = {cstar} over {len(P333)} (E,A) pairs (every tree; no one-site above 333); "
      "the budget E <= c|A| holds for some tree iff c >= 10/9")

# ---------------------------------------------------------------- symmetry
check("H1", {sig(m) for m in MARKS} == MSET and {sig(x) for x in ONE} == ONESET
      and all(KIND[sig(x)] == KIND[x] and V[sig(x)] == V[x] for x in ONE),
      "marks, one-set, kinds and v are invariant under (a,b,c)->(c,a,b)")

# ---------------------------------------------------------------- the floor of block 32's T4.2 at c >= 10/9
b = Fr(4, 27)
t1 = Fr(2, 27)
ctrl = (t1 * (b - t1) == Fr(4, 729) and not 729 * (2 * 367 + 11) < 4 * (367 ** 2 + 2 * 367 + 11)
        and 729 * (2 * 368 + 11) < 4 * (368 ** 2 + 2 * 368 + 11))
check("I1", ctrl, "c = 1 control: max t(4/27-t) = 4/729 at t = 2/27; d_3 < 4/729 fails at p = 367, holds at 368 (block 32's E2)")
ts = Fr(40, 513)
check("I2", Fr(10, 9) * (b - ts) == ts and b - ts == Fr(36, 513),
      "t* = 40/513 is the stationary point of t^(10/9)(4/27 - t): (10/9)(4/27 - t*) = t*, 4/27 - t* = 36/513")
dec = all(2 * (p * p + 2 * p + 11) - (2 * p + 11) * (2 * p + 2) == -2 * p * p - 22 * p for p in range(0, 12))
check("I3", dec, "d_3 = (2p+11)/(p^2+2p+11) has derivative numerator -2p^2-22p (identity of degree 2, checked at 12 points)")


def holds(p):  # d_3(p) < h* = (40/513)^(10/9) (36/513), both sides raised to the 9th power
    return (2 * p + 11) ** 9 * 513 ** 19 < 40 ** 10 * 36 ** 9 * (p * p + 2 * p + 11) ** 9


P1 = next(p for p in range(1, 100000) if holds(p))
check("I4", P1 == 489 and not any(holds(p) for p in range(1, 489)) and all(holds(p) for p in range(489, 5001)),
      f"d_3 < h* fails for every p <= {P1 - 1} and holds for 489 <= p <= 5000 (exact integers)")

# ---------------------------------------------------------------- INFO: floating-point MILP (decides nothing)
try:
    import rooted as R
    agree = []
    for z in ONE:
        val, info = R.rooted(eta3, z, 1.0)
        agree.append(val is not None and abs(val - V[z]) < 1e-6)
    val, info = R.rooted(eta3, (3, 3, 3), 1.0)
    print(f"INFO: probes/lib/rooted.py MILP agrees with the exact DP at {sum(agree)}/37 sites; at 333 value {val:g}, "
          f"(E,A,S) = ({info['E']},{info['A']},{info['S']})")
except Exception as exc:  # the MILP is optional
    print(f"INFO: MILP cross-check not run ({type(exc).__name__})")

# ---------------------------------------------------------------- verdict
print(f"TOTAL: PASS={len(PASSES)} FAIL={len(FAILS)}")
if FAILS:
    print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} (a check of this script failed; no claim is made)")
    sys.exit(1)
print("HIT: counterexample to block 33's tight-sibling lemma and (H): marks {000,001,010,100,021,102,210,113,131,311} "
      "(one seed, nine amplified) give 37 one-sites in [0,3]^3; 333 is processed, its 1-predecessors 233,323,332 are "
      "processed and tight (v=0), yet v(333)=1 (exact level DP; hand bound E>=k+4, A<=k+3); (H) holds at the other 36")
print("HIT: c*(eta,333)=10/9 exactly (tree E=10, A=9, S=1; every tree has E/A>=10/9), so block 32's constant "
      "c*>=10/9 and the unit budget c=1 fails at this realization")
print("HIT: with block 32 T4.2's inputs (t+eps2/t^c<4/27, eps2>=d_3=(2p+11)/(p^2+2p+11) on (p,1,2)), c>=10/9 needs "
      "d_3<max t^(10/9)(4/27-t) (t*=40/513): false for p<=488, true from 489, so T4.2's floor moves from 367 to 488")
print("SUMMARY: COUNTEREXAMPLE to the task's statement, block 33's tight-sibling lemma and (H): at a one-seed "
      "realization in [0,3]^3 the processed site 333 has three tight processed 1-predecessors and rooted value 1; "
      "c*(eta,333)=10/9, so block 32's c*>=10/9 and routes through the unit budget (453; block 33's c=1 certificates) "
      "are unavailable; conditional on T4.2's inputs the (p,1,2) floor is p<=488")
