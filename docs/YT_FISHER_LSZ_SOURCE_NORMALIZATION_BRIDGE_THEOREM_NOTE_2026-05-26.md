---
claim_id: yt_fisher_lsz_source_normalization_bridge_theorem_note_2026-05-26
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Fisher-LSZ Source Normalization Bridge Theorem

**Claim type:** bounded_theorem
**Role:** Route 1 normalization bridge support.
**Status:** exact support under an accepted isolated-pole source surface; no
retained or proposed-retained Y_T closure by this note alone.
**Primary runner:** `scripts/frontier_yt_fisher_lsz_source_normalization_bridge.py`
**Generated output:** `outputs/yt_fisher_lsz_source_normalization_bridge_2026-05-26.json`

## Theorem Statement

The Fisher-arclength theorem shows that the raw source-scale family

```text
S_h^(lambda) = S_0 - h lambda O
```

has an invariant source coefficient when read per unit Fisher arclength.  This
note proves the pole-row companion:

```text
For an accepted isolated one-particle pole, Fisher source arclength is the
same normalization as LSZ unit-residue normalization.
```

Equivalently, if a source operator `O` has pole residue

```text
C_OO(t) ~ A_O^2 exp(-m t),
```

then the Fisher metric for the source coupled to `O` is proportional to
`A_O^2`, and the LSZ-normalized operator is

```text
O_LSZ = O / A_O.
```

The Fisher-arclength source derivative gives the same normalized insertion:

```text
dS / d ell = - O / A_O = -O_LSZ.
```

Thus a strict same-surface pole-residue theorem can convert the previous
Fisher source unit into the usual canonical field normalization.  The remaining
physics gate is not a free scalar convention; it is the evidence/theorem that
the Y_T source has the accepted isolated pole and residue on the physical
top/Higgs transfer surface.

## Relation To The Pole-Row No-Go

[`YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md`](YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md)
proves that Gram purity alone cannot fix absolute normalization:

```text
Res(C_sH)^2 = Res(C_ss) Res(C_HH)
```

is invariant under independent source/Higgs rescalings.  This theorem does
not dispute that result.  It adds the missing positive statement:

```text
Once a same-surface pole residue is accepted as the LSZ residue, Fisher
arclength and LSZ unit-residue normalization are identical.
```

So pole rows are insufficient if they only prove rank-one purity.  They become
normalization evidence only when they include an accepted pole-residue
normalization surface.

## Proof

Assume a finite-volume Euclidean source family

```text
S_h = S_0 - h O.
```

For the connected generator `W(h) = log Z(h)`, the source curvature is

```text
W''(0) = <O O>_c.
```

On a single isolated pole, write the pole part of the correlator as

```text
C_OO(t) = A_O^2 exp(-m t) + excited terms.
```

After projecting to the one-pole residue surface, the source Fisher metric is

```text
I_O = A_O^2
```

up to a common positive kinematic factor fixed by the pole-projection
convention.  That common factor cancels in the normalized source coordinate.

The Fisher arclength coordinate is therefore

```text
ell = A_O h
```

at the origin.  Hence

```text
dS / d ell
  = (dS / dh) (dh / d ell)
  = (-O) (1/A_O)
  = -O_LSZ.
```

This is exactly the unit-residue LSZ insertion.

Under an operator rescaling

```text
O -> lambda O,
A_O -> lambda A_O,
```

the LSZ insertion is invariant:

```text
(lambda O) / (lambda A_O) = O / A_O.
```

The Fisher arclength insertion is invariant for the same reason:

```text
d ell_lambda / dh = lambda A_O,
dS_lambda / d ell_lambda = -lambda O / (lambda A_O).
```

Thus the source-scale ambiguity is removed exactly on the accepted
Fisher/LSZ pole-normalized surface.

## What This Moves

This note gives Route 1 a concrete review target:

```text
prove same-surface isolated-pole residue authority
  -> Fisher source arclength = LSZ unit-residue coordinate
  -> combine with six-component O_top theorem
  -> invariant top source component 1/sqrt(6)
```

It does not itself prove the first line.  The strict source-Higgs/top response
campaign still needs pole isolation, contact subtraction, finite-volume/IR
checks, and same-model-class evidence.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive `y_t`, `m_t`, `v`, or `g_2`;
- prove an isolated Higgs/top pole exists on the Y_T surface;
- prove canonical `O_H` from the qubit substrate;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, old Ward matrix-element
  authority, observed top/W/Z masses, PDG values, `alpha_LM`, plaquette/u0,
  Planck, alpha_s, or a fitted selector as proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
proposal_allowed_reason: |
  Fisher-LSZ normalization equivalence is exact once an accepted isolated-pole
  residue surface is supplied, but this note does not supply that physical
  pole-residue authority or a coefficient-certified top/W response row.
bare_retained_allowed: false
audit_required_before_effective_retained: true
remaining_bridge: >
  prove accepted same-surface pole-residue authority for the Y_T source/Higgs
  and top/W transfer rows, or measure strict same-source top/W responses.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_fisher_lsz_source_normalization_bridge.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
