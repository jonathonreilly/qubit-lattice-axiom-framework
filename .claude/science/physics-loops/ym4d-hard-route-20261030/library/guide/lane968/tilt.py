# GUIDE only (row 968, Section 7.2/7.4). Half-space lattice gauge theory, open time, Higgs-type tilt kap*Re(U) on the
# spatial links of slice 0. Measures the transverse boundary susceptibility chi(kap; k) of the imaginary link components.
# Groups: su2 (links as complex pairs (a, b), U = [[a, b], [-conj b, conj a]]) and u1 (b = 0).
import sys, time, json, math, resource
import numpy as np
group, L, T, beta, kap = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
ntherm, nmeas, nsep, seed = int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])
SU2 = (group == "su2")
rng = np.random.default_rng(seed)
shape = (T, L, L, L)
def mul(x, y):
    if not SU2: return (x[0] * y[0], None)
    return (x[0] * y[0] - x[1] * np.conj(y[1]), x[0] * y[1] + x[1] * np.conj(y[0]))
def dag(x):
    if not SU2: return (np.conj(x[0]), None)
    return (np.conj(x[0]), -x[1])
def add(x, y):
    if not SU2: return (x[0] + y[0], None)
    return (x[0] + y[0], x[1] + y[1])
def sh(x, mu, d=-1):   # d = -1: field at n + mu; d = +1: field at n - mu
    if not SU2: return (np.roll(x[0], d, axis=mu), None)
    return (np.roll(x[0], d, axis=mu), np.roll(x[1], d, axis=mu))
def scale(x, m):
    if not SU2: return (x[0] * m, None)
    return (x[0] * m, x[1] * m)
def haar(n):
    if not SU2: return (np.exp(2j * np.pi * rng.random(n)), None)
    v = rng.normal(size=(4,) + n); v /= np.sqrt((v * v).sum(0))
    return (v[0] + 1j * v[1], v[2] + 1j * v[3])
U = [haar(shape) for _ in range(4)]            # hot start
tt = np.arange(T)[:, None, None, None]
par = (np.indices(shape).sum(0) % 2)
mask_fwd_t = (tt <= T - 2) * np.ones(shape)    # forward time staple exists
mask_bwd_t = (tt >= 1) * np.ones(shape)        # backward time staple exists
def staple(mu):
    tot = None
    for nu in range(4):
        if nu == mu: continue
        f = mul(mul(sh(U[nu], mu), dag(sh(U[mu], nu))), dag(U[nu]))
        Un = sh(U[nu], nu, +1)                 # U_nu(n - nu)
        b = mul(mul(dag(sh(Un, mu)), dag(sh(U[mu], nu, +1))), Un)
        if nu == 0 and mu != 0:
            f = scale(f, mask_fwd_t); b = scale(b, mask_bwd_t)
        s = add(f, b)
        tot = s if tot is None else add(tot, s)
    return tot
def su2_x0(al):                                # density sqrt(1 - x^2) exp(al x) on [-1, 1] (Creutz)
    al = np.maximum(al, 1e-9)
    x0 = np.empty_like(al); todo = np.ones(al.shape, bool)
    while todo.any():
        a = al[todo]; r = rng.random(a.shape)
        x = 1.0 + np.log(np.exp(-2 * a) + r * (1.0 - np.exp(-2 * a))) / a
        ok = rng.random(a.shape) ** 2 <= 1.0 - x * x
        idx = np.flatnonzero(todo)[ok]
        x0.flat[idx] = x[ok]; todo.flat[idx] = False
    return np.clip(x0, -1.0, 1.0)
def update(mu, p):
    A = staple(mu)
    S = dag(A)                                 # weight exp(beta <U, S>)
    Sa = S[0].copy()
    if mu != 0 and kap != 0.0: Sa[0] += kap / beta
    sel = (par == p)
    if mu == 0: sel = sel & (tt <= T - 2)
    if not SU2:
        s = Sa[sel]
        th = rng.vonmises(np.angle(s), beta * np.abs(s))
        U[mu][0][sel] = np.exp(1j * th); return
    sa, sb = Sa[sel], S[1][sel]
    k = np.sqrt(np.abs(sa) ** 2 + np.abs(sb) ** 2)
    x0 = su2_x0(beta * k)
    n = rng.normal(size=(3,) + x0.shape); n *= np.sqrt(1.0 - x0 * x0) / np.sqrt((n * n).sum(0))
    xa, xb = x0 + 1j * n[0], n[1] + 1j * n[2]
    kk = np.maximum(k, 1e-12); va, vb = sa / kk, sb / kk
    U[mu][0][sel] = xa * va - xb * np.conj(vb)
    U[mu][1][sel] = xa * vb + xb * np.conj(va)
def sweep():
    for mu in range(4):
        for p in (0, 1): update(mu, p)
xs = np.arange(L)
phase = [np.exp(2j * np.pi * xs / L).reshape([L if a == j else 1 for a in range(3)]) for j in range(3)]
def measure():
    c1, c0, re_sum = [], [], 0.0
    for i in (1, 2, 3):
        a = U[i][0][0]; comps = [a.imag]
        if SU2: b = U[i][1][0]; comps += [b.real, b.imag]
        re_sum += a.real.sum()
        for cpt in comps:
            c0.append(cpt.sum() ** 2 / L ** 3)
            for j in range(3):
                if j == i - 1: continue
                c1.append(abs((cpt * phase[j]).sum()) ** 2 / L ** 3)
    return np.mean(c1), np.mean(c0), re_sum / (3 * L ** 3)
def plaq():                                    # spatial plaquettes on the middle slices
    tot, cnt = 0.0, 0
    for i in (1, 2, 3):
        for j in range(i + 1, 4):
            P = mul(mul(U[i], sh(U[j], i)), mul(dag(sh(U[i], j)), dag(U[j])))
            tot += P[0].real[2:T - 2].mean(); cnt += 1
    return tot / cnt
t0 = time.time()
for _ in range(ntherm): sweep()
ser = np.zeros((nmeas, 3)); pl = []
for m in range(nmeas):
    for _ in range(nsep): sweep()
    ser[m] = measure()
    if m % 50 == 0: pl.append(plaq())
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2 * 2 ** 30: sys.exit("RSS above 2 GB")
def blk(x, nb=20):
    b = x[: (len(x) // nb) * nb].reshape(nb, -1).mean(1)
    return float(b.mean()), float(b.std(ddof=1) / math.sqrt(nb))
nb = 20; n2 = (nmeas // nb) * nb
mre = ser[:n2, 2].reshape(nb, -1)
var_re = [float(((bk - bk.mean()) ** 2).mean() * 3 * L ** 3) for bk in mre]   # connected, inside blocks (biased low)
out = dict(group=group, L=L, T=T, beta=beta, kap=kap, nmeas=nmeas, nsep=nsep, seed=seed,
           chi1=blk(ser[:, 0]), chi0=blk(ser[:, 1]), mean_re=blk(ser[:, 2]),
           chi_re=(float(np.mean(var_re)), float(np.std(var_re, ddof=1) / math.sqrt(nb))),
           plaq=float(np.mean(pl)), sec=round(time.time() - t0, 1),
           ms_per_sweep=round(1000 * (time.time() - t0) / (ntherm + nmeas * nsep), 2))
print(json.dumps(out), flush=True)
