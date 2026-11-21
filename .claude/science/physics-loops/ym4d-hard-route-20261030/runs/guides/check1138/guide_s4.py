# Numeric guide only (not a proof): commutator class-angle law and s_4. Pure Python.
import math, random
rng = random.Random(1138)
def haar():
    while True:
        q = [rng.gauss(0, 1) for _ in range(4)]
        r = math.sqrt(sum(x*x for x in q))
        if r > 1e-12:
            return [x / r for x in q]
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return [a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2]
def qinv(q):
    return [q[0], -q[1], -q[2], -q[3]]
n = 400000
nb = 10
hist = [0]*nb
acc_abs = 0.0
plus = [0]*nb; tot = [0]*nb
for _ in range(n):
    a, b = haar(), haar()
    c = qmul(qmul(a, b), qmul(qinv(a), qinv(b)))
    th = math.acos(max(-1.0, min(1.0, c[0])))
    i = min(nb - 1, int(th / math.pi * nb)); hist[i] += 1
    s = 1 if rng.random() < 0.5 else -1
    thz = th if s == 1 else math.pi - th
    acc_abs += abs(1 - 2*thz/math.pi)
    j = min(nb - 1, int(thz / math.pi * nb)); tot[j] += 1; plus[j] += (s == 1)
w = math.pi / nb
maxdev = 0.0
for i in range(nb):
    lo, hi = i*w, (i+1)*w
    # exact bin mass of density (1/pi) sin(t)(pi - t): antiderivative F(t) = (1/pi)[-(pi - t)cos t - sin t]
    F = lambda t: (-(math.pi - t)*math.cos(t) - math.sin(t)) / math.pi
    maxdev = max(maxdev, abs(hist[i]/n - (F(hi) - F(lo))))
print("max |empirical - predicted| bin mass, commutator angle:", round(maxdev, 5))
print("E|1-2theta_z/pi| = %.5f, predicted 1-2/pi = %.5f" % (acc_abs/n, 1 - 2/math.pi))
for i in (0, 3, 6, 9):
    th0 = (i + 0.5)*w
    print("bin %d: P(sigma=+1|theta) = %.4f, predicted near %.4f" % (i, plus[i]/tot[i], (math.pi - th0)/math.pi))
s4 = (1 + (1 - 2/math.pi)**4)/2
print("s_4 = %.6f, below 0.51: %s; (1-2/pi)^4 = %.6f < (4/11)^4 = %.6f < 0.02" % (s4, s4 < 0.51, (1-2/math.pi)**4, (4/11)**4))
