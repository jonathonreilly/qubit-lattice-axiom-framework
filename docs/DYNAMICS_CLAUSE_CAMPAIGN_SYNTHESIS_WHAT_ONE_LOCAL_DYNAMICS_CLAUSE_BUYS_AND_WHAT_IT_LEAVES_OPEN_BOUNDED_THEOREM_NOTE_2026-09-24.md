---
claim_id: dynamics_clause_campaign_synthesis_what_one_local_dynamics_clause_buys_and_what_it_leaves_open_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Synthesis of eighteen open campaign blocks (PRs 9040, 9041, 9043, 9046, 9048, 9050, 9052, 9054, 9066, 9069, 9072, 9077, 9081, 9083, 9084, 9085, 9086, 9088), all built on one supplied and unadopted local dynamics clause, with nineteen recorded decision points. Three findings. (a) Quantum rules and dynamics: under locality of marginals (D-loc), the lock (a record leaves its own site in its possibility), two-possibility menus, a closed lattice whose only irreversible events are records, continuous time-homogeneous nearest-neighbour evolution and covariance, the following all follow: the Born law Tr(P_q rho), the compression update at distant sites, antipodal menus, and linear, completely positive, unitary evolution of the clause's two-site form. (b) Exact emergent content: under full soldering, record carvings give exactly solvable Kitaev models: Majorana fermions in a Z2 gauge field, in one dimension and, with relaxed carvings, in three. Zero-field carving components are exactly 2x2x2 cubes or face-diagonal strips. (c) What further sectors need: U(1) link fields freeze under every two-site generator with an exact Gauss law, and move by a one-neighbourhood plaquette ring or a soft vertex Gauss energy. The landed linear-gravity tensor field is moved by no single neighbourhood (integer slots). SU(N) links need 2N states, so composite links. Time-reversal-odd star terms need soldering and break the carvings' solvability. U(1) charges under the clause are bosonic Gauss defects. The runner re-derives one identity per block and checks that the declared decision points are exactly those used. No decision point is adopted, no block is audited, and no physical identification is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_campaign_synthesis_consolidated_certificates_2026_09_24.py
---

# One dynamics clause: what it buys and what it leaves open

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** synthesis of eighteen open campaign blocks with consolidated re-derivations; unaudited.

## Result

A review of main at `0e6ad82850` found one gap shared by every lane that
moves content: the dynamics is supplied. The axioms memo says Admissibility
"is not a dynamics axiom". This campaign supplied the smallest candidate, a
covariant nearest-neighbour two-site generator, as a decision point. It did
not adopt it, and it asked what that clause generates and what each other
sector needs beyond it.

1. **The quantum rules follow from a few readings.** Given the readings
   below, the following all follow (open PRs 9083–9086):
   - the Born law `Tr(P_q ρ)`;
   - the compression update of distant sites ("collapse");
   - antipodal record menus;
   - linear, completely positive, unitary evolution between records, with
     the clause's two-site form.

   The readings are:
   - locality of marginals (D-loc);
   - the lock (a record leaves its own site in its possibility);
   - two-possibility menus;
   - a closed lattice whose only irreversible events are records;
   - continuous time-homogeneous nearest-neighbour evolution;
   - covariance.
2. **Exact emergent matter and gauge content.**
   - Under full soldering, records carve the medium into exactly solvable
     Kitaev models (open PRs 9048, 9054). These are Majorana fermions in a
     Z2 gauge field, with genuine flux, in one and three dimensions.
   - Zero-field carvings are classified completely: 2x2x2 cubes, or strips
     one square wide that wind along a face diagonal.
3. **A ladder of what the other sectors need.**

   | Sector | What it needs beyond the two-site clause | Blocks |
   |---|---|---|
   | Quantum probability: Born law, frequencies, Bell values | nothing further; the readings above | 9041, 9043, 9046, 9052, 9083–9086 |
   | Z2 gauge field and Majorana fermions | full soldering at the compass point, plus a record carving | 9048, 9054 |
   | U(1) photon | one neighbourhood: a plaquette ring, or a soft vertex Gauss energy | 9066, 9069, 9072 |
   | Landed linear-gravity tensor field (E-slot moves, integer slots) | more than one neighbourhood | 9077 |
   | SU(2), SU(3) gauge fields | composite links of at least 2 and 3 qubits (6 for independent Standard Model fields, 4 for one joint link) | 9081 |
   | Time-reversal-odd (chiral) content | a star term under soldering, which breaks the carvings' solvability | 9088 |

## Decision points

These are recorded so each result names what it rests on. None is adopted.
Some are now derived from others, as marked.

| Point | Content | Used by | Status |
|---|---|---|---|
| D-dyn | a covariant nearest-neighbour two-site Hermitian generator | 9040–9077, 9083 | form follows from D-loc, D-closed, D-onlyrec, D-rev and covariance (9084, 9086) |
| D-pc | possibility covariance (every internal rotation) | 9040, 9084, 9088 | supplied |
| D-sold | full soldering of the rotations to the Bloch vector | 9040, 9048, 9050, 9054, 9066, 9069, 9072, 9084, 9088 | supplied |
| D-perm | records update by compression | 9041, 9043, 9046, 9048, 9054, 9083, 9084, 9085 | distant part follows from D-loc and the lock (9085) |
| D-tr | odds read from the state by the trace rule | 9041, 9043, 9046, 9050, 9052, 9072 | follows from D-loc, D-perm and the menu (9083) |
| D-relax | relaxation profile: which state records form from | 9041, 9052 | supplied (it fixes the state, not the law) |
| D-menu | antipodal menus | 9041, 9043, 9050, 9052, 9083, 9085 | antipodal follows for two-possibility menus (9085) |
| D-set | independently formed setting records | 9043 | supplied |
| D-nn | Admissibility conditions: records alone, or states | 9043, 9046 | records alone leave the dynamics unreadable (9046) |
| D-pattern | a record carving and its contents | 9048, 9054, 9066, 9069, 9072, 9088 | supplied |
| D-sign | the sign of the Moriya coupling | 9050 | supplied |
| D-roles | doubled-coordinate roles (vertex, link, plaquette, cube sites) | 9066, 9069, 9072, 9077, 9081 | supplied |
| D-gauss | a Gauss law on link sites, exact or as a soft vertex-star energy | 9066, 9069, 9072, 9077, 9081 | supplied |
| D-star | a covariant generator on a plaquette site's four link neighbours | 9072 | supplied |
| D-loc | marginal record distributions do not depend on distant record formation | 9083, 9084, 9085, 9086 | supplied reading of physical locality |
| D-rev | reversible, continuous-time, nearest-neighbour evolution between records | 9084 | reversibility follows from D-closed and D-onlyrec (9086) |
| D-closed | the lattice is the whole system | 9086 | supplied reading |
| D-onlyrec | records are the only irreversible events | 9086 | supplied reading of the Record axiom |
| D-chir | a time-reversal-odd three-spin star term | 9088 | supplied |

## The blocks

**Quantum rules and dynamics.**
- **9041 — records act as fields.** A recorded neighbour enters the dynamics
  through its content, `P_q s P_q = q P_q`. A site with six recorded
  neighbours is a qubit in their field, and odds that depend on records
  alone point along that field.
- **9043 — Bell values.** Records-only formation laws with independent
  settings keep CHSH at most 2. The clause reaches `2√2` and goes no
  further.
- **9046 — records-only admissibility.** If odds are fixed by the six
  neighbour records alone, every record forms isolated, and the dynamics
  leaves no readable trace.
- **9052 — frequencies.** The sequence law is the joint trace rule, and
  frequencies follow the one-shot odds exactly when correlations cluster.
- **9083 — the Born law.**
  - A distant record is a recorded randomizer. The clause can carry a
    purification to any distance, and recording the partner steers the site
    to either end of any chord.
  - Under D-loc the law is affine. That holds even with the partner's
    weights from the same law, where D-loc leaves `λ ∈ {0, 1}`.
  - Compression consistency then forces `E_q = P_q`.
  - This reduces the landed affine/Born gate's first obligation to D-loc
    and settles its third.
- **9084 — linear dynamics.** Under D-loc, the evolution between records is
  affine for a partner decoupled during it. Positivity of joint records
  after the clause's own rotations and bonds makes it completely positive.
  With reversibility it is unitary, with the clause's two-site form.
- **9085 — the collapse.** Joint record effects whose marginals stay Born
  are product projectors. So a record leaves every other site in its Lüders
  conditional state, and two-possibility menus are antipodal.
- **9086 — unitarity.** In a closed lattice whose only irreversible events
  are records, evolution between records keeps pure states pure and
  distinguishable, and so it is unitary.

**Exact emergent content.**
- **9040 — the couplings.** Covariant two-site couplings have dimension 6,
  4, 4 and 3 under the four landed actions. Possibility covariance leaves
  Heisenberg alone. Full soldering allows Heisenberg, compass and Moriya.
- **9048 — Kitaev carvings.**
  - At the compass point, records carve Kitaev's model.
  - Zero-field components are exactly 2x2x2 cubes or face-diagonal strips.
    The proof uses a surface of Euler characteristic (interior sites)/4 ≥ 0.
  - The staircase tube is gapped (`2|K|`, π flux).
- **9050 — handedness.** The Moriya bond is an XXZ bond in a turned frame.
  Records see it as `E(a,b) − E(b,a) = −2 sin φ (a×b)·e`.
- **9054 — three dimensions.** A 20-site relaxed network is exactly
  solvable, with genuine flux (vison `0.111|K|`). Its Majoranas are gapped
  at `0.618|K|` above two flat zero modes per cell.
- **9088 — time-reversal breaking.**
  - Possibility covariance allows no T-odd three-spin star term.
  - Under the landed actions such terms exist, but none has Kitaev's
    solvable pattern, and on the cube none preserves the loop operators.

**What further sectors need.**
- **9066 — the Gauss freeze.**
  - Link sites are never adjacent in doubled coordinates. So every
    two-site generator that respects an exact U(1) or Z2 Gauss law freezes
    the link field.
  - Hops and rings move it, each inside one neighbourhood. An oriented
    link field is covariant under full soldering alone.
  - A soft vertex Gauss energy with equal record fields gives the ring at
    fourth order, `g = 5h⁴/(32U³)`, with no diagonal term at that order.
- **9069 — charges.** Under full soldering no qubit carries a covariant
  charge. With a soft Gauss law, charges are gapped bosonic defects, and
  record-field phases are pure gauge.
- **9072 — the plaquette clause.**
  - It is a ring plus four orbit potentials.
  - The member that annihilates uniform ice is the Rokhsar–Kivelson
    projector, whose ground states record uniform class measures.
  - At `D = 0` with normal fields, unrecorded plaquettes polarize the ice.
- **9077 — the tensor constraints.**
  - The landed vector constraint `∂_i E_ij = 0` sits on link sites.
    Two-site generators respecting it freeze the tensor field.
  - For integer slots, no single neighbourhood moves it. The smallest moves
    are 10-slot planar curvature pieces.
- **9081 — non-Abelian links.** One qubit carries no SU(N) link. An SU(N)
  link needs `2N` states, reached by `(N, 1) ⊕ (1, N)` with a covariant link
  operator.

## What stays open

- **Gauge group.** The exact gauge field found is Z2. U(1) needs a
  companion term of Admissibility shape. SU(2) and SU(3) need composite
  links, and no superlattice is chosen.
- **Charged chiral fermions.** The emergent fermions are Z2-charged
  Majoranas, and the clause's U(1) charges are bosons. No gapless or Weyl
  case appeared among 15 three-direction networks. Covariant time-reversal
  breaking destroys the carvings' solvability.
- **Gravity.** No long-range rate field is generated. The landed tensor
  field needs dynamics wider than one neighbourhood.
- **Parameters and supplied structure.**
  - The coupling values `J`, `K`, `D`.
  - Generations.
  - Where, when and how fast records form, and the relaxation profile.
  - How records come to form a carving.
- **The photon phase.** Not placed, either for the Rokhsar–Kivelson family
  or for the pure-ring point where the soft route lands.
- **Relaxation.** With unitary evolution between records (open PR 9086), a
  site whose six neighbours are all recorded precesses in their field.
  - Its Bloch component along the field is conserved, so it cannot relax.
  - The relaxation profile of open PR 9041 therefore needs unrecorded
    surroundings that act as an environment. How that environment fixes
    the profile is not derived.
- **The readings themselves.** D-loc, the lock, D-closed, D-onlyrec,
  continuous time, the range and covariance are recorded readings, not
  derived from the axiom text.

## Consolidated certificates

The runner re-derives one identity per block, independently of that
block's runner, and checks the ledger. There are nineteen checks and all
pass in about two seconds.
- **L.** The nineteen declared points are exactly those used by the
  eighteen blocks.
- **1.** Coupling dimensions 1, 1 and 3.
- **2.** The projection lemma, the resultant ground state, and the pentagon
  law `(1 + t)/2`.
- **3.** 3000 random shared-source records-only models (largest `1.857`)
  against the singlet's `2.828427`.
- **4.** All 6561 cube-graph labellings.
- **5.** `ε² = 12 + 8 cos k` on the π-flux tube, to `2e-14`.
- **6.** `c = −1.1469246887 = −2 sin(atan 0.7)`.
- **7.** The variance identity on a random 5-qubit state.
- **8.** The 20-site network's two sector levels, two flat zero modes and
  gap `0.618`.
- **9.** The Gauss freeze on a vertex–link–vertex window, the intertwiner
  dimensions `0, 0, 0, 1` and invariant axes `3, 1, 0, 0`, and the ring
  element `−5/32`.
- **10.** No fixed Bloch axis for any role, the vertex–link flip dimensions
  `0, 0, 0, 2`, and commuting defect hops.
- **11.** The uniform-ice plaquette solution, with coefficients
  `(1, 1, 0, 0, 0)`.
- **12.** Six-neighbour placement of the tensor rows, and no integer
  neighbourhood move for any role.
- **13.** The scalar SU(2) commutant on a qubit, and covariant link
  operators on the 4-dimensional SU(2) link.
- **14.** Steering of random chords, the trace rule's exact steered average,
  and a cubic deformation's shift.
- **15.** A Weinberg-type precession's signalling shift, and the negative
  partial transpose of a singlet.
- **16.** The one-line range intersection, and tomography matching the
  Lüders state.
- **17.** Proportional Kraus operators, and a random channel's purity loss.
- **18.** The vanishing covariant scalar-chirality sum.

## Independent checks

Separate checkers wrote their own code without reading the campaign's
runners. Every computation they repeated agreed. Where the prose went
further than the theorems, it has been corrected.
- **Blocks 2–5.** 10 of 10 claims pass. "π flux" means an oriented
  bond-variable product of `−1`, which is loop eigenvalue `W = +1`.
- **Blocks 6–8.** All claims pass. They flagged two things, both corrected:
  the first 3D headline network was a tree, and zero-field dangling
  Majoranas are decoupled zero modes.
- **The Gauss freeze (9066).** Every claim passes, with no gap in the proof.
  Corrected since:
  - the true span ranks are 26 and 18;
  - `V = 0` needs equal field sizes.
- **Charges and the carving proof (9069, 9048).** All pass, on 22,972
  carving components across nine tori. The checker supplied the
  interior-site lemma that completes the classification. Corrected since:
  9069's scope, to full soldering and bare flips.
- **The plaquette and tensor blocks (9072, 9077).** All pass, and the
  10-slot minimum holds on the whole lattice. Corrected since:
  - the Rokhsar–Kivelson projector is characterized by annihilating uniform
    ice;
  - polarization needs `D = 0` and normal fields;
  - even-N clocks and the landed `C2` terms are one-neighbourhood
    exceptions.
- **The link, Born and dynamics blocks (9081, 9083, 9084).** All pass.
  Corrected since:
  - the partner's Born weights are no longer assumed;
  - complete positivity uses the clause's own entangling step;
  - D-loc is scoped to decoupled partners;
  - a joint Standard Model link needs 4 qubits.
- **The collapse, unitarity and time-reversal blocks (9085, 9086, 9088).**
  The check is still running.

## What this does not do

- It adopts no decision point and derives no dynamics from the axiom text.
- It does not audit, land or promote any block. The blocks are open PRs.
- Its checks re-derive identities and do not replace the blocks' own
  runners.
