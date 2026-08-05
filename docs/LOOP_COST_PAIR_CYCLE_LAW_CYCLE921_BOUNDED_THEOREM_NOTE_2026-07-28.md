# The tax is per pair and the meter is cycle length: the loop cost explained — Cycle 921

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane closure,
window 2b; no axiom surface touched). The loop cost that Cycles 917
and 919 measured and could not explain is EXPLAINED, as a measured
law — and it was never a loop-count law. The surviving mechanism is
the PAIR-CYCLE LAW: the tax is levied per fragment-pair, graded by
the length of the shortest pointer-through cycle joining the pair's
anchors; loop COUNT is refuted outright (ten loops can cost
nothing), and loop POSITION reduces to a binary through-the-pointer
gate already contained in the length axis. One exception — the
degree-2 chain at the high field — is reported as an unexplained
second channel, not absorbed.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle921_loop_cost_2026_07_28.py`](../scripts/frontier_cycle921_loop_cost_2026_07_28.py)
- [`frontier_cycle921_loop_cost_independent_check_2026_07_28.py`](../scripts/frontier_cycle921_loop_cost_independent_check_2026_07_28.py)

Receipt:

- [`loop_cost_cycle921_receipt_2026_07_28.json`](../outputs/loop_cost_cycle921_receipt_2026_07_28.json)
- [`loop_cost_independent_check_cycle921_receipt_2026_07_28.json`](../outputs/loop_cost_independent_check_cycle921_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). Both readings of "loop count" were run
(linear and fitted-half cyclomatic), neither silently dropped. One
receipt defect found by the checker is documented rather than hidden:
fragment pairs are keyed under two orderings (one inherited from the
pinned 917 receipt, which cannot change without breaking the
value-for-value gate; one in declared label order) — content verified
identical on all geometries by canonical comparison; downstream
readers must key on the unordered pair. Independent audit still
required.

## The design idea, and the candidate set

Nine candidate mechanisms plus five degeneracy probes, each reduced
to an INTEGER PREDICTOR that is a pure function of the graph and the
frozen partition, computed BEFORE any propagator runs — nothing is
fitted after the fact. The controlling observation: the frozen
partition rule makes every pointer neighbour the anchor of its own
fragment, so a cycle through the pointer joins two anchors, and the
anchor-to-anchor distance d in G with the pointer deleted is exactly
(cycle length - 2). The designed families sweep d at fixed pointer
degree. 32 designed geometries + the 10 pinned 917/919 anchors = 42
geometries at the three declared fields (126 declared cells), plus
64 non-claim probe cells at higher fields.

## The measurement

Restriction gates at exactly zero deviation before any new number:
917 reproduced value-for-value (12 cells, 156 rows, all deviations
exactly 0) AND the 919 anchors reproduced the same way (H4's
5 / 3 / 3 ceiling profile exact); 21/21 frozen constants
byte-verified, quote-identical to both pinned receipts; the
partition rule reproduces the memo's own six cube fragment lists.
Routes: Chebyshev/Bessel (tail 3.7e-18) vs scaling-and-marching
Taylor (remainder 8.8e-20) at 6.8e-14; dense eigendecomposition at
6.9e-14 where n <= 12; deterministic double-run with identical
receipt content digest.

**The decisive matched pairs** (lambda = 0.10): two pairs of
designed geometries are identical on EVERY statistic the machinery
tracks — sites, bonds, loops, seams, degree, max degree, depth,
components, the fragment-size multiset — and still split their
ceilings 4 against 3. No function of those counts can produce that
split; only the anchor distance differs. The seam-count and
loop-count ladders hold the pair set fixed while loop count rises —
the ceiling never moves (ten-loop QB10 pays nothing; four internal
loops pay nothing).

**Margins are wide, unlike the persistence boundary**: at the high
field the d=2 pairs clear the dependence gate by ~ +0.016 bits and
the d=3 pairs miss by ~ -0.010 bits — a factor-of-two separation on
the gate, not a razor.

## The pair-cycle law

For each pair of pointer-fragments (a, b), let d(a, b) be the
distance between their anchors in G with the pointer deleted (the
shortest pointer-through cycle containing both anchors has length
d + 2). Over the frozen certification window:

- **d = 1** (cycle length 3): removes BOTH fragments — they fail
  the content gate at every measured field;
- **d = 2** (cycle length 4, the lattice plaquette): removes the
  PAIR from mutual independence at lambda >= 0.075, but not at
  0.05;
- **d >= 3** (cycle length >= 5): costs nothing at any measured
  field;

and **max R_ind = the independence number of what survives.** A
loop-free geometry has no finite d, so the ceiling equals pointer
degree — exactly Cycle 917's reading — and 917's high-field loopy
failures are exactly its d = 2 pairs. The crossover field is
monotone in d (d = 1 over at 0.05; d = 2 crosses in (0.05, 0.075];
d = 3 near 0.15; d >= 5 never in range — probe-grade).

**Discrimination**: the law scores 42/42, 42/42, 41/42 exact at the
three fields (32/32 on every geometry this block designed); the
best rival reaches 34/42 — and it is a degeneracy probe (the
Koenig/matching bound, separated by the odd-cycle pair graphs), not
a mechanism. Loop-count is refuted in both readings; seam monogamy
predicts 1 where 5 is measured; position candidates die on QP1 and
QW1.

**The three axes, answered**: LENGTH is decisive and sets the
regime. COUNT is not decisive (six ladders, ceiling unchanged in
every one). POSITION is decisive only as the binary
through-the-pointer gate — a loop that avoids the pointer costs
nothing however many and however close (four internal loops,
ceiling intact), and once a loop passes through the pointer its
distance IS its length.

## The exception, reported

917's degree-2 chain G1 at lambda = 0.10: predicted 2, measured 1.
Its two arms sit at infinite anchor distance, so the law predicts
no cost — the drop comes from a SECOND, loop-independent channel
that grows with fragment size and field (the 4-site arms reach
C_ab = 0.0217, just over the 0.02 gate). This block does not
explain that channel; it is the named successor (running as Cycle
927). [Correction 2026-08-05, Cycle 927: "grows with fragment
size" is WRONG — the channel is flat in size beyond a saturation
step at arm length 2 (a 3-site and a 15-site chain agree to six
decimals); it grows with field and FALLS with pointer degree
(arity dilution), and only degree 2 crosses the 0.02 gate at the
high field — which fully explains this exception. The pair-cycle
law itself is untouched (this block's full designed set reproduces
at deviation exactly 0 in Cycle 927). See the Cycle-927 note.]

## Scope findings (structural, disclosed)

- Under the frozen partition rule, a site adjacent to two anchors
  is necessarily equidistant from both, so **anchor distance 2 is
  only constructible in cube coordinates**, where the memo's
  tie-break is defined: the field-graded d = 2 regime CANNOT appear
  on any tie-free geometry. A property of the frozen rule, not a
  design choice.
- A length-3 pointer cycle necessarily joins two recording sites,
  both prepared +X — structurally forced, not a confound.
- One design-extension-field cell (QC8 at 0.075) has a d = 2 pair
  not yet crossed; no such exception at either frozen field.
- lambda* for d = 2 is located to (0.05, 0.075], not bisected.
- G6 (cube27) is imported through the pinned receipts, not re-run,
  and not entered in the discrimination table.

## Checker

Fully independent: geometries rebuilt from published site/bond
lists; the partition re-derived by Floyd-Warshall with the
tie-break parsed out of the frozen memo's bytes; Hamiltonians by
explicit Pauli Kronecker products; propagation by Lanczos/Krylov
with full reorthogonalisation (residual 4.0e-16) cross-checked
against Pade scaling-and-squaring (9.3e-15); reduced states in the
opposite site-ordering convention; MIS by Bron-Kerbosch on the
complement. **Attack A, the adversarial hunt: 60 cube sub-lattices
NOT in the roster — 120/120 cells match the law, zero failures.
Attack B, model degeneracy: on the widened 102-geometry sample the
law scores 102/102 and 101/102 at the two frozen fields; best
rival 93/102; no rival ties.** 12/12 teeth fire (including Euler
and truncated-Krylov guards that flip ceilings, one-byte tampers,
and planted loop-count data flipping the survivor). Checker
position: SUPPORTED, zero disagreements. Runtimes: primary 218.5 s
(0.99 GiB), checker 11.6 s.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the loop-cost mechanism (why loops tax redundancy above the low field — measured by Cycle 917, confirmed at degree 5 by Cycle 919, unexplained)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the loop cost is the PAIR-CYCLE LAW (per-pair tax graded by shortest pointer-through cycle length: 3 kills content, 4 kills pair-independence above the low field, >=5 free; ceiling = independence number of survivors) — carry it wherever 'loops cost redundancy' is cited, and retire loop-COUNT phrasing everywhere (ten loops can cost nothing); the G1 second channel (size-driven, loop-independent) is the named successor (Cycle 927); the d=2-needs-cube-coordinates scope rule travels with the law; lambda*(d=2) bisection and the QC8 design-extension cell are small named opens"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the law is at the frozen gates and fields (the crossover-field ladder is probe-grade outside the frozen set); anchor distance 2 is constructible only in cube coordinates under the frozen tie-break (structural scope rule); the G1 chain exception is carried openly (predicted 2, measured 1 — the second channel); pair keys appear under two orderings in the receipt (documented; key on the unordered pair)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "every predictor is a pre-registered integer function of the graph computed before any propagator ran; two matched pairs identical on every tracked statistic still split, excluding all counting mechanisms at once; the law is exact on 32/32 designed geometries with the margins wide (not a persistence razor); the checker's 120-cell adversarial hunt and 102-geometry degeneracy attack leave no rival within 8 cells; both restriction surfaces reproduced at deviation exactly 0 first"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen memos (gates and partition rule, verbatim), the
  917/919 primaries + receipts (the anchors and constants
  authority, both reproduced at zero), the axiom memo (pinned);
  the G6 row via pinned receipts (not re-run).

### Derived

- the pair-cycle law with its three-tier grading and the
  ceiling-as-independence-number composition;
- the refutation of loop-count (both readings) and the reduction
  of position to the through-pointer gate;
- the matched-pair exclusion of every counting mechanism;
- the crossover-field ladder in d (probe-grade);
- the G1 exception as a second channel (named, unexplained);
- the structural scope rules (d = 2 needs cube coordinates; l = 3
  forces +X/+X).

### Open

- the size-driven second channel (G1's drop — Cycle 927, running);
- the lambda*(d = 2) bisection; the QC8 extension cell;
- the tie-free-geometry question (whether any tie-break extension
  admits d = 2 off the cube — a frozen-rule question, not this
  block's);
- the audit-lane propagation: retire loop-count phrasing wherever
  cited.

## Verdict

Two cycles measured that loops cost redundancy and left the reason
standing as a slogan; this block replaces the slogan with a meter.
The cost was never about how many loops a geometry carries — ten
can be free — and never about where they sit, except as the single
question of whether they pass through the pointer. What matters is
the length of the cycle a pair of records shares: three sites and
both records die of contamination, four and the pair merely stops
being independent once the field is high enough, five or more and
the loop is invisible. The ceiling the earlier cycles wrote as a
degree with corrections becomes one clean sentence — the
independence number of what the cycles leave alive — and the one
geometry the sentence cannot cover is promoted, not buried: the
chain's quiet second channel is already on the bench as the next
measurement. Independent audit still required.
