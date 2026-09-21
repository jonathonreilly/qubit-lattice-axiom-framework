#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 75 (floating point; machinery disjoint from the exact runner's).

W1  CURVATURE MEMBER, AN ATTEMPT TO FIND A CLOSED LATTICE AT REST. On a 6 x 6 x 6 torus, three bodies with bare energies of mixed signs; unknowns
    log chi and log N at every site (so both fields stay positive); least-squares minimisation of the residuals of the two field equations
    (Delta chi)_z + mu_z/chi_z = 0 and [(Delta N)_z - mu_z N_z/chi_z^2]/N_z = 0 (per unit rate) from several random starts, for several choices of
    the mu's, with the mean length held fixed. Reported: the smallest residual norm reached, and the note's sum rule on the best point.
W2  SIMPLEST MEMBER. The lowest eigenvalue of -Delta + (gamma/2) t M on the same torus as a function of the overall scale t of the bodies, for a
    pair and for three bodies with sum m > 0: the scale t* at which it vanishes; for the pair, t* against the closed form; the lowest mode's sign.
W3  the pair's closed form on tori of side 4, 6, 8 at two separations (dense linear algebra for G).
"""
import itertools
import numpy as np
from scipy.optimize import least_squares, brentq

rng = np.random.default_rng(75)


def torus(side):
    n = side**3; idx = np.arange(n).reshape(side, side, side)
    lap = 6*np.eye(n)
    for a in range(3):
        nb = np.roll(idx, -1, axis=a).ravel()
        lap[idx.ravel(), nb] -= 1; lap[nb, idx.ravel()] -= 1
    return n, idx, lap                                           # lap = -Delta


def w1():
    side = 6; n, idx, lap = torus(side)
    places = [idx[0, 0, 0], idx[3, 1, 0], idx[1, 4, 2]]
    print("[W1] curvature member, 6x6x6 torus, three bodies; least squares over positive chi and N. The rates' equation is homogeneous in N, so its")
    print("     residual is taken PER UNIT RATE; the mean of chi is held at c (without that the bodies can be made negligible by inflating every length:")
    print("     the residual then tends to zero and is never attained). Reported: the smallest residual norm found from 6 random starts.")
    bond = lambda f: 0.5*np.sum((f[:, None] - f[None, :])**2/(f[:, None]*f[None, :])*(lap < -0.5))
    for mus in ((0.8, -0.5, -0.2), (1.0, -0.3, 0.2), (0.4, -0.6, 0.3), (0.5, 0.5, -0.9)):
        mu = np.zeros(n); mu[places] = mus
        line = []
        for c in (1.0, 2.0, 4.0):
            def fields(v):
                chi = np.exp(v[:n]); chi = c*chi/chi.mean()
                return chi, np.exp(v[n:])
            def residuals(v):
                chi, N = fields(v)
                return np.concatenate([-lap@chi + mu/chi, (-lap@N)/N - mu/chi**2])
            best = None
            for _ in range(6):
                sol = least_squares(residuals, 0.3*rng.normal(size=2*n), method="trf", max_nfev=300)
                if best is None or sol.cost < best.cost: best = sol
            chi, N = fields(best.x); r = residuals(best.x)
            line.append(f"c = {c}: |residual| = {np.sqrt(2*best.cost):.4f}, sum rule sum r1/chi + sum r2/N = {(r[:n]/chi).sum() + r[n:].sum():.4f} = bond forms {bond(N) + bond(chi):.4f}")
        print(f"     mu = {mus}: " + "; ".join(line))


def w2_w3():
    side = 6; n, idx, lap = torus(side); gam = 0.5
    print("\n[W2] simplest member, 6x6x6 torus, gamma = 1/2: lowest eigenvalue of -Delta + (gamma/2) t M as the overall scale t of the bodies grows")
    for label, places, ms in (("pair (3, -2)", [idx[0, 0, 0], idx[3, 1, 0]], (3.0, -2.0)), ("three bodies (3, -1, -1.5)", [idx[0, 0, 0], idx[3, 1, 0], idx[1, 4, 2]], (3.0, -1.0, -1.5))):
        M = np.zeros(n); M[places] = ms
        low = lambda t: np.linalg.eigvalsh(lap + np.diag(0.5*gam*t*M))[0]
        ts = np.linspace(0.0, 3.0, 13)
        vals = [low(t) for t in ts]
        t_star = brentq(low, 0.05, 3.0)
        w, v = np.linalg.eigh(lap + np.diag(0.5*gam*t_star*M)); mode = v[:, 0]*np.sign(v[:, 0].sum())
        print(f"     {label}: lambda_0 at t = 0.25, 0.5, 1, 2, 3: {vals[1]:+.5f}, {vals[2]:+.5f}, {vals[4]:+.5f}, {vals[8]:+.5f}, {vals[12]:+.5f}; vanishes at t* = {t_star:.6f}; lowest mode there positive at every site: {bool((mode > 0).all())}, rates at the bodies {np.round((mode[places]/mode.mean())**2, 4)}")
        if len(ms) == 2:
            G = np.linalg.pinv(lap); h = G[places[0], places[0]] - G[places[0], places[1]]
            # closed form with bodies t*m: 1/(t|m_B|) - 1/(t m_A) = gamma h
            t_closed = (1/abs(ms[1]) - 1/ms[0])/(gam*h)
            print(f"       closed form 1/|m_B| - 1/m_A = gamma (G_0 - G_d) with bodies t m: t* = {t_closed:.6f} (G_0 - G_d = {h:.6f})")
    print("\n[W3] the pair's condition on other tori (gamma = 1/2, m_A = 3): the m_B at which the lowest eigenvalue vanishes, against the closed form")
    for side in (4, 6, 8):
        n, idx, lap = torus(side); G = np.linalg.pinv(lap)
        for place in ((1, 0, 0), (2, 1, 0)):
            a, b = idx[0, 0, 0], idx[place]
            h = G[a, a] - G[a, b]
            closed = -1/(1/3.0 + gam*h)
            def low(mb):
                M = np.zeros(n); M[a] = 3.0; M[b] = mb
                return np.linalg.eigvalsh(lap + np.diag(0.5*gam*M))[0]
            root = brentq(low, -2.99, -0.5)
            print(f"     side {side}, B at {place}: numerical m_B = {root:.6f}, closed form {closed:.6f}")


if __name__ == "__main__":
    w1()
    w2_w3()
