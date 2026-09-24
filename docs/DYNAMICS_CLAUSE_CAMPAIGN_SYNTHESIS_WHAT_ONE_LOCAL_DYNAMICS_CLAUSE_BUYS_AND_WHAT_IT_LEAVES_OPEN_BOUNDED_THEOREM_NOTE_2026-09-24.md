---
claim_id: dynamics_clause_campaign_synthesis_what_one_local_dynamics_clause_buys_and_what_it_leaves_open_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Synthesis of eighteen campaign blocks (open PRs 9040, 9041, 9043, 9046, 9048, 9050, 9052, 9054, 9066, 9069, 9072, 9077, 9081, 9083, 9084, 9085, 9086, 9088), each built on one supplied and unadopted local dynamics clause. The runner re-derives one load-bearing identity per block in fast independent form: the coupling dimensions 1 (possibility covariance) and 3 (full soldering); records acting as fields and the ferromagnetic law (1 + t)/2; records-only CHSH <= 2 against the singlet's 2 sqrt 2; the isolated-order equivalence on the cube graph; the pi-flux tube's eps^2 = 12 + 8 cos k; the Moriya record statistic -2 sin(phi); the frequency variance identity; the 20-site three-direction network's local-flux splitting and gap above two flat zero-mode bands; and, for the Gauss block, the freeze of the link field by Gauss-invariant two-site terms, the intertwiner count that makes an oriented link field covariant under full soldering alone, and the soft-Gauss ring element -5 h^4/(32 U^3); and, for the charges block, that no role's stabilizer fixes a Bloch axis under full soldering, that covariant vertex-link terms flip a soldered link only against a fully soldered vertex, and that defect hops commute; and, for the plaquette block, that the covariant plaquette clause annihilating uniform ice is the Rokhsar-Kivelson projector; and, for the tensor block, that each row of the landed tensor vector constraint uses exactly its link site's six neighbours and that no single neighbourhood supports an integer move; and, for the non-Abelian block, that one qubit's SU(2) commutant is the scalars and that the 4-dimensional SU(2) link carries a covariant link operator; and, for the randomizer block, that a distant record steers every chord and that the trace rule, but not a cubic deformation, matches the steered average; and, for the dynamics block, that a Weinberg-type precession lets a distant record shift a later marginal and that the transpose on half a singlet is negative; and, for the collapse block, that joint record effects with Born marginals are product projectors and that a record leaves its partner in the Lueders state; and, for the unitarity block, that proportional Kraus operators give a unitary conjugation while a random non-unitary channel mixes some pure state; and, for the time-reversal block, that the covariant scalar-chirality star sum vanishes under possibility covariance. It also checks that the nineteen declared decision points are exactly those the blocks use. No block, and not this synthesis, derives the dynamics clause, adopts a decision point or establishes a physical identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_campaign_synthesis_consolidated_certificates_2026_09_24.py
---

# One dynamics clause: what it buys and what it leaves open

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** synthesis of eighteen open campaign blocks with consolidated re-derivations; unaudited.

## The gap this campaign addressed

A review of main at `0e6ad82850` found one gap shared by every lane that
moves content: the dynamics is supplied. Examples:
- the two-component walk of the eight-species notes;
- the positive local rates, clocked walk and ledger of the rate-field
  notes;
- the finite clock and Villain laws of the Maxwell-scaling notes;
- the ring and Rokhsar–Kivelson Hamiltonians of the ice notes;
- the stochastic generators of the mobile-record notes.

The axioms memo says that Admissibility "is not a dynamics axiom" and does
not "choose a Hamiltonian or transfer operator".

This campaign did not try to derive a dynamics from the axioms. It took
the smallest local dynamics clause as a decision point and asked what that
one clause generates across the lanes.

## Decision points (none adopted)

| Point | Content | First used |
|---|---|---|
| D-dyn | a covariant nearest-neighbour two-site Hermitian generator | 9040 |
| D-pc | possibility covariance (every internal rotation) | 9040 |
| D-sold | full soldering of the rotations to the Bloch vector | 9040 |
| D-perm | permanence as compression onto record projectors; its distant part follows from D-loc (9085) | 9041 |
| D-tr | odds read from the site's state by the trace rule | 9041 |
| D-relax | relaxation profile; which state records form from | 9041, 9052 |
| D-menu | antipodal menus | 9041 |
| D-set | independently formed setting records | 9043 |
| D-nn | Admissibility conditions: records alone, or states | 9043, 9046 |
| D-pattern | a record carving and its contents | 9048, 9054 |
| D-sign | the sign of the Moriya coupling | 9050 |
| D-roles | doubled-coordinate roles (vertex, link, plaquette, cube sites) | 9066, 9069, 9077, 9081 |
| D-gauss | a Gauss law on link sites, exact or as a soft vertex-star energy | 9066, 9069, 9077, 9081 |
| D-star | a covariant generator on a plaquette site's four link neighbours | 9072 |
| D-loc | marginal record distributions do not depend on distant record formation | 9083, 9084 |
| D-rev | reversible, continuous-time, nearest-neighbour evolution between records; its reversibility follows from D-closed and D-onlyrec (9086) | 9084 |
| D-closed | the lattice is the whole system | 9086 |
| D-onlyrec | records are the only irreversible events | 9086 |
| D-chir | a time-reversal-odd three-spin star term | 9088 |

## What the clause generates

1. **The clause is finite (open PR 9040).**
   - Covariant nearest-neighbour two-qubit couplings form spaces of
     dimension 6, 4, 4 and 3 under the four landed rotation actions.
   - Possibility covariance leaves the Heisenberg coupling alone,
     `J s.s = J(2 SWAP - 1)`.
   - Full soldering leaves the Heisenberg, compass and Moriya couplings.
   - The Moriya coupling is odd under the improper inversion, which the
     axioms omit.
2. **Records act as fields, and the law gets a form (open PR 9041).**
   - A recorded neighbour enters the dynamics through its content,
     `P_q s P_q = q P_q`.
   - A site with six recorded neighbours is a qubit in their field.
   - Odds that depend on the records alone point along that field,
     `(1 + lam p.h^)/2`.
   - The Born lane's two decision points relocate. Affinity becomes the
     trace rule, and repeat certainty becomes ferromagnetic ground
     relaxation.
3. **Quantum correlations need quantum conditions (open PR 9043).**
   - Formation laws that condition on records alone, with independent
     settings, are local causal models: CHSH is at most 2.
   - The clause reaches `2 sqrt 2` and goes no further.
   - A record carrying a setting across the wings gives 4, and static
     conditioning exceeds `2 sqrt 2`.
4. **Records-only admissibility leaves the dynamics unreadable (open PR 9046).**
   - If odds are fixed by the six neighbour records, every record forms
     isolated.
   - The forming sites are then independent, they never interact, and no
     readable trace of the dynamics remains.
   - The formation lane's question "which neighbours are already written"
     is then forced to: all six.
5. **Fermions and a gauge field, exactly, in one dimension (open PR 9048).**
   - At the compass point, records carve the medium into Kitaev's model.
   - With zero fields the components are classified completely, as a
     general theorem. Each is either the 2x2x2 cube or a strip one square
     wide that winds along a face diagonal.
   - The proof goes through a surface of Euler characteristic
     (interior sites)/4 ≥ 0. An interior site forces a cube, and a strip
     that does not wind would need a reversal.
   - The staircase tube is gapped (`2|K|`, pi flux).
6. **A handedness that records see (open PR 9050).**
   - The Moriya bond is an XXZ bond in a turned frame.
   - Along a straight line the turn is a gauge. Where bond directions meet
     it has curvature.
   - Records register it as the parity-odd statistic
     `E(a,b) - E(b,a) = -2 sin(phi) (a x b).e`.
7. **Frequencies follow the odds exactly when correlations cluster (open PR 9052).**
   - The sequence law is the joint trace rule.
   - The firewall's IID and locked laws are a product state and a cat
     state.
   - Unique gapped ground states cluster.
8. **Fermions and a gauge field, exactly, in three dimensions (open PR 9054).**
   - Allowing dangling axes, relaxed carvings reach three dimensions.
   - A 20-site network with one local loop per cell is exactly solvable:
     20-qubit ED equals the least Majorana energy.
   - Its flux is genuine, and a vison costs `0.111 |K|`.
   - Its Majorana fermions are gapped (`0.618 |K|`) above two localized
     zero modes per cell.
9. **An exact Gauss law freezes the link field (open PR 9066).**
   - In doubled coordinates no two link sites are adjacent. So every
     two-site generator that respects an exact U(1) or Z2 Gauss law leaves
     every link field conserved.
   - The field moves by vertex–link–vertex hops or plaquette rings. Each
     lies inside one site's neighbourhood, the set Admissibility conditions
     on.
   - Among the four landed rotation actions, an oriented link field is
     covariant under full soldering alone. A dynamical vertex charge needs
     the trivial action or the sign twist.
   - A soft vertex-star Gauss energy lets record fields generate the ring
     at fourth order: `g = 5h⁴/(32U³)`, with no diagonal term at that order.
10. **Charges are Gauss defects (open PR 9069).**
    - Under full soldering, no site of any role has a covariant charge.
    - No covariant two-site term moves charge between a vertex qubit and
      a soldered link, under any landed vertex action.
    - With a soft Gauss energy the charges are defects of the Gauss law.
      They are gapped, hop at first order by record-field flips, and
      exchange as bosons.
    - Record-field phases are pure gauge: the ring is `−5/(2U³)` times the
      product of the flip amplitudes, so only magnitudes matter.
11. **The covariant plaquette clause (open PR 9072).**
    - It is a ring plus four orbit potentials.
    - The member that annihilates uniform ice is the Rokhsar–Kivelson
      projector. Summed over plaquettes, that is the flip-graph Laplacian.
      Its ground states record the uniform measure of each flip class by
      the trace rule.
    - At `D = 0` with normal fields, unrecorded plaquette qubits polarize
      the ice. So the ring needs plaquette sites that add no such
      potential, such as recorded ones.
12. **The landed tensor constraints freeze (open PR 9077).**
    - The vector constraint `∂_i E_ij = 0` of the landed linear-gravity
      tensor model sits on link sites, using exactly their six neighbours.
    - Every two-site generator that respects it conserves the tensor field.
    - For integer (or odd-N) slots, no single site's neighbourhood holds a
      move of the E slots.
    - The smallest local moves are 10-slot planar curvature pieces. That
      is the minimum on the whole lattice (independent check).
13. **Non-Abelian links need several qubits (open PR 9081).**
    - One qubit carries U(1) and Z2 links but no non-Abelian link.
    - An SU(N) link needs at least 2N states, and `(N, 1) ⊕ (1, N)`
      reaches that with a covariant link operator.
    - So SU(2) needs 2 qubits per link, SU(3) 3, and independent Standard
      Model fields 6.
14. **A distant record is a recorded randomizer (open PR 9083).**
    - The clause carries a condition qubit's purification to any distance.
    - Recording the partner steers the qubit to either end of any chord.
    - Under D-loc (marginals do not depend on distant record formation), the
      law is affine: the trace rule.
    - Compression consistency (D-perm) then forces `E_q = P_q`, the Born
      orientation with full contrast.
    - This discharges the landed affine/Born gate's first and third
      obligations. D-tr is now derived from D-loc and D-perm, not supplied.
15. **Locality of marginals forces linear dynamics (open PR 9084).**
    - Under D-loc, the evolution between records is affine; otherwise a
      distant record signals.
    - Joint positivity makes it completely positive; reversibility makes it
      unitary.
    - With continuous time and nearest-neighbour range, it has the form of
      the clause. The clause's content reduces to D-rev and covariance.
16. **A record updates the rest of the lattice by compression (open PR 9085).**
    - Joint record effects whose marginals stay Born are product
      projectors.
    - So a record leaves every other site in its Lüders conditional state.
    - The distant part of D-perm, the collapse, follows from D-loc and the
      site-local lock.
    - Two-possibility menus are forced to be antipodal.
17. **A closed lattice evolves unitarily between records (open PR 9086).**
    - Suppose the lattice is closed and records are its only irreversible
      events. Then evolution between records keeps pure states pure and
      distinguishable, which makes it unitary.
18. **Covariant time-reversal breaking never keeps a carving solvable (open PR 9088).**
    - Possibility covariance allows no time-reversal-odd three-spin star
      term.
    - Under the landed actions such terms exist, but none has Kitaev's
      solvable pattern. On the cube, none preserves the loop operators.
    - In exactly solvable carvings, time reversal is broken only by
      records.

**The ladder.** What each sector needs from the dynamics and the lattice:

| Sector | Needs | Blocks |
|---|---|---|
| Quantum probability (Born form, frequencies, Bell) | the two-site clause; the Born law follows from locality of marginals (D-loc) and compression (D-perm) | 9041, 9043, 9046, 9052, 9083 |
| Z2 gauge field and Majorana fermions | the two-site clause at the compass point, plus a record carving | 9048, 9054 |
| U(1) photon | one neighbourhood: a plaquette ring (Rokhsar–Kivelson at uniform ice), or a soft vertex Gauss energy | 9066, 9069, 9072 |
| Linearized-gravity tensor field (landed discretization, E-slot moves) | more than one neighbourhood: the smallest moves span a vertex's second neighbourhood | 9077 |
| SU(2), SU(3) gauge fields | composite links of 2 and 3 qubits (6 for the full group) | 9081 |
| Time-reversal-odd (chiral) content | a star term under soldering, which then breaks the carvings' solvability; within solvable carvings, only records break it | 9088 |

## What it does not generate

- **U(1), SU(2) or SU(3) gauge fields.** The exact gauge field found is
  Z2. SU(2) and SU(3) links need at least 2 and 3 qubits (open PR 9081),
  so they cannot sit on one-qubit link sites. A U(1) field on link sites needs one of two terms of Admissibility
  shape (open PR 9066):
  - a plaquette ring clause, whose covariant family contains the
    Rokhsar–Kivelson point;
  - a soft vertex Gauss energy, which gives the pure ring at fourth order.

  The two-site clause alone freezes the field.
- **Charged or chiral fermions.** The emergent fermions are Majorana. No
  gapless or Weyl case appears among 15 three-direction networks with
  random record contents. No single landed action gives both an oriented
  link field and a dynamical vertex charge. Under the clause, U(1) charges
  are Gauss defects, and they are bosons (open PR 9069).
- **Gravity.** The clause supplies no long-range rate field. The landed
  linear-gravity tensor field is frozen by every two-site generator under
  its vector constraint. For integer slots, no single neighbourhood moves
  its E slots (open PR 9077). So in that discretization, moving the
  tensor field takes dynamics wider than a photon's.
- **Parameters and supplied structure.** Generations are not addressed,
  and the values of `J`, `K`, `D` are not fixed. The formation site, time
  and rate, the relaxation profile, and how records come to form a carving
  are all still supplied.
- **Soldering is needed for the fermion and gauge content.** Under
  possibility covariance only the Heisenberg coupling remains, and the
  Kitaev route (blocks 5 and 8) is not available.
- **The full spin model of a carved network is extensively degenerate.**
  The degeneracy comes from its localized zero modes.

## Consolidated certificates

The runner re-derives one identity per block, independently of that
block's runner, and checks the ledger. There are nineteen checks and all
pass in about two seconds.
- **L.** The nineteen declared points are exactly those used by the
  eighteen blocks.
- **1.** Coupling dimensions 1, 1 and 3.
- **2.** The projection lemma, the resultant ground state, and the
  pentagon law `(1 + t)/2`.
- **3.** 3000 random shared-source records-only models (largest `1.857`)
  against the singlet's `2.828427`.
- **4.** All 6561 cube-graph labellings.
- **5.** `eps^2 = 12 + 8 cos k` on the pi-flux tube, to `2e-14`.
- **6.** `c = -1.1469246887 = -2 sin(atan 0.7)`.
- **7.** The variance identity on a random 5-qubit state.
- **8.** The 20-site network's two sector levels, its two flat zero modes
  and its gap `0.618`.
- **9.** The Gauss freeze on a vertex–link–vertex window, the intertwiner
  dimensions `0, 0, 0, 1` and invariant axes `3, 1, 0, 0`, and the ring
  element `−5/32`.
- **10.** No fixed Bloch axis for any role, the vertex–link flip dimensions
  `0, 0, 0, 2`, and commuting defect hops.
- **11.** The frustration-free plaquette solution space: one ray with
  coefficients `(1, 1, 0, 0, 0)`.
- **12.** Six-neighbour placement of the tensor rows, and null
  neighbourhood moves for every role.
- **13.** Scalar SU(2) commutant on a qubit, and covariant link operators
  on the 4-dimensional SU(2) link.
- **14.** Steering of random chords, the trace rule's exact steered
  average, and a cubic deformation's shift.
- **15.** A Weinberg-type precession's signalling shift, and the negative
  partial transpose of a singlet.
- **16.** The one-line range intersection, and tomography matching the
  Lüders state.
- **17.** Proportional Kraus operators, and a random channel's purity loss.
- **18.** The vanishing covariant scalar-chirality sum.

## Independent checks

Two checkers wrote separate code and did not read the campaign's runners.
- **Blocks 2–5:** 10 of 10 claims pass. Their additions:
  - "pi flux" means an oriented bond-variable product of `-1`, which is
    loop eigenvalue `W = +1`;
  - a closed form for the tube energy.
- **Blocks 6–8:** 6 of 6 claims pass. They flagged two things, both now
  corrected in open PR 9054:
  - the first 3D headline network is a tree;
  - zero-field dangling Majoranas are decoupled zero modes.
- **The Gauss-freeze block (9066):** every claim passes, with no gap in the
  proof.
  - Corrected since: the printed span dimensions counted redundant zero
    combinations (true ranks 26 and 18).
  - Also corrected: `V = 0` needs equal field sizes, and some prose was
    overstated.
- **The plaquette and tensor blocks (9072, 9077):** every computation
  passes, and the tensor block's 10-slot minimum holds without a box.
  - Corrected since: the Rokhsar–Kivelson projector is characterized by
    annihilating uniform ice, not by term-by-term positivity.
  - Also corrected: the polarization result needs `D = 0` and normal
    fields. Even-N clocks admit a one-neighbourhood cube move, and the
    landed `C2` terms fit in one neighbourhood.
- **The charges block (9069) and the carving proof (9048):** every claim
  passes, on 22,972 carving components across nine tori.
  - The checker supplied the interior-site lemma that completes the
    carving classification.
  - It flagged scope in 9069, now corrected: full soldering, supplied Gauss
    energy, and bosons for bare flips.

## The state of the candidate after this campaign

One locality reading, D-loc, now does triple duty (open PRs 9083, 9084 and
9085). It makes the record law and the evolution between records linear,
and it fixes how a record updates distant sites. So the
quantum-probability sector's decision points reduce to:
- D-loc;
- the lock (a record leaves its own site in its possibility);
- two-possibility menus (that they are antipodal follows, open PR 9085);
- a closed lattice whose only irreversible events are records (D-closed,
  D-onlyrec), which gives unitarity;
- continuous time and nearest-neighbour range;
- covariance.

A candidate built on the four axioms plus one local dynamics clause holds
together in its quantum-probability sector:
- the Born law `Tr(P_q ρ)`: locality of marginals forces affinity and
  compression forces the orientation (open PR 9083);
- frequencies, through clustering;
- Bell values, which reach the quantum bound and no further.

Records-only readings cannot supply quantum correlations or readable
dynamics, so the Admissibility conditions must include the states of
unrecorded neighbours.

Under full soldering, the same clause and a pattern of records produce
emergent Majorana fermions and a Z2 gauge field, exactly, in three
dimensions.

For a U(1) photon the clause needs a companion term of Admissibility
shape, a plaquette ring or a soft Gauss energy. The two-site clause cannot
move a field under an exact Gauss law. The charges it then carries are
bosonic Gauss defects. Linearized gravity's tensor field needs more still:
no single neighbourhood moves it.

The Standard Model's gauge group, charged chiral matter, gravity and the
parameters remain open. So do the owner-level readings the decision points
name.

## What this does not do

- It adopts no decision point and derives no dynamics.
- It does not audit, land or promote any block. The blocks are open PRs.
- Its checks re-derive identities and do not replace the blocks' own
  runners.
