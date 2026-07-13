# Route Portfolio

The dramatic-step score is `0..3`; risk is subtractive.  All routes were
evaluated from `A_min`, not from the accepted numerical branch.

| Route | Type | Upgrade | Trace | Import retirement | Review closure | Artifactability | Hard pressure | Risk | Total | Disposition |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R1: derive the exact kernel directly from axioms | constructive theorem | 3 | 3 | 3 | 3 | 1 | 3 | -3 | 13 | blocked: axioms explicitly supply no dynamics/source/readout |
| R2: use the bare Ward ratio to fix transport | atlas reuse | 2 | 2 | 1 | 1 | 2 | 2 | -3 | 7 | pruned: algebraic ratio does not select a transport operator |
| R3: exact Schur/Feshbach normal form | constructive theorem | 2 | 2 | 1 | 2 | 2 | 2 | -2 | 9 | pruned: exact reduction is conditional on a supplied operator |
| R4: rearrangement derivation | constructive theorem | 2 | 2 | 1 | 2 | 2 | 2 | -3 | 8 | pruned: assumes an accepted positive kernel/background |
| R5: variational selector | selector/chamber | 2 | 2 | 1 | 2 | 2 | 2 | -3 | 8 | pruned: assumes the missing local quadratic selector |
| R6: scalar affine-remainder theorem | constructive theorem | 2 | 2 | 2 | 2 | 3 | 3 | -1 | 13 | open PR #5179 partially closes scalar mathematics; physical identification open |
| R7: exact axiom-compatible countermodel | no-go/obstruction | 2 | 2 | 3 | 3 | 3 | 3 | 0 | 16 | selected as negative route pruning |

## Stuck fan-out synthesis

The seven frames agree on one wall: the current axiom surface does not identify
a physical dynamics or endpoint observable.  R2-R6 can become physically
load-bearing only after such a packet exists.  R7 changes claim state narrowly:
it constructs an allowed non-affine kernel and an equal-moment profile pair
with unequal first-order responses, proving bare-foundation non-entailment
without target calibration while leaving the physical claim open.

The best remaining positive attack is therefore sharply isolated: derive the
microscopic dynamics/source/readout packet, then prove its response functional
annihilates every zero-zeroth/zero-first-moment perturbation.
