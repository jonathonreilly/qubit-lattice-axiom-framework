#!/usr/bin/env python3
"""A15 task 2 (1D): rate mismatch 2:1 for the A10 alternating-pairing cycle, one excitation, supplied toy.

Rigid local clocks. Time in half-ticks h. Region B (x >= s) runs one sub-step per half-tick (fast): jB = h + phiB.
Region A (x < s) runs one sub-step per tick (slow): jA = floor(h/2); an A site acts at most once per tick.
Seam rule H-rate: the cross pair (s-1, s) acts at half-tick h iff A's site names it this tick, B's site names it at
h, and it has not yet acted this tick. A-A pairs act at the first half-tick of each tick.
Frequency matching at a seam that repeats every 2 ticks: omega_cycle(K_A) = 2 omega_cycle(K_B) (mod 2 pi), where
cos omega_cycle = cos^2 th - sin^2 th cos K (A10 S4). Predictions: from slow A every packet has a partner in B;
from fast B a packet with |omega_B| > th has no partner in A's band and must reflect totally."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from seam1d import ublock, packet, branch

def sel1(x, j, N):
    y = x + 1 if j % 2 == x % 2 else x - 1
    return y if 0 <= y < N else -1

def step_pairs(N, s, h, phiA, phiB, acted_A):
    t = h // 2
    pairs = []
    sel = [sel1(x, (t + phiA) if x < s else (h + phiB), N) for x in range(N)]
    for x in range(N - 1):
        y = x + 1
        if sel[x] == y and sel[y] == x:
            if y < s:                     # A-A pair: first half-tick only
                if h % 2 == 0:
                    pairs.append((x, y))
            elif x >= s:                  # B-B pair
                pairs.append((x, y))
            else:                         # cross pair (s-1, s)
                if not acted_A.get(t, False):
                    pairs.append((x, y)); acted_A[t] = True
    return pairs

def omega(K, th):
    return np.arccos(np.clip(np.cos(th) ** 2 - np.sin(th) ** 2 * np.cos(K), -1, 1))

def run(th, K0, side, phiA=0, phiB=0, N=700, s=300, sigma=12.0):
    u = ublock(th)
    vg, w, _ = branch(K0, u, +1 if side == 'A' else -1)
    if side == 'A':
        psi = packet(N, s // 2 - 58, K0, sigma, u, +1, ) if phiA == 0 else None
        psi[s:] = 0
        Tticks = int(2 * 116 / abs(vg)) + 30            # A does half a cycle per tick
        H = 2 * Tticks
    else:
        tmp = packet(N + 2, s // 2 + 58, K0, sigma, u, -1)
        psi = tmp[phiB:N + phiB].copy() if phiB in (0, 1) else None
        psi[:s] = 0
        H = 2 * (int(116 / abs(vg)) + 30)               # B does a full cycle per tick
    psi = psi.astype(complex) / np.linalg.norm(psi)
    acted = {}
    for h in range(H):
        for (x, y) in step_pairs(N, s, h, phiA, phiB, acted):
            a, b = psi[x], psi[y]
            psi[x] = u[0, 0] * a + u[0, 1] * b
            psi[y] = u[1, 0] * a + u[1, 1] * b
    p = np.abs(psi) ** 2
    trans = p[s:].sum() if side == 'A' else p[:s].sum()
    # dominant momenta of the transmitted part (cell momentum, from even-site amplitudes)
    part = psi.copy()
    if side == 'A':
        part[:s] = 0
    else:
        part[s:] = 0
    ev = part[0::2]
    f = np.abs(np.fft.fft(ev, 4096)) ** 2
    Ks = 2 * np.pi * np.fft.fftfreq(4096)
    Kpk = Ks[np.argmax(f)] % (2 * np.pi)
    return trans, 1 - trans, Kpk, w, vg, H

def full_bands(th, M=20001):
    """quasi-energy per cycle (with the gate phases, as evolved) and group velocity on a K grid, both branches."""
    from seam1d import bloch_W
    u = ublock(th)
    Ks = np.linspace(0, 2 * np.pi, M, endpoint=False)
    W = np.array([bloch_W(K, u) for K in Ks])
    ev = np.linalg.eigvals(W)
    w = np.sort(-np.angle(ev), axis=1)
    return Ks, w

def predict(th, w_in, side):
    """transmitted cell momenta from matching w_A = 2 w_B (mod 2 pi) per 2 ticks, with outgoing velocity."""
    Ks, w = full_bands(th)
    dK = Ks[1] - Ks[0]
    target = (2 * w_in) if side == 'B' else None
    sols = []
    for b in range(2):
        wb = np.unwrap(w[:, b])
        vg = np.gradient(wb, dK)
        if side == 'A':      # need 2 w_B = w_in (mod 2 pi), transmitted into B moving right
            mis = np.angle(np.exp(1j * (2 * w[:, b] - w_in)))
            want = vg > 0
        else:                # need w_A = 2 w_in (mod 2 pi), transmitted into A moving left
            mis = np.angle(np.exp(1j * (w[:, b] - target)))
            want = vg < 0
        idx = np.where((np.abs(mis) < 2e-3) & want)[0]
        # keep one representative per cluster
        last = -10
        for i in idx:
            if i - last > 5:
                sols.append(round(float(Ks[i]), 3))
            last = i
    return sols

if __name__ == '__main__':
    print("rate 2:1 seam (A slow, B fast), rule H-rate; trans/refl of packets; peak cell momentum of transmitted part")
    print(" theta   side  K0     w_in(full)  trans     refl      K_trans  predicted K_trans (2-tick matching)")
    for th in (np.pi / 2, np.pi / 4, 0.3):
        for side, Ks in (('A', (np.pi - 0.4, 2.171)), ('B', (np.pi - 0.4, 2.171, 3.541, 4.112))):
            for K0 in Ks:
                if th == np.pi / 2 and K0 != Ks[0]:
                    continue
                tr, rf, Kt, w, vg, H = run(th, K0, side)
                pred = predict(th, w, side)
                print(" %.3f   %s    %.3f  %+.4f    %.6f  %.6f  %.3f    %s" % (th, side, K0, w, tr, rf, Kt,
                      pred if pred else "none (total reflection expected)"))
