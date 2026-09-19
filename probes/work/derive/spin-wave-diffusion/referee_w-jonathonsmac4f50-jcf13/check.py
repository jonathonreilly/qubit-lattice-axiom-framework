#!/usr/bin/env python3
"""Referee check for J:derive:spin-wave-diffusion:a3 (author w-macbookpro90c72-jbb16, grok-4.6).

Independent code; nothing is taken from the author's script. Sphere formation law on the periodic L x L level plane
(blocks 26, 34): the record at x is a von Mises-Fisher draw about S/|S| with concentration beta |S|, S the sum of the
three recorded predecessors x, x - e1, x - e2. sigma^2 = A(3 beta)/(3 beta), A(k) = coth k - 1/k, N = L^2,
M_t = N^-1 sum_x s_x(t), n_t = M_t/|M_t|; D_1 = per-component diffusion constant of n (so the probe's ratio is
D_1 L^2/sigma^2; the linearized law has ratio exactly 1, block 34).

C1  step 1: vMF moments (sympy): E[mu] = A, E[mu^2] = 1 - 2A/k, transverse variance A/k per component.
C2  step 3: Jacobian of x/|x| at (0, 0, m) is diag(1/m, 1/m, 0) for symbolic m.
C3  steps 2-4 as a ONE-STEP statement: from an aligned plane, N iid vMF(3 beta) draws; the per-component variance
    of n' = M'/|M'| against sigma^2/(N A^2) (Monte Carlo, 4 couplings) -- the attempt's 1/A(3 beta)^2.
C4  step 4 as a statement about D_1 (the diffusion constant defined in (1)): stationary simulation on L = 4 at
    beta = 12, 24, 48 from an aligned start after burn-in, D_1 from E[n_t . n_{t-l}] = exp(-D_1 l) at l = 20, 40
    (Brownian motion on S^2), against 1/A(3 beta)^2 and against 1/<|M|>^2 with the measured magnetization.
"""
from __future__ import annotations

import math

import numpy as np
import sympy as sp


def A(k):
    return 1.0 / np.tanh(k) - 1.0 / k


def c1():
    k, u = sp.symbols("kappa u", positive=True)
    Z = sp.integrate(sp.exp(k * u), (u, -1, 1))
    Emu = sp.integrate(u * sp.exp(k * u), (u, -1, 1)) / Z
    Emu2 = sp.integrate(u ** 2 * sp.exp(k * u), (u, -1, 1)) / Z
    Ak = sp.coth(k) - 1 / k
    return (sp.simplify((Emu - Ak).rewrite(sp.exp)) == 0 and sp.simplify((Emu2 - (1 - 2 * Ak / k)).rewrite(sp.exp)) == 0
            and sp.simplify(((1 - Emu2) / 2 - Ak / k).rewrite(sp.exp)) == 0)


def c2():
    m = sp.Symbol("m", positive=True)
    x = sp.Matrix(sp.symbols("x1 x2 x3", real=True))
    f = x / sp.sqrt(x.dot(x))
    J = f.jacobian(x).subs({x[0]: 0, x[1]: 0, x[2]: m})
    return sp.simplify(J - sp.diag(1 / m, 1 / m, 0)) == sp.zeros(3, 3)


def vmf(field, rng):
    kap = np.linalg.norm(field, axis=-1)
    U = rng.random(kap.shape)
    w = 1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap
    phi = 2 * np.pi * rng.random(kap.shape)
    r = np.sqrt(np.clip(1 - w * w, 0, None))
    n = field / kap[..., None]
    a = np.zeros_like(n)
    a[..., 0] = 1.0
    swap = np.abs(n[..., 0]) > 0.9
    a[swap, 0], a[swap, 1] = 0.0, 1.0
    e1 = np.cross(n, a)
    e1 /= np.linalg.norm(e1, axis=-1, keepdims=True)
    e2 = np.cross(n, e1)
    return w[..., None] * n + (r * np.cos(phi))[..., None] * e1 + (r * np.sin(phi))[..., None] * e2


def c3(L=4, reps=400_000, seed=1):
    rng = np.random.default_rng(seed)
    N = L * L
    out = []
    for beta in (6, 12, 24, 48):
        k = 3 * beta
        field = np.zeros((reps, N, 3))
        field[..., 2] = k
        s = vmf(field, rng)
        M = s.mean(axis=1)
        n = M / np.linalg.norm(M, axis=1, keepdims=True)
        var = 0.5 * (n[:, 0] ** 2 + n[:, 1] ** 2).mean()
        err = 0.5 * (n[:, 0] ** 2 + n[:, 1] ** 2).std() / math.sqrt(reps)
        s2 = A(k) / k
        out.append((beta, var * N / s2, err * N / s2, 1 / A(k) ** 2, 2 / (k * N)))
    return out


def c4(L=4, reps=12_000, burn=100, T=3000, lags=(20, 40), groups=12, seed=7):
    rng = np.random.default_rng(seed)
    N = L * L
    res = []
    gsz = reps // groups
    for beta in (12, 24, 48):
        s = np.zeros((reps, L, L, 3))
        s[..., 2] = 1.0
        hist = []
        acc = {l: np.zeros(groups) for l in lags}
        cnt = {l: 0 for l in lags}
        mag = 0.0
        nm = 0
        for t in range(burn + T):
            S = s + np.roll(s, 1, axis=1) + np.roll(s, 1, axis=2)
            s = vmf(beta * S, rng)
            if t >= burn:
                M = s.reshape(reps, N, 3).mean(axis=1)
                Mn = np.linalg.norm(M, axis=1)
                n = M / Mn[:, None]
                mag += Mn.mean()
                nm += 1
                hist.append(n)
                if len(hist) > max(lags) + 1:
                    hist.pop(0)
                for l in lags:
                    if len(hist) > l:
                        dots = (hist[-1] * hist[-1 - l]).sum(axis=1)
                        acc[l] += dots[: gsz * groups].reshape(groups, gsz).sum(axis=1)
                        cnt[l] += gsz
        l1, l2 = lags
        s2 = A(3 * beta) / (3 * beta)
        per_group = (np.log(acc[l1] / cnt[l1]) - np.log(acc[l2] / cnt[l2])) / (l2 - l1) * N / s2
        c1_all, c2_all = acc[l1].sum() / (cnt[l1] * groups), acc[l2].sum() / (cnt[l2] * groups)
        ratio = (math.log(c1_all) - math.log(c2_all)) / (l2 - l1) * N / s2
        err = per_group.std(ddof=1) / math.sqrt(groups)
        res.append((beta, ratio, err, 1 / A(3 * beta) ** 2, 1 / (mag / nm) ** 2, mag / nm))
    return res


def main():
    print(f"C1 vMF moments E[mu] = A, E[mu^2] = 1 - 2A/k, transverse variance A/k: {c1()}")
    print(f"C2 Jacobian of x/|x| at (0,0,m) = diag(1/m, 1/m, 0): {c2()}")
    r3 = c3()
    ok3 = True
    for beta, ratio, err, target, allow in r3:
        ok3 &= abs(ratio - target) < 4 * err + allow
        print(f"C3 one step from the aligned plane, L=4, beta={beta}: N Var(n'_perp)/sigma^2 = {ratio:.5f} +- {err:.5f}; "
              f"1/A(3 beta)^2 = {target:.5f} (difference {ratio - target:+.5f}, within 4 sigma + the O(1/(kappa N)) allowance "
              f"{allow:.4f}); linearized zero mode: 1")
    r4 = c4()
    diffs = []
    signif = []
    for beta, ratio, err, target, pred_m, mag in r4:
        diffs.append(beta * (ratio - target))
        signif.append((ratio - target) / err)
        print(f"C4 stationary, L=4, beta={beta}: D_1 L^2/sigma^2 = {ratio:.4f} +- {err:.4f}; 1/A(3 beta)^2 = {target:.4f}; "
              f"1/<|M|>^2 = {pred_m:.4f} (<|M|> = {mag:.5f}); beta (ratio - 1/A^2) = {beta * (ratio - target):.3f} "
              f"({(ratio - target) / err:.1f} sigma); beta (1/<|M|>^2 - 1/A^2) = {beta * (pred_m - target):.3f}")
    step4_fails = signif[0] > 4 and signif[1] > 3
    if c1() and c2() and ok3 and step4_fails:
        print("SUMMARY: fails at step 4 - the exact content is a one-step identity to leading order in 1/N (from an aligned plane "
              "the direction's increment variance is sigma^2/(N A(3 beta)^2); Monte Carlo on L = 4 gives " +
              ", ".join(f"{r:.4f} vs {t:.4f}" for b, r, e, t, c in r3) + " at beta = 6..48, gaps within O(1/(kappa N))), but step 4 "
              "names it D_1, the diffusion constant of (1); the aligned plane is not preserved, and on L = 4 the stationary "
              "D_1 L^2/sigma^2 is " + ", ".join(f"{r:.4f} +- {e:.4f}" for b, r, e, t, p, m in r4) + " at beta = 12, 24, 48 against "
              "1/A^2 = " + ", ".join(f"{t:.4f}" for b, r, e, t, p, m in r4) + " (beta(ratio - 1/A^2) = " +
              ", ".join(f"{d:.2f}" for d in diffs) + "; 1/<|M|>^2 = " + ", ".join(f"{p:.4f}" for b, r, e, t, p, m in r4) +
              ", below the measured values but also not 1/A^2): the O(1/beta) term of D_1 is not the aligned plane's 2/(3 beta); the limit 1 as beta -> infinity is "
              "not proved (step 5 open), and the SUMMARY's '(linearized zero-mode)' label contradicts block 34's linear ratio of 1")
    else:
        print(f"SUMMARY: fails - C1 {c1()}, C2 {c2()}, C3 {ok3}, C4 significance {signif}")


if __name__ == "__main__":
    main()
