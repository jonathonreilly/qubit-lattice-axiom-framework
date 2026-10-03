"""A22 two-body toolkit (supplied toy): two excitations on the 1D two-layer partial-swap round, reduced to the
relative coordinate at fixed total cell momentum P.

Sites x = 2j + alpha (cell j, sublattice alpha = 0 'a' / 1 'b').  Even layer: bonds (2j, 2j+1) (inside a cell),
odd layer: bonds (2j+1, 2j+2).  One-excitation block of exp(-i theta SWAP) RELATIVE TO THE EMPTINESS:
    e^{i theta} (cos theta - i sin theta sigma_x);   |11> on a bond: relative phase e^{i phi} (phi = 0 for the S1 gate).
A19's round = (theta_e, theta_o) = (pi/2, pi/2 - m).

Two-body state psi(j_A, alpha; j_B, beta) = e^{i P j_B} chi[r, alpha, beta],  r = j_A - j_B (mod M).
Geometry 'ladder': A and B on different chains (distinguishable), interaction = diagonal phases V(x_A - x_B, pair type).
Geometry 'chain' : both on one chain (identical hard-core excitations, chi exchange-symmetric), |11> relative phases
                   phi_e, phi_o on same-bond pairs (hard-core fix after each layer), optional extra diagonal phases.
"""
import numpy as np

PI = np.pi


def bloch(K, te, to):
    """Relative-to-emptiness Bloch matrix U(K) = e^{i(te+to)} O(K) E, shape (..., 2, 2)."""
    K = np.asarray(K, float)
    ce, se, co, so = np.cos(te), np.sin(te), np.cos(to), np.sin(to)
    E = np.array([[ce, -1j * se], [-1j * se, ce]])
    O = np.zeros(K.shape + (2, 2), complex)
    O[..., 0, 0] = co; O[..., 1, 1] = co
    O[..., 0, 1] = -1j * so * np.exp(-1j * K)
    O[..., 1, 0] = -1j * so * np.exp(1j * K)
    return np.exp(1j * (te + to)) * (O @ E)


def bands(K, te, to):
    """Return E[s], v[s], vec[s] for s in (0,1) <-> sign (+1,-1): eigenvalue e^{-iE}, E_s = -(te+to) - s*omega(K)."""
    K = np.asarray(K, float)
    c = np.cos(te) * np.cos(to) - np.sin(te) * np.sin(to) * np.cos(K)
    om = np.arccos(np.clip(c, -1, 1))
    U = bloch(K, te, to)
    out = []
    for s in (+1, -1):
        Es = -(te + to) - s * om
        lam = np.exp(-1j * Es)
        # eigenvector of 2x2: (U - lam) v = 0  ->  v = (U01, lam - U00) or (lam - U11, U10)
        v1 = np.stack([U[..., 0, 1], lam - U[..., 0, 0]], -1)
        v2 = np.stack([lam - U[..., 1, 1], U[..., 1, 0]], -1)
        n1 = np.linalg.norm(v1, axis=-1); n2 = np.linalg.norm(v2, axis=-1)
        v = np.where((n1 >= n2)[..., None], v1 / np.maximum(n1, 1e-300)[..., None], v2 / np.maximum(n2, 1e-300)[..., None])
        # dE_s/dK = -s d(om)/dK,  d(om)/dK = -sin(te) sin(to) sin K / sin(om)
        vel = s * np.sin(te) * np.sin(to) * np.sin(K) / np.maximum(np.sin(om), 1e-300)
        out.append((Es, vel, v))
    return out


class Rel:
    """Relative-coordinate two-body evolution."""

    def __init__(self, M, te, to, P, geom="ladder", phi_e=0.0, phi_o=0.0, V=None):
        self.M, self.te, self.to, self.P, self.geom = M, te, to, P, geom
        self.phi_e, self.phi_o = phi_e, phi_o
        self.r = np.arange(M); self.r[self.r >= M // 2] -= M          # signed relative cell coordinate
        # diagonal interaction phases (applied once per tick, after both layers): array (M, 2, 2) of phases
        self.Vph = None
        if V is not None:
            ph = np.zeros((M, 2, 2))
            for (d_site, kind, val) in V:   # d_site = x_A - x_B ; kind in ('all','even','odd')
                for a in (0, 1):
                    for b in (0, 1):
                        # x_A - x_B = 2r + a - b = d_site  ->  r = (d_site - a + b)/2
                        num = d_site - a + b
                        if num % 2:
                            continue
                        rr = num // 2
                        if abs(d_site) == 1 and kind != "all":
                            # bond type of the pair {x_A, x_B}: even bond = (2j,2j+1) (same cell), odd = (2j+1, 2j+2)
                            lo_alpha = a if d_site < 0 else b       # sublattice of the lower site
                            btype = "even" if lo_alpha == 0 else "odd"
                            if btype != kind:
                                continue
                        ph[rr % M, a, b] += val
            self.Vph = np.exp(1j * ph)

    # ---- one-particle layers acting on index A (axis 1) or B (axis 2) of chi[r, a, b]
    def even(self, chi):
        c, s = np.cos(self.te), np.sin(self.te); f = np.exp(1j * self.te)
        # particle A
        a, b = chi[:, 0, :].copy(), chi[:, 1, :].copy()
        chi[:, 0, :] = f * (c * a - 1j * s * b); chi[:, 1, :] = f * (c * b - 1j * s * a)
        a, b = chi[:, :, 0].copy(), chi[:, :, 1].copy()
        chi[:, :, 0] = f * (c * a - 1j * s * b); chi[:, :, 1] = f * (c * b - 1j * s * a)
        return chi

    def odd(self, chi):
        c, s = np.cos(self.to), np.sin(self.to); f = np.exp(1j * self.to)
        eP = np.exp(1j * self.P)
        # particle A: a'_j = c a_j - i s b_{j-1} ; b'_j = c b_j - i s a_{j+1}   (r = j_A - j_B)
        a, b = chi[:, 0, :].copy(), chi[:, 1, :].copy()
        chi[:, 0, :] = f * (c * a - 1j * s * np.roll(b, 1, axis=0))
        chi[:, 1, :] = f * (c * b - 1j * s * np.roll(a, -1, axis=0))
        # particle B: chi'_{.b}(r) = c chi_{.b}(r) - i s e^{iP} chi_{.a}(r-1); chi'_{.a}(r) = c chi_{.a}(r) - i s e^{-iP} chi_{.b}(r+1)
        a, b = chi[:, :, 0].copy(), chi[:, :, 1].copy()
        chi[:, :, 1] = f * (c * b - 1j * s * eP * np.roll(a, 1, axis=0))
        chi[:, :, 0] = f * (c * a - 1j * s * np.conj(eP) * np.roll(b, -1, axis=0))
        return chi

    def tick(self, chi):
        M = self.M
        if self.geom == "chain":
            old_e = chi[0, 0, 1]  # same even bond: r=0, (a,b) [and (b,a) equal by symmetry]
            chi = self.even(chi)
            chi[0, 0, 0] = 0; chi[0, 1, 1] = 0
            chi[0, 0, 1] = np.exp(1j * self.phi_e) * old_e; chi[0, 1, 0] = np.exp(1j * self.phi_e) * old_e
            # odd bond (b_j, a_{j+1}): A at b_j, B at a_{j+1} -> r=-1,(b,a) ; A at a_{j+1}, B at b_j -> r=+1,(a,b)
            o1, o2 = chi[M - 1, 1, 0], chi[1, 0, 1]
            chi = self.odd(chi)
            chi[0, 0, 0] = 0; chi[0, 1, 1] = 0
            chi[M - 1, 1, 0] = np.exp(1j * self.phi_o) * o1; chi[1, 0, 1] = np.exp(1j * self.phi_o) * o2
        else:
            chi = self.even(chi)
            chi = self.odd(chi)
        if self.Vph is not None:
            chi = chi * self.Vph
        return chi

    # ---- states and analysis
    def packet(self, sel_band, Kc, k_lo, k_hi, r0, edge=0.02):
        """Relative packet: A at Kc + k (k in [k_lo, k_hi], smooth edges), B at P - (Kc + k); both in band sel_band;
        centred at relative position r0 (cells).  Returns chi and the amplitude profile g(q) on the FFT grid."""
        M = self.M
        q = 2 * PI * np.fft.fftfreq(M)              # A's cell momentum
        k = (q - Kc + PI) % (2 * PI) - PI
        g = 0.5 * (np.tanh((k - k_lo) / edge) - np.tanh((k - k_hi) / edge))
        g[g < 1e-14] = 0.0
        EA, vA, uA = bands(q, self.te, self.to)[sel_band]
        EB, vB, uB = bands(self.P - q, self.te, self.to)[sel_band]
        amp = g * np.exp(-1j * q * r0)
        chi_q = amp[:, None, None] * uA[:, :, None] * uB[:, None, :]
        chi = np.fft.ifft(chi_q, axis=0) * np.sqrt(M)
        if self.geom == "chain":
            # exchange symmetrize: chi_{ab}(r) <- (chi_{ab}(r) + e^{iPr} chi_{ba}(-r)) / sqrt2
            rr = self.r
            ex = np.exp(1j * self.P * rr)[:, None, None] * np.transpose(chi[(-rr) % M], (0, 2, 1))
            chi = (chi + ex) / np.sqrt(2)
            chi[0, 0, 0] = 0; chi[0, 1, 1] = 0
        chi /= np.sqrt(np.sum(np.abs(chi) ** 2))
        return chi, q, g

    def project(self, chi_part):
        """Band-pair weights per A-momentum q: returns W[sA, sB, q] (sA, sB in 0/1 band index)."""
        M = self.M
        q = 2 * PI * np.fft.fftfreq(M)
        F = np.fft.fft(chi_part, axis=0) / np.sqrt(M)
        bA = bands(q, self.te, self.to); bB = bands(self.P - q, self.te, self.to)
        W = np.zeros((2, 2, M))
        for sA in (0, 1):
            for sB in (0, 1):
                uA, uB = bA[sA][2], bB[sB][2]
                amp = np.einsum("qa,qb,qab->q", np.conj(uA), np.conj(uB), F)
                W[sA, sB] = np.abs(amp) ** 2
        return q, W
