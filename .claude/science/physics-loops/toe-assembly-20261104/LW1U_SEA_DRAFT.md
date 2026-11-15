lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW1-U_sea, pass 1 (long draft): the free sea's Born law does not move at a half-tick

Written 2026-11-05 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. Lane: LW1-U_sea of part LW1.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation. The scripts are `check_transpose.py`, `check_segment.py`, `check_segment2.py`, `check_kd_corner.py`, `check_kd_simple.py` and `check_misc.py` in `/tmp/toe-usea/`. Each ran in under one minute and under 100 MB, in floating point; the largest space was a torus of 512 sites. A check guides or refutes. It never proves. Every proof below is by hand and is meant to be Lean-formalizable.

**Source revisions read.**

| Ref | Commit |
|---|---|
| branch `claude/toe-assembly`, local checkout (HEAD) | `92e03055c3` |

Files read at that commit, by line, with the commit that last changed each. All are in `.claude/science/physics-loops/toe-assembly-20261104/`.
- `LW1U_DRAFT.md` (last changed `73d98e1a8`): lines 1-386, all of it. Used by line: 67-69 (Lemma 3.1), 73-77 (Lemma 3.2 and its exception), 79-85 (Lemma 3.3, Theorem 3.4), 155-173 (Theorem 4.3), 302-328 (section 10.3, (CL), Theorem 10.2, Corollary 10.3), 330-336 (Lemma 10.4), 345-356 (LW1-U_sea and its attacks).
- `LW1.md` (frozen; last changed `da0ec1934`): lines 1-502, all of it. Used by line: 11-17 (Amendment 1), 30-60 (definitions, free and dressed tick), 64-97 (time convention, Born law, transport, `C_h`, `O_h`, sea), 119 and 124 (inferred definitions 13 and 18), 132 (inferred definition 26), 166 (statement of `L_cube`), 176-205 (A1, A2), 249-266 (B6, B7, support factorization), 310-347 (Theorem B10), 434-462 (E4-E6), 466-472 (LW1-U and its attacks).
- `TOE_ASSEMBLY.md` (last changed `7d2b20d29`): lines 71-235 (section 3 in full). Used by line: 102-107 (PS-3), 144 (PS-7's tension), 169-189 (section 3.2), 190-199 (section 3.3), 212-219 (section 3.5).
- `LW1_5_DRAFT.md` (last changed `e648fa3e0`): lines 1-62 and 296-421 (sections 8 and 9). Used by line: 313 (free tick), 318 (`L5-U`), 324 (PS-3h5), 377 (the carry-over row for LW1-U), 402 (flavour factorization).
- `Y2W_DRAFT.md` (last changed `92e03055c`): lines 1-30 and 169-208, for the file format only.

No other branch was read. No existing file was edited.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-3h, PS-7r and PS-3h5 are read plainly. This file proposes no reading, specification or definition, so no four-test smuggle check is run. Section 7 records two facts for the owner. Neither is proposed as a rule.

**Working set used, by name.** PS-1 read by PS-1c, only through the law `L_cube` of `LW1.md` section 2. PS-3 read by PS-3h (support and transport). PS-7 read by PS-7r (the sea). PS-5 and PS-3h5, only in section 6. The owner decision of `TOE_ASSEMBLY.md` section 3.3, "Non-factor states: held", fixes the scope: the sea is a pure state, hence a factor state, so it is in scope.

**Results of other files used.** `LW1.md`: A1 (`R_T^2 = I`, face phase `-1`), A2 (symmetries), B7 (finite uniqueness, for Remark 3.4 and Lemma 5.9), B10 (the sea), E4-E6 (the sets `C_h`, `O_h` and the history construction). `LW1U_DRAFT.md`: Lemma 3.2, rebuilt in full as Lemma 3.1 below; Lemma 3.3, Theorem 3.4 and Corollary 10.3, rebuilt in short as Lemma 5.9 for the product point outside the window; Lemma 10.4's averaging argument, rebuilt as Lemma 5.4; Theorem 4.3, cited (not rebuilt) only in section 5.7 as context for why one attack fails; Theorem 10.2, discussed and not used as a proof step. `LW1_5_DRAFT.md`: the free tick, PS-3h5 and the flavour factorization, in section 6.

**Inputs from outside the working set.** The joint Born identification, which `LW1.md` takes as a premise (inferred definition 26). Standard mathematics, each rebuilt where used: Wick's determinant rule for gauge-invariant quasi-free states; the Slater-determinant formula for matrix elements of a Fock lift; the continuous functional calculus of a unitary with the Stone-Weierstrass theorem; the Riesz projection and its first-order expansion (credited: Kato, *Perturbation Theory for Linear Operators*, ch. II; not load-bearing); the identity theorem for real-analytic functions; Bloch decomposition over a cell lattice. Literature credited from memory and never load-bearing: Kirkwood (1933) and Dirac (1945) for complex joint quasi-probabilities, and Margenau-Hill (1961) for their real part, which section 5.6 uses as a candidate.

---

## 0. The question, quoted

`LW1U_DRAFT.md` line 347:

> "**Lemma LW1-U_sea (open).** *Let `0 < mu < 2 eps < pi` and let `omega_P` be the PS-7r sea of the free cube tick. For `h = 0` (the even half-tick acting on `omega_P`) and `h = 1` (the odd half-tick acting on `omega_P o beta_e`), the set `O_h` of Theorem E6 has exactly one element.* (`omega_P` is stationary under the tick, so these two cases cover every half-tick.)"

`LW1.md` lines 89-93 define the set:

> "For cell-invariant \(\omega_h\), let \(\mathcal C_h\) be the cell-translation-invariant couplings of \(\nu_h,\nu_{h+1}\) obeying every active-cube support. ... \(\mathcal O_h=\mathop{\rm argmax}_{\mathop{\rm argmin}_{\mathcal C_h}\bar d}s\)."

The route on file is `LW1U_DRAFT.md` line 308:

> "**Theorem 10.2 (uniqueness under CL; proved here).** Under (CL), with `lambda` invariant, `O_h` has exactly one element".

Its hypothesis, line 306:

> "**Hypothesis (CL), cube-local given numbers.** There is a law `lambda` of the number field and, for each `m in {0, ..., 8}`, cube laws `alpha_m` and `alpha'_m` on `{sigma : N(sigma) = m}`, such that `mu_h = ∫ ⊗_k alpha_{n_k} dlambda(n)` and `mu_{h+1} = ∫ ⊗_k alpha'_{n_k} dlambda(n)`."

Line 328 records that (CL) fails for the sea, by a [check] only: "(CL) is false for the sea. This is shown by computation, which may refute but does not prove."

`LW1U_DRAFT.md` line 73 holds the degenerate case that decides most of this lane:

> "**Lemma 3.2 (equal Born laws).** Assume `cos alpha != 0` ... If `mu_{h+1} = mu_h`, then `O_h` is the single diagonal coupling `pi(dc, dc') = mu_h(dc) delta_c(dc')`."

Line 77 names its exception: "At the odd half-tick with `beta = eps + mu/2 = pi/2`, `cos beta = 0` ... and the lemma does not apply."

The lane brief asks: prove or refute LW1-U_sea; follow Theorem 10.2's route, either by showing the needed cube-conditional independence or by finding where it fails and building a second optimal transport; then say whether the answer carries to the free sea of the five-mode laws.

## 0.1 Outcome

**LW1-U_sea is proved at every point of the window except one segment at one half-tick.** The proof does not use Theorem 10.2. It rests on one identity.

**Theorem T (proved here).** Both half-step one-body unitaries are symmetric matrices in the site basis: `V_e^T = V_e` and `V_o^T = V_o`. So `V_e V V_e^* = V_e V_o = V^T`. A spectral projection of `V^T` is the transpose of the same projection of `V`. Hence the sea's covariance after the even half-step is `V_e P V_e^* = P^T = \bar P`, the entrywise complex conjugate. A determinantal law depends only on the principal minors of its kernel, and `\bar P` has the same principal minors as `P`. So the sea's Born law is the same at every half-tick. The quantum state does change: `P ≠ P^T` [check: `max|P - P^T|` up to 0.32]. Only its occupation statistics stay fixed.

**Theorem U (proved here).** With equal Born laws, `LW1U_DRAFT.md` Lemma 3.2 (rebuilt here as Lemma 3.1) gives `O_h = {diagonal}` whenever the active angle has nonzero cosine. The even angle `a_e = eps - mu/2` lies in `(0, pi/2)`, so `O_0` is the diagonal coupling everywhere in the window. The odd angle `a_o = eps + mu/2` lies in `(0, pi)`, so `O_1` is the diagonal coupling unless `a_o = pi/2`, which is the segment `2 eps + mu = pi`, `0 < mu < pi/2`. Off that segment, the actual configuration of the free sea never moves: under PS-3h the history starting from the sea is constant in time, almost surely (Corollary 3.3). The torus clause also holds for torus seas (Remark 3.4).

**The route on file.** Theorem 10.2 is not needed off the segment. Its hypothesis (CL) is false for the sea at the even half-tick on an open dense subset of the window. This is now proved (Proposition 4.3), not only checked. So (CL) is sufficient for uniqueness and not necessary: at those points (CL) fails and uniqueness holds.

**The segment `2 eps + mu = pi`, odd half-tick.** There the odd gate is a pure hop `Γ(i R_o)`. The Born laws before and after are still equal, but the support excludes the diagonal for many cube configurations. The least cost is strictly positive at every point of the segment (Lemma 5.3). So the transport must move the configuration, and PS-3's transport jumps from the identity to a moving transport as `a_o` reaches `pi/2`. On the segment this draft proves the structure of the problem (Lemmas 5.1-5.3) and leaves one lemma open, **LW1-U_hop** (section 5.4). Three attacks on it failed, each at a stated step:
1. **Conditional independence (Theorem 10.2 with the finer shared field `(N_E, N_O)`).** Its hypothesis fails near the product point at the end of the segment and at all but isolated points of it (Proposition 5.6). The failing entry is computed by hand: `\bar P_{(2,1,2),(3,2,2)} = i a/6 + O(a^2)`, with `a = pi/2 - mu`.
2. **A coupling built from the state's own cube-local symmetry.** On the segment the state is invariant under a product of cube-local Bogoliubov involutions with exactly the gate's support (Lemma 5.2). The resulting Margenau-Hill form has the right marginals, support and invariance (Lemma 5.7), but it is not positive: one entry equals `-1/648` at the product point, by a hand computation, and stays negative nearby (Lemma 5.8).
3. **Continuation from the solved product point.** At the product point `mu = pi/2` (outside the window) the problem is a product and its optimizer is unique (Lemma 5.9). Specific entropy is affine, the product point's structure is not stable under the perturbation, and continuity alone cannot carry uniqueness: `LW1U_DRAFT.md`'s own family has a singleton at `delta = 0` and a segment for every small `delta > 0` (section 5.7; cited, not rebuilt). So continuation needs a quantitative estimate, and none is available.

No second optimal transport is built anywhere: off the segment none exists, and on the segment none was found.

**Five-mode laws.** Theorem T carries to the free sea of `L5-O` and `L5-U` for both actual configurations of PS-3h5 (site numbers `N_x`, site parities). The same conclusion holds: the transport is the diagonal coupling at both half-ticks off the segment, and the segment is the same open exception (section 6).

---

## 1. Setting and notation

### 1.1 The free tick

The notation is that of `LW1.md` section 1. Sites are `x ∈ Z^3`. The even tiling is `T_e = {b + {0,1}^3 : b ∈ 2Z^3}`. The odd tiling is `T_o = {b + 1 + {0,1}^3 : b ∈ 2Z^3}`, with `1 = (1,1,1)`. The edge `(x, x + e_i)` lies in an even cube when `x_i` is even and in an odd cube when `x_i` is odd (`LW1.md` A1: "a tiling with offset \(o\in\{0,\mathbf1\}\) contains both endpoints in one cube exactly when \(x_i\equiv o_i\pmod2\)"). The signs are `η_i(x) = (-1)^{Σ_{j<i} x_j}`. The hop operators are

`R_T = 3^{-1/2} Σ η_i(x) (|x + e_i⟩⟨x| + |x⟩⟨x + e_i|)`, summed over the edges of the cubes of `T_T`, `T ∈ {e, o}`.

Each `R_T` is a real symmetric matrix in the site basis, and `R_T^2 = I` (`LW1.md` A1). Put `a_e = eps - mu/2`, `a_o = eps + mu/2`,

`V_e = e^{-i a_e R_e} = cos a_e - i sin a_e R_e`,  `V_o = e^{i a_o R_o} = cos a_o + i sin a_o R_o`,  `V = V_o V_e`.

The second forms use `R_T^2 = I`. In the window `0 < mu < 2 eps < pi`, `a_e ∈ (0, pi/2)` and `a_o ∈ (0, pi)`: `a_e > 0` because `mu < 2 eps`, `a_e < eps < pi/2`, and `a_o < 2 eps < pi`.

The half-steps are `W_0 = Γ(V_e)` (the even layer acts first) and `W_1 = Γ(V_o)`, repeated with period 2. States evolve by `ω_{h+1} = ω_h ∘ β_h` with `β_h(A) = W_h^* A W_h` (`LW1.md` line 64). At infinite volume `Γ(·)` of a layer means its automorphism (`LW1.md` E1).

The sea is `ω_P`, the gauge-invariant quasi-free state with covariance `P = 1_{(-pi, 0)}(w(V))`, the projection onto the eigenvalues `e^{-iw}` of `V` with `w ∈ (-pi, 0)`. These are the eigenvalues with positive imaginary part. By `LW1.md` B10, `ω_P` is pure, stationary, `𝒢`-invariant and half filled, `P_xx = 1/2`.

**The spectrum.** By B10(1), every point of the spectrum of `V` has real part in `[cos 2 eps, cos mu]`. For `0 < mu` and `2 eps < pi` this interval lies inside `(-1, 1)`. So `σ(V)` consists of two closed arcs, one in the open upper half plane and one in the open lower half plane. The function `f_P` equal to `1` on the upper arc and `0` on the lower arc is continuous on `σ(V)`, and `P = f_P(V)`.

### 1.2 Quasi-free states and their Born laws

For `0 ≤ G ≤ I` on `ℓ^2(Z^3)`, `ω_G` is the gauge-invariant quasi-free state with `ω_G(c_y^† c_x) = G_xy` and Wick's determinant rule (`LW1.md` line 97). Its Born law `ν_G` is the law of the occupation configuration `c ∈ {0,1}^{Z^3}`, with `ν_G(c_F = σ) = ω_G(P_{F,σ})` (`LW1.md` line 69). Applying the state to joint occupation projectors is the joint Born identification, a premise of `LW1.md` (inferred definition 26).

**Lemma 1.1 (principal minors fix the Born law).** For every finite set `A` of sites, `ν_G(c_x = 1 for all x ∈ A) = det G_{AA}`. If `det G_{AA} = det G'_{AA}` for every finite `A`, then `ν_G = ν_{G'}`.

*Proof.* For distinct sites the occupation projectors commute, and `∏_{x ∈ A} n_x = c^†_{x_1} ⋯ c^†_{x_k} c_{x_k} ⋯ c_{x_1}` (move each `c_{x_j}` to the right past even pairs). Wick's determinant rule gives `ω_G(c^†_{x_1} ⋯ c^†_{x_k} c_{x_k} ⋯ c_{x_1}) = det[ω_G(c^†_{x_i} c_{x_j})]_{ij} = det[G_{x_j x_i}] = det G_{AA}`. For disjoint finite `A, B`, expanding `∏_{y ∈ B}(1 - n_y)` gives `ν_G(c = 1 on A, c = 0 on B) = Σ_{C ⊆ B} (-1)^{|C|} det G_{A ∪ C, A ∪ C}`. So every cylinder probability is a fixed combination of principal minors. Cylinder events determine a measure on `{0,1}^{Z^3}` (Kolmogorov). ∎

**Lemma 1.2 (evolved covariance).** Let `W` be a layer: a unitary on `ℓ^2(Z^3)` that is a direct sum of unitaries on the disjoint cubes of one tiling. Then `ω_G ∘ β` with `β(A) = Γ(W)^* A Γ(W)` is the quasi-free state with covariance `W G W^*`.

*Proof.* `Γ(W) c^†(f) Γ(W)^* = c^†(Wf)` for every one-body vector `f` (the Fock lift acts on each Slater determinant factor by factor). So `Γ(W)^* c_x^† Γ(W) = c^†(W^* e_x) = Σ_z \overline{W_{xz}} c_z^†`, and its adjoint is `Γ(W)^* c_x Γ(W) = Σ_z W_{xz} c_z`. On a cube these are finite sums; at infinite volume they define the layer automorphism of `LW1.md` E1. Then `ω_G(β(c_y^† c_x)) = Σ_{z,z'} \overline{W_{yz}} W_{xz'} ω_G(c_z^† c_{z'}) = Σ_{z,z'} W_{xz'} G_{z'z} (W^*)_{zy} = (W G W^*)_{xy}`. `β` maps each `c_x` to a linear combination of annihilators, so every Wick contraction transforms in the same way, and the image state is quasi-free and gauge invariant. ∎

`LW1.md` B10's proof uses the same rule: "Since \(P\) commutes with \(V\), its evolved covariance is \(VPV^*=P\)."

### 1.3 Supports and the PS-3 sets

At half-tick `h` the active cubes are the even ones for `h` even and the odd ones for `h` odd. On an active cube `C` the one-body gate is `u_C = cos a - i s sin a R_C`, with `(a, s) = (a_e, +1)` on even cubes and `(a, s) = (a_o, -1)` on odd cubes. The cube support is

`S_C = {(σ, σ') : ⟨σ'| Γ(u_C) |σ⟩ ≠ 0}`

on the cube's configurations, as in `LW1.md` line 80 ("\(P_{\Lambda,\zeta}W_\Lambda P_{\Lambda,\xi}\ne0\)") for a single cube. By `LW1.md`'s support factorization (line 266), the support of the whole layer is `∏_C S_C`.

**Lemma 1.3 (Slater matrix elements).** List the corners of a cube in a fixed order. Let `|A⟩ = c^†_{a_1} ⋯ c^†_{a_n} |0⟩` for `A = {a_1 < ⋯ < a_n}`. For a one-body unitary `u` on the cube, `⟨A'| Γ(u) |A⟩ = det u_{A'A}` when `|A'| = |A|`, and `0` otherwise. Here `u_{A'A}` has rows `A'` and columns `A` in the fixed order.

*Proof.* `Γ(u)|A⟩ = c^†(u e_{a_1}) ⋯ c^†(u e_{a_n}) |0⟩` has `n` particles, so it is orthogonal to `|A'⟩` when `|A'| ≠ n`. For `|A'| = n`, the anticommutation relations give `⟨0| c_{a'_n} ⋯ c_{a'_1} c^†(f_1) ⋯ c^†(f_n) |0⟩ = det[⟨e_{a'_i}, f_j⟩]_{ij}` by induction on `n` (expand along the first annihilator). With `f_j = u e_{a_j}` the matrix is `u_{A'A}`. ∎

`C_h`, the per-site cost `dbar` and the specific entropy `s` are those of `LW1.md` lines 89-93. `O_h = argmax_s argmin_{dbar} C_h`. The **diagonal coupling** is `π_diag(dc, dc') = ν_h(dc) δ_c(dc')`.

---

## 2. Theorem T: the Born law is the same at every half-tick

**Lemma 2.1 (the half-steps are symmetric matrices).** `V_e^T = V_e`, `V_o^T = V_o`, and `V^T = V_e V_o = V_e V V_e^*`. Here `X^T` is the transpose in the site basis, `(X^T)_{xy} = X_{yx}`.

*Proof.* `R_e` and `R_o` are real symmetric, so `R_T^T = R_T`. Then `V_e^T = cos a_e I - i sin a_e R_e^T = V_e`, and likewise `V_o^T = V_o`. For bounded operators on `ℓ^2(Z^3)`, `(XY)_{xy} = Σ_z X_{xz} Y_{zy}` (Parseval), so `(XY)^T = Y^T X^T`. Hence `V^T = (V_o V_e)^T = V_e^T V_o^T = V_e V_o = V_e (V_o V_e) V_e^* = V_e V V_e^*`. ∎

The proof uses only that each hop operator is real and symmetric. The face phase `-1` and the angles play no role.

**Lemma 2.2 (transpose and functional calculus).** Let `X` be a unitary on `ℓ^2(Z^3)`. Then `σ(X^T) = σ(X)`, and `f(X^T) = f(X)^T` for every function `f` continuous on `σ(X)`.

*Proof.* Let `J` be complex conjugation in the site basis. Then `X^T = J X^* J`, so the transpose is linear, isometric, reverses products, and satisfies `(X^*)^T = (X^T)^*`; `X^T` is unitary. `λ - X^T = J(\bar λ - X^*)J` is invertible exactly when `\bar λ - X^*` is, that is, when `λ - X` is. So `σ(X^T) = σ(X)`. For a polynomial `p(z, \bar z) = Σ c_{jk} z^j \bar z^k`, `p(X, X^*)^T = Σ c_{jk} ((X^*)^k)^T (X^j)^T = p(X^T, (X^T)^*)`, because `X^T` is normal and its powers commute with those of its adjoint. By Stone-Weierstrass, choose such polynomials `p_n → f` uniformly on `σ(X)`. The continuous functional calculus is isometric, so `p_n(X, X^*) → f(X)` and `p_n(X^T, X^{T*}) → f(X^T)` in norm. Transposition is isometric, so `f(X)^T = lim p_n(X, X^*)^T = lim p_n(X^T, X^{T*}) = f(X^T)`. ∎

**Theorem 2.3 (Theorem T; proved here).** Let `f` be real valued and continuous on `σ(V)` with `0 ≤ f ≤ 1`, and put `G = f(V)`. Start from `ω_0 = ω_G` and apply the half-steps. Then:
(i) the covariance after the even half-step is `V_e G V_e^* = G^T = \bar G`, the entrywise complex conjugate;
(ii) the covariance after the odd half-step is `V_o \bar G V_o^* = G`;
(iii) the states at half-ticks `h = 0, 1, 2, …` have covariances `G, \bar G, G, \bar G, …`, and their Born laws are all equal: `ν_h = ν_G` for every `h`.
(iv) For `0 < mu < 2 eps < pi` the sea `P = f_P(V)` is such a covariance. So the sea's Born law is the same at every half-tick, and the covariance at odd half-ticks is `\bar P`.

*Proof.* (i) Unitary conjugation commutes with the continuous functional calculus (it holds for polynomials in `V, V^*`, and passes to uniform limits). With Lemma 2.1, `V_e f(V) V_e^* = f(V_e V V_e^*) = f(V^T)`, and Lemma 2.2 gives `f(V^T) = f(V)^T`. `G` is Hermitian because `f` is real, so `(G^T)_{xy} = G_{yx} = \overline{G_{xy}}`. (ii) `V_o \bar G V_o^* = V_o V_e G V_e^* V_o^* = V G V^* = G`, since `G = f(V)` commutes with `V`. (iii) Lemma 1.2 turns each half-step into conjugation of the covariance by the layer's one-body unitary, which gives the list. For every finite `A`, `\bar G_{AA}` is the conjugate of the Hermitian matrix `G_{AA}`, so `det \bar G_{AA} = \overline{det G_{AA}} = det G_{AA}`, a real number. Lemma 1.1 gives `ν_{\bar G} = ν_G`. (iv) Section 1.1 shows `P = f_P(V)` with `f_P` continuous on `σ(V)` and valued in `{0, 1}`. ∎

[check: on the `4^3` torus at `(eps, mu) = (0.3, 0.1), (0.7, 0.5), (1.2, 0.3), ((pi - 0.4)/2, 0.4)`, `max|V_e P V_e^* - \bar P| ≤ 4.5e-16`, `max|V_o \bar P V_o^* - P| ≤ 6.2e-16`, and 200 random principal minors agree to `4.5e-16`; yet `max|P - P^T|` is `0.071, 0.141, 0.296, 0.323`.]

**Remark 2.4 (the state moves; its statistics do not).** The check shows `P ≠ P^T` at those points, so the quantum state at odd half-ticks differs from the sea. The even half-step acts on the sea as complex conjugation in the site basis: `ω_1 = ω_{\bar P}`. Every occupation statistic, at any finite set of sites, is unchanged. The proof never uses that `P` is a projection. It uses only that the covariance is a real function of `V`.

**Remark 2.5 (the massless case `mu = 0`; proved here).** At `mu = 0` the arcs of `σ(V)` meet at `1`, and `f_P` is not continuous there. The conclusion still holds. Use the Bloch representation of `LW1.md` line 97 over even cells, `x = 2b + r`. A cell-invariant bounded `X` has fibre matrices `X(K)` (`8 x 8`) with `X_{(b,r),(b',r')} = (2π)^{-3} ∫ e^{iK·(b - b')} X(K)_{rr'} dK`. Then `X^T_{(b,r),(b',r')} = (2π)^{-3} ∫ e^{iK·(b' - b)} X(K)_{r'r} dK`, so `(X^T)(K) = X(-K)^T`. `V_e` acts inside even cells, so its fibre is a constant matrix, and Lemma 2.1 reads `V_e V(K) V_e^* = V(-K)^T` for every `K`. For `K ≠ 0` the fibre `V(K)` has no eigenvalue `±1` (B10(1): `Re λ = 1` only at `chi(K) = 1`, i.e. `K = 0`, and `Re λ > -1` since `2 eps < pi`), and `P(K)` is its spectral projection onto `Im λ > 0`. For a normal matrix `M = Σ_λ λ E_λ`, the matrices `E_λ^T` are mutually orthogonal projections that sum to `I`, and `M^T = Σ_λ λ E_λ^T`; so a spectral projection of `M^T` is the transpose of the same projection of `M`. Hence `V_e P(K) V_e^* = P(-K)^T = (P^T)(K)` for every `K ≠ 0`. The point `K = 0` is null (`LW1.md` line 124: "The massless zero fibre is null in infinite volume"). So `V_e P V_e^* = P^T` at `mu = 0` too, and (iii) holds as before.

**Remark 2.6 (scope).** Theorem 2.3 covers every stationary quasi-free state whose covariance is a real continuous function of `V`: the sea, the tracial state (`f = 1/2`), and any filling by a union of arcs separated by gaps. It says nothing about other invariant states.

---

## 3. Theorem U: LW1-U_sea off one segment

**Lemma 3.1 (equal Born laws; `LW1U_DRAFT.md` Lemma 3.2, rebuilt for both tilings).** Let `ω_h` be cell-invariant with `ν_{h+1} = ν_h`, and let `a` be the active angle of half-tick `h`.
(i) If `cos a ≠ 0`, then `(σ, σ) ∈ S_C` for every configuration `σ` of every active cube, and `O_h = {π_diag}`.
(ii) If `cos a = 0`, then `(σ, σ) ∉ S_C` whenever `σ` has exactly one particle in `C`.

*Proof.* (i) Let `σ` have occupied set `A`, `|A| = n`. By Lemma 1.3, `⟨A| Γ(u_C) |A⟩ = det(cos a I_A - i s sin a R_{AA})`. `R_{AA}` is real symmetric, with real eigenvalues `r_1, …, r_n`. So the determinant is `∏_j (cos a - i s sin a r_j)`. Each factor has real part `cos a ≠ 0`, so the product is nonzero (for `n = 0` it is `1`). Hence `(σ, σ) ∈ S_C`. Now `π_diag` has marginals `ν_h` and `ν_h = ν_{h+1}`. It is cell-invariant because `ν_h` is. Each of its cube pairs is `(c_C, c_C)`, so it is carried by `∏_C S_C`. So `π_diag ∈ C_h` and `dbar(π_diag) = 0`. Let `π ∈ C_h` have `dbar(π) = 0`. Then `c_{C_0} = c'_{C_0}` `π`-a.s.; by invariance the same holds for every active cube, and there are countably many. So `c = c'` `π`-a.s., and `π` is the law of `(c, c)` with `c ~ ν_h`, which is `π_diag`. The least-cost face is `{π_diag}`, and so is `O_h`.
(ii) If `cos a = 0`, then `u_C = -i s sin a R_C` with `|sin a| = 1`. For `A = {x}`, Lemma 1.3 gives `⟨A| Γ(u_C) |A⟩ = -i s sin a R_xx = 0`, because `R_C` has zero diagonal. ∎

**Theorem 3.2 (Theorem U; proved here).** Let `0 < mu < 2 eps < pi` and `ω_0 = ω_P`.
(i) `O_0 = {π_diag}`.
(ii) If `2 eps + mu ≠ pi`, then `O_1 = {π_diag}`.
So LW1-U_sea holds at `h = 0` on the whole window, and at `h = 1` on the whole window except the segment

`Σ_π = {(eps, mu) : 2 eps + mu = pi, 0 < mu < pi/2}`.

*Proof.* Theorem 2.3(iv) gives `ν_1 = ν_0` and `ν_2 = ν_1`. `ω_0 = ω_P` is cell-invariant (B10(3)). `ω_1 = ω_0 ∘ β_0` is cell-invariant too, because even translations preserve both tilings and every sign exactly (`LW1.md` line 199: "Even translations preserve its phases exactly"), so `β_0` commutes with them. At `h = 0` the active angle is `a_e ∈ (0, pi/2)`, so `cos a_e > 0`, and Lemma 3.1(i) applies. At `h = 1` it is `a_o ∈ (0, pi)`, and `cos a_o = 0` exactly when `a_o = pi/2`, that is, `2 eps + mu = pi`. Inside the window this forces `mu < 2 eps = pi - mu`, so `mu < pi/2`. Off that set, Lemma 3.1(i) applies. ∎

At `mu = 0` (outside LW1-U_sea's statement), Remark 2.5 gives equal Born laws and `a_e = a_o = eps ∈ (0, pi/2)`, so `O_0 = O_1 = {π_diag}` there as well.

**Corollary 3.3 (the free sea's actual configuration does not move; proved here).** Let `(eps, mu)` lie in the window and off `Σ_π`. Build a history measure from `ω_P` as in `LW1.md` E5, with each step selected from `O_h`. Then `ξ_h = ξ_0` for every `h`, almost surely, and `ξ_0 ~ ν_P`.

*Proof.* `ω_{2n} = ω_P` and `ω_{2n+1} = ω_1` for all `n` (B10(3)), so Theorem 3.2 applies at every half-tick: the only selectable coupling is `π_diag`. Its disintegration kernel is `K_h(ξ, ·) = δ_ξ` for `ν_P`-almost every `ξ`; completions on null inputs do not change the history measure (`LW1.md` inferred definition 13). The Ionescu-Tulcea measure of E5 then gives `Q(ξ_{h+1} = ξ_h) = π_diag(c = c') = 1` for each `h`. A countable intersection of probability-one events has probability one. ∎

**Remark 3.4 (the torus clause, for torus seas; proved here).** On an even torus with periodic signs and tilings, `R_e` and `R_o` are real symmetric involutions. The torus Bloch fibres are the infinite-volume fibres at the torus momenta, so the torus spectrum lies in `σ(V)`, and the torus sea `P_L = f_P(V_L)` is defined for `mu > 0`. Lemmas 2.1-2.2 and Theorem 2.3 hold verbatim in finite dimension. With `cos a ≠ 0`, the argument of Lemma 3.1 on the torus shows that the unique transport of `LW1.md` B7 is the identity coupling. As `L → ∞`, `P_L → P` entrywise (Riemann sums of the analytic Bloch integrand), so every principal minor converges, the torus Born laws converge locally to `ν_P`, and the identity couplings converge locally to `π_diag`. So the torus clause of LW1-U_f holds at the sea for the torus seas. Nothing is claimed for other torus approximants.

**Remark 3.5 (the entropy stage is idle).** Off `Σ_π`, the least-cost face is already one point. PS-3's greatest-entropy stage plays no role at the free sea. Theorem 10.2 is not needed.

---

## 4. The route on file: (CL) is false for the sea, and not needed

Theorem 3.2 settles LW1-U_sea off `Σ_π` without (CL). This section answers the brief's question about (CL) itself. It turns `LW1U_DRAFT.md`'s [check] (line 328) into a proof, on an open dense set.

**Lemma 4.1 ((CL) forces flat cross-cube correlations; proved here).** Let `ν_h` have the form `∫ ⊗_k α_{n_k} dλ(n)` of (CL). Suppose a group of symmetries of `ν_h` (site permutations) fixes the active cube `C_0`, acts transitively on its corners, and maps active cubes to active cubes. Then for every `k ≠ 0`, `E_{ν_h}[c_x c_y]` takes one value for all `x ∈ C_0`, `y ∈ C_k`. If `ν_h = ν_G` with `G_xx = 1/2`, then `|G_xy|` is constant on `C_0 × C_k`.

*Proof.* Under (CL), the law of `c_{C_0}` given `N_0 = m` is `∫ α_{n_0} dλ(n | N_0 = m) = α_m`, whenever `λ(N_0 = m) > 0`. A symmetry `g` of the group fixes `C_0` and the event `{N_0 = m}`, so this conditional law is `g`-invariant. By transitivity, `α_m(c_x = 1)` is the same for all eight corners, and the eight values sum to `m`, so each is `m/8`. The laws `α_m` are the same for every cube (they do not depend on `k`), so `α_m(c_y = 1) = m/8` for each corner `y` of `C_k` too. Under (CL), given the number field, `c_{C_0}` and `c_{C_k}` are independent with laws `α_{n_0}` and `α_{n_k}`. So `E[c_x c_y] = E_λ[(n_0/8)(n_k/8)] = E_λ[n_0 n_k]/64`, for all `x ∈ C_0`, `y ∈ C_k`. For `ν_G`, Lemma 1.1 with `A = {x, y}` gives `E[c_x c_y] = G_xx G_yy - |G_xy|^2 = 1/4 - |G_xy|^2`. ∎

At `h = 0` the hypotheses hold for `ν_P`: the 24 rotations about the centre of `C_0 = {0,1}^3` lie in `𝒢`, act transitively on its corners and map even cubes to even cubes (`LW1.md` A2), and their sign-gauge lifts do not change occupations, so they preserve `ν_P` (B10(3)).

**Lemma 4.2 (the boundary value; proved here).** At `a_e = 0` and any `a_o ∈ (0, pi)`, `P = (I + R_o)/2`. Then `|P_{(1,0,0),(2,0,0)}|^2 = 1/12` and `P_{(0,0,0),(3,1,1)} = 0`. Here `(1,0,0), (0,0,0) ∈ C_0` and `(2,0,0), (3,1,1) ∈ C_{e_1} = (2,0,0) + {0,1}^3`.

*Proof.* At `a_e = 0`, `V = V_o = cos a_o + i sin a_o R_o`, with eigenvalue `e^{i a_o}` (imaginary part `sin a_o > 0`) where `R_o = 1` and `e^{-i a_o}` where `R_o = -1`. So `P = (I + R_o)/2`. The sites `(1,0,0)` and `(2,0,0)` lie in the odd cube `{1,2} x {-1,0} x {-1,0}` and are joined by an odd edge along `e_1` (its first coordinate `1` is odd), with sign `η_1 = 1`. So `P_{(1,0,0),(2,0,0)} = 1/(2√3)`. The sites `(0,0,0)` and `(3,1,1)` lie in the different odd cubes `{-1,0}^3` and `{3,4} x {1,2}^2`, and `R_o` acts inside odd cubes, so that entry is `0`. ∎

**Proposition 4.3 ((CL) fails at the even half-tick on an open dense set; proved here).** Let `F(eps, mu) = |P_{(1,0,0),(2,0,0)}|^2 - |P_{(0,0,0),(3,1,1)}|^2`. The zero set of `F` in the window is closed with empty interior. At every point of the window off it, the sea's Born law `ν_P` does not satisfy (CL) at `h = 0`.

*Proof.* Let `Ω = {(eps, mu) : 0 < 2 eps < pi, 0 < mu < pi}`. It is convex and contains the window and the line `mu = 2 eps`. The identity `V + V^* = 2 cos a_e cos a_o I + sin a_e sin a_o {R_e, R_o}` of B10's proof uses only `LW1.md` A1, so it holds for all angles. With `{R_e, R_o}` acting on each Bloch fibre as `2 chi(K) I`, every spectral point of `V` has real part between `cos(a_o - a_e) = cos mu` and `cos(a_o + a_e) = cos 2 eps`. On `Ω` both lie in `(-1, 1)`, so `σ(V)` is two closed arcs, one in each open half plane, with `|Im λ|` bounded below locally uniformly. So near each point of `Ω` one fixed contour `Γ` encloses the upper arc and excludes the lower one, and `P = (2πi)^{-1} ∮_Γ (z - V)^{-1} dz` (`LW1.md` lines 346-347). `V` is an entire function of `(a_e, a_o)`, so each entry `P_xy` extends holomorphically to a complex neighbourhood, and `|P_xy|^2 = P_xy \overline{P_xy}` is real-analytic on `Ω`. So `F` is real-analytic on the connected open set `Ω`. By Lemma 4.2, `F = 1/12` on the line `mu = 2 eps`, so `F ≢ 0`. A real-analytic function on a connected open set that vanishes on a nonempty open subset vanishes identically, so the zero set of `F` has empty interior; it is closed by continuity. At a point where `F ≠ 0`, `|P_xy|` is not constant on `C_0 × C_{e_1}`, and Lemma 4.1 shows that (CL) fails. ∎

**What this says about the route.** At every point of that open dense set, (CL) fails and `O_0` is still one point (Theorem 3.2). So (CL) is sufficient for uniqueness, not necessary. At `h = 1` off `Σ_π`, Theorem 3.2 makes (CL) moot, and this file does not decide it there. On `Σ_π` the relevant condition is the finer (CL') of section 5.5, and it fails too.

---

## 5. The segment `Σ_π`: the odd half-step is a pure hop

On `Σ_π`, `a_o = pi/2`, so `V_o = i R_o` and the gate of each odd cube `D` is `Γ(i R_D)`. Parametrize `Σ_π` by `a := a_e = pi/2 - mu ∈ (0, pi/2)`. The point `a = 0` is the product point `mu = 2 eps = pi/2`. It lies on the window's boundary, outside the window. Each odd cube's corners split by the parity of the coordinate sum into four E-corners `E_D` (even sum) and four O-corners `O_D` (odd sum). Every edge changes that parity, so `(R_D)_{xy} = 0` when `x` and `y` are both E-corners or both O-corners.

### 5.1 The support

**Lemma 5.1 (the pure-hop support; proved here).** On `Σ_π` at `h = 1`, let `σ, σ'` be configurations of an odd cube `D` with occupied sets `A, A'`, split as `A = A_E ∪ A_O` and `A' = A'_E ∪ A'_O`. Then `(σ, σ') ∈ S_D` exactly when `|A'_E| = |A_O|`, `|A'_O| = |A_E|`, `det R_{A'_E A_O} ≠ 0` and `det R_{A'_O A_E} ≠ 0`. In particular:
(i) every pair in `S_D` swaps the two counts: `N_E(σ') = N_O(σ)` and `N_O(σ') = N_E(σ)`;
(ii) if `N(σ)` is odd, every `(σ, σ') ∈ S_D` has `|σ Δ σ'| ≥ 2`;
(iii) `S_D` is symmetric: `(σ, σ') ∈ S_D` exactly when `(σ', σ) ∈ S_D`.

*Proof.* By Lemma 1.3, `⟨A'| Γ(i R_D) |A⟩ = i^n det R_{A'A}` for `|A| = |A'| = n`. Order E-corners before O-corners (this changes the determinant by a sign only). Since `R_D` vanishes on pairs of the same class, `R_{A'A} = [[0, X], [Y, 0]]` with `X = R_{A'_E A_O}` of size `p x q` and `Y = R_{A'_O A_E}` of size `r x s`, `p + r = q + s = n`. Its rank is `rank X + rank Y ≤ min(p, q) + min(r, s)`. If `p > q`, the rank is at most `q + r < n`. If `p < q`, then `s < r` and the rank is at most `p + s < n`. So invertibility needs `p = q` and `r = s`, and then `det R_{A'A} = ± det X det Y`. This proves the criterion and (i). (ii) If `N(σ)` is odd then `N_E(σ) ≠ N_O(σ)`, so by (i) the E-parts of `σ` and `σ'` differ in size by `|N_E - N_O| ≥ 1`, and so do the O-parts; hence `|σ Δ σ'| ≥ 2`. (iii) `R_D` is symmetric, so `det R_{AA'} = det (R_{A'A})^T = det R_{A'A}`. ∎

So the support pairs the particles on O-corners before with E-corners after, and the particles on E-corners before with O-corners after. The cost compares E-corners with E-corners and O-corners with O-corners.

### 5.2 Identities of the state on the segment

**Lemma 5.2 (proved here).** On `Σ_π` let `Z_x = (-1)^{⌊x_1/2⌋ + ⌊x_2/2⌋ + ⌊x_3/2⌋}` (the parity of the even-cell index), `D_s = (-1)^{x_1 + x_2 + x_3}` and `Y = D_s Z`, all diagonal.
(i) `Z R_e Z = R_e` and `Z R_o Z = -R_o`. Hence `Z V Z = -V` and `Z P Z = I - P`.
(ii) `\bar P = Y P Y`.
(iii) `Y` is constant on each odd cube: on `D_b = b + 1 + {0,1}^3`, `b ∈ 2Z^3`, it equals `s_b = -(-1)^{(b_1 + b_2 + b_3)/2}`.
(iv) The covariance `\bar P` of `ω_1` commutes with `R_o^s := Y R_o = ⊕_b s_b R_{D_b}`, a real symmetric involution acting inside odd cubes. So `ω_1` is invariant under the product `∏_D Ad Γ(s_D R_D)` of cube-local Bogoliubov automorphisms. The odd gate factors as `Γ(i R_o) = Γ(iY) Γ(R_o^s)`: that symmetry of `ω_1`, followed by a diagonal phase.

*Proof.* (i) An even edge `(x, x + e_i)` has `x_i` even, so `⌊x_i/2⌋ = ⌊(x_i + 1)/2⌋` and `Z_x Z_{x+e_i} = 1`. An odd edge has `x_i` odd, so the cell index steps by one and `Z_x Z_{x+e_i} = -1`. So `Z R_e Z = R_e`, `Z V_e Z = V_e`, and `Z V_o Z = cos a_o - i sin a_o R_o`, which is `-i R_o = -V_o` at `a_o = pi/2`. Hence `Z V Z = -V`. So `σ(V) = -σ(V)`, and `f_P(-z) = 1 - f_P(z)` on `σ(V)` (`-z` lies on the upper arc exactly when `z` lies on the lower one). So `Z P Z = f_P(Z V Z) = f_P(-V) = I - P`. (ii) B10(2) states `\Theta P \Theta^{-1} = I - P` with `\Theta = D_s \mathcal K`, that is, `D_s \bar P D_s = I - P`. With (i), `\bar P = D_s Z P Z D_s = Y P Y`. (iii) For `x = b + 1 + r`, `r ∈ {0,1}^3`: `⌊x_i/2⌋ = b_i/2 + r_i`, so `Z_x = (-1)^{Σ b_i/2 + Σ r_i}`, and `D_s(x) = (-1)^{3 + Σ b_i + Σ r_i} = -(-1)^{Σ r_i}`. The product does not depend on `r`. (iv) By Lemma 1.2 and B10(3), the covariance at `h = 2` is `P = V_o \bar P V_o^* = R_o \bar P R_o`. With (ii), `\bar P = Y P Y = Y R_o \bar P R_o Y = R_o^s \bar P R_o^s`, where `R_o^s = Y R_o = R_o Y` by (iii). `(R_o^s)^2 = I`, so `\bar P` commutes with `R_o^s`, and Lemma 1.2 shows that the Bogoliubov automorphism of `R_o^s` fixes `ω_1`. `R_o^s` acts inside odd cubes, so `Γ(R_o^s) = ∏_D Γ(s_D R_D)`. Finally `i R_o = (iY)(Y R_o)`. ∎

[check: on the `4^3` and `8^3` tori (`Z` needs an even number of cells per side) at `a = 0.3, 1.0`: `max|ZPZ - (I - P)| ≤ 2.4e-15`, `max|\bar P - YPY| ≤ 6.4e-16`, `max|[\bar P, R_o^s]| ≤ 1.3e-15`. Off the segment, at `a_o = 1.2`, `max|ZPZ - (I - P)| = 0.056`.]

**Reading.** On `Σ_π` the odd half-step acts on `ω_1` exactly as the diagonal phase `Γ(iY)` does, and a diagonal phase moves no occupation. That is why the Born law does not change. But PS-3h takes its support from the gate `Γ(i R_o)`, a pure hop, and a pure hop forbids staying put for many configurations.

### 5.3 On the segment the transport must move

**Lemma 5.3 (proved here).** At every point of `Σ_π`:
(i) `P` does not act inside odd cubes: some `P_xy ≠ 0` with `x, y` in different odd cubes;
(ii) `ν_P(N_{D_0} odd) > 0` for the odd cube `D_0 = {1,2}^3`;
(iii) every `π ∈ C_1` has `E_π |c_{D_0} Δ c'_{D_0}| ≥ 2 ν_P(N_{D_0} odd) > 0`. So the least cost at `h = 1` is strictly positive, `π_diag ∉ C_1`, and every element of `O_1` moves the configuration with positive probability.

*Proof.* (i) Use the Bloch representation over odd cells: `x = 1 + 2b + r`, `b ∈ Z^3`, `r ∈ {0,1}^3`, so cell `b` is an odd cube. A cell-invariant bounded operator acts inside odd cubes exactly when its fibre `X(K)` does not depend on `K`. `R_o` acts inside odd cubes, so `R_o(K) = R_D` for all `K`. The shift `T_{±2e_i}` has fibre `e^{∓ i K_i} I_8`, so `Δ := (1/6) Σ_i (T_{2e_i} + T_{-2e_i})` has fibre `chi(K) I_8`. B10's identity at `a_o = pi/2` reads `V + V^* = sin a {R_e, R_o} = 2 sin a Δ` (B10: `R_e R_o + R_o R_e = (1/3) Σ_i (T_{2e_i} + T_{-2e_i})`). So `V(K) + V(K)^* = 2 c(K) I_8` with `c(K) = sin a chi(K)` and `|c| ≤ sin a < 1`. Every eigenvalue of the normal matrix `V(K)` then has real part `c(K)` and imaginary part `±(1 - c^2)^{1/2}`, and the projection onto `Im λ > 0` is `P(K) = (1/2)[I + (V(K) - V(K)^*)/(2i (1 - c(K)^2)^{1/2})]`. On `Σ_π`, `V = i R_o V_e = i cos a R_o + sin a R_o R_e`, so `V - V^* = 2i cos a R_o + sin a [R_o, R_e]`. Now `tr R_D = 0`, `tr R_D^2 = 8`, and `tr(R_D [R_D, R_e(K)]) = tr(R_e(K)) - tr(R_e(K)) = 0` by cyclicity and `R_D^2 = I`. So

`tr(R_D P(K)) = 16 i cos a / (4i (1 - sin^2 a chi(K)^2)^{1/2}) = 4 cos a / (1 - sin^2 a chi(K)^2)^{1/2}`.

At `K = 0`, `chi = 1` and the value is `4`. At `K = (pi/2, pi/2, pi/2)`, `chi = 0` and the value is `4 cos a < 4`, because `a ∈ (0, pi/2)`. So `P(K)` depends on `K`.
(ii) By (i) and cell invariance there are `x ∈ D_0` and `y ∉ D_0` with `P_xy ≠ 0`. Let `G = \bar P`, the covariance at `h = 1`, and `G_0 = G_{D_0 D_0}`. `G` is a projection, so `Σ_z |G_xz|^2 = G_xx`, hence `(G_0^2)_{xx} = Σ_{z ∈ D_0} |G_xz|^2 < G_xx`, and `G_0` is not a projection. Its eigenvalues `g_j` lie in `[0, 1]` (it compresses a projection), so some `g_j ∈ (0, 1)`. By Lemma 1.1 and `det(I + tM) = Σ_B t^{|B|} det M_{BB}`, `E[(-1)^{N_{D_0}}] = Σ_{B ⊆ D_0} (-2)^{|B|} det G_{BB} = det(I - 2 G_0) = ∏_j (1 - 2 g_j)`. Each factor has modulus at most `1`, and one has modulus below `1`. So `E[(-1)^{N_{D_0}}] ≤ ∏_j |1 - 2 g_j| < 1` and `ν_P(N_{D_0} odd) = (1 - E[(-1)^{N_{D_0}}])/2 > 0`. (`ν_1 = ν_P` by Theorem 2.3.)
(iii) Under `π ∈ C_1`, `(c_{D_0}, c'_{D_0}) ∈ S_{D_0}` almost surely, and Lemma 5.1(ii) gives `|c_{D_0} Δ c'_{D_0}| ≥ 2` on `{N(c_{D_0}) odd}`. The per-site cost is the same whether counted on an even or an odd cube, since both are fundamental domains of the cell lattice. A coupling with zero cost would have `c = c'`, so `π_diag` is not carried by the support. ∎

[check: on the `6^3` torus, `ν(N_{D_0} odd) = 0.00017, 0.0042, 0.13, 0.49` at `a = 0.01, 0.05, 0.3, 1.0`. On the `8^3` torus at `a = 0.3, 1.0`, `tr(R_{D_0} P_{D_0 D_0})` equals the torus average of `4 cos a / (1 - sin^2 a chi(K)^2)^{1/2}` to ten digits (`3.8500070731`, `2.3453186121`), and `Y` is constant on every odd cube with the value `s_b`.]

**Consequence: PS-3's transport is discontinuous at `Σ_π`.** Off `Σ_π` the transport is `π_diag` (Theorem 3.2). As the constants approach a point of `Σ_π`, `ν_P` varies continuously and `π_diag` converges locally to the diagonal coupling there, which is not in `C_1` at that point. So the selected transport jumps when the odd angle reaches `pi/2`.

### 5.4 The open lemma

**Lemma LW1-U_hop (open).** *Let `0 < mu < pi/2` and `2 eps = pi - mu`. At `h = 1` (the odd half-tick, a pure hop, acting on `ω_P ∘ β_e`), the set `O_1` has exactly one element.*

It is the only part of LW1-U_sea that Theorem 3.2 leaves. It asks for the least-change, greatest-entropy coupling of `ν_P` with itself through the pure-hop support.

**Lemma 5.4 (a reversible optimizer exists; proved here).** On `Σ_π`, the time swap `τ(c, c') = (c', c)` maps `O_1` onto itself. So `O_1` contains a `τ`-invariant element.

*Proof.* Both marginals are `ν_P` (Theorem 2.3), `S` is symmetric (Lemma 5.1(iii)), the cost `|c Δ c'|` is symmetric, invariance is kept, and `τ` acts on each cell's pair alphabet as a bijection, so it keeps every box entropy. So `τ` maps `C_1` onto itself and keeps cost and specific entropy. `O_1` is convex (`LW1.md` E6), so `(π + τπ)/2 ∈ O_1` for any `π ∈ O_1`. This is the argument of `LW1U_DRAFT.md` Lemma 10.4. ∎

So a second optimizer would have to be irreversible, or two reversible ones would have to tie.

### 5.5 Attack 1: conditional independence given the finer shared field

By Lemma 5.1(i), every `π ∈ C_1` shares the field `m(c) = (N_E(c_D), N_O(c_D))_D` in the sense that `m(c) = m^s(c')` almost surely, with `m^s(c') = (N_O(c'_D), N_E(c'_D))_D`. This field is finer than the cube-number field. `LW1U_DRAFT.md` Theorem 10.2's proof uses the number field only through two facts: it is a field of cube-local functions shared by every coupling in `C_h`, and (CL) holds for it. So the same proof would give uniqueness on `Σ_π` from:

**(CL')** There are a law `λ` of the field and, for each value `v` of a cube's pair of counts, cube laws `α_v` (carried by the configurations with `(N_E, N_O) = v`) and `α'_v` (carried by those with `(N_O, N_E) = v`), such that `ν_1 = ∫ ⊗_D α_{m_D} dλ(m)` and `ν_2 = ∫ ⊗_D α'_{m_D} dλ(m)`.

(CL) implies (CL'): if the cubes are independent given the numbers, they stay independent given the finer field, since each `m_D` is a function of its own cube. So refuting (CL') refutes (CL) on `Σ_π` too.

**Lemma 5.5 ((CL') forces class-flat correlations; proved here).** If `ν_1 = ∫ ⊗_D α_{m_D} dλ(m)`, then for each odd cube `D_k ≠ D_0` and each pair of classes (E or O), `|\bar P_xy|` takes one value over all `x ∈ D_0` and `y ∈ D_k` in those classes.

*Proof.* As Lemma 4.1, with the twelve rotations about the centre `(3/2, 3/2, 3/2)` of `D_0` that keep the parity of the coordinate sum: the identity, the eight turns by `±120°` about the body diagonals, and the three half-turns about the face axes. (Write a rotation as `x ↦ Q(x - c) + c` with `2c = (3,3,3)` and `Q` a signed permutation of determinant `1`. If `Q` flips the signs of a set `F` of coordinates, `Σ_i x_i` changes by `-2 Σ_{i ∈ F} x_i + 3|F|`, which is even exactly when `|F|` is even, that is, when the permutation part of `Q` is even. The even ones are the identity, the eight `±120°` turns and the three face half-turns; the quarter-turns and edge half-turns change the parity.) These twelve lie in `𝒢` (`LW1.md` line 203: "Rotations about other even or odd cube centres differ from these by even translations"). They preserve `ν_1`: `ω_P` is `𝒢`-invariant and each rotation preserves the even half-step up to a sign gauge (A2). They fix `D_0`, keep the field `m`, and act transitively on the four E-corners and on the four O-corners of `D_0` (they are the rotations of a regular tetrahedron with vertices `E_{D_0}`). So `α_v(c_x = 1) = v_E/4` for an E-corner `x` and `v_O/4` for an O-corner `x`, the same in every cube. Under (CL'), `E[c_x c_y] = E_λ[(m_{cl(x)}(D_0)/4)(m_{cl(y)}(D_k)/4)]`, which depends on `x, y` only through their classes. With `\bar P_xx = 1/2`, `E[c_x c_y] = 1/4 - |\bar P_xy|^2`. ∎

**Proposition 5.6 ((CL') fails near the product point and at all but isolated points of `Σ_π`; proved here).** Let `x = (2,1,2)` and `x' = (1,1,1)` in `D_0`, and `y = (3,2,2)` in `D_{e_1} = (3,1,1) + {0,1}^3`. All three are O-corners (coordinate sums `5, 3, 7`). Then

`\bar P_{xy} = i a/6 + O(a^2)`,  `\bar P_{x'y} = O(a^2)`.

So `F_hop(a) := |\bar P_{xy}|^2 - |\bar P_{x'y}|^2 = a^2/36 + O(a^3)`. `F_hop` is real-analytic and not identically zero, so its zeros are isolated, and (CL') fails at every point of `Σ_π` where `F_hop ≠ 0`, including all `a` in some interval `(0, a_1)`.

*Proof.* At `a = 0`, `V(0) = i R_o` and `P_0 := P(0) = (I + R_o)/2`; put `Q_0 = I - P_0`. `V(a) = i R_o e^{-i a R_e} = V(0) + a V_1 + O(a^2)` in norm, with `V_1 = R_o R_e`. Take `Γ` the circle `|z - i| = 1`. For small `|a|`, `σ(V(a))` lies within `O(a)` of `{i, -i}`, so `P(a) = (2πi)^{-1} ∮_Γ (z - V(a))^{-1} dz`. Expand `(z - V(a))^{-1} = R_0 + a R_0 V_1 R_0 + O(a^2)` uniformly on `Γ`, with `R_0(z) = P_0/(z - i) + Q_0/(z + i)`. Inside `Γ`, `(z - i)^{-2}` has zero residue, `(z + i)^{-2}` has no pole, and `(z - i)^{-1}(z + i)^{-1}` has residue `1/(2i)`. So `P(a) = P_0 + a P_1 + O(a^2)` with `P_1 = (P_0 V_1 Q_0 + Q_0 V_1 P_0)/(2i)` (Kato's first-order formula, rebuilt here). Since `P_0 R_o = P_0` and `Q_0 R_o = -Q_0`, `P_1 = (P_0 R_e Q_0 - Q_0 R_e P_0)/(2i)`. `P_0`, `Q_0`, `R_e` are real, so `\bar P(a) = P_0 - a P_1 + O(a^2)`.

For `u ∈ D_0` and `w ∈ D_{e_1}`, `(P_0)_{uw} = 0`. `P_0` and `Q_0` act inside odd cubes. `R_e` joins `D_0` to `D_{e_1}` only by the four even edges `z ↔ z + e_1` with `z ∈ F_0 := {(2, s, t) : s, t ∈ {1,2}}` (first coordinate `2` is even), each with sign `η_1 = 1`. Write `r` for the entries of `R_o` and use `(P_0)_{uv} = (δ_uv + r_uv)/2`, `(Q_0)_{uv} = (δ_uv - r_uv)/2`. Then `(P_0)_{uz}(Q_0)_{z',w} - (Q_0)_{uz}(P_0)_{z',w} = (1/2)[r_{uz} δ_{z'w} - δ_{uz} r_{z'w}]`, and

`(P_1)_{uw} = (4i√3)^{-1} [ r_{u, w - e_1} 1(w ∈ F_0 + e_1) - r_{u + e_1, w} 1(u ∈ F_0) ]`.

For `u = x = (2,1,2)`, `w = y = (3,2,2)` both indicators are `1`. The entry `r_{(2,1,2),(2,2,2)}` belongs to an odd edge along `e_2` (second coordinate `1` is odd) with sign `η_2 = (-1)^{x_1} = (-1)^2 = 1`, so it is `1/√3`. The entry `r_{(3,1,2),(3,2,2)}` belongs to an odd edge along `e_2` with sign `(-1)^3 = -1`, so it is `-1/√3`. Hence `(P_1)_{xy} = (4i√3)^{-1}(2/√3) = 1/(6i)` and `\bar P_{xy} = -a/(6i) + O(a^2) = ia/6 + O(a^2)`. For `u = x' = (1,1,1)`: `x' ∉ F_0`, and `r_{(1,1,1),(2,2,2)} = 0` (opposite corners). So `(P_1)_{x'y} = 0` and `\bar P_{x'y} = O(a^2)`.

The two first-order paths from `x` to `y` run around the face `(2,1,2), (2,2,2), (3,2,2), (3,1,2)`. They add because that face carries the phase `-1` (`LW1.md` A1). On the line `a_o = pi/2`, `mu = pi/2 - a` and `2 eps = pi/2 + a` lie in `(0, pi)` for `a ∈ (-pi/2, pi/2)`, so the argument of Proposition 4.3 makes `F_hop` real-analytic there. It is not identically zero, so its zeros are isolated. Where `F_hop(a) ≠ 0`, Lemma 5.5 (with `x, x', y` all O-corners) shows that (CL') fails. ∎

[check: on the `6^3` torus, `\bar P_{xy}/a = 0.16667i, 0.16666i, 0.16662i, 0.16499i, 0.14662i` at `a = 0.001, 0.01, 0.05, 0.3, 1.0`, and `\bar P_{x'y}` vanished to the printed digits even after division by `a^2`. So `F_hop > 0` at all five points.]

**Where Attack 1 fails, exactly.** The pair of cubes `(D_0, D_{e_1})` is not conditionally independent given the shared field. The dependence appears at first order in `a`, through a face with phase `-1` that straddles the even edge between the cubes.

### 5.6 Attack 2: a coupling from the state's own cube-local symmetry

`LW1U_DRAFT.md` line 356 names what would move the open lemma: "some explicit coupling `pi_hat` built from `P` (for example from the determinantal structure, or from the quantum dynamics of the half-tick)". Lemma 5.2(iv) supplies a candidate from the dynamics. Let `γ_+ = ∏_D Ad Γ(R_D)`. Since `Γ(-R_D) = (-1)^{N_D} Γ(R_D)`, the automorphisms `Ad Γ(-R_D)` and `Ad Γ(R_D)` agree on every element that commutes with the cube parity `(-1)^{N_D}`. So `γ_+` agrees with the symmetry `γ = ∏_D Ad Γ(s_D R_D)` of Lemma 5.2(iv) on every element that commutes with all cube parities. These include every occupation projector `P_E` and its image `γ_+(P_E)`, because each `Γ(R_D)` conserves `N_D`. Unlike `γ`, `γ_+` commutes with cell translations.

**Lemma 5.7 (the Margenau-Hill form; proved here).** For cylinder events `E` of the before-configuration and `E'` of the after-configuration, put

`q(E x E') = Re ω_1(P_E γ_+(P_{E'}))`.

(i) For each finite set `Λ` of odd cubes, `q` restricted to the pair alphabet of `Λ` is a real signed measure, and these are consistent as `Λ` grows; `q` is invariant under cell translations.
(ii) `q(E x all) = ν_1(E)` and `q(all x E') = ν_1(E') = ν_2(E')`.
(iii) `q` vanishes on every `{c_D = σ} x {c'_D = σ'}` with `(σ, σ') ∉ S_D`.
So `q` has every property of an element of `C_1` except, possibly, positivity. If `q ≥ 0` on cylinder rectangles, Kolmogorov's theorem makes it an element of `C_1`.

*Proof.* (i) `q` is bilinear in `(P_E, P_{E'})`, and the occupation projectors of `Λ` sum to `I`, which gives additivity and consistency. Invariance follows from that of `ω_1` and `γ_+`. (ii) `γ_+(I) = I`, so `q(E x all) = ω_1(P_E)`. `γ_+(P_{E'}) = γ(P_{E'})` commutes with all cube parities, and `ω_1 ∘ γ = ω_1`, so `q(all x E') = ω_1(γ(P_{E'})) = ω_1(P_{E'})`; Theorem 2.3 gives `ν_1 = ν_2`. (iii) `P_σ γ_+(P_{σ'}) = P_σ Γ(R_D) P_{σ'} Γ(R_D)^*` (the other factors commute with both projectors and cancel). `Γ(R_D)` and `Γ(i R_D)` have the same nonzero matrix elements up to the factor `i^n` (Lemma 1.3), so `P_σ Γ(R_D) P_{σ'} = 0` when `(σ, σ') ∉ S_D`. ∎

**Lemma 5.8 (the form is not positive near the product point; proved here).** At the product point `a = 0`, take on `D_0` the configurations `A = {(1,1,1), (1,1,2), (1,2,2), (2,2,2)}` and `B = {(1,1,1), (1,1,2), (2,2,1), (2,2,2)}`. Then `(A, B) ∈ S_{D_0}` and `q({c_{D_0} = A} x {c'_{D_0} = B}) = -1/648`. For all small `a > 0` on `Σ_π`, the same value is negative. So `q` is not a coupling there.

*Proof.* At `a = 0`, `ω_1 = ω_{P_0}` with `P_0 = (I + R_o)/2` real, a product over odd cubes of the Slater states `ψ_D` that fill the four-dimensional space `{R_D = 1}`. On `D_0` let `Φ` be a real `8 x 4` matrix whose columns are an orthonormal basis of that space. `Γ(R_D)` is a self-adjoint involution and `Γ(R_D) ψ = det(Φ^T R_D Φ) ψ = ψ`. By Lemma 1.3, `ψ_A := ⟨A|ψ⟩ = det Φ_{A,:}`, so `ψ_A ψ_B = det(Φ_A Φ_B^T) = det (P_0)_{AB}`. Hence `q = ψ_A ⟨A| Γ(R_D) |B⟩ ψ_B = det (P_0)_{AB} · det R_{AB}`, with rows `A` and columns `B` in one fixed order (a reordering changes both determinants by the same sign).

Order `A` and `B` as listed (lexicographic). The signed entries `√3 R_{AB}` are: row `(1,1,1)`: `+1` at `(1,1,2)` (edge along `e_3`, `η_3 = (-1)^{1+1}`). Row `(1,1,2)`: `+1` at `(1,1,1)`. Row `(1,2,2)`: `-1` at `(1,1,2)` (edge along `e_2` from `(1,1,2)`, `η_2 = (-1)^1`) and `+1` at `(2,2,2)` (edge along `e_1`). Row `(2,2,2)`: `+1` at `(2,2,1)` (edge along `e_3` from `(2,2,1)`, `η_3 = (-1)^{2+2}`). All other entries vanish (those corners are not adjacent). So

`√3 R_{AB} = [[0,1,0,0],[1,0,0,0],[0,-1,0,1],[0,0,1,0]]`.

Adding row 1 to row 3 leaves the permutation matrix of `(2,1,4,3)`, of determinant `+1`. So `det R_{AB} = 1/9 ≠ 0`, and `(A, B) ∈ S_{D_0}`. With `t = 1/√3`, `2 (P_0)_{AB} = I_{AB} + R_{AB} = I_{AB} + t · (√3 R_{AB})`, that is,

`2 (P_0)_{AB} = [[1, t, 0, 0], [t, 1, 0, 0], [0, -t, 0, t], [0, 0, t, 1]]`,

where the `1`s mark `A ∩ B = {(1,1,1), (1,1,2), (2,2,2)}`. Expanding along the third column (one entry, `t`, at row 4, cofactor sign `-1`), and then the remaining `3 x 3` along its third column (one entry, `t`), gives `det = -t · t · (1 - t^2) = -(1/3)(2/3) = -2/9`. So `det (P_0)_{AB} = -2/(9 · 16) = -1/72`, and `q = (-1/72)(1/9) = -1/648`.

For `a > 0`, `q_a = Re ω_1^{(a)}(P_A Γ(R_{D_0}) P_B Γ(R_{D_0}))`. The operator is a fixed element of the cube algebra, and `ω_1^{(a)}` evaluates it as a polynomial in finitely many entries of `\bar P(a)` (Wick), which are continuous in `a` (Proposition 4.3's argument). So `q_a → -1/648` as `a → 0`. ∎

[check: at the product point the one-cube form has 528 negative entries among `70^2`, minimum `-1/144`, total negative mass `1.074`. Its signed cost is 8 changes per cube; the one-cube least cost is 3 (linear program).]

**Where Attack 2 fails, exactly.** Positivity: the form built from the state's own symmetry has the marginals, support and invariance of a transport, but it puts weight `-1/648` on a supported pair at the product point, and negative weight there for small `a > 0`. Even setting positivity aside, at the product point its signed cost (8) is far above the least cost (3) [check], so it would not be the least-change transport.

### 5.7 Attack 3: continuation from the solved product point

**Lemma 5.9 (the product point; rebuilt from `LW1U_DRAFT.md` Corollary 10.3 and Theorem 3.4).** At `a = 0` (outside the window), `O_1 = {⊗_D λ*}`, where `λ*` is the unique least-change, greatest-entropy coupling of the cube law `p` of `ψ_D` with itself on `S_D` (`LW1.md` B7). It is not the diagonal coupling.

*Proof.* `ν_1 = ν_2 = ⊗_D p` (product state; `Γ(i R_D) ψ_D = i^4 ψ_D`). Every `π ∈ C_1` has cube laws in `Π(p, p; S_D)`, so its cost per cube is at least `κ(p, p)`, the least cost of the one-cube problem, with equality for `⊗ λ*`. A least-cost `π` has every cube law `π_D` in the least-cost face, hence `H(π_D) ≤ H(λ*)`, with equality only at `π_D = λ*` (B7). By cell invariance all `π_D` are equal. Subadditivity gives `H_Λ(π) ≤ |Λ| H(π_{D_0})` for every box `Λ` of cubes, so `s(π) ≤ H(π_{D_0}) ≤ H(λ*)`. If `π` is not the product of its cube laws, some box `B` has `H_B(π) = |B| H(π_{D_0}) - g` with `g > 0` (equality in subadditivity holds only for independence). Tile a large box by translates of `B`; subadditivity across the translates gives `s(π) ≤ H(π_{D_0}) - g/|B|`. So `s(π) = H(λ*)` only for `π = ⊗ λ*`, which attains it. This is the chain of `LW1U_DRAFT.md` Lemma 3.3 and Theorem 3.4. `p` gives probability `det (P_0)_{E_D E_D} = det(I_4/2) = 1/16` to `A = E_D` (`R_D` vanishes on pairs of E-corners, and `N_D = 4` almost surely), and Lemma 5.1(i) moves that configuration to `O_D`, so `λ*` is not diagonal. ∎

The attack tries to carry this uniqueness to small `a > 0`. It fails at the following step.

**Where Attack 3 fails, exactly.** Continuation needs a quantitative estimate that holds at `a = 0` and survives the perturbation: a strict entropy deficit for every least-cost coupling that differs from the optimizer on some box, uniform in `a`, or a contraction for the optimizers' conditional laws. Neither is available.
- Specific entropy is affine on invariant couplings (`LW1.md` E6), so the second stage has no strict concavity to perturb.
- The product point's structure is not stable. At `a = 0`, `N_D = 4` almost surely. For every `a > 0`, cubes with odd `N_D` have positive probability (Lemma 5.3(ii)) and enter new sectors of the support, which the single-cube face at the product point does not describe. At first order in `a` the cubes also become conditionally dependent given the shared field (Proposition 5.6). So the problem at `a > 0` is not a small deformation of a family of finite problems.
- Continuity alone cannot carry uniqueness. `LW1U_DRAFT.md` Theorem 4.3 gives a family of invariant states, affine in a parameter `delta`, with `O_h` a non-degenerate segment for each `delta ∈ (0, 1/16)` (its proof uses `delta` only in Lemma 4.0(i), which needs `delta < 1/16`, and Lemma 4.0(iii), which needs `delta ≠ 0`). At `delta = 0` the state is a product with equal Born laws, and `O_h = {π_diag}` by Lemma 3.1. This family is cited here, not rebuilt, and is not a step of any proof in this file. Its states are not factor states, so it does not decide the question for the sea; it shows only that a continuation argument must use more than continuity.

### 5.8 Status of LW1-U_hop

Open. Three distinct attacks failed, at the steps stated in sections 5.5-5.7: (CL') is false (Proposition 5.6); the state's own symmetry gives a non-positive form (Lemma 5.8); continuation from the product point lacks a quantitative estimate (section 5.7). No second optimal transport was found. The source a counterexample would need is an optimizer that breaks a symmetry of the problem, such as the time swap of Lemma 5.4. At the product point the optimizer is unique (Lemma 5.9), hence symmetric, so no breaking is visible at zeroth order in `a`.

---

## 6. The five-mode laws

**The answer carries over, with the same exception.** The free tick of both `L5-O` and `L5-U` is the one-body tick `(W V W^*) ⊗ 1_5`, with `W = diag(i^{x_1 + x_2 + x_3})` (`LW1_5_DRAFT.md` line 313: "Its one-body tick is `(W V W^*) ⊗ 1_5`"). Its half-steps are `(W V_e W^*) ⊗ 1_5` and `(W V_o W^*) ⊗ 1_5`, and its PS-7r sea has covariance `(W P W^*) ⊗ 1_5`. By Lemma 1.2 and Theorem 2.3, the covariance after the even half-step is `W V_e P V_e^* W^* ⊗ 1_5 = W \bar P W^* ⊗ 1_5`, and after the odd one it returns to `W P W^* ⊗ 1_5`. A block-diagonal covariance makes the state a product over flavours (`LW1_5_DRAFT.md` line 402: "Block-diagonal covariance makes the quasi-free state a product over flavours: Wick's determinant rule factorizes every moment"). Each flavour's occupation law has principal minors `det(W_A P_{AA} W_A^*) = det P_{AA}` before and `det(W_A \bar P_{AA} W_A^*) = det P_{AA}` after (Lemma 1.1; `W` is diagonal and unitary). So the joint law of all `n_{x,j}` is the same at every half-tick, and so are the laws of the site numbers `N_x` (`L5-U`) and of the site parities `P_x = (-1)^{N_x}` (`L5-O`), which are functions of it. Theorem 2.3 needs no determinantal structure of these laws; that structure was the obstacle `LW1_5_DRAFT.md` line 377 named for Theorem 10.2. Under PS-3h5 the support of an active cube is the set of pairs `(ξ, ζ)` of `N`-patterns (or parity patterns) with `P_ζ Γ P_ξ ≠ 0`. If the active angle has nonzero cosine, choose any flavour-occupation pattern `σ = (σ^{(1)}, …, σ^{(5)})` with pattern `ξ`; Lemma 1.3 for the block-diagonal one-body gate `(W u_C W^*) ⊗ 1_5` gives `⟨σ| Γ |σ⟩ = ∏_j det((W u_C W^*)_{A_j A_j}) = ∏_j det(u_{A_j A_j}) ≠ 0` (`W` is diagonal; proof of Lemma 3.1), so `(ξ, ξ)` is in the support. For any cost that vanishes exactly when no site value changes, the diagonal coupling is then the unique least-cost coupling, and `O_h = {π_diag}`: off `Σ_π`, at both half-ticks, for both laws and both actual configurations, the five-mode free sea's transport is unique and its actual configuration never moves. On `Σ_π` the odd half-step is again a pure hop, which swaps each flavour's E-corner and O-corner counts (Lemma 5.1). A cube whose total number is odd then cannot keep its `N`-pattern (that would need `N_E = N_O`) nor its parity pattern (that would need `N_E ≡ N_O mod 2`). That event has probability `(1 - E[(-1)^{N^{(1)}_{D_0}}]^5)/2 > 0` by Lemma 5.3(ii) and flavour independence. So on `Σ_π` the five-mode transport must move too, and the question is the five-flavour form of LW1-U_hop, not treated here.

---

## 7. What this changes

- **LW1.** LW1-U_sea holds at `h = 0` on the whole window and at `h = 1` off `Σ_π` (Theorem 3.2), with the torus clause for torus seas (Remark 3.4). The open input the vacuum needs shrinks from LW1-U_sea to LW1-U_hop: the odd half-tick on the segment `2 eps + mu = pi`. LW1-U_f, for other invariant factor states, is untouched. LW1's statement "A unique such element is not yet proved" (`LW1.md` line 166) no longer applies to the free sea off `Σ_π`.
- **The route on file.** Theorem 10.2 is not needed for the sea off `Σ_π`. Its hypothesis (CL) is false there at `h = 0` on an open dense set (Proposition 4.3), and the finer (CL') is false on `Σ_π` at all but isolated points (Proposition 5.6). `LW1U_DRAFT.md` line 328's [check] is now a proof on those sets.
- **The free vacuum does not move.** Off `Σ_π`, the PS-3 history from the free sea is constant in time (Corollary 3.3). With `LW1.md` B8a (no records form in the free sea), nothing actual happens in the free vacuum. For TM1 (time and its arrow) and VC1, this sharpens the tension that `TOE_ASSEMBLY.md` line 144 records ("Records on change are frozen in the tested half-filled seas"): in the free sea the actual configuration itself is frozen, not only the records. Actual change must come from states other than the free sea, from the gauged dynamics, or from the segment. This file decides none of those.
- **Five-mode laws.** The row "LW1-U_f, LW1-U_sea, LW1-N | open" of `LW1_5_DRAFT.md` line 377 can be narrowed for the free sea: unique, and the diagonal coupling, off `Σ_π`, for both `L5-O` and `L5-U` (section 6).
- **Two facts for the owner (no rule proposed).** (a) PS-3's transport is discontinuous in the law's constants: it is the identity for `a_o ≠ pi/2` and moves the configuration with positive probability at `a_o = pi/2` (section 5.3). (b) At the free sea off `Σ_π`, PS-3's greatest-entropy stage is idle; the least-change stage alone selects the transport (Remark 3.5).
- **A fact about the gates, for VC1 (no claim about any vacuum).** The dressed generators `H_C` of `LW1.md` lines 57-60 have real matrix elements in the basis of matter occupations and link values `|m⟩` (both `c_y^† c_x` and `J_ℓ` are real there), so they are real symmetric and the dressed half-steps `M_e`, `M_o` are symmetric matrices in that basis. With `τ_E = 0` this gives `M_e U_0 M_e^* = M_e M_o = U_0^T`, and the proof of Theorem 2.3 shows that on a finite torus every density matrix that is a real function of `U_0` has the same joint law of occupations and link values at every half-tick. With `τ_E ≠ 0` the electric layer breaks the identity, since `M_e U_0 M_e^* = M_e W_E M_o` while `U_0^T = M_e M_o W_E`. Whether VC1's vacuum is such a function is VC1's question.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemmas 1.1-1.3 (rebuilt standard facts): principal minors fix a quasi-free Born law; a layer conjugates the covariance; Slater matrix elements of a Fock lift.
- Lemma 2.1: `V_e^T = V_e`, `V_o^T = V_o`, `V_e V V_e^* = V^T`. Lemma 2.2: `f(X^T) = f(X)^T` for unitary `X` and continuous `f`.
- **Theorem 2.3 (Theorem T):** for every stationary quasi-free state whose covariance is a real continuous function of `V`, in particular the PS-7r sea with `0 < mu < 2 eps < pi`, the covariance alternates `G, \bar G, G, …` and the Born law is the same at every half-tick. Remark 2.5 extends this to the sea at `mu = 0`.
- Lemma 3.1 (`LW1U_DRAFT.md` Lemma 3.2, rebuilt for both tilings).
- **Theorem 3.2 (Theorem U):** LW1-U_sea holds at `h = 0` for all `0 < mu < 2 eps < pi`, and at `h = 1` whenever `2 eps + mu ≠ pi`; the unique element is the diagonal coupling. Also at `mu = 0` for both half-ticks.
- Corollary 3.3: off `Σ_π` the actual configuration of the free sea never moves. Remark 3.4: the torus clause holds for torus seas.
- Lemma 4.1 and Proposition 4.3: (CL) fails for the sea at `h = 0` on an open dense subset of the window.
- Lemmas 5.1-5.3 on `Σ_π`: the pure-hop support swaps each cube's E-corner and O-corner counts; the state satisfies `Z P Z = I - P`, `\bar P = Y P Y`, and is invariant under a product of cube-local Bogoliubov involutions with the gate's support; the least cost is strictly positive at every point of `Σ_π`, so PS-3's transport is discontinuous there.
- Lemma 5.4 (a time-swap-invariant optimizer exists on `Σ_π`), Lemma 5.5 and Proposition 5.6 ((CL') fails near the product point and at all but isolated points; `\bar P_{(2,1,2),(3,2,2)} = ia/6 + O(a^2)`), Lemmas 5.7-5.8 (the Margenau-Hill form has marginals, support and invariance but an entry `-1/648` at the product point), Lemma 5.9 (the optimizer at the product point is unique and not diagonal).
- Section 6: the same results for the free sea of `L5-O` and `L5-U`, for site numbers and site parities.

**Counterexamples.** None to LW1-U_sea; off `Σ_π` none exists (Theorem 3.2). Proved false here: (CL) for the sea at `h = 0` on an open dense set (Proposition 4.3); (CL') on `Σ_π` at all but isolated points (Proposition 5.6); positivity of the Margenau-Hill form built from the state's cube-local symmetry, near the product point (Lemma 5.8).

**Open, by name.**
- **LW1-U_hop** (section 5.4): uniqueness of `O_1` on `Σ_π = {2 eps + mu = pi, 0 < mu < pi/2}`, the odd half-tick, where the gate is a pure hop. Three distinct attacks failed: (1) conditional independence given the finer shared field `(N_E, N_O)` fails at (CL'), false by Proposition 5.6; (2) the coupling built from the state's own cube-local symmetry fails at positivity, Lemma 5.8; (3) continuation from the solved product point fails for want of a quantitative estimate, since specific entropy is affine, the product point's structure is not stable (Lemma 5.3(ii), Proposition 5.6), and continuity alone cannot carry uniqueness (section 5.7). Its five-flavour form is open too (section 6).
- LW1-U_f for invariant factor states other than the free sea: not addressed.

**What changes downstream.**
- LW1: replace LW1-U_sea by LW1-U_hop in the open list; the free sea's transport is unique, and the identity, off `Σ_π`.
- TM1, VC1: the free vacuum's actual configuration is frozen off `Σ_π` (Corollary 3.3), in addition to forming no records (B8a).
- LW1-5: the free-sea row narrows the same way for `L5-O` and `L5-U`.
- Owner: two facts, no proposal: PS-3's transport is discontinuous at `a_o = pi/2`; at the free sea the greatest-entropy stage is idle.
- VC1: with `τ_E = 0`, the dressed half-steps satisfy `M_e U_0 M_e^* = U_0^T`; whether this reaches the gauged vacuum is open and not claimed.
