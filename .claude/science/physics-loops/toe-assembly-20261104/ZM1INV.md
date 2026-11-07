# ZM1-I1[INV]. The invariant-algebra zoom

## 0. Status

**Pass 2; not refereed or frozen.** The target remains open. The results below are author-side mathematics, not independent audit findings. They neither construct the requested zoom nor prove it impossible.

**Proved here, subject to the stated hypotheses.** The locked even-`m` U and O witnesses restrict to characters of the invariant algebra (Theorem 2.1). Character pairs make the class-(a) comparison vanish (Theorem 2.2). For those base-tick witnesses, the target with an even U coarse register reduces to K-INV; the analogous O result is conditional on allowing an O coarse law (Theorem 2.3). Local neutral matrix registers do not exist in these fine laws (Theorem 3.2). A specified equivariant link-path construction and a specified representative-end construction fail (Theorems 3.3–3.6). A good sector of an `m=1` path carries an exact coarse link algebra (Theorem 3.4).

**GAP.** Pass 1 states the O coarse-law reduction as an instance of the owner target. The owner text specifies the same five-mode construction with coarse `m₁` in R-form; it does not explicitly specify an O coarse alternative. The O reduction below is a conditional variant, not an interpretation adopted here. Pass 1 also claims exact tail matching for all the named non-character tests and shared support in any solution. The image of the relevant test observables is not established, Lemma ER concerns tail envelopes, and shared support is proved only for exactly localized images. Section 4 records the corrected statements. The good-sector global construction also needs a compatible assignment of paths and local algebras; its single-path result is proved, not a global unital map.

**Open by name.** K-INV and K-INV-O; ZM1-I1[INV] in non-character vacua; VC1 and its vacuum choice; ICE-T and ice-state tails; LZ1-i[ZM1a]; ZM1-G; Y1; H-BLOCK; R-CS, including R-CS^str; MT1-S. The finite-parameter witness tails, the coarse odd-register character-state question, and extensions of the good-sector construction to defects also remain open. The proposed readings R-V, R-NC and R-ALL are not adopted.

**Provenance.** Pass 1: `ZM1INV_DRAFT.md`, Claude Opus 5.5, SHA-256 `078d8fd390241eb8afb23d9e4e25c12676b815cf3b653180c9a3abd6cd599e7d`; it reports source revision `b2690b690`. Pass 2: Codex, model requested as `gpt-6.1-terra`; actual model identifier, effort and session id: see run log. This file is a distillation, not an independent referee report. No scratch computation from pass 1 was reported. The prior digest is `prior/ZM1INV.md`; source paths below are relative to this folder unless stated otherwise.

## 1. Definitions inferred by the distiller

1. The fine U law `L5-U[m]`, `1≤m≤9`, has five CAR matter modes per site and link space `Λ^m(C⁵⊕C⁵)`. The end numbers satisfy `p_{ℓ,x}+p_{ℓ,y}=m`. The O law has link space `S_+`, the even sector of ten rishon modes. Its local gauge group is `Spin(10)`; U uses `U(5)` (`VC1_5.md`, section 2). Link factors commute with one another and matter. `𝔄` is the norm-completed quasi-local algebra, `𝔄^G` the fixed algebra of all local gauge transformations, and `E` the gauge average. Finite invariant elements are dense in `𝔄^G` (`VC1_5.md`, Theorem 2.1).
2. For a finite collection `R` of site and link factors, `𝔄(R)=End(H_R)` with the graded matter algebra represented using a Jordan–Wigner ordering. `𝔄^G(R)=𝔄(R)∩𝔄^G` is the commutant of the local gauge actions at all sites touching these factors, including outer link endpoints. Invariant operators are even (`ZM1_OBS.md`, Theorem 3).
3. A coarse cell has eight sites; its fine block contains `(2L)^3` sites, and one coarse tick is `L` fine ticks, `L≥2` (`ZM1I1A.md`, section 1). In R-form the coarse U register has any `m₁∈{1,…,9}`. The owner requires a unital injective `*`-homomorphism `Φ:𝔄₁^G→𝔄^G`, cell covariance, and exponential locality for each local invariant input, with constants allowed to depend on its support radius. Charged fields and Gauss generators receive no map (`TOE_ASSEMBLY.md`, sections 3.8–3.9).
4. **K-INV(m,m₁,L)** asks for that map with its covariance and locality, independently of states and updates. **K-INV-O** is the analogous O-to-O question. These labels do not assert existence. A character is a state `ω` satisfying `ω(AB)=ω(A)ω(B)` for all invariant `A,B`.
5. For stationary states and gauge-preserving updates, set
   `F₀ᵀ(A*,B;t)=ω₀(Φ(A)* α^{Lt}(Φ(B)))−ω₀(Φ(A)*)ω₀(Φ(B))`, with `F₁ᵀ` defined by `ω₁,α₁` without `Φ`. For norm-at-most-one local invariant `A,B`, the retained class-(a) condition at `r=|β|∞≥1` is
   \[
   |F_0^T(A^*,\tau_\beta B;t)-F_1^T(A^*,\tau_\beta B;t)|\le C_{R_0}(r^{-2}+tr^{-3})M(r,t),\quad
   M(r,t)=\sup_{|\beta'|_\infty\ge r}\max_i|F_i^T(A^*,\tau_{\beta'}B;t)|.
   \]
   It quantifies over every support radius, all such inputs and their cell-group images, and all nonnegative coarse ticks. A zero envelope gives zero values on both sides. No one-point matching is imposed.
6. `P_m={max(0,m−5),…,min(5,m)}` is the spectrum of either end number of a U link. It has at least two elements for `1≤m≤9`. A locked U product vector occupies flavours `1,…,k` at both ends of every link, `m=2k`, with matter everywhere empty or everywhere full; its gauge average is a VC1 witness. The locked O vectors have all matter and link modes empty or all full. Their averages are the witnesses in `VC1_5.md`, Theorems 5.5 and 4.2. `H_phys` means the closure of `π(𝔄^G)Ω` in the state’s GNS representation.

## 2. Character witnesses and reduction

**Theorem 2.1 (C1, C1-O).** Each locked U witness for even `m` and each locked O witness is a character on `𝔄^G`. For every finite `R`, every `A∈𝔄^G(R)` sends the corresponding product vector `Ψ_R` to a scalar multiple of itself.

*Proof.* For U, use the diagonal gauge torus. Let `h_{x,j}` count flavour `j` in the factors of `R` incident at `x`, including matter if present. Let `d_x` be the number of link ends there. For empty matter the product vector has weights `d_x` for `j≤k` and zero otherwise. Any basis vector with these weights has no high flavours. Each link contains `2k` rishons and each end can contain at most the `k` low flavours. Hence every end contains exactly those `k`, and the matter is empty. For full matter, each low-flavour weight is the maximum possible, so every incident slot contains that flavour. The link number then excludes high flavours at both ends; the remaining high-flavour weights force full matter. In either case the joint weight space is one-dimensional. Invariant operators preserve it.

For O, the Cartan charges are sums of `n_j−1/2` over the included factors at each endpoint. The all-empty vector uniquely minimizes every charge, and the all-full vector uniquely maximizes every charge; both link vectors lie in `S_+`. The same weight-space argument applies. The gauge average fixes invariant observables. For local invariant `A,B`, the scalar action gives `ω(AB)=ω(A)ω(B)`. Density and continuity extend this to `𝔄^G`. □

This strengthens the already proved dark-kinematics result in `ZM1I1A.md`, Theorem 8. Purity of these restrictions was already proved in `VC1_5.md`, Theorems 4.2 and 5.5; purity alone does not imply multiplicativity.

**Theorem 2.2 (C2–C3).** Let both stationary states restrict to characters and let both updates preserve the invariant algebras. For any unital `*`-homomorphism `Φ:𝔄₁^G→𝔄^G`, both truncated functions vanish for every input, separation and tick. Class (a) then holds for every exponent and nonnegative constant. In a character state `H_phys=CΩ`.

*Proof.* Both time-evolved observables stay invariant. Multiplicativity factors each two-point value; stationarity identifies the time-evolved one-point value with its initial value. Thus both truncated values vanish. Also `‖π(A)Ω−ω(A)Ω‖²=ω(A* A)−|ω(A)|²=0`; take the closure. □

This extends the finite-range dark-pair benchmark already in `ZM1I1A.md`, Theorem 7; no locality of `Φ` is needed here.

**Theorem 2.3 (R).** For a locked U fine witness, even `m`, and its base tick, the target with even coarse `m₁` holds exactly when K-INV holds for some such `m₁` and `L≥2`. The analogous statement holds for locked O witnesses if an O coarse law is allowed. Any instance of the target implies its kinematic map conditions, for every fine state and update.

*Proof.* The target includes the K-INV map. Conversely, choose the coarse base tick and a coarse locked witness. `VC1_5.md`, Theorem 5.5, gives its stationarity, and Theorem 2.1 makes it a character. The fine pair has the same properties. Theorem 2.2 supplies the bound. For the conditional O variant use `VC1_5.md`, Theorem 4.2. □

For odd coarse `m₁` this proof supplies no coarse character witness. A different coarse state could still work; its existence is open. A plaquette update is not included in Theorem 2.3 unless the chosen witness is separately shown stationary for it.

## 3. Kinematic tests

**Theorem 3.1 (T).** For even `m` and a finite region containing a link, `𝔄^G(R)` has at least two tracial states.

*Proof.* Restrict the normalized matrix trace `τ` and the locked character `ω` to the invariant algebra. Both are traces. For `P=[p_{ℓ,x}=k]`, `ω(P)=1` while `τ(P)=binom(5,k)^2/binom(10,2k)<1`. □

Thus the unique-full-matrix-trace transfer used in `ZM1I1A.md`, Theorems 1–6, cannot be applied directly to the invariant algebra. This does not disprove every possible trace obstruction.

**Theorem 3.2 (N).** In an even-`m` U or O fine law, no unital `*`-homomorphism `M_D→𝔄^G(R)` exists for finite `R` and `D≥2`.

*Proof.* The scalar action on `Ψ_R` from Theorem 2.1 is a character of `𝔄^G(R)`. Composition would give a unital homomorphism `M_D→C`. Its kernel would be a proper nonzero ideal, impossible because matrix units generate all of `M_D` from any nonzero matrix. □

If a coarse finite invariant algebra is mapped unitally into a fine finite invariant algebra, composition with its character gives a character of the coarse algebra. The locked even-register coarse algebra has such characters by Theorem 2.1. This rules out the proposed finite-region neutral full-matrix register. It does not rule out K-INV, a direct-sum encoding, or exponentially localized registers; the latter would need a near-inclusion argument.

**Theorem 3.3 (E, E1).** For U fine and coarse links with `1≤m,m₁≤9`, a path of at least two distinct fine links admits no unital link-algebra homomorphism equivariant for the independent U(1) end-number actions, when these actions are implemented by the first and last fine end numbers. If covariant representatives are connected by such paths, one-link paths for every coarse edge are also impossible for `L≥2`.

*Proof.* Let `K` be the coarse link Hilbert space and `H` contain the first and last fine link factors. Matrix units give a unitary `W:H→K⊗K'` with `Wι(a)W*=a⊗1`. End equivariance and the matrix commutant give
\[
Wp_xW^*=p_X\otimes1+1\otimes k_x,\qquad Wp_yW^*=p_Y\otimes1+1\otimes k_y,
\]
with commuting self-adjoint `k_x,k_y`. The coarse joint spectrum is `{(q,m₁−q):q∈P_{m₁}}`; the fine joint spectrum is `P_m×P_m` because the first and last links are distinct tensor factors. Write `s=min P_m`. Represent `(s,s)` as `(q+a,m₁−q+b)` using a joint eigenvalue `(a,b)` of the `k`'s. An adjacent `q±1∈P_{m₁}` then yields a joint spectral point with one coordinate below `s`, a contradiction.

If every coarse edge were a one-link path, representatives of neighbours would be fine neighbours. Cell-translation covariance gives `x_{X+2e_i}=x_X+2Le_i`, whereas two coarse edges give a sum of two fine unit steps. This is impossible for `L≥2`. □

This tests a factorwise full-link, end-equivariant construction. It does not require every invariant-only map to lift to one. The O parity case is not covered by the U number-spectrum argument.

**Theorem 3.4 (S).** For `m=m₁=1`, let a path have links `ℓ_i=(z_{i−1},z_i)`, `i=1,…,n`, and let `h_i=1` when its rishon is at its head. Let `P_γ=[h₁=⋯=h_n]`. On `ran P_γ` there is an equivariant unitary
\[
W_γ:\operatorname{ran}P_γ\to(C^5_x\oplus C^5_y)\otimes\bigotimes_{i=1}^{n-1}C^5_{z_i}.
\]
The commutant of the interior gauge groups is the full coarse link algebra on the first factor. For `U_ℓ^{ab}=r^{head}_a r^{tail\dagger}_b` and `T_γ^{jk}=\sum_{a_1,…,a_{n-1}}U_{ℓ_n}^{j a_{n-1}}\cdots U_{ℓ_1}^{a_1 k}`, one has `T_γ=P_γT_γP_γ` and `T_γ^{jk}=(-1)^{n+1}ι_γ(U^{jk})`, extended by zero off the good sector.

*Proof.* At `z_i` the two path ends contain `h_i+1−h_{i+1}` rishons, equal to one exactly when `h_i=h_{i+1}`. In the all-tails sector, identify the first colour with the coarse `x` end and each remaining colour with its interior site. In the all-heads sector identify the last colour with `y` and the others with the same interior sites. Both copies at each interior site transform as the defining `U(5)` representation. Their product representation is irreducible, so Schur's lemma gives the stated commutant.

Each `U_ℓ` kills a tail-occupied state and sends a head colour `a` to a tail colour `b` with coefficient `−1`. Therefore the product kills every sector except all-heads, maps it to all-tails, preserves interior colours after summation, and acts there as `(-1)^n|x,k⟩⟨y,j|⊗1`. The coarse `U^{jk}` is `−|x,k⟩⟨y,j|`, giving the sign. □

The sector projection is invariant. Extending this local good-sector action by zero is not unital; an infinite product of sector projections is not a quasi-local projection. Compatibility across local supports and defect sectors remains to be constructed.

**Theorem 3.5 (F).** For `m=m₁` in `1,…,9`, no unital `*`-homomorphism of invariant algebras can send both coarse end-number functions of one link to the corresponding end-number functions of the first and last links of a fine path with at least two distinct links.

*Proof.* Set `s=min P_m`. Since `2s≠m`, the coarse spectral projections `[p_X=s]` and `[p_Y=s]` have zero product. Their prescribed fine images are nonzero projections on different link factors, hence have nonzero product. A homomorphism preserves products. □

**Theorem 3.6 (F′).** Let an injective invariant-algebra homomorphism send orthogonal coarse projections `P,P'` into exactly localized fine algebras on disjoint site and link factors. Then `P=0` or `P'=0`.

*Proof.* The fine images are even. After ordering finite CAR factors, their Jordan–Wigner strings across the other region cancel, so they act on disjoint tensor factors. A tensor product of two nonzero projections is nonzero. Their product is zero, hence one image is zero; injectivity gives the conclusion. □

In particular, nonzero incompatible coarse end-number projections cannot have disjoint exact supports. This does not establish literal common support for merely exponentially localized images.

## 4. Tests, inherited results and limits

`ZM1_OBS.md`, Lemma ER, already proves that at each fixed tick the two tail envelopes agree to relative error `O(r^{-2})` if class (a) holds. If both have positive exponential asymptotics `a_i exp(−r/ξ_i)(1+o(1))`, their lengths and amplitudes agree; the analogous conclusion holds for positive power-law asymptotics. These are envelope statements with stated asymptotic hypotheses. They do not by themselves give equality of every correlation at each finite separation or time.

The locked base-tick U and O witnesses give zero invariant truncated values by Theorem 2.2, paired with a coarse character. By contrast:

- The `VC1_5.md` Theorem 5.2 empty/full-matter states with tracial links are not characters: an end-number projection has expectation strictly between zero and one. They are dark for the base tick by `ZM1I1A.md`, Theorem 8. Theorem 7 there makes the comparison automatic for finite-range maps between dark pairs. With only exponential locality this automatic conclusion does not follow. Against an identically zero coarse tail, the relative bound forces the fine tail to vanish beyond a sufficiently large separation at each fixed tick.
- The R2 mixture has the invariant projection tail `1/4`, already proved for all nonzero cell translations and ticks in `ZM1I1A.md`, Theorem 9 and RC-5. ER applies to that channel only if it is in the image of `Φ`. It does not prove that image inclusion.
- The neutral swap band is already constructed under NN-a in `GA1_5.md`, Theorem 6.3 and Proposition S-odd. `ZM1I1A.md`, RC-4, gives an approximate coarse moving-point lower bound if the required fine signal occurs in the image. A component of an image alone does not establish an exact coarse glider.
- The two neutral Clifford bands are already constructed in `LZ1I.md`, Theorems 6–8, under their stated state and update conditions. Their occurrence in the map image and the hypotheses of `ZM1_OBS.md`, Theorems 8′–9′, must be checked before branch matching follows.
- The odd-`m` ice states under ICE-T and their invariant-algebra purity and tails remain conditional or open; see `VC1_5U_ODD.md`, Theorems 4.2–4.3. The fact that a test state is non-character does not by itself show a nonzero long-distance tail in an arbitrary map image.

**GAP, pass-1 scope.** The draft says these non-character tests each require exact matching of every nonzero invariant tail in the image. ER establishes relative matching of tail envelopes; exact equality of decay parameters and amplitudes follows under its displayed asymptotic forms. It does not prove that a named channel is in the image or that all its finite-separation values coincide. The ice tails are not computed. Similarly, the three failed constructions in section 3 do not exhaust K-INV. Theorem 3.2 addresses finite-region full-matrix registers, Theorem 3.3 an end-equivariant full-link path map, and Theorems 3.5–3.6 the specified end-number and exact-support conditions. None rules out arbitrary invariant-only embeddings.

**Existing related work.** The digest `prior/ZM1INV.md` identifies exact regrouping and free approximations in `ZM1.md`, Theorems Z0–Z2; the one-dimensional even refinement in `ref/main/docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md`; the finite-region Peter–Weyl approximation in `ref/main/docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`; and the level-matched gauge toy in `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`. They are already proved or stated in those sources under their own hypotheses, with the ledger or review qualifications recorded in the digest. They do not construct the present map. `ZM1.md`, Theorems Z3–Z3′, already excludes the stated linear transported charged fields; `GA2_Y2.md`, Theorem 3.4, supplies the cited finite-link coherence obstruction to the c-number-link attack. Neither establishes a general invariant-map obstruction.

**Literature provenance.** Pass 1 reports searches on 2026-11-07, not a new verification here. It reports abstract-page checks for Brothier and Stottmeister, arXiv:1901.04940; Morinelli, Morsella, Stottmeister and Tanimoto, arXiv:2010.11121; Trezzini, Pizzamiglio, Bisio and Perinotti, arXiv:2511.23398; Nachtergaele and Sims, arXiv:math-ph/0506030; and Grundling and Rudolph, arXiv:1512.06319. `ZM1I1A.md`, RC-6, separately checks the first paper's refinement in a finite-group one-dimensional example. The pass-1 listings of arXiv:1907.05549, 2002.01442, 2107.13834, 2407.12652, 2011.04287, 0910.3675, 1108.1335, 1212.5562, math-ph/0210020, math-ph/0407063 and 1707.06243, and the Bałaban and Gawędzki–Kupiainen titles, are search-result or title-only records, not verified proofs. None is a proof input here. The pass-1 search's failure to locate the desired 3+1-dimensional invariant-map construction is not a nonexistence theorem.

## 5. Interfaces and proposed readings

The invariant domain contains the central charges `Q_X`, but the owner imposes no identification of their images with fine Gauss charges. Traceless Gauss generators and odd charged fields are outside the domain. Thus R-CS, MT1-S and CG1's charged `16` need a separate bridge. A finite charge–anticharge string has an image at each fixed support radius; class (a) gives no uniform-in-length bound for the straight-string limit R-CS^str.

Complete exact invariant data reconstruct the centered physical-sector tick and translations under the hypotheses already proved in `ZM1_OBS.md`, Theorem 4. Its conditional branch results require their own summability, phase and weight hypotheses; class (a) alone does not establish a common speed. In a character state the centered physical sector is zero. Wilson loops of fixed size belong to the domain, but constants may depend on their support radius; class (a) does not control growing loops. GA2 and ZM1-G still need a continuum dictionary and propagated errors. H-BLOCK needs a joint limiting state; one-step two-point comparison does not supply it. Full ZM1 also needs a fixed point or controlled trajectory and compatible content (`TOE_ASSEMBLY.md`, ZM1 target).

The following are **proposed readings**, not owner decisions. The four tests ask whether a reading (1) fixes a target, (2) is open-ended, (3) settles downstream physics by premise, and (4) adds unnecessary structure or constants. P means pass, C conditional, F fail. These are pass-1 assessments, not independent review verdicts.

- **R-V:** pose ZM1-I1[INV] in the vacuum VC1 selects once selected. Checks: P, P, P, P. It restates the specified-vacuum reading without selecting one. If that vacuum is a locked witness with the base tick, Theorem 2.3 applies.
- **R-NC:** exclude states whose restriction to `𝔄^G` is a character. Checks: C, P, F, P. Theorem 2.2 implies `H_phys≠CΩ` under this exclusion; whether that is a relevant premise for VC1's excitation target is a physical interpretation, not a new VC1 theorem.
- **R-ALL:** require the bound for every P-witness VC1 supplies. Checks: P, F, P, C. The set of supplied witnesses can grow; the pass-1 assessment treats that as open-ended. This assessment is not a proof that every closed universal formulation would fail the test.

R-V alone passes all four on these assessments. No reading is required for the conditional theorems above. The actual VC1 vacuum and whether a locked witness represents it remain open. In particular, if VC1 requires massless gauge and graviton excitations as vectors in that vacuum's own `H_phys`, Theorem 2.2 excludes a locked witness under that requirement; it does not establish what VC1 requires or prove a physical vacuum selection.
