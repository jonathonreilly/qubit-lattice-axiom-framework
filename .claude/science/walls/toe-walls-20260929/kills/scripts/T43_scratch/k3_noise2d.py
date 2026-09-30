"""K3: is 'phase proportional to Q' a property of the topological sector or of the exact-zero-mode uniform-flux background?
2D U(1): uniform flux 2 pi Q plus i.i.d. Gaussian link-angle noise sigma (total flux unchanged: noise cancels around the torus,
plaquette angles stay inside (-pi,pi)).  Report phase statistics per sector, lifted would-be zero modes, and C-oddness."""
import numpy as np
from k1_indep2d import build

def build_noisy(L, Q, sigma, rng):
    D0, G0, _ = build(L, Q)
    V = L * L
    # multiply forward links by exp(i xi): rebuild via link-noise applied to shifts; simplest: reconstruct T1,T2 from D0 structure
    # -> rebuild directly
    idx = lambda x1, x2: (x1 % L) * L + (x2 % L)
    phi = 2 * np.pi * Q / L ** 2
    th1 = np.zeros((L, L)); th2 = np.zeros((L, L))
    for x1 in range(L):
        for x2 in range(L):
            th2[x1, x2] = phi * x1
            if x1 == L - 1:
                th1[x1, x2] = -phi * L * x2
    th1 = th1 + sigma * rng.normal(size=(L, L)); th2 = th2 + sigma * rng.normal(size=(L, L))
    T1 = np.zeros((V, V), complex); T2 = np.zeros((V, V), complex)
    for x1 in range(L):
        for x2 in range(L):
            T1[idx(x1, x2), idx(x1 + 1, x2)] = np.exp(1j * th1[x1, x2])
            T2[idx(x1, x2), idx(x1, x2 + 1)] = np.exp(1j * th2[x1, x2])
    eta2 = np.array([(-1.0) ** x1 for x1 in range(L) for x2 in range(L)])
    D = 0.5 * ((T1 - T1.conj().T) + np.diag(eta2) @ (T2 - T2.conj().T))
    C1 = 0.5 * (T1 + T1.conj().T); C2 = 0.5 * (T2 + T2.conj().T)
    G = 1j * np.diag(eta2) @ (0.5 * (C1 @ C2 + C2 @ C1))
    tot = 0.0
    for x1 in range(L):
        for x2 in range(L):
            a = th1[x1, x2] + th2[(x1 + 1) % L, x2] - th1[x1, (x2 + 1) % L] - th2[x1, x2]
            tot += np.angle(np.exp(1j * a))
    return D, G, tot / (2 * np.pi)

def argdet(M):
    return np.angle(np.linalg.slogdet(M)[0])

if __name__ == "__main__":
    import warnings; warnings.simplefilter("ignore")
    out = []
    def rep(s):
        print(s, flush=True); out.append(s)
    L = 12; r = 0.1; N = 30
    rng = np.random.default_rng(20260929)
    rep(f"2D U(1) L={L}, r={r}, {N} configs per row; c_eff = -arg det/(2 arctan r) (Q=1 rows) ; Q=0 rows report raw arg det/(2 arctan r)")
    for sigma in (0.0, 0.02, 0.05, 0.1, 0.2, 0.4):
        for Q in (1, 0):
            res = {0.05: [], 0.5: []}; lam = []; fl = []
            for _ in range(N):
                D, G, f = build_noisy(L, Q, sigma, rng)
                fl.append(f)
                w = np.linalg.eigvalsh(-1j * D)
                lam.append(np.sort(np.abs(w))[:2 * max(Q, 1)].max())
                for m in res:
                    res[m].append(-argdet(D + m * np.eye(L * L) + 1j * r * m * G) / (2 * np.arctan(r)))
            s = f"sigma={sigma:4.2f} Q={Q}  flux/2pi in [{min(fl):.3f},{max(fl):.3f}]  median lifted |lambda|={np.median(lam):.3f}  "
            for m in res:
                a = np.array(res[m])
                s += f" m={m}: mean={a.mean():+.3f} std={a.std():.3f}  "
            rep(s)
    open("k3_out.txt", "w").write("\n".join(out) + "\n")
