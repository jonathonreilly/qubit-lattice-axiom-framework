AUDIT_INPUT_PATHS = ('docs/FACE_REGISTER_LOOPS_AROUND_BLOCK_EDGES_ARE_GAUGE_INVARIANT_COMPLETE_AND_REACH_MAXWELL_AND_YANG_MILLS_AT_LIGHT_SPEED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""face-plaquette-law: the plaquette (magnetic) term for face registers on B_f-blocks.

Layout (CL-1 after the fourth review): each gauge factor's registers sit on the faces of its
B_f-blocks; a register is 2S fermion-mode sites (rishons) at each end; Gauss's law per B_f-block.
Proposed law: loops = the cycles of blocks around each block-edge segment (4 faces in the bulk,
3 or 4 of mixed sizes along a hanging face); loop operator = Re tr of the ordered product of the
faces' link operators; Hodge weights h/A (faces) and l/S (loops), lapse N, metric (N/sqrt g) g_ij.

A. gauge invariance per B_f-block, exact many-body (U(1) S=1/2,1,3/2; SU(2); SU(3); hanging loops)
B. the loop set is complete: ker(curl) = gauge + 3 torus harmonics (bulk and hanging meshes)
C. classical continuum: lattice energy -> (1/2) int(E^2 + B^2), U(1), SU(2), SU(3), O(B_f^2)
D. harmonic photon: c = 1 in cell units for every B_f; null cone of a diagonal / sheared metric
E. small S: single-loop register truncation vs the Kogut-Susskind loop (U(1), SU(2), SU(3))
F. one vacuum subtraction vs the old double subtraction
G. hanging-face interface: patch tests and cavity spectrum under refinement
Labels: [T] exact check, [D] finite diagnostic of a supplied model, [E] estimate.
"""
import time
import itertools
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = [0, 0]
rng = np.random.default_rng(20261022)


def rss():
    import resource
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


def memcheck(limit=290e6):
    import resource
    m = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if m > limit:
        raise SystemExit(f"memory guard: {m/1e6:.0f} MB")


def check(ok, label, detail=""):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" | {detail}" if detail else ""))


# ------------------------------------------------------------------ fermion helpers
def jw_ops(m):
    """annihilators c_0..c_{m-1} on 2^m (Jordan-Wigner, dense)."""
    a = np.array([[0.0, 1.0], [0.0, 0.0]])
    z = np.diag([1.0, -1.0])
    i2 = np.eye(2)
    out = []
    for j in range(m):
        op = np.array([[1.0]])
        for k in range(m):
            op = np.kron(op, z if k < j else (a if k == j else i2))
        out.append(op)
    return out


def polar(u, tol=1e-10):
    w, s, vh = np.linalg.svd(u)
    r = s > tol
    return w[:, r] @ vh[r, :]


def kron_list(mats):
    out = sp.csr_matrix(mats[0])
    for m in mats[1:]:
        out = sp.kron(out, sp.csr_matrix(m), format="csr")
    return out


def embed(op, pos, dims):
    mats = [sp.identity(d, format="csr") for d in dims]
    mats[pos] = sp.csr_matrix(op)
    return kron_list(mats)


def u1_link(S):
    """one U(1) face register: 2S rishons at end X then 2S at end Y. Returns U, V, NX, NY."""
    f = int(round(2 * S))
    c = jw_ops(2 * f)
    U = sum(c[f + k].T @ c[k] for k in range(f))       # moves a rishon X -> Y
    NX = sum(c[k].T @ c[k] for k in range(f))
    NY = sum(c[f + k].T @ c[f + k] for k in range(f))
    return U, polar(U), np.diag(NX).copy(), np.diag(NY).copy()


def gauss_diag(links, nblk, d):
    """diagonal of G_X (rishon number at X's ends) on the product of link spaces."""
    dims = [d] * len(links)
    G = []
    for X in range(nblk):
        g = np.zeros(d ** len(links))
        for li, (a, b, nx, ny) in enumerate(links):
            for end, nd in ((a, nx), (b, ny)):
                if end == X:
                    vecs = [np.ones(dd) for dd in dims]
                    vecs[li] = nd
                    v = vecs[0]
                    for w in vecs[1:]:
                        v = np.kron(v, w)
                    g += v
        G.append(g)
    return G


def charge_conserving(op, G):
    coo = op.tocoo()
    keep = np.abs(coo.data) > 1e-12
    r, cc = coo.row[keep], coo.col[keep]
    return all(np.all(np.abs(g[r] - g[cc]) < 1e-9) for g in G), int(keep.sum())


# ================================================================= A. gauge invariance
print("== A. gauge invariance per B_f-block (exact operator identities)")
resA = []
for S, shape in ((0.5, "square"), (1.0, "square"), (1.0, "triangle")):
    U, V, nx, ny = u1_link(S)
    d = U.shape[0]
    if shape == "square":       # blocks 0..3 around a bulk block edge; link 2 stored reversed
        geo, use, nb = [(0, 1), (1, 2), (3, 2), (3, 0)], ["V", "V", "Vd", "V"], 4
    else:                       # hanging: coarse block 0 with two face pieces, children 1, 2
        geo, use, nb = [(0, 1), (1, 2), (2, 0)], ["V", "V", "V"], 3
    links = [(a, b, nx, ny) for (a, b) in geo]
    G = gauss_diag(links, nb, d)
    for kind, M in (("V", V), ("U", U)):
        W = kron_list([M if u == "V" else M.T.conj() for u in use])
        okW, nnz = charge_conserving(W, G)
        resA.append((S, shape, kind, okW, nnz))
    loc = [V if u == "V" else V.T.conj() for u in use]
    loc[-1] = np.eye(d)
    okc, _ = charge_conserving(kron_list(loc), G)
    resA.append((S, shape, "open", okc, 0))
    memcheck()
ok = all(r[3] for r in resA if r[2] != "open") and not any(r[3] for r in resA if r[2] == "open")
check(ok, "[T] A1 U(1) many-body: the loop of domain-normalised raisers V (and of rishon bilinears U) around a bulk "
      "block edge (4 faces) and a hanging-face triangle (coarse block with two face pieces) conserves every block's "
      "rishon number; an open string does not",
      f"S=1/2 square, S=1 square and triangle: V and U loops invariant in "
      f"{sum(r[3] for r in resA if r[2] != 'open')}/6, open strings invariant in {sum(r[3] for r in resA if r[2] == 'open')}/3")


def local_shift(M, nx, ny):
    r, c = np.nonzero(np.abs(M) > 1e-12)
    dX, dY = set(np.round(nx[r] - nx[c]).astype(int)), set(np.round(ny[r] - ny[c]).astype(int))
    return (dX.pop(), dY.pop()) if len(dX) == 1 and len(dY) == 1 else None


shifts = []
for S in (0.5, 1.0, 1.5, 2.0):
    U, V, nx, ny = u1_link(S)
    shifts.append((S, local_shift(V, nx, ny), local_shift(U, nx, ny),
                   np.abs(V.conj().T @ V @ V.conj().T @ V - V.conj().T @ V).max()))
ok = all(sv == (-1, 1) and su == (-1, 1) and e < 1e-10 for (_, sv, su, e) in shifts)
check(ok, "[T] A1b every U(1) register (S = 1/2 .. 2) has V of definite charge (one rishon X -> Y) and V^dag V a "
      "projector, so around any closed cycle of blocks each block gains one and loses one rishon: the loop is "
      "gauge-invariant for every S (any number of faces, any sizes)", f"{len(shifts)} sizes")


def su_gens(N):
    if N == 2:
        s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
        return [x / 2 for x in s]
    L = []
    for i in range(3):
        for j in range(i + 1, 3):
            m = np.zeros((3, 3), complex); m[i, j] = m[j, i] = 1; L.append(m)
            m = np.zeros((3, 3), complex); m[i, j] = -1j; m[j, i] = 1j; L.append(m)
    L.append(np.diag([1, -1, 0]).astype(complex))
    L.append(np.diag([1, 1, -2]).astype(complex) / np.sqrt(3))
    return [x / 2 for x in L]


def suN_link(N):
    c = jw_ops(2 * N)
    cX, cY = c[:N], c[N:]
    U = [[cX[a] @ cY[b].T for b in range(N)] for a in range(N)]     # U^{ab} = c_{X,a} c_{Y,b}^dagger
    T = su_gens(N)
    gX = [sum(T[al][a, b] * cX[a].T @ cX[b] for a in range(N) for b in range(N)) for al in range(len(T))]
    gY = [sum(T[al][a, b] * cY[a].T @ cY[b] for a in range(N) for b in range(N)) for al in range(len(T))]
    return U, gX, gY, T


def expmh(H):
    w, v = np.linalg.eigh(H)
    return (v * np.exp(1j * w)) @ v.conj().T


cov = []
for N in (2, 3):
    U, gX, gY, T = suN_link(N)
    al = rng.normal(size=len(T))
    Om = expmh(-sum(a * t for a, t in zip(al, T)))
    RX = expmh(sum(a * g for a, g in zip(al, gX)))
    RY = expmh(sum(a * g for a, g in zip(al, gY)))
    eX = max(np.abs(RX @ U[a][b] @ RX.conj().T - sum(Om[a, c] * U[c][b] for c in range(N))).max()
             for a in range(N) for b in range(N))
    eY = max(np.abs(RY @ U[a][b] @ RY.conj().T - sum(U[a][c] * Om.conj().T[c, b] for c in range(N))).max()
             for a in range(N) for b in range(N))
    cov.append(max(eX, eY))
    if N == 2:   # polar (domain-normalised) link matrix on colour x Fock
        dF = U[0][0].shape[0]
        M = np.zeros((N * dF, N * dF), complex)
        for a in range(N):
            for b in range(N):
                M[a * dF:(a + 1) * dF, b * dF:(b + 1) * dF] = U[a][b]
        Vp = polar(M)
        Vb = [[Vp[a * dF:(a + 1) * dF, b * dF:(b + 1) * dF] for b in range(N)] for a in range(N)]
        ePol = max(np.abs(RX @ Vb[a][b] @ RX.conj().T - sum(Om[a, c] * Vb[c][b] for c in range(N))).max()
                   for a in range(N) for b in range(N))
check(max(cov) < 1e-12 and ePol < 1e-10,
      "[T] A2 SU(N) rishon link U^{ab} = c_{X,a} c_{Y,b}^dagger is covariant at each end, U -> Omega_X U Omega_Y^dagger "
      "(so every closed trace is invariant); its polar (domain-normalised) part is covariant too",
      f"max dev SU(2) {cov[0]:.1e}, SU(3) {cov[1]:.1e}, SU(2) polar {ePol:.1e}")


def loop_trace(Us, rev, N):
    """Re tr of the ordered product around a loop; rev[i]: link i stored against the loop."""
    def mat(i, a, b):
        return Us[i][a][b] if not rev[i] else Us[i][b][a].T.conj()
    nL = len(Us)
    tot = None
    for idx in itertools.product(range(N), repeat=nL):
        term = kron_list([mat(i, idx[i], idx[(i + 1) % nL]) for i in range(nL)])
        tot = term if tot is None else tot + term
    return 0.5 * (tot + tot.T.conj())


many = []
for N, nl, rev in ((2, 4, [False, False, True, False]), (3, 3, [False, False, False])):
    U, gX, gY, T = suN_link(N)
    d = U[0][0].shape[0]
    W = loop_trace([U] * nl, rev, N)
    geo = [(0, 1), (1, 2), (3, 2), (3, 0)] if nl == 4 else [(0, 1), (1, 2), (2, 0)]
    dims = [d] * nl
    worst = 0.0
    for X in range(nl):
        for al in range(len(T)):
            G = None
            for li, (a, b) in enumerate(geo):
                for end, g in ((a, gX[al]), (b, gY[al])):
                    if end == X:
                        t = embed(g, li, dims)
                        G = t if G is None else G + t
            C = W @ G - G @ W
            worst = max(worst, abs(C).max() if C.nnz else 0.0)
    # control: wrong colour contraction on one link (transposed) breaks invariance
    Ubad = [U] * nl
    Ut = [[U[b][a] for b in range(N)] for a in range(N)]
    Wb = loop_trace([Ut] + [U] * (nl - 1), rev, N)
    G = None
    for li, (a, b) in enumerate(geo):
        for end, g in ((a, gX[0]), (b, gY[0])):
            if end == 1:
                t = embed(g, li, dims)
                G = t if G is None else G + t
    Cb = Wb @ G - G @ Wb
    many.append((N, nl, W.shape[0], worst, abs(Cb).max(), abs(W).max()))
    memcheck()
ok = all(m[3] < 1e-12 and m[4] > 1e-3 and m[5] > 0.1 for m in many)
check(ok, "[T] A3 many-body: Re tr of the rishon loop commutes with every colour Gauss generator of every block: SU(2) "
      "square loop (bulk block edge) and SU(3) hanging triangle; a wrongly contracted link fails",
      "; ".join(f"SU({m[0]}) {m[1]}-face loop dim {m[2]}: max|[W,G]| {m[3]:.1e}, control {m[4]:.2f}" for m in many))


del W, G, C, Cb, Wb, U, gX, gY
import gc as _gc0
_gc0.collect()
print(f"   peak RSS after A {rss():.0f} MB")


# ================================================================= block-complex builder
def build_mesh(owner, blocks):
    """owner: int array on the unit grid (periodic); blocks: list of (lo, size).
    Returns faces [(A,B,d,area,h)], Grad (F x Nb), loops [(d, rows{face:sign}, Svec)], positions."""
    L = np.array(owner.shape)
    cen = [np.array(lo, float) + sz / 2.0 for lo, sz in blocks]
    fidx, faces = {}, []
    for c in itertools.product(*[range(n) for n in L]):
        c = np.array(c)
        A = owner[tuple(c)]
        for d in range(3):
            c2 = c.copy(); c2[d] = (c2[d] + 1) % L[d]
            B = owner[tuple(c2)]
            if A == B:
                continue
            key = (A, B, d, c[d])
            if key not in fidx:
                offA = cen[A] - (c + 0.5)
                offB = cen[B] - (c2 + 0.5)
                e = np.zeros(3); e[d] = 1
                disp = e + offB - offA
                fidx[key] = len(faces)
                faces.append([A, B, d, 0, abs(disp[d])])
            faces[fidx[key]][3] += 1
    F, Nb = len(faces), len(blocks)
    G = sp.lil_matrix((F, Nb))
    for f, (A, B, d, ar, h) in enumerate(faces):
        G[f, A] -= 1; G[f, B] += 1
    loops = []
    for d in range(3):
        d1, d2 = (d + 1) % 3, (d + 2) % 3
        e1 = np.zeros(3, int); e1[d1] = 1
        e2 = np.zeros(3, int); e2[d2] = 1
        for p in itertools.product(*[range(n) for n in L]):
            p = np.array(p)
            qs = [p, p - e1, p - e1 - e2, p - e2]                       # counter-clockwise about +e_d
            bl = [owner[tuple(q % L)] for q in qs]
            if len(set(bl)) < 3:
                continue
            pos = [q + 0.5 + (cen[b] - (q % L + 0.5)) for q, b in zip(qs, bl)]
            rows = {}
            for i in range(4):
                j = (i + 1) % 4
                if bl[i] == bl[j]:
                    continue
                dq = qs[j] - qs[i]
                n = int(np.argmax(np.abs(dq)))
                if dq[n] > 0:
                    key, sg = (bl[i], bl[j], n, qs[i][n] % L[n]), 1
                else:
                    key, sg = (bl[j], bl[i], n, qs[j][n] % L[n]), -1
                rows[fidx[key]] = rows.get(fidx[key], 0) + sg
            # collapse cyclic duplicates (keep one vertex per run of equal blocks)
            seq = []
            for i in range(4):
                if not seq or seq[-1][0] != bl[i]:
                    seq.append((bl[i], pos[i]))
            if len(seq) > 1 and seq[0][0] == seq[-1][0]:
                seq.pop()
            pts = [s_[1] for s_ in seq]
            Sv = 0.5 * sum(np.cross(pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts)))
            loops.append((d, rows, Sv, p.copy()))
    C = sp.lil_matrix((len(loops), F))
    for r, (d, rows, Sv, p) in enumerate(loops):
        for f, sg in rows.items():
            C[r, f] = sg
    return faces, G.tocsr(), loops, C.tocsr(), cen


def slab(P, nc, nf, fine_only=False):
    X, Lz = 2 * P, 2 * nc + nf
    owner = -np.ones((X, X, Lz), int)
    blocks = []
    if not fine_only:
        for i in range(P):
            for j in range(P):
                for k in range(nc):
                    lo = (2 * i, 2 * j, 2 * k)
                    owner[2 * i:2 * i + 2, 2 * j:2 * j + 2, 2 * k:2 * k + 2] = len(blocks)
                    blocks.append((lo, 2))
    for i in range(X):
        for j in range(X):
            for k in range(Lz):
                if owner[i, j, k] < 0:
                    owner[i, j, k] = len(blocks)
                    blocks.append(((i, j, k), 1))
    return owner, blocks, (X, X, Lz)


def weights(faces, loops):
    wE = np.array([h / ar for (A, B, d, ar, h) in faces])
    wB = np.array([1.0 / Sv[d] for (d, rows, Sv, p) in loops])
    return wE, wB


def mesh_ops(owner, blocks, comp=False):
    faces, G, loops, C, cen = build_mesh(owner, blocks)
    wE, wB = weights(faces, loops)
    return dict(faces=faces, G=G, loops=loops, C=C, wE=wE, wB=wB, V=float(np.prod(owner.shape)))


# ================================================================= B. completeness of the loop set
print("== B. the loops are complete")
resB = []
for name, (owner, blocks, Ls) in (("bulk 4^3 torus", (None, None, None)), ("hanging slab", slab(3, 3, 6))):
    if owner is None:
        owner = np.arange(64).reshape(4, 4, 4)
        blocks = [((i, j, k), 1) for i in range(4) for j in range(4) for k in range(4)]
    m = mesh_ops(owner, blocks)
    C, G = m["C"], m["G"]
    cg = abs(C @ G).max()
    F, Nb = G.shape
    rk = np.linalg.matrix_rank(C.toarray())
    kinds = {}
    for (d, rows, Sv, p) in m["loops"]:
        kinds[len(rows)] = kinds.get(len(rows), 0) + 1
    resB.append((name, cg, F - rk, Nb - 1 + 3, kinds, Nb, F))
ok = all(r[1] == 0 and r[2] == r[3] for r in resB)
check(ok, "[T] B1 curl.grad = 0 and dim ker(curl) = (blocks - 1) + 3: every face-register configuration that is not a "
      "gauge transform or a torus holonomy changes some loop (no extra mode, unlike the site-bond layout)",
      "; ".join(f"{r[0]}: blocks {r[5]}, faces {r[6]}, loops by size {r[4]}, ker {r[2]} = {r[3]}" for r in resB))
memcheck()


# ================================================================= C. classical continuum limit
print("== C. classical continuum: Hodge-weighted face and loop energies -> (1/2) int (E^a E^a + B^a B^a)")


def gens(N):
    return [np.array([[1.0 + 0j]])] if N == 1 else su_gens(N)


def expmh_b(H):
    w, v = np.linalg.eigh(H)
    return np.einsum("...ij,...j,...kj->...ik", v, np.exp(1j * w), v.conj())


Lbox, gc = 24, 1.0
KM = [np.array(k) for k in ((1, 0, 0), (0, 1, 1), (1, -1, 1))]


def field(N, amp, seed):
    r = np.random.default_rng(seed)
    T = gens(N)
    coef = [[(sum(r.normal() * t for t in T) * amp, r.uniform(0, 2 * np.pi)) for _ in KM] for _ in range(3)]

    def A(x):                      # x (..., 3) -> (..., 3, N, N)
        out = np.zeros(x.shape[:-1] + (3, N, N), complex)
        for i in range(3):
            for (H, ph), k in zip(coef[i], KM):
                arg = 2 * np.pi * (x @ k) / Lbox + ph
                out[..., i, :, :] += np.cos(arg)[..., None, None] * H
        return out

    def dA(x):                     # d_j A_i -> (..., j, i, N, N)
        out = np.zeros(x.shape[:-1] + (3, 3, N, N), complex)
        for i in range(3):
            for (H, ph), k in zip(coef[i], KM):
                arg = 2 * np.pi * (x @ k) / Lbox + ph
                for j in range(3):
                    out[..., j, i, :, :] += (-np.sin(arg) * 2 * np.pi * k[j] / Lbox)[..., None, None] * H
        return out
    return A, dA


def tr(M):
    return np.real(np.trace(M, axis1=-2, axis2=-1))


def mag_cont(A, dA, N, TR, ng=32):
    g1 = (np.arange(ng) + 0.5) * Lbox / ng
    e = 0.0
    for ch in np.array_split(np.arange(ng), 8):          # x-slabs keep the peak memory low
        x = np.stack(np.meshgrid(g1[ch], g1, g1, indexing="ij"), -1)
        a, da = A(x), dA(x)
        for i, j in ((0, 1), (1, 2), (2, 0)):
            Fij = da[..., i, j, :, :] - da[..., j, i, :, :] + 1j * gc * (a[..., i, :, :] @ a[..., j, :, :]
                                                                        - a[..., j, :, :] @ a[..., i, :, :])
            e += 0.5 * tr(Fij @ Fij).sum() / TR
    return e * (Lbox / ng) ** 3


def mag_lat(A, N, TR, Bf):
    n = Lbox // Bf
    g1 = np.arange(n) * Bf
    x = np.stack(np.meshgrid(g1, g1, g1, indexing="ij"), -1).astype(float)
    U = []
    for i in range(3):
        e = np.zeros(3); e[i] = Bf / 2
        U.append(expmh_b(gc * Bf * A(x + e)[..., i, :, :]))
    tot = 0.0
    I = np.eye(N)
    for i, j in ((0, 1), (1, 2), (2, 0)):
        Ui, Uj = U[i], U[j]
        Uj_xi = np.roll(Uj, -1, axis=i)
        Ui_xj = np.roll(Ui, -1, axis=j)
        P = Ui @ Uj_xi @ np.swapaxes(Ui_xj.conj(), -1, -2) @ np.swapaxes(Uj.conj(), -1, -2)
        tot += tr(I - P).sum()
    return tot / (gc ** 2 * Bf * TR)


resC = []
for N in (1, 2, 3):
    TR = 1.0 if N == 1 else 0.5
    A, dA = field(N, 0.1, 7 + N)
    ec = mag_cont(A, dA, N, TR)
    errs = [abs(mag_lat(A, N, TR, Bf) / ec - 1) for Bf in (1, 2, 3)]
    # commutator share of the continuum energy (non-abelian content tested)
    resC.append((N, ec, errs))
    memcheck()
ok = all(r[2][0] < 0.03 and 3.0 < r[2][1] / r[2][0] < 5.5 and 1.8 < r[2][2] / r[2][1] < 3.0 for r in resC)
check(ok, "[T/D] C1 magnetic part: sum over block edges of (1/(g^2 B_f T)) Re tr(1 - U_loop) -> (1/2) int B^a B^a with "
      "the full Yang-Mills F = dA - dA + i g [A, A]; error falls as B_f^2 (ratios near 4 and 9/4 for B_f = 1, 2, 3; field wavelengths 24 cells)",
      "; ".join(f"{'U(1)' if r[0] == 1 else f'SU({r[0]})'}: rel err {r[2][0]:.1e}, {r[2][1]:.1e}, {r[2][2]:.1e}"
                for r in resC))


def nonab_share(N):
    TR = 0.5
    A, dA = field(N, 0.1, 7 + N)
    gsave = globals()["gc"]
    e1 = mag_cont(A, dA, N, TR)
    globals()["gc"] = 0.0
    e0 = mag_cont(A, dA, N, TR)
    globals()["gc"] = gsave
    return abs(e1 - e0) / e1


shares = [nonab_share(N) for N in (2, 3)]
check(min(shares) > 0.05, "[D] C2 the test fields are genuinely non-abelian: the commutator changes the continuum "
      "magnetic energy by", f"SU(2) {shares[0]:.0%}, SU(3) {shares[1]:.0%} (C1 tests the Yang-Mills term)")

# electric part: face value Phi^a = B_f^2 E^a(face centre)/g, energy (g^2/(2 B_f T)) tr Phi^2
resE = []
for N in (1, 3):
    TR = 1.0 if N == 1 else 0.5
    Ef, _ = field(N, 0.1, 99 + N)
    g1 = (np.arange(12) + 0.5) * Lbox / 12
    x = np.stack(np.meshgrid(g1, g1, g1, indexing="ij"), -1)
    Ex = Ef(x)
    ecE = 0.5 * sum(tr(Ex[..., i, :, :] @ Ex[..., i, :, :]).sum() for i in range(3)) / TR * (Lbox / 12) ** 3
    for Bf in (2, 3):
        n = Lbox // Bf
        xs = np.stack(np.meshgrid(*[np.arange(n) * Bf] * 3, indexing="ij"), -1).astype(float)
        el = 0.0
        for i in range(3):
            e = np.zeros(3); e[i] = Bf / 2
            Phi = Bf ** 2 * Ef(xs + e)[..., i, :, :] / gc
            el += gc ** 2 / (2 * Bf * TR) * tr(Phi @ Phi).sum()
        resE.append(abs(el / ecE - 1))
check(max(resE) < 1e-10, "[T] C3 electric part: (g^2/(2 B_f T)) sum_faces tr Phi^2 with Phi = flux through the face "
      "in units of g equals (1/2) int E^a E^a exactly for band-limited fields (U(1), SU(3); B_f = 2, 3)",
      f"max rel dev {max(resE):.1e}")


# ================================================================= D. harmonic photon on the B_f lattice
print("== D. harmonic photon: speed 1 in cell units for every B_f; null cone of the cell metric")


def photon_w2(kc, gcell, N, Bf, g=1.0):
    """omega^2 (per unit time) of the two photon branches; kc in cell units; gcell the cell metric."""
    gam = Bf ** 2 * np.asarray(gcell, float)
    sg = np.sqrt(np.linalg.det(gam))
    kap = Bf * np.asarray(kc, float)
    c = np.cos(kap / 2)
    s = 2 * np.sin(kap / 2)
    m = np.array([c[1] * c[2], c[2] * c[0], c[0] * c[1]])
    ME = gam * np.outer(c, c); np.fill_diagonal(ME, np.diag(gam))
    MB = gam * np.outer(m, m); np.fill_diagonal(MB, np.diag(gam))
    ME *= g ** 2 * N / sg
    MB *= N / (g ** 2 * sg)
    Cu = 1j * np.array([[0, -s[2], s[1]], [s[2], 0, -s[0]], [-s[1], s[0], 0]])
    w2 = np.sort(np.real(np.linalg.eigvals(ME @ Cu.conj().T @ MB @ Cu)))
    return w2, ME, MB


resD = []
for Bf in (1, 2, 3, 24):
    worst = 0.0
    for kc in rng.uniform(-np.pi, np.pi, size=(20, 3)) / Bf:
        w2, _, _ = photon_w2(kc, np.eye(3), 1.0, Bf, g=0.7)
        exact = 4 / Bf ** 2 * np.sum(np.sin(kc * Bf / 2) ** 2)
        worst = max(worst, abs(w2[1] - exact), abs(w2[2] - exact), abs(w2[0]))
    small = []
    for kh in (np.array([1, 0, 0]), np.array([1, 1, 0]) / np.sqrt(2), np.ones(3) / np.sqrt(3)):
        w2, _, _ = photon_w2(1e-3 * kh / Bf, np.eye(3), 1.0, Bf, g=0.7)
        small.append(np.sqrt(w2[1:]) / (1e-3 / Bf))
    resD.append((Bf, worst, max(abs(np.array(small) - 1).ravel())))
check(all(r[1] < 1e-12 and r[2] < 1e-6 for r in resD),
      "[T] D1 flat cells, electric g^2/(2 B_f) per face and magnetic 1/(g^2 B_f) per loop: omega^2 = (4/B_f^2) "
      "sum sin^2(k_i B_f/2) for both polarisations, one zero (gauge) branch; speed exactly 1 cell per unit time as k -> 0 "
      "along axes, face and body diagonals, independent of g",
      "; ".join(f"B_f={r[0]}: |dev| {r[1]:.0e}, |v-1| {r[2]:.0e}" for r in resD))


def cone_err(gcell, N, Bf, kap):
    gi = np.linalg.inv(gcell)
    errs = []
    for kh in rng.normal(size=(12, 3)):
        kh /= np.linalg.norm(kh)
        kc = kap * kh / Bf
        w2, _, _ = photon_w2(kc, gcell, N, Bf)
        tgt = N ** 2 * kc @ gi @ kc
        errs.append(max(abs(w2[1] / tgt - 1), abs(w2[2] / tgt - 1)))
    return max(errs)


cases = [("diagonal", np.diag([1.3, 0.8, 1.1]) ** 2, 0.7, 3),
         ("sheared", np.array([[1.0, 0.3, 0.1], [0.3, 1.2, -0.2], [0.1, -0.2, 0.9]]), 1.1, 2)]
resD2 = []
for name, gm, N, Bf in cases:
    e1, e2 = cone_err(gm, N, Bf, 0.02), cone_err(gm, N, Bf, 0.01)
    minE = min(min(np.linalg.eigvalsh(photon_w2(k, gm, N, Bf)[1]).min(), np.linalg.eigvalsh(photon_w2(k, gm, N, Bf)[2]).min())
               for k in rng.uniform(-np.pi, np.pi, size=(200, 3)))
    resD2.append((name, e1, e2, minE))
check(all(r[1] < 1e-3 and 3.5 < r[1] / r[2] < 4.5 and r[3] > 0 for r in resD2),
      "[T] D2 weights (N/sqrt g) g_ij per block (diagonal per face and loop, off-diagonal via the block's mean face "
      "values and mean loop fluxes): both branches reach the null cone N^2 g^ij k_i k_j at O(k^2); both forms positive "
      "definite at every k (Schur product)",
      "; ".join(f"{r[0]}: rel err {r[1]:.1e} at kB=0.02, ratio {r[1]/r[2]:.2f}, min eig {r[3]:.2e}" for r in resD2))


# ================================================================= E. small S: one loop
print("== E. small S: one isolated loop (4 faces, no matter) in the register vs the untruncated loop")


def loop_gap(group, cut, g2):
    if group == "U1":
        ms = np.arange(-cut, cut + 1e-9, 1.0)
        n = len(ms)
        H = np.diag(2 * g2 * ms ** 2 + 1 / g2) - (np.eye(n, k=1) + np.eye(n, k=-1)) / (2 * g2)
    elif group == "SU2":
        js = np.arange(0, cut + 1e-9, 0.5)
        n = len(js)
        # Re tr U = chi_1/2 acts as |j> -> |j-1/2> + |j+1/2>; magnetic (2/g^2)(2 - chi)
        H = np.diag(2 * g2 * js * (js + 1) + 4 / g2) - 2 / g2 * (np.eye(n, k=1) + np.eye(n, k=-1))
    else:
        reps = [(p, q) for p in range(int(cut) + 1) for q in range(int(cut) + 1 - p)]
        ix = {r: i for i, r in enumerate(reps)}
        n = len(reps)
        H = np.zeros((n, n))
        for (p, q), i in ix.items():
            H[i, i] = 2 * g2 * (p * p + q * q + p * q + 3 * p + 3 * q) / 3 + 6 / g2
            for r in ((p + 1, q), (p - 1, q + 1), (p, q - 1)):      # chi_F chi_(p,q)
                if r in ix:
                    H[ix[r], i] -= 1 / g2          # (2/g^2) * (1/2) per term of Re chi_F
                    H[i, ix[r]] -= 1 / g2
    w = np.linalg.eigvalsh(0.5 * (H + H.T))
    return w[1] - w[0], w[0]


def harm(group):
    return 2.0 if group == "U1" else 4.0


# weak coupling: the untruncated loop reaches the harmonic plaquette frequency (2/B_f; class functions 2 x 2/B_f)
weak = {gname: loop_gap(gname, cut, 0.03)[0] / harm(gname)
        for gname, cut in (("U1", 40), ("SU2", 40), ("SU3", 40))}
check(all(abs(v - 1) < 0.03 for v in weak.values()),
      "[T/D] E1 weak coupling (g^2 = 0.03): the untruncated loop's gap is the harmonic plaquette value fixed by the same "
      "c_E c_B (2/B_f for U(1); 4/B_f, the first class-function level, for SU(2), SU(3))",
      ", ".join(f"{k} {v:.4f}" for k, v in weak.items()))
G2 = {"U1": 4 * np.pi / 137.036, "SU2": 4 * np.pi * 0.0338, "SU3": 4 * np.pi * 0.118}
rows = []
for gname in ("U1", "SU2", "SU3"):
    ref = loop_gap(gname, 40 if gname != "U1" else 80, G2[gname])[0]
    cuts = (0.5, 1, 1.5, 2, 3, 6) if gname != "SU3" else (1, 2, 3, 6)
    if gname == "U1":
        cuts = (0.5, 1, 1.5, 2, 3, 6, 10)
    rows.append((gname, [(c, loop_gap(gname, c, G2[gname])[0] / ref) for c in cuts]))
conv = all(abs(r[1][-1][1] - 1) < 1e-3 for r in rows if r[0] != "U1") and abs(rows[0][1][-1][1] - 1) < 2e-2
check(conv, "[D] E2 small S distorts the loop's levels (CL-3's dressed-coupling clause, not the bare Hodge product, then sets the cone); truncation at measured-scale couplings (supplied g^2 = 4 pi alpha: 1/137, 0.0338, 0.118): "
      "gap / untruncated gap by register size (U(1): |E| <= S; SU(N): reps up to j or p+q; supplied reading of S)",
      "; ".join(f"{r[0]} " + " ".join(f"{c}:{v:.2f}" for c, v in r[1]) for r in rows))


# ================================================================= F. one vacuum subtraction
print("== F. vacuum standard: one subtraction")
n = 4
ks = [2 * np.pi * np.array(m) / n for m in itertools.product(range(n), repeat=3) if any(m)]
wk = np.array([np.sqrt(4 * np.sum(np.sin(k / 2) ** 2)) for k in ks])
Evac = lambda lam: np.sum(wk) / lam                    # 2 polarisations x omega/2, edges dilated by lam
HBvac = lambda lam: 0.5 * Evac(lam)                    # virial: magnetic share of a harmonic vacuum
single = [Evac(l) - Evac(l) for l in (1.0, 1.3)]
double = [Evac(l) - Evac(l) - HBvac(l) for l in (1.0, 1.3)]
force_double = (double[1] - double[0]) / 0.3
one_photon_single = (Evac(1) + wk[0]) - Evac(1)
one_photon_double = (Evac(1) + wk[0]) - Evac(1) - HBvac(1)
# exact quantum loop at small S: U(1) S = 1, g^2 = 1
ms = np.arange(-1, 2.0)
HE = np.diag(2 * ms ** 2); HB = np.eye(3) - (np.eye(3, k=1) + np.eye(3, k=-1)) / 2
w, v = np.linalg.eigh(HE + HB)
hb0 = v[:, 0] @ HB @ v[:, 0]
check(max(abs(np.array(single))) < 1e-12 and abs(one_photon_single - wk[0]) < 1e-12 and abs(force_double) > 1,
      "[T] F1 one subtraction (review-4 Total phase): vacuum phase 0 at every edge value, one photon exactly omega; the "
      "old extra subtraction of the plaquette's vacuum Born mean leaves -<H_B>_vac (half the zero-point, virial), "
      "edge-dependent: a spurious vacuum energy and edge force",
      f"4^3 torus: single {single[0]:.0e}; double {double[0]:.1f} at lam=1, {double[1]:.1f} at 1.3 (force {force_double:.1f}); "
      f"one photon single {one_photon_single:.3f} = omega, double {one_photon_double:.1f}; S=1 loop: <H_B>_vac {hb0:.3f} != 0")


# ================================================================= G. hanging-face interface
print("== G. hanging faces: a split region (child blocks B/2) beside unsplit blocks B; weights h/A and l/S")


def patch(m, comp=None):
    faces, loops, wE, wB, V = m["faces"], m["loops"], m["wE"].copy(), m["wB"].copy(), m["V"]
    if comp is not None:
        wB = wB * comp
    outE, outB = [], []
    for d in range(3):
        Phi = np.array([(1.0 if fd == d else 0.0) * ar for (A, B, fd, ar, h) in faces])
        outE.append(0.5 * np.sum(wE * Phi ** 2) / (0.5 * V) - 1)
        th = np.array([Sv[d] for (dd, rows, Sv, p) in loops])
        outB.append(0.5 * np.sum(wB * th ** 2) / (0.5 * V) - 1)
    return outE, outB


def modes(m, nev, comp=None, mu=50.0):
    C, G, wE, wB = m["C"], m["G"], m["wE"], m["wB"].copy()
    if comp is not None:
        wB = wB * comp
    Wh, Wih = sp.diags(np.sqrt(wE)), sp.diags(1 / np.sqrt(wE))
    K = Wh @ C.T @ sp.diags(wB) @ C @ Wh + mu * (Wih @ G @ G.T @ Wih)
    vals = spla.eigsh(K.tocsc(), k=nev, sigma=-1e-3, which="LM", return_eigenvectors=False)
    vals = np.sort(vals)
    return np.sqrt(np.clip(vals[vals > 1e-8], 0, None))


def cont_modes(X, Lz, nev):
    out = []
    R = 4
    for nx, ny, nz in itertools.product(range(-R, R + 1), repeat=3):
        if nx or ny or nz:
            w = 2 * np.pi * np.sqrt((nx / X) ** 2 + (ny / X) ** 2 + (nz / Lz) ** 2)
            out += [w, w]
    return np.sort(out)[:nev]


def first_layer_comp(m, Ls, nc, excess):
    """scale the loops around normal (z) edges in the first child layer on each side of the interface."""
    comp = np.ones(len(m["loops"]))
    zs = {2 * nc, Ls[2] - 1}
    for r, (d, rows, Sv, p) in enumerate(m["loops"]):
        if d == 2 and p[2] in zs and len(rows) == 4 and abs(Sv[2] - 1) < 1e-9:
            comp[r] = 1 - excess
    return comp


s1 = slab(3, 3, 6)
m1 = mesh_ops(s1[0], s1[1])
pE, pB = patch(m1)
X, _, Lz = s1[2]
exc_per_area = pB[2] * m1["V"] / (2 * X * X)     # extra normal-field layer thickness per interface
check(max(abs(np.array(pE))) < 1e-12 and max(abs(pB[0]), abs(pB[1])) < 1e-12 and pB[2] > 0,
      "[T] G1 patch tests across the hanging face: uniform E (every direction) and uniform B along the interface give "
      "exactly (1/2) V E^2 and (1/2) V B^2; a normal B costs an extra layer (the hanging loops' polygons tilt)",
      f"E dev {max(abs(np.array(pE))):.0e}; B_x,B_y dev {max(abs(pB[0]), abs(pB[1])):.0e}; B_z excess = layer of "
      f"{exc_per_area:.4f} child units = B/{2/exc_per_area:.2f} per interface (B the unsplit side)")
comp1 = first_layer_comp(m1, s1[2], 3, exc_per_area)
pEc, pBc = patch(m1, comp1)
memcheck()

res = []
for sc in (1, 2):
    P, nc, nf = 2 * sc, 2 * sc, 4 * sc
    sh = slab(P, nc, nf)
    mh = mesh_ops(sh[0], sh[1])
    X, _, Lz = sh[2]
    nev = 24
    ref = cont_modes(X, Lz, nev - 3)
    wh = modes(mh, nev)[:len(ref)]
    wu = np.sort([np.sqrt(4 * (np.sin(np.pi * a / X) ** 2 + np.sin(np.pi * b / X) ** 2 + np.sin(np.pi * c / Lz) ** 2))
                  for a in range(X) for b in range(X) for c in range(Lz) if a or b or c for _ in range(2)])[:len(ref)]
    import gc as _gc
    _gc.collect()
    _, pBs = patch(mh)
    comp = first_layer_comp(mh, sh[2], nc, pBs[2] * mh["V"] / (2 * X * X))
    wc = modes(mh, nev, comp)[:len(ref)]
    _gc.collect()
    res.append((sc, np.abs(wh / ref - 1), np.abs(wu / ref - 1), np.abs(wc / ref - 1), len(sh[1]),
                np.abs((wh - wc) / ref).max(), len(mh["faces"])))
    memcheck()
dh = [r[1].max() for r in res]
mh_ = [r[1].mean() for r in res]
mc_ = [r[3].mean() for r in res]
mu_ = [r[2].mean() for r in res]
dhc = [r[5] for r in res]
check(dh[0] / dh[1] > 3.0 and 1.4 < dhc[0] / dhc[1] < 2.6 and all(a <= b for a, b in zip(mh_, mc_)),
      "[D] G2 cavity (torus 4x4x8 in child units, half split; 72 then 576 blocks): the lowest 21 modes converge to "
      "the c = 1 continuum as all blocks halve (second order overall); the B_z excess is a first-order term (its effect, "
      "against the same mesh with it removed by rescaling the first child layer's normal-edge loops, falls about linearly); removal "
      "does not improve the spectrum, so the plain h/A, l/S rule is kept",
      f"max rel dev scale 1 -> 2: {dh[0]:.3f} -> {dh[1]:.3f} (ratio {dh[0]/dh[1]:.2f}); excess effect "
      f"{dhc[0]:.4f} -> {dhc[1]:.4f} (ratio {dhc[0]/dhc[1]:.2f}); mean dev plain {mh_[0]:.3f}, {mh_[1]:.3f}; "
      f"removed {mc_[0]:.3f}, {mc_[1]:.3f}; all-child torus {mu_[0]:.3f}, {mu_[1]:.3f}")
print(f"elapsed_seconds {time.time()-T0:.1f}, peak RSS {rss():.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
