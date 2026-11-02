#!/usr/bin/env python3
"""ol55_1 -- exact-arithmetic convention checks for OSLEAF55 (criteria: checks/ol55_1_criteria.md).
Plain python, fractions only. Complex numbers are pairs (re, im) of Fractions. Not a Yang-Mills computation."""
from fractions import Fraction as Fr
from itertools import product, combinations
import random
import sys

results = {}

# ---------------- G1: clover count ----------------
def plaquettes_with_corner_origin(d):
    seen = set()
    for mu, nu in combinations(range(d), 2):
        e_mu = tuple(1 if i == mu else 0 for i in range(d))
        e_nu = tuple(1 if i == nu else 0 for i in range(d))
        for cmu in (0, -1):
            for cnu in (0, -1):
                base = tuple(cmu * e_mu[i] + cnu * e_nu[i] for i in range(d))
                corners = frozenset([
                    base,
                    tuple(base[i] + e_mu[i] for i in range(d)),
                    tuple(base[i] + e_nu[i] for i in range(d)),
                    tuple(base[i] + e_mu[i] + e_nu[i] for i in range(d)),
                ])
                assert tuple([0] * d) in corners
                seen.add((mu, nu, corners))
    return seen

p4 = plaquettes_with_corner_origin(4)
n_unordered = len(p4)
n_ordered_terms = 2 * n_unordered  # ordered pairs (mu,nu) and (nu,mu) both sum the same 4 plaquettes
max_a4_e = Fr(n_ordered_terms * 2, 4)  # s <= 2, prefactor 1/4
g1 = (n_unordered == 24) and (n_ordered_terms == 48) and (max_a4_e == 24)
x1_fires = (len(plaquettes_with_corner_origin(3)) != 24)
results['G1'] = g1
results['X1_fires'] = x1_fires
print(f"G1: unordered plaquettes with corner 0 in Z^4 = {n_unordered}; ordered clover terms = {n_ordered_terms}; "
      f"max a^4 e_a = {max_a4_e}; PASS={g1}")
print(f"X1: Z^3 count = {len(plaquettes_with_corner_origin(3))}; control fires = {x1_fires}")

# ---------------- G2: (2n)^{5n} <= ((5n)!)^2 ----------------
def fact(k):
    r = 1
    for i in range(2, k + 1):
        r *= i
    return r

g2 = all((2 * n) ** (5 * n) <= fact(5 * n) ** 2 for n in range(1, 101))
x2_fires = any(not ((2 * n) ** (5 * n) <= fact(2 * n) ** 2) for n in range(1, 101))
results['G2'] = g2
results['X2_fires'] = x2_fires
print(f"G2: (2n)^(5n) <= ((5n)!)^2 for n=1..100: PASS={g2}")
print(f"X2: false variant (2n)^(5n) <= ((2n)!)^2 fails for some n: control fires = {x2_fires}")

# ---------------- G3: OS form = <Theta(A)^* A> on a toy chain ----------------
def cadd(a, b): return (a[0] + b[0], a[1] + b[1])
def cmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def cconj(a): return (a[0], -a[1])
def creal(x): return (Fr(x), Fr(0))
ZERO = (Fr(0), Fr(0))

TIMES = list(range(-3, 4))
V = [Fr(1), Fr(0), Fr(-1)]  # field value of each state

def path_measure(P, pi):
    """list of (prob, path dict t->state) for the stationary chain on TIMES"""
    out = []
    for states in product(range(3), repeat=len(TIMES)):
        pr = pi[states[0]]
        for i in range(len(states) - 1):
            pr *= P[states[i]][states[i + 1]]
        if pr != 0:
            out.append((pr, dict(zip(TIMES, states))))
    return out

def moment(paths, ts):
    s = Fr(0)
    for pr, path in paths:
        term = pr
        for t in ts:
            term *= V[path[t]]
            if term == 0:
                break
        s += term
    return s

ORD = {0: [()], 1: [(1,), (2,), (3,)], 2: [(1, 2), (1, 3), (2, 3)], 3: [(1, 2, 3)]}

def random_F(rng):
    F = {}
    for n in range(4):
        F[n] = {}
        for tup in ORD[n]:
            if rng.random() < 0.8:
                F[n][tup] = (Fr(rng.randint(-9, 9), rng.randint(1, 9)), Fr(rng.randint(-9, 9), rng.randint(1, 9)))
    return F

def theta_star(Fn, x, use_conj=True):
    # (Theta F^*)(x_1..x_n) := conj F(-x_n, ..., -x_1)
    arg = tuple(-xi for xi in reversed(x))
    val = Fn.get(arg, ZERO)
    return cconj(val) if use_conj else val

def Q_OS(F, paths, mom_cache, use_conj=True):
    total = ZERO
    for n in range(4):
        for m in range(4):
            if not F[n] or not F[m]:
                continue
            for x in product(TIMES, repeat=n):
                tx = theta_star(F[n], x, use_conj)
                if tx == ZERO:
                    continue
                for y, Fy in F[m].items():
                    key = tuple(x) + tuple(y)
                    if key not in mom_cache:
                        mom_cache[key] = moment(paths, key)
                    total = cadd(total, cmul(cmul(tx, Fy), creal(mom_cache[key])))
    return total

def Q_dir(F, paths):
    total = ZERO
    for pr, path in paths:
        A = ZERO
        Atheta = ZERO
        for n in range(4):
            for tup, val in F[n].items():
                prod_phi = Fr(1)
                prod_phi_theta = Fr(1)
                for t in tup:
                    prod_phi *= V[path[t]]
                    prod_phi_theta *= V[path[-t]]
                A = cadd(A, cmul(val, creal(prod_phi)))
                Atheta = cadd(Atheta, cmul(val, creal(prod_phi_theta)))
        total = cadd(total, cmul(creal(pr), cmul(cconj(Atheta), A)))
    return total

P_rev = [[Fr(1, 2), Fr(1, 4), Fr(1, 4)], [Fr(1, 4), Fr(1, 2), Fr(1, 4)], [Fr(1, 4), Fr(1, 4), Fr(1, 2)]]
pi_u = [Fr(1, 3)] * 3
paths_rev = path_measure(P_rev, pi_u)
rng = random.Random(55)
cache = {}
g3 = True
x3a_fires = False
for k in range(200):
    F = random_F(rng)
    qo = Q_OS(F, paths_rev, cache)
    qd = Q_dir(F, paths_rev)
    if not (qo == qd and qo[1] == 0 and qo[0] >= 0):
        g3 = False
        print(f"G3 failure at sample {k}: Q_OS={qo}, Q_dir={qd}")
    qn = Q_OS(F, paths_rev, cache, use_conj=False)
    if qn != qd:
        x3a_fires = True
results['G3'] = g3
results['X3a_fires'] = x3a_fires
print(f"G3: Q_OS == Q_dir, real and >= 0 on 200 samples: PASS={g3}")
print(f"X3a: dropping the conjugation changes the form for some sample: control fires = {x3a_fires}")

P_cyc = [[Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)], [Fr(1), Fr(0), Fr(0)]]
paths_cyc = path_measure(P_cyc, pi_u)
F_cyc = {0: {}, 1: {(1,): (Fr(1), Fr(0))}, 2: {}, 3: {}}
q_cyc_os = Q_OS(F_cyc, paths_cyc, {})
q_cyc_dir = Q_dir(F_cyc, paths_cyc)
x3b_fires = (q_cyc_os == q_cyc_dir) and q_cyc_os[1] == 0 and q_cyc_os[0] < 0
results['X3b_fires'] = x3b_fires
print(f"X3b: cyclic chain form = {q_cyc_os[0]} + {q_cyc_os[1]} i (direct {q_cyc_dir[0]}); negative: control fires = {x3b_fires}")

overall = all(results.values())
print("RESULTS:", results)
print("OVERALL:", "PASS" if overall else "FAIL")
sys.exit(0 if overall else 1)
