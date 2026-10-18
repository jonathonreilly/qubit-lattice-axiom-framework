# Independent stationary-response implementation check

Reviewed `compass_stationary_response.py` and its `apply` implementation; did not rerun the large eigensolve. The retained full-Hamiltonian response construction has the correct signs and leading moment identities.

## Operators and local identity

In the computational convention, YY on two sites contributes −1 times the double flip and two-site Z phase. Thus the composite's +YY coefficient is −1, whereas the Hamiltonian/local energy's −YY coefficient is +1. The script uses both correctly. Its rawE is the sum of six incident Hamiltonian bonds, so dividing by two gives the central local energy for K=−1. Each term preserves the selected sector.

At this interior site, the six distinct axis neighbors give the exact operator identity

C_center = 2 e_center^2 −3 I

for J=1; generally C_center=2 e_center^2/J²−3I. Cross-axis terms cancel by central Pauli anticommutation and the opposite-neighbor same-axis terms yield C. This is an operator relation, not a linear equivalence of the two response functions; it does not imply they couple only to the same modes with proportional weights.

## Moment and acceleration formulas

For normalized real eigenvector g with energy E0, set v=(O−<O>)g and L=H−E0. The code calculates weight ||v||², centroid <v,Lv>/||v||² and variance ||Lv||²/||v||²−centroid². These are the connected source's first two spectral moments. All native reduced matrices and the eigensolver vectors are real, so `np.dot` is appropriate here. A later complex implementation must use conjugate inner products and the real part where indicated.

The initial acceleration is −<g,[H,[H,O]]g>. For real symmetric H,O this equals

−2 <Hg,H Og> +2 <Hg,O Hg>,

exactly the implemented formula. It vanishes in an exact eigenstate, independent of whether that state is the global ground state. The reported order-1e−12 value is consistent with numerical stationarity, but does not itself certify eigenpair completeness or ground-state status.

## Lanczos inverse moments

For normalized starting vector v/sqrt(weight), exact-arithmetic Lanczos gives a tridiagonal representation whose quadrature estimates the source measure. The code's quantity is

I_eta = integral lambda/(lambda²+eta²) dmu_v(lambda)
      = Re <v,(L+i eta)^−1 v>.

It is a regularized inverse moment, not a mode energy or a gap estimate. Under the usual zero-temperature ground-state retarded-response convention for perturbation −fO, the zero-frequency susceptibility with this damping corresponds to 2 I_eta, not I_eta alone. Passing eta to zero requires control of low-energy weight. A 64-step estimate with comparisons at 16 and 32 steps is a numerical diagnostic, not a certified exact susceptibility or quadrature error bound. The code uses only three-term recurrence with ground-vector removal, not full reorthogonalization; finite-precision loss of orthogonality or ghost Ritz values remains possible. Near-breakdown would also require a guard before dividing by nxt. These are scope/robustness limitations, not evidence the present run failed.

Centering removes the elastic component along g. If there are additional degenerate states at E0 with nonzero O matrix elements, their zero-frequency weight is not removed merely by subtracting <O>g. Calling ||v||² strictly inelastic therefore additionally requires exclusion of such degeneracy/weight; “connected source weight” is unconditionally accurate. The present computed next levels support numerical separation but do not constitute a certified full-spectrum exclusion.

The first three computed excitation overlaps below 1e−25 say only that those numerical eigenvectors are essentially dark for this source. They do NOT certify a spectral gap, absence of low-weight modes, completeness below any threshold, a global ground state, or a bulk particle.

## Independent small native-graph control

`/private/tmp/native-stationary-small-control.py` explicitly constructs all Pauli Kronecker matrices for an eight-site open native subgraph containing the full central six-neighbor star plus a corner. This retains nontrivial C and e spectral weights while avoiding a large solve. The exact matrix relation C=2e²−3I passes. Dense eigenbasis spectral centroids agree with source-vector formulas to floating precision; the implemented acceleration agrees with a directly formed double commutator at about 1e−14. The C source has weight 0.9760388668130273 and centroid 2.7708090519999717 in this control, so the test is not a zero-source special case. This checks operator/sign/formula correctness, not the root's 27-site numerical values independently.

The result is an honest stationary finite-open-system benchmark in a selected invariant sector. It does not derive a cosmological state, environmental coupling, or thermodynamic scalar pole.
