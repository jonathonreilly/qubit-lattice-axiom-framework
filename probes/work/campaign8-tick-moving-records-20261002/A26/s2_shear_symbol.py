"""A26 s2_shear_symbol: massless cone speeds of all four bands vs direction, under a uniform static shear
(a z-travelling TT wave's local action in the x-y plane), for three fixed couplings (supplied toy):
  BL  bond-length only: x-bonds x (1 - h_xx/2), y-bonds x (1 - h_yy/2)        [A23 D18]
  P2  period-2 staggered Peierls phases ~ h_xy (taste-graded, from s1_span)
  FR  frame rotation: x-block conjugated by R(beta) = S P(beta) S^dag, sin(2 beta) = h_xy
Metric prediction (inverse metric g^ij = delta - h, first order): v(phi)^2 = v0^2 (1 - h_xx c^2 - h_yy s^2 - 2 h_xy c s).
Fit per band: v^2/v0^2 = a + b cos(2phi) + c sin(2phi); metric: b = -(h_xx - h_yy)/2, c = -h_xy (times dose factor for BL).
Also: conformal h = 2U delta with lapse N = 1-U: cone speed vs the metric speed N/(1+U) (gamma = 1)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from walk2d import cycle, quasi, KSTAR

th = 0.3
dq = 1e-4
phis = np.linspace(0, np.pi, 24, endpoint=False)


def speeds(**kw):
    out = []
    for ph in phis:
        K = KSTAR + dq * np.array([np.cos(ph), np.sin(ph)])
        w = quasi(cycle(K, th=th, **kw))
        out.append(np.sort(np.abs(w)) / dq)          # 4 slopes (2 positive-band, 2 negative-band magnitudes)
    return np.array(out)                              # (nphi, 4)


def fit(v2):
    A = np.column_stack([np.ones_like(phis), np.cos(2 * phis), np.sin(2 * phis)])
    coef, res, *_ = np.linalg.lstsq(A, v2, rcond=None)
    resid = np.abs(A @ coef - v2).max()
    return coef, resid


v0 = speeds()
print("flat cone: all 4 slopes / sin(th): min %.10f max %.10f" % ((v0 / np.sin(th)).min(), (v0 / np.sin(th)).max()))
dose = th / np.tan(th)                                # d ln sin(th e)/d e at e = 1
for h in (0.02, 0.05):
    print("--- shear amplitude h = %.2f   (th = %.2f, dose factor th cot th = %.4f)" % (h, th, dose))
    cases = [
        ("plus  h_xx=-h_yy=h, BL", dict(ex=1 - h / 2, ey=1 + h / 2), (-h, 0.0), dose),
        ("cross h_xy=h,       BL", dict(), (0.0, -h), dose),
        ("cross h_xy=h,       P2", dict(imx=-h / 2, imy=-h / 2), (0.0, -h), None),
        ("cross h_xy=h,       FR", dict(beta=0.5 * np.arcsin(h)), (0.0, -h), 1.0),
        ("plus+cross,    BL + FR", dict(ex=1 - h / 2, ey=1 + h / 2, beta=0.5 * np.arcsin(h)), (-h, -h), None),
    ]
    for name, kw, (bm, cm), df in cases:
        v = speeds(**kw)
        rows = []
        for band in range(4):
            coef, resid = fit((v[:, band] / np.sin(th)) ** 2)
            rows.append((coef, resid))
        bs = [r[0][1] for r in rows]; cs = [r[0][2] for r in rows]; rs = max(r[1] for r in rows)
        pred = "" if df is None else "  metric x dose: b=%+.5f c=%+.5f" % (bm * df, cm * df)
        print("   %-24s per-band b: %s  c: %s  (fit resid %.1e)%s" % (
            name, np.array2string(np.array(bs), precision=5, sign='+'), np.array2string(np.array(cs), precision=5, sign='+'),
            rs, pred))
    # explicit diagonal speeds for the cross shear
    i45, i135 = np.argmin(np.abs(phis - np.pi / 4)), np.argmin(np.abs(phis - 3 * np.pi / 4))
    for name, kw in (("BL", dict()), ("P2", dict(imx=-h / 2, imy=-h / 2)), ("FR", dict(beta=0.5 * np.arcsin(h)))):
        v = speeds(**kw) / np.sin(th)
        print("   cross h_xy=%.2f %s: v(45)/v0 = %s ; v(135)/v0 = %s ; metric %.5f / %.5f" % (
            h, name, np.array2string(v[i45], precision=5), np.array2string(v[i135], precision=5),
            np.sqrt(1 - h), np.sqrt(1 + h)))

print("--- conformal field h_ij = 2U delta, lapse N = 1-U, field coupling (bond factor N_b e_b, e_b = 1-U)")
for U in (0.01, 0.05):
    for name, kw in (("field (N e)", dict(N=1 - U, ex=1 - U, ey=1 - U)), ("lapse only", dict(N=1 - U)),
                     ("frame only", dict(ex=1 - U, ey=1 - U))):
        v = speeds(**kw)[:, 0]
        # metric speed (small dose): N * e ; dose-exact: sin(th N e)/sin(th)
        Ne = (1 - U) ** 2 if name.startswith("field") else (1 - U)
        print("   U=%.2f %-12s: cone speed/v0 = %.8f (isotropy spread %.1e); sin(th N e)/sin th = %.8f; "
              "effective (1+gamma) = -dln v/dU / (th cot th) = %.4f"
              % (U, name, v.mean() / np.sin(th), v.std() / v.mean(), np.sin(th * Ne) / np.sin(th),
                 -np.log(v.mean() / np.sin(th)) / U / dose))
