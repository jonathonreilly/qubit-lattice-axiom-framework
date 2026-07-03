"""Class-A finite runner (memory-safe, H=0.6): supports the mechanism behind the lensing
deflection exponent ~ -1.43. The Kubo deflection observable alpha(b) = sum_e c_e/r_e(b)
(retained_bounded lensing_deflection_note) is a SIGNED linear-response susceptibility
whose MONOPOLE CANCELS (sum_e c_e = 0, a translation-invariance sum rule: a uniform field
produces NO centroid deflection -- only gradients do). Hence the leading 1/b term vanishes.
At coarse H=0.6 the large-b signed falloff is dipole-like; the fine-H companion checks the
H=0.25 edge kernel directly and leaves the exact asymptotic order open. The measured -1.43
is NOT an asymptotic exponent: it is a CROSSOVER slope, measured at impact parameters b in
{3,4,5,6} that are
COMPARABLE to the near-source kernel support (~3.6), in the transition between the
cancelled-monopole (-1) and steeper signed-multipole regimes. The slope drifts steeper with refinement
as the kernel sharpens; it is L-independent because the kernel is localized near the source.

Memory note: the slope value is H-dependent (a crossover slope, not a converged exponent);
the runner asserts the MECHANISM (monopole cancellation, coarse-H large-b falloff, crossover at
b~support), which is robust, at the memory-safe coarse H=0.6 (~10^4 sites). The H=0.25
edge-kernel companion is the fine-H certificate. The flagship
G(r)->1/(4pi r) (PR #3184) is the genuine 1/r structure; THIS observable is a distinct,
monopole-suppressed susceptibility, not the geometric ray deflection.

  T1  monopole cancels: |sum_e c_e| / sum_e |c_e| < 0.01 (translation-invariance sum rule).
  T2  uniform-field sum rule: a constant field (1/r_e -> 1) gives deflection = sum_e c_e,
      tiny vs a typical |alpha(b)| -> a uniform field does not deflect the centroid.
  T3  kernel localized near source: |c|-weighted <|mx - x_src|> ~ 3.6 << path span (~15);
      so the fitted b-values {3,4,5,6} are COMPARABLE to the kernel support (crossover).
  T4  crossover: |slope| at small b (b ~ support) < |slope| at large b; at H=0.6
      the large-b signed slope is near -2 (dipole-like).
  T5  CONTROL (decisive): the SAME geometry with a NON-cancelling kernel |c_e| (monopole
      = sum|c| != 0) gives the large-b slope -> -1 (the 1/b of a non-cancelled monopole).
      So the steepening is CAUSED by the monopole cancellation, not the geometry.

prints TOTAL: PASS=N FAIL=0
"""

import os
import json
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import frontier_lensing_h025_edge_kernel_certificate_2026_06_08  # noqa: F401
import frontier_lensing_h025_source_packet_manifest_2026_06_09  # noqa: F401
from kubo_continuum_limit import BETA, K_PER_H, PW_PHYS, SRC_LAYER_FRAC, grow
from lensing_adjoint_kernel_probe import build_free_and_adjoint
from lensing_adjoint_kernel_reduced_model import signed_edge_coefficients, exact_edge_sum, log_slope
import runner_cache as rc

results = []
def check(name, ok): results.append((name, bool(ok)))

ROOT = Path(__file__).resolve().parents[1]
H025_RUNNER = "scripts/frontier_lensing_h025_edge_kernel_certificate_2026_06_08.py"
H025_MANIFEST_RUNNER = "scripts/frontier_lensing_h025_source_packet_manifest_2026_06_09.py"
H025_OUTPUT = ROOT / "outputs/lensing_h025_edge_kernel_certificate_2026_06_08.json"


def cache_green(runner_path, total_marker):
    cache_path, header, text = rc.load_cache(runner_path)
    return (
        rc.cache_status(runner_path) == "fresh"
        and header is not None
        and header.get("status") == "ok"
        and str(header.get("exit_code")) == "0"
        and text is not None
        and total_marker in text
        and cache_path.exists()
    )


def h025_json_green():
    try:
        data = json.loads(H025_OUTPUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    summary = data.get("summary", {})
    setup = data.get("setup", {})
    return (
        summary.get("pass") == 12
        and summary.get("fail") == 0
        and setup.get("H") == 0.25
        and setup.get("NL") == 60
        and setup.get("n_edges_streamed", 0) > 60_000_000
        and abs(data.get("small_fit", {}).get("slope", 0.0) + 1.4335) < 1.0e-3
    )

H = 0.6
T_PHYS = 15.0
NL = max(3, round(T_PHYS / H))
k_phase = K_PER_H / H
x_src = round(NL * SRC_LAYER_FRAC) * H

pos, adj, _ = grow(0, 0.20, 0.70, NL, PW_PHYS, 3, H)
A, lam, cz, T0, _ = build_free_and_adjoint(pos, adj, NL, PW_PHYS, H, k_phase, BETA)
edges = signed_edge_coefficients(pos, adj, H, k_phase, BETA, A, lam)
cs = np.array([e[1] for e in edges])
mx = np.array([e[2] for e in edges])
mz = np.array([e[3] for e in edges])

# --- T1: monopole cancels ---
mono = abs(cs.sum()) / np.abs(cs).sum()
check("T1 monopole cancels: |sum c|/sum|c| < 0.01 (got %.4f)" % mono, mono < 0.01)

# --- T2: uniform-field sum rule (constant field -> deflection = sum c, tiny) ---
typ = np.median([abs(exact_edge_sum(edges, x_src, b)) for b in [3., 4., 5., 6.]])
check("T2 uniform field -> ~0 deflection (|sum c| << typical |alpha|)", abs(cs.sum()) < 0.05 * typ)

# --- T3: kernel localized near source (b~support => crossover) ---
support = np.sum(np.abs(cs) * np.abs(mx - x_src)) / np.abs(cs).sum()
path_span = mx.max() - mx.min()
check("T3 kernel localized near source (support ~%.1f << path span ~%.1f)" % (support, path_span),
      support < 0.4 * path_span)
check("T3b fitted b-values {3..6} are ~ kernel support (crossover regime)",
      3.0 < support < 6.0)

# --- T4: crossover small-b vs coarse-H large-b signed falloff ---
sl_small = log_slope([3., 4., 5., 6.], [exact_edge_sum(edges, x_src, b) for b in [3., 4., 5., 6.]])[0]
sl_asym = log_slope([30., 45., 60., 80.], [exact_edge_sum(edges, x_src, b) for b in [30., 45., 60., 80.]])[0]
check("T4 crossover: |small-b slope| < |large-b slope| (%.2f vs %.2f)" % (sl_small, sl_asym),
      abs(sl_small) < abs(sl_asym))
check("T4b coarse-H large-b signed slope is near -2 (got %.2f, within 0.15)" % sl_asym, abs(sl_asym + 2.0) < 0.15)
check("T4c small-b slope is steeper than -1 but shallower than -2 (crossover, got %.2f)" % sl_small,
      -2.0 < sl_small < -1.0)

# --- T5: CONTROL -- non-cancelling kernel |c_e| gives large-b -> -1 (1/b) ---
def alpha_abs(b):
    r = np.hypot(mx - x_src, mz - b)
    return np.sum(np.abs(cs) / r)
sl_abs = log_slope([30., 45., 60., 80.], [alpha_abs(b) for b in [30., 45., 60., 80.]])[0]
check("T5 CONTROL: non-cancelling kernel |c_e| gives large-b -> -1 (1/b) (got %.2f)" % sl_abs,
      abs(sl_abs + 1.0) < 0.1)

# --- T6: fine-H source packet is pinned without rerunning the expensive certificate ---
check("T6 fine-H edge-kernel cache and JSON are present, fresh, and green",
      cache_green(H025_RUNNER, "TOTAL: PASS=12 FAIL=0") and h025_json_green())
check("T6b fine-H source-packet manifest cache is present, fresh, and green",
      cache_green(H025_MANIFEST_RUNNER, "TOTAL: PASS=5 FAIL=0"))

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("mechanism: monopole=%.4f support=%.2f small_b_slope=%.2f asym_slope=%.2f abs_kernel_asym=%.2f"
      % (mono, support, sl_small, sl_asym, sl_abs))
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
