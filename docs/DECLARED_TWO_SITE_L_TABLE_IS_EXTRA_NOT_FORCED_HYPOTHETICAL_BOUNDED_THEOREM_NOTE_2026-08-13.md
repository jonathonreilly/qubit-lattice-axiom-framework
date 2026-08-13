---
claim_id: declared_two_site_l_table_is_extra_not_forced_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a declared two-site window, two well-defined finite tables that jointly list (μ, o, K) disagree at μ and K. Current Admissibility names one fixed nearest-neighbor rule and leaves the distribution's form and values unspecified; it does not name either table. Granting that there is an L does not select the table. If a later owner adopted one displayed table as the referenced law, then μ, o, and K would be consequences of that one object, but that adoption is not made here. A friction-audit candidate C3 without a selected table is not cheaper than three extras. This note adopts no table, no L_phys, no r=1/2, and does not claim Born is derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/declared_two_site_l_table_is_extra_not_forced_hypothetical_2026_08_13.py
---

# Declared Two-Site L-Table Is Extra, Not Forced

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite algebra on two displayed two-site tables, plus
a textual non-selection reading of the current Admissibility wording.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/declared_two_site_l_table_is_extra_not_forced_hypothetical_2026_08_13.py`](../scripts/declared_two_site_l_table_is_extra_not_forced_hypothetical_2026_08_13.py)
**Parent on origin/main:** the current axiom memo only,
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

This is a hypothetical bounded theorem. It is not an `L_phys` adoption.
It is not a fifth extra named “compiler.” No axiom is edited.

## Result Up Front

A friction-audit candidate can ask whether one executable table that
jointly lists the site-conditional probability `μ`, the formation
occupancy `o`, and a declared projector grade `K` would be cheaper than
three separate extras. On a declared two-site window the answer is not
automatic.

Two finite tables `L0` and `L1` are displayed below. Both are
well-defined. They disagree at `μ` and at `K` (`1/3 ≠ 3/5`). Current
Admissibility names one fixed nearest-neighbor rule and does not specify
the distribution's form or values. It does not name `L0` versus `L1`.
Granting “there is an `L`” does not select the table.

If a later owner adopted `L0` as the referenced law, then `μ`, `o`, and
`K` would be consequences of that one object, and candidate C3 would be
cheaper than three extras. That adoption is not made here. Candidate C3
without a selected table is not cheaper than `H_extra`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two displayed finite tables are well-defined and disagree at exact Fraction entries; Admissibility is quoted as not selecting either table; no table is adopted and Born is not derived."
trace_class: negative_route_pruning
target_claim_id: declared_two_site_l_table_forced_by_admissibility
target_blocker_text: "does current Admissibility force one executable two-site table jointly listing (μ, o, K), making candidate C3 cheaper than three extras?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed L0/L1 tables and the quoted non-selection of the current axiom memo; adoption of any table remains open and is not made here"
hypothetical_axiom_status: "C3 counterfactual: Admissibility references one declared executable L-table; table not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let the window be `W={x,y}` and the finite menu be `{A,B}`. Write
`P_z=diag(1,0)` for the rank-one projector

```text
P_z = ((1, 0), (0, 0)).
```

A **declared executable L-table** on this window is a finite triple
`(μ, o, K)` with:

- occupancy `o=(o_x, o_y)` in `{0,1}^2`, read as which sites of `W` are
  formed (`1`) or unformed (`0`);
- for each formed site, a probability `μ` on `{A,B}`: nonnegative
  `Fraction` masses summing to `1`;
- a finite grade `K(P_z)` in `[0,1]` assigned to the declared projector.

The numerical match `K(P_z)=μ_x(A)` is a **declared identification** on
each displayed table. It is not a derivation of Born.

### Displayed table L0 (not adopted)

- `o=(1,0)` — only site `x` formed
- `μ_x(A)=1/3`, `μ_x(B)=2/3`
- `K(P_z)=1/3`

### Displayed table L1 (not adopted)

- `o=(1,0)` — same occupancy
- `μ_x(A)=3/5`, `μ_x(B)=2/5`
- `K(P_z)=3/5`

The runner identity gates are the accessors `L0_muA()` and `L1_muA()`.
They return the declared `μ_x(A)` entries of `L0` and `L1`.

## Theorem 1

`L0` and `L1` are both well-defined finite tables: each occupancy is a
`{0,1}` pair, each formed-site `μ` is a two-outcome probability, `P_z`
is the declared projector, and each `K(P_z)` lies in `[0,1]`.

They disagree at `μ` and at `K`:

```text
L0_muA() = 1/3
L1_muA() = 3/5
1/3 ≠ 3/5
K_0(P_z) ≠ K_1(P_z)
```

The predicate `L0=L1` therefore fails.

## Theorem 2

Quote the current Admissibility wording. The axiom memo states that
there is one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations, and that for each site
the probability distribution over the possibilities is determined by,
and varies with, the nearest-neighbor conditions. The same memo states
that the distribution's extensional form and values are not specified
by this memo, and that the remaining formation rules (the
distribution's form and values, at which site, and at what rate) remain
outside axiom content.

That wording names one fixed nearest-neighbor rule. It does not name
`L0` versus `L1`. Granting “there is an `L`” does not select the table.

The predicate “axiom memo names `L0`” therefore fails.

## Theorem 3

*If* a later owner adopted `L0` as the referenced law, then `μ`, `o`,
and `K` would be consequences of that one object. Candidate C3 would
then be cheaper than three extras (`H_extra`).

That adoption is not made here. Candidate C3 without a selected table
is not cheaper than `H_extra`. The counterfactual cheapness is
conditional on a later selected table; the current axiom memo does not
perform that selection.

## Theorem 4

This note does not adopt `L0` or `L1`. It does not adopt `L_phys`. It
does not force `r=1/2`. It does not claim Born is derived. The displayed
`K(P_z)=μ_x(A)` match remains a declared identification on each table,
not a physical readout theorem.

## Scope And Non-Claims

- The window, menu, occupancy pair, and both tables are declared
  finite objects of this note. They are not lattice-wide laws.
- No observational number is imported.
- No unmerged pull request is cited. No other theorem note is a parent.
- No axiom sentence is edited or proposed for edit.
- No compiler extra is added to the primitive roster.

## Exact Target And Obligation Graph

**Exact target.** Decide whether current Admissibility already forces
one executable two-site table jointly listing `(μ, o, K)`, so that
friction-audit candidate C3 is cheaper than three extras without a
later owner selecting the table.

| Obligation | Role | Disposition |
|---|---|---|
| exhibit two well-defined finite tables | Theorem 1 | proved: `L0` and `L1` |
| show they disagree at `μ` and `K` | Theorem 1 | proved: `1/3 ≠ 3/5` |
| quote Admissibility as one fixed rule with form and values unspecified | Theorem 2 | quoted from the current axiom memo |
| show the memo does not name `L0` versus `L1` | Theorem 2 | proved by absence |
| record the counterfactual cheapness if `L0` were adopted | Theorem 3 | stated; adoption not made |
| refuse table, `L_phys`, `r=1/2`, and Born-derivation claims | Theorem 4 | explicit non-adoption |

The strongest missing lemma, if candidate C3 is to become cheaper than
`H_extra`, is a later owner-selected referenced law that picks one
executable table. That lemma is not supplied here.
