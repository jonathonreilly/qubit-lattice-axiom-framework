# Route portfolio — Cycle 721 (block01)

## Prior-art sweep record (skill step 2)

- Searched commit: `2f2f4878ca8676d963e80b33e697e76825614de0` (origin/main,
  refreshed 2026-07-27 ~21:50 local, after the record-campaign/N5/compute
  landings of 2026-07-27).
- Commands and hits:
  - S1 title scan `git ls-tree ... docs/ | grep -iE "INPUT_COUPLING|ENCODED_INPUT|EPOCH|LIVE_INPUT|BELL.*(M2|INPUT)|INPUT.*BELL"`
    -> zero hits.
  - S2 `git grep -iE "input.coupling circuit" origin/main -- 'docs/*.md'`
    -> only the Cycle-720 note (3 hits) — the open declaration itself.
  - S3 encoded-input Clifford (both orders) -> only Cycle-720 note lines
    345/408/449: `UNTESTED/OPEN`, "naming the route is not an attempt".
  - S4 collision-free schedule/epoch -> two context-only hits:
    - `AUXILIARY_PAIR_COMPLETION_GATE_CYCLE54_NOTE_2026-07-14.md:235` —
      caution "collision-free signature tables do not imply schedule-safe
      composition" (older rule-graph nucleation surface; NOT the companion
      code; classified nonmatching prior art, adopted as a design
      constraint for Route F3).
    - `CYCLE80_RECURRENCE_AUDIT_ENDPOINT_TUBE_NUCLEATION_CYCLE85_NOTE_2026-07-14.md:27`
      — collision-free composition of tube-recurrence tables (older
      endpoint-tube surface; nonmatching).
  - S5 bell measurement/M2 compile statements outside Cycles 719/720 ->
    zero hits.
  - S6 runner-name scan cycles 656-729 for input/bell/clifford/schedule ->
    `frontier_cycle709_local_seam_clifford*` (seam Clifford on the earlier
    surface — adjacent machinery, not input coupling) plus the known
    Cycle-720 runners.
  - S7 obligations/ledger scan `companion.*(input|bell)` -> four old
    unrelated ledger rows (axiom_first_spectrum, ckm, dm_*) — nonmatching.
  - S8 "input hardware / measurement compilation" -> Cycle-146/147 record
    machines compile Pauli measurement *choices* on the record-machine
    surface (different code, no CAR/companion, no site-map composition);
    Cycle-703 plaquette decoder is adjacent controller machinery. Both
    nonmatching for the Cycle-721 statement.
- Classification: **Open after matched-hit review** for all three routes.
  No landed note proves or refutes a literal M2 input-Bell compilation, an
  encoded-input Clifford on the companion/center code, or a collision-free
  epoch composition on the Cycle-720 site map.

## Routes (artifact types; approach families in APPROACH_REGISTRY.md)

| route | artifact | expected movement | score notes |
|---|---|---|---|
| F1 CAR-BELL-M2 | runner + note section | retires Cycle-720 Open item 1 (literal physical-M2 circuit for input-side even-CAR Bell measurements) at bounded_theorem ceiling | strongest: Cycle 720 already certified the Bell rows as bounded CAR-domain operations with one-cell private duals; compilation is the declared missing leg |
| F2 ENC-CLIFFORD | runner + note section | independent constructive escape of the raw-Bell diagnostic; second tournament leg | medium: no prior attempt exists (N1 row `UNTESTED/OPEN`); risk that the input-side M2 assignment reintroduces JW growth |
| F3 EPOCH-SCHEDULE | runner + note section | retires Cycle-720 Open item 2 (collision-free composition of preparation/Bell/corrections/recurrent G on one site map) | gated on F1 or F2 supplying the input leg; must do register-liveness accounting per the Cycle-54 caution, not signature tables |

Tournament shape per the Cycle-720 verdict: all three attempted; each leg
reports its own PASS/FAIL against the preregistered support/diameter gate;
failures ship as route-specific diagnostics only (N1-N8 gated), never as
broader negatives.
