"""B22 library: 1D Dirac quantum walk W = S.C in brickwork (partitioned) form, and
local-lapse ("cut") evolution.

Layout: Lc cells, cell i = sites (2i, 2i+1) = components (a_i, b_i); site 2i sits at
cell coordinate X = i, site 2i+1 at X = i + 1/2.  One period = two layers:
  layer t even : gate u_e on (a_i, b_i)        (position X = i + 1/4)
  layer t odd  : gate u_o on (b_i, a_{i+1})    (position X = i + 3/4)
With u_o = swap and u_e = X.C, C = [[c, -is], [-is, c]], one period is the standard
Dirac walk S.C (S = conditional shift); cos(omega) = cos(theta) cos(k).
A global phase exp(i phi) on u_e multiplies W by exp(i phi): omega -> omega - phi.

Local lapse: a real "time function" F(X) (in layers) selects the down-set of gates
{g : 0 <= t_g < F(X_g)} (and, where F < 0, the inverse of {F(X_g) <= t_g < 0}).
For |F'| < 2 layers per cell this set is past-closed, i.e. a causal cut; W_F is the
product of its gates (single-particle sector; the circuit is quadratic so the many-body
operator is its second quantisation).
"""
import numpy as np

SW = np.array([[0, 1], [1, 0]], complex)


def coin_gate(theta, phi=0.0):
    c, s = np.cos(theta), np.sin(theta)
    return np.exp(1j * phi) * np.array([[-1j * s, c], [c, -1j * s]], complex)


class Brick1D:
    def __init__(self, Lc, theta, phi=0.0, uo=None):
        self.Lc = Lc
        self.theta = theta
        self.ue = coin_gate(theta, phi)
        self.uo = SW.copy() if uo is None else uo
        self.Xe = np.arange(Lc) + 0.25
        self.Xo = np.arange(Lc) + 0.75
        self.Xsite = np.repeat(np.arange(Lc), 2) + np.tile([0.0, 0.5], Lc)

    # ---- one layer, masked
    def layer(self, psi, t, mask, inverse=False):
        if t % 2 == 0:
            u = self.ue.conj().T if inverse else self.ue
            a, b = psi[0::2].copy(), psi[1::2].copy()
            na = u[0, 0] * a + u[0, 1] * b
            nb = u[1, 0] * a + u[1, 1] * b
            psi[0::2] = np.where(mask, na, a)
            psi[1::2] = np.where(mask, nb, b)
        else:
            u = self.uo.conj().T if inverse else self.uo
            x = psi[1::2].copy()
            y = np.roll(psi[0::2], -1)
            nx = u[0, 0] * x + u[0, 1] * y
            ny = u[1, 0] * x + u[1, 1] * y
            psi[1::2] = np.where(mask, nx, x)
            psi[0::2] = np.roll(np.where(mask, ny, y), 1)
        return psi

    def ops(self, F):
        """F: callable X -> layers. Returns ordered op list [(t, mask, inverse)]."""
        Fe, Fo = F(self.Xe), F(self.Xo)
        lo = int(np.floor(min(Fe.min(), Fo.min()))) - 1
        hi = int(np.ceil(max(Fe.max(), Fo.max()))) + 1
        out = []
        for t in range(-1, lo - 1, -1):          # retreat where F < 0 (inverse gates, descending t)
            Ft = Fe if t % 2 == 0 else Fo
            m = Ft <= t
            if m.any():
                out.append((t, m, True))
        for t in range(0, hi + 1):               # advance where F > 0 (ascending t)
            Ft = Fe if t % 2 == 0 else Fo
            m = t < Ft
            if m.any():
                out.append((t, m, False))
        return out

    def apply(self, psi, F, inverse=False):
        psi = psi.copy()
        ol = self.ops(F)
        if inverse:
            for t, m, inv in reversed(ol):
                psi = self.layer(psi, t, m, not inv)
        else:
            for t, m, inv in ol:
                psi = self.layer(psi, t, m, inv)
        return psi

    def group_commutator(self, psi, FN, FM):
        """C psi = W_N W_M W_N^-1 W_M^-1 psi."""
        p = self.apply(psi, FM, inverse=True)
        p = self.apply(p, FN, inverse=True)
        p = self.apply(p, FM)
        p = self.apply(p, FN)
        return p

    # ---- Bloch data
    def Wk(self, k):
        Uo = np.array([[self.uo[1, 1] * 0 + 0, 0], [0, 0]], complex)
        # odd layer in k-space: new a_k = uo[1,0] e^{-ik} b_k + uo[1,1] a_k ; new b_k = uo[0,0] b_k + uo[0,1] e^{ik} a_k
        u = self.uo
        Uo = np.array([[u[1, 1], u[1, 0] * np.exp(-1j * k)], [u[0, 1] * np.exp(1j * k), u[0, 0]]], complex)
        return Uo @ self.ue

    def to_k(self, psi):
        """psi (sites) -> array (Lc, 2) of Bloch amplitudes with psi_i = sum_k e^{iki} psi_k / sqrt(Lc)."""
        A = np.stack([psi[0::2], psi[1::2]], axis=1)
        return np.fft.fft(A, axis=0) / np.sqrt(self.Lc)

    def from_k(self, Ak):
        A = np.fft.ifft(Ak, axis=0) * np.sqrt(self.Lc)
        psi = np.empty(2 * self.Lc, complex)
        psi[0::2], psi[1::2] = A[:, 0], A[:, 1]
        return psi

    def kgrid(self):
        return 2 * np.pi * np.fft.fftfreq(self.Lc)

    def band(self, k, sign=+1):
        """eigenphase omega (W u = e^{-i omega} u) of the band with sign(omega) = sign, and eigenvector."""
        ev, V = np.linalg.eig(self.Wk(k))
        om = -np.angle(ev)
        j = np.argmax(sign * om)
        return om[j], V[:, j] / np.linalg.norm(V[:, j])

    def packet(self, k0, X0, sig, sign=+1):
        ks = self.kgrid()
        dk = (ks - k0 + np.pi) % (2 * np.pi) - np.pi
        Ak = np.zeros((self.Lc, 2), complex)
        _, v0 = self.band(k0, sign)
        j0 = np.argmax(np.abs(v0))
        for n, k in enumerate(ks):
            amp = np.exp(-dk[n] ** 2 * sig ** 2)
            if amp < 1e-14:
                continue
            _, v = self.band(k, sign)
            v = v * np.exp(-1j * np.angle(v[j0]))
            Ak[n] = amp * np.exp(-1j * (k0 + dk[n]) * X0) * v
        psi = self.from_k(Ak)
        return psi / np.linalg.norm(psi)

    def xmean(self, psi):
        p = np.abs(psi) ** 2
        z = np.sum(p * np.exp(2j * np.pi * self.Xsite / self.Lc))
        return self.Lc * np.angle(z) / (2 * np.pi)


def omega_walk(k, theta):
    """positive eigenphase of S.C: cos omega = cos theta cos k."""
    return np.arccos(np.cos(theta) * np.cos(k))


def g1(k, theta, shift=0.0, h=1e-4):
    """(1/2) d^2/dk^2 [(omega - shift)^2] for the positive band (the predicted
    displacement coefficient)."""
    f = lambda q: 0.5 * (omega_walk(q, theta) - shift) ** 2
    return (f(k + h) - 2 * f(k) + f(k - h)) / h ** 2


def oo1(k, theta, shift=0.0, h=1e-6):
    """(omega - shift) * d omega/dk for the positive band."""
    om = omega_walk(k, theta) - shift
    d = (omega_walk(k + h, theta) - omega_walk(k - h, theta)) / (2 * h)
    return om * d
