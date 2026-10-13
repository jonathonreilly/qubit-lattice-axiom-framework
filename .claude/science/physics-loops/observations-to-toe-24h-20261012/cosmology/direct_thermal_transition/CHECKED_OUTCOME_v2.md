# Direct thermal transition: checked outcome

The prescribed three-field action has been evolved through the finite-temperature
electron-pair transition in its x=0, radiation-only sector. This is a conditional
fluid calculation, not an abundance measurement or a fit of the early universe.
All field constants and initial data were supplied before each execution.

The two branches differ. At k=1e-5, b=a gives sampled H_J/H_GR between
1.09886284 and1.11803063; calibrated b=k gives0.99999979247 to1.00000018788.
The comparator uses the same specified fluids and reference Newton constant.
These are extrema on supplied sample sites. The neutrino temperature ratio
0.71393016904494 follows the finite initial Ti=10 electron masses and differs
from the infinite-temperature entropy approximation. Three massless, already
decoupled neutrino pairs remain an assumption of this block.

Parent v1 ran13573 checks with no reported failure, but independent mutation
testing found a real gap: removing the physical-clock velocity factor from
H_J passed all those controls. Its actual changed readout reached0.000283275
in the tested thermal cases. Version2 adds a separate raw-action/proper-clock
oracle, generic nonzero-velocity fixtures and full serialized-readout checks.
It executes29986/0 while all five original scientific sections and13564 old
non-source assertion objects stay exactly unchanged. The same one-line
mutation now fails1216 scientific checks with all12 fresh input identities
passing; the original successful mutation remains preserved.

The complete independent numerical review uses Bessel sums and separately
scaled quadrature for the EOS, algebraic entropy and a different
temperature-clock covariant-momentum evolution. It reproduces every original
history and all2020 sample sites within its fixed2e-6 comparison bound.
All12 independent integrations completed. Its later affected-source check
reports49593 record/numerical checks with zero failures. The full reports and
methods were read by the parent, with215 original and128 affected unique
source/recovery/evidence identities verified, including each final receipt.
The separate handwritten check supplies62 mathematical controls and17 parent
identity verifications. Counts describe different checks, not independent
physical experiments.

Two limitations remain visible. Six reviewer tests of a stronger relative
accuracy requirement for tiny unscaled traces failed; the parent's actual
criterion applies to temperature-scaled quantities and passed. The same two
SciPy finite-difference Jacobian warnings persist. A separately reproduced
passive-coordinate mechanism and the independent DOP853 evolution assess
their scope; the original warning events were not instrumented. Neither
failure record was deleted or relabelled as a successful original check.

This sector omits nonzero conserved dust, massive-neutrino trace evolution,
neutrino collisions, nuclear reactions and abundances. It does not establish
that the thermal solution reaches the late ideal dust family. The next parent
block directly tests that missing connection with both tracking fields active.
