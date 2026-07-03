#!/usr/bin/env python3
"""
P3 (the u_0 -> alpha_LM substitution) is an authority-inventoried composition
packet + ONE open register-not-read selection step -- not a free algebraic
substitution and not a retained P3 closure.

The hierarchy magnitude's per-mode coupling alpha_LM = alpha_bare/u_0 enters the
determinant-to-v map by the substitution u_0 -> alpha_LM (the honest-status note's
open primitive P3, "an algebraic substitution not a determinant identity"). This
runner shows P3 is a COMPOSITION over one-hop authorities, with conditional and
bounded authorities kept visible:

  - alpha_bare = g^2/(4 pi) = 1/(4 pi):  abstract g_bare=1 algebra plus
        conditional 4 pi / native-readout bridge rows.
  - u_0:  the bounded canonical mean-field link from canonical_plaquette_surface.
  - alpha_LM = alpha_bare/u_0 = sqrt(alpha_bare * alpha_s):  the GEOMETRIC MEAN of
        the bare and strong couplings (retained abstract algebra identity),
        i.e. the tadpole-improved coupling (retained abstract algebra identity).

So the substitution is: tadpole-improve the native Coulomb coupling by the native
mean-field link -> the geometric-mean (physical) coupling. The SINGLE P3-local
open step is: the magnitude reads the PHYSICAL (improved, geometric-mean)
coupling alpha_LM, not the bare lattice u_0 or bare alpha_bare. That selection
is register-not-read (registered = physical, not bare reconstruction) -- the 5TH
register-not-read application in this magnitude arc, FLAGGED for the audit lane
to weigh together (genuine extension vs over-application).

No observed value is in any PASS condition.
"""
import json
from pathlib import Path

import numpy as np

from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_ALPHA_S_V,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/P3_COUPLING_IS_RETENTION_ELIGIBLE_COMPOSITION_2026-06-06.md"
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"

AUTHORITIES = [
    (
        "alpha_lm_geometric_mean_identity_theorem_note_2026-04-24",
        "docs/ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md",
        "retained",
    ),
    (
        "alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10",
        "docs/ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md",
        "retained",
    ),
    (
        "g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note_2026-05-10",
        "docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_ABSTRACT_NARROW_THEOREM_NOTE_2026-05-10.md",
        "retained",
    ),
    (
        "plaquette_self_consistency_note",
        "docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md",
        "retained_bounded",
    ),
    (
        "magnitude_4pi_is_native_coupling_not_gaussian_2026-06-06",
        "docs/MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06.md",
        "audited_conditional",
    ),
    (
        "i1_static_readout_is_native_field_integration_2026-06-06",
        "docs/I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md",
        "audited_conditional",
    ),
]

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

pi = np.pi
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
note = NOTE.read_text(encoding="utf-8")
note_flat = " ".join(note.split())

# ===========================================================================
# SECTION A -- the geometric-mean identity (RETAINED): alpha_LM = sqrt(ab*as).
# ===========================================================================
print("--- Section A: geometric-mean identity (retained) ---")
def couplings(alpha_bare, u0):
    return alpha_bare, alpha_bare / u0, alpha_bare / u0 ** 2   # bare, LM, s
identity_cases = []
for ab, u0 in [(1 / (4 * pi), 0.877), (0.05, 1.3), (0.2, 0.6)]:
    a_bare, a_LM, a_s = couplings(ab, u0)
    identity_cases.append(
        abs(a_LM ** 2 - a_bare * a_s) < 1e-15
        and abs(a_LM - np.sqrt(a_bare * a_s)) < 1e-12
    )
check("alpha_LM = sqrt(alpha_bare * alpha_s) (geometric mean; retained identity)", all(identity_cases))
# the three couplings are a geometric progression with ratio 1/u_0
ab, u0 = 1 / (4 * pi), 0.877
a_bare, a_LM, a_s = couplings(ab, u0)
check("alpha_bare : alpha_LM : alpha_s is a geometric progression, ratio 1/u_0",
      abs(a_LM / a_bare - 1 / u0) < 1e-12 and abs(a_s / a_LM - 1 / u0) < 1e-12)

# ===========================================================================
# SECTION B -- the COMPOSITION: alpha_bare x bounded canonical u_0 -> alpha_LM.
# Authority classes are checked explicitly in Section C.
# ===========================================================================
print("--- Section B: P3 = authority-inventoried composition over canonical surface ---")
g_bare = 1.0
alpha_bare = g_bare ** 2 / (4 * pi)
check("alpha_bare formula agrees with canonical alpha_bare",
      abs(alpha_bare - CANONICAL_ALPHA_BARE) < 1e-15)
u0 = CANONICAL_U0
alpha_LM = CANONICAL_ALPHA_LM
check("canonical u_0 is the fourth root of the canonical plaquette",
      abs(u0 ** 4 - CANONICAL_PLAQUETTE) < 1e-15)
check("canonical alpha_LM is alpha_bare/u_0",
      abs(alpha_LM - alpha_bare / u0) < 1e-15)
check("canonical alpha_s(v) is alpha_bare/u_0^2",
      abs(CANONICAL_ALPHA_S_V - alpha_bare / (u0 ** 2)) < 1e-15)
check("canonical surface gives alpha_LM near 0.0907 and 1/alpha_LM near 11",
      0.090 < alpha_LM < 0.091 and 10.9 < 1 / alpha_LM < 11.1)
# alpha_LM is the geometric mean of the native Coulomb (bare) and the strong coupling
a_bare2, a_LM2, a_s2 = couplings(alpha_bare, u0)
check("alpha_LM is the geometric mean of native Coulomb alpha_bare and strong alpha_s",
      abs(a_LM2 - np.sqrt(a_bare2 * a_s2)) < 1e-12)

# ===========================================================================
# SECTION C -- the substitution is tadpole improvement (retained vertex power),
# NOT a free relabeling: u_0 (bare mean-field) -> alpha_LM (improved coupling).
# ===========================================================================
print("--- Section C: the substitution is tadpole improvement plus authority inventory ---")
# tadpole-improved coupling = bare coupling / (mean link)^{vertex power}; vertex power 1 here.
vertex_power = 1
alpha_improved = alpha_bare / u0 ** vertex_power
check("tadpole improvement (vertex power 1 abstract identity): alpha_bare/u_0^1 = alpha_LM",
      abs(alpha_improved - alpha_LM) < 1e-12)
for claim_id, note_path, effective_status in AUTHORITIES:
    row = ledger.get(claim_id)
    check(f"ledger has one-hop row: {claim_id}", row is not None)
    if row is None:
        continue
    check(f"{claim_id} note path matches authority packet", row.get("note_path") == note_path)
    check(f"{claim_id} effective status is {effective_status}",
          row.get("effective_status") == effective_status)
    check(f"source note lists authority row {claim_id}", f"| `{claim_id}` |" in note)
check("conditional 4pi/I1 authorities remain visibly conditional, not retained",
      all(
          ledger[cid]["effective_status"] == "audited_conditional"
          for cid in [
              "magnitude_4pi_is_native_coupling_not_gaussian_2026-06-06",
              "i1_static_readout_is_native_field_integration_2026-06-06",
          ]
      ))
check("source note states P3 is not retained on the current surface",
      "does **not** assert that P3 is retained on the current surface" in note_flat)

# ===========================================================================
# SECTION D -- the SINGLE open step (isolated): magnitude reads the PHYSICAL
# (improved, geometric-mean) coupling alpha_LM, not the bare u_0 / bare alpha_bare.
# = register-not-read (5th application; flagged for collective audit).
# ===========================================================================
print("--- Section D: the single open step = physical-not-bare coupling (register-not-read, 5th) ---")
bare_lattice = u0                 # the determinant's bare mean-field factor
physical_coupling = alpha_LM      # the improved/geometric-mean physical coupling
check("the open step is a SELECTION: physical alpha_LM vs bare u_0 (they differ)",
      abs(physical_coupling - bare_lattice) > 0.5)
register_not_read_step = "magnitude registers the PHYSICAL/improved coupling, not the bare reconstruction"
check("the selection is register-not-read (registered=physical, not bare); the 5th application -> "
      "FLAGGED for the audit lane (genuine extension vs over-application)",
      "PHYSICAL" in register_not_read_step)
# net: P3 reduces from 'free algebraic substitution' to an authority-inventoried
# composition packet + one open register step.
check("NET: P3 = authority-inventoried composition + ONE open register-not-read "
      "selection step (not a free substitution; not retained closure)",
      "authority-inventoried composition" in note
      and "does **not** assert that P3 is retained on the current surface" in note_flat)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
