"""R13-8 script A: invariant counts for set C (Z^3 x R, proper cubic O, time fixed).

Part 1: matter/photon SME-type tensors (invariant dims under O, time fixed).
Part 2: graviton quadratic forms Pi(p) on h_{mu nu} (10 comps) of degree 0,1,2 in p=(w,k),
        invariant under the group; gauge-invariant subspace under linearized diffeo
        delta h_{mu nu} = p_mu xi_nu + p_nu xi_mu  (condition Pi(p) G(p) = 0);
        TT-restricted rank (polarization matrices on the 2 TT modes).
Validation: W(B4) on Z^4 must give K1's 3 mass + 9 two-derivative forms, codim 11, TT rank 5.
"""
import itertools, numpy as np
rng = np.random.default_rng(1)

# ---------- groups ----------
def signed_perms(n, proper_only):
    out = []
    for perm in itertools.permutations(range(n)):
        for signs in itertools.product([1, -1], repeat=n):
            M = np.zeros((n, n))
            for i, j in enumerate(perm):
                M[i, j] = signs[i]
            if proper_only and round(np.linalg.det(M)) != 1:
                continue
            out.append(M)
    return out

O3 = signed_perms(3, True)          # 24 proper cubic rotations
Oh3 = signed_perms(3, False)        # 48 with inversion
assert len(O3) == 24 and len(Oh3) == 48
def lift(R):                        # time fixed
    M = np.eye(4); M[1:, 1:] = R; return M
G_C = [lift(R) for R in O3]                       # axioms' group (set C)
G_C_PT = [lift(R) for R in Oh3]                   # + parity; T handled separately
TREV = np.diag([-1., 1, 1, 1])                    # time reversal on indices
G_C_PT = G_C_PT + [TREV @ g for g in G_C_PT]      # O_h x T (index action)
WB4 = signed_perms(4, False)                      # 384
WB4p = signed_perms(4, True)                      # 192

# ---------- Part 1: tensor invariants ----------
def inv_dim(group, rank, sym=None):
    """dimension of invariant tensors of given rank (indices 0..3), with an optional
    projector 'sym' acting on the flattened tensor space."""
    n = 4 ** rank
    P = np.zeros((n, n))
    for g in group:
        T = g
        for _ in range(rank - 1):
            T = np.kron(T, g)
        P += T
    P /= len(group)
    if sym is not None:
        P = P @ sym
    return int(round(np.linalg.matrix_rank(P, tol=1e-9)))

def perm_op(rank, perm):
    n = 4 ** rank
    M = np.zeros((n, n))
    for idx in itertools.product(range(4), repeat=rank):
        src = np.ravel_multi_index(idx, (4,) * rank)
        dst = np.ravel_multi_index(tuple(idx[p] for p in perm), (4,) * rank)
        M[dst, src] = 1
    return M

I2 = np.eye(16)
S2 = (I2 + perm_op(2, (1, 0))) / 2
A2 = (I2 - perm_op(2, (1, 0))) / 2
I3 = np.eye(64)
A3_01 = (I3 - perm_op(3, (1, 0, 2))) / 2          # g_{lambda mu nu}, antisym in lambda mu

def report_tensors(group, name):
    lines = [f"[{name}] |G|={len(group)}"]
    lines.append(f"  vector (a_mu,b_mu,e_mu,f_mu,(k_AF)_mu): {inv_dim(group,1)}")
    lines.append(f"  sym rank-2 (c_(mu nu), d_(mu nu)): {inv_dim(group,2,S2)}")
    lines.append(f"  antisym rank-2 (c_[mu nu], d_[mu nu], H_mu nu): {inv_dim(group,2,A2)}")
    lines.append(f"  g_{{lambda mu nu}} antisym in (lambda mu): {inv_dim(group,3,A3_01)}")
    return lines

out = []
out += report_tensors(G_C, "set C: proper O, time fixed")
out += report_tensors([lift(R) for R in Oh3], "O_h, time fixed (parity added)")
# photon: symmetric bilinear forms on (E,B) in R^6 under proper O (E,B both vectors under proper rotations)
def eb_forms(Rs, parity):
    n = 6
    rows = []
    basis = [(i, j) for i in range(n) for j in range(i, n)]
    for R in Rs:
        for P in ([False, True] if parity else [False]):
            D = np.zeros((6, 6)); D[:3, :3] = R; D[3:, 3:] = R
            if P:
                D[:3, :3] = -R; D[3:, 3:] = R   # E polar, B axial
            for _ in range(3):
                x = rng.normal(size=6); y = D @ x
                rows.append([y[i]*y[j] - x[i]*x[j] for (i, j) in basis])
    A = np.array(rows)
    return len(basis) - np.linalg.matrix_rank(A, tol=1e-9)
out.append(f"  photon: O-invariant quadratic forms on (E,B): {eb_forms(O3, False)} (E.E, B.B, E.B)")
out.append(f"  photon: O_h-invariant quadratic forms on (E,B): {eb_forms(O3, True)}")

# ---------- Part 2: graviton forms ----------
SYM = [(a, b) for a in range(4) for b in range(a, 4)]           # 10 components of h
def hvec(H):
    return np.array([H[a, b] for (a, b) in SYM])
def Gmat(p):
    """10x4: delta h_A = (p_a xi_b + p_b xi_a) for A=(a,b)."""
    G = np.zeros((10, 4))
    for A, (a, b) in enumerate(SYM):
        G[A, b] += p[a]
        G[A, a] += p[b]
    return G

def monomials(deg):
    """List of (A,B,mus) monomial labels for Pi^{AB}(p). For even deg Pi symmetric (A<=B),
    for odd deg antisymmetric (A<B)."""
    pairs = [(A, B) for A in range(10) for B in range(A, 10)] if deg % 2 == 0 else \
            [(A, B) for A in range(10) for B in range(A + 1, 10)]
    mus = list(itertools.combinations_with_replacement(range(4), deg))
    return [(A, B, m) for (A, B) in pairs for m in mus]

def Pi_of(coeffs, mons, p, deg):
    Pi = np.zeros((10, 10))
    for c, (A, B, m) in zip(coeffs, mons):
        if c == 0: continue
        v = c * np.prod([p[i] for i in m]) if m else c
        if deg % 2 == 0:
            Pi[A, B] += v
            if A != B: Pi[B, A] += v
        else:
            Pi[A, B] += v; Pi[B, A] -= v
    return Pi

def basis_Pi(mons, p, deg):
    """returns array (nmon, 10, 10) of Pi for each monomial at momentum p."""
    out = np.zeros((len(mons), 10, 10))
    for k, (A, B, m) in enumerate(mons):
        v = np.prod([p[i] for i in m]) if m else 1.0
        if deg % 2 == 0:
            out[k, A, B] += v
            if A != B: out[k, B, A] += v
        else:
            out[k, A, B] += v; out[k, B, A] -= v
    return out

def hrep(g):
    """10x10 matrix: h -> g h g^T in the SYM basis (h_A coordinates)."""
    M = np.zeros((10, 10))
    for B, (a, b) in enumerate(SYM):
        H = np.zeros((4, 4)); H[a, b] = 1; H[b, a] = 1
        if a == b: H[a, b] = 1
        Hn = g @ H @ g.T
        # coordinates: h_A = H[a,b]
        M[:, B] = hvec(Hn)
    return M

def invariant_forms(group, deg, nsamp=None):
    mons = monomials(deg)
    nm = len(mons)
    # Pi invariant: Pi(g p) = R(g)^{-T} Pi(p) R(g)^{-1} in h-coordinates, where h' = R h.
    # Equivalent: h'^T Pi(gp) h' = h^T Pi(p) h  for h' = R h (as a quadratic/bilinear form).
    gens = group
    rows = []
    ns = nsamp or max(4, (2 * nm) // len(gens) + 4)
    for g in gens:
        R = hrep(g)
        for _ in range(ns):
            p = rng.normal(size=4)
            B0 = basis_Pi(mons, p, deg)
            B1 = basis_Pi(mons, g @ p, deg)
            h1 = rng.normal(size=10); h2 = rng.normal(size=10)
            # bilinear values
            v0 = np.einsum('kab,a,b->k', B0, h1, h2)
            v1 = np.einsum('kab,a,b->k', B1, R @ h1, R @ h2)
            rows.append(v1 - v0)
    A = np.array(rows)
    u, s, vt = np.linalg.svd(A, full_matrices=True)
    rank = int((s > 1e-8 * s[0]).sum())
    N = vt[rank:].T          # nm x ninv
    return mons, N

def gauge_invariant_subspace(mons, N, deg, nsamp=60):
    rows = []
    for _ in range(nsamp):
        p = rng.normal(size=4)
        B = basis_Pi(mons, p, deg)               # nm x10x10
        G = Gmat(p)
        xi = rng.normal(size=4); h1 = rng.normal(size=10)
        v = np.einsum('kab,a,b->k', B, h1, G @ xi)
        rows.append(v)
    A = np.array(rows) @ N
    s = np.linalg.svd(A, compute_uv=False)
    rank = int((s > 1e-8 * max(s[0], 1e-300)).sum()) if len(s) else 0
    return N.shape[1] - rank

def tt_basis(k):
    """two orthonormal symmetric traceless transverse 3x3 matrices, embedded into 10-vectors."""
    k = k / np.linalg.norm(k)
    a = np.array([1.0, 0, 0]) if abs(k[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = a - k * (a @ k); e1 /= np.linalg.norm(e1); e2 = np.cross(k, e1)
    P = (np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(2)
    X = (np.outer(e1, e2) + np.outer(e2, e1)) / np.sqrt(2)
    E = []
    for M in (P, X):
        H = np.zeros((4, 4)); H[1:, 1:] = M
        E.append(hvec(H))
    return np.array(E).T      # 10x2  (h_A coordinates; off-diagonal stored once)

def tt_rank(mons, N, deg, nsamp=40):
    feats = []
    pts = [(rng.normal(), rng.normal(size=3)) for _ in range(nsamp)]
    for j in range(N.shape[1]):
        coeffs = N[:, j]
        f = []
        for (w, k) in pts:
            p = np.concatenate([[w], k])
            Pi = Pi_of(coeffs, mons, p, deg)
            E = tt_basis(k)
            # note: h_A coordinates with off-diagonal stored once; the bilinear form h^T Pi h uses
            # the same coordinates, so E is a legitimate 2-dim subspace of h-space.
            M = E.T @ Pi @ E
            f.extend(M.ravel())
        feats.append(f)
    F = np.array(feats)
    s = np.linalg.svd(F, compute_uv=False)
    return int((s > 1e-8 * s[0]).sum()) if F.size else 0

def tt_rank_split(mons, N, deg, nsamp=40):
    """For degree 2: TT ranks of the w^2, w k and k^2 parts separately and jointly."""
    res = {}
    for part in ("ww", "wk", "kk", "all"):
        feats = []
        pts = [rng.normal(size=3) for _ in range(nsamp)]
        for j in range(N.shape[1]):
            coeffs = N[:, j]; f = []
            for k in pts:
                E = tt_basis(k)
                def M_at(w, kk):
                    return E.T @ Pi_of(coeffs, mons, np.concatenate([[w], kk]), deg) @ E
                Mww = (M_at(1, 0 * k) )               # w^2 coefficient (k=0 part), p=(1,0,0,0)
                Mkk = M_at(0, k)
                Mwk = (M_at(1, k) - M_at(-1, k)) / 2  # odd in w part
                if part == "ww": f.extend(Mww.ravel())
                elif part == "kk": f.extend(Mkk.ravel())
                elif part == "wk": f.extend(Mwk.ravel())
                else: f.extend(np.concatenate([Mww.ravel(), Mwk.ravel(), Mkk.ravel()]))
            feats.append(f)
        F = np.array(feats)
        s = np.linalg.svd(F, compute_uv=False)
        res[part] = int((s > 1e-8 * s[0]).sum()) if (F.size and s[0] > 1e-12) else 0
    return res

def gauge_inv_basis(mons, N, deg, nsamp=80):
    rows = []
    for _ in range(nsamp):
        p = rng.normal(size=4)
        B = basis_Pi(mons, p, deg); G = Gmat(p)
        xi = rng.normal(size=4); h1 = rng.normal(size=10)
        rows.append(np.einsum('kab,a,b->k', B, h1, G @ xi))
    A = np.array(rows) @ N
    u, s, vt = np.linalg.svd(A, full_matrices=True)
    r = int((s > 1e-8 * s[0]).sum())
    return N @ vt[r:].T

def run_group(group, name, gens_note=""):
    out.append(f"\n[graviton forms: {name}] |G|={len(group)} {gens_note}")
    tot = {}
    for deg in (0, 1, 2):
        mons, N = invariant_forms(group, deg)
        n_inv = N.shape[1]
        n_gi = gauge_invariant_subspace(mons, N, deg) if n_inv else 0
        ttr = tt_rank(mons, N, deg) if n_inv else 0
        line = f"  degree {deg}: invariant forms {n_inv}, gauge-invariant {n_gi}, codim {n_inv-n_gi}, TT rank {ttr}"
        if deg == 2 and n_inv:
            sp = tt_rank_split(mons, N, deg)
            Ngi = gauge_inv_basis(mons, N, deg)
            ttr_gi = tt_rank(mons, Ngi, deg) if Ngi.shape[1] else 0
            sp_gi = tt_rank_split(mons, Ngi, deg) if Ngi.shape[1] else {}
            line += f"; TT split {sp}; TT rank of gauge-invariant forms {ttr_gi} split {sp_gi}"
        out.append(line)
        tot[deg] = (n_inv, n_gi)
    return tot

out += [""]
t4 = run_group(WB4, "W(B4) on Z^4 (validation vs K1: 3 mass, 9 two-derivative, codim 11, TT rank 5)")
tC = run_group(G_C, "set C: proper O x time-translation (no P, no T)")
tCPT = run_group(G_C_PT, "O_h x T on Z^3 x R (P and T imposed)")
# tadpoles: linear invariant forms in h
def lin_inv(group):
    rows = []
    for g in group:
        R = hrep(g)
        for _ in range(3):
            h = rng.normal(size=10); rows.append(list(R @ h - h))
    A = np.array(rows)
    return 10 - np.linalg.matrix_rank(A.T @ A, tol=1e-9)
out.append(f"\n[tadpoles] linear invariant forms in h: set C {lin_inv(G_C)}, O_h x T {lin_inv(G_C_PT)}, W(B4) {lin_inv(WB4)}")

txt = "\n".join(out)
print(txt)
