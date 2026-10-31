# c33 criteria (written BEFORE checks/c33_bfour.py; session 18, 2026-10-27, after RLARGE.md §13 and before the §7 repair text)

Purpose: a toy instance of the B_4 step of RLARGE Theorem R1 (iii), the subject of REVIEW_S16_S17 fix R-3b. It tests
(a) that the repaired localisation (each connected tuple of clusters assigned, with weight 1/|S|, to the base points of its
UNFATTENED support S = ∪Y_i) gives a base-point functional F^tup_x that is exactly invariant under the point group about x;
(b) that the session-17 localisation (assignment to x ∈ ∪Ŷ_i, Ŷ = Y + {0,1}^d, weight 1/|∪Ŷ_i|) gives a functional F^fat_x
that is NOT invariant for generic data; (c) that both sum to the same graded logarithm, which equals the brute-force
log Ξ; (d) that on translation-invariant data the two agree (so the value of the extracted coupling shift is unchanged
and only the written proof step was wrong). Not a proof. Two parts, each its own job (`python3 c33_bfour.py A|B`), one job
at a time, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, no `timeout`. No float tolerance beyond those written here; any
needed later goes into an addendum to THIS file before the run that uses it.

## Common definitions
- Cubes = sites of the torus (Z/T)^d. *-adjacency: x ≠ x', x - x' ∈ {-1, 0, 1}^d (mod T). A cluster Y is a nonempty
  *-connected set. ∂Y := the cubes at *-distance 1 from Y, not in Y. e(Y) := the number of nearest-neighbour (face) pairs
  inside Y.
- Data: a real field D on cubes. Activities r_Y(D) := (1 + 0.2·e(Y))·exp(Σ_{y∈Y}D(y) + 0.5·Σ_{z∈∂Y}D(z)²) (graded by
  |Y|; the grading variable t is kept as the exponent N = Σ|Y_i|). r is covariant under every lattice isometry R:
  r_{RY}(R·D) = r_Y(D), (R·D)(z) := D(R^{-1}z).
- Gas: Ξ(D) = Σ_B Π_{*-components Y of B} r_Y(D) t^{|B|}; c_N := the t^N coefficient of log Ξ (exact power-series log).
- Tuples τ = (Y_1, …, Y_n), n ≥ 1, touching graph G(τ): edge {i, j} iff Y_i ∪ Y_j has two cubes at *-distance ≤ 1 or
  Y_i ∩ Y_j ≠ ∅. φ^T(G) := Σ over connected spanning subgraphs H of G of (-1)^{|E(H)|} (n = 1: 1; n = 2: -1 if the edge is
  present; n = 3: path 1, triangle 2, disconnected 0). Term(τ) := φ^T(G(τ))Π_ir_{Y_i}/n!, N(τ) := Σ|Y_i|,
  S(τ) := ∪Y_i, X(τ) := ∪(Y_i + {0,1}^d).
- F^tup_x := Σ_{τ: x∈S(τ), N(τ)≤N_max} Term(τ)/|S(τ)|; F^fat_x := Σ_{τ: x∈X(τ), N(τ)≤N_max} Term(τ)/|X(τ)| (both per order N).
- Point group about x: all signed permutations R of the d axes acting as z ↦ x + R(z - x) (8 in d = 2, 384 in d = 4).

## Part A: d = 2, T = 9, N_max = 3, all tuples on the torus
Data: D = 0.3·ξ, ξ iid N(0,1), seeds 0-4; plus the constant field D ≡ 0.2 (seed "const").
- **A1 (tuple identity):** for each seed and each N ≤ 3, |Σ_{τ: N(τ)=N}Term(τ) - c_N| ≤ 1e-10·max(1, |c_N|), with c_N from the
  brute-force enumeration of all B with |B| ≤ 3.
- **A2 (repaired localisation invariant):** for each seed, each N ≤ 3, x = (4, 4) and all 8 R:
  |F^tup_x(R·D) - F^tup_x(D)| ≤ 1e-12·max(1, |F^tup_x(D)|).
- **A3 (fattened localisation not invariant):** for each random seed (0-4), some N ≤ 3 and some R has
  |F^fat_x(R·D) - F^fat_x(D)| > 1e-6·max(1, |F^fat_x(D)|).
- **A4 (same total):** for each seed and N ≤ 3, |Σ_xF^tup_x - Σ_xF^fat_x| and |Σ_xF^tup_x - c_N| ≤ 1e-10·max(1, |c_N|).
- **A5 (translation-invariant data):** for D ≡ 0.2 and every N ≤ 3: |F^tup_x - F^fat_x| ≤ 1e-12·max(1, |F^tup_x|), and both
  equal c_N/T² to the same tolerance.
- **PASS iff A1-A5.**

## Part B: d = 4, T = 7, N_max = 2, tuples meeting a neighbourhood of x only
Data: D = 0.3·ξ, seeds 0-2, and D ≡ 0.2. Only tuples with x ∈ S(τ) or x ∈ X(τ) are enumerated (n = 1: |Y| ≤ 2; n = 2:
two single cubes, equal or *-adjacent).
- **B1:** for each random seed, each N ≤ 2 and all 384 R: |F^tup_x(R·D) - F^tup_x(D)| ≤ 1e-12·max(1, |F^tup_x(D)|).
- **B2:** for each random seed, some N ≤ 2 and some R give |F^fat_x(R·D) - F^fat_x(D)| > 1e-6·max(1, |F^fat_x(D)|).
- **B3 (the review's explicit case):** with Y = {x - e_1}, Y' = {x + e_1} (the reflection of Y through x): x ∈ Y + {0,1}^4
  and x ∉ Y' + {0,1}^4.
- **B4 (translation-invariant data):** for D ≡ 0.2 and N ≤ 2: |F^tup_x - F^fat_x| ≤ 1e-12·max(1, |F^tup_x|).
- **PASS iff B1-B4.**
