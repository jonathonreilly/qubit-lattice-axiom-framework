#!/usr/bin/env python3
"""J:derive:kappa-from-the-rule:a2 -- the one number of block 53 against block 50's clock and block 55's pulls.

Objects (supplied clauses, not adopted): block 53 (PR #8568): u = log w, a record is a source log kappa,
u_x - (1/6) sum_e u_{x+e} = (log kappa) n_x, kappa = w_x / F(neighbours' rates) with F of the degree-one
class (the geometric mean makes the law exact). Block 50 (PR #8562): the local clock, the event of the
record at x runs at rate 1/pi_x, pi_x the product of the pair weights c*omega at x (omega = p, q, r for
equal, opposite, orthogonal contents), neutral scale c0 = 6/(p + q + 4r). Block 55 (PR #8571): the
weak-field law u_x - avg = -(gamma/6)(e_x - mu)/wbar and the pull -E grad u (block 54, PR #8570).
Families: A kappa of block 50's clock at (p,q,r) = (3,1,2), exact; B the rate field of that clock and its
sources; C the pulls; D gamma. Exact: Fractions and sympy.
"""
import itertools
import sys
from fractions import Fraction as F

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    print(("ok " if cond else "FAIL ") + tag + (" " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


p, q, r = F(3), F(1), F(2)
c0 = 6 / (p + q + 4 * r)
W = {"equal": c0 * p, "opposite": c0 * q, "orthogonal": c0 * r}
MULT = {"equal": 1, "opposite": 1, "orthogonal": 4}           # partner contents relative to the record's
ok("A.c0", c0 == F(1, 2) and W == {"equal": F(3, 2), "opposite": F(1, 2), "orthogonal": F(1)},
   "c0 = 1/2; pair weights c0 p, c0 q, c0 r = 3/2, 1/2, 1 (c0 r = 1 since p + q = 2r)")
ok("A.neutral", sum(MULT[k] * W[k] for k in W) / 6 == 1, "mean pair weight over the partner's six contents = 1")

# ---------------------------------------------------------------- A kappa of the local clock
# rates: w = 1/pi at every site; an empty site and an isolated record have pi = 1.
def kappa_arith(wx, wn):
    return wx / (sum(wn) / 6)


# isolated record
ok("A.isolated", kappa_arith(F(1), [F(1)] * 6) == 1, "isolated record: pi_x = 1, all neighbours at rate 1: kappa = 1 exactly (both means)")
rows = []
one = {}
for k_, cw in W.items():
    ka = kappa_arith(1 / cw, [1 / cw] + [F(1)] * 5)
    one[k_] = ka
    rows.append("%s: arith %s, geometric (c w)^(-5/6) = %s^(-5/6)" % (k_, ka, cw))
ok("A.one", one == {"equal": F(12, 17), "opposite": F(12, 7), "orthogonal": F(1)},
   "one record neighbour: kappa = 6/(1 + 5 c w): " + "; ".join(rows))
two = {}
for (k1, cw1), (k2, cw2) in itertools.combinations_with_replacement(W.items(), 2):
    wx = 1 / (cw1 * cw2)
    two[(k1, k2)] = kappa_arith(wx, [1 / cw1, 1 / cw2] + [F(1)] * 4)
ok("A.two", two[("equal", "equal")] == F(1, 2) and two[("opposite", "opposite")] == 3 and two[("orthogonal", "orthogonal")] == 1,
   "two record neighbours (not adjacent to each other): kappa = (1/pi_x)/((1/(c w1) + 1/(c w2) + 4)/6): "
   + ", ".join("%s-%s %s" % (a, b, v) for (a, b), v in two.items()))
below = {k_: v < 1 for k_, v in one.items()}
ok("A.below", below == {"equal": True, "opposite": False, "orthogonal": False},
   "below one only next to equal contents (aligned); above one next to opposite contents; exactly one next to orthogonal ones")
# averages over the partner's content
unif = sum(MULT[k_] * one[k_] for k_ in W) / 6
stat_w = {k_: MULT[k_] * W[k_] for k_ in W}
stat = sum(stat_w[k_] * one[k_] for k_ in W) / sum(stat_w.values())
L = {k_: sp.log(sp.Rational(W[k_].numerator, W[k_].denominator)) for k_ in W}
glog_unif = sp.simplify(sum(MULT[k_] * (-sp.Rational(5, 6)) * L[k_] for k_ in W) / 6)
glog_stat = sp.simplify(sum(stat_w[k_] * (-sp.Rational(5, 6)) * L[k_] for k_ in W) / sum(stat_w.values()))
ok("A.average", unif == F(382, 357) and stat == F(352, 357) and sp.N(glog_unif) > 0 and sp.N(glog_stat) < 0,
   "arithmetic kappa averaged uniformly over the partner: 382/357 > 1; under the stationary pair law: %s < 1; "
   "mean log kappa (geometric): uniform %.4f > 0, stationary %.4f < 0: the sign depends on the average"
   % (stat, float(sp.N(glog_unif)), float(sp.N(glog_stat))))

# ---------------------------------------------------------------- B the local clock as a rate field
# With w = 1/pi at every site, u = -log pi and log kappa_geo(x) = u_x - (1/6) sum u_y = -((1 - A) log pi)_x.
# On a torus the sources sum to zero and the field is confined to the records with neighbours.
Lt = 3
SITES = list(itertools.product(range(Lt), repeat=3))
NB = {x: [tuple((x[i] + (d if i == j else 0)) % Lt for i in range(3)) for j in range(3) for d in (-1, 1)] for x in SITES}
E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def rel(a, b):
    if a == b:
        return "equal"
    if E6[a] == tuple(-t for t in E6[b]):
        return "opposite"
    return "orthogonal"


sym = {k_: sp.Symbol("l_" + k_) for k_ in W}        # l_omega = log(c omega), formal
good = True
tot_ok = True
import random
random.seed(11)
for trial in range(40):
    n = random.randint(1, 6)
    occ = dict(zip(random.sample(SITES, n), [random.randrange(6) for _ in range(n)]))
    logpi = {}
    for x in SITES:
        acc = sp.Integer(0)
        if x in occ:
            for y in NB[x]:
                if y in occ:
                    acc += sym[rel(occ[x], occ[y])]
        logpi[x] = acc
    u = {x: -logpi[x] for x in SITES}
    src = {x: sp.expand(sp.sympify(u[x]) - sp.Rational(1, 6) * sum(sp.sympify(u[y]) for y in NB[x])) for x in SITES}
    tot_ok &= sp.expand(sum(src.values())) == 0
    good &= all(src[x] == 0 for x in SITES if logpi[x] == 0 and all(logpi[y] == 0 for y in NB[x]))
ok("B.zero_total", tot_ok, "40 random record configurations on the 3^3 torus: the sources log kappa of the local clock sum to zero exactly")
ok("B.local", good, "and vanish at every site whose own and neighbours' pair weights are one: the field u = -log pi has no tail")

# ---------------------------------------------------------------- C equal and opposite pulls
EA, EB, SA, SB, g1 = sp.symbols("E_A E_B S_A S_B gprime")
FA = -EA * SB * g1          # pull on A in B's field u_B = S_B G(x - x_B), G even: grad at x_A is g'
FB = +EB * SA * g1          # pull on B in A's field: the gradient flips sign
ok("C.sum", sp.expand(FA + FB - (-(EA * SB - EB * SA) * g1)) == 0,
   "pull on A + pull on B = -(E_A S_B - E_B S_A) grad G: zero at every separation iff S_A/E_A = S_B/E_B")
gam, Erec = sp.symbols("gamma E_rec", positive=True)
S_packet_per_E = -gam / 6          # block 55's law u_x - avg = -(gamma/6) e_x/wbar
logkappa = sp.solve(sp.Eq(sp.Symbol("lk") / Erec, S_packet_per_E), sp.Symbol("lk"))[0]
ok("C.kappa", sp.simplify(logkappa + gam * Erec / 6) == 0,
   "a record with block 53's source log kappa and a packet with block 55's pull equally only if log kappa = -(gamma/6) E_rec")
print("   so kappa = exp(-gamma E_rec/6): the free number becomes the record's energy E_rec in ambient ticks, "
      "with gamma universal; a block 54 walker at rest has none (no 2x2 rest term anticommutes with H), so kappa = 1")

# ---------------------------------------------------------------- D gamma
print("   gamma is the coefficient of the supplied field energy F = (2/gamma) sum (phi_x - phi_y)^2; every gamma > 0 "
      "meets blocks 53-55 (covariance, weight one, kept ledger, action = reaction): nothing in them fixes gamma "
      "(ATTEMPT.md step 7); the pull at weak field is -(gamma/(4 pi)) E_A E_B / R")

if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: block 50's local clock gives an isolated record kappa = 1 exactly and a record with neighbours a kappa that "
    "depends on their contents (at (3,1,2), c0 = 1/2: one neighbour 12/17, 12/7, 1 for equal, opposite, orthogonal; two "
    "equal 1/2, two opposite 3); read as block 53's rate field it is exactly u = -log pi, so its sources log kappa sum "
    "to zero on every torus and it has no far field: it cannot be block 53's kappa.",
    "HIT: a record that sources block 53's field and falls as block 54's packets do pulls a packet equally and "
    "oppositely only if log kappa = -(gamma/6) E_rec (block 55's gamma): kappa gives way to the record's energy, which "
    "a block 54 walker at rest does not have; gamma itself is left free by every present clause.",
]
print("SUMMARY: PARTIAL kappa of block 50's clock is 1 for an isolated record and configuration-dependent otherwise, "
      "with sources that sum to zero (no far field); equal pulls force log kappa = -(gamma/6)E_rec; nothing fixes gamma")
print("\n".join(HITS))
