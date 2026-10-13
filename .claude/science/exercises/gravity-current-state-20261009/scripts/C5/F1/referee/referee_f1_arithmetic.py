"""Independent arithmetic check for the F1 sign and F2 Earth-row use."""

import math

# Independent N=156 value from referee_f1_baseline_n6.out.
hess_t = 2.423855387e-2

# F1/R19-31 normalization: t=-2h, hence c_h=d2/dh2=4*d2/dt2.
c_h = 4.0 * hess_t

# The canonical bridge used by F1 is m_g^2 a^2 = 16*pi*mu_SF with
# mu_SF proportional to <psibar psi>*positive coupling*hess_t.  Thus the
# reported positive Hessian is the massive sign in the packet's convention.
sign = "massive" if c_h > 0 else "tachyonic"

# Scale F2's H-cov placeholder coefficient linearly in |c_h|.
placeholder_mu_rho = 1.012e-21
placeholder_abs_c_h = 0.040475
mu_rho = placeholder_mu_rho * abs(c_h) / placeholder_abs_c_h

earth_density = 5500.0
earth_mass_ev = math.sqrt(mu_rho * earth_density)
f2_earth_bound = 1.5e-29
earth_ratio = mu_rho / f2_earth_bound

print(f"hess_t={hess_t:+.12e}")
print(f"c_h=4*hess_t={c_h:+.12e}")
print(f"packet_sign={sign}")
print(f"mu_rho={mu_rho:.12e} eV^2 m^3/kg")
print(f"earth_mass_at_5500={earth_mass_ev:.12e} eV")
print(f"ratio_to_F2_row1={earth_ratio:.12e}")
