"""T18 Test A: can ANY bounded-range hop-sign rule, in ANY diagonal gauge, reproduce the
free-fermion exchange class on unlabelled hard-core records?  Exact linear algebra over F_2.

Fermion cochain a_f (Jordan-Wigner, row-major site order): a hop u->v of one record changes the
sign by (-1)^(number of OTHER records strictly between u and v in the site order).
Local rule: a hop's sign may depend on the other records ONLY if one lies within Chebyshev
distance r of an endpoint of the hop (key = lattice edge + tuple of near others).  Hops with
no other record near carry the one-body rule, which for the fermion is flux-free -> gauge-fixed
to 0 (WLOG: absorbed into f).
Equation per config-graph edge (S,S'):   alpha[key] + f(S) + f(S') = a_f(S,S')   over F_2.
Unknowns: f(S) for every configuration (arbitrary diagonal gauge), alpha[key] for near keys.
r*(L) = smallest r where the system is solvable.
"""
import itertools, sys, time
from collections import deque


def build(L, d, N):
    dims = (L,) * d
    sites = list(itertools.product(range(L), repeat=d))      # row-major order
    idx = {s: i for i, s in enumerate(sites)}
    nbrs = []
    for s in sites:
        out = []
        for ax in range(d):
            for sg in (-1, 1):
                t = list(s); t[ax] += sg
                if 0 <= t[ax] < L:
                    out.append(idx[tuple(t)])
        nbrs.append(out)
    confs = list(itertools.combinations(range(len(sites)), N))
    cidx = {c: i for i, c in enumerate(confs)}
    return sites, nbrs, confs, cidx


def cheb(sites, a, b):
    return max(abs(x - y) for x, y in zip(sites[a], sites[b]))


def config_edges(sites, nbrs, confs, cidx):
    """list of (iS, iS', u, v, others) one per undirected config-graph edge"""
    edges = []
    for iS, S in enumerate(confs):
        for p in S:
            others = tuple(x for x in S if x != p)
            for v in nbrs[p]:
                if v in S:
                    continue
                S2 = tuple(sorted(others + (v,)))
                iS2 = cidx[S2]
                if iS2 < iS:
                    continue          # count each undirected edge once
                edges.append((iS, iS2, p, v, others))
    return edges


def fermion_sign(u, v, others):
    lo, hi = (u, v) if u < v else (v, u)
    return sum(1 for w in others if lo < w < hi) & 1


def solvable(sites, confs, edges, r):
    """returns (True, info) or (False, info)."""
    nconf = len(confs)
    keys = {}
    pivots = {}
    def var(col):  # bit position for variable col (bit 0 = RHS)
        return 1 << (col + 1)
    nkey = 0
    for (iS, iS2, u, v, others) in edges:
        near = tuple(w for w in others if min(cheb(sites, w, u), cheb(sites, w, v)) <= r)
        rhs = fermion_sign(u, v, others)
        row = var(iS) ^ var(iS2)
        if near:
            key = ((min(u, v), max(u, v)), near)
            if key not in keys:
                keys[key] = nconf + len(keys)
            row ^= var(keys[key])
        if rhs:
            row ^= 1
        # reduce
        while True:
            x = row & ~1
            if x == 0:
                if row & 1:
                    return False, dict(nkeys=len(keys))
                break
            lb = x & -x
            if lb in pivots:
                row ^= pivots[lb]
            else:
                pivots[lb] = row
                break
    return True, dict(nkeys=len(keys))


def far_exchange_certificate(sites, confs, cidx, edges, r):
    """Find a cycle made only of FAR hops (no other record within r of the hop) on which the
    fermion sign product is -1, and verify it is an exchange loop.  N = 2 only."""
    n = len(confs)
    adj = [[] for _ in range(n)]
    for (a, b, u, v, others) in edges:
        near = any(min(cheb(sites, w, u), cheb(sites, w, v)) <= r for w in others)
        if near:
            continue
        s = fermion_sign(u, v, others)
        adj[a].append((b, s, u, v))
        adj[b].append((a, s, v, u))
    pot = [None] * n
    par = [None] * n
    for root in range(n):
        if pot[root] is not None:
            continue
        pot[root] = 0
        dq = deque([root])
        while dq:
            x = dq.popleft()
            for (y, s, u, v) in adj[x]:
                if pot[y] is None:
                    pot[y] = pot[x] ^ s
                    par[y] = (x, u, v)
                    dq.append(y)
                elif pot[y] != pot[x] ^ s:
                    # found odd cycle through x-y : rebuild path x->root and y->root
                    def path(z):
                        p = [z]
                        while par[z] is not None:
                            z = par[z][0]
                            p.append(z)
                        return p
                    px, py = path(x), path(y)
                    # cycle: lowest common ancestor
                    sx, sy = set(px), set(py)
                    lca = next(z for z in px if z in sy)
                    cyc = px[:px.index(lca) + 1] + list(reversed(py[:py.index(lca)]))
                    cyc.append(cyc[0])
                    return cyc
    return None


def verify_cycle(sites, confs, cyc, r):
    """track labelled records along the cycle; return (min separation, exchanged?, fermion parity)"""
    S0 = confs[cyc[0]]
    lab = {S0[0]: 0, S0[1]: 1}   # site -> label
    minsep = 10**9
    par = 0
    for a, b in zip(cyc[:-1], cyc[1:]):
        Sa, Sb = confs[a], confs[b]
        gone = [x for x in Sa if x not in Sb][0]
        new = [x for x in Sb if x not in Sa][0]
        other = [x for x in Sa if x != gone][0]
        par ^= fermion_sign(gone, new, (other,))
        lab[new] = lab.pop(gone)
        minsep = min(minsep, cheb(sites, other, gone), cheb(sites, other, new))
    final = {lab[s]: s for s in lab}
    exchanged = (final[0] == S0[1] and final[1] == S0[0])
    return minsep, exchanged, par


def run(L, d, N, rmax=None, certify=True):
    t0 = time.time()
    sites, nbrs, confs, cidx = build(L, d, N)
    edges = config_edges(sites, nbrs, confs, cidx)
    rmax = rmax if rmax is not None else L
    rstar = None
    log = []
    for r in range(0, rmax + 1):
        ok, info = solvable(sites, confs, edges, r)
        log.append((r, ok))
        if ok:
            rstar = r
            break
    cert = None
    if certify and N == 2 and rstar is not None and rstar > 0:
        cyc = far_exchange_certificate(sites, confs, cidx, edges, rstar - 1)
        if cyc:
            cert = verify_cycle(sites, confs, cyc, rstar - 1)
            cert = cert + (len(cyc) - 1,)
    return dict(L=L, d=d, N=N, nconf=len(confs), nedges=len(edges), rstar=rstar, log=log, cert=cert,
                secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    cases = []
    # 1D control
    for L in (6, 8):
        cases.append((L, 1, 2)); cases.append((L, 1, 3))
    # 2D N=2
    for L in range(3, 9):
        cases.append((L, 2, 2))
    # 2D N=3
    for L in (3, 4, 5):
        cases.append((L, 2, 3))
    # 3D N=2
    for L in (2, 3, 4):
        cases.append((L, 3, 2))
    for (L, d, N) in cases:
        res = run(L, d, N)
        print(f"d={d} N={N} L={L}: configs={res['nconf']} edges={res['nedges']}  r*={res['rstar']}  "
              f"(r: solvable) {[(r, ok) for r, ok in res['log']]}  cert(minsep, exchanged, fermion_parity, len)={res['cert']}  {res['secs']}s",
              flush=True)
