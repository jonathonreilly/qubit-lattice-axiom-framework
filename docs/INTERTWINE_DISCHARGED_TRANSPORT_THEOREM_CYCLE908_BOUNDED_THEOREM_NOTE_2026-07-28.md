# Eleven censuses, one ledger: the intertwine premise discharges, and covariance stops being a selector — Cycle 908

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (owner-directed Born-lane closure,
window 2; no axiom surface touched). The filed premise
P-INTERTWINE-878 is DISCHARGED by running the eleven phase-composed
scans it priced: the two covariance readings genuinely DIFFER
(witness exhibited), BL7 is READING-DEPENDENT with both resolutions
priced — and the discharge carries a sting: under the intertwining
reading, EVERY ledger-native weighting is covariant, so the
credential has no discriminating power at all.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle908_intertwine_discharge_2026_07_28.py`](../scripts/frontier_cycle908_intertwine_discharge_2026_07_28.py)
- [`frontier_cycle908_intertwine_independent_check_2026_07_28.py`](../scripts/frontier_cycle908_intertwine_independent_check_2026_07_28.py)

Receipt:

- [`intertwine_discharge_cycle908_receipt_2026_07_28.json`](../outputs/intertwine_discharge_cycle908_receipt_2026_07_28.json)
- [`intertwine_independent_check_cycle908_receipt_2026_07_28.json`](../outputs/intertwine_independent_check_cycle908_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). The import firewall admits exactly the
719 kernel (the substrate 856/863 themselves import — the 889/891
pattern), everything else AST-lifted; the double-build coverage is
honestly partial and DISCLOSED (phases {0,1,5,6} double-built by the
primary, {0,1,7} full-horizon rebuilt by the checker, the remaining
six built once at full horizon and spot-checked at 1024 — the
combined coverage stated, not implied complete). Independent audit
still required.

## Q1 — the eleven scans and the transport theorem

All eleven phase-composed scans ran at the full horizon (the
phase-0 scan reproduces the pinned 878 census digest EXACTLY —
value-for-value, the block's anchoring gate). All eleven digests are
distinct; all eleven censuses carry identical global counts (92,260
events; 164 formed; 584 never-formed; 55 mixed orbits).

**C908-T1, the transport theorem**: for every phase m, the phase-m
event set is the sigma_m transport of phase 0's — event for event —
and the occupation ledger, formation ledger, per-world counts, and
per-lane signatures all transport; the dead-wire set and safe-slot
map are phase-INDEPENDENT. **The eleven censuses are one ledger in
eleven world-labellings.** The event sets themselves intertwine —
Cycle 856's identity verbatim, now on the composed-record ledger.

## Q2 — COV-EQV, and the two readings differ

The derived form: a family {w_m} satisfies COV-EQV iff
w_m(g.e) = w_{(m+g) mod 11}(e), equivalently w_m = w_0 o sigma_m —
with COV-INV exactly the CONSTANT-FAMILY specialization. The
six-recipe table: **all six recipes (M1-M6) satisfy COV-EQV**; only
M2 and M6 satisfy COV-INV (reproducing 878 and 906). The mechanism
is computed, not inferred: every recipe is a function of the phase
ledger alone, and the ledger transports — so EVERY ledger-native
recipe intertwines automatically.

**The relationship: DIFFER_WITH_WITNESS.** M3 intertwines exactly
but is not orbit-constant (orbit-mate worlds 0 and 7 carry masses
differing by four orders of magnitude — the exhibited witness). They
separate because the ledger is not orbit-closed (55 of 68 orbits
mixed) — the composed-record analogue of 856's own non-closure.

**The second dissolution route: CONFIRMED.** M3/M4/M5 all satisfy
COV-EQV, so **BL7 does not arise under the intertwining reading.**
Both resolutions now priced: R1 (Cycle 906's, under COV-INV) — adopt
M6, price one new generator with BL6 driven to its maximum; R2
(this block's, under COV-EQV) — nothing to adopt, price zero on the
878 span, but the STRONGER credential is given up (a fixed-monitor
observer sees different mass on orbit-mates). The 906 fidelity sweep
found no axiom sentence requiring either reading; this block selects
neither.

**C908-T5, the sting**: because every ledger-native weighting
satisfies COV-EQV, the intertwining credential has NO discriminating
power — it removes BL7 by removing covariance as a selector. Filed
as the new ledger row **BL11_COV_EQV_IS_FREE** (renumbered by the
supervisor from the worker's BL9 to avoid collision with Cycle 907's
BL9_WITHIN_WORLD_DISTRIBUTION).

## Q3 — the discharge and the escape orbit's new test

- **P-INTERTWINE-878: DISCHARGED** (differ-with-witness).
- **BL7: READING-DEPENDENT**, priced both ways; M6 is one of two
  lawful resolutions.
- **The escape orbit is PHASE-STATIONARY**: the same eleven worlds,
  the same orbit index, the same census shape at all eleven phases —
  EXACTLY the invariance Cycle 856's ABSOLUTE-record orbits carry by
  definition. P-856-SHAPE is tested from a new direction and
  SURVIVES; not discharged (the predicates still differ).
- **The checker's sharpest refinement, adopted**: M6's defining
  orbit is a LATE-HORIZON object — nine of its eleven worlds first
  form near the boundary (~162,180 of 180,224) — so below the pinned
  horizon NO orbit escapes the never-formed block and **M6 collapses
  to zero**. Any future block that shortens the horizon loses M6
  entirely; the 906/907 single-orbit scope is sharper than stated.

## Checker

Genuinely independent construction (the lane keeps its census and
the MONITOR moves — a different program; agreement is a result).
Three full-horizon phases rebuilt by published rule (identity,
generator, and the most-rearranged once-built phase) — all three
digests reproduce exactly; all eleven phases spot-checked at horizon
1,024 on four transport identities. Orbits by union-find; COV-EQV
derived independently from 856's own string constants; recipes
re-instantiated from definitions. The M6 phase-behaviour attack
found no movement, with sensitivity proven (a planted broken-M6
fails with witness). Teeth 8/8, including a wrong-sign-action tooth
(tau_{-g} turns COV-EQV into a different condition — M3 flips to
FAIL, the constants survive) and a leaked-verdict tooth whose
needles are read from the primary receipt at run time so the audit
cannot self-defeat. Zero disagreements; three refinements adopted
(the coverage statement; the universality-is-negative caution; the
late-horizon finding).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "P-INTERTWINE-878 (filed by Cycle 906): 878's coded covariance is invariance, 856's landed theorem is intertwining — do they differ on the composed-record ledger, and does BL7 survive the intertwining reading?"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "DISCHARGED: the readings differ (witness M3); BL7 is reading-dependent with both resolutions priced; COV-EQV is free (BL11) so covariance is not a selector under either reading that survives scrutiny; the escape orbit is phase-stationary (P-856-SHAPE strengthened, not discharged); carry the late-horizon M6 caveat wherever M6 or the 906/907 constructions are consumed; the lane's live questions remain BL9 (within-world distribution) and BL10 (the degree-2 carrier)"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the discharge is at the pinned horizon (the late-horizon M6 finding makes horizon-dependence explicit); inherits P-NONEMPTY and the 856 phase-lift scope (byte-quoted)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the transport theorem is verified digest-wise on all eleven phases and set-wise at the generator; the phase-0 gate reproduces the pinned census exactly; the readings' difference carries an exhibited witness; the checker's construction is genuinely different (monitor-moving) and agrees; the coverage limits are stated rather than implied complete"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel (imported as substrate, disclosed); the 856
  primary/checker/note/receipt, the 863 and 878 primaries + receipt,
  the 905/906 receipts, the axiom memo (all pinned, hard-fail
  preflight; discovery sweep published);
- the 856 phase-lift scope and intertwining identity (byte-quoted).

### Derived

- C908-T1 (the transport theorem — one ledger, eleven labellings);
- COV-EQV's derived form with COV-INV as its constant-family
  specialization; the six-recipe table; the difference witness;
- the BL7 reading-dependence with both resolutions priced;
- C908-T5 (COV-EQV is free — BL11);
- the escape orbit's phase-stationarity and the late-horizon M6
  finding (adopted).

### Open

- BL9 (the within-world distribution) and BL10 (the degree-2
  carrier) — the lane's live questions, untouched here;
- P-856-SHAPE (strengthened, undischarged);
- the horizon-dependence of the whole M6 branch (now explicit).

## Verdict

The premise that two covariance readings might secretly disagree
turns out to be the door to the block's real theorem: the eleven
monitor phases never make a new world, only a new naming, and once
that is proved every ledger-built weighting intertwines for free —
which discharges the premise, dissolves the tension a second way,
and simultaneously demotes the credential that caused it. The
framework's covariance story ends where good symmetries end: true,
transported, and unable to choose anything. What can still choose is
what was left standing before: the counting inside the worlds, and
the second column nothing yet carries. Independent audit still
required.
