# Harmonic Depth Weight-Distribution Ordering: Bounded L=3 Realized-State Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome and does not edit audit-owned registry, ledger, queue,
or publication-status surfaces.
**Primary runner:** `scripts/frontier_depth_weight_distribution_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_depth_weight_distribution_2026_06_12.txt`

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Scope

This note is an exact finite-dimensional statement for the landed L=3 gauge-link
system and the four realized fillings used by the det-phase harmonic-depth
machinery:

- `K=3`, seed `391`
- `K=4`, seed `99`
- `K=5`, seed `99`
- `K=6`, seed `466`

It does not claim an asymptotic law, a generic-seed theorem, or a larger-Fock-space
statement.

## Anchors

The runner first reproduces the landed det-phase anchors:

| state | capture@order4, window 64 | rank, window 128, threshold 1e-6 | coupled gap count |
| --- | ---: | ---: | ---: |
| K=3 | 0.898130088565 | 71 | 3 |
| K=4 | 0.777619557343 | 84 | 3 |
| K=5 | 0.899155545493 | 36 | 3 |
| K=6 | 0.994936516891 | 35 | 3 |

The three external capture anchors are reproduced within the fixed `1e-2` tolerance:
the landed capture anchors are `0.995` for K=6 and `0.898`/`0.778` for K=3/K=4.
The equal gap-count inventory is exact: every state has the same three coupled tones.

## Weight Distribution

For each realized state, the runner computes the amplitude attached to each distinct
coupled spectral gap `g` by the landed eigenbasis-pair machinery:

`w_g = sum_{lambda_a-lambda_b=g} |(V* rho0 V)_{ab}| |(V* P_01 V)_{ba}|`.

The resulting tone tables are:

| state | w(-3) | w(0) | w(+3) | PR | entropy |
| --- | ---: | ---: | ---: | ---: | ---: |
| K=3 | 0.370985256951 | 2.544541431437 | 0.370985256951 | 1.600183529915 | 0.690591472333 |
| K=4 | 0.477687362555 | 3.088920133342 | 0.477687362555 | 1.635992331983 | 0.710433206511 |
| K=5 | 0.387343847004 | 3.891613207946 | 0.387343847004 | 1.409825406281 | 0.564589500331 |
| K=6 | 0.229806223341 | 4.683222031819 | 0.229806223341 | 1.200132406216 | 0.363022803006 |

Lower participation ratio here means fewer effective coupled tones, hence stronger
concentration. The measured concentration order is:

`K=6 -> K=5 -> K=3 -> K=4`.

This is the same order as the order-4 capture table. The K=3/K=4 pair is least
concentrated, and K=6 is the most concentrated.

## Synthetic Null

The runner applies a fixed cyclic shuffle of the same three weights over the same
three tones:

`new[-3] = old[0]`, `new[0] = old[+3]`, `new[+3] = old[-3]`.

This preserves the three-tone support but changes the depth-relevant gap moment:

| state | real gap2 | cyclic-null gap2 | delta |
| --- | ---: | ---: | ---: |
| K=3 | 2.031860749687 | 7.984069625156 | 5.952208875469 |
| K=4 | 2.126049862072 | 7.936975068964 | 5.810925206892 |
| K=5 | 1.494157662047 | 8.252921168977 | 6.758763506930 |
| K=6 | 0.804325326323 | 8.597837336838 | 7.793512010515 |

The null also reverses the center-share ordering away from the capture ordering:
`K=4 -> K=3 -> K=5 -> K=6`. In this gated realized-data check, equal support count
alone is not the ordering witness; the concentration ordering of the realized tone
weights matches the landed depth ordering on the four realized states.

## Bounded Claim

On this exact L=3 realized-state data, the gated claim is that the concentration
ordering of the realized coupling-weight distribution matches the landed det-phase
depth ordering on the four realized states. The count of coupled gaps is identically
three, while K=6 concentrates most strongly on the central tone and has the
smallest effective tone count, and K=3/K=4 are the least concentrated states.
Any broader causal or generative interpretation remains the named follow-on, not a
claim gated by this runner.

## Dependencies

- [`DET_PHASE_HARMONIC_DEPTH_STATE_DEPENDENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](DET_PHASE_HARMONIC_DEPTH_STATE_DEPENDENT_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  -- the landed realized-state capture-depth anchors and supplied state family.
- [`HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md`](HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  -- the rank/gap-count mechanism and the named weight-distribution follow-on
  closed by this finite realized-state table.
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  -- pointwise evaluation on supplied law-admissible realized states only; no
  state selection, typicality, weighting, or averaging rule is imported.
