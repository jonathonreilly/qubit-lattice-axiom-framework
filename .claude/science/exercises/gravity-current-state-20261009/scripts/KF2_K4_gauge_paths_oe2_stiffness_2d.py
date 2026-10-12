#!/usr/bin/env python3
"""K4 (kill agent, route F2): does gauge invariance on nearest-neighbour links bring the
label-space structure back at O(e^2)?

2D toy (sites Z^2, L x L torus, Hamiltonian, continuous time), metric g = exp(eps X), det g = 1,
A = g^{1/2}. Gaussian proper-distance weights w_n = exp(-|A n|^2/2s^2)/(pi s^4) (so K ~ p_cov^2).

MATTER: complex scalar, mass M, smooth hopping in proper distance:
   H_m = sum |pi|^2 + sum_x sum_n (w_n/2) |exp(i e theta_n(x)) phi_{x+n} - phi_x|^2 + M^2 |phi|^2,
   K_m(p) = sum_n w_n (1 - cos p.n),  omega_p = sqrt(M^2 + K_m).
TRANSPORTER: theta_n(x) = sum_links rho_n(link) A_link, rho_n = the UNIFORM average over monotone
   lattice staircases from 0 to n (a lattice flow, div = delta_n - delta_0; exactly gauge covariant).
PHOTON on nn links, built to be as smooth as possible: kinetic metric T(q) = sum_n (w_n/2) c_n^* c_n^T
   (c_n = Fourier transform of rho_n), potential M = K T - (T d)(T d)^dag, d_mu = e^{i q_mu} - 1.
   Then the transverse frequency is EXACTLY omega_gamma^2 = K(q) = d^dag T d (path-independent, smooth),
   i.e. the free photon is image-suppressed. IR regulator: omega_gamma^2 = K + mu^2 and Coulomb 1/(K + mu^2).
O(e^2) vacuum energy (generalized Coulomb gauge d^dag T A = 0):
   E2 = E_Coulomb + E_transverse(2nd order: photon + pair) + E_diamagnetic.
CONTROL ('smooth'): same code, but the photon-current vertex c_n(q)^T eps(q) is replaced by the smooth
   covariant vector (A n)_a, a = 1, 2 (a Feynman-gauge-like vector field with the same omega_gamma,
   coupled to the smooth current); no lattice paths anywhere. Its stiffness should fall like the free part.
Observable: TT Hessian d^2 E/deps^2 (5-point, h = 0.02) along X1 = diag(1,-1)/sqrt2, X2 = offdiag/sqrt2.
"""
import sys
import numpy as np
from math import comb
from scipy.linalg import expm

X1 = np.diag([1.0, -1.0]) / np.sqrt(2)
X2 = np.array([[0.0, 1.0], [1.0, 0.0]]) / np.sqrt(2)


def staircase_flow(a, b, L):
    """uniform monotone-staircase flow from 0 to (a, b); returns rho[mu] as L x L arrays."""
    rho = np.zeros((2, L, L))
    A_, B_ = abs(a), abs(b)
    sa, sb = (1 if a >= 0 else -1), (1 if b >= 0 else -1)
    tot = comb(A_ + B_, A_)
    for i in range(A_ + 1):
        for j in range(B_ + 1):
            # x-step from (i,j) to (i+1,j) in the reflected frame
            if i < A_:
                P = comb(i + j, i) * comb((A_ - i - 1) + (B_ - j), B_ - j) / tot
                sx, sy = sa * i, sb * j
                if sa > 0:
                    rho[0, sx % L, sy % L] += P
                else:
                    rho[0, (sx - 1) % L, sy % L] -= P
            if j < B_:
                P = comb(i + j, j) * comb((A_ - i) + (B_ - j - 1), A_ - i) / tot
                sx, sy = sa * i, sb * j
                if sb > 0:
                    rho[1, sx % L, sy % L] += P
                else:
                    rho[1, sx % L, (sy - 1) % L] -= P
    return rho


class Model:
    def __init__(self, L, R, M=0.4, mu=0.3):
        self.L, self.M, self.mu = L, M, mu
        k = 2 * np.pi * np.fft.fftfreq(L)
        self.kx, self.ky = np.meshgrid(k, k, indexing="ij")
        nr = np.arange(-R, R + 1)
        ns = [(a, b) for a in nr for b in nr if (a, b) != (0, 0) and a * a + b * b <= R * R]
        self.ns = np.array(ns, float)
        self.nsi = np.array(ns, int)
        Nn = len(ns)
        self.C = np.zeros((Nn, 2, L, L), complex)  # c_{n,mu}(q) = sum_y rho e^{+i q.y}
        for idx, (a, b) in enumerate(ns):
            rho = staircase_flow(a, b, L)
            for m in range(2):
                self.C[idx, m] = np.fft.ifft2(rho[m]) * L * L
        self.d = np.stack([np.exp(1j * self.kx) - 1, np.exp(1j * self.ky) - 1])  # (2, L, L)
        # Ward check: sum_mu c_mu d_mu = e^{i q.n} - 1
        ph = np.exp(1j * (self.ns[:, 0, None, None] * self.kx + self.ns[:, 1, None, None] * self.ky))
        self.ward = np.abs((self.C * self.d[None]).sum(1) - (ph - 1)).max()
        self.phase = ph  # e^{i q.n}

    def weights(self, g, s):
        r2 = np.einsum("ni,ij,nj->n", self.ns, g, self.ns)
        return np.exp(-r2 / (2 * s * s)) / (np.pi * s ** 4)

    def kernel(self, w):
        # K(q) = sum_n w_n (1 - cos q.n)
        return (w[:, None, None] * (1 - self.phase.real)).sum(0)

    def energies(self, g, s, mode):
        L, M, mu = self.L, self.M, self.mu
        N = L * L
        w = self.weights(g, s)
        Kq = self.kernel(w)
        om = np.sqrt(M * M + Kq)                 # matter
        omg = np.sqrt(Kq + mu * mu)              # photon (transverse), IR-regulated
        E0 = om.mean() + 0.5 * omg.mean()        # free part: complex scalar + one transverse mode
        Lg = np.arange(L)
        # index of p' = q - p for every (q, p): handled via np.roll per q below
        if mode == "paths":
            T = 0.5 * np.einsum("n,nalm,nblm->ablm", w, self.C.conj(), self.C)  # (2,2,L,L)
            v = np.einsum("ablm,blm->alm", T, self.d)
            eps0 = np.stack([v[1].conj(), -v[0].conj()])
            nrm = np.einsum("alm,ablm,blm->lm", eps0.conj(), T, eps0).real
            nrm[0, 0] = 1.0
            eps = eps0 / np.sqrt(nrm)
            # q = 0 on the finite torus: both constant-field polarizations are physical; T0-orthonormal pair
            T0 = T[:, :, 0, 0].real
            ev, U = np.linalg.eigh(T0)
            e1, e2 = U[:, 0] / np.sqrt(ev[0]), U[:, 1] / np.sqrt(ev[1])
            eps[:, 0, 0] = e1
            eps2 = np.zeros_like(eps)
            eps2[:, 0, 0] = e2
            Kchk = np.abs(np.einsum("alm,ablm,blm->lm", self.d.conj(), T, self.d).real - Kq).max()
            F = [w[:, None, None] * np.einsum("nalm,alm->nlm", self.C, eps),
                 w[:, None, None] * np.einsum("nalm,alm->nlm", self.C, eps2)]  # f_q(n)
        else:  # smooth control: vertex (A n)_a, two components
            wv, V = np.linalg.eigh(g)
            Am = V @ np.diag(np.sqrt(wv)) @ V.T
            An = self.ns @ Am.T
            F = [w[:, None, None] * An[:, a, None, None] * np.ones((1, L, L)) for a in range(2)]
            Kchk = 0.0
        # place f_q(n) on the torus n-grid for every q: G[q][n]
        Et = 0.0
        Ed_theta = np.zeros(len(w))
        for f in F:
            # <theta_n^2> contribution: (1/N) sum_q |f_q(n)/w_n|^2 /(2 omg)
            Ed_theta += (np.abs(f) ** 2 / (2 * omg[None])).mean(axis=(1, 2)) / np.maximum(w ** 2, 1e-300)
            for qi in range(L):
                for qj in range(L):
                    if not np.any(f[:, qi, qj]):
                        continue
                    fn = np.zeros((L, L), complex)
                    np.add.at(fn, (self.nsi[:, 0] % L, self.nsi[:, 1] % L), f[:, qi, qj])
                    Fm = np.fft.fft2(fn)                      # sum_n f e^{-i p.n}
                    ph_q = np.exp(-1j * (self.kx[qi, qj] * self.nsi[:, 0] + self.ky[qi, qj] * self.nsi[:, 1]))
                    fn2 = np.zeros((L, L), complex)
                    np.add.at(fn2, (self.nsi[:, 0] % L, self.nsi[:, 1] % L), f[:, qi, qj] * ph_q)
                    Fp = np.fft.ifft2(fn2) * N                # sum_n f e^{-i q.n} e^{+i p.n}
                    Gam = (Fp - Fm) / 2j                      # Gamma(p, q)
                    omp2 = np.roll(np.roll(om[::-1, ::-1], qi + 1, 0), qj + 1, 1)  # omega_{q-p}
                    den = 4 * om * omp2 * 2 * omg[qi, qj] * (omg[qi, qj] + om + omp2)
                    Et -= (np.abs(Gam) ** 2 / den).sum()
        Et /= N * N
        # diamagnetic: (1/2) sum_n w_n <theta_n^2> <Re phi*_x phi_{x+n}>
        Pn = np.array([np.mean(np.cos(self.kx * a + self.ky * b) / (2 * om)) for a, b in self.nsi])
        Ed = 0.5 * (w * Ed_theta * Pn).sum()
        # Coulomb: (1/2)(1/N^2) sum_q sum_p (om_p - om_{q-p})^2 /(4 om_p om_{q-p} (K(q)+mu^2))
        Ec = 0.0
        for qi in range(L):
            for qj in range(L):
                omp2 = np.roll(np.roll(om[::-1, ::-1], qi + 1, 0), qj + 1, 1)
                Ec += ((om - omp2) ** 2 / (4 * om * omp2)).sum() / (Kq[qi, qj] + mu * mu)
        Ec *= 0.5 / (N * N)
        return E0, Ec, Et, Ed, Kchk


def hessians(model, s, mode, h=0.02):
    out = {}
    for name, X in (("X1", X1), ("X2", X2)):
        vals = [model.energies(expm(t * h * X), s, mode) for t in (-2, -1, 0, 1, 2)]
        arr = np.array([[v[0], v[1], v[2], v[3], v[1] + v[2] + v[3]] for v in vals])
        H = (-arr[0] + 16 * arr[1] - 30 * arr[2] + 16 * arr[3] - arr[4]) / (12 * h * h)
        out[name] = H
        out["center"] = arr[2]
        out["Kchk"] = vals[2][4]
    return out


if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    svals = [float(x) for x in sys.argv[2:]] or [0.75, 1.0, 1.25, 1.5]
    R = int(np.ceil(7.5 * max(svals)))
    R = min(R, L // 2 - 1)
    model = Model(L, R)
    print(f"L={L} R={R} M={model.M} mu={model.mu}  #n={len(model.ns)}  Ward residual={model.ward:.1e}")
    for s in svals:
        for mode in ("smooth", "paths"):
            o = hessians(model, s, mode)
            c = o["center"]
            print(f"s={s:4.2f} {mode:6s} E0={c[0]:.6f} E2[Coul,trans,dia]=({c[1]:+.5f},{c[2]:+.5f},{c[3]:+.5f})"
                  f"  K-check={o['Kchk']:.1e}")
            for nm in ("X1", "X2"):
                Hh = o[nm]
                print(f"       H_{nm}: free={Hh[0]:+.3e}  O(e2): Coul={Hh[1]:+.3e} trans={Hh[2]:+.3e} dia={Hh[3]:+.3e}  TOTAL={Hh[4]:+.3e}")
            sys.stdout.flush()
