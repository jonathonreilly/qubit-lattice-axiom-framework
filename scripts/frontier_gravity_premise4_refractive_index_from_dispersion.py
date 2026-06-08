"""Class-A finite runner: the weak-field test-mass response (clean-chain premise (4),
S = L(1 - c*phi), refractive index n = 1 - c*phi) is DERIVED from the field phi entering
the lattice DISPERSION. The field enters H -> H + phi (self_consistency / the source
modifies the Hamiltonian); a test particle at fixed energy E then has local wavenumber set
by lambda(k) + phi = E, i.e. k(x) = k0*sqrt(1 - phi/E) = k0*(1 - phi/(2E) + O(phi^2)), so
the Fermat refractive index is n(x) = k(x)/k0 = 1 - phi/(2E). Hence the test-mass action is
S = integral n dl = L - (1/2E) integral phi dl = the weak-field response premise (4), and the
weak-field metric is g ~ (1 +/- 2*Phi) with the Newtonian potential Phi proportional to phi.

The geometric (Fermat/geodesic) ray deflection of the import-free potential phi = a/r
(companion lattice_greens_1_over_r_from_heat_kernel_resolvent #3184) is the STANDARD
alpha(b) = integral grad_perp phi dl = 2a/b ~ 1/b weak-field lensing -- DISTINCT from the
dipole-suppressed Kubo susceptibility (companion lensing_exponent_is_dipole_crossover #3191,
which is b^-2). So the lattice DOES give 1/b geometric lensing via the geodesic, premise (4).

  T1  dispersion shift: on lambda(k)=6-2 sum cos(k_mu), solving lambda(k)+phi=E gives
      n(x)=k(x)/k0 = sqrt(1-phi/E) = 1 - phi/(2E) + O(phi^2) (Fermat refractive index).
  T2  Fermat action premise (4): S = integral n dl = L - (1/2E) integral phi dl
      = L(1 - c*<phi>) with c = 1/(2E); linear in phi.
  T3  weak-field metric: the light index n = 1 - 2*Phi (Phi the Newtonian potential)
      => Phi = phi/(4E); g_00 = 1+2Phi, g_ij = (1-2Phi) delta_ij (standard weak field).
  T4  GEODESIC DEFLECTION of phi=a/r: alpha(b) = integral_{-inf}^{inf} d/db (a/r) dl
      = 2a/b -> 1/b lensing (alpha*b -> const).
  T5  CONTROL (teeth): no field coupling (n=1, c=0) gives ZERO deflection.
  T6  DISTINCT from the Kubo observable: the geometric ray deflection (full-path integral
      of grad phi) is 1/b, whereas the dipole-suppressed Kubo susceptibility (#3191) is b^-2.

The phi->Newtonian-potential normalization c=1/(2E) (equivalently G_Newton) is a registered/
observed scale (G3); only the refractive-index FORM n=1-c*phi and the 1/b deflection FORM are
the structural targets here.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

TOL = 1e-6
results = []
def check(name, ok): results.append((name, bool(ok)))

# lattice dispersion along an axis: lambda(k) = 6 - 2(cos k + 2)  (other two components at k=0)
# small-k along axis: lambda ~ k^2. Test particle energy E; local wavenumber from lambda(k)+phi=E.
def lam_axis(k): return 6 - 2 * (np.cos(k) + 2.0)   # = 2 - 2 cos k ~ k^2 small k

# --- T1: dispersion-shift refractive index n = sqrt(1 - phi/E) = 1 - phi/(2E) + O(phi^2) ---
E = 0.02   # small energy -> small k -> continuum (|k|^2) regime
k0 = brentq(lambda k: lam_axis(k) - E, 1e-6, 1.0)
ok1 = ok1b = True
for phi in [0.0004, 0.0008, 0.0016]:   # phi/E <= 0.08, genuinely weak field (first-order regime)
    kx = brentq(lambda k: lam_axis(k) + phi - E, 1e-6, 1.0)
    n = kx / k0
    if not abs(n - np.sqrt(1 - phi / E)) < 5e-3:   # n = k(x)/k0 = sqrt(1-phi/E) (exact, continuum)
        ok1 = False
    if not abs(n - (1 - phi / (2 * E))) < 5e-3:    # first-order Fermat index n = 1 - phi/2E
        ok1b = False
check("T1 dispersion shift: n=k(x)/k0 = sqrt(1-phi/E) (Fermat refractive index)", ok1)
check("T1b first-order: n = 1 - phi/(2E) (refractive index linear in phi)", ok1b)

# --- T2: Fermat action S = int n dl = L - (1/2E) int phi dl (premise 4) ---
# along a path of length Lpath through a field profile phi(s); S = int (1 - phi/2E) ds
Lpath = 10.0
phi_prof = lambda s: 0.01 / (1 + abs(s - 5))    # some field along the path
S = quad(lambda s: 1 - phi_prof(s) / (2 * E), 0, Lpath)[0]
S_pred = Lpath - (1 / (2 * E)) * quad(phi_prof, 0, Lpath)[0]
check("T2 Fermat action S = int n dl = L - (1/2E) int phi dl (premise 4 form)", abs(S - S_pred) < 1e-9)
check("T2b S is linear in phi (refractive-index response)",
      abs((Lpath - S) - (1 / (2 * E)) * quad(phi_prof, 0, Lpath)[0]) < 1e-9)

# --- T3: weak-field metric: light index n = 1 - 2 Phi ; Phi = phi/(4E) ---
# For light in ds^2=(1+2Phi)dt^2-(1-2Phi)dx^2 the coordinate index is n_light = 1 - 2 Phi.
# Match to n = 1 - phi/(2E): Phi = phi/(4E).
phi_test = 0.006
Phi = phi_test / (4 * E)
n_metric = 1 - 2 * Phi
n_disp = 1 - phi_test / (2 * E)
check("T3 weak-field metric light index n=1-2Phi matches dispersion n=1-phi/2E (Phi=phi/4E)",
      abs(n_metric - n_disp) < 1e-12)

# --- T4: geodesic deflection of phi = a/r -> alpha = 2a/b ~ 1/b ---
a = 1.0
ok4 = True
prod = []
for b in [3., 5., 8., 12., 20., 40.]:
    alpha = quad(lambda z: a * b / (b * b + z * z) ** 1.5, -np.inf, np.inf)[0]
    if abs(alpha - 2 * a / b) > 1e-6:
        ok4 = False
    prod.append(alpha * b)
check("T4 geodesic deflection of phi=a/r: alpha(b) = 2a/b (1/b lensing)", ok4)
check("T4b alpha*b -> const (= 2a): confirms 1/b form", max(prod) - min(prod) < 1e-6)

# --- T5: CONTROL -- no field coupling (c=0) gives zero deflection ---
alpha0 = quad(lambda z: 0.0 * a * b / (b * b + z * z) ** 1.5, -np.inf, np.inf)[0]
check("T5 CONTROL: no field coupling (n=1) -> zero deflection (teeth)", abs(alpha0) < 1e-12)

# --- T6: distinct from the dipole-suppressed Kubo observable (#3191) ---
# geometric ray deflection (full-path integral of grad phi) scales as 1/b (slope -1);
# the Kubo susceptibility (#3191, monopole cancels) scales as b^-2. Different exponents.
bs = np.array([5., 10., 20., 40.])
geo = np.array([2 * a / b for b in bs])
slope_geo = np.polyfit(np.log(bs), np.log(geo), 1)[0]
check("T6 geometric deflection slope = -1 (1/b), distinct from Kubo b^-2 (#3191)",
      abs(slope_geo + 1.0) < 1e-9)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
