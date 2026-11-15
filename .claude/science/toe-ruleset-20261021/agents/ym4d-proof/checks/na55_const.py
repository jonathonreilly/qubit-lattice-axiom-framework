"""na55_const — exact rational / rigorous-interval arithmetic for NODEA55.md (criteria: checks/na55_const_criteria.md,
written first). Plain python: fractions only. Every transcendental value is a closed rational interval [lo, hi]."""
from fractions import Fraction as Fr
import itertools, sys, time

t0 = time.time()
res = {}


# ---------- rigorous intervals ----------
def atanh_iv(z, terms=80):
    """2*atanh(z) for rational 0 < z < 1: partial sum S_N and remainder <= 2 z^{2N+1}/((2N+1)(1 - z^2))."""
    s = Fr(0)
    p = z
    for k in range(terms):
        s += p / (2 * k + 1)
        p *= z * z
    rem = 2 * p / ((2 * terms + 1) * (1 - z * z))
    return (2 * s, 2 * s + rem)


LN2 = atanh_iv(Fr(1, 3))          # ln 2
LN54 = atanh_iv(Fr(1, 9))         # ln(5/4)
LN32 = atanh_iv(Fr(1, 5))         # ln(3/2)


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def iscale(c, a):
    c = Fr(c)
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


LN3 = iadd(LN2, LN32)
LN5 = iadd(iscale(2, LN2), LN54)
LN10 = iadd(LN2, LN5)
LN6400 = iadd(iscale(12, LN2), iscale(2, LN54))       # 6400 = 2^8 * 5^2
LN12800 = iadd(iscale(13, LN2), iscale(2, LN54))      # 12800 = 2^9 * 5^2


def ln_rat(x):
    """ln of a positive rational x, as an interval: x = 2^e * m with m in [1, 2); ln m = 2 atanh((m-1)/(m+1))."""
    x = Fr(x)
    e = 0
    while x >= 2:
        x /= 2
        e += 1
    while x < 1:
        x *= 2
        e -= 1
    z = (x - 1) / (x + 1)
    lm = atanh_iv(z, 120) if z > 0 else (Fr(0), Fr(0))
    return iadd(iscale(e, LN2), lm)


def log10_rat(x):
    lx = ln_rat(x)
    return (lx[0] / LN10[1] if lx[0] >= 0 else lx[0] / LN10[0], lx[1] / LN10[0] if lx[1] >= 0 else lx[1] / LN10[1])


def sin_iv(x, terms=60):
    """sin x for rational x >= 0 (x <= 6): alternating Taylor series, terms decreasing once n > x."""
    x = Fr(x)
    s = Fr(0)
    t = x
    n = 1
    for k in range(terms):
        s += t if k % 2 == 0 else -t
        t = t * x * x / ((n + 1) * (n + 2))
        n += 2
    return (s - abs(t), s + abs(t))


def cos_iv(x, terms=60):
    x = Fr(x)
    s = Fr(0)
    t = Fr(1)
    n = 0
    for k in range(terms):
        s += t if k % 2 == 0 else -t
        t = t * x * x / ((n + 1) * (n + 2))
        n += 2
    return (s - abs(t), s + abs(t))


def idiv_pos(a, b):          # a, b positive intervals
    return (a[0] / b[1], a[1] / b[0])


def fmt(iv):
    lo, hi = iv
    return "[%.12e, %.12e]" % (float(lo), float(hi))     # display only


A = Fr(1, 10 ** 86)
BETA = Fr(186, 1000)
DX = Fr(25, 10 ** 153)
RLF = Fr(1, 10 ** 94)


def g2_hw(cplus, cU=1):
    b_n = 81 * 81 * 10002 * cplus + 10001 * cU
    return idiv_pos((A, A), iadd((Fr(b_n), Fr(b_n)), LN12800)), b_n


# ---------- K1 ----------
g_noring, bn1 = g2_hw(1)
g_ring17, bn17 = g2_hw(17)
k1 = (Fr(152361, 10 ** 99) <= g_noring[0] and g_noring[1] <= Fr(152363, 10 ** 99)
      and Fr(896375, 10 ** 101) <= g_ring17[0] and g_ring17[1] <= Fr(896377, 10 ** 101))
res['K1'] = k1
print("K1: HW s6 no ring: b_n=%d g2 in %s ; ring x17: b_n=%d g2 in %s -> %s"
      % (bn1, fmt(g_noring), bn17, fmt(g_ring17), "PASS" if k1 else "FAIL"))

# ---------- K2 ----------
def route4(cU, cA):
    b_n = 12401 * cU + 810162 * cA
    b_D = 10000 * cU + 810000 * cA
    c_f = cU + 81 * cA
    g2 = idiv_pos((A, A), iadd((Fr(b_n), Fr(b_n)), LN6400))
    nT = idiv_pos((Fr(b_D), Fr(b_D)), iscale(A * BETA, LN3))
    out = dict(b_n=b_n, b_D=b_D, c_f=c_f, g2=g2, nT=nT)
    for tag, h1, h0 in (('HIST', 38417, 38416), ('sharp', 10001, 10000)):
        Bs, B0 = c_f + 1, c_f + 2
        out['rel_' + tag] = (A / (h1 * Bs), A / (h1 * Bs))
        out['hist_' + tag] = idiv_pos((A, A), iadd((Fr(h1 * B0), Fr(h1 * B0)), LN12800))
        num = iadd((Fr(4), Fr(4)), idiv_pos((Fr(h0 * c_f), Fr(h0 * c_f)), LN3)) if c_f > 0 else (Fr(4), Fr(4))
        out['nH_' + tag] = (num[0] / (A * BETA), num[1] / (A * BETA))
    return out


k2ok = True
for (cU, cA) in ((1, 0), (1, 1)):
    o = route4(cU, cA)
    print("K2 route (4°) at c_U=%d, c_A=%d: b_n°=%d b_D°=%d c_f°=%d" % (cU, cA, o['b_n'], o['b_D'], o['c_f']))
    for key in ('g2', 'nT', 'rel_HIST', 'hist_HIST', 'nH_HIST', 'rel_sharp', 'hist_sharp', 'nH_sharp'):
        iv = o[key]
        print("     %-10s %s" % (key, fmt(iv)))
        if iv[1] - iv[0] > iv[0] / 10 ** 6:
            k2ok = False
    ceil = min((o['g2'][0], 'g2'), (o['hist_HIST'][0], 'hist_HIST'), (o['rel_HIST'][0], 'rel_HIST'))
    ceil_sharp = min((o['g2'][0], 'g2'), (o['hist_sharp'][0], 'hist_sharp'), (o['rel_sharp'][0], 'rel_sharp'))
    for name, c in (('HIST as written', ceil), ('H-geo\' adopted', ceil_sharp)):
        d1 = log10_rat(c[0] / RLF)
        d2 = log10_rat(c[0] / DX)
        print("     binding ceiling (%s) = %s (%s): decades above 1e-94 %s ; above 2.5e-152 %s"
              % (name, "%.6e" % float(c[0]), c[1], fmt(d1), fmt(d2)))
    nTmax = o['nT'][1]
    nHmin = min(o['nH_HIST'][0], o['nH_sharp'][0])
    print("     (T°) adds nothing beyond n_H (n_T° < n_H): %s" % (nTmax < nHmin))
# HW s6 ring x17 binding ceiling for comparison (HIST as written): HIST-sum at B_0 = 111537 + 2
cf17 = 81 * 81 * 17
hist17 = idiv_pos((A, A), iadd((Fr(38417 * (cf17 + 2)), Fr(38417 * (cf17 + 2))), LN12800))
print("     HW s6 x17 HIST-sum (HIST as written) = %s ; route(4°)/HW ratio of binding ceilings (HIST as written) = %s"
      % (fmt(hist17), fmt(idiv_pos(route4(1, 0)['hist_HIST'], hist17))))
res['K2'] = k2ok
print("K2-sanity (all enclosures relative width < 1e-6): %s" % ("PASS" if k2ok else "FAIL"))

# ---------- K3 ----------
def k3(b):
    b = Fr(b)
    s = sin_iv(50 * b)
    c = cos_iv(b)
    lhs = (4 * min(s[0] ** 2, s[1] ** 2) / 72 if s[0] > 0 else Fr(0), 4 * max(s[0] ** 2, s[1] ** 2) / 72)
    rhs = (100 * (1 - c[1]), 100 * (1 - c[0]))
    return lhs, rhs


k3ok = True
for b in (Fr(1, 1000), Fr(1, 100), Fr(3, 100)):
    lhs, rhs = k3(b)
    ok = lhs[0] > rhs[1]
    k3ok = k3ok and ok
    print("K3: b=%s  LHS (2 sin 50b)^2/72 in %s  RHS 100(1-cos b) in %s  -> %s" % (b, fmt(lhs), fmt(rhs), ok))
lhs, rhs = k3(Fr(1, 10))
neg = lhs[1] < rhs[0]
res['K3'] = k3ok
print("K3: %s ; K3n (b = 1/10 must fail): LHS %s RHS %s -> control fires = %s"
      % ("PASS" if k3ok else "FAIL", fmt(lhs), fmt(rhs), neg))

# ---------- K4 ----------
lo4, hi4 = -2, 10
def inB(p):
    return all(0 <= c <= 8 for c in p)
okA = okB = okC = True
slice_counts = []
for x3 in range(lo4, hi4 + 1):
    for x4 in range(lo4, hi4 + 1):
        nfree = ninside = 0
        for x1 in range(lo4, hi4):
            for x2 in range(lo4, hi4):
                v = [(x1, x2, x3, x4), (x1 + 1, x2, x3, x4), (x1 + 1, x2 + 1, x3, x4), (x1, x2 + 1, x3, x4)]
                links = [(v[i], v[(i + 1) % 4]) for i in range(4)]
                free = any(inB(a) or inB(b) for a, b in links)
                if free:
                    nfree += 1
                    if not (-1 <= x1 <= 8 and -1 <= x2 <= 8):
                        okA = False
                if all(inB(p) for p in v):
                    ninside += 1
        inslice = (0 <= x3 <= 8 and 0 <= x4 <= 8)
        if inslice:
            slice_counts.append((nfree, ninside))
            if not (nfree == 100 and ninside == 64):
                okA = False
            # (c) boundary loop of [-1, 9]^2
            loop = []
            for t in range(-1, 9):
                loop.append(((t, -1, x3, x4), (t + 1, -1, x3, x4)))
                loop.append(((9, t, x3, x4), (9, t + 1, x3, x4)))
                loop.append(((t, 9, x3, x4), (t + 1, 9, x3, x4)))
                loop.append(((-1, t, x3, x4), (-1, t + 1, x3, x4)))
            if any(inB(a) or inB(b) for a, b in loop):
                okC = False
        else:
            if nfree != 0:
                okB = False
res['K4'] = okA and okB and okC
print("K4: 81 slices, (free, inside) counts all (100, 64): %s ; (b) no free (1,2)-plaquette off the 81 slices: %s ; "
      "(c) loop links all outside-outside: %s -> %s" % (okA, okB, okC, "PASS" if res['K4'] else "FAIL"))
print("    distinct per-slice counts:", sorted(set(slice_counts)))

# ---------- K5 ----------
k5 = all(Fr(k, 1000) / (1 - Fr(k, 1000)) <= 2 * Fr(k, 1000) for k in range(1, 501))
x = Fr(3, 4)
k5n = not (x / (1 - x) <= 2 * x)
res['K5'] = k5
print("K5: x/(1-x) <= 2x on x = k/1000, k = 1..500: %s ; K5n (x = 3/4 violates): %s" % ("PASS" if k5 else "FAIL", k5n))

# ---------- K6 ----------
links = 0
rng9 = range(0, 9)
for p in itertools.product(rng9, repeat=4):
    for mu in range(4):
        q = list(p)
        q[mu] += 1
        if q[mu] <= 8:
            links += 1
k6 = (links == 4 * 8 * 9 ** 3)
res['K6'] = k6
logc = iscale(Fr(3 * links, 2), LN2)
print("K6: links in a 9^4 block = %d (4*8*9^3 = %d) -> %s ; real dof 3*links = %d ; Gaussian-model log c_cem at lambda_f=1/2: %s"
      % (links, 4 * 8 * 9 ** 3, "PASS" if k6 else "FAIL", 3 * links, fmt(logc)))

# ---------- K7 ----------
cpr = Fr(1, 1797760)
for (p, q) in ((Fr(2), Fr(2)), (Fr(3, 2), Fr(3)), (Fr(7, 6), Fr(7))):
    assert 1 / p + 1 / q == 1
    for r in (Fr(0), Fr(1, 100)):
        th = min(1 / (24 * p * (1 + 2 * r)), 1 / (4 * q * (1 + 2 * r)))
        kap = 256 * q * th * cpr / Fr(1, 2)
        print("K7: (p,q)=(%s,%s) r=%s: theta_max = %s = %.6f ; kappa >= %s = %.6e" % (p, q, r, th, float(th), kap, float(kap)))
print("SUMMARY:", " ".join("%s=%s" % (k, "PASS" if v else "FAIL") for k, v in res.items()),
      " elapsed %.1fs" % (time.time() - t0))
