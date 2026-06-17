# Corner Transfer Extends To Fixed Gauge Backgrounds -- Bounded Note

**Date:** 2026-06-12
**Type:** bounded_theorem
**Audit boundary:** source proposal only; independent audit lane sets
`audit_status` and pipeline-derived `effective_status`.
**Primary runner:** `scripts/frontier_corner_transfer_fixed_gauge_background_2026_06_12.py`
**No-promotion statement:** this note does not promote, demote, or set the
effective status of any cited row, does not edit any audit registry or queue,
and does not assert a retained outcome for this packet.

## Boundary

FIREWALL: fixed background only. This note proves (N1)--(N5) on the supplied
corner-axis surface at a fixed spatial gauge background in temporal gauge. The
computed witness class is arbitrary finite `U(1)` phase backgrounds at
`L_s = 2`; the retained fixed-gauge engine supplies the general
fixed-background `SU(3)`/`U(1)` authority. The note does **not** integrate over
backgrounds, does **not** supply the gauge measure, does **not** select a
species reading, does **not** select an occupancy cell, does **not** fix `r`,
and leaves the binary untouched.

The U-INTEGRATED level remains the named open next path: what is still missing
is the measure over backgrounds and the full gauge dynamics. This note narrows
both interacting opens only to that level; it does not claim the integrated
step.

## The supplied surface

Work with the staggered `1+1d` action at a fixed spatial background
`{U_i(x)}` in temporal gauge. The generation factor carries the Hermitian
circulant mass

```text
H(delta) = a I + B e^{i delta} C + B e^{-i delta} C^T,
lambda_k(delta) = a + 2 B cos(delta + 2 pi k / 3).
```

The positivity domain is `lambda_k(delta) > 0` for all `k`, for example
`a > 2B > 0`. The runner checks `(a, B, delta) = (1, 1/4, 2/9)` and a second
domain point. The circulant facts are reproved inline: the Fourier basis
diagonalizes `C`, so `H(delta)` splits into three channels; under
`delta -> -delta`, channel `0` is fixed and the doublet channels `1` and `2`
swap.

The retained fixed-background engine gives the position-space two-step
staggered transfer construction. At fixed `U`, the spatial hop is
anti-Hermitian; each positive channel mass `lambda_k` therefore inherits
config-by-config two-step positivity:

```text
T_k^2[U] = B_k[U]^dag B_k[U] >= 0.
```

## Theorem

**(N1) Channel decomposition survives the background.** The generation mass
acts on the internal factor and the gauge background acts on the spatial
factor. They commute, so the Fourier/circulant basis block-diagonalizes the
fixed-background action into three channels with masses `lambda_k`. Each
channel inherits the retained fixed-background two-step positivity
`T_k^2[U] = B_k[U]^dag B_k[U]`, positive Hermitian config-by-config. The runner
checks the block residual and the channel positivity on two fixed random
`U(1)` backgrounds and both parameter points. Check tags: `N1a`, `N1b`,
`N1c`.

**(N2) Corner transfer at fixed background.** Define the fixed-background
corner transfer by tensoring the three channel transfers:

```text
T_corner^2[U] = tensor_k T_k^2[U].
```

It is positive Hermitian config-by-config because a tensor product of positive
Hermitian finite matrices is positive Hermitian. The free wave-6 result is the
`U = 1` member of this family; the runner rederives that member by comparing
the position-space two-step eigenvalues with the free dispersion. Check tag:
`N2`.

**(N3) Trace correspondence config-by-config.** For each fixed background,
the finite-fermion second quantization obeys

```text
Tr Gamma(t[U]) = det(1 + t[U]).
```

The canonical Berezin pair normalization is forced: multiplying each pair
measure by a positive scalar `lambda` changes the Berezin side by
`lambda^N`, so equality for arbitrary nonzero determinant requires
`lambda = 1`. The runner checks the equality per witness background, shows
`lambda = 2` breaks it, solves the positive normalization condition, and
performs one genuine two-pair Grassmann expansion for a channel at a complex
background. Check tags: `N3a`, `N3b`, `N3c`.

**(N4) K and the complement at fixed background -- honest scope.** `K`/CPT
conjugation acts on the background as `U -> conj(U)`. The channel kernels obey
the computed doublet-swap relation

```text
t_k[U](delta) = t_sigma(k)[conj(U)](-delta),
sigma(0)=0, sigma(1)=2, sigma(2)=1.
```

Therefore:

- On `K`-real backgrounds, `conj(U) = U`, so the hw-complement
  registration-equivalence extends config-by-config exactly. The two readings'
  corner transfers are unitarily equivalent by the channel-swap permutation,
  and the registrable data checked by the runner, including traces and
  dispersions, agree.
- On general backgrounds, the operator-level statement is the
  conjugated-background statement: reading-1 data at `U` equal reading-2 data
  at `conj(U)`; operator-level unitary equivalence at the same background is
  asserted only on the `K`-invariant class.
- **(strengthened, second pass) Registrable trace data are same-background
  equivalent at EVERY fixed background.** Three computed legs: traces of the
  positive Hermitian corner transfer are real; conjugating the background
  conjugates the transfer matrix, so trace data at `conj(U)` are the complex
  conjugates of those at `U`; real and conjugate together force equality, and
  with the conjugated-background statement the same-background trace gap
  between the two readings vanishes — a theorem-backed runner condition, not
  an empirical flag. Operator-level same-background equivalence beyond the
  `K`-real class is still not claimed.

Check tags: `N4a`, `N4b`, `N4c`, `N4d-i/ii/iii`.

**(N5) Consequence.** Both interacting opens narrow from "interacting/gauge" to
the U-INTEGRATED level. The occupancy lane's transfer-route prerequisite chain
has its fixed-background corner-transfer prerequisite supplied, and the
species-bridge equivariance has its fixed-background `K`/complement statement
supplied. What remains is the measure over gauge backgrounds and the full gauge
dynamics. Check tag: `N5`.

## Consequence

The fixed-background corner structure is no longer the obstruction. For every
supplied background in the fixed-background class, the channel split, the
corner tensor product, the trace/determinant correspondence, and the
`K`/conjugated-background complement relation are finite linear algebra.
The two interacting routes are now pointed at the same remaining layer:
the U-INTEGRATED gauge-dynamics level.

## Does NOT

- Does not integrate over gauge backgrounds.
- Does not supply or select the gauge measure.
- Does not prove full dynamical-gauge reflection positivity.
- Does not select a species reading.
- Does not select an occupancy cell.
- Does not fix `r`.
- Does not alter the binary.
- Does not remove or rewrite `AC_phi_lambda`.
- Does not claim that the U-INTEGRATED level has been handled.

## Dependencies

- [`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
  -- the retained fixed-gauge engine (N1/N2 authority; construction reused).
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  -- the canonical pair measure (N3's Berezin side).
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- the registrable class (N4's data).

## Context

Backticked context only; the needed facts are reproved in this packet:
`ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`,
`P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md`,
`AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md`,
`ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md`,
`ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md`,
`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`.

The free corner-extension, trace-correspondence, and hw-dynamics companion
facts are used only as patterns; this note rechecks the finite Fourier,
second-quantization, and `K`/conjugation identities directly.

## Validation

Run:

```bash
python3 scripts/frontier_corner_transfer_fixed_gauge_background_2026_06_12.py
```

Expected scorecard: `PASS=30 FAIL=0`. The runner prints the two parameter
points, the two fixed random `U(1)` witness seeds, the channel positivity
minima, the `dim 64` corner positivity check, Berezin normalization forcing,
the `K`-real and conjugated-background complement checks, firewall checks, and
a final `SUMMARY`.
