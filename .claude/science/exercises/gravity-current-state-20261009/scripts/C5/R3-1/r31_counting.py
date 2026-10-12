"""R3-1 check 2: norm-shell counting on L7 and convergence of Poincare-type orbit sums.

x = (sqrt7 n0, n1, n2, n3), x^2 = Q7(n) = -7 n0^2 + |n|^2 = N, |x|_E^2 = 7 n0^2 + |n|^2 = 14 n0^2 + N.
Shell S_N = {n in Z^4 : Q7(n) = N} is a finite union of Gamma_L-orbits (finiteness of classes).
N_N(T) = #{x in S_N : |x|_E <= T} = sum_{n0: 14 n0^2 + N <= T^2} r3(7 n0^2 + N).
Prediction (H^3 / dS_3 lattice-point counting, critical exponent delta = 2): N_N(T) ~ c_N T^2.
Poincare series P_s(N) = sum_{x in S_N} |x|_E^{-s} converges iff s > 2.
r3 computed exactly by FFT convolution of the theta series (rounded integers, verified on small m).
"""
import numpy as np

M = 2**23  # r3 up to M
sq = np.zeros(M, dtype=float)
k = 0
while k * k < M:
    sq[k * k] += 1 if k == 0 else 2
    k += 1
L = 1 << (int(np.ceil(np.log2(3 * M))))
f = np.fft.rfft(sq, L)
r3 = np.rint(np.fft.irfft(f ** 3, L)[:M]).astype(np.int64)
# verify small values by brute force
bf = np.zeros(200, dtype=int)
for a in range(-15, 16):
    for b in range(-15, 16):
        for c in range(-15, 16):
            s = a * a + b * b + c * c
            if s < 200: bf[s] += 1
assert (bf == r3[:200]).all(), "r3 FFT mismatch"
print("r3 via FFT verified for m<200; r3 computed to", M)
# Legendre check: no representation of 7 n0^2 for n0 != 0 (anisotropy of Q7)
bad = [n0 for n0 in range(1, int(np.sqrt(M / 7))) if r3[7 * n0 * n0] != 0]
print("anisotropy: #{n0 <= %d : r3(7 n0^2) > 0} =" % int(np.sqrt(M / 7)), len(bad))

def shell_counts(N, Tmax):
    n0max = int(np.sqrt((Tmax ** 2 - N) / 14.0))
    n0 = np.arange(-n0max, n0max + 1)
    m = 7 * n0 * n0 + N
    ok = (m >= 0) & (m < M)
    assert ok[m >= 0].all(), "increase M"
    cnt = np.where(m >= 0, r3[np.clip(m, 0, M - 1)], 0)
    E2 = 14.0 * n0 * n0 + N
    return E2[cnt > 0], cnt[cnt > 0]

Tmax = float(np.sqrt(2 * (M - 1) - 50))
print(f"Tmax = {Tmax:.1f}")
for N in [-7, -6, -3, -1, 1, 2, 3, 7]:
    E2, cnt = shell_counts(N, Tmax)
    if len(E2) == 0:
        print(f"N={N:3d}: empty shell"); continue
    Ts = np.array([Tmax / 64, Tmax / 16, Tmax / 4, Tmax])
    NT = np.array([cnt[E2 <= T * T].sum() for T in Ts])
    slopes = np.diff(np.log(NT)) / np.diff(np.log(Ts))
    c = NT[-1] / Tmax ** 2
    kind = "timelike" if N < 0 else "spacelike"
    print(f"N={N:3d} ({kind}): N(T) at T/64,T/16,T/4,T = {NT.tolist()}, log-slopes {np.round(slopes,4).tolist()}, N(T)/T^2 = {c:.5f}")
    for s in [1.5, 2.0, 2.5, 3.0, 4.0]:
        part = [float((cnt[E2 <= T * T] * E2[E2 <= T * T] ** (-s / 2)).sum()) for T in Ts]
        print(f"      s={s}: partial sums sum |x|_E^-s up to T/64..T: {np.round(part, 6).tolist()}")
