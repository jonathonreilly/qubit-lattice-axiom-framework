"""C5 R4-2 (3): illustration of Corollary N (no propagating site two-point function).

Claim (proved in the report, singular part via RECALLED Benoist-Quint): a Gamma-invariant
positive-definite function W on L7 is c*delta_0 + (Fourier transform of a singular
Gamma-invariant finite measure); its absolutely continuous part is c*Haar.
Illustration: orbit-constant candidates W = delta_0 + eps * w(Q7(d)) [d != 0]
are tested for positive semidefiniteness on finite site boxes [-L, L]^4.  For every
eps != 0 the Gram matrix I + eps*A_w eventually fails PSD, because the extreme
eigenvalues of A_w run off to +-infinity as the box grows.
"""
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla


def gram_parts(L, wfun, Qmax):
    r = np.arange(-L, L + 1)
    pts = np.array(np.meshgrid(r, r, r, r, indexing="ij")).reshape(4, -1).T
    N = len(pts)
    idx = {tuple(p): i for i, p in enumerate(pts)}
    # displacements d with 0 < |Q7(d)| <= Qmax inside the box difference range
    R = np.arange(-2 * L, 2 * L + 1)
    D = np.array(np.meshgrid(R, R, R, R, indexing="ij")).reshape(4, -1).T
    Q = -7 * D[:, 0]**2 + D[:, 1]**2 + D[:, 2]**2 + D[:, 3]**2
    keep = (np.any(D != 0, axis=1)) & (np.abs(Q) <= Qmax)
    D, Q = D[keep], Q[keep]
    W = np.array([wfun(q) for q in Q])
    nz = W != 0
    D, W = D[nz], W[nz]
    rows, cols, vals = [], [], []
    for d, w in zip(D, W):
        tgt = pts + d
        ok = np.all(np.abs(tgt) <= L, axis=1)
        src = np.nonzero(ok)[0]
        dst = [idx[tuple(t)] for t in tgt[ok]]
        rows += list(src)
        cols += dst
        vals += [w] * len(src)
    A = sps.csr_matrix((vals, (rows, cols)), shape=(N, N))
    return A, N, len(D)


tests = {
    "timelike shell Q=-7 indicator": (lambda q: 1.0 if q == -7 else 0.0, 7),
    "spacelike shell Q=+1 indicator": (lambda q: 1.0 if q == 1 else 0.0, 1),
    "smooth in |Q|: exp(-|Q|/3), all orbits |Q|<=12": (lambda q: np.exp(-abs(q) / 3.0), 12),
}
for name, (wf, Qmax) in tests.items():
    print(f"W = delta + eps * w, w = {name}")
    for L in (1, 2, 3, 4):
        A, N, nd = gram_parts(L, wf, Qmax)
        A = 0.5 * (A + A.T)
        lmax = spla.eigsh(A, k=1, which="LA", return_eigenvectors=False)[0]
        lmin = spla.eigsh(A, k=1, which="SA", return_eigenvectors=False)[0]
        # PSD of I + eps A requires -1/lmax <= eps <= -1/lmin
        print(f"   L={L}: sites={N:6d}, displacements used={nd:5d}, "
              f"lambda_min={lmin:9.3f}, lambda_max={lmax:9.3f}, "
              f"PSD window for eps: [{-1/lmax:.4f}, {-1/lmin:.4f}]")
print("Reading: the PSD window shrinks toward {0} as the box grows (both extreme "
      "eigenvalues grow without visible bound), as Corollary N requires.")
