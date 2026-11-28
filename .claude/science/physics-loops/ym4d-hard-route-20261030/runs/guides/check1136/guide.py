"""GUIDE numerics for the check of gap-council-op-astra.md (row 1136).
Standard library only. Nothing here is a proof step."""
import math
import random

def besseli(n, x, terms=80):
    # I_n(x) = sum_k (x/2)^(n+2k) / (k! (n+k)!), terms built by recursion
    h = x / 2.0
    t = math.exp(n * math.log(h) - math.lgamma(n + 1)) if h > 0 else (1.0 if n == 0 else 0.0)
    s = 0.0
    for k in range(terms):
        s += t
        t *= h * h / ((k + 1) * (n + k + 1))
    return s

def a(d, beta):
    return besseli(d, beta) / besseli(1, beta)

print("== a_2 on the window [2.3, 2.6] ==")
for beta in (2.3, 2.45, 2.6):
    a2 = a(2, beta)
    r32 = besseli(3, beta) / besseli(2, beta)
    print(f"beta={beta}: a2={a2:.6f} (>0.4: {a2 > 0.4}); 1/(4/b+I3/I2)={1/(4/beta + r32):.6f};"
          f" I3/I2={r32:.4f} <= b/6={beta/6:.4f}: {r32 <= beta/6}; a2^4={a2**4:.6f} > 1/256={1/256:.6f}")

print("== a_d <= (13/20)^(d-1) for beta in (0, 2.6], d = 2..40 (grid) ==")
worst = 0.0
for i in range(1, 261):
    beta = i / 100.0
    for d in range(2, 41):
        ratio = a(d, beta) / (0.65 ** (d - 1))
        worst = max(worst, ratio)
print(f"max of a_d / (13/20)^(d-1) on the grid: {worst:.6f} (<= 1 expected)")

print("== twelve-step sum ==")
for beta in (2.3, 2.6):
    s = sum(d ** 4 * a(d, beta) ** 12 for d in range(2, 60))
    print(f"beta={beta}: sum_d d^4 a_d^12 = {s:.3e}  vs 16/65 = {16/65:.4f}")
print(f"(13/20)^12 = {0.65**12:.6e}, 1/81 = {1/81:.6e}; 16*(13/20)^12 = {16*0.65**12:.4f} <= 16/81 = {16/81:.4f}")

_acache = {}
def deconv_min(beta, k, nth=2000):
    # min over theta of (1 - Delta) h_beta^{*k} = sum_d d^3 a_d^k chi_d(theta)
    if beta not in _acache:
        _acache[beta] = [None] + [a(d, beta) for d in range(1, 60)]
    ad = _acache[beta]
    coef = [d ** 3 * ad[d] ** k for d in range(1, 60)]
    best = float("inf")
    for i in range(1, nth):
        th = math.pi * i / nth
        st = math.sin(th)
        s = 0.0
        for idx, d in enumerate(range(1, 60)):
            s += coef[idx] * math.sin(d * th) / st
        best = min(best, s)
    # endpoints theta -> 0 and theta -> pi by the limits chi_d(I) = d, chi_d(-I) = (-1)^(d-1) d
    s0 = sum(coef[idx] * d for idx, d in enumerate(range(1, 60)))
    spi = sum(coef[idx] * d * (-1) ** (d - 1) for idx, d in enumerate(range(1, 60)))
    return min(best, s0, spi)

print("== smallest k with (1 - Delta) h^{*k} >= 0 (single link; GUIDE, not claimed in the note) ==")
for beta in (2.3, 2.6):
    for k in range(1, 13):
        m = deconv_min(beta, k, nth=600)
        if m > 0:
            print(f"beta={beta}: first k with positive single-link deconvolution: {k} (min {m:.4f})")
            break
    print(f"beta={beta}: k=12 min = {deconv_min(beta, 12, nth=600):.6f}")

print("== one-step bracket 1 + 3 b x - b^2 (1 - x^2) ==")
for beta in (0.2, 1/3, 0.34, 2.3):
    mn = min(1 + 3 * beta * x - beta ** 2 * (1 - x * x) for x in [-1 + 2 * i / 10000 for i in range(10001)])
    print(f"beta={beta:.4f}: min over [-1,1] = {mn:.5f}; value at -1 = {1 - 3*beta:.5f}")

print("== commutator law: Monte Carlo E chi_j([a,b]) vs 1/d, and density normalization ==")
random.seed(1136)
def rand_quat():
    v = [random.gauss(0, 1) for _ in range(4)]
    n = math.sqrt(sum(t * t for t in v))
    return [t / n for t in v]
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return [a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2]
def qinv(p):
    return [p[0], -p[1], -p[2], -p[3]]
M = 200000
acc = {d: 0.0 for d in (2, 3, 4, 5)}
for _ in range(M):
    x1 = rand_quat(); y1 = rand_quat()
    c = qmul(qmul(x1, y1), qmul(qinv(x1), qinv(y1)))
    th = math.acos(max(-1.0, min(1.0, c[0])))
    st = math.sin(th)
    for d in acc:
        acc[d] += (math.sin(d * th) / st) if st > 1e-12 else d
for d in acc:
    print(f"d={d}: MC E chi = {acc[d]/M:.4f}  vs 1/d = {1/d:.4f}")
# normalization of w(theta) = (pi - theta)/(2 sin theta) against Haar (2/pi) sin^2 theta dtheta
n = 200000
s = 0.0
for i in range(n):
    th = math.pi * (i + 0.5) / n
    s += (math.pi - th) / (2 * math.sin(th)) * (2 / math.pi) * math.sin(th) ** 2 * (math.pi / n)
print(f"integral of commutator density against Haar = {s:.6f} (1 expected)")

print("== (1 - Delta_e) M at U_e = -I, other links I: M = exp(2 beta x) in x = tr(U_e)/2 ==")
for beta in (0.1, 1/6, 0.2, 2.3):
    x = -1.0
    c = 2 * beta
    lap = (1 - x * x) * c * c - 3 * x * c   # Delta e^{cx} / e^{cx}
    print(f"beta={beta:.4f}: (1 - Delta)M / M = {1 - lap:.5f}, 1 - 6 beta = {1 - 6*beta:.5f}")
# finite-difference Laplacian on S^3 at -I along a geodesic sphere (radial function): check formula
beta = 0.5
f = lambda th: math.exp(2 * beta * math.cos(th))
h = 1e-3
th0 = math.pi - 0.3
fd = (f(th0 + h) - 2 * f(th0) + f(th0 - h)) / h ** 2 + 2 / math.tan(th0) * (f(th0 + h) - f(th0 - h)) / (2 * h)
x = math.cos(th0); c = 2 * beta
formula = ((1 - x * x) * c * c - 3 * x * c) * f(th0)
print(f"radial Laplacian check at theta={th0:.3f}: finite difference {fd:.6f} vs formula {formula:.6f}")

print("== Chebyshev numbers for the disjoint-plaquette bound at beta = 2.3, eta = 0.99 ==")
a2 = a(2, 2.3)
b = 0.99 * a2 ** 4 - 4 ** -4
for N in (10 ** 4, 10 ** 6):
    eN = 4 / (N * b * b)
    print(f"N={N}: b={b:.5f}, e_N={eN:.4e}, p <= {eN/(1-eN):.4e}")
