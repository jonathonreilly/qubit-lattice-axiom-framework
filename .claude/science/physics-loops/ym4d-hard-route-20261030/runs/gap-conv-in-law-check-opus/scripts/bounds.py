# Guide arithmetic for the variational lower bounds used in the check of row 1118.
# Modified Bessel functions by their power series (exact up to float rounding).
import math
def I(n, x, terms=80):
    s = 0.0
    for k in range(terms):
        s += (x/2.0)**(2*k+n) / (math.factorial(k)*math.factorial(k+n))
    return s
def z(a):  # E_Haar exp(a tr U/2) on SU(2) = E_unif exp(a sigma.e) on S^3
    return 2.0*I(1,a)/a
def r(a):  # mean of tr U/2 under density prop. to exp(a tr U/2)
    return I(2,a)/I(1,a)
print("check z(2), I1(2), I2(2):", z(2.0), I(1,2.0), I(2,2.0))
grid = [0.5*k for k in range(1,61)]
# 2D O(4) sheet: <s.s>_nn >= sup_a [2b m^2 - (a m - log z)] / (2b)
for b in [2.3, 2.45, 2.6]:
    best = max(((2*b*r(a)**2 - (a*r(a) - math.log(z(a))))/(2*b), a) for a in grid)
    a2 = (2*b*r(2.0)**2 - (2.0*r(2.0) - math.log(z(2.0))))/(2*b)
    lb = best[0]
    print(f"O(4) b={b}: <ss> >= {lb:.4f} (a={best[1]}); a=2 gives {a2:.4f}; E p_c >= {(1-math.exp(-4*b))*lb/2:.4f} (a=2: {(1-math.exp(-4*b))*a2/2:.4f}); eps0(2)={1/50}")
# 4D SU(2) Wilson: Pbar >= sup_a [beta(3r^2+3r^4) - 3(a r - log z)] / (6 beta)
for beta in [2.3, 2.45, 2.6]:
    best = max(((beta*(3*r(a)**2+3*r(a)**4) - 3*(a*r(a)-math.log(z(a))))/(6*beta), a) for a in grid)
    a2 = (beta*(3*r(2.0)**2+3*r(2.0)**4) - 3*(2.0*r(2.0)-math.log(z(2.0))))/(6*beta)
    lb = best[0]
    l = 2
    print(f"SU(2) beta={beta}: Pbar >= {lb:.4f} (a={best[1]}); a=2 gives {a2:.4f}; E p_c >= {(1-math.exp(-3*beta*l))*lb/2:.4f} (a=2: {(1-math.exp(-3*beta*l))*a2/2:.4f}); eps0(4)={1/1250}")
# Donsker-Varadhan lower bound on KL(plaquette law || Haar) for a given mean P
for P in [0.6, 0.65]:
    kl = max(t*P - math.log(z(t)) for t in grid)
    print(f"KL(law with mean {P} || Haar) >= {kl:.3f}")
# small-beta scale: E p_c >= (1-e^{-3 beta l}) Pbar/2 with Pbar ~ beta/4 (strong-coupling leading order, argued)
for l in [2, 4, 8]:
    bmax = math.sqrt((1/1250)/(3*l/8))
    print(f"l={l}: (3/8) beta^2 l < 1/1250 needs beta < {bmax:.4f}")
