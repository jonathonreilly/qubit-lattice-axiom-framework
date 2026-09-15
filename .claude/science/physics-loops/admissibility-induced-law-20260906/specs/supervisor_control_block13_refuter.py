"""Refuting pass, block 13 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the torus covariance by explicit inversion of (I - A) on the full six-level system (150 x 150, exact), against the
     runner's level recursion; (R2) the coincidence probabilities from the multinomial-square formula instead of walk counts;
(R3) the simple-random-walk return probabilities by direct enumeration of all 6^m step sequences for m <= 8, against
     C(2n,n)/4^n * P_n; (R4) the variance growth at g = 1 against the harmonic bounds with the multinomial route;
(R5) the second-order expansion of log f(s.a) by a different chart (stereographic) for the Born overlap.
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import sys
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
r13 = importlib.import_module("admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15")

# R1: explicit inversion.  Sites (t, y) for t = 1..T on the W x W torus; L = I - A_full where A_full couples level t to t-1.
W, T = 5, 6
sites, idx, A = r13.torus_matrices(W, F(1, 3))
n = W * W
N = n * T
L = [[F(0)] * N for _ in range(N)]
for i in range(N):
    L[i][i] = F(1)
for t in range(1, T):
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                L[t * n + i][(t - 1) * n + j] = -A[i][j]
# invert L by forward substitution (unit lower triangular): G = L^{-1}
G = [[F(0)] * N for _ in range(N)]
for j in range(N):
    col = [F(0)] * N
    col[j] = F(1)
    for i in range(j + 1, N):
        s = -sum(L[i][k] * col[k] for k in range(j, i) if L[i][k])
        col[i] = s
    for i in range(N):
        G[i][j] = col[i]
# Cov = G G^T (sigma^2 = 1); compare the last level's block with the runner's recursion
Cs = None
C = [[F(0)] * n for _ in range(n)]
AT = r13.transpose(A)
for t in range(1, T + 1):
    C = r13.matmul(r13.matmul(A, C), AT)
    for i in range(n):
        C[i][i] += 1
last = [[sum(G[(T - 1) * n + i][k] * G[(T - 1) * n + j][k] for k in range(N)) for j in range(n)] for i in range(n)]
print("R1 explicit inversion of I - A on 150 sites: last-level covariance equals the level recursion:", all(last[i][j] == C[i][j] for i in range(n) for j in range(n)))
# R2: multinomial-square route
P, _ = r13.coincidence_probabilities(60)
mult = [F(r13.multinomial_square_sum(k), 9 ** k) for k in range(61)]
print("R2 P_n from the multinomial-square formula equals the walk-count route for n <= 60:", P == mult)
# R3: direct enumeration of 6^m sequences
steps = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
ok = True
for m in range(0, 9):
    ret = 0
    for seq in product(range(6), repeat=m):
        pos = [0, 0, 0]
        for s in seq:
            pos[0] += steps[s][0]; pos[1] += steps[s][1]; pos[2] += steps[s][2]
        if pos == [0, 0, 0]:
            ret += 1
    if m % 2 == 0:
        k = m // 2
        ok = ok and F(ret, 6 ** m) == F(comb(m, k), 4 ** k) * P[k]
    else:
        ok = ok and ret == 0
print("R3 direct enumeration of all 6^m step sequences (m <= 8): p_m = C(2n,n)/4^n P_n for even m, 0 for odd:", ok)
# R4: harmonic bounds by the multinomial route
V = [F(0)]
for t in range(1, 61):
    V.append(V[-1] + mult[t - 1])
H = [r13.harmonic(t) for t in range(61)]
print("R4 H_t/36 <= Var_t <= 1 + 2 H_{t-1} for t <= 60 (multinomial route):", all(H[t] / 36 <= V[t] <= 1 + 2 * H[t - 1] for t in range(1, 61)))
# R5: stereographic chart for the Born overlap
u1, u2, v1, v2, e = sp.symbols("u1 u2 v1 v2 epsilon", real=True)
def stereo(a, b):
    d = 1 + a ** 2 + b ** 2
    return sp.Matrix([2 * a / d, 2 * b / d, (1 - a ** 2 - b ** 2) / d])
# near the pole, stereographic coordinates (a, b) ~ (theta/2): use a = e u/2 etc.
dot = (stereo(e * u1 / 2, e * u2 / 2).T * stereo(e * v1 / 2, e * v2 / 2))[0]
ser = sp.series(sp.log((1 + dot) / 2), e, 0, 3).removeO()
print("R5 stereographic chart, Born overlap: log f = -(1/4) e^2 |u - v|^2 + O(3):", sp.simplify(sp.expand(ser + sp.Rational(1, 4) * e ** 2 * ((u1 - v1) ** 2 + (u2 - v2) ** 2))) == 0)
