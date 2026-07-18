# Stationary Dressed Reservoir / Shifted Green Profile

Date: 2026-07-17

Authority: none

Audit: unset

Runner: `scripts/stationary_dressed_reservoir_shifted_green_profile_2026_07_17.py`

Test contract: a numerically selected stationary dressed one-excitation
eigenstate on L=3,...,9; the exact shifted-Laplacian resolvent identity
conditional on the tested eigenpair equations; comparison with Cycle216's
3 L^+ block; the theta=0 parameter endpoint; held-out L=9; and explicit
claim-boundary and supplied structure inventory controls.

## Result

For every tested finite periodic volume L=3,...,9, the runner numerically
selects a normalized eigenpair of the closed local reservoir-plus-field
unitary with nonzero reservoir and field basis-component squared-norm weights.
The eigenpair residual is below the runner tolerance at all seven sizes.  This
is evidence for the selected finite matrices and selection rule, not a general
existence theorem outside the tested sizes.

After the uniform scalar component is separated algebraically, the nonuniform
scalar field satisfies

\[
 \phi_\perp=q\left[-\frac12\rho
 +i\sin\omega_L\,3(L-\mu I)^{-1}\rho\right],
 \qquad \mu=6(1-\cos\omega_L),
\]

on the declared zero-mean subspace.  Here
\(\rho=\delta_0-|\Lambda|^{-1}\).  The normalized-tail ratio uses no fitted
Green coefficient:

\[
 \frac{\phi_\perp+(q/2)\rho}{i q\sin\omega_L}
 =3(L-\mu I)^{-1}\rho.
\]

The finite-size observations are exactly L=3,...,9.  L=3,...,8 are the
declared training sizes and L=9 is held out.  The measured shifted-profile
ratio decreases across that tested sequence, and its held-out L=9 value is
below \(7.1\times10^{-4}\).  No law beyond those volumes is inferred.

This is a closed-unitary stationary dressing result.  There is no host-side
source renewal.  It is not physical energy, not gravity, not a Hamiltonian or
stress tensor, and the eigenphase is not a rate or clock.

## Closed local update

Use one active site-local reservoir M2 at the source cell and six directional
field M2 per lattice cell.  Work in the conserved one-excitation sector.  Let
\(C\) be the Cycle214/215 field coin, \(S\) its one-edge directional stream,
\(|r\rangle\) the reservoir excitation, and \(|s_0\rangle\) the uniform scalar
field excitation at the source cell.  The supplied local conjugate exchange is

\[
 V_\theta=\exp[-i\theta T],\qquad
 T=|r\rangle\langle s_0|+|s_0\rangle\langle r|,
\]

with supplied \(\theta=\kappa m\), \(\kappa=0.8\), and
\(m=-3\tan(\beta/2)\) at \(\beta=-0.3\).  The closed update is

\[
 U_\theta=S V_\theta (I_r\oplus C).
\]

The runner checks unitarity, norm preservation, and one-step radius-one
support.  The reservoir is a degree of freedom in this sparse one-excitation
update, rather than a value reinserted on every iteration.

## Exact eigenpair selection rule

For each L and each requested phase sign, sparse shift-invert uses target

\[
 \exp[\mathord{\pm} i\theta/L^{3/2}].
\]

Exactly three eigenvalues are requested.  Among returned eigenvalues with the
requested nonzero phase sign, the runner chooses the eigenvector with maximum
reservoir squared-norm weight.  It normalizes that vector and fixes its
otherwise arbitrary common phase by making the reservoir amplitude
real-positive.  This algorithmic rule, including the target and the number of
returned candidates, is supplied structure.  It is not a derived spectral
uniqueness theorem.

For the selected positive branch, the reservoir squared-norm weight lies
inside the declared interval \((0.45,0.48)\) at every tested size.  Applying
one update multiplies the eigenvector by one common phase, so every
basis-component squared norm is stationary.  That statement does not invoke
a Born or occurrence rule.

The observed dimensionless ratio
\(\omega_L L^{3/2}/\theta\) lies inside the declared acceptance window
\((0.96,0.99)\) for L=3,...,9.  This is only a tested finite-volume
observation.  In particular, \(\omega_L\) is not assigned energy or rate
semantics.

## Direct eigenpair-to-q controls

Write the selected normalized eigenvector as reservoir amplitude \(a\) plus
field amplitude \(f\), and define

\[
 b=\langle s_0|Cf\rangle,
 \qquad
 q=(\cos\theta-1)b-i\sin\theta\,a.
\]

The runner does not merely insert this \(q\) into a fitted profile.  At every
tested L it directly checks both block equations

\[
 \lambda a=\cos\theta\,a-i\sin\theta\,b,
\]

and

\[
 (\lambda-U_f)f=q\,U_f|s_0\rangle,
 \qquad U_f=SC,
\]

as well as the supplied coin identity

\[
 C|s_0\rangle=|s_0\rangle.
\]

Thus \(q\) is the field amplitude produced by the supplied local vertex for
the selected eigenvector.  It is not a separately supplied classical source
strength.  It is also not invariant under eigenvector normalization or common
phase: if \(|\Psi\rangle\mapsto c|\Psi\rangle\), then
\(\phi\mapsto c\phi\) and \(q\mapsto cq\).  The runner's real-positive
reservoir convention fixes one representative of the normalized eigenvector;
the normalized-tail ratio above is invariant under the joint scaling and
rephasing.  This narrower ratio invariance, not an intrinsic value of \(q\),
is the normalization result.

## Scalar profile identity and uniform component

Cycle215's scalar-row identity gives, at each nonflat momentum,

\[
 \langle s|(\lambda-U_f(k))^{-1}U_f(k)|s\rangle
 =\frac{\gamma(k)\lambda-1}
 {\lambda^2-2\gamma(k)\lambda+1}.
\]

With \(L(k)=6[1-\gamma(k)]\),
\(\lambda=e^{i\omega_L}\), and
\(\mu=6(1-\cos\omega_L)\), the row is

\[
 -\frac12+i\,\frac{3\sin\omega_L}{L(k)-\mu}.
\]

The uniform component is not silently discarded.  Its predicted spatial mean
is tested directly:

\[
 \overline\phi
 =\frac{q}{L^3}
 \left(-\frac12-i\frac{3\sin\omega_L}{\mu}\right).
\]

Only after that equality is checked is the mean removed to form
\(\phi_\perp\) for the zero-mean Cycle216 comparison.  Across L=3,...,9 the
runner requires the eigenpair residual, both block-equation residuals,
\(C|s_0\rangle-|s_0\rangle\), the explicit uniform-component residual, the
full nonuniform-profile residual, and the normalized-tail residual all to lie
inside their declared numerical tolerances.

## Finite comparison with Cycle216

Cycle216's exact static scalar block is \(3L^+\) on the zero-mean source
domain.  This stationary dressed route instead gives
\(3(L-\mu I)^{-1}\) at finite L.  On nonzero modes,

\[
 3(L-\mu I)^{-1}-3L^+
 =3\mu(L-\mu I)^{-1}L^+.
\]

Two different quantities are reported and must not be conflated:

1. the measured source-specific profile ratio
   \(\|3(L-\mu I)^{-1}\rho-3L^+\rho\|_2/
   \|3L^+\rho\|_2\); and
2. the uniform relative operator-norm bound
   \(\mu/(\ell_{\min}-\mu)\) on the full zero-mean subspace.

The first is a ratio for this particular \(\rho\).  The second controls all
vectors in the declared zero-mean domain and is generally looser.  At every
tested size \(0<\mu<\ell_{\min}\), so the tested shifted operator has no
nonzero-mode pole.  The runner verifies that the source-specific ratio is no
larger than the operator bound, that it decreases at each successive tested
L, and that the held-out L=9 ratio is below \(7.1\times10^{-4}\).

This earns a finite tested connection to Cycle216.  It does not identify the
shifted resolvent with gravity, establish a continuum result, or turn the
source-specific ratio into an operator norm.

## Zero-mode, conjugate-branch, covariance, and domain controls

- The comparison source \(\rho=\delta_0-|\Lambda|^{-1}\) has zero sum and a
  zero Fourier coefficient at \(k=0\).
- The dressed eigenvector has the explicit nonzero uniform scalar component
  tested above; zero-mode subtraction is used only for the comparison domain.
- The scalar source is numerically orthogonal to both \(U=+1\) flat
  directions and both \(U=-1\) flat directions at the tested generic
  momentum.
- The negative branch is independently selected and checked for opposite
  eigenphase, equal reservoir squared-norm weight, and its own eigenpair
  residual at every L=3,...,9, not only at endpoint sizes.
- The source-centered update and selected dressed state are checked under all
  24 proper-cubic frames.
- All 27 source positions on the L=3 torus form a translated covariant defect
  family.  A single defect member is not called translation invariant.
- The lawful domain requires L>=3, one active reservoir M2, six field M2 per
  cell, and the one-excitation sector.  Aliased, mistyped, and wrong-sector
  fixtures are rejected.

The theta=0 parameter endpoint is a parameter-setting control, not a deletion
theorem.  Externally setting the supplied \(\kappa=0\), or selecting the
supplied family member \(\beta=0\), gives \(\theta=0\) and leaves a pure
reservoir excitation stationary.  The test neither derives why either
parameter should be selected nor deletes a term from a candidate law.  The
separate zero-shift mathematical comparator equals Cycle216's
\(3L^+\rho\); a decoupled reservoir is not claimed to generate that field.

## Acceptance and supplied structure inventory

The numerical acceptance inventory is fixed in the runner:

1. tested sizes L=3,...,9, with L=3,...,8 declared training and held-out L=9;
2. eigenpair and stationary squared-norm tolerances stated by each check;
3. reservoir squared-norm interval \((0.45,0.48)\);
4. phase-ratio interval \((0.96,0.99)\);
5. exact-profile, normalized-tail, gate-equation, coin, uniform-component,
   covariance, and conjugate-branch residual tolerances stated by each check;
6. source-specific profile-ratio monotonicity on this seven-size list and the
   held-out upper threshold \(7.1\times10^{-4}\).

These are acceptance thresholds for this runner, not physical constants or
statements about untested sizes.

Supplied:

1. the Cycle214/215 six-direction field coin, one-edge stream, and
   coin-vertex-stream ordering;
2. one active site-local reservoir M2 and the uniform scalar conjugate
   exchange;
3. \(\beta=-0.3\), the Cycle219 parameter conversion, and \(\kappa=0.8\);
4. finite periodic volume, source position, one-excitation preparation, and
   zero-mean comparison convention;
5. the exact shift-invert eigenpair selection rule stated above, including its
   target, three returned candidates, phase-sign filter, maximum-reservoir-
   weight choice, normalization, and phase convention;
6. the acceptance inventory above; and
7. Cycle216's stiffness/\(3L^+\) comparator.

Derived on that supplied finite problem:

1. the numerically selected closed finite-volume dressed eigenpairs and their
   stationary basis-component squared norms;
2. the direct gate-equation bridge to \(q\), conditional on those selected
   eigenpairs;
3. the exact local-coordinate plus shifted-Green normalized-tail identity and
   explicit uniform component;
4. the tested source-specific comparison with Cycle216 and the distinct
   zero-mean operator bound; and
5. proper-cubic covariance, translated-source family covariance, the theta=0
   parameter endpoint, negative-branch, held-out-size, and lawful-domain
   controls.

Not earned or attempted here:

No matter or contact update is implemented.  There is no interface to the
carried-source code, and there is no whole-compiler claim.

1. physical energy, Hamiltonian density, stress, gravity, source mass,
   eigenphase-as-rate, or clock normalization;
2. a matter Hilbert space or any matter or contact update, including the
   Cycle230 contact block;
3. a whole-compiler claim, physical-M2 compiler, or intertwiner with the
   Cycle230 coarse CAR cell;
4. any interface to the carried-source code: this fixed active reservoir is
   neither a carried source nor a moving source;
5. host-side renewal, retarded selection, radiation reaction, source recoil,
   moving-source transport, or many-excitation closure;
6. a physical preparation mechanism for the selected eigenvector or a result
   outside the tested finite matrices; and
7. occurrence, Record formation, a Born/probability rule, axiom change, or
   audit authority.

## Discipline and next step

This is a constructive finite-matrix result, not an impossibility or
minimum-content claim.  The shifted response is explicitly different from
exact \(3L^+\) at finite L, but no route-independent obstruction is inferred.
There is no axiom pressure.

The next scientifically separate task would need to supply an actual matter
or contact interface and test it without treating this reservoir-field block
as a whole compiler.  That task is outside this note.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status surface was edited.
