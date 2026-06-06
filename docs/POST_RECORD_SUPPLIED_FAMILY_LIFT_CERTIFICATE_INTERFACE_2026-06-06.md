# Post-Record Supplied Family-Lift Certificate Interface

**Date:** 2026-06-06
**Type:** exact support / supplied interface
**Claim type:** methodology
**Status:** exact-support branch-local under a supplied family-lift rule;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py`](../scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.txt)

## Result

The finite-to-unbounded no-go says a finite post-record certificate alone cannot
determine an unbounded law. This branch records the complementary exact-support
interface: if a family-lift rule is supplied, a finite projective ladder can be
checked mechanically.

The interface has three pieces:

1. a finite ladder of post-record certificates;
2. supplied projection maps between adjacent levels;
3. a supplied lift rule that names which stable finite predicate is allowed to
   pass through the family.

This is not an unbounded retained claim. It is the exact finite certificate that
the missing family-lift input has been provided for this supplied ladder.

## Finite Ladder

```text
C1 = 1
C2 = 1, 0
C3 = 1, 0, 1
C4 = 1, 0, 1, 1
```

The supplied projection map truncates one site:

```text
pi_n(C_{n+1}) = first n sites of C_{n+1}
```

The runner verifies:

```text
pi_1(C2) = C1
pi_2(C3) = C2
pi_3(C4) = C3
```

The supplied stable predicate is:

```text
leading_marker_is_one(C_n) = true
```

That predicate is stable across the checked ladder. By contrast, prefix density is not stable on this ladder:

```text
1, 1/2, 2/3, 3/4
```

The interface therefore records the stable predicate and refuses to smuggle in a
density-limit claim.

## Framework Implication

This is the constructive side of the bounded/unbounded split:

- pre-record law carries probabilities;
- post-record records carry realized information;
- finite certificates can verify a supplied projective ladder;
- unbounded interpretation still needs the supplied or derived family-lift rule;
- independent audit remains required before effective retained status.

## Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "supplied family-lift rule admits a finite projective ladder certificate"
hypothetical_axiom_status: "a family-lift axiom could supply this rule but would still need audit"
admitted_observation_status: "finite ladder levels remain realized records, not a probability law"
proposal_allowed: false
proposal_allowed_reason: "This branch checks a supplied family-lift interface and does not derive or apply unbounded retained authority."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner Certificate

The runner verifies:

- four finite ladder levels are present;
- adjacent supplied projections commute;
- the leading-marker predicate is stable across the ladder;
- the prefix density is not used as a stable lift on this ladder;
- the family-lift rule is supplied, not derived from Record alone;
- no audit verdict, authority write, selected dial, or unbounded retained
  promotion is applied.

Run:

```text
python3 scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py
```
