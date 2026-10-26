#!/usr/bin/env python3
"""J:derive:review-20260929-ens-parity-capacity:a1  independent check.

Disjoint machinery: nothing is imported from the ENS source modules.
 * potential Fourier coefficients: Gauss-Legendre quadrature of -sqrt(1-tau sin^2(phi/2)) (source: FFT of w_tau)
 * physical coupling G(n-q) built directly (source: displaced-offset reduction of the old model)
 * level labels: dominant overlap AND adiabatic continuation (source: dominant overlap only)
 * envelope: Fourier-in-offset analysis of f06(q) (source: sampled grid + bounded 1-D searches)
 * own least-squares calibration (5 equations, 5 unknowns) from the declared start, own rounding corners
Every number is recomputed here; the five calibration values and the digitized
Ramsey bins are embedded literals copied from the pinned source files.
"""
import os, sys, time, hashlib
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
from itertools import product
import numpy as np
import sympy as sp
from scipy.linalg import eigh
from scipy.optimize import least_squares, brentq, linear_sum_assignment
from scipy.stats import spearmanr

T0 = time.time()
RES = []


def chk(name, ok, detail=''):
    RES.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name + (' | ' + detail if detail else ''), flush=True)


# ----------------------------------------------------------------------------
# embedded inputs (pinned source values)
# ----------------------------------------------------------------------------
CAL = np.array([5.354767, 10.5356, 7.76131, 7.75608, 7.75135])   # f01 f02 fres1 fres2 fres3 (GHz)
IDX = [0, 1, 6, 7, 8]                                            # positions in [f01..f06, fres1..fres7]
HALF = np.array([5e-7, 5e-5, 5e-6, 5e-6, 5e-6])                  # half printed-decimal units
NOTE_P = np.array([0.1841990760792327, 21.829772186093592, 7.738912856323958,
                   0.18858878602560333, 0.15464897201354028])    # note's selected point (for comparison only)
NOTE_COS = np.array([0.16655540250096806, 23.191412220844157, 7.738909192510041, 0.17934375909924566, 0.0])
NOTE_MAX = {'andreev': 3.464585, 'cosine': 0.544477}             # note's numerical parity maxima, MHz
NOTE_CORNER = {'andreev': (2.586015, 4.596982), 'cosine': (0.540476, 0.548504)}
# digitized Figure-7 bins (centre MHz, mean blue-minus-red), bin height 0.3317 MHz
BIN_H = 0.3317000032594169
ROW = {
    40: [(8.12586238741433, .0980392156862745), (8.457562390673734, .10849673202614378), (8.78926239393314, .36993464052287583),
         (9.120962397192589, .2705882352941177), (9.452662400451992, .13464052287581701), (9.784362403711398, .064),
         (10.12, .084), (10.45, .097), (10.78, .173), (11.111162416749057, .478), (11.44, .129), (11.77, .095), (12.11, .076), (12.44, .086)],
    120: [(8.12586238741433, .102), (8.457562390673734, .125), (8.78926239393314, .580), (9.12, .202), (9.45, .086), (9.78, .076),
          (10.12, .084), (10.45, .090), (10.78, .439), (11.111162416749057, .467), (11.44, .135), (11.77, .090), (12.11, .082), (12.44, .069)],
}
# author pixel-profile peak pairs (MHz) at the six nominal times (central column): (low, high)
AUTHOR = {20: (9.140, 10.783), 40: (8.775, 11.148), 60: (9.140, 10.783), 80: (8.775, 10.783), 100: (9.140, 10.783), 120: (8.821, 11.102)}

# optional provenance check of the source files if they sit next to this script
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = {'ens_physical_parity_2026_09_27.py': '253c90a25efb3270a9101bf01a590f3c5297a6de764b5641a57d77d03c56c443',
       'ENS_CAVITY_CALIBRATED_HOLDOUT_OPEN_GATE_NOTE_2026-09-27.md': 'f48540b024fab42672e0076316d2a3fbf79ddeafa55f090dea7bb385523a8b08'}
for fn, h in SRC.items():
    pth = os.path.join(HERE, 'src', fn)
    if os.path.exists(pth):
        chk('source hash ' + fn, hashlib.sha256(open(pth, 'rb').read()).hexdigest() == h)
    else:
        print('NOTE source file absent, hash not re-verified here: ' + fn)

# ----------------------------------------------------------------------------
# model (own implementation)
# ----------------------------------------------------------------------------
_gx, _gw = np.polynomial.legendre.leggauss(400)
_PHI = (_gx + 1) * np.pi / 2
_W = _gw * np.pi / 2


def fourier_coeffs(tau, N):
    """F_m = (1/pi) int_0^pi V0(phi) cos(m phi) dphi, V0 = -sqrt(1 - tau sin^2(phi/2)); m=0..2N."""
    raw = -np.sqrt(1 - tau * np.sin(_PHI / 2) ** 2)
    m = np.arange(0, 2 * N + 1)
    return (np.cos(np.outer(m, _PHI)) @ (raw * _W)) / np.pi


def pot_matrix(tau, ej, N):
    n = np.arange(-N, N + 1)
    D = np.abs(n[:, None] - n[None, :])
    if tau == 0:
        F = np.zeros(2 * N + 1)
        F[1] = -0.5 * ej
    else:
        F = fourier_coeffs(tau, N)
        F = F * (-ej / (2 * F[1]))           # cos(phi) coefficient 2F_1 -> -EJ1
    return F[D]


def delta_of(p):
    return p[3] ** 2 / (4 * p[0] * p[2])


def reduced_levels(p, ng, qc, N, M, K, return_vecs=False):
    """Charge basis -> M lowest eigenstates of the bare transmon at offset ng, coupling G (n - qc)(a+a^dag)."""
    ec, ej, om, g, tau = p
    n = np.arange(-N, N + 1, dtype=float)
    Hc = pot_matrix(tau, ej, N) + np.diag(4 * ec * (n - ng) ** 2)
    e, U = eigh(Hc, subset_by_index=[0, M - 1])
    e = e - e[0]
    nm = U.T @ (n[:, None] * U) - qc * np.eye(M)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    H = np.diag((om * np.arange(K)[:, None] + e[None, :]).ravel()) + g * np.kron(a + a.T, nm)
    E, V = eigh(H)
    labs = [(0, j) for j in range(7)] + [(1, j) for j in range(7)]
    ix = [int(np.argmax(V[k * M + j] ** 2)) for k, j in labs]
    if len(set(ix)) != 14:
        raise ValueError('label collision')
    ee = E[ix]
    f = np.r_[ee[1:7] - ee[0], ee[7:14] - ee[0:7]]
    if return_vecs:
        return f, V[:, ix], ix, [float(V[k * M + j, i] ** 2) for (k, j), i in zip(labs, ix)]
    return f


def full_levels(p, ng, qc, N, K, method='overlap', ramp=(0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 1.0)):
    """Dense charge (x) Fock matrix, no transmon-subspace reduction.  Labels: overlap with bare (transmon j, Fock k)
    states, or adiabatic continuation in the coupling G -> lam G from the bare product states."""
    ec, ej, om, g, tau = p
    n = np.arange(-N, N + 1, dtype=float)
    d = 2 * N + 1
    Hc = pot_matrix(tau, ej, N) + np.diag(4 * ec * (n - ng) ** 2)
    _, B = eigh(Hc)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    base = np.kron(Hc, np.eye(K)) + np.kron(np.eye(d), om * np.diag(np.arange(K).astype(float)))
    X = g * np.kron(np.diag(n - qc), a + a.T)
    labs = [(j, 0) for j in range(7)] + [(j, 1) for j in range(7)]
    bare = np.column_stack([np.kron(B[:, j], np.eye(K)[:, k]) for j, k in labs])
    if method == 'overlap':
        E, V = eigh(base + X)
        ov = np.abs(bare.T @ V) ** 2
        ix = ov.argmax(axis=1)
        assert len(set(ix.tolist())) == 14
        lev = E[ix]
        wts = ov[np.arange(14), ix]
    else:
        S = bare
        for lam in ramp:
            E, V = eigh(base + lam * X)
            ov = np.abs(S.T @ V) ** 2
            _, col = linear_sum_assignment(-ov)
            S = V[:, col]
            ix = col
        lev = E[ix]
        wts = np.abs(bare.T @ S).diagonal() ** 2
    f = np.r_[lev[1:7] - lev[0], lev[7:14] - lev[:7]]
    return f, np.array(ix), wts


# standard cutoffs
CUT = dict(N=16, M=14, K=9)
FINE = dict(N=20, M=18, K=12)


def f_phys(p, q, **cut):
    return reduced_levels(p, q, q, **cut)


def pred_mean(p, **cut):
    """benchmark convention: mean of the physical parity pair (0, 1/2)"""
    return (f_phys(p, 0.0, **cut) + f_phys(p, 0.5, **cut)) / 2


def s_pair(p, q, **cut):
    return abs(f_phys(p, q, **cut)[5] - f_phys(p, q + 0.5, **cut)[5]) * 1000.0   # MHz, full energy-frequency splitting


BOUNDS5 = ([.03, 1, 7, .001, 0], [1, 100, 8.5, 1, .99])
SC5 = np.array([.2, 20, 8, .1, .2])
DIV = np.array([1, 2, 1, 1, 1], float)


def fit5(target, start, cut=CUT):
    def r(p):
        return (pred_mean(p, **cut)[IDX] - target) / DIV
    res = least_squares(r, start, bounds=BOUNDS5, x_scale=SC5, ftol=1e-14, xtol=1e-14, gtol=1e-14, max_nfev=400)
    err = pred_mean(res.x, **cut)[IDX] - target
    return res.x, float(np.abs(err).max())


def fit4cos(target, start, cut=CUT):
    def r(x):
        return (pred_mean(np.r_[x, 0.0], **cut)[IDX[:4]] - target) / DIV[:4]
    res = least_squares(r, start, bounds=(BOUNDS5[0][:4], BOUNDS5[1][:4]), x_scale=SC5[:4], ftol=1e-14, xtol=1e-14, gtol=1e-14, max_nfev=400)
    p = np.r_[res.x, 0.0]
    return p, float(np.abs(pred_mean(p, **cut)[IDX[:4]] - target).max())


# ----------------------------------------------------------------------------
# 1  exact gauge identity (symbolic; PROVED by completing the square, CHECKED here by expansion)
# ----------------------------------------------------------------------------
a_, ad_, b_, bd_ = sp.symbols('a ad b bd', commutative=False)
n_, q_, EC_, Om_, G_, V_ = sp.symbols('n q EC Omega G V', real=True)
gam = G_ * q_ / Om_
delta_s = G_ ** 2 / (4 * EC_ * Om_)
Hphys = 4 * EC_ * (n_ - q_) ** 2 + V_ + Om_ * ad_ * a_ + G_ * (n_ - q_) * (a_ + ad_)
Hdisp = sp.expand(Hphys.subs({a_: b_ + gam, ad_: bd_ + gam}, simultaneous=True))
ng_eff = (1 - delta_s) * q_
Hold = 4 * EC_ * (n_ - ng_eff) ** 2 + V_ + Om_ * bd_ * b_ + G_ * n_ * (b_ + bd_)
scalar = 4 * EC_ * q_ ** 2 * delta_s * (1 - delta_s)
diff = sp.simplify(sp.expand(Hdisp - sp.expand(Hold) - scalar))
chk('1 displacement identity H_phys(q) -> H_old((1-delta)q)+4EC q^2 delta(1-delta) (symbolic, delta=G^2/4EC Omega)', diff == 0, 'residual=' + str(diff))
# commutation relation preserved by the shift a -> b + gamma (c-number)
comm = sp.expand((b_ + gam) * (bd_ + gam) - (bd_ + gam) * (b_ + gam))
chk('1b [a,a^dag]=[b,b^dag] under the c-number shift', sp.simplify(comm - (b_ * bd_ - bd_ * b_)) == 0)

# ----------------------------------------------------------------------------
# 2  calibration reproduced independently
# ----------------------------------------------------------------------------
t = time.time()
P, perr = fit5(CAL, np.array([.18, 20, 7.75, .1, .2]))
rel = np.abs(P / NOTE_P - 1).max()
chk('2 own calibration from declared start tau=.2 reproduces the note parameters (rel diff < 1e-6), residual < 1e-9 GHz',
    rel < 1e-6 and perr < 1e-9, 'max rel diff=%.2e residual=%.1e GHz params=%s (%.1fs)' % (rel, perr, np.array2string(P, precision=10), time.time() - t))
PC, perrc = fit4cos(CAL[:4], np.array([.18, 20, 7.75, .1]))
relc = np.abs(PC[:4] / NOTE_COS[:4] - 1).max()
chk('2b own cosine baseline (4 inputs, tau=0) reproduces the note parameters (rel < 1e-6)', relc < 1e-6 and perrc < 1e-9, 'rel=%.2e' % relc)
DEL = delta_of(P)
chk('2c quadratic stability 4EC > G^2/Omega and delta<1', 4 * P[0] > P[3] ** 2 / P[2] and 0 < DEL < 1, 'delta=%.8f' % DEL)

# potential-shape sanity: note's higher-harmonic ratios and raw-sqrt == w_tau normalization
F = fourier_coeffs(P[4], 4)
r2, r3 = -F[2] / F[1], -F[3] / F[1]
chk('2d potential: cos(2phi), cos(3phi) coefficients in units of EJ1 = +.0104917249, -.00022017684 (note)',
    abs(r2 / 0.0104917249 - 1) < 1e-6 and abs(r3 / (-0.00022017684) - 1) < 1e-5, 'got %.10f, %.8f' % (r2, r3))
phi = np.linspace(0, 2 * np.pi, 4097)[:-1]
s_ = np.sin(phi / 2) ** 2
w = 4 * s_ / (1 + np.sqrt(1 - P[4] * s_))
raw = -np.sqrt(1 - P[4] * s_)
chk('2e identity w_tau = 4(1-sqrt(1-tau s))/tau = affine image of raw -sqrt(1-tau s)', np.abs(w - (4 / P[4]) * (1 + raw)).max() < 1e-12)

# ----------------------------------------------------------------------------
# 3  direct-charge vs displaced-oscillator representation
# ----------------------------------------------------------------------------
# 3a: old-convention model is periodic with period (1-delta) in ng (corollary of 1)
per = []
for ng in (0.0, 0.13, 0.31):
    per.append((reduced_levels(P, ng + (1 - DEL), 0.0, **FINE)[5] - reduced_levels(P, ng, 0.0, **FINE)[5]) * 1e9)
per1 = [(reduced_levels(P, ng + 1.0, 0.0, **FINE)[5] - reduced_levels(P, ng, 0.0, **FINE)[5]) * 1e9 for ng in (0.0, 0.13, 0.31)]
chk('3a old (G n) convention: f06(ng+(1-delta)) = f06(ng) to < 3 Hz, but period 1 fails by kHz-scale', max(abs(x) for x in per) < 3 and min(abs(x) for x in per1) > 1e3,
    'period (1-delta): %s Hz ; period 1: %s Hz' % (np.round(per, 3), np.round(per1, 0)))
# 3b: truncation-only difference between the two representations in the SAME dense space
errs = []
for K in (3, 4, 5, 6, 8, 10, 12):
    m = 0
    for q in (0.0, 0.25, 0.5):
        fp, _, _ = full_levels(P, q, q, 10, K)
        fo, _, _ = full_levels(P, (1 - DEL) * q, 0.0, 10, K)
        m = max(m, np.abs(fp - fo).max() * 1e9)
    errs.append(m)
chk('3b K-scaling of (direct physical) - (displaced old) in the dense charge(x)Fock space: error falls below 1e-3 Hz by K=12 and decreases monotonically',
    errs[-1] < 1e-3 and all(errs[i + 1] <= errs[i] * 1.0001 for i in range(len(errs) - 1)), 'max |diff| Hz for K=3,4,5,6,8,10,12: ' + ', '.join('%.2e' % e for e in errs))
# 3c: dense direct physical vs reduced-basis physical vs source-style displaced reduced (cutoffs of the source)
mx_dense_red, mx_disp = 0.0, 0.0
for q in (0.0, 0.25, 0.5):
    fd, ixd, wd = full_levels(P, q, q, 20, 12)
    fr = reduced_levels(P, q, q, **FINE)
    fo = reduced_levels(P, (1 - DEL) * q, 0.0, **FINE)
    mx_dense_red = max(mx_dense_red, np.abs(fd - fr).max() * 1e9)
    mx_disp = max(mx_disp, np.abs(fd - fo).max() * 1e9)
chk('3c dense direct physical (N=20,K=12, 492 states, no subspace reduction) vs reduced physical vs displaced: all 13 gaps agree to < 1 Hz',
    mx_dense_red < 1.0 and mx_disp < 1.0, 'dense-vs-reduced %.3f Hz, dense-vs-displaced %.3f Hz' % (mx_dense_red, mx_disp))

# ----------------------------------------------------------------------------
# 4  branch labels: overlap vs adiabatic continuation (coupling) and continuity in q
# ----------------------------------------------------------------------------
ok_lab, minw = True, 1.0
for q in (0.0, 0.25, 0.5):
    fo, io, wo = full_levels(P, q, q, 14, 10, 'overlap')
    fc, ic, wc = full_levels(P, q, q, 14, 10, 'continuation')
    same = np.array_equal(io, ic) and np.abs(fo - fc).max() < 1e-9
    ok_lab &= bool(same)
    minw = min(minw, wo.min())
chk('4a dominant-overlap labels = adiabatic-continuation labels (coupling ramp) at q=0,1/4,1/2; all 14 states', ok_lab and minw > 0.9, 'min dominant overlap=%.5f' % minw)
# continuity in q along a 129-point loop (reduced basis, overlap-based tracking)
Q129 = np.arange(129) / 128
prev, jumps, minwq, f06loop = None, 0, 1.0, []
for q in Q129:
    f, vec, ix, wts = reduced_levels(P, q, q, 16, 14, 10, return_vecs=True)
    minwq = min(minwq, min(wts))
    if prev is not None:
        _, col = linear_sum_assignment(-np.abs(prev.T @ vec) ** 2)
        if not np.array_equal(col, np.arange(14)):
            jumps += 1
    prev = vec
    f06loop.append(f[5])
f06loop = np.array(f06loop)
chk('4b following the 14 labelled states around q in [0,1] (129 steps): tracked state = dominant-overlap state at every step, f06(1)=f06(0)',
    jumps == 0 and abs(f06loop[-1] - f06loop[0]) * 1e9 < 1.0, 'label jumps=%d min dominant weight=%.5f period closure=%.3f Hz' % (jumps, minwq, abs(f06loop[-1] - f06loop[0]) * 1e9))

# ----------------------------------------------------------------------------
# 5  exact structure of the offset envelope (Fourier in q)
# ----------------------------------------------------------------------------
def fourier_f06(p, npts=128, **cut):
    q = np.arange(npts) / npts
    f = np.array([f_phys(p, x, **cut)[5] for x in q])
    c = np.fft.rfft(f) / npts
    c[1:] *= 2
    return f, c


def odd_series(c, kmax=15):
    return {k: c[k].real for k in range(1, kmax + 1, 2)}


f128, c128 = fourier_f06(P, 128, **FINE)
sin_part = np.abs(c128.imag).max() * 1000      # MHz
a1 = abs(c128[1].real) * 1000
oddk = [k for k in range(3, 64, 2)]
Rk = sum(k * k * abs(c128[k].real) * 1000 for k in oddk)
evenk = [(k, abs(c128[k].real) * 1000) for k in (2, 4, 6)]
s_grid = np.array([(f128[i] - f128[i + 64]) * 1000 for i in range(64)])
q64 = np.arange(64) / 128
s_series = 2 * sum(c128[k].real * np.cos(2 * np.pi * k * q64) for k in range(1, 64, 2)) * 1000
chk('5a f06(q) even in q (sine coefficients < 1e-6 MHz)', sin_part < 1e-6, 'max|Im|=%.2e MHz' % sin_part)
chk('5b parity splitting uses ONLY odd harmonics: s(q)=2|sum_{k odd} a_k cos 2 pi k q| reproduces 64 pair differences to < 1e-6 MHz',
    np.abs(np.abs(s_grid) - np.abs(s_series)).max() < 1e-6, 'max diff %.2e MHz' % np.abs(np.abs(s_grid) - np.abs(s_series)).max())
chk('5c s(1/4)=0 exactly for every odd harmonic (cos(k pi/2)=0) and numerically', abs(s_grid[32]) < 1e-6, 's(1/4)=%.2e MHz' % abs(s_grid[32]))
# monotonicity certificate: ds/dq = -4 pi sum_odd k a_k sin(k theta); |sin(k th)|<=k sin(th)
cert = a1 / Rk
chk('5d certificate |a_1| > sum_{k odd>=3} k^2 |a_k| (then s is strictly monotone on [0,1/4], so max over offset = s(0) and the 4-interval search is redundant)',
    cert > 10, '|a_1|=%.6f MHz, sum k^2|a_k|(k odd 3..63)=%.3e MHz, ratio=%.1f (a_3 level is at eigensolver noise)' % (a1, Rk, cert))
S0 = abs(s_grid[0])
chk('5e envelope maximum = s(0) = 2|sum odd a_k| = %.6f MHz equals the note\'s 3.464585 (|diff| < 2e-4 MHz)' % S0, abs(S0 - NOTE_MAX['andreev']) < 2e-4, 'diff %.2e MHz' % (S0 - NOTE_MAX['andreev']))
chk('5f even harmonics move the doublet centre: pair centre = a_0 + a_2 cos 4 pi q + ..., range 2|a_2| = %.2e MHz vs the note\'s centre range 0.00172418 MHz (|diff| < 5e-5)' % (2 * evenk[0][1]),
    abs(2 * evenk[0][1] - 0.0017241800769340898) < 5e-5)
# cosine baseline
fc128, cc128 = fourier_f06(PC, 128, **FINE)
a1c = abs(cc128[1].real) * 1000
Rc = sum(k * k * abs(cc128[k].real) * 1000 for k in oddk)
S0c = abs((fc128[0] - fc128[64])) * 1000
chk('5g cosine baseline: same odd-harmonic certificate (ratio>10) and max s = %.6f MHz = note 0.544477 (|diff|<2e-4)' % S0c,
    a1c / Rc > 10 and abs(S0c - NOTE_MAX['cosine']) < 2e-4, 'ratio %.1f' % (a1c / Rc))

# ----------------------------------------------------------------------------
# 6  convention (physical vs legacy pair) size against the other uncertainties
# ----------------------------------------------------------------------------
def old_conv_f06(p, ng, **cut):
    return reduced_levels(p, ng, 0.0, **cut)[5]


leg_a = abs(old_conv_f06(P, 0.0, **FINE) - old_conv_f06(P, 0.5, **FINE)) * 1e9          # Hz, legacy pair (ng, ng+1/2)
phy_a = abs(old_conv_f06(P, 0.0, **FINE) - old_conv_f06(P, 0.5 * (1 - DEL), **FINE)) * 1e9
dA = leg_a - phy_a
dC_del = delta_of(PC)
leg_c = abs(old_conv_f06(PC, 0.0, **FINE) - old_conv_f06(PC, 0.5, **FINE)) * 1e9
phy_c = abs(old_conv_f06(PC, 0.0, **FINE) - old_conv_f06(PC, 0.5 * (1 - dC_del), **FINE)) * 1e9
chk('6a legacy-pair minus physical-pair endpoint splitting: Andreev %.0f Hz (note ~337), cosine %.0f Hz (note ~53)' % (abs(dA), abs(leg_c - phy_c)),
    abs(abs(dA) - 337) < 40 and abs(abs(leg_c - phy_c) - 53) < 15)
# calibration-input shift that has the same effect on the capacity (via fres2 sensitivity computed in 7)
REL_CONV = abs(dA) / (S0 * 1e6)

# ----------------------------------------------------------------------------
# 7  rounding corners (own fits) and calibration sensitivity of the capacity
# ----------------------------------------------------------------------------
t = time.time()
cap_a, f06_a = [], []
for sg in product((-1, 1), repeat=5):
    sh = np.array(sg) * HALF
    pp, err = fit5(CAL + sh, P)
    assert err < 1e-9
    d = delta_of(pp)
    cap_a.append(abs(old_conv_f06(pp, 0.0, **FINE) - old_conv_f06(pp, 0.5 * (1 - d), **FINE)) * 1000)
    f06_a.append(pred_mean(pp, **CUT)[5])
cap_c, f06_c = [], []
for sg in product((-1, 1), repeat=4):
    sh = np.array(sg) * HALF[:4]
    pp, err = fit4cos(CAL[:4] + sh, PC[:4])
    assert err < 1e-9
    d = delta_of(pp)
    cap_c.append(abs(old_conv_f06(pp, 0.0, **FINE) - old_conv_f06(pp, 0.5 * (1 - d), **FINE)) * 1000)
    f06_c.append(pred_mean(pp, **CUT)[5])
lo_a, hi_a, lo_c, hi_c = min(cap_a), max(cap_a), min(cap_c), max(cap_c)
chk('7a own 32 Andreev rounding corners: endpoint capacity range [%.6f, %.6f] MHz vs note [2.586015, 4.596982] (|diff|<2e-3)' % (lo_a, hi_a),
    abs(lo_a - NOTE_CORNER['andreev'][0]) < 2e-3 and abs(hi_a - NOTE_CORNER['andreev'][1]) < 2e-3, '%.0fs' % (time.time() - t))
chk('7b own 16 cosine rounding corners: [%.6f, %.6f] MHz vs note [0.540476, 0.548504] (|diff|<2e-3)' % (lo_c, hi_c),
    abs(lo_c - NOTE_CORNER['cosine'][0]) < 2e-3 and abs(hi_c - NOTE_CORNER['cosine'][1]) < 2e-3)
rho = spearmanr(np.array(f06_a), np.log(cap_a)).correlation
rho2 = spearmanr(np.array(f06_a + f06_c), np.log(cap_a + cap_c)).correlation
chk('7c ln(capacity) is a monotone function of the predicted f06 across the 32 Andreev corners (Spearman %.4f) and across Andreev+cosine corners together (%.4f): capacity tracks the level-6 energy relative to the barrier, so it is not independent of the f06 residual' % (rho, rho2),
    rho < -0.9 and rho2 < -0.9)
bl, al = np.polyfit(np.array(f06_a) * 1000, np.log(cap_a), 1)         # per MHz of f06
F06_OBS = 29.1888
cap_at_obs = float(np.exp(al + bl * F06_OBS * 1000))
r2lin = np.corrcoef(np.array(f06_a) * 1000, np.log(cap_a))[0, 1] ** 2
chk('7i (suggested, extrapolation outside the fitted family) slope d ln(cap)/d f06 = %.4f per MHz (R^2=%.3f on the 32 corners); extrapolated to the measured f06=29.1888 GHz the capacity would be ~%.2f MHz (nominal Andreev f06 is %.1f MHz below it)'
    % (bl, r2lin, cap_at_obs, (F06_OBS - pred_mean(P, **CUT)[5]) * 1000), bl < 0 and np.isfinite(cap_at_obs))

# sensitivity of ln(capacity) to each calibration line (refit, 5 eq/5 unknowns)
def cap_of(shift_vec):
    pp, err = fit5(CAL + shift_vec, P)
    assert err < 1e-9, err
    d = delta_of(pp)
    return abs(old_conv_f06(pp, 0.0, **CUT) - old_conv_f06(pp, 0.5 * (1 - d), **CUT)) * 1000


cap_ref = cap_of(np.zeros(5))
names = ['f01', 'f02', 'fres1', 'fres2', 'fres3']
h = 2e-6
deriv = []   # d ln(cap) / d kHz
for i in range(5):
    e = np.zeros(5)
    e[i] = h
    deriv.append((np.log(cap_of(e)) - np.log(cap_of(-e))) / (2 * h * 1e6))
deriv = np.array(deriv)
chk('7d capacity sensitivity d ln(cap)/d(kHz): ' + ', '.join('%s %+.4f' % (n_, d_) for n_, d_ in zip(names, deriv)) + '  (note: fres3 +-1 kHz moves f06/6 by .123 MHz)',
    abs(deriv[3]) > 0.02 and abs(deriv[2]) > 0.01 and abs(deriv[4]) > 0.01)
common = deriv[2] + deriv[3] + deriv[4]
chk('7e common-mode cavity shift (fres1,2,3 all +1 kHz, i.e. a bare-cavity shift) leaves the capacity unchanged: sum of the three sensitivities |%.1e| << each' % common,
    abs(common) < 0.01 * abs(deriv[3]), 'sum=%.2e vs fres2 %.4f' % (common, deriv[3]))
# thresholds: single-line shifts that bring the capacity down to the digitized separation (centre) and to the bin upper edge
SEP = 2.3219000228159175
BIN_LO, BIN_HI = 1.9902000195564913, 2.6536000260753454
thr = {}
for tgt_name, tgt in (('sep', SEP), ('binhi', BIN_HI)):
    for i in (2, 3, 4):
        est = np.log(tgt / cap_ref) / (deriv[i] * 1e-6 if False else deriv[i])      # kHz, linear estimate
        def g(kHz, i=i):
            e = np.zeros(5)
            e[i] = kHz * 1e-6
            return cap_of(e) - tgt
        lo, hi = 0.0, est * 1.6
        gl, gh = g(lo), g(hi)
        k = 0
        while gl * gh > 0 and k < 4:
            hi *= 1.5
            gh = g(hi)
            k += 1
        thr[(tgt_name, i)] = brentq(g, lo, hi, xtol=1e-3) if gl * gh < 0 else float('nan')
msg = '; '.join('%s: %s %+.1f kHz' % (tn, names[i], v) for (tn, i), v in thr.items())
chk('7f single calibration-line shifts that bring the capacity down to the digitized separation (2.322 MHz) / bin upper edge (2.654 MHz): ' + msg,
    all(np.isfinite(v) for v in thr.values()) and abs(thr[('sep', 3)]) < 20, 'compare printed half-unit 5 kHz')
D2 = (CAL[2] - 2 * CAL[3] + CAL[4]) * 1e6
chk('7g the capacity is set by a %.0f kHz second difference of the three cavity lines (fres1-2 fres2+fres3); sep-threshold in fres2 is %.1f%% of it per line'
    % (D2, abs(thr[('sep', 3)]) * 2 / D2 * 100), D2 > 100, 'D2=%.0f kHz' % D2)
chk('7h physical-vs-legacy charge convention changes the capacity by %.1e relative = a fres2 shift of %.4f kHz, versus the 5 kHz printed half-unit: convention is not load-bearing for the envelope'
    % (REL_CONV, REL_CONV / abs(deriv[3])), REL_CONV / abs(deriv[3]) < 0.05)

# ----------------------------------------------------------------------------
# 8  digitized separation, window choice, sign ambiguity, time selection
# ----------------------------------------------------------------------------
def pk(row):
    low = max((r for r in row if 8 <= r[0] <= 9.8), key=lambda r: r[1])
    hig = max((r for r in row if 10 <= r[0] <= 12), key=lambda r: r[1])
    return low, hig
seps = {}
for tmin, row in ROW.items():
    lo_, hi_ = pk(row)
    seps[tmin] = hi_[0] - lo_[0]
chk('8a digitized bin-centre separation at 40 and 120 min = %.4f MHz (both rows give the same two bins); geometric range +-bin height = [%.4f, %.4f]' % (SEP, SEP - BIN_H, SEP + BIN_H),
    abs(seps[40] - SEP) < 1e-9 and abs(seps[120] - SEP) < 1e-9 and abs((SEP - BIN_H) - BIN_LO) < 1e-6 and abs((SEP + BIN_H) - BIN_HI) < 1e-6)
second = sorted((r for r in ROW[120] if 10 <= r[0] <= 12), key=lambda r: -r[1])[:2]
gap120 = second[0][1] - second[1][1]
alt = second[1][0] - pk(ROW[120])[0][0]
chk('8b at 120 min the high-window winner (11.11 MHz, 0.467) beats 10.78 MHz (0.439) by only %.3f contrast; choosing the runner-up gives separation %.3f MHz (one bin lower, still inside the stated range)' % (gap120, alt),
    gap120 < 0.05 and BIN_LO - 1e-6 <= alt <= BIN_HI)
tri = 8.789262 + 11.111162
chk('8c opposite-sign detunings would need splitting = sum of the two |detunings| = %.3f MHz (reverse triangle inequality gives |d_a-d_b| = |d_a|+|d_b|) > every computed capacity %.3f / %.3f (and corner max %.3f): in this model same sign is forced'
    % (tri, S0, S0c, hi_a), tri > hi_a)
auth_sep = {t_: v[1] - v[0] for t_, v in AUTHOR.items()}
mn, mx_ = min(auth_sep.values()), max(auth_sep.values())
top2 = sorted(auth_sep, key=lambda t_: -auth_sep[t_])[:2]
chk('8d author pixel peaks at all six times: separations %s; the two slices selected after the fact (%s) are the two largest' % (
    {k: round(v, 3) for k, v in auth_sep.items()}, sorted(top2)), sorted(top2) == [40, 120])
chk('8e cosine exclusion is NOT selection-dependent: the smallest separation over all six times minus a bin height (%.3f MHz) exceeds the cosine capacity %.3f and its corner max %.3f' % (mn - BIN_H, S0c, hi_c),
    mn - BIN_H > hi_c)
chk('8f nominal assertion reproduced: cosine capacity %.3f < bin lower edge %.3f; Andreev capacity %.3f > bin upper edge %.3f' % (S0c, BIN_LO, S0, BIN_HI), S0c < BIN_LO and S0 > BIN_HI)
top_edge = max(auth_sep.values()) + BIN_H
chk('8g FINDING: the lowest Andreev rounding corner (%.3f MHz) lies BELOW the bin upper edge %.3f (and the author-profile edge %.3f); at that corner the capacity covers only separations <= %.3f'
    % (lo_a, BIN_HI, top_edge, lo_a), lo_a < BIN_HI and lo_a < top_edge and lo_a > SEP)

# ----------------------------------------------------------------------------
# 9  which offsets are compatible (nothing is predicted)
# ----------------------------------------------------------------------------
th = np.linspace(0, 0.25, 20001)
cs = np.zeros_like(th)
for k, ak in odd_series(c128, 15).items():
    cs += 2 * ak * np.cos(2 * np.pi * k * th) * 1000
cs = np.abs(cs)
chk('9a s(q) strictly decreasing on [0,1/4] (20001-point Fourier evaluation)', np.all(np.diff(cs) < 0))
def qstar(target, cap):
    return float(np.arccos(target / cap) / (2 * np.pi))
qn = [np.interp(-v, -cs, th) for v in (SEP, BIN_LO, BIN_HI)]
chk('9b offsets compatible with the digitized range at nominal parameters: q in [%.4f, %.4f] (centre %.4f) or its images q->-q, q+1/2; width %.3f of a 2e period; single-cos approximation agrees to < 2e-4'
    % (qn[2], qn[1], qn[0], qn[1] - qn[2]), abs(qn[0] - qstar(SEP, S0)) < 2e-4)
qlo = [qstar(SEP, c) for c in cap_a]
chk('9c over the 32 rounding corners the centre-compatible offset ranges over [%.4f, %.4f]: the (unknown) offset is not constrained by this comparison' % (min(qlo), max(qlo)), max(qlo) - min(qlo) > 0.01)

# ----------------------------------------------------------------------------
n_fail = RES.count(False)
print('TOTAL: PASS=%d FAIL=%d' % (RES.count(True), n_fail))
print('runtime %.1f s' % (time.time() - T0))
if n_fail == 0:
    print('HIT: scoped new result (same-family, unrefereed). (i) The offset envelope is an exact odd-harmonic Fourier structure: s(q)=2|sum_odd a_k cos 2 pi k q|, zero at q=1/4 for every model of this form, '
          'strictly decreasing on [0,1/4] with certificate ratio %.0e, so the capacity is the q=0 endpoint (%.6f MHz) and the four-interval extremum search is redundant. '
          '(ii) The capacity is exponentially conditioned on a %.0f kHz second difference of the cavity lines: a single-line shift of %.1f kHz (fres2) / %.1f kHz (fres3) / %.1f kHz (fres1) takes it to the digitized %.2f MHz separation, '
          'versus 5 kHz printed half-units, and the lowest printed-rounding corner (%.3f MHz) already sits below the bin upper edge %.3f MHz. '
          '(iii) The physical-offset gauge correction changes the capacity by %.1e relative (%.0f Hz), i.e. a %.4f kHz cavity-line shift, orders below those.' % (
              cert, S0, D2, abs(thr[('sep', 3)]), abs(thr[('sep', 4)]), abs(thr[('sep', 2)]), SEP, lo_a, BIN_HI, REL_CONV, abs(dA), REL_CONV / abs(deriv[3])))
print('SUMMARY: independent recomputation confirms the note\'s capacity numbers (cos %.3f, Andreev %.3f MHz) and shows they equal the q=0 endpoint splitting with only odd harmonics in q, '
      'while the capacity is set by a ~%.0f kHz cavity second difference so ~%.0f kHz of cross-acquisition drift in one cavity line erases the margin over the digitized %.2f MHz separation.' % (S0c, S0, D2, abs(thr[('sep', 3)]), SEP))
sys.exit(0 if n_fail == 0 else 1)
