"""bb8w: Theorem N1-loc (BFT_B §24.2), interior C^{1,alpha} of the nonlinear box normal form, d = 2, SU(2) (lane B session 8).

Criteria: checks/bb8w_criteria.md (written before this script). Quaternions as in bb6n (exp(v) = (cos|v|, sin|v| v/|v|)).
Box sites z in {0..S-1}^2, S = 4n + 1, centre c = (2n, 2n); link (z, a): z -> z + e_a, valid iff z_a <= S - 2.
"""
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

T0 = time.time()
EPS = 0.2
ALPHA = 0.25


def qmul(p, q):
    w1, x1, y1, z1 = np.moveaxis(p, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(q, -1, 0)
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=-1)


def qinv(q):
    return q * np.array([1.0, -1.0, -1.0, -1.0])


def qexp(v):
    th = np.linalg.norm(v, axis=-1, keepdims=True)
    sinc = np.where(th > 1e-15, np.sin(th) / np.where(th > 1e-15, th, 1.0), 1.0)
    return np.concatenate([np.cos(th), sinc * v], axis=-1)


def qlog(q):
    vn = np.linalg.norm(q[..., 1:], axis=-1, keepdims=True)
    th = np.arctan2(vn, q[..., :1])
    fac = np.where(vn > 1e-15, th / np.where(vn > 1e-15, vn, 1.0), 1.0)
    return fac * q[..., 1:]


def profile(x0, x1):
    a0 = np.stack([np.sin(x1 + 0.2), 0.5 * np.cos(x0 + 0.3), 0.3 * np.sin(x0 * x1)], axis=-1)
    a1 = np.stack([0.4 * np.cos(0.7 * x0), np.sin(x0 - 0.5 * x1), 0.6 * np.cos(x1)], axis=-1)
    return EPS * a0, EPS * a1


def setup(n):
    S = 4 * n + 1
    HW = 2 * n
    z0, z1 = np.meshgrid(np.arange(S), np.arange(S), indexing="ij")
    U = np.zeros((S, S, 2, 4))
    a0, _ = profile((z0 + 0.5 - HW) / n, (z1 - HW) / n)
    _, a1 = profile((z0 - HW) / n, (z1 + 0.5 - HW) / n)
    U[:, :, 0] = qexp(a0 / n)
    U[:, :, 1] = qexp(a1 / n)
    valid = np.ones((S, S, 2), bool)
    valid[S - 1, :, 0] = False
    valid[:, S - 1, 1] = False
    U[~valid] = np.array([1.0, 0, 0, 0])
    return S, HW, U, valid


def wfield(U, g, valid):
    w = np.zeros(U.shape[:3] + (3,))
    for a in range(2):
        gy = np.roll(g, -1, axis=a)
        w[:, :, a] = qlog(qmul(qmul(g, U[:, :, a]), qinv(gy)))
    w[~valid] = 0.0
    return w


def dstar(w):
    return sum(np.roll(w[:, :, a], 1, axis=a) - w[:, :, a] for a in range(2))


def laplacian(S, valid, cidx):
    N = S * S
    idx = np.arange(N).reshape(S, S)
    rows, cols, vals = [], [], []
    e = 0
    for a in range(2):
        tail = idx[valid[:, :, a]]
        head = np.roll(idx, -1, axis=a)[valid[:, :, a]]
        m = len(tail)
        rows += [np.arange(e, e + m)] * 2
        cols += [head, tail]
        vals += [np.ones(m), -np.ones(m)]
        e += m
    Dm = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(e, N))
    Lp = (Dm.T @ Dm).tocsc()
    keep = np.setdiff1d(np.arange(N), [cidx])
    return spl.splu(Lp[keep][:, keep]), keep, N


def solve_pinned(lu, keep, N, rhs):
    out = np.zeros(N)
    out[keep] = lu.solve(rhs.reshape(-1)[keep])
    return out


def normal_form(U, valid, S, HW):
    cidx = HW * S + HW
    lu, keep, N = laplacian(S, valid, cidx)
    g = np.zeros((S, S, 4))
    g[..., 0] = 1.0
    for it in range(60):
        w = wfield(U, g, valid)
        dw = dstar(w)
        err = np.abs(dw).max()
        if err < 1e-12:
            break
        xi = np.stack([solve_pinned(lu, keep, N, dw[..., c]).reshape(S, S) for c in range(3)], axis=-1)
        g = qmul(qexp(xi), g)
    return g, w, err, it, lu, keep, N


def grads(wc, valid, n, region):
    """coarse gradients n*(w^c(z + e_b, a) - w^c(z, a)) for links (z, a), (z + e_b, a) valid and in region."""
    G = {}
    for a in range(2):
        for b in range(2):
            ok = valid[:, :, a] & np.roll(valid[:, :, a], -1, axis=b) & region[:, :, a] & np.roll(region[:, :, a], -1, axis=b)
            ok[(slice(None), slice(None))] &= True
            if b == 0:
                ok[-1, :] = False
            else:
                ok[:, -1] = False
            G[(a, b)] = (n * (np.roll(wc[:, :, a], -1, axis=b) - wc[:, :, a]), ok)
    return G


def measures(w, valid, n, S, HW, halfw):
    z0, z1 = np.meshgrid(np.arange(S), np.arange(S), indexing="ij")
    reg = np.zeros((S, S, 2), bool)
    for a in range(2):
        e = (1, 0) if a == 0 else (0, 1)
        inside = (np.maximum(np.abs(z0 - HW), np.abs(z1 - HW)) <= halfw) & \
                 (np.maximum(np.abs(z0 + e[0] - HW), np.abs(z1 + e[1] - HW)) <= halfw)
        reg[:, :, a] = inside & valid[:, :, a]
    wc = n * w
    A1 = np.linalg.norm(wc, axis=-1)[reg].max()
    G = grads(wc, valid, n, reg)
    A2 = max(np.linalg.norm(gv, axis=-1)[ok].max() for gv, ok in G.values())
    A3 = 0.0
    for (a, b), (gv, ok) in G.items():
        for c in range(2):
            d = 1
            while d <= n:
                sl_hi = [slice(None)] * 2
                sh_ok = np.roll(ok, -d, axis=c)
                if c == 0:
                    sh_ok[S - d:, :] = False
                else:
                    sh_ok[:, S - d:] = False
                both = ok & sh_ok
                if both.any():
                    diff = np.linalg.norm(np.roll(gv, -d, axis=c) - gv, axis=-1)[both].max()
                    A3 = max(A3, diff / (d / n) ** ALPHA)
                d *= 2
    return A1, A2, A3


def curv_info(U, n, S):
    pl = qmul(qmul(U[:, :, 0], np.roll(U[:, :, 1], -1, axis=0)), qmul(qinv(np.roll(U[:, :, 0], -1, axis=1)), qinv(U[:, :, 1])))
    F = qlog(pl)[: S - 1, : S - 1] * n * n
    f0 = np.linalg.norm(F, axis=-1).max()
    # Lipschitz proxy: neighbouring plaquettes, Ad by the shared link (covariant difference)
    lip = 0.0
    for a in range(2):
        e = (1, 0) if a == 0 else (0, 1)
        t = U[: S - 1, : S - 1, a]
        Fp = np.roll(qlog(pl), (-e[0], -e[1]), axis=(0, 1))[: S - 1, : S - 1] * n * n
        pv = np.concatenate([np.zeros(Fp.shape[:-1] + (1,)), Fp], axis=-1)
        AdF = qmul(qmul(t, pv), qinv(t))[..., 1:]
        dd = np.linalg.norm(F - AdF, axis=-1)
        if a == 0:
            dd = dd[: S - 2, :]
        else:
            dd = dd[:, : S - 2]
        lip = max(lip, dd.max() * n)
    return f0, lip


out = []
rows = {}
W0ok = True
for n in (3, 9, 27):
    S, HW, U, valid = setup(n)
    g, w, err, it, lu, keep, N = normal_form(U, valid, S, HW)
    W0ok &= err < 1e-12 and it < 60 and abs(g[HW, HW, 0] - 1) < 1e-14
    inner = measures(w, valid, n, S, HW, 1.5 * n)
    full = measures(w, valid, n, S, HW, 2 * n)
    f0, lip = curv_info(U, n, S)
    A = np.zeros((S, S, 2, 3))
    for a in range(2):
        A[:, :, a] = qlog(U[:, :, a])
    A[~valid] = 0.0
    lam = np.stack([solve_pinned(lu, keep, N, -dstar(A)[..., c]).reshape(S, S) for c in range(3)], axis=-1)
    alin = A.copy()
    for a in range(2):
        alin[:, :, a] += np.roll(lam, -1, axis=a) - lam
    alin[~valid] = 0.0
    nl = np.abs(w - alin).max() / np.abs(w).max()
    rows[n] = (inner, full, f0, lip, nl, err, it)
    out.append(f"n = {n} (S = {S}): Coulomb iterations {it}, max|d*w| = {err:.1e}; N': A1 = {inner[0]:.5f}, A2 = {inner[1]:.5f}, "
               f"A3 = {inner[2]:.5f}; full box: {full[0]:.5f}, {full[1]:.5f}, {full[2]:.5f}; f_0 = {f0:.5f}, Lip proxy = {lip:.5f}; "
               f"(A1+A2+A3)/(f_0+Lip) = {sum(inner) / (f0 + lip):.4f}; |w - a_lin|/|w| = {nl:.2e}")
W1ok = all(rows[27][0][i] <= 1.25 * max(rows[3][0][i], rows[9][0][i]) for i in range(3))
out.append(f"W0 convergence and pinning: {'PASS' if W0ok else 'FAIL'}")
out.append(f"W1 interior C^(1,alpha) flat in n (N1L-F1): {'PASS' if W1ok else 'FAIL'}")
out.append(f"VERDICT: {'ALL PASS' if (W0ok and W1ok) else 'NOT ALL PASS'} (W0, W1)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
