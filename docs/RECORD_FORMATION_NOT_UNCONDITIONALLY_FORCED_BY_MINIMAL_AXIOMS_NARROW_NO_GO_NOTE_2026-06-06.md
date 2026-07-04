# Record Formation Rule Is Not Supplied by the Minimal Axioms: Post-Append Scope Repair

**Date:** 2026-06-06
**Revision:** 2026-07-04 post-Record-append scope repair
**Claim type:** no_go (formation-rule/process forcing) + minimality-boundary localization
**Status:** source-side no-go scope repair; audit status and effective status remain set only by the independent audit lane.
**Primary runner:** [`scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py`](../scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py)
**Cached output:** [`logs/runner-cache/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.txt`](../logs/runner-cache/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.txt)

## Audit Context

This file keeps the historical path stable for existing citation-graph edges,
but the original June 6 no-go no longer holds as stated. The 2026-07-04
owner-approved Record append added the sentence:

> Records form.

Generic record occurrence is therefore axiom content on the current premise
surface. The live minimality boundary is narrower: the axioms do not supply the
formation rule or process.

The current front-door axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) states the four
framework axioms Lattice, Qubit, Admissibility, and Record. Its open-gates list
keeps outside the axioms the formation-rule content:

- which admissible possibility a new record locks;
- at which site;
- with what weight;
- at what rate.

It also keeps arrow, record-production dynamics, physical persistence dynamics,
time metric, and local observability outside axiom content.

## Safe Statement

The Record axiom now supplies occurrence strength only: records form. It does
not supply a law that chooses a site, chooses one admissible local possibility,
sets weights or probabilities, gives a rate or clock, defines a stochastic or
deterministic process, supplies a record-production dynamics, or asserts a
single comparable realized history.

**No-go.** The claim "the minimal axioms determine a record-formation rule or
process" does **not** hold. A theory layer that needs a specific history,
frequency, rate, clock, site selector, admissible-possibility selector,
weighting, probability kernel, or comparable record chain must supply or derive
that content separately.

## Witness Form

The no-go is an underdetermination boundary, not a no-record witness.
Consistent supplied extensions can agree that records form while disagreeing on
the downstream rule. For example, from the same open starting state and the same
local admissibility data:

1. one extension may first form a record at site `x` locking admissible
   possibility `p`;
2. another may first form a record at neighboring site `y` locking admissible
   possibility `q`;
3. two extensions may use different rates or weights for the same available
   local possibilities.

The current axiom text distinguishes records from non-records and says records
form, but it contains no selector or process that picks one of those extensions.

## No-Go Discipline (N1-N8)

- **N1 (alternative routes).** Routes from occurrence to a rule all import
  downstream content: a transition kernel, a Hamiltonian/transfer operator,
  a clock, a site selector, a weighting/probability rule, a measurement
  instrument, or comparability of realized configurations.
- **N2 (wall-independence).** Single-wall no-go: the wall is the approved
  axiom boundary excluding formation-rule/process content after occurrence is
  supplied.
- **N3 (hidden-wall scan).** The note does not use an empty-history witness or
  any claim that records fail to form. Generic occurrence is accepted as axiom
  content.
- **N4 (residual matching).** The residual is exactly formation
  rule/process/site/choice/weight/rate/clock/comparability, not occurrence.
- **N5 (rhetoric audit).** The no-go is not "records never form" and not
  "time cannot emerge." It only says the current axioms do not determine the
  formation rule or process.
- **N6 (partial-closure).** A later retained theorem, bridge, explicit
  admission, or approved primitive may supply a formation rule/process for a
  named surface. This note only prevents laundering that content into Record.
- **N7 (steelman).** The strongest opposing view is that once records form,
  a law-domain clause should force a unique formation answer. The current
  Qualification says a law's domain is supplied; it does not supply a default
  law, clock, rate, or domain for record production.
- **N8 (cross-cycle echo).** This matches the July 4 consistency sweep:
  occurrence flips to axiom content; formation rule/process remains downstream.

## The Genuine Open Piece

The open theory task is to supply or derive a formation rule/process and then
prove the desired arrow, rate, history, or weighting consequences inside that
surface. The baseline itself remains minimal.

## Boundary

- Generic occurrence is supplied by the Record axiom.
- The formation rule/process is not supplied by the minimal axioms.
- The note does not add an axiom, primitive, Tier-A admission, probability
  rule, clock, Hamiltonian, transfer operator, measurement model, state
  selector, or comparability sentence.

## Forbidden Imports Check

No observed target value, fitted selector, empirical comparator, new primitive,
or new axiom is used. The runner checks the current premise text and the
approved primitive registry for the presence of occurrence content and the
absence of formation-rule/process defaults.

## Runner Check Breakdown

Class A/B premise-surface checks:

1. current Record text contains the occurrence sentence;
2. current open-gates text names formation-rule content as outside the axioms;
3. the approved primitive registry mirrors that boundary;
4. no default site/choice/weight/rate/process/comparability selector is present
   in the axiom text;
5. two distinct supplied formation-rule witnesses can agree on occurrence while
   disagreeing on downstream rule content.

Expected `runner_check_breakdown = {A/B: N, C: 0, D: 0, total_pass: N}`.

## Honest Auditor Read

After the 2026-07-04 Record append, the old no-go against generic record
occurrence must be retired as stated. The surviving no-go is narrower and still
load-bearing: the minimal axioms do not determine the formation rule or
process. Any downstream use of a particular record history, rate, clock,
weighting, site selector, admissible-possibility selector, or comparable chain
must cite a separate retained authority, explicit admission, or approved
primitive.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py
```
