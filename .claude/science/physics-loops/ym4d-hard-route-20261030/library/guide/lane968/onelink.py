# GUIDE only: one free SU(2) link, mid-slice bridge marginal. Checks the hand numbers of Sections 5.2, 5.3, 6.3.
import numpy as np, math
def bessel(nu, z, K=80):
    k = np.arange(K)[:, None]
    lg = (2 * k + nu) * np.log(np.maximum(z, 1e-300) / 2.0) - np.array([math.lgamma(i + 1) + math.lgamma(i + nu + 1) for i in range(K)])[:, None]
    return np.exp(lg).sum(0)
def A(z):  # I_2/I_1
    return bessel(2, z) / bessel(1, z)
for beta in (2.3, 2.6):
    s = 1.0 / (2 * beta); c = s / 2
    r = np.linspace(1e-4, 3.0, 300001); dr = r[1] - r[0]
    z = r / s
    logh = -(r * r + 1) / (2 * s) + np.log(2 * bessel(1, z) / z)          # log of g_s * Haar, up to a constant
    dens = r ** 3 * np.exp(2 * (logh - logh.max()))                       # radial law of |y| under nu_mid
    dens /= dens.sum() * dr
    ktan = (1 / c) * (1 - A(z) / r)                                       # Phi'(r)/r = 4 beta (1 - A(2 beta r)/r)
    neg = ktan < 0
    rstar = r[neg].max() if neg.any() else 0.0
    print("beta", beta, " r* = %.3f" % rstar, " P(r<r*) = %.4f" % (dens[neg].sum() * dr),
          " P(r<0.4) = %.4f" % (dens[r < 0.4].sum() * dr), " ktan(0+) = %.3f" % ktan[0], " ktan(1) = %.3f" % ktan[np.argmin(abs(r - 1))])
    print("   identity: E[ktan] = %.4f   2 E[r^-2] = %.4f   E r^2 = %.4f" % ((ktan * dens).sum() * dr, 2 * (dens / r ** 2).sum() * dr, (r * r * dens).sum() * dr))
    print("   worst-case conditioning: P(chi2_4 < 0.16/c) = %.4f" % (1 - math.exp(-0.16 / c / 2) * (1 + 0.16 / c / 2)))
