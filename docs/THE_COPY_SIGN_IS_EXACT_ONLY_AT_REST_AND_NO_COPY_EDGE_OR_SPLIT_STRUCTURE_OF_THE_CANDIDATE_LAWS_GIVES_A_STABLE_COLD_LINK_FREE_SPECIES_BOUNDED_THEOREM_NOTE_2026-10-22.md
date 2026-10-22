---
claim_id: the_copy_sign_is_exact_only_at_rest_and_no_copy_edge_or_split_structure_of_the_candidate_laws_gives_a_stable_cold_link_free_species_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For CL-1's cube tick with the copy mass, read on diagonal metrics: R_i = sqrt3 W_i are Clifford generators and G = i R1 R2 R3 is central, so the copy sign s = G R commutes with the even half-tick and the copy mass at every metric; on Bloch states the odd half-tick keeps s exactly at K = 0 (flat and a random metric, 7e-16) and not at random K (0.52); at K = 0 the s = -1 copy has rest phase mu + M; cell-local operators commuting with the tick at three random K (and three metrics) are only the identity; a one-cube traceless strain vertex taking the heavy copy at rest to the light copy at recoil q vanishes at q = 0, grows as q/M, and is O(1) (0.30 to 0.93) at a real decay's recoil q = 0.87 M for M = 0.5 and 0.05, while conformal strain gives zero; the second-quantised copy sign commutes with mode number, so each copy carries its species' link charges. For one chiral family (hand-entered table) nu^c is the only link-free Weyl state and nu^c nu^c the only singlet bilinear, Z4 = i^(B-L)-odd. An edge register's hop and value have trivial commutant and the hop anticommutes with (-1)^n. Squared edge lengths are a linear bijection of a tetrahedron's Gram matrix, so the positive-volume set is convex and the flat vacuum manifold contractible; exhaustive scans of one tetrahedron (s = 2, Delta = 0, 1) find every positive-volume state connected to the flat one by single steps; a child edge at the parent value minus s is exactly half the parent length. Estimates against measurement use supplied inputs. Supplied model, finite diagnostic: (b, mu, M), metric weights, the charge table, s and Delta, the unit map, the graviton-coupling normalisation, y, measured bounds; the label-parity survivor N' and the edge-register root are cited, not recomputed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_copy_sign_is_exact_only_at_rest_and_no_copy_edge_or_split_structure_of_the_candidate_laws_gives_a_stable_cold_link_free_species_2026_10_22.py
---

# The copy sign is exact only at rest, and no copy, edge or split structure of the candidate laws gives a stable, cold, link-free species

Claim type: bounded_theorem.
Primary runner: `scripts/the_copy_sign_is_exact_only_at_rest_and_no_copy_edge_or_split_structure_of_the_candidate_laws_gives_a_stable_cold_link_free_species_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The measured dark matter has Omega_c h^2 = 0.120, is cold, is collisionless to sigma/m below about 1 cm^2/g, carries no electromagnetic or colour charge, and is stable over the age of the universe. The register lists no candidate (predictions row K6). Building on the label-copy note (PR #9946) and the link-free-slot note (PR #9877), this note searches four further places in CL-1 to CL-3, without axiom edits. It names what would conserve each candidate and tests that protection exactly on small registers:
- (a) the s = -1 copy of CL-1's cube tick;
- (b) edge-register quanta;
- (c) nu^c;
- (d) split and geometry defects.

## Statement

A. The copy sector.

1. R_i = sqrt3 W_i anticommute and square to one, so R(c)^2 = 1 for every diagonal metric. G = i R1 R2 R3 is central in their Clifford algebra, so s = G R commutes with R. The even half-tick and the copy mass therefore keep s at every metric.
2. On Bloch states the odd half-tick commutes with s exactly at K = 0, for the flat metric and for a random diagonal metric, but not at generic K. There the s = -1 copy has rest phase mu + M and the s = +1 copy has rest phase mu. So the copy sign is an exact number of states at rest only.
3. No cell-local operator other than the identity (particle number) commutes with the tick at three random K, with or without three random metrics. The laws carry no copy number.
4. Consider a one-cube traceless (spin-2) strain vertex taking the heavy copy at rest to the light copy at recoil q. It vanishes at q = 0 and grows as q/M. At the recoil of a real two-body decay, q = 0.87 M, it is O(1) (0.30 to 0.93) at both M = 0.5 and M = 0.05. Exactness at rest therefore suppresses no real decay. A conformal strain gives exactly zero, since R is normalised.
5. The second-quantised copy sign commutes with mode number. Link charges are q times number, so each copy carries its species' link charges. The heavy copy of a charged species is charged. The heavy copy of nu^c, N_c, is link-free only if the tick's Dirac partner of nu^c is link-free, which the supplied chiral content decides.

B. nu^c. In one chiral family nu^c is the only link-free Weyl state, and nu^c nu^c is the only gauge-singlet bilinear. It is odd under Z4 = i^(B-L), while L H nu^c and (nu^c)^4 are even. So nu^c has no Majorana mass in a Z4 vacuum: it is the Dirac partner of nu_L.

C. Edge registers. The register hop and the register value have trivial commutant, and the hop anticommutes with (-1)^n. No edge-register number or parity is conserved by any edge-local term.

D. Split and geometry defects.

1. Squared edge lengths are a linear bijection of a tetrahedron's Gram matrix. Positive volume is a convex cone in squared lengths, the window is a box, and their intersection over all tetrahedra is convex. The flat vacuum manifold PD(3) is contractible, so no topological geometry charge exists: no geometric monopole, string or wall.
2. In the discrete registers (s = 2, Delta = 0 and 1, corner and central tetrahedra), every positive-volume state joins the flat state by single register steps. No geometry is frozen.
3. Under the passing, a child edge at the parent's value minus s is exactly half the parent's length. A split's children in their vacuum therefore read the parent's flat geometry. CL-3 measures departures from the vacuum of the same edges, so a refined bubble has zero departure and does not gravitate.

E. Conserved numbers. Only label parity (supplied, #9946) and magnetic charge (not dark, #9946) stabilise a massive relic. This note adds that the copy sign, edge value, edge parity and refinement pattern are not conserved for moving states, and that the geometry carries no topological charge.

## Derivation

The cube tick is built from the law text: spin-3/2 overlap phases along the body diagonals, hop weights from a diagonal metric, the copy sign read from the even cube, and the copy mass on even cubes only. It is set in Bloch form with the odd cube read in the even cube's sublattice labels. Items A1, A2 and A5 are matrix identities. A2 is checked on Bloch matrices. A3 diagonalises the commutator superoperator of {Ue, Uo(K)} over several K and metrics. A4 takes the derivative of the even half-tick with respect to a strain c -> (1,1,1) + h dc as a one-cube vertex. It then projects that vertex between the two heavy positive-phase states at K = 0 and the two light positive-phase states at K = q, maximised over six seeded directions. A5 builds 8-mode Jordan-Wigner operators. B scans the hand-entered table. C uses the commutant of {hop, diag(n)} on 9 levels. D1 computes the rank of the linear map from Gram matrix to squared lengths. D2 enumerates all 9^6 and 11^6 register states of one tetrahedron, tests the Gram matrix for positive definiteness, and labels 6D components with single-step connectivity.

## Finite checks

Exact or closed-form (the runner asserts each):
- Clifford relations and [G, R_i] below 1e-15.
- Fock: [S_hat, N_hat] = 0.
- Link-free state ['nu^c']; singlet bilinear [('nu^c', 'nu^c')]; the Z4 signs.
- Register commutant dims 9 (hop alone) and 1 (hop and value); hop anticommutes with parity.
- Gram-map rank 6; child length exactly half.

Finite diagnostics at (b, mu, M) = (0.3, 0.4, 0.5) unless stated (supplied model, finite diagnostic):
- Rest phases 0.9 (s = -1) and 0.4 (s = +1).
- ||[s, Uo]|| is 7e-16 at K = 0 (flat and metric) and 0.524 at a random K.
- Commutant dims: 16 at K = 0, 1 at three K, 1 at three K x three metrics.
- Strain vertex at q = 0.1 M and 0.87 M: 0.038 and 0.297 (M = 0.5); 0.046 and 0.358 (M = 0.05); 0.769 and 0.929 (M = 0.05, mu = 1e-3). It is zero at q = 0 and zero for conformal strain.
- Tetrahedron scans: 8052/531441, 8849/531441, 12876/1771561 and 13959/1771561 positive-volume states, each in one component that contains the flat state.

## Estimates against measurement

Supplied inputs:
- the unit map a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c): 1 rad per tick = 2.1e18 GeV;
- the graviton width g^2 M^3/(32 pi Mbar^2), with g the vertex at recoil;
- y = 3e-13;
- an invisible-decay bound of 8e18 s;
- LEP's ~100 GeV bound on new charged leptons;
- sum m_nu < 0.07 eV.

Estimates by candidate:
- (a) N_c. At the natural M (about 1e18 GeV) it decays in about 1e-42 s. The graviton channel gives tau = 4e6 s at 1 TeV, and tau > 8e18 s needs M < 82 MeV. But M is one law-text constant for every copy (the law gives it no species index), and an 82 MeV heavy electron copy is excluded. The Yukawa leg gives about 2 s at 1 TeV. Excluded at every M.
- (b) Edge quanta. The lowest massive root of 1.49 per block tick (cited from the edge-set computation via #9946) gives 7.9e16 GeV at b_e = 40. There is no conserved number, so they decay to gravitons at the cell rate. Excluded.
- (c) Dirac nu^c. It is hot, with Omega h^2 <= 7.5e-4 even if fully thermal. Freeze-in through h -> L nu^c gives Y ~ 2e-13 and Omega h^2 ~ 3e-15. The heavy reading is Z4-forbidden, and in a Z4-breaking vacuum nu^c decays through L H nu^c. Excluded.
- (d) Split bubbles have zero departure, so they have no gravitating mass and no charge. Link monopoles are stable but magnetic (#9946). Excluded.

Ranking:
1. N' (#9946): stable only with a supplied label parity, m about 3e13 to 1e17 GeV, non-thermal, abundance supplied.
2. N_c: it would need a supplied copy parity (one that keeps each term even in s = -1 modes at every K), and it then reduces to the N' case.
3. Dirac nu^c.
4. Edge quanta.
5. Split and geometry defects.

None has an abundance set by the rules: in every case the abundance is an initial-state condition or a supplied production history.

## Boundary

Not claimed:
- a dark-matter species of CL-1 to CL-3;
- the graviton-coupling normalisation of the strain vertex (only its q dependence and size per unit strain are computed);
- vertices from supplied four-mode or Yukawa lattice terms, which could break s even at rest;
- a species-dependent copy mass, which the law text does not have; a 82 MeV neutral-only copy mass would reopen N_c's lifetime, not its abundance;
- the whole-cube 18-edge configuration space, beyond the convexity argument;
- the label-parity survivor and the edge-register root, both cited.

The link-freeness of N_c rests on chiral content, which no law supplies.

## Supplied vs forced

Supplied: (b, mu, M), the diagonal metric weights, the charge table, s and Delta, the unit map, the graviton normalisation, y, the measured bounds.

Forced, given these:
- s is exact at rest and on the even half-tick at every metric, not for moving states;
- the heavy copy's extra rest phase is M;
- no cell-local copy number exists;
- the copy-changing strain vertex is O(1) at real recoil;
- copies share link charges;
- nu^c is the sole link-free Weyl state and is Z4-Dirac;
- no edge-register number or parity exists;
- the geometry configuration space is convex and connected, with no topological defects;
- split children have zero departure.

Possible replacement rule (not adopted, owner decision): an exact Z2 in the update that keeps every non-tick term even in the s = -1 copy at every K. Like label parity, it would be a new supplied symmetry, not a theorem of the present laws.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. Unchanged.
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1's copy sign and copy mass, the edge registers and window, the split's passing, CL-3's vacuum standard. Zero premise weight; results using it are conditional on it.
- Companion results: LABEL_COPIES_CARRY_LINKED_FAMILIES_AND_ONLY_A_SUPPLIED_LABEL_PARITY_OR_MAGNETIC_CHARGE_STABILISES_A_MASSIVE_RELIC_BOUNDED_THEOREM_NOTE_2026-10-22 (PR #9946; N', monopoles and the edge root, cited) and CANDIDATE_LAWS_LEAVE_ONLY_A_LINK_FREE_SPECIES_AS_DARK_MATTER_SLOT_BOUNDED_THEOREM_NOTE_2026-10-21 (PR #9877).

## How to run

```
python3 scripts/the_copy_sign_is_exact_only_at_rest_and_no_copy_edge_or_split_structure_of_the_candidate_laws_gives_a_stable_cold_link_free_species_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 120 MB resident, prints about 4.4 kB and ends with `TOTAL: PASS=14 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output.
