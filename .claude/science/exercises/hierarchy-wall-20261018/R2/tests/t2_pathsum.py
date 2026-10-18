"""T2: exact leading-order tunnelling coefficient for minimal flips, and the
second-order diagonal detuning.

Model (declared): H = J * sum_r [star(r) not in A] + eps * sum_r X_r.
For two valid configurations c and c xor 1_S with S a minimal flip (n = |S|),
the leading effective amplitude is t = (-1)^(n-1) C_n eps^n / J^(n-1), with
C_n = sum over the n! orderings of prod_{k=1}^{n-1} 1/E(T_k), E(T) = number of
violated stars of c xor 1_T.  Computed by a subset DP (exact, float64).
Second order: E2(c) = -eps^2/J * sum_r 1/E_r(c), E_r = violations after one
flip at r.  Detuning D2 = E2(c xor S) - E2(c) (local sum; differences vanish far
from S).
"""
import sys, itertools, math, time
import numpy as np
import numba
import t1_minflip as T


@numba.njit(cache=False)
def dp(n, ncent, base_cfg, plen, ppos_i, ppos_j, orbarr, bad):
    N = 1 << n
    g = np.zeros(N, dtype=np.float64)
    Emin_layer = np.full(n + 1, 10 ** 9, dtype=np.int64)
    zero_count = 0
    g[0] = 1.0
    full = N - 1
    for Tm in range(1, N):
        s = 0.0
        for i in range(n):
            if (Tm >> i) & 1:
                s += g[Tm ^ (1 << i)]
        if Tm == full:
            g[Tm] = s
            break
        E = 0
        for c in range(ncent):
            m = base_cfg[c]
            for q in range(plen[c]):
                if (Tm >> ppos_i[c, q]) & 1:
                    m ^= 1 << ppos_j[c, q]
            E += bad[orbarr[m]]
        k = 0
        x = Tm
        while x:
            k += x & 1
            x >>= 1
        if E < Emin_layer[k]:
            Emin_layer[k] = E
        if E == 0:
            zero_count += 1
            g[Tm] = 0.0
        else:
            g[Tm] = s / E
    return g[full], Emin_layer, zero_count


def setup(base, S, A, orb):
    S = [tuple(s) for s in S]
    idx = {s: i for i, s in enumerate(S)}
    cents = sorted({t for s in S for t in T.star_sites(s)})
    base_cfg = np.array([base.star(r) for r in cents], dtype=np.int64)
    plen = np.zeros(len(cents), dtype=np.int64)
    pi = np.zeros((len(cents), 7), dtype=np.int64)
    pj = np.zeros((len(cents), 7), dtype=np.int64)
    for c, r in enumerate(cents):
        q = 0
        for j, s in enumerate(T.star_sites(r)):
            if s in idx:
                pi[c, q] = idx[s]
                pj[c, q] = j
                q += 1
        plen[c] = q
    bad = np.array([0 if o in A else 1 for o in range(max(orb) + 1)], dtype=np.int64)
    return S, cents, base_cfg, plen, pi, pj, np.array(orb, dtype=np.int64), bad


def violations(cfgfun, r, A, orb):
    return sum(1 for t in T.star_sites(r) if orb[cfgfun(t)] not in A)


def detuning(base, S, A, orb, pad=3):
    Sset = set(map(tuple, S))
    lo = [min(s[i] for s in S) - pad for i in range(3)]
    hi = [max(s[i] for s in S) + pad for i in range(3)]
    region = list(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))

    def star_of(val, r):
        cfg = 0
        for j, s in enumerate(T.star_sites(r)):
            if val(s):
                cfg |= 1 << j
        return cfg

    def E2(val):
        tot = 0.0
        zeros = 0
        for r in region:
            def v2(s, r=r):
                return val(s) ^ (1 if s == r else 0)
            E = sum(1 for t in T.star_sites(r) if orb[star_of(v2, t)] not in A)
            if E == 0:
                zeros += 1
            else:
                tot += 1.0 / E
        return -tot, zeros

    v0 = lambda s: base(s)
    v1 = lambda s: base(s) ^ (1 if s in Sset else 0)
    e0, z0 = E2(v0)
    e1, z1 = E2(v1)
    return e1 - e0, z0, z1


if __name__ == '__main__':
    orb_t, reps_t = T.orbits(False)
    name_t = {T.describe(reps_t[o]): o for o in range(len(reps_t))}
    bases = {b.name: b for b in T.period2_bases() + T.layered_bases(3) + T.layered_bases(4)}
    cases = [
        ('cube8 (uniform, corner rule)', 'p2:00000000',
         "c=0 f={}; c=0 f={+x}; c=1 f={+x,+y,+z}",
         [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]),
        ('12 (p2:00011011)', 'p2:00011011',
         "c=0 f={+x}; c=0 f={+x,-x}; c=1 f={+x,-x}; c=1 f={+x,+y}; c=0 f={+x,-x,+y}; c=0 f={+x,-x,+y,-y}; c=1 f={+x,-x,+y,-y}; c=1 f={+x,-x,+y,+z}",
         [(0, 1, 3), (1, 0, 3), (1, 2, 3), (2, 0, 2), (2, 0, 4), (2, 1, 1), (2, 1, 5), (2, 2, 2), (2, 2, 4), (3, 0, 3), (3, 2, 3), (4, 1, 3)]),
        ('18 (p2:00000001)', 'p2:00000001',
         "c=0 f={}; c=1 f={}; c=1 f={+x}; c=0 f={+x,-x}; c=1 f={+x,+y}; c=0 f={+x,-x,+y}; c=0 f={+x,+y,+z}; c=1 f={+x,-x,+y,-y,+z,-z}",
         [(1, 1, 2), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 2), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3), (3, 1, 2), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 2)]),
        ('22 (p2:00000110)', 'p2:00000110',
         "c=0 f={}; c=1 f={}; c=0 f={+x}; c=0 f={+x,-x}; c=0 f={+x,+y}; c=1 f={+x,+y}; c=1 f={+x,-x,+y}; c=0 f={+x,-x,+y,-y}; c=1 f={+x,-x,+y,-y}; c=0 f={+x,+y,+z}; c=1 f={+x,-x,+y,+z}; c=0 f={+x,-x,+y,-y,+z}; c=1 f={+x,-x,+y,-y,+z}",
         [(0, 2, 2), (0, 2, 4), (0, 3, 3), (0, 4, 2), (0, 4, 4), (1, 1, 2), (1, 1, 4), (1, 2, 1), (1, 2, 2), (1, 2, 4), (1, 2, 5), (1, 4, 1), (1, 4, 2), (1, 4, 4), (1, 4, 5), (1, 5, 2), (1, 5, 4), (2, 2, 2), (2, 2, 4), (2, 3, 3), (2, 4, 2), (2, 4, 4)]),
    ]
    for label, bname, desc, S in cases:
        A = {name_t[x.strip()] for x in desc.split(';')}
        base = bases[bname]
        t0 = time.time()
        S2, cents, bc, plen, pi, pj, orbarr, bad = setup(base, S, A, orb_t)
        n = len(S2)
        Cn, Emin, zc = dp(n, len(cents), bc, plen, pi, pj, orbarr, bad)
        # sanity: endpoint valid
        def val(s):
            return base(s) ^ (1 if s in set(S2) else 0)
        endbad = sum(1 for r in cents if orb_t[sum(((val(q)) << j) for j, q in enumerate(T.star_sites(r)))] not in A)
        D2, z0, z1 = detuning(base, S2, A, orb_t)
        per = Cn ** (1.0 / n)
        # eps/J at which C_n eps^n / J^(n-1) = 1e-15 J
        epsJ = (1e-15 / Cn) ** (1.0 / n)
        print(f"{label}: n={n} C_n={Cn:.4e} C_n^(1/n)={per:.4f} n!={math.factorial(n):.3e} "
              f"zero-energy intermediates={zc} endpoint violations={endbad} "
              f"barrier(max over layers of min E)={max(Emin[1:n])} "
              f"eps/J for t=1e-15 J: {epsJ:.4f}; t/J at eps/J=0.1: {Cn*0.1**n:.3e}, at 0.3: {Cn*0.3**n:.3e} "
              f"| D2 = {D2:+.4f} eps^2/J (zero-denominator sites: base {z0}, flipped {z1}) t={time.time()-t0:.1f}s", flush=True)
