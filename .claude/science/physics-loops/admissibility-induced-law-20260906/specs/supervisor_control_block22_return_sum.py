"""Control, block 22 (supervisor): the strong-coupling threshold of block 19 sharpened.
3 G(0) = 3 (2pi)^{-3} int d^3k / E(k) = (1/2) sum_{n>=0} P_{2n}(0,0), P_{2n}(0,0) the return probability of the simple random walk on Z^3:
P_{2n} = 6^{-2n} C(2n, n) T_n, T_n = sum_{a+b+c=n} (n!/(a! b! c!))^2 = sum_a C(n,a)^2 C(2(n-a), n-a).
(1) exact partial sums S_N = sum_{n<=N} P_{2n} for N = 250, 500, 1000, 2000 (timing); float value vs the Watson constant 1.516386...;
(2) the tail bound: 1 - cos u >= u^2/2 - u^4/24 >= 11 u^2/24 on |u| <= 1 (g(u) = 1 - u^2/2 + u^4/24 - cos u >= 0 via g'' >= 0), and
    1 - cos u >= 2/pi^2 on 1 <= |u| <= pi; so 1 - phi(k) >= (11/72)|k|^2 on |k|_inf <= 1 and >= 2/(3 pi^2) elsewhere in the cube;
    phi^{2n} <= e^{-2n(1 - |phi|)} with 1 - |phi(k)| = min(1 - phi(k), 1 - phi(k - (pi,pi,pi))) => P_{2n} <= 2 (2pi)^{-3} (36 pi/(11 n))^{3/2} + 2 e^{-4n/(3 pi^2)};
    sum_{n>N} n^{-3/2} <= 2/sqrt(N); tail T(N) = (1/(2 pi^3)) (36 pi/11)^{3/2} / sqrt(N) + 2 e^{-4(N+1)/(3 pi^2)}/(1 - e^{-4/(3 pi^2)});
(3) the certificate: 3 G(0) <= (S_N + T(N))/2 < 77/100 ? and compare with the crude 3 sqrt(3) pi/8 = 2.04; exact form of the comparison
    (rational S_N; T(N)^2 rational up to pi: use pi <= 22/7 in the constant and check (S_N + T)/2 < 77/100 with an exact rational upper bound for T)."""
import math, time
from fractions import Fraction as F
from math import comb
def T_n(n):
    return sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))
def partial(N):
    # common denominator 6^{2N}: S_N * 6^{2N} = sum_n C(2n,n) T_n 6^{2(N-n)}
    num = 0
    for n in range(N + 1):
        num += comb(2 * n, n) * T_n(n) * 6 ** (2 * (N - n))
    return F(num, 6 ** (2 * N))
for N in (250, 500, 1000, 2000):
    t0 = time.time(); S = partial(N); dt = time.time() - t0
    print(f"(1) N={N}: S_N = {float(S):.9f} (denominator digits {len(str(S.denominator))}) in {dt:.1f}s")
print("(1) Watson constant W = 1.516386059151978...; S_N approaches it from below")
# (2) tail bound
c_tail = (1 / (2 * math.pi ** 3)) * (36 * math.pi / 11) ** 1.5
print(f"(2) tail constant (1/(2 pi^3))(36 pi/11)^{{3/2}} = {c_tail:.6f}; crude constant (1/2)(3 pi/4)^{{3/2}} = {0.5*(3*math.pi/4)**1.5:.6f}")
# check P_{2n} <= 2(2pi)^{-3}(36 pi/(11n))^{3/2} + 2 e^{-4n/(3pi^2)} numerically for n <= 2000
ok = True
for n in range(1, 2001):
    P = comb(2 * n, n) * T_n(n) / 6 ** (2 * n) if n <= 60 else None
    if P is None: break
    bound = 2 / (2 * math.pi) ** 3 * (36 * math.pi / (11 * n)) ** 1.5 + 2 * math.exp(-4 * n / (3 * math.pi ** 2))
    ok = ok and P <= bound
print("(2) P_{2n} <= the bound for n <= 60 (exact P as float):", ok)
g_ok = all(1 - math.cos(u) >= u * u / 2 - u ** 4 / 24 - 1e-15 for u in [i / 1000 for i in range(-3142, 3143)])
print("(2) 1 - cos u >= u^2/2 - u^4/24 on [-pi, pi] (sampled):", g_ok, "; 11/24 =", 11 / 24)
for N in (1000, 2000):
    T = c_tail / math.sqrt(N) + 2 * math.exp(-4 * (N + 1) / (3 * math.pi ** 2)) / (1 - math.exp(-4 / (3 * math.pi ** 2)))
    S = float(partial(N))
    print(f"(3) N={N}: tail T(N) = {T:.6f}; 3G(0) <= (S_N + T)/2 = {(S + T)/2:.6f}  (true 3G(0) = {1.516386059151978/2:.6f}); crude threshold 3 sqrt(3) pi/8 = {3*math.sqrt(3)*math.pi/8:.4f}")
# exact rational upper bound for T(2000) with pi <= 22/7 (36 pi/11)^{3/2}/(2 pi^3) = (36/11)^{3/2} pi^{-3/2}/2 <= (36/11)^{3/2} (3)^{-3/2}/2 using pi >= 3
# T^2 <= (36/11)^3 / (4 * 27 * N) ; plus the exponential term bounded by 2 e^{-4(N+1)/(3 pi^2)}/(1-e^{-4/(3pi^2)}) <= 2 e^{-4(N+1)/30}/(1 - e^{-4/30}) with pi^2 <= 10
N = 2000
S = partial(N)
T1sq = F(36, 11) ** 3 / (4 * 27 * N)
print(f"(3) exact: T1(N)^2 <= (36/11)^3/(108 N) = {float(T1sq):.3e} -> T1 <= {math.sqrt(float(T1sq)):.6f} (pi >= 3 used); exponential term at N = 2000 is below 1e-100")
target = F(77, 100)
ok_exact = (2 * target - S) > 0 and T1sq < (2 * target - S - F(1, 10**40)) ** 2
print(f"(3) exact comparison (S_N + T1)/2 < 77/100 with the exponential term absorbed in 1e-40: {ok_exact}; 2*77/100 - S_N = {float(2*target - S):.6f} vs T1 <= {math.sqrt(float(T1sq)):.6f}")
