---
claim_id: sm_gstar_hunit_neutral_radial_orbit_support_note_2026-06-18
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# SM g_* H_unit Neutral/Radial Orbit Support

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Role:** exact support / bounded support.
**Status:** exact support for a supplied-doublet radial carrier boundary; no
positive `g_*` status change.
**Primary runner:** [`scripts/frontier_sm_gstar_hunit_neutral_radial_orbit_2026_06_18.py`](../scripts/frontier_sm_gstar_hunit_neutral_radial_orbit_2026_06_18.py)
**Runner cache:** [`logs/runner-cache/frontier_sm_gstar_hunit_neutral_radial_orbit_2026_06_18.txt`](../logs/runner-cache/frontier_sm_gstar_hunit_neutral_radial_orbit_2026_06_18.txt)
**Generated output:** [`outputs/sm_gstar_hunit_neutral_radial_orbit_support_2026-06-18.json`](../outputs/sm_gstar_hunit_neutral_radial_orbit_support_2026-06-18.json)

## Claim

On an already supplied one-complex-`SU(2)_L` Higgs doublet surface, the
`H_unit` scalar-singlet structure can support only a scalar/radial carrier
statement: the invariant radius of the supplied doublet and, after gauge
choosing a representative, the neutral ray. It cannot by itself supply the four
real thermal components of the full doublet.

Equivalently:

```text
supplied doublet H in C^2
  -> invariant radius rho = sqrt(H^\dag H)
  -> SU(2) orbit representative H_neutral = (0, rho)^T
  -> one radial carrier direction compatible with H_unit scalar support
```

but not:

```text
H_unit scalar singlet -> full one-complex SU(2)_L thermal doublet.
```

## Inputs

Load-bearing source surfaces:

- [`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  for the `H_unit` scalar-singlet structure on the `Q_L=(2,3)` block.
- [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
  for the one-doublet electroweak bookkeeping surface, `Y_H=1/2`, and the
  neutral representative.
- [`HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md`](HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md)
  for the route-pruning boundary that no nonzero equivariant bridge exists
  from the `SU(2)_L` singlet to the fundamental doublet.
- `SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md` is the downstream
  `R-HIGGS` census residual this support note is meant to clarify. It is named
  here as target context, not as a load-bearing input to this support lemma.

No observed Higgs count, Standard Model census value, PDG number, fitted
selector, new axiom, audit verdict, or premise registration is used.

## Orbit And Radial Lemma

Let `H = (a,b)^T in C^2` be nonzero and set

```text
rho = sqrt(|a|^2 + |b|^2).
```

For the normalized vector `(alpha,beta) = (a/rho,b/rho)`, define

```text
U(H) =
  [  beta      -alpha  ]
  [  alpha^*    beta^* ].
```

Then `U(H)` is an `SU(2)` matrix:

```text
U(H)^\dag U(H) = I,
det U(H) = |alpha|^2 + |beta|^2 = 1,
```

and it gauges the supplied doublet to the neutral representative:

```text
U(H) H = (0, rho)^T.
```

The radius is invariant:

```text
H^\dag H = (U H)^\dag (U H) = rho^2.
```

With `T_3 = diag(1/2,-1/2)`, `Y_H = (1/2) I`, and `Q = T_3 + Y_H`, the lower
representative is electromagnetically neutral:

```text
Q (0, rho)^T = 0.
```

Thus the supplied doublet decomposes into one invariant radial coordinate plus
an `S^3` `SU(2)` orbit of representatives. The broken-phase neutral gauge
choice can display the radial carrier, but it does not erase the high-T
four-real-component field content of the doublet.

## Relation To `H_unit`

The Ward theorem's `H_unit` is scalar on the isospin factor. It commutes with
all `SU(2)_L` generators and therefore cannot choose a fundamental doublet
orientation. The representation no-go proves the stronger boundary

```text
Hom_SU(2)(trivial, fundamental) = 0.
```

This packet records the positive part left by that no-go. Once the one-doublet
surface is supplied independently, a scalar source can be interpreted as a
local radial coordinate on the invariant `rho` direction, and the neutral
representative is a gauge choice inside the supplied doublet. That is valid
support for scalar/radial carrier language; it is not field-content authority.

## Consequence For The `g_*` Higgs-Sector Row

The downstream `g_*` Higgs-sector count row uses the retained-bounded declared
SM finite-inventory premise for one complex Higgs doublet. Under that premise,
the Higgs-sector contribution is four real scalar dof and the census is
`g_* = 106.75`.

This support note does not replace that premise. It only sharpens why `H_unit`
can be used as native scalar/radial support without being misread as a
framework-native derivation of the complete thermal doublet:

- a single supplied complex doublet has four real scalar dof;
- its invariant radial coordinate is one real carrier direction;
- the neutral representative is a ray inside the supplied doublet;
- a second thermalized doublet would add a second independent `C^2` field and
  `+4` to the census, not merely another scalar/radial coordinate.

## What This Closes

This note closes the narrow support ambiguity:

```text
If the one-doublet surface is already supplied, can H_unit-compatible scalar
support be aligned with the neutral/radial carrier without adding a second
thermalized doublet?
```

Answer: yes. The alignment is the invariant radius and its neutral
representative on the supplied `SU(2)_L` doublet orbit.

## What This Does Not Close

- It does not derive the one-complex `SU(2)_L` EWSB thermal doublet from
  `H_unit`.
- It does not promote the `g_*` Higgs-sector row, retag the ledger, or set an
  audit verdict.
- It does not introduce a new axiom, Tier-A admission, fitted selector, or
  observed-value input.
- It does not prove Higgs potential dynamics, thermal equilibrium, hypercharge
  uniqueness, or physical-scale `g_2(v)`.
- It does not alter the retained-bounded declared-inventory premise consumed
  by the `g_*` Higgs-sector row.

## Review Boundary Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  The supplied-doublet radial/orbit support is closed, but it does not supply
  the full one-complex SU(2)_L thermal doublet field content. The downstream
  g_* row still relies on the retained-bounded declared-inventory premise for
  field content, with independent audit required for any effective status
  change.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_sm_gstar_hunit_neutral_radial_orbit_2026_06_18.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
