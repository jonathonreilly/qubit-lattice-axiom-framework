# Gauge-Vacuum Plaquette Strip-Word Deep Ladder Product Axis Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite strip-word product-axis measurement at `beta = 6`,
tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`, and source
`MODE_MAX = 200`. The strip-word is the 625-state two-strip layer object with
the derived dimension-stripped internal width contraction. The depth ladder
uses the derived matrix-element longitudinal bond on each rail. This note does
not compute the full physical `3D` unmarked rim environment, a wider strip
limit, an all-link non-class intertwiner basis, an `L_perp` limit, analytic
`P(6)`, or a repinning.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.txt

No literature value, new axiom, external citation, fitted selector, or new
comparator number is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for them.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the single-word depth bond `delta(lambda,mu) / d_lambda`.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `B_4` tensor-word packet, the `D_lambda` convention, and the
  fundamental / anti-fundamental fusion recurrences.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the tensor-transfer construction language: character expansion,
  finite coefficient products, and shared-link Haar integration.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the Schur/character convolution dictionary and inverse-dimension shared
  link factor.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the same-link mixed Wilson kernel and its matrix-coefficient
  convolution eigenvalue.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the finite source-sector Perron machinery with supplied `rho`.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
  for the one-word rho normalization and composed one-word value.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934`, used here only in the
  fenced distance block.

Context pointer, not a one-hop authority:
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py.
Branch-local temporary reference paths are intentionally omitted from this
source note.

## Strip Object And Depth Bond

The internal width link follows the contraction context note's connected-trace
Schur step:

```text
integral_SU(3) chi_lambda(U A) chi_mu(U^dagger B) dU
  = delta_(lambda,mu) chi_lambda(A B) / d_lambda.
```

In the same context note, applying that factor to the central class coefficient
gives:

```text
central boundary law coefficient = d_lambda D_lambda
connected shared-link Haar factor = 1 / d_lambda
derived internal-link coefficient = D_lambda.
```

Thus the licensed strip-word is the dimension-stripped two-strip object. For a
strip state `s = (a,b)` define

```text
D_strip(s) = D_a D_b E_D(a,b),
F_strip = M tensor M,
d_strip(s) = d_a d_b,
```

where

```text
E_D(a,b) = 1 + sum_(lambda != 0) D_lambda N_(a,b)^lambda.
```

The adjacent-word authority derives the one-rail depth bond

```text
b(lambda,mu) = delta_(lambda,mu) / d_lambda.
```

The two rails are separate longitudinal shared links, so the strip-word depth
bond used here is the product

```text
B_strip((a,b),(c,d))
  = delta_(a,c) delta_(b,d) / (d_a d_b).
```

Equivalently, after the middle-label collapse in a `k`-strip-word chain,

```text
C_k(s) = D_strip(s)^k / d_strip(s)^(k-1).
```

The unselected character-level diagnostic would omit the two inverse
dimensions. The authority chain above selects the matrix-element product bond
for this finite scalar class-channel strip object. A future all-link
non-class `6j` / intertwiner normalization remains a named residual.

## Reduction

The word-chain finite-rank reduction carries over with the 625-state strip box.
Let

```text
G_strip = F_strip^T diag(D_strip^2) F_strip,
ell_eta(mu) = sum_s eta_strip(s) D_strip(s) F_strip(s,mu),
```

where `eta_strip` is the Perron vector of the single strip transfer. Then the
nonzero spectral problem for the depth-`k` strip-word transfer is

```text
R_k(mu,nu)
  = sqrt(C_k(mu)) G_strip(mu,nu)^k sqrt(C_k(nu)).
```

Equivalently, with

```text
t_strip(mu,nu)
  = sqrt(D_strip(mu) / d_strip(mu))
    G_strip(mu,nu)
    sqrt(D_strip(nu) / d_strip(nu)),
```

the scaled reduction is

```text
R_k(mu,nu)
  = sqrt(d_strip(mu) d_strip(nu)) t_strip(mu,nu)^k.
```

For source readout, if `v_k` is the Perron vector of `R_k`, set

```text
Z_k(s)
  = D_strip(s) sum_mu F_strip(s,mu)
      [sqrt(C_k(mu)) v_k(mu)] ell_eta(mu)^(k-1).
```

The composed source `rho` is the left-rail marginal

```text
rho_k(a) = sum_b Z_k(a,b) / sum_b Z_k((0,0),b).
```

This marginal convention is fixed by the gate that `k = 1` reproduces the
two-strip composed readout.

## Gates

The runner checks:

```text
strip-word state count = 625
P_1(strip-word) = 0.439904783618900
```

The direct matrix-free `k = 2` solve acts on `625^2 = 390625` states and
agrees with the 625-rank reduction:

```text
P_2(strip-word) = 0.449370834209281
```

The internal-width cut gate reproduces the certified one-word depth ladder:

| cut k | P |
|---:|---:|
| 1 | `0.434215413259920` |
| 2 | `0.433061880379652` |
| 3 | `0.543142610051424` |
| 4 | `0.603630724651002` |
| 20 | `0.615191992181771` |
| 40 | `0.615191992185898` |

The `k = 40` cut value reaches the same pair-support source limit as the
composition context:

```text
P_inf(word chain) = 0.615191992185898.
```

## Strip-Word Measurement

The strip-word ladder values are:

| k | P_k(strip-word) |
|---:|---:|
| 1 | `0.439904783618900` |
| 2 | `0.449370834209281` |
| 3 | `0.452852422088833` |
| 4 | `0.453183676480635` |
| 5 | `0.523578153848870` |
| 6 | `0.603873940264150` |
| 7 | `0.612716959303744` |
| 8 | `0.614490486747600` |
| 9 | `0.614970945672875` |
| 10 | `0.615118658741640` |
| 11 | `0.615166957004086` |
| 12 | `0.615183295918934` |
| 13 | `0.615188937692828` |
| 14 | `0.615190911381744` |
| 15 | `0.615191607832157` |
| 16 | `0.615191855028469` |
| 17 | `0.615191943122270` |
| 18 | `0.615191974604943` |
| 19 | `0.615191985878463` |
| 20 | `0.615191989921045` |
| 21 | `0.615191991372136` |
| 22 | `0.615191991893382` |
| 23 | `0.615191992080716` |
| 24 | `0.615191992148067` |
| 25 | `0.615191992172289` |
| 26 | `0.615191992181001` |
| 27 | `0.615191992184136` |
| 28 | `0.615191992185264` |
| 29 | `0.615191992185669` |
| 30 | `0.615191992185815` |
| 31 | `0.615191992185868` |
| 32 | `0.615191992185887` |
| 33 | `0.615191992185893` |
| 34 | `0.615191992185896` |
| 35 | `0.615191992185897` |
| 36 | `0.615191992185897` |
| 37 | `0.615191992185897` |
| 38 | `0.615191992185898` |
| 39 | `0.615191992185897` |
| 40 | `0.615191992185897` |

The high-`k` last digits are at the displayed roundoff floor. The source
limit is computed directly from the pair-support source vector:

```text
P_inf(strip-word chain) = 0.615191992185898.
```

## Theta

The four symmetry-related strip channels
`((1,0),(0,0))`, `((0,1),(0,0))`, `((0,0),(1,0))`, and
`((0,0),(0,1))` give the same closed expression:

```text
ell_eta(channel) / ell_eta(0)       = 3.592467585287829
sqrt(D_strip(channel)/d_strip(channel)) = 0.447610251097099
t_strip(channel,0) / t_strip(0,0)  = 0.223805125548550
theta_strip                         = 0.359884308159842
```

Measured tail ratios over the pre-roundoff window approach the same value;
the runner checks the mean window against the closed expression. The
one-word theta restated from the composition context is

```text
theta_word = 0.263745855973467.
```

Thus the theta identification structure carries to the strip-word product
axis, but the strip finite packet has a slower displayed tail.

## Headline Comparison

The fenced comparison number is used only as comparison/reuse context:

```text
P_inf(strip-word chain) = 0.615191992185898
P_inf(word chain)       = 0.615191992185898
fenced comparator       = 0.593400000000000

P_inf(strip) - P_inf(word) = 0.000000000000000
P_inf(word) - comparator   = 0.021791992185898
P_inf(strip) - comparator  = 0.021791992185898
```

This is a genuine negative for the hoped asymptotic movement on this finite
product axis: the first strip rung moves the one-word composed readout upward,
but the depth limit lands on the same pair-support source limit as the
one-word chain. The residual is not removed; it remains named below.

## Residual Ledger

| residual | what would discharge it |
|---|---|
| finite `B_4` strip-word packet | Repeat or bound the construction beyond the finite dominant-weight box and finite Bessel support. |
| scalar class-channel internal width contraction | Build the all-link non-class intertwiner / `6j` basis object and compare its normalization. |
| product-axis geometry | Relate this depth x two-strip product ladder to the full physical `3D` rim environment. |
| wider strip limit | Extend the width axis beyond the two-strip object and test the same depth reduction. |
| `L_perp` limit | Evaluate or bound the physical transverse-depth transfer limit on the same source surface. |
| analytic `P(6)` | Supply an analytic same-surface derivation of the Wilson plaquette value at `beta = 6`. |
| no repinning | Supply a separate repo-ratified canonical repinning or enclosure; this note does not do that. |

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=35, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
