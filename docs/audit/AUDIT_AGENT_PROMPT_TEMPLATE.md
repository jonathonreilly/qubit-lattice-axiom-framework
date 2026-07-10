# Audit Agent Prompt Template

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** binding template for fresh-look audits run by the current best
full Codex GPT model at maximum reasoning (or any independent auditor).

The wrapping pipeline (`docs/audit/scripts/`) constructs the actual prompt
by substituting variables marked `{{LIKE_THIS}}` below. The auditor sees
**only** the substituted prompt — no broader repo context, no publication
framing, no prior audit verdicts.

---

## Prompt body

You are an independent reviewer auditing a single claim from a physics
research repository. You have no prior context about the project. Do not
search the web. Do not read files outside the ones provided. Answer only
the questions in section 5.

### 1. The claim under audit

- `claim_id`: `{{CLAIM_ID}}`
- Source note path: `{{NOTE_PATH}}`
- Seeded `claim_type` hint, if any: `{{CLAIM_TYPE_HINT}}`
- Primary runner: `{{RUNNER_PATH}}`

The full text of the source note follows between the markers.

```
=== BEGIN SOURCE NOTE ===
{{NOTE_BODY}}
=== END SOURCE NOTE ===
```

### 2. Cited authorities (one hop upstream)

Each cited authority is provided in full below. You may use these as
inputs. You must not assume access to any other note.

```
{{FOREACH cited_authority IN CITED_AUTHORITIES}}
=== BEGIN CITED AUTHORITY: {{cited_authority.path}} ===
=== Cited authority effective_status: {{cited_authority.effective_status}} ===
=== Cited authority claim_type: {{cited_authority.claim_type}} ===
{{cited_authority.body}}
=== END CITED AUTHORITY: {{cited_authority.path}} ===
{{ENDFOREACH}}
```

### 3. Runner output (if available)

The evidence path for this exact rendered stdout block is
`{{RUNNER_STDOUT_EVIDENCE_PATH}}`.

```
{{RUNNER_STDOUT}}
```

If the runner output is absent only because the runner timed out, exceeded
the audit wall-time budget, or is known to require a long compute run, that
is not a scientific audit verdict. Do not convert mere noncompletion into
`audited_conditional` or `audited_failed`. If the load-bearing step cannot be
judged without the missing run, return exactly:

```
COMPUTE_REQUIRED: <one sentence naming the missing completed run, sliced runner, cached certificate, or independent derivation needed>
```

The wrapper must then leave the row pending or blocked for compute and must
not apply a terminal audit verdict for that reason alone. Completed runner
mismatches, stale numbers, import errors, or code that hard-codes the
contested premise remain valid audit evidence; the special rule is only for
wall-time noncompletion.

If you are asked to review a prior terminal verdict whose main rationale was
timeout, missing stdout, or compute-budget exhaustion, treat that prior result
as requiring policy repair or fresh re-audit. Do not inherit the old terminal
status as scientific evidence unless the current restricted packet also
contains an independent substantive blocker.

### 3a. Runner source code (if available)

The runner's source code is included so you can verify the runner actually
computes what its stdout claims. Stdout alone is not authoritative — a
trivial runner that prints `PASS=10 FAIL=0` without computing anything must
NOT pass as class `(C)` ("first-principles compute from the axiom"). The
load-bearing-step class judgment in section 5 must reflect what the code
does, not just what it prints.

When the source is present, look for:

- Hard-coded expected values (e.g., `assert result == 1.234567`) where the
  note's load-bearing step claims a derivation — this should be class `(G)`
  numerical-match or `(F)` renaming, not class `(C)`.
- Imports of the contested premise as input (e.g., reading a fitted value
  from another note and asserting equality) where the note claims first-
  principles compute — this is class `(B)` cross-note input verification at
  best.
- Runners that produce no actual computation and just print constants —
  these are class `(E)` definitions; the verdict is `audited_renaming`.
- Class `(D)` external comparator checks (PDG / lattice QCD constants
  embedded in the code) where the note claims framework-internal closure.

Conversely, runner source that genuinely instantiates the framework's
operators / lattice / Clifford algebra and computes a number not present
in any input is consistent with class `(C)`.

```python
{{RUNNER_SOURCE}}
```

### 3b. Helper runner sources and cache excerpts

Primary runners often `import` from helper modules in `scripts/*.py`.
Without their source, you cannot verify what the imported functions
actually compute, and the chain reduces to opaque calls — which forces
class `(C)` on packet-incompleteness grounds even when the chain is
sound. Some legacy rows also register load-bearing sibling runner
artifacts that are not imports of the primary runner. The audit ledger
row exposes a `helper_runner_paths` field listing the `scripts/X.py`
paths the audit packet builder is required to include alongside the
primary runner.

The full source and SHA-pinned cache excerpt for each helper script is
included below, one per section, in the same order as
`helper_runner_paths` in the ledger row.

```text
{{HELPER_RUNNER_SOURCES}}
```

When forming the load-bearing-step class judgment:

- Treat each helper as part of the chain. A helper that hard-codes a
  contested constant turns the parent into class `(G)` numerical-match
  or class `(B)` cross-note input verification.
- A helper that genuinely instantiates framework primitives and is
  called from the primary runner's load-bearing path is consistent
  with class `(C)` for the parent.
- A helper used only for plotting / logging / non-load-bearing
  bookkeeping does not change the class judgment.

If `helper_runner_paths` is non-empty but a named helper is missing
from this packet, that is a packet-completeness defect on the
orchestrator's side, not a chain failure on the parent's side. In
that case, return `audit_status=audited_conditional`, prefix
`notes_for_re_audit_if_any` with `runner_artifact_issue`, and name the
missing path in `verdict_rationale`.

### 3c. If primary runner source is unavailable

If the source is unavailable (`[runner missing on disk]` or similar),
fall back to judging the load-bearing step from the note text alone, and
include that limitation in `verdict_rationale`.

### 4. The audit rubric

#### 4a. No-Go Discipline gate

The orchestrator's source-shape check says this row requires the gate:
`{{NO_GO_DISCIPLINE_REQUIRED}}`.

Run the N1-N8 gate whenever that value is `true`, whenever you classify the
row as `no_go`, or whenever your rationale would name walls, admissions,
obstructions, "does not lift," "no route exists," "no retained primitive
supplies this," or "requires a new axiom." The restricted-input rule still
applies: do not search the wider repository. For N8, judge only the source note,
runner/helper sources, one-hop authorities, and premise registries supplied
here. Missing cross-cycle evidence is a checklist failure, not permission to
browse.

The complete current premise registries and their canonical source notes are
included below. Use their actual text and boundaries; do not infer a primitive
from a desired conclusion and do not use a superseded axiom summary.

```text
{{FRAMEWORK_PREMISE_CONTEXT}}
```

The accepted-premise types have different effects:

- `axiom_or_approved_primitive`: accepted, does not bound downstream status.
- `owner_governed_residual`: accepted only inside the registry boundary, is
  not an axiom or theorem derivation, and does not bound downstream status.
- `tier_a_derivation_target`: accepted only at the bounded tier and forces
  downstream `retained_bounded` until retired.
- `tier_a_convention_not_accepted`: survey metadata, not a chain-satisfying
  premise. Do not treat it as an admission.

Every N1-N8 evidence reference must use a path from this restricted manifest
and a locator that occurs verbatim in that file's supplied content (whitespace
normalization is allowed). A locator must contain at least 12 normalized
characters. The manifest is an allow-list, not evidence by itself:

```json
{{NO_GO_EVIDENCE_MANIFEST}}
```

For N6, the orchestrator has supplied a partial-closure index built from all
registered premise classes, the controlled vocabulary, every ledger-indexed
meta note, the active review queue, and repository-visible physics-loop
handoff/status surfaces. Its metadata declares every scanned path and the
similarity thresholds and candidate limits. You must disposition every listed
`candidate_id`; a free-text `none_found_reason` is not a substitute for this
index.

```json
{{NO_GO_PARTIAL_CLOSURE_INDEX}}
```

For N8, the orchestrator has also supplied a cross-cycle search index. It is
constructed from this row's audit history, one-hop authority audit history,
Tier-A retirements, owner-governed retirements, similar `no_go` rows in the
audit ledger, and every tracked
`.claude/science/physics-loops/**/NO_GO_LEDGER.md` file. The index metadata
states the exact glob, scanned file count and paths, similarity threshold, and
candidate limit. You must disposition every listed `candidate_id`;
`packet_complete` is valid only when the N8 evidence path names this index.

```json
{{NO_GO_CROSS_CYCLE_INDEX}}
```

Record all eight checks in `no_go_discipline`. A gate `FAIL` is allowed with a
conservative non-clean verdict, `chain_closes=false`, an explicitly narrowed
`claim_scope`, a corrected wall set, and the next untested route. It can never
support `audited_clean`. A gate `PASS` requires at least five genuinely distinct
N1 mechanism classes, every route closed, complete structured N2-N8 records,
no unresolved items, a resolved steelman, a complete cross-cycle scan, and no
failure items. Do not turn five phrasings of one route into five routes. A
`RULED OUT BY PRIOR` route must cite either a retained-grade one-hop authority
or the registered text of an accepted axiom/primitive or owner-governed premise.
Tier-A conventions and unretained ordinary dependencies cannot rule out a route.

Definitions you must use:

- **Load-bearing step.** The single sentence or equation in the source
  note that does the actual work — the step that, if removed, would break
  the chain from cited inputs to the conclusion.
- **Derivation class.** Pick exactly one:
  - `(A)` algebraic identity check on existing inputs
  - `(B)` cross-note input verification (reads value from another note)
  - `(C)` first-principles compute from the framework baseline (one-qubit
    operator algebra on the `Z^3` spatial substrate plus accepted
    normalizations) producing a number not present in any input. A cited
    authority flagged `axiom_premise: true` is the accepted axiom premise for
    this class — deriving from it is class (C), not a downgrade.
  - `(D)` external comparator check against PDG / lattice QCD / observation
  - `(E)` definition (introduces a new symbol)
  - `(F)` renaming (asserts symbol identity between two existing concepts;
    e.g., "define A² := dim(SU(2))/dim(SU(3))" while the empirical CKM A
    is defined as |V_cb|/λ²)
  - `(G)` numerical match at a tuned input scale
- **Verdicts:**
  - `audited_clean` — the load-bearing step is in class (C) or is a
    genuine algebraic closure of class (A) over independent retained-grade
    inputs. Conclusion follows from cited inputs without appeal to anything
    else.
  - `audited_renaming` — the load-bearing step is in class (E) or (F).
    The chain reduces to a definition substitution rather than a
    derivation.
  - `audited_conditional` — at least one cited authority is not retained-grade
    (`retained`, `retained_no_go`, `retained_bounded`, or
    `decoration_under_<retained_parent>` — the decoration form is only
    assigned by the pipeline when the parent is itself retained-grade, so
    it inherits retention) or contains explicit language that the
    identification is open work; or the claim imports an explicit premise,
    bridge, carrier, readout, normalization, boundary condition, or
    asymptotic authority that is not closed by the restricted packet.
    Retained status does not propagate through an open identification.
    **Accepted-premise carve-out.** A cited authority flagged
    `axiom_premise: true` or `accepted_premise: true` does **not** count
    toward the "not-retained-grade authority" downgrade. Axiom and explicitly
    approved primitive premises are accepted framework premises (you do not
    audit the premise itself), so a class (C) derivation whose only
    non-retained-grade upstream is the axiom/primitive premise, and whose
    load-bearing step genuinely closes from that premise content plus
    retained-grade inputs, is eligible for `audited_clean`.
    Owner-governed residual premises are also accepted premises inside their
    recorded registry boundaries. They are not axioms, primitives, or theorem
    derivations, but they do not impose Tier-A boundedness once adopted.
    Tier-A admitted derivation targets are different: they are accepted
    non-axiom premises only at the bounded tier. A clean row depending on a
    Tier-A admitted derivation target may become `retained_bounded` after the
    pipeline computes effective status, but it is not eligible for full
    unbounded `retained` until that admission is retired by a retained
    derivation or explicit owner-governance adoption.
    **This is not a free pass.** The carve-out removes only the automatic
    downgrade; the load-bearing step must still correctly use the axiom
    content. If the step merely re-reads the axiom's wording or asserts a
    symbol identity, it is class (E)/(F) → `audited_renaming`. If it
    misuses, overreaches, or misattributes the axiom content, the chain
    does not close → `audited_conditional` / `audited_failed`. Citing the
    accepted premise must be a *correct* citation, judged on its own terms.
    The carve-out applies only to authorities the packet explicitly flags
    `axiom_premise: true` or `accepted_premise: true`; every other
    not-retained-grade authority still downgrades as above.
  - `audited_decoration` — every load-bearing step is class (A), the
    note has zero (D) checks, and the chain reduces to a single upstream
    parent claim plus standard mathematics. (See
    `ALGEBRAIC_DECORATION_POLICY.md`'s definition.)
  - `audited_numerical_match` — class (G) load-bearing step. The chain
    works only at a chosen input scale or chosen input value, with the
    input itself imported from a calibrated external source.
  - `audited_failed` — chain does not close even on its own terms.

### 5. Required answers

Return a single JSON object with exactly these fields. No other prose.

```json
{
  "claim_id": "{{CLAIM_ID}}",
  "load_bearing_step": "<one-sentence quote or paraphrase from the note>",
  "load_bearing_step_class": "<one of A, B, C, D, E, F, G>",
  "claim_type": "<one of positive_theorem, bounded_theorem, no_go, open_gate, decoration, meta>",
  "claim_scope": "<short citeable statement of what was actually audited>",
  "chain_closes": <true | false>,
  "chain_closure_explanation": "<one or two sentences. If false, name the missing step.>",
  "runner_check_breakdown": {
    "A": <int>, "B": <int>, "C": <int>, "D": <int>, "total_pass": <int>
  },
  "verdict": "<one of audited_clean, audited_renaming, audited_conditional, audited_decoration, audited_numerical_match, audited_failed>",
  "verdict_rationale": "<two to four sentences>",
  "decoration_parent_claim_id": "<claim_id of the upstream parent if verdict = audited_decoration, else null>",
  "open_dependency_paths": ["<note path of any cited authority that is itself support / open / conditional>"],
  "auditor_confidence": "<low | medium | high>",
  "notes_for_re_audit_if_any": "<for audited_conditional and audited_renaming, prefix exactly one repair class from missing_dependency_edge, dependency_not_retained, missing_bridge_theorem, scope_too_broad, runner_artifact_issue, compute_required, other, then name the cheapest next repair action; if that action is dependent-side (for example narrowing downstream citing sentences), it must also name adding a dated downstream-hygiene line to this note's own boundary, because only this note's own hash drift (or a dispatcher sidecar) re-enters the row into the audit queue; otherwise short note flagging anything a second auditor should re-check, or empty>",
  "no_go_discipline": null
}
```

Use `null` only when the gate is not required. Otherwise replace it with:

```json
{
  "required": true,
  "status": "<PASS | FAIL>",
  "N1_alternative_routes": [
    {
      "route_id": "<stable short id unique inside this packet>",
      "route_class": "<one of algebraic_rearrangement, symmetry_or_representation, alternate_carrier_or_sector, boundary_or_initial_condition, normalization_or_units, dynamical_or_effective_action, lattice_scale_or_limit, numerical_or_finite_case, convention_or_relabeling, alternate_observable_or_readout, topology_or_global_structure, dependency_or_registry_reclassification>",
      "mechanism": "<physical or mathematical mechanism, distinct from every other route>",
      "attempt": "<what calculation or restricted-packet test was actually performed>",
      "outcome": "<why the attempt closes the route or why it remains open>",
      "honesty_marker": "<ATTEMPTED | RULED OUT BY PRIOR>",
      "disposition": "<CLOSED | OPEN | UNTESTED>",
      "prior_witness_id": "<required only for RULED OUT BY PRIOR: matching N4 witness_id>",
      "evidence_path": "<path from NO_GO_EVIDENCE_MANIFEST>",
      "evidence_locator": "<12+ character quote/locator actually present at evidence_path>"
    }
  ],
  "N2_wall_independence": {
    "walls": ["<every wall claimed by the scoped negative result>"],
    "pairwise_checks": [
      {
        "left": "<wall from walls>",
        "right": "<different wall from walls>",
        "left_closes_right": false,
        "right_closes_left": false,
        "independent": true
      }
    ],
    "collapsed_wall_set": ["<minimal wall set after pairwise collapse>"],
    "unresolved": [],
    "evidence_path": "<manifest path>",
    "evidence_locator": "<actual locator>"
  },
  "N3_hidden_wall_scan": {
    "scan_scope": "<phrases and restricted packet surfaces checked>",
    "hits": [
      {
        "phrase": "<scanned phrase>",
        "classification": "<retained_authority | hidden_admission | non_load_bearing>",
        "promoted_wall": "<matching N2 wall when hidden_admission, otherwise omit>",
        "evidence_path": "<manifest path>",
        "evidence_locator": "<actual locator>"
      }
    ],
    "none_found_reason": "<required when hits is empty>",
    "unresolved": [],
    "evidence_path": "<manifest path covering the scan>",
    "evidence_locator": "<actual locator>"
  },
  "N4_residual_matching": {
    "scan_scope": "<witness and residual surfaces checked>",
    "witnesses": [
      {
        "witness_id": "<unique id referenced by a prior-ruled N1 route>",
        "route_id": "<matching N1 route_id>",
        "witness_residual": "<residual in cited witness>",
        "claim_residual": "<residual asserted here>",
        "match": true,
        "evidence_path": "<manifest path>",
        "evidence_locator": "<actual locator>"
      }
    ],
    "none_found_reason": "<required when witnesses is empty; forbidden as a substitute for prior-route evidence>",
    "unresolved": [],
    "evidence_path": "<manifest path covering the scan>",
    "evidence_locator": "<actual locator>"
  },
  "N5_rhetoric_audit": {
    "scan_scope": "<negative-resolution language checked>",
    "statements": [
      {
        "phrase": "<negative or resolution phrase>",
        "tested_resolutions": ["<resolution actually tested>"],
        "untested_resolutions": [],
        "evidence_path": "<manifest path>",
        "evidence_locator": "<actual locator>"
      }
    ],
    "none_found_reason": "<required when statements is empty>",
    "unresolved": [],
    "evidence_path": "<manifest path covering the scan>",
    "evidence_locator": "<actual locator>"
  },
  "N6_partial_closure_scan": {
    "scan_scope": "<primitive, owner-governed, Tier-A, convention, definition, and scope surfaces checked>",
    "premise_classes_checked": [
      "axiom_or_approved_primitive",
      "owner_governed_residual",
      "tier_a_derivation_target",
      "tier_a_convention_not_accepted",
      "definition_or_scope_reframe"
    ],
    "candidates": [
      {
        "candidate_id": "<candidate_id from the orchestrator partial-closure index>",
        "kind": "<approved_primitive | owner_governed | tier_a | convention_reframe | definition_refactor>",
        "could_close_wall": false,
        "addressed": true,
        "disposition": "<why the candidate does or does not close the scoped wall>",
        "evidence_path": "<manifest path>",
        "evidence_locator": "<actual locator>"
      }
    ],
    "none_found_reason": "<required when candidates is empty>",
    "unresolved": [],
    "evidence_path": "<manifest path covering the scan>",
    "evidence_locator": "<actual locator>"
  },
  "N7_steelman": {
    "route_id": "<the evidenced N1 route that instantiates the strongest steelman>",
    "argument": "<strongest argument against the no-go>",
    "resolution": "<why it succeeds or fails in the scoped packet>",
    "resolved": true,
    "evidence_path": "<manifest path>",
    "evidence_locator": "<actual locator>"
  },
  "N8_cross_cycle_echo": {
    "packet_complete": true,
    "echoes": [
      {
        "candidate_id": "<candidate_id from the orchestrator cross-cycle index>",
        "mechanism": "<earlier wall/admission mechanism>",
        "retired": false,
        "applicable": true,
        "addressed": true,
        "evidence_path": "<manifest path>",
        "evidence_locator": "<actual locator>"
      }
    ],
    "none_found_reason": "<required only when the orchestrator index contains zero candidates>",
    "unresolved": [],
    "evidence_path": "<manifest path covering the restricted search>",
    "evidence_locator": "<actual locator>"
  },
  "failures": ["<failing N-item; empty only for PASS>"],
  "demotion": "<for FAIL only: partial-attempt-with-named-untested-routes | partial-narrowing | bounded-with-corrected-wall-count | stretch-attempt-with-honest-residual>",
  "prior_claim_scope": "<for FAIL only: exact pre-audit ledger scope supplied by the orchestrator>",
  "narrowed_claim_scope": "<for FAIL only: exact same text as top-level claim_scope>",
  "corrected_wall_set": ["<for FAIL only: honest walls still supported>"],
  "next_route": {
    "route_id": "<for FAIL only: OPEN or UNTESTED N1 route_id>",
    "reason_untested": "<why this route remains the next concrete target>"
  }
}
```

For `PASS`, omit the five FAIL-only fields. For `FAIL`, all five are required.
The orchestrator adds `evidence_snapshot` after validating the exact rendered
packet; do not emit or fabricate that field. An `audited_clean` PASS must carry
`chain_closes=true`.
Any `OPEN`/`UNTESTED` route, unresolved N2-N6/N8 item, mismatched witness,
untested rhetoric resolution, unaddressed partial-closure candidate, unresolved
steelman, incomplete N8 packet, or applicable unaddressed echo forces `FAIL`.

### 6. What you are not asked to do

- Do not propose alternative positive derivations. The audit checks whether
  the presented derivation closes from cited inputs. The only exception is the
  mandatory N1/N7 stress test for a negative claim: enumerate attack routes
  and steelman them, but do not promote an unpresented route into a theorem.
- Do not recompute the underlying physics from scratch.
- Do not consult external sources (PDG, lattice QCD literature, the
  arXiv) beyond what is quoted in the source note.
- Do not adjust the verdict based on external reputation of the
  framework or of the author.
- Do not soften the verdict because the topic is ambitious. If a
  renaming is presented as a derivation, the verdict is
  `audited_renaming` regardless of how interesting the renaming is.

### 7. Tie-breaking

If you are torn between two verdicts:

- `audited_clean` vs `audited_renaming` → choose `audited_renaming`. The
  burden is on the derivation to be unambiguously class (C) or genuine
  (A) over independent inputs.
- `audited_clean` vs `audited_conditional` → choose `audited_conditional`
  if any cited authority is `support` or `open` for any reason.
- `audited_clean` vs `audited_decoration` → choose `audited_decoration` if
  there are zero (D) checks and the chain reduces to one parent claim.
- `audited_clean` vs `audited_numerical_match` → choose
  `audited_numerical_match` if the result depends on a specific input
  value (e.g., `α_s(v) = 0.1033`) imported from a separate calibrated
  measurement.

The audit lane prefers conservative verdicts. Borderline cases that turn
out to be clean can be ratified by a second audit with explicit
rationale; borderline cases that turn out to be renamings cannot easily be
caught downstream.

---

## Pipeline notes (not shown to the auditor)

- The wrapping script substitutes the variables, sends the prompt to the
  current best full Codex GPT model in a fresh session, captures the JSON
  response, and validates it against the schema.
- If JSON parsing fails or required fields are missing, the response is
  logged as `audit_status = audit_in_progress` with `blocker:
  malformed_audit_response` and the audit is re-queued.
- For `criticality: critical` claims (by transitive-descendant count;
  the audit lane intentionally does not use author-declared flagship
  status), the pipeline runs the prompt twice in independent sessions
  and requires matching `verdict`, `claim_type`, and
  `load_bearing_step_class` before landing `audited_clean`. A same-family
  second audit is eligible only when recorded as `independence:
  fresh_context` from a distinct restricted-input session. Mismatches
  promote to a judicial third-auditor review. The judicial auditor receives
  the restricted source packet and the two prior audit arguments, then
  records whether the first audit, second audit, or neither should be
  ratified.
- The auditor's session metadata (model version, session ID, timestamp)
  is recorded in the audit row's `auditor` field; the exact
  `auditor_family`, for example `codex-gpt-5.6`, is set automatically when
  this template is used.
