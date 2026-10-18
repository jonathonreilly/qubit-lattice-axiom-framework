import sys, pickle, itertools, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
C = pickle.load(open('canon_1.pkl', 'rb')); tix = {t: i for i, t in enumerate(C.types)}
def on_shell(ks, guess):
    f = lambda kt: np.linalg.det(RG.p1_scalar(C, np.array([*ks, kt])))
    x = guess
    for _ in range(80):
        h = 1e-7; st = f(x)/((f(x+h)-f(x-h))/(2*h)); x -= st
        if abs(st) < 1e-14: break
    k = np.array([*ks, x]); w, V = np.linalg.eig(RG.p1_scalar(C, k)); i = np.argmin(abs(w)); return k, V[:, i]
def stress(k1, phi1, k2, phi2):
    q = k1 - k2; J = np.zeros(C.E, complex)
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); E = P[1:] - P[0]; G = E @ E.T; Gi = np.linalg.inv(G)
        v2 = np.array([phi2[tix[v[1]]]*np.exp(1j*k2 @ np.array(v[0], float)) for v in vs])
        v1 = np.array([np.conj(phi1[tix[v[1]]])*np.exp(-1j*k1 @ np.array(v[0], float)) for v in vs])
        d2 = v2[1:] - v2[0]; d1 = v1[1:] - v1[0]
        X = d1 @ Gi @ d2; Pm = np.outer(Gi @ d2, Gi @ d1); Pm = 0.5*(Pm + Pm.T)
        Psi = np.sqrt(np.linalg.det(G))/24*(0.5*Gi*X - Pm)
        for i, j in itertools.combinations(range(5), 2):
            key, anc = RG._key_pair(vs[i], vs[j]); c = C.ekey[key]
            dl2 = 2*np.linalg.norm(P[j] - P[i])*np.exp(1j*q @ np.array(anc, float)); dG = np.zeros((4, 4), complex)
            if i == 0:
                dG[j-1, j-1] += dl2
                for b in range(4):
                    if b != j-1: dG[j-1, b] += dl2/2; dG[b, j-1] += dl2/2
            else:
                dG[i-1, j-1] -= dl2/2; dG[j-1, i-1] -= dl2/2
            J[c] += np.sum(Psi*dG)
    return J
rng = np.random.default_rng(9); n1, n2 = rng.standard_normal(3), rng.standard_normal(3)
for s in (0.1, 0.05):
    k1, p1 = on_shell(s*n1/np.linalg.norm(n1), 1j*s); k2, p2 = on_shell(0.7*s*n2/np.linalg.norm(n2), 0.7j*s)
    J = stress(k1, p1, k2, p2); G = C.gauge(k1 - k2); Ga = sum(G[:, 4*t:4*t+4] for t in range(len(C.types)))
    print(f"s={s}: P1 on every fine site: |G^T J|/|J| (all displacements) {np.linalg.norm(G.T @ J)/np.linalg.norm(J):.2f}; uniform part {np.linalg.norm(Ga.T @ J)/np.linalg.norm(J):.1e}")
