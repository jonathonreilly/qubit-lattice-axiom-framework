---
claim_id: m2_record_seed_grown_front_chiral_support_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether the M_2 Record neighbor alphabet is July-3 k=3, and whether the unique k=3 chiral pair has empty support on seed-grown ℓ¹ fronts of radius 0..4, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/m2_record_seed_grown_front_chiral_support_2026_08_15.py
---

# M_2 Record Seed-Grown Front Chiral Support Is Empty

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** lock-content alphabet of one `M_2` record plus unread/empty, the
July-3 unique `k = 3` chiral pair, and already-displayed seed-grown `ℓ¹`
front geometry on radii `t = 0..4`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/m2_record_seed_grown_front_chiral_support_2026_08_15.py`](../scripts/m2_record_seed_grown_front_chiral_support_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
July-3 theorems 2–3 are re-earned here from the same named condition-alphabet
models; they are not a status source.

## Result Up Front

One `M_2(C)` record locks one of two spectral contents. The nearest-neighbor
condition alphabet is therefore `{empty, +, −}`, which is July-3 `k = 3`,
not `k = 4`. At `k = 3` the unique chiral pair is the handed fully-mixed
pair: every axis bi-colored, every value used twice. That pair is a coloring
of all six cubic neighbor slots and therefore requires a 6-occupied-neighbor
member.

The already-displayed seed-grown occupancy is the `ℓ¹` ball
`B_t = {x ∈ Z^3 : |x|_1 ≤ t}`. The ordinary-growth front is the sphere
`S_{t+1} = {x : |x|_1 = t+1}`. On that front, the number of occupied
nearest neighbors equals the number of nonzero coordinates and is at most
`3`. For `t = 0..4` the count `N_with_6` of front sites with six occupied
neighbors is identically zero. The unique `k = 3` pair therefore has empty
support on those fronts.

Displayed: no `M_2`-Record seed-grown 6-NN member turns on July-3 chirality
during ordinary growth. That is a mismatch with observed weak `P`-violation
on this growth. Displayed, not adopted. Qubit stays `M_2(C)`. No `V−A`
sentence is written into the axioms. L1 is not attached.

`claim_scope`: Whether the `M_2` Record neighbor alphabet is July-3 `k=3`,
and whether the unique `k=3` chiral pair has empty support on seed-grown
`ℓ¹` fronts of radius `0..4`, is reported. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite alphabet count, exact Burnside/orbit re-earn of the unique k=3 pair, and exact occupied-neighbor counts on already-displayed ℓ¹ fronts t=0..4. The weak-P mismatch is displayed, not adopted."
trace_class: residual_display
target_claim_id: m2_record_seed_grown_front_chiral_support
target_blocker_text: "can M_2 Record content chirally fire on seed-grown growth"
source_of_blocker_text: handoff
reachability_to_target: reports
artifact_role: theorem
next_trace_action: "independent audit of the alphabet and front-support counts; do not treat the displayed mismatch as an axiom edit"
conditional_surface_status: "exact for k=3 lock-content-plus-empty and for S_{t+1} at t=0..4; larger radii and non-seed-grown occupancy remain unclaimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: "weak P-violation is displayed as a mismatch only"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** Prove that the `M_2` Record neighbor alphabet is July-3
`k = 3`; that the unique `k = 3` chiral pair is the handed fully-mixed pair
and requires six occupied neighbors; that `N_with_6 = 0` on `S_{t+1}` for
`t = 0..4`; and that the pair's support is therefore empty on those fronts.
Display the mismatch with observed weak `P`-violation. Do not adopt a repair.

| Obligation | Disposition |
|---|---|
| lock-content of one `M_2` record is two letters | Theorem 1; Qubit plus Record |
| unread/empty makes `k = 3` | Theorem 1 |
| unique chiral pair at `k = 3` is handed fully-mixed | Theorem 1; July-3 Theorem 3 re-earned |
| that pair requires six occupied neighbors | Theorem 1 |
| max occupied NN on `S_{t+1}` equals the number of nonzero coordinates | Theorem 2 |
| `N_with_6 = 0` for `t = 0..4` | Theorem 2 |
| empty support of the pair on those fronts | Theorem 2 |
| displayed mismatch; no axiom edit | Theorem 3 |

No occupancy is grown on a new patch. Only the already-displayed seed-grown
`ℓ¹` balls and their next spheres are scored.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  `Z^3` with nearest-neighbor adjacency, the one-site algebra `M_2(C)`,
  the nearest-neighbor condition sentence, and the lock-one Record sentence.
- [`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md)
  supplies the named `k`-letter models whose Theorems 2–3 are re-earned:
  openness (`k = 2`) is automatically achiral; at `k = 3` there is exactly
  one chiral pair, the handed fully-mixed pair.
- Occupied set `B_t` and front `S_{t+1}` are the already-displayed seed-grown
  `ℓ¹` geometry. They are not a newly grown patch.
- Observed weak `P`-violation is an external comparison only. It is not a
  framework premise and is not adopted.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

## Theorem 1 — `M_2` Record plus empty is July-3 `k = 3`, and the unique pair needs six occupied neighbors

Qubit presents the one-site possibility domain as `M_2(C)`. Record locks
exactly one admissible local possibility and determines a readout by record
content alone. The spectral content of one such lock is therefore one of two
letters, written `+` and `−`. A neighbor with no record is unread. The
nearest-neighbor condition alphabet is `{empty, +, −}`: two lock-contents
plus unread/empty, hence `k = 3`.

This is not a four-letter alphabet. A third lock-content is not supplied by
`M_2(C)` and is not written into Qubit.

July-3 Theorem 2, re-earned by Burnside and direct orbit enumeration on the
six cubic directions: every `k = 2` coloring is proper-equivalent to its
spatial-inversion image, so openness-only patterns are automatically achiral.

July-3 Theorem 3, re-earned the same way: at `k = 3` the proper/full orbit
counts differ by one. There is exactly one chiral pair. A representative
satisfies: every axis is bi-colored, and the three values each occur twice.
That pair is a coloring of all six neighbor directions. A seed-grown
6-NN member is a site whose six cubic neighbors all lie in the occupied set.
The pair's occupancy support is the set of 6-NN members. It therefore
requires six occupied neighbors.

(The same pair, read with `empty` as a letter, uses `empty` twice and so
would also require exactly four content-occupied neighbors. Front geometry
below fails that count as well. The load-bearing occupancy statement here is
the six-neighbor member count, matching the pair's six-slot coloring.)

## Theorem 2 — `N_with_6 = 0` on `S_{t+1}` for `t = 0..4`; the pair's front support is empty

Let `|x|_1 = |x_1| + |x_2| + |x_3|`. The already-displayed seed-grown
occupied set at depth `t` is `B_t = {x ∈ Z^3 : |x|_1 ≤ t}`. The ordinary
growth front is `S_{t+1}`. No further occupancy is added.

Fix `x ∈ S_{t+1}` and a cubic neighbor `x + s e_i` with `s ∈ {±1}`.

- If `x_i ≠ 0` and `s = −sign(x_i)`, then `|x + s e_i|_1 = |x|_1 − 1 = t`,
  so the neighbor lies in `B_t`.
- If `x_i ≠ 0` and `s = +sign(x_i)`, then `|x + s e_i|_1 = |x|_1 + 1 = t+2`,
  so the neighbor is unoccupied.
- If `x_i = 0`, then both signs raise the `ℓ¹` radius to `t+2`, so both
  neighbors are unoccupied.

Hence the occupied-neighbor count of `x` equals the number of nonzero
coordinates of `x`, which is in `{1, 2, 3}` and never `6`.

The companion runner enumerates every site of `S_{t+1}` for `t = 0,1,2,3,4`
and checks this identity sitewise. In particular `N_with_6 = 0` on each of
those five fronts. The unique `k = 3` chiral pair therefore has empty
support on seed-grown `ℓ¹` fronts of radius `0..4`.

This is not leftover character of the six-neighbor need alone (that is
alphabet classification) and not leftover character of the front bound
alone (that is geometry). It is the conjunction: the only `k = 3` chiral
pair requires a 6-NN member, and seed-grown fronts of these radii have none.

## Theorem 3 — displayed mismatch; not adopted

Ordinary seed-grown growth forms new records on `S_{t+1}`. Theorem 2 says
that during that growth the unique `M_2`-Record `k = 3` chiral pair has
empty support: no 6-NN member is present to turn the pair on.

Observed weak `P`-violation on this growth is therefore a mismatch with the
only July-3 chiral channel available at the `M_2` Record alphabet. The
mismatch is displayed. It is not adopted as a premise, as an axiom edit, or
as a license to change Qubit, to write a `V−A` sentence into the axioms, or
to attach L1.

## Mutations

1. Replace the neighbor alphabet by openness only (`k = 2`): Theorem 1's
   re-earn finds no chiral pair, so the unique-pair claim fails.
2. Replace `k = 3` by `k = 4`: the chiral-pair count is no longer one, and
   the alphabet is no longer the `M_2` Record alphabet.
3. Replace the front by an interior site of `B_t` with `t ≥ 1`: the origin
   has six occupied neighbors, so `N_with_6` is not the front count.
4. Replace occupied-neighbor count by total degree `6`: every cubic site
   has six geometric neighbors; the occupancy count is the quantity scored.
5. Adopt the mismatch as an axiom sentence: that step is refused.

## What This Does Not Claim

- No Qubit rewrite. The one-site algebra remains `M_2(C)`.
- No `V−A` axiom sentence and no L1 attachment.
- No new occupancy patch and no growth rule beyond the already-displayed
  `ℓ¹` balls.
- No claim about fronts of radius greater than `5`, about non-seed-grown
  occupancy, or about interior 6-NN sites as a physical chiral channel.
- Observed weak `P`-violation is not imported as a framework premise.
- July-3's `k = 4` oriented-frame carrier is not the `M_2` Record alphabet
  and is not adopted here.

## No-Go Discipline Gate

The negative claim is only this: the unique July-3 `k = 3` chiral pair has
empty occupancy support on the already-displayed seed-grown fronts
`S_{t+1}` for `t = 0..4`. It is not a claim that chirality is impossible
in the framework, and it is not a wall against observed weak `P`-violation.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| openness-only alphabet | Score `k = 2` chiral pairs | Theorem 1 re-earn: zero pairs | **ATTEMPTED** |
| lock-content-plus-empty | Score `k = 3` pair count and shape | Theorem 1: one fully-mixed pair on six slots | **ATTEMPTED** |
| four-letter alphabet | Treat a third lock-content as native | Refused: Qubit is `M_2(C)` | **ATTEMPTED** |
| front occupancy count | Enumerate `S_{t+1}` for `t = 0..4` | Theorem 2: occupied NN equals nonzero coordinates, `N_with_6 = 0` | **ATTEMPTED** |
| empty-as-letter count | Compare `2/2/2` empty multiplicity to the front | Front sites have at least three unread neighbors | **ATTEMPTED** |
| adopt the mismatch | Write `V−A` or change Qubit | Refused; displayed only | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one reported residual: empty front support for the only `k = 3`
pair. Alphabet classification and front geometry are independent premises
of that conjunction; neither is a second wall.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| unique `k = 3` pair / `N_with_6 = 0` | no | no | independent factors of one residual |
| six-slot coloring / four-content-occupied reading | no: slot count is not the empty-letter count | no | same pair, two readings; not two walls |

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| `M_2(C)` one-site algebra | cited registered axiom premise |
| lock-one Record sentence | cited registered axiom premise |
| `{empty, +, −}` | derived alphabet, not a new axiom |
| `B_t`, `S_{t+1}` | already-displayed seed-grown geometry |
| observed weak `P`-violation | external comparison; displayed, not adopted |
| 6-NN member | occupancy definition used by Theorem 1–2 |

### N4 — citation-to-residual matching

| Evidence path | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Qubit sentence | one-site algebra | `M_2(C)` only | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Record lock sentence | lock-content count | one of two spectral contents | yes |
| July-3 Theorems 2–3, re-earned | chiral-pair existence at `k = 3` | unique fully-mixed pair | yes |
| runner front census `t = 0..4` | 6-NN members on the front | `N_with_6 = 0` | yes |

No citation is used to close a Qubit rewrite, a `V−A` law, or an L1
attachment.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each front site at `t = 0..4` | occupied NN equals nonzero coordinates |
| per site | yes: one `M_2` record alphabet | `k = 3`, not `k = 4` |
| per mode | yes: the unique `k = 3` pair | six-slot fully-mixed pair only |
| per block | yes: each front `S_{t+1}` | `N_with_6 = 0` on that block |
| lattice wide | no | no claim about all occupancy histories |

### N6 — partial closure and primitive scan

The only registered premise used is `minimal_axioms`. No approved primitive
is added. Interior 6-NN sites of `B_t` for `t ≥ 1` are a partial-closure
mechanism: they can host six occupied neighbors, but they are not the
ordinary-growth front and are not claimed here as a physical chiral channel.

### N7 — hostile steelman

The strongest objection is that empty is already a letter, so the fully-mixed
pair needs only four occupied neighbors plus two unread neighbors, and a
sufficiently connected front might supply that. On seed-grown `ℓ¹` fronts the
occupied count is at most three, so the empty count is at least three and
the `2/2/2` pattern still fails. A second objection is that interior sites
already have six occupied neighbors. That is true and is why the residual is
restricted to the front of ordinary growth, not to the whole ball.

### N8 — cross-cycle echo

July-3 classifies alphabets. The seed-grown front bound is geometry. This
note only multiplies those two already-displayed facts. It does not reopen
other chirality or color routes.

No-Go Discipline disposition: **PASS** for the empty-front-support residual
stated at the start of this section.

## Runner Contract

The companion runner re-earns the `k = 2` and `k = 3` orbit counts, checks
the fully-mixed representative, enumerates `S_{t+1}` for `t = 0..4` without
growing a new occupancy patch, verifies `N_with_6 = 0`, and binds
`AUDIT_INPUT_PATHS` to this note and the axiom memo as static string
literals. It writes no cache and no citation manifest.
