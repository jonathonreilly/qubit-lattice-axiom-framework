"""OS reflection positivity for massive Gaussian fields: controls and the D4-cone P1 scalar and Hodge 1-forms."""
import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from rp import rp_matrix

def min_eig(R):
    w = np.linalg.eigvalsh(0.5 * (R + R.conj().T)); return w.min() / max(abs(w).max(), 1e-300), w.max()

if __name__ == '__main__':
    Nt = 8; m2 = 0.3
    # control 1: 1-type NN Laplacian on Z^4 (known RP)
    nn = lambda k: np.array([[np.sum(4 * np.sin(np.asarray(k) / 2) ** 2) + m2]], complex)
    # control 2: a higher-derivative scalar (Laplacian + Laplacian^2), not RP
    hd = lambda k: np.array([[(lambda L: L + 0.5 * L * L + m2)(np.sum(4 * np.sin(np.asarray(k) / 2) ** 2))]], complex)
    D = pickle.load(open('d4.pkl', 'rb'))
    offs_t = [float(o[3]) for o in D.OFF]
    gi = np.eye(4)
    def p1(k):
        S = RG.p1_scalar(D, k); M0 = mass0(k); return S + m2 * M0
    def mass0(k):
        k = np.asarray(k, complex); nt = len(D.types); tix = {t: i for i, t in enumerate(D.types)}; M = np.zeros((nt, nt), complex)
        for vs in D.simp:
            P = np.array([D.pos(v) for v in vs]); E = P[1:] - P[0]; vol = abs(np.linalg.det(E)) / 24
            for i in range(5):
                for j in range(5):
                    M[tix[vs[i][1]], tix[vs[j][1]]] += vol * (2 if i == j else 1) / 30 * np.exp(1j * k @ (np.array(vs[j][0], float) - np.array(vs[i][0], float)))
        return M
    for ks in [np.array([0.0, 0.0, 0.0]), np.array([0.7, -0.3, 0.2]), np.array([1.9, 0.4, -1.1])]:
        out = []
        for lab, Qf, offs in (('NN', nn, [0.0]), ('higher-deriv', hd, [0.0]), ('D4 P1', p1, offs_t)):
            for t0 in (0.0, 0.5):
                if lab == 'higher-deriv' and t0 == 0.5: continue
                R, half = rp_matrix(Qf, offs, ks, Nt, t0)
                mn, mx = min_eig(R); out.append(f"{lab} t0={t0}: min/max {mn:+.2e}")
        print(f"ks={ks}: " + "; ".join(out))
