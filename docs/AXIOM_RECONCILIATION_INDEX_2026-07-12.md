# Axiom-Reconciliation Index — Fresh Scan And Triage Of Pre-Reset Surfaces (2026-07-12)

**Date:** 2026-07-12
**Type:** meta
**Status:** campaign index for the axiom-reconciliation campaign (started
2026-07-03). Detection and classification only: this note proposes repairs
and flags audit-lane items; it changes no claim, no status, and no axiom
content.
**Status authority:** sets no audit status; the independent audit lane owns
all row statuses.
**Primary tool:**
[`scripts/axiom_reconciliation_rescan_2026_07_12.py`](../scripts/axiom_reconciliation_rescan_2026_07_12.py)
(regenerable; writes
[`logs/runner-cache/axiom_reconciliation_rescan_2026_07_12.tsv`](../logs/runner-cache/axiom_reconciliation_rescan_2026_07_12.tsv))
**Triage evidence:** `logs/runner-cache/recon_triage/*.tsv` (30 batch files,
one row per classified file)

## Context

The 2026-06-29 foundation reset replaced the three-axiom set (Lattice,
Quantum, Record — Record read as durable realized-outcome registration with
a `K`/CPT-orbit reading in a supplied readout context) with the current four
axioms (Lattice, Qubit, Admissibility, Record) in
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), and the
2026-07-04 revision appended the formation sentence "Records form." The
campaign's first two blocks (PR #4908, PR #4910, and the guard re-keys landed
as commit `71cc2ec52`) restored the mechanical baseline: all axiom-live-guard
runners green as of 2026-07-03.

The campaign's working index from 2026-07-03 was a session artifact and was
never banked. This note replaces it with a REGENERABLE scan so the index can
never be lost again: needle categories are derived from the superseded memo
texts and from the phrase list in the PR #4887 repair record, and every hit
file is joined to its audit-ledger row by `note_path`.

## Scan result (at `7b9260b85`, 2026-07-12)

Scanned: 8,583 files (`docs/**/*.md` except `docs/audit/data/`, plus
`scripts/*.py`).

- **146 live hard-needle files** (102 notes, 44 scripts): superseded Record
  wording or legacy axiom-set naming outside marked-historical files.
  Of these, 8 carry retained audit status (see the audit-lane flag below)
  and 47 have no ledger row (scripts and non-claim docs); the rest are
  unaudited or in progress.
- **739 soft-only files**: only superseded-memo citations or generic
  legacy naming. Dated split: 607 pre-reset, 131 undated legacy-era, and
  2 post-reset scripts — both of which turned out to be deliberate
  absence-guards (they assert that superseded memo links are GONE from
  their notes), i.e. zero real post-reset drafting slips.
- 8 files intentionally excluded as historical/campaign authority (the
  `MINIMAL_AXIOMS_*` lineage, `docs/audit/AXIOM_MINIMALITY_POLICY.md`, and
  this index note, which quotes the needles as documentation).

Scan correction (2026-07-12, same day): the first scan pass used
literal-space needles, and this repo hard-wraps prose — a stale phrase
broken across a line escaped detection. Found live when a re-keyed runner
needle failed against `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`
(whose firewall paragraph wraps "durable realized-outcome registration").
All multi-word needles are now whitespace-tolerant; the fix surfaced five
additional hard files (three REKEY — the objectivity note itself, repaired
in the Block 6 wave; the Darwinism-bridge residual note; the
magnitude-reads note — and two CONTENT-FLIP — the native-carrier
registration-kernel note, a post-reset note still using the central-sector
reading, and the PMNS TM2 runner, which joins its note in the flip set).

## Classification (triage of all 146 hard files)

Each hard file was classified by a bounded worker pass (rubric frozen in the
campaign pack; every row carries evidence line numbers, a representative
stale quote, and a proposed fix) and line-reviewed by the supervising agent.
Classes:

- **REKEY** — argument survives the landed text; mechanical
  quote/needle/citation refresh.
- **CONTENT-FLIP** — a load-bearing premise or the verdict itself uses
  deleted or changed axiom content; needs a refutation-seat re-derivation.
- **REOPENED-WALL** — a no-go whose blocking premise was the old wording;
  the wall may not survive the landed text.
- **HISTORICAL-OK** — old wording as marked historical context only.
- **DELIBERATE-OLD-TEXT** — runner references old wording by design (flip
  demonstrations, absence guards).

Counts over the 146 hard files:

- **CONTENT-FLIP**: 27
- **REOPENED-WALL**: 15
- **REKEY**: 88
- **DELIBERATE-OLD-TEXT**: 3
- **HISTORICAL-OK**: 13

### CONTENT-FLIP (27)

- `docs/ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md` — Recast the result as a conditional downstream readout-context bridge and replace the old Record dependency with retained authorities for central sectors and K/CPT orbit structure.
- `docs/FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md` — Split off F1 or add a retained readout-context bridge proving that local U(3) leaves record content and readout fixed; otherwise narrow the theorem to F2-F4 and refresh the axiom citation and names.
- `docs/GENERATION_DIAL_DYNAMICS_STABILITY_CLASSIFIER_2026-06-05.md` — Rebuild the record-sector premise from landed Record additivity plus separate retained sector/K-CPT authorities; rename Quantum to Qubit and include Admissibility.
- `docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md` — Recast the result as conditional on separately supplied K/CPT-real two-sector readout authority, then update the four axiom names.
- `docs/KCPT_ORBIT_CLAUSE_KINVARIANT_SURFACE_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-10.md` — Rescope this as a conditional downstream K/CPT-context equivalence and remove all claims that it locates or rewrites landed Record content.
- `docs/KOIDE_KODIM_REAL_STRUCTURE_ROUTE_EMPTY_R_UNDETERMINED_BOUNDED_NO_GO_NOTE_2026-06-08.md` — Re-prove both candidate readouts satisfy Qubit, Admissibility, record-content determination, and finite disjoint-record additivity, or narrow the conclusion to J-silence.
- `docs/OBSERVABLE_PRINCIPLE_P1_REGISTRATION_REALIZATION_PIN_CONSOLIDATION_NARROW_THEOREM_NOTE_2026-06-11.md` — Rebuild the record model and REG-site witnesses under landed site-local admissible Record semantics, then restate the consolidation and formation boundary from the resulting verdict.
- `docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md` — Recast K/CPT orbit and central-sector structure as a separately supplied bridge, then re-prove the dictionary claims for admissible record content.
- `docs/PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md` — Move central-sector selection/dephasing to an explicit downstream bridge and make the theorem conditional, or re-prove the map from landed Admissibility and Record content.
- `docs/RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md` — Rewrite the theorem around admissible-possibility locking and make K/CPT orbit typing a separately supplied condition.
- `docs/RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md` — Reframe as a conditional K/CPT-orbit theorem and supply a separate retained bridge from record content to orbit-valued readout.
- `docs/RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md` — Recast the principle as a separate conditional readout bridge requiring independent authority; do not attribute it to Record.
- `docs/RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md` *(covered by open PR)* — Rebuild the interface as Qubit to Admissibility to formation to permanent record, and require separate support for any finite orbit alphabet.
- `docs/RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md` — Reprove arbitrary finite nonzero atom availability under simultaneous nearest-neighbor Admissibility, or narrow the schema to explicitly supplied admissible records; rekey the memo and Qubit name.
- `docs/SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md` — Rebuild the boundary from the landed Qubit/Admissibility/Record text and recheck whether local admissibility or record content bears on exchange sign.
- `docs/THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md` — Rework the theorem to make K/CPT-orbit constancy a separately supplied downstream premise, refresh the axiom citation, and reassess the verdict.
- `docs/UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md` — Redefine P-dep from current record content, keep K/CPT and sector data explicitly supplied, and reprove and rerun B1-B3.
- `scripts/frontier_dynamics_sort_records_accumulate_2026_07_03.py` — Rebuild the locking predicate from the landed admissible-local-possibility semantics and reassess every dependent witness and conclusion.
- `scripts/frontier_edge_two_site_framing_no_native_color_route_record_text_2026_06_08.py` — Retarget Part 3 to the 2026-06-29 memo, rewrite its Record checks and verdict, and reassess the paired note.
- `scripts/frontier_eident_decomposition_ctx_match_2026_07_02.py` — Replace the old axiom-derived outcome anchor with separately supported context content and re-evaluate the CTX match.
- `scripts/frontier_occupancy_atom_outcome_dictionary_2026_06_12.py` — Rebuild the outcome dictionary from record content or a separately retained readout-context bridge, then update the memo link inventory.
- `scripts/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.py` — Point to the 2026-06-29 memo and add a supplied/verified admissibility premise before identifying instrument outcomes with record atoms.
- `scripts/frontier_record_production_interface_principle_2026_06_06.py` *(covered by open PR)* — Repoint the memo/citation and make admissibility filtering an explicit formation-stage premise before one-hot outputs are typed as records.
- `scripts/generation_weight_dial_structure_2026_06_05.py` — Recast the result as conditional on a separately retained central-sector/K/CPT bridge, rekey the four axioms, and recheck the open-position claim.
- `scripts/record_outcome_observable_principle_runner.py` — Make the result conditional on separate retained central-sector, K/CPT, and record-map/readout authorities; remove the axiom-direct claim.

- `docs/NATIVE_CARRIER_REGISTRATION_KERNEL_RATE_VS_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md` — Reopen the kernel derivation: derive the neighbor-conditioned admissible sector set and recompute, or state full central resolution as a supplied bridge premise.
- `scripts/pmns_tm2_trimaximal_from_record_central_sector_runner.py` — Recast the runner as conditional on an explicit central-sector dephasing/K-reality bridge and remove the verdict that the trimaximal column follows from Record alone.

### REOPENED-WALL (15)

- `docs/EDGE_TWO_SITE_FRAMING_SUPPLIES_NO_NATIVE_COLOR_ROUTE_RECORD_TEXT_NARROW_NO_GO_NOTE_2026-06-08.md` — Reopen the no-go under the four axioms; rebuild G-B/G-C around admissible local record content and update the runner's authority needles.
- `docs/EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md` — Rebuild both completions with identical landed Qubit, Admissibility, admissible-locking, uniqueness, permanence, and readout data; remove central-sector/K-CPT premises and rerun the no-go.
- `docs/KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md` — Recast the orbit quotient and phase-resolution exclusion as conditional on a separate retained K/CPT readout-context bridge, or remove the claimed Record entailment.
- `docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md` — Reopen Conclusion C and the aggregate no-go; either mark it historical to the old Record text or supply a new K/CPT-to-record bridge and re-prove it.
- `docs/P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md` — Reopen and rerun the Record/Admissibility supplier leg under the landed locking and content-only-readout clauses, then restate the no-go only if branch non-selection is freshly shown.
- `docs/QUARK_ROUTE2_RECORD_RAW_Q_SELECTOR_GATE_NOTE_2026-06-21.md` — Reopen the raw-q selector proof under content-only readout and distinguish failure of q to equal additive I from failure of Record to permit or select a derived quotient.
- `docs/SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md` — Rebuild the countermodel with an explicit covariant nearest-neighbor admissibility rule and prove the factor flows and records preserve it, or withdraw/rescope the no-go.
- `docs/STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md` — Reopen the wall and enumerate or prove survivor multiplicity under the landed Admissibility rule; otherwise narrow the claim conditionally.
- `docs/STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md` — Rerun or narrow the chirality-survivor protocol under landed Admissibility, retain the unaffected limbs, and refresh the memo/name.
- `docs/STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md` — Reopen the CPT branch, require a separate retained K/CPT/readout-context authority, and refresh the axiom-set name and memo citation.
- `scripts/audit_companion_strong_cp_gauge_theta_not_forced_by_reality_positivity_cpt_exact.py` — Reframe the wall against the landed axioms: remove the Record/CPT identification, address the new admissibility-and-record constraints or bound the claim to a standard-CPT toy model, and update the axiom names.
- `scripts/frontier_exercise_spin_statistics_fs_admission_located_2026_06_06.py` — Reopen the wall under all four axioms and replace the central-sector-silence checks with a new admissibility-aware argument.
- `scripts/frontier_koide_r_polarization_orbit_quotient_2026_06_09.py` — Reopen K3: remove the Record-derived exclusion, or restate it conditionally on a separate retained K/CPT-orbit readout context.
- `scripts/generation_dial_occupancy_free_input_2026_06_05.py` — Rebuild the independence proof against Lattice/Qubit/Admissibility/Record and retain the free-r conclusion only if admissibility cannot constrain it.
- `scripts/one_time_dimension_dt1_reduction_check_2026_06_17.py` — Rebuild the countermodel under all four current axioms, including nearest-neighbor admissibility and record locking, before retaining the d_t=1 open-gate conclusion.

### REKEY (88) — full list in the triage TSVs

### No-fix classes

- DELIBERATE-OLD-TEXT: 3 files (listed in the triage TSVs)
- HISTORICAL-OK: 13 files (listed in the triage TSVs)

A reopened wall is not a reversed verdict. For each wall, the walls block
must determine the direction of consequence before any edit. Some walls
closed derivation routes — the record-stiffness context-independence no-go
and the staggered-chirality free-selector wall are the clearest cases —
and for those, reopening under the landed Admissibility rule is a potential
opportunity, not damage. Others lose only a branch premise while the
conclusion survives or strengthens: the strong-CP note's CPT branch used
the deleted Record `K`/CPT-orbit reading as its blocking premise, and with
no axiom-supplied `K`/CPT structure at all, the branch restates to an even
weaker forcing route (verified by direct read during this triage). Each
wall file gets an explicit direction line in its repair block.


## Files already owned by open PRs (skipped by the waves)

- `docs/POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md`
  and its runner — PR #5208.
- `docs/PWC_DERIVATION_FROM_CUMULANT_GENERATING_FUNCTIONAL_NARROW_THEOREM_NOTE_2026-05-22.md`
  and `docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md` — PR #5156.
- `docs/RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md` and its runner —
  PR #5222.
- `docs/SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-17.md`
  — PR #5216.

## Live-guard drift measured on today's main

Re-running the five runners repaired in Blocks 1–2 found two have drifted
back to failing since 2026-07-03 — both needle drift, not science
regressions:

- `scripts/acphilambda_ambient_equivariant_heat_trace_face_2026_07_02.py`
  (PASS=79 FAIL=2): PR #5184 rewrote the C3 fixed-locus supplier note and
  dropped the two exact sentences this runner pins. The rewritten supplier
  still derives the `2/9` density and still states the readout exclusion
  ("No physical single-summand readout is derived."), so the repair is a
  re-pin of both needles plus the consumer note's quote. Queued for Wave 1.
- `scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py`
  (PASS=79 FAIL=2): the premise-node disclaimer sentence moved again and
  the "current snapshot" row-count pin is stale (17 → 22). The file is
  owned by open PR #5208; left to that PR, with this drift noted for its
  reviewer.

## Audit-lane flag (no action taken here)

Eight hard-needle files carry retained audit status (4 `audited_clean`,
4 `audited_conditional`). This is a structural gap, now precisely locatable:
`docs/audit/scripts/invalidate_stale_audits.py` triggers on changes to the
audited artifact (note hash, runner hash, classifier class, no-go packets) —
it has no trigger for "the axiom authority this note quotes was superseded."
Rows audited before 2026-06-29 against pre-reset axiom text therefore retain
status even though their quoted axiom surface no longer exists. The eight
files are listed in the scan TSV (`RETAINED_STATUS_HARD` block of the runner
output). Handing to the audit lane: either a reset-boundary invalidation
trigger, or targeted re-audit of the eight rows.

## Soft-only policy (740 files)

No mechanical mass-edit. The pre-reset and undated files cite the memo that
was current when they were written; their reconciliation burden is already
carried by their ledger rows (overwhelmingly unaudited), and a 738-file
citation swap would churn history, invalidate runner needles, and change no
live claim. The two post-reset hits are deliberate absence-guards needing
nothing. Fresh surfaces are already covered by the guard pattern those two
scripts implement. Soft-only files re-enter scope one at a time when their
rows are audited or their content is next touched.

## Wave plan (Blocks 4+)

1. **Wave 1 — live-guard and retained-status re-keys**: the drifted
   heat-trace runner re-pin plus the four REKEY-classed, non-covered
   members of the retained-status eight (they carry live audit status):
   the RP two-step transfer-positivity note, the blocked time-normalization
   bridge note, the RP/P2 gauge-extension residual note, and the Wilson
   small-`a` matching note.
2. **Waves 2+ — mechanical re-keys per lane** (REKEY class), one PR per
   lane wave, stacked on this branch, every wave re-running the affected
   runners plus `vocab_lint` before commit.
3. **Content flips**: each CONTENT-FLIP file gets a refutation-seat
   re-derivation under the landed text (worker seats draft, supervising
   agent decides) before any edit; verdict changes become their own repair
   notes, never silent edits.
4. **Reopened walls last**: each REOPENED-WALL file gets its no-go proof
   re-read against the landed text; a wall that no longer blocks is
   reported as an opened route, not repaired in place.

## Boundaries

Textual needle detection only; a file with no needle hit but a silently
stale argument is out of scope for this index. Classification is triage,
not audit. No ledger, queue, registry, or publication effective-status
file is touched by this campaign. Sets no audit status.
