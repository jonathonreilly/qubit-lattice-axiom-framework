lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T00:30Z

# T0 skeleton (queue row 155)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, pinned at `3f78ce873`. Author work. Not an audit. Not yet checked by the other model. Nothing here grants status.

Credit: the node structure is the outline of Ethan Sussman and Levent Alpoge (`YM4_sketch_500.tex` at `31a47c543775`, with Claude and Codex as authors of their text), its catalogue A1–H4 (SA L3757–4644) and Theorems 0, 0′ (SA L6915–7038). The 3D sources read for the route choice are their `YM3/YM3_I.tex`, `QED3/QED3.tex` and `RP O(d) trick (RP1)/RPM1.tex` at the same commit, fetched to a scratch folder, not committed; RPM1 is credited as their README states (half written by Sussman, completed by Astra). Balaban (CMP 89–122) and Dimock enter through the rebuilt rows. `SA L` is a line of `YM4_sketch_500.tex`; `Y3 L` is a line of `YM3_I.tex`.

States used: **checked** = proved here and checked line by line once by the other model (files named); **proved** = proved here, not yet checked by the other model; **open**; **cited** = stated in the outline or YM3_I, not rebuilt here; **off** = not on T0's path. A checked result is still an implication from its named inputs.

## 1. T0, pinned

T0 (GOAL.md, owner 2026-11-03), pinned to the outline's Theorem 0′ (SA L7017–7038) with 0(a)(iii), 0(b), 0(c)(4) until the OpenAI write-up is public: SU(2), Wilson action, observable O(f) = Σ_p f(x(p)) a_p (the tr F² sector). There is a volume-first limit S on separated tests in R⁴ with a canonical decomposition S = ∫σ_ξ dλ(ξ). Each σ_ξ satisfies E0′ (diagonal-flat extension with factorial growth), E1 (R⁴ ⋊ O(4) invariance), E2 (reflection positivity), E3 (symmetry, reality), E4 (clustering). The limit is non-trivial in the sense NT1 + NT2 of GOAL.md.

Reconstruction of a Wightman theory (OS II, §IV.1, E′→R′) is a corollary of E0′–E4. It is node O11 below, not a clause of T0 (owner to confirm; Section 2, R20).

## 2. Route at ranks 11, 12, 16–20 and K

Two short lemmas decide the choice. Both are proved by Claude here, not yet checked by the other model.

**Lemma S (no torus is adapted to both mirror families of one plane).** Use YM3_I's definition (Y3 L73363): a period lattice Γ ⊂ Z⁴ is adapted to a normal m if Γ = (Γ ∩ m^⊥) ⊕ Zv with v = hm/abs(m)², h > 0. Then no Γ is adapted to both m = e_4 and n = e_1 − e_4.
*Proof.* Adaptation to m gives Γ ∩ Rm = Zv, and the projection along m^⊥ maps Γ onto Zv. Adaptation to n makes the reflection θ_n (swap of x_1 and x_4) preserve Γ, since θ_n fixes Γ ∩ n^⊥ and sends v to −v. Write Γ ∩ Re_4 = pZe_4 and Γ ∩ Rn = qZn, with p, q positive integers. Then p e_1 = θ_n(p e_4) ∈ Γ. Its projection along n^⊥ is (p/2)n, so p ∈ 2qZ. Also qn ∈ Γ, and its projection along e_4^⊥ is −q e_4, so q ∈ pZ. Hence p ∈ 2pZ, which is false. ∎
*Consequence.* The torus proof of reflection positivity (two-mirror positivity, Y3 Prop IV-16-26) needs a period lattice adapted to the mirror. By Lemma S, no torus has this for a coordinate mirror and a diagonal mirror of the same plane. The spectral cone (O6) and the two-point step of the rotation proof (S10) need both in one state. So diagonal positivity comes through infinite-volume periodic states (AM1), and the limit is volume-first. Our joint torus extraction (upper chain Theorems 8, 10.2) serves T1 only.

**Lemma N (RPM1 Theorem A does not apply to O).** Let μ be a law with RPM1 hypothesis (i): E e^{F(χ)} ≤ exp C(‖χ‖₁ + ‖χ‖₂²) for real χ. Let f, h have values in [0,1] and supports in balls of radius d ≤ 1. Then |E F(f)F(h)| ≤ C′d⁴.
*Proof.* Put X = F(f+h) and u = d^{−2}. From cosh y − 1 ≥ y²/2, E X² ≤ u^{−2}(E e^{uX} + E e^{−uX} − 2). By (i) with χ = ±u(f+h), each exponential moment is at most exp C(2u|B_d| + 4u²|B_d|) ≤ e^{C₁}, since |B_d| = (π²/2)d⁴. So E X² ≤ 2(e^{C₁} − 1) d⁴. Finally 4 E F(f)F(h) = E X² − E F(f−h)² ≤ E X². The same steps with f − h in place of f + h give the lower bound. Also |E F(f)| ≤ C₂d⁴ by Jensen and (i), so the connected value is O(d⁴) too. ∎
*Consequence.* The outline's law 0(c)(4) on R⁴ gives a connected two-point value of at least c g(d)⁴ ≈ c′(log 1/d)^{−2} on its shape class at scale d. The one-point part is O(d⁴). This contradicts Lemma N for small d, and NT2 contradicts it the same way. So hypothesis (i) fails for every non-trivial asymptotically free O, and RPM1 cannot be applied as stated. (QED3 applies Theorem A (QED3.tex L21579): there the Gaussian bound (i) is available for F_{μν} in d = 3.)

| Rank | Choice for T0 | Reason | First statement to prove | Reverses if |
|---|---|---|---|---|
| 11 link symmetry, common period (SA L2112) | outline's statement, proved by porting YM3_I's shorter proof: temporal gauge and two-layer determination (Y3 L78814–78969, Lemmas IV-54-9, IV-54-13, Prop IV-54-16) to d = 4 | AM1's separation step needs one compact convex class. The comparison state of Y3 Prop IV-29-40 is shown invariant only under 𝔗 ⊕ Z(2v_h) (Y3 L78700–78712, L78789), not under all translations, so the translation-invariant class does not contain it. Fixed spacing, reads no RG rank. | Y3 Prop IV-54-16 at d = 4: every periodic Wilson DLR state is invariant under a common translation group | a proof of diagonal positivity for the cubic volume-first state without a separation over all periodic states |
| 12 AM1, all mirrors (SA L2749) | outline's statement, proved by porting Y3 Prop IV-29-40 (lower tangent, folding, Jensen on adapted split tori), Prop IV-54-17 (separation, reflection invariance) and Cor IV-54-31 (passage to the limit) | Lemma S. T0 reads diagonal mirrors in O6, S10 and, for every component, in O9. Our site-plane positivity covers coordinate mirrors on cubic tori only. | Y3 Prop IV-29-40 at a diagonal mirror in d = 4, with crossing-kernel positivity on adapted split tori (SA L2773) | as for rank 11 |
| 16 E3 (SA L4226) | off | T0 allows a subsequential limit, as Theorem 0′ does | none | uniqueness or whole-sequence convergence joins T0 |
| 17 UI (SA L28489) | outline's UI = YM3_I (R5) (Y3 Props IV-55-9, IV-55-19, IV-56-17) | the plate kernels need a bound uniform in the number of surrounding fields. Our upper-chain Theorem 9(d) gives a closable insertion only. RPM1's slab bound needs (i), false by Lemma N. | Y3 Prop IV-55-9 (multiple reflections with an insertion) at d = 4, from D1's rooted source bound | none found |
| 18 AK (SA L29028–29774) | outline's AK, cross-read with Y3 L75578–76680 (slab operators, point fields, plate kernels) | no shorter route found. RPM1 builds the same kernels from (i). | the AK tube/product construction (SA L29028) from PD | none found |
| 19 TU + AC (SA L30071–30848) | outline's TU and AC, cross-read with Y3 L75872–77017 | RPM1's elimination (convexity, M_{2a} ∈ 8Z from the 45° rotated law, RPM1 L2438–2590) closes only if the band constant ℘ < 4. The outline has ℘ = p + 5 ≥ 5 (SA L28789). So polygon divisibility stays, and the two-point step needs TU10 (SA L30091): S₂(f,h) ≤ u(d)‖f‖_∞‖h‖_∞ with u(d) → 0. TU10 says that the coupling vanishes at short distance; a scale-invariant dimension-4 field would fail it. The outline reads it from F2–F3 (SA L4412). So F2–F3 are on O(4)'s path, not only on the witness's. | TU10 directly from D1 and the flow E1, as an upper bound with the factor g(d)⁴, without F2's exact coefficient | a plate density with ℘ < 4 (then RPM1's elimination replaces AC and TU) |
| 20 H3 (SA L4616, L31688) | off T0's clauses; corollary node O11, cited | GOAL states T0 as the OS axioms with growth. If the owner wants the Wightman theory inside T0, port YM3_I's direct scalar reconstruction (Y3 Thm IV-76-59, L79749–81160). It reads the UI/PD bounds already on the path. It avoids rebuilding OS II's analytic continuation. | owner decision first | the owner puts the Wightman theory into T0 |
| K components, clustering (SA G3 L4486, L31278) | outline's G3 and canonical decomposition, ported from Y3 L77017–78324, L79580–79749 | the construction gives separated moments only; no law on S′(R⁴) is built, and Lemma N excludes one with RPM1's bound (i). So QED3's decomposition of a continuum law (QED3.tex L21721) is not available. Components are built at fixed spacing by conditioning on invariants. | the lattice clustering estimate (Y3 Prop IV-31-51) at d = 4, rate abs(v)^{−2} | uniqueness of the vacuum proved directly |

## 3. Nodes, top down

One line per statement: what it says, where it is stated, its inputs by node, its state. The headings name the thirteen positions of `library/sa-ledger.md` (L, M, G, E, N, P, C, T, R, K, H, V, Z).

### 3.1 The clauses of T0 (Z, assembly)

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

### 3.2 Lattice mirrors (L; G1; ranks 11, 12)

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
| F2 | rank 8: positive leading two-point law on the full bump class, uniform in position; on the reference torus (7.3), then for every periodic state through S15 | SA L4289; 7.3 L26085; L26222–26494; L27149–28205 | D1, B3, F1, 4.14, D3, A1–A3 | open |
| F3 | rank 15: logarithmic running at the witness scale; constant-source normalization ζ → 1 | SA L4360; L32030 | F2, B3, E1, D1 | open |
| 4.14 | rank 14: weighted surviving-lineage age tail | SA L23300, L23315 | 2.13, 2.10, S1e | open |
| D3 | age-resolved uniform rarity; live-cell probabilities | SA L4165; 4.13 L23258 | C3, 2.13, S1e | open |
| E1 | consistent flow x_j = β − Σ b_i up to first passage, with positive block drift | SA L4197; L19867; 3.1 L20719, 3.4 L21456, 3.8 L22042 | B3, B4, C4 | open |
| B3 | rank 9: one-loop law for b_j⁰ with a summable lattice correction and controlled nonlinear errors | SA L3986 | A1–A3, B2, F1 | open. Ours: Theorem P1, `gates/p1-gate-2f2ec0f89.md` CORRECT-NO-ADVANCE with one WRONG; row 151 `prefactor` open |
| E2–E4, 2.12 | tuned calibration, matched cutoffs, aged loads | SA L4207–4252; L23358 | none | off (T0 allows a subsequence) |

### 3.7 Histories and large fields (H, Package C; ranks 5–7)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| C1 | every operation is a total Borel positive kernel or change of variables that keeps the sourced invariant integral | SA L4041; 1a.2.3 L7463 | none | open. Map only: `library/sa-histories.md` |
| C2 | histories keep margins, determining sets and nonwrapping geometry, with a matching entropy bound | SA L4052; 2.3 L17398 | 2.4 | GEO1–GEO6, EXT-out, W3: checked under three supplied rules (`library/geo-prop23.md`, `geo-2.md` to `geo-5.md`, `geo5c-count.md`; `gates/geo-gate.md`, `gates/geo5c-gate.md`). Rest of C2: open |
| C3 | each created component has mass ≤ exp[−c p₀(g_j) − κ abs(X)_j], with Wilson payment, complex suprema and insertion costs kept | SA L4063; 2.5 L17676, 2.6 L17719, 2.7 L17794, L18334 | 2.4, 2.8, 2.13, C2 | floor screening (Theorem R): checked as an implication (`library/floor-screen.md`; `gates/floor-screen-gate.md`, `support-envelope-gate.md`, `support-physical-gate.md`). Mass bound: open |
| C4 | one nonempty presentation class is mapped into itself by the exact step, with one simultaneous order of constants | SA L4075; 2.11 L19435–19470 | C1–C3, 2.8, 2.10, 2.13, B4, WF, A1–A3 | open |
| 2.4 | prepared-box minimizer: unique regular orbit, analytic in exterior data, uniform gap (Balaban CMP 122 Prop. 1) | SA L17656 | A1, A3, GEO4 | checked as an implication (`library/ref-chart.md` Theorem 2.4; `gates/ref-chart-gate.md`, `gates/ref-chart-regate.md`) |
| 2.8 | rank 5: prepared, reference and healed actions cancel to a paid core, a positive quadratic form and a remainder ≤ C g_k^{1/2} | SA L17598, L17854 | A3 (L), 2.4, C2 | checked as a conditional implication (`library/sa-2.8-terms.md`; `gates/sa-2.8-terms-gate.md`, repairs there). Open: I1 and the Gaussian comparison of 2.8-T^C (`library/ref-chart.md`) |
| 2.13 | rank 6: loaded labels and history masses sum to the normalized extensive bound, creation payments kept; feeds OSF16 (SA L19782) and D1 | SA L17820, L18944–19406 | 2.8, 2.10, 2.4, C2, C3 | partial. Proved, not yet checked: `library/sa-2.13.md`, `library/sa-2.13-2.md` (Codex). Checked: the joint chart (`library/ref-chart.md`). Open: (8.1) for the literal operations; Pre, Inn, Act comparisons of V_X; (4.1) for curved carrier series; rigidity on every compatible fibre |
| 2.10 | rank 7: healed deletion and restriction factor exactly on the actual read and support sets; the connected sum has local activity bounds | SA L17451, L18877 | C1, C2, 2.8 | open (row 142 `s210`) |
| OSF16 | the weighted total-variation label sum supplies the integrated normalization | SA L19782; OH4 L23439; floor L23481 | 2.13 | open |

### 3.8 The exact nonlinear step (N; rank 4)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| B1 | polymer majorant with strict complex room (Kotecký–Preiss form) | SA L3910; L1191–1310 | none | cited (abstract part); actual activities open |
| B2 | pointed marginal extraction | SA L3937 | A2, A3 | cited |
| B4 | the ordinary step is uniformly holomorphic on its product box; finer derivatives on their own domains; the small-field one-step map 1.6 | SA L4006; L7569; L22879 | A1–A3, WF, B1 T0 reads only the ordinary step and 1.6; the typed potential, zone and joint tests are off T0's path (SA 3779-3780, 4469-4470, 5115, 5119; FINISH row 227). Ordinary B4: one-level implication checked (rows 210-222), defect sector closed for constant sources (rows 239, 242), nonconstant sources by `src-array.md` (row 241, not yet checked); first open input (D4). | open. Ours is real only (`library/one-step-closure.md`, `gates/closure-bad958abb.md`) and does not replace it |
| WF | rank 4: every nested substitution of the window stays in its hereditary pair core | SA L15879; WF15 L16327; LB14 L16584 | A1–A3, 2.4 | partial, checked: tower estimate and room (`library/wf-room-2.md`, `gates/wf-room-2-gate.md`), (O1) (`library/o1-decoupled.md`, `gates/o1-decoupled-gate.md`), removed-map comparison (`library/removed-fix.md`, `gates/removed-fix-gate.md`), R9 bounds [PW], [NL] (`library/pw-bridge.md`, `library/nl-r9.md`, `gates/pw-bridge-gate.md`), `library/dec-field.md` (`gates/dec-field-gate.md`) |
| WF7 | the removed factor e^{−cM/σ_j} of the window estimate | SA L15850–15866 | WF, A3 | open. No proof through WF4's actual pair (`library/old-depth.md`, `gates/old-depth-gate.md`); projection-first fails (`library/wf7-extension.md`, `gates/wf7-extension-gate.md`). Live: row 156 `wf7-bf` (Balaban CMP 109 (3.18)–(3.25)); row 153 `cp-old-proj` with `library/joint-loc.md` (not yet checked) |
| WF-c | 6(c) for the window's box at complex data; the Landau node-lift comparison; pointed-core admission (10.2) | `library/a1-balaban.md` (10.2); `library/a3-close.md` Lemma T | A1, A3 | open (hereditary part of (10.2) proved in `library/a3-close.md`, checked in `gates/a3-close-meet-gate.md`) |

### 3.9 Backgrounds and propagators (G, M; ranks 1–3)

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| F0–F5 | Balaban's flat propagator package (CMP 89, 95, 96), uniform in depth and mesh, level-0 seam | `library/flat-port.md` | none | checked (`gates/flat-port-gate.md`) |
| LU | lattice Uhlenbeck gauge (Lemma U); quadratic (LC) | `library/lattice-uhlenbeck.md`, `library/seam-quadratic-c.md` | none | checked (`gates/share-check-199fac1cb.md`) |
| A1 | rank 1: unique regular constrained critical orbit, Borel in real data, holomorphic nearby, constants free of depth (Balaban CMP 102 Thm 1) | SA L3811 | F0–F5, LU | checked as an implication on separated sequences (`library/a1-balaban.md`, `gates/a1-balaban-gate.md`). Open: (10.2) (moved to WF-c) |
| A2 | rank 2: coercivity Re⟨B, EB⟩ ≥ c‖B‖² on gauge-fixed fibres, c/2 on complex neighbourhoods | SA L3835 | F0–F5, A1, A3 | checked as an implication (`library/a2-curved.md`, `a2-layers.md`, `a2-full.md`, `h-walk.md`, `h-walk-fix.md`; gates of the same names). Open inputs: (H-ct) counterterm accounting (SA L7864), (H-prof) |
| A3 | rank 3: weighted inverse and response bounds at real and complex regular backgrounds, independent currents, periodisation | SA L3864 | F0–F5, A1, P82° | real-critical chain checked (`library/a3-profile.md`, `a3-derivative.md`, `p82-curved.md`, `a3-close.md`, `meet-6c.md`, `a3-clauses.md`, `assign-adopt.md`; gates of the same names, `gates/a3-balaban-reads-gate.md`). Open: WF-c |
| P82° | weighted curved inverse at a regular critical reference | `library/p82-curved.md` | F0–F5, A1 | checked (`gates/p82-curved-gate.md`) |
| A4 | uniform intertwining between averaging schemes | SA L3898 | A1–A3 | cited; read only if the averaging scheme changes. Definition A is adopted (`library/assign-adopt.md`, checked in `gates/a2-full-gate.md`) |

### 3.10 Non-triviality and the splice

| Node | Statement | Where | Inputs | State |
|---|---|---|---|---|
| W1 | NT1: H is not zero on the orthocomplement of Ω | GOAL.md | F2 law on R⁴ (SA 0(c)(4)), by Lemma W below; row 152 `nt1-window` is a fallback | open (Lemma W proved here, not yet checked) |
| W2 | NT2: across scales, gauge-invariant correlators equal their leading perturbative values in g_r, with the three-gluon vertex part (NT2-V), and g_r runs at the one-loop rate | GOAL.md; `parts/witness.md` Text 8.1 | F2, F3, S15, X1 | open. The outline gives the R⁴ law only with abs(ε) ≤ 1/2 (SA 0(c)(4)); NT2 needs ε → 0 on R⁴ and the vertex part |
| X1 | the witness reads the outline's law, blocking map, gauge and observables without a change of law | `library/route-decisions.md` §8 | none | open |

**Lemma W (NT1 from the R⁴ two-point law).** Proved by Claude here, not yet checked. Fix ϑ_W ≤ 10^{−7}. Assume the law SA 0(c)(4) on R⁴ for C¹ pairs in 𝔗(d; ϑ_W) at one d ≤ d₀, with abs(ε) ≤ 1/2 (this needs g ≤ γ_W(ϑ_W)). Then H ≠ 0 on Ω^⊥.
*Proof.* Suppose H = 0 on Ω^⊥. Since HΩ = 0, e^{−tH} = 1, so σ(θF̄·τ_t G) = ⟨[F], e^{−tH}[G]⟩ does not depend on t ≥ 0 (O4). Put ρ = d/20 and c = (d + 2ρ)/2 > ρ. Let f₀, h be C¹ bumps of height 1 on balls of radius ρ centred on the time axis at times c. Their slopes can be at most 3/ρ, so they lie in 𝔗(d; ϑ_W) once the centre distance is right. Let f = θf₀. Then σ(f, τ_t h) is constant in t, and so is its connected part, because the one-point part is constant. At t = 0 the centre distance is d + 2ρ; at t = 4d − 2ρ it is 5d. Both pairs are in 𝔗(d; ϑ_W) at the same d, so the prefactor of K_free is the same. K_free changes by a factor at least ((5d − 2ρ)/(d + 4ρ))⁸ > 7·10⁴. On R⁴ the error factor obeys (1 − 1/2)(1 − η̄)⁴ ≤ 1 + η ≤ (1 + 1/2)(1 + η̄)⁴ with η̄ ≤ 1/3, so the ratio of the two error factors is at most 48. So the two connected values differ, a contradiction. ∎
*Consequence.* F2 is on T0's path through TU10 (Section 2, R19). With F2, NT1 needs no further lane; row 152 `nt1-window` stays a fallback.

**Off T0's path:** E2–E4 and 2.12 (tuned and matched runs), the Ward route of 0(e) (SA 9.1, 9.3, 9.7–9.11, L6979–7014), the four-point clause 7.5 (SA L25990), F4 (full gauge-theory identification, SA L4416), the mass gap. O11 (reconstruction) is a cited corollary.

## 4. What this item moved, and what it does not show

Moved: (1) the map of T0, with every node located and its state named. (2) The route at ranks 11, 12, 16–20 and K (Section 2). (3) Lemma S: diagonal positivity must come through periodic states, so T0's limit is volume-first and our joint torus extraction serves T1 only. (4) Lemma N: RPM1 Theorem A cannot be applied to O, so O(4) follows the outline's UI–PD–AK–TU–AC route, ported from YM3_I where the 3D text is the same. (5) F2–F3 are on O(4)'s path through TU10, so row 152 no longer takes rank 8 off the path for T0. (6) Lemma W: NT1 follows from the F2 law on R⁴.

Changes the queue would need (for the lead): a lane for TU10 from D1 and E1 (Section 5, item 2); lattice-only port lanes for items 10 and 11, which read no RG rank; row 152 becomes a fallback.

Does not show: any open node. The states of cited nodes are the outline's claims, not checked here. Lemmas S, N and W are proved by Claude and not yet checked by the other model. No numeric job was run. Line numbers in YM3_I, QED3 and RPM1 refer to commit `31a47c543775`.

## 5. Open nodes, hardest first

Each line: the node, then the first statement a lane should prove. "Hardest" means the most likely place for the chain to die.

1. **WF7** (rank 4). First: the physical identity of Balaban's box-first map Φ(s,t,ν) with WF4's box map at every t (SA L9776–9780, Lemma CR of `library/old-depth.md`) at complete physical pairs. This is row 156 `wf7-bf`; row 153 is its fallback.
2. **F2 → TU10** (ranks 8, 13, 14, with D3). The outline itself leaves an obstruction open here: the complete-force identity GCB52 (SA L28205) carries an extra old-activity and exterior force. First: TU10 (S16) as an implication from D1 and E1: on 𝔗(d; ϑ_*), S₂(f,h) ≤ C g(d)⁴‖f‖_∞‖h‖_∞, an upper bound only, for every periodic state. If that fails, the finite-cutoff identity 7.3 on the reference torus (SA L26085). F2 is needed twice: by TU (O(4)) and, with S15, by NT1 (Lemma W) and NT2.
3. **2.13** (rank 6). First: the prepared comparison (Pre) of V_X on the actual prepared substitutions, sup abs(V_X^{Pre}) ≤ C N₀ (`library/ref-chart.md` Section 9 as left by `gates/ref-chart-regate.md`). The lane's first section checks `library/sa-2.13.md` and `library/sa-2.13-2.md` (Codex) line by line, since it reads them.
4. **C4** (2.11). First: one written order of choice for every constant used by A1–A3, WF, 2.4, 2.8, C2 and the step of SA L19435–19470, with a check that no constant is chosen before one it depends on. A circular order kills the induction, so this cheap table comes early.
5. **2.10** (rank 7). First: exact factorisation of healed deletion and restriction on the actual read and support sets (`library/sa-histories.md` 3.2), counterexample first. This is row 142 `s210`.
6. **D1** (rank 10). First: the unsourced torus floor from one admitted all-small-field label with its own action bound (SA L23481), verified on the checked backgrounds. Then the upper stability bound OH4 (SA L23439) from OSF16 and 2.13.
7. **B4 and 1.6**. First: the small-field one-step map is holomorphic on its product box with the radius ratios of SA L7569, at complex data, reading A1–A3.
8. **B3 and E1** (rank 9). First: row 151 `prefactor`, the Gaussian integration identity for the local flux coefficient at the actual critical branch.
9. **S7–S11** (ranks 17–19). First: Y3 Prop IV-55-9 (multiple reflections with an insertion) at d = 4, conditional on D1's rooted bound; then PD with ℘ = p + 5 (SA L28789). Port from YM3_I; credit Sussman–Alpoge.
10. **S1c, S1g** (ranks 11, 12). First: Y3 Prop IV-29-40 at a diagonal mirror in d = 4 (lower tangent, folding, Jensen on adapted split tori, SU(2) crossing kernel). Lattice-only: it can run on any free machine now.
11. **S12–S14** (K). First: Y3 Prop IV-31-51 (lattice clustering estimate) at d = 4, rate abs(v)^{−2}. Lattice and Hilbert-space only, given S3.
12. **S2, S5** (growth). First: SA QF3 (L24960) from D2, with the factorial loss and seminorm order linear in n.
13. **W2 and X1**. First: X1, the reading of the witness on the outline's law and blocking map; then NT2 on R⁴ with ε → 0 (the outline has only the two constant bounds there, SA L6888).
14. **Leaves**: (H-ct) and (H-prof) of A2; WF-c; C1; the rest of C2; the C3 mass bound; F3; S15; 4.14; D3. Each starts from the SA line in its row.


## Convergence point, 2026-11-04

After rows 221-253 the open inputs of ordinary B4, 1.6, (LOC), (Gamma), (FG) and (R-cov) reduce to one: **(D4), complex domain admission of every carried composition** (lifted and stage cores, stored arguments, healing gauges, logarithm charts, with room), the outline's own named open item (SA 4036-4037: inclusions and history formation "remain to be verified"; SA 5813-5825, 6155-6158, 17229-17233). Checked implications now conditional only on it: kept-form covariance (row 252), (R-inv) and the zero defect budget (row 242), Theorem UR (row 223), (REL') and Lemma 2 (row 234), the typed reduction (row 227, off T0's path). Route search (row 253): the real-first route fails, so the complex route through the background package (OA5)-(OA7) is needed.
