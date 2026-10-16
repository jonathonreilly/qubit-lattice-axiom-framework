---
claim_id: cubic_cell_shape_sets_the_taste_content_axis_permutation_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "Cells formed by an orbit of the proper cubic group around a centre (6 face centres, 8 corners, 12 edge midpoints), one amplitude per point, with the binary octahedral group acting by monomial matrices (signs or phases). Exact (characters): every spinorial such representation contains only E1/2, E5/2 and H = E (x) E1/2, so it equals E1/2 (x) F with F a representation of S3, the permutation group of the three axes. The copy ('taste') content is F = A1 + E or A2 + E for face centres (the axis triplet, no repeated summand), 2E for signed corners, A1 + A2 + E for phased corners, and A1 + A2 + 2E for edges (phased only). Under the threefold axis cycle C3, A1 and A2 carry 1 and E carries omega + omega-bar. Exact: wherever F contains F' + F', the two-qubit Dirac walk tensored with 1_F' is a moving covariant tick with dim F' Dirac copies. Numerical: the pair E1/2 + E5/2 admits moving unitary walks, but those found are massive, and with U(0) = 1 imposed the solution found is degenerate (zero quasienergy along axis lines); no clean massless singlet copy was found. Algebraic evidence (cell walks, U(0) = 1): of the nine line branches that pass a numerical linear prefilter, the eight that move along an axis give the unit ideal (Groebner basis mod 32003, and over Q by Singular's multi-prime modStd), and only the axis-flat branch has solutions (a 4-dimensional component), so such a walk is constant along the axes and carries no Dirac cone there. The six-neighbour coin E1/2 + H showed no moving walk (residuals rise steeply with the motion bound, a high-order valley). This is not a derivation of three generations."
upstream_dependencies:
  - staggered_one_qubit_blocks_carry_a_cubic_covariant_dirac_tick_bounded_theorem_note_2026-10-16
  - two_qubit_site_unfreezes_the_cubic_tick_doubler_free_dirac_walk_bounded_theorem_note_2026-10-16
runner: scripts/cubic_cell_taste_content_axis_permutation_2026_10_16.py
---

# Cubic cell shape sets the taste content, and the tastes are labelled by axis permutations

**Date:** 2026-10-16
**Type:** bounded_theorem
**Status:** bounded-support. The representation theory is exact and the
walk statements are labelled; unaudited. Nothing is adopted. This note does
not derive the number of generations.

## Question

If an electron is a pattern on a neighbourhood of one-amplitude points, as in
the staggered-block note, how many copies of it does a neighbourhood carry,
and how does the cubic symmetry label those copies? The motivating
hypothesis is that three generations might be the three spatial axes.

## Result up front

1. **Every spinorial cell is spin-1/2 times an axis-permutation
   representation (exact).** For any cell formed by an orbit of the cube's
   rotations, with signs or phases on the points, the spinorial part
   decomposes as

       E1/2 (x) F,   F = m1 A1 + m5 A2 + m3 E,

   where A1, A2 and E are the irreps of S3 = O / V4. S3 is the permutation
   group of the three axes, and V4 is the group of axis half-turns. Within this supplied spinorial representation the factor F records the
   axis permutations; an electron identification is a separate premise.
2. **Cell shape sets the copies (exact, characters):**

   | cell | signs or phases | spinorial content | taste F |
   |---|---|---|---|
   | 6 face centres (a site's six neighbours) | phases | E1/2 + H, or E5/2 + H | A1 + E or A2 + E: the axis triplet, no repeat |
   | 8 corners (2x2x2 block) | signs | 2H | 2E |
   | 8 corners | other odd phases (q = 1,5) | E1/2 + E5/2 + H | A1 + A2 + E |
   | 12 edges (the links of a cube) | phases only | E1/2 + E5/2 + 2H | A1 + A2 + 2E |

3. **Moving Dirac copies (exact construction).** If F contains F' + F', the
   two-qubit Dirac walk U_2q (x) 1_F' is a moving covariant tick carrying
   dim F' Dirac copies. The repeated summand plays the role of handedness,
   and the remaining F' labels the copies. Signed corners give two copies
   (F' = E), as in the companion note. Edges also give F' = E, two copies,
   and leave an extra pair A1 + A2.
4. **The extra pair (numerical).** The coin E1/2 + E5/2, a spin-1/2 doublet
   whose second member is twisted by the sign character, does admit moving,
   dispersive unitary walks: band spread up to 5.6 rad, unitarity and
   covariance about 1e-15. All found are massive at k = 0. With U(0) = 1
   imposed, the one solution found is degenerate: zero quasienergy along the
   axis lines and a doubler at X. No clean massless Dirac copy from this pair
   was found.
   **Algebraic evidence (mod p, labelled).** The line lemma reduces the
   U(0) = 1 cell walks to branches: along the x axis,
   U(t e_x) = sum_k z^(m_k) P_k on the four J_x eigenlines (eigenvalues
   distinct), with m_k in {-1, 0, 1}, plus monomials on the body diagonal.
   Nine branches pass a numerical linear-consistency prefilter, each with
   32 free unknowns and 336 real unitarity equations. The results:
   - The eight branches with nonzero axis exponents give the unit ideal.
     A Groebner basis mod 32003 (slimgb) is {1}, and Singular's multi-prime
     modular method over Q (modStd) also returns {1}. For a unit result,
     modStd does not itself certify 1 in I; an explicit lift (a cofactor
     certificate) would.
   - Only the axis-flat branch (0, 0, 0, 0) has solutions: a component of
     Krull dimension 4, both mod p and over Q.
   So every such walk is constant along the axes (zero quasienergy on the
   axis lines). This matches the degenerate numerical solution, and rules
   out a Dirac cone of the singlet pair at k = 0 along the axes. This is
   mod-p evidence plus a numerical branch prefilter, not a theorem; the
   inputs and outputs are in
   `.claude/science/physics-loops/toe-campaign-20261015/generations/twisted_branches/`.
5. **Under the threefold axis cycle C3.** A1 and A2 carry the character 1, and
   E carries omega + omega-bar.
   - The twelve-link cell therefore carries copies with C3 labels
     {1, 1, omega, omega-bar} plus a repeat of the E pair.
   - The two E copies inherit the constructed massless cone; absence of
     additional band touching has only the companion's finite-grid support.
   - The singlet pair gave only massive or degenerate walks in the searches,
     and with U(0) = 1 the branch ideals leave only walks that are flat
     along the axes (algebraic evidence, item 4).

## How this bears on generations (interpretation, not a claim)

- The repository's generation program uses the threefold axis cycle C3: the
  generations are the C3 characters 1, omega and omega-bar, through the
  circulant (Brannen) form.
- Under the supplied spinorial cell representation, the C3 labels follow
  from its decomposition. Identifying such a walk with an electron remains
  a separate physical premise.
  The full axis triplet A1 + E restricts to 1 + omega + omega-bar.
- What the results do not show:
  - No cell gives exactly three clean, light, doubler-free Dirac copies with
    the triplet labels.
  - The six-neighbour cell has the triplet but no repeated summand, so the
    U_2q mechanism does not apply. Searches with the coin E1/2 + H found no
    moving walk (numerical). The best residuals rise steeply with the lower
    bound on motion:

    | motion bound | 0.02 | 0.05 | 0.2 | 0.4 |
    |---|---|---|---|---|
    | best residual | 2e-10 | 4e-10 | 7.9e-5 | 1.3e-3 |

    This is a flat, high-order valley at the constant walk. A family of
    moving walks would reach machine zero, as the two-qubit family does.
    So the triplet cell most likely does not move by itself (not proved).
  - The twelve-link cell has the right C3 labels, but its singlet looks
    massive or degenerate. This could be read as "one heavy plus two light",
    but nothing here fixes masses or rules out other cells.

## Premises

- **Axioms used.** The Lattice axiom (Z^3, proper cubic rotations) and the
  full Qubit axiom supplies M_2(C). The one-amplitude-per-point
  walk space is separately supplied, not an equivalent axiom presentation.
- **Declared objects, not framework content.** The cell, the action about
  its centre, and the signs or phases (a background flux, in effect).

## Proof sketch of 1–2

The action on each of these three orbits is induced from a character of
its cyclic stabilizer preimage C_(2m): m = 4 for faces, 3 for corners, 2
for edges. Spinorial characters have odd q modulo 2m. By Frobenius
reciprocity, count q among the restricted weights of E1/2 (-1,1), H
(-3,-1,1,3), and E5/2 (the E1/2 weights shifted by m when the rotation
permutes axes oddly, otherwise unchanged). This gives the table by integer
arithmetic, independently of floating character rounding. For corners q=3
is the unique real odd character and gives 2H; q=1,5 give E1/2+E5/2+H.
For faces q=1,7 give E1/2+H, q=3,5 give E5/2+H. Both odd edge characters
give E1/2+E5/2+2H. The real character q=m is spinorial only when m is odd,
so faces and edges require phases.

The three spinorial irreps have dimensions 2,2,4; together with the five
ordinary cubic irreps (1,1,2,3,3), their squared dimensions sum to 48.
Their character identities H=E(x)E1/2 and E5/2=A2(x)E1/2 give the factor
F, whose factors A1,A2,E descend to S3=O/V4. The runner checks the integer
multiplicities exactly; its numerical group-character computations are
corroboration, not an exact certificate. The table covers these three orbit
types, not every orbit of a generic point about the cube centre. ∎

## Relation to prior work

- S3 flavor models with a 1 + 2 split are standard in model building
  (e.g. Pakvasa–Sugawara 1978).
- Staggered-fermion taste counting is standard: 2^(d/2) tastes in d
  Euclidean dimensions, and 2 per eight-site cube in the 3+1 Hamiltonian
  form.
- In this repository, `STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23`
  shows the hw=1 triplet of the standard staggered lattice carries an
  unbroken S3: the eta-convention asymmetry is gauge. The generation lane
  builds on that triplet.
  `EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03`
  finds N_f = 2 identical tastes on the cube with no generation label. The
  table here is consistent with both: signed corners give 2E, two tastes.
- New here: the classification of the taste content of the three listed cubic-orbit
  cells. It shows the taste index is always an axis-permutation
  representation, with the table above. This is a statement about copy
  spaces and is separate from the hw=1 momentum-space triplet of the
  generation lane. The two-qubit note's light-speed corollary is where the
  hw=1 triplet appears in the one-tick setting.

## No-Go Discipline Gate

No impossibility claim is made. The singlet-pair statements are numerical
or mod-p evidence and are labelled as such. Promoting item 4 to a no-go
would need the branch prefilter done exactly and cofactor certificates
for the eight unit ideals, then the N1-N8 gate.

## Verification

```bash
python3 scripts/cubic_cell_taste_content_axis_permutation_2026_10_16.py
```

Expected: `TOTAL: PASS=10 FAIL=0` (seconds). The twisted-pair walk searches
are in `.claude/science/physics-loops/toe-campaign-20261015/generations/`.

## Load-bearing sources

- [Required parent](TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md)
- [Required parent](STAGGERED_ONE_QUBIT_BLOCKS_CARRY_A_CUBIC_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-16.md)
- [Review scope](../.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md)
