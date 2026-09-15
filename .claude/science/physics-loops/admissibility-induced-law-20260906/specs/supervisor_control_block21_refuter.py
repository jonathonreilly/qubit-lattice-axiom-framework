"""Refuting pass, block 21 (supervisor seat, disjoint machinery from the runner's checks):
(R1) W1 by direct quadrature on the sphere: TV(P_h, P_{h+Delta}) against beta |Delta|/(2 sqrt 3) at random fields (|h| <= 6) and changes
     (|Delta| <= 2), beta in {1/10, 28/100, 1, 3}; the worst ratio;
(R2) the eigenvalue bounds L'(x) <= 1/3 and L(x)/x <= 1/3 on a grid x in (0, 60], and the value 1/3 at x -> 0;
(R3) the exactly solvable open chain: three sites with two bonds, <s_0 . s_2> = L(beta)^2 by a one-dimensional quadrature (the middle
     site integrates to Z(|s_0 + s_2|)); the decay bound's direction on the line: L(beta) <= 2 beta/sqrt(3) (the line's alpha) for beta < sqrt(3)/4;
(R4) the fixed point on the 3x3x3 box by floating-point linear algebra (D = (I - C)^{-1} >= 0, u* = D b), with the centre's value against
     alpha^2/(2(1 - alpha)) (its neighbours are boundary sites; max b = 3c);
(R5) the torus sum sum_x alpha^{d_T(0,x)} on (Z/2LZ)^3 for L = 1..10 against ((1+alpha)/(1-alpha))^3."""
import math
import random
from itertools import product

import numpy as np

random.seed(2121)
np.random.seed(2121)
nodes, weights = np.polynomial.legendre.leggauss(100)
phis = np.linspace(0, 2 * math.pi, 200, endpoint=False)
ct = np.repeat(nodes, len(phis)); st = np.sqrt(1 - ct ** 2); ph = np.tile(phis, len(nodes))
S = np.stack([st * np.cos(ph), st * np.sin(ph), ct], axis=1)
W = np.repeat(weights, len(phis)) * (2 * math.pi / len(phis))


def dens(beta, h):
    e = np.exp(beta * (S @ h) - beta * np.linalg.norm(h)); w = e * W; return w / w.sum()


worst = 0.0; ok1 = True
for beta in (0.1, 0.28, 1.0, 3.0):
    for _ in range(150):
        h = np.random.normal(size=3); h *= random.uniform(0, 6) / np.linalg.norm(h)
        D = np.random.normal(size=3); D *= random.uniform(0, 2) / np.linalg.norm(D)
        tv = 0.5 * np.abs(dens(beta, h) - dens(beta, h + D)).sum()
        bound = beta * np.linalg.norm(D) / (2 * math.sqrt(3))
        ok1 = ok1 and tv <= bound + 1e-9
        worst = max(worst, tv / bound if bound > 0 else 0)
print(f"R1 W1 by quadrature at 600 random (beta, h, Delta): TV <= beta|Delta|/(2 sqrt 3) always: {ok1}; worst ratio {worst:.4f}")
L = lambda x: 1 / math.tanh(x) - 1 / x
xs = np.linspace(1e-3, 60, 60000)
lp = [1 / x ** 2 - 1 / math.sinh(x) ** 2 if x < 30 else 1 / x ** 2 for x in xs]
lx = [L(x) / x for x in xs]
print(f"R2 sup L'(x) = {max(lp):.6f}, sup L(x)/x = {max(lx):.6f} on (0, 60] (both <= 1/3; the value 1/3 is the limit at 0): {max(lp) <= 1/3 + 1e-9 and max(lx) <= 1/3 + 1e-9}")
def Z(beta, r):
    return 4 * math.pi * (math.sinh(beta * r) / (beta * r) if r > 1e-12 else 1.0)
ok3 = True
for beta in (0.1, 0.28, 1.0, 2.0):
    ts = nodes; ws = weights
    num = sum(w * t * Z(beta, math.sqrt(max(2 + 2 * t, 0))) for t, w in zip(ts, ws))
    den = sum(w * Z(beta, math.sqrt(max(2 + 2 * t, 0))) for t, w in zip(ts, ws))
    corr = num / den
    ok3 = ok3 and abs(corr - L(beta) ** 2) < 1e-9
    if beta in (0.28, 1.0):
        print(f"R3 open chain beta={beta}: <s_0.s_2> = {corr:.9f} vs L(beta)^2 = {L(beta)**2:.9f}")
line_ok = all(L(b) <= 2 * b / math.sqrt(3) for b in np.linspace(1e-3, math.sqrt(3) / 4, 2000))
print(f"R3 <s_0.s_2> = L(beta)^2 at four couplings: {ok3}; on the line L(beta) <= 2 beta/sqrt 3 (the decay bound's direction) for beta < sqrt(3)/4: {line_ok}")
alpha = 0.9; c = alpha / 6
sites = list(product(range(3), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
C = np.zeros((27, 27)); b = np.zeros(27)
for s in sites:
    for d in range(3):
        for e in (1, -1):
            y = list(s); y[d] += e; y = tuple(y)
            if y in idx:
                C[idx[s], idx[y]] = c
            else:
                b[idx[s]] += c
Dm = np.linalg.inv(np.eye(27) - C)
u = Dm @ b
print(f"R4 3x3x3 box at alpha = 9/10: D >= 0: {bool((Dm >= -1e-12).all())}; u*_centre = {u[idx[(1,1,1)]]:.6f} <= alpha^2/(2(1-alpha)) = {alpha**2/(2*(1-alpha)):.6f}: {u[idx[(1,1,1)]] <= alpha**2/(2*(1-alpha))}; max b = {b.max():.4f} = 3c")
ok5 = True
for Lt in range(1, 11):
    tor = sum(alpha ** sum(min(n, 2 * Lt - n) for n in nvec) for nvec in product(range(2 * Lt), repeat=3))
    ok5 = ok5 and tor <= ((1 + alpha) / (1 - alpha)) ** 3 + 1e-9
print(f"R5 torus sums for L = 1..10 at alpha = 9/10 are at most ((1+alpha)/(1-alpha))^3 = {((1+alpha)/(1-alpha))**3:.2f}: {ok5}")
