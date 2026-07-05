# Gauge-Vacuum Plaquette Windowed-Bond Deep Limit Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Claim boundary:** finite W55 probe of the W53 oriented
fundamental-window bond on the 625-state B4 two-strip surface at `beta = 6`,
tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`, and source
`MODE_MAX = 200`. The note tests the slice-identity mechanism and measures
feasible finite rungs. It does not compute the full B4 windowed `k = 3`
vector, the B4 windowed deep limit, a W54 symmetrized window, higher window
channels, larger boxes, the physical 3D rim environment, analytic `P(6)`, or
repinning.

**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.txt

No literature value, new axiom, external citation, fitted selector, or new
comparator number is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for Wilson-coefficient or Perron
readout decimals.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the unwindowed adjacent-word inverse-dimension bond.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite B4 tensor-word packet, Wilson coefficient convention, and
  fundamental / antifundamental recurrences.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the tensor-transfer construction language.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character convolution and inverse-dimension shared-link dictionary.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source readout surface.
- [SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md](SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md)
  for the finite B4 SU(3) fusion table engine used to rebuild the
  dimension-stripped strip factor.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934`, used here only in the
  fenced distance block.

Repo-local context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12.py.

The W54 symmetrized surface is a separate finite-window source surface and is
not consumed as authority here. The bounded window result below remains the
W53 oriented fundamental-window surface.

## Windowed Slice Equation

For a strip-word state `s = (a,b)`, write

```text
D_s = D_a D_b E_D(a,b),
F_strip = M tensor M.
```

For a `k`-word strip chain with a general adjacent bond `B`, the middle-label
form is

```text
T_k[x,y]
  = D_x D_y sum_(mu_1,...,mu_k)
      [ product_j D_(mu_j) product_(j=1 to k-1) B(mu_j, mu_(j+1)) ]
      product_j F_strip(x_j, mu_j) F_strip(y_j, mu_j).
```

On the raw trivial slice `x = (s,e,...,e)`, where `e=((0,0),(0,0))`, the later
trivial strip rows see the four strip channels

```text
Q = {(f,f), (f,fb), (fb,f), (fb,fb)}.
```

With the unwindowed bond `B_0(mu,nu) = delta_(mu,nu) / dim(mu)`, this forces
`mu_1` into the same four-channel set. That is the finite mechanism behind the
collapse used in the strip-word and slice-lemma context: after conjugation and
rail symmetries, the normalized left-rail source limit lands on the same
pair-support source vector as the one-word chain.

With the W53 oriented windowed bond

```text
B_window = B_0 + (c_fund(6)/c_0(6)) B_f,
B_f[(a,b),(c,d)] = 1/9
  if a x 3 -> c and b x 3bar -> d inside B4,
  else 0,
```

the predecessor set into `Q` is larger. The runner measures:

```text
zero-window predecessor count into Q      = 4
windowed predecessor count into Q         = 19
zero-window first-row slice support count = 36
windowed first-row slice support count    = 81
```

The off-slice dependence therefore no longer reduces to one common
two-channel scalar. The finite W53 bond modifies the inter-layer coupling in
the place used by the old slice identity, so the old closed fixed point does
not follow for this oriented windowed surface. The B4 windowed deep limit is a
named open target after this structural test.

## B4 k = 2 Gate

The runner rebuilds the B4 strip object, the W53 oriented window support, and
the direct `k = 2` power solve:

```text
B4 one-rail state count = 25
B4 strip state count    = 625
c_fund(6)/c_0(6)        = 1.267595218949950
W53 window support      = 3136 entries

P(k=2, window -> 0)        = 0.449370834209279
W44 k=2 anchor             = 0.449370834209281
P(k=2, W53 oriented window)= 0.445084590711323
displacement_vs_anchor     = -0.004286243497958
```

Thus the W53 finite `k = 2` rung moves below the W44 `k = 2` anchor by
`0.004286243497958` on this surface.

## Zero-Window Gate

Switching the window strength to zero recovers the old mechanism and the
certified unwindowed surfaces:

```text
zero-window B4 k=2 P              = 0.449370834209279
zero-window reduced B4 k=3 P      = 0.452852422088833
zero-window pair-support deep P   = 0.615191992185898
unwindowed deep reference         = 0.615191992185898
```

The zero-window slice predecessor set is exactly `Q`, so the slice-lemma
closed form is recovered at the support level. The finite-runner decimal
agreement above is the numerical gate; no exact-arithmetic statement is made
for those Perron decimals.

## k = 3 Fallback

The full B4 windowed `k = 3` direct vector has

```text
625^3 = 244140625 states,
one float64 vector = 1.953125 GB.
```

That leaves no practical room for the required second vector, middle tensor,
and axis temporaries in this runner. The fallback reduces the one-rail box to
`NMAX = 3`, giving `256^3 = 16777216` states and `0.134217728 GB` per vector.
The same W53 oriented bond construction is used inside that reduced box.

Reduced probe:

```text
NMAX=2 windowed k=2 P = 0.445070052253144
NMAX=2 windowed k=3 P = 0.448656762149366
NMAX=3 windowed k=2 P = 0.445084574646653
NMAX=3 windowed k=3 P = 0.448674745889987
```

The `NMAX=3` `k = 2` sensitivity against B4 is `-1.606e-08`. The
`NMAX=2 -> NMAX=3` `k = 3` drift is `+1.798e-05`. On the reduced surface, the
windowed `k = 3` rung remains below the same-box zero-window `k = 3` rung, but
it rises from the windowed `k = 2` value. This is a bounded finite-rung trend,
not a B4 deep-limit value.

## Fenced Comparison

The comparison number is used only as fenced comparison context:

```text
unwindowed deep reference      = 0.615191992185898
fenced comparator             = 0.593400000000000
unwindowed deep residual      = 0.021791992185898
B4 windowed k=2 displacement  = -0.004286243497958
k=2 residual fraction         = 0.196688924142130
NMAX=3 window-vs-zero k=3      = -0.004177674469898
```

At `k = 2`, the oriented W53 window accounts for `19.6688924142130%` of the
unwindowed deep residual as a finite displacement. The reduced `k = 3` probe
does not supply the B4 deep answer; it only shows that the finite windowed rung
is lower than the same-box zero-window rung while trending upward from its
own `k = 2` value.

## Residual Ledger

| residual | what would discharge it |
|---|---|
| full B4 windowed `k = 3` | Complete the 625^3 matrix-free solve or an equivalent memory-controlled contraction. |
| B4 windowed deep limit | Derive a new windowed finite-rank/MPO fixed point or compute a controlled deep ladder. |
| W54 symmetrized window | Add an independently derived conjugate-orientation or real-window surface and rerun the slice/rung checks. |
| larger boxes | Repeat or bound the construction beyond B4 and finite Bessel support. |
| higher window channels | Add the next window-character channels with their derived strengths. |
| physical 3D rim environment | Relate this depth x two-strip product surface to the physical unmarked rim construction. |
| all-link non-class normalization | Build the all-link intertwiner / `6j` normalization instead of the scalar class-channel strip contraction. |
| analytic `P(6)` and repinning | Supply separate same-surface derivations; this note does not. |

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=34, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
