#!/usr/bin/env python3
"""J:derive:recapture-share-of-a-body-in-balance:a1 - checks for ATTEMPT.md (same directory).

Blocks 44-49 (sphere menu, supplied clause): a record of content s steps to x + e_k with probability max(0, s.e_k)/sqrt 3;
a body in balance re-emits each captured record from a random site through a random free face k, with the cosine law about
e_k, the new record sitting on the neighbouring site (probes/lib/inertial_balanced.py, emit()).
Without scattering and at small density an emitted content is a directed walk: each move goes along sign(v_j) e_j with
probability |v_j|/|v|_1. The share of the body's captures that are its own emissions is the probability that this walk
steps onto a body site (steady state: emissions = captures). Exact pieces: combinatorics, the two-site hitting function
(Gauss quadrature on the simplex, checked for convergence), the first-order share, exact first-passage DP given the content;
the task's check is the share by DIRECT SAMPLING of the walks (numba, cache=False).
"""
import math
import time

import numpy as np
from numba import njit
from scipy.stats import poisson

FAILS = []
T0 = time.time()


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg, flush=True)
    if not good:
        FAILS.append(tag)


EK = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], np.int64)
R = 4
BALL = [(x, y, z) for x in range(-R, R + 1) for y in range(-R, R + 1) for z in range(-R, R + 1) if x * x + y * y + z * z <= R * R]


# ------------------------------------------------------------------ A1: the walk never returns to its site or a neighbour
def reachable(d, k):
    """can the walk that starts at e_k with content v (v.e_k > 0) reach displacement d for SOME v?"""
    D = np.array(d) - EK[k]
    ax, sg = k // 2, (1 if k % 2 == 0 else -1)
    return tuple(d) != tuple(EK[k]) and sg * D[ax] >= 0


never_self = all(not reachable((0, 0, 0), k) for k in range(6))
never_nbr = all(not reachable(tuple(EK[j]), k) for j in range(6) for k in range(6))
pairs = {}
for a in BALL:
    for b in BALL:
        if a != b:
            d = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
            pairs[d] = pairs.get(d, 0) + 1
ok("A1", never_self and never_nbr and len(BALL) == 257 and sum(pairs.values()) == 257 * 256,
   "exact: a record emitted through face k has v.e_k > 0, so its k-coordinate never decreases; it can never step back "
   "onto the emitting site nor onto any lattice neighbour of it (all 6 x 6 cases); the lattice ball of radius 4 has "
   f"257 sites, {len(pairs)} displacements over the 65792 ordered pairs")


# ------------------------------------------------------------------ A2: the two-site function and the first-order share
def tri_rule(n):
    x, w = np.polynomial.legendre.leggauss(n)
    x, w = (x + 1) / 2, w / 2
    U, T = np.meshgrid(x, x, indexing='ij')
    WU, WT = np.meshgrid(w, w, indexing='ij')
    return U.ravel(), ((1 - U) * T).ravel(), (WU * WT * (1 - U)).ravel()


def make_J(n):
    qa, qb, wt = tri_rule(n)
    qn = 1 - qa - qb
    r4 = (qa ** 2 + qb ** 2 + qn ** 2) ** 2
    cache = {}

    def J(mn, ma, mb):
        """(1/pi) int_simplex q_n^(mn+1) q_a^ma q_b^mb |q|^-4 dq_a dq_b: one octant of the cosine law, q = |v|/|v|_1"""
        key = (mn, ma, mb)
        if key not in cache:
            cache[key] = float(np.sum(wt * qn ** (mn + 1) * qa ** ma * qb ** mb / r4)) / math.pi
        return cache[key]
    return J


def g_of(d, J):
    """hitting probability of displacement d by one emission from the origin, averaged over the six faces (the face that
    points at d, blocked when d is a neighbour, contributes nothing) and over the cosine law"""
    tot = 0.0
    for k in range(6):
        if not reachable(d, k):
            continue
        D = np.array(d) - EK[k]
        ax = k // 2
        tr = [int(D[j]) for j in range(3) if j != ax]
        m = [abs(int(D[ax])), abs(tr[0]), abs(tr[1])]
        mult = math.factorial(sum(m)) // (math.factorial(m[0]) * math.factorial(m[1]) * math.factorial(m[2]))
        tot += (2 if tr[0] == 0 else 1) * (2 if tr[1] == 0 else 1) * mult * J(*m)
    return tot / 6


J80, J60 = make_J(80), make_J(60)
norm = 4 * J80(0, 0, 0)
gbar80 = sum(c * g_of(d, J80) for d, c in pairs.items()) / (257 * 256)
gbar60 = sum(c * g_of(d, J60) for d, c in pairs.items()) / (257 * 256)
f1 = 14 * gbar80
ok("A2", abs(norm - 1) < 1e-12 and abs(gbar80 - gbar60) < 1e-12,
   f"cosine law in simplex coordinates: dOmega cos(theta)/pi = (1/pi) q_n |q|^-4 d^2q, four octants sum to "
   f"{norm:.13f}; two-site function g(d) = (1/6) sum_k (octants) multinomial(D) J(D), D = d - e_k; its mean over the "
   f"ordered pairs of the ball is {gbar80:.12f} (80- and 60-point rules agree to 1e-12); first-order share for N = 15: "
   f"(N - 1) g_bar = {f1:.6f} (sum over the other sites; an upper bound: it counts every site a walk passes)")


# ------------------------------------------------------------------ A3: direct sampling of directed walks (+ exact DP)
@njit(cache=False)
def cosine_v(k):
    u = np.random.random()
    cn = np.sqrt(u)
    st = np.sqrt(1.0 - u)
    ph = 2 * np.pi * np.random.random()
    a = k // 2
    sg = 1.0 if k % 2 == 0 else -1.0
    v = np.zeros(3)
    v[a] = sg * cn
    v[(a + 1) % 3] = st * np.cos(ph)
    v[(a + 2) % 3] = st * np.sin(ph)
    return v


@njit(cache=False)
def walk(B, s0, v):
    """direct simulation of the directed walk; returns 1 if it steps onto a body site, 0 if it leaves the box"""
    G = B.shape[0]
    l1 = abs(v[0]) + abs(v[1]) + abs(v[2])
    y = s0.copy()
    while True:
        u = np.random.random() * l1
        j = 0 if u < abs(v[0]) else (1 if u < abs(v[0]) + abs(v[1]) else 2)
        y[j] += 1 if v[j] > 0 else -1
        if y[j] < 0 or y[j] >= G:
            return 0.0
        if B[y[0], y[1], y[2]]:
            return 1.0


@njit(cache=False)
def dp(B, s0, v):
    """exact first-passage probability of the body given the content (monotone paths)"""
    G = B.shape[0]
    sg = np.zeros(3, np.int64)
    p = np.zeros(3)
    n = np.zeros(3, np.int64)
    l1 = abs(v[0]) + abs(v[1]) + abs(v[2])
    for j in range(3):
        sg[j] = 1 if v[j] >= 0 else -1
        p[j] = abs(v[j]) / l1
        n[j] = (G - 1 - s0[j]) if sg[j] > 0 else s0[j]
    h = np.zeros((n[0] + 1, n[1] + 1, n[2] + 1))
    hit = 0.0
    for i0 in range(n[0] + 1):
        for i1 in range(n[1] + 1):
            for i2 in range(n[2] + 1):
                if i0 == 0 and i1 == 0 and i2 == 0:
                    inflow = 1.0
                else:
                    inflow = 0.0
                    if i0 > 0:
                        inflow += p[0] * h[i0 - 1, i1, i2]
                    if i1 > 0:
                        inflow += p[1] * h[i0, i1 - 1, i2]
                    if i2 > 0:
                        inflow += p[2] * h[i0, i1, i2 - 1]
                if B[s0[0] + sg[0] * i0, s0[1] + sg[1] * i1, s0[2] + sg[2] * i2]:
                    hit += inflow
                    h[i0, i1, i2] = 0.0
                else:
                    h[i0, i1, i2] = inflow
    return hit


@njit(cache=False)
def sample(ball, G, mode, N, fill, nsamp, seed):
    """mode 0: uniform N-subset of the ball; 1: each ball site with probability fill (N >= 3); 2: one site; 3: the whole
    ball (solid). One emission per body: random site, random FREE face, cosine-law content. Returns per sample
    (walk hit, DP hit, N)."""
    np.random.seed(seed)
    out = np.zeros((nsamp, 3))
    nb = ball.shape[0]
    for t in range(nsamp):
        B = np.zeros((G, G, G), np.bool_)
        if mode == 0:
            idx = np.random.permutation(nb)[:N]
        elif mode == 1:
            while True:
                sel = np.random.random(nb) < fill
                if sel.sum() >= 3:
                    break
            idx = np.nonzero(sel)[0]
        elif mode == 2:
            idx = np.array([np.random.randint(0, nb)])
        else:
            idx = np.arange(nb)
        for q in idx:
            B[ball[q, 0], ball[q, 1], ball[q, 2]] = True
        while True:
            x = ball[idx[np.random.randint(0, idx.shape[0])]]
            k = np.random.randint(0, 6)
            s0 = np.empty(3, np.int64)
            for j in range(3):
                s0[j] = x[j]
            s0[k // 2] += 1 if k % 2 == 0 else -1
            if not B[s0[0], s0[1], s0[2]]:
                break
        v = cosine_v(k)
        out[t, 0] = walk(B, s0, v)
        out[t, 1] = dp(B, s0, v)
        out[t, 2] = idx.shape[0]
    return out


G11 = 2 * R + 3
ball4 = np.array([(x + R + 1, y + R + 1, z + R + 1) for (x, y, z) in BALL], np.int64)
ball3 = np.array([(x + 5, y + 5, z + 5) for x in range(-3, 4) for y in range(-3, 4) for z in range(-3, 4)
                  if x * x + y * y + z * z <= 9], np.int64)
NS = 400000
res = {}
for name, (bl, G, mode, fill) in {'uniform N=15': (ball4, G11, 0, 0.0), 'Bernoulli 0.06': (ball4, G11, 1, 0.06),
                                   'one site': (ball4, G11, 2, 0.0), 'solid ball R=3': (ball3, 11, 3, 0.0)}.items():
    o = sample(bl, G, mode, 15, fill, NS, 20260923 + mode)
    w = o[:, 2] if mode == 1 else np.ones(NS)
    walk_m = (w * o[:, 0]).sum() / w.sum()
    dp_m = (w * o[:, 1]).sum() / w.sum()
    err = np.sqrt(((w * (o[:, 0] - walk_m)) ** 2).sum()) / w.sum()
    res[name] = (walk_m, err, dp_m)
agree = all(abs(a - c) < 4 * e + 1e-12 for a, e, c in res.values())
ok("A3", agree and res['one site'][0] == 0.0 and res['uniform N=15'][0] < f1,
   "direct sampling of the directed walks (" + f"{NS} emissions each; walk estimate, error, exact-DP estimate on the "
   "same emissions): " + "; ".join(f"{k}: {a:.4f} +- {e:.4f} (DP {c:.4f})" for k, (a, e, c) in res.items())
   + " - the Bernoulli line is capture weighted (weight N, the balanced capture rate is proportional to N); one site: no "
   "emission ever returns (A1)")

# ------------------------------------------------------------------ A4: the 40-tick window of the executed control
# hit mass by number of moves m and by content speed lambda = |v|_1/sqrt 3 (Bernoulli bodies, capture weighted), exact DP
@njit(cache=False)
def moves_hist(ball, G, fill, nb, per, seed, mmax, nl):
    np.random.seed(seed)
    H = np.zeros((mmax, nl))
    wsum = 0.0
    nball = ball.shape[0]
    for t in range(nb):
        while True:
            sel = np.random.random(nball) < fill
            if sel.sum() >= 3:
                break
        idx = np.nonzero(sel)[0]
        B = np.zeros((G, G, G), np.bool_)
        for q in idx:
            B[ball[q, 0], ball[q, 1], ball[q, 2]] = True
        N = idx.shape[0]
        for r in range(per):
            while True:
                x = ball[idx[np.random.randint(0, N)]]
                k = np.random.randint(0, 6)
                s0 = np.empty(3, np.int64)
                for j in range(3):
                    s0[j] = x[j]
                s0[k // 2] += 1 if k % 2 == 0 else -1
                if not B[s0[0], s0[1], s0[2]]:
                    break
            v = cosine_v(k)
            l1 = abs(v[0]) + abs(v[1]) + abs(v[2])
            lb = min(nl - 1, max(0, int((l1 / np.sqrt(3.0) - 0.55) / 0.06)))
            sg = np.zeros(3, np.int64)
            p = np.zeros(3)
            n = np.zeros(3, np.int64)
            for j in range(3):
                sg[j] = 1 if v[j] >= 0 else -1
                p[j] = abs(v[j]) / l1
                n[j] = (G - 1 - s0[j]) if sg[j] > 0 else s0[j]
            h = np.zeros((n[0] + 1, n[1] + 1, n[2] + 1))
            for i0 in range(n[0] + 1):
                for i1 in range(n[1] + 1):
                    for i2 in range(n[2] + 1):
                        if i0 == 0 and i1 == 0 and i2 == 0:
                            inflow = 1.0
                        else:
                            inflow = 0.0
                            if i0 > 0:
                                inflow += p[0] * h[i0 - 1, i1, i2]
                            if i1 > 0:
                                inflow += p[1] * h[i0, i1 - 1, i2]
                            if i2 > 0:
                                inflow += p[2] * h[i0, i1, i2 - 1]
                        if B[s0[0] + sg[0] * i0, s0[1] + sg[1] * i1, s0[2] + sg[2] * i2]:
                            m = i0 + i1 + i2
                            if m < mmax:
                                H[m, lb] += N * inflow / per
                            h[i0, i1, i2] = 0.0
                        else:
                            h[i0, i1, i2] = inflow
        wsum += N
    return H / wsum


H = moves_hist(ball4, G11, 0.06, 20000, 20, 7, 30, 8)
fH = H.sum()
lams = 0.55 + 0.06 * (np.arange(8) + 0.5)
TT = 40


def travel_cdf(extra):
    cdf = np.zeros(TT + 1)
    for m in range(H.shape[0]):
        for b in range(8):
            if H[m, b] > 0:
                cdf[1:] += H[m, b] * poisson.sf(m + extra - 1, lams[b] * np.arange(1, TT + 1))
    return cdf / fH


Ps, Pr = travel_cdf(1), travel_cdf(0)
shares = []
for pe in (0.62, 0.66, 0.70):
    W = np.zeros(TT + 1)
    Rr = np.zeros(TT + 1)
    E = np.zeros(TT + 1)
    S = 0.0
    for t in range(1, TT + 1):
        W[t] = 1 - fH * Ps[t - 1]
        Rr[t] = fH * sum(E[te] * (Pr[t - te] - Pr[t - te - 1]) for te in range(1, t))
        Sb = S + W[t] + Rr[t]
        E[t] = pe * Sb
        S = Sb - E[t]
    shares.append(Rr[1:].sum() / (W[1:] + Rr[1:]).sum())
sh = float(np.mean(shares))
mdist = H.sum(1) / fH
ok("A4", abs(fH - res['Bernoulli 0.06'][2]) < 0.002 and max(shares) - min(shares) < 0.002,
   f"40 ticks (floating point model): hits need m = 1, 2, 3, 4 moves with weights {mdist[1]:.3f}, {mdist[2]:.3f}, "
   f"{mdist[3]:.3f}, {mdist[4]:.3f}; moves arrive as a Poisson stream of rate |v|_1/sqrt 3 per tick; a stored record "
   f"leaves with probability 0.62-0.70 per tick; the shadow of the capture-only body forms with one more move. "
   f"Cumulative share over 40 ticks {sh:.4f} (steady {fH:.4f}); predicted push per capture 0.97 (1 - {sh:.4f}) = "
   f"{0.97 * (1 - sh):.3f}, executed 0.846 +- 0.032 (block 49 control, gamma = 0)")

label = "PARTIAL" if not FAILS else "PARTIAL (failed: " + ", ".join(FAILS) + ")"
print(f"SUMMARY: {label} (a) solved at gamma = 0 and small density: the own-emission share of a balanced body's captures "
      f"is the directed-walk hitting probability of its cosine-law emissions, {res['uniform N=15'][2]:.4f} for 15 sites "
      f"uniform in the radius-4 ball ({f1:.4f} at first order), {res['Bernoulli 0.06'][2]:.4f} for the executed bodies, "
      f"0 for one site; it gives the executed push 0.846 through the 40-tick window; (b), (c) are estimates in ATTEMPT.md "
      f"(scattered returns carry the local wind; the push follows the own-content share)")
if not FAILS:
    print(f"HIT: without scattering and at small density, a body in balance captures its own emissions with the "
          f"directed-walk hitting probability of the cosine law (never at its own site or a neighbour): the share is "
          f"{res['uniform N=15'][2]:.4f} for 15 sites uniform in the ball of radius 4 (first order 14 g_bar = {f1:.4f}), "
          f"{res['Bernoulli 0.06'][2]:.4f} capture weighted for the executed bodies and {res['solid ball R=3'][2]:.3f} for "
          f"the solid ball of radius 3 (lattice steps); since the wind captures equal the capture-only body's, the push "
          f"per capture is 0.97 (1 - share): 0.97 (1 - {sh:.4f}) = {0.97 * (1 - sh):.3f} over the 40-tick window, "
          f"executed 0.846 +- 0.032")
