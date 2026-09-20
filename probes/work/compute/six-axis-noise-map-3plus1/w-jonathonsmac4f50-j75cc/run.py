#!/usr/bin/env python3
"""C:six-axis-noise-map-3plus1:a1   worker w-jonathonsmac4f50-j75cc (claude-opus-5)

Block 12's exact noise map with FOUR recorded predecessors (the 3+1 backward neighbourhood).
The six-axis record takes axis a with probability proportional to prod_j W(a, s_j),
W(a,s) = p if a = s, q if a = -s, r if a is orthogonal to s.

A1  the predecessor patterns up to the cube group, with the exact law of each as a rational function of (p,q,r)
A2  block 30's two domination parameters: leaving a unanimous neighbourhood, following the minority of a 3-1
A3  the 2-2 ties, which four predecessors have and three do not
N1  brute-force check of every formula at three random rational weights
"""
import time
from fractions import Fraction
from itertools import combinations_with_replacement, permutations, product
import sympy as sp

t0 = time.time()
p, q, r = sp.symbols("p q r", positive=True)
AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
OPP = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
def W(a, s): return p if a == s else (q if a == OPP[s] else r)
def law(multiset, weights=(p, q, r)):
    pp, qq, rr = weights
    def w(a, s): return pp if a == s else (qq if a == OPP[s] else rr)
    num = [sp.prod([w(a, s) for s in multiset]) for a in range(6)]
    tot = sum(num)
    return [sp.simplify(n / tot) for n in num]

# the cube group as signed permutations of the coordinates, acting on the six axes
group = []
for perm in permutations(range(3)):
    for signs in product((1, -1), repeat=3):
        mapping = {}
        for i, v in enumerate(AX):
            wvec = [0, 0, 0]
            for j in range(3): wvec[perm[j]] = signs[perm[j]] * v[j]
            mapping[i] = AX.index(tuple(wvec))
        group.append(tuple(mapping[i] for i in range(6)))
group = sorted(set(group))
print(f"A1 the cube group acting on the six axes has {len(group)} elements")

def canon(ms):
    return min(tuple(sorted(g[s] for s in ms)) for g in group)
multisets = list(combinations_with_replacement(range(6), 4))
orbits = {}
for ms in multisets: orbits.setdefault(canon(ms), []).append(ms)
print(f"A1 {len(multisets)} multisets of four predecessors fall into {len(orbits)} orbits")

def describe(ms):
    cnt = {}
    for s in ms: cnt[s] = cnt.get(s, 0) + 1
    mult = sorted(cnt.values(), reverse=True)
    axes = sorted(cnt)
    pairs = []
    for a, b in combinations_with_replacement(axes, 2):
        if a != b: pairs.append("opposite" if OPP[a] == b else "orthogonal")
    return "-".join(map(str, mult)) + (" (" + ", ".join(sorted(set(pairs))) + ")" if pairs else " (unanimous)")

rows = []
for rep in sorted(orbits):
    L = law(rep)
    rows.append((rep, describe(rep), len(orbits[rep]), L))
    nz = [(AX[a], sp.factor(L[a])) for a in range(6) if L[a] != 0]
    print(f"A1 pattern {describe(rep)}: representative {[AX[s] for s in rep]}, orbit size {len(orbits[rep])}")
    print(f"A1   law: " + ", ".join(f"P({v}) = {sp.factor(L[a])}" for a, v in zip(range(6), [AX[i] for i in range(6)])))
# every member of an orbit must give the same law up to relabelling
same = True
for rep, members in orbits.items():
    base = law(rep)
    for ms in members:
        gg = next(g for g in group if tuple(sorted(g[s] for s in ms)) == rep)
        Lm = law(ms)
        for a in range(6):
            if sp.simplify(Lm[a] - base[gg[a]]) != 0: same = False
print(f"A1 every multiset in an orbit gives its representative's law relabelled by the group element: {same}")

# ---------------------------------------------------------------- A2 the domination parameters
unan = law((0, 0, 0, 0))
leave = sp.factor(sp.simplify(1 - unan[0]))
claim = (q ** 4 + 4 * r ** 4) / (p ** 4 + q ** 4 + 4 * r ** 4)
print(f"A2 leaving a unanimous neighbourhood: 1 - P(same axis) = {sp.simplify(sp.expand(leave))} "
      f"(factored: {leave})")
print(f"A2 equals the task's (q^4 + 4 r^4)/(p^4 + q^4 + 4 r^4):", sp.simplify(leave - claim) == 0)
op31 = law((0, 0, 0, 1))          # three +e, one -e
or31 = law((0, 0, 0, 2))          # three +e, one orthogonal
min_op = sp.factor(op31[1]); min_or = sp.factor(or31[2])
print(f"A2 3-1 with the odd one opposite: P(minority) = {min_op}")
print(f"A2 3-1 with the odd one orthogonal: P(minority) = {min_or}")
b = sp.Symbol("b", positive=True)
for name, sub in (("(p,1,2)", {q: 1, r: 2}), ("(e^b, e^-b, 1)", {p: sp.exp(b), q: sp.exp(-b), r: 1})):
    print(f"A2 on {name}: leave = {sp.simplify(leave.subs(sub))}")
    print(f"A2 on {name}: minority opposite = {sp.simplify(min_op.subs(sub))}, "
          f"minority orthogonal = {sp.simplify(min_or.subs(sub))}")
print("A2 numerically on (p,1,2): p | leave | minority opposite | minority orthogonal")
for pv in (1, 2, 4, 8, 16, 84, 4165):
    s = {p: sp.Integer(pv), q: 1, r: 2}
    print(f"A2   p={pv:5d}: {float(leave.subs(s)):.6f}  {float(min_op.subs(s)):.3e}  {float(min_or.subs(s)):.3e}")
print("A2 numerically on (e^b, e^-b, 1): b | leave | minority opposite | minority orthogonal")
for bv in (0.5, 1, 2, 3, 5):
    s = {p: sp.exp(sp.Float(bv)), q: sp.exp(-sp.Float(bv)), r: 1}
    print(f"A2   b={bv}: {float(leave.subs(s)):.6f}  {float(min_op.subs(s)):.3e}  {float(min_or.subs(s)):.3e}")

# ---------------------------------------------------------------- A3 the ties
print("A3 the 2-2 patterns, which need an even number of predecessors and so do not occur with three:")
for rep in sorted(orbits):
    cnt = {}
    for s in rep: cnt[s] = cnt.get(s, 0) + 1
    if sorted(cnt.values(), reverse=True) == [2, 2]:
        L = law(rep); axes = sorted(cnt)
        print(f"A3   {[AX[s] for s in rep]} ({'opposite' if OPP[axes[0]] == axes[1] else 'orthogonal'} pair): " +
              ", ".join(f"P({AX[a]}) = {sp.factor(L[a])}" for a in range(6)))
        print(f"A3     the two carried axes are exactly tied: "
              f"{sp.simplify(L[axes[0]] - L[axes[1]]) == 0}, at probability {sp.factor(L[axes[0]])} each")
print("A3 with three predecessors the patterns are 3, 2-1 and 1-1-1: no two axes can carry two predecessors each,")
print("A3 so the strict majority of a 2-1 always has the larger weight when p > q, r. For comparison:")
for ms3 in ((0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 2, 4)):
    L3 = law(ms3)
    print(f"A3   three predecessors {[AX[s] for s in ms3]}: " +
          ", ".join(f"P({AX[a]}) = {sp.factor(L3[a])}" for a in range(6) if L3[a] != 0))

# ---------------------------------------------------------------- N1 brute force
print("N1 brute-force check: for three random rational (p,q,r), every orbit's law recomputed by direct")
print("N1 enumeration of the six numerators, compared with the symbolic formula evaluated there")
import random
random.seed(7)
bad = 0; total = 0
for trial in range(3):
    pv = Fraction(random.randint(1, 40), random.randint(1, 9))
    qv = Fraction(random.randint(1, 40), random.randint(1, 9))
    rv = Fraction(random.randint(1, 40), random.randint(1, 9))
    def wf(a, s): return pv if a == s else (qv if a == OPP[s] else rv)
    worst = Fraction(0)
    for rep, desc, size, L in rows:
        num = []
        for a in range(6):
            x = Fraction(1)
            for s in rep: x *= wf(a, s)
            num.append(x)
        tot = sum(num)
        for a in range(6):
            direct = num[a] / tot
            sym = sp.Rational(L[a].subs({p: sp.Rational(pv.numerator, pv.denominator),
                                         q: sp.Rational(qv.numerator, qv.denominator),
                                         r: sp.Rational(rv.numerator, rv.denominator)}))
            d = abs(Fraction(int(sym.p), int(sym.q)) - direct)
            worst = max(worst, d); total += 1
            if d != 0: bad += 1
    # the stated expectation, checked the same way
    un = [Fraction(1)] * 6
    for a in range(6):
        x = Fraction(1)
        for s in (0, 0, 0, 0): x *= wf(a, s)
        un[a] = x
    lv = 1 - un[0] / sum(un)
    exp_lv = (qv ** 4 + 4 * rv ** 4) / (pv ** 4 + qv ** 4 + 4 * rv ** 4)
    print(f"N1 (p,q,r) = ({pv}, {qv}, {rv}): worst deviation over all {len(rows)} orbits {worst}; "
          f"leaving a unanimous neighbourhood {lv} equals (q^4+4r^4)/(p^4+q^4+4r^4): {lv == exp_lv}")
print(f"N1 all {total} probabilities agreed exactly with the symbolic laws: {bad == 0}")
print(f"SUMMARY: with four predecessors the 126 multisets fall into {len(orbits)} cube-group orbits whose laws are "
      f"given exactly above; leaving a unanimous neighbourhood has probability (q^4+4r^4)/(p^4+q^4+4r^4) as stated "
      f"({float(leave.subs({p: sp.Integer(84), q: 1, r: 2})):.3e} at (84,1,2), "
      f"{float(leave.subs({p: sp.Integer(4165), q: 1, r: 2})):.3e} at (4165,1,2)), following the minority of a 3-1 "
      f"neighbourhood has "
      f"{min_op} when the odd one is opposite and {min_or} when it is orthogonal, and the 2-2 patterns tie their "
      f"two carried axes exactly - a case three predecessors "
      f"cannot produce; every formula reproduced by brute force at three random rational weights; {time.time()-t0:.0f}s")
