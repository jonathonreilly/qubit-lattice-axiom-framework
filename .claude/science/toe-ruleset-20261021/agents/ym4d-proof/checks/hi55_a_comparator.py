"""hi55_a -- comparator-side exact identities for HINT55 (criteria: hi55_a_criteria.md, written first).

Plain Python, fractions.Fraction only. No floats in any verdict.
"""
from fractions import Fraction as Fr
from itertools import product
from math import factorial
import random

D = 4
rng = random.Random(5501)


def rand_p():
    while True:
        p = [Fr(rng.randint(-9, 9), rng.randint(1, 7)) for _ in range(D)]
        if any(x != 0 for x in p):
            return p


def delta(i, j):
    return 1 if i == j else 0


def TI(p, mu, nu, rho, sig, flip=False):
    s3 = 1 if flip else -1
    return (p[mu] * p[rho] * delta(nu, sig) - p[mu] * p[sig] * delta(nu, rho)
            + s3 * p[nu] * p[rho] * delta(mu, sig) + p[nu] * p[sig] * delta(mu, rho))


def v(p, lam, mu, nu):
    return p[mu] * delta(nu, lam) - p[nu] * delta(mu, lam)


def gram(p, mu, nu, rho, sig):
    return sum(v(p, l, mu, nu) * v(p, l, rho, sig) for l in range(D))


results = {}

# ---------------- A1 and A1-F ----------------
moms = [rand_p() for _ in range(25)]
a1_ok = True
a1f_fails = 0
for p in moms:
    p2 = sum(x * x for x in p)
    for mu, nu, rho, sig in product(range(D), repeat=4):
        if TI(p, mu, nu, rho, sig) != gram(p, mu, nu, rho, sig):
            a1_ok = False
    tr = sum(TI(p, mu, nu, mu, nu) for mu in range(D) for nu in range(D))
    if tr != 6 * p2:
        a1_ok = False
    bad = any(TI(p, mu, nu, rho, sig, flip=True) != gram(p, mu, nu, rho, sig)
              for mu, nu, rho, sig in product(range(D), repeat=4))
    if bad:
        a1f_fails += 1
results['A1'] = a1_ok
results['A1-F'] = (a1f_fails >= 1, a1f_fails)

# ---------------- A2 and A2-F ----------------
xis = [Fr(0), Fr(1, 3), Fr(1), Fr(7, 2), Fr(10)]
a2_ok = True
ctrl_vals = set()
for p in moms:
    p2 = sum(x * x for x in p)
    for xi in xis:
        Dm = [[(delta(m, n) - (1 - xi) * p[m] * p[n] / p2) / p2 for n in range(D)] for m in range(D)]
        S = Fr(0)
        for mu in range(D):
            for nu in range(D):
                S += (p[mu] * p[mu] * Dm[nu][nu] - p[mu] * p[nu] * Dm[nu][mu]
                      - p[nu] * p[mu] * Dm[mu][nu] + p[nu] * p[nu] * Dm[mu][mu])
        if S != 6:
            a2_ok = False
        ctrl_vals.add(p2 * sum(Dm[m][m] for m in range(D)))
results['A2'] = a2_ok
results['A2-F'] = (len(ctrl_vals) >= 2, sorted(ctrl_vals))

# ---------------- A3 ----------------
def L(k, t):
    return Fr(factorial(k)) / (2 * t) ** (k + 1)


def F_eps(eps, t):
    return t * t * (L(1, t) - eps * L(2, t) + eps * eps * L(3, t))


eps_list = [Fr(1), Fr(1, 3), Fr(5)]
us = [Fr(rng.randint(1, 40), rng.randint(1, 9)) for _ in range(25)]
ts = [Fr(rng.randint(1, 40), rng.randint(1, 9)) for _ in range(25)]
a3a = all((1 / u - e + e * e * u) - e == (1 - e * u) ** 2 / u for e in eps_list for u in us)
a3b = all(F_eps(e, t) == Fr(1, 4) - e / (4 * t) + 3 * e * e / (8 * t * t) for e in eps_list for t in ts)
pairs = [(Fr(4), Fr(8)), (Fr(6), Fr(12)), (Fr(10), Fr(1000)), (Fr(7, 2), Fr(7)), (Fr(3), Fr(300))]
a3c_vals = [F_eps(Fr(1), t2) - F_eps(Fr(1), t1) for t1, t2 in pairs]
a3c = all(x > 0 for x in a3c_vals)
a3d_val = F_eps(Fr(1), Fr(1)) - F_eps(Fr(1), Fr(1, 2))
a3d = a3d_val < 0
a3e = all(F_eps(Fr(1), Fr(1, k)) >= Fr(k * k, 4) for k in range(2, 51))
a3f_vals = [F_eps(Fr(0), t2) - F_eps(Fr(0), t1) for t1, t2 in pairs]
a3f = all(x == 0 for x in a3f_vals)
results['A3a'] = a3a
results['A3b'] = a3b
results['A3c'] = (a3c, [str(x) for x in a3c_vals])
results['A3d'] = (a3d, str(a3d_val))
results['A3e'] = a3e
results['A3-F'] = (a3f, [str(x) for x in a3f_vals])

# ---------------- A4 ----------------
a4_val = Fr(1, 4) * 6 * Fr(1, 16) * L(1, Fr(1))
results['A4'] = (a4_val == Fr(3, 128), str(a4_val))

for k, val in results.items():
    print(k, val)

verdict = (results['A1'] and results['A1-F'][0] and results['A2'] and results['A2-F'][0]
           and a3a and a3b and a3c and a3d and a3e and a3f and results['A4'][0])
print('VERDICT', 'PASS' if verdict else 'FAIL')
