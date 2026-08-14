# Axiom-Fidelity Re-read — Bounded Measurement Note

**Date:** 2026-08-09
**Claim type:** `bounded_theorem`
**Actual current-surface status:** bounded-support
**Trace class:** methodology
**Reachability:** none; this measurement reads a pinned corpus and repairs no row
**Snapshot:** `323d7fc32d77598f74ea6cd4d30c38dda0fe5070`
**Primary runner:** [`scripts/frontier_cycle971_axiom_fidelity_reread_2026_08_09.py`](../scripts/frontier_cycle971_axiom_fidelity_reread_2026_08_09.py)
**Independent checker:** [`scripts/frontier_cycle971_fidelity_independent_check_2026_08_09.py`](../scripts/frontier_cycle971_fidelity_independent_check_2026_08_09.py)
**Primary cache:** [`logs/runner-cache/frontier_cycle971_axiom_fidelity_reread_2026_08_09.txt`](../logs/runner-cache/frontier_cycle971_axiom_fidelity_reread_2026_08_09.txt)
**Checker cache:** [`logs/runner-cache/frontier_cycle971_fidelity_independent_check_2026_08_09.txt`](../logs/runner-cache/frontier_cycle971_fidelity_independent_check_2026_08_09.txt)
**Primary receipt:** [`outputs/axiom_fidelity_reread_cycle971_receipt_2026_08_09.json`](../outputs/axiom_fidelity_reread_cycle971_receipt_2026_08_09.json)
**Checker receipt:** [`outputs/axiom_fidelity_reread_independent_check_cycle971_receipt_2026_08_09.json`](../outputs/axiom_fidelity_reread_independent_check_cycle971_receipt_2026_08_09.json)
**Independent semantic ledger:** [`outputs/axiom_fidelity_reread_cycle971_independent_semantic_adjudications_2026_08_09.json`](../outputs/axiom_fidelity_reread_cycle971_independent_semantic_adjudications_2026_08_09.json)

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
target_claim_id: axiom_fidelity_reread_cycle971_bounded_theorem_note_2026-08-09
trace_class: methodology
target_blocker_text: independent_audit_required
source_of_blocker_text: user_goal
reachability_to_target: none
artifact_role: runner_certificate
next_trace_action: "Independent audit may assess this pinned bounded measurement."
packet_helper_runner: scripts/frontier_cycle971_fidelity_independent_check_2026_08_09.py
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact finite census on a named Git snapshot plus an explicit, provenance-aware semantic routing convention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Governing text and scope

The load-bearing sources are the pinned [minimal-axiom memo](MINIMAL_AXIOMS_2026-06-29.md)
and its pinned [premise-registry entry](audit/data/axiom_premise_nodes.json).
The 2026-08-05 text makes the probability distribution, rather than the set of
available possibilities, vary with nearest-neighbor conditions, and identifies
availability with the distribution's support. Consequently
`supp(mu(condition))` remains determined by the condition, but the axiom no
longer forces that support to vary nontrivially.

This snapshot predates the owner-approved 2026-08-13 Record simplification.
The present measurement addresses only the 2026-08-05 Admissibility change. It
does **not** classify current consumers of the later Record change and must not
be cited as doing so. In current framework authority, Record supplies no named
scalar collection functional `I`, no finite additivity, and no value
`I(empty)=0`; any row requiring those structures needs a separate retained
authority or remains conditional/open.

The primary enumerates the tracked `docs/` and `scripts/` paths with
`git ls-tree`, uses deliberately broad commit-scoped `git grep` anchors, and
reads candidate blobs with `git show <PIN>:<path>`. Full-blob token matching
then removes broad-selector false positives. No working-tree corpus body is a
measurement input, and no pinned runner is imported or executed.

The four-way routing is an explicit measurement convention:

- `UNAFFECTED` includes ordinary token uses and authority-free historical or
  supplied-comparator rows that do not assert the second sentence as current.
- `SUPPORT_READING_SAFE` includes support-level readings, current distribution
  wording, dated provenance that explicitly records the replacement, and
  model-specific support choices not attributed as axiom compulsion.
- `MEANING_CHANGED` includes rows that treat nonconstant support variation as
  live/current axiom content or use that variation load-bearingly.
- `NEWLY_WITNESSABLE` requires a literal neighbor-conditioned probability
  branch pair with identical positive supports and different weights. Merely
  changing positive support already had content under the old sentence.

This convention resolves the otherwise ambiguous history-only rows as
`UNAFFECTED`; routing those three rows as support-safe would instead give
`SUPPORT_READING_SAFE=73` and `UNAFFECTED=1341`. That taxonomy choice is
recorded rather than hidden, and is why this artifact is `meta`, not a theorem.

## Results

The four token classes select 1,440 of 15,205 tracked files. The complete,
disjoint file lists, every file-to-token count, and every classification reason
are in `measurement.consumer_rows` and `measurement.classes` of the primary
receipt. Rows resolved by a local phrase match also carry a bounded evidence
excerpt; semantic-reread overrides are identified by their pinned path and
override reason.

| Class | Files |
|---|---:|
| `UNAFFECTED` | 1,344 |
| `SUPPORT_READING_SAFE` | 70 |
| `MEANING_CHANGED` | 26 |
| `NEWLY_WITNESSABLE` | 0 |

Token totals are `availability=2788`, `vary_with=193`,
`nearest_neighbor_conditions=94`, and `admissible_possibility=240`.

The literal vacuity probe finds one state-resolved runner/branch pair and zero
marginal runners/branch pairs under its declared AST grammar. The state row is
`local_distribution(neighborhood_records)` in the pinned minimal-axioms
companion; its positive support changes between branches, so it is support-safe
and not newly witnessable. The zero is only a syntax-bounded corpus count. It
does not assert physical marginal independence or exclude other encodings.

Source-pinned comparison context at
`6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad` reports 4/20 state-resolved
comparisons (8/40 configurations) and 0/10 uniform-marginal comparisons. That
head is absent from the measurement pin, so those numbers are source-pinned,
non-load-bearing context and do not alter either corpus count.

## Certificate findings (verbatim)

```text
PASS A_CONSUMER_CENSUS :: pinned_snapshot=323d7fc32d77598f74ea6cd4d30c38dda0fe5070; tracked_files=15205; consumer_files=1440; selector_anchor_complete=True; token_totals={"admissible_possibility":240,"availability":2788,"nearest_neighbor_conditions":94,"vary_with":193}; file_to_token_counts=receipt.consumer_rows; row_digest=a24d1a30308acae64c6836a5e8804e433a16185085cebef704661193b772186f
PASS B_DELTA_CLASSIFICATION :: class_counts={"MEANING_CHANGED":26,"NEWLY_WITNESSABLE":0,"SUPPORT_READING_SAFE":70,"UNAFFECTED":1344}; complete_disjoint=True; full_file_lists=receipt.classes; classification is measurement-only
PASS C_VACUITY_PROBE :: literal_state_resolved_witness_runners=1; literal_state_resolved_branch_pairs=1; literal_marginal_witness_runners=0; literal_marginal_branch_pairs=0; state_paths=['scripts/audit_companion_minimal_axioms_clean_base_exact.py']; marginal_paths=[]; pinned_python_files_scanned=5646; a marginal-independence row would not refute state-resolved dependence
PASS D_CONTROLS :: object_pins={"axiom_blob":"2f5fdd26898f62c17fcabc846761f7785c2eadb1","docs_tree":"7dbc99ea9bb07250a72fff4722d37cdc1c573daf","registry_blob":"f01d3be864f682584d50eede8b3abe6671bb4719","scripts_tree":"b74e1639fc2a2250c0de2a56ad33665533a22c81","snapshot_commit":"323d7fc32d77598f74ea6cd4d30c38dda0fe5070","snapshot_tree":"45f8bd67eedaccb34918cb6804e850e1ba7f21fb"}; authority_checks={"availability_support_in_axiom":true,"new_sentence_in_axiom":true,"provenance_date_in_axiom":true,"registry_has_new_sentence":true,"registry_has_support_note":true}; BLOCKLIST=['323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/**', '323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/**'] execution=False; determinism_replay=True; runtime_s=158.651143<timeout_s=300<=300; stdout_upper_bound_bytes=4407<6000<150000; literal_AUDIT_INPUT_PATHS=['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/audit/data/axiom_premise_nodes.json']; pinned_snapshot_surfaces=['323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/', '323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/', '323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/MINIMAL_AXIOMS_2026-06-29.md', '323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/audit/data/axiom_premise_nodes.json']
VERDICT: PINNED_AXIOM_FIDELITY_MEASUREMENT_COMPLETE
TOTAL: PASS=4 FAIL=0
```

Integrity gates cover bookkeeping only. No primary predicate requires a
preferred class count or witness outcome.

## Independent refutation findings (verbatim)

```text
PASS R0_REFUTE_PINS_BLOCKLIST_AND_SNAPSHOT_IO :: file_pins_present_or_match=4/4; stable_science_digest_match=True; cache_contract_match=True; literal_pin=323d7fc32d77598f74ea6cd4d30c38dda0fe5070; git_ls_tree/show=True/True; working_tree_corpus_reads=False; BLOCKLIST_text_AST_only=['scripts/frontier_cycle971_axiom_fidelity_reread_2026_08_09.py', 'logs/runner-cache/frontier_cycle971_axiom_fidelity_reread_2026_08_09.txt', 'outputs/axiom_fidelity_reread_cycle971_receipt_2026_08_09.json', 'outputs/axiom_fidelity_reread_cycle971_independent_semantic_adjudications_2026_08_09.json', '323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/', '323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/']
PASS R1_REFUTE_CONSUMER_CENSUS :: independent_tracked/consumers=15205/1440; token_totals={"admissible_possibility":240,"availability":2788,"nearest_neighbor_conditions":94,"vary_with":193}; row_digest=a24d1a30308acae64c6836a5e8804e433a16185085cebef704661193b772186f; exact_path_token_rows_match=True
PASS R2_REFUTE_DELTA_CLASSIFICATION :: independent_class_counts={"MEANING_CHANGED":26,"NEWLY_WITNESSABLE":0,"SUPPORT_READING_SAFE":70,"UNAFFECTED":1344}; adjudication_manifest_valid=True; adjudication_manifest_sha256=e2b5195b9fd140d30eb551a3906c67dee1e603718b1ea6913d7410923716b68c; full_lists_match=True; classes_digest=389004fadd21329b142498f9af6042ad74d66b63561da88bdfb37750b67b9c59
PASS R3_REFUTE_VACUITY_PROBE :: independent_state_resolved_runners/branch_pairs=1/1; independent_marginal_runners/branch_pairs=0/0; pinned_python_files_scanned=5646; state_paths=['scripts/audit_companion_minimal_axioms_clean_base_exact.py']; marginal_paths=[]
PASS R4_REFUTE_AXIOM_PROVENANCE :: independent_authority_checks={"new_distribution_sentence":true,"owner_date":true,"registry_support":true,"support_provenance":true}
PASS R5_CONTROLS :: determinism_replay=True; runtime_s=148.924364<timeout_s=300<=300; stdout_upper_bound_bytes=5104<6000<150000; literal_AUDIT_INPUT_PATHS=['scripts/frontier_cycle971_axiom_fidelity_reread_2026_08_09.py', 'logs/runner-cache/frontier_cycle971_axiom_fidelity_reread_2026_08_09.txt', 'outputs/axiom_fidelity_reread_cycle971_receipt_2026_08_09.json', 'outputs/axiom_fidelity_reread_cycle971_independent_semantic_adjudications_2026_08_09.json']
VERDICT: PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT
TOTAL: PASS=6 FAIL=0
```

The checker pins the primary source and independently reviewed semantic-ledger
SHAs exactly, validates the canonical cache header and stable science digest,
and intentionally does not pin elapsed-time bytes. It rebuilds the census and
witness probe with separate Git-object and AST logic, then checks the primary's
complete class lists against the ledger; it does not duplicate the primary's
semantic regex router. Thus an ordinary primary-then-checker replay remains
reproducible even when runtime fields change.

## No-Go Discipline Gate

This gate applies only to the syntax-bounded statement that the declared
marginal witness grammar returns zero rows. It does not claim that marginal
dependence is physically absent.

### N1 — Alternative routes

| Route | Disposition | Why it does not refute the bounded count |
|---|---|---|
| Literal neighbor-branched numeric dictionaries under either marginal or uniform-self-input names | `ATTEMPTED` | Exhaustive pinned Python-AST traversal returns zero; see C and R3 above. |
| Array- or tuple-valued marginal distributions | `ATTEMPTED` | Located syntax would be outside the declared numeric-dictionary grammar; the note makes no claim about it. |
| Indirect helper calls or dynamically constructed distributions | `ATTEMPTED` | Such encodings are outside the literal-return grammar and are explicitly left open. |
| Neighbor-keyed lookup tables or `match`/dispatch encodings without literal branch returns | `ATTEMPTED` | These use a different control/data formulation outside the declared branch-return grammar and remain open. |
| Empirical tables or cached comparison summaries | `ATTEMPTED` | They cannot alter the literal AST count; they remain possible evidence for a different measurement. |

The literal-dictionary route was exhaustively executed over the pinned path
set. The other four were exercised as exclusion/counterexample families
against the declared grammar and remain explicitly open for any broader
measurement. They defeat a broad corpus or physics absence claim, which is why
that claim is not made.

### N2 — Wall independence

There is one boundary only: membership in the declared literal AST grammar.
There is no multi-wall independence count to inflate.

### N3 — Hidden-wall scan

No appeal to “standard,” “natural,” “obvious,” background physics, or an
uncited framework provision is load-bearing. The Git pin, token grammar,
classification convention, and AST grammar are explicit inputs.

### N4 — Residual matching

No prior no-go is cited as proof. The comparison head is labeled out-of-pin context and
its state/marginal result does not supply or close the pinned literal residual.

### N5 — Resolution audit

The primary cache lands the required five-line execution certificate. It
records one per-site literal branch pair and states that per-element, per-mode,
per-block, and lattice-wide comparisons were checked but not executed because
the grammar does not resolve those levels. No broader-resolution negative is
inferred.

### N6 — Partial-closure paths

The owner-approved distribution/support reframe is already applied to the
classification. The source-pinned comparison machinery is a separate state/marginal
comparison path and remains outside this pin. Neither route is described as a
new-axiom requirement.

### N7 — Steelman

A hostile reviewer should expect a marginal witness to be encoded through
arrays, helper calls, result tables, or a function without the selected name.
That is a concrete route against any broad corpus or physics absence claim.
The objection is accepted: the landed statement is demoted to a literal
grammar count, for which those encodings are expressly untested and open.

### N8 — Cross-run echo

The earlier “sites do not talk” reading was overturned by resolving neighbor
states before marginalization. The same retirement mechanism is honored here:
state-resolved and marginal syntax counts are separate, and a zero marginal
literal count does not erase the nonzero state-resolved count.

**N1–N8 result:** PASS for the narrowed literal-count statement; FAIL for, and
therefore no assertion of, a broader marginal-independence or impossibility
claim.

## Review record and hard landing condition

The adversarial review found and repaired a multiline-selector omission,
support-determination conflation, provenance/model false positives,
new-only-witness error, marker-only marginal test, duplicated runtime-byte
pins, and missing N5 resolution output. Mutation attacks must independently
flip every named primary and checker certificate before landing.

The final mutation harness returned exit 1 and exactly the targeted `FAIL`
name for each of `A_CONSUMER_CENSUS`, `B_DELTA_CLASSIFICATION`,
`C_VACUITY_PROBE`, `D_CONTROLS`,
`R0_REFUTE_PINS_BLOCKLIST_AND_SNAPSHOT_IO`,
`R1_REFUTE_CONSUMER_CENSUS`, `R2_REFUTE_DELTA_CLASSIFICATION`,
`R3_REFUTE_VACUITY_PROBE`, `R4_REFUTE_AXIOM_PROVENANCE`, and `R5_CONTROLS`.
The A mutation reproduced the historical seven-path line-selector omission;
the R2 mutation invalidated the independent semantic ledger. The other eight
mutations changed their named count, provenance, witness, or control input.

The audit packet also requires this helper mapping:

```json
{"axiom_fidelity_reread_cycle971_bounded_theorem_note_2026-08-09":["scripts/frontier_cycle971_fidelity_independent_check_2026_08_09.py"]}
```

The dependency-policy repair on current `main` permits this claim-scoped
mapping without exempting any other builder byte from the policy epoch. The
mapping co-lands with this packet. Rebuilding/seeding the ledger and a full
pipeline exit 0 remain hard landing conditions; this packet authors no audit
verdict.

No axiom, primitive, landed corpus row, or audit verdict is edited, and no
rewrite is proposed.
