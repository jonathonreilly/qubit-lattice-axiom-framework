---
claim_id: record_readout_classification_i_bag_o_j_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with a two-point lock menu, the four displayed Record readouts scalar I, site-blind bag (I, locks), weak occupancy o, and strong site-indexed J are pairwise inequivalent: I and the bag miss site, I and o miss lock, and only J splits ordered two-site locks; none is adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_readout_classification_i_bag_o_j_hypothetical_2026_08_13.py
---

# Record Readout Classification: I / Bag / Occupancy / J

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact classification of four displayed readouts on one
two-site window. Hypothetical discriminating test. No axiom edit.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_readout_classification_i_bag_o_j_hypothetical_2026_08_13.py`](../scripts/record_readout_classification_i_bag_o_j_hypothetical_2026_08_13.py)

## Result Up Front

Current Record names a scalar additive readout `I` determined by record
content alone. It does not name a site-indexed occupancy map and does not
name a site-indexed lock map. Four displayed objects sit on the same
two-site histories. They are not interchangeable.

- Scalar `I` counts occupied sites and is site-blind and lock-blind.
- The site-blind bag `(I,` multiset of locks`)` sees lock content and still
  misses which site carries which lock.
- Weak occupancy `o` sees which sites formed and is lock-blind.
- Strong `J` sees both the site and the lock. It is the only displayed
  object that splits the ordered two-site pair.

The five histories below are the discriminating witnesses. The table is
displayed. None of the four readouts is adopted. No pairing is placed on
`J`. The value `r=1/2` is not forced. `L_phys` is not adopted. No fifth
extra object is named.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four readouts are compared by exact integer identities on five stipulated two-site histories; none is adopted as axiom content, and no Newton pairing, r=1/2, L_phys, or fifth extra is introduced."
trace_class: negative_route_pruning
target_claim_id: record_readout_classification_i_bag_o_j
target_blocker_text: "treat scalar I, a site-blind content bag, weak occupancy o, and strong site-indexed J as interchangeable Record readouts"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact on the declared two-site window and five histories; owner wording, if any, must pick weak o or strong J; none of the four displayed readouts is adopted"
hypothetical_axiom_status: "C1 follow-on: classify Record readouts I / (I,bag) / o / J; none adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The only parent on `origin/main` is the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). Occupancy and
lock arithmetic is reconstructed here. No unmerged pull request is a
premise.

Let `W={x,y}` and `M={A,B}`. A **history** is an occupancy

`o:W → {0,1}`

together with one lock in `M` at each occupied site. Records are
permanent and a site never carries more than one record, so the lock at
an occupied site is unique. The empty site carries no lock.

Four displayed readouts (none adopted):

| Symbol | Domain | Definition |
|---|---|---|
| scalar `I` | histories → `{0,1,2}` | `I(h)=|o^{-1}(1)|` |
| site-blind bag `β` | histories → `N ×` multisets of `M` | `β(h)=(I(h),` multiset of locks`)` |
| weak occupancy `o` | histories → `{0,1}^W` | the occupancy map itself |
| strong `J` | histories → `({0}∪M)^W` | `J(z)=0` if `o(z)=0`, else the lock at `z` |

Unit locks are used throughout: each occupied site contributes strength
one to `I`. This is the current additive scalar on pairwise-disjoint
records, restricted to the window, with `I(empty)=0`.

The five discriminating histories:

| History | Occupancy `o=(o(x),o(y))` | Locks | `I` | bag `β` | `J=(J(x),J(y))` |
|---|---|---|---:|---|---|
| `h10A` | `(1,0)` | `A` at `x` | 1 | `(1,{A})` | `(A,0)` |
| `h10B` | `(1,0)` | `B` at `x` | 1 | `(1,{B})` | `(B,0)` |
| `h01A` | `(0,1)` | `A` at `y` | 1 | `(1,{A})` | `(0,A)` |
| `h11AB` | `(1,1)` | `A` at `x`, `B` at `y` | 2 | `(2,{A,B})` | `(A,B)` |
| `h11BA` | `(1,1)` | `B` at `x`, `A` at `y` | 2 | `(2,{A,B})` | `(B,A)` |

The braces in the bag column are multisets. On these five histories every
occupied-site lock list is already a set, so sorting the lock list is a
faithful representative of the multiset.

## Exact Target And Obligation Graph

**Exact target.** Decide which of the four displayed readouts split the
three columns site, lock, and ordered two-site lock, and decide whether
any readout coarser than `J` recovers the lock at a named site on the
displayed set.

| Obligation | Role | Disposition |
|---|---|---|
| reconstruct occupancy/lock arithmetic on `W` | objects | stipulated from the Record sentences quoted below |
| split the site column `h10A` vs `h01A` | Theorem 1 | `I` and `β` fail; `o` and `J` succeed |
| split the lock column `h10A` vs `h10B` | Theorem 2 | `I` and `o` fail; `β` and `J` succeed |
| split ordered two-site locks `h11AB` vs `h11BA` | Theorem 3 | only `J` succeeds |
| recover the lock at a named site | Theorem 4 | `lock_J` recovers every lock; no map of `I`, of `o`, or of `β` does so on the displayed set |
| keep the display hypothetical | Theorem 5 | no pairing on `J`, no `r=1/2`, no `L_phys`, no fifth extra, no adoption |

## Current Record Sentences

The current Record section of the axiom memo states:

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

> A state is a configuration of records.

Those sentences name scalar additive `I` and a content-only readout. They
name neither weak occupancy `o` nor strong `J`. Owner wording, if any,
must pick weak or strong. This note displays the table and does not
adopt either.

## Theorem 1 — Site Column

`I` and the bag fail to split `h10A` from `h01A`:

`I(h10A)=1=I(h01A)`,

`β(h10A)=(1,{A})=β(h01A)`.

Occupancy and `J` split them:

`o(h10A)=(1,0) ≠ (0,1)=o(h01A)`,

`J(h10A)=(A,0) ≠ (0,A)=J(h01A)`.

A site-blind count, and a site-blind content bag, cannot see that the
same unit lock of type `A` sits at `x` on one history and at `y` on the
other. Weak occupancy sees the site and is silent on the lock. Strong
`J` sees both.

## Theorem 2 — Lock Column

`I` and occupancy fail to split `h10A` from `h10B`:

`I(h10A)=1=I(h10B)`,

`o(h10A)=(1,0)=o(h10B)`.

The bag and `J` split them:

`β(h10A)=(1,{A}) ≠ (1,{B})=β(h10B)`,

`J(h10A)=(A,0) ≠ (B,0)=J(h10B)`.

Weak occupancy is lock-blind. Scalar `I` is lock-blind. A content bag
sees which lock occurred once it forgets the site. Strong `J` sees the
lock at the named site.

## Theorem 3 — Ordered Two-Site Locks

`I`, the bag, and occupancy all fail to split `h11AB` from `h11BA`:

`I(h11AB)=2=I(h11BA)`,

`β(h11AB)=(2,{A,B})=β(h11BA)`,

`o(h11AB)=(1,1)=o(h11BA)`.

Only `J` splits them:

`J(h11AB)=(A,B) ≠ (B,A)=J(h11BA)`.

A site-blind content bag is therefore not a substitute for `J`. The two
histories carry the same two locks and the same two occupied sites. They
disagree on which site carries which lock. Only a site-indexed lock map
records that disagreement.

## Theorem 4 — Named-Site Lock Recovery

Define

`lock_J(z) = J(z)` if `J(z)≠0`, else `none`.

On every displayed history, `lock_J` recovers every lock: it returns the
menu entry at each occupied site and `none` at each empty site.

No map that depends only on `o`, or only on `I`, or only on `β`,
recovers the lock at a named site on the set
`{h10A,h10B,h11AB,h11BA}`.

- `h10A` and `h10B` share `o=(1,0)` and `I=1` but lock `A` versus `B` at
  `x`. Any function of `o` or of `I` is constant on that pair.
- `h11AB` and `h11BA` share `o=(1,1)`, `I=2`, and `β=(2,{A,B})` but lock
  `A` versus `B` at `x`. Any function of `o`, of `I`, or of `β` is
  constant on that pair.

Strong `J` commits `M` as its nonzero codomain: every nonempty value is
an element of the lock menu. Weak `o` does not: its values are bits, and
the menu never appears.

Current Record names scalar additive `I` and content-only readout. It
names neither `o` nor `J`. The table above is the displayed comparison.
It is not an axiom rewrite.

## Theorem 5 — Scoped Residual

This note does not put a pairing on `J`. It does not force `r=1/2`. It
does not adopt `L_phys`. It does not name a fifth extra. It does not
reopen formation. It does not import Newton. The four displayed
readouts remain displayed. None is adopted.

The residual after the table is owner wording, if any: pick weak
occupancy or strong `J`, or keep the current scalar content-only `I`.
That choice is not made here.

## Split Summary

| Pair | `I` | bag `β` | weak `o` | strong `J` |
|---|---|---|---|---|
| `h10A` vs `h01A` (site) | same | same | split | split |
| `h10A` vs `h10B` (lock) | same | split | same | split |
| `h11AB` vs `h11BA` (order) | same | same | same | split |

## No-Go Discipline Gate

The negative claims are restricted to inequivalence of the four
displayed readouts on the five stipulated histories. The gate does not
certify that a later derivation cannot produce one of these objects, and
it does not certify that Record must be rewritten.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Scalar `I` as a complete readout | ask `I` to split site or lock | Theorems 1 and 2: `I=1` on `h10A`, `h10B`, and `h01A` | **ATTEMPTED** |
| Site-blind bag as a substitute for `J` | ask `β` to split ordered two-site locks | Theorem 3: `β=(2,{A,B})` on both `h11AB` and `h11BA` | **ATTEMPTED** |
| Weak occupancy as a lock readout | ask `o` to split `h10A` from `h10B` | Theorem 2: `o=(1,0)` on both | **ATTEMPTED** |
| Recover a named-site lock from `I`, `o`, or `β` | seek a function of one coarse readout | Theorem 4: each coarse readout is constant on a pair that disagrees at `x` | **ATTEMPTED** |
| Pairing on `J`, force `r=1/2`, adopt `L_phys`, or name a fifth extra | enlarge the display | Theorem 5: refused | **ATTEMPTED** |
| Treat the table as an axiom rewrite | adopt `o` or `J` | refused; current Record still names scalar `I` and content-only readout | **ATTEMPTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| site column / lock column | no: `o` splits site and is lock-blind | no: `β` splits lock and is site-blind | independent |
| site column / ordered two-site locks | no: `o` splits `h10A`/`h01A` and identifies `h11AB` with `h11BA` | no: `J` splits order and also splits site, but order-splitting is strictly finer | independent obligations |
| lock column / ordered two-site locks | no: `β` splits `h10A`/`h10B` and identifies `h11AB` with `h11BA` | no: order-splitting implies lock-splitting on these histories, not conversely | bag is strictly coarser than `J` |
| weak `o` / strong `J` | no: occupancy is the support of `J`, not the lock values | yes definitionally: `o(z)=0` iff `J(z)=0` | `o` is a retract of `J`, not a substitute |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}` | stipulated finite object, not a lattice-wide claim |
| menu `M={A,B}` | stipulated two-point lock menu; not a Born menu and not an effect algebra |
| occupancy `o` | reconstructed from Record permanence and one-record-per-site; displayed, not adopted |
| lock at an occupied site | the unique admissible possibility locked by the record at that site |
| bag `β` | site-blind multiset of those locks together with the count `I` |
| strong `J` | site-indexed lock map with sentinel `0` on empty sites; displayed, not adopted |
| unit strengths | each occupied site contributes `1` to `I`; matches `I(empty)=0` and additivity on disjoint unit records |
| Newton pairing, `r=1/2`, `L_phys` | not used |
| fifth extra | not named |
| observations or empirical frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Records form; one lock per present record; one record per site; permanence; only records are readable; content-only readout; additive scalar `I` with `I(empty)=0`; a state is a configuration of records | exact current wording; no `o` or `J` borrowed from the memo |

No other repository note is a parent. Occupancy/lock arithmetic is
reconstructed in the objects section. Unmerged pull requests are not
cited.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | five histories, four readouts, exact integer table | no classification of every conceivable readout |
| per site | named sites `x` and `y` in a two-site window | no lattice-wide formation rule |
| per mode | site column, lock column, ordered two-site column | no spectral or harmonic mode claim |
| per block | Record readout type only | no Newton, Born, rate, or formation-process closure |
| lattice-wide | not executed | no lattice-wide dynamics or axiom necessity |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

1. Keep current Record: scalar additive `I` and content-only readout,
   with occupancy and site-indexed locks remaining extra bookkeeping.
2. Owner wording could pick weak occupancy as the named extra formation
   object and leave locks to the existing one-possibility sentence.
3. Owner wording could pick strong `J` as the named readout; occupancy
   would then be the support of `J`, not a second extra.
4. A later derivation could produce one of these maps from Record
   dynamics without changing the axiom text.
5. A later derivation could prove that content-only readout already
   forces one of the four objects on a declared window.

None of those paths is taken here. The approved primitives were not
needed and are not counted as extra walls.

### N7 — hostile steelman

> Content-only readout already includes the lock, and additivity already
> includes the count, so the bag is just `I` plus content. Site labels
> are lattice structure, not Record structure. Therefore `J` is a
> presentation of the same records and is not a different readout.

The steelman is half right and half wrong. The bag is exactly `I` plus
site-blind content, and Theorem 2 confirms that this pair sees the lock
column. Theorem 1 and Theorem 3 show that the same pair is silent on
which site carries which lock. Lattice structure names the sites. It
does not by itself assign a lock to a named site. That assignment is
the extra map `J`. The steelman therefore identifies a real object — the
bag — and then overclaims that the bag is `J`.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| Record names additive scalar `I` and content-only readout | those sentences remain the current authority | `I` and the bag are the content-only column; they are displayed, not enlarged |
| occupancy is easy to treat as a synonym for lock | the type split is site-blind content versus site-indexed lock | Theorems 1--3 keep occupancy, bag, and `J` distinct |
| a site-indexed readout can recover occupancy as its support | that retract is definitional for `J` | Theorem 4 records the retract and refuses to adopt `J` |

Cross-cycle movement does not license an axiom rewrite. The table is a
classification, not a proposal.

**Gate disposition:** PASS for (i) inequivalence of `I`, `β`, `o`, and
`J` on the displayed histories, (ii) failure of the bag as a substitute
for `J`, and (iii) named-site lock recovery only from `J`.
FAIL / DO NOT SHIP for "an axiom update is necessary," "adopt `J`,"
"adopt `o`," "put a pairing on `J`," "force `r=1/2`," "adopt `L_phys`,"
or "name a fifth extra."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record sentences | semantic baseline | supplied; no edit |
| window `W`, menu `M`, five histories | stipulated finite objects | constructed here |
| unit-lock additivity | `I` on the window | reconstructed from `I(empty)=0` and disjoint additivity |
| Newton pairing, `r=1/2`, `L_phys` | out of scope | not imported |
| observed frequencies, fits | none | not used |

The exact advance is a type classification on one window. It does not
move any TOE percentage. It makes the next wording decision testable:
keep scalar `I`, or pick weak `o`, or pick strong `J`. The note picks
none of those.

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing or self-reviewing this
artifact.
