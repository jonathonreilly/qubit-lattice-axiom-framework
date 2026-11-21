#!/usr/bin/env python3
"""Kill test for library/lift-nonlinear.md, Sections 1 to 3. Criteria: CRITERIA.md.

SU(2) as unit quaternions q = w + x (i s1) + y (i s2) + z (i s3).
exp(i A.sigma), A in R^3, is cos|A| + (sin|A|/|A|) A in this basis, so |log| = |A|
and half real trace = cos|A|, the normalisation of the note.

A run can refute or guide. It discharges nothing.
"""
import resource
import sys

import numpy as np

RSS_LIMIT_GB = 2.0
L = 3


def check_rss():
    # ru_maxrss is in bytes on darwin
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9
    if rss > RSS_LIMIT_GB:
        sys.exit(f"stopping: RSS {rss:.2f} GB above {RSS_LIMIT_GB} GB")


# ---------- quaternion arithmetic, last axis of length 4 ----------
def qmul(a, b):
    w1, v1 = a[..., 0], a[..., 1:]
    w2, v2 = b[..., 0], b[..., 1:]
    w = w1 * w2 - np.sum(v1 * v2, axis=-1)
    v = w1[..., None] * v2 + w2[..., None] * v1 - np.cross(v1, v2)
    return np.concatenate([w[..., None], v], axis=-1)


def qinv(a):
    out = a.copy()
    out[..., 1:] *= -1
    return out


def qexp(A):
    th = np.linalg.norm(A, axis=-1)
    sinc = np.where(th > 1e-12, np.sin(th) / np.where(th > 1e-12, th, 1.0), 1.0 - th**2 / 6)
    return np.concatenate([np.cos(th)[..., None], sinc[..., None] * A], axis=-1)


def qlog(q):
    w = np.clip(q[..., 0], -1.0, 1.0)
    v = q[..., 1:]
    n = np.linalg.norm(v, axis=-1)
    th = np.arctan2(n, w)
    fac = np.where(n > 1e-14, th / np.where(n > 1e-14, n, 1.0), 1.0)
    return fac[..., None] * v


def qdist(a, b):
    return np.linalg.norm(qlog(qmul(a, qinv(b))), axis=-1)


# ---------- lattice: field arr[ix, iy, mu, ...], site spacing one ----------
def shift(n, ix, iy, mu, k=1):
    if mu == 0:
        return (ix + k) % n, iy
    return ix, (iy + k) % n


def plaquette(U):
    """Holonomy of (x, 0), (x + e0, 1), (x + e1, 0)^-1, (x, 1)^-1, all sites."""
    n = U.shape[0]
    ix, iy = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    a = U[ix, iy, 0]
    b = U[(ix + 1) % n, iy, 1]
    c = qinv(U[ix, (iy + 1) % n, 0])
    d = qinv(U[ix, iy, 1])
    return qmul(qmul(qmul(a, b), c), d)


def action(U):
    p = plaquette(U)
    return float(np.sum(1.0 - np.clip(p[..., 0], -1, 1)))


def theta_norm(U):
    return float(np.sqrt(np.sum(np.linalg.norm(qlog(plaquette(U)), axis=-1) ** 2)))


def disp(U, Up):
    return float(np.sqrt(np.sum(qdist(plaquette(Up), plaquette(U)) ** 2)))


def path_steps(start, dest):
    """Axis-ordered comb from start to dest: list of (dx, dy, mu, sign), offsets from origin."""
    steps = []
    x, y = start
    while x != dest[0]:
        if dest[0] > x:
            steps.append((x, y, 0, +1))
            x += 1
        else:
            steps.append((x - 1, y, 0, -1))
            x -= 1
    while y != dest[1]:
        if dest[1] > y:
            steps.append((x, y, 1, +1))
            y += 1
        else:
            steps.append((x, y - 1, 1, -1))
            y -= 1
    return steps


def walk(V, base_x, base_y, steps):
    """Holonomy array along steps, based at sites (base_x, base_y), left to right."""
    n = V.shape[0]
    shape = base_x.shape + (4,)
    q = np.zeros(shape)
    q[..., 0] = 1.0
    for dx, dy, mu, sign in steps:
        link = V[(base_x + dx) % n, (base_y + dy) % n, mu]
        q = qmul(q, link if sign > 0 else qinv(link))
    return q


def contour_sum(theta, base_x, base_y, steps):
    n = theta.shape[0]
    out = np.zeros(base_x.shape + (3,))
    for dx, dy, mu, sign in steps:
        out = out + sign * theta[(base_x + dx) % n, (base_y + dy) % n, mu]
    return out


OFFS = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]


def block_map(V):
    """All-lines log-average, one level, site-centred blocks of side 3."""
    n = V.shape[0]
    m = n // L
    Y0, Y1 = np.meshgrid(np.arange(m) * L, np.arange(m) * L, indexing="ij")
    out = np.zeros((m, m, 2, 4))
    for mu in (0, 1):
        ey = (L, 0) if mu == 0 else (0, L)
        centre = walk(V, Y0, Y1, path_steps((0, 0), ey))
        vs = np.zeros(Y0.shape + (3,))
        for off in OFFS:
            # Gamma_{y,x} . line_x . (Gamma_{y',x'})^-1, with x' = x + L e_mu
            xp = (off[0] + ey[0], off[1] + ey[1])
            steps = path_steps((0, 0), off) + path_steps(off, xp)
            steps = steps + [(s[0], s[1], s[2], -s[3]) for s in reversed(path_steps(ey, xp))]
            om = walk(V, Y0, Y1, steps)
            vs = vs + qlog(qmul(om, qinv(centre)))
        A = vs / len(OFFS)
        out[:, :, mu] = qmul(qexp(A), centre)
    return out


def contour_average(theta):
    """Phi_y theta, on level-(l+1) sites."""
    n = theta.shape[0]
    m = n // L
    Y0, Y1 = np.meshgrid(np.arange(m) * L, np.arange(m) * L, indexing="ij")
    out = np.zeros((m, m, 3))
    for off in OFFS:
        out = out + contour_sum(theta, Y0, Y1, path_steps((0, 0), off))
    return out / len(OFFS)


def N_level(V):
    """N_l(V) := g . M_l(V), g_y = exp(-i Phi_y log V), base point 1."""
    theta = qlog(V)
    M = block_map(V)
    g = qexp(-contour_average(theta))
    m = M.shape[0]
    ix, iy = np.meshgrid(np.arange(m), np.arange(m), indexing="ij")
    out = np.zeros_like(M)
    for mu in (0, 1):
        jx, jy = shift(m, ix, iy, mu)
        out[:, :, mu] = qmul(qmul(g[ix, iy], M[:, :, mu]), qinv(g[jx, jy]))
    return out


def chain_log(a, j):
    V = qexp(a)
    for _ in range(j):
        V = N_level(V)
    return qlog(V)


def path_linear(theta):
    """Q^o at U = 1, one level: the line part only."""
    n = theta.shape[0]
    m = n // L
    out = np.zeros((m, m, 2) + theta.shape[3:])
    for mu in (0, 1):
        for off in OFFS:
            for k in range(L):
                if mu == 0:
                    px, py = (np.arange(m)[:, None] * L + off[0] + k) % n, (np.arange(m)[None, :] * L + off[1]) % n
                else:
                    px, py = (np.arange(m)[:, None] * L + off[0]) % n, (np.arange(m)[None, :] * L + off[1] + k) % n
                out[:, :, mu] = out[:, :, mu] + theta[px, py, mu]
        out[:, :, mu] /= len(OFFS)
    return out


def path_composite(theta, j):
    for _ in range(j):
        theta = path_linear(theta)
    return theta


def wh1(x, s):
    """Whitney lift of a level-j bond field x (n, n, 2, ...) to fine bonds (n s, n s, 2, ...)."""
    n = x.shape[0]
    N = n * s
    out = np.zeros((N, N, 2) + x.shape[3:])
    for mu in (0, 1):
        nu = 1 - mu
        for cx in range(n):
            for cy in range(n):
                val = x[cx, cy, mu]
                base = [cx * s, cy * s]
                for along in range(s):
                    for u in range(-s + 1, s):
                        w = (1.0 - abs(u) / s) / s
                        p = list(base)
                        p[mu] = (p[mu] + along) % N
                        p[nu] = (p[nu] + u) % N
                        out[p[0], p[1], mu] += w * val
    return out


def T_symbol(n, s):
    p = 2 * np.pi * np.fft.fftfreq(n)
    tau = 1.0 - (s**2 - 1) * (1.0 - np.cos(p)) / (4.0 * s**2)
    return tau[:, None] * tau[None, :]


def T_apply(x, s, inverse=False):
    sym = T_symbol(x.shape[0], s)
    if inverse:
        sym = 1.0 / sym
    f = np.fft.fft2(x, axes=(0, 1))
    shape = sym.shape + (1,) * (x.ndim - 2)
    return np.real(np.fft.ifft2(f * sym.reshape(shape), axes=(0, 1)))


def curl(h):
    n = h.shape[0]
    ix, iy = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    return (h[ix, iy, 0] + h[(ix + 1) % n, iy, 1] - h[ix, (iy + 1) % n, 0] - h[ix, iy, 1])


def l4(x):
    return float(np.sum(np.linalg.norm(x, axis=-1) ** 4) ** 0.25)


def l2(x):
    return float(np.sqrt(np.sum(np.linalg.norm(x, axis=-1) ** 2)))


# ---------- T1, T2 ----------
def t1():
    X = np.array([0.0, 1.0, 0.0, 0.0])
    Y = np.array([0.0, 0.0, 1.0, 0.0])
    worst = 0.0
    fd_ok = True
    for t in np.linspace(0.02, 1.55, 60):
        eX, eY = qexp(t * X[1:]), qexp(t * Y[1:])
        hol = qmul(qmul(qmul(eX, eY), qinv(eX)), qinv(eY))
        worst = max(worst, abs(hol[0] - (1 - 2 * np.sin(t) ** 4)))
        theta = np.linalg.norm(qlog(hol))
        fd_ok &= (1 - np.cos(theta)) <= 0.5 * theta**2 + 1e-14
    print(f"T1 commutator square: max |half trace - (1 - 2 sin^4 t)| = {worst:.2e}, (FD) holds = {fd_ok}")
    return worst < 1e-12 and fd_ok


def t2(rng):
    n = 4
    worst = -np.inf
    for k in range(2000):
        scale = rng.choice([0.05, 0.3, 1.0, 2.0])
        U = qexp(scale * rng.normal(size=(n, n, 2, 3)))
        Up = qmul(U, qexp(rng.choice([0.01, 0.1, 0.5, 1.5]) * rng.normal(size=(n, n, 2, 3))))
        S = np.linalg.norm(qlog(plaquette(U)), axis=-1)
        Th = qdist(plaquette(Up), plaquette(U))
        rhs = float(np.sum(S * Th) + 0.5 * np.sum(Th**2))
        worst = max(worst, action(Up) - action(U) - rhs)
    print(f"T2 (FD) at random, in pointwise-summed form: max (lhs - rhs) = {worst:.3e}, must be <= 0")
    return worst <= 1e-12


def t3(rng):
    ok = True
    for j, n in ((1, 9), (2, 9)):
        s = L**j
        x = rng.normal(size=(n, n, 2, 3))
        H = wh1(T_apply(x, s, inverse=True), s)
        back = path_composite(H, j)
        err = float(np.max(np.abs(back - x)))
        print(f"T3 Q^o Wh_1 T^-1 = 1, j = {j}: max error {err:.2e}")
        ok &= err < 1e-10
    return ok


# ---------- T4 ----------
def base_field(kind, N, eps, rng):
    if kind == "noise":
        a = rng.normal(size=(N, N, 2, 3))
    elif kind == "smooth":
        k = 2 * np.pi / N
        ix, iy = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
        a = np.zeros((N, N, 2, 3))
        for mu in (0, 1):
            for c in range(3):
                ph = rng.uniform(0, 2 * np.pi, size=2)
                a[..., mu, c] = np.sin(k * ix + ph[0]) * np.cos(k * iy + ph[1])
    elif kind == "pairs":
        a = np.zeros((N, N, 2, 3))
        for cx in range(0, N, L):
            for cy in range(0, N, L):
                u = rng.normal(size=3)
                u /= np.linalg.norm(u)
                a[(cx - 1) % N, (cy + 1) % N, 0] += u
                a[(cx - 1) % N, (cy - 1) % N, 0] -= u
    else:
        raise ValueError(kind)
    return a * eps / l4(a)


def displacement(kind, n, size, rng):
    h = np.zeros((n, n, 2, 3))
    ctr = n // 2
    if kind == "bump":
        u = rng.normal(size=3)
        u /= np.linalg.norm(u)
        for cx in range(n):
            for cy in range(n):
                w = max(0.0, 1 - abs(cx - ctr) / 3.0) * max(0.0, 1 - abs(cy - ctr) / 3.0)
                h[cx, cy, 0] = w * u
    elif kind == "grad":
        om = np.zeros((n, n, 3))
        for cx in range(n):
            for cy in range(n):
                w = max(0.0, 1 - abs(cx - ctr) / 3.0) * max(0.0, 1 - abs(cy - ctr) / 3.0)
                om[cx, cy] = w * np.array([np.cos(cx), np.sin(cy), 0.3])
        ix, iy = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
        for mu in (0, 1):
            jx, jy = shift(n, ix, iy, mu)
            h[ix, iy, mu] = om[jx, jy] - om[ix, iy]
    elif kind == "rand":
        h[ctr - 2 : ctr + 3, ctr - 2 : ctr + 3] = rng.normal(size=(5, 5, 2, 3))
    else:
        raise ValueError(kind)
    return h * size / l4(h)


def t4(rng):
    worst = {1: 0.0, 2: 0.0}
    passed = True
    n = 9
    print("T4  j base  disp   eps   |h|4   steps  resid     D       |dh|2    D/(|dh|2+(e+h)h)  FD gap")
    for j in (1, 2):
        s = L**j
        N = n * s
        for base in ("noise", "smooth", "pairs"):
            for dk in ("bump", "grad", "rand"):
                for eps in (0.02, 0.05):
                    for hs in (0.01, 0.03):
                        a = base_field(base, N, eps, rng)
                        h = displacement(dk, n, hs, rng)
                        target = chain_log(a, j) + h
                        H = np.zeros_like(a)
                        res = np.inf
                        steps = 0
                        for steps in range(1, 31):
                            r = target - chain_log(a + H, j)
                            res = float(np.max(np.abs(r)))
                            if res < 1e-10:
                                break
                            H = H + wh1(T_apply(r, s, inverse=True), s)
                            check_rss()
                        conv = res < 1e-10
                        U0, U1 = qexp(a), qexp(a + H)
                        D = disp(U0, U1)
                        dh = l2(curl(h))
                        h4 = l4(h)
                        second = (eps + h4) * h4
                        ratio = D / (dh + second)
                        nrm = theta_norm(U0)
                        gap = (action(U1) - action(U0)) - (nrm * D + 0.5 * D**2)
                        ok_b = D <= 8 * dh + 8 * second
                        ok_d = gap <= 1e-12
                        worst[j] = max(worst[j], ratio)
                        passed &= conv and ok_b and ok_d
                        flag = "" if (conv and ok_b and ok_d) else "  <-- FAIL"
                        print(f"T4  {j} {base:6s} {dk:5s} {eps:.2f}  {hs:.2f}  {steps:3d}  {res:.1e} {D:.3e} {dh:.3e}  {ratio:7.3f}  {gap:.2e}{flag}", flush=True)
    growth = worst[2] / worst[1]
    print(f"T4 worst ratio: j = 1: {worst[1]:.3f}, j = 2: {worst[2]:.3f}, growth {growth:.3f} (limit 1.5)")
    return passed and growth <= 1.5


def main():
    rng = np.random.default_rng(20261101)
    results = {"T1": t1(), "T2": t2(rng), "T3": t3(rng)}
    if results["T3"]:
        results["T4"] = t4(rng)
    else:
        print("T3 failed: T4 void")
    for k, v in results.items():
        print(k, "PASS" if v else "FAIL")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9
    print(f"max RSS {rss:.2f} GB")


if __name__ == "__main__":
    main()
