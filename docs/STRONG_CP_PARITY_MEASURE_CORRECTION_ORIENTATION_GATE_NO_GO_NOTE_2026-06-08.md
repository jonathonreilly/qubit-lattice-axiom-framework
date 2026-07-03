# Strong-CP Parity Measure Correction And Orientation Gate

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/strong_cp_parity_measure_orientation_gate_2026_06_08.py`](../scripts/strong_cp_parity_measure_orientation_gate_2026_06_08.py)
**Cached log:**
[`logs/runner-cache/strong_cp_parity_measure_orientation_gate_2026_06_08.txt`](../logs/runner-cache/strong_cp_parity_measure_orientation_gate_2026_06_08.txt)

## Statement

The runner verifies a correction and a narrowed gate for the gauge-side
strong-CP angle.

1. The lattice topological-charge slot
   `Q[F] = epsilon^{ijk} F_{0i} F_{jk}` is determinant-odd under the
   spatial cubic point group `O_h`: `Q[R.F] = det(R) Q[F]`.
2. The lattice sum does not add a second determinant sign. It is a relabeling
   of sites, and the continuum volume measure is `|det R| = 1`. Therefore an
   `O_h`/parity-invariant color action cannot contain a nonzero coefficient of
   this determinant-odd slot.
3. Proper rotations alone do not forbid the slot; only the improper/parity
   elements do.
4. The local `Cl(3,0)` pseudoscalar line has the same determinant character
   under `O_h`. That does not itself create a gauge action term, but it blocks
   the absent-source shortcut: the baseline does not prove that the color action
   has zero coupling to the lattice-orientation character.

So this note does **not** solve strong CP. It sharpens the residual:
`theta_gauge = 0` follows from a parity-invariant color action, but that
parity-invariant action class is not forced by the minimal axioms or by the
checked vectorlike/color-reality facts here.

## Boundary

This note does not claim `theta_gauge != 0`, does not consume the empirical
smallness of strong CP, does not derive the gauge action, and does not transfer
the mass-side determinant-reality mechanism to the gauge side. It also does not
claim that a future retained gauge-action derivation could not force the
parity-even action class. Such a derivation would retire this gate.

The mass-side `arg det(M_q)` facts remain cited context from the strong-CP
operator-basis/mass-orientation notes, not a new consequence of Record. Record
does not supply a mass circulant, gauge action, topological sector weighting, or
theta normalization.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  for the cubic `Z^3` lattice and one-qubit operator algebra baseline.
- [`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md)
  for the determinant-character action on the local `Cl(3)` pseudoscalar line.
- [`STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_BOUNDED_NOTE_2026-05-26.md)
  for the earlier epsilon-pseudotensor sign bridge; this note adds the explicit
  no-measure-cancellation correction.
- [`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)
  for the prior gauge-side obstruction frame.
- [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
  for the separate mass-side determinant orientation context.

## No-Go Discipline Gate

**Gate result:** pass for the narrowed gate; fail for any broader "no future
strong-CP route exists" claim, which is not shipped.

- **N1 alternative routes:** reflection positivity, reality/positivity/CPT,
  determinant-reality transfer, pure proper-rotation invariance, and absent
  P-source reasoning do not force `theta_gauge = 0` under the cited notes and
  runner checks. A retained derivation of a parity-even gauge action remains
  open.
- **N2 wall independence:** the parity-even action-class gate is distinct from
  the mass-determinant orientation facts and from reflection-positivity/reality
  route pruning.
- **N3 hidden-wall scan:** the hidden admission would be "the color action is
  parity-even." This note makes it explicit as the open gate.
- **N4 residual matching:** the residual is the gauge-side color-action parity
  gate, not the mass-side determinant phase residual.
- **N5 rhetoric audit:** "not forced" means not forced by the checked parity,
  vectorlike, determinant-character, reality, positivity, CPT, or RP routes. It
  does not mean impossible.
- **N6 partial-closure scan:** an independent gauge-action derivation excluding
  the determinant-odd slot would retire this gate without a new axiom.
- **N7 steelman:** vectorlike color and Wilson parity invariance are strong
  reasons to expect a parity-even color action. The runner accepts that as a
  motivation, but not as a derivation of the full action class.
- **N8 cross-cycle echo:** this matches prior strong-CP action-class notes:
  clean local symmetry checks prune routes, while the un-derived gauge-action
  class remains the residual.

## Forbidden-Imports Check

No external empirical value, fitted selector, new axiom, primitive, or audit
verdict is consumed. Nelson-Barr/parity and Vafa-Witten style arguments are
context only; the runner performs finite `O_h`, Wilson-action, chirality,
circulant-determinant, and pseudoscalar-character checks.

## Validation

Run:

```bash
python3 scripts/strong_cp_parity_measure_orientation_gate_2026_06_08.py
```

Expected: `TOTAL: PASS=7 FAIL=0`.
