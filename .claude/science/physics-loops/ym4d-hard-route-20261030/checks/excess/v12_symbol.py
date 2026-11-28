#!/usr/bin/env python3
"""T12 of CRITERIA.md: sup over P of the abelian lift's constants, by the tensor structure."""
import numpy as np
from v8_lift1d import build


def tables(L, ngrid):
    n, Nc, T0, R0 = build(L, Nc=24)
    dz = np.roll(T0, -1, axis=0) - T0
    eta = np.zeros(n)
    for s in range(1, Nc // 2):
        eta += dz[:, s % Nc]
    x = np.arange(n)
    dist = ((x - L / 2 + n / 2) % n) - n / 2
    eta[np.abs(dist) > 6.5 * L] = 0
    zeta = T0[:, 0].copy()
    # eta sits on the bond (0, L): symmetric about L/2; zeta about 0. Moduli only are used.
    Ps = (np.arange(ngrid) + 0.5) * 2 * np.pi / ngrid - np.pi
    out = {}
    xs = ((x + n // 2) % n) - n // 2
    for name, ker in (("z", zeta), ("e", eta)):
        A = np.zeros(ngrid)
        G = np.zeros(ngrid)
        for i, P in enumerate(Ps):
            qs = (P + 2 * np.pi * np.arange(L)) / L
            kh = np.array([(ker * np.exp(-1j * q * xs)).sum() for q in qs])
            A[i] = (np.abs(kh) ** 2).sum() / L**2
            G[i] = ((np.abs(kh) ** 2) * (2 * np.sin(qs / 2)) ** 2).sum() / L**2
        out[name] = (A, G)
    return Ps, out


def main():
    for L in (3, 5, 7, 9, 13, 21, 41, 81):
        ng = 24
        Ps, t = tables(L, ng)
        Az, Gz = t["z"]
        Ae, Ge = t["e"]
        ph = (2 * np.sin(Ps / 2)) ** 2
        # orientation (0,1): eta in axes 0, 1, zeta in 2, 3
        Ax = [Ae, Ae, Az, Az]
        Gx = [Ge, Ge, Gz, Gz]
        I = np.ix_(range(ng), range(ng), range(ng), range(ng))
        E = Ax[0][I[0]] * Ax[1][I[1]] * Ax[2][I[2]] * Ax[3][I[3]]
        Gr = 0
        for a in range(4):
            term = 1.0
            for b in range(4):
                term = term * (Gx[b] if a == b else Ax[b])[I[b]]
            Gr = Gr + term
        P2 = ph[I[0]] + ph[I[1]] + ph[I[2]] + ph[I[3]]
        norm = E[ng // 2, ng // 2, ng // 2, ng // 2]
        C2 = (L**2 * Gr / P2 / norm).max()
        C1 = ((E / norm - 1) / P2).max()
        print(f"L {L}: norm {norm:.6f} C_2 sup {C2:.3f} C_2/L^2 {C2/L**2:.4f} C_1 sup {C1:.3f}", flush=True)


if __name__ == "__main__":
    main()
