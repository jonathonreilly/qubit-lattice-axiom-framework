# Assumptions and imports — block 215

Registry check (`docs/audit/data/axiom_premise_nodes.json`): the four axioms (Lattice, Qubit, Admissibility, Record) and the three approved primitives (`scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`) are the complete supplied foundation; none is used as content in this block. The Admissibility axiom's covariance clause is QUOTED (verbatim) as the candidate principle; its reach to the cell form is a reading, never a premise.

## Imposed objects (the lane's banner, inherited verbatim)
| object | source | role here |
| --- | --- | --- |
| the cube complex, corners, degree indices, wedge signature | Block 209, Block 213's `eta`/`lane_rules`/`raising_rules` | the action of rotations on the cell is built on these signs |
| the six-face-compatible cell-form family with its ties and the four free duality parameters | Block 211 (`solve_pinned`, `face_system`, `branch_moduli`, the gauge congruence `D -> E D E`) | the space on which the loci are computed |
| the corner-sign gauge (64 sign vectors, four classes) | Block 211 | the twist in "twisted covariance" |
| the 24 proper cubic rotations with exact intertwiners | Block 201 (if on the eight-corner cell) or built from the geometric action + signature | the group whose covariance is measured |
| the two assemblies (onsite, overlap) | Block 105, Block 213/214 | the overlap sum `s` (c) |
| the plane `D16 = D34 = −D25`, `F-1`..`F-4` | Block 214 | the locus whose name is sought |

## Counterfactual pass (implicit framework choices; none adopted here)
- **Proper vs full cubic group.** The axiom names PROPER rotations. Improper elements would make 2-forms a pseudo-representation and could change the `0 <-> 3` and `1 <-> 2` intertwiner spaces; not used — recorded as the direction a full-`O_h` reading would open.
- **Is `t` a lattice direction?** The chain's `(t, x, y)` are three lattice directions of `Z^3` (the 2+1D bench); a time-slice reading would restrict the symmetry to the planar subgroup fixing `t` (the `D4` about the face axis). The census reports EVERY subgroup class, so this counterfactual is covered by the table rather than chosen.
- **Covariance strict vs twisted.** Strict covariance (`E_R = 1`) is one column of the census; twisted covariance (gauge allowed) is the honest notion because Block 211's gauge is a symmetry of the six-face system. Both are reported.
- **Assembly.** Both assemblies are run; the fork is not decided (Block 214 `H-2`).
- **Moduli.** Symbolic on the family's ties; nothing at a fitted point.

## Forbidden imports
Floats, `nsimplify`, literature rotation matrices without the representation checks, any continuum/light-cone/dynamics reading, any selector.
