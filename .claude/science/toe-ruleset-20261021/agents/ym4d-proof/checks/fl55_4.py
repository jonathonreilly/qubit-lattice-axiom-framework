#!/usr/bin/env python3
"""fl55_4 -- uniqueness of the marginal (degree-1) cubic jet under hypercubic covariance, Bose symmetry and the Ward
identity.  Criteria: checks/fl55_4_criteria.md (written first).  Exact Fractions; sympy only for one polynomial identity."""
import itertools
from fractions import Fraction as Fr
import sympy as sp

D = 4
def ia(mu, nu, rho, sg): return 64 * mu + 16 * nu + 4 * rho + sg          # alpha (coefficient of p_sigma)
def ib(mu, nu, rho, sg): return 256 + 64 * mu + 16 * nu + 4 * rho + sg    # beta  (coefficient of q_sigma)
NU = 512

def rank(rows):
    """rows: list of dict {col: Fraction}; exact Gaussian elimination, returns rank."""
    pivots = {}   # col -> row(dict) normalised with pivot 1
    r = 0
    for row in rows:
        row = {k: v for k, v in row.items() if v != 0}
        # reduce by existing pivots
        changed = True
        while row:
            # eliminate pivot columns present in row
            pc = [c for c in row if c in pivots]
            if not pc: break
            for c in pc:
                if c in row:
                    f = row[c]
                    for k, v in pivots[c].items():
                        row[k] = row.get(k, Fr(0)) - f * v
                        if row[k] == 0: del row[k]
        if not row: continue
        c0 = min(row)
        p = row[c0]
        newp = {k: v / p for k, v in row.items()}
        # back-substitute into existing pivots to keep reduced form
        for c, pr in pivots.items():
            if c0 in pr:
                f = pr[c0]
                for k, v in newp.items():
                    pr[k] = pr.get(k, Fr(0)) - f * v
                    if pr[k] == 0: del pr[k]
        pivots[c0] = newp
        r += 1
    return r

# ---------------- B4 generators (signed permutation matrices)
def perm_matrix(perm, signs):
    g = [[0] * D for _ in range(D)]
    for i in range(D): g[perm[i]][i] = signs[i]
    return g
G_swap12 = perm_matrix([1, 0, 2, 3], [1, 1, 1, 1])
G_cycle = perm_matrix([1, 2, 3, 0], [1, 1, 1, 1])
G_refl1 = perm_matrix([0, 1, 2, 3], [-1, 1, 1, 1])
GENS = [G_swap12, G_cycle, G_refl1]

def eqs_H():
    rows = []
    for g in GENS:
        for (mu, nu, rho, tau) in itertools.product(range(D), repeat=4):
            for idx in (ia, ib):
                row = {}
                # LHS: sum_sigma g[sigma][tau] * X[mu,nu,rho,sigma]
                for sg in range(D):
                    if g[sg][tau]: row[idx(mu, nu, rho, sg)] = row.get(idx(mu, nu, rho, sg), Fr(0)) + Fr(g[sg][tau])
                # RHS: sum g[mu][m'] g[nu][n'] g[rho][r'] X[m',n',r',tau]
                for m_, n_, r_ in itertools.product(range(D), repeat=3):
                    w = g[mu][m_] * g[nu][n_] * g[rho][r_]
                    if w: row[idx(m_, n_, r_, tau)] = row.get(idx(m_, n_, r_, tau), Fr(0)) - Fr(w)
                rows.append(row)
    return rows

def eqs_S(sign):
    """sign = -1 for Bose-antisymmetric (f-type), +1 for symmetric (d-type).  Equations X' - sign*X = 0."""
    rows = []
    for (mu, nu, rho, sg) in itertools.product(range(D), repeat=4):
        # swap legs 1,2: T_{nu mu rho}(q,p) = sign * T_{mu nu rho}(p,q)
        #   p_sigma coefficient: beta_{nu mu rho sg} = sign*alpha_{mu nu rho sg}
        rows.append({ib(nu, mu, rho, sg): Fr(1), ia(mu, nu, rho, sg): Fr(-sign)})
        #   q_sigma coefficient: alpha_{nu mu rho sg} = sign*beta_{mu nu rho sg}
        rows.append({ia(nu, mu, rho, sg): Fr(1), ib(mu, nu, rho, sg): Fr(-sign)})
        # swap legs 1,3: T_{rho nu mu}(r,q) = sign*T_{mu nu rho}(p,q),  r = -p-q
        #   p coefficient: -alpha_{rho nu mu sg} = sign*alpha_{mu nu rho sg}
        row = {ia(rho, nu, mu, sg): Fr(-1)}; row[ia(mu, nu, rho, sg)] = row.get(ia(mu, nu, rho, sg), Fr(0)) - Fr(sign)
        rows.append(row)
        #   q coefficient: -alpha_{rho nu mu sg} + beta_{rho nu mu sg} = sign*beta_{mu nu rho sg}
        row = {ia(rho, nu, mu, sg): Fr(-1)}
        row[ib(rho, nu, mu, sg)] = row.get(ib(rho, nu, mu, sg), Fr(0)) + Fr(1)
        row[ib(mu, nu, rho, sg)] = row.get(ib(mu, nu, rho, sg), Fr(0)) - Fr(sign)
        rows.append(row)
    return rows

def eqs_W0():
    rows = []
    for nu, rho in itertools.product(range(D), repeat=2):
        for mu, sg in itertools.product(range(D), repeat=2):
            if mu <= sg:
                row = {ia(mu, nu, rho, sg): Fr(1)}
                row[ia(sg, nu, rho, mu)] = row.get(ia(sg, nu, rho, mu), Fr(0)) + Fr(1)
                rows.append(row)
            rows.append({ib(mu, nu, rho, sg): Fr(1)})
    return rows

H = eqs_H(); Sm = eqs_S(-1); Sp = eqs_S(+1); W0 = eqs_W0()
null = lambda rows: NU - rank([dict(r) for r in rows])
dim_HSm = null(H + Sm); dim_HSp = null(H + Sp)
dim_J1 = null(H + Sm + W0); dim_J2 = null(H + Sp + W0)
print(f"J4 (informational) dim{{(H),(S-)}} = {dim_HSm};  dim{{(H),(S+)}} = {dim_HSp}")
ok1 = dim_J1 == 0; ok2 = dim_J2 == 0
print(f"J1 f-type uniqueness dim{{(H),(S-),(W0)}} = {dim_J1}: {'PASS' if ok1 else 'FAIL'}")
print(f"J2 d-type vanishing dim{{(H),(S+),(W0)}} = {dim_J2}: {'PASS' if ok2 else 'FAIL'}")

# ---------------- the YM vertex
def dl(a, b): return 1 if a == b else 0
X = {}
for mu, nu, rho, sg in itertools.product(range(D), repeat=4):
    X[ia(mu, nu, rho, sg)] = Fr(dl(mu, nu) * dl(rho, sg) + dl(nu, rho) * dl(mu, sg) - 2 * dl(rho, mu) * dl(nu, sg))
    X[ib(mu, nu, rho, sg)] = Fr(-dl(mu, nu) * dl(rho, sg) + 2 * dl(nu, rho) * dl(mu, sg) - dl(rho, mu) * dl(nu, sg))
def residual(rows): return max(abs(sum(v * X[k] for k, v in r.items())) for r in rows)
resH = residual(H); resS = residual(Sm); resW = residual(W0)
# inhomogeneous Ward identity, polynomial check
p = sp.symbols('p0:4'); q = sp.symbols('q0:4')
r = [-p[i] - q[i] for i in range(D)]
def T(mu, nu, rho):
    return sum(sp.Rational(X[ia(mu, nu, rho, s)].numerator, X[ia(mu, nu, rho, s)].denominator) * p[s]
               + sp.Rational(X[ib(mu, nu, rho, s)].numerator, X[ib(mu, nu, rho, s)].denominator) * q[s] for s in range(D))
sq = lambda v: sum(x * x for x in v)
ward_ok = True
for nu, rho in itertools.product(range(D), repeat=2):
    lhs = sum(p[mu] * T(mu, nu, rho) for mu in range(D))
    rhs = (sq(r) * dl(nu, rho) - r[nu] * r[rho]) - (sq(q) * dl(nu, rho) - q[nu] * q[rho])
    if sp.expand(lhs - rhs) != 0: ward_ok = False
ok3 = (resH == 0 and resS == 0 and ward_ok)
print(f"J3 V^YM satisfies (H) [res {resH}], (S-) [res {resS}], inhomogeneous Ward identity [{ward_ok}]: {'PASS' if ok3 else 'FAIL'}")
c1 = dim_HSm >= 1
print(f"J-c1 without (W0) dim{{(H),(S-)}} = {dim_HSm} >= 1: {'control fires' if c1 else 'CONTROL DOES NOT FIRE'}")
c2 = resW != 0
print(f"J-c2 V^YM violates (W0) [max residual {resW}]: {'control fires' if c2 else 'CONTROL DOES NOT FIRE'}")
print("=== fl55_4 SUMMARY ===")
print("OVERALL:", "PASS" if (ok1 and ok2 and ok3 and c1 and c2) else ("INVALID (a control did not fire)" if (ok1 and ok2 and ok3) else "FAIL"))
