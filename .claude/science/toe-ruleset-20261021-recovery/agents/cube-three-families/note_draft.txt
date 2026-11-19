Cube-cell three-family candidates: regular split, Heisenberg slab, and the unique [[8,3,3]] code
Bounded theorem note, 2026-10-24 (draft; probe agent, TOE-ruleset campaign, synthesis item B)
Runner: cube_cell_three_family_candidates_2026_10_24 (18 PASS, 0 FAIL, about 1 s). Criteria were fixed before the run (criteria_pre_run.txt).

Claim scope
Three exact checks of the wizard-panel family proposals: w1 (the regular representation of a point group), w3 (Delta(27) on class-preserving hops) and w4 (the [[8,3,3]] cell code). Each check settles whether its "3" is forced or chosen. Free fields and finite group/code theory only. No physical identification is claimed, and no CL or axiom text is proposed.

(i) Regular-representation split [T]. HYPOTHESIS H1 FAILS (numerology).
- Embeddings: T and T_h embed in O_h, T embeds in O, and 2T embeds in 2O.
  - 2T does not embed in O_h: 2T contains Q8 and O_h does not.
  - T and T_h do not embed in 2O: 2O has a single involution.
- Restriction: Res_H L^2(G) = [G:H] L^2(H).
- Families: take family f to be the omega^f eigenspace of an order-3 turn c.
  - Each family has dimension |G|/3 for ANY G of order 48. The reason is that c acts freely, so this is arithmetic, not structure.
  - O gives 3 families of 8.
- Three pairs give 3 x 16:
  - (O_h,T) and (O_h,T_h) split as 4 + 12 (one-dimensional label blocks plus triplet blocks).
  - (2O,2T) splits as 2 + 8 + 6. The 8 sits in doublet blocks, so it can be read as 4 doublets plus 8 singlets, which matches the SM's doublet/singlet count.
  - So two inequivalent "SM-like readings" exist. This is w1's own failure condition.
- The families are not identical under G: conjugation either fixes the three labels or swaps families 1 and 2 (Aut Z3 = Z2), so the lepton labels form 1 + E.
- Hypercharge cannot come from the H-labels. A label-constant charge takes at most 2, 4 or 3 values (for T, T_h, 2T). SM Y takes 6 values on a 16.
- The one traceless label U(1) of (O_h,T) has a cubic anomaly of 32/9 per family.
- Verdict: CHOSEN (the group, the subgroup and the reading). It does not help any wall.

(ii) Delta(27) slab [T] plus [F]. H2 PASSES AS A COUNT; the 3 is CHOSEN.
- Setup: the CL-1 Wilson-type domain-wall slab (m = 0.6, one-copy window, Ls = 12) with hops {e_i - e_j, +-(1,1,1)}.
- H(k+q) = H(k) exactly, with q = (2pi/3)(1,1,1).
- Torus side N = 6: there are exactly 3 light Weyl copies per wall, at k = 0, q, 2q. Equivalently, these are the 3 sublattice classes.
  - The chirality pair (-1,+1) is the same on all three copies.
  - There are no other light states (the next |E| is 0.62).
- Control N = 5: one copy, as w3 predicted.
- The copies carry the 3-dim irrep of Delta(27): the group has order 27, the commutator is omega, and det T = det Omega = 1. So the family operations lie in SU(3), and the tree-level contribution to arg det M is 0, as w3 claimed.
- Adding a class-changing e_i hop to every field:
  - eps = 0.05 detunes the q and 2q copies.
  - eps = 0.3 removes them (wall mass m - 1 - 4.5 eps < -1), leaving 1 copy.
  - So "the one class-changing sector" must be restricted to one sector (for example W) by hand.
- Exact obstruction: no O_h-invariant sublattice of Z^3 has index 3. The allowed indices are n^3, 2n^3 and 4n^3. The x+y+z mod 3 lattice is invariant only under the stabiliser D3d of the (111) axis.
- Consequences:
  - The rule picks one body diagonal, a lopsided choice.
  - The 3 equals the index of the chosen hop sublattice; mod 2 would give 2 and mod n gives n.
  - The copies are decoupled and each keeps its own mirror.
- Wall impact:
  - Count: 3 is natural for this hop set, but not forced.
  - Labels: the tree-level FCNC selection rule follows from Schur, given the hop assignment.
  - CP/theta: det = 1 is genuine and cheap.
  - Mirror wall: no help.

(iii) [[8,3,3]] codes [T]. H3 PASSES. The code is UNIQUE.
- Purity: the LP (Shor-Laflamme plus shadow) gives max(A1 + A2) = 0.375 < 1, so every [[8,3,3]] code is pure.
- Lines of PG(4,2): a pure d = 3 code on 8 qubits is the same thing, up to LC x permutation, as 8 pairwise-skew lines of PG(4,2) whose Pluecker sum is 0, taken modulo GL(5,2).
  - Each qubit gives the line spanned by the syndromes of X_j and Z_j.
  - A local Clifford on a qubit is a change of basis on its line.
- Counting:
  - Exhaustive search finds 192 such sets through a fixed skew pair, which gives 59520 sets in total.
  - One stabiliser has order 168, and 9999360/168 = 59520, so there is exactly one orbit.
  - Hence there is exactly ONE [[8,3,3]] code up to LC x permutation (Gottesman's), with |Aut| = 168.
- Weights: d = 3 is checked exhaustively, and S has weight enumerator 1 + 28y^6 + 3y^8.
- 3-fold turn:
  - A plain permutation symmetry never works: the 56 permutation automorphisms contain no element of order 3.
  - With the frame cycle X->Y->Z, 28 qubit permutations work, giving 1008 cube labellings (confirming w4).
  - No 4-fold turn is a symmetry with any of the 6 uniform frames.
  - On the logical classes the turn has order 3 and a 2-dim fixed space. There are 108 symplectic logical bases in which it is a literal 3-cycle of the logical qubits.
- So "every maximal-k distance-3 cube code carries a C3 family permutation and no C4" is now a rigid finite theorem, because there is only one code.
- Chosen inputs:
  - the record unit = one 8-qubit cell (two cells give 6);
  - distance 3 and maximal k (the Hamming bound gives k <= 0, 3, 10 for n = 4, 8, 16);
  - the frame rotation;
  - "logical qubit = family", which is an identification that has not been derived.
- Wall impact: count 3 vs 6 only if the unit is one cell. It does not help with labels (C3 must be broken) or with CP.

Overall
- None of the three forces 3 from the axioms alone.
- (iii) is the most rigid: a unique code, and the C3-not-C4 structure is a theorem.
- (ii) gives the cheap theta-bar statement (det = 1).
- (i) is numerology.
- Smuggling review:
  - No measured number was used.
  - SM content enters only as the comparison target in (i).
  - Supplied: the Wilson slab, Gottesman's generators, the LP bounds.

Most promising follow-up
- Merge (ii) and (iii). The code's C3 needs a frame rotation, and the Delta(27) rule picks one (111) axis. Test whether the [[8,3,3]] cell code, tiled with its turn axis, produces the x+y+z mod 3 class structure as the stabiliser-preserving hop set. That would force (ii)'s hop choice from (iii)'s code instead of choosing it.
- Separately, ask whether "record unit = one cell" follows from CL-2 (actuality) rather than being supplied.
