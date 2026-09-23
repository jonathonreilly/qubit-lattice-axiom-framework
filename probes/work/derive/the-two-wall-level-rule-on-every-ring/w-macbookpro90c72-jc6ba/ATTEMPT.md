# J:derive:the-two-wall-level-rule-on-every-ring:a2

Worker `w-macbookpro90c72-jc6ba` (claude-opus-5-5). This is attempt 2 of 2. No earlier attempt had files when I claimed the unit, and I formed my plan before reading anything else.

**Overlap.** My earlier unit on block 86's walls under the scalar hop (#8754) used the same one-axis operator with walls, but asked a different question: how block 86's point zero modes split under an added hop. This attempt reuses none of its results.

**Definitions** come from block 87 (open PR #8662): its note, and the function `axis_operator` in its runner. The log parametrisation is taken from the unit text (block 89).

## (1) Exact statement

### The model

- **Ring.** A ring of `L` sites, with `L` even.
- **Operator (block 87).** `h = (1/2i)(t T − Tᵀ t)`, where `t = diag(t_x)`. Block 87's `T` has `T[x, x+1] = 1`, so the bond from `x` to `x+1` carries `t_x`.
- **My convention.** I write `(Tψ)(x) = ψ(x−1)`, so `(hψ)(x) = (1/2i)(t_x ψ_{x−1} − t_{x+1} ψ_{x+1})`. The two operators are related by `h₈₇(t) = −τ h(t) τ⁻¹`, where `τ` translates the ring by one site. So every squared spectrum below is block 87's.
  - **CHECKED (A1, A5):** the characteristic polynomials of `h₈₇²` and `h²` agree on every ring up to `L = 16`.
- **Alternation with two walls.**
  - `t_x = 1 + δ s_x (−1)^x`, where `s_x = +1` for `x < L/2` and `−1` otherwise.
  - More generally `t_x ∈ {t_s, t_w}`: take `t_s` where `s_x(−1)^x = +1` and `t_w` otherwise, with `t_s ≠ t_w` and both positive.
  - `t = 1 ± δ` is block 87's case, and `t = e^{±δ}` is block 89's.
- **Wall.** A wall is a place where two consecutive bonds are equal. It is strong–strong (ss) or weak–weak (ww).

### Claims

**(a) — the HIT.** Let `4 | L`. The multiset of `E²` of `h` with walls equals the wall-free multiset with these changes:
- two copies each of `(t_s − t_w)²/4` and `(t_s + t_w)²/4` are removed;
- two copies each of `0` and `(t_s² + t_w²)/2` are added.

For `t = 1 ± δ` this is block 87's rule: `±δ, ±1 → 0, 0, ±√(1+δ²)`. For `L ≡ 2 (mod 4)` the rule is false: see step 9.

**(b) Any separation, and 2n walls.**
- **Two walls at one sublattice.** Place them `2r` sites apart on a ring with `M = L/2` sublattice sites. Then `det(λ − J) = det(λ − J₀) · χ_r/χ₀`, where
  - `χ_r = (T_M(z) − 1) − (η²/2C²) U_{r−1}(z) U_{M−r−1}(z)`, and `χ₀ = T_M(z) − 1`;
  - `z = (D − λ)/2C`, `D = (t_s² + t_w²)/4`, `C = t_s t_w/4`, `η = (t_s² − t_w²)/4`.
- **Which levels move.** The band edges always move. A degenerate wall-free level `cos(2πj/M)` keeps both copies if `M | 2rj`, and loses both otherwise.
- **Any bonds at all.** `det(λ − J_odd) = (Π b_i)(tr Π T_i − 2)`.
- **Exact zero modes.** They exist iff `Π_{x even} t_x = Π_{x odd} t_x`, and then there are exactly two. For two walls this means the walls are antipodal.

**(c) Log parametrisation.** For `t = e^{±δ}`: `±sinh δ, ±cosh δ → 0, 0, ±√(cosh 2δ)` on every ring with `4 | L`.

## (2) Steps

1. **PROVED (the two sublattice chains are partners).**
   - Order the sites even first, then odd. Then `h = [[0, A], [A†, 0]]`, with `A` of size `M × M`, `M = L/2`.
   - So `h² = J_even ⊕ J_odd`, with `J_even = AA†` and `J_odd = A†A`.
   - **The spectra are equal.** For square `A`, `det(λ − AA†) = det(λ − A†A)`:
     - if `A` is invertible, then `AA† = A(A†A)A⁻¹`;
     - both sides are polynomials in the entries of `A`, so the identity extends to every `A`.
   - So the multiset of `E²` is two copies of `spec J_odd`.
   - **The matrix `J_odd`.** Reading off `h²`:
     - the diagonal at an odd `x` is `(t_x² + t_{x+1}²)/4`;
     - the hop between the odd sites `x` and `x+2` is `−t_{x+1}t_{x+2}/4`.
   - **Chiral pairing.** Since `h` anticommutes with the sublattice sign, each `E² = λ > 0` of multiplicity `2m` is `E = ±√λ`, each `m` times.
   - **CHECKED (A1):** `charpoly(J_even) = charpoly(J_odd)` on every ring up to `L = 40`, and `charpoly(h²) = charpoly(J_odd)²` up to `L = 16`.

2. **PROVED (for `4 | L` the walls are antipodal diagonal defects of `J_odd`).**
   - **Where the walls sit.** The walls are at `x = L/2 − 1` and `x = L − 1`.
     - At `x = L/2 − 1`, `t = 1 − δ` twice: ww.
     - At `x = L − 1`, `t = 1 + δ` twice: ss.
     - Both sites are odd when `4 | L`.
     - Their indices on the odd ring are `M/2 − 1` and `M − 1`, which are `M/2` apart.
   - **Every hop of `J_odd` is uniform.** It pairs one strong and one weak bond, so it equals `−C` with `C = t_s t_w/4`.
   - **Every diagonal away from the walls** is `D = (t_s² + t_w²)/4`.
   - **At the walls** the diagonal is `t_s²/2 = D + η` and `t_w²/2 = D − η`, with `η = (t_s² − t_w²)/4`.
   - So `J_odd = J₀ + η(P_{ss} − P_{ww})`, where `J₀ = D − C(S + S⁻¹)` is the wall-free block.
   - **CHECKED (A1):** entry by entry, on every ring up to `L = 40` for `t = 1 ± 3/10`, and up to `L = 24` for `(t_s, t_w) = (7/4, 2/5)`.

3. **PROVED (ring lemma).** Take a ring of `M ≥ 3` sites with diagonal `a_i` and hops `b_i` between `i` and `i+1`. Set `T_i = [[(λ − a_i)/b_i, −b_{i−1}/b_i], [1, 0]]`. Then `det(λ − J) = (Π b_i)(tr(T_{M−1}⋯T_0) − 2)`.
   - **Proof.** Expand the determinant over permutations. On a ring with `M ≥ 3` every permutation that contributes is one of two kinds:
     - a set of disjoint adjacent transpositions (a matching) together with fixed points;
     - one of the two full rotations.
   - **The matchings.** A fixed point weighs `λ − a_i`, and a matched edge weighs `−b_i²`.
     - The normalised continuants `P_k = Q_k/(b_1⋯b_k)` satisfy `P_k = ((λ − a_k)/b_k)P_{k−1} − (b_{k−1}/b_k)P_{k−2}`. That is the recursion `T_k`.
     - The `(1,1)` entry of the product counts the matchings that avoid the closing edge.
     - The `(2,2)` entry equals `−b_{M−1}²/Π b` times the continuant of the open chain that remains when the closing edge is matched.
     - So `Π b · tr` is the matching sum of the ring.
   - **The two rotations.** Each has sign `(−1)^{M−1}` and product `(−1)^M Π b`. Together they add `−2Π b`.
   - **Uniform case.** With `b_i = −C` and `a_i = D + d_i`, this becomes `T_i = B + (d_i/C)E₁₁`, where `B = [[2z, −1], [1, 0]]` and `z = (D − λ)/2C`.
   - **CHECKED (A3):** exactly, on 36 random bond sequences with `L = 6..16` and walls anywhere, including both kinds of hop defect.

4. **PROVED (Chebyshev form).** Let `T_k` and `U_k` be the Chebyshev polynomials (`U_{−1} = 0`).
   - **Powers of `B`.** `B^k = [[U_k, −U_{k−1}], [U_{k−1}, −U_{k−2}]]`, by induction from `U_{k+1} = 2zU_k − U_{k−1}`.
   - **Its trace.** `tr B^k = U_k − U_{k−2} = 2T_k`. With `z = cos θ` this is `sin((k+1)θ) − sin((k−1)θ) = 2cos(kθ)sin θ`, and a polynomial identity that holds on `[−1, 1]` holds everywhere.
   - **Two defects of opposite sign.** Put `+η` at site `0` and `−η` at site `r`, and let `ε = η/C`. By step 3 the characteristic function is `tr(B^{r−1}(B + εE₁₁)B^{M−r−1}(B − εE₁₁)) − 2`.
     - By cyclicity, both linear terms equal `ε tr(E₁₁ B^{M−1})`. They enter with opposite signs and cancel.
     - The quadratic term is `−ε² (B^{r−1})₁₁ (B^{M−r−1})₁₁`.
     - So the function is `2(T_M − 1) − ε² U_{r−1} U_{M−r−1}`.
   - **CHECKED (A2):** symbolically in `z` and `ε`, for every `M = 3..24` and every `r`. `B^k` and `tr B^k` are checked up to `k = 40`.

5. **PROVED (the four-level rule, every `M = 2n`).**
   - **The factorisation.** `T_{2n} − 1 = 2(z² − 1)U_{n−1}²`, because `cos 2nθ − 1 = −2 sin² nθ = 2(cos²θ − 1)(sin nθ/sin θ)²`.
     - So at `r = n` the characteristic function is `U_{n−1}² (4(z² − 1) − ε²)`.
     - The wall-free one is `U_{n−1}² · 4(z² − 1)`.
   - **The ratio.** Dividing, `det(λ − J_walls)/det(λ − J₀) = (4(z² − 1) − ε²)/(4(z² − 1)) = ((D − λ)² − 4C² − η²)/((D − λ)² − 4C²)`.
   - **The band edges.** `D² − 4C² = ((t_s² − t_w²)/4)² = η²`, `D − 2C = (t_s − t_w)²/4` and `D + 2C = (t_s + t_w)²/4`. Therefore
     - `det(λ − J_walls) · (λ − (t_s − t_w)²/4)(λ − (t_s + t_w)²/4) = det(λ − J₀) · λ(λ − (t_s² + t_w²)/2)`,
     - an identity of polynomials, so multiplicities included.
   - **Which levels move.** The removed levels are the band edges `z = ±1`, i.e. `k = 0` and `k = π`, which lie on the odd ring because `M` is even. Each has multiplicity 1 in `J₀`.
   - **The degenerate levels stay.** Every degenerate level `cos(2πj/M)` sits on both sides in the common factor `U_{n−1}²`, so both copies stay.
   - With steps 1 and 2 this is claim (a). For `t = 1 ± δ` it gives `D = (1+δ²)/2`, `C = (1−δ²)/4`, `η = δ`, and the levels `δ², 1 → 0, 1 + δ²`.
   - **CHECKED (A1):** the final identity holds exactly on every ring `L = 4, 8, …, 40` at `δ = 3/10`, and on `L = 4, …, 24` at `(t_s, t_w) = (7/4, 2/5)`.
   - **CHECKED (A2):** `D² − 4C² = η²` and the level map, symbolically.

6. **PROVED (a second route, and why only the band edges move).** Use Weinstein–Aronszajn on the rank-two defect.
   - **The determinant ratio.** It is `1 − η²(g₀² − g_{M/2}²)`, where `g_r` is `J₀`'s resolvent at distance `r`.
   - **Splitting by parity.** Splitting the Fourier sum into even and odd momenta gives
     - `g₀ + g_{M/2} = −S_per/(CM)` and `g₀ − g_{M/2} = −S_anti/(CM)`;
     - `S_per = Σ_j 1/(z − cos(2πj/n)) = nU_{n−1}/(T_n − 1)` and `S_anti = Σ_j 1/(z − cos((2j+1)π/n)) = nU_{n−1}/(T_n + 1)`. These are logarithmic derivatives of `Π(z − cos) = 2^{1−n}(T_n ∓ 1)`.
   - **The product.** Hence `S_per S_anti = n²U²/(T_n² − 1) = n²/(z² − 1)`, and `g₀² − g_{M/2}² = 1/((D − λ)² − 4C²)`, as in step 5.
   - **The mechanism.** The periodic sum has poles at every degenerate level. The antiperiodic sum vanishes at exactly those points. So the product has poles only at the band edges.
   - **CHECKED (A2):** `S_per S_anti = n²/(z² − 1)` to 40 digits for `n ≤ 16`, at three values of `z`.

7. **PROVED (c).** Put `t_s = e^δ` and `t_w = e^{−δ}` into step 5:
   - `(t_s − t_w)²/4 = sinh²δ`;
   - `(t_s + t_w)²/4 = cosh²δ`;
   - `(t_s² + t_w²)/2 = cosh 2δ`;
   - and `C = 1/4`, `η = sinh(2δ)/2`.

   So `±sinh δ, ±cosh δ → 0, 0, ±√(cosh 2δ)` on every ring with `4 | L`.
   - **CHECKED (A4):** the identities symbolically, and the rings `L = 8, …, 24` at `δ = 0.37` to `10⁻¹⁰` in floating point. The exact ring checks at `(7/4, 2/5)` in A1 cover unequal `t_s`, `t_w` in general.

8. **PROVED (b): any separation, and 2n walls.**
   - **Wall types.** Between walls the bonds alternate. So two consecutive walls have opposite types iff their separation is even, which puts both wall sites on one sublattice. They have the same type iff the separation is odd, which puts them on different sublattices.
   - **Two walls on one sublattice, `2r` sites apart.** By step 4 they give `χ_r = (T_M − 1) − (η²/2C²) U_{r−1}U_{M−r−1}` over `χ₀ = T_M − 1`.
     - **Band edges.** `U_{r−1}(±1)U_{M−r−1}(±1) = r(M − r) ≠ 0` for even `M`, so both band edges always move.
     - **A degenerate level `z_j = cos k_j`, `k_j = 2πj/M`.**
       - Here `χ_r(z_j) = (η²/2C²) sin²(rk_j)/sin²k_j`. This is nonzero unless `sin(rk_j) = 0`, i.e. `M | 2rj`, and when nonzero both copies move.
       - When `sin(rk_j) = 0`, both `U`'s and `T_M − 1` have double zeros at `z_j`. The ratio there is `1 + (η²/C²) r(M − r)/(M² sin²k_j) ≠ 0`, so both copies stay.
     - **CHECKED (A3):**
       - the formula, exactly, for `M = 6, 8, 9, 12` and every `r`;
       - the degree of `gcd(charpoly_walls, charpoly_free)` equals `2 · #{j : M | 2rj}` in every case;
       - `λ = 0` is a level iff `r = M/2`.
   - **Walls on different sublattices** (ss + ss, or ww + ww). The even-site wall enters `J_odd` as one changed hop (`−t²/4` instead of `−C`), and the odd-site wall enters as a diagonal defect. Step 3 covers this. CHECKED (A3) within the random rings.
   - **2n walls on one sublattice.** The characteristic function is `tr Π_k (B + (d_k/C)E₁₁) B^{m_k} − 2`, where `m_k` is the number of plain sites after wall `k`. CHECKED (A3) with four walls at irregular places on rings of 10, 12 and 16.
   - **Exact zero modes, any bonds.**
     - `A` is cyclic and bidiagonal. By the Leibniz expansion, `det A = (−1)^M (Π_{x odd} t_x − Π_{x even} t_x)/(2i)^M`.
     - Deleting one row and one column of `A` leaves a triangular matrix with a nonzero diagonal. So `dim ker A ≤ 1`, and `h` has either 0 or exactly 2 zero modes, one on each sublattice.
     - For `t ∈ {t_s, t_w}`, the products are equal iff the strong bonds are equally many on even and odd `x`.
       - For an ss–ww pair `2r` apart the counts are `r` and `M − r`, which forces `r = M/2`: the walls are antipodal.
       - For a same-type pair `d` apart (odd `d`), balance forces `d = L/2`: again antipodal. This is possible only when `L ≡ 2 (mod 4)`.
     - **CHECKED (A3):** the `det A` formula and the criterion on 36 random rings, of which 8 are balanced; zero multiplicity is exactly one in `J_odd`.
   - **Consequence for block 87's wall-pair energy (executed, floating point).** The sea's energy of a wall pair, `Σ√λ_free − Σ√λ_walls`, equals block 87's `(1 + δ) − √(1 + δ²)` exactly for antipodal walls (step 5). Closer pairs cost less.
     - At `M = 32` and `δ = 0.3` the deficit is `−0.1296` at `r = 1`, and it shrinks by a factor `0.54–0.56` per sublattice step.
     - The scale is set by the zero mode's decay `(1 − δ)/(1 + δ) = 0.538` per step.
     - So through the sea the walls attract at short range. Block 87's constant is the value for separated walls.
     - CHECKED (A3, float).

9. **PROVED (on `L ≡ 2 (mod 4)` the rule cannot hold); CHECKED (what happens instead).**
   - **Why it cannot hold.** `M = L/2` is odd, so `k = π` is not a momentum of the odd ring. The wall-free ring therefore has no level `1 = D + 2C`, and the rule's "remove two copies of 1" is impossible.
   - **Block 87's `s_x` on these rings.**
     - It gives `t_{L/2−1} = t_{L/2} = 1 + δ` and `t_{L−1} = t_0 = 1 + δ`: two ss walls, `L/2` apart (an odd separation).
     - The bonds have period `L/2`, since `t_{x+L/2} = t_x`.
     - The ring is balanced, so there are two exact zero modes.
   - **CHECKED (A5), exactly for `L = 6, 10, 14, 18, 22`:**
     - no squared level of the wall-free ring survives (the gcd is 1);
     - at `L = 6`, `{9/100 ×2, 309/400 ×4}` is replaced by `{0 ×2, 387/400 ×4}`.
   - **An ss + ww pair on these rings** is never antipodal (it would need `2r = M` with `M` odd), so it has no exact zero mode. CHECKED (A3) at `M = 9`.

### ASSUMED

- Only block 87's definitions, as read from its runner's `axis_operator`, and block 89's parametrisation as the unit states it.
- Every other step is argued in full above. The classical facts used (the Chebyshev identities, Sylvester's `AA†`/`A†A` identity, and the ring determinant expansion) are re-proved at the scope used.

## (3) Where the route fails

- **For `4 | L` nothing fails.** Claim (a) holds on every such ring, for any `(t_s, t_w)`.
- **The problem's wording "every even ring" is too broad**, and so is the summary line of block 87's note ("On an even ring, two sharp walls …"). On `L ≡ 2 (mod 4)`:
  - the level `1` does not exist without walls;
  - block 87's walls are both strong–strong;
  - every level moves (step 9).

  Block 87's exact rings (4, 8, 12) and its executed rings (16, 64, 256, control W1) are all multiples of 4, so nothing it computed conflicts with this.
- **Not done:**
  - a closed form for the moved levels on `L ≡ 2 (mod 4)` (checked to `L = 22`, not proved for all such `L`);
  - closed forms for the new levels at non-antipodal separations, beyond the Chebyshev characteristic function.

## (4) What would finish it

- A referee from another model family, reading steps 1–5 line by line. This attempt and blocks 53–89 are one model family.
- **For `L ≡ 2 (mod 4)`:** the period-`L/2` structure splits `h` into a periodic and an antiperiodic sector on an odd ring of `L/2` sites. A closed form there would turn step 9's checks into a proof.
