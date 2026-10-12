"""Q1 (D): structured (complex) substrate amplitudes under a final-state projection, single mode.
Per-realization coherent amplitude lambda*x_P, x_P with law mu (here circular Gaussian, mean Psi1, variance V per mode).
Requirement: int psi(P) D(lambda x_P)|0> dmu = c(lambda) |lambda Psi1>  for ALL source strengths lambda.
Claim (report section 3.4): with g = psi * p_mu (p_mu = law density), the requirement is equivalent to the angular
components g_{-n}(r) = Psi1^n r^{-n} g_0(r) (n >= 0), forcing g_0 = 0 on r < |Psi1|; an explicit normalizable solution is
   g(x) = g0(|x|) x/(x - Psi1) 1[|x| > |Psi1|],  g0(r) = (r - |Psi1|) exp(-r^2/w),
and every solution has |c(lambda)| non-constant, -> 0 as |lambda| -> infinity (branch weight depends on the light).
Checks: (i) recombined state vs c|lambda Psi1> (fidelity), (ii) c(lambda), (iii) ||psi||_{L2(mu)} finite,
(iv) uniform psi = 1 for comparison (Gaussian closed form |2 lambda Psi1/(2+lambda^2 V)>)."""
import numpy as np
from scipy.special import gammaln
Psi1, V, w = 1.0, 4.0, 1.5
Nf = 60; n = np.arange(Nf)
def coh_amp(beta):  # Fock amplitudes of |beta>, vectorised over beta array -> (len(beta), Nf)
    beta = np.asarray(beta)[:, None]
    return np.exp(-np.abs(beta)**2/2 + n*np.log(np.abs(beta) + 1e-300) + 1j*n*np.angle(beta) - 0.5*gammaln(n + 1))
# polar grid r in (|Psi1|, rmax), theta uniform; midpoint rule; refine near the boundary
r = np.concatenate([np.linspace(Psi1, Psi1 + 0.2, 801)[:-1], np.linspace(Psi1 + 0.2, 7.0, 2401)])
rm = 0.5*(r[1:] + r[:-1]); dr = np.diff(r)
th = np.linspace(-np.pi, np.pi, 1441)[:-1] + np.pi/1440; dth = 2*np.pi/1440
R_, T_ = np.meshgrid(rm, th, indexing="ij"); X = R_*np.exp(1j*T_); dA = (R_*dr[:, None]*dth).ravel()
g = ((R_ - Psi1)*np.exp(-R_**2/w)*X/(X - Psi1)).ravel(); Xr = X.ravel()
pmu = np.exp(-np.abs(Xr - Psi1)**2/V)/(np.pi*V)
print("||psi||^2_{L2(mu)} = int |g|^2/p_mu dA = %.4g (finite => normalizable substrate amplitude)" % np.sum(np.abs(g)**2/pmu*dA))
print("int psi dmu = int g dA = %.4g" % abs(np.sum(g*dA)))
for lam in [0.3, 0.7, 1.0, 1.5, 2.0, 3.0]:
    st = (coh_amp(lam*Xr)*(g*dA)[:, None]).sum(0)
    tgt = coh_amp([lam*Psi1])[0]
    c = np.vdot(tgt, st); fid = abs(c)**2/np.vdot(st, st).real
    # uniform psi = 1 over the full Gaussian law (closed form) for comparison
    Vl = lam**2*V; amp_u = 2*lam*Psi1/(2 + Vl); cu = 2/(2 + Vl)*np.exp(-lam**2*Psi1**2*Vl/(2 + Vl)**2)
    print(" lambda=%.1f (GR photons nbar=%.2f, V_ph=%.1f): structured psi -> fidelity with |lambda Psi1> = %.6f, |c(lambda)| = %.4g ;"
          "  uniform psi -> coherent amp %.3f (target %.2f), weight %.3g" % (lam, (lam*Psi1)**2, Vl, fid, abs(c), amp_u, lam*Psi1, cu))
