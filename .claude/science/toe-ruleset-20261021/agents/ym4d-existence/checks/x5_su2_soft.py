"""Check x5: the compact SU(2) soft chain (EXISTENCE §15). Criteria: checks/x5_criteria.md (written first).

d = 4, L = 3, literal S4' contours (24 orders x 81 offsets, deduplicated with multiplicities), SU(2) as unit
quaternions (tr U / 2 = q0; the matrix average is the quaternion average). Seeded sampling; every Monte Carlo number
carries its standard error.
"""
import itertools
import sys
import time

import numpy as np
from scipy.special import ive

L, D = 3, 4
O = (L - 1) // 2
out = []


def say(s):
    out.append(s)
    print(s, flush=True)


# ------------------------------------------------------------------ quaternion utilities
def qmul(p, q):
    a1, b1, c1, d1 = p[..., 0], p[..., 1], p[..., 2], p[..., 3]
    a2, b2, c2, d2 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return np.stack([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                     a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                     a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2], axis=-1)


def qconj(q):
    r = q.copy()
    r[..., 1:] *= -1
    return r


def qmat(q):
    """2x2 complex matrix of a quaternion (a faithful representation)."""
    w, x, y, z = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    m = np.empty(q.shape[:-1] + (2, 2), dtype=complex)
    m[..., 0, 0] = w + 1j * z
    m[..., 0, 1] = y + 1j * x
    m[..., 1, 0] = -y + 1j * x
    m[..., 1, 1] = w - 1j * z
    return m


def haar(rng, shape):
    g = rng.standard_normal(shape + (4,))
    return g / np.linalg.norm(g, axis=-1, keepdims=True)


def a_of_t(t):
    return ive(2, t) / ive(1, t)


def fisher(rng, t, n):
    """n samples of mu_t: Haar density prop. to exp(t q0) on S^3 (rejection, chunked to bound memory)."""
    w = np.empty(n)
    filled = 0
    while filled < n:
        m = min(int((n - filled) * (2.0 + 1.6 * np.sqrt(t))) + 1000, 4_000_000)
        u = rng.random(m)
        x = 1.0 + np.log1p(-u * (-np.expm1(-2.0 * t))) / t        # density prop. to e^{t x} on [-1, 1]
        acc = rng.random(m) < np.sqrt(np.clip(1.0 - x * x, 0.0, None))
        x = x[acc][: n - filled]
        w[filled: filled + len(x)] = x
        filled += len(x)
    v = rng.standard_normal((n, 3))
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    q = np.empty((n, 4))
    q[:, 0] = w
    q[:, 1:] = v * np.sqrt(np.clip(1.0 - w * w, 0.0, None))[:, None]
    return q


def mean_se(x):
    x = np.asarray(x, dtype=float)
    return x.mean(), x.std(ddof=1) / np.sqrt(len(x))


# ------------------------------------------------------------------ A: exact one-step identities
def part_a():
    rng = np.random.default_rng(20261027)
    ok = True
    # A1
    dev = 0.0
    for _ in range(1000):
        q = haar(rng, (7,))
        w = rng.dirichlet(np.ones(7))
        M = qmat(q)
        Mbar = np.einsum('i,ijk->jk', w, M)
        r2 = np.real(np.linalg.det(Mbar))
        dev = max(dev, np.abs(Mbar.conj().T @ Mbar - r2 * np.eye(2)).max(),
                  np.abs(qmat((w[:, None] * q).sum(0)) - Mbar).max())
    say(f"A1 max |Mbar^dag Mbar - det(Mbar) 1|, |quaternion avg - matrix avg| = {dev:.2e}")
    ok &= dev <= 1e-12
    # A2
    for t in (5.0, 20.0, 100.0):
        z = fisher(rng, t, 2_000_000)
        m, se = mean_se(z[:, 0])
        ex = a_of_t(t)
        say(f"A2 t={t:6.1f}: mean q0 = {m:.6f} +- {se:.1e}, I2/I1 = {ex:.6f}, |diff|/SE = {abs(m - ex) / se:.2f}")
        ok &= abs(m - ex) <= 4 * se
    ts = np.logspace(-1, 4, 400)
    gap = 1.0 - a_of_t(ts)
    worst = (gap * 2 * ts / 3).max()
    say(f"A2 bound: min(1 - a) = {gap.min():.3e} (>= 0), max (1 - a)/(3/(2t)) = {worst:.6f} (<= 1)")
    ok &= gap.min() >= 0 and worst <= 1 + 1e-12
    # A3 (i): convolution identity on one plaquette with random background
    Wc = haar(rng, (4,))
    tc = np.array([8.0, 15.0, 30.0, 60.0])

    def plaq(v1, v2, v3, v4):
        return qmul(qmul(qmul(v1, v2), qconj(v3)), qconj(v4))

    WP = plaq(*[Wc[i] for i in range(4)])
    pred = np.prod(a_of_t(tc)) * WP[0]
    vals, vecs = [], []
    for _ in range(4):
        n = 1_000_000
        V = [qmul(np.broadcast_to(Wc[i], (n, 4)), fisher(rng, tc[i], n)) for i in range(4)]
        VP = plaq(*V)
        vals.append(VP[:, 0])
        vecs.append(qmul(np.broadcast_to(qconj(WP), (n, 4)), VP)[:, 1:])
    vals = np.concatenate(vals)
    vecs = np.concatenate(vecs)
    m, se = mean_se(vals)
    say(f"A3 E[tr V_P/2] = {m:.6f} +- {se:.1e}; prod a(t_c) tr W_P/2 = {pred:.6f}; |diff|/SE = {abs(m - pred) / se:.2f}")
    ok &= abs(m - pred) <= 4 * se
    for k in range(3):
        mk, sk = mean_se(vecs[:, k])
        say(f"A3 location: mean vector part of W_P^-1 V_P, comp {k}: {mk:+.2e} +- {sk:.1e} ({abs(mk) / sk:.2f} SE)")
        ok &= abs(mk) <= 4 * sk
    # A3 (ii): the normalised kernel itself, by rejection from Haar
    T = haar(rng, (7,))
    T = qmul(np.broadcast_to(haar(rng, ()), (7, 4)), (T * np.array([3, 1, 1, 1]))
             / np.linalg.norm(T * np.array([3, 1, 1, 1]), axis=-1, keepdims=True))
    w = rng.dirichlet(np.ones(7))
    Mq = (w[:, None] * T).sum(0)
    r = np.linalg.norm(Mq)
    Wq = Mq / r
    beta = 6.0 / r                       # kappa / g^2 chosen so that t = kappa r / g^2 = 6
    acc_q = []
    while sum(len(a) for a in acc_q) < 200_000:
        V = haar(rng, (1_000_000,))
        keep = rng.random(len(V)) < np.exp(beta * (V @ Mq - r))
        acc_q.append(V[keep])
    V = np.concatenate(acc_q)
    Z = qmul(np.broadcast_to(qconj(Wq), V.shape), V)
    m, se = mean_se(Z[:, 0])
    say(f"A3 kernel: r = {r:.4f}; mean Re(W^-1 V) = {m:.5f} +- {se:.1e}, a(6) = {a_of_t(6.0):.5f}, "
        f"|diff|/SE = {abs(m - a_of_t(6.0)) / se:.2f} ({len(V)} accepted)")
    ok &= abs(m - a_of_t(6.0)) <= 4 * se
    for k in range(1, 4):
        mk, sk = mean_se(Z[:, k])
        ok &= abs(mk) <= 4 * sk
        say(f"A3 kernel: mean vector comp {k}: {mk:+.2e} +- {sk:.1e}")
    say(f"A: {'PASS' if ok else 'FAIL'}")
    return ok


# ------------------------------------------------------------------ literal S4' contours (deduplicated)
# A contour of the coarse link (X, X + e_mu) is P(sig, u) . S_mu(c_X + u) . P(sig, u)[X + e_mu]^-1, where P(sig, u) is the
# axial path from the root c_X to c_X + u in the coordinate order sig, S_mu the straight leg of L steps, and the far path
# from c_{X+e_mu} = c_X + L e_mu is the coarse translate of the near one (literal S4' pairing).
def axial_steps(sig, u):
    z, st = [0] * D, []
    for a in sig:
        for _ in range(abs(u[a])):
            if u[a] > 0:
                st.append((a, tuple(z), False))
                z[a] += 1
            else:
                z[a] -= 1
                st.append((a, tuple(z), True))
    return tuple(st)


PATHS = {}
for _sig in itertools.permutations(range(D)):
    for _u in itertools.product(range(-O, O + 1), repeat=D):
        _k = (axial_steps(_sig, _u), _u)
        PATHS[_k] = PATHS.get(_k, 0) + 1
assert sum(PATHS.values()) == 24 * L ** D
NPATH = len(PATHS)


def gather(F, a, w, Tf, base):
    ix = [(base + w[k]) % Tf for k in range(D)]
    return F[:, a][:, ix[0][:, None, None, None], ix[1][None, :, None, None],
                   ix[2][None, None, :, None], ix[3][None, None, None, :]]


def soft_average(F, Tf):
    """F: (S, D, Tf,Tf,Tf,Tf, 4) unit quaternions. Returns the polar contour means W: (S, D, Tc^4, 4) and |M|."""
    Tc = Tf // L
    S = F.shape[0]
    base = L * np.arange(Tc) + O
    one = np.zeros((S, Tc, Tc, Tc, Tc, 4))
    one[..., 0] = 1.0
    near = {}
    for (steps, u), mult in PATHS.items():
        T = one.copy()
        for (a, w, inv) in steps:
            G = gather(F, a, w, Tf, base)
            T = qmul(T, qconj(G) if inv else G)
        near[(steps, u)] = T
    Wout = np.empty((S, D, Tc, Tc, Tc, Tc, 4))
    Rout = np.empty((S, D, Tc, Tc, Tc, Tc))
    for mu in range(D):
        straight = {}
        for u in itertools.product(range(-O, O + 1), repeat=D):
            T = one.copy()
            z = list(u)
            for _ in range(L):
                T = qmul(T, gather(F, mu, tuple(z), Tf, base))
                z[mu] += 1
            straight[u] = T
        M = np.zeros((S, Tc, Tc, Tc, Tc, 4))
        for (steps, u), mult in PATHS.items():
            Pn = near[(steps, u)]
            Pf = np.roll(Pn, -1, axis=1 + mu)
            M += mult * qmul(qmul(Pn, straight[u]), qconj(Pf))
        M /= 24 * L ** D
        r = np.linalg.norm(M, axis=-1)
        Wout[:, mu] = M / r[..., None]
        Rout[:, mu] = r
    return Wout, Rout


def plaquettes(W):
    """W: (S, D, Tc^4, 4) -> list over (mu<nu) of (S, Tc^4, 4) plaquette holonomies."""
    res = []
    for mu in range(D):
        for nu in range(mu + 1, D):
            a = W[:, mu]
            b = np.roll(W[:, nu], -1, axis=1 + mu)
            c = np.roll(W[:, mu], -1, axis=1 + nu)
            d = W[:, nu]
            res.append(qmul(qmul(qmul(a, b), qconj(c)), qconj(d)))
    return res


def noise_field(rng, t, S, Tf):
    n = S * D * Tf ** D
    return fisher(rng, t, n).reshape((S, D) + (Tf,) * D + (4,))


# ------------------------------------------------------------------ B: one step, compact noise, flat background
def part_b():
    rng = np.random.default_rng(271)
    Tf, S, nb = 9, 100, 20
    R1 = 38.0 / 81.0
    ts = [25.0, 50.0, 100.0, 200.0, 400.0]
    Rs, SEs = [], []
    ok_na3 = True
    t0 = time.time()
    for t in ts:
        per_sample, vec_means, link_vec = [], [], []
        for _ in range(nb):
            F = noise_field(rng, t, S, Tf)
            W, _ = soft_average(F, Tf)
            P = np.stack(plaquettes(W), axis=1)            # (S, 6, Tc^4, 4)
            per_sample.append((1.0 - P[..., 0]).reshape(S, -1).mean(1))
            vec_means.append(P[..., 1:].reshape(S, -1, 3).mean(1))
            link_vec.append(W[:, 0, 0, 0, 0, 0, 1:])
        ps = np.concatenate(per_sample)
        m, se = mean_se(ps)
        Rs.append(t * m)
        SEs.append(t * se)
        vm = np.concatenate(vec_means)
        lv = np.concatenate(link_vec)
        vtxt = []
        for k in range(3):
            mk, sk = mean_se(vm[:, k])
            ok_na3 &= abs(mk) <= 4 * sk
            vtxt.append(f"{mk / sk:+.2f}")
        ltxt = [f"{mean_se(lv[:, k])[0]:+.1e}" for k in range(3)]
        R0 = t * (1.0 - a_of_t(t) ** 4)
        say(f"B t={t:5.0f}: R(t) = {t * m:.5f} +- {t * se:.5f}  (R1 = {R1:.5f}; depth-0 R0 = {R0:.4f}); "
            f"W_P vector-part means / SE = {', '.join(vtxt)}; one block link vector part = {', '.join(ltxt)}")
    tb = time.time() - t0
    x = 1.0 / np.array(ts)
    y = np.array(Rs)
    wgt = 1.0 / np.array(SEs) ** 2
    A = np.stack([np.ones_like(x), x], axis=1)
    cov = np.linalg.inv(A.T @ (wgt[:, None] * A))
    Rinf, b = cov @ (A.T @ (wgt * y))
    seR = np.sqrt(cov[0, 0])
    y0 = np.array([t * (1.0 - a_of_t(t) ** 4) for t in ts])
    b0 = np.polyfit(x, y0, 2)[1]
    say(f"B fit: R_inf = {Rinf:.5f} +- {seR:.5f} (R1 = {R1:.5f}, |diff| = {abs(Rinf - R1):.5f}); b = {b:.3f}; "
        f"depth-0: R0 -> 6, b0 = {b0:.3f}; chi2/dof = {float(((y - A @ np.array([Rinf, b])) ** 2 * wgt).sum()) / 3:.2f}")
    pass_b = abs(Rinf - R1) <= max(3 * seR, 0.015) and abs(Rs[-1] - R1) <= 0.05 * R1
    bias = Rinf > 1.0
    verdict = 'PASS' if pass_b else ('BIAS' if bias else 'INCONCLUSIVE')
    say(f"B: {verdict}; NA-3 sub-check: {'PASS' if ok_na3 else 'FAIL'}; wall {tb:.1f} s")
    return verdict, ok_na3, tb, Rs[2]


# ------------------------------------------------------------------ C: two steps (informational)
def part_c(R100):
    rng = np.random.default_rng(314)
    t, Tf, nsamp = 100.0, 27, 24
    vals1, vals2 = [], []
    t0 = time.time()
    for _ in range(nsamp):
        F = noise_field(rng, t, 1, Tf)
        W1, _ = soft_average(F, Tf)                            # (1, D, 9^4, 4)
        P1 = np.stack(plaquettes(W1), axis=1)
        vals1.append((1.0 - P1[..., 0]).mean())
        W2, _ = soft_average(W1, Tf // L)                      # deterministic second step, no fresh noise
        P2 = np.stack(plaquettes(W2), axis=1)
        vals2.append((1.0 - P2[..., 0]).mean())
    m1, s1 = mean_se(vals1)
    m2, s2 = mean_se(vals2)
    R2pred = 2.0 * (2.0 / 81 + 1.0 / 6561)
    say(f"C t=100, {nsamp} samples on (Z/27)^4: one step t*E = {t * m1:.5f} +- {t * s1:.5f} (38/81 = {38 / 81:.5f}); "
        f"two steps R2 = {t * m2:.5f} +- {t * s2:.5f} (linear response {R2pred:.5f}); R2/R(100) = {t * m2 / R100:.4f} "
        f"(linear 0.1059); wall {time.time() - t0:.1f} s")
    finding = t * m2 > 0.2
    within = abs(t * m2 - R2pred) <= 0.3 * R2pred
    say(f"C: {'FINDING (undamped second step)' if finding else ('as expected' if within else 'outside the 30% band')}")


if __name__ == '__main__':
    tstart = time.time()
    okA = part_a()
    verdict, ok3, tb, R100 = part_b()
    if tb < 300:
        part_c(R100)
    else:
        say(f"C: not run (B wall {tb:.0f} s >= 300 s, as pre-stated)")
    say(f"total wall {time.time() - tstart:.1f} s")
    with open(sys.argv[1] if len(sys.argv) > 1 else 'x5_out.txt', 'w') as fh:
        fh.write('\n'.join(out) + '\n')
