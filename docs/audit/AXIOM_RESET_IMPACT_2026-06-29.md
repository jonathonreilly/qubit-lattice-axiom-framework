# Axiom Reset Impact Map (2026-06-29)

**Claim type:** meta
**Status:** draft PR impact note for PR #4747

This note maps the expected repo impact of replacing the prior
Lattice/Quantum/Record baseline with the Lattice/Qubit/Admissibility/Record
baseline in `docs/MINIMAL_AXIOMS_2026-06-29.md`.

It does not apply any audit verdict, admit any new Tier-A target, or refresh the
generated audit ledger/queue files.

## Reviewer Instruction

PR #4747 intentionally does not commit the generated audit-pipeline refresh.
After the axiom wording and methodology updates are accepted, the reviewer or
audit owner should run:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

The refresh should be reviewed as mechanical generated fallout from the
`minimal_axioms` premise hash change, not as new audit verdicts.

## Dry-Run Audit Impact

A dry run on the PR branch, performed in a throwaway worktree before the final
Admissibility wording pass, produced this mechanical impact:

- `minimal_axioms` has 290 direct graph dependents and roughly 1700 transitive
  dependents.
- The pipeline reset 251 previously settled rows to `unaudited`.
- The audit queue changed from 1492 pending / 0 ready to 1743 pending / 80
  ready.
- Ready rows included core surfaces in tensor-product translation,
  no-per-site chirality, staggered Dirac forcing, probability/Gleason/Busch
  bridges, record-formation no-go surfaces, observable-principle rows, and the
  Rconn EW-register open gate.
- `audit_lint.py` remained clean except for the pre-existing notice set.

The effect is therefore a foundation reset with a large audit blast radius, not
a wording-only change.

## Primitive And Tier-A Impact

The approved primitive set remains:

- `minimal_axioms`
- `scale_reference_primitive`
- `kinetic_isotropy_primitive`
- `realized_state_primitive`

Tier-A admitted derivation targets remain exactly:

- `AC_phi_lambda`
- `theta`

Admissibility does not absorb either Tier-A target. It also does not absorb the
`realized_state_primitive`: Admissibility determines site-level availability
through nearest-neighbor conditions, while the realized-state primitive permits
pointwise evaluation at a supplied law-admissible realized state.

## Blocked-Lane Impact

The reset improves premise hygiene by replacing an untyped realization/record
surface with four separated ontology roles:

- **Lattice** says where physical locality is carried.
- **Qubit** says each site has a domain of local possibilities, whose full
  one-site algebraic presentation is `M_2(C)`.
- **Admissibility** says one fixed nearest-neighbor rule, covariant under
  lattice translations and proper cubic rotations, determines the available
  subset of possibilities at each site.
- **Record** says a record locks one available local possibility, only records
  are readable, and scalar readout is additive over finite pairwise-disjoint
  record collections.

This directly addresses the arbitrary-record-mosaic gap: records are not free
assignments independent of the local constraint. It does not by itself promote
downstream rows that require:

- readout-context selection or measurement-basis selection;
- probability, Born weights, occurrence rules, or update laws;
- local observability or Darwinism-style redundant witness structure;
- central-sector decomposition or `K`/CPT structure;
- source/action bridges, log-det readouts, P2/modulus structure, or arbitrary
  observable identification;
- species/gauge selectors or physical carrier identification;
- nonzero kinetic branch selection, Dirac-square carrier selection, or temporal
  evolution.

Those structures remain compatible downstream targets, but they require
derivation, bridge, explicit admission, or approved primitive registration
before use as load-bearing content.

## Completeness Verdict

The four-axiom set is complete enough for the minimal ontology reset and for
premise policing of record availability:

- unrecorded sites carry local possibility;
- the available possibilities are determined by, and vary with, the
  nearest-neighbor conditions
  at each site;
- a record can lock only an available local possibility;
- finite scalar record readout is additive over disjoint record collections.

It is not complete enough, by itself, to unblock every predictive audit lane.
The remaining predictive work belongs downstream: probability/weighting,
readout contexts, physical observable bridges, kinetic branch selection,
source/action structure, and temporal dynamics must be derived, bridged,
explicitly admitted, or registered as approved primitives before audit rows may
use them.

## Dynamics Direction

The useful 30,000-foot split is:

1. **Admissibility / record-availability layer.** This concerns which
   possibilities are available at each site through nearest-neighbor
   conditions.
2. **Spatial kinetic branch layer.** This concerns whether the realized spatial
   kinetic context is scalar/trivial or a nonzero first-order Dirac-square
   carrier.
3. **Temporal dynamics layer.** This concerns Hamiltonians, transfer matrices,
   record preservation, clock rates, and physical persistence.

The current d=3 / B-Z2 / static-propagation blockers mostly live in the second
layer, not the third. They are about static spatial kinetic structure over a
Brillouin-zone or lattice-Green surface, not yet about a full time-evolution
axiom.

The right next direction is therefore not to add a broad "Dynamics" axiom to
the foundation set. PR #4747 should keep the axiom base as the ontology and
availability reset, then handle kinetic nontriviality as a separate downstream
target:

- either derive the nonzero Dirac-square branch from retained authorities;
- or explicitly propose a narrow realized-kinetic-branch primitive/admission
  and register it only after owner approval and review;
- then re-audit the affected d=3 / B-Z2 / propagation rows against that
  admitted or derived branch.

If a realized-kinetic-branch primitive is proposed, it should not be phrased as
only "the Bloch family has trivial joint commutant." A pair of noncommuting
Pauli matrices already has scalar joint commutant, so that condition is weaker
than saturating the three-generator grade-1 capacity. The load-bearing branch
condition should state the actual needed structure: nonzero first-order
Dirac-square kinetic carrier, translation covariance/locality as required by
the target theorem, and the mutually anticommuting self-adjoint-unitary
coefficient family if the d<=3 Clifford-capacity theorem is being invoked.

One further governance point matters: the current Lattice axiom already names
`Z^3`. Under PR #4747, d=3 is part of the foundation surface, not newly derived
from dynamics. If the project goal changes to deriving the spatial dimension
itself, Lattice must be generalized in a separate foundation reset and `Z^3`
must move downstream. PR #4747 does not do that larger move.

## Pre-Review Checklist

- Confirm the owner-approved axiom text in `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- Confirm the stable `minimal_axioms` registry note matches the four axiom
  names.
- Run the pipeline refresh only after review accepts the premise reset.
