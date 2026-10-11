# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed K1 answer is **NO**.  Under the registered full quadratic
linearized-gauge-restoration definition, the exact count is

\[
N_{\rm tune}(\mathbb Z^4)=3+(9-1)=11.
\]

This is an operator-codimension count.  The supplied one-loop calculation
also shows a nonzero obstruction, and in its chosen coordinates all three net
mass coefficients and all nine kinetic coefficients are nonzero.  It does not,
however, prove that a single loop has generated eight basis-independent
directions, nor that every possible W(B4)-covariant stress has this cost.

## 1. Form enumeration, gauge combination, and TT reduction

- **Confirmed exactly.**  An independent character calculation gives three
  W(B4)-invariant mass forms and nine W(B4)-invariant two-derivative forms;
  independent polynomial coefficient ranks show the named forms span those
  spaces (`referee_checks.py:31-52`, `referee_checks.py:85-96`,
  `referee_checks.out:1-2`).  This agrees with the worker
  (`K1_report.md:32-43`) and K-ana (`C3_K-ana_report.md:76-90`).
- The continuous O(4) subspace has dimension four.  The mass gauge map has
  rank three.  The kinetic gauge map has rank eight and unique null vector
  proportional to `(1,-2,2,-1,0,0,0,0,0)`, i.e.
  `EH = (F1-2F2+2F3-F4)/4`.  Its O(4) and anisotropic image ranks are three and
  five (`referee_checks.py:102-185`, `referee_checks.out:3-7`).  This independently
  confirms the earlier referee result (`C3_K_referee.md:11-19`).
- The exact restriction ranks are two for masses and four for kinetic forms,
  of which one is O(4)-invariant (`referee_checks.py:188-240`,
  `referee_checks.out:8-9`).  Thus `11` is the full gauge-restoration
  codimension, while `5 = 2 + (4-1)` is the direct TT-restriction count.
- **Correction.**  The five-dimensional Euclidean TT space used by the code is
  not “the two physical polarisations”: `TTbasis` explicitly returns a
  five-vector basis (`forms.py:63-81`).  Moreover, off-axis TT/longitudinal
  mixing lets A3, A4 and other gauge-breaking terms enter the physical Schur
  complement after masses are removed (`C3_K-ana_report.md:297-301`).  The
  number five is therefore a valid algebraic restriction count, not an
  established sufficient set or a rigorously demonstrated two-helicity
  physical floor.

## 2. One-loop calculation

- The implemented couplings are stated sufficiently to reproduce the code:
  the fermion uses a link-averaged inverse-square-root vielbein and densitized
  fields (`loop_fermion.py:1-15`), while the photon uses the corner-metric
  Maxwell action with h-independent gauge fixing (`loop_photon.py:1-11`).
- The fermion bubble numerator is correct.  An explicit 4-by-4 Euclidean gamma
  trace agrees with the reduced scalar expression to `2.2e-16`
  (`referee_checks.py:255-296`, `referee_checks.out:11`).  Minor documentation
  correction: the expression called `tr[...]` in `loop_fermion.py:8-10` is the
  spin trace divided by four; the external cosine and log-determinant factors
  restore the coded normalization.
- The cosmological counterterm is normalized correctly.  If the loop tadpole
  is `t tr h`, `-2t sqrt(det(1+h))` cancels it and shifts the local quadratic
  coefficients by `(t/2,t/2,-t/4)`, exactly as the code applies
  (`loop_fermion.py:111-117`, `referee_checks.out:12`).
- Representative reruns reproduce the supplied artifacts.  At `L=16,m=0.5`
  the fermion rerun gives tadpole `0.436447040`, raw masses
  `(-0.405311434,-0.356306728,+0.040070156)`, and the same nine kinetic
  coefficients (`referee_checks.out:13-16`; compare
  `loop_fermion_test3.out:1-5`).  At photon `L=8`, the loop masses and kinetic
  coefficients are reproduced, both q-squared Weyl combinations vanish, and
  an independent constant-metric determinant agrees in the masses to
  `8.7e-11` (`referee_checks.out:17-20`; compare
  `loop_photon_test.out:1-2` and `photon_q0_test.out:1`).
- The high-volume convergence is adequate for nonzeroness.  Fermion `L=64` to
  `80` changes kinetic coefficients by `2.8e-4` of the largest, and photon
  `L=24` to `32` by `7.2e-4`; the smallest named QED-total coefficient at the
  quoted point is still `4.259e-4` (`count.out:21-32`, `count.out:73-85`,
  `referee_checks.out:21-24`).
- The exact photon U(1) kernel test, fermion zero-momentum current cancellation,
  W(B4) covariance and evenness rerun cleanly (`ward_checks.out:1-8`).  The
  photon Weyl mass and q-squared identities are also satisfied
  (`count.out:73-85`).  The fermion check is only at zero external photon
  momentum; it is not a general gravitational Ward identity.  The latter is
  intentionally violated by the reported masses and non-EH kinetic vector
  (`K1_report.md:126-143`).
- **Correction: no literal staggered metric coupling was computed.**  Dividing
  the naive determinant by four is exact only before the off-diagonal
  vielbein spoils spin diagonalisation.  The worker says this explicitly
  (`K1_report.md:61-67`).  It is a rooted-naive four-taste proxy, not the
  one-component staggered action named in the fixed readout.
- **Correction: the quoted QED total is placement/scheme specific.**  The
  fermion treats all h components as site fields (`K1_report.md:61-64`), while
  the photon places off-diagonal components at plaquette centres
  (`K1_report.md:68-70`).  Before the masses are tuned, derivative field
  redefinitions shift q-squared coefficients by the mass differences
  (`C3_K-ana_report.md:150-162`).  The total coefficients, the `0.84/4.9/0.15`
  norm diagnostics, and the factor-three Euclidean-TT spread are valid only in
  the chosen conventions; they are not placement-independent observables.
- The calculation is the one-loop free determinant of each QED sector,
  `O(e^0)`.  It does not include the interaction corrections first appearing
  at higher loop order; the worker correctly discloses this
  (`K1_report.md:197-203`).  This does not undo the displayed one-loop
  obstruction, but “interacting QED” must not be read as an `O(e^2)` result.

## 3. Doubler-symmetry zero

- **Confirmed, with scope.**  The site phase on a hop in direction `nu` and
  gamma conjugation in direction `a` produce exactly the two reflection signs
  acting on `h_{a nu}` for every `(mu,a,nu)`
  (`referee_checks.py:243-252`, `referee_checks.out:10`).  The direct numerical
  test is at `10^-17` for the fermion and fails at order `10^-2` for the photon
  (`doubler_check.out:1-5`).  In the named basis this forces the fermion-sector
  coefficients of F2, F3 and A4 to vanish, as observed
  (`count.out:21-26`).
- The zero belongs to the fermion determinant with that naive-vielbein
  coupling.  It is not a symmetry of the photon sector or of the complete
  h-dependent QED measure.  Thus `K1_report.md:153-157` and
  `K1_report.md:160-163` should be read together: photon and mixed effects can
  populate those forms, so the structural zero does not lower the full count.

## 4. Count and the meaning of “generated nonzero”

- **The registered count survives h placement:** the target subspace has
  codimension `3+8=11`, and an invertible derivative field redefinition only
  moves coefficients between the already-counted mass and kinetic blocks.  It
  cannot change that total codimension.  Once all mass coefficients vanish,
  the mass-proportional placement shifts vanish as well
  (`C3_K-ana_report.md:150-162`; `referee_checks.out:9`).
- In the worker's fixed coordinates, all three combined net mass coefficients
  and all nine named kinetic coefficients are numerically nonzero; the values
  are independently reassembled in `referee_checks.out:21-24` and agree with
  `count.out:99-109`.  The induced vector is not EH-shaped, and it has a
  nonzero anisotropic TT restriction.  This is enough for the fixed K1 answer
  `N_tune>2`.
- **Correction to the stronger wording:** a single one-loop coefficient vector
  does not “generate eight independent quotient directions” in a
  basis-independent sense.  Nonzero coordinates can be changed by a basis
  choice, especially while masses remain.  What is exact is the eleven-fold
  codimension and the absence of a protecting identity in this chosen
  implementation; what is numerical is one non-EH vector with every named
  coordinate nonzero.
- `5` is retained only as the Euclidean-TT restriction count.  Because that
  restriction omits mixing and does not isolate the two Lorentzian helicities,
  it should not be advertised as a proved physical floor.  The conservative
  implementation-level consequence is nonetheless strictly more than two:
  the two TT mass conditions plus at least one nonzero kinetic anisotropy.

## 5. Comparison with P0, F2, and R2

- **P0:** its two established tunings are the two TT shear masses; its speed
  count was explicitly unresolved (`PRICE_NOTE.md:71-72`,
  `C3_K_referee.md:64-70`).  K1 answers the newly registered, broader full
  quadratic gauge-restoration count.  Saying P0's old “2” is globally
  incomplete is too broad; K1 establishes the extra cost for this W(B4)
  operator count and chosen couplings.
- **F2:** exact W(B4) symmetry at `xi=1` removes rank-two dimension-four matter
  speed splittings (`C4_F2_referee.md:31-35`).  That is consistent with K1:
  it does not force a rank-four h effective action into the unique EH
  direction.  F2's overall verdict was NOT CONFIRMED and its own comparison to
  a two-tuning P0 was rejected because P0's speed sector was then open
  (`C4_F2_referee.md:37-42`, `C4_F2_referee.md:56-58`).
- **R2:** the referee-confirmed local speed codimension in the tested Z3
  rank-two models was three (four without P/T), but the overall R2 lane stayed
  INCONCLUSIVE (`TESTS.md:749-759`).  This is qualitatively consonant with K1's
  three anisotropic TT restrictions, not an independent validation that K1's
  TT number is the physical tuning count.
- The unrefereed K2 report itself exhibits the important escape in scope:
  exact O(kappa) lattice diffeomorphism coupling may exist and the alleged
  obstruction enters only later (`K2_report_unrefereed.md:206-221`).  It cannot
  be used as authority, but it reinforces why K1 is a bounded one-loop
  implementation result rather than a universal grid no-go.

## 6. Verdict and strongest correct statement

**CONFIRMED WITH CORRECTIONS.**  Against the fixed K1 definition, lane K is
correctly answered **NO**: the exact W(B4) quadratic operator count is
`N_tune(Z4)=11`, consisting of three mass conditions after the separate
cosmological-tadpole tuning and eight kinetic conditions that reduce a
nine-dimensional kinetic space to the one-dimensional EH line.  The chosen
photon plus rooted-naive-vielbein calculation supplies a robust non-EH
one-loop example with every named coefficient nonzero, so `N_tune>2` is not in
doubt for that implementation.  The strongest correction is one of scope:
`11` is the registered operator codimension, not eight independently spanned
radiative directions and not a theorem for every W(B4)-covariant stress; the
actual staggered coupling and interaction corrections were not computed, and
`5` is only the `2+3` Euclidean-TT restriction rank, not a demonstrated
two-helicity physical floor.
