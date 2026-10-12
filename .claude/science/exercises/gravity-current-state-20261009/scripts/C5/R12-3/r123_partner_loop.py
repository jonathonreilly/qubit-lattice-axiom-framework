"""C5 R12-3, script 2: the Q-FIXED photino-selectron vertex of the BF + Clifford-flat matter Nicolai law, and its one-loop
electron speed shift (TRANSVERSE-PHOTINO PART ONLY -- see scope).

Law: W = <B, dA> + <tau, dB> + (1/2) <phi, M_A phi>, phi = 16 real (8 Clifford x 2, complex structure J), M_A = Peierls-
dressed Clifford-flat M (R10-5 Theorem Q content, doubled per Lemma J).  Hess W supplies the electron term psi_phi^+ M_A
psi_phi and the photino-electron-selectron Yukawa  psi_{A_l}^+ (d_{A_l} M_A phi)_a psi_{phi,a} + h.c. (coupling e, no free y).
Momentum-space vertex (bra = selectron k_s, ket = electron p, photino q = p - k_s, link axis j):
   V_j = e J [h_j(-p) - h_j(-k_s)] / X_j,   X_j = -conj(D_j(q)),
with D_j the photon/photino cochain symbol (cochain e^{iq}-1, or the R8-5 box symbol i d(q) e^{iq/2}).
Ward identity check: sum_j conj(D_j) V_j = -e J [h(-p) - h(-k_s)]  (longitudinal photino = matter difference).
BF photino: C chiral => positive- and negative-band projectors have A-block P_T/2 (checked), energy w = sqrt(Delta).
Rayleigh-Schroedinger second order, Dirac seas filled, average over the 4 positive states u of the 8-comp electron
(the J-doubling only duplicates sectors):
   dE(p) = < (1/2) tr(P_T(q) G(q)) / (2 eps) * [ 1/(E_p - w - eps) + 1/(E_p + w + eps) ] >_q ,  G_jj' = R_j . conj(R_j'),
   R_j = V_j^T u (selectron index), eps = E(p - q) (selectron = electron dispersion, matched mass).
   dc^2 = d/dp^2 [2 E_p dE], Richardson in p;  report dc x 16 pi^2 / e^2.
SCOPE (stated before any number): only the transverse (horizontal-at-phi=0) photino is kept.  The O(e) phi-dependence of
the horizontal constraint (fermionic Gauss law G_F = d^+ psi_A + e<J phi, psi_phi>) and the quotient-metric terms also
contribute at O(e^2) to the electron self-energy; they are NOT computed.  So this is not the full one-loop Q-exact value.
Also checked: the one-loop A-B mixing from the selectron loop vanishes (trace of J times a traceless Clifford matrix).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r101_pairing import make_box_curve, wilson_curve
from r85_box_qed_copy import plateau
t0 = time.time()
I2 = np.eye(2); X_ = np.array([[0, 1], [1, 0]], complex); Y_ = np.array([[0, -1j], [1j, 0]]); Z_ = np.diag([1., -1.]).astype(complex)
P = {'I': I2, 'X': X_, 'Y': Y_, 'Z': Z_}
mat = lambda s: np.kron(np.kron(P[s[0]], P[s[1]]), P[s[2]])
A = [mat(s) for s in ('IIY', 'IYX', 'XYZ')]; B = [mat(s) for s in ('YYZ', 'ZIZ', 'ZXX')]; B0 = mat('ZZX')
U16 = 16 * np.pi ** 2

def hj(cur, kj, j):
    return cur['S'](np.array(kj)) * A[j] + cur['W'](np.array(kj)) * B[j]

def h(cur, k, m):
    return m * B0 + sum(hj(cur, k[j], j) for j in range(3))

def Dsym(kind, q):
    q = (np.asarray(q, float) + np.pi) % (2 * np.pi) - np.pi
    if kind == 'cochain':
        return np.exp(1j * q) - 1
    rg = plateau(q, 1.0, 2.0)
    d = rg * q + (1 - rg) * 2 * np.sin(q / 2)
    return 1j * d * np.exp(1j * q / 2)

# ---- Ward identity check on random momenta (electron box curve b1=0.8)
cur = make_box_curve(0.8, 1.6)
rng = np.random.default_rng(3)
J = np.array([[0, -1], [1, 0]], float)
wmax = 0
for _ in range(200):
    p = rng.uniform(-np.pi, np.pi, 3); ks = rng.uniform(-np.pi, np.pi, 3); q = p - ks
    for kind in ('cochain', 'box'):
        D = Dsym(kind, q)
        V = [np.kron(hj(cur, -p[j], j) - hj(cur, -ks[j], j), J) / (-np.conj(D[j])) for j in range(3)]
        lhs = sum(np.conj(D[j]) * V[j] for j in range(3))
        rhs = -np.kron(h(cur, -p, 0.3) - h(cur, -ks, 0.3), J)
        wmax = max(wmax, np.abs(lhs - rhs).max())
print('Ward identity  sum_j conj(D_j) V_j = -eJ[h(-p)-h(-k_s)]  max error over 400 cases: %.1e' % wmax)
# ---- A-B one-loop mixing trace: selectron propagator ~ identity (M^2 = E^2), A-vertex ~ J x scalar, B-vertex ~ J x Clifford
mx = 0
for _ in range(50):
    k = rng.uniform(-np.pi, np.pi, 3); kq = k + rng.uniform(-0.5, 0.5, 3)
    for j in range(3):
        Bv = np.kron(hj(cur, kq[j], j) - hj(cur, k[j], j), J)
        Av = np.kron(np.eye(8), J)  # {M, dM} = d(E^2) * 1 for Clifford-flat curves: J x scalar
        mx = max(mx, abs(np.trace(Av @ Bv)))
print('A-B mixing trace tr[(1 x J)(Clifford x J)] max = %.1e  (selectron loop A-B mixing vanishes)' % mx)
# ---- check: A-block of BF positive projector = P_T / 2
PAIRS = [(1, 2), (2, 0), (0, 1)]
def C_bf(D):  # same as r123_bf_multiplet.C_bf
    d1 = np.zeros((3, 3), complex)
    for r, (j, k) in enumerate(PAIRS):
        d1[r, k] += D[j]; d1[r, j] -= D[k]
    d2 = np.array([[D[0], D[1], D[2]]], complex)
    C = np.zeros((7, 7), complex)
    C[3:6, 0:3] = d1; C[0:3, 3:6] = d1.conj().T
    C[6:7, 3:6] = d2; C[3:6, 6:7] = d2.conj().T
    return C
em = 0
for _ in range(100):
    q = rng.uniform(-np.pi, np.pi, 3)
    for kind in ('cochain', 'box'):
        D = Dsym(kind, q)
        w, Vv = np.linalg.eigh(C_bf(D))
        Pp = Vv[:, w > 1e-9] @ Vv[:, w > 1e-9].conj().T; Pm = Vv[:, w < -1e-9] @ Vv[:, w < -1e-9].conj().T
        PT = np.eye(3) - np.outer(D, D.conj()) / np.vdot(D, D).real
        em = max(em, np.abs(Pp[:3, :3] - PT / 2).max(), np.abs(Pm[:3, :3] - PT / 2).max())
print('A-block of BF photino projectors P_+ and P_- equals P_T/2: max error %.1e' % em)

def dE(cure, kind, m, p, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi  # photino momentum q
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    q = [k[IX], k[IY], k[IZ]]
    D = [Dsym(kind, q[j]) for j in range(3)]
    w = np.sqrt(sum(np.abs(Dj) ** 2 for Dj in D))
    pv = np.array([p, 0.0, 0.0])
    ks = [pv[j] - q[j] for j in range(3)]
    v = lambda kk: cure['S'](kk) ** 2 + cure['W'](kk) ** 2
    eps = np.sqrt(m * m + v(ks[0]) + v(ks[1]) + v(ks[2]))
    H = h(cure, pv, m)
    ev, Ve = np.linalg.eigh(H)
    Ep = ev[-1]
    # Delta-h_j matrices as fields over the grid: dh_j = h_j(-p) - h_j(-k_s) = [S(-p_j)-S(-ks_j)] A_j + [W(-p_j)-W(-ks_j)] B_j
    dS = [cure['S'](np.array(-pv[j])) - cure['S'](-ks[j]) for j in range(3)]
    dW = [cure['W'](np.array(-pv[j])) - cure['W'](-ks[j]) for j in range(3)]
    Xj = [-np.conj(D[j]) for j in range(3)]
    tot = 0.0
    for s in range(4, 8):
        u = Ve[:, s]
        # R_j = dh_j^T u / X_j (8-vector per grid point); J-doubling gives |J^T u|=|u| so it drops out
        aT = [A[j].T @ u for j in range(3)]; bT = [B[j].T @ u for j in range(3)]
        R = [(dS[j][..., None] * aT[j] + dW[j][..., None] * bT[j]) / Xj[j][..., None] for j in range(3)]
        G = [[np.sum(R[j] * np.conj(R[jj]), axis=-1) for jj in range(3)] for j in range(3)]
        Dn = sum(np.abs(D[j]) ** 2 for j in range(3))
        trPTG = sum(G[j][j] for j in range(3)) - sum(np.conj(D[j]) * G[j][jj] * D[jj] for j in range(3) for jj in range(3)) / Dn
        num = 0.5 * trPTG.real / (2 * eps)
        tot += np.mean(num * (1 / (Ep - w - eps) + 1 / (Ep + w + eps)))
    return Ep, tot / 4

def dc(cure, kind, m, N, hstep=0.02):
    E0, d0 = dE(cure, kind, m, 0.0, N)
    vals = []
    for hh in (hstep, 2 * hstep):
        Ep, d = dE(cure, kind, m, hh, N)
        vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2

print('Q-fixed photino-selectron loop, transverse photino only: dc_e x 16pi^2/e^2  (photon loop, R10-1 refereed: -17.96 Wilson, -10.66 box)')
for lab, ce, kind in [('Wilson-circle electron / cochain photino', wilson_curve(), 'cochain'),
                      ('box b1=0.8 electron / box photino (1,2)', make_box_curve(0.8, 1.6), 'box')]:
    for m, N in [(0.1, 48), (0.1, 64), (0.05, 64), (0.05, 80)]:
        r = dc(ce, kind, m, N)
        print('   %-42s m=%.2f N=%2d : %+9.4f   [%.0fs]' % (lab, m, N, r * U16, time.time() - t0), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
