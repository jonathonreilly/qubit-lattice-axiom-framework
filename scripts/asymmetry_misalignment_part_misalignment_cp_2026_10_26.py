#!/usr/bin/env python3
"""Test B (pre-registered): sector misalignment of residual antiunitaries.
Up sector keeps Theta_u = T*g_u, down sector keeps Theta_d = T*g_d; Q, u^c, d^c are X-node family triplets on which
g acts by the family matrix F(g) (from Test A, spin-statistics normalised) and T acts as K (family part 1).
Invariance of a Yukawa Y (Q_a Y_ab q^c_b) under T*g: Y = F^T Y^* F (real-linear constraint).
theta_bar = theta_QCD - arg det Yu - arg det Yd, with theta_QCD fixed by T*g_u invariance of the gauge sector:
theta_QCD = 2 arg det F(g_u) (mod pi) [anomaly of F on 4 coloured Weyl triplets per family: Q twice, u^c, d^c].
2026-11-14 repair (PR 10129 hold, finding 2): the residual constraints fix theta_bar_tree only modulo pi. Y -> -Y keeps
every constraint (it is real-linear and homogeneous) and shifts arg det Y by pi, and theta_QCD itself is fixed only mod pi.
So the result is theta_bar_tree in {0, pi} with the sign branch not selected. The census below takes theta_QCD =
2 arg det F(g_u) mod 2 pi and reports both branches of arg det(Yu Yd); the explicit witness is printed (B5)."""
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ("scripts/asymmetry_misalignment_part_slab_family_characters_2026_10_26.py",)
import numpy as np
rng = np.random.default_rng(20261025)
_nsA = {'__file__': __file__, '__name__': 'partA'}
import contextlib as _cl, io as _io
with _cl.redirect_stdout(_io.StringIO()):
    exec(compile(__import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_slab_family_characters_2026_10_26.py').read_text(), 'partA', 'exec'), _nsA)
famN = _nsA['famN']
I3 = np.eye(3, dtype=complex)
fam = {'1': I3, **{k: v for k, v in famN.items() if k != 'C3(111)'}}
def invariant_basis(F):
    # real basis of {Y : Y = F^T conj(Y) F}; Y = A + iB, unknown vector (A, B) in R^18
    rows = []
    for idx in range(18):
        e = np.zeros(18); e[idx] = 1
        Y = (e[:9] + 1j * e[9:]).reshape(3, 3)
        Rm = Y - F.T @ Y.conj() @ F
        rows.append(np.concatenate([Rm.real.ravel(), Rm.imag.ravel()]))
    Mx = np.array(rows).T            # columns = images of basis vectors (18 x 18, real)
    u, s, vh = np.linalg.svd(Mx); null = vh[s < 1e-10]
    return [(v[:9] + 1j * v[9:]).reshape(3, 3) for v in null]
def sample(F):
    B = invariant_basis(F); c = rng.normal(size=len(B)); return sum(ci * Bi for ci, Bi in zip(c, B))
Jmax = 1 / (6 * np.sqrt(3))
def jarlskog(Yu, Yd):
    Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
    mu = np.linalg.eigvalsh(Hu); md = np.linalg.eigvalsh(Hd)
    den = np.prod([mu[j] - mu[i] for i in range(3) for j in range(i + 1, 3)]) * np.prod([md[j] - md[i] for i in range(3) for j in range(i + 1, 3)])
    return (np.linalg.det(Hu @ Hd - Hd @ Hu) / (2j * den)).real
def wrap_pi(x): return (x + np.pi / 2) % np.pi - np.pi / 2        # theta_bar mod pi
def wrap_2pi(x): return (x + np.pi) % (2 * np.pi) - np.pi        # theta_bar mod 2 pi, in [-pi, pi)
def resid(Y, F): return np.abs(Y - F.T @ Y.conj() @ F).max()
BR = {}
def run(name, Fu, Fd, N=2000):
    th = []; J = []; full = []; flips = 0; worst = 0.0
    thq = 2 * np.angle(np.linalg.det(Fu))                         # theta_QCD (mod pi) fixed by T*g_u
    cons = wrap_pi(2 * np.angle(np.linalg.det(Fu)) - 2 * np.angle(np.linalg.det(Fd)))
    for i in range(N):
        Yu, Yd = sample(Fu), sample(Fd)
        t2 = wrap_2pi(thq - np.angle(np.linalg.det(Yu)) - np.angle(np.linalg.det(Yd)))
        th.append(wrap_pi(t2)); full.append(t2)
        J.append(abs(jarlskog(Yu, Yd)) / Jmax)
        if i < 50:                                                # Y_u -> -Y_u: constraint kept, branch flipped
            t2f = wrap_2pi(thq - np.angle(np.linalg.det(-Yu)) - np.angle(np.linalg.det(Yd)))
            worst = max(worst, resid(-Yu, Fu)); flips += (abs(t2) < np.pi / 2) != (abs(t2f) < np.pi / 2)
    th = np.abs(np.array(th)); J = np.array(J); full = np.array(full)
    npi = int(np.sum(np.abs(full) > np.pi / 2))
    BR[name] = (npi, N, flips, worst)
    print(f"  {name}: dims(inv space) up {len(invariant_basis(Fu))}, down {len(invariant_basis(Fd))}; consistency {cons:+.1e}; "
          f"max|sin theta_bar| {np.max(np.abs(np.sin(th))):.1e}; median |J|/Jmax {np.median(J):.2e}; max {np.max(J):.2e}; "
          f"branch theta_bar = pi in {npi} of {N}; Y_u -> -Y_u flips the branch in {flips} of 50 (residual {worst:.0e})")
    return th, J
print("== B1 misaligned sectors (pre-registered pass: |sin theta| < 1e-10 in 100%, median |J|/Jmax > 1e-2)")
b1 = []
for gu, gd in (('tau_x', '1'), ('C2x', 'C2y'), ('tau_x', 'tau_y'), ('C2z', '1')):
    th, J = run(f"up keeps T*{gu}, down keeps T*{gd}", fam[gu], fam[gd]); b1.append(np.max(np.abs(np.sin(th))) < 1e-10 and np.median(J) > 1e-2)
print("B1 PASS" if all(b1) else f"B1 FAIL {b1}")
b1s = [0 < BR[k][0] < BR[k][1] and BR[k][2] == 50 and BR[k][3] < 1e-10 for k in BR]
print("B1s branch census: in every misaligned pair both theta_bar = 0 and theta_bar = pi occur, and Y_u -> -Y_u keeps the "
      "residual constraint and flips the branch, so the residuals fix theta_bar_tree only in {0, pi}: " + ("B1s PASS" if all(b1s) else f"B1s FAIL {b1s}"))
# B5 explicit witness (hold, finding 2): F_u = tau_x = diag(-1,1,1), F_d = 1, Y_u = diag(-1,2,3), Y_d = diag(4,5,6)
Fw, Yuw, Ydw = fam['tau_x'], np.diag([-1.0, 2, 3]).astype(complex), np.diag([4.0, 5, 6]).astype(complex)
thw = wrap_2pi(2 * np.angle(np.linalg.det(Fw)) - np.angle(np.linalg.det(Yuw)) - np.angle(np.linalg.det(Ydw)))
okw = np.allclose(Fw, np.diag([-1, 1, 1])) and resid(Yuw, Fw) < 1e-12 and resid(Ydw, I3) < 1e-12 and abs(abs(thw) - np.pi) < 1e-12
print(f"B5 witness: F_u = diag(-1,1,1), F_d = 1, Y_u = diag(-1,2,3), Y_d = diag(4,5,6): residuals {resid(Yuw, Fw):.0e}, "
      f"{resid(Ydw, I3):.0e}; 2 arg det F_u = {2 * np.angle(np.linalg.det(Fw)):.4f}; theta_bar = {abs(thw):.6f} (pi): "
      + ("B5 PASS" if okw else "B5 FAIL"))
print("== B2 control: aligned residual antiunitaries (must give J = 0)")
b2 = []
for g in ('1', 'tau_x', 'C2x'):
    th, J = run(f"both keep T*{g}", fam[g], fam[g], N=500); b2.append(np.max(J) * Jmax < 1e-13)
print("B2 PASS" if all(b2) else f"B2 FAIL {b2}")
print("== B3 control: no residual antiunitary (generic complex Yukawas)")
th = []
for _ in range(2000):
    Yu = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Yd = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    th.append(wrap_pi(-np.angle(np.linalg.det(Yu)) - np.angle(np.linalg.det(Yd))))
fr = np.mean(np.abs(np.sin(th)) < 1e-6); print(f"  fraction |sin theta_bar| < 1e-6: {fr:.4f}"); print("B3 PASS" if fr < 0.005 else "B3 FAIL")
print("== B4 genericity of the theta protection: det F(g_rel) must be real (+-1)")
def haar(n):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); q, r = np.linalg.qr(z); return q * (np.diag(r) / abs(np.diag(r)))
safe_haar = np.mean([abs(np.sin(np.angle(np.linalg.det(haar(3))))) < 1e-8 for _ in range(20000)])
w = np.exp(2j * np.pi / 3)
safe_z3 = abs(np.sin(np.angle(np.linalg.det(np.diag([1, w, w * w]))))) < 1e-8
safe_inc = np.mean([abs(np.sin(np.angle(np.prod(np.exp(1j * rng.uniform(0, 2 * np.pi, 3)))))) < 1e-8 for _ in range(20000)])
lattice = {g: np.round(np.linalg.det(F), 6) for g, F in fam.items()}
print(f"  Haar U(3) relative action theta-safe fraction {safe_haar:.4f}; Z3 characters (1,w,w^2) safe {safe_z3}; random incommensurate characters safe {safe_inc:.4f}")
print(f"  lattice family actions det: {lattice}")
print("B4 PASS" if (safe_haar < 0.005 and safe_z3 and safe_inc < 0.005) else "B4 FAIL")
