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
obstructions, "no route exists," "no retained primitive supplies this," or
"requires a new axiom." The restricted-input rule still applies: do not search
the wider repository. For N8, judge only the source note and one-hop authorities
provided here; missing cross-cycle evidence is a checklist failure, not
permission to browse. For N6, the approved premises are exactly the registered
four-axiom node (Lattice, Qubit, Admissibility, Record) plus any authority this
packet explicitly flags as an approved primitive. The currently registered
primitives grant only: scale reference as units conversion, structural kinetic
isotropy `c_t = c_s`, and pointwise evaluation at a supplied realized state.
They do not supply selectors, dynamics, probability, normalization, arbitrary
observable identifications, or empirical matches.

Record all eight checks in `no_go_discipline`. A gate `FAIL` is allowed with a
conservative non-clean verdict and must name its failure items. It can never
support `audited_clean`. A gate `PASS` requires at least five genuinely distinct
N1 routes, complete N2-N8 answers, and no failure items. Do not turn five
phrasings of one route into five routes.

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
      "route": "<distinct attack route>",
      "outcome": "<why it fails or remains open>",
      "honesty_marker": "<ATTEMPTED | RULED OUT BY PRIOR>",
      "authority": "<restricted-packet authority, or explicit packet gap>"
    }
  ],
  "N2_wall_independence": "<pairwise collapse result>",
  "N3_hidden_wall_scan": "<classified hidden-wall phrase hits>",
  "N4_residual_matching": "<witness/residual match result>",
  "N5_rhetoric_audit": "<resolutions actually tested>",
  "N6_partial_closure_scan": "<primitive/convention/reframe result>",
  "N7_steelman": "<strongest argument against the no-go>",
  "N8_cross_cycle_echo": "<restricted-packet prior-wall result or missing evidence>",
  "failures": ["<failing N-item; empty only for PASS>"]
}
```

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
