# Flavor Carrier Momentum Type From Translation Theorem

**Date:** 2026-06-15
**Claim type:** bounded_theorem
**Status:** source-side carrier-type split; no audit verdict or effective-status
change.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py`](../scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py)

## Purpose

This note splits the clean carrier-type theorem out of
`FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md`.

The parent note was audited conditional because it combines:

1. a clean carrier-type theorem: translation symmetry puts
   flavor-separating observables on the momentum/BZ factor rather than on
   local position observables;
2. an open physical-locus bridge: forcing the physical generation locus to be
   the staggered/KS `hw=1` triplet.

This split proves only item 1. It does not claim that the physical generation
locus is forced to be `hw=1`.

## Theorem

On the finite periodic `2 x 2 x 2` framework representative with commuting
translation unitaries `T_x, T_y, T_z`, the joint character basis gives a
framework-native momentum/BZ decomposition. Local position-diagonal
observables are generation-blind on the character states, while momentum-block
projectors separate corner labels. Therefore, within the position-diagonal
local readout class tested here, flavor-separating label resolution is supplied
by the momentum/BZ factor, not by local position weights.

For the supplied `hw=1` three-corner sector, this becomes:

- the three `hw=1` corners have distinct joint translation characters;
- the `C_3[111]` rotation permutes them transitively;
- every diagonal position observable has equal expectation across the three
  character states;
- a momentum projector onto one corner separates the three labels;
- the extensive position `Gamma_5 = (-1)^(x+y+z)` sum vanishes on the full
  periodic cell.

## Proof Sketch

The runner constructs the three translation permutation matrices on the
periodic `2 x 2 x 2` cell and verifies they are commuting unitaries. It then
constructs the eight explicit `Z_2^3` character vectors

```text
psi_k(n) = (-1)^(k.n) / sqrt(8),
```

checks that they are an orthonormal simultaneous eigenbasis, and forms the
rank-one momentum projectors `P_k = |psi_k><psi_k|`.

For any diagonal position observable `O = diag(w_n)`,

```text
<psi_k, O psi_k> = (1/8) sum_n w_n,
```

so no position-diagonal local observable separates the `hw=1` characters. By
contrast, `P_k` gives Kronecker separation on the momentum labels.

## Boundary

This note does not prove:

- that the physical generation locus is `hw=1`;
- that staggered/Kawamoto-Smit chirality is forced by the baseline;
- that the continuous Koide basepoint `r = 1/2` is derived;
- that the index-density readout `delta = 2/9` is selected;
- any audit verdict.

The open bridge remains the parent audit's named blocker: derive the
staggered/KS `hw=1` physical generation locus from retained framework inputs,
or keep downstream claims conditional on that bridge.

## Verification

Run:

```bash
python3 scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py
```

Expected:

```text
TOTAL: PASS=10 FAIL=0
```
