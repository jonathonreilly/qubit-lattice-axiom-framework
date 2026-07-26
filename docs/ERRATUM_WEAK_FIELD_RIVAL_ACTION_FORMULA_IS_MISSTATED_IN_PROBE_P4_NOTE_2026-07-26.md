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

Barrier B(c) is a named admission on the `G_Newton` lane, and it is currently
discharged only by empirical match:

> "The selection of valley-linear is by EMPIRICAL match to `F~M = 1`, not by
> retained derivation."

Anyone attacking B(c) from P4's text would be trying to discriminate
valley-linear from `L√(1-φ)`. Those two expressions share a leading power, so
**the mass-law exponent cannot discriminate them** — the very observable B(c)
is stated in terms of. They are not identical functions, and higher-order
behaviour or a different observable could in principle tell them apart; but the
comparison as B(c) frames it has no content. The genuine alternative on the
mass-law observable is the sublinear class. This erratum redirects that work; it
does not do it.

On framing: the lane's parent row `gravity_full_self_consistency_note` is
`criticality: critical` with 773 transitive descendants. That count belongs to
the parent row and is quoted only to indicate why the lane is worth keeping
tidy — **it does not follow that this transcription error bears on those
descendants**, and no such claim is made here.

## Claim ledger

Per the inference audit (physics-loop step 11). One row per claim; a
restatement gets its own row.

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| E1 | `L√(1-φ)` has leading power 1 | row R1/R2, exact closed-form depth `f/(1+√(1-f))` | `f > 0` and small; real branch of the square root | shown: depth/f → 1/2, a finite nonzero limit; claimed: the same | depth/f failing to converge, or converging to 0 or ∞ |
| E2 | the probe measures `L(1-√f)`, power 1/2 | `action_value()` in `scripts/action_universality_probe.py`, quoted verbatim | none — it is a source quotation | shown: the source defines `valley_sqrt` as `L*(1.0 - np.sqrt(f))`; claimed: the same | the branch reading otherwise on `main` at the searched commit |
| E3 | P4 pairs the first formula with the second's number | P4 lines ~89, ~199, ~305, quoted | none — a quotation | shown: three occurrences pairing `L√(1-φ)` with 0.50; claimed: the same | any of the three reading `L(1-√f)` |
| E4 | the geometric spent-delay is also power 1/2 | row R3, expansion of `dl - √(dl²-L²)` at `dl = L(1+ε)` | `ε > 0` and small, so the root is real | shown: depth/√(2ε) → 1 and the log-log slope → 1/2; claimed: the same | the coefficient failing to converge to 1 |
| E5 | the mass-law exponent cannot discriminate `L(1-f)` from `L√(1-φ)` | E1 plus the landed class definition | the landed classes are keyed to leading power on that fixed family | shown: both have leading power 1, so that one observable cannot separate them; claimed: the same, **and explicitly not** that no observable can — higher-order behaviour may | an observable keyed to leading power that separates them |

Note on E5: an earlier draft claimed the comparison was undecidable outright.
That overstated it — the two are different functions and only the leading
mass exponent is blind to the difference. The row records the narrower claim.

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

An accompanying attempt to supply a mechanism for the exponent was rejected at
the value gate and is **not** part of this change. Nothing from it appears in
this note or its runner, and it is absent from this branch entirely.

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
