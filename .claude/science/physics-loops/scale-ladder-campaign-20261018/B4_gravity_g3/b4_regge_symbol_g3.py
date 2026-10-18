#!/usr/bin/env python3
"""B4 / kernel 1: long-wavelength spin-2 symbol of the repo's 4D cubic-Coxeter (Kuhn) Regge Hessian.

Source objects (unchanged, imported read-only):
  scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py  (R4: bloch_Q,
  metric_map, gauge_map) -- the helper used by the 2026-09-03 Regge second-variation note's runner.

What is computed (floating point, finite samples; not exact-arithmetic certificates):
  G1  exact vertex-displacement (linearised diffeo) null directions of Q(k) at sampled real and
      complex momenta, incl. large |k|;
  G2  the 5 non-metric edge modes at k=0: 4 massive + 1 flat; leading O(k^2) symbol of
      (a) the restriction Q_h = M^+ Q M and (b) the Schur complement with the 4 massive
      non-metric modes integrated out (the low-energy effective metric form);
  G3  the symmetry group of the Kuhn triangulation acting on quadratic forms is S4 (coordinate
      permutations; global inversion acts trivially).  Count S4- and B4-invariant two-derivative
      forms and their gauge-invariant subspaces; decompose the extracted symbol;
  G4  TT dispersion (k_tau = i omega) along [100],[110],[111]: speeds^2 and polarisation degeneracy;
  G5  'g3' read off directly: O_h-type decomposition of the kinetic (k_tau^2) block on spatial h.
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, *[".."] * 5))
sys.path.insert(0, os.path.join(REPO, "scripts"))
sys.path.insert(0, HERE)

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4  # noqa: E402
from common_spin2 import (check_factory, eh_tensor, gauge_invariant_subspace,  # noqa: E402
                          gauge_variation_operator, hcomps, invariant_forms, matrix_symbol_to_tensor,
                          perm_matrices, tensor_to_matrix, tt_dispersion)

check, ST = check_factory()
t0 = time.time()
D = 4
HC = hcomps(D)
assert [tuple(x) for x in R4.HCOMPS] == HC, "HCOMP ordering mismatch"

# ------------------------------------------------------------------ G1 gauge null directions
print("== G1: exact linearised-diffeo null directions of the edge Hessian Q(k) ==")
rng = np.random.default_rng(20261018)
ks = [rng.uniform(-np.pi, np.pi, 4) for _ in range(12)] + [np.array([np.pi, np.pi, np.pi, np.pi]),
                                                         np.array([1e-3, 0, 0, 0])]
worst = 0.0
for k in ks:
    Q = R4.bloch_Q(k)
    G = R4.gauge_map(k)
    r = np.linalg.norm(Q @ G) / (np.linalg.norm(Q) * max(np.linalg.norm(G), 1e-300))
    worst = max(worst, r)
check("G1a vertex-displacement fields are null vectors of Q(k) at 14 real momenta (incl. random, "
      "zone corner, tiny)", worst < 1e-12, f"max relative residual {worst:.2e}")
# complex momentum: use the 09-03 note's holomorphic continuation (precomputed term lists)
try:
    import importlib
    RC = importlib.import_module("regge_4d_complex_native_linearised_graviton_dispersion_check_2026_09_03")
    worst_c = 0.0
    for kc in [np.array([0.3, -0.2, 0.5, 0.7j]), np.array([1.1, 0.4, 0.0, 1.3j]),
               np.array([0.2 + 0.1j, 0.0, 0.0, 0.9j])]:
        Qc = RC.Qan(kc)
        Gc = np.zeros((15, 4), complex)
        for ci, v in enumerate(R4.DIRS15):
            vv = np.array(v, float)
            Gc[ci, :] = (np.exp(1j * (kc @ vv)) - 1.0) * vv / np.linalg.norm(vv)
        worst_c = max(worst_c, np.linalg.norm(Qc @ Gc) / np.linalg.norm(Qc) / np.linalg.norm(Gc))
    check("G1b gauge null directions persist at complex (continued) momenta", worst_c < 1e-12,
          f"max relative residual {worst_c:.2e}")
except Exception as exc:  # pragma: no cover
    check("G1b complex-momentum gauge null directions", False, f"could not import continuation: {exc}")

# ------------------------------------------------------------------ G2 leading symbols
print("\n== G2: non-metric modes and the leading O(k^2) metric symbol ==")
M0 = R4.metric_map(np.zeros(4)).real
U, s, Vt = np.linalg.svd(M0, full_matrices=True)
Ncomp = U[:, 10:]                                   # 5 real non-metric directions at k=0
Q0 = R4.bloch_Q(np.zeros(4)).real
D0 = Ncomp.T @ Q0 @ Ncomp
w0, v0 = np.linalg.eigh(D0)
print("   non-metric block eigenvalues at k=0:", np.round(w0, 9))
flat = np.abs(w0) < 1e-9
check("G2a the 5 non-metric modes are 4 massive + 1 flat at k=0 (as the R4 inventory states)",
      flat.sum() == 1 and np.all(np.abs(w0[~flat]) > 1.0), f"eigenvalues {np.round(w0, 6)}")
Nm = Ncomp @ v0[:, ~flat]                           # 4 massive directions
nflat = Ncomp @ v0[:, flat][:, 0]


def S_restr(k):
    M = R4.metric_map(k)
    return M.conj().T @ R4.bloch_Q(k) @ M


def S_schur(k):
    M = R4.metric_map(k)
    Q = R4.bloch_Q(k)
    A = M.conj().T @ Q @ M
    B = M.conj().T @ Q @ Nm
    Dm = Nm.T @ Q @ Nm
    return A - B @ np.linalg.solve(Dm, B.conj().T)


def leading(Sfun, n, eps=2e-3):
    n = np.asarray(n, float)
    def even(x):
        return 0.5 * (Sfun(x * n) + Sfun(-x * n))
    X1 = even(eps) / eps ** 2
    X2 = even(2 * eps) / (2 * eps) ** 2
    return (4 * X1 - X2) / 3.0


# coupling order of massive modes to the metric
for nm_ in ([1, 0, 0, 0], [1, 1, 1, 1]):
    nn = np.array(nm_, float) / np.linalg.norm(nm_)
    cs = []
    for e in (1e-2, 2e-2):
        M = R4.metric_map(e * nn)
        cs.append(np.linalg.norm(M.conj().T @ R4.bloch_Q(e * nn) @ Nm))
    print(f"   |metric-massive coupling| along {nm_}: {cs[0]:.3e} at 0.01, {cs[1]:.3e} at 0.02 "
          f"(ratio {cs[1] / cs[0]:.3f}; 2 => O(k), 4 => O(k^2))")

T_restr = matrix_symbol_to_tensor(lambda n: leading(S_restr, n), D)
T_schur = matrix_symbol_to_tensor(lambda n: leading(S_schur, n), D)
for name, T in (("restricted Q_h", T_restr), ("Schur-complement", T_schur)):
    im = np.abs(T.imag).max() / np.abs(T.real).max()
    print(f"   {name}: max|Im|/max|Re| of O(k^2) tensor = {im:.2e}")
T_restr = T_restr.real
T_schur = T_schur.real

# exact-quadraticity of the extracted leading symbol on random directions
dev = 0.0
for _ in range(6):
    n = rng.normal(size=4)
    S2 = leading(S_schur, n).real
    dev = max(dev, np.abs(S2 - tensor_to_matrix(T_schur, n, D)).max() / np.abs(S2).max())
check("G2b extracted O(k^2) Schur symbol is reproduced by the polarisation tensor on 6 random "
      "directions", dev < 1e-6, f"max relative deviation {dev:.2e}")

# ------------------------------------------------------------------ G3 invariant decomposition
print("\n== G3: symmetry-allowed forms and decomposition ==")
B_S4 = invariant_forms(D, perm_matrices(D, signed=False))
G_S4 = gauge_invariant_subspace(B_S4, D)
B_B4 = invariant_forms(D, perm_matrices(D, signed=True))
G_B4 = gauge_invariant_subspace(B_B4, D)
print(f"   S4 (perm-only) invariant forms: {B_S4.shape[1]}, gauge-invariant: {G_S4.shape[1]}")
print(f"   B4 (signed perms) invariant forms: {B_B4.shape[1]}, gauge-invariant: {G_B4.shape[1]}")
check("G3a counts: B4 -> 9 forms, 1 gauge-invariant (reproduces probe P-G1); S4 -> 2 gauge-invariant",
      B_B4.shape[1] == 9 and G_B4.shape[1] == 1 and G_S4.shape[1] == 2)

EH = eh_tensor(D)
EHn = EH / np.linalg.norm(EH)
# the second S4 gauge-invariant direction: is it d/dc EH(g0 = I + c(J - I))?
J = np.ones((4, 4))
dc = 1e-4
tilt = (eh_tensor(D, np.eye(4) + dc * (J - np.eye(4))) - eh_tensor(D, np.eye(4) - dc * (J - np.eye(4)))) / (2 * dc)
span = np.column_stack([EH, tilt])
resid = G_S4 - span @ np.linalg.lstsq(span, G_S4, rcond=None)[0]
check("G3b the two S4 gauge-invariant forms are spanned by EH(delta) and d/dc EH(I + c(J-I)) "
      "(a 'tilted background metric' -- one common cone, no birefringence)",
      np.abs(resid).max() < 1e-6, f"residual {np.abs(resid).max():.1e}")

ratios = []
worst_in = 0.0
for cval in (-0.3, -0.2, -0.1, 0.1, 0.3, 0.6, 0.9):
    Eg = eh_tensor(D, np.eye(4) + cval * (J - np.eye(4)))
    co = np.linalg.lstsq(span, Eg, rcond=None)[0]
    worst_in = max(worst_in, np.linalg.norm(Eg - span @ co) / np.linalg.norm(Eg))
    ratios.append((cval, co[1] / co[0]))
print("   tilt/EH coefficient ratio of EH[I + c(J-I)]:", [(c_, round(r_, 4)) for c_, r_ in ratios])
check("G3b' EH[I + c(J-I)] lies in the 2-dim S4 gauge-invariant space for finite c (so the whole space is the "
      "cone of 'EH of some S4-invariant background metric': every S4+gauge-invariant leading form in the "
      "covered ratio range has ONE cone for both TT polarisations)",
      worst_in < 1e-9 and all(np.diff([r_ for _, r_ in ratios]) > 0),
      f"max residual {worst_in:.1e}; ratio monotone in c over c in [-0.3, 0.9]")

gv = gauge_variation_operator(D)
for name, T in (("restricted", T_restr), ("Schur", T_schur)):
    var = np.abs(gv(T[:, None])).max() / np.abs(T).max()
    print(f"   gauge variation of extracted {name} O(k^2) tensor (relative): {var:.2e}")
    coef = np.linalg.lstsq(span, T, rcond=None)[0]
    res = np.linalg.norm(T - span @ coef) / np.linalg.norm(T)
    c_eh = (T @ EH) / (EH @ EH)
    res_eh = np.linalg.norm(T - c_eh * EH) / np.linalg.norm(T)
    print(f"   {name}: T = {coef[0]:+.10f} EH + {coef[1]:+.3e} tilt ; residual outside span {res:.2e}; "
          f"pure-EH residual {res_eh:.2e}")
    if name == "Schur":
        c_schur, res_schur, tilt_schur = c_eh, res_eh, coef[1]
    else:
        c_restr, res_restr = c_eh, res_eh
check("G3c effective (Schur) O(k^2) symbol = c * linearised EH, with zero tilt and zero non-gauge "
      "B4/S4 admixture to numerical precision", res_schur < 1e-7 and abs(tilt_schur) < 1e-6 * abs(c_schur),
      f"c = {c_schur:+.10f}; relative residual {res_schur:.2e}")
check("G3d restricted Q_h O(k^2) symbol = c * linearised EH as well (note's T4 / R4 comparator)",
      res_restr < 1e-7, f"c = {c_restr:+.10f}; relative residual {res_restr:.2e}; "
      f"Schur/restricted ratio {c_schur / c_restr:.10f}")

# ------------------------------------------------------------------ G4 TT dispersion
print("\n== G4: TT dispersion of the extracted Schur symbol (tau = axis 3, k_tau = i omega) ==")
speeds = {}
for name, nv in (("[100]", (1, 0, 0)), ("[110]", (1, 1, 0)), ("[111]", (1, 1, 1))):
    r = tt_dispersion(T_schur, D, nv)
    print(f"   {name}: (omega^2/k^2, sign omega, multiplicity, rel sigma_min) = "
          f"{[(round(a, 12), b, c, float('%.1e' % d_)) for a, b, c, d_ in r]}")
    speeds[name] = r
ok = all(len(r) == 2 and all(abs(a - 1) < 1e-8 and m == 2 for a, _, m, _ in r) for r in speeds.values())
check("G4a both TT polarisations have omega^2/k^2 = 1 (multiplicity 2, both signs of omega) along "
      "[100],[110],[111]: no leading-order birefringence", ok)
# axis-choice robustness: time = axis 0 instead of 3 (S4 symmetry)
r0 = tt_dispersion(T_schur, D, (1, 1, 1), tau=0)
check("G4b same result with the tick placed on axis 0 (S4 relabelling)",
      len(r0) == 2 and all(abs(a - 1) < 1e-8 and m == 2 for a, _, m, _ in r0))
# positive control: EH of a rescaled background g0 = diag(1,1,1,1.1) (gauge invariant, one cone with
# omega^2/k^2 = 1.1).  (A tilt admixture is NOT a usable control on a real-omega scan: its cone has
# complex omega at real spatial k.)
Tc = eh_tensor(D, np.diag([1.0, 1.0, 1.0, 1.1]))
rc = tt_dispersion(Tc, D, (1, 1, 1))
print("   control g0 = diag(1,1,1,1.1) [111]:", [(round(a, 9), b, c) for a, b, c, _ in rc])
check("G4c positive control: solver returns omega^2/k^2 = 1.1 (multiplicity 2) for EH of a rescaled "
      "background", len(rc) == 2 and all(abs(a - 1.1) < 1e-8 and m == 2 for a, _, m, _ in rc))

# ------------------------------------------------------------------ G5 g3 read off directly
print("\n== G5: O_h decomposition of the kinetic (k_tau^2) block on spatial metric components ==")
Kfull = tensor_to_matrix(T_schur, np.array([0, 0, 0, 1.0]), D)
sp_idx = [I for I, (a, b) in enumerate(HC) if a != 3 and b != 3]
hc3 = [HC[I] for I in sp_idx]
Kh = Kfull[np.ix_(sp_idx, sp_idx)]
# orthonormal coordinates q_ii = h_ii, q_ij = sqrt2 h_ij  (h^T K h = q^T Kq q)
sc = np.array([1.0 if a == b else 1 / np.sqrt(2) for a, b in hc3])
Kq = (sc[:, None] * Kh * sc[None, :])
I6 = np.eye(6)
TR = np.zeros((6, 6))
DG = np.zeros((6, 6))
for i, (a, b) in enumerate(hc3):
    for j, (c, d_) in enumerate(hc3):
        TR[i, j] = float(a == b) * float(c == d_)
        DG[i, j] = float(a == b and c == d_ and a == c)
basis = np.column_stack([I6.ravel(), TR.ravel(), DG.ravel()])
g, *_ = np.linalg.lstsq(basis, Kq.ravel(), rcond=None)
res = np.linalg.norm(Kq.ravel() - basis @ g) / np.linalg.norm(Kq)
print(f"   kinetic block = g1*Id + g2*tr(x)tr + g3*sum_i E_ii^2 with (g1,g2,g3) = "
      f"({g[0]:+.10f}, {g[1]:+.10f}, {g[2]:+.3e}); residual {res:.1e}")
print(f"   g2/g1 = {g[1] / g[0]:+.10f} (DeWitt lambda=1 kinetic: -1),  g3/g1 = {g[2] / g[0]:+.2e}")
check("G5a kinetic block is O(3)-form (g3/g1 = 0 to numerical precision) with DeWitt ratio g2/g1 = -1",
      abs(g[2] / g[0]) < 1e-7 and abs(g[1] / g[0] + 1) < 1e-7 and res < 1e-7)
lapse_shift = Kfull[np.ix_([I for I in range(10) if I not in sp_idx], range(10))]
check("G5b lapse/shift rows of the kinetic block vanish (multiplier structure)",
      np.abs(lapse_shift).max() < 1e-7 * np.abs(Kh).max(), f"max {np.abs(lapse_shift).max():.1e}")

print(f"\nruntime {time.time() - t0:.1f}s")
print(f"TOTAL: PASS={ST['PASS']} FAIL={ST['FAIL']}")
