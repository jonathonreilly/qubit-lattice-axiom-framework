#!/usr/bin/env python3
"""DELTA0 S3 fixed-gap-spectrum no-go.

This runner checks the dedicated S3 boundary note:

    docs/HIERARCHY_DELTA0_S3_FIXED_GAP_SPECTRUM_NO_GO_NOTE_2026-06-18.md

It generalizes the NJL-style lattice-gauge-only gap equation from the
landed n=16 row to active taste count n, verifies that the leading-order
Kawamoto-Smit coupling produces no nontrivial gap roots for n=1..16,
and proves that a single fixed broken-phase coupling cannot produce a
constant alpha_LM rung ratio across more than one adjacent threshold.

No audit status is written; this is a source-side bounded theorem runner.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
NOTE = DOCS / "HIERARCHY_DELTA0_S3_FIXED_GAP_SPECTRUM_NO_GO_NOTE_2026-06-18.md"
PARENT_GATE = DOCS / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md"

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}][{klass}] {name}{suffix}")
    return condition


def residual(message: str) -> None:
    global RESIDUAL_COUNT
    RESIDUAL_COUNT += 1
    print(f"  RESIDUAL (declared-open): {message}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


P_BOUNDARY = 0.5934
U0 = P_BOUNDARY ** 0.25
C = 4.0 * U0 * U0
N_C = 3
G_LO = 1.0 / (2.0 * N_C)
ALPHA_BARE = 1.0 / (4.0 * math.pi)
ALPHA_LM = ALPHA_BARE / U0
ALPHA_S = ALPHA_BARE / (U0 * U0)


def dV_over_sigma(n: int, sigma: float, G: float) -> float:
    return 1.0 / G - n / (sigma * sigma + C)


def sigma_sq(n: int, G: float) -> float:
    return n * G - C


def g_crit(n: int) -> float:
    return C / n


def adjacent_ratio(n: int, G: float) -> float:
    num = sigma_sq(n - 1, G)
    den = sigma_sq(n, G)
    if num <= 0 or den <= 0:
        raise ValueError("adjacent roots must both be in the broken phase")
    return math.sqrt(num / den)


def g_star_for_ratio(n: int, alpha: float = ALPHA_LM) -> float:
    a2 = alpha * alpha
    return C * (1.0 - a2) / (n - 1.0 - a2 * n)


section("A. Note and scope discipline")
note = NOTE.read_text(encoding="utf-8")
parent = PARENT_GATE.read_text(encoding="utf-8")
note_flat = " ".join(note.split())
parent_flat = " ".join(parent.split())

required_note_markers = [
    "# Hierarchy DELTA0 S3 Fixed-G Gap-Spectrum No-Go",
    "**Claim type:** bounded_theorem",
    "**Status authority:** independent audit lane only.",
    "This source note does not set or predict an audit outcome",
    "does not eliminate threshold-dependent, EW-driven, or non-NJL transport mechanisms",
    "The DELTA0 gate remains open.",
    "does not modify the route inventory",
    "S3 itself is not globally eliminated",
    "## No-Go Discipline Gate",
    "N1 -- alternative route enumeration",
    "N2 -- wall independence",
    "N3 -- hidden-wall scan",
    "N4 -- residual matching",
    "N5 -- rhetoric audit",
    "N6 -- partial-closure path scan",
    "N7 -- steelman",
    "N8 -- cross-cycle echo",
    "Gate result: PASS for the narrowed fixed-`G` NJL gap-spectrum no-go",
]
for marker in required_note_markers:
    check("A", f"note contains marker: {marker}", marker in note or marker in note_flat)

forbidden_note_markers = [
    "observed target mass",
    "promoted to " + "retained",
    "retained on the actual " + "surface",
    "source-note proposal",
    "audit_status",
]
for marker in forbidden_note_markers:
    check("B", f"note avoids forbidden/overclaim marker: {marker}", marker not in note)

section("B. Generalized NJL active-taste algebra")
for n in (1, 2, 8, 16):
    sig2 = sigma_sq(n, g_crit(n))
    check("A", f"G_crit({n}) makes sigma_n^2 vanish", abs(sig2) < 1e-12, f"sigma2={sig2:.3e}")

sample_n = 11
sample_G = 0.9
sample_sigma_sq = sigma_sq(sample_n, sample_G)
sample_sigma = math.sqrt(sample_sigma_sq)
check(
    "A",
    "gap equation vanishes at sigma_n^2 = n G - 4 u_0^2",
    abs(dV_over_sigma(sample_n, sample_sigma, sample_G)) < 1e-12,
    f"n={sample_n}, G={sample_G}, sigma2={sample_sigma_sq:.6f}",
)
check(
    "A",
    "nontrivial root exists iff G > G_crit(n)",
    sigma_sq(10, g_crit(10) * 1.01) > 0 and sigma_sq(10, g_crit(10) * 0.99) < 0,
)
check("A", "alpha constants form the expected hierarchy", ALPHA_BARE < ALPHA_LM < ALPHA_S, f"{ALPHA_BARE:.7f} < {ALPHA_LM:.7f} < {ALPHA_S:.7f}")
check("A", "alpha_LM = alpha_bare/u_0", abs(ALPHA_LM - ALPHA_BARE / U0) < 1e-15)
check("A", "alpha_s = alpha_bare/u_0^2", abs(ALPHA_S - ALPHA_BARE / (U0 * U0)) < 1e-15)

section("C. Leading-order lattice-gauge-only S3 has no threshold spectrum")
lo_sigmas = {n: sigma_sq(n, G_LO) for n in range(1, 17)}
max_n = max(lo_sigmas, key=lo_sigmas.get)
check("B", "canonical N_c=3 gives G_LO=1/(2 N_c)=1/6", abs(G_LO - 1.0 / 6.0) < 1e-15)
check("B", "all n=1..16 leading-order sigma_n^2 are negative", all(v < 0 for v in lo_sigmas.values()))
check("B", "largest leading-order root test is n=16", max_n == 16, f"max_n={max_n}")
check(
    "B",
    "sigma_16^2 = 16/6 - 4 u_0^2 is the recorded symmetric-phase value",
    abs(lo_sigmas[16] + 0.414602) < 2e-4,
    f"sigma16^2={lo_sigmas[16]:.6f}",
)
check("B", "G_LO is below the n=16 threshold", G_LO < g_crit(16), f"G_LO={G_LO:.6f}, Gcrit16={g_crit(16):.6f}")
check("B", "G_LO is below every active-taste threshold", all(G_LO < g_crit(n) for n in range(1, 17)))
check("B", "therefore no adjacent leading-order ratio is constructible", all(lo_sigmas[n] <= 0 or lo_sigmas[n-1] <= 0 for n in range(2, 17)))

section("D. Fixed-G broken-phase extension cannot supply constant alpha_LM")
gstars = {n: g_star_for_ratio(n) for n in range(2, 17)}
for n, gstar in gstars.items():
    r = adjacent_ratio(n, gstar)
    check("C", f"G_star({n}) realizes alpha_LM for that one step", abs(r - ALPHA_LM) < 1e-12, f"G*={gstar:.6f}, ratio={r:.7f}")

unique_gstars = len({round(v, 12) for v in gstars.values()})
check("D", "G_star(n) values are unique over n=2..16", unique_gstars == 15)
check("D", "G_star decreases with n because alpha_LM^2 != 1", all(gstars[n] > gstars[n + 1] for n in range(2, 16)))
check("D", "no single fixed G can realize alpha_LM for both n=16 and n=15", abs(gstars[16] - gstars[15]) > 1e-3, f"G16={gstars[16]:.6f}, G15={gstars[15]:.6f}")
check("D", "full forced-G range is threshold-dependent by more than 10x", gstars[2] / gstars[16] > 10.0, f"range={gstars[2] / gstars[16]:.2f}x")
check("D", "low-threshold forced G exceeds leading-order G by O(10)", gstars[2] / G_LO > 10.0, f"G*_2/G_LO={gstars[2] / G_LO:.2f}")

section("E. Parent-gate context and residuals")
check(
    "C",
    "parent gate records S3 context handle",
    "HIERARCHY_DELTA0_S3_FIXED_GAP_SPECTRUM_NO_GO_NOTE_2026-06-18.md" in parent,
)
check(
    "C",
    "parent gate still says the gate is open",
    "named gap: B4 attachment-observable identification" in parent_flat
    and "does not derive the attachment-observable identification" in parent_flat,
)
check(
    "C",
    "note dependencies include route inventory and NJL authorities",
    "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_SYNTHESIS_NOTE_2026-06-11.md" in note
    and "V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md" in note,
)
check(
    "C",
    "note leaves threshold-dependent and EW mechanisms open",
    "threshold-dependent" in note_flat and "EW-sector" in note_flat,
)
check("C", "no electroweak VEV literal is consumed", "246" not in note and "125" not in note)
audit_ledger_token = "AUDIT" + "_LEDGER"
check("C", "runner source does not write audit ledgers", audit_ledger_token not in Path(__file__).read_text(encoding="utf-8"))

residual("Threshold-dependent G_n or EW-driven gap equations remain open; this runner does not derive or rule them out.")
residual("Non-NJL direct transport rules remain open; this runner only prunes the fixed-G NJL gap-spectrum arm of S3.")

print("\nVERDICT: S3 fixed-G lattice-gauge-only gap-spectrum arm is pruned within stated scope; DELTA0 remains open.")
print(
    "Breakdown: "
    + " ".join(f"{k}={v}" for k, v in CLASS_COUNTS.items())
    + f" RESIDUAL={RESIDUAL_COUNT}"
)
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")

if FAIL_COUNT:
    sys.exit(1)
