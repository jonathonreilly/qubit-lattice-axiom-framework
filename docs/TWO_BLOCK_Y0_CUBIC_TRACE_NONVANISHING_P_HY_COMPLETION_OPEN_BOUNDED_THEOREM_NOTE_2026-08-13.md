---
claim_id: two_block_y0_cubic_trace_nonvanishing_p_hy_completion_open_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the eight-component two-block line Y(t)=t Y_0 the cubic trace equals -48 t^3 and vanishes only at t=0; May 1 closed SU(2)^2 Y and left Y^3 open; matching Y_like or a PDG table is extra; a later completion remains open and is not adopted."
upstream_dependencies:
  - minimal_axioms
  - lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02
  - hypercharge_identification
  - physical_hypercharge_alpha_scale_freedom_cycle692
  - lh_doublet_su2_squared_hypercharge_anomaly_cancellation_note_2026-05-01
runner: scripts/two_block_y0_cubic_trace_nonvanishing_p_hy_completion_open_2026_08_13.py
---

# Two-Block Y_0 Cubic Trace Is Nonvanishing; Physical-Hypercharge Completion Remains Open

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact cubic trace of the two-block line `Y(t)=t Y_0` on `C^8`;
the May 1 `Y^3` residual on these eight components; scale conventions
`t=1`, `t=1/3`, and `t=1/6`; P-HY completion left open.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_block_y0_cubic_trace_nonvanishing_p_hy_completion_open_2026_08_13.py`](../scripts/two_block_y0_cubic_trace_nonvanishing_p_hy_completion_open_2026_08_13.py)

## Result Up Front

[`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
already forces the two-block ratio from ranks `(6,2)`:

```text
6 α + 2 β = 0  ⇒  β = -3 α.
```

That note is a structural ratio result. It explicitly does not identify
with Y. [`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)
writes the un-normalized generator as

```text
Y_0 = P_sym - 3 P_anti
```

on the same ranks, equivalently `Y_0 = Pi_+ - 3 Pi_-` in complementary-projector
notation. Cycle 692,
[`PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md`](PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md),
records that tracelessness fixes the ratio and nothing else: the
normalized `(+1/3,-1)` pattern depends on an explicitly supplied
`alpha=1/3` scale, which is not derived.

[`LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION_NOTE_2026-05-01.md`](LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION_NOTE_2026-05-01.md)
closed the `SU(2)^2 × Y` identity on the left-handed doublet and left the
cubic open. Its scoped sentence is

> the remaining anomaly identities (SU(3)² × Y, gravitational × Y, Y³)
> are scoped explicitly to the parent and are **not** derived in this note.

The same note names the residual

> (R-B) U(1)_Y³ anomaly: requires `Σ Y³ = 0` over all LH fermions.
> Requires the full one-generation matter content.

May 1 therefore closed a mixed nonabelian identity and scoped `Y^3` out.
This note computes that scoped residual on the eight-component two-block
line and nothing else.

On `C^8` write `Y(t) := t Y_0 = t (Pi_+ - 3 Pi_-)` for `t` in `Q`. The
spectrum is `{+t x6, -3t x2}`. The cubic trace is

```text
Tr(Y(t)^3) = 6 (t)^3 + 2 (-3t)^3 = 6 t^3 - 54 t^3 = -48 t^3.
```

Three conventional specializations, not derivations, are

```text
6(1)^3 + 2(-3)^3 = 6-54 = -48
6(1/3)^3 + 2(-1)^3 = 2/9 - 2 = -16/9
6(1/6)^3 + 2(-1/2)^3 = 1/36 - 1/4 = -2/9
```

The value `-48 t^3` vanishes if and only if `t=0`. The zero operator is
not a hypercharge. No nonzero two-block scale is cubic-anomaly-free on
these eight components alone. Matching a named table (`Y_like` at `t=1/3`,
or PDG-like `Q=T_3+Y` numbers `{1/6 x6, -1/2 x2}` at `t=1/6`) is a scale
convention plus a species map. Axioms do not select `t`. This note does
not identify `Y_like` with `U(1)_Y`. Additional fields can cancel a
cubic; that completion is not adopted. P-HY remains open. No axiom is
edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Tr(Y(t)^3)=-48 t^3 on the eight-component two-block line and is nonzero for every nonzero rational t. A named scale is extra. A completion remains open."
trace_class: frontier_discovery
target_claim_id: p_hy_identification
target_blocker_text: "identify the two-block traceless line with anomaly-complete physical hypercharge"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The 8-component cubic is nonzero at every nonzero scale. A completion remains open. Do not identify Y_like with U(1)_Y. Do not adopt axiom text."
conditional_surface_status: "exact for the cubic formula and the never-zero residual on these 8 components; P-HY completion open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on `C^8` with complementary orthogonal projectors of ranks `6` and
`2`, written `Pi_+` and `Pi_-`. These are the two-block projectors of the
May 2 ratio surface and of the name-free generator `Y_0`. In an eigenbasis
they are the diagonal cuts

```text
Pi_+ = diag(1,1,1,1,1,1,0,0),
Pi_- = diag(0,0,0,0,0,0,1,1).
```

The un-normalized generator and its rational scale line are

```text
Y_0 := Pi_+ - 3 Pi_-,
Y(t) := t Y_0 = t Pi_+ - 3t Pi_-,    t in Q.
```

The spectrum of `Y(t)` is `{+t` with multiplicity `6`, `-3t` with
multiplicity `2}`. The linear trace is the May 2 identity

```text
Tr Y(t) = 6t + 2(-3t) = 0.
```

The cubic trace is the new object:

```text
Tr(Y(t)^3) = 6 t^3 + 2 (-3t)^3 = -48 t^3.
```

Three named points on the line, kept as conventions, are

| label | `t` | spectrum | `Tr(Y(t)^3)` |
|---|---|---|---|
| un-normalized `Y_0` | `1` | `{+1 x6, -3 x2}` | `-48` |
| `Y_like` | `1/3` | `{+1/3 x6, -1 x2}` | `-16/9` |
| PDG-like `Q=T_3+Y` numbers | `1/6` | `{+1/6 x6, -1/2 x2}` | `-2/9` |

`Y_like` is the conventional scale already displayed as
`(1/3) Pi_+ - Pi_-`. The PDG-like row is the same line at the numbers
that appear in the `Q=T_3+Y` table for a left-handed doublet pair. Neither
row is a derived unit, and neither row is an identification with
`U(1)_Y`.

The identity-gate function of the runner is `cubic_trace(t)`, equal to
`-48 t^3` for every rational `t`.

## Exact Target And Obligation Graph

**Exact target.** Evaluate `Tr(Y(t)^3)` on the eight-component two-block
line, record that it vanishes only at `t=0`, and record that May 1 left
this cubic open. Do not identify a named scale with `U(1)_Y`, and do not
adopt a completion.

| Obligation | Role | Disposition |
|---|---|---|
| pin May 2 ratio `6α+2β=0 ⇒ β=-3α` and the non-identification with Y | premise | quoted; linear trace recomputed |
| pin name-free `Y_0 = P_sym - 3 P_anti` | premise | cited as the un-normalized generator |
| pin cycle 692: tracelessness does not fix the scale | premise | quoted; `α=1/3` not derived |
| pin May 1 `Y^3` scoped-out sentence | premise | quoted; mixed `SU(2)^2 Y` is not this residual |
| evaluate `Tr(Y(t)^3)=-48 t^3` | Theorem 1 | spectrum cubes; three specializations |
| show the cubic vanishes iff `t=0` | Theorem 2 | `-48 t^3=0` over `Q` |
| record that May 1 left `Y^3` open | Theorem 3 | scoped residual on these 8 components |
| refuse identification of a named table with `U(1)_Y` | Theorem 4 | scale extra; cubic nonzero |
| keep a later completion open and unadopted | Theorem 5 | named escape, not used |
| edit an axiom, or derive `α=1/3` | non-claim | not attempted |

## Theorem 1 — Cubic Formula

**Claim.** For every rational `t`,

```text
Tr(Y(t)^3) = -48 t^3.
```

The three conventional specializations are `-48`, `-16/9`, and `-2/9`.

**Proof.** `Y(t)` is diagonalizable with eigenvalues `t` (multiplicity
`6`) and `-3t` (multiplicity `2`). The cubic trace is the sum of cubed
eigenvalues:

```text
Tr(Y(t)^3) = 6 t^3 + 2 (-3t)^3
           = 6 t^3 + 2 (-27 t^3)
           = 6 t^3 - 54 t^3
           = -48 t^3.
```

The same number is the matrix trace of the cube of
`diag(t,t,t,t,t,t,-3t,-3t)`. Substituting the three conventional scales:

```text
t=1:     6(1)^3 + 2(-3)^3 = 6-54 = -48,
t=1/3:   6(1/3)^3 + 2(-1)^3 = 6/27 - 2 = 2/9 - 2 = -16/9,
t=1/6:   6(1/6)^3 + 2(-1/2)^3 = 6/216 - 2/8 = 1/36 - 1/4 = -2/9.
```

The linear trace `6t+2(-3t)=0` is the May 2 ratio restated at scale `t`.
It does not evaluate the cubes. The cubic formula is not a restatement of
that ratio.

## Theorem 2 — Never Zero On The Nonzero Line

**Claim.** `Tr(Y(t)^3)=0` if and only if `t=0`. The zero operator is not
a hypercharge. Therefore no nonzero two-block scale is
cubic-anomaly-free on these eight components alone.

**Proof.** Over `Q` the monomial `-48 t^3` vanishes exactly at `t=0`.
At every nonzero sample, including `t=1`, `t=1/3`, `t=1/6`, `t=-2`, and
`t=5/7`, the identity-gate value `cubic_trace(t)` is the nonzero rational
`-48 t^3`.

The operator `Y(0)` is the zero endomorphism of `C^8`. A hypercharge
generator on this surface is a nonzero traceless two-block operator, i.e.
a nonzero point of the May 2 line. The only cubic-vanishing point of that
line is the origin, which is excluded. Hence every live two-block scale
has a nonzero eight-component cubic.

A predicate that some nonzero rational `t` has vanishing cubic on these
eight components contradicts the identity `-48 t^3=0 ⇔ t=0`.

## Theorem 3 — May 1 Scope

**Claim.** May 1 closed `SU(2)^2 × Y` for the left-handed doublet and
left `Y^3` open. This note addresses that scoped residual on the
two-block surface only.

**Proof.** The May 1 theorem is the mixed identity

```text
A_{SU(2)^2 Y, LH doublets} = T(2) · (3 · (+1/3) + 1 · (-1)) = 0.
```

That is a weighted linear sum, the same arithmetic as tracelessness
after the Dynkin index is factored out. The May 1 exclusions name the
cubic separately: `Y³` is scoped to the parent one-generation surface
and is not derived there. The `(R-B)` residual requires `Σ Y³ = 0` over
all left-handed fermions and the full one-generation matter content.

The eight-component operator `Y(t)` is exactly the two-block line whose
linear trace entered May 1. Its cubic was not evaluated there. Theorem 1
is that evaluation. The result is a statement about these eight
components. It is not a one-generation cancellation, not a mixed
`SU(3)^2 Y` identity, and not a gravitational mixed identity.

## Theorem 4 — Identification Is Extra

**Claim.** Matching a named table (`Y_like` or PDG-like `Y`) is a scale
convention plus a species map. Axioms do not select `t`. Cycle 692
already records that `α=1/3` is not derived. This note does not identify
with Y. This note does not identify `Y_like` with `U(1)_Y`.

**Proof.** The May 2 line is one-dimensional. Every point is
`Y(t)=t Y_0`. The three rows of the specialization table are three
points of that line. Selecting `t=1/3` makes the minus-block eigenvalue
`-1` and recovers the displayed `Y_like` spectrum `{+1/3 x6, -1 x2}`.
Selecting `t=1/6` recovers the `Q=T_3+Y` numbers `{+1/6 x6, -1/2 x2}`.
Each selection is a choice of unit on an already one-dimensional line,
together with a map that would send the plus block and the minus block
to named species. Neither the unit nor the map is forced by
tracelessness.

Cycle 692 states the same split at the scale: tracelessness fixes the
ratio and nothing else, and the normalized `(+1/3,-1)` result depends on
an explicitly supplied `alpha=1/3`. The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) names
Lattice, Qubit, Admissibility, and Record. Those sentences do not name
`Y(t)`, `Y_like`, `U(1)_Y`, or a cubic anomaly, and they do not select
`t`.

Even if a scale were chosen, Theorem 2 would still apply. At the
`Y_like` point one has `cubic_trace(1/3)=-16/9 ≠ 0`. At the PDG-like
point one has `cubic_trace(1/6)=-2/9 ≠ 0`. A nonzero eight-component
cubic is not an anomaly-complete `U(1)_Y` generator on these components
alone. Treating “`Y_like` is `U(1)_Y`” as a theorem therefore fails for
two independent reasons: the scale is extra, and the cubic is nonzero.

## Theorem 5 — Completion Remains Open

**Claim.** Additional fields (for example right-handed singlets) can
cancel a cubic. This note does not forbid a later completion and does
not adopt one. P-HY remains open. No axiom is edited. Extra fields are
a named escape.

**Proof.** Theorem 2 is a statement about these eight components. It
does not quantify over a larger fermion content. If further fields with
charges `y_i` are supplied, the total cubic is

```text
-48 t^3 + Σ_i y_i^3,
```

and that sum can vanish for a suitable list `(y_i)`. A standard named
escape is a right-handed singlet completion. Naming the escape is not
adopting the fields, not selecting their charges, and not identifying
the two-block line with anomaly-complete physical hypercharge.

The current axiom sentences do not name those fields. An axiom edit
that installed a completion, or that named `Y_like` as `U(1)_Y`, is not
required by the cubic formula. Theorems 1 and 2 remain true whether or
not a later note supplies extra fields.

The residual is therefore a P-HY stretch, not an identification: the
eight-component cubic is nonzero at every nonzero scale, and a
completion that would cancel it is still open.

## Boundary And Non-Claims

The note does not:

- identify `Y_like` or `Y(t)` with anomaly-complete `U(1)_Y`;
- derive `α=1/3`, or treat `t=1/3` or `t=1/6` as a selected unit;
- adopt right-handed singlets or any other extra fields;
- evaluate mixed `SU(3)^2 Y` or gravitational mixed traces;
- close a one-generation or three-generation anomaly table;
- edit an axiom, or argue that an axiom update is necessary;
- claim that a later completion is impossible.

The exact advance is the cubic formula on the eight-component two-block
line, the never-zero residual, and the scoped statement that May 1 left
this cubic open.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| May 2 ratio `1:(-3)` and non-identification with Y | premise | quoted; linear trace recomputed |
| name-free `Y_0` generator | premise | cited; same two-block line |
| cycle 692 scale freedom | premise | quoted; `α=1/3` not derived |
| May 1 `SU(2)^2 Y` identity and `Y^3` exclusion | sibling scope pin | quoted; cubic not evaluated there |
| current axiom memo | scanned wording | no `Y_like`, no cubic, no `t` |
| `Tr(Y(t)^3)=-48 t^3` and the three specializations | Theorem 1 | computed here |
| never-zero residual on these 8 components | Theorem 2 | computed here |
| identification of a named table with `U(1)_Y` | extra | refused |
| right-handed or other extra fields | named escape | not adopted |
| P-HY / anomaly-complete physical hypercharge | target identification | open |

The exact advance is a finite cubic-trace theorem on `C^8`. Independent
audit remains required before any effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | May 1 closed `SU(2)^2 Y` and scoped `Y^3` out. Cycle 692 records that `α=1/3` is not derived. This note evaluates the scoped eight-component cubic and keeps the scale a convention. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for two-block `Y_0` cubic nonvanishing and `Tr(Y_0^3)`. May 1 is the `SU(2)^2 Y` identity and scopes `Y^3` out. The June 18 ABJ scale-free core writes `Tr[Y_a^3]=-48 a^3` as ABJ arithmetic and then exhibits a four-charge completion witness; that witness is extra fields, not a parent of this residual. Historic intake wraps an unlanded May 30 theorem and is not a parent. No landed note addresses the May 1 scoped residual on the eight-component two-block line as a P-HY stretch that keeps completion open and records the specializations `-48`, `-16/9`, `-2/9`. |
| V3 | Independently checkable? | Textbook one-generation cubic traces sum `Y^3` over a completed fermion list and do not mention Record, the two-block generator `Y_0`, or the May 1 scoped residual. The runner recomputes `cubic_trace(t)` from the `C^8` operator in exact rationals. |
| V4 | More than a restatement? | Yes. The identity `6(1)^3+2(-3)^3=-48` and the specializations `-16/9`, `-2/9`, together with `Tr(Y(t)^3)=0 ⇔ t=0`, are not restatements of the May 2 ratio sentence or of the May 1 mixed identity. |
| V5 | One-step relabel? | No. May 2 is a linear ratio. A ratio is not a cubic. Evaluating cubes, proving they never vanish on the nonzero line, and leaving a completion open is not a corollary of `β=-3α`. |

## No-Go Discipline Gate (Theorems 4–5)

The negative claims are only these: a named scale is not a derived
identification with `U(1)_Y`, and a later completion is not adopted.
The gate does not ship a global non-existence theorem against extra
fields, and it does not ship physical hypercharge.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| force `t=1/3` | set the minus-block eigenvalue to `-1` and call the result `U(1)_Y` | Theorem 4: the unit is extra; `cubic_trace(1/3)=-16/9 ≠ 0` | **ATTEMPTED** |
| force `t=1/6` | read PDG-like `Q=T_3+Y` numbers `{1/6 x6, -1/2 x2}` as a derived generator | Theorem 4: another point of the same line; `cubic_trace(1/6)=-2/9 ≠ 0` | **ATTEMPTED** |
| claim the cubic vanishes | assert some nonzero `t` has `Tr(Y(t)^3)=0` on these 8 components | Theorem 2: `-48 t^3=0` only at `t=0` | **ATTEMPTED** |
| identify `Y_like` with `U(1)_Y` | treat the conventional scale as anomaly-complete physical hypercharge | Theorems 2 and 4: scale extra; cubic nonzero | **ATTEMPTED** |
| axiom edit | add a sentence naming `Y_like` as `U(1)_Y` or installing extra fields | not required by the cubic formula; see N6 | **ATTEMPTED** |
| right-handed completion | add singlets so that `-48 t^3 + Σ y_i^3 = 0` | named escape; extra fields; not adopted | **ATTEMPTED** (escape) |

### N2 — wall independence

Theorem 4 closes only the claim that a named point of the May 2 line is
already `U(1)_Y`. Theorem 5 closes only the claim that this note adopts
a completion. The cubic formula (Theorem 1), the never-zero residual
(Theorem 2), the May 1 scope pin (Theorem 3), mixed `SU(3)^2 Y`, and a
later extra-field construction remain independent walls. Nonvanishing
on eight components does not by itself forbid a larger content, and a
larger content would not make `t=1/3` a theorem of the axioms.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| ranks `(6,2)` and `Y_0` | declared May 2 / name-free objects |
| scale line `Y(t)=t Y_0` | explicit one-parameter family |
| `cubic_trace(t)=-48 t^3` | explicit identity-gate output |
| specializations `-48`, `-16/9`, `-2/9` | explicit conventional witnesses |
| May 1 `Y^3` exclusion | quoted sibling scope |
| cycle 692 underived `α=1/3` | quoted scale obstruction |
| axiom edit naming `Y_like` | live governance path; not required |
| right-handed or other extra fields | named escape; not assumed |
| P-HY identification | open; not assumed |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md) | ratio `1:(-3)`; does not identify with Y | linear premise only; cubes not evaluated |
| [`docs/HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md) | `Y_0 = P_sym - 3 P_anti` | un-normalized generator; no cubic |
| [`docs/PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md`](PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md) | tracelessness does not fix `α=1/3` | scale pin only; not reversed |
| [`docs/LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION_NOTE_2026-05-01.md`](LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION_NOTE_2026-05-01.md) | `Y^3` scoped out after `SU(2)^2 Y` | sibling residual; cubic computed here |
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice, Qubit, Admissibility, Record | no `t`, no `Y_like`, no cubic |

No unmerged note is used as a parent. The three specializations are
recomputed here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | eight eigenvalues of `Y(t)` and the specializations `-48`, `-16/9`, `-2/9` | no classification of every operator on `C^8` |
| per site | one `C^8` two-block carrier | no composite generation or lattice source field |
| per mode | the cubic trace of the two-block line | no mixed `SU(3)^2 Y` or gravitational mode |
| per split | Theorems 4–5 on identification and completion | no axiom edit and no adopted extra fields |
| lattice-wide | checked and not executed | no lattice-wide hypercharge law |

The residual is an eight-component cubic. It is not lattice-wide.

### N6 — live partial-closure paths

1. Force `t=1/3` by an independent dimensionless selector. Cycle 692
   already records that the tested mechanisms do not supply one. This
   note does not add that selector.
2. Force `t=1/6` by reading a `Q=T_3+Y` table into the two-block line.
   That remains a species map plus a unit, not a theorem of ranks
   `(6,2)`.
3. Supply extra fields, for example right-handed singlets, whose cubed
   charges cancel `-48 t^3`. That is the named escape. It is not
   adopted here.
4. An owner-approved typed axiom addition that named `Y_like` as
   `U(1)_Y` or that installed a completion. The cubic formula does not
   require that addition.

The quoted axiom sentences already name Lattice, Qubit, Admissibility,
and Record. They do not name `Y(t)` or a completion. No axiom sentence
is required by Theorems 4 and 5.

### N7 — hostile steelman

> The cubic is the elementary sum `6t^3+2(-3t)^3`, so May 2 already
> knew it. Choosing `t` so that some other convention holds, or adding
> the usual singlets, makes the cubic a non-obstruction. Therefore
> `Y_like` is `U(1)_Y`.

**Answer.** May 2 evaluates a linear combination, not cubes. Theorem 1
is that evaluation, and Theorem 2 is that the cubes never vanish on the
nonzero line. The eight-component values at `t=1/3` and `t=1/6` are
`-16/9` and `-2/9`, not `0`. Extra fields can cancel those numbers;
that is Theorem 5's named escape, and it is not a theorem that the
eight-component operator is already anomaly-complete `U(1)_Y`. Scale
choice plus a species map is exactly the extra identification Theorems
4 and 5 refuse.

### N8 — cross-cycle echo

May 1 already removed `Y^3` from its load-bearing claim. Cycle 692
already removed `α=1/3` from the ratio surface. The present cubic
theorem does not reverse those exclusions. It answers a different
question: on the eight-component two-block line the cubic is `-48 t^3`,
never zero for `t≠0`; among named tables, that cubic is still not
`U(1)_Y`; among possible extra fields, a completion remains open.

**Gate disposition.** PASS for the cubic formula, the never-zero
residual, and the scoped statements that identification is extra and
that a completion remains open. FAIL / DO NOT SHIP for "`Y_like` is
`U(1)_Y`," "`α=1/3` is derived," "the eight-component cubic vanishes,"
or "an axiom edit is required."

## Primary Runner

[`scripts/two_block_y0_cubic_trace_nonvanishing_p_hy_completion_open_2026_08_13.py`](../scripts/two_block_y0_cubic_trace_nonvanishing_p_hy_completion_open_2026_08_13.py)
reconstructs `Y(t)` on `C^8`, evaluates `cubic_trace(t)` as the matrix
trace of `Y(t)^3` in exact rationals, checks the closed form `-48 t^3`,
recomputes the specializations `-48`, `-16/9`, and `-2/9`, and checks
that the cubic vanishes only at `t=0`. Identity gates call
`cubic_trace(t)`. Replacing `cubic_trace` by `0` must fail at `t=1` and
at `t=1/3`. A predicate that some nonzero `t` has vanishing cubic on
these eight components must fail Theorem 2. Identifying `Y_like` with
`U(1)_Y` as a theorem must fail: the scale is extra and the cubic is
nonzero. No runner cache is written.
