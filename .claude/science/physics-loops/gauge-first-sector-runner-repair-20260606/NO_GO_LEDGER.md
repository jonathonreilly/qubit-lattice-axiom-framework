# No-Go Ledger

## Rank-One Exact Diagonal Factorization

The rank-one transfer `T_min` exactly realizes `Z_min`, but it is not itself a
diagonal Wilson half-slice factorization of the form
`T = exp(3J) D exp(3J)`.

Reason: `exp(3J)` is invertible.  Therefore any such representation has a
unique pullback `D_back = M^-1 T_min M^-1`.  The restored runner computes
`||offdiag(D_back)||_F = 0.250338180104`, so the unique pullback is not
diagonal.

## Overclaim Avoided

The restored runner does not claim that no other transfer realization exists.
The current helper stack already contains a positive rank-one realization.
This boundary is only about the diagonal Wilson factorized-class subfamily for
that exact rank-one transfer.
