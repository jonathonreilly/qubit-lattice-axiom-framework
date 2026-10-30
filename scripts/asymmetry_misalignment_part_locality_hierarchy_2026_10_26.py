#!/usr/bin/env python3
"""Test C (pre-registered): hierarchy from cell-locality of the mass vertex on X-node families, and its
compatibility with the CP misalignment of Test B.
X-family Yukawa from a 2x2x2-cell-periodic on-site vertex profile f(c), c in {0,1}^3:
  Y_ab = sum_c f(c) exp(i (X_a + X_b).c)  =  sum_c f(c) s(c)_a s(c)_b,   s(c)_a = (-1)^{c_a}."""
import itertools, numpy as np
rng = np.random.default_rng(424242)
cells = [np.array(c) for c in itertools.product((0, 1), repeat=3)]
S = {tuple(c): np.array([(-1) ** c[a] for a in range(3)], float) for c in cells}
def Y_of(f): return sum(f[tuple(c)] * np.outer(S[tuple(c)], S[tuple(c)]) for c in cells)
def sv(Y): return np.linalg.svd(Y, compute_uv=False)
# C1
site = {tuple(c): (1.0 if not c.any() else 0.0) for c in cells}; unif = {tuple(c): 1.0 for c in cells}
s_site, s_unif = sv(Y_of(site)), sv(Y_of(unif))
C1 = s_site[1] / s_site[0] < 1e-12 and np.allclose(s_unif, s_unif[0])
print(f"C1: single-site vertex singular values {np.round(s_site, 6)}; uniform vertex {np.round(s_unif, 6)} -> {'PASS' if C1 else 'FAIL'}")
# C2, C3: random local profiles eps^|c| * N(0,1)
def stats(gen, N=4000):
    r12, r23 = [], []
    for _ in range(N):
        s = sv(Y_of(gen())); r12.append(s[0] / s[1]); r23.append(s[1] / max(s[2], 1e-300))
    return np.median(r12), np.median(r23)
eps = 0.1
loc = lambda: {tuple(c): eps ** c.sum() * rng.normal() for c in cells}
nonloc = lambda: {tuple(c): rng.normal() for c in cells}
def aniso():
    e = rng.uniform(0.01, 0.3, 3)
    return {tuple(c): np.prod(e ** c) * rng.normal() for c in cells}
m12, m23 = stats(loc); n12, n23 = stats(nonloc); a12, a23 = stats(aniso)
print(f"C2/C3: local eps^|c| profiles: median s1/s2 {m12:.1f}, s2/s3 {m23:.2f}")
print(f"       control non-local iid profiles: median s1/s2 {n12:.2f}, s2/s3 {n23:.2f}")
print(f"       anisotropic local profiles (eps_i in (0.01,0.3)): median s1/s2 {a12:.1f}, s2/s3 {a23:.2f}")
print(f"C2 {'PASS' if m12 >= 10 else 'FAIL'}  C3 {'PASS' if m23 >= 10 else 'FAIL'}")
# data comparison (cited running masses at M_Z, Xing-Zhang-Zhou 2008): s2/s3 = m2/m1
data = {'up': (0.00138, 0.638, 172.1), 'down': (0.00282, 0.057, 2.86), 'lepton': (0.000487, 0.1027, 1.746)}
print("       measured m3/m2, m2/m1:", {k: (round(v[2] / v[1], 1), round(v[1] / v[0], 1)) for k, v in data.items()})
# C4 compatibility: is the democratic rank-1 term s s^T (all |s_a| = 1) invariant under T*g for a real non-scalar F(g)?
_nsA = {'__file__': __file__, '__name__': 'partA'}
import contextlib as _cl, io as _io
with _cl.redirect_stdout(_io.StringIO()):
    exec(compile(__import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_slab_family_characters_2026_10_26.py').read_text(), 'partA', 'exec'), _nsA)
famN = _nsA['famN']
Fs = {g: F for g, F in famN.items() if g != 'C3(111)'}
Fs.update({'tau_x': np.diag([-1, 1, 1.]), 'tau_y': np.diag([1, -1, 1.]), 'tau_z': np.diag([1, 1, -1.])})
ok = []
for g, F in Fs.items():
    if np.allclose(F, F[0, 0] * np.eye(3)): continue
    for c in cells:
        s = S[tuple(c)]; M = np.outer(s, s)
        ok.append(np.allclose(F.T @ M.conj() @ F, M) or np.allclose(F.T @ (1j * M).conj() @ F, 1j * M))
C4 = any(ok)
print(f"C4: democratic rank-1 term invariant under some non-scalar real T*g: {C4} -> {'PASS' if C4 else 'FAIL'}")
# escape check (reported, not pre-registered): rank-1 along a face diagonal from a bond vertex
v = np.array([1, 1, 0.]); M = np.outer(v, v); F = np.diag([1, 1, -1.])
print(f"  (post hoc) face-diagonal rank-1 (1,1,0)(1,1,0)^T invariant under T*C2z-type F=diag(1,1,-1): {np.allclose(F.T @ M @ F, M)}")
