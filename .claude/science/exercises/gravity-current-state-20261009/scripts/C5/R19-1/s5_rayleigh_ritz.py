"""R19-1 s5: six-mode Rayleigh-Ritz (multi-mode SMA) on the slot-type basis at each k: F v = lambda G v, with
G = 6x6 static matrix (R18-1's M(k)), F = 6x6 f-sum (Dirichlet-form) matrix. Seed-averaged, per direction copy, then
copy-averaged eigenvalues. Theorem 5 (report): along a ray each RR branch is gapped or O(t^2)."""
import numpy as np, pickle, glob, sys, scipy.linalg as sl
sys.path.insert(0, '.')
for L in [6, 8]:
    for bU in [0.5, 1.0, 2.0, 3.0]:
        fs = [f for f in sorted(glob.glob('../data/fs_L%d_b%.1f_s[12].pkl' % (L, bU)))]
        if len(fs) < 2: continue
        R = [pickle.load(open(f, 'rb')) for f in fs]
        out = {}
        for ik, (name, m, v) in enumerate(R[0]['klist']):
            G = np.mean([r['Mb'][:, ik].mean(0) for r in R], 0); F = np.mean([r['Fb'][:, ik].mean(0) for r in R], 0)
            G = (G + G.conj().T)/2; F = (F + F.conj().T)/2
            w = sl.eigh(F, G, eigvals_only=True)
            out.setdefault((name, m), []).append(np.sort(w.real))
        line = []
        for name in ["axis", "face", "body"]:
            for m in [1, 2]:
                ws = np.mean(out[(name, m)], 0)
                line.append("%s m=%d: %s" % (name, m, np.array2string(ws, precision=3, max_line_width=200)))
        print("L=%d bU=%.1f\n   " % (L, bU) + "\n   ".join(line))
