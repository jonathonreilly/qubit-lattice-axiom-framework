---
claim_id: five_modes_per_site_are_the_smallest_anomaly_free_protected_spin2n_content_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Suppose N identical complex fermion modes are carried per frame cell, the frame group is the full
  Bogoliubov group Spin(2N) of those modes, and the light content is one fermion-parity half S+ (dimension 2^(N-1)),
  read as 2^(N-1) Weyl species in 3+1 dimensions. Then the smallest N for which S+ has no perturbative anomaly, no
  old SU(2) (Witten) anomaly, no Spin-Z4 (mod-16) anomaly of the centre, and no Spin(2N)-invariant mass is N = 5,
  which gives Spin(10) on the 16. Chirality is not an input: it comes out at the minimum. Every odd N >= 5 also
  passes, so only the 'smallest' selector is well posed. Two loopholes stay open: proper frame subgroups for
  N <= 3, and finite groups for N = 1, 2. With one mode per site, no 5-site cluster tiles Z^3 covariantly, and no
  nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact. Global anomalies beyond the computed indices are
  cited. Supplied model, exact finite group theory, no physical identification established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/five_modes_per_site_are_the_smallest_anomaly_free_protected_spin2n_content_2026_10_22.py
---

# Five modes per site are the smallest anomaly-free, protected Spin(2N) content

Claim type: bounded_theorem. Runner: runner.py (PASS=37, FAIL=0, about 3 s, under 270 MB). It ran through
scripts/runner_cache.execute_runner (status ok, stdout 5862 characters).

## Question

The leading ruleset (minimal-toe-merged) protects a 16 with Spin(10), but it supplies the 16 by putting 5 modes on
each site. Commutant-c showed that N identical modes on the tick carry so(2N). This note asks whether N = 5 is
forced by the ruleset's own selectors: least information (M0/P0, "shortest") together with consistency and
protection (M4/R4, "no anomaly, perturbative or global; nothing light unless protected"). No observed input is
used.

## Setting (supplied)

- N complex modes per cell are built with Jordan-Wigner, giving 2N Majoranas g_a.
- The frame group is Spin(2N), with generators M_ab = (i/2) g_a g_b. The Cartan generators are
  M_{2j,2j+1} = n_j - 1/2.
- The content is S+, the even-occupation half, with weights (+-1/2)^N and an even number of +.
- The 4D reading is that each state of S+ is one left-handed Weyl species. This is the Wilczek-Zee reading of
  Lambda(C^N), used by the merged ruleset; it is not derived here.

## Exact results

1. **S+ and chirality (ABCD1-7, C8-C9).**
   - S+ is irreducible for N = 1..7. The weights are distinct, and the raising graph is connected, so Schur
     applies.
   - Negating a weight flips N signs, so it maps S+ to S- exactly when N is odd. Hence S+ is complex (chiral)
     iff N is odd, and self-conjugate iff N is even.

2. **Perturbative anomalies, general proof (C).**
   - By Weyl conjugacy, the cubic form Tr X^3 vanishes iff its restriction to the Cartan, sum_w (w.t)^3,
     vanishes.
   - Coefficients of w_i^2 w_j and w_i^3 equal (1/4) sum w_j. That sum is zero for N >= 2: flip a coordinate
     other than j, and parity is preserved because it pairs states.
   - Coefficient of w_i w_j w_k with i, j, k distinct:
     - For N >= 4 a fourth coordinate absorbs the parity constraint, so the sum over the signs of i, j, k is
       zero.
     - For N = 3 the parity constraint fixes the product of the signs, which gives the coefficient -4 (runner).
   - So the cubic anomaly is nonzero exactly for N = 1 (abelian) and N = 3 (su(4)). The linear (gravitational)
     form is nonzero only for N = 1.
   - Correction to the brief: Spin(2) = U(1) also has a cubic anomaly. "Cubic Casimir only for N = 3" holds
     only for the nonabelian cases.
   - Checked exactly through N = 9, with random X numerically through N = 7.

3. **Protection (ABCD).**
   - A Majorana mass for a Weyl multiplet needs a *symmetric* invariant bilinear on S+. The runner computes the
     invariant bilinears exactly, using the weight-zero-sum ansatz plus all generators.
   - N odd: there are none (the weights never pair), so the content is protected.
   - N = 0 mod 4: there is a symmetric invariant, so S+ is real and a mass is allowed (N = 4: 8s).
   - N = 2 mod 4: there is an antisymmetric invariant (pseudoreal). One copy is protected.

4. **Old SU(2) anomaly (E2-E7).**
   - The test is the index 2 Tr J3^2 mod 2 over SU(2) subgroups: Spin(4)_L, Spin(4)_R and the vector Spin(3).
   - N = 2: S+ = (2,1), with index 1. This is the Witten anomaly.
   - N = 3: indices 1 and 1. This is the descendant of the cubic anomaly.
   - N >= 4: all even, consistent with pi_4(Spin(n >= 6)) = 0 (cited).

5. **Centre Z4 and mod 16 (F1-F7, F5b).**
   - For N odd, z = exp(i pi (n - N/2)) lies in Spin(2N), acts on S+ as a uniform +-i, and z^2 = -1.
   - The element -1 in Spin(2N) acts as -1 on every S+ field and as +1 on every bilinear. It therefore equals
     (-1)^F, so the natural global structure is Spin x_Z2 Spin(2N), which contains Spin-Z4.
   - The Spin-Z4 anomaly is nu = 2^(N-1) mod 16 (Z16 cited). It is 1, 4, 0, 0 for N = 1, 3, 5, 7.
   - This gives an independent route: 2^(N-1) = 0 mod 16 iff N >= 5. "16 per family" and "5 modes" are the same
     condition.
   - Removing the SU(5)-singlet state (nu^c) leaves nu = 15. So nu^c is required once the Z4 is kept.

6. **Selection (G1, G2).**

   | N | chiral | perturbative | Witten | Z16 | protected | result |
   |---|---|---|---|---|---|---|
   | 1 | yes | fails | - | fails | yes | fail |
   | 2 | no | ok | fails | - | yes | fail |
   | 3 | yes | fails | fails | fails | yes | fail |
   | 4 | no | ok | ok | - | fails | fail |
   | 5 | yes | ok | ok | ok | yes | **PASS** |
   | 6 | no | ok | ok | - | yes | pass (but non-chiral) |
   | 7 | yes | ok | ok | ok | yes | pass |

   - The smallest N passing criteria (ii)-(iv) is 5, *without using (i)*. Chirality is an output at the minimum.
   - All odd N >= 5 pass, by the general proofs in 2, 3 and 5. "Largest" over N therefore has no solution, so only
     P0's "smallest" is well posed, and P0 has to be applied before M3's "largest group", not after.

7. **Subgroup loopholes (H1-H6).**
   - The theorem uses the full Spin(2N). If M3's "as large as M4 permits" lets a proper subgroup serve for small N,
     the following hold.
   - Tori, exact: for 4 Weyl with sum q = 0, sum q^3 = -3(q1+q2)(q1+q3)(q2+q3). Anomaly freedom therefore forces
     the charges to cancel in pairs (vectorlike), so tori fail for N <= 3.
   - N = 3: Sp(4) has a Witten anomaly. SO(4) acting as (2,2) is real, so it is massable.
   - N = 4: every subgroup keeps the real structure, so every subgroup fails.
   - **N = 3, principal SU(2) (the 4 as j = 3/2): this is open.** It has old Witten index 10 (even) and is
     protected (pseudoreal, one copy). It is excluded only by the new SU(2) anomaly of Wang-Wen-Witten (cited),
     under the natural structure where (-1)^F is the centre -1 of the group, which holds here.
   - **Open, not computed:** finite frame groups for N = 1, 2. For example, Q8 inside SU(2) protects the N = 2
     doublet, and its anomaly has not been computed.

## Owner question: building the 5 from several one-mode sites (W1-W7, Z1-Z2)

This section keeps the Qubit axiom (one mode per site).

(1) **Covariant 5-clusters (lattice tilings).**
- Point-group orbits around a site have sizes 1, 6, 8, 12, 24. Around any other centre all orbits are even. So no
  5-site cluster is O_h-symmetric; the smallest odd one with at least 5 sites is the 7-star (Z1).
- Over all 14950 five-site clusters in a 3^3 box, the most symmetric is site + 4 alternate body diagonals (a
  tetrahedron, T_d, 24/48). Its best lattice tiling keeps only 4/48.
- The plus (site + 4 in-plane neighbours, 16/48) tiles with at most 8/48.
- site + 3 forward + diagonal (6/48), and the cube 5-of-8 with the 3 around a corner removed (6/48), do not
  lattice-tile at all.
- The best 5-site tiling keeps 8/48: lopsided by 2.6 bits.
- The 7-star (48/48) tiles through perfect Lee codes, but each such tiling keeps at most 6/48.
- Fully O_h-covariant tiling blocks up to size 30 have sizes 8, 16, 27. Sizes 8 and 16 have N = 0 mod 4, so they
  are real and fail. **The smallest fully covariant passing block is 27** (the 3^3 cube, Spin(54)). That result
  is not a sensible world.

(2) **Existing structure.**
- The cube tick's blocks are 8 sites, which fail (real 128).
- The 2+3 count, counted consistently at one mode per site (site + 3 forward links), is N = 4, which is real and
  fails protection.
- Adding "one more" site has stabiliser 6/48 and does not tile.
- So no structure the laws already have produces 5 without a choice.

(3) **Does spreading the modes break the argument?**
- The anomaly, chirality and protection results are statements about the representation, so they survive
  unchanged. Inter-cluster masses S+ x S+ have no invariant, but S+ x S- has one (W7). Protection therefore needs
  the same parity half on every cluster, which is a uniformity rule.
- What breaks is exactness of the frame group:
  - By Schur, the only Spin(2N)-invariant coupling between two clusters' Majorana vectors is the identity (W5).
    The hop must therefore be mode-diagonal, with displacement in the tiling lattice L.
  - Nearest-neighbour hops on all three axes need e1, e2, e3 in L, which means L = Z^3 and N = 1.
  - A gauge-covariant hop would need K(5,5) of nearest-neighbour bonds, which is impossible (W6). Two sites share
    at most 2 neighbours.
  - So Spin(10) on a spread cluster can be at most emergent. Protection by an approximate symmetry is the tuned
    smallness that M4 forbids.
- **Answer:** 5 cannot be built from one-mode sites without smuggling. It is an intrinsic per-site multiplicity
  (bends the Qubit axiom), unless a coarse-rung rule makes a cluster the "site" and redefines "neighbour" at that
  rung. That rule would still have to pick a lopsided 5-tiling (at best 8/48) with no reason.
- The symmetric zoom alternative is the 7-star: Spin(14) on 64 = (16,(2,1)) + (16bar,(1,2)) under
  Spin(10) x Spin(4) (Z2). It is chiral under Spin(14) but carries mirror 16bars, and its tiling is lopsided too.

## Verdict

- **Conditionally YES.** Under the full-frame-group reading, least information + M4 force N = 5, and with it the
  16, Spin(10), nu^c and chirality. No measured number and no group name is used.
- The derivation has three conditions:
  - (a) the frame group is the full Spin(2N);
  - (b) the content is one parity half, read as Weyl species;
  - (c) the cited global anomalies, including the WWW new SU(2) anomaly, which is needed to close N = 3 if
    subgroups are allowed.
- Finite frame groups at N = 1, 2 are an open loophole.
- The 5 does not come from site clusters without a lopsided choice. As a per-site multiplicity it bends the Qubit
  axiom.

## Gate

1. Numbers chosen: none.
2. Observed structure by name: none. Spin(10), the 16 and nu^c are outputs. The Weyl-species reading (b) is an
   inserted identification, borderline, the same one the merged ruleset already makes.
3. Predictions it was not built for:
   - "largest" is ill-posed over N;
   - nu^c is forced by mod 16;
   - no Spin(14)-type family unification inside a cell, so families must replicate outside the site modes;
   - the j = 3/2 loophole.
   None is tested against measurement here.
4. Axiom bent: Qubit (5 fermion modes per site). The one-mode cluster route fails.

## Cited, not rederived

- pi_4 of Spin(n);
- Witten 1982;
- Wang-Wen-Witten 2018 (new SU(2) anomaly);
- Z16 for Spin-Z4 (Garcia-Etxebarria-Montero; Tachikawa-Yonekura);
- Wang-Wen 2018 (the Spin(10) 16 is free of all anomalies);
- Golomb-Welch (perfect Lee codes).

## Used / narrowed

- Used: commutant-c E1 (N identical modes give so(2N)).
- Narrows minimal-toe row 13: the "16 from Z16" step there becomes "N = 5 from Z16 + cubic + Witten + protection".
- Narrows minimal-toe-b-tests: it confirms that IM prefers Spin(10), and adds that the 5 is selected rather than
  supplied, but only per site.
- Related, not contradicted: main SPIN10_SYMMETRIC_ATOMIC_GAPS... (2026-09-14), which supplies the 16.
- Search limits: lattice tilings only; clusters within a 3^3 box; covariant blocks with index <= 30 and orbit
  radius^2 <= 9.
