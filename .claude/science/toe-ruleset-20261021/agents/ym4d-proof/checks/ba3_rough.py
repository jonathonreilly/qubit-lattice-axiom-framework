"""ba3: BFT lane A, session 3 (criteria: checks/ba3_criteria.md, written before this file).

R1 Lemma RS + Lemma BR-1 (exact rough reduction); R2 Lemma CR-1 (commutator row is residual type) + BCH sign;
R3 Lemma TS (top source, configuration level); R4 Lemma Lambda (root-to-root holonomy); R5 Lemma LR-pot (tent-axial
slice). Real-space chains of checks/c26_led.py and the CG code of checks/ba2_lin.py (imported, read-only).
Usage: python3 ba3_rough.py
"""
import itertools
import time

import numpy as np
from scipy.linalg import expm, logm

import ba2_lin as b2

c26 = b2.c26
L = c26.L
T0 = time.time()
OK = {}


def flag(name, cond):
    OK[name] = OK.get(name, True) and bool(cond)


def mx(a):
    return float(np.max(np.abs(a)))


def rel(a, b):
    return mx(a - b) / max(mx(a), 1e-300)


# ------------------------------------------------------------------ R1, R3 (k = 2, T = 2)
def part_R1_R3(rng):
    for kap in ((1.0, 1.0), (0.5, 2.0)):
        tt = time.time()
        ch = b2.SChain(4, 2, 2, kap); lv = ch.levels
        D1T = ch.D[1].T.tocsr()
        D2 = lv[2].dmat().toarray()
        cst2 = np.zeros((lv[2].NL, 4))
        for mu in range(4):
            cst2[mu * lv[2].N:(mu + 1) * lv[2].N, mu] = 1.0
        A = np.hstack([D2.T, cst2])                       # spans C_2 (co-closed level-2 1-forms)
        QA = (ch.Q[1].T @ A)                             # Q_1^T C_2 (dense, NL_1 x 100)
        j = D1T @ rng.normal(size=ch.D[1].shape[0]) + np.repeat(rng.normal(size=4), lv[1].N)
        coef = np.linalg.lstsq(QA, j, rcond=None)[0]
        w = j - QA @ coef
        G1T = b2.gradmat(lv[1]).T.tocsr()
        a1 = mx(G1T @ w) / mx(w)
        nrm = np.linalg.norm(QA, axis=0); keep = nrm > 1e-12
        a2 = float(np.max(np.abs(QA[:, keep].T @ w) / (np.linalg.norm(w) * nrm[keep])))
        a3 = max(abs(float(w[mu * lv[1].N:(mu + 1) * lv[1].N].mean())) for mu in range(4)) / mx(w)
        flag("R1a", a1 <= 1e-11 and a2 <= 1e-10 and a3 <= 1e-11)
        Q1w = ch.Q[1] @ w
        G2 = b2.gradmat(lv[2]).toarray()
        cg2 = np.linalg.lstsq(G2, Q1w, rcond=None)[0]
        b1 = float(np.linalg.norm(Q1w - G2 @ cg2) / np.linalg.norm(Q1w))
        flag("R1b", b1 <= 1e-9)
        Bk = rng.normal(size=ch.ntop)
        x, res1, it1 = ch.cg(Bk, ch.grad_src(j=[None, w]))
        By = Bk - Q1w / kap[0]
        y, res2, it2 = ch.cg(By, ch.grad_src(j=[ch.Q[0].T @ w, None]))
        rx, fx, _ = ch.outs(x, Bk); ry, fy, _ = ch.outs(y, By)
        c1 = max(rel(rx[0], ry[0] - w / kap[0]), rel(rx[1], ry[1]), rel(fx[0], fy[0]),
                 rel(fx[1], fy[1] + ch.D[1] @ w / kap[0]))
        flag("R0", max(res1, res2) <= 1e-10); flag("R1c", c1 <= 1e-7)
        print(f"R1 kap={kap}: |d*w|/|w| {a1:.1e}, max cos(w, Q^T C_2) {a2:.1e}, |mean w|/|w| {a3:.1e}; "
              f"|Q_1w perp Ran d|/|Q_1w| {b1:.1e}; BR-1 rel {c1:.2e} (CG res {res1:.1e}/{res2:.1e}, {it1}/{it2} it); "
              f"info |Q_1w|/|Q_1j| {mx(Q1w) / mx(ch.Q[1] @ j):.3f}, |w|/|j| {mx(w) / mx(j):.3f}", flush=True)
        if kap == (0.5, 2.0):
            s1 = rng.normal(size=ch.ntop)
            x, r1_, i1 = ch.cg(Bk, ch.grad_src(s=[None, s1]))
            y, r2_, i2 = ch.cg(Bk + s1 / kap[1], np.zeros_like(x))
            d3 = rel(x, y)
            flag("R0", max(r1_, r2_) <= 1e-10); flag("R3", d3 <= 1e-9)
            print(f"R3 kap={kap}: configuration rel {d3:.2e} (CG res {r1_:.1e}/{r2_:.1e}, {i1}/{i2} it)", flush=True)
        print(f"   ({time.time() - tt:.0f} s, RSS {b2.rss():.0f} MB)", flush=True)


# ------------------------------------------------------------------ R2
def part_R2(rng):
    kap = 0.7; dev = 0.0
    Q = rng.normal(size=(12, 30)); xl = rng.normal(size=(30, 3)); xu = rng.normal(size=(12, 3))
    q = Q @ xl; r = q - xu; s = 0.5 * kap * np.cross(xu, r)
    for _ in range(50):
        ul = rng.normal(size=(30, 3)); uu = rng.normal(size=(12, 3))
        row = -0.5 * kap * float(np.sum(r * (np.cross(uu, q) + np.cross(xu, Q @ ul))))
        res = float(np.sum(s * (Q @ ul - uu)))
        dev = max(dev, abs(row - res) / max(abs(row), 1e-300))
    flag("R2", dev <= 1e-12)
    worst = 0.0
    for _ in range(20):
        mats = []
        for _ in range(2):
            h = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            a = (h - h.conj().T) / 2; a -= np.trace(a) / 2 * np.eye(2); a /= max(np.linalg.norm(a), 1.0)
            mats.append(a)
        a, b = mats
        for eps in (1e-2, 1e-3):
            lg = logm(expm(-eps * a) @ expm(eps * b))
            err = np.linalg.norm(lg - eps * (b - a) + 0.5 * eps ** 2 * (a @ b - b @ a))
            worst = max(worst, err / eps ** 3)
    flag("R2", worst <= 10.0)
    print(f"R2: commutator row vs residual form, max rel dev {dev:.1e}; BCH max err/eps^3 {worst:.3f}", flush=True)


# ------------------------------------------------------------------ R4, R5 helpers
def as_arr(v, lv):
    return v.reshape((lv.d,) + (lv.n,) * lv.d)


def smooth_field(rng, lv):
    a = rng.normal(size=(lv.d,) + (lv.n,) * lv.d)
    for _ in range(2):
        b = np.zeros_like(a)
        for sh in itertools.product((-1, 0, 1), repeat=lv.d):
            b += np.roll(a, sh, axis=tuple(range(1, lv.d + 1)))
        a = b / 3 ** lv.d
    return a.reshape(-1)


def Lam(x0a, n, T):
    """Lambda(X, mu): straight level-0 sum from the root c_X = nX + (n-1)/2 to c_X + n e_mu; shape (4, T,T,T,T)."""
    h = (n - 1) // 2; out = np.zeros((4,) + (T,) * 4)
    idx = np.arange(T) * n + h
    for mu in range(4):
        acc = 0.0
        for t in range(n):
            ix = [idx] * 4; ix = [i.copy() for i in ix]; ix[mu] = (idx + t) % (n * T)
            acc = acc + x0a[mu][np.ix_(*ix)]
        out[mu] = acc
    return out


ORDERS = list(itertools.permutations(range(4)))


def tent_lambda(x0a, n, T):
    """P lambda = sum_X chi_X lambda_X, lambda_X(z) = -avg_sigma (axial line sum c_X -> z), on the level-0 torus."""
    S = n * T; h = (n - 1) // 2; lam = np.zeros((S,) * 4)
    o = np.arange(-n, n + 1); W = 2 * n + 1
    E = 2 * n + 3                                          # local box with one spare site each side
    tent1 = 1.0 - np.abs(o) / n
    chi = tent1[:, None, None, None] * tent1[None, :, None, None] * tent1[None, None, :, None] * tent1[None, None, None, :]
    grid = np.indices((W,) * 4) + 1                        # local coordinates of the box points (centre at n+1)
    for X in itertools.product(range(T), repeat=4):
        c = np.array(X) * n + h
        ix = [((c[i] + np.arange(-n - 1, n + 2)) % S) for i in range(4)]
        Sx = []
        for nu in range(4):
            loc = x0a[nu][np.ix_(*ix)]
            cs = np.zeros_like(loc); cs = np.cumsum(loc, axis=nu) - loc   # S_nu(q) = sum_{t<q_nu} x_nu(t)
            Sx.append(cs)
        lamX = np.zeros((W,) * 4)
        for sig in ORDERS:
            p = [np.full((W,) * 4, n + 1) for _ in range(4)]
            tot = np.zeros((W,) * 4)
            for nu in sig:
                q = [pp.copy() for pp in p]; q[nu] = grid[nu]
                tot += Sx[nu][tuple(q)] - Sx[nu][tuple(p)]
                p = q
            lamX -= tot
        lamX /= len(ORDERS)
        gi = np.ix_(*[((c[i] + o) % S) for i in range(4)])
        np.add.at(lam, gi, chi * lamX)
    return lam


def dlam(lam):
    return np.stack([np.roll(lam, -1, axis=mu) - lam for mu in range(4)])


def part_R4_R5(rng):
    for (T, k) in ((3, 1), (2, 2), (4, 1)):
        tt = time.time()
        kap = (1.0,) * k
        ch = b2.SChain(4, T, k, kap); lv = ch.levels; n = L ** k
        Qc = ch.Q[0]
        for l in range(1, k):
            Qc = (ch.Q[l] @ Qc).tocsr()
        Bk = rng.normal(size=ch.ntop)
        x, res, its = ch.cg(Bk, np.zeros(ch.M.shape[1]))
        flag("R0", res <= 1e-10)
        xs = ch.split(x)
        cfgs = {"a": (xs[0], Bk, [ch.Q[i] @ xs[i] - (xs[i + 1] if i + 1 < k else Bk) for i in range(k)]),
                "b": (rng.normal(size=lv[0].NL), None, None), "c": (smooth_field(rng, lv[0]), None, None)}
        for name, (x0, B, rr) in cfgs.items():
            f0 = n ** 2 * mx(ch.D0 @ x0)
            x0a = as_arr(x0, lv[0])
            lam_s = Lam(x0a, n, T)
            qx = as_arr(Qc @ x0, lv[k])
            dev = mx(lam_s - qx)
            flag("R4", dev <= 10 * f0)
            msg = f"T={T} k={k} cfg {name}: R4 |Lam - Q x_0| / ||f_0|| = {dev / f0:.4f} (bound 10)"
            if k == 1:
                if B is None:
                    r0 = rng.normal(size=lv[1].NL) * 0.3
                    B = Qc @ x0 - r0; rr = [r0]
                lam = tent_lambda(x0a, n, T)
                h = (n - 1) // 2; roots = np.arange(T) * n + h
                a1 = mx(lam[np.ix_(roots, roots, roots, roots)]) / max(mx(lam), 1e-300)
                px = x0a + dlam(lam)
                lam2 = tent_lambda(px, n, T)
                a2 = mx(lam2) / max(mx(px), 1e-300)
                flag("R5a", a1 <= 1e-12 and a2 <= 1e-11)
                sh = np.roll(x0a, n, axis=1)
                lam3 = tent_lambda(sh, n, T)
                b5 = rel(np.roll(px, n, axis=1), sh + dlam(lam3))
                flag("R5b", b5 <= 1e-11)
                pc = n * mx(px)
                bnd1 = 75 * f0 + 8 * mx(lam_s)
                bnd2 = 155 * f0 + 8 * mx(B) + 40 * sum(L ** (k - 1 - i) * mx(rr[i]) for i in range(k))
                flag("R5c", pc <= bnd1 and pc <= bnd2)
                msg += (f"; R5a |lam(roots)| {a1:.1e}, |lam(Px)|/|Px| {a2:.1e}; R5b {b5:.1e}; R5c ||(Px)^c_0|| {pc:.3f}, "
                        f"ratio to bounds {pc / bnd1:.4f} / {pc / bnd2:.4f} (||x_0^c|| {n * mx(x0):.3f}, ||f_0|| {f0:.3f}, "
                        f"max|Lam| {mx(lam_s):.3f})")
            print(msg, flush=True)
        print(f"   ({time.time() - tt:.0f} s, RSS {b2.rss():.0f} MB)", flush=True)


if __name__ == "__main__":
    rng = np.random.default_rng(20261028 + 3)
    part_R2(rng)
    part_R1_R3(rng)
    part_R4_R5(rng)
    for kk in ("R0", "R1a", "R1b", "R1c", "R2", "R3", "R4", "R5a", "R5b", "R5c"):
        print(f"{kk}: {'PASS' if OK.get(kk, False) else 'FAIL (or not run)'}")
    print(f"ba3: time {time.time() - T0:.0f} s, peak RSS {b2.rss():.0f} MB")
