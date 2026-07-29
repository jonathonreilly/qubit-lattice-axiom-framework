# The Born acceptance harness — evidence-ceiling support for the Born lane

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact support (acceptance infrastructure)

Claim type: meta

Runners:

- [`frontier_born_acceptance_harness_2026_07_28.py`](../scripts/frontier_born_acceptance_harness_2026_07_28.py)
- [`frontier_born_acceptance_independent_check_2026_07_28.py`](../scripts/frontier_born_acceptance_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. It adds test infrastructure only.

## Result up front

The gravity/source lane gained a standing acceptance-harness set that
raised its evidence ceiling: any regression, tampering, or out-of-domain
feed against the landed surfaces is caught mechanically, with frozen
expected outputs. This package builds the same instrument for the Born
lane, over the landed Cycle-317 ternary Born-forcing surface (bridge and
release modules):

- **byte pins + landed self-runs**: both landed modules are sha256-pinned
  as frozen literals and executed in subprocess isolation (zero attribute
  writes into landed modules); their own certificate runs reproduce the
  frozen counts (bridge 15/0, release 14/0) and terminal markers —
  verdict ACCEPT;
- **lawful probes ACCEPT**: four frozen lawful feeds from the surface's
  own declared domain (exact axis directions and exact rational fraction
  tuples) pass through the unchanged machinery and match frozen expected
  values exactly;
- **malformed witnesses REJECT**: four frozen malformations (wrong
  arity, non-normalized, out-of-domain value, type violation) are
  refused — three by the landed surface's own domain checks with frozen
  refusal signatures, and one honestly labeled `harness-schema` (the
  landed surface does not itself check that malformation; the harness
  refuses it at the schema layer and says so — no silent claim that the
  surface enforces what it does not);
- **DRIFT armed**: a one-byte mutation of a sandbox copy of the bridge
  is detected as DRIFT while the real module's sha is proven unchanged;
- **live comparators**: a deliberately wrong frozen expectation in a
  quarantined table is caught by the harness's own comparison — the
  freeze-then-verify machinery is demonstrably not vacuous;
- **firewall audit**: an AST-level check finds feeds are data-only, no
  weight/probability synthesis identifiers, and exactly the declared
  surface call sites.

## Firewall (verbatim discipline)

Feeds are supplied apparatus data. The harness selects no Born law, no
weight map `w(E)`, and no probability content; it certifies only that
the landed machinery accepted or refused as frozen. The Born lane's
open physics (occurrence/Record/calibration bridges to weights) is
untouched.

## Supplied / derived / open

### Supplied

- the four lawful probe feeds and four malformation witnesses (declared
  apparatus data with frozen expectations; zero fitted parameters);
- the harness schema for feed shape (declared, printed);
- everything the landed Cycle-317 surface declares supplied.

### Derived

- the standing ACCEPT/REJECT/DRIFT verdict machinery with byte pins,
  subprocess-isolated self-runs, frozen-value comparisons, live-
  comparator demonstration, and the honest landed-vs-harness refusal
  labeling.

### Open

- the Born lane's physics itself (no movement claimed here);
- wiring epoch-derived feeds (the Cycle-729 package, not yet landed on
  main) into this harness once its surfaces land — the natural next
  infrastructure step;
- the full-Fock lift as an input-ported surface on the source-lane
  harness set (tracked separately).

## Negative-claim discipline

No negative claim ships. The `harness-schema` refusal label records a
scope fact about the landed surface's own checks, not a defect claim.

## Verdict

The Born lane now has what the gravity lane got: a standing instrument
that mechanically certifies the landed forcing surface against frozen
expectations and catches drift. The evidence ceiling of the lane's
methodology rises accordingly; the physics above it is unchanged and
still owner-audited. Independent audit still required.
