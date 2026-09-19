# formation-in-3plus1, attempt 3 (worker w-macbookpro90c72-jb4a1, model grok-4.6)

Own plan: the L=2 return sum and the continuum prefactor from `det M`. a2 treated `A/κ` and `G_4`; a4 the Green form; this is `G_2=25/24` and `1/(4π√(det M))=4/π`.

## (1) The statement attempted

**Statement (PARTIAL).** For `φ=(1+∑ e^{-ik_j})/4`, `G_2=25/24` exactly (`1-|φ|²∈{3/4,1}` on the seven nonzero modes of `(Z/2)^3`). The small-k metric `M` of `1-|φ|²=k^T M k+O(k^4)` has `det M=1/256` and eigenvalues `1/16` (once), `1/4` (twice). The continuum equal-level covariance is
`σ²/(4π √(det M) √(x^T M^{-1} x)) = (4σ²/π)/√(x^T M^{-1} x)`,
a 1/r law in the plane metric `M`. The causal response is a forward-cone multinomial, not this kernel. Sphere LRO is not proved.

## (2) Steps

**Step 1 — `G_2` (CHECKED).** Cosine form on `L=2`.

**Step 2 — `det M` (PROVED; CHECKED).** Hessian `H` at 0 as in a2; `M=H/2`; `det` and eigensystem.

**Step 3 — prefactor (PROVED; CHECKED).** `√(det M)=1/16`, `1/(4π×1/16)=4/π`. Fourier of `1/(k^T M k)` on `R³` ASSUMED at the usual scope.

**Step 4 — cone (PROVED).** Backward predecessors send influence only into the future cone.

## (3) Where the route stops

LRO (a) is not proved. (b) is the linear continuum form, not two-sided nonlinear bounds.

## (4) What would finish it

Domination of the sphere by the linear kernel at large `β`, plus the `A/κ` lemma of a2.
