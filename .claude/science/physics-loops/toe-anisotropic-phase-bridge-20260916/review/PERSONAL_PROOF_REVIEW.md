# Personal review of the compact-Hamiltonian derivations

This is an author review, not an independent review. The eight current
notes and primary finite programs were reread, including their assumptions,
normalizations and comparisons. The preserved attempt-to-current diffs
were inspected. Main is e0ef7cf4633034a8c1e6d57f5812cc4275bf1349 and the
standing instruction snapshot is068e916ca37b004757ad3a3c082857a91dc37215.

The weighted conditional exponent contains one half. Hodge duality swaps
temporal and spatial plaquettes. The integer Bernoulli/Poisson comparison
uses L1 distance, not the half-sized total-variation convention; its variance
estimate is separate. Quadratic killing couples jumps and produces only a
finite-graph Trotter conclusion from the extensive norm error. The endpoint
amplitude identity retains both boundary factors and is not an equality of
the two transfer operators.

The electric source is an offset of the kinetic term, not a Wilson flux.
The sum rule and inverse spectral moment agree with the phase-corrector
normalization. The physical quotient metric and longitudinal/harmonic
exceptions are explicit. A vanishing lower-bound certificate cannot give
an upper bound on the response. The local-density proof cancels the global
ground energy before taking heat-kernel extrema. Haar orthogonality is
applied to distinct link characters, not independent plaquette variables.
The cube witness and local event floor retain the nonlinear principal map.

In the quantum comparison, the half-angle map is a finite cover. The pulled
back product ground state is strictly positive on the whole covering torus,
so ground-state uniqueness justifies its use there. This does not identify
the full thermal trace; a separate check exposes that error. The momentum
transpose changes sign in the second Hilbert-Schmidt factor, making the
electric-square difference cone positive. Finite Fourier truncation of this
insertion and elliptic graph-norm regularity justify its domain. Only equal-
time angle and electric quadratic moments are ordered; no susceptibility
comparison is inferred. Directed free-box inclusion yields cofinal angle
limits, not uniqueness under arbitrary boundaries or all quantum observables.

The raw-curl source witness lives in an actual free square and all its
nonzero link angles are strictly interior. Its compact plaquette action
vanishes while its raw quadratic curl does not. The positive replacement
constant retains m dependence; the source's entire proof is not repaired.

For the Wilson mixture, the Bessel bridge conditions on radius, so the
endpoint planar angle must first be sampled. The centered bridge is then
independent. Normalized Wilson and Villain factors have matching Fourier
coefficients and an absolutely summable envelope. The positive partition
sum is decreasing in every auxiliary variance; product association has the
correct sign, including when the partition function is unbounded. Classical
integer-character Ginibre plus circle convolution supplies Villain
monotonicity. The diluted bound is therefore for compact characters. The
auxiliary variance's infinite mean prevents identifying its unwrapped normal
with a finite-variance physical field. No vertex-spin phase theorem is used.

For the actual Hamiltonian bridge, temporal Dirichlet precision dominates
negative cosine curvature at short T uniformly in volume. Sine-mode cutoff
bounds use the exact continuum temporal spectrum. The continuum positive
Green kernel is used only after cutoff passage in the mean identity.
Endpoint Hessians include the negative covariance term. In the spatial
locality argument, the scalar path diffusion preserves vector-component
labels even though its coefficients depend on all paths; the cosine
Hessian alone moves those labels. The Neumann-series support argument is
therefore applicable. The extensive constant F_T(0,0), compact winding sum,
endpoint nonconvexity and remaining long-time task are all retained.

A manual source review caught an important verification defect: the first
bridge check called a finite image sum an infinite-winding bound. Its
assertions had passed. The current geometric majorant bounds the entire
sum, and both versions remain in the record. This is why a PASS string
alone is not treated as evidence of the theorem's full correctness.

The formulas survived the selected independent constructions and23 final
formula-fault challenges. Those are finite author checks; not every proof
step has a second implementation, and no spatial phase was computed. The
next substantive work should address the actual compact endpoint/winding
law. Formal registration, N-packet submission where applicable, independent
review and integrated landing validation remain pending.
