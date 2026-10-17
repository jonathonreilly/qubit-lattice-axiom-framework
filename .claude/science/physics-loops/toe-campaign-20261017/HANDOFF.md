# Handoff — toe-campaign-20261017

Branch `claude/toe-campaign-12h-20261017`, cut from
`claude/toe-campaign-20261016-followup` (PR #9658). C1 landed on main via
#9660. Later blocks go out in fresh PRs from main, starting with
`claude/toe-campaign-12h-20261017-c2`. Window
2026-10-16T23:40Z – 2026-10-17T11:40Z. Lane: the electron as an emergent
excitation of neighbourhood conditions (owner's direction). Nothing here is
adopted; every result is unaudited bounded support with a declared model.

## The arc in one paragraph (for the owner; interpretation, not a claim)

- **Nearest-neighbour rules give no fermion.** Simple symmetric rules on
  one, two or three qubits per site, with each condition on a site's
  nearest-neighbour star, never produce a freely moving fermion (C1–C4).
- **Fermions appear one step up.** Once conditions span a plaquette and
  each site carries several direction-labelled qubits, fermions appear
  (BKSF, C6; site-local version, C11).
- **What spin they carry depends on how a rotation acts on a site's
  qubits.**
  - If rotations only move qubits around, the fermions are spin-1/2-like
    (C8). But no single fermion type is then fully cube-symmetric: at
    least four come together (C6).
  - If a rotation may also apply a fixed local unitary inside each site,
    one fermion type can be fully cube-symmetric (C12). It is then
    spinless, or spinorial for some half-turns only. The full spin-1/2
    pattern was not reached.
  - Pure Majorana-type dynamics prefers the spinless choice.
    Charge-conserving dynamics ties the choice to the electric charge, as
    in the electron's spin-charge relation.
- **Next.** To make a prediction, the framework has to fix how rotations
  act inside a site, and whether there is a conserved charge.

## Headline (C15, rescoped after its independent check)

- **What was built.** Two matter modes per site (spin up and spin down) share one Z2 gauge field, and
  rotations act on the pair as a spin-1/2 doublet. This gives a fermion doublet that rotates like spin
  1/2 under all 24 cube rotations.
- **Why it is not emergent spin.** The check showed this spin is inherited from the spinor matter put in
  by hand. With that action, even trivial local excitations can be spinorial, so it is not fractional.
- **What was learned.** A genuinely emergent electron spin needs two things at once:
  - a fermion doublet;
  - a rotation action under which every local excitation has ordinary, integer-type behaviour.
- **Status.** Not achieved; the sharpest open target.
- **The closest thing so far.** BKSF fermions under pure relabelling (C8). Those classes are genuine,
  but not on the full rotation group.

## Realization dictionary: the emergent fermion's half-turn signs

The rotation class eta_f is detected by the squares of the half-turns. In each entry, "+" means
C2^2 = +1 on the fermion (spinless) and "-" means C2^2 = (-1)^F (spin-1/2-like). The pair-test sign
lambda = -eta_f.

| Code | How rotations act | Group covered | Axis C2 | Edge C2 | Class |
|---|---|---|---|---|---|
| BKSF, edge or half-edge (C8, C11) | bare permutation | the code's stabilizer (D3, D2 or Z2) | - | - | w2 restricted (spin-1/2) |
| BKSF, D3 or single-C2 code | bare permutation, twisted by W on the C2 (sign character) | stabilizer | n/a | + | trivial |
| BKSF, order-4 code | bare permutation, twisted by W along a character | D2 | two of the three C2 flip | | (+,+,-)-type; trivial not reachable |
| BKSF, half-edge (C13) | on-site CZ network times permutation (Majorana permutation) | all of O | + | + | trivial |
| Majorana-per-direction (C12) | on-site signed Majorana permutation U_R | all of O | + | + | trivial |
| Majorana-per-direction (C12) | U_R twisted by W on odd elements | all of O | + | - | sign-pullback |
| Either family | any W-twist | all of O | | | w2 on all of O not reachable |

Here W = prod_v exp(-i pi B_v / 4). In BKSF, W = const * e^{i pi N / 2}, a quarter-turn of fermion number.
Majorana-only hopping selects the trivial-class realizations. A single species with w2 on all of O is open.

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
    charges have at most planar mobility, and a single defect is immobile.
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
  - The rule "spin Chamon (x) flavour X on the neighbours" has eight charge
    types that move by any even translation. Each such move anticommutes
    with a free flavour variable.
  - *Interpretation for the owner, not a claim:* there, three-dimensional
    motion is tied to changing extra local data along the path. That would
    be expected to spoil coherent propagation, which is not computed.
- **The supplied three-axis-qubit class (C3).**
  - With labels that do not turn with space, eight interleaved toric codes
    give a covariant star rule whose charges move coherently in three
    dimensions, with bounded code dimension. The charges are bosons.
  - With soldered labels, restricted to C4- or C3-symmetric strings, no
    maximal rule does: each is fracton-type, a product state, or obstructed
    as in C2.
  - Within these classes the obstruction tracks soldering, not storage.
  - *Interpretation for the owner, not a claim:* making the internal labels
    turn with space, which is what gives spin-1/2 its meaning, is what
    blocks coherent motion of the defects in these classes.
- **The fermion search (C4).** In the symmetric three-qubit classes, no
  defect is both coherently mobile in three dimensions and a fermion:
  - soldered labels give no coherent motion at all;
  - unsoldered labels give only bosons (toric-code-type).
  - The hunch that soldering would enable fermions is not supported.
    Known emergent-fermion models use low-symmetry ingredients, such as a
    framing or spin structure, which these searches exclude.
- **C5 exploration (no note).** A quick test of "framed" toric codes found
  apparent fermions. They were an artifact of the statistics solver, whose
  leg operators could cross. With properly confined legs, all were bosons.
  The tool is now fixed and the C4 result re-checked.
- **C6: a real emergent fermion cannot come alone.**
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
  - Test: put two fermions at points swapped by a half-turn. The plain
    permutation gives this pair eigenvalue +1. For fermions that means a
    half-turn done twice acts as fermion parity, the spin-1/2 behaviour.
    This holds for all 108 (code, half-turn) cases, proven independently of
    how the test states are dressed. For every code the full sign pattern
    under its rotation symmetry is that of a spin-1/2 particle.
  - An independent check refuted the first version of this note, which had
    the opposite sign; the note is corrected.
  - The answer depends on how the rotation acts. Moving the qubits gives
    spin-1/2. Adding a phase built from the stabilizers gives a spinless
    fermion.
  - *Interpretation for the owner, not a claim:* if the framework's
    rotations simply move sites, this lattice fermion already behaves like
    a spin-1/2 particle under rotations.

- **The fermion can live on the framework's sites (C11).** Give each site
  six qubits, one per direction, and tie the two halves of each edge
  together. The fermion code then lives on sites, and the framework's own
  site rotation reproduces everything above exactly. The four-copy minimum
  and the spin-1/2 behaviour both carry over. The cost: six qubits per
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
    action the fermion is spinless. Under pure relabelling it is
    spin-1/2-like. Same code, two readings of "rotate". How the framework's rotations act on a site's
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
| C12 | `docs/MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17.py` (PASS=8) | Three qubits per site, six Majoranas: one fermion species covariant under all 24 rotations (on-site Cliffords, group A4 x| Z4); spinless under U_R; sign twist gives (axis +, edge -); w2 on O not reached. |
| C11 | `docs/BKSF_CUBIC_FERMION_CODES_SITE_LOCAL_REALIZATION_WITH_SIX_DIRECTION_QUBITS_PER_SITE_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_site_local_six_direction_qubit_realization_2026_10_17.py` (PASS=6) | Six direction qubits per site: framework site rotation = edge rotation exactly; C6/C8 transfer to a site-local model. |
| C8 | `docs/BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py` (PASS=9) | Zero- and pi-flux sectors are rotation-symmetric with bare-permutation action; swapped-pair test gives eta_f(C2,C2) = -1 for all 108 (code, C2) pairs under the bare permutation: the spin-1/2 class w2 on every code's rotation stabilizer; realization-dependent. |
| C6 | `docs/BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_rotation_orbits_2026_10_17.py` (PASS=8) | 60 translation-invariant BKSF codes, all with a fermionic charge; none rotation-invariant; minimal orbit 4 (D3, body diagonals). |
| C4 | `docs/THREE_AXIS_QUBIT_SYMMETRIC_STABILIZER_RULES_FERMION_SEARCH_FINDS_NO_COHERENTLY_MOBILE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py` (PASS=8) | No coherently 3D-mobile fermion in symmetric three-axis-qubit rules: soldered gives no coherent motion; unsoldered gives bosons only. Alphabet lemma unifies the obstructions. |
| C3 | `docs/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/three_axis_qubit_site_stabilizer_rules_soldering_and_three_dimensional_charge_mobility_2026_10_17.py` (PASS=10 with Singular) | Unsoldered: interleaved toric codes, coherent 3D-mobile bosons. Soldered (C4/C3-fixed): no maximal rule with bounded code dimension and 3D-mobile charge. |
| C2 | `docs/TWO_QUBIT_SITE_SOLDERED_SPIN_STABILIZER_RULES_THREE_DIMENSIONAL_CHARGE_MOTION_FLIPS_A_FREE_LOCAL_VARIABLE_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/two_qubit_site_soldered_spin_stabilizer_rules_charge_motion_flips_free_local_variable_2026_10_17.py` (PASS=17 with Singular) | Free-variable-preserving operators never give a charge rank-three mobility; rules without free local variables have no 3D-mobile charge; example rule with 8 even-step-mobile charges. |
| C1 | `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py` (PASS=20) | Soldered: Chamon only, with fracton defects (no 3D mobility; planons in planes normal to body diagonals). Unsoldered: classical or cluster rules. No 3D-mobile fermionic defect in the class. |

## Open obligations
- C1 and C2 independent checks: done. C2's first classification statement missed the E orbit; this is corrected and checked by the runner.
- C3 onwards in OPPORTUNITY_QUEUE.

## Next decision
- C3 independent check: done. It corrected the validity of three large unions (they contain -1); the conclusions are restated through the rank bound.
- C4 independent check: confirmed. Next: C5, low-symmetry generators (framed fermion codes).
