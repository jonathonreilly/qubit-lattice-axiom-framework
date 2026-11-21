#!/usr/bin/env python3
"""Gate history-budget at 769697e8d. Criteria are in REGISTRATION.md, written first.

Abstract arithmetic and finite probability only. Nothing here is a statement
about the Wilson law. Same-model check, not independent and not an audit.
"""
import json
import math
import os
import resource
import sys
from itertools import product

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RSS_LIMIT_BYTES = 2 * 1024 ** 3


def guard():
    # macOS reports ru_maxrss in bytes.
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT_BYTES:
        sys.exit("stopping: above 2 GB RSS")


def stoch(rng, shape):
    a = rng.random(shape) ** 3 + 1e-3
    return a / a.sum(axis=-1, keepdims=True)


# ---------- T1: Theorem GH ----------

def random_chain(rng):
    J = int(rng.integers(1, 5))
    n = [int(rng.integers(2, 5)) for _ in range(J + 1)]
    P = [stoch(rng, (n[j + 1], n[j])) for j in range(J)]
    verts = [[] for _ in range(J + 1)]
    for level in range(J + 1):
        for _ in range(int(rng.integers(1, 4))):
            v = {}
            if level == 0:
                v["F"] = rng.normal(size=n[0])
                v["d"] = float(np.abs(v["F"]).max())
            else:
                v["S"] = rng.normal(size=n[level]) * rng.choice([0.0, 0.3, 1.0])
                k = int(rng.integers(1, len(verts[level - 1]) + 1))
                idx = rng.choice(len(verts[level - 1]), size=k, replace=False)
                v["e"] = [(int(u), float(rng.normal() * 2)) for u in idx]
                F = v["S"].copy()
                for u, t in v["e"]:
                    F = F + t * (P[level - 1] @ verts[level - 1][u]["F"])
                v["F"] = F
                v["B"] = rng.random(n[level]) < 0.6
                off = np.abs(F)[~v["B"]]
                v["b"] = float(off.max()) if off.size else 0.0
            verts[level].append(v)
    nu = stoch(rng, (n[J],))
    return J, n, P, verts, nu


def gh_rhs(level, v, mass, c, q, P, verts):
    """Right side of (GH) for the subtree of paths through vertex v, where
    mass is the restricted measure on V_level given by the path so far."""
    if level == 0:
        return c * v["d"] * mass.sum() ** (1 / q)
    B = v["B"]
    total = c * v["b"] * mass[~B].sum() ** (1 / q)
    total += c * (mass[B] * np.abs(v["S"][B]) ** q).sum() ** (1 / q)
    down = (mass * B) @ P[level - 1]
    for u, t in v["e"]:
        total += gh_rhs(level - 1, verts[level - 1][u], down, c * abs(t), q, P, verts)
    return total


def t1(rng, chains=4000):
    worst, best = 0.0, 0.0
    for i in range(chains):
        if i % 500 == 0:
            guard()
        J, n, P, verts, nu = random_chain(rng)
        root = verts[J][0]
        E = root["B"] if rng.random() < 0.5 else rng.random(n[J]) < 0.7
        for q in (1, 2, 4):
            lhs = (nu[E] * np.abs(root["F"][E]) ** q).sum() ** (1 / q)
            rhs = gh_rhs(J, root, nu * E, 1.0, q, P, verts)
            if rhs > 0:
                worst = max(worst, lhs / rhs - 1)
                best = max(best, lhs / rhs)
            elif lhs > 1e-12:
                worst = max(worst, 1.0)
    return {"max_excess": worst, "max_ratio": best,
            "pass": bool(worst <= 1e-9 and best >= 0.5)}


def t1c():
    """Copied bad bit, with P(D_p) wrongly replaced by a product of marginals."""
    violations = 0
    for J, p, b in product((2, 3, 4), (0.01, 0.1), (2.0, 4.0)):
        for q in (1, 2, 4):
            lhs = b ** J * p ** (1 / q)
            # one history term with bottom d_0 = 1 and J + 1 marginal factors
            wrong = b ** J * (p ** (J + 1)) ** (1 / q)
            violations += lhs > wrong * (1 + 1e-9)
    return {"violations": int(violations), "pass": violations > 0}


# ---------- T2: source table and identities ----------

def t2(rng, trials=200):
    worst = 0.0
    for _ in range(trials):
        K, m = 3, 2
        nc = [2 * m ** (K - j) for j in range(K + 1)]
        ns = [int(rng.integers(3, 6)) for _ in range(K + 1)]
        P = [stoch(rng, (ns[j + 1], ns[j])) for j in range(K)]
        x = list(np.exp(rng.normal(1, 0.3, size=K + 1)))
        blocks = lambda j: [list(range(m * c, m * (c + 1))) for c in range(nc[j + 1])]
        f = [rng.normal(size=nc[j]) for j in range(K + 1)]
        beta = rng.normal(size=K) * 0.2
        a = rng.normal(size=(ns[0], nc[0]))
        a[0] = 0
        z, rho, r = 1.0, np.zeros_like(a), np.zeros_like(a)
        total = a.sum(axis=1)  # T_0(V) - T_0(1)
        y = (a * f[0]).sum(axis=1)

        def C(j, e):
            pe = P[j] @ e
            return pe - pe[0]

        def H(j, e):
            ce = C(j, e)
            return np.stack([ce[:, b].sum(axis=1) for b in blocks(j)], axis=1)

        for j in range(K):
            D = z * a + rho
            t = x[j + 1] / x[j]
            a1 = rng.normal(size=(ns[j + 1], nc[j + 1]))
            a1[0] = 0
            Iraw = rng.normal(size=(ns[j + 1], nc[j + 1], nc[j + 1]))
            I = Iraw - np.swapaxes(Iraw, 1, 2)
            I[0] = 0
            Jc = I.sum(axis=2)
            ha, hr = H(j, a), H(j, rho)
            h = ha - a1 - Jc
            Rem = hr - beta[j] * a1
            rho1 = Rem + z * h
            z1 = z + beta[j]
            D1 = z1 * a1 + rho1
            # r^f recipe
            r1 = H(j, r).copy()
            for cp, b in enumerate(blocks(j)):
                for c in b:
                    r1[:, cp] += (f[j][c] - f[j + 1][cp]) * C(j, D)[:, c]
                r1[:, cp] += (z / 2) * ((f[j + 1][cp] - f[j + 1])[None, :] * I[:, cp, :]).sum(axis=1)
            # (G1)
            errs = [np.abs(D1 - (H(j, D) - z * Jc)).max()]
            # total mark and y identities
            pt = P[j] @ total
            total = pt - pt[0]
            y = P[j] @ y
            errs.append(np.abs(D1.sum(axis=1) - (total - total[0])).max())
            lhs = y - y[0]
            rhs = (f[j + 1][None, :] * D1 + r1).sum(axis=1)
            errs.append(np.abs(lhs - rhs).max())
            # source table rows, section 2
            Fe = lambda e: x[j] * e
            v = lambda e: (P[j] @ Fe(e))[0]
            A, A1 = x[j] * a, x[j + 1] * a1
            xp = x[j + 1]
            block_sum = lambda vec: np.array([vec[b].sum() for b in blocks(j)])
            tr = lambda e: t * np.stack([(P[j] @ Fe(e))[:, b].sum(axis=1) for b in blocks(j)], axis=1)
            refsub = lambda e: t * block_sum(v(e))
            # D row
            errs.append(np.abs(xp * D1 - (tr(D) - refsub(D) - xp * z * Jc)).max())
            # rho row
            pa = tr(a) - refsub(a)
            errs.append(np.abs(xp * rho1 - (tr(rho) - refsub(rho) + z * pa - (z + beta[j]) * A1 - xp * z * Jc)).max())
            # Rem row
            errs.append(np.abs(xp * Rem - (tr(rho) - refsub(rho) - beta[j] * A1)).max())
            # H row and h row
            errs.append(np.abs(xp * ha - (tr(a) - refsub(a))).max())
            errs.append(np.abs(xp * h - (pa - A1 - xp * Jc)).max())
            # r row
            out = tr(r) - refsub(r)
            for cp, b in enumerate(blocks(j)):
                for c in b:
                    d = f[j][c] - f[j + 1][cp]
                    out[:, cp] += t * d * ((P[j] @ Fe(D))[:, c] - v(D)[c])
                out[:, cp] += xp * (z / 2) * ((f[j + 1][cp] - f[j + 1])[None, :] * I[:, cp, :]).sum(axis=1)
            errs.append(np.abs(xp * r1 - out).max())
            worst = max(worst, max(errs))
            a, rho, r, z = a1, rho1, r1, z1
    return {"max_error": float(worst), "pass": bool(worst <= 1e-10)}


# ---------- T3: scalar sum ----------

def log_psi(a, lam, y, bp, cG, l1, one_level=False):
    a = np.asarray(a, dtype=float)
    if one_level:
        h, s = np.zeros_like(a), np.ones_like(a)
        tail = np.zeros_like(a)
    else:
        h = np.floor(a / 2)
        s = a - h
        tail = l1 * (a - 1 + h) * (a - h) / 2  # sum_(r=h..a-1) r
    t1_ = np.log(s) - cG * (y + bp * h) ** 1.5
    t2_ = -s * lam - tail
    return np.minimum(0.0, np.logaddexp(t1_, t2_))


def log_sum(terms):
    return float(np.logaddexp.reduce(terms))


def e_star(X, N, B, bp, cG, l0):
    Y = X / 2
    D = N * math.exp(B / (2 * Y))
    muG = 3 * cG * bp * math.sqrt(Y) / 16
    r1, r2 = D * math.exp(-muG), D * math.exp(-l0 / 8)
    if r1 >= 1 or r2 >= 1:
        return None
    return (D * math.exp(-cG * Y ** 1.5 / 4) / (1 - r1) ** 2
            + D * math.exp(-l0 / 8) / (1 - r2))


def t3(depth=4000):
    worst = 0.0
    tested = 0
    a = np.arange(1, depth + 1)
    for N, B, bp, cG, alpha, l1, X, SoN, Aval in product(
            (1e3, 1e6, 1e9), (1.0, 5.0), (0.2, 1.0), (1e-2, 0.1), (0.05, 0.5),
            (1e-3, 0.1), (1e3, 1e4, 1e5, 1e6), (1.0, 3.0), (20.0, 1e3)):
        l0 = alpha * X
        es = e_star(X, N, B, bp, cG, l0)
        if es is None:
            continue
        tested += 1
        Y = X / 2
        for xJ, K_J in ((Y, 0), (2 * X, 0), (2 * X + B * 50, 50)):
            y = max(Y, Y + bp * K_J)
            lam = l0 + l1 * K_J
            lpsi = log_psi(a, lam, y, bp, cG, l1)
            lw = a * math.log(N) + 0.5 * np.log1p(B * a / xJ)
            direct = log_sum(lw + lpsi / 4)
            # Full ratio: good stops, sources, one bottom at each J in the depth range.
            good = lw + lpsi / 4 + math.log(1 / 8)
            src = (a - 1) * math.log(N) + 0.5 * np.log1p(B * (a - 1) / xJ) + lpsi / 4 + math.log(SoN * N)
            bottom = a * math.log(N) + math.log(12 / (Aval * math.sqrt(xJ))) + lpsi / 4
            full = np.logaddexp(log_sum(good), log_sum(src))
            full_with_bottom = float(np.logaddexp(full, bottom.max()))
            bound = (1 / 8 + SoN + 12 / (Aval * math.sqrt(Y))) * es
            if es > 0:
                worst = max(worst, math.exp(direct) / es - 1 if direct < 700 else 1e9)
                worst = max(worst, math.exp(full_with_bottom) / bound - 1)
    guard()
    # X needed at sample constants: L = 5, spatial constants of order ten.
    samples = []
    for name, N, B, bp, cG, alpha in (
            ("L5 single tier", 1250.0, 5.0, 0.3, 1e-3, 1e-3),
            ("L5 two tier, kappa_s small", 1250.0, 5.0, 0.3, 1e-5, 1e-3),
            ("L25 two tier", 2 * 25.0 ** 4, 10.0, 0.6, 1e-7, 1e-4)):
        X = 1e2
        while True:
            es = e_star(X, N, B, bp, cG, alpha * X)
            if es is not None and (1 / 8 + 3 + 12 / (20 * math.sqrt(X / 2))) * es <= 0.5:
                break
            X *= 1.2
        samples.append({"case": name, "X_min_within_20pct": X})
    return {"tested": tested, "max_excess": worst, "samples": samples,
            "pass": bool(worst <= 1e-9 and tested > 100)}


def t3prime(depth=4000):
    worst = 0.0
    tested = near = 0
    a = np.arange(1, depth + 1)
    for N, B, bp, cG, alpha, l1, X, SoN, Aval in product(
            (1e3, 1e6, 1e9), (1.0, 5.0), (0.2, 1.0), (1e-5, 1e-3, 0.1), (1e-3, 0.05, 0.5),
            (1e-3, 0.1), (1e6, 1e8, 1e10, 1e12, 1e14), (1.0, 3.0), (20.0, 1e3)):
        l0 = alpha * X
        es = e_star(X, N, B, bp, cG, l0)
        if es is None:
            continue
        tested += 1
        Y = X / 2
        D = N * math.exp(B / (2 * Y))
        muG = 3 * cG * bp * math.sqrt(Y) / 16
        near += max(D * math.exp(-muG), D * math.exp(-l0 / 8)) > 0.5
        for xJ, K_J in ((Y, 0), (2 * X, 0), (2 * X + B * 50, 50)):
            y = Y + bp * K_J
            lam = l0 + l1 * K_J
            lpsi = log_psi(a, lam, y, bp, cG, l1)
            lw = a * math.log(N) + 0.5 * np.log1p(B * a / xJ)
            direct = log_sum(lw + lpsi / 4)
            good = lw + lpsi / 4 + math.log(1 / 8)
            src = (a - 1) * math.log(N) + 0.5 * np.log1p(B * (a - 1) / xJ) + lpsi / 4 + math.log(SoN * N)
            bottom = a * math.log(N) + math.log(12 / (Aval * math.sqrt(xJ))) + lpsi / 4
            full = np.logaddexp(log_sum(good), log_sum(src))
            full_with_bottom = float(np.logaddexp(full, bottom.max()))
            bound = (1 / 8 + SoN + 12 / (Aval * math.sqrt(Y))) * es
            if es > 0:
                worst = max(worst, math.exp(direct) / es - 1 if direct < 700 else 1e9)
                worst = max(worst, math.exp(full_with_bottom) / bound - 1)
    guard()
    return {"tested": tested, "near_denominator_points": int(near), "max_excess": worst,
            "pass": bool(worst <= 1e-9 and tested >= 500 and near >= 20)}


def t3c():
    a = np.arange(1, 100001)
    N, B, bp, cG, l1, lam, y, xJ = 1e4, 5.0, 0.3, 1e-3, 1e-2, 1e3, 5e3, 1e4
    lpsi = log_psi(a, lam, y, bp, cG, l1, one_level=True)
    lw = a * math.log(N) + 0.5 * np.log1p(B * a / xJ)
    return {"log_direct_sum": log_sum(lw + lpsi / 4),
            "pass": bool(log_sum(lw + lpsi / 4) > 0)}


# ---------- T4: radius lemma ----------

def radius_holds(x, lam):
    x = np.asarray(x, dtype=float)
    lam = np.asarray(lam, dtype=float)
    small = lam / 5 < 600
    ok = np.ones_like(x, dtype=bool)
    ok[small] = x[small] ** 2 + 3 < np.floor(np.exp(lam[small] / 5))
    ok[~small] = 2 * np.log(x[~small]) < lam[~small] / 5 - 1e-9
    return ok


def t4(rng, draws=2000):
    fails = acount_fails = 0
    d = np.unique(np.concatenate([np.arange(0, 2001), np.logspace(3.3, 6, 400).astype(np.int64)]))
    for i in range(draws):
        if i % 500 == 0:
            guard()
        B = 10 ** rng.uniform(-1, 1.5)
        l1 = 10 ** rng.uniform(-3, 0)
        alpha = 10 ** rng.uniform(-3, 0)
        X = max(1.0, B, 10 * B / l1)
        while alpha * X < 5 * math.log(4 * X * X + 5):
            X *= 1.5
        X *= rng.uniform(1, 3)
        CAA = 10 ** rng.uniform(0, 4)
        Xa = X
        while math.log(CAA) + 8 * math.log(2 * Xa + 2) > alpha * Xa:
            Xa *= 1.3
        for xK_base, check_a in ((X, False), (Xa, True)):
            xK = xK_base * rng.uniform(1, 2)
            lam = alpha * xK_base + l1 * d
            # extremal sequence, and a random one obeying FLOW-UL pointwise
            seqs = [xK + B * d, xK + B * d * rng.uniform(0, 1, size=d.size)]
            for x in seqs:
                fails += int((~radius_holds(x, lam)).sum())
                if check_a:
                    acount_fails += int((math.log(CAA) + 8 * np.log(x + 2) > lam + 1e-9).sum())
    return {"radius_failures": fails, "acount_failures": acount_fails,
            "pass": bool(fails == 0 and acount_fails == 0)}


def t4c():
    # (a) geometric sequence violating FLOW-UL, l_1 below 10 log(5/4).
    d = np.arange(0, 2000)
    logx = math.log(1e3) + d * math.log(5 / 4)
    lam = 200.0 + 0.5 * d
    bad_a = int((2 * logx > lam / 5).sum())
    # (b) fixed l_0 with large x_K, at d = 0.
    bad_b = bool(1e4 ** 2 + 3 >= math.floor(math.exp(30.0 / 5)))
    return {"geometric_failures": bad_a, "fixed_l0_fails": bad_b,
            "pass": bool(bad_a > 0 and bad_b)}


# ---------- T5: K-transport ----------

def t5(rng, draws=2000):
    worst = 0.0
    tight = 0.0
    for i in range(draws):
        if i % 500 == 0:
            guard()
        nn, nr, nu_loc, ny = 2, 3, 4, 3
        nuw = stoch(rng, (nn * nr,)).reshape(nn, nr)
        kern = stoch(rng, (nn, nr, nu_loc * ny)).reshape(nn, nr, nu_loc, ny)
        G = rng.normal(size=(nu_loc, ny))
        nuv = np.einsum("nr,nruy->uy", nuw, kern)
        pu = nuv.sum(axis=1)
        Gn = (nuv * G).sum(axis=1) / pu
        l1 = (nuv * np.abs(G - Gn[:, None])).sum()
        l2 = math.sqrt((nuv * G ** 2).sum())
        # conditional-mean error of PG
        PG = np.einsum("nruy,uy->nr", kern, G)
        pn = nuw.sum(axis=1)
        cond = nuw / pn[:, None]
        mean = (cond * PG).sum(axis=1)
        ell = (nuw * np.abs(PG - mean[:, None])).sum()
        # tau over all sign vectors on the local block
        marg = kern.sum(axis=3)  # E_W of a function of u
        tau = 0.0
        for signs in product((-1.0, 1.0), repeat=nu_loc):
            F = np.array(signs)
            EF = marg @ F  # shape n, r
            val = 0.0
            for n in range(nn):
                diff = np.abs(EF[n][:, None] - EF[n][None, :])
                val += pn[n] * (cond[n][:, None] * cond[n][None, :] * diff).sum()
            tau = max(tau, val)
        rhs = 2 * l1 + 3 * l2 * math.sqrt(tau)
        worst = max(worst, ell / rhs - 1)
        tight = max(tight, ell / rhs)
    return {"max_excess": worst, "max_ratio": tight, "pass": bool(worst <= 1e-9)}


# ---------- T6: bounded shell ----------

def t6():
    kappa, CB, C = 1.0, 1.0, 1.0
    out = []
    for x in (100.0, 150.0, 200.0):
        lam = x
        M = math.floor(math.exp(lam / 5))
        m = M // 2
        s = int(math.floor(math.sqrt(m / lam)))
        n = np.arange(m + 1, m + min(s, 5_000_000) + 1, dtype=float)
        phi_ratio = np.exp(-kappa * (np.sqrt(n * lam) - math.sqrt(m * lam)))
        ell_over_eta_phi = 0.5 * phi_ratio.sum() * (s / n.size)
        budget = C * CB * x ** 2
        out.append({"x": x, "s": s, "m_gt_lambda": bool(m > lam),
                    "m_plus_s_le_M": bool(m + s <= M),
                    "increment_gap": math.sqrt((m + s) * lam) - math.sqrt(m * lam),
                    "ell_over_U_B_Phi": ell_over_eta_phi / budget})
    return {"cases": out, "pass": any(c["ell_over_U_B_Phi"] > 1 and c["m_gt_lambda"]
                                      and c["m_plus_s_le_M"] for c in out)}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "t3prime":
        res = t3prime()
        print("T3p", json.dumps(res), flush=True)
        with open(os.path.join(HERE, "results_t3prime.json"), "w") as fh:
            json.dump(res, fh, indent=1)
        return 0 if res["pass"] else 1
    rng = np.random.default_rng(769697)
    results = {}
    for name, fn in (("T1", lambda: t1(rng)), ("T1c", t1c), ("T2", lambda: t2(rng)),
                     ("T3", t3), ("T3c", t3c), ("T4", lambda: t4(rng)), ("T4c", t4c),
                     ("T5", lambda: t5(rng)), ("T6", t6)):
        results[name] = fn()
        guard()
        print(name, json.dumps(results[name]), flush=True)
        with open(os.path.join(HERE, "results.json"), "w") as fh:
            json.dump(results, fh, indent=1)
    return 0 if all(r["pass"] for r in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
