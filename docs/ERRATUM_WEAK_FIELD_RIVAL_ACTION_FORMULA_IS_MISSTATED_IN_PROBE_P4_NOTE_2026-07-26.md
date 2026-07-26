# Erratum: the Weak-Field Rival Action Formula Is Misstated in Probe P4 — `L√(1-φ)` Is Weak-Field Linear, and the Measured 0.50 Row Is `L(1-√f)`

**Date:** 2026-07-26
**Type:** erratum
**Claim type:** erratum (a correction to the statement of a landed support
note; no new theorem, no mechanism, no derivation).
**Status authority:** none. Audit: unset. Constitutional effect: none. This
note edits no axiom, foundation, Qualification, primitive, registry, policy,
queue, audit-status, or PR-control surface. **It changes no numerical result,
no verdict, and no lane status.** It corrects a formula.
**Primary runner:**
[`scripts/physical_weak_field_action_form_erratum_cycle707b_2026_07_26.py`](../scripts/physical_weak_field_action_form_erratum_cycle707b_2026_07_26.py)
(4 PASS / 0 FAIL, exit 0).

## The correction

[`G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4`](G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md)
states, in three places (Barrier B(c) at lines ~89, ~199 and ~305), that the
alternative to the valley-linear weak-field action is

> `S = L√(1 - φ)` (spent-delay), gives `F~√M = 0.50`, NOT Newtonian

**The formula and the number do not belong together.** What the probe measures
is a different expression. In
[`scripts/action_universality_probe.py`](../scripts/action_universality_probe.py),
`action_value()` defines the sqrt mode as

```python
if action_mode == "valley_sqrt":
    return L * (1.0 - np.sqrt(f))
```

— the square root is on the **field**, giving `S = L(1 - √f)`, whose valley
depth is `√f`: leading power **1/2**, consistent with the measured
`F~M = 0.50`. This matches the landed
[`ACTION_UNIQUENESS_NOTE`](ACTION_UNIQUENESS_NOTE.md), whose sublinear row is
`S = L(1 - f^0.5)`.

P4's expression has the square root on `1 - φ` instead, and

```text
1 - sqrt(1 - f) = f/2 + f^2/8 + ...
```

so `L√(1 - φ)` has leading power **1**, coefficient 1/2. By the landed
classification it therefore sits in the **Newtonian** class, alongside
`L(1-f)`, `L exp(-f)` and `L/(1+f)` — the very class it is offered as the
alternative to.

| expression | source | leading power | class |
|---|---|---:|---|
| `L(1-f)` | valley-linear | 1 | Newtonian |
| `L exp(-f)` | ACTION_UNIQUENESS | 1 | Newtonian |
| `L/(1+f)` | ACTION_UNIQUENESS | 1 | Newtonian |
| **`L√(1-φ)`** | **P4's stated rival** | **1** | **Newtonian** |
| `L(1-√f)` | what the probe measures | 1/2 | sublinear |
| `L(1-f²)` | ACTION_UNIQUENESS | 2 | superlinear |

## The intended class is right; only the formula is wrong

Three different expressions carry the "spent-delay / sqrt" name across the
repo, and it is worth recording that two of them agree, so this erratum does
not disturb any measured result.
[`ACTION_CROSSOVER_NOTE`](ACTION_CROSSOVER_NOTE.md) defines spent-delay
geometrically as `S = dl - √(dl² - L²)`. Writing `dl = L(1+ε)`,

```text
S = L[(1 + eps) - sqrt(2 eps + eps^2)]  ->  L[1 - sqrt(2 eps)],
```

so the geometric spent-delay has depth `√(2ε)`: leading power **1/2**, with
coefficient `√2` (row R3 confirms the coefficient converges). So the
*geometric* spent-delay and the *measured* `L(1-√f)` share the sublinear class,
and P4's `L√(1-φ)` is the sole outlier among the three.

**Net effect: P4's number `0.50` is correct for the action it meant; the
formula it prints is not that action.**

## Why this is worth recording

Barrier B(c) is a named admission on the `G_Newton` lane, whose parent row
`gravity_full_self_consistency_note` is `criticality: critical` with 773
transitive descendants. B(c) is currently discharged only by empirical match:

> "The selection of valley-linear is by EMPIRICAL match to `F~M = 1`, not by
> retained derivation."

Anyone attacking B(c) from P4's text would be trying to discriminate
valley-linear from `L√(1-φ)` — a comparison **between two members of the same
universality class**, which no argument can decide because there is nothing to
decide. The genuine alternative is the sublinear class. This erratum redirects
that work; it does not do it.

## What this does not do

- It does **not** derive the weak-field action, supply a mechanism for why any
  exponent takes its value, or change admission (c)'s status. B(c) remains
  empirically selected and unforced.
- It does **not** revise any measured number, any log, any cached artifact, or
  any audit verdict. `F~M = 0.50` stands for the action that was run.
- It does **not** claim the universality classes are universal. They are landed
  as a fixed-family observation, explicitly "not promoted to a closed formula
  or a universal theorem", and are used here only to place expressions in the
  classes that note defines.
- It makes no claim about which class the framework's rule should be in.

A companion cycle attempted to supply the missing mechanism via perturbation
theory and was rejected at the value gate for overreach — it invoked Rellich
without its analyticity hypothesis, claimed a premise reduction it had not
established, and contained a control row that silently excluded its own
counterexample. That content is **not** reissued here; it is recorded in
`PR_BACKLOG_707.md`. This erratum is deliberately limited to what survived
adversarial review.

## Scope for independent review

Every row is a leading-power extraction from a closed-form valley depth, with
no lattice run and no fitted quantity. The rationalized depth forms are used
because direct evaluation of `1 - g(f)` at `f ~ 1e-9` loses the answer to
cancellation — for `g = 1 - f²` it underflows to exactly zero, which row R4
demonstrates deliberately, and R4 also cross-checks every closed form against
`1 - g(f)` at moderate `f` where the subtraction is safe. R2 reproduces the
probe's `action_value()` branch inline rather than importing it, so the runner
is self-contained.

## Dependency citations

The runner imports nothing from the repository.
[`G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4`](G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md)
is the note corrected.
[`ACTION_UNIQUENESS_NOTE`](ACTION_UNIQUENESS_NOTE.md) supplies the universality
classes and the tested forms;
[`ACTION_CROSSOVER_NOTE`](ACTION_CROSSOVER_NOTE.md) supplies the geometric
spent-delay definition;
[`scripts/action_universality_probe.py`](../scripts/action_universality_probe.py)
supplies what was actually executed. The `criticality` and descendant count are
read from `docs/audit/data/ledger/gr/gravity_full_self_consistency_note.json`.
