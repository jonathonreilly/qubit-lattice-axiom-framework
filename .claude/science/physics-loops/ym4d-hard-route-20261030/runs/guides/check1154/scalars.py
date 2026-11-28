# GUIDE only (pure Python). Scalar identities and constants used in row 1153.
import math

def f(x):
    return math.log((1 + math.exp(-x)) / (1 - math.exp(-x)))

# 1. int_{R^3} f(|u|) du = pi^5/6, and 6/(2pi)^3 * that = pi^2/8
def radial_integral(N=200000, R=60.0):
    # Simpson on [0, R] of r^2 f(r); integrand -> 0 at r=0
    h = R / N
    s = 0.0
    for i in range(N + 1):
        r = i * h
        v = 0.0 if r == 0 else r * r * f(r)
        w = 1 if i in (0, N) else (4 if i % 2 else 2)
        s += w * v
    return s * h / 3

I = 4 * math.pi * radial_integral()
print("int f(|u|) d^3u =", I, " pi^5/6 =", math.pi**5 / 6)
print("6/(2pi)^3 * int =", 6 / (2 * math.pi)**3 * I, " pi^2/8 =", math.pi**2 / 8)
odd = sum(1.0 / h**4 for h in range(1, 200001, 2))
print("sum_odd h^-4 =", odd, " pi^4/96 =", math.pi**4 / 96)
# 2. second limit factor
ser = sum(2.0**(-k - 1) * 2.0**(-3 * k) for k in range(60))
print("sum 2^{-k-1} 2^{-3k} =", ser, " 8/15 =", 8 / 15)
# 3. counting constant (8)
c = math.pi**2 / 15
for x in (0.3, 1.0, 5.0):
    best = min(t * x + c / t**3 for t in [0.001 * k for k in range(1, 20000)])
    print("x=", x, " min_t(tx + c t^-3) =", best, " 4(c/27)^(1/4) x^(3/4) =", 4 * (c / 27)**0.25 * x**0.75)
# 4. ray recursion
cc = 0.0
for k in range(2):
    cc = (1 + cc) / (5 + 4 * cc)
print("two-step ray coefficient =", cc, " 6/29 =", 6 / 29, " 4*that =", 4 * cc, " 24/29 =", 24 / 29)
# 5. G_infinity by the midpoint rule (smooth periodic integrand)
M = 800
s = 0.0
for i in range(M):
    p1 = -math.pi + (i + 0.5) * 2 * math.pi / M
    c1 = math.cos(p1)
    for j in range(M):
        p2 = -math.pi + (j + 0.5) * 2 * math.pi / M
        s += 1.0 / (1 + (4 - 2 * c1 - 2 * math.cos(p2)) / 4)
G = s / (M * M)
eta = 1 / G - 1
print("G_inf =", G, " eta_inf =", eta, " (3/16)(1-G) =", 3 / 16 * (1 - G), " 9/106 =", 9 / 106, " 3/32 =", 3 / 32)
