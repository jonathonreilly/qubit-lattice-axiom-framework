---
claim_id: one_light_dirac_copy_needs_a_tick_written_on_larger_cells_than_two_cubed_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For covariant partitioned ticks with one fermion mode per site of Z^3, two-partition L^3 Margolus ticks are cubic covariant only for offset (L/2)(1,1,1), so none exists for odd L; a spinorial site character exists only for stabilisers C1, C2, C3, C4, D3 (with parity only Cs, C3v, D3d), and at the 2^3 corner parity forces the j = 3/2 type; for the 2^3 rung no site action gives the representation content one Dirac copy at an invariant momentum needs, the smallest geometries with that content have 16 sites per cell (rotations) and 32 (with parity), integer-spin site actions force an even copy count, and reading the supplied 2^3 tick on 4^3 cells keeps two copies; a supplied 4^3 Margolus tick with exactly one light Dirac copy exists on the grids checked. Finite diagnostics; the 4^3 block rule, its mass tuning and the hop are supplied. No adopted cell rule, chirality or physical matter content is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_light_dirac_copy_needs_a_tick_written_on_larger_cells_than_two_cubed_2026_10_21.py
---

# One light Dirac copy needs a tick written on cells larger than 2^3

Claim type: bounded_theorem.
Primary runner: `scripts/one_light_dirac_copy_needs_a_tick_written_on_larger_cells_than_two_cubed_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its supplied tick on 2^3 blocks has two light Dirac copies. This note asks which cell geometries of covariant partitioned ticks, with one fermion mode per site of Z^3, leave room for exactly one. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are kept: one mode per site, finite range and partitioned updates all remain. What changes is the rung on which the tick is written.

The result is positive within supplied models. One light copy is possible, but only on larger cells. The 2^3 rung cannot give one copy for any site action, and neither can a coarser reading of the existing tick.

## Statement

1. Partition geometry. A two-partition Margolus tick on L^3 blocks is cubic covariant about a common centre only for offset 0 or (L/2)(1,1,1). No two-partition covariant tick exists for odd L, and for L = 2 only the offset (1,1,1) works.
2. Site actions. A spinorial site character, with the 2 pi rotation acting as -1, exists exactly for the stabilisers C1, C2, C3, C4 and D3. It exists for none of D2, D4, T and O. With parity, the live stabilisers are Cs, C3v and D3d only. At the 2^3 corner (C3v), parity forces chi(C3) = -1, which is the j = 3/2 type, so the K = 0 space is G_(3/2)g + G_(3/2)u. The spin-3/2 choice on 2^3 blocks is therefore not arbitrary.
3. Counting for one Dirac copy. A single copy at a cubic-invariant momentum needs E_(1/2) or E_(5/2) with multiplicity at least 2 under rotations only, one for the particle and one for the antiparticle. With parity it needs the pair E_(1/2)g + E_(1/2)u. Any non-invariant momentum comes in a star of at least 3 points, so it gives at least 3 copies. On the 2^3 rung no site action gives multiplicity 2 under rotations, and none gives a pair with parity. The smallest geometry with room and no dead sites has 16 sites per cell under rotations (two FCC sublattices) and 32 with parity (two BCC sublattices). The uniform 4^3 cell has two parity pairs.
4. Integer-spin sites. The spinorial irreps of the double cube group have dimensions 2, 2 and 4, all even. If every site is integer-spin, a light spin-1/2 sector carries E_(1/2) x tau with tau spinorial, so the copy space has even dimension, at least 2.
5. Zoom. Reading the supplied 2^3 tick on 4^3 cells still gives exactly 8 light states, two copies, with fourfold rest levels. Coarse-graining folds doublers onto K = 0 and never removes a light state. Only a tick defined at the 4^3 rung changes the count.
6. A supplied 4^3 tick with one copy. The tick is a 4^3 Margolus tick with offset (2,2,2). On even blocks, H_A = (pi/2) Q + c0 P + m0 (P_g - P_u), where P_g and P_u project onto the E_(1/2)g and E_(1/2)u multiplets (rank 2 each) of the 24 edge-centre sites. On odd blocks a covariant hop t h is applied, and the tick is e^(-i H_A/2) e^(-i t h) e^(-i H_A/2). It is unitary and commutes with the double-group lifts of O_h and with translation by 4. At K = 0 it has exactly 4 light states, E_(1/2)g at +mu and E_(1/2)u at -mu. The other 60 bands stay at least 1.17 from both 0 and pi on the points checked. The light band has Dirac form with v = 0.6775 sites per tick, and the gap closes at K = 0 only as mu goes to 0.

## Derivation

Item 1: covariance about a common centre requires the rotation group to map the even tiling onto itself or onto the odd one, which fixes the offset modulo L to 0 or (L/2)(1,1,1). Item 2: a site's mode is a one-dimensional representation of the double cover of its stabiliser that sends the 2 pi rotation to -1, and such a character exists only for the listed groups. Item 3: the Bloch space at an invariant K is the induced representation from the site characters, so its multiplicities follow from the characters of the double group O' and of O_h'. Item 4 is the evenness of the spinorial irreps. Item 5 holds because folding relabels the Bloch states without changing the tick's spectrum.

## Checks

The runner prints 20 PASS lines, and its output ends `TOTAL: PASS=20 FAIL=0`.

- Section 1: the offset table for L = 2 to 5.
- Section 2:
  - the spinorial-stabiliser table;
  - the j = 3/2 type at the C3v corner (2 characters);
  - the lists of live and dead stabilisers with parity.
- Section 3:
  - the printed survey of all O-invariant translation sublattices of index up to 64, with E multiplicities, parity pairs and dead-site counts;
  - none at the 2^3 rung;
  - the smallest geometries: fcc2 at 16 sites under rotations, and bcc2 at 32 sites with parity.
- Section 4: irrep dimensions 2, 2 and 4.
- Section 5: 8 light states at |w| = 0.05 in the zoomed 2^3 tick.
- Section 6:
  - the induced site action is a representation (9.8e-16), and the edge-centre projectors have rank 2;
  - unitarity;
  - covariance on an 8^3 torus (1.5e-15 over 6 lifts);
  - the Bloch tick matches 512 real-space quasi-energies (1.6e-15);
  - exactly 4 light states at K = 0, at w = +-0.01;
  - on a 13^3 grid, heavy bands at least 1.171 from 0 and from pi, light bands at least 0.140 from 0 for |K| > 0.3, and the light maximum 0.596. The same light content holds on 600 random points;
  - the Dirac fit within 2.6e-4 for |k| <= 0.016, with v = 0.6775, e2 = -0.058, direction spread 2.4e-4 and spin splitting 3.7e-15;
  - the k^2 offset 2 mu e2 / v^2 = -0.003;
  - closure of the gap at K = 0 only when mu goes to 0 (1.6e-15).

The grid and random-point checks are finite diagnostics. They do not prove that no other light states exist.

## What is supplied and the boundary

Supplied:
- the two-state edge multiplets, put in by hand;
- the heavy level pi/2;
- the mass m0 = 0.30282, tuned so the levels at Gamma sit at +-0.01 (Wilson-like);
- the choice among the allowed site phases;
- the choice of hop.

Not established:
- an adopted cell rule. Writing the tick on 4^3 cells fixes room for one copy, not the block unitary;
- chirality;
- any physical matter content.

A single Weyl node at quasi-energy 0 would still need an opposite node at pi, which would count as a second light species. Exact parity would conflict with weak-interaction parity violation unless something else breaks it. The light band reaches |w| = 0.60, past the switching-law domain of 1/2 near the zone edge.
