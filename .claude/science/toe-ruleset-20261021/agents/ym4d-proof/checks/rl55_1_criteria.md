# rl55_1 criteria (written 2026-10-29T04:36Z, before rl55_1.py exists)

Purpose: decide, exactly, the boundary convention of RLOC55's soft-density patch in d = 4: that every link of every S4'
contour word of a level-(l+1) coarse link c lies (both endpoints) in the explicit box Box(c), that Box(c) is exactly the
bounding box (no slack, no shortfall), that the oscillation paths used for delta stay in Box(c) with the stated l1 length,
and to compute (report, exact) the incidence constants that enter RLOC55's constant K_1.

Model (exactly the words of BFT_A §3.4 / PROOF.md "Decision 4" / hg55_1): level-l lattice Z^4 (the local cover; RLOC55
shows separately that T >= 3 gives level-l torus side >= 3L > 2L, so no identification inside Box(c)). Coarse link
c = (X = 0, mu); root c_X = (o,o,o,o), o = (L-1)/2; c_Y = c_X + L e_mu. For every axis order (24 permutations) and every
y in c_X + {-o..o}^4: word = axial path c_X -> y moving coordinates in that order; then L steps +mu from y to y + L e_mu;
then the axial path c_Y -> y + L e_mu (same order) traversed in reverse. A step between z and z + e_nu is the link
(base point min(z, z+e_nu), direction nu). L in {3, 5}.
Box(c) := { z : 0 <= z_nu <= L-1 (nu != mu), 0 <= z_mu <= 2L-1 }  ( = c_X + [-o,o]^4 extended by L in direction +mu ).
Integer arithmetic only (Fractions for frequencies). No floats.

Pre-registered gates (all four mu, both L):
- P1 (containment): every vertex of every word lies in Box(c). PASS iff no exception.
- P2 (tightness): the coordinatewise min/max of all word vertices equal Box(c)'s faces exactly. PASS iff equal.
- P3 (oscillation path length): for each direction nu, D_nu := max l1 distance between base points of two nu-links used
  by the words; PASS iff max_nu D_nu <= 5L - 4 (BA-6's diameter bound, RLOC55's delta bound). D_nu reported exactly.
  Also: every monotone lattice path between two such base points, shifted to nu-links, has both endpoints of every
  intermediate link in Box(c): checked by testing that the coordinatewise-rectangle spanned by any two used nu-link base
  points b, b' satisfies rect + {0, e_nu} inside Box(c) (equivalent, since rectangles are monotone-path hulls).
  PASS iff true for all pairs (checked via the per-direction bounding rectangle of used base points).
- P4 (linearisation sanity): average over words of the signed count of nu-letters equals L*[nu == mu] exactly
  (Q maps direction-constant fields to L*xbar_mu). PASS iff exact for all nu, mu.
- P5 (incidence, exact, reported; gate = internal consistency): for a level-l link b, n_c(b) := #{coarse links c'
  (all X' in Z^4, all mu') : b is used by a word of c'}; n_box(b) := #{c' : both endpoints of b in Box(c')};
  cfreq(b) := sum over c' of (average over words of c' of the number of occurrences of b). Report max over b of each
  (b ranging over all links with base point in one fundamental cell {0..L-1}^4, all 4 directions). PASS iff
  n_c <= n_box for every b (support incidence is dominated by patch incidence) and cfreq values are exact Fractions.
Negative controls (each MUST fire, i.e. make its gate fail; if one does not fire the check is NON-DISCRIMINATING and the
overall result is FAIL, no verdict):
- K1: uncentred y-range y in c_X + {0..L-1}^4 (lower-corner block): P1 must FAIL for some mu.
- K2: Box with its +mu face lowered by one (z_mu <= 2L-2): P1 must FAIL for some mu.
- K3: P3 threshold replaced by 5L - 6: P3 must FAIL (shows the reported D_nu is attained near the bound, not vacuous).
Overall: PASS iff P1-P5 PASS for both L and K1, K2, K3 all FIRE.

What this check cannot decide: anything analytic (sizes, holomorphy, Cauchy), k- or T-uniformity (it is one local cover,
which is the point: the patch is k-independent in own level-l steps), or the Wilson-pair / Campanato patches (those are
handled analytically in RLOC55). It decides the explicit boundary convention for the soft patch and the counting constants.
