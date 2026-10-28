#!/usr/bin/env python3
"""check nl1 - Lemma NL-11 (degree-2 analytic division), exact integer polynomial algebra, d=4.
Criteria: checks/nl1_criteria.md (written first). No BLAS, single process, no numeric lock."""
import random, itertools, sys

D = 4
# polynomial = dict {exponent tuple (e1..e4) : int coeff}, representing sum c * prod z_a^{e_a}
def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0: del r[k]
    return r
def pscale(p, c):
    return {} if c == 0 else {k: c*v for k, v in p.items()}
def pmul_z(p, a):          # multiply by z_a
    r = {}
    for k, v in p.items():
        kk = list(k); kk[a] += 1
        r[tuple(kk)] = r.get(tuple(kk), 0) + v
    return r
def pmul_nu(p, a):         # multiply by nu_a = z_a - 1
    return padd(pmul_z(p, a), pscale(p, -1))
def E(p, a):               # set z_a = 1
    r = {}
    for k, v in p.items():
        kk = list(k); kk[a] = 0
        r[tuple(kk)] = r.get(tuple(kk), 0) + v
        if r[tuple(kk)] == 0: del r[tuple(kk)]
    return r
def T(p, a):
    """divide by (z_a - 1); returns (quotient, remainder). Exact iff remainder == {}."""
    # group by the other exponents, do synthetic division in z_a
    groups = {}
    for k, v in p.items():
        rest = tuple(x if i != a else 0 for i, x in enumerate(k))
        groups.setdefault(rest, {})[k[a]] = groups.setdefault(rest, {}).get(k[a], 0) + v
    quot, rem = {}, {}
    for rest, coefs in groups.items():
        if not coefs: continue
        n = max(coefs)
        # p(z) = sum coefs[j] z^j ; divide by (z-1): q_{n-1}=c_n, q_{j-1}=c_j+q_j, rem=c_0+q_0
        q = {}
        carry = 0
        for j in range(n, 0, -1):
            carry = coefs.get(j, 0) + carry
            q[j-1] = carry
        r0 = coefs.get(0, 0) + carry
        for j, c in q.items():
            if c:
                kk = list(rest); kk[a] = j
                quot[tuple(kk)] = quot.get(tuple(kk), 0) + c
        if r0:
            rem[rest] = rem.get(rest, 0) + r0
    return quot, rem

def dd(a_forms):           # (nu ^ a)_{ab} = nu_a a_b - nu_b a_a
    F = {}
    for i in range(D):
        for j in range(D):
            if i == j: continue
            F[(i, j)] = padd(pmul_nu(a_forms[j], i), pscale(pmul_nu(a_forms[i], j), -1))
    return F

def construct(F, rem_log):
    """Lemma NL-11: b_beta = T_1 F_{1beta} (beta>=2), b_1 = T_2(-E_1 F_{12}).  (0-indexed: 1->0, 2->1)"""
    b = [{} for _ in range(D)]
    for beta in range(1, D):
        q, r = T(F[(0, beta)], 0)
        rem_log.append(r)
        b[beta] = q
    V2 = pscale(E(F[(0, 1)], 0), -1)          # V_2 = -E_1 F_{12}
    q, r = T(V2, 1)
    rem_log.append(r)
    b[0] = q
    return b

def residual(F, b):
    out = {}
    for i in range(D):
        for j in range(i+1, D):
            lhs = padd(pmul_nu(b[j], i), pscale(pmul_nu(b[i], j), -1))
            out[(i, j)] = padd(lhs, pscale(F[(i, j)], -1))
    return out

def rnd_form(rng):
    a = []
    for _ in range(D):
        p = {}
        for _ in range(3):
            k = tuple(rng.randint(0, 2) for _ in range(D))
            c = rng.randint(-4, 4)
            if c: p[k] = p.get(k, 0) + c
        a.append({k: v for k, v in p.items() if v})
    return a

rng = random.Random(20261028)
# ---- nl1-A / nl1-B / nl1-D : closed inputs
bad_A, diff_B, bad_D = 0, 0, 0
for t in range(200):
    a = rnd_form(rng)
    F = dd(a)
    rem_log = []
    b = construct(F, rem_log)
    if any(r for r in rem_log): bad_D += 1
    res = residual(F, b)
    if any(v for v in res.values()): bad_A += 1
    if any(b[i] != a[i] for i in range(D)): diff_B += 1
print("nl1-A: cases with nonzero residual on CLOSED input :", bad_A, "/ 200  -> ", "PASS" if bad_A == 0 else "FAIL")
print("nl1-B: cases where b != a (different representative):", diff_B, "/ 200  -> ", "PASS" if diff_B >= 1 else "FAIL")
print("nl1-D: cases with inexact T_alpha division          :", bad_D, "/ 200  -> ", "PASS" if bad_D == 0 else "FAIL")

# ---- nl1-C : designed-FAIL control, non-closed inputs
nonzero_C = 0
for t in range(20):
    F = {}
    for i in range(D):
        for j in range(i+1, D):
            p = {}
            for _ in range(2):
                k = tuple(rng.randint(0, 2) for _ in range(D))
                c = rng.randint(-4, 4)
                if c: p[k] = p.get(k, 0) + c
            F[(i, j)] = {k: v for k, v in p.items() if v}
            F[(j, i)] = pscale(F[(i, j)], -1)
    rem_log = []
    b = construct(F, rem_log)
    res = residual(F, b)
    if any(v for v in res.values()) or any(r for r in rem_log): nonzero_C += 1
print("nl1-C: non-closed inputs detected (nonzero residual or inexact division):", nonzero_C, "/ 20  -> ",
      "PASS" if nonzero_C >= 19 else "FAIL (test would be vacuous)")
