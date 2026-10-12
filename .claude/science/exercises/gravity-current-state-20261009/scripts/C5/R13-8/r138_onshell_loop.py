"""R13-8 script B.
(1) On-shell TT ranks (Lorentzian, w = +-|k|) of the invariant graviton forms: the number of
    dispersion-relevant coefficients (EH vanishes on shell; iso w^2 and iso k^2 collapse to c_T).
(2) One-loop witness: TT self-energy of a free NN lattice scalar with an O_h-covariant local
    metric vertex (not Ward-complete; see report). Extract the on-shell degree-2 TT matrix and
    the degree-0 TT matrix, fit to the invariant on-shell basis, and check that every
    P,T-even anisotropic structure is generated, and that a mass family spans all of them.
"""
import numpy as np, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "r138_forms.py")).read()
exec(src.split('out += [""]')[0])        # definitions + Part 1 (cheap)
rng = np.random.default_rng(7)

def onshell_features(mons, N, deg, dirs):
    feats = []
    for j in range(N.shape[1]):
        f = []
        for k in dirs:
            E = tt_basis(k)
            for w in (1.0, -1.0):
                p = np.concatenate([[w], k])
                f.extend((E.T @ Pi_of(N[:, j], mons, p, deg) @ E).ravel())
        feats.append(f)
    return np.array(feats)

def rank(F):
    if F.size == 0: return 0
    s = np.linalg.svd(F, compute_uv=False)
    return int((s > 1e-8 * s[0]).sum()) if s[0] > 1e-12 else 0

dirs = [v / np.linalg.norm(v) for v in rng.normal(size=(40, 3))]
res = {}
for name, grp in (("set C (O x time)", G_C), ("O_h x T", G_C_PT)):
    line = [f"[on-shell TT ranks] {name}:"]
    for deg in (0, 1, 2):
        mons, N = invariant_forms(grp, deg)
        F = onshell_features(mons, N, deg, dirs) if N.shape[1] else np.zeros((0, 0))
        r = rank(F)
        line.append(f"deg{deg}={r}")
        if deg == 2:
            Ngi = gauge_inv_basis(mons, N, deg)
            rgi = rank(onshell_features(mons, Ngi, deg, dirs))
            line.append(f"(gauge-invariant deg2 on-shell rank {rgi})")
            res[name] = (mons, N, F)
    print(" ".join(line))

# ---------------- one-loop witness ----------------
mons2, N2, F2 = res["O_h x T"]
mons0, N0 = invariant_forms(G_C_PT, 0)

def basis_onshell_matrix(mons, N, deg, dirs):
    """matrix with rows = invariant forms, columns = flattened on-shell TT features (w=+1 only,
    since P,T-even degree-2 forms are even in w)."""
    feats = []
    for j in range(N.shape[1]):
        f = []
        for k in dirs:
            E = tt_basis(k)
            p = np.concatenate([[1.0], k])
            f.extend((E.T @ Pi_of(N[:, j], mons, p, deg) @ E).ravel())
        feats.append(f)
    return np.array(feats)

def scalar_loop_tt(m, w, q, Ngrid=36):
    """Paramagnetic one-loop TT matrix for a real NN scalar, eps^2 = m^2 + sum 4 sin^2(k/2),
    vertex V_ii = 1/2[(e^{ik}-1)(e^{ik'}-1) + (1-e^{-ik})(1-e^{-ik'})], V_ij = 1/2[(i sin k_i)(i sin k'_j)+(i<->j)],
    pair (k, k' = -k-q). Returns 2x2 matrix in the TT basis of q (real symmetric part)."""
    ks = 2 * np.pi * (np.arange(Ngrid) + 0.5) / Ngrid
    K = np.stack(np.meshgrid(ks, ks, ks, indexing="ij"), -1).reshape(-1, 3)
    Kp = -K - q[None, :]
    def eps(k):
        return np.sqrt(m * m + (4 * np.sin(k / 2) ** 2).sum(-1))
    e1, e2 = eps(K), eps(Kp)
    V = np.zeros((K.shape[0], 3, 3), complex)
    for i in range(3):
        V[:, i, i] = 0.5 * ((np.exp(1j * K[:, i]) - 1) * (np.exp(1j * Kp[:, i]) - 1)
                            + (1 - np.exp(-1j * K[:, i])) * (1 - np.exp(-1j * Kp[:, i])))
        for j in range(3):
            if i != j:
                V[:, i, j] = 0.5 * ((1j * np.sin(K[:, i])) * (1j * np.sin(Kp[:, j]))
                                    + (1j * np.sin(K[:, j])) * (1j * np.sin(Kp[:, i])))
    qn = q / np.linalg.norm(q) if np.linalg.norm(q) > 0 else np.array([0, 0, 1.0])
    E = tt_basis(qn)          # 10x2 in h_A coordinates; convert to 3x3 tensors
    pol = []
    for a in range(2):
        H = np.zeros((4, 4))
        for A, (x, y) in enumerate(SYM):
            H[x, y] = E[A, a]; H[y, x] = E[A, a]
        pol.append(H[1:, 1:])
    W = np.stack([np.einsum("nij,ij->n", V, P) for P in pol], 1)       # n x 2
    F = (e1 + e2) / (e1 * e2 * ((e1 + e2) ** 2 - w * w))
    M = -np.einsum("na,nb,n->ab", W, W.conj(), F) / K.shape[0]
    return M.real, E

def onshell_deg2(m, k, d=0.04):
    """second-order on-shell part along p = s*(1, k), s -> 0, by symmetric differences."""
    k = k / np.linalg.norm(k)
    M0, _ = scalar_loop_tt(m, 0.0, 1e-9 * k)
    Mp, E = scalar_loop_tt(m, d, d * k)
    Mp2, _ = scalar_loop_tt(m, 2 * d, 2 * d * k)
    # Richardson for the s^2 coefficient: M(s) = M0 + c2 s^2 + c4 s^4
    c2a = (Mp - M0) / d ** 2; c2b = (Mp2 - M0) / (2 * d) ** 2
    return (4 * c2a - c2b) / 3, M0

# fixed directions for the fit (also used to build the basis features)
fit_dirs = [np.array(v, float) for v in ([0, 0, 1], [1, 1, 1], [1, 1, 0], [1, 2, 3], [2, 1, 0], [3, 1, 1], [1, 2, 2], [4, 1, 2])]
fit_dirs = [v / np.linalg.norm(v) for v in fit_dirs]
B2 = basis_onshell_matrix(mons2, N2, 2, fit_dirs)       # forms x features
B0 = basis_onshell_matrix(mons0, N0, 0, fit_dirs)
# reduce B2 to an independent set (on-shell rank) and identify the isotropic (c_T) direction
u, s, vt = np.linalg.svd(B2, full_matrices=False)
r2 = int((s > 1e-8 * s[0]).sum())
Bind = vt[:r2]                                           # orthonormal basis of the on-shell span
# isotropic on-shell structure = identity on TT for every direction
iso = np.concatenate([np.eye(2).ravel() for _ in fit_dirs])
iso_c = Bind @ iso                                       # coordinates of iso in Bind basis
print(f"\n[witness] on-shell P,T-even degree-2 span r={r2}; isotropic direction in span: residual "
      f"{np.linalg.norm(iso - Bind.T @ iso_c):.1e}")
# anisotropic subspace: orthogonal complement of iso within span
Q, _ = np.linalg.qr(np.column_stack([iso_c / np.linalg.norm(iso_c)] + [np.eye(r2)[:, i] for i in range(r2)]))
aniso_basis = Q[:, 1:r2]                                 # r2 x (r2-1)
u0, s0, vt0 = np.linalg.svd(B0, full_matrices=False); r0 = int((s0 > 1e-8 * s0[0]).sum()); B0ind = vt0[:r0]

rows_aniso = []; rows_mass = []
for m in (0.3, 0.6, 1.0, 2.0):
    feat2 = []; feat0 = []
    for k in fit_dirs:
        c2, M0 = onshell_deg2(m, k)
        feat2.extend(c2.ravel()); feat0.extend(M0.ravel())
    feat2 = np.array(feat2); feat0 = np.array(feat0)
    coord = Bind @ feat2
    resid = np.linalg.norm(feat2 - Bind.T @ coord) / np.linalg.norm(feat2)
    a = aniso_basis.T @ coord
    c0 = B0ind @ feat0
    resid0 = np.linalg.norm(feat0 - B0ind.T @ c0) / np.linalg.norm(feat0)
    rows_aniso.append(a); rows_mass.append(c0)
    print(f"m={m}: deg2 on-shell fit residual {resid:.1e}; c_T component {coord @ (iso_c/np.linalg.norm(iso_c)):+.4e}; "
          f"anisotropic components {np.array2string(a, precision=4)}; "
          f"mass fit residual {resid0:.1e}, TT mass components {np.array2string(c0, precision=4)}")
A = np.array(rows_aniso)
sA = np.linalg.svd(A, compute_uv=False)
print(f"[witness] anisotropic one-loop vectors over m in (0.3,0.6,1,2): singular values {np.array2string(sA, precision=3)}; "
      f"span dim {int((sA > 1e-6 * sA[0]).sum())} of {r2-1}")
Ms = np.array(rows_mass); sM = np.linalg.svd(Ms, compute_uv=False)
print(f"[witness] TT mass vectors over m: singular values {np.array2string(sM, precision=3)}; span dim {int((sM > 1e-6*sM[0]).sum())} of {r0}")
