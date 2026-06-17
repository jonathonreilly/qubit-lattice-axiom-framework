# Wilson Action Generator-Rescaling Beta Transformation Boundary

**Date:** 2026-06-17
**Claim type:** bounded_theorem
**Type:** exact-support boundary theorem inside the supplied Wilson plaquette
action and canonical trace-normalization surface.
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/frontier_wilson_action_generator_rescaling_beta_transformation_2026_06_17.py`](../scripts/frontier_wilson_action_generator_rescaling_beta_transformation_2026_06_17.py)
**Cached log:**
[`logs/runner-cache/frontier_wilson_action_generator_rescaling_beta_transformation_2026_06_17.txt`](../logs/runner-cache/frontier_wilson_action_generator_rescaling_beta_transformation_2026_06_17.txt)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
target_claim_id: g_bare_rescaling_freedom_removal_theorem_note_2026-05-03
target_blocker_text: "missing_bridge_theorem: add a Wilson-action normalization/transformation theorem deriving beta_new/beta_old under T_a -> c T_a, or narrow the row to the closed Gram-scaling lemma only."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
conditional_surface_status: "Exact inside the supplied standard Wilson plaquette action; it separates fixed-component action compensation from coupling-coordinate WM naming."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true_for_exact_support_only
proposal_allowed_reason: "The note derives the beta transformation only after the rescaling convention is specified; it does not derive Wilson action-surface selection or g_bare=1."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Purpose

The audit blocker for
[`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)
identified a missing bridge:

```text
derive beta_new/beta_old under T_a -> c T_a
```

The current repaired `g_bare` row is already narrowed to the closed
Gram-scaling lemma. This note supplies the separate Wilson-action
transformation boundary that the old broader row was missing. The important
point is that there is no convention-free beta law under the phrase
`T_a -> c T_a`. There are three different exact statements, depending on
which object is held fixed.

## Setup

Let `T_a` be Hermitian `su(N_c)` generators with canonical trace form

```text
Tr(T_a T_b) = delta_ab / 2.
```

Use the supplied standard Wilson plaquette action and small-`a` plaquette
parametrization

```text
S_W = beta sum_p (1 - (1/N_c) Re Tr U_p),
U_p = exp(i a^2 g F^a T_a + O(a^3)).
```

For a single plaquette plane, the second-order deficit is

```text
1 - (1/N_c) Re Tr U_p
  = a^4 g^2 F^a F^b Tr(T_a T_b) / (2 N_c) + higher order
  = a^4 g^2 F^a F^a / (4 N_c) + higher order.
```

This note assumes the Wilson action form and the continuum coefficient target
used in
[`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
It does not derive Wilson action-surface selection.

## Theorem A: Fixed-Component Generator Scaling

Let

```text
T'_a = c T_a,
```

with the same component field `F^a`, the same coupling coordinate `g`, and
the same continuum coefficient target. Then

```text
Tr(T'_a T'_b) = c^2 delta_ab / 2,
```

so the Wilson plaquette deficit scales by

```text
D'(F,g,T') = c^2 D(F,g,T).
```

Therefore, to keep the same Wilson action coefficient against the same
component field, the beta coefficient must compensate inversely:

```text
beta'_fixed * D' = beta * D
        => beta'_fixed / beta = 1 / c^2.
```

Equivalently, matching the continuum coefficient gives

```text
beta'_fixed = 2 N_c / (c^2 g^2) = beta / c^2.
```

This is the literal Wilson-action transformation at fixed component field.

## Theorem B: Pure Basis Relabeling

If the generator basis and components are relabeled together,

```text
T'_a = c T_a,
F'^a = F^a / c,
```

then the Lie-algebra element in the plaquette exponent is unchanged:

```text
g F'^a T'_a = g (F^a / c) (c T_a) = g F^a T_a.
```

The plaquette group element, Wilson deficit, and action coefficient are
unchanged:

```text
D(F',g,T') = D(F,g,T),
beta'_basis = beta.
```

This is a coordinate relabeling, not a physical change of the Wilson action.

## Theorem C: Coupling-Coordinate WM Naming Route

The abstract Wilson-matching naming rule

```text
beta(g) = 2 N_c / g^2
```

has the pure algebraic rescaling identity

```text
g' = g / c
        => beta(g') = c^2 beta(g).
```

This is the exact identity isolated in
[`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md).
It is a coupling-coordinate statement. It becomes a statement about
`T_a -> c T_a` only after an additional convention declares that the coupling
coordinate transforms as `g -> g / c` while the generator basis transforms as
`T_a -> c T_a`.

Under that additional convention, the plaquette exponent may be held fixed:

```text
(g / c) F^a (c T_a) = g F^a T_a.
```

But the beta law in this route is the WM coordinate law

```text
beta'_WM / beta = c^2,
```

not the fixed-component Wilson action compensation law of Theorem A. The two
laws answer different questions.

## Consequence

The expression "`T_a -> c T_a`" by itself is underspecified for beta routing.
The exact alternatives are:

| Rescaling convention | Deficit ratio | Required beta ratio |
|---|---:|---:|
| Fixed components: `T'_a=cT_a`, same `F^a`, same `g` | `c^2` | `1/c^2` |
| Pure basis relabeling: `T'_a=cT_a`, `F'^a=F^a/c` | `1` | `1` |
| WM coupling-coordinate naming: `g'=g/c` inside `beta(g)=2N_c/g^2` | naming route | `c^2` |

Therefore the old beta-routing claim does not follow from Wilson matching
alone. A source row that uses `beta_new = c^2 beta_old` must say it is using
the coupling-coordinate WM naming route, not the fixed-component Wilson action
coefficient transformation.

## Boundary

This note does not claim:

- Wilson plaquette action-surface selection from the framework axioms;
- `g_bare = 1`;
- `beta = 6` as a physical value;
- a retained or effective audit status for any row;
- that the fixed-component law, basis-relabeling law, or WM naming law is the
  uniquely framework-native convention;
- that the narrowed Gram-scaling row should be promoted without independent
  audit.

The theorem is only the exact transformation boundary inside the supplied
Wilson action and canonical trace surface.

## Downstream Use

The repaired Gram-only row
[`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)
can cite this note as a separate beta-routing boundary. The conditional
arithmetic row
[`BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md`](BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md)
may cite it for the coupling-coordinate WM route, while keeping the
fixed-component Wilson-action route out of that algebraic claim.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_wilson_action_generator_rescaling_beta_transformation_2026_06_17.py
```

Expected:

```text
TOTAL: PASS=137 FAIL=0
```
