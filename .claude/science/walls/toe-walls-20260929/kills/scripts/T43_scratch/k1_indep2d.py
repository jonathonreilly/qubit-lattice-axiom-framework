"""K1: independent 2D re-implementation (no import of the attack's stag.py) of the taste-singlet Gamma_f determinant phase,
with (a) m, L scan to L=32, (b) zero-mode decomposition (index-theorem reading), (c) fixed m*L continuum-like scan,
(d) scheme dependence: Gamma_f -> symmetrised Gamma_f (1 + kappa D^2) (same continuum limit, different lattice artefact)."""
import numpy as np

def build(L, Q):
    V = L * L
    idx = lambda x1, x2: (x1 % L) * L + (x2 % L)
    phi = 2 * np.pi * Q / L ** 2
    U1 = np.ones((L, L), complex); U2 = np.ones((L, L), complex)
    for x1 in range(L):
        for x2 in range(L):
            U2[x1, x2] = np.exp(1j * phi * x1)
            if x1 == L - 1:
                U1[x1, x2] = np.exp(-1j * phi * L * x2)
    # forward shifts T_mu (T chi)(x) = U_mu(x) chi(x+mu)
    T1 = np.zeros((V, V), complex); T2 = np.zeros((V, V), complex)
    for x1 in range(L):
        for x2 in range(L):
            T1[idx(x1, x2), idx(x1 + 1, x2)] = U1[x1, x2]
            T2[idx(x1, x2), idx(x1, x2 + 1)] = U2[x1, x2]
    eta2 = np.array([(-1.0) ** x1 for x1 in range(L) for x2 in range(L)])
    D = 0.5 * ((T1 - T1.conj().T) + np.diag(eta2) @ (T2 - T2.conj().T))
    C1 = 0.5 * (T1 + T1.conj().T); C2 = 0.5 * (T2 + T2.conj().T)
    G = 1j * np.diag(eta2) @ (0.5 * (C1 @ C2 + C2 @ C1))
    # check total flux = sum of plaquette angles
    tot = 0.0
    for x1 in range(L):
        for x2 in range(L):
            a = U1[x1, x2] * U2[(x1 + 1) % L, x2] * np.conj(U1[x1, (x2 + 1) % L]) * np.conj(U2[x1, x2])
            tot += np.angle(a)
    return D, G, tot / (2 * np.pi)

def argdet(M):
    s, ld = np.linalg.slogdet(M)
    return np.angle(s)

def cfun(D, G, Q, m, r):
    a = argdet(D + m * np.eye(len(D)) + 1j * r * m * G)
    return -a / (2 * Q * np.arctan(r))

if __name__ == "__main__":
    out = []
    def rep(s):
        print(s); out.append(s)
    D, G, fl = build(8, 1)
    rep(f"sanity L=8 Q=1: flux/2pi={fl:.6f} Hermitian(G)={np.abs(G-G.conj().T).max():.1e} antiherm(D)={np.abs(D+D.conj().T).max():.1e}")
    rep(f"sanity arg det(m=.5,r=.2)={argdet(D+0.5*np.eye(64)+1j*0.1*G):+.5f}   (attack: -0.27268)")
    rep("=== (a) c(m,L) = -arg det/(2 Q arctan r), r=0.1, Q=1")
    ms = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0)
    rep("  L   " + "  ".join(f"m={m:<5}" for m in ms))
    cache = {}
    for L in (8, 12, 16, 24, 32):
        D, G, _ = build(L, 1); cache[L] = (D, G)
        rep(f" {L:3d}  " + "  ".join(f"{cfun(D,G,1,m,0.1):.4f}" for m in ms))
    rep("=== (b) zero-mode decomposition, Q=1 and 2: g_j = eigenvalues of Gamma restricted to ker D; zero-mode-only c")
    for Q in (1, 2):
        for L in (8, 16, 32):
            D, G, _ = build(L, Q)
            H = -1j * D
            w, v = np.linalg.eigh((H + H.conj().T) / 2)
            zm = np.abs(w) < 1e-9
            P = v[:, zm]
            g = np.linalg.eigvalsh(P.conj().T @ G @ P)
            czm = np.mean(np.arctan(0.1 * g)) / np.arctan(0.1) * (len(g) / (2 * Q))
            rest = [cfun(D, G, Q, m, 0.1) for m in (0.02, 0.5)]
            rep(f" Q={Q} L={L:2d}: #zero modes={zm.sum()} (2Q expected {2*Q})  <Gamma>_zm = {np.round(g,4)}  c_zm(r=.1)={czm:.4f}  next |lambda|={np.sort(np.abs(w))[zm.sum()]:.3f}   total c(m=.02)={rest[0]:.4f} c(m=.5)={rest[1]:.4f}")
    rep("=== (c) continuum-like scan: m*L = 1.6 fixed (physical mass and volume fixed, a -> 0), Q=1, r=0.1")
    for L in (8, 12, 16, 24, 32):
        D, G = cache[L]
        m = 1.6 / L
        rep(f" L={L:2d} m={m:.4f}: c={cfun(D,G,1,m,0.1):.4f}   1-c={1-cfun(D,G,1,m,0.1):.4f}   (1-c)*L^2={(1-cfun(D,G,1,m,0.1))*L*L:.3f}")
    rep("=== (c') fixed lattice mass m=0.5, L -> infinity: c(0.5)")
    for L in (8, 12, 16, 24, 32):
        D, G = cache[L]
        rep(f" L={L:2d}: c(m=0.5)={cfun(D,G,1,0.5,0.1):.5f}")
    rep("=== (d) scheme dependence: Gamma_kappa = sym(Gamma (1+kappa D^2)), same free-field limit at p->0 corners, Q=1, L=16, r=0.1")
    D, G = cache[16]
    D2 = D @ D
    I = np.eye(len(D))
    for kappa in (0.0, 0.25, 0.5, -0.25):
        Gk = 0.5 * (G @ (I + kappa * D2) + (I + kappa * D2) @ G)
        Gk = 0.5 * (Gk + Gk.conj().T)
        row = "  ".join(f"m={m}:{cfun(D,Gk,1,m,0.1):.4f}" for m in (0.02, 0.1, 0.5, 1.0))
        rep(f" kappa={kappa:+.2f}: {row}")
    open("k1_out.txt", "w").write("\n".join(out) + "\n")
