# Framework-Rule Approval Packet: R1-corollary, LSP-projective, PRR, PWC (User Sign-Off Required)

**Date:** 2026-05-22
**Type:** meta (decision packet — NOT a ratification)
**Status:** awaiting explicit user approval, per the
`2026-05-22-lsp-prr-framework-rule-approval-gate` entry in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`. The reviewer's gate explicitly
requires user sign-off before any of these readings can land as
load-bearing framework rules.

## What this packet is

This packet asks the user (framework author) to **explicitly approve, defer, or reject** four candidate framework-rule readings on the measurement / observable side of the framework. None of them are derivable from Axiom 1 (qubit per site) plus Axiom 2 (Z³ lattice) alone — each is a substantive physical commitment.

**This packet has been revised after a five-physicist Nature-grade panel review** (foundations, stat-mech, lattice QFT, quantum information, math physics). The panel findings drive scope adjustments and explicit narrow-claim vs substantive-commitment framing for each rule. Specifically:

- **R1-corollary** (formerly "R1 ratification") and **LSP-projective** (narrowed from "LSP") came through the panel as **5/5 yes** on the narrow claim
- **PRR** splits cleanly: the math step is unanimous yes; the choice of ρ_ref = tracial is contested
- **PWC** has serious narrow-claim issues and the panel recommends defer

The R1 (k=1 per-site selection) ratification already landed via PR #1656 with explicit user approval. This packet's "R1-corollary" section confirms its compatibility with the panel review and does NOT propose any change to the landed R1. PR #1658 attempted to ratify LSP and PRR without going through the gate; it was correctly closed by the review-loop.

## What this packet is NOT

- Not a ratification — no framework rule is added by this PR
- Not a re-audit — no row's status changes
- Not a runner-bearing claim
- Not a self-promotion of any candidate rule

## How to use this packet

For each candidate rule, the user reads:

1. **Layman's explanation** — plain English first
2. **Narrow technical claim** — the precise mathematical/algebraic statement
3. **Substantive physical commitment** — what the framework would actually be approving as physical content
4. **Panel review findings** — what the 5 reviewers said about each
5. **Recommendation** — based on panel review
6. **Sign-off lines** — approve / defer / reject

The narrow-claim vs substantive-commitment distinction matters: in two cases (LSP, PRR) the math is unanimous-yes but the physical-commitment is contested. The panel review surfaces exactly which framing each rule survives.

---

## Panel review summary

Five role-played senior theoretical physicists, each with distinct specialty (foundations / stat-mech / lattice QFT / quantum information / math physics), independently reviewed each candidate rule. Each was asked to review as if for a Nature submission.

Verdict matrix (narrow-claim, after scope-correct framing):

| Rule | Found. | Stat-mech | Lattice QFT | QI | Math-phys | Panel net |
|---|---|---|---|---|---|---|
| R1-corollary (k=1 unpacking) | Yes | Yes | Yes (their reject was about A1 substrate, not R1) | Yes | Yes | **5/5 yes** |
| LSP-projective | Yes | Yes | Yes | Yes | Yes | **5/5 yes** |
| PRR (math step only) | Yes | Yes | Yes | Yes | Yes | **5/5 yes** |
| PRR (ρ_ref = tracial choice) | No (PBR) | Yes w/ caveat | No (β=0) | Yes w/ caveat | Yes w/ caveat | **2 reject / 3 contingent** |
| PWC (any framing) | Reject | No | Reject | Yes w/ caveat | No | **3 reject / 1 weak yes** |

Common panel critiques the packet now reflects:

- **Universal LSP** (covers all measurements, including POVMs) overreaches; **LSP-projective** (sharp projections only) survives
- **PRR's "no information yet" gloss** hides a strong β=0 / infinite-temperature commitment
- **PWC's "rules out Z^p" claim** is wrong (Rényi α-free-energies are perfectly physical) and the Pattern L circularity is relocated rather than resolved
- **R1 is the most defensible** rule, with all panel critiques landing on downstream gauge-emergence (already open work), not on R1's narrow content

---

## Rule 1 — R1-corollary (k = 1 per-site reading; A1 already landed)

### Layman's explanation

When the framework says "reality is a qubit at every lattice site," it commits to **exactly one qubit per site** — a single 2-dim complex Hilbert space — not a multi-copy bundle (k=2 means two copies, etc.). Multi-copy versions would carry hidden internal indices that could mimic extra matter content; R1 rules those out as the framework's substrate choice.

### Narrow technical claim

A1's "qubit at every lattice site" specifies the multiplicity index `k(x) = 1` (single faithful complex irrep of `M_2(ℂ) ≅ Cl(3,0)` per site), not the multi-copy module `ρ_+^{n_+} ⊕ ρ_-^{n_-}` with `n_+ + n_- ≥ 2`.

### Substantive physical commitment

Each site is exactly one qubit. The substrate has no per-site multiplicity beyond the bare two-dim algebra.

### Panel review findings

**5/5 yes** on the narrow claim. The lattice-QFT referee's rejection was about gauge-link variables and Wilson recognizability — a critique of the qubit substrate itself (A1, already landed), not of R1's k=1 unpacking. The same gauge-emergence concern applies identically to k=1 and to any per-site multiplicity. R1 is downstream-clean: no panel reviewer disputes the narrow content.

Caveats from individual reviewers (none rejections):
- Foundations: prefer naming honestly as "A1(b)" rather than "ratification of intent"
- Stat-mech: explicitly state the uniformity (no site-dependent k(x))
- QI: defend why d=2 over qudit-per-site (also a critique of A1 substrate, not R1)
- Math-physics: per-site type-I → quasi-local type-II_1 in the GNS completion is a type-jump worth disclosing

### Recommendation

**Approve.** Already landed via PR #1656; this packet confirms the panel finds R1-corollary "yes obviously" at the narrow-claim level. Downstream concerns are tracked by existing open gates.

### Sign-off

- [x] **Approved (already landed PR #1656)** — explicit ratification on `MINIMAL_AXIOMS_2026-05-20.md` and `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § Hardening II

---

## Rule 2 — LSP-projective (Lüders Sequential-Product, projective-only scope)

### Layman's explanation

When the framework measures whether a sharp property `P` holds — and gets "yes" — what happens to the state after?

LSP-projective commits to the **minimum-disturbance** reading: the state is just **filtered** down to the part consistent with the answer. No extra rotation, no extra phase, no extra basis change. Apparatus-induced disturbances are modeled separately as Hamiltonian evolution between measurements, not folded into the measurement act itself.

**Scope: projective measurements only.** Non-projective POVMs (weak measurements, ancilla-coupled measurements, smeared lattice observables) are explicitly left open for a separate framework rule.

### Narrow technical claim

For a projective measurement of an orthogonal projection `P ∈ A_Λ` on a finite qubit-lattice region, the framework's measurement instrument is the Lüders Kraus operator `K_P := P`. Sequential composition of "outcome P then effect E" is `M_{P, E} := K_P† E K_P = P E P`.

### Substantive physical commitment

For sharp projective measurements only: the measurement is minimum-disturbance. The framework does not commit to a universal measurement-instrument selection — non-projective POVMs are out of LSP-projective's scope.

### Panel review findings

**5/5 yes** on LSP-projective as scoped. The QI referee's rejection was specifically against framing LSP as a **universal** measurement-instrument rule (which would foreclose POVM tomography, weak measurements, ancilla-coupled measurements). Once narrowed to "projective measurement only," the QI referee accepts it.

Caveats:
- Foundations: resolve ontic-vs-epistemic ambiguity in the post-measurement state language elsewhere in the framework
- Stat-mech: state the non-projective POVM extension as a separate open gate
- Lattice QFT: note this is about idealized Lüders updates, not about transfer-matrix expectation values
- Math-physics: on tracial reference, LSP coincides with Connes-Størmer modular conditional expectation; for non-tracial states (finite-β KMS), they diverge — flag this scope

### Recommendation

**Approve LSP-projective.** Explicit narrowing: applies to sharp projective measurements only. Non-projective POVM instrument selection deferred to a future framework rule. The framework's existing Stinespring V construction (PR #1650, landed) takes arbitrary Kraus families {K_r} as input, which is the correct posture — LSP-projective fixes the special case, not the universal one.

### Sign-off for LSP-projective

- [ ] **Approve LSP-projective** — proceed to ratification PR + dispatch + companion runner, with explicit "projective-only" scope and non-projective POVM rule deferred
- [ ] **Defer LSP-projective** — keep PR #1651 as conditional support; don't ratify
- [ ] **Reject LSP-projective** — don't add to framework

---

## Rule 3 — PRR (Pre-Record Reference state)

### Layman's explanation (two pieces)

PRR is two separate things bundled together. The first is uncontroversial math; the second is a real physical choice the framework needs to make explicit.

**The math piece (uncontroversial):** *If* a state is invariant under every inner unitary rotation on every finite region, *then* by Schur's lemma it must be the maximally mixed state ρ = ⊗_x I/2.

**The substantive choice piece (contested):** *Should the framework's "pre-record reference" be that maximally mixed state?*

The "pre-record" label has been carrying a "fair coin before flipping = no information yet" connotation. But on the framework's UHF algebra, the maximally mixed state is the unique **infinite-temperature KMS state** — the β = 0 thermodynamic equilibrium. Choosing it as ρ_ref locks the framework into:

- **No thermal physics** at any nontrivial temperature (no finite-β Gibbs state ρ = e^{-βH}/Z)
- **No vacuum state** (ground states are not tracial except for trivial Hamiltonians)
- **No Tomita-Takesaki modular flow** (Δ = 1 on the tracial state — no Hawking, no Unruh, no Bisognano-Wichmann)
- **No β-dependent Wilson lattice gauge measure**

The framework's downstream physics (g_bare, three-generation matter, hierarchy) is supposed to be β-dependent. If ρ_ref is locked at β=0, recovering finite-β physics needs a separate framework rule (β-dressed reference).

### Narrow technical claims

**PRR-math:** For every finite region `Λ ⊂ Z³` and any state ρ ∈ A_Λ, if `U ρ U† = ρ` for every unitary `U ∈ U(A_Λ)`, then `ρ = I/2^|Λ|`. This extends to the unique tracial state τ on the quasi-local UHF algebra.

**PRR-physical:** The framework's pre-record reference state `ρ_ref` satisfies the PRR-math premise (inner-unitary invariance on every finite region). Equivalently: `ρ_ref = ⊗_x I/2`, the unique tracial state on the qubit-lattice UHF algebra.

### Substantive physical commitment

The framework's pre-record state is the **β=0 / infinite-temperature / unique-tracial** state. Finite-β physics requires a separate framework rule introducing a β-dressed reference (e.g., Gibbs `e^{-βH}/Z` with explicit Hamiltonian).

### Panel review findings

**PRR-math: 5/5 yes** (standard Schur + Powers-Glimm-Dixmier).

**PRR-physical: 2 reject / 3 yes-with-caveats:**
- Foundations: rejects on PBR/Spekkens grounds — "fair coin not yet flipped" reading is precisely what PBR-type theorems problematize
- Lattice QFT: rejects — Wilson lattice gauge theory's relevant measure is the β-dependent Gibbs measure, not the tracial reference
- Stat-mech: yes but explicitly disclose β=0 / infinite-temperature commitment, drop "fair coin" analogy
- QI: yes but flag that PRR is the tracial commitment, not merely an "epistemic uniformity" claim
- Math-physics: yes but acknowledge no Tomita modular flow / no KMS thermal physics / no vacuum

### Recommendation

**Two options:**

**(A) Approve PRR with explicit β=0 disclosure.** Land the math step plus an honest "this is the infinite-temperature reference; finite-β physics requires a separate rule" disclosure. The "fair coin" / "no information" language gets dropped or scoped.

**(B) Defer PRR.** Keep the math available as a conditional bridge (PR #1635-salvage already landed). Don't ratify ρ_ref = tracial as the framework's reference until the β-dependent extension is also drafted.

The panel split means (A) is workable but requires the disclosure framing be honest. (B) is the cleaner posture if the framework intends to later commit to a β-dressed reference (e.g., for Wilson lattice gauge theory).

### Sign-off for PRR

- [ ] **Approve PRR — option (A)** with explicit β=0 disclosure and dropped "fair coin" language
- [ ] **Defer PRR — option (B)** until β-dependent extension is drafted
- [ ] **Reject PRR** entirely

---

## Rule 4 — PWC (Physical-W as Cumulant generator)

### Layman's explanation

PWC was the proposed P1 unlock: commit that the framework's physical scalars are computed via "log of probability sums on the pre-record state." This was sold as sidestepping the Pattern L circularity (the "only log makes multiplication into addition" tautology).

**The panel review found the sidestep does not actually work.** Three of five reviewers reject PWC at the narrow-claim level (not just downstream consequences). The specific findings:

1. **The Pattern L sidestep is bookkeeping.** Restating "physical W IS log Z" as a physical commitment instead of a functional-selection doesn't dissolve the circularity; it relocates it (foundations referee).

2. **"Rules out Z^p" is wrong.** Rényi α-free-energies `F_α = -(1/β(α-1)) log Tr ρ^α` are perfectly physical and arise from Z^p-like structures. They show up in single-shot thermodynamics, large-deviation rate functions, and quantum information. PWC would incorrectly forbid them (stat-mech referee).

3. **Tracial reference makes PWC β=0 trivia.** On the tracial reference, W[J] is the infinite-temperature free energy — the standard QSM recipe at finite β is `W[J] = -β^{-1} log Tr(e^{-β(H+J)})` with a Gibbs reference, not the tracial state. Calling PWC "the standard QSM recipe" is misleading (math-physics referee; lattice QFT referee).

4. **No genuinely quantum content.** On a tracial reference, every connected cumulant of order ≥ 3 collapses to the classical-symmetric form. Under PWC + PRR, the framework's "physical scalars" inherit no genuinely quantum cumulant structure. The "biggest single unlock" framing actually purchases additivity by removing all the interesting physics (foundations referee; lattice QFT referee).

### Narrow technical claim (for completeness)

`W[J] := log Tr(ρ_ref · e^{-J}) - log Tr(ρ_ref)`, with ρ_ref the tracial state per PRR.

### Substantive physical commitment

Physical observables ARE probability cumulants (log Z form) on the tracial reference. Alternative interpretations (Rényi α-free-energies, state-dependent W[J;ρ], non-equilibrium scalars) are ruled out.

### Panel review findings

**3 reject / 1 no / 1 yes-with-caveats:**
- Foundations: REJECT — Pattern L circularity not actually resolved
- Stat-mech: NO — "rules out Z^p" overclaim is wrong; conflates definition with derivation
- Lattice QFT: REJECT — gives trivial β=0 generator; doesn't recover Wilson plaquette expectations
- QI: yes with caveats — recognizes it as ONE valid cumulant generator but not THE universal one
- Math-physics: NO — should use Araki relative-entropy on β-dependent reference, not tracial

### Recommendation

**Defer PWC.** The panel does not support landing it as a framework rule. Substantive rework required:

- Either replace tracial ρ_ref with a state-dependent reference (β-dependent Gibbs, or vacuum, or coherent)
- Or drop the "rules out Z^p" claim and frame PWC as a definition of one particular generating functional (not the universal one)
- Or pursue an operational derivation from a Naimark-dilated measurement model (foundations referee's suggestion) that doesn't presuppose the log form

P1 remains an open derivation target. The 11+ existing P1-route notes (Connes, Tomita-Gibbs, Jones-index, structural-reframing, etc.) all classified `no_go` for similar circularity reasons; PWC joins them rather than escaping them.

### Sign-off for PWC

- [ ] **Defer PWC** — do not ratify in current form; rework with state-dependent reference or operational derivation
- [ ] **Approve PWC** anyway (against panel recommendation) — note the panel-flagged risks
- [ ] **Reject PWC** entirely — don't pursue this route to P1

---

## Dependency notes (revised)

- **R1-corollary**: already landed (PR #1656)
- **LSP-projective**: independent; approval lands one ratification + dispatch + runner
- **PRR (math)**: 5/5 panel-yes; safe to land as a narrow theorem if user approves
- **PRR (physical commitment to tracial reference)**: needs decision; if approved, requires honest β=0 disclosure
- **PWC**: panel recommends defer; if approved, lands with explicit "narrow definition" framing (not universal scalar generator)

If you approve LSP-projective and PRR-math, that's a clean two-rule package. PRR-physical and PWC are independent contested decisions.

## What this PR does NOT ship

- No actual ratification — that's the follow-up after sign-off
- No audit-dispatch sidecar — same
- No companion runner — drafted only after sign-off
- No changes to MINIMAL_AXIOMS_2026-05-20 or QUBIT_AXIOM_HARDENING_NOTE
- No new audit ledger row promotions
- No runner runs

## After user approval

For each approved rule, the follow-up PR pattern (R1 template):

1. Add the rule clause to `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` (new section) with panel-flagged caveats explicit
2. Add cross-link from `MINIMAL_AXIOMS_2026-05-20.md` commentary block
3. Write a runner-backed companion theorem
4. Write a dispatch manifest listing the eligible re-audit rows
5. (When reviewer's audit-dispatch infrastructure lands) add a machine-readable dispatch sidecar

## Sign-off summary table

| Rule | Status | Recommendation |
|---|---|---|
| R1-corollary (k=1 reading) | landed PR #1656 | confirmed by panel review |
| LSP-projective (sharp projections only) | awaiting approval | panel-supported approve |
| PRR-math (Schur step) | awaiting approval | panel-supported approve |
| PRR-physical (ρ_ref = tracial) | awaiting approval | contested — approve with disclosure or defer |
| PWC (any framing) | awaiting approval | panel recommends defer |

The user signs off (or defers/rejects) by editing the sign-off lines above and adding a brief decision rationale in the merge comment. Once recorded, the follow-up ratification PRs can land per the R1 template.

The reviewer will independently confirm with the audit lane that the approved readings should be treated as load-bearing axiom-surface input on land.

## Citation-graph note

This is a meta decision-packet doc; all references are plain-text only. No load-bearing dep edges.

Plain-text pointer references:

- `docs/repo/ACTIVE_REVIEW_QUEUE.md` — `2026-05-22-lsp-prr-framework-rule-approval-gate` entry (the gate this packet is responding to)
- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § Hardening II — R1 ratification (already landed)
- `R1_REAUDIT_MANIFEST_NOTE_2026-05-22.md` — R1 dispatch manifest template this packet's follow-ups will follow
- `LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1651) — landed conditional LSP-projective bridge
- `INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-20.md` (PR #1635-salvage) — landed conditional PRR-math bridge
- `OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md` — drafted unaudited PWC-style sketch (now contested by panel)
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — parent that P1 would unlock (PWC was the proposed unlock route; panel recommends alternative routes)
- `PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md` (PR #1650, landed) — Stinespring V construction takes arbitrary {K_r}; consistent with LSP-projective narrow scope
