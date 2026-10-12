"""Lane RS / S1: matrix-valued (taste/band-resolved) Born collision invariants for
interacting staggered fermions in d = 1, 2, 3.

Model (one complex fermion component per site, spinless):
  h = sum_{x,j} (i/2) eta_j(x) (c+_x c_{x+j} - h.c.) + m sum_x eps(x) n_x
  eta_j(x) = (-1)^{x_1+...+x_{j-1}},  eps(x) = (-1)^{sum x}
Interactions (density-density, H_int = (1/2) sum_{x,y} K(x-y) :n_x n_y:):
  'nn'  : V sum_{x,j} n_x n_{x+j}             -> v(q) = 2 sum_j cos q_j
  'cube': U sum_{all hypercubes y} (Q_y)^2,  Q_y = sum_{x in y+{0,1}^d} n_x
          (taste-singlet point-split density squared; invariant under all shift
           symmetries)                         -> v(q) = prod_j (2 + 2 cos q_j)
Full-zone momentum p: h maps c_p -> c_{p + pi zeta_j}; reduced zone k, components
A in {0,1}^d, p = k + pi A.  h(k)^2 = (sum sin^2 k_j + m^2) 1.

One-body charge basis: O_{B,r} = sum_x e^{i pi B.x} c+_x c_{x+r}, |r|_inf <= R,
B in {0,1}^d  (every one-body operator invariant under translation by 2).
Symbol: O(k)[A xor B, A] = exp(i (k + pi A).r).
Inversion (symmetry of h and of both interactions): c_x -> eps(x) c_{-x}, maps
O_{B,r} -> eps(r) O_{B,-r}.  Odd sector = momentum-like.

Necessary condition (O(V), Born; exact asymptotic 2-particle statement at O(V) for a
conserved P = P0 + V P1 + ..., P0 one-body part commuting with h):
  for every on-shell 2-particle process (k1 s1, k2 s2) -> (k3 s3, k4 s4),
  k1+k2 = k3+k4 (mod pi), s1 w1 + s2 w2 = s3 w3 + s4 w4:
    (F3 x 1 + 1 x F4) W - W (F1 x 1 + 1 x F2) = 0
  with F_i = U_i^+ F(k_i) U_i the block of F on the degenerate eigenspace (dim 2^{d-1})
  and W the antisymmetrized vertex between degenerate spaces (true form factors).
Only the diagonal blocks of F enter; we quotient by the off-diagonal kernel, which
covers every F that commutes with h and every C(F) = (F + hFh/E^2)/2 (exp-local, m>0).
"""
import numpy as np, itertools, sys, time
from scipy.optimize import brentq
from scipy.linalg import qr

def setup(d):
    As = np.array(list(itertools.product([0, 1], repeat=d)))[:, ::-1]  # A[idx]; idx = sum A_j 2^j
    As = np.array([[ (a >> j) & 1 for j in range(d)] for a in range(2**d)])
    zeta = [np.array([1]*j + [0]*(d-j)) for j in range(d)]   # zeta_j (0-based j): ones in slots < j
    idx = lambda A: int(sum(int(A[j]) << j for j in range(d)))
    return As, zeta, idx

class Stag:
    def __init__(self, d, m, inter):
        self.d, self.m, self.inter = d, m, inter
        self.As, self.zeta, self.idx = setup(d)
        self.n = 2**d; self.D = 2**(d-1)
        self.xor = np.array([[self.idx((self.As[a] + self.As[b]) % 2) for b in range(self.n)] for a in range(self.n)])
    def h(self, k):
        d, n = self.d, self.n
        H = np.zeros((n, n))
        for a in range(n):
            A = self.As[a]
            for j in range(d):
                ap = self.idx((A + self.zeta[j]) % 2)
                H[ap, a] += -np.sin(k[j] + np.pi*A[j])
            H[self.idx((A + 1) % 2), a] += self.m
        return H
    def omega(self, k):
        k = np.atleast_2d(k)
        return np.sqrt(np.sum(np.sin(k)**2, axis=-1) + self.m**2)
    def U(self, k):
        w, v = np.linalg.eigh(self.h(k))
        return v[:, :self.D], v[:, self.D:], w   # minus band, plus band
    def v(self, q):
        if self.inter == 'nn':   return 2*np.sum(np.cos(q), axis=-1)
        if self.inter == 'cube': return np.prod(2 + 2*np.cos(q), axis=-1)
        if self.inter == 'zero': return 0*np.sum(q, axis=-1)
        raise ValueError
    def W(self, ks, Us):
        """antisymmetrized vertex W[a3,a4,a1,a2] between degenerate band spaces; k4 = k1+k2-k3 exactly."""
        k1, k2, k3, k4 = ks; U1, U2, U3, U4 = Us
        n, As = self.n, self.As
        out = 0
        for (ka, Ua, kb, Ub, sgn) in ((k1, U1, k2, U2, 1.0), (k2, U2, k1, U1, -1.0)):
            # direct with leg 'a' as the one whose momentum transfers to leg 3
            Vm = np.array([[self.v(k3 - ka + np.pi*(As[A3] - As[Aa])) for Aa in range(n)] for A3 in range(n)])
            T = np.zeros((self.D,)*4, dtype=complex)
            for A3 in range(n):
                for Aa in range(n):
                    for Ab in range(n):
                        A4 = self.xor[self.xor[A3, Aa], Ab]
                        c = Vm[A3, Aa]
                        if c == 0: continue
                        # U*_3[A3,a3] U*_4[A4,a4] Ua[Aa,.] Ub[Ab,.]
                        t = c*np.einsum('i,j,k,l->ijkl', U3[A3].conj(), U4[A4].conj(), Ua[Aa], Ub[Ab])
                        if sgn > 0: T += t
                        else: T += t.transpose(0, 1, 3, 2)  # in-state order (1,2): leg a=2 -> index of particle 2
            out = out + sgn*T
        return out

def basis(d, R):
    rs = [np.array(r) for r in itertools.product(range(-R, R+1), repeat=d)]
    Bs = [np.array([(b >> j) & 1 for j in range(d)]) for b in range(2**d)]
    full = [(B, r) for B in Bs for r in rs]
    pos = {(tuple(B), tuple(r)): i for i, (B, r) in enumerate(full)}
    # parity combos: O_{B,r} -> eps(r) O_{B,-r}
    odd, even = [], []
    seen = set()
    for i, (B, r) in enumerate(full):
        j = pos[(tuple(B), tuple(-r))]
        if (min(i, j), max(i, j)) in seen: continue
        seen.add((min(i, j), max(i, j)))
        e = (-1)**int(np.sum(r))
        if i == j:
            (even if e == 1 else odd).append({i: 1.0})
        else:
            odd.append({i: 1.0, j: -e}); even.append({i: 1.0, j: e})
    return full, odd, even

def blocks(model, full, k, U):
    """Fb[n, a, b] = U^+ O_n(k) U for the full basis."""
    n = model.n
    rs = np.array([r for (B, r) in full], dtype=float)
    ph = np.exp(1j*(rs @ k))[:, None] * np.exp(1j*np.pi*(rs @ model.As.T))   # (nb, n)
    Bi = np.array([model.idx(B) for (B, r) in full])
    out = np.zeros((len(full), U.shape[1], U.shape[1]), dtype=complex)
    for b in range(n):
        sel = np.where(Bi == b)[0]
        Up = U[model.xor[:, b]]   # Up[A] = U[A xor B]
        out[sel] = np.einsum('Aa,nA,Ab->nab', Up.conj(), ph[sel], U)
    return out

_SM = {}
def to_sector(Fb, sector):
    import scipy.sparse as sp
    key = id(sector)
    if key not in _SM:
        rows, cols, vals = [], [], []
        for j, comb in enumerate(sector):
            for i, c in comb.items(): rows.append(i); cols.append(j); vals.append(c)
        _SM[key] = (sector, sp.csr_matrix((vals, (rows, cols)), shape=(Fb.shape[0], len(sector))).T.tocsr())
    S = _SM[key][1]
    return (S @ Fb.reshape(Fb.shape[0], -1)).reshape((S.shape[0],) + Fb.shape[1:])

def sample_processes(model, N, chans, rng, special=None, tmin=0.05, ball=None):
    d = model.d
    om = lambda k: model.omega(k)[0] if np.ndim(k) == 1 else model.omega(k)
    out = []; tries = 0
    tgrid = np.linspace(tmin, np.pi*np.sqrt(d), 300)
    while len(out) < N and tries < 400*N:
        tries += 1
        s = chans[rng.integers(len(chans))]
        k1 = rng.uniform(-np.pi/2, np.pi/2, d) if ball is None else rng.uniform(-ball, ball, d)
        if special is None:
            k2 = rng.uniform(-np.pi/2, np.pi/2, d) if ball is None else rng.uniform(-ball, ball, d)
        else:
            k2 = np.array(special) - k1
        K = k1 + k2
        E = s[0]*om(k1) + s[1]*om(k2)
        u = rng.normal(size=d); u /= np.linalg.norm(u)
        k3s = k1[None, :] + tgrid[:, None]*u[None, :]
        g = s[2]*model.omega(k3s) + s[3]*model.omega(K[None, :] - k3s) - E
        if np.all(np.abs(g) < 1e-12):   # flat branch: any point on the line is on shell
            t = tgrid[rng.integers(len(tgrid))]
        else:
            idx = np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]
            if len(idx) == 0: continue
            i = idx[rng.integers(len(idx))]
            G = lambda t: s[2]*om(k1 + t*u) + s[3]*om(K - k1 - t*u) - E
            try: t = brentq(G, tgrid[i], tgrid[i+1], xtol=1e-15)
            except ValueError: continue
        k3 = k1 + t*u; k4 = K - k3
        wr = lambda a: (a + np.pi/2) % np.pi - np.pi/2
        # drop trivial (same leg labels): (k3,s3)=(k1,s1) or (k3,s3)=(k2,s2)
        if s[2] == s[0] and np.linalg.norm(wr(k3 - k1)) < 1e-3: continue
        if s[2] == s[1] and np.linalg.norm(wr(k3 - k2)) < 1e-3: continue
        if min(om(k1), om(k2), om(k3), om(k4)) < 1e-3: continue
        out.append((s, k1, k2, k3, k4))
    return out

def residual_rows(model, proc, full, sector):
    s, k1, k2, k3, k4 = proc
    ks = (k1, k2, k3, k4); Us = []; Fs = []
    for k, si in zip(ks, s):
        Um, Up, w = model.U(k)
        U = Up if si > 0 else Um
        Us.append(U)
        Fs.append(to_sector(blocks(model, full, k, U), sector))
    W = model.W(ks, Us)
    F1, F2, F3, F4 = Fs
    R = (np.einsum('nab,bcde->nacde', F3, W) + np.einsum('ncb,abde->nacde', F4, W)
         - np.einsum('abce,ncd->nabde', W, F1) - np.einsum('abdc,nce->nabde', W, F2))
    return R.reshape(R.shape[0], -1).T, np.linalg.norm(W)

def block_map_Q(model, full, sector, rng, nk):
    rows = []
    for _ in range(nk):
        k = rng.uniform(-np.pi/2, np.pi/2, model.d)
        Um, Up, w = model.U(k)
        for U in (Um, Up):
            Fb = to_sector(blocks(model, full, k, U), sector)
            rows.append(Fb.reshape(Fb.shape[0], -1).T)
    M = np.vstack(rows)
    u, sv, vh = np.linalg.svd(M, full_matrices=False)
    keep = sv > 1e-9*sv[0] + 1e-10
    return vh[keep].conj().T, sv  # columns: orthonormal basis of complement of ker(blockmap)

def nullspace_run(model, R, procs, sector_name, rng, chunk=200, verbose=True):
    full, odd, even = basis(model.d, R)
    sector = odd if sector_name == 'odd' else even
    nk = int(3*len(sector)/(2*model.D**2)) + 20
    Q, svM = block_map_Q(model, full, sector, rng, nk)
    Rtri = None; nrows = 0; Wn = []
    buf = []
    for i, p in enumerate(procs):
        A, wn = residual_rows(model, p, full, sector); Wn.append(wn)
        buf.append(A @ Q); nrows += A.shape[0]
        if len(buf) >= chunk or i == len(procs) - 1:
            stack = np.vstack(buf if Rtri is None else [Rtri] + buf)
            Rtri = qr(stack, mode='r')[0][:Q.shape[1]]
            buf = []
    sv = np.linalg.svd(Rtri, compute_uv=False) / np.sqrt(len(procs))
    return sv, Q.shape[1], len(sector), np.array(Wn)

def report(lbl, sv, ncol, nsec, Wn, expect_null):
    atol, rtol = 1e-8, 1e-9
    nul = int(np.sum(sv < atol + rtol*sv[0]))
    nontriv = sv[:len(sv) - nul] if nul < len(sv) else np.array([np.nan])
    gap = sv[len(sv) - nul - 1] if nul < len(sv) else np.nan
    print(f"  {lbl}: basis {nsec} -> {ncol} block-distinct; nullity {nul} (expected trivial {expect_null}); "
          f"sv_max {sv[0]:.3e}, smallest nonzero sv {gap:.3e} (ratio {gap/sv[0]:.2e}); "
          f"largest 'null' sv {sv[-1] if nul else float('nan'):.1e}; |W| median {np.median(Wn):.2e}, frac |W|<1e-8 {np.mean(Wn<1e-8):.2f}")
    sys.stdout.flush()
    return nul

ALLCH = [s for s in itertools.product([1, -1], repeat=4)]
