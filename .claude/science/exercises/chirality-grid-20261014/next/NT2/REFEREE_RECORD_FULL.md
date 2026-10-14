# NT-2 independent referee verdict

## VERDICT: CONFIRMED WITH CORRECTIONS

The exact T22 counterexample is valid and by itself fixes the pre-registered
reading to **PG3-NEG**.  O12 supplies a second exact counterexample and O22 is
strong, reproducible numerical corroboration.  The needed correction is one of
scope: the result proves failure on specified finite 3D link-reflection
geometries (and therefore disproves universal finite-lattice reflection
positivity of the flat hard plaquette weight); it does not prove that every
finite geometry or the infinite-volume 3D measure is non-RP.  The O22 error is
an a-posteriori convergence diagnostic, not a certified quadrature remainder.

## 1. T22 kernel, boundary reduction, and exact witness

For a positive-half boundary link field `u`, its reflected partner `v`, and
crossing temporal links `g_x`, each crossing plaquette contributes
`1(|w_l+(dg)_l|<delta)`, where `w=u-v`.  Integrating the crossing links modulo
the redundant global gauge angle therefore gives

`K(u,v)=(2 pi)^(-3) integral prod_l 1(|w_l+(dg)_l|<delta)`.

This is the link-reflection kernel, not an imposed boundary projection.  All
strictly admissible boundary configurations used by the witness are realizable:
copying a boundary slice into the positive bulk and taking temporal links zero
makes every added temporal plaquette flat.  The positive-half marginal is thus
strictly positive near the six configurations.  Continuity then replaces the
point masses by small gauge-invariant bumps without changing the negative sign.
This validates the reduction stated at `PREREG.md:34-41`.

On the 2x2 torus write `Delta_j=g_(1,j)-g_(0,j)` and
`Gamma_i=g_(i,1)-g_(i,0)`.  The two oppositely oriented links in row `j`
restrict `Delta_j` to an interval of width
`a_j=(2 delta-|Delta X_j|)_+`; the column pair similarly gives
`b_i=(2 delta-|Delta Y_i|)_+`.  The only relation is
`Delta_1-Delta_0=Gamma_1-Gamma_0`.  A determinant-one change of the three
independent gauge variables therefore gives

`K=(2 pi)^(-3) (B_a0*B_a1*B_b0*B_b1)(sigma)`,

with `sigma=(Delta phi_10+Delta phi_01)/2` up to the irrelevant sign of the
even convolution.  When `4 delta < pi`, the four interval half-widths cannot
wrap around the circle, so there are no omitted winding copies.  This
independently derives `PREREG.md:47-53` and agrees with the explicit-link route
at `scripts/t22lib.py:101-126`.

I recomputed the six-by-six matrix without using the signed-truncated-power
implementation, instead integrating the product of two triangular overlap
functions piecewise in exact rational arithmetic.  It exactly reproduces the
matrix printed at `scripts/V2_exact_witness.out:1-7`.  Exact symmetric LDL
elimination has signs `+++++-`, hence inertia `(5,1)`.  In the configuration
order used at `scripts/v2_exact_witness.py:18-24`, the vector

`(1,-9/5,1,-1,9/5,-1)`

gives exactly `-27/12500`, followed by the positive normalization
`(2 pi)^(-3)`, confirming `scripts/v2b_exact_vector.py:13-20` and
`scripts/V2b_exact_vector.out:4-6`.  Scaling `delta`, the fluxes, and the
holonomy offset together multiplies the matrix by `delta^3` and preserves its
inertia.  Thus the witness works for every `0 < delta < pi/4`.

The stated cusp mechanism is also correct.  For an infinitesimal row-holonomy
split, `(K_0-K_epsilon)/epsilon` tends on the witness range to
`B(sigma)=(2 delta)^2-sigma^2/2`.  On flux points `(-s,0,s)`, a symmetric
vector `(1,beta,1)` has quadratic form
`a((2 delta)^2 a-2s^2)`, where `a=2+beta`; it is negative for
`0<a<2s^2/(2 delta)^2`.  The choice `s=11 delta/12`, `beta=-9/5` satisfies
this inequality.  This explains, rather than merely numerically accompanies,
the exact witness.

## 2. O12 exact witness

For the open two-plaquette strip, gauge fixing leaves the shared edge `e` and
three independent outer edges per plaquette.  Consequently, up to the positive
Haar normalization,

`h(F1,F2)=integral_[-delta,delta] T3(F1-e) T3(F2+e) de`,

where `T3=B_(2 delta)^{*3}`.  This is the correct open-strip crossing kernel
used at `scripts/o12.py:1-25`.

I recomputed it from the independent piecewise formula
`T3(x)=3 delta^2-x^2` for `|x|<=delta` and
`T3(x)=(3 delta-|x|)^2/2` for `delta<=|x|<=3 delta`, integrating each quartic
piece exactly.  On the 4x4 grid specified at
`scripts/v3_o12_exact.py:26-28`, exact LDL again gives inertia `(15,1)`.
The printed integer vector at `scripts/V3_o12_exact.out:4-5` evaluates exactly
to `-24077087111/243000000 < 0`.  The matrix scales by `delta^5`.  For
`delta < pi/3`, a nonzero plaquette winding would require at least
`2 pi-2 delta > 4 delta`, so the real-line formula contains every circular
sector.  The exact O12 claim for all `0 < delta < pi/3` is therefore confirmed.

## 3. O22 convergence

The reduction at `scripts/o22lib.py:1-7` is correct: the four central edges are
integrated over `[-delta,delta]^4`, while each pair of outer edges produces
`T(x)=(2 delta-|x|)_+`.  Replacing each point probe by a product cubic
B-spline replaces `T` by its convolution with the degree-seven autocorrelation,
as implemented at `scripts/o22lib.py:11-48`; the test-function support remains
strictly inside the admissible box (`scripts/o22_rp.py:16-31`).

The saved `rho=0.1` runs progress from 81 to 256 to 625 test functions with
negative minima `-1.7359e-4`, `-1.6082e-3`, and `-3.3166e-3`
(`scripts/O22_grid3.out:1`, `scripts/O22_grid4.out:1`,
`scripts/O22_grid5.out:1`).  The independent `rho=0.05` sequence is positive
at the under-resolved 81-function level but negative at 256 and 625 functions
(`scripts/O22_grid3_rho0.05.out:1`, `scripts/O22_grid4_rho0.05.out:1`,
`scripts/O22_grid5_rho0.05.out:1`).  I reran the 256-function, `rho=0.1` case
at Nyström levels 96 and 128: `lambda_min=-1.6082e-3`, relative
`-1.464e-5`, level-difference Weyl bound `4.5e-10`, peak RSS 81 MB.  Hence
"quadrature-converged negative" is justified.  It should not be called a
rigorous/certified quadrature bound, because successive-level agreement alone
does not bound the unseen remainder.

## 4. Scope and positive sub-sectors

The evidence is for pure compact U(1), link reflection, the flat plaquette
indicator, and `beta_g=0`, exactly as delimited at `REPORT.md:65-69`.  T22 and
O12 are exact finite-lattice counterexamples; O22 is corroboration.  No result
here establishes non-RP for every finite 3D geometry, an infinite-volume Gibbs
state, a full 4D slice, a nonabelian group, site reflection, or `beta_g>0`.
Thus the phrase "finite 3D lattices" at `REPORT.md:67` should be read
existentially and replaced by "the specified finite 3D lattices."

The positive-sector statements at `REPORT.md:44-45` are consistent with the
kernel.  If all four Wilson lines are matched, every box has width `2 delta`
and the remaining translation kernel has Fourier transform `sinc^4 >= 0`.
In the free-holonomy charge-zero sector, the eight components of every closed
current pair as `(n,-n)` on opposite parallel links, so its coefficient is a
product of `c_n c_-n=c_n^2` factors and is nonnegative.  These are proper
sub-sectors and do not constrain the mixed flux/holonomy witness.

Finally, replacing the flat indicator by the circular convolution of two
half-width indicators gives a triangular profile with the same support and
nonnegative Fourier coefficients (squares).  The standard
Osterwalder-Seiler character-expansion criterion then restores pure-gauge RP.
This is a different plaquette profile with the same support, not a rescue of
the flat indicator.

## 5. Fixed reading and adversarial scope check

The five principal attacks on PG3-NEG all close at the finite T22 scope:
the link-reflection crossing variables and normalization are correct; the
six configurations are genuine gauge-orbit boundary data; strict
admissibility permits smooth bump witnesses; circular winding sectors are
excluded by `4 delta < pi`; and the exact rational quadratic form is negative
under an independent piecewise integration.  The strongest steelman is that a
particular infinite-volume state or other finite geometries might still be RP;
that is outside, and narrows rather than defeats, the finite counterexample.
K2c's unresolved residual was precisely the restriction to admissible boundary
spatial plaquettes (`K2c_REPORT.md:105-108`); every T22 witness plaquette has
absolute angle at most `11/20 < 3/5`, so the new witness closes that residual.
Under the fixed criterion at `TESTS.md:35-38`, **PG3-NEG follows**.  The 4D
status remains suggested/open.

## Strongest correct statement

For every `0 < delta < pi/4`, at `beta_g=0` the flat compact-U(1) plaquette
weight `1(|arg U_p|<delta)` is not link-reflection-positive on the finite 3D
lattice with a 2x2 periodic spatial reflection slice: six strictly admissible
boundary gauge orbits have an exact crossing-kernel quadratic form
`-27/12500 (2 pi)^(-3)` after scaling from `delta=3/5`, and continuity turns
this point certificate into smooth gauge-invariant positive-half test
functions with negative Osterwalder-Schrader form.  An independent open 1x2
strip certificate holds for every `delta < pi/3`, and open 2x2 smooth probes
are quadrature-converged negative at `delta=3/5`; these results disprove
universal finite-lattice RP of the flat hard weight in 3D, while making no
claim about all geometries, the infinite-volume state, or 4D.
