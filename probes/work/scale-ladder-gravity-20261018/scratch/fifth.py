import sys, numpy as np, contextlib, io
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
with contextlib.redirect_stdout(io.StringIO()):
    import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4
Qe, Mh = R.regge(np.eye(4))
D15 = [np.array(v, float) for v in R4.DIRS15]
def gauge(k):
    G = np.zeros((15, 4), complex)
    for c, v in enumerate(D15): G[c] = (np.exp(1j*k@v) - 1)*v/np.linalg.norm(v)
    return G
def null5(k):
    u, s, vh = np.linalg.svd(Qe(k)); N = vh[-5:].conj().T          # 15x5 null basis
    G = gauge(k); Pg = G @ np.linalg.pinv(G)
    r = N - Pg @ N; uu, ss, _ = np.linalg.svd(r); f = uu[:, 0]       # direction in null space orthogonal to gauge
    return f, np.linalg.norm(Qe(k) @ f), np.linalg.norm(G.conj().T @ f)
def p1_edge_stress(k1, k2):
    """J_c: coefficient of eps_c in delta S_phi[phibar(k1), phi(k2)] for delta l_c(x) = eps_c e^{iq.x}, q = k1-k2 (edge-length variables)."""
    q = k1 - k2; J = np.zeros(15, complex)
    for vs in R.SIMP:
        E = np.array([vs[i]-vs[0] for i in range(1, 5)], float); G = E @ E.T; Gi = np.linalg.inv(G)
        d2 = np.array([np.exp(1j*k2@v) for v in vs])[1:] - 1; d1 = np.array([np.exp(-1j*k1@v) for v in vs])[1:] - 1
        X = d1 @ Gi @ d2; P = np.outer(Gi @ d2, Gi @ d1); P = 0.5*(P+P.T)
        Psi = np.sqrt(np.linalg.det(G))/24*(0.5*Gi*X - P)
        # edges of the simplex: (i,j), i<j among 0..4
        for i in range(5):
            for j in range(i+1, 5):
                c, anc, sg = R.edge(vs[i], vs[j]) if tuple(vs[j]-vs[i]) in R.DIDX else R.edge(vs[j], vs[i])
                l = np.linalg.norm(vs[j]-vs[i]); dl2 = 2*l*np.exp(1j*q@anc)    # d(l^2) per unit eps_c
                dG = np.zeros((4, 4), complex)
                if i == 0: dG[j-1, j-1] += dl2; 
                if i == 0:
                    for b in range(4):
                        if b != j-1: dG[j-1, b] += dl2/2; dG[b, j-1] += dl2/2
                else:
                    dG[i-1, j-1] -= dl2/2; dG[j-1, i-1] -= dl2/2
                J[c] += np.sum(Psi*dG)
    return J
rng = np.random.default_rng(4)
for t in range(4):
    q = rng.standard_normal(4)*0.3
    f, res, gov = null5(q)
    # metric overlap of the fifth mode
    M = Mh(q); mov = np.linalg.norm(np.linalg.pinv(M) @ f) * np.linalg.norm(M) / 1
    # P1 static-ish stress at momentum transfer q (legs k2 random, k1 = k2 + q)
    k2 = rng.standard_normal(4)*0.4; k1 = k2 + q
    J = p1_edge_stress(k1, k2)
    G = gauge(q)
    ov_f = abs(f.conj() @ J)/np.linalg.norm(J); ov_g = np.linalg.norm(np.linalg.pinv(G) @ J)*np.linalg.norm(G)/np.linalg.norm(J)
    print(f"|q|={np.linalg.norm(q):.2f}: fifth mode |Qf|={res:.0e} |G^dag f|={gov:.0e}; P1 stress overlap with fifth {ov_f:.3e}, with gauge {ov_g:.3e}")
