---
claim_id: yt_primitive_source_unit_fisher_normalization_support_note_2026-05-25
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Primitive Source-Unit Fisher Normalization Support

**Claim type:** bounded_theorem
**Role:** conditional / bounded support theorem.
**Status:** exact support under the source-family and source/action premises;
no positive Y_T closure by this note alone.
**Primary runner:** `scripts/frontier_yt_primitive_source_unit_fisher_normalization.py`
**Generated output:** `outputs/yt_primitive_source_unit_fisher_normalization_2026-05-25.json`

This note proves the best available `lambda = 1` statement for Y_T source-action.

```text
primitive signed-record source unit
  + source-coupled local action convention
  -> lambda = 1.
```

It does **not** prove the source/action convention from the
qubit-at-each-`Z^3`-site baseline alone.  The
paired no-go note
[`YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md`](YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md)
remains true: without a source-unit premise, the family
`y_33(lambda)=lambda/sqrt(6)` is not selected by current carrier/W/Z/LSP
support alone.

## Theorem Statement

Let `epsilon in {-1,+1}` be the primitive signed qubit record supplied by the
ideal projective Pauli readout.  On the uniform pre-source reference, the
canonical one-parameter Radon-Nikodym source family is

```text
R_h(epsilon) = exp(h epsilon) / cosh(h).
```

Its score at the origin is

```text
d log R_h(epsilon) / dh |_{h=0} = epsilon,
```

and its Fisher information at the origin is

```text
I(0) = E[epsilon^2] = 1.
```

For a scaled family

```text
R_h^(lambda)(epsilon) = exp(h lambda epsilon) / cosh(lambda h),
```

the score and Fisher information become

```text
score_lambda(0) = lambda epsilon,
I_lambda(0) = lambda^2.
```

Therefore requiring the physical source coordinate to be the primitive
signed-record unit coordinate forces

```text
lambda = 1.
```

Equivalently, `lambda != 1` is not new physics in this source family; it is a
rescaling of the source coordinate away from primitive signed-record units.

## Six-Component Top Trilinear Source

For the normalized six-component color-isospin top carrier,

```text
u_dem = (1,1,1,1,1,1)/sqrt(6),
O_top = sum_i u_dem(i) O_i,
```

the primitive signed-linear source family is

```text
R_h(O_top) = exp(h O_top) / Z(h).
```

At the origin,

```text
d log R_h / dh |_{h=0} = O_top,
```

so every component tangent is exactly

```text
u_dem(i) = 1/sqrt(6).
```

A scaled source family gives `lambda O_top` and Fisher norm `lambda^2`.
Requiring the primitive unit Fisher/source coordinate on the normalized
operator gives `lambda = 1`, hence

```text
y_33 = 1/sqrt(6)
```

on the conditional source/action branch.

## Action-Source Bridge

The source-coupled local action convention states that local source
derivatives of the action define the coupled local operator insertions:

```text
S_h = S_0 - h O.
```

In a finite-volume Gibbs/RN reading, this changes the density by

```text
dP_h/dP_0 = exp(h O) / E_0[exp(h O)].
```

Thus the unit coefficient in the action source is exactly the natural
Radon-Nikodym/Fisher unit above.  Under this convention,

```text
S_h = S_0 - h O_top
```

is the primitive source-unit deformation, while

```text
S_h = S_0 - h lambda O_top
```

has Fisher norm `lambda^2` and is not the primitive unit coordinate unless
`lambda = 1`.

## What This Closes

This note closes the scalar unit **inside** the canonical source-family /
source-action branch:

```text
primitive signed-record source unit
  -> lambda = 1
  -> y_33 = 1/sqrt(6)
```

No color/isospin, LSP-probability, W/Z-denominator, or top/W-ratio algebra is
left to fix `lambda` once this source unit is accepted.

## What This Does Not Close

This note does not prove positive retained Y_T closure.  It does not claim:

- the qubit-at-each-`Z^3`-site baseline alone already supplies the
  source-coupled local action convention;
- the LSP signed-record source support has been independently audited clean;
- the physical top Yukawa deformation has been identified with the primitive
  source/action tangent on the current retained surface;
- retained one-Higgs/top carrier authority;
- retained same-scale `g_2`;
- physical matching/running closure.

The remaining global closure question is therefore:

```text
Can the source-coupled local action convention be promoted/derived strongly
enough that the primitive source unit applies to the physical top Yukawa
deformation?
```

If yes, this packet supplies the `lambda=1` proof.  If no, the direct
measurement route remains necessary.

## Why This Is Not The Old Ward Trap

This packet does not use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed
W/Z/top masses, PDG values, `alpha_LM`, plaquette/u0, package-v, Planck,
alpha_s, or a fitted selector as proof inputs.

The old failure hid the physical identification inside a definition of a
matrix element.  Here the identification is explicit: the only conditional
premise is that the physical top source is the primitive unit source/action
deformation.

## Verification

Run:

```text
python3 scripts/frontier_yt_primitive_source_unit_fisher_normalization.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21](OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md)
- [yt_lsp_signed_record_source_readout_support_note_2026-05-24](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md)
