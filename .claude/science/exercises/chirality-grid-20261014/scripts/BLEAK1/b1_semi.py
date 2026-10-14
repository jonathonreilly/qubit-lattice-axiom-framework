"""BLEAK-1 semi-analytic route: exact k4 integration, 3D midpoint + Richardson, and the closed form I_1 - I_4 = -1/96.

Hand formulas (derived in REPORT.md sec. 4; U^a from b1_core.U_alpha; x = shat_4^2, Q = qhat^2):
  W_inst(U^4,U^4) = [5/8 sin^2 k4 + 1/8 c4^2 Q]/Q
  W_inst(U^a,U^a) = [-3/8 sin^2 ka + 1/2 x c_a^2 - 3/8 x c_a^2 shat_a^2/Q]/Q     (a spatial)
  W_TT(U^a,U^a) = 0 for every a (U^a's spatial block = scalar*1 + longitudinal)
k4 averages: <1/(Q+x)> = R = 1/sqrt(Q(Q+4)), <x/(Q+x)> = 1 - Q R, <x^2/(Q+x)> = 2 - Q + Q^2 R.
Cubic-symmetrized difference: d(q) = <f_1>_sym - <f_4> = 1/(16Q) + tau/(32 Q^2) - 1/6 + Q R/6, tau = sum_i shat_i^4.
Identities: int Q R = 3/4 (W(B4): int shat_4^2/shat^2 = 1/4);  int tau/Q^2 = 1 - 2 W3 (integration by parts of
d_i(sin q_i/Q));  W3 = int d^3q/(2pi)^3 1/Q = Watson/2.  Hence I_1 - I_4 = -1/24 + W3/16 + (1-2W3)/32 = -1/96.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from b1_core import shat, chalf, U_alpha, kernel_parts, midpoint_axis

rng = np.random.default_rng(7)
print("== (1) hand formulas vs general kernel code, 2000 random k ==")
k = rng.uniform(-np.pi, np.pi, (4, 2000)); s = shat(k); c = chalf(k)
Q = np.sum(s[:3] ** 2, 0); x = s[3] ** 2
U4 = U_alpha(k, 3); TT4, I4, _ = kernel_parts(U4, U4, k)
h4 = (5 / 8 * np.sin(k[3]) ** 2 + 1 / 8 * c[3] ** 2 * Q) / Q
U1 = U_alpha(k, 0); TT1, I1, _ = kernel_parts(U1, U1, k)
h1 = (-3 / 8 * np.sin(k[0]) ** 2 + 0.5 * x * c[0] ** 2 - 3 / 8 * x * c[0] ** 2 * s[0] ** 2 / Q) / Q
print("  max|W_inst(U4)-hand| = %.1e ; max|W_inst(U1)-hand| = %.1e ; max|W_TT(U4)|, |W_TT(U1)| = %.1e, %.1e" % (
    np.abs(I4 - h4).max(), np.abs(I1 - h1).max(), np.abs(TT4).max(), np.abs(TT1).max()))

print("\n== (2) k4 average checked against brute force at 5 random q (2^16-point k4 midpoint) ==")
k4 = midpoint_axis(1 << 16, -np.pi, np.pi); xx = shat(k4) ** 2
for j in range(5):
    q = rng.uniform(-np.pi, np.pi, 3); sq = shat(q); Qv = np.sum(sq ** 2); cq = chalf(q)
    R = 1 / np.sqrt(Qv * (Qv + 4))
    bf4 = np.mean((5 / 8 * np.sin(k4) ** 2 + 1 / 8 * np.cos(k4 / 2) ** 2 * Qv) / (Qv * (Qv + xx)))
    an4 = (5 / 16 - 0.5 * Qv * R + Qv / 8 - Qv ** 2 * R / 8) / Qv
    bf1 = np.mean((-3 / 8 * np.sin(q[0]) ** 2 + 0.5 * xx * cq[0] ** 2 - 3 / 8 * xx * cq[0] ** 2 * sq[0] ** 2 / Qv) / (Qv * (Qv + xx)))
    an1 = (-3 / 8 * np.sin(q[0]) ** 2 * R + cq[0] ** 2 * (0.5 - 3 / 8 * sq[0] ** 2 / Qv) * (1 - Qv * R)) / Qv
    print("  q=%s  <f4>: bf %.12f an %.12f | <f1>: bf %.12f an %.12f" % (np.round(q, 3), bf4, an4, bf1, an1))

def grid3(M, chunk=1 << 15):
    ax = midpoint_axis(M)
    for i in range(M):
        A2, A3 = np.meshgrid(ax, ax, indexing='ij')
        qq = np.stack([np.full(A2.size, ax[i]), A2.ravel(), A3.ravel()])
        for a in range(0, qq.shape[1], chunk):
            yield qq[:, a:a + chunk]

def integ3(M):
    acc = np.zeros(7); n = 0
    for q in grid3(M):
        sq = shat(q); cq = chalf(q); Qv = np.sum(sq ** 2, 0); R = 1 / np.sqrt(Qv * (Qv + 4)); tau = np.sum(sq ** 4, 0)
        f4 = (5 / 16 - 0.5 * Qv * R + Qv / 8 - Qv ** 2 * R / 8) / Qv
        f1 = (-3 / 8 * np.sin(q[0]) ** 2 * R + cq[0] ** 2 * (0.5 - 3 / 8 * sq[0] ** 2 / Qv) * (1 - Qv * R)) / Qv
        d = 1 / (16 * Qv) + tau / (32 * Qv ** 2) - 1 / 6 + Qv * R / 6
        acc += [f1.sum(), f4.sum(), d.sum(), (1 / Qv).sum(), (Qv * R).sum(), (tau / Qv ** 2).sum(), (f1 - f4).sum()]
        n += q.shape[1]
    return acc / n

print("\n== (3) 3D midpoint on [0,pi]^3 (M points per axis = N/2), exact k4 average ==")
print("   M      I_1(inst)        I_4(inst)        int d (sym)      int f1-f4        W3=int 1/Q       int QR           int tau/Q^2")
res = []
for M in (16, 32, 64, 128, 256):
    r = integ3(M); res.append((M, r))
    print("  %4d  %.12f  %.12f  %.12f  %.12f  %.12f  %.12f  %.12f" % (M, r[0], r[1], r[2], r[6], r[3], r[4], r[5]), flush=True)
Ms = np.array([m for m, _ in res], float); R_ = np.array([r for _, r in res])
print("\n== (4) Richardson: fit c0 + c1/M + c2/M^2 + c3/M^3 to the four largest grids ==")
names = ['I_1', 'I_4', 'int d', 'int f1-f4', 'W3', 'int QR', 'int tau/Q^2']
cols = [0, 1, 2, 6, 3, 4, 5]
for nm, ci in zip(names, cols):
    A = np.vstack([np.ones(4), 1 / Ms[-4:], 1 / Ms[-4:] ** 2, 1 / Ms[-4:] ** 3]).T
    c0 = np.linalg.solve(A, R_[-4:, ci])[0]
    A3 = np.vstack([np.ones(3), 1 / Ms[-3:], 1 / Ms[-3:] ** 2]).T
    c0b = np.linalg.solve(A3, R_[-3:, ci])[0]
    print("  %-12s extrapolated %.10f   (3-pt %.10f)" % (nm, c0, c0b))
W3 = 0.505462019717326 / 2
print("\n  exact targets: W3 = Watson/2 = %.12f ; int QR = 0.75 ; int tau/Q^2 = 1-2W3 = %.12f ; I_1-I_4 = -1/96 = %.12f" % (W3, 1 - 2 * W3, -1 / 96))
print("  I_4 exact: int <f4> = 5/16 W3 - 1/2*3/4 + 1/8 - 1/8 int Q R ... see report; numeric above")
print("  delta c = -16 pi (I_1 - I_4) G/a^2 = (pi/6) G/a^2 = %.10f (l_P/a)^2" % (np.pi / 6))
