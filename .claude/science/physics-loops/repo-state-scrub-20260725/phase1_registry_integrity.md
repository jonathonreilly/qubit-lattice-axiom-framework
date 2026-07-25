# Phase 1 — Registry Integrity Audit

**Brief:** audit the registries themselves for internal consistency (a) derivation
obligations, (b) axiom premise nodes, (c) the `no_go` population, (d) lane gating
data, (e) prioritized repair with churn cost.

**Measurement base:** `origin/main` at `f865c14cd4` (fetched 2026-07-25). The
worktree HEAD `13644707d8` is **290 commits behind**, so every number below was
taken from a clean extract of `origin/main`, not the worktree:

```bash
git fetch origin --prune
git archive origin/main | tar -x -C "$SCRATCH/main"      # 20180 files, 241 MB
```

Ledger index used throughout (**3872 rows**, one per shard under
`docs/audit/data/ledger/<id[:2]>/<id>.json`):

```bash
python3 - <<'PY'
import json, pathlib, collections
rows = {}
for p in pathlib.Path("docs/audit/data/ledger").rglob("*.json"):
    d = json.loads(p.read_text()); rows[d.get("claim_id") or p.stem] = d
print(len(rows), collections.Counter(r.get("claim_type") for r in rows.values()))
PY
```

No prose status label was trusted anywhere in this report. Every status comes
from a ledger shard or from `docs/audit/data/effective_status_summary.json`
(itself pipeline-generated on `origin/main`).

**Nothing was committed, pushed, or PR'd. Only this report file was written.**

---

## Headline counts

| Question | Count |
|---|---|
| Registered derivation obligations | **3** |
| Obligations whose machine record MISMATCHES its source note | **3 of 3 (100%)** |
| Distinct registry↔note mismatches | **6** |
| Registered axiom/primitive nodes | **4** |
| Nodes whose registry `note` diverges from the source note | **2 of 4** |
| Registry `note` fields read by any tool | **0** |
| Gate bullets in `MINIMAL_AXIOMS_2026-06-29.md` "Open Gates" | **8** |
| Of those, with a `derivation_obligations.json` entry | **2 bullets, partially** |
| Fully unregistered gate bullets (incl. `:170`) | **5** |
| `no_go` rows | **439** (brief said 438; +1 since) |
| `no_go` rows `unaudited` | **438** |
| `no_go` rows at `retained_no_go` | **0** |
| `no_go` rows that HELD `audited_clean` historically | **196** |
| `no_go` clean audits killed on 2026-07-11/12 | **202** |
| `no_go` rows audited in the last 13 days (of 370 audits) | **0** |
| Lanes certified (of 4) | **0** |
| Lane blockers that are `meta` rows (structurally unclearable) | **20** |

---

## (a) `derivation_obligations.json` vs source notes — 3/3 DEFECTIVE, 6 mismatches

Registry: `docs/audit/data/derivation_obligations.json` (3 entries, 35 lines).
Reproduce with:

```bash
python3 "$SCRATCH/oblig_check.py" "$SCRATCH/main"   # script listed at the end
```

The comparison is mechanical: registry `target` vs the note's `## Exact target`
first paragraph; registry `self_liquidation_condition` vs the note's
`## Closure criterion` and the ledger row's `notes_for_re_audit_if_any`.

### A-1 `ac_orbit_occupancy_statistical_grain_derivation_obligation` — 1 mismatch

`target` matches the note exactly (string-equal after backtick/whitespace
normalization). The defect is in the closure condition.

- Registry `derivation_obligations.json:15`:
  `"A retained kappa/counting-rule theorem deriving this exact grain removes the obligation; until then it blocks dependent closure."`
- Note `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21-24`:
  `"A closing theorem must derive the physical matter action and its measure, then distinguish the count-once det_C/holomorphic realization from the count-twice |det_C|^2/realified realization without inserting the desired charged-lepton value or readout dictionary."`
- Ledger row `docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json`,
  `notes_for_re_audit_if_any.missing_bridge_theorem`:
  `"supply an independently auditable derivation of the physical matter action and measure that selects det_C rather than |det_C|^2, without inserting the target readout."`

**MISMATCH:** the registry omits the *derive the physical matter action and its
measure* conjunct and the *without inserting the desired value/readout dictionary*
guard. The auditor's own re-audit note treats both as binding. This is the
instance named in the campaign brief — **confirmed**.

The registry's `self_liquidation_condition` is in fact a paraphrase of the note's
`## Running-program relation` paragraph (lines 35-38), **not** of `## Closure
criterion`. The same substitution occurs in all three entries, so this is a
systematic construction error, not a one-off typo.

### A-2 `ac_reta_hclass_hunit_readout_derivation_obligation` — 2 mismatches

**MISMATCH (target text).** Diff ratio 0.904:

- Registry `derivation_obligations.json:21`: `"... with no extra normalization or transport factor."`
- Note `docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md:11-13`: `"... with no extra clock-rate, transport, or normalization factor."`

The registry **drops `clock-rate`** from the excluded-factor list (and drops the
`h` label on the density class). A closing theorem that admitted a clock-rate
factor would satisfy the registry target and violate the note's target. Given
that the AC/R-eta lane's live physics is exactly about clock-rate/normalization
readout, this omission is load-bearing, not cosmetic.

**MISMATCH (closure).** Registry `:23` says only `"A retained G3/angle-readout
theorem deriving this exact identity removes the obligation"`. The note `:21-25`
requires `"a physical carrier/source-action bridge and either a native
eta/holonomy identity or a genuinely inhomogeneous Record-facing normalization
theorem"`. The ledger row's `notes_for_re_audit_if_any.missing_bridge_theorem`
agrees with the note: `"add and independently audit the carrier/source-action
and density-to-angle normalization theorem"`. The **carrier/source-action bridge
conjunct is absent from the registry entirely.**

### A-3 `theta_quark_determinant_cross_sector_readout_derivation_obligation` — 3 mismatches

**MISMATCH (target text).** Diff ratio 0.894. Registry `:29` drops the provenance
restriction `"from the retained framework chain"` that the note carries at
`docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md:11`,
and narrows `"quark-sector determinant readout"` to `"quark determinant readout"`.
Entries A-1 and A-2 both carry the provenance clause, so this entry is
inconsistent with its own siblings.

**MISMATCH (closure).** Registry `:31` compresses to `"A retained cross-sector
determinant-readout theorem removes the obligation"`. The note `:21-26` names
**three** conjuncts plus an insufficiency clause: `"must construct the quark
mass/determinant carrier, identify the physical readout map, and prove the
cross-sector correspondence ... Algebraic similarity, shared notation, and
historical decision text are insufficient."` The ledger row's re-audit note names
**four**: carrier, physical readout, K/CPT correspondence, resulting determinant
phase.

**MISMATCH (provenance).** Registry `:32` asserts
`"historical_governance_source": "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md"`.
That document is **not cited anywhere in the source note** (A-1 and A-2 both cite
it at their lines 15-17; the theta note does not). The registry attributes a
governance provenance the note does not claim.

### A-4 The lint gap that lets all six through

`docs/audit/scripts/audit_lint.py:707-721` is the entire obligation check:

```python
for dep_id, entry in sorted(nodes.items()):
    if dep_id not in rows:                 errors.append(... "has no ledger row")
    if premise_nodes.is_accepted_premise_dep(dep_id): errors.append(... "incorrectly accepted")
    if not entry.get("target"):            errors.append(... "lacks target")
    source_path = entry.get("current_path")
    if not source_path:                    errors.append(... "lacks current_path")
    elif not (REPO_ROOT / source_path).exists(): errors.append(... "missing on disk")
```

It never opens the source note. `target` is checked for **truthiness only**.
`self_liquidation_condition` is **never read at all** — no lint rule anywhere in
the repo references that key. Confirmed by:

```bash
grep -rn "self_liquidation_condition" docs/audit/scripts/ scripts/   # -> 0 hits
```

**A-5 Second lint gap (not in the brief, found here).** `audit_lint.py:707-721`
also never checks that a registered obligation's ledger row has
`claim_type == "open_gate"`. The registry's own preamble
(`derivation_obligations.json:3`) promises entries `"never satisfy dependency
closure, never bound or promote downstream rows"`. That invariant is enforced
*only* by `compute_effective_status.py:107-108`, which returns `open_gate` for
`claim_type == "open_gate"`. If any obligation row were retyped to
`bounded_theorem` and audited clean, it would become `retained_bounded`, which
`is_chain_satisfying_status` accepts — laundering an open obligation into a
premise. Nothing catches that. Blast radius if it happened: the three obligations
carry **101 + 106 + 8 = 215 transitive descendants** and `direct_in_degree`
**16 + 14 + 6 = 36**.

---

## (b) `axiom_premise_nodes.json` — 4 nodes, all resolve; 2 registry-note divergences; 5 unregistered gates

### B-1 Structural integrity: clean

`canonical_ids == set(nodes)`; all four `current_path` values exist on disk; all
four have a ledger row (`claim_type: meta`, `effective_status: meta`); no
`legacy_claim_ids` still occupy live ledger rows; no node's source note is missing
or superseded (`MINIMAL_AXIOMS_2026-06-29.md` is the current memo and the three
superseded aliases are correctly listed).

`docs/audit/scripts/check_axiom_premise_clean.py` passes on all four.

### B-2 The registry `note` field is read by NOTHING

```bash
grep -rn 'get("note")' docs/audit/scripts/premise_nodes.py     # -> 0 hits
```

`premise_nodes.py` exposes only ids (`:33 foundational_premise_ids`,
`:50 axiom_premise_ids`, `:55 accepted_premise_ids`, `:70 non_evidence_context_ids`).
`scripts/codex_audit_runner.py:1005-1013` loads the registry **only** to collect
`current_path` values into `allowed_context_paths`. So the 1,100-word normative
paraphrase at `axiom_premise_nodes.json:25` is dead documentation: no tool reads
it, and no lint reconciles it against the memo it paraphrases. This is why the
next two divergences went unnoticed.

### B-3 DIVERGENCE — `minimal_axioms` registry note vs the memo's withholding list

`MINIMAL_AXIOMS_2026-06-29.md:130-134` names what rows must cite separate
authority for:

> "Rows that require P2/modulus, log-det, source/action, measurement, Born
> weights, readout-context selection, central-sector decomposition, `K`/CPT
> structure, transition relations, record-production dynamics, physical
> persistence dynamics, local observability, or any other additional bridge must
> cite separate retained authorities"

`axiom_premise_nodes.json:25` closes with its own list. Reconciling item by item,
**4 memo items are absent from the registry note**: `P2/modulus`, `log-det`,
`Born weights`, `local observability`. (`transition relations` is only loosely
covered by the registry's `update law`.) The registry adds five that the memo's
sentence does not carry: `law-domain derivation`, `law-level dependence on an
unfixed choice`, `downstream theory consequence`, `state-selection rule`,
`physical observable bridge` — of which `physical observable bridge` and
`state-selection rule` are supported elsewhere in the memo (`:170`, `:107-111`),
so the *additions* are mostly benign. The *omissions* are not: the registry's
paraphrase of the axiom node silently permits four bridges the memo withholds.

Severity is limited by B-2 (nothing reads it). It becomes severe the moment any
tool starts rendering the registry note as premise context.

### B-4 DIVERGENCE — `scale_reference_primitive` registry note grants LESS than the note

- Source note `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md:15-17`:
  `"The framework takes exactly one dimensionful reference ... The chosen reference is the Planck mass scale, a^{-1} = M_Pl."`
- Skill surface `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md:23-28`:
  `"This grants the single dimensionful scale reference a^{-1} = M_Pl as a units conversion only."`
- Registry `axiom_premise_nodes.json:33`:
  `"Explicitly approved framework primitive for the single dimensionful scale reference a^{-1}. Units conversion only ... does not assert a/l_P=1."`

The machine registry is the **only** one of the three surfaces that omits `= M_Pl`.
Per `PRIMITIVE_REGISTRY_CHECK.md:13-16` ("Do not grant more than the primitive
source note declares"), a worker reading only the registry would under-grant; a
worker reading only the note would take the Planck-mass pin as approved premise.
Two surfaces disagree about what the sole dimensionful primitive supplies.

**Named tension for owner adjudication (NOT a verdict, NOT a defect claim).**
`MINIMAL_AXIOMS_2026-06-29.md:172-173` lists as an OPEN GATE
`"the scale-reference primitive and the separate gravity self-consistency
question that the framework's natural unit equals the Planck length."`
The source note at `:17` pins `a^{-1} = M_Pl` while at `:39-41` disclaiming
`a/l_P = 1`. In `hbar = c = 1` these differ only by the reduced-vs-non-reduced
Planck convention. I am **not** asserting a contradiction — the disclaimer is
stated identically on all three surfaces, so it is a deliberate, consistently
worded convention. But the open gate at `:172-173` and the pin at `:17` are about
the same identification up to that convention factor, and no registry entry
records which convention makes them compatible. This wants an explicit sentence,
not a silent parallel.

`kinetic_isotropy_primitive` and `realized_state_primitive`: registry notes are
faithful summaries of `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` and
`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` respectively, including the
policing clauses and the past-hypothesis exclusion. **No mismatch found.**

### B-5 UNREGISTERED GATES — full enumeration of `MINIMAL_AXIOMS_2026-06-29.md:156-173`

The memo's `## Open Gates Outside The Axioms` section names **8 bullets**.
"Registered" here means: has an entry in `docs/audit/data/derivation_obligations.json`,
the only machine registry for open derivation obligations (3 entries total).

| # | Line | Gate as named in the memo | Registry entry | Status |
|---|---|---|---|---|
| 1 | :161 | staggered-Dirac / finite-Grassmann realization **and** `AC_phi_lambda` | `ac_orbit_occupancy_...`, `ac_reta_hclass_...` | **PARTIAL** — the two AC obligations cover the occupancy grain and the h-class readout. The *staggered-Dirac / finite-Grassmann realization* conjunct is **unregistered** |
| 2 | :162 | strong-CP theta **gauge** and **mass-side** derivation obligations | `theta_quark_determinant_...` | **PARTIAL** — covers the mass-side determinant readout only. The *theta gauge* side is **unregistered** |
| 3 | :163 | P2/modulus/phase-blindness and any log-det readout theorem | — | **UNREGISTERED** |
| 4 | :164-167 | context selection, measurement basis selection, Born weights, probability rules, update laws, decoherence mechanisms, formation rules | — | **UNREGISTERED** |
| 5 | :168-169 | arrow, record-production dynamics, physical persistence dynamics, time metric, local observability of records | — | **UNREGISTERED** |
| 6 | **:170** | **source/action and physical-observable identification** | — | **UNREGISTERED** |
| 7 | :171 | `g_bare = 1` convention handling | — | **UNREGISTERED** |
| 8 | :172-173 | scale-reference primitive + gravity self-consistency (natural unit = Planck length) | primitive registered in `axiom_premise_nodes.json`; the **gate** is not | **UNREGISTERED (gate)** |

**5 bullets fully unregistered; 2 partially; 1 has its primitive registered but
not its gate.** The campaign's named instance (`:170`) is confirmed:

```bash
grep -rn "source/action and physical-observable identification" docs/ scripts/
```

returns the memo itself (`:170`) plus the two superseded memos, three prose notes
— and **11 occurrences across 6 ledger shards where auditors use the phrase as an
`evidence_locator` to CLOSE a route**, e.g.
`docs/audit/data/ledger/ga/gate_b_farfield_note.json:449`:

> `"CLOSED: the accepted axioms expressly withhold source/action and physical-observable identification, so this route cannot enlarge the bounded certificate."`

and `docs/audit/data/ledger/gr/gravity_full_self_consistency_note.json:301`,
`docs/audit/data/ledger/fl/flavor_retention_law_is_a2plus_note_2026-05-31.json:222`,
`docs/audit/data/ledger/yt/yt_qubit_democratic_top_coefficient_candidate_note_2026-05-25.json:429`.

So the `:170` gate is **actively load-bearing as a foreclosure instrument** in at
least 6 audited rows, while having no node, no exact target, no closure criterion,
and nothing that would ever tell the repo it had been closed. Ledger search for a
candidate owner:

```bash
# 11 rows mention source/action or physical-observable in id/title;
# 2 are open_gate, both unaudited, both gravity-lane-specific:
#   signed_gravity_source_action_escape_hatch_note      (lb 5.959, unaudited)
#   signed_gravity_aps_locked_source_action_proposal_note (lb 3.000, unaudited)
```

Neither is the framework-level identification gate the memo names.

---

## (c) The `no_go` population — count VERIFIED, cause is STRUCTURAL, not backlog

### C-1 Independent verification of the count

Method 1 — direct shard walk (3872 shards):

| | |
|---|---|
| `claim_type == "no_go"` | **439** |
| `effective_status == "unaudited"` | **438** |
| `effective_status == "audited_conditional"` | **1** (`gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_full_packet_no_go_theorem_note_2026-04-20`) |
| `effective_status == "retained_no_go"` | **0** |
| `retained` / `retained_bounded` among `no_go` | **0 / 0** |

Method 2 — the pipeline's own generated summary,
`docs/audit/data/effective_status_summary.json`:
`claim_type_counts.no_go = 439`; `effective_status_counts` contains
`retained: 109`, `retained_bounded: 332`, and **no `retained_no_go` key at all**.

Both methods agree. The brief's 438/437/1 is reproduced with **+1 row** (one
`no_go` row added since the brief was written). **Total retained-grade rows
repo-wide: 441, of which 0 are no-gos.** Every foreclosure in the repository is
ungraded — confirmed.

### C-2 The route EXISTS in code — so this is not a missing route

`docs/audit/scripts/compute_effective_status.py:39-43`:

```python
CLAIM_TYPE_TO_RETAINED = {
    "positive_theorem": "retained",
    "no_go": "retained_no_go",
    "bounded_theorem": "retained_bounded",
}
```

and `:47-49` ranks `retained_no_go` at 100, equal to `retained`. `clean_status()`
(`:105-128`) will hand a `no_go` row `retained_no_go` the moment it is
`audited_clean` with chain-closed deps. The bucket is fully wired.

### C-3 Auditors HAVE cleared no-gos — 196 times — so this is not auditor reluctance

Walking `previous_audits` for every `no_go` row: **196 of 439** rows carry
`audited_clean` somewhere in their audit history. Some carry it repeatedly, e.g.
`no_per_site_chirality_theorem_note_2026-05-02` has 9 archived `audited_clean`
verdicts; `gauge_wilson_isotropy_boundary_note_2026-05-04` has 9.
Historic clean verdicts by month: 2026-04: 36, 2026-05: 138, 2026-06: 130,
2026-07: 91. **Current count: 0.**

### C-4 CAUSE 1 — a two-day mass invalidation on 2026-07-11/12

Invalidation reasons in `previous_audits`, grouped by archive date, restricted to
`no_go` rows and to reasons beginning `no_go_discipline`:

| archive date | packet-gate invalidations |
|---|---|
| 2026-07-11 | **162** |
| 2026-07-12 | **40** |
| **total** | **202** |

All `no_go` archive events, by date, tail: `2026-07-10: 14`, **`2026-07-11: 181`**,
**`2026-07-12: 50`**, `2026-07-13: 1`, `2026-07-17: 1`. The population was wiped in
two days and has not recovered.

Most-recent invalidation reason per `no_go` row (220 rows have one):

| reason | count | share |
|---|---|---|
| `no_go_discipline_packet_missing` | 117 | |
| `no_go_discipline_packet_invalid` | 39 | |
| `cross_confirmation_first_audit_no_go_packet_invalid` | 7 | |
| `no_go_discipline_cross_confirmation_packet_invalid` | 1 | |
| **packet-gate subtotal** | **164** | **74.5%** |
| `dep_weakened` | 37 | |
| `criticality_increased` | 11 | |
| other | 8 | |

For comparison, `bounded_theorem` rows: packet-gate reasons are 498 of 1200
(41.5%), and 332 bounded rows are currently `audited_clean`. The asymmetry is the
signal.

The date corroborates: `docs/audit/scripts/no_go_discipline_gate.py:717-718`
refers to `"packets signed before the 2026-07-11 authority reset"`, and
`forensic_mode()`'s docstring (`:2823-2836`) dates the two-tier assurance regime
to **2026-07-12, owner-approved**.

### C-5 CAUSE 2 — the steady-state gate demands an artifact that 0 rows in the repo hold

`docs/audit/scripts/invalidate_stale_audits.py:300-304` makes forensic tier
**unconditional** for no-gos:

```python
_forensic = bool(
    source_required
    or (row.get("claim_type") or "") == "no_go"
    or no_go_discipline_gate.forensic_mode()
)
```

and `:316-322` makes an authenticated evidence snapshot mandatory for any
forensic `audited_clean` row:

```python
if audit_status == "audited_clean" and _forensic:
    if evidence_manifest is None:
        return "no_go_discipline_packet_invalid"
    if no_go_discipline_gate.evidence_snapshot_current_error(packet, current_manifest):
        return "no_go_discipline_packet_invalid"
```

while `:432-441` catches the no-packet case:

```python
if audit_status == "audited_clean":
    required = source_required or output_required or declared_requires
    if required and packet is None:
        return "no_go_discipline_packet_missing"
```

`source_requires_no_go_discipline` → `source_is_no_go_artifact`
(`no_go_discipline_gate.py:2838-2860`) returns `True` immediately when
`claim_type_hint == "no_go"`, so `source_required` is always True for these rows.

**Measured supply of the required artifact, repo-wide:**

| | count |
|---|---|
| rows carrying a live `no_go_discipline` packet | **3** |
| of those, `claim_type == "no_go"` | **0** (2 `positive_theorem`, 1 `bounded_theorem`) |
| of those, carrying an `evidence_snapshot` | **0** |
| rows declaring `negative_assertion_classes` | 150 |
| of those, currently `audited_clean` | **1** |

The snapshot is only ever built when the orchestrator supplies a trusted evidence
manifest (`scripts/codex_audit_runner.py:3263` sets
`CODEX_AUDIT_TRUSTED_EVIDENCE_MANIFEST`; `apply_audit.py:89, 193, 210` consumes
it). **No `no_go` row in the repository currently holds the artifact its own gate
requires**, so any clean no-go verdict is invalidated on the next pipeline run.

### C-6 CAUSE 3 — a DISPATCH RULE excludes every no-go from the only lane with throughput

`docs/audit/scripts/orchestrate_audit_batch.py:543-546`:

```python
claim_type = row.get("claim_type") or row.get("claim_type_author_hint")
if claim_type == "no_go":
    skipped.append(f"{cid}: no_go row - forensic tier, run individually")
    continue
```

and `:1418-1419`, after a worker returns:

```python
if blob.get("claim_type") == "no_go":
    return None, {**base, "result": "forensic_required_final_no_go"}
```

So (i) no `no_go` row is ever dispatched by the batch lane, and (ii) a batch
auditor who *types* a row `no_go` has that verdict **discarded**. `docs/audit/README.md:11-12`
states `"the auditor sets claim_type"` — but the lane that produces essentially
all throughput structurally cannot record an auditor's `no_go` typing.

The consequence is measurable in `claim_type_provenance`:

| claim_type | `provenance == "audited"` | share |
|---|---|---|
| `no_go` | **1 / 439** | **0.2%** |
| `bounded_theorem` | 459 / 2156 | 21.3% |
| `positive_theorem` | 148 / 670 | 22.1% |
| `open_gate` | 21 / 208 | 10.1% |

no-go typing is ~100× less auditor-owned than every other type.

### C-7 Throughput proof: 370 audits in 13 days, ZERO no-gos

Rows with `audit_date >= 2026-07-12`:

| claim_type | audits landed |
|---|---|
| `bounded_theorem` | 234 |
| `positive_theorem` | 101 |
| `decoration` | 20 |
| `open_gate` | 15 |
| **`no_go`** | **0** |
| total | **370** |

`docs/audit/data/audit_dispatch_queue.json` `live` section: **9 entries, 0 of them
`no_go`.**

An individual/forensic route does exist — `orchestrate_audit_loop.py:532-582
first_ready_forensic_claim` + `run_forensic_canary` (`:723`) — and its selector
`batch.source_requires_forensic` *does* accept `claim_type == "no_go"`. But it is a
**canary**: one row per loop, gated on `ready` status. Empirically it has cleared
**zero** no-gos in 13 days and 370 audits.

### C-8 Verdict on (c)

**Structural, not backlog.** Three independent mechanisms compose into a ratchet:

1. **Dispatch exclusion** (`orchestrate_audit_batch.py:543-546`) keeps no-gos out
   of the only high-throughput lane, and (`:1418-1419`) prevents batch auditors
   from typing rows `no_go` at all.
2. **Unconditional forensic tier** (`invalidate_stale_audits.py:300-304`) demands
   an authenticated evidence snapshot for every clean no-go, an artifact **0 rows
   in the repo hold**, so any clean verdict is reset on the next run.
3. **A one-shot reset** on 2026-07-11/12 destroyed 202 live clean no-go verdicts
   at once, moving the whole population to `unaudited`.

The strictness is deliberate and owner-approved (`forensic_mode()` docstring:
`"mandatory for no-go rows — where foreclosure is permanent"`). What is **not**
evidenced as deliberate is that no forensic run has cleared a single no-go in the
13 days since, while 370 other audits landed. The framework's foreclosures are
therefore all ungraded, and under the current wiring no ordinary audit round can
change that.

---

## (d) Lane gating data — 0 of 4 lanes certified; 20 permanently-unclearable blockers

`docs/audit/data/lane_certification.json` (schema `lane_certification_v2`),
config `docs/audit/data/lane_certification_config.json` (hand-edited, owner-approved
2026-07-12):

| lane | closure | blocking | certified |
|---|---|---|---|
| `charged_lepton_koide_value` | 40 | **24** | No |
| `acphilambda_retirement_basis` | 2 | **2** | No |
| `rule_universality_grain` | 19 | **18** | No |
| `theta_retirement` | 708 | **628** | No |

### D-1 Top blockers by lane (ranked by `load_bearing_score`)

`charged_lepton_koide_value` (24 blockers: 10 bounded, 8 positive, 4 open_gate, 2 no_go)

| lb | type | status | claim |
|---|---|---|---|
| 62.325 | bounded_theorem | unaudited | `three_generation_observable_theorem_note` |
| 26.699 | bounded_theorem | unaudited | `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` |
| 24.564 | no_go | unaudited | `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` |
| 23.938 | bounded_theorem | unaudited | `three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02` |
| 18.837 | positive_theorem | audited_conditional | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` |

`acphilambda_retirement_basis` (2 blockers, both roots, reason `root_not_retained_science`)

| lb | type | status | claim |
|---|---|---|---|
| 14.672 | open_gate | audited_renaming | `ac_orbit_occupancy_statistical_grain_derivation_obligation` |
| 13.741 | open_gate | audited_conditional | `ac_reta_hclass_hunit_readout_derivation_obligation` |

This lane is uncertifiable **by design** — its configured roots are the two AC
obligations, and the config states a configured open-gate root keeps its lane
uncertified until source-level science retires it. Note this is exactly the pair
whose registry closure conditions are defective per (a): **the lane cannot certify
until an obligation closes, and the machine record of what would close it is
wrong.**

`rule_universality_grain` (18 blockers: 8 bounded, 4 positive, 3 meta, 2 open_gate, 1 no_go)

| lb | type | status | claim |
|---|---|---|---|
| 44.850 | **meta** | **meta** | `key_terminology` |
| 25.295 | positive_theorem | audited_conditional | `cl3_complexification_split_narrow_theorem_note_2026-05-10` |
| 20.275 | bounded_theorem | unaudited | `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29` |
| 18.400 | positive_theorem | unaudited | `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` |
| 15.566 | no_go | unaudited | `record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06` |

`theta_retirement` (628 blockers: 314 bounded, 194 positive, 73 no_go, 25 open_gate, 17 meta, 5 decoration; 538 of them plain `unaudited`)

| lb | type | status | claim |
|---|---|---|---|
| 62.325 | bounded_theorem | unaudited | `three_generation_observable_theorem_note` |
| 61.632 | bounded_theorem | unaudited | `observable_principle_from_axiom_note` |
| 44.850 | **meta** | **meta** | `key_terminology` |
| 44.171 | **meta** | **meta** | `minimal_axioms_2026-05-03` |
| 40.027 | bounded_theorem | unaudited | `yt_ward_identity_derivation_theorem` |

### D-2 Cross-lane blockers (highest leverage)

23 rows block more than one lane. Top by lane count:

| lanes | type | status | lb | claim |
|---|---|---|---|---|
| 3 | open_gate | audited_renaming | 14.672 | `ac_orbit_occupancy_statistical_grain_derivation_obligation` |
| 3 | open_gate | audited_conditional | 13.741 | `ac_reta_hclass_hunit_readout_derivation_obligation` |
| 3 | positive_theorem | audited_conditional | 17.787 | `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10` |
| 3 | positive_theorem | unaudited | 15.714 | `per_site_su2_spin_half_theorem_note_2026-05-02` |
| 2 | bounded_theorem | unaudited | 62.325 | `three_generation_observable_theorem_note` |
| 2 | meta | meta | 44.850 | `key_terminology` |
| 2 | no_go | unaudited | 24.564 | `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` |

**`three_generation_observable_theorem_note`** (unaudited, lb 62.3, 1282
transitive descendants) is the single highest-value audit target across lanes.
The two AC obligations are the most-shared blockers (3 lanes each).

### D-3 DEFECT — two incompatible definitions of "chain-satisfying"

`docs/audit/scripts/compute_lane_certification.py:35-41`:

```python
def status_satisfies_certification(claim_id: str, status: object) -> bool:
    """Match the pipeline's chain boundary without inventing premise policy."""
    if status in RETAINED_GRADE: return True
    if isinstance(status, str) and status.startswith("decoration_under_"): return True
    return False
```

The docstring is **false**. `compute_effective_status.py:83-90`:

```python
def is_chain_satisfying_status(status: str | None) -> bool:
    return status == "meta" or is_retained_grade(status)
```

`meta` satisfies chain closure for retention but **not** for lane certification.
The config description does document the divergence ("Metadata does not"), so the
*policy* may be intentional — but the code comment asserting the two match is
wrong, and the consequence is not obviously intended:

**20 lane-blocking entries are `meta` rows** (3 in `rule_universality_grain`, 17 in
`theta_retirement`). A `meta` row's clean status is `"meta"` forever
(`compute_effective_status.py:109-110`), so **no audit and no science can ever
clear them.** `key_terminology` (lb 44.85) and `minimal_axioms_2026-05-03`
(lb 44.17) permanently block their lanes. Under the current rule those two lanes
cannot certify at any level of audit throughput.

Other gating surfaces checked: `docs/audit/data/doc_authority_registry.json`
(21 rows, class A/C/D/E/F/G; drives `premise_nodes.non_evidence_context_ids` via
`chain_satisfying: false`) — no internal inconsistency found.
`docs/audit/data/no_go_index_growth_targets.json` — `targets: []`, empty.
`docs/audit/data/load_bearing_summary.json` — 4506 nodes, thresholds consistent
with the ledger `criticality` values.

---

## (e) Prioritized repair plan with churn cost

### Churn model

Note hashes are source-content hashes, so editing a note requeues its row. Two
separate mechanisms matter:

1. **Row requeue** — editing `X.md` requeues the ledger row whose `note_path == X.md`.
2. **Premise-hash cascade** — `invalidate_stale_audits.py:558-573
   (axiom_premise_changed)` invalidates **every direct citer** of an
   `axiom_premise_nodes.json` node whose `note_hash` changed.

Measured exposure of the premise notes (direct citers with a premise-hash snapshot
→ would invalidate; retained-grade among them → verdicts at risk):

| premise note | direct citers | requeued on edit | **retained verdicts at risk** |
|---|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | 490 | **46** | **11** (7 `retained_bounded` + 4 `retained`) |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` | 32 | **2** | **0** |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | 50 | **2** | **0** |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | 30 | **2** | **1** (`retained_bounded`) |

Denominator: **441 retained-grade rows repo-wide.** An axiom-memo edit therefore
risks **2.5% of the entire retained library**; a primitive-note edit risks 0-0.2%.

### Batches, in priority order

---

**BATCH R1 — obligation reconciliation lint (TOOLING).** *Highest value.*

- Files: `docs/audit/scripts/audit_lint.py` (extend the block at `:707-721`),
  `docs/audit/scripts/tests/` (one test).
- Rule: for each id in `derivation_obligations.json`, open `current_path`; require
  (i) registry `target` == the note's `## Exact target` first paragraph after
  backtick/whitespace normalization; (ii) `self_liquidation_condition` non-empty
  **and** containing every conjunct of `## Closure criterion` (or, more robustly,
  add a `closure_criterion_sha256` field pinned to the note section and verify it);
  (iii) the obligation's ledger row has `claim_type == "open_gate"` (closes A-5);
  (iv) `historical_governance_source`, when present, is actually cited in the note.
- **Requeue cost: 0 rows. Verdicts at risk: 0.** Touches no claim note.
- Why worth it: catches the entire defect class permanently. All 6 mismatches in
  (a) plus the A-5 laundering hole are detected by this one rule, and any future
  obligation is born checked. Per campaign rule 4, this beats hand-fixing.
- Caveat: the lint will FAIL on landing until R2/R3 run. Land it as a warning
  first, or land R2 in the same reviewed change.

---

**BATCH R2 — registry text repair (CONTENT, but AUDIT-DATA SURFACE).**

- Files: `docs/audit/data/derivation_obligations.json` (6 field edits),
  `docs/audit/data/axiom_premise_nodes.json` (2 `note` edits per B-3/B-4).
- **Requeue cost: 0 rows.** Neither file is a claim note; no row hashes it.
  Verified: no ledger row has `note_path` pointing at `docs/audit/data/`.
- **BLOCKER — route, not cost.** Campaign hard rule 1 says PRs cannot land audit
  data and `docs/audit/data/` must be restored from `origin/main` before
  committing. `review-loop/SKILL.md:835-836` carves out "machine-readable
  audit/re-audit targeting metadata ... that do not assert a verdict", which a
  registry-text correction arguably is — but this is genuinely ambiguous and the
  repair sits inside the restore surface. **Escalate the route to the owner before
  attempting.** This is itself a finding: *registry defects cannot currently be
  repaired through the normal science-PR route.*
- If the route is refused, R1 alone still delivers the permanent detection, and
  R3 delivers a note-side fix that needs no audit-data edit.

---

**BATCH R3 — obligation notes carry their own closure conjuncts (CONTENT).**

- Files: `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`,
  `docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`,
  `docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`.
- Change: fold the `## Closure criterion` conjuncts (and, for A-2, `clock-rate`)
  into `## Exact target` so the note is self-contained, and add the theta note's
  missing governance-source citation. No status word, no verdict, no new
  vocabulary.
- **Requeue cost: exactly 3 rows** —
  `ac_orbit_occupancy_...` (`audited_renaming`),
  `ac_reta_hclass_...` (`audited_conditional`),
  `theta_quark_determinant_...` (`audited_conditional`).
- **Retained verdicts at risk: 0.** All three are terminal non-clean.
- **Downstream `dep_weakened` cascade: 0 direct dependents.** Verified against the
  rank map (`invalidate_stale_audits.py:155-168`): `audited_conditional`/`audited_renaming`
  rank 10 → `unaudited` rank 30 is a rank *increase*, so `dep_weakened`
  (`:535`) cannot fire; `claim_type` stays `open_gate`, so `dep_claim_type_changed`
  (`:547`) cannot fire either.
- Why worth it: 3 requeued terminal rows to make the three most-shared lane
  blockers (3 lanes each) say what actually closes them. Cheapest possible
  correction of a live governance error.

---

**BATCH R4 — axiom-memo gate registration lint (TOOLING).**

- Files: `docs/audit/scripts/audit_lint.py`, one new tracked allowlist under
  `docs/audit/data/` (e.g. bullets deliberately left unregistered, with a reason).
- Rule: parse the `## Open Gates Outside The Axioms` section of the registry's
  `minimal_axioms.current_path`; every bullet must resolve to a
  `derivation_obligations.json` entry or appear in the allowlist. Fail otherwise.
- **Requeue cost: 0 rows. Verdicts at risk: 0.**
- Why worth it: makes the `:170` class of defect impossible to reintroduce, and
  forces an explicit decision on the 5 unregistered bullets rather than silence.
  The allowlist file is audit data — same route question as R2; the lint rule
  itself is tooling and lands cleanly.

---

**BATCH R5 — reconcile the two chain-satisfaction definitions (TOOLING).**

- Files: `docs/audit/scripts/compute_lane_certification.py:35-41`.
- Either (i) correct the false docstring and state that certification is strictly
  stronger than retention, or (ii) if the owner intends parity, accept `meta` and
  unblock 20 entries. **Do not choose for the owner** — this changes what
  "certified" means.
- **Requeue cost: 0 rows** (regenerates `lane_certification.json` only, which is
  generated data and must be restored before commit).
- Why worth it: today two lanes carry permanently unclearable blockers and nobody
  reading the code would know, because the comment says the definitions match.

---

**BATCH R6 — no-go lane wiring (TOOLING + OWNER DECISION). Report only.**

- Files implicated: `docs/audit/scripts/orchestrate_audit_batch.py:543-546` and
  `:1418-1419`; `docs/audit/scripts/orchestrate_audit_loop.py:532-582`;
  `scripts/codex_audit_runner.py:3263`.
- The finding is (c). The repair is a **policy decision I must not make**: either
  (i) run the forensic canary against the no-go backlog until the first
  `retained_no_go` exists, proving the gate is passable end-to-end; or (ii) if it
  is not passable, the gate needs a reviewed change; or (iii) if 439 ungraded
  foreclosures are acceptable, that should be stated, because today the repo reads
  as if its no-gos were graded.
- **Requeue cost: 0 rows for the diagnosis.** Cost of (i) is audit capacity only.
- Suggested proof-of-passability target: one low-lb, self-contained no-go with a
  current runner — 433 of 439 no-go rows have a `runner_path`, so runner supply is
  not the constraint.

---

**BATCH R7 — scale-reference convention sentence (CONTENT, cheap). Owner-gated.**

- File: `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (one sentence reconciling `:17`
  `a^{-1} = M_Pl` with `:39-41` "does not assert `a/l_P = 1`" and with the open
  gate at `MINIMAL_AXIOMS_2026-06-29.md:172-173`).
- **Requeue cost: 2 rows, both `audited_conditional`. Retained verdicts at risk: 0.**
- Owner-gated because it touches what an approved primitive grants. Do not land
  without explicit approval — that is a foundation change, not hygiene.

---

**EXPLICITLY NOT RECOMMENDED — editing `docs/MINIMAL_AXIOMS_2026-06-29.md`.**
Cost: **46 rows requeued, 11 retained-grade verdicts at risk (2.5% of the retained
library).** Nothing found in (a)-(d) requires an axiom-memo edit: B-3 is a
registry-side divergence repairable in R2, and B-5 is repairable by registration
(R4) rather than by rewording the memo. If a future repair does need it, batch it
with every other memo change and get explicit approval per the churn guard
(`review-loop/SKILL.md:809-820`).

### Summary table

| batch | kind | files | rows requeued | retained at risk | route |
|---|---|---|---|---|---|
| R1 obligation lint | tooling | 2 | **0** | **0** | normal PR |
| R2 registry text | content | 2 | **0** | **0** | **audit-data — owner** |
| R3 obligation notes | content | 3 | **3** | **0** | normal PR |
| R4 gate-registration lint | tooling | 1 + data | **0** | **0** | PR + owner for data |
| R5 chain-def reconcile | tooling | 1 | **0** | **0** | normal PR, owner decides semantics |
| R6 no-go lane wiring | tooling/policy | 3 | **0** | **0** | **owner decision** |
| R7 scale convention | content | 1 | **2** | **0** | **owner-gated** |
| ~~axiom memo edit~~ | content | 1 | 46 | **11** | do not |

Total cost of the recommended set (R1+R3+R4+R5): **3 rows requeued, 0 retained
verdicts at risk**, and three permanent lint rules that make (a), A-5 and B-5
undetectable-only-once.

---

## Mandatory framework refresher — surfaces read

Read in full on `origin/main`, not from memory:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (194 lines, complete) — four axioms
  Lattice / Qubit / Admissibility / Record; Qualification `:74-84`; audit-pipeline
  treatment `:86-101`; dynamics relation `:103-118`; observable-principle parent
  `:120-134`; **Open Gates `:156-173`**.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (47 lines, complete) —
  six-step check; `:13-16` "do not grant more than the primitive source note
  declares"; `:17-19` unregistered proposals are unapproved; current primitive
  list `:21-46`.
- `docs/audit/README.md` (read `:1-80`) — auditor owns `claim_type` and
  `audit_status` (`:11-12`); claim_type enum `:67-73`; ledger shard layout;
  `ledger_io.save_ledger()` requirement.
- `docs/audit/data/axiom_premise_nodes.json` (53 lines, complete) — 4 nodes.
- Also read for this task: `docs/audit/data/derivation_obligations.json`,
  the three obligation notes, the three primitive notes,
  `docs/audit/scripts/{audit_lint,compute_effective_status,compute_lane_certification,invalidate_stale_audits,check_axiom_premise_clean,premise_nodes,orchestrate_audit_batch,orchestrate_audit_loop,apply_audit}.py`,
  `docs/audit/scripts/no_go_discipline_gate.py` (targeted sections),
  `docs/ai_methodology/skills/review-loop/SKILL.md:806-891` (**audit-hash churn
  guard `:809-820`**, note_hash policy `:882-891`).

**Compliance:** no commit, push, or PR; only this report file written; no audit
verdict set or predicted; no status value written into any note; no new axiom,
primitive, or vocabulary proposed. Every load-bearing statement above carries a
`file:line` or a reproducible command.

---

## Appendix — obligation comparison script

Saved at `$SCRATCH/oblig_check.py`; run as `python3 oblig_check.py <repo-root>`.

```python
import json, re, sys, pathlib, difflib
ROOT = pathlib.Path(sys.argv[1])
reg = json.loads((ROOT/"docs/audit/data/derivation_obligations.json").read_text())
norm = lambda s: re.sub(r"\s+", " ", s.replace("`", "")).strip()
def section(text, name):
    m = re.search(r"^##\s+"+re.escape(name)+r"\s*$(.*?)(?=^##\s|\Z)", text, re.M|re.S)
    return m.group(1).strip() if m else None
for cid, e in reg["nodes"].items():
    txt = (ROOT/e["current_path"]).read_text()
    tgt, clo = section(txt, "Exact target"), section(txt, "Closure criterion")
    rt = norm(e["target"]); nt = norm(tgt.split("\n\n")[0]) if tgt else ""
    print(cid, "| target match:", rt == nt)
    if rt != nt:
        sm = difflib.SequenceMatcher(None, rt, nt)
        print("   ratio %.3f" % sm.ratio())
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                print(f"   {tag:8s} REG[{rt[i1:i2]!r}] -> NOTE[{nt[j1:j2]!r}]")
    print("   slc :", norm(e.get("self_liquidation_condition", "")))
    print("   note:", norm(clo) if clo else "<<MISSING>>")
    hgs = e.get("historical_governance_source")
    if hgs:
        print("   governance src cited in note?", hgs.split("/")[-1] in txt)
```
