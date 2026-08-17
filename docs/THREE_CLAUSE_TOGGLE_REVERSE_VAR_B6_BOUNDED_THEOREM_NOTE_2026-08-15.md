---
claim_id: three_clause_toggle_reverse_var_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among 8 named three-clause toggles on B_6(0), reversers and the lex-first variance-minimizing reverser are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_clause_toggle_reverse_var_b6_2026_08_15.py
---

# Named Three-Clause Toggles: Reverse Versus Variance On `B_6(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** eight named nearest-neighbor hop-cost rules on the finite ball
`B_6(0)`, obtained by independently enabling the three clauses of the
already-named support-drop cost. Arrival times, the reverse bit, and the
population variance of `|v|_2/t` are scored. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_clause_toggle_reverse_var_b6_2026_08_15.py`](../scripts/three_clause_toggle_reverse_var_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `B_6(0)` for the closed `ℓ¹` ball of radius `6` in `Z^3`. That set
has `377` sites, of which `376` are nonzero. The graph is the induced
six-neighbor graph. A hop `v → w` carries inward weights
`(|σ_v|, |σ_w|)`, where `|σ_u|` is the number of nonzero coordinates of
`u` relative to the seed `0`.

A clause triple `(s,a,d) ∈ {0,1}^3` names the rule that costs `3` if

- `s` is on and the hop is a seed-exit (`|σ_v| = 0`), or
- `a` is on and both weights are `1` (`|σ_v| = |σ_w| = 1`), or
- `d` is on and the hop is a support drop (`|σ_w| < |σ_v|`),

and costs `1` otherwise. The already-named support-drop cost is the full
triple `ν = (1,1,1)`. Disabling a clause replaces that clause's cost-`3`
hits by cost `1`. The zero triple is the unit-cost law: every hop costs
`1`, so first arrival is `t(v) = |v|_1`.

Eight Dijkstras, one per triple, give first-arrival times from `0`. A
triple *reverses* when

```text
12 t(4,0,0)^2 > 16 t(2,2,2)^2.
```

**Theorem 1.** `N_rev = 2`. The reversing triples and their
`(t_axis, t_diag) = (t(4,0,0), t(2,2,2))` are

```text
(0,1,1) : (t_axis, t_diag) = (8, 6)
(1,1,1) : (t_axis, t_diag) = (10, 8)
```

**Theorem 2.** Among those reversers, the lex-first minimizer of the
population variance of `|v|_2/t` on `B_6(0) \ {0}` is `ν = (1,1,1)`, with

```text
var(|v|_2/t) = 0.005905639029
ℓ¹ var(|v|_2/t) = 0.013502037619
```

The other reverser `(0,1,1)` has variance `0.010622504917`. Uniqueness of
the minimizer is observed on this eight-row census and is not required by
the claim.

**Theorem 3.** Displayed, not adopted. Do not write any triple into
Admissibility. Do not attach L1.

The census is not leftover of `ν` alone: both reversing rows and the
variance order are properties of the eight named toggles together.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite eight-rule Dijkstra census on B_6(0) reports reversers and the lex-first variance-minimizing reverser. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: three_clause_toggle_reverse_var_b6
target_blocker_text: "whether independently enabling the three nu clauses on B_6(0) yields reversers other than nu, and which reverser minimizes var(|v|_2/t)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the eight named toggles and the 377-site ball B_6(0); no hop-cost is written into Admissibility"
hypothetical_axiom_status: "none; every clause triple is displayed rule data and is not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies `Z^3` with
  nearest-neighbor adjacency. The live Admissibility sentence supplies one
  fixed nearest-neighbor rule and is quoted without rewrite; no clause
  triple is substituted for that rule. The live Record unread sentence is
  quoted without rewrite.
- **Explicit theorem-domain condition:** the finite ball `B_6(0)`, the
  six-neighbor graph it induces, the three named clauses, and the eight
  independent on/off assignments are supplied mathematical data for this
  theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a hop-cost by Admissibility or
  Record, any identification of `t` with a physical clock, and any
  attachment of the unit-cost comparison law remain separate, open
  obligations outside the target proved here.

## Exact Objects

Sites are points of `Z^3`. The ball is

```text
B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }.
```

It contains `377` sites. Edges are the six axis steps that remain inside
the ball. For a site `u = (x,y,z)`, the support size is

```text
|σ_u| = 1_{x ≠ 0} + 1_{y ≠ 0} + 1_{z ≠ 0}.
```

The three clauses on a directed hop `v → w` are mutually exclusive:

1. seed-exit: `|σ_v| = 0`;
2. both-weights-1: `|σ_v| = |σ_w| = 1`;
3. support-drop: `|σ_w| < |σ_v|`.

A disabled clause does not fire, so those hops cost `1`. Enabled clauses
cost `3`. First arrival `t(v)` is the Dijkstra distance from `0` in
nonnegative integer hop-costs. The origin is excluded from the variance
sample because `|v|_2/t` is undefined at `t(0) = 0`.

Population variance on the `376` nonzero sites is

```text
var = (1/376) Σ_v (|v|_2/t(v) − mean)^2,
mean = (1/376) Σ_v |v|_2/t(v).
```

The comparison law called `ℓ¹` in Theorem 2 is the zero triple: every hop
costs `1` and `t(v) = |v|_1`. It is a scored row, not an attached law.
Lex order on triples is the dictionary order on `(s,a,d)` with each bit
in `{0,1}`.

## Exact Target And Proof Obligations

The exact target is the eight-row census: which triples reverse, and
which reversing triple is the lex-first minimizer of `var(|v|_2/t)`.

The obligation graph is:

1. enumerate `{0,1}^3` and run one Dijkstra per triple on `B_6(0)`;
2. evaluate the integer reverse test at `(4,0,0)` and `(2,2,2)`;
3. evaluate the population variance on the same `376` nonzero sites;
4. among reversers, take the minimum variance and, on a tie, the
   lex-first triple;
5. keep every triple displayed and outside Admissibility.

All five obligations are closed below and in the runner. Larger balls,
other hop-cost families, and any axiom edit are outside this theorem.

## Theorem 1 — `N_rev` among the eight triples

The eight arrivals at the two probe sites are

```text
(s,a,d)   t(4,0,0)  t(2,2,2)  12 t_axis^2  16 t_diag^2  reverse
(0,0,0)        4         6         192          576      no
(0,0,1)        4         6         192          576      no
(0,1,0)        6         6         432          576      no
(0,1,1)        8         6         768          576      yes
(1,0,0)        6         8         432         1024      no
(1,0,1)        6         8         432         1024      no
(1,1,0)        8         8         768         1024      no
(1,1,1)       10         8        1200         1024      yes
```

Hence `N_rev = 2`. The reversing triples are `(0,1,1)` with
`(t_axis, t_diag) = (8, 6)` and `(1,1,1)` with
`(t_axis, t_diag) = (10, 8)`.

The second reverser is `ν`. The first is `ν` with seed-exit disabled:
axis extensions and support drops remain expensive, but leaving the seed
costs `1`. That already reverses the diamond test, so reverse on this
ball is not leftover of `ν` alone.

The axis-skeleton triple `(1,1,0)` (seed-exit and both-weights-1, support
drop cheap) gives `t(4,0,0) = t(2,2,2) = 8` and does not reverse: cheap
return-to-axis hops undercut the expensive 1-skeleton, which is why the
support-drop clause is present in `ν`.

## Theorem 2 — lex-first variance-minimizing reverser

On the same `376` nonzero sites the two reversers have

```text
(0,1,1) : var(|v|_2/t) = 0.010622504917
(1,1,1) : var(|v|_2/t) = 0.005905639029
```

The unique minimum is `ν = (1,1,1)`. Lex order is not required to break
a tie on this census; it is the stated tie-break and would select `ν`
if the two variances were equal.

The unit-cost comparison value on the same sample is

```text
ℓ¹ var(|v|_2/t) = 0.013502037619
```

Both reversers beat that comparison value. The smaller variance is still
the `ν` row. No uniqueness claim is made for hop-costs outside the eight
named toggles.

## Theorem 3 — displayed, not adopted

Every triple, including `ν` and the unit-cost comparison row, is displayed
rule data on `B_6(0)`. Do not write any triple into Admissibility. Do not
attach L1. No additional axiom is proposed.

The live Admissibility sentence remains the one fixed nearest-neighbor
rule already on the axiom memo. This note does not replace that sentence
by a hop-cost, a clause triple, or a variance selector.

## Physical-Interpretation Boundary

The proved output is the eight-row reverse-and-variance census. This note
neither assigns a physical clock to `t` nor changes the Admissibility
sentence. Each clause triple is displayed hop-cost data, not axiom
content, and no additional axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. the axis-skeleton triple `(1,1,0)` has `t_axis = t_diag = 8` and fails
   the strict reverse test, so reverse is not automatic for every
   expensive 1-skeleton;
2. the other reverser `(0,1,1)` has a strictly larger variance than `ν`,
   so the variance minimizer is not “any reverser”;
3. the unit-cost row is not a reverser, so the comparison `ℓ¹` variance
   is not a reverse witness.

## What This Does Not Claim

- No clause triple is claimed to be the Admissibility rule.
- The unit-cost comparison is not attached as a preferred law.
- Uniqueness of `ν` among hop-costs outside these eight toggles is not
  claimed.
- Arrival times off `B_6(0)` are not scored.
- `t` is not identified with a physical clock, a Record readout, or a
  time metric.
- Independent class leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's lattice adjacency
vocabulary, the existence of one fixed nearest-neighbor rule, and the
unread sentence. This theorem separately supplies the eight named
toggles and the finite-ball census; writing a triple into Admissibility
remains outside its target.

## Runner Contract

The companion runner runs the eight Dijkstras on `B_6(0)`, checks the
integer reverse test, recomputes the three reported population
variances, confirms that the lex-first variance-minimizing reverser is
`ν`, quotes the live axiom sentences, and records the import boundary.
Declared review inputs are this note and the axiom memo only.

Not leftover of ν alone.
