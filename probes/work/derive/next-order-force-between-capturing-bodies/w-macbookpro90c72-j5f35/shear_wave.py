#!/usr/bin/env python3
"""Transverse momentum diffusivity nu_T of block 44's sphere-menu gas, measured with the block's own simulator (floating point; executed,
not claimed).  A periodic box of side L at density rho, contents drawn from (1 + 3 u.s)/(4 pi) with u = eps cos(k y) x^ (a shear wave, no
density perturbation); the amplitude A(t) = 2 sum occ s_x cos(k y) / (rho L^3 eps) decays as exp(-nu_T k^2 t) in the linearized
hydrodynamics (the transverse mode is purely diffusive).  usage: shear_wave.py L rho gamma mode T runs seed [eps] [diag]
(diag: k along (1,1,0) with |k| = 2 pi mode sqrt2/L and the flow along (1,-1,0)/sqrt2 - the other cubic shear viscosity)"""
import sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "lib"))
import inertial as I


def shear_gas(L, rho, eps, phase, e, rng):
    occ = rng.random((L, L, L)) < rho
    amp = eps * np.cos(phase)                           # u = amp e
    s = rng.normal(size=(L, L, L, 3)); s /= np.linalg.norm(s, axis=-1, keepdims=True)
    todo = np.ones((L, L, L), bool)
    while todo.any():                                   # rejection: accept with (1 + 3 u.s)/(1 + 3|u|)
        acc = rng.random((L, L, L)) < (1 + 3 * amp * (s @ e)) / (1 + 3 * np.abs(amp))
        todo &= ~acc
        if todo.any():
            snew = rng.normal(size=(L, L, L, 3)); snew /= np.linalg.norm(snew, axis=-1, keepdims=True)
            s[todo] = snew[todo]
    return occ, s[..., 0].copy(), s[..., 1].copy(), s[..., 2].copy()


def main():
    L, rho, gamma, mode, T, runs, seed = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
    eps = float(sys.argv[8]) if len(sys.argv) > 8 else 0.3
    diag = len(sys.argv) > 9 and sys.argv[9] == "diag"
    X, Y, Z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
    if diag:
        k = 2 * np.pi * mode * np.sqrt(2) / L; phase = 2 * np.pi * mode * (X + Y) / L; e = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)
    else:
        k = 2 * np.pi * mode / L; phase = 2 * np.pi * mode * Y / L; e = np.array([1.0, 0.0, 0.0])
    rng = np.random.default_rng(seed); I.seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); force = np.zeros((3, 3))
    cosp = np.cos(phase)
    amps = np.zeros((runs, T + 1))
    t0 = time.time()
    for r in range(runs):
        occ, sx, sy, sz = shear_gas(L, rho, eps, phase, e, rng)
        for t in range(T + 1):
            amps[r, t] = 2 * np.sum(occ * (sx * e[0] + sy * e[1] + sz * e[2]) * cosp) / (rho * L ** 3 * eps)
            if t < T:
                I.tick_s(occ, sx, sy, sz, solid, force, L, True, gamma, False)
    A = amps.mean(axis=0); E = amps.std(axis=0, ddof=1) / np.sqrt(runs)
    # fit log A over the window t in [t1, t2] where A > 0.15: slope = -nu k^2; errors from the spread of per-run fits
    t1 = 5
    t2 = int(np.max(np.nonzero(A > 0.15)[0]))
    tt = np.arange(t1, t2 + 1)
    slope = np.polyfit(tt, np.log(A[t1:t2 + 1]), 1)[0]
    per = []
    for r in range(runs):
        m = amps[r, t1:t2 + 1] > 0.05
        if m.sum() > 5:
            per.append(np.polyfit(tt[m], np.log(amps[r, t1:t2 + 1][m]), 1)[0])
    per = np.array(per)
    nu = -slope / k ** 2; dnu = per.std(ddof=1) / np.sqrt(len(per)) / k ** 2
    print(f"side {L}, rho {rho}, gamma {gamma}, mode {mode} (k = {k:.4f}), eps {eps}{', diagonal' if diag else ''}, {runs} runs x {T} ticks, seed {seed}: "
          f"A(t) every {max(1, T // 10)} ticks: " + " ".join(f"{A[t]:.3f}" for t in range(0, T + 1, max(1, T // 10))))
    print(f"   fit window t = {t1}..{t2}: nu_T = {nu:.4f} +- {dnu:.4f}  ({time.time() - t0:.0f} s)")


if __name__ == "__main__":
    main()
