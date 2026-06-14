# Handoff

This PR repairs the chiral-body N2 source scope.

N2 now says scalar doublet block only for `C3`-equivariant
real-symmetric/Hermitian mass operators. It separately records that
`J_cs=(C-C^2)/sqrt3` is `C3`-equivariant and commutes with `Gamma_chi`, but is
the non-scalar real antisymmetric complex structure on the doublet plane, not
a real-symmetric/Hermitian mass operator and not a source for a real doublet
direction `h`.

The runner now checks these source statements and the cache is refreshed to
`SCORECARD: PASS=39 FAIL=0`.

No audit ledger rows, publication matrices, lane registries, or status boards
are edited here. Independent audit owns any status change.
