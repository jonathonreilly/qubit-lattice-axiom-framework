# Axiom Reset Impact Map (2026-06-29)

**Claim type:** meta
**Status:** draft PR impact note for PR #4747

This note maps the expected repo impact of replacing the prior
Lattice/Quantum/Record baseline with the Lattice/Qubit/Actualization/Record
baseline in `docs/MINIMAL_AXIOMS_2026-06-29.md`.

It does not apply any audit verdict, admit any new primitive, or refresh the
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

A dry run on the PR branch, performed in a throwaway worktree, produced this
mechanical impact:

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

Actualization does not absorb either Tier-A target. It also does not absorb the
`realized_state_primitive`: Actualization names definite realization in a
declared context, while the realized-state primitive permits pointwise
evaluation at a supplied law-admissible realized state.

## Blocked-Lane Impact

The reset improves premise hygiene by splitting definite realization from fixed
registration. It does not by itself promote downstream rows that require:

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

The four-axiom set is complete enough for the minimal ontology:

- **Lattice** says where local sites are.
- **Qubit** says what local alternatives exist.
- **Actualization** says that one context-indexed outcome is realized.
- **Record** says that the realized outcome can be fixed as a record.

It is not complete enough, by itself, to unblock the predictive audit lanes.
The missing ingredient is not probability and not metric time. The missing
ingredient is a law-admissibility/process layer that constrains which
actualizations and records are allowed to occur together.

A minimal candidate, if the owner decides to extend the foundation later, would
be:

> **Law / Admissible Transition.** For finite lattice regions with supplied
> boundary records, there is a local, composable, nontrivial admissibility
> relation on actualization/record extensions. It constrains which extensions
> are law-admissible. It does not assign probabilities or weights, choose a
> readout context, supply a measurement basis, define a time metric, select
> species/gauge content, fix source/action coefficients, or identify physical
> observables.

This is the minimal missing thing at the foundation level: not a full
Hamiltonian, not Born dynamics, not an empirical action, and not a clock.
It is the statement that reality's actualizations are law-constrained rather
than arbitrary.

This candidate would still not, on its own, select the nonzero Dirac-square
kinetic branch. It would make room for branch-selection theorems or admissions
without pretending the four ontology axioms already supplied them.

## Dynamics Direction

The parallel dynamics handoff attacks a real obstruction: Lattice, Qubit,
Actualization, and Record are satisfied by trivial/scalar realized behavior as
well as by a nonzero Dirac-square kinetic branch. Actualization names that a
context-indexed outcome is realized; it does not select which kinetic branch is
realized.

The useful 30,000-foot split is:

1. **Actualization / measurement layer.** This concerns definite outcomes,
   occurrence rules, probabilities, and update laws.
2. **Spatial kinetic branch layer.** This concerns whether the realized
   spatial kinetic context is scalar/trivial or a nonzero first-order
   Dirac-square carrier.
3. **Temporal dynamics layer.** This concerns Hamiltonians, transfer matrices,
   record preservation, clock rates, and physical persistence.

The current d=3 / B-Z2 / static-propagation blockers mostly live in the second
layer, not the third. They are about static spatial kinetic structure over a
Brillouin-zone or lattice-Green surface, not yet about a full time-evolution
axiom.

The right next direction is therefore not to add a broad "Dynamics" axiom to
the foundation set. If the foundation is extended, the narrow extension should
be a law/admissible-transition principle like the candidate above. The cleaner
route for PR #4747 is to keep it as the ontology reset, then handle kinetic
nontriviality as a separate downstream target:

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

Before moving PR #4747 out of draft:

- Confirm the four-axiom baseline wording in `MINIMAL_AXIOMS_2026-06-29.md`.
- Confirm methodology docs no longer instruct agents to use the old
  three-axiom live baseline.
- Confirm the Tier-A registry description names the four-axiom
  `minimal_axioms` node.
- Decide whether a realized-kinetic-branch primitive/admission should be opened
  as a separate PR, source note, or audit campaign.
- Run and review the generated pipeline refresh after the foundation wording is
  final.
