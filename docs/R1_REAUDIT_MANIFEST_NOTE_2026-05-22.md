# R1 Re-Audit Request Manifest

**Date:** 2026-05-22
**Type:** meta (audit-request navigation doc)
**Status:** source-side request; independent audit lane owns each re-audit verdict
**Companion to:** [`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md) § "Hardening II: k = 1 per-site selection (load-bearing ratification, 2026-05-22)"
**Depends on:** PR #1656 (ratifies clause (R1))

## Purpose

PR #1656 ratifies the **k = 1 per-site selection** as load-bearing axiom content under A1's "qubit at every lattice site" reading. This manifest catalogs the specific `audited_conditional` rows that become eligible for re-audit once (R1) is read by the audit lane as a strengthened axiom commitment rather than a definitional relabeling.

This doc does **not**:

- Re-audit any row (auditor-owned verdicts)
- Promote any row (status authority remains with the audit lane)
- Modify any existing source note's content
- Carry load-bearing dep edges (plain-text references only)

This doc **does**:

- List the audited_conditional rows whose verdicts cite the pre-2026-05-08-narrowing U4 admission or the substep-1 k = 1 selection
- For each, identify the specific re-audit hypothesis (R1) enables
- Cite the audit verdict text the framework asks the audit lane to revisit
- Provide a single place for the audit lane to drive batch re-audit under the strengthened A1 reading

## Re-audit candidates under (R1)

Each row below is currently `audited_conditional` with a verdict that (R1) directly addresses. All ledger statuses verified against `docs/audit/data/audit_ledger.json` on 2026-05-22.

### A. Substep-1 chain (staggered-Dirac realization gate)

#### A.1 `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17`

- **Current:** `audited_conditional`, score 0.00
- **Verdict text:** `dependency_not_retained: cheapest repair is to provide a retained-grade effective-status certificate for docs/CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md or audit this row explicitly as conditional on that decoration parent.`
- **Note's conditional sub-claim (C1):** *"if the per-site Hilbert space carries a single faithful Cl(3) module (k = 1), then dim_C H_x = 2 exactly."*
- **(R1) effect:** A1's "qubit" reading commits k = 1 as load-bearing axiom content. The conditional in (C1) is no longer required — k = 1 is fixed by A1 itself.
- **Re-audit hypothesis:** The conditional sub-claim becomes unconditional under (R1); the row should be eligible for `audited_clean` / retained promotion, contingent on dep-chain status under the strengthened axiom reading.

#### A.2 `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`

- **Current:** `audited_conditional`, score 14.54
- **Verdict text:** `dependency_not_retained: re-audit after replacing or upgrading the Cl(3) faithful-irrep dim-two dependency with a retained-grade authority, or include the retained parent chain needed to make that dependency retained-grade.`
- **(R1) effect:** The note's U4 admission ("per-site Hilbert IS Cl(3) faithful complex irrep on Z^3 substrate") becomes axiom content under (R1). The dependency-on-decoration concern is bypassed because (R1) gives the dim-two readout directly from A1.
- **Re-audit hypothesis:** Eligible for re-audit citing (R1) as the upstream strengthened axiom reading, with dep-chain via A1 instead of via the decoration sibling.

#### A.3 `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17`

- **Current:** `audited_conditional`, score 10.54
- **Verdict text:** `dependency_not_retained; cheapest repair is to provide a retained-grade status or complete retained dependency chain for docs/CL3_FAITHFUL_IRREP_DIM_TWO_NARROW_THEOREM_NOTE_2026-05-10.md, then re-audit this JW bridge.`
- **(R1) effect:** Same as A.2 — the U4 admission becomes axiom content under (R1). The JW construction on V ≅ ℂ² per site is well-defined directly from A1's qubit specification.
- **Re-audit hypothesis:** Eligible for re-audit under (R1).

### B. Per-site dim-2 consumer rows

The following rows all consume the per-site dim = 2 result. Their `missing_dependency_edge` verdicts post-2026-05-08 trace to the narrowing of the per-site uniqueness chain (which removed U4 from that chain's scope, leaving the dim-2 result conditional). (R1) closes the gap by supplying dim H_x = 2 directly from A1.

#### B.1 `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 13.04
- **(R1) effect:** Dim H_x = 2 follows in one line from A1 + (R1), bypassing the narrowed per-site-uniqueness chain.
- **Re-audit hypothesis:** Eligible for `audited_clean` / retained as a one-line corollary of A1 under (R1).

#### B.2 `no_per_site_bosonic_ccr_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 10.54
- **(R1) effect:** No-bosonic-CCR follows from finite-dim per-site = 2 (trace identity 0 ≠ d), where d = 2 is fixed by (R1).
- **Re-audit hypothesis:** Eligible for re-audit under (R1).

#### B.3 `no_per_site_chirality_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 12.04
- **(R1) effect:** No-per-site-chirality (a separate per-site result that consumed the narrowed U4-removed chain) closes under (R1) as the per-site Hilbert is uniquely ℂ² under A1's strengthened reading.
- **Re-audit hypothesis:** Eligible for re-audit under (R1).

#### B.4 `pauli_group_order_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 10.54
- **(R1) effect:** Pauli group |P| = 16 on a single qubit follows from per-site M_2(ℂ) under (R1).
- **Re-audit hypothesis:** Eligible for re-audit under (R1).

#### B.5 `q_integer_spectrum_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 11.04
- **Verdict text:** `missing_dependency_edge after 2026-05-08 narrowing of cited per-site uniqueness dep removed U4`
- **(R1) effect:** Q-integer-spectrum's per-site Hilbert dependence is closed by (R1).
- **Re-audit hypothesis:** Eligible for re-audit under (R1).

#### B.6 `per_site_su2_spin_half_theorem_note_2026-05-02`

- **Current:** `audited_conditional`, score 2.08
- **Verdict text:** `missing_dependency_edge after 2026-05-08 narrowing of cited per-site uniqueness dep`
- **(R1) effect:** Per-site su(2) spin-half identification closes under A1's qubit reading + (R1).
- **Re-audit hypothesis:** Eligible for re-audit under (R1).

### C. The U4 closure note itself

#### C.1 `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20`

- **Current:** `audited_renaming`, score 0.00
- **Verdict text:** *"If the qubit reframe of A1 is later treated by audit policy as a definitional equivalence rather than a load-bearing axiom (e.g. via QUBIT_AXIOM_HARDENING_NOTE_2026-05-20 ratification), this row could be reconsidered as audited_decoration under the cl3_complexification_split parent. As-is, the load-bearing step is identification (renaming), not corollary algebra, so audited_renaming is the more conservative non-clean verdict."*
- **(R1) effect:** This is exactly the case the auditor's own follow-up note flagged. With (R1) ratifying the qubit reframe as load-bearing rather than definitional, the U4 closure becomes:
  - A *decoration* of the load-bearing A1+(R1) commitment — `audited_decoration` under `cl3_complexification_split_narrow_theorem_note_2026-05-10` parent (the auditor's own suggested target);
  - OR an `audited_clean` recording of a load-bearing identification step, depending on whether the audit lane treats (R1) as a definitional addendum to A1 or as a separate framework rule on the same authority surface.
- **Re-audit hypothesis:** The row should be moved from `audited_renaming` to `audited_decoration` (or `audited_clean`) under (R1), per the auditor's stated repair criterion.

## Reviewer ask

This manifest is the framework's request to the audit lane to **batch-re-audit the rows in §A, §B, §C above** with (R1) cited as the strengthened upstream axiom reading. Specifically:

1. Confirm (R1) from PR #1656 is now in effect on the canonical axiom surface (`MINIMAL_AXIOMS_2026-05-20.md` A1 + `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § "Hardening II")
2. Re-evaluate each row's `audited_conditional` verdict under (R1)
3. Where the verdict text references the per-site-uniqueness narrowing or the k = 1 admission, apply (R1) as the load-bearing closure
4. Record the re-audit verdicts in the standard audit ledger format

The framework does **not** propose specific new verdicts; the manifest only identifies which rows are eligible for re-audit and which verdict-text clauses (R1) addresses.

## What this PR is not

- **Not a self-promotion** of any row. All status changes are audit-lane decisions.
- **Not a derivation.** (R1) is an axiom strengthening recorded in PR #1656; this manifest only catalogs its downstream effects on existing verdicts.
- **Not a unilateral re-axiomatization.** A1's content is unchanged; the strengthened reading is recorded as a framework rule on the same authority surface.
- **Not a load-bearing dep node.** This is a navigation / audit-request doc; the citation-graph builder should not see it as carrying upstream theorem deps. All references below are plain-text only.

## Plain-text pointer references (NOT load-bearing deps)

- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` — upstream PR #1656 ratification doc carrying clause (R1) in § "Hardening II"
- `MINIMAL_AXIOMS_2026-05-20.md` — canonical axiom doc with inline (R1) cross-link
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — open-gate parent whose substep-1 U4 bridge is closed by (R1); substeps 2-4 remain open
- `U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md` — the `audited_renaming` row whose audit verdict explicitly identified this ratification path

## What independent audit ownership means here

The audit lane retains sole authority over each re-audit verdict. This manifest is the framework's audit-request artifact — it identifies eligibility under the strengthened axiom reading. The audit lane evaluates the strengthened reading on its own terms, applies its standard verdict rules, and records whatever outcome those rules produce. The manifest does not predict, prescribe, or constrain that outcome.

This is the same pattern used for any framework-rule strengthening: the framework records the change on its authority surface; the audit lane independently applies the updated reading on next re-audit.
