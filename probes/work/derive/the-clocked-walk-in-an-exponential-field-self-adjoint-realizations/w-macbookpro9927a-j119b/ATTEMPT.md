# The clocked walk in an exponential field: self-adjoint realizations — attempt 2 of 2

**Worker:** `w-macbookpro9927a-j119b` (claude-opus-5-5).

**Checks:** `check.py` in this directory runs in about 2 s. All five families (Q, G, A, B, C) are exact: sympy, Gaussian rationals and symbolic identities. There is no floating point.

**Disclosures.**
- At claim time the tool printed no earlier attempt on this problem.
- Blocks 54, 108 and 109 were written by the same model family.
- For conventions I read:
  - block 54 as landed;
  - the claim scopes of blocks 108 and 109;
  - block 108's set-up and the statements of its T3 and T4.

  Both routes below are my own and do not start from the notes' proofs:
  - explicit series solutions at every energy for (a);
  - the translation's eigenspaces on the boundary space for (b) and (c).
- My related unit #8760 (the ray limit of the clocked walk) does not treat realizations.

Nothing is adopted, and no gravitational claim is made.

## 1. The exact statement attempted

**Setting.**
- **The walk.** Block 54 as landed: `(Tψ)(x) = ψ(x − 1)`, `D = (i/2)(T − T†)`, `H = Σ_j σ_j D_j` and `H_w = W^{1/2} H W^{1/2}`, with `w = λ^{x₁}`, `λ = μ² = e^g > 1`.
- **Sectors.** A plane wave in `(x₂, x₃)` gives the sector operator
  `(Jψ)(n) = (i/2)σ₁[λ^{n−1/2}ψ(n−1) − λ^{n+1/2}ψ(n+1)] + λⁿ(p₂σ₂ + p₃σ₃)ψ(n)`, with `p = (sin k₂, sin k₃)` and `m = |p|`.
  The case `p = 0` is block 108's line walk.
- **Realizations.** A realization is a self-adjoint extension of `J` on finitely supported vectors.
- **The identity.** A realization *keeps the identity* for the shift `T_a` along `x₁` when `U(t)T_a = T_aU(λ^a t)`.

**(a) Deficiency counts by explicit solutions.**
- **The line.** For every complex `z` there are four solutions

  `f_{s,ε}(n) = (ε/μ)ⁿ v_s Σ_{j≥0} c_j (zλ^{−n})^j`, with `c₀ = 1` and `c_j = −2isε c_{j−1}/(λ^j − λ^{−j})`,

  where `s, ε = ±1` and `v_s` is the eigenvector with `σ₁ = s`.
  - The coefficients fall like `λ^{−j²/2}`, so each series is entire in `z`.
  - Each solution behaves as `(±μ^{−1})ⁿ` at the fast end. So **all four are square-summable there, for every `z`**: the fast end is limit circle, seen directly.
  - The bonds are bounded on the slow side, so that end is limit point (ASSUMED, Weyl). Hence the deficiency indices are `(2, 2)`.
- **In three dimensions.** For `m < m* = sinh(g/2)` the same recursion `A_j c_j = c_{j−1}` holds, with `A_j = (i/2)(λ^j/r − rλ^{−j})σ₁ + P`.
  - It is solvable for every `j ≥ 1` exactly because `(√(1+m²) + m)² < λ ⟺ m < m*`.
  - So all four solutions follow the zero-energy Floquet solutions at the fast end, for every `z`.

**(b) The line.**
- **The boundary space.** The four zero-energy solutions `u_{ε,v}(n) = (ε/μ)ⁿ v` (`ε = ±1`, `v ∈ ℂ²`) span the four-dimensional boundary space at the fast end.
  - Their boundary form is `G = diag(−iσ₁, +iσ₁)`, independent of the cut.
  - `T₁` acts as `εμ`, and `T₂` acts as the scalar `λ`.
  - `G(T₁x, T₁y) = λ G(x, y)`.
  - Realizations are Lagrangian planes of `G`.
- **Classification.**
  - **Every realization, chain-mixing ones included, keeps `U(t)T₂ = T₂U(λ²t)`.**
  - **The realizations keeping `U(t)T_a = T_aU(λ^a t)` for every `a` are exactly**

    `L(v₁, v₂) = span(v₁ ⊗ E₊, v₂ ⊗ E₋)`, with `v₁, v₂` on the isotropic circle `{(1, it)} ∪ {(0, 1)}`.

    They form **a torus**.
  - Chain A is `{(x, σ₃x)}` and chain B is `{(x, −σ₃x)}`.
  - `L(v₁, v₂)` is chain-separate iff `v₂ ∥ σ₃v₁` (`t₂ = −t₁`). That circle is **block 108's**.
  - **Every other point of the torus is a chain-mixing realization that keeps the identity for every translation.** An example is `v₁ = (1, 0)`, `v₂ = (1, i)`, which meets neither chain.
  - A chain-separate realization off block 108's circle is not kept by `T₁`.
- **The half-turn.** The line walk commutes with `σ₁`, the half-turn of the content about the line. **No realization keeps both `σ₁` and the identity for `T₁`.**

**(c) Three dimensions, sector by sector.**
- **The Floquet solutions.** Let `N = sin k₂ σ₃ − sin k₃ σ₂` (so `N² = m²`) and `s = √(1 + m²)`. The zero-energy solutions are `(r/μ)ⁿ v` with `Nv = ((r − 1/r)/2)v`. Label them
  - `a = (v₊, m + s)`,
  - `b = (v₊, m − s)`,
  - `c = (v₋, s − m)`,
  - `d = (v₋, −m − s)`.
- **`m > m*`.** There is one realization (block 109), and it keeps the identity.
- **`0 < m < m*`.**
  - `G` pairs only a with c, and b with d.
  - `T₁ = diag(μ/r)` has four distinct values.
  - **Exactly four realizations keep the identity for every `x₁`-shift**: the isotropic pairs `{a,b}`, `{a,d}`, `{b,c}`, `{c,d}`.
  - The shift by two alone keeps `{a,d}`, `{b,c}` and the sphere `span(αa + δd, ᾱb + δ̄c)`.
  - Each of the four is covariant under the rotations about `x₁`. The quarter-turn `e^{−iπσ₁/4}` sends `p` to `(−p₃, p₂)`, and the half-turn `σ₁` sends `p` to `−p`. Both keep `m`, `r` and the sign of `N`.
- **`m = 0`** (`k₂, k₃ ∈ {0, π}`).
  - The sector is the line: its realizations with the identity form the torus of (b).
  - The half-turn about `x₁` fixes these four sectors and acts on them as `σ₁`. **It keeps none of the torus.**
- **The limit `m → 0`.** Each of the four choices tends to a plane that **depends on the direction of `(sin k₂, sin k₃)`**. For example, `{b,c}` tends to
  - `span((0,1)⊗E₊, (1,0)⊗E₋)` along `(1, 0)`;
  - `span((1,i)⊗E₊, (1,−i)⊗E₋)` along `(0, 1)`.

  Both are points of the torus.
- **Hence** no single choice serves every sector with `m < sinh(g/2)` while being covariant under the half-turn about `x₁`, and no choice continuous in `(k₂, k₃)` does either.
- **On `ℓ²(ℤ³)`.** The four `m = 0` sectors are a null set. So each of the four uniform choices still defines a realization that is covariant under the rotations and keeps the identity for every `x₁`-shift. It is discontinuous in `(k₂, k₃)` at the four points.
- **On a transverse torus** `ℤ × (ℤ/L)²`, the sector `(0, 0)` carries weight. There **no realization keeps both the identity and the half-turn about `x₁`**.

The task's HIT condition ("(b) or (c) exact") is met: (b) and (c) are exact.

## 2. Steps

**S1 (PROVED; CHECKED G). The boundary form.**
- Summation by parts gives `Σ_{n=M}^{N}[ψ†(Jφ) − (Jψ)†φ] = B_N − B_{M−1}`, where

  `B_N(ψ, φ) = ψ(N)† H_{N,N+1} φ(N+1) − ψ(N+1)† H_{N+1,N} φ(N)`,

  with `H_{N,N+1} = −(i/2)λ^{N+1/2}σ₁`.
- The on-site terms are hermitian, so they cancel.
- CHECKED exactly on random Gaussian-rational sequences, including a transverse term.

**S2 (PROVED; CHECKED A). Explicit solutions and the count on the line.**
- **The series.** In the `σ₁ = s` sector, divide the equation by `(ε/μ)ⁿμ^{2n}` and put `X = zλ^{−n}`. The equation becomes `(is/2)(ε^{−1}S(λX) − εS(X/λ)) = X S(X)` for `S = Σ c_j X^j`.
- **The coefficients.** Matching powers gives the stated `c_j`. `|c_j| = 2^j/Π_{i≤j}(λ^i − λ^{−i})`, so the series is entire.
- **The fast end.** For `n ≥ 0`, `|f(n)| ≤ μ^{−n} Σ|c_j||z|^j`, so each solution is square-summable there. The four are independent, because their fast-end behaviours differ.
- **The slow end.** For `n ≤ 0` the operator has bounded entries, so it is limit point (ASSUMED: Weyl's alternative for a bounded end). Exactly two solutions are square-summable there when `Im z ≠ 0`.
- **The count.** Deficiency `= dim(V₊ ∩ V₋) = dim V₋ = 2`.
- CHECKED: the truncated series satisfies the equation up to the exact remainder `−c_J X^{J+1}`, to order 5, with `z` and `λ` symbolic.

**S3 (PROVED; CHECKED A). Three-dimensional sectors below `m*`.**
- `det A_j = ((λ^j/r − rλ^{−j})/2)² − m²`, which vanishes iff `rλ^{−j}` is a Floquet root.
- For `j ≥ 1`, `|rλ^{−j}| ≤ (s + m)/λ`. This is below `s − m`, the smallest root, iff `(s + m)² < λ`, that is iff `m < m*` (`(s+m)²` increases in `m` and equals `λ` at `m*`).
- The series therefore exist for every `z`, and the fast end is limit circle.
- For `m > m*` the count `(0, 0)` is block 109's (the Weyl alternative for matrix chains is ASSUMED).

**S4 (PROVED; CHECKED B). The line's boundary space.**
- **The form.** For `ψ = (r/μ)ⁿv` and `φ = (r′/μ)ⁿv′`: `B_N = −(i/2)(rr′)^N (r + r′) v†σ₁v′`. With `r, r′ = ±1` this gives `G = diag(−iσ₁, iσ₁)`, with no cross term.
- **The shifts.** `T₁` multiplies `(ε/μ)ⁿv` by `εμ`, and `T₂` multiplies it by `λ`.
- **The scaling.** `T₁^{−1} J_max T₁ = λ J_max`, so the boundary form scales by `λ`.
- **Realizations.** The realizations are `D(H_L) = {ψ ∈ D_max : B_∞(ξ, ψ) = 0 for all ξ ∈ L}` for Lagrangian `L`. `T₁` maps `D(H_L)` onto `D(H_{ML})`. So `U(t)T₁ = T₁U(λt)` iff `ML = L`: the forward direction by functional calculus, the converse by comparing generators.

**S5 (PROVED; CHECKED B). The torus.**
- `M` is diagonalizable with eigenvalues `±μ`. So an invariant plane is `(L ∩ E₊) ⊕ (L ∩ E₋)`.
- `E₊` and `E₋` are not isotropic. So `L = span(v₁ ⊗ E₊, v₂ ⊗ E₋)`, and it is Lagrangian iff `v₁†σ₁v₁ = v₂†σ₁v₂ = 0` (the cross terms vanish).
- The isotropic vectors are `(1, it)` and `(0, 1)`.
- `M² = λ` is a scalar, so every `L` is kept by `T₂`.

**S6 (PROVED; CHECKED B). The chains.**
- The solution `x ⊕ σ₃x` is supported on `(↑, even)` and `(↓, odd)`, so it lies in chain A. The solution `x ⊕ −σ₃x` lies in chain B.
- `L(v₁, v₂)` meets chain A iff `v₂ ∥ σ₃v₁`, and then it is chain-separate.
- The witness `t₁ = 0`, `t₂ = 1` is Lagrangian, kept by `T₁`, and meets neither chain.
- A chain-separate plane with `x = (1, 0)` on A and `(1, i)` on B is Lagrangian but not kept by `T₁`.

**S7 (PROVED; CHECKED B). The half-turn.**
- `σ₁ ⊕ σ₁` commutes with `M`. A plane kept by both is spanned by joint eigenvectors `(1, ±1) ⊗ E_±`.
- Each joint eigenvector has `G(x, x) = ∓2i ≠ 0`, so none is isotropic.

**S8 (PROVED; CHECKED C). Three-dimensional sectors with `0 < m < m*`.**
- **The Floquet solutions.** Multiplying the zero-energy recurrence by `σ₁` gives `σ₁P = iN` and `Nv = ((r − 1/r)/2)v`.
- **The form.** From S4's formula, `G_ij` is independent of the cut only if `r_i r_j = 1` or `(r_i + r_j) v_i†σ₁v_j = 0`.
  - The products are 1 exactly for a–c and b–d (CHECKED symbolically for all `m > 0`).
  - `σ₁` maps the `N = −m` space onto the `N = +m` space, so `v₊†σ₁v₊ = v₋†σ₁v₋ = 0` and `v₊†σ₁v₋ ≠ 0`.
  - So `G` pairs a with c, and b with d, nondegenerately.
- **The invariant planes.** `T₁ = diag(μ/r_i)` has four distinct values. The invariant planes are the six pairs, and the isotropic ones are `ab`, `ad`, `bc`, `cd`.
- **The shift by two.** `T₂ = diag(λ/r_i²)` has eigenspaces `{a, d}` and `{b, c}`. A plane of type (1, 1) is Lagrangian iff `(β : γ) = (ᾱ : δ̄)`.
- **Rotations.** They commute with `σ₁D₁` and conjugate `P` and `N` to those of the image sector, so the labels are kept.
- The exact witness is `λ = 4`, `p = (1/4, 1/3)`, `m = 5/12`, `s = 13/12`, with roots `3/2, −2/3, 2/3, −3/2`.

**S9 (PROVED; CHECKED C). `m = 0` and the limits.**
- **The half-turn at `m = 0`.** The half-turn about `x₁` sends `(k₂, k₃)` to `(−k₂, −k₃)`, which fixes `{0, π}²`, and acts on spinors as `−iσ₁`. S7 applies.
- **The limits.** As `m → 0` along the direction `β`: `a → (v₊(β), r = 1)`, `b → (v₊(β), −1)`, `c → (v₋(β), 1)`, `d → (v₋(β), −1)`. The limiting planes at `β = 0` and `β = 90°` differ for all four choices.
- **Continuity.** Near each `m = 0` point the set `0 < m < m*` is a punctured disk, which is connected. There the four invariant realizations are isolated and depend continuously on `k`.
  - So any choice keeping the identity that is continuous there is one fixed label throughout the disk.
  - Its limit then depends on the direction, so it has no continuous value at `m = 0`.

**S10 (ASSUMED).** These are imported at definition level:
- Weyl's limit-point / limit-circle alternative, for scalar and 2×2 three-term operators;
- von Neumann's extension theory and its boundary-form description (Glazman–Krein–Naimark);
- the functional calculus;
- the decomposition over the transverse momenta of a realization that commutes with the transverse shifts (a direct integral).

## 3. Where the route stops

- **The slow end.** Part (a) imports Weyl's alternative there. The fast end is settled for every energy by the explicit series, without Carleman's test.
- **Locality.** "Continuous in `(k₂, k₃)`" is the property that a condition of finite range across the gradient would have. That implication is standard for translation-invariant operators of finite range, and it is used, not proved.
- **Symmetries covered.** Only the rotations about `x₁` are examined. The reflections are not.
- **The physical rule.** Not addressed: which realization, if any, is selected by a limit of finite slabs or by a boundary law at the fast end.

## 4. What would finish it

1. A rule from the framework for the fast end, such as slabs with held walls whose far wall recedes, and which of the four sector choices it selects.
2. The kernel across the gradient of the four uniform choices: how slowly it decays, given the jumps at the four points.
3. Whether giving up the shift by one, and keeping only the shift by two, allows a choice that is continuous and rotation-covariant in every sector. The sphere of choices kept by `T₂` in each sector may allow one.
