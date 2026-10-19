# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Independent simple xy-cycle coefficient check

Checked 2026-10-18. Read neutral_simple_loop.py/json. The formula is correct for the specified distinct-edge simple-cycle monomial, with V_e=-g_e sigma_i^(a_e) sigma_j^(a_e), a_e in {X,Y}, and independent local reference flips of common positive cost d. The native embedding requires the qualifications below.

## Derivation without a Gaussian premise

Temporarily treat each edge coupling g_e as an independent formal variable. The coefficient of product_e g_e in the ground-energy expansion is minus the connected imaginary-time integral of the N distinct edge insertions, per unit time. The expansion's 1/N! cancels the N! assignments of distinct labelled edges. Every nonempty proper edge subset of a simple cycle has vertices of odd degree. Its reference expectation is zero, because a vertex with one X or Y insertion has zero expectation. Consequently all proper-subset cumulant subtraction terms vanish for this monomial. There are no repeated-edge folded/normalization contributions with this same multivariate monomial.

Each site receives exactly two insertions. Their exact two-point spin correlator suffices; no Wick theorem for higher spin correlators and no Gaussian state assumption are used. For a local reference with Z eigenvalue z=+/-1, using Fourier convention exp(i omega tau),

    chi_XX=chi_YY=2d/(d^2+omega^2),
    chi_XY=-2z omega/(d^2+omega^2),
    chi_YX=+2z omega/(d^2+omega^2).

Reversing the Fourier convention changes the cross signs together and leaves the loop answer unchanged. Choose an orientation around the loop. Color changes X->Y and Y->X occur equally often, c/2 each, so the product of cross signs is (-1)^(c/2). The Z factors occur precisely at the c color-changing vertices. Frequency conservation around the cycle leaves one integration variable. Thus

    coefficient = -(-1)^(c/2) product_corners z
                  * integral_R (domega/2pi)
                    2^N d^(N-c) omega^c/(omega^2+d^2)^N.

The integral is

    2^(N-1)/pi * d^(-(N-1))
    * B((c+1)/2, N-(c+1)/2).

This is exactly the proposed coefficient multiplying the corner-Z product. c is automatically even on any binary-colored cycle. The expression also exists for an abstract odd cycle; square-lattice geometric cycles of course have even N.

There is no additional factor of two. The direct labelled-edge time integral already counts all time orderings once and uses one chosen loop orientation merely to evaluate it. If reorganized as a graph trace, the 2 orientations and N cyclic starts cancel the corresponding 1/(2N) trace-loop factor. Mixing that trace convention with the already labelled coefficient would double count.

## Checks and examples

The parent exact subset DP uses the excitation energy d times the number of flipped sites. For X edges its matrix amplitude is -1; for Y edges it is (-1)^(number of currently down endpoints), correctly implementing -YY in the up reference. Every proper subset denominator is nonzero for a simple cycle. Its unit-d outputs agree with the integral:

- N4,c4: -1/2.
- N6,c4: -3/8.
- N8,c4: -9/16.
- N8,c6: +5/16.

Therefore a geometric N8 six-corner L-shaped loop has the opposite sign to a four-corner rectangle, as stated. As an extra algebra control I ran all binary color assignments on abstract N=3,5,7 cycles against the closed formula; all passed. These odd cycles are representation controls only, not proposed native square-lattice loops.

At d=4Jz, the N4 coefficient is -1/(128 Jz^3), matching the familiar native plaquette coefficient after multiplying its four transverse couplings. At an open longitudinal end use d=2Jz instead. Equal d across the loop is essential to this beta-function simplification; unequal local gaps require the unsimplified product of local susceptibilities.

## Native scope

For a simple same-z xy loop in the strong-longitudinal aligned-column reference, each cycle vertex is a different column. Any intermediate subset flips at most one physical spin per participating column. The longitudinal energy cost is additive with the appropriate common interior/end gap, and no proper subset returns to the aligned manifold when a single-spin column flip costs positive energy. This is the native setting in which the calculation applies. The corner Z product is then the product of the corresponding aligned column labels; all local factors have been computed in that supplied reference manifold.

The formula gives the coefficient of the monomial with each of these N distinct edges used once. Setting all transverse couplings equal afterward does not make it the complete order-N effective Hamiltonian: repeated-edge paths, other cycles, different longitudinal-slice processes, short-column degeneracies, and endpoint terms still need their own classification. Self-intersecting loops or repeated vertices can give more than two insertions at a site, so this proof no longer applies unchanged. An independently selected equilibrium state, universal source/detector coupling, or cosmological field does not follow.

Conclusion: the prefactor, sign, and simple-loop cumulant reasoning pass under the stated microscopic/reference assumptions. No Gaussian premise or added physical interaction is required for this formal coefficient calculation.

## Added absolute family bound

The unsigned sum of all ordered-path denominator weights for a length-N simple cycle is the c=0 magnitude,

    U_N = binom(2N-2,N-1)/2^(N-1) < 2^(N-1), N>=2.

Absolute values of the phase-bearing colored sum are bounded by this unsigned sum. Counting rooted nonbacktracking square-lattice walks gives at most 4*3^(N-1) candidates and therefore, with |g_e|<=J,

    sum_rooted |coefficient_N| <= (2d/3) q^N,
    q=6J/d.

Self-avoidance and closure only reduce this overcount. If two distinct same-row columns are separated by R>=1, any simple square-lattice cycle containing both has even perimeter at least m=2R+2. A product-of-corner-labels term contributes to their two-flip connected energy difference only when both occur among its corners; the magnitude of that difference is at most four times the coefficient. Thus for ell identical bulk slices,

    |connected family energy| <= (8d ell/3) q^m/(1-q^2), q<1.

For d=4Jz this is q=3lambda/2 and the sufficient condition lambda<2/3. Counts are deliberately loose; no unique-cycle symmetry divisor is needed in an upper bound.

For the stated interior NNN source convention d(s)=4Jz-4s, differentiating a length-N coefficient at fixed transverse J multiplies its magnitude by (N-1)/Jz. Accordingly the readout bound is

    (8d ell/(3Jz)) q^m *
    [(m-1)/(1-q^2) + 2q^2/(1-q^2)^2].

The derivative has to be defined with the actual source-dependent microscopic cost; other source normalizations or longitudinal endpoints need a separate factor. The displayed derivative sum is valid at the reference s=0.

These constants and summations check. This is absolute convergence and an exponential-separation bound for the selected distinct-edge simple-loop coefficient family only. It is neither convergence of the complete native perturbation series nor a proof that all physical long-range response is exponentially bounded. Repeated edges, multi-loop clusters, other orders/processes and state selection remain outside it.
