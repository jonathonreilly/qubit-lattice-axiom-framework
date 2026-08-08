# Phase 1C — Pipeline gap analysis: what the toolchain does and does NOT check

**Brief.** Inventory every check the audit toolchain enforces; determine for
seven observed defect classes whether any existing check catches them; design
the lint rules that would have prevented them; answer the owner's diagnostic
question with proportions.

**Measured against** `origin/main` @ `f865c14cd4b17f4659438f458a4fa3b89b24c1bc`
(`audit: plaquette_beta6_strong_coupling_character_narrow_theorem_note_2026-05-27
audited_failed`), in a detached read-only worktree at
`/private/tmp/claude-502/.../scratchpad/gapwt-origin-main`. Nothing was
committed, pushed, or PR'd; no repository file was edited. Generated caches
(`audit_ledger.json`, `citation_graph.json`, `audit_queue.json`) were
materialized locally for measurement only — all three are gitignored.

**Ledger universe at that commit:** 3872 rows; 4506 citation-graph nodes;
5243 `scripts/*.py`; 3740 files in `logs/runner-cache/`.

---

## 0. Headline result, stated once

`audit_lint.py` on `origin/main` today reports **0 errors**, 23 warnings, 441
notices. Every defect the campaign was opened over passes the pipeline clean.
That is not a bug in any individual check — it is the correct output of a
toolchain whose gates were designed to police *ledger-internal consistency*
and which has **no gate on the boundary between "a result exists in the repo"
and "a result has a ledger row."**

```
cd <worktree> && python3 docs/audit/scripts/ledger_io.py --materialize \
  && python3 docs/audit/scripts/build_citation_graph.py \
  && python3 docs/audit/scripts/audit_lint.py
# → audit_lint: 3872 rows checked / 23 warnings / 441 notices / OK: no errors
```

The single most load-bearing line in the whole toolchain for this campaign is
`docs/audit/scripts/check_staged_claim_typing.py:51-54` — the only ratchet
that inspects *newly staged notes*:

```python
hit = row_by_note_path.get(path)
if hit is None:
    # Excluded/gated infrastructure or not a ledger row at all.
    continue
```

**The ratchet that is supposed to stop unowned science from entering the repo
explicitly skips every note that has no ledger row.** A note with a runner, a
PASS total, and a real theorem, staged under `docs/work_history/`, passes this
gate *by construction*.

---

## (a) INVENTORY — every check currently enforced

### A.1 The pipeline is 24 script invocations; only 4 of them are gates

`docs/audit/scripts/run_pipeline.sh` (240 lines) runs 18 numbered stages.
Counting `return 1` / `sys.exit(1)` sites per stage:

| Stage | Script | file:line of gate | Hard-fail? |
|---|---|---|---|
| 0-ledger | `ledger_io.py --materialize` | `run_pipeline.sh:83` | shard-parse only (1 site) |
| **0** | **`check_axiom_premise_clean.py`** | `run_pipeline.sh:86`; `check_axiom_premise_clean.py:104` | **YES — gate** |
| **0a** | **`scripts/audit_model_family_normalization_guard.py`** | `run_pipeline.sh:89` | **YES — gate** |
| 1 | `build_citation_graph.py` | `run_pipeline.sh:93` | producer (fails only on checkpoint receipt, `:734`) |
| 1b | `write_citation_graph_manifest.py` | `run_pipeline.sh:96` | producer, 0 fail sites |
| 1c/5/7a | `compute_load_bearing.py` | `run_pipeline.sh:103,120,181` | producer, 0 fail sites |
| 2/3a | `seed_audit_ledger.py` | `run_pipeline.sh:106,124` | producer |
| 3 | `sanitize_legacy_audit_artifacts.py` | `run_pipeline.sh:112` | producer, 0 fail sites |
| 3b/4b/18b | `static_pipeline_checkpoint.py` | `run_pipeline.sh:127,133,221/227` | freshness proof only |
| 4 | `classify_runner_passes.py` | `run_pipeline.sh:130` | 1 site: ledger missing (`:193`) |
| 6 | `compute_effective_status.py` | `run_pipeline.sh:139,167` | producer, 0 fail sites |
| 7 | `invalidate_stale_audits.py` + restore loop | `run_pipeline.sh:150,159` | fixed-point non-convergence only (`:170-173`) |
| 7b | `compute_lane_certification.py` | `run_pipeline.sh:184` | producer, 0 fail sites |
| 8 | `build_cycle_inventory.py` | `run_pipeline.sh:187` | producer, 0 fail sites |
| 9 | `compute_audit_queue.py` | `run_pipeline.sh:190` | producer, 0 fail sites |
| 10 | `compute_reaudit_candidates.py` | `run_pipeline.sh:193` | producer, 0 fail sites |
| 11 | `compute_audit_dispatch_queue.py` | `run_pipeline.sh:196` | producer, 0 fail sites |
| 12 | `compute_auditor_reliability.py` | `run_pipeline.sh:199` | producer, 0 fail sites |
| **13** | **`audit_lint.py`** | `run_pipeline.sh:202`; `audit_lint.py:1538-1544` | **YES — gate** |
| 14 | `render_audit_ledger.py` | `run_pipeline.sh:205` | producer, 0 fail sites |
| 15 | `render_publication_effective_status.py` | `run_pipeline.sh:208` | producer, 0 fail sites |
| 16 | `compute_dispatch_shadow.py` | `run_pipeline.sh:211` | producer, 0 fail sites |
| 17 | `render_front_door_status.py` | `run_pipeline.sh:214` | producer, 0 fail sites |
| **18** | **`repo_invariants_check.py --check --enforce-links`** | `run_pipeline.sh:217`; `repo_invariants_check.py:842` | **YES — gate** |

**Count: 18 numbered stages, 24 invocations, 4 gates.** 14 stages have zero
hard-fail sites; they are *producers* that write generated state and cannot
refuse anything.

### A.2 `audit_lint.py` — 85 emission sites across 3 severity classes

56 `errors.append` + 1 `errors.extend` = **57 error sites**; **13
`add_warning` sites** (13 distinct categories); **16 `add_notice` sites** (15
distinct categories). Reproduce with:

```bash
grep -c 'errors\.append' docs/audit/scripts/audit_lint.py   # 56
grep -n 'add_warning(\|add_notice(' docs/audit/scripts/audit_lint.py | grep -v 'def add_'
```

**Error-level checks (blocking), grouped:**

| # | Check | file:line |
|---|---|---|
| 1 | Front-door surface does not cite current `minimal_axioms` path | `audit_lint.py:517-520`, driver `:750-763` |
| 2 | Front-door surface cites a superseded axiom-memo alias | `audit_lint.py:523-527` |
| 3 | Front-door surface listed but missing on disk | `audit_lint.py:753-756` |
| 4 | `tier_a_admissions.json` / `owner_governed_premise_nodes.json` must not exist | `audit_lint.py:679-687` |
| 5 | `derivation_obligations.json` parse failure | `audit_lint.py:693` |
| 6 | `canonical_ids` ≠ `nodes` | `audit_lint.py:698-700` |
| 7 | Obligation overlaps the axiom/primitive foundation | `audit_lint.py:703-706` |
| 8 | Obligation has **no ledger row** | `audit_lint.py:709` |
| 9 | Obligation is "incorrectly accepted" as a premise | `audit_lint.py:711` |
| 10 | Obligation **lacks** `target` (non-empty test only) | `audit_lint.py:713` |
| 11 | Obligation lacks `current_path` / path missing on disk | `audit_lint.py:716-721` |
| 12 | Scientific row depends on a non-evidence context dep | `audit_lint.py:728-731` |
| 13 | Stale top-level timestamp keys in the ledger | `audit_lint.py:775-778` |
| 14 | Deprecated ledger field present | `audit_lint.py:850` |
| 15-17 | `audit_status` / `claim_type` / `effective_status` outside enum | `audit_lint.py:852,854,856` |
| 18-19 | Audited row lacks `claim_type` / `claim_scope` | `audit_lint.py:859,861` |
| 20 | `independence` outside enum | `audit_lint.py:907` |
| 21-22 | `prose_status` outside enum; `prose_corrections` not a list | `audit_lint.py:916,921` |
| 23 | `auditor_family` outside canonical/legacy set | `audit_lint.py:956-960` |
| 24 | Unsupported `cross_confirmation.agreement_schema` | `audit_lint.py:1025-1028` |
| 25-30 | v2 agreement-tuple schema/match/live-row-consistency errors | `audit_lint.py:1043,1057,1080,1108,1136,1160` |
| 31 | `third_confirmed_*` missing `third_audit` | `audit_lint.py:1096,1264` |
| 32 | `third_audit.sided_with` conflicts with status | `audit_lint.py:1120` |
| 33 | `judicial_review` row disagrees with `third_audit` | `audit_lint.py:1171` |
| 34-35 | `audited_clean` lacks `auditor` / `auditor_family` | `audit_lint.py:1178,1180` |
| 36 | Codex `audited_clean` family/model/effort inconsistency | `audit_lint.py:1194` |
| 37 | Non-Codex `audited_clean` without strong/external/judicial independence | `audit_lint.py:1201` |
| 38-39 | `audited_clean` claim_type→effective_status promotion mismatch | `audit_lint.py:1212,1222` |
| 40 | `critical`/`high` criticality with `independence='weak'` | `audit_lint.py:1229` |
| 41-44 | Critical cross-confirmation: missing, reused auditor, same-family without `fresh_context`, third-audit reuse | `audit_lint.py:1237,1247,1256,1266,1276,1283` |
| 45-46 | `audited_decoration` requires `claim_type='decoration'` and a parent | `audit_lint.py:1291,1300` |
| 47 | **`note_hash` mismatch on a RETAINED-grade row** | `audit_lint.py:1380-1383` |
| 48 | Retained-grade row with a non-chain-satisfying dep | `audit_lint.py:1417-1420` |
| 49-50 | No-Go Discipline packet absent/invalid on a live `audited_clean` | `audit_lint.py:614,624` |

**Warning-level (13 categories, non-blocking):** `claim_type_defaulted`
(`:875`), `conditional_repair_prefix` (`:943`), `legacy_auditor_family`
(`:962`), `codex_model_floor` (`:973`), `claude_independence` (`:1007`),
`criticality_bumped` (`:1347`), `source_note_missing` (`:1363`),
`dangling_dependency` (`:1394`), `audit_dispatch_queue_invalid` (`:1442`),
`audit_dispatch_queue_missing` (`:1447`), `audit_dispatch_sidecar_invalid`
(`:1456`), `audit_dispatch_sidecar_unsupported` (`:1463`),
`audit_dispatch_queue_stale` (`:1473`).

**Notice-level (15 categories, non-blocking):** `legacy_no_go_packet_absent`
(`:616`), `non_authoritative_invalid_no_go_packet` (`:626`),
`archived_invalid_no_go_packet` (`:847`), `legacy_backfill_scope` (`:864`),
`legacy_claim_type_backfill` (`:870`), `excluded_path_row_grandfathered`
(`:893`), `excluded_path_row_pending_drop` (`:900`),
`prose_status_backfill_pending` (`:927`),
`legacy_cross_confirmation_tuple_mismatch` (`:1070`, `:1149`),
`pending_dependency_chain` (`:1217`), `legacy_decoration_parent` (`:1295`),
`decoration_parent_not_retained` (`:1304`),
`criticality_bumped_to_critical_awaits_cc` (`:1354`),
**`note_hash_drift_reaudit_pending`** (`:1385`), `graph_cycles` (`:1511`).

**Live baseline on `origin/main`:** warnings — `claim_type_defaulted` 11,
`conditional_repair_prefix` 9, `legacy_auditor_family` 3 (total 23). Notices —
`archived_invalid_no_go_packet` 246, `legacy_cross_confirmation_tuple_mismatch`
85, `legacy_backfill_scope` 63, `excluded_path_row_grandfathered` 38,
`decoration_parent_not_retained` 7, `graph_cycles` 1 (59 back-edges),
`legacy_no_go_packet_absent` 1 (total 441). Errors: **0**.

### A.3 The other three gates

**`check_axiom_premise_clean.py`** (`run_pipeline.sh:86`): for each node in
`axiom_premise_nodes.json`, fails if the source doc contains one of 6
ratification-clause regexes (`check_axiom_premise_clean.py:39-46`) or the
registered path is missing (`:83-85`). Scope: **4 docs**
(`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`). It reads *only* those 4 files.

**`repo_invariants_check.py --check --enforce-links`** (`run_pipeline.sh:217`),
gate at `:842`. Failure conditions (`run_check`, `:758-842`): ledger shard
parse/schema errors (`:765`), duplicate claim ids (`:767`), premises/obligations
registry untracked (`:768-771`), unexpected duplicate doc basenames (`:773-777`),
non-regular authority surfaces (`:779-784`), authority-surface links to
untracked/absolute/outside/directory/irregular targets (`:785-795`), class-F
registry/header violations (`:797-801`), unacknowledged citation-graph manifest
delta (`:803-826`). **Authority surfaces are only** `README.md`, `docs/repo/`,
`docs/publication/ci3_z3/`, `docs/audit/`, `docs/lanes/README.md`,
`docs/lanes/open_science/README.md` (`repo_invariants_check.py:84-91`).
`docs/work_history/` is not an authority surface, so nothing in it is
link-checked.

**`scripts/audit_model_family_normalization_guard.py`** (`run_pipeline.sh:89`):
model/family provenance compatibility only.

### A.4 Enforcement points outside the pipeline

- **CI (`.github/workflows/audit.yml`)** triggers on `schedule` (nightly
  06:00 UTC) and `workflow_dispatch` **only** (`audit.yml:22-25`). There is
  **no `pull_request` and no `push` trigger** — deliberately, per
  `audit.yml:12-17`. Runner-cache drift is reported with
  `echo "::warning::"` and never fails the job (`audit.yml:60-66`).
- **`pre_commit_audit_check.sh`** is opt-in (must be manually symlinked into
  `.git/hooks/pre-commit`) and bypassable with `--no-verify`. It runs
  `precompute_audit_runners.py --staged-only --check-only`, then — only if a
  `docs/**.md` is staged — materialize + graph + seed + `audit_lint.py` +
  `check_staged_claim_typing.py` + a "stage the shards" check.
- **`scripts/vocab_lint.py`** exists but is invoked by **no pipeline stage and
  no CI job**. `grep -rn vocab_lint docs/audit/scripts/run_pipeline.sh
  .github/workflows/audit.yml` → 0 hits. It is a *skill-instructed* step only
  (`review-loop/SKILL.md:63`, `audit-loop/SKILL.md:98`,
  `physics-loop/SKILL.md:89`), i.e. enforced by agent compliance, not machinery.

### A.5 The registration boundary (root mechanism)

`build_citation_graph.py:645-652` walks **every** `docs/**/*.md`, skipping only
`audit/` (`:38`), generated publication/repo files (`:39-45`), and class-F memos
(`:51`). So `docs/work_history/**` **is** in the citation graph — 4506 nodes.

`seed_audit_ledger.py:214-247` (`should_gate_node`) then **drops** any node
whose path matches `data/excluded_source_patterns.txt` unless it is listed in
`never_gate_source_paths.txt` (`:237-238`) or already carries audit history
(`:240-245`). `docs/work_history/**` is line 19 of
`docs/audit/data/excluded_source_patterns.txt`.

**Result: 4506 graph nodes → 3872 ledger rows. 634 nodes have no ledger row.**
An author's `**Type:**` header cannot rescue a note under an excluded path —
`should_gate_node` runs before `default_claim_type_for`.

---

## (b) DEFECT CLASSES — CAUGHT or NOT CAUGHT

### (1) A note with a linked runner but no claim_id and no ledger row — **NOT CAUGHT**

**Population.**

| Measure | Count |
|---|---|
| Citation-graph nodes with **no** ledger row | **634** |
| …of those, carrying a `runner_path` | **350** (all 350 runner files exist on disk) |
| …under `docs/work_history/repo/` | **322** |
| `docs/work_history/repo/review_feedback/*.md` | **450** |
| …that reference an existing `scripts/*.py` | **401** |
| …**of those 401, with a ledger row** | **0** |
| …dated `2026-07-14` | **127** |

```bash
python3 - <<'PY'
import json
g=json.load(open('docs/audit/data/citation_graph.json'))
L=json.load(open('docs/audit/data/audit_ledger.json'))['rows']
m=[(c,n) for c,n in g['nodes'].items() if c not in L]
print(len(m), sum(1 for c,n in m if n.get('runner_path')))
PY
```

**The four named surfaces.** All four are graph nodes, none is a ledger row,
each names an existing runner, none of the four runners has a cache:

| Note (`docs/work_history/repo/review_feedback/…`) | Runner named | ledger row | cache |
|---|---|---|---|
| `QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:146` | `scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py` | none | none |
| `SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md` | `scripts/single_invariant_action_steelman_attack_probe_2026_07_14.py` | none | none |
| `RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md` | `scripts/relational_qubit_disagreement_canonical_law_escalation_probe_2026_07_14.py` | none | none |
| `FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md` | `scripts/full_law_inventory_adversarial_reduction_probe_2026_07_14.py` | none | none |

(The brief said "two runners"; there are in fact **four**, one per note. **135**
`scripts/*_2026_07_14.py` exist; **0** of them have a cache in
`logs/runner-cache/`.)

**Why nothing found them.** The four form a **closed citation island entirely
inside unregistered `work_history/`**. In-degree of
`qubit_symmetry_…` is 2 — both citers are themselves unregistered
`work_history/` notes. In-degree of `full_law_inventory_…` is **0**. **No
ledger row cites any of the four.** They are invisible to the ledger, the
audit queue, `FRONT_DOOR_STATUS.md`, and every retained-side view.

**Compounding capture bug.** The graph shows `runner_path=None` for all four
even though the runner is in the text.
`build_citation_graph.extract_runner` (`:551-588`) recognises only bold
`**Runner:**`-style labels (`RUNNER_LABEL_RE`, `:116-125`) or headings matching
`RUNNER_SECTION_RE` (`:129-133` — `Artifact|Script|Runner|Files|Surfaces|What
was tested`). These notes use `## Verification` + a `bash` fence at line 146.
The `preamble` fallback is explicitly disabled for `work_history/` (`:577`),
and the last-resort fallback only scans `lines[:80]` (`:584-586`).

> **173 notes repo-wide mention an existing `scripts/*.py` while the graph
> captured no `runner_path`. 57 of those 173 DO have a ledger row** — i.e. 57
> audited-lane rows are missing their runner from the audit packet.

**Which check would have caught it: none.**
`check_staged_claim_typing.py:51-54` `continue`s on `hit is None`.
`audit_lint` iterates `ledger["rows"]` only (`:723`, `:781`) — a note without a
row is not iterated. `repo_invariants_check` does not treat `work_history/` as
an authority surface. Grepping the lint output for the four surfaces or their
runners returns **0 matches**.

### (2) A runner in `scripts/` referenced by no claim-bearing note — **NOT CAUGHT**

| Measure | Count |
|---|---|
| `scripts/*.py` on disk | 5243 |
| Bound to a ledger row (primary + helper) | 3674 |
| Bound to any citation-graph node | 4083 |
| **Bound to NO ledger row** | **1569** |
| **Bound to no graph node at all** | **1161** |
| Ledger-orphan runners that nonetheless have a cache | 169 |

The only reverse-direction hygiene that exists is
`precompute_audit_runners.cleanup_orphans` (`:317-340`), which deletes *caches
whose runner file is gone*. Nothing anywhere asks "does this runner belong to a
claim?" No lint category, no invariant, no CI step.

### (3) A note whose prose asserts a status contradicting its live ledger row — **NOT CAUGHT (and not-caught by explicit design)**

`audit_lint` reads note bodies at exactly one place — `:787-798`, and only to
feed `no_go_discipline_gate.source_requires_no_go_discipline`. It **never**
parses a status assertion. `docs/audit/README.md:62-64` states the policy:

> "Authors may write whatever status prose they need inside source notes, but
> the retained library is driven only by auditor-owned fields"

So this is a deliberate orthogonality invariant, not an oversight — but it was
written for *human* readers who consult the ledger. Agents read prose.

**Measured divergence (high-precision pass: "retained" within ≤4 tokens of a
markdown link or backticked `.md`, negation-filtered on the preceding 40 chars):**

| Measure | Count |
|---|---|
| Lines falsely asserting a target is retained-grade | **199** |
| Distinct asserting ledger rows | **90** |
| Distinct falsely-labelled targets | **110** |
| Target live status: `unaudited` / `audited_conditional` / `meta` | 182 / 10 / 7 |
| **Asserting rows that are themselves retained-grade** | **0** |

Self-assertions (`**Status:** RETAINED…` on a non-retained row) are rare: **4
lines across 2 claim ids** (`DM_ABCC_SIGNATURE_FORCING_THEOREM_NOTE_2026-04-19.md:336,412`;
`SCALAR_SELECTOR_FULL_STACK_RECOVERY_NOTE_2026-04-19.md:55,69`). The class is
overwhelmingly **cross-note**, not self-labelling.

### (4) Two notes mutually asserting each other retained while both unaudited — **NOT CAUGHT**

Same mechanism as (3): no prose is read. Strict mutual-pair search over
markdown links → **0 pairs**. Widening to backticked `.md` references (the
graph parser emits zero edges for those — repo memory, confirmed at
`build_citation_graph.py:135` `LINK_RE`) → **1 pair, both sides unaudited**:

- `docs/WILSON_CORRECTED_V_TASTE_TREE_LEVEL_BOUNDED_NOTE_2026-05-08.md:62`
  asserts "…**retained** mean-field staggered anti-Hermiticity in
  [`HIGGS_MASS_FROM_AXIOM_NOTE.md`]" — that row is
  `audit_status=unaudited`, `effective_status=unaudited`.
- `docs/HIGGS_MASS_FROM_AXIOM_NOTE.md:605` names the Wilson note as one that
  "cites this note as its load-bearing parent"; that row is also
  `unaudited`/`unaudited`.

(The prose-divergence brief counts this class differently — 44 across 14 ids in
one lane. My number is a conservative lower bound under a link-adjacency
definition. The CAUGHT/NOT-CAUGHT determination is unaffected: **no check reads
note prose for status at all**, so no count of instances changes the verdict.)

### (5) A registered obligation whose registry target omits a binding conjunct — **NOT CAUGHT** *(confirmed live instance)*

`audit_lint.py:712-713` is the entire target check:

```python
if not entry.get("target"):
    errors.append(f"derivation obligation {dep_id!r} lacks target")
```

It tests non-emptiness. It never compares the registry string to the note's
`## Exact target` section, nor to the audited `claim_scope` on the row.

**Live instance — `ac_reta_hclass_hunit_readout_derivation_obligation`:**

- `docs/audit/data/derivation_obligations.json:21` — target: "…with no extra
  **normalization or transport** factor."
- `docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md:11-13` — "…with no
  extra **clock-rate, transport, or normalization** factor."
- Ledger `claim_scope` (`docs/audit/data/ledger/ac/ac_reta_hclass_hunit_readout_derivation_obligation.json`)
  — "…without an additional **normalization, transport, or clock-rate** factor."

**The machine registry drops `clock-rate`, a conjunct that both the source note
and the audited scope treat as binding.** 1 of 3 registered obligations (33%)
carries a substantive omission; the other two agree modulo backticks and one
dropped qualifier ("from the retained framework chain", "quark-sector"→"quark"
on `theta_quark_…`).

### (6) A gate named in MINIMAL_AXIOMS with no node, row, or closure criterion — **NOT CAUGHT**

`docs/MINIMAL_AXIOMS_2026-06-29.md:159-172` ("Open Gates Outside The Axioms")
names **8 gate bullets**. Registered machine nodes total **7**: 4 in
`axiom_premise_nodes.json` (`minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) and 3 in
`derivation_obligations.json`. **There is no mapping between the two sets and
no script that reads that section.**

`MINIMAL_AXIOMS_2026-06-29.md:170` — "`- source/action and physical-observable
identification;`" — has no registry node and no closure criterion. Twelve
ledger rows have `source_action`/`observable_identification` in their claim id
(e.g. `yt_source_action_support_packet_note_2026-05-22`, `audited_conditional`;
`signed_gravity_source_action_escape_hatch_note`, `open_gate`/`unaudited`), but
none is *the* gate node and nothing binds them to the memo bullet.

The only script that touches `MINIMAL_AXIOMS` content is
`check_axiom_premise_clean.py`, and it only scans for 6 forbidden ratification
markers. `audit_lint`'s front-door check (`:733-763`) verifies that 8 listed
surfaces *link to* the memo — never that the memo's own gate list is
registered.

### (7) A note-linked runner whose cache is missing — **NOT CAUGHT** (CI warning only)

| Measure | Count |
|---|---|
| Ledger rows with a `runner_path` | 3649 |
| …whose primary runner has **no cache file** | **16** |
| Unregistered graph nodes with a runner | 350 |
| …with **no cache file** | **329** |
| Distinct **helper** runners across the audit queue | 381 |
| …with **no cache file** | **80** |
| **Queue entries marked `ready=True` whose PRIMARY runner has no cache** | **9 of 13** |
| **Queue entries marked `ready=True` with an uncached HELPER** | **56** |

`cache_freshness` is computed in `compute_audit_queue.py:267` via
`runner_cache.cache_status` (`scripts/runner_cache.py:395-420`), and the only
validation is an **enum-membership test** (`compute_audit_queue.py:411-414`) —
`"missing"` is a *permitted value*. Readiness is computed by `is_ready`
(`compute_audit_queue.py:64-80`) purely from dependency status; it never
consults the cache. `audit_lint` never reads `cache_freshness` at all.
CI's only cache check is a non-blocking `::warning::` (`audit.yml:60-66`).

**This is the mechanism behind the prior failed audit round in repo memory:
56 rows are offered to auditors as `ready` while a helper runner in their
packet has no evidence artifact.**

### Summary table

| # | Defect class | Verdict | Live count |
|---|---|---|---|
| 1 | Runner-bearing note, no claim_id / no ledger row | **NOT CAUGHT** | 350 graph nodes; 401 in `review_feedback/` alone |
| 2 | Runner referenced by no claim-bearing note | **NOT CAUGHT** | 1569 (1161 with no graph node at all) |
| 3 | Prose status contradicts live ledger row | **NOT CAUGHT** (by design) | 199 lines / 90 rows / 110 targets |
| 4 | Mutual retained-assertion between unaudited notes | **NOT CAUGHT** | ≥1 confirmed pair |
| 5 | Obligation registry target omits a binding conjunct | **NOT CAUGHT** | 1 of 3 obligations |
| 6 | Named gate with no node / row / closure criterion | **NOT CAUGHT** | 8 memo bullets vs 7 registry nodes; `:170` unregistered |
| 7 | Note-linked runner with missing cache | **NOT CAUGHT** (CI warning) | 16 primary + 80 helper; 56 `ready` rows affected |

**7 of 7 NOT CAUGHT.**

---

## (c) LINT RULE DESIGNS

Design constraints observed throughout: (i) `audit_lint` already distinguishes
blocking errors from non-blocking warnings/notices; (ii) `note_hash` drift is a
notice for non-retained rows and an error for retained-grade rows
(`audit_lint.py:1367-1389`; `review-loop/SKILL.md:877-890`) — the same
severity split is the right template; (iii) the repo already has a
*ratchet* pattern that blocks NEW instances while leaving legacy as a visible
worklist (`check_staged_claim_typing.py` + `claim_type_defaulted`); every rule
below reuses it. **All are tooling changes: zero note edits, zero `note_hash`
changes, zero requeues.**

### L1 — `unregistered_runner_bearing_note` (defect 1) — *highest value*

**Two components.**

**L1a — pre-commit ratchet (ERROR, blocks new instances).** New file
`docs/audit/scripts/check_staged_runner_ownership.py`, wired into
`pre_commit_audit_check.sh` immediately after the `check_staged_claim_typing.py`
call, and — critically — the `hit is None` `continue` at
`check_staged_claim_typing.py:51-54` must stop being a silent skip.

```
INPUT: staged repo-relative paths on stdin (same contract as check_staged_claim_typing.py)
For each staged path P where P.startswith("docs/") and P.endswith(".md"):
    body = read(P)
    runners = {m for m in RUNNER_PATH_RE.finditer(body)
               if normalize_runner_path(m) is not None}     # reuse build_citation_graph helpers
    if not runners:                     continue            # narrative note: fine
    row = ledger.rows_by_note_path.get(P)
    if row is not None:                 continue            # owned: fine
    if P in never_gate_source_paths:    continue
    EMIT ERROR:
      f"{P} names runner(s) {sorted(runners)} but seeding produced no ledger row "
      f"(matches data/excluded_source_patterns.txt). A runner-gated result must be "
      f"owned: move the note out of the excluded path, or register it in "
      f"docs/audit/data/never_gate_source_paths.txt, or delete the runner reference "
      f"if the note is narrative only."
```

**L1b — corpus notice in `audit_lint.py` (NOTICE, never blocks).** Insert after
the existing per-row loop (i.e. after `audit_lint.py:1397`), iterating the
citation graph rather than the ledger:

```
for cid, node in graph["nodes"].items():
    if cid in rows:                                   continue
    runners = [node["runner_path"], *node.get("helper_runner_paths", [])]
    runners = [r for r in runners if r and (REPO_ROOT / r).exists()]
    if not runners:                                   continue
    add_notice("unregistered_runner_bearing_note",
               f"{node['path']}: names runner(s) {runners} but has no ledger row; "
               "runner-gated result is unowned and invisible to the audit queue")
```

- **Severity:** L1a ERROR (ratchet on new), L1b NOTICE (legacy worklist).
  Making L1b an error today would emit **350** errors and hard-block the
  pipeline — unacceptable; the notice makes the backlog countable and
  drainable exactly like `claim_type_defaulted`.
- **Emits today:** L1b → **350** notices (322 under `work_history/repo/`).
  L1a → 0 on a clean tree; fires on the next such commit.
- **False-positive risk: LOW-MODERATE.** A genuinely narrative note that
  *mentions* a runner path in passing (e.g. a session summary listing what ran)
  would be flagged. Mitigations: (i) `normalize_runner_path` already requires
  the file to exist on disk; (ii) exempt paths registered in
  `data/meta_source_patterns.txt`; (iii) for L1a only, require the mention to
  be inside a fenced block or a `Run:`/`Verification`/`Runner` section, which
  is the same signal `extract_runner` looks for. Residual false positives are
  cheap: the author adds the path to `meta_source_patterns.txt` or drops the
  runner reference.

### L2 — `runner_extraction_miss` (defect 1, capture half) — *cheapest real win*

Two sub-parts, both zero-churn:

**L2a — widen `RUNNER_SECTION_RE`** (`build_citation_graph.py:129-133`) to
include `Verification|Verify|Reproduce|Reproduction|How\s+to\s+run|Check(?:s)?`,
and raise the last-resort window at `:584` from `lines[:80]` to the whole body
when exactly one distinct existing runner path appears (the uniqueness test
already guards against ambiguity).

**L2b — new lint NOTICE** at the same insertion point as L1b, over ledger rows:

```
if row.get("runner_path") is None and node_for(cid) is not None:
    mentioned = {p for p in RUNNER_PATH_RE-scan(note_body) if exists(p)}
    if mentioned:
        add_notice("runner_extraction_miss",
                   f"{cid}: note names runner(s) {sorted(mentioned)} but the graph "
                   "captured none; the audit packet will omit the runner")
```

- **Severity:** NOTICE. **Emits today:** L2b → **57** (the ledger-row subset of
  the 173). After L2a lands, that number should drop sharply — L2a is a
  *parser* change, so it costs zero note edits, but it **does** change
  `citation_graph.json`, so `repo_invariants_check`'s manifest-acknowledgment
  gate (`:803-826`) will require a refreshed
  `docs/audit/data/citation_graph_manifest.json`. Newly-attached runners flow
  into `runner_cache_state`, which is part of the audit-state snapshot — so
  L2a's real cost is measured by running the pipeline in validation mode and
  reading `invalidate_stale_audits.py` counts before landing. Land L2b first
  (pure notice, zero effect), then L2a as its own reviewed change with its
  requeue count measured.
- **False-positive risk: LOW** for L2b (it only reports; the runner path must
  exist on disk). MODERATE for L2a — a widened heading regex could attach the
  *wrong* runner on a note that lists several; the existing `len(top_paths)==1`
  uniqueness guard is the mitigation and must be preserved.

### L3 — `orphan_runner_no_claim` (defect 2)

New lint NOTICE, ledger-independent:

```
known = {r["runner_path"] for r in rows.values()} | {h for r in rows.values()
         for h in (r.get("helper_runner_paths") or [])}
graph_known = same union over graph["nodes"]
for path in sorted(Path("scripts").glob("*.py")):
    if path in known or path in graph_known:        continue
    if path.name.startswith("_"):                   continue   # loaders/helpers
    add_notice("orphan_runner_no_claim",
               f"{path}: no note in the citation graph names this runner")
```

- **Severity:** NOTICE only. **Emits today: 1161.** This is a housekeeping
  signal, not an integrity signal — a runner with no note is inert, it cannot
  launder anything. Its value is as a *drain worklist* and as the reverse index
  that would have surfaced the 2026-07-14 material from the `scripts/` side.
- **False-positive risk: HIGH by volume, LOW by consequence.** Many are
  legitimately one-off exploration scripts. Recommend shipping it behind a
  `--report-orphan-runners` flag or writing it to
  `docs/audit/data/runner_ownership_report.json` rather than into the default
  lint output, so 1161 notices do not drown the 441 that already exist.

### L4 — `prose_status_contradicts_ledger` (defects 3 and 4)

New lint NOTICE. This is the rule that would have prevented an agent from
believing a false label.

```
RETAINED_WORD = r'\bretained(?:_no_go|_bounded|-grade)?\b|\baudited_clean\b'
REF           = markdown link to *.md  OR  backticked `*.md`
NEG           = not|no longer|non-retained|pending|awaiting|proposed|candidate|
                until|unless|once|if|would|toward|seek|fails?

for each ledger row R with a note on disk:
  for each line:
    for each match of  RETAINED_WORD (\s+\S+){0,4}? \s+ (in|from|per|:)? REF:
       if NEG matches the 40 chars preceding the RETAINED_WORD:  skip
       target = resolve REF -> claim_id (path first, then unique basename)
       if target is None:                                        skip
       t_eff = rows[target].effective_status
       if not is_retained_grade(t_eff):
          add_notice("prose_status_contradicts_ledger",
                     f"{R.note_path}:{lineno}: asserts {target} is retained-grade; "
                     f"live effective_status={t_eff!r}")
```

Plus a self-assertion variant on the note's own `**Status:**` line value.

- **Severity: NOTICE, not ERROR.** Two independent reasons. (i)
  `docs/audit/README.md:62-64` establishes prose/verdict orthogonality as a
  design invariant — an error would contradict a landed policy and should be an
  owner decision, not a lint author's. (ii) The corpus effect is that **0 of
  the 90 asserting rows are retained-grade**, so an error would block the
  pipeline over rows nobody's verdict depends on.
- **Emits today: 199** notices across 90 rows.
- **False-positive risk: MODERATE — the main design risk of this rule.**
  Legitimate patterns it can misfire on: historical narration ("this was
  retained in May, then demoted"), a note describing the *target state* of a
  program, and tables where "retained" is a column header adjacent to a link.
  Mitigations, in order of importance: (1) require the reference within 4 tokens
  — this alone took my count from 1191 loose lines to 199; (2) the negation
  lookbehind; (3) skip lines inside fenced code (reuse
  `audit_lint.mask_nonrendered_markdown`, `:328-475`, which already exists and
  is battle-tested); (4) skip blockquotes (same helper); (5) an
  opt-out marker the author can place on a line documenting history.
  Ship as a notice, tune the regex against the emitted list, and only then
  consider a ratchet on newly-staged notes.

### L5 — `obligation_target_divergence` (defect 5)

Extend the existing obligation block at `audit_lint.py:707-721`:

```
note_text  = read(entry["current_path"])
note_target = text of the "## Exact target" section (heading-delimited,
              via the existing extract_section pattern)
row_scope   = rows[dep_id].get("claim_scope") or ""

def content_tokens(s):   # backtick-, case-, punctuation-, whitespace-insensitive
    return set(re.findall(r"[a-z0-9][a-z0-9_-]{3,}", s.replace("`","").lower())) - STOPWORDS

reg = content_tokens(entry["target"])
for label, other in (("note '## Exact target'", note_target), ("ledger claim_scope", row_scope)):
    missing = content_tokens(other) - reg
    if missing:
        add_warning("obligation_target_divergence",
            f"{dep_id}: derivation_obligations.json target omits term(s) "
            f"{sorted(missing)} present in the {label}; the machine registry is "
            "the dispatch surface and must carry every binding conjunct")
```

- **Severity: WARNING.** Non-blocking (so it cannot brick the pipeline on a
  wording change) but louder than a notice, because the registry is what the
  dispatcher and the auditor read. There are only 3 obligations — this list is
  hand-auditable forever.
- **Emits today: 1** — `ac_reta_hclass_hunit_readout_derivation_obligation`,
  missing `clock-rate` (and, depending on stopword tuning, `chain`/`framework`
  on `theta_quark_…`).
- **False-positive risk: MODERATE, fully controllable.** Prose in the note's
  `## Exact target` will always contain words the one-line registry target
  omits. Mitigations: a curated `STOPWORDS` list; restrict comparison to the
  *first sentence* of `## Exact target`; and, strongest, seed the check with an
  explicit `binding_conjuncts: [...]` array per obligation in
  `derivation_obligations.json` and require registry-target coverage of that
  array instead of free-text diffing. With 3 obligations, the explicit-array
  form is cheap and has essentially zero false positives — **recommended**.

### L6 — `unregistered_named_gate` (defect 6)

The memo section is the source of truth; give it a machine mirror.

```
# in audit_lint.py, near the existing front-door check (:733-763)
memo   = read(axiom_registry.nodes.minimal_axioms.current_path)
bullets = bullet items under the "## Open Gates Outside The Axioms" heading
registry = data/named_gate_registry.json    # NEW controlled file
if set(registry["gates"]) != set(bullets):           # normalized text
    errors.append("named_gate_registry.json does not match the axiom memo's "
                  "'Open Gates Outside The Axioms' bullets: "
                  f"added={...} removed={...}")
for gate_id, entry in registry["gates"].items():
    if not entry.get("closure_criterion"):
        add_warning("unregistered_named_gate",
                    f"{gate_id}: named in {memo_path}:{lineno} with no closure criterion")
    for cid in entry.get("claim_ids", []):
        if cid not in rows:
            errors.append(f"named gate {gate_id} references unknown claim id {cid}")
    if not entry.get("claim_ids"):
        add_warning("unregistered_named_gate",
                    f"{gate_id}: named in {memo_path}:{lineno} with no ledger row")
```

- **Severity:** ERROR on *registry/memo set mismatch* (mechanical, and the
  memo is edited only by owner-approved axiom resets — the same fail-closed
  logic that justifies the existing front-door pointer error at `:750-763`);
  WARNING on a gate lacking a closure criterion or claim ids (that is science
  work, not a mechanical repair).
- **Emits today:** the registry file does not exist, so the first landing
  creates it with 8 entries; **8 warnings** initially, of which
  `source/action and physical-observable identification`
  (`MINIMAL_AXIOMS_2026-06-29.md:170`) is the one the campaign named.
- **False-positive risk: LOW.** The only churn source is re-wording a bullet,
  which is already a controlled owner action. **Note the hard constraint:** the
  new file lives under `docs/audit/data/`, which
  `review-loop/SKILL.md:962-966` restores wholesale from `origin/main` before
  landing — so it must be introduced through the audit lane / owner, not a
  science PR (see §Constraint below).

### L7 — `note_linked_runner_cache_missing` (defect 7)

Two components again.

**L7a — audit_lint NOTICE / WARNING split.** Insert in the per-row loop
alongside the existing hash-drift check (`audit_lint.py:1360-1389`), mirroring
its severity logic:

```
for path in [row.runner_path, *row.helper_runner_paths]:
    if not path or not (REPO_ROOT/path).exists():   continue
    status = runner_cache.cache_status(path)        # scripts/runner_cache.py:395
    if status == "fresh":                            continue
    msg = f"{cid}: runner {path} cache is {status!r}"
    if is_retained_grade(row["effective_status"]):
        add_warning("retained_row_runner_cache_stale", msg + " (retained-grade row: "
                    "its evidence artifact is not reproducible from the repo)")
    else:
        add_notice("note_linked_runner_cache_missing", msg)
```

**L7b — queue readiness gate (the one that actually prevents wasted audits).**
In `compute_audit_queue.is_ready` (`:64-80`), add: a row is not `ready` when
its primary runner or any helper runner has `cache_status != "fresh"`. Emit the
reason into a new `blocker` value so the dispatcher can see it.

- **Severity:** L7a WARNING for retained-grade / NOTICE otherwise (exactly
  parallel to the note_hash split, which is the repo's established precedent
  and is documented in `review-loop/SKILL.md:877-890`). **Never an error** —
  caches are gitignored-adjacent build products and a fresh clone would
  hard-fail.
- **Emits today:** L7a → **16** primary + up to **80** helper occurrences.
  L7b → moves **9** currently-`ready` rows and **56** helper-affected rows out
  of `ready`. That is the whole point: those 56 are the rows that make an audit
  round fail on missing evidence.
- **False-positive risk: LOW.** `cache_status` already returns `"fresh"` when
  the runner file is absent (`runner_cache.py:402-403`), so deleted runners do
  not fire. The real cost is that L7b *shrinks* the ready queue from 589 —
  correctly, but the audit-loop operator must be told, and
  `precompute_audit_runners.py --all` must be run to refill it.

---

## (d) VERDICT ON THE OWNER QUESTION

> Is the failure (a) science never ENTERING the pipeline, (b) prose/ledger
> DIVERGENCE, (c) PIPELINE GAPS, (d) obligation/registry integrity, or (e) a
> combination — and in what proportions?

**Verdict: (c) PIPELINE GAPS is the root cause; (a) MISSING REGISTRATION is the
dominant symptom and where all the mass is. (b) is large in count and near-zero
in audit consequence. (d) is tiny in count and disproportionately severe.**

This matches the supervisor's pre-recorded prediction in `CAMPAIGN.md:73-82`.
The evidence:

**Proportions, by volume of affected surfaces:**

| Failure mode | Affected surfaces | Share |
|---|---|---|
| (a) unregistered runner-bearing science | **350** graph nodes (401 in `review_feedback/` alone) | **~62%** |
| (b) prose/ledger divergence | **90** ledger rows / 199 lines | ~16% |
| (a′) runner capture missed on registered rows | **57** ledger rows | ~10% |
| (7) runner-cache holes on note-linked runners | **16** primary + 80 helper | ~10% |
| (d) registry integrity | **1** obligation + **8** unmapped gate bullets | **~2%** |

**Proportions, by severity (what could actually corrupt a verdict):**

| Failure mode | Verdicts at risk today |
|---|---|
| (b) prose divergence | **0** — 0 of 90 asserting rows are retained-grade; 0 of 110 falsely-labelled targets are cited by a retained row through a recorded dep |
| (a) unregistered science | **0 directly** — but 100% of 401 runner-gated results are un-auditable, un-queueable, and un-findable |
| (7) cache holes | **56** `ready` rows would hand an auditor an incomplete packet |
| (d) registry integrity | **3** — 1 obligation dispatched against a target missing a binding conjunct, and it is `criticality: high`; 8 named gates with no closure criterion |

**Why (c) is the root and not merely a co-factor.** Three structural facts,
each independently sufficient:

1. **`check_staged_claim_typing.py:51-54` skips exactly the class of file that
   caused this campaign.** It is the only ratchet on new notes, and its
   `hit is None → continue` makes "no ledger row" the *passing* condition.
2. **`docs/work_history/**` is line 19 of `excluded_source_patterns.txt`, and
   `should_gate_node` (`seed_audit_ledger.py:214-247`) runs before claim-typing.**
   So an author writing `**Type:** bounded_theorem` on a `work_history/` note
   still gets no row. The directory is, mechanically, a write-only sink.
   Result: **401 of 450** `review_feedback/` notes reference an existing runner
   and **0** have a ledger row.
3. **CI never runs on a pull request or a push** (`audit.yml:22-25`). The whole
   pipeline is a nightly cron. The only per-change enforcement is an opt-in,
   `--no-verify`-bypassable git hook, plus agent compliance with skill text.

Given (1)-(3), any amount of author diligence would have produced the same
outcome: the toolchain had no place to say no.

**Why (b) is a red herring for audit capacity but a real hazard for agents.**
Zero retained-grade rows assert a false retained status, and zero false
assertions are recorded as deps — so the effective-status propagation is
*sound*. The damage is entirely on the reading side: an agent that greps for
"retained" and believes the answer is misled 199 times. That is a
**documentation-truth** problem, and it is cheap to fix (see Batch 4) precisely
because none of the 90 rows carries a verdict.

**Why (d) punches above its count.** The obligation registry is the surface a
dispatcher and an auditor read; a target missing `clock-rate` means a closing
theorem could be accepted that leaves a clock-rate factor undetermined, on a
`criticality: high` row. And 8 named gates with no closure criterion means the
framework's own memo describes a boundary the machine cannot see.

---

## PRIORITIZED, BATCHED REPAIR PLAN

**Hard constraint discovered, applies to every batch below.**
`review-loop/SKILL.md:962-966` restores `docs/audit/data/` **wholesale** from
`origin/main` before landing:

```bash
git checkout origin/main -- docs/audit/data/ docs/audit/AUDIT_QUEUE.md \
    docs/audit/MISSING_DERIVATION_PROMPTS.md \
    'docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md' \
    docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md
git clean -fd -- docs/audit/data/
```

That directory contains the *controlled* registration inputs —
`never_gate_source_paths.txt`, `excluded_source_patterns.txt`,
`meta_source_patterns.txt`, `derivation_obligations.json`. **A science PR
therefore cannot register an orphan by editing them.** The only science-PR-legal
registration route is to **move the note out of the excluded path**. Batches
that must edit `docs/audit/data/` are marked **[audit-lane / owner route]**.

---

### Batch 1 — L1a + L7b + fix the `check_staged_claim_typing` skip — **TOOLING** — *do this first*

| | |
|---|---|
| Files | `docs/audit/scripts/check_staged_runner_ownership.py` (new), `docs/audit/scripts/pre_commit_audit_check.sh`, `docs/audit/scripts/check_staged_claim_typing.py`, `docs/audit/scripts/compute_audit_queue.py` |
| Note edits | **0** |
| Rows requeued | **0** |
| Verdicts risked | **0** |
| Emits today | 0 (ratchet); L7b removes 9 + 56 rows from `ready` |
| Why worth it | Closes the exact hole that produced the campaign. Zero audit cost. Stops the backlog growing while everything else is decided. |

Ship `check_staged_runner_ownership.py` with an env/flag escape hatch for the
first week so it cannot wedge an in-flight loop.

### Batch 2 — L1b + L2b + L4 + L5 + L7a lint notices — **TOOLING**

| | |
|---|---|
| Files | `docs/audit/scripts/audit_lint.py` only |
| Note edits | **0** |
| Rows requeued | **0** |
| Verdicts risked | **0** |
| Emits today | +350 (`unregistered_runner_bearing_note`), +57 (`runner_extraction_miss`), +199 (`prose_status_contradicts_ledger`), +1 (`obligation_target_divergence`, WARNING), +16/+80 (cache) — total ≈ **703 new notices**, 0 new errors |
| Why worth it | Turns four invisible defect classes into countable, drainable worklists — the same mechanism that made `claim_type_defaulted` shrinkable. Notices never block, so the pipeline stays green. |

Ship L3 (`orphan_runner_no_claim`, 1161) to a JSON report, **not** to the
default lint output.

### Batch 3 — register the 2026-07-14 island — **CONTENT** — *owner science decision required*

| | |
|---|---|
| Files | the 4 named notes (+ up to 123 more dated 2026-07-14 with runners) |
| Route | Move out of `docs/work_history/repo/review_feedback/` into `docs/`, and replace `**Type:** meta` with the type the note as written actually is. **[audit-lane route also possible via `never_gate_source_paths.txt`.]** |
| Rows requeued | **0** — the notes have **no** ledger rows today, and **no ledger row cites any of the four** (in-degree from ledger rows = 0) |
| Verdicts risked | **0** |
| New rows created | 4 (or up to 127 if the whole date-slice is registered) |
| Side effect | Citation-graph manifest delta must be acknowledged (`repo_invariants_check.py:803-826`): 4 removed + 4 added nodes plus 3 intra-island edge rewires |
| Why worth it | This is the material two campaigns re-derived. Registering it is free in audit capacity and directly recovers the wasted waves. |

**Blocking caveat, must go to the owner:** all four carry
`**Type:** meta` and one carries `**Authority:** none`
(`QUBIT_SYMMETRY_…:5,7`). `docs/audit/README.md:202-205` warns that `meta`
"is reserved for documents that carry no claim any dependent could consume as
evidence" — and these were consumed as evidence by two campaigns. Retyping them
is an authoring judgement (`docs/audit/README.md:228-229`: "a header must
describe the note as written, never retype content to fit a desired class"),
**not** a mechanical
repair, and it must not be done by this lane. Recommend: register the **4**
named surfaces first as a reviewed pilot; decide the remaining 123 (and the 397
older `review_feedback/` runner notes) only after seeing what the pilot costs.

### Batch 4 — prose-divergence correction — **CONTENT** — *cheap, do after Batch 2*

| | |
|---|---|
| Files | the 90 asserting notes (199 lines) |
| Rows requeued | **0 terminal verdicts** |
| Verdicts risked | **0** — measured: **0 of 90** asserting rows are retained-grade, **0 of 90** carry any terminal verdict; all 90 are `unaudited` |
| Lint effect | 90 `note_hash_drift_reaudit_pending` **notices** (non-blocking, per `audit_lint.py:1384-1389`) |
| Why worth it | A note asserting a false status IS a science correction, not cosmetics (`CAMPAIGN.md:55-57`). It costs nothing here because the affected rows are entirely unaudited. Drive it from the L4 notice list, not from a blind sweep. |

Sequence matters: land L4 (Batch 2) first so the worklist is machine-generated
and the fix is verifiable by re-running the lint.

### Batch 5 — obligation + gate registry integrity — **[audit-lane / owner route]**

| | |
|---|---|
| Files | `docs/audit/data/derivation_obligations.json:21`; new `docs/audit/data/named_gate_registry.json`; `audit_lint.py` (L5 + L6) |
| Rows requeued | **0** — no source note is edited; the registry is machine data |
| Verdicts risked | **0** |
| Why worth it | Highest severity per unit of work in the whole plan. Restoring `clock-rate` to the reta target is a one-word edit that re-binds a `criticality: high` obligation to its audited scope. |

Preferred L5 implementation is the explicit `binding_conjuncts` array — with 3
obligations it is cheap and has near-zero false-positive risk.

### Batch 6 — runner-cache refill — **OPERATIONAL**

| | |
|---|---|
| Command | `python3 scripts/precompute_audit_runners.py --all` |
| Note edits | **0**; rows requeued **0**; verdicts risked **0** |
| Effect | Fills the 16 primary + 80 helper cache holes; restores the 9 + 56 rows that Batch 1's L7b would park |
| Why worth it | Must run *with* Batch 1 or the ready queue shrinks with no path to refill. |

### Batch 7 — L2a runner-capture parser widening — **TOOLING, but MEASURE FIRST**

| | |
|---|---|
| Files | `build_citation_graph.py:129-133`, `:584` |
| Note edits | **0** |
| Rows requeued | **UNKNOWN — must be measured before landing** |
| Why | Attaching a runner to a previously runner-less row changes `runner_cache_state` and the audit-state snapshot, and it changes `citation_graph_manifest.json`. Per the churn guard (`review-loop/SKILL.md:809-819`), run the pipeline in validation mode and read the `seed_audit_ledger.py` / `invalidate_stale_audits.py` counts **before** landing. Only 3 of the 57 affected rows carry a terminal verdict and only 1 is retained-grade, so the expected cost is small — but it must be shown, not assumed. |

### Explicitly NOT recommended

- **Mass cosmetic sweep over audited claim notes.** The one class that looks
  like it needs one — the **63** `legacy_backfill_scope` rows — is **100%
  retained-grade and 100% terminal**. Editing them would trip the hard
  `note_hash` error at `audit_lint.py:1380-1383` on all 63 and requeue every
  one. They cannot be repaired by editing at all: a real `claim_scope` can only
  be written by a re-audit. Leave them as notices.
- **Promoting L1b, L3, or L4 to error severity.** 350 / 1161 / 199 new errors
  would hard-block the pipeline (`audit_lint.py:1544`) with no drain path.

---

## MANDATORY FRAMEWORK REFRESHER — surfaces read

1. **`docs/MINIMAL_AXIOMS_2026-06-29.md`** (193 lines, read in full around the
   axiom statements and the gate list). Four axioms — Lattice/`Z^3`, Qubit
   (one-site `M_2(C)`), Admissibility (nearest-neighbour), Record (durable
   locking of one admissible local possibility, one-per-site uniqueness,
   permanence, finite scalar readout additivity; "Records form." is axiom
   content, every formation rule is not). `:159-172` "Open Gates Outside The
   Axioms" — 8 bullets, including `:170` "source/action and physical-observable
   identification", the unregistered gate measured above.
2. **`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`** (46 lines, full).
   Three approved primitives — `scale_reference_primitive`,
   `kinetic_isotropy_primitive`, `realized_state_primitive`. They chain-satisfy
   deps without conferring `retained_bounded`; §5 "do not grant more than the
   primitive source note declares"; §6 any proposed primitive absent from the
   registry is unapproved. **No new axiom, primitive, or vocabulary is proposed
   anywhere in this report.** Every rule name above reuses the existing lint
   category-string convention; every severity reuses the existing
   error/warning/notice trichotomy.
3. **`docs/audit/README.md`** (429 lines; §§ "Scope-aware fields",
   "Claim typing at authoring time", "The hard rules" read in full).
   Load-bearing for this analysis: `:62-64` prose/verdict orthogonality;
   `:174-193` the four-tier claim-typing precedence and
   `INFRA_META_PATH_PREFIXES`; `:202-205` the warning that `meta`
   chain-satisfies dependents and must be reserved for documents carrying no
   consumable claim; `:242-245` "Retained grade is audit-only… Author labels
   and source-note status prose do not promote rows."
4. **`docs/audit/data/axiom_premise_nodes.json`** — 4 nodes
   (`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
   `realized_state_primitive`), each with a `current_path` that
   `check_axiom_premise_clean.py` scans and `audit_lint.py:742-763` uses for the
   front-door pointer gate.
5. Additionally, as instructed: **`docs/ai_methodology/skills/review-loop/SKILL.md`**
   — `:809-819` the audit-hash churn guard, `:877-890` the note_hash
   notice/error split, `:962-966` the generated-output restore list (which
   produced the Batch-3 routing constraint).

**Compliance statement.** No audit verdict is set, predicted, or implied
anywhere in this report. No `audited_*` or `retained*` value is proposed for
any note. Every count is reproducible from `origin/main` @ `f865c14cd4` with
the commands shown. Nothing was committed, pushed, or opened as a PR; the only
file written is this report.
