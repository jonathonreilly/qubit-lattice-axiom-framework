# Post-Record Supplied Selection-Rule Interface

**Date:** 2026-06-06
**Type:** exact conditional selection interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for supplied finite selection rules and
margin stability; candidate, score, rule, and dial-score derivation remain open;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_supplied_selection_rule_interface_2026_06_06.py`](../scripts/frontier_post_record_supplied_selection_rule_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_supplied_selection_rule_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_supplied_selection_rule_interface_2026_06_06.txt)

## Result

The post-record score layer cannot choose a model or dial canonically. If the
missing selection rule is supplied, the finite selection step itself is exact.

Let `M` be a finite candidate set, let

```text
s: M -> Q
```

be a supplied exact score map, and let `prec` be a supplied total tie-priority
order. The lexicographic selector

```text
Sel(s,prec) = the candidate with maximal (score, tie-priority)
```

is unique and deterministic.

If the winning score gap is

```text
Delta = s(winner) - max{s(m) : m != winner},
```

and `Delta > 0`, then the selected candidate is stable under any score
perturbation bounded by `epsilon < Delta/2` on every candidate. This is the
finite margin-stability interface.

For a dial surface, the safe statement is therefore:

```text
supplied dial candidates
  + supplied exact scores
  + supplied tie/decision rule
  + positive margin
  => stable selected dial location under that supplied rule.
```

This does not force the dial. It identifies a stable location only inside the
supplied score-and-rule surface.

## What this unlocks

This gives downstream dynamics and audit lanes a clean replacement for
score-to-selection overclaims:

```text
post-record data
  + supplied model or dial candidate scores
  + supplied selection rule
  => exact selected candidate under that rule.
```

When a positive score gap is supplied, the selected candidate is robust to
small bounded score errors. This is useful for candidate dial stability
arguments, finite model comparisons, and conditional audit decisions.

## What remains outside

This note does not derive:

- the candidate set;
- the score map;
- the tie-priority order, threshold, loss, or decision rule;
- the physical interpretation of the score;
- Born weights, an instrument, transition kernel, Hamiltonian, action, clock,
  or rate;
- a generation or Koide dial score landscape;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: stable selected location remains conditional on supplied candidates, scores, selection rule, and positive margin
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a supplied-selection interface, not a derivation of scores, rules, or a dial setting."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries for post-record data and selection residuals;
- deterministic max-with-priority selection on finite rational scores;
- tie resolution only when a priority order is supplied;
- margin stability for perturbations below half the exact score gap;
- boundary loss of strict margin at half-gap;
- likelihood-score and posterior-score examples with supplied rules;
- supplied dial-score example selecting a stable location under the supplied
  margin rule;
- Record does not derive candidate scores, rules, physical laws, or a
  generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_supplied_selection_rule_interface_2026_06_06.py
```
