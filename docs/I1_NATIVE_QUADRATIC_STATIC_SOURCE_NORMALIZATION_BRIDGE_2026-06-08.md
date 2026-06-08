# I1 Native Quadratic Static-Source Normalization Bridge

**Date:** 2026-06-08
**Type:** bounded_theorem
**Status:** exact support for the native quadratic source-normalization subgap.
Independent audit owns any effective status.
**Runner:** `scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py`

## Claim

On the finite periodic `Z^3` lattice, after projecting away the zero mode, the
leading Wilson/graph-Laplacian gauge surface has the native source-normalized
quadratic action

```text
S[phi; J] = (1/(2 g^2)) <d phi, d phi> - <J, phi>.
```

Since `<d phi, d phi> = <phi, L phi>` for the graph Laplacian `L`, completing
the square gives

```text
L phi_* = g^2 J,
S_eff[J] = -(g^2/2) <J, L^+ J>.
```

For two static source records with channel signs `s_1, s_2`, the
separation-dependent cross term is therefore

```text
V_cross(r) = -g^2 s_1 s_2 G(r),
```

where `G = L^+` is the native zero-mean lattice Green kernel. In the massless
large-distance limit, the existing Green-kernel authority supplies
`G(r) -> 1/(4 pi r)`, so this source-normalization substep is the finite-lattice
origin of the `-g^2 G(r)` term used by the I1 relocation row.

## What This Closes

This closes only the native quadratic gauge-source action/normalization subgap
named by the conditional audit of
`I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06`.

The runner verifies:

- the stationary equation `L phi = g^2 J`;
- the completed-square identity `S_eff[J] = -(g^2/2) <J, L^+ J>`;
- the two-source cross term `V_cross(r) = -g^2 s_1 s_2 G(r)`;
- exact quadratic scaling in source amplitude;
- exact `g^2` coupling dependence;
- the native graph-Laplacian small-`k` normalization and the `1/(4 pi)`
  inverse-Laplacian coefficient.

## What This Does Not Close

This bridge does not derive the general energy-readout bridge. It does not close
the hierarchy magnitude, the Casimir/readout assignments, `u_0`, or any
phenomenological value. It does not add a new axiom and does not change any
audit result.

## Relation To I1

The parent I1 row had already shown that the static-source readout content can
be relocated from a standalone lattice-gauge readout convention to native
field-integration plus a framework-wide energy-readout bridge. The present note
supplies the missing finite-lattice source-normalization derivation for the
native field-integration half:

```text
native quadratic field + static source -> -g^2 G(r).
```

After this bridge, the remaining I1 blocker is narrower: the general
energy-readout bridge remains open, but the native quadratic source
normalization is no longer an imported convention inside the I1 packet.

## Verification

```bash
python3 scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py
```

Expected:

```text
TOTAL: PASS=18 FAIL=0
```
