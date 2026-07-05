# Gauge-Vacuum Plaquette Derived Word-Chain End-to-End Composition, Finite Packet Only

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim boundary:** finite composition on the derived word-chain packet at
`beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`,
and source `MODE_MAX = 200`. The composed inputs are the source-dependency
notes listed below. They are not evaluated here as
physical `3D` rim geometry, all-weight tensor-transfer closure, an `L_perp`
limit, analytic `P(6)`, or a canonical repinning.

**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_derived_word_chain_end_to_end_composition_bounded_theorem_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_derived_word_chain_end_to_end_composition_bounded_theorem_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for them.

## Composition Theorem

Assume the derived finite-packet conventions in the hypothesis ledger:

- adjacent-word matrix-element bond
  `delta_(lambda,mu) / d_lambda`;
- `eta_inf`, the finite tensor-word Perron vector, on every unmarked word
  slot;
- the rank-25 entrywise-power reduced family for word counts `k >= 2`;
- the finite source readout on source `NMAX = 7`, source `MODE_MAX = 200`;
- the pair-support limiting source vector in the word-count limit.

Then, on this finite packet and under those derived conventions, the
word-chain environment readout has limiting source value

```text
P_inf = 0.615191992185898.
```

The finite-packet convergence rate is given by the packet expression

```text
theta
  = (L_eta(f) / L_eta(0))
    * sqrt(D_f / d_f)
    * t(f,0) / t(0,0)
  = 0.263745855973467,
```

with

```text
L_eta(0)       = 0.319869137220260
L_eta(f)       = 1.197980906223103
D_f            = 0.422531739649983
d_f            = 3
t(f,0)/t(0,0) = 0.187645885390981
theta^(-1)     = 3.791528766619179.
```

The all-k finite-packet remainder source dependency supplies

```text
P_inf - P_k = C_source * theta^(k-1) + R_k,
|R_k| <= c3 * theta_3^k,

C_source = 0.410170474927582
theta_3  = 0.127269601426283
c3       = 3.631819614924623e+05
k0       = 17
```

and the dominance inequality

```text
c3 * theta_3^k < C_source * theta^(k-1)
```

from `k >= 17` onward. The composition runner rechecks the envelope on the
printed rungs `k = 2..20`.

The finite readout is separated from the fenced canonical comparison number:

```text
|P_inf - 0.5934| = 0.021791992185898.
```

That distance is not a fit target and not a repinning input. In this note it
is owned by the named structural residual: the current object is a `1D`
word-chain environment, while the physical target is a `3D` rim geometry.

The pair-support limiting source input is exact on the finite packet. The
word-box/mode sweep reports zero displayed `P_inf` span across the tested
word-packet cells. Changing the finite source box is not exact stationarity:
the source sweep gives

```text
source NMAX=5: P_inf = 0.615191040446003
source NMAX=7: P_inf = 0.615191992185898
source NMAX=9: P_inf = 0.615191992282189
```

so this theorem surface is the source `NMAX = 7`, `MODE_MAX = 200` value, and
source-box sensitivity remains reported rather than hidden.

The retirement interface names a certified enclosure as one possible
route. This row supplies no enclosure of the physical plaquette value; the
structural word-chain-to-rim residual is open.

## Runner-Checked Numeric Ledger

<!-- runner-checked-ledger:start -->
| key | value | role |
|---|---:|---|
| `tensor_NMAX` | `4` | theorem tensor dominant-weight box |
| `tensor_MODE_MAX` | `80` | theorem tensor Bessel mode support |
| `source_NMAX` | `7` | theorem source dominant-weight box |
| `source_MODE_MAX` | `200` | theorem source Bessel mode support |
| `P_1` | `0.434215413259920` | one-word composed readout |
| `P_2` | `0.433061880379652` | derived eta-weighted two-word readout |
| `P_3` | `0.543142610051424` | derived eta-weighted three-word readout |
| `P_4` | `0.603630724651002` | derived eta-weighted four-word readout |
| `P_20` | `0.615191992181771` | finite rung used in the tail check |
| `P_inf` | `0.615191992185898` | pair-support source limit on source `NMAX = 7` |
| `theta` | `0.263745855973467` | finite-packet rate expression |
| `theta_inverse` | `3.791528766619179` | reciprocal rate diagnostic |
| `theta_3` | `0.127269601426283` | third scale in the remainder envelope |
| `C_source` | `0.410170474927582` | pair-support source coefficient |
| `c3` | `3.631819614924623e+05` | conservative finite-packet remainder constant |
| `k0` | `17` | dominance gate |
| `comparator_distance` | `0.021791992185898` | fenced distance to admitted `0.5934` |
| `source_NMAX5_P_inf` | `0.615191040446003` | source-box sensitivity row |
| `source_NMAX7_P_inf` | `0.615191992185898` | theorem source-box row |
| `source_NMAX9_P_inf` | `0.615191992282189` | source-box sensitivity row |
| `source_5_to_7_drift` | `9.517398950054101e-07` | source-box sensitivity |
| `source_7_to_9_drift` | `9.629119723797e-11` | source-box sensitivity |
<!-- runner-checked-ledger:end -->

## Hypothesis Ledger

The word "authority" in this table means citation role for this composition.
It does not set a review outcome for any claim.

| input | provenance class | role in this note |
|---|---|---|
| [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md) | one-hop authority | Supplies the linkwise mixed-kernel factorization and the per-link convolution eigenvalue used to justify matrix-element propagation through shared links. |
| [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) | one-hop authority | Supplies the Schur/character convolution dictionary and the `1/d_lambda` contraction normalization. |
| [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md) | one-hop authority | Supplies the finite `tensor_word`, `boundary0`, and amplitude packet at tensor `NMAX = 4`, `MODE_MAX = 80`. |
| [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md) | one-hop authority | Supplies the finite source-sector Perron machinery with `rho` supplied as input at source `NMAX = 7`, `MODE_MAX = 200`. |
| [GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md) | one-hop authority | Supplies the formal all-weight convolution identification as a structural dictionary; no coefficient value is imported from it. |
| [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md) | one-hop authority | Supplies the source-sector factorized operator form behind the source Perron packet. |
| [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md) | source dependency, not regraded here | Fixes the composed one-word readout convention and reports `P_1 = 0.434215413260`. |
| [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md) | source dependency, not regraded here | Fixes the adjacent-word matrix-element bond `delta_(lambda,mu) / d_lambda` and separates trivial-slice from marginal readout. |
| [GAUGE_VACUUM_PLAQUETTE_TRIVIAL_SLICE_EIGEN_IDENTITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_TRIVIAL_SLICE_EIGEN_IDENTITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md) | source dependency, not regraded here | Fixes the stationary all-trivial-except-word0 slice identity and the frozen slice components. |
| [GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_RIM_BOUNDARY_ETA_ENV_CONSTRUCTED_READOUT_BOUNDED_NOTE_2026-06-12.md) | source dependency, not regraded here | Constructs the finite `eta = tensor_word e_(0,0)` rim-boundary vector and its eta-weighted readout convention. |
| [GAUGE_VACUUM_PLAQUETTE_RIM_DEPTH_LADDER_DEEP_RIM_LIMIT_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_RIM_DEPTH_LADDER_DEEP_RIM_LIMIT_BOUNDED_NOTE_2026-06-12.md) | source dependency, not regraded here | Fixes the finite-depth ladder and the deep-rim `eta_inf` boundary used on unmarked word slots. |
| [GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RUNG_FOUR_DEEP_RIM_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RUNG_FOUR_DEEP_RIM_BOUNDED_NOTE_2026-06-12.md) | source dependency, not regraded here | Supplies the `k = 4` direct/rank-reduced agreement and the `k = 1..20` word-count rung table. |
| [GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md) | source dependency, not regraded here | Supplies the packet expression for `theta`, the pair-support source limit `P_inf`, and `C_source`. |
| [GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_ALL_K_REMAINDER_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_ALL_K_REMAINDER_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md) | source dependency, not regraded here | Supplies the finite-packet remainder envelope constants `theta_3`, `c3`, and `k0 = 17`. |
| [GAUGE_VACUUM_PLAQUETTE_WORD_LIMIT_BOX_MODE_SWEEP_BOUNDED_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_WORD_LIMIT_BOX_MODE_SWEEP_BOUNDED_NOTE_2026-06-12.md) | source dependency, not regraded here | Supplies word-box/mode and source-box sweep diagnostics; source-box drift is preserved as sensitivity. |
| [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md) | admitted/fenced item | Supplies the `0.5934` reuse license only; no value is derived or fitted here. |
| [WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md](WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md) | admitted/fenced item | Names the Wilson real-positive `beta = 6` surface conventions; this note does not extend that surface. |

## Residual Ledger

| residual | what would discharge it |
|---|---|
| word-geometry lift | Derive or compute a map from this `1D` word-chain packet to the actual `3D` rim geometry and show the readout transformation on the same source surface. |
| L_perp on the physical surface | Evaluate or prove the `L_perp` transfer limit for the physical boundary-character target rather than for the finite word-count packet alone. |
| physical 3D rim | Compute the full unmarked spatial Wilson rim boundary state, including rim/far support and compression, then re-read the source Perron value from that state. |
| analytic P(6) | Supply an analytic same-surface derivation of the physical Wilson plaquette expectation at `beta = 6`. |
| no repinning | Provide a separate repo-ratified canonical repinning or enclosure; this note does not do that. |

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_derived_word_chain_end_to_end_composition_bounded_theorem_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=18, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_derived_word_chain_end_to_end_composition_bounded_theorem_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
