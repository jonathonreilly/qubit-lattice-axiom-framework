# Audit-Unlock Keystone Map — Drain the DAG in Maximum-Cascade Order

**Date:** 2026-06-06
**Type:** audit-pipeline analysis / tooling
**Claim type:** meta
**Status:** an analysis + reproducible tool for the audit lane; sets no audit
status, changes no audit verdict. Recommends a dispatch ORDER; the audit lane owns
adoption. **Status authority:** independent audit lane only.
**Runner:** [`scripts/audit_unlock_keystone_map_2026_06_06.py`](../../scripts/audit_unlock_keystone_map_2026_06_06.py)
(`TOTAL: PASS=10 FAIL=0`; reproducible — re-run as the DAG drains to regenerate the
next priority list).

## The question

"Unlock more of the audit" — why are ~1330 rows unaudited, and what is the
highest-leverage way to get more of them audited?

## Diagnosis (computed from the live ledger)

The backlog is **not** blocked by physics or by broken wiring; it is a **dependency-DAG
drain** problem.

| fact | value |
|---|---|
| total rows | 2993 |
| need-audit (`audit_status` unaudited / in-progress) | **1643** |
| blocking (unaudited **and** non-ready effective_status) | 1330 |
| **broken dependency edges** (wiring bugs) | **0** |
| rows carrying a recorded `blocker` | **2** |
| READY-now (all deps already retained-grade → auditable immediately) | **93** |
| not-ready, waiting **solely** on unaudited deps (unlock as DAG drains) | **1213** |

The auditor (per `compute_audit_queue.py`) can only mark a row `ready` once **all its
deps are at retained-grade**. So 1213 of the blocked rows are simply waiting for
their deps to be audited — the DAG must be drained from the roots up. Only **93**
rows are auditable right now, and the dispatch queue surfaces ~10 at a time, sorted
ready-first + criticality but **not by downstream fanout**.

## The lever: audit ORDER (keystone-first)

The single highest-leverage move is to audit the **high-fanout ready keystones
first** — the auditable-now rows whose audit unblocks the most downstream rows.
Computed downstream-blocker fanout (runner Section C):

| unlocks (downstream blocked rows) | criticality | row |
|---:|---|---|
| **942** | critical | `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-0...` |
| **761** | critical | `alpha_s_derived_note` |
| **709** | critical | `yt_ward_identity_dependencies_registered_bound_narrow_theorem...` |
| **614** | critical | `cl3_taste_generation_theorem` |
| **526** | critical | `higgs_channel_effective_ntaste_boundary_bounded_note_2026-05...` |
| 435 | critical | `pmns_twisted_flux_transfer_holonomy_boundary_note` |
| 301 | critical | `quark_projector_ray_phase_completion_note_2026-04-18` |
| 276 | critical | `koide_higgs_dressed_resolvent_root_theorem_note_2026-04-20` |
| 237 | critical | `g_bare_constraint_vs_convention_restatement_note_2026-05-07` |
| 226 | critical | `koide_full_lattice_schur_inheritance_note_2026-04-18` |
| 221 | critical | `koide_taste_cube_cyclic_source_descent_note_2026-04-18` |
| 187 | high | `higgs_mass_from_axiom_status_correction_audit_note_2026-05...` |

**The top-5 ready keystones together gate 1050 distinct blocked rows — 79% of the
backlog.** Auditing these five (all `critical`, all auditable now) opens the audit
path for nearly four-fifths of the unaudited ledger. They are the framework's
foundational theorems (staggered-Dirac forcing, the strong coupling, the Ward-identity
dependency registration, taste-generation, the Higgs taste channel), which is exactly
why their fanout is enormous.

## Recommended actions (for the audit lane)

1. **Dispatch the top ready keystones first.** Re-order the dispatch queue to put the
   high-fanout ready rows (this table) at the head. Concretely: add a **downstream-
   blocker-fanout tiebreaker** to `compute_audit_queue.py` / `compute_audit_dispatch_queue.py`
   (currently ready-first + criticality; fanout is the missing signal). The runner here
   computes that fanout and can seed it.
2. **RESOLVE THE KEYSTONE CYCLES FIRST (prerequisite for #1).** Three of the top
   keystones sit in **mutual-dependency 2-cycles**, so they can **never become `ready`**
   (each waits on the other) — the dispatch never reaches them via the ready-DAG, and the
   keystone unlock in #1 is blocked until the cycle is resolved. **These are GENUINE
   mutual dependencies, not spurious edges** — verified 2026-06-06 by reading each note's
   amendment context (below). In every case the older note was deliberately amended to
   rest on its newer repair for a load-bearing piece, so **no edge can be cut without
   deleting a real dependency.**

   | keystone 2-cycle (genuine mutual dep `A ↔ B`) | max fanout | why BOTH edges are real |
   |---|---:|---|
   | `axiom_first_reflection_positivity_theorem` ↔ `rp_wilson_temporal_gauge_bridge_sign_and_positivity_repair` | **949** | repair→theorem: the repair fixes the theorem's failed Wilson bridge (sign root `S_0:=-β Re Tr`). theorem→repair: the 04-29 note was amended so its "Wilson-plane sign and character-kernel source packet **is supplied by**" the repair. Both load-bearing. |
   | `observable_principle_from_axiom_note` ↔ `observable_principle_positive_source_cone_p2_elimination` | **765** | elimination→parent: the bridge narrows the parent principle. parent→elimination: the parent's "**load-bearing** P2 repair **is** the positive-source-cone bridge" (`det(D+J)∈ℝ_{>0}`). Both load-bearing. |
   | `staggered_dirac_kawamoto_smit_conditional_realization` ↔ `staggered_dirac_chirality_parity_bridge` | **256** | parity→conditional: the bridge extends the conditional. conditional→parity: the 2026-06-06 repair "**replaces that free premise with** the narrow chirality-parity bridge." Both load-bearing. |

   The correct resolution is therefore **joint audit**, not a graph edit: treat each
   repair-pair as one logical unit and audit it together (closing it as
   `retained_pending_chain`), which the `cycle_break_targets` machinery already supports.
   That makes the RP, observable-principle, and staggered-Dirac keystones auditable —
   directly enabling the ~949 / ~765 / ~256 cascades. **(Correction 2026-06-06: an earlier
   draft of this note recommended *cutting* the older→newer edge as "anachronistic." That
   was wrong — reading the notes shows the amendment makes that edge a real dependency.
   Cutting it would corrupt the graph; joint audit is the right mechanism.)**
3. **Iterate.** After each keystone is audited (its deps become retained-grade for the
   layer below), re-run this runner — the next layer of keystones surfaces. The DAG
   drains in ~log-depth waves rather than one-at-a-time.

## Secondary unlocks

- **The remaining 12 (minor) cyclic SCCs** (max-fanout ≤ 28: the Born/Lüders record
  cluster, the beta6-plaquette clusters, the qubit-foundations cluster). Lower leverage
  than the three keystone cycles above; break via `cycle_break_targets`
  (`missing_dependency_edge` naming or a `retained_pending_chain` closure) as the DAG
  drains toward them.
- **160 gated/dropped sources** (`stats.dropped_gated_sources`; cf.
  `never_gate_source_paths.txt`). These are excluded from the audit entirely. Reviewing
  which are gated for a stale reason and ungating the eligible ones recovers them.

## Scope / non-claims

- Sets **no** audit status and changes **no** verdict; it recommends a dispatch ORDER
  and provides the tool to compute it. The audit lane owns adoption.
- Does **not** assert any keystone WILL pass audit — only that auditing it (whatever
  the verdict) unblocks its downstream readiness computation.
- The fanout numbers are as-of the current ledger and DRIFT as auditing proceeds; the
  runner is the reproducible source of truth (re-run for the live priority).
- No physics claim; no new axiom/import.

## Validation

`scripts/audit_unlock_keystone_map_2026_06_06.py` (`PASS=10 FAIL=0`): Section A (the
backlog is DAG-drain — 0 broken edges, ~0 recorded blockers), Section B (93 ready-now;
1213 waiting solely on unaudited deps), Section C (the keystone priority; top-5 gate
≥60% of the backlog; all critical), Section D (20 cycles + 160 gated sources as
secondary unlocks).

## Reading rule

The audit backlog is a dependency-DAG drain, not a wall. Maximum throughput =
audit the high-fanout READY keystones first (this map; top-5 → 79% cascade), resolve
the dep-cycles by JOINT audit (`retained_pending_chain` — they are genuine mutual deps,
not cuttable edges), and review the 160 gated sources. Re-run the runner after each
wave for the next priority layer.
