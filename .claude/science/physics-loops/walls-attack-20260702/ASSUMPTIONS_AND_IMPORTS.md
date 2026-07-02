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
