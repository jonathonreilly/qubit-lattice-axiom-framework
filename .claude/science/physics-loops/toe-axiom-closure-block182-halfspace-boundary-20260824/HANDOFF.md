# Handoff

Block 182 completed the selected endpoint/metric decision. At the supplied
reflected action and `k=(pi/2,0,0)`, the polynomial descriptor has seven zero,
fourteen finite-nonzero, and seven infinite generalized eigenvalues. Both
endpoint staircases have partial multiplicities `(3,1,1,1,1)`, and the scalar
TT numerator has support `-6..6` against denominator support `-7..7`; endpoint
chains are not poles of the TT response.

The stable scalar response is minimal on three real modes with weights
`(+1.51761e-4,-2.17451e-4,+0.581884812)`. The equations
`H A=A^T H`, `H b=c` uniquely force `H=diag(weights)`, so no positive
OS/self-adjoint realization preserves that exact response at one or two
steps. Direct moments and Hankel determinants agree.

Crucially, positivity alone survives: the dispatcher and an independent
refuter constructed `H_c>0` with `H_c b=c` and
`H_c-A^T H_c A>0`, but `H_c A != A^T H_c`. The scientific fork is now
OS/self-adjoint boundary repair versus a physically justified unitary/open
dilation—not “gravity cannot be positive.”

Next action: derive the palindromic descriptor boundary concomitant and a
reflection-real stable/unstable intertwiner, transporting the Ward source and
TT/Record readout explicitly. Compare it with a minimal unitary dilation of
the positive contraction. Do not select roots by hand and do not amend axioms
from this one probe.

Validation is clean for the primary runner, seven mutations, fresh cache,
vocabulary, deterministic citation manifest, strict audit lint, and local
diff scope. The full pipeline stops at the same inherited policy-v2
dependency-epoch mismatch recorded by parent PR #7338; current `origin/main`
contains the reviewed v3 repair. Do not copy that owner-governed audit-policy
change into this gravity block. Land #7338 and its transitive stack first,
then incorporate current main before landing this child. Independent audit is
still required.
