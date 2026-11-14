#!/usr/bin/env python3
"""GUIDE for FINISH row 963 (gap-rotgeom-opus): sector thermal sums of a free massive scalar.

Model: one free real scalar boson of mass m on the periodic cube of side L (continuum dispersion
omega_k = sqrt(m^2 + (2 pi k / L)^2), k in Z^3 with |k_i| <= K), Euclidean time tau = 1, x = m.
Vacuum-normalised Fock traces (bosons):
    log Tr(V_R e^{i theta.P} e^{-H}) = sum_{n>=1} (1/n) sum_{k: R^n k = k} e^{i theta.(S_n k)} e^{-n omega_k},
    S_n = 1 + R + ... + R^{n-1}.
Outputs per x:
    S   = Tr e^{-H} - 1                          (full thermal sum, the seed),
    S0  = Tr(P_{p=0} e^{-H}) - 1                 (zero momentum sector),
    S1  = Tr(P_{p=0} P_{A1} e^{-H}) - 1          (trivial sector of the space group Z^3 x| O_h),
    lr  = log Tr(V_R e^{-H}) / log Tr e^{-H}     (R a quarter turn about an axis).
P_{p=0} is the mean over an M^3 grid of theta in (2 pi / M) Z^3 (aliasing only from total momentum in M Z^3).
The A1 projection is (1/48) sum over O_h, summed by conjugacy class.
A run can refute or guide; it proves nothing.  Usage: sector_sums.py M x1,x2,...
"""
import itertools
import resource
import sys

import numpy as np

L = 24.0
K = 60


def rss_check():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on macOS
    if rss > 2.0e9:
        sys.exit("RSS above 2 GB: stopping")


def oh_classes():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            r = np.zeros((3, 3), dtype=np.int64)
            for i in range(3):
                r[i, perm[i]] = signs[i]
            mats.append(r)
    seen = set()
    classes = []
    for r in mats:
        if r.tobytes() in seen:
            continue
        cls = {}
        for g in mats:
            c = g @ r @ g.T
            cls[c.tobytes()] = c
        seen.update(cls.keys())
        classes.append((r, len(cls)))
    assert sum(c for _, c in classes) == 48 and len(classes) == 10
    return classes


def log_mean_exp(f):
    a = f.real.max()
    s = np.exp(f - a).sum() / f.size
    return a + np.log(s.real), abs(s.imag) / abs(s.real)


def run(m_grid, xs):
    r1 = np.arange(-K, K + 1)
    k1, k2, k3 = np.meshgrid(r1, r1, r1, indexing="ij")
    kv = np.stack([k1.ravel(), k2.ravel(), k3.ravel()], axis=1)
    del k1, k2, k3
    p2 = (2.0 * np.pi / L) ** 2 * (kv ** 2).sum(axis=1)
    classes = oh_classes()
    quarter = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=np.int64)
    eye = np.eye(3, dtype=np.int64)
    m3 = m_grid ** 3
    print("# L=%g K=%d M=%d; columns: x logZ S S0 S1 lr(quarter) maxImagRel" % (L, K, m_grid))
    for x in xs:
        om = np.sqrt(x * x + p2)
        nmax = int(np.ceil(34.0 / x))
        logz_cls = []
        lr = None
        logz_full = None
        imag_max = 0.0
        if x < 1.0:
            # dense regime: only the theta = 0 traces are used (criterion C4); the p = 0 grid would alias
            logz_full = sum(np.exp(-n * om).sum() / n for n in range(1, nmax + 1))
            logz_p0 = float("nan")
            logz_cls = [(float("nan"), 48)]
        for rmat, size in (classes if x >= 1.0 else []):
            acc = np.zeros(m3, dtype=np.float64)
            rn = eye.copy()
            sn = np.zeros((3, 3), dtype=np.int64)
            for n in range(1, nmax + 1):
                sn = sn + rn          # S_n = 1 + R + ... + R^{n-1}
                rn = rn @ rmat        # R^n
                if np.array_equal(rn, eye):
                    ks = kv
                    w = np.exp(-n * om)
                else:
                    mask = np.all(kv @ rn.T == kv, axis=1)
                    if not mask.any():
                        continue
                    ks = kv[mask]
                    w = np.exp(-n * om[mask])
                q = (ks @ sn.T) % m_grid
                flat = (q[:, 0] * m_grid + q[:, 1]) * m_grid + q[:, 2]
                acc += np.bincount(flat, weights=w / n, minlength=m3)
                rss_check()
            f = m3 * np.fft.ifftn(acc.reshape(m_grid, m_grid, m_grid))
            lz0, im = log_mean_exp(f)
            imag_max = max(imag_max, im)
            logz_cls.append((lz0, size))
            if np.array_equal(rmat, eye):
                logz_full = f[0, 0, 0].real
                logz_p0 = lz0
        # quarter turn twisted trace at theta = 0
        lz_q = 0.0
        rn = eye.copy()
        for n in range(1, nmax + 1):
            rn = rn @ quarter
            if np.array_equal(rn, eye):
                lz_q += np.exp(-n * om).sum() / n
            else:
                mask = np.all(kv @ rn.T == kv, axis=1)
                lz_q += np.exp(-n * om[mask]).sum() / n
        lr = lz_q / logz_full
        if x >= 1.0:
            mx = max(v for v, _ in logz_cls)
            lz1 = mx + np.log(sum(s * np.exp(v - mx) for v, s in logz_cls) / 48.0)
        else:
            lz1 = float("nan")
        s_full = np.expm1(logz_full)
        s0 = np.expm1(logz_p0)
        s1 = np.expm1(lz1)
        print("%6.2f %12.5e %12.5e %12.5e %12.5e %10.5f %8.1e" % (x, logz_full, s_full, s0, s1, lr, imag_max))
        sys.stdout.flush()


if __name__ == "__main__":
    mg = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    xv = [float(v) for v in sys.argv[2].split(",")] if len(sys.argv) > 2 else [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
    run(mg, xv)
