#!/usr/bin/env python3
"""One-step transport of plaquette energy under Balaban's average, d = 4. Consumer: Lemma TE, library/relative-density-bound.md.

Written before running. Lattice N = L n_c, odd L, block B(y) = y + [-h, h]^4, h = (L-1)/2. For a parent bond (y, mu):
W_r := T(y, y+r) Line_mu(y+r) T(y', y'+r)^-1, axis-ordered contours T, and V' := exp(avg_r log(W_r W_0^-1)) W_0.
Square S_x := the L x L square of (mu, nu) plaquettes with corner x. rho(p; P') := L^-4 #{x in B(y): p in S_x}.
Claims: theta'(P') = sum_p rho(p; P') theta_p at the abelian level; sum_{P'} L^2 rho(p; P') = 1.

PRE-STATED criteria.
 T1 (exact identity). Random U(1) field of size 1e-3, L = 3, 5, n_c = 3: max |theta' - sum rho theta| < 1e-10.
 T2 (Jensen). Same fields: sum t^2 <= sum e^2 (1 + 1e-10). Uniform flux on the torus: sum t^2 / sum e^2 = 1 within 1e-9.
 T3 (cubic structure, SU(2), no exclusion). e_p, t_P' := angles of the holonomies. G := (sum t^2 - sum e^2) / sum t^3, the K that
    phi(e) = e^2 - K e^3 needs, up to sum e^3 << sum t^3. Smooth low-mode fields of link size s, then random search over mode
    amplitudes, phases and colours; G_max(s) := largest G found. Claim: no growth as s -> 0: G_max(s/2) <= 1.5 G_max(s) + 1e-3 for
    s = 0.04, 0.02, 0.01, at L = 3, and L = 5 with fewer trials. Growth like 1/s would mean a failure of monotonicity at second order.
 T4 (cost of one excluded cube, abelian). Uniform flux T = 1 per (0, 1) plaquette, one parent plaquette, unit cube Q, largest over
    positions in the block. Delta(L) := |theta'_excl - T sum_{p not in Q} rho(p)|. Claim: Delta(L) <= C/L: L Delta(L) at L = 11 is at
    most 2 times its value at L = 5.
Added after the first run, before running it, because T3's fields were all far from the equality case (G_max < 0 throughout):
 T5 (near the equality case, SU(2)). Constant links U(x, mu) = exp(i a_mu), with a_mu in su(2) of size s, so every plaquette has about
    the same non-abelian flux, plus a low-mode perturbation of relative size 0.1 in half of the trials. Random search over the a_mu.
    G as in T3. Claim: G_max(s/2) <= 1.5 G_max(s) + 1e-3 for s = 0.08, 0.04, 0.02, at L = 3 and 5, and K = max(G_max, 0) with
    K t_max <= 1/2 at s = 0.02.
FAIL if any fails. Limitations: T3 is a search, not a supremum; T4 is one field, a lower bound on the supremum over fields with flux at
most T. RSS guard 2 GB.
"""
import itertools
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


def qmul(a, b):
    w = a[..., 0] * b[..., 0] - a[..., 1] * b[..., 1] - a[..., 2] * b[..., 2] - a[..., 3] * b[..., 3]
    x = a[..., 0] * b[..., 1] + a[..., 1] * b[..., 0] + a[..., 2] * b[..., 3] - a[..., 3] * b[..., 2]
    y = a[..., 0] * b[..., 2] - a[..., 1] * b[..., 3] + a[..., 2] * b[..., 0] + a[..., 3] * b[..., 1]
    z = a[..., 0] * b[..., 3] + a[..., 1] * b[..., 2] - a[..., 2] * b[..., 1] + a[..., 3] * b[..., 0]
    return np.stack([w, x, y, z], axis=-1)


def qconj(a):
    out = a.copy()
    out[..., 1:] *= -1
    return out


def qexp(v):
    n = np.linalg.norm(v, axis=-1)
    s = np.sinc(n / np.pi)  # sin(n)/n
    return np.concatenate([np.cos(n)[..., None], s[..., None] * v], axis=-1)


def qlog(q):
    im = q[..., 1:]
    sn = np.linalg.norm(im, axis=-1)
    a = np.arctan2(sn, q[..., 0])
    f = np.where(sn > 1e-14, a / np.maximum(sn, 1e-300), 1.0)
    return f[..., None] * im


class Kernel:
    """Field U: shape (N, N, N, N, 4, 4), quaternions, U[x, mu]."""

    def __init__(self, L, nc):
        self.L, self.nc, self.h, self.N = L, nc, (L - 1) // 2, L * nc
        h = self.h
        rs = np.array(list(itertools.product(range(-h, h + 1), repeat=4)))
        self.rs = rs
        ms = np.array(list(itertools.product(range(nc), repeat=4)))
        self.ms = ms
        self.ys = h + L * ms
        self.mi = lambda m: np.ravel_multi_index(tuple(np.mod(m, nc).T), (nc,) * 4)

    def seg(self, U):
        """Seg[d][s + h]: transport from x to x + s e_d."""
        h, out = self.h, []
        for d in range(4):
            u = U[..., d, :]
            pos = [None] * (h + 1)
            pos[0] = np.zeros_like(u)
            pos[0][..., 0] = 1.0
            for s in range(1, h + 1):
                pos[s] = qmul(pos[s - 1], np.roll(u, -(s - 1), axis=d))
            arr = {0: pos[0]}
            for s in range(1, h + 1):
                arr[s] = pos[s]
                arr[-s] = np.roll(qconj(pos[s]), s, axis=d)
            out.append(arr)
        return out

    def line(self, U):
        L, out = self.L, []
        for d in range(4):
            u = U[..., d, :]
            acc = u.copy()
            for s in range(1, L):
                acc = qmul(acc, np.roll(u, -s, axis=d))
            out.append(acc)
        return out

    def parents(self, U):
        h, N, nc, L = self.h, self.N, self.nc, self.L
        seg, line = self.seg(U), self.line(U)
        n_m, n_r = len(self.ms), len(self.rs)
        site = (self.ys[:, None, :] + self.rs[None, :, :]) % N
        T = np.zeros((n_m, n_r, 4))
        T[..., 0] = 1.0
        here = np.repeat(self.ys[:, None, :], n_r, axis=1) % N
        for d in range(4):
            for s in range(-h, h + 1):
                mask = self.rs[:, d] == s
                if not mask.any():
                    continue
                idx = here[:, mask]
                piece = seg[d][s][idx[..., 0], idx[..., 1], idx[..., 2], idx[..., 3]]
                T[:, mask] = qmul(T[:, mask], piece)
                here[:, mask, d] = (here[:, mask, d] + s) % N
        V = np.zeros((n_m, 4, 4))
        c0 = np.where((self.rs == 0).all(axis=1))[0][0]
        for mu in range(4):
            nxt = self.ms.copy()
            nxt[:, mu] += 1
            j = self.mi(nxt)
            Lm = line[mu][site[..., 0], site[..., 1], site[..., 2], site[..., 3]]
            W = qmul(qmul(T, Lm), qconj(T[j]))
            W0 = W[:, c0][:, None, :]
            avg = qlog(qmul(W, qconj(W0))).mean(axis=1)
            V[:, mu] = qmul(qexp(avg), W0[:, 0])
        return V

    def parent_plaq(self, V):
        out = {}
        for mu in range(4):
            for nu in range(mu + 1, 4):
                a = self.ms.copy()
                a[:, mu] += 1
                b = self.ms.copy()
                b[:, nu] += 1
                out[(mu, nu)] = qmul(qmul(qmul(V[:, mu], V[self.mi(a), nu]), qconj(V[self.mi(b), mu])), qconj(V[:, nu]))
        return out


def fine_plaq(U):
    out = {}
    for mu in range(4):
        for nu in range(mu + 1, 4):
            a, b = U[..., mu, :], U[..., nu, :]
            out[(mu, nu)] = qmul(qmul(qmul(a, np.roll(b, -1, axis=mu)), qconj(np.roll(a, -1, axis=nu))), qconj(b))
    return out


def angles(pl):
    return {k: np.linalg.norm(qlog(v), axis=-1) for k, v in pl.items()}


def abelian(a):
    q = np.zeros(a.shape + (4,))
    q[..., 0], q[..., 3] = np.cos(a), np.sin(a)
    return q


def predicted(k, theta_mu_nu, mu, nu):
    """sum_p rho(p; P') theta_p for all P' of orientation (mu, nu)."""
    L, h = k.L, k.h
    out = np.zeros(len(k.ms))
    ax = np.array(np.indices((k.N,) * 4)).reshape(4, -1).T  # not used below, kept small
    del ax
    # theta(S_x) for all x, by cumulative rolling
    S = theta_mu_nu.copy()
    acc = np.zeros_like(S)
    for i in range(L):
        for j in range(L):
            acc += np.roll(np.roll(S, -i, axis=mu), -j, axis=nu)
    for n, y in enumerate(k.ys):
        idx = (y[None, :] + k.rs) % k.N
        out[n] = acc[idx[:, 0], idx[:, 1], idx[:, 2], idx[:, 3]].mean()
    return out


def t1_t2(L, nc, rng):
    k = Kernel(L, nc)
    a = 1e-3 * rng.standard_normal((k.N,) * 4 + (4,))
    U = abelian(a)
    V = k.parents(U)
    P = k.parent_plaq(V)
    F = fine_plaq(U)
    err, st, se = 0.0, 0.0, 0.0
    for key in P:
        mu, nu = key
        th = qlog(F[key])[..., 2]
        thp = qlog(P[key])[..., 2]
        err = max(err, float(np.abs(thp - predicted(k, th, mu, nu)).max()))
        st += float((thp**2).sum())
        se += float((th**2).sum())
    # uniform flux in the (0, 1) plane on the torus
    N = k.N
    th0 = 2 * np.pi / N**2
    a2 = np.zeros((N,) * 4 + (4,))
    x0 = np.arange(N).reshape(N, 1, 1, 1)
    x1 = np.arange(N).reshape(1, N, 1, 1)
    a2[..., 1] = th0 * x0
    a2[N - 1, :, :, :, 0] = -th0 * N * x1[0, :, :, :]
    Uu = abelian(a2)
    Pu = k.parent_plaq(k.parents(Uu))
    Fu = fine_plaq(Uu)
    tu = sum(float((angles({q: Pu[q]})[q] ** 2).sum()) for q in Pu)
    eu = sum(float((angles({q: Fu[q]})[q] ** 2).sum()) for q in Fu)
    guard()
    return err, st / se, tu / eu


class Modes:
    def __init__(self, rng, n=6):
        self.amp = rng.standard_normal((n, 4, 3))
        self.k = rng.integers(-1, 2, size=(n, 4))
        for i in range(n):
            if not self.k[i].any():
                self.k[i, rng.integers(4)] = 1
        self.ph = rng.uniform(0, 2 * np.pi, size=(n, 4, 3))

    def jiggle(self, rng, w):
        o = Modes.__new__(Modes)
        o.amp = self.amp + w * rng.standard_normal(self.amp.shape)
        o.k = self.k.copy()
        o.ph = self.ph + w * rng.standard_normal(self.ph.shape)
        return o

    def field(self, N, s):
        g = np.indices((N,) * 4).astype(float)
        v = np.zeros((N,) * 4 + (4, 3))
        norm = 0.0
        for i in range(len(self.k)):
            arg = 2 * np.pi * sum(self.k[i, d] * g[d] for d in range(4)) / N
            for mu in range(4):
                for c in range(3):
                    v[..., mu, c] += self.amp[i, mu, c] * np.cos(arg + self.ph[i, mu, c])
        norm = float(np.abs(v).max())
        return qexp(s * v / norm)


def t3_value(k, U):
    t = angles(k.parent_plaq(k.parents(U)))
    e = angles(fine_plaq(U))
    st2 = sum(float((v**2).sum()) for v in t.values())
    st3 = sum(float((v**3).sum()) for v in t.values())
    se2 = sum(float((v**2).sum()) for v in e.values())
    se3 = sum(float((v**3).sum()) for v in e.values())
    tmax = max(float(v.max()) for v in t.values())
    return (st2 - se2) / st3, se3 / st3, tmax


def t3(L, nc, trials, rng):
    k = Kernel(L, nc)
    res = {}
    start = Modes(rng)
    for s in (0.04, 0.02, 0.01):
        best, bm, info = -np.inf, start, None
        for _ in range(max(10, trials // 5)):
            m = Modes(rng)
            g, r, tm = t3_value(k, m.field(k.N, s))
            if g > best:
                best, bm, info = g, m, (r, tm)
        for i in range(trials):
            m = bm.jiggle(rng, 0.2)
            g, r, tm = t3_value(k, m.field(k.N, s))
            if g > best:
                best, bm, info = g, m, (r, tm)
            guard()
        res[s] = (best, info)
        print(f"T3 L={L} s={s}: G_max={best:.4g}, sum e^3/sum t^3={info[0]:.3g}, t_max={info[1]:.3g}, rss={rss_gb():.2f}GB", flush=True)
    return res


def t5(L, nc, trials, rng):
    k = Kernel(L, nc)
    N = k.N
    res = {}
    for s in (0.08, 0.04, 0.02):
        best, ba, info = -np.inf, None, None
        for i in range(trials):
            if ba is None or i < trials // 4:
                a = rng.standard_normal((4, 3))
            else:
                a = ba + 0.15 * rng.standard_normal((4, 3))
            a = a / np.abs(a).max()
            U = qexp(np.broadcast_to(s * a, (N,) * 4 + (4, 3)).copy())
            if i % 2 == 1:
                U = qmul(U, Modes(rng, n=3).field(N, 0.1 * s))
            g, r, tm = t3_value(k, U)
            if g > best:
                best, ba, info = g, a, (r, tm)
            guard()
        res[s] = (best, info)
        print(f"T5 L={L} s={s}: G_max={best:.4g}, sum e^3/sum t^3={info[0]:.3g}, t_max={info[1]:.3g}, rss={rss_gb():.2f}GB", flush=True)
    return res


def t4(L, side=1):
    """Closed forms for a_1 = x_0, a_0 = a_2 = a_3 = 0 on the infinite lattice, parent plaquette at y = 0, mu = 0, nu = 1."""
    h = (L - 1) // 2
    rng1 = np.arange(-h, h + 1)
    R = np.stack(np.meshgrid(rng1, rng1, rng1, rng1, indexing="ij"), axis=-1).reshape(-1, 4)
    corners = {1: (np.array([0, 0, 0, 0]), 0, +1), 2: (np.array([L, 0, 0, 0]), 1, +1), 3: (np.array([0, L, 0, 0]), 0, -1), 4: (np.array([0, 0, 0, 0]), 1, -1)}

    def gamma(y, x):
        return x[..., 0] * (x[..., 1] - y[1])  # along dir 0 first, where a_0 = 0; then along dir 1 at fixed x_0

    def bond(y, d, keep):
        x = y + R
        ye = y.copy()
        ye[d] += L
        xe = x.copy()
        xe[:, d] += L
        line = x[:, 0] * L if d == 1 else np.zeros(len(x))
        val = gamma(y, x) + line - gamma(ye, xe)
        return val[keep].mean()

    def rho_mass(z):
        # sum over p in Q of rho(p; P'), with p of orientation (0, 1)
        total = 0.0
        for off in itertools.product(range(side), repeat=4):
            p = z + np.array(off)
            n0 = max(0, min(L, L - abs(p[0] - h)))  # number of x_0 in [-h, h] with p_0 in [x_0, x_0 + L)
            n1 = max(0, min(L, L - abs(p[1] - h)))
            n2 = 1 if abs(p[2]) <= h else 0
            n3 = 1 if abs(p[3]) <= h else 0
            total += n0 * n1 * n2 * n3 / L**4
        return total

    worst = 0.0
    step = max(1, L // 3)
    for z in itertools.product(range(-h, L + h, step), range(-h, L + h, step), range(-h, h + 1, step), range(-h, h + 1, step)):
        z = np.array(z)
        val = 0.0
        for _, (y, d, sg) in corners.items():
            x = y + R
            hit = np.zeros(len(x), dtype=bool)
            for s in range(L):
                pt = x.copy()
                pt[:, d] += s
                hit |= ((pt >= z) & (pt < z + side)).all(axis=1)
            val += sg * bond(y, d, ~hit)
        worst = max(worst, abs(val - (L**2 - rho_mass(z))))
    guard()
    return worst


def main():
    rng = np.random.default_rng(20261031)
    ok = True
    for L in (3, 5):
        err, ratio, ru = t1_t2(L, 3, rng)
        c1, c2 = err < 1e-10, ratio <= 1 + 1e-10 and abs(ru - 1) < 1e-9
        ok = ok and c1 and c2
        print(f"T1 L={L}: max error {err:.2e} {c1}; T2 sum t^2/sum e^2 = {ratio:.4f}, uniform flux {ru:.10f} {c2}, rss={rss_gb():.2f}GB", flush=True)
    for L, trials in ((3, 150), (5, 25)):
        r = t3(L, 3, trials, rng)
        for a, b in ((0.04, 0.02), (0.02, 0.01)):
            good = r[b][0] <= 1.5 * r[a][0] + 1e-3 if r[a][0] > 0 else r[b][0] <= 1e-3
            ok = ok and good
            print(f"T3 L={L}: G_max({b})={r[b][0]:.4g} against G_max({a})={r[a][0]:.4g}: {good}", flush=True)
    for L, trials in ((3, 120), (5, 30)):
        r = t5(L, 3, trials, rng)
        for a, b in ((0.08, 0.04), (0.04, 0.02)):
            good = r[b][0] <= 1.5 * r[a][0] + 1e-3 if r[a][0] > 0 else r[b][0] <= 1e-3
            ok = ok and good
            print(f"T5 L={L}: G_max({b})={r[b][0]:.4g} against G_max({a})={r[a][0]:.4g}: {good}", flush=True)
        kt = max(r[0.02][0], 0.0) * r[0.02][1][1]
        ok = ok and kt <= 0.5
        print(f"T5 L={L}: K t_max at s=0.02 = {kt:.3g}: {kt <= 0.5}", flush=True)
    d = {L: t4(L) for L in (5, 7, 9, 11)}
    for L in d:
        print(f"T4 L={L}: Delta={d[L]:.4g}, L Delta={L*d[L]:.4g}, cube side 1", flush=True)
    c4 = 11 * d[11] <= 2 * 5 * d[5]
    ok = ok and c4
    print(f"T4: {c4}; side 2 at L=9: Delta={t4(9, side=2):.4g}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
