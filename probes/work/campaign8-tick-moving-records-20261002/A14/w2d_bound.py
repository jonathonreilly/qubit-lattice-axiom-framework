"""A14 check N2c: does one wall bind a massive ripple (eigenphase inside the gap)?
Builds the one-tick unitary U_1 of the 2D conveyor walk (w2d_walls.step) with one wall
on an L x L torus, column by column, and lists eigen-quasi-energies with |w| < gap edge."""
import sys, signal, time
import numpy as np
import w2d_walls as W
signal.alarm(58)
L = int(sys.argv[1]); m = float(sys.argv[2])
t0 = time.time()
for r in (1j, 1.0):
    Wm = np.zeros((L, L)); Wm[L//2, L//2] = 1.0; F = 1 - Wm
    free = np.where(F.ravel() > 0)[0]
    n = 2*len(free)
    # basis vectors: component c at free site
    basis = np.zeros((n, 2, L, L), complex)
    for i, s in enumerate(free):
        x, y = divmod(s, L)
        basis[2*i, 0, x, y] = 1; basis[2*i+1, 1, x, y] = 1
    out = np.zeros((n, n), complex)
    B = 512
    for a in range(0, n, B):
        ps = W.step(W.mass(basis[a:a+B], m), F, Wm, r)
        flat = ps.reshape(ps.shape[0], 2, L*L)[:, :, free]          # (b,2,nfree)
        out[:, a:a+B] = flat.transpose(0, 2, 1).reshape(ps.shape[0], n).T
    ev = np.linalg.eigvals(out)
    w = -np.angle(ev)
    print(f"r={r} m={m} L={L}: unitarity |U^dag U - 1| = {np.abs(out.conj().T@out - np.eye(n)).max():.1e}")
    # clean gap edge: min over k of upper band, computed on the same grid
    ks = 2*np.pi*np.arange(L)/L
    om = np.array([abs(W.upper(kx, ky, m)[0]) for kx in ks for ky in ks])
    gap = om.min()
    ing = np.sort(w[np.abs(w) < gap - 1e-9])
    print(f"   clean gap edge |w|min = {gap:.4f}; eigenphases strictly inside the gap: {np.round(ing, 4)}")
print(f"elapsed {time.time()-t0:.1f}s")
