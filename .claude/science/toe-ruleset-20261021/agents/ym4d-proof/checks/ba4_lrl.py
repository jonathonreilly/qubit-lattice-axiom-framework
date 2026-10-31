"""ba4: BFT lane A, session 4 (criteria: checks/ba4_criteria.md, written before this file).

Usage: python3 ba4_lrl.py D3 | D1a | D1b | D2
D1a: LRL (a) ratio Q_a for F = d x_l of the source-free response to the unit datum at (X, mu) = (0, 0), k = 1, T = 2..5.
D1b: the same at (k, T) = (2, 2), l = 0, 1 (informational).
D2:  Theorem XR ratio Q_XR = max|r_0| / (L^2 sup|w|) (k = 1, l = 0) on rough w (C_0 minus Q_0^T C_1):
     XR-designed w = P_R sign(P_R B'_0), RP-designed w = P_R sign(P_R K) (rev3_probe P3), random w; with the (RP) ratio
     Q_RP = sup|g|/sup|w|, g = d Delta^-1 w, and the sanity identities S2 (duality) and S3 (flux coarse-graining).
D3:  LRL (a) ratio for synthetic exact F = dA' on the level-l torus (side M = T R), FFT, R = lattice steps per coarse unit.
     Periodic smooth coordinates: g_T(u) = (T/2pi)^2 2(1 - cos(2pi u/T)) (~ u^2), s_T(u) = (T/2pi) sin(2pi u/T) (~ u),
     rho = sqrt(sum s_T(u_mu)^2), env = exp(-sum g_T(u_mu)/(2 w^2)), w = 1/2 (u = coarse coordinate of the base point).
     S-bump: A'_0 = env.  S-cusp: A'_0 = env rho^{1+alpha} s_1 s_2 / rho^2 (F Hoelder-alpha at rho = 0).
     S-jump: A'_0 = env rho s_1 s_2 / rho^2 (F of degree 0, discontinuous).  S-noise: A'_mu = env * N(0,1) (seeded).
Numerator / denominator of Q_a as in the criteria file; all lattice units (the coarse factors R^2 cancel in Q_a).
"""
import itertools
import resource
import sys
import time

import numpy as np
from scipy.sparse.linalg import cg

import ba2_lin as b2

c26 = b2.c26
L = c26.L
ALPHA = 0.25
MPS = (0.25, 0.5)
PLANES = list(itertools.combinations(range(4), 2))
T0 = time.time()


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


def mx(a):
    return float(np.max(np.abs(a)))


# ------------------------------------------------------------------ FFT forms on (Z/M)^4
def fwd(f, mu):
    return np.roll(f, -1, axis=mu) - f


def nus(M):
    p = 2 * np.pi * np.fft.fftfreq(M)
    out = []
    for mu in range(4):
        sh = [1, 1, 1, 1]; sh[mu] = M
        out.append((np.exp(1j * p) - 1).reshape(sh))
    return out


def coulomb(Ap, keep_mean=False):
    """Pi_cc of a 1-form (list of 4 arrays): A - d Delta^-1 d* A; the mean is dropped unless keep_mean."""
    M = Ap[0].shape[0]; nu = nus(M)
    hat = [np.fft.fftn(a) for a in Ap]
    psi = sum(np.abs(n) ** 2 for n in nu); psi = np.broadcast_to(psi, (M,) * 4).copy()
    div = sum(np.conj(nu[m]) * hat[m] for m in range(4))
    psi0 = psi.copy(); psi0[0, 0, 0, 0] = 1.0
    out = []
    for m in range(4):
        h = hat[m] - nu[m] * div / psi0
        if not keep_mean:
            h[0, 0, 0, 0] = 0.0
        out.append(np.real(np.fft.ifftn(h)))
    return out


def dform(A):
    return [fwd(A[n], m) - fwd(A[m], n) for (m, n) in PLANES]


def dstar1(A):
    return sum(np.roll(A[m], 1, axis=m) - A[m] for m in range(4))


def grads(A):
    return [fwd(A[m], n) for m in range(4) for n in range(4)]


# ------------------------------------------------------------------ Campanato machinery
def slide(H, s, ax):
    M = H.shape[ax]
    Hp = np.concatenate([H, np.take(H, np.arange(s - 1), axis=ax)], axis=ax) if s > 1 else H
    C = np.cumsum(Hp, axis=ax)
    z = np.zeros_like(np.take(C, [0], axis=ax))
    C = np.concatenate([z, C], axis=ax)
    return np.take(C, np.arange(s, s + M), axis=ax) - np.take(C, np.arange(0, M), axis=ax)


def boxmean(H, s):
    S = H
    for ax in range(4):
        S = slide(S, s, ax)
    return S / s ** 4


def dist1(M, R):
    y = np.arange(M)
    return np.minimum(y, M - y) / R


def dmax_boxes(M, R, s):
    d1 = dist1(M, R)
    dm = np.array([max(d1[(c + t) % M] for t in range(s)) for c in range(M)])
    return dm[:, None, None, None] + dm[None, :, None, None] + dm[None, None, :, None] + dm[None, None, None, :]


def dpoint(M, R):
    d1 = dist1(M, R)
    return d1[:, None, None, None] + d1[None, :, None, None] + d1[None, None, :, None] + d1[None, None, None, :]


def campanato_sup(Hs, R, wfun):
    """max over components, box sides 2..R, corners of wfun(d_max(B)) * rho^-alpha * Osc_2(H; B)."""
    M = Hs[0].shape[0]; best = 0.0
    for s in range(2, min(R, M) + 1):
        W = wfun(dmax_boxes(M, R, s)) * (s / R) ** (-ALPHA)
        for H in Hs:
            m1 = boxmean(H, s); m2 = boxmean(H * H, s)
            osc = np.sqrt(np.maximum(m2 - m1 * m1, 0.0))
            best = max(best, float(np.max(W * osc)))
    return best


def Q_a(F, A, R, mp):
    M = F[0].shape[0]; dp = dpoint(M, R)
    G = grads(A)
    num = max(float(np.max((1 + dp) ** 5 * np.abs(g))) for g in G) + campanato_sup(G, R, lambda d: (1 + d) ** 5)
    den = max(float(np.max(np.exp(mp * dp) * np.abs(f))) for f in F) + campanato_sup(F, R, lambda d: np.exp(mp * d))
    return num / den


def sanity_S1(F, A):
    dA = dform(A)
    e1 = max(mx(dA[i] - F[i]) for i in range(6)) / max(mx(f) for f in F)
    e2 = mx(dstar1(A)) / max(mx(a) for a in A)
    return e1, e2


# ------------------------------------------------------------------ D3 synthetic
def synthetic(kind, M, R, rng):
    T = M / R
    u = (np.arange(M) - M * (np.arange(M) > M // 2)) / R  # minimum-image coarse coordinate (not used directly)
    ang = 2 * np.pi * np.arange(M) / M
    g1 = (T / (2 * np.pi)) ** 2 * 2 * (1 - np.cos(ang)); s1 = (T / (2 * np.pi)) * np.sin(ang)
    sh = lambda a, mu: a.reshape([M if i == mu else 1 for i in range(4)])
    gs = sum(sh(g1, mu) for mu in range(4)); env = np.exp(-gs / (2 * 0.25))
    rho2 = sum(sh(s1, mu) ** 2 for mu in range(4)); rho = np.sqrt(rho2); r0 = np.where(rho2 > 0, rho2, 1.0)
    ang12 = sh(s1, 1) * sh(s1, 2) / r0
    z = np.zeros((M,) * 4)
    if kind == "S-bump":
        Ap = [env * np.ones((M,) * 4), z, z, z]
    elif kind == "S-cusp":
        Ap = [env * rho ** (1 + ALPHA) * ang12, z, z, z]
    elif kind == "S-jump":
        Ap = [env * rho * ang12, z, z, z]
    else:
        Ap = [env * rng.normal(size=(M,) * 4) for _ in range(4)]
    del u
    return Ap


def part_D3():
    rng = np.random.default_rng(20261028 + 44)
    grid = [(3, 2), (3, 4), (3, 8), (3, 1), (9, 1), (27, 1), (9, 2)]
    res = {}
    for kind in ("S-bump", "S-cusp", "S-jump", "S-noise"):
        for (R, T) in grid:
            tt = time.time(); M = R * T
            Ap = synthetic(kind, M, R, rng)
            F = dform(Ap); A = coulomb(Ap)
            e1, e2 = sanity_S1(F, A)
            qs = [Q_a(F, A, R, mp) for mp in MPS]
            res[(kind, R, T)] = qs
            print(f"D3 {kind} R={R} T={T} M={M}: Q_a(m'=0.25) {qs[0]:.4f}, Q_a(m'=0.5) {qs[1]:.4f}; "
                  f"S1 |dA-F| {e1:.1e}, |d*A| {e2:.1e} ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
    return res


# ------------------------------------------------------------------ chain helpers
def arr1(v, M):
    N = M ** 4
    return [v[m * N:(m + 1) * N].reshape((M,) * 4) for m in range(4)]


def vec1(A):
    return np.concatenate([a.reshape(-1) for a in A])


def data_response(ch):
    Bk = np.zeros(ch.levels[ch.k].NL); Bk[0] = 1.0
    x, res, it = ch.cg(Bk, np.zeros(ch.M.shape[1]))
    return ch.split(x), res, Bk


def part_D1(cases):
    out = {}
    for (k, T) in cases:
        tt = time.time()
        ch = b2.SChain(4, T, k, (1.0,) * k)
        xs, res, Bk = data_response(ch)
        for l in range(k):
            M = ch.levels[l].n; R = L ** (k - l)
            X = arr1(xs[l], M); F = dform(X); A = coulomb(X)
            e1, e2 = sanity_S1(F, A)
            qs = [Q_a(F, A, R, mp) for mp in MPS]
            out[(k, T, l)] = qs
            print(f"D1 k={k} T={T} l={l} (R={R}, M={M}): Q_a(m'=0.25) {qs[0]:.4f}, Q_a(m'=0.5) {qs[1]:.4f}; "
                  f"S1 {e1:.1e}, {e2:.1e}; CG res {res:.1e} ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
        del ch
    return out


# ------------------------------------------------------------------ D2 rough currents
def flux_cg(A, T):
    """F^(0->1) A as a coarse link vector: total flux through the face between blocks Y and Y + e_nu."""
    out = []
    for nu in range(4):
        a = A[nu].reshape(T, L, T, L, T, L, T, L)
        idx = [slice(None)] * 8; idx[2 * nu + 1] = L - 1
        a = a[tuple(idx)]
        pos = 0; sum_axes = []
        for j in range(4):
            if j == nu:
                pos += 1
            else:
                sum_axes.append(pos + 1); pos += 2
        out.append(a.sum(axis=tuple(sum_axes)).reshape(-1))
    return np.concatenate(out)


def part_D2(Ts):
    rng = np.random.default_rng(20261028 + 45)
    out = {}
    for T in Ts:
        tt = time.time()
        ch = b2.SChain(4, T, 1, (1.0,)); lf, lc = ch.levels; M = lf.n; Q = ch.Q[0]
        Df = lf.dmat(); Gf = b2.gradmat(lf); GtG = (Gf.T @ Gf).tocsr()
        Gc = b2.gradmat(lc).toarray()
        Pic = np.eye(lc.NL) - Gc @ np.linalg.pinv(Gc.T @ Gc) @ Gc.T          # coarse Pi_cc (dense)
        QQt = (Q @ Q.T).toarray()
        Gram = Pic @ QQt @ Pic; Gp = np.linalg.pinv(Gram, rcond=1e-11, hermitian=True)
        del QQt, Gram

        def P_C(v):
            return vec1(coulomb(arr1(v, M), keep_mean=True))

        def P_S(v):
            return Q.T @ (Pic @ (Gp @ (Pic @ (Q @ v))))

        def P_R(v):
            v = P_C(v)
            return v - P_S(v)

        Bk = np.zeros(lc.NL); Bk[0] = 1.0
        xB, resB, _ = ch.cg(Bk, np.zeros(ch.M.shape[1])); B0 = ch.split(xB)[0]
        # RP design (rev3_probe P3): y = Delta^-1 d* p0, K = P_R(y)
        p0 = np.zeros(Df.shape[0]); p0[0] = 1.0
        dsp = Df.T @ p0
        yv = np.zeros_like(dsp)
        nu_ = nus(M); psi = np.broadcast_to(sum(np.abs(n) ** 2 for n in nu_), (M,) * 4).copy(); psi[0, 0, 0, 0] = np.inf
        for m, a in enumerate(arr1(dsp, M)):
            yv[m * M ** 4:(m + 1) * M ** 4] = np.real(np.fft.ifftn(np.fft.fftn(a) / psi)).reshape(-1)
        fams = {"XR-designed": P_R(np.sign(P_R(B0))), "RP-designed": P_R(np.sign(P_R(yv))),
                "random": P_R(rng.normal(size=lf.NL))}
        row = {}
        for name, w in fams.items():
            g = ch.grad_src(j=[w])
            x, res, it = ch.cg(np.zeros(lc.NL), g)
            r0 = Q @ ch.split(x)[0]
            qxr = mx(r0) / (L ** 2 * mx(w))
            gw = np.zeros_like(w)
            for m, a in enumerate(arr1(w, M)):
                gw[m * M ** 4:(m + 1) * M ** 4] = np.real(np.fft.ifftn(np.fft.fftn(a) / psi)).reshape(-1)
            g_rp = Df @ gw
            qrp = mx(g_rp) / mx(w)
            dual = float(w @ B0)
            s2 = abs(r0[0] - dual) / abs(dual)
            s2ok = abs(r0[0] - dual) <= 1e-8 * abs(dual) + 1e-12 * mx(w)
            row[name] = (qxr, qrp)
            print(f"D2 T={T} {name}: Q_XR {qxr:.4f}, Q_RP {qrp:.4f}; r_0(0,0) {r0[0]:.4e} vs <w,B'_0> {dual:.4e} "
                  f"(S2 rel {s2:.1e} {'ok' if s2ok else 'FAIL'}); |d*w|/|w| {mx(Gf.T @ w) / mx(w):.1e}; "
                  f"CG res {res:.1e}", flush=True)
            out.setdefault((name, "S2"), []).append(bool(s2ok))
        # S3 and FC (ii) on A = Pi_cc B'_0
        Aarr = coulomb(arr1(B0, M), keep_mean=True)
        z = flux_cg(Aarr, T)
        QTz = Q.T @ z
        dsz = mx(Gc.T @ z) / mx(z)
        w = fams["XR-designed"]
        s3 = abs(float(w @ QTz)) / (mx(w) * float(np.sum(np.abs(QTz))))
        Av = vec1(Aarr)
        gradA = max(mx(gg) for gg in grads(Aarr))
        fc2 = mx(Av - QTz) / (L * gradA)
        e_dual = abs(float(w @ (Av - QTz)) - float(w @ B0)) / abs(float(w @ B0))
        print(f"D2 T={T} S3: <w,Q^T F A>/(sup|w| sum|Q^T F A|) {s3:.1e}, |d* F A|/|F A| {dsz:.1e}; "
              f"<w, A - Q^T F A> vs <w, B'_0> rel {e_dual:.1e}; FC(ii) ratio max|A - Q^T F A|/(L max|grad A|) "
              f"{fc2:.3f} ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)
        out[T] = row; out.setdefault("S3", []).append((s3, dsz))
        del ch, Pic, Gp
    return out


def trend(seq, rule_name):
    d_prev = seq[-2] - seq[-3]; d_last = seq[-1] - seq[-2]
    ok = d_last <= 0.5 * abs(d_prev) + 0.01 * seq[0]
    return ok, f"{rule_name}: seq {', '.join(f'{v:.4f}' for v in seq)}; last incr {d_last:+.4f} vs 0.5|prev| " \
               f"{0.5 * abs(d_prev):.4f} + {0.01 * seq[0]:.4f} -> {'PASS' if ok else 'FAIL'}"


if __name__ == "__main__":
    part = sys.argv[1]
    if part == "D3":
        res = part_D3()
        for kind in ("S-bump", "S-cusp"):
            for i, mp in enumerate(MPS):
                print("T3 " + kind + f" m'={mp} " + trend([res[(kind, 3, T)][i] for T in (2, 4, 8)], "doubling T (R=3)")[1])
                print("T3 " + kind + f" m'={mp} " + trend([res[(kind, R, 1)][i] for R in (3, 9, 27)], "tripling R (T=1)")[1])
    elif part == "D1a":
        res = part_D1([(1, 2), (1, 3), (1, 4), (1, 5)])
        for i, mp in enumerate(MPS):
            print(f"T1 m'={mp} " + trend([res[(1, T, 0)][i] for T in (2, 3, 4, 5)], "T = 2..5 (k=1, l=0)")[1])
    elif part == "D1b":
        part_D1([(2, 2)])
    elif part == "D2":
        res = part_D2([2, 3, 4, 5])
        for name in ("XR-designed", "RP-designed", "random"):
            print(f"T2 {name} Q_XR " + trend([res[T][name][0] for T in (2, 3, 4, 5)], "T = 2..5")[1]
                  + (" [informational]" if name == "random" else ""))
            print(f"   {name} Q_RP (informational) " + trend([res[T][name][1] for T in (2, 3, 4, 5)], "T = 2..5")[1])
        print(f"S2 all ok: {all(all(v) for kk, v in res.items() if isinstance(kk, tuple))}; "
              f"S3 max {max(s for s, _ in res['S3']):.1e}, d*z max {max(d for _, d in res['S3']):.1e}")
    print(f"ba4 {part}: time {time.time() - T0:.1f} s, peak RSS {rss():.0f} MB")
