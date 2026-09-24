---
claim_id: dynamics_clause_campaign_synthesis_what_one_local_dynamics_clause_buys_and_what_it_leaves_open_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Synthesis of twenty open campaign blocks (PRs 9040, 9041, 9043, 9046, 9048, 9050, 9052, 9054, 9066, 9069, 9072, 9077, 9081, 9083, 9084, 9085, 9086, 9088, 9095, 9097), all built on one supplied and unadopted local dynamics clause, with twenty-one recorded decision points. Three findings. (a) Quantum rules as consistency conditions inside supplied kinematics. Take the Hilbert-space kinematics the clause brings (density operators, tensor products, purifications), records updating by compression (the lock, the support condition and the distant update), and odds that are a function of the site's conditional state. Then locality of marginals at equal time makes the odds affine, and the support condition fixes them to Tr(P_q rho) with antipodal two-possibility menus. The distant update is the one consistent with locality of marginals, affine joint laws and Born marginals: self-consistent, not derived. With the clause's own bond as the entangling test, a site's evolution between records with a decoupled partner is linear and completely positive. It is unitary exactly when records are the only irreversible events, which restates reversibility for channels. The generator is Hermitian, and its two-site form restates the range imposed on the generator. This is the standard no-signalling route placed in the framework. (b) Exact emergent content: under full soldering, record carvings give exactly solvable Kitaev models: Majorana fermions in a Z2 gauge field, in one dimension and, with relaxed carvings, in three. Zero-field carving components are exactly 2x2x2 cubes or face-diagonal strips. (c) What further sectors need. U(1) link fields freeze under every two-site generator with an exact Gauss law, and move by a one-neighbourhood plaquette ring or a soft vertex Gauss energy. The landed linear-gravity tensor field is moved by no single neighbourhood (integer slots), but a soft vector constraint with one-site slot fields generates its smallest moves, the planar pieces, at twelfth order (path sum 111150053/31850496; for rotor slots no diagonal term at any order, so the leading dynamics is a sum of planar-curvature cosines; qubit slots need 20-slot moves at order 20, behind fourth-order potentials). SU(N) links need 2N states, so composite links. Covariance allows time-reversal-odd star terms, even possibility covariance (an off-centre octant chirality), but on the cube carving none keeps the Majoranas free; under soldering the tripod keeps the Z2 fluxes and makes the Majoranas interact. Record fields on dangling axes keep the carved Majoranas sublattice-symmetric, so they give the gapped bands no weak Chern number, and the gapped three-dimensional networks stay non-chiral even under Kitaev's time-reversal-odd pattern. A gapless start changes this: with its dangling Majoranas decoupled, a network's bands are gapless, and Kitaev's pattern then gives weak Chern numbers (1, 0, 0); zero dangling fields are realizable by records on some networks (8 of 16 found are gapless), though not on that one, and Kitaev's pattern is not covariant. U(1) charges under the clause are bosonic Gauss defects. The runner re-derives one identity per block and checks that the declared decision points are exactly those used. No decision point is adopted, no block is audited, and no physical identification is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_campaign_synthesis_consolidated_certificates_2026_09_24.py
---

# One dynamics clause: what it buys and what it leaves open

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** synthesis of twenty open campaign blocks with consolidated re-derivations; unaudited.

## Result

A review of main at `0e6ad82850` found one gap shared by every lane that
moves content: the dynamics is supplied. The axioms memo says Admissibility
"is not a dynamics axiom". This campaign supplied the smallest candidate, a
covariant nearest-neighbour two-site generator, as a decision point. It did
not adopt it, and it asked what that clause generates and what each other
sector needs beyond it.

1. **The quantum rules are consistency conditions inside supplied
   kinematics** (open PRs 9083–9086).
   - **The setting.** Take three things:
     - the Hilbert-space kinematics the clause brings: density operators,
       tensor products, purifications (the axioms fix no cross-site
       composition law);
     - records updating by compression: the lock, the support condition
       and the distant update;
     - odds that are a function of the site's conditional state.
   - **The record law.** Locality of marginals at equal time makes the odds
     affine. The support condition then fixes them to `Tr(P_q ρ)`, with
     antipodal two-possibility menus.
   - **The collapse.** The distant update is the one consistent with
     locality of marginals, affine joint laws and Born marginals. That is
     self-consistency, not derivation. The lock alone does not give it: a
     record that only resets its own site passes locality of marginals with
     anti-Born odds.
   - **The dynamics.** With the clause's own bond as the entangling test, a
     site's evolution between records, with a decoupled partner, is linear
     and completely positive.
     - It is unitary exactly when records are the only irreversible events,
       which for channels restates reversibility.
     - The generator is Hermitian. Its two-site form restates the range
       imposed on the generator.

   This is the standard no-signalling route (prior art: Gisin 1990; Simon,
   Bužek and Gisin 2001; Masanes, Galley and Müller 2019), placed in the
   framework. What it adds is an autonomous recorded randomizer and one
   locality reading that constrains both the law and the dynamics.
2. **Exact emergent matter and gauge content.**
   - Under full soldering, records carve the medium into exactly solvable
     Kitaev models (open PRs 9048, 9054). These are Majorana fermions in a
     Z2 gauge field, with genuine flux, in one and three dimensions.
   - Zero-field carvings are classified completely: 2x2x2 cubes, or strips
     one square wide that wind along a face diagonal.
3. **A ladder of what the other sectors need.**

   | Sector | What it needs beyond the two-site clause | Blocks |
   |---|---|---|
   | Quantum probability: Born law, frequencies, Bell values | nothing further, inside the supplied kinematics and readings | 9041, 9043, 9046, 9052, 9083–9086 |
   | Z2 gauge field and Majorana fermions | full soldering at the compass point, plus a record carving | 9048, 9054 |
   | U(1) photon | one neighbourhood: a plaquette ring, or a soft vertex Gauss energy | 9066, 9069, 9072 |
   | Landed linear-gravity tensor field (E-slot moves, integer slots) | more than one neighbourhood, generated at twelfth order by a one-neighbourhood soft constraint and slot fields | 9077, 9095 |
   | SU(2), SU(3) gauge fields | composite links of at least 2 and 3 qubits (6 for independent Standard Model fields, 4 for one joint link) | 9081 |
   | Time-reversal-odd (chiral) content | a realizable gapless carving plus a covariant same-class time-reversal-odd bilinear; record fields alone keep a sublattice symmetry, and Kitaev's pattern on a gapless start gives weak Chern number 1 but is not covariant | 9088, 9097 |

## Decision points

These are recorded so each result names what it rests on. None is adopted.

| Point | Content | Used by | Status |
|---|---|---|---|
| D-dyn | a covariant nearest-neighbour two-site Hermitian generator, with the Hilbert-space kinematics it acts on | 9040–9077, 9083–9085, 9097 | supplied; unitarity gives a Hermitian generator, and the two-site form restates the imposed range (9084) |
| D-pc | possibility covariance (every internal rotation) | 9040, 9084, 9088 | supplied |
| D-sold | full soldering of the rotations to the Bloch vector | 9040, 9048, 9050, 9054, 9066, 9069, 9072, 9084, 9088, 9097 | supplied |
| D-perm | records update by compression: the lock, the support condition and the distant update | 9041, 9043, 9046, 9048, 9054, 9083, 9084, 9085 | supplied; the distant update is the one consistent with D-loc, affine joint laws and Born marginals (9085); the lock alone does not give it (9083) |
| D-tr | odds are a function of the site's (conditional) state | 9041, 9043, 9046, 9050, 9052, 9072, 9083, 9084, 9085 | supplied; the trace-rule form follows from D-loc, D-perm and the menu (9083) |
| D-relax | relaxation profile: which state records form from | 9041, 9052 | supplied (it fixes the state, not the law) |
| D-menu | antipodal menus | 9041, 9043, 9050, 9052, 9083, 9085 | antipodal follows for two-possibility menus from the support condition and normalization (9085) |
| D-set | independently formed setting records | 9043 | supplied |
| D-nn | Admissibility conditions: records alone, or states | 9043, 9046 | records alone leave the dynamics unreadable (9046) |
| D-pattern | a record carving and its contents | 9048, 9054, 9066, 9069, 9072, 9088, 9097 | supplied |
| D-sign | the sign of the Moriya coupling | 9050 | supplied |
| D-roles | doubled-coordinate roles (vertex, link, plaquette, cube sites) | 9066, 9069, 9072, 9077, 9081, 9095 | supplied |
| D-gauss | a Gauss law on link sites, exact or as a soft vertex-star energy | 9066, 9069, 9072, 9077, 9081 | supplied |
| D-star | a covariant generator on a plaquette site's four link neighbours | 9072 | supplied |
| D-loc | at equal time, marginal record distributions do not depend on distant record formation | 9083, 9084, 9085 | supplied reading of physical locality; at equal time only; given the distant update it is equivalent to affinity (9083) |
| D-rev | reversible, continuous-time, time-homogeneous evolution with a nearest-neighbour generator | 9084 | supplied; its reversibility is D-chan with D-onlyrec (9086) |
| D-chan | the evolution of a finite region between records is a channel | 9086 | supplied |
| D-onlyrec | records are the only irreversible events | 9086 | supplied reading; for channels it is reversibility (9086) |
| D-chir | a time-reversal-odd star term of weight at most three | 9088 | supplied |
| D-tsoft | a soft vector-constraint energy on link sites with one-site slot fields | 9095 | supplied |
| D-slot | the tensor slot type: rotor (unbounded) or qubit | 9095 | supplied |

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
- **9083 — the trace rule.**
  - Inside the clause's kinematics and under the compression update, a
    distant record is a recorded randomizer. The clause carries a
    purification to any distance, and recording the partner steers the
    site to either end of any chord.
  - D-loc at equal time makes the law affine. Given the distant update, it
    is equivalent to affinity, so it restates affinity as a locality
    reading. The partner's weights can come from the same law, where D-loc
    leaves `λ ∈ {0, 1}`.
  - The support condition forces `E_q = P_q`.
  - The lock alone does not give the law: a replacement update passes D-loc
    with anti-Born odds.
  - D-loc fails at later times, where the dynamics connects the sites.
- **9084 — linear dynamics.**
  - Under D-loc, a site's evolution between records, with a decoupled
    partner, is affine. Tested with the clause's own rotation and bond, it
    is completely positive.
  - Reversibility gives a Hermitian generator.
  - The clause's evolution is not a nearest-neighbour unitary at finite
    time. So its two-site form restates the range imposed on the generator.
- **9085 — the distant update.** Joint record effects with Born marginals
  are product projectors, so the distant update consistent with them is
  compression. The steering that gives joint affinity assumes the same
  update, so this is self-consistency and uniqueness.
- **9086 — reversibility.** For channels, "records are the only
  irreversible events" is reversibility (Wigner's condition), and it gives
  the unitary form.

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
- **9088 — time-reversal-odd star terms.**
  - Possibility covariance allows one at weight at most three: the
    orientation-weighted chirality of each octant's three neighbours, off
    the centre.
  - The landed actions allow 68, 50, 49 and 37 dimensions. None has
    Kitaev's solvable pattern.
  - On the cube, no covariant odd term keeps the loops and stays bilinear
    in the Majoranas.
  - Under the axis and full actions, the tripod keeps the loops and is
    quartic.
- **9097 — record fields and chirality.**
  - Record fields sit on dangling axes. Classing each `c` Majorana by its
    site's parity and each dangling `b` oppositely makes every coupling
    join opposite classes. So a sublattice symmetry holds, and every weak
    Chern number of the gapped bands vanishes.
  - Outside the content rule, a leaf's kept-axis field is solvable and
    breaks the symmetry.
  - Kitaev's time-reversal-odd pattern breaks it too, but the gapped
    networks stay non-chiral up to `κ = 4`.
  - A gapless start changes this. With its dangling Majoranas decoupled,
    the 20-site network is gapless. Kitaev's pattern at `κ = 0.3` gaps it
    with weak Chern numbers `(1, 0, 0)`.
  - Records cannot give that network zero fields. They can on 16 other
    networks, 8 of which are gapless.

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
- **9095 — the tensor field's generated moves.**
  - A soft vector-constraint energy `U Σ (G v)²`, one term per link site's
    neighbourhood, with one-site slot fields `h`, generates the planar
    pieces at twelfth order: `g = A h¹²/U¹¹`, `A = 111150053/31850496`.
  - The planar pieces are exactly the moves of smallest L1 norm, 12.
    Exact diagonalization confirms the amplitude.
  - For rotor slots every constraint-satisfying configuration has the same
    diagonal energy at every order. So the leading dynamics is a sum of
    planar-curvature cosines of the conjugate slots.
  - Qubit slots allow only 20-slot unit moves, at order 20, behind
    fourth-order potentials.

## What stays open

- **The kinematics.** The quantum rules above are consistency conditions
  inside Hilbert-space kinematics that the clause supplies. Deriving that
  kinematics, meaning the cross-site composition law, from the axioms is
  open.
- **Gauge group.** The exact gauge field found is Z2. U(1) needs a
  companion term of Admissibility shape. SU(2) and SU(3) need composite
  links, and no superlattice is chosen.
- **Charged chiral fermions.** The emergent fermions are Z2-charged
  Majoranas, and the clause's U(1) charges are bosons.
  - No gapless or Weyl case appeared among the three-direction networks.
  - No covariant time-reversal-odd star term keeps the cube's Majoranas
    free. The soldered tripod keeps the fluxes, and its interacting
    dynamics is unexplored.
  - Record fields keep a sublattice symmetry, so they give the gapped
    bands no Chern number.
  - A gapless start plus Kitaev's pattern gives weak Chern number 1.
    What is missing is a realizable gapless carving where a covariant
    same-class time-reversal-odd bilinear opens that gap.
- **Gravity.** No long-range rate field is generated. The landed tensor
  field needs dynamics wider than one neighbourhood.
  - A one-neighbourhood soft constraint generates that dynamics at twelfth
    order.
  - Whether a gapless tensor phase follows needs three more things: an
    electric energy, which the generated model lacks, the scalar
    constraint, and a phase analysis.
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
- **The readings themselves.** The kinematics, D-perm, D-tr, D-loc, D-chan,
  D-onlyrec, continuous time, the range, covariance, the soft constraints and
  the slot types are supplied, not derived from the axiom text.

## Consolidated certificates

The runner re-derives one identity per block, independently of that
block's runner, and checks the ledger. There are twenty-one checks and all
pass in about three seconds.
- **L.** The twenty-one declared points are exactly those used by the
  twenty blocks.
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
  a cubic deformation's shift, and an anti-Born law passing locality of
  marginals under a replacement update.
- **15.** A Weinberg-type precession's signalling shift, and the negative
  partial transpose of a singlet.
- **16.** The one-line range intersection, and tomography matching the
  Lüders state.
- **17.** Proportional Kraus operators, and a random channel's purity loss.
- **18.** Vanishing through-centre chirality sums, the invariant
  orientation-weighted octant chirality, and the tripod as a product of
  three bond operators with four odd-degree sites.
- **19.** The planar piece's exact path sum `111150053/31850496`, and the
  ring's `5/2`.
- **20.** The sublattice symmetry of a chain with dangling-axis fields, and a
  leaf pair's spectrum with its kept-axis field.

## Independent checks

Separate checkers wrote their own code without reading the campaign's
runners, and a final adversarial review examined the quantum-rules chain.
Every computation they repeated agreed. Where the prose went
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
  All computations pass. Corrected since:
  - 9085 claimed the distant collapse follows from D-loc and the lock. That
    was circular, and it now states self-consistency and uniqueness. The
    orientation comes from the support condition, and the positivity step
    of its proof is repaired.
  - 9086's reading is reversibility for channels. Closure did no
    mathematical work, the whole-region channel is now a premise, and the
    lemma is corrected.
  - 9088 missed three things: fields, the off-centre octant chirality, and
    the loop-keeping tripod. It now classifies all odd star terms of weight
    at most three, with a Majorana-degree test.
- **An adversarial review of Finding 1 (9083–9086).** It raised these
  points:
  - the Hilbert-space kinematics was used but not listed;
  - the collapse was circular;
  - the orientation comes from the support condition, not the lock;
  - D-loc is equivalent to affinity given the distant update;
  - the conditional-state premise was dropped;
  - the two-site form is imposed;
  - unitarity is inside D-onlyrec;
  - D-loc fails at later times.

  Finding 1 now carries the review's proposed scope. The blocks carry new
  checks for the distant update's role, the equal-time scope and the
  imposed range.
- **The chirality block (9097).** Every number reproduces. Corrected since:
  - the sublattice claim is scoped to the content rule, with leaves outside
    it;
  - the flat zero bands are stated, and particle–hole symmetry removes the
    condition on them;
  - band touchings are scoped to zero energy;
  - the gaps are refined minima.
- **The tensor block (9095).** Its independent check is still running.

## What this does not do

- It adopts no decision point and derives no dynamics from the axiom text.
- It does not audit, land or promote any block. The blocks are open PRs.
- Its checks re-derive identities and do not replace the blocks' own
  runners.
