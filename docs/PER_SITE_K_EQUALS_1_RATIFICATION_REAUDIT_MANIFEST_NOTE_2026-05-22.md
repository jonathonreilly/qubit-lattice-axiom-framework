# Per-Site k = 1 Ratification Re-Audit Request Manifest

**Date:** 2026-05-22
**Type:** meta (audit-request navigation doc)
**Status:** source-side request; independent audit lane owns each re-audit verdict
**Companion to:** [`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md) § "Hardening II: k = 1 per-site selection (load-bearing ratification, 2026-05-22)"
**Axiom surface:** [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) Axiom 1
**Depends on:** landed commit `f471b5bd6`, which ratifies clause (R1) inside Axiom 1

## Purpose

Commit `f471b5bd6` ratifies the **k = 1 per-site selection** as load-bearing Axiom 1 content under the repo's "qubit at every lattice site" reading. This manifest catalogs rows whose current audit verdicts cite the earlier missing `k = 1` / legacy U4 per-site faithful-irrep authority. It asks the independent audit lane to re-check those rows against the updated axiom surface.

This doc does **not**:

- Re-audit any row (auditor-owned verdicts)
- Promote any row (status authority remains with the audit lane)
- Modify any existing source note's content
- Predict a new verdict for any candidate

This doc **does**:

- List the `audited_conditional` and `audited_renaming` rows whose verdicts cite the pre-2026-05-08-narrowing legacy U4 admission or the substep-1 `k = 1` selection
- For each, identify the specific re-audit question enabled by the per-site `k = 1` ratification
- Cite the audit verdict text the framework asks the audit lane to revisit
- Provide a single place for the audit lane to drive batch re-audit under the updated Axiom 1 reading
- Carry graph-visible links to the landed axiom authority documents for audit discoverability; this meta note is not itself theorem authority

## Re-audit candidates under the per-site k = 1 ratification

Each row below currently has a non-clean audit verdict with a clause that the per-site `k = 1` ratification may address if independent audit accepts it as load-bearing Axiom 1 authority. All ledger statuses were verified against `docs/audit/data/audit_ledger.json` on 2026-05-22 after commit `f471b5bd6`.

### A. Substep-1 chain (staggered-Dirac realization gate)

#### A.1 `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17`

- **Current:** `audited_conditional`, score 0.00
- **Verdict text:** `dependency_not_retained: cheapest repair is to provide a retained-grade effective-status certificate for docs/CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md or audit this row explicitly as conditional on that decoration parent.`
- **Note's conditional sub-claim (C1):** *"if the per-site Hilbert space carries a single faithful Cl(3) module (k = 1), then dim_C H_x = 2 exactly."*
- **Ratification effect to test:** Axiom 1's "qubit at every lattice site" reading now records `k = 1` as load-bearing axiom content. Independent audit should decide whether that removes the conditional premise in (C1).
- **Re-audit question:** Is the row now closed from Axiom 1 plus the landed per-site `k = 1` ratification, or does another dependency remain non-retained?

#### A.2 `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`

- **Current:** `audited_conditional`, score 14.54
- **Verdict text:** `dependency_not_retained: re-audit after replacing or upgrading the Cl(3) faithful-irrep dim-two dependency with a retained-grade authority, or include the retained parent chain needed to make that dependency retained-grade.`
- **Ratification effect to test:** The legacy U4 per-site faithful-irrep admission is a candidate for removal if audit accepts the per-site `k = 1` ratification as the upstream Axiom 1 authority for the one-qubit local module.
- **Re-audit question:** Can the dependency chain run through Axiom 1's ratified one-qubit reading instead of through the non-retained decoration sibling?

#### A.3 `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17`

- **Current:** `audited_conditional`, score 10.54
- **Verdict text:** `dependency_not_retained; cheapest repair is to provide a retained-grade status or complete retained dependency chain for docs/CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md, then re-audit this JW bridge.`
- **Ratification effect to test:** Same as A.2: the legacy U4 per-site faithful-irrep admission may be replaceable by the ratified one-qubit local module.
- **Re-audit question:** Does the JW construction on `V ≅ ℂ²` per site close directly from Axiom 1's qubit specification, or does another load-bearing dependency remain?

### B. Per-site dim-2 consumer rows

The following rows all consume the per-site `dim = 2` result. Their `missing_dependency_edge` verdicts post-2026-05-08 trace to the narrowing of the per-site uniqueness chain, which removed the legacy U4 premise from that chain's scope and left the dim-2 result conditional. The per-site `k = 1` ratification is the proposed authority for re-checking whether `dim H_x = 2` now follows directly from Axiom 1.

#### B.1 `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 13.04
- **Ratification effect to test:** `dim H_x = 2` may follow from Axiom 1 plus the per-site `k = 1` ratification, instead of relying on the narrowed per-site-uniqueness chain.
- **Re-audit question:** Does the row close as a one-line consequence of the ratified one-qubit local module, or does audit still require an additional retained dependency?

#### B.2 `no_per_site_bosonic_ccr_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 10.54
- **Ratification effect to test:** No-bosonic-CCR may follow from finite-dimensional per-site `d = 2` (trace identity `0 ≠ d`) if audit accepts that `d = 2` is fixed by the ratified one-qubit local module.
- **Re-audit question:** Does the non-CCR conclusion close under that updated upstream authority?

#### B.3 `no_per_site_chirality_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 12.04
- **Ratification effect to test:** This separate per-site result consumed the narrowed legacy U4-removed chain. It is a re-audit candidate if the per-site Hilbert module is now fixed to `ℂ²` by Axiom 1's ratified qubit reading.
- **Re-audit question:** Does the no-per-site-chirality conclusion close from that authority, or does it still need a separate retained chain?

#### B.4 `pauli_group_order_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 10.54
- **Ratification effect to test:** Pauli group `|P| = 16` on a single qubit may follow from per-site `M_2(ℂ)` once the one-qubit local module is ratified as Axiom 1 content.
- **Re-audit question:** Does the row close under the updated local-algebra authority?

#### B.5 `q_integer_spectrum_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 11.04
- **Verdict text:** `missing_dependency_edge after 2026-05-08 narrowing of cited per-site uniqueness dep removed U4`
- **Ratification effect to test:** Q-integer-spectrum's per-site Hilbert dependence is a candidate for closure under the ratified one-qubit local module.
- **Re-audit question:** Does the spectrum result now have retained-grade upstream support, or is another bridge still missing?

#### B.6 `per_site_su2_spin_half_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 2.08
- **Verdict text:** `missing_dependency_edge after 2026-05-08 narrowing of cited per-site uniqueness dep`
- **Ratification effect to test:** The per-site `su(2)` spin-half identification is a candidate for closure under Axiom 1's ratified qubit reading.
- **Re-audit question:** Does this identification now follow from the one-qubit local module, or does audit still classify it as conditional/renaming/decoration?

### C. The U4 closure note itself

#### C.1 `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20`

- **Current:** `audited_renaming`, score 0.00
- **Verdict text:** *"If the qubit reframe of A1 is later treated by audit policy as a definitional equivalence rather than a load-bearing axiom (e.g. via QUBIT_AXIOM_HARDENING_NOTE_2026-05-20 ratification), this row could be reconsidered as audited_decoration under the cl3_complexification_split parent. As-is, the load-bearing step is identification (renaming), not corollary algebra, so audited_renaming is the more conservative non-clean verdict."*
- **Ratification effect to test:** This is the case flagged by the prior auditor's follow-up note. The landed per-site `k = 1` ratification asks audit to decide whether the row remains a renaming, becomes an algebraic decoration under a retained parent, or closes in another allowed audit status.
- **Re-audit question:** Does the ratification satisfy the prior repair criterion, and if so what standard audit verdict should replace `audited_renaming`?

## Reviewer ask

This manifest is the framework's request to the audit lane to **batch-re-audit the rows in §A, §B, §C above** with the per-site `k = 1` ratification cited as the updated upstream Axiom 1 reading. Specifically:

1. Confirm the per-site `k = 1` ratification from commit `f471b5bd6` is now in effect on the canonical axiom surface (`MINIMAL_AXIOMS_2026-05-20.md` Axiom 1 + `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening II")
2. Re-evaluate each listed row's current non-clean verdict under that ratification
3. Where the verdict text references the per-site-uniqueness narrowing or the `k = 1` admission, decide whether the ratification supplies the load-bearing closure
4. Record the re-audit verdicts in the standard audit ledger format

The framework does **not** propose specific new verdicts; the manifest only identifies which rows are eligible for re-audit and which verdict-text clauses the per-site `k = 1` ratification may address.

## What this PR is not

- **Not a self-promotion** of any row. All status changes are audit-lane decisions.
- **Not a derivation.** Clause (R1) is a load-bearing Axiom 1 ratification recorded in commit `f471b5bd6`; this manifest only catalogs possible downstream audit questions.
- **Not a new axiom.** The local-algebra content `M_2(ℂ) ≅ Cl(3,0)` is unchanged; the per-site `k = 1` selection is now explicit inside Axiom 1's qubit reading.
- **Not theorem authority.** This is a navigation / audit-request doc. Graph-visible links below are present so the audit pipeline can discover the landed axiom authority; they do not make this meta note a premise for the candidate rows.

## Pointer references

- [`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md) — landed ratification doc carrying clause (R1) in § "Hardening II"
- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — canonical axiom doc with inline clause (R1) cross-link
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — open-gate parent whose substep-1 U4 bridge is a re-audit target under the ratification; substeps 2-4 remain open
- `U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md` — the `audited_renaming` row whose audit verdict explicitly identified this ratification path

## What independent audit ownership means here

The audit lane retains sole authority over each re-audit verdict. This manifest is the framework's audit-request artifact: it identifies eligibility under the updated Axiom 1 reading. The audit lane evaluates the ratification on its own terms, applies its standard verdict rules, and records whatever outcome those rules produce. The manifest does not predict, prescribe, or constrain that outcome.

This is the same pattern used for any framework-rule strengthening: the framework records the change on its authority surface; the audit lane independently applies the updated reading on next re-audit.
