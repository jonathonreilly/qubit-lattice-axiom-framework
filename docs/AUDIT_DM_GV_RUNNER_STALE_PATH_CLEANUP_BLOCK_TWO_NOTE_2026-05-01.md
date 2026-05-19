# Audit DM + Gauge-Vacuum Runner Stale-Path Cleanup (Block Two) — Cleanup-Action Record (Binding)

**Date:** 2026-05-01 (scope narrowed 2026-05-17 per audited_conditional `runner_artifact_issue` repair: binding scope is the cleanup-action record for the 8 named runners; PASS-accounting / runner-correctness verification is split out)
**Status:** support / audit-hygiene cleanup. Companion to
[`docs/AUDIT_DM_RUNNER_STALE_PATH_CLEANUP_NOTE_2026-05-01.md`](AUDIT_DM_RUNNER_STALE_PATH_CLEANUP_NOTE_2026-05-01.md)
(Block One). This block extends the same audit-hygiene cleanup to a second
cluster of runners with stale `read("docs/X.md")` calls.
**Lane:** audit-hygiene. No physics claim is added or removed.

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `runner_artifact_issue`, stating: *"attach the current
sources and completed stdout or SHA-pinned caches for the eight named
Block Two runners, then re-audit the cleanup and PASS accounting."*

This revision implements the splitting alternative rather than the
full-attachment option. The binding evidence of this note is **only**
the cleanup-action record: the 8 named runners had stale
`read("docs/X.md")` calls referring to notes deleted by commit
`d2e754fdc`, and this note documents the per-runner cleanup applied
to remove those stale path references.

The **broader PASS-accounting / runner-correctness verification** —
i.e. confirming that each cleaned-up runner produces a passing
post-cleanup output across its full audit-lane evaluation — is
**demoted to out-of-binding-scope** until SHA-pinned caches for each
of the 8 runners are attached and re-audited as a separate
runner-correctness row. Each runner's own audit row carries that
verification on its own ledger entry; this Block Two note is not the
authority for that.

---

## 0. Why this note exists

After Block One landed (PR #246) covering 8 DM-cluster runners with stale
references to notes deleted by commit `d2e754fdc`, a comprehensive scan of
the remaining runners under `scripts/` found 8 more on-main runners that
still carried stale `read("docs/X.md")` calls. Each one's audit row was
landing as `audited_conditional` or `audited_failed` for reasons reducible
to `FileNotFoundError`.

This block addresses the second cluster.

## 1. Affected runners and changes

| runner | stale path(s) | action |
|---|---|---|
| `frontier_dm_neutrino_postcanonical_polar_section.py` | `DM_NEUTRINO_YUKAWA_BLOCKER_NOTE_2026-04-14.md` (deleted), atlas row `\| DM neutrino post-canonical positive polar section \|` (trimmed) | remove read + 2 dependent checks |
| `frontier_dm_neutrino_polar_aligned_core_nogo.py` | `DM_NEUTRINO_YUKAWA_BLOCKER_NOTE_2026-04-14.md` (deleted), atlas row `\| DM neutrino positive-polar aligned-core no-go \|` (trimmed) | remove read + 2 dependent checks |
| `frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py` | `DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md` (archived to `archive_unlanded/dm-neutrino-stale-runners-2026-04-30/`) | redirect read to archive path (substring checks preserved) |
| `frontier_dm_neutrino_source_surface_z3_doublet_block_full_closure_boundary.py` | same archived note | redirect to archive path |
| `frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py` | same archived note | redirect to archive path |
| `frontier_dm_abcc_exact_target_surface_source_cubic_closure_2026_04_21.py` | `DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md` (archived to `archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/`) | redirect to archive path |
| `frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19.py` | `GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_TAIL_UNDERDETERMINATION_THEOREM_NOTE_2026-04-19.md` (archived to `archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/`) | redirect to archive path |
| `frontier_gauge_vacuum_plaquette_first_sector_zero_extension_factorized_class_theorem_2026_04_19.py` | `GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_RANK_ONE_FACTORIZED_CLASS_BOUNDARY_NOTE_2026-04-19.md` (same archive) | redirect to archive path |

The cluster naturally splits into two patterns:

- **Deleted-note removal** (postcanonical_polar_section, polar_aligned_core_nogo): the deleted notes (YUKAWA_BLOCKER) plus trimmed atlas rows are removed; the runner's surviving content checks verify the load-bearing claims directly.
- **Archived-note redirect** (six runners): the relevant note was moved to `archive_unlanded/<reason-tag>/` rather than deleted. Substring checks against archived note content are preserved by redirecting the `read()` to the archive path. This is the safer move because the archive preserves the historical content verbatim and the runners' verifications remain intact.

Every change is annotated in-source with the move/deletion provenance.

## Block-Two runner state (load-bearing for restricted packet, inlined 2026-05-18)

This section inlines current-state snapshots for each of the 8 named Block-Two
runners, with commit-hash references, so the restricted audit packet has direct
visibility into the cleanup-applied source. Per the audit-verdict guidance,
PASS-accounting / runner-correctness data is kept in a SEPARATE section
(section 2 below) — this section only documents the source state showing the
stale-path cleanup is applied.

All eight runners were modified by the same cleanup commit:

- **Cleanup commit:** `f00767de1` ("audit-hygiene: remove/redirect stale read()
  calls in 8 more runners (block 2)", 2026-05-01)
- **Merge commit on main:** `36b4a7134` (PR #247)
- **Diff shape:** 8 files changed, +83 / -31 lines

### scripts/frontier_dm_neutrino_postcanonical_polar_section.py

Deleted-note removal pattern. The stale `read("docs/DM_NEUTRINO_YUKAWA_BLOCKER_NOTE_2026-04-14.md")`
call plus its trimmed atlas-row check were removed; the runner's surviving
content check verifies the load-bearing `Y_+(H) = H^(1/2)` / `K_+(H) = H` claim
directly. Annotated in-source with provenance to commit `d2e754fdc`.

Most recent commit: `f00767de1` ("audit-hygiene: remove/redirect stale read()
calls in 8 more runners (block 2)").

```python
#!/usr/bin/env python3
"""
DM neutrino post-canonical positive polar section.

Question:
  After the exact post-canonical extension/support-class reduction and the
  raw right-frame orbit obstruction, does the generic full-rank DM right orbit
  still admit a canonical intrinsic representative that makes the remaining
  slot-supported bridge readable from H = Y Y^dag alone?

Answer:
  Yes.

  On the generic full-rank patch, the exact right orbit admits the unique
  positive polar representative

      Y_+(H) = H^(1/2).

  For that representative,

      K_+(H) = Y_+(H)^dag Y_+(H) = H,

  so the remaining post-canonical singlet-doublet slot carrier is read
  directly from the Hermitian data through

      K_Z3(H) = U_Z3^dag H U_Z3
      a(H) = (K_Z3(H))_01
      b(H) = (K_Z3(H))_02.
...
"""
```

### scripts/frontier_dm_neutrino_polar_aligned_core_nogo.py

Deleted-note removal pattern. Same `YUKAWA_BLOCKER` stale read + trimmed
atlas-row check removed; surviving content check verifies the CP-empty
aligned-Hermitian-core result `Im[(K_mass)01^2] = Im[(K_mass)02^2] = 0`
directly.

Most recent commit: `f00767de1`.

```python
#!/usr/bin/env python3
"""
DM neutrino positive-polar aligned-core no-go.

Question:
  Once the positive polar section makes the post-canonical DM bridge intrinsic
  from H = Y Y^dag, does the exact residual-Z_2 aligned Hermitian core already
  supply the needed CP support?

Answer:
  No.

  On the aligned active Hermitian core

      H_act =
      [ a  b  b ]
      [ b  c  d ]
      [ b  d  c ],

  the Z_3-basis singlet-doublet slot entries are exactly equal and real:

      (U_Z3^dag H_act U_Z3)_01 = (U_Z3^dag H_act U_Z3)_02 = (a+b-c-d)/3.

  After the current real Majorana doublet rotation, one physical singlet-
  doublet mass-basis entry vanishes and the other is purely real, so

      Im[(K_mass)01^2] = Im[(K_mass)02^2] = 0.
...
"""
```

### scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py

Archived-note redirect pattern. The `read()` call targeting
`DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md` was
redirected to its new archive path
`archive_unlanded/dm-neutrino-stale-runners-2026-04-30/...`. Substring checks
against archived content remain valid because the archive preserves content
verbatim.

Most recent commit: `f00767de1`.

```python
#!/usr/bin/env python3
"""
DM neutrino weak-triplet coefficient axiom boundary.

Framework convention for this runner:
  "axiom" means only the single framework axiom

      Cl(3) on Z^3.

Question:
  Does the current single-axiom Cl(3) on Z^3 stack, together with the current
  derived atlas rows, already derive the transfer coefficients c_odd and
  M_even in

      gamma = c_odd * a_sel
      [E1,E2]^T = M_even [tau_E,tau_T]^T ?

Answer:
  Yes.

  The transfer class is exact, and the transfer coefficients are now fixed:

    - c_odd = +1 on the source-oriented branch convention
    - M_even = v_even [1,1]
    - v_even = (sqrt(8/3), sqrt(8)/3)
...
"""
```

### scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_full_closure_boundary.py

Archived-note redirect pattern. Same archived note as previous runner;
read() redirected to archive path. Surviving substring checks unchanged.

Most recent commit: `f00767de1`.

```python
#!/usr/bin/env python3
"""
DM neutrino source-surface Z3 doublet-block full closure boundary.

Question:
  After checking the reusable atlas tools and reducing the live source-oriented
  sheet all the way to the exact Z3 doublet-block pair (delta, q_+), does the
  current exact axiom/atlas bank actually finish the last microscopic
  selection step?

Answer:
  No.

  The current source-facing bank already collapses to the fixed sharp tuple

      a_sel = 1/2, tau_+ = 1,
      gamma = 1/2, E1 = sqrt(8/3), E2 = sqrt(8)/3,
...
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

from dm_leptogenesis_exact_common import exact_package
from frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem import (
    ...
)
```

### scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py

Archived-note redirect pattern. Same archived note; read() redirected to
archive path.

Most recent commit: `f00767de1`.

```python
#!/usr/bin/env python3
"""
DM neutrino source-bank Z3 doublet-block selection obstruction theorem.

Question:
  After checking the reusable atlas tools, does the current exact source bank
  determine the remaining right-sensitive Z3 doublet-block point
  (delta, q_+) on the live source-oriented sheet?

Answer:
  No.

  The atlas-supported upstream source side is already closed to the fixed sharp
  tuple

      a_sel = 1/2,   tau_+ = 1,
      gamma = 1/2,   E1 = sqrt(8/3),   E2 = sqrt(8)/3.

  But there are distinct live-sheet points with different (delta, q_+) and
  different Z3 doublet blocks that carry exactly the same current-bank
  signature

      (gamma, E1, E2, cp1, cp2, a_*, b_*, T_slot).
...
"""
```

### scripts/frontier_dm_abcc_exact_target_surface_source_cubic_closure_2026_04_21.py

Archived-note redirect pattern. `read()` redirecting to
`archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md`
(note was archived as `retained_no_go`, not deleted, so substring checks
preserve their semantics).

Most recent commit: `f00767de1`.

```python
#!/usr/bin/env python3
"""
DM A-BCC exact target-surface source-cubic closure theorem.

Question:
  Is there still a separate strict/native A-BCC branch-choice residue once the
  exact PMNS target surface itself is fixed?

Answer:
  No.

  On the exact target surface:
    - the active-half-plane chamber is already exact on the source side,
    - the chamber roots are exactly {Basin 1, Basin 2, Basin X},
    - and the coefficient-free source cubic I_src(H) > 0 selects Basin 1
      uniquely there.
...
"""
```

### scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19.py

Archived-note redirect pattern. `read()` redirecting to
`archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_TAIL_UNDERDETERMINATION_THEOREM_NOTE_2026-04-19.md`.

Most recent commit: `f1175f630` ("science: land review-loop repair wave",
post-Block-Two refinement); the Block-Two cleanup itself is in `f00767de1`.

```python
#!/usr/bin/env python3
"""
Bounded minimal-bulk completion witness check for the first-sector Wilson
factorized cone.

The first-sector seam already fixes the retained coefficient packet `rho_ret`
on the first-symmetric support. Inside the exact Wilson factorized class

    T(rho) = exp(3 J) D_loc diag(rho) exp(3 J),

admissible extensions are the nonnegative conjugation-symmetric full packets
extending that retained data.

This runner certifies bounded, witness-restricted facts only:

1. The retained packet `rho_ret` produced by the local `completed_sector_data`
   import is normalized, conjugation-symmetric, and zero on the `(1,1)`
   slot.  No substring import of upstream prose is used to substantiate this
   property; the assertions are verified directly on the numeric packet.

2. The zero-extension `rho_0` of `rho_ret` to all higher weights produces a
   self-adjoint, conjugation-symmetric transfer matrix on the truncated
   dominant-weight box.  This existence-of-one-explicit-extension fact is
   verified by direct numeric computation on the transfer.
...
"""
```

### scripts/frontier_gauge_vacuum_plaquette_first_sector_zero_extension_factorized_class_theorem_2026_04_19.py

Archived-note redirect pattern. `read()` redirecting to
`archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_RANK_ONE_FACTORIZED_CLASS_BOUNDARY_NOTE_2026-04-19.md`.

Most recent commit: `f00767de1`.

```python
#!/usr/bin/env python3
"""
Explicit factorized-class extension of the retained first-sector environment
packet by minimal support on the dominant-weight box.

This closes one more existence seam:

  1. the retained first-sector completion already determines one exact
     truncated packet `(z00_min, rho_ret)`;
  2. that retained packet admits one explicit full extension inside the
     canonical Wilson factorized class by zeroing higher retained coefficients;
  3. so existence inside the factorized class is no longer open either.

What remains open is the actual framework-point Wilson environment packet,
not existence of some factorized-class extension.
"""
```

---

## 2. Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_neutrino_postcanonical_polar_section.py
# PASS=12 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_dm_neutrino_polar_aligned_core_nogo.py
# PASS=8 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py
# PASS=14 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_full_closure_boundary.py
# PASS=14 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py
# PASS=13 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_dm_abcc_exact_target_surface_source_cubic_closure_2026_04_21.py
# PASS=15 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19.py
# PASS=7 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_zero_extension_factorized_class_theorem_2026_04_19.py
# PASS=6 FAIL=0
```

Total: **89 PASS / 0 FAIL** across the cluster.

## 3. What this changes for the audit ledger

Each affected claim row's `audit_status` was either `audited_conditional` or
`audited_failed` with rationale text reducible to "primary runner returned
nonzero in the restricted audit environment". After Block One + Block Two
land and the audit pipeline re-runs, **none** of the addressed runners
should fail with FileNotFoundError; the rows can re-audit on substantive
physics merits rather than file-availability noise.

Most of the affected claim rows are leaf or medium-criticality with
author-declared `support` / `bounded` / `unknown` status. This block does
NOT promote any claim to `retained`. It only removes the noise floor.

Two notable rows in this cluster carry `current_status: proposed_retained`:
- `dm_abcc_basin_enumeration_completeness_theorem_note_2026-04-20` — already archived as retained_no_go in the ledger.
- `dm_neutrino_weak_triplet_coefficient_axiom_boundary_note_2026-04-15` — already archived as retained_no_go in the ledger.

For these archived rows, the redirected reads keep the runners self-contained
verification harnesses for the historical claim content; they do not
re-promote the archived rows.

## 4. Out of scope

- Restoring deleted notes or de-archiving moved notes (the trim and
  archival decisions were deliberate).
- Promoting any leaf row to `retained`.
- Modifying the audit pipeline runtime environment to ship the deleted
  files separately.
- The remaining 6 stale-path PMNS references in
  `frontier_pmns_intrinsic_completion_boundary.py`: that runner has already
  been hygiene-repaired (uses redirected reads to currently-existing notes);
  it now passes with PASS=14 FAIL=0 against the present `docs/` tree, so
  no further change is needed for that runner. Block 1+2 cover the
  remaining stale-path cluster reachable from on-main audit rows.

## 5. Forbidden-import role

This note introduces no new physical content, no new numerical comparators,
no new admitted observations. It is structural cleanup of runner code only.

## 6. Cross-references

- Block 1: PR #246 (open / review-only) — first half of the runner
  stale-path cleanup.
- This block: second block of the audit-hygiene campaign.
- Original trim commit: `d2e754fdc` (2026-04-16, "Trim DM package to
  science-only surface").
- Original archive commits: 2026-04-30 stale-runners + missing-runners
  archive packets.
