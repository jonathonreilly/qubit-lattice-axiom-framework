"""exact stationarity of the law with vacancies mu ~ z^n prod_{adjacent} W under inertial clauses (six-axis menu)."""
import itertools, sys, time
from fractions import Fraction as F
E = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]          # content d; d^1 = opposite
M6 = range(6)
def Wmat(p, q, r, c):
    return [[c * (p if a == b else q if a == (b ^ 1) else r) for b in M6] for a in M6]
def nbrs(x, L):
    return [tuple((x[i] + E[d][i]) % L for i in range(3)) for d in M6]
def mu(cfg, W, L):
    val = F(1)
    for x, d in cfg.items():
        for y in nbrs(x, L):
            if y in cfg and x < y: val *= W[d][cfg[y]]
    return val
def what(cfg, x, W, L):
    """departure weight of the record at x: product of its pair weights"""
    val = F(1)
    for y in nbrs(x, L):
        if y in cfg: val *= W[cfg[x]][cfg[y]]
    return val
def events(cfg, W, L, rule, gamma):
    out = []
    for x, d in cfg.items():
        y = tuple((x[i] + E[d][i]) % L for i in range(3))
        rate = F(1) if rule == "plain" else 1 / what(cfg, x, W, L)
        new = dict(cfg)
        if y not in cfg:
            del new[x]; new[y] = d
        else:
            new[x], new[y] = cfg[y], d                                  # exchange = pass-through
        out.append((rate, new))
    if gamma:
        # scattering: each adjacent pair re-drawn on its momentum class with heat-bath weights mu(new) (detailed balance)
        seen = set()
        for x in cfg:
            for y in nbrs(x, L):
                if y in cfg and (y, x) not in seen:
                    seen.add((x, y))
                    a, b = cfg[x], cfg[y]
                    cls = [(e, e ^ 1) for e in M6] if b == a ^ 1 else ([(a, b), (b, a)] if a != b else [(a, a)])
                    cands = []
                    for (u, v) in cls:
                        new = dict(cfg); new[x], new[y] = u, v
                        cands.append((mu(new, W, L), new))
                    tot = sum(m for m, _ in cands)
                    for m, new in cands:
                        out.append((gamma * m / tot, new))
    return out
def check(L, n, W, rule, gamma=F(0), limit=None):
    sites = list(itertools.product(range(L), repeat=3))
    inflow, outflow, weight = {}, {}, {}
    cnt = 0
    for occ in itertools.combinations(sites, n):
        for contents in itertools.product(M6, repeat=n):
            cfg = dict(zip(occ, contents)); key = tuple(sorted(cfg.items()))
            m = mu(cfg, W, L); weight[key] = m; cnt += 1
            for rate, new in events(cfg, W, L, rule, gamma):
                k2 = tuple(sorted(new.items()))
                inflow[k2] = inflow.get(k2, 0) + m * rate
                outflow[key] = outflow.get(key, 0) + m * rate
    bad = [k for k in outflow if inflow.get(k, 0) != outflow[k]]
    return cnt, bad, inflow, outflow
if False:
    L, n = int(sys.argv[1]), int(sys.argv[2])
    W = Wmat(5, 1, 2, F(6, 5 + 1 + 8))                                 # (p,q,r) = (5,1,2) at the pinned scale c0 = 6/(p+q+4r)
    for rule in ("plain", "departure"):
        for gamma in (F(0), F(1)):
            t0 = time.time()
            cnt, bad, inf, outf = check(L, n, W, rule, gamma)
            print(f"L={L} n={n} rule={rule} gamma={gamma}: {cnt} configurations, {len(bad)} unbalanced ({time.time()-t0:.0f}s)", flush=True)
            if bad and rule == "departure":
                k = bad[0]; print("   e.g.", k, "in", inf.get(k), "out", outf[k])
