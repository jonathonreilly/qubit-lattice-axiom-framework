"""Classical flux checks for bounded-range bijections of site contents.

1D: ring Z_N; permutation = random block-local layers (arbitrary permutations
inside blocks, offset blockings) composed with a global shift s.
Displacements are lifted to integers (|d| <= range < N/2), so crossing a cut
is well defined.  Check: net flux identical at every cut and equal to s.

3D: torus Z_L^3; permutation = random swaps on random edges, random plaquette
4-cycles, then a global shift v.  Check: flux through every plane x_a=c+1/2 is
identical for all c and equals v_a*L^2; net flux out of random boxes is 0.
Exact integer arithmetic throughout.
"""
import numpy as np

rng = np.random.default_rng(20261002)


def lift(d, N):
    d = np.asarray(d) % N
    return np.where(d > N // 2, d - N, d)


def check_1d(N=96, layers=4, maxblock=4, trials=200):
    worst = 0
    for t in range(trials):
        # positions of items: item i starts at site i
        pos = np.arange(N)
        disp = np.zeros(N, dtype=int)  # lifted cumulative displacement
        for _ in range(layers):
            b = rng.integers(2, maxblock + 1)
            off = rng.integers(0, b)
            # site -> new site map for this layer (block-local permutation)
            newsite = np.arange(N)
            start = off
            while start < off + N:
                blk = [(start + j) % N for j in range(b)]
                if start + b > off + N:
                    blk = [(start + j) % N for j in range(off + N - start)]
                perm = rng.permutation(len(blk))
                for j, s_ in enumerate(blk):
                    newsite[s_] = blk[perm[j]]
                start += b
            step = lift(newsite[pos] - pos, N)
            disp += step
            pos = newsite[pos]
        s = int(rng.integers(-3, 4))
        disp += s
        pos = (pos + s) % N
        assert sorted(pos.tolist()) == list(range(N))  # bijection
        # flux across cut between c and c+1 (c+1/2): count lifted paths
        start = np.arange(N)
        fluxes = []
        for c in range(N):
            # an item crosses c+1/2 rightward if start <= c < start+disp (mod N windows)
            right = left = 0
            for x0, d in zip(start, disp):
                # unwrap: positions x0 .. x0+d; cut at c+1/2 + kN for integer k
                lo, hi = (x0, x0 + d) if d >= 0 else (x0 + d, x0)
                # number of cuts c+1/2+kN inside (lo,hi)
                kmin = int(np.ceil((lo - c - 0.5) / N))
                kmax = int(np.floor((hi - c - 0.5) / N))
                n = max(0, kmax - kmin + 1)
                if d > 0:
                    right += n
                elif d < 0:
                    left += n
            fluxes.append(right - left)
        fluxes = np.array(fluxes)
        assert np.all(fluxes == fluxes[0]), fluxes
        assert fluxes[0] == s, (fluxes[0], s)
        worst = max(worst, int(np.max(np.abs(disp))))
    return trials, worst


def check_3d(L=8, trials=60):
    sites = np.array(np.meshgrid(range(L), range(L), range(L), indexing="ij")).reshape(3, -1).T
    idx = lambda p: ((p[..., 0] % L) * L + (p[..., 1] % L)) * L + (p[..., 2] % L)
    E = np.eye(3, dtype=int)
    box_checks = 0
    for t in range(trials):
        n = L ** 3
        pos = sites.copy()          # current (unwrapped) position of each item
        occ = np.arange(n)          # occ[site] = item
        for _ in range(3):
            used = np.zeros(n, bool)
            # random plaquette 4-cycles
            for _ in range(n // 16):
                x = sites[rng.integers(n)]
                a, b = rng.choice(3, 2, replace=False)
                cyc = [x, x + E[a], x + E[a] + E[b], x + E[b]]
                ids = [int(idx(np.array(p))) for p in cyc]
                if used[ids].any():
                    continue
                used[ids] = True
                items = [occ[i] for i in ids]
                if rng.random() < 0.5:  # random orientation
                    cyc, ids, items = cyc[::-1], ids[::-1], items[::-1]
                for j in range(4):  # item at cyc[j] moves to cyc[j+1]
                    it = items[j]
                    dvec = np.array(cyc[(j + 1) % 4]) - np.array(cyc[j])
                    pos[it] += dvec
                    occ[ids[(j + 1) % 4]] = it
            # random swaps on free edges
            for _ in range(n // 8):
                x = sites[rng.integers(n)]
                a = rng.integers(3)
                i1, i2 = int(idx(x)), int(idx(x + E[a]))
                if used[i1] or used[i2]:
                    continue
                used[i1] = used[i2] = True
                it1, it2 = occ[i1], occ[i2]
                pos[it1] += E[a]
                pos[it2] -= E[a]
                occ[i1], occ[i2] = it2, it1
        v = rng.integers(-1, 2, size=3)
        pos += v
        final = idx(pos)
        assert len(set(final.tolist())) == n  # bijection
        disp = pos - sites
        for a in range(3):
            fl = []
            for c in range(L):
                tot = 0
                for x0, d in zip(sites[:, a], disp[:, a]):
                    lo, hi = (x0, x0 + d) if d >= 0 else (x0 + d, x0)
                    kmin = int(np.ceil((lo - c - 0.5) / L))
                    kmax = int(np.floor((hi - c - 0.5) / L))
                    m = max(0, kmax - kmin + 1)
                    tot += m if d > 0 else (-m if d < 0 else 0)
                fl.append(tot)
            assert all(f == fl[0] for f in fl), (a, fl)
            assert fl[0] == v[a] * L * L, (a, fl[0], v)
        # closed-surface check: random boxes (with no wrap), net outflow = 0
        for _ in range(10):
            lo = rng.integers(0, L // 2, size=3)
            hi = lo + rng.integers(1, L // 2, size=3)
            inside0 = np.all((sites >= lo) & (sites < hi), axis=1)
            fin = pos % L
            inside1 = np.all((fin >= lo) & (fin < hi), axis=1)
            out = int(np.sum(inside0 & ~inside1))
            inn = int(np.sum(~inside0 & inside1))
            assert out == inn
            box_checks += 1
    return trials, box_checks


if __name__ == "__main__":
    t1, w = check_1d()
    print(f"1D: {t1} random bounded-range bijections on Z_96 (max |disp| = {w}):"
          " net flux equal at all 96 cuts and equal to the shift; PASS")
    t3, nb = check_3d()
    print(f"3D: {t3} random NN-built bijections on Z_8^3 (+ global shift):"
          " plane flux equal for all 8 planes in each of 3 directions, = v_a*L^2;"
          f" {nb} random boxes have zero net outflow; PASS")
