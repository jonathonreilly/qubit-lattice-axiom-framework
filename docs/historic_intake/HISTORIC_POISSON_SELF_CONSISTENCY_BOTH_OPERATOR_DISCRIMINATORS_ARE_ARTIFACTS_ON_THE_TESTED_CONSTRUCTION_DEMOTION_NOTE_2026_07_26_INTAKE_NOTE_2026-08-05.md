# Historic intake: The attractiveness comparison and the 0.93 correlation in the self-consistency Poisson note are both empty discriminators, under the parent note's own parameters and its own decay diagnostic

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: closed_unmerged_never_landed
Era: post_reset_2026_06_29 — no axiom load-bearing; operators and propagator imported bit-identically from scripts/frontier_self_consistent_field_equation.py

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

On the parent note's own imported construction the response kernel K = d_rho/d_phi is sign-indefinite (frac(K<0) = 0.70..0.78) while the inverse Dirichlet graph Laplacian is single-signed (frac(G>0) = 1.000000), so no scalar multiple connects them (least-squares relative residual 0.9987..0.9996); the matched point-to-point correlation is -0.058/-0.048/-0.031 against the parent note's reported 0.93, and that 0.93 threshold admits every exponent up to p = 4.57 including the r^-2.805 the verdict flags and (within 0.013) the 8.637 of the operator the note calls unphysical. Under per-operator source-sign normalization all four operators are attractive and monotone and Poisson ranks third of four by abs(beta-1) at N=20 and N=24.

Original verdict: The two named discriminators are empty (not reversed): the beta comparison does not favour Poisson and does not establish any operator in this family as best at any tested lattice size, removing the parent note's stated ground for Bounded Claim 1.
Scope: Every numerical row is scoped to the tested 3D Dirichlet cubic-lattice transfer-propagator construction at the parent note's parameters and stated lattice sizes; no row is a continuum-limit claim; L4 is a seven-point grid in k, not a statement about all k.
Escape conditions (negative claims): The negative is confined to the two named discriminators at the parent note's own working point and is explicitly NOT a claim that the lane's field equation is not Poisson, nor that any rival is better — R16 refuses that reading on two grounds: biharmonic's power-law fit is the worst of the four (R^2 = 0.8556 vs 0.9240 Poisson, 0.9855 for 1/r^2) and the abs(beta-1) gap 0.156 sits inside the parent note's own documented finite-size shift 0.280. Amplitude-artifact escape tested and closed (beta spread <= 0.0229 over an 80-fold G sweep). Test 1 (convergence) and Test 4 (screened sweep) survive; Bounded Claim 1 is proposed narrowed to the screened family rather than dropped.

## Why pulled (supervisor decision, on the record)

No-go: the response kernel is sign-indefinite (70-78% negative) vs single-signed inverse Laplacian — the two named discriminators on the landed Poisson row are EMPTY; first of the cluster.

## Provenance (pinned)

- Original path: `docs/POISSON_SELF_CONSISTENCY_BOTH_OPERATOR_DISCRIMINATORS_ARE_ARTIFACTS_ON_THE_TESTED_CONSTRUCTION_DEMOTION_NOTE_2026-07-26.md`
- Source commit: `2da0f23f932510294be7c3171b0012bf8fcf8f0c`
- git blob: `2301fba9541eebbb4b50b194d5124575421b1eac`
- sha256: `8395b1274ea565e37dededdfc7caeb6a1138111734750a5ae4e90841c1f2870f`
- Lines: 340; runners named: scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py, scripts/frontier_self_consistent_field_equation.py

## Attached evidence (registered with, not as, this claim)

- `docs/CYCLE710_VALUE_AND_NO_GO_GATES_2026-07-26.md` — Gate record for Cycle 710 — process record of 3092's no-go content.

## Flags carried

audit_required_before_effective_retained: true, bare_retained_allowed: false; the note records that its own author's preferred repair (removing per-layer renormalization) was falsified by test.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
