"""T3b: direct (no extrapolation) Zolotarev error for sign(x) on [k,1], computed at high precision.
Correction to t3: the recalled closed-form rate in t3 had K and K' swapped (it gave rates ~8/pole, wrong
direction in the k->1 limit).  This script computes the actual error of the Zolotarev-form approximant
   r(x) = d0 * x * prod_{l=1..n} (x^2 + c_{2l}) / (x^2 + c_{2l-1}),
   c_l = sn^2(l K'/(2n+1); k') / (1 - sn^2(l K'/(2n+1); k')),  K' = K(k'),  k' = sqrt(1-k^2)
(Chiu, Hsieh, Huang, Huang, hep-lat/0206007 form), d0 fixed by symmetric equioscillation,
error = max_{x in [k,1]} |1 - r(x)| evaluated on a dense log grid.  n = number of poles
(= auxiliary fields per site in the partial-fraction / continued-fraction realization).
"""
import mpmath as mp

mp.mp.dps = 130


def zolo_error(k, n, npts=1500):
    k = mp.mpf(k)
    kp = mp.sqrt(1 - k * k)
    Kp = mp.ellipk(kp**2)  # mpmath ellipk takes parameter m = k^2
    c = []
    for l in range(1, 2 * n + 1):
        u = l * Kp / (2 * n + 1)
        sn = mp.ellipfun('sn', u, m=kp**2)
        c.append(sn**2 / (1 - sn**2))
    # Chiu et al. form is for x in [1, sqrt(b)], b = 1/k^2, i.e. x in [1, 1/k] (lam scaled by lam_min).
    # (first run evaluated on [k,1] = wrong scale; kept as t3b_zolotarev_direct_WRONGSCALE.out)
    xs = [(1 / k) ** (mp.mpf(i) / (npts - 1)) for i in range(npts)]
    vals = []
    for x in xs:
        r = x
        for l in range(1, n + 1):
            r *= (x * x + c[2 * l - 1]) / (x * x + c[2 * l - 2])
        vals.append(r)
    lo, hi = min(vals), max(vals)
    d0 = 2 / (lo + hi)
    err = max(abs(1 - d0 * v) for v in vals)
    return err


if __name__ == "__main__":
    import math
    # kappa = lam_min/lam_max of |H_W| from t3 (free 4D, r=1): M=0.5 -> 0.5/7.5, M=1 -> 1/7, M=1.5 -> 0.5/6.5
    for M, k in ((0.5, 0.5 / 7.5), (1.0, 1 / 7), (1.5, 0.5 / 6.5)):
        print(f"M={M}  k={k:.4f}")
        prev = None
        for n in (4, 8, 12, 16, 20, 24, 28, 32, 40):
            e = zolo_error(k, n)
            le = float(mp.log10(e))
            rate = None if prev is None else (prev[1] - le) * math.log(10) / (n - prev[0])
            print(f"   n={n:3d}  max error = 1e{le:7.2f}" + ("" if rate is None else f"   local rate/pole = {rate:.3f}"))
            prev = (n, le)
