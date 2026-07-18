# Stationary dressed carried-source relative mode — 2026-07-17

**Status:** constructive finite-volume stationary dressed eigenmode of the
actual carried update, with a bounded scalar-shape comparison.

**Authority:** none

**Audit:** unset

## Question

Does the declared direct carried hard-core code admit a stationary dressed
mode when the matter carrier is allowed to move, rather than being replaced by
the fixed site-local reservoir used in
`STATIONARY_DRESSED_RESERVOIR_SHIFTED_GREEN_PROFILE_NOTE_2026-07-17.md`?

The tested domain is one matter carrier and

\[
Q=N_e+N_f=1,
\]

on a finite periodic cubic lattice.  Translation invariance is reduced at
total momentum \(K=0\), leaving the field-minus-matter relative coordinate.
The executed update contains the full matter coin, field coin, local exchange,
matter stream, and field stream.  No source pinning or host-side renewal is
used.

## Declared carried domain and reduction

Before reduction the direct one-matter state has amplitudes

\[
e_d(x),\qquad f_{d_m d_f}(x,y),
\]

where \(e\) is the internally excited/no-field summand and \(f\) is the
ground-matter/one-field summand.  At \(K=0\), write

\[
e_d(x)=L^{-3/2} e_d,
\qquad
f_{d_m d_f}(x,y)=L^{-3/2} f_{d_m d_f}(r),
\qquad r=y-x.
\]

The full periodic direct domain has dimension
\(6L^3+36L^6\).  The exactly invariant \(K=0\) block has dimension

\[
6+36L^3.
\]

This is a symmetry reduction of the actual direct carried state, not a
fixed-defect replacement.  At \(L=3\), the runner constructs the complete
\(26406\times978\) basis-spanning \(K=0\) lift \(E_0\).  It has 26406
nonzero entries and obeys

\[
\lVert E_0^\dagger E_0-I\rVert=2.0832\times10^{-14},
\qquad
\lVert U_{\rm full}E_0-E_0U_{K=0}\rVert=0.
\]

This is the isometry/intertwiner control behind the exact reduction claim.
A separate random \(L=3\) relative state was also lifted and advanced by the
previously tested dictionary-form periodic carried-state executor.  Its
residual was \(2.00\times10^{-16}\), with global-\(Q\) residual
\(4.44\times10^{-15}\); that random check is corroboration, not the basis for
the exactness claim.

## Full update

The sparse relative update is

\[
U_{\rm carry}(0)
=S_f S_m V
\left(C_m\oplus(C_m\otimes C_f)^{\oplus L^3}\right).
\]

Here:

- \(C_m\) is the Cycle-219 common matter coin at \(\beta=-0.3\);
- \(C_f\) is the Cycle-214 six-direction field coin;
- \(V\) is the direction-preserving exchange between \(e_d\) and the
  field-scalar component of \(f_{d d_f}(0)\), with supplied
  \(\theta=0.8m=0.3627245233399082\);
- \(S_m\) moves the matter direction and changes
  \(r\mapsto r-\delta_{d_m}\);
- \(S_f\) moves the field direction and changes
  \(r\mapsto r+\delta_{d_f}\).

The \(L=3\) relative matrix has dimension 978.  Its unitarity residual is
below \(10^{-13}\), and its action agrees with an independent relative-array
execution below \(10^{-13}\).  The basis-spanning test additionally assembles
the full 26406-dimensional logical one-matter \(Q=1\) periodic matrix.  No
full \(2^{18L^3}\) physical tensor-space matrix is assembled here.

No contact layer is applied in this runner.

## Eigenpair selection

The update itself contains no eigenvalue target.  Numerically, a six-candidate
shift-invert neighborhood is requested near the supplied selector phase
0.365.  The primary selector takes the four closest candidates and chooses
the one with maximum excited-sector squared norm, normalizes it, and gives it
a common phase for which its overlap with the uniform excited direction is
real-positive.  This selection procedure is an explicit analysis input, not
candidate law content.

Training sizes were declared as \(L=3,4,5,6,7\).  Held sizes were declared as
**held L=8,9**.

The selected source-bright branch is:

| \(L\) | held | eigenphase | excited squared-norm weight | field squared-norm weight |
|---:|:---:|---:|---:|---:|
| 3 | no | 0.37277048526221035 | 0.5551299430158378 | 0.4448700569841622 |
| 4 | no | 0.37315256916064005 | 0.5511360498548953 | 0.4488639501451047 |
| 5 | no | 0.36455096573371315 | 0.5618547087233885 | 0.4381452912766115 |
| 6 | no | 0.3651736256931815 | 0.5609370875710045 | 0.4390629124289955 |
| 7 | no | 0.36284052191874117 | 0.5621421858789255 | 0.4378578141210745 |
| 8 | yes | 0.3632299688784465 | 0.5620559456220201 | 0.4379440543779799 |
| 9 | yes | 0.3621779656761907 | 0.5614620237756212 | 0.4385379762243788 |

Every eigenpair residual is below \(1.4\times10^{-15}\) in the direct run,
and \(|\lambda|-1\), \(N_e+N_f-1\), and both direct-sum block-equation
residuals are at numerical zero.  Thus the selected finite-volume state is a
stationary dressed eigenmode of the actual full carried update, not a
multi-tick recurrence inferred from a prepared source pulse.

For branch identity and selector stability, the held six-candidate
neighborhood is re-ranked at target phases 0.35, 0.365, and 0.37, using both
four and six candidates.  On held \(L=8,9\), all six re-rankings return the
same eigenphase and phase-agnostic eigenvector within \(3\times10^{-11}\).
The declared audit and acceptance inventory is:

- selector target window \([0.35,0.37]\);
- candidate counts 4 and 6;
- held eigenphase window \((0.36,0.375)\);
- held excited squared-norm window \((0.55,0.57)\); and
- held double-scalar contact-fraction minimum 0.96.

The exact source/field charge tested here is \(Q=N_e+N_f\).  It is not
physical energy and is not a gravitational source.

Scope tags used literally by the runner: total momentum K=0; all 24
proper-cubic frames; eigenphase is not a rate; not gravity.

## Coherent exchange balance

The stationary sector weights do not mean that the local exchange is idle.
For a coined eigenstate, the exact local decomposition is

\[
\Delta N_f
=\sin^2\theta\left(\lVert e\rVert^2-\lVert f_s(0)\rVert^2\right)
+2\sin\theta\cos\theta\,\operatorname{Im}\langle e,f_s(0)\rangle.
\]

The three displayed quantities below are the positive excited diagonal term,
negative field diagonal term, and coherent interference term.  They are
algebraic terms in \(\Delta N_f\), not separately executed processes:

| \(L\) | \(\Delta N_f\) | excited diagonal | field diagonal | coherent interference |
|---:|---:|---:|---:|---:|
| 3 | \(-1.67\times10^{-16}\) | 0.0698904246752716 | -0.027740917420315158 | -0.04214950725495658 |
| 5 | \(0\) | 0.07073706740650147 | -0.02621333646013065 | -0.044523730946370896 |
| 7 | \(-2.78\times10^{-17}\) | 0.07077326055503845 | -0.02584745731950958 | -0.04492580323552896 |
| 8 | \(-2.78\times10^{-17}\) | 0.07076240297429537 | -0.025929574425832203 | -0.044832828548463245 |
| 9 | \(-1.11\times10^{-16}\) | 0.07068762867939203 | -0.02567024584217756 | -0.04501738283721453 |

The cancellation is a coherent exchange balance.  The table does not assign
an incoherent process mixture and supplies no Born interpretation.

## Proper-cubic covariance

At total momentum \(K=0\), every proper-cubic frame maps the tested momentum
sector to itself.  The frame acts on the relative coordinate and on both
six-direction labels.  Direct tests give:

- 24/24 proper-cubic frames checked;
- the complete \(L=3\) sparse update-commutator residual below \(10^{-15}\);
- selected-state invariance below \(2.4\times10^{-15}\) for every
  \(L=3,\ldots,9\), including both held sizes; and
- randomized update-action covariance in all 24 frames separately at held
  \(L=8,9\), with maxima below \(3.0\times10^{-16}\).

Thus full operator-norm covariance is asserted only at \(L=3\); the held-size
extension is an action test plus selected-state invariance.  All are controls
of the tested \(K=0\) block.  Nonzero-total-momentum dispersion was not tested
here.

## Relative scalar comparison

To compare with scalar Green fixtures, project both the matter and field
direction labels onto the proper-cubic uniform direction:

\[
\phi(r)=\langle s_m|f(r)|s_f\rangle.
\]

This double-scalar projection is a supplied comparison coordinate; it is not
the entire field sector.  Three shape comparisons are kept distinct:

1. the residual-matched carried shifted comparator
   \(H_{\mu_{\rm carry}}\rho=3(L-\mu_{\rm carry}I)^{-1}\rho\), with
   `mu_carry` computed from the carried eigenphase;
2. the separate analytic fixed-reservoir shifted response
   \(3(L-\mu_{\rm fixed}I)^{-1}\rho\), using the fixed-reservoir eigenphase;
3. the Cycle216 zero-mean static fixture \(3L^+\rho\).

For the carried comparator the runner also records the pole margin
\(\ell_{\min}-\mu_{\rm carry}\).  It is positive at both held sizes, so the
declared zero-mean shifted comparator is pole-free there.  The actual
fixed-reservoir scalar state is not compared; only its separately derived
analytic shifted-response coordinate is used.

For each comparison, no Green coefficient is fitted.  The profiles are
mean-subtracted and unit-normalized, and the overlap is insensitive only to a
common phase.  The **contact-deleted tail** comparison removes the relative
origin entry from both arrays, subtracts the mean over only the remaining
entries, and unit-normalizes those masked arrays.  The deleted entry is not
reintroduced by the subsequent mean subtraction.

The held results are:

| \(L\) | contact scalar fraction | \(\mu_{\rm carry}\) | pole margin | contact-deleted overlap with carried shifted | with Cycle216 | with fixed shifted |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.9661818695952215 | 0.39147534668663075 | 0.19431109094027432 | 0.2821158729766802 | 0.3020612379973966 | 0.30207056682887057 |
| 9 | 0.9716262722212686 | 0.3892358197963468 | 0.07867529396569739 | 0.28718913497721305 | 0.32959978409869556 | 0.32961551760307395 |

On these sizes the fixed-reservoir shifted response and Cycle216 profile have
unit-shape overlap above 0.999999.  In contrast, the carried-shifted/Cycle216
overlap is 0.90855 at \(L=8\) and 0.79907 at \(L=9\), because
\(\mu_{\rm carry}\) is much larger than \(\mu_{\rm fixed}\).  The selected
carried mode has more than 96% of its double-scalar squared norm at relative
contact.  Its contact-deleted overlap is about 0.28 with the residual-matched
carried comparator and about 0.30--0.33 with the separate comparators.

Therefore the constructive result is a stationary carried dressed mode, plus
a quantitative statement that this selected branch and supplied projection
are localized and are not numerically identified with the three Green shapes on
the tested sizes.  This is not a claim that another branch, momentum sector,
projection, scaling regime, or multi-field completion cannot produce a Green
profile.  It is no no-go claim and creates no axiom pressure.

## Theta=0 parameter endpoint and lawful-domain controls

At \(\theta=0\), the pure uniform \(K=0\) excited-matter vector is an exact
eigenvector with inherited rest eigenphase
0.15113521805829505 and zero field squared norm after the update.  This is a
supplied theta=0 parameter endpoint, not a deletion theorem for a derived law.
It checks the parameter endpoint while the one-particle mass fixture remains
inherited.

The runner accepts only:

- periodic \(L\geq3\);
- six matter and six field directions;
- one matter and \(Q=1\);
- the selected \(K=0\) stationary branch.

It rejects an aliased \(L=2\) fixture, nonzero \(K\) passed to this branch,
mistyped direction alphabets, two-matter input, and \(Q=2\).

## Prior-art and novelty boundary

The fixed-reservoir stationary note already constructed an exact shifted
field-walk response for one active site-local reservoir and explicitly stated
that it had no matter or carried-source interface.  Cycle216 already supplied
the conditional static \(3L^+\) comparator.  Those results are used only as
bounded comparison surfaces.

The new content here is:

1. the exact \(K=0\) relative-coordinate reduction of the actual direct
   carried \(e/(g+f)\) code, supported by the basis-spanning \(L=3\)
   isometry/intertwiner;
2. source-bright stationary eigenpairs of its full coin/exchange/two-stream
   update through held \(L=8,9\);
3. exact coherent exchange balance in those eigenpairs;
4. the declared \(L=3\) operator and held-size action/state proper-cubic
   covariance controls;
5. held branch-identity stability under the supplied selector audit; and
6. the measured localization and residual-matched/separate Green-shape overlaps of the selected
   double-scalar relative profile.

No Thirring engine is used or extended.

## Supplied structure inventory

Supplied:

1. the declared direct carried one-matter \(Q=1\) hard-core code and its
   12 matter plus six field M2 per-cell basis injection;
2. \(\beta=-0.3\), the common Cycle-219 matter coin, the Cycle-214 field coin,
   coupling 0.8, and the coupling-times-mass angle map;
3. the direction-preserving local exchange and the
   coin--exchange--matter-stream--field-stream schedule;
4. finite periodic volumes, total momentum \(K=0\), and the relative-coordinate
   representation;
5. the six-candidate neighborhood, primary four-candidate selector, target
   0.365, audit window \([0.35,0.37]\), candidate counts 4 and 6, normalization,
   and common-phase convention;
6. training sizes \(L=3,\ldots,7\), held sizes \(L=8,9\), held eigenphase
   window \((0.36,0.375)\), excited-weight window \((0.55,0.57)\), and
   contact-fraction minimum 0.96;
7. the double-scalar and honest contact-deleted-tail comparison coordinates;
   and
8. the residual-matched \(\mu_{\rm carry}\), separate fixed-reservoir shifted
   response, and Cycle216 \(3L^+\) comparators, including their source,
   zero-mean, and pole-margin conventions.

Derived on the declared domain:

1. full-update stationary dressed eigenpairs with nonzero excited and field
   squared-norm weights;
2. exact \(Q\), unitary, block-equation, basis-spanning lift-intertwiner, and
   full-schedule residual controls;
3. nontrivial coherent exchange balance;
4. the scoped proper-cubic operator/action/state controls at \(K=0\);
5. held-size persistence, selector stability, and the displayed scalar-shape
   comparisons; and
6. the supplied theta=0 parameter endpoint.

Not earned:

1. physical energy, a Hamiltonian or transfer-generator identification,
   eigenphase-as-rate, clock normalization, stress, or a gravitational source;
2. gravity, a static field law, or a derivation of Cycle216 from the carried
   code;
3. equality of the carried tail with either comparison profile;
4. nonzero-\(K\) dispersion, localized center-of-mass stationarity,
   many-matter or many-field closure, or contact dynamics;
5. a full physical tensor-space matrix, a Cycle269 splice, or a whole
   physical-M2 compiler/intertwiner;
6. a Record, occurrence law, Born rule, axiom change, or audit authority.

## Disposition

The actual carried code does have a finite-volume stationary dressed
eigenmode.  On held \(L=8,9\), approximately 56% of its squared norm is in the
internal-excitation summand and 44% in the ground-plus-field summand, with
stationarity maintained by coherent exchange balance.  The tested
double-scalar mode is strongly localized in relative separation and is
quantitatively compared with the residual-matched carried shifted response,
the separate fixed-reservoir shifted response, and Cycle216 after honest
contact deletion.

The next constructive question is whether a different spectral branch,
nonzero-total-momentum limit, or enlarged field sector carries an extended
relative scalar response while preserving the same exact charge and
proper-cubic controls.  No axiom language is proposed.
