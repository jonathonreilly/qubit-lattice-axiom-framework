---
claim_id: dynamics_clause_campaign_synthesis_what_one_local_dynamics_clause_buys_and_what_it_leaves_open_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Synthesis of nine campaign blocks (open PRs 9040, 9041, 9043, 9046, 9048, 9050, 9052, 9054, 9066), each built on one supplied and unadopted local dynamics clause. The runner re-derives one load-bearing identity per block in fast independent form: the coupling dimensions 1 (possibility covariance) and 3 (full soldering); records acting as fields and the ferromagnetic law (1 + t)/2; records-only CHSH <= 2 against the singlet's 2 sqrt 2; the isolated-order equivalence on the cube graph; the pi-flux tube's eps^2 = 12 + 8 cos k; the Moriya record statistic -2 sin(phi); the frequency variance identity; the 20-site three-direction network's local-flux splitting and gap above two flat zero-mode bands; and, for the Gauss block, the freeze of the link field by Gauss-invariant two-site terms, the intertwiner count that makes an oriented link field covariant under full soldering alone, and the soft-Gauss ring element -5 h^4/(32 U^3). It also checks that the thirteen declared decision points are exactly those the blocks use. No block, and not this synthesis, derives the dynamics clause, adopts a decision point or establishes a physical identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_campaign_synthesis_consolidated_certificates_2026_09_24.py
---

# One dynamics clause: what it buys and what it leaves open

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** synthesis of nine open campaign blocks with consolidated re-derivations; unaudited.

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
| D-perm | permanence as compression onto record projectors | 9041 |
| D-tr | odds read from the site's state by the trace rule | 9041 |
| D-relax | relaxation profile; which state records form from | 9041, 9052 |
| D-menu | antipodal menus | 9041 |
| D-set | independently formed setting records | 9043 |
| D-nn | Admissibility conditions: records alone, or states | 9043, 9046 |
| D-pattern | a record carving and its contents | 9048, 9054 |
| D-sign | the sign of the Moriya coupling | 9050 |
| D-roles | doubled-coordinate roles (vertex, link, plaquette, cube sites) | 9066 |
| D-gauss | a Gauss law on link sites, exact or as a soft vertex-star energy | 9066 |

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
   - With zero fields the carvings are cubes and tubes, a finite result
     complete on 4x4x4 and 5x5x5.
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

## What it does not generate

- **U(1), SU(2) or SU(3) gauge fields.** The exact gauge field found is
  Z2. A U(1) field on link sites needs one of two terms of Admissibility
  shape (open PR 9066):
  - a plaquette ring clause, whose covariant family contains the
    Rokhsar–Kivelson point;
  - a soft vertex Gauss energy, which gives the pure ring at fourth order.

  The two-site clause alone freezes the field.
- **Charged or chiral fermions.** The emergent fermions are Majorana. No
  gapless or Weyl case appears among 15 three-direction networks with
  random record contents. No single landed action gives both an oriented
  link field and a dynamical vertex charge. Charges then need a
  role-dependent action, or must be defects of a soft Gauss law.
- **Gravity.** The clause supplies no long-range rate field.
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
block's runner, and checks the ledger. There are ten checks and all pass
in about one second.
- **L.** The thirteen declared points are exactly those used by the nine
  blocks.
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

## The state of the candidate after this campaign

A candidate built on the four axioms plus one local dynamics clause holds
together in its quantum-probability sector:
- the Born form, from the trace rule;
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
move a field under an exact Gauss law.

The Standard Model's gauge group, charged chiral matter, gravity and the
parameters remain open. So do the owner-level readings the decision points
name.

## What this does not do

- It adopts no decision point and derives no dynamics.
- It does not audit, land or promote any block. The blocks are open PRs.
- Its checks re-derive identities and do not replace the blocks' own
  runners.
