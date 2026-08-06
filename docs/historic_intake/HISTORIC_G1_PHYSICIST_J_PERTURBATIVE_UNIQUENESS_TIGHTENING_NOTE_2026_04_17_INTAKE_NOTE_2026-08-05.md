# Historic intake: G1 Physicist-J - Perturbative-Scale Uniqueness Tightening of the PMNS-as-f(H) Closure

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Adversarial review found the Physicist-H closure was NOT unique: over the wide box [-5,10]^3 there are exactly three in-chamber chi^2 = 0 basins - Basin 1 (0.657, 0.934, 0.715) with sin delta_CP = -0.987, Basin 2 (28.0, 20.7, 5.0) with +0.554, and Basin X at permutation (2,0,1) with -0.419 - and only the retained perturbative-scale criterion ||J|| <= ||H_base|| (Frobenius 0.941 and operator 0.858 for Basin 1 versus 20.88/17.62 and 13.92/11.35) selects Basin 1.

Original verdict: Closes four adversarial issues (basin non-uniqueness, permutation non-uniqueness, the U_e = I citation chain, delta_CP framing) and states the theta_23 upper-octant conditionality as a falsifiable retained structural prediction.
Scope: Uniqueness is SCALE uniqueness from the axiom-native log-det expansion's convergence discipline, not variational uniqueness; the closure is additionally CONDITIONAL on theta_23 being in the upper octant, with the threshold measured to 4 digits.


## Why pulled (supervisor decision, on the record)

Adversarial tightening: THREE chi^2 = 0 basins (not one), permutation ambiguity, citation-chain repair — the closure corrected on the record.

## Provenance (pinned)

- Original path: `docs/G1_PHYSICIST_J_PERTURBATIVE_UNIQUENESS_TIGHTENING_NOTE_2026-04-17.md`
- Source commit: `b2899d831e1257e5761a6c4c205d0e0c02d66853`
- git blob: `00dc092cb21073da46530124edb528a8db44de41`
- sha256: `200d19393b3093e3795124c0960f7e8126733f5e8d0f7e5776875659c78ef661`
- Lines: 447; runners named: scripts/frontier_g1_physicist_j_perturbative_uniqueness_theorem.py

## Attached evidence (registered with, not as, this claim)

- `docs/G1_PHYSICIST_H_PMNS_AS_F_H_CLOSURE_THEOREM_NOTE_2026-04-17.md` — PMNS-as-f(H) closure; uniqueness corrected by 535.
- `docs/G1_PHYSICIST_L_Z3_TRICHOTOMY_UE_IDENTITY_NOTE_2026-04-17.md` — Z_3 trichotomy repair; conditional on the underived q_H = 0 branch.

## Flags carried

Two CRITICAL adversarial findings against the sibling closure, including a second basin with OPPOSITE-sign delta_CP that reproduces all three observed angles to machine precision; the closure also became conditional on the theta_23 octant.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
