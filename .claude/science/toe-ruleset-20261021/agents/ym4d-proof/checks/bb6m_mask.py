"""bb6m: exact-arithmetic regularity of ternary Deslauriers-Dubuc masks (lane B session 6, RS5-10).

Criteria: checks/bb6m_criteria.md (written before this script).
Exact integers / Fractions throughout; floats only for the final logarithms.
"""
import math
import time
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
NMAX = 10


def lagrange_weights(nodes, x):
    w = []
    for i, xi in enumerate(nodes):
        num = Fr(1)
        for j, xj in enumerate(nodes):
            if j != i:
                num *= (x - xj) / Fr(xi - xj)
        w.append(num)
    return w


def mask(p):
    """Ternary interpolatory mask through p coarse nodes (p even), as {exponent: Fraction}.
    Fine value f_n = sum_j a_{n-3j} c_j; roots at 3i (a_0 = 1)."""
    h = p // 2
    nodes = list(range(-h + 1, h + 1))           # coarse nodes i+t around the interval [i, i+1]
    w1 = lagrange_weights(nodes, Fr(1, 3))       # point i + 1/3, fine index 3i+1
    a = {0: Fr(1)}
    for t, wt in zip(nodes, w1):
        a[1 - 3 * t] = wt                        # c_{i+t} enters f_{3i+1} with a_{1-3t}
        a[-(1 - 3 * t)] = wt                     # symmetric point i - 1/3
    return a, nodes, w1


def to_list(d):
    lo, hi = min(d), max(d)
    return lo, [d.get(e, Fr(0)) for e in range(lo, hi + 1)]


def divide_sigma(coeffs):
    """Divide polynomial (ascending coefficients) by sigma = 1 + z + z^2; return (quotient, remainder)."""
    c = list(coeffs)
    n = len(c)
    q = [Fr(0)] * (n - 2)
    for k in range(n - 1, 1, -1):           # leading term elimination, sigma leading coeff 1
        lead = c[k]
        q[k - 2] = lead
        c[k] -= lead
        c[k - 1] -= lead
        c[k - 2] -= lead
    return q, c[:2]


def run(p):
    a, nodes, w1 = mask(p)
    lo, coeffs = to_list(a)
    res_sums = [sum(a.get(e, Fr(0)) for e in a if (e - r) % 3 == 0) for r in range(3)]
    m1_sum = all(s == 1 for s in res_sums)
    e = [9 * c for c in coeffs]
    rem_ok = True
    for _ in range(3):
        e, rem = divide_sigma(e)
        rem_ok = rem_ok and all(r == 0 for r in rem)
    # integer form E / D
    D = 1
    for c in e:
        D = D * c.denominator // math.gcd(D, c.denominator)
    E = [int(c * D) for c in e]
    out = {"p": p, "M1_sums": m1_sum, "M1_div": rem_ok, "w1": w1, "nodes": nodes, "len_e": len(E), "D": D}
    P = np.array(E, dtype=object)
    rows = []
    for n in range(1, NMAX + 1):
        if n > 1:
            step = 3 ** (n - 1)
            new = np.zeros(len(P) + step * (len(E) - 1), dtype=object)
            new[:] = 0
            for j, cj in enumerate(E):
                if cj != 0:
                    new[j * step: j * step + len(P)] += cj * P
            P = new
        modn = 3 ** n
        pad = (-len(P)) % modn
        A = np.concatenate([np.abs(P), np.zeros(pad, dtype=object)]) if pad else np.abs(P)
        A = A.reshape(-1, modn)
        colsum = A.sum(axis=0)
        mx = max(colsum)
        denom = D ** n
        # rho_n = (mx / denom)^(1/n); exact comparison with 1, float log only at the end
        rho_ge_1 = mx >= denom
        logratio = (math.log(mx) - math.log(denom)) / n   # natural log of rho_n
        beta = -logratio / math.log(3)
        rows.append((n, rho_ge_1, math.exp(logratio), beta))
    out["rows"] = rows
    return out


results = {p: run(p) for p in (4, 6, 8)}
lines = []
lines.append("bb6m: ternary DD masks, exact arithmetic (e = 9a/sigma^3, rho_n = ||S_e^n||^(1/n), beta_n = -log_3 rho_n)")
for p, r in results.items():
    lines.append(f"DD{p}: M1 residue sums = 1: {r['M1_sums']}; divisible by sigma^3: {r['M1_div']}; len(e) = {r['len_e']}; "
                 f"denominator D = {r['D']}")
    lines.append(f"  offset-1/3 weights on nodes {r['nodes']}: " + ", ".join(str(w) for w in r['w1']))
    for n, ge1, rho, beta in r["rows"]:
        lines.append(f"  n = {n:2d}: rho_n = {rho:.6f}  (rho_n >= 1: {ge1})  beta_n = {beta:.4f}")
r4, r6, r8 = results[4], results[6], results[8]
M1 = all(results[p]["M1_sums"] and results[p]["M1_div"] for p in results)
M2 = r8["rows"][-1][3] >= 0.47 and not r8["rows"][-1][1]
M3 = r6["rows"][-1][3] >= 0.25 and not r6["rows"][-1][1]
M4 = all(row[1] for row in r4["rows"])
M5 = [str(w) for w in r4["w1"]] == ["-5/81", "20/27", "10/27", "-4/81"]
lines.append(f"M1 {'PASS' if M1 else 'FAIL'}; M2 (DD8 beta_{NMAX} >= 0.47) {'PASS' if M2 else 'FAIL'}; "
             f"M3 (DD6 beta_{NMAX} >= 0.25) {'PASS' if M3 else 'FAIL'}; M4 (DD4 rho_n >= 1 all n) {'PASS' if M4 else 'FAIL'}")
lines.append(f"M5 (informational) DD4 weights = (-5, 60, 30, -4)/81: {M5}")
lines.append(f"VERDICT: {'ALL PASS' if (M1 and M2 and M3 and M4) else 'NOT ALL PASS'}")
lines.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(lines))
