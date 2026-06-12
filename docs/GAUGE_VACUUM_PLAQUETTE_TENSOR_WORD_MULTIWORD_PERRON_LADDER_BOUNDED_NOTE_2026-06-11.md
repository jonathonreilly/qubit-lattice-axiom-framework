# Gauge-Vacuum Plaquette Multi-Word Tensor-Transfer Perron Ladder Bounded Note

**Date:** 2026-06-11
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Claim boundary:** finite bounded measurement on tensor-word product
truncations at `beta = 6`, with primary two-word and feasible three-word
readouts at tensor `NMAX = 4`, `MODE_MAX = 80`, composed into the existing
source-sector Perron machinery at source `NMAX = 7`, `MODE_MAX = 200`. This
note does not compute the physical 3D unmarked spatial Wilson environment, an
untruncated tensor-transfer Perron state, an `L_perp` limit, an analytic
plaquette value, a selected adjacent-contraction convention, or a canonical
repinning.

**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** `scripts/gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11.py`

## Inputs

The one-hop authorities for the finite computation are:

- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the one-word matrix construction
  `tensor_word := diag_c * (N_f + N_fbar) * diag_c * (N_f + N_fbar)^T * diag_c`.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-transfer ingredient language: matrix elements are
  finite sums of products of Wilson coefficients and exact nonnegative
  `SU(3)` fusion/intertwiner multiplicities; the finite packet uses
  fundamental/anti-fundamental fusion recurrences on the same dominant-weight
  box.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source-sector operator and the `rho`-input Perron solve.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparator/reuse-number license used only in the fenced
  distance block.

The in-flight one-word PR3606 note is referenced as a plain-text pointer, not
as a one-hop authority: `.claude/tmp/refs/TENSOR_WORD_PERRON_NOTE.md`.

No literature value, new axiom, external citation, or fitted selector is used.

## Construction

Let `B_N = {(p,q): 0 <= p,q <= N}` and let

```text
D[(p,q)] = c_(p,q)(6) / (d_(p,q) c_(0,0)(6)),
M = N_f + N_fbar.
```

The one-word packet is

```text
T_1 = D M D M^T D.
```

For `k` words, the runner uses the tensor-product word state
`(lambda_1, ..., lambda_k) in B_N^k`, with

```text
D_k(lambda_1, ..., lambda_k) = product_i D[lambda_i],
M_k = M tensor ... tensor M  (k factors).
```

The adjacent-word contraction is the ambiguous step in the cited notes.
The runner therefore implements both finite readings:

1. **Character-level singlet contraction.** Adjacent intermediate word labels
   must fuse through the singlet channel, with unit character-orthogonality
   weight on the allowed channel.
2. **Matrix-element-level singlet contraction.** The same singlet channel is
   used, but each adjacent Haar/intertwiner bond carries an extra
   `1 / d_lambda` factor.

For both readings the runner tests same-orientation bonds
`lambda_{i+1} = lambda_i` and conjugate-orientation bonds
`lambda_{i+1} = bar(lambda_i)`. At this symmetric finite box the same and
conjugate orientations agree numerically to the runner tolerance.

With middle diagonal

```text
D_mid(lambda_1, ..., lambda_k)
  = D_k(lambda_1, ..., lambda_k) * product_adjacent_bonds b(lambda_i, lambda_{i+1}),
```

the finite `k`-word transfer used by the runner is

```text
T_k = D_k M_k D_mid M_k^T D_k.
```

The uncontracted control sets every adjacent bond factor to `1`. In that case
`T_2 = T_1 tensor T_1`, and the marked-word readout reproduces the one-word
value.

## Readout Conventions

For the Perron vector `psi_k(lambda_1, ..., lambda_k)`, the runner reports two
finite boundary-character readouts with word `0` marked:

```text
marginal:
rho(lambda) =
  sum_{all other word labels} psi_k(lambda, other labels)
  / sum_{all other word labels} psi_k((0,0), other labels)

trivial_slice:
rho(lambda) =
  psi_k(lambda, (0,0), ..., (0,0))
  / psi_k((0,0), (0,0), ..., (0,0)).
```

Word-position alternatives are tested by symmetry in the runner; the printed
table reports word `0` because the positions agree at the displayed precision.

## Anchor Gate

The runner reproduces the one-word PR3606 readout before measuring the ladder:

```text
one-word tensor Perron eigenvalue: 1.012369912748
rho_tw1(1,0): 0.378514922317
P_tw1(6): 0.434215413260
P_loc reference: 0.452407159045
P_triv reference: 0.422531739647
```

The uncontracted two-word control gives

```text
T_2 = T_1 tensor T_1
P = 0.434215413260
```

so the multi-word machinery reproduces the one-word readout when no adjacent
bond is inserted.

## Two-Word Measurement

At `NMAX = 4`, `MODE_MAX = 80`, source `NMAX = 7`, source `MODE_MAX = 200`:

| bond reading | orientation | readout | `rho_(1,0)` | `rho_(1,1)` | `P(6)` | direction vs one-word distance to `0.5934` |
|---|---|---:|---:|---:|---:|---:|
| character | same | marginal | `0.232710097468` | `0.162385894803` | `0.429847250027` | away by `0.004368163233` |
| character | same | trivial slice | `0.211265869825` | `0.162259799480` | `0.429196712321` | away by `0.005018700938` |
| matrix-element | same | marginal | `0.448136509420` | `0.162403385294` | `0.436251149956` | toward by `0.002035736696` |
| matrix-element | same | trivial slice | `0.211265869825` | `0.162259799480` | `0.429196712321` | away by `0.005018700938` |

The conjugate-orientation rows match the same-orientation rows to the runner
tolerance and are printed by the runner.

The two-word `NMAX/MODE_MAX` sweep over `NMAX in {3,4}` and
`MODE_MAX in {80,200}` is stable on the printed values:

```text
character/marginal P span:      8.044e-14
character/trivial_slice span:   0.000e+00
matrix_element/marginal span:   2.304e-14
matrix_element/trivial_slice:   5.551e-17
```

## Three-Word Feasibility Measurement

The three-word default box has dimension `25^3 = 15625`. A dense matrix would
be about `1.819 GiB`, so the runner uses a matrix-free symmetric operator
with sparse `M tensor M tensor M` fusion multiplication.

At `NMAX = 4`, `MODE_MAX = 80`:

| bond reading | readout | `rho_(1,0)` | `rho_(1,1)` | `P(6)` | direction vs one-word distance to `0.5934` |
|---|---:|---:|---:|---:|---:|
| character | marginal | `0.214641212848` | `0.162262316312` | `0.429299240786` | away by `0.004916172474` |
| character | trivial slice | `0.211265869825` | `0.162259799480` | `0.429196712321` | away by `0.005018700938` |
| matrix-element | marginal | `22.802148174123` | `0.162354707873` | `0.592817119605` | toward by `0.158601706345` |
| matrix-element | trivial slice | `0.211265869825` | `0.162259799480` | `0.429196712321` | away by `0.005018700938` |

The matrix-element three-word marginal value is a finite convention-sensitive
measurement. It is not selected by the cited notes as the physical
boundary-character convention, and it is not a fit to the comparator.

## Fenced Comparator Distances

The canonical comparison number below is admitted only as a comparison/reuse
number, not as a derived value, fit target, or repinning input.

```text
P_tw1 = 0.434215413260
|P_tw1 - P_loc_reference| = 0.018191745785
|P_tw1 - P_triv_reference| = 0.011683673613
|P_tw1 - 0.5934| = 0.159184586740

two-word character marginal:
P = 0.429847250027
|P - P_loc_reference| = 0.022559909018
|P - P_triv_reference| = 0.007315510380
|P - 0.5934| = 0.163552749973
direction_vs_tw1 = away by 0.004368163233

two-word character trivial_slice:
P = 0.429196712321
|P - P_loc_reference| = 0.023210446723
|P - P_triv_reference| = 0.006664972674
|P - 0.5934| = 0.164203287679
direction_vs_tw1 = away by 0.005018700938

two-word matrix_element marginal:
P = 0.436251149956
|P - P_loc_reference| = 0.016156009088
|P - P_triv_reference| = 0.013719410309
|P - 0.5934| = 0.157148850044
direction_vs_tw1 = toward by 0.002035736696

two-word matrix_element trivial_slice:
P = 0.429196712321
|P - P_loc_reference| = 0.023210446723
|P - P_triv_reference| = 0.006664972674
|P - 0.5934| = 0.164203287679
direction_vs_tw1 = away by 0.005018700938

three-word character marginal:
P = 0.429299240786
|P - P_loc_reference| = 0.023107918258
|P - P_triv_reference| = 0.006767501139
|P - 0.5934| = 0.164100759214
direction_vs_tw1 = away by 0.004916172474

three-word matrix_element marginal:
P = 0.592817119605
|P - P_loc_reference| = 0.140409960560
|P - P_triv_reference| = 0.170285379958
|P - 0.5934| = 0.000582880395
direction_vs_tw1 = toward by 0.158601706345
```

## Bounded Statement

The two-word rung exists as a finite tensor-product transfer under the stated
repo-internal construction. The direction depends on the unresolved
adjacent-contraction and boundary-readout convention:

- character-level singlet contraction moves the marginal readout away from
  the comparator relative to the one-word value;
- matrix-element-level singlet contraction moves the two-word marginal readout
  modestly toward the comparator;
- trivial-slice readout moves away under both bond normalizations;
- feasible three-word matrix-element marginal readout has a small fenced
  comparator distance, but that convention is not selected here.

Named residuals:

- finite word count only;
- finite dominant-weight box and finite Bessel mode support only;
- no physical 3D unmarked spatial Wilson environment computation;
- no all-weight or untruncated convergence proof;
- no `L_perp` limit;
- no selected adjacent-contraction convention;
- no analytic `P(6)`;
- no canonical repinning.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11.py
```

Expected tail:

```text
TOTAL: PASS=25, FAIL=0
```

Cache refresh command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
