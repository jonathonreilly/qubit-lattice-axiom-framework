"""Exact diagonalisation in the psi-frame Fock space (gate iii), built independently of the d-frame/HS code:
operators are Jordan-Wigner fermions on psi modes, the interaction is written from the psi-frame pairings
P_e = psi_S^T M_e psi_S, and observables from Bh^a = psi_S^T Tvec_a psi_S.  Uses the d-number (U(1)_c) sectors only
to block the dense diagonalisation.  Only for tiny systems (reduced flavours)."""
import numpy as np
import scipy.sparse as sp

SX = np.array([[0., 1.], [1., 0.]], complex)
SY = np.array([[0., -1j], [1j, 0.]], complex)
SZ = np.array([[1., 0.], [0., -1.]], complex)


def jw_ops(n):
    I = sp.identity(2, format="csr", dtype=complex)
    Z = sp.csr_matrix(np.diag([1.0, -1.0]).astype(complex))
    a = sp.csr_matrix(np.array([[0, 1], [0, 0]], complex))       # |0><1| on (|0>,|1>) : annihilator
    ops = []
    for j in range(n):
        m = sp.identity(1, format="csr", dtype=complex)
        for k in range(n):
            m = sp.kron(m, Z if k < j else (a if k == j else I), format="csr")
        ops.append(m)
    return ops


def build(fm, kappa, lat, W):
    """returns dict with H (sparse), Qtot, Hkin, X_a, Y_a (Q = 0 vector components), d-number per basis state."""
    N, D, nfl = lat.N, fm.D, fm.nfl
    nm = N * D
    c = jw_ops(nm)
    cd = [o.conj().T.tocsr() for o in c]
    idx = lambda x, m: x * D + m
    # walker one-body matrix in the psi frame
    sig = [SX, SY, SZ][:lat.d]
    h = np.zeros((nm, nm), complex)
    for a in range(lat.d):
        for x in range(N):
            e = np.zeros(lat.d, int); e[a] = 1
            yp, ym = lat.site(lat.coords[x] + e), lat.site(lat.coords[x] - e)
            blk = np.kron(sig[a], np.eye(nfl))
            for i in range(D):
                for j in range(D):
                    if blk[i, j] != 0:
                        h[idx(x, i), idx(yp, j)] += blk[i, j] / 2j
                        h[idx(x, i), idx(ym, j)] += -blk[i, j] / 2j
    assert np.allclose(h, h.conj().T)
    Hkin = sp.csr_matrix((2 ** nm, 2 ** nm), dtype=complex)
    for i in range(nm):
        for j in range(nm):
            if h[i, j] != 0:
                Hkin = Hkin + h[i, j] * (cd[i] @ c[j])
    # smeared annihilators psi_S(x)_m
    psiS = [[sum(w * c[idx(y, m)] for y, w in zip(lat.nbr[x], lat.wts[x])) for m in range(D)] for x in range(N)]

    def pairing(x, M):
        out = sp.csr_matrix((2 ** nm, 2 ** nm), dtype=complex)
        for i in range(D):
            for j in range(D):
                if M[i, j] != 0:
                    out = out + M[i, j] * (psiS[x][i] @ psiS[x][j])
        return out
    Qtot = sp.csr_matrix((2 ** nm, 2 ** nm), dtype=complex)
    for x in range(N):
        for f, k in kappa.items():
            if k == 0:
                continue
            for M in fm.fams[f]:
                P = pairing(x, M)
                Qtot = Qtot + (-0.25 * k) * (P @ P + (P @ P).conj().T)
    Xs, Ys = [], []
    for T in fm.Tvec:
        B = sum(pairing(x, T) for x in range(N))
        Xs.append(0.5 * (B + B.conj().T)); Ys.append((B - B.conj().T) / 2j)
    # d-number of each basis state: JW ordering: mode j is the j-th tensor factor (most significant first)
    states = np.arange(2 ** nm)
    occ = (states[:, None] >> (nm - 1 - np.arange(nm))[None, :]) & 1
    Smask = np.tile(fm.Smask, N)
    nd = occ[:, Smask].sum(1) + (1 - occ[:, ~Smask]).sum(1)
    return dict(H=(Hkin + W * Qtot).tocsr(), Hkin=Hkin.tocsr(), Qtot=Qtot.tocsr(), X=Xs, Y=Ys, nd=nd)


def thermal(ops, beta):
    """thermal averages, sector by sector (memory ~ largest sector squared)."""
    H, nd = ops["H"], ops["nd"]
    sectors = {}
    for q in np.unique(nd):
        sel = np.where(nd == q)[0]
        Hb = H[sel][:, sel].toarray()
        rest = H[sel][:, np.where(nd != q)[0]]
        assert (abs(rest).max() if rest.nnz else 0.0) < 1e-12
        sectors[q] = (sel,) + tuple(np.linalg.eigh(Hb))
    E0 = min(e.min() for _, e, _ in sectors.values())
    Z = sum(np.exp(-beta * (e - E0)).sum() for _, e, _ in sectors.values())

    def ev(O):
        tot = 0.0
        for sel, e, v in sectors.values():
            w = np.exp(-beta * (e - E0))
            Ob = O[sel][:, sel]
            tot += np.real(np.sum(w * np.einsum("ik,ik->k", v.conj(), Ob @ v)))
        return tot / Z

    def ev2(O):      # <O O> = sum_n w_n |O|n>|^2 for Hermitian O
        tot = 0.0
        for sel, e, v in sectors.values():
            w = np.exp(-beta * (e - E0))
            OV = O[:, sel] @ v
            tot += np.real(np.sum(w * np.einsum("ik,ik->k", OV.conj(), OV)))
        return tot / Z
    allE = np.sort(np.concatenate([e for _, e, _ in sectors.values()]))
    return dict(E=ev(H), Ekin=ev(ops["Hkin"]), Q=ev(ops["Qtot"]),
                SX=np.array([ev2(X) for X in ops["X"]]), SY=np.array([ev2(Y) for Y in ops["Y"]]),
                E0=E0, gap=allE[1] - allE[0])
