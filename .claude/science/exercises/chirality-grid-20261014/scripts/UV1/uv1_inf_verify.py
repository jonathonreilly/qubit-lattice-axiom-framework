"""UV-1 V-INF (bug hunt for F1-a): recompute K_inf on a saved beta=inf torus pool with K2c's INDEPENDENT explicit-link builder
(k2c_v6_torus_verify.py: own site indexing, every plaquette from links, overlap via X (X^dag X)^(-1/2)); functions copied verbatim
from that file (lines 9-31), driver mine.  Flat crossings: a1 and y = b1 - b0 chosen from explicit plaquettes; Polyakov b0 trapezoid.
usage: python3 uv1_inf_verify.py POOL.npz NW"""
import numpy as np, sys, time
POOL = sys.argv[1]; NW = int(sys.argv[2])
d = np.load(POOL); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]; k = len(U)
T = d['ux'].shape[1]; Lx = 2; Lt = 2 * T; N = 2 * Lx * Lt; M = 1.0; m = 0.05
def wrap(a): return (a + np.pi) % (2 * np.pi) - np.pi
gx = np.array([[0, 1], [1, 0]], complex); gt = np.array([[0, -1j], [1j, 0]]); I2 = np.eye(2)
def sidx(x, ti): return 2 * (ti + Lt * (x % Lx))
def links(ua, ub, a1, b0, b1):
    UX = np.zeros((Lx, Lt)); UT = np.zeros((Lx, Lt))
    for t in range(1, T + 1):
        UX[:, t + T - 1] = ua['x'][t - 1]; UX[:, (1 - t) + T - 1] = ub['x'][t - 1]
    for t in range(1, T):
        UT[:, t + T - 1] = ua['t'][t - 1]; UT[:, (-t) + T - 1] = -ub['t'][t - 1]
    UT[:, T - 1] = [0.0, a1]; UT[:, Lt - 1] = [b0, b1]
    return UX, UT
def plaqs(UX, UT):
    return wrap(np.array([[UX[x, ti] + UT[(x + 1) % Lx, ti] - UX[x, (ti + 1) % Lt] - UT[x, ti] for x in range(Lx)] for ti in range(Lt)]))
def D_of(UX, UT):
    D = 2.0 * np.eye(N, dtype=complex)
    for x in range(Lx):
        for ti in range(Lt):
            a = sidx(x, ti); b = sidx(x + 1, ti); u = np.exp(1j * UX[x, ti])
            D[a:a+2, b:b+2] += -0.5 * (I2 - gx) * u; D[b:b+2, a:a+2] += -0.5 * (I2 + gx) * np.conj(u)
            b = sidx(x, (ti + 1) % Lt); u = (-1.0 if ti == Lt - 1 else 1.0) * np.exp(1j * UT[x, ti])
            D[a:a+2, b:b+2] += -0.5 * (I2 - gt) * u; D[b:b+2, a:a+2] += -0.5 * (I2 + gt) * np.conj(u)
    return D
G5 = np.kron(np.eye(N // 2), np.diag([1., -1.]))
def logdet(D, op):
    if op == 'W': s, l = np.linalg.slogdet(D + m * np.eye(N)); return l + np.log(complex(s)), np.inf
    X = D - M * np.eye(N); w, V = np.linalg.eigh(X.conj().T @ X)
    gap = np.abs(np.linalg.eigvalsh(G5 @ X)).min()
    Dov = np.eye(N) + X @ (V * (1 / np.sqrt(w))) @ V.conj().T
    s, l = np.linalg.slogdet((1 - m / 2) * Dov + m * np.eye(N)); return l + np.log(complex(s)), gap
t00 = time.time(); bw = 2 * np.pi * np.arange(NW) / NW; maxflat = 0.0
for op in ('O', 'W'):
    Lm = np.zeros((k, k), complex); gmin = np.inf
    for a in range(k):
        for b in range(a, k):
            P0 = plaqs(*links(U[a], U[b], 0.0, 0.0, 0.0)); a1 = -P0[T - 1, 0]; y = -P0[Lt - 1, 0]
            vals = []
            for b0 in bw:
                UX, UT = links(U[a], U[b], a1, b0, b0 + y)
                if b0 == 0.0:
                    P = plaqs(UX, UT); maxflat = max(maxflat, np.abs(P[[T - 1, Lt - 1]]).max())
                    near = [T - 2, T, Lt - 2, 0]          # rows adjacent to the planes (buffer gaps when t0 >= 2)
                v, g = logdet(D_of(UX, UT), op); vals.append(v); gmin = min(gmin, g)
            l = np.array(vals); lm = l.real.max(); Lm[a, b] = lm + np.log(np.mean(np.exp(l - lm)) + 0j); Lm[b, a] = np.conj(Lm[a, b])
    dd = Lm.diagonal().real; Z = np.exp(Lm - 0.5 * (dd[:, None] + dd[None, :])); ev = np.linalg.eigvalsh(0.5 * (Z + Z.conj().T))
    print(f"V-INF {op} nw={NW}: k={k} lam_min {ev[0]:+.5e} min/max {ev[0]/ev[-1]:+.4e} | max |crossing plaquette| {maxflat:.1e}"
          + (f" | min|eig H_W| {gmin:.3f}" if op == 'O' else "") + f" [{time.time()-t00:.0f}s]", flush=True)
print("done")
