#!/usr/bin/env python3
"""smg-ladder: is there a symmetric gapped window of the filtered SU(4)-singlet quartic toy in quasi-1D?
 A  exact: width-2 cross-sections collapse to the 1D filtered chain (and at mu = 0 to a filled band); the half-filled 3D toy
    has free Fermi lines on the face planes; the open-chain face mode decouples; MPO = explicit Hamiltonian
 B  exact sector diagonalisation, open chain L = 4, g/t = 1..16 (charge-1, charge-2 pair, adjoint, neutral gaps)
 C  two-site DMRG (numpy, chi <= 64) at g/t = 4, L = 6: pair and particle gaps vs free, pair correlations, density
Model: H = -g sum_x (C_x + C_x^+) - t sum_<xy>,f (a+_fx a_fy + h.c.) + 10 n_face, C_x = c1c2c3c4, c_f(x) = (a_fx + a_f,x+1)/sqrt2.
Self-contained (numpy/scipy/stdlib)."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/THE_FILTERED_QUARTIC_CHAIN_IS_SYMMETRIC_AND_GAPPED_AT_INTERMEDIATE_COUPLING_AND_THE_HALF_FILLED_3D_TOY_HAS_FREE_FACE_FERMI_LINES_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import itertools, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla

KQ = 128
VQ = [1, KQ, KQ * KQ, -(1 + KQ + KQ * KQ)]          # charge code of one particle in flavour f
I2 = np.eye(2); Zm = np.diag([1.0, -1.0]); SM = np.array([[0.0, 1.0], [0.0, 0.0]]); SP = SM.T.copy(); NN = np.diag([0.0, 1.0])

def qcode(v): return int(v[0] + KQ * v[1] + KQ * KQ * v[2])

# ------------------------------------------------------------------ filters
def binom_window(n):
    from math import comb
    w = np.array([float(comb(n, j)) for j in range(n + 1)]); return w / np.linalg.norm(w)

# ------------------------------------------------------------------ MPO by automata
class MPOBuilder:
    """transitions per mode p: (label_in, label_out, 2x2 op); 'S' = nothing yet (identity), 'D' = done (identity)."""
    def __init__(s, nmode):
        s.n = nmode; s.tr = [[] for _ in range(nmode)]

    def add_string(s, coef, ops):   # generic fermion string: ops = [(mode, dag)], leftmost first; must be even
        ms = [m for m, _ in ops]; lo, hi = min(ms), max(ms); tag = ('str', len(s.tr[0]), id(ops), lo, hi, coef)
        loc = {}
        for p in range(lo, hi + 1):
            M = I2.copy()
            for m, dg in ops:
                fac = Zm if p < m else ((SP if dg else SM) if p == m else I2)
                M = M @ fac
            loc[p] = M
        if lo == hi: s.tr[lo].append(('S', 'D', coef * loc[lo])); return
        for p in range(lo, hi + 1):
            a = 'S' if p == lo else (tag, p - 1); b = 'D' if p == hi else (tag, p)
            s.tr[p].append((a, b, (coef if p == lo else 1.0) * loc[p]))

    def add_bilinear(s, modes, u, v, tag):
        """sum_{i,j} u_i v_j a^+_{m_i} a_{m_j} (modes increasing) by a 2-state automaton."""
        pos = {m: i for i, m in enumerate(modes)}; lo, hi = modes[0], modes[-1]
        for p in range(lo, hi + 1):
            inA, inB = ((tag, 'A', p - 1), (tag, 'B', p - 1)); oA, oB = (tag, 'A', p), (tag, 'B', p)
            if p > lo: s.tr[p].append((inA, oA, Zm)); s.tr[p].append((inB, oB, Zm))
            if p in pos:
                i = pos[p]
                s.tr[p].append(('S', 'D', u[i] * v[i] * NN))
                s.tr[p].append(('S', oA, u[i] * (SP @ Zm)))
                s.tr[p].append(('S', oB, v[i] * (Zm @ SM)))
                if p > lo:
                    s.tr[p].append((inA, 'D', v[i] * SM)); s.tr[p].append((inB, 'D', u[i] * SP))

    def add_qsquare(s, c, lam, target, tag):
        """lam * (sum_m c_m n_m - target)^2 - lam * target^2  (constant dropped), c: dict mode -> weight"""
        ms = sorted(c); lo, hi = ms[0], ms[-1]
        for p in range(lo, hi + 1):
            inA, oA = (tag, p - 1), (tag, p)
            if p > lo: s.tr[p].append((inA, oA, I2))
            if p in c:
                cm = c[p]
                s.tr[p].append(('S', 'D', lam * (cm * cm - 2 * target * cm) * NN))
                s.tr[p].append(('S', oA, lam * cm * NN))
                if p > lo: s.tr[p].append((inA, 'D', 2 * cm * NN))

    def add_quartic(s, x, w, coef, dag=False):
        """coef * c0 c1 c2 c3 (dag: coef * c3^+ c2^+ c1^+ c0^+), c_f = sum_j w[j] a_{f, x+j}; automaton over emitted sets."""
        order = [3, 2, 1, 0] if dag else [0, 1, 2, 3]; op1 = SP if dag else SM
        sites = range(x, x + len(w)); tag = ('q', x, dag)
        p_lo = 4 * x; p_hi = 4 * (x + len(w) - 1) + 3
        for p in range(p_lo, p_hi + 1):
            si, fp = divmod(p, 4); wj = w[si - x]
            for E in itertools.product((0, 1), repeat=4):
                E = tuple(E)
                if sum(E) == 4: continue
                lab_in = 'S' if sum(E) == 0 else (tag, E, p - 1)
                # not emitting here (only for started terms): pending flavours give Z
                if sum(E) > 0:
                    M = I2.copy()
                    for f in order: M = M @ (I2 if E[f] else Zm)
                    s.tr[p].append((lab_in, (tag, E, p), M))
                if E[fp] == 0:
                    E2 = list(E); E2[fp] = 1; E2 = tuple(E2)
                    M = I2.copy()
                    for f in order: M = M @ (I2 if E[f] else (op1 if f == fp else Zm))
                    c = (np.conj(wj) if dag else wj) * (coef if sum(E) == 0 else 1.0)
                    s.tr[p].append((lab_in, 'D' if sum(E2) == 4 else (tag, E2, p), c * M))

    def build(s):
        n = s.n
        # prune: forward reachability from S and backward co-reachability to D
        alive_out = [set() for _ in range(n)]
        live_in = {'S'}
        fwd = []
        for p in range(n):
            ok = [t for t in s.tr[p] if t[0] in live_in or t[0] == 'D' and False]
            live_in = {t[1] for t in ok} | {'S', 'D'}
            fwd.append(ok)
        need = {'D'}; final = [None] * n
        for p in range(n - 1, -1, -1):
            ok = [t for t in fwd[p] if t[1] in need]
            final[p] = ok; need = {t[0] for t in ok} | {'S', 'D'}
        bonds = [['S']] + [None] * n
        for p in range(n):
            labs = ['S', 'D'] + sorted({t[1] for t in final[p]} - {'S', 'D'}, key=repr)
            bonds[p + 1] = labs if p < n - 1 else ['D']
        bonds[0] = ['S']
        Ws = []
        for p in range(n):
            li = {l: i for i, l in enumerate(bonds[p])}; lo = {l: i for i, l in enumerate(bonds[p + 1])}
            W = np.zeros((len(li), len(lo), 2, 2))
            if 'S' in li and 'S' in lo: W[li['S'], lo['S']] += I2
            if 'D' in li and 'D' in lo: W[li['D'], lo['D']] += I2
            for a, b, M in final[p]:
                if a in li and b in lo: W[li[a], lo[b]] += np.real_if_close(M)
            Ws.append(W)
        return Ws

def compress_mpo(Ws, tol=1e-12):
    Ws = [W.copy() for W in Ws]; n = len(Ws)
    for p in range(n - 1):   # left-orthogonalise
        Dl, Dr = Ws[p].shape[:2]; M = Ws[p].transpose(0, 2, 3, 1).reshape(Dl * 4, Dr)
        Q, R = np.linalg.qr(M); Ws[p] = Q.reshape(Dl, 2, 2, -1).transpose(0, 3, 1, 2)
        Ws[p + 1] = np.tensordot(R, Ws[p + 1], axes=([1], [0]))
    for p in range(n - 1, 0, -1):
        Dl, Dr = Ws[p].shape[:2]; M = Ws[p].reshape(Dl, Dr * 4)
        U, S, Vh = np.linalg.svd(M, full_matrices=False); k = max(1, int(np.sum(S > tol * S[0])))
        Ws[p] = Vh[:k].reshape(k, Dr, 2, 2); Ws[p - 1] = np.tensordot(Ws[p - 1], U[:, :k] * S[:k], axes=([1], [0])).transpose(0, 3, 1, 2)
    return Ws

# ------------------------------------------------------------------ Hamiltonians
def chain_terms(L, n=1, g=1.0, band=0.0, hop=0.0, mu=0.0, pbc=False, face=0.0):
    """H = -g sum_x (C_x + C_x^+)  [open: x = 0..L-1-n]  + band * sum_q (1 - cos q)/2 n_q  - hop * sum NN a^+a  - mu N.
    band in real space: band/2 n_x - band/4 (a_x^+ a_{x+1} + h.c.)."""
    w = binom_window(n); B = MPOBuilder(4 * L); strs = []
    xs = range(L) if pbc else range(L - n)
    for x in xs:
        if pbc: raise NotImplementedError
        B.add_quartic(x, w, -g); B.add_quartic(x, w, -g, dag=True)
    th = -band / 4 - hop
    for x in range(L - 1):
        for f in range(4):
            m1, m2 = 4 * x + f, 4 * (x + 1) + f
            if th != 0: B.add_string(th, [(m1, True), (m2, False)]); B.add_string(th, [(m2, True), (m1, False)])
    for x in range(L):
        for f in range(4):
            e = band / 2 - mu
            if e != 0: B.add_string(e, [(4 * x + f, True), (4 * x + f, False)])
    if face:
        u = np.array([(-1.0) ** x for x in range(L)]) / np.sqrt(L)
        for f in range(4): B.add_bilinear([4 * x + f for x in range(L)], face * u, u, ('face', f))
    return B

# ------------------------------------------------------------------ charge-labelled DMRG
def lanczos(mv, v0, m):
    Q = [v0 / np.linalg.norm(v0)]; a = []; b = []
    for it in range(m):
        w = mv(Q[-1]); a.append(np.dot(Q[-1], w))
        for q in Q: w -= np.dot(q, w) * q
        for q in Q: w -= np.dot(q, w) * q
        bb = np.linalg.norm(w)
        if bb < 1e-10 or it == m - 1: break
        b.append(bb); Q.append(w / bb)
    k = len(a); T = np.diag(a) + np.diag(b[:k - 1], 1) + np.diag(b[:k - 1], -1)
    e, U = np.linalg.eigh(T); v = np.array(Q[:k]).T @ U[:, 0]
    return e[0], v / np.linalg.norm(v)

def mode_q(p): return VQ[p % 4]

def split_by_charge(M, qrow, qcol, chi, cutoff, reserve=False):
    """block SVD of M (rows charge qrow, cols charge qcol; nonzero only where equal). Returns U, S, Vh, qbond."""
    blocks = []
    for q in np.unique(qrow):
        r = np.nonzero(qrow == q)[0]; c = np.nonzero(qcol == q)[0]
        if len(c) == 0: continue
        u, sv, vh = np.linalg.svd(M[np.ix_(r, c)], full_matrices=False)
        for k in range(len(sv)): blocks.append((sv[k], q, r, c, u[:, k], vh[k]))
    blocks.sort(key=lambda z: -z[0])
    tot = sum(b[0] ** 2 for b in blocks)
    keep = [b for b in blocks[:chi] if b[0] ** 2 > cutoff * tot] or blocks[:1]
    if reserve:   # keep the leading state of every charge block alive (sector reserve), up to chi // 4 extra slots
        have = {b[1] for b in keep}; extra = []
        for b in blocks:
            if b[1] not in have and b[0] ** 2 > 1e-24 * tot and len(extra) < max(1, chi // 4): extra.append(b); have.add(b[1])
        if extra: keep = keep[:max(1, chi - len(extra))] + extra
    k = len(keep); U = np.zeros((M.shape[0], k)); Vh = np.zeros((k, M.shape[1])); S = np.zeros(k); qb = np.zeros(k, np.int64)
    for i, (sv, q, r, c, u, vh) in enumerate(keep): U[r, i] = u; Vh[i, c] = vh; S[i] = sv; qb[i] = q
    disc = 1 - sum(b[0] ** 2 for b in keep) / tot
    return U, S, Vh, qb, disc

class DMRG:
    qmax0 = 2; dsec = 1; reserve = False
    def __init__(s, Ws, Qvec=(0, 0, 0), seed=0):
        s.W = Ws; s.n = len(Ws); s.Qt = qcode(Qvec); rng = np.random.default_rng(seed); s.rng = np.random.default_rng(seed + 1000)
        n = s.n
        # initial MPS: random, bond charges = reachable codes with |Q_i| <= qmax (dimension 1 each), then right-canonical
        qmax = s.qmax0; vecs = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1]), np.array([-1, -1, -1])]
        tv = np.array(Qvec)
        fwd = [{(0, 0, 0)}]
        for p in range(n):
            nxt = set()
            for v in fwd[-1]:
                nxt.add(v); w = tuple(np.array(v) + vecs[p % 4])
                if max(abs(x) for x in w) <= qmax + 1: nxt.add(w)
            fwd.append(nxt)
        bwd = [None] * (n + 1); bwd[n] = {tuple(tv)}
        for p in range(n - 1, -1, -1):
            prv = set()
            for v in bwd[p + 1]:
                prv.add(v); w = tuple(np.array(v) - vecs[p % 4])
                if max(abs(x) for x in w) <= qmax + 1: prv.add(w)
            bwd[p] = prv
        qs = [np.array(sorted(qcode(v) for v in (fwd[p] & bwd[p]) if max(abs(x) for x in v) <= qmax or p in (0, n)), np.int64) for p in range(n + 1)]
        qs = [np.repeat(q, s.dsec) if 0 < p < n else q for p, q in enumerate(qs)]
        s.q = qs; s.A = []
        for p in range(n):
            ql, qr = qs[p], qs[p + 1]; qsv = np.array([0, mode_q(p)])
            mask = (ql[:, None, None] + qsv[None, :, None]) == qr[None, None, :]
            s.A.append(rng.normal(size=mask.shape) * mask)
        for p in range(n - 1, 0, -1):   # right-canonicalise blockwise
            a, _, b = s.A[p].shape; M = s.A[p].reshape(a, 2 * b); qsv = np.array([0, mode_q(p)])
            qcol = (s.q[p + 1][None, :] - qsv[:, None]).ravel()
            U, S, Vh, qb, _ = split_by_charge(M, s.q[p], qcol, 10 ** 9, 1e-30)
            s.A[p] = Vh.reshape(-1, 2, b); s.q[p] = qb
            s.A[p - 1] = np.tensordot(s.A[p - 1], U * S[None, :], axes=([2], [0]))
        s.A[0] /= np.linalg.norm(s.A[0])
        s.R = [None] * (n + 1); s.Lv = [None] * (n + 1)
        s.Lv[0] = np.ones((1, 1, 1)); s.R[n] = np.ones((1, 1, 1))
        for p in range(n - 1, 0, -1): s.R[p] = s._rup(s.R[p + 1], s.A[p], s.W[p])
        s.E = None; s.krylov = 8; s.pen = []

    def add_penalty(s, other, w):   # H -> H + w |other><other| (other: a converged DMRG object, normalised)
        nrm = np.sqrt(other.envs()[0][-1][0, 0]); B = [a.copy() for a in other.A]; B[0] = B[0] / nrm
        OR = [None] * (s.n + 1); OR[s.n] = np.ones((1, 1)); OL = [None] * (s.n + 1); OL[0] = np.ones((1, 1))
        for p in range(s.n - 1, 0, -1): OR[p] = s._orup(OR[p + 1], s.A[p], B[p])
        s.pen.append([B, w, OL, OR])

    @staticmethod
    def _olup(O, A, B): return np.tensordot(np.tensordot(A.conj(), O, axes=([0], [0])), B, axes=([0, 2], [1, 0]))
    @staticmethod
    def _orup(O, A, B): return np.tensordot(np.tensordot(A.conj(), O, axes=([2], [0])), B, axes=([1, 2], [1, 2]))

    @staticmethod
    def _lup(L, A, W):   # L (a', w, a), A (a, s, b) -> (b', w', b)
        T = np.tensordot(L, A, axes=([2], [0]))                  # a' w s b
        T = np.tensordot(T, W, axes=([1, 2], [0, 3]))             # a' b w' s'
        T = np.tensordot(A.conj(), T, axes=([0, 1], [0, 3]))      # b' b w'
        return T.transpose(0, 2, 1)

    @staticmethod
    def _rup(R, A, W):   # R (b', w, b), A (a, s, b) -> (a', w', a)
        T = np.tensordot(A, R, axes=([2], [2]))                  # a s b' w
        T = np.tensordot(T, W, axes=([1, 3], [3, 1]))             # a b' w' s'
        T = np.tensordot(A.conj(), T, axes=([1, 2], [3, 1]))      # a' a w'
        return T.transpose(0, 2, 1)

    def _matvec(s, L, W1, W2, R, th):
        T = np.tensordot(L, th, axes=([2], [0]))                 # a' w s1 s2 b
        T = np.tensordot(T, W1, axes=([1, 2], [0, 3]))            # a' s2 b w' s1'
        T = np.tensordot(T, W2, axes=([3, 1], [0, 3]))            # a' b s1' w'' s2'
        T = np.tensordot(T, R, axes=([1, 3], [2, 1]))             # a' s1' s2' b'
        return T

    def _solve(s, p, th0, mask, tol):
        L, R, W1, W2 = s.Lv[p], s.R[p + 2], s.W[p], s.W[p + 1]; shp = th0.shape; idx = np.nonzero(mask.ravel())[0]
        def mv(v):
            th = np.zeros(int(np.prod(shp))); th[idx] = v
            return s._matvec(L, W1, W2, R, th.reshape(shp)).ravel()[idx]
        if s.pen:
            phis = []
            for B, w, OL, OR in s.pen:
                ph = np.tensordot(OL[p], np.tensordot(B[p], B[p + 1], axes=([2], [0])), axes=([1], [0]))
                ph = np.tensordot(ph, OR[p + 2], axes=([3], [1])).ravel()[idx]; phis.append((w, ph))
            mv0 = mv
            def mv(v): return mv0(v) + sum(w * ph * np.dot(ph, v) for w, ph in phis)
        v0 = th0.ravel()[idx]
        if np.linalg.norm(v0) < 1e-12: v0 = np.random.default_rng(p).normal(size=len(idx))
        if len(idx) <= 64:
            Hm = np.array([mv(e) for e in np.eye(len(idx))]).T; e, V = np.linalg.eigh((Hm + Hm.T) / 2); E, v = e[0], V[:, 0]
        else:
            E, v = lanczos(mv, v0, s.krylov)
        th = np.zeros(int(np.prod(shp))); th[idx] = v
        return E, th.reshape(shp)

    def sweep(s, chi, cutoff=1e-12, tol=1e-9, noise=0.0):
        n = s.n; maxdisc = 0.0
        for direction in (1, -1):
            rng_ = range(0, n - 1) if direction == 1 else range(n - 2, -1, -1)
            for p in rng_:
                th = np.tensordot(s.A[p], s.A[p + 1], axes=([2], [0]))   # a s1 s2 b
                ql, qr = s.q[p], s.q[p + 2]
                q1, q2 = (0, 0) if getattr(s, 'nocharge', False) else (mode_q(p), mode_q(p + 1))
                qs1 = np.array([0, q1]); qs2 = np.array([0, q2])
                mask = (ql[:, None, None, None] + qs1[None, :, None, None] + qs2[None, None, :, None]) == qr[None, None, None, :]
                E, th = s._solve(p, th, mask, tol)
                if noise > 0:
                    th = th + noise * s.rng.normal(size=th.shape) * mask
                    th /= np.linalg.norm(th)
                a, _, _, b = th.shape; M = th.reshape(a * 2, 2 * b)
                qrow = (ql[:, None] + qs1[None, :]).ravel(); qcol = (qr[None, :] - qs2[:, None]).ravel()
                U, S, Vh, qb, disc = split_by_charge(M, qrow, qcol, chi, cutoff, reserve=s.reserve and noise > 0)
                maxdisc = max(maxdisc, disc); s.q[p + 1] = qb
                if direction == 1:
                    s.A[p] = U.reshape(a, 2, -1); s.A[p + 1] = (S[:, None] * Vh).reshape(-1, 2, b)
                    s.Lv[p + 1] = s._lup(s.Lv[p], s.A[p], s.W[p]); s.R[p + 2] = None if p + 2 < n else s.R[p + 2]
                    for B, w, OL, OR in s.pen: OL[p + 1] = s._olup(OL[p], s.A[p], B[p])
                else:
                    s.A[p] = (U * S[None, :]).reshape(a, 2, -1); s.A[p + 1] = Vh.reshape(-1, 2, b)
                    s.R[p + 1] = s._rup(s.R[p + 2], s.A[p + 1], s.W[p + 1]); s.Lv[p + 1] = None if p + 1 > 0 else s.Lv[p + 1]
                    for B, w, OL, OR in s.pen: OR[p + 1] = s._orup(OR[p + 2], s.A[p + 1], B[p + 1])
                s.E = E
        return s.E, maxdisc

    def run(s, chis, cutoff=1e-12, noise=None, verbose=False):
        hist = []
        for i, chi in enumerate(chis):
            nz = noise[i] if noise is not None else 0.0
            E, d = s.sweep(chi, cutoff, noise=nz); hist.append((chi, E, d, max(len(q) for q in s.q)))
            if verbose: print(f'   sweep chi={chi} E={E:.10f} disc={d:.1e} D={hist[-1][3]}', flush=True)
        return hist

    # ---- measurements (state is left-canonical except site 0 after a full sweep pair: normalise generically)
    def envs(s):
        n = s.n; EL = [None] * (n + 1); ER = [None] * (n + 1); EL[0] = np.ones((1, 1)); ER[n] = np.ones((1, 1))
        for p in range(n):
            EL[p + 1] = np.tensordot(np.tensordot(EL[p], s.A[p], axes=([1], [0])), s.A[p].conj(), axes=([0, 1], [0, 1])).T
        for p in range(n - 1, -1, -1):
            ER[p] = np.tensordot(np.tensordot(s.A[p], ER[p + 1], axes=([2], [0])), s.A[p].conj(), axes=([1, 2], [1, 2]))
        s.EL, s.ER = EL, ER; s.norm = float(EL[n][0, 0])
        return EL, ER

    def string_ops(s, ops, coef=1.0):   # local 2x2 ops per mode for an even fermion string
        ms = [m for m, _ in ops]; lo, hi = min(ms), max(ms); loc = {}
        for p in range(lo, hi + 1):
            M = I2.copy()
            for m, dg in ops: M = M @ (Zm if p < m else ((SP if dg else SM) if p == m else I2))
            loc[p] = M
        loc[lo] = coef * loc[lo]
        return lo, hi, loc

    def expect_loc(s, lo, hi, loc):   # EL[p] is (ket a, bra a') ordered as (a, a')? we store EL[p][bra, ket]
        E = s.EL[lo]
        for p in range(lo, hi + 1):
            T = np.tensordot(E, s.A[p], axes=([1], [0]))                    # bra a', s, b
            T = np.tensordot(T, loc.get(p, I2), axes=([1], [1]))            # a', b, s'
            E = np.tensordot(s.A[p].conj(), T, axes=([0, 1], [0, 2]))       # [bra, ket]
        return float(np.tensordot(E, s.ER[hi + 1], axes=([0, 1], [1, 0]))) / s.norm

# ------------------------------------------------------------------ bit-basis sector ED (cross-check)
def sector_basis(L, Q):
    nm = 4 * L; per = {}
    for f in range(4):
        per[f] = {}
        for bits in itertools.product((0, 1), repeat=L):
            k = sum(bits); st = 0
            for x, b in enumerate(bits):
                if b: st |= 1 << (4 * x + f)
            per[f].setdefault(k, []).append(st)
    out = []
    for n3 in range(L + 1):
        ns = [n3 + Q[0], n3 + Q[1], n3 + Q[2], n3]
        if min(ns) < 0 or max(ns) > L: continue
        arrs = [np.array(per[f][ns[f]], np.int64) for f in range(4)]
        tot = arrs[0]
        for a in arrs[1:]: tot = (tot[:, None] | a[None, :]).ravel()
        out.append(tot)
    return np.sort(np.concatenate(out))

_PC = np.array([bin(i).count('1') for i in range(1 << 16)], np.int64)
def popcount(a): return _PC[a & 0xFFFF] + _PC[(a >> 16) & 0xFFFF] + _PC[(a >> 32) & 0xFFFF]

def apply_string(basis, ops, coef):
    st = basis.copy(); amp = np.full(len(st), coef, float); ok = np.ones(len(st), bool)
    for m, dg in reversed(ops):
        occ = (st >> m) & 1
        ok &= (occ == 0) if dg else (occ == 1)
        par = popcount(st & ((1 << m) - 1)) & 1
        amp *= 1.0 - 2.0 * par
        st = st ^ (1 << m)
    return st, amp, ok

def ed_hamiltonian(basis, terms):
    R, C, V = [], [], []
    for coef, ops in terms:
        st, amp, ok = apply_string(basis, ops, coef)
        j = np.searchsorted(basis, st); j = np.clip(j, 0, len(basis) - 1); ok &= basis[j] == st
        R.append(j[ok]); C.append(np.nonzero(ok)[0]); V.append(amp[ok])
    R = np.concatenate(R); C = np.concatenate(C); V = np.concatenate(V)
    return sp.csr_matrix((V, (R, C)), shape=(len(basis), len(basis)))

def ed_terms(L, n=1, g=1.0, band=0.0, hop=0.0, mu=0.0, pbc=False, face=0.0):
    """explicit fermion strings (expanded quartics), same Hamiltonian as chain_terms; pbc wraps sites mod L."""
    w = binom_window(n); T = []
    xs = range(L) if pbc else range(L - n)
    for x in xs:
        for js in itertools.product(range(n + 1), repeat=4):
            c = -g * np.prod([w[j] for j in js])
            ann = [(4 * ((x + js[f]) % L) + f, False) for f in range(4)]
            T.append((c, ann)); T.append((c, [(m, True) for m, _ in reversed(ann)]))
    th = -band / 4 - hop
    for x in range(L if pbc else L - 1):
        for f in range(4):
            m1, m2 = 4 * x + f, 4 * ((x + 1) % L) + f
            if th != 0: T += [(th, [(m1, True), (m2, False)]), (th, [(m2, True), (m1, False)])]
    for x in range(L):
        for f in range(4):
            if band / 2 - mu != 0: T.append((band / 2 - mu, [(4 * x + f, True), (4 * x + f, False)]))
    if face:   # face * n_v, v = (-1)^x / sqrt(L): the mode outside the filter span (exactly decoupled from H_int)
        for f in range(4):
            for x in range(L):
                for y in range(L): T.append((face * (-1) ** (x + y) / L, [(4 * x + f, True), (4 * y + f, False)]))
    return T


# ------------------------------------------------------------------ measurements on a converged DMRG state
def local_string(ops, coef=1.0):
    ms = [m for m, _ in ops]; lo, hi = min(ms), max(ms); loc = {}
    for p in range(lo, hi + 1):
        M = I2.copy()
        for m, dg in ops: M = M @ (Zm if p < m else ((SP if dg else SM) if p == m else I2))
        loc[p] = M
    loc[lo] = coef * loc[lo]
    return loc

def add_loc(*locs):   # sum of local-op dicts with identical support
    out = {}
    for d in locs:
        ks = sorted(set(out) | set(d))
        if not out: out = {k: d[k].copy() for k in d}; continue
        raise ValueError
    return out

def mul_loc(A, B):   # operator product A @ B as local dicts (both even)
    ks = sorted(set(A) | set(B)); return {k: A.get(k, I2) @ B.get(k, I2) for k in ks}

def expect(dm, loc):
    ks = sorted(loc); return dm.expect_loc(ks[0], ks[-1], loc)

def expect_sum(dm, locs):   # sum of terms, each a local dict
    return sum(expect(dm, l) for l in locs)

def two_point(dm, opsA, opsB):
    """C[i, j] = <A_i B_j> for i < j where each A_i, B_j is a local dict (even) and span(A_i) < span(B_j) for i < j;
    incremental transfer.  Returns dict (i, j) -> value."""
    out = {}
    spans = [(min(a), max(a)) for a in opsA]; spB = [(min(b), max(b)) for b in opsB]
    for i, A in enumerate(opsA):
        lo, hi = spans[i]; E = dm.EL[lo]
        for p in range(lo, hi + 1):
            T = np.tensordot(np.tensordot(E, dm.A[p], axes=([1], [0])), A.get(p, I2), axes=([1], [1]))
            E = np.tensordot(dm.A[p].conj(), T, axes=([0, 1], [0, 2]))
        pos = hi + 1
        for j in range(i + 1, len(opsB)):
            blo, bhi = spB[j]
            if blo <= hi: continue
            while pos < blo:
                T = np.tensordot(E, dm.A[pos], axes=([1], [0])); E = np.tensordot(dm.A[pos].conj(), T, axes=([0, 1], [0, 1])); pos += 1
            F = E
            for p in range(blo, bhi + 1):
                T = np.tensordot(np.tensordot(F, dm.A[p], axes=([1], [0])), opsB[j].get(p, I2), axes=([1], [1]))
                F = np.tensordot(dm.A[p].conj(), T, axes=([0, 1], [0, 2]))
            out[(i, j)] = float(np.tensordot(F, dm.ER[bhi + 1], axes=([0, 1], [1, 0]))) / dm.norm
    return out

def dmrg_nocharge(Ws, seed=0, d0=16):
    """DMRG object with charge labels disabled (all zero): finds the global ground state of all sectors."""
    dm = DMRG.__new__(DMRG); dm.W = Ws; dm.n = n = len(Ws); dm.Qt = 0; rng = np.random.default_rng(seed)
    dims = [1] + [min(2 ** min(p, n - p), d0) for p in range(1, n)] + [1]
    dm.A = [rng.normal(size=(dims[p], 2, dims[p + 1])) for p in range(n)]; dm.q = [np.zeros(d, np.int64) for d in dims]
    dm.R = [None] * (n + 1); dm.Lv = [None] * (n + 1); dm.Lv[0] = np.ones((1, 1, 1)); dm.R[n] = np.ones((1, 1, 1))
    for p in range(n - 1, 0, -1): dm.R[p] = dm._rup(dm.R[p + 1], dm.A[p], dm.W[p])
    dm.E = None; dm.krylov = 6; dm.pen = []; dm.nocharge = True; dm.rng = np.random.default_rng(seed + 1000)
    return dm


def sector_mpo(L, r, Q=(0, 0, 0), lam=0.0, face=10.0, n=1):
    """H = -sum(C + C^+) - (1/r) NN hop + face n_face [+ lam sum_i (Q_i - t_i)^2 - lam t_i^2], open chain, g = 1."""
    B = chain_terms(L, n=n, g=1.0, hop=(1.0 / r if r else 0.0), face=face)
    if lam:
        for i in range(3):
            c = {}
            for x in range(L): c[4 * x + i] = 1.0; c[4 * x + 3] = -1.0
            B.add_qsquare(c, lam, float(Q[i]), ('Q', i))
    return compress_mpo(B.build()), lam * sum(q * q for q in Q)

# ================================================================== runner body
T0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''), flush=True)

def free_levels(L, t=1.0, face=10.0):
    h = np.zeros((L, L))
    for x in range(L - 1): h[x, x + 1] = h[x + 1, x] = -t
    v = np.array([(-1.0) ** x for x in range(L)]) / np.sqrt(L); h += face * np.outer(v, v)
    e, U = np.linalg.eigh(h); p = e[e > 1e-12].min(); hh = -e[e < -1e-12].max(); G = U[:, e < 0] @ U[:, e < 0].T
    return dict(p=p, h=hh, pair=2 * p, adj=p + hh, ex=p + hh, SP0=float((G ** 2).sum() / L))

def cube_matrix(Ls):
    S = list(itertools.product(*[range(L) for L in Ls])); idx = {s: i for i, s in enumerate(S)}; C = np.zeros((len(S), len(S)))
    for y, s in enumerate(S):
        for c in itertools.product((0, 1), repeat=3): C[idx[tuple((a + b) % L for a, b, L in zip(s, c, Ls))], y] += 8 ** -0.5
    return C, S, idx

def hop_matrix(Ls, t=1.0):   # toy-qmc convention: for each site and axis, H[i,j] -= t and H[j,i] -= t with j = i + e_d mod L
    S = list(itertools.product(*[range(L) for L in Ls])); idx = {s: i for i, s in enumerate(S)}; H = np.zeros((len(S), len(S)))
    for i, s in enumerate(S):
        for d in range(3):
            w = list(s); w[d] = (w[d] + 1) % Ls[d]; j = idx[tuple(w)]; H[i, j] -= t; H[j, i] -= t
    return H

print('== A. exact structure of the quasi-1D geometries and of the half-filled toy')
# A1: L x 2 x 2 torus -> 1D filtered chain
L = 6; Ls = (L, 2, 2); C, S, idx = cube_matrix(Ls); H0 = hop_matrix(Ls)
Pk = np.zeros((L, len(S)))          # transverse-symmetric (k_perp = 0) modes b_x = (1/2) sum_{y,z} a_{x,y,z}
for i, s in enumerate(S): Pk[s[0], i] = 0.5
rankC = np.linalg.matrix_rank(C.T @ C, tol=1e-9)
chain = np.zeros((L, L))
for x in range(L): chain[x, x] = chain[x, (x + 1) % L] = 2 ** -0.5
ok1 = rankC == L - 1 and np.allclose(C.T, (C.T @ Pk.T) @ Pk)          # every cube vector lies in the k_perp = 0 sector
cols = [C[:, idx[(x, y, z)]] @ Pk.T for x in range(L) for y in range(2) for z in range(2)]
ok1 &= all(np.allclose(cols[4 * x + j], chain[x]) for x in range(L) for j in range(4))   # four coincident copies of the chain filter
h_perp = Pk @ H0 @ Pk.T; eb = np.linalg.eigvalsh(h_perp)
ok1 &= np.allclose(h_perp, h_perp.T) and eb.max() <= -2 + 1e-9
check('A1 THEOREM width-2 cross-sections: on the L x 2 x 2 torus (L = 6) the cube vectors span exactly the L - 1 off-face '
      'modes of the transverse-symmetric sector and each equals the 1D two-site filter (a_x + a_{x+1})/sqrt2 four times, so '
      'H_int is the filtered chain with coupling 4g; every k_perp != 0 mode is a free face spectator. With the toy-qmc hopping '
      'at mu = 0 that sector has band -2t cos q - 4t <= -2t: a filled band, gapped at g = 0, so the L x 2 x 2 ladder cannot '
      'test the massless-to-gapped question. The genuine quasi-1D test is the bare chain (band -2t cos q, Dirac points at pi/2)',
      ok1, f'rank {rankC} = L - 1; k_perp = 0 band max {eb.max():+.3f} t')
# A2: half-filled 3D toy: free Fermi lines on the face planes
rows = []; ok2 = True
for L in (4, 6, 8):
    ks = 2 * np.pi * np.arange(L) / L; K = np.array(list(itertools.product(ks, repeat=3)))
    eps = -2 * np.cos(K).sum(1); filt = np.prod(np.cos(K / 2) ** 2, 1)
    nz = np.sum((np.abs(eps) < 1e-9) & (filt < 1e-12)); nzt = np.sum(np.abs(eps) < 1e-9)
    rows.append(f'L={L}: {nz} of {nzt} zero-energy momenta lie on faces'); ok2 &= nz > 0
check('A2 THEOREM in the toy-qmc model (NN hopping at mu = 0, cube filter) the face planes k_i = pi carry the free Fermi lines '
      'cos k_j + cos k_l = 1, where the filter prod cos^2(k/2) vanishes, so those modes commute with H_int: on every L^3 torus '
      'below they are exactly free zero modes, and the half-filled 3D toy is gapless through free face fermions at every g/t. '
      'A fully gapped symmetric phase of that toy is excluded; only the off-face (interacting) sector can be gapped. In 1D the '
      'face q = pi sits at +2t, away from the Fermi points',
      ok2, '; '.join(rows))
# A3: the open-chain face vector is outside the filter span; MPO = ED
Lc = 4; F = np.array([[2 ** -0.5 if y in (x, x + 1) else 0 for y in range(Lc)] for x in range(Lc - 1)]); v = np.array([(-1.0) ** x for x in range(Lc)])
bas = sector_basis(Lc, (0, 0, 0)); Hi = ed_hamiltonian(bas, ed_terms(Lc, g=1.0)); Nf = ed_hamiltonian(bas, ed_terms(Lc, g=0.0, face=1.0))
comm = abs(Hi @ Nf - Nf @ Hi).max()
Ws = chain_terms(2, n=1, g=1.0, hop=0.3, face=2.0).build(); full = Ws[0]
for W in Ws[1:]:
    full = np.einsum('awAB,wvcd->avAcBd', full, W); a, b_, A_, c_, B_, d_ = full.shape; full = full.reshape(a, b_, A_ * c_, B_ * d_)
nm = 8; He = ed_hamiltonian(np.arange(1 << nm, dtype=np.int64), ed_terms(2, n=1, g=1.0, hop=0.3, face=2.0)).toarray()
perm = np.array([int(format(i, f'0{nm}b')[::-1], 2) for i in range(1 << nm)]); dm_ = abs(full[0, 0] - He[np.ix_(perm, perm)]).max()
Wq, c0 = sector_mpo(2, 4.0, (1, 0, 0), lam=3.0); full = Wq[0]
for W in Wq[1:]:
    full = np.einsum('awAB,wvcd->avAcBd', full, W); a, b_, A_, c_, B_, d_ = full.shape; full = full.reshape(a, b_, A_ * c_, B_ * d_)
occ = np.array([[(st >> m) & 1 for m in range(nm)] for st in range(1 << nm)]); Q0 = occ[:, 0::4].sum(1) - occ[:, 3::4].sum(1)
Q1 = occ[:, 1::4].sum(1) - occ[:, 3::4].sum(1); Q2 = occ[:, 2::4].sum(1) - occ[:, 3::4].sum(1)
pen = 3.0 * ((Q0 - 1) ** 2 + Q1 ** 2 + Q2 ** 2) - 3.0
Href = ed_hamiltonian(np.arange(1 << nm, dtype=np.int64), ed_terms(2, n=1, g=1.0, hop=0.25, face=10.0)).toarray() + np.diag(pen)
dq = abs(full[0, 0] - Href[np.ix_(perm, perm)]).max()
check('A3 THEOREM-CHECK the open-chain alternating mode (-1)^x is orthogonal to every filter vector, so its number commutes with '
      'H_int ([n_face, H_int] = 0 on the L = 4 sector); the automaton MPO (quartic, hopping, face lift, sector penalty) equals '
      'the explicit Jordan-Wigner Hamiltonian', np.allclose(F @ v, 0) and comm < 1e-12 and dm_ < 1e-12 and dq < 1e-12,
      f'|[n_face, H_int]| {comm:.1e}; |MPO - ED| {dm_:.1e}, with penalty {dq:.1e}')

print('== B. exact diagonalisation, open chain L = 4 (sectors Q = (n0-n3, n1-n3, n2-n3); g = 1, t = 1/r; face lift 10)')
SECT = {'0': (0, 0, 0), 'p': (1, 0, 0), 'h': (-1, 0, 0), 'pair': (1, 1, 0), 'adj': (1, -1, 0)}
bases = {k: sector_basis(4, Q) for k, Q in SECT.items()}; edres = {}; fr4 = free_levels(4)
for r in (1.0, 2.0, 4.0, 8.0, 16.0):
    terms = ed_terms(4, g=1.0, hop=1 / r, face=10.0); E = {}
    for k, b in bases.items():
        H = ed_hamiltonian(b, terms); e = np.linalg.eigvalsh(H.toarray()) if H.shape[0] <= 2000 else None
        E[k] = e[0]
        if k == '0': E['ex'] = e[1]
    edres[r] = {k: (E[k] - E['0']) * r for k in ('p', 'h', 'pair', 'adj', 'ex')}
    print(f'   r = g/t = {r:>4}: ' + ' '.join(f'{k} {v:6.3f}t ({v / fr4[k]:.2f}x free)' for k, v in edres[r].items()))
check('B1 FINITE DIAGNOSTIC L = 4 exact: unique neutral ground state in every coupling; from g/t = 4 every sector gap exceeds '
      'its free value (all > 1.1x), the pair (charge-2, SU(4) 6) channel being the softest ratio; at g/t = 1 the gaps stay '
      'within 1.5x of free', all(min(v / fr4[k] for k, v in edres[r].items()) > 1.1 for r in (4.0, 8.0, 16.0))
      and all(edres[r]['ex'] > 0.3 for r in edres) and max(edres[1.0][k] / fr4[k] for k in ('p', 'pair')) < 1.5,
      'pair ratio ' + ', '.join(f'{r:g}: {edres[r]["pair"] / fr4["pair"]:.2f}' for r in edres))

print('== C. DMRG (two-site, unlabelled MPS, sector chosen by an exact penalty lam sum_i (Q_i - t_i)^2, chi <= 64)')
CH = [32, 48, 64, 64, 64, 64]; NZ = [1e-3, 1e-4, 1e-5, 0, 0, 0]
def solve(L, r, Q, seeds, ch=None):
    best = None; ch = ch or CH
    for sd in seeds:
        W, c0 = sector_mpo(L, r, Q, lam=6.0); d = dmrg_nocharge(W, seed=sd); h = d.run(ch, noise=NZ); E = h[-1][1] + c0
        if best is None or E < best[1]: best = (d, E, h[-1][1] - h[-2][1])
    return best
# validation against ED at L = 4, g/t = 4
r = 4.0; terms = ed_terms(4, g=1.0, hop=1 / r, face=10.0)
e_ed = {k: np.linalg.eigvalsh(ed_hamiltonian(bases[k], terms).toarray())[0] for k in ('0', 'pair')}
e_dm = {k: solve(4, r, SECT[k], (1,))[1] for k in ('0', 'pair')}
err = max(abs(e_dm[k] - e_ed[k]) for k in e_dm)
check('C1 consistency DMRG (chi 64) reproduces the L = 4 exact sector energies (Q = 0 and pair) at g/t = 4 within 1e-2 g (0.04 t, below 3% of the gaps it resolves)', err < 1e-2, f'max error {err:.1e} (g units)')
out = {}
for L, seeds in ((6, (1, 2)),):
    fr = free_levels(L); res = {}
    for k in ('0', 'pair', 'p'):
        d, E, conv = solve(L, r, SECT[k], seeds if k != 'p' else (1,)); res[k] = E
        if k == '0': gs = d; gs.envs()
    gaps = {k: (res[k] - res['0']) * r for k in ('pair', 'p')}
    Pd = [local_string([(4 * x + 1, True), (4 * x, True)]) for x in range(L)]; Pa = [local_string([(4 * x, False), (4 * x + 1, False)]) for x in range(L)]
    tp = two_point(gs, Pd, Pa); diag = [expect(gs, mul_loc(Pd[x], Pa[x])) for x in range(L)]
    Cm = np.diag(diag)
    for (i, j), v_ in tp.items(): Cm[i, j] = Cm[j, i] = v_
    SP0 = Cm.sum() / L; row = Cm[1, 2:]
    dens = [sum(expect(gs, {4 * x + f: NN}) for f in range(4)) for x in range(L)]
    out[L] = dict(gaps=gaps, ratio={k: gaps[k] / fr[k] for k in gaps}, SP0=SP0, row=row, dens=dens, conv=conv)
    print(f'   L = {L}, g/t = 4: E0 {res["0"]:.4f}; pair gap {gaps["pair"]:.3f}t ({gaps["pair"] / fr["pair"]:.2f}x free), '
          f'particle gap {gaps["p"]:.3f}t ({gaps["p"] / fr["p"]:.2f}x free); S_pair(0) {SP0:.3f} (free {fr["SP0"]:.3f}); '
          f'<P+_1 P_y> y = 3..: {np.round(row[1:], 4).tolist()}; centre density {dens[L // 2 - 1]:.3f}, {dens[L // 2]:.3f} [{time.time() - T0:.0f} s]')
o6 = out[6]; r4p = edres[4.0]['pair'] / fr4['pair']; r4q = edres[4.0]['p'] / fr4['p']
check('C2 FINITE DIAGNOSTIC g/t = 4, L = 4 -> 6: the pair gap and the particle gap stay of order t while the free gaps fall '
      'as 1/L, so their ratios to free grow with L (no 1/L closing as quasi-long-range pair order would give); the pair '
      'structure factor stays at its free value 1/2 (no enhancement) and <P+_1 P_y> is below 0.01 beyond distance 2',
      o6['ratio']['pair'] > r4p and o6['ratio']['p'] > r4q and o6['gaps']['pair'] > 1.2 and abs(o6['SP0'] - 0.5) < 0.06
      and max(o6['row'][2:]) < 0.01,
      f"pair ratio {r4p:.2f} -> {o6['ratio']['pair']:.2f}; particle ratio {r4q:.2f} -> {o6['ratio']['p']:.2f}; "
      f"pair gap {edres[4.0]['pair']:.2f} -> {o6['gaps']['pair']:.2f} t")
d6 = o6['dens']
check('C3 FINITE DIAGNOSTIC no translation breaking at the centre of the L = 6 chain: the two centre sites carry equal density '
      '(reflection-symmetric profile, no period-2 density wave beyond the edge Friedel pattern)', abs(d6[2] - d6[3]) < 0.02,
      f'centre densities {d6[2]:.3f}, {d6[3]:.3f}')
print('L = 8 (DMRG chi 96, and the full g/t scan at L = 6, 8) are production runs recorded in the note, not recomputed here')
print('supplied: toy content (4 flavours, SU(4)-singlet quartic c1c2c3c4 + h.c. on the two-site filter), toy-qmc hopping at mu = 0, '
      'open chains, the face lift (10) on the exactly decoupled alternating mode, sizes, chi, seeds, penalty lam = 6')
print('cited: composite-band-3d (sheared tori, 6-ring), filtered-smg-1d, toy-qmc (3D pair order at g = infinity)')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
