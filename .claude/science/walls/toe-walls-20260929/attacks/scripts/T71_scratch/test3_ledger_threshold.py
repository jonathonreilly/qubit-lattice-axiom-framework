#!/usr/bin/env python3
"""T71 test 3 (final): Lemma S on the member's ledger (b55).  Net static kernel K(q) = K_bare(q) + c(q) from the walker sea.
Total interaction energy of a source distribution J (mean removed) at the stationary point: W[J] = -(1/2) J K^{-1} J.
Lemma S: K > 0 on the sources' modes  =>  W[J] < 0 for every J (binding); K < 0 on some mode => some J has W > 0.
(Individual pair terms at lattice separations need not share the sign: shown, not asserted.)
First-run note: my first version of check 3b assumed a uniform stiffness mu = 1.05 |E_0| suffices; it FAILED at gamma = 0.05
because the axis zone-boundary mode has c_u = -1.593 < E_0.  The record is test3_output_run1_first_criteria.txt.
"""
import itertools
import sys
import numpy as np
from test2_sea_rate_hessian import build_H, sea_energy, curvature, lat_lap

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


L = 8
E0 = sea_energy(build_H(L, [np.ones((L, L, L))] * 3))
E0N = E0 / L ** 3
orb, orbl = {}, {}
for m in itertools.product(range(L // 2 + 1), repeat=3):
    key = tuple(sorted(m))
    if key == (0, 0, 0) or key in orb:
        continue
    orb[key] = curvature(L, 'phiHphi', key, E0=E0)[0]
    orbl[key] = curvature(L, 'lapse', key, E0=E0)[0]
Kc = np.zeros((L, L, L)); Kl = np.zeros((L, L, L)); lapq = np.zeros((L, L, L))
for m in itertools.product(range(L), repeat=3):
    key = tuple(sorted(min(mi, L - mi) for mi in m))
    lapq[m] = lat_lap(m, L)
    Kc[m] = E0N if key == (0, 0, 0) else orb[key]
    Kl[m] = 0.0 if key == (0, 0, 0) else orbl[key]
qm = np.ones((L, L, L), bool); qm[0, 0, 0] = False
print(f"L={L}: E0/N = {E0N:.5f}; c_u ranges over q != 0: [{Kc[qm].min():.4f}, {Kc[qm].max():.2e}]")


def Wtot(K, J):
    Jq = np.fft.fftn(J)
    val = 0.0
    nz = qm & (np.abs(K) > 1e-9)
    val = -0.5 * np.sum(np.abs(Jq[nz]) ** 2 / K[nz]) / J.size
    return val


rng = np.random.default_rng(1)
Js = [rng.normal(size=(L, L, L)) for _ in range(300)]
for J in Js:
    J -= J.mean()
Wsea = [Wtot(Kc, J) for J in Js]
check("3a sea alone (log-rate, site placement): K <= 0 on every q != 0, so every source distribution has W > 0 (no binding)",
      Kc[qm].max() <= 1e-9 and min(Wsea) > 0, f"max c_u = {Kc[qm].max():.1e}; min over 300 random J of W = {min(Wsea):.3f}")

print("       pair terms of the sea-only kernel, W_AB(r=1..4) = -J^2 G(r):", end=" ")
Kinv = np.zeros_like(Kc); nz = qm & (np.abs(Kc) > 1e-9); Kinv[nz] = 1 / Kc[nz]
G = np.real(np.fft.ifftn(Kinv)); print(np.round([-G[r, 0, 0] for r in range(1, 5)], 4), "(alternating signs)")

# uniform stiffness needed (curvature of the uniform mode = total weight-one vacuum energy density)
for gamma in (0.0, 0.05, 0.3):
    mu_min = max(-(Kc[m] + gamma * lapq[m]) for m in itertools.product(range(L), repeat=3) if m != (0, 0, 0))
    print(f"       gamma = {gamma}: uniform stiffness mu needed for K > 0 on all q != 0: {mu_min:.4f} = {mu_min / abs(E0N):.3f} |E_0|")
    K = Kc + gamma * lapq + 1.02 * mu_min
    Wb = [Wtot(K, J) for J in Js]
    K2 = Kc + gamma * lapq + 0.9 * mu_min
    # worst mode of the deficient kernel: a plane wave sitting on it is the source distribution that unbinds
    worst = np.unravel_index(np.argmin(np.where(qm, K2, np.inf)), K2.shape)
    xg = np.arange(L)
    XX, YY, ZZ = np.meshgrid(xg, xg, xg, indexing='ij')
    Jbad = np.cos(2 * np.pi * (worst[0] * XX + worst[1] * YY + worst[2] * ZZ) / L)
    Wgood_plane = Wtot(K, Jbad)
    Wbad_plane = Wtot(K2, Jbad)
    check(f"3b gamma={gamma}: with mu = 1.02 mu_min every source distribution tested binds (W < 0, 300 random J and the worst-mode plane wave); with mu = 0.9 mu_min the plane wave on the worst mode has W > 0",
          max(Wb) < 0 and Wgood_plane < 0 and Wbad_plane > 0, f"max random W {max(Wb):.3f}; plane wave {tuple(int(w) for w in worst)}: W = {Wgood_plane:.3f} at 1.02 mu_min, {Wbad_plane:.3f} at 0.9 mu_min")
    if gamma == 0.05:
        Kinv = np.zeros_like(K); nz = qm & (np.abs(K) > 1e-9); Kinv[nz] = 1 / K[nz]
        G = np.real(np.fft.ifftn(Kinv))
        print("       pair terms at mu = 1.02 mu_min, gamma = 0.05: W_AB(r=1..4) =", np.round([-G[r, 0, 0] for r in range(1, 5)], 4))

# long-wavelength sign after the zero of energy is tuned (uniform mode removed): who supplies the gradient stiffness?
long_ = qm & (lapq <= 2.2)
Kt = Kc - E0N
check("3c zero of energy tuned, site placement: long-wavelength K = -E_0/12 lap + (para <= 0) > 0, but zone-boundary modes are negative",
      Kt[long_].min() > 0 and Kt[qm].min() < 0, f"min K (lap <= 2.2) = {Kt[long_].min():.4f}; min over all q = {Kt[qm].min():.4f}")
ratio = np.array([Kt[m] / lapq[m] for m in itertools.product(range(L), repeat=3) if long_[m]])
print(f"       K/lap at long wavelength (site placement): {ratio.min():.4f} .. {ratio.max():.4f}; -E_0/12 = {-E0N / 12:.4f}")
check("3d zero of energy tuned, midpoint placement (linear-rate coupling): the sea's own kernel is <= 0 for all q, so any positive gradient stiffness must be supplied",
      Kl[qm].max() <= 1e-9, f"max K = {Kl[qm].max():.1e}; K/lap ranges {min(Kl[m] / lapq[m] for m in itertools.product(range(L), repeat=3) if qm[m] and lapq[m] > 0):.4f} .. 0")
gam_min = max(-Kl[m] / lapq[m] for m in itertools.product(range(L), repeat=3) if qm[m] and lapq[m] > 0)
print(f"       bare gradient stiffness gamma needed to make K > 0 on this torus: {gam_min:.4f} (set by zone-boundary modes; long-wavelength modes need only gamma q^2 > |c| ~ q^4); "
      f"the sign of the Newtonian tail is then the sign of the supplied gamma")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
