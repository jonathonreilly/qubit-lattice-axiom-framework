"""F6 (c) clock row: rms drift of the E_g strain quadratic Q_E = (h_E1^2 + h_E2^2)/2 at a point under the NANOGrav 15-yr GW background.
Q_E is normalised so that the SF strain diag(-t, t, 0) (|t| = |h_+|, reading as pheno T2) gives Q_E = t^2; the E_g Hessians multiply Q_E
(cubic invariance on E_g).  T_2g components are not included (their Hessian is not computed); since E_g and T_2g quadratics involve
disjoint independent components, omitting T_2g can only LOWER the rms drift (proved: zero cross-covariance).
Spectrum (comparator, NANOGrav 15-yr, arXiv:2306.16213; values as pre-registered at TESTS F6): h_c(f) = A (f/f_yr)^{(3-gamma)/2},
A = 2.4e-15, gamma = 13/3; one-sided PSD of <h_ij h_ij> = 2 h_c^2/f (Maggiore convention: <h_ij h^ij> = 2 int dlnf h_c^2), isotropic
-> each of the 5 orthonormal traceless components gets 1/5: S_a(f) = (2/5) h_c^2/f, for f >= f_min (cut), f_max = 50/yr.
Drift estimators: (i) least-squares slope of Q_E over a window T_obs (Gaussian field: Cov(Q(tau),Q(tau')) = C(tau-tau')^2, C = cov per
component); (ii) rms of dQ/dtau from modes slower than 1/T_obs (pheno T2's estimator: 2 t tdot)."""
import numpy as np
yr = 1.0
A, gam = 2.4e-15, 13/3
alpha = (3 - gam)/2
def run(fmin, Tobs, fmax=50.0, nf=4000, nt=801):
    f = np.exp(np.linspace(np.log(fmin), np.log(fmax), nf))
    hc2 = (A*(f/1.0)**alpha)**2
    S = 0.4*hc2/f
    lnf = np.log(f)
    def integ(y, mask=None):
        if mask is not None:
            y = np.where(mask, y, 0.0)
        return float(np.sum(0.5*(y[1:] + y[:-1])*np.diff(lnf)))
    sig2 = integ(S*f)                     # int S df = int S f dlnf
    tau = np.linspace(-Tobs/2, Tobs/2, nt)
    D = tau[:, None] - tau[None, :]
    # C(Delta) = int S cos(2 pi f Delta) df, evaluated on the unique Delta grid
    dg = np.linspace(0, Tobs, nt)
    Cg = np.array([integ(S*f*np.cos(2*np.pi*f*dd)) for dd in dg])
    C = np.interp(np.abs(D), dg, Cg)
    wts = np.full(nt, tau[1] - tau[0]); wts[0] *= 0.5; wts[-1] *= 0.5
    num = (wts[:, None]*wts[None, :]*tau[:, None]*tau[None, :]*C**2).sum()
    beta_rms = np.sqrt(num)*12/Tobs**3
    low = f < 1/Tobs
    sd2l = integ((2*np.pi*f)**2*S*f, low)
    qdot_rms = np.sqrt(2*sig2*sd2l)        # <Qdot^2> = 2 sigma^2 sigma_dot^2 (2 independent E_g components; sigma^2 all modes)
    return sig2, beta_rms, qdot_rms
print('NANOGrav 15-yr: A = %.2e, gamma = %.4f. per-component variance sigma^2, <Q_E> = 2 sigma^2/2 = sigma^2' % (A, gam))
out = {}
for fmin_yr in (16.0, 30.0):
    for Tobs in (5.0, 10.0):
        s2, b, q = run(1/fmin_yr, Tobs)
        out[(fmin_yr, Tobs)] = (s2, b, q)
        print('  f_min = 1/(%2.0f yr), T_obs = %4.1f yr: sigma_a = %.3e (rms h_ij h_ij = %.3e); LS slope rms of Q_E = %.3e /yr; rms dQ/dt (f < 1/T_obs) = %.3e /yr'
              % (fmin_yr, Tobs, np.sqrt(s2), np.sqrt(5*s2), b, q))
np.save('f6_drift.npy', np.array([[k[0], k[1], *v] for k, v in out.items()]))
