# Phase 1 — Prose/ledger status divergence: measurement, severity, churn cost

Brief (b) of the repo-state-scrub campaign. Measured against `origin/main`
= `f865c14cd4b17f4659438f458a4fa3b89b24c1bc` (fetched 2026-07-25).

Status truth is read **only** from the tracked shards
`docs/audit/data/ledger/<id[:2]>/<id>.json`. No prose status label is
trusted anywhere in this report. Nothing here sets, predicts, or implies an
audit verdict; every status named below is a *measurement* of what the live
ledger currently records.

**Framework refresher read before concluding** (as required):
`docs/MINIMAL_AXIOMS_2026-06-29.md` (Lattice / Qubit / Admissibility /
Record; the unregistered "source/action and physical-observable
identification" gate is at line 170),
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (three approved
primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`), `docs/audit/README.md`,
`docs/audit/data/axiom_premise_nodes.json` (4 canonical ids:
`minimal_axioms` + the three primitives). Also read for this brief:
`docs/ai_methodology/skills/review-loop/SKILL.md` (churn guard, lines
809-820 and 882-891), `docs/audit/scripts/invalidate_stale_audits.py`,
`docs/audit/scripts/seed_audit_ledger.py`, `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`.

---

## HEADLINE

| | count |
|---|---|
| ledger rows (tracked shards) | 3872 |
| rows `audit_status == unaudited` | 3100 (80.1%) |
| rows `audit_status != unaudited` (audit capital at stake) | 772 (19.9%) |
| **status-attribution defect lines** (note labels a *named other* note with a status stronger than that note's live status) | **478** |
| — distinct citing notes | 176 |
| — distinct mislabelled targets | 203 |
| **self over-claim notes** (note declares its *own* status stronger than the ledger) | **26** |
| mutually circular pairs (X calls Y retained ∧ Y calls X retained) | **0** |
| **rows requeued if EVERY defect above is fixed** | **4** |
| **retained-grade verdicts put at risk** | **0** |

**The churn guard does not bind this defect class.** Fixing 100% of the
measured divergence costs 4 requeued rows out of 772 audited (0.5%) and
risks zero retained-grade verdicts — because the notes that carry false
status labels are themselves almost entirely `unaudited`.

---

## The mechanism that makes churn cheap (this is the load-bearing fact)

`docs/audit/scripts/seed_audit_ledger.py:606-615`:

```python
elif prior.get("note_hash") != node["note_hash"] and prior.get("audit_status") in {None, "unaudited"}:
    row["note_hash"] = node["note_hash"]
    reset_prose_defaults(row)
    preserved += 1                       # <-- edit an unaudited note: ZERO churn
elif prior.get("note_hash") != node["note_hash"]:
    row = archive_prior_audit(row)       # <-- verdict archived, row reset to unaudited
    row["note_hash"] = node["note_hash"]
    reset_prose_defaults(row)
    re_audit_required += 1               # <-- the only real churn
```

So **churn cost = (number of edited notes whose `audit_status != "unaudited"`)**,
not the number of edited notes. `invalidate_stale_audits.py:1-46` confirms
it does not duplicate the hash path (trigger 1 is explicitly delegated to
the seeder); its own triggers (dep added/removed, dep weakened, criticality
bump, runner-hash drift, classifier upgrade, no-go packet) are *not* fired
by editing a status word in a citing note's prose, because that edit changes
neither `deps` nor any dependency's `effective_status`.

Corroborating policy, `review-loop/SKILL.md:882-891`: a `note_hash` mismatch
on a non-retained-grade row "does **not** block review-loop PASS"; only a
mismatch on a **retained-grade** row is a hard error. Every repair proposed
below touches zero retained-grade rows.

---

## (a) Divergence counts, and how to reproduce them

Two disjoint populations. Both are measured line-by-line, which is exactly
the granularity a lint rule would police.

### Population C — status attribution to a *named other* note

A line that (i) resolves a reference to a ledger-registered note and
(ii) attaches a retained-grade/clean status token to it, where only
delimiter characters separate token from reference (the "label" relation),
and the target's **live** `effective_status` is weaker.

* **478 lines / 176 citing notes / 203 mislabelled targets.**
* Token split: `retained` 298, `retained_bounded` 123, `retained_no_go` 41,
  `audited_clean` 16.
* Target live status: `unaudited` 387, `audited_conditional` 55,
  `audited_failed` 14, `meta` 6, `decoration_under_*` 5,
  `retained_pending_chain` 3, `audit_in_progress` 2, `retained_bounded` 2.
* A looser same-line variant (token within 120 chars of the reference, words
  allowed in between) gives **1081 lines / 336 citing notes** — treat that as
  the upper bound; the 478 is the defensible core.

**Measured precision: 19/20** on a seeded random sample I adjudicated
against the source lines (`random.seed(5)`); the single miss was
`SCALAR_SELECTOR_REVIEWER_PACKAGE_2026-04-20.md:557`, where
"retained-observational inputs" is a compound noun, not a status label.
So ≈ 454 of the 478 are true defects.

### Population S — note declares its own status

* **31 candidates → 26 hand-verified true / 5 false (84% precision).** I
  adjudicated all 31 individually rather than sampling.
* False positives were the ordinary-English sense of "retained" (kept):
  `FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md:3` ("retained for
  provenance"), `YT_EW_COUPLING_BRIDGE_NOTE.md:74` ("retained for historical
  context only"), one conditional/future case
  (`WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md:292`),
  one where the token described a *citation* not the note
  (`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md:104`), and one
  consistent with its live status
  (`STAGGERED_NEWTON_REPRODUCTION_NOTE_2026-04-11.md:127`, live
  `retained_bounded`).
* **22 of the 26 are a single authoring batch**: `YT_*` notes dated
  2026-04-17/18 that all open with the sentence template *"This note is a
  retained structural sub-theorem…"*. This is one copy-paste header pattern,
  not 22 independent judgements — which makes it a single cheap batch fix.

### Grouped by claim id

Full machine-readable groupings were produced by the reproducer below.
The 26 self over-claim notes, ranked by in-degree:

| in-deg | claim id | live effective_status | file:line |
|---|---|---|---|
| 12 | `dm_neutrino_source_surface_schur_scalar_baseline_theorem_note_2026-04-17` | unaudited | `docs/DM_NEUTRINO_SOURCE_SURFACE_SCHUR_SCALAR_BASELINE_THEOREM_NOTE_2026-04-17.md:24` |
| 12 | `higgs_mass_retention_analysis_note_2026-04-18` | unaudited | `docs/HIGGS_MASS_RETENTION_ANALYSIS_NOTE_2026-04-18.md:36` |
| 12 | `yt_bottom_yukawa_retention_analysis_note_2026-04-18` | unaudited | `docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md:194` |
| 12 | `yt_p1_delta_r_2_loop_extension_note_2026-04-18` | unaudited | `docs/YT_P1_DELTA_R_2_LOOP_EXTENSION_NOTE_2026-04-18.md:48` |
| 8 | `yt_p1_rep_a_rep_b_cancellation_theorem_note_2026-04-17` | unaudited | `docs/YT_P1_REP_A_REP_B_CANCELLATION_THEOREM_NOTE_2026-04-17.md:46` |
| 7 | `yt_p1_delta_r_master_assembly_theorem_note_2026-04-18` | unaudited | `docs/YT_P1_DELTA_R_MASTER_ASSEMBLY_THEOREM_NOTE_2026-04-18.md:143` |
| 7 | `yt_p1_h_unit_renormalization_framework_native_note_2026-04-17` | unaudited | `docs/YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md:26` |
| 5 | `pmns_hw1_source_transfer_boundary_note` | **audited_conditional** | `docs/PMNS_HW1_SOURCE_TRANSFER_BOUNDARY_NOTE.md:139` |
| 5 | `yt_p1_loop_geometric_bound_note_2026-04-17` | unaudited | `docs/YT_P1_LOOP_GEOMETRIC_BOUND_NOTE_2026-04-17.md:28` |
| 4 | `yt_ew_coupling_bridge_note` | unaudited | `docs/YT_EW_COUPLING_BRIDGE_NOTE.md:7` |
| 4 | `yt_p1_color_factor_retention_note_2026-04-17` | unaudited | `docs/YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md:16` |
| 4 | `yt_p1_delta_1_bz_computation_note_2026-04-17` | unaudited | `docs/YT_P1_DELTA_1_BZ_COMPUTATION_NOTE_2026-04-17.md:28` |
| 4 | `yt_p1_delta_2_bz_computation_note_2026-04-17` | unaudited | `docs/YT_P1_DELTA_2_BZ_COMPUTATION_NOTE_2026-04-17.md:28` |
| 4 | `yt_p1_delta_3_bz_computation_note_2026-04-17` | unaudited | `docs/YT_P1_DELTA_3_BZ_COMPUTATION_NOTE_2026-04-17.md:34` |
| 3 | `yt_h_unit_flavor_column_decomposition_note_2026-04-18` | unaudited | `docs/YT_H_UNIT_FLAVOR_COLUMN_DECOMPOSITION_NOTE_2026-04-18.md:29` |
| 3 | `yt_p1_shared_fierz_no_go_sub_theorem_note_2026-04-17` | unaudited | `docs/YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md:29` |
| 2 | `kubo_continuum_limit_families_note` | unaudited | `docs/KUBO_CONTINUUM_LIMIT_FAMILIES_NOTE.md:196` |
| 2 | `yt_p3_k_series_geometric_bound_note_2026-04-17` | unaudited | `docs/YT_P3_K_SERIES_GEOMETRIC_BOUND_NOTE_2026-04-17.md:10` |
| 2 | `yt_right_handed_species_dependence_note_2026-04-18` | unaudited | `docs/YT_RIGHT_HANDED_SPECIES_DEPENDENCE_NOTE_2026-04-18.md:31` |
| 1 | `yt_p1_delta_r_sm_rge_crosscheck_note_2026-04-18` | unaudited | `docs/YT_P1_DELTA_R_SM_RGE_CROSSCHECK_NOTE_2026-04-18.md:47` |
| 1 | `yt_p2_f_yt_loop_geometric_bound_note_2026-04-17` | unaudited | `docs/YT_P2_F_YT_LOOP_GEOMETRIC_BOUND_NOTE_2026-04-17.md:20` |
| 1 | `yt_p3_msbar_to_pole_k1_framework_native_derivation_note_2026-04-17` | unaudited | `docs/YT_P3_MSBAR_TO_POLE_K1_FRAMEWORK_NATIVE_DERIVATION_NOTE_2026-04-17.md:14` |
| 0 | `yt_class_3_susy_2hdm_analysis_note_2026-04-18` | unaudited | `docs/YT_CLASS_3_SUSY_2HDM_ANALYSIS_NOTE_2026-04-18.md:41` |
| 0 | `yt_class_5_non_ql_yukawa_vertex_note_2026-04-18` | unaudited | `docs/YT_CLASS_5_NON_QL_YUKAWA_VERTEX_NOTE_2026-04-18.md:282` |
| 0 | `yt_p1_bz_quadrature_2_loop_full_staggered_pt_note_2026-04-18` | unaudited | `docs/YT_P1_BZ_QUADRATURE_2_LOOP_FULL_STAGGERED_PT_NOTE_2026-04-18.md:217` |
| 0 | `yt_p1_bz_quadrature_numerical_note_2026-04-18` | unaudited | `docs/YT_P1_BZ_QUADRATURE_NUMERICAL_NOTE_2026-04-18.md:28` |

Total in-degree carried by these 26 notes: **115**.

### Reproducible command

Save the appendix script (end of this file) as `/tmp/prose_ledger_divergence.py`, then from repo root:

```bash
git fetch origin && git stash list >/dev/null
python3 /tmp/prose_ledger_divergence.py .
```

Verified output on `origin/main` @ `f865c14`:

```
ledger rows                        : 3872
status-attribution defect LINES    : 478
  distinct citing notes            : 176
  distinct mislabelled targets     : 203
HIGH  (target is a real dep):  425 lines | 154 notes | REQUEUE=0 | retained-grade-at-risk=0
MEDIUM(cited, not a dep):   47 lines |  30 notes | REQUEUE=3 | retained-grade-at-risk=0
LOW   (in-deg 0 / meta):    6 lines |   5 notes | REQUEUE=0 | retained-grade-at-risk=0
TOTAL churn if ALL fixed           : requeue=3 rows, retained-grade at risk=0
mutual 2-cycles (X<->Y)            : 0
both-endpoints-unaudited lines     : 392
```

---

## (b) Severity grading

The brief's HIGH criterion is "claims a stronger status **and** is cited by
other work as an authority, so the false authority actually propagates". I
made that mechanical with the strongest available test: **is the mislabelled
target an actual entry in the citing note's `deps`?** If yes, the false label
is attached to a real load-bearing dependency edge — the false authority is
doing work, not decorating a table.

### Population C (status attribution)

| severity | criterion | lines | citing notes | targets | requeue |
|---|---|---|---|---|---|
| **HIGH** | mislabelled target is in the citer's `deps` | **425** | 154 | 182 | **0** |
| MEDIUM | target cited elsewhere (in-degree ≥ 1) but not a dep of this citer | 47 | 30 | 35 | 3 |
| LOW | target in-degree 0, or target is a `meta`/axiom node | 6 | 5 | 2 | 0 |

**This refutes the recorded supervisor prediction on the severity half.**
The prediction was that divergence would be "large in COUNT but low in
severity (mostly stale labels on rows nobody cites)". In fact **89% of
defect lines (425/478) sit on genuine dependency edges**, and the
mislabelled targets carry in-degrees up to 104. The divergence is large in
count *and* load-bearing. (The prediction's *repair* conclusion — lint rule
over mass sweep — still holds, but for a different reason than predicted:
the churn is zero, not the severity.)

### HIGH-severity targets with their citation-graph in-degree

Every one of these is `deps`-load-bearing for the citers listed, and every
live status shown is read from the tracked shard:

| citers-as-dep | in-deg | live effective_status | mislabelled target |
|---|---|---|---|
| 15 | **104** | unaudited | `three_generation_observable_theorem_note` |
| 13 | 37 | unaudited | `ckm_magnitudes_structural_counts_theorem_note_2026-04-25` |
| 13 | 53 | unaudited | `koide_circulant_character_derivation_note_2026-04-18` |
| 13 | 44 | unaudited | `charged_lepton_koide_cone_algebraic_equivalence_note` |
| 11 | 35 | unaudited | `cl3_sm_embedding_theorem` |
| 10 | 54 | unaudited | `cl3_color_automorphism_theorem` |
| 8 | 44 | unaudited | `yt_ew_color_projection_theorem` |
| 8 | 45 | unaudited | `ckm_cp_phase_structural_identity_theorem_note_2026-04-24` |
| 8 | 34 | unaudited | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` |
| 8 | 60 | unaudited | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` |
| 7 | 26 | unaudited | `ckm_nlo_barred_triangle_protected_gamma_theorem_note_2026-04-25` |
| 6 | 42 | unaudited | `wolfenstein_lambda_a_structural_identities_theorem_note_2026-04-24` |
| 6 | 26 | unaudited | `sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26` |
| 5 | 29 | **audited_conditional** | `cl3_complexification_split_narrow_theorem_note_2026-05-10` |
| 5 | 41 | unaudited | `three_generation_structure_note` |
| 5 | 24 | **audited_conditional** | `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` |
| 5 | 6 | unaudited | `parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23` |
| 4 | 13 | **audited_failed** | `single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10` |
| 4 | 55 | unaudited | `alpha_s_derived_note` |
| 4 | 22 | unaudited | `complete_prediction_chain_2026_04_15` |
| 3 | 41 | unaudited | `koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24` |
| 3 | 11 | unaudited | `no_per_site_chirality_theorem_note_2026-05-02` |

Verbatim instances (target live status in brackets, read from shard):

* `three_generation_observable_theorem_note` [**unaudited**, in-deg 104] —
  `docs/A3_R4_REVIEW_CONFIRMED_NOTE_2026-05-08_r4hr.md:202`
  `| [\`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md\`](…) | retained | M_3(C) on hw=1 |`
* `cl3_color_automorphism_theorem` [**unaudited**, in-deg 54] —
  `docs/A3_R4_REVIEW_CONFIRMED_NOTE_2026-05-08_r4hr.md:201`
  `| [\`CL3_COLOR_AUTOMORPHISM_THEOREM.md\`](…) | retained-bounded | SU(3) on V_3 |`
* `left_handed_charge_matching_note` [**audited_decoration**, in-deg 38] —
  `docs/CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md:188`
  `| … | **retained corollary** | **S1 SOURCE** (load-bearing) |`
  — the same line that mislabels it also marks it load-bearing.

### Two worst sub-classes inside HIGH

**(i) Terminal non-clean rows cited as retained-grade — 81 lines / 47 targets.**
Of these, **14 lines / 7 targets / 9 citing notes** label an
`audited_failed` row as retained-grade. A reader following the citation sees
"retained" for a row the audit lane has already failed:

* `single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10`
  [**audited_failed**, in-deg 13], labelled `retained` at
  `docs/G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md:161`
  and `docs/KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md:166`.
* Also affected: `decoherence_action_independence_note` (in-deg 3),
  `wave_retardation_continuum_limit_note` (7),
  `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22` (9),
  `cubic_coxeter_regge_second_variation_equals_linearized_eh_narrow_theorem_note_2026-06-09` (5),
  `universal_gr_so3_isotypic_orbit_flat_narrow_theorem_note_2026-05-10` (3),
  `teleportation_apparatus_dynamics_closure_note` (2).

**(ii) Prose that fabricates audit metadata — 3 lines / 2 notes.**
Small but qualitatively the worst, because it claims to *be quoting the
ledger*, which defeats the "check the ledger" instruction:

* `docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md:103`
  — `` | `retained_bounded` in the current audit ledger | `` for a target whose
  live row is `unaudited`/`unaudited`.
* `docs/G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18.md:24` and `:248` — assert
  `` `audited_clean` / `retained_bounded` `` **with an `audit_date`** for the
  same target. The verdict they cite was archived by
  `archive_prior_audit()` when the target note drifted; the prose kept the
  corpse.

Note the interaction with the churn mechanic: this is exactly how these
arise. A note is audited → the note is later edited → `seed_audit_ledger.py`
archives the verdict and resets the row to `unaudited` → **every downstream
prose sentence quoting the old verdict silently becomes false**, and nothing
in the toolchain looks at those sentences.

**(iii) A status value that exists nowhere.** **41 lines across 28 citing
notes assert `retained_no_go` about a cited note. Zero rows in the live
ledger have `effective_status == retained_no_go`** (439 rows have
`claim_type == no_go`: 438 `unaudited`, 1 `audited_conditional`). This whole
label is prose-only.

### Population S severity

| severity | criterion | notes |
|---|---|---|
| HIGH | self over-claim, in-degree ≥ 1 | **22** |
| MEDIUM | self over-claim, in-degree 0 | 4 |
| LOW | understates its status, or no status semantics | 1 measured (`STAGGERED_NEWTON_REPRODUCTION_NOTE_2026-04-11.md:127`, consistent with its live `retained_bounded`) |

---

## (c) Mutual circularity — measured, and it is ZERO

The brief cites "44 such contradictions across 14 claim ids" in a recent
lane. Corpus-wide, under four separate definitions, I find **no circularity
at all**:

| definition | strict set | loose set |
|---|---|---|
| 2-cycles: X labels Y retained ∧ Y labels X retained | **0** | **0** |
| any directed cycle in the status-attribution graph (DFS) | **0** | **0** |

The status-attribution graph is a **DAG**. That is a real negative result:
the 44-contradiction figure is not corpus-wide graph circularity, and a
repair plan should not be sized for it.

What *is* there instead, and is arguably the more accurate description of
the phenomenon:

* **392 of 478 defect lines (82%) have BOTH endpoints `unaudited`** — 153
  citing notes conferring retained-grade status on 153 target notes, with
  zero ledger backing on either side. A self-certifying authority layer,
  but acyclic.
* **4 claim ids both self-declare retained AND are labelled retained by
  another note, while `unaudited`** — the only genuine mutual-reinforcement
  cases: `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03`
  (in-deg 9), `yt_p1_color_factor_retention_note_2026-04-17` (4),
  `yt_p1_loop_geometric_bound_note_2026-04-17` (5),
  `yt_zero_import_chain_note` (10).

---

## (d) Churn cost per tier

Computed mechanically from `seed_audit_ledger.py:606-615` (edit an
`unaudited` note → `preserved`, zero churn; edit any other → verdict
archived + requeue). Cross-checked against every trigger in
`invalidate_stale_audits.py`: none of them fire for a prose status-word edit
in a citing note, because `deps` and dependency `effective_status` are
untouched.

| batch | notes to edit | **rows requeued** | retained-grade at risk | requeued rows' status |
|---|---|---|---|---|
| C-HIGH (425 lines) | 154 | **0** | 0 | — |
| C-MEDIUM (47 lines) | 30 | **3** | 0 | 2 `audited_failed`, 1 `audited_conditional` |
| C-LOW (6 lines) | 5 | **0** | 0 | — |
| **C-ALL (478 lines)** | **176** | **3** | **0** | as above |
| S-HIGH (22 notes) | 22 | **1** | 0 | 1 `audited_conditional` |
| S-MEDIUM (4 notes) | 4 | **0** | 0 | — |
| **S-ALL (26 notes)** | **26** | **1** | **0** | `pmns_hw1_source_transfer_boundary_note` |
| **EVERYTHING** | **≈197** | **4** | **0** | — |

4 requeued rows against 772 audited rows = **0.5% of audit capital**, and
**not one retained-grade verdict is touched**. For comparison, the guard in
`review-loop/SKILL.md:809-820` exists to prevent sweeps that "reset or
requeue already-audited rows"; at 4 rows this is roughly a rounding error,
and 3 of the 4 are already-terminal non-clean rows whose re-entry is
governed by the stuck-row requeue gate (`SKILL.md:893-908`) rather than by
ordinary queue pressure.

**Why the churn is so low, stated plainly:** false status labels are written
by notes that never earned a status themselves. 153 of the 176 citing notes
are `unaudited`. Audited notes, having been through a fresh-look review,
mostly do not carry these labels. The defect concentrates precisely where
fixing it is free.

---

## (e) Recommendation

### Ranked plan

**BATCH 1 — TOOLING (do this first; zero churn, catches the class forever).**
Add one check to `audit_lint.py`. The hook already exists: the main per-row
loop at `audit_lint.py:787-799` **already reads every claim note's body**
(`note_body = (REPO_ROOT / note_path).read_text(...)`) and already has the
full `rows` dict in scope, so target lookup is a dict access. The rule:

> For each line of a claim note, if the line resolves a reference to a
> ledger-registered claim id and attaches a status token to it with only
> delimiters in between, compare the token to that target's live
> `effective_status`. Emit a notice when the prose token is stronger.

Cost: zero audit churn (tooling, not source). Catches all 478 of today's
instances plus every future one. Emit it as a **notice, not a hard error**,
for two reasons: `docs/audit/README.md:63-65` explicitly permits authors to
"write whatever status prose they need inside source notes", so a hard error
would contradict standing policy and would fail the build on 176 notes on
day one; and precision is ~95%, not 100%. Escalate to error only for the
narrow, unambiguous sub-rule below.

Ship two narrow **hard** sub-rules where precision is effectively 100% and
the harm is greatest:
* prose asserting `retained_no_go` — **41 lines / 28 notes**, a value that
  exists on zero live rows, so any occurrence is wrong by construction;
* prose asserting a status **together with an `audit_date` or an explicit
  "in the current audit ledger" / "per the ledger" claim** — **3 lines / 2
  notes** today. This impersonates the ledger and is never legitimate;
  the ledger is the ledger.

**BATCH 2 — CONTENT, C-HIGH terminal-verdict subset (highest harm/effort ratio).**
The 14 lines / 9 citing notes that label an `audited_failed` row
retained-grade, plus the 3 fabricated-metadata lines. **17 lines, ~11 notes,
requeue 0.** These are not cosmetics: a note that tells a reader an
`audited_failed` dependency is `retained` is a science-correctness defect,
and the constraint doc explicitly classes "a note asserting a false status"
as a science correction rather than churn.

**BATCH 3 — CONTENT, S-ALL self over-claims (26 notes, requeue 1).**
Cheap because 22 of 26 are the one `YT_*` 2026-04-17/18 header template
*"This note is a retained structural sub-theorem…"*. A single templated
edit — delete the status adjective, keep the sentence — resolves 22 notes
carrying 115 total in-degree. Only `pmns_hw1_source_transfer_boundary_note`
requeues, and it is `audited_conditional`, not retained-grade. Handle it
under the stuck-row requeue gate or leave it to Batch 4.

**BATCH 4 — CONTENT, remainder of C-HIGH (≈408 lines / ~145 notes, requeue 0).**
Genuinely worth doing since it is free of churn, but it is bulk editing, so
sequence it *after* the lint lands — otherwise the same pattern reappears in
the next campaign's notes and the work is re-done. Best executed as a
mechanical rewrite of the recurring "cited authorities" table column, not as
prose judgement calls.

**LEAVE ALONE — C-LOW (6 lines / 5 notes) and S-LOW.** Five of the six are
`meta`/axiom-node targets (e.g. `MINIMAL_AXIOMS_2026-04-11.md` described as
"retained"): registered premise nodes chain-satisfy dependencies without
being retained-grade at all (`PRIMITIVE_REGISTRY_CHECK.md` items 3-4), so
the label is loose wording rather than propagating false theorem authority.
Not worth an edit; the Batch-1 notice will surface them if they ever matter.
Likewise leave under-statements alone — a note claiming *less* than its row
harms nobody.

### The justification in one line

The churn guard is the campaign's stated main risk, and **for this defect
class it does not bind**: total cost to fix everything is 4 requeued rows
(0.5% of audited capital) and 0 retained-grade verdicts. So the usual
"lint instead of sweep" trade-off is *not* the reason to prefer tooling
here. The reason is **recurrence**: 478 instances accumulated because
nothing in the toolchain ever compared a prose status word to the row it
names, and a content-only sweep would leave that hole open. Ship the lint
first because it is permanent and free; then spend the (nearly free) content
edits in harm order.

### Answer to the campaign's diagnostic question, for this brief's slice

Divergence (b) is **real, large, and load-bearing** — 478 lines, 89% of them
on true dependency edges — but it is a **symptom**, and its proximate cause
is (c) **pipeline gap**: `audit_lint.py` reads note bodies already and never
checks them for status claims, `vocab_lint.py` contains no status vocabulary
at all, and the one ledger field designed for prose hygiene is inert
(`prose_status`: 2876/3872 rows are `not_evaluated_pre_vocab_lint`, 996 are
`clean`, and **0 rows carry a single `prose_corrections` entry** — the
auto-correct-and-log mechanism specified in
`docs/repo/VOCABULARY_HYGIENE_DESIGN.md` principle 4 has never fired).
Note also that `prose_status` would not have caught any of this even if
live: `docs/audit/README.md:108-124` scopes it to *vocabulary* drift, and it
explicitly "does **not** propagate into `effective_status`". There is no
field anywhere that means "this note's prose asserts a status contradicting
the ledger". That is the gap to close.

---

## Appendix — reproducer script

Save as `/tmp/prose_ledger_divergence.py`; run `python3 /tmp/prose_ledger_divergence.py <repo-root>`.
Reads only the tracked ledger shards and the notes they point at; writes nothing.

```python
#!/usr/bin/env python3
import json, glob, os, re, collections, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
rows = {}
for f in glob.glob(os.path.join(ROOT, "docs/audit/data/ledger/*/*.json")):
    d = json.load(open(f, encoding="utf-8")); rows[d["claim_id"]] = d
base2cid, cid_l = {}, {}
for c, d in rows.items():
    base2cid.setdefault(os.path.basename(d["note_path"]).lower(), c); cid_l[c.lower()] = c

RANK = {"retained":100,"retained_no_go":100,"retained_bounded":95,"retained_pending_chain":80,
        "audited_clean":70,"open_gate":40,"decoration":35,"audited_conditional":30,
        "audited_numerical_match":25,"audited_renaming":20,"audited_decoration":20,
        "audited_failed":10,"audit_in_progress":5,"unaudited":0,"meta":0}
def er(e): return 0 if not e else (RANK["decoration"] if e.startswith("decoration_under_") else RANK.get(e,0))

TOKENS=[(r"retained[_\- ]bounded","retained_bounded"),(r"retained[_\- ]no[_\- ]?go","retained_no_go"),
        (r"audited[_\- ]clean","audited_clean"),(r"retained[_\- ]grade","retained"),(r"\bretained\b","retained")]
TOK=re.compile("|".join("(?P<g%d>%s)"%(i,p) for i,(p,_) in enumerate(TOKENS)),re.I)
NM={"g%d"%i:n for i,(_,n) in enumerate(TOKENS)}
REF=re.compile(r"(?:\[[^\]]{2,200}?\]\(([^)\s]*?([A-Za-z0-9_\-]+\.md))[^)]*\)"
               r"|`([A-Za-z0-9_\-/]*?([A-Za-z0-9_\-]+\.md))`|`([a-z0-9_]{10,})`"
               r"|\b([A-Z][A-Z0-9_]{9,}\.md)\b)")
NEG=re.compile(r"(\bnot\b|\bno\b|\bnever\b|\bwithout\b|\black\w*|\bmissing\b|\bunless\b|\bpending\b|"
   r"\bawait\w*|\buntil\b|\bonce\b|\bif\b|\bwould\b|\bcould\b|\bmay\b|\bmight\b|\bshould\b|\bwill\b|"
   r"\bto\s+be\b|\btoward\w*|\btarget\w*|\bcandidate\w*|\bpropos\w*|\brequir\w*|\bneed\w*|\bre-?audit\w*|"
   r"\bformer\w*|\bpreviou\w*|\bwas\b|\bwere\b|\barchiv\w*|\brather\s+than\b|\bupgrad\w*|\bbelow\b|"
   r"\bor\s+its\b|\bequivalent\b)[^\n]{0,60}$",re.I)
DELIM=re.compile(r"^[\s|:;,.—–\-()\[\]`*>\"']*$")

out=[]
for cid,d in sorted(rows.items()):
    try: txt=open(os.path.join(ROOT,d["note_path"]),encoding="utf-8",errors="replace").read()
    except OSError: continue
    for ln,line in enumerate(txt.split("\n"),1):
        if len(line)>1200: continue
        refs=[]
        for m in REF.finditer(line):
            b=m.group(2) or m.group(4) or m.group(6)
            t=base2cid.get(b.lower()) if b else cid_l.get((m.group(5) or "").lower())
            if t: refs.append((t,m.start(),m.end()))
        if not refs: continue
        for m in TOK.finditer(line):
            name=next(n for g,n in NM.items() if m.group(g)); s,e=m.span()
            if any(a<=s<b for _,a,b in refs) or NEG.search(line[:s]): continue
            for t,a,b in refs:
                gap = line[e:a] if a>=e else (line[b:s] if s>=b else None)
                if gap is None or len(gap)>40 or not DELIM.match(gap) or t==cid: continue
                if RANK.get(name,0)<=er(rows[t].get("effective_status")): continue
                out.append((cid,d["note_path"],ln,name,t,rows[t].get("effective_status"),
                            rows[t].get("audit_status"),t in (d.get("deps") or []),
                            rows[t].get("direct_in_degree") or 0)); break

AUD=lambda c: rows[c].get("audit_status") not in (None,"unaudited")
RG={"retained","retained_bounded","retained_no_go"}
hi=[r for r in out if r[7] and r[5]!="meta"]
med=[r for r in out if not r[7] and r[8]>=1 and r[5]!="meta"]
low=[r for r in out if r[5]=="meta" or (not r[7] and r[8]==0)]
print(f"ledger rows                        : {len(rows)}")
print(f"status-attribution defect LINES    : {len(out)}")
print(f"  distinct citing notes            : {len({r[0] for r in out})}")
print(f"  distinct mislabelled targets     : {len({r[4] for r in out})}")
for lbl,g in (("HIGH  (target is a real dep)",hi),("MEDIUM(cited, not a dep)",med),("LOW   (in-deg 0 / meta)",low)):
    src={r[0] for r in g}; aud=[c for c in src if AUD(c)]
    print(f"{lbl}: {len(g):4d} lines | {len(src):3d} notes | REQUEUE={len(aud)} | "
          f"retained-grade-at-risk={len([c for c in aud if rows[c].get('effective_status') in RG])}")
allsrc={r[0] for r in out}; allaud=[c for c in allsrc if AUD(c)]
print(f"TOTAL churn if ALL fixed           : requeue={len(allaud)} rows, "
      f"retained-grade at risk={len([c for c in allaud if rows[c].get('effective_status') in RG])}")
g=collections.defaultdict(set)
for r in out: g[r[0]].add(r[4])
print(f"mutual 2-cycles (X<->Y)            : "
      f"{len({tuple(sorted((a,b))) for a,o in g.items() for b in o if a in g.get(b,())})}")
print(f"both-endpoints-unaudited lines     : "
      f"{len([r for r in out if rows[r[0]].get('audit_status')=='unaudited' and r[6]=='unaudited'])}")
```

### Measurement caveats (stated so the numbers can be trusted or re-derived)

* Precision is **measured, not assumed**: 19/20 on a seeded random sample
  for population C; 26/31 by exhaustive hand-adjudication for population S.
  I did not estimate recall — the strict adjacency rule deliberately trades
  recall for precision, so 478 is a **floor**, and the looser same-line
  variant (1081 lines / 336 notes) bounds it above.
* `docs/audit/data/citation_graph.json` is gitignored (`.gitignore:41`), so
  in-degree is read from the tracked shards' own `direct_in_degree` and
  `deps` fields, which are the graph materialized into the source of truth.
* Everything was measured against a clean `git archive origin/main` export,
  not the working tree, which is 1270 files divergent from `origin/main`.
