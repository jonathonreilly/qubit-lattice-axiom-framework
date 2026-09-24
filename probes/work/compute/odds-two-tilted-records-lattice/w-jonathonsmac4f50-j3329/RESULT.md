# Two tilted records in possibility's odds on the sphere menu — run 1

Worker `w-jonathonsmac4f50-j3329`, model `claude-opus-5-5`. Blocks 42 and 103 were written by the same model family (Claude). The solver is block 103's `probes/lib/odds_sphere_lattice.solve`, with the box's boundary layer held at the ordered sea (lean along z). Floating point throughout. The run took 1153 s for β = 1 on 21³ and 582 s for β = 0.6 on 17³.

## Setup

- Record 1 has content (1,0,0).
- Record 2 has content (cos a, sin a, 0): a = 0 (like), π (unlike), π/2 (perp).
- The aligned case has both records along the lean, (0,0,1).
- The records are separated by d along x.

## Linear prediction for the far field

Records are held boundary values (block 42 T6). Block 103 shows the turn of the lean has per-neighbour eigenvalue exactly 1/6, so the transverse lean is discrete-harmonic. The linear far field of the pair is therefore

`Σ_i tilt_i · h_i(x)`,

where `h_i` is the probability that the lattice walk from `x` reaches record `i` first, before the held boundary (a sparse solve). The comparison is against the plain sum of the two one-record fields.

## (i) Far sideways lean

Deviation over the largest far field, at four far sites (two beyond the pair along x, two on the y axis through the midpoint):

| β | d | like: Σ tilt h / sum of singles | unlike | perp |
|---|---|---|---|---|
| 1 | 2 | 0.006 / 0.137 | 0.025 / 0.132 | 0.083 / 0.063 |
| 1 | 3 | 0.008 / 0.074 | 0.020 / 0.072 | 0.065 / 0.030 |
| 1 | 4 | 0.006 / 0.047 | 0.015 / 0.046 | 0.049 / 0.019 |
| 1 | 6 | 0.004 / 0.023 | 0.011 / 0.023 | 0.024 / 0.009 |
| 0.6 | 2 | 0.039 / 0.179 | 0.008 / 0.159 | 0.046 / 0.089 |
| 0.6 | 3 | 0.025 / 0.100 | 0.003 / 0.091 | 0.042 / 0.044 |
| 0.6 | 4 | 0.014 / 0.061 | 0.003 / 0.057 | 0.037 / 0.028 |
| 0.6 | 6 | 0.010 / 0.025 | 0.008 / 0.026 | 0.023 / 0.014 |

**Like and unlike pairs.** The far field follows the pair's reaching probabilities, and so its capacity: the fields of like tilts are not additive, and the pair counts less than two single records. The deviation is at most 4%, against up to 18% for the sum of singles.

**Perp pairs.** The linear boundary-value theory does worse, up to 8%, and here the sum of singles is closer. A 90° tilt of each record is a large rotation on the sphere. The deviation falls with d.

## (ii) and (iii): the summed site log normalizer

`E_int = Σ_unformed[log N − log N_sea](pair) − the same for each record alone`.

| β | d | like | unlike | perp | aligned |
|---|---|---|---|---|---|
| 1 | 2 | +0.867 | −0.508 | +0.158 | −3.17e-2 |
| 1 | 3 | +0.462 | −0.394 | +0.0150 | −2.39e-3 |
| 1 | 4 | +0.298 | −0.277 | +8.8e-4 | −1.81e-4 |
| 1 | 6 | +0.157 | −0.153 | −4.0e-4 | −1.04e-6 |
| 0.6 | 2 | +0.747 | −0.470 | +0.163 | −0.168 |
| 0.6 | 3 | +0.452 | −0.399 | +0.0343 | −4.00e-2 |
| 0.6 | 4 | +0.295 | −0.292 | +3.5e-3 | −9.77e-3 |
| 0.6 | 6 | +0.155 | −0.159 | −1.6e-3 | −6.0e-4 |

**Tilted pairs.**
- Like and unlike pairs have opposite signs at every d and both β.
- They become near mirror images (±0.155) as d grows. The d-dependent weight is bilinear in the two tilts.
- It decays slowly, as the massless turn mode should: at β = 1 it halves from d = 4 to d = 6, between `1/d` and `1/d²` in these boxes.
- Perpendicular tilts carry no first-order weight. Their small residual changes sign.

**Aligned records.** Their weight is short-ranged:
- At β = 1 it falls by about an order of magnitude or more per step: 3.2e-2 → 2.4e-3 → 1.8e-4 → 1.0e-6.
- At β = 0.6, nearer the massless point β₀ ≈ 0.5085, it has a longer but still finite range, falling about 4× per unit of d.
- There is no d-dependence beyond the massive range.

## Verdict

The task expected three things, and all hold:
- the far fields follow the pair's capacity, here via its reaching probabilities;
- the weight has opposite signs for like and unlike tilts;
- it vanishes for aligned records beyond the massive range.

There is no HIT.
