# Handoff — toe-campaign-20261017

Branch `claude/toe-campaign-12h-20261017`, cut from
`claude/toe-campaign-20261016-followup` (PR #9658). C1 landed on main via
#9660. Later blocks go out in fresh PRs from main, starting with
`claude/toe-campaign-12h-20261017-c2`. Window
2026-10-16T23:40Z – 2026-10-17T11:40Z. Lane: the electron as an emergent
excitation of neighbourhood conditions (owner's direction). Nothing here is
adopted; every result is unaudited bounded support with a declared model.

## Final state (2026-10-17T15:46Z)

- The campaign is closed and the hourly task is deleted.
- C1–C15 are on main. C16, C17 and C18 are in PR #9671.
- **Next:** queue item 0++, a direction-carried charge with no site term.

## The arc in one paragraph (for the owner; interpretation, not a claim)

- C1–C4 give scoped Pauli-class obstructions and finite search results; no general nearest-neighbour fermion exclusion is established.
- BKSF supplies fermions in a declared plaquette-supported model (C6; site-local C11).
- Bare permutations give finite pair eigenvalues consistent, under the stated localization relation, with restricted w2 for D3 and single-C2 stabilizers; D2 localization remains open. The bare BKSF family has rotation orbits of at least four codes.
- Supplied conditional dynamics distinguish the rotation realizations. Majorana-only and number-conserving hopping are modeling choices; no physical electric charge or electron spin-charge relation is derived.
- **Next.** To make a prediction, the framework has to fix how rotations
  act inside a site, and whether there is a conserved charge.

## C18: the large fermion (owner's "electron much larger than the grid")

- **One spin-1/2 doublet at long wavelengths.** For square = plaquette = tube = π, the site rotations fix exactly two crystal momenta, ±k* (affine action from the PSG). The corner fermion's band minimum is a single 2-fold level there. It has an isotropic mass, with anisotropy only at δk^4, and carries spin-1/2 (E1/2).
- **The effective theory.** A wavepacket much larger than the grid is a nonrelativistic spin-1/2 particle if the hopping keeps I·K (inversion × conjugation). If I·K is broken it is a spin-1/2 Kramers–Weyl fermion, linear and relativistic-looking (independent check).
- **The qubit count.** The 48 qubits per site embed equivariantly into 5^3 blocks of one qubit per fine site.
- **Open.** A uniform one-qubit rule producing the blocks; Dirac structure; charge.

## C17: a qubit code whose emergent fermion carries the spin-1/2 class under a genuine cube-rotation action

- **Construction.** The fermion lives on the 12 corners (perpendicular direction pairs) of each site, off the C4 axes. It sees a π flux around every lattice line. The code uses 48 qubits per site, all on sites.
- **The action.** Rotations act as a genuine linear representation of O on the whole Hilbert space: site permutation, on-site CZ network, Z fixes, and a repetition-stabilizer coboundary.
- **The class.**
  - The pair test gives w2 + w1^2.
  - With the twist W on the odd elements (natural for number-conserving dynamics), all nine C2 give +1. That is w2, the spin-1/2 class.
- **The local doublet.** A chiral on-site term makes an E1/2 doublet the cluster ground state.
- **Caveat (independent check).** Only the point group about a site matches spin-1/2. The full space group differs: C4 T C4^-1 T^-1 = -1 on the fermion, and bond-centred C2 give -1.
- **Open.** A mobile doublet as the lowest band state; dynamics selection; a flux pattern whose space-group fractionalization is that of spin-1/2.

## C16: why the cube-invariant realizations came out spinless; the six-direction shell

- **Obstruction (conditional on symmetry localization).** If a rotation
  group H about a site maps the Hamiltonian's Pauli terms to terms and the
  fermion can sit on an H-invariant violated-term pattern, then its local
  state is one-dimensional. So its class lies in
  ker(H^2(H;Z2) -> H^2(H;U(1))).
  - For O this kernel is {0, w1^2}, never w2.
  - w2 forces degeneracy exactly for D2, D4, T and O. Cyclic groups and D3
    do not, which is consistent with C8.
- **Where it applies.** Under the on-site Clifford realizations, the
  single-site charge pattern (B_v violated) is invariant: every generator
  maps to plus a generator. This explains the spinless results for C12 and
  C13.
- **Where it does not (independent check).** Under the bare permutation the
  term set is not preserved. The single-fermion pattern picks up plaquette
  violations near v, including for all 12 axis C2 of the order-4 codes. So
  the obstruction does not apply there. That is a concrete candidate
  resolution of the order-4 tension, not a proof.
- **The sharpened target needs one of two things.**
  - No charge term whose support is O- or D4-invariant about a site, so no
    site-centred charge term like B_v.
  - Or an action that mixes degenerate terms. That is C15's route, where
    the spin was inherited.
- **The owner's count.** One qubit per connecting direction gives the
  smallest allowed shell: the six direction positions.
  - For a spin-1/2-class charge they split as a doublet plus a quartet
    (E1/2 + G3/2, or E5/2 + G3/2).
  - For a trivial class they split as A1 + E + T1.
- **Note:** `docs/SITE_LOCALIZABLE_STABILIZER_CODE_FERMION_CANNOT_CARRY_THE_SPIN_HALF_CLASS_DIRECTION_SHELL_BOUNDED_THEOREM_NOTE_2026-10-17.md`.
- **Runner:** PASS=11, 3 s.

## C15: supplied matter doublet; conditional spin-class identification

The construction:
- add two matter modes per site (spin up and spin down) that share the C12 code's Z2 gauge field;
- let rotations act on that pair as a spin-1/2 doublet.

The five-qubit/site model has a dressed fermionic charge with two matter states and an exact supplied on-site spin-1/2 action. Its relative pair factors have the w2 sign pattern, but a local matter spinor changes that pattern: this is inherited on-site spin, not an established anyon-invariant fractional class. The code subspace is invariant; no common invariant link ground vector is constructed.

This construction supplies two matter modes and their spin action. Whether the framework derives them remains open; they are not proved necessary for every construction.

## Realization dictionary: the emergent fermion's half-turn signs

The rotation class eta_f is detected by the squares of the half-turns. In each entry, "+" means
C2^2 = +1 on the fermion (spinless) and "-" means C2^2 = (-1)^F (spin-1/2-like). The pair-test sign
lambda = -eta_f only under the stated localization relation; consistent D2 localization is open. C12 entries are clean-representative signs: local Majorana dressings can change them, so they are not unrestricted anyon invariants.

| Code | How rotations act | Group covered | Axis C2 | Edge C2 | Class |
|---|---|---|---|---|---|
| BKSF, edge or half-edge (C8, C11) | bare permutation | D3 or single C2: conditional class; D2: individual pair-derived signs only | - | - | restricted w2 conditional; D2 localization open |
| BKSF, D3 or single-C2 code | bare permutation, twisted by W on the C2 (sign character) | stabilizer | n/a | + | trivial |
| BKSF, order-4 code | bare permutation, twisted by W along a character | D2 | two of the three C2 flip | | conditional (+,+,-)-type pair-derived signs; D2 localization open |
| BKSF, half-edge (C13) | on-site CZ network times permutation (Majorana permutation) | all of O | + | + | trivial |
| Majorana-per-direction (C12) | on-site signed Majorana permutation U_R | all of O | + | + | clean-sector trivial pattern; not an anyon invariant |
| Majorana-per-direction (C12) | U_R twisted by W on odd elements | all of O | + | - | clean-sector sign-pullback pattern |
| Either family | any W-twist | all of O | | | w2 on all of O not reachable |

Here W = prod_v exp(-i pi B_v / 4). In BKSF, W = const * e^{i pi N / 2}, a quarter-turn of fermion number.
The supplied conditional Majorana-only hopping model selects the trivial-class realizations. A single species with w2 on all of O is open.

**A tension.** w2 restricted to D2 has all three squares -1, the quaternion class. A nondegenerate
fermion (one local state) can only carry even-minus patterns on D2. So w2 on any group containing three
orthogonal C2 needs a Kramers-like doublet. This includes all of O. In the order-4 BKSF codes the bare
action shows the odd pattern, so either the action has a localization obstruction or lambda = theta*eta
fails there. Open, and ranked first in the queue.

**And so, for the owner:** a fermion that is spin-1/2 under all 24 cube rotations must come with two
internal states, as the electron does with spin up and spin down. A single-state fermion cannot do it,
whatever the rotation action. That is the next target.

## Plain-language summary (for the owner)

- **The supplied one-qubit Pauli stabilizer class has no three-dimensionally
  mobile fermionic defect.**
  - The seven-site star support, commuting Pauli conditions and four actions
    on Pauli labels are declared mathematical choices. They are not derived
    from Admissibility or required by the axioms' cubic symmetry alone.
  - Under the axis/full actions the nontrivial rule is Chamon's; nonzero
    charges have translation rank <= 2 (including lineons and planons), and a single defect is immobile.
  - Under trivial/sign actions the rules are single-label or cluster-type;
    the stated statistics argument excludes mobile fermionic charges, not
    all mobile defects.
  - No physical electron exclusion or general free-tick obstruction follows.
- **The supplied two-qubit soldered-spin Pauli class (C2).**
  - In every such rule, an operator that commutes with all free single-site
    variables cannot preserve a nonzero charge under three independent
    translations.
  - Rules without free local variables therefore have no charge with
    three-dimensional mobility.
  - The rule "spin Chamon (x) flavour X on the neighbours" has eight elementary basis
    charges (256 total classes including zero). Each elementary charge moves by any even translation, and each nonzero such move anticommutes
    with a free flavour variable.
  - *Interpretation for the owner, not a claim:* there, three-dimensional
    motion is tied to changing extra local data along the path. That would
    be expected to spoil coherent propagation, which is not computed.
- **The supplied three-axis-qubit class (C3).**
  - With labels that do not turn with space, eight interleaved toric codes
    give a covariant star rule whose charges move coherently in three
    dimensions, with bounded code dimension. The charges are bosons.
  - For the stated soldered rotation-fixed class, the rank-growth proof and alphabet lemma exclude the conjunction of bounded code dimension and free-single-site-variable-preserving charge motion. The exact odd-L specialization argument supplies the unbounded subsequence.
- **The fermion search (C4).** Among the 36 supplied maximal unsoldered C4/C3-fixed rules selected by equal nonzero log2 code dimension at L=4 and L=6, every nonzero same-site charge pattern for which the radius-1 tube solver finds legs from 0 to 4e_x,4e_y,4e_z in the radius-5 box has T-junction sign +1. The finite rank selection is not an asymptotic classification of all bounded-dimension rules.
  - These supplied Pauli models do not classify all nearest-neighbour models on one to three qubits. Other supports, strides, non-maximal rules and arbitrary-support fermionic sectors remain outside this search.
- **C5 exploration (no note).** A quick test of "framed" toric codes found
  apparent fermions. They were an artifact of the statistics solver, whose
  leg operators could cross. With properly confined legs, all were bosons.
  The tool is now fixed and the C4 result re-checked.
- **C6: Bare BKSF codes require an orbit of at least four under cubic permutations.**
  - The standard qubit encoding of fermions, BKSF, always gives genuine
    fermions.
  - None of its 60 translation-invariant versions is symmetric under all 24
    cube rotations. The most symmetric ones are symmetric only about a body
    diagonal.
  - So a rotation-symmetric arrangement needs at least 4 copies, one per
    body diagonal.
  - *Interpretation for the owner, not a claim:* rotations act on the four
    diagonals as "1 + 3", a singlet plus a triplet labelled like
    generations. In this simple stack, though, the four copies cannot mix
    as real generations do; making them mix needs couplings not yet built.
- **Next:** couple the four BKSF copies so the species can mix (C7), and
  test other fermion encodings for full rotation symmetry.
- **Spin of the BKSF fermion under lattice rotations (C8).**
  - Give each plaquette orientation a sign: 8 sectors, all valid. In the
    zero-flux and pi-flux sectors, every rotation that fixes a code acts on
    the qubits as a plain permutation.
  - All 108 finite pair tests give lambda=+1. With the stated lambda=theta eta localization relation this yields eta=-1 per tested C2. D3/single-C2 class inference is conditional; consistent D2 localization remains open.
  - Historical earlier sign claims were corrected; finite pair data do not by themselves certify a localized D2 action.

- **The fermion can live on the framework's sites (C11).** Give each site
  six qubits, one per direction, and tie the two halves of each edge
  together. The fermion code then lives on sites, and the framework's own
  site rotation reproduces everything above exactly. The bare-action four-code orbit minimum, finite pair data and conditional D3/single-C2 inference carry over; D2 localization remains open. The cost: six qubits per
  site, and conditions that span a plaquette rather than just a site's
  nearest neighbours.

- **One fermion species with full cube symmetry (C12).** Use three qubits
  per site holding six "half-fermions" (Majoranas), one per direction.
  - This code has a single fermion species and is symmetric under all 24
    rotations, provided a rotation may act inside a site by a simple
    unitary that permutes the Majoranas with signs.
  - So the "at least four species" result depends on rotations acting by
    pure qubit relabelling. Confirmed directly (C13): the same BKSF codes,
    in the six-qubit site form, become symmetric under all 24 rotations
    once a rotation may shuffle the site's Majoranas. Under that shuffling
    action the fermion is spinless. Under pure relabelling the finite pair data support conditional D3/single-C2 inference; D2 localization remains open. Same code, two readings of "rotate". How the framework's rotations act on a site's
    qubits is therefore a real modelling choice with physical
    consequences.
  - Spin: with the plain on-site action this fermion is spinless. An
    on-site phase built from the site parities, which does nothing in the
    ground state, can be added only on the "odd" rotations. That makes the
    edge half-turns spinorial but not the axis ones. The full spin-1/2
    pattern under all 24 rotations is not reached this way; an
    independent check refuted an earlier claim that it was.

## Blocks

| Block | Note | Runner | Headline |
|---|---|---|---|
| C12 | `docs/MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17.py` (PASS=8) | Three qubits per site, six Majoranas: one fermion species covariant under all 24 rotations (on-site Cliffords, group sign-pullback central extension (A4 semidirect Z4)); clean-representative trivial pair pattern under U_R; not an unrestricted anyon invariant; sign twist gives (axis +, edge -); w2 on O not reached. |
| C11 | `docs/BKSF_CUBIC_FERMION_CODES_SITE_LOCAL_REALIZATION_WITH_SIX_DIRECTION_QUBITS_PER_SITE_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_site_local_six_direction_qubit_realization_2026_10_17.py` (PASS=6) | Six direction qubits per site: framework site rotation = edge rotation exactly; C6 bare-action orbit bound and C8 finite pair data transfer; conditional D3/single-C2 inference, D2 localization open. |
| C8 | `docs/BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py` (PASS=9) | All 108 finite pair tests give lambda=+1. With the stated lambda=theta eta localization relation this yields eta=-1 per tested C2. D3/single-C2 class inference is conditional; consistent D2 localization remains open. |
| C6 | `docs/BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_rotation_orbits_2026_10_17.py` (PASS=8) | 60 translation-invariant BKSF codes, all with a fermionic charge; none rotation-invariant; minimal orbit 4 (D3, body diagonals). |
| C4 | `docs/THREE_AXIS_QUBIT_SYMMETRIC_STABILIZER_RULES_FERMION_SEARCH_FINDS_NO_COHERENTLY_MOBILE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py` (expected PASS=9 (10 with --full)) | Soldered rank bounds exclude bounded dimension together with free-variable-preserving charge motion. Among the 36 supplied maximal unsoldered C4/C3-fixed rules selected by equal nonzero log2 code dimension at L=4 and L=6, every nonzero same-site charge pattern for which the radius-1 tube solver finds legs from 0 to 4e_x,4e_y,4e_z in the radius-5 box has T-junction sign +1. The finite rank selection is not an asymptotic classification of all bounded-dimension rules. |
| C3 | `docs/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/three_axis_qubit_site_stabilizer_rules_soldering_and_three_dimensional_charge_mobility_2026_10_17.py` (expected PASS=11 with Singular) | Unsoldered: interleaved toric codes, coherent 3D-mobile bosons. Soldered (C4/C3-fixed): no maximal rule with bounded code dimension and 3D-mobile charge. |
| C2 | `docs/TWO_QUBIT_SITE_SOLDERED_SPIN_STABILIZER_RULES_THREE_DIMENSIONAL_CHARGE_MOTION_FLIPS_A_FREE_LOCAL_VARIABLE_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/two_qubit_site_soldered_spin_stabilizer_rules_charge_motion_flips_free_local_variable_2026_10_17.py` (PASS=17 with Singular) | Free-variable-preserving operators never give a charge rank-three mobility; rules without free local variables have no 3D-mobile charge; example rule with 8 basis charges (256 classes) mobile by even steps. |
| C1 | `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py` (PASS=20) | Soldered: Chamon only, with fracton defects (no 3D mobility; lineons and planons; nonzero charge translation rank <= 2; elementary charge immobile). Unsoldered: classical or cluster rules. No 3D-mobile fermionic defect in the class. |

## Open obligations
- C1 and C2 independent checks: done. C2's first classification statement missed the E orbit; this is corrected and checked by the runner.
- C3 onwards in OPPORTUNITY_QUEUE.

## Next decision
- C3 independent check: done. It corrected the validity of three large unions (they contain -1); the conclusions are restated through the rank bound.
- C4 historical independent check: confirmed within its finite search domain; no arbitrary-support classification follows. Next: C5, low-symmetry generators (framed fermion codes).
