# GUIDE checks for row 1150 (pure Python, standard library only).
import math, random

def bessel_I(d, x, terms=400):
    # I_d(x) via series, computed in logs for stability
    s = 0.0
    lt0 = None
    out = 0.0
    for k in range(terms):
        lt = (2*k + d)*math.log(x/2) - math.lgamma(k+1) - math.lgamma(k+d+1)
        if lt0 is None:
            lt0 = lt
        out += math.exp(lt - lt0)
    return out, lt0  # value = out * exp(lt0)

def ratio_I(d, x):
    a, la = bessel_I(d, x)
    b, lb = bessel_I(1, x)
    return a/b*math.exp(la-lb)

# 1. W_r generating function
err = 0.0
for _ in range(200):
    r = random.uniform(0.0, 0.95); t = random.uniform(0.01, 3.1)
    s = sum(d*r**(d-1)*math.sin(d*t)/math.sin(t) for d in range(1, 3000))
    f = (1-r*r)/(1-2*r*math.cos(t)+r*r)**2
    err = max(err, abs(s-f)/f)
print("1. W_r formula max rel err:", err)

# 2. a_beta(d) * exp((d-1)/sqrt(beta)) bounded (expect about e^{1/2} = 1.65)
for beta in [4.0, 25.0, 100.0, 400.0]:
    m = max(ratio_I(d, beta)*math.exp((d-1)/math.sqrt(beta)) for d in range(1, int(12*math.sqrt(beta))+5))
    print("2. beta", beta, "max a(d) e^{(d-1)/sqrt beta} =", round(m, 4))

# 2b. 1 - a_beta(2) times beta (expect bounded, about 3/2)
for beta in [4.0, 25.0, 100.0, 400.0]:
    print("2b. beta", beta, "(1 - r_beta) beta =", round((1-ratio_I(2, beta))*beta, 4))

# 3. alternating lag sum <= H/4
worst = -1e9
for a in [0.5, 0.9, 0.99, 0.999]:
    for H in [10, 101, 1000]:
        v = 0.25*(H + 2*sum((-1)**d*(H-d)*a**(2*d) for d in range(1, H)))
        worst = max(worst, v/(H/4))
print("3. max of alternating variance / (H/4):", round(worst, 4))

# 4. Mehler composition: compose kernel exp(-s(x^2+y^2)/2 + xy) r times
def compose(A1, D1, A2, D2):
    # exp(-A1(x^2+z^2)/2 + D1 x z) * exp(-A2(z^2+y^2)/2 + D2 z y), integrate z
    # exponent in z: -(A1+A2) z^2/2 + z (D1 x + D2 y)
    S = A1 + A2
    # result: -A1 x^2/2 - A2 y^2/2 + (D1 x + D2 y)^2/(2S)
    Ax = A1 - D1*D1/S; Ay = A2 - D2*D2/S; Dxy = D1*D2/S
    return Ax, Ay, Dxy
for v in [0.01, 0.3, 2.0]:
    s = 1 + v/2; om = math.acosh(s)
    A, Ay, D = s, s, 1.0
    for r in range(2, 9):
        A, Ay, D = compose(A, D, s, 1.0)[0], compose(A, D, s, 1.0)[1], compose(A, D, s, 1.0)[2]
    r = 8
    print("4. v", v, "A err", abs(A - math.sinh(om)/math.tanh(r*om)), "D err", abs(D - math.sinh(om)/math.sinh(r*om)))

# 5. one-loop constant
print("5. 3 pi^2/11 =", 3*math.pi**2/11)

# 6. vacuum mean ratio 1/(s+d0) = e^{-omega}
for v in [0.001, 0.5, 3.0]:
    s = 1+v/2; d0 = math.sqrt(s*s-1)
    print("6. v", v, "1/(s+d0) - e^{-omega} =", 1/(s+d0) - math.exp(-math.acosh(s)))

# 7. thermal ratio identity tanh: tanh(log(1651/1650)/2) and 1 - e^{-J}
J = math.log(1651/1650)
print("7. 1 - e^{-J} =", 1-math.exp(-J), " 1/1651 =", 1/1651)

# 8. Bessel ratio monotone in v: I_{j+1}/I_j increasing
ok = True
for j in range(1, 6):
    prev = 0
    for v in [0.1*k for k in range(1, 300)]:
        a, la = bessel_I(j+1, v); b, lb = bessel_I(j, v)
        rr = a/b*math.exp(la-lb)
        if rr < prev - 1e-12: ok = False
        prev = rr
print("8. I_{j+1}/I_j increasing on grid:", ok)

# 9. z_{beta/2}/z_beta with z_s = int e^{-s a} dHaar, a = 1 - cos r, Haar density (2/pi) sin^2 r
def z(s, M=20000):
    h = math.pi/M
    return sum((2/math.pi)*math.sin((k+0.5)*h)**2*math.exp(-s*(1-math.cos((k+0.5)*h)))*h for k in range(M))
for beta in [10.0, 100.0, 1000.0]:
    print("9. beta", beta, "z_{beta/2}/z_beta =", round(z(beta/2)/z(beta), 4), "(2^{3/2} =", round(2**1.5, 4), ")")
