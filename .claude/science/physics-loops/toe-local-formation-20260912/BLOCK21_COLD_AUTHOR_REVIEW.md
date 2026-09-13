# Complete-instrument precision: author review

The coherent isometry overlap gives an upper bound after outcome dephasing.
A balanced input between both B eigenspaces saturates it separately in each
classical block; identical native intertwiners preserve those norms. Thus
the equality concerns the complete flagged instrument, not merely its
nonselective channel or the outcome probabilities. Both eigenspaces must
be present for saturation. Finite code dimensions and the full diamond-norm
convention are explicit. Watrous Theorem3.51 and its proof were checked
for the required Hermitian-preserving finite-space hypothesis.

Adaptive telescoping requires shared observables, code maps, labels, dwell
and controller structure, with a bound at every prior classical history.
The histories are classical; dephasing any off-diagonal history blocks is
a common contraction. There is no bound claimed for separately normalized
rare-branch states. Contrast precision is at worst square-root near1 but
angle precision is Lipschitz; this does not show generic noise robustness
or supply the missing physical program decoder.

The proof preceded an exact two-sector matrix comparator. Its50 checks
pass in0.196seconds: channel completeness, coherent overlaps, separate
flag-block singular values, balanced outcome probabilities and projective
endpoint saturation. The comparator checks finite representatives, not all
adaptive histories or the native spatial embedding. No predicate failed
and no tolerance was used. The initial file-creation patch had a missing
patch prefix and was rejected without writing a file; it was reapplied
with the same intended proof. No independent review or new source PR.
