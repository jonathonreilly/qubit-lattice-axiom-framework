# Deferred-science recovery, species — first bounded pass

**Worker:** `w-macbookpro9927a-j45fd` (claude-opus-5-5).

**Files.**
- `check.py` in this directory runs in about 1 s. All five families (Q, A, C, W, U) are exact: Gaussian rationals, and characteristic polynomials over `F_1000033` used as certificates. There is no floating point.
- `RECOVERY_STATUS.json` lists the sources inspected, with their dispositions, links and the ranked remainder.

**Pins.**
- `origin/main` is `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`.
- The landing snapshot is `c288aa9…`; batch 8 was landed in `7445cc7a50`.
- Every deferred source used was fetched from its frozen head and checked against the manifest's SHA256. The check does this again for all ten.

**Disclosures.**
- My own earlier units on these objects are:
  - #8741, are-the-eight-species-all-kept a2: which clause removes a branch;
  - #8705, su2-bond-links a3: the species maps as gauge transformations onto flat Z₂ links.
- Neither treats the static multiplicity.
- The related problem the-blind-walk-beyond-first-order (#8848, confirmed #8907) is about second order. all-eight-species-under-the-three-couplings has no attempt.
- No other unit claims this question. Blocks 54 and 68–70 were written by the same model family.

Nothing is adopted, and no physical species selection or infinite-volume claim is made.

## 1. The residual and its statement

**Target** (review U8-R1, PR8599/8601/8602): "distinguish formal branch-label orbits from static finite eigenvalue doubling".

**What the landed note says** (block 70 T3, on main):
- **T3(a):** in rate and reach-three fields, the three nonidentity even maps commute with the generator;
- **T3(b):** Θ = σ₂K commutes with the walk in all five field kinds, with Θ² = −1, so every static level is **at least** doubled; and the branch-label orbits are "not eightfold eigenspace degeneracy".

**What was deferred.** The PR8602 checker (item 2) records a failed scratch expectation of a further doubling beyond Θ's. The control's W2 found, in floating point only, "multiplicity two for every level in every case".

**The residual.** On even tori, what static degeneracy of the uniform walk's branch structure survives in varying real fields? Is the doubling exactly two, or does the extra symmetry of the rate and reach-three fields force four?

**The statement attempted.**

- **(a) The symmetry forces doubling only.**
  - In rate and reach-three fields, the three even maps `V₁₁₀, V₁₀₁, V₀₁₁` commute with the walk. They are Hermitian involutions, pairwise anticommuting, with `V₁₁₀V₀₁₁ = iV₁₀₁`.
  - The reversal Θ commutes with the walk and has Θ² = −1.
  - **Θ anticommutes with each even map: `ΘV_nΘ⁻¹ = −V_n`.** This relation is new.
  - Together they admit the 2-dimensional irreducible corepresentation `V ↦ σ_z, σ_x, −σ_y`, `Θ ↦ σ_yK`.
  - So on each eigenspace `ℂ² ⊗ W`, Θ acts on `W` as a real structure. Symmetry forces even multiplicity and nothing more: **never a forced four- or eightfold level**.
- **(b) Rate fields keep the species' zero modes exactly.**
  - `ker(ΦHΦ) = Φ⁻¹ ker H` for every positive rate field `w = Φ²`.
  - On every even torus, `ker H` is the 16-dimensional span of the eight species' zero-momentum states (`k ∈ {0, π}³`) times the two coin states.
  - So in every rate field the zero level has multiplicity exactly 16.
- **(c) Generic levels are exactly doubled** (certified).
  - **Rate field on `4×4×4`.** The `V₁₁₀ = +1` block has characteristic polynomial `E⁸ q(E)`, with `q` of degree 56, squarefree and `q(0) ≠ 0`. `V₁₀₁` maps it onto the `−1` block. So there are 56 nonzero levels, each of multiplicity exactly 2.
  - **Reach-three strain on `6×4×4`.** The block has degree 96, is squarefree, and has no zero root.
  - **Frame and reach-two strain on `4×4×4`,** where no species map is a symmetry: the characteristic polynomial is `q²`, with `q` of degree 64 squarefree.
  - **Genericity.** The discriminant of the block polynomial, with the forced `E⁸` removed, is a polynomial in the field values. It is nonzero at the witness. So for each kind and torus size witnessed, every nonzero level has multiplicity exactly 2 **for all fields outside a proper algebraic subset**.
- **(d) The uniform contrast.** The uniform walk on `4×4×4` has characteristic polynomial `E¹⁶(E² − 1)²⁴(E² − 2)²⁴(E² − 3)⁸`.
  - Its levels have multiplicities 16, 24, 24 and 8, where momentum and species labels coincide.
  - A varying field lifts all of it to exact doubling, apart from the rate field's zero level.

## 2. Steps

**S1 (CHECKED Q). The sources.**
- The landed T3(a) and T3(b); the frozen T3's "two classes of eight exact copies"; review U8-R1.
- The four deferred PR8602 sources (checker item 2, control W2).
- The six PR8599/8601 sources.
- All are verified by SHA256 against the manifest.

**S2 (PROVED; CHECKED A). The algebra.**
- `V_n = R_nU_n`, with `R₁₁₀ = σ₃`, `R₁₀₁ = σ₂`, `R₀₁₁ = σ₁` (the half turns), and `U_n` the real site signs.
- **The new relation.** `ΘV_nΘ⁻¹ = σ₂ V̄_n σ₂ = (σ₂σ̄_cσ₂)U_n = −σ_cU_n`, because `σ₂σ̄_cσ₂ = −σ_c` for every Pauli matrix.
- **Checked on `4×4×4`, as matrix identities:**
  - `V_n² = 1`, the pairwise anticommutation, and `V₁₁₀V₀₁₁ = iV₁₀₁`;
  - `V_nH_wV_n = s_nH_w` for all eight `n` in a varying rate field;
  - Θ commuting with the rate, reach-two and frame walks;
  - `ΘV_nΘ⁻¹ = −V_n`.

**S3 (PROVED; CHECKED C). The corepresentation.**
- Let `𝒜` be the algebra generated by `V₁₁₀` and `V₁₀₁`. The relations make it `≅ M₂(ℂ)`. On an eigenspace, `E_λ ≅ ℂ² ⊗ W` with `𝒜` acting on the first factor.
- **Θ on the eigenspace.** Put `J₀ = (σ_yK) ⊗ K_W`. It anticommutes with `𝒜`'s generators, as Θ does. So `ΘJ₀⁻¹` commutes with `𝒜`, and hence equals `1 ⊗ u_W`.
- **The real structure.** `Θ = σ_yK ⊗ Θ_W` with `Θ_W = u_WK_W`. From `Θ² = −1 = (σ_yK)² ⊗ Θ_W² = −Θ_W²` we get `Θ_W² = +1`: a real structure, which forces no degeneracy on `W`.
- So `dim E_λ = 2 dim W`. The minimum 2 is allowed. CHECKED: the explicit `2×2` corepresentation obeys every relation.

**S4 (PROVED; CHECKED W). The zero modes of rate fields.**
- `Φ` is invertible, so `ΦHΦψ = 0 ⟺ H(Φψ) = 0`.
- `H`'s symbol `Σσ_a sin k_a` vanishes exactly at `k ∈ {0, π}³`, which are allowed on even sides.
- CHECKED: `ΦHΦ(Φ⁻¹ψ) = 0` exactly, for the 16 free zero modes, in the witness field.

**S5 (PROVED; CHECKED W). The certificates.**
- **Reduction mod p.** Reduce the Gaussian-rational matrices modulo `p = 1000033 ≡ 1 (mod 4)`, sending `i ↦ 649529`. A repeated factor over `ℚ(i)` would persist mod `p`, so a squarefree polynomial mod `p` is squarefree over `ℚ(i)`.
- **The block form.** `V₁₁₀` is diagonal in the site-coin basis. So its `±1` blocks are principal submatrices, and `V₁₀₁` intertwines them.
- **The Kramers form.** Θ makes the characteristic polynomial a square `q²` over `ℚ(i)`: a monic square root is fixed by the Galois action. It is certified by `gcd(f, f′) = q` with `q` squarefree and `q² = f` mod `p`.
- **The reach-three check.** On `6×4×4` the reach-three strain is nonzero, and the commutation with the even maps and Θ is checked exactly there.

**S6 (PROVED). Genericity.**
- The block's characteristic polynomial, divided by the forced `E⁸`, has coefficients that are polynomials in the field values. So its discriminant `D` is one too.
- `D ≢ 0`, since it is nonzero at the witness (it is nonzero mod `p`).
- So `{D ≠ 0}` is dense and open, and outside the algebraic set `D = 0` every nonzero level is exactly doubled.
- For the frame and reach-two kinds, the same argument applies to the Kramers square root `q`. This needs `q`'s coefficients to be polynomial in the field values. They are the Moore determinant of the quaternion-Hermitian `E − H`: ASSUMED, as a standard identity.

**S7 (CHECKED U). The uniform contrast.**
- The characteristic polynomial of the uniform `4×4×4` walk over `F_p` equals `E¹⁶(E² − 1)²⁴(E² − 2)²⁴(E² − 3)⁸`.
- This also validates the characteristic-polynomial routine against a known answer.

## 3. The first failing step, and the limits

- **Certified sizes only.** Exact doubling is certified for the torus sizes and field kinds tested. For other sizes it rests on S3's upper-bound argument and needs new witnesses.
- **Twist fields.** Block 65's twist fields are not tested. The table in the landed T2 transforms them, so only Θ applies, and a witness is needed.
- **Special fields.** Fields with extra lattice symmetry can have more degeneracy. The exceptional set `D = 0` is not classified.
- **Infinite volume.** Continuous spectra and the infinite lattice are not addressed; the landed T3(b) limits apply.
- **The frozen T3's "two classes of eight exact copies"** stays demoted to formal labels. What extends exactly is the doubling, plus the rate field's 16 zero modes.

## 4. The next exact obligation, and the ranked remainder

1. Witnesses for the twist fields, and for a second torus size per kind. Classify when `D = 0`.
2. The ranked remainder, as in `RECOVERY_STATUS.json`:
   - **(i)** PR8599/8601: the varying-field packet deflection under the reach-two coupling (±12.64). This needs a ray-limit theorem in a varying strain.
   - **(ii)** U8-R2 (PR8603, 8605, 8607).
   - **(iii)** U8-R4 (PR8611, 8612).
   - **(iv)** U8-R5 (PR8613, 8614, 8615).
   - **(v)** U8-R3 (PR8606, 8608).
3. The process-context files of PR8599/8601/8602 were not inspected and stay open.
