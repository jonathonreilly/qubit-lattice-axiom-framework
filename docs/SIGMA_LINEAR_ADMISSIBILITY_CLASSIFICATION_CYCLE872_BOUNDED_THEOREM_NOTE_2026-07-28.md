# The admissible response algebra is blind, and escape (b) routes through escape (a) — Cycle 872

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed gravity axiom-up
ladder, campaign 5 wave 2; no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle872_sigma_linear_admissibility_2026_07_28.py`](../scripts/frontier_cycle872_sigma_linear_admissibility_2026_07_28.py)
- [`frontier_cycle872_admissibility_independent_check_2026_07_28.py`](../scripts/frontier_cycle872_admissibility_independent_check_2026_07_28.py)

Receipt:

- [`sigma_linear_admissibility_cycle872_receipt_2026_07_28.json`](../outputs/sigma_linear_admissibility_cycle872_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted 2026-08-03; substitution disclosed);
supervisor review including direct verification of the load-bearing
identity (below). Independent audit still required.

## The classification

The constructor grammar is declared as data and generates a finite
class: 8 pre-states (identity/exchange per endpoint slot at grading
power one or two), 8 index-subset contractions, 5 tensor-square
pairings — 384 generators (64 linear, 320 quadratic, 3,200 scalar
components), closed under rational linear combination and product, so
the classified object is the generated ALGEBRA, not a generator list.
Admissibility = K1 direction-reversal parity + K2 endpoint-exchange
equivariance (both stated as data): 344 of 384 admissible (the 40
failures are all endpoint-transfer objects with mismatched premaps).

**Outcome B, hardened.** Over all 470,592 landed (member, object)
pairs: ZERO sigma-sensitive. Every admissible generator is a
sigma-CONSTANT on the landed family (degree census {-1, 0}), and
constants close under sums and products, so the blindness extends to
the whole generated algebra (500 seeded random elements to monomial
degree 4: 0 sensitive; checker to degree 5). All six Cycle-868 objects
reproduce exactly as named class members — this block SUBSUMES 868's
wall rather than replacing it.

## The escape-dependence theorem (the important part)

Escape (b) of Cycle 868 — a sigma-linear admissible object — is
REALISABLE as a shape: 162 of 344 admissible objects are genuinely
sigma-odd on a conformally loaded source. Yet all 162 yield zero
sensitivity on the landed family, and the mechanism is one identity
(supervisor-verified by hand): the only sigma-odd algebra element is
the sector contraction of the graded source,

    sector_contract(G_sigma S) = 3 sigma * conformal(S)
                               = sigma * (sector trace of S),

since the trace-free channel sector-sums to zero. Hence blindness of
the entire admissible algebra ⟺ the source's conformal channel
vanishes. **Cycle 868's two escape conditions are therefore NOT
independent: (b) supplies the shape, (a) supplies the load. The sign
datum is reachable only through a trace-bearing source.** The
companion block (Cycle 873) settles what that means.

## Refinement of 868's general mechanism statement

Cycle 868's M1, stated for its six objects, is correct and unaffected
(its own unbalanced-ledger certificate verified evenness for any
source at that scope). As a GENERAL claim about quadratic
contractions it is too broad, in two separable ways found here:
per-sector axis contractions are sigma-odd already at equal grading
power (sector-orthogonality, not quadratic degree, is what forces
evenness where it holds), and mixing grading powers G^1 with G^2
admits sigma^3 terms (top observed degree 4, above the degree-2 bound
that held for 868's six objects). The corrected general mechanism:
evenness holds exactly where a sector sum kills the trace-free/
conformal cross terms.

## Checker teeth

Corroboration by exhaustion with NO admissibility filter (nothing can
hide in the rejected bin): a wider class (7 premaps x grading powers
1-4), 1,838,592 linear + 7,230,720 quadratic + 600 random degree-<=5
comparisons — 0 sensitive; independent route in six integer sigma
worlds with exactness certified by fifth finite difference; reproduces
344 admissible and 162 sigma-odd exactly. Adversary controls fire:
detuned ledger 608 features; a planted off-grammar sigma-visible
object caught on 456 features across 3 members ON THE LANDED LEDGER;
fabricated claim block caught on 6 fields. 0/8 claim disagreements.

## Negative-claim discipline (compact N-gate)

Routes attacked: the full generator class (384); the generated algebra
to degree 4 (primary) and 5 (checker); the no-filter wider class
(~9M comparisons); per-sector contractions (found odd, vanish on
landed via the conformal channel); mixed-grading terms (found, degree
<= 4, vanish on landed). Steelman ("something outside the grammar sees
sigma") is answered constructively: the planted off-grammar
sigma-visible object IS caught by the checker's sweep on the landed
ledger — visibility requires conformal load, which is escape (a), not
a grammar gap. The negative is scoped to the declared grammar, its
closure operations, and the landed family; the closure boundary is
stated in the emitted payload.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "868 escape (b): a response object linear in the endpoint exchange ... could see sigma"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "escape (b) is dead as an independent route; everything gates on the conformal channel — see Cycle 873 for where that channel's zero comes from"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite declared grammar classified exhaustively in exact arithmetic; algebra closure argued by the constants property and swept to degree 5; the odd-element identity is a one-line sector-sum computation"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 868 scope (family, ledger, grading, objects) — sha-pinned, six
  objects reproduced in-class;
- nothing else: stdlib exact arithmetic.

### Derived

- the admissible-algebra classification (344/384; K1/K2 as data);
- the blindness of the generated algebra on the landed family;
- the escape-dependence theorem via the sector-contraction identity;
- the general-mechanism refinement (sector-orthogonality, not degree).

### Open

- the conformal channel's provenance — Cycle 873's question;
- constructors outside the declared grammar (boundary stated).

## Verdict

The wall 868 built object-by-object is really an algebra-wide fact
with a single load-bearing beam: every admissible way of looking at
the response surface factors its sigma-dependence through the source's
sector trace. The two named ways out collapse into one door.
Independent audit still required.
