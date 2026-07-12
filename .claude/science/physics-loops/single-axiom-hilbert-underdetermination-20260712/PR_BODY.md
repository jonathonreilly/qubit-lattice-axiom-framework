## Science block

This block replaces the class-E “single Hilbert axiom” compression with a
polarity-safe theorem split:

- `docs/SINGLE_AXIOM_HILBERT_NOTE.md` remains the existing positive dependency
  hub and now proposes a bounded exact theorem: disjoint factor algebras
  commute; supplied graph support, Hermiticity, and Born readout imply exact
  support recovery, unitarity, and `I_3=0` respectively.
- `docs/FINITE_FACTORIZED_HILBERT_PHYSICAL_SELECTOR_NONUNIQUENESS_NO_GO_NOTE_2026-07-12.md`
  is a new zero-inbound leaf `no_go`: under one fixed expansion signature, the
  same factorized Hilbert base admits nonisomorphic graphs, unitary and
  dephasing CPTP semigroups, and `p=2` and `p=4` normalized contextual
  readouts. The base/type surface does not uniquely distinguish one member as
  physical.
- The former invalid Test 4 localization comparison is deleted; its two
  participation ratios used different sample spaces and normalizations.

Independent audit remains required before either row receives an effective
status. This PR does not carry an audit verdict, generated audit ledger, or
repo-wide authority-surface edit.

## Quoted repair target

> The runner numerically demonstrates consequences after constructing
> Hamiltonians with selected support, choosing Born-rule probabilities, and
> comparing unitary/Lindblad examples, but it does not derive those structures
> from the single Hilbert-space axiom. The conclusion mainly repackages several
> specifications into the phrase "local tensor product Hilbert space" and then
> reads graph/locality/unitarity back out of the added Hamiltonian data. This
> is a definitional compression rather than a first-principles derivation from
> the stated axiom.

The same-path theorem now keeps every supplied object on the premise side of
the implication. The leaf closes unchanged-base selector uniqueness
negatively with explicit same-base counter-expansions.

## Artifacts

- [Handoff](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/HANDOFF.md)
- [Trace gate](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/TRACE_GATE.md)
- [Claim-status certificate](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/CLAIM_STATUS_CERTIFICATE.md)
- [Assumptions/imports](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/ASSUMPTIONS_AND_IMPORTS.md)
- [Route portfolio](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/ROUTE_PORTFOLIO.md)
- [No-go discipline](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/NO_GO_DISCIPLINE_CHECKLIST.md)
- [Review history](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/REVIEW_HISTORY.md)
- [Same-path runner output](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/RUNNER_OUTPUT.txt)
- [Leaf no-go runner output](.claude/science/physics-loops/single-axiom-hilbert-underdetermination-20260712/NO_GO_RUNNER_OUTPUT.txt)

## Verification

- `python3 -m py_compile` on both changed runners: PASS
- `python3 scripts/frontier_single_axiom_hilbert.py`: 10/10 PASS
- `python3 scripts/finite_factorized_hilbert_physical_selector_nonuniqueness_2026_07_12.py`: 21/21 PASS
- independent SymPy/manual checks: Pauli-word support, complex `I_3`, Kraus
  completeness, Choi positivity, full-superoperator semigroup composition,
  purity loss, exact readout fractions, and factor commutators: PASS
- runner output captures compared byte-for-byte: PASS
- vocabulary lint and `git diff --check`: PASS
- review-loop: code/math PASS; physics/import/Nature PASS; N1-N8 PASS;
  governance PASS
- full 16-stage audit pipeline plus `audit_lint.py --strict` after rebase onto
  `origin/main`: PASS with no errors
- validation rows: `single_axiom_hilbert_note` is ready `bounded_theorem`, high
  criticality; the new `no_go` is ready, leaf, zero inbound; both depend only
  on `minimal_axioms`

## Imports retired or exposed

No observation, fit, empirical value, literature value, or unit convention is
load-bearing. The formerly hidden graph, dynamics, and readout selectors are
now explicit conditional inputs/open derivation obligations. `minimal_axioms`
is the sole registered comparison dependency.

## Remaining blocker and next action

The bare Hilbert surface does not positively derive a physical graph,
dynamics, or Born readout. A positive program needs explicit retained bridges
on a richer premise surface. The immediate next action is independent audit of
the bounded same-path theorem and the separate zero-inbound no-go. Do not merge
this PR or treat author-side status as audit ratification.
