"""A46 library (supplied toys; nothing adopted).  Works in the Klein-dual (pi-flux) frame of A44.
Dual-frame rule: H' = J' sum_bonds s.s + K' sum_bonds s^a s^a + R sum_faces (P + P^-1),
P + P^-1 = (1/4)[(12)(34) + (14)(23) - (13)(24)] + (1/4) sum_{i<j} (ij) + 1/4  (ring_check.py, exact).
Original (soldered) frame: J = -J', K = K' + 2J', and the ring term with every dot product Klein-twisted
(edge along a: 2 s^a s^a - s.s; face diagonal: 2 s^c s^c - s.s, c the face normal); same coefficient R.
Mean field: soldered-frame hops (NN t + i lam s^a; face-diagonal t2 + i lam2 s.d/|d|), APBC, transformed
by V = (+) V_x to the dual frame, plus a dual-frame staggered field m (-1)^{|x|} s^z (the AF family)."""
import sys, time, numpy as np
sys.path.insert(0, __file__.rsplit('/', 2)[0] + "/A44")
from a44lib import Cluster, cube, SIG, CYC, bits_table, projected_vector, sparse_terms, product_vector

FD = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
A_ = [1j * S for S in SIG]


def Vx(x):
    return np.linalg.matrix_power(A_[0], int(x[0]) % 4) @ np.linalg.matrix_power(A_[1], int(x[1]) % 4) @ np.linalg.matrix_power(A_[2], int(x[2]) % 4)


def plaquettes(cl):
    E = np.eye(3, dtype=int); out = []
    for s in cl.sites:
        x = np.array(s)
        for a, b in ((0, 1), (1, 2), (0, 2)):
            pts = [x, x + E[a], x + E[a] + E[b], x + E[b]]
            out.append([cl.idx[tuple(cl.canon(p)[0])] for p in pts])
    return np.array(out)


def mf_dual(cl, t=0., lam=1., m=0., t2=0., lam2=0., twist=(np.pi, np.pi, np.pi), pattern="neel"):
    N = cl.N; tw = np.array(twist, float)
    h = np.zeros((2 * N, 2 * N), complex)
    def add(i, j, u, n):
        ph = np.exp(1j * (tw @ n))
        h[2 * i:2 * i + 2, 2 * j:2 * j + 2] += u * ph
        h[2 * j:2 * j + 2, 2 * i:2 * i + 2] += (u * ph).conj().T
    for (i, j, a, n) in cl.bonds:
        add(i, j, t * np.eye(2) + 1j * lam * SIG[a], n)
    if t2 != 0 or lam2 != 0:
        for i, s in enumerate(cl.sites):
            for d in FD:
                rep, n = cl.canon(np.array(s) + np.array(d))
                dh = np.array(d, float) / np.sqrt(2)
                add(i, cl.idx[tuple(rep)], t2 * np.eye(2) + 1j * lam2 * sum(dh[c] * SIG[c] for c in range(3)), n)
    V = np.zeros((2 * N, 2 * N), complex)
    for i, s in enumerate(cl.sites):
        V[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Vx(s)
    hd = V.conj().T @ h @ V
    for i, s in enumerate(cl.sites):
        sg = (-1) ** int(sum(s)) if pattern == "neel" else (-1) ** int(s[0] + s[1])   # Neel or collinear (pi,pi,0)
        hd[2 * i:2 * i + 2, 2 * i:2 * i + 2] += m * sg * SIG[2]
    ev, W = np.linalg.eigh(hd)
    return W[:, :N].copy(), ev[N] - ev[N - 1]


def binerr(x):
    x = np.asarray(x); n = len(x); out = []; B = 1
    while n // B >= 16:
        mm = x[:(n // B) * B].reshape(-1, B).mean(1); out.append(m_e := mm.std(ddof=1) / np.sqrt(len(mm))); B *= 2
    return x.mean(), max(out)


def vmc_dual(cl, Phi, nsweep, ntherm, seed, tlimit, plaq=None, conserve=False, pairs2=None):
    """Samples per sweep: [e_J', e_K', ring per face, staggered m_z]."""
    N = cl.N; rng = np.random.default_rng(seed); rows0 = 2 * np.arange(N)
    for _ in range(500):
        s = rng.permutation(np.r_[np.zeros(N // 2, int), np.ones(N - N // 2, int)]) if conserve or _ < 250 else rng.integers(0, 2, N)
        M = Phi[rows0 + s]
        if np.linalg.cond(M) < 1e10: break
    Q = np.linalg.inv(M); bi, bj, ba = cl.bi, cl.bj, cl.ba
    stag = (-1.) ** cl.X.sum(1)
    acc = [0, 0, 0, 0]; samples = []; drift = 0.; t0 = time.time()
    eye4 = np.eye(4, dtype=bool)
    for sw in range(ntherm + nsweep):
        for _ in range(N):
            if (not conserve) and rng.random() < 0.5:
                i = rng.integers(N); v = Phi[2 * i + 1 - s[i]]; R = v @ Q[:, i]; acc[1] += 1
                if rng.random() < abs(R) ** 2:
                    u = v @ Q; u[i] -= 1.; Q -= np.outer(Q[:, i], u) / R; s[i] = 1 - s[i]; acc[0] += 1
            else:
                b = rng.integers(len(bi)); i, j = bi[b], bj[b]
                if conserve and s[i] == s[j]:
                    acc[3] += 1; continue
                vi, vj = Phi[2 * i + 1 - s[i]], Phi[2 * j + 1 - s[j]]; Qc = Q[:, [i, j]]
                Rm = np.array([[vi @ Qc[:, 0], vi @ Qc[:, 1]], [vj @ Qc[:, 0], vj @ Qc[:, 1]]])
                R = Rm[0, 0] * Rm[1, 1] - Rm[0, 1] * Rm[1, 0]; acc[3] += 1
                if rng.random() < abs(R) ** 2:
                    U = np.vstack([vi @ Q, vj @ Q]); U[0, i] -= 1.; U[1, j] -= 1.
                    Q -= Qc @ np.linalg.solve(Rm, U); s[i], s[j] = 1 - s[i], 1 - s[j]; acc[2] += 1
        if sw % 10 == 0 or sw == ntherm + nsweep - 1:
            Qf = np.linalg.inv(Phi[rows0 + s]); drift = max(drift, np.abs(Q - Qf).max() / np.abs(Qf).max()); Q = Qf
        if sw < ntherm:
            continue
        Pa = Phi[rows0 + 1 - s]
        R1 = np.einsum('in,ni->i', Pa, Q)
        Gij = np.einsum('bn,nb->b', Pa[bi], Q[:, bj]); Gji = np.einsum('bn,nb->b', Pa[bj], Q[:, bi])
        R2 = R1[bi] * R1[bj] - Gij * Gji
        z = 1. - 2. * s
        cc = lambda al, zz: np.ones_like(zz, dtype=complex) if al == 0 else (-1j * zz if al == 1 else zz.astype(complex))
        C = np.empty((3, 3, len(bi)), complex)
        for al in range(3):
            for be in range(3):
                r = R2 if (al < 2 and be < 2) else (R1[bi] if al < 2 else (R1[bj] if be < 2 else 1.))
                C[al, be] = cc(al, z[bi]) * cc(be, z[bj]) * r
        eJ = (C[0, 0] + C[1, 1] + C[2, 2]).mean(); eK = C[ba, ba, np.arange(len(bi))].mean()
        ring = 0.
        if plaq is not None:
            tot = 0.
            for c0 in range(0, len(plaq), 512):
                pq = plaq[c0:c0 + 512]
                G4 = np.einsum('pkn,npl->pkl', Pa[pq], Q[:, pq])
                s4 = s[pq]
                for sh in (1, -1):
                    ch = np.roll(s4, sh, axis=1) != s4
                    mask = ch[:, :, None] & ch[:, None, :]
                    Mm = np.where(mask, G4, eye4[None].astype(complex))
                    tot += np.linalg.det(Mm).sum()
            ring = tot / len(plaq)
        row = [eJ, eK, ring, (stag * z).mean()]
        if pairs2 is not None:                      # s.s on extra pairs (face diagonals), pair-averaged
            pi_, pj_ = pairs2
            Gp = np.einsum('bn,nb->b', Pa[pi_], Q[:, pj_]); Gq = np.einsum('bn,nb->b', Pa[pj_], Q[:, pi_])
            Rp2 = R1[pi_] * R1[pj_] - Gp * Gq
            zi, zj = z[pi_], z[pj_]
            row.append((zi * zj + Rp2 * (1. - zi * zj)).mean())   # s^z s^z + (s^x s^x + s^y s^y): 1 + (-i zi)(-i zj) = 1 - zi zj
        samples.append(row)
        if time.time() - t0 > tlimit:
            break
    return np.array(samples), dict(acc=acc, drift=drift, secs=time.time() - t0)


def ring_sparse(cl, plaq):
    """sum over faces of P + P^-1 on 2^N (permutation matrices)."""
    import scipy.sparse as sp
    N = cl.N; D = 2 ** N; b = np.arange(D, dtype=np.int64)
    rows, cols = [], []
    for pq in plaq:
        bitsq = [(b >> int(p)) & 1 for p in pq]
        for sh in (1, -1):
            nb = b.copy()
            for k in range(4):
                nb &= ~(np.int64(1) << int(pq[k]))
            for k in range(4):
                nb |= bitsq[(k - sh) % 4] << int(pq[k])
            rows.append(nb); cols.append(b)
    r = np.concatenate(rows).astype(np.int32); c = np.concatenate(cols).astype(np.int32)
    M = sp.csr_matrix((np.ones(len(r)), (r, c)), shape=(D, D)); M.sum_duplicates()
    return M
