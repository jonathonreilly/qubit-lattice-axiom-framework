import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
def rows(C, k, which):
    out = []
    for a, d in C.terms:
        t = d if which == 'd' else a
        r = np.zeros(C.E, complex); np.add.at(r, t[0], t[2]*np.exp(1j*(t[1] @ k))); out.append(r)
    return np.array(out)
def analyse(C, ngauge, nnull, label):
    rng = np.random.default_rng(3)
    for _ in range(2):
        k = rng.standard_normal(4)*0.4
        Q = C.Q(k); _, s, vh = np.linalg.svd(Q); N = vh[-nnull:].conj().T; G = C.gauge(k)
        X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :nnull-ngauge]
        D = rows(C, k, 'd'); A = rows(C, k, 'a')
        nD = np.linalg.norm(D @ X, axis=0)/np.linalg.norm(D, 2); nG = np.linalg.norm(D @ G)/np.linalg.norm(D, 2)/np.linalg.norm(G)
        print(f"{label} |k|={np.linalg.norm(k):.2f}: |D G| {nG:.1e}; |D x_extra| per extra (rel. to ||D||): " + " ".join(f"{x:.1e}" for x in nD[:6]),
              f"; rank D = {np.linalg.matrix_rank(D, tol=1e-8*np.linalg.norm(D,2))}, edges {C.E}, hinges {len(C.terms)}")
OFF, S = RG.kuhn(); analyse(RG.Complex(OFF, S), 4, 5, 'Kuhn')
analyse(pickle.load(open('bary.pkl', 'rb')), 64, 80, 'bary')
