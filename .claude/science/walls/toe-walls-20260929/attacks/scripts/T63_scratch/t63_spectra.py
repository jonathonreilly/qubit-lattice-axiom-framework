"""T63 test B: small-k structure factor S(k) of record patterns from local rules on periodic Z^3.
Fits (i) power law A k^alpha and (ii) analytic S0 + S2 k^2 in integer shells n = 1..NMAX."""
import numpy as np, numba as nb, sys, time, math

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
        if sweep(occ, allowed, perm, L) == 0: break
    return occ

@nb.njit(cache=True)
def eden_snapshots(L, seed_p, targets, seed):
    """Records arrive only at empty sites with >= 1 recorded nearest neighbour (uniform among such sites),
    starting from sparse independent seeds. Returns snapshots at fill fractions in targets."""
    np.random.seed(seed)
    N = L*L*L
    occ = np.zeros(N, dtype=np.int8)
    infront = np.zeros(N, dtype=np.int8)
    pos = np.full(N, -1, dtype=np.int64)
    front = np.empty(N, dtype=np.int64)
    nf = 0
    count = 0
    snaps = np.zeros((len(targets), N), dtype=np.int8)
    # seeds
    for i in range(N):
        if np.random.random() < seed_p:
            occ[i] = 1; count += 1
    for i in range(N):
        if occ[i]:
            x = i // (L*L); y = (i // L) % L; z = i % L
            for d in range(6):
                nx = x; ny = y; nz = z
                if d == 0: nx = (x+1) % L
                elif d == 1: nx = (x-1) % L
                elif d == 2: ny = (y+1) % L
                elif d == 3: ny = (y-1) % L
                elif d == 4: nz = (z+1) % L
                else: nz = (z-1) % L
                j = (nx*L + ny)*L + nz
                if occ[j] == 0 and infront[j] == 0:
                    infront[j] = 1; pos[j] = nf; front[nf] = j; nf += 1
    t = 0
    while t < len(targets) and nf > 0:
        while t < len(targets) and count >= targets[t]*N:
            snaps[t, :] = occ; t += 1
        if t >= len(targets): break
        r = int(np.random.random()*nf)
        j = front[r]
        # remove from frontier
        last = front[nf-1]; front[r] = last; pos[last] = r; nf -= 1; infront[j] = 0; pos[j] = -1
        occ[j] = 1; count += 1
        x = j // (L*L); y = (j // L) % L; z = j % L
        for d in range(6):
            nx = x; ny = y; nz = z
            if d == 0: nx = (x+1) % L
            elif d == 1: nx = (x-1) % L
            elif d == 2: ny = (y+1) % L
            elif d == 3: ny = (y-1) % L
            elif d == 4: nz = (z+1) % L
            else: nz = (z-1) % L
            k = (nx*L + ny)*L + nz
            if occ[k] == 0 and infront[k] == 0:
                infront[k] = 1; pos[k] = nf; front[nf] = k; nf += 1
    while t < len(targets) and count >= targets[t]*N:
        snaps[t, :] = occ; t += 1
    return snaps.reshape(len(targets), L, L, L)

def shell_S(occ, nmax):
    L = occ.shape[0]
    f = occ.astype(float) - occ.mean()
    F = np.fft.fftn(f)
    P = (np.abs(F)**2) / f.size
    n = np.fft.fftfreq(L, d=1.0/L)
    nx, ny, nz = np.meshgrid(n, n, n, indexing='ij')
    nn = np.sqrt(nx**2 + ny**2 + nz**2)
    out = np.zeros(nmax)
    for m in range(1, nmax+1):
        sel = (nn >= m-0.5) & (nn < m+0.5)
        out[m-1] = P[sel].mean()
    return out

def fits(L, S, sem, nmax):
    n = np.arange(1, nmax+1); k = 2*np.pi*n/L
    # power law: weighted LSQ in log space
    y = np.log(S); sy = sem/S
    Amat = np.vstack([np.ones_like(k), np.log(k)]).T / sy[:, None]
    coef, *_ = np.linalg.lstsq(Amat, y/sy, rcond=None)
    cov = np.linalg.inv(Amat.T @ Amat)
    chi_pow = float(np.sum(((y - Amat[:, 0]*0 - (coef[0] + coef[1]*np.log(k)))/sy)**2))
    alpha, aerr = coef[1], math.sqrt(cov[1, 1])
    # analytic S0 + S2 k^2
    B = np.vstack([np.ones_like(k), k**2]).T / sem[:, None]
    c2, *_ = np.linalg.lstsq(B, S/sem, rcond=None)
    chi_an = float(np.sum(((S - (c2[0] + c2[1]*k**2))/sem)**2))
    return alpha, aerr, chi_pow, chi_an, c2

def run(L, name, gen, nseeds, nmax):
    t0 = time.time(); acc = []
    for sd in range(nseeds):
        occ = gen(sd)
        acc.append(shell_S(occ, nmax))
    acc = np.array(acc); S = acc.mean(0); sem = acc.std(0, ddof=1)/math.sqrt(nseeds)
    a, ae, cp, ca, c2 = fits(L, S, sem, nmax)
    print("  %-38s S(n=1..%d)= %s" % (name, nmax, np.round(S, 3).tolist()))
    print("  %-38s alpha_eff = %+.3f +- %.3f   chi2(power)=%.1f  chi2(S0+S2k^2)=%.1f  (dof 4)  S0=%.3f S2=%.3f  [%.0fs]" % ("", a, ae, cp, ca, c2[0], c2[1], time.time()-t0))
    return dict(name=name, L=L, alpha=a, err=ae, chi_pow=cp, chi_an=ca, S=S.tolist())

if __name__ == "__main__":
    out = []
    for L, nseeds, nmax in ((48, 16, 6), (64, 12, 8)):
        print("L=%d seeds=%d shells 1..%d (k=2 pi n/L)" % (L, nseeds, nmax))
        out.append(run(L, "Bernoulli(0.25) control", lambda sd: (np.random.default_rng(sd).random((L, L, L)) < 0.25).astype(np.int8), nseeds, nmax))
        for m in (0, 1, 2, 3):
            out.append(run(L, "frozen crowding A={0..%d}" % m, lambda sd, m=m: frozen_state(L, list(range(m+1)), np.random.default_rng(1000+sd)), nseeds, nmax))
        for fill in (0.15, 0.30, 0.60):
            cache = {}
            def gen(sd, fill=fill):
                key = sd
                if key not in cache:
                    cache[key] = eden_snapshots(L, 0.002, np.array([0.15, 0.30, 0.60]), 5000+sd)
                return cache[key][[0.15, 0.30, 0.60].index(fill)]
            out.append(run(L, "Eden arrival, sparse seeds, fill %.2f" % fill, gen, nseeds, nmax))
        x, y, z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing='ij')
        cb = ((x+y+z) % 2 == 0).astype(np.int8)
        S = shell_S(cb, nmax)
        print("  chessboard control: S(n=1..%d) = %s (crystal; k=0 mode only)" % (nmax, np.round(S, 6).tolist()))
    import json; json.dump(out, open("t63_spectra_results.json", "w"), indent=1)
