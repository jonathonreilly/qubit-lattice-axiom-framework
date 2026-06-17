# CKM-EW Lattice A4 Bridge Boundary

**Date:** 2026-04-25

**Status (2026-06-17):** bounded-support EW-CKM lattice-scale bridge. The exact
arithmetic identity `sin^2(theta_W)|_lattice = A^4 = 4/9` is preserved as a
value-level bridge, but retained closure is dependency-gated on independent
audit of the EW, Wolfenstein, CKM-counts, and below-`W2` source rows. This note
does not itself apply an audit verdict or promote the bridge to retained status.

**Primary runner:** `scripts/frontier_ckm_ew_lattice_a4_bridge.py`

## Purpose

This note packages the lattice-scale EW-CKM bridge

```text
sin^2(theta_W)|_lattice = A^4 = 4/9
```

on the bounded-support source surface.

The companion theorem
[`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md)
now separately grounds

```text
A^2 = N_pair/N_color = 2/3
```

below `W2` from the companion quark-doublet source theorem. This note keeps the
EW-CKM bridge itself isolated as the lattice-scale corollary.

The value-level identity packaged here is:

```text
sin^2(theta_W)|_lattice = A^4 = 4/9.
```

The left side is supplied by the EW lattice-normalization lane. The right side
is supplied by the Wolfenstein `W2` lane. Retained closure requires those
dependencies to be independently clean on the current audit surface.

What is **not** claimed here is that the bridge note by itself re-derives
`A^2` below `W2` solely from the retained existence of `SU(2)_L` and
`SU(3)_c`.
The equality

```text
dim_fund(SU(2)) / dim_fund(SU(3)) = 2/3 = A^2
```

is a retained consistency equality at the accepted values. The actual
below-`W2` derivation now lives in the companion source theorem, not in this
corollary note alone.

## Inputs And Gates

| Input | Authority | Status |
| --- | --- | --- |
| `g_2^2 = 1/(d+1)`, `g_Y^2 = 1/(d+2)`, `d=3` | [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md) | EW algebraic/support input; not the v-scale `K_EW(kappa_EW)` matching rule |
| `A^2 = N_pair/N_color = 2/3` | [`WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md`](WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md) | dependency-gated CKM structural identity |
| below-`W2` source theorem for `A^2 = N_pair/N_color = 2/3` | [`CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md) | companion theorem; retained closure depends on audit |
| `N_pair=2`, `N_color=3` | [`CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md`](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | dependency-gated CKM structural-counts identity |
| `SU(2)_L`, `SU(3)_c` gauge structures | [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md) | framework/current-consequence surface |

Support-tier CL3 taste-generation readings are not used.

## Theorem 1: bounded lattice-scale EW-CKM bridge

On the EW lattice-normalization lane,

```text
g_2^2 = 1/(d+1),
g_Y^2 = 1/(d+2),
d = 3.
```

Therefore

```text
sin^2(theta_W)|_lattice
  = g_Y^2 / (g_Y^2 + g_2^2)
  = (1/(d+2)) / (1/(d+2) + 1/(d+1))
  = (d+1)/(2d+3)
  = 4/9.
```

On the CKM Wolfenstein lane,

```text
A^2 = 2/3,
```

so

```text
A^4 = 4/9.
```

Thus

```text
sin^2(theta_W)|_lattice = A^4 = 4/9.
```

This is an exact value-level identity at the lattice scale. It is not a claim
about the low-energy physical value of `sin^2(theta_W)` at `M_Z`.

## Theorem 2: gauge-dimension consistency equality

The framework gauge structures include `SU(2)_L` and `SU(3)_c`. Standard
representation theory gives

```text
dim_fund(SU(2)) = 2,
dim_fund(SU(3)) = 3.
```

Therefore

```text
dim_fund(SU(2)) / dim_fund(SU(3)) = 2/3.
```

Since `W2` gives

```text
A^2 = 2/3,
```

there is a value-level equality

```text
A^2 = dim_fund(SU(2)) / dim_fund(SU(3)) = 2/3.
```

This is a consistency identity between framework structures. The actual
below-`W2` derivation of the Wolfenstein `A^2` law now comes from the
companion quark-doublet source theorem; the equality in this note remains the
gauge-dimension corollary.

## Claim Boundary

What is certified here:

- `sin^2(theta_W)|_lattice = A^4 = 4/9`;
- `A^2 = dim_fund(SU(2))/dim_fund(SU(3)) = 2/3` as a value-level consistency
  equality;
- exact rational verification using EW and CKM source files.

What remains boundary-gated here:

- retained closure of the EW-CKM bridge before independent audit of the
  dependency rows;
- proof that the companion theorem closes `A^2` below `W2` on current `main`;
- an independent below-`W2` derivation inside this note alone;
- a promotion of `CL3_TASTE_GENERATION_THEOREM` or any support-tier theorem;
- a physical `M_Z` prediction for `sin^2(theta_W)`;
- a Koide closure or charged-lepton mass theorem.

## Reproduction

```bash
python3 scripts/frontier_ckm_ew_lattice_a4_bridge.py
```

Expected result:

```text
TOTAL: PASS=32, HARD_ISSUES=0
PASSED: 32/32
```

## Closeout Flags

```text
CKM_EW_LATTICE_A4_BRIDGE_BOUNDED_SUPPORT=TRUE
SIN2_THETA_W_LATTICE_EQUALS_A4=TRUE
GAUGE_DIMENSION_RATIO_EQUALS_A2_CONSISTENCY=TRUE
A2_BELOW_W2_DERIVATION_DEPENDENCY_GATED=TRUE
SUPPORT_TIER_PROMOTION=FALSE
KOIDE_CLOSURE=FALSE
```
