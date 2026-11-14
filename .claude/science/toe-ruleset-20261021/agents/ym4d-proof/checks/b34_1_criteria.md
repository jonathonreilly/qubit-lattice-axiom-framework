# b34_1 — criteria (written 2026-10-29, BEFORE the script b34_1_tree.py exists)

Owner: BFT34_55.md (claude-opus-5-5). Exact rational arithmetic (fractions.Fraction), plain python, no floats in any
verdict, no numpy.

## What is tested
The derivative formulas BFT34_55 §1.4 displays for the implicit critical point and for the critical value, orders n <= 4
(U-part) and n <= 5 (E-part), in the abstract finite-dimensional setting:
- (TREE-U) G(Z(V), V) = 0, A := D_Z G(0,0) invertible, Gm := -A^{-1}. For an index list (a_1..a_n),
  d^n Z / dV_{a_1}..dV_{a_n} (0) = Gm * SUM over pairs (P, W), W a subset of positions, P a set partition of the remaining
  positions, (P, W) != ({all}, {}), of D_Z^{|P|} D_V^{|W|} G(0,0)[ (d^{|B|}Z / dV_B)_{B in P} ; (e_{a_i})_{i in W} ].
- (TREE-E) E(V) := F(Z(V), V) with G := grad_Z F and Z(V) the critical point:
  d^n E / dV_{a_1}..dV_{a_n} (0) = SUM over pairs (P, W) built on positions 2..n (no exclusion) of
  D_Z^{|P|} D_V^{|W|} (d F / dV_{a_1})(0,0)[ (d^{|B|}Z/dV_B)_{B in P} ; (e_{a_i})_{i in W} ].
- Counts: the number of (P, W) pairs in (TREE-U) is B(n+1) - 1 = 1, 4, 14, 51 for n = 1..4 (B = Bell numbers); in
  (TREE-E) it is B(n) = 1, 2, 5, 15, 52 for n = 1..5. The fully expanded (recursively substituted) tree counts T(n) are
  reported, informational only.

## Ground truth (independent of the formulas)
Z(V) as a truncated multivariate power series to total degree 4 (U-part) / 5 (for E: Z to degree 4 suffices for
E to degree 5 because D_Z F = 0 at the critical point — NOT assumed: Z is computed to degree 5 when testing E to degree
5), obtained by exact fixed-point iteration Z <- -A^{-1}(B V + H(Z, V)) in truncated polynomial arithmetic, iterated
until the truncated series is stationary. E(V) := F(Z(V), V) truncated. Derivatives at 0 = alpha! * coefficient.

## Instances
p = dim Z = 2, q = dim V = 2. Three seeds. G (U-part): random integer coefficients in [-3, 3] for every monomial of total
degree 2..4 in (Z, V), linear part A Z + B V with A having nonzero determinant. F (E-part): F = 1/2 Z^T A_s Z + Z^T B V +
random cubic/quartic/quintic monomials (integer coefficients in [-2, 2]), A_s symmetric with nonzero determinant;
G := grad_Z F computed symbolically from F.

## PASS / FAIL (pre-registered)
- P1: (TREE-U) equals ground truth EXACTLY for every index tuple in {1,2}^n, n = 1..4, every seed.
- P2: (TREE-E) equals ground truth EXACTLY for every index tuple in {1,2}^n, n = 1..5, every seed.
- P3: the (P, W) counts equal 1, 4, 14, 51 (U) and 1, 2, 5, 15, 52 (E).
- Controls — each must FIRE (produce at least one exact mismatch somewhere in n <= 4), otherwise the check is declared
  NON-DECISIVE (a FAIL of the check design, reported as such):
  - K1: drop every root-level pair with |P| >= 2 (the nonlinear Z-vertices) in (TREE-U).
  - K2: replace set partitions by ordered set partitions (each partition counted |P|! times) in (TREE-U).
  - K3: drop every pair with |P| >= 1 and |W| >= 1 (mixed vertices) in (TREE-U).
  - K4: drop the root-level W != {} pairs in (TREE-E).
Overall PASS iff P1, P2, P3 hold and K1-K4 all fire.

## What this check cannot decide
It verifies the algebraic identities (multivariate Faa di Bruno for an implicit function and an envelope value) and
their term counts. It says nothing about locality, decay rates, norms, k-uniformity, or any lattice-gauge input.
