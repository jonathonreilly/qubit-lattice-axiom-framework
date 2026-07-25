# Physical tick/echo association, pi-ceiling, matched-ray, and causal-order tournament — Cycle 612

Date: 2026-07-22

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none.

Runners:
`scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py`
(6 PASS / 1 FAIL, exit 1 expected) and
`scripts/physical_minus_channel_certification_addendum_cycle612_2026_07_22.py`
(5 PASS / 0 FAIL).  Frozen contract (main + two addenda, each hashed before its
outputs): final SHA
`d45cad77c7d74df1951930ae796295fd8c405cc59d668f2fda98ca430b32cea1`; the
association rule and mechanism gate were hashed BEFORE the W4 mechanism
extraction was read (intermediate SHA `4b11781b…`, recorded in the contract
file lineage).

## Result up front

1. **The Cycle-451 mechanism is a COUNT-EDIT** (worker extraction, verified
   against the 451/445 runners): both clocks advance lock-step through all
   four corridor sweeps; a dedicated fifth stage applies one receiver-gated
   +/-1 one-hot clock edit (Fredkin swap network, direction = the supplied
   delay/advance law).  The 3:4 and 5:4 words are single discrete tick
   deletions/insertions, not rates.
2. **A-count cross-surface consistency (frozen rule, frozen table).**
   Quantizing the Cycle-610 rate law over the 451 window
   (n = sign(R) floor(4|R|+1/2)) reproduces the frozen expected table
   exactly: one 3:4 hit at (Q=1, s=+1); 4:4 at the Q=8 nulls, both motion
   rows, and the species row; s=-1 rows land in a distinct
   orientation-reversed class matching no 451 word.  This is genuine
   cross-surface consistency in the delay sector — and it is NOT an
   identification: the mechanisms differ (single gated edit versus
   window-quantized rate deficit), and the event association between the two
   apparatuses remains underived.
3. **Pi-ceiling discriminator (exhaustive).**  Under the principal-lift tick
   law, |R| <= pi/|theta_0| = 1.0556 for EVERY uniform-field modulation
   (checked over the full W=16 and W=64 alpha lattices, both signs; maximum
   found 1.0456).  The 5:4 advance word (|R| = 1.25) is therefore unreachable
   by any uniform-field rate shift at this species, while 3:4 is reached.
   **The two Cycle-451 response signs are mechanically distinguishable:
   delay is rate-reachable, advance is only edit-reachable.**  This is a
   falsifiable discriminator between response mechanisms, not a no-go on
   advance (451's own count-edit mechanism serves both signs).
4. **Matched-ray prediction falsified, mechanism found, law refined, chain
   closed.**  The frozen matched-ray prediction (addendum 1) FAILED: the
   0.893-purity state read through its own rays gave rate -0.3128, unlocked.
   Diagnosis: the aggregate word reweights every spectral line by
   |1 + e^{-i theta}|^2/2; at theta_0 = -2.9756 this suppresses the bound
   line by 0.0138 and amplifies near-zero-phase dust — **the plus-sign
   member of the fixed two-channel family is a dust-passing, bound-blocking
   filter for mixed states at this species** (exact eigenvectors are immune,
   which is why every Cycle-610 purified row passed).  This one mechanism
   retro-explains the Cycle-610 raw dust lock (+0.0499) and every Cycle-611
   certification failure.  Addendum 2 (frozen before output): the minus
   channel (weights (1,-1)/sqrt(2), the other member of the same fixed
   family; bound-line factor 1.986) certifies the Cycle-611 P-A (m=16, k=4)
   state with RAW rays (fine rate -0.4735797 vs root -0.4735774), certifies
   the exact eigenvector, still refuses the raw source (rate -0.2697:
   preparation remains necessary), and the channel is selected by a derived,
   local, spectral-data-free rule — run both signs, keep the one passing
   lock + convention independence (CT-1''); contact-off selects nothing.
   **Composed chain now certified end-to-end: raw source -> P-A filter
   (postselected, success 0.0070, resource-accounted) -> certificate-selected
   minus channel -> certified intrinsic clock at the spectral rate.**  The
   plus-channel FAIL rows of 610/611/612 stand unrepaired.
5. **Causal-order bridge (finite executable).**  Per-device total order from
   local head markers plus shared co-registrations: consistent sequential
   co-registrations are admitted and the joint predecessor relation is
   acyclic; a shared event that would precede an earlier shared event in one
   device is refused by a locally checkable cross-order rule; forcing
   inverted identifications past the rule creates a cycle that the decoder
   detects as undefined.  This is the finite declared-code form of the
   spatial-to-temporal bridge; the unbounded statement (bounded-speed signal
   exchange can never present a lawful inverted co-registration) is posed as
   the exact open theorem.

## Interface contract for the physical-M2 side (Cycle 608 / PR #5523)

Their side supplies a physical matter-caused endpoint predicate and a
reversible deletion-sensitive predecessor/clock interval packet.  For those
objects to feed this law:

1. **Endpoint predicate**: bounded local support; matter-caused (contact
   deletion kills it); oriented (exposes the crossing direction);
   duplicate-safe (at most one certificate per crossing); channel-sign
   declared per device (the two-channel relative sign is load-bearing
   apparatus — see the pi-ceiling/channel findings; the certificate-based
   selector CT-1'' may be compiled as the selection mechanism); convention
   declared (T1 or T2; fixed per device).
2. **Interval packet**: rotor increments exactly once per admitted
   certificate; carry receipt exactly on K15 -> K0; predecessor = the local
   head marker (never host bookkeeping); decode returns undefined on lineage
   gaps (never zero); binder deletion blocks the opportunity; reversibility
   with visible deletion signatures.
3. **Admission ports**: actuality, admissibility, and law-domain tokens must
   be explicit ports, not hardwired — the supplied middle stays visible.
4. **Acceptance tests**: the device word must pass lock + convention
   independence, and its rate must match the species' spectral root within
   2/(window); two-device use requires a co-registration surface honoring the
   cross-order refusal rule above.  The Cycle-610/611/612 runners are the
   executable acceptance harness.

## Composition-law assembly (from retained receipts)

One law, all clauses already executed: additivity over predecessor-linked
concatenation (610); orientation antisymmetry (610); reparameterization
independence = tick-unit convention freedom AND q-freedom of every decoder
(610, refined by CT-1''); reference independence = preparation independence
on the certified domain (610/612); recurrence across rollovers (610);
unequal profiles = species row (the ratio of the two spectral roots).  A
matched-profile ratio of 1 is a calibration identity; every nontrivial
relation obtained so far requires exactly one controlled asymmetry — motion
(K), field value (Q, s), or species (beta) — and this trichotomy is the
required-additional-observable answer to the compute-side question 2.

## Verdict classification (compute-side question)

The construction is **a certified operational relational-duration candidate
with derived nontrivial clock-ratio laws** — more than calibration, less than
proper time: it is a protected causal-interval candidate.  Missing for proper
time, exactly: the occurrence/admission middle (actuality + permanence), the
empirical unit, the unbounded causal-order theorem, and continuum/Lorentz
control.  Record permanence is NOT derived anywhere in the retained
science — every finite protected packet retains an accessible inverse; the
611 note's scoping section types this precisely.

## Supplied / derived / open

Supplied: the A-count window (4, from the 451 apparatus), the association
rule's rounding convention, the channel family (fixed by 602; sign selected
by CT-1''), the admission tokens, and everything inherited (see 610/611).
Derived: the count-edit mechanism fact (W4, verified); the frozen A-count
table; the pi ceiling (exhaustive); the channel reweighting law and CT-1'';
the end-to-end certified chain; the finite causal-order results.  Open: the
tick-to-echo event association on one shared code (the A-count consistency
is necessary, not sufficient); the unbounded acyclicity theorem; a
deterministic preparation; the occurrence middle; the advance-sector
mechanism on the tick side.

## N1-N8 (abbreviated)

N1: attempted — A-count (consistent, delay sector), matched-ray plus channel
(falsified), minus channel (positive), causal-order finite bridge (positive),
adversary refusal (positive).  Open: shared-code association, unbounded
light-cone theorem, advance-sector tick mechanisms.  `< 5` falsified: no broad
negative.  N2: channel selection, association, occurrence, permanence, and
order-consistency are directionally distinct.  N3: rounding convention,
window 4, channel family, and all tokens are explicit.  N4: the one FAIL row
is the plus-channel matched-ray prediction; it is not cited against the
minus-channel law.  N5: finite L9/K=0/declared-code scope throughout; the pi
ceiling is exhaustive over the named lattices only, with the analytic bound
stated.  N6: live paths — shared-code association runner; compile CT-1'';
deterministic preparation.  N7: steelman — a reviewer should press that
A-count consistency without a shared-code association is circumstantial; the
612 verdict already concedes exactly that.  N8: 610 exposed the boundary,
611 falsified two preparation priors, 612 falsified the matched-ray prior,
found the channel mechanism, and closed the chain — three consecutive
preregistered falsifications each converted into a derived law refinement.

## Interpretation firewall

A count word is not time.  A-count consistency is not identification.  The
pi ceiling is a property of the candidate tick law.  The channel sign is
apparatus within the fixed 602 family, selected by certificates, not by
spectral data.  Shared co-registrations are candidate events.  An admitted
cell is a conditional candidate Record.  No proper time, lapse, redshift,
energy, Lorentz covariance, Born meaning, or actual Record is claimed.

## Cold verification

```text
main runner:     RESULT 6 PASS / 1 FAIL (matched-ray prior falsification; exit 1 expected)
addendum runner: RESULT 5 PASS / 0 FAIL, exit 0
transcripts:     outputs/physical_tick_echo_association_causal_order_tournament_cycle612_cold_2026_07_22.txt
                 outputs/physical_minus_channel_certification_addendum_cycle612_cold_2026_07_22.txt
receipts:        the two matching *_receipt_2026_07_22.json files
contract:        final SHA d45cad77c7d74df1951930ae796295fd8c405cc59d668f2fda98ca430b32cea1
W4 extraction:   scratchpad artifact, SHA-256
                 3b3162d42f8f2dc6281136d62b1a8cc66abdcfb331ea178489726bb4d26c62f0
```

## Dependency citations

This runner loads and byte-pins
[Cycle 610](PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md)
and [Cycle 611](PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md),
and through them the accepted upstream surfaces
[Cycle 578](PHYSICAL_INTRINSIC_CONTACT_BOUND_MOVING_TRANSITION_TOURNAMENT_CYCLE578_NOTE_2026-07-22.md)
and [Cycle 583](PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_CYCLE583_NOTE_2026-07-22.md).
