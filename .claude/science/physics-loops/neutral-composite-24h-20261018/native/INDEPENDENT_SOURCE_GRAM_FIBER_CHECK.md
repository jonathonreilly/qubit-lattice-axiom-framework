# Adversarial source-Gram and momentum-fiber check

The added arguments can close the previously identified source/fiber gaps, but three details should be made explicit: the source vector, rather than the centered operator itself, starts at order lambda; finite cat factorization requires a proper UNION of supports; and the scaled O(lambda²) fiber error requires evenness of D2 around pi, not merely bounded first derivatives. None requires an added physical premise beyond the stated invariant observable, prepared vacuum and equivariant local normal form.

## Source vector versus operator

The original centered diagonal readout O_j-c0 I annihilates every uniform vacuum, but is generally a NONZERO operator at lambda0. Therefore “its quasilocal interaction expansion begins at lambda” is false if read literally as the operator expansion of the centered dressed readout.

Define instead

A_j(lambda)=Y O_j Y†-O_j-<Y O_j Y†-O_j>_vac I.

Its action on the vacuum equals that of the centered dressed source, because (O_j-c0 I)|vac>=0. This replacement genuinely starts at order lambda in the quasilocal observable norm. Local conjugation and Cauchy estimates give a uniform anchored expansion A_j=lambda A_j^(1)+R_j with ||R_j||_anchored,mu=O(lambda²), using a slight decay loss if needed. This is the right object for the Gram argument. The finite-state mean can be taken in any uniform color because invariance makes it independent of color.

Each local term may be centered separately by subtracting its same-color vacuum mean. The color-invariant local decomposition follows by symmetry averaging the generator/readout commutator pieces; conjugating by a global monomial plane symmetry does not enlarge a local support. The same construction applies to the second-order remainder.

## Product and cat Gram kernels

For a product uniform vacuum, disjoint centered local terms have exactly zero covariance. For the symmetric cat, their diagonal contributions in each color factorize and have the same vanishing means. Off-diagonal color contributions vanish whenever the UNION of their supports omits at least one rung. Individual properness alone is not sufficient: two disjoint large intervals whose union covers the whole ring can together connect two uniform vacua.

This finite-ring qualification is harmless if handled rather than omitted. In the infinite local cat state (equivalently its mixture for finite-support observations), every finite union is proper and the factorization is exact. On a finite ring, covariance terms whose union covers it require large supports; exponential dressing tails suppress them exponentially in circumference. Their contribution summed over relative translations remains uniformly bounded, and tends to zero for large rings. State that tail step explicitly, or formulate the infinite Gram estimate first and then bound finite-ring corrections.

In an anchored exponential decomposition, nonzero covariance at separation r requires overlapping supports or the finite-ring covering exception. The local coefficients have total size O(lambda), so overlap estimates yield |G(r)|<=C lambda² exp(-mu' distance(r,0)), with a possible polynomial absorbed by reducing mu'. The finite-ring covering terms admit the same type of summable control. Thus sum_r|G(r)|<=C lambda² is justified. Repeating with the O(lambda²) anchored remainder gives sum_r|G_R(r)|<=C lambda^4 and normalized-packet remainder vector norm O(lambda²).

Translation invariance of the chosen product vacuum or symmetric cat then identifies the Gram operator as a convolution. Its Fourier multiplier is bounded pointwise by the l1 kernel norm. This stronger fact, not only a bound on the total packet norm, controls the outside-window signal by C lambda² times the packet's Fourier tail. It supplies the missing O(lambda²) per-momentum upper bound. Translation covariance and consistent centering must be retained throughout.

## Infinite-separation fiber and derivatives

A fixed-order N-conserving local term, after vacuum subtraction, acts only near walls. Its finite support bounds wall displacement and color changes. In an infinite oriented interval/separation basis, each matrix element therefore contains only bounded center-of-mass translation phases. The number and norm of outgoing transitions are bounded at fixed order, uniformly in separation. Termwise row/column estimates then also bound any fixed number of momentum derivatives: differentiation multiplies phases by bounded displacement powers.

The earlier 8a_k operator bound alone does not imply derivative bounds, but locality/displacement and the finite-order support bound do. One may use a coarse range-dependent row bound here; its constants may grow rapidly with order without compromising a fixed-order theorem.

Formulate these derivatives in the infinite fiber, not by differentiating finite-ring terminal-fold identifications with phases exp(iqL/2). Finite ring momenta are discrete and the terminal orbit changes with their parity. The existing explicit basis resolves these finite folds, but it is not itself a smooth-in-q uniform finite-ring gauge.

## Required parity refinement for the scaled error

Bounded first derivatives and D_odd(pi)=0 give the needed estimate for D3, but by themselves only give D2(pi+delta)-D2(pi)=O(delta). That would produce O(lambda), not O(lambda²), in the scaled crossover operator. The stronger conclusion follows from the available symmetries:

1. Checkerboard Q commutes with N and maps lambda to -lambda, so Q D_k(q) Q=(-1)^k D_k(q).
2. In the centered interval basis, physical longitudinal reflection maps q to -q. Comparing pi+delta with pi-delta involves the2pi gauge factor (-1)^(ell-1), which equals -Q on the complete scalar edge/even-diagonal space.
3. Thus D_k(pi+delta)=(-1)^k D_k(pi-delta) in that fixed infinite-fiber gauge.

Even coefficients are even about pi and odd coefficients are odd. In particular D2 has vanishing first derivative, while D1 has a cubic remainder after its linear term. For q=pi-lambda*kappa and bounded kappa, the contributions are

lambda D1 = lambda² M_nearest(kappa)+O(lambda4),
lambda² D2 = lambda² D2(pi)+O(lambda4),
lambda³ D3 = O(lambda4),
remaining retained orders = O(lambda4).

After dividing by lambda² this gives the claimed uniform O(lambda²) error. Uniform derivative bounds through the necessary orders are supplied by finite-range wall displacement as above. This parity argument should be written explicitly in the note; the present first-derivative sentence does not on its own prove the stated order.

## Eigenprojection, finite limits and signal

An operator-norm O(lambda²) perturbation of the infinite crossover fiber, uniformly for kappa tending to zero, preserves the isolated upper eigenprojection and its source overlap. Combined with the Gram bound and the sine-packet tail, this yields the stated (15/4+o(1))lambda² normal-form packet mode contribution, once the leading source formula is verified in the same centered gauge.

Finite rings do not converge to a half-line in global operator norm merely because they grow. The useful statement is convergence of the source-local spectral projection/measure: truncate the localized boundary eigenvector, control its exponentially small tail, and use the uniform isolated gap or a local resolvent argument. Far-terminal states or their degeneracies should not be mistaken for failure or proof of this local convergence. The same reasoning must include the packet's discrete momentum approximation and require the cutoff to grow sufficiently fast. Choosing L much larger than lambda^-2 is compatible with the packet and dynamical scales, but is a specified limit, not automatic from a fixed-L run.

These refinements support a finite-order normal-form signal and its prepared-state finite-time transfer. They do not select an exact-H ground state, turn the nonstationary exact correlator into a positive equilibrium spectral measure, or establish an infinite-time native pole. The existing note retains those limits correctly.

## Follow-up: fixes verified in current note

I reread the canonical note after the parent's update. It now explicitly uses [Y O_j Y†-O_j] centered, handles proper unions and exponentially small finite-ring covering tails, and obtains the scaled error from the explicit K2 cos(q) dependence. These changes resolve the three issues identified above. The explicit K2 dependence gives its quadratic variation without requiring the more general all-even-coefficient parity proof. Together with K1's cubic Taylor remainder, D3's vanishing at pi and bounded derivative, and bounded higher coefficients, it suffices for the stated O(lambda²) scaled error.

The newly included first-order source check also works directly: a single transverse rung flip changes two of O_j's four longitudinal pair terms when at either endpoint j or j+2, reducing O_j by4. S1 maps the uniform vacuum into the energy8 sector with coefficient1/8. Hence [S1,O_j]|vac>=(h_j+h_(j+2))|vac>/2. Orthogonal distinct-rung flip states and ||h_j vac||²=4 give the exact leading Gram kernel2delta_0+delta_2+delta_-2 and Fourier multiplier4cos²q. A harmless center-phase convention affects the amplitude phase but not this multiplier or the mode weight. This supplies the previously conditional leading source normalization.

The remaining finite-fiber/half-line convergence and locality arguments are mathematical steps, not numerical certificates. Keep them explicit as described above; the applied refinements do not remove the prepared-state, finite-order and no-exact-pole qualifications.
