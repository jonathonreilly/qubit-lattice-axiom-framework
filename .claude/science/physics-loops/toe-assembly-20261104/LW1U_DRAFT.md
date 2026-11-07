# LW1-U, pass 1 (long draft): uniqueness of the PS-3 transport at infinite volume

- Written by: Claude Opus 5.5 subagent, pass 1 (Claude drafts; Codex distils; a fresh session referees). Not yet refereed. "Proved here" means written out in full in this file, not checked by another model.
- Date: 2026-11-04.
- Branch and commit read: `toe-assembly-local` at `f3f61bed4359f8cb28cd4e4246c13d7e753c540d` (same as `origin/claude/toe-assembly`).
- Sources read (all at that commit):
  - `LW1_DRAFT.md` (last changed in `f3f61bed43`): section 2 (C1-C5), 3.1 (Definition A1, Lemma A1a, Theorem A2), 5.4 (definitions, Lemma B6, Theorem B7, PS-3h, PS-3c), 5.5 (Theorem B10), 9.1-9.5 (Theorems E1-E6, Lemma LW1-U and its three attacks).
  - `TOE_ASSEMBLY.md` (last changed in `f3f61bed43`): section 3.2 (the adopted texts of PS-1c, PS-3h, PS-3c, PS-6r, PS-7r, PS-11c and the smuggle check).
- Not read: the audit ledger. No existing file was edited.
- Words: "[check]" marks a number from the scratch script `check_cube.py` (in the session scratchpad, not in the repo). It guides only. Nothing below depends on it.

---

## 0. The target, quoted

`LW1_DRAFT.md` section 9.5 states:

> "**Lemma LW1-U (outstanding).** *For the cube tick, PS-3h and a `2Z^3`-invariant state `omega_h` (in particular the PS-7r vacuum and its half-tick images), the set `O_h` of Theorem E6 has exactly one element, and it is the local limit of the unique torus transports of Theorem B7 on tori of side `L -> infinity` with states converging locally to `omega_h`.*"

`O_h` is defined in Theorem E6:

> "Let `C_h` be the set of `2Z^3`-invariant couplings of `mu_h, mu_{h+1}` that respect the cube supports. Let `dbar(pi) = (1/8) E_pi sum_{x in cell} 1[c_x != c'_x]` (changes per site) and `s(pi)` the specific entropy of `pi` (per cell, on the pair alphabet). Then `O_h = argmax_s argmin_dbar C_h` is a nonempty compact convex set."

The lemma claims uniqueness for every `2Z^3`-invariant state. The vacuum is named as a special case ("in particular"), not as the scope.

## 0.1 Outcome

**Counterexample (proved here).** LW1-U is false as stated. Theorem 4 builds a `2Z^3`-invariant, ergodic (but not factor) state of the free cube tick for which `O_h` is a whole segment `{t pi*_0 + (1 - t) pi*_1 : t in [0, 1]}` with `pi*_0 != pi*_1`. It works for every `(eps, mu)` in the window `0 <= mu < 2 eps < pi` at the even half-tick. The same construction works for the one-dimensional Margolus walk (section 5).

**What it rests on.** The state is a uniform mixture of four translates of a product state whose pattern has period 4 cells along `e_1`. Its Born law before the half-tick carries a hidden phase in `Z/2`, and its Born law after carries a hidden phase in `Z/4`. A coupling may match the two phases in two ways. Both ways have the same fewest-change cost and the same greatest entropy, by a four-line counting identity (Lemma 4.2). The PS-3 functionals see only averages of local statistics, so they cannot tell the two matchings apart.

**What it does not touch.** The vacuum. The mechanism needs a non-trivial invariant event of a sublattice in the Born law. A factor state (in particular any pure state, so the PS-7r vacuum and its half-tick images) has a Born law with trivial tail (Remark 6.1, credited to Powers), so it has no such event. Uniqueness for factor states is stated as Lemma LW1-U_f (section 6). It is open. This draft does not run attacks on it beyond the reductions of section 3.

**Proved positive cases (section 3).** (i) Every support-respecting coupling keeps each active cube's particle number. (ii) If the two Born laws are equal, `O_h` is the identity coupling alone. (iii) For ergodic Born laws, `O_h` is a singleton iff it has exactly one ergodic element. (iv) LW1-U holds in full (uniqueness and torus limit) for states that are products over the active cubes.

**Proposed specification.** PS-3m (section 8): the transport of a mixture of disjoint states is the mixture of the components' transports, each component carried to its own image. It restores one answer for the counterexample. It passes the smuggle check with one stated limit.

---

## 1. Literature, read first

What is known and used. Each item is credited; none is load-bearing. Every step used below is rebuilt in this file.

- **d-bar and rho-bar.** Minimising expected Hamming distance per site over stationary couplings ("joinings") of two stationary processes is Ornstein's d-bar distance (Ornstein 1973). Gray, Neuhoff and Shields (Ann. Probab. 3 (1975) 315-328) generalised it to the rho-bar distance with a single-letter cost. PS-3's first stage is a rho-bar problem with the single-cube cost `|sigma Δ sigma'|` on `S_C` and `+infinity` off it. Rüschendorf and Sei (Electron. J. Probab. 17 (2012), "On optimal stationary couplings between stationary processes") identify rho-bar with an optimal stationary coupling problem and solve classes of cases explicitly. A 2021 preprint (arXiv 2107.11858) treats an entropy-penalised optimal joining problem for finite alphabets; that is the nearest published object to PS-3's two-stage selection. A bounded search (2026-11-04) found no published result on uniqueness of optimal joinings or of greatest-entropy optimal joinings. So uniqueness is not available from the literature and is not assumed.
- **Joinings and ergodic decomposition.** Furstenberg (1967) introduced joinings; Glasner, "Ergodic theory via joinings" (2003), is the standard text. Used: ergodic decomposition, and the fact that an ergodic measure is extreme among invariant measures.
- **Specific entropy.** Existence by subadditivity, affinity, and the formula over ergodic decompositions (Jacobs; for `Z^d` see Georgii, "Gibbs Measures and Phase Transitions", 2nd ed. 2011, ch. 15). Only affinity over finite mixtures (proved in `LW1_DRAFT.md` Attack 1) and subadditivity are used in the counterexample.
- **Determinantal processes.** The vacuum's Born law is determinantal. Lyons and Steif (Duke Math. J. 2003) study stationary determinantal processes on `Z^d` (Bernoulli property, entropy). Orientation only; not used.
- **Factor states cluster.** Powers (Ann. Math. 1967) proved that a state of a UHF algebra is a factor state iff it has the uniform cluster property. Used only in Remark 6.1, which is not part of the counterexample.
- **Entropic optimal transport / Schrödinger bridges.** Léonard's survey (2014). The draft's Attack 3 already uses this form. Not used here.

## 2. Setting and notation

Fix a half-tick `h` and take its active tiling to be the even one (the odd case is the same with `beta` in place of `alpha`). Write cells by their index `k in Z^3`: the active cube is `C_k = 2k + {0,1}^3`. The cell translation `tau_v` (`v in Z^3`) acts on configurations by `(tau_v c)(x) = c(x + 2v)`, and on measures by image. "Invariant" means invariant under all `tau_v`, which is `2Z^3`-invariance in site units.

- Cube alphabet `Omega_C = {0,1}^8`; pair alphabet `Omega_C x Omega_C`. A configuration pair `(c, c')` is the same as a field of cube pairs `((c_{C_k}, c'_{C_k}))_k`.
- `S_C` = the cube support: pairs `(sigma, sigma')` with `<sigma'| G_C |sigma> != 0`, where `G_C = Gamma(u)` and `u = exp(-i alpha R_C) = cos alpha - i sin alpha R_C` on the cube's 8 corners (Definition A1 (5)). By Section 5.4 of `LW1_DRAFT.md` the support is the product `S = prod_k S_{C_k}`.
- Cost of cell `k`: `D_k(c, c') = |c_{C_k} Δ c'_{C_k}|`. For invariant `pi`, `dbar(pi) = (1/8) E_pi D_0`.
- For a subgroup `Gamma` of `Z^3` of finite index `d` with fundamental domain `F` (a set of `d` cells), a `Gamma`-invariant `pi` has cost `(1/(8d)) sum_{k in F} E_pi D_k` per site. Specific entropy per cell: `s(pi) = lim_n H_{Lambda_n}(pi)/|Lambda_n|`, with `Lambda_n = {0, ..., np - 1}^3` cells and `p` such that `pZ^3` lies in `Gamma` (`p = d` works). The limit exists by subadditivity (credited, standard). For `Gamma = Z^3` this is Theorem E6's `s`.
- **Single-cube problem.** For laws `P, Q` on `Omega_C`, let `Pi(P, Q; S_C)` be the couplings of `P` and `Q` carried by `S_C`. When it is nonempty: `kappa(P, Q)` = its least expected cost; `F(P, Q)` = the face of least-cost couplings; `lambda*(P, Q)` = the unique element of greatest entropy in `F(P, Q)` (Theorem B7 applied to one cube); `H*(P, Q) = H(lambda*(P, Q))`. If `P` and `Q` are the Born laws of a cube state `rho` and of `u rho u^*` (on the cube's Fock space), the set is nonempty by Lemma B6.

Two finite-mixture bounds are used repeatedly. For laws `nu_1, ..., nu_r` on a finite set and weights `w_i`: `sum w_i H(nu_i) <= H(sum w_i nu_i) <= sum w_i H(nu_i) + log r`. The left inequality is concavity of `H`. The right one is `H(X) <= H(X, T) = H(T) + H(X | T)` with `T` the mixing label (as in `LW1_DRAFT.md` Attack 1).

---

## 3. Structural facts (proved here)

**Lemma 3.1 (cube numbers are kept).** Let `N_k(c)` be the number of particles of `c` in `C_k`. Every support-respecting coupling `pi` has `N_k(c) = N_k(c')` for every `k`, `pi`-almost surely. The law of the field `(N_k)_k` is the same under `mu_h` and `mu_{h+1}`.

*Proof.* `G_C` is the Fock lift of a one-body unitary, so it commutes with the cube number operator `N_C`. The projector `P_sigma` is an eigenprojector of `N_C` with eigenvalue `N(sigma)`. So `P_{sigma'} G_C P_sigma = P_{sigma'} P_{N(sigma)} G_C P_sigma`, where `P_n` projects on `N_C = n`, and this is `0` when `N(sigma') != N(sigma)`. Hence `S_C` only contains pairs with equal numbers, and a coupling carried by `S` keeps every `N_k`. For the second claim: the active half-tick `beta` fixes each `N_C` (the gate of `C` commutes with it, and the other gates act on disjoint modes and are even). So for any function `f` of finitely many `N_k`, `omega_{h+1}(f) = omega_h(beta(f)) = omega_h(f)`. ∎

So a support-respecting coupling only moves particles inside cubes, and the PS-3 problem is to couple the within-cube configurations given the common number field. This was a lead in the brief; it holds.

**Lemma 3.2 (equal Born laws).** Assume `cos alpha != 0` (true in the window `0 <= mu < 2 eps < pi`, where `alpha = eps - mu/2` lies in `(0, pi/2)`). If `mu_{h+1} = mu_h`, then `O_h` is the single diagonal coupling `pi(dc, dc') = mu_h(dc) delta_c(dc')`.

*Proof.* For a cube configuration `sigma` with occupied set `A`, `<sigma|Gamma(u)|sigma> = det(u_{AA})`, the principal minor of `u` on `A` (the standard Slater-determinant formula for matrix elements of a Fock lift; for `A` empty it is `1`). `u_{AA} = cos alpha I - i sin alpha R_{AA}`, and `R_{AA}` is real symmetric with real eigenvalues `r_j`. So `det(u_{AA}) = prod_j (cos alpha - i sin alpha r_j)`, and each factor has real part `cos alpha != 0`. So every pair `(sigma, sigma)` is in `S_C`, and the diagonal coupling is in `C_h` with `dbar = 0`. A coupling with `dbar = 0` has `c = c'` almost surely, so it is the diagonal coupling. Hence the set of least-cost couplings is this one point, and so is `O_h`. ∎

This is the brief's degenerate case. It holds. (At the odd half-tick with `beta = eps + mu/2 = pi/2`, `cos beta = 0`; then `<sigma|G|sigma> = (-i)^{|A|} det(R_{AA})`, which is `0` for a single particle, and the lemma does not apply.)

**Lemma 3.3 (tiling lemma).** Let `Gamma` have index `d`, fundamental domain `F`, and let `nu` be a `Gamma`-invariant law on `(Omega_C x Omega_C)^{Z^3}` with cell laws `nu_k`. Then `s(nu) <= (1/d) sum_{k in F} H(nu_k)`, with equality iff `nu` is the product of its cell laws.

*Proof.* Choose `p` with `pZ^3` in `Gamma`. Every box `B = {0, ..., mp - 1}^3` meets each `Gamma`-class of cells in exactly `|B|/d` cells, because it is a union of translates of `{0, ..., p-1}^3` by `pZ^3`, and each such translate meets each class `p^3/d` times. Write `hbar = (1/d) sum_{k in F} H(nu_k)`. Subadditivity of `H` gives `H_{Lambda_n}(nu) <= sum_{k in Lambda_n} H(nu_k) = |Lambda_n| hbar`, so `s(nu) <= hbar`. If `nu` is the product of its cell laws, `H_{Lambda_n} = |Lambda_n| hbar` exactly and `s = hbar`. If it is not, some finite set of cells has a joint law that is not the product of its cell laws, and that set lies in some box `B` of the form above. Equality in subadditivity holds iff the variables are independent (chain rule: `H(X_1, ..., X_m) = sum H(X_i | X_1, ..., X_{i-1})`, and `H(X_i | Y) = H(X_i)` iff `X_i` is independent of `Y`). So `H_B(nu) = |B| hbar - g` with `g > 0`. For `n` a multiple of `m`, `Lambda_n` is the disjoint union of `|Lambda_n|/|B|` translates of `B` by vectors of `mpZ^3`, which lie in `Gamma`, so each translate has entropy `H_B(nu)`. Subadditivity over these translates gives `H_{Lambda_n} <= |Lambda_n| (hbar - g/|B|)`, so `s(nu) <= hbar - g/|B| < hbar`. ∎

**Theorem 3.4 (LW1-U holds for active-cube product states).** Let `omega_h` be a product, over the active cubes, of even cube states `rho_k` with `rho_{k+g} = rho_k` for all `g` in a finite-index `Gamma`. Let `O_h(Gamma)` be the PS-3 selection among `Gamma`-invariant support-respecting couplings (cost and entropy per cell as in section 2). Then `O_h(Gamma)` is the single coupling `pi* = ⊗_k lambda*(P_k, Q_k)`, where `P_k` and `Q_k` are the Born laws of `rho_k` and `u rho_k u^*`. For `Gamma = Z^3` (all `rho_k` equal) this is LW1-U for these states, including its torus clause for the tori of side `L` (a multiple of the period) carrying the same product state.

*Proof.* The Born law of a product of even states is the product of the cube Born laws (even states on a graded tensor product factorise on products of even operators, and the `P_sigma` are even). The half-tick maps the product state to the product of the `u rho_k u^*`. So `mu_h = ⊗ P_k` and `mu_{h+1} = ⊗ Q_k`. The product `pi*` has these marginals, is carried by `S`, and is `Gamma`-invariant. Let `pi` be any `Gamma`-invariant support-respecting coupling, with cell laws `lambda_k`. Each `lambda_k` lies in `Pi(P_k, Q_k; S_C)`, so `E_pi D_k >= kappa(P_k, Q_k)`, with equality for `pi*`. So `pi*` has least cost, and a least-cost `pi` has every `lambda_k` in `F(P_k, Q_k)`, hence `H(lambda_k) <= H*(P_k, Q_k)` with equality iff `lambda_k = lambda*(P_k, Q_k)`. By Lemma 3.3, `s(pi) <= (1/d) sum_{k in F} H(lambda_k) <= (1/d) sum_{k in F} H*(P_k, Q_k) = s(pi*)`. Equality forces `pi` to be a product (Lemma 3.3) with cell laws `lambda*`, i.e. `pi = pi*`. On a torus the same chain of inequalities holds with finite sums in place of limits (subadditivity, with equality iff product), so the unique torus transport of Theorem B7 is the torus product of the same `lambda*`. Its restriction to any finite set of cells equals that of `pi*` once the torus contains the set. ∎

**Lemma 3.5 (ergodic reduction).** If `mu_h` and `mu_{h+1}` are ergodic (for the cell translations), then the ergodic components of any element of `O_h` lie in `O_h`. Hence `O_h` is a singleton iff it has exactly one ergodic element.

*Proof.* Let `pi = ∫ pi_xi dnu(xi)` be the ergodic decomposition of `pi` in `O_h` (credited, standard). The first marginals `(pi_xi)_1` are invariant and integrate to `mu_h`. An ergodic measure is extreme among invariant measures, and this excludes non-trivial integral decompositions too: if `(pi_xi)_1(f) > mu_h(f) + r` on a set `B` of `xi` of positive measure for some cylinder function `f` and rational `r > 0`, then `mu_h = nu(B) m_B + nu(B^c) m_{B^c}` with `m_B = nu(B)^{-1} ∫_B (pi_xi)_1 dnu` invariant and different from `mu_h`, a contradiction. Countably many `(f, r)` suffice, so `(pi_xi)_1 = mu_h` for almost every `xi`; likewise for the second marginal. `pi(S^c) = 0` gives `pi_xi(S^c) = 0` for almost every `xi`. So almost every `pi_xi` is in `C_h`. `dbar` is affine and continuous, so `dbar(pi) = ∫ dbar(pi_xi)`; each term is at least the minimum, and the integral equals it, so almost every `pi_xi` has least cost. Specific entropy satisfies `s(pi) = ∫ s(pi_xi)` (Jacobs' theorem; credited, standard, e.g. Georgii 2011, ch. 15). The same argument puts almost every `pi_xi` in `O_h`. If `O_h` had one ergodic element `e`, every element of `O_h` would be `∫ e dnu = e`. ∎

Lemma 3.5 is not used in the counterexample. It says what a counterexample with ergodic Born laws must look like: two distinct ergodic optimisers. The counterexample of section 4 has ergodic Born laws, and its two optimisers `pi*_0`, `pi*_1` are each ergodic (each is the orbit average of a product measure under a finite-index sublattice; the argument of Lemma 4.1 (ii) shows such averages are ergodic).

---

## 4. The counterexample (proved here)

### 4.1 Four cube states

Let `H_1` be the one-particle space of an active cube (span of the 8 corners `|z>`). On it the gate acts as the one-body `u = cos alpha - i sin alpha R_C`. A density matrix `rho` on `H_1` defines a state of the cube's CAR algebra carried by the sector `N_C = 1`. It is even: an odd operator maps that sector into `N_C = 0` or `N_C = 2`, so its expectation is `0`.

Fix the cube edge from `x = 2k` to `y = 2k + e_1` (the corner `(0,0,0)` and its `e_1` neighbour). Its hop weight is `R_{xy} = eta_1(x)/sqrt3 = 1/sqrt3` (Definition A1 (3), (4)). Put

- `Y = i(|x><y| - |y><x|)`, `X = u^* Y u`, `delta = 1/32`,
- `rho_{ab} = I/8 + delta((-1)^a X + (-1)^b Y)` for `a, b in {0, 1}`,
- `P_a` = the corner law of `rho_{ab}` (its diagonal), `Q_b` = the corner law of `u rho_{ab} u^*`.

**Lemma 4.0.** Assume `sin 2alpha != 0` (true in the window: `alpha` lies in `(0, pi/2)`).
(i) Each `rho_{ab}` is a density matrix.
(ii) `P_a` depends only on `a`, and `Q_b` depends only on `b`.
(iii) `P_a(x) = 1/8 + (-1)^a delta sin(2alpha)/sqrt3` and `Q_b(x) = 1/8 - (-1)^b delta sin(2alpha)/sqrt3`. So `P_0 != P_1` and `Q_0 != Q_1`.
(iv) `P_a = Q_{1-a}`.

*Proof.* (i) `Y` is Hermitian with eigenvalues `1, -1, 0`, so `||Y|| = ||X|| = 1` and both are traceless. So `rho_{ab}` is Hermitian, has trace 1, and `rho_{ab} >= (1/8 - 2 delta) I > 0`.
(ii) `diag Y = 0`, so `diag rho_{ab} = 1/8 + (-1)^a delta diag X`. Also `u rho_{ab} u^* = I/8 + delta((-1)^a Y + (-1)^b u Y u^*)`, so its diagonal is `1/8 + (-1)^b delta diag(u Y u^*)`.
(iii) For any `z`, `(u Y u^*)_{zz} = i u_{zx} conj(u_{zy}) - i u_{zy} conj(u_{zx}) = -2 Im(u_{zx} conj(u_{zy}))`. At `z = x`: `u_{xx} = cos alpha` (`R` has zero diagonal) and `u_{xy} = -i sin alpha R_{xy}`, so `u_{xx} conj(u_{xy}) = i cos alpha sin alpha R_{xy}` and `(u Y u^*)_{xx} = -sin(2alpha) R_{xy}`. The same computation with `u^* = cos alpha + i sin alpha R` gives `(u^* Y u)_{xx} = +sin(2alpha) R_{xy}`. Insert `R_{xy} = 1/sqrt3`.
(iv) `R` is real symmetric, so `u^T = u` and `u^* = conj(u)` entrywise. Then `(u^* Y u)_{zz} = sum_{m,n} conj(u_{zm}) Y_{mn} u_{zn} = conj( (u conj(Y) u^*)_{zz} ) = (u conj(Y) u^*)_{zz}` (a diagonal entry of a Hermitian matrix is real), and `conj(Y) = -Y`. So `diag X = -diag(u Y u^*)`, which is (iv). ∎

[check: at `(eps, mu) = (0.3, 0.1)`, `(u Y u^*)_{xx} = -0.276796` against `-sin(2 alpha)/sqrt3 = -0.276796`; `||P_0 - P_1||_1 = ||Q_0 - Q_1||_1 = 0.0346`.]

Each pair `(P_a, Q_b)` is the Born pair of `rho_{ab}` and `u rho_{ab} u^*`, so `Pi(P_a, Q_b; S_C)` is nonempty (Lemma B6), and `kappa`, `lambda*`, `H*` are defined for all four pairs. Put `K = sum_{a,b} kappa(P_a, Q_b)` and `S = sum_{a,b} H*(P_a, Q_b)`. By (iv) and Lemma 3.2's argument, `kappa(P_a, Q_{1-a}) = 0`. [check: `kappa(P_a, Q_a) = 0.0346` changes per cube.] The values of `K` and `S` play no role below; only their independence of the phases does.

### 4.2 The state

Let `a(n) = n mod 2` and `b(n) = floor(n/2) mod 2` for `n in Z`; `a` has period 2 and `b` has period 4 (`b` runs `0, 0, 1, 1`). For `t in Z/4` let `omega^(t)` be the product, over all active cubes `C_k`, of the cube states `rho_{a(k_1 + t), b(k_1 + t)}`. A product of even states on the graded tensor product is a well-defined state (credited, standard). Put

`omega_h = (1/4) (omega^(0) + omega^(1) + omega^(2) + omega^(3))`.

The cell translations `tau_{e_2}`, `tau_{e_3}` fix each `omega^(t)` (the pattern depends on `k_1` only), and `tau_{e_1}` maps `omega^(t)` to `omega^(t+1)` or `omega^(t-1)` (one fixed direction; write it `t -> t + 1`). So `omega_h` is `2Z^3`-invariant. It is a state of the free cube tick's algebra; it is in the scope of LW1-U.

### 4.3 Its Born laws

For `i in Z/2` and `l in Z/4` let `m_i = ⊗_k P_{a(k_1 + i)}` and `m'_l = ⊗_k Q_{b(k_1 + l)}` (product measures over cells). Let `Gamma_4 = 4Z x Z x Z` (cells).

**Lemma 4.1.**
(i) `mu_h = (1/2)(m_0 + m_1)` and `mu_{h+1} = (1/4) sum_{l in Z/4} m'_l`. The translation `t -> t + 1` maps `m_i` to `m_{i+1}` and `m'_l` to `m'_{l+1}`.
(ii) Each `m_i` and each `m'_l` is `Gamma_4`-ergodic, and `mu_h`, `mu_{h+1}` are ergodic for the cell translations.
(iii) There are maps `phi` (defined `mu_h`-a.s., values in `Z/2`) and `phi'` (defined `mu_{h+1}`-a.s., values in `Z/4`) with `m_i(phi = i) = 1` and `m'_l(phi' = l) = 1`, and with `phi o tau_g = phi`, `phi' o tau_g = phi'` almost surely for `g` in `Gamma_4`.

*Proof.* (i) The Born law (C3) is linear in the state. The Born law of `omega^(t)` is the product of the cube Born laws, `m_{t mod 2}` (as in Theorem 3.4). The half-tick maps `omega^(t)` to the product of the states `u rho u^*`, whose Born law is `m'_t`. Average over `t`.
(ii) Group the cells into blocks of 4 consecutive cells along `e_1`, one block per element of `Gamma_4`. Under `m_i` the blocks are independent and identically distributed, so `Gamma_4` acts on `m_i` as a Bernoulli shift, which is mixing and so ergodic (credited, standard). Same for `m'_l`. If `E` is invariant under all cell translations, it is `Gamma_4`-invariant, so `m_0(E)` is `0` or `1`, and `m_1(E) = m_0(E)` because the translation `t -> t + 1` maps `m_0` to `m_1` and fixes `E`. So `mu_h(E)` is `0` or `1`. Same for `mu_{h+1}`.
(iii) Let `e` be the cube event "corner `x` occupied"; `P_0(e) != P_1(e)` by Lemma 4.0 (iii). For a configuration `c` let `L(c) = lim_N (1/N) sum_{n < N} 1_e(c on C_{2n e_1})` where the limit exists. Under `m_i` these indicators are independent with mean `P_{a(2n + i)}(e) = P_i(e)`, so by Kolmogorov's strong law (bounded independent variables; credited, standard) `L = P_i(e)` almost surely. Set `phi(c) = i` when `L(c) = P_i(e)`. Shifting the averaging line by `e_2` or `e_3`, or the index by two steps (a shift by `4e_1`), gives the same limit almost surely (the same strong law on the shifted line; a Cesàro limit ignores finitely many terms). For `phi'` use the four averages along the cells `(4n + r) e_1`, `r = 0, 1, 2, 3`, of the event `e' =` "corner `x` occupied" (`Q_0(e') != Q_1(e')`); under `m'_l` they converge to `Q_{b(r + l)}(e')`, and the word `(b(l), b(l+1), b(l+2), b(l+3))` determines `l` mod 4 because the four cyclic shifts of `0, 0, 1, 1` are distinct. ∎

Since `m_{1-i}(phi = i) = 0`, `mu_h` restricted to `{phi = i}` is `(1/2) m_i`, and `mu_{h+1}` restricted to `{phi' = l}` is `(1/4) m'_l`.

### 4.4 The counting identity

**Lemma 4.2.** For every `i in Z/2` and `l in Z/4`, the map `n -> (a(n + i), b(n + l))` from `Z/4` to `{0,1}^2` is a bijection.

*Proof.* `a(n + i)` depends on `n` mod 2, so the map is well defined on `Z/4`. `b(n + l) = 0` exactly for the two values `n = -l, 1 - l` (mod 4). They are consecutive, so they have opposite parity, and `a(n + i)` takes the value `0` at one and `1` at the other. The same holds for `b(n + l) = 1` at `n = 2 - l, 3 - l`. So the four values of `n` give the four pairs. ∎

So every way of matching the phases sees each of the four cube problems `(P_a, Q_b)` exactly once per period. This is the whole mechanism.

### 4.5 The theorem

**Theorem 4.3 (LW1-U fails).** For the free cube tick with `0 <= mu < 2 eps < pi`, the even half-tick, and the `2Z^3`-invariant ergodic state `omega_h` of section 4.2:
(i) the least cost over `C_h` is `E D_0 = K/4` changes per cell (`dbar = K/32`);
(ii) the greatest specific entropy among least-cost couplings is `S/4` per cell;
(iii) for `j in {0, 1}`, let `rho_j = ⊗_k lambda*(P_{a(k_1)}, Q_{b(k_1 + j)})` and let `pi*_j` be the average of the four translates of `rho_j` by `0, 1, 2, 3` steps of `tau_{e_1}`; then `pi*_j` is in `O_h`;
(iv) `pi*_0 != pi*_1`;
(v) `O_h = {t pi*_0 + (1 - t) pi*_1 : t in [0, 1]}`.
So `O_h` does not have exactly one element, and Lemma LW1-U is false as stated.

*Proof.* *Step 1 (split by phases).* Let `pi` be in `C_h`. Its marginals are `mu_h` and `mu_{h+1}`, so `phi(c)` and `phi'(c')` are defined `pi`-a.s. Let `A_{il} = {phi(c) = i, phi'(c') = l}` and `w_{il} = pi(A_{il})`; the eight sets cover the pair space up to a null set. By Lemma 4.1 (iii) each `A_{il}` is `Gamma_4`-invariant up to a null set, and `pi` is invariant, so the restriction `pi|A_{il}` is `Gamma_4`-invariant. Its first marginal `nu` is `Gamma_4`-invariant and `nu <= mu_h|{phi = i} = (1/2) m_i`. The density `d nu / d m_i` is then `Gamma_4`-invariant, hence constant `m_i`-a.s. by ergodicity, so `nu = w_{il} m_i`. In the same way its second marginal is `w_{il} m'_l`. For `w_{il} > 0` put `pi_{il} = pi|A_{il} / w_{il}`: a `Gamma_4`-invariant coupling of `m_i` and `m'_l`, carried by `S`. And `pi = sum_{il} w_{il} pi_{il}`.

*Step 2 (cost bound).* By invariance under `tau_{e_1}`, `E_pi D_0 = (1/4) sum_{n=0}^{3} E_pi D_{n e_1} = (1/4) sum_{il} w_{il} sum_{n=0}^{3} E_{pi_{il}} D_{n e_1}`. Under `pi_{il}` the cell law at `n e_1` is a coupling of `P_{a(n+i)}` and `Q_{b(n+l)}` carried by `S_C`, so its cost is at least `kappa(P_{a(n+i)}, Q_{b(n+l)})`. By Lemma 4.2 the sum over `n` of these lower bounds is `K` for every `(i, l)`. So `E_pi D_0 >= K/4`.

*Step 3 (entropy bound).* Let `pi` have `E_pi D_0 = K/4`. Then every inequality of Step 2 is an equality: for each `(i, l)` with `w_{il} > 0` and each `n`, the cell law `lambda^{il}_n` lies in `F(P_{a(n+i)}, Q_{b(n+l)})`, so `H(lambda^{il}_n) <= H*(P_{a(n+i)}, Q_{b(n+l)})`. The right mixture bound (section 2) gives `H_{Lambda_m}(pi) <= sum_{il} w_{il} H_{Lambda_m}(pi_{il}) + log 8`; divide by `|Lambda_m|` and let `m` grow: `s(pi) <= sum_{il} w_{il} s(pi_{il})`. Lemma 3.3 with `Gamma = Gamma_4` and fundamental domain `{0, e_1, 2e_1, 3e_1}` gives `s(pi_{il}) <= (1/4) sum_n H(lambda^{il}_n) <= (1/4) sum_n H*(P_{a(n+i)}, Q_{b(n+l)}) = S/4`, the last step by Lemma 4.2. So `s(pi) <= S/4`.

*Step 4 (`pi*_j` attains both bounds).* `rho_j` is a product of couplings carried by `S_C`, so it is carried by `S`. Its marginals are `m_0` and `m'_j`. It is `Gamma_4`-invariant (its cell laws depend on `k_1` mod 4 only). Its translate by `t` steps has marginals `m_{t mod 2}` and `m'_{j+t}` (Lemma 4.1 (i)). So `pi*_j` has marginals `(1/4) sum_t m_{t mod 2} = mu_h` and `(1/4) sum_t m'_{j+t} = mu_{h+1}`, is carried by `S`, and is invariant (`tau_{e_1}` permutes the four terms because `tau_{4e_1}` fixes `rho_j`; `tau_{e_2}`, `tau_{e_3}` fix each term). So `pi*_j` is in `C_h`. Each term attains `kappa` in every cell, so the computation of Step 2 gives `E D_0 = K/4`. Each term is a product with cell laws `lambda*`, so for boxes `Lambda_m` of side a multiple of 4, `H_{Lambda_m}(term) = sum_{cells} H(lambda*) = |Lambda_m| S/4` (Lemma 4.2 on each line along `e_1`). The left mixture bound gives `H_{Lambda_m}(pi*_j) >= |Lambda_m| S/4`, so `s(pi*_j) >= S/4`. With Steps 2 and 3, `pi*_j` attains the least cost and, among least-cost couplings, the greatest entropy: `pi*_j` is in `O_h`. This also proves (i) and (ii).

*Step 5 (distinct).* Let `E_0 = {phi'(c') - phi(c) = 0 mod 2}`. Under the `t`-th term of `pi*_j`, `phi = t mod 2` and `phi' = j + t mod 4` almost surely, so `phi' - phi = j mod 2`. Hence `pi*_0(E_0) = 1` and `pi*_1(E_0) = 0`. Two distinct probability measures on the pair space also differ on some cylinder event (cylinder events determine a measure), so `pi*_0` and `pi*_1` give different probabilities to some event that names finitely many sites at half-ticks `h` and `h+1`.

*Step 6 (the whole set).* Let `pi` be in `O_h`. Then `s(pi) = S/4`, so every inequality of Step 3 is an equality: for each `(i, l)` with `w_{il} > 0`, `s(pi_{il}) = (1/4) sum_n H(lambda^{il}_n)` and `H(lambda^{il}_n) = H*`. By Lemma 3.3 (equality case) `pi_{il}` is the product of its cell laws, and by uniqueness of `lambda*` (Theorem B7 on one cube) those are `lambda*(P_{a(n+i)}, Q_{b(n+l)})`. So `pi_{il} = rho_{il}`, the product coupling of `m_i` and `m'_l` with these cell laws. The translation `t -> t + 1` maps `A_{il}` to `A_{i+1, l+1}` up to null sets (it maps `m_i` to `m_{i+1}` and `m'_l` to `m'_{l+1}`), so invariance of `pi` gives `w_{il} = w_{i+1, l+1}`. The orbits of `(i, l) -> (i+1, l+1)` on `Z/2 x Z/4` are the two classes `l - i = 0` and `l - i = 1` mod 2, each with four elements. The four `rho_{il}` of class `j` are exactly the four translates of `rho_j`. So `pi = 4 w_0 pi*_0 + 4 w_1 pi*_1` with `4 w_0 + 4 w_1 = 1`. Conversely every such mixture is in `O_h`, since `O_h` is convex (Theorem E6). ∎

**Remarks.**
1. *Which element follows the state.* The quantum state locks the phases: `omega^(t)` has Born law `m_{t mod 2}` and its image has Born law `m'_t`, so `phi' - phi = 0`. The element that carries each component to its own image is `pi*_0`. `pi*_1` couples configurations typical of `omega^(t)` with configurations typical of the images of `omega^(t+1)` and `omega^(t-1)`. PS-3 cannot see this: its data are the two Born laws and the supports, not the locking.
2. *Parameters.* The proof uses only `sin 2 alpha != 0` (Lemma 4.0) and Lemma B6. It holds at the even half-tick for every `(eps, mu)` in the window. At the odd half-tick it holds when `sin 2 beta != 0`.
3. *The torus clause.* On tori of side `4M` cells along `e_1` with the torus versions of `omega_h`, the torus transports are unique (Theorem B7). Whatever they do as `M` grows, the first clause of LW1-U fails. On a finite torus the four components are not mutually singular, so the torus problem cannot follow the components exactly; this draft does not compute which point of the segment, if any, the torus transports approach.
4. *The gauged law.* With link registers in a product state that is a joint eigenstate of all link variables `U_l` (as in `LW1_DRAFT.md` section 9.2's rotor remark), the dressed gates act on matter as the free gates and the same construction applies. Not written out.
5. *Ergodic, not factor.* `omega_h` is an ergodic invariant state (its Born laws are ergodic; the state is the orbit average of a `Gamma_4`-ergodic product state). It is not a factor state: it is a mixture of four mutually disjoint product states, which the macroscopic observable `phi` tells apart.

---

## 5. The one-dimensional analogue

The brief asked for the Margolus walk on `Z` first. The same construction works, with smaller numbers; it is written here as a check on the three-dimensional proof.

Sites `Z`, one mode per site. Even blocks `{2k, 2k+1}`, odd blocks `{2k+1, 2k+2}`. Even gate `Gamma(u)`, `u = cos alpha - i sin alpha sigma_x` on the block. Take every block in its one-particle sector: a qubit with basis `|L>` (particle at `2k`) and `|R>` (particle at `2k+1`). With `Y = i(|L><R| - |R><L|)`, `X = u^* Y u`, `delta = 1/8` and `rho_{ab} = I/2 + delta((-1)^a X + (-1)^b Y)`, Lemma 4.0 holds with `R_{LR} = 1`: `P_a(L) = 1/2 + (-1)^a delta sin 2alpha` and `Q_b(L) = 1/2 - (-1)^b delta sin 2alpha`. The block support contains all four transitions of the qubit when `sin 2 alpha != 0`. The single-block problems are explicit: for `a != b`, `P_a = Q_b` and `lambda*` is the diagonal coupling (cost 0); for `a = b`, the least cost is `2 |P_a(L) - Q_a(L)| = 4 delta |sin 2 alpha|` changes per block, attained only by the monotone coupling (a binary coupling with `P(X != Y) = |P(X = L) - P(Y = L)|` is unique). With blocks in place of cubes and `k_1` replaced by the block index, sections 4.2-4.5 hold word for word. So LW1-U fails for the Margolus walk too, at an ergodic invariant state that is a mixture of four period-4 product states.

---

## 6. What the counterexample needs, and the vacuum

The proof of Theorem 4.3 used one thing beyond local data: a non-trivial `Gamma_4`-invariant event in each Born law (the phase maps `phi`, `phi'`). Factor states have no such event.

**Remark 6.1 (factor states have tail-trivial Born laws; sketched, credited).** Let `omega` be a factor state of `A(Z^3)` (for instance a pure state). Then its Born law `mu` has a trivial tail sigma-field. Hence, for every finite-index `Gamma`, every `Gamma`-invariant event has `mu`-probability `0` or `1` (invariant events agree with tail events up to null sets; credited, standard), and no phase map with two values of positive probability exists.

*Sketch.* Enumerate the sites. The Jordan-Wigner map along the enumeration is an isomorphism of `A(Z^3)` onto the UHF algebra of a qubit chain. An even monomial in modes beyond position `N` maps into the chain algebra beyond `N`: each string factor `prod_{m < n} sigma^z_m` appears an even number of times, the `sigma^z_m` at `m < N` commute with everything beyond `N`, and `(sigma^z)^2 = 1`. The Born projectors are even. Being a factor state is preserved by the isomorphism. Powers' theorem (1967): a state of a UHF algebra is a factor state iff for every `A` and `epsilon > 0` there is `N` with `|omega(AB) - omega(A) omega(B)| <= epsilon ||B||` for all `B` beyond `N`. Let `T` be a tail event and `A` a cylinder event. For each `N`, `T` is measurable with respect to the sites beyond `N`, so there are cylinder events `B_r` beyond `N` with `mu(B_r Δ T) -> 0`. Then `|mu(A ∩ T) - mu(A) mu(T)| <= epsilon`. So `T` is independent of every cylinder event, hence of itself, and `mu(T)` is `0` or `1`. ∎

Every pure state is a factor state (its GNS representation is irreducible). The PS-7r vacuum `omega_P` is pure (Theorem B10 (iv), Powers-Størmer), and its half-tick images are pure (images under automorphisms). So the mechanism of section 4 is not available at the vacuum.

**Lemma LW1-U_f (open).** *For the cube tick, PS-3h, and a `2Z^3`-invariant factor state `omega_h` (in particular every pure invariant state, hence the PS-7r vacuum and its half-tick images), the set `O_h` of Theorem E6 has exactly one element, and it is the local limit of the unique torus transports on tori of side `L -> infinity` with states converging locally to `omega_h`.*

Status: open. This draft ran no attack on LW1-U_f beyond the reductions of section 3. What is known about it:
- By Lemma 3.1 a counterexample must couple the within-cube configurations differently for the same number field.
- Factor states have tail-trivial, hence ergodic, Born laws, so by Lemma 3.5 LW1-U_f is equivalent to: `O_h` has exactly one ergodic element.
- Tail triviality of both marginals excludes the phase-matching mechanism of section 4. This draft knows no theorem, in either direction, on whether tail-trivial marginals force a unique greatest-entropy optimal joining. The bounded literature search found none.
- Theorem 3.4 proves LW1-U_f for invariant product states over the active cubes. It does not cover the vacuum, whose Born law is determinantal and not a product over cubes.

---

## 7. What this changes for LW1

- Theorems E4, E5 and E6 of `LW1_DRAFT.md` stand: transports exist at infinite volume, and `O_h` is nonempty, compact and convex.
- Lemma LW1-U is false as stated (Theorem 4.3). Section 9.5's sentence "If false, the owner must choose among: ..." applies. Its first option, the torus-limit tie-break, is not settled by this draft (Remark 3 after Theorem 4.3): the torus transports are unique, but whether they converge, and to which point of the segment, is not computed. Its second option (restrict readable statistics) would have to cover finite two-time statistics: by Theorem 4.3 (iv), `pi*_0` and `pi*_1` differ on an event naming finitely many sites at half-ticks `h` and `h+1`.
- The Qualification, as `LW1_DRAFT.md` section 9.4 quotes it ("at every state where the condition holds it gives exactly one answer"), fails for PS-3 alone at the state of section 4. The PS-3 selection there gives a segment of transports.
- The failure is at a non-factor state. For the vacuum the question is LW1-U_f, which is open.
- Two ways forward are on file below: add PS-3m (section 8), which gives one answer at the counterexample and at every mixture of periodic factor states, and leaves LW1-U_f; or leave PS-3 as is and record that its transport is fixed only up to the face `O_h` at non-factor states.

---

## 8. Proposed specification

**Proposed specification PS-3m (transport of a mixture).**
> "If the state at a half-tick is not a factor state, its transport is the mixture, over the state's central decomposition, of the transports of its factor components. The transport of a component couples that component's Born law with the Born law of its own image under the half-tick, and it is selected as in PS-3 among the couplings invariant under the cell translations that leave the component invariant."

*Reasons.*
1. Theorem 4.3: without a further rule, PS-3 gives a segment of transports at a `2Z^3`-invariant state, and the elements differ on finite two-time events.
2. Disjoint components are told apart by the actual configuration. In section 4 the component is read off from limits of frequencies (the phase `phi`), which are statements of PS-11c item (2). So "which component" is a fact of the realized history at each half-tick. The update maps each component to its own image (an automorphism maps the central decomposition of a state to that of its image). PS-3m makes the actual configuration follow the odds' own map of components. Without it, PS-3 allows `pi*_1`, which pairs configurations typical of one component with configurations typical of the image of another.
3. Under PS-3m the state of section 4 has one transport, `pi*_0`: each component `omega^(t)` is a `Gamma_4`-invariant product state, and Theorem 3.4 with `Gamma = Gamma_4` gives it one transport, the translate of `rho_0`. Their average is `pi*_0`.
4. At a factor state PS-3m says nothing. So it changes nothing at the vacuum, and nothing a part has proved about the vacuum.

*Limits, stated.* (a) If the factor components are invariant under no finite-index lattice of cell translations (possible for an ergodic invariant state, for example with incommensurate components), PS-3's per-site selection is not defined for them, and PS-3m gives no answer. (b) PS-3m reduces uniqueness to uniqueness at factor states: LW1-U_f for invariant factor states, and its analogue for factor states invariant under a finite-index sublattice.

*Smuggle check (the four tests of `TOE_ASSEMBLY.md` section 3.2).*
1. *Does it state or fix a part's target?* No part lists the transport of a mixed state as its target. TM1 supplies `omega_0`; PS-3m does not choose it. Pass.
2. *Is it open-ended?* No. The text is fixed and has no list a part could extend. Pass.
3. *Does it settle a downstream physics question by premise?* It fixes that the actual history of a mixture of disjoint states stays in one component's image at every half-tick. That is a statement about the transport, which PS-3 owns; it is not a statement about the vacuum, records, frequencies or the arrow. One note for the owner: if TM1 or BR1 wants to derive "macroscopic labels persist" from the dynamics, PS-3m would supply it by premise. Pass, with that note.
4. *Does it add structure its reasons do not need?* It uses the central decomposition (needed to say "component") and the stabiliser sublattice of a component (needed because components have fewer symmetries than the state; the counterexample's components are only `Gamma_4`-invariant). It adds no constant. Pass.

*Alternatives on file.* (A) No new rule: record that at non-factor states PS-3 fixes the transport only up to the face `O_h`, and accept that the Qualification then holds only for statements common to all of `O_h`. (B) The torus-limit rule of `LW1_DRAFT.md` section 9.5, which still needs the limit to exist. This draft gives no evidence for (B) at the counterexample: on finite tori the components overlap, so there is no reason the limit is `pi*_0`.

---

## 9. Status (FINISH block)

```
LEMMA:      LW1-U (LW1_DRAFT.md section 9.5), as stated for all 2Z^3-invariant states.
OUTCOME:    COUNTEREXAMPLE, proved here (pass 1; not refereed).
            Theorem 4.3: free cube tick, any (eps, mu) with 0 <= mu < 2 eps < pi, even
            half-tick; omega_h = average of four translates of a product state with
            period 4 cells along e_1; O_h is the segment [pi*_0, pi*_1], pi*_0 != pi*_1.
            Same for the 1D Margolus walk (section 5).
MECHANISM:  hidden phases in Z/2 (before) and Z/4 (after) in the Born laws; the two
            phase matchings tie in cost and entropy by the counting identity (Lemma 4.2).
PROVED POSITIVE (here): Lemma 3.1 (cube numbers kept), Lemma 3.2 (equal Born laws:
            identity unique), Lemma 3.3 (tiling), Theorem 3.4 (LW1-U in full for
            active-cube product states), Lemma 3.5 (ergodic reduction; uses Jacobs, credited).
NOT TOUCHED: the vacuum. Factor states have tail-trivial Born laws (Remark 6.1, Powers,
            sketched), so the mechanism does not apply.
OPEN:       Lemma LW1-U_f (section 6): uniqueness and torus limit for invariant factor
            states, in particular the PS-7r vacuum and its half-tick images. No attack
            run on it here beyond the reductions of section 3.
PROPOSED:   PS-3m (section 8): transport of a mixture = mixture of the components'
            transports, each to its own image. Smuggle check: passes 1, 2, 4; passes 3
            with a note (TM1/BR1 "labels persist"). Limit: components with no
            finite-index stabiliser get no answer.
FOR LW1:    Theorems E4-E6 stand. Replace LW1-U by LW1-U_f in the open-inputs list.
            Owner decision: PS-3m, or alternative (A) or (B) of section 8.
CHECKS:     check_cube.py (scratchpad, guidance only): R^2 = 1 to 2.2e-16; the formula
            of Lemma 4.0 (iii) to all printed digits; P and Q depend on a and b only;
            per-cell least cost K/4 equal for both phase classes (0.0173 per cell).
```

---

## 10. Round 2: Lemma LW1-U_f (factor states; the PS-7r sea first)

- Written by: Claude Opus 5.5 subagent, round 2 of pass 1, 2026-11-04. Not refereed.
- Base: this file as committed at `58d5c77701c6f8384b62c2b9f6e47b9e50bcf2fa`. Sections 0-9 are unchanged; this section is appended.
- New scratch script: `check_sea_condind.py` (session scratchpad, guidance and refutation only).

### 10.0 Outcome

**One precise smaller lemma, after three attacks.** None of the three attacks closes LW1-U_f, and none yields a counterexample. Each fails for a reason stated exactly below. The open statement is narrowed to the vacuum alone (Lemma LW1-U_sea, section 10.5). Three new results are proved here. Theorem 10.2 proves uniqueness whenever both Born laws are, given the shared cube-number field, independent across cubes with laws that depend only on each cube's own number; this generalises Theorem 3.4. Corollary 10.3 proves LW1-U_f for the sea at the boundary point `alpha = 0` of the window. Lemma 10.4 shows that a symmetry of the problem always leaves a symmetric optimiser. So a symmetry-based counterexample must exhibit spontaneous breaking in the PS-3 selection itself.

### 10.1 The sea's Born law, stated

By C3 and Wick's theorem, the Born law of a gauge-invariant quasi-free state with one-body density `G` is the determinantal measure with kernel `G`. For a finite window `W` and occupation pattern `s` on `W`, `mu(c_W = s) = det M`, where row `x` of `M` is row `x` of `G_{WW}` if `s_x = 1` and row `x` of `(I - G)_{WW}` if `s_x = 0` (credited, standard). For the sea, `G = P` (Theorem B10), with `P_xx = 1/2`, and with `|P_xy|` decaying exponentially for `mu > 0` (Theorem B10 (v)). The half-tick image has kernel `V_e P V_e^*`. Both are pure states, hence factor states. By Remark 6.1 both Born laws have trivial tails.

### 10.2 Attack 1: Bernoulli property and Ornstein theory

*The idea.* If the sea's Born laws were Bernoulli shifts or finitely determined, Ornstein theory might control optimal joinings, and it might give the recovery sequence that Attack 2 of `LW1_DRAFT.md` lacked.

*What the literature gives.* Lyons and Steif (Duke Math. J. 120 (2003) 515-575) study "stationary processes indexed by Z^d that are defined via minors of d-dimensional (multilevel) Toeplitz matrices", and their abstract states "all of these processes are Bernoulli shifts". I read the abstract only, through a search summary. Their class, as the abstract states it, is `Z^d`-stationary with a scalar symbol. The sea's Born law is stationary only under the cell lattice `2Z^3`, with an `8 x 8` matrix symbol. So it is not in that class as stated. Whether their proof extends is not checked here.

*Why the attack fails, even granting Bernoullicity.*
1. PS-3's data are local in the configuration coordinates: the cost counts changed sites, and the support is a product of cube supports. A Bernoulli isomorphism with an i.i.d. process is a non-local measurable map. It does not carry the cost or the support. So the product theorem (Theorem 3.4 or 10.2), which needs product structure in these coordinates, does not transfer through it.
2. Uniqueness of a greatest-entropy optimal joining is a property of the cost, not of the isomorphism class of the marginals. Section 4 already shows this: there, an ergodic pair of marginals has two optimal joinings, while products have one.
3. The finitely-determined property (Ornstein) controls the unconstrained d-bar distance from nearby processes. The couplings it supplies move single occupations freely, so they leave `S`. Lemma 3.1 shows that every element of `C_h` keeps every cube number, and those couplings do not. So it does not give the support-respecting recovery estimate that `LW1_DRAFT.md` Attack 2 named as missing.

### 10.3 Attack 2: condition on the shared cube-number field

By Lemma 3.1 every coupling in `C_h` shares the active number field `n = (N_k)_k`. The attack conditions on `n` and tries to reduce the problem to finite single-cube problems. It works exactly when the internal configurations are independent across cubes given the numbers.

**Hypothesis (CL), cube-local given numbers.** There is a law `lambda` of the number field and, for each `m in {0, ..., 8}`, cube laws `alpha_m` and `alpha'_m` on `{sigma : N(sigma) = m}`, such that `mu_h = ∫ ⊗_k alpha_{n_k} dlambda(n)` and `mu_{h+1} = ∫ ⊗_k alpha'_{n_k} dlambda(n)`.

**Theorem 10.2 (uniqueness under CL; proved here).** Under (CL), with `lambda` invariant, `O_h` has exactly one element, `pi_hat = ∫ ⊗_k lambda*(alpha_{n_k}, alpha'_{n_k}) dlambda(n)`.

*Proof.* *Feasibility.* Take any `pi` in `C_h` (Theorem E4). Under `mu_h`, the cube-0 configuration given `N_0 = m` has law `∫ alpha_{n_0} dlambda(n | N_0 = m) = alpha_m`; likewise `alpha'_m` under `mu_{h+1}`. Since `N_0(c) = N_0(c')` `pi`-a.s. (Lemma 3.1), the cell-0 pair law given `N_0 = m` lies in `Pi(alpha_m, alpha'_m; S_C)`. So that set is nonempty whenever `lambda(N_0 = m) > 0`, and `kappa_m`, `lambda*_m`, `H*_m` are defined.

*Cost.* For every `pi` in `C_h`, `E_pi D_0 = sum_m lambda(N_0 = m) E_pi[D_0 | N_0 = m] >= sum_m lambda(N_0 = m) kappa_m =: kbar`. `pi_hat` is in `C_h`: its marginals are `mu_h` and `mu_{h+1}` by (CL), it is carried by `S`, and it is invariant because `lambda` is. It attains `kbar`.

*Least cost forces the face, box by box.* Let `pi` have least cost. Fix a finite set `Lambda` of cells, `k` in `Lambda`, and a value `n_Lambda` of positive probability. Under (CL), given `n_Lambda` the configuration of cube `k` has law `alpha_{n_k}` under `mu_h` (integrate out the cells outside `Lambda`), and `alpha'_{n_k}` under `mu_{h+1}`. So the pair law of cube `k` given `n_Lambda` lies in `Pi(alpha_{n_k}, alpha'_{n_k}; S_C)`. The pair law of cube `k` given `N_k = m` is the mixture of these over the values of `n_Lambda` with `n_k = m`, and it lies in the face `F_m` because `pi` has least cost. A convex combination with positive weights lies in a face only if each term does. So each pair law given `n_Lambda` lies in `F_{n_k}`, and its entropy is at most `H*_{n_k}`, with equality iff it is `lambda*_{n_k}`.

*Entropy bound.* `n_Lambda` is a function of `c_Lambda`, so `H_Lambda(pi) = H(n_Lambda) + H(pairs_Lambda | n_Lambda) <= H(n_Lambda) + sum_{k in Lambda} H(pair_k | n_Lambda) <= H(n_Lambda) + |Lambda| hbar*`, where `hbar* = sum_m lambda(N_0 = m) H*_m`. Under `pi_hat`, given `n_Lambda` the pairs in `Lambda` are independent with laws `lambda*_{n_k}`, so equality holds. Hence `s(pi) <= s(lambda) + hbar* = s(pi_hat)` (`s(lambda)` is the specific entropy of the number field, which exists by subadditivity). So `pi_hat` is in `O_h`.

*Uniqueness.* Let `pi` be in `O_h` with `pi != pi_hat`. Then some box `B` of cells has a pair law under `pi` different from that under `pi_hat`. Both give `n_B` the law of `lambda`, so for some value `n_B` of positive probability the conditional pair law on `B` differs from `⊗_{k in B} lambda*_{n_k}`. Then either the cubes are not conditionally independent, or some cube's conditional law lies in `F_{n_k}` but is not `lambda*_{n_k}`. Either way, `H(pairs_B | n_B) = |B| hbar* - g` with `g > 0` (equality conditions as in Lemma 3.3). Tile `Lambda_m` (side a multiple of that of `B`) by translates `B_t` of `B`. Then `H(pairs_Lambda | n_Lambda) <= sum_t H(pairs_{B_t} | n_Lambda) <= sum_t H(pairs_{B_t} | n_{B_t})`. The last step holds because conditioning on less cannot lower entropy, and `n_{B_t}` is a function of `n_Lambda`. By invariance each term equals `|B| hbar* - g`. So `H_Lambda(pi) <= H(n_Lambda) + |Lambda| (hbar* - g/|B|)`, and `s(pi) <= s(pi_hat) - g/|B|`, a contradiction. ∎

(CL) holds for Born laws that are products over the active cubes, with `lambda` a product, so Theorem 10.2 contains Theorem 3.4's uniqueness clause. It also holds for "classical" states whose internal configurations are cube-local given the numbers, with `lambda` arbitrary (correlated, even long-range).

**Corollary 10.3 (the sea at `alpha = 0`; proved here).** At the boundary point `mu = 2 eps` of the window (so `alpha = 0` and `beta = 2 eps` in `(0, pi)`), the PS-7r filling satisfies LW1-U_f at both half-ticks.

*Proof.* `V_e = 1` and `V = V_o = exp(i beta R_o)`. On each odd cube `R_C^2 = 1` and `tr R_C = 0`, so `R_C` has eigenvalues `+1` and `-1`, four of each. `V_o` has eigenvalues `e^{i beta r}`, i.e. quasi-energy `w = -beta r`, which lies in `(-pi, 0)` iff `r = +1`. So `P` is the direct sum over odd cubes of the projections `(1 + R_C)/2`, and `omega_P` is the product over odd cubes of the pure 4-particle state filling the `r = +1` space. At the even half-tick `V_e = 1`, so `mu_{h+1} = mu_h` and `cos alpha = 1`, and Lemma 3.2 applies. At the odd half-tick the active cubes are the odd ones, and each cube state is an eigenvector of its gate (a Slater determinant of eigenvectors of `V_o`). So both Born laws are the same product over the active cubes, and Theorem 3.4 applies. ∎

The window of Theorem B10 has `mu < 2 eps` strictly, so this is a boundary statement. It shows that LW1-U_sea holds in the atomic limit. It says nothing inside the window.

*Why the attack fails for the sea.* (CL) is false for the sea. This is shown by computation, which may refute but does not prove. For two adjacent active cubes, the internal configurations are dependent given both cube numbers. Since (CL) applied to the box made of the two cubes demands independence given their two numbers, (CL) fails. [check, `(eps, mu) = (0.3, 0.1)`: 1D Margolus sea, `L = 200`, blocks `{0,1}` and `{2,3}`, given one particle in each: conditional mutual information `0.148` nats. 3D cube-tick sea on the `8^3` torus, cubes at cells `0` and `e_1`, given four particles in each: `0.084` nats; given one in each: `0.011` nats.] The dependence comes from the kernel `P` linking corners of different cubes. Conditioning on the numbers does not remove it, so the conditional problem is not a family of finite problems. Theorem 10.2's tiling step needs the conditional entropy given `n_B` to split over cubes. For the sea it does not split, and nothing replaces the per-cube target `lambda*_{n_k}`.

### 10.4 Attack 3: a symmetry not respected by the optimiser

**Lemma 10.4 (symmetric optimisers exist; proved here).** Let `g` be a bijection of configurations, of finite order `r`, that maps the cell partition to itself, commutes with the cell translations up to an automorphism of `Z^3`, and maps `mu_h`, `mu_{h+1}` and `S` to themselves and changed sites to changed sites. Then `g x g` maps `O_h` onto `O_h`, and `O_h` contains a `g`-invariant element.

*Proof.* `g x g` maps `C_h` to itself (marginals, support and invariance are kept) and keeps cost per site. It maps the box entropies of a box to those of the image box, so it keeps specific entropy. So it maps `O_h` to itself. `O_h` is convex (Theorem E6), so for `pi` in `O_h` the average `(1/r) sum_i (g x g)^i pi` is in `O_h` and is `g`-invariant. ∎

So a symmetry gives a second optimiser only if some optimiser is not symmetric. For a finite group, the symmetric average of an ergodic, non-symmetric optimiser is non-ergodic. So with ergodic marginals (Lemma 3.5) this means spontaneous breaking of `g` inside the PS-3 selection. The sea's coupling problem has such symmetries: the rotations of `G_U` that keep the active tiling, and the occupation flip `c -> 1 - c` (the sea's Born law is flip-invariant, since `Theta P Theta^{-1} = 1 - P`, Theorem B10 (iii); whether the flip keeps `S` is not checked here).

*Candidate constructions, and where each stops.*
1. *Lift section 4 to a factor state by randomising the pattern independently per cube.* A mixture of product states with independent random cube labels is itself a product state: `∫ ⊗_k rho_{r_k} dnu(r) = ⊗_k (sum_r nu_1(r) rho_r)` when `nu = nu_1^{⊗}`. So Theorem 3.4 applies, and `O_h` is a singleton. The tie of section 4 is resolved because the matching choice becomes local and the per-cube optimum `lambda*` absorbs it.
2. *Randomise the pattern by a mixing Markov label chain along `e_1`.* The state `∫ ⊗_k rho_{r_k} dnu(r)` is then a factor state when `nu` is absolutely regular (Powers' criterion with `|omega(AB) - omega(A) omega(B)| <= 2 ||A|| ||B|| beta_nu(N)`; sketched only). Its Born laws do not satisfy (CL), because the labels are hidden: `P_0` and `P_1` overlap. This draft has neither a proof nor a counterexample for this family.
3. *Rigidity from subshifts.* Burton and Steif (Ergodic Theory Dynam. Systems, 1994; credited from memory, not re-read) gave `Z^d` subshifts of finite type, `d >= 2`, with more than one measure of maximal entropy. A breaking of the kind Lemma 10.4 requires would need the least-cost face to impose such a rigid constraint between cubes. The support `S` is a product over cubes, so any such rigidity would have to come from the marginal constraints. No mechanism is known by which a determinantal marginal imposes it.

*Why the attack fails.* A counterexample at a factor state needs a choice that PS-3 cannot see and that cannot be changed locally. Section 4's choice was global (a phase), which factor states exclude (Remark 6.1). Making the choice local (construction 1) lets the greatest-entropy stage randomise it independently, and the optimum is unique. The intermediate case (construction 2) is not settled, and no rigid mechanism (construction 3) is available for the sea.

### 10.5 The precise smaller lemma

**Lemma LW1-U_sea (open).** *Let `0 < mu < 2 eps < pi` and let `omega_P` be the PS-7r sea of the free cube tick. For `h = 0` (the even half-tick acting on `omega_P`) and `h = 1` (the odd half-tick acting on `omega_P o beta_e`), the set `O_h` of Theorem E6 has exactly one element.* (`omega_P` is stationary under the tick, so these two cases cover every half-tick.)

It is smaller than LW1-U_f in two ways. It names one state and its half-tick image instead of all invariant factor states, and it drops the torus clause. It is the statement that the vacuum needs.

*Exact reason each attack fails on it.*
- **Attack 1:** PS-3's cost and support are local in the occupation coordinates, and a Bernoulli isomorphism is not. Lyons-Steif, as stated in their abstract, covers scalar `Z^d`-stationary kernels, not the sea's `2Z^3`-periodic `8 x 8` kernel. Finite determination bounds the unconstrained d-bar, not the support-respecting cost.
- **Attack 2:** Theorem 10.2 needs the internal configurations to be independent across cubes given the numbers. The sea violates this ([check] conditional mutual information `0.148` nats in 1D, `0.084` nats in 3D).
- **Attack 3:** Lemma 10.4 forces any symmetry-based counterexample to show breaking inside the PS-3 selection. Factor states exclude the global-phase mechanism. Local randomisation of a tie is absorbed by the entropy stage. No rigid mechanism is known for a determinantal marginal.

*What would move it.* A proof of Lemma LW1-U_sea would need a replacement for the per-cube target of Theorem 10.2: some explicit coupling `pi_hat` built from `P` (for example from the determinantal structure, or from the quantum dynamics of the half-tick). It would also need a strict entropy deficit for every least-cost coupling that differs from `pi_hat` on a finite box. A counterexample would need a rigid least-cost constraint between cubes coming from the determinantal marginals. The 1D Margolus sea is the natural first test case (section 5's setting).

### 10.6 What round 2 changes for LW1

- LW1-U_f stays open. The vacuum statement LW1-U_sea is the named open input that LW1 needs.
- LW1's Qualification at every factor state needs more than LW1-U_sea. If the owner reads the Qualification as needing one answer at every state, then PS-3m (section 8) plus LW1-U_f are both required. Theorem 10.2 and Theorem 3.4 cover product states and states that satisfy (CL), and nothing more is proved. The owner decides whether the Qualification applies at every state or at the states the law reaches from its `omega_0`.
- No new specification is proposed in this round. LW1-U_f has not failed, so no further rule is called for yet.

```
LEMMA:      LW1-U_f (section 6), the PS-7r sea first.
OUTCOME:    PRECISE SMALLER LEMMA after three attacks: LW1-U_sea (section 10.5), open.
            No proof, no counterexample at any factor state.
PROVED HERE (round 2, not refereed):
            Theorem 10.2: uniqueness for Born laws that are cube-local given the number
              field (CL); contains Theorem 3.4's uniqueness.
            Corollary 10.3: LW1-U_f for the sea at the window boundary alpha = 0 (both
              half-ticks).
            Lemma 10.4: a finite-order symmetry of the problem leaves a symmetric
              optimiser; a counterexample needs breaking inside PS-3.
ATTACKS:    (1) Bernoulli/Ornstein: isomorphisms do not carry PS-3's local cost and support;
                Lyons-Steif (abstract) is scalar Z^d, not the sea's 8x8 2Z^3 kernel.
            (2) Number-field conditioning: (CL) false for the sea [check: conditional MI
                0.148 nats 1D, 0.084 nats 3D].
            (3) Symmetry: global phases excluded (Remark 6.1); local ties are absorbed by
                the entropy stage (product states); the Markov-label factor family is
                unsettled; no rigid mechanism for determinantal marginals.
FOR LW1:    LW1-U_sea is the open input the vacuum needs. The Qualification at every state
            needs PS-3m plus LW1-U_f; owner to decide its reading. No new specification.
CHECKS:     check_sea_condind.py (scratchpad): sea gap min|Im lambda| = sin(mu) = 0.0998;
            P_xx = 1/2 to 1e-15; conditional MI as above. Guidance and refutation only.
```
