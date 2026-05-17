# Block 23 Report: cpt-exact-theorem (fresh lane)

**Block:** 23 (CPT, fresh lane)
**Date:** 2026-05-17
**Target:** `cpt_exact_note` — desc=697, claim_type=positive_theorem, audited_conditional
**Branch:** `physics-loop/cpt-exact-theorem-block23-2026-05-17`
**Worktree:** `/private/tmp/physics-loop-2026-05-17/block23-cpt-exact-theorem`

## Outcome

**POSITIVE narrow closure landed** as bounded class-A narrow theorem on
the algebraically-clean half of the parent bridge note that load-bears
on `cpt_exact_note`.

## Audit landscape ground (V1)

Pulled from `docs/audit/data/audit_ledger.json` at session start:

- `cpt_exact_note` — `audited_conditional` (effective), `positive_theorem`,
  desc=697, load-bearing 23.115.
- Verdict cause: cited dependency
  `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30`
  is itself `audited_conditional` (load-bearing-step class D).
- Bridge verdict (2026-05-16 codex-cli-gpt-5.5): "Clean only as a
  bounded free staggered lattice Hamiltonian statement: D anti-Hermitian
  implies H = iD Hermitian, naive CP K flips H, and Theta_H = P K
  preserves H with zero Theta_H-odd lattice Hamiltonian sectors on the
  checked even periodic lattices. Not clean as an unconditional
  physical SME-zero theorem beyond the explicitly defined lattice
  odd-sector proxy."
- Sister narrow theorems already retained-bounded (2026-05-17):
  `CPT_C3_CP_SQUARED_SCALAR_NARROW_THEOREM_NOTE` and
  `CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE`.

The two are independent: C3 closes `(CP)^2 = ε I`; the present block
closes the orthogonal `Θ_H = P K` Hermitian-lift symmetry half of the
bridge.

## V1-V5 fresh-lane check

- **V1 existence:** no existing narrow theorem isolates the
  framework-instance `Θ_H = P K` Hermitian-lift content. The
  `CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10` (C2)
  takes `Θ_H = P K` as a definition without framework-instance
  verification on the explicit C, P; the present narrow theorem
  supplies that.
- **V2 premise check:** premises are (D1), (D2), (D3) from parent
  `cpt_exact_note` algebraic core (class-A in parent runner) + abstract
  antiunitary K with K(i) = −i. No new axioms.
- **V3 orthogonality:** single load-bearing markdown-link dependency
  (`CPT_EXACT_NOTE.md`), and that citation hits the parent's
  algebraic-clean core, **not** the SME-bridge half that is
  conditional.
- **V4 downstream:** parent `cpt_exact_note` may cite the present
  narrow theorem for the Hermitian-lift algebra, dropping the bridge
  dependency for that half of the chain. The SME-bilinear conditional
  remains the bridge's content; not discharged here.
- **V5 forbidden imports:** none consumed (no PDG, no fitted, no SME
  numerics, no SME operator dictionary, no continuum CPT theorem, no
  interacting-theory inputs).

## Artifacts

- **Source note:**
  `docs/HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`
  (claim_type: `bounded_theorem`).
- **Runner:**
  `scripts/audit_companion_hermitian_lift_theta_h_pk_bounded_exact_2026_05_17.py`.
- **Runner cache:**
  `logs/runner-cache/audit_companion_hermitian_lift_theta_h_pk_bounded_exact_2026_05_17.txt`.

## Runner result

```
Summary: PASS=42  FAIL=0
Verdict: PASS.
```

Items covered (all class-A exact algebra; sympy 1-d slice + numpy 3-d
on `L ∈ {4, 6}`):

- Items 1-7: 3-d numpy verification at `L = 4` and `L = 6` (34 checks).
  Verifies (D1)-(D3) parent identities on construction, then (L1)
  `Θ_H^2 = I`, (L2) `Θ_H H Θ_H^{-1} = H`, (L3) `H_odd = 0` matrix-
  entrywise with `||H_odd||_F = 0` numeric, and (L4) `H_{μ,odd} = 0`
  for each `μ ∈ {1, 2, 3}`.
- Item 8: 1-d sympy slice at `L = 4` (6 checks, symbolic certainty
  for (L1)-(L3)).
- Item 9: counterfactual on the framework `L = 4` instance (2 checks).
  Confirms naive `CP K` lift sends `H → −H` per the bridge's "naive
  lift fails" observation; confirms `Θ_H = P K` correct lift.
- Item 10: out-of-scope marker (SME bilinear operator dictionary).
  Explicitly NOT verified per the parent bridge's open conditional;
  recorded as a hard scope boundary.

## Honest status

The narrow theorem closes the algebraically-clean half of the parent
bridge note as a class-A bounded theorem. The unconditional SME-zero
conclusion of the parent `cpt_exact_note` row remains
`audited_conditional` until the bridge's SME bilinear operator
dictionary, basis completeness, and exclusion proof are supplied by
separate authority. The present block reduces the conditional surface
of the chain by extracting the algebraic content as a class-A
retainable narrow theorem; it does **not** lift the parent
`cpt_exact_note` row to retained-grade because the SME-bridge half
remains the conditional bottleneck.

## What this block did NOT do

- Did not touch atlas, harness, audit-data, README, or lane-registry
  files.
- Did not derive the SME bilinear operator dictionary (out of scope:
  bridge's open conditional).
- Did not lift the parent `cpt_exact_note` audit status (which
  requires the SME-bridge half closure).
- Did not push to main; did not merge any PR.
- Did not invoke or change any continuum CPT-theorem authority.

## Time

Block 23 of 12-hour campaign. Source-only PR. A_min only.
