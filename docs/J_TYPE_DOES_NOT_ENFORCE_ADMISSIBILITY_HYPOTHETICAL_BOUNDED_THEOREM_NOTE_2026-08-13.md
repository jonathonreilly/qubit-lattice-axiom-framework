---
claim_id: j_type_does_not_enforce_admissibility_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a two-site window with labels {A,B,C} and a declared one-site law mu(A)=3/5, mu(B)=2/5, mu(C)=0, the displayed C1 type J:W→{0}∪M admits both J_ok=(A,0) and J_bad=(C,0). Unit-count I is 1 on both, so scalar I does not split them; displayed J does. Admissibility is not a consequence of that type unless M is defined to be supp(mu). The leftover constraint is im(J)\\{0} ⊆ supp(mu). Hypothetical; not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/j_type_does_not_enforce_admissibility_hypothetical_2026_08_13.py
---

# `J` Type Does Not Enforce Admissibility (Hypothetical)

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** C1 follow-on on lock type versus the Record word “admissible.”
Not pairing-on-`J`. Not a menu-picking type-split sold as progress.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/j_type_does_not_enforce_admissibility_hypothetical_2026_08_13.py`](../scripts/j_type_does_not_enforce_admissibility_hypothetical_2026_08_13.py)
**Parent on origin/main:** axiom memo only,
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Record says a lock is *admissible*. Displayed C1 writes a lock field
`J:W→{0}∪M`. That type does not force `J(z)∈supp(μ)` unless `M` is
*defined* to be `supp(μ)`. On the declared labels `M={A,B,C}` the
inadmissible lock `J_bad=(C,0)` is well-typed and illegal. Scalar
unit-count `I` is `1` on both the legal and the illegal lock, so `I`
does not split them. Displayed `J` does. The leftover constraint is

`im(J)\{0} ⊆ supp(μ)`.

C1-strong therefore does not absorb the word “admissible.” Owner
wording must either set `M:=supp(μ)` or keep that constraint. The
declared `μ` is a model, not a derived law. Unit-count `I=1` is a
convention; Record additivity does not force the unit. C1 is not
adopted. No pairing is placed on `J`. No Born compiler is imported.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Unit-count I, displayed J, and declared mu are exact on a two-site window; the C1 type does not absorb Record admissibility, and C1 remains a displayed counterfactual."
trace_class: negative_route_pruning
target_claim_id: c1_j_type_absorbs_admissible
target_blocker_text: "the C1 type W→{0}∪M already forces the lock into supp(mu)"
source_of_blocker_text: packet C1 follow-on (not C6/C7)
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for J_ok=(A,0) and J_bad=(C,0) on W={x,y} with declared mu; axiom adoption remains closed"
next_trace_action: "C1 type does not force lock in supp(mu). Keep im(J)\\{0} ⊆ supp(mu) or set M:=supp(mu). Do not adopt C1."
hypothetical_axiom_status: "C1 follow-on: J type does not force lock in supp(mu); admissibility stays a constraint on im J; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Window `W={x,y}`. Labels `{A,B,C}`. Declared one-site law, as exact
`Fraction` values and not a derived distribution,

```text
μ(A) = 3/5,    μ(B) = 2/5,    μ(C) = 0.
```

Support `supp(μ)={A,B}`. The displayed C1 lock type is a map

```text
J : W → {0} ∪ M,    M = {A,B,C}.
```

Legal lock: `J_ok=(A,0)`, meaning `J(x)=A` and `J(y)=0`.
Inadmissible lock: `J_bad=(C,0)`, meaning `J(x)=C` and `J(y)=0`.

Both tuples are values of that type. Unit-count readout is the
cardinality convention

```text
I(J) = |{z ∈ W : J(z) ≠ 0}|.
```

Occupied sites contribute one because that is the unit chosen for this
display. Record additivity does not force the unit `1`. Identity gates
call `I_of` on both locks, `J_of` on both locks, `mu_C()` (`=0`), and
`mu_A()` (`=3/5`).

The only parent on `origin/main` is the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). C1 `J`
arithmetic is reconstructed here.

## Exact Target

Show that scalar `I` does not split `J_ok` from `J_bad`, that displayed
`J` does, that the C1 type on `M={A,B,C}` does not enforce
`J(z)∈supp(μ)`, and that the leftover constraint is
`im(J)\{0} ⊆ supp(μ)`.

## Theorem 1 — Scalar `I` Does Not Split

```text
I(J_ok) = I(J_bad) = 1.
```

Each map is nonzero at exactly one site. The identity gates are
`I_of(J_ok)` and `I_of(J_bad)`. The common value `1` is the unit-count
convention, not a consequence of Record additivity. Scalar `I` therefore
does not split the admissible lock from the inadmissible lock.

## Theorem 2 — Displayed `J` Splits Them

```text
J_ok ≠ J_bad.
```

The first component is `A` versus `C`. The identity gates are `J_of` on
both maps. Displayed `J` splits the two locks. This is not a pairing
and is not a menu-picking type-split sold as progress.

## Theorem 3 — Admissibility Is Not a Type Consequence

The current Record axiom, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), includes:

> When present, a record locks exactly one admissible local possibility.

Admissibility is not a consequence of the C1 type `W→{0}∪M` unless `M`
is *defined* to be `supp(μ)`. On the declared labels `M={A,B,C}`,
`J_bad` is well-typed (`C∈{0,A,B,C}`) and illegal (`C∉supp(μ)`). The
leftover constraint, after the type is written, is

```text
im(J) \ {0} ⊆ supp(μ).
```

On `J_ok` the nonzero image is `{A}`, which sits in `{A,B}`. On
`J_bad` the nonzero image is `{C}`, which does not. The identity gates
`mu_C()` and `mu_A()` return `0` and `3/5`. Declared `μ` is a model,
not a derived one-site law.

## Theorem 4 — C1-Strong Does Not Absorb “Admissible”

C1-strong is the claim that the type `W→{0}∪M` already carries the
Record word “admissible.” Theorem 3 shows it does not, unless `M` is
reset to the support. Owner wording must either set `M:=supp(μ)` or
keep the image constraint. This note displays that fork. It does not
pick `μ`. It does not adopt C1. It does not rewrite Record.

## Theorem 5 — Scoped Residual

Do not force `r=1/2`. Do not adopt `L_phys`. Do not put a pairing on
`J`. Do not import a Born compiler (no `Tr`). Do not adopt C1.

## Mutation And Identity Gates

Identity gates must call `I_of(J_ok)`, `I_of(J_bad)`, `J_of` on both,
`mu_C()` (`=0`), and `mu_A()` (`=3/5`).

Required failures:

- predicate “`I` splits `J_ok` from `J_bad`” must fail
- predicate “`J_ok=J_bad`” must fail
- predicate “`μ(C)≠0`” must fail

## Negative Scope

The residual in Theorem 5 is only that C1, a pairing on `J`, a Born
compiler, `r=1/2`, and `L_phys` stay off the axiom file. The finite
identities are exact on this window. They do not pick a physical `μ`
and they do not rewrite Record.

## No-Go Discipline Gate

The negative claims are restricted to “the C1 type already forces the
lock into `supp(μ)`” and “scalar `I` distinguishes admissible from
inadmissible.” The gate does not certify a Record rewrite.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Scalar `I` as the split | evaluate `I_of` on both locks | Theorem 1: both equal `1` | **ATTEMPTED** |
| Displayed `J` as the split | evaluate `J_of` on both locks | Theorem 2: `J_ok ≠ J_bad` | **ATTEMPTED** |
| Type `W→{0}∪M` absorbs “admissible” | well-typed `J_bad` with `μ(C)=0` | Theorem 3: leftover image constraint | **ATTEMPTED** |
| C1-strong absorbs the word | set `M={A,B,C}` and keep the type | Theorem 4: wording fork remains | **ATTEMPTED** |
| Adopt C1, pairing on `J`, Born `Tr`, `r=1/2`, `L_phys` | enlarge the display | Theorem 5: refused | **ATTEMPTED** |

### N2 — wall independence

Equal unit-count `I` does not give the image constraint. Distinct `J`
does not pick `μ`. The leftover constraint is independent of the
scalar readout.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| window `W={x,y}`, labels `{A,B,C}` | stipulated finite objects |
| `μ(A)=3/5`, `μ(B)=2/5`, `μ(C)=0` | declared model; not derived |
| unit-count `I=1` | convention; not forced by additivity |
| C1 adoption, pairing on `J`, Born `Tr` | not used |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | “locks exactly one admissible local possibility” | quoted; not used as a type theorem |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two displayed locks; three labels | no classification of every `J` |
| per site | both sites of `W` | no lattice-wide type theorem |
| per mode | unit-count `I` versus displayed `J` | no pairing on `J` |
| per block | C1 type versus Record “admissible” | no Born compiler |
| lattice-wide | not executed | only `W={x,y}` |

The runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure paths

1. Keep Record “admissible” as an image constraint on the current axiom file.
2. If C1 is later adopted, either set `M:=supp(μ)` or keep
   `im(J)\{0} ⊆ supp(μ)`.
3. A pairing on `J` remains extra either way.

### N7 — hostile steelman

> Once `M` is the local possibility domain, an illegal lock is already
> off-type, so the C1 type absorbs “admissible.”

The steelman is a definition of `M`. On the declared labels
`M={A,B,C}` it is false: `J_bad` is on-type and off-support. Absorbing
the word requires defining `M` to be `supp(μ)`, which is a wording
choice, not a type theorem.

### N8 — cross-cycle echo

This is a C1 follow-on, not C6 or C7. It reconstructs C1 `J`
arithmetic and stops. It does not put a pairing on `J` and it does not
import a Born compiler.

**Gate disposition:** PASS for (i) `I(J_ok)=I(J_bad)=1`, (ii)
`J_ok≠J_bad`, and (iii) leftover constraint
`im(J)\{0} ⊆ supp(μ)`. FAIL / DO NOT SHIP for “adopt C1,” “put a
pairing on `J`,” “import `Tr`,” “force `r=1/2`,” or “adopt `L_phys`.”

## Review Record

Independent audit remains required before any effective status may
change. No `review-loop` was invoked in producing this artifact.
