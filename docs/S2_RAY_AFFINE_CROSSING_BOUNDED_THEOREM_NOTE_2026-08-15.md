---
claim_id: s2_ray_affine_crossing_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Affine forms and crossing k_* of the displayed s2 same-k table are reported. No new Dijkstra. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/s2_ray_affine_crossing_2026_08_15.py
---

# Displayed S2 Same-k Affine Forms And Reverse Crossing

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact affine algebra on one displayed five-row s2 same-k table,
including the gapped row `k=7`, plus the unique positive reverse-crossing of
those affine forms and a locked-slope intercept-extra obstruction. The table
is displayed, not adopted. Uniqueness of any underlying hop realization is
not required.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/s2_ray_affine_crossing_2026_08_15.py`](../scripts/s2_ray_affine_crossing_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the cubic lattice `Z^3` with nearest-neighbor adjacency. That sentence is
  quoted only as ambient lattice context for an already-displayed table.

Everything after that quoted sentence is defined and proved here from the
displayed integers. This note does not recompute the table, does not search
paths, and does not write into Admissibility.

## Result Up Front

The displayed s2 same-k table is

```text
k    t_axis  t_body
7    21      24
13   27      42
14   28      45
18   32      57
19   33      60
```

Those five rows are computed lattice input, displayed not adopted. On
`k=13,14,18,19` (and `k=7`) the rows equal the affine forms `t_axis=k+14`
and `t_body=3k+3`. Equivalently, the locked slopes are `(α,γ)=(1,3)` with
intercepts `(β,δ)=(14,3)`.

The reverse comparison `3 t_axis^2 > t_body^2` on those affine forms has a
unique positive crossing

```text
k_* = (√3 · 14 - 3) / (3 - √3) = (11 + 13√3) / 2 ≈ 16.7583.
```

This crossing is strictly less than the separately displayed c2d4 crossing
`k_* ≈ 18.70`. Direct integer arithmetic on the displayed rows therefore
gives reverse failure at both `k=18` and `k=19`:

```text
k=18:  3 · 32^2 = 3072 < 57^2 = 3249,    reverse fails,
k=19:  3 · 33^2 = 3267 < 60^2 = 3600,    reverse fails.
```

Any extra that keeps the locked slopes `(α,γ)=(1,3)` and only changes
intercepts cannot restore reverse for all integers `k>k_*`. Displayed, not
adopted. Do not write into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact affine forms on the displayed five-row s2 table, unique positive reverse crossing earlier than the c2d4 crossing, and locked-slope intercept-extra obstruction are proved; the table is not adopted and no Admissibility edit is proposed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "report affine forms and reverse crossing of the displayed s2 same-k table"
source_of_blocker_text: handoff
reachability_to_target: advances
next_trace_action: "Use the displayed affine forms only as table algebra; do not adopt them as an Admissibility rule or recompute them by a path search."
artifact_role: theorem
conditional_surface_status: "exact on the displayed five-row table and locked-slope intercept extras; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

The Lattice sentence quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

No further Lattice content is used. Qubit is unused. Record is unused. The
Admissibility axiom is not an input to the algebra and is not edited:

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

The displayed integers are a separately supplied computed table. They are not
derived in this note and are not written into that admissibility rule.

## Exact Objects

Write the displayed rows as ordered triples `(k, t_axis(k), t_body(k))` for

```text
k in {7,13,14,18,19}.
```

The **reverse comparison** on a pair of positive integers is the predicate

```text
R(t_axis, t_body) := (3 t_axis^2 > t_body^2).
```

An **intercept extra** of the displayed slopes is a pair of integers `(β,δ)`
together with the affine forms

```text
t_axis = α k + β,    t_body = γ k + δ,    (α,γ)=(1,3).
```

The displayed intercepts are `(β,δ)=(14,3)`. Uniqueness of any underlying hop
realization is not required: the theorems below are statements about this
table and about locked-slope extras of this table.

## Theorem 1 — Affine Forms On The Displayed Rows

On k=13,14,18,19 (and k=7) the displayed rows equal

```text
t_axis(k) = k + 14,    t_body(k) = 3k + 3.
```

Direct substitution recovers every displayed pair. Equivalently, the
intercepts extracted from any row by `β = t_axis - k` and `δ = t_body - 3k`
are constantly `14` and `3`. Consecutive displayed pairs, including the gap
from `k=7` to `k=13`, have slope ratios

```text
Δ t_axis / Δ k = 1,    Δ t_body / Δ k = 3.
```

This is table interpolation, not a uniqueness claim about hop realizations.

## Theorem 2 — Unique Positive Reverse Crossing

Substitute the affine forms of Theorem 1 into equality in the reverse
comparison:

```text
3 (k+14)^2 = (3k+3)^2.
```

Expanding gives

```text
3(k^2 + 28k + 196) - (9k^2 + 18k + 9) = -6k^2 + 66k + 579 = 0,
```

or equivalently `2k^2 - 22k - 193 = 0`. The quadratic formula yields

```text
k = [22 ± sqrt(484 + 1544)] / 4 = [22 ± sqrt(2028)] / 4.
```

Because `2028 = 4 · 3 · 13^2`, one has `sqrt(2028)=26√3`, so

```text
k = [11 ± 13√3] / 2.
```

The minus branch is negative: `(11 - 13√3)/2 < 0`. The plus branch is the
unique positive root

```text
k_* = (11 + 13√3) / 2.
```

The same root is obtained from the positive-branch linearization
`√3(k+14)=3k+3`, which rearranges to

```text
k_* = (√3 · 14 - 3) / (3 - √3).
```

Rationalizing the latter by `3+√3` recovers `(11 + 13√3)/2` exactly.
Numerically, `k_* ≈ 16.7583`. In particular `k_* < 18.70`, so the displayed
s2 crossing is strictly earlier than the separately displayed c2d4 crossing
`k_* ≈ 18.70`. Direct integer arithmetic on the displayed rows therefore
gives

```text
k=13:  3 · 27^2 = 2187 > 42^2 = 1764,    reverse holds,
k=14:  3 · 28^2 = 2352 > 45^2 = 2025,    reverse holds,
k=18:  3 · 32^2 = 3072 < 57^2 = 3249,    reverse fails,
k=19:  3 · 33^2 = 3267 < 60^2 = 3600,    reverse fails.
```

The gapped row `k=7` also holds (`3 · 21^2 = 1323 > 24^2 = 576`), consistent
with `7 < k_*`. The displayed table does not contain `k=16` or `k=17`; the
crossing itself is the unique positive root of the affine equality, not a
displayed integer row.

## Theorem 3 — Locked-Slope Intercept Extras Cannot Restore All-k Reverse

Keep `(α,γ)=(1,3)` and replace the displayed intercepts by arbitrary finite
`(β,δ)`. Then

```text
3(k+β)^2 - (3k+δ)^2 = -6k^2 + 6(β-δ)k + (3β^2 - δ^2).
```

The quadratic coefficient in `k` is `-6`, independent of intercepts. Hence
the left-hand side is negative for all sufficiently large positive `k`, so
the reverse comparison fails for infinitely many integers `k>k_*`. In
particular, no intercept extra restores reverse for **all** integers `k>k_*`.

The displayed pair `(β,δ)=(14,3)` already fails at `k=18` and at `k=19`. An
intercept extra with a large positive axis intercept can postpone the first
failure past `k=19`, but it cannot postpone failure past every integer
larger than `k_*`. Example: `(β,δ)=(100,0)` still obeys reverse at `k=19`,
yet the same leading `-6k^2` forces failure at large `k`.

This obstruction is table algebra for locked slopes. It is not an
Admissibility rule and is not adopted.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| Lattice sentence naming `Z^3` | ambient context only | current minimal axioms |
| five displayed `(k, t_axis, t_body)` rows | computed lattice input | displayed, not adopted |
| reverse comparison `3 t_axis^2 > t_body^2` | declared predicate on the table | displayed, not adopted |
| `(α,γ)=(1,3)` | locked slopes of the displayed table | Theorem 1 |
| intercept extras `(β,δ)` | mutation family for Theorem 3 | declared; uniqueness not required |
| c2d4 crossing `k_* ≈ 18.70` | numeric comparator only | separately displayed; not an input table |

There are no measured, fitted, literature, or observational inputs. No path
search is performed. No new shortest-path algorithm is invoked. The displayed
integers are not identified with a graph-length functional. Admissibility is
not edited.

## No-Go Discipline Gate

The negative statement gated here is only:

> Any extra that keeps `(α,γ)=(1,3)` and only changes intercepts cannot
> restore the reverse comparison for all integers `k>k_*`.

It is not a no-go on other slope pairs, on adopting a different table, or on
later dynamics.

### N1 — Alternative routes

| Route | Status | Attempt and disposition |
|---|---|---|
| intercept-extraction route | ATTEMPTED | `t_axis-k` and `t_body-3k` are constantly `14` and `3` on all five rows, including `k=7`. |
| consecutive-slope route | ATTEMPTED | Every consecutive displayed pair, including the `k=7` to `k=13` gap, has `Δ t_axis/Δ k=1` and `Δ t_body/Δ k=3`. |
| quadratic-root route | ATTEMPTED | `3(k+14)^2=(3k+3)^2` has roots `(11±13√3)/2`, exactly one of which is positive. |
| integer-straddle route | ATTEMPTED | Direct evaluation shows reverse holds at `k=13` and `k=14` and fails at `k=18` and `k=19`. |
| locked-slope extra route | ATTEMPTED | For every finite `(β,δ)` the reverse polynomial has leading coefficient `-6`, so it is eventually negative. |

These are distinct interpolation, slope, radical, integer, and mutation
attacks. Each is closed by exact arithmetic on the displayed table or on the
locked-slope family; no prior negative result is used as authority.

### N2 — Wall independence

There is no multi-wall impossibility claim. The displayed table, the reverse
predicate, the locked slopes, and the all-`k>k_*` quantifier are one declared
comparison contract, not four independently claimed physical walls.

### N3 — Hidden-wall scan

The load-bearing conditions are explicit: the five displayed rows, the reverse
quadratic predicate, locked slopes `(1,3)`, finite intercept extras, and the
quantifier “all integers `k>k_*`”. No unspoken uniqueness of a hop
realization is used. No graph search, no named path witness, and no
Admissibility rewrite is used.

### N4 — Residual matching

No prior no-go, wall, or campaign is cited as a witness. The minimal-axiom
source supplies only the lattice sentence; it does not supply the table, the
affine forms, or the crossing. Those residuals are closed directly here, so
there is no borrowed residual to mismatch. The c2d4 decimal `18.70` is a
comparator for the inequality `k_* < 18.70`, not a proof ingredient of the
s2 root.

### N5 — Rhetoric audit

The runner and note resolve the following exact granularities:

```text
per_element: each displayed same-k row is checked against the affine forms and the reverse quadratic comparison
per_site: checked and not executed — no site-wise path search is performed
per_mode: checked and not executed — no spectral or harmonic mode is asserted
per_block: intercept extras with locked slopes (1,3) are checked as a family through the leading -6 k^2 coefficient
lattice_wide: checked and not executed — no lattice-wide search or path listing is claimed
```

The negative conclusion is per locked-slope intercept extra. It is not
upgraded to a lattice-wide dynamical statement or to an Admissibility edit.

### N6 — Partial-closure paths

No axiom edit is required for this table algebra: displaying the five rows and
locking the slopes closes it. A later theory may display a different table or
a different slope pair. Those are live construction paths, not forbidden
escapes and not premises of this theorem. FAIL / DO NOT SHIP for writing the
displayed forms into Admissibility, for claiming all-k reverse restoration by
intercept extras, or for treating uniqueness of a hop realization as a
hypothesis of Theorems 1–3.

### N7 — Steelman

The strongest counterargument is that a sufficiently large axis intercept can
push the extra’s own crossing far to the right of `k_*`, so reverse still
holds at `k=19`. That is true and is exhibited by `(β,δ)=(100,0)`. It does
not restore reverse for **all** integers `k>k_*`, which is the stated
quantifier. A second counterargument is that another slope pair could change
the leading coefficient. That is also true and is outside the claim: Theorem
3 locks `(α,γ)=(1,3)`.

### N8 — Cross-cycle echo

This is the first display of the affine-crossing theorem for the displayed
s2 same-k table. No previously retired wall is being revived. The note
imports no other science note as a proof ingredient. The earlier c2d4
crossing `k_* ≈ 18.70` is named only as a numeric comparator.

## Review Record

The durable content is the three table theorems above. Uniqueness of an
underlying hop realization is not required and is not claimed. The displayed
s2 same-k pairs remain displayed, not adopted.

## Primary Runner

The paired runner performs exact integer and radical checks of Theorems 1–3
on the displayed table only, including affine recovery of every row including
`k=7`, the unique positive crossing, the comparison `k_* < 18.70`, the
`k=18`/`k=19` reverse failures, locked-slope intercept extras,
source-boundary pins, and note/runner agreement. It writes no cache.
