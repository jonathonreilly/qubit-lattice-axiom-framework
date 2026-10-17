"""Item 4: code validity (own construction)."""
import sys, time
import numpy as np
from ccode import CornerCode, StabGroup, pmul, pdag, commute, hermitian

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4


def to_np(paulis, n):
    nb = (n + 7) // 8
    X = np.zeros((len(paulis), n), dtype=np.float32)
    Z = np.zeros((len(paulis), n), dtype=np.float32)
    for i, P in enumerate(paulis):
        X[i] = np.unpackbits(np.frombuffer(P[0].to_bytes(nb, 'little'), dtype=np.uint8), bitorder='little')[:n]
        Z[i] = np.unpackbits(np.frombuffer(P[1].to_bytes(nb, 'little'), dtype=np.uint8), bitorder='little')[:n]
    return X, Z


def main():
    t0 = time.time()
    C = CornerCode(L)
    n = C.nq
    gens = C.generators()
    print('qubits', n, 'per site', n // L**3, 'generators', len(gens))
    herm = all(hermitian(g[2]) for g in gens)
    print('all generators Hermitian:', herm)
    X, Z = to_np([g[2] for g in gens], n)
    S = (X @ Z.T + Z @ X.T) % 2
    print('generator commutation failures:', int(S.sum()))
    # on-site check of B and R supports
    G = StabGroup(n)
    rk = 0
    for g in gens:
        if G.add(g[2]):
            rk += 1
    print('rank', rk, 'contains -I or iI:', G.minus_identity, 'k =', n - rk, f'({time.time()-t0:.1f}s)')
    # face types reversal invariance
    faces = C.faces()
    bad = 0
    for (t, cyc) in faces[:200]:
        a = C.loop(cyc, 1)
        b = C.loop(list(reversed(cyc)), 1)
        c = C.loop(cyc[1:] + cyc[:1], 1)
        bad += (a != b) + (a != c)
    print('loop orientation/start dependence (first 200 faces):', bad)
    # hops: anticommute iff share exactly one corner
    hops = []
    for e in C.edges:
        j, k = tuple(e)
        hops.append((e, C.hop(j, k)))
    HX, HZ = to_np([h[1] for h in hops], n)
    Sh = (HX @ HZ.T + HZ @ HX.T) % 2
    share = np.zeros_like(Sh)
    for a, (e, _) in enumerate(hops):
        pass
    E = np.zeros((len(hops), C.lat.ncorner), dtype=np.float32)
    for a, (e, _) in enumerate(hops):
        for c in e:
            E[a, c] = 1
    share = (E @ E.T)
    np.fill_diagonal(share, 0)
    expect = (share == 1).astype(np.float32)
    print('hop anticommutation rule failures:', int(np.abs(Sh - expect).sum()))
    # hops vs stabilizers: commute with R and loops; anticommute with B at its two ends only
    gX, gZ = X, Z
    Ch = (HX @ gZ.T + HZ @ gX.T) % 2
    fails = 0
    for a, (e, _) in enumerate(hops):
        for i, g in enumerate(gens):
            want = 1 if (g[0] == 'B' and g[1] in e) else 0
            if Ch[a, i] != want:
                fails += 1
    print('hop/stabilizer syndrome failures:', fails)
    # T-junction: corner c0 with three neighbours
    c0 = C.lat.corner((0, 0, 0), [(1, 0, 0), (0, 1, 0)])
    nb = [t[0] for t in C.nbrs[c0]][:6]
    import itertools
    tj = set()
    for (a, b, c) in itertools.permutations(nb, 3):
        W1, W2, W3 = C.hop(c0, a), C.hop(c0, b), C.hop(c0, c)
        lhs = pmul(pmul(W3, pdag(W2)), W1)
        rhs = pmul(pmul(W1, pdag(W2)), W3)
        assert lhs[:2] == rhs[:2]
        tj.add(((lhs[2] - rhs[2]) % 4))
    print('T-junction W3 W2^dag W1 = theta W1 W2^dag W3, theta values:', {0: '+1', 2: '-1'}.get(tj.pop()) if len(tj) == 1 else tj)
    # product of all B and all R
    P = (0, 0, 0)
    for g in gens:
        if g[0] in ('B', 'R'):
            P = pmul(P, g[2])
    print('prod B prod R == I:', P == (0, 0, 0))
    # site-locality of B and R-halves
    sites_B = all(len({C.site_of[q] for q in range(n) if (C.Bq(c)[1] >> q) & 1}) == 1 for c in range(0, C.lat.ncorner, 37))
    print('B_q on one site (sample):', sites_B)
    print(f'time {time.time()-t0:.1f}s')


if __name__ == '__main__':
    main()
