# Geometry activates the original neutral diagnostic

**Status:** bounded-support.
**Primary runner:** [scripts/native_odd_rectangle_response.py](../scripts/native_odd_rectangle_response.py)

Odd-height large column features support a neutral two-state degree of
freedom that was absent in the even-height ground band. A square array keeps
the original scalar diagnostic dark by symmetry. A rectangular array removes
that restriction and gives a nonzero coupling derived from the original
Hamiltonian and observable, without adding an interaction.

These are fixed finite-array, weak-coupling results. They do not establish a
propagating cosmological scalar, a feature embedded in an infinite grid, or
a universal matter coupling.

## The parity change exposes a neutral degree of freedom

Keep the supplied directional one-qubit XX/YY/ZZ Hamiltonian, with
Jx=Jy=lambda Jz>0. Columns now have odd open height L>=5. The transverse
sizes are even and at least four. The derived plaquette-positive patterns
remain s_xy=a_x b_y.

For odd height, the physical X and Y plane operators anticommute. On a
square transverse M by M array, their two-dimensional irreducible
representations occur with multiplicity two. The second two-state factor
is neutral under the physical plane symmetries. This differs from the
multiplicity-one even-height result; its selection rule cannot simply be
carried across the parity change.

The same native row-tunneling hierarchy gives, in the maximal center sector,

    H_eff = scalar - tau_M(U+V) + o(tau_M),
    U^2=V^2=M^2,   UV+VU=0.

Here U and V both commute with the physical plane symmetries. They act on
the neutral multiplicity factor, while an exact physical symmetry doublet
remains. The neutral transition has gap 2sqrt(2)M tau_M+o(tau_M).
The existing anisotropy diagnostic Hx-Hy couples to it. For M=4,L=5 its
gap is (2sqrt(2)/19)Jz lambda^6 at leading order.

That square-array transition is nematic: it is odd under exchange of x and
y. The original uniform C=sum Z_j Z_(j+2) is even. Combined spatial/spin
exchange makes the invariant operator algebra on the symmetry-resolved
four-state band commutative, so C is exactly intraband inelastic-dark there.
Other center sectors can lie between its two doublets; this is not a claim
that the four states form the lowest four consecutive energy levels.

## A rectangle gives a nonzero original-source matrix element

Take periodic transverse sizes 4 by 6 and open odd height 5, totaling 120
physical one-qubit sites. The two native scales are

    t = Jz lambda^5/16,     K = 19 Jz lambda^4/128.

Whole-row and whole-column processes now require different numbers of pair
flips. In the maximal center's neutral factor,

    H_eff = scalar - a sigma_x - b sigma_z + higher orders,
    a = 3 Jz lambda^7/361,   b = 3 Jz lambda^6/38.

The actual ground doublet selects this maximal center for sufficiently
small lambda. This requires an order-eight check: the row energy lowering
is only order lambda^8. A neutral row/column operator has the unique phase
B^p R_I C_J, and its transpose sign is (-1)^(pq). The mixed single-row,
single-column term is therefore forbidden in the real symmetric native
Hamiltonian. The remaining order-eight column terms are identical across
row centers in the lowest column branch; the derived row mixing selects
the maximal row center. The independent source proof checks this comparison.
This does not identify the neutral transition as the unrestricted first gap.

Use H+sC only to calculate the matrix elements of the existing diagnostic;
s is not a proposed physical interaction. Exact virtual-path differentiation
and boundary-layer counting give

    t'/t = 9/(2Jz),    K'/K = 54/(19Jz).

A process with n pair events has logarithmic derivative
r_n=n t'/t-(n-1)K'/K. The row and column processes have n=3 and n=2, so
r_3-r_2=63/(38Jz). The original C therefore has an offdiagonal matrix element

    |C_ge| = ab|r_3-r_2|/sqrt(a^2+b^2) + O(lambda^8)
           = (189/13718)lambda^7 + O(lambda^8),

at the neutral transition

    gap = (3/19)Jz lambda^6 + O(Jz lambda^8).

The spectral weight is (189/13718)^2 lambda^14+o(lambda^14).
C here is unnormalized. For C/sqrt(120), divide the weight by 120.
The coefficient is small and geometry-dependent; it is not a supplied
universal scalar charge.

The positive static Lehmann susceptibility contributed by this line is

    2|C_ge|^2/gap = (11907/4952198)lambda^8/Jz + o(lambda^8/Jz).

Thus the soft line becomes weakly coupled as lambda tends to zero. This
is its contribution only, not a bound on the total static susceptibility.

Differentiating an effective Hamiltonian alone would be insufficient.
The [root source proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/RECTANGLE_SOURCE_ACTIVATION_PROOF.md)
controls both projected transformation connections: they begin at order
lambda^2. Their commutator with the first nonconstant lambda^6 ground
operator is order lambda^8, below the displayed lambda^7 matrix element.
Checkerboard parity also excludes a lambda^7 correction to b. All estimates
are at fixed finite dimensions in an analytic source neighborhood.

## Removing the transverse wrap is a geometry control

For a fully open 4 by 6 by 5 array, each row has one perfect matching.
A dimer-domain wall violates c neighboring plaquettes, where c is one at
a transverse boundary and two in the interior. The exact open-path
ordering sum is t^n/(Kc)^(n-1). Summing these native processes gives, in
the maximal center,

    a = (5/2)t^3/K^2 = 10Jz lambda^7/361,
    b = 4t^2/K = 2Jz lambda^6/19.

The leading neutral gap is 4Jz lambda^6/19 and the original-C amplitude
is 315lambda^7/6859. The same projected-connection estimate controls the
source remainder. The [independent open-path proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_OPEN_RECTANGLE.md)
derives the all-length path sum by independent edge-time integrals and
checks it with exact rational subset sums. This extension is stated in
the maximal center; the periodic rectangle's global-center comparison
is the ground-selection result used above.

Removing the transverse wrap still leaves a whole finite array with open
ends. It does not embed that array into a common surrounding lattice.

## Evidence and boundary

The [odd-height proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/ODD_COLUMN_NEUTRAL_PROOF.md)
and independent algebra, native-source and rectangular-coefficient checks
are in the campaign's native directory. The runner independently evaluates
the rational source coefficients and the column-model spectra. For the
rectangle, it uses a 32768-dimensional exact symmetry sector of the
24-column model, not the 120-spin native Hilbert space. At t/K=.01 the gap
and source-weight ratios to the leading predictions are 1.0000146 and
1.0010225. The square's even plaquette diagnostic remains dark numerically.
These are exposed development controls, not independent observational tests.

Geometry and boundary conditions remain supplied. The result establishes
activation of an existing neutral readout in a finite candidate array;
it does not derive its embedding in a surrounding source or detector,
spatial propagation between arrays, a cosmological field, physical units,
or observed gravity. The rectangle also breaks rotational symmetry, so
calling the mode a Lorentz scalar would exceed the result. No empirical
value is fitted or imported as a derivation.
