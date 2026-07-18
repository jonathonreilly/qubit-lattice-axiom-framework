# First-contact boundary diagnostic — Cycle 199

Date: 2026-07-16

Status: exploratory source-grade diagnostic; audit unset

Authority: none

Companion runner:
`scripts/first_contact_boundary_diagnostic_cycle199_2026_07_16.py`

This note and companion runner are committed only on the draft parking branch
and referenced by draft PR #5389; no foundation, axiom, primitive, registry,
policy, audit, or queue surface is changed.

## Result

Moving the Cycle-193 R2 bounding slab one lattice step toward the Cycle-190
hard apparatus, from x-offset 133 to 132, closes the open slab layer. It does
not produce occupied-record contact. Bounding-slab contact is not
occupied-record contact.

The exact occupied-support approach profile is:

| R2 x-offset | Minimum occupied-support distance | Contact pairs |
|---:|---:|---:|
| 132 | 4 | 0 |
| 131 | 3 | 0 |
| 130 | 2 | 0 |
| 129 | 1 | 1 |

At the requested one-step placement, there is no mixed local signature. The
joint minimum and maximum histories retain transparent closure:

```text
states                    6,677
edges                     8,615
unordered writes              0
terminal continuations       10
```

The first mixed open-site signature occurs at offset 130, before occupied
records touch. At target `(7,3,-3)` it is exactly:

```text
R_A13 at -x
MARK   at +x
```

No existing row acts on that signature. The complete joint replay nevertheless
has the same transparent closure: 6,677 states, 8,615 edges, zero unordered
writes, and ten inherited terminal continuations. The mixed signature is inert
under the present full deterministic candidate raw table.

The first occupied-record contact occurs one step later at offset 129:

```text
(6,3,-3)  R_A13  --  MARK  (7,3,-3)
```

Both records are fixed initial records. Cycle 199 stops at that exact contact
census; it does not call adjacency an interaction and does not infer gate
semantics.

## Licensed reading

This diagnostic distinguishes three different geometrical boundaries:

1. adjacent bounding slabs at offset 132;
2. a first mixed open-site premise at offset 130; and
3. first occupied-record contact at offset 129.

Only the second is a candidate local interaction site, because a new record
could in principle form between two records at distance two. Here no existing
row acts, so the observed outcome is transparent closure, not interaction.

This is not a no-go. It does not say that a different placement, orientation,
generated approach history, or added source-grade interaction family cannot
act. It also does not establish quantum execution, scattering, measurement,
probability, time, or an axiom consequence.
