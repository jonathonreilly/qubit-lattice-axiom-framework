"""T14 test: one-loop speed shifts of a naive Dirac fermion and a real scalar with a
Yukawa coupling g phi psibar psi on a Euclidean lattice with spatial step 1 and
time step eps.  Tree speeds are set by (c_psi, lam).  Everything is a coefficient of g^2.

Conventions (derived in PREREGISTRATION.md / report):
  fermion  M(k) = i gamma.s(k) + m,  s_0 = c_psi sin(theta)/eps, s_j = sin k_j, theta = eps*omega
  scalar   D^-1 = mu^2 + lam*(4/eps^2) sin^2(theta/2) + sum_j 4 sin^2(k_j/2)
  Gamma_psi(P) = M(P) - g^2 int D(k) S(P-k)     -> coefficient of i gamma_nu: s_nu(P) + g^2 F_nu(P)
  Gamma_phi(P) = D^-1(P) + g^2 int tr[S(k)S(k+P)]
  measure  int dw d3k/(2pi)^4 = (1/eps) * mean over the (theta,k) torus
Derivatives are analytic (no finite differences).
"""
import numpy as np, sys, json, time


def build(Nt, Ns, eps, m, mu, c_psi=1.0, lam=1.0):
    tt = 2 * np.pi * np.arange(Nt) / Nt
    ts = 2 * np.pi * np.arange(Ns) / Ns

    def sh(a, ax, n):
        shape = [1, 1, 1, 1]
        shape[ax] = n
        return a.reshape(shape)

    # fermion s_nu, s'_nu (d/d physical momentum), s''_nu
    s = [sh(c_psi * np.sin(tt) / eps, 0, Nt)]
    s1 = [sh(c_psi * np.cos(tt), 0, Nt)]
    s2 = [sh(-c_psi * eps * np.sin(tt), 0, Nt)]
    for j in (1, 2, 3):
        s.append(sh(np.sin(ts), j, Ns))
        s1.append(sh(np.cos(ts), j, Ns))
        s2.append(sh(-np.sin(ts), j, Ns))
    den = m**2 + sum(x**2 for x in s)
    Dinv = mu**2 + sh(lam * 4 * np.sin(tt / 2) ** 2 / eps**2, 0, Nt) + sum(
        sh(4 * np.sin(ts / 2) ** 2, j, Ns) for j in (1, 2, 3))
    D = 1.0 / Dinv
    meas = 1.0 / (eps * Nt * Ns**3)
    return dict(s=s, s1=s1, s2=s2, den=den, D=D, meas=meas, m=m)


def f_coef(B, nu):
    s, s1, den, D, meas = B['s'][nu], B['s1'][nu], B['den'], B['D'], B['meas']
    # F_nu(P) = int D(k) s_nu(P-k)/den(P-k);  d/dP_nu at 0
    return meas * np.sum(D * s1 * (1.0 / den - 2 * s**2 / den**2))


def t_coef(B, nu):
    """T(P) = int tr[S(k)S(k+P)] = 4 int (m^2 - s(k).s(k+P)) / (den(k) den(k+P)).
    t_nu = (1/2) d^2 T / dP_nu^2 at P=0."""
    m = B['m']
    s, s1, s2 = B['s'][nu], B['s1'][nu], B['s2'][nu]
    den, meas = B['den'], B['meas']
    Nk = m**2 - sum(x**2 for x in B['s'])          # N(q=k) = m^2 - s(k).s(k)
    Np = -s * s1                                   # dN/dq_nu
    Npp = -s * s2                                  # d2N/dq_nu2
    dp = 2 * s * s1
    dpp = 2 * s1**2 + 2 * s * s2
    second = Npp / den - 2 * Np * dp / den**2 - Nk * dpp / den**2 + 2 * Nk * dp**2 / den**3
    Tnn = 4 * meas * np.sum(second / den)
    return 0.5 * Tnn


def run(Nt, Ns, eps, m, mu, c_psi=1.0, lam=1.0):
    B = build(Nt, Ns, eps, m, mu, c_psi, lam)
    ft, fx = f_coef(B, 0), f_coef(B, 1)
    tt_, ts_ = t_coef(B, 0), t_coef(B, 1)
    # log-speed shifts per g^2
    a_psi = fx - ft / c_psi
    a_phi = 0.5 * (ts_ - tt_ / lam)
    return dict(ft=ft, fx=fx, tt=tt_, ts=ts_, a_psi=a_psi, a_phi=a_phi, gap=a_psi - a_phi)


if __name__ == "__main__":
    t0 = time.time()
    print(run(16, 16, 1.0, 0.5, 0.5))
    print(time.time() - t0)
