"""Diagnostic D1 (gauge-fixed kernel on the T-X3f prime configs); (admissible-set variant, delta=0.3, chunk 64 of T-X3d): gauge-invariant RP necessary condition for the gauged overlap at beta_g = 0.
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

rng = np.random.default_rng(31)
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
GAPS = []
def logdets(D0, phis, op):
    out = []
    for c in range(0, len(phis), 64):
        ph = phis[c:c+64]
        e = np.exp(1j * ph)
        D = D0[None] + np.einsum('px,xij->pij', e, Fx) + np.einsum('px,xij->pij', np.conj(e), Bx)
        if op == "W":
            Dm = D + m * np.eye(N)[None]
        else:
            H = np.einsum('ij,pjk->pik', G5, D - M * np.eye(N)[None])
            w, V = np.linalg.eigh(H)
            GAPS.append(np.abs(w).min())
            sgn = np.einsum('pij,pj,pkj->pik', V, np.sign(w), V.conj())
            Dov = np.eye(N)[None] + np.einsum('ij,pjk->pik', G5, sgn)
            Dm = (1 - m / 2) * Dov + m * np.eye(N)[None]
        sg, ld = np.linalg.slogdet(Dm)
        out.append(ld + np.log(sg))
    return np.concatenate(out)


delta = 0.3
def wrap(a): return (a + np.pi) % (2 * np.pi) - np.pi
def nodes(ua, ub, n):
    """returns phis (P,4) and weights for the admissible crossing-link integral"""
    c = wrap(np.angle(ub["Ux"][1]) - np.angle(ua["Ux"][1]))   # Ux(x,0)=ub Ux[1]; Ux(x,1)=ua Ux[1]
    C = wrap(c.sum())
    xg, wg = np.polynomial.legendre.leggauss(n)
    P = []; W = []
    for d0, w0 in zip(delta * xg, delta * wg):
        for d1, w1 in zip(delta * xg, delta * wg):
            lo = max(-delta, C - d0 - d1 - delta); hi = min(delta, C - d0 - d1 + delta)
            if hi <= lo: continue
            for t2, w2 in zip(xg, wg):
                d2 = 0.5 * (hi - lo) * t2 + 0.5 * (hi + lo); ww = w0 * w1 * w2 * 0.5 * (hi - lo)
                p1 = d0 - c[0]; p2 = p1 + d1 - c[1]; p3 = p2 + d2 - c[2]
                P.append([0.0, p1, p2, p3]); W.append(ww)
    return np.array(P), np.array(W)
def Zadm(U, n, op):
    k = len(U); L = np.full((k, k), -np.inf); Mt = np.zeros((k, k), complex)
    for a in range(k):
        for b in range(k):
            P, W = nodes(U[a], U[b], n)
            if len(P) == 0: continue
            l = logdets(DW_base(*links(U[a], U[b])), P, op)
            lm = np.max(l.real); L[a, b] = lm; Mt[a, b] = np.sum(W * np.exp(l - lm))
    d = L.diagonal(); md = Mt.diagonal()
    assert np.all(md.real > 0) and np.all(np.abs(md.imag) < 1e-10 * md.real), md
    with np.errstate(invalid='ignore'):
        Zn = np.where(np.isfinite(L), Mt * np.exp(L - 0.5 * (d[:, None] + d[None, :])), 0) / np.sqrt(np.outer(md.real, md.real))
    ev = np.linalg.eigvalsh(0.5 * (Zn + Zn.conj().T))
    return ev.min() / np.abs(ev).max(), np.abs(Zn - Zn.conj().T).max(), Zn
def maxplaq(U):
    mp = 0
    for u in U:
        for t in [1, 2, 3]:
            for x in range(Lx):
                th = np.angle(u["Ux"][t][x]) + np.angle(u["Ut"][t][(x + 1) % Lx]) - np.angle(u["Ux"][t + 1][x]) - np.angle(u["Ut"][t][x])
                mp = max(mp, abs(wrap(th)))
    return mp

k = 5
for s in [0.15]:
    for rep in range(3):
        U = [rand_half(s) for _ in range(k)]
        out = {}
        for op in ["W", "O"]:
            L = np.zeros((k, k), complex)
            for a in range(k):
                for b in range(k):
                    L[a, b] = logdets(DW_base(*links(U[a], U[b])), np.zeros((1, Lx)), op)[0]
            d = L.diagonal().real
            Zn = np.exp(L - 0.5 * (d[:, None] + d[None, :]))
            ev = np.linalg.eigvalsh(0.5 * (Zn + Zn.conj().T))
            out[op] = (ev.min() / np.abs(ev).max(), np.abs(Zn - Zn.conj().T).max())
        print(f"s={s} set {rep}: gauge-FIXED (U_c=1) Z min/max: Wilson {out['W'][0]:+.3e} (herm {out['W'][1]:.1e}) | overlap {out['O'][0]:+.3e} (herm {out['O'][1]:.1e})")
print("done")
