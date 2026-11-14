# Row 974 (gap-trajtest-opus), GUIDE only. SU(2) Wilson on a periodic L^3 x Nt lattice. Heat bath (Creutz sampler),
# checkerboard by direction and 4D parity; pattern of guide/lane968/tilt.py with periodic time. Per time slice, zero
# momentum, after spatial APE smearing (X <- Proj(X + alpha * sum of 4 spatial staples)) at two levels:
#   G: plaquette sum and 2x2-loop sum over the 3 spatial planes (centre-even, 0++)       -> 4 operators
#   F: Polyakov lines along x, y, z (half trace), summed over the slice / L (centre-odd)  -> 2 levels x 3 axes
# Writes raw slice series to out/<tag>.npz; analysis in ana974.py. Criteria: library/gap-trajtest-opus.md Section 3.
# Usage: python3 -I traj974.py L Nt beta ntherm nmeas nsep seed n1 n2 tag
import sys, time, math, resource, os
import numpy as np
L, T, beta = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
ntherm, nmeas, nsep, seed = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
n1, n2, tag = int(sys.argv[8]), int(sys.argv[9]), sys.argv[10]
ALPHA = 0.5
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
rng = np.random.default_rng(seed)
shape = (T, L, L, L)
def mul(x, y): return (x[0] * y[0] - x[1] * np.conj(y[1]), x[0] * y[1] + x[1] * np.conj(y[0]))
def dag(x): return (np.conj(x[0]), -x[1])
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sh(x, mu, d=-1): return (np.roll(x[0], d, axis=mu), np.roll(x[1], d, axis=mu))   # d=-1: field at n+mu
def haar(n):
    v = rng.normal(size=(4,) + n); v /= np.sqrt((v * v).sum(0))
    return (v[0] + 1j * v[1], v[2] + 1j * v[3])
U = [haar(shape) for _ in range(4)]
par = (np.indices(shape).sum(0) % 2)
def staple(mu):
    tot = None
    for nu in range(4):
        if nu == mu: continue
        f = mul(mul(sh(U[nu], mu), dag(sh(U[mu], nu))), dag(U[nu]))
        Un = sh(U[nu], nu, +1)
        b = mul(mul(dag(sh(Un, mu)), dag(sh(U[mu], nu, +1))), Un)
        s = add(f, b); tot = s if tot is None else add(tot, s)
    return tot
def su2_x0(al):
    al = np.maximum(al, 1e-9); x0 = np.empty_like(al); todo = np.ones(al.shape, bool)
    while todo.any():
        a = al[todo]; r = rng.random(a.shape)
        x = 1.0 + np.log(np.exp(-2 * a) + r * (1.0 - np.exp(-2 * a))) / a
        ok = rng.random(a.shape) ** 2 <= 1.0 - x * x
        idx = np.flatnonzero(todo)[ok]; x0.flat[idx] = x[ok]; todo.flat[idx] = False
    return np.clip(x0, -1.0, 1.0)
def update(mu, p):
    S = dag(staple(mu)); sel = (par == p)
    sa, sb = S[0][sel], S[1][sel]
    k = np.sqrt(np.abs(sa) ** 2 + np.abs(sb) ** 2); x0 = su2_x0(beta * k)
    n = rng.normal(size=(3,) + x0.shape); n *= np.sqrt(1.0 - x0 * x0) / np.sqrt((n * n).sum(0))
    xa, xb = x0 + 1j * n[0], n[1] + 1j * n[2]
    kk = np.maximum(k, 1e-12); va, vb = sa / kk, sb / kk
    U[mu][0][sel] = xa * va - xb * np.conj(vb); U[mu][1][sel] = xa * vb + xb * np.conj(va)
def sweep():
    for mu in range(4):
        for p in (0, 1): update(mu, p)
def proj(x):
    nrm = np.sqrt(np.abs(x[0]) ** 2 + np.abs(x[1]) ** 2); return (x[0] / nrm, x[1] / nrm)
def ape(X, n):
    for _ in range(n):
        new = []
        for i in (1, 2, 3):
            S = X[i]; Ssum = (ALPHA * 0 + S[0], S[1])
            acc = None
            for j in (1, 2, 3):
                if j == i: continue
                f = mul(mul(X[j], sh(X[i], j)), dag(sh(X[j], i)))
                Xj = sh(X[j], j, +1)
                b = mul(mul(dag(Xj), sh(X[i], j, +1)), sh(Xj, i))
                s = add(f, b); acc = s if acc is None else add(acc, s)
            new.append(proj((S[0] + ALPHA * acc[0], S[1] + ALPHA * acc[1])))
        X = [None] + new
    return X
def slice_obs(X):
    pl, l2 = np.zeros(T), np.zeros(T)
    for i in (1, 2, 3):
        for j in range(i + 1, 4):
            P = mul(mul(X[i], sh(X[j], i)), mul(dag(sh(X[i], j)), dag(X[j])))
            pl += P[0].real.sum(axis=(1, 2, 3))
            Li = mul(X[i], sh(X[i], i)); Lj = mul(X[j], sh(X[j], j))
            W = mul(mul(Li, sh(sh(Lj, i), i)), mul(dag(sh(sh(Li, j), j)), dag(Lj)))
            l2 += W[0].real.sum(axis=(1, 2, 3))
    pol = np.zeros((3, T))
    for a, i in enumerate((1, 2, 3)):
        W = X[i]
        for k in range(1, L): W = mul(W, (np.roll(X[i][0], -k, axis=i), np.roll(X[i][1], -k, axis=i)))
        pol[a] = W[0].real.sum(axis=(1, 2, 3)) / L
    return pl, l2, pol
def allplaq():
    tot = 0.0
    for m in range(4):
        for n in range(m + 1, 4):
            P = mul(mul(U[m], sh(U[n], m)), mul(dag(sh(U[m], n)), dag(U[n]))); tot += P[0].real.mean()
    return tot / 6
t0 = time.time()
print(f"traj974 L={L} Nt={T} beta={beta} ntherm={ntherm} nmeas={nmeas} nsep={nsep} seed={seed} ape={n1},{n2} tag={tag}", flush=True)
for s in range(ntherm):
    sweep()
    if s % 100 == 0: print(f"[{time.time()-t0:7.1f}s] therm {s} plaq {allplaq():.5f}", flush=True)
G = np.zeros((nmeas, 4, T)); F = np.zeros((nmeas, 2, 3, T)); PL = np.zeros(nmeas)
for m in range(nmeas):
    for _ in range(nsep): sweep()
    PL[m] = allplaq()
    X = [None] + [U[i] for i in (1, 2, 3)]
    X1 = ape(X, n1); a1 = slice_obs(X1); X2 = ape(X1, n2 - n1); a2 = slice_obs(X2)
    G[m] = [a1[0], a1[1], a2[0], a2[1]]; F[m, 0] = a1[2]; F[m, 1] = a2[2]
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > 3 * 2 ** 30: sys.exit("RSS above 3 GB; stopping")
    if m % 50 == 0 or m == nmeas - 1:
        print(f"[{time.time()-t0:7.1f}s rss {rss/2**20:.0f}MB] meas {m} plaq {PL[m]:.5f}", flush=True)
        np.savez(os.path.join(OUT, tag + ".npz"), G=G[:m + 1], F=F[:m + 1], PL=PL[:m + 1],
                 meta=np.array([L, T, beta, ntherm, nsep, seed, n1, n2]))
print(f"done {time.time()-t0:.1f}s plaq mean {PL.mean():.5f} +- {PL.std(ddof=1)/math.sqrt(nmeas):.5f}", flush=True)
