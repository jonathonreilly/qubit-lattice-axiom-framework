# Koide: the C3 doublet-count is not a measure to select — it is two observables (mass ratio Q=2/3 and spectral asymmetry 2/9)

**Date:** 2026-05-31
**Claim type:** bounded structural reframe (positive) — dissolves the per-block-vs-per-dimension "selection problem"
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
**Primary runner:**
`scripts/frontier_koide_three_measures_three_observables_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_three_measures_three_observables_2026_05_31.txt`.

## Result (one sentence)

The long "which `C_3`-isotype measure is *the* Koide measure" question — per-block
(`Q=2/3`) vs per-dimension (`Q=1`) — was ill-posed: the two natural counts of the
complex-type generation doublet compute **two different, separately-realized invariants**
of the same `C_3` structure — the **mass ratio** (`Q=2/3`, count-once) and the **spectral
asymmetry** (`L_3(1,2)=2/9`, count-twice) — so there is nothing to select.

## The structure

With `Q=(1+2r)/3`, `r=|b|^2/a^2`, and block weights `(mu,nu)` on the (singlet, doublet)
`C_3`-isotypes giving extremum `r*=nu/(2 mu)` (F1):

| weight `(mu,nu)` | `r*` | `Q` | reading |
|---|---|---|---|
| democratic `(1,0)` | `0` | `1/3` | degenerate / symmetric limit |
| equal-block `(1,1)` | `1/2` | `2/3` | the **mass ratio** (charged leptons) |
| dimension / Plancherel `(1,2)` | `1` | `1` | the **dimension count** |

The **dimension count is the spectral asymmetry** (F2): the retained_bounded finite `Z_N`
equivariant spectral-asymmetry / Lefschetz weight
`L_N(a) = (1/N) sum_{k=1}^{N-1} prod_j 1/(zeta_N^{k a_j}-1)` evaluates to
`L_3(1,2) = 2/9` exactly, and `2/9 = (N-1)/N^2 = (doublet dimension 2)/N^2`.

## One count, two observables

The single binary "count the `C_3` doublet **once** (over its Wedderburn block) or
**twice** (over its real dimension)" produces **both** readouts (F3):

- **count-once (block)** `-> ` the magnitude / **mass-ratio** observable `Q=2/3`;
- **count-twice (dimension)** `-> ` the sign / **spectral-asymmetry** observable
  `L_3(1,2)=2/9`.

So `Q=1` is **not** a competing *wrong* mass ratio — it is the dimension count whose
**spectral** readout is the retained `2/9`. The mass-ratio observable and the
spectral-asymmetry observable are different invariants of the same operator, and **both
are realized** (F4): the charged-lepton Koide mass ratio is `2/3` (equal-block readout,
on the physical `r=1/2` configuration), and the `C_3` spectral asymmetry is `2/9`
(dimension readout, retained_bounded).

## Why this dissolves the "force r=1/2" problem

Asking "is `r=1/2` forced over `r=1`?" conflates two observables. The mass-ratio
observable **is** `2/3` and the spectral-asymmetry observable **is** `2/9`; neither needs
to "beat" the other, and the framework reproduces **both** with its two natural counts —
a feature, not an ambiguity. The operator-level search for a principle to *select* the
block measure was solving a non-problem: the block count is the right one **for the mass
ratio**, the dimension count is the right one **for the spectral asymmetry**.

## Boundary

This is a **reframe**, not a new derivation of either value: the mass ratio `2/3` and the
spectral weight `2/9` are each computed by their own count, both already retained-grounded
(the block surface `koide_q23_block_weight_frontier` for `2/3`; the spectral-asymmetry
theorem `axiom_first_z_n_equivariant_spectral_asymmetry` for `2/9`). What it removes is
the false premise that one weight must be *selected* as the unique physical measure. (The
Brannen phase `delta=2/9` **rad** is a third, `Q`-orthogonal charged-lepton datum,
separated from the dimensionless `L_3=2/9` by the radian-bridge no-go
`koide_a1_radian_bridge_irreducibility`.)

**The next path** (sharper, now that the framing is corrected): which physical *channel*
of the charged-lepton sector reads the mass ratio (the eigenvalue magnitudes, the
block/equal-energy structure) vs the spectral asymmetry (the signed spectral flow, the
dimension/Lefschetz structure) — both are present in the same circulant operator; the task
is to identify the observable each native readout corresponds to, not to suppress one.

## Anchors (live-ledger tiers)

retained / retained_bounded: `axiom_first_z_n_equivariant_spectral_asymmetry`
(retained_bounded), `koide_q23_block_weight_frontier` (retained_bounded),
`koide_circulant_q_two_thirds_algebraic`, `koide_a1_radian_bridge_irreducibility`
(retained_no_go). Complements `KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE` and
`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE`.
