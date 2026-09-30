# Plaquette Self-Consistency Finite MC Diagnostic

**Date:** 2026-04-15; finite-diagnostic repair 2026-05-25
**Status:** bounded-support finite Wilson-plaquette diagnostic. The canonical infinite-volume value `0.5934` is an admitted comparison/reuse number here, not a value derived by this note.
**Status authority:** independent audit lane only.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py`

## Scope note (2026-09-30): point estimates of the same quantity

The reuse license above is unchanged. For the record, two point estimates of the
same pure-gauge Wilson plaquette at `beta = 6`, each with its source. They are
point estimates, not certificates, and neither replaces the admitted reuse
number.

- `0.59369(2)`: weighted mean of the `1 x 1` space-time Wilson loops of the
  repository's April 2026 production ensembles,
  `outputs/alpha_s_wilson_loop_production/ensemble_{12x12x12x24,16x16x16x32,24x24x24x48}_unsmeared.json`,
  500 configurations each (`0.593692(44)`, `0.593671(33)`, `0.593741(61)`;
  chi-squared 1.0 for 2 degrees of freedom), recomputed with Madras-Sokal errors by
  `scripts/frontier_hierarchy_taste_in_plaquette_measure_spot_check.py`.
- `0.59372(4)`: a reduced heatbath plus overrelaxation run at `L = 12` and `16`
  of the 2026-09-29 wall campaign (code outside the repository; a same-family
  check, not an independent referee).

Both lie about `3e-4` above `0.5934`, which is twelve times the April error
bar. Neither is a certificate under
`PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md`: the reduced run's
total budget is `4.3e-5`, so its `2 sigma` (`8.5e-5`) is above the grade-4 limit
`5e-5`; its `L^-4` fit fails the protocol's gate (chi-squared 63 for 2 degrees
of freedom), and step 6 of the protocol then says no certificate is issued; the
April ensembles have no infinite-volume fit. Read against the protocol's
pre-registered bands, a conforming certificate at these values would fall in
Band D (`|d| > 1e-4`). No such certificate exists, so nothing the protocol lists
under Band D is re-opened by this note, but the licensed `0.5934` should not be
read as good to `+/- 5e-5`. The 2026-05-05 finite-size fit `0.59400(37)`
is within one sigma of `0.59372`. The repository's analytic "bridge-support
upper candidate" `0.59353` (a non-theorem candidate, see
`PLAQUETTE_BOOTSTRAP_FRAMEWORK_INTEGRATION_NOTE_2026-05-03.md`) is `1.6e-4`
below the April mean, about 6.5 sigma of the April error; that tension is
recorded here, not resolved.

The quantity above is the pure-gauge plaquette. A plaquette measured with
dynamical staggered fermions in the measure is a different number (about `+0.02`
higher on a `4^4` lattice with one staggered field); see the 2026-09-30
corrigendum of `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`.

## Actual claim

For a finite periodic `L^4` lattice with `SU(3)` link variables and Wilson single-plaquette action

```text
S_W[U; beta] = (beta / 3) sum_P (3 - Re Tr U_P),
```

the average plaquette

```text
P_bar(U) = (1 / N_P) sum_P Re Tr U_P / 3
```

is a well-defined bounded observable of the finite compact configuration space. A Monte Carlo runner can evaluate finite-volume diagnostics of this observable at `beta = 6`, and those diagnostics are not fit parameters.

That is the entire repaired claim.

## What changed

The earlier row mixed a true finite same-surface statement with a stronger unresolved physical readout:

- true finite statement: `P_bar` is a unique observable of the finite Wilson partition function once `beta`, lattice size, action, and measure are selected;
- unresolved physical readout: the canonical `0.5934` value at the physical `beta=6` surface is not derived analytically here and is not certified here by a completed same-surface MC campaign.

This repair keeps the finite observable/diagnostic theorem and withdraws the stronger value-closure language. The canonical value `0.5934` may still be used by downstream notes only as an admitted comparison/reuse number unless a separate retained MC certificate or analytic beta=6 closure is supplied.

## Finite theorem

Fix:

- finite periodic lattice size `L`;
- gauge group `SU(3)` on each oriented link;
- Wilson single-plaquette action at a specified `beta`;
- compact Haar product measure over all links.

Then:

1. the finite configuration space is compact;
2. `S_W[U; beta]` is real and finite for every configuration;
3. the finite partition function `Z_L(beta)` is finite and positive;
4. `P_bar(U)` is bounded configuration-wise;
5. the finite expectation

```text
<P>_L(beta) = Z_L(beta)^(-1) integral P_bar(U) exp(-S_W[U; beta]) dU
```

is a unique mathematical number for the selected finite surface.

Monte Carlo is an evaluation method for this finite expectation. It does not introduce a fit parameter, but a short finite diagnostic run is not the same as an infinite-volume physical certificate.

## Runner-backed diagnostic

The paired runner verifies:

- `SU(3)` proposal construction preserves unitarity and determinant one to numerical tolerance;
- finite-lattice link and plaquette counts for `L^4`;
- Wilson action and average plaquette are finite and real on sampled `SU(3)` configurations;
- a one-plaquette Metropolis diagnostic changes the average plaquette between `beta=0` and `beta=6` in the expected direction;
- the source note explicitly withholds a derivation of the canonical `0.5934` readout;
- after audit-pipeline regeneration, the row is dependency-free and requeued for independent audit.

## Boundaries

This row does not claim:

- a completed same-surface MC certificate for `0.5934`;
- an analytic tensor-transfer/Perron solution for the physical `beta=6` boundary character;
- that the finite diagnostic runner is an infinite-volume extrapolation;
- that downstream uses of `0.5934` are proven by this note;
- any audit verdict or status promotion.

The remaining science target is still the real one: either ship a completed same-surface MC certificate for the physical value or derive the beta=6 boundary-character/tensor-transfer closure analytically.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_plaquette_self_consistency_finite_mc_repair.py
```

Expected result:

```text
Plaquette self-consistency finite MC diagnostic repair
TOTAL: PASS=24 FAIL=0
```
