"""C5 R10-5, script 4: the electron's one-loop speed shift from a selectron-photino (Yukawa) partner loop, minimal-pairing
construction (NOT an exact lattice supersymmetry -- Lemma PD forbids one in the SUSY-QM class; this is the structural
'edge-supertrace' analogue of R10-1 Theorem P / R10-5 Theorem PT).

Content (per site): electron = 8-comp Clifford-flat field h_e = sum_j [S(k_j) A_j + W(k_j) B_j] + m B0;
photino = 8-comp Clifford-flat massless field on curve c_g (same Clifford matrices, m = 0);
selectrons phi_L, phi_R = complex scalars with the electron's dispersion eps = E_e.
Yukawa  y sum_{X=L,R} [phi_X^dag lambda-bar P_X psi + h.c.] = y sum_X [phi_X^dag lambda^dag B0 P_X psi + h.c.],
P_{L,R} = (1 -+ g5)/2, g5 = B_x B_y B_z B0.  (B0 = beta: lambda-bar = lambda^dag beta; without it the bilinear is the time
component of a vector and the in-box loop is not Lorentz invariant -- first run, kept in r105_partner_loop_nobeta.out (and r105_partner_conv_nobeta.out))
(commutes with A_j, anticommutes with B_j, B0: the lattice analogue of the chiral SUSY-QED Yukawa).
Also the scalar variant Y = B0 (lambda-bar psi, one selectron).
Old-fashioned (Rayleigh-Schroedinger) second order on the one-electron state, Dirac seas filled, averaged over the 4 positive
states at p (p along x):
  dE(p) = (y^2/4) < sum_X [ tr(P_l+(k) X P_e+(p) X^dag) / (2 eps (E_p - E_l(k) - eps))
                         + tr(P_l-(k) X P_e+(p) X^dag) / (2 eps (E_p + E_l(k) + eps)) ] >_k ,  eps = E_e(p - k).
The first term is the normal 'electron -> photino + selectron' graph; the second is the Pauli-blocked vacuum (Z) graph.
dc^2 = d/dp^2 [2 E_p dE(p)] (Richardson over p = h, 2h);  dc = dc^2/2 reported x 16 pi^2 / y^2.
Sign test is normalization-free: the photon loop gives dc_e < 0 (R10-1, referee-confirmed: -10.66 box, -17.96 Wilson).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r101_pairing import make_box_curve, wilson_curve
import itertools
t0 = time.time()
I2 = np.eye(2); X_ = np.array([[0, 1], [1, 0]], complex); Y_ = np.array([[0, -1j], [1j, 0]]); Z_ = np.diag([1., -1.]).astype(complex)
P = {'I': I2, 'X': X_, 'Y': Y_, 'Z': Z_}
mat = lambda s: np.kron(np.kron(P[s[0]], P[s[1]]), P[s[2]])
A = [mat(s) for s in ('IIY', 'IYX', 'XYZ')]; B = [mat(s) for s in ('YYZ', 'ZIZ', 'ZXX')]; B0 = mat('ZZX')
g5 = B[0] @ B[1] @ B[2] @ B0
assert np.allclose(g5 @ g5, np.eye(8)) and all(np.allclose(g5 @ a, a @ g5) for a in A) and all(np.allclose(g5 @ b, -b @ g5) for b in B + [B0])
PL, PR = (np.eye(8) - g5) / 2, (np.eye(8) + g5) / 2
U = 16 * np.pi ** 2

def he(cur, k, m):
    out = m * B0
    for j in range(3):
        out = out + cur['S'](np.array(k[j])) * A[j] + cur['W'](np.array(k[j])) * B[j]
    return out

def dE(cure, curl, m, p, N, Ys):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    Sg, Wg = curl['S'](k), curl['W'](k)
    vg = Sg ** 2 + Wg ** 2
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    El = np.sqrt(vg[IX] + vg[IY] + vg[IZ])
    # selectron energy at p - k (p along x)
    ve = lambda kk: cure['S'](kk) ** 2 + cure['W'](kk) ** 2
    vx = ve(p - k); vyz = ve(-k)
    eps = np.sqrt(m * m + vx[IX] + vyz[IY] + vyz[IZ])
    H = he(cure, (p, 0.0, 0.0), m)
    w, V = np.linalg.eigh(H)
    Pe = V[:, 4:] @ V[:, 4:].conj().T
    Ep = w[-1]
    tot = 0.0
    for Y in Ys:
        Xm = Y @ Pe @ Y.conj().T
        trX = np.trace(Xm).real
        ta = [np.trace(A[j] @ Xm).real for j in range(3)]; tb = [np.trace(B[j] @ Xm).real for j in range(3)]
        c = Sg[IX] * ta[0] + Sg[IY] * ta[1] + Sg[IZ] * ta[2] + Wg[IX] * tb[0] + Wg[IY] * tb[1] + Wg[IZ] * tb[2]
        tp = 0.5 * (trX + c / El); tm = 0.5 * (trX - c / El)
        tot += np.mean(tp / (2 * eps * (Ep - El - eps)) + tm / (2 * eps * (Ep + El + eps)))
    return Ep, tot / 4

def dc(cure, curl, m, N, Ys, h=0.02):
    E0, d0 = dE(cure, curl, m, 0.0, N, Ys)
    vals = []
    for hh in (h, 2 * h):
        Ep, d = dE(cure, curl, m, hh, N, Ys)
        vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    dc2 = (4 * vals[0] - vals[1]) / 3
    return dc2 / 2, d0

cases = [('Wilson circle e / Wilson circle photino', wilson_curve(), wilson_curve()),
         ('box b1=0.8 e / box b1=0.8 photino', make_box_curve(0.8, 1.6), make_box_curve(0.8, 1.6)),
         ('box b1=0.8 e / Wilson circle photino', make_box_curve(0.8, 1.6), wilson_curve())]
print('partner (selectron-photino) loop: dc_e x 16pi^2 / y^2  (photon loop alone, R10-1 refereed: -17.96 Wilson, -10.66 box)')
for lab, ce, cl in cases:
    for m, N in [(0.1, 48), (0.1, 64), (0.05, 64)]:
        r_ch, d0 = dc(ce, cl, m, N, [B0 @ PL, B0 @ PR])
        r_sc, _ = dc(ce, cl, m, N, [B0])
        print('  %-42s m=%.2f N=%2d | chiral (P_L + P_R, two selectrons): %+8.4f | scalar Y=B0 (one selectron): %+8.4f | dE(0)x16pi^2=%+.3f' % (
            lab, m, N, r_ch * U, r_sc * U, d0 * U), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
