"""C5 R12-6, script 4: the B-repaired law (report section 3.4).  W_matter -> (1/2)<phi,(M_A + N_B) phi>,
N_B = kappa sum_{j<k} B_jk A_j A_k J, kappa = -e (cancels the selectron Pauli term against the cross term of (1/2)|d_B W|^2).
Site-local coupling (form factor 1; B_jk read at the site).  New one-loop electron pieces (e = 1, units 16 pi^2/e^2):
  photino b_jk vertex  Gamma_b = i kappa A_j A_k = -i e A_j A_k  (from Hess cross d_B d_phi W);  photino = (eta, a, b) with full
  Kaehler-Dirac projectors (b-a block d1);  electron-B Yukawa  -i e B_jk psi_+^+ A_j A_k psi_+  (B real, 3 comps, w^2 = Delta).
Reports, per curve and mass: unrepaired partner total (KD(eta+a) + sigma, script 3) and repaired total (KD(eta+a+b) + sigma + B).
The quantity of interest is the m-dependence (in-box log) of the totals.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
import r126_electron_loops as L
from r101_pairing import make_box_curve, wilson_curve
A, B, B0, e, U16 = L.A, L.B, L.B0, L.e, L.U16
PAIRS = [(1, 2), (2, 0), (0, 1)]
t0 = time.time()

def dE_photino_full(cur, kind, m, p, N):
    q = L.grid(N)
    D = [L.Dsym(kind, q[j]) for j in range(3)]
    w = np.sqrt(sum(np.abs(Dj) ** 2 for Dj in D))
    pv = np.array([p, 0.0, 0.0]); ks = [pv[j] - q[j] for j in range(3)]
    v = lambda kk: cur['S'](kk) ** 2 + cur['W'](kk) ** 2
    eps = np.sqrt(m * m + v(ks[0]) + v(ks[1]) + v(ks[2]))
    ev, Ve = np.linalg.eigh(L.Mmat(cur, pv, m)); Ep = ev[-1]
    dS = [cur['S'](np.array(pv[j])) - cur['S'](ks[j]) for j in range(3)]
    dW = [cur['W'](np.array(pv[j])) - cur['W'](ks[j]) for j in range(3)]
    # d1[r, c] symbol: (d1 A)_r = D_j A_k - D_k A_j for r <-> (j,k)
    d1 = {}
    for r, (j, k) in enumerate(PAIRS):
        d1[(r, k)] = D[j]; d1[(r, j)] = -D[k]
    tot = 0.0
    for s in range(4, 8):
        u = Ve[:, s]
        Au = [A[j] @ u for j in range(3)]; Bu = [B[j] @ u for j in range(3)]
        Ra = [1j * e * (dS[j][..., None] * Au[j] + dW[j][..., None] * Bu[j]) / np.conj(D[j])[..., None] for j in range(3)]
        Reta = -1j * e * u
        Rb = [-1j * e * (A[j] @ A[k] @ u) for (j, k) in PAIRS]           # Gamma_b^+ u, constant over the grid
        trG = e ** 2 + sum(np.sum(np.abs(Ra[j]) ** 2, axis=-1) for j in range(3)) + sum(np.vdot(x, x).real for x in Rb)
        cross = 2 * np.real(sum(np.conj(D[j]) * np.sum(np.conj(Reta) * Ra[j], axis=-1) for j in range(3)))
        for (r, c), val in d1.items():
            cross = cross + 2 * np.real(np.conj(val) * np.sum(np.conj(Ra[c]) * Rb[r], axis=-1))
        Sp = 0.5 * trG + cross / (2 * w); Sm = 0.5 * trG - cross / (2 * w)
        tot += np.mean((Sp / (Ep - w - eps) + Sm / (Ep + w + eps)) / (2 * eps))
    return Ep, tot / 4

def dE_Bloop(cur, kind, m, p, N):
    q = L.grid(N)
    D = [L.Dsym(kind, q[j]) for j in range(3)]
    w = np.sqrt(sum(np.abs(Dj) ** 2 for Dj in D))
    pv = np.array([p, 0.0, 0.0]); ks = [pv[j] - q[j] for j in range(3)]
    v = lambda kk: cur['S'](kk) ** 2 + cur['W'](kk) ** 2
    Ek = np.sqrt(m * m + v(ks[0]) + v(ks[1]) + v(ks[2]))
    ev, Ve = np.linalg.eigh(L.Mmat(cur, pv, m)); Ep = ev[-1]
    tot = 0.0
    for s in range(4, 8):
        u = Ve[:, s]
        for (j, k) in PAIRS:
            g = (A[k] @ A[j]) @ u * e        # Gamma^+ u up to a phase: Gamma = -i e A_j A_k, Gamma^+ = i e A_k A_j
            # u^+ Gamma P(k) Gamma^+ u = g^+ P(k) g,  P_+- = (1 +- M(k)/E_k)/2
            gMg = m * np.real(np.vdot(g, B0 @ g)) + sum(cur['S'](ks[i]) * np.real(np.vdot(g, A[i] @ g)) + cur['W'](ks[i]) * np.real(np.vdot(g, B[i] @ g)) for i in range(3))
            gg = np.vdot(g, g).real
            Pp = 0.5 * (gg + gMg / Ek); Pm = 0.5 * (gg - gMg / Ek)
            tot += np.mean((1 / (2 * w)) * (Pp / (Ep - Ek - w) + Pm / (Ep + Ek + w)))
    return Ep, tot / 4

if __name__ == '__main__':
    print('dc_e x 16pi^2/e^2 (partner sector only; the photon loop -17.96 Wilson / -10.66 box is common to both laws)')
    for lab, ce, kind in [('Wilson e / cochain photino', wilson_curve(), 'cochain'), ('box b1=0.8 e / box photino', make_box_curve(0.8, 1.6), 'box')]:
        for m, N in [(0.2, 48), (0.1, 64), (0.05, 80)]:
            rK = L.dcl(L.dE_photino, ce, kind, m, N, 'KD') * U16
            rS = L.dcl(L.dE_sigma, ce, kind, m, N) * U16
            rKB = L.dcl(dE_photino_full, ce, kind, m, N) * U16
            rB = L.dcl(dE_Bloop, ce, kind, m, N) * U16
            print('  %-28s m=%.3f N=%3d : unrepaired KD+sigma %+8.3f | repaired: KD(eta,a,b) %+8.3f  sigma %+7.3f  B %+8.3f  total %+8.3f  [%.0fs]'
                  % (lab, m, N, rK + rS, rKB, rS, rB, rKB + rS + rB, time.time() - t0), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
