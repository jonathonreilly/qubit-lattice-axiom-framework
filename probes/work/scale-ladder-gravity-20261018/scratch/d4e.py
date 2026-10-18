import sys, pickle, itertools, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
C = pickle.load(open('d4.pkl', 'rb')); tix = {t: i for i, t in enumerate(C.types)}
def S(k): return RG.p1_scalar(C, k)
def on_shell(ks, guess):
    f = lambda kt: np.linalg.det(S(np.array([*ks, kt])))
    x = guess
    for _ in range(80):
        h = 1e-7; d = (f(x+h)-f(x-h))/(2*h); st = f(x)/d; x -= st
        if abs(st) < 1e-14: break
    k = np.array([*ks, x]); w, V = np.linalg.eig(S(k)); i = np.argmin(abs(w)); return k, V[:, i], abs(w[i])
def stress(k1, phi1, k2, phi2):
    """J_c: coefficient of eps_c in delta S[phibar(k1), phi(k2)] for delta l_c(T) = eps_c e^{iq.T}, q = k1 - k2."""
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
            dl2 = 2*np.linalg.norm(P[j] - P[i])*np.exp(1j*q @ np.array(anc, float))
            dG = np.zeros((4, 4), complex)
            if i == 0:
                dG[j-1, j-1] += dl2
                for b in range(4):
                    if b != j-1: dG[j-1, b] += dl2/2; dG[b, j-1] += dl2/2
            else:
                dG[i-1, j-1] -= dl2/2; dG[j-1, i-1] -= dl2/2
            J[c] += np.sum(Psi*dG)
    return J
rng = np.random.default_rng(9)
n1, n2 = rng.standard_normal(3), rng.standard_normal(3)
for s in (0.1, 0.05, 0.025):
    k1s, k2s = s*n1/np.linalg.norm(n1), 0.7*s*n2/np.linalg.norm(n2)
    k1, p1, r1 = on_shell(k1s, 1j*s); k2, p2, r2 = on_shell(k2s, 0.7j*s)
    J = stress(k1, p1, k2, p2); q = k1 - k2
    # soft extras at q
    Qq = C.Q(q); Qh = 0.5*(Qq + Qq.conj().T) if np.allclose(q.imag, 0) else Qq
    w, V = np.linalg.eig(Qq); idx = np.argsort(np.abs(w)); Vs = V[:, idx[:40]]
    A = np.hstack([C.line_map(q), C.gauge(q)]); P = np.eye(C.E) - A @ np.linalg.pinv(A, rcond=1e-10)
    u, sv, _ = np.linalg.svd(P @ Vs); X = u[:, :2]          # the two non-metric soft directions
    ov = np.linalg.norm(X.conj().T @ J)/np.linalg.norm(J)
    print(f"s={s}: Re k_t legs {abs(k1[3].real):.1e},{abs(k2[3].real):.1e} (shell residual {max(r1,r2):.0e}); |X^dag J|/|J| = {ov:.3e}; |J| = {np.linalg.norm(J):.2e}")
