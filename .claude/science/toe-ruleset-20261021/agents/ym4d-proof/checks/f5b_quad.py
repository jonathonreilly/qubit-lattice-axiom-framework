#!/usr/bin/env python3
"""f5b (criteria checks/f5b_criteria.md, written before this script): f5's class integrand (imported unchanged) with a
clustering periodic quadrature map P = t - alpha sin(l t)/l, the P3/P4 reflection and swap symmetries, and h = 3e-4."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys, time, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f5_cov_kernel as F

AUDIT_TIMEOUT_SEC = 7200
T0 = time.time()
ALPHA = 0.65
NP_ = NF_ = 0


def report(name, ok, msg):
    global NP_, NF_
    NP_ += bool(ok); NF_ += (not ok)
    print(f"[{name}] {'PASS' if ok else 'FAIL'} :: {msg}", flush=True)


def nodes(ell, n):
    t = (np.arange(n) + 0.5) * (2 * np.pi / ell) / n - np.pi / ell
    P = t - ALPHA * np.sin(ell * t) / ell
    w = 1 - ALPHA * np.cos(ell * t)
    return P, w / w.sum()


def grid(ell, n):
    """points and weights (normalised to 1) using P3,P4 >= 0 and P3 <= P4 with multiplicities."""
    P, w = nodes(ell, n)
    pos = np.where(P > 0)[0]
    pts, wts = [], []
    for i in range(n):
        for j in range(n):
            for a in pos:
                for b in pos:
                    if P[a] > P[b]:
                        continue
                    mult = 4 * (1 if a == b else 2)
                    pts.append((P[i], P[j], P[a], P[b])); wts.append(w[i] * w[j] * w[a] * w[b] * mult)
    wts = np.array(wts)
    return np.array(pts), wts / wts.sum()


def T_w(pts, wts, k1, ell, kappas, batch=8):
    acc = {kap: [0j, 0j] for kap in kappas}
    for i in range(0, len(pts), batch):
        r = F.class_integrand(pts[i:i + batch], k1, 0, 1, ell, kappas)
        ww = wts[i:i + batch]
        for kap in kappas:
            acc[kap][0] += (ww * r[kap][0]).sum(); acc[kap][1] += (ww * r[kap][1]).sum()
    return {kap: (acc[kap][0] * ell ** -4, acc[kap][1] * ell ** -4) for kap in kappas}


def cgam(ell, kcs, n, h=3e-4):
    pts, wts = grid(ell, n)
    kappas = [kc * ell ** 2 for kc in kcs]
    v = {s: T_w(pts, wts, [s[0] * h, s[1] * h, 0, 0], ell, kappas) for s in [(1, 1), (1, -1), (-1, 1), (-1, -1)]}
    out = {}
    for kc, kap in zip(kcs, kappas):
        res = []
        for part in (0, 1):
            d = (v[(1, 1)][kap][part] - v[(1, -1)][kap][part] - v[(-1, 1)][kap][part] + v[(-1, -1)][kap][part]) / (4 * h * h)
            res.append(-d.real / 2)
        out[kc] = tuple(res)
    return out


def main():
    print("f5b: f5 class integrand, clustered symmetric quadrature; criteria checks/f5b_criteria.md", flush=True)
    rng = np.random.default_rng(11)
    Ps = rng.uniform(-np.pi / 5, np.pi / 5, (5, 4))
    k1 = [1e-3, 2e-3, 0, 0]
    base = F.class_integrand(Ps, k1, 0, 1, 5, [25.0])[25.0][0]
    worst = 0
    for R in (lambda P: P * np.array([1, 1, -1, 1]), lambda P: P * np.array([1, 1, 1, -1]), lambda P: P[:, [0, 1, 3, 2]]):
        fr = F.class_integrand(R(Ps), k1, 0, 1, 5, [25.0])[25.0][0]
        worst = max(worst, np.max(np.abs(fr - base) / np.abs(base)))
    report("S", worst <= 1e-12, f"max relative symmetry defect {worst:.1e}")
    kcs = [0.25, 1.0, 4.0]
    c10 = cgam(5, kcs, 10); c14 = cgam(5, kcs, 14)
    okC = all(abs(c10[kc][0] - c14[kc][0]) <= 1e-5 * abs(c14[kc][0]) for kc in kcs)
    report("C'", okC, "; ".join(f"kc={kc}: n=10 {c10[kc][0]:.9f}, n=14 {c14[kc][0]:.9f}, rel {abs(c10[kc][0]-c14[kc][0])/abs(c14[kc][0]):.1e}" for kc in kcs))
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    ch = cgam(5, [1.0], 12, 3e-4)[1.0][0]; c2h = cgam(5, [1.0], 12, 6e-4)[1.0][0]
    err = abs(ch - c2h) / 3
    report("D'", err <= 1e-6 * abs(ch), f"h=3e-4 {ch:.10f}, h=6e-4 {c2h:.10f}, Richardson error {err:.1e} (rel {err/abs(ch):.1e})")
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    ells = [3, 5, 7, 9, 11, 13]
    tab = {}
    for el in ells:
        tab[el] = cgam(el, kcs, 12)
        print(f"   l={el}: " + ", ".join(f"kc={kc}: c={tab[el][kc][0]:.8f} cM={tab[el][kc][1]:.8f} cK={tab[el][kc][0]-tab[el][kc][1]:.8f}" for kc in kcs)
              + f"  [t={time.time()-T0:.0f}s]", flush=True)
    t = 48 * np.pi ** 2
    sl = lambda f, a, b: (f(b) - f(a)) / np.log(b / a) * t
    okE = okG = True; last = {}
    for kc in kcs:
        sT = [sl(lambda e: tab[e][kc][0], a, b) for a, b in zip(ells[:-1], ells[1:])]
        sM = [sl(lambda e: tab[e][kc][1], a, b) for a, b in zip(ells[:-1], ells[1:])]
        sK = [sl(lambda e: tab[e][kc][0] - tab[e][kc][1], a, b) for a, b in zip(ells[:-1], ells[1:])]
        print(f"   kc={kc}: slope x 48pi^2 total {', '.join(f'{x:.4f}' for x in sT)}; M-only {', '.join(f'{x:.4f}' for x in sM)}; kernel-vertex {', '.join(f'{x:.4f}' for x in sK)}", flush=True)
        dev = [abs(x - 1) for x in sT]; mids = [np.sqrt(a * b) for a, b in zip(ells[:-1], ells[1:])]
        print(f"   [info] kc={kc}: |slope-1| * l_mid^2 = {', '.join(f'{d*m*m:.3f}' for d, m in zip(dev, mids))}", flush=True)
        okE &= abs(sT[-1] - 1) <= 0.03
        okG &= abs(sK[-1]) <= 0.05 and abs(sK[-1]) <= abs(sK[2])
        last[kc] = sT[-1]
    report("E'", okE, "slope at (11,13) x 48pi^2: " + ", ".join(f"kc={kc}: {last[kc]:.4f}" for kc in kcs))
    spread = max(last.values()) - min(last.values())
    report("F'", spread <= 0.03, f"kappa spread at (11,13) = {spread:.4f} x 1/(48pi^2)")
    report("G'", okG, "kernel-vertex slopes printed above")
    print("   [info] constants c(13) - log(13)/(48pi^2): " + ", ".join(f"kc={kc}: {tab[13][kc][0]-np.log(13)/t:.6f}" for kc in kcs))
    print(f"f5b done: PASS={NP_} FAIL={NF_}; wall {time.time()-T0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
