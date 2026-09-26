# The neutral law with vacancies, two-valued menu: no order at low density, order at large β and high density

Worker `w-macbookpro9927a-ja869` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about 2 seconds with a peak of about 60 MB, and all of them are exact (fractions, integers, sympy). The families are:
- **N**: the neutral kernel.
- **R**: reflection positivity.
- **L**: low density.
- **C**: the chessboard ratios and the Peierls sum.

## Sources, provenance and overlap

**Block 126, as landed on main** (`ef918c1910`, `docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_WITH_VACANCIES_THE_INFRARED_STIFFNESS_IS_SET_BY_THE_BINDING_SCALE_…_2026-09-24.md`; PR #9182 is closed). It is read as landed. It supplies:
- the law with vacancies of block 39 T5: site states `∅` or a content `s`, with a priori weight `1` for `∅` and `z` times the menu's measure for a content;
- the bond kernel `B(∅, ·) = B(·, ∅) = 1` and `B(s, s′) = c e^{βs·s′}`, with the law `∝ Π_b B(u_x, u_y)` on an even torus;
- the two-valued menu `s = ±1` with counting measure;
- `σ_x = n_x s_x`;
- the neutral scale `c₀(β) = 1/cosh β` for the two-valued menu (block 40's scale carried to it);
- the torus magnetization diagnostic of T4.

Its discipline gate item N1.3 reads: "Whether the neutral law has long-range order at large `β` is open." That is the question here.

**Provenance.** The claim printed no prior attempts on this problem. Related work:
- Block 126 harvests the `moving-kernel-with-vacancies` attempts (a1, #8616; confirmed #9114).
- That problem's directory holds three referee reports under this machine's older label `w-macbookpro90c72`. The one I read (`jd2d4`) records its model as `grok-4.6`.
- None of that work treats order at the neutral scale. Nothing here depends on it.

## Definitions

- **Torus.** `T_L = (Z/LZ)³`, `L` even and `≥ 4`, `N = L³`. There is one bond per site and direction.
- **Neutral scale.** `t = tanh β ∈ (0, 1)`.
- **Two-point function.** `⟨σ_0σ_x⟩` is the torus expectation.
- **Long-range order** means `liminf_L M_L² > 0`, where `M_L² = ⟨(N⁻¹Σ_xσ_x)²⟩ = N⁻¹Σ_x⟨σ_0σ_x⟩`. This is block 126 T4's diagnostic for this scalar menu.
- **Cubes.** A cube is `t + {0, 1}³` for `t ∈ T_L`. Neighbouring cubes overlap on a face.
  - A cube is **good±** if all 8 of its sites are `±1`, and **bad** otherwise.
  - Two cubes are ⋆-adjacent if their indices differ by at most 1 in every coordinate (26 neighbours).

## (1) The statement attempted

At `c = c₀(β)`, with the two-valued menu:

- **(T0)** `B(u, u′) = 1 + t σσ′` for all `u, u′`, with `σ ∈ {−1, 0, 1}`.
- **(T1) No order at low density, at every `β`.** If `z < 1/320`, then on every even torus
  `Σ_x ⟨σ_0σ_x⟩ ≤ p + 6p²/(1 − 5p)`, with `p = 64z`.
  So `M_L² ≤ (p + 6p²/(1−5p))/N → 0`, and the structure factor is bounded uniformly in `k` and `L`.
- **(T2) Order at large `β` and high density.** Let `A = z^{−1/8}` and `U = ((1−t)/(1+t))^{1/4}`. Let `P(A, U) = Σ_{bad τ} A^{V(τ)} U^{m(τ)}` be the pattern polynomial over the 6559 bad `2×2×2` patterns, where:
  - `V` is the number of vacancies;
  - `m` is the number of cube edges whose ends are occupied with opposite signs.

  If `ε := P(A, U) ≤ 1/2704`, then for every `x` and every even `L`:
  `⟨σ_0σ_x⟩ ≥ 1 − 2[2ε + 2ε/(1 − 676ε)²] − δ_L`, with `δ_L → 0`.

  This rests on A1 and A2 (ASSUMED). In particular, `z ≥ 10⁴⁰` and `1 − tanh β ≤ 10⁻⁸` (`β ≥ 9.557`) give `⟨σ_0σ_x⟩ ≥ 0.998 − δ_L`, and `liminf M_L² ≥ 0.998`.

So the neutral two-valued law does not order at low density at any `β`, and it does order at large `β` and high density. In particular, a no-order statement at the neutral scale that holds for all densities at large `β` is false for this menu.

## (2) Steps

**Step 1 (CHECKED N1): the neutral kernel.**
- At `c = 1/cosh β`, `c e^{±β} = 1 ± tanh β`.
- So an occupied pair has `B = 1 + t ss′`, and a pair with a vacancy has `B = 1`.
- Both cases are `B = 1 + tσσ′`.
- Averaged over the other end's two states, an occupied neighbour weighs `1`, the same as the empty state. That is the neutral scale's meaning.

**Step 2 (PROVED; CHECKED R1): reflection positivity through planes of sites.**

*The split.* Let `θ` be the reflection through the plane of sites `{x₁ = j}`. It also fixes `{x₁ = j + L/2}`. The torus splits into two halves `H±` that share these two planes, `Π`, and no bond crosses from `H₊∖Π` to `H₋∖Π`. Write the weight as `W = W₊ · θW₊`. Here `W₊` collects:
- the site weights of `H₊∖Π`;
- all bonds with an end in `H₊∖Π`;
- the square roots of the site weights on `Π`;
- the square roots of the bond weights of bonds inside `Π`.

All weights are positive, since `1 − t > 0`, so the square roots are real.

*The inequality.* For a real `F` depending only on `H₊`:
`Z · E[F θF] = Σ_{σ_Π} (Σ_{σ_{H₊∖Π}} F W₊)(Σ_{σ_{H₋∖Π}} θF · θW₊) = Σ_{σ_Π} G(σ_Π)² ≥ 0`,
because the two inner sums are equal. Symmetry is similar.

*Checked.* R1 checks the resulting positive-semidefinite joint law of mirror sites on a 4-ring, exactly. This holds for every `c`, `β` and `z`, and uses only positive weights.

**Step 3 (PROVED; CHECKED L1–L3): no order at low density.**

(a) *Correlations stay inside occupied clusters.* Condition on the occupied set `O`. The spins on `O` then have law `∝ Π_{bonds in O}(1 + t s_x s_y)` (L2). This is invariant under flipping every spin of one cluster of `O`. So `⟨σ_0σ_x | O⟩ = 0` unless `0` and `x` lie in the same cluster of `O`. Always `|⟨σ_0σ_x | O⟩| ≤ 1`. Hence `|⟨σ_0σ_x⟩| ≤ P(0 ↔ x in O)`.

(b) *The occupation bound.* Given everything off `x`:
- `P(x occupied | rest) = zS/(1 + zS)`, where `S = Σ_{s=±1} Π_{y∼x}(1 + t s σ_y)`.
- With `k` neighbours at `+1` and `l` at `−1`, `S = (1+t)^k(1−t)^l + (1−t)^k(1+t)^l`.
- The coefficients of `(1+t)^k(1−t)^l` are bounded in modulus by those of `(1+t)^{k+l}`. Those are at most the coefficients of `(1+t)⁶`, since `k + l ≤ 6`. The odd powers cancel in `S`.
- So `(1+t)⁶ + (1−t)⁶ − S` has non-negative coefficients (L1 checks all `(k, l)`).
- `(1+t)⁶ + (1−t)⁶` has positive coefficients and equals `64` at `t = 1`.
- So `P(x occupied | rest) ≤ 64z =: p`.

(c) *Domination.* Order the sites `x₁, …, x_N` and sample them in sequence. Given any history of the earlier sites, `P(x_k occupied | history) = E[P(x_k occupied | all others) | history] ≤ p`. Draw independent uniforms `U_k` and declare `x_k` occupied iff `U_k ≤ P(x_k occupied | history)`. This builds the law with `O ⊆ {x_k : U_k ≤ p}`. So `O` is dominated by Bernoulli(`p`) site percolation. The event `0 ↔ x` is increasing.

(d) *Counting paths.* `0 ↔ x` in Bernoulli(`p`) needs a self-avoiding path of `n` steps from `0` to `x` whose `n + 1` sites are all open. On the torus such paths lift to self-avoiding paths in `Z³`, of which there are at most `6·5^{n−1}`. So `Σ_x P(0 ↔ x) ≤ p + Σ_{n≥1} 6·5^{n−1}p^{n+1} = p + 6p²/(1 − 5p)` for `p < 1/5`, that is `z < 1/320` (L3).

(e) *Conclusion.*
- `M_L² = N⁻¹Σ_x⟨σ_0σ_x⟩ ≤ N⁻¹(p + 6p²/(1−5p)) → 0`.
- `⟨|σ̂(k)|²⟩ = Σ_x e^{ik·x}⟨σ_0σ_x⟩ ≤ p + 6p²/(1−5p)` for every `k`.

*Remark (sphere menu, same argument).* Cluster rotation invariance gives (a). The occupation bound is `P(x occupied | rest) ≤ z|μ|(c e^β)⁶`, where `|μ|` is the menu's total mass. At the sphere's neutral scale `c = β/sinh β`, so `c e^β = βe^β/sinh β`. So there is no order for `z|μ|(βe^β/sinh β)⁶ < 1/5`, at every `β`. This is a proof in the text, not checked by check.py.

**Step 4 (PROVED; CHECKED C1, C2): chessboard ratios of the bad patterns.**

*Dissemination.* For a pattern `τ` on `{0,1}³`, reflect it through planes of sites into every cube. The result is the configuration `σ^τ(x) = τ(x mod 2)`. The reflection through `{x_i = 1}` sends `0 ↔ 2` and fixes `1`.

*Its weight.* In `σ^τ`, each of the cube's 12 edges occurs twice per `2×2×2` period cell (C1 counts it directly on the `4³` torus for all `3⁸` patterns). So `W(σ^τ) = w_τ^{N/8}`, with `w_τ = Π_a z^{|τ_a|} Π_{edges}(1 + tτ_aτ_b)²`.

*The ratio.* Let `w₊ = z⁸(1+t)²⁴` be the all-`+` weight. Then
`w_τ/w₊ = z^{−V}((1−t)/(1+t))^{2m}(1+t)^{−2k}`,
where `k` is the number of edges touching a vacancy. Because `Z ≥ W(all +)`, the disseminated probability satisfies `𝔷(τ) := P(σ = σ^τ)^{1/N} ≤ (w_τ/w₊)^{1/8} ≤ A^V U^m`.

*The count.* There are 6559 bad patterns. Without vacancies, `m ≥ 3`, the minimal edge cut of the cube (C1). The pattern polynomial is `P = 16A + 16U³ + 48AU² + 56A² + 30U⁴ + …`, with 42 terms (C2).

**Step 5 (ASSUMED A1; subadditivity PROVED): the chessboard estimate.**

*A1.* For events `E₁, …, E_r` that each depend only on the cube `{0,1}³`, and for distinct `t₁, …, t_r`:
`P(∩_j θ_{t_j}E_j) ≤ Π_j 𝔷(E_j)`, with `𝔷(E) = P(∩_{t∈T_L} θ_t E)^{1/N}`.

*Subadditivity.* `𝔷(E ∪ E′) ≤ 𝔷(E) + 𝔷(E′)`. Expand `∩_t θ_t(E ∪ E′)` over the `2^N` choices of `E` or `E′` at each cube, and apply A1 to each choice. Then `𝔷(E ∪ E′)^N ≤ (𝔷(E) + 𝔷(E′))^N`.

*Consequence.* The bad event is the union of the 6559 pattern events, and it is invariant under reflections. So for any `n` distinct cubes, `P(all bad) ≤ ε^n`, with `ε = Σ_τ 𝔷(τ) ≤ P(A, U)`.

**Step 6 (PROVED given A2; CHECKED C3, C4): the Peierls bound.**

*The cases.* Let `t₀` be the cube with corner `0` and `t₁` the cube with corner `x`. If `σ_0σ_x ≠ 1`, then one of two things holds:
- `t₀` or `t₁` is bad; the probability is at most `2ε`;
- both are good with opposite signs.

*The separating set.* Good cubes that share a site agree, and consecutive cubes on a nearest-neighbour path share four sites. So in the second case every such path from `t₀` to `t₁` meets a bad cube. By A2 the bad cubes contain a ⋆-connected `S′` such that either:
- `|S′| < L` and `S′` separates; or
- `|S′| ≥ L`.

*A small separating set meets a ray.* Suppose `|S′| = n < L`. Then `S′` lies in a box of side at most `n` that does not wrap. The torus minus that box is connected, and it lies in one component of the complement of `S′`. At least one of `t₀` and `t₁` is outside that component, say `t₀`. The walk `t₀ + ke₁` leaves the box within `n` steps, so it meets `S′` at some `1 ≤ k ≤ n`.

*Counting.* A ⋆-connected set of `n` cubes through a given cube is fixed by a closed walk of `2(n−1)` steps along a spanning tree. So there are at most `26^{2(n−1)} = 676^{n−1}` of them.

*The sum.* Put `q = 676ε`. Then
`P(σ_0σ_x ≠ 1) ≤ 2ε + Σ_{n≥1} 2n·676^{n−1}ε^n + N Σ_{n≥L} 676^{n−1}ε^n = 2ε + 2ε/(1−q)² + L³ε q^{L−1}/(1−q)` (C4).

Finally `⟨σ_0σ_x⟩ ≥ 1 − 2P(σ_0σ_x ≠ 1)`, since `σ_0σ_x ∈ {−1, 0, 1}`.

**Step 7 (CHECKED C3, C5): the explicit region.**
- `z ≥ 10⁴⁰` gives `A ≤ 10⁻⁵`.
- `1 − t ≤ 10⁻⁸` gives `U ≤ (1 − t)^{1/4} ≤ 10⁻²`. This is `β ≥ ½ log(2·10⁸ − 1) = 9.5569`.
- `P` has non-negative coefficients, so it is increasing in `A` and `U`.
- So `ε ≤ P(10⁻⁵, 10⁻²) = 1.764·10⁻⁴ ≤ 1/2704`, `q = 0.119`, and `1 − 2[2ε + 2ε/(1−q)²] = 0.99839`.
- The density is `ρ ≥ 1 − ε`, since a vacancy at `0` makes `t₀` bad.

## ASSUMED

- **A1 (the chessboard estimate).** Fröhlich, Israel, Lieb and Simon, *Commun. Math. Phys.* 62 (1978), Theorem 4.1; Biskup, *Reflection positivity and phase transitions in lattice spin models* (2009), Theorem 5.8.
  - It is used for the torus `T_L` (`L` even), whose law is reflection positive under every reflection through a plane of sites (Step 2), with blocks `{0,1}³`.
  - `θ_t` is the composition of reflections through planes of sites mapping `{0,1}³` onto `t + {0,1}³`.
- **A2 (separation on the torus).** Let `L ≥ 4`, and let `S ⊂ T_L` meet every nearest-neighbour path of cubes from `t₀` to `t₁` (`t₀, t₁ ∉ S`). Then `S` contains a ⋆-connected `S′` that either separates `t₀` from `t₁` with `|S′| < L`, or has `|S′| ≥ L`.
  - This is the torus form of the ⋆-connectivity of separating sets in `Z^d` (Deuschel and Pisztora 1996, Lemma 2.1; Timár 2013). Non-contractible separating sets fall under the second alternative.

## (3) Where the route stops

- **The sphere menu at large `β`** is not reached. The chessboard Peierls bound needs a finite set of ground states. A continuous menu has spin waves, and order there needs an infrared bound. That is task route (a), which is not attempted here. For the sphere, only the Step 3 remark (no order at low density) holds.
- **The window between the two statements** is open for the two-valued menu at large `β`: `1/320 ≤ z < 10⁴⁰`. The constants are far from sharp. `P` gives the whole region `{P(z^{−1/8}, ((1−t)/(1+t))^{1/4}) ≤ 1/2704}`, not only the quoted corner.
- **Task route (b)**, a lower bound on `S(k)` at large `k` that forces no order at large `β` for every density, cannot hold for the two-valued menu, by T2.
- **Task item (c)**, exact data on `4³`, is not computed. The state space is `3⁶⁴`.

## (4) What would finish it

- A proof of A2 at this scope (the torus topology), or a Peierls map that avoids it.
- For the sphere menu at the neutral scale: an infrared bound with positive stiffness from another embedding of the empty state (task route (a)). Alternatively, show that the high-density law's occupied set dominates a supercritical percolation, and use Griffiths' second inequality and the random-cluster comparison on it. For continuous spins this still needs a stiffness input.
- Sharp thresholds in `z` and `β` for the two-valued menu.
