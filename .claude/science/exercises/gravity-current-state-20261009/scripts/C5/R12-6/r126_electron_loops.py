"""C5 R12-6, script 3: one-loop electron speed shifts from the partner sector of the equivariant (Cartan) law, unrepaired
coupling (W_matter = (1/2)<phi, M_A phi>, no B-dependent matter terms), matched masses, e = 1, units 16 pi^2/e^2.

Vertices (derived in the report, section 3.5; my Fourier convention f_x = sum_q e^{iqx} f_q, D_j = photon symbol):
  photino-A :  psi_+(p)^+ Gamma_j phi_+(k) a_j(q),   Gamma_j = -i e [h_j(p) - h_j(k)] / D_j(q)     (Peierls divided difference)
  eta       :  psi_+(p)^+ (i e 1_8) phi_+(k) eta(q)                                              (Cartan term (v.psi^+) eta)
  photino one-particle operator on (eta, a_1..3, b, tau): K = d + d^+, (a_j, eta) entry D_j(q);  P_+- = (1 +- K/w)/2, w = |D|.
  sigma     :  sqrt2 i e  sbar psi_+^+ chi + h.c.,  chi = psi_-^+ (particle-hole), one-particle operator of chi = -M(k);
               s canonical complex scalar with w^2 = Delta.
Second order (Rayleigh-Schroedinger, Dirac seas filled; normal + Pauli-blocked Z term), averaged over the 4 positive states u:
  photino:  dE = < (1/(2 eps_k)) [ S_+ / (E_p - w - eps_k) + S_- / (E_p + w + eps_k) ] >_q ,  S_+- = sum_{mu nu} (P_+-)_{mu nu} R_mu^+ R_nu,
            R_mu = Gamma_mu^+ u  (mu over eta, a_1..3; b, tau do not couple),  k = p - q,  eps_k = E(k) (selectron = electron band).
  sigma:    dE = < (2 e^2 / (2 w)) [ u^+ P^M_-(k) u / (E_p - E_k - w) + u^+ P^M_+(k) u / (E_p + E_k + w) ] >_q
  dc = (1/2) d/dp^2 [2 E_p dE]  (Richardson in p).
Modes: 'T' = transverse a only with P_T/2 (reproduces R12-3's table: control); 'KD' = eta + a with Kaehler-Dirac projectors.
Ward check: sum_j D_j Gamma_j = -i e [M(p) - M(k)].
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r101_pairing import make_box_curve, wilson_curve
from r85_box_qed_copy import plateau
t0 = time.time()
I2 = np.eye(2); X_ = np.array([[0, 1], [1, 0]], complex); Y_ = np.array([[0, -1j], [1j, 0]]); Z_ = np.diag([1., -1.]).astype(complex)
P_ = {'I': I2, 'X': X_, 'Y': Y_, 'Z': Z_}
mat = lambda s: np.kron(np.kron(P_[s[0]], P_[s[1]]), P_[s[2]])
A = [mat(s) for s in ('IIY', 'IYX', 'XYZ')]; B = [mat(s) for s in ('YYZ', 'ZIZ', 'ZXX')]; B0 = mat('ZZX')
U16 = 16 * np.pi ** 2
e = 1.0

def Dsym(kind, q):
    q = (np.asarray(q, float) + np.pi) % (2 * np.pi) - np.pi
    if kind == 'cochain':
        return np.exp(1j * q) - 1
    rg = plateau(q, 1.0, 2.0)
    d = rg * q + (1 - rg) * 2 * np.sin(q / 2)
    return 1j * d * np.exp(1j * q / 2)

def hfield(cur, kj, j):  # axis-j part as (S, W) coefficient arrays
    return cur['S'](kj), cur['W'](kj)

def Mmat(cur, k, m):
    return m * B0 + sum(cur['S'](np.array(k[j])) * A[j] + cur['W'](np.array(k[j])) * B[j] for j in range(3))

# ---- Ward identity check
rng = np.random.default_rng(7)
cur = make_box_curve(0.8, 1.6); werr = 0
for _ in range(200):
    p = rng.uniform(-np.pi, np.pi, 3); k = rng.uniform(-np.pi, np.pi, 3); q = p - k
    for kind in ('cochain', 'box'):
        D = Dsym(kind, q)
        G = [-1j * e * ((cur['S'](np.array(p[j])) - cur['S'](np.array(k[j]))) * A[j] + (cur['W'](np.array(p[j])) - cur['W'](np.array(k[j]))) * B[j]) / D[j] for j in range(3)]
        werr = max(werr, np.abs(sum(D[j] * G[j] for j in range(3)) + 1j * e * (Mmat(cur, p, 0.3) - Mmat(cur, k, 0.3))).max())
print('Ward identity sum_j D_j Gamma_j = -ie[M(p)-M(k)]: max err %.1e' % werr)

def grid(N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    return [k[IX], k[IY], k[IZ]]

def dE_photino(cur, kind, m, p, N, mode):
    q = grid(N)
    D = [Dsym(kind, q[j]) for j in range(3)]
    w = np.sqrt(sum(np.abs(Dj) ** 2 for Dj in D))
    pv = np.array([p, 0.0, 0.0]); ks = [pv[j] - q[j] for j in range(3)]
    v = lambda kk: cur['S'](kk) ** 2 + cur['W'](kk) ** 2
    eps = np.sqrt(m * m + v(ks[0]) + v(ks[1]) + v(ks[2]))
    ev, Ve = np.linalg.eigh(Mmat(cur, pv, m)); Ep = ev[-1]
    dS = [cur['S'](np.array(pv[j])) - cur['S'](ks[j]) for j in range(3)]
    dW = [cur['W'](np.array(pv[j])) - cur['W'](ks[j]) for j in range(3)]
    tot = 0.0
    for s in range(4, 8):
        u = Ve[:, s]
        Au = [A[j] @ u for j in range(3)]; Bu = [B[j] @ u for j in range(3)]
        # R_j = Gamma_j^+ u = +i e (Delta h_j) u / conj(D_j)
        R = [1j * e * (dS[j][..., None] * Au[j] + dW[j][..., None] * Bu[j]) / np.conj(D[j])[..., None] for j in range(3)]
        trAA = sum(np.sum(np.abs(R[j]) ** 2, axis=-1) for j in range(3))
        if mode == 'T':
            L = sum(np.conj(D[j])[..., None] * R[j] for j in range(3))
            S = 0.5 * (trAA - np.sum(np.abs(L) ** 2, axis=-1) / w ** 2)
            Sp = Sm = S
        else:
            Reta = -1j * e * u                                     # Gamma_eta^+ u
            Getaj = [np.sum(np.conj(Reta) * R[j], axis=-1) for j in range(3)]   # R_eta^+ R_j
            cross = 2 * np.real(sum(np.conj(D[j]) * Getaj[j] for j in range(3)))  # sum_{mu nu} K_{mu nu} G_{mu nu}
            trG = e ** 2 + trAA
            Sp = 0.5 * trG + cross / (2 * w); Sm = 0.5 * trG - cross / (2 * w)
        tot += np.mean((Sp / (Ep - w - eps) + Sm / (Ep + w + eps)) / (2 * eps))
    return Ep, tot / 4

def dE_sigma(cur, kind, m, p, N):
    q = grid(N)
    D = [Dsym(kind, q[j]) for j in range(3)]
    w = np.sqrt(sum(np.abs(Dj) ** 2 for Dj in D))
    pv = np.array([p, 0.0, 0.0]); ks = [pv[j] - q[j] for j in range(3)]
    v = lambda kk: cur['S'](kk) ** 2 + cur['W'](kk) ** 2
    Ek = np.sqrt(m * m + v(ks[0]) + v(ks[1]) + v(ks[2]))
    ev, Ve = np.linalg.eigh(Mmat(cur, pv, m)); Ep = ev[-1]
    tot = 0.0
    for s in range(4, 8):
        u = Ve[:, s]
        # u^+ M(k) u = sum_j [S(k_j) u^+A_j u + W(k_j) u^+B_j u] + m u^+B0 u
        uMu = m * np.real(np.vdot(u, B0 @ u)) + sum(cur['S'](ks[j]) * np.real(np.vdot(u, A[j] @ u)) + cur['W'](ks[j]) * np.real(np.vdot(u, B[j] @ u)) for j in range(3))
        Pm = 0.5 * (1 - uMu / Ek); Ppl = 0.5 * (1 + uMu / Ek)
        tot += np.mean((2 * e ** 2 / (2 * w)) * (Pm / (Ep - Ek - w) + Ppl / (Ep + Ek + w)))
    return Ep, tot / 4


def dcl(fun, cur, kind, m, N, extra=None, hstep=0.02):
    call = (lambda p: fun(cur, kind, m, p, N, extra)) if extra is not None else (lambda p: fun(cur, kind, m, p, N))
    E0, d0 = call(0.0)
    vals = []
    for hh in (hstep, 2 * hstep):
        Ep, d = call(hh)
        vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2

if __name__ == '__main__':
    print('dc_e x 16pi^2/e^2.  Control row T must reproduce R12-3 (Wilson/cochain m=0.1 N=48: -8.88; N=64: -9.01; box m=0.1 N=48: -9.56)')
    cases = [('Wilson e / cochain photino', wilson_curve(), 'cochain'), ('box b1=0.8 e / box photino', make_box_curve(0.8, 1.6), 'box')]
    for lab, ce, kind in cases:
        for m, N in [(0.1, 48), (0.1, 64), (0.05, 64), (0.05, 80)]:
            rT = dcl(dE_photino, ce, kind, m, N, 'T') * U16
            rK = dcl(dE_photino, ce, kind, m, N, 'KD') * U16
            rS = dcl(dE_sigma, ce, kind, m, N) * U16
            print('  %-28s m=%.3f N=%3d :  T(control) %+8.3f | KD photino(eta+A) %+8.3f | sigma %+8.3f | KD+sigma %+8.3f  [%.0fs]'
                  % (lab, m, N, rT, rK, rS, rK + rS, time.time() - t0), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
