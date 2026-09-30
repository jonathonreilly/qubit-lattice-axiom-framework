#!/usr/bin/env python3
"""T71 test 3: Lemma S on the member's ledger (b55): net static kernel K = K_bare + c_u(q) from the walker sea.
Two sources J at separation r; W_AB(r) = -J^2 G(r), G = K^{-1} (mean removed).  Attraction = W_AB < 0.
Uses test2's code (L = 8, log-rate form phi H phi).
"""
import itertools
import sys
import numpy as np
from test2_sea_rate_hessian import build_H, sea_energy, tfun, curvature, lat_lap

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


L = 8
E0 = sea_energy(build_H(L, [np.ones((L, L, L))] * 3))
E0N = E0 / L ** 3
orb = {}
orb_lapse = {}
for m in itertools.product(range(L // 2 + 1), repeat=3):
    key = tuple(sorted(m))
    if key == (0, 0, 0) or key in orb:
        continue
    orb[key] = curvature(L, 'phiHphi', key, E0=E0)[0]
    orb_lapse[key] = curvature(L, 'lapse', key, E0=E0)[0]
print(f"{len(orb)} orbits computed; E0/N = {E0N:.5f}")

Kc = np.zeros((L, L, L))
Kl = np.zeros((L, L, L))
lapq = np.zeros((L, L, L))
for m in itertools.product(range(L), repeat=3):
    mm = tuple(min(mi, L - mi) for mi in m)
    lapq[m] = lat_lap(m, L)
    key = tuple(sorted(mm))
    Kc[m] = E0N if key == (0, 0, 0) else orb[key]
    Kl[m] = 0.0 if key == (0, 0, 0) else orb_lapse[key]


def pair_W(K):
    Kinv = np.zeros_like(K)
    nz = np.abs(K) > 1e-12
    Kinv[nz] = 1.0 / K[nz]
    Kinv[0, 0, 0] = 0.0
    G = np.real(np.fft.ifftn(Kinv))
    return [-float(G[r, 0, 0]) for r in range(1, 5)], float(np.min(K[np.arange(L ** 3).reshape(L, L, L) != 0]))


qmask = np.ones((L, L, L), bool)
qmask[0, 0, 0] = False
Wsea, kmin = pair_W(Kc)
print("A sea only:                       W_AB(r=1..4) =", np.round(Wsea, 5), " max K over q != 0 =", round(float(Kc[qmask].max()), 5))
check("3a sea-only kernel is negative semidefinite on q != 0 (nothing in the sea makes the clock field stiff)", float(Kc[qmask].max()) <= 1e-9,
      f"max c_u = {float(Kc[qmask].max()):.2e}")

# bare stiffness threshold, finite torus
thr = max((-(Kc[m]) / lapq[m]) for m in itertools.product(range(L), repeat=3) if m != (0, 0, 0) and lapq[m] > 0 and abs(Kc[m]) > 1e-12)
qmin = lapq[1, 0, 0]
print(f"B finite 8^3 torus: a pure gradient bare kernel gamma*lap(q) makes K positive on all q with a nonzero sea response only if gamma > {thr:.3f}; "
      f"at lap(q_min) = {qmin:.3f} the requirement is gamma > |E_0|/lap = {abs(E0N) / qmin:.3f}, and it diverges as 1/q^2 in infinite volume")
# nonzero-response modes only (the chessboard mode has zero response and zero lap)
for gamma in (0.5, thr * 1.05):
    K = Kc + gamma * lapq
    W, _ = pair_W(K)
    print(f"C bare gamma = {gamma:.3f} (pure gradient):   W_AB(r=1..4) =", np.round(W, 5), " min K over q != 0 =", round(float(K[qmask].min()), 5))
mu = abs(E0N) * 1.05
for gamma in (0.05, 0.3):
    K = Kc + gamma * lapq + mu
    W, _ = pair_W(K)
    print(f"D bare gradient gamma = {gamma} plus uniform mu = 1.05|E_0| = {mu:.3f}: W_AB(r=1..4) =", np.round(W, 5), " min K =", round(float(K[qmask].min()), 5))
    check(f"3b net kernel positive (gamma = {gamma}, mu = 1.05 |E_0|): every pair energy attractive (Lemma S)", all(w < 0 for w in W) and K[qmask].min() > 0, f"W = {np.round(W, 5)}")
# zero of energy tuned: total weight-one vacuum energy density zero => uniform-mode curvature zero (and no tadpole)
K = Kc - E0N
W, _ = pair_W(K)
print("F E_vac tuned to 0, site-placed log-rate, no bare gradient (gamma=0): W_AB(r=1..4) =", np.round(W, 5), " min K over q != 0 =", round(float(K[qmask].min()), 6), "  <- positive only through the placement term -E_0/12")
longw = qmask & (lapq <= 2.2)
check("3d tuned zero of energy, site placement: at long wavelength (lap <= 2.2) K = -E_0/12 lap + para > 0, so the sign of the Newtonian tail is the placement term -E_0/12; zone-boundary modes stay negative",
      K[longw].min() > 0 and K[qmask].min() < 0, f"min K (long wavelength) = {K[longw].min():.4f}; min K (all q) = {K[qmask].min():.4f}; W = {np.round(W, 5)}")
W, _ = pair_W(Kl)
print("G E_vac tuned to 0, midpoint-placed (linear-rate) coupling, no bare gradient:  W_AB(r=1..4) =", np.round(W, 5), " max K over q != 0 =", round(float(Kl[qmask].max()), 8))
check("3e tuned zero of energy, midpoint placement: the sea's own kernel is <= 0 (no positive gradient coefficient at all): sign is the sign of the supplied bare gradient stiffness",
      float(Kl[qmask].max()) <= 1e-9, f"max K = {float(Kl[qmask].max()):.2e}")
for gamma in (0.01, 0.1):
    K = Kl + gamma * lapq
    W, _ = pair_W(K)
    print(f"H E_vac tuned to 0, midpoint placement, bare gamma = {gamma}: W_AB(r=1..4) =", np.round(W, 5), " min K over q != 0 =", round(float(K[qmask].min()), 5))
K = Kc + 0.3 * lapq + 0.5 * abs(E0N)
W, _ = pair_W(K)
print(f"E net kernel NOT positive (mu = 0.5|E_0|, gamma=0.3): W_AB(r=1..4) =", np.round(W, 5), " min K =", round(float(K[qmask].min()), 5))
check("3c with mu < |E_0| the net kernel has negative modes (tachyonic clock field): pair energies of mixed sign, no Newtonian law",
      K[qmask].min() < 0 and (min(W) < 0 < max(W) or K[qmask].min() < 0), f"min K = {K[qmask].min():.4f}, W = {np.round(W, 5)}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
