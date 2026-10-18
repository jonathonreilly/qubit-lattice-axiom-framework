"""R2: independent Monte Carlo for Theorem C (neighbour-dependent rates).

Different method from the author: the record field is computed by a FORWARD
time-ordered event simulation of the thinned Poisson construction on a finite
window (no backward recursion).  Separately, the reach C(0) is computed by a
breadth-first search over ALL backward chains (revisits allowed).  Tests:
 (a) determinacy / cutoff / blank-boundary: resampling, or adversarially
     replacing, all data outside B(0, rho+1) never changes xi_0 (forward sim);
     a control shows resampling outside B(0, rho-1) DOES sometimes change xi_0,
     so the test has power;
 (b) loop erasure on Z: the site- and point-reach of all chains equals that of
     straight (self-avoiding on Z) chains;
 (c) tail: P(rho>=n) <= D(D-1)^(n-1) kappa^(n+1)/(n+1)!;
 (d) C1: E[# straight chains 0..n] = kappa^(n+1)/(n+1)! (4 SE).
Points generated per site are exactly the relevant points (up to and incl.
the first sure point); later points are inert because tau_x <= sigma_x.
The forward simulation ALSO uses inert-free data, so for (a) we additionally
run a forward sim with extra post-sigma points to confirm inertness.
Rule (menu {0,1}): rate = lmin*(1+(kappa-1)*#{formed nbrs with content 1}/D);
content = XOR of formed nbr contents if any, else bit(U<1/2).
"""
import math, random
from rv_common import Checks
C = Checks("r2")

def gen_site(rng, lmax, kappa, extra=False):
    pts, t = [], 0.0
    while True:
        t += rng.expovariate(lmax)
        V, U = rng.random(), rng.random()
        pts.append((t, V, U))
        if V <= 1.0 / kappa:
            break
    if extra:   # inert points after sigma
        for _ in range(3):
            t += rng.expovariate(lmax); pts.append((t, rng.random(), rng.random()))
    return pts

def nbrs(x, d):
    if d == 1:
        return [x-1, x+1]
    a, b = x
    return [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]

def dist(x, d):
    return abs(x) if d == 1 else abs(x[0]) + abs(x[1])

def forward(data, d, kappa, lmin):
    D = 2*d
    lmax = kappa*lmin
    ev = sorted((t, x, V, U) for x, pts in data.items() for (t, V, U) in pts)
    rec = {}
    for t, x, V, U in ev:
        if x in rec: continue
        f = [rec[y] for y in nbrs(x, d) if y in rec]
        lam = lmin*(1 + (kappa-1)*sum(f)/D)
        if V <= lam/lmax:
            if f:
                v = 0
                for s in f: v ^= s
            else:
                v = 1 if U < 0.5 else 0
            rec[x] = v
    return rec

def reach(data, d, origin):
    # BFS over space-time points; all backward chains (revisits allowed)
    start = [(origin, t) for (t, V, U) in data[origin]]
    seen = set(start); stack = list(start)
    while stack:
        y, t = stack.pop()
        for z in nbrs(y, d):
            if z not in data: continue
            for (s, V, U) in data[z]:
                if s < t and (z, s) not in seen:
                    seen.add((z, s)); stack.append((z, s))
    return seen

def straight_reach(data):
    pts = set()
    for direc in (1, -1):
        frontier = [t for (t, V, U) in data[0]]
        pts |= {(0, t) for t in frontier}
        k = 0
        while frontier:
            k += direc
            if k not in data: break
            mx = max(frontier)
            frontier = [s for (s, V, U) in data[k] if s < mx]
            pts |= {(k, s) for s in frontier}
    return pts

def window(d, Wr):
    if d == 1: return list(range(-Wr, Wr+1))
    return [(a, b) for a in range(-Wr, Wr+1) for b in range(-Wr, Wr+1) if abs(a)+abs(b) <= Wr]

def bound(n, D, kappa):
    return D*(D-1)**(n-1)*kappa**(n+1)/math.factorial(n+1)

def run(d, kappa, Wr, N, seed, do_straight):
    rng = random.Random(seed)
    lmin = 1.0; lmax = kappa*lmin; D = 2*d
    sites = window(d, Wr)
    rhos = []; viol = 0; ctrl_changes = 0; ctrl_tests = 0; inert_viol = 0
    lo_viol = 0; edge = 0
    nchain = {n: [] for n in range(1, 6)}
    for it in range(N):
        data = {x: gen_site(rng, lmax, kappa) for x in sites}
        R = reach(data, d, 0 if d == 1 else (0, 0))
        rho = max(dist(y, d) for (y, t) in R)
        if rho + 2 >= Wr:
            edge += 1; continue
        rhos.append(rho)
        o = 0 if d == 1 else (0, 0)
        xi = forward(data, d, kappa, lmin)[o]
        # (a) resample outside B(0, rho+1), twice; plus adversarial: exterior sites get one early sure point
        for mode in range(3):
            d2 = {}
            for x in sites:
                if dist(x, d) <= rho + 1: d2[x] = data[x]
                elif mode < 2: d2[x] = gen_site(rng, lmax, kappa, extra=(mode == 1))
                else: d2[x] = [(1e-9*rng.random(), 0.0, rng.random())]
            if forward(d2, d, kappa, lmin)[o] != xi: viol += 1
        # inert points inside the ball too
        d3 = {x: list(p) for x, p in data.items()}
        for x in sites:
            t = d3[x][-1][0]
            d3[x] = d3[x] + [(t + 0.1 + rng.random(), rng.random(), rng.random())]
        if forward(d3, d, kappa, lmin)[o] != xi: inert_viol += 1
        # control: resample outside B(0, rho-1) -> should change sometimes
        if rho >= 1:
            ctrl_tests += 1
            d4 = {x: (data[x] if dist(x, d) <= rho - 1 else gen_site(rng, lmax, kappa)) for x in sites}
            if forward(d4, d, kappa, lmin)[o] != xi: ctrl_changes += 1
        if do_straight:
            if straight_reach(data) != R: lo_viol += 1
            # count straight chains 0..n (rightwards) by DP
            for n in nchain:
                cnt = [1]*len(data[0]); prev = [t for (t, V, U) in data[0]]
                for k in range(1, n+1):
                    cur = [s for (s, V, U) in data[k]]
                    cnt = [sum(c for (c, t) in zip(cnt, prev) if s < t) for s in cur]
                    prev = cur
                nchain[n].append(sum(cnt))
    tag = f"d={d} kappa={kappa} N={len(rhos)}"
    C.ok(f"{tag}: resampled/adversarial exterior outside B(0,rho+1) never changes xi_0 (forward sim): violations={viol}", viol == 0)
    C.ok(f"{tag}: adding post-sigma points (inert) never changes xi_0: violations={inert_viol}", inert_viol == 0)
    C.ok(f"{tag}: control has power: resampling outside B(0,rho-1) changed xi_0 in {ctrl_changes}/{ctrl_tests} samples", ctrl_changes > 0)
    C.ok(f"{tag}: edge-discarded samples {edge} <= 1%", edge <= 0.01*N)
    n_max = max(rhos)
    for n in range(1, n_max+1):
        p = sum(r >= n for r in rhos)/len(rhos)
        se = math.sqrt(max(p*(1-p), 1e-12)/len(rhos))
        b = bound(n, D, kappa)
        if b < 1.0:
            C.ok(f"{tag}: P(rho>={n}) = {p:.4f} (SE {se:.4f}) <= bound {b:.4f}", p <= b + 4*se)
    if do_straight:
        C.ok(f"{tag}: all-chain point reach == straight-chain point reach in every sample (loop erasure, Z): failures={lo_viol}", lo_viol == 0)
        for n, v in nchain.items():
            m = sum(v)/len(v); s = math.sqrt(sum((x-m)**2 for x in v)/(len(v)-1)/len(v))
            ex = kappa**(n+1)/math.factorial(n+1)
            C.ok(f"{tag}: E[#rightward chains of length {n}] = {m:.4f} +- {s:.4f} vs kappa^(n+1)/(n+1)! = {ex:.4f}", abs(m-ex) <= 4*s)

run(1, 4.0, 40, 3000, 1, True)
run(1, 7.0, 60, 1500, 2, True)
run(2, 3.0, 14, 300, 3, False)
C.done()
