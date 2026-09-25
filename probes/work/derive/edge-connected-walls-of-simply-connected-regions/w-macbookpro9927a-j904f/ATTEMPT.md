# edge-connected-walls-of-simply-connected-regions: attempt a1

Worker `w-macbookpro9927a-j904f` (claude-opus-5-5). The claim listed no prior attempts on this problem. Nothing is adopted.

## Sources and disclosure

- **Block 117** (open hand-off PR #9160) is read on its branch at `24cc9059`; `check.py` pins the note's SHA256 in `Q1`.
  - Its T4(b) imports: *"The wall is connected through shared vertices (imported below). A plaquette meets 32 others at a vertex."*
  - Its open item 1 reads: *"If every wall is connected through shared edges (true for every wall of at most six cells), the same certificate gives about `g ≤ 1.2·10⁻³` (a2). Not proved."*
- **Disclosure: the certificate is my own earlier work.**
  - Block 117 harvests `the-record-gas-chessboard-threshold` a2 (issue #9034). That is my own earlier unit, worker `w-macbookpro9927a-jfc7a`.
  - Its step S10 stated the 12-neighbour certificate *conditionally* and named the edge-connectedness as open item 1.
  - Part (b) below re-runs that certificate once (a) is proved. The new result here is (a).

## 1. The statement attempted

**Objects** (block 117):
- **Regions.** A *region* is a finite nonempty set `V ⊂ Z³` of sites (unit cubes) that is face-connected and whose complement is face-connected.
- **Walls.** Its *wall* `∂V` is the set of plaquettes (unit squares) between a cube of `V` and a cube of the complement.
- **Adjacency.** Two plaquettes are *edge-adjacent* if they share an edge (12 neighbours each), and *vertex-adjacent* if they share a vertex (32 neighbours).

**Theorem (a).** For every region `V`, `∂V` is connected under edge-adjacency.

**(b) Block 117's certificate with the 12-neighbour tree count.**
- **The sum.** At `x₀ = 347/10000`, which is below `10¹⁰/11¹¹ = 0.035049…`, the sum over the regions around a site is
  `Σ_{V∋x} x₀^{|∂V|} ≤ 0.1430`.
  Block 117's is `0.0897` at `3/250`.
- **Order.** So the two framed states have `⟨σ_x⟩ ≥ 0.714` at every site of every box, for all `x ≤ 347/10000`.
- **The new `g*`.** Through block 117's `x = g^{1/2}Λ(Λ/m)^{5/6}` at `ζ = g⁻³`:

  | case | new `g*` | block 117 |
  |---|---|---|
  | without contents | `(347/10000)² = 1.204·10⁻³` | `9/62500 = 1.44·10⁻⁴` |
  | `(3,1,2)` | `8.575·10⁻⁵` | `10⁻⁵` |
  | `(5,2,4)` | `1.536·10⁻⁴` | `1.8·10⁻⁵` |
  | `(12,1,2)` | `1.628·10⁻⁶` | `1.9·10⁻⁷` |
  | `(9,8,8)` | `8.147·10⁻⁴` | `9.7·10⁻⁵` |

  Each value is the four-figure `g*`: the inequality holds exactly at `g` and fails at `1.001g`.
- **The ceiling of this form.** A tree-count certificate with 12 neighbours cannot pass `x₀ < 10¹⁰/11¹¹`. So without contents, `g* < (10¹⁰/11¹¹)² = 1.2285·10⁻³`.

## 2. Steps

**S1 (PROVED; CHECKED A7). Every wall is a mod-2 cycle.**
- The four cubes around a lattice edge `e` form a cycle.
- Each wall plaquette at `e` separates two consecutive cubes of the cycle with different membership in `V`.
- Membership changes an even number of times around a cycle. So `e` lies on 0, 2 or 4 wall plaquettes.

**S2 (PROVED; CHECKED A6). Lemma: every finite mod-2 2-cycle `Σ` of plaquettes is the wall of exactly one finite cube set.** Here a 2-cycle means that every edge lies on an even number of plaquettes of `Σ`.
- **The candidate set.**
  - For a cube `c`, let `f(c)` be the parity of the number of plaquettes of `Σ` crossed by the ray from `c` in direction `+e₁`. These are the plaquettes between `c + je₁` and `c + (j+1)e₁`, for `j ≥ 0`.
  - Put `U = {c : f(c) = 1}`.
- **Claim.** For face-adjacent cubes `c` and `c′`, `f(c) + f(c′) ≡ [the face between them ∈ Σ] (mod 2)`.
  - **If `c′ = c + e₁`**, the ray from `c` is the face `(c, c′)` followed by the ray from `c′`.
  - **If `c′ = c + e_a` with `a ∈ {2, 3}`**, take for `j ≥ 0` the edge `e_j` shared by the four cubes `c + je₁`, `c + (j+1)e₁`, `c′ + je₁` and `c′ + (j+1)e₁`. The four plaquettes around `e_j` are:
    - the `j`-th plaquette of each ray;
    - the faces between the two rays at steps `j` and `j+1`.

    By the cycle condition, an even number of these four lie in `Σ`. Sum over `j = 0, …, J`, with `J` beyond the extent of `Σ`. The between-faces telescope to the face at step 0, since the face at step `J+1` is not in `Σ`. This leaves `f(c) + f(c′) + [face(c, c′) ∈ Σ] ≡ 0`.
- **Hence `∂U = Σ`.**
- **`U` is finite.** Take a cube outside a box containing `Σ`. Join it to a cube whose ray misses the box, by a path that stays outside the box. `f` is constant along such a path, since the path crosses no plaquette of `Σ`. So `f = 0` there.
- **Uniqueness.** If `∂U = ∂U′`, then `U Δ U′` has an empty wall. It is therefore `∅` or all of `Z³`, and being finite it is `∅`.

**S3 (PROVED). Theorem (a).** Suppose `∂V = S_A ⊔ S_B`, with both parts nonempty and no plaquette of `S_A` edge-adjacent to one of `S_B`.
1. **Each part is a 2-cycle.** All wall plaquettes at an edge share that edge, so they lie in the same part. By S1, each part meets every edge 0, 2 or 4 times. So both parts are 2-cycles.
2. **Both parts are walls.** By S2, `S_A = ∂U_A` and `S_B = ∂U_B` for finite nonempty `U_A` and `U_B`. Then `∂V = ∂U_A + ∂U_B = ∂(U_A Δ U_B)` mod 2, so `V = U_A Δ U_B` by uniqueness.
3. **The key restriction.** No plaquette lies in both `∂U_A` and `∂U_B`. So no two face-adjacent cubes can differ both in membership of `U_A` and in membership of `U_B`.
4. **Using `V` face-connected.** `V = (U_A∖U_B) ∪ (U_B∖U_A)`. A face between these two parts is forbidden by step 3. Since `V` is face-connected, one part is empty. Say `U_B ⊆ U_A`, so that `V = U_A∖U_B`.
5. **Using the complement face-connected.** The complement is `U_B ∪ (Z³∖U_A)`. A face between `U_B` (in both sets) and `Z³∖U_A` (in neither) is forbidden by step 3. The complement is face-connected and `Z³∖U_A ≠ ∅`, so `U_B = ∅`. Then `S_B = ∅`, a contradiction.
6. **The other case**, `U_A ⊆ U_B`, is symmetric. ∎

The proof uses only S1 and S2; nothing is imported. Block 117's Mayer–Vietoris import, which gives vertex-connectedness, becomes unnecessary: edge-connectedness implies it.

**S4 (CHECKED A2–A5, A8). Exact checks.**
- **Exhaustive to 8 cells.** Redelmeier enumeration gives the fixed polycubes of 1 to 8 cells, `1, 3, 15, 86, 534, 3481, 23502, 162913` (190535 in all). Every one has a face-connected complement and an edge-connected wall.
- **Random large regions.** 400 random regions of up to 266 cells, grown by random site acceptance with cavities filled, all have edge-connected walls.
- **The test is not vacuous.** These walls contain 1135 vertices where they are locally pinched, with two edge-classes at the vertex.
- **Sharpness of the hypotheses.**
  - A `3³` block with an empty centre, whose complement is not face-connected, has two wall classes even through vertices.
  - Two cubes meeting only at a vertex (`V` not face-connected) have two edge-classes and one vertex-class.
  - Two cubes meeting along an edge stay edge-connected.

**S5 (PROVED; CHECKED A1, B2). The 12-neighbour tree count.**
- A plaquette is edge-adjacent to 12 others (A1).
- A connected set of `k` plaquettes through a given one maps injectively to its breadth-first tree. The root has at most 12 children and every other vertex at most 11.
- Lagrange inversion gives `r_k = (12/(k−1)) C(11k, k−2)`, the `k`-th coefficient of `R = x(1+U)¹²` with `U = x(1+U)¹¹` (B2, for `k ≤ 30`).
- Its radius of convergence is `x_c = 10¹⁰/11¹¹`, at `U_c = 1/10`.

**S6 (PROVED; CHECKED B1, B3). Block 117's T4 with S3 and S5.**
- The small regions around a site are unchanged (B1, recomputed): `{6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538}`, and seven or more cells need `|∂V| ≥ 24`.
- The ray argument is unchanged: the wall meets the `e₁` ray within `|∂V|/4` sites.
- **The tail.**
  - At `x₀ = 347/10000`, `U₊ = 88/1000` satisfies `x₀(1+U₊)¹¹ ≤ U₊`, so `U(x₀) ≤ U₊`.
  - The tail `Σ_{k≥24}(k/4)r_k x₀^k` is at most `(x₀/4)R′(x₀)` minus its first 23 terms.
  - Here `R′ = (1+U)¹² + 12x(1+U)¹¹U′` and `U′ = (1+U)¹¹/(1 − 11x(1+U)¹⁰)`, both evaluated at `U₊`.
- **Result.** Adding the exact small counts gives `Σ ≤ 0.14296` in exact rationals.
- **Control.** The same code reproduces block 117's 32-neighbour sum below `0.0897`.

**S7 (CHECKED B4, B5). The new `g*`.** Block 117's T5 gives `x ≤ x₀ ⟺ g³Λ⁶(Λ/m)⁵ ≤ x₀⁶`, with `Λ` and `m` the largest and smallest entries of `M`. This yields the table in §1. Without contents `Λ = m = 1`, so `g* = x₀² = 120409/10⁸`.

## 3. First failing step

None for (a) or (b). Not done:
- Block 117's half-filling window with contents (a2's `1.5·10⁻⁷` at `(3,1,2)`). It uses a separate site bracket and is not re-run here.
- A count of closed walls. Walls are closed edge-connected surfaces, so their growth rate is far below the tree bound of 28.5 per plaquette.

## 4. What would finish it

(a) is complete. For larger `g*`: count closed edge-connected walls rather than all connected plaquette sets. Any certificate of the present tree form is capped at `g* < 1.2285·10⁻³` without contents.
