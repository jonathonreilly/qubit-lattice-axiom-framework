# Single-Clock B-AXIS — Owner / Audit-Lane Decision Packet (Block 04)

**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block04-20260620` (stacked on block03)
**Type:** meta — owner / audit-lane decision enumeration. NOT a derivation; authors
NO audit grade; sets NO publication status; edits NO audit-lane authority file.
**Status:** branch-local owner-packet record. This note PROPOSES actions for the
owner / independent audit lane to apply; it applies none of them. The independent
audit lane is the **sole status authority**.
`proposal_allowed=false`; `bare_retained_allowed=false`;
`audit_required_before_effective_retained=true`.

**Boundary flags:** B_AXIS_DERIVED = FALSE; B_AXIS_CONSUMED_AS_PREMISE = TRUE;
AUDIT_LEDGER_WRITTEN = FALSE; AUDIT_VERDICT_APPLIED = FALSE; NEW_AXIOM_ADDED = FALSE;
PREMISE_NODE_REGISTERED = FALSE (proposed only, see Decision 1).

---

## 0. What this packet is, and is not

The single-clock B-AXIS wall-consolidation campaign proved that the **B-AXIS
missing bridge** of the keystone
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
(audited_conditional, bounded_theorem, downstream fanout 959 / Class A) is
**WALLED under the no-new-axiom rule**: none of its three clauses —
**B-AXIS.1 = N2** (one supplied blocked time-step `2a_τ`), **B-AXIS.2 = N4**
(one declared evolution axis), **B-AXIS.3 = N5** (no second commuting clock) —
is derivable from `A_min` = Lattice + Quantum + Record on the retained
even-extent staggered-Dirac surface. The full obstruction, with all load-bearing
facts recomputed in-tree, is consolidated in
`docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`
(the **unified note**).

The physics-loop-addressable work is **DONE**. What actually unlocks the audit —
draining the 959-row descendant cone — is a set of **OWNER / AUDIT-LANE
decisions** outside physics-loop authority. This packet enumerates each as an
actionable item: **(a)** the decision, **(b)** recommendation + rationale,
**(c)** the EXACT artifact to apply, **(d)** who owns it.

**Scope discipline.** This packet does not touch `docs/audit/data/**`,
`docs/audit/AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`, `MISSING_DERIVATION_PROMPTS.md`,
or `docs/publication/**`. Every JSON/ledger artifact below is a **proposal for the
owner to apply**, quoted inside this packet so the owner can paste it; the packet
applies none of them.

---

## Decision 1 — REGISTER THE B-AXIS PREMISE NODE (governance decision, distinct from landing the no_go)

**(a) The decision.** Whether to register B-AXIS as a first-class
**declared-premise bundle** in the premise-node registry
`docs/audit/data/axiom_premise_nodes.json`, so that the 959 descendants
chain-satisfy on a single tracked premise edge rather than on per-doc prose
markers or on undeclared keystone authority.

**(b) Recommendation + rationale.** Recommendation is **conditional, not
automatic** — this is the one item the campaign deliberately does NOT
pre-decide for the owner. Registering a premise node is a **governance decision
with a strong consequence**: nodes in `axiom_premise_nodes.json` *chain-satisfy
WITHOUT bounding* downstream rows (per the registry `description`: "These
premises chain-satisfy without bounding downstream rows"). That is materially
different from merely landing the no_go (Decision 2): landing the no_go makes
descendants cite a `retained_no_go` authority and stay **audited_conditional**;
registering the premise node lets them chain-satisfy as if B-AXIS were an
**approved premise**.

The owner must weigh two genuinely different end-states:

- **Option 1A — register the premise node.** B-AXIS becomes an approved
  declared-premise bundle. Durable: replaces ~947 per-doc prose markers + the
  block03 firewall stopgap with one graph edge the audit lane adjudicates once;
  the residual is tracked at the node. Cost: it admits B-AXIS as a premise the
  framework *carries* (not derives), so any downstream "single clock / unique
  time axis" language inherits premise status, not theorem status, framework-wide.
- **Option 1B — do NOT register; keep rows audited_conditional citing the
  no_go.** More conservative: descendants remain explicitly conditional on the
  unified `no_go` and the still-open emergent-dynamics gate; nothing
  chain-satisfies. Cost: the firewall stays a per-doc decoration (block03's own
  §6 calls it a "stopgap"), and a future doc can silently revert to treating
  B-AXIS as derived unless re-firewalled.

**Campaign recommendation:** register the node (Option 1A) **only if** the owner
is comfortable with B-AXIS as an approved-premise bundle; otherwise keep the rows
audited_conditional (Option 1B). The campaign's honest read is that B-AXIS is a
*genuine* declared premise (Section 3 of the unified note exhibits explicit
realizable objects each clause excludes — it is load-bearing, not cosmetic), so
1A is defensible; but the chain-satisfy-without-bounding consequence is an owner
call, not a physics-loop call.

**(c) The EXACT artifact to apply.** A new entry in the `nodes` dict of
`docs/audit/data/axiom_premise_nodes.json` (and the new stable id appended to
`canonical_ids`). Matched to the registry's existing schema (schema_version 1;
each node has `current_path`, `aliased_paths[]`, `legacy_claim_ids[]`, `note`):

```json
"single_clock_baxis_premise": {
  "current_path": "docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md",
  "aliased_paths": [
    "docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md"
  ],
  "legacy_claim_ids": [],
  "note": "B-AXIS declared-premise bundle for the single-clock keystone (axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03, downstream fanout 959). B-AXIS = {B-AXIS.1 = N2 one supplied blocked time-step 2a_tau; B-AXIS.2 = N4 one declared evolution axis / RP-transfer construction; B-AXIS.3 = N5 no independent commuting transfer factor admitted as a second clock}. This is a DECLARED PREMISE bundle, NOT a derived result: the unified obstruction note shows B-AXIS is not derivable from A_min (Lattice+Quantum+Record) on the retained even-extent staggered-Dirac surface, and consolidates the obstruction (N2a exact-support FORCED; N2b/N4/N5 walled, all residuals relocated to the emergent-dynamics OPEN GATE of minimal_axioms). Registering this node lets the 959 descendants chain-satisfy on a tracked premise WITHOUT bounding them. The residual is NOT discharged: a downstream row needing an absolute clock unit (N2b), a derived axis label (N4), or exclusion of a second clock (N5) must still identify the named supplier shape (clock/rate bridge; per-axis Z2 BC-asymmetry / registration-direction bridge; T-hat^2 irreducibility / physical-clock-admission ray / gauge-redundancy theorem) — none supplied by A_min. Even-extent cubic-symmetric scope on the exact-zero W/S4 facts (odd-L falsifier resid 6.000); dimension-selection off-surface remains axiomatic. On re-date of the source note, update current_path and append the old path to aliased_paths."
}
```

And append `"single_clock_baxis_premise"` to the top-level `canonical_ids` array.

**CAVEAT (load-bearing).** Registering this node is **not** the same as landing
the no_go (Decision 2), and must not be conflated:

- *Landing the no_go* (Decision 2) makes the unified note a citable
  `retained_no_go` authority; descendants citing it stay **bounded /
  audited_conditional**.
- *Registering the premise node* (this decision) lets descendants
  **chain-satisfy without bounding** — a strictly stronger graph effect. Per the
  registry `description`, premise nodes "chain-satisfy without bounding
  downstream rows" (Tier-A bounding admissions live in `tier_a_admissions.json`,
  not here). The registry's PR3 structural guard also requires each listed doc
  to contain **only approved premise content (no framework-rule / ratification
  clauses)**; the owner / audit lane must confirm the unified note clears that
  guard before listing it (the note authors no audit grade and sets no status,
  which is consistent with the guard, but the guard is the audit lane's to run).

**(d) Who owns it.** **Owner (governance) + independent audit lane.** The
premise-bundle admission is an owner governance call; the audit lane runs the
PR3 structural guard and applies the JSON edit. Physics-loop proposes only.

---

## Decision 2 — LAND THE UNIFIED NO_GO to `retained_no_go` grade

**(a) The decision.** What grade the unified obstruction note
`docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md` lands at:
`retained_no_go` vs `audited_conditional` vs other.

**(b) Recommendation + rationale.** **Recommend `retained_no_go`.** Direct
precedent: `single_clock_kms_apbc_axis_supplier_no_go_note_2026-06-16` landed
`retained_no_go` (Class A, independence=cross_family, auditor codex-gpt-5.5) and
is itself cited by the unified note as a pruned-route authority. The unified note
is a `no_go` of the same kind (negative_route_pruning over B-AXIS N2b/N4/N5, plus
the N2a exact-support pin), passes its own per-clause N1–N8 No-Go Discipline Gate,
recomputes every load-bearing fact in-tree (consolidated runner PASS=32/0; four
absorbed block01 runners aggregate PASS=91/0), and survived a hostile adversarial
review (block02 disposition `passed_with_notes` — the reviewer "tried hard to
reject this note and could not").

**(c) The EXACT artifact to apply.** An **independent audit-lane pass** producing
a ledger row in `docs/audit/AUDIT_LEDGER.md` of the precedent form, e.g.:

```
| `single_clock_baxis_obstruction_unified_no_go_note_2026-06-20` | no_go | <prior> | **retained_no_go** | cross_family | <auditor-id> | A | - |
```

This is an audit-lane authoring action, NOT a physics-loop edit. It **requires an
independent audit-lane pass** because `proposal_allowed=false` and
`bare_retained_allowed=false`: the loop may not self-grade, and no bare `retained`
status may be asserted. The note carries `AUDIT_LEDGER_WRITTEN=FALSE` and is
correctly **not yet** in the ledger.

**(d) Who owns it.** **Independent audit lane (sole status authority).**
Physics-loop submits the note for grading; it does not grade.

---

## Decision 3 — SOURCE-NARROWING of the keystone's N5 "no second clock" assertion

**(a) The decision.** Whether to **narrow** the keystone source claim from a broad
"**no second clock**" assertion to "**exactly one supplied framework transfer is
admitted**" (the N5 dissolving framing).

**(b) Recommendation + rationale.** **Recommend the narrowing.** This is the
**only** way N5 stops being a live bridge **without a new theorem**. The unified
note (§6) shows the broad assertion is unprovable: the supplied two-step transfer
`T̂²` is *maximally factorized* into `L_s` commuting per-mode clocks, so no
commutant/center argument forces a single one-parameter orbit, and the factor
flows are Record-visible (not gauge). What `A_min` *does* support is a
**source-scope firewall**, not an exclusion theorem: of the candidate transfers,
the only one the framework **admits** as a physical clock is `{ (T̂², 2a_τ) }`
(the per-mode factors satisfy the admission checks (1)–(3) but FAIL check (4): no
source packet admits them as a second physical-clock transfer). Restating N5 as
"exactly one supplied framework transfer is admitted" makes the keystone's claim
**true as written** (an admission-scope statement) instead of an unprovable
exclusion statement.

This is a **source-wording decision, not a derivation** — it changes what the
keystone *claims*, narrowing it to what the admission inventory supports. It does
NOT close N5 as an exclusion theorem (none exists), and it does NOT supply the
physical-clock-admission ray (still open, `(L_s−1)`-param; see Opportunity row
6.(ii)/(iii)).

**(c) The EXACT artifact to apply.** A source-wording edit to the keystone note
`docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`,
replacing the N5 / B-AXIS.3 clause text with admission-scope wording, e.g.:

> B-AXIS.3 (N5): exactly one supplied framework transfer `(T̂², 2a_τ)` is
> **admitted** as the physical-clock transfer (a source-scope admission, not an
> exclusion theorem). No independent commuting transfer factor is admitted as a
> second clock; the per-mode factor flows of `T̂²` exist on the surface but are
> not admitted (they fail the physical-clock-admission inventory), per the
> unified note §6 and `axiom_premise_nodes` `single_clock_baxis_premise`.

Because this edits a keystone whose status is **audited_conditional**, the owner
must decide whether the re-wording is a content change requiring re-audit of the
keystone, or a clarifying narrowing within its existing conditional grade.

**(d) Who owns it.** **Owner (source-content decision) + audit lane (re-audit
disposition of the keystone).** Physics-loop may stage the wording; it does not
apply it to the keystone.

---

## Decision 4 — ADJUDICATE the two load-bearing co-cycle deps of the keystone's consolidation

**(a) The decision.** Adjudicate the two load-bearing co-cycle dependencies
flagged by the A3 Route2 meta artifact —
`axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` and
`staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` — before
the still-**unaudited / audited_conditional** keystone can be consolidated as a
wall.

**(b) Recommendation + rationale.** **Recommend audit-lane adjudication of both
before any wall status rests on the keystone.** The keystone is itself
audited_conditional; the A3 Route2 obstruction parent that consumes it is
unaudited (td~250). The two named deps are the load-bearing edges that the wall
ultimately co-cycles through: the microcausality / Lieb-Robinson theorem note
(the upstream `v_LR` / M2 authority) and the substep-4 AC narrowing note (the
closest staggered-Dirac sibling obstruction). The unified note's source
discipline (§11) deliberately takes **no load-bearing citation edge** to the
conditional parent keystone, the unaudited finite-speed cone note, or the
downstream ANOMALY_FORCES_TIME consumer — it recomputes instead. But a *wall
status* (as opposed to the recompute-only no_go) inherits any conditionality of
these two deps. Until the audit lane adjudicates them, **any wall resting on the
keystone is conditional** (unified note §10.4 conditional-parent caveat).

**(c) The EXACT artifact to apply.** Two audit-lane verdicts (independent passes)
on:
- `docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
- `docs/STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`

producing their ledger rows, recorded in `docs/audit/AUDIT_LEDGER.md`. No
physics-loop edit; this is a queue + grade action.

**(d) Who owns it.** **Independent audit lane** (queue ordering may be an owner
prioritization call).

---

## Decision 5 — APPROVE the consumer-firewall WIDTH

**(a) The decision.** Accept the campaign's consumer-firewall scope, or require
full per-descendant coverage of the 959-row cone.

**(b) Recommendation + rationale.** **Recommend accepting the scope.** The
firewall scope is, with full triage (block03 coverage note + triage record):

- **11 direct-claiming consumers repointed in block03** (purely additive
  B-AXIS-premise citations to the unified note; coverage runner PASS=34/0; all
  edits insertions-only, 0 deletions).
- **9 consumers covered by the in-flight firewall branch**
  `origin/physics-loop/single-clock-baxis-consumer-firewall-20260617` (commit
  `745cb10`, runner PASS=46/0) — NOT re-edited (conflict avoidance with the
  unmerged branch); flagged **repoint-to-unified-pending-integration**: at
  integration, repoint these 9 from the keystone citation to the unified note.
- **~936 transitive-covered** cone members (reach the keystone only through a
  direct consumer; inherit the premise by closure; need no direct edit).
- **5 non-claiming** direct dependents (meta surgical-fix / tracking records and
  bare dependency-pointer entries that make no load-bearing B-AXIS claim) — left
  untouched, documented.

This is the conservative-correct reading: every direct-claiming consumer is
covered (11 here + 9 at integration = 20), and transitive members inherit by
closure. **Decision: accept this scope** (20 direct-claiming covered + documented
triage of the rest) **vs require full per-descendant coverage** of all 959 rows.
Full per-descendant coverage is unnecessary work (transitive members carry no
fresh B-AXIS claim), and is **superseded** if Decision 1 (premise-node
registration) is taken — a single graph edge then replaces all per-doc markers.
The campaign recommends: **accept the scope; prefer Decision 1 as the durable
replacement for the decoration firewall.**

**(c) The EXACT artifact to apply.** An owner/audit-lane sign-off recorded
against the firewall coverage note
`docs/SINGLE_CLOCK_BAXIS_CONSUMER_FIREWALL_COVERAGE_NOTE_2026-06-20.md`, plus —
at integration of the in-flight firewall branch — the 9 repoint edits named in
that note §4. No new physics-loop edit is required to *accept*; the 9 repoints
are an integration action.

**(d) Who owns it.** **Owner (scope acceptance) + audit lane (records the
disposition); integration action at branch merge.**

---

## Decision 6 — REGISTER OPPORTUNITY ROWS for the named positive-supplier shapes

**(a) The decision.** Whether to register the named positive-supplier shapes as
governance **OPPORTUNITY rows** so future loops attack them directly without
re-deriving the obstruction.

**(b) Recommendation + rationale.** **Recommend registering all four.** Each is a
**named supplier shape** the unified note proved absent on the retained surface
but explicitly left open as a derivation/admission target (no new axiom). Without
opportunity rows, a future loop re-derives the same wall before reaching the live
edge. Each row: one-line target statement + the open gate it sits behind.

| # | clause | one-line target statement | open gate it sits behind |
|---|---|---|---|
| (i) | N4 | Derive a **per-axis Z₂ BC-asymmetry / registration-direction bridge** that selects one evolution axis non-transportably from a record-production layer (the only sub-S₄ selector is the supplied `(A,P,P,P)` datum, which is S₄-transportable + outside A_min). | record-production / emergent-dynamics |
| (ii) | N5 | Prove a **`T̂²` irreducibility / nonfactorization (gauge-redundancy of the factor clocks)** theorem showing the per-mode commuting factors carry no independent Record-order parameter (currently FALSIFIED on the surface: factors escape `span{I,Ĥ}`, produce distinct durable records). | emergent-dynamics |
| (iii) | N5 | Supply a **physical-clock-admission ray** — a chosen positive clock-ray in `span_{≥0}{n_p}` (carries `(L_s−1)` free params) admitting exactly one transfer as the framework clock. | record-production / emergent-dynamics |
| (iv) | N2b | Supply a **clock/rate bridge / absolute unit** carrying an actual `1/time` unit (no A_min observable returns a unit-bearing `1/time` number; `a_τ→c·a_τ` is an exact gauge). | emergent-dynamics (clock-rate) |

**(c) The EXACT artifact to apply.** Four OPPORTUNITY-row entries in the
governance opportunity registry (the audit-lane-owned queue; this packet does NOT
edit `AUDIT_QUEUE.md` or `MISSING_DERIVATION_PROMPTS.md`). The owner/audit lane
applies them in the appropriate registry, each carrying: clause, target
statement, open gate, and a back-citation to the unified note section
(N4 §5.5 / N5 §6 / N2b §4) and to `single_clock_baxis_premise` (if Decision 1 is
taken).

**(d) Who owns it.** **Owner (queue prioritization) + audit lane (registry
authoring).**

---

## Decision 7 — CONFIRM the even-cubic-symmetric scope boundary for the exact-zero claims

**(a) The decision.** Confirm that the **even cubic-symmetric** scope boundary is
acceptable for the exact-zero W / S₄ claims, and that **dimension-selection
off-surface remains axiomatic**.

**(b) Recommendation + rationale.** **Recommend confirming the boundary as
acceptable, as honestly scoped.** Every exact-zero W/S₄ transport fact and the
maximal `T̂²` factorization hold on the **even cubic-symmetric staggered-Dirac
reconstruction surface** ((R-RP2)/(R-SC2)/(R-CL3) object). The **odd-L falsifier**
is carried verbatim and recomputed live: at `L=(3,3,3,3)` the signed exchange does
NOT preserve the hop, `‖W M Wᵀ − M‖ = 6.000`; at even `L=(4,4,4,4)` the residual
is 0. The note is therefore a **no-go ABOUT the retained surface, NOT a
framework-wide impossibility proof**, and it carves out off-surface
dimension-selection (why `Z³` and one time) as remaining an **axiomatic input**.
This is the correct, honest scoping; mis-stating it as framework-wide would invite
an `audited_failed`. The non-exact escape claims (factors escape `span{I,Ĥ}`
≈ 0.65/1.3; distinct durable record min-dist ≈ 0.40) are stated as inequalities,
not exact zeros — also correct.

**(c) The EXACT artifact to apply.** An audit-lane confirmation recorded with the
Decision-2 grading: that the `retained_no_go` is scoped to even cubic-symmetric
staggered-Dirac blocks (exact-zero claims) and that dimension-selection
off-surface is acknowledged axiomatic. No source edit; this is a scope-acceptance
note in the grading record.

**(d) Who owns it.** **Independent audit lane** (folded into the Decision-2 pass).

---

## What draining the 959 requires — summary

The **physics-loop-addressable work is DONE**:

- the obstruction is honestly earned (block01: four genuine fresh attempts of the
  never-attempted positive routes — `T̂²` irreducibility, derived
  registration-direction bridge, joint two-rate-gate unit-pinning, full
  automorphism enrichment search — 91 PASS / 0 FAIL, NO CRACK; closes the
  premature-no-go objection at N1/N7);
- it is **consolidated** into one citable note (block02) that passes its own
  per-clause N1–N8 gate, recomputes every load-bearing fact in-tree, and survived
  hostile adversarial review (`passed_with_notes`);
- the **consumer firewall is widened** (block03): 11 repointed + 9 at integration
  + ~936 transitive-covered + 5 non-claiming, fully triaged.

What remains is **exactly these owner / audit-lane actions** (none performable by
physics-loop):

1. **Premise-node registration** (Decision 1) — governance call; register
   `single_clock_baxis_premise` (Option 1A, chain-satisfies without bounding) OR
   keep rows audited_conditional citing the no_go (Option 1B). The durable
   mitigation that replaces the decoration firewall.
2. **Land the unified no_go** to `retained_no_go` (Decision 2) — independent
   audit-lane pass; precedent = the KMS/APBC supplier no_go.
3. **Source-narrow N5** to "exactly one supplied framework transfer is admitted"
   (Decision 3) — the only way N5 stops being a live bridge without a new theorem.
4. **Adjudicate the two co-cycle deps** (Decision 4) — microcausality/Lieb-Robinson
   + staggered substep-4 AC — before any wall status rests on the keystone.
5. **Approve firewall width** (Decision 5) — accept the 20 direct-claiming +
   triaged scope; do the 9 repoints at integration.
6. **Register the four OPPORTUNITY rows** (Decision 6) — N4 BC/registration-direction;
   N5 irreducibility/gauge-redundancy; N5 physical-clock-admission ray;
   N2b clock/rate bridge.
7. **Confirm the even-cubic-symmetric scope boundary** (Decision 7) — fold into
   the Decision-2 grading.

Taken together, Decisions 1 + 2 drain the cone: the 959 descendants then either
chain-satisfy on the registered B-AXIS premise (1A) or stay honestly
audited_conditional on a landed `retained_no_go` (1B + 2). The remaining decisions
(3–7) harden the source wording, adjudicate the conditional ancestry, accept the
firewall scope, open the live-edge opportunity rows, and confirm scope.

---

## Status discipline

Branch-local owner-packet artifact for
`physics-loop/single-clock-baxis-wall-block04-20260620`. Adds NO framework axiom,
introduces NO primitive, sets / updates NO audit status, edits NO audit /
publication / effective-status surface. Every registry / ledger artifact above is
a **proposal for the owner / audit lane to apply**, quoted here for convenience;
this packet applies none of them. Branch-local status vocabulary only; no bare
"retained" / "promoted" in any status line (cited upstream statuses such as
`retained_no_go` and `audited_conditional` are quoted from their source records,
not reasserted here). `proposal_allowed=false`; `bare_retained_allowed=false`;
`audit_required_before_effective_retained=true`. The independent audit lane is the
sole status authority.
