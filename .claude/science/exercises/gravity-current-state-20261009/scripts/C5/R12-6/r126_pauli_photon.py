"""C5 R12-6, script 2: the selectron Pauli term forced by the Q-exact matter coupling, and the one-loop photon speed.

In every Nicolai / equivariant law whose electron one-particle operator is the Hessian M_A (Peierls-dressed Clifford-flat
M, R10-5 Theorem Q content), the selectron potential is (1/2)|d_phi W|^2 = (1/2) phi M_A^2 phi.  With Peierls dressing,
M_A^2 = E_A^2 (R10-1's minimally coupled scalar) + a Pauli part (continuum: (e/2) F_jk A_j A_k J).
Static probe: A_y(x) = a cos(q x).  Charge-+ sector (complex 8-component selectron), K = M_A^2, vacuum energy tr sqrt(K).
  K1(k+q, k) = -(e/2) [ M0(k+q) G + G M0(k) ],  G = S'(k_y) A_y + W'(k_y) B_y
            = K1'(k+q,k) [R10-1 scalar: -(e/2) d/dk_y (S^2+W^2) * 1]  +  P,   P = -(e/2) Delta_x G,
  Delta_x = [S(k_x+q)-S(k_x)] A_x + [W(k_x+q)-W(k_x)] B_x;   K2_diag = K2'_diag (both (e^2/4)(S^2+W^2)'').
Second order of tr f(K0 + aK1 + a^2 K2):  a^2 [ tr f'(K0) K2 + (1/2) sum_ij f'[1](l_i,l_j) |K1_ij|^2 ],
  f'[1](E^2,E'^2) = -1/(2 E E'(E+E')).   The Pauli part adds  dE2 = (1/2) sum_k sum_{+-} f'[1] ||P||^2  (cross term traceless).
Photon:  static energy (1/4) a^2 V [q^2 + Pi(0,q)], Pi = 4 E2 / V;  the Pauli piece vanishes at q = 0 for any omega, so
  dc_gamma(Pauli) = (1/2) dPi/dq^2 = lim 2 dE2/(V q^2) = - e^2 < |c'(k_x)|^2 |c'(k_y)|^2 / E^3 >   (zone mean)
                  = - e^2 <1/E^3>  for unit-speed (Clifford-flat) curves;  continuum in-box value -(e^2/2pi^2) ln(Lambda/m).
Lorentz test: a Lorentz-invariant Pi^{mu nu} = (q^2 g - q q) pi(q^2); the Pauli vertex couples only to B = curl A, so
  Pi_00(Pauli) = 0 while Pi_T(Pauli) = -q^2 chi != 0: in-box Lorentz violation (not an edge effect).
With the B-coupling repair N_B (report section 3.4): P -> P_res = P + (e/2) D_x(q) A_x A_y (in-box cancellation), and
  dc_gamma(res) = - e^2 < [ (S'_x S'_y - 1)^2 + S'_x^2 W'_y^2 + W'_x^2 S'_y^2 + W'_x^2 W'_y^2 ] / E^3 >  = -2e^2 <(1 - S'_x S'_y)/E^3>.
Units: dc x 16 pi^2 / e^2.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r101_pairing import make_box_curve, wilson_curve
t0 = time.time()
I2 = np.eye(2); X_ = np.array([[0, 1], [1, 0]], complex); Y_ = np.array([[0, -1j], [1j, 0]]); Z_ = np.diag([1., -1.]).astype(complex)
P_ = {'I': I2, 'X': X_, 'Y': Y_, 'Z': Z_}
mat = lambda s: np.kron(np.kron(P_[s[0]], P_[s[1]]), P_[s[2]])
A = [mat(s) for s in ('IIY', 'IYX', 'XYZ')]; B = [mat(s) for s in ('YYZ', 'ZIZ', 'ZXX')]; B0 = mat('ZZX')
U16 = 16 * np.pi ** 2
rng = np.random.default_rng(1262)

# ---- (0) second-order trace formula on random matrices (f = sqrt)
n = 6
Q0 = np.linalg.qr(rng.normal(size=(n, n)))[0]; lam0 = rng.uniform(0.5, 2.0, n); K0 = Q0 @ np.diag(lam0) @ Q0.T
K1 = rng.normal(size=(n, n)); K1 = K1 + K1.T; K2 = rng.normal(size=(n, n)); K2 = K2 + K2.T
def trsqrt(Km):
    return np.sum(np.sqrt(np.linalg.eigvalsh(Km)))
hh = 1e-3
num = (trsqrt(K0 + hh * K1 + hh ** 2 * K2) + trsqrt(K0 - hh * K1 + hh ** 2 * K2) - 2 * trsqrt(K0)) / (2 * hh ** 2)
K1e = Q0.T @ K1 @ Q0; K2e = Q0.T @ K2 @ Q0
fp = 1 / (2 * np.sqrt(lam0))
F = np.array([[(fp[i] - fp[j]) / (lam0[i] - lam0[j]) if i != j else -1 / (4 * lam0[i] ** 1.5) for j in range(n)] for i in range(n)])
pred = np.sum(fp * np.diag(K2e)) + 0.5 * np.sum(F * K1e ** 2)
print('(0) second-order formula for tr sqrt(K): finite difference %.8f vs formula %.8f' % (num, pred))

# ---- (1) algebraic decomposition at random momenta: K1 = K1' + P, K2_diag = K2'_diag, tr(K1'^+ P) = 0
def Mk(cur, k, m):
    return m * B0 + sum(cur['S'](np.array(k[j])) * A[j] + cur['W'](np.array(k[j])) * B[j] for j in range(3))
cur = make_box_curve(0.8, 1.6)
e = 1.0; err1 = err2 = err3 = 0
for _ in range(200):
    k = rng.uniform(-np.pi, np.pi, 3); q = rng.uniform(-0.6, 0.6); m = 0.3
    kp = k + np.array([q, 0, 0])
    G = cur['Sp'](np.array(k[1])) * A[1] + cur['Wp'](np.array(k[1])) * B[1]
    K1 = -(e / 2) * (Mk(cur, kp, m) @ G + G @ Mk(cur, k, m))
    v = lambda kk: cur['S'](np.array(kk)) ** 2 + cur['W'](np.array(kk)) ** 2
    dv = 2 * (cur['S'](np.array(k[1])) * cur['Sp'](np.array(k[1])) + cur['W'](np.array(k[1])) * cur['Wp'](np.array(k[1])))
    K1p = -(e / 2) * dv * np.eye(8)
    Dx = (cur['S'](np.array(kp[0])) - cur['S'](np.array(k[0]))) * A[0] + (cur['W'](np.array(kp[0])) - cur['W'](np.array(k[0]))) * B[0]
    Pm = -(e / 2) * Dx @ G
    err1 = max(err1, np.abs(K1 - K1p - Pm).max()); err3 = max(err3, abs(np.trace(K1p.conj().T @ Pm)))
    # K2 diagonal: (M1^2)_diag + {M0, M2}_diag, M1(k+-q,k) = -(e/2) G, M2_diag = (e^2/4) G'' (numerical second derivative)
    h = 1e-4
    Gpp = ((cur['S'](np.array(k[1] + h)) - 2 * cur['S'](np.array(k[1])) + cur['S'](np.array(k[1] - h))) * A[1]
           + (cur['W'](np.array(k[1] + h)) - 2 * cur['W'](np.array(k[1])) + cur['W'](np.array(k[1] - h))) * B[1]) / h ** 2
    K2 = 2 * (e / 2) ** 2 * G @ G + (e ** 2 / 4) * (Mk(cur, k, m) @ Gpp + Gpp @ Mk(cur, k, m))
    K2p = (e ** 2 / 4) * (v(k[1] + h) - 2 * v(k[1]) + v(k[1] - h)) / h ** 2 * np.eye(8)
    err2 = max(err2, np.abs(K2 - K2p).max())
print('(1) K1 = K1_scalar + P: max err %.1e ; K2_diag = K2_scalar: max err %.1e (num. 2nd deriv) ; |tr K1_scalar^+ P| max %.1e'
      % (err1, err2, err3))

# ---- (2) finite-q direct evaluation vs the q -> 0 zone-mean formula (box curve, m = 0.3)
def zone(cur, m, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W, Sp, Wp = cur['S'](k), cur['W'](k), cur['Sp'](k), cur['Wp'](k)
    return k, S, W, Sp, Wp

def dc_pauli_finite_q(cur, m, N, nq, repaired=False, Dphot=None):
    k, S, W, Sp, Wp = zone(cur, m, N)
    q = 2 * np.pi * nq / N
    v = S ** 2 + W ** 2
    E = np.sqrt(m * m + v[:, None, None] + v[None, :, None] + v[None, None, :])
    tot = 0.0
    for sgn in (+1, -1):
        sh = np.roll(np.arange(N), -sgn * nq)
        dS = S[sh] - S; dW = W[sh] - W
        Ep = np.sqrt(m * m + v[sh][:, None, None] + v[None, :, None] + v[None, None, :])
        fdd = -1.0 / (2 * E * Ep * (E + Ep))
        if not repaired:
            P2 = (e ** 2 / 4) * 8 * (dS ** 2 + dW ** 2)[:, None, None] * (Sp ** 2 + Wp ** 2)[None, :, None]
        else:
            Dq = sgn * Dphot(q)
            P2 = (e ** 2 / 4) * 8 * ((dS[:, None] * Sp[None, :] - Dq) ** 2 + (dS[:, None] * Wp[None, :]) ** 2
                                     + (dW[:, None] * Sp[None, :]) ** 2 + (dW[:, None] * Wp[None, :]) ** 2)[:, :, None]
        tot += 0.5 * np.sum(fdd * P2)
    dE2 = tot
    return 2 * dE2 / (N ** 3 * Dphot(q) ** 2)

def dc_pauli_limit(cur, m, N, repaired=False):
    k, S, W, Sp, Wp = zone(cur, m, N)
    v = S ** 2 + W ** 2
    vyz = v[:, None] + v[None, :]
    tot = 0.0
    for ix in range(N):                      # slice over k_x to bound memory
        E3 = (m * m + v[ix] + vyz) ** 1.5    # (k_y, k_z)
        if not repaired:
            num = ((Sp[ix] ** 2 + Wp[ix] ** 2) * (Sp ** 2 + Wp ** 2))[:, None]
        else:
            num = ((Sp[ix] * Sp - 1) ** 2 + (Sp[ix] * Wp) ** 2 + (Wp[ix] * Sp) ** 2 + (Wp[ix] * Wp) ** 2)[:, None]
        tot += np.sum(num / E3)
    return -e ** 2 * tot / N ** 3

dbox = lambda qq: qq                       # box photon inside its plateau (|q| <= 1)
dwil = lambda qq: 2 * np.sin(qq / 2)       # cochain photon
print('(2) finite-q check (x 16pi^2/e^2), box curve b1=0.8, m=0.3, N=96:')
for nq in (1, 2, 4):
    print('     q = 2pi*%d/96: unrepaired %+9.4f   repaired %+9.4f' % (nq, U16 * dc_pauli_finite_q(cur, 0.3, 96, nq, False, dbox),
                                                                         U16 * dc_pauli_finite_q(cur, 0.3, 96, nq, True, dbox)))
print('     q -> 0 limit formula:  unrepaired %+9.4f   repaired %+9.4f' % (U16 * dc_pauli_limit(cur, 0.3, 96), U16 * dc_pauli_limit(cur, 0.3, 96, True)))

# ---- (3) mass dependence: the in-box log
print('(3) one-loop photon speed from the selectron Pauli term, dc_gamma x 16pi^2/e^2 (q -> 0), and the repaired residual:')
print('     continuum in-box estimate: -8 [ln(2 Lambda/m) - 1]; slope d/d ln(1/m) should be -8 if in-box')
for lab, cu in (('Wilson circle', wilson_curve()), ('box b1=0.8', make_box_curve(0.8, 1.6)), ('box b1=0.5', make_box_curve(0.5, 1.0))):
    prev = None
    for m, N in ((0.4, 128), (0.2, 192), (0.1, 256), (0.05, 320), (0.025, 384)):
        u = U16 * dc_pauli_limit(cu, m, N); r = U16 * dc_pauli_limit(cu, m, N, True)
        u2 = U16 * dc_pauli_limit(cu, m, int(N * 1.25))
        slope = '' if prev is None else ' slope per ln2: %+7.3f' % ((u - prev) / np.log(2))
        print('     %-14s m=%.3f N=%3d: unrepaired %+9.3f (N*1.25: %+9.3f)  repaired %+8.4f %s  [%.0fs]'
              % (lab, m, N, u, u2, r, slope, time.time() - t0), flush=True)
        prev = u
print('elapsed %.1fs' % (time.time() - t0))
