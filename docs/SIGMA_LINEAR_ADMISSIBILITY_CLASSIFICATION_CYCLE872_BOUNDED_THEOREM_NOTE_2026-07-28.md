# Sigma-dependence in a stipulated response-constructor grammar factors through the sector trace — Cycle 872 (exact support; grammar exhaustiveness and physical identifications open)

Date: 2026-08-03

Authority: none

Audit: unset

Status: exact algebraic support (demoted at review-loop iteration 1,
2026-08-08, because the grammar-exhaustiveness lemma and two physical
identifications are open and the submitted census contained a count
error — see the review record below for what was demoted and why; one
worker-authored primary and one independent checker spec'd to refute;
no axiom surface touched). The filename's historical token is
provenance only; the claim type below governs.

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
identity (below). Review-loop iteration 1 fixes applied 2026-08-08.
Independent audit still required.

## The claim, exactly

At the declared scope — the k <= 2 source family on the two-endpoint
held L=6 surface (72 single-source + 1,296 two-source = 1,368 members),
three sectors, three axes / six signed directions, the sector-weight
ladder d = 1..6 carried as an EXPLICIT SCOPE INPUT (no source supplies
a weight ladder), and the stipulated traceless recoil ledger
`(-2d, +d, +d)` — this package stipulates a constructor GRAMMAR as
data: the grading `G_sigma = Pi_tracefree + sigma * Pi_conformal` at
powers one and two, the endpoint exchange R, four endpoint premaps
{id, R, I+R, I-R}, eight index-subset contractions, five tensor-square
pairings, source degree at most two, closed under rational linear
combination and product. That grammar generates 384 objects (64 linear,
320 quadratic, 3,200 scalar components); the classified object is the
generated ALGEBRA, not a generator list.

The grammar is then filtered by two response-class covariance
conditions, both DECLARED AS DATA in the primary: direction-reversal
parity (working label K1) and endpoint-exchange equivariance (working
label K2). 344 of 384 generators survive (the 40 failures are all
endpoint-transfer objects with mismatched premaps). The working label
"admissible" in the runners' payloads abbreviates exactly this
stipulated filter; it does not invoke and is not derived from the
framework Admissibility axiom, and no theorem is claimed that the
filter characterizes physically permitted response objects. The
theorem is stated for the direction-reversal-parity and
endpoint-exchange-equivariant subset of the stipulated grammar.

**The exact result.** Over all 470,592 (member, filtered-generator)
pairs: ZERO sigma-sensitive; every filtered generator is a
sigma-CONSTANT on the declared family, and constants close under sums
and products, so the blindness extends to the whole generated algebra
at this stipulated scope. The six response objects stipulated by the
reviewed Cycle-868 package reproduce exactly as named class members,
so the classification applies to them; nothing beyond that containment
is inherited. The census of escape-shaped objects, taken EXHAUSTIVELY
over every declared member under both declared conformally loaded
probe ledgers, finds 180 of 344 filtered generators genuinely
sigma-odd on a loaded source (the originally submitted 162 was a
sample-census error, corrected at review).

Three items are OPEN and are NOT established by this package:

1. the identification of the stipulated objects and constructors with
   the Cycle-749/768/812 response lineage (that lineage is UNLANDED on
   `origin/main` at review time and is cited as provenance only — its
   runners are NOT inputs of this package);
2. the identification of the grading sign `sigma` with the physical
   conformal-mode sign of the emergent-gravity lane;
3. the grammar-exhaustiveness lemma: no proof is offered that every
   physically relevant response object lies in the stipulated grammar.
   This lemma is TARGET-EQUIVALENT to the escape-route question itself,
   and the checker exhibits a concrete outside-grammar construction (a
   trace-free-channel grading) that sees sigma while the conformal
   source channel is zero, so the boundary is real, not hypothetical.

Because of items 1-3, this package makes NO statement about physical
escape routes, NO statement about the physical conformal sign, and NO
statement about any response surface beyond its own stipulated one.

## The mechanism (the informative part)

Within the stipulated grammar the dependence structure is one exact
identity, supervisor-verified by hand and machine-verified on every
member under all three ledgers:

    sector_contract(G_sigma S) = 3 sigma * conformal(S)
                               = sigma * (sector trace of S),

since the trace-free channel sector-sums to zero. The sector
contraction of the graded source is a DECISIVE WITNESS — sufficient
for the only-if direction, with no uniqueness claimed (179 further
filtered generators are sigma-odd on a loaded source, and products of
the witness with sigma-even elements give more). Hence, INSIDE THE
GRAMMAR: every element of the generated algebra is blind to sigma if
and only if the source's conformal channel vanishes. The stipulated
ledger's sector sum `-2d + d + d = 0` is verified as the zero
polynomial with d a formal indeterminate, so every declared source has
zero conformal channel at every weight, which is the entire mechanism.
Within the grammar, the two boundaries named by the reviewed Cycle-868
note are therefore not independent — the escape-(b) shape sees sigma
only through a nonzero conformal channel, which is boundary (a). No
physical escape-route collapse follows, because of open item 3.

## Refinement of the general mechanism reading

The reviewed Cycle-868 structural sigma-evenness mechanism, stated for
its six objects, is correct and unaffected. Read as a GENERAL claim
about quadratic contractions it would be too broad for this wider
stipulated grammar, in two separable ways found here: per-sector axis
contractions are sigma-odd already at equal grading power
(sector-orthogonality, not quadratic degree, is what forces evenness
where it holds), and mixing grading powers one and two admits sigma^3
terms (top measured degree 4 on a loaded source, above the degree-2
bound that held for the six objects). The corrected general reading,
valid inside this grammar: evenness holds exactly where a sector sum
kills the trace-free/conformal cross terms.

## Checker design and teeth

Integer-only arithmetic in hard-wired sigma worlds (no polynomial
algebra shared with the primary), exactness recovered by finite
differences. The LINEAR refutation hunt is exhaustive: all 1,368
declared members against 1,344 wide-class features (seven premaps,
grading powers one through four, no covariance filter — nothing the
primary filtered out can hide), 1,838,592 exact comparisons, 0
sensitive. The quadratic sweep (7,230,720 product comparisons) runs on
a DECLARED EIGHT-MEMBER SAMPLE and the degree-<=5 sweep on 600 random
elements; both are corroboration on top of the linear exhaustion, not
exhaustion. The escape-shape census is EXHAUSTIVE (2,736 member-ledger
evaluations in four sigma worlds) and independently reproduces 344
filtered and 180 sigma-odd generators. The exact loaded sigma degree
is MEASURED from the finite-difference table with an identified
witness (generator, member, component), never assumed from the bound
being checked. Adversary controls: a detuned ledger fires on 608
features; a planted off-grammar sigma-visible object is caught on 456
features across 3 members on the stipulated ledger; a fabricated claim
block is caught on 6 comparison fields. Since review-loop iteration 1
every refutation quantity is GATING: any hunt sensitivity, any
declared-family sensitive pair, any claim disagreement, or any verdict
mismatch fails its certificate, and eight exit-path drills push
fabricated counterevidence through the exact predicate that decides
the terminal line and the process exit status. The primary likewise
gates its full submitted boundary (zero sensitive pairs, generator
constancy, algebra closure, the nonempty 180-member witness class,
zero declared-family escape sensitivity, and the intended verdict);
every alternative outcome exits nonzero.

## Review record (why this is not a no-go)

The original packet presented this result as a hardened wall with a
compact N-gate checklist, claimed the "landed" admissible response
algebra, said the block SUBSUMES the Cycle-868 wall, and concluded
that Cycle 868's two physical escape conditions collapse. Review-loop
iteration 1 (2026-08-08, Sol reviewer) found: the no-go discipline
FAILS at the claimed physical scope (the attack routes were nested
variants of one constructor route; the hidden-condition inventory
omitted the stipulated scope and filter inputs; the steelman —
something outside the grammar sees sigma — is actually CONSTRUCTED by
the checker rather than defeated); the grammar-exhaustiveness lemma is
target-equivalent and open; the claimed 162 odd generators was a
sample-census error (exhaustive count: 180); both runners' decisive
gates were fail-open; the pinned Cycle-868 ancestry was superseded by
its reviewed landing; and the "admissible" label conflated a
stipulated filter with the framework Admissibility axiom. The claim is
therefore held at exact algebraic support on the stipulated grammar
with the three open items named above. The original checklist is
preserved in git history; it must not be cited as a passed no-go gate.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "868 escape (b): a response object linear in the endpoint exchange ... could see sigma"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: support
next_trace_action: "carry the within-grammar factorization as upstream support; the live work is the three open items (object lineage; physical-sign carrier; grammar exhaustiveness, which is target-equivalent to the escape-route question), and the conformal channel's provenance is a separate open question"
```

## Status fields

```yaml
actual_current_surface_status: support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite stipulated grammar classified exhaustively in exact arithmetic with fail-closed gates binding the submitted boundary; the escape-shape census exhaustive over every declared member under both loaded ledgers; the witness identity a one-line sector-sum computation; the grammar-exhaustiveness lemma and both physical identifications are open, so nothing beyond exact support on the stipulated surface is claimed"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/frontier_cycle872_admissibility_independent_check_2026_07_28.py
```

The `packet_helper_runner` line is the machine-readable declaration
that the independent checker is a claim-scoped, co-load-bearing packet
source: no audit packet generated for this note is complete without
that runner, and at landing the citation-graph builder's explicit
packet-helper table must carry the matching entry (see the landing
conditions below).

## Imports, declared scope, provenance, derived, open

### Imports (load-bearing)

- the reviewed Cycle-868 exact-support package, whose source authority
  is
  [`RESPONSE_SURFACE_CONFORMAL_SIGN_CENSUS_CYCLE868_NARROW_NO_GO_NOTE_2026-07-28.md`](RESPONSE_SURFACE_CONFORMAL_SIGN_CENSUS_CYCLE868_NARROW_NO_GO_NOTE_2026-07-28.md):
  its runner and pinned stdout are sha-pinned by both runners at the
  blobs landed on `origin/main` after its review fixes, its six
  stipulated objects are re-derived in-file and matched into the
  class, and its two open identifications are carried forward
  unchanged (they are open items 1 and 2 above);
- nothing else from other rows: the source family, ledger, grading,
  premaps, contractions, pairings, and both covariance filters are
  STIPULATED IN-FILE in the two linked runners; stdlib exact
  arithmetic only.

### Explicit scope inputs and conventions

- scope inputs (theorem hypotheses): held edge L=6; sector-weight
  ladder d = 1..6 (cardinality matching the held edge; no cited
  supplier); source multiplicity k <= 2; two endpoints; three sectors;
  three axes / six signed directions; the traceless recoil ledger
  `(-2d, +d, +d)`; the grading channel fixed to the conformal
  projector; grade powers one and two; source degree at most two;
  rational closure;
- declared response-class conditions (stipulations, not axiom
  consequences): direction-reversal parity (K1) and endpoint-exchange
  equivariance (K2), whose well-posedness on the family is re-derived
  in-file while their content remains declared data;
- naming convention: "admissible" in runner payloads is the working
  label for this filtered subset only (see the claim section).

### Provenance context (non-load-bearing)

- the Cycle-320 unit-weight recoil ledger and Cycle-322 endpoint
  exchange, which inspired the stipulated definitions (no longer
  runner inputs);
- the Cycle-749/768/812 response-object lineage, which inspired the
  constructor set (UNLANDED on `origin/main` at review time; its
  runners were removed from both runners' input closures at review);
- the sign-status note (the one-admission reduction), which frames why
  the sign question was asked.

### Derived

- the 384-generator enumeration and the 344-member covariance-filtered
  subset (under the stipulated filter, as data);
- the blindness of the generated algebra on the declared family
  (470,592 pairs, zero sensitive, constants closed under the algebra
  operations);
- the within-grammar factorization through the sector trace via the
  decisive witness identity, and the within-grammar iff;
- the exhaustive escape-shape census (180 of 344) and the corrected
  general-mechanism reading (sector-orthogonality, not degree).

### Open

- the three open items named in the claim section (object lineage;
  physical-sign carrier; grammar exhaustiveness — the last being
  target-equivalent to the escape-route question);
- the conformal channel's provenance — why the ledger is traceless is
  a question this package does not touch;
- nothing in this package constrains the sign's value.

## Landing conditions

Outstanding at landing (outside this PR's frozen file set), as hard
landing conditions: (a) add to `EXPLICIT_PACKET_HELPER_RUNNER_PATHS`
in `docs/audit/scripts/build_citation_graph.py` the claim-scoped entry
mapping this note's claim id
`sigma_linear_admissibility_classification_cycle872_bounded_theorem_note_2026-07-28`
to
`["scripts/frontier_cycle872_admissibility_independent_check_2026_07_28.py"]`,
so the generated packet's helper closure carries the checker; (b)
co-land the citation-graph manifest acknowledgment for this note's
node, regenerated on the actual landing tree. Do not spend an audit
seat on this row before both are done.

## Verdict

On the stipulated surface the result is exact support: no element of
the covariance-filtered constructor algebra separates the grading sign
on the declared family, the blindness closes over the generated
algebra, and every escape-(b)-shaped object inside the grammar reads
sigma only through the source's sector trace, which the stipulated
ledger annihilates identically in the formal weight. The decisive
witness makes the mechanism one line. This package makes no statement
about response objects outside its stipulated grammar (the checker
constructs one that sees sigma), no statement about the physical
conformal-mode sign, and no statement about the unlanded response
lineage; those are the open items named above. Independent audit still
required.
