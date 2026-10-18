# Exact distinct-edge rectangle coefficient and bound

Disposition: PASS for the root's susceptibility-derived closed form of this edge-resolved minimal-cycle coefficient. An independent unsigned Catalan argument also supplies a rigorous exponential bound. Neither result proves convergence of the complete native effective interaction.

## Exact local susceptibility argument

Use H0=-(d/2)Z for one polarized spin, so its excitation cost is d. With Matsubara Fourier convention exp(i omega tau), direct two-level calculation gives

    chi_XX=2d/(omega²+d²),
    chi_YX=+2omega/(omega²+d²),
    chi_XY=-2omega/(omega²+d²).

For example, the time-ordered YX correlation is -i exp(-d tau) for tau>0 and +i exp(d tau) for tau<0. Its Fourier transform is the expression above. The discontinuity at zero time is already included; no extra contact term is to be added. Reversing Fourier convention reverses both mixed signs and leaves their product unchanged.

On one row with r distinct native -Jx XX edges, the coefficient in the endpoint YY susceptibility at order Jx^r is the unique connected path. Each intermediate spin has exactly two X insertions, and each endpoint has one Y and one X insertion. Independent-spin expectation values therefore factor into TWO-point functions at every site. This argument does not assume Gaussian spin statistics or Wick factorization of higher local correlations. The r! orderings cancel the perturbative exponential factorial; each distinct edge is used once. Instantaneous bonds conserve the frequency along the path. The result is

    chi_Y0Yr(i omega)|distinct path
      = Jx^r chi_YX chi_XX^(r-1) chi_XY
      = -(omega²/d²) Jx^r [2d/(omega²+d²)]^(r+1).

At r>=1 this has no frequency-independent contact piece. Contributions with repeated edges or higher local insertions are not part of this coefficient.

Now couple two independent rows through the TWO distinct endpoint -Jy YY bonds. In the ground-energy cumulant, the cross factor2 cancels the1/2 of the quadratic expansion. Thus the cross coefficient is

    -Jy² integral_(real omega) d omega/(2pi) chi_Y0Yr(i omega)^2.

The row susceptibility is even in omega, so the usual product chi(i omega)chi(-i omega) is indeed its square. This fixes both the overall minus sign and the factor of two.

After omega=d*u, the dimensionless coefficient is exactly

    c_r = -4^(r+1) B(5/2,2r-1/2)/(2pi)
        = -(6/4^r) binom(4r-2,2r-1)/[(2r)(2r+1)],   r>=1.

The energy term is c_r Jx^(2r) Jy²/d^(2r+1). For a nonuniform aligned background each mixed endpoint susceptibility acquires its endpoint spin sign; the two rows consequently multiply this coefficient by the four-corner Z parity. The internal spin signs cancel.

The beta integral converges for every r>=1. Exact rational evaluation of the binomial expression matches all seven supplied path-enumeration results. This independently justifies the formula rather than inferring it from those seven values. Saved comparison: neutral-rectangle-range-closed-independent.json.

## Folded terms and coefficient scope

Treat edge couplings as distinct before extracting the monomial that uses each perimeter edge once. No nonempty proper subset of a simple cycle restores every physical spin. Thus no intermediate P return, disconnected vacuum factor, or canonical folded term can contain this monomial. This is why the linked energy coefficient above equals the distinct-edge resolvent word sum. It does not exclude other terms at the same uniform-coupling order when edge variables are subsequently identified.

## Independent unsigned bound

For a simple N-edge cycle, define F(S) as the sum of absolute denominator weights of all ordered additions producing a proper edge subset S, including its final denominator. If S has k disjoint edge runs of lengths l_1,...,l_k, its flipped-vertex count is2k. The recurrence is

    F(S)=[sum_(e in S) F(S without e)]/(2k),   F(empty)=1.

Induction and the Catalan convolution give the exact solution

    F(S)=product_j Catalan(l_j)/2^|S|.

Indeed deleting an edge from a run splits it into two shorter runs, and their Catalan convolution sums to the Catalan number of the original run. Each run contributes a ratio2 to the numerator, canceling the denominator2k. The last cycle edge has no denominator, giving total unsigned sum

    U_N=N Catalan(N-1)/2^(N-1)
       =binom(2N-2,N-1)/2^(N-1).

Hence for N=2r+2,

    |c_r| <= binom(4r+2,2r+1)/2^(2r+1) < 2*4^r.

This is an all-r exponential bound independent of the signed closed form. Exact subset-DP checks at N4,6,8,10,12 confirm the identity; results are saved in neutral-rectangle-range-bound-independent.json. Stirling's formula gives the unsigned asymptotic O(4^r/sqrt(r)), whereas the signed closed form is O(4^r/r^(5/2)).

Restoring couplings, the elementary bound is

    |term_r| <= (2 Jy²/d) [4 Jx²/d²]^r.

It gives a geometric majorant for this selected minimal-rectangle family when |Jx|<d/2. It is NOT a convergence bound for all native words, repeated-edge dressings, all transverse shapes, canonical transformations, or excited-sector remainders. No all-order physical interaction or scalar conclusion is established. No repository edits or formal audit were performed.

## Bulk coefficient and connected two-column subtraction

For a bulk slice d=4Jz and Jx=Jy=lambda Jz, writing the contribution as -K_R times the four-corner parity gives

    K_R = [6 binom(4R-2,2R-1)/(4^(3R+1)(2R)(2R+1))]
          Jz lambda^(2R+2),   R>=1.

This follows directly from the exact c_R and its denominator d^(2R+1); it is positive. Using binom(2n,n)~4^n/sqrt(pi*n) with n=2R-1 gives

    K_R ~ [3/(32 sqrt(2pi))] Jz lambda²
           (lambda²/4)^R R^(-5/2).

The asymptotic prefactor and powers therefore check. If energies are expressed in Jz units, the displayed factor Jz is omitted; it should otherwise be retained for dimensional consistency.

For one such rectangle containing both selected flipped columns among its four corners, define the connected energy by E_both-E_first-E_second+E_vacuum. Its parity is positive in the vacuum and after both flips, negative after either single flip. The four energies from this rectangle are respectively -K_R,+K_R,+K_R,-K_R, so the connected subtraction is exactly -4K_R per shared bulk slice.

Two columns on the same transverse row at horizontal separation R are simultaneous corners of exactly two HEIGHT-ONE, WIDTH-R rectangles, one extending to y+1 and one to y-1. Over ell shared longitudinal bulk layers, this selected family therefore contributes

    Delta E_connected = -8 K_R ell,

apart from endpoint motifs, which have not been included. At R1, K_1=Jz lambda^4/128, hence the contribution is -Jz lambda^4 ell/16. This equals the previously checked adjacent-column tension minus the tension of two columns sharing no plaquette: Jz lambda^4 ell/16-Jz lambda^4 ell/8.

This subtraction concerns a reference configuration with identical uniformly polarized bulk outside the intervals. It isolates the distinct-perimeter monomial for width-R, height-one rectangles. Other rectangle heights, repeated-edge corrections, other connected shapes, background changes, and higher-order canonical processes are not summed. It must not be called the full all-order two-column potential, a universal force, or an empirical interaction law. No source/detector coupling is inferred.

## Original longitudinal observable from the same cycle

The proposed source derivative checks for a bulk slice away from longitudinal feature endpoints. Take H(s)=H+sC solely as a generating family, with the existing observable C=sum Z_z Z_(z+2). Flipping one physical spin on that slice reverses its two nearest longitudinal bonds, costing4Jz, and reverses its two distance-two readout pairs, changing C by-4. Thus its source-dependent excitation cost is exactly d(s)=4(Jz-s). For several virtual flips on distinct columns at the same slice, both costs add; there are no flipped distance-two partners on another longitudinal slice in this particular word family.

An N-edge simple cycle has N-1 intermediate denominators, each proportional to d(s). Its vertices contain no s. Consequently

    K(s)=K(0)*(1-s/Jz)^(-(N-1)),
    C_eff,cycle=partial_s[-K(s)P] at0
               =-(N-1) K(0) P/Jz.

The sign is specific to the PLUS-source convention H+sC. It can also be checked directly by inserting the diagonal observable into every intermediate denominator; all N-1 derivatives have the same relative factor1/Jz. The reference C value is unchanged by reversing aligned columns in the interior, so no additional bulk reference term enters this nonconstant cycle coefficient.

A canonical observable derivative can in general differ from the derivative of the effective Hamiltonian by a connection commutator. Here the squarefree edge monomial can be isolated before identifying couplings. Any lower folded or connection product contributing this monomial would split the cycle into a proper subset returning to P. No such subset exists: it leaves a physical site with odd flip parity. The commutator with the unperturbed scalar energy in the chosen degenerate manifold is also zero. Thus those terms cannot alter this diagonal distinct-cycle coefficient. This argument is specific to the edge-resolved monomial and does not make effective-H differentiation an unrestricted all-orders observable identity.

For width R, N=2R+2. Applying the same connected two-column subtraction gives

    Delta C_connected = (2R+1) Delta E_connected/Jz

for this rectangle family and its overlapping bulk slices. The factor depends on R. It therefore does not yield a universal mass/source proportionality after summing different processes. Longitudinal endpoints, mixed-slice paths, repeated edges and other operator families need separate derivatives and have not been included. H+sC is a calculation device for the supplied observable, not a newly adopted physical interaction or detector coupling.
