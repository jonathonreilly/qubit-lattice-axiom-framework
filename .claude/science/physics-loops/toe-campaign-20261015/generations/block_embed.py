import numpy as np, itertools
from scipy.linalg import null_space, polar
import coinrep as CR
B = np.load('blockreps.npy'); DZb, DXb = B[3].astype(complex)
(Rz, Ez), (Rx, Ex) = CR.rep('spin1/2(x)E')          # E (x) D_1/2, 4-dim
R2z, R2x = np.kron(np.eye(2), Ez), np.kron(np.eye(2), Ex)   # flavor (x) E (x) spin
best = None
for sz in (1, -1, 1j, -1j):
    for sx in (1, -1, 1j, -1j):
        M = np.vstack([np.kron(np.eye(8), DZb) - np.kron((sz * R2z).T, np.eye(8)), np.kron(np.eye(8), DXb) - np.kron((sx * R2x).T, np.eye(8))])
        Ns = null_space(M)
        if Ns.shape[1] >= 4:
            best = (sz, sx, Ns); break
    if best: break
sz, sx, Ns = best
rng = np.random.default_rng(0)
T = (Ns @ rng.normal(size=Ns.shape[1])).reshape(8, 8, order='F')
T, _ = polar(T)                                      # unitary intertwiner
print('phases', sz, sx, 'hom dim', Ns.shape[1], 'intertwining error', np.abs(DZb @ T - T @ (sz * R2z)).max(), np.abs(DXb @ T - T @ (sx * R2x)).max())
# two-qubit Dirac walk coefficients (coin 1 (x) D_1/2 on flavor (x) spin)
A2 = np.load('hits2q_massless_A.npy')[0]; S = [tuple(v) for v in CR.stencil('cube')]
# reorder flavor (x) spin (x) E  ->  flavor (x) E (x) spin
Pm = np.zeros((8, 8))
for f in range(2):
    for s in range(2):
        for e in range(2):
            Pm[f * 4 + e * 2 + s, f * 4 + s * 2 + e] = 1
A8 = np.array([T @ Pm @ np.kron(A, np.eye(2)) @ Pm.T @ T.conj().T for A in A2])
def W(k): return sum(A * np.exp(1j * np.dot(k, n)) for A, n in zip(A8, S))
err_u = max(np.abs(W(k) @ W(k).conj().T - np.eye(8)).max() for k in rng.uniform(-np.pi, np.pi, (200, 3)))
RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
err_c = 0
for R, D in ((RZ, DZb), (RX, DXb)):
    for k in rng.uniform(-np.pi, np.pi, (50, 3)):
        err_c = max(err_c, np.abs(W(R @ k) - D @ W(k) @ D.conj().T).max())
mov = sum(np.abs(A).sum() for A, n in zip(A8, S) if n != (0, 0, 0))
print('unitarity error', err_u, ' block covariance error', err_c, ' moving weight', mov)
for kk in ([0.05, 0, 0], [0.05, 0.05, 0.05], [0.1, 0, 0]):
    ev = np.sort(np.abs(np.angle(np.linalg.eigvals(W(np.array(kk))))))
    print('k =', kk, '|k| =', round(float(np.linalg.norm(kk)), 4), 'quasienergies / |k|:', np.round(ev / np.linalg.norm(kk), 4))
tg = np.linspace(-np.pi, np.pi, 25); mins = []
for k in __import__('itertools').product(tg, tg, tg):
    if np.linalg.norm(k) < 1e-9: continue
    mins.append((np.abs(np.angle(np.linalg.eigvals(W(np.array(k))))).min(), np.linalg.norm(k)))
mins = np.array(mins); print('smallest quasienergy away from k=0 on 25^3 grid:', mins[:, 0][mins[:, 1] > 0.5].min())
np.save('block3_dirac_A.npy', A8)
