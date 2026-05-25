---
claim_id: yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Source-Coordinate Invariant Top/W Ratio Gate

**Claim type:** bounded theorem / exact support.
**Status:** support theorem; no positive Y_T closure.
**Primary runner:** `scripts/frontier_yt_source_coordinate_invariant_top_w_ratio_gate.py`
**Generated output:** `outputs/yt_source_coordinate_invariant_top_w_ratio_gate_2026-05-25.json`

This note sharpens the remaining Y_T source-Higgs blocker.  The top/W
Feynman-Hellmann route does **not** need a canonical absolute source coordinate,
nor a derived numerical slope from the signed-record source to the EW radial
coordinate.  It only needs both pole masses to be differentiated with respect
to the same local source coordinate on the same EW radial surface.

## Theorem

Let `h` be any local scalar source coordinate and let the neutral EW radial
background be

```text
H(h) = (0, v(h)/sqrt(2))^T,
```

where `v'(h_0) != 0` at the expansion point.  Assume the same local transfer
surface gives

```text
M_t(h) = y_t v(h) / sqrt(2),
M_W(h) = g_2 v(h) / 2.
```

Then

```text
dM_t/dh = (y_t/sqrt(2)) v'(h),
dM_W/dh = (g_2/2) v'(h),
```

and therefore

```text
y_t = (g_2/sqrt(2)) (dM_t/dh)/(dM_W/dh).
```

The unknown Jacobian `v'(h)` cancels.  More generally, for any local
reparameterization `h = f(s)` with `f'(s_0) != 0`, both derivatives acquire the
same factor `f'(s)`, so the ratio is unchanged.

## Consequence

The scalar-source problem is narrower than a full canonical `O_H` problem.

The route does **not** need:

- a fixed source-side covariance normalization;
- a canonical source knob;
- a numerical slope between signed-record source units and Higgs radial units;
- `H_unit`;
- the old Ward identity.

After the carrier-ray bridge in
[`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md),
the signed-record source is aligned with the neutral `P_-` Higgs ray up to an
affine source reparameterization.  The route still needs:

1. an accepted same-surface EW transfer-response theorem saying the neutral
   carrier-ray source is the physical radial coordinate on the top and W
   transfer surfaces;
2. top and W isolated-pole response rows on that same source;
3. retained `g_2` authority, or a deliberately scoped `y_t/g_2` result;
4. matching/running if the claim is a physical-scale `y_t`.

## Why This Is Not A Renaming

This note does not name the signed-record source "the Higgs" and then read off
`y_t`.  It proves a coordinate-invariance fact: if a later retained theorem
supplies a common EW radial source, the top/W response ratio does not depend on
which local coordinate parametrizes that source.  The physical EW carrier
authority remains outside this note.

## Non-Claims

This note does not:

- derive full same-surface EW transfer response from signed records;
- derive `y_t`;
- derive `m_t`;
- derive `g_2`;
- derive `v = 246 GeV`;
- certify strict top/W response rows;
- use observed W/Z/top masses, fitted selectors, `H_unit`, `yt_ward_identity`,
  `y_t_bare`, `alpha_LM`, or plaquette/u0 as proof inputs.

## Verification

```text
python3 scripts/frontier_yt_source_coordinate_invariant_top_w_ratio_gate.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```

The green result means the source-coordinate normalization blocker is removed
for the same-source top/W ratio.  It does not mean retained Y_T closure has been
obtained.
