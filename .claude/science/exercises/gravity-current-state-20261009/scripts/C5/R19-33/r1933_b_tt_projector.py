"""R19-33 (b): time-locality and reflection positivity of the TT projection on Z^4.
Lattice symbols in s_mu = 2 sin(k_mu/2) (K7a/K2 staggered placement makes the FP symbol O(4)-covariant
in s).  Spatial components h_ij live on integer time slices, so their k4-dependence is through
s4^2 = 2 - 2 cos k4 (2pi-periodic).
 (1) spatial-TT projector P3(q): independent of k4 -> kernel delta_{t,0} (local in time).
 (2) 4D-TT projector P4(s) = 1/2(th th + th th) - 1/3 th th, th = delta - s s / s^2: depends on k4;
     its time kernel at fixed q decays like exp(-E_q |t|), 2 sinh(E_q/2) = |q_hat| (non-local in time,
     range -> infinity as q -> 0).
 (3) OS (Hankel) tests at fixed spatial momentum of the spatial-component two-point matrix
     G_ab(t) = (1/2pi) int dk4 cos(k4 t) C_ab(k4),  a,b in {11,22,33,12,13,23}:
       control: spatial-TT field (K2's reduced graviton): C = P3 / s^2
       model A: 4D-TT Gaussian (R2-4's positive local constrained form): C = P4 / s^2
     site: H0=[G(i+j)], H2=[G(i+j)-G(i+j+2)];  link: [G(1+i+j)] (block Hankel, 6x6 blocks).
"""
import numpy as np
comps = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
def P_of(th):
    P = np.zeros((6, 6))
    for A, (m, n) in enumerate(comps):
        for B, (r, s) in enumerate(comps):
            P[A, B] = 0.5 * (th[m, r] * th[n, s] + th[m, s] * th[n, r]) - th[m, n] * th[r, s] / 3.0
    return P
def P3_of(qh):
    th = np.eye(3) - np.outer(qh, qh) / (qh @ qh)
    P = np.zeros((6, 6))
    for A, (m, n) in enumerate(comps):
        for B, (r, s) in enumerate(comps):
            P[A, B] = 0.5 * (th[m, r] * th[n, s] + th[m, s] * th[n, r]) - 0.5 * th[m, n] * th[r, s]
    return P
# metric on the 6 components (off-diagonals count twice in h:h); use unit-norm components
w = np.array([1, 1, 1, np.sqrt(2), np.sqrt(2), np.sqrt(2)])
def sym(P): return (w[:, None] * P * w[None, :])

NK = 1 << 14
k4 = 2 * np.pi * (np.arange(NK) + 0.5) / NK - np.pi
def G_of(Cfun, tmax):
    Cs = np.array([Cfun(k) for k in k4])               # NK x 6 x 6
    return [np.tensordot(np.cos(k4 * t), Cs, axes=(0, 0)) / NK for t in range(tmax + 1)]

def hankel_tests(G, N):
    d = G[0].shape[0]
    def blk(f):
        return np.block([[f(i, j) for j in range(N + 1)] for i in range(N + 1)])
    H0 = blk(lambda i, j: G[i + j]); H2 = blk(lambda i, j: G[i + j] - G[i + j + 2]); L1 = blk(lambda i, j: G[1 + i + j])
    out = []
    for M in (H0, H2, L1):
        e = np.linalg.eigvalsh(0.5 * (M + M.T)); out.append(e[0] / e[-1])
    return out

for q in ([0.3, 0.2, 0.1], [0.9, 0.0, 0.0], [1.2, -0.7, 0.4]):
    q = np.array(q); qh = 2 * np.sin(q / 2); q2 = qh @ qh
    E = 2 * np.arcsinh(np.sqrt(q2) / 2)
    print("\n== spatial momentum q =", q, " |q_hat|^2 = %.4f, E_q = %.4f ==" % (q2, E))
    def th4(k):
        s = np.array([qh[0], qh[1], qh[2], 2 * np.sin(k / 2)]); return np.eye(4) - np.outer(s, s) / (s @ s)
    # (1)/(2) time kernels of the projectors (component 11,11)
    G3 = G_of(lambda k: sym(P3_of(qh)), 6)
    G4P = G_of(lambda k: sym(P_of(th4(k)[:3, :3]) if False else P_of(th4(k))), 6)
    print(" spatial-TT projector kernel P3_{11,11}(t), t=0..4:", np.round([g[0, 0] for g in G3[:5]], 6))
    print(" 4D-TT  projector kernel P4_{11,11}(t), t=0..4:", np.round([g[0, 0] for g in G4P[:5]], 6))
    r = [G4P[t][0, 0] / G4P[t - 1][0, 0] for t in (3, 4, 5)]
    print("   successive ratios t=3..5:", np.round(r, 5), " vs exp(-E_q) = %.5f" % np.exp(-E))
    # (3) OS tests
    Nmax = 6
    for name, Cf in [("control: spatial-TT field  P3/s^2", lambda k: sym(P3_of(qh)) / (q2 + 4 * np.sin(k / 2) ** 2)),
                     ("model A: 4D-TT field       P4/s^2", lambda k: sym(P_of(th4(k))) / (q2 + 4 * np.sin(k / 2) ** 2))]:
        G = G_of(Cf, 2 * Nmax + 3)
        res = []
        for N in (1, 2, 4, 6):
            h0, h2, l1 = hankel_tests(G, N)
            res.append("N=%d site H0 %+.2e H2 %+.2e | link %+.2e" % (N, h0, h2, l1))
        print(" " + name)
        for s_ in res: print("    " + s_)
    # which component carries the failure (model A): diagonal entries G_aa(t) sign pattern
    G = G_of(lambda k: sym(P_of(th4(k))) / (q2 + 4 * np.sin(k / 2) ** 2), 8)
    for A, c in enumerate(comps):
        seq = [G[t][A, A] for t in range(8)]
        print("   model A G_{%d%d,%d%d}(t), t=0..7:" % (c[0]+1, c[1]+1, c[0]+1, c[1]+1), np.round(seq, 5))
