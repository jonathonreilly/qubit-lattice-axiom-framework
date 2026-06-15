---
claim_id: hunit_to_ewsb_doublet_representation_no_go_note_2026-06-15
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# H_unit to EWSB Doublet Representation No-Go

**Date:** 2026-06-15
**Type:** no_go / exact-support boundary.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, retag any row, or promote the `g_*` Higgs-sector count.
**Primary runner:** `scripts/hunit_to_ewsb_doublet_representation_no_go_2026_06_15.py`

## Claim

On the current authority surface, the direct bridge

```text
H_unit scalar-singlet structure  ->  one complex SU(2)_L EWSB doublet
```

does not exist as an equivariant derivation. The retained-bounded Ward packet
identifies `H_unit` as the unit-normalized scalar singlet on the
`Q_L = (2,3)` block. That object carries the trivial `SU(2)_L`
representation. A high-temperature EWSB Higgs field-content assertion,
however, asks for a full complex `SU(2)_L` fundamental doublet, whose real
thermal census has four scalar components.

There is no nonzero `SU(2)`-equivariant linear map from the trivial
representation to the fundamental doublet:

```text
Hom_SU(2)(1, 2) = 0.
```

Therefore `H_unit` alone can support scalar-singlet or neutral-ray/radial
carrier statements only after an already supplied one-doublet bookkeeping
surface is present. It cannot itself derive the full one-complex-doublet
thermal field content.

## Inputs

The proof uses only representation bookkeeping already present in the source
surface:

- `YT_WARD_IDENTITY_DERIVATION_THEOREM.md` for the scalar-singlet
  `H_unit` structure on `Q_L`.
- `EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md` for the
  one-doublet electroweak bookkeeping surface: `H = (H^+, H^0)^T`,
  `Y_H = 1/2`, `Q = T_3 + Y`, and the neutral ray.
- `YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md` for the
  already audited bounded support that a signed-record source aligns with the
  neutral ray once the one-doublet surface is supplied.

No observed Higgs count, Standard Model census value, PDG number, fitted
selector, new axiom, or accepted-premise registration is used.

## Proof

Let `V_0 = C` be the trivial representation and `V_2 = C^2` the fundamental
`SU(2)` doublet. An equivariant bridge `T : V_0 -> V_2` is determined by one
vector `v = T(1)`. Equivariance requires

```text
U v = v
```

for every `U in SU(2)`. Infinitesimally, this requires

```text
sigma_i v = 0,  i = 1,2,3.
```

The Pauli generators have no common nonzero kernel in the fundamental doublet,
so `v = 0`. Hence no nonzero equivariant map exists.

The same obstruction is visible on the operator side. In the Ward packet,
`H_unit` is proportional to the identity on the isospin factor:

```text
H_unit = I_2 tensor I_3 / sqrt(6).
```

It commutes with all `SU(2)_L` generators and is therefore an isospin scalar.
By contrast, the one-Higgs doublet surface has component projectors
`P_+` and `P_-` that do not commute with the off-diagonal `SU(2)` generators;
selecting the neutral ray is a gauge/ray statement inside an already supplied
doublet, not a derivation of that doublet from a singlet.

## Consequence For R-HIGGS

This no-go sharpens the remaining blocker in
`SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md`.

The viable routes are:

1. supply a separate retained-grade or accepted-premise authority for the
   one-complex-`SU(2)_L` thermal EWSB doublet field content; or
2. keep the `g_* = 106.75` Higgs-sector row conditional on that named
   field-content bridge.

The nonviable route is:

```text
derive the full one-doublet thermal census directly from H_unit scalar-singlet
uniqueness.
```

This packet therefore does not close R-HIGGS positively. It closes a false
bridge route and prevents a scalar-singlet support theorem from being reused
as a full thermal-doublet derivation.

## What This Does Not Claim

- It does not refute the one-Higgs electroweak bookkeeping theorem.
- It does not refute the conditional `g_* = 106.75` arithmetic.
- It does not prove a two-Higgs-doublet model or `g_* = 110.75`.
- It does not derive hypercharge, physical Higgs potential dynamics, or
  thermal equilibrium.
- It does not add an axiom or accepted premise.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/hunit_to_ewsb_doublet_representation_no_go_2026_06_15.py
```

Expected result:

```text
TOTAL: PASS=34 FAIL=0
```
