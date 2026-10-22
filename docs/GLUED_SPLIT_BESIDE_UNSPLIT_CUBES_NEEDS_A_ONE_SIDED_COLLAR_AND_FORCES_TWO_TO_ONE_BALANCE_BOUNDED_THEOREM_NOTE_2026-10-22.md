---
claim_id: glued_split_beside_unsplit_cubes_needs_a_one_sided_collar_and_forces_two_to_one_balance_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's glued split of a cube into children at half the edge, beside unsplit cubes, on the alternating five-tetrahedron triangulation (child units: axis window [1, 2], diagonal [sqrt2, 2 sqrt2]): each site's six forward registers partition the edges (384 = 6 x 64 on a 4^3 torus), and a split's 64 children sit at its 8 sites, the midpoints of exactly its 48 owned edges and 8 cell centres; the two tilings share no edge and their passings send a shared site to disjoint child sets, so the even tiling owns the split; the child triangulation is nested in the parent's (320 of 320 tetrahedra) but is no bisection of it; all 9 tested refinement patterns close to a simplicial complex. A bisected parent edge passes as two children inside their windows only when full (stated). An exact LP shows that beside an isolated split cube every child register in a partly refined parent tetrahedron is held at its floor and the parent edges it reads are held full: 42 of the 48 owned edges plus a one-sided collar of 36 edges, the 12 in-plane registers of each unsplit +x, +y, +z face neighbour; the collar moves with the pattern (60 edges from 5 blocks with a +x neighbour split; 144 from 12 for a 2^3 super-block); every child cube of an isolated split cube owns a held register, so 2:1 balance is forced; with the held values and free edges in a 30% band below full, all 5491 closure tetrahedra keep positive volume. A link endpoint rule (child odd centre if complete, else the nearest parent odd centre) has no ties and the right bond count on all 256 patterns of a 2^3-block torus, and Gauss's law is solvable on 6 sampled patterns x 3 random configurations. In a three-block register toy (2S = 2, dimension 5832) the glued generator with collar is hermitian and keeps the orthogonal sum over the 8 patterns exactly; without the collar odds reach states outside it (weight up to 0.892). In a one-particle toy the passing's channel modes make mixed odd cubes tick unitarily and reproduce the parent's odd half-tick at the split moment (6e-17). Supplied model, finite diagnostic: flat closure template and bookkeeping centres, small tori and toys; no full register dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/glued_split_beside_unsplit_cubes_needs_a_one_sided_collar_and_forces_two_to_one_balance_2026_10_22.py
---

# The glued split beside unsplit cubes needs a one-sided collar and forces 2:1 balance

Claim type: bounded_theorem.
Primary runner: `scripts/glued_split_beside_unsplit_cubes_needs_a_one_sided_collar_and_forces_two_to_one_balance_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) stores each edge of the alternating five-tetrahedron triangulation in an edge register on a window, and when a cube's edges fill the window the glued split replaces it by children at half the edge. Only lengths at which every tetrahedron has positive volume occur. In three dimensions a split cube borders unsplit cubes, so the refined and unrefined triangulations meet at hanging nodes. This note asks which edges a split owns, which tiling owns it, how the mixed region is triangulated, what the windows force at the interface, how links keep Gauss's law, whether the glued generator stays unitary on the sum over refinement patterns, and how matter crosses the interface. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Ownership, tilings, nesting, closure (coarse sites at even integer coordinates, children at all integers).

1. Each site's six forward registers (the three +axis edges and the even diagonal of each forward face) partition the edges. A split puts its 64 children at its 8 sites, at the midpoints of exactly its 48 owned edges, and at the centres of the 8 cells its sites are least corner of.
2. The two tilings' cubes share no edge; an odd cube's corners lie in 8 even blocks; the two passings send a shared site to disjoint child sets, so one tiling (the even) owns the split; 1 of a block's 8 cells is wholly its own.
3. The children's triangulation is nested in the parent's, but it is no bisection of it: each first bisection of a parent corner tetrahedron draws a non-lattice edge.
4. Every tested refinement pattern closes to a simplicial complex: the children's tetrahedra where all 6 parent edges are bisected, otherwise a cone from the cell centre over a canonical subdivision of each face (a finite check on 9 patterns).

B. The windows force the interface.

5. A parent edge passes as two children inside their windows only when it is full: l1 + l2 = l, l1, l2 >= L, l <= 2L give l1 = l2 = L and l = 2L. So all 48 edges a split bisects must be full, not just the 18 of its tiling cube. (Stated in the runner, not computed.)
6. Beside an isolated split cube, every child register in a partly refined parent tetrahedron is held at its floor, and the parent edges it reads are held full: 42 owned edges plus a collar of the 12 in-plane registers of each unsplit +x, +y and +z face neighbour (exact LP per tetrahedron). The trigger therefore reads the 48 owned edges and the 36 collar edges, 84 in all.
7. The collar moves with the pattern: when the +x neighbour is split it drops its share; a 2^3 super-block has a 144-edge collar from 12 blocks, so no finite block of blocks closes on its own.
8. 2:1 balance is forced: every child cube of an isolated split cube owns a held register and can never split; in a 2^3 super-block 8 of its 64 child cubes are free.
9. If a neighbour may read a bisected edge beyond its own window, the collar stands but fewer hanging-face children are held (a contrast).
10. With the held values and the free edges anywhere in a 30% band below full, every closure tetrahedron read affinely from its flat parent has positive volume, so the positive-volume restriction holds on the closure.

C. Links: Gauss's law on the sum over patterns (torus of 2 x 2 x 2 blocks).

11. A child link ends at its odd centre if that child odd cube is complete, otherwise at the nearest parent odd centre, with no ties; unsplit links keep their laws. On all 256 patterns the bond labels are distinct and their number is right; on the sampled patterns Gauss's law is solvable for a parent field obeying it and random child occupations (every connected component of the child bonds carries zero net residual divergence, and vertices with only coarse bonds keep their old law).

D. Register toy: the glued split with collar on a ring of three blocks (each block coarse with bulk and minus-face registers, or split with two child registers; 2S = 2).

12. The kinematic space is the tensor product over blocks of (coarse + split); local commuting projectors (the glued trigger with collar, the held collar, the held children) cut it into an orthogonal sum over the 8 patterns; the glued generator is hermitian and keeps that sum exactly.
13. With the trigger on owned edges only, the split fires with the collar below full, which puts children below their floor (no state there), and the odds go there (a contrast).
14. Register shifts never change the pattern and are undefined on held edges, so shift-invariant odds are a sum over patterns and the response law's tick acts sector by sector (checked on the toy's register shifts).

E. Matter: one-particle toy on a 4^3 torus with block A split.

15. The passing's 8 channel modes (the equal-weight sum of one corner over the 8 children) are orthonormal with disjoint supports; mixed odd cubes tick on them, and the full tick is unitary.
16. On the split image the mixed odd half-tick is the passing of the unsplit one, so the split is invisible to neighbours when it fires; the complete child odd cube overlaps every mixed cube and must wait.
17. Channel-mode mixed cubes let a particle cross into the children; freezing them would wall the split region off (a contrast).

## Derivation

Items 1 to 3 enumerate edges, children and tetrahedra on a coarse 4^3 torus and test containment by barycentric coordinates. Item 4 builds the closure for 9 patterns (single split, four neighbour pairs, a 2^3 block and three random patterns on a 3^3 block neighbourhood), counts each face's incidence and checks the total volume. Items 6 to 9 set up, for every partly refined parent tetrahedron, the affine reading of the child registers inside it from its six parent squared edges, with window bounds on parent and child, and solve an exact linear program (scipy HiGHS) for the extremes of each parent edge and each child register; an edge is held when its extremes coincide with a window wall. Item 10 draws six random coarse configurations and computes each closure tetrahedron's Cayley-Menger volume. Item 11 builds the bond graph for every pattern on the 2^3-block torus and, for the patterns with index a multiple of 37 (six nonempty patterns), solves the parent field by least squares and sums the child residual divergence per connected component, three random draws each. Items 12 to 14 build the register toy's configuration space and generator as sparse matrices and evolve to t = 12 with expm_multiply. Items 15 to 17 build the one-particle cube unitaries with hop angle 0.6 and compare the mixed odd half-tick on the split image with the parent's.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Ownership: 384 edges = 6 x 64 sites on the 4^3 torus; children 8 + 48 + 8 = 64; no other edge's midpoint is a child of the split.
- Tilings: no shared edge; odd-cube corners in 8 even blocks; disjoint passing images (site (1,1,1): (1,1,1).. against (2,2,2)..); own cells 1 of 8.
- Nesting: 320 child tetrahedra nested, 0 not; non-lattice first bisections 6 of 6.
- Closure: 9 patterns, unmatched faces 0, orphan points 0, total volume matched; single split: 916 tetrahedra and 60 cone apexes that are not lattice points.
- Held edges beside an isolated split: owned 42 of 48, collar 36 from the (2,0,0), (0,2,0), (0,0,2) neighbours, child registers held 309 of 384, free child registers in partly refined tetrahedra 0. (The total 84 is stated in the runner's label as 48 + 36.)
- Collar with a +x neighbour split: 60 edges from 5 blocks; 2^3 super-block: 144 edges from 12 blocks.
- Free child cubes: isolated split 0 of 8; 2^3 super-block 8 of 64.
- Reading beyond the window: collar 36; held children 63 against 309.
- Closure positivity: 5491 tetrahedra, nonpositive 0; minimum child-to-parent volume ratio 0.062.
- Links: 256 patterns, ties 0, 18 solvability checks passed.
- Register toy: dimension 5832, allowed 1505, 8 patterns; generator hermitian, leak out of the pattern sum 0e+00, norm kept; split fraction up to 0.10.
- Register shifts: pattern changes 0.
- Channel modes: |B B^T - 1| = 2e-16; full tick unitary to 1e-12.
- Split image: |U_o V - V U_o,parent| = 6e-17; max |[U_child, U_mixed]| = 0.03.

Finite diagnostics (contrasts, supplied model, finite diagnostic):
- Owned-edge trigger without collar: weight outside the pattern projector up to 0.892.
- Weight on the children within 12 ticks: 0.146 with channel-mode mixed cubes, 0e+00 with the mixed cubes frozen.

## Estimates against measurement

Estimates with supplied inputs (L = sqrt(8 pi) l_P, metric-perturbation amplitude 1e-5 at the shortest probed scale lambda = 1e-19 m):
- Collar wait: neighbouring edges differ by about 1e-5 x 2 pi L/lambda, so the split waits about 7e-20 of a doubling for its collar.
- Bound regions: next to a cube that never fills, one layer stalls full, and forced 2:1 balance grades the region one level per layer; with the runner's supplied level count log2(7) this is 2.8 levels, a shell of about 9e-34 m.

## Boundary

Supplied: forward ownership (read from the passing's child placement); the closure template and its cone apexes at cell centres on flat parents; the affine reading of child registers from their parent tetrahedron; the sum-in-window reading of item 9; channel-mode mixed ticks and a deferred child odd tick; the toy hop, the register size 2S = 2 and the three-block ring; the link endpoint rule of item 11; the estimates' inputs. Forced, given those: the edge partition and the even tiling's ownership; nesting without bisection; closure of the tested patterns; the held owned edges, the one-sided collar and its movement with the pattern; forced 2:1 balance; positivity of the closure tetrahedra in the sampled band; the tie-free link rule and the sampled Gauss solvability; the exact pattern-sum invariance of the glued generator with collar in the toy; the unitarity of the channel-mode tick and its agreement with the parent tick at the split moment. Not claimed: closure for every refinement pattern; Gauss solvability on every pattern; positivity outside the sampled band; register dynamics beyond the toys; curved parents; the choice of closure template as unique.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's edge registers on the alternating triangulation, its window, the glued split and the passing; the positive-volume restriction; the links and Gauss's law; the response law's register shifts. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/glued_split_beside_unsplit_cubes_needs_a_one_sided_collar_and_forces_two_to_one_balance_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 10 s with about 105 MB resident, prints about 5.3 kB and ends with `TOTAL: PASS=19 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the elapsed-time line.
