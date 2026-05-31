# Koide: one generation operator, three physical readouts — scale (Q=1/3), ratio (Q=2/3), asymmetry (2/9)

**Date:** 2026-05-31
**Claim type:** bounded structural map (positive) — the constructive readout-to-channel identification
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
**Primary runner:**
`scripts/frontier_koide_readout_channel_map_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_readout_channel_map_2026_05_31.txt`.

## Result (one sentence)

The three `C_3`-isotype weights are not rival "Koide measures" to select — they are the
three natural **readouts of one circulant generation operator** `H = aI + bC + b-bar C^2`,
each measuring a different physical channel: the **scale** (singlet, `r=0`, `Q=1/3`), the
**ratio** (doublet magnitude, `r=1/2`, `Q=2/3`), and the **asymmetry** (doublet sign /
dimension, `r=1`, `L_3=2/9`).

## The decomposition

The `C_3` Fourier transform splits `H` into a **singlet** amplitude `a = Tr(H)/3` (the
generation-uniform `(1,1,1)` direction) and a **doublet** amplitude `b = (1/3)Tr(C^-1 H)`
(the generation-difference directions). The singlet axis `(1,1,1)` is `C_3`-fixed and
generation-uniform — it is the direction that **generation-blind** charges (em,
hypercharge) couple to, weighting all three generations equally.

## The three channels

**Channel 1 — SCALE (the third `r`: `r=0`, democratic weight `(1,0)`, `Q=1/3`).** The
singlet `a` is the **overall mass scale** — the flavor-**universal**, generation-blind
piece common to all three generations. At `b=0` (pure singlet) the three masses are
**degenerate** (the fully-`C_3`-symmetric configuration), whose Koide value is `Q=1/3`
(the democratic floor). So **the third `r` is the flavor-universal overall mass scale /
the degenerate-symmetric base** that the doublet then splits.

**Channel 2 — RATIO (`r=1/2`, equal-block weight `(1,1)`, `Q=2/3`).** The doublet
**magnitude** `|b|` sets the flavor **splitting**; with `r=|b|^2/a^2` and `Q=(1+2r)/3`,
the equal-block (mass-ratio) reading gives `r=1/2 -> Q=2/3` = the charged-lepton Koide
relation.

**Channel 3 — ASYMMETRY (`r=1`, dimension weight `(1,2)`).** The doublet's **signed /
spectral** content gives the finite `Z_N` equivariant spectral asymmetry
`L_3(1,2) = 2/9` (the eta / Lefschetz weight, retained_bounded). Separately, the doublet
**phase** `arg(b) = delta` is the CP / orientation datum (Brannen `delta = 2/9` rad),
which is `Q`-**orthogonal** (verified: `Q` depends only on `|b|`).

## One operator, three complementary observables

All three live in the **same** `H`: the eigenvalue **magnitudes** carry the scale
(singlet) and the ratio (doublet magnitude); the eigenvalue **signs / spectral flow**
carry the asymmetry; the doublet **phase** carries CP. The charged-lepton sector realizes
all of them — an overall scale, the ratio `2/3`, the asymmetry `2/9`, the phase `2/9` rad
— so the readouts are **complementary observables, not competitors**, exactly as the
reframe (`KOIDE_THREE_MEASURES_THREE_OBSERVABLES_NOTE`) requires.

## Boundary

This is the constructive channel map, not a new derivation of any single value. It
identifies *which physical quantity each native readout measures*: magnitudes → scale +
ratio, signs → asymmetry, phase → CP. The map makes explicit that the previously-feared
"measure ambiguity" is the generation operator carrying **three** independent charged-
lepton data (scale, ratio, CP/asymmetry) on its three `C_3` channels.

**The next path:** identify the physical interaction that *reads* each channel — a
generation-blind coupling (gauge/Higgs-universal) reads the scale; a flavor-texture
coupling reads the ratio; a CP/anomaly-sensitive coupling reads the sign/asymmetry — so
each channel's value is observed in its own sector rather than competing for one number.

## Anchors (live-ledger tiers)

retained / retained_bounded: `axiom_first_z_n_equivariant_spectral_asymmetry`
(retained_bounded), `koide_q23_block_weight_frontier` (retained_bounded),
`koide_circulant_q_two_thirds_algebraic`, `three_generation_observable`,
`koide_a1_radian_bridge_irreducibility` (retained_no_go). Complements
`KOIDE_THREE_MEASURES_THREE_OBSERVABLES_NOTE`.
