#!/usr/bin/env python3
"""A15: (1) 'angle lapse' alternative: one shared beat, gate angle theta(x) varying along the chain (A10 1D cycle,
one excitation): smooth vs sharp change, transmission and quasi-energy matching (supplied toy).
(2) 2D A11 rigid clocks, handshake: the region L evolves exactly as if region R were recorded (A11 lock rule)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from seam1d import ublock, packet, branch, bloch_W
import a11walls as aw

# (1) angle lapse
def run_angle(thA, thB, width, K0, N=900, a=400):
    x = np.arange(N - 1)
    if width == 0:
        thb = np.where(x < a, thA, thB)
    else:
        thb = np.where(x < a, thA, np.where(x > a + width, thB, thA + (thB - thA) * (x - a) / width))
    uA = ublock(thA)
    vg, wA, _ = branch(K0, uA, +1)
    psi = packet(N, a // 2 - 60, K0, 12.0, uA, +1).astype(complex)
    psi[a:] = 0; psi /= np.linalg.norm(psi)
    T = int(2 * 180 / vg) + 40
    for t in range(T):
        par = t % 2
        A = np.arange(par, N - 1, 2)
        B = A + 1
        th = thb[A]
        cth, sth = np.cos(th), np.sin(th)
        ph = np.exp(1j * th)
        pa, pb = psi[A].copy(), psi[B].copy()
        psi[A] = ph * (cth * pa - 1j * sth * pb)
        psi[B] = ph * (-1j * sth * pa + cth * pb)
    p = np.abs(psi) ** 2
    end = a + width
    # dominant cell momentum of the transmitted part
    part = psi.copy(); part[:end + 1] = 0
    f = np.abs(np.fft.fft(part[0::2], 8192)) ** 2
    Kt = (2 * np.pi * np.fft.fftfreq(8192))[np.argmax(f)] % (2 * np.pi)
    # predicted: same full quasi-energy per cycle (beat shared), right-moving branch in B
    Ks = np.linspace(0, 2 * np.pi, 40001, endpoint=False)
    best = None
    uB = ublock(thB)
    for K in Ks[::1]:
        pass
    ev = np.array([np.sort(-np.angle(np.linalg.eigvals(bloch_W(K, uB)))) for K in Ks])
    cand = []
    for bnd in range(2):
        w = ev[:, bnd]
        vgB = np.gradient(np.unwrap(w), Ks[1] - Ks[0])
        mis = np.abs(np.angle(np.exp(1j * (w - wA))))
        ok = np.where((mis < 2e-3) & (vgB > 0))[0]
        if ok.size:
            cand.append(round(float(Ks[ok[np.argmin(mis[ok])]]), 3))
    return p[end:].sum(), p[:a].sum(), Kt, cand

if __name__ == "__main__":
    print("(1) angle lapse: one shared beat, gate angle changes from thA to thB (A10 1D, one excitation)")
    for thA, thB in ((np.pi / 4, np.pi / 8), (0.6, 0.3)):
        for K0 in (np.pi - 0.3, np.pi - 0.6):
            for width in (0, 20, 100):
                tr, rf, Kt, pred = run_angle(thA, thB, width, K0)
                print("  thA=%.3f thB=%.3f K0=%.3f ramp width %3d sites: transmitted %.4f reflected %.4f  K_out %.3f  (matching %s)"
                      % (thA, thB, K0, width, tr, rf, Kt, pred))

    # (2) phantom-lock equivalence in 2D
    L = 16
    print("(2) A11 rigid clocks + handshake: L-region permutation vs L-region with R recorded (lock rule)")
    for k in (1, 2, 3):
        phi = np.zeros((L, L), int); phi[4:12, :] = k
        fin_h, _ = aw.cycle_perm(L, phi, 'H')
        # lock rule: offset-0 cycle with R sites recorded (pairs touching a recorded site skipped)
        locked = {(x, y) for x in range(4, 12) for y in range(L)}
        where = {(x, y): (x, y) for x in range(L) for y in range(L)}
        for t in range(4):
            pairs = aw.substep_pairs(L, (t + np.zeros((L, L), int)) % 4, 'H')
            new = dict(where)
            for a_, b_ in pairs:
                if a_ in locked or b_ in locked:
                    continue
                new[a_], new[b_] = where[b_], where[a_]
            where = new
        fin_lock = {item: site for site, item in where.items()}
        Lsites = [s for s in fin_h if s not in locked]
        same_L = all(fin_h[s] == fin_lock[s] for s in Lsites)
        # and R region vs offset-k cycle with L recorded
        lockedL = {(x, y) for x in range(L) for y in range(L)} - locked
        where = {(x, y): (x, y) for x in range(L) for y in range(L)}
        for t in range(4):
            pairs = aw.substep_pairs(L, (t + k + np.zeros((L, L), int)) % 4, 'H')
            new = dict(where)
            for a_, b_ in pairs:
                if a_ in lockedL or b_ in lockedL:
                    continue
                new[a_], new[b_] = where[b_], where[a_]
            where = new
        fin_lockL = {item: site for site, item in where.items()}
        same_R = all(fin_h[s] == fin_lockL[s] for s in locked)
        print("  offset k=%d: L side identical to 'R recorded': %s; R side identical to 'L recorded': %s" % (k, same_L, same_R))
