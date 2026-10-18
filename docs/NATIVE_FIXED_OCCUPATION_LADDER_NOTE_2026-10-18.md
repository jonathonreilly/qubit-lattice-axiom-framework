# Native neutral-feature ladder at every fixed finite occupation

Status: bounded-support. The previous two-rung result extends to any fixed
finite number of large neutral features. The original one-qubit Hamiltonian
and readout yield orthonormal microscopic energy-window vectors with
additive energy centers and adjacent coupling ratios `sqrt(m)`. Prepared
superpositions also follow approximate harmonic evolution for
`|t|<=S/(J lambda delta)`, with error `O(lambda/delta)` at fixed M and S.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/FIXED_OCCUPATION_LADDER_PROOF.md)
uses exact spin-pair combinatorics, controlled ray/contact corrections, and
the existing microscopic projection bounds. A formal boson generating
function evaluates a polynomial identity; it adds no physical degrees of
freedom. The maximum occupation M stays fixed as the grid grows. An
M-dependent interval cutoff preserves the ground-background isometry.

[Replay](../scripts/native_fixed_occupation_ladder.py) checks the determinant,
mixed derivative and hard-core projection identities against direct finite
algebra. These numerical controls are not a native many-body spectral
calculation. Independent [algebra](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FIXED_LADDER_ALGEBRA_CHECK.md)
and [physical-bound](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FIXED_LADDER_PHYSICAL_CHECK.md)
checks support the stated extension.

No exact invariant oscillator, full CCR, finite-density theory, stable
particle, cosmological scalar or empirical identification is inferred.
The supplied Hamiltonian, weak regime, selected momentum family, preparation,
scales and measurement bridge remain assumptions. In particular, most of
the readout response need not stay within this selected ladder. All work
is exposed model development, without observational calibration or an
independent observation test.
