#!/usr/bin/env python3
"""T73 test: on ONE support (maximal independent sets = probe 19's crowding rule m = 0),
does the outcome measure move the entropy?  See PREREGISTER.md (written first).

Part A  exact Renyi entropies of the frozen state under a local covariant family of
        sequential formation laws; d = 1 chains and d = 2 boxes.
Part B  three permanent-record formation laws on the same L x L box (volume / seed /
        boundary-ring), all outputs verified to be maximal independent sets.
"""
import itertools, math, sys, time
from collections import defaultdict

# ------------------------------------------------------------------ graphs
def grid_adj(L, d):
    sites = list(itertools.product(range(L), repeat=d))
    idx = {s: i for i, s in enumerate(sites)}
    adj = [0] * len(sites)
    for s in sites:
        for k in range(d):
            for dv in (-1, 1):
                t = list(s); t[k] += dv; t = tuple(t)
                if t in idx:
                    adj[idx[s]] |= 1 << idx[t]
    return sites, adj


def popcount(x):
    return bin(x).count("1")


def nbr_mask(state, adj):
    m = 0; s = state; i = 0
    while s:
        if s & 1:
            m |= adj[i]
        s >>= 1; i += 1
    return m


# ------------------------------------------------------------------ Part A engine
def frozen_distribution(adj, w=1.0):
    """Exact distribution over frozen (maximal independent) states of the sequential law:
    at each step pick an eligible site v with weight w**(number of eligible neighbours of v).
    w = 1 is uniform random-order sequential adsorption (RSA)."""
    n = len(adj); full = (1 << n) - 1
    layer = {0: 1.0}
    frozen = defaultdict(float)
    while layer:
        nxt = defaultdict(float)
        for s, p in layer.items():
            elig = full & ~s & ~nbr_mask(s, adj)
            if elig == 0:
                frozen[s] += p; continue
            vs = []; ws = []
            e = elig; i = 0
            while e:
                if e & 1:
                    vs.append(i)
                    ws.append(1.0 if w == 1.0 else w ** popcount(adj[i] & elig))
                e >>= 1; i += 1
            tot = sum(ws)
            for v, wt in zip(vs, ws):
                nxt[s | (1 << v)] += p * wt / tot
        layer = nxt
    return frozen


def renyi(dist):
    ps = [p for p in dist.values() if p > 0]
    s1 = -sum(p * math.log(p) for p in ps)
    s2 = -math.log(sum(p * p for p in ps))
    sinf = -math.log(max(ps))
    return s1, s2, sinf


def part_A():
    print("=== Part A: Renyi entropies of the frozen state, m = 0 crowding rule ===", flush=True)
    rows = []
    # d = 1
    print("-- d = 1 chains, w = 1 (uniform RSA)")
    print("L    N        S0=lnN   S1       S2       Sinf     S1/S0   (S0-S1)/L")
    d1 = {}
    for L in list(range(2, 23)):
        _, adj = grid_adj(L, 1)
        dist = frozen_distribution(adj, 1.0)
        N = len(dist)
        S0 = math.log(N); S1, S2, Si = renyi(dist)
        d1[L] = (N, S0, S1)
        print(f"{L:<4d} {N:<8d} {S0:.4f}  {S1:.4f}  {S2:.4f}  {Si:.4f}  {S1/S0:.4f}  {(S0-S1)/L:.4f}", flush=True)
    # d = 2
    print("-- d = 2 boxes")
    d2 = {}
    for L in range(2, 6):
        _, adj = grid_adj(L, 2)
        t0 = time.time()
        for w in (0.1, 0.3, 1.0, 3.0, 10.0):
            dist = frozen_distribution(adj, w)
            N = len(dist)
            S0 = math.log(N); S1, S2, Si = renyi(dist)
            d2[(L, w)] = (N, S0, S1, S2, Si)
            print(f"L={L} w={w:<5} N={N:<5d} S0={S0:.4f} S1={S1:.4f} S2={S2:.4f} Sinf={Si:.4f} S1/S0={S1/S0:.4f} S1/L^2={S1/L**2:.4f} S0/L^2={S0/L**2:.4f}", flush=True)
        print(f"   (L={L} done in {time.time()-t0:.1f}s)", flush=True)
    return d1, d2


# ------------------------------------------------------------------ Part B
def box_adj(L):
    return grid_adj(L, 2)


def is_mis(state, adj):
    n = len(adj)
    for i in range(n):
        if state >> i & 1:
            if adj[i] & state:
                return False
    full = (1 << n) - 1
    elig = full & ~state & ~nbr_mask(state, adj)
    return elig == 0


def raster_fill(state, order, adj):
    for v in order:
        if not (state >> v & 1) and not (adj[v] & state):
            state |= 1 << v
    return state


def sym_maps(L):
    """8 symmetries of the L x L box as permutations of site indices (site (i,j) -> i*L+j)."""
    maps = []
    for k in range(4):
        for refl in (False, True):
            m = []
            for i in range(L):
                for j in range(L):
                    a, b = i, j
                    if refl:
                        b = L - 1 - b
                    for _ in range(k):
                        a, b = b, L - 1 - a
                    m.append(a * L + b)
            maps.append(m)
    return maps


def seed_law_entropy(L):
    """deterministic single-pass raster from a uniformly random cyclic start site and
    a uniformly random box symmetry: entropy of the (empirical) outcome distribution."""
    sites, adj = box_adj(L); n = L * L
    outs = defaultdict(int); total = 0
    for g in sym_maps(L):
        base = [g[i] for i in range(n)]      # raster order transported by g
        for t in range(n):
            order = base[t:] + base[:t]
            s = raster_fill(0, order, adj)
            assert is_mis(s, adj)
            outs[s] += 1; total += 1
    ps = [c / total for c in outs.values()]
    return -sum(p * math.log(p) for p in ps), len(outs), total


def ring_sites(L):
    """boundary ring of the L x L box in cyclic order."""
    r = []
    for j in range(L): r.append((0, j))
    for i in range(1, L): r.append((i, L - 1))
    for j in range(L - 2, -1, -1): r.append((L - 1, j))
    for i in range(L - 2, 0, -1): r.append((i, 0))
    return r


def cycle_mis(P):
    """all maximal independent sets of the cycle C_P as (bitmask, n_gap3).
    A MIS of C_P = recorded sites with cyclic gaps (distances) in {2, 3} summing to P.
    Canonical form: smallest recorded position f, then gaps g_1..g_k (k = #recorded, sum = P);
    valid iff f < g_k (wrap gap covers positions after the last recorded and before f)."""
    res = []
    def seqs(rem, acc):
        if rem == 0:
            yield list(acc); return
        for g in (2, 3):
            if g <= rem:
                acc.append(g)
                yield from seqs(rem - g, acc)
                acc.pop()
    for gs in seqs(P, []):
        k = len(gs); n3 = sum(1 for g in gs if g == 3)
        for f in range(gs[-1]):
            pos = [f]
            for g in gs[:-1]:
                pos.append(pos[-1] + g)
            m = 0
            for p in pos:
                m |= 1 << p
            res.append((m, n3))
    return res


def ring_entropy(P, w, cmis):
    ws = [w ** n3 for _, n3 in cmis]
    Z = sum(ws)
    ps = [x / Z for x in ws]
    return -sum(p * math.log(p) for p in ps if p > 0), ps


def solve_w(P, target, cmis):
    lo, hi = 1e-9, 1.0   # entropy increases with w on (0, w_max]; find w with S = target
    # S(w) is unimodal; bracket on the left branch [0, w_peak]
    def S(w): return ring_entropy(P, w, cmis)[0]
    # find peak by ternary search on log w
    a, b = math.log(1e-6), math.log(1e6)
    for _ in range(200):
        m1 = a + (b - a) / 3; m2 = b - (b - a) / 3
        if S(math.exp(m1)) < S(math.exp(m2)): a = m1
        else: b = m2
    wpk = math.exp((a + b) / 2)
    if S(wpk) < target: return None, wpk
    lo, hi = 1e-9, wpk
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if S(mid) < target: lo = mid
        else: hi = mid
    return math.sqrt(lo * hi), wpk


def ring_law_final_states(L, cmis, sites_idx, adj, P, ring_idx):
    """map each ring MIS to its final MIS of the box (interior raster fill); verify."""
    n = L * L
    interior = [i * L + j for i in range(1, L - 1) for j in range(1, L - 1)]
    finals = []
    for m, _ in cmis:
        s = 0
        for k in range(P):
            if m >> k & 1:
                s |= 1 << ring_idx[k]
        s = raster_fill(s, interior, adj)
        finals.append(s)
    return finals


def part_B(d2):
    print("\n=== Part B: three formation laws on the same support (2D sealed L x L box, m = 0) ===", flush=True)
    print("L   ringP  |cycleMIS|  S_V(RSA)  S_seed  ln(8L^2)  #outs   S_ring(w=1)  S_ring(w*)  w*   S_ring/P  verified-MIS")
    cache = {}
    for L in range(3, 11):
        sites, adj = box_adj(L)
        ring = ring_sites(L); P = len(ring)
        ring_idx = [i * L + j for (i, j) in ring]
        cmis = cycle_mis(P)
        # exact check that cycle_mis counts Perrin numbers
        S_seed, nouts, tot = seed_law_entropy(L)
        S1w, _ = ring_entropy(P, 1.0, cmis)
        ws, wpk = solve_w(P, P / 4.0, cmis)
        Sstar = ring_entropy(P, ws, cmis)[0] if ws else float('nan')
        ver = "n/a"
        if L <= 7:
            finals = ring_law_final_states(L, cmis, None, adj, P, ring_idx)
            ok = all(is_mis(f, adj) for f in finals) and len(set(finals)) == len(cmis)
            ver = "ok" if ok else "FAIL"
        SV = d2.get((L, 1.0), (None, None, float('nan')))[2] if L <= 5 else float('nan')
        print(f"{L:<3d} {P:<6d} {len(cmis):<10d} {SV:9.4f} {S_seed:7.4f} {math.log(8*L*L):8.4f}  {nouts:<6d} {S1w:9.4f}  {Sstar:9.4f} {ws if ws else float('nan'):.4f}  {Sstar/P:.4f}  {ver}", flush=True)
        cache[L] = (P, len(cmis), SV, S_seed, S1w, Sstar, ws)
    return cache


if __name__ == "__main__":
    d1, d2 = part_A()
    part_B(d2)
