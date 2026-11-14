# lg55_2 -- exact linearised structure of the S4' block average (LARGE55 sections 3 and 6).
# Criteria: lg55_2_criteria.md (written before this script). Exact arithmetic (fractions.Fraction) for every verdict.
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial
import sys

def axial_path(start, end, sigma):
    cur = list(start); steps = []
    for k in sigma:
        while cur[k] < end[k]:
            steps.append(((tuple(cur), k), 1)); cur[k] += 1
        while cur[k] > end[k]:
            cur[k] -= 1; steps.append(((tuple(cur), k), -1))
    return steps

def add(v, w): return tuple(a + b for a, b in zip(v, w))
def scal(c, v): return tuple(c * a for a in v)
def unit(d, k): return tuple(1 if i == k else 0 for i in range(d))

def base_map(d, L, mu):
    """signed incidence counts (integers) for coarse link (0, mu); returns (counts, first_step_counts, empty_count, sites)"""
    m = (L - 1) // 2
    cX = tuple([0] * d); cY = scal(L, unit(d, mu))
    counts = {}; first = {}; empty = 0; sites = set()
    for sigma in permutations(range(d)):
        for z in product(range(-m, m + 1), repeat=d):
            y = tuple(z)
            p1 = axial_path(cX, y, sigma)
            if p1:
                (lk, sg) = p1[0]
                key = (lk[1], sg)
                first[key] = first.get(key, 0) + 1
            else:
                empty += 1
            p2 = [((add(y, scal(j, unit(d, mu))), mu), 1) for j in range(L)]
            p3f = axial_path(cY, add(y, scal(L, unit(d, mu))), sigma)
            p3 = [(lk, -sg) for (lk, sg) in reversed(p3f)]
            for (lk, sg) in p1 + p2 + p3:
                counts[lk] = counts.get(lk, 0) + sg
                s = lk[0]; sites.add(s); sites.add(add(s, unit(d, lk[1])))
    return counts, first, empty, sites

def translate_map(mp, shift, d):
    return {((add(s, shift)), k): v for (s, k), v in mp.items()}

def run(d, L, report):
    m = (L - 1) // 2
    norm = factorial(d) * L ** d
    base = {}; firsts = {}; empties = {}; siteset = {}
    for mu in range(d):
        c, f, e, s = base_map(d, L, mu)
        base[mu] = {k: F(v, norm) for k, v in c.items() if v != 0}
        firsts[mu] = f; empties[mu] = e; siteset[mu] = s
    def in_block(s, X):
        cX = scal(L, X)
        return all(-m <= s[i] - cX[i] <= m for i in range(d))
    # G0: every site visited by contours of (0,mu) lies in B(0) U B(e_mu)  (translation covariance gives all X)
    g0 = all(all(in_block(s, tuple([0]*d)) or in_block(s, unit(d, mu)) for s in siteset[mu]) for mu in range(d))
    # weight map of a general coarse link (X, mu) by translation
    def wmap(X, mu):
        return translate_map(base[mu], scal(L, X), d) if any(X) else base[mu]
    zero = tuple([0] * d)
    # plaquettes containing coarse site 0
    plaqs = []
    for mu in range(d):
        for nu in range(mu + 1, d):
            for a, b in product([0, 1], repeat=2):
                X = add(scal(-a, unit(d, mu)), scal(-b, unit(d, nu)))
                plaqs.append((X, mu, nu))
    def plaq_links(P):
        X, mu, nu = P
        return [((X, mu), 1), ((add(X, unit(d, mu)), nu), 1), ((add(X, unit(d, nu)), mu), -1), ((X, nu), -1)]
    maps = {}
    def getmap(cl):
        if cl not in maps:
            maps[cl] = wmap(cl[0], cl[1])
        return maps[cl]
    def theta(cl, a):
        return sum((w * a(lk) for lk, w in getmap(cl).items()), F(0))
    def Theta(P, a):
        return sum((sg * theta(cl, a) for cl, sg in plaq_links(P)), F(0))
    # G1 gauge control and non-gauge control
    def omega(s):
        h = 0
        for i, x in enumerate(s):
            h = (h * 1000003 + (x + 7919) * (i + 3)) % 2147483647
        return (h * 48271) % 1009 - 504
    a_gauge = lambda lk: omega(add(lk[0], unit(d, lk[1]))) - omega(lk[0])
    def a_rand(lk):
        s, k = lk; h = 17
        for x in s: h = (h * 31 + x + 101) % 1000003
        return (h * (k + 13) * 2654435761) % 97 - 48
    g1a = all(Theta(P, a_gauge) == 0 for P in plaqs)
    g1b = any(Theta(P, a_rand) != 0 for P in plaqs)
    # G2 first-link formula
    target = F(L ** d - 1, 2 * d * L ** d)
    g2 = True
    for mu in range(d):
        for nu in range(d):
            for sg in (1, -1):
                if F(firsts[mu].get((nu, sg), 0), norm) != target: g2 = False
        if F(empties[mu], norm) != F(1, L ** d): g2 = False
    # H3
    wmax = max(abs(w) for mu in range(d) for w in base[mu].values())
    h3 = wmax < F(1, 2)
    # single-link responses for links with both ends in B(0)
    blinks = set()
    for mu in range(d):
        for cl in [(zero, mu), (scal(-1, unit(d, mu)), mu)]:
            for lk in getmap(cl):
                s, k = lk
                if in_block(s, zero) and in_block(add(s, unit(d, k)), zero):
                    blinks.add(lk)
    R1 = F(0); R1c = F(0)
    centre_links = set([(zero, k) for k in range(d)] + [(scal(-1, unit(d, k)), k) for k in range(d)])
    for lk in blinks:
        for P in plaqs:
            val = sum((sg * getmap(cl).get(lk, F(0)) for cl, sg in plaq_links(P)), F(0))
            if abs(val) > R1: R1 = abs(val)
            if lk in centre_links and abs(val) > R1c: R1c = abs(val)
    # H5 two levels at a deep centre: perturb b0 = (c_0, e_0)
    b0 = (zero, 0)
    th1 = {}
    for mu in range(d):
        for cl in [(zero, mu), (scal(-1, unit(d, mu)), mu)]:
            th1[cl] = getmap(cl).get(b0, F(0))
    # support check: no other coarse link in the radius-1 star reads b0 (G0 already implies it)
    R1b0 = max(abs(sum((sg * th1.get(cl, F(0)) for cl, sg in plaq_links(P)), F(0))) for P in plaqs)
    # level 2: level-1 links are (site, dir) on the coarse lattice; their level-2 weights use the same base maps
    th2 = {}
    for mu in range(d):
        for cl2 in [(zero, mu), (scal(-1, unit(d, mu)), mu)]:
            mp = getmap(cl2)   # same construction one level up (scale-free)
            th2[cl2] = sum((mp.get((cl1[0], cl1[1]), F(0)) * v for cl1, v in th1.items()), F(0))
    R2 = max(abs(sum((sg * th2.get(cl, F(0)) for cl, sg in plaq_links(P)), F(0))) for P in plaqs)
    # gauge decomposition of theta^(1)(b0)
    outs = [th1[(zero, mu)] for mu in range(d)]
    ins = [th1[(scal(-1, unit(d, mu)), mu)] for mu in range(d)]
    om = (sum(-x for x in outs) + sum(ins)) / (2 * d)
    rem = max([abs(x + om) for x in outs] + [abs(x - om) for x in ins])
    res = dict(g0=g0, g1a=g1a, g1b=g1b, g2=g2, h3=h3, wmax=wmax, R1=R1, R1c=R1c, R1b0=R1b0, R2=R2, om=om, rem=rem,
               nblinks=len(blinks))
    report.append("d=%d L=%d: G0=%s G1(gauge=0)=%s G1(nongauge!=0)=%s G2=%s H3=%s wmax=%s R1=%s (%.5f) R1c=%s (%.5f) "
                  "R1(b0)=%s (%.5f) R2=%s (%.5f) omega=%s (%.5f; predicted -(L^d-1)/(2dL^d)=%s) gauge-remainder=%s (%.6f) "
                  "#links(B0)=%d" % (d, L, g0, g1a, g1b, g2, h3, wmax, R1, float(R1), R1c, float(R1c), R1b0, float(R1b0),
                  R2, float(R2), om, float(om), -F(L**d-1, 2*d*L**d), rem, float(rem), len(blinks)))
    return res

report = []
results = {}
for (d, L) in [(2, 3), (2, 5), (3, 3), (3, 5), (4, 3), (4, 5)]:
    results[(d, L)] = run(d, L, report)
    print(report[-1]); sys.stdout.flush()
G0 = all(r['g0'] for r in results.values())
G1 = all(r['g1a'] and r['g1b'] for r in results.values())
G2 = all(r['g2'] for r in results.values())
H3 = all(r['h3'] for r in results.values())
H4 = results[(4, 3)]['R1'] <= F(1, 4) and results[(4, 5)]['R1'] <= F(1, 4) and results[(4, 5)]['R1'] < results[(4, 3)]['R1']
H5 = all(results[(4, L)]['R2'] <= results[(4, L)]['R1b0'] / 2 for L in (3, 5))
for name, v in [("G0", G0), ("G1", G1), ("G2", G2), ("H3", H3), ("H4", H4), ("H5", H5)]:
    print("%s: %s" % (name, "PASS" if v else "FAIL"))
print("OVERALL (gates G0-G2 and hypotheses H3-H5): %s" % ("PASS" if all([G0, G1, G2, H3, H4, H5]) else "FAIL"))
