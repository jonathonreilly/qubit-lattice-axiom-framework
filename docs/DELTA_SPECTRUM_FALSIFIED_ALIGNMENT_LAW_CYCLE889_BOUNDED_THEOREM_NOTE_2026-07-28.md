# The conjecture dies, the law arrives: the DELTA spectrum falsified and replaced — Cycle 889

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed campaign-5, successor to
the Cycle-881 discovery; no axiom surface touched). Cycle 881's
DELTA-spectrum CONJECTURE stated its own falsifier; this block ran the
census the falsifier required, and **the falsifier fired at every
tier**. Cycle 881's relay-gap THEOREM — the formula DELTA(B, e) =
8B - 13 - 8e and its mechanism — is untouched. What died is the claim
that the full non-orbit period spectrum equals the DELTA set; what
replaces it is a derived exact law and a strictly larger spectrum.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle889_delta_spectrum_2026_07_28.py`](../scripts/frontier_cycle889_delta_spectrum_2026_07_28.py)
- [`frontier_cycle889_delta_spectrum_independent_check_2026_07_28.py`](../scripts/frontier_cycle889_delta_spectrum_independent_check_2026_07_28.py)

Receipt:

- [`delta_spectrum_cycle889_receipt_2026_07_28.json`](../outputs/delta_spectrum_cycle889_receipt_2026_07_28.json)
- [`delta_spectrum_independent_check_cycle889_receipt_2026_07_28.json`](../outputs/delta_spectrum_independent_check_cycle889_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted; substitution disclosed). Checker
independence is cross-context, with an INDEPENDENT period-detection
algorithm (backward membership scan + KMP failure function — never the
primary's bitmask), independent program reconstruction, and its own
tick generation. Independent audit still required.

## The census (exhaustive, no sampling)

Every clock of every corpus at B = 3..7 — 389,304 clock readings at
horizons 4,096 / 8,192 / 16,384 — with the pinned Cycle-881 checker's
own cap-free detector semantics reimplemented, horizon-abutting
readings flagged and excluded from tail claims, and a second
HORIZON-ROBUST instrument (the same detector inside every closed
quiescent stretch — 881's single quiescent window generalized to all
of them; up to 440,933 stretches per corpus). The B=4/8192 cell
reproduces the sha-pinned Cycle-881 checker census exactly ({11: 16}
over 6,480 clocks) before any new claim.

## The falsification, stated plainly

Non-DELTA periods fire with horizon-closed witnesses at every tested
tier: P=7 at B=3; P=16 at B=4; P=6 and 7 at B=5; P=6, 8, 9, 12, 13,
16, 20 at B=6; P=6, 7, 10, 15, 20, 25 at B=7 — witness substrate,
clock, lane, sigma, and transient recorded per row. **The conjecture
"the full non-orbit spectrum at every B is exactly the DELTA set" is
FALSIFIED as stated.** Of the DELTA members themselves, only 11, 19,
27 ever fire; **DELTA = 3 never fires at any B** — its firing window
carries at most 2(3 - sigma) <= 4 clean ticks, below the detector's
pinned 8-event floor, at every bank count.

## The alignment law (the replacement, derived and exact)

In the relay-quiescent regime the clock is dirty on two sigma-runs
per orbit separated by G = (2 * DELTA) mod N. A period P in
{DELTA, N - DELTA} exhibits iff the shift-exact index run

    I_max(DELTA, sigma) = max(G - sigma, N - G - sigma)

reaches P + 1, inside a CLOSED quiescent stretch of length >= 2P + 1
(the 2P bound is insufficient — checker-attacked and confirmed in all
27 worst-case cells). The law is an identity, not a fit: 580/580
cells exact in the primary (B=3..8, every edge, every admissible
sigma, both periods); the checker extends it to 2,080/2,080 in-family
cells (B=3..12) plus 1,200/1,200 randomized cells OUTSIDE the 8B-5
station family.

**Corollary 1 (spectrum shape).** Some DELTA members can NEVER align,
at any horizon, on any key: 19 at B=4; 27 at B=5; 35 at B=6; {35, 43}
at B=7; {43, 51} at B=8. The conjectured spectrum was too large in
one direction —

**Corollary 2 (the spectrum is also too small).** The ring complements
N - DELTA = 8(e + 1) are alignment-admissible on the identical
geometry. DELTA is always odd, the complements always even, so the
two families are disjoint — and complements 8, 16, 24, 32, 40, 48
were ALL observed in the census. The mechanism's own spectrum is
strictly larger than the conjecture claimed.

Honest caveat, carried in the receipt: the never-aligns corollary is a
statement about the pure relay two-run pattern. The episode census
shows 35 and 43 firing at B=7 from stretches whose dirt is NOT the
two-run structure — no contradiction, and the checker's direct
counterexample hunt over every sigma confirms the law as stated (7/7
impossibility rows survive).

## The alignment contingency (Cycle 881's named-but-not-run census)

- **B=5: RETIRED.** DELTA = 11 and 19 exhibit as horizon-closed
  readings and in thousands of mid-horizon episode readings. 881's
  invisibility at B=5 was the horizon, as it claimed.
- **B=3: NOT retired, with the obstruction computed.** 132,996 closed
  stretches swept; neither DELTA member exhibits. DELTA=3 fails the
  8-event floor everywhere; DELTA=11 is alignment-admissible only at
  sigma <= 4 and no B=3 key realizes the pure two-run pattern at such
  sigma inside a long-enough stretch — clause A2 fails, not
  alignment. 881's contingency claim was RIGHT for B=5 and WRONG in
  mechanism for B=3.

## A further repricing of 881's tails

The B=4 P=11 carriers are clean again from tick ~10,280 at the long
horizon — their "last clean tick" in 881 was a cut, not an end. The
non-orbit TAIL spectrum is a property of the (substrate, horizon)
pair and moves non-monotonically with the cut (B=3: {7} at 4,096,
empty at 8,192, {7} again at 16,384). Tail censuses should not be
consumed as substrate facts; the episode instrument is the
horizon-robust replacement.

## Controls

Falsifier-visibility: a planted P=23 (outside every predicted set) is
detected and flagged, both synthetically and grafted onto a real B=5
clock — the census can SEE a falsifier, so the falsification is not a
blind spot artifact, and neither would a confirmation have been.
Detector self-test: six known periods recovered; Thue-Morse, all-clean
and all-dirty controls refused; three seeded-wrong-period impostors
pushed past the damage. Longest closed stretches measured per B
confirm every alignment-admissible class was exercised — nothing is
reported as NOT_EXERCISED.

## Checker

Independent program reconstruction and an independent detector
algorithm; full B=5 recomputation agreeing with the primary on both
instruments at all three horizons (episode stretch count matching to
the unit, zero missed periods, zero over-counts); B=6/B=7
spot-verified on a DECLARED 25% lane subset plus all witness lanes;
independent tick generation on 10 lanes with zero cadence mismatches;
the 2P+1 stretch bound attacked and confirmed; the impossibility rows
attacked by direct counterexample hunt and confirmed. Teeth 7/7 —
including a leaked-predicted-set mutation (hiding the B=5 falsifiers)
and an undisclosed-shortened-horizon mutation, both caught by named
gates. `findings_the_primary_did_not_report` is EMPTY — the first
block this campaign where the checker added nothing.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the DELTA-spectrum conjecture at general B with its stated falsifier, and the cap-free long-horizon re-census at B=3/B=5 (Cycle 881's named frontier)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the conjecture is closed by falsification; the alignment law I_max = max(G - sigma, N - G - sigma) with the 2P+1 stretch bound is the standing replacement — carry it wherever period claims are consumed; the ring-complement family 8(e+1) is a named discovery (all observed); the episode instrument supersedes tail censuses for substrate facts; the non-two-run episode dirt at B=7 (35/43 firings) is the named open mechanism question"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the falsification carries horizon-closed witnesses at every tier with the falsifier-visibility control proving the census could have confirmed instead; the law is an exact identity on 3,860 verified cells including 1,200 outside the family; the contingency verdicts are computed per-mechanism; the checker's independent algorithm agrees in full at B=5 and on declared subsets above"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the Cycle-881 primary, checker, receipt, and both caches; the
  Cycle-879 primary; the Cycle-719 kernel PAIR (controller core plus
  its import dependency) — eight pins, all sha256 + git-blob matched
  under hard-fail preflight; only the kernel is imported (the
  substrate under test), everything else firewalled.

### Derived

- the exhaustive B=3..7 census on both instruments with the
  falsification witnesses;
- the alignment law and its exactness (580 + 2,080 + 1,200 cells);
- both spectrum-shape corollaries (never-aligning DELTA members; the
  disjoint even complement family, all observed);
- the DELTA=3 floor obstruction; the B=5 retirement; the B=3
  obstruction re-attribution (A2, not alignment);
- the tail-vs-episode repricing of 881's readings.

### Open

- the non-two-run episode dirt that fires 35/43 at B=7 — the named
  mechanism question the law does not cover;
- the even-complement family's own mechanism note (observed,
  law-admissible, not yet derived the way 881 derived DELTA);
- consumers of 881's tail cells should re-read them against the
  episode instrument.

## Verdict

The conjecture did what a good conjecture does: it named its
falsifier, and the falsifier fired — six ways at five bank counts.
What the census found instead is better than what was conjectured: an
exact two-parameter law that says which periods CAN align and for how
long, a floor that explains why the smallest gap never shows, a
disjoint even family the odd conjecture could never have contained,
and a clean split between the substrate's facts and the horizon's
artifacts. The relay mechanism of Cycle 881 survives intact; its
spectrum was simply bigger than its discoverer guessed. Independent
audit still required.
