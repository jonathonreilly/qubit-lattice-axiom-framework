# c21 criteria (written BEFORE c21_cluster_expansion.py; session 10, 2026-10-27)

Purpose: exact checks for Target A (RTARGET §12): the tree-graph inequality (323) and the Penrose partition used to
prove it; the Mayer/grouping identity and the integration step (Dimock I App. B steps 1-2); the polymer-gas
exponentiation (step 3) against the exact log; and the question whether Thm 27's c_0 can be κ-independent.
These are instances. Uniformity rests on the written proof (PROOF.md, L5 [S10], Theorem CE).

Definitions used by the script.
- For a connected graph g on vertices {0, …, n-1}: ρ^T(g) := Σ_{G ⊆ g, G spanning and connected} (-1)^{|E(G)|}
  (this is Dimock's (317) with ζ - 1 = -1 on overlapping pairs). #T(g) := number of spanning trees of g.
- Penrose rule (root 0). For a spanning tree T of g with depths d_T and parents p_T: an edge {i, j} ∈ g \ T is
  admissible iff d_T(i) = d_T(j), or d_T(j) = d_T(i) + 1 and i > p_T(j) (or the same with i, j swapped). R(T) := the
  admissible edges. For connected G ⊆ g (spanning): T(G) := the BFS tree with parent(j) := the smallest-label
  G-neighbour of j at G-distance d_G(j) - 1 from 0.
- Lattice models: sites of a 2 × 3 grid (each site = one cube); polymers = face-connected site sets; overlap = sharing a
  site.

Part G (graphs).
- G1. For every connected labelled graph on n = 2, 3, 4, 5 vertices, and for K_6 and 300 random connected graphs on 6
  vertices (fixed seed): ρ^T(g) = (-1)^{n-1}·#{T : R(T) = ∅} exactly (integers).
- G2. Same set: |ρ^T(g)| ≤ #T(g).
- G3. ρ^T(K_n) = (-1)^{n-1}(n-1)! for n = 2, …, 6.
- G4. Partition property, for every connected graph with n ≤ 5: for every spanning connected G ⊆ g,
  T(G) ⊆ G ⊆ T(G) ∪ R(T(G)); and for every spanning tree T and every S ⊆ R(T), T(T ∪ S) = T.

Part M (Mayer and integration, steps 1-2). Field φ_x ∈ {-1, 0, 1} with probabilities (0.3, 0.3, 0.4), independent.
H on singletons, nearest-neighbour pairs and the two 2 × 2 squares (15 polymers):
H({x}) = 0.03φ_x + 0.02φ_x², H({x, y}) = 0.03φ_xφ_y + 0.02φ_x²φ_y, H(square) = 0.03φ_1φ_2φ_3φ_4 + 0.01φ_1², with a fixed
site order. f_X := e^{H(X)} - 1.
- K(Y, φ) := the sum, over all collections of distinct polymers that are overlap-connected and have union Y, of Π f
  (Dimock (301)), by direct enumeration of all 2^15 collections.
- M1. For every subset Z of the grid and every φ (3^6 configurations): Π_{X ⊆ Z}(1 + f_X) = Σ_{families of pairwise
  disjoint Y ⊆ Z} Π K(Y), the right side by an independent subset recursion. Max relative error ≤ 1e-12.
- M2. K(Y) = 0 (exactly, as an empty sum) unless Y is face-connected.
- M3. With K#(Y) := E_μ K(Y): Ξ(Z) := E_μ exp(Σ_{X ⊆ Z} H(X)) = Σ_{disjoint families in Z} Π K#(Y), for every Z.
  Max relative error ≤ 1e-12.

Part S (exponentiation, step 3). H#_Möb(Y) := Σ_{Z ⊆ Y} (-1)^{|Y \ Z|} log Ξ(Z) (exact). The truncated cluster series
H#_{≤N}(Y) := Σ_{n=1}^{N} (1/n!) Σ_{(Y_1, …, Y_n) ordered, ∪Y_i = Y} ρ^T(overlap graph) Π K#(Y_i) (ρ^T := 0 if the
overlap graph is disconnected), with Y_i ranging over connected sets.
- S1. |H#_Möb(Y)| ≤ 1e-13 for every Y that is not face-connected.
- S2. err_N := max_Y |H#_{≤N}(Y) - H#_Möb(Y)| satisfies err_{N+1} ≤ 0.5·err_N for N = 1, 2, 3.
- S3. err_4 ≤ 1e-6.

Part I (Ising instance for the κ-dependence of c_0). σ_x = ±1 uniform; H({x, y}) = h σ_xσ_y on nearest-neighbour pairs,
H = 0 otherwise. Y_6 := the 2 × 3 rectangle, Y_4 := a 2 × 2 square. H#(Y) := Σ_{Z ⊆ Y}(-1)^{|Y \ Z|} log Ξ(Z), exact.
- I1. |H#(Y_6)|/h^6 ∈ [0.9, 1.1] for h ∈ {0.01, 0.03, 0.1}.
- I2. |H#(Y_4)|/h^4 ∈ [0.9, 1.1] for the same h.
- I3. |H#(Y)| ≤ 1e-15 for Y = two non-adjacent sites.
Interpretation fixed in advance: a nearest-neighbour pair X has d(X) = 0 (a point of the common face meets both cubes),
so |H(X)| ≤ h e^{-κ d(X)} holds for EVERY κ with H_0 = h, while d(Y_6) ≥ 1 (the outer columns are at distance 1). If
I1 holds, a κ-independent c_0 would give h^6·0.9 ≤ C_1 h e^{-(κ - 3κ_0 - 3)} for all large κ, which is false. So I1 PASS
means: Thm 27 as stated (c_0 depending only on d) is false, and c_0 must depend on κ, as the proof on p.40 says.
I1 FAIL means the question stays open.

Result: PASS iff every criterion holds. Resource rules: one job, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8, ≥ 25%
free memory before start; peak memory and time reported. No criterion is edited after the run.

## Addendum [S11] (2026-10-27, after REVIEW_S9_S10 fix 1; written BEFORE the c21 script edit)
- **Reporting fix for I1/I2 (criteria unchanged).** The ratios are recomputed in 60-digit mpmath arithmetic (exact
  enumeration of the 2^|Z| spin sums, then the Möbius sum) and printed to 4 digits from that computation. The
  double-precision value is reported only through a bound check |r_double - r_mp| ≤ 1e-3, not as raw digits. The
  pass windows [0.9, 1.1] are unchanged.
- **I4 (new, exact).** Six-bond finite difference: switch only the six outer bonds of Y_6 (coupling h each) on or off,
  and form Δ := Σ_{S ⊆ six bonds}(-1)^{6-|S|}log Ξ_S. Criterion: |Δ_mp - log(1 + tanh(h)^6)| ≤ 1e-40 at h = 0.01,
  0.03, 0.1 (60 digits). Informational: |Δ_double - Δ_mp| / Δ_mp, as a bound check (≤ 0.05), not raw digits.
- The original output checks/c21_out.txt is kept unchanged; the re-run writes checks/c21_out_s11.txt.
- **[R1112-fix] Annotation (session 13, 2026-10-27; appended, l.52-53 not edited).** The session-10 reading above,
  "So I1 PASS means: Thm 27 as stated (c_0 depending only on d) is false", is WITHDRAWN per REVIEW_S9_S10 fix 1. I4
  (the exact six-bond finite difference) now carries the argument. The correct reading of I1/I4 PASS: the literal
  statement's quantifier order (c_0 before κ) is corrected to c_0 = c_0(d, κ), as Dimock's own p.40 remark "(So c0
  does depend on κ.)" already does; none of Dimock's results is affected (PROOF.md, Proposition CE-κ).
