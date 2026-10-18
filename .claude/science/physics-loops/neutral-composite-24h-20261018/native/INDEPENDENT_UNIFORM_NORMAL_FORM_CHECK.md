# Focused check: wall projector estimate and explicit local BCH remainder

The updated quadratic projector argument is correct with the Hermiticity and proper-support assumptions made explicit. A straightforward weighted interaction estimate supplies the requested fixed-order, volume-independent BCH remainder. This report does not edit the root draft or certify its downstream infinite-volume mode interpretation.

## 1. Projector support identity

Decompose each D_k into Hermitian local terms d_I that individually commute with N and are individually invariant under the global plane color transformations. Such a decomposition can be obtained by Hermitian grouping, termwise N averaging and finite-group color averaging; these operations preserve locality up to the stated N-filter support enlargement. Translation covariance can be retained by treating all translates identically.

Let w_b=1_{n_b>0}, and Q_I=1-prod_(b touching I)(1-w_b). For a computational configuration with Q_I=0, every rung in I and each neighboring exterior rung has the same color. A change supported in I leaves every other bond unchanged. Since all touched bonds initially have zero N, any nonuniform final configuration increases N. Conservation therefore prohibits it. The only zero-cost final configuration is the identical uniform color, provided I is a proper subset of the ring. Thus d_I acts as a scalar c_I on this local-uniform subspace. Plane-color transitivity makes c_I independent of the uniform color; locality makes it independent of the exterior configuration.

Consequently d'_I=d_I-c_I I annihilates (1-Q_I). Hermiticity gives annihilation on the left too, so

d'_I=Q_I d'_I Q_I,
||d'_I||<=2||d_I||.

The proper-support condition matters: a term supported on the whole ring could change one uniform vacuum into another without creating a wall. The retained finite-order ranges must therefore be smaller than L, as the draft assumes. No statement about exact quasilocal remainder terms is implied by this finite-range support identity.

Because all wall projectors are diagonal and Q_I<=sum_(b touching I)w_b,

sum_I ||d_I|| Q_I <= sum_b w_b sum_(I touching b)||d_I||
                    <=2 a_k sum_b w_b,

a_k=sup_x sum_(I containing x)||d_I||.

For a normalized vector in a fixed-W wall subspace, the quadratic form of sum d'_I has absolute value at most4 a_k W. Each term preserves N, so the restricted total is self-adjoint. In the periodic N=2 sector there are exactly two distance-two walls, giving

||D_k-E_vac,k||_(N=2)<=8 a_k.

This is a valid operator bound even for coherent superpositions of wall positions. It does not require a matrix row-count estimate. Periodic/equal-asymptotic boundaries remain necessary for identifying N=2 with exactly two such walls.

## 2. Explicit interaction-norm commutator bound

For interval interactions define

||A||_mu=sup_x sum_(I containing x) exp(mu |I|)||A_I||,

using a chosen local decomposition, with mu>=0. This is an interaction norm, not the global operator norm of sum A_I. Use the ordinary commutator decomposition with term [A_I,B_J] supported on I union J for overlapping intervals; disjoint terms vanish.

For 0<=mu'<mu and delta=mu-mu', split the condition x in I union J into x in I or x in J. The operator commutator contributes factor2, and the sum over J intersecting I is bounded by |I| times the per-site interaction norm. Using |I| exp(-delta |I|)<=1/delta gives

||[A,B]||_mu' <= (4/delta)||A||_mu ||B||_mu.

This bound is independent of ring circumference. Overcounting terms or unions is harmless. It also works for complex interactions, needed below for analytic lambda estimates.

For the m-fold nested commutator, divide the total decay loss delta into m equal parts. Monotonicity of the norm in mu and repeated application give

||ad_S^m(A)||_mu' <= (4m/delta)^m ||S||_mu^m ||A||_mu.

Since m!>=(m/e)^m,

||ad_S^m(A)/m!||_mu' <= [4e||S||_mu/delta]^m ||A||_mu.

Hence the exact BCH interaction series converges absolutely whenever r=4e||S||_mu/delta<1, and

||exp(ad_S)A||_mu' <= ||A||_mu/(1-r).

At each finite volume the series equals ordinary unitary conjugation for real anti-Hermitian S; absolute convergence in the interaction norm makes this equality uniform in volume. The resulting interaction is generally quasilocal, not finite range. This elementary small-generator bound suffices at fixed order; it is not an optimal high-order prethermal estimate.

## 3. Finite-product normal form and a uniform Taylor remainder

Suppose the recursive construction has produced finite-range, volume-uniform S_1,...,S_n, independent of lambda, and choose total decay loss Delta=mu-mu'>0. Allocate delta=Delta/n to each conjugation in the product. Let s_k=||S_k||_mu. Choose a fixed rho>0, for example rho<=1 satisfying

rho^k s_k <= Delta/(8 e n) for every k with s_k nonzero.

Then every exp(ad_(lambda^k S_k)) has r<=1/2 for complex |lambda|<=rho. Successive applications give the analytic transformed interaction G(lambda) in the final norm mu', bounded by

M=2^n (||4N||_mu+rho||V||_mu).

All constants are independent of volume. Since the construction cancels the off-diagonal terms through order n, the first n Taylor coefficients of G are exactly the retained D_k (with zeroth term4N). Banach-valued Cauchy estimates give, for |lambda|<=rho/2,

||G(lambda)-4N-sum_(k=1..n)lambda^k D_k||_mu'
 <=2 M rho^(-(n+1)) |lambda|^(n+1).

Thus C_n=2M rho^(-(n+1)) is one explicit, deliberately loose fixed-order remainder constant. This proves the desired form of the interaction-norm remainder PROVIDED the finite-range generators and their uniform norm bounds have been constructed. It does not require a global spectral gap between the many-body N sectors of the perturbed H, and never uses ||S||global=O(L).

The constants can deteriorate rapidly with n, mu and chosen range bounds. No exponential lifetime or optimal order should be inferred. The draft's integer-gap local filters make the induction plausible: a finite collection of connected commutators and bounded P/T operations at each fixed order supplies finite s_k. The claimed numerical range bound4k-1 should be proved by its own support induction if retained as a precise assertion; the BCH result only requires a finite order-dependent range.

## 4. Remaining downstream qualifications

The normal form retains exact symmetries if generators are chosen equivariantly. Its D_k are finite range and N-conserving; the remainder is quasilocal and need not conserve N. The wall projector estimate therefore applies directly to retained coefficients, not automatically to all remainder dynamics restricted to N=2.

The updated draft correctly separates the dressed prepared vacuum from an exact-H stationary ground state, local LR control from momentum-summed response, and absolute order-five errors from relative visibility of an O(lambda²) signal. Those qualifications should remain. A uniform finite-order interaction bound is genuine progress, but passage to half-line momentum fibers, simultaneous finite-size limits and near-threshold bound states still needs the stated separate control. No exact native pole or physical scalar conclusion follows from this estimate alone.

## Follow-up: finite-packet scaling

For translates of a fixed local observable O_j, let A_f=sum_j f_j O_j with sum|f_j|²=1 and support on at most M sites. Then sum|f_j|<=sqrt(M), ||A_f||<=sqrt(M)||O||, and the local evolution comparison sums to ||A_f^G(t)-A_f^D(t)||<=sqrt(M) C lambda^(n+1)(1+|t|)². Multiplication by the other packet operator in a correlation adds at most another sqrt(M), so the stated correlation-error bound C M lambda^(n+1)(1+|t|)² is valid. The same triangle argument handles connected subtraction with an adjusted constant and consistently transformed states/observables.

At t of order lambda^-2, n=7 gives a local error of order lambda^4. Taking M of order lambda^-3/2 yields total error O(lambda^(5/2)), which is smaller than an O(lambda²) packet signal. A smooth envelope of spatial width M has typical momentum width O(1/M)=O(lambda^(3/2)), smaller than the O(lambda) crossover window. Compact support alone does not guarantee a sharp single-momentum profile; the envelope and its Fourier leakage need specifying.

This establishes an absolute-error scaling compatible with visibility, not the mode weight itself. One must separately bound the packet's overlap/residue in D from below, control spectral/dispersion variation across its momentum envelope, and keep observable truncation errors smaller than the same target. For comparison with infinite-line dynamics, a finite ring must accommodate both the packet and the relevant Lieb-Robinson cone; L much larger than lambda^-2 is a sufficient conservative choice for the stated times. The uniform finite-ring estimate itself is not invalidated by wrapping, but infinite-line interpretation would need an explicit wrap-error control.
