# Focused independent check of the actual-carrier Neumann lower theorem

No material error found in the complete frozen REPORT a837bb64fe72a88a8913fa9c5f181f516a4ec45dc91733bbeb9e27d3d789ca6c. The new lower coefficient, finite-volume error, grand-energy/density consequences, separate cell gap and narrowly stated template counterexample follow under their supplied-model hypotheses. This is a focused discovery check, not formal review/audit or an exact EOS/phase result.

Root PRE71c4d9ecaf0dfa97cf50b17435be79b98b73ddb08cc8d7bf118b58cdff6d7f52 was frozen after reading CONTRACT and before opening author derivation/report/code. It disclosed the author's target coefficient and scales. It reconstructed the Neumann mean/variance argument, literal removal normalization, translated particle loss and scale balance. Root then read all420 lines of the released proof, checked the affected premises against earlier complete checks, and wrote a new finite control without reading/importing the author implementation. The independent PRE proposed a heat-kernel route; the author's different smooth-Fourier-cutoff proof of the same uniform Green estimate was checked in full.

## Actual physical premise and boundary handling

The full positive decomposition H0=S+mu D+W, the fifteen-gradient inequality and the previously checked B_R bound retain all hard-core occupation sectors. Passing to nine forward fields drops the duplicate plane-gradient copy and translates the axial anchors, preserving the lower direction. An occupied residual site pins all nine forward amplitudes. No many-pair Fock identification or background gap is used.

The proof partitions only positive gradient rows. It never deletes neighbors from D(m), whose nonmonotonicity really does defeat that naive boundary operation: one isolated dimer has D=0 and its two deleted-neighbor vertices have D=2. Bonds may extend beyond their anchor cells; the argument does not require independent physical Hilbert spaces per cell.

The premise B_R bound needs R>=10,L>=10R. The final theorem imposes ell>=3R and L>=4ell, which suffices. The earlier draft condition was narrowed before release; the claimed small-density scales meet it. Its huge universal constants only make the eventual density threshold small; they do not depend on mu,tau except through a=min(tau,mu/12).

## Uniform Neumann Green estimate

The scalar symbol is exactly ell(k)=4sum sin²(k_i/2), and the form sums each positive axial edge once. Its Green diagonal is therefore the same g used in the earlier single-pin normalization. The dyadic annulus derivative estimate gives shell coefficients C_j s(1+s|r|)^(-j); summing yields the asserted1/(1+|r|) envelope. For the low-frequency-removed symbol, summing shells beginning at kappa gives the stronger1/(1+|r|)(1+kappa|r|)^(-4) bound, with one fixed cutoff profile. Smooth outer torus patches pose no singularity.

Choosing kappa=1/ell is decisive: every nonzero momentum on the2ell torus has magnitude>=pi/ell>2kappa, so the sampled cutoff inverse equals the exact mean-zero discrete inverse, including its zero value at zero. The cut kernel is absolutely summable. Its nonzero images costO(1/ell), and the removed Fourier ball has L1 normO(1/ell). The uniform torus comparison is legitimate without periodizing the divergent uncut1/r series.

The eight reflected images give the free-path Neumann kernel with NO division by eight. Their stationary contributions match the removed Neumann constant mode. A nonidentity reflection of interior points lies at periodic distance at least2w+1 in a reflected coordinate, so the infinite-kernel decay and O(1/ell) torus comparison giveO(1/w). This checks the central boundary estimate with the required universal constants and correct diagonal leading term g.

## Pin form and literal many-particle count

R-separated sites have cardinality<=8ell³/R³ by disjoint translated cubes. Shell packing bounds the direct offdiagonal1/r sum byC ell²/R³; reflected-image errors costCm/w. The leading diagonal g plus these terms is bounded by g+C ell³/(R³w). Cauchy in the zero-mean inverse form on the sum of evaluations yields m²||c||²<=(1^T Gamma1)E<=mBE, componentwise and hence for all nine components. No invertibility of Gamma is required.

Free-path Poincare lambda1>=4/ell² prices the variance. Eliminating the mean gives exactly E>=m||f||²/[ell³(B+M/(4ell))], including m=0. This is a form inequality on actual removal amplitudes, not an independently supplied scalar particle model.

For each original isolated dimer removed inside a cell interior, all other selected isolated dimers remain valid residual pins. There is one forward physical graph edge for that dimer and one possible input occupation for a fixed output and edge. Thus g_j removals each receive at leastg_j−1 pins, proving the literal g_j(g_j−1) coefficient. Extra removals add positive terms. Cross-input quantum coherence cannot enter the squared amplitude of a fixed annihilator/output pair because the input word is unique. Purification or linearity gives mixed states.

## Particle loss and unconditional scales

The omitted-site fraction is at most3ell/L+6w/ell. Averaging the tiling over torus translations bounds its omitted particle expectation by theta<N> for at least one translate. Interiors are separated by at least2w+1>=3 coordinate steps while graph edges have Chebyshev length<=2, so any omitted isolated dimer has an endpoint in the bad region. Counting dimers, rather than particles, gives G>=(N−B_R)/2−theta N. Both the factor2theta in beta and the subtractionN/2 in Jensen are correct.

With n_cells ell³<=V, Cauchy/Jensen yields the exact finite inequality(17), including its potentially adverse rho/(2ell³) term. It remains valid for arbitrary particle-number fluctuations at fixed MEAN density. The selected translate is allowed because the original positive-row lower bound holds for every translate.

The exponents ell~rho^(-3/8),R~rho^(-7/24),w~rho^(1/16)ell give Green-row and strip errorsO(rho^(1/16)), and variance, bad-particle and subtraction errorsO(rho^(1/8)). Integer rounding changes only fixed constants at sufficiently smallrho. In the branch e<=(a/g)rho², the energy inside beta is controlled; the other branch already exceeds the desired lower bound. Using(1−beta)_+²>=1−2beta and the inverse-denominator estimate therefore removes the low-energy hypothesis rather than presuming it.

The result is e>=a rho²[1/(4g)−C rho^(1/16)−C ell/L]. The volume-first limit is essential. FixedN=2 zero-energy sequences are outside L>=4ell at the chosen density-dependent scale, so there is no contradiction with the five exact two-particle zero modes.

For chemical-potential ground states, the old full-carrier coercivity forces thermodynamic densities to zero asnu tends to zero. The new asymptotic quadratic lower bound then minimizes to−g/a for energy/nu². Comparing to vacuum gives the independent upper density slope4g/a. Neither argument differentiates an unknown EOS or identifies a unique density/phase.

## Auxiliary nine-component gap and restricted lift failure

The unregularized row cut has a genuine axial corner zero variable because each complete relevant centered row would also require an outside anchor. Adding epsilon a times all nine scalar Neumann gradients forces every zero mode to be spatially constant; interior S rows then remove exactly four internal high directions, leaving the five normalized soft modes.

For the gap, S_inner(m)=2mu(ell−2)³||P_high m||² and S_inner(q)<=2mu||q||². The latter is the actual infinite nine-bond symbol bound, with zero extension of q. The triangle inequality gives ell³||P_high m||²<=27S_inner(f)/mu+54||q||². Adding the variance and applying Neumann Poincare gives the coefficient55ell²/(4epsilon a)+27/((1−epsilon)mu). For ell>=3,epsilon<=1/2,a<=mu/12 it is<=14ell²/(epsilon a), exactly the claimed gap. The common-pin inverse lower bound follows from K<=bI and the one-site constant-soft projection U U†/ell³. This gap is explicitly NOT a premise of the scalar lower theorem.

The warning about a naive matrix-Green cutoff is correct: a derivative of the forward axial singlet row can map a zero-mode E vector into the high singlet, so a first-order residual cannot silently be priced as the scalar second-order one. No repaired matrix capacity convergence is asserted.

Finally the normalized four-removal lift counts additional spectators with factors(N−1)/3,1,2/(N−2) for one-,two-,three-body terms. Subtracting it from H_N gives exactly(N−4)[V3/(N−2)−mu N/3]. It is negative on separated dimers at evenN>4. This rules out that direct lower-comparison template only; it does not rule out compatible quartet localization or another emergence map.

## Actual independent finite controls

The new check_exact.py constructs the27-site Neumann Laplacian directly from graph edges and computes its mean-zero inverse in exact rational arithmetic. Three pin sets yield exact minimum capacities243/44,1215/211,576234/39431, and satisfy the mean-capacity/norm and variance inequalities. An independently generated doubled-period FFT Green kernel matches all729 rational-inverse entries after eight reflections, maximum discrepancy1.11e−16; the erroneous one-eighth normalization fails by0.3759.

Literal occupations with6,9,8 particles give removal counts6,15,6 against the respective g(g−1)=6 lower bound, including a triangle and a boundary dimer. The extra one-half fails for three isolated dimers. Five exact symbolic spectator counts reproduce the four-removal factors and negative difference. These are finite controls, not evidence that sampled lattices prove asymptotic constants. No author implementation was inspected or executed. Actual runtime0.126982CPU, peakRSS67,616,768bytes; exit0, no failed run or repair.

## Reuse boundary

This is a substantial actual many-particle lower coefficient with explicit finite-volume error. It retires the need to demand negligible ENERGY from every rare higher cluster in this particular lower argument; their particle loss suffices. It does not identify the coefficient with the full15-channel threshold form, prove condensation/fragmentation, derive record or gravity observables, or establish an axiom contradiction. Full compatible two-pair replacement with the actual T0 interaction remains a distinct useful hard target.
