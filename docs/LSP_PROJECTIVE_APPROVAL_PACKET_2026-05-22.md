# LSP-Projective Framework Rule — Approval Packet (User Sign-Off Required)

**Date:** 2026-05-22
**Type:** meta (decision packet — NOT a ratification)
**Status:** awaiting explicit user approval, per the
`2026-05-22-lsp-prr-framework-rule-approval-gate` entry in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`. The reviewer's gate requires user
sign-off before any new framework rule can land.

## What this packet is

This packet asks the user to **explicitly approve, defer, or reject** **one** candidate framework rule: **LSP-projective** (Lüders Sequential-Product instrument selection, sharp-projection scope only).

Five-physicist Nature-grade panel review verdict: **5/5 yes** on LSP-projective.

This packet supersedes the closed PR #1659 (which bundled four rules; the bundled approach didn't fit the reviewer's gate). PRR and PWC are separate decisions for later, NOT in this packet.

## What this packet is NOT

- Not a ratification — no framework rule is added by this PR
- Not a re-audit — no row's status changes
- Not a runner-bearing claim
- Not a self-promotion of any rule

## Layman's explanation

When the framework measures a sharp property `P` — e.g., "is the qubit in the |0⟩ state?" — and gets the answer "yes," what happens to the state afterward?

LSP-projective commits to the **minimum-disturbance** reading: the state is just **filtered** down to the part consistent with the "yes" answer. No extra rotation, no extra phase, no extra basis change.

The alternative would be: every projective measurement comes with a hidden built-in rotation `U` that's part of the measurement act. The framework would then have to specify a specific `U_P` for every projection `P` — a massive axiom expansion. LSP-projective says: don't do that. The measurement is just the filter.

Real-experiment apparatus disturbances are modeled separately (as Hamiltonian evolution between measurements), not folded into the measurement act itself.

**Scope is explicit: projective measurements only.** Non-projective POVMs (weak measurements, ancilla-coupled measurements, smeared lattice observables) are explicitly left open for a separate framework rule. This narrowing is what made the panel approve.

## Narrow technical claim

For projective measurement of an orthogonal projection `P ∈ A_Λ` on a finite qubit-lattice region, the framework's measurement instrument is the Lüders Kraus operator:

```text
K_P := P
```

Sequential composition of "outcome P then effect E" is then:

```text
M_{P, E} := K_P† E K_P = P E P
```

## Substantive physical commitment

For **sharp projective measurements only**: the measurement is minimum-disturbance. The framework does **not** commit to a universal measurement-instrument selection — non-projective POVM instrument selection is deferred to a future framework rule.

## Why this is a framework rule, not a theorem

The literature explicitly shows the sequential product on the effect algebra `E(H)` is **not unique** — there are mathematically valid alternative sequential products that don't reduce to `P E P` (arXiv:0905.0596 Gudder counterexample; arXiv:math/0211033 broader landscape). A prior PR (#1626) tried to derive uniqueness from Greechie/Gudder axioms alone and was rejected for overclaim. The framework needs to commit to LSP-projective as a *selection*, not a *derivation*, because no theorem on A1+A2 alone forces the selection.

The conditional bridge already landed in PR #1651 with a 39/0 runner exhibiting:
- The conditional algebra (if K_P = P, then M_{P,E} = P E P) symbolically on 5 instrument families
- A worked **counterexample**: K_P^twist := H · P (Hadamard-twisted) also satisfies K_P† K_P = P but gives a DIFFERENT composition, confirming the load-bearing role of the selection

## Panel review findings (5/5 yes when narrowed to projective-only)

Five senior theoretical physicists with distinct specialties (foundations, stat-mech, lattice QFT, quantum information, math physics) independently reviewed LSP at Nature-grade rigor.

| Reviewer | Verdict on LSP-projective | Caveat |
|---|---|---|
| Foundations | Yes | Resolve ontic-vs-epistemic ambiguity in post-measurement state language elsewhere in the framework |
| Stat-mech | Yes | State the non-projective POVM extension as a separate open gate |
| Lattice QFT | Yes | Note this is about idealized Lüders updates, not transfer-matrix expectation values |
| Quantum Info | Yes | Specifically rejected when LSP was framed as UNIVERSAL — accepts when narrowed to projective-only |
| Math-physics | Yes | On tracial reference, LSP coincides with Connes-Størmer modular conditional expectation; for non-tracial states (finite-β KMS), they diverge — flag this scope |

**Caveats are documentation/disclosure items, not rejection grounds.** The narrow LSP-projective claim itself is panel-supported.

The QI reviewer's caveat is particularly important and shaped the scope narrowing: the framework's existing Stinespring V construction (PR #1650, landed) takes **arbitrary Kraus families {K_r}** as input, including non-projective POVMs. LSP-projective leaves that arbitrary-Kraus posture intact — the framework selects Lüders only for the special projective case, not for universal measurement-instrument selection.

## What it unlocks if approved

| Row | Current | Under LSP-projective |
|---|---|---|
| `luders_rule_from_composition_consistency_note_2026-05-20` | `audited_conditional` — `missing_bridge_theorem` on `M_{P,E} = P E P` | Step-1 sequential composition for projective P becomes the load-bearing consequence of LSP-projective |
| `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` (PR #1651, landed) | unaudited conditional | Conditional becomes unconditional for projective P |
| `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20` | unaudited | One blocker removed (Born chain still needs other pieces) |

## What it does NOT commit the framework to

- Doesn't constrain dynamics (free evolution between measurements)
- Doesn't pick a specific Hamiltonian or measurement schedule
- Doesn't apply to POVMs that aren't projective; those have their own instrument-selection question, deferred to a future rule
- Doesn't promote any audited_conditional row by itself — auditor still owns each verdict

## What this PR does NOT ship

- No actual ratification — that's the follow-up after sign-off
- No audit-dispatch sidecar — same
- No new companion runner (the conditional bridge runner already exists in PR #1651)
- No changes to MINIMAL_AXIOMS_2026-05-20 or QUBIT_AXIOM_HARDENING_NOTE
- No audit ledger row promotions

## Sign-off

- [ ] **Approve LSP-projective** — proceed to ratification PR + dispatch + companion runner (with explicit "projective-only" scope and non-projective POVM rule deferred)
- [ ] **Defer LSP-projective** — keep PR #1651 as conditional support; don't ratify
- [ ] **Reject LSP-projective** — don't add to framework

## After user approval

Follow-up ratification PR pattern (R1 template):

1. Add LSP-projective clause to `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` (new section) with explicit "projective-only" scope and panel caveats recorded
2. Add cross-link from `MINIMAL_AXIOMS_2026-05-20.md` commentary block
3. Re-link PR #1651's conditional bridge runner as the LSP-projective runner
4. Write an LSP-projective dispatch manifest listing the eligible re-audit rows (Lüders parent + downstream)
5. (When reviewer's audit-dispatch infrastructure lands) add a machine-readable dispatch sidecar

PRR and PWC are separate decisions, not coupled to this one. They can be packaged later as their own approval packets if/when the framework decides to pursue them.

## Citation-graph note

This is a meta decision-packet doc; all references are plain-text only. No load-bearing dep edges.

Plain-text pointer references:

- `docs/repo/ACTIVE_REVIEW_QUEUE.md` — `2026-05-22-lsp-prr-framework-rule-approval-gate` entry
- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § Hardening II — R1 ratification template (already landed)
- `LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1651, landed) — conditional LSP-projective bridge with 39/0 runner and worked counterexample
- `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` — Lüders rule parent (audited_conditional; would unblock under LSP-projective)
- `PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1650, landed) — Stinespring V construction takes arbitrary {K_r}; consistent with LSP-projective narrow scope (non-projective POVMs explicitly deferred)
