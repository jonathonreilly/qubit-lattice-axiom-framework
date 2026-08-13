---
claim_id: permanence_not_visible_in_scalar_i_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with two snapshots and occupancy already one unit lock, the named scalar readout I and the site-blind lock bag assign the same sequence to a legal stay and to an illegal site-to-site move, while the reconstructed site-indexed lock field J splits them. The Record permanence clause is therefore not a property of the named scalar readout on this window. The note displays a C1 retype to J as the cheapest change that makes permanence checkable from the named readout; it does not adopt that retype, does not reopen formation, and does not install a pairing, a clock, r=1/2, or L_phys."
upstream_dependencies:
  - minimal_axioms
runner: scripts/permanence_not_visible_in_scalar_i_hypothetical_2026_08_13.py
---

# Record Permanence Is Not Visible In Scalar I

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact two-site, two-snapshot integer occupancy arithmetic on a
displayed stay versus an illegal move. Hypothetical test of the Record
permanence clause against the named scalar readout. Not a formation-rate
claim and not an addition-order-of-legal-growth claim.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/permanence_not_visible_in_scalar_i_hypothetical_2026_08_13.py`](../scripts/permanence_not_visible_in_scalar_i_hypothetical_2026_08_13.py)

Parent on `origin/main`: the axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The current Record axiom says records are permanent. The named readout is
still scalar `I`. On a two-site window whose occupancy is already one unit
lock, a legal stay and an illegal site-to-site move have the same `I`
sequence and the same site-blind lock bag. The reconstructed site-indexed
lock field `J` splits them. Permanence is therefore not a property of the
named scalar readout on this window.

Displayed counterfactual C1: the named Record readout is the site-indexed
lock field `J`, not scalar `I`. A C1 retype is the cheapest change that
makes permanence checkable from the named readout on this window. This note
does not adopt that retype.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer I-sequence, bag, and J-sequence identities on one declared two-site two-snapshot window; C1 retype, axiom adoption, formation, pairing, clock, r=1/2, and L_phys remain unadopted."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "is Record permanence visible in the named scalar readout I on a two-site stay-versus-move window"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed stay and illegal-move sequences; no axiom edit"
hypothetical_axiom_status: "C1 follow-on: Record permanence is not visible in scalar I; J splits stay vs illegal move; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Quoted Record Wording

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.
>
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

The permanence sentence is the constraint under test. The named readout
remains scalar `I`. This note does not rewrite those sentences.

## Exact Objects

Window `W={x,y}` in site order `(x,y)`. Lock menu `{A,B}`. Two snapshots
`t=0,1`. Occupancy is already one unit lock at `t=0`.

Reconstructed C1 lock field, displayed and not adopted:

```text
J : W → {0} ∪ {A,B}
J(z) = 0 if site z is unformed, else the locked menu entry at z.
I(J) = |{z in W : J(z) ≠ 0}|
bag(J) = { J(z) : z in W and J(z) ≠ 0 }
```

`0` is absence, not a menu element. Occupancy is the retract
`o_J(z)=0` if `J(z)=0` else `1`. No pairing is placed on `J`. No clock map
is imported. Snapshots are an unordered pair of labels `{0,1}` used only to
compare two configurations; they are not a time metric.

Two histories, each already carrying one unit lock at `t=0`:

| History | Role | `J_0` | `J_1` |
|---|---|---|---|
| `S` | legal stay | `(A,0)` | `(A,0)` |
| `M` | illegal move | `(A,0)` | `(0,A)` |

Permanence on this window means: if `J_0(z)≠0`, then `J_1(z)=J_0(z)`. The
stay keeps the lock `A` at `x`. The move empties `x` and places `A` at `y`.
Record says records are permanent, so `M` is forbidden as a history.

## Theorem 1

The `I`-sequence and the site-blind bag do not split stay from illegal move.

```text
I_seq(S) = (I(J_0), I(J_1)) = (1,1)
I_seq(M) = (1,1)
bag_seq(S) = ({A},{A})
bag_seq(M) = ({A},{A})
```

Both snapshots of both histories have occupancy one and lock content `{A}`.
Scalar `I` and the site-blind bag are therefore identical on `S` and `M`.

## Theorem 2

The `J`-sequence splits them.

```text
J_seq(S) = ((A,0),(A,0))
J_seq(M) = ((A,0),(0,A))
J_seq(S) ≠ J_seq(M)
```

Identity gates call `I_seq(S)`, `I_seq(M)`, `J_seq(S)`, and `J_seq(M)`.

## Theorem 3

Quote current Record: “records are permanent.” That constraint is not a
property of the named scalar readout. On this window the cheapest change
that makes permanence checkable from the named readout is a C1 retype to
`J`. The note displays that retype and does not adopt it. The current
file still names additive scalar `I` with `I(empty)=0`.

## Theorem 4

This is not a formation rate and not an addition-order-of-legal-growth
exercise. There is no growth from empty: occupancy stays `1` on every
snapshot of `S` and of `M`. The comparison is stay versus illegal move of
an already-formed unit lock. Formation is not reopened. No site-picking
rule and no occurrence rate are selected.

## Theorem 5

Display only. Do not adopt C1. Do not force `r=1/2`. Do not adopt
`L_phys`. Do not put a pairing on `J`. Do not import a clock.

## Mutation Predicates

The predicate “`I_seq(S)` differs from `I_seq(M)`” fails.

The predicate “`J_seq(S)=J_seq(M)`” fails.

## What This Note Does Not Claim

- It does not edit the axiom memo.
- It does not adopt a Record rewrite, a C1 retype, `L_phys`, or `r=1/2`.
- It does not place a pairing on `J`.
- It does not import a clock, a formation rate, or a site-picking rule.
- It does not treat an unmerged pull request as a parent.

## Runner

[`scripts/permanence_not_visible_in_scalar_i_hypothetical_2026_08_13.py`](../scripts/permanence_not_visible_in_scalar_i_hypothetical_2026_08_13.py)
recomputes `I_seq` and `J_seq` from the two displayed histories with exact
integers, guards the quoted permanence sentence, and checks the mutation
predicates. No runner cache is written.

## No-Go Discipline Gate

The negative claims are restricted to stay versus illegal move on two
snapshots. The gate does not certify a Record rewrite.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| I-seq as a permanence check | compare `I_seq(S)` with `I_seq(M)` | Theorem 1: both `(1,1)` | **ATTEMPTED** |
| Site-blind bag as a permanence check | compare bags | Theorem 1: both `({A},{A})` | **ATTEMPTED** |
| J-seq as a permanence check | compare `J_seq` | Theorem 2: `((A,0),(A,0))` vs `((A,0),(0,A))` | **ATTEMPTED** |
| Current Record as a named-readout permanence test | quote “records are permanent” | Theorem 3: constraint is not a property of scalar `I` | **ATTEMPTED** |
| Rate, clock, pairing, `r=1/2`, `L_phys` | enlarge the display | Theorem 4–5: refused | **ATTEMPTED** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| I-seq / J-seq | no: `I` identifies stay with move | no: `J` splits them and still yields the same `I` | independent |
| permanence type / formation rate | no: stay vs move is not a rate | no: a rate would still need a typed stack | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}` | stipulated finite object |
| occupancy already 1 | stipulated; not growth from empty |
| permanence | quoted Record sentence |
| clock, rate, pairing, `r=1/2`, `L_phys` | not used |
| observations | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | records are permanent; content-only additive `I` | exact current wording; no J-process borrowed |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two snapshots; unit lock `I=1` | no classification of every history |
| per site | illegal move empties `x` and occupies `y` | no lattice-wide permanence dynamics |
| per mode | I-seq and bag are stay/move-blind; J-seq is not | no spectral claim |
| per block | permanence visibility in named readout only | no rate, clock, `L_phys`, or pairing |
| lattice-wide | not executed | two-site window only |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

1. Keep current Record: permanence as an existence constraint, scalar `I`.
2. Owner wording could name `J` later; permanence would then be checkable.
3. A later derivation could produce a site-indexed stack from Record dynamics.

None of those paths is taken here.

### N7 — hostile steelman

> Permanence already forbids `M`, so comparing `S` with an illegal history
> is not a readout test. Scalar `I` only needs to read legal records.

The steelman names a real constraint — `M` is forbidden — and then
overclaims that the named readout therefore sees permanence. Theorem 1
shows the named readout cannot tell `S` from `M`. A constraint that is
invisible to the named readout is not a property of that readout.

### N8 — cross-cycle echo

This is a C1 follow-on permanence test, not `c1hist` (no growth from
empty), not a second formation exercise, and not pairing-on-`J`.

**Gate disposition:** PASS for (i) I-seqs agree, (ii) J-seqs differ, and
(iii) permanence is not a property of scalar `I`. FAIL / DO NOT SHIP for
"adopt C1," "install a clock," "select a formation rate," "force `r=1/2`,"
"adopt `L_phys`," or "put a pairing on `J`."

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing this artifact.
