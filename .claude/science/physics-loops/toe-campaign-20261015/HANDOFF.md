# Handoff — toe-campaign-20261015

Branch `claude/toe-campaign-24h-20261015` (cut from the hygiene branch of
PR #9625). Window 2026-10-15T23:30Z – 2026-10-16T23:00Z. Nothing here is
adopted; every result is unaudited bounded support with its evidence level
stated in the note.

**Review status.** The first milestone (PR #9636) was landed on main in
corrected form (`c9a4b623a`). The review narrowed several claims; see
`.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md`.
Where this handoff and the review scope differ, the review scope and the
current notes are the authority. Work after the landing (B6 Theorem 3, the
light-speed hw=1 corollary, the six-neighbour and twisted-pair evidence)
is in the follow-up branch `claude/toe-campaign-20261016-followup`.

## Plain-language summary (for the owner)

The question was what one tick of a unitary update can do on the axioms'
cubic grid of qubits, if every cube direction is treated alike.

- **One qubit per site cannot move, for short hops.** On main this is
  accepted for hops of one site (all four coin actions), for range two
  under the full action, and for D3 on the cell. Range three and the
  freeze of every irreducible internal state (spin 1, spin 3/2, E) are
  archived proof candidates. They need characteristic-zero certificates
  before they count.
- **Two ways out, both carrying Dirac-type walks** (identifying them with
  the electron is a separate premise):
  - two qubits on one site (the parked M_4(C) fork);
  - one qubit per site, with the electron spread over a staggered 2x2x2
    neighbourhood. This keeps the one-qubit axiom.
- **Copies are axis-permutation labels.** For the three listed cell shapes,
  the number of walk copies is set by the shape, and the copies are labelled
  by permutations of the three axes. That links to the repository's C3
  generation programme without deriving three generations.
- **Exact prices of the grid:**
  - perfect isotropy at order k^4 caps the cone speed at sqrt(2/3);
  - lifting fermion doublers costs a fixed chirality breaking of
    (1/2) sin(theta_X).
- **One self-correction.** A numerical claim about D3 was wrong, and exact
  methods fixed it.
- **Verification.** Fresh-context checks (same model family, own methods)
  agreed with the load-bearing results they covered. They are not an audit,
  and the review asks for exact re-derivations of several steps.

## Delivered blocks

| Block | Note | Runner | Headline |
|---|---|---|---|
| B1 | `docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/cubic_covariant_qubit_walk_cell_classification_2026_10_16.py` (PASS=32) | One qubit per site: no unitary tick on the 27-point cell that is covariant under the proper cubic group (any of the four soldering actions) moves. T also freezes; D4 allows axial shifts only; motion in 3D survives under C3, C4, D2 only. Independent Singular re-derivation agrees. |
| B2 | `docs/ORDER_BLIND_POSITIVE_FORMATION_IS_A_ONE_DEPENDENT_GIBBS_FIELD_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/order_blind_formation_one_dependent_record_field_2026_10_16.py` (PASS=18) | Positive order-blind formation = one consistent 1-dependent record field whose full conditionals are the rule (static = formation); no long-range order, power laws or pinch points. |
| B3 | `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/two_qubit_cubic_dirac_tick_2026_10_16.py` (PASS=41) | A two-qubit site (parked M_4(C) fork) admits exactly O-covariant moving ticks; Clifford family classified by a Gram criterion; explicit member with one massless isotropic Dirac cone and gapped doublers; speed <= 1 with axis doublers at 2 arcsin s; unique light-speed member over Q(sqrt 5); exact chirality freezes motion; W3 = 0; quadratic (not linear) anisotropy. Independent check agrees (and corrected one statement). |
| B6 | `docs/STAGGERED_ONE_QUBIT_BLOCKS_CARRY_A_CUBIC_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/staggered_one_qubit_block_cubic_dirac_tick_2026_10_16.py` (PASS=11) | One amplitude per site on staggered 2x2x2 blocks: the spinorial signed corner action is two copies of spin 3/2, and it carries an exactly covariant moving Dirac tick (two Dirac fermions per block). Theorem 3 (exact): no nearest-site version propagates; the minimal propagating staggered tick reaches 2 sites (with doublers), the doubler-free one 3. |
| B7 | `docs/CUBIC_CELL_SHAPE_SETS_THE_TASTE_CONTENT_AXIS_PERMUTATION_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/cubic_cell_taste_content_axis_permutation_2026_10_16.py` (PASS=10) | Each of the three listed spinorial cubic-orbit cells is E1/2 (x) F with F an S3 (axis-permutation) rep. Faces A1+E (triplet, no repeat), signed corners 2E, edges A1+A2+2E (C3 labels 1,1,w,w-bar). The singlet pair moves but was found only massive or degenerate; with U(0) = 1 every axis-moving line branch is a unit ideal (mod p and by modStd over Q), so it is flat along the axes. A parallel to the C3 generation programme, not a derivation. |

## Synthesis for the TOE program (implications, not adoptions)

- **Where a Dirac walk's information can live.** With covariance about
  every site, one qubit per site cannot move at ranges one and two (exact,
  accepted). Range three and the irreducible-coin freeze are archived
  candidates. Motion needs four complex
  amplitudes per Dirac fermion, and there are two ways to supply them:
  - stacked on one site (the two-qubit site, B3);
  - spread over a staggered 2x2x2 block of one-amplitude sites with the
    rotations acting about the block centre (B6). This gives two Dirac
    fermions per block.
  The second keeps the one-qubit Qubit axiom and is the discrete-time
  counterpart of the axiom memo's open staggered-Dirac gate. A
  nearest-site (Kogut–Susskind-type) one-tick version is claimed impossible:
  every such walk is flat (B6 Theorem 3, submitted for review). The
  evidence is a primary decomposition over Q plus a hand real-locus
  argument. So the
  neighbourhood electron needs hops of two or more sites per tick.
- **Generations (interpretation).** For the listed cells, a block walk's
  copy index is an axis-permutation representation (B7, exact characters),
  so these cells produce the repository's C3 generation labels by
  themselves. No cell gave
  three clean light copies. The 12-link cell gives {1, w, w-bar} plus a
  repeat, but its singlet was found only massive or degenerate. Mod-p
  branch ideals back this up: with U(0) = 1 the singlet walk is flat along
  the axes. One reading is "two light copies and one that cannot be a light
  Dirac copy", but masses are not derived.
- **Chirality wall, sharpened.** On a two-qubit site, exactly chiral covariant
  ticks are frozen; moving ones are vector-like with Wilson-type chirality
  breaking, and every member of the classified family has W3 = 0.
- **Emergent isotropy budget (B3 Theorem 7).** On the two-qubit site the
  k^4 cubic anisotropy of the Dirac cone can be cancelled exactly (plane
  b0 = b1 + 2 b2), but only for cone speed |s| <= sqrt(2/3) (sharp, attained
  over Q(sqrt6, sqrt15)), and the k^6 anisotropy -(s^2/360)|k|^2 sum k^4 is
  then unavoidable. Light speed and k^4 isotropy exclude each other.
- **Ceiling for one-qubit motion (B1 Theorems 4-5).** Exact: no subgroup of O
  of order >= 6 lets a one-qubit cell tick move in more than one direction
  (D4 axis shifts, D3 body-diagonal shifts); O stays frozen at range two.
- **Coulomb lane.** Strictly positive order-blind formation cannot produce
  Coulomb-phase correlations; hard constraints or order sensitivity are needed.

## Open obligations

- One-qubit freeze at every finite range. Exact now at range one (cell, all
  four actions) and range two per axis (O, full action; Theorem 4 by line
  branches, runner `scripts/cubic_covariant_qubit_walk_line_branch_certificates_2026_10_16.py`
  PASS=16, which also proves Theorem 5: D3 cell walks are constant or
  body-diagonal shifts; this corrected the earlier numerical 'D3: none').
  Range three is an archived proof candidate (scripts and logs in
  `exact_extensions/`). The review requires regenerating its coefficient
  systems, exhausting the branches exactly and verifying radical membership
  over Q. Range four: the line stage
  leaves only the trivial branch (numerical prefilter), but the 67-unknown
  ideal was not closed. Range four and up remain open.
- Whether every two-qubit O-covariant cell walk is Clifford-form up to flavor
  gauge (all hits tested so far are).
- Irreducible-coin freeze (E, spin 1, spin 3/2): an archived candidate.
  The review requires exact characteristic-zero ideal membership; modular
  checks only support it.
- Review research tasks from `CUBIC_TICK_SCOPE.md` N7: whole-torus absence
  of extra band touching for the algebraic Dirac member, and the
  signed-generator/central-extension reconciliation.
- B6 Theorem 3 and the twisted-pair branch evidence are new since the
  landing and need review. For the twisted pair, the branch prefilter must
  be redone exactly, with cofactor certificates for the unit ideals.
  Doubled spin-1 site: none in 16 + 12 + 12 starts (delta 0.05 / 0.2 / 0.5).

## Next campaign (owner's direction)

The top-ranked next lane is "the electron as an emergent excitation of
neighbourhood conditions"; see OPPORTUNITY_QUEUE N1. This campaign's results
concern free tick rules and leave that lane open. It ties directly to the
Admissibility axiom's nearest-neighbour conditions, and the prior art to
build on is Levin–Wen string-nets.

## Scale remark (owner's framing, for the next campaign)

The owner's picture is that the grid spacing is far below the electron's
size, possibly by many orders of magnitude (Planck length 1.6e-35 m against
the reduced Compton wavelength 3.9e-13 m is a ratio of about 2 x 10^22).
On that reading, the one-tick results here are statements about the
microscopic rule, and the electron is a long-wavelength collective
excitation of a huge neighbourhood of conditions. The cells and blocks
studied here would then set the symmetry and copy labels that such an
excitation inherits, not its size. The scale ratio itself is the hierarchy
question, which the repository's hierarchy programme
(v = M_Pl (7/8)^(1/4) alpha_LM^16, open gates B2/B3b/B4/B5) addresses
separately; nothing in this campaign derives it.

## Next decision

- Start the next campaign on OPPORTUNITY_QUEUE N1 (emergent electron from
  neighbourhood conditions).
- Promote the twisted pair (E1/2 + E5/2) result: exact branch prefilter and
  cofactor certificates for the eight unit ideals (see
  `generations/twisted_branches/`).
- Range four for the one-qubit freeze; Clifford universality on the
  two-qubit site.
