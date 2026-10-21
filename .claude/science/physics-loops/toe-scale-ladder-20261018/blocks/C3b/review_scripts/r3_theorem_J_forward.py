"""Reviewer r3: Theorem J by FORWARD event simulation (time-ordered), independent of the author's code.

Model on an open box [-W,W]^2: Poisson points rate lam_max=1 per site on [0,Tm], marks (V,U), iid seeds (p=0.3).
Acceptance at a point (x,s) of a blank site: V <= lam(x,s,history), with
  seed:     lam = 0.6
  non-seed: lam = 0 if no neighbour formed before s (so lam_min = 0);
            else lam = min(1,(s - first nbr formation)/0.5) * (0.4+0.6*frac of formed nbrs with content 1) * (0.75+0.25 cos s)
  -> history (age) dependent, content dependent, time-inhomogeneous.
Content: seed -> (U<.5); else content of earliest-formed nbr XOR (U < 0.15 + 0.05*#formed nbrs).
Reach: space-time BFS from the points of site 0 with t <= tau_0 over ALL points of neighbours with smaller time
(any point, no relevance cutoff), rho = max graph distance of reached sites.
Tests: (1) resampling ALL data at distance > rho+1 (fresh, and adversarial: early sure seeds) never changes
(tau_0, xi_0); (2) power control: resampling at distance > rho-1 sometimes does; (3) J2 tail bound
P(rho >= n) <= P(tau_0 > t) + c_n t^(n+1)/(n+1)! (lam_max=1); (4) J3: no seeds -> nothing forms.
"""
import heapq, math
import numpy as np
from rv_common import check, total

rng = np.random.default_rng(9090)
W = 12
Tm = 25.0
coords = [(i, j) for i in range(-W, W + 1) for j in range(-W, W + 1)]
sid = {c: k for k, c in enumerate(coords)}
NB = [[sid[(i + a, j + b)] for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (i + a, j + b) in sid] for (i, j) in coords]
dist = np.array([abs(i) + abs(j) for (i, j) in coords])
N = len(coords)
O = sid[(0, 0)]


def gen_site(seedp=0.3):
    k = rng.poisson(Tm)
    t = np.sort(rng.random(k) * Tm)
    return dict(t=t, V=rng.random(k), U=rng.random(k), seed=rng.random() < seedp)


def simulate(data):
    tau = np.full(N, np.inf); con = np.zeros(N, np.int8)
    ev = [(d['t'][m], x, m) for x, d in enumerate(data) for m in range(len(d['t']))]
    heapq.heapify(ev)
    while ev:
        s, x, m = heapq.heappop(ev)
        if tau[x] < np.inf:
            continue
        d = data[x]
        fn = [y for y in NB[x] if tau[y] < s]
        if d['seed']:
            lam = 0.6
        elif not fn:
            lam = 0.0
        else:
            first = min(tau[y] for y in fn)
            frac1 = sum(con[y] for y in fn) / len(NB[x])
            lam = min(1.0, (s - first) / 0.5) * (0.4 + 0.6 * frac1) * (0.75 + 0.25 * math.cos(s))
        if d['V'][m] <= lam:
            tau[x] = s
            if d['seed']:
                con[x] = 1 if d['U'][m] < 0.5 else 0
            else:
                ye = min(fn, key=lambda y: tau[y])
                con[x] = con[ye] ^ (1 if d['U'][m] < 0.15 + 0.05 * len(fn) else 0)
    return tau, con


def reach(data, t0max):
    start = [(O, t) for t in data[O]['t'] if t <= t0max]
    seen = set(start); st = list(start); sites = {O}
    while st:
        y, t = st.pop()
        for z in NB[y]:
            for u in data[z]['t']:
                if u < t and (z, u) not in seen:
                    seen.add((z, u)); st.append((z, u)); sites.add(z)
    return max(dist[s] for s in sites)


def resample(data, rad, adversarial=False):
    new = list(data)
    for x in range(N):
        if dist[x] > rad:
            if adversarial:
                new[x] = dict(t=np.array([1e-3 * (1 + rng.random())]), V=np.array([0.0]), U=rng.random(1), seed=True)
            else:
                new[x] = gen_site()
    return new


ns, used, ch_out, ch_pow, pow_trials = 400, 0, 0, 0, 0
rhos, taus = [], []
for it in range(ns):
    data = [gen_site() for _ in range(N)]
    tau, con = simulate(data)
    if not np.isfinite(tau[O]):
        rhos.append(None); taus.append(np.inf); continue
    rho = reach(data, tau[O])
    rhos.append(rho); taus.append(tau[O])
    if rho + 2 > W:
        continue
    used += 1
    for adv in (False, True):
        t2, c2 = simulate(resample(data, rho + 1, adv))
        if t2[O] != tau[O] or c2[O] != con[O]:
            ch_out += 1
    if rho >= 2:
        pow_trials += 1
        t3, c3 = simulate(resample(data, rho - 1, True))
        if t3[O] != tau[O] or c3[O] != con[O]:
            ch_pow += 1
check("j1 (tau_0, xi_0) unchanged when all data beyond rho+1 is resampled (fresh + adversarial)", ch_out == 0 and used >= 100,
      f"{ch_out} changes in {2*used} resamples")
check("j2 power control: adversarial resampling beyond rho-1 changes (tau_0, xi_0) in some samples", ch_pow > 0,
      f"{ch_pow}/{pow_trials}")
# J2 tail
cn = [1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100, 120292]
R = np.array([r if r is not None else 99 for r in rhos]); TT = np.array(taus)
ok = True; rep = []
for n in range(2, 11):
    p = (R >= n).mean(); se = math.sqrt(max(p * (1 - p), 1e-4) / len(R))
    best = min((TT > t).mean() + cn[n] * t ** (n + 1) / math.factorial(n + 1) for t in np.linspace(0.2, 30, 150))
    ok &= p - 4 * se <= best
    rep.append(f"n={n}: P={p:.3f} bound={best:.3f}")
check("j3 P(rho>=n) <= min_t [P(tau_0>t) + c_n t^(n+1)/(n+1)!], n=2..10", ok, "; ".join(rep[::3]))
data = [gen_site(0.0) for _ in range(N)]
tau, _ = simulate(data)
check("j4 J3: lam=0 on empty history, no seeds -> no site forms", np.all(~np.isfinite(tau)))
total()
