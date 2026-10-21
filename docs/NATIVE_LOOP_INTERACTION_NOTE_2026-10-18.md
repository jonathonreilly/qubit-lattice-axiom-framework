# Native simple-loop interactions between extended features

Claim type: bounded_theorem.

Primary runner: `scripts/native_loop_interaction.py`

**Status:** bounded-support.

The supplied one-qubit compass Hamiltonian already produces interactions
between column features. This block derives an arbitrary-size family of
those terms and its contribution to the original readout. No new Hamiltonian
interaction, scalar field, or fitted coupling is inserted. The selected
family is short ranged at weak coupling; it does not yield a Newtonian force.
It is not the whole effective Hamiltonian or a no-go theorem for that model.

The preceding [native coefficient calculation](NATIVE_SLOW_COMPOSITE_CONTROL_NOTE_2026-10-18.md)
and [corrected channel calculation](NATIVE_CORRECTED_FAST_STRIP_NOTE_2026-10-18.md)
leave the full native pole and physical identification open. This route
addresses interaction coefficients directly, rather than interpreting a
chosen diagnostic as a physical coupling.

## A coefficient with no free selector

Fix a bulk longitudinal layer away from feature ends. In a reference with
aligned columns, flipping one spin at that layer costs d=4Jz. A simple xy
cycle has N distinct transverse edges. Attach a separate formal coefficient
to each edge and extract the monomial in which each occurs exactly once.
No proper subset of a simple cycle returns all spins to their reference
values. Consequently no intermediate energy denominator vanishes, and no
folded lower-order return can carry this monomial. This is a statement about
a formal perturbative coefficient, not convergence of the full expansion.

Let c be the number of changes between X and Y edge colors around the cycle.
It is even. The surviving diagonal operator is P_c, the product of reference
Z coordinates at those corners; vertices with equal colors cancel. The
coefficient for unit edge amplitudes is

    a_(N,c) = -(-1)^(c/2) 2^(N-1)/pi
              * B((c+1)/2, N-(c+1)/2) / d^(N-1).

For a geometric rectangle c=4. For an eight-edge L-shaped loop c=6, the
sign reverses: at d=1 the rectangle coefficient is -9/16 and the L-shaped
coefficient is +5/16. This generates multi-column interactions of different
signs without adding them. Arbitrary binary color cycles used in algebra
controls need not all embed as simple square-grid polygons.

## Derivation from two-point spin response

At a single reference spin, H0=-dZ/2. With Fourier convention exp(i omega tau),
its zero-temperature imaginary-time susceptibilities are

    chi_XX=chi_YY=2d/(omega^2+d^2),
    chi_YX=+2omega/(omega^2+d^2),
    chi_XY=-2omega/(omega^2+d^2).

At each vertex of the selected monomial there are exactly two insertions.
The connected cycle therefore contracts only these exact single-spin
functions. This does not assume Gaussian spins: higher on-site cumulants
are absent for this monomial. The expansion factorial cancels the distinct
edge orderings; there is no additional N or orientation factor. Integrating
all vertex times leaves one frequency integral per unit imaginary time.
The minus sign converting logZ to ground energy gives

    a_(N,c)=-(-1)^(c/2) integral d omega/(2pi)
              (2d)^N (omega/d)^c /(omega^2+d^2)^N.

The beta integral yields the formula above. Equal-time mixed-spin jumps are
already included in chi_XY and chi_YX; no separate contact term is appended.
Changing the reference spin signs supplies precisely P_c.

An independent exact subset dynamic program sums all virtual edge orders,
with rational denominators -d times the number of flipped spins. It agrees
for all binary color assignments at N=4,6,8. Rectangle checks reach N=20.
The initial guess of a simpler central-binomial coefficient failed at width3;
that failed guess and its actual outputs are preserved.

## Arbitrary-width rectangles and feature interaction

For width R, height1, N=2R+2 and c=4, the coefficient is

    a_R(d=1) = -6/4^R * binom(4R-2,2R-1)/[(2R)(2R+1)].

With Jx=Jy=lambda Jz and bulk d=4Jz, write the energy term as -K_R P:

    K_R = Jz lambda^(2R+2) * 6 binom(4R-2,2R-1)
          /[4^(3R+1)(2R)(2R+1)].

This recovers K_1=Jz lambda^4/128 and K_2=3Jz lambda^6/8192.
The large-R behavior within this selected family is

    K_R ~ [3/(32 sqrt(2pi))] Jz lambda^2
           (lambda^2/4)^R R^(-5/2).

Consider two flipped columns at the same y, separated by R in x, sharing
ell bulk layers. For one rectangle containing both as corners, subtracting
the two isolated-feature energies from the pair energy gives -4K_R. The two
rectangles displaced toward y+1 and y-1 give the family contribution

    Delta E_rectangle = -8 K_R ell.

For R=1 this is -Jz lambda^4 ell/16, agreeing with the prior adjacent-versus-
separated string-tension difference. End layers, repeated-edge diagrams,
other cycle shapes and full-H corrections are outside this expression.

## The original readout coefficient also follows

Let C=sum Z_(r,z) Z_(r,z+2), the existing longitudinal distance-two observable.
Use H+sC solely as a derivative generator for that observable, not a new
physical interaction. In an interior layer each virtual flip changes C by-4,
so d(s)=4(Jz-s). The selected cycle has N-1 denominators, giving

    K_R(s)=K_R(0)(1-s/Jz)^(-(2R+1)),
    C_eff,rectangle=-(2R+1)K_R P/Jz,
    Delta C_rectangle=(2R+1)Delta E_rectangle/Jz.

The absence of proper-subset returns also excludes folded or effective-basis
connection corrections carrying this particular distinct-edge monomial.
This derives a source coefficient from the same microscopic process. Its
R-dependent ratio is not a universal mass coupling, and the identification
of C with a measured detector remains an unproved premise.

## Absolute range bound for the whole simple-cycle family

For a proper edge subset of a simple N-cycle, the unsigned partial path sum
is the product of Catalan numbers of its edge-run lengths divided by2 to
the subset size. Deleting the last edge and using Catalan convolution proves
this by induction. The complete unsigned sum, without a final denominator,
is

    U_N=binom(2N-2,N-1)/2^(N-1) < 2^(N-1).

There are at most4*3^(N-1) rooted nonbacktracking cycles of length N at a
specified square-grid site. This deliberately overcounts simple loops and
orientations. With uniform transverse J, their total absolute coefficient
is bounded by (2d/3)q^N, q=6J/d=3lambda/2. Thus the selected simple-cycle
subseries converges absolutely for lambda<2/3. For the two-column geometry,
N is even and at least m=2R+2, giving

    |Delta E_simple cycles| <= (8d ell/3) q^m/(1-q^2).

The readout bound multiplies the prefactor by1/Jz and replaces1/(1-q^2) by

    (m-1)/(1-q^2)+2q^2/(1-q^2)^2.

These bounds sum only the distinct-edge simple-cycle family. They do not
control repeated-edge diagrams, self-intersections, full effective-series
convergence, or the actual microscopic long-distance response. They establish
exponential range for this family, not a global prohibition on emergent gravity.

## Evidence and remaining assumptions

Exact path sums, independent susceptibility/combinatorial checks and the
source-bound runner are in the campaign pack. No empirical calibration or
independent observation data were used. Supplied Hamiltonian, anisotropy,
column reference and geometry remain premises. Preparation, full native
resonance, light scale, cosmological state and physical source mapping remain
open. Compass-model high-order perturbation theory is established prior art;
the literature context (`outputs/neutral_continuation_review_2026_10_18/pr9745/native/LOOP_INTERACTION_PRIOR_ART.md`)
is separate from this coefficient derivation, for which no novelty claim is made.

## Portable proof and execution closure

The complete mathematical sources below retain their actual assumptions and derivations. Historical execution/review labels are not fresh evidence. The primary uses an isolated temporary copy of the bound source package, streams child diagnostics, enforces one aggregate wall-clock cap and records required fresh JSON identities. Large frozen grids remain historical source-bound results, not replays. No stronger physical or asymptotic scope is inferred.

- `outputs/neutral_continuation_review_2026_10_18/pr9745/native/INDEPENDENT_RECTANGLE_RANGE.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9745/native/INDEPENDENT_SIMPLE_LOOP.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9745/native/LOOP_INTERACTION_PRIOR_ART.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9745/native/REVIEW_LOOP_INTERACTION.md`
