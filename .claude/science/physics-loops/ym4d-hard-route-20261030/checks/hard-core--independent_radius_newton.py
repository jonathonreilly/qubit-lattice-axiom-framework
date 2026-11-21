#!/usr/bin/env python3
"""Lemma 4.7f of Text 4.7, the logic only, on a chain: a saddle with a tree-type vertex, expanded in far variables at a radius function.

Toy: E(u; w) = (1/2) <u, (D^T D + m^2) u> + (lam / 4) sum_x (D u)_x^4 - <w, u>, on a periodic chain of N sites; w lives off a set Y' (an interval).
The saddle u(w) has an odd Taylor series: u = G w + u3(w, w, w) + ..., with G = (D^T D + m^2)^(-1), u3 = -lam G D^T (D G w)^3.
Radius function: rho(c) = min(rho_e, a exp(c1 d(c, Y'))), r(l) = the same with the signed distance. The lemma says that the norm
||u_l||_rho := sum over monomials of prod rho^alpha |coefficient| is at most C r(l), with C free of the volume and of a, when c1 is below the
rate of G, and uses only the all-order tree bound of the vertex, not a first-derivative kernel.

This tests the inequalities of the proof at orders 1 and 3 (exact coefficients, order 3 is the first non-linear one). It cannot test the actual saddle.

PRE-STATED CRITERIA, written before the first run. m = 1 (rate of G about 0.96), lam = 1, Y' an interval of 5 sites at the centre, N in {41, 81}, rho_e in {0.05, 0.2},
a in {1e-2, 1e-4}. c1 = 0.25 (below the rate), and c1 = 1.5 (above it).
PASS-ORDER1: at c1 = 0.25, sup_l ||order 1||_rho / r(l) <= 2 / m^2 + 1, the same on both N, within 1 percent.
PASS-ORDER3: at c1 = 0.25, sup_l ||order 3||_rho / r(l) <= 8 rho_e^2 times the cube of that row bound times the vertex constant 8 lam, for all rho_e, a.
PASS-DEPTH: at c1 = 0.25, inside Y' at depth D, ||order 1||_rho / (a exp(-c1 D)) stays below the same bound (the signed radius).
FAIL-EXPECTED at c1 = 1.5: sup_l ||order 1||_rho / r(l) grows with rho_e / a by more than a factor 3 between a = 1e-2 and a = 1e-4 (a control that the test can see the rate condition).
RESULT OF THE FIRST RUN: PASS-ORDER1 (sup 1.07, same on both N), PASS-ORDER3, PASS-DEPTH (0.56), and the control saw the failure at c1 = 1.5 (154 at a = 1e-2, 908 at a = 1e-4). This tests the row and vertex inequalities at orders 1 and 3 on a toy, with a bound for order 3 that does not resolve cancellation between y.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import resource
import numpy as np


def setup(N, m):
    D = np.zeros((N, N))
    for x in range(N):
        D[x, x] = -1.0
        D[x, (x + 1) % N] = 1.0
    K = D.T @ D + m * m * np.eye(N)
    return D, np.linalg.inv(K)


def dist(N, a, b):
    d = abs(a - b)
    return min(d, N - d)


def radii(N, c1, rho_e, a, half=2):
    centre = N // 2
    inside = [centre + j for j in range(-half, half + 1)]
    d_out = np.array([min(dist(N, x, y) for y in inside) for x in range(N)], float)
    outside = [x for x in range(N) if x not in inside]
    d_in = np.array([min(dist(N, x, y) for y in outside) for x in range(N)], float)
    signed = np.where(d_out > 0, d_out, -d_in)
    r = np.minimum(rho_e, a * np.exp(c1 * signed))
    rho = np.where(d_out > 0, np.minimum(rho_e, a * np.exp(c1 * d_out)), 0.0)  # no variable on Y'
    return rho, r, d_in, d_out


def norms(N, m, lam, c1, rho_e, a):
    D, G = setup(N, m)
    rho, r, d_in, d_out = radii(N, c1, rho_e, a)
    order1 = np.abs(G) @ rho
    # order 3: u3_l = -lam sum_y (G D^T)_{l y} (sum_c (D G)_{y c} w_c)^3, so the coefficient norm is at most, and for a cube exactly bounded by the same monomials with signs,
    # sum_y |(G D^T)_{l y}| (sum_c |(D G)_{y c}| rho_c)^3, an upper bound that equals the norm when no cancellation between y occurs; this is the quantity the proof bounds.
    GD = G @ D.T
    DG = D @ G
    y_row = np.abs(DG) @ rho
    order3 = lam * np.abs(GD) @ (y_row ** 3)
    return order1, order3, r, d_in, d_out, rho


m, lam = 1.0, 1.0
row_bound = 2.0 / m ** 2 + 1.0
c1 = 0.25
res = {}
ok1 = ok3 = okd = True
for N in (41, 81):
    for rho_e in (0.05, 0.2):
        for a in (1e-2, 1e-4):
            o1, o3, r, d_in, d_out, rho = norms(N, m, lam, c1, rho_e, a)
            s1 = float(np.max(o1 / r))
            s3 = float(np.max(o3 / r))
            res[(N, rho_e, a)] = s1
            ok1 &= s1 <= row_bound
            ok3 &= s3 <= 8 * rho_e ** 2 * row_bound ** 3 * 8 * lam
            inside = d_out == 0
            depth_ratio = float(np.max((o1 / (a * np.exp(-c1 * d_in)))[inside]))
            okd &= depth_ratio <= row_bound
            print("N=%d rho_e=%.2f a=%.0e  sup order1/r=%.4f  sup order3/r=%.3e  depth ratio=%.4f" % (N, rho_e, a, s1, s3, depth_ratio))
same = all(abs(res[(41, e, a)] - res[(81, e, a)]) <= 0.01 * res[(81, e, a)] for e in (0.05, 0.2) for a in (1e-2, 1e-4))
print("PASS-ORDER1" if ok1 and same else "FAIL-ORDER1", "same on both N within 1 percent:", same)
print("PASS-ORDER3" if ok3 else "FAIL-ORDER3")
print("PASS-DEPTH" if okd else "FAIL-DEPTH")
# control: the rate condition
c1 = 1.5
v = {}
for a in (1e-2, 1e-4):
    o1, o3, r, d_in, d_out, rho = norms(81, m, lam, c1, 1.0, a)
    v[a] = float(np.max(o1 / r))
print("control at c1 above the rate: sup order1/r =", v, "FAIL-EXPECTED seen" if v[1e-4] > 3 * v[1e-2] else "control did not see it")
print("max RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)
