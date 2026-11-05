#!/usr/bin/env python3
"""Test B (pre-registered): sector misalignment of residual antiunitaries.
Up sector keeps Theta_u = T*g_u, down sector keeps Theta_d = T*g_d; Q, u^c, d^c are X-node family triplets on which
g acts by the family matrix F(g) (from Test A, spin-statistics normalised) and T acts as K (family part 1).
Invariance of a Yukawa Y (Q_a Y_ab q^c_b) under T*g: Y = F^T Y^* F (real-linear constraint).
theta_bar = theta_QCD - arg det Yu - arg det Yd, with theta_QCD fixed by T*g_u invariance of the gauge sector:
theta_QCD = 2 arg det F(g_u) (mod pi) [anomaly of F on 4 coloured Weyl triplets per family: Q twice, u^c, d^c]."""
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
def run(name, Fu, Fd, N=2000):
    th = []; J = []
    thq = 2 * np.angle(np.linalg.det(Fu))                         # theta_QCD (mod pi) fixed by T*g_u
    cons = wrap_pi(2 * np.angle(np.linalg.det(Fu)) - 2 * np.angle(np.linalg.det(Fd)))
    for _ in range(N):
        Yu, Yd = sample(Fu), sample(Fd)
        th.append(wrap_pi(thq - np.angle(np.linalg.det(Yu)) - np.angle(np.linalg.det(Yd))))
        J.append(abs(jarlskog(Yu, Yd)) / Jmax)
    th = np.abs(np.array(th)); J = np.array(J)
    print(f"  {name}: dims(inv space) up {len(invariant_basis(Fu))}, down {len(invariant_basis(Fd))}; consistency {cons:+.1e}; "
          f"max|sin theta_bar| {np.max(np.abs(np.sin(th))):.1e}; median |J|/Jmax {np.median(J):.2e}; max {np.max(J):.2e}")
    return th, J
print("== B1 misaligned sectors (pre-registered pass: |sin theta| < 1e-10 in 100%, median |J|/Jmax > 1e-2)")
b1 = []
for gu, gd in (('tau_x', '1'), ('C2x', 'C2y'), ('tau_x', 'tau_y'), ('C2z', '1')):
    th, J = run(f"up keeps T*{gu}, down keeps T*{gd}", fam[gu], fam[gd]); b1.append(np.max(np.abs(np.sin(th))) < 1e-10 and np.median(J) > 1e-2)
print("B1 PASS" if all(b1) else f"B1 FAIL {b1}")
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
