---
claim_id: occupancy_pattern_is_smallest_complete_formation_input_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window W={x,y}, Record allows all four occupancy maps o:W→{0,1}. The shared one-site law μ with μ(A)=1/3, μ(B)=2/3 together with the unit-lock count I does not recover o, because o10 and o01 share μ and I=1. A capacity-1 token T∈{x,y,none} cannot represent the Record-allowed history o11. The occupancy map itself represents all four histories, is not a function of μ, and is not a value of I. Any complete extra object on this window must distinguish those four histories, so o is a smallest complete extra formation input. The axioms do not select o; display it; do not adopt it. Rate |o|/|W| is not a separate target."
upstream_dependencies:
  - minimal_axioms
runner: scripts/occupancy_pattern_is_smallest_complete_formation_input_2026_08_13.py
---

# Occupancy Pattern Is The Smallest Complete Extra Formation Input

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact four occupancy histories on a two-site window; unit-lock
count `I`; one shared one-site law `μ`; a capacity-1 token as an incomplete
slice.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_pattern_is_smallest_complete_formation_input_2026_08_13.py`](../scripts/occupancy_pattern_is_smallest_complete_formation_input_2026_08_13.py)

## Result Up Front

This is a missing-input type theorem. It names the smallest extra object that
represents every Record-allowed occupancy on a declared two-site window. It
does not select that object from the axioms and it does not edit an axiom
sentence.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The Admissibility reading note is quoted only as a premise. The distribution
concerns which possibility a forming record locks, conditional on formation at
that site; it does not supply the formation site, probability, or rate.

The current Record wording is quoted only as a premise:

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.

Five exact statements locate the extra object.

1. **`(μ, I)` does not recover `o`.** The four occupancy histories share one
   content law `μ`. The single-occupancy histories `o10` and `o01` also share
   the unit-lock count `I=1` and are different patterns.
2. **A capacity-1 token is a slice.** A token `T ∈ {x, y, none}` represents
   at most one formed site. It cannot represent `o11`, which Record allows
   as two disjoint formed sites.
3. **The occupancy map is complete on this window.** The map `o:W→{0,1}`
   represents all four histories. It is not a function of `μ` and not a
   value of `I`.
4. **Smallest complete extra object.** Any complete extra object must
   distinguish those four histories, so it is at least as fine as `o` up to
   relabeling. The map `o` is therefore a smallest complete extra object on
   this window.
5. **Display, do not adopt.** The quoted axiom sentences do not select `o`.
   Display `o`. Do not adopt it as an axiom. The rate `|o|/|W|` is a
   function of `I` and is not a separate target here.

This split is not the product-versus-occurrence split (a content law is not
an occupancy mark). It is not the claim that a formation site is free under
support (support constrains locked content). It is not a capacity-1 token
calculus. The token is recovered as the incomplete slice of `o` that omits
`o11`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four occupancy maps, the shared μ, the unit-lock collisions I(o10)=I(o01)=1, the token miss of o11, and the fineness of o among complete extra objects are proved by finite enumeration and exact Fraction arithmetic; axiom selection of o remains extra."
trace_class: missing_input_object
target_claim_id: occupancy_pattern_smallest_complete_formation_input
target_blocker_text: "name the smallest extra object that represents every Record-allowed occupancy on a 2-site window"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Display the occupancy map o:W->{0,1} as the smallest complete extra object on this window. Do not adopt axiom text. Rate |o|/|W| is not a separate target."
conditional_surface_status: "exact for the four occupancy histories on a 2-site window; axiom selection of o remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window be the two-site set

`W = {x, y}`

with `x ≠ y`. An **occupancy pattern** is a map

`o : W → {0, 1}`,

written in coordinates as `o = (o(x), o(y))`. The four patterns are

| Pattern | `o(x)` | `o(y)` | formed sites | `I(o)` |
|---|---|---|---|---|
| `o00` | `0` | `0` | empty | `0` |
| `o10` | `1` | `0` | `{x}` | `1` |
| `o01` | `0` | `1` | `{y}` | `1` |
| `o11` | `1` | `1` | `{x, y}` | `2` |

Here `1` means a record is present at that site and `0` means it is not.
Record uniqueness (`A site never carries more than one record`) forces the
codomain `{0, 1}`. Distinct sites carry pairwise-disjoint records.

The **unit-lock count** on the window is the additive occupancy readout

`I(o) = o(x) + o(y) = |{z ∈ W : o(z) = 1}|`.

This is the number of present records on `W`. Additivity and the empty-set
normalization are the quoted Record sentences: `I` is additive on pairwise-
disjoint records and `I(empty)=0`. Hence `I(o00)=0`, `I(o10)=I(o01)=1`, and
`I(o11)=2`. The window bound is `I(o) ≤ |W| = 2`. This `I` is a unit-lock
count. It is not a content readout that would distinguish `A` from `B`.

The executed one-site content law is the same probability `μ` on `{A, B}` at
both sites:

`μ(A) = 1/3`, `μ(B) = 2/3`, `μ(A) + μ(B) = 1`.

Full support: both masses are positive, so both labels are admissible. The
masses are a declared content law. Fairness is not derived. Occupancy is not
a coordinate of `μ`.

A **history** on this window is a pair `(μ, o)`. The four executed histories
are `(μ, o00)`, `(μ, o10)`, `(μ, o01)`, and `(μ, o11)`. Record allows all
four: the unit-lock bound is `I ≤ 2`, and emptiness of the window is
emptiness of `{x, y}`, not emptiness of the lattice. The occurrence sentence
Records form. may be realized at sites outside `W`.

A **capacity-1 token** is a value `T ∈ {x, y, none}`. Formation at a site
occurs in the token calculus if and only if `T` equals that site. The three
token values encode

| Token | encoded occupancy |
|---|---|
| `T = x` | `o10` |
| `T = y` | `o01` |
| `T = none` | `o00` |

There is no token value whose encoded occupancy is `o11`.

The **rate** on the window is `|o|/|W| = I(o)/2`. It takes the three values
`0`, `1/2`, `1`. It collides on `o10` and `o01` exactly as `I` does. It is
not a separate target here.

## Exact Target And Obligation Graph

**Exact target.** On a declared two-site window, list the four occupancy
maps allowed by Record, prove that the pair `(μ, I)` does not recover `o`,
prove that a capacity-1 token cannot represent every allowed history, prove
that `o` itself does, and record that `o` is a smallest complete extra
object on this window without adopting it.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin the formation-site/rate reading note | premise | quoted; no edit |
| pin Record occurrence, lock, uniqueness, and `I(empty)=0` | premise | quoted; no edit |
| exhibit four occupancy maps with `I ≤ 2` | objects | listing |
| show `(μ, I)` collides on `o10` and `o01` | Theorem 1 | same `μ`, same `I=1` |
| show a capacity-1 token misses `o11` | Theorem 2 | three-valued slice |
| show `o` represents all four and is not a function of `μ` or a value of `I` | Theorem 3 | four distinct maps |
| show any complete extra object is at least as fine as `o` | Theorem 4 | fineness |
| display `o`; refuse axiom adoption; refuse a separate rate target | Theorem 5 | scoped residual |
| adopt `o` as axiom text | non-claim | not attempted |
| claim that no formation rule exists | non-claim | not attempted |

## Theorem 1 — `(μ, I)` Does Not Recover `o`

**Claim.** The pair `(μ, I)` does not recover the occupancy pattern. The
histories `(μ, o10)` and `(μ, o01)` share the same content law and the same
unit-lock count `I=1`, and they are different patterns.

**Proof.** Both sites carry the same declared law `μ`. In particular
`μ` on `o10` equals `μ` on `o01`. The unit-lock counts are

`I(o10) = 1 + 0 = 1`, `I(o01) = 0 + 1 = 1`.

The occupancy maps differ: `o10(x)=1` and `o10(y)=0`, while `o01(x)=0` and
`o01(y)=1`. Therefore a function of `(μ, I)` cannot return both `o10` and
`o01`. A predicate that reads “same `μ` and same `I` imply the same
occupancy” fails on this pair.

The same `μ` is also shared with `o00` and `o11`. Those two are already
separated by `I`, which takes the values `0` and `2`. The collision that
blocks recovery is the `I=1` pair.

## Theorem 2 — A Capacity-1 Token Is A Slice, Not The Complete Extra Object

**Claim.** A capacity-1 token `T ∈ {x, y, none}` cannot represent every
Record-allowed occupancy on `W`. It cannot represent `o11`.

**Proof.** By definition the token calculus has three values. Those values
encode `o10`, `o01`, and `o00`. There is no fourth value. The pattern `o11`
has two formed sites. A token equal to `x` forms only `x`. A token equal to
`y` forms only `y`. A token equal to `none` forms neither. Mutual exclusion
of `T=x` and `T=y` is the declared capacity: there is no history in the
token calculus with both sites formed.

Record allows `o11`. The sites are distinct, so the two records are
pairwise disjoint. Additivity gives `I(o11)=I({x})+I({y})=1+1=2`, which
respects `I ≤ 2`. The lock sentence applies at each present site separately.
Uniqueness forbids two records at one site; it does not forbid one record at
each of two sites.

A predicate that reads “the token represents every Record-allowed history
on `W`” therefore fails on `o11`. The token is a capacity-1 slice of the
occupancy map, not the complete extra object.

## Theorem 3 — The Occupancy Map Represents All Four Histories

**Claim.** The map `o:W→{0,1}` represents all four Record-allowed histories
on this window. It is not a function of `μ` and not a value of `I`.

**Proof.** The four maps `o00`, `o10`, `o01`, `o11` are pairwise distinct as
functions `W→{0,1}`. Each is a legal occupancy: values lie in `{0,1}`, and
the unit-lock counts are `0`, `1`, `1`, `2`, all at most `2`. Assigning the
same `μ` to each produces the four histories.

The map `o` is not a function of `μ`: one `μ` is paired with four different
occupancies. The map `o` is not a value of `I`: the level set `I^{-1}(1)`
contains both `o10` and `o01`. Completeness on this window is exactly the
statement that the four maps are available as values of `o`.

## Theorem 4 — `o` Is A Smallest Complete Extra Object On This Window

**Claim.** Any extra object that represents every Record-allowed occupancy
history on `W` must distinguish those four histories, and is therefore at
least as fine as `o` up to relabeling. The occupancy map is a smallest
complete extra object on this window.

**Proof.** A complete extra object is a function `Φ` of the window history
such that `Φ(μ, o) = Φ(μ, o')` implies `o = o'` for the four executed
occupancies. Equivalently, `Φ` is injective on `{o00, o10, o01, o11}` once
`μ` is held fixed. Any such `Φ` therefore has at least four values on this
window.

The occupancy map itself is injective on that four-element set: the four
rows of the occupancy table are distinct. Hence `o` is complete. If a
complete `Φ` identified two of those rows, injectivity would fail. If a
complete `Φ` omitted a row, some allowed history would be unrepresented.
Therefore every complete extra object admits a factorization through `o` up
to relabeling of the four values.

Coarser displayed objects fail completeness. The pair `(μ, I)` takes only
three combined labels on the four histories, because `I` has three values
and collides on `o10` and `o01`. The capacity-1 token takes only three
values and omits `o11`. The rate `|o|/|W|` takes the same three numbers as
`I/2`. None of those objects is complete. No strictly coarser object than
`o` can be complete, because `o` already has one value per allowed history.

## Theorem 5 — Display `o`; Do Not Adopt It

**Claim.** The quoted axiom sentences do not select `o`. Display the
occupancy map. Do not adopt it as an axiom. The rate `|o|/|W|` is not a
separate target here.

**Proof.** The Admissibility sentence names a content law from nearest-
neighbor conditions. The reading note says that law does not supply the
formation site, probability, or rate. The Record lock sentence applies when
a record is present. Additivity and `I(empty)=0` constrain readout of
present, pairwise-disjoint records; they do not pick which subset of `W`
is present. Occurrence says that records form somewhere; it does not pick
a pattern on `{x, y}`.

Theorem 1 already shows that the objects the axioms do name on this
exhibit — a content law `μ` and an additive unit-lock count `I` — fail to
recover `o`. Theorems 3 and 4 show what a complete extra object on the
window must be. Naming that object is a display of the missing input. It
is not a derivation that the axioms select it, and it is not a proposal to
edit axiom text.

The rate `|o|/|W|` equals `I(o)/2`. It is determined by the unit-lock
count and inherits the `o10`/`o01` collision. It is not an independent
complete object and is not a separate target in this note.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom-sentence change is
  necessary;
- claim that no formation rule exists;
- claim that records never form, or that `o00` is a completed empty
  universe;
- derive the masses `1/3` and `2/3` from nearest-neighbor data;
- replace the unit-lock count by a content-valued readout that would
  distinguish `A` from `B`;
- identify the executed `{A, B}` menu with the full one-site possibility
  domain `M_2(C)`;
- promote a capacity-1 token to a complete occupancy object;
- treat rate `|o|/|W|` as an independent target.

The scope is the exact two-site split: four occupancy maps, a shared
content law, a three-valued unit-lock count, and a three-valued token
slice.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Admissibility distribution sentence | premise | quoted; no edit |
| Admissibility reading note on formation site/rate | premise | quoted; no edit |
| Record occurrence, lock, uniqueness, additivity, `I(empty)=0` | premise | quoted; no edit |
| four occupancy maps on `W={x,y}` | Theorems 1--4 | listed here |
| declared `μ` with masses `1/3`, `2/3` | Theorems 1, 3 | executed here |
| unit-lock count `I(o)` | Theorems 1, 4, 5 | computed here |
| capacity-1 token `T` | Theorem 2 | executed slice |
| axiom selection of `o` | residual | extra; not derived |
| observed frequencies or fitted occupancies | none | not used |

The exact advance is a finite occupancy-table theorem that names the
smallest complete extra object on one window. Independent audit is
required. This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The missing extra input is an object that can represent every Record-allowed occupancy on a two-site window. This note asks for the smallest such object and answers with the occupancy map `o:W→{0,1}`. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for a smallest complete occupancy extra object, for histories `o10`/`o01`/`o11` as a completeness table, and for a capacity-1 token miss of double occupancy. Hits: the 2026-06-06 record-formation residual is a process/rule gap, not a four-row completeness table; the 2026-07-04 occupancy-append notes concern a different append object; the 2026-08-10 type-separation note leaves physical construction of registered partitions open. No landed four-history occupancy-completeness theorem naming `o` as a smallest extra object appears on that commit. |
| V3 | Independently checkable? | Textbook additivity does not mention the four occupancy rows, the token slice, or the `o10`/`o01` collision at `I=1`. The runner rebuilds the four maps, the unit-lock counts, and the token encoding in exact `Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The discriminating witnesses are that `(μ, I)` identifies `o10` with `o01` and that a capacity-1 token omits `o11`, while `o` itself has one row per allowed history. Those identities are not restatements of the axiom sentences. |
| V5 | One-step relabel? | No. Quoting additivity and the reading note does not by itself produce the four-row table or the fineness argument that `o` is smallest among complete extra objects. |

## No-Go Discipline Gate (Theorems 1, 2, and 5)

The negative claims are restricted to: `(μ, I)` does not recover `o` on this
window; a capacity-1 token does not represent `o11`; the axioms do not
select `o`. This is not a claim that no formation rule exists.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| `(μ, I)` recovers occupancy | treat shared content law and unit-lock count as already naming the pattern | Theorem 1: `o10` and `o01` share `μ` and `I=1` | **ATTEMPTED** |
| capacity-1 token is complete | treat `T ∈ {x, y, none}` as representing every allowed history | Theorem 2: `o11` has no token value | **ATTEMPTED** |
| rate is a separate complete object | treat `|o|/|W|` as independent of `I` and complete | Theorem 5: rate equals `I/2` and collides on `o10`, `o01` | **ATTEMPTED** |
| axiom sentences select `o` | read occurrence, lock, or additivity as a pattern selector | Theorem 5: those sentences do not pick a subset of `W` | **ATTEMPTED** |
| adopt the occupancy map | close the residual by writing `o` into axiom text | Theorem 5: display only; no axiom sentence is edited | **ATTEMPTED** |

### N2 — wall independence

Theorems 1, 2, and 5 close only the route that would recover every
window occupancy from `(μ, I)` or from a capacity-1 token, and the route
that would treat display of `o` as axiom selection. They do not close a
later derivation of a formation rule, a later content-valued readout, or a
later larger-window object.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}` | explicit hypothesis |
| occupancy maps `o:W→{0,1}` | declared extra object |
| unit-lock count `I(o)` | declared additive occupancy readout |
| one-site law `μ` on `{A,B}` | declared content law; masses not derived |
| capacity-1 token | declared incomplete slice |
| rate `|o|/|W|` | function of `I`; not a separate target |
| axiom selection of `o` | extra; not derived |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; formation-site/rate reading note; Record occurrence, lock, uniqueness, additivity, `I(empty)=0` | quoted as premises only; no edit |
| four occupancy rows | completeness table | listed here |
| token slice | miss of `o11` | executed here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the four occupancy rows and the three token values | no classification of every map on a larger window |
| per site | occupancy bits and the same `μ` at `x` and at `y` | no composite bonded-pair dynamics |
| per mode | unit-lock count versus content label; no spectral mode | no harmonic-mode exhaustion |
| per block | only the declared two-site window is executed | no formation rate law and no lattice process |
| lattice-wide | checked and not executed | no lattice-wide claim that `o` is selected |

The obstruction is per-window / declared two-site table; it is not
lattice-wide.

### N6 — live partial-closure paths

1. A later derivation that selects one occupancy pattern on `W`.
2. A later complete extra object on a larger window, which must still
   restrict to something at least as fine as `o` on every two-site subset.
3. A later content-valued readout, independent of the unit-lock count.
4. A later formation rule. Display of `o` does not forbid one.

No axiom sentence is edited here.

### N7 — hostile steelman

> The pair `(μ, I)` already names the history: the content law plus how
> many records formed. The token names which site formed when `I=1`.
> Together they recover occupancy, so no extra object is missing.

**Answer.** The token is not supplied by `(μ, I)`. Theorem 1 uses only
`(μ, I)` and already collides on `o10` versus `o01`. Adding a capacity-1
token repairs that collision and then fails on `o11` (Theorem 2). The
object that repairs both failures is the occupancy map (Theorems 3 and 4).
That map is extra relative to the quoted axiom sentences (Theorem 5).

### N8 — cross-cycle echo

Earlier formation residuals prune routes that would force a formation
rule, site, or rate from the axiom baseline, or that would read occupancy
off a product of one-site laws, or that would treat support as a site
selector. The present note faces a narrower residual: once occupancy is
granted as extra, the smallest complete extra object on a two-site window
is the occupancy bit-map itself. Those earlier notes are not cancelled.
They remain notes about different premises.

**Gate disposition.** PASS for the four-row completeness table, the two
mutations of Theorems 1 and 2, and the display-only residual of Theorem 5.
FAIL / DO NOT SHIP for “no formation rule exists” or for editing an axiom
sentence to name `o`.

## Primary Runner

[`scripts/occupancy_pattern_is_smallest_complete_formation_input_2026_08_13.py`](../scripts/occupancy_pattern_is_smallest_complete_formation_input_2026_08_13.py)
rebuilds the four occupancy maps, the shared `μ` with masses `1/3` and
`2/3`, the unit-lock counts, and the capacity-1 token encoding in exact
`Fraction` arithmetic. A predicate “`(μ, I)` recovers `o`” must fail on
`o10` versus `o01`. A predicate “the token represents every history” must
fail on `o11`.
