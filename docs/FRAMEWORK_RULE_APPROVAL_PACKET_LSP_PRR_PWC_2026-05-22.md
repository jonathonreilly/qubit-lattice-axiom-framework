# Framework-Rule Approval Packet: LSP, PRR, PWC (User Sign-Off Required)

**Date:** 2026-05-22
**Type:** meta (decision packet — NOT a ratification)
**Status:** awaiting explicit user approval, per the
`2026-05-22-lsp-prr-framework-rule-approval-gate` entry in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`. The reviewer's gate explicitly
requires user sign-off before any of these readings can land as
load-bearing framework rules.

## What this packet is

This packet asks the user (framework author) to **explicitly approve, defer, or reject** three candidate framework-rule readings on the measurement / observable side of the framework. None of them are derivable from Axiom 1 (qubit per site) plus Axiom 2 (Z³ lattice) alone — each is a substantive physical commitment about the framework's operational behavior.

The R1 (k=1 per-site selection) ratification went through this same gate via PR #1656 with explicit user approval. PR #1658 attempted to ratify LSP and PRR without going through the gate; it was correctly closed by the review-loop with the reviewer note:

> *"Both LSP and PRR are new framework-rule commitments rather than derivations from Axiom 1 / Axiom 2, so they require explicit user approval before any ratification or audit-dispatch sidecar can land."*

This packet records each candidate rule with a layman's explanation, the technical statement, what it commits the framework to, what it would unlock, and a sign-off line. No row in the audit ledger changes from this packet; only the user's signed-off decisions on which (if any) to ratify drive the follow-up ratification PRs.

## What this packet is NOT

- Not a ratification — no framework rule is added by this PR
- Not a re-audit — no row's status changes
- Not a runner-bearing claim
- Not a self-promotion of any candidate rule
- Not a substitute for the conditional bridges that already encode the
  math (those landed in PR #1635 for PRR, PR #1651 for LSP, and exist
  as a draft sketch for PWC in this packet's appendix)

## How to use this packet

For each candidate rule, the user reads the **plain-English explanation** first, then the **technical statement** and **what it commits the framework to**. The user can independently:

- **Approve** the rule (record sign-off; follow-up PR will draft the ratification + dispatch + companion runner)
- **Defer** the rule (keep the math available as conditional bridges; don't promote to framework rule)
- **Reject** the rule (don't add to the framework; explore alternatives)

Sign-off section at the bottom provides explicit lines for each.

---

## Rule 1 — LSP (Lüders Sequential-Product instrument selection)

### Layman's explanation

When the framework measures whether some property `P` holds — say, "is this qubit pointing up?" — and gets the answer "yes," what happens to the system after the measurement?

LSP commits the framework to the **minimum-disturbance** reading: the measurement just **filters** the state down to the part consistent with the "yes" answer. It doesn't rotate, scramble, or otherwise modify the state beyond that filtering.

Mathematically there are many possible "yes"-measurements that all agree on the *probability* of getting "yes," but disagree on what the state looks like AFTER. Some include a hidden rotation or basis change as part of the measurement act. LSP commits to the version that doesn't add any extra rotation — just the bare filter.

An analogy: imagine you have a die and you ask "is this an even number?" The answer "yes" leaves you knowing it's 2, 4, or 6 — but it doesn't change *which* even number is on top. LSP is the framework's commitment that quantum measurement works the same way: the answer constrains, but doesn't gratuitously rearrange.

### Technical statement

> **LSP.** For projective measurement of an orthogonal projection `P ∈ A_Λ` on a finite qubit-lattice region, the framework's measurement instrument is the Lüders Kraus operator `K_P := P`. Sequential composition of "outcome `P` then effect `E`" is then `M_{P, E} := K_P† E K_P = P E P`.

### What it commits the framework to

- The Lüders state-update rule `σ ↦ P σ P / Tr(P σ P)` after a "yes" outcome
- Sequential measurement composition follows the standard `P E P` formula
- Alternative instruments (e.g., `K_P^twist := U · P` for a unitary U) are NOT the framework's selection, even though they give the same outcome probabilities

### What it does NOT commit the framework to

- Doesn't constrain dynamics (free evolution between measurements)
- Doesn't pick a specific Hamiltonian or measurement schedule
- Doesn't apply to POVMs that aren't projective; those have their own
  instrument-selection question

### What it unlocks if approved

| Row | Current | Under LSP |
|---|---|---|
| `luders_rule_from_composition_consistency_note_2026-05-20` | `audited_conditional` — `missing_bridge_theorem` on `M_{P,E} = P E P` | Step-1 sequential composition becomes load-bearing consequence of LSP |
| `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22` (PR #1651) | unaudited conditional | Conditional becomes unconditional |
| `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20` | unaudited | One blocker removed (still needs PRR + the rest of the chain) |

### Background on why it's a framework rule, not a theorem

The literature explicitly shows the sequential product on the effect algebra `E(H)` is **not unique** — there are mathematically valid alternative sequential products that don't reduce to `P E P` (arXiv:0905.0596 Gudder counterexample; arXiv:math/0211033 broader landscape). A prior PR (#1626) tried to derive uniqueness from Greechie/Gudder axioms alone and was rejected for overclaim. The framework needs to commit to LSP as a *selection*, not a *derivation*, because no theorem on A1+A2 alone forces the selection.

### Sign-off for LSP

- [ ] **Approve LSP** — proceed to ratification PR + dispatch + companion runner
- [ ] **Defer LSP** — keep PR #1651 as conditional support; don't ratify
- [ ] **Reject LSP** — don't add to framework

---

## Rule 2 — PRR (Pre-Record Reference inner-unitary invariance)

### Layman's explanation

Before any measurement has been made — before any "record" of an outcome exists in the world — what state is the framework's substrate in?

PRR commits to the **no-information** reading: the pre-measurement state has no preferred direction, no preferred basis, no bias toward any particular outcome. If you looked at it through any rotated frame, it would look exactly the same.

Mathematically, the only state with that property is the **maximally mixed state** — a kind of "complete uncertainty," uniformly distributed across all possible outcomes. This is the state `ρ_ref = ⊗_x I/2` (each qubit independently in the 50/50 mix).

An analogy: imagine a fair coin that hasn't been flipped yet. From your perspective, before you flip and look, "heads" and "tails" are equally likely — you have no information yet about which way it'll land. PRR is the framework's commitment that the pre-measurement quantum state is the equivalent of "fair coin you haven't flipped" — no information yet, complete symmetry.

This is sometimes called the "reality is probability until recorded" reading. The state isn't "really" pointing one way — it's a uniform distribution over all possible answers, and the measurement creates the record that breaks the symmetry.

### Technical statement

> **PRR.** For every finite region `Λ ⊂ Z³`, the pre-record reference state `ρ_ref|_Λ` is invariant under every inner unitary automorphism: `U ρ_ref|_Λ U† = ρ_ref|_Λ` for every unitary `U ∈ U(A_Λ)`.

### What it commits the framework to

- The pre-record reference state is the maximally mixed state `ρ_ref = ⊗_x I/2`
- No preferred basis or direction before measurement
- Equivalent to: the state is the **unique tracial state** on the quasi-local UHF algebra (by Schur's lemma)

### What it does NOT commit the framework to

- Doesn't say what happens AFTER measurement (records can break symmetry)
- Doesn't constrain dynamics between measurements
- Doesn't apply to states that have *already* accumulated record content — only the bare pre-record reference

### What it unlocks if approved

| Row | Current | Under PRR |
|---|---|---|
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | `audited_conditional` — `missing_bridge_theorem` on no-extra-structure identification | Identification with unique tracial state becomes load-bearing consequence of PRR |
| `inner_automorphism_invariance_tracial_identification_narrow_theorem_note_2026-05-20` (salvaged PR #1635) | unaudited conditional | Conditional becomes unconditional |
| Born derivation chain | blocked | One blocker removed |
| **PWC (below) — if also approved** | needs PRR for tensor factorization | PWC's tensor-factorization step uses PRR |

### Background on why it's a framework rule, not a theorem

A1 (qubit per site) constrains the per-site algebra but says nothing about which specific state on that algebra is the "pre-record" reference. The maximally mixed state happens to be the unique inner-unitary-invariant state (by Schur's lemma — a standard math result), but the framework still has to commit that the pre-record reference IS that state. The "no information yet" reading is a physical commitment, not derivable from A1+A2 alone.

### Sign-off for PRR

- [ ] **Approve PRR** — proceed to ratification PR + dispatch + companion runner
- [ ] **Defer PRR** — keep PR #1635-salvage as conditional support; don't ratify
- [ ] **Reject PRR** — don't add to framework

---

## Rule 3 — PWC (Physical-W as Cumulant generator on ρ_ref)

### Layman's explanation

When the framework wants to compute a physical scalar quantity from the substrate — energy, free energy, action, entropy, etc. — what's the recipe?

PWC commits to the **standard quantum statistical-mechanics recipe**: physical scalars are **logarithms of probability sums**. Specifically:

```text
W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref · 1)
```

In plain English: you take the pre-record reference state, weight it by an exponential of the source `J` (this captures how `J` influences probabilities), sum it all up, take the log, and subtract a normalization. That log-of-probability-sum IS what the framework calls a "physical scalar."

Why "log" specifically? Because the log function has a special property: when you multiply probabilities, the logs add. Physical scalars need to **add** on independent subsystems (an energy of a combined system is the sum of energies of the parts; same for free energy, entropy, action). Only the log function turns the multiplicative probability structure into additive scalars.

Mathematically, you *could* use other functions like `Z^p` for various `p` — they all give well-defined real numbers — but only the log-version is additive. PWC commits that the framework's physical observables ARE the additive (log) kind, not the alternatives.

An analogy: when computing the "weight" of a stack of objects, you want a quantity that **adds** when you stack two piles together. The natural choice is weight in grams (additive), not weight squared or weight cubed. PWC is the framework's commitment that physical scalars are the "weight-in-grams" kind — they add on independent subsystems.

### Technical statement

> **PWC.** The framework's physical scalar generator `W[J]` is the source cumulant generator on the pre-record reference state:
> ```
> W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref).
> ```
> Physical scalar observables are derivatives of `W[J]` evaluated at `J = 0`.

### What it commits the framework to

- Physical W is the log-partition / Gibbs free-energy form — not alternatives like `Tr(ρ_ref · e^{-J})^p` for `p ≠ 0`
- The framework's observables are probability cumulants (operationally derived from Born probabilities on ρ_ref)
- Additivity on independent subsystems is automatic (follows from PRR's tensor factorization + log-of-product algebra)

### What it does NOT commit the framework to

- Doesn't pick a specific Hamiltonian or source-coupling rule
- Doesn't commit to specific numerical predictions
- Doesn't claim that all physical quantities are this W; only the framework's source-cumulant generator
- Doesn't replace the existing 11+ P1-route notes (Pattern L circularity analyses); they remain as alternative-route exploration

### What it unlocks if approved

This is the **biggest single unlock available** in the framework if approved:

| Row | Current | Under PWC |
|---|---|---|
| **`observable_principle_from_axiom_note`** (#1 most load-bearing audited_conditional row) | `audited_conditional`, score **53.57**, **1006+ transitive descendants** | P1 (scalar additivity) becomes load-bearing consequence of PWC + PRR + A2 tensor composition. Parent eligible for retained |
| `OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20` (already drafted) | unaudited | Becomes the runner-backed companion theorem under PWC |
| Born derivation chain | blocked on P1 | Major blocker removed |
| Standard-Model connection chain (gauge couplings, three generations, hierarchy) | blocked on P1 | Foundational blocker removed |
| 11+ in-flight P1-route notes (Connes, Tomita-Gibbs, Jones-index, etc.) | all `no_go` | Pattern L circularity sidestepped at the physical-interpretation level |

### Background on why it's a framework rule, not a theorem

P1 (scalar additivity on independent subsystems) is required to make the framework's physical quantities behave like physical quantities (extensive). Every prior attempt to derive P1 from A1+A2 alone has been classified as `no_go` because of "Pattern L circularity": the only function making multiplication into addition is the log, so "select additive" trivially gives "select log" — but the load-bearing question is *why* the framework's W is the additive one rather than `Z^p`.

PWC sidesteps this by committing **at the physical-interpretation level**: the framework's W IS the probability cumulant generator on ρ_ref. Alternatives like `Z^p` exist as mathematical objects but don't correspond to "probability cumulants" — they're a different physical interpretation that the framework's "reality is probability until recorded" commitment doesn't admit.

This is a substantive physical commitment, not a theorem. It needs explicit user approval.

### Sketch of the under-PWC derivation of P1 (for context only)

Given PWC + PRR + A2 tensor composition:

1. By A2 tensor composition, disjoint regions `Λ_1, Λ_2` give `A_{Λ_1 ∪ Λ_2} = A_{Λ_1} ⊗ A_{Λ_2}`
2. By PRR (R3 if approved), `ρ_ref|_{Λ_1 ∪ Λ_2} = ρ_ref|_{Λ_1} ⊗ ρ_ref|_{Λ_2}`
3. For commuting sources `J_A ∈ A_{Λ_1}`, `J_B ∈ A_{Λ_2}` (commute because supported on disjoint sub-algebras):
   ```
   e^{-(J_A ⊕ J_B)} = e^{-J_A} ⊗ e^{-J_B}
   ```
4. Tomita tensor-trace factorization (already retained):
   ```
   Tr_{Λ_1 ∪ Λ_2}((ρ_ref|_{Λ_1} ⊗ ρ_ref|_{Λ_2}) · (e^{-J_A} ⊗ e^{-J_B}))
     = Tr_{Λ_1}(ρ_ref|_{Λ_1} · e^{-J_A}) · Tr_{Λ_2}(ρ_ref|_{Λ_2} · e^{-J_B})
   ```
5. Taking logs:
   ```
   W[J_A ⊕ J_B] = W[J_A] + W[J_B]
   ```
6. This is **P1**.

Under PWC, the load-bearing step isn't "select additive over multiplicative" (the Pattern L objection). It's "physical W IS the probability cumulant generator on ρ_ref" — a commitment about what W *means*, not which functional to pick.

### Sign-off for PWC

- [ ] **Approve PWC** — proceed to ratification PR + dispatch + companion runner
- [ ] **Defer PWC** — keep the P1 chain conditional / explore other routes
- [ ] **Reject PWC** — don't add to framework

---

## Dependency notes

The three rules can be approved/deferred/rejected **independently** of each other, but they cascade:

- LSP alone unlocks the Lüders chain
- PRR alone unlocks the pre-record tracial chain
- PWC needs PRR's tensor factorization to do its work; approving PWC without PRR would land a weaker version
- PWC alone gives the biggest unlock (observable_principle parent + 1000+ descendants)

If you want to do them in stages, the dependency-respecting order is: PRR first (no dependencies), then LSP (independent), then PWC (uses PRR).

If you want to do them all at once, the follow-up bundle is three ratification PRs + three dispatch manifests + three companion runners.

## What this PR does NOT ship

- No actual ratification — that's the follow-up after sign-off
- No audit-dispatch sidecar — same
- No companion runner for PWC — that's drafted but waits on PWC approval
- No changes to MINIMAL_AXIOMS_2026-05-20 or QUBIT_AXIOM_HARDENING_NOTE
- No new audit ledger row promotions
- No runner runs

## After user approval

For each approved rule, the follow-up PR pattern (R1 template):

1. Add the rule clause to `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` (new section)
2. Add cross-link from `MINIMAL_AXIOMS_2026-05-20.md` commentary block
3. Write a runner-backed companion theorem if not already in place
4. Write a dispatch manifest listing the eligible re-audit rows
5. (When reviewer's audit-dispatch infrastructure lands) add a machine-readable dispatch sidecar

## Sign-off summary

The user signs off (or defers/rejects) by editing the sign-off lines above and adding a brief decision rationale in the merge comment. Once recorded, the follow-up ratification PRs can land per the R1 template.

The reviewer will independently confirm with the audit lane that the approved readings should be treated as load-bearing axiom-surface input on land.

## Citation-graph note

This is a meta decision-packet doc; all references are plain-text only. No load-bearing dep edges.

Plain-text pointer references:

- `docs/repo/ACTIVE_REVIEW_QUEUE.md` — `2026-05-22-lsp-prr-framework-rule-approval-gate` entry (the gate this packet is responding to)
- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` — R1 ratification template this packet follows
- `R1_REAUDIT_MANIFEST_NOTE_2026-05-22.md` — R1 dispatch manifest template this packet's follow-ups will follow
- `LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1651) — landed conditional LSP bridge
- `INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-20.md` (PR #1635-salvage) — landed conditional PRR bridge
- `OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md` — drafted unaudited PWC-style sketch
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — parent that PWC would unlock
