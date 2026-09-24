#!/usr/bin/env python3
"""Independent referee of the-fall-from-the-ledgers-consistency attempt a2.

Author w-jonathonsmac4f50-j5024 (claude-opus-5-5). Referee w-macbookpro90c72-jd3f6 (grok-4.6).
Own algebra. The author's check.py is not imported.
"""
from fractions import Fraction as F

import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAILS.append(msg)


# i(φ S - S φ) = -C[dφ], one axis, generic values at x-e, x, x+e
pm, p0, pp = sp.symbols("phi_m phi_0 phi_p", real=True)
um, u0, up = sp.symbols("psi_m psi_0 psi_p")
# S(φψ) = ((φψ)(x+e) - (φψ)(x-e))/(2i); φ S ψ = φ(x) (ψ(x+e)-ψ(x-e))/(2i)
S_phi_psi = (pp * up - pm * um) / (2 * sp.I)
phi_S_psi = p0 * (up - um) / (2 * sp.I)
comm = sp.I * (phi_S_psi - S_phi_psi)
# dφ(x) = φ(x+e)-φ(x); (C[v]ψ)(x) = ½[v(x)ψ(x+e) + v(x-e)ψ(x-e)]
v0 = pp - p0
vm = p0 - pm
C = sp.Rational(1, 2) * (v0 * up + vm * um)
require(sp.simplify(comm + C) == 0, "A1 i[φ, S] = -C[dφ] at a generic site")

# plane wave: Re ψ† C[v] ψ = ½ |χ|² cos(k) (v(x)+v(x-e)) = ½ |χ|² cos(k) (φ(x+e)-φ(x-e))
k = sp.symbols("k", real=True)
vx, vm_ = sp.symbols("v_x v_m", real=True)
bracket = vx * sp.exp(sp.I * k) + vm_ * sp.exp(-sp.I * k)
re_part = sp.simplify(sp.re(bracket))
require(sp.simplify(re_part - sp.cos(k) * (vx + vm_)) == 0,
        "A2 real part of v(x)e^{ik}+v(x-e)e^{-ik} is cos(k)(v(x)+v(x-e))")
require(sp.simplify((pp - p0) + (p0 - pm) - (pp - pm)) == 0,
        "A2 v(x)+v(x-e) = φ(x+e)-φ(x-e), so f picks up cos k times the centred difference")

# two rational points make the content-blind coefficients impossible
# E^2 cos k_1 = A E^2 + Σ_{a,i} B_ai cos(k_a) s_i s_a
# k=(θ,0,0): only B_00 survives, and it must be 1 with A=0
# k=(0,θ,0): the same equation then asks one B to equal two different rationals


def row_and_target(s, c):
    e2 = sum(v * v for v in s)
    row = [e2] + [c[a] * s[i] * s[a] for a in range(3) for i in range(3)]
    return row, e2 * c[0]


# (sin, cos) pairs
axis = (F(3, 5), F(4, 5))
pure = (F(1), F(0))
s_a = [axis[0], F(0), F(0)]
c_a = [axis[1], F(1), F(1)]
s_b = [pure[0], F(0), F(0)]
c_b = [pure[1], F(1), F(1)]
ra, ta = row_and_target(s_a, c_a)
rb, tb = row_and_target(s_b, c_b)
# From k with cos=0: target 0 = A * 1, so A=0. From the 3/5 point: (9/25)*(4/5) = B00*(4/5)*(9/25)
require(tb == 0 and rb[0] == 1 and ta == F(36, 125) and ra[1] == F(36, 125),
        "B2 on the first axis, A=0 and B_00=1 are forced")

def second_axis(sin, cos):
    s = [F(0), sin, F(0)]
    c = [F(1), cos, F(1)]
    return row_and_target(s, c)

r1, t1 = second_axis(F(3, 5), F(4, 5))
r2, t2 = second_axis(F(5, 13), F(12, 13))
# surviving coefficient is B for (a,i)=(1,1), column index 1 + 3*1 + 1 = 5
b_from_1 = t1 / r1[5]
b_from_2 = t2 / r2[5]
require(b_from_1 == F(5, 4) and b_from_2 == F(13, 12) and b_from_1 != b_from_2,
        f"B2 on the second axis the same coefficient would have to be {b_from_1} and {b_from_2}")

ser = sp.series(sp.cos(k), k, 0, 4).removeO()
require(sp.expand(ser - (1 - k**2 / 2)) == 0, "C1 cos k = 1 - k^2/2 + O(k^4)")
require(sp.cos(sp.pi) - 1 == -2, "C1 a species reflected along j has cos k - 1 = -2")

# curl ledger: div of ∂F/∂B is 0 for F = Σ w (curl)^2 on a 3-torus, and the gradient is not identically 0
N = 3


def idx(x, y, z):
    return (x % N) * N * N + (y % N) * N + (z % N)


def xyz(n):
    return n // (N * N), (n // N) % N, n % N


def step(n, a, m):
    x, y, z = xyz(n)
    d = [0, 0, 0]
    d[a] = m
    return idx(x + d[0], y + d[1], z + d[2])


# rational rates and a few nonzero strains
w = [F(n + 1, 2) for n in range(N**3)]
B = {(a, j): [F(0) for _ in range(N**3)] for a in range(3) for j in range(3)}
B[(0, 0)][0] = F(2)
B[(1, 2)][4] = F(-3, 2)
B[(2, 1)][7] = F(5, 3)


def curl(a, b, j, n):
    na, nb = step(n, a, 1), step(n, b, 1)
    return (B[(b, j)][na] - B[(b, j)][n]) - (B[(a, j)][nb] - B[(a, j)][n])


# ∂F/∂B_c^j(p) = Σ_{plaquettes} w * 2 curl * ∂curl/∂B
grad = {(a, j): [F(0) for _ in range(N**3)] for a in range(3) for j in range(3)}
for n in range(N**3):
    for a in range(3):
        for b in range(a + 1, 3):
            for j in range(3):
                cu = curl(a, b, j, n)
                # curl = (B_b(n+a) - B_b(n)) - (B_a(n+b) - B_a(n))
                spots = [
                    ((b, j), step(n, a, 1), F(1)),
                    ((b, j), n, F(-1)),
                    ((a, j), step(n, b, 1), F(-1)),
                    ((a, j), n, F(1)),
                ]
                for key, site, coef in spots:
                    grad[key][site] += w[n] * 2 * cu * coef

div_zero = True
nonzero = False
for j in range(3):
    for n in range(N**3):
        div = sum(grad[(a, j)][n] - grad[(a, j)][step(n, a, -1)] for a in range(3))
        if div != 0:
            div_zero = False
        if any(grad[(a, j)][n] != 0 for a in range(3)):
            nonzero = True
require(div_zero and nonzero,
        "B1 on a 3-torus, ∂F/∂B for F=Σ w curl^2 is not zero and its lattice divergence is 0 at every site")

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0])
else:
    print("HIT: confirmed - the walk's first-order force is e times the centred difference of u times cos k, and a curl ledger stays divergence-free")
    print("SUMMARY: confirmed - i[φ,S]=-C[dφ], the plane-wave factor cos k, the content-blind system is inconsistent (5/4 versus 13/12), and div ∂F/∂B=0.")
