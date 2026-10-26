# Supplied shifted-relative-action finite packet diagnostic

**Type:** open_gate
**Date:** 2026-04-21
**Status:** finite supplied numerical comparisons; physical selection open
**Primary runner:** `scripts/frontier_dm_selector_shifted_relative_action_recovered_packet_closure_2026_04_21.py`

## Supplied construction and premises

The five recovered lifts, fixed `H_SEED`, repairs and `SHIFT_OFFSETS` are supplied inputs. For each tested common shift, stipulate `A_mu(H)=H+mu I` and the scalar

```text
S_mu(H || H_seed)
 = Tr(A_mu(H_seed)^(-1) A_mu(H))
   - log det(A_mu(H_seed)^(-1) A_mu(H)) - 3.
```

Using this formula on positive-definite windows is a specified mathematical construction; neither the formula's physical selection nor positivity for an arbitrary physical source follows from documentary text. The runner retains its original floating implementation and all failure conditions. The seed and bank are not derived here.

## Finite checks

The runner compares all five bank entries for each supplied `SHIFT_OFFSETS` value above the computed `mu_floor=max_i repair(H_i)`. It also compares the same entries at sixty points from three original `linspace` grids, and at one additional point `mu_floor+1e6`. The grids, repeated endpoints, scalar implementation, argmin tie behavior, margins (`1e-9`, and `1e-18` at the far point) and sign predicates are unchanged.

These checks report whether lift 0 has the smallest floating value at those points. Sixty samples are not a continuum interval proof; one large-shift value is not an asymptotic theorem. Exact minimizer/sign claims require separate numerical enclosures or analytical proof. No absent competitor outside the supplied bank is excluded.

The same runner computes `Im(K_Z3[1,2])` on the five entries and compares the positive-sign entry with the sampled scalar minimizer. This is a finite supplied-table correlation, not a physical selection mechanism.

## Documentary dependencies and withdrawn authority

The relative-action, projection and shifted-sign notes are read as documentary context. Their historical exact/canonical-selector statements are not proof premises for these computations. The current projection and sign diagnostics distinguish finite supplied calculations from earlier stronger prose. Substring checks report text only. The former literal-True transport narration is unscored.

The [independent finite owner](DM_SELECTOR_SUPPLIED_BANK_SEED_RELATIVE_ACTION_FINITE_DIAGNOSTIC_NOTE_2026-10-23.md) provides the self-contained supplied-bank comparison scope; this older integrated reader additionally checks documentary context. Neither owner establishes a physical law. The source-cubic companion's supplied rows do not constitute complete exact-target enumeration or derive a positivity selector.

The earlier claim that an exact/canonical closure stack and threshold law are all thereby justified is withdrawn. Physical branch choice, bank provenance, selector normalization, continuum inequalities and complete source coverage remain open. Original source/cache bytes and stronger claims remain in predecessor `e9bf37ecba6baed5aa02bc52980c5e7d97241d1d` and external repair recovery; old PASS counts are historical, not current authority.
