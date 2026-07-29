# Review history — block01 (Cycle 721)

## Supervisor review log

- Extraction pass: three worker extracts (Bell surface; site-map/recurrent;
  geometry/factorization) spot-verified against source line ranges before
  use (B:84-233 verified verbatim; adversary blocklist and cache mechanics
  read directly; landed even-CAR runner re-executed clean).
- F2 draft: two spec-level defects found by the worker's honest failures and
  fixed under supervisor edits + one sol-xhigh fix pass — (i) covariance
  must evaluate the transported port (lexicographic-minimum is a chart
  convention; demoted to an informational counter); (ii) the 3-CNOT-SWAP
  reversal control is palindromic (replaced by middle-CNOT flip +
  stray-primitive detection). Chart-family lesson: the 11-generator
  adjacent-pair basis is a JW path chart; covariant objects are dictionary
  families + fixture-derived seam orientation classes. Supervisor reviewed
  the full algebra core line-by-line (phase conventions re-derived
  independently) and the covariance rewrite. Final: 22/22 PASS, exit 0,
  supervisor-rerun verified.
- F1 draft: first draft honestly FAILED; diagnosed (i) dilation-direction
  spec error (H-CP-H fixes X_a, transports Z_a -> Z_a R — supervisor
  re-derived and corrected the spec), (ii) bare-JW input bank drags global
  strings (16 cells / diameter 7) — physics fix: companion-encoded bank,
  (iii) covariance chart-family objects, (iv) route-tuple semantics.
  Revision pass returned 9/10; the last failure (layer constancy) was a
  wrongly-posed check: supervisor re-posed it as the structural law
  measurement layers = 3 + maximum cell degree (Koenig bound) with interior
  saturation certified by adding the (4,4,4) box; correction layers
  constant at 11 from 3x2x2. Final: 10/10 PASS, exit 0, supervisor-rerun
  verified; core construction functions reviewed (consistency anchors:
  tag-rebuild equality + coarse-half/target binary equality).
- F3 + independent checker: see below when landed.

## Promotion Value Gate (V1-V5, written record)

The block proposes bounded_theorem status only (no retained-positive
movement), so the gate is answered for the PR record:

- V1 (specific obstruction closed): quoted from the Cycle-720 note's Open
  list — "a literal physical-M2 circuit for the input-side even-CAR Bell
  measurements; a collision-free composition of Choi preparation, Bell
  coupling, correction controller, and recurrent matter word on one literal
  site map" — and from its receipt boundary,
  `even_car_input_bell_measurement_physical_M2_compiled: false`. Routes 1
  and 3 retire exactly these two items at the bounded ceiling; Route 2
  moves N1 escape route 4 (direct encoded-input Clifford) from
  UNTESTED/OPEN to ATTEMPTED-constructive.
- V2 (new derivation + novelty search): the compiled dilation surface,
  the conflict-coloring law (3 + max cell degree with Koenig saturation),
  the port-local seam-coupling result, and the epoch liveness walk exist
  nowhere on origin/main. Prior-art sweep recorded in ROUTE_PORTFOLIO.md:
  commit 2f2f4878ca, searches S1-S8 with matched-hit classification — the
  only occurrences of "input-coupling circuit" / "encoded-input Clifford"
  on origin/main are the Cycle-720 note's own open/untested declarations.
- V3 (could the audit lane already do it from standard machinery?): no —
  the content is the literal construction on the companion code (site-map
  compilation, atlas one-hot duality, fixture-derived orientation classes),
  not a textbook identity; the audit lane has no compiled measurement
  surface for this code.
- V4 (non-trivial marginal content): yes — the compiled words flip a
  declared receipt flag under a preregistered support gate that the
  raw-mode route measurably fails (7 cells / diameter 4, Cycle 720), and
  the seam coupling collapsing to one cell is a structural discovery about
  the companion representation.
- V5 (one-step variant of a landed cycle?): no — closest prior work is
  Cycle 720 itself, which certified the Bell rows as CAR-domain operations
  but explicitly did not compile them ("naming the route is not an
  attempt"); Cycle 146/147's record machines compile Pauli measurement
  choices on a different code with no CAR/companion structure and no
  site-map composition (classified nonmatching in the sweep). origin/main
  re-checked at 2f2f4878ca.

## Block02 (Cycle 722) supervisor review log

- Grounding agent verified the Cycle-610/612 harness interfaces from the
  primary sources (JointOrder call shapes; C704.joint_order_controls as
  the canonical consumer; interval arithmetic 16*carries + rotor_delta on
  identities (2,11,23); SHA pins; the projection-only feed rule; the
  Cycle-718 hostile-control boundary), and established that "coherent
  source-lift tournament" has NO landed definition (repo-wide sweep) —
  block02 scoped accordingly (feed leg only; source-lift handled as an
  undefined forward reference with a handoff target contract).
- F4 draft: PASS first delivery; supervisor reviewed the packet-sources
  construction (admission bits computed from the bundle's own algebra —
  symplectic dual/row pairings, F2 parity certificate — with slot-traced
  retained-register witnesses; the supplied convention is the register
  assignment, not the values) and the stage-E slot/handoff/walk reuse.
  Supervisor rerun: 7/7 PASS, exit 0.
- Independent checker: ast-extracts the packet map as data (no import of
  the primary; blocklist enforced), reimplements grammar/rotor/carry/
  interval arithmetic from first principles, agrees exactly with the
  imported EventChain, re-verifies the six 612 outcomes, SHA pins, fault
  behavior, and the primary's source discipline. 6/6 PASS; supervisor
  rerun verified.

## Block02 Promotion Value Gate (V1-V5)

- V1: closes the first leg of the quoted Cycle-720 gate sentence ("the
  unchanged Cycle-612 endpoint/interval harness ... feed") at bounded
  resolution, from the composed epoch of Cycle 721.
- V2: no epoch-fed harness exists on origin/main (sweep at ab163961a9
  recorded in STATE: the only EventChain consumers are the 704/718/719
  lineage, none epoch-driven); new content = the certified producer path
  (epoch retained registers -> witnessed projections -> unchanged
  decoder) as liveness-walked slots.
- V3: no — the content is the constructed feed on the certified epoch,
  not standard machinery the audit lane could assemble.
- V4: yes — byte-pinned "unchanged" discipline plus bundle-witnessed
  admission bits is a non-trivial bridge; the harness outputs are frozen
  values reproduced through a genuinely new producer.
- V5: no — closest prior art is the Cycle-719 bank core, whose packets
  come from its own controller banks, not from the companion-code epoch;
  the structural distinction is the producer surface (compiled input +
  epoch), checked against fresh origin/main.

## Block03 (Cycle 723) supervisor review log

- Grounding: EXTRACT_719_CONTROLLER.md (bounded extraction of the two-rail
  core + refusal primitive + rerun surfaces + coupling traps), used to lock
  the reversible per-station sandwich design (compute B|work; X-guard;
  NOT-syndrome control on every lifted gate; unguard; uncompute — valid
  because B/work are station-invariant inside Q; fresh scratch pool honors
  the dirty-work trap).
- F5 draft: first-delivery PASS (A-H certificates), supervisor rerun
  verified (exit 0); supervisor reviewed refusing_controlled_macro and the
  wrapped/unwrapped builders line-by-line (every macro gate guarded; R1/R2
  and program rows untouched; work_s/B_s invariance preserved).
- Independent checker: 4/4 PASS, supervisor rerun verified — first-
  principles simulator + own sandwich implementation agree exhaustively on
  the 2-bank program (22/22 dirt cases), inverse restores 32/32 basis
  states, source discipline verified by AST, and the 95,850-gate word size
  reproduced by independent arithmetic (728+12,306+2,796+79,240+780).
- V1-V5: V1 closes the Cycle-719 N6 "strongest next closure" and executes
  the refusal half of its N7 steelman terminal test (quoted in the note);
  V2 sweep: no wrapped-controller artifact exists on origin/main (the 719
  runner's own report records non-integration); V3 no (companion-code
  controller construction, not standard machinery); V4 yes (exhaustive
  182-case refusal census with independent predictions + honest
  supplied-inventory trade); V5 no (the Cycle-719 diagnostic guards one
  sample X at one station; this wraps all 91 stations with a different,
  reversible sandwich and re-certifies the full surface).

## Review-loop disposition

Owner-operated lane (standing rule 2026-06-11): this block prepares the PR
and hands off; the review loop is not run from this session.

## Block 10 (Cycle 730) — V1-V5 promotion value gate (author-side record)
- V1 claim-state movement: W1 ledger line parity-sector ENFORCED (was:
  witnessed/compressed). PASS.
- V2 decisive artifact: prediction-exact 183-violation census; exhaustive
  8,388,608-case iff theorem; independent checker with own simulator.
  PASS.
- V3 honest boundary: matched-parity residual FROZEN in-package;
  w1_closed false; supplies enumerated. PASS.
- V4 no vocabulary/authority drift: bounded_theorem, authority none,
  audit unset; no new repo vocabulary. PASS.
- V5 independent-audit handoff: stated in note + PR #5709. PASS.
- Status ships as bounded_theorem (NOT proposed_retained); review-loop
  and audit remain owner lanes.

## Block 11 (Cycle 731) — V1-V5 promotion value gate (author-side record)
- V1 claim-state movement: the named-open W1 nonlocal certificate
  BUILT; matched-parity residual REFUSED (55/55). PASS.
- V2 decisive artifact: exhaustive iff theorem with frozen outcome
  tables; checker REBUILT the full outcome table independently, sha
  matched byte-exact. PASS.
- V3 honest boundary: w1_closed carries a verbatim bounded-scope key
  (ring-11 only; inventory declared-not-derived; genesis open). PASS.
- V4 no drift: bounded_theorem; no new vocabulary; expected_count reuses
  the existing declared supply line. PASS.
- V5 handoff: stated in note + PR #5710. PASS.

## Full-Fock support — V1-V5 (author-side record)
- V1: the Cycle-322-named absent lift constructed (n_max=2). PASS.
- V2: 8/8 + independent 6/6 (0-ULP anchor recount; 20/20 pinned
  replay). PASS. V3: truncation + embedding declared supplied; C_source
  firewall verbatim. PASS. V4: no drift. PASS. V5: stated; PR #5708.
  PASS.
