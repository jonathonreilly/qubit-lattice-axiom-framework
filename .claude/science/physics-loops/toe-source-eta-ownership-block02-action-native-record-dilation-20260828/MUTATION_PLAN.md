# Mutation Plan

Mutations must reject: dropping one POVM branch; changing a Kraus amplitude;
using a noninvariant blank; replacing a covariant post-state by a fixed frame;
merging two outcome codes; calling positive overlap orthogonality; erasing the
24-orbit; adding an orbit lookup; treating center/two-shell data as six
neighbors; fitting polynomial coefficients after H1; using adjoint instead of
actual reverse; changing any 110-term source; using `p/q`; suppressing a
second probability law; and claiming H2, axiom, retained, obligation, or TOE
closure.

The independent checker must rebuild the group, orbit histograms, code Gram
matrix, completeness blocks, polynomial constraints, and source/probability
image without importing primary result flags.

Executed result: the primary runner passes 11/11 checks and rejects 33/33
mutations; the independent checker passes 12/12 and rejects 25/25.  Mutations
cover group closure, cocycle rank/class count, stabilizer matching, ANF degree
and covariance, carrier injectivity/covariance, POVM and Kraus completeness,
QND locking, overlap, sharpness nonselection, branch/source collision, exact
110/110 source equality, cache identity, and claim-scope sentinels.
