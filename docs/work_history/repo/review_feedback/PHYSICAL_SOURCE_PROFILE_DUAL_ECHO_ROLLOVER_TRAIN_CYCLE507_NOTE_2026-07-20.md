# Physical source/profile dual-echo rollover — Cycle 507 TRAIN note (2026-07-20)

Authority: none
Audit: unset
Disposition: **TRAIN POSITIVE FOR THE FINITE N=8 DELAY APPARATUS ONLY; HELD ADVANCE REMAINS UNRUN**

## Frozen inputs

- Preflight runner: `scripts/physical_source_profile_dual_echo_rollover_preflight_cycle507_2026_07_20.py`
  - SHA-256 `228b37f92069117aac5a13023bbc11e32188bc4d3425815bdec366aa06ffa3c3`
- Preflight note: `docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_PROFILE_DUAL_ECHO_ROLLOVER_PREFLIGHT_CYCLE507_NOTE_2026-07-20.md`
  - SHA-256 `3b81720d0589a4d523d2eeee5a9624132602a76aa7ee19caf32466279279cc9f`
- Train manifest SHA-256: `7c98084fbc3ef6c64879e6994127984464a6c3cb625d9038d966b91bd7d36ed3`
- Held manifest SHA-256: `3a3814d2cac73bcf94ccc1f9ea2427fe098b2de861524dc02a5be84a91fc9e3f`
- Train evaluator: `scripts/physical_source_profile_dual_echo_rollover_train_cycle507_2026_07_20.py`
  - SHA-256 `03403653f941ec344db5045efe62ba2ea58151353caaca3a5e06e753964b39d6`
- Canonical scout transcript: `/tmp/cycle507_train_scout_2026-07-20.txt`
  - SHA-256 `991a84840bfcfbe2a46bc429b873f75b00a6119ca5e0141b5c8f2958d23b53ca`
- Canonical full-train transcript: `/tmp/cycle507_train_full_2026-07-20.txt`
  - SHA-256 `15e77c1723c58536272a8e286abfd8eb45be90361ae25c2523e4c82034920c51`

The evaluator dispatches exactly the 19 frozen train rows: six primary rows and thirteen controls. It contains no held dispatcher. The canonical full run reports `held_rows_executed: 0`.

## Exact finite result

For every Cartesian product of the three frozen train source sectors

`{-2pi/9, -4pi/9, -2pi/3}`

and both frozen mass routes

`{cayley, principal}`,

the evaluator physically compiles the inherited Cycle-441/451 source fixture, applies the Cycle-451 selected-rail transport, and retains the resulting actual coherent nine-M2 register x eight-M2 local-mode controller. It does not replace that state by a selected receiver bit. The receiver-zero and local-mode-7 histories remain together in the same joint state.

The response program is a separately supplied physical `one_hot_2(DELAY)` carrier. It is not obtained from beta, a receiver squared norm, a grade, a threshold, a loop ordinal, or host lookup. Receiver squared norms are reported only as diagnostics; they are not occurrence or probability.

On the declared N=8 train code, with two independently prepared equal `ell=2` Cycle-504 corridors and one common supplied opportunity delta:

- every receiver-zero component retains reference/probe totals `32/32`, hence `4:4` per return and ratio `1`;
- every local-mode-7 component retains reference/probe totals `32/24`, hence `4:3` per return and probe/reference ratio `3/4`;
- all eight endpoint bindings in both corridors carry the same register/local-mode/program/profile label as their coherent controller component;
- all eight probe response receipts classify baseline versus suppressed response and retain event identity;
- the six response work M2 sites exhaust blank after every application;
- no host-selected corridor length, cadence, decoder schedule, or source-sector lookup is an input to the update or decoder.

Thus, for this frozen finite train code,

`E G_coarse = G_physical E`

with exact represented-state residual `0`, exact inverse residual `0`, controller-population residual `0`, binding failures `0`, response-receipt failures `0`, and work-exhaust residual `0`. The largest inherited floating normalization residual across the six primary rows is `2.4424906541753444e-15`.

This is a conditional finite compiler result. It is not a derivation or selection of the DELAY law, not a physical lapse or proper-time result, not a branch occurrence law, not a Record, and not an actuality result.

## What was executed and what was certified compactly

The evaluator literally executes the inherited logical Cycle-504 corridor gate tables. For the probe, it replaces baseline clock and wrap controls by the computed response step-enable and explicitly computes/uncomputes the six-work-M2 response word. The installed local schema contains both D and A controls and the fifteen-Fredkin extra-clock word. All sixteen receiver/program/distinguished-edge/edge-control truth rows pass and return the response work blank.

Two implementation boundaries must remain explicit:

1. Endpoint courier/binding outcomes in `evolved_joint` and `courier_bank` are evaluated as the optimized exact effect of the declared CNOT/Toffoli logical gates. The run does not replay each courier terminal gate separately for every coherent amplitude.
2. Restored-line locality is an exact compact route certificate. The evaluator verifies operand existence, arity at most three, exact route counts, restored placement by construction, and all-24 carried line adjacency. It does **not** materialize or execute the roughly twenty million elementary adjacent operations.

These optimizations preserve the represented logical map and its exact inverse checks, but they do not turn the result into a literal hardware execution trace. The apparatus is a finite size-specific restored-line circuit, not a size-uniform bounded-depth or bounded-radius QCA.

## Geometry and resources

The exact train layout contains `1562` represented M2 sites:

- two complete N=8, `ell=2` Cycle-504 corridors;
- one 24-M2 register/local-mode/D-A/profile carrier;
- two initial 24-M2 bindings;
- two 24-M2 endpoint bindings per event;
- nine response-receipt M2 sites per event;
- six clean response-work M2 sites.

The compact compiler reports:

- logical terminal gates: `1451` (below the frozen preflight envelope `1512`);
- maximum terminal support: `3` M2 sites;
- exact forward-plus-restoration adjacent SWAP count: `6,742,818`;
- exact compact elementary-operation count: `20,230,291`;
- route/operand failures: `0`;
- proper-cubic frames: `24`;
- carried line-adjacency failures: `0`;
- expanded SWAP tuples materialized: false.

The inherited source/mass target residual is `0` for both Cayley and principal routes. The maximum inherited all-24 source-operator covariance residual is `8.830824800525959e-16`.

The canonical full train run took `96.61 s` wall time and `972,472,320` bytes maximum RSS under `/usr/bin/time -l`, below the frozen `600 s` and `2 GiB` caps.

## Frozen controls

All thirteen controls reject the positive classifier:

| Control | Exact train disposition |
|---|---|
| label courier deleted | rejected by nonzero retained-binding failures |
| reference profile binding deleted | rejected by reference-binding failures |
| probe profile binding deleted | rejected by probe-binding failures |
| receiver control deleted | mode-7 trajectory becomes `4:4`; rejected |
| DELAY enable deleted | mode-7 trajectory becomes `4:4`; rejected |
| response receipt deleted | retained receipt classifier fails |
| ordinary wrap carry deleted | lawful physical domain rejects missing `EDGE_PASSED` arrival word |
| extra wrap carry deleted | **schema-level pre-held rejection only**: the installed A truth column loses its extra-carry kind; this is not an exercised D-trajectory deletion |
| reference RETURN deleted | endpoint lineage/payload domain rejects |
| probe RETURN deleted | endpoint lineage/payload domain rejects |
| host cadence comparator | arithmetic can match, but response receipts and schedule-free decoding are absent |
| host-selected corridor length comparator | leaves the frozen equal-`ell=2` code |
| source-sector lookup comparator | has no physical two-M2 D/A carrier |

The extra-wrap result must not be promoted beyond its exact status: train prepares D and therefore does not exercise the A trajectory. Held ADVANCE must physically test the extra-step wrap conveyor before that control becomes a trajectory-level deletion result.

Five malformed-domain fixtures are also rejected: non-one-hot D/A word, blank profile, blank local mode, dirty response work, and wrong-width binding bank. An AST audit confirms that the decoder has no host application, loop, schedule, depth, beta, source-sector, or corridor-length input.

## N1-N8 no-go discipline after train

### N1 — normalized constructive families

1. **Primary object:** actual joint Cycle-441 register x Cycle-451 local-mode controller plus two equal echo corridors. **Mechanism:** coherent local-mode-7 and physical D jointly suppress the distinguished probe step. **Terminal obligation:** train 3:4 with receiver-zero 4:4, inverse, couriers, receipts, and all controls. **Disposition:** finite N=8 DELAY train positive; held A open.
2. **Primary object:** one fixed short/neutral/long supergraph. **Mechanism:** transported label controls a local reversible route switch. **Terminal obligation:** restored switch and equal external endpoints. **Disposition:** open and untested.
3. **Primary object:** edge-token stream plus reversible 3/4/5 transducer. **Mechanism:** source-labelled finite token accumulator. **Terminal obligation:** renewable blank work and retained lineage. **Disposition:** open and untested.
4. **Primary object:** joint source-register x dual-clock block operator. **Mechanism:** operator-first coherent accumulator control. **Terminal obligation:** sparse physical compiler without beta/projector lookup. **Disposition:** open and untested.
5. **Primary object:** transported common-profile handshake. **Mechanism:** local rendezvous admits a suppressed or extra step. **Terminal obligation:** autonomous certificate genesis/consumption. **Disposition:** open and untested.
6. **Primary object:** source-emitted mediator collision. **Mechanism:** one local boundary collision changes certified probe emissions while retaining a mediator ledger. **Terminal obligation:** size-stable source/clock scattering compiler. **Disposition:** open and untested.

### N2 — wall independence

The finite train compiler, D/A law selection or genesis, Record occurrence, and continuum metric/proper-time walls remain logically independent. This train result advances only the first wall for N=8 D input. It neither collapses nor proves any of the other three.

### N3 — hidden-wall scan

Supplied structure remains: common delta, finite N=8 apparatus, two independent blank `ell=2` corridors, Cycle-441 source-sector preparation, Cayley/principal mass route, actual Cycle-451 controller transport, physical D program, profile identity, distinguished probe edge, blank finite banks, restored line placement, and noiseless reversible gates.

### N4 — residual matching

- Cycle 451's joined-response/renewal residual is partially matched by the finite N=8 D corridor compiler.
- Cycle 504's source-conditioned dual-echo residual is partially matched by the same finite apparatus.
- Host beta-to-program lookup is absent, but physical program genesis and law selection remain open.
- The continuum lapse/proper-time residual is not matched; only finite dimensionless ratios were tested.
- Held A and its extra-wrap conveyor are not matched.

### N5 — rhetoric audit

“Host-selected length is inadmissible” applies only to the frozen equal-`ell=2` classifier; it is not a no-go against a physical local supergraph switch. “Host cadence is absent” applies only to this retained endpoint/receipt decoder; it is not a no-go against every autonomous transducer. “Source lookup is absent” means D is physically supplied here; it does not derive D from the source.

### N6 — partial-closure paths

Run the frozen held A rows only after root review and implement the extra-wrap conveyor; build the fixed-supergraph and edge-token alternatives; replace supplied D/A preparation by a local source interaction; replace restored global line routing by a bounded-radius tiling; and address occurrence/Record and continuum metric laws independently.

### N7 — hostile steelman

A fixed short/neutral/long supergraph remains a serious alternative. One immutable physical geometry can contain all arms, while a transported local label controls only a reversible switch. That route could satisfy the no-host-length target without sharing the present clock-step-control implementation or its finite restored-line routing.

### N8 — cross-cycle echo

Cycle 451 closed a denominator-registration problem by adding a co-registered dual clock. Cycle 504 closed finite no-wrap endpoints by adding retained rollover and renewal carriers. Cycle 507's train result composes those carriers for supplied D. Those earlier closures came from new physical carriers, so failure of held A or a future size-uniform compiler would still not support a route-independent no-go while the supergraph, transducer, operator, handshake, and mediator routes remain live.

Broad no-go gate: **FAIL / DO NOT SHIP**.
Shared substrate obstruction: **not established**.
Axiom pressure: **none**.

## Exact disposition and next decision

The strongest result is a finite, source/profile-labelled, coherent-controller compiler for the N=8 supplied-DELAY train apparatus. It joins the Cycle-451 source/mass controller to two independently prepared Cycle-504 retained-history corridors without host length, cadence, branch selection, decoder schedule, or source lookup.

The optimal immediate next action is root review of this train evidence. Only after approval should the two-row held ADVANCE manifest run. That held evaluator must implement and exercise the extra-step wrap/carry path rather than relying on the present schema-only A truth column. No held run, stage, commit, or push occurred in producing this note.
