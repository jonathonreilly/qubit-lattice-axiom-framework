"""T62 test V: number variance of record patterns from local nearest-neighbour formation rules on Z^3.
Var(N_w) ~ w^s.  Relative fluctuation ~ w^(s/2-3).  rho_vac a^4 ~ (relative fluct) ~ T^(-(3-s/2)); observed needs 3-s/2 = 2 (s=2)."""
import numpy as np, numba as nb, sys, time

@nb.njit(cache=True)
def sweep(occ, allowed, perm, L):
    changed = 0
    for idx in perm:
        z = idx % L; y = (idx // L) % L; x = idx // (L*L)
        if occ[x, y, z]: continue
        k = (occ[(x+1) % L, y, z] + occ[(x-1) % L, y, z] + occ[x, (y+1) % L, z] + occ[x, (y-1) % L, z]
             + occ[x, y, (z+1) % L] + occ[x, y, (z-1) % L])
        if allowed[k]:
            occ[x, y, z] = 1; changed += 1
    return changed

def frozen_state(L, A, rng, max_sweeps=200):
    allowed = np.zeros(7, dtype=np.bool_)
    for k in A: allowed[k] = True
    occ = np.zeros((L, L, L), dtype=np.int8)
    for s in range(max_sweeps):
        perm = rng.permutation(L**3).astype(np.int64)
        ch = sweep(occ, allowed, perm, L)
        if ch == 0: break
    # verify frozen
    nn = sum(np.roll(occ, sh, ax) for sh in (1, -1) for ax in (0, 1, 2))
    elig = (occ == 0) & allowed[nn]
    return occ, int(elig.sum()), s+1

def window_counts(occ, w):
    L = occ.shape[0]
    P = np.pad(occ.astype(np.int64), ((0, w-1),)*3, mode='wrap')
    C = np.zeros((L+w, L+w, L+w), dtype=np.int64)
    C[1:, 1:, 1:] = P.cumsum(0).cumsum(1).cumsum(2)[:L+w-1, :L+w-1, :L+w-1]
    # box sum at origin (i,j,k): C[i+w,j+w,k+w]-C[i,j+w,k+w]-... 
    i = np.arange(L)
    S = (C[w:w+L, w:w+L, w:w+L] - C[0:L, w:w+L, w:w+L] - C[w:w+L, 0:L, w:w+L] - C[w:w+L, w:w+L, 0:L]
         + C[0:L, 0:L, w:w+L] + C[0:L, w:w+L, 0:L] + C[w:w+L, 0:L, 0:L] - C[0:L, 0:L, 0:L])
    return S

def var_curve(occ, ws):
    out = []
    for w in ws:
        S = window_counts(occ, w)
        out.append((S.var(), S.mean()))
    return np.array(out)

def slope(ws, V, lo=4, hi=16):
    m = (np.array(ws) >= lo) & (np.array(ws) <= hi)
    x = np.log(np.array(ws)[m]); y = np.log(V[m])
    p = np.polyfit(x, y, 1)
    return p[0]

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    seeds = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    ws = list(range(1, 17))
    rules = {
      "Bernoulli(0.25) control": None,
      "crowding A={0} (max indep set)": [0],
      "crowding A={0,1}": [0, 1],
      "crowding A={0,1,2}": [0, 1, 2],
      "crowding A={0,1,2,3}": [0, 1, 2, 3],
      "A={0,2,3,4,5,6} (k=1 blocks)": [0, 2, 3, 4, 5, 6],
      "A={0,3,4,5,6} (referee 3D rule)": [0, 3, 4, 5, 6],
    }
    print("L=%d seeds=%d windows w=1..16 (periodic, all positions)" % (L, seeds))
    results = {}
    for name, A in rules.items():
        slopes = []; fanos = []; dens = []; t0 = time.time(); bad = 0
        for sd in range(seeds):
            rng = np.random.default_rng(1000 + sd)
            if A is None:
                occ = (rng.random((L, L, L)) < 0.25).astype(np.int8); ne = 0; ns = 0
            else:
                occ, ne, ns = frozen_state(L, A, rng)
                bad += ne
            vc = var_curve(occ, ws)
            V = vc[:, 0]; M = vc[:, 1]
            dens.append(occ.mean())
            if occ.mean() > 0.999:
                slopes.append(np.nan); fanos.append(np.nan); continue
            slopes.append(slope(ws, V)); fanos.append(V[15]/M[15])
        s = np.array(slopes)
        if np.mean(dens) > 0.999:
            print("%-34s density 1.000  fills the periodic lattice (trivial frozen state; no pattern to measure)" % name)
            continue
        print("%-34s density %.3f  s(w=4..16) = %.3f +- %.3f   Fano(w=16) = %.3f   eligible-left %d   (%.1fs)" %
              (name, np.mean(dens), s.mean(), s.std(ddof=1)/np.sqrt(len(s)), np.mean(fanos), bad, time.time()-t0))
        results[name] = (s.mean(), np.mean(fanos))
    # chessboard control
    x, y, z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing='ij')
    cb = ((x+y+z) % 2 == 0).astype(np.int8)
    vc = var_curve(cb, ws)
    print("%-34s density %.3f  Var(w=1..16) = %s" % ("chessboard control", cb.mean(), np.round(vc[:, 0], 3).tolist()))
    # Fano trend for the 'pure' rule
    print("\nFano(w) trend for the m=0 frozen state (w=1,2,4,8,16):")
    rng = np.random.default_rng(7); occ, ne, ns = frozen_state(L, [0], rng)
    vc = var_curve(occ, ws)
    print([round(float(vc[w-1, 0]/vc[w-1, 1]), 3) for w in (1, 2, 4, 8, 16)])
