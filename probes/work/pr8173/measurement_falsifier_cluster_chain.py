#!/usr/bin/env python3
"""J:falsifier:PR8173 - block 29 (PR #8173), the Falsifiers section's measurement bullet: "For the measurement: a normalization outside
[(m^2/3)^2, 1] beyond its scatter, a sum-rule violation in a field beyond the statistical error, or a real-space constant differing from
the structure-factor constant."  Implemented with a chain disjoint from the note's (heat-bath checkerboard; refuter: single-site
Metropolis): embedded Swendsen-Wang cluster moves (random reflection axis r; bonds 1 - exp(-2 beta a_x a_y) on aligned projections
a = s.r; each cluster flipped by a heat-bath choice with its field weight exp(beta h sum_C s^3)) alternated with overrelaxation sweeps
(reflection of each spin about its local field, checkerboard).  Errors: batch means (20 batches).  Beyond the note's sizes: the sum rule
on L = 4, 8, 16, 24 at beta = 0.5, 1, 1.5, 3 and h = 0.05, 0.1, 0.2, 0.5 (the note: L = 16, beta = 1.5, h = 0.05, 0.1, 0.2, one run each);
the normalization on L = 16, 24, 32, 48 at beta = 0.8, 1, 1.5, 2, 3 (the note: L = 16, 24, 32).

Objects (the note's declared objects).  Sphere static law on T_L = (Z/L)^3, weight exp(beta sum_bonds s_x.s_y + beta h sum_x s_x^3).
m^ = N^{-1} sum s_x; u = m^/|m^|; transverse components in the instantaneous frame; S_perp(k) = <|s^perp^(k)|^2>/2 per component,
s^(k) = N^{-1/2} sum_x e^{-ik.x} s_x; c(beta, k) = beta E(k) S_perp(k), E(k) = 2 sum_j (1 - cos k_j), k = 2 pi n/L along an axis
(averaged over the three axes); T(r) = <s_0^perp . s_{r e}^perp>/2; G_L(r) = N^{-1} sum_{k != 0} e^{ik.r}/E(k); c_real(r) = beta T(r)/G_L(r).
HIT criteria (stated before the run): (i) |beta h N <((m^1)^2 + (m^2)^2)/2> - <m^3>| > 5 sigma at any (L, beta, h) [T2 is exact];
(ii) c(beta, k) > 1 + 5 sigma or < (m^2/3)^2 - 5 sigma for any n >= 1 at any (L, beta);
(iii) |mean_{r=1..4} c_real(r) - mean_{n=2..8} c(beta, k_n)| > 0.05 + 5 sigma at any (L, beta).
INFO: the note's table values against these measurements (z-scores with this run's sigma).
"""
import sys
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

SEED = 8173
QUICK = 20 if "--quick" in sys.argv else 1      # smoke-test divisor for the step counts (the logged run uses none)
NOTE_TABLE = {   # the note's executed table: (L, beta) -> (m, c for n = 1..8)
    (16, 0.8): (0.537, [0.77, 0.92, 0.92, 0.92, 0.91, 0.95, 0.90, 0.89]),
    (16, 1.0): (0.688, [0.86, 0.87, 0.93, 0.91, 0.92, 0.92, 0.89, 0.95]),
    (16, 1.5): (0.817, [0.93, 0.96, 0.93, 0.99, 0.94, 0.96, 0.92, 1.01]),
    (16, 2.0): (0.868, [0.95, 0.96, 0.97, 0.96, 0.91, 0.97, 0.93, 0.98]),
    (16, 3.0): (0.915, [0.96, 0.95, 0.94, 0.99, 0.98, 1.00, 0.99, 0.98]),
    (24, 0.8): (0.525, [0.92, 0.86, 0.91, 0.91, 0.90, 0.90, 0.90, 0.93]),
    (24, 1.0): (0.681, [0.98, 0.86, 0.89, 0.91, 0.89, 0.88, 0.90, 0.94]),
    (24, 1.5): (0.813, [1.05, 0.90, 0.92, 0.91, 0.95, 0.94, 0.92, 0.96]),
    (24, 2.0): (0.866, [0.97, 0.94, 0.92, 1.01, 0.98, 0.98, 0.94, 0.92]),
    (32, 1.0): (0.678, [0.65, 0.88, 0.97, 0.93, 0.96, 0.90, 0.91, 0.94]),
    (32, 1.5): (0.811, [0.92, 0.97, 0.88, 0.88, 0.96, 0.93, 0.93, 0.98]),
}


class Lattice:
    def __init__(self, L):
        self.L, self.N = L, L ** 3
        idx = np.arange(self.N).reshape(L, L, L)
        self.nb = [np.roll(idx, -1, ax).ravel() for ax in range(3)]
        self.par = np.indices((L, L, L)).sum(0) % 2


def nbsum(s):
    return sum(np.roll(s, sh, ax) for ax in range(3) for sh in (1, -1))


def overrelax(s, lat, h):
    for p in (0, 1):
        H = nbsum(s)
        H[..., 2] += h
        n = np.linalg.norm(H, axis=-1, keepdims=True)
        Hn = H / np.maximum(n, 1e-300)
        refl = 2 * (s * Hn).sum(-1, keepdims=True) * Hn - s
        s = np.where((lat.par == p)[..., None], refl, s)
    return s


def sw_step(s, rng, beta, h, lat):
    r = rng.normal(size=3)
    r /= np.linalg.norm(r)
    a = (s @ r).ravel()
    rows, cols = [], []
    for ax in range(3):
        prod = a * a[lat.nb[ax]]
        p = np.where(prod > 0, -np.expm1(-2 * beta * np.maximum(prod, 0)), 0.0)
        act = rng.random(lat.N) < p
        rows.append(np.nonzero(act)[0])
        cols.append(lat.nb[ax][act])
    rows, cols = np.concatenate(rows), np.concatenate(cols)
    g = coo_matrix((np.ones(len(rows), dtype=np.int8), (rows, cols)), shape=(lat.N, lat.N))
    nc, lab = connected_components(g, directed=False)
    A = np.bincount(lab, weights=a, minlength=nc)
    pf = 1.0 / (1.0 + np.exp(np.clip(2 * beta * h * r[2] * A, -700, 700)))   # heat-bath: P(flip) = w_flip/(w_flip + w_stay)
    f = (rng.random(nc) < pf)[lab]
    sf = s.reshape(lat.N, 3)
    sf = np.where(f[:, None], sf - 2 * a[:, None] * r[None, :], sf)
    return sf.reshape(s.shape)


def batch(x, nb=20):
    x = np.asarray(x, dtype=float)
    m = len(x) // nb
    b = x[:m * nb].reshape(nb, m).mean(1)
    return b.mean(), b.std(ddof=1) / np.sqrt(nb)


def sum_rule(rng):
    print("== (i) the transverse sum rule in a field (T2, exact): beta h N <((m^1)^2 + (m^2)^2)/2> against <m^3>")
    rows = []
    plan = {L: (a // QUICK, b // QUICK) for L, (a, b) in {4: (4000, 40000), 8: (4000, 40000), 16: (3000, 20000), 24: (2000, 10000)}.items()}
    for L, (therm, steps) in plan.items():
        lat = Lattice(L)
        for beta in (0.5, 1.0, 1.5, 3.0):
            for h in (0.05, 0.1, 0.2, 0.5):
                t0 = time.time()
                s = np.zeros((L, L, L, 3))
                s[..., 2] = 1
                D, X, Y = [], [], []
                for it in range(therm + steps):
                    s = sw_step(s, rng, beta, h, lat)
                    s = overrelax(s, lat, h)
                    if it >= therm:
                        M = s.mean((0, 1, 2))
                        x = beta * h * lat.N * (M[0] ** 2 + M[1] ** 2) / 2
                        X.append(x)
                        Y.append(M[2])
                        D.append(x - M[2])
                (dm, ds), (xm, _), (ym, _) = batch(D), batch(X), batch(Y)
                z = dm / ds if ds > 0 else 0.0
                rows.append((L, beta, h, xm, ym, dm, ds, z))
                print(f"[i] L={L:2d} beta={beta:3.1f} h={h:4.2f}: beta h N<(m1^2+m2^2)/2> = {xm:.5f}, <m3> = {ym:.5f}, difference {dm:+.5f} "
                      f"+- {ds:.5f} (z = {z:+.2f}; {steps} steps, {time.time() - t0:.0f}s)")
    return rows


def kernel(rng):
    print("== (ii)-(iii) the normalization c(beta, k) = beta E(k) S_perp(k) (k = 2 pi n/L along the axes, n = 1..8) and the real-space "
          "constant beta T(r)/G_L(r), r = 1..4")
    out = []
    plan = {L: (a // QUICK, b // QUICK) for L, (a, b) in {16: (1000, 12000), 24: (1000, 8000), 32: (800, 6000), 48: (600, 3000)}.items()}
    for L, (therm, steps) in plan.items():
        lat = Lattice(L)
        kx = 2 * np.pi * np.fft.fftfreq(L)
        K = np.meshgrid(kx, kx, kx, indexing="ij")
        E3 = 2 * (3 - np.cos(K[0]) - np.cos(K[1]) - np.cos(K[2]))
        invE = np.where(E3 > 1e-12, 1 / np.where(E3 > 1e-12, E3, 1), 0.0)
        G = np.real(np.fft.ifftn(invE))                   # G_L(r) = N^{-1} sum_{k != 0} e^{ik.r}/E(k)
        GL = np.array([(G[r, 0, 0] + G[0, r, 0] + G[0, 0, r]) / 3 for r in range(1, 5)])
        ns = np.arange(1, 9)
        Ek = 2 * (1 - np.cos(2 * np.pi * ns / L))
        for beta in (0.8, 1.0, 1.5, 2.0, 3.0):
            t0 = time.time()
            s = np.zeros((L, L, L, 3))
            s[..., 2] = 1
            ms, Sk, Tr = [], [], []
            for it in range(therm + steps):
                s = sw_step(s, rng, beta, 0.0, lat)
                s = overrelax(s, lat, 0.0)
                if it >= therm and it % 2 == 0:
                    M = s.mean((0, 1, 2))
                    m = np.linalg.norm(M)
                    u = M / m
                    a0 = np.array([1.0, 0, 0]) if abs(u[0]) < 0.9 else np.array([0, 1.0, 0])
                    e1 = a0 - (a0 @ u) * u
                    e1 /= np.linalg.norm(e1)
                    e2 = np.cross(u, e1)
                    t1, t2 = s @ e1, s @ e2
                    acc = np.zeros(8)
                    for ax in range(3):
                        other = tuple(a for a in range(3) if a != ax)
                        F1 = np.fft.fft(t1.sum(axis=other))
                        F2 = np.fft.fft(t2.sum(axis=other))
                        acc += (np.abs(F1[ns]) ** 2 + np.abs(F2[ns]) ** 2) / (2 * lat.N)
                    Sk.append(acc / 3)
                    tr = np.zeros(4)
                    for r in range(1, 5):
                        for ax in range(3):
                            tr[r - 1] += ((t1 * np.roll(t1, r, ax)).mean() + (t2 * np.roll(t2, r, ax)).mean()) / 2
                    Tr.append(tr / 3)
                    ms.append(m)
            Sk, Tr = np.array(Sk), np.array(Tr)
            mm, msd = batch(ms)
            c = [batch(beta * Ek[i] * Sk[:, i]) for i in range(8)]
            cr = [batch(beta * Tr[:, i] / GL[i]) for i in range(4)]
            c_sf_mean = batch(beta * (Sk[:, 1:] * Ek[None, 1:]).mean(1))
            c_re_mean = batch(beta * (Tr / GL[None, :]).mean(1))
            lb = (mm * mm / 3) ** 2
            out.append(dict(L=L, beta=beta, m=(mm, msd), c=c, cr=cr, csf=c_sf_mean, cre=c_re_mean, lb=lb))
            print(f"[ii] L={L:2d} beta={beta:3.1f}: m = {mm:.4f} +- {msd:.4f}, (m^2/3)^2 = {lb:.4f}; c(n=1..8) = "
                  + " ".join(f"{v:.3f}({100 * e:.0f})" for v, e in c) + f"   ({len(Sk)} measurements, {time.time() - t0:.0f}s)")
            print(f"[iii] L={L:2d} beta={beta:3.1f}: c_real(r=1..4) = " + " ".join(f"{v:.3f}({100 * e:.0f})" for v, e in cr)
                  + f"; mean c_real = {c_re_mean[0]:.4f} +- {c_re_mean[1]:.4f}; mean c(n=2..8) = {c_sf_mean[0]:.4f} +- {c_sf_mean[1]:.4f}")
    return out


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    sr = sum_rule(rng)
    kr = kernel(rng)
    hits = []
    zmax = max(sr, key=lambda r: abs(r[7]))
    for L, beta, h, xm, ym, dm, ds, z in sr:
        if abs(z) > 5:
            hits.append(f"HIT: (i) sum rule violated beyond 5 sigma at L={L}, beta={beta}, h={h}: {xm:.5f} vs {ym:.5f} (z = {z:+.2f})")
    over, under, nsig = [], [], 0
    for r in kr:
        for n, (v, e) in enumerate(r["c"], start=1):
            if v > 1 + 5 * e:
                over.append((r["L"], r["beta"], n, v, e))
            if v < r["lb"] - 5 * e:
                under.append((r["L"], r["beta"], n, v, e))
    for L, beta, n, v, e in over:
        hits.append(f"HIT: (ii) c(beta, k) above the infrared bound 1 beyond 5 sigma at L={L}, beta={beta}, n={n}: {v:.4f} +- {e:.4f}")
    for L, beta, n, v, e in under:
        hits.append(f"HIT: (ii) c(beta, k) below (m^2/3)^2 beyond 5 sigma at L={L}, beta={beta}, n={n}: {v:.4f} +- {e:.4f}")
    diffs = []
    for r in kr:
        d = r["cre"][0] - r["csf"][0]
        e = np.hypot(r["cre"][1], r["csf"][1])
        diffs.append((r["L"], r["beta"], d, e))
        if abs(d) > 0.05 + 5 * e:
            hits.append(f"HIT: (iii) real-space constant {r['cre'][0]:.4f} vs structure-factor constant {r['csf'][0]:.4f} at L={r['L']}, "
                        f"beta={r['beta']} (difference {d:+.4f} +- {e:.4f})")
    # INFO: the note's table against this run
    zs = []
    for r in kr:
        key = (r["L"], r["beta"])
        if key in NOTE_TABLE:
            m_note, c_note = NOTE_TABLE[key]
            zc = [(c_note[i] - r["c"][i][0]) / r["c"][i][1] for i in range(8)]
            zs.extend((abs(z), key, i + 1, c_note[i], r["c"][i][0], r["c"][i][1]) for i, z in enumerate(zc))
            print(f"[INFO] note table at L={key[0]}, beta={key[1]}: m {m_note:.3f} vs {r['m'][0]:.4f}; c(n) note - this run in sigma: "
                  + " ".join(f"{z:+.1f}" for z in zc))
    big = sorted(zs, reverse=True)[:5]
    print("[INFO] largest deviations of the note's table from this run: " + "; ".join(
        f"L={k[0]} beta={k[1]} n={n}: note {cn:.2f} vs {v:.3f}+-{e:.3f} ({z:.1f} sigma)" for z, k, n, cn, v, e in big))
    csf_all = [v for r in kr for v, e in r["c"][1:]]
    print(f"[INFO] this run: c(beta, k) for n = 2..8 over all (L, beta): {min(csf_all):.3f} .. {max(csf_all):.3f} (note: 0.86-0.98, "
          f"with values up to 1.01 in its table)")
    for h in hits:
        print(h)
    print(f"[time] {time.time() - t0:.0f}s")
    print(f"SUMMARY: (i) sum rule at {len(sr)} (L, beta, h) points: max |z| = {abs(zmax[7]):.2f} at L={zmax[0]}, beta={zmax[1]}, h={zmax[2]} "
          f"({sum(1 for r in sr if abs(r[7]) > 5)} beyond 5 sigma); (ii) c(beta, k) at {len(kr)} (L, beta) x 8 modes: {len(over)} above 1 and "
          f"{len(under)} below (m^2/3)^2 beyond 5 sigma, n>=2 range {min(csf_all):.3f}..{max(csf_all):.3f}; (iii) real-space vs structure-factor "
          f"constant: max |difference| {max(abs(d) for _, _, d, _ in diffs):.4f}; falsifier {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
