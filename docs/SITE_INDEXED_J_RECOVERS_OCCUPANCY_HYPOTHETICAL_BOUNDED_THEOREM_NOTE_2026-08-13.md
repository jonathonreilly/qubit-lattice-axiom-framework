---
claim_id: site_indexed_j_recovers_occupancy_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the two-site window W={x,y} with menu {A,B}, scalar Record I fails to split the unit-lock histories o10 and o01, while the displayed C1 site-indexed readout J does split them and retracts occupancy; the current Record sentences do not name J, C1 is not adopted, and the reconstructed I-table (0,1,1,2) still disagrees with the extra product table (0,0,0,1)."
upstream_dependencies:
  - minimal_axioms
runner: scripts/site_indexed_j_recovers_occupancy_hypothetical_2026_08_13.py
---

# Site-Indexed J Recovers Occupancy (Hypothetical, Not Adopted)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** two-site window, unit locks, displayed C1 readout versus current
scalar `I`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/site_indexed_j_recovers_occupancy_hypothetical_2026_08_13.py`](../scripts/site_indexed_j_recovers_occupancy_hypothetical_2026_08_13.py)

Scientific parent on `origin/main`: the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

This is a hypothetical discriminating test. It is not an axiom edit.

## Result Up Front

Fix the two-site window `W={x,y}` and the finite menu `M={A,B}`. An occupancy
is a map `o:W→{0,1}`. Current Record readout on unit locks is the scalar

`I(o)=|o^{-1}(1)|`.

The displayed C1 counterfactual readout (not adopted) is the site-indexed map

`J:W → {0}∪M`,

with `J(z)=0` if `o(z)=0` and `J(z)` equal to the locked menu entry if
`o(z)=1`. Write `o_J(z)=0` if `J(z)=0` and `o_J(z)=1` otherwise.

On the two unit-lock histories that lock `A` at exactly one site, scalar `I`
and any site-blind one-site law `μ` are the same, so `(μ,I)` does not split
them. The displayed `J` does. Occupancy is a definitional retract of `J`
under C1 and remains extra on the current axiom sentences. The reconstructed
`2×2` `I`-table is still `(0,1,1,2)` and the declared extra product table is
still `(0,0,0,1)`. C1 dissolves the extra formation map `o`. It does not by
itself dissolve a pairing through scalar `I`.

The note displays `J`. It does not adopt C1. It does not force `r=1/2`. It
does not adopt `L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On W={x,y}, I(o10)=I(o01)=1 while J(o10)=(A,0) differs from J(o01)=(0,A), and o_J equals o on every {0,1}-occupancy. Current Record sentences do not name J. Adoption of C1, r=1/2, L_phys, and a pairing through I remain open."
trace_class: negative_route_pruning
target_claim_id: site_indexed_j_recovers_occupancy
target_blocker_text: "replace scalar Record I by a site-indexed readout J that retracts occupancy"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the displayed two-site unit-lock window and the displayed C1 map J; C1 is not adopted"
hypothetical_axiom_status: "C1 counterfactual: Record readout is site-indexed J, not scalar I; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let

`W={x,y}`, `M={A,B}`.

An **occupancy** is a function `o:W→{0,1}`. The four occupancies are written

`o00=(0,0)`, `o10=(1,0)`, `o01=(0,1)`, `o11=(1,1)`.

A **history** on this window is an occupancy together with, at each occupied
site, exactly one locked menu entry. The two discriminating unit-lock
histories lock `A`:

- `o10`: only `x` formed, lock `A`;
- `o01`: only `y` formed, lock `A`.

The empty history `o00` locks nothing. The double-lock history `o11` used
below locks `A` at both sites. Record allows all four occupancies as finite
collections of pairwise-disjoint unit locks.

Current scalar readout on unit locks is

`I(o)=|o^{-1}(1)|`,

so `I(o00)=0`, `I(o10)=1`, `I(o01)=1`, `I(o11)=2`. This is additivity plus
`I(empty)=0`: one unit lock has `I=1`, and two disjoint unit locks have
`I=1+1=2`.

A **site-blind** one-site law `μ` is the same probability law on `M` at both
sites. It does not carry a site index.

The displayed C1 readout is

`J(z)=0` if `o(z)=0`, else the locked menu entry at `z`.

The occupancy retract is

`o_J(z)=0` if `J(z)=0`, else `1`.

Write `I_J=|{z: J(z)≠0}|`.

The reconstructed **I-table** on the four occupancies, in the order
`(o00,o10,o01,o11)`, is

`(I(o00),I(o10),I(o01),I(o11))=(0,1,1,2)`.

The declared extra **product table** on the same order treats the two sites as
unit atoms and multiplies their occupancies:

`(0·0, 1·0, 0·1, 1·1)=(0,0,0,1)`.

That product table is extra. It is not a Record readout.

## Exact Target And Obligation Graph

**Exact target.** Decide whether current scalar `I`, with a site-blind law,
already splits the two unit-lock histories, and whether the displayed C1 map
`J` recovers occupancy without being named by the current Record sentences.

| Obligation | Role | Disposition |
|---|---|---|
| `I(o10)=I(o01)=1`; site-blind `μ` is the same; `(μ,I)` does not split | Theorem 1 | proved |
| `J(o10)=(A,0)≠(0,A)=J(o01)` | Theorem 1 | proved |
| `o_J=o` on every `{0,1}`-occupancy of `W` | Theorem 2 | proved |
| `I_J=I`; I-table `(0,1,1,2)`; product table `(0,0,0,1)` | Theorem 3 | proved |
| current Record sentences do not name `J`; do not adopt C1 | Theorem 4 | scoped residual |

## Theorem 1 — Scalar `I` Does Not Split `o10` From `o01`; Displayed `J` Does

Both discriminating histories are one unit lock, so

`I(o10)=1=I(o01)`.

Any site-blind law `μ` is the same object at `x` and at `y`. The pair
`(μ,I)` is therefore the same on `o10` and on `o01`. The predicate
“`I` splits `o10` from `o01`” fails.

The locked content is `A` in both histories. Content-only readout of the
locked possibility is therefore also the same. The site that carries the
lock is not a value of scalar `I`.

The displayed C1 map is

`J(o10)=(A,0)`, `J(o01)=(0,A)`.

These tuples are unequal. The predicate “`J(o10)=J(o01)`” fails. Identity
gates for this theorem call `I_of` and `J_of`.

## Theorem 2 — Occupancy Is A Retract Of `J` Under C1

Let `J` be the displayed C1 readout of any `{0,1}`-occupancy of `W`, with
any locks in `M` at occupied sites. Then `o_J(z)=0` exactly when `J(z)=0`,
and `J(z)=0` exactly when `o(z)=0`. So `o_J=o`.

Occupancy is therefore a definitional retract of `J`, not an extra map,
**under the C1 counterfactual**. On the current axiom sentences the
occupancy map remains extra: those sentences name a scalar additive `I`,
not a site-indexed `J` from which `o` would be recovered.

Identity gates for the retract call `o_from_J`.

## Theorem 3 — `I_J` Equals Current `I`; The Product Table Stays Extra

By definition `I_J=|{z: J(z)≠0}|`. Theorem 2 gives `J(z)≠0` exactly when
`o(z)=1`, so `I_J=I` on every occupancy of `W`. The `2×2` I-table is
therefore still

`(0,1,1,2)`.

The declared extra product table on the same four cells is still

`(0,0,0,1)`.

Those two tables disagree at three of the four cells, including the
double-lock cell `2≠1`. A pairing through scalar `I` is still extra. C1
dissolves the extra formation map `o`, because `o=o_J` once `J` is the
readout. C1 does not by itself dissolve that pairing: replacing `I` by
`I_J` leaves the product table untouched.

This note does not import a force law, a Green kernel, or a coupling. The
product table is reconstructed here as multiplication of the two unit
occupancies.

## Theorem 4 — Quote Current Record; Display `J`; Do Not Adopt C1

The current Record sentences are:

> Records form.
>
> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.
>
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

Those sentences name formation, a single lock per site, content-only
readout, and additive scalar `I` with `I(empty)=0`. They do not name a
site-indexed map `J:W→{0}∪M`.

The Admissibility reading note already records that the one-site
distribution is conditional on formation and does not supply the formation
site, probability, or rate. Occupancy as a map `W→{0,1}` is that unsupplied
site pattern.

This note displays `J`. It does not adopt C1. It does not rewrite Record. It
does not force `r=1/2`. It does not adopt `L_phys`.

## Promotion Value Gate

### V1 — current wording

The load-bearing Record sentences are quoted in Theorem 4 from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). The named
readout is scalar additive `I`. The displayed `J` is not in that text.

### V2 — origin/main search

A search of `origin/main` `docs/` for a site-indexed Record readout that
retracts occupancy on a two-site window did not find a parent theorem to
cite. Hits on the phrase “site-indexed” belong to other lanes. This note
reconstructs the occupancy-bit arithmetic and the two `2×2` tables locally.
No unmerged pull request is cited.

### V3 — no literature substitution

That occupancy is the indicator of a nonzero site-indexed label is a
definitional retract, not a borrowed external theorem. The I-table is
additivity plus `I(empty)=0`. The product table is declared extra
multiplication of two unit occupancies.

### V4 — exact witnesses

`I(o10)=I(o01)=1`, `J(o10)=(A,0)≠(0,A)=J(o01)`, `o_J=o` on all four
occupancies, `I_J=I`, I-table `(0,1,1,2)`, product table `(0,0,0,1)`.

### V5 — not an axiom corollary

A corollary of the current Record sentences would already name `J` or split
`o10` from `o01` by scalar `I`. Theorem 1 and Theorem 4 show neither.

## No-Go Discipline Gate

The negative claims shipped here are narrow: scalar `I` does not split
`o10` from `o01` on this window; the current Record sentences do not name
`J`; a pairing through scalar `I` remains extra after C1 is displayed. The
gate does not certify that no later derivation of a site-indexed readout
exists, and it does not certify that gravity is impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Scalar `I` as splitter | use `I(o)` to separate `o10` from `o01` | both have `I=1` | **ATTEMPTED** |
| Site-blind law plus `I` | use `(μ,I)` as a joint readout | `μ` is the same and `I` is the same | **ATTEMPTED** |
| Content-only lock label | use the locked menu entry `A` as a site address | both histories lock `A` | **ATTEMPTED** |
| Formation sentence as occupancy map | read “Records form” as already supplying `o:W→{0,1}` | the sentence is occurrence, not a site-indexed table; named readout remains scalar `I` | **ATTEMPTED** |
| Product table as Record readout | identify the I-table with occupancy multiplication | `(0,1,1,2)≠(0,0,0,1)` at three cells | **ATTEMPTED** |
| Adopt C1 to dissolve the pairing | replace `I` by `I_J` and declare `π` selected | `I_J=I`, so the product table is unchanged and still extra | **ATTEMPTED** |
| Force `r=1/2` or `L_phys` from `J` | treat menu labels in `J` as a Bloch radius or a physical length | `J` takes values in `{0}∪M`; no radius or length is named | **ATTEMPTED** |

The broad statements “occupancy cannot be derived later” and “no pairing can
exist later” are not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| occupancy extra on current sentences / pairing through `I` extra | no: C1 retracts `o` and leaves the product table | no: a declared product on scalar `I` does not site-index the readout | independent |
| occupancy extra / C1 not adopted | no: displaying `J` does not write it into the axiom memo | no: refusing adoption does not by itself prove `o` extra | distinct: one is a current-sentence fact, one is a governance refusal |
| pairing extra / C1 not adopted | no | no | independent |

The collapsed residual shipped with the theorems is: on the current
sentences, `o` is extra and a pairing through `I` is extra. C1 is a
displayed counterfactual, not a second independent physics wall.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}` | explicit finite window; not a lattice-wide claim |
| menu `{A,B}` | explicit finite lock alphabet |
| unit locks | explicit; `I` reconstructed from additivity and `I(empty)=0` |
| site-blind `μ` | explicit same-law-at-both-sites hypothesis used only in Theorem 1 |
| `J` | displayed C1 counterfactual; not attributed to the current axioms |
| product table | declared extra multiplication; not attributed to Record |
| “registered” / “canonical” | unused as load-bearing words |
| `r=1/2`, `L_phys` | named only to refuse them |

No hidden continuity, measure, dynamics, or force law is used.

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) Record block | formation sentence; content-only readout; additive `I` with `I(empty)=0`; no named `J` | exact current wording only |
| same memo, Admissibility reading note (2) | distribution does not supply formation site, probability, or rate | used only to locate occupancy as that unsupplied site pattern |

No other note is a scientific parent. Occupancy-formation no-gos in other
lanes attack species-grain dictionaries, not this two-site retract.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | each site of `W` is assigned `0` or a menu lock in `J` | no claim about every possible menu alphabet |
| per site | two named sites; unit locks | no composite-carrier theorem |
| per mode | not a spectral claim | no mode exhaustion |
| per block | only the `I` versus `J` readout block on this window | no Born, dynamics, or gravity closure |
| lattice-wide | not executed | no lattice-wide frequency or formation-rate law |

### N6 — live partial-closure paths

C1 is a displayed counterfactual, not a required axiom edit. A later
derivation that extracts site labels from the Lattice structure of a record
collection, while keeping content-only readout, would be an extra theorem,
not a silent rewrite of scalar `I`. A later supplier of the product table
would still be extra after that derivation.

The approved scale-reference, kinetic-isotropy, and realized-state
primitives were checked against
[`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json).
None supplies a site-indexed Record readout or a two-argument pairing, and
none is counted as a wall.

No unmerged pull request is cited as a closure path.

### N7 — hostile steelman

Lattice already distinguishes `x` from `y`. Record already says that a
readout is determined by record content alone, and that a site carries at
most one record. A hostile reading is that the pair (site, locked
possibility) is already the physical record, so `J` is not counterfactual
and occupancy is not extra.

That reading names a different object than the *named* scalar `I`. Theorem
1 is about `I`, not about an unspoken site-labeled ledger. Theorem 4 is
about the sentences as written: they do not write `J`. If a later theorem
constructs `J` from site labels plus content, that theorem is welcome and
is not this note. The steelman does not restore a split of `o10` from `o01`
by scalar `I`, and it does not write `J` into the current memo.

### N8 — cross-cycle echo

Formation-append notes record that “Records form” supplies occurrence and
not a formation-site rule. That residual is similar in shape and is not
retired into a site-indexed readout. This note does not re-open those
species-grain no-gos and does not depend on them.

The product-table residual is the same shape as a pairing through scalar
`I`: additivity fills `(0,1,1,2)` and does not fill `(0,0,0,1)`. That
disagreement is recomputed here.

## Why The Broad Claim Is Rejected

FAIL / DO NOT SHIP: “occupancy is underivable,” “C1 must be adopted,”
“Newton is selected,” “no later compiler exists.”

The shipped claim is only the displayed two-site arithmetic and the
quotation of the current Record sentences.
