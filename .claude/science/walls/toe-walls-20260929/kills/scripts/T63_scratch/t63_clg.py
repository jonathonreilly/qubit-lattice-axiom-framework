"""T63 route R2 (outside vocabulary): conserved-count local hop dynamics with one record per site.
A record with >= 1 recorded nearest neighbour is 'crowded' and hops to a random empty neighbour
(conserved lattice gas, Rossi-Pastor-Satorras-Vespignani PRL 85:1803 type). Absorbing (frozen) states
at record density rho. Question: does the frozen pattern have a non-analytic small-k structure factor
S(k) ~ k^alpha with alpha near 1 (hyperuniform, Hexner-Levine PRL 114:110602 mechanism)?"""
import numpy as np, numba as nb, sys, time, math
sys.path.insert(0, ".")
from t63_spectra import shell_S, fits

@nb.njit(cache=True)
def evolve(occ, L, max_sweeps, seed):
    np.random.seed(seed)
    N = L*L*L
    dx = np.array([1, -1, 0, 0, 0, 0]); dy = np.array([0, 0, 1, -1, 0, 0]); dz = np.array([0, 0, 0, 0, 1, -1])
    for sweep in range(max_sweeps):
        # count active
        active = 0
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    if occ[x, y, z]:
                        n = 0
                        for d in range(6):
                            n += occ[(x+dx[d]) % L, (y+dy[d]) % L, (z+dz[d]) % L]
                        if n > 0: active += 1
        if active == 0:
            return sweep
        for _ in range(N):
            i = np.random.randint(0, N)
            x = i // (L*L); y = (i // L) % L; z = i % L
            if occ[x, y, z] == 0: continue
            n = 0
            for d in range(6):
                n += occ[(x+dx[d]) % L, (y+dy[d]) % L, (z+dz[d]) % L]
            if n == 0: continue
            d = np.random.randint(0, 6)
            nx = (x+dx[d]) % L; ny = (y+dy[d]) % L; nz = (z+dz[d]) % L
            if occ[nx, ny, nz] == 0:
                occ[x, y, z] = 0; occ[nx, ny, nz] = 1
    return -1

def init(L, rho, rng):
    N = L**3; occ = np.zeros(N, dtype=np.int8)
    occ[rng.choice(N, size=int(round(rho*N)), replace=False)] = 1
    return occ.reshape(L, L, L)

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    nseeds = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    T = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    nmax = 4
    print("CLG hop rule, L=%d, seeds=%d, max sweeps=%d; S(k) shells n=1..%d" % (L, nseeds, T, nmax))
    for rho in (0.10, 0.14, 0.18, 0.22, 0.26, 0.30, 0.34):
        t0 = time.time(); acc = []; times = []
        for sd in range(nseeds):
            rng = np.random.default_rng(sd + int(rho*1000))
            occ = init(L, rho, rng)
            t = evolve(occ, L, T, 9000 + sd)
            times.append(t)
            if t >= 0: acc.append(shell_S(occ, nmax))
        frac = len(acc)/nseeds
        if len(acc) >= 3:
            A = np.array(acc); S = A.mean(0); sem = A.std(0, ddof=1)/math.sqrt(len(A))
            a, ae, cp, ca, c2 = fits(L, S, np.maximum(sem, 1e-9), nmax)
            print("rho=%.2f absorbed %d/%d  mean t_abs=%s  S=%s  alpha_eff=%+.2f+-%.2f chi2pow=%.1f chi2an=%.1f [%.0fs]" %
                  (rho, len(acc), nseeds, np.round(np.mean([t for t in times if t >= 0]), 0), np.round(S, 4).tolist(), a, ae, cp, ca, time.time()-t0))
        else:
            print("rho=%.2f absorbed %d/%d within %d sweeps (active phase or slow)  [%.0fs]" % (rho, len(acc), nseeds, T, time.time()-t0))
