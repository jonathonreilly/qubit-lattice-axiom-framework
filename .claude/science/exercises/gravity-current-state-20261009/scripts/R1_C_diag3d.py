"""C: diagnose 3D periodic Delaunay consistency (total volume, row sums, linear precision)."""
import numpy as np
src = open("B_liquid_glass_crystal.py").read().split("which = sys.argv")[0]
ns = {}; exec(src, ns)
rng = np.random.default_rng(3)
N = 1000; L = N ** (1/3); A0 = L*np.eye(3)
X = rng.uniform(0, L, size=(N, 3))
S = np.diag([1.0, -1.0, 0.0])
for e in (0.0, 0.02, 0.04, 0.06):
    M = ns["expm_sym"](S, e); Y, A = X @ M.T, A0 @ M.T
    vid, voff = ns["periodic_delaunay"](Y, A)
    pos = Y[vid] + np.einsum("tvk,kl->tvl", voff, A)
    D = pos[:, 1:, :] - pos[:, :1, :]
    vol = np.abs(np.linalg.det(D)) / 6
    K = ns["stiffness"](Y, A, vid, voff)
    # linear precision: for affine u = a.x on the torus use the periodic-gradient test: energy of
    # the cochain du_e = a.(edge vector) should equal |a|^2 * Vol for a consistent mesh
    a = np.array([0.3, -0.5, 0.8])
    Ga = 0.0
    for t in range(len(vid)):
        pass
    Dinv = np.linalg.inv(D)
    grads = np.concatenate([-Dinv.sum(axis=2, keepdims=True), Dinv], axis=2)   # T x 3 x 4
    u = pos @ a                                                                 # T x 4
    gu = np.einsum("tka,ta->tk", grads, u)                                      # gradient per tet
    lin_err = np.abs(gu - a).max()
    E_lin = (vol * (gu**2).sum(1)).sum()
    lam = np.linalg.eigvalsh(K)
    print(f"eps={e:+.2f} ntet={len(vid)} sumvol={vol.sum():.6f} detA={abs(np.linalg.det(A)):.6f} "
          f"minvol={vol.min():.2e} rowsum_max={np.abs(K.sum(1)).max():.1e} lin_grad_err={lin_err:.1e} "
          f"E_lin/(|a|^2 V)={E_lin/((a@a)*abs(np.linalg.det(A))):.6f} lam_min={lam[0]:.2e} lam_max={lam[-1]:.2e}")
