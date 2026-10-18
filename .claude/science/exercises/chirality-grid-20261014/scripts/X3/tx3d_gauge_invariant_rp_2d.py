"""T-X3d: gauge-invariant RP necessary condition for the gauged overlap at beta_g = 0.
Pre-registered in ../PREREG.md. 2D U(1), Lx=4 periodic, t in {-3..4} OPEN ends, one reflection plane (0|1).
Zt_ab = int dU_c det D_m[(u_a on Lambda+, U_c crossing, theta u_b on Lambda-)], Haar over 4 crossing links
by an n^4 trapezoid grid. Must be Hermitian PSD.
"""
import numpy as np, itertools, sys
Lx, Lt = 4, 8
ts = list(range(-3, 5)); plus = [1, 2, 3, 4]
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex)
gt, gx, g5 = s1, s2, s3
I2 = np.eye(2); N = 2 * Lx * Lt
def idx(x, t): return 2 * ((t + 3) * Lx + (x % Lx))
def theta(t): return 1 - t
G5 = np.kron(np.eye(N // 2), g5)

def DW_base(Ux, Ut):
    """Ux[t] (t in ts) array Lx; Ut[t] for t in ts except 0 (crossing) and 4 (open end)."""
    D = np.zeros((N, N), complex)
    for t in ts:
        for x in range(Lx):
            a = idx(x, t); D[a:a+2, a:a+2] += 2 * I2
            b = idx(x + 1, t); u = Ux[t][x]
            D[a:a+2, b:b+2] += -0.5 * (I2 - gx) * u
            D[b:b+2, a:a+2] += -0.5 * (I2 + gx) * np.conj(u)
            if t in Ut:
                b = idx(x, t + 1); u = Ut[t][x]
                D[a:a+2, b:b+2] += -0.5 * (I2 - gt) * u
                D[b:b+2, a:a+2] += -0.5 * (I2 + gt) * np.conj(u)
    return D
Fx = np.zeros((Lx, N, N), complex); Bx = np.zeros((Lx, N, N), complex)
for x in range(Lx):
    a = idx(x, 0); b = idx(x, 1)
    Fx[x, a:a+2, b:b+2] = -0.5 * (I2 - gt)
    Bx[x, b:b+2, a:a+2] = -0.5 * (I2 + gt)

rng = np.random.default_rng(23)
def rand_half(s):
    return {"Ux": {t: np.exp(1j * rng.normal(0, s, Lx)) for t in plus},
            "Ut": {t: np.exp(1j * rng.normal(0, s, Lx)) for t in [1, 2, 3]}}
def links(ua, ub):
    Ux = {}; Ut = {}
    for t in plus:
        Ux[t] = ua["Ux"][t]; Ux[theta(t)] = ub["Ux"][t]
    for t in [1, 2, 3]:
        Ut[t] = ua["Ut"][t]; Ut[-t] = np.conj(ub["Ut"][t])
    return Ux, Ut

m = 0.05; M = 1.0
def logdets(D0, phis, op):
    out = []
    for c in range(0, len(phis), 256):
        ph = phis[c:c+256]
        e = np.exp(1j * ph)
        D = D0[None] + np.einsum('px,xij->pij', e, Fx) + np.einsum('px,xij->pij', np.conj(e), Bx)
        if op == "W":
            Dm = D + m * np.eye(N)[None]
        else:
            H = np.einsum('ij,pjk->pik', G5, D - M * np.eye(N)[None])
            w, V = np.linalg.eigh(H)
            sgn = np.einsum('pij,pj,pkj->pik', V, np.sign(w), V.conj())
            Dov = np.eye(N)[None] + np.einsum('ij,pjk->pik', G5, sgn)
            Dm = (1 - m / 2) * Dov + m * np.eye(N)[None]
        sg, ld = np.linalg.slogdet(Dm)
        out.append(ld + np.log(sg))
    return np.concatenate(out)

def grid(n):
    g = 2 * np.pi * np.arange(n) / n
    return np.array(list(itertools.product(g, repeat=Lx)))

def Ztilde(U, n, op):
    k = len(U); phis = grid(n)
    L = np.zeros((k, k)); Mt = np.zeros((k, k), complex)
    for a in range(k):
        for b in range(k):
            l = logdets(DW_base(*links(U[a], U[b])), phis, op)
            lm = np.max(l.real)
            L[a, b] = lm; Mt[a, b] = np.mean(np.exp(l - lm))
    d = L.diagonal(); md = Mt.diagonal()
    assert np.all(np.abs(md.imag) < 1e-10 * np.abs(md)) and np.all(md.real > 0), md
    Zn = Mt * np.exp(L - 0.5 * (d[:, None] + d[None, :])) / np.sqrt(np.outer(md.real, md.real))
    h = np.abs(Zn - Zn.conj().T).max()
    ev = np.linalg.eigvalsh(0.5 * (Zn + Zn.conj().T))
    return ev.min() / np.abs(ev).max(), h, Zn

k = 5
print("convergence check (E, s=1.0, first set):")
U0 = [rand_half(1.0) for _ in range(k)]
for op in ["W", "O"]:
    for n in [4, 6, 8]:
        r, h, Zn = Ztilde(U0, n, op)
        if n == 6: Z6 = Zn
        if n == 8: print(f"   {op}: max |Zt(n=8) - Zt(n=6)| = {np.abs(Zn - Z6).max():.2e}")
        print(f"   op={op} n={n}: min eig/max = {r:+.4e}, herm defect {h:.1e}"); sys.stdout.flush()
for s in [0.3, 1.0]:
    for rep in range(4):
        U = U0 if (s == 1.0 and rep == 0) else [rand_half(s) for _ in range(k)]
        rW, hW, _ = Ztilde(U, 6, "W"); rO, hO, _ = Ztilde(U, 6, "O")
        print(f"s={s} set {rep}: Wilson min/max {rW:+.3e} (herm {hW:.1e}) | overlap min/max {rO:+.3e} (herm {hO:.1e})"); sys.stdout.flush()
print("done")
