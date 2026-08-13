---
claim_id: admissibility_support_constrains_content_not_formation_site_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the exact finite menu {A,B,C} with μ(A)=1/3, μ(B)=2/3, μ(C)=0, a forming record cannot lock C because admissible content is the support. The same per-site μ is compatible with two occupancy patterns on a 2-site star that differ in which site forms, and with two distinct formation counts. Records form does not pick the site or the rate. Not an axiom edit."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py
---

# Admissibility Support Constrains Locked Content, Not Formation Site

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-menu support of one declared content law, and two
occupancy exhibits on a 2-site star.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py`](../scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py)

## Result Up Front

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Read with Record, that distribution is the content law for a forming record:
it names which possibility may be locked, conditional on formation at that
site. On a finite menu its support is exactly the admissible set. It does not
name the formation site or the formation rate.

On the declared three-point menu the support constraint is sharp and the site
and rate remain free. A forming record at a site carrying this law cannot lock
the zero-mass point. The same law is compatible with formation at a named site
and with no formation at that site, and it is compatible with two different
formation counts. The occurrence sentence Records form. is used only as
occurrence: at least one record exists in the realized history. No axiom
sentence is edited.

## Exact Objects

Let the finite local possibility menu at one site be

`X = {A, B, C}`.

Let `μ` be the probability measure on `X` with

`μ(A) = 1/3`, `μ(B) = 2/3`, `μ(C) = 0`.

These three masses are the declared content law. They sum to one:

`μ(A) + μ(B) + μ(C) = 1/3 + 2/3 + 0 = 1`.

On finite menus the current axiom memo identifies available/admissible content
with support: exactly the possibilities of nonzero probability. The support
computed from the masses is

`supp(μ) = {ω ∈ X : μ(ω) > 0} = {A, B}`.

Thus `C` is not admissible.

The 2-site star is the nearest-neighbor pair `{x, y} ⊂ Z^3` with the single
edge `xy`. On this fragment each site has the other as its unique neighbor, so
the nearest-neighbor conditions are the same at `x` and at `y`. Translation
covariance of the fixed admissibility rule therefore assigns the same `μ` to
both sites. Occupancy is not part of that condition in this exhibit: the
content law is the same whether or not a record is present.

A site-occupancy pattern on the star is a partial function from `{x, y}` to
`X`. Absence of a value means no record at that site. Record uniqueness makes
the partial function at most single-valued. A pattern is **lawful** for `μ`
when every locked value lies in `supp(μ)`. A pattern **satisfies occurrence**
when at least one site carries a record.

The current Record wording used below is:

Records form.

When present, a record locks exactly one admissible local possibility.

## Theorem 1 — Support Constrains Locked Content

Let a record form at a site carrying this `μ`. The Record axiom requires that
the lock `L` be exactly one admissible local possibility. On the finite menu,
admissible means `μ(L) > 0`. Because `μ(C) = 0`, the point `C` is outside
`supp(μ)`, so `L ≠ C`.

The same computation permits `L = A` and `L = B`. The masses `1/3` and `2/3`
are the relative odds among admissible alternatives; only positivity is used
to exclude `C`. The support constraint is therefore a constraint on locked
content, not a statement that the site must form and not a statement that it
must not form.

## Theorem 2 — The Same `μ` Does Not Pick The Formation Site

The axiom memo states that the distribution concerns which possibility a
forming record locks, conditional on formation at that site; it does not
supply the formation site. The following two lawful occupancy patterns on the
2-site star share the same per-site `μ` and differ in which site forms.

| Pattern | lock at `x` | lock at `y` | formed sites | count |
|---|---|---|---|---|
| `ω_x` | `A` | empty | `{x}` | `1` |
| `ω_y` | empty | `A` | `{y}` | `1` |

Both patterns use the same content law `μ` at `x` and at `y`. Both lock only
admissible content. Both are nonempty, so both are compatible with Records
form. They are distinct as occupancy maps: `ω_x` has a record at `x` and none
at `y`, while `ω_y` has a record at `y` and none at `x`.

In particular, the same `μ` at site `x` is compatible with formation at `x`
(`ω_x`) and with no formation at `x` (`ω_y`). Occurrence names that records
form somewhere in the realized history. It does not select the site.

## Theorem 3 — The Same Content Law Does Not Fix The Rate

The axiom memo likewise does not supply a formation rate. The next two lawful
patterns share the same per-site `μ` and have different formation counts.

| Pattern | lock at `x` | lock at `y` | formed sites | count |
|---|---|---|---|---|
| `ω_1` | `A` | empty | `{x}` | `1` |
| `ω_2` | `A` | `B` | `{x, y}` | `2` |

The counts are read off the occupancy maps: `ω_1` occupies one site and `ω_2`
occupies two. Both lock only admissible content, both are nonempty, and both
carry the same content law `μ`. Therefore two different formation counts are
compatible with one content law. Rate remains unfixed.

No further formation process is introduced. The two counts are only an
existence exhibit that the current sentences do not select between them.

## Boundary And Non-Claims

- No axiom sentence is edited. The displayed Admissibility and Record wording
  is the current wording.
- The exhibit is a finite menu. It does not identify `{A, B, C}` with a
  physical laboratory basis, and it does not replace the full one-site domain
  `M_2(C)`.
- Support is computed from the declared masses. The note does not derive those
  masses from nearest-neighbor data; it takes one exact content law and reads
  its support.
- Site and rate remain open supplier content. The two occupancy tables are
  compatibility witnesses, not a classification of all lawful histories and
  not a dynamics.
- Empty-everywhere is excluded only as a completed realized history, by
  Records form. A single named site may still be empty, as in `ω_y` at `x`.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: no edit
```

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The current reading notes already separate content-law support from site and rate. This note makes that split exact on one finite menu and one 2-site star. |
| V2 | New content? | Yes: the `{A,B,C}` masses, the computed support `{A,B}`, the two occupancy patterns that swap the formed site, and the two formation counts `1` and `2`. |
| V3 | Independently checkable? | Yes. The runner recomputes support from the masses and reads formed sites and counts from the occupancy maps. |
| V4 | More than a restatement? | Yes. The axiom memo states the type split; the note supplies an exact finite witness that content is constrained while site and rate are not. |
| V5 | One-step relabel? | No. Quoting the reading notes does not by itself produce the two-site occupancy tables or the distinct counts. |

## No-Go Discipline

This is a bounded compatibility exhibit. The only negative sentences are that
`C` is not lockable under this `μ`, and that the current sentences do not
select the formation site or the formation count. No other content law, graph,
or later site/rate theorem is excluded.

## Primary Runner

[`scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py`](../scripts/admissibility_support_constrains_content_not_formation_site_2026_08_13.py)
recomputes the three masses, the support, the lockable set, the two site
patterns, and the two formation counts in exact rational arithmetic.
