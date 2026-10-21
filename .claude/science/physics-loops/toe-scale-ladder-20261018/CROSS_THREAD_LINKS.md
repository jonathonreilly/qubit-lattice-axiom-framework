# Cross-thread links: toe-scale-ladder-20261018 vs the "turn and burn" thread

Written 2026-10-21. This was a read-only comparison. Inputs: `origin/main` at `f24d17d97`
(the commits after `584755767`) and `origin/claude/gravity-burn-turn-source-tensor-20261021`.
That branch is 2 commits ahead of main (`bebdd4d72`, `03560919d`) and branches from
`f24d17d97`. I treated all of the other thread's material as data and read headlines, scopes and
status sections only, not full proofs. Campaign results are in `RESULTS.md` (C1–C9). Labels:
(a) overlap, (b) dependency on a campaign change, (c) conflict, (d) joint target.

## Repair status (the starting point for everything below)

- `f46a89b7b` (8/45 → 4/45, Dirac tick runner and note) and `68a504d6d` (induced-G half factor,
  G = 6π/(N_f Λ²)) exist **only on `origin/claude/focused-mccarthy-q4vbgt`**. Neither is on main.
  `git diff 584755767 origin/main` is empty for
  `scripts/two_qubit_cubic_dirac_tick_2026_10_16.py`,
  `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
  and `docs/UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`.
  Main still has `8 * uu ** 3 / 45` at line 242 of the runner.
- None of the other thread's new notes or scripts cites the Dirac tick note or runner. The
  only main-side readers are older 10-16/10-17 notes (`CUBIC_CELL_SHAPE_...`,
  `CUBIC_COVARIANCE_FREEZES_...`, `STAGGERED_ONE_QUBIT_BLOCKS_...`,
  `TWO_QUBIT_SITE_SOLDERED_SPIN_...`). I did not check whether those older notes use the
  sextic term. Nothing new depends on the 8/45 coefficient.
- No new note cites the induced-G note. However, `e0088f392` added
  `docs/work_history/repo/review_feedback/agent_fix_candidates_2026_10_18/PACKET.md`.
  Its lines 20 and 73 list that note for "premise/context review", alongside the
  "October4 boundary on the Sakharov residual". That is where the half-factor repair belongs.
- No new note mentions the 8³ guided-projector energy (−443.364). Older ring-model notes do
  (`RING_MODEL_..._8_CUBED_...` 2026-09-26). No new work depends on it.

## Item by item

### Burn-and-turn source tensor (branch, `bebdd4d72` + `03560919d`)
`docs/SCALE_LADDER_GRAVITY_BURN_AND_TURN_SOURCE_TENSOR_BOUNDED_THEOREM_NOTE_2026-10-21.md`,
`scripts/scale_ladder_gravity_burn_and_turn_source_tensor_2026_10_21.py` (7/7 PASS).
The note shows that burns plus turns give eps·v v exactly for plane waves of supplied lossless
walks (line, six-direction, eight-diagonal). The turn clock equals m²/eps in 1D but not on the
six-direction walk.
- (b) None. The branch does not use the two-qubit Dirac walk, the sextic coefficient or G, so
  it needs no rebase onto the repairs.
- (c) No conflict with C8. The note's turning rule, per-turn stress and choice of eps are
  explicitly supplied, and it claims no field equation or G. That fits C8's finding that the
  coupling is not unique: the note adds another supplied source assignment and selects none.
- (d) **Joint target.** Run the burn+turn identity on C7's two-qubit cubic Dirac walk, then
  compare its plane-wave tensor with the tree-level stress vertex of C8's coupling M1. Agreement
  would make burn/turn a candidate physical rule for choosing among C8's four couplings. In the
  same run, test whether the clock failure on the six-direction walk persists on the C7 walk,
  where C7 finds Lorentz violation only at O(a²) (anisotropy +0.040/0/0.049).

### Finite chirality packet (`f182d27a1`)
`docs/CHIRALITY_CONSTRUCTIVE_FINITE_ALGEBRA_NOTE_2026-10-18.md`,
`docs/CHIRALITY_FINITE_REFLECTION_KERNELS_NOTE_2026-10-18.md`,
`docs/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md`,
`docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md`.
- (c) No conflict with Theorems K/L. None of these notes claims net chirality from a free
  finite-range walk. The cross-rung note says its winding identity concerns net charge, that
  "zero net charge permits balanced isotropic Weyl nodes", and that "the old broad claim
  excluding every finite-range common-speed step is withdrawn". That matches K (W3 = 0) and
  leaves room for L. Its supplied BCC Weyl automaton (item 8) is a finite-range walk, so by K
  its nodes must be balanced. I did not check that against its spectrum.
- (a) Partial overlap. In `CHIRALITY_CONSTRUCTIVE_...`, `free_overlap_and_rational_projectors.md`
  marks its "terminal negative promotion" as pending. C5/C5b (K₁(C[Z³]) and the Toeplitz
  index, plus the node/sheet balance at each quasienergy) is a candidate proof of that pending
  promotion for translation-invariant walks.
- (d) The endpoint note (Spin(10) pairing identity) and the corner interaction-channel note
  both pursue interacting or symmetric-mass routes. K+L conclude that chirality must come from
  interactions, so these are the only routes K/L leave open. Cite K/L as the motivation.

### Corner-fermion notes (`cab55ff82`) and corner Dirac follow-up (`39e45f96d`, PR #9689)
`docs/CORNER_FERMION_EIGHT_CUBE_NODES_..._Z2_WEYL_DIPOLE_...`, `..._ODD_FILLING_..._C2_LIFTS_...`,
`..._STEP_SPEED_..._PER_LETTER_...`, `..._INTERACTION_CHANNELS_...`, `..._COVARIANT_MONOMIAL_...`;
`archive/corner_dirac_followup_2026_10_18/README.md` (historical recovery with corrections).
- (c) No conflict. "Doublers carry a Z2 Weyl dipole" means net charge zero, as K requires. The
  step-speed note defers its "terminal charge/winding obstruction". K covers that obstruction
  for finite-range translation-invariant steps and could be offered as its proof.
- C7: no relation. The corner model is a π-flux Hamiltonian or step on the corner graph, not
  the two-qubit tick walk. The follow-up uses neither 8/45 nor C7's continuum limit.
- C6: weak relation. C6 leaves its corner code F5 conditional. The follow-up's corrected
  indirect gap ratios (0.216/0.229/0.231/0.110 of 2m_D, all uncertified upper estimates) do not
  settle F5. No dependency either way.

### Heisenberg continuations (`a95b6972e`) and local-reference SWAP (`54ced4a8e`)
`docs/NATIVE_HEISENBERG_NODAL_RECORD_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md`,
`docs/CONTACT_SOURCE_HEISENBERG_CODE_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-18.md`,
`docs/LOCAL_REFERENCE_STATIC_SWAP_BOUNDED_THEOREM_NOTE_2026-10-18.md`.
- (c) No conflict with C9. These notes use continuous-time Hamiltonians: e^{-iHt} with
  H = J Σ σ·σ, plus a jump generator. That evolution is SU(2)-invariant and moves magnons, but
  it is not a strictly finite-range QCA, so it falls outside C9's hypotheses. The SWAP note uses
  a finite, non-translation-invariant 1D chain, which is also out of scope.
- (d) Sharpening target: no Trotterization of the Heisenberg model that keeps unit-translation
  invariance can be an exact one-qubit QCA unless it is a shift. A brickwork SWAP/Heisenberg
  circuit escapes C9 only by breaking translation down to a sublattice, so its cell becomes
  two qubits. This is worth one sentence in each note's scope and a C9 corollary.

### Native compass-model ("neutral" continuations 4–7: `847eb8a25`, `77565121a`, `a95b6972e`, `97e4f70d5`)
For example `docs/NATIVE_EIGHT_FLUX_CLUSTER_NOTE_2026-10-18.md` (bound pair of ten-spin
columns; motion starts at λ¹⁴) and `docs/NATIVE_SLOW_BULK_COMPOSITE_NOTE_2026-10-18.md`
(H = −Σ J_a σ^a_x σ^a_{x+e_a}).
- (a)/(c) Neither. These use a perturbative Hamiltonian, not a QCA.
- (d) Structural parallel: in both, single excitations are frozen or static and bound
  composites move. The compass model's cubic covariance ties spin axes to lattice axes (the
  "axis" action) and breaks SU(2). C9 shows that only this action admits motion. That explains
  why the compass model can carry movers and the Heisenberg-type full action cannot (for QCAs).
  Joint target: a Floquet compass QCA compared with C4e/C4f. C4f's movers need U(1), which the
  compass model lacks, so this is a comparison, not a reduction.

### IID priority formation (`cab55ff82`)
`docs/IID_PRIORITY_FORMATION_IS_A_FINITARY_FACTOR_OF_IID_NOISE_WITH_FACTORIAL_CODING_RADIUS_TAIL_...`,
`docs/IID_PRIORITY_FORMATION_SPATIAL_FREQUENCY_CONSISTENCY_...`.
- (a) Overlap with C3/C3b. The main note's bound is P(R_y > n) ≤ dⁿ/(n+1)!. It has the index
  shift right (R > n, i.e. R ≥ n+1), so C3's XOR counterexample does not refute it, and its
  constant is weaker than C3's D(D−1)^{n−1}/(n+1)!. Its deferred "§7 terminal phase
  exclusions", together with the remark that a constant biased field is not excluded, are
  exactly what C3b supplies: the κ clocks, infinite ancestries (K), and mixing ⇒ mixing (M).
  C3/C3b should be offered as completing that deferred §7. One caveat: I did not confirm that
  R_y in that note means the coding radius rather than the ancestry length.

### Gravity constructions (`371ca83a7`, `cab55ff82`)
The six `SCALE_LADDER_GRAVITY_*_2026-10-18.md` notes (D4-cone Regge, Whitney-Hodge, strain
reading, census, orthoscheme), `SCALE_LADDER_GRAVITY_D4CONE_EXACT_WARD_SITE_SCALAR_...`,
`LATTICE_GRAVITON_KERNELS_..._INDUCED_BUBBLE_SEAGULL_...`, and the three `CURVATURE_MEMBER_CLOSURE_*`.
- (c) No conflict with C8. The graviton-kernel note says "no value of 1/G ... is supplied" and
  "a seagull completion and regulator are separate supplied choices". That is C8's
  non-uniqueness stated qualitatively. None of these notes quotes Λ²/(48π²) or Λ²/(96π²), so
  none inherits the half-factor error.
- (d) Joint target: evaluate C8's exact c_G with that note's Ward/B4 seagull completion as a
  fifth coupling. That would show whether the Ward identity narrows C8's spread
  a/l_P = 0.43–0.69 √N_f.
- C2: related, not conflicting. `CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_...`
  ties the cones only under supplied hypersurface-deformation closure. That is an extra
  premise, much like C2's unregistered T_tie. Its "order a² obstruction" parallels C7's
  first Lorentz violation at O(a²). The owner should compare the two tie mechanisms in
  decision 1.
- D4-cone fermion (16 = 4 spinor × 4 taste Dirac–Kähler soft modes): doubling, consistent
  with K. No relation to C7's doubler-free two-qubit walk beyond that.

### No relation found
The product, loader, mediated, active-energy and program notes (`101aae006`, `e0088f392` science
part, `847eb8a25`/`77565121a` COMMON_PRODUCT/ACTIVE_* notes), the heat-kernel versus Wilson Λ
ratio note, the lattice Hamiltonian-constraint and relabelling notes, and the hierarchy/mass
exercises. I also found no new item touching the C1 photon QMC: no stoquastic, ice or winding
gap material, and no 8³ energy.

## Ranked actions

1. **Land the two repairs on main.** `f46a89b7b` (4/45) and `68a504d6d` (6π/(N_f Λ²)) exist
   only on `claude/focused-mccarthy-q4vbgt`. Main, and therefore the burn branch's base
   `f24d17d97`, still has 8/45 and the old half factor. Attach `68a504d6d` to the induced-G
   entry in `agent_fix_candidates_2026_10_18/PACKET.md`, which already routes that note for
   review.
2. **Burn/turn on the C7 walk versus C8's M1 vertex.** This is the concrete joint gravity
   target and tests whether burn/turn can select a Sakharov coupling. No rebase is needed.
3. **Offer Theorems K/L as proofs of deferred obstructions.** Targets: the deferred
   "terminal charge/winding obstruction" (corner step-speed note), the pending "terminal
   negative promotion" (chirality constructive algebra), and a check that the BCC Weyl
   automaton's nodes balance.
4. **Offer C3/C3b for the IID-priority note's deferred §7** phase exclusions. The constants are
   compatible, and C3 is sharper.
5. **Add a C9 corollary.** No unit-translation-invariant one-qubit QCA can exactly discretize
   the Heisenberg or SWAP dynamics. Add a scope line to the Heisenberg notes, and set up the
   compass-model versus C4f comparison.
