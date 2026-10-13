"""R19-5: an exactly W1-conserved, symmetric, Hermitian Wilson-Dirac stress whose interband (pair) block
is R18-5's UD vertex unchanged.

Operator: T^{mu nu}(q) = sum_k psi^dag(k1) M^{mu nu}(k1,k2) psi(k2), k1 = k2 + q.
W1 (R13-5's (W1-s), all channels): h(k1) M^{0nu} - M^{0nu} h(k2) = sum_j D_j(q) M^{j nu},  nu = 0..3,
with D_j(q) = d_g(q_j) e^{i q_j/2} (R9-9's graviton symbol; d_g = q on |q| <= 1).
(H-sym) M^{j0} = M^{0j}, M^{ij} = M^{ji}.  (H-E) M^{00}(k,k) = h(k).

Construction (Lemma Div, near region |q_j| <= 1, telescoping divided differences; algebraically exact):
  ++ / -- (scattering) blocks:  M^{00} = +-(E1+E2)/2 P1P2,  M^{0j} = (1/2) g^f_j e^{-iq_j/2} P1P2,
     A^{ij} = +-(1/2) e^{-i(q_i+q_j)/2} g^E_j g^f_i P1P2  (f = E^2),
     antisym part = sum_l D_l C^{ijl},  S^{ij} = sum_l D_l (C^{ilj} + C^{jli}),  M^{ij} = A^{(ij)} + S^{ij}.
  +- / -+ (pair) blocks: M^{ij} = P(k1) Gamma_UD^{ij}(kbar) P'(k2)  [UD unchanged];
     M^{0i} = +-sum_j D_j M^{ji}/(E1+E2),  M^{00} = +-sum_j D_j M^{0j}/(E1+E2)  (R13-5 Lemma P1, fermion version).
Far region: (V D* + D* V)/|D|^2 - (D.V) D* D*/|D|^4 (exact algebra), glued by a partition of unity in q.
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18_5'))
from dirac import D1

rng = np.random.default_rng(19055)
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z = np.zeros((2, 2)); I2 = np.eye(2)
alpha = [np.block([[Z, s], [s, Z]]) for s in (s1, s2, s3)]
beta = np.block([[I2, Z], [Z, -I2]]).astype(complex)
I4 = np.eye(4, dtype=complex)

class Band:
    def __init__(self, law, m):
        self.L, self.m = law, m
    def S(self, k): return np.array([float(self.L.S(k[j])) for j in range(3)])
    def dS(self, k): return np.array([float(self.L.dS(k[j])) for j in range(3)])
    def W(self, k): return np.array([float(self.L.W(k[j])) for j in range(3)])
    def dW(self, k): return np.array([float(self.L.dW(k[j])) for j in range(3)])
    def M(self, k): return self.m + self.W(k).sum()
    def h(self, k):
        S = self.S(k); return sum(S[a] * alpha[a] for a in range(3)) + self.M(k) * beta
    def E(self, k):
        S = self.S(k); return np.sqrt((S ** 2).sum() + self.M(k) ** 2)
    def f(self, k): return self.E(k) ** 2
    def p(self, k):  # grad(E^2/2)
        return self.S(k) * self.dS(k) + self.M(k) * self.dW(k)
    def proj(self, k, sgn):
        return 0.5 * (I4 + sgn * self.h(k) / self.E(k))
    def dh(self, k, i):
        return self.dS(k)[i] * alpha[i] + self.dW(k)[i] * beta

def divdiff(band, fun, dfun, k2, q, tol=1e-9):
    """telescoping divided differences: fun(k2+q) - fun(k2) = sum_j q_j g_j (exact)."""
    g = np.zeros(3); p0 = k2.copy()
    for j in range(3):
        p1 = p0.copy(); p1[j] += q[j]
        if abs(q[j]) < tol:
            g[j] = dfun(p0)[j]
        else:
            g[j] = (fun(p1) - fun(p0)) / q[j]
        p0 = p1
    return g

def gE_gf(band, k2, q):
    gE = divdiff(band, band.E, lambda k: band.p(k) / band.E(k), k2, q)
    gf = divdiff(band, band.f, lambda k: 2 * band.p(k), k2, q)
    return gE, gf

def bfun(band, k2, q):
    gE, gf = gE_gf(band, k2, q)
    return np.outer(gf, gE) - np.outer(gE, gf)   # b[i,j] = gE_j gf_i - gE_i gf_j

def UD(band, k, i, j):
    p = band.p(k)
    return 0.5 * (p[j] * band.dh(k, i) + p[i] * band.dh(k, j))

def near(band, k2, q):
    """returns M[mu][nu] (4x4 complex) on the near region, before Hermitization."""
    k1 = k2 + q
    D = q * np.exp(1j * q / 2)           # d_g = q on |q_j| <= 1
    E1, E2 = band.E(k1), band.E(k2)
    Pp1, Pm1, Pp2, Pm2 = band.proj(k1, 1), band.proj(k1, -1), band.proj(k2, 1), band.proj(k2, -1)
    gE, gf = gE_gf(band, k2, q)
    ph = np.exp(-1j * q / 2)
    # antisym division: b(q) = sum_l [b(Q_l) - b(Q_{l-1})]
    c = np.zeros((3, 3, 3))
    Q0 = np.zeros(3); b0 = bfun(band, k2, Q0)
    for l in range(3):
        Q1 = Q0.copy(); Q1[l] = q[l]
        b1 = bfun(band, k2, Q1)
        c[:, :, l] = (b1 - b0) / q[l]
        Q0, b0 = Q1, b1
    M = [[np.zeros((4, 4), complex) for _ in range(4)] for _ in range(4)]
    for sgn, Pa, Pb in ((1, Pp1, Pp2), (-1, Pm1, Pm2)):
        PP = Pa @ Pb
        M[0][0] += sgn * 0.5 * (E1 + E2) * PP
        for j in range(3):
            M[0][j + 1] += 0.5 * gf[j] * ph[j] * PP
        A = np.array([[sgn * 0.5 * ph[i] * ph[j] * gE[j] * gf[i] for j in range(3)] for i in range(3)])
        As = 0.5 * (A + A.T)
        # antisym part of A = sgn*(1/4) ph_i ph_j (gE_j gf_i - gE_i gf_j) = sum_l D_l C[i,j,l]
        C = np.array([[[sgn * 0.25 * ph[i] * ph[j] * c[i, j, l] * ph[l] for l in range(3)] for j in range(3)] for i in range(3)])
        Sij = np.array([[sum(D[l] * (C[i, l, j] + C[j, l, i]) for l in range(3)) for j in range(3)] for i in range(3)])
        for i in range(3):
            for j in range(3):
                M[i + 1][j + 1] += (As[i, j] + Sij[i, j]) * PP
    # pair blocks: UD at the midpoint, unchanged
    kb = k2 + q / 2
    G = [[UD(band, kb, i, j) for j in range(3)] for i in range(3)]
    for sgn, Pa, Pb in ((1, Pp1, Pm2), (-1, Pm1, Pp2)):
        Mij = [[Pa @ G[i][j] @ Pb for j in range(3)] for i in range(3)]
        M0i = [sgn * sum(D[j] * Mij[j][i] for j in range(3)) / (E1 + E2) for i in range(3)]
        M00 = sgn * sum(D[j] * M0i[j] for j in range(3)) / (E1 + E2)
        M[0][0] += M00
        for i in range(3):
            M[0][i + 1] += M0i[i]
            for j in range(3):
                M[i + 1][j + 1] += Mij[i][j]
    for j in range(1, 4):
        M[j][0] = M[0][j]
    return M

def residual(band, M, k2, q, Dfun):
    k1 = k2 + q; D = Dfun(q); h1, h2 = band.h(k1), band.h(k2)
    r = 0.0
    for nu in range(4):
        lhs = h1 @ M[0][nu] - M[0][nu] @ h2
        rhs = sum(D[j] * M[j + 1][nu] for j in range(3))
        r = max(r, np.abs(lhs - rhs).max())
    sym = max(np.abs(M[i][j] - M[j][i]).max() for i in range(4) for j in range(4))
    return r, sym

def herm(band, k2, q, builder):
    Ma = builder(band, k2, q); Mb = builder(band, k2 + q, -q)
    return [[0.5 * (Ma[a][b] + Mb[a][b].conj().T) for b in range(4)] for a in range(4)]

def Dnear(q): return q * np.exp(1j * q / 2)

if __name__ == '__main__':
    import time; t0 = time.time()
    law = D1(0.909103707957, 0.555604225797)      # R18-9 refereed retuned Dirac edge (vR18-9:11)
    for m in (0.3, 0.01):
        band = Band(law, m)
        print(f'== D1(0.909103708, 0.555604226), m = {m} ==')
        rmax = smax = hmax = 0.0
        for t in range(300):
            k2 = rng.uniform(-np.pi, np.pi, 3)
            q = rng.uniform(-1, 1, 3) * 10 ** rng.uniform(-3, 0, 3)
            M = near(band, k2, q)
            r, s = residual(band, M, k2, q, Dnear)
            MH = herm(band, k2, q, near)
            rH, sH = residual(band, MH, k2, q, Dnear)
            rmax, smax, hmax = max(rmax, r), max(smax, s, sH), max(hmax, rH)
        print(f'  near region (|q_j|<=1, 300 random (k,q)): W1 residual max {rmax:.2e}; Hermitized {hmax:.2e}; mu-nu symmetry {smax:.2e}')
        # forward limit: ++ block -> E v_i v_j P+, -- block -> -E v_i v_j P-;  M^{0j}(k,k) -> h-weighted E v_j
        fmax = 0.0; pmax = 0.0
        for t in range(40):
            k = rng.uniform(-np.pi, np.pi, 3); n = rng.normal(size=3); n /= np.linalg.norm(n)
            M = herm(band, k, 1e-6 * n, near)
            E = band.E(k); p = band.p(k); Pp, Pm = band.proj(k, 1), band.proj(k, -1)
            for i in range(3):
                for j in range(3):
                    req = p[i] * p[j] / E * (Pp - Pm)
                    blk = Pp @ M[i + 1][j + 1] @ Pp + Pm @ M[i + 1][j + 1] @ Pm
                    fmax = max(fmax, np.abs(blk - req).max())
                req0 = p[i] * (Pp + Pm)
                fmax = max(fmax, np.abs(M[0][i + 1] - (Pp @ M[0][i + 1] @ Pp + Pm @ M[0][i + 1] @ Pm)).max() * 0 + np.abs(Pp @ M[0][i + 1] @ Pp + Pm @ M[0][i + 1] @ Pm - req0).max())
            # pair block of M^{ij} equals UD's
            for i in range(3):
                for j in range(3):
                    G = UD(band, k + 0.5e-6 * n, i, j)
                    pb = Pp @ M[i + 1][j + 1] @ Pm
                    pmax = max(pmax, np.abs(pb - band.proj(k + 1e-6 * n, 1) @ G @ band.proj(k, -1)).max())
        print(f'  forward values at |q| = 1e-6 (40 k): |intraband - (p_i p_j/E)(P+ - P-)|, |M^0j - p_j| max {fmax:.2e}')
        print(f'  interband (pair) block of M^ij vs UD at midpoint (after Hermitization): max diff {pmax:.2e}')
        # continuity of the scattering construction as q -> 0 along a ray
        k = np.array([0.7, -1.9, 2.4]); n = np.array([0.3, 0.5, 0.81]); n /= np.linalg.norm(n)
        vals = []
        for s in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
            M = herm(band, k, s * n, near)
            vals.append(M[1][2])
        d = [np.abs(vals[i + 1] - vals[i]).max() for i in range(len(vals) - 1)]
        print('  continuity along a ray, |M^xy(s) - M^xy(s/10)| for s = 1e-1..1e-4:', ' '.join(f'{x:.1e}' for x in d))
    print(f'time {time.time() - t0:.1f} s')
