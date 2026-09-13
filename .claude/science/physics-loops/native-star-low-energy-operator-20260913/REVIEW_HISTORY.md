# Focused author review of the complete operator extension

2026-09-13. This is the source author's review, not an independent review or
audit. No execution subagents were used. The source base remains main
cda8b1445e21b3908a0a520710e0dae57b7bc3a3. The original scalar constituent is
6e0541d4e6717c938c1bef380d0ed90a3438e228; the scalar/spectral constituent is
7b03ad8d4b160c002f0a0c9bedeba10f8eab02c7. This adds one connected operator
theorem to that same PR8086 unit. Existing parent source and cache inputs
are unchanged; the entire final chain remains pending independent review.

The complete new derivation was cold-read on the campaign branch, and the
canonical note, imports, source differences and finite comparator were read
after packaging. The final theorem is explicitly double-compressed. It
bounds P_E[O(zeta)-alpha gamma0]P_E, not the uncompressed action on P_E or
leakage into higher energy. It also does not sum the local error over the
lattice or assume that the interacting ground state has small free energy.

The real cutoff is scalar in the eight-site native cell and gives field
norm sqrt(v), not sqrt(4v). It preserves the origin/neighbor orthogonality
needed for separately Hermitian high, mixed and low defect terms. The
high-only gap follows by low-vacuum form compression, retaining the W2
scalar. All inverse families have a common self-adjoint unbounded part
and a bounded perturbation controlled on the complex disk. High parity
removes even coefficients after high-vacuum expectation. The Cauchy tail
is independently bounded by a positive Neumann coefficient majorant.

Only the linear analytic coefficient is assigned a one-low-field energy
margin; the complete inverse family is not. The finite telescoping bound
retains zeta, both placements and all inverses. The exact vacuum amplitude
is used to calibrate a field only after that coefficient is proved
Hermitian and linear. Its CAR norm isometry is then legitimate. The
compressed leading norm is attained by a vacuum/one-particle pair within
P_E. The endpoint E=0 is treated without a zero-mode operator.

The new primary executes35 operator checks and34 spectral-parent checks,
69 total with zero failures, in an envelope elapsed1.17 seconds; timeout180.
The parent call recomputes the exact Ward scalar and gap arithmetic. Counts
are predicate groups and include reused parent checks, not independent
measurements. The finite implementation has three low and four high complex
CAR modes and an explicit positive defect shift. Its frequencies and soft
weights are independent comparator choices, not a native density-of-states
sample. It tests the whole soft-Fock operator, including a three-particle
input, and preserves a nonzero unrestricted high-energy mismatch.

Three checks were added during canonical review: the scalar Neumann
majorant's cubic coefficient is compared with the convolution of two
independently recurred inverse series; the nonzero real spectral parameter
is compared with the unsplit full operator; and its derivative is checked
against direct inverses. These make the denominator multiplicity and real
spectral sign directly falsifiable. No failed mathematical predicate or
tolerance change occurred in this extension.

Ten actual source mutations failed at their intended assertions: omitted
mixed placement, omitted quadratic low field, omitted low-vacuum scalar,
wrong analytic degree, inverse derivative sign, missing last derivative,
real spectral sign, missing creation-energy margin, missing annihilation
in the Hermitian reconstruction and a single instead of paired inverse
majorant. Stored mutant sources are exactly the recorded one-edit variants;
raw outputs and source hashes are in mutations/RESULTS.json. Temporary
scripts/ execution paths preserved root/input resolution and were removed.
The earlier eighteen mutation records remain bound to unchanged sources.

All three primary caches are fresh. The new primary has14 declared inputs
and two graph-attached helpers: the spectral primary and its arithmetic
helper. No registry or dependency-policy edit was needed. The source links,
input existence, mutation hashes and graph-derived readiness checks passed.
All35 changed Python sources across the full main delta, including mutation
and recovery copies, compile. Vocabulary fix/report return zero findings;
the tool skips .claude and does not certify packet prose.

The generated manifest adds only this node and its two declared parents
relative to7b03ad8d4b:5044 nodes,12522 edges. Relative to main the full unit
adds three claims and three dependency edges. No prior node is changed or
removed. MECHANICAL_CHECKS.json records the focused results. Staged and full
branch whitespace checks are separate completion checks before and after
the commit.

This is a positive mathematical estimate with explicit supplied premises,
not a route-exhaustion or axiom-forcing conclusion. Independent source
review of the complete final unit and the exact combined current-main
pipeline, strict lint and ledger-based changed-evidence gates remain
required before landing. Formal audit is deferred by the current campaign
cadence. The author does not land this source, assign audit-owned status,
change an axiom/primitive or edit a prompt.
