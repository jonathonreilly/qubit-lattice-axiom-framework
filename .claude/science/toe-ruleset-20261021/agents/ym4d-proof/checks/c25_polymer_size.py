"""c25: polymer-size bound N(tau) <= 2^d + 2^(d-1) sqrt(d) * length(tau) (criteria: checks/c25_criteria.md, first)."""
import itertools
import math
import resource
import time

import numpy as np

T0 = time.time()
RNG = np.random.default_rng(20261027)


def seg_hits_box(p, q, lo, hi):
    s0, s1 = 0.0, 1.0
    v = q - p
    for i in range(len(p)):
        if abs(v[i]) < 1e-15:
            if p[i] < lo[i] - 1e-12 or p[i] > hi[i] + 1e-12:
                return False
        else:
            a = (lo[i] - p[i]) / v[i]; b = (hi[i] - p[i]) / v[i]
            if a > b:
                a, b = b, a
            s0 = max(s0, a); s1 = min(s1, b)
            if s0 > s1 + 1e-12:
                return False
    return True


def count(segs, d):
    hit = set()
    for p, q in segs:
        mn = np.floor(np.minimum(p, q) - 1).astype(int); mx = np.ceil(np.maximum(p, q) + 1).astype(int)
        for k in itertools.product(*[range(mn[i], mx[i] + 1) for i in range(d)]):
            k = np.array(k, dtype=float)
            if seg_hits_box(p, q, k - 0.5, k + 0.5):
                hit.add(tuple(k.astype(int)))
    return len(hit)


def bound(d, ell):
    return 2 ** d + 2 ** (d - 1) * math.sqrt(d) * ell


def random_tree(d):
    segs = []
    p = RNG.uniform(-1, 1, size=d)
    for j in range(int(RNG.integers(1, 7))):
        if segs:
            a, b = segs[int(RNG.integers(len(segs)))]
            p = a + RNG.uniform() * (b - a)
        u = RNG.normal(size=d); u /= np.linalg.norm(u)
        if RNG.uniform() < 0.3:
            u = np.zeros(d); u[int(RNG.integers(d))] = 1.0
        segs.append((p, p + RNG.uniform(0, 3) * u))
    return segs


def adversarial(d):
    out = []
    h = np.full(d, 0.5)
    out.append([(h, h.copy())])                                   # a point at a cube corner
    for m in (1, 2, 3):
        for start in (np.zeros(d), h, np.r_[0.5, np.zeros(d - 1)]):
            e = np.zeros(d); e[0] = m
            out.append([(start, start + e)])                       # axis segments
    out.append([(h, h + np.ones(d))])                              # diagonal
    out.append([(h, h + 2 * np.ones(d) / math.sqrt(d))])
    for eps in (0.0, 0.05):                                        # stars of near-axis arms
        arms = []
        for i in range(d):
            for s in (1, -1):
                u = np.full(d, eps); u[i] = s; u /= np.linalg.norm(u)
                arms.append((h, h + 0.55 * u))
        out.append(arms)
    st = []; p = h.copy()                                          # staircase
    for j in range(6):
        e = np.zeros(d); e[j % d] = 1.0
        st.append((p, p + e)); p = p + e
    out.append(st)
    return out


worst = {}; worst3 = {}; viol = 0; n = 0
for d in (2, 3, 4):
    insts = [random_tree(d) for _ in range(2000)] + adversarial(d)
    w = 0.0; w3 = 0.0
    for segs in insts:
        ell = sum(float(np.linalg.norm(q - p)) for p, q in segs)
        N = count(segs, d)
        n += 1
        if N > bound(d, ell + 1e-9):
            viol += 1
        w = max(w, N / bound(d, ell)); w3 = max(w3, N / (3 ** d * (1 + ell)))
    worst[d] = w; worst3[d] = w3
    print(f"d={d}: {len(insts)} instances, max N/(2^d + 2^(d-1) sqrt(d) l) = {w:.4f}, max N/(3^d (1+l)) = {w3:.4f}",
          flush=True)
print(f"Q1 no violation of N <= 2^d + 2^(d-1) sqrt(d) l: {'PASS' if viol == 0 else 'FAIL'} ({viol} of {n})")
print(f"c25: time {time.time() - T0:.1f} s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB")
