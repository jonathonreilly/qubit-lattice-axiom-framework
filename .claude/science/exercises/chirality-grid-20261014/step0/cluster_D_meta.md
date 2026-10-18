# Step-0 prior-art map, cluster D (meta surfaces): chirality / doubling wall

Reader: read-only, 2026-10-14 13:00–13:10Z. **Framework refresher done:** read
`origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines). Note that
`:206-208` lists "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`"
as an open gate outside the axioms.

Refs: `HEAD` = `claude/candidate-law-20261008` @152384b70a (it matches origin). Abbreviations:
`GX` = `.claude/science/exercises/gravity-current-state-20261009/` (HEAD only, unlanded);
`CL` = `.claude/science/candidates/candidate-law-20261008/` (HEAD only, unlanded);
`W` = `.claude/science/walls/toe-walls-20260929/` at 4bd42747e5 (PR #9395, closed unmerged);
`VB` = `origin/claude/toe-viability-probes-20260927` @fd51a1f4c7 (PR #9363, closed unmerged).
Every PR found by the searches is CLOSED or MERGED. **No open PR touches chirality.** Of the 50 open
PRs (#9499–#9546), none mention it.

## (i) Table

| Object / packet | path:line or # | Status | What it shows | What it does NOT show |
|---|---|---|---|---|
| Fork probe, 4-lens panel | `7adeccb570:.claude/science/physics-loops/admissibility-induced-law-20260906/FORK_PROBE_source_link_20260922.md:10,14`; PR #8572 | closed, not on main | The 8 species are all kept, 4R+4L: no covariant `b(k)·σ` gaps a corner. Tension: "vector-like spectrum forced; SM is chiral". It lists the exits as a larger coin (parked), a 4th direction with a wall, non-local reach, or filling. It says 16 branches ≠ 16 Weyl fields | No exit is tested |
| Block 82: what gaps the walk | memory `admissibility-induced-law-block82.md:3`; PR #8628 | closed (memory) | No covariant translation-invariant term at any reach gaps a corner. Only the chessboard (staggered) term or stripes gap, and they gap pairs | Nothing chiral |
| Block 79: chessboard background and walls | memory `…block79.md:13`; PR #8614 | closed | Walls bind exact zero modes. Its own caveat: a seam in 3D carries 2+1D modes, so there is no 4D handedness (Kaplan needs a 5th dimension) | 3+1D chiral modes |
| Block 119: species doubling | memory `…block119.md:3,12`; PR #9170 | closed | Species symmetry forces only doubling. Rate fields keep 16 zero modes. No clock field gaps the species | — |
| Probe-HIT issues on species and filling | #8741 (eight species all kept), #9106/#9126 (filling between a-term levels, chiral content), #8668, #8867/#8987/#9007 (parity-odd couplings under proper rotations only), #9045/#9123 (species), #9368 (double-Weyl touching, charge ±2) | OPEN issues, same-family | #8741: nothing in M₂(C) gaps a species; the staggered mass gaps opposite-sense pairs; one object per site is "the parked site-algebra decision". #9106: no filling gives single-sense gapless content (overlaps #8668). #8867: the one parity-odd term is the scalar hop `a`; the chiral 8-step loop trace is −a³β⁵ | No chiral spectrum; mostly unrefereed |
| LATTICE_HANDEDNESS note (viability probe 2) | `VB:docs/LATTICE_HANDEDNESS_…_2026-09-27.md` (claim scope `:4`, summary `:24-40`) | unlanded; sol referee: "stands with corrections mathematically; fails as an exhaustive framework claim" (`VB:docs/TOE_VIABILITY_MAP_…:1247`) | T1: two-band C¹ ⇒ zero net chirality (walker 4R/4L). T2: every strictly local tick has W3 = 0 (SK₁ = 0). T3: S_xS_yS_z has 16 nodes, 8R at the corners and 8L at (π/2)(±1,±1,±1). T4: a covariant W3 = 4 tick exists only with tails; it is not a Hamiltonian flow. T5 is a flux check | Interacting or gauge-coupled walkers; N-band node balance (cited, not proved) |
| Viability map, chirality items | `VB:docs/TOE_VIABILITY_MAP_…:241-256, 575-578, 647-649, 738-739` | unlanded | Fastest route: "overlap (Ginsparg–Wilson) fermions plus symmetric gapping of a 16-Weyl mirror sector". Probe 4 suggests a 1D symmetric-gapping analogue. The chiral tick's π sector is a time doubler and it heats | None of these was run |
| TOE walls T22 (chirality) and T24 (doublers) | `W/WALLS.md:41,43`; `W/attacks/T22.md`; `W/kills/T22.md`; `W/kills/T24.md` | PR #9395 closed; its claims moved to the J queue | T22 STANDS → WEAKENED. A left-only SU(2) is the same theorem as the free no-go. Test B: the native surface is anomalous and a unique 7-state completion gives 15/16. The tails tick pumps phase 4·N_φ, but that cancels over the 16-plet (kill). T24: the 8 corners are forced by soldering (block 82); only pairs lift | Overlap/Lüscher–Kikukawa route ("missed, alive"); domain wall unanalysed; SMG intermediate coupling |
| SPIN10 mirror-boundary note | main `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` (PR #8113 closed; note on main) | landed, bounded | Exact Spin(10) atomic gap. Freezing the mirror slots returns eight doublers (per `W/attacks/T22.md`). It is the declared starting point of K2a and SMG route R1 | Intermediate-coupling phase ("N6") |
| Candidate 1, kill sheet K2 | `CL/KILL_SHEET.md:19,75-83,108-112` | pre-registered | K2a: Spin(10) 16 ⊕ 16̄ per generation plus a local symmetric-gapping interaction (Wang–Wen / Eichten–Preskill). K2b: the mirror actually gaps (Butt–Catterall–Hasenfratz). K6: three generations | — |
| K2a result | `CL/TEST_LOG.md:58-96` | run, supervisor-checked; no referee ("not owed for a PASS") | Continuous-time (H) form PASS (weak): Z = T₁T₂T₃ equals Weyl chirality on the zero modes, which gives a 9-site mirror projector P̄_R and a Spin(10)-singlet FK quartic. Content per field is 2×16 ⊕ 2×16̄. Hypercubic (Q) form INCONCLUSIVE: in 4D, T₁T₂T₃ takes ±i inside each chirality block, so there is no selector | The gap is not shown (ψ^R is not canonical). Eichten–Preskill leakage through links. The staggered mass is forbidden (Z-odd). Gauss law needs a Spin(10) Cartan. 16–32 bits per vertex. Generations come in pairs |
| "Tension" record | `CL/TEST_LOG.md:90-93` | reading | "chirality wants continuous time, one cone wants hypercubic time" | Not a theorem |
| Decision matrix, chirality row | `CL/DECISION_MATRIX.md:55` | reading | "every repo route keeps a mirror partner. Symmetric mass generation (Wang–Wen) is named only as prior art" | — |
| K7a referee | `CL/checks/referee_K7a/REFEREE_VERDICT.md:13,40`; `CL/TEST_LOG.md:27,33` | refereed | 4D staggered fermions: 4 tastes, two-step transfer matrix. Shift symmetries kill taste-nonsinglet dim-4 terms | Chirality |
| R2-4 (set B weight) | `GX/TESTS.md:2562-2590` (pre-registered), `:2728-2736` (verdict); `GX/agents/C5_R2-4_report.md:20-32,165-204,255-262,293-297,330-338`; referee `C5_R2-4_referee.md:44-63,75` | refereed, CONFIRMED WITH CORRECTIONS | No ultralocal GW operator in the hypercube-range W(B_d) class (exact Gröbner, d = 2, 3, 4). The overlap operator is only exponentially local. Mirror-SMG is nearest-neighbour compatible and open. "No class-wide chiral no-go": NN is a free-field theorem only | Positivity/RP of overlap or domain-wall fermions; any construction |
| R6-5 (CPT-odd dimension-3 terms) | `GX/TESTS.md:3181-3210,3264-3268` | worker readings only | Law-level CPT is SYMMETRY-PRICED and conditional. It needs inversion in Lattice and Admissibility, a reversible law, and "a chiral lattice construction that has not been built" | — |
| R9-1 (edge/doubler population) | `GX/TESTS.md:3600-3612,3839-3842` | referee: only "L under G-out EXCLUDED" survives | Literal doublers: 7 electron corner valleys add about 588 MeV to Γ_Z | — |
| R19-34 / F-series | `GX/TESTS.md:8729-8745,8886` | worker or refereed OPEN | Wilson doubler removal gives a strain hazard. Zeros occur only at r = 0, on staggered edges, or on GW edges | — |
| NF-1 (staggered strain control) | `GX/TESTS.md:9448-9474` (pre-registered), `:9493-9520` (worker), `:9578-9583` (referee); `GX/agents/C5_NF1_report.md:46-57,200-230`; `C5_NF1_referee_verdict.md:3-19` | refereed: OPEN (the literal U(1)_ε is not exact) | Discrete Θ (sublattice + τ→−τ) and P_stag force all 64 entries of Σ(0,0) = 0 under strain. One staggered field = 2 Dirac tastes. 22.5/2 = 11.25 is not an integer. T1 (a twin per field): +84 MeV in Γ_Z (36σ, conditional). T2 (tastes paired across generations) needs SM + 3ν_R + one vector-like family | T2 untested. Electroweak chirality is "common to both edges" (`C5_NF1_report.md:229`) |
| E1 (emergent coarseness) | `GX/TESTS.md` after 9583 (worker MECHANISM-SPLIT) | worker reading; referee was running | Protected gaps (staggered, graphene) stay exactly 0 under stretch. Suggests a composite Higgs | Chirality |
| TW-1/2/3 | `GX/TESTS.md:9611-9658`; commit 152384b70a | pre-registered 2026-10-14 12:58Z | see (iii) | not run |
| Photon doublers | `GX/SUMMARY.md:652-653,684`; `GX/TESTS.md:4308,4375-4506` | refereed | Class 𝒮: the photino has Chern ±2, which forces photon doublers (R10-5). The doubler-free BF/Kähler–Dirac multiplet needs a 1/r term (R12-3, R13-4) | Gauge-boson analogue only |
| C3 lane D (spin-½ on links) | `GX/SUMMARY.md:253,271`; `GX/PRICE_NOTE.md:58,99,168` | refereed INCONCLUSIVE | "Order alone gives no handedness"; price P6 = an orientation and spin-transport primitive | — |
| Lane RS (interacting staggered) | `GX/TESTS.md:900-971`; `GX/SUMMARY.md:302-311` | refereed bounded FAIL (momentum only) | Taste adds no collision invariant: the staggered band is lattice KG at (2k, 2m) | Chirality |
| Archived opus-direct campaign | `archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md:2974,3407-3530` (main) | archive, historical | Kähler–Dirac operator: the only chirality is the form-degree parity, which gives no axial anomaly (R45). R46: "forbids ultralocal chiral matter", not chiral matter outright. A GW operator from the cochain structure is "not attempted" | Any GW build |
| Chirality correction packet | `.claude/science/physics-loops/chirality-correction-20260909/` (main); originals #7973/#7989/#7991 | corrected, landed as conditional | Record-side handedness. A mirror-asymmetric rule registers only its own texture; the movers are T-images; a formation sweep registers direction, not handedness | Lattice-fermion chirality |
| Vortex backlog | `archive/backlog/vortex-7935-7949/` (main) | archived | A 2D vortex carries a single Weyl mode; the taste-singlet second-mass vortex strings carry 2n co-moving modes | 3+1D |
| ai/execution scorecard | `origin/ai/execution:TOE_SCORECARD.md:49` | planning only (no science status) | "physical chirality remains open" | — |

## (ii) What was tried and failed, with the reasons

1. **Free local walker or tick.** Every two-band finite-range free walker is balanced, whether it flows or ticks, and W3 = 0 for any band count (VB handedness T1/T2). Same-family tests in `W/attacks/T22.md`: 40/40 random SU(2)-symmetric walkers have zero chirality per isotype.
2. **Covariant gapping of the species inside M₂(C).** The corner stabilisers make every covariant symbol scalar at a corner (block 82; fork probe `:10`; #8741). The staggered mass only gaps opposite-sense pairs.
3. **Filling between the a-term levels.** No filling gives single-sense content. Exclusion makes the needed filling impossible: it would need ≥ N+6 records on N sites (#9106 → #8668; block 85).
4. **Record-side chirality.** A mirror-asymmetric rule or a formation sweep registers texture or direction, not a chiral mode (chirality-correction packet).
5. **Ultralocal GW in the hypercube-range class.** No such operator exists (R2-4 A2, exact, bounded to the ansatz).
6. **Hypercubic 4D staggered selector.** None exists: T₁T₂T₃ takes ±i inside each chirality block (K2a Q form, `CL/TEST_LOG.md:74`).
7. **The tails tick as an escape.** It is not a flow, so there is no Hamiltonian and no ground state. Its π sector is a time doubler and it heats (`VB` map `:738-739`). The kill check showed its phase pump cancels over the 16-plet, so the pump is not its price (`W/kills/T22.md`, route table).
8. **Domain-wall seams in 3D.** They give 2+1D modes only (block 79). A 5th dimension is not in Lattice (`W/kills/T22.md`).
9. **Taste-as-twin (NF-1 T1).** It fails Γ_Z by about 36σ, conditional on an identical Z coupling.
10. **K2a in the H form.** It passed only weakly. Its seven caveats in (i) are the actual open obligations, and it is not refereed.

## (iii) Pre-registered but NOT run

- **TW-1** "Twin = antiparticle (Majorana / reduced-staggered halving)". Readings HALVE-WORKS / -PARTIAL / -FAILS / OPEN; expectation HALVE-PARTIAL. `GX/TESTS.md:9619-9631`.
- **TW-2** "Twins as generations with realistic taste splitting". Readings SPLIT-SAFE / -HAZARD / OPEN; expectation SPLIT-HAZARD. `GX/TESTS.md:9633-9645`.
- **TW-3** "Symmetric mass generation toy". Probes: an 8-Majorana SO(7) quartic, strained hopping, multiplicative vs additive gap, and the 16-Weyl count. Readings SMG-PROTECTS / -LEAKS / OPEN. `GX/TESTS.md:9647-9658`. Its expectation hands the 3+1D question "to the chirality exercise".
  - All three were pre-registered at 12:58Z today (commit 152384b70a, TESTS only). There are no worker or referee files on HEAD or origin.
- **K2b** (mirror sector gaps without symmetry breaking). `CL/KILL_SHEET.md:83`. Not run.
- **K6** (three generations from content). `CL/KILL_SHEET.md:108-112`. Not run.
- **NF-1 T2 content** (SM + 3ν_R + one vector-like family; taste-splitting operators). Named but "not computed" (`C5_NF1_report.md:218-229`; referee `:13` says "untested").
- **Viability probe 4.** A 1D in-framework symmetric-gapping analogue of the walker's mirror partners. Suggested, not run (`VB` map `:575-578`).
- **T22 kill's "cheaper question".** Which inputs does the Lüscher/Kikukawa overlap Weyl-measure route use on Z³×Z_τ, and are any derivable from the four axioms? Named, not run (`W/kills/T22.md`, Errors item 3).
- **J-queue task `J:derive:review-20260929-interacting-cones-and-chiral-carriers:a1`.** It covers the degree/winding or locality proof for a chosen chiral carrier, plus "heating, sixteen-state necessity and interacting mirror removal". It is in `origin/ai/probes:probes/tasks/review-science-20260929.json` (sources #9363 and #9395 via `probes/work/review-science-20260929/SOURCE_MAP.json`, wall T22). There is no log directory and no attempt directory on ai/probes @d61e03f1fe (2026-10-12), so it is unclaimed.
  - The memory notes that the 09-30 Sonnet chirality prior-art worker died before reporting (`stadium-picture-20260930.md:43,47`).
- **R2-4 open items** (named, not run): RP of overlap or domain-wall fermions in physical time, and a positive 4D pair model with emergent chiral fermions (`C5_R2-4_report.md:204,255,273`).

## (iv) Current statements of the wall and its price

- T22: "A free local walker always has a mirror twin; a left-only weak force is the same theorem. Every exit needs the full anomaly-free 16-state family." (`W/WALLS.md:41`)
- T22 kill: the overlap route "is the better documented; its open point is locality of the measure. The wall stands." (`W/kills/T22.md`, last section)
- R2-4: "Nielsen–Ninomiya covers only the free exact-chiral class." (`GX/TESTS.md:2733`). Π-QL ("nearest-neighbor" → "quasi-local") is only SUGGESTED for chirality (`C5_R2-4_report.md:296`).
- K2a: "chirality wants continuous time, one cone wants hypercubic time" (memory `candidate-law-campaign-20261008.md:39`; `CL/TEST_LOG.md:90-93`).
- PRICE_NOTE P6: chiral matter needs "an orientation and spin-transport structure" as a new primitive (`GX/PRICE_NOTE.md:168`).
- NF-1 prices P-NF1a (native staggered route with T2 content), P-NF1b (the strained law keeps Θ and P_stag), and P-NF1c (photon edge moves) (`GX/TESTS.md:9509-9511`). These are not yet in PRICE_NOTE, which ends at the v7 delta.

## (v) Open gates and owner decisions named

- **Larger coin / site algebra (M₄): parked.** Fork probe `:14`; #8741 calls one object per site "the parked site-algebra decision". T25 says the real cost is a second carrier.
- **Weak-force hand / orientation bit: parked owner decision.** `W/WALLS.md:42` (T23).
- **Owner ruling: does Admissibility fix range only (tails / quasi-local allowed)?** `W/attacks/T22.md`, premise table. The same question appears as R2-4's Π-QL and Π-FR wording prices, against `MINIMAL_AXIOMS:57-73`.
- **Matter-count reading (owner).** `VB` map `:580`.
- **Law-level CPT** (inversion added to Lattice and Admissibility). R6-5, conditional on a chiral construction.
- **Axiom-memo open gate** "staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`" (`MINIMAL_AXIOMS:206-208`).
- **Content premises P-COMP / P-ABJ** (anomaly-free completion is supplied). `W/attacks/T22.md`; test B gives a unique 7-state completion on the grid only.
- **#9395** was rejected for wholesale landing. Its claims are hypotheses in the J queue (memory `toe-walls-campaign-20260929.md:31`).

## (vi) Relevant memory lines (`~/.claude/projects/…/memory/`)

- `fork-probe-20260922.md:10`: "species kept 4+4 … NN theorem in-framework … Tension: vector-like spectrum forced; SM is chiral; 8 ≠ 16."
- `fork-probe-20260922.md:22`: probes loaded, including "filling between levels (chiral content)".
- `candidate-law-campaign-20261008.md:38-39` (K7a; K2a tension), `:111` ("D INCONCLUSIVE (chirality needs an orientation primitive)"), `:133-134` (lane RS: taste adds nothing), `:180` ("subluminal b=1.4 box … has exact doublers").
- `viability-campaign-20260927.md:22-24`: handedness results (W3 = 0; 16 nodes; tails needed).
- `toe-walls-campaign-20260929.md:31` (#9395 outcome); `:40,51` (#9409: hierarchy formula with 4 tastes gives about 214 GeV).
- `stadium-picture-20260930.md:43,47`: chirality prior-art worker died; chirality obligation = `interacting-cones-and-chiral-carriers`.
- `openai-math-and-campaign8-20261008.md:24` ("Handedness, several charges and generations are not reached"), `:37` (kill sheet order includes chirality).
- `admissibility-induced-law-block119.md:3,12`; `…block82.md:3`; `…block79.md:13` (Kaplan needs a 5th dimension); `…block77.md:3`; `…block139.md:3` (only the staggered mass keeps the books).
- No panel-*.md memory mentions chirality.

## Notes for other clusters

- **Docs claim ids surfaced** in `archive/campaigns/densify-freeze-20260904/final_front_list.txt:124-172,290,413,971,1338`, for example:
  - `cl3_chiral_cube_wilson_hop_doubling_foreclosed_narrow_no_go_note_2026-05-27`;
  - `chirality_gate_is_two_independent_gates_dirac_vs_generation_scoping_note_2026-06-08`;
  - `historic_hierarchy_exponent16_chirality_forced_doubler_negative_note_2026_05_30`;
  - `domain_wall_chiral_edge_from_achiral_cl3_bulk_2026_07_04` (runner task on ai/probes).
- **Main docs named by T22 and the handedness note:**
  - `docs/ANOMALY_FORCES_TIME_NOTE_2026-05-16.md` (`:72,101,387` call GW "external and absent");
  - `docs/THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md`;
  - `KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md`.
- **No repo hits** for Horváth's ultralocality theorem or Lüscher's chiral construction outside these packets (`C5_R2-4_report.md:71`).
- **The `.claude/science/derivations/` hits on main** (6 files, 2026-04-17) are about the "anomaly-forced 3+1 chirality parity". None is a doubling construction.
- **A worktree `claude/chirality-grid-exercise-20261014` exists** (407c33516c, "packet started"). It is presumably this exercise; it was not read.
