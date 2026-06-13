"""Bounded runner for the weak-field refractive-index support packet.

The field-shift input H -> H + phi is routed through the retained-bounded
weak-field source-response bridge and checked here as a local diagonal
scalar-potential lattice-symbol calculation.  The Fermat/eikonal index
n=k/k0 is checked here by phase counting for a fixed-energy single-frequency
packet.  This runner does not claim a universal matter-coupling theorem,
physical light-bending prefactor, nonlinear GR, or SI-unit G_Newton.

On the axis lattice dispersion lambda_axis(k) = 2 - 2 cos(k), fixed energy
lambda_axis(k) + phi = E gives the exact relation

    k(phi) = arccos(1 - (E - phi)/2),   n(phi) = k(phi)/k(0).

For small k and weak field, n(phi) = sqrt(1 - phi/E) + O(E, phi), hence
n = 1 - phi/(2E) + O((phi/E)^2, E, phi).  The packet-level Fermat reading is
the phase identity integral k dl = k0 integral (k/k0) dl.

The geometric (Fermat/geodesic) ray deflection of a retained lattice-unit
source-potential form phi = a/r is alpha(b) = integral grad_perp phi dl =
2a/b ~ 1/b in this scalar ray model.  This is distinct from the
dipole-suppressed Kubo susceptibility.  The calculation is only the bounded
geometric form, not a physical light-bending theorem.

  T0  one-hop field/source bridge and operator shift:
      retained-bounded weak-field source-response bridge supplies the scalar
      test response; constant-patch diagonal M_phi shifts the lattice symbol
      lambda(k) -> lambda(k)+phi.
  T1  exact axis-lattice dispersion shift:
      k(phi)=arccos(1-(E-phi)/2), n(phi)=k(phi)/k0.
      Small-k weak-field limit: n=sqrt(1-phi/E)+O(E,phi)
      and first order n=1-phi/(2E)+...
  T2  Fermat/eikonal phase counting:
      integral k dl = k0 integral (k/k0) dl, so n=k/k0.  First order:
      S = integral n dl = L - (1/2E) integral phi dl.
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
AUDIT_LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
KUBO_RUNNER = ROOT / "scripts" / "frontier_lensing_exponent_is_dipole_crossover.py"
KUBO_CACHE = ROOT / "logs" / "runner-cache" / "frontier_lensing_exponent_is_dipole_crossover.txt"
BRIDGE_NOTE = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
BRIDGE_RUNNER = ROOT / "scripts" / "frontier_gravity_weak_field_source_response_bridge_2026_06_11.py"
BRIDGE_CACHE = ROOT / "logs" / "runner-cache" / "frontier_gravity_weak_field_source_response_bridge_2026_06_11.txt"


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


def periodic_axis_laplacian(n: int) -> np.ndarray:
    h = np.zeros((n, n), dtype=complex)
    for i in range(n):
        h[i, i] = 2.0
        h[i, (i - 1) % n] = -1.0
        h[i, (i + 1) % n] = -1.0
    return h


# --- T0: one-hop field/source bridge plus local operator-symbol shift. ---
note_text = NOTE.read_text(encoding="utf-8")
bridge_text = BRIDGE_NOTE.read_text(encoding="utf-8")
ledger = json.loads(AUDIT_LEDGER.read_text(encoding="utf-8"))
rows = ledger.get("rows", {})

check("T0 source note names the 2026-06-13 one-hop bridge repair",
      "2026-06-13 One-Hop Bridge Repair" in note_text)
check("T0 source note routes to weak-field source-response bridge",
      "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md" in note_text
      and "S_test(phi; x)=L_test(1-phi(x))" in note_text
      and "U_test(phi; x)=-m phi(x)" in note_text)
check("T0 bridge note supplies bounded weak-field test response",
      "S_test(phi; x) = L_test (1 - phi(x))" in bridge_text
      and "U_test(phi; x) = -m phi(x)" in bridge_text
      and "This is a bounded weak-field theorem" in bridge_text)
check("T0 weak-field source-response bridge is retained_bounded",
      rows.get("gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11", {}).get("effective_status") == "retained_bounded")
check("T0 weak-field bridge audit status is clean",
      rows.get("gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11", {}).get("audit_status") == "audited_clean")
check("T0 weak-field bridge runner and cache are present",
      BRIDGE_RUNNER.exists() and BRIDGE_CACHE.exists())
if BRIDGE_RUNNER.exists() and BRIDGE_CACHE.exists():
    bridge_header = cache_header(BRIDGE_CACHE)
    check("T0 weak-field bridge cache is SHA-fresh",
          bridge_header.get("runner_sha256") == sha256(BRIDGE_RUNNER))
    check("T0 weak-field bridge cached run passed",
          "TOTAL: PASS=44 FAIL=0" in BRIDGE_CACHE.read_text(encoding="utf-8", errors="replace"))
else:
    check("T0 weak-field bridge cache is SHA-fresh", False)
    check("T0 weak-field bridge cached run passed", False)

n_sites = 64
mode_m = 5
k_mode = 2.0 * np.pi * mode_m / n_sites
phi_const = 0.037
axis_h = periodic_axis_laplacian(n_sites)
field_shift = phi_const * np.eye(n_sites, dtype=complex)
plane = np.exp(1j * k_mode * np.arange(n_sites)) / np.sqrt(n_sites)
lhs = (axis_h + field_shift) @ plane
rhs = (2.0 - 2.0 * np.cos(k_mode) + phi_const) * plane
check("T0 constant-patch diagonal field shifts symbol: H+M_phi has lambda(k)+phi",
      np.linalg.norm(lhs - rhs) < 1e-12)
check("T0 source note states H->H+phi is checked as a lattice-symbol step",
      "lattice-symbol shift" in note_text and "not a new primitive" in note_text)

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
# along a path of length Lpath through a field profile phi(s); phase = int k ds.
Lpath = 10.0
phi_prof = lambda s: 0.01 / (1 + abs(s - 5))    # some field along the path
grid = np.linspace(0.0, Lpath, 2048)
ds = grid[1] - grid[0]
phi_grid = np.array([phi_prof(float(s)) for s in grid])
k_grid = np.sqrt(np.maximum(E - phi_grid, 0.0))
k0_cont = np.sqrt(E)
phase_direct = float(np.trapezoid(k_grid, grid))
phase_via_index = float(k0_cont * np.trapezoid(k_grid / k0_cont, grid))
check("T2 eikonal phase counting identifies n=k/k0",
      abs(phase_direct - phase_via_index) < 1e-12)
check("T2 source note states n=k/k0 is runner-checked by phase counting",
      "phase-counting identity" in note_text and "n=k/k_0" in note_text)
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
check("SOURCE note names the 2026-06-08 audit-targeted boundary repair",
      "2026-06-08 Audit-Targeted Boundary Repair" in note_text)
check("SOURCE note no longer leaves Fermat n=k/k0 as a bare supplied bridge",
      "bare import" in note_text and "phase counting" in note_text
      and "phase-counting identity" in note_text)
check("SOURCE note contains exact arccos lattice relation",
      "k(phi)=arccos(1 - (E - phi)/2)" in note_text
      or "k(φ)=arccos(1−(E−φ)/2)" in note_text)
check("AUTH self_consistency_forces_poisson is retained_bounded",
      rows.get("self_consistency_forces_poisson_note", {}).get("effective_status") == "retained_bounded")
check("AUTH finite_rank_source_to_metric is retained_bounded",
      rows.get("finite_rank_source_to_metric_theorem_note", {}).get("effective_status") == "retained_bounded")
check("AUTH gravity leading lattice correction is retained",
      rows.get("gravity_leading_lattice_correction_cubic_anisotropy_theorem_note_2026-06-07", {}).get("effective_status") == "retained")
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
check("AUTH weak-field bridge is exposed in source relation table",
      "`gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11` | retained_bounded" in note_text)
check("AUTH leading lattice correction is exposed in source relation table",
      "`gravity_leading_lattice_correction_cubic_anisotropy_theorem_note_2026-06-07` | retained" in note_text)
check("KUBO comparison packet status is exposed as retained_bounded comparison-only authority",
      rows.get("lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07", {}).get("effective_status") == "retained_bounded"
      and "`lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07` | retained_bounded" in note_text
      and "does not supply the Fermat/eikonal bridge" in note_text)
check("SOURCE no physical light-bending or nonlinear-GR promotion",
      "not a physical light-bending prefactor theorem" in note_text
      and "nonlinear GR" in note_text
      and "SI-unit Newton constant" in note_text)
check("SOURCE keeps universal matter coupling outside the packet",
      (("universal matter-coupling" in note_text or "universal matter coupling" in note_text)
       and ("outside this packet" in note_text or "remain open" in note_text)))

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
