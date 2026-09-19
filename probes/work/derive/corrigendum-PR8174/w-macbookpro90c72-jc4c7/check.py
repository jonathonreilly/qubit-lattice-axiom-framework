#!/usr/bin/env python3
"""Corrigendum to block 30 (PR #8174), T1: the inequality d_1 <= max(d_2, d_3).

Exact arithmetic only (fractions, integers, sympy polynomial identities).
Every claim printed below is decided here; nothing is quoted on authority.

Objects (block 30's note, "the rule, level time, the deviations", line 84):
  six-axis menu phi(v, v') = p, q, r for equal / antipodal / orthogonal pairs,
  K(v | v_1, v_2, v_3) proportional to prod_j phi(v, v_j),
  d_1 = 1 - K(a|a,a,a), d_2 = 1 - K(a|a,a,-a), d_3 = 1 - K(a|a,a,b), b _|_ a,
  eps_1 := d_1, eps_2 := max(d_2, d_3),
  eta': eta'_x = 1 if >= 2 predecessors are 1; = 1{U_x < eps_2} if exactly one;
        = 1{U_x < eps_1} if none.  xi_x = 1{v_x != a}.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

P, Q, R = sp.symbols("p q r", positive=True)
D1S = P ** 3 + Q ** 3 + 4 * R ** 3
D2S = P * Q * (P + Q) + 4 * R ** 3
D3S = R * (P ** 2 + Q ** 2) + R ** 2 * (P + Q) + 2 * R ** 3
GS = R * P ** 2 + (Q ** 2 + Q * R + 2 * R ** 2) * P - (Q ** 3 + 4 * R ** 3)

results = []


def record(tag, ok, text):
    results.append(bool(ok))
    print(("ok   " if ok else "FAIL ") + tag + " " + text)


def allpos(expr):
    """True when every coefficient of the expanded polynomial is > 0."""
    return all(c > 0 for c in sp.Poly(sp.expand(expr), P, Q, R).coeffs())


# ---------------------------------------------------------------- the menu
# states 0..5 = +e1, -e1, +e2, -e2, +e3, -e3 ; a = 0, -a = 1, orthogonal = 2..5
def phi(i, j, p, q, r):
    if i == j:
        return p
    if i ^ 1 == j:
        return q
    return r


def kernel(preds, p, q, r):
    """The menu's conditional over the six states, exactly."""
    w = [phi(u, preds[0], p, q, r) * phi(u, preds[1], p, q, r) * phi(u, preds[2], p, q, r)
         for u in range(6)]
    tot = sum(w)
    return [x / tot for x in w]


def dev_of(preds, p, q, r):
    """1 - K(a | preds): the site's chance of dissenting from a."""
    return 1 - kernel(preds, p, q, r)[0]


def devs_menu(p, q, r):
    p, q, r = F(p), F(q), F(r)
    return (dev_of((0, 0, 0), p, q, r), dev_of((0, 0, 1), p, q, r), dev_of((0, 0, 2), p, q, r))


def devs(p, q, r):
    """The front matter's closed forms."""
    p, q, r = F(p), F(q), F(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def gval(p, q, r):
    return r * p * p + (q * q + q * r + 2 * r * r) * p - (q ** 3 + 4 * r ** 3)


# C1 -------------------------------------------------- closed forms = menu
lines = [(3, 1, 2), (10, 1, 2), (1, 2, 1), (7, 3, 5), (F(3, 2), F(5, 7), 1), (2, 5, 3)]
ok = all(devs_menu(*t) == devs(*t) for t in lines)
ok = ok and all(dev_of((0, 0, b), F(7), F(3), F(5)) == devs(7, 3, 5)[2] for b in (2, 3, 4, 5))
record("C1", ok, "closed forms = menu conditional, 6 rational lines, any b _|_ a")

# C2 ------------------------------------------------------ sign identities
id1 = sp.expand(P * D2S - Q * D1S - (P - Q) * (Q ** 2 * (P + Q) + 4 * R ** 3))
id2 = sp.expand(P * D3S - R * D1S - R * GS)
id3 = sp.expand(GS - (Q ** 2 * (P - Q) + P * R * (P + Q) + 2 * R ** 2 * (P - 2 * R)))
d1s, d2s, d3s = 1 - P ** 3 / D1S, 1 - P ** 2 * Q / D2S, 1 - P ** 2 * R / D3S
id4 = sp.simplify(d2s - d1s - P ** 2 * (P - Q) * (Q ** 2 * (P + Q) + 4 * R ** 3) / (D1S * D2S))
id5 = sp.simplify(d3s - d1s - P ** 2 * R * GS / (D1S * D3S))
record("C2", all(e == 0 for e in (id1, id2, id3, id4, id5)),
       "p*D2-q*D1=(p-q)(q^2(p+q)+4r^3), p*D3-r*D1=r*g: sgn(d2-d1)=sgn(p-q),")

# C2b ------------------------------- monotonicity in p (T1(a)'s other half)
mono = True
for dd in (d1s, d2s, d3s):
    num, den = sp.fraction(sp.together(-sp.diff(dd, P)))
    mono = mono and allpos(num) and allpos(den)
record("C2b", mono, "  sgn(d3-d1)=sgn(g); -d(d_i)/dp = pos/pos: all three decrease")

# C3 ----------------------------------------------- the failure at (1,2,1)
d = devs(1, 2, 1)
record("C3", d == (F(12, 13), F(4, 5), F(9, 10)) and d[0] > max(d[1], d[2]),
       "(p,q,r)=(1,2,1): d_1=12/13 > 9/10=max(d_2,d_3); p<q and g=-3<0")

# C4 -------------------------------- census: the failure set is {p<q, g<0}
fail, pred = set(), set()
for p, q, r in product(range(1, 8), repeat=3):
    a, b, c = devs(p, q, r)
    if a > max(b, c):
        fail.add((p, q, r))
    if p < q and gval(p, q, r) < 0:
        pred.add((p, q, r))
record("C4", fail == pred and len(fail) == 127,
       "census 1..7: {d_1>max(d_2,d_3)} = {p<q and g<0}, %d of 343" % len(fail))

# C5 ------------------------------------------- the root p* and its bracket
gq = sp.expand(GS.subs(P, Q) - 2 * R * (Q + 2 * R) * (Q - R))
gq2r = sp.expand(GS.subs(P, Q - 2 * R) + 4 * R ** 2 * (Q + R))
g0 = sp.expand(GS.subs(P, 0) + Q ** 3 + 4 * R ** 3)
record("C5", gq == 0 and gq2r == 0 and g0 == 0 and allpos(sp.diff(GS, P)),
       "dg/dp>0, g(0)<0: p* unique; g(q)=2r(q+2r)(q-r), g(q-2r)=-4r^2(q+r)")

# C6 ------------------------ the maximal domain, by the sign identities only
dom = True
for p, q, r in list(product(range(1, 10), repeat=3)) + [(F(3, 2), F(5, 7), 1), (F(1, 3), 2, 1)]:
    a, b, c = devs(p, q, r)
    dom = dom and ((a <= max(b, c)) == (p >= q or gval(p, q, r) >= 0))
record("C6", dom, "census 1..9 + 2 rational: d_1<=max(d_2,d_3) <=> p>=q or g>=0")

# C7 ------------------------------ every line the campaign runs is inside it
camp = {(4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3), (11, 1, 2),
        (453, 1, 2), (232, 1, 1), (905, 2, 4), (677, 1, 3), (367, 1, 2), (368, 1, 2),
        (2921, 1, 2), (1464, 1, 1), (5841, 2, 4), (4380, 1, 3),
        (405, 1, 2), (208, 1, 1), (810, 2, 4), (605, 1, 3)}
inside = all(p >= q and max(devs(p, q, r)) == max(devs(p, q, r)[1:]) for p, q, r in camp)
record("C7", inside, "all %d lines of PRs 8174-8177 have p>=q: eps_2 unmoved" % len(camp))

# C8/C9 ----------------------- explicit witnesses against T1(b) at (1,2,1) -
# Level time tau = x1+x2+x3, predecessors x - e_j; level 0 is all a, eta' = 0.
# One uniform U_x per site drives both chains: v_x = a iff U_x >= dev(v-preds)
# (so xi_x = 1{U_x < dev}), v_x = -a iff U_x < K(-a | v-preds), and eta' by its
# own rule with the note's thresholds.  Each site below is confined to an
# interval of U_x; the product of the lengths is the event's exact probability.
p0, q0, r0 = F(1), F(2), F(1)
dd1, dd2, dd3 = devs(1, 2, 1)
e1, e2 = dd1, max(dd2, dd3)
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
sub = lambda x, e: (x[0] - e[0], x[1] - e[1], x[2] - e[2])
lvl = lambda x: x[0] + x[1] + x[2]
CODE = {"a": 0, "anti": 1, "orth": 2}


def scaffold(cls_g, eps2):
    """Nine sites forced, then report the tenth, (1,1,1).  cls_g sets v at
    (0,1,1), the one predecessor of (1,1,1) whose eta' is 1."""
    plan = [((-1, 1, 1), "anti", 1), ((0, 0, 1), "a", 0), ((0, 1, 0), "a", 0),
            ((1, 0, 0), "a", 0), ((1, -1, 1), "a", 0), ((1, 1, -1), "a", 0),
            ((0, 1, 1), cls_g, 1), ((1, 0, 1), "a", 0), ((1, 1, 0), "a", 0)]
    state, prob = {}, F(1)
    for site, cls, eta in plan:
        preds = [sub(site, e) for e in E]
        pv = tuple(state[y][0] if lvl(y) > 0 else 0 for y in preds)
        ones = sum(state[y][1] if lvl(y) > 0 else 0 for y in preds)
        dev = dev_of(pv, p0, q0, r0)
        thr = F(1) if ones >= 2 else (eps2 if ones == 1 else e1)
        kan = kernel(pv, p0, q0, r0)[1]
        lo, hi = {"a": (dev, F(1)), "anti": (F(0), kan), "orth": (kan, dev)}[cls]
        elo, ehi = (F(0), thr) if eta == 1 else (thr, F(1))
        lo, hi = max(lo, elo), min(hi, ehi)
        if hi <= lo:
            return None
        prob *= hi - lo
        state[site] = (CODE[cls], eta)
    x = (1, 1, 1)
    preds = [sub(x, e) for e in E]
    pv = tuple(state[y][0] for y in preds)
    ones = sum(state[y][1] for y in preds)
    thr = F(1) if ones >= 2 else (eps2 if ones == 1 else e1)
    return prob, dev_of(pv, p0, q0, r0), ones, thr


w = scaffold("a", e2)
lo8, hi8 = w[3], w[1]  # xi_x = 1 with eta'_x = 0  <=>  U_x in [eps_2, d_1)
p8 = w[0] * (hi8 - lo8)
record("C8", w is not None and w[2] == 1 and w[1] == dd1 and hi8 > lo8
       and p8 == F(24, 13 ** 8 * 1300),
       "(1,2,1) 10-site witness: xi=1 > 0=eta' at (1,1,1), P=24/(13^8*1300)")

rep = max(dd1, dd2, dd3)
mins = []
for cls, target in (("a", dd1), ("anti", dd2), ("orth", dd3)):
    s = scaffold(cls, e2)
    mins.append(s is not None and s[0] > 0 and s[2] == 1 and s[1] == target)
srep = scaffold("a", rep)
record("C9", all(mins) and srep is not None and srep[3] >= srep[1],
       "all of (a,a,a),(a,a,-a),(a,a,b) reach such a site: eps_2 >= max(d_i);")
record("C9b", rep == dd1 and srep[3] == rep and srep[3] >= srep[1],
       "  eps_2 := max(d_1,d_2,d_3) closes the window [eps_2, d_1) exactly")

# C10 ------------------------------------ what the repair costs off the domain
coll = all(max(devs(*t)) == devs(*t)[0] for t in fail)
record("C10", coll and len(fail) > 0,
       "off the domain max(d_1,d_2,d_3)=d_1=eps_1: the two levels collapse")

n = len(results)
print("TOTAL: %d/%d exact checks passed" % (sum(1 for z in results if z), n))
if all(results):
    print("SUMMARY: PARTIAL - d_1 <= max(d_2,d_3) holds exactly on p >= min(q,p*), p* the "
          "unique positive root of g = r p^2 + (q^2+qr+2r^2) p - (q^3+4r^3), and q-2r < p* < q "
          "when q > r; off that domain the two-level domination itself fails at an exhibited "
          "10-site configuration of positive probability; eps_2 := max(d_1,d_2,d_3) repairs it "
          "and is minimal; every parameter line of PRs 8174-8177 has p >= q, so no number moves.")
    print("HIT: block 30's T1(a) inequality d_1 <= max(d_2,d_3) is false exactly on "
          "{p < q and g < 0} (127 of the 343 integer triples in 1..7), and there T1(b)'s "
          "coupling xi <= eta' with eps_2 = max(d_2,d_3) fails with positive probability; "
          "eps_2 := max(d_1,d_2,d_3) is the minimal repair.")
else:
    print("SUMMARY: ROUTE FAILS AT the check(s) marked FAIL above")
