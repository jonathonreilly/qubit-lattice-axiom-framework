#!/usr/bin/env python3
"""J:derive:one-set-of-variables-for-strains-and-coin-rotations:a2 -- exact checks.

Supplied clauses (nothing adopted): block 54's walk H = sum_a s_a S_a; block 63/64's strains on BONDS,
H[B] = H + sum_a s_a (1/2){C_a[B_a^j], S_j}, with relabellings B -> B + d xi; block 65's rotation on SITES,
H[th] = H + (1/2) sum_j {(th x e_j).s, S_j} + (1/2) sum_a C_a[d_a th_a], with coin rotations th -> th + theta.
(T psi)(x) = psi(x + e_a); a bond function v on bond x -> x + e_a is attached to x.
EXACT: sympy symbols on plane waves; Gaussian-rational arithmetic on the exactly stationary state of the 4^3 torus.
"""
import sys
from itertools import product
import numpy as np
import sympy as sy

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------- (b) the symbols of the two deformations on plane waves e^{ik.x} -> e^{i(k+q).x}
I = sy.I
# the pieces, each an exact scalar identity (so no matrix needs simplifying):
#   C_a[v] with v = amp e^{iq.x}:  amp (e^{ik_a} + e^{-iq_a} e^{-ik_a})/2 = amp e^{-iq_a/2} cos(k_a + q_a/2)
#   (1/2){f(x), S_j} and (1/2){C_a[v], S_j}:  (sin k_j + sin(k_j + q_j))/2 = sin(k_j + q_j/2) cos(q_j/2)
#   the twist hop (1/2) C_a[d_a th_a]:
#       th_a (e^{iq_a} - 1)(e^{ik_a} + e^{-iq_a} e^{-ik_a})/4 = i th_a sin(q_a/2) cos(k_a + q_a/2)
x1, x2 = sy.symbols("x1 x2", real=True)
ok = sy.simplify(sy.expand_complex((sy.exp(I * x1) + sy.exp(-I * x2) * sy.exp(-I * x1)) / 2
                                   - sy.exp(-I * x2 / 2) * sy.cos(x1 + x2 / 2))) == 0
ok &= sy.simplify(sy.expand_trig((sy.sin(x1) + sy.sin(x1 + x2)) / 2 - sy.sin(x1 + x2 / 2) * sy.cos(x2 / 2))) == 0
ok &= sy.simplify(sy.expand_complex((sy.exp(I * x2) - 1) * (sy.exp(I * x1) + sy.exp(-I * x2) * sy.exp(-I * x1)) / 4
                                    - I * sy.sin(x2 / 2) * sy.cos(x1 + x2 / 2))) == 0
# hence, with B_a^j = eps_abj th_b on the forward bonds and the same th on the site (block 65's coupling):
#   D = sum s_a eps_abj th_b [e^{-iq_a/2} cos(k_a+q_a/2) - 1] sin(k_j+q_j/2) cos(q_j/2)
#       - i sum_a th_a sin(q_a/2) cos(k_a+q_a/2)
lam = sy.symbols("lam", positive=True)
brk = sy.exp(-I * lam * x2 / 2) * sy.cos(lam * x1 + lam * x2 / 2) - 1             # the bracket, scaled
sfac = sy.sin(lam * x1 + lam * x2 / 2) * sy.cos(lam * x2 / 2)
tw = -I * sy.sin(lam * x2 / 2) * sy.cos(lam * x1 + lam * x2 / 2)
ser_frame = sy.expand(sy.series(brk * sfac, lam, 0, 4).removeO())
ser_twist = sy.expand(sy.series(tw, lam, 0, 3).removeO())
q0_frame = sy.expand(sy.series((sy.cos(lam * x1) - 1) * sy.sin(lam * x1), lam, 0, 4).removeO())
ok &= ser_frame.coeff(lam, 1) == 0 and ser_frame.coeff(lam, 2) != 0                # the sigma part starts at order 2
ok &= sy.simplify(ser_twist.coeff(lam, 1) + I * x2 / 2) == 0                        # the twist: -(i/2) th_a q_a
ok &= q0_frame.coeff(lam, 1) == 0 and q0_frame.coeff(lam, 2) == 0 and q0_frame.coeff(lam, 3) != 0
need(ok, "(b) difference operator")
rec("ok (b) on plane waves (k -> k+q) the forward-bond rotation B_a^j = eps_abj th_b(x) and the coin rotation th(x) "
    "differ by D(k,q) = sum s_a eps_abj th_b [e^(-iq_a/2) cos(k_a + q_a/2) - 1] sin(k_j + q_j/2) cos(q_j/2) - "
    "sum_a i th_a sin(q_a/2) cos(k_a + q_a/2) exactly; for a uniform rotation D = O(k^3) (the cos k_a factor), and "
    "at first order in the rotation's wave vector D = -(i/2) th.q, the twist hop the bonds do not carry")

# ---------------------------------- (c) the exactly stationary state of the 4^3 torus and the two responses
L = 4
sites = list(product(range(L), repeat=3))
ix = {s: i for i, s in enumerate(sites)}
coins = [np.array([1, 1], dtype=complex), np.array([1, 1j]), np.array([1, 0], dtype=complex)]   # +1 of s1, s2, s3
psi = np.zeros((len(sites), 2), dtype=complex)
for a in range(3):
    for s in sites:
        psi[ix[s]] += (1j ** s[a]) * coins[a]                 # e^{i (pi/2) x_a} with coin u_a: H psi_a = psi_a
SG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]),
      np.array([[1, 0], [0, -1]], dtype=complex)]


def nb(s, a, d=1):
    t = list(s)
    t[a] = (t[a] + d) % L
    return ix[tuple(t)]


def S_psi(j):
    out = np.zeros_like(psi)
    for s in sites:
        out[ix[s]] = (psi[nb(s, j)] - psi[nb(s, j, -1)]) / 2j
    return out


def H_psi(v):
    out = np.zeros_like(v)
    for a in range(3):
        for s in sites:
            out[ix[s]] += SG[a] @ ((v[nb(s, a)] - v[nb(s, a, -1)]) / 2j)
    return out


stationary = np.array_equal(H_psi(psi), psi)                  # exactly E = 1
Sj = [S_psi(j) for j in range(3)]
Th = np.array([[[np.real(psi[i].conj() @ SG[a] @ Sj[j][i]) for i in range(len(sites))] for j in range(3)]
               for a in range(3)])                              # Theta_a^j(x)
J = np.array([[[0.5 * np.real(psi[nb(s, a)].conj() @ SG[a] @ Sj[j][ix[s]] + Sj[j][nb(s, a)].conj() @ SG[a] @ psi[ix[s]])
                for s in sites] for j in range(3)] for a in range(3)])       # J_a^j(x -> x + e_a)
b_ = np.array([[np.real(psi[ix[s]].conj() @ psi[nb(s, c)]) for s in sites] for c in range(3)])
coin_resp = np.array([[sum(float(sy.LeviCivita(c, a, d)) * Th[d, a, i] for a in range(3) for d in range(3))
                       - 0.5 * (b_[c, i] - b_[c, nb(sites[i], c, -1)]) for i in range(len(sites))] for c in range(3)])
torque_fwd = np.array([[sum(float(sy.LeviCivita(c, a, j)) * J[a, j, i] for a in range(3) for j in range(3))
                        for i in range(len(sites))] for c in range(3)])
# symmetric placement: the rotation shared by the forward and backward bonds of x
J_bwd = np.array([[[J[a, j, nb(sites[i], a, -1)] for i in range(len(sites))] for j in range(3)] for a in range(3)])
torque_sym = np.array([[sum(float(sy.LeviCivita(c, a, j)) * (J[a, j, i] + J_bwd[a, j, i]) / 2
                            for a in range(3) for j in range(3)) for i in range(len(sites))] for c in range(3)])
exact_vals = all(np.array_equal(v * 8, np.round(v * 8)) for v in (Th, J, b_, coin_resp, torque_fwd, torque_sym))
ok = stationary and exact_vals and np.all(coin_resp == 0)
ok &= np.any(torque_fwd != 0) and np.any(torque_sym != 0)
nz_f = int(np.count_nonzero(np.any(torque_fwd != 0, axis=0)))
nz_s = int(np.count_nonzero(np.any(torque_sym != 0, axis=0)))
need(ok, "(c) responses")
rec("ok (c) on the exactly stationary state of the 4^3 torus (wave numbers pi/2, coins (1,1), (1,i), (1,0); "
    "H psi = psi exactly): the coin-rotation response sum eps Theta - (1/2)[b_c(x) - b_c(x - e_c)] is 0 at all 64 "
    "sites (block 65 T3), while the torque of the forward bonds is non-zero at %d sites and the torque shared by "
    "forward and backward bonds at %d; all values exact multiples of 1/8" % (nz_f, nz_s))

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL the exact symbol of the difference between a rotation of a site's forward bonds and a rotation of its "
      "coin: O(k^3) for uniform rotations, -(i/2) th.q (the twist hop) at first order in the rotation's wave "
      "vector; tying the antisymmetric bond strain to the site rotation (forward or shared bonds) fails: on the "
      "exactly stationary 4^3 state the coin response is zero at every site and the tied torque is not, so a field "
      "energy blind to th has no consistent static equations under the tie."))
if not FAIL:
    print("HIT: exactly, a rotation of the forward bonds at x by eps_abj th_b and a rotation of the coin by th differ "
          "on plane waves by D = sum s_a eps_abj th_b [e^(-iq_a/2) cos(k_a+q_a/2) - 1] sin(k_j+q_j/2) cos(q_j/2) - "
          "i sum th_a sin(q_a/2) cos(k_a+q_a/2): O(k^3) at q = 0 and -(i/2) th.q at first order; on the exactly "
          "stationary 4^3 state the coin response vanishes at all sites while the forward-bond and shared-bond "
          "torques do not, so no such tie gives a th-blind field energy consistent static equations.")
sys.exit(1 if FAIL else 0)
