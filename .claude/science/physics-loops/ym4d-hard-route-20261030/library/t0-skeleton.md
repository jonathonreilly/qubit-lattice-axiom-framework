lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T00:30Z

# T0 skeleton (queue row 155)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, pinned at `3f78ce873`. Author work. Not an audit. Not yet checked by the other model. Nothing here grants status.

Credit: the node structure is the Sussman–Alpoge outline (`YM4_sketch_500.tex` at `31a47c543775`, with Claude and Codex as authors of their text), its catalogue A1–H4 (SA L3757–4644) and Theorems 0, 0′ (SA L6915–7038). The 3D sources read for the route choice are their `YM3/YM3_I.tex`, `QED3/QED3.tex` and `RP O(d) trick (RP1)/RPM1.tex` at the same commit, fetched to a scratch folder, not committed. Balaban (CMP 89–122) and Dimock enter through the rebuilt rows. `SA L` is a line of `YM4_sketch_500.tex`; `Y3 L` is a line of `YM3_I.tex`.

States used: **checked** = proved here and checked line by line once by the other model (files named); **proved** = proved here, not yet checked by the other model; **open**; **cited** = stated in the outline or YM3_I, not rebuilt here; **off** = not on T0's path. A checked result is still an implication from its named inputs.

## 1. T0, pinned

T0 (GOAL.md, owner 2026-11-03), pinned to the outline's Theorem 0′ (SA L7017–7038) with 0(a)(iii), 0(b), 0(c)(4) until the OpenAI write-up is public: SU(2), Wilson action, observable O(f) = Σ_p f(x(p)) a_p (the tr F² sector). There is a volume-first limit S on separated tests in R⁴ with a canonical decomposition S = ∫σ_ξ dλ(ξ). Each σ_ξ satisfies E0′ (diagonal-flat extension with factorial growth), E1 (R⁴ ⋊ O(4) invariance), E2 (reflection positivity), E3 (symmetry, reality), E4 (clustering). The limit is non-trivial in the sense NT1 + NT2 of GOAL.md.

Reconstruction of a Wightman theory (OS II, §IV.1, E′→R′) is a corollary of E0′–E4. It is node O11 below, not a clause of T0 (owner to confirm; Section 2, R20).

## 2. Route at ranks 11, 12, 16–20 and K

Two short lemmas decide the choice. Both are proved by Claude here, not yet checked by the other model.

**Lemma S (no torus has both mirror families of one plane).** Let Γ ⊂ Z⁴ have finite index, with θ_n Γ = Γ for θ_n the swap of x_1 and x_4. Say Γ is adapted to a normal m if Γ = (Γ ∩ Rm) ⊕ (Γ ∩ m^⊥) (Y3 L73349). Then Γ is not adapted to both m = e_4 and n = e_1 − e_4.
*Proof.* Adapted to e_4 gives π_4(Γ) = Γ ∩ Re_4 = aZe_4 with a ≥ 1, where π_4 projects along e_4^⊥. Since θ_n Γ = Γ, a e_1 ∈ Γ. Adapted to n gives π_n(Γ) = Γ ∩ Rn = bZn. Now π_n(a e_1) = (a/2) n, so a ∈ 2bZ. Also bn ∈ Γ and π_4(bn) = −b e_4, so b ∈ aZ. Hence a ∈ 2aZ, which is false for a ≥ 1. ∎
*Consequence.* No torus sequence gives coordinate and diagonal reflection positivity in the same plane. The spectral cone (O6) and the two-point step of the rotation proof (S10) need both. So diagonal positivity must come through infinite-volume periodic states (AM1), and the limit must be volume-first. Our joint torus extraction (upper chain Theorems 8, 10.2) serves T1 only.

**Lemma N (RPM1 Theorem A does not apply to O).** Let μ be a law with RPM1 hypothesis (i): E e^{F(χ)} ≤ exp C(‖χ‖₁ + ‖χ‖₂²) for real χ. Let f, h have values in [0,1] and supports in balls of radius d ≤ 1. Then |E F(f)F(h)| ≤ C′d⁴.
*Proof.* Put X = F(f+h) and u = d^{−2}. From cosh y − 1 ≥ y²/2, E X² ≤ u^{−2}(E e^{uX} + E e^{−uX} − 2). By (i) with χ = ±u(f+h), each exponential moment is at most exp C(2u|B_d| + 4u²|B_d|) ≤ e^{C₁}, since |B_d| = (π²/2)d⁴. So E X² ≤ 2(e^{C₁} − 1) d⁴. Finally 4 E F(f)F(h) = E X² − E F(f−h)² ≤ E X². The same steps with f − h in place of f + h give the lower bound. Also |E F(f)| ≤ C₂d⁴ by Jensen and (i), so the connected value is O(d⁴) too. ∎
*Consequence.* The outline's law 0(c)(4) on R⁴ gives a connected two-point value of at least c g(d)⁴ ≈ c′(log 1/d)^{−2} on its shape class at scale d. The one-point part is O(d⁴). This contradicts Lemma N for small d, and NT2 contradicts it the same way. So hypothesis (i) fails for every non-trivial asymptotically free O, and RPM1 cannot be applied as stated. (QED3 can use it: its F_{μν} in d = 3 has an L²-bounded covariance; QED3.tex L21579.)

| Rank | Choice for T0 | Reason | First statement to prove | Reverses if |
|---|---|---|---|---|
| 11 link symmetry, common period (SA L2112) | outline's statement, proved by porting YM3_I's shorter proof: temporal gauge and two-layer determination (Y3 L78814–78969, Lemmas IV-54-9, IV-54-13, Prop IV-54-16) to d = 4 | AM1's separation step needs one compact convex class. The comparison state of Y3 Prop IV-29-40 is invariant only under 𝔗 ⊕ Z(2v_h) (Y3 L78698–78720), not under all translations, so the translation-invariant class does not contain it. Fixed spacing, reads no RG rank. | Y3 Prop IV-54-16 at d = 4: every periodic Wilson DLR state is invariant under a common translation group | a proof of diagonal positivity for the cubic volume-first state without a separation over all periodic states |
| 12 AM1, all mirrors (SA L2749) | outline's statement, proved by porting Y3 Prop IV-29-40 (lower tangent, folding, Jensen on adapted split tori), Prop IV-54-17 (separation, reflection invariance) and Cor IV-54-31 (passage to the limit) | Lemma S. T0 reads diagonal mirrors in O6, S10 and, for every component, in O9. Our site-plane positivity covers coordinate mirrors on cubic tori only. | Y3 Prop IV-29-40 at a diagonal mirror in d = 4, with crossing-kernel positivity on adapted split tori (SA L2773) | as for rank 11 |
| 16 E3 (SA L4226) | off | T0 allows a subsequential limit, as Theorem 0′ does | none | uniqueness or whole-sequence convergence joins T0 |
| 17 UI (SA L28489) | outline's UI = YM3_I (R5) (Y3 Props IV-55-9, IV-55-19, IV-56-17) | the plate kernels need a bound uniform in the number of surrounding fields. Our upper-chain Theorem 9(d) gives a closable insertion only. RPM1's slab bound needs (i), false by Lemma N. | Y3 Prop IV-55-9 (multiple reflections with an insertion) at d = 4, from D1's rooted source bound | none found |
| 18 AK (SA L29028–29774) | outline's AK, cross-read with Y3 L75578–76680 (slab operators, point fields, plate kernels) | no shorter route found. RPM1 builds the same kernels from (i). | the AK tube/product construction (SA L29028) from PD | none found |
| 19 TU + AC (SA L30071–30848) | outline's TU and AC, cross-read with Y3 L75872–77017 | RPM1's elimination (convexity, M_{2a} ∈ 8Z from the 45° rotated law, RPM1 L2438–2590) closes only if the band constant ℘ < 4. The outline has ℘ = p + 5 ≥ 5 (SA L28789). So polygon divisibility stays, and the two-point step needs TU10 (SA L30091): S₂(f,h) ≤ u(d)‖f‖_∞‖h‖_∞ with u(d) → 0. TU10 says that the coupling vanishes at short distance; a scale-invariant dimension-4 field would fail it. The outline reads it from F2–F3 (SA L4412). So F2–F3 are on O(4)'s path, not only on the witness's. | TU10 directly from D1 and the flow E1, as an upper bound with the factor g(d)⁴, without F2's exact coefficient | a plate density with ℘ < 4 (then RPM1's elimination replaces AC and TU) |
| 20 H3 (SA L4616, L31688) | off T0's clauses; corollary node O11, cited | GOAL states T0 as the OS axioms with growth. If the owner wants the Wightman theory inside T0, port YM3_I's direct scalar reconstruction (Y3 Thm IV-76-59, L79749–81160). It reads the UI/PD bounds already on the path. It avoids rebuilding OS II's analytic continuation. | owner decision first | the owner puts the Wightman theory into T0 |
| K components, clustering (SA G3 L4486, L31278) | outline's G3 and canonical decomposition, ported from Y3 L77017–78324, L79580–79749 | the moments of O define no measure on S′(R⁴) (Lemma N), so QED3's abstract ergodic decomposition (QED3.tex L21721) is not available. Components are built at fixed spacing by conditioning on invariants. | the lattice clustering estimate (Y3 Prop IV-31-51) at d = 4, rate |v|^{−2} | uniqueness of the vacuum proved directly |

## 3. Nodes, top down

One line per statement: what it says, where it is stated, its inputs by node, its state. Inputs that are whole layers are named by layer.

### 3.1 The clauses of T0

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| T0 | Section 1 | GOAL.md; SA L7017–7038 | O1–O10 | open |
| O1 | volume-first limits exist: periodic Gibbs states ν_j at first-passage data (K_j, β_j), K_j → ∞; one subsequence converges on every separated C¹ tuple | SA 0(a)(iii) L6915; L24376, L24889; Y3 L72903–74672 | S1b, S2, S3, S4, E1 | cited |
| O2 | the limit is invariant under translations and W₄, RP at coordinate mirrors, symmetric, real, regular on E^n_≠ | SA 0(b)(i)–(iv); L525, L24651 | O1, S1g | cited. Ours covers torus limits only (upper-chain Lemmas 1.1, 1.2) |
| O3 | E0′: one diagonal-flat extension, abs S_n(φ) ≤ c C^n (n!)^κ abs(φ)_{kn} | SA 0(b)(v); H1 L4572; QF3 L24960 | S5 | cited |
| O4 | OS space H(S): e^{−tH} strongly continuous, H ≥ 0, HΩ = 0, spatial translations, W₃ | SA 0(b)(v); H2 L4600; HB3 L25491 | O2, S6 | cited. Ours: upper-chain Theorem 9(a), an implication from (SM) |
| O5 | RP at every coordinate and diagonal mirror, in the limit | SA 0(b) last sentence; Y3 Cor IV-54-31 | S1g, O1 | cited |
| O6 | spectral cone H ≥ abs(P_j), j = 1, 2, 3 | SA 0′(1); L25736–25904; Y3 L75249–75578 | O4, O5 | cited |
| O7 | O(4) invariance on separated C¹ tuples and on the diagonal-flat domain | SA G2 L4441; L30848 | O3, O6, S7–S11 | cited |
| O8 | canonical decomposition (X, λ, σ_ξ), unique; ker H ≅ L²(X, λ) | SA 0′(2); L31278; L31442 | S12, S13, S14 | cited |
| O9 | each σ_ξ has O2–O7 with the same constants, a unique vacuum, the forward cone and clustering at rate abs(v)^{−2}, uniform in ξ | SA 0′(3) | O8, S3, S1g; S7–S11 and S16 for every periodic state, through S15 | cited |
| O10 | NT1 and NT2 of GOAL.md on the limit | GOAL.md; `parts/witness.md` Text 8.1 | W1, W2 | open |
| O11 | corollary, not a clause: one scalar Wightman theory per component | SA 0′(4); H3 L4616, L31688 (OS II §IV.1) | O3, O5, O7, O9 | cited |

### 3.2 Lattice mirrors (G1; ranks 11, 12)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| S1a | finite-cutoff Wilson measures with Haar measure | SA L238–294 | none | cited |
| S1b | fixed-spacing DLR existence; periodic limits are DLR states | SA L442, L24376 | S1a | cited |
| S1c | rank 11: all periodic DLR states have one common translation group | SA L2112; Y3 Prop IV-54-16 | S1b | cited |
| S1d | positive crossing kernels on adapted split tori (SU(2) Gram expansion); coordinate mirrors on cubic tori (Osterwalder–Seiler) | SA L2773; Y3 L78336–78522 | S1a | cited. Coordinate case written in upper-chain Lemma 1.1 |
| S1e | finite chessboard inequality | SA L2885 | S1d | cited |
| S1f | lower tangent of the pressure at a periodic DLR state; folding inequality | SA L2944, L2993; Y3 L73102–74343 | S1b | cited |
| S1g | rank 12, AM1: every periodic state is RP and invariant at every coordinate site, coordinate bond and diagonal mirror, on the bounded half-space algebra | SA L2749, L4429; Y3 Props IV-29-40, IV-54-17 | S1c–S1f | cited |
| S1h | Lemma S: no period lattice is adapted to a coordinate and a diagonal mirror of one plane | Section 2 | none | proved |

### 3.3 From source bounds to all states (R, C)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| D1 | rank 10: torus (ST5)–(ST6): holomorphic point counterterms, localized source energies with e^{−κ m(X)} on the rooted indexing, entropy gap, normalized upper stability, unsourced floor; uniform in cutoff and torus | SA L4088; L22947; L23385–23541 | 2.13, 2.10, C1–C4, B4, WF, A1–A3, E1 | open. Our UV-CT (`parts/upper-chain.md` Text 7) is a consumer form of it; `gates/uv-ct-upper-chain-41489e4876.md`: the implications hold, UV-CT is open |
| S2 | D2: graded all-state bound abs S^T_n[ν] ≤ [2B(R)]^n (n!)^k max{1, d^{−5n}} Π‖f_i‖_♯ | SA L4138; L24078–24117; L24302 | D1, S1e | cited |
| S3 | D4, G4: all-state one-point differences and cumulant bounds; common cell normalizers | SA L4179, L4541; L23640, L23833, L23906 | D1, S1g | cited |
| S4 | compactness on separated tuples: countable extension, moving tests, mirrors, one-point and cumulant limits | SA L479, L24541–24889; Y3 L72903–74672 | S3 | cited. Ours: upper-chain Theorems 8, 10.2, for torus limits only (Lemma S) |
| S5 | H1, QF3: diagonal-flat extension with factorial growth; constrained density | SA L4572, L24960, L31589 | S2 | cited |
| S6 | H2: Hilbert bridge and continuous evolution, also on the extended domain | SA L4600, L25491 | O2, S3 | cited |

### 3.4 Rotations (G2; ranks 17–19)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| S7 | rank 17, UI: one-field Hilbert insertion bound C η^{−p}‖k‖_♯, independent of the number of surrounding fields | SA L28489; Y3 Props IV-55-9, IV-55-19, IV-56-17 | D1 (rooted), S1g, S6 | cited |
| S8 | PD: analytic plate density and L¹ plate bound with exponent ℘ = p + 5; scaled parametrix | SA L28832, L28639, L28789 | S7, O6 | cited |
| S9 | rank 18, AK: product kernels on tubes, smoothing removal, frame gluing, Gram kernel, finite band 4abs(m) ≤ ℘n, boost positivity, cut inequality | SA L29028–29774; Y3 L75578–76680 | S8, O2, O6 | cited |
| S10 | TU: every nonconstant two-point harmonic vanishes, the critical frequency included | SA L30071–30470; Y3 L75872–76220 | S9, O5, S16 | cited |
| S11 | rank 19, AC: polygon divisibility, discrete convexity, local translations, removal of exceptional support, O(4) at all orders | SA L30582–30848; Y3 L76680–77017 | S9, S10 | cited |
| S16 | TU10: 0 ≤ S₂(f,h) ≤ u(d)‖f‖_∞‖h‖_∞ on the shape class 𝔗(d; ϑ_*), with u(d) → 0 | SA L30091; derivation L4412 | F2, F3 (outline route); D1 and E1 (candidate, Section 2) | open |
| S17 | Lemma N: RPM1's hypothesis (i) fails for O | Section 2 | none | proved |

### 3.5 Components and clustering (G3, K)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| S12 | G3, PL3: uniform lattice plateau law (transfer carrier, plateau identification, positive-filter momentum density, closedness of the ergodic RP class) | SA L4486, L3238–3722; Y3 L77017–77560 | S1g, S3 | cited |
| S13 | conditional kernels on compact spaces; fixed-spacing DLR decomposition; canonical decomposition with uniform clustering | SA L30875, L31180, L31278; Y3 L77560–78324, L79580–79749 | S12, S3, S4 | cited |
| S14 | PV4: ker H ≅ L²(X, λ) | SA L31442; Y3 Thm IV-36-25 | S13, O4 | cited |
| S15 | rank 13, 7.6: one common reference/all-state normalizer; carries the UV law to every periodic state with O(d²) error | SA L26062, L26934; L26765–26934 | D1, S1g, F2 | open |

### 3.6 Ultraviolet law and flow (V, T, E, P)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| F1 | free-kernel comparison; exact continuum coefficient | SA L4252 | none | cited. Our `library/nt2-free-value-by-hand.md` is a different free computation |
| F2 | rank 8: positive leading two-point law, uniform in state and position, on the full bump class | SA L4289; 7.3 L26085; L26222–26494; L27149–28205 | D1, B3, F1, 4.14, D3, S15, A1–A3 | open |
| F3 | rank 15: logarithmic running at the witness scale; constant-source normalization ζ → 1 | SA L4360; L32030 | F2, B3, E1, D1 | open |
| 4.14 | rank 14: weighted surviving-lineage age tail | SA L23300, L23315 | 2.13, 2.10, S1e | open |
| D3 | age-resolved uniform rarity; live-cell probabilities | SA L4165; 4.13 L23258 | C3, 2.13, S1e | open |
| E1 | consistent flow x_j = β − Σ b_i up to first passage, with positive block drift | SA L4197; L19867; 3.1 L20719, 3.4 L21456, 3.8 L22042 | B3, B4, C4 | open |
| B3 | rank 9: one-loop law for b_j⁰ with a summable lattice correction and controlled nonlinear errors | SA L3986 | A1–A3, B2, F1 | open. Ours: Theorem P1, `gates/p1-gate-2f2ec0f89.md` CORRECT-NO-ADVANCE with one WRONG; row 151 `prefactor` open |
| E2–E4, 2.12 | tuned calibration, matched cutoffs, aged loads | SA L4207–4252; L23358 | none | off (T0 allows a subsequence) |
