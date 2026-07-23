# Record/Born admission-law discriminator harness tournament — Cycle 679

Date: 2026-07-23. Authority: none. Audit: unset. Contract SHA
`8b968ceb7c32b9350869c8f65126aa3e45388d8d48f54b2a00c66f43cf03d966` (in-runner
canonical-JSON assert, frozen before the definitive run; `--print-contract-sha`;
drift aborts exit 2 before any row). Runner:
`scripts/physical_record_born_admission_law_discriminator_tournament_2026_07_23.py`
Cold: **24 PASS / 0 FAIL over the 14 preregistered rows, exit 0** (5.86 s).

Work-history: joint visible max 678 at freeze (campaign tip `fb0ab5636e`);
claiming 679. COLLISIONS RECORDED: the campaign lane independently claimed
676 (`moving_carrier_phase_field_finite_restriction`) and 677
(`selected_record_joint_operand_corridors`, pushed 2026-07-23 12:12 -0400)
while this lane's 676 (PR #5561) and 677 branch were in flight; the branch
name `causal-time/cycle677-record-born-discriminator-20260723` predates the
677-collision discovery and stands per owner instruction — the claimed
number everywhere in contract/receipt/note is 679. Per the owner's
work-via-PRs directive, filenames are descriptive (no cycle numbers);
self-contained off origin/main `e42c5ec242` — nothing imported from
campaign-only substrate. Worker-drafted (Opus 4.8, effort max) to the
supervisor's bounded spec; independent Opus worker grid committed alongside;
reviewed line-by-line; all verdicts supervisor-owned; no codex.

This is the staged Objective 4 of the 2026-07-23 owner directive: the
repo-side READOUT HARNESS for the modeling side's Record/Born shared-middle
formation tournament. Cycle 625 (campaign lane) proved the retained
Admissibility surface does not select the extensional admission law: five
extensionally distinct, total, nonconstant, proper-cubic-covariant local
relations on the 64 six-neighbor words satisfy the structural schema
(unique_quorum {1}, odd_shells {1,3,5}, nonempty {1..6}, low_density {1,2},
even_nonzero {2,4,6}). The modeling side's formation routes (their cycle661
deterministic constrained-QCA and cycle663 dissipative channels are in
flight and pin the same c625 artifacts pinned here) plug into the unchanged
Cycle-625-B/Cycle-531 conditional-occurrence port. Cycle 679 supplies the
discriminating observable and the blinded held-corpus protocol that, given
ONLY port-readout streams, identifies WHICH candidate law a route implements
— or refuses with a witness. No formation route is built; no gravity surface
is touched; no Born probability content is claimed.

## The discriminating observable

`discriminate(stream, tables, frames)` — a pure function of the port-readout
stream, the public candidate tables, and the 24 proper-cubic frames.
Decision tiers, first refusal wins:

1. **Port grammar** (the Cycle-625-B/Cycle-531 lane-zero readout,
   winner-generalized): every trial tuple (archive[6], losers[6], ready,
   spent, edge, member[5], receipt[5], snapshot[12]) must satisfy
   PRECOMMIT=OCCURRENCE=ATOM_FLAG with zero label-zero tail, lane-zero
   one-hot MEMBER = LAW_RECEIPT tied to occurrence, edge and ready/spent
   rails tied to occurrence, losers = archive on refusal and
   archive-minus-one-hot-winner on admission (eight clauses W-bits, W-531,
   W-member, W-receipt, W-edge, W-resource, W-losers0, W-losers1).
   Violation -> refuse_malformed(clause, index).
2. **Determinism**: a word observed with both occurrence bits ->
   refuse_contradiction(word).
3. **Covariance**: observed acceptance must be constant on each orbit of
   the 24-frame action -> refuse_covariance(same-orbit witness pair).
4. **Family match**: the consistent subfamily C of the five frozen tables.
   |C| = 1 -> identified(law, one witness word per rejected law);
   |C| >= 2 -> ambiguous(C, all minimum completing shell sets) — the
   protocol refuses to guess under insufficient coverage;
   |C| = 0 -> off_family(one witness per family law).

The grammar is anchored at the unique-quorum point: the winner-generalized
emitter reproduces the pinned c625 `b_expected` field-for-field on all 64
words, edge included (row 1, 64/64). The winner generalization (any one-hot
admitted candidate cleared from the loser mask, not only the unique-hit bit)
is the minimal extension letting non-unique-quorum laws emit the same
retained tuple; the emitter's lowest-index winner convention is supplied
bookkeeping the decoder never reads beyond grammar well-formedness.

## The blinded held-corpus protocol (row results)

Blinding: 22 streams, generator assignment and per-stream word order
shuffled by a deterministic sha256 PRNG from the frozen seed; the manifest
is consulted only after all verdicts are recorded (unblind section);
decoder blindness proven by signature + source discipline (row 14, the
Cycle-676 check-9 pattern). Corpus split: train = weight <= 3 (42 words),
held = weight >= 4 (22) — the c625 census split.

- **Row 5**: all five in-family full-coverage streams identified blind,
  5/5, complete witness sets (one per rejected law).
- **Row 6**: all five identified from the train prefix alone (profiles
  restricted to shells {1,2,3} are pairwise distinct), and all five held
  extensions return the identical verdict — zero retractions, no refit.
- **Row 7 (refusal over guess)**: the shell-1-only unique_quorum-labeled
  stream returns ambiguous with consistent set exactly {low_density,
  nonempty, odd_shells, unique_quorum} and minimum completing shell sets
  {2,3} and {2,5}; the same six words labeled by even_nonzero already
  identify it (six rejections separate even_nonzero).
- **Row 11 (the core held row)**: the mimic shell law {1,3} agrees with
  odd_shells on all 42 train words (0 disagreements) and differs on 6 held
  words (all weight 5). Train verdict: identified(odd_shells). Full
  verdict: off_family with a weight-5 witness. Train identification is
  defeasible; the held corpus catches a train-consistent imposter.
- **Row 8**: the antipodal-pair orbit law (accepts the 3 antipodal shell-2
  words; orbit-constant, not a shell function) is refused EXTENSIONALLY
  (off_family, same-shell witness pair), not by the covariance tier — the
  candidate family does not exhaust covariant laws.
- **Row 9**: the +x-reading axis law -> refuse_covariance with a verified
  same-orbit witness pair. **Row 10**: the contradictory repeat ->
  refuse_contradiction on the repeated word.
- **Row 12**: eight malformed-port streams (member without occurrence,
  receipt mismatch, snapshot equation, snapshot tail, resource rail, loser
  mask, winner not one-hot, edge) each refused with exactly the expected
  clause, 8/8.
- **Row 13**: verdicts frame-invariant across all 24 frames for both an
  identified stream and an off-family stream (kind and identification
  unchanged under whole-stream rotation).

## Separator catalog (derived, cross-checked, pinned)

Orbit census: 10 orbits (shell: sizes) 0:1, 1:6, 2:3+12, 3:12+8, 4:3+12,
5:6, 6:1. The in-runner census reproduces the pinned c625 Route-A receipt
exactly: per-law truth rows (6/32/63/21/31), train/held accepts, all 10
pairwise separator counts, and the relation digest `c7242432...` (rows 2-3;
falsifier P-F3 unfired). Minimal separating shell sets: six sets of size 3
— {1,2,3}, {1,2,5}, {2,3,4}, {2,3,6}, {2,4,5}, {2,5,6}; shell 2 appears in
every minimal set (shell 2 is where low_density and even_nonzero peel off
the odd/unique cluster). The independently implemented Opus worker grid
(committed: `outputs/physical_record_born_admission_law_discriminator_worker_grid_2026_07_23.json`,
sha256 `5eeb9ca2c109e3f6...`) agrees on every compared field: orbit census,
shell profiles, pairwise separators, minimal sets, scenario consistent
sets, completing sets, mimic train/held split, antipodal summary,
train-only identifiability (row 4).

## Implementation repairs (pre-cold-run, contract untouched)

Two supervisor repairs between worker draft and the definitive run, both
logged with the frozen contract SHA unchanged (`8b968ceb...` before and
after; neither value class is contract content): (1) the row-4 comparison
was adapted to the independent grid's spec'd schema (the worker draft had
invented its own shapes for orbit census / pairwise rows / scenario keys /
mimic split — flagged by the drafting worker itself as an alignment risk);
(2) `shell2_accept_reject` carried a spec ambiguity (field name suggested
[accepted, rejected]; the grid spec's text defined [accepted, total] = [3,
15]) — resolved to the spec text. One dev run failed row 4 on (2) and is
preserved in the work log; the cold run is the first and only run after
repair.

## Supplied / derived / open

Supplied: the five candidate tables and the port grammar (transcribed from
the pinned c625 surfaces; read-only evidence anchors at campaign head
`fb0ab5636e` — c625 runner `a618b580...`, note `190ed6df...`, receipt
`a867cbee...`; c531 runner `8885593d...`, receipt `9be70316...`; nothing
imported or executed from these); the blind seed, corpus split, stream
roster, imposter definitions, malformed catalog, and the emitter winner
convention (all inside the frozen contract).

Derived on the declared code: the four-tier discriminating observable; the
orbit census and separator catalog with minimal separating sets; exact
blinded identification of all five laws from full and train coverage; the
ambiguity/completion semantics; the held-corpus retraction of the
train-consistent mimic; extensional (non-covariance) refusal of the
antipodal orbit law; covariance/determinism/grammar refusals with verified
witnesses; verdict frame-invariance; decoder blindness by signature+source.

Open: which law (if any) nature's fixed rule is — the harness identifies
what a ROUTE implements, not what the framework selects (c625's extensional
identification wall stands); objective actuality, framework-Record
identification, permanence realization; any frequency/grade/Born
calibration content (the Route-C lane untouched); noisy/sampled streams and
renewal (deterministic noiseless readout only); the three physical
formation routes themselves (modeling side; their cycle661/663/678 work is
theirs — untouched here).

## N1-N8 and firewall

No negative claim ships: every refusal row is a designed-imposter control
with witness semantics, not a no-go (N1 not engaged; no five-family
threshold in play). N5 discipline: no promotion of identification to
actuality, packet to Record, or profile to Born probability — acceptance
profiles are Boolean and no frequency is interpreted. The five laws are
c625 Route-A candidates at their exact residual (N4); the port is the
unchanged c625-B/c531 interface; emitters are synthetic self-test
generators, not formation routes; no gravity content; certification-side
combinatorics only; no control-plane changes.

Acceptance duties (modeling side, in the runner docstring): feed each
route's port-readout stream to `discriminate` unchanged; rerun rows 5-14
semantics on real streams; a refusal on a physical route is a finding about
the route (off-family, frame-dependence, non-determinism, or port-grammar
violation), not about the harness.

Preregistered falsifiers: P-F1 any blinded in-family stream misidentified
(rows 5-6) — discriminator unsound; P-F2 the mimic survives the held corpus
(row 11) — the held protocol has no content; P-F3 census/catalog disagrees
with the pinned c625 receipt (rows 2-3) — wrong family anchor. All map to
exit-1 rows; none fired.

## Cold verification

```text
RESULT 24 0 OK, exit 0; wall 5.86 s
receipt:     outputs/physical_record_born_admission_law_discriminator_tournament_receipt_2026_07_23.json
transcript:  outputs/physical_record_born_admission_law_discriminator_tournament_cold_2026_07_23.txt
worker grid: outputs/physical_record_born_admission_law_discriminator_worker_grid_2026_07_23.json
contract:    8b968ceb7c32b9350869c8f65126aa3e45388d8d48f54b2a00c66f43cf03d966
pins:        campaign head fb0ab5636e; c625 a618b580/190ed6df/a867cbee; c531 8885593d/9be70316
```
