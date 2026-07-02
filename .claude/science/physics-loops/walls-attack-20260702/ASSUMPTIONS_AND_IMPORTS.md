# Assumptions and Imports

## Block04

**Artifact:** `docs/ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`  
**Runner:** `scripts/frontier_action_family_character_semigroup_discriminator_2026_07_02.py`  
**Output:** `outputs/frontier_action_family_character_semigroup_discriminator_2026_07_02.txt`

**Status:** bounded support only. No action is selected; no beta value is
selected; no emergent-time or record-composition bridge is established.

**Allowed source inputs read fully:**

- `docs/ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md`
- `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `docs/ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08.md`

**Conditional / unaudited citations:**

- The relocation note is cited conditionally for the scoped regulator-reading
  verdict, the `t = 2N_c/beta` normalization context, and the emergent-time
  generator open question.
- The ADM-2/global-SU(3) note is cited conditionally as context for the
  bi-invariant action-form class. It is not used as an authority closing ADM-2.

**In-runner certified inputs:**

- Wilson `I_n(beta)` is defined by the explicit positive Bessel series with a
  ratio-test tail bound, evaluated by `fractions.Fraction` interval arithmetic.
- Heat-kernel coefficients are defined in the note as `c_n=exp(-n^2 t/2)`;
  symbolic checks cover the `n^2` law and semigroup identity.
- Principal-angle Manton finite-window coefficients are bounded by rational
  interval arithmetic using a Machin-certified `pi` interval, polynomial moment
  identities, Taylor/Lagrange remainder bounds, and a finite Gaussian-tail sign
  certificate for the `c_1` lower bound.
- Wilson convolution non-closure is certified by bracketing the only possible
  `c_1`-matching Wilson `beta'` and separating the `c_2` fingerprint.

**Imports deliberately not used:**

- No literature theorem or numerical table is imported.
- No continuum-limit equivalence is used as a finite-beta selector.
- No record-production dynamics, time metric, action-source bridge, or
  emergent-time generator premise is assumed.
- No new axiom or primitive is introduced.

**Named next-attack premise only:**

If a later bridge proves additive composition of successive plaquette-record
accumulations, then the action kernel must be a one-parameter convolution
semigroup. This Block04 artifact names that premise and tests the three action
families against it; the record-composition bridge is not established here.

## Block09

**New bounded artifact:**

- `docs/SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md`
- `scripts/frontier_semigroup_closure_quadratic_condition_2026_07_02.py`
- `outputs/frontier_semigroup_closure_quadratic_condition_2026_07_02.txt`

**Role:**

- Self-adversarial sharpening of Block04's T5 premise. The exact `Z_5` witness
  proves that one-parameter convolution-semigroup closure alone selects the
  broad class `c_n(t)=exp(-t psi(n))`, not the heat-kernel subfamily.
- The missing named condition is `Q-gen`: `psi(n)=s n^2` for all modes. Its
  first-level check is exactly Block04's `c_2=c_1^4` discriminator within a
  semigroup class.

**In-runner certified inputs:**

- `theta_0=2*pi/5`, `psi(n)=1-cos(n theta_0)`, and
  `c_n(t)=exp(-t psi(n))`.
- Semigroup additivity is checked symbolically.
- Positivity is constructed directly on `Z_5` by
  `w_t=exp(t(M-I)) delta_0=exp(-t) exp(tM) delta_0`, with `M` the symmetric-step
  stochastic matrix; rational-time samples are certified by truncated series
  with exact remainder bounds.
- Fourier diagonalization of `M` on `Z_5` gives the stated characters exactly.
- The exact identity
  `4 psi(1)-psi(2)=2(cos(2*pi/5)-1)^2>0` certifies
  `c_2(t) != c_1(t)^4` for positive `t`.

**Imports deliberately not used:**

- No literature theorem is imported.
- No continuum or CLT premise is used.
- No Record bridge, action selector, new axiom, or new primitive is assumed.
- Block04's three-candidate conclusion is not changed: Wilson and
  principal-angle Manton remain non-semigroups at finite beta by Block04 T4.

## Block10

**New bounded artifact:**

- `docs/SINGLE_STEP_LOCALITY_EXCLUDES_QUADRATIC_GENERATOR_BOUNDED_NOTE_2026-07-02.md`
- `scripts/frontier_single_step_locality_excludes_qgen_2026_07_02.py`
- `outputs/frontier_single_step_locality_excludes_qgen_2026_07_02.txt`

**Role:**

- Sharpens Block09's `Q-gen` condition by proving that finite-step generators
  on `U(1)` are bounded and therefore cannot equal `s n^2` with `s>0`.
- Separates the finite `Z_N` bookkeeping fact from positivity: full step sets
  span the finite quadratic vector, but the tested exact matches
  `N=5,7,8,9,12` require signed weights.
- Proves that strict nearest-step locality on every finite `Z_N` fails the
  first `Q-gen` check by the exact deficit `4 sin^2(pi/N)`.

**Imports deliberately not used:**

- No literature theorem is imported.
- No continuum limit is used as authority.
- No Record bridge, action selector, new axiom, or new primitive is assumed.
- No horn of the extended-step / many-step-limit / rejected-bridge trichotomy
  is selected.

## Block13

**New bounded artifact:**

- `docs/EXACT_QGEN_NOT_POSITIVE_ON_ZN_WRAPPED_GAUSSIAN_CORRECTION_BOUNDED_NOTE_2026-07-02.md`
- `scripts/frontier_exact_qgen_wrapped_gaussian_correction_2026_07_02.py`
- `outputs/frontier_exact_qgen_wrapped_gaussian_correction_2026_07_02.txt`

**Role:**

- Closes the named finite positivity follow-up to Block10 for tested `Z_N`.
  The finite convolution semigroup `P_t=exp(tL)` is positive for all `t>=0`
  exactly when the off-diagonal entries of the symmetric circulant generator
  are nonnegative at the level needed here.
- Applies the small-time direction to the exact finite `Q-gen` generators:
  `N=5` has a certified negative entry at displacement `2` for
  `t_0=1/2000`, and `N=7` has one at displacement `2` for `t_0=1/5000`.
- Separates the positive finite Gaussian object from exact `Q-gen`: the wrapped
  Gaussian is positive by construction, while its `Z_5` characters have
  certified theta corrections at the sampled rational times.

**In-runner certified inputs:**

- The finite Markov positivity lemma is implemented with the Metzler shift
  construction and the explicit matrix-exponential remainder bound
  `|R_ij| < 2 t^2 ||L||_infty^2` when `t ||L||_infty <= 1`.
- For `N=5`, the runner uses Block10's
  `w_2=1-3 sqrt(5)/5`, the exact bound `sqrt(5)>223/100`,
  `||L||_infty<=10`, and certifies
  `(exp(t_0 L))_{j+2,j} <= -69/2000000`.
- For `N=7`, the runner uses the exact cubic for `2 cos(2*pi/7)` to certify
  `|L_2|>1/2`, `||L||_infty<=28`, and
  `(exp(t_0 L))_{j+2,j} <= -233/6250000`.
- For the wrapped Gaussian on `Z_5`, the runner evaluates the dual theta
  character ratio with truncated sums and Gaussian tail bounds, certifying
  nonzero deviations of `-log c_n(t)` from `(t/2)n^2` for
  `t in {1/5,1,2}` and `n in {1,2}`.

**Imports deliberately not used:**

- No literature theorem is imported.
- No all-`N` positivity obstruction is claimed.
- No Record bridge, action selector, new axiom, or new primitive is assumed.
- No wrapped-Gaussian correction outside the sampled rational `Z_5` points is
  promoted to a certified numerical claim.

## Block14

**New bounded artifact:**

- `docs/EXACT_QGEN_METZLER_VIOLATION_ALL_ODD_N_CLOSED_FORM_BOUNDED_NOTE_2026-07-02.md`
- `scripts/frontier_exact_qgen_metzler_all_odd_n_2026_07_02.py`
- `outputs/frontier_exact_qgen_metzler_all_odd_n_2026_07_02.txt`

**Role:**

- Upgrades Block13's tested `Z_5,Z_7` exact `Q-gen` positivity obstruction to
  a closed-form all-odd theorem: for every odd `N>=5`, the exact quadratic
  generator has `L_2<0`, so the finite Metzler condition fails.
- Fixes the Fourier sign convention explicitly: `hat L(k)=-psi(k)` and
  `L_j=-(1/N) sum_k psi(k) exp(2 pi i k j/N)`, giving characters
  `exp(-t psi(k))`.
- Separately records the even-`N` analogue under the stated one-copy
  self-inverse boundary-mode convention `{ -N/2+1, ..., N/2 }`.

**In-runner certified inputs:**

- The odd Dirichlet-kernel identity
  `S_j=(N/2)(-1)^j cos(pi j/N)/sin^2(pi j/N)` is verified against direct exact
  symbolic summation for `N=5,7,9,11,13` and all `1<=j<=N-1`.
- The odd `j=2` generator sign is checked exactly for odd `N=5..41`.
- The even convention gives
  `S_j=(N/2)(-1)^j/sin^2(pi j/N)`; this is verified against direct exact
  symbolic summation for `N=6,8,10,12,14` and all off-zero `j`, with `j=2`
  negativity checked for the same even values.

**Imports deliberately not used:**

- No literature theorem is imported.
- No source note other than the Block13 sibling is used as a load-bearing
  input.
- No Record bridge, action selector, horn selection, new axiom, or new
  primitive is assumed.
- No wrapped-Gaussian correction theorem beyond Block13's sampled data is
  added.
