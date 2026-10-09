"""C2: vacuum TT shear modulus of a label-blind local field on different frozen point sets.

Model (supplied, toy): massive scalar, H = 1/2 sum pi^2 + 1/2 phi^T (Lap + m^2) phi, where the graph
Laplacian has weights w(d_g) = (1 - d_g^2/R^2)^4_+ computed from CURRENT proper distances
d_g^2 = dx^T g dx (label-blind: who couples to whom is decided by proper distance only).
Metric g = exp(t h), h traceless (volume preserving), tr h^2 = 1.
Vacuum energy E = sum_n 1/2 sqrt(lam_n + m^2).  E''(0) computed EXACTLY by
  E'' = sum_n f'(l_n) (V^T L'' V)_nn + sum_{n,m} (V^T L' V)_nm^2 [f'(l_n)-f'(l_m)]/(l_n-l_m).
Point sets (density 1, periodic box side Lb):
  Z3 crystal; jittered Z3 (+-a); hard-core RSA (min distance d0); uniform iid ("Poisson").
Prediction (pushforward lemma): uniform iid -> ensemble mean E'' = 0 up to torus-shape finite size;
  crystal / jittered / hard-core -> nonzero.
Also: infinite-lattice Z3 value from k-space (cross-check of the real-space code).
"""
import numpy as np, sys, time
rng = np.random.default_rng(20261009)
R = 1.8; m2 = 1.0
f1 = lambda x: 0.25/np.sqrt(x + m2)
f2 = lambda x: -0.125/(x + m2)**1.5

def hs():
    E = [np.diag([1., -1, 0]), np.diag([0., 1, -1]), np.diag([1., 0, -1])]
    T = []
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1.; T.append(M)
    return {'E_g': [e/np.sqrt(2) for e in E], 'T_2g': [t/np.sqrt(2) for t in T]}
H = hs()

def pairs(X, Lb):
    D = X[None, :, :] - X[:, None, :]
    D -= Lb*np.round(D/Lb)
    d2 = np.einsum('ijk,ijk->ij', D, D)
    iu = np.triu_indices(len(X), 1)
    msk = d2[iu] < R**2
    return iu[0][msk], iu[1][msk], D[iu][msk]

def lap(n, I, J, w):
    Lm = np.zeros((n, n))
    np.add.at(Lm, (I, J), -w); np.add.at(Lm, (J, I), -w)
    deg = np.zeros(n); np.add.at(deg, I, w); np.add.at(deg, J, w)
    Lm[np.diag_indices(n)] += deg
    return Lm

def hessians(X, Lb):
    n = len(X)
    I, J, D = pairs(X, Lb)
    s = np.einsum('pk,pk->p', D, D)/R**2
    w = (1 - s)**4; ws = -4*(1 - s)**3; wss = 12*(1 - s)**2
    L0 = lap(n, I, J, w)
    lam, V = np.linalg.eigh(L0)
    lam = np.clip(lam, 0, None)
    F1 = f1(lam)
    dl = lam[:, None] - lam[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        F = (F1[:, None] - F1[None, :])/dl
    deg = np.abs(dl) < 1e-10
    F[deg] = (f2(0.5*(lam[:, None] + lam[None, :])))[deg]
    out = {}
    for ch, hl in H.items():
        vals1, vals2 = [], []
        for h in hl:
            sp = np.einsum('pi,ij,pj->p', D, h, D)/R**2
            spp = np.einsum('pi,ij,pj->p', D, h@h, D)/R**2
            w1 = ws*sp; w2 = wss*sp**2 + ws*spp
            A1 = V.T @ lap(n, I, J, w1) @ V
            A2 = V.T @ lap(n, I, J, w2) @ V
            e1 = np.sum(F1*np.diag(A1))
            e2 = np.sum(F1*np.diag(A2)) + np.sum(A1**2*F)
            vals1.append(e1/n); vals2.append(e2/n)
        out[ch] = (np.mean(vals1), np.mean(vals2))
    return out

def kspace_Z3(M=64):
    rr = int(np.ceil(R))
    ns = np.array([(a, b, c) for a in range(-rr, rr+1) for b in range(-rr, rr+1) for c in range(-rr, rr+1)
                   if 0 < a*a+b*b+c*c < R**2], float)
    k = 2*np.pi*np.arange(M)/M
    K = np.stack(np.meshgrid(k, k, k, indexing='ij'), -1).reshape(-1, 3)
    C = 1 - np.cos(K @ ns.T)          # (Nk, Nn)
    s = np.einsum('pk,pk->p', ns, ns)/R**2
    w = (1-s)**4; ws = -4*(1-s)**3; wss = 12*(1-s)**2
    lam = C @ w                       # lambda(k) = sum over all n (both signs) w_n (1 - cos k.n)
    res = {}
    for ch, hl in H.items():
        h = hl[0]
        sp = np.einsum('pi,ij,pj->p', ns, h, ns)/R**2
        spp = np.einsum('pi,ij,pj->p', ns, h@h, ns)/R**2
        l1 = C @ (ws*sp); l2 = C @ (wss*sp**2 + ws*spp)
        res[ch] = (np.mean(f1(lam)*l1), np.mean(f1(lam)*l2 + f2(lam)*l1**2))
    return res

def rsa(N, Lb, d0, maxtry=10**7):
    pts = []
    tries = 0
    while len(pts) < N and tries < maxtry:
        c = rng.uniform(0, Lb, (2000, 3)); tries += 2000
        for p in c:
            if pts:
                P = np.array(pts); d = P - p; d -= Lb*np.round(d/Lb)
                if np.min(np.einsum('ij,ij->i', d, d)) < d0**2: continue
            pts.append(p)
            if len(pts) == N: break
    return np.array(pts)

if __name__ == '__main__':
    Lb = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    nreal = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    N = Lb**3
    print(f"R={R} m2={m2} box={Lb} N={N} realizations={nreal}")
    print("k-space Z3, M=64 (infinite lattice):", {c: tuple(round(x, 7) for x in v) for c, v in kspace_Z3(64).items()})
    print(f"k-space Z3, M={Lb} (same torus):    ", {c: tuple(round(x, 7) for x in v) for c, v in kspace_Z3(Lb).items()})
    g = np.stack(np.meshgrid(*[np.arange(Lb)]*3, indexing='ij'), -1).reshape(-1, 3).astype(float)
    print("real-space Z3 crystal:            ", {c: tuple(round(x, 7) for x in v) for c, v in hessians(g, Lb).items()})
    sets = {
        'jittered Z3 a=0.25': lambda: (g + rng.uniform(-0.25, 0.25, g.shape)) % Lb,
        'hard-core RSA d0=0.80': lambda: rsa(N, Lb, 0.80),
        'uniform iid (Poisson-like)': lambda: rng.uniform(0, Lb, (N, 3)),
    }
    for name, gen in sets.items():
        t0 = time.time()
        acc = {c: [] for c in H}
        for r_ in range(nreal):
            X = gen(); o = hessians(X, Lb)
            for c in H: acc[c].append(o[c][1])
        msg = []
        for c in H:
            a = np.array(acc[c]); msg.append(f"{c}: E''/N = {a.mean():+.6f} +- {a.std(ddof=1)/np.sqrt(len(a)):.6f} (per-real sd {a.std(ddof=1):.5f})")
        print(f"{name:28s} " + " | ".join(msg) + f"   [{time.time()-t0:.0f}s]")
