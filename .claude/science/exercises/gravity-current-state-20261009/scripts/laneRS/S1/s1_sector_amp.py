"""d=2, m>0: sector-resolved same-sector ++ amplitude.  Sector = eigenvalue of the exact
symmetry S1S2 on D_+(k); label s = lambda * exp(-i(k_x+k_y)) (cover labelling, consistent
because k4 = k1+k2-k3 exactly).  Checks that (a,a)->(a,a) is not identically zero."""
import numpy as np
from s1_matrix_collision import *
rng = np.random.default_rng(3)
for inter in ('nn', 'cube'):
    model = Stag(2, 0.5, inter)
    def Ssym(k, B, r):
        n = model.n; M = np.zeros((n, n), complex)
        for A in range(n):
            M[model.xor[A, model.idx(np.array(B))], A] = np.exp(1j*np.dot(k + np.pi*model.As[A], r))
        return M
    procs = sample_processes(model, 800, [(1, 1, 1, 1)], rng)
    labs_all = []; amp = {1: [], -1: []}; Wn = []
    for (s, k1, k2, k3, k4) in procs:
        vecs = []; labs = []
        for k in (k1, k2, k3, k4):
            Um, Up, w = model.U(k)
            S12 = Ssym(k, (0, 1), np.array([1, 0])) @ Ssym(k, (0, 0), np.array([0, 1]))  # xi_1 = (-1)^{x2}, xi_2 = 1
            assert np.linalg.norm(S12 @ model.h(k) - model.h(k) @ S12) < 1e-12
            lam, v = np.linalg.eig(Up.conj().T @ S12 @ Up)
            lab = lam*np.exp(-1j*(k[0] + k[1]))
            vecs.append(Up @ v); labs.append(lab)
        labs_all += [l for L in labs for l in L]
        Us = vecs
        W = model.W((k1, k2, k3, k4), Us); Wn.append(np.linalg.norm(W))
        # same-sector element: label value c (two values +-c); pick index with matching label in each leg
        ref = labs[0]
        for ia in range(2):
            c = ref[ia]
            idx = [int(np.argmin(np.abs(L - c))) for L in labs]
            if max(np.min(np.abs(L - c)) for L in labs) > 1e-8: continue
            amp[1 if ia == 0 else -1].append(abs(W[idx[2], idx[3], idx[0], idx[1]]))
    u = np.unique(np.round(np.array(labs_all), 6))
    print(f"d=2 m=0.5 {inter}: distinct sector labels {u}; |W| median {np.median(Wn):.2f}")
    for a in (1, -1):
        A = np.array(amp[a])
        print(f"  same-sector (a,a)->(a,a) amplitude, label branch {a}: {len(A)} processes, median {np.median(A):.3e}, fraction > 1e-8: {np.mean(A > 1e-8):.3f}")
