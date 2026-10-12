# Lane RS probe S1 — independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

Under the unchanged FIXED reading in `TESTS.md:914-918`, S1 qualifies as a
**bounded FAIL concerning momentum only**.  The analytic no-slope result can be
completed for `d=2` at every finite mass and for `d=3,m=0`; the `d=3,m=0.5`
case is supported only in the sampled finite-range matrix spaces (`R<=4`), as
the reading explicitly permits when the singular gaps are order one.  The
headline at `S1_report.md:3` is nevertheless too broad: symmetry averaging
preserves and therefore excludes a taste-universal scalar slope, but it can
annihilate an odd non-singlet charge, and the massive-3D all-range/quasi-local
matrix problem remains analytically open.

I read all supplied reports, scripts and outputs, the Lane RS FIXED reading,
the local axiom memo, and the RN L2 referee's scope correction.  I compared the
scalar step with Spohn's proposition, and ran `S1_referee_checks.py`; its fresh
direct SVDs bypass the submitted TSQR accumulation.  Results are recorded in
`S1_referee_checks.out`.

## 1. One-particle structure

**Confirmed, with the cone-point qualification and one interaction-normalization correction.**

- The reduced-zone symbol at `S1_report.md:26-30` follows from the stated
  staggered phases.  The Clifford generators can absorb the displayed
  Fourier-sign convention, and `h(k)^2=(m^2+sum_j sin^2 k_j)I`.  Fresh checks
  give square and eigenvalue errors below `2.4e-15`
  (`S1_referee_checks.out:1-5`).
- The `+/- omega` multiplicities are `2^(d-1)` only away from the massless cone.
  At `m=0,k=0`, `h=0` and the zero eigenvalue has multiplicity `2^d`; there is
  no distinguished positive/negative band there.  This is a correction to the
  unqualified wording at `S1_report.md:29-30`, not to the generic result.
- `P_j=1/2{J_j,h}` has scalar symbol `sin(2p_j)/2`, real-space form
  `sum_x(c_x^dagger c_{x+2e_j}-h.c.)/(4i)`, unit slope at every full-zone
  corner, and commutes exactly with `h`.  The independent `6x6` construction
  gives zero commutator and a `4.1e-16` Fourier-spectrum error
  (`S1_referee_checks.out:6-7`).
- For the Hamiltonian as written at `S1_report.md:16`, normal ordering
  `U sum_y Q_y^2` gives two-body kernel
  `2U prod_j(2-|r_j|)` and Fourier kernel
  `2U prod_j(2+2cos q_j)`.  The collision code uses the same interaction at
  half this coupling (`s1_matrix_collision.py:64-67`), whereas the ED code
  includes the factor two (`s1_cluster_ed.py:40-44`).  This overall factor
  changes absolute cube amplitudes/singular values but not any null space,
  gap ratio, or verdict.

## 2. Matrix collision condition and kinematics

**Confirmed as a necessary first-order two-particle obstruction, with a missing regularity premise made explicit.**

The intertwiner equation at `S1_report.md:42-50` is the correct restriction of
`[h,P_1]+[H_int,P_0]=0` between equal-energy free two-particle states:

`(F_3 tensor 1 + 1 tensor F_4)W = W(F_1 tensor 1 + 1 tensor F_2)`.

It is necessary, not sufficient, and it assumes a family regular/analytic in
the coupling and a bounded `P_1` kernel.  If `P_0` contains a connected
two-body term, the displayed commutator derivation also needs the asymptotic
clustering/Moller argument used at `RN_L2_referee_full.md:37-60`, or an
equivalent statement excluding resonance-supported free two-body kernels.
Charges with zero one-particle action are not excluded, but cannot meet the
required momentum slope.  U(1) averaging correctly removes charged pieces
without changing a neutral one-particle action (`S1_report.md:51-54`).

The subadditivity argument at `S1_report.md:56-60` is valid.  For `m>0` it is
strict.  At `m=0`, equality in all componentwise sine and Euclidean triangle
inequalities forces cone/zero-energy degeneracies; there is no regular
positive-energy band-changing shell.  Thus six of sixteen channels are the
regular open channels.  The report's broader phrase “measure-zero collinear
set” should be narrowed to these exceptional cone configurations.  Fresh
sampling found all six regular channels and no low-ball band-changing process
(`S1_referee_checks.out:15-36`).

## 3. Shift-symmetry Schur reduction

**Confirmed for the required universal-slope question.**

With normalized reduced-zone shifts `s_mu=e^{-ik_mu}S_mu`, the `s_mu` are
`k`-independent Clifford generators: they commute with massless `h`,
anticommute with the mass matrix, and their even products are exactly the
surviving massive symmetries.  The interactions are invariant.  Conjugation
therefore preserves `s.k I`, so group averaging preserves the required
taste-universal slope (`S1_report.md:67-70`; `s1_shift_schur.py:43-72`).

The commutants at `S1_report.md:72-79` are correct:

- `d=2,m=0`: one irreducible 2D representation, commutant `C`;
- `d=2,m!=0`: two one-dimensional even-subgroup sectors, commutant `C+C`;
- `d=3,m=0`: two inequivalent 2D irreducibles, commutant `C+C`;
- `d=3,m!=0`: the even algebra `M_2(C)` occurs with multiplicity two, leaving
  commutant `M_2(C)`.

Thus the massive-3D `2x2` multiplicity/taste freedom is real.  Calling the two
tensor factors “spin” and “taste” is conventional; the representation-theory
content is the multiplicity.  Averaging does **not** prove that every odd
non-singlet invariant vanishes; it proves that any invariant with the
prescribed scalar universal slope would yield an averaged invariant with the
same slope.  This is enough for the FIXED momentum question but corrects
`S1_report.md:3`.

## 4. KG map, double cover, Spohn, and amplitudes

**The no-slope conclusion is correct after two explicit repairs; the report's proof as written is incomplete.**

The identity `k'=2k` sends
`omega^2=m^2+sum_j sin^2(k'_j/2)` and reduced momentum conservation modulo
`pi` to conservation modulo `2pi` (`S1_report.md:81-85`).  In the sector cases,
define

- `Z=-i s_1 s_2` for `d=2,m!=0`;
- `Z=-i s_1 s_2 s_3` for `d=3,m=0`.

Bloch sewing `k -> k+pi n` flips `Z` by `(-1)^(sum n_j)`.  Hence the two sector
functions are one scalar function on the connected cover
`R^d/{pi n: sum n_j even}`.  This makes the report's argued double-cover label
at `S1_report.md:84` precise.  A linear choice of primitive periods need not
look hypercubic, but it preserves Spohn's regularity and Hessian hypotheses.

[Spohn's theorem](https://arxiv.org/html/math-ph/0605069v1) allows a codimension-at-least-one singular set and requires a
generically nondegenerate Hessian.  The massless cones are isolated.  At
`k=(t,0,...)`, `0<t<pi/2`, the massless Hessian is
`diag(-sin t,1/sin t,...)`, so it is nondegenerate; for `m>0` the Hessian at
zero is `I/m`.  The conclusion is `g=a omega+c` almost everywhere.  The
sentence at `S1_report.md:85` that its gradient is zero at the massless cone is
false: `omega` has a cusp.  Local/exponentially quasi-local momentum has a C1
symbol, so the cusp forces `a=0` (and periodicity has already killed the affine
`b.k` term).  This is the correct massless conclusion.

Finally, “same-sector amplitude is not identically zero” plus random samples
(`S1_report.md:87-93`) is not by itself Spohn's almost-everywhere collision
hypothesis.  A sufficient repair is generic nonvanishing at forward
collisions, followed by continuity and the local collision differential
identity.  Independent sector projections give nonzero squared forward norms
for both sectors: `4.889...`/`104.267...` in massive 2D and exactly
`160`/`12800` in massless 3D for nn/cube (`S1_referee_checks.out:9-13`).  More
explicitly, in 2D at `k_1=0,k_2=(pi/2,0)`, the amplitudes in the submitted
normalization are `4(1-t)` and `12-4t`, with
`t=m/sqrt(1+m^2)`, hence positive at every finite `m>0`.  Analyticity away from
the cones then supplies generic local-shell coverage.  Thus the scalar
no-slope proof is repairable, but “the scalar problem is exactly the L2
problem” overstates what follows without this amplitude step.

## 5. Numerical null spaces

**Confirmed as well-conditioned sampled finite-basis results.**

Fresh-seed direct full-matrix SVDs (no TSQR) reproduce zero odd nullity for
both interactions, both masses, and `d=2,3`; representative gap ratios are
`0.26-0.41` (`S1_referee_checks.out:15-31`).  The even nullity is two in every
case, with null singular values `1e-14-1e-13`.  Counts are unchanged under
absolute cutoffs `1e-6`, the worker's `1e-8+1e-9 sv_max`, and `1e-10`, so the
RN L2 relative-only tolerance pitfall is absent (`s1_matrix_collision.py:215-222`).

The free control gives nullity `32/32`; the 1D massless control gives odd
nullity four at `R=8`, while massive 1D gives zero; and fixed `K=0`,
`K=(pi/2,...)`, and `K=(pi/2,0,...)` samples all reproduce with energy errors
at most `1.3e-15` (`S1_referee_checks.out:32-39`).  The submitted maximal-range
gaps—through `R=8` in 2D and `R=4` in 3D—are likewise order one
(`S1_report.md:123-140`).

These facts establish numerical rank only in the sampled finite Fourier
spaces.  Flat smallest singular values do not prove a uniform infinite-range
floor, and they do not exclude an exponentially quasi-local massive-3D matrix
invariant outside the tested ranges.  The report acknowledges this at
`S1_report.md:138-140,210-217`; its opening “no odd invariant at all” must be
read with that qualification.

## 6. Cluster exact diagonalization

**The calculation is correct and meaningful as supporting evidence for the specific natural momentum, not as a general locality theorem.**

For finite-dimensional Hermitian `H`,
`Pbar=sum_E Pi_E P Pi_E` is the Hilbert-Schmidt orthogonal projection onto the
full commutant of `H`; hence the code at `s1_cluster_ed.py:80-98` really computes
the distance to the nearest exactly conserved operator.  On `6x6,N=2,m=0.5`
the independent calculation reproduces
`||Pi_E[H_int,P]Pi_E||_op=0.204124...`, Frobenius `1.277087...`, and
`dist(P,Comm(H))/||P||=0.676931` from `V=1e-5` through `1e-3`
(`S1_referee_checks.out:41-45`).  The order-one limit is the expected
degenerate-perturbation discontinuity and cannot be canceled by a bounded
analytic `P_1`.

It is meaningful evidence that this particular `P_x` is not adiabatically
connected to any exact conserved operator on that finite two-particle cluster.
It does not impose locality on the comparator, take a thermodynamic limit,
exclude another free `P_0` with the same slope, or replace the collision
analysis.  The worker's own limitation at `S1_report.md:176-177` is therefore
essential.  The `6x4,N=3` order-one distances have zero first-order on-shell
block and are only higher-order finite-size support.

## 7. Verdict and remaining routes

The FIXED line expressly accepts either a proof or a matrix-valued numerical
check with order-one gaps (`TESTS.md:914-918`).  Therefore the genuine massive
3D taste doublet does **not** force the protocol verdict to INCONCLUSIVE: the
reported `m=0.5` finite-range spaces have zero odd nullity with order-one gaps.
It does force a scope correction: massive 3D is a numerical bounded FAIL only,
not an analytic no-go for all local/exponentially quasi-local charges.

Remaining routes are: nonanalytic-in-coupling or strong-coupling charges;
massive-3D matrix symbols beyond `R=4`, including uncontrolled quasi-local
tails; interactions with number-nonconserving or higher-body leading terms;
gauge-mediated interactions; singular resonance-supported dressings; and
conserved charges with zero one-particle action.  The last class cannot satisfy
the momentum PASS slope, and charged additions to a momentum are not a rescue
for these U(1)-invariant laws because U(1) averaging retains the neutral
one-particle action.  Exact translation and shift eigenvalues remain
group-valued lattice/taste symmetries; a local additive logarithm is not
supplied.

## No-go discipline gate

- **N1:** eight distinct routes were separated.  `ATTEMPTED`: (i) scalar
  collision invariants via Schur/Spohn, closing the universal-slope route in
  2D and massless 3D; (ii) the massive-3D matrix/taste route, closed only in
  the sampled `R<=4` spaces; (iii) direct finite-range extension, with
  order-one gaps through the stated maxima; (iv) exact-cluster dressing of the
  natural `P_x`, obstructed on `6x6,N=2`; (v) the exact group-valued
  translation/shift route, which supplies no local additive logarithm.
  `RULED OUT BY TARGET DEFINITION`: (vi) zero-one-particle-action charges
  cannot supply the required slope; (vii) charged additions under the present
  U(1)-invariant laws average to the same neutral action.  `UNTESTED AND
  EXCLUDED FROM THE CLAIM`: (viii) strong/nonanalytic coupling and
  number-nonconserving/higher-body-leading interactions.  Massive-3D
  quasi-local tails beyond `R=4` are explicitly unclosed rather than counted
  as a failed route.
- **N2:** no count of independent walls is claimed.  Massive-3D range,
  strong/nonanalytic coupling, and alternative interaction body/number class
  are domain boundaries, not asserted pairwise-independent obstructions.
- **N3:** explicit hidden premises are regular coupling expansion, bounded
  `P_1`, asymptotic clustering, C1 one-particle symbols, regular nonzero
  same-sector amplitudes, and the finite sampled basis.
- **N4:** RN L2 and Spohn close only the scalar residual; the Schur/cover and
  forward-amplitude steps are separately required for staggered sectors.
- **N5:** one-particle matrix action and on-shell two-particle scattering were
  tested; full many-particle, thermodynamic, strong-coupling, and all-range
  massive-3D resolutions were not.
- **N6:** discrete translations provide group-valued momentum but no local
  additive logarithm; this is an out-of-class nonlocal route, not closure.
- **N7:** the strongest counter-route is a massive-3D `2x2` multiplicity-space
  quasi-local invariant beyond `R=4` or nonanalytic in coupling.  It defeats an
  unrestricted theorem, but lies outside the honestly stated numerical range.
- **N8:** RN L2 left matrix tastes open; S1 analytically closes the
  universal-slope route in 2D and massless 3D and numerically narrows, but does
  not analytically close, massive 3D.

## Strongest correct statement

For either stated nonzero density interaction, any regular coupling-analytic local or exponentially quasi-local conserved charge with a nonzero taste-universal one-particle momentum slope must satisfy the matrix Born collision intertwiner.  After shift averaging, explicit sector sewing and generic same-sector forward-amplitude nonvanishing reduce that necessary condition to Spohn's scalar collision-invariant obstruction in `d=2` for every finite mass and in `d=3,m=0`, so no such momentum exists there; at the massless cone, C1 regularity excludes the `a omega` cusp.  In `d=3,m=0.5` the surviving `2x2` multiplicity-space problem has no odd null vector in the sampled matrix-valued spaces through `R=4`, with order-one gaps and independent controls, but no all-range or quasi-local theorem is proved.  Thus the FIXED protocol's **bounded FAIL (momentum only)** is confirmed, while strong coupling, nonanalytic families, higher-body/number-nonconserving or gauge-mediated interactions, zero-one-particle-action charges, and massive-3D quasi-local tails beyond the tested range remain open.
