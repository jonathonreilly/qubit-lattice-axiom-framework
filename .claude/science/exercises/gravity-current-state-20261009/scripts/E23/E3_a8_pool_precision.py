"""E3 (a8): pooled quasicrystal mean from the E3_a4 patches (buffer 2.5, truncation bias ~1e-6 per E3_a4_check).
Per patch: interior mean per direction; pooled mean per channel with SE from the patch-to-patch spread."""
import numpy as np, glob
import e23_core as c
for R in ['1.8', '2.2']:
    fs = sorted(glob.glob(f"E3_a4_R{R}_*.npz")); M = []; S1 = []
    for f in fs:
        d = np.load(f); X, e2, e1 = d['X'], d['e2'], d['e1']; m = np.linalg.norm(X, axis=1) < 9.0 - 2.5
        M.append(e2[m].mean(0)); S1.append(e1[m].mean(0))
    M = np.array(M); S1 = np.array(S1)
    iso = M.mean(1)                 # icosahedral: all 5 directions estimate the same number
    print(f"R={R}: {len(fs)} patches, ~{m.sum()} interior sites each | isotropic mean {iso.mean():+.5f} +- {iso.std(ddof=1)/np.sqrt(len(iso)):.5f}"
          f" | E_g {M[:, c.CH['E_g']].mean():+.5f} +- {M[:, c.CH['E_g']].mean(1).std(ddof=1)/np.sqrt(len(iso)):.5f}"
          f" | T_2g {M[:, c.CH['T_2g']].mean():+.5f} +- {M[:, c.CH['T_2g']].mean(1).std(ddof=1)/np.sqrt(len(iso)):.5f}"
          f" | stress mean {S1.mean():+.1e} +- {S1.mean(1).std(ddof=1)/np.sqrt(len(iso)):.1e}")

print("\nnoise of n-site interior averages (patch to patch), per direction, vs independent-site expectation:")
for R in ['1.8', '2.2']:
    fs = sorted(glob.glob(f"E3_a4_R{R}_*.npz")); M, S1, ps, pt, ns = [], [], [], [], []
    for f in fs:
        d = np.load(f); X, e2, e1 = d['X'], d['e2'], d['e1']; m = np.linalg.norm(X, axis=1) < 6.5
        M.append(e2[m].mean(0)); S1.append(e1[m].mean(0)); ps.append(e2[m].std(0)); pt.append(e1[m].std(0)); ns.append(m.sum())
    M, S1, ps, pt, n = np.array(M), np.array(S1), np.array(ps).mean(), np.array(pt).mean(), np.mean(ns)
    sdM = (M - M.mean(0)).std(ddof=1); sdS = (S1 - S1.mean(0)).std(ddof=1)
    print(f"R={R}: n={n:.0f}  stiffness: patch sd {sdM:.2e} vs per-site sd/sqrt(n) {ps/np.sqrt(n):.2e} (ratio {sdM/(ps/np.sqrt(n)):.2f});"
          f" vs Poisson white level 0.067/sqrt(n) {0.067/np.sqrt(n):.2e}  |  stress: patch sd {sdS:.2e} vs {pt/np.sqrt(n):.2e} (ratio {sdS/(pt/np.sqrt(n)):.2f})")
