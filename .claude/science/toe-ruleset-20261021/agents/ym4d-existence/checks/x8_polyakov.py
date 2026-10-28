"""x8: deterministic inequalities of the session-9 Polyakov-loop route (EXISTENCE §18) and an SU(2) Wilson MC.
Criteria: checks/x8_criteria.md (written before this script). Non-load-bearing.
SU(2) is represented by unit quaternions with the product of x7 (an anti-isomorphic copy of SU(2), used consistently);
every inequality checked is group-theoretic, so it holds in either copy."""
import math, time, resource, sys
import numpy as np

T0 = time.time()
OUT = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); OUT.append(s); sys.stdout.flush()

def qmul(a, b):
    a0, av = a[..., :1], a[..., 1:]
    b0, bv = b[..., :1], b[..., 1:]
    s = a0 * b0 - np.sum(av * bv, axis=-1, keepdims=True)
    v = a0 * bv + b0 * av - np.cross(av, bv)
    return np.concatenate([s, v], axis=-1)

def qdag(a):
    return np.concatenate([a[..., :1], -a[..., 1:]], axis=-1)

def qexp(X):  # X[..., 3] in su(2) ~ R^3 (half-angle convention: exp(X) = cos|X| + sin|X| X/|X|)
    r = np.linalg.norm(X, axis=-1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        u = np.where(r > 0, X / np.where(r > 0, r, 1), 0.0)
    return np.concatenate([np.cos(r), np.sin(r) * u], axis=-1)

def opdist(q):  # ||1 - q||_op for a unit quaternion
    return np.sqrt(np.maximum(2.0 - 2.0 * q[..., 0], 0.0))

def haar(rng, shape):
    q = rng.normal(size=shape + (4,))
    return q / np.linalg.norm(q, axis=-1, keepdims=True)

TOL = 1e-12
# ------------------------------------------------------------------------------------------------------------ A1
a = np.linspace(0, 2 * math.pi, 2001, endpoint=False)
A, B = np.meshgrid(a, a, indexing="ij")
G = np.cos(A) ** 2 + np.cos(B) ** 2 + np.cos(A + B) ** 2
i, j = np.unravel_index(np.argmin(G), G.shape)
x = np.array([a[i], a[j]])
for h in [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]:   # local refinement
    best = None
    for dx in np.linspace(-10 * h, 10 * h, 41):
        for dy in np.linspace(-10 * h, 10 * h, 41):
            v = math.cos(x[0] + dx) ** 2 + math.cos(x[1] + dy) ** 2 + math.cos(x[0] + dx + x[1] + dy) ** 2
            if best is None or v < best[0]:
                best = (v, x[0] + dx, x[1] + dy)
    x = np.array(best[1:])
m1 = best[0]
okA1 = (0.75 - 1e-9 <= m1 <= 0.75 + 1e-6) and G.min() >= 0.75 - 1e-9
pr(f"A1: grid min {G.min():.12f}; refined min {m1:.12f} at ({x[0]:.6f}, {x[1]:.6f}) [pi/3 = {math.pi/3:.6f}]  "
   f"{'PASS' if okA1 else 'FAIL'}")

# ------------------------------------------------------------------------------------------------------------ A2
rng = np.random.default_rng(802)
W1 = haar(rng, (400000,)); W2 = haar(rng, (400000,))
# near-commuting pairs
V1 = haar(rng, (400000,))
ax = V1[:, 1:] / np.linalg.norm(V1[:, 1:], axis=1, keepdims=True)
phi = rng.uniform(0, 2 * math.pi, size=(400000, 1))
Csub = np.concatenate([np.cos(phi), np.sin(phi) * ax], axis=1)
eps = np.exp(rng.uniform(math.log(1e-6), 0.0, size=(400000, 1)))
Xd = rng.normal(size=(400000, 3)); Xd /= np.linalg.norm(Xd, axis=1, keepdims=True)
V2 = qmul(qexp(eps * Xd), Csub)
# exactly commuting
C1 = haar(rng, (200000,))
ax2 = C1[:, 1:] / np.linalg.norm(C1[:, 1:], axis=1, keepdims=True)
phi2 = rng.uniform(0, 2 * math.pi, size=(200000, 1))
C2 = np.concatenate([np.cos(phi2), np.sin(phi2) * ax2], axis=1)
P1 = np.concatenate([W1, V1, C1]); P2 = np.concatenate([W2, V2, C2])
F = P1[:, 0] ** 2 + P2[:, 0] ** 2 + qmul(P1, P2)[:, 0] ** 2
comm = opdist(qmul(qmul(P1, P2), qmul(qdag(P1), qdag(P2))))
slack = F - 0.75 + comm
nv = int(np.sum(slack < -TOL))
pr(f"A2: {len(F)} pairs; violations {nv}; min slack {slack.min():.3e} (Haar {slack[:400000].min():.3e}, "
   f"near-comm {slack[400000:800000].min():.3e}, commuting {slack[800000:].min():.3e})  {'PASS' if nv == 0 else 'FAIL'}")
okA2 = nv == 0

# ------------------------------------------------------------------------------------------------------------ lattice
shape = (8, 4, 4, 4)
sh = lambda X, mu, s: np.roll(X, -s, axis=mu)   # X(x + s e_mu)

def plaq(U, mu, nu):
    return qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qdag(sh(U[mu], nu, 1)), qdag(U[nu])))

def poly(U, mu):  # W_mu based at every site
    n = U.shape[1 + mu]
    W = U[mu].copy()
    for k in range(1, n):
        W = qmul(W, np.roll(U[mu], -k, axis=mu))   # W := W * U_mu(x + k e_mu)
    return W

def family(U):
    W1 = poly(U, 1); W2 = poly(U, 2)
    return W1, W2, [W1[..., 0], W2[..., 0], qmul(W1, W2)[..., 0]]

def stokes_check(U):
    """returns number of violations of A3 (a), (b), (c) and the min slack of (c)."""
    W1, W2, fs = family(U)
    dist = {}
    for mu in range(4):
        for nu in range(mu + 1, 4):
            dist[(mu, nu)] = opdist(plaq(U, mu, nu))
    nviol = 0
    # (a) and (c): 2-torus (1,2) through the base point: depends on (t, x3) only
    T12 = dist[(1, 2)].sum(axis=(1, 2))                      # shape (8, 4): (t, x3)
    T12b = T12[:, None, None, :] * np.ones(shape)
    cm = opdist(qmul(qmul(W1, W2), qmul(qdag(W1), qdag(W2))))
    nviol += int(np.sum(cm > T12b + TOL))
    Fv = fs[0] ** 2 + fs[1] ** 2 + fs[2] ** 2
    nviol += int(np.sum(Fv > 3 + TOL)) + int(np.sum(Fv < 0.75 - T12b - TOL))
    minc = float((Fv - 0.75 + T12b).min())
    # (b): ribbons
    d01 = dist[(0, 1)]; d02 = dist[(0, 2)]
    r1 = d01.sum(axis=1)                                     # sum over x1 of the (0,1) plaquettes: (t, x2, x3)
    r2 = d02.sum(axis=2)                                     # sum over x2 of the (0,2) plaquettes: (t, x1, x3)
    R1 = r1[:, None, :, :] * np.ones(shape)                  # ribbon slice of the e1-loop at each base point
    R2 = r2[:, :, None, :] * np.ones(shape)
    Rs = [R1, R2, R1 + R2]
    nt = shape[0]
    for n in range(3):
        f = fs[n]
        for t in range(nt):
            acc = np.zeros(shape[1:])
            for d in range(1, nt):
                acc = acc + Rs[n][(t + d - 1) % nt]
                diff = np.abs(f[(t + d) % nt] - f[t])
                nviol += int(np.sum(diff > acc + TOL))
    return nviol, minc

rng = np.random.default_rng(803)
nvA3 = 0; minc_all = []
cfgs = []
for e in [0.02, 0.1, 0.3]:
    for r in range(7 if e != 0.3 else 6):
        X = rng.normal(size=(4,) + shape + (3,)) * e
        cfgs.append(qexp(X))
for r in range(20):
    cfgs.append(haar(rng, (4,) + shape))
for U in cfgs:
    v, mc = stokes_check(U); nvA3 += v; minc_all.append(mc)
pr(f"A3 (i)-(ii): {len(cfgs)} configs; violations {nvA3}; min slack of (c) {min(minc_all):.3e}")

# ------------------------------------------------------------------------------------------------------------ A4
def su3_obj(p, Smat):
    al = np.zeros((3, 3)); al[:2, :] = p.reshape(2, 3); al[2, :] = -al[0] - al[1]   # al[a, mu]; sum_a al[a, mu] = 0
    z = np.mean(np.exp(1j * (al @ Smat.T)), axis=0)                                  # f_n = N^-1 tr h^n, n in S
    return float(np.sum(np.abs(z) ** 2))
Sall = [(a1, a2, a3) for a1 in (-1, 0, 1) for a2 in (-1, 0, 1) for a3 in (-1, 0, 1) if (a1, a2, a3) != (0, 0, 0)]
S3 = [(1, 0, 0), (0, 1, 0), (1, 1, 0), (1, -1, 0), (1, 2, 0)]
try:
    from scipy.optimize import minimize
    have_sp = True
except Exception:
    have_sp = False
rng = np.random.default_rng(804)
for name, S in [("charged {-1,0,1}^3", Sall), ("S3", S3)]:
    best = 1e9; Smat = np.array(S, float)
    for s in range(2000):
        p0 = rng.uniform(0, 2 * math.pi, 6)
        if have_sp:
            r = minimize(su3_obj, p0, args=(Smat,), method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 4000})
            v = r.fun
        else:
            v = su3_obj(p0, Smat)
        best = min(best, v)
    pr(f"A4 (info, SU(3), {'Nelder-Mead' if have_sp else 'random only'}): min over commuting triples of sum_n |f_n|^2, "
       f"S = {name} ({len(S)} vectors): {best:.6f}")
tA = time.time() - T0

# ------------------------------------------------------------------------------------------------------------ B
def staple(U, mu):
    S = np.zeros_like(U[0])
    for nu in range(4):
        if nu == mu:
            continue
        up = qmul(qmul(sh(U[nu], mu, 1), qdag(sh(U[mu], nu, 1))), qdag(U[nu]))
        Um = sh(U[nu], nu, -1)
        dn = qmul(qmul(qdag(sh(Um, mu, 1)), qdag(sh(U[mu], nu, -1))), Um)
        S += up + dn
    return S

def heat(U, mu, beta, mask, rng):
    V = staple(U, mu)
    k = np.sqrt(np.sum(V * V, axis=-1))
    Vh = V / k[..., None]
    alpha = beta * k
    a0 = np.empty(k.shape); todo = np.ones(k.shape, bool)
    while todo.any():
        n = todo.sum()
        r1, r2, r3, r4 = (1.0 - rng.random(n) for _ in range(4))
        lam2 = -(np.log(r1) + np.cos(2 * math.pi * r2) ** 2 * np.log(r3)) / (2 * alpha[todo])
        acc = r4 ** 2 <= 1 - lam2
        tmp = a0[todo]; tmp[acc] = 1 - 2 * lam2[acc]; a0[todo] = tmp
        t2 = todo.copy(); t2[todo] = ~acc; todo = t2
    nv = rng.normal(size=k.shape + (3,)); nv /= np.linalg.norm(nv, axis=-1, keepdims=True)
    W = np.concatenate([a0[..., None], np.sqrt(np.maximum(1 - a0 ** 2, 0))[..., None] * nv], axis=-1)
    new = qmul(W, qdag(Vh))
    U[mu] = np.where(mask[..., None], new, U[mu])

def over(U, mu, mask):
    V = staple(U, mu)
    Vh = V / np.sqrt(np.sum(V * V, axis=-1))[..., None]
    new = qdag(qmul(qmul(Vh, U[mu]), Vh))
    U[mu] = np.where(mask[..., None], new, U[mu])

par = np.indices(shape).sum(axis=0) % 2
masks = [par == 0, par == 1]

def jk(vals, nb=25):
    n = len(vals) // nb * nb; X = vals[:n]; bs = n // nb
    full = X.mean()
    j = np.array([np.concatenate([X[:b * bs], X[(b + 1) * bs:]]).mean() for b in range(nb)])
    return full, math.sqrt((nb - 1) * np.mean((j - j.mean()) ** 2))

pr("x8 B (MC, SU(2) Wilson, 8x4^3, HB + 3 OR, hot start, 1000 therm + 2500 meas)")
res = {}; nvB = 0; mincB = []
ns, nt = 4, shape[0]
for beta, seed in [(8.0, 811), (16.0, 1611), (32.0, 3211)]:
    t1 = time.time()
    rng = np.random.default_rng(seed)
    U = haar(rng, (4,) + shape)
    Xd = {1: [], 3: [], 5: []}; fm = []; sv = []
    for it in range(1000 + 2500):
        for mu in range(4):
            for m in masks:
                heat(U, mu, beta, m, rng)
        for _ in range(3):
            for mu in range(4):
                for m in masks:
                    over(U, mu, m)
        if it % 50 == 0:
            U /= np.linalg.norm(U, axis=-1, keepdims=True)
        if it >= 1000:
            _, _, fs = family(U)
            for d in (1, 3, 5):
                t = (d - 1) // 2
                Xd[d].append(sum(np.mean(f[t] * f[nt - 1 - t]) for f in fs))
            fm.append([np.mean(f) for f in fs])
            sv.append(np.mean(np.stack([1.0 - plaq(U, a_, b_)[..., 0] for a_ in range(4) for b_ in range(a_ + 1, 4)])))
            if (it - 1000) % 50 == 0:
                v, mc = stokes_check(U); nvB += v; mincB.append(mc)
    s_mean = float(np.mean(sv)); eta = 2 * s_mean
    out = {d: jk(np.array(Xd[d])) for d in Xd}
    fmean = np.mean(np.array(fm), axis=0)
    bound = {d: 0.75 - (ns ** 2 + 4 * ns * d) * math.sqrt(eta) for d in Xd}
    res[beta] = (out, s_mean)
    pr(f" beta={beta:4.0f}: <s>beta={s_mean*beta:.4f}; X(1)={out[1][0]:.4f}+-{out[1][1]:.4f} ({out[1][0]/out[1][1]:.1f} SE); "
       f"X(3)={out[3][0]:.4f}+-{out[3][1]:.4f}; X(5)={out[5][0]:.4f}+-{out[5][1]:.4f}; "
       f"E f_n = {fmean[0]:+.3f},{fmean[1]:+.3f},{fmean[2]:+.3f}; theorem bound (d=1,3,5) = "
       f"{bound[1]:.2f},{bound[3]:.2f},{bound[5]:.2f} [{time.time()-t1:.0f}s]")
pr(f"A3 (iii): {len(mincB)} MC configs; violations {nvB}; min slack of (c) {min(mincB):.3e}")
okA3 = (nvA3 == 0) and (nvB == 0)
pr(f"A1 {'PASS' if okA1 else 'FAIL'}; A2 {'PASS' if okA2 else 'FAIL'}; A3 {'PASS' if okA3 else 'FAIL'}")
b0 = 0.6 <= res[32.0][1] * 32 <= 0.9
ok = all(res[b][0][1][0] - 5 * res[b][0][1][1] >= 0.375 for b in (16.0, 32.0))
fail = res[32.0][0][1][0] + 3 * res[32.0][0][1][1] < 0.375
pr(f"B0 {'PASS' if b0 else 'FAIL'}; B1 {'PASS' if ok else ('FAIL' if fail else 'INCONCLUSIVE')}")
ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20
pr(f"wall {time.time()-T0:.0f}s (A {tA:.0f}s); peak {ru:.0f} MB")
open(sys.argv[1] if len(sys.argv) > 1 else "x8_out.txt", "w").write("\n".join(OUT) + "\n")
