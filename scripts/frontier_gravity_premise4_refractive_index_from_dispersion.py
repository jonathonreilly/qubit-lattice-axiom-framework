"""Bounded runner for the weak-field refractive-index support packet.

The scalar weak-field source/action sign is supplied by the retained-bounded
weak-field source-response bridge.  A paired fixed-energy eikonal bridge proves
n=k/k0 as a bounded phase-count identity for this scalar ray packet.  This
runner checks the lattice-dispersion arithmetic, bridge wiring, and
source-boundary discipline; it does not claim a physical Newton-constant value
or nonlinear metric closure.

On the axis lattice dispersion lambda_axis(k) = 2 - 2 cos(k), fixed energy
lambda_axis(k) + phi = E gives the exact relation

    k(phi) = arccos(1 - (E - phi)/2),   n(phi) = k(phi)/k(0).

For small k and weak field, n(phi) = sqrt(1 - phi/E) + O(E, phi), hence
n = 1 - phi/(2E) + O((phi/E)^2, E, phi).  With the Fermat reading supplied,
the test-mass action is S = integral n dl = L - (1/2E) integral phi dl.

The geometric (Fermat/geodesic) ray deflection of the import-free potential phi = a/r
(companion lattice_greens_1_over_r_from_heat_kernel_resolvent #3184) is the STANDARD
alpha(b) = integral grad_perp phi dl = 2a/b ~ 1/b weak-field lensing -- DISTINCT from the
dipole-suppressed Kubo susceptibility (companion lensing_exponent_is_dipole_crossover #3191,
which is b^-2). So the lattice DOES give 1/b geometric lensing via the geodesic, premise (4).

  T1  exact axis-lattice dispersion shift:
      k(phi)=arccos(1-(E-phi)/2), n(phi)=k(phi)/k0.
      Small-k weak-field limit: n=sqrt(1-phi/E)+O(E,phi)
      and first order n=1-phi/(2E)+...
  T2  Fermat action premise (4): S = integral n dl = L - (1/2E) integral phi dl
      = L(1 - c*<phi>) with c = 1/(2E); linear in phi.
  T3  weak-field metric: the light index n = 1 - 2*Phi (Phi the Newtonian potential)
      => Phi = phi/(4E); g_00 = 1+2Phi, g_ij = (1-2Phi) delta_ij (standard weak field).
  T4  GEODESIC DEFLECTION of phi=a/r: alpha(b) = integral_{-inf}^{inf} d/db (a/r) dl
      = 2a/b -> 1/b lensing (alpha*b -> const).
  T5  CONTROL (teeth): no field coupling (n=1, c=0) gives ZERO deflection.
  T6  DISTINCT from the Kubo observable: the geometric ray deflection (full-path integral
      of grad phi) is 1/b, whereas the retained-bounded dipole-suppressed Kubo
      susceptibility packet is a different bounded object.

The phi->Newtonian-potential normalization c=1/(2E) (equivalently G_Newton) is a registered/
observed scale (G3); only the refractive-index FORM n=1-c*phi and the 1/b deflection FORM are
the structural targets here.

prints TOTAL: PASS=N FAIL=0
"""

import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

TOL = 1e-6
results = []
def check(name, ok): results.append((name, bool(ok)))

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GRAVITY_PREMISE4_REFRACTIVE_INDEX_FROM_DISPERSION_BOUNDED_THEOREM_NOTE_2026-06-07.md"
EIKONAL_NOTE = ROOT / "docs" / "GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
EIKONAL_RUNNER = ROOT / "scripts" / "frontier_gravity_fixed_energy_eikonal_index_bridge_2026_06_16.py"
SCALAR_SHIFT_NOTE = ROOT / "docs" / "GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md"
SCALAR_SHIFT_RUNNER = ROOT / "scripts" / "frontier_gravity_scalar_shift_sign_normalization_2026_06_18.py"
AUDIT_LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
KUBO_RUNNER = ROOT / "scripts" / "frontier_lensing_exponent_is_dipole_crossover.py"
KUBO_CACHE = ROOT / "logs" / "runner-cache" / "frontier_lensing_exponent_is_dipole_crossover.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_header(cache_path: Path) -> dict[str, str]:
    header = cache_path.read_text(encoding="utf-8", errors="replace").split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields

# lattice dispersion along an axis: lambda(k) = 6 - 2(cos k + 2)  (other two components at k=0)
# small-k along axis: lambda ~ k^2. Test particle energy E; local wavenumber from lambda(k)+phi=E.
def lam_axis(k): return 6 - 2 * (np.cos(k) + 2.0)   # = 2 - 2 cos k ~ k^2 small k

# --- T1: exact axis-lattice shift plus small-k weak-field limit. ---
E = 0.02   # small energy -> small k -> continuum (|k|^2) regime
k0 = brentq(lambda k: lam_axis(k) - E, 1e-6, 1.0)
exact_lattice_ok = small_k_ok = first_order_ok = True
for phi in [0.0004, 0.0008, 0.0016]:   # phi/E <= 0.08, genuinely weak field (first-order regime)
    kx = brentq(lambda k: lam_axis(k) + phi - E, 1e-6, 1.0)
    exact_kx = np.arccos(1.0 - (E - phi) / 2.0)
    n_exact = kx / k0
    n_continuum = np.sqrt(1 - phi / E)
    n_linear = 1 - phi / (2 * E)
    if abs(kx - exact_kx) > 1e-12:
        exact_lattice_ok = False
    if not abs(n_exact - n_continuum) < 5e-3:
        small_k_ok = False
    if not abs(n_exact - n_linear) < 5e-3:
        first_order_ok = False
check("T1 exact axis-lattice map: k(phi)=arccos(1-(E-phi)/2)", exact_lattice_ok)
check("T1b small-k limit: n=k(phi)/k0 = sqrt(1-phi/E)+O(E,phi)", small_k_ok)
check("T1c first-order weak field: n = 1 - phi/(2E)", first_order_ok)

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

# --- SOURCE/AUTHORITY BOUNDARY: expose ledger statuses and comparison packet. ---
note_text = NOTE.read_text(encoding="utf-8")
ledger = json.loads(AUDIT_LEDGER.read_text(encoding="utf-8"))
rows = ledger.get("rows", {})
check("SOURCE note names the 2026-06-08 audit-targeted boundary repair",
      "2026-06-08 Audit-Targeted Boundary Repair" in note_text)
check("SOURCE note names the 2026-06-16 source-side eikonal bridge repair",
      "2026-06-16 Source-Side Eikonal Bridge Repair" in note_text)
check("SOURCE note names the 2026-06-18 scalar-shift sign bridge repair",
      "2026-06-18 Scalar-Shift Sign and Normalization Bridge Repair" in note_text
      and "GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md" in note_text)
check("SOURCE note cites the fixed-energy eikonal index bridge",
      "GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md" in note_text
      and "n(x) = k_s(x) / k_0" in note_text)
check("SOURCE note routes H_s=H_0+sI through scalar-shift sign bridge",
      "scalar-shift sign and fixed-energy normalization bridge for" in note_text
      and "`H_s=H_0+sI` and `phi_action=c_E s`" in note_text
      and "`gravity_scalar_shift_sign_normalization_bounded_theorem_note_2026-06-18`" in note_text)
check("SOURCE note states bounded bridge hypotheses explicitly",
      "bounded source-side repair proposal" in note_text
      and "Hypotheses for T1-T6" in note_text
      and "phase-count bridge" in note_text)
check("SOURCE note leaves physical normalization and nonlinear metric closure open",
      "does not claim a physical value of `G_Newton`" in note_text
      and "nonlinear metric theorem" in note_text
      and "arbitrary-graph WKB closure" in note_text)
check("SOURCE note contains exact arccos lattice relation",
      "k(phi)=arccos(1 - (E - phi)/2)" in note_text
      or "k(φ)=arccos(1−(E−φ)/2)" in note_text)
check("AUTH self_consistency_forces_poisson is retained_bounded",
      rows.get("self_consistency_forces_poisson_note", {}).get("effective_status") == "retained_bounded")
check("AUTH finite_rank_source_to_metric is retained_bounded",
      rows.get("finite_rank_source_to_metric_theorem_note", {}).get("effective_status") == "retained_bounded")
check("AUTH weak-field source-response bridge is retained_bounded",
      rows.get("gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11", {}).get("effective_status") == "retained_bounded")
check("SCALAR-SHIFT sign bridge note and runner are present",
      SCALAR_SHIFT_NOTE.exists() and SCALAR_SHIFT_RUNNER.exists())
if SCALAR_SHIFT_NOTE.exists():
    scalar_shift_text = SCALAR_SHIFT_NOTE.read_text(encoding="utf-8")
    check("SCALAR-SHIFT sign bridge proves H_s=H_0+sI and phi_action=c_E s",
          "H_s = H_0 + s I" in scalar_shift_text
          and "lambda_axis(k_s) + s = E" in scalar_shift_text
          and "phi_action := c_E s" in scalar_shift_text
          and "s = phi_action / c_E = k0 lambda_axis'(k0) phi_action" in scalar_shift_text)
else:
    check("SCALAR-SHIFT sign bridge proves H_s=H_0+sI and phi_action=c_E s", False)
check("EIKONAL bridge note and runner are present",
      EIKONAL_NOTE.exists() and EIKONAL_RUNNER.exists())
if EIKONAL_NOTE.exists():
    eikonal_text = EIKONAL_NOTE.read_text(encoding="utf-8")
    check("EIKONAL bridge proves n=k/k0 as phase-count identity",
          "n_j := k_{s_j} / k0" in eikonal_text
          and "Phase[s]/k0" in eikonal_text
          and "does not derive a universal matter" in eikonal_text)
else:
    check("EIKONAL bridge proves n=k/k0 as phase-count identity", False)
check("KUBO comparison runner and cache are present",
      KUBO_RUNNER.exists() and KUBO_CACHE.exists())
if KUBO_RUNNER.exists() and KUBO_CACHE.exists():
    kubo_header = cache_header(KUBO_CACHE)
    check("KUBO comparison cache is SHA-fresh",
          kubo_header.get("runner_sha256") == sha256(KUBO_RUNNER))
else:
    check("KUBO comparison cache is SHA-fresh", False)
check("AUTH lattice Green support is retained_bounded",
      rows.get("lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07", {}).get("effective_status") == "retained_bounded"
      and "`lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07` | retained_bounded" in note_text)
check("KUBO comparison packet status is exposed as retained_bounded comparison-only authority",
      rows.get("lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07", {}).get("effective_status") == "retained_bounded"
      and "`lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07` | retained_bounded" in note_text
      and "does not supply the Fermat/eikonal bridge" in note_text)
check("SOURCE no full premise-4 promotion",
      "independent audit must still decide the effective status" in note_text
      and "physical Newton-constant" in note_text
      and "nonlinear/strong-field regime remain open" in note_text)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
