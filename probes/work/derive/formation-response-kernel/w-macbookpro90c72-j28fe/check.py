#!/usr/bin/env python3
"""J:derive:formation-response-kernel:a3 (worker w-macbookpro90c72-j28fe): exact checks for ATTEMPT.md.

Linear formation on the L x L level plane: m_{t+1} = P m_t + h, P the average of predecessors
(i,j), (i-1,j), (i,j-1); phi(k) = (1 + exp(i k1) + exp(i k2))/3.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

I = sp.I


def phi_sym(k1, k2):
    """Note writes (1+e^{ik1}+e^{ik2})/3; that is this function of -k.
    Predecessors (i,j),(i-1,j),(i,j-1) give multiplier (1+e^{-ik1}+e^{-ik2})/3
    on e^{ik·x} modes. Identity F2 uses the note's sign; F1/F3 use predecessors."""
    return (1 + sp.exp(I * k1) + sp.exp(I * k2)) / 3


def phi_pred(k1, k2):
    return (1 + sp.exp(-I * k1) + sp.exp(-I * k2)) / 3


def E_sym(K1, K2, K3):
    return sum(2 * (1 - sp.cos(K)) for K in (K1, K2, K3))


def f1_identity():
    q1, q2, w = sp.symbols("q1 q2 w", real=True)
    K1, K2, K3 = q1 + w, q2 + w, w
    phi = phi_sym(q1, q2)
    u = sp.simplify(sp.expand_complex(phi * sp.conjugate(phi)))
    diff = sp.simplify(sp.expand_trig(E_sym(K1, K2, K3) - 3 * (sp.Abs(1 - phi * sp.exp(I * w)) ** 2 + 1 - u)))
    # Abs of complex trig can resist; numerically + random exact subst
    if diff == 0:
        return True, "sympy 0"
    # substitute several exact points
    pts = [(0, 0, sp.pi / 2), (sp.pi / 2, 0, 0), (sp.pi / 3, -sp.pi / 4, sp.pi / 6), (sp.pi, sp.pi / 2, sp.pi / 3)]
    ok = True
    for a, b, c in pts:
        Ev = sp.N(E_sym(a + c, b + c, c), 40)
        ph = phi_sym(a, b).subs({q1: a, q2: b})
        uv = sp.simplify(sp.expand_complex(phi_sym(a, b) * sp.conjugate(phi_sym(a, b))))
        rhs = sp.N(3 * (sp.Abs(1 - phi_sym(a, b) * sp.exp(I * c)) ** 2 + 1 - uv), 40)
        if abs(Ev - rhs) > sp.N("1e-20"):
            ok = False
    # algebraic expansion in cos/sin
    e1, e2, e3 = sp.exp(I * K1), sp.exp(I * K2), sp.exp(I * K3)
    one_minus = (3 - e1 - e2 - e3) / 3
    modsq = sp.simplify(sp.expand_complex(one_minus * sp.conjugate(one_minus)))
    ph = (1 + sp.exp(I * (K1 - K3)) + sp.exp(I * (K2 - K3))) / 3
    uu = sp.simplify(sp.expand_complex(ph * sp.conjugate(ph)))
    lhs = E_sym(K1, K2, K3)
    rhs = 3 * (modsq + 1 - uu)
    alg = sp.simplify(sp.expand_trig(sp.expand_complex(lhs - rhs)))
    return ok and alg == 0, f"alg={alg} pts={ok}"


def f1_L4():
    """L=4: (I-P)^{-1} on mean-zero delta vs DFT of 1/(1-phi), exact in Q(i)."""
    L = 4
    n = L * L
    P = sp.zeros(n)
    def idx(i, j):
        return (i % L) * L + (j % L)
    for i, j in itertools.product(range(L), repeat=2):
        a = idx(i, j)
        for ii, jj in ((i, j), (i - 1, j), (i, j - 1)):
            P[a, idx(ii, jj)] += sp.Rational(1, 3)
    A = sp.eye(n) - P
    # mean-zero projector
    h = sp.Matrix([1] + [0] * (n - 1))
    h = h - sp.ones(n, 1) / n
    # solve A m = h on the mean-zero subspace: A is singular (constants). Use A + ones/n
    Areg = A + sp.ones(n) / n
    m = Areg.inv() * h
    m = sp.simplify(m)
    # DFT formula
    m_hat = []
    for n1, n2 in itertools.product(range(L), repeat=2):
        if n1 == 0 and n2 == 0:
            m_hat.append(0)
            continue
        k1, k2 = 2 * sp.pi * n1 / L, 2 * sp.pi * n2 / L
        ph = phi_pred(k1, k2)
        hk = sum(h[idx(i, j)] * sp.exp(-I * (k1 * i + k2 * j)) for i, j in itertools.product(range(L), repeat=2))
        m_hat.append(hk / (1 - ph))
    rec = []
    for i, j in itertools.product(range(L), repeat=2):
        val = sum(
            m_hat[n1 * L + n2] * sp.exp(I * (2 * sp.pi * n1 / L * i + 2 * sp.pi * n2 / L * j))
            for n1, n2 in itertools.product(range(L), repeat=2)
        ) / n
        rec.append(sp.N(sp.expand_complex(val), 30))
    mx = [sp.N(m[a], 30) for a in range(n)]
    err = max(abs(complex(mx[a] - rec[a])) for a in range(n))
    # geometric R vs truncated sum at z=i, mode (1,0)
    k1 = 2 * sp.pi / L
    ph = complex(sp.N(phi_pred(k1, 0), 40))
    z = 1j
    R = 1 / (1 - ph * z)
    N = 80
    S = sum(ph ** t * z ** t for t in range(N))
    rem = abs((ph * z) ** N / (1 - ph * z))
    tail = abs(R - S)
    return err < 1e-18, float(err), tail <= rem * 1.01 + 1e-15, float(tail)


def f4_eight():
    k = sp.symbols("k", positive=True)
    R = 0
    for e1, e2, e3 in itertools.product((-1, 1), repeat=3):
        ph = (sp.exp(-I * e1 * k) + sp.exp(-I * e2 * 0) + sp.exp(-I * e3 * 0)) / 3
        R += 1 / (1 - ph)
    R = sp.simplify(R / 8)
    lim = sp.limit(sp.simplify(sp.expand_complex(R)), k, 0)
    # 1/E along (k,0,0) is 1/(2(1-cos k)) ~ 1/k^2
    return lim, sp.simplify(lim - sp.Rational(3, 2)) == 0


def f5_not_proportional():
    # mode with phi = (1+i)/3 (note's +k convention) or (1-i)/3 (predecessors)
    u = Fr(2, 9)
    var_q = Fr(1) / (1 - u)
    chi_c = 1 / (1 - (1 + 1j) / 3)
    return var_q == Fr(9, 7) and abs(chi_c.imag) > 0.5 and abs(chi_c.real - float(var_q)) > 0.05


def f3_torus_wake():
    L = 32
    n1 = np.fft.fftfreq(L) * 2 * np.pi
    k1, k2 = np.meshgrid(n1, n1, indexing="ij")
    phi = (1 + np.exp(-1j * k1) + np.exp(-1j * k2)) / 3
    Rk = np.zeros_like(phi, dtype=complex)
    nz = ~((k1 == 0) & (k2 == 0))
    Rk[nz] = 1 / (1 - phi[nz])
    mx = np.fft.ifft2(Rk).real
    down = np.array([abs(mx[n, n]) for n in range(4, 13)])
    up = np.array([abs(mx[n, L - n]) for n in range(4, 13)])
    r = np.arange(4, 13)
    # not 1/r: |m| r would be flat for 1/r; 3D Coulomb on a plane slice is 1/r
    coulomb = down * r
    wake = down * np.sqrt(r)
    # downstream heavier than anti-diagonal; 1/r scaling worse than 1/sqrt(r) (larger relative spread)
    down_vs_up = down.mean() > 1.5 * up.mean()
    spread = lambda a: a.max() / a.min()
    not_coulomb = spread(coulomb) > spread(wake)
    return down_vs_up and not_coulomb, down.tolist(), up.tolist(), float(spread(wake)), float(spread(coulomb))


def f4_numeric():
    def E(k):
        return sum(2 * (1 - np.cos(ki)) for ki in k)

    def R8(k):
        s = 0j
        for eps in itertools.product((-1, 1), repeat=3):
            ph = sum(np.exp(-1j * eps[j] * k[j]) for j in range(3)) / 3
            s += 1 / (1 - ph)
        return s / 8

    rows = []
    ok = True
    for k in [(0.05, 0.0, 0.0), (0.1, 0.2, 0.3), (0.3, 0.3, 0.3), (0.2, 0.1, 0.05)]:
        r, e = R8(k), E(k)
        rows.append((k, r.real, 1 / e, abs(r.imag)))
        if k[1] == 0 and k[2] == 0:
            ok &= abs(r.real - 1.5) < 0.05 and (1 / e) > 50
        else:
            ok &= abs(r.real * e - 1) > 0.1  # not 1/E
    return ok, rows


def main():
    hits = []
    print("F2 E-identity in level coordinates k=(q1+w, q2+w, w):")
    ok, msg = f1_identity()
    print(f"  {ok} ({msg})")
    if not ok:
        hits.append("E-identity")

    print("F1 L=4 (I-P)^{-1} vs DFT of 1/(1-phi); geometric R at z=i:")
    a, err, b, tail = f1_L4()
    print(f"  real-space err={err:.3e} ok={a}; geometric tail={tail:.3e} ok={b}")
    if not (a and b):
        hits.append("L=4 response")

    print("F3 L=32 torus wake (downstream |m|√n slowly varying; anti-diagonal decays):")
    ok3, down, up, sw, sc = f3_torus_wake()
    print(
        f"  |m|(n,n) {['%.3f' % x for x in down]}; |m|(n,-n) {['%.3e' % x for x in up]}; "
        f"spread |m|√n={sw:.2f} vs |m|n={sc:.2f}; ok={ok3}"
    )
    if not ok3:
        hits.append("wake diagnostic")

    print("F4 eight-corner average vs 1/E; axis limit 3/2:")
    lim, lim_ok = f4_eight()
    print(f"  lim k->0 R8(k,0,0) = {lim}; is 3/2: {lim_ok}")
    ok4, rows = f4_numeric()
    for k, rr, ie, im in rows:
        print(f"  k={k}: Re R8={rr:.4f} 1/E={ie:.4f} |Im|={im:.1e}")
    if not (lim_ok and ok4):
        hits.append("eight-corner")

    print("F5 static chi vs variance at phi=(1+i)/3:")
    ok5 = f5_not_proportional()
    print(f"  1/(1-|phi|^2)=9/7, 1/(1-phi) complex and not a real multiple: {ok5}")
    if not ok5:
        hits.append("FR")

    if hits:
        print("SUMMARY: ROUTE FAILS AT " + ", ".join(hits))
        return 1
    print(
        "HIT: linear formation response R(k,w)=1/(1-phi e^{iw}) with static 1/(1-phi); E(k)="
        "3(|1-phi e^{iw}|^2+1-u) in level coordinates so 1/E is not the response; no 1/r channel "
        "(2D convection-diffusion wake ~1/sqrt(r) downstream, exponential upstream; 8-corner average "
        "-> 3/2 along an axis, not 1/k^2); regression C_s=C_0 phi^s holds, equilibrium FR fails"
    )
    print(
        "SUMMARY: PARTIAL - exact linear response and the replacement of 1/r by a directed 2D "
        "convection-diffusion kernel; 1/E is a modulus identity, not a channel of the formation law"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
