#!/usr/bin/env python3
"""Exact small-model tests of the strip bound (Lemma 10.1), and of the claim in
Theorem 10.2(e) that moving one interior observable alone is covered by it.

Model A: 2D SU(2) on S x T torus, exact in characters. F, G = half-trace of the
         spatial Polyakov loop on one slice (multiplication operators, h = 0).
Model B: 3D Z_2 Wilson gauge theory on a 2 x 2 x T torus (8 spatial links, 256
         states, exact transfer matrix). Thick slabs (h = 1), including functions
         that are not gauge invariant. Not SU(2), but it has the same structure
         (T_1 = K P, positive-type phi), and it has a non-diagonal transfer matrix,
         which the 2D model does not.

Prints the worst ratio |f(x+iy)| / (||F|| ||G||) and the derivative bound.
"""
import itertools
import numpy as np

np.set_printoptions(precision=5, suppress=True, linewidth=120)


# ---------------- Model A: 2D SU(2) ----------------
def su2_a_j(beta, nj):
    """a_j = int dU exp(-beta s(U)) chi_j(U)/d_j, s = 1 - cos(theta), j = n/2."""
    th, w = np.polynomial.legendre.leggauss(1500)
    th = 0.5 * np.pi * (th + 1)
    w = 0.5 * np.pi * w
    meas = (2 / np.pi) * np.sin(th) ** 2 * w
    out = np.zeros(nj)
    base = np.exp(-beta * (1 - np.cos(th)))
    for n in range(nj):
        chi = np.sin((n + 1) * th) / np.sin(th)
        out[n] = np.sum(meas * base * chi) / (n + 1)
    return out


def model_a():
    print("Model A: 2D SU(2), Polyakov loops, exact characters")
    worst = 0.0
    worstd = 0.0
    for beta in [0.0, 1.0, 25.0, 400.0]:
        for S, T in [(1, 8), (4, 16), (3, 64)]:
            nj = 80
            a = su2_a_j(beta, nj)
            a = np.maximum(a, 0.0)
            lam = (a / a[0]) ** S  # normalised eigenvalues >= 0, index n = 2j
            Z = np.sum(lam ** T)
            # F = (1/2) chi_{1/2}: acts |n> -> (1/2)(|n+1> + |n-1>), ||F||_inf = 1.
            n = np.arange(nj)
            F2 = np.zeros((nj, nj))
            for i in range(nj - 1):
                F2[i, i + 1] = F2[i + 1, i] = 0.25
            N = T
            for x in np.linspace(0.05, N - 0.05, 15):
                for y in [0.0, 0.3, 3.0, 30.0]:
                    # f = Z^-1 sum lam_k^z lam_l^(N-z) |F_lk|^2 ; here F = G
                    lk = np.where(lam > 0, lam, 1e-300)
                    Az = np.exp((x + 1j * y) * np.log(lk))
                    Bz = np.exp((N - x - 1j * y) * np.log(lk))
                    val = abs(np.sum(np.outer(Bz, Az) * F2)) / Z
                    worst = max(worst, val)
            # derivative bound at integer m: |f'(m)| <= 1 / min(m, N-m)
            for m in range(1, N):
                t = min(m, N - m)
                lk = np.where(lam > 0, lam, 1e-300)
                Az = lk ** m
                Bz = lk ** (N - m)
                d = abs(np.sum(np.outer(Bz, Az * np.log(lk)) * F2
                               - np.outer(Bz * np.log(lk), Az) * F2)) / Z
                worstd = max(worstd, d * t)
    print("  worst |f| / (||F|| ||G||) over all beta, S, T, strip grid: %.6f (bound 1)" % worst)
    print("  worst t |f'(m)| / (||F|| ||G||):                            %.6f (bound 1)" % worstd)


# ---------------- Model B: 3D Z_2 on 2 x 2 x T ----------------
# Spatial torus 2 x 2. Sites (i,j), i,j in {0,1}. Spatial links: 8. Temporal links per step: 4.
sites = [(i, j) for i in range(2) for j in range(2)]
sid = {s: k for k, s in enumerate(sites)}
links = []  # (site, dir)
for s in sites:
    for d in (0, 1):
        links.append((s, d))
lid = {l: k for k, l in enumerate(links)}


def shift(s, d):
    s = list(s)
    s[d] = (s[d] + 1) % 2
    return tuple(s)


# spatial plaquettes on a 2 x 2 torus: 4 of them
plaqs = []
for s in sites:
    plaqs.append((lid[(s, 0)], lid[(shift(s, 0), 1)], lid[(shift(s, 1), 0)], lid[(s, 1)]))

conf = np.array(list(itertools.product([1, -1], repeat=8)), dtype=np.int8)  # 256 x 8
utemp = np.array(list(itertools.product([1, -1], repeat=4)), dtype=np.int8)  # 16 x 4


def build(beta):
    """Return W_s (diag) and the kernel array B[u, eta, eta'] of temporal plaquettes."""
    Ws = np.zeros(256)
    for p in plaqs:
        up = conf[:, p[0]] * conf[:, p[1]] * conf[:, p[2]] * conf[:, p[3]]
        Ws += 1 - up
    h = np.exp(-(beta / 2) * Ws)
    # temporal plaquette on spatial link l=(s,d): s_p = 1 - eta_l u_{s+d} eta'_l u_s
    B = np.zeros((16, 256, 256))
    for iu, u in enumerate(utemp):
        expo = np.zeros((256, 256))
        for (s, d), l in lid.items():
            sign = int(u[sid[s]]) * int(u[sid[shift(s, d)]])
            expo += 1 - sign * np.outer(conf[:, l], conf[:, l])
        B[iu] = np.exp(-beta * expo)
    return h, B


def slab_op(h, B, F=None):
    """Kernel of the one-step slab with insertion F(u, eta, eta') (None = 1)."""
    if F is None:
        K = B.sum(axis=0) / 16
    else:
        K = (B * F).sum(axis=0) / 16
    return (h[:, None] * K * h[None, :]) / 256  # normalised Haar on eta too


def insert_funcs():
    """Thick (h = 1) functions, bounded by 1:
       Ftemp: temporal plaquette; Flink: one temporal link (NOT gauge invariant);
       Fmix: product of a spatial plaquette on eta, one on eta', and temporal plaquette."""
    F = {}
    u0 = utemp[:, sid[(0, 0)]].astype(float)
    u1 = utemp[:, sid[(1, 0)]].astype(float)
    eta = conf[:, lid[((0, 0), 0)]].astype(float)
    Ftemp = np.einsum('u,i,j->uij', u0 * u1, eta, eta)
    F['temporal plaquette'] = Ftemp
    F['single temporal link'] = np.einsum('u,i,j->uij', u0, np.ones(256), np.ones(256))
    p0 = plaqs[0]
    up = (conf[:, p0[0]] * conf[:, p0[1]] * conf[:, p0[2]] * conf[:, p0[3]]).astype(float)
    F['spatial x temporal x spatial'] = np.einsum('u,i,j->uij', u0 * u1, up * eta, up * eta)
    # the (1 + temporal plaquette)/2 projector, not centred and positive
    F['positive projector'] = (1 + Ftemp) / 2
    return F


def model_b():
    print("Model B: 3D Z_2 on 2 x 2 x T, exact transfer matrix, thick slabs")
    funcs = insert_funcs()
    worst = {k: 0.0 for k in funcs}
    worstd = {k: 0.0 for k in funcs}
    worst3 = 0.0
    worst3info = None
    for beta in [0.05, 0.44, 1.5, 4.0]:
        h, B = build(beta)
        T1 = slab_op(h, B)
        T1 = 0.5 * (T1 + T1.T)
        ev, Q = np.linalg.eigh(T1)
        ev[np.abs(ev) < 1e-13 * ev.max()] = 0.0
        if ev.min() < -1e-10 * ev.max():
            print("  beta %.3g: NEGATIVE eigenvalue %g" % (beta, ev.min()))
        lam = ev / ev.max()
        good = lam > 0
        lq = np.where(good, np.log(np.where(good, lam, 1)), -np.inf)
        scale = ev.max()
        ops = {k: Q.T @ slab_op(h, B, funcs[k]) @ Q / scale for k in funcs}
        for T in [7, 10, 24]:
            Z = np.sum(np.where(good, np.exp(T * lq), 0.0))
            N = T - 2  # h = 1 for both
            for k, Fh in ops.items():
                # G = F: f(z) = Z^-1 sum_{k,l} lam_k^z lam_l^(N-z) <l|F|k><k|F|l>
                M = Fh * Fh.T
                for x in np.linspace(0.1, N - 0.1, 11):
                    for y in [0.0, 0.5, 5.0, 37.0]:
                        Az = np.where(good, np.exp((x + 1j * y) * lq), 0.0)
                        Bz = np.where(good, np.exp((N - x - 1j * y) * lq), 0.0)
                        val = abs(Bz @ M @ Az) / Z
                        worst[k] = max(worst[k], val)
                for m in range(1, N):
                    t = min(m, N - m)
                    Az = np.where(good, np.exp(m * lq), 0.0)
                    Bz = np.where(good, np.exp((N - m) * lq), 0.0)
                    dA = np.where(good, Az * lq, 0.0)
                    dB = np.where(good, Bz * lq, 0.0)
                    d = abs(Bz @ M @ dA - dB @ M @ Az) / Z
                    worstd[k] = max(worstd[k], d * t)
            # Interior observable moved alone: Tr(F T^(m1+z) A T^(m2-z) G T^r) / Z, all thick.
            # Is |g(z)| <= ||F|| ||A|| ||G|| off the real axis?
            names = list(ops)
            if T >= 10:
                r = T - 3 - 4
                if r >= 0:
                    m1, m2 = 2, 2
                    for a_name in names:
                        for f_name in names:
                            FF = ops[f_name]
                            AA = ops[a_name]
                            GG = ops[f_name].T
                            Dr = np.where(good, np.exp(r * lq), 0.0)
                            for x in [-1.0, 0.0, 1.0]:
                                for y in [0.0, 0.7, 2.1, 5.3, 11.0, 37.0]:
                                    D1 = np.where(good, np.exp((m1 + x + 1j * y) * lq), 0.0)
                                    D2 = np.where(good, np.exp((m2 - x - 1j * y) * lq), 0.0)
                                    val = abs(np.trace((FF * D1[None, :]) @ (AA * D2[None, :]) @ (GG * Dr[None, :]))) / Z
                                    if val > worst3:
                                        worst3 = val
                                        worst3info = (beta, T, a_name, f_name, x, y)
    for k in funcs:
        print("  %-30s worst |f|/(||F||||G||) = %.6f, worst t|f'(m)| = %.6f" % (k, worst[k], worstd[k]))
    print("  moving a thick interior observable alone: worst |g(z)|/(sup norms) = %.6f at %s" % (worst3, worst3info))
    # Negative test: where positivity is used.
    h, B = build(-0.5)
    T1 = slab_op(h, B)
    ev = np.linalg.eigvalsh(0.5 * (T1 + T1.T))
    print("  control: beta = -0.5 gives min eigenvalue / max |eigenvalue| = %.4f" % (ev.min() / np.abs(ev).max()))


if __name__ == "__main__":
    model_a()
    model_b()
