The 4-by-1-by-1-by-1 complex check was interrupted after over three CPU
minutes. The returned traceback identified `Q.rank()` inside
`complex_matrices`, in SymPy's rational row reduction and integer gcd.
Exit code 130, KeyboardInterrupt. No assertion failure was returned.

The exact idempotence check had already passed. Rank of an idempotent is
its trace, so the replacement checks `trace(Q) == rank(B) == faces-rank(D)`.
It preserves the mathematical rank assertion without the redundant dense
rational elimination. The frozen source and its SHA256 are alongside this
record. This is an execution-efficiency correction, not physical evidence.
