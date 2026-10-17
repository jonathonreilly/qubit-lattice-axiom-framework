# Handoff — toe-campaign-20261017

Branch `claude/toe-campaign-12h-20261017`, cut from
`claude/toe-campaign-20261016-followup` (PR #9658). C1 landed on main via
#9660. Later blocks go out in fresh PRs from main, starting with
`claude/toe-campaign-12h-20261017-c2`. Window
2026-10-16T23:40Z – 2026-10-17T11:40Z. Lane: the electron as an emergent
excitation of neighbourhood conditions (owner's direction). Nothing here is
adopted; every result is unaudited bounded support with a declared model.

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
    This holds for every case the test covers (72 of 108).
  - An independent check refuted the first version of this note, which had
    the opposite sign; the note is corrected.
  - The answer depends on how the rotation acts. Moving the qubits gives
    spin-1/2. Adding a phase built from the stabilizers gives a spinless
    fermion.
  - *Interpretation for the owner, not a claim:* if the framework's
    rotations simply move sites, this lattice fermion already behaves like
    a spin-1/2 particle under rotations.

## Blocks

| Block | Note | Runner | Headline |
|---|---|---|---|
| C8 | `docs/BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py` (PASS=7) | Zero- and pi-flux sectors are rotation-symmetric with bare-permutation action; swapped-pair test gives eta_f(C2,C2) = -1 (spinorial) under the bare permutation; realization-dependent. |
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
