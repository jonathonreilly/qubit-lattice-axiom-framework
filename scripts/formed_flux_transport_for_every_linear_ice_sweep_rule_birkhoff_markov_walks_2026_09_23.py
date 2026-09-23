#!/usr/bin/env python3
"""Formed flux transport for every linear ice sweep rule: a Markov walk on
directions, damped unless it is a rigid translation.

In a sweep, a vertex forms its three forward arrows after its three back
arrows, keeping the ice rule in arrow form (forward sum = back sum).  Take
rules symmetric under reversing every arrow.  When the back arrows are not
all equal, one of them is the minority, and the rule places the forward
minority according to a law pi^(j) given the back minority at j.  Then:
  * the mean forward arrows are a linear function M b of the back arrows,
    for every back pattern, exactly when sum_j pi^(j) = 1: M is doubly
    stochastic, with columns pi^(j);
  * every doubly stochastic M arises (Birkhoff: mixtures of the six
    permutation rules), and open PR 8701's straight-continuation family is
    the line M = p I + (1 - p) J / 3;
  * for these rules the mean arrow field obeys, exactly,
    F_t(q) = M E(q) F_(t-1)(q) layer by layer, E(q) = diag(e^(-i q_j)):
    a Markov walk on directions;
  * off the permutations, M E(q) has spectral radius below 1 at every
    wavevector with nonzero transverse part (checked exactly on the
    quarter-period grid); the permutations translate flux rigidly along
    axes or helices, with no damping and no spreading.
So no linear sweep rule carries undamped isotropic transport.  For every
rule, linear or not, a single reversed arrow in the saturated ice state
(every arrow forward) walks exactly by the column-stochastic kernel
pi^(j), with the same dichotomy.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * arrows sigma in {+1, -1} on the links of Z^3 with sigma = +1 along +e_i;
    the ice rule in arrow form at every vertex (open PRs 8687, 8701);
  * sweep rules: a law for the three forward arrows given the three back
    arrows, symmetric under reversing all six;
  * exact arithmetic: Fractions and Gaussian rationals; a spectral radius
    below 1 is certified by an infinity-norm bound on a power, with
    |a + b i| <= |a| + |b|.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def rule_laws(pis):
    """Exact law of the forward arrows for each back pattern: dict b -> {f: probability}."""
    out = {}
    for b in product((1, -1), repeat=3):
        B = sum(b)
        if abs(B) == 3:
            out[b] = {b: Fr(1)}
            continue
        maj = 1 if B == 1 else -1
        j = next(i for i in range(3) if b[i] == -maj)
        law = {}
        for i in range(3):
            if pis[j][i]:
                f = tuple(-maj if k == i else maj for k in range(3))
                law[f] = law.get(f, 0) + pis[j][i]
        out[b] = law
    return out


def mean(law):
    return tuple(sum(p * f[i] for f, p in law.items()) for i in range(3))


def matrix(pis):
    return [[pis[j][i] for j in range(3)] for i in range(3)]


def linear(pis):
    laws, M = rule_laws(pis), matrix(pis)
    return all(mean(laws[b]) == tuple(sum(M[i][j] * b[j] for j in range(3)) for i in range(3)) for b in laws)


def doubly(M):
    return all(sum(M[i][j] for i in range(3)) == 1 for j in range(3)) and all(sum(M[i]) == 1 for i in range(3))


print("A. which rules have a linear mean response")
det_linear, det_perm = [], []
for choice in product(range(3), repeat=3):
    pis = [[Fr(int(i == choice[j])) for i in range(3)] for j in range(3)]
    laws = rule_laws(pis)
    ice = all(sum(f) == sum(b) for b, law in laws.items() for f in law)
    det_linear.append((choice, linear(pis) and ice))
    det_perm.append(sorted(choice) == [0, 1, 2])
check("of the 27 deterministic rules, exactly the 6 permutation rules have a linear mean response",
      all(ok == perm for (c, ok), perm in zip(det_linear, det_perm)) and sum(det_perm) == 6,
      "every rule keeps the ice rule; linearity holds for all 8 back patterns exactly when sum_j pi^(j) = 1")

rng = random.Random(7)
perms = [list(p) for p in permutations(range(3))]
mix_ok, nonlin = True, 0
for _ in range(40):
    w = [Fr(rng.randint(0, 9)) for _ in range(6)]
    w = [x / sum(w) for x in w] if sum(w) else [Fr(1, 6)] * 6
    pis = [[sum(wk for wk, p in zip(w, perms) if p[j] == i) for i in range(3)] for j in range(3)]
    M = matrix(pis)
    mix_ok = mix_ok and linear(pis) and doubly(M)
    raw = [[Fr(rng.randint(1, 9)) for _ in range(3)] for _ in range(3)]
    pis2 = [[x / sum(r) for x in r] for r in raw]
    if not doubly(matrix(pis2)):
        nonlin += 1
        mix_ok = mix_ok and not linear(pis2)
check("mixtures of the permutation rules are linear with a doubly stochastic M; other laws are not linear",
      mix_ok and nonlin > 30,
      f"40 random mixtures linear and doubly stochastic; {nonlin} random laws off the Birkhoff polytope all nonlinear")

print("B. the mean arrow field is a Markov walk on directions")


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


UNIT = {0: (Fr(1), Fr(0)), 1: (Fr(0), Fr(-1)), 2: (Fr(-1), Fr(0)), 3: (Fr(0), Fr(1))}


def transfer(M, q):
    """T(q) = M E(q) with E(q) = diag(e^(-i q_j pi / 2)), q_j in 0..3."""
    return [[cmul((M[i][j], Fr(0)), UNIT[q[j] % 4]) for j in range(3)] for i in range(3)]


def matmul(A, B):
    out = [[(Fr(0), Fr(0))] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = (Fr(0), Fr(0))
            for k in range(3):
                t = cmul(A[i][k], B[k][j])
                s = (s[0] + t[0], s[1] + t[1])
            out[i][j] = s
    return out


def norm_bound(A):
    return max(sum(abs(x[0]) + abs(x[1]) for x in row) for row in A)


def radius_below_one(M, q, N=64):
    T = transfer(M, q)
    P = T
    for _ in range(N - 1):
        P = matmul(P, T)
        if norm_bound(P) < 1:
            return True
    return False


# one vertex of the p = 1/2 rule: the exact mean of the forward arrows is M times the back arrows
M_half = [[Fr(1, 2) * (i == j) + Fr(1, 6) for j in range(3)] for i in range(3)]
pis_half = [[M_half[i][j] for i in range(3)] for j in range(3)]
laws_half = rule_laws(pis_half)
b0 = (1, 1, -1)
two_step = mean({f: p for f, p in laws_half[b0].items()})
check("for a linear rule the mean forward arrows are M times the mean back arrows, so means propagate by M E(q)",
      two_step == tuple(sum(M_half[i][j] * b0[j] for j in range(3)) for i in range(3)) and linear(pis_half),
      "by linearity of expectation, F_t(q) = M E(q) F_(t-1)(q) for the layer transforms of the mean arrow field")

print("C. damped off the permutations, rigid on them")
grid = [q for q in product(range(4), repeat=3) if not (q[0] == q[1] == q[2])]
damped_all = True
for _ in range(6):
    w = [Fr(rng.randint(1, 9)) for _ in range(6)]
    w = [x / sum(w) for x in w]
    M = [[sum(wk for wk, p in zip(w, perms) if p[j] == i) for j in range(3)] for i in range(3)]
    damped_all = damped_all and all(radius_below_one(M, q) for q in grid)
Mp = [[Fr(1, 2) * (i == j) + Fr(1, 6) for j in range(3)] for i in range(3)]
damped_all = damped_all and all(radius_below_one(Mp, q) for q in grid)
rigid = True
for p in perms:
    P = [[Fr(int(p[j] == i)) for j in range(3)] for i in range(3)]
    for q in grid:
        T = transfer(P, q)
        Pw = T
        for _ in range(11):
            Pw = matmul(Pw, T)
        rigid = rigid and norm_bound(Pw) == 1 and all(sum(1 for x in row if x != (0, 0)) == 1 for row in Pw)
        rigid = rigid and not radius_below_one(P, q, N=12)
check("mixtures with all transitions positive are damped at every nonzero transverse grid wavevector; permutations never damp",
      damped_all and rigid,
      f"{len(grid)} quarter-period wavevectors with nonzero transverse part; spectral radius below 1 certified by "
      "a power of norm below 1 for 7 rules including p = 1/2; each permutation's powers stay unimodular and monomial, "
      "and the certificate correctly fails for them")

print("D. spreading")


def occupation_rate(M, d=0):
    """lim Var(N_d)/n for the direction chain P(j -> i) = M[i][j] (irreducible, doubly stochastic)."""
    mu = [Fr(1, 3)] * 3
    P = [[M[i][j] for i in range(3)] for j in range(3)]
    Z = [[(1 if r == c else 0) - P[r][c] + mu[c] for c in range(3)] for r in range(3)]
    det = (Z[0][0] * (Z[1][1] * Z[2][2] - Z[1][2] * Z[2][1]) - Z[0][1] * (Z[1][0] * Z[2][2] - Z[1][2] * Z[2][0])
           + Z[0][2] * (Z[1][0] * Z[2][1] - Z[1][1] * Z[2][0]))
    inv = [[None] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            rows = [Z[i] for i in range(3) if i != c]
            m = [[row[k] for k in range(3) if k != r] for row in rows]
            inv[r][c] = ((-1) ** (r + c)) * (m[0][0] * m[1][1] - m[0][1] * m[1][0]) / det
    h = [Fr(int(x == d)) - Fr(1, 3) for x in range(3)]
    Zh = [sum(inv[x][y] * h[y] for y in range(3)) for x in range(3)]
    return sum(mu[x] * h[x] * (2 * Zh[x] - h[x]) for x in range(3))


rates = {p: occupation_rate([[p * (i == j) + (1 - p) * Fr(1, 3) for j in range(3)] for i in range(3)]) for p in (Fr(0), Fr(1, 2), Fr(3, 4))}
check("the straight-continuation family reproduces open PR 8701's spreading rate (2/9)(1 + p)/(1 - p)",
      all(r == Fr(2, 9) * (1 + p) / (1 - p) for p, r in rates.items()),
      "occupation variance rates " + ", ".join(f"{r} at p = {p}" for p, r in rates.items()))

print("E. every rule, one defect in the saturated state")
# Saturated state: every arrow +1, so every vertex sees back sum 3 and passes it on.  One reversed arrow
# entering a vertex along j is its back minority; the rule sends it on along i with probability pi^(j)_i.
sat_ok, sat_rules = True, 0
for _ in range(20):
    raw = [[Fr(rng.randint(1, 9)) for _ in range(3)] for _ in range(3)]
    pis = [[x / sum(r) for x in r] for r in raw]
    laws = rule_laws(pis)
    full = laws[(1, 1, 1)] == {(1, 1, 1): Fr(1)}
    for j in range(3):
        b = tuple(-1 if k == j else 1 for k in range(3))
        law = laws[b]
        full = full and all(sum(1 for x in f if x == -1) == 1 for f in law) \
            and all(law.get(tuple(-1 if k == i else 1 for k in range(3)), 0) == pis[j][i] for i in range(3))
    Mc = matrix(pis)
    col = all(sum(Mc[i][j] for i in range(3)) == 1 for j in range(3))
    sat_ok = sat_ok and full and col and not doubly(Mc) and all(radius_below_one(Mc, q) for q in grid)
    sat_rules += 1
check("for every rule, one reversed arrow in the saturated state walks by the column-stochastic kernel pi, damped off the axis",
      sat_ok and sat_rules == 20,
      "20 random rules off the Birkhoff polytope: the reversed arrow leaves each vertex along i with probability "
      "pi^(j)_i and the rest stays saturated; spectral radius below 1 at all 60 transverse grid wavevectors")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
