# Guide checks of (3), the Z_kappa bound, (4) under adversarial tilts, and the
# small-value probability of (11) under product Haar. Guide only.
import math
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quat import *  # noqa

rng = random.Random(7)


def I0(x):
    s, t, k = 0.0, 1.0, 0
    while True:
        s += t
        k += 1
        t *= (x/2)**2/(k*k)
        if t < 1e-17*s:
            return s + t


def I1(x):
    s, t, k = 0.0, x/2, 0
    while True:
        s += t
        k += 1
        t *= (x/2)**2/(k*(k+1))
        if t < 1e-17*s:
            return s + t


print("kappa, exact sup density kappa I0/(2 I1), bound 2 e^(1/2)(1+kappa), M_b at kappa = 6b")
for kappa in [0.5, 2.0, 6.0, 13.8, 15.6]:
    # numeric Z by midpoint rule
    n = 20000
    Z = sum(2*((k+0.5)/n)*I0(kappa*(k+0.5)/n) for k in range(n))/n
    Zc = 2*I1(kappa)/kappa
    lb = math.exp(-0.5)*I0(kappa)/(2*(1+kappa))
    print("  %.1f  Z_num %.6g  Z_closed %.6g  Z_lower %.6g  sup %.3f  bound %.3f  M_b %.3f"
          % (kappa, Z, Zc, lb, I0(kappa)/Z, 2*math.exp(0.5)*(1+kappa), 4*(1+kappa)))


def sample_tilt(kappa, c, rng):
    """q with density exp(kappa <q, c>) w.r.t. Haar, c a unit quaternion."""
    while True:
        lo = math.exp(-2.0*kappa)
        y = lo + (1.0 - lo)*rng.random()
        w0 = 1.0 + math.log(y)/kappa
        if rng.random() < math.sqrt(max(0.0, 1.0 - w0*w0)):
            break
    while True:
        d = [rng.gauss(0.0, 1.0) for _ in range(3)]
        nd = math.sqrt(sum(t*t for t in d))
        if nd > 1e-12:
            break
    s = math.sqrt(max(0.0, 1.0 - w0*w0))/nd
    W = (w0, s*d[0], s*d[1], s*d[2])
    # density exp(kappa Re W); q = W c has Re(q conj c) = Re W
    return qmul(W, c)


b = 2.6
kappa = 6*b
Mb = 4*(1+6*b)
n = (0.0, 0.0, 1.0)
print("\n(3) at b = 2.6, kappa = 15.6, n = k: P{|u x n| <= t} versus M_b t^2")
for name, c in [("h along 1", ONE), ("h along k", (0.0, 0.0, 0.0, 1.0)),
                ("h along i", (0.0, 1.0, 0.0, 0.0)),
                ("h along (1+k)/sqrt2", (1/math.sqrt(2), 0.0, 0.0, 1/math.sqrt(2)))]:
    N = 200000
    cnt = {0.05: 0, 0.1: 0, 0.2: 0}
    for _ in range(N):
        q = sample_tilt(kappa, c, rng)
        cr = math.sqrt(vnorm2(vcross(im(q), n)))
        for t in cnt:
            if cr <= t:
                cnt[t] += 1
    print("  %-22s" % name + "  ".join("t=%.2f: P=%.5f bound=%.4f" % (t, cnt[t]/N, Mb*t*t) for t in sorted(cnt)))

# (4) with both holonomies tilted toward 1 at kappa = 6b (an adversarial case)
delta = 1/(8*(1+6*b))
N = 200000
small = 0
c1 = 0
for _ in range(N):
    h1 = sample_tilt(kappa, ONE, rng)
    h2 = sample_tilt(kappa, ONE, rng)
    D = 4*lam_min_cross([im(h1), im(h2)])
    if D < delta:
        small += 1
    u1, u2 = im(h1), im(h2)
    if vnorm2(u1) > 0:
        uh = vscale(1/math.sqrt(vnorm2(u1)), u1)
        if vnorm2(vcross(u2, uh)) < delta/2:
            c1 += 1
print("\n(4) adversarial tilt to 1 at b=2.6: delta_b = %.5f, P{D < delta_b} = %.5f (bound 1/2);"
      " P{|u2 x u1hat|^2 < delta_b/2} = %.5f (bound M_b delta_b/2 = 1/4)" % (delta, small/N, c1/N))

# small-value probability for the (11) test under product Haar, two masks
lat = Lattice([5, 5, 5, 5], cold=True)
y = (2, 2, 2, 2)
i, j = 0, 1
z = lat.sh(y, i)
# support: links in plaquettes through incoming links at z
support = set()
for mu in range(4):
    t = lat.sh(z, mu, -1)
    e = (t, mu)
    support.add(e)
    for nu in range(4):
        if nu == mu:
            continue
        for base in [t, lat.sh(t, nu, -1)]:
            for (xx, mm) in [(base, mu), (lat.sh(base, mu), nu), (lat.sh(base, nu), mu), (base, nu)]:
                support.add((xx, mm))
supp = sorted(support)
print("\nsupport size of the (11) test:", len(supp), "(file bound 96)")
# max-norm distance of support link endpoints from y
def dist(a, c):
    return max(min(abs(a[k]-c[k]), 5-abs(a[k]-c[k])) for k in range(4))
print("max max-norm distance of support endpoints from y:",
      max(max(dist(xx, y), dist(lat.sh(xx, mm), y)) for (xx, mm) in supp))
lnk = (y, i)
mnk = (y, j)
v = (0.0, 0.0, 1.0)
for maskname, treeprob in [("all support chords", 0.0), ("random mask p_tree=0.5", 0.5)]:
    N = 20000
    vals = []
    for _ in range(N):
        for key in supp:
            if key in (lnk, mnk) or rng.random() >= treeprob:
                lat.U[key] = haar(rng)
            else:
                lat.U[key] = ONE
        B = (0.0, 0.0, 0.0)
        for mu in range(4):
            t = lat.sh(z, mu, -1)
            Nf = lat.force(t, mu, 1.0)
            B = vadd(B, vsub(ad_inv(lat.U[(t, mu)], Nf), Nf))
        vals.append(abs(vdot(v, B)))
    out = []
    for eps in [0.005, 0.02, 0.05, 0.2]:
        out.append("eps=%.3f: %.4f" % (eps, sum(1 for x in vals if x <= 2*eps)/N))
    print("  P_Haar{|v.B_z|/b <= 2 eps}, %s: " % maskname + ", ".join(out))
