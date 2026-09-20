#!/usr/bin/env python3
"""C:static-response-equals-green-function:a1   worker w-jonathonsmac4f50-j5feb (claude-opus-5)

Linear light-cone formation on Z^3: theta_{t+1} = P theta_t + noise + f delta_0, P the average over a site and
its six neighbours (n = 7).

A1  1 - P = (-Delta)/7 exactly, so (1 - P)^{-1} = 7 (-Delta)^{-1} and its symbol is 7/E(k); exact rational check
A2  the field: the record's mean direction and its mean vector under exp(beta s.S + h s.t), exactly in h
A3  the fluctuation-response relation (1 + P) C/sigma^2 = (1 - P)^{-1}, exactly on the same tori
"""
import time
from fractions import Fraction
from itertools import product
import numpy as np
import sympy as sp

t0 = time.time()
N_PRED = 7
OFF = [(0, 0, 0)] + [tuple(v if j == i else 0 for j in range(3)) for i in range(3) for v in (1, -1)]

# ---------------------------------------------------------------- A1
print("A1 (P theta)(x) = (1/7)[theta(x) + sum_{6 neighbours} theta(y)], so")
print("A1   ((1 - P) theta)(x) = (6 theta(x) - sum_{neighbours} theta(y))/7 = (-Delta theta)(x)/7 exactly,")
print("A1 with -Delta the Z^3 lattice Laplacian whose symbol is E(k) = 2 sum_j (1 - cos k_j). Hence")
print("A1   (1 - P)^{-1} = 7 (-Delta)^{-1}: the lattice Green function times 7, symbol 7/E(k).")
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
phi = (1 + 2 * sum(sp.cos(k) for k in (k1, k2, k3))) / 7
E = 2 * sum(1 - sp.cos(k) for k in (k1, k2, k3))
print("A1 symbol check 1 - phi(k) = E(k)/7:", sp.simplify(1 - phi - E / 7) == 0)

def conv(f, g, L):
    out = {}
    for x, a in f.items():
        if a == 0: continue
        for z, bq in g.items():
            if bq == 0: continue
            y = tuple((x[i] + z[i]) % L for i in range(3))
            out[y] = out.get(y, Fraction(0)) + a * bq
    return out
def kernel_P(L):
    ker = {}
    for o in OFF:
        y = tuple(c % L for c in o)
        ker[y] = ker.get(y, Fraction(0)) + Fraction(1, 7)
    return ker
def solve_circulant(op, L, rhs):
    """solve op * g = rhs on (Z_L)^3 with sum g = 0, exactly over Q"""
    N = L ** 3; pts = list(product(range(L), repeat=3)); idx = {p: i for i, p in enumerate(pts)}
    M = sp.zeros(N, N); b = sp.zeros(N, 1)
    for x in pts:
        r = idx[x]
        for z, v in op.items():
            M[r, idx[tuple((x[i] - z[i]) % L for i in range(3))]] += sp.Rational(v.numerator, v.denominator)
        b[r, 0] = sp.Rational(rhs[x].numerator, rhs[x].denominator) if x in rhs else 0
    M[N - 1, :] = sp.ones(1, N); b[N - 1, 0] = 0
    sol = M.solve(b)
    return {p: Fraction(int(sp.nsimplify(sol[idx[p]]).p), int(sp.nsimplify(sol[idx[p]]).q)) for p in pts}

R0 = {}
for L in (3, 4, 5):
    N = L ** 3
    P = kernel_P(L)
    delta = {(0, 0, 0): Fraction(1)}
    one_minus_P = {(0, 0, 0): Fraction(1)}
    for z, v in P.items(): one_minus_P[z] = one_minus_P.get(z, Fraction(0)) - v
    lap = {(0, 0, 0): Fraction(6)}
    for o in OFF[1:]:
        y = tuple(c % L for c in o); lap[y] = lap.get(y, Fraction(0)) - 1
    same = all(one_minus_P.get(z, Fraction(0)) == lap.get(z, Fraction(0)) / 7 for z in set(one_minus_P) | set(lap))
    rhs = {p: (Fraction(1) - Fraction(1, N) if p == (0, 0, 0) else -Fraction(1, N)) for p in product(range(L), repeat=3)}
    R = solve_circulant(one_minus_P, L, rhs)
    G = solve_circulant(lap, L, rhs)
    ratio_ok = all(R[p] == 7 * G[p] for p in R)
    resid = conv(one_minus_P, R, L)
    eq_ok = all(resid.get(p, Fraction(0)) == rhs[p] for p in rhs)
    print(f"A1 L={L}: 1 - P equals (-Delta)/7 entrywise: {same}; the exact solution of (1-P)R = delta - 1/N "
          f"satisfies its equation: {eq_ok}; R = 7 G entrywise with G the lattice Green function: {ratio_ok}; "
          f"R(0) = {R[(0,0,0)]} = {float(R[(0,0,0)]):.6f}")
    R0[L] = R[(0, 0, 0)]
    # ---------------------------------------------------------------- A3 on the same torus
    P2 = conv(P, P, L)
    one_minus_P2 = {(0, 0, 0): Fraction(1)}
    for z, v in P2.items(): one_minus_P2[z] = one_minus_P2.get(z, Fraction(0)) - v
    C = solve_circulant(one_minus_P2, L, rhs)            # sigma^2 = 1
    onePC = conv({(0, 0, 0): Fraction(1), **{z: v for z, v in P.items()}} if (0, 0, 0) not in P else
                 {z: (v + Fraction(1) if z == (0, 0, 0) else v) for z, v in P.items()}, C, L)
    fr_ok = all(onePC.get(p, Fraction(0)) == R[p] for p in R)
    print(f"A3 L={L}: (1 + P) C / sigma^2 equals (1 - P)^{{-1}} exactly: {fr_ok}  "
          f"(C(0) = {C[(0,0,0)]} sigma^2 = {float(C[(0,0,0)]):.6f} sigma^2)")
print("A3 the identity is (1+P)(1-P^2)^{-1} = (1-P)^{-1}, which needs P self-adjoint - true for this symmetric")
print("A3 neighbourhood. On the backward lattice P is not self-adjoint and the relation fails (the response is")
print("A3 one-sided while the covariance is inversion symmetric).")

# ---------------------------------------------------------------- A2 the field
b, h, kap = sp.symbols("beta h kappa", positive=True)
n = sp.Integer(N_PRED)
print("A2 with the predecessors aligned, S = n u, the weight exp(beta s.S + h s.t) is the von Mises-Fisher law")
print("A2 with concentration vector V = n beta u + h t, so |V| = sqrt(n^2 beta^2 + h^2) and")
print("A2   mean DIRECTION V/|V|: transverse part h/sqrt(n^2 beta^2 + h^2) = h/(n beta) + O(h^3),")
print("A2   mean VECTOR A(|V|) V/|V|: transverse part A(sqrt(n^2 beta^2 + h^2)) h/sqrt(n^2 beta^2 + h^2)")
print("A2                             = A(n beta) h/(n beta) + O(h^3) = sigma^2 h,  sigma^2 = A(n beta)/(n beta).")
print("A2 So the exact first-order coefficient is A(n beta)/(n beta) for the mean record and 1/(n beta) for its")
print("A2 direction: the 'something' is 1, and the two differ by exactly A(n beta).")
def A_l(x): return 1.0 / np.tanh(x) - 1.0 / x
print("A2 the simulator's quoted ratios against A(n beta):")
for nn, beta, quoted, lat in ((7, 6.0, 0.99, "light cone"), (4, 6.0, 0.96, "backward")):
    print(f"A2   {lat}: n={nn} beta={beta} -> A(n beta) = {A_l(nn*beta):.4f}, quoted {quoted} "
          f"(difference {abs(A_l(nn*beta)-quoted):.4f}); 1/(n beta) = {1/(nn*beta):.6f}, "
          f"A(n beta)/(n beta) = {A_l(nn*beta)/(nn*beta):.6f}")
# exact finite-h coefficient, and a quadrature cross-check of the vMF mean
print("A2 finite h (n=7): h | transverse mean direction | transverse mean vector | ratio to h sigma^2")
for beta in (2.0, 6.0):
    s2 = A_l(N_PRED * beta) / (N_PRED * beta)
    for hv in (0.01, 0.05, 0.2, 1.0):
        V = np.sqrt((N_PRED * beta) ** 2 + hv ** 2)
        dirt = hv / V; vect = A_l(V) * hv / V
        print(f"A2   beta={beta} h={hv}: {dirt:.8f} | {vect:.8f} | {vect/(hv*s2):.6f}")
# quadrature check that the vMF mean is A(|V|) V/|V|
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(400)
for V in (14.0, 42.0, 5.0):
    num = np.sum(wg * xg * np.exp(V * xg)); den = np.sum(wg * np.exp(V * xg))
    print(f"A2 quadrature check of the vMF mean at |V|={V}: <cos> = {num/den:.10f} vs A(|V|) = {A_l(V):.10f}")
print(f"SUMMARY: 1 - P = (-Delta)/7 exactly, so the stationary mean is f times 7 (-Delta)^{{-1}} delta_0 with symbol "
      f"7/E(k), verified over the rationals on L = 3, 4, 5 tori (R = 7G entrywise, R(0) = {R0[5]} = "
      f"{float(R0[5]):.6f} at L=5); the field "
      f"enters as h/(n beta) in the mean direction and A(n beta) h/(n beta) = sigma^2 h in the mean record, the two "
      f"differing by exactly A(n beta) = 0.9762 (light cone, beta=6) and 0.9583 (backward, beta=6), against the "
      f"simulator's quoted 0.99 and 0.96; and (1 + P) C/sigma^2 = (1 - P)^{{-1}} holds exactly on every torus "
      f"checked, P being self-adjoint here; {time.time()-t0:.0f}s")
