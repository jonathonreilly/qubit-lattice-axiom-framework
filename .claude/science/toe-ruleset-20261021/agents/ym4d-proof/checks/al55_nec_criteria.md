# al55_nec — criteria (written before the script; ALIGN55.md §3)

Purpose: exact (rational) verification of the identities behind Lemma DW, Lemma LC and Proposition NEC on a small model, with controls
that must fire. Python, fractions/ints only, no floats, no BLAS; run with `python3 -I -B`; writes stdout only.

## Model
d = 2, L = 3, k = 2, T = 2: level-0 torus side 18 (324 sites, 648 links), level-1 sites = coordinates ≡ 1 (mod 3) (6×6), level-2 roots =
coordinates ≡ 4 (mod 9) (2×2; each is a level-1 site). Gauge algebra su(2) ≅ R³ with the Euclidean (Ad-invariant) pairing; Ad by rational
SO(3) matrices from rational quaternions. Linearised S4′ root map Q_0 (level 0 → 1) built from its contour definition (order average over
the 2 coordinate orders, block average over the 9 sites of B(X), straight leg of 3 steps). Line current: the level-1 line in direction 1
through y_0 = (4, 1) (a level-1 site, not a level-2 root).
Backgrounds: PG = pure gauge 1^G with random rational G at every level-0 site (Z_l(b) = G(tail)G(head)^{−1}); CV = random rational
rotations on the level-1 links (curved), used only for control C1.
Left inverses: Λ_A = level-0 forest gauge (BFS forest of the level-0 torus rooted at the level-2 roots, coordinate-1-first neighbour
order); Λ_B = the same with coordinate-2-first order (a second level-0-only left inverse); Λ_H = hierarchical: level-1 values from x_1 by a
level-1 forest rooted at the level-2 roots, level-0 values inside each level-1 block from x_0 by a block tree rooted at the block centre.

## PASS criteria (all exact equalities)
- A1 (Lemma LC): at PG with random v, every covariant site charge of the line current is 0, and |j(b_i)|² = |v|² for all i.
- A2: the flat charges computed as the adjoint d^Tj equal (1 − Ad^{−1}_{Z(b_{i−1})})j(b_{i−1}) at every line site; q(y_0) ≠ 0.
- A3: Λ_•Ξ_1ν = −ν for • ∈ {A, B, H} and 3 random ν ∈ Λ_0.
- A4: Λ_Ax^φ = −φ and Λ_Bx^φ = −φ (computed by the actual forest sums), φ = v′δ_{y_0}.
- A5: (Π_•^TS)(x^φ) := S(x^φ + Ξ_1Λ_•x^φ) equals −⟨q(y_0), v′⟩ for • ∈ {A, B}, and is nonzero.
- A6: (Π_H^TS)(x^φ) = 0 (the hierarchical left inverse does not move the level-0 datum to level-1 sites).
- A7 (Lemma DW): Q_0dφ = d ev^{(1)}φ exactly (via the contour definition), and for 5 random flat representations (G_0, G_1, j_0, j_1, s_0, s_1)
  the full pairing y(x^φ) = Σ_l[⟨G_l, dx^φ_l⟩ + ⟨j_l, x^φ_l⟩ + ⟨s_l, r_l(x^φ)⟩] equals ⟨j_0, dφ⟩ + ⟨s_0, d ev^{(1)}φ⟩ exactly (the inequality of
  Lemma DW is then Cauchy–Schwarz over the 2d + 2d links at y_0).
- A8 (hierarchy of Λ_H): changing x_0 at random leaves ev^{(1)}Λ_Hx unchanged; changing x_1 changes it.

## Controls (each must FIRE, i.e. the tested property must FAIL)
- C1: at CV, the line current built with a random v (not in the centraliser of the line holonomy) has a nonzero covariant charge at y_1.
- C2: 2Λ_A is not a left inverse (2Λ_AΞ_1ν ≠ −ν).
- C3: Λ_A is not hierarchical: ev^{(1)}Λ_Ax^φ ≠ 0 (it equals −φ at y_0).
- C4: with y_0 replaced by a level-2 root, Λ_Ax^φ ≠ −φ (pinning: φ ∉ Λ_0).
- C5: dropping the s_0 term from A7's two-term formula gives a mismatch for at least one random representation.

## What this check cannot decide
Uniformity in k, T (no asymptotics are sampled); the d = 4 constants (the identities are dimension-free, the factor 2d is not tested);
anything about S_E's boxes (Λ_A, Λ_B are other level-0-only left inverses — Proposition NEC's level-0-only clause covers S_E by its
definition, not by this script); anything about backgrounds that are critical points (PG is a pure gauge; CV is not critical).
