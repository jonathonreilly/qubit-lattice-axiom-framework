#!/usr/bin/env python3
"""J:derive:the-fall-from-the-ledgers-consistency:a1 -- which momenta can carry the fall.

Walk (block 54, PR #8570): H = sum_a sigma_a D_a, D_a = (i/2)(T_a - T_a^dag), (T_a psi)(x) = psi(x - e_a),
symbol sin k_a (the task's S_a with T_a the forward shift); clocked H_w = phi H phi, phi = sqrt(w), u = log w. Momenta: pi_j = S_j (block 63), the
two-step P_j = S_j C_j, C_j = (T_j + T_j^dag)/2 (blocks 69, 73), and any finite-reach P with [P, H] = 0.
Claim (ATTEMPT.md): for a plane-wave eigenstate in a uniform gradient phi = 1 + eps g.x, at first order,
d<P>/dt = -E grad(u) . grad_k pbar(k), pbar the band value of P's symbol; pbar is periodic, so the weight
d pbar/dk_j has zero mean on every line of the zone: no local momentum falls with weight one at every k.
Exact: sympy symbols and integer matrices. Families: S symbol identities; O operator identities on a
chain; B band identities for matrix momenta; W the weights of the named momenta.
"""
import sys

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    print(("ok " if cond else "FAIL ") + tag + (" " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


k = sp.symbols("k", real=True)

# ---------------------------------------------------------------- O operator identities on an open chain
N = 9
X = sp.diag(*range(N))


def T(n):          # (T_n psi)(x) = psi(x - n) on the chain, rows x, columns x - n
    return sp.Matrix(N, N, lambda a, b: 1 if a - b == n else 0)


good = all((X * T(n) - T(n) * X) == n * T(n) for n in (-2, -1, 1, 2))
ok("O.XT", good, "[X, T_n] = n T_n exactly (integer matrices on a 9-site chain)")
# symbol of i[X, P] for P = sum_n c_n T_n is sum_n i n c_n e^{-i k n} = -dp/dk with p(k) = sum_n c_n e^{-ikn}


def symbol(coeffs):
    return sum(c * sp.exp(-sp.I * k * n) for n, c in coeffs.items())


S1 = {1: sp.I / 2, -1: -sp.I / 2}                           # block 54's D = (i/2)(T - T^dag), T^dag = T_{-1}: symbol sin k
C1 = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}


def mult(a, b):
    out = {}
    for n1, c1 in a.items():
        for n2, c2 in b.items():
            out[n1 + n2] = out.get(n1 + n2, 0) + c1 * c2
    return {n: sp.nsimplify(c) for n, c in out.items() if c != 0}


P2 = mult(S1, C1)
for name, co, pexpr in [("S", S1, sp.sin(k)), ("SC", P2, sp.sin(k) * sp.cos(k))]:
    ok("S.sym_" + name, sp.simplify(sp.expand(symbol(co).rewrite(sp.cos)) - pexpr) == 0, "symbol of %s is %s" % (name, pexpr))
    comm_sym = sum(sp.I * n * c * sp.exp(-sp.I * k * n) for n, c in co.items())
    ok("S.comm_" + name, sp.simplify(sp.expand((comm_sym + sp.diff(symbol(co), k)).rewrite(sp.cos))) == 0,
       "symbol of i[X, %s] = -d/dk of its symbol" % name)

# ---------------------------------------------------------------- B band identity for a matrix momentum commuting with H
# P(k) = a(k) + c(k) sigma.s(k) commutes with H(k) = sigma.s(k); on the band sigma.s chi = |s| chi, <chi|dP|chi> = d pbar
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
s = sp.Matrix([sp.sin(k1), sp.sin(k2), sp.sin(k3)])
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
Hk = sum((s[i] * sig[i] for i in range(3)), sp.zeros(2))
a_ = sp.cos(k1) + sp.cos(k2) * sp.cos(k3)
c_ = 1 + sp.cos(k1 + k2)
Pk = a_ * sp.eye(2) + c_ * Hk
ok("B.commute", sp.simplify(Pk * Hk - Hk * Pk) == sp.zeros(2), "P(k) = a + c sigma.s commutes with H(k)")
# test the band identity at a rational-sine point: k with sin = (3/5, 4/5, 0), cos = (4/5, 3/5, 1)
pt = {sp.sin(k1): sp.Rational(3, 5), sp.cos(k1): sp.Rational(4, 5), sp.sin(k2): sp.Rational(4, 5),
      sp.cos(k2): sp.Rational(3, 5), sp.sin(k3): 0, sp.cos(k3): 1}
Hn = Hk.subs(pt)
E = sp.sqrt(sum(v**2 for v in s.subs(pt)))        # = 1
ok("B.E", E == 1, "|s| = 1 at the test point")
vecs = (Hn - E * sp.eye(2)).nullspace()
chi = vecs[0] / sp.sqrt((vecs[0].H * vecs[0])[0])
dP = sp.diff(Pk, k1)
dP_expanded = sp.expand(sp.expand_trig(dP))
pbar = a_ + c_ * sp.sqrt(sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + sp.sin(k3) ** 2)
dpbar = sp.diff(pbar, k1)


def at(expr):
    e = sp.expand_trig(sp.expand(expr))
    return sp.nsimplify(sp.simplify(e.subs(pt)))


lhs = sp.simplify((chi.H * dP.applyfunc(at) * chi)[0])
ok("B.band", sp.simplify(lhs - at(dpbar)) == 0, "<chi| dP/dk1 |chi> = d pbar/dk1 = %s at the test point (positive band)" % at(dpbar))

# ---------------------------------------------------------------- W weights of the named momenta
w_pi = sp.diff(sp.sin(k), k)
w_P = sp.simplify(sp.diff(sp.sin(k) * sp.cos(k), k))
p4 = sp.Rational(4, 3) * sp.sin(k) - sp.Rational(1, 6) * sp.sin(2 * k)
w_4 = sp.diff(p4, k)
ok("W.pi", w_pi == sp.cos(k) and sp.integrate(w_pi, (k, -sp.pi, sp.pi)) == 0,
   "pi_j: weight cos k_j (block 66 / a2), zone mean 0; -1 at k = pi (the reflected species rise)")
ok("W.P", sp.simplify(w_P - sp.cos(2 * k)) == 0 and sp.integrate(w_P, (k, -sp.pi, sp.pi)) == 0,
   "two-step P_j = S_j C_j: weight cos 2k_j, zone mean 0; -1 at k_j = pi/2, +1 at 0 and pi")
ok("W.P4", sp.series(w_4, k, 0, 6).removeO() == 1 - k**4 / 6 and sp.integrate(w_4, (k, -sp.pi, sp.pi)) == 0,
   "fourth-order stencil (4/3)S - (1/6)S_2: weight (4/3)cos k - (1/3)cos 2k = 1 - k^4/6 + ..., zone mean 0; value %s at k = pi"
   % sp.simplify(w_4.subs(k, sp.pi)))
ok("W.torus", [w_pi.subs(k, v) for v in (0, sp.pi / 2, sp.pi, 3 * sp.pi / 2)] == [1, 0, -1, 0]
   and [sp.simplify(w_P.subs(k, v)) for v in (0, sp.pi / 2, sp.pi, 3 * sp.pi / 2)] == [1, -1, 1, -1],
   "on the 4^3 torus's wave numbers: pi_j weights 1, 0, -1, 0; P_j weights 1, -1, 1, -1")
import random
random.seed(3)
ptrig = sum(random.randint(-5, 5) * sp.sin(n * k) + random.randint(-5, 5) * sp.cos(n * k) for n in range(1, 7))
ok("W.zero_mean", sp.integrate(sp.diff(ptrig, k), (k, -sp.pi, sp.pi)) == 0
   and sp.integrate(sp.sign(sp.sin(k)) * sp.cos(k), (k, -sp.pi, sp.pi)) == 0,
   "the k-derivative of a random trigonometric polynomial, and of the band-type |sin k|, integrate to zero over a period")

if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: for the clocked walk in a uniform rate gradient, a plane-wave eigenstate of energy E changes any finite-reach "
    "momentum P that commutes with H at first order by -E grad(u).grad_k pbar(k) (pbar the band value of P's symbol), so "
    "the weight of the fall along j is d pbar/dk_j: cos k_j for pi_j, cos 2k_j for the two-step P_j.",
    "HIT: since pbar is periodic, that weight has zero mean on every line of the zone: no local conserved momentum falls "
    "with weight one at every wave vector (it either never falls along j or rises for some k); the exact fall of block 54 "
    "belongs to the non-local quasi-momentum, so any local ledger can owe it only asymptotically in k.",
]
print("SUMMARY: PARTIAL no local momentum of the walk carries block 54's fall with weight one: the weight is d pbar/dk_j "
      "with zero zone mean (cos k_j, cos 2k_j, ...); the fall is owed by a local ledger only asymptotically in k")
print("\n".join(HITS))
