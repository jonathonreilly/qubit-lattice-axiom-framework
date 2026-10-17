"""QMC-1 algebra: the X2 lambda1 = 0 vertex in the Kramers d-frame.

Per site, complex fermions psi_m, m = s * nfl + alpha, s in {0, 1} the walker spinor, alpha a flavour index.
Flavours are ordered so that alpha < n_s are the "s" block and alpha >= n_s the "c" block.
  Spin(10):  nfl = 16, n_s = 8; the 16 is built from the real Cl(9) gammas of SIGN-1 (common.py:16-46),
             rotated to the Gamma^9 eigenbasis: s = 8_s (Gamma^9 = +1), c = 8_c (Gamma^9 = -1).
  reduced:   nfl = 2, n_s = 1 (one s-flavour, one c-flavour): engine check only (gate iii).

d-frame (SIGN-1): d_m = psi_m on the s block, d_m = psi_m^dag on the c block. U(1)_c-neutral operators
(the pairings psi_s psi_c, the walker) are d-number conserving in this frame.

Operators are represented in the d-frame as (A, P, Qm, c0):  O = d^dag A d + d^T P d + d^dag Qm d^dag^T + c0,
with P, Qm antisymmetric.  Wick contractions for such operators are in afqmc.py.

Interaction (lambda1 = 0, normalisation of PREREG section 1):
  Q_x = -(1/4) sum_a (Bh^a Bh^a + h.c.),  Bh^a = (1/2) psi_S^T (i sigma_y x N^a) psi_S,
and the exact Fierz identity  sum_a Bh^a Bh^a = sum_f kappa_f sum_{e in f} P_e P_e  (P_e U(1)_c-neutral pairings) gives
  Q_x = -(1/2) sum_f kappa_f sum_e [ (Re P_e)^2 - (Im P_e)^2 ]     (no remainder: (Re P)^2 - (Im P)^2 = (P^2 + P^dag^2)/2).
"""
import itertools
import numpy as np

I2 = np.eye(2)
SX = np.array([[0., 1.], [1., 0.]], complex)
SY = np.array([[0., -1j], [1j, 0.]], complex)
SZ = np.array([[1., 0.], [0., -1.]], complex)
ISY = 1j * SY                     # i sigma_y = [[0, 1], [-1, 0]] (real)
PAULI = [SX, SY, SZ]


# ----------------------------------------------------------------------------------------------- Clifford algebra
def cl9_gammas():
    """9 mutually anticommuting real symmetric 16x16 matrices squaring to 1 (copied from SIGN-1 common.py:16-43)."""
    E = np.array([[0., 1], [-1, 0]]); X = np.array([[0., 1], [1, 0]]); Z = np.diag([1., -1])
    lab = {"I": np.eye(2), "X": X, "Z": Z, "E": E}

    def kron(*ms):
        out = np.array([[1.0]])
        for m in ms:
            out = np.kron(out, m)
        return out
    cands = [kron(*[lab[c] for c in s]) for s in itertools.product("IXZE", repeat=4)
             if s.count("E") % 2 == 0 and s != ("I",) * 4]
    n = len(cands)
    anti = np.array([[np.allclose(cands[i] @ cands[j], -cands[j] @ cands[i]) for j in range(n)] for i in range(n)])
    best = []

    def bt(cl, start):
        nonlocal best
        if len(cl) > len(best):
            best = list(cl)
        if len(best) == 9:
            return True
        for j in range(start, n):
            if all(anti[j, c] for c in cl):
                cl.append(j)
                if bt(cl, j + 1):
                    return True
                cl.pop()
        return False
    bt([], 0)
    G = [cands[i] for i in best]
    assert len(G) == 9
    for a in range(9):
        assert np.allclose(G[a], G[a].T) and np.allclose(G[a] @ G[a], np.eye(16))
        for b in range(a):
            assert np.allclose(G[a] @ G[b] + G[b] @ G[a], 0)
    return G


# ----------------------------------------------------------------------------------------------- flavour models
class FlavourModel:
    """Per-site algebra. Attributes:
    nfl, n_s, D = 2 nfl (d-modes per site), Nvec (vector N^a in the ordered flavour basis),
    fams: dict name -> list of pairing matrices M_e (D x D antisymmetric, psi-frame, P_e = psi^T M_e psi)."""

    def __init__(self, kind):
        self.kind = kind
        if kind == "spin10":
            G = cl9_gammas()
            w, V = np.linalg.eigh(G[8])                     # Gamma^9
            Ws, Wc = V[:, w > 0], V[:, w < 0]
            O = np.hstack([Ws, Wc])                          # real orthogonal: new flavour basis
            self.nfl, self.n_s = 16, 8
            self.Nvec = [O.T @ g @ O for g in G] + [1j * np.eye(16)]
            self.Nvec = [np.where(np.abs(n) < 1e-13, 0, n).astype(complex) for n in self.Nvec]
            Gr = [O.T @ g @ O for g in G[:8]]                # Gamma^1..8 rotated: off-diagonal s-c blocks
            Y8 = [g[:8, 8:] for g in Gr]
            Y56 = [(Gr[a] @ Gr[b] @ Gr[c])[:8, 8:] for a, b, c in itertools.combinations(range(8), 3)]
            Ydict = {"8v": Y8, "56v": Y56}
        elif kind == "reduced":
            self.nfl, self.n_s = 2, 1
            self.Nvec = [SX.copy(), SZ.copy(), 1j * np.eye(2)]   # analogue of (Gamma^{a<=8}, Gamma^9, i 1)
            Ydict = {"1v": [np.ones((1, 1))]}
        else:
            raise ValueError(kind)
        self.D = 2 * self.nfl
        self.fams = {}
        for yt, Yl in Ydict.items():
            for st, taus in (("sing", [ISY]), ("trip", [ISY @ s for s in PAULI])):
                mats = []
                for tau in taus:
                    for Y in Yl:
                        Y16 = np.zeros((self.nfl, self.nfl), complex)
                        Y16[:self.n_s, self.n_s:] = Y
                        T = np.kron(tau, Y16)
                        mats.append(0.5 * (T - T.T))
                self.fams[f"{st}:{yt}"] = mats
        # vector bilinears Bh^a = psi^T Tvec_a psi, Tvec_a = (1/2) i sigma_y x N^a  (antisymmetric)
        self.Tvec = [0.5 * np.kron(ISY, Na) for Na in self.Nvec]
        for T in self.Tvec:
            assert np.allclose(T, -T.T)
        self.Smask = np.array([(m % self.nfl) < self.n_s for m in range(self.D)])

    # ---------------------------------------------------------------- psi-frame pairing -> d-frame (A, P, Qm)
    def pairing_to_d(self, M):
        """psi^T M psi (M antisymmetric, D x D) -> (A, P, Qm) in the d-frame."""
        S, C = self.Smask, ~self.Smask
        A = np.zeros_like(M, dtype=complex); P = np.zeros_like(A); Qm = np.zeros_like(A)
        P[np.ix_(S, S)] = M[np.ix_(S, S)]
        Qm[np.ix_(C, C)] = M[np.ix_(C, C)]
        A[np.ix_(C, S)] = 2 * M[np.ix_(C, S)]
        return A, P, Qm

    @staticmethod
    def dagger(op):
        """(A, P, Qm) -> representation of the Hermitian conjugate."""
        A, P, Qm = op
        return (A.conj().T, -Qm.conj(), -P.conj())

    def vector_ops(self):
        """Re and Im of Bh^a as d-frame (A, P, Qm) local operators, a = 0..len(Nvec)-1."""
        out = []
        for T in self.Tvec:
            op = self.pairing_to_d(T)
            dg = self.dagger(op)
            re = tuple(0.5 * (x + y) for x, y in zip(op, dg))
            im = tuple((x - y) / 2j for x, y in zip(op, dg))
            out.append((re, im))
        return out

    # ---------------------------------------------------------------- Kramers T2 in the d-frame
    def T2(self):
        """unitary part Theta of T2 on one site's d-modes: T2 v = Theta v^*  (Theta = i sigma_y x 1_nfl)."""
        return np.kron(ISY, np.eye(self.nfl))

    def t2_parity(self, Hm):
        Th = self.T2()
        t = Th @ Hm.conj() @ np.linalg.inv(Th)
        if np.allclose(t, Hm, atol=1e-12):
            return +1
        if np.allclose(t, -Hm, atol=1e-12):
            return -1
        return 0

    # ---------------------------------------------------------------- Fierz identity
    def quads(self):
        return np.array(list(itertools.combinations(range(self.D), 4)))

    @staticmethod
    def four_form(M, q):
        """coefficient (up to the common factor 8) of psi_i psi_j psi_k psi_l (i<j<k<l) in (psi^T M psi)^2."""
        i, j, k, l = q.T
        return M[i, j] * M[k, l] - M[i, k] * M[j, l] + M[i, l] * M[j, k]

    def fierz(self, verbose=print):
        """Solve sum_a Bh^a Bh^a = sum_f kappa_f sum_e P_e P_e exhaustively on all C(D,4) components; choose the
        sign-correct solution minimising the HS noise sum_f |kappa_f| w_f (LP). Returns dict and diagnostics."""
        from scipy.optimize import linprog
        q = self.quads()
        tgt = sum(self.four_form(T, q) for T in self.Tvec)
        names = list(self.fams)
        cols = np.array([sum(self.four_form(M, q) for M in self.fams[n]) for n in names]).T
        Ar = np.vstack([cols.real, cols.imag]); br = np.concatenate([tgt.real, tgt.imag])
        k0, *_ = np.linalg.lstsq(Ar, br, rcond=None)
        res0 = np.abs(Ar @ k0 - br).max() / np.abs(br).max()
        u, sv, vt = np.linalg.svd(Ar, full_matrices=False)
        ker = vt[sv < 1e-10 * sv[0]]
        # required sign of kappa_f: Re P_e T2-even -> c_Re = -kappa/2 <= 0 -> kappa >= 0 ; Re P_e T2-odd -> kappa <= 0
        sgn, w = {}, {}
        for n in names:
            pars = set()
            wn = 0.0
            for M in self.fams[n]:
                re, im = self.channel_pair(M)
                pr, pi = self.t2_parity(re), self.t2_parity(im)
                assert pr != 0 and pi == -pr, (n, pr, pi)
                pars.add(pr)
                wn += np.sum(np.abs(re) ** 2) + np.sum(np.abs(im) ** 2)
            assert len(pars) == 1
            sgn[n] = +1 if pars.pop() == +1 else -1
            w[n] = wn
        s = np.array([sgn[n] for n in names], float); wv = np.array([w[n] for n in names])
        if len(ker) == 0:
            kap = k0
        else:
            K = ker.T
            # minimise sum_f w_f s_f (k0 + K x)_f  s.t.  s_f (k0 + K x)_f >= 0
            c = (wv * s) @ K
            res = linprog(c, A_ub=-(s[:, None] * K), b_ub=s * k0, bounds=[(None, None)] * K.shape[1], method="highs")
            assert res.status == 0, res.message
            kap = k0 + K @ res.x
            kap[np.abs(kap) < 1e-12 * np.abs(kap).max()] = 0.0
        resid = np.abs(Ar @ kap - br).max() / np.abs(br).max()
        margin = np.min(s * kap)
        verbose(f"[fierz:{self.kind}] families {names}; components {len(q)}; lstsq residual {res0:.1e}; "
                f"kernel dim {len(ker)}; singular values {np.round(sv, 6).tolist()}")
        verbose(f"[fierz:{self.kind}] required kappa signs {dict(zip(names, s.astype(int).tolist()))}; HS weights "
                f"{dict(zip(names, np.round(wv, 3).tolist()))}")
        verbose(f"[fierz:{self.kind}] chosen kappa {dict(zip(names, np.round(kap, 12).tolist()))}; exhaustive relative "
                f"residual {resid:.2e}; sign margin (>= 0 required) {margin:.3e}")
        return dict(zip(names, kap)), dict(resid=resid, margin=margin, kernel=ker, k0=k0, names=names, sgn=sgn, w=w)

    def channel_pair(self, M):
        """Hermitian d-frame matrices of Re P and Im P for P = psi^T M psi (neutral pairing: pure A part)."""
        A, P, Qm = self.pairing_to_d(M)
        assert np.abs(P).max() < 1e-14 and np.abs(Qm).max() < 1e-14
        re = 0.5 * (A + A.conj().T)
        im = (A - A.conj().T) / 2j
        return re, im

    def hs_channels(self, kappa):
        """list of (c_e, O_e): Q_x = sum_e c_e O_e^2 with O_e Hermitian D x D (d-frame, traceless)."""
        out = []
        for n, k in kappa.items():
            if k == 0:
                continue
            for M in self.fams[n]:
                re, im = self.channel_pair(M)
                out.append((-0.5 * k, re))
                out.append((+0.5 * k, im))
        return out


def check_channels(fm, chans):
    """Every HS channel: Hermitian, traceless, and T2 parity matching its sign (real field iff c <= 0 and even)."""
    bad = 0
    for c, O in chans:
        assert np.allclose(O, O.conj().T)
        p = fm.t2_parity(O)
        if not ((c < 0 and p == +1) or (c > 0 and p == -1)):
            bad += 1
        assert abs(np.trace(O)) < 1e-12
    return bad


if __name__ == "__main__":
    for kind in ("spin10", "reduced"):
        fm = FlavourModel(kind)
        kap, info = fm.fierz()
        ch = fm.hs_channels(kap)
        print(f"[{kind}] D = {fm.D}; HS channels per vertex {len(ch)}; sign-rule violations {check_channels(fm, ch)}")
