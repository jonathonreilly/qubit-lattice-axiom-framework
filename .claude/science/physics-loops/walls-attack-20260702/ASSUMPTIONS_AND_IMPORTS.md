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
