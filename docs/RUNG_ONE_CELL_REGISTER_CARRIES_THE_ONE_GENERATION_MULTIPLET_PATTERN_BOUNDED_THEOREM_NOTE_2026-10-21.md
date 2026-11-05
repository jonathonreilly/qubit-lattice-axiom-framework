---
claim_id: rung_one_cell_register_carries_the_one_generation_multiplet_pattern_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied Margolus tick of the candidate laws register run at rung 1 (2x2x2 cells of one-mode sites as super-sites, cell modes
  carried in parallel): exact unitarity, 24/24 covariance, band, exact internal symmetry U(8) (SO(16) with staggered
  pairings), rotation-covariant masses with multiplets 1:1:3:3, the canonical factorisation of the cell as C^2 x C^4 and
  its forced generators T3 and B-L; the charge identities that follow; for a supplied 5-mode register, its exact
  Spin(10), Fock content and exchange statistics; SMG algebra for one Weyl 16. Supplied model; finite diagnostic; no
  physical identification; no chirality, generation number, SMG gap or adopted tick is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/rung_one_cell_register_carries_the_one_generation_multiplet_pattern_2026_10_21.py
---

# A rung-1 cell of one-mode sites carries the one-generation multiplet pattern

Claim type: bounded_theorem.
Primary runner: `scripts/rung_one_cell_register_carries_the_one_generation_multiplet_pattern_2026_10_21.py`.

## Question

A register of five fermion modes, Lambda(C^3 + C^2), has a Spin(10) spinor 16 as its even sector, and with vacuum
neutrality and anomaly freedom the hypercharges are 1:-4:2:-3:6. Can the lattice realise such a register without
changing the Qubit axiom, by zooming out so that a cell of one-mode sites is one super-site? And does the result match
measured matter?

## Setting (supplied)

Sites of Z^3 with one fermion mode each. A cell is a 2x2x2 block of sites; cells form the coarse lattice 2Z^3. The tick
is the register's Margolus tick applied to cells: each half-tick, every 2x2x2 block of cells of the partition applies the spin-3/2 edge
hop W to the cells, carrying the eight modes of each cell in parallel (W x 1_8). Rotations about a coarse block centre
act as the spin-3/2 corner phase of the cell's coarse corner times the plain permutation of the cell's sites.

## Results

1. Cells. Under the 24 rotations the plain 2x2x2 cell is A1+A2+T1+T2, so T+(A1+A2) is a rotation-invariant C^3+C^2 inside
   one cell. (Within the spin-3/2-twisted action the cell is 2 x G3/2 and has no such subspace; that is the scope of the
   earlier no-go.) The 4^3 cell gives multiplicities (4,4,4,8,8) for (A1,A2,E,T1,T2); the six-site octahedron gives T1+E but
   is not a Margolus cell.
2. Spin-statistics. With the spin-3/2 coarse twist the 2pi turn is -1 only if the cell index carries a non-spinorial
   action: the plain one (A1+A2+T1+T2) or the j=1 one (E+T1+T2).
3. The rung-1 tick is unitary and commutes with all 24 rotations about both coarse block centres (8^3 sites, to 2e-15).
   Its band is the Margolus band in the coarse momentum, each level eight times.
4. Exact internal symmetry. Every internal operator 1 x X commutes with the tick: U(8). The tick is real in a cell-phase
   gauge, so staggered pairings are conserved as well: SO(16). Rotation-covariant masses, one per irrep, leave
   SO(2)^2 x SO(6)^2, which contains U(1)^2 x U(3)^2; the light levels are 1:1:3:3. Equal masses on T1+A1+A2 leave an exact
   SO(10) on that five-mode register times SO(6).
5. Factorisation. Each corner is a pair (tetrahedron parity, body diagonal), so the cell is C^2 x C^4 canonically, and a
   rotation acts as X^[odd] x P_diag. The traceless rotation-invariant generators on one factor are unique up to scale:
   T3 = X/2 and B-L = (1 - 4 P_A1)/3, with eigenvalues 1/3 (three times) and -1.
6. Charges. For Q = a T3 + b (B-L)/2 + c F, q_e + q_p = 4c and q_n + q_nu = 4c identically. With c = 0 and b = a the
   charges are (2/3, -1/3, -1, 0). If L lives on even cells with SU(2) on C^2 and R on odd cells, Y = (B-L)/2 on L and
   T3 + (B-L)/2 on R give the left-handed 16 with ratios 1:-4:2:-3:6 and every anomaly zero.
7. Massless tick: independent unitaries on even and odd cells commute with it (U(8)_e x U(8)_o). The masses mu and b break
   this to the diagonal, and the 12 odd rotations exchange even and odd cells.
8. Five modes per site (axiom change). W x 1_5 keeps everything, and the full register Spin(10) is exact (the tick is
   real in a site gauge). But Spin(10) moves single fermions as its vector 10; its 16 lives in a register's Fock space,
   where the commutant is span{1, (-1)^N}. The only Y-neutral register states are the empty and the full one. Over the
   empty one the 16 states are bosons. Over the full one they are fermions, but only L and d^c are single holes; Q, u^c
   and e^c are three-hole states and nu^c a five-hole state. Either way no whole generation is elementary.
9. SMG algebra for one Weyl 16 at a site: no invariant 16-16 bilinear. Without the spin pair (16 modes) there is no
   singlet in Lambda^1..8, so no invariant quartic. With it (32 modes) Lambda^2 has none and Lambda^4 exactly one, the
   10-channel pair square; the pairs and their adjoints generate a 66-dimensional algebra (so(12)).

## Against measurement

- The 1:1:3:3 pattern is the measured Dirac pattern of one generation: nu, e, and colour triplets u and d.
- The literal register reading (even sector = generation) makes quarks and leptons bosons (empty vacuum) or makes Q,
  u^c and e^c three-mode composites (full vacuum); measured quarks and leptons are elementary fermions. Under a free
  tick only a 5 or 5bar propagates as single particles.
- The cell is vector-like (finite-range tick), so measured parity violation is not reproduced.
- Each internal state comes with the two Margolus tastes; LEP's N_nu = 2.984 +- 0.008 excludes a light doubled
  neutrino, so one taste must be removed.
- One cell gives one generation, not three.

## Not claimed

Supplied: the rung-1 rule, the plain internal action, the masses, the gauged subgroup, the chiral assignment and the
5-mode register. No chirality, mirror gapping, generation number, mass ratio or SMG gap is established; the 2^32-state
site was not diagonalised.
