# GUIDE-only numerics: Watson's integral W_3 and finite-torus analogues.
import math, itertools
# Closed form (Watson 1939; Glasser-Zucker 1977): W_3 = sqrt(6)/(32 pi^3) * G(1/24) G(5/24) G(7/24) G(11/24)
g = math.gamma
W3 = math.sqrt(6)/(32*math.pi**3) * g(1/24)*g(5/24)*g(7/24)*g(11/24)
print("W3 closed form =", W3, " threshold n W3/2 for n=4:", 4*W3/2, " n=2:", 2*W3/2)
# Bessel representation check: W3 = int_0^inf (e^{-t} I0(t))^3 dt, I0 by series / asymptotic
def i0e(t):
    if t < 30:
        s, term, k = 1.0, 1.0, 0
        while True:
            k += 1
            term *= (t/2)**2/(k*k)
            s += term
            if term < 1e-17*s: break
        return s*math.exp(-t)
    # asymptotic expansion
    s, term = 1.0, 1.0
    for k in range(1, 12):
        term *= (2*k-1)**2/(8*t*k)
        s += term
    return s/math.sqrt(2*math.pi*t)
# integrate on [0, T] by Simpson in log-spaced pieces, tail analytically ~ (2 pi t)^{-3/2}
def simpson(f, a, b, n):
    h = (b-a)/n; s = f(a)+f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2)*f(a+i*h)
    return s*h/3
f = lambda t: i0e(t)**3
edges = [0, 1, 4, 16, 64, 256, 1024, 4096, 16384]
tot = sum(simpson(f, edges[i], edges[i+1], 2000) for i in range(len(edges)-1))
T = edges[-1]
tail = 2*(2*math.pi)**-1.5 * T**-0.5   # int_T^inf (2 pi t)^{-3/2} dt
print("W3 Bessel integral ~", tot+tail)
# finite torus sums (1/|L|) sum_{p != 0} 1/E_p on Z_L^3, and (n/2) times it for n = 4
for L in (4, 6, 8, 16, 32):
    s = 0.0
    for k in itertools.product(range(L), repeat=3):
        if k == (0, 0, 0): continue
        E = sum(1 - math.cos(2*math.pi*kj/L) for kj in k)
        s += 1/E
    print("L =", L, " (1/|L|) sum_{p!=0} 1/E_p =", s/L**3, "  x2 =", 2*s/L**3)
