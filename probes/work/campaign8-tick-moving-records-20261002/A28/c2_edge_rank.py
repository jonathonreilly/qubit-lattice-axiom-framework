"""A28 c2: Reeh-Schlieder at the EDGE of a recorded region (supplied free-fermion toys).

Under Option R a record is a wall for the possibilities (A27 Step 1a).  Question: is the
sea's marginal on the UNRECORDED part of a star next to a wall still full rank?  If yes, every
nonzero gated weight F^(R) forms records there at a positive rate (positivity, A12 L1).

(1) 1D half-filled hopping chain (the 1D staggered/massless-Dirac sea), hard wall at the left:
    unrecorded star part of the wall-adjacent site = {0, 1}.  Bulk star {i-1,i,i+1} for contrast.
(2) 3D simple-cubic half-filled sea, planar wall (open boundary in z), periodic in x,y:
    unrecorded star part of a wall-adjacent site = 6 sites.  Bulk 7-site star for contrast.
Many-body marginal of a Gaussian state: smallest eigenvalue = prod_i min(nu_i, 1-nu_i).
(3) Energy injected by one sharp formation (Lueders cut of n_0) at the wall-adjacent site in 1D,
    averaged over the two lock outcomes: (a) under the old generator, (b) above the new
    ground state of the compressed generator (site 0 becomes a second wall).
"""
import signal
import numpy as np
signal.alarm(55)


def chain_C(N, nocc):
    h = np.zeros((N, N))
    for i in range(N - 1):
        h[i, i + 1] = h[i + 1, i] = -1.0
    e, v = np.linalg.eigh(h)
    C = v[:, :nocc] @ v[:, :nocc].T  # C_ij = <c_i^dag c_j> (real)
    return h, C, e


def mb_min(nu):
    return float(np.prod(np.minimum(nu, 1 - nu)))


print('(1) 1D half-filled chain, open (wall) left end')
for N in (200, 400, 800):
    h, C, _ = chain_C(N, N // 2)
    nu_w = np.linalg.eigvalsh(C[np.ix_([0, 1], [0, 1])])
    m = N // 2
    nu_b = np.linalg.eigvalsh(C[np.ix_([m - 1, m, m + 1], [m - 1, m, m + 1])])
    print(f'  N={N}: wall-adjacent star nu = {np.round(nu_w, 6)}  min MB eig = {mb_min(nu_w):.4e} | '
          f'bulk star nu = {np.round(nu_b, 6)}  min MB eig = {mb_min(nu_b):.4e}')

print('(2) 3D simple-cubic half-filled sea, planar wall at z=-1, periodic x,y')
for Lxy, Lz in ((16, 32), (24, 48)):
    ks = 2 * np.pi * np.arange(Lxy) / Lxy
    # star of wall-adjacent site r0=(0,0,0): (+-1,0,0),(0,+-1,0),(0,0,1); bulk star around (0,0,Lz//2)
    zb = Lz // 2
    sites_w = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    sites_b = [(0, 0, zb), (1, 0, zb), (-1, 0, zb), (0, 1, zb), (0, -1, zb), (0, 0, zb + 1), (0, 0, zb - 1)]
    hz = np.zeros((Lz, Lz))
    for i in range(Lz - 1):
        hz[i, i + 1] = hz[i + 1, i] = -1.0
    ez, vz = np.linalg.eigh(hz)
    Cw = np.zeros((6, 6), dtype=complex); Cb = np.zeros((7, 7), dtype=complex)
    nocc = 0
    for kx in ks:
        for ky in ks:
            eps = -2 * (np.cos(kx) + np.cos(ky)) + ez
            occ = eps < 0
            nocc += occ.sum()
            Pz = vz[:, occ] @ vz[:, occ].T
            for C, sl in ((Cw, sites_w), (Cb, sites_b)):
                for a, (xa, ya, za) in enumerate(sl):
                    for b, (xb, yb, zbb) in enumerate(sl):
                        C[a, b] += np.exp(-1j * (kx * (xa - xb) + ky * (ya - yb))) * Pz[za, zbb]
    Cw /= Lxy ** 2; Cb /= Lxy ** 2
    nu_w = np.linalg.eigvalsh(Cw); nu_b = np.linalg.eigvalsh(Cb)
    print(f'  L={Lxy}x{Lxy}x{Lz} filling {nocc / (Lxy * Lxy * Lz):.4f}: wall star nu in [{nu_w.min():.4f},{nu_w.max():.4f}] '
          f'min MB eig {mb_min(nu_w):.3e} | bulk 7-star nu in [{nu_b.min():.4f},{nu_b.max():.4f}] min MB eig {mb_min(nu_b):.3e}')

print('(3) energy injected by one sharp lock at the wall-adjacent site (1D, units of hopping J)')
for N in (200, 400, 800):
    h, C, e = chain_C(N, N // 2)
    E0 = np.sum(h * C)
    p1 = C[0, 0]
    d0 = np.zeros(N); d0[0] = 1
    # Lueders lock of n_0: block i,j != 0 from Wick; coherences with site 0 are removed
    C1 = C - np.outer(C[:, 0], C[0, :]) / p1               # lock n_0 = 1
    C0 = C + np.outer(C[:, 0], C[0, :]) / (1 - p1)         # lock n_0 = 0
    for Cp, occ0 in ((C1, 1.0), (C0, 0.0)):
        Cp[0, :] = 0.0; Cp[:, 0] = 0.0; Cp[0, 0] = occ0
    avg = p1 * C1 + (1 - p1) * C0
    assert abs(avg[0, 1]) < 1e-14 and np.allclose(avg[1:, 1:], C[1:, 1:])
    dE_old = p1 * (np.sum(h * C1) - E0) + (1 - p1) * (np.sum(h * C0) - E0)
    # compressed generator: site 0 decoupled; remaining chain sites 1..N-1 at fixed number
    hr = h[1:, 1:]
    er = np.linalg.eigvalsh(hr)
    exc = 0.0
    for p, Cp, n0 in ((p1, C1, 1), (1 - p1, C0, 0)):
        Erest = np.sum(hr * Cp[1:, 1:])
        Egs = er[:N // 2 - n0].sum()
        exc += p * (Erest - Egs)
    print(f'  N={N}: P(lock 1)={p1:.6f}  mean dE under old generator = {dE_old:.6f} J ; '
          f'mean excess above new walled ground state = {exc:.6f} J ; 2*C_01 = {2*C[0,1]:.6f}')
