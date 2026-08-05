# Five behaves like six: the field-ceiling threshold is degree 5, by less than a thousandth of a bit — Cycle 919

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane closure,
window 2b; no axiom surface touched). The Cycle-917 ladder's named
successor measurement is executed: four degree-5 geometries — the
star, two tree readings, and a controlled one-face deletion of the
cube — under the frozen certification gates verbatim, at all three
fields. Degree 5 certifies at the 0.10 field on every geometry.
On integer degrees the 917 bracket's interior is thereby exhausted:
the smallest degree certifying at the frozen high field is FIVE.
The result travels with its own margin honesty — the YES/NO split
at the boundary is decided by about eight ten-thousandths of a bit.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle919_degree_five_2026_07_28.py`](../scripts/frontier_cycle919_degree_five_2026_07_28.py)
- [`frontier_cycle919_degree_five_independent_check_2026_07_28.py`](../scripts/frontier_cycle919_degree_five_independent_check_2026_07_28.py)

Receipt:

- [`degree_five_cycle919_receipt_2026_07_28.json`](../outputs/degree_five_cycle919_receipt_2026_07_28.json)
- [`degree_five_independent_check_cycle919_receipt_2026_07_28.json`](../outputs/degree_five_independent_check_cycle919_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). The spec's "at least 2 branches of
depth 2" tree family is run at both extremes (exactly-2 and all-5),
neither privileged. The checker CORRECTED the primary's rationale
for the 0.075 design extension — the primary called it "the
discriminating cell"; it is not (see below) — and the corrected
reading STRENGTHENS the claim. Independent audit still required.

## The four geometries

- **H1** `star6` = K_{1,5}: 6 sites, depth 1, loop-free.
- **H2** `tree16`: five branches, all of depth 2, branching factor
  2 — 16 sites (2^16 full space), the 917 tree family's degree-5
  member.
- **H3** `tree10d5`: five branches, exactly two of depth 2 — 10
  sites.
- **H4** `cubeminus10`: 917's cube with the -z face deleted — 10
  sites, degree 5, FOUR loops: a controlled degree 6 -> 5 deletion
  at fixed loop number.

Fragments by the frozen rule (one per pointer neighbour; the
917-verified cube tie-break, firing four times on H4 only).
Full-space exact evolution throughout — route A Chebyshev with a
Bessel tail bound; route B a scaling-and-marching Taylor propagator
with a factorial remainder bound (algorithmically disjoint — the
only feasible second route at 2^16); route C dense
eigendecomposition where n <= 12.

## The measurement: degree 5 certifies at 0.10

**All twelve cells YES** — 0.05, the 0.075 extension, and 0.10, on
all four geometries. Five behaves like six, not like four. The four
geometries agree at every field while n runs 6 to 16, depth 1 to 2,
and loops 0 to 4: degree is isolated from every confound the 917
checker named. The graded field ceiling is now complete and
non-decreasing — **degree 2 -> 0.05; degrees 3-4 -> 0.075;
degrees 5-6 -> 0.10** — with its one jump between degree 4 and
degree 5. On integer degrees, (4, 5] is the singleton {5}: **the
threshold is located, not bracketed.** [Qualification 2026-08-05,
Cycle 926: the located threshold is GATE-FRAGILE — it survives only
for the C_ab gate in [0.0191673, 0.0207835) (relative half-width
3.92%) and 6 of 32 persistence/deadline combinations; just below
the band the threshold is 6, and at the upper endpoint the
degree-4/degree-5 cut stops being clean. The exact sweep also
re-scopes the carrying statistic: certification at the 0.10 field
follows the unique conjunction "pointer degree >= 5 AND fragment
count >= 3", with degree and fragment count co-varying on this
note's family. The margin honesty below was the right instinct;
the band is now exact. See the Cycle-926 note.]

**The ceiling law confirmed at degree 5**: max R_ind = 5 on all
three loop-free geometries at all three fields, and on the loopy H4
at 0.05; H4 drops to 3 at 0.075 and 0.10 — loops still cost
redundancy above the low field, exactly the 917 pattern (while H4
still CERTIFIES at 0.10: the ceiling drop and certification are
different things). theta_A at events 0.4999-0.5029; C_ab at the
0.10 events 0.0094 (loop-free) and 0.0160 (loopy) against the 0.02
gate; xi_reg = 1 on all cells, as everywhere in this lane.

## How narrow this is (measured, not asserted)

The threshold is a PERSISTENCE boundary — every geometry of degree
>= 3 reaches R_ind >= 2 by the deadline; only the three-sample
persistence flag separates them. The tightest NO (917's degree-4
tree13) misses its third sample by **0.00078 bits** of C_ab on its
binding pair; the tightest YES (the degree-5 cubeminus10) clears
the same sample by **0.00083 bits**. A gate moved by ~2e-3 bits
moves the threshold. Per-sample margins are published for every
geometry; a gate-robustness sweep is the named hardening.

## The checker's findings (three, all adopted)

1. **The 0.075 extension is not load-bearing — and the primary's
   rationale for it was wrong.** At 0.075 EVERY geometry of degree
   >= 3 certifies; it is the last field where degrees 3-4 still
   pass, not the first where they fail. The threshold is decided
   entirely at **lambda = 0.10, a frozen certified field**, against
   917's degree-4 NO cells at the same frozen field. The 0.075
   column can be dropped from the claim surface with the verdict
   untouched — the corrected reading strengthens the result.
2. **Grade split.** The THRESHOLD is frozen-grade (decided at
   frozen fields only). The graded CEILING TABLE is
   diagnostic-grade — the 0.075 and 0.125 values that give it
   resolution are outside the frozen field set. The two are not to
   be cited at the same grade.
3. **Cross-degree controls** (beyond the primary's brief): H3 vs
   917's G3a — both 10 sites, differing only in degree — YES vs
   NO. H4 vs 917's G4 — both 4 loops, differing only in degree —
   YES vs NO. Neither system size nor loop count can carry the
   split.

## Gates, falsifiers, checker

Pins 12/12 (sha256 + git blob); 21/21 frozen constants
byte-verified and quote-identical to the pinned 917 receipt; the
partition rule reproduces the frozen memo's six cube lists;
**Cycle 917 reproduced value-for-value — 12 cells, 156 rows,
maximum deviation exactly 0** in chi, C_ab, theta_A, H_Z, verdicts,
events, witnesses, the R_ind ledger, xi_reg, and max R_ind; all six
of the 917 checker's 0.075 probes reproduced before any new 0.075
number was produced. Route A vs B at 3.4e-14, A vs C at 3.2e-14;
Taylor remainder 2.1e-20; double-run digests identical; orbit
reduction exact on H1. Falsifiers live: a planted certification on
a real 917 NO cell flips to YES; suppressed independence flips a
real YES to NO; every degree-5 geometry returns NO at 0.125; the
under-converged-propagator guard fires (first-order Euler, state
deviation 0.415, verdict flips). Checker: fully independent
machinery (sparse Pauli-kron Hamiltonians, expm_multiply intervals,
its own MIS and partitions rebuilt from the spec bytes, every
statistic recomputed from adjacency); **13/13 claims survive,
11/11 teeth fire**; maximum deviation vs the primary: chi 2.0e-13,
C_ab 4.0e-14, theta_A 4.4e-14. Runtimes 8.0 s and 9.1 s.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the degree-5 geometry (the 917 bracket's interior — the named successor measurement): locate the field-ceiling threshold inside (4, 6]"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the threshold is LOCATED at degree 5 (integer degrees exhaust (4, 5]); the ceiling law R_ind = pointer degree confirmed at degree 5 with the loop cost reproduced (H4: 5 -> 3 above the low field); carry the margin honesty (the boundary is decided by ~8e-4 bits; a ~2e-3-bit gate shift moves it) and the grade split (threshold frozen-grade, ceiling table diagnostic-grade) with every citation; named successors: the loop-cost mechanism (running as Cycle 921), the gate-robustness sweep, a geometry separating the four collapsed degree statistics"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the threshold claim is at the frozen gates and frozen fields; the graded ceiling table is diagnostic-grade (0.075/0.125 outside the frozen field set); 'degree' on this family means the four collapsed statistics jointly (pointer degree, max degree, branch count, fragment count — 917's correction carried); the G6 cube row reaches the ladder through pinned imports and was recomputed in neither cycle"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "every cell is dual-implemented with checker agreement at 2e-13 on fully independent machinery; 917 is reproduced value-for-value (deviation exactly 0) before any new number; the threshold is decided at frozen fields against frozen-field NO cells; the cross-degree controls isolate degree from size and loops; the persistence margins are published per sample"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen memos (the gates, verbatim), the 914-917
  primaries + receipts (the 917 receipt as the constants authority,
  quote-identical), the axiom memo (pinned); the G6 cube row via
  the pinned 914/917 receipts (imported, not recomputed).

### Derived

- the twelve degree-5 cells (all YES) and the located threshold
  (degree 5, frozen-grade);
- the completed graded ceiling table (diagnostic-grade);
- the ceiling-law confirmation at degree 5 with the loop cost
  reproduced;
- the persistence-margin quantification of the boundary
  (0.00078 / 0.00083 bits);
- the cross-degree controls (size and loops excluded as carriers).

### Open

- the loop-cost mechanism (why loops tax redundancy — measured
  twice, unexplained; Cycle 921 running);
- the gate-robustness sweep (the ~2e-3-bit fragility of the
  boundary);
- a geometry family separating pointer degree, max degree, branch
  count, and fragment count (collapsed by the partition rule on
  every family measured so far);
- the G6 fresh recomputation (never done in 914, 917, or here).

## Verdict

The ladder's missing rung turns out to hold the whole answer: four
geometries that share nothing but their degree — a star, two trees,
and a wounded cube — certify in unison at the field where every
degree-4 geometry dies, and the bracket the last cycle could only
name collapses to a single integer. The law underneath repeats for
the third time at a new degree: branching sets the ceiling, loops
tax it, and the field a pointer can survive climbs with its
connectivity. What keeps the result honest is how thin the edge is
— less than a thousandth of a bit separates the last NO from the
first YES — so the threshold is real, located, and carried
everywhere with the width of the razor it balances on. Independent
audit still required.
