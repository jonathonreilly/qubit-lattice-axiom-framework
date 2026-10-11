"""Isospectral O(eps^2) rule on non-separable flows and the E∇E tuned symbol: brute-force RK4 flow + G2 = 1/2 (grad F . v)(div v),
for F = Omega (KG).  Confirms mu = 0 independent of symbol/channel/mass; prints the range of the G2 kernel (Fourier support)."""
import numpy as np
from s2_core import grid
def hess_fd(E, de=0.02):
    v = {e: E(e) for e in [-de, -de/2, 0, de/2, de]}
    Dd = lambda e: (v[e]+v[-e]-2*v[0])/e**2
    return (4*Dd(de/2)-Dd(de))/3
def make_v(kind, ch):
    def p(K):
        kx, ky = K
        if kind == 'sin':  return [np.sin(kx), np.sin(ky)], [[np.cos(kx), 0*kx], [0*kx, np.cos(ky)]]
        if kind == 'diag': return [np.sin(kx)*np.cos(ky), np.sin(ky)*np.cos(kx)], [[np.cos(kx)*np.cos(ky), -np.sin(kx)*np.sin(ky)], [-np.sin(kx)*np.sin(ky), np.cos(kx)*np.cos(ky)]]
        if kind == 'mix':  # 0.6 sin + 0.4 diag  (non-separable, both channels anomalous)
            a, da = p_sin(K); b, db = p_diag(K)
            return [0.6*x+0.4*y for x, y in zip(a, b)], [[0.6*da[i][j]+0.4*db[i][j] for j in range(2)] for i in range(2)]
    def vel(K):
        P, D = p(K)
        if ch == 'E':  return [0.5*P[0], -0.5*P[1]], 0.5*(D[0][0]-D[1][1])
        if ch == 'T2': return [0.5*P[1], 0.5*P[0]], 0.5*(D[1][0]+D[0][1])
    return vel
p_sin = lambda K: ([np.sin(K[0]), np.sin(K[1])], [[np.cos(K[0]), 0*K[0]], [0*K[0], np.cos(K[1])]])
p_diag = lambda K: ([np.sin(K[0])*np.cos(K[1]), np.sin(K[1])*np.cos(K[0])], [[np.cos(K[0])*np.cos(K[1]), -np.sin(K[0])*np.sin(K[1])], [-np.sin(K[0])*np.sin(K[1]), np.cos(K[0])*np.cos(K[1])]])
def flow_back(Q, vel, eps, n=40):
    x = [q.copy() for q in Q]; h = eps/n
    f = lambda x: [-vv for vv in vel(x)[0]]
    for _ in range(n):
        k1 = f(x); k2 = f([a+h/2*b for a, b in zip(x, k1)]); k3 = f([a+h/2*b for a, b in zip(x, k2)]); k4 = f([a+h*b for a, b in zip(x, k3)])
        x = [a + h/6*(b1+2*b2+2*b3+b4) for a, b1, b2, b3, b4 in zip(x, k1, k2, k3, k4)]
    return x
L = 128; K = grid(2, L)
Om = lambda K, M: M*M + sum(4*np.sin(k/2)**2 for k in K)
for kind in ['sin', 'diag', 'mix']:
    for ch in ['E', 'T2']:
        vel = make_v(kind, ch); V, D = vel(K)
        G2 = 0.5*(2*np.sin(K[0])*V[0] + 2*np.sin(K[1])*V[1])*D
        Gk = np.fft.fft2(G2)/L**2; sup = np.argwhere(np.abs(Gk) > 1e-12)
        rng_ = max(max(min(i, L-i), min(j, L-j)) for i, j in sup) if len(sup) else 0
        out = []
        for M in [1.0, 0.3]:
            flow = hess_fd(lambda e: np.mean(0.5*np.sqrt(Om(flow_back(K, vel, e), M))))
            iso = hess_fd(lambda e: np.mean(0.5*np.sqrt(Om(flow_back(K, vel, e), M) + e*e*G2)))
            out.append(f"M={M}: flow {flow:+.6e}  flow+G2 {iso:+.1e}")
        print(f"p={kind:4s} {ch:2s} | " + " | ".join(out) + f" | G2 kernel range {rng_}")
