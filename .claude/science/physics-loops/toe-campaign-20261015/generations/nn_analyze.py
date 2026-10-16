import numpy as np, itertools, sys, glob
import coinrep as CR
S = [tuple(v) for v in CR.stencil('cube')]
B = np.load('blockreps.npy'); DZ, DX = B[3]
RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
for f in sorted(glob.glob('blockNN_block3_hit*.npy')):
    A = np.load(f); W = lambda k: sum(a * np.exp(1j * np.dot(k, n)) for a, n in zip(A, S))
    rng = np.random.default_rng(1)
    eu = max(np.abs(W(k) @ W(k).conj().T - np.eye(8)).max() for k in rng.uniform(-np.pi, np.pi, (100, 3)))
    ec = max(np.abs(W(R @ k) - D @ W(k) @ D.T).max() for R, D in ((RZ, DZ), (RX, DX)) for k in rng.uniform(-np.pi, np.pi, (30, 3)))
    # gap closings: minimise min quasienergy over BZ (grid), relative to the k=0 spectrum's global phase
    w0 = np.angle(np.linalg.eigvals(W(np.zeros(3))))
    print(f, 'unitarity', f'{eu:.1e}', 'covariance', f'{ec:.1e}', 'U(0) eigen-phases', np.round(np.sort(w0), 3))
    # remove a global phase so that U(0) eigenphases are centred: find degeneracy points of the spectrum (band touchings)
    tg = np.linspace(-np.pi, np.pi, 17)
    best = []
    for k in itertools.product(tg, tg, tg):
        ph = np.sort(np.angle(np.linalg.eigvals(W(np.array(k)))))
        gaps = np.diff(np.concatenate([ph, [ph[0] + 2 * np.pi]]))
        best.append((gaps.min(), k))
    best.sort(key=lambda t: t[0])
    print('   smallest band gaps on grid:', [(round(g, 4), tuple(np.round(k, 2))) for g, k in best[:6]])
    # dispersion near k = 0
    for d in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        d = np.array(d) / np.linalg.norm(d); e = 1e-3
        p0 = np.sort(np.angle(np.linalg.eigvals(W(np.zeros(3))))); p1 = np.sort(np.angle(np.linalg.eigvals(W(e * d))))
        print('   direction', np.round(d, 3), 'eigenphase slopes', np.round((p1 - p0) / e, 3))
