#!/usr/bin/env python3
"""GUIDE validation of su2lat.py (row 918). Usage: validate.py part
part A: 3^4 torus at beta 2.3: coloured HB+OR vs sequential random-order HB (no colouring). Plaquette and |Polyakov|.
part B: strong coupling beta 0.5 on 3x4x4x4: plaquette vs u + 4u^5 (u = I2/I1). Free-wall box check: decoupled links.
part C: 8^4 plaquette at beta 2.3 and 2.5, timing per sweep; spin-weight estimator vs row 860 (guide860.out).
"""
import sys, time
import numpy as np
from scipy.special import iv
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from su2lat import Lattice, sequential_sweep, binned_err, PLANES

part = sys.argv[1]

def polyabs(lat, mu=0):
    _, P = lat.polyakov(mu); return np.abs(P[:, 0]).mean()

if part == 'A':
    for mode in ('colour', 'seq'):
        t = time.time()
        lat = Lattice((3, 3, 3, 3), 2.3, seed=11 if mode == 'colour' else 12)
        nth, nme = (200, 3000) if mode == 'colour' else (100, 1500)
        for _ in range(nth):
            lat.sweep(3) if mode == 'colour' else sequential_sweep(lat)
        P, Q = [], []
        for _ in range(nme):
            lat.sweep(3) if mode == 'colour' else sequential_sweep(lat)
            P.append(lat.plaquettes().mean()); Q.append(np.mean([polyabs(lat, m) for m in range(4)]))
        print(f"{mode}: <x_p> = {np.mean(P):.5f} +- {binned_err(P):.5f}   <|tr P|/2> = {np.mean(Q):.5f} +- {binned_err(Q):.5f}  classes={[len(c) for c in lat.classes]}  {time.time()-t:.0f}s", flush=True)

if part == 'B':
    b = 0.5; u = iv(2, b)/iv(1, b)
    lat = Lattice((3, 4, 4, 4), b, seed=21)
    for _ in range(100): lat.sweep(3)
    P = []
    for _ in range(2000):
        lat.sweep(3); P.append(lat.plaquettes().mean())
    print(f"beta 0.5 3x4^3: <x_p> = {np.mean(P):.5f} +- {binned_err(P):.5f}; u + 4u^5 = {u + 4*u**5:.5f}")
    lat = Lattice((4, 3, 3, 3), 2.3, seed=22, free=(False, True, True, True))
    for _ in range(100): lat.sweep(3)
    # crossing links of a free direction must be Haar: <U0> = 0, <U0^2> = 1/4
    vals = []
    for _ in range(400):
        lat.sweep(3)
        edge = lat.coords[1] == 2
        vals.append(lat.U[1][edge][:, 0])
    vals = np.concatenate(vals)
    print(f"free wall crossing links: mean a0 = {vals.mean():.4f} (Haar 0), mean a0^2 = {(vals**2).mean():.4f} (Haar 0.25)")
    x = lat.plaquettes(); w = lat.C
    print(f"free box 4x3^3: weighted plaquettes = {(w*x).sum()/w.sum():.4f}, number with c=1: {int(w.sum())}")

if part == 'C':
    for b in (2.3, 2.5):
        lat = Lattice((8, 8, 8, 8), b, seed=31)
        t = time.time()
        for _ in range(150): lat.sweep(3)
        ts = (time.time() - t)/150
        P = []; rho = []
        for i in range(300):
            lat.sweep(3); x = lat.plaquettes(); P.append(x.mean())
            if i % 3 == 0:
                sites = np.arange(lat.V)
                w = np.concatenate([lat.spin_weights(k, sites) for k in range(6)], axis=1)
                rho.append(w.mean(axis=1))
        rho = np.array(rho)
        print(f"beta {b} 8^4: <x_p> = {np.mean(P):.5f} +- {binned_err(P):.5f}; sweep(HB+3OR) = {ts:.3f}s", flush=True)
        print("  rho_j j=0..2.5:", " ".join(f"{m:.4e}+-{e:.1e}" for m, e in zip(rho.mean(0)[:6], binned_err(rho)[:6])), f" half-int sum {rho.mean(0)[1::2].sum():.5f}")
