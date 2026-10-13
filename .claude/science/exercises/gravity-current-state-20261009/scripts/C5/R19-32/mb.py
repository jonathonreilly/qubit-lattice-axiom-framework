"""R19-32 many-body builder: one sector of the covariant 10-slot model on the 1x1xL slice (momenta || z).
Slots: (field A in sector) x (site x = 0..L-1), each a d-level truncated oscillator, a|n> = sqrt(n)|n-1>,
Krein metric eta_A = +1 (identity) or -1 ((-1)^n), a^K = eta a^dag eta. Slot frequency nu:
 f = (a + a^K)/sqrt(2 nu), pi = -i sqrt(nu/2)(a - a^K)  ([f,pi] = i eta_A below the top level).
Twist s = +1 periodic, -1 antiperiodic (f(x+L) = s f(x)); momenta k = (2 pi j + (pi if s=-1))/L.
H = sum_A eta_A/2 sum_x [pi_Ax^2 + (f_A(x+1) - f_A(x))^2]   (massless Feynman-gauge lattice scalar per eigenfield;
    offsets do not change H). Krein-self-adjoint; equals a positive Hermitian matrix.
Formula lowering parts: b_A(k) = L^-1/2 sum_x e^{-ik(x+o_A)}[u_k a_Ax + v_k a^K_Ax], u,v = (sqrt(w/nu) +- sqrt(nu/w))/2,
 D_n(k) = sum_A chat_nA b_A(k) (chat = c/w from cov.constraint_coeffs at k||z; k-independent on the slice).
Constraint field (for spectral GB): chi_n(x) = sum_A [ -Ebar_A{0n} pi_A(x) + Ebar_A{zn} (f_A(x+1/2) - f_A(x-1/2)) ].
"""
import numpy as np, scipy.sparse as sp, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from cov import *

def slot_ops(d, eta):
    a = np.zeros((d, d))
    for n in range(1, d): a[n-1, n] = np.sqrt(n)
    E = np.eye(d) if eta > 0 else np.diag([(-1.)**n for n in range(d)])
    aK = E@a.T@E
    return a, aK, E

class Sector:
    def __init__(self, sector, L, d, nu=1.0, twist=1, fields=None):
        self.idx = SECTORS[sector] if fields is None else fields
        self.L, self.d, self.nu, self.twist = L, d, nu, twist
        self.etas = ETA[self.idx]; self.offs = OFFZ[self.idx]
        self.nf = len(self.idx); self.ns = self.nf*L
        self.dim = d**self.ns
        js = range(L)
        self.ks = [(2*np.pi*j + (np.pi if twist < 0 else 0.))/L for j in js]
        self.ws = [2*abs(np.sin(k/2)) for k in self.ks]
        c, _ = constraint_coeffs([0, 0, np.pi/2])
        w0 = 2*np.sin(np.pi/4)
        rows = [n for n in range(4) if np.abs(c[n, self.idx]).max() > 1e-12]
        self.rows = rows
        self.chat = c[np.ix_(rows, self.idx)]/w0
        self.Ebar = []
        for A in self.idx:
            h = sum(R[I, A]*B[I] for I in range(10)); self.Ebar.append(h - 0.5*eta4*np.trace(eta4@h))
        self._build()

    def slot(self, A, x):           # slot index for field position A (0..nf-1), site x
        return A*self.L + x

    def emb(self, X, s):
        left = sp.identity(self.d**s, format='csr'); right = sp.identity(self.d**(self.ns - s - 1), format='csr')
        return sp.kron(sp.kron(left, sp.csr_matrix(X)), right, format='csr')

    def _build(self):
        d = self.d
        self.a = {}; self.aK = {}; etadiag = np.ones(1)
        for A in range(self.nf):
            a, aK, E = slot_ops(d, self.etas[A])
            for x in range(self.L):
                s = self.slot(A, x)
                self.a[s] = self.emb(a, s); self.aK[s] = self.emb(aK, s)
        eta = np.ones(1)
        for A in range(self.nf):
            e1 = np.ones(d) if self.etas[A] > 0 else np.array([(-1.)**n for n in range(d)])
            for x in range(self.L): eta = np.kron(eta, e1)
        self.eta = eta                                  # diagonal of the Krein metric
        nu = self.nu
        self.f = {s: (self.a[s] + self.aK[s])/np.sqrt(2*nu) for s in self.a}
        self.p = {s: -1j*np.sqrt(nu/2)*(self.a[s] - self.aK[s]) for s in self.a}
        H = sp.csr_matrix((self.dim, self.dim), dtype=complex)
        for A in range(self.nf):
            for x in range(self.L):
                s = self.slot(A, x); s2 = self.slot(A, (x + 1) % self.L)
                sg = self.twist if x == self.L - 1 else 1
                df = self.f[s2]*sg - self.f[s]
                H = H + 0.5*self.etas[A]*(self.p[s]@self.p[s] + df@df)
        self.H = H.tocsr()

    def b(self, A, j):
        k = self.ks[j]; w = self.ws[j]; nu = self.nu
        u = 0.5*(np.sqrt(w/nu) + np.sqrt(nu/w)); v = 0.5*(np.sqrt(w/nu) - np.sqrt(nu/w))
        out = 0
        for x in range(self.L):
            s = self.slot(A, x)
            out = out + np.exp(-1j*k*(x + self.offs[A]))*(u*self.a[s] + v*self.aK[s])
        return out/np.sqrt(self.L)

    def D(self, r, j):
        return sum(self.chat[r, A]*self.b(A, j) for A in range(self.nf))

    def constraints(self):
        return [self.D(r, j) for j in range(self.L) if self.ws[j] > 1e-12 for r in range(len(self.rows))]

    def Kad(self, X):
        Et = sp.diags(self.eta)
        return (Et@X.conj().T@Et).tocsr()

    def chi(self, r, x):
        """position-space constraint field row r at site x (pi = velocity). Spatial part: d_z of hbar_{z n}: the
        field with offset o sits at x+o; difference between the two neighbours of the constraint point."""
        n = self.rows[r]; out = 0
        for A in range(self.nf):
            Eb = self.Ebar[A]
            if abs(Eb[0, n]) > 1e-14:
                out = out - Eb[0, n]*self.p[self.slot(A, x)]          # -d_0 hbar_{0n}, pi = velocity
            if abs(Eb[3, n]) > 1e-14:
                o = self.offs[A]
                # constraint point of row n: offset 1/2 if n == 3 (z-link) else 0
                cp = 0.5 if n == 3 else 0.0
                # neighbours at cp +- 1/2 must be positions x' + o
                xp = int(round(x + cp + 0.5 - o)); xm = int(round(x + cp - 0.5 - o))
                def fsite(y):
                    sg = 1
                    while y >= self.L: y -= self.L; sg *= self.twist
                    while y < 0: y += self.L; sg *= self.twist
                    return sg*self.f[self.slot(A, y)]
                out = out + Eb[3, n]*(fsite(xp) - fsite(xm))
        return out
