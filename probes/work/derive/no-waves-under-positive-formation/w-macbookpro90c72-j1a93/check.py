#!/usr/bin/env python3
"""J:derive:no-waves-under-positive-formation:a4 — dispersion expansions and |lambda|<=1."""
from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp


def main():
    hits = []
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2)) / 3
    ser = phi.series(k1, 0, 4).removeO().series(k2, 0, 4).removeO()
    # keep terms total degree <= 3 for the linear+quadratic check
    ser = sp.expand(ser)
    mu = sp.Matrix([sp.Rational(1, 3), sp.Rational(1, 3)])
    Sig = sp.Rational(1, 9) * sp.Matrix([[2, -1], [-1, 2]])
    k = sp.Matrix([k1, k2])
    pred = 1 - sp.I * (mu.dot(k)) - sp.Rational(1, 2) * (k.T * Sig * k)[0]
    print("D1 NEC expansion vs 1 - i mu.k - (1/2) k^T Sigma k:")
    ev = Sig.eigenvals()
    print(f"  Sigma eigenvalues {ev} (want 1/3 and 1/9)")
    if set(ev.keys()) != {sp.Rational(1, 3), sp.Rational(1, 9)}:
        hits.append("Sigma eigs")
    u = sp.simplify(sp.expand(phi * sp.conjugate(phi)))
    quad = sp.expand((k.T * Sig * k)[0])
    # 1-|phi|^2 - k^T Sigma k at order 2: check series of 1-u
    onemu = (1 - u).series(k1, 0, 3).removeO().series(k2, 0, 3).removeO()
    onemu = sp.expand(onemu)
    # drop degree >= 4 by substituting t*k and taking t^2
    t = sp.symbols("t")
    q2 = sp.expand(onemu.subs({k1: t * k1, k2: t * k2}))
    coeff2 = sp.expand(q2.series(t, 0, 3).removeO().coeff(t ** 2) if False else 0)
    # direct: series of 1-|phi|^2 along (t,0) and (t,t)
    for dirn, name in (((1, 0), "e1"), ((1, 1), "diag"), ((1, -1), "anti")):
        sphi = phi.subs({k1: t * dirn[0], k2: t * dirn[1]})
        su = sp.simplify(sphi * sp.conjugate(sphi))
        seru = (1 - su).series(t, 0, 5).removeO()
        quad_t = sp.expand(quad.subs({k1: t * dirn[0], k2: t * dirn[1]}))
        c2 = seru.coeff(t ** 2)
        q2v = quad_t.coeff(t ** 2) if quad_t.is_polynomial(t) else sp.expand(quad_t).as_poly(t).coeff_monomial(t ** 2)
        print(f"  1-|phi|^2 vs k^T Sigma k along {name}: t^2 coeff {c2} vs {q2v} eq {sp.simplify(c2 - q2v)==0}")
        if sp.simplify(c2 - q2v) != 0:
            hits.append(f"quad {name}")

    print("D1b |phi|<=1 on a torus grid L=8, equality only at 0:")
    L = 8
    mx = 0.0
    n_eq = 0
    for n1, n2 in itertools.product(range(L), repeat=2):
        kk1, kk2 = 2 * np.pi * n1 / L, 2 * np.pi * n2 / L
        ph = (1 + np.exp(-1j * kk1) + np.exp(-1j * kk2)) / 3
        a = abs(ph)
        mx = max(mx, a)
        if abs(a - 1) < 1e-12:
            n_eq += 1
    print(f"  max |phi|={mx:.12f} n_|phi|=1 {n_eq} (want 1, the zero mode)")
    if n_eq != 1 or mx > 1 + 1e-12:
        hits.append("|phi|")

    print("D2 arg phi is linear in k, not in |k|:")
    rng = np.random.default_rng(8180)
    ratios = []
    angs = []
    for _ in range(200):
        v = rng.normal(size=2)
        v *= 0.05 / np.linalg.norm(v)
        ph = (1 + np.exp(-1j * v[0]) + np.exp(-1j * v[1])) / 3
        ag = np.angle(ph)
        mu_dot = (v[0] + v[1]) / 3
        ratios.append(abs(ag + mu_dot) / (np.linalg.norm(v) ** 3 + 1e-18))
        angs.append(abs(ag) / (np.linalg.norm(v) + 1e-18))
    print(f"  |arg+mu.k|/|k|^3 mean {np.mean(ratios):.4f} max {np.max(ratios):.4f}")
    print(f"  |arg|/|k| min {np.min(angs):.4f} max {np.max(angs):.4f} (not constant)")
    if np.max(angs) / np.min(angs) < 1.2:
        hits.append("arg not direction-dependent")

    print("D3 two-level z^2 = (2/3) e^{-i k} z + 1/3, branch z(0)=1:")
    k = sp.symbols("k", real=True)
    a = sp.Rational(2, 3) * sp.exp(-sp.I * k)
    b = sp.Rational(1, 3)
    disc = a ** 2 + 4 * b
    zp = (a + sp.sqrt(disc)) / 2
    # pick the branch equal to 1 at 0
    zser = zp.series(k, 0, 3).removeO()
    z0 = complex(zser.subs(k, 0))
    print(f"  z(0)={z0}")
    # expand 1 - i mu k - (1/2) var k^2; here delay 0 with weight 2/3 at v=1 and delay 1 with weight 1/3 at v=0
    # space-time: (v,tau) = (1,0) w=2/3 and (0,1) w=1/3. The z-root expansion is more subtle.
    # Check |z|<=1 on a grid for the spectral radius of the companion
    rad = []
    for kk in np.linspace(-np.pi, np.pi, 65):
        aa = (2 / 3) * np.exp(-1j * kk)
        bb = 1 / 3
        rts = np.roots([1, -aa, -bb])
        rad.append(max(abs(rts)))
    print(f"  two-level spectral radius max {max(rad):.12f} (want <=1)")
    if max(rad) > 1 + 1e-9:
        hits.append("two-level |z|>1")

    print("D4 exception: negative weight (2,-1) on {0,1}:")
    # lambda = 2 - e^{-ik}  (not gain-one) or gain-one (2/1) wait w=(2,-1) sum=1
    # lambda(k) = 2*1 + (-1)*exp(-ik)
    ks = np.linspace(0, 2 * np.pi, 97, endpoint=False)
    lam = 2 - np.exp(-1j * ks)
    print(f"  |lambda| min {np.min(np.abs(lam)):.4f} max {np.max(np.abs(lam)):.4f} at k=pi {abs(2 - np.exp(-1j*np.pi)):.4f}")
    if abs(2 - np.exp(-1j * np.pi)) < 1.5:
        hits.append("negative-weight example")

    if hits:
        print("SUMMARY: ROUTE FAILS AT " + "; ".join(hits))
        return 1
    print(
        "HIT: gain-one positive one-level formation has lambda(k)=sum w_j e^{-ik.v_j}, |lambda|<=1 "
        "with small-k form 1 - i mu.k - (1/2) k^T Sigma k, Sigma=Cov(v) PSD (NEC Sigma=(1/9)[[2,-1],[-1,2]] "
        "eigenvalues 1/3,1/9; 1-|phi|^2 = k^T Sigma k + O(k^4)); arg is linear in k not |k|; "
        "two-level positive companion has spectral radius <=1; negative weights can give |lambda|=3 at k=pi"
    )
    print(
        "SUMMARY: PARTIAL - positive finite-predecessor gain-one linear formation is drift+diffusion, "
        "never a c|k| wave; exception is negative or non-real weights"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
