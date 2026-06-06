# Record IID/Typicality Firewall

Date: 2026-06-06

Status: no-go

actual_current_surface_status: no-go
trace_class: direct_blocker_closure
reachability_to_target: prunes
conditional_surface_status: "IID sequence law gives the usual binomial frequency law when supplied."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block prunes a shortcut; it does not derive IID, typicality, or frequency convergence."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Summary

This block closes the next record-dynamics shortcut:

```text
one-shot production probability -> IID frequencies / typicality
```

That implication is invalid on the current surface. The runner constructs two
exact two-record joint laws with the same one-step marginal

```text
p = (2/3, 1/3)
```

but different count/frequency distributions.

## Runner

Runner:

```text
scripts/frontier_record_iid_typicality_firewall_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_record_iid_typicality_firewall_2026_06_06.txt
```

Scorecard:

```text
PASS=22 FAIL=0
```

## Exact Counterfamily

The IID joint law is:

```text
P_iid(00)=4/9, P_iid(01)=2/9, P_iid(10)=2/9, P_iid(11)=1/9.
```

The locked/correlated joint law is:

```text
P_lock(00)=2/3, P_lock(01)=0, P_lock(10)=0, P_lock(11)=1/3.
```

Both have the same first and second one-step marginals `(2/3, 1/3)`. They are
therefore indistinguishable from the one-step probability vector alone.

But their zero-count laws differ:

```text
IID:    Pr(N_0=0,1,2) = (1/9, 4/9, 4/9)
Locked: Pr(N_0=0,1,2) = (1/3, 0, 2/3)
```

The expected count can agree while the variance and typicality data differ.
Thus frequency claims require a sequence law, not only a one-step law.

## Dynamics Implication

The record stack now has four separated gates:

```text
pre-record instrument + Born bridge -> one-shot probabilities
IID/sequence law                    -> frequencies / typicality
supplied generator                  -> stable dial locations
clock/rate unit                     -> physical rates
```

The realized post-record history remains a word or count after outcomes are
written. An empirical frequency from one realized finite word need not equal
the one-step probability.

## Boundaries

This block does not:

- derive IID or typicality;
- derive a Born/instrument probability-origin bridge;
- derive a physical generator;
- derive a clock/rate unit;
- select a generation/Koide dial value;
- update repo-wide authority surfaces.
