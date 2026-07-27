# Claim Status Certificate — poisson-self-bound-source (cycle 713)

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "Conditional on the isolation condition stated in the note: that an isolated object's binding energy must have a limit independent of the box it is measured in. Row R14 shows that under a different reference choice -- potential differences across a fixed window rather than the well bottom -- biharmonic is not excluded."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Every row is a finite computation on finite lattices. The box-independence statements are least-squares model comparisons on finite size sequences, not proofs of a limit. The operator family is the parent note's own four members, which is not an exhaustiveness result over local operators. The selection statement composes this block's gate with PR #5693's far-field result, and #5693 is itself unmerged and unaudited."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency classes

| Dependency | Class |
|---|---|
| `A_min` = Lattice + Qubit + Admissibility + Record | approved axiom baseline |
| Dirichlet nearest-neighbour graph Laplacian from `F.build_laplacian_sparse` | shared construction with the parent note, blob-verified in row P0 |
| `scripts/frontier_frozen_stars_rigorous.py` | landed runner, executed directly in rows F1/F2, blob-verified in row P0 |
| PR #5693 far-field result on a prescribed source | **unmerged, unaudited**; load-bearing only for the composed two-gate selection sentence in the thesis, not for any of R0-R14 |
| operator family, screening value `mu^2 = 0.25`, hopping `t = 1` | explicit conventions, listed in `ASSUMPTIONS_AND_IMPORTS.md` |

No observed target value, fitted selector, literature constant, or empirical
comparator is a proof input. No new axiom or framework primitive is used, and
the primitive-registry check found nothing this cycle needs to register.

## Why not a higher status

The claim-type certificate's item 4 fails: the composed selection sentence
depends on PR #5693, which is neither merged nor audited. Item 2 fails for the
same sentence. The block is therefore recorded as bounded support with a
`bounded_theorem` intended claim type, and rows R0-R14 stand on their own
without that composition.

Independent audit remains required before the repo may treat any of this as
retained-grade.

## Secondary finding

Rows F1/F2 report a measurement on `docs/FROZEN_STARS_RIGOROUS_NOTE.md`'s own
runner at its own parameters. That row is `criticality: leaf`, `verdict: null`,
`direct_in_degree: 0`, so nothing downstream depends on it. The finding is
reported for the audit lane's attention; this block does not re-audit it and
does not modify it.

## Review-loop disposition

Local pass, recorded in `REVIEW_HISTORY.md`. The no-go discipline gate's N7
steelman forced a demotion from an unconditional no-go against biharmonic to a
bounded theorem under a named isolation condition; that demotion is applied in
the note's thesis row and in `conditional_surface_status` above.
