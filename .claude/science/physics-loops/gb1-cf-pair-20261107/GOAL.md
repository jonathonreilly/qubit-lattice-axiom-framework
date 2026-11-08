# GB1-CF: finite-register two-plaquette probe

Operation: bounded research requested by the owner on 2026-11-07. This is not
an unattended campaign and does not adopt an update law or change an axiom.

## Exact target

On two coplanar elementary squares sharing one edge, construct the s=1
five-state SU(2) quantum-link model explicitly. Determine its gauge-invariant
zero-external-charge sector, the two magnetic operators, their commutator,
and whether an ordered or joint update respects the square-exchange symmetry.
Test the construction at finite register size, without using a rotor limit.

Then distinguish the exact finite-patch qubit encoding from the unproved
homogeneous cubic-lattice implementation and compatibility with Admissibility
and permanent Record. A mathematical model is not a law selected by the axioms.

## Model and sources

- Main authority: f5af11cd0102cfd0b51aef0911f600130bf5beb1.
- Assembly context: fb9508e8390bf66da8f29ddb44611d2a531768cb, PR #10139.
- `GB1QL.md` sections 1.1-1.3 define the finite family; derive s=1 directly.
- `GB1ISO_REFEREE.md` section 2.3 keeps GB1-CF open: finite-register
  full-plaquette form, covariance, and nearest-neighbor implementation.
- Chandrasekharan and Wiese, hep-lat/9609042, provide the quantum-link context.
  No continuum theorem from that paper is a premise of this calculation.

## Allowed premises and limits

The mathematical test model has one five-state factor per oriented link.
The physical baseline remains Lattice, Qubit, Admissibility, Record, and the
three registered primitives. The model's factors, SU(2) action, zero external
charge sector, and update choices are supplied construction data, not derived
physical premises. A three-qubit code for a link is a finite encoding; it is
not yet a homogeneous allocation of physical site qubits.

No five-mode site, independent physical link register, selected vacuum,
continuum limit, mass gap, Born rule, or record evolution may be silently added.

## Completion witness for this probe

Exact formulas with a reproducible sparse or reduced-space computation and a
separate derivation checking the load-bearing coefficients, sector dimension,
and symmetry conclusion. Preserve counterexamples and failed constructions.
Numerical spectra or a finite list of zero commutators do not by themselves
prove lattice-wide covariance or the full Yang-Mills bridge.

## Delivery

One scoped note/runner pair at a coherent milestone, with exact source and
execution identities and independent-check limits. No main edits or audit
verdicts. The supervising session owns integration and any commit/push/PR.
