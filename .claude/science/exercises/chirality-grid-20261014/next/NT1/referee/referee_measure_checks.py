#!/usr/bin/env python3
"""Focused checks of the worker's finite-strip phase prescription."""

import numpy as np
import sys

sys.path.insert(0, "scripts")
from lat2d import Geom, nodes
from nt1_lib import Links, Chiral


def phase_abs(z):
    return float(abs(np.angle(np.exp(1j * z))))


def richardson(LK, A, n):
    ca = Chiral(LK, "11112", Ns=n, sk=-1)
    cb = Chiral(LK, "11112", Ns=2*n, sk=-1)
    wa, ga, oka = ca.logrho(A)
    wb, gb, okb = cb.logrho(A)
    wa = wa + 2j*np.pi*np.round((wb-wa).imag/(2*np.pi))
    return (4*wb-wa)/3, min(ga, gb), oka and okb


def main():
    z = np.load("scripts/pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz")
    G = Geom(2, 6, False, -1)
    LK = Links(G)
    U = [{"x": z["ux"][i], "t": z["ut"][i]} for i in range(len(z["ux"]))]
    ph, weights = nodes(G, U[0], U[1], 0.6, 16, "hard")
    A = LK.joined(U[0], U[1], ph[len(weights)//3:len(weights)//3+1])
    rng = np.random.default_rng(91827)
    transforms = {
        "random_0.2": rng.normal(0, 0.2, (1, LK.nsite)),
        "random_1.0": rng.normal(0, 1.0, (1, LK.nsite)),
        "random_3.0": rng.normal(0, 3.0, (1, LK.nsite)),
    }
    om = np.zeros((1, LK.nsite)); om[0, LK.site(0, 0)] = 2*np.pi
    transforms["identity_winding_2pi_one_site"] = om
    om2 = np.zeros((1, LK.nsite)); om2[0, LK.site(0, -2)] = 2*np.pi; om2[0, LK.site(1, 3)] = -2*np.pi
    transforms["identity_winding_two_sites"] = om2

    for n in (4, 8, 16, 32):
        w, gap, ok = richardson(LK, A, n)
        print(f"R{n}: base gap={gap:.12e} index={ok}")
        for label, omega in transforms.items():
            wg, gg, okg = richardson(LK, LK.gauge(A, omega), n)
            d = wg[0]-w[0]
            print(f"  {label:32s} dRe={d.real:+.3e} dphase={phase_abs(d.imag):.3e} gap={gg:.12e} index={okg}")

    # The algebraic divergence check is independent of the transport.
    anomaly = rng.normal(size=(7, LK.nsite))
    anomaly -= anomaly.mean(axis=1, keepdims=True)
    current, _ = LK.current(anomaly)
    print(f"current_divergence_max_error={np.max(np.abs(LK.div(current)-anomaly)):.3e}")


if __name__ == "__main__":
    main()
