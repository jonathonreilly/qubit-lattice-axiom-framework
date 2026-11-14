#!/usr/bin/env python3
"""The excess of Wilson energy along the minimal chain. Consumer: the telescoping route to (VAL_k) in `library/sector-values.md`, which replaces the per-level contraction (LIFT-I).

Written before running. With A_l^W the Wilson action at level l, and e_j(V') := A_j^W(V^*(V')) - A_{j+1}^W(V'), the sum over the chain telescopes exactly: sum_{j<k} e_j(V_{j+1}) = A_k(V) - A_k^W(V). If e_j dominates the gradient energy of the parent, then the sum over all levels of the gradient energy is bounded by the top alone, and nothing per level has to contract. Four things are claimed, at the abelian level or in a model.

 X1. Coercivity at one level: on closed forms, g(P) - L^(d-4) >= c_e |P-hat|^2, with g the one-level minimal Wilson energy over |F'|^2, c_e > 0; in d = 4 this is g - 1. By hand, from the main alias: on an axis P, g = D^-4, so c_e -> 1/6; with two equal components, g = D^-6 and |P-hat|^2 doubles, so 1/8; with four, D^-12 and four times, so 1/8. So I predict c_e near 1/8 at large L, and the aliases only lower g, so somewhat below. (Corrected before the criteria were applied: a first run of E3, E4 used the d = 4 normalisation in d = 2, which made e negative; it was stopped, and E1, E2 are d = 4 and unaffected. In that run the minimum was at three equal components with the field along the fourth, g = D^-8, c_e = (1/9)(1 - 1/L^2), which I had not listed.)
 X2. For a composite: the level-(n-1) field of the minimal lift of a parent lies in the fibre, so its Wilson energy is at least the one-level minimum. As forms in the parent field: E_(n) - E_(1) >= 0. So c_e at level j is at least the one-level c_e, free of j.
 X3. Domination across sectors, in the toy of `checks/hard-core--mapped_sector_value.py`: its source Z against the excess e of the same parent, at charged patches and neutral pairs.
 X4. Non-abelian: at a true SU(2) constrained minimiser with the comb, d = 2, e >= c |grad' F'|^2 up to terms of order f E, with non-commuting parents, by a small random search for the smallest ratio.

PRE-STATED criteria.
 E1. d = 4: c_e(L) >= 0.05 for L = 3, 5, 7, 11, 17, over a grid including small P, and c_e(17) >= 0.7 c_e(7). Reported: the P of the minimum.
 E2. d = 4: min eig (E_(n) - E_(1)) >= -1e-8 at (L, n) = (3, 2), (3, 3), (5, 2). Control: at n = 1 the two agree to 1e-8.
 E3. Toy: with R_1 := max over charged patches of |Z|/e and R_0 := the same for neutral pairs, R_0/3 <= R_1 <= 3 R_0, and over n = 4, 6, 8, 10 the ratio |Z|/e in charged patches varies by at most a factor 3.
 E4. SU(2): over the random parents at f = 0.02, 0.05, 0.1, L = 3, 5: e/|grad' F'|^2 >= 0.5 c_e(d = 2, L), where c_e(d = 2, L) is computed as in E1 on the momenta of the torus. Only converged solves are used.
FAIL if any fails. A failure of E1 or E2 would end this route. A failure of E4 at f = 0.1 only would mean that the f E term matters at that size, and is reported as such.

Limits. E1, E2 are abelian, on a grid. E3 is U(1), d = 2, with a lift by hand. E4 is d = 2, low modes, a random and not a thorough search. RSS guard 2 GB.
"""
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


lg = load("lg", "hard-core--mapped_lift_gradient.py")


def forms(P, L, n, d):
    """In the basis of A' transverse to P-hat: Min := one-level minimal energy form at block side L^n, and E := the Wilson energy of the level-(n-1) field. Both over |P-hat|^2, so over |F'|^2."""
    Pv = np.asarray(P, float)
    Phat = 2 * np.sin(Pv / 2)
    P2 = float(np.sum(Phat**2))
    B = L**n
    k, q = lg.qvec(Pv, B, d)
    khat = 2 * np.sin(k / 2)
    k2 = np.sum(khat**2, axis=1)
    G = np.diag(np.sum(q * q / k2[:, None], axis=0))
    u = Phat / P2**0.5
    Perp = np.linalg.svd(np.eye(d) - np.outer(u, u))[0][:, : d - 1]
    Ginv = Perp @ np.linalg.inv(Perp.T @ G @ Perp) @ Perp.T
    Min = B**d * Perp.T @ Ginv @ Perp / P2
    B1 = L ** (n - 1)
    grids = np.meshgrid(*[np.arange(L)] * d, indexing="ij")
    ms = np.stack([g.ravel() for g in grids], axis=-1)
    kappas = (Pv[None, :] + 2 * np.pi * ms) / L
    ghat = np.zeros((len(kappas), d, d))
    if B1 == 1:
        ghat = np.einsum("mi,ij->mij", q / k2[:, None], np.eye(d))
    else:
        for m, ka in enumerate(kappas):
            kf, q1 = lg.qvec(ka, B1, d)
            lk = np.rint((kf * B - Pv[None, :]) / (2 * np.pi)).astype(np.int64)
            sg = 1.0 - 2.0 * (lk % 2)
            Df = lg.dirichlet(kf, B)
            qf = sg * B * Df * np.prod(Df, axis=1, keepdims=True)
            kh = 2 * np.sin(kf / 2)
            kk = np.sum(kh**2, axis=1)
            ghat[m] = np.diag(np.sum(q1 * qf / kk[:, None], axis=0))
    ka_hat = 2 * np.sin(kappas / 2)
    ka2 = np.sum(ka_hat**2, axis=1)
    Sdot = np.einsum("mi,mij->mj", ka_hat, ghat)
    Fform = ka2[:, None, None] * np.einsum("mij,mik->mjk", ghat, ghat) - np.einsum("mj,mk->mjk", Sdot, Sdot)
    E = L**d * np.sum(Fform, axis=0)
    # Energy in cells of level n - 1: L^d of them per parent. In A': Ginv E Ginv, normalised so that lambda has the right size.
    # lambda := Ginv A'; ghat lambda is the field.
    En = Perp.T @ Ginv @ E @ Ginv @ Perp / P2
    return Min, En, P2


def grid(d):
    vals = [0.0, 0.02 * np.pi, np.pi / 8, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
    import itertools

    return [t for t in itertools.combinations_with_replacement(vals, d) if max(t) > 0]


def c_e(L, d, pts=None):
    best, where = np.inf, None
    for P in pts if pts is not None else grid(d):
        Min, _, P2 = forms(P, L, 1, d)
        ev = np.linalg.eigvalsh(0.5 * (Min + Min.T))[0]
        val = (ev - float(L) ** (d - 4)) / P2
        if val < best:
            best, where = val, P
    return best, where


def e1e2():
    ok = True
    print("E1", flush=True)
    vals = {}
    for L in (3, 5, 7, 11, 17):
        v, w = c_e(L, 4)
        vals[L] = v
        print(f" d=4 L={L}: c_e={v:.5f} at P/pi={tuple(round(x / np.pi, 3) for x in w)}, rss={lg.rss_gb():.2f}GB", flush=True)
        lg.guard()
    good = min(vals.values()) >= 0.05 and vals[17] >= 0.7 * vals[7]
    ok = ok and good
    print(f" E1: {good}", flush=True)
    print("E2", flush=True)
    worst = 0.0
    for P in grid(4)[::7]:
        Min, En, _ = forms(P, 3, 1, 4)
        worst = max(worst, float(np.max(np.abs(Min - En))))
    good0 = worst <= 1e-8
    ok = ok and good0
    print(f" control, n = 1: |Min - E| = {worst:.1e}: {good0}", flush=True)
    for L, n in ((3, 2), (3, 3), (5, 2)):
        low = np.inf
        for P in grid(4)[::7]:
            Min, _, _ = forms(P, L, 1, 4)
            _, En, _ = forms(P, L, n, 4)
            low = min(low, float(np.linalg.eigvalsh(0.5 * (En - Min + (En - Min).T))[0]))
        good = low >= -1e-8
        ok = ok and good
        print(f" L={L} n={n}: min eig (E_(n) - E_(1)) = {low:.5f}: {good}, rss={lg.rss_gb():.2f}GB", flush=True)
        lg.guard()
    return ok


def toy_excess(Theta, L):
    nc = Theta.shape[0]
    Fh = np.fft.fft2(Theta)
    e = 0.0
    for a in range(nc):
        for b in range(nc):
            if a == 0 and b == 0:
                continue
            P = (2 * np.pi * a / nc, 2 * np.pi * b / nc)
            P = tuple(((x + np.pi) % (2 * np.pi)) - np.pi for x in P)
            Min, _, _ = forms(P, L, 1, 2)
            e += (float(Min[0, 0]) - float(L) ** (2 - 4)) * abs(Fh[a, b]) ** 2 / nc**2
    return e


def e3():
    sv = load("sv", "hard-core--mapped_sector_value.py")
    nc = 16
    fib = sv.Fibre(nc)
    z0 = np.zeros((fib.N, fib.N))
    G1 = fib.G(z0, z0)
    # kappa from the uniform sectors, as in that check.
    kap = []
    for k in (1, 2, 3):
        Th = np.full((nc, nc), 2 * np.pi * k / nc**2)
        Ax, Ay = sv.links_from_flux(sv.fine_flux(Th))
        kap.append((Th[0, 0] ** 2, (fib.G(Ax, Ay) - G1) / sv.energy(Th)))
    kappa = float(np.polyfit([a for a, b in kap], [b for a, b in kap], 2)[-1])
    r1, r0 = {}, {}
    for n in (4, 6, 8, 10):
        for name, store, split in (("charged", r1, False), ("neutral", r0, True)):
            Th = sv.patch(nc, n, sign_split=split)
            Ax, Ay = sv.links_from_flux(sv.fine_flux(Th))
            Z = fib.G(Ax, Ay) - G1 - kappa * sv.energy(Th)
            e = toy_excess(Th, sv.L)
            store[n] = abs(Z) / e
            print(f"  n={n} {name}: Z={Z:+.4e} e={e:.4e} |Z|/e={abs(Z) / e:.5f} rss={lg.rss_gb():.2f}GB", flush=True)
            lg.guard()
    R1, R0 = max(r1.values()), max(r0.values())
    spread = max(r1.values()) / min(r1.values())
    good = R0 / 3 <= R1 <= 3 * R0 and spread <= 3
    print(f" E3: R_1={R1:.5f} R_0={R0:.5f} spread in n {spread:.3f}: {good}", flush=True)
    return good


def e4():
    ls = load("ls", "hard-core--mapped_lift_su2.py")
    ok = True
    Nc = 4
    pts = [
        (2 * np.pi * a / Nc, 2 * np.pi * b / Nc)
        for a in range(-1, 3)
        for b in range(-1, 3)
        if (a, b) != (0, 0)
    ]
    for L, tries in ((3, 12), (5, 4)):
        ce, _ = c_e(L, 2, pts)
        level = ls.Level(L, Nc)
        low = {}
        for seed in range(tries):
            rng = np.random.default_rng(500 + seed)
            modes = []
            for _ in range(int(rng.integers(1, 4))):
                Px, Py = rng.integers(0, Nc, 2)
                if Px == 0 and Py == 0:
                    Px = 1
                modes.append((int(Px), int(Py), [rng.standard_normal(3) for _ in range(2)], float(rng.uniform(0, 2 * np.pi))))
            for f in (0.02, 0.05, 0.1):
                Vp, A = ls.make_parent(Nc, modes, f)
                V, info = ls.solve(level, Vp, ls.initial_lift(level, A))
                if not (info["cres"] <= 1e-7 and info["pgrad"] <= 1e-3):
                    print(f"  L={L} seed={seed} f={f}: not converged, not used", flush=True)
                    continue
                fine = ls.grad_energy(V)
                par = ls.grad_energy(Vp)
                e = fine[2] - par[2] / L**2
                ratio = e / par[0]
                low[f] = min(low.get(f, np.inf), ratio)
                lg.guard()
        for f in low:
            good = low[f] >= 0.5 * ce
            ok = ok and good
            print(f" L={L} f={f}: smallest e/|grad' F'|^2 = {low[f]:.5f}, abelian c_e(2, L) on these momenta = {ce:.5f}: {good} rss={lg.rss_gb():.2f}GB", flush=True)
    return ok


def main():
    ok = e1e2()
    print("E3", flush=True)
    ok = e3() and ok
    print("E4", flush=True)
    ok = e4() and ok
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
