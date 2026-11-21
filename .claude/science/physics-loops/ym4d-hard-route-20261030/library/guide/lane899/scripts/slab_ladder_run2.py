#!/usr/bin/env python3
"""GUIDE run 2 for FINISH row 899, Step 8.3. Decides nothing.

Same model and observables as slab_ladder_guide.py (imported), with a HOT start
(Haar-random time-like links and interior space-like links), so that order, if
seen, is not a memory of the flat start.

Criteria, written before this run (the quick run of slab_ladder_guide.py had
passed C0 and had shown m2 = 0.69, 0.42, 0.23, 0.11 for T = 1..4 at L = 8 from a
cold start, with G flat in r):
 D1. "Ordered at thickness T" if m2(L=12) >= 0.7 * m2(L=8) and G(6) at L=12 is
     at least 0.7 * G(4) at L=8 and m2(12) >= 0.02.
 D2. "Disordered" if chi = m2 * L^3 grows by less than 1.6 from L=8 to L=12.
 D3. Otherwise "undecided".
 Expectation to be tested (finite-temperature picture): order for T up to about
 the deconfinement length at beta 2.3 (N_t = 4 for a periodic time), hence at
 least T <= 4; the stiffness-in-series guess of Step 8.2 says order only for T <= 2.
"""
import sys, time
import numpy as np
from slab_ladder_guide import Slab

def haar(rng, shape):
    q = rng.normal(size=shape + (4,))
    return q / np.sqrt((q * q).sum(axis=-1, keepdims=True))

def run(L, T, beta, ntherm, nmeas, seed):
    sl = Slab(L, T, beta, seed)
    for s in range(T):
        sl.H[s] = haar(sl.rng, (L, L, L))
    for s in range(1, T):
        for mu in range(3):
            sl.U[s][mu] = haar(sl.rng, (L, L, L))
    for _ in range(ntherm):
        sl.sweep()
    m2s, gs = [], []
    for _ in range(nmeas):
        sl.sweep()
        m2, g = sl.measure()
        m2s.append(m2); gs.append(g)
    m2s = np.array(m2s); nb = 10
    blocks = m2s[: (len(m2s) // nb) * nb].reshape(nb, -1).mean(axis=1)
    return m2s.mean(), blocks.std(ddof=1) / np.sqrt(nb), np.mean(gs, axis=0)

def main():
    beta = float(sys.argv[1]) if len(sys.argv) > 1 else 2.3
    Ts = [int(t) for t in sys.argv[2].split(",")] if len(sys.argv) > 2 else [1, 2, 3, 4, 6, 8]
    nth, nme = 300, 700
    t0 = time.time()
    print(f"beta={beta} hot start, ntherm={nth}, nmeas={nme}")
    for T in Ts:
        res = {}
        for L in (8, 12):
            m2, err, g = run(L, T, beta, nth, nme, seed=100 * T + L)
            res[L] = (m2, err, g)
            print(f"  T={T} L={L}: m2={m2:.4f}+-{err:.4f} chi={m2 * L ** 3:.1f} "
                  f"G(1)={g[1]:.4f} G(2)={g[2]:.4f} G(L/2)={g[-1]:.4f}", flush=True)
        r_m = res[12][0] / max(res[8][0], 1e-12)
        r_g = res[12][2][-1] / max(res[8][2][-1], 1e-12)
        r_chi = res[12][0] * 12 ** 3 / max(res[8][0] * 8 ** 3, 1e-12)
        if r_m >= 0.7 and r_g >= 0.7 and res[12][0] >= 0.02:
            v = "ordered (D1)"
        elif r_chi < 1.6:
            v = "disordered (D2)"
        else:
            v = "undecided (D3)"
        print(f"  T={T}: m2 ratio {r_m:.2f}, G ratio {r_g:.2f}, chi ratio {r_chi:.2f} -> {v}", flush=True)
    print(f"elapsed {time.time() - t0:.1f} s")

if __name__ == "__main__":
    main()
