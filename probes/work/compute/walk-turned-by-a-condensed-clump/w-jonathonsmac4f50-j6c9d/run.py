#!/usr/bin/env python3
"""The clocked walk turned by a condensed clump of records, against rays and against block 98's first-order kick (floating point throughout).

As landed on main:
- Block 98 (#8878):
  - T1: mean-zero torus line sums.
  - T2: the supplied continuum profile u = 6 lambda/(4 pi r) gives a first-order transverse kick
    -int d_b u dx = 3 lambda/(pi b), towards the source, magnitude 2|U(b)| with U(b) = 6 lambda/(4 pi b), for a unit-speed ray.
  - T3: the ray law is a conditional weak-field model; 'no nonlinear bending or changed-length result'.
- Block 54 (#8570): the clocked walk H_w = sqrt(W) H sqrt(W), H = sum_a sigma_a S_a, W = e^u.
  The exact packet force is withdrawn; T4 is a conditional ray model.
- Block 95 (#8860): log w_z = 6 lambda sum_r G(z - r), lambda = log kappa = -g, G the zero-mean lattice kernel (a neutralized torus law).
The clump:
- Block 95's gas on a 16^3 torus (N = 96, g = 1), run with the dynamics of probes/lib/clocked_gas.py.
  The loop body is copied, because the lib returns only statistics and the task needs the positions.
  Checked below against the lib's own statistics.
- The largest cluster is unwrapped across the torus, and the other records are placed at the minimum image about its centre.
- Everything is placed at the centre of an 80^3 torus, whose clock field is u = 6 lambda sum_r G_80(z - r) (zero-mean kernel, FFT).
Packets:
- Positive branch of H, k0 = (0.8, 0, 0), position spread 4 on each axis (amplitude exp(-|x - x0|^2 / 64)).
- Start at x0 = centre - 30 along x, impact parameter b along y (b = 10, 15, 20, 25, 30).
- Evolved by expm_multiply on the 2 x 80^3 space.
- Turn = change of <sin k_y>, read by FFT at t = 20, 40, 60, 80 (the free packet then sits 26 sites past the clump, short of the torus wrap).
Rays:
- H = w(x) eps(k), eps = sqrt(sum sin^2 k_j), with w from the same field.
- Cubic splines of u and of its central differences, periodic.
- 2000 rays per b drawn from the packet's Wigner function (independent Gaussians: position sd 4, wave-vector sd 1/8).
- RK4, dt = 0.05.
- Mean and spread of the change of sin k_y at the same times.
First order:
- (a) Block 98's continuum kick summed over the records, sum_i 2|U(b_i)| (y-component of the unit transverse vector
  to record i), for a unit-speed ray.
- (b) The same kick for the lattice ray of speed v = cos k0 and energy eps0 = sin k0: multiplied by eps0/v = tan k0.
- (c) The straight-line integral -(eps0/v) int d_y u dx of the actual lattice field over the distance v t.
HIT (the task's): the walk departs from its rays by much more than the spreads allow.
  Read here as: at t = 80 the walk's mean differs from the ray bundle's mean by more than twice the bundle's spread.
  Also printed as HIT, because it contradicts the task's expectation sentence:
  at the largest b, the first-order kick misses the walk by more than max(twice the ray spread, half the walk's turn).
Weak-field control: the same field scaled by 1/100 at b = 10, 20, 30.
"""
import math, os, sys, time
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
from scipy.ndimage import map_coordinates, spline_filter
from numba import njit

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "lib")))
from clocked_gas import zero_mean_kernel, many_records

def out(s): print(s, flush=True)

LAM, NREC, LG, EVENTS, SEED = -1.0, 96, 16, 2000000, 7
LB = int(os.environ.get("CLUMP_BOX", "80"))
K0, SIG = 0.8, 4.0
BS = tuple(int(x) for x in os.environ.get("CLUMP_BS", "10,15,20,25,30").split(","))
TIMES = (20.0, 40.0, 60.0, 80.0)
NRAY, DT = int(os.environ.get("CLUMP_NRAY", "2000")), 0.05

# ---------------------------------------------------------------- the clump (dynamics copied from probes/lib/clocked_gas.py)
@njit(cache=False)
def run_gas(G, L, lam, n, steps, seed):
    np.random.seed(seed)
    V = L * L * L
    occ = -np.ones(V, dtype=np.int64)
    pos = np.zeros((n, 3), dtype=np.int64)
    i = 0
    while i < n:
        s = np.random.randint(V)
        if occ[s] < 0:
            occ[s] = i
            pos[i, 0] = s // (L * L); pos[i, 1] = (s // L) % L; pos[i, 2] = s % L
            i += 1
    dirs = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    logw = np.zeros(n)
    for i in range(n):
        acc = 0.0
        for j in range(n):
            acc += G[(pos[i, 0] - pos[j, 0]) % L, (pos[i, 1] - pos[j, 1]) % L, (pos[i, 2] - pos[j, 2]) % L]
        logw[i] = 6 * lam * acc
    empt = np.zeros(n, dtype=np.int64)
    R = np.zeros(n)
    for t in range(steps):
        tot = 0.0
        for i in range(n):
            c = 0
            for e in range(6):
                s = ((pos[i, 0] + dirs[e, 0]) % L) * L * L + ((pos[i, 1] + dirs[e, 1]) % L) * L + (pos[i, 2] + dirs[e, 2]) % L
                if occ[s] < 0:
                    c += 1
            empt[i] = c
            R[i] = math.exp(logw[i]) * c / 6
            tot += R[i]
        u = np.random.random() * tot
        acc = 0.0
        k = n - 1
        for i in range(n):
            acc += R[i]
            if acc >= u:
                k = i
                break
        while R[k] == 0.0:
            k -= 1
        m = np.random.randint(empt[k])
        for e in range(6):
            s = ((pos[k, 0] + dirs[e, 0]) % L) * L * L + ((pos[k, 1] + dirs[e, 1]) % L) * L + (pos[k, 2] + dirs[e, 2]) % L
            if occ[s] < 0:
                if m == 0:
                    old = pos[k, 0] * L * L + pos[k, 1] * L + pos[k, 2]
                    x0, x1, x2 = pos[k, 0], pos[k, 1], pos[k, 2]
                    occ[old] = -1
                    occ[s] = k
                    pos[k, 0] = (pos[k, 0] + dirs[e, 0]) % L
                    pos[k, 1] = (pos[k, 1] + dirs[e, 1]) % L
                    pos[k, 2] = (pos[k, 2] + dirs[e, 2]) % L
                    for j in range(n):
                        if j == k:
                            continue
                        logw[j] += 6 * lam * (G[(pos[j, 0] - pos[k, 0]) % L, (pos[j, 1] - pos[k, 1]) % L, (pos[j, 2] - pos[k, 2]) % L]
                                              - G[(pos[j, 0] - x0) % L, (pos[j, 1] - x1) % L, (pos[j, 2] - x2) % L])
                    acc2 = 0.0
                    for j in range(n):
                        acc2 += G[(pos[k, 0] - pos[j, 0]) % L, (pos[k, 1] - pos[j, 1]) % L, (pos[k, 2] - pos[j, 2]) % L]
                    logw[k] = 6 * lam * acc2
                    break
                m -= 1
    return pos

def unwrap_clump(pos, L):
    n = len(pos); key = {tuple(p): i for i, p in enumerate(pos)}
    seen = -np.ones(n, int); comps = []
    for s in range(n):
        if seen[s] >= 0: continue
        comp = [s]; seen[s] = len(comps); un = {s: np.array(pos[s], float)}; stack = [s]
        while stack:
            i = stack.pop()
            for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                q = tuple((pos[i] + np.array(d)) % L)
                j = key.get(q)
                if j is not None and seen[j] < 0:
                    seen[j] = len(comps); un[j] = un[i] + np.array(d); comp.append(j); stack.append(j)
        comps.append(un)
    big = max(comps, key=len); cen = np.mean(list(big.values()), axis=0)
    X = np.zeros((n, 3))
    for i in range(n):
        if i in big: X[i] = big[i]
        else: X[i] = cen + ((pos[i] - cen + L / 2) % L - L / 2)
    return X - np.rint(cen), len(big)

# ---------------------------------------------------------------- the field on the box
def box_field(X, L):
    c = L // 2
    n = np.zeros((L, L, L))
    for p in np.rint(X).astype(int): n[(p[0] + c) % L, (p[1] + c) % L, (p[2] + c) % L] += 1
    k = 2 * np.pi * np.fft.fftfreq(L); kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz)); E[0, 0, 0] = 1.0
    Gh = 1.0 / E; Gh[0, 0, 0] = 0.0
    return 6 * LAM * np.real(np.fft.ifftn(np.fft.fftn(n) * Gh))

# ---------------------------------------------------------------- the walk
def walk_op(u, L):
    V = L ** 3; idx = np.arange(V).reshape(L, L, L); rt = np.exp(0.5 * u)
    rows, cols, vals = [], [], []
    SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex)
    for a, sig in enumerate((SX, SY, SZ)):
        nb = np.roll(idx, -1, axis=a)                              # z + e_a
        amp = (rt * np.roll(rt, -1, axis=a)).ravel()
        src, dst = idx.ravel(), nb.ravel()
        for p in range(2):
            for q in range(2):
                if sig[p, q] == 0: continue
                # (S_a psi)(z) = (psi(z+e) - psi(z-e)) / 2i : entry (z, z+e) = 1/2i, entry (z+e, z) = -1/2i
                rows.append(2 * src + p); cols.append(2 * dst + q); vals.append(sig[p, q] * amp / 2j)
                rows.append(2 * dst + p); cols.append(2 * src + q); vals.append(-sig[p, q] * amp / 2j)
    return sps.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * V, 2 * V))

def packet(L, x0):
    k = 2 * np.pi * np.fft.fftfreq(L); kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    dk2 = np.angle(np.exp(1j * (kx - K0))) ** 2 + ky ** 2 + kz ** 2
    g = np.exp(-dk2 * SIG ** 2) * np.exp(-1j * (kx * x0[0] + ky * x0[1] + kz * x0[2]))
    nx, ny, nz = np.sin(kx), np.sin(ky), np.sin(kz); nn = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
    a1, b1 = nx - 1j * ny, nn - nz; a2, b2 = nn + nz, nx + 1j * ny
    use1 = (np.abs(a1) ** 2 + np.abs(b1) ** 2) >= (np.abs(a2) ** 2 + np.abs(b2) ** 2)
    a = np.where(use1, a1, a2); b = np.where(use1, b1, b2); nrm = np.sqrt(np.abs(a) ** 2 + np.abs(b) ** 2); nrm[nrm == 0] = 1
    up = np.fft.ifftn(g * a / nrm); dn = np.fft.ifftn(g * b / nrm)
    psi = np.stack([up, dn], axis=-1).reshape(-1)
    return psi / np.linalg.norm(psi)

def mean_sin_ky(psi, L):
    ph = psi.reshape(L, L, L, 2)
    k = np.sin(2 * np.pi * np.fft.fftfreq(L))
    tot = 0.0; w = 0.0
    for c in range(2):
        P = np.abs(np.fft.fftn(ph[..., c])) ** 2
        tot += (P * k[None, :, None]).sum(); w += P.sum()
    return tot / w

def mean_pos(psi, L):
    p = (np.abs(psi.reshape(L, L, L, 2)) ** 2).sum(-1)
    outv = []
    for a in range(3):
        m = p.sum(axis=tuple(b for b in range(3) if b != a)); ang = 2 * np.pi * np.arange(L) / L
        outv.append((np.angle((m * np.exp(1j * ang)).sum()) % (2 * np.pi)) * L / (2 * np.pi))
    return np.array(outv)

# ---------------------------------------------------------------- rays
def rays(u, L, x0, rng):
    cu = [spline_filter(u, order=3, mode="grid-wrap")]
    for a in range(3): cu.append(spline_filter((np.roll(u, -1, a) - np.roll(u, 1, a)) / 2, order=3, mode="grid-wrap"))
    def field(X):
        co = np.mod(X.T, L)
        return [map_coordinates(c, co, order=3, mode="grid-wrap", prefilter=False) for c in cu]
    X = x0[None, :] + SIG * rng.standard_normal((NRAY, 3))
    K = np.array([K0, 0, 0])[None, :] + rng.standard_normal((NRAY, 3)) / (2 * SIG)
    def rhs(X, K):
        uu, gx, gy, gz = field(X); w = np.exp(uu)
        s, c = np.sin(K), np.cos(K); eps = np.sqrt((s * s).sum(1)); eps = np.where(eps > 1e-12, eps, 1e-12)
        dX = w[:, None] * s * c / eps[:, None]
        dK = -(eps * w)[:, None] * np.stack([gx, gy, gz], 1)
        return dX, dK
    s0 = np.sin(K[:, 1]).copy(); res = {}; t = 0.0
    for T in TIMES:
        while t < T - 1e-9:
            a1, b1 = rhs(X, K); a2, b2 = rhs(X + 0.5 * DT * a1, K + 0.5 * DT * b1)
            a3, b3 = rhs(X + 0.5 * DT * a2, K + 0.5 * DT * b2); a4, b4 = rhs(X + DT * a3, K + DT * b3)
            X = X + DT / 6 * (a1 + 2 * a2 + 2 * a3 + a4); K = K + DT / 6 * (b1 + 2 * b2 + 2 * b3 + b4); t += DT
        d = np.sin(K[:, 1]) - s0
        res[T] = (d.mean(), d.std(), X.mean(0).copy())
    return res

if __name__ == "__main__":
    t_start = time.time()
    G16 = zero_mean_kernel(LG)
    pos = run_gas(G16, LG, LAM, NREC, EVENTS, SEED)
    touch, sk, big = many_records(G16, LG, LAM, NREC, EVENTS, SEED, 50)
    X, nbig = unwrap_clump(pos, LG)
    rg = math.sqrt(((X - X.mean(0)) ** 2).sum(1).mean())
    out("N clump: block 95's gas, L = 16, N = 96, g = 1, %d events, seed %d; the lib's own run with the same seed: time-weighted largest-cluster "
        "share %.3f, touching %.3f; the copied dynamics' final state: largest cluster %d of 96, radius of gyration %.2f"
        % (EVENTS, SEED, big, touch, nbig, rg))
    u = box_field(X, LB); c = LB // 2
    out("N field on the %d^3 torus: u at the centre %.2f, min %.2f, max %.3f; u on the line y = c + b, z = c at x = c: %s; at the packet start (x = c - 30): %s"
        % (LB, u[c, c, c], u.min(), u.max(), " ".join("b=%d %.3f" % (b, u[c, c + b, c]) for b in BS),
           " ".join("b=%d %.3f" % (b, u[c - 30, c + b, c]) for b in BS)))
    eps0, v0 = math.sin(K0), math.cos(K0)
    H = walk_op(u, LB)
    rng = np.random.default_rng(1)
    rows = []
    for b in BS:
        x0 = np.array([c - 30.0, c + b, c])
        # first order
        tr = X - np.array([0.0, b, 0.0]); byz = np.sqrt(tr[:, 1] ** 2 + tr[:, 2] ** 2)
        kick_a = float((3 * abs(LAM) / (math.pi * byz) * (tr[:, 1] / byz)).sum())
        xs = np.arange(c - 30, c - 30 + int(round(v0 * TIMES[-1])) + 1) % LB
        gy = (np.roll(u, -1, 1) - np.roll(u, 1, 1)) / 2
        kick_c = float(-(eps0 / v0) * gy[xs, c + b, c].sum())
        # walk
        t0 = time.time()
        psi = packet(LB, x0); s0 = mean_sin_ky(psi, LB); tprev = 0.0; wk = {}
        for T in TIMES:
            psi = expm_multiply(-1j * H * (T - tprev), psi); tprev = T
            wk[T] = (mean_sin_ky(psi, LB) - s0, mean_pos(psi, LB), np.linalg.norm(psi))
        tw = time.time() - t0
        ry = rays(u, LB, x0, rng)
        out("N b = %d: first order (a) block 98's sum_i 2|U(b_i)| (unit speed) %+.4f; (b) x tan k0 %+.4f; (c) straight-line lattice integral over v t %+.4f"
            % (b, kick_a, kick_a * math.tan(K0), kick_c))
        for T in TIMES:
            dw, pw, nw = wk[T]; dm, ds, pr = ry[T]
            out("    t = %3d: walk change of <sin k_y> %+.4f (centre %.1f %.1f %.1f, norm %.6f); rays %+.4f with spread %.4f (centre %.1f %.1f %.1f)"
                % (T, dw, pw[0], pw[1], pw[2], nw, dm, ds, pr[0], pr[1], pr[2]))
        rows.append((b, wk[TIMES[-1]][0], ry[TIMES[-1]][0], ry[TIMES[-1]][1], kick_a, kick_c))
        out("    (walk %.0f s)" % tw)
    # weak-field control: the same clump field scaled by 1/100, where block 98's first-order kick should hold
    out("")
    SC = 0.01
    Hs = walk_op(SC * u, LB); ctrl = []
    for b in (10, 20, 30):
        x0 = np.array([c - 30.0, c + b, c])
        tr = X - np.array([0.0, b, 0.0]); byz = np.sqrt(tr[:, 1] ** 2 + tr[:, 2] ** 2)
        kick_b = SC * float((3 * abs(LAM) / (math.pi * byz) * (tr[:, 1] / byz)).sum()) * math.tan(K0)
        xs = np.arange(c - 30, c - 30 + int(round(v0 * TIMES[-1])) + 1) % LB
        gy = (np.roll(u, -1, 1) - np.roll(u, 1, 1)) / 2
        kick_c = float(-(eps0 / v0) * SC * gy[xs, c + b, c].sum())
        psi = packet(LB, x0); s0 = mean_sin_ky(psi, LB)
        psi = expm_multiply(-1j * Hs * TIMES[-1], psi); dw = mean_sin_ky(psi, LB) - s0
        ry = rays(SC * u, LB, x0, rng)[TIMES[-1]]
        ctrl.append((b, dw, ry[0], ry[1], kick_b, kick_c))
        out("N weak-field control (field x 1/100), b = %d, t = %d: walk %+.5f; rays %+.5f spread %.5f; first order (b) block 98 x tan k0 %+.5f; "
            "(c) straight-line lattice integral %+.5f" % (b, TIMES[-1], dw, ry[0], ry[1], kick_b, kick_c))
    hits = []
    for b, dw, dm, ds, ka, kc in rows:
        if abs(dw - dm) > 2 * ds:
            hits.append("b = %d: the walk's turn %+.4f departs from its rays' %+.4f by %.4f, more than twice their spread %.4f" % (b, dw, dm, abs(dw - dm), ds))
    # the task's expectation sentence also says 'first-order formula good at large b': checked at the largest b
    b, dw, dm, ds, ka, kc = rows[-1]
    if abs(ka * math.tan(K0) - dw) > max(2 * ds, 0.5 * abs(dw)):
        hits.append("(the task's expectation 'first-order formula good at large b') at b = %d the first-order kick %+.3f (block 98 x tan k0) against the walk's %+.3f: "
                    "the clump's field is strong at every b of the task (u on the line at x = c: %.2f)" % (b, ka * math.tan(K0), dw, u[c, c + b, c]))
    out("")
    for h in hits: out("HIT: " + h)
    out("SUMMARY: walk turned by a condensed clump (N = 96, g = 1) in an %d^3 box, at t = %d: " % (LB, TIMES[-1])
        + "; ".join("b=%d walk %+.3f rays %+.3f+-%.3f first-order(a) %+.2f" % (b, dw, dm, ds, ka) for b, dw, dm, ds, ka, kc in rows)
        + " (%.0f s)" % (time.time() - t_start))
