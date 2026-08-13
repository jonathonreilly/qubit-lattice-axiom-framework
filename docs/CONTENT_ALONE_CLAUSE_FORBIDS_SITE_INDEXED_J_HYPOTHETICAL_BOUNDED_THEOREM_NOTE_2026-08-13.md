---
claim_id: content_alone_clause_forbids_site_indexed_j_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with a two-possibility menu, the site-indexed occupancy field J takes distinct values on two histories that lock the same possibility. Under the strict reading that a readout is a function of locked possibility content (and of the site-blind bag of locked possibilities), J is not an allowed readout. Scalar I and the site-blind bag are allowed. The current Record wording does not choose the strict reading versus a site-inclusive reading. The content-alone clause is a drop/narrow candidate if a site-indexed field is later adopted as a readout. Neither reading, C1-strong, r=1/2, L_phys, nor a pairing on J is adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/content_alone_clause_forbids_site_indexed_j_hypothetical_2026_08_13.py
---

# Content-Alone Clause Forbids Site-Indexed Occupancy Under a Strict Reading

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-history window algebra for the Record clause
"a readout value is determined by record content alone."
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/content_alone_clause_forbids_site_indexed_j_hypothetical_2026_08_13.py`](../scripts/content_alone_clause_forbids_site_indexed_j_hypothetical_2026_08_13.py)

This is a C1 follow-on (friction audit 2026-08-13). It is not a type-split of
readout classes. It is not a pairing construction on the site-indexed field.
No axiom sentence is edited.

## Result Up Front

The current Record axiom says:

> Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

On the two-site window `W={x,y}` with menu `M={A,B}`, reconstruct the
site-indexed occupancy field `J` from the locked possibility at each site,
using `0` for an unlocked site:

- `h10A` locks only `x` to `A`. Record content is `A`. Then `J(h10A)=(A,0)`
  and `I(h10A)=1`.
- `h01A` locks only `y` to `A`. Record content is `A`. Then `J(h01A)=(0,A)`
  and `I(h01A)=1`.

Two readings of "record content alone" are live on the present wording:

- **R_strict:** a readout is a function of the locked possibility, and of the
  multiset of locked possibilities on a window. Site is not content.
- **R_lax:** "content" includes which site holds the record.

Under R_strict the two histories are indistinguishable, so every allowed
readout takes the same value on both. The site-indexed field `J` does not.
Adopting the candidate that treats `J` as a readout (C1-strong) therefore
contradicts R_strict. It is not a conservative retype of the quoted clause.
Under R_lax the same `J` is allowed. The current wording does not pick either
reading. This note adopts neither reading, does not force `r=1/2`, does not
adopt `L_phys`, and does not put a pairing on `J`.

If C1-strong is later adopted, owner wording must either drop or narrow
"content alone" so a site-indexed field can be a readout, or keep R_strict and
reject C1-strong. Weak occupancy `o` also violates R_strict. The clause is a
drop/narrow candidate, not a fifth extra.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two-history J arithmetic is exact. Whether Record content includes site is a wording choice, not a derived axiom fact. C1-strong, R_strict, R_lax, r=1/2, L_phys, and any pairing on J remain unadopted."
trace_class: negative_route_pruning
target_claim_id: record_content_alone_site_index
target_blocker_text: "decide whether site-indexed occupancy is a Record readout or whether the content-alone clause must be dropped or narrowed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed window and the two readings; no axiom adoption"
hypothetical_axiom_status: "C1 follow-on: strict content-alone forbids J; clause is a drop/narrow candidate; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window be the ordered pair of Lattice sites

`W = (x, y)`.

Let the local menu be the two-possibility set

`M = {A, B}`.

A window history is a function `h: W -> M union {0}`, where the token `0`
means the site carries no record. The locked set of `h` is

`{ s in W : h(s) != 0 }`.

The two one-record histories used below are

`h10A(x)=A`, `h10A(y)=0`

and

`h01A(x)=0`, `h01A(y)=A`.

Each history locks exactly one available local possibility, namely `A`. The
Record sentence that a present record locks exactly one admissible local
possibility is therefore satisfied, and no second record sits on the same
site.

Reconstruct the three maps from the history, without a pairing and without a
half-integer fill:

- Scalar readout `I(h)` is the occupancy count of locked sites (unit-count
  convention: each occupied site contributes `1`). Record additivity and
  `I(empty)=0` do not force that unit. A common singleton strength `a≠0`
  leaves Theorems 1–2 unchanged, because both histories still share the
  same `I`.
- Site-indexed occupancy `J(h)` is the ordered pair `(h(x), h(y))`.
- The site-blind bag `bag(h)` is the multiset of locked possibilities.

These reconstructions give the exact integers and labels

| History | locks | content | `I` | `J` | `bag` | weak occupancy `o` |
|---|---|---|---:|---|---|---|
| `h10A` | only `x`, lock `A` | `A` | `1` | `(A,0)` | `{A}` | `(1,0)` |
| `h01A` | only `y`, lock `A` | `A` | `1` | `(0,A)` | `{A}` | `(0,1)` |

The runner's identity gates call `I_of(h10A)`, `I_of(h01A)`, `J_of(h10A)`,
`J_of(h01A)`, and `bag_of(h10A)` on these objects.

## Theorem 1 — R_strict forces equal readout on `h10A` and `h01A`

Assume R_strict: a readout `f` is a function of the locked possibility and of
the multiset of locked possibilities on the window. Site is not content.

Both histories lock only `A`, so

`bag(h10A) = {A} = bag(h01A)`.

Therefore any R_strict readout satisfies

`f(h10A) = f(h01A)`.

Scalar `I` obeys R_strict:

`I(h10A) = 1 = I(h01A)`.

The predicate "`I(h10A)` differs from `I(h01A)`" therefore fails.

The site-blind bag also obeys R_strict, because it is already the multiset of
locked possibilities.

## Theorem 2 — `J` does not obey R_strict

The reconstructed field is

`J(h10A) = (A,0) != (0,A) = J(h01A)`.

The two values are distinct ordered pairs. The predicate "`J` obeys R_strict"
therefore fails: R_strict would require `J(h10A)=J(h01A)`.

C1-strong is the candidate that treats this site-indexed field as an allowed
readout. Adopting C1-strong therefore contradicts R_strict. That adoption is
not a conservative retype of the quoted content-alone clause. It is a change
in what "content" is allowed to include, or a change in which maps count as
readouts.

No pairing is placed on `J`. A pairing would replace the ordered pair by a
scalar and would no longer be the site-indexed field reconstructed above.

## Theorem 3 — R_lax permits the same `J`

Assume R_lax: "content" includes which site holds the record. Then `h10A` and
`h01A` are distinct contents, because one record sits at `x` and the other
sits at `y`. A map that returns `(A,0)` on the first history and `(0,A)` on
the second is then a function of content.

The current Record wording, quoted above, does not pick R_strict versus
R_lax. Both readings are displayed. Neither is adopted.

## Theorem 4 — drop/narrow candidate, not a fifth extra

If C1-strong is adopted, owner wording must do one of the following:

1. Drop or narrow "content alone" so that a site-indexed field is a readout.
2. Keep R_strict and reject C1-strong.

Option 2 also rejects weak occupancy `o`, because

`o(h10A)=(1,0) != (0,1)=o(h01A)`.

The same two histories that share bag `{A}` receive distinct site-indexed
occupancy vectors. Weak occupancy is therefore not a R_strict workaround.

This is a drop/narrow candidate for the quoted clause. It is not a fifth
axiom and not an extra primitive. No Record rewrite is adopted here.

## Theorem 5 — nothing is adopted

This note does not adopt R_strict. It does not adopt R_lax. It does not
adopt C1-strong. It does not force `r=1/2`. It does not adopt `L_phys`. It
does not put a pairing on `J`. The displayed algebra is a bounded reading
test of the present clause, not a proposal to change the axiom memo.

## No-Go Discipline Gate

The negative claim is only this: under R_strict, the reconstructed field `J`
is not an allowed readout, and weak occupancy `o` is not an allowed readout
either. The gate does not certify that C1-strong is impossible on the current
wording, and it does not certify that Record must be rewritten.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Project `J` to the bag | forget the site index and keep only the locked-possibility multiset | the result equals `bag`, which obeys R_strict, but it is not `J` | **ATTEMPTED** |
| Identify the two sites | force `x=y` so the two histories coincide | Lattice distinguishes sites by the supplied lattice structure; the window has two sites | **ATTEMPTED** |
| Pair `J` to a scalar | replace the ordered pair by a pairing or trace | the spec of this follow-on forbids a pairing on `J`; a scalar is not the site-indexed field | **ATTEMPTED** |
| Collapse the window | keep only one site so `h01A` is not in the window | the conflict is a two-site statement; removing a site removes the comparison | **ATTEMPTED** |
| Relabel the empty token | choose a token that makes `(A,0)=(0,A)` | exact ordered pairs with a fixed empty token remain unequal | **ATTEMPTED** |
| Switch to R_lax | declare site to be part of content | Theorem 3: `J` is then allowed; this changes the reading, it does not make `J` a function of the bag | **ATTEMPTED** |
| Replace `J` by weak occupancy | use `o` in `{0,1}^W` | Theorem 4: `o(h10A)!=o(h01A)`, so `o` also fails R_strict | **ATTEMPTED** |

The first five routes try to keep R_strict and still treat a site-indexed
object as a readout. They fail or change the object. The last two change the
reading or the field and do not rescue C1-strong under R_strict. The broad
statement "the current axioms forbid `J`" is not shipped.

### N2 — wall independence and collapse

There is one wording decision, not a list of independent walls: either
"content" includes site, or it does not, or the clause is dropped or
narrowed. No second independent wall is claimed.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| R_strict versus drop/narrow | yes: keeping R_strict and adopting C1-strong is inconsistent, so adoption forces drop/narrow or rejection | no: dropping the clause does not by itself select R_strict | collapsed to one owner wording choice |
| `J` versus weak occupancy `o` | no: they are different maps | no | both fail R_strict separately; they are not two walls |

Collapsed wall set: the content-alone clause versus site-indexed readout.
Count: one.

### N3 — hidden-condition scan

| Phrase / construction | Classification |
|---|---|
| "reconstruct C1 `J` arithmetic" | explicit: `J` is the ordered pair of locked labels, empty token `0` |
| "content" | explicit two readings, quoted clause, neither adopted |
| "by construction" unused | no hidden fill, no `r=1/2`, no `L_phys` |
| approved primitives | scale reference, kinetic isotropy, and realized state supply none of `I`, `J`, or the reading |

No hidden wall is promoted.

### N4 — source residual matching

No prior no-go is cited as a witness that this residual is already closed.
The residual here is the reading of "record content alone" on a two-site
window. That is not the AC occupancy statistical-grain obligation, not a
Born-menu kernel residual, and not a pairing-on-`J` residual.

| Cited witness | Residual it attacks | Residual here | Match? |
|---|---|---|---|
| none | — | R_strict versus site-indexed `J` | no prior witness claimed |

### N5 — resolution and rhetoric audit

The phrase under test is: "under R_strict, `J` is not an allowed readout."

| Resolution | Tested? | Holds? |
|---|---|---|
| per-element (one locked possibility `A`) | yes | yes: both histories lock `A` |
| per-site (the two window sites) | yes | yes: `J` differs by site |
| per-mode | not a spectral object | not claimed |
| per-block (the two-site window) | yes | yes: the inequality is a window statement |
| lattice-wide | not executed | not claimed |

The phrase "the axioms forbid site-indexed occupancy" is over-broad and is
not shipped. The current wording does not pick R_strict.

### N6 — live partial-closure paths

| Partial-closure / governance surface | Current status used here | What it could close |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Record clause | quoted; no edit | the baseline sentence being read |
| `docs/audit/data/axiom_premise_nodes.json` | three approved primitives; none is a site-indexed readout | no part of this reading test |
| drop or narrow "content alone" | owner wording option in Theorem 4 | C1-strong as a readout after a clause change |
| keep R_strict and reject C1-strong | owner wording option in Theorem 4 | the clause as written under R_strict |

No unmerged PR is cited. A convention reframe that drops or narrows the
clause is exactly option (i). This note does not call that "a new axiom."
It also does not perform the reframe.

### N7 — hostile steelman

> Lattice already distinguishes sites. A record is a lock at a site of one
> possibility. Calling the pair (site, locked possibility) the content of
> the record is the ordinary reading of "record content," so R_lax is not an
> extra. Under that reading C1-strong is a conservative retype: `J` merely
> writes down, site by site, the locks the Record axiom already names. The
> two-history inequality then shows that the field is informative, not that
> it is forbidden. Forcing R_strict would erase a distinction the Lattice
> axiom supplies.

The steelman is accepted as a reason not to adopt R_strict and not to claim
that the current wording already forbids C1-strong. It does not make `J` a
function of the site-blind bag. Theorem 2 stands under R_strict; Theorem 3
stands under R_lax; Theorem 5 adopts neither.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| Record content-alone applied to menu/context labels | those notes keep a content-only bridge open and do not rewrite Record | the same clause is quoted; site index is a different object than a menu label |
| readout-license splits that separate construction content from record-determined content | those splits do not adopt a Record rewrite | this follow-on likewise adopts no rewrite |
| type-separations of measure versus menu kernel | those notes display a hypothetical interface and refuse axiom adoption | this follow-on displays two readings and refuses adoption |

No similar prior wall was retired by a mechanism that would make `J` equal
on `h10A` and `h01A` while remaining site-indexed.

**Gate disposition:** PASS for (i) `I` and `bag` obey R_strict, (ii) `J` and
`o` do not obey R_strict, and (iii) the clause is a drop/narrow candidate if
C1-strong is adopted. FAIL / DO NOT SHIP for "an axiom update is necessary,"
"the current wording already selects R_strict," "C1-strong is adopted,"
"`r=1/2` or `L_phys` is forced," or "a pairing on `J` repairs the clause."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | exact semantic baseline | supplied; no edit |
| two-site window and two-possibility menu | Theorem 1--4 arena | constructed here |
| reconstructed `I`, `J`, `bag`, `o` | exact maps | constructed here |
| R_strict and R_lax | displayed readings | not adopted |
| C1-strong | candidate that treats `J` as a readout | not adopted |
| `r=1/2`, `L_phys`, pairing on `J` | extras | not used, not adopted |
| approved primitives | checked; none supplies the reading | not walls |
| unmerged PRs | none cited | — |

The exact advance is a clause-reading theorem on one window. It does not
move any TOE percentage. It makes the next owner wording decision testable:
keep R_strict and reject site-indexed readout, or drop/narrow "content
alone," or explicitly adopt R_lax. This note does none of those.

## Review Record

Independent audit remains required before any effective status may change.
No `review-loop` was invoked in producing or self-reviewing this artifact.
