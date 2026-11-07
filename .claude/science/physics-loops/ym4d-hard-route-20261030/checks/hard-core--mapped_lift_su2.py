#!/usr/bin/env python3
"""(LIFT-I) of `library/sector-values.md` in SU(2), with non-commuting parents, at a true constrained minimiser with the comb. Consumer: the hardest inequality of `parts/hard-core--mapped.md` at this stop, on which the uniformity in k of the value clause rests.

Written before running. In the abelian sector the fine gradient energy is exactly C L^(d-6) times the parent's, and the comb has no effect. In SU(2) the contour part of Q^* lambda does not vanish: it leaves a residual at most C L^2 ||F||_L4 |lambda| in l^2, (AD). In d = 2 the count is: the line part has squared norm of order |lambda|^2, and the comb's first stage has L bonds with weight of order one and residual |v| |lambda|, |v| about f, the parent's flux. So the excess in the ratio should be of order L f^2 at most, at f small, and it should not grow with L at a fixed L f^2. This is a first test of that count, in the only dimension I can reach with a full non-abelian solver.

Model. d = 2, SU(2), one level, the comb in axis order, the true gauge-covariant block map, as in `checks/hard-core--mapped_composite_jet_d4.py` with D = 2 but without its linear gauge rotation, torus of N_c = 4 parents. Parent: V'(y, mu) := exp(sum over modes a_m c_m cos(P_m . y + phi_m)), with colours c_m not commuting, scaled so that the largest parent flux is f. Solve min sum_p |log hol_p|^2 over U with block map(U) = V', by SQP with a Gauss-Newton Hessian, which converges at a linear rate of order the flux, and a finite-difference constraint Jacobian.

R(L, f) := L^4 sum_fine |grad F_U|^2 / sum_parent ( |grad' F'|^2 + |F'|^3 ).

PRE-STATED criteria.
 S0. Solver: at the end, constraint residual at most 1e-9, and the gradient of the action orthogonal to the fibre, relative to its norm, at most 1e-5.
 S1. Control, commuting parents: a single colour. R agrees with the abelian formula of `checks/hard-core--mapped_lift_gradient.py` for the same mode within 2 percent at f = 0.02, L = 3, 5.
 S2. Non-commuting parents, seeds of modes (three at L = 3, 5, one at L = 7): at f = 0.02, 0.05, 0.1 and L = 3, 5, 7, R(L, f) <= 1.5 C(2, L, 1), with C(2, L, 1) the abelian supremum (14.8, 21.4, and 23.5 by interpolation at L = 7).
 S3. Excess against the value at small f: for each seed, X(L, f) := R(L, f)/R(L, 0.02) - 1 obeys |X(L, 0.05)| <= 0.05 at each L.
 S4. Reported: X(L, 0.1) and X(L, 0.1)/(L f^2), to read the power. S0 applies at f <= 0.05. At f = 0.1 the Gauss-Newton Hessian omits lambda D^2 M, so convergence is slow, at a rate about 0.6 at L = 3 in a smoke run, and it failed at f = 0.2; a case that does not converge is reported, and not used.
FAIL if S0, S1, S2 or S3 fails.

Limits. d = 2, where the count differs from d = 4; one level; parents with low modes on a torus of 4; a search over three seeds, not a supremum. RSS guard 2 GB.
"""
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
    w = a[..., 0] * b[..., 0] - np.sum(a[..., 1:] * b[..., 1:], axis=-1)
    v = a[..., 0, None] * b[..., 1:] + b[..., 0, None] * a[..., 1:] + np.cross(a[..., 1:], b[..., 1:])
    return np.concatenate([w[..., None], v], axis=-1)


def qinv(a):
    out = a.copy()
    out[..., 1:] *= -1
    return out


def qexp(t):
    n = np.linalg.norm(t, axis=-1, keepdims=True)
    s = np.where(n > 1e-12, np.sin(n) / np.where(n > 1e-12, n, 1.0), 1.0 - n * n / 6)
    return np.concatenate([np.cos(n), s * t], axis=-1)


def qlog(q):
    v = q[..., 1:]
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    ang = np.arctan2(n, q[..., 0, None])
    s = np.where(n > 1e-12, ang / np.where(n > 1e-12, n, 1.0), 1.0)
    return s * v


def adjoint(q):
    """Rotation matrix of q acting on 3-vectors: q v q^-1."""
    w, x, y, z = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    R = np.empty(q.shape[:-1] + (3, 3))
    R[..., 0, 0] = 1 - 2 * (y * y + z * z)
    R[..., 0, 1] = 2 * (x * y - w * z)
    R[..., 0, 2] = 2 * (x * z + w * y)
    R[..., 1, 0] = 2 * (x * y + w * z)
    R[..., 1, 1] = 1 - 2 * (x * x + z * z)
    R[..., 1, 2] = 2 * (y * z - w * x)
    R[..., 2, 0] = 2 * (x * z - w * y)
    R[..., 2, 1] = 2 * (y * z + w * x)
    R[..., 2, 2] = 1 - 2 * (x * x + y * y)
    return R


D = 2


class Level:
    def __init__(self, L, Nc):
        self.L, self.Nc = L, Nc
        self.h = (L - 1) // 2
        self.N = L * Nc
        self.rs = [(a, b) for a in range(-self.h, self.h + 1) for b in range(-self.h, self.h + 1)]
        P = [self.h + L * np.arange(Nc)] * 2
        self.C = np.meshgrid(*P, indexing="ij")

    def contour(self, r):
        steps = []
        for ax in range(D):
            for _ in range(abs(r[ax])):
                steps.append((ax, 1 if r[ax] > 0 else -1))
        return steps

    def block_map(self, V):
        """V: quaternions, shape (2, N, N, 4). Returns parent quaternions, shape (2, Nc, Nc, 4)."""
        N, L, Nc = self.N, self.L, self.Nc
        C = self.C

        def at(arr, ax, x):
            return arr[ax][x[0] % N, x[1] % N]

        Gamma = {}
        for r in self.rs:
            x = [C[0].copy(), C[1].copy()]
            q = np.zeros((Nc, Nc, 4))
            q[..., 0] = 1
            for ax, sg in self.contour(r):
                if sg > 0:
                    q = qmul(q, at(V, ax, x))
                    x[ax] = x[ax] + 1
                else:
                    x[ax] = x[ax] - 1
                    q = qmul(q, qinv(at(V, ax, x)))
            Gamma[r] = q
        out = np.zeros((2, Nc, Nc, 4))
        for mu in range(2):
            Om = {}
            for r in self.rs:
                x = [C[0] + r[0], C[1] + r[1]]
                q = Gamma[r]
                for _ in range(L):
                    q = qmul(q, at(V, mu, x))
                    x[mu] = x[mu] + 1
                Om[r] = qmul(q, qinv(np.roll(Gamma[r], -1, axis=mu)))
            Oc = Om[(0, 0)]
            tavg = np.zeros((Nc, Nc, 3))
            for r in self.rs:
                tavg += qlog(qmul(Om[r], qinv(Oc)))
            tavg /= len(self.rs)
            out[mu] = qmul(qexp(tavg), Oc)
        return out


def plaq_torus(V):
    """Plaquette quaternions at each site; V shape (2, n, n, 4)."""
    a = V[0]
    b = np.roll(V[1], -1, axis=0)
    c = qinv(np.roll(V[0], -1, axis=1))
    d = qinv(V[1])
    return qmul(qmul(qmul(a, b), c), d)


def grad_energy(V):
    """sum over sites and two directions of |transported F(x + e) - F(x)|^2, sum |F|^3, sum |F|^2, with F := log of the plaquette."""
    F = qlog(plaq_torus(V))
    tot = 0.0
    for e in range(2):
        Fn = np.roll(F, -1, axis=e)
        R = adjoint(V[e])
        diff = np.einsum("...ij,...j->...i", R, Fn) - F
        tot += float(np.sum(diff**2))
    nF = np.linalg.norm(F, axis=-1)
    return tot, float(np.sum(nF**3)), float(np.sum(nF**2)), float(nF.max())


def gn_system(V):
    """Residual r := log hol_p, Jacobian J in left-multiplied bond variables, first order. Returns r (flat), J (sparse-like dense)."""
    N = V.shape[1]
    nb = 2 * N * N
    r = np.zeros((N * N, 3))
    J = np.zeros((3 * N * N, 3 * nb))
    idx = lambda ax, x, y: ax * N * N + (x % N) * N + (y % N)
    for x in range(N):
        for y in range(N):
            k = x * N + y
            a = V[0, x, y]
            b = V[1, (x + 1) % N, y]
            c = V[0, x, (y + 1) % N]
            d = V[1, x, y]
            hol = qmul(qmul(qmul(a, b), qinv(c)), qinv(d))
            r[k] = qlog(hol)
            # Left multiply each bond by exp(delta): the first-order change of the holonomy, on the left, is Ad(prefix) delta with a sign.
            pre_a = np.array([1.0, 0, 0, 0])
            pre_b = a
            pre_c = qmul(qmul(a, b), qinv(c))
            pre_d = hol
            for (ax, i, j), pre, s in (
                ((0, x, y), pre_a, 1.0),
                ((1, x + 1, y), pre_b, 1.0),
                ((0, x, y + 1), pre_c, -1.0),
                ((1, x, y), pre_d, -1.0),
            ):
                b_idx = idx(ax, i, j)
                J[3 * k : 3 * k + 3, 3 * b_idx : 3 * b_idx + 3] += s * adjoint(pre)
    return r.ravel(), J


def apply_delta(V, delta):
    N = V.shape[1]
    d = delta.reshape(2, N, N, 3)
    return qmul(qexp(d), V)


def constraint(level, V, Vp):
    """Residual: log( block_map(V) Vp^-1 ), flat."""
    return qlog(qmul(level.block_map(V), qinv(Vp))).ravel()


def constraint_jacobian(level, V, Vp, eps=1e-7):
    """Finite differences with a colouring: blocks two apart in each axis touch disjoint parents, so one evaluation serves four bonds. Needs Nc = 4."""
    L, Nc, N = level.L, level.Nc, level.N
    assert Nc == 4
    base = constraint(level, V, Vp)
    n = 2 * N * N * 3
    Q = np.zeros((base.size, n))
    prow = lambda mu, p, q: 3 * (mu * Nc * Nc + (p % Nc) * Nc + (q % Nc))
    for ax in range(2):
        for ox in range(L):
            for oy in range(L):
                for col in range(3):
                    for ca in range(2):
                        for cb in range(2):
                            d = np.zeros((2, N, N, 3))
                            blocks = [(ca + 2 * i, cb + 2 * j) for i in range(2) for j in range(2)]
                            for a_, b_ in blocks:
                                d[ax, L * a_ + ox, L * b_ + oy, col] = eps
                            diff = (constraint(level, apply_delta(V, d.ravel()), Vp) - base) / eps
                            for a_, b_ in blocks:
                                c = 3 * (ax * N * N + (L * a_ + ox) * N + (L * b_ + oy)) + col
                                rows = [prow(m, a_, b_) for m in range(2)] + [prow(0, a_ - 1, b_), prow(1, a_, b_ - 1)]
                                for r_ in rows:
                                    Q[r_ : r_ + 3, c] = diff[r_ : r_ + 3]
    return Q, base


def solve(level, Vp, V0, verbose=False):
    """SQP on the KKT system through a Schur complement. Inner gauge directions are null in the Hessian and in the constraint, and a small regulator keeps the step off them."""
    import scipy.linalg as sla

    V = V0.copy()
    info = {}
    Q = None
    prev = None
    for it in range(30):
        Q, c = constraint_jacobian(level, V, Vp)
        r, J = gn_system(V)
        g = J.T @ r
        n = g.size
        H = J.T @ J + 1e-3 * np.eye(n)
        cf = sla.cho_factor(H, check_finite=False)
        HiQ = sla.cho_solve(cf, Q.T, check_finite=False)
        Hig = sla.cho_solve(cf, g, check_finite=False)
        S = Q @ HiQ
        # The constraints are independent: parents' gauge is fixed by the block map.
        mu = np.linalg.lstsq(S, c - Q @ Hig, rcond=1e-12)[0]
        delta = -Hig - HiQ @ mu
        step = float(np.max(np.abs(delta)))
        alpha = min(1.0, 0.3 / max(step, 1e-30))
        V = apply_delta(V, alpha * delta)
        if verbose:
            print(f"   it={it} |r|^2={float(r @ r):.6e} cres={float(np.max(np.abs(c))):.2e} step={step:.2e}", flush=True)
        guard()
        val = float(r @ r)
        if step < 1e-6 or (prev is not None and abs(val - prev) <= 1e-11 * max(val, 1e-30) and float(np.max(np.abs(c))) <= 1e-10):
            break
        prev = val
    Q, c = constraint_jacobian(level, V, Vp)
    r, J = gn_system(V)
    g = J.T @ r
    lam = np.linalg.lstsq(Q.T, g, rcond=1e-10)[0]
    pg = g - Q.T @ lam
    info["cres"] = float(np.max(np.abs(c)))
    info["pgrad"] = float(np.linalg.norm(pg) / max(np.linalg.norm(g), 1e-30))
    info["iters"] = it + 1
    return V, info


def make_parent(Nc, modes, f):
    """modes: list of (Px, Py, colours for each direction, phase)."""
    A = np.zeros((2, Nc, Nc, 3))
    xs, ys = np.meshgrid(np.arange(Nc), np.arange(Nc), indexing="ij")
    for Px, Py, cols, ph in modes:
        P = np.array([2 * np.pi * Px / Nc, 2 * np.pi * Py / Nc])
        for mu in range(2):
            mid = (xs + 0.5 * (mu == 0), ys + 0.5 * (mu == 1))
            A[mu] += np.cos(P[0] * mid[0] + P[1] * mid[1] + ph)[..., None] * cols[mu]
    V = qexp(A)
    # Scale to the requested largest flux, by bisection on a scale of A.
    lo, hi = 0.0, 1.0
    while grad_energy(qexp(hi * A))[3] < f and hi < 64:
        hi *= 2
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if grad_energy(qexp(mid * A))[3] < f:
            lo = mid
        else:
            hi = mid
    return qexp(0.5 * (lo + hi) * A), 0.5 * (lo + hi) * A


def initial_lift(level, A):
    """Spread parent angles along bonds, one L-th each, on the tube."""
    L, Nc, N = level.L, level.Nc, level.N
    t = np.zeros((2, N, N, 3))
    for mu in range(2):
        t[mu] = np.kron(A[mu], np.ones((L, L, 1))) / L
    return qexp(t)


def ratio(level, Vp, V):
    fine, cub, en, fmax = grad_energy(V)
    pg, pc, pe, pm = grad_energy(Vp)
    return level.L**4 * fine / (pg + pc), dict(fine=fine, pg=pg, pc=pc, en=en, pe=pe, fmax=fmax, pm=pm)


def abelian_value(L, Px, Py, Nc):
    """The abelian ratio L^4 sum |grad F|^2 / sum |grad' F'|^2 for one mode."""
    import importlib.util
    import os

    spec = importlib.util.spec_from_file_location("lg", os.path.join(os.path.dirname(os.path.abspath(__file__)), "hard-core--mapped_lift_gradient.py"))
    lg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lg)
    P = (2 * np.pi * Px / Nc, 2 * np.pi * Py / Nc)
    return L**4 * lg.mode(P, L, 1, 2)[0]


def main():
    ok = True
    Nc = 4
    print("S1: commuting parents", flush=True)
    e = np.eye(3)
    perp = lambda Px, Py: (e[0] * (-np.sin(np.pi * Py / Nc)), e[0] * np.sin(np.pi * Px / Nc))
    for L in (3, 5):
        level = Level(L, Nc)
        Px, Py = 1, 0
        cols = perp(Px, Py)
        Vp, A = make_parent(Nc, [(Px, Py, cols, 0.3)], 0.02)
        V, info = solve(level, Vp, initial_lift(level, A))
        R, d = ratio(level, Vp, V)
        ab = abelian_value(L, Px, Py, Nc)
        good = abs(R / ab - 1) <= 0.02 and info["cres"] <= 1e-9 and info["pgrad"] <= 1e-5
        ok = ok and good
        print(f" L={L}: R={R:.4f}, abelian {ab:.4f}: cres={info['cres']:.1e} pgrad={info['pgrad']:.1e} iters={info['iters']}: {good} rss={rss_gb():.2f}GB", flush=True)
    print("S2, S3, S4: non-commuting parents", flush=True)
    Cab = {3: 14.8, 5: 21.4, 7: 23.5}
    fs = (0.02, 0.05, 0.1)
    for L in (3, 5, 7):
        level = Level(L, Nc)
        for seed in range(3 if L < 7 else 1):
            rng = np.random.default_rng(100 + seed)
            modes = []
            for _ in range(3):
                Px, Py = rng.integers(0, Nc, 2)
                if Px == 0 and Py == 0:
                    Px = 1
                cols = [rng.standard_normal(3) for _ in range(2)]
                modes.append((int(Px), int(Py), cols, float(rng.uniform(0, 2 * np.pi))))
            Rs = {}
            for f in fs:
                Vp, A = make_parent(Nc, modes, f)
                V, info = solve(level, Vp, initial_lift(level, A))
                R, d = ratio(level, Vp, V)
                Rs[f] = R
                good0 = info["cres"] <= 1e-9 and info["pgrad"] <= 1e-5
                conv = info["cres"] <= 1e-7 and info["pgrad"] <= 1e-3
                if f <= 0.05:
                    ok = ok and good0
                good2 = R <= 1.5 * Cab[L] or not conv
                ok = ok and good2
                Rs[f] = R if conv else float("nan")
                print(f"  L={L} seed={seed} f={f}: R={R:.4f}, fine flux max {d['fmax']:.5f} (f/L^2 = {f / L**2:.5f}), cubic share {d['pc'] / (d['pg'] + d['pc']):.3f}, cres={info['cres']:.1e} pgrad={info['pgrad']:.1e} iters={info['iters']}: S0 {good0}, converged {conv}, S2 {good2} rss={rss_gb():.2f}GB", flush=True)
            X05 = Rs[0.05] / Rs[0.02] - 1
            X1 = Rs[0.1] / Rs[0.02] - 1
            good3 = abs(X05) <= 0.05
            ok = ok and good3
            print(f" L={L} seed={seed}: X(0.05)={X05:+.4f}: {good3}; X(0.1)={X1:+.4f}, X(0.1)/(L f^2)={X1 / (L * 0.01):+.4f}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
