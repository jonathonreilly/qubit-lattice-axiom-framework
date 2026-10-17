"""Items (1),(2),(5): code validity, anyon sector, statistics, energetics."""
AUDIT_TIMEOUT_SEC = 1800
import sys, itertools, numpy as np
from mj import *

def build(L):
    lat = Lat(L)
    g = generators(lat)
    names = []; gens = []
    for key in ['D', 'Pu', 'Pd', 'W']:
        for j, x in enumerate(g[key]):
            names.append((key, j)); gens.append(x)
    return lat, names, gens

def site_index(gens, N):
    touch = [[] for _ in range(N)]
    for gi, g in enumerate(gens):
        for s in np.nonzero(g[1])[0]: touch[s].append(gi)
    return touch

def synd_of(m, gens, touch):
    """syndrome bitmask (python int over generators) of monomial masks m"""
    out = 0
    for s in np.nonzero(m)[0]:
        for gi in touch[s]:
            if anticomm_site(int(m[s]), int(gens[gi][1][s])):
                out ^= 1 << gi
    return out

class F2Span:
    def __init__(s): s.piv = {}
    def add(s, v):
        while v:
            p = v.bit_length() - 1
            if p in s.piv: v ^= s.piv[p]
            else: s.piv[p] = v; return True
        return False
    def contains(s, v):
        while v:
            p = v.bit_length() - 1
            if p in s.piv: v ^= s.piv[p]
            else: return False
        return True

def main():
    res = []
    for L in [4, 6]:
        lat, names, gens = build(L)
        G = StabGroup(gens)
        ncomm = G.commuting()
        nbad = G.check_no_minus_one()
        k = 5 * lat.N - G.rank
        print(f'L={L}: gens={len(gens)} anticommuting pairs={ncomm} relations={len(G.relations)} '
              f'relations with -1={nbad} rank={G.rank} log2dim={k}')
        res.append((L, ncomm, nbad, k))
    # odd L sanity
    lat, names, gens = build(3)
    G = StabGroup(gens)
    print(f'L=3: anticommuting pairs={G.commuting()} relations with -1={G.check_no_minus_one()} log2dim={5*lat.N-G.rank}')

    L = 6
    lat, names, gens = build(L)
    N = lat.N; touch = site_index(gens, N)
    nm = {n: i for i, n in enumerate(names)}
    v0 = (2, 2, 2); s0 = lat.idx(v0)
    def single(site, k):
        m = np.zeros(N, dtype=np.int64); m[site] = 1 << k; return m
    def show(sy):
        return [names[i] for i in range(len(gens)) if sy >> i & 1]
    print('syndrome chi6(v):', show(synd_of(single(s0, 6), gens, touch)))
    print('syndrome chi8(v):', show(synd_of(single(s0, 8), gens, touch)))
    print('syndrome b_{v,+x}:', show(synd_of(single(s0, 0), gens, touch)))
    # local operator span in radius-2 (L_inf) ball around v0
    span = F2Span()
    for dv in itertools.product(range(-2, 3), repeat=3):
        s = lat.idx(np.add(v0, dv))
        for k in range(10):
            span.add(synd_of(single(s, k), gens, touch))
    tgt = {
        'P_up(v) alone': 1 << nm[('Pu', s0)],
        'D(v) alone': 1 << nm[('D', s0)],
        'P_up(v)+P_dn(v)': (1 << nm[('Pu', s0)]) | (1 << nm[('Pd', s0)]),
        'P_up(v)+D(v)': (1 << nm[('Pu', s0)]) | (1 << nm[('D', s0)]),
    }
    flux = synd_of(single(s0, 0), gens, touch) ^ (1 << nm[('D', s0)])
    tgt['4 W around edge (v,+x) alone'] = flux
    tgt['4 W around edge + D(v)'] = flux | (1 << nm[('D', s0)])
    tgt['4 W around edge + P_up(v)'] = flux | (1 << nm[('Pu', s0)])
    for k_, t in tgt.items():
        print(f'  locally creatable in radius-2 ball: {k_:32s} {span.contains(t)}')
    # up <-> down local converter: c_dn^dag c_up ~ Majorana bilinears chi8 chi6 etc
    m = np.zeros(N, dtype=np.int64); m[s0] = (1 << 6) | (1 << 8)
    print('syndrome chi6 chi8 (up<->dn converter piece):', show(synd_of(m, gens, touch)))
    # gauge-dressed hop chi6(v) u_e chi6(w)
    for a in range(3):
        w = list(v0); w[a] += 1
        h = mul(mul(mono(N, [(s0, 6)]), u_edge(lat, v0, a)), mono(N, [(lat.idx(w), 6)]))
        print(f'hop along {DIRS[a]} syndrome:', show(synd_of(h[1], gens, touch)))
    # Levin-Wen T-junction, legs of length 2 from v0, all 20 triples
    def leg(d):
        """hermitian operator moving an up-matter excitation from v0+2d to v0"""
        op = mono(N, [(s0, 6)])
        v = v0
        for step in range(2):
            w = tuple(np.add(v, DIRS[d]))
            a = d % 3
            if d < 3: op = mul(op, u_edge(lat, v, a))
            else: op = mul(op, u_edge(lat, w, a))
            v = w
        op = mul(op, mono(N, [(lat.idx(v), 6)]))
        return op
    thetas = []
    for tri in itertools.combinations(range(6), 3):
        A, B, Cc = [leg(d) for d in tri]
        # check each leg flips only P_up at its two ends
        for l in (A, B, Cc):
            assert len(show(synd_of(l[1], gens, touch))) == 2
        # W_c W_b^-1 W_a W_c^-1 W_b W_a^-1 with W^-1 = W^dag
        prod = (1.0 + 0j, np.zeros(N, dtype=np.int64))
        for op in [Cc, dagger(B), A, dagger(Cc), B, dagger(A)]:
            prod = mul(prod, op)
        assert not prod[1].any()
        thetas.append(prod[0])
    print('T-junction phases over 20 triples:', sorted({complex(np.round(t, 9)) for t in thetas}), 'count', len(thetas))
    # also with the dn Majorana chi8 and mixed hop chi6 ... chi6
    # Energetics: charged-sector representatives
    print('\nEnergetics of charged-sector representatives (H = -K D - J W - mu (P_up+P_dn)):')
    print('  P_up flip (matter doublet member): 2 mu')
    print('  D flip (bare gauge charge):        2 K')
    print('  4-plaquette flux loop (charged, see above): 8 J')
    print('  => lowest charged excitation is the doublet iff mu < K and mu < 4 J')

if __name__ == '__main__':
    main()
