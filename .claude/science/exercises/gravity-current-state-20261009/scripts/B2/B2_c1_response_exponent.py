"""B2 check c1: how fast must the substrate's transverse (TT) stress response
vanish at low frequency for gravitational waves to be massless enough and to
cross 1 Gpc undamped?

Model (suggested, linear response): the graviton's TT self-energy from a
medium is Pi(w) = 16 pi G * G_T(w), where G_T(w) is the medium's zero-momentum
transverse stress response (shear modulus at frequency w).  Static part
Re G_T(0) = shear modulus -> mass^2 (Rubakov-Tinyakov); dissipative part
Im G_T(w) = eta*w -> amplitude damping Gamma = Im Pi/(2w) = 8 pi G eta
(energy damping 16 pi G eta, Hawking 1966).
Planck normalisation: G_T(w) = c * M_P^4 * (w/M_P)^n.  Units hbar=c=1.
"""
import math
eV = 1.0
M_P = 1.220890e28 * eV            # Planck mass in eV (G = 1/M_P^2)
hbar_eVs = 6.582119569e-16         # eV s
lP_m = 1.616255e-35
Gpc_m = 3.0857e25
mg_bound = 1.3e-23 * eV            # GWTC-3 graviton mass bound (approx)

def omega_eV(f_Hz):
    return 2*math.pi*f_Hz*hbar_eVs

D_planck = {"40 Mpc": 0.04*Gpc_m/lP_m, "1 Gpc": Gpc_m/lP_m}

print("Planck-normalised medium, c = 1")
for f in (20.0, 100.0, 1000.0):
    x = omega_eV(f)/M_P
    # mass condition: 16 pi x^n M_P^2 < mg^2  ->  n > log(mg^2/(16 pi M_P^2))/log x
    n_mass = math.log(mg_bound**2/(16*math.pi*M_P**2))/math.log(x)
    out = [f"f={f:6.0f} Hz  w/M_P={x:.2e}  n_mass>{n_mass:.2f}"]
    for lab, D in D_planck.items():
        # amplitude damping: Gamma = Im Pi/(2w) = 8 pi M_P x^(n-1)  (M_P units: 8 pi x^(n-1) per t_P)
        # need Gamma*D < 0.1 -> 8 pi x^(n-1) D < 0.1
        n_damp = 1 + math.log(0.1/(8*math.pi*D))/math.log(x)
        out.append(f"n_damp({lab})>{n_damp:.2f}")
    print("  ".join(out))

print()
print("Classical dissipative liquid, n = 1 (eta = G_inf * tau, Planck values g*kappa):")
for lab, D in D_planck.items():
    need = 0.1/(8*math.pi*D)
    print(f"  {lab}: D = {D:.2e} l_P ; need g*kappa < {need:.1e}  (amplitude loss < 10%)")
print()
print("Lorentz-invariant quantum vacuum: Pi ~ G k^4 log k^2  ->  n = 4 at q = 0:")
x = omega_eV(100.0)/M_P
print(f"  at 100 Hz: Pi/M_P^2 ~ 16 pi x^4 = {16*math.pi*x**4:.1e} ; mass bound needs < {mg_bound**2/M_P**2:.1e}")
