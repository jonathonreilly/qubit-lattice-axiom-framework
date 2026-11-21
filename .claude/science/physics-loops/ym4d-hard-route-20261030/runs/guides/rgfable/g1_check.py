# Guide only. One-link sewing on SU(2) = unit S^3 for class functions.
# w = exp(-phi), phi(rho) radial, rho in [0, pi] geodesic distance from identity.
# Exact stiffness at identity of w*w from characters, against:
#   bound B = (1/6) E_mu[Laplacian phi], mu ~ exp(-2 phi) Haar   (Proposition G1)
#   asymptotic s/2 - 1/6.
import math

def simpson(f, a, b, n):
    if n % 2: n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def run(s, kind):
    if kind == "quad":      # phi = s rho^2 / 2
        phi  = lambda r: 0.5 * s * r * r
        dphi = lambda r: s * r
        d2phi = lambda r: s
    else:                   # Wilson type: phi = s (1 - cos rho); Hess phi = s cos(rho) g <= s
        phi  = lambda r: s * (1 - math.cos(r))
        dphi = lambda r: s * math.sin(r)
        d2phi = lambda r: s * math.cos(r)
    n = 20000
    eps = 1e-9
    # character coefficients  what_d = (2/pi) int sin(rho) w(rho) sin(d rho) drho
    dmax = int(12 * math.sqrt(s)) + 40
    num = 0.0; den = 0.0
    for d in range(1, dmax + 1):
        wd = (2 / math.pi) * simpson(lambda r: math.sin(r) * math.exp(-phi(r)) * math.sin(d * r), 0.0, math.pi, n)
        a = wd * wd / d
        num += a * d * (d * d - 1) / 3.0
        den += a * d
    exact = num / den
    # bound: (1/6) E_mu[phi'' + 2 cot(rho) phi'],  mu ~ sin^2(rho) exp(-2 phi)
    Z = simpson(lambda r: math.sin(r) ** 2 * math.exp(-2 * phi(r)), eps, math.pi - eps, n)
    L = simpson(lambda r: math.sin(r) ** 2 * math.exp(-2 * phi(r)) * (d2phi(r) + 2 * dphi(r) * math.cos(r) / math.sin(r)), eps, math.pi - eps, n)
    bound = L / Z / 6.0
    return exact, bound

print("kind   s     exact      boundG1    s/2-1/6    s/2")
for kind in ("quad", "wilson"):
    for s in (2.0, 5.0, 10.0, 20.0, 40.0):
        ex, bd = run(s, kind)
        print(f"{kind:6s} {s:5.1f} {ex:10.5f} {bd:10.5f} {s/2-1/6:10.5f} {s/2:8.3f}")
