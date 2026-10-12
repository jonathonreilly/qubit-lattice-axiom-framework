"""Self-test of t1_loop.coeffs against the COMPARATOR formula of Collins et al. PRL 93 191301 (2004),
appendix eq. (A.2): fermion propagator x f(|k|/Lambda) =>
  xi = g^2/(6 pi^2) [1 + 2 int_0^inf x f'(x)^2 dx],  c_phi -> 1 + xi/4.
For f(x) = exp(-x^2/2): int x f'^2 = 1/2, so dc_phi = g^2/(12 pi^2) = (4/3) g^2/16pi^2.
Continuum R^3 quadrature in spherical coordinates; IR masses m (both species) -> 0.
Also prints dc_psi and Delta for this (fermion-only) Collins regulator, and for the regulator on both lines.
"""
import numpy as np
from t1_loop import coeffs, selftest_q0



def sph_grid(nr, nt, nph, qmax, qmin):
    # radial: Gauss-Legendre in log q
    x, wx = np.polynomial.legendre.leggauss(nr)
    lq = np.log(qmin) + (x + 1) / 2 * (np.log(qmax) - np.log(qmin))
    q = np.exp(lq); wq = wx / 2 * (np.log(qmax) - np.log(qmin)) * q  # dq
    ct, wct = np.polynomial.legendre.leggauss(nt)
    ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph; wph = np.full(nph, 2 * np.pi / nph)
    Q, CT, PH = np.meshgrid(q, ct, ph, indexing="ij")
    W = (wq[:, None, None] * q[:, None, None] ** 2) * wct[None, :, None] * wph[None, None, :] / (2 * np.pi) ** 3
    st = np.sqrt(1 - CT ** 2)
    qv = np.stack([Q * st * np.cos(PH), Q * st * np.sin(PH), Q * CT])
    return qv, W


def run(m, Lam=1.0, both=False):
    qv, W = sph_grid(400, 48, 48, 12 * Lam, 1e-4 * m)
    r2 = (qv ** 2).sum(0)
    f = np.exp(-r2 / (2 * Lam ** 2))
    df = -qv[0] / Lam ** 2 * f
    d2f = (-1 / Lam ** 2 + qv[0] ** 2 / Lam ** 4) * f
    one, zero = np.ones_like(r2), np.zeros_like(r2)
    dS = np.stack([one, zero, zero]); d2S = np.zeros_like(qv)
    F = dict(S=qv, M=m * one, dS=dS, d2S=d2S, dM=zero, d2M=zero, fF=f, dfF=df, d2fF=d2f)
    if both:
        Bd = dict(w2=m * m + r2, dw2=2 * qv[0], fB=f, dfB=df)
    else:
        Bd = dict(w2=m * m + r2, dw2=2 * qv[0], fB=one, dfB=zero)
    return coeffs(W, F, Bd)


if __name__ == "__main__":
    print("q0 closed forms: worst rel err", selftest_q0())
    k = 16 * np.pi ** 2
    print("Collins target: 16pi^2 dc_phi = 4/3 =", 4 / 3)
    for both in (False, True):
        print("regulator on", "both species" if both else "fermion line only (Collins)")
        for m in (0.2, 0.1, 0.05, 0.02, 0.01):
            o = run(m, both=both)
            print(f"  m/Lam={m:5.3f}  16pi^2 dc_phi={k*o['dc_phi']:+.5f}  16pi^2 dc_psi={k*o['dc_psi']:+.5f}  Delta={o['Delta']:+.5f}"
                  f"   (16pi^2 a={k*o['a']:.3f}, b={k*o['b']:.3f})")
