#!/usr/bin/env python3
"""A13 check 3: two readings of "time = accumulation of records" in the assembled model (supplied toy).

Option-A records on a 3D torus under the six-layer cycle (x-even, x-odd, y-even, y-odd, z-even, z-odd):
in each tick every site has one partner; a record whose partner is empty re-forms there with odds s.
Counted per site:
  C2 = formation events including relocations (each arrival is a fresh formation under option A);
  C1 = distinct records formed at the site (new records only).
Case (a): quiet emptiness (no new formations).  Predicted (EXACT, product measure is stationary for the pair
          dynamics): arrivals per site per tick = s u (1-u); C2 grows linearly at every site; C1 = 0.
Case (b): illustration with a noisy emptiness (spontaneous formation p per empty site per tick): C1 per site
          saturates at <= 1 - rho0, the grid jams and C2 stops growing (time stops).
"""
import sys
import numpy as np


def layers(L):
    idx = np.arange(L ** 3).reshape(L, L, L)
    out = []
    for a in range(3):
        for par in (0, 1):
            m = np.moveaxis(idx, a, 0)
            left = m[par::2].ravel()
            right = np.roll(m, -1, axis=0)[par::2].ravel()
            out.append((left, right))
    return out


def run(L, u, s, T, p_form, seed):
    rng = np.random.default_rng(seed)
    n = L ** 3
    occ = rng.random(n) < u
    rho0 = occ.mean()
    lay = layers(L)
    C2 = np.zeros(n, np.int64)
    C1 = np.zeros(n, np.int64)
    snaps = {}
    nrec0 = occ.sum()
    for t in range(1, T + 1):
        left, right = lay[(t - 1) % 6]
        oL, oR = occ[left], occ[right]
        mov = (oL ^ oR) & (rng.random(left.size) < s)
        # record moves to the empty partner: arrival = a formation event at the destination
        to_right = mov & oL
        to_left = mov & oR
        occ[left[mov]] = ~occ[left[mov]]
        occ[right[mov]] = ~occ[right[mov]]
        C2[right[to_right]] += 1
        C2[left[to_left]] += 1
        if p_form > 0:
            new = (~occ) & (rng.random(n) < p_form)
            occ |= new
            C1[new] += 1
            C2[new] += 1
        if t in (500, 1000, 2000, T):
            snaps[t] = (C2.copy(), C1.copy(), occ.mean(), occ.sum())
    return rho0, nrec0, snaps


def main():
    L, s, T = 16, 0.5, 3000
    u = 0.2
    rho0, nrec0, sn = run(L, u, s, T, 0.0, 20261002)
    print(f"(a) quiet emptiness, L={L}, u={u}, s={s}: records at start {nrec0}, at end {sn[T][3]} (distinct records constant)")
    pred = s * u * (1 - u)
    for t in (500, 1000, 2000, T):
        C2, C1, dens, nr = sn[t]
        print(f"    t={t}: C2 per site mean/t = {C2.mean()/t:.5f} (s u(1-u) with realized u: {s*rho0*(1-rho0):.5f}); "
              f"min C2 over sites = {C2.min()}, max = {C2.max()}; C1 total = {C1.sum()}")
    C2a, C2b = sn[2000][0], sn[T][0]
    print(f"    sites with an arrival during ticks 2001-{T}: {np.mean(C2b - C2a > 0):.4f}")
    rho0, nrec0, sn = run(L, u, s, T, 0.01, 7)
    print(f"(b) noisy emptiness p=0.01 (illustration only): rho0={rho0:.4f}")
    for t in (500, 1000, 2000, T):
        C2, C1, dens, nr = sn[t]
        print(f"    t={t}: density={dens:.5f}; C1 per site mean = {C1.mean():.4f} (bound 1-rho0 = {1-rho0:.4f}); "
              f"C2 per site mean = {C2.mean():.3f}")
    C2a, C2b = sn[2000][0], sn[T][0]
    print(f"    events per site during ticks 2001-{T}: {np.mean(C2b - C2a):.2e} (frozen: time stops everywhere)")


if __name__ == '__main__':
    main()
