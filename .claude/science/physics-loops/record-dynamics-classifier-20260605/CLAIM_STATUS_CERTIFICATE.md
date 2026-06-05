# Claim Status Certificate - Record Dynamics Classifier

**Loop slug:** `record-dynamics-classifier-20260605`  
**Date:** 2026-06-05  
**Branch:** `physics-loop/record-dynamics-classifier-20260605`  
**Review PR:** https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2700  
**Runners:**

- `scripts/record_function_finite_sector_algebra_2026_06_05.py` -> PASS=18 FAIL=0
- `scripts/generation_dial_local_stability_grammar_2026_06_05.py` -> PASS=13 FAIL=0
- `scripts/generation_dial_dynamics_stability_classifier_2026_06_05.py` -> PASS=26 FAIL=0

## Status fields

```yaml
actual_current_surface_status: open
target_claim_type: bounded_theorem
conditional_surface_status: bounded-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Claim

On the exact generation dial `r(s)=2^(s-1)`, dynamics classes can be
classified by local stability:

- two-sector entropy ascent stabilizes `s=0`;
- reverse branch `r -> sqrt(r/2)` stabilizes `s=0`;
- sharpening `r -> 2r^2` repels `s=0`;
- real-mode entropy ascent stabilizes `s=1`;
- heat-kernel path `r(t)=tanh(t)^4` transits through `s=0`.

## What this narrows

It replaces "force Koide" with the audit-safe question:

```text
Which record-function dynamics make s=0 stable, and what gate selects that
partition/arrow physically?
```

## What remains open

- Physical charged-lepton partition selection.
- Physical arrow/source/action selection.
- Any move from bounded classifier to retained value selection.

## Honesty result

The artifact is clean as a bounded theorem/proposal. It should not be used as a
retained proof that charged leptons physically sit at `Q=2/3`.
