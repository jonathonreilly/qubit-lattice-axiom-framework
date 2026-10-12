"""C1 checks for part (a).
 K: Koszul lemma -- every finite-range divergence-free edge field on Z^d (free-module sector) is a finite-range curl.
    Linear algebra over Laurent polynomials supported in a box, d = 2, 3.
 R: Lemma R -- C^1 collision invariants of the NORMAL on-shell set inside the open cube are span{k_x, k_y, E} (+const).
    Finite-basis SVD on sampled normal collisions, d = 2, for NN Klein-Gordon and for SLAC.
    Also: residual of f = E grad E on normal collisions (sin k for KG fails; k for SLAC passes).
"""
import numpy as np, itertools
rng = np.random.default_rng(7)
out = []
P = lambda *s: (print(*s), out.append(' '.join(str(t) for t in s)))

# ---------------- K: Koszul ----------------
def koszul_check(d, R, Rbig):
    # index Laurent monomials in a box
    def box(lo, hi):
        pts = list(itertools.product(range(lo, hi+1), repeat=d))
        return {p: i for i, p in enumerate(pts)}
    Bw = box(-R, R)                 # support of W_j
    Bout = box(-R-1, R)              # support of div W
    nW = len(Bw)
    # div: (1 - t_j^{-1}) W_j ; coefficient of t^a in t_j^{-1} W is W_{a+e_j}
    D = np.zeros((len(Bout), d*nW))
    for j in range(d):
        for p, i in Bw.items():
            D[Bout[p], j*nW+i] += 1
            q = list(p); q[j] -= 1
            D[Bout[tuple(q)], j*nW+i] -= 1
    # kernel of div
    u, s, vt = np.linalg.svd(D)
    rank = (s > 1e-9).sum()
    ker = vt[rank:].T      # columns: div-free W in the box
    # curl images from a bigger box of 2-forms A_{il} (i<l), W_j = sum_i (1 - t_i^{-1}) A_{ij}, A antisym
    Ba = box(-Rbig, Rbig)
    Bw2 = box(-Rbig-1, Rbig)
    nW2 = len(Bw2)
    pairs = [(i, l) for i in range(d) for l in range(i+1, d)]
    Cm = np.zeros((d*nW2, len(pairs)*len(Ba)))
    for pi_, (i, l) in enumerate(pairs):
        for p, ia in Ba.items():
            col = pi_*len(Ba) + ia
            # W_l += (1 - t_i^{-1}) A_{il};  W_i += (1 - t_l^{-1}) A_{li} = -(1 - t_l^{-1}) A_{il}
            for (jw, jt, sg) in [(l, i, +1), (i, l, -1)]:
                Cm[jw*nW2 + Bw2[p], col] += sg
                q = list(p); q[jt] -= 1
                Cm[jw*nW2 + Bw2[tuple(q)], col] -= sg
    # embed kernel vectors into the bigger W-space
    E = np.zeros((d*nW2, ker.shape[1]))
    for j in range(d):
        for p, i in Bw.items():
            E[j*nW2 + Bw2[p], :] = ker[j*nW + i, :]
    sol, resid, rk, sv = np.linalg.lstsq(Cm, E, rcond=None)
    err = np.abs(Cm @ sol - E).max()
    return ker.shape[1], err

for d, R, Rb in [(2, 2, 3), (2, 3, 4), (3, 1, 2)]:
    nk, err = koszul_check(d, R, Rb)
    P(f"K: d={d}, W in box [-{R},{R}]^{d}: dim ker(div) = {nk}; max residual of curl fit from A-box [-{Rb},{Rb}]^{d} = {err:.2e}")

# ---------------- R: collision invariants on the normal set ----------------
def disp(name, m=1.0):
    if name == 'KG':
        E = lambda k: np.sqrt(m**2 + 2*(2 - np.cos(k[...,0]) - np.cos(k[...,1])))
        f = lambda k: np.sin(k)       # E grad E
    else:
        E = lambda k: np.sqrt(m**2 + (k**2).sum(-1))
        f = lambda k: k.copy()
    return E, f

def sample_normal(E, N):
    rows = []
    while len(rows) < N:
        k1 = rng.uniform(-np.pi, np.pi, 2); k2 = rng.uniform(-np.pi, np.pi, 2)
        K = k1 + k2; W = E(k1) + E(k2)
        d = rng.normal(size=2); d /= np.linalg.norm(d)
        # k3 = c + t d with c = K/2 ; find roots of E(k3)+E(K-k3) - W along the line, keep those with k3,k4 in open cube
        c = K/2
        ts = np.linspace(-8, 8, 4001)
        k3 = c[None, :] + ts[:, None]*d[None, :]
        k4 = K[None, :] - k3
        g = E(k3) + E(k4) - W
        inside = (np.abs(k3) < np.pi).all(1) & (np.abs(k4) < np.pi).all(1)
        idx = np.where((np.sign(g[:-1]) != np.sign(g[1:])) & inside[:-1] & inside[1:])[0]
        for i in idx:
            a, b = ts[i], ts[i+1]
            for _ in range(60):
                mid = 0.5*(a+b)
                gm = E(c + mid*d) + E(K - c - mid*d) - W
                ga = E(c + a*d) + E(K - c - a*d) - W
                if np.sign(gm) == np.sign(ga): a = mid
                else: b = mid
            t = 0.5*(a+b); q3 = c + t*d; q4 = K - q3
            if np.abs(q3 - k1).max() > 1e-3 and np.abs(q3 - k2).max() > 1e-3:
                rows.append((k1, k2, q3, q4))
    return rows[:N]

def basis(k, E):
    x, y = k[..., 0], k[..., 1]
    cols = {'kx': x, 'ky': y, 'E': E(k), 'kx^2': x*x, 'ky^2': y*y, 'kxky': x*y, 'kx^3': x**3, 'kx ky^2': x*y*y,
            'sinx': np.sin(x), 'siny': np.sin(y), 'cosx': np.cos(x), 'cosy': np.cos(y), 'sin2x': np.sin(2*x),
            'cosx cosy': np.cos(x)*np.cos(y), 'E^2': E(k)**2, 'E^3': E(k)**3, 'x sin y': x*np.sin(y)}
    return list(cols.keys()), np.stack(list(cols.values()), -1)

for name in ['KG', 'SLAC']:
    E, f = disp(name)
    rows = sample_normal(E, 600)
    k1, k2, k3, k4 = [np.array([r[i] for r in rows]) for i in range(4)]
    en = np.abs(E(k1)+E(k2)-E(k3)-E(k4)).max(); mo = np.abs(k1+k2-k3-k4).max()
    names, B1 = basis(k1, E); _, B2 = basis(k2, E); _, B3 = basis(k3, E); _, B4 = basis(k4, E)
    M = B1 + B2 - B3 - B4
    M = M / np.linalg.norm(B1, axis=0)
    s = np.linalg.svd(M, compute_uv=False)
    P(f"\nR: {name} d=2 m=1, {len(rows)} normal on-shell collisions in open cube (energy resid {en:.1e}, momentum resid {mo:.1e})")
    P(f"   {len(names)}-column basis; singular values (normalized cols), smallest 5: " + ' '.join(f"{v:.2e}" for v in s[-5:]))
    _, s_, vt = np.linalg.svd(M)
    null = vt[(s_ < 1e-8)]
    P(f"   null-space dim = {null.shape[0]}; null vectors supported on: " + '; '.join(
        ', '.join(f"{names[i]}" for i in np.where(np.abs(v) > 1e-6)[0]) for v in null))
    fr = f(k1) + f(k2) - f(k3) - f(k4)
    P(f"   f = E grad E: max |collision defect| on normal set = {np.abs(fr).max():.3e}  (rms {np.sqrt((fr**2).mean()):.3e})")
open('c1_checks.out', 'w').write('\n'.join(out) + '\n')
