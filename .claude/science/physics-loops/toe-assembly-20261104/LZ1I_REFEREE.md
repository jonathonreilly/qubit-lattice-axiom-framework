lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LZ1-i referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3, the referee, under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. This session wrote neither pass 1 (`LZ1I_DRAFT.md`) nor pass 2 (`LZ1I.md`). This is one check: one line-by-line read of `LZ1I.md`, checked against its pass-1 source and the texts it cites. No review of this review was commissioned.

**What this file is.** An author-side referee report for the lead to check and commit. It grants no status. It adopts no law, reading or specification. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. It does not edit `LZ1I.md`. "Referee closure" marks a short complete argument written here; it is unrefereed. "[check]" marks one tiny floating-point computation (§6.F). It guides and never proves.

**Text read.** `LZ1I.md` at commit `bca2aaabd` (the commit that adds it; branch head when read). SHA-256 of the file read: `657677c48fec7c550ba02b7b71cedb6be48abb42837ebd6a4a32e7f6d8d9856b`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local `claude/toe-assembly` (this checkout, HEAD) | `bca2aaabd` |
| `origin/main` (fetched 2026-11-06; read with `git show` only) | `f5af11cd01` |
| `origin/docs/consolidate-lorentz-dispersion` (PR #10125, carries #9913; read with `git show` only) | `586d7c81d0` |

**Files read, by line.** This folder: `prior/LZ1I.md` 1–77 (all); `LZ1I.md` 1–137 (all); `LZ1I_DRAFT.md` 1–327 (all); `LW1_REFEREE.md` 1–92 and its headings (format only); `Y2W_DRAFT.md` 1–40 (format only); `TOE_ASSEMBLY.md` 71–250 and 286–410; `LZ1.md` 1–216 (all); `GA1_5.md` 1–386 (all); `MT1.md` 1–140 and 150–160; `LW1.md` 20–79, 186–215, 318–347, 399–406; `LW1_5.md` 20–109 and 256–300; `ZM1_OBS.md` 40–141 and 163–222, with grep hits in 1–19 and 272–345; `ZM1.md` grep hits at lines 28, 51–59, 91–100, 119, 144. Main: `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md` 48–72; `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md` 43–83; `docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` 20–26; `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` 29–43, 452–458, 468–473, 485–489; `docs/SOFT_SPIN2_COLLISION_INVARIANTS_COMMON_CONES_AND_LATTICE_WARD_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md` 225–229, 245–249, 266–271; `docs/CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_AND_THE_LORENTZIAN_SIGN_AND_HAS_AN_ORDER_A_SQUARED_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-18.md` 14–18; `docs/CROSS_SECTOR_FRONT_SPEED_B4_TWO_SURFACE_ALIGNMENT_BOUNDED_THEOREM_NOTE_2026-07-16.md` 32–37, 77–81, 92–95; `docs/EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md` 60–66. PR #10125: `docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` 9–12, 81–88, 99–113, 130–133, 788–791. The audit ledger was not read; ledger statuses below are the digest's.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and readings are read plainly, as `LZ1I.md` §1 states them. No hostile reading of a premise is used. Where a theorem needs more than a text gives, this report states the missing step and closes it.

**Working set and owner decisions used, by name.** PS-1 read by PS-1c (cell covariance); PS-5 (five modes per site); PS-6 and PS-6r (finite link registers); PS-7 only through the words "half filled"; LZ1-SC (`TOE_ASSEMBLY.md` §3.6, line 229); GA1-P-NN = NN-a (§3.7, line 235); ZM1-I1[a] (§3.8, line 243), only in a downstream remark. Proposed readings used and not adopted: LZ1's D1 states, bands, nodes, light species and D5 symmetries (`LZ1.md` lines 34–38); R-loc (line 40); GA1-P-5 and R-Φ (`GA1_5.md` lines 50 and 59).

**Results used, by name.** Ported with credit, not re-derived: `LZ1.md` Theorem 4.1; `MT1.md` Theorems 1 and 7 and line 93; `LW1.md` A1, A2, B10, E1 and the word argument of lines 198–205; `LW1_5.md` §2 and B1-U; `GA1_5.md` GA1-P-5, Lemma U and Proposition C (Lemma U is rebuilt in §6.B, because `GA1_5.md` line 9 lists it as an unrefereed referee closure); `ZM1_OBS.md` Theorems 7, 9 and 9′, Lemmas S0 and SP (Theorem 9's proof is rebuilt inside RC-Z); `ZM1.md` line 28 (folded fine momenta).

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: Schur's lemma; the character-norm test; Fourier series on `Z³`; the geometric-sum bound `|Σ_{t<T}e^{itx}| ≤ π/|x|` for `0<|x|≤π`; the commutant of the multiplication algebra on `L²(T³;C^d)` (proved in RC-C); the Lie-group word argument of `LW1.md` lines 198–205. No citation is load-bearing.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false or wrong line, quoted, with its fix); INCOMPLETE (a named missing step, with its closure). Proof steps of the longer theorems are separate items.

**Counts.** 76 items: 67 CORRECT, 4 ERROR, 5 INCOMPLETE. No ERROR or INCOMPLETE item changes what Theorems 1–8 assert. Item 28 restores a clause of the gate's definition that the distillation dropped; item 56 corrects the second sentence of Theorem 9. One INCOMPLETE item limits the proof scope of Theorem 10; a referee closure restores it in a stronger form.

---

## 1. The three questions put to this referee

**Q1. Are the two appended link-only layers admissible under NN-a and the GA1-5 compilation?** Yes, once edit E3 restores one clause of the gate definition. The reasons, each checked in §6.B:
- Each gate `G_C` is a unitary on the registers of the 36 links `L′_C` with an end at a corner of `C`. It is link-only and commutes with every local gauge transformation. Gates of one tiling act on disjoint corner ends, conserve end numbers, and so commute. Every lift carries `G_C` to `G_{gC}` (with RC-A). So `L_e` and `L_o` are sublayers of GA1-P-5 (`GA1_5.md` line 50) and layers of LZ1's class (`LZ1.md` line 28).
- `L′_C` is connected. Lemma U (`GA1_5.md` line 234) writes `G_C⊗1` as a finite word of unitaries in the algebras `𝒢_{w,ℓ}=𝒜_w^+⊗B(H_ℓ)`. Each such unitary is an even gate on one edge triple, a nearest-neighbour gate in NN-a's sense (`TOE_ASSEMBLY.md` line 235).
- Split each tiling into the eight classes of cubes with a fixed cube index mod 2. Corners of two cubes of one class lie at sup-distance at least 3. Every compiled factor acts within sup-distance 1 of its own cube's corners. So the `k`-th factors of one class act on pairwise disjoint edge triples and form one NN-a layer. This is Proposition C(i)'s argument (`GA1_5.md` line 264) applied to `G_C`. The depth is independent of volume.
- NN-a requires gauge invariance and cell covariance of the complete update only. Here both hold gate by gate, which is more than NN-a asks. The compiled factors are not gauge invariant; NN-a allows that: "Gauge invariance and cell covariance are required of the complete update only."

**Q2. Are both bands in the physical sector of the stated D1 state, with exact Clifford cones of different speeds?** Yes, for `ω_Σ` (Theorem 7) and for the cell-invariant mixture `ω̄` (Theorem 8, with RC-B). The vectors `u^j_x=π(E^x_{j0})Ω` come from gauge-invariant local operators, so they lie in `H_phys=closure π(𝔄^G)Ω`. The operators are link-only, so the vectors are even. The tick acts on them exactly by the matrix of `W_{θ_j}^*` (§6.C). The band fibre is `V_j(K)=Ψ₀^*V_{θ_j}(−K)^*Ψ₀`, with leading generators `N^{(j)}_i=v_jΨ₀^*G_iΨ₀`, `{G_i,G_k}=2δ_{ik}`, `v_j=sin θ_j/√3`. By B10 the fibre has eigenvalue 1 only at `K=0`, so each image lies in `ker(Ũ−1)^⊥`. The speeds differ exactly when `θ₁≠θ₂`. The conclusion does not depend on how species are counted: the direct sum of the two bands is a band whose leading generators satisfy `{N_i,N_k}=2δ_{ik}(v₁²1₈⊕v₂²1₈)`, which is not one Clifford cone when `v₁≠v₂`. Both bands are neutral. They are not flux-carrying under R-Φ, and nothing identifies them with gauge bosons, fermions or gravitons; `LZ1I.md` says so.

**Q3. Is the distiller's GAP on the relative-budget comparison real?** Only as a wording defect of the draft, not as a missing mathematical step (§4). For the fine list used, the relative and absolute budgets are equivalent up to a constant. The draft's phrase "suppose their branch form meets the same hypotheses" already supplies the coarse weight bound that Theorem 9′ needs. This report finds a different, real gap in the same theorem. Its fine-side check is done for one fine tick and one fine cell per coarse step. It survives several fine ticks per coarse tick, but not a spatial block: a zoom with `L′≥2` fine cells per coarse cell folds the fine momenta, and then Theorem 9's hypotheses fail on the fine side (item 59). Referee closure RC-Z repairs this. The repaired Theorem 10′ also asks less of the coarse side than either alternative of Theorem 10.

---

## 2. Verdict table

| # | Item (`LZ1I.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status summary (5) | CORRECT | Matches Theorems 1–9; "different" needs `θ₁≠θ₂`, which Theorem 8 states. |
| 2 | §0 GAP paragraph (7) | CORRECT | An accurate report of the draft's wording. Verdict on the GAP: §4 (wording only). |
| 3 | §0 open list (9) | CORRECT | Add LZ1-i[ZM1a] (E9). |
| 4 | §0 provenance (11) | CORRECT | Draft hash and all seven prefixes match the files read [shasum]. |
| 5 | §1 update class and "admissible" (15) | ERROR | Cites NN-a as `TOE_ASSEMBLY.md` §3.6; it is §3.7 (line 235). Content correct. E1. |
| 6 | §1 D1, GNS, band, node, cone, species, LZ1-SC (17) | CORRECT | Matches `LZ1.md` lines 34–36 and `TOE_ASSEMBLY.md` line 229. |
| 7 | §1 cell group, ends, D5, R-Φ (19) | CORRECT | Matches `LZ1.md` line 38 and `GA1_5.md` line 59. |
| 8 | §2 sector `Σ` (23) | CORRECT | `(n_F,n_E)` is `(2,0),(4,0),(5,1),(5,3)`. |
| 9 | Theorem 1 statement (25) | CORRECT | Holds for every allowed `(ε,μ,τ_E)`. |
| 10 | Theorem 1 proof (27) | CORRECT | Hop monomial conditions checked (§6.A). |
| 11 | `D_∥`, `W`, `B`, `A_x`, `ev_x` (29) | CORRECT | |
| 12 | Theorem 2 statement (31) | CORRECT | |
| 13 | Theorem 2 proof: link factorization (33) | CORRECT | |
| 14 | Theorem 2 proof: `B` irreducible (33) | CORRECT | Character `(3,1,−1,0,−1)`, norm 1. |
| 15 | Theorem 2 proof: Schur, isometry, `A_x≠0` (33) | CORRECT | [check] `dim A_x` is 105 for `m=2,8` and 1485 for `m=4,6`. |
| 16 | Theorem 2 proof: gauge invariance, multiplicativity, parity (33) | CORRECT | |
| 17 | Theorem 3 statement (35) | CORRECT | |
| 18 | Theorem 3 proof: stabilizer (37) | CORRECT | |
| 19 | Theorem 3 proof: freeness, two orbits (37) | CORRECT | [check] on a `4³` torus. |
| 20 | Theorem 3 proof: six cosets, end numbers differ at every site (37) | CORRECT | |
| 21 | Theorem 3 proof: lift on labels (37) | CORRECT | Reordering signs are constant on fixed sectors. |
| 22 | Frames and `α_g(E^x_{jk})=E^{gx}_{jk}` (39) | CORRECT | One-line verification omitted; it is immediate from Theorem 3. |
| 23 | §3 walk and imports (43) | ERROR | Cites `R_C` to `MT1.md` §2, which does not define it; `LW1.md` lines 64–65 do. E2. |
| 24 | Theorem 4 statement (45) | CORRECT | |
| 25 | Theorem 4 proof (47) | CORRECT | [check] `ρ(r)⁴=−1`; covariance holds for every cube. |
| 26 | `W_θ`, `Ψ₀` (49) | CORRECT | |
| 27 | Definition of `g_C` (49) | CORRECT | The frames of line 39 are implicit; E3 names them. |
| 28 | Definition of `G_C^Σ` (49) | ERROR | Omits the identity on the non-`B` part of the corner stars, so `G_C` is not unitary as written. E3. |
| 29 | Cosets, `G_C`, `L_T`, `U` (51–54) | CORRECT | |
| 30 | Theorem 5 statement (56) | CORRECT | With E3. |
| 31 | Theorem 5 proof: independence of representatives (58) | INCOMPLETE | Needs exact composition of lifts on link operators. RC-A. |
| 32 | Theorem 5 proof: orthogonal projections, unitarity (58) | CORRECT | With E3. |
| 33 | Theorem 5 proof: gauge invariance (58) | CORRECT | |
| 34 | Theorem 5 proof: support and commutation (58) | CORRECT | |
| 35 | Theorem 5 proof: covariance under `𝒢` (58) | CORRECT | With RC-A. |
| 36 | Theorem 5 proof: GA1-P-5 and LZ1 class (58) | CORRECT | |
| 37 | Theorem 5 proof: NN-a compilation (58) | CORRECT | Lemma U rebuilt (§6.B). |
| 38 | Definition of `ω_Σ` (62) | CORRECT | |
| 39 | Theorem 6 statement (64) | CORRECT | |
| 40 | Theorem 6 proof: gauge and translation invariance (66) | CORRECT | |
| 41 | Theorem 6 proof: stationarity (66) | CORRECT | The region contains the corner stars of every appended gate used (§6.C). |
| 42 | Theorem 6 proof: filling (66) | CORRECT | |
| 43 | Theorem 7 statement (68–72) | CORRECT | |
| 44 | Theorem 7 proof: orthonormality, sectors, translation (74) | CORRECT | |
| 45 | Theorem 7 proof: one-excitation evolution (74) | CORRECT | |
| 46 | Theorem 7 proof: isometry and fibre (76) | CORRECT | Fourier convention checked: the fibre is the Bloch fibre of `W_θ^*` at `−K`. |
| 47 | Theorem 7 proof: node and Clifford generators (76) | CORRECT | |
| 48 | Theorem 7 proof: orthogonality to `ker(Ũ−1)` (76) | CORRECT | |
| 49 | Theorem 8 statement (78) | CORRECT | |
| 50 | Theorem 8 proof: D1, cell invariance, filling (80) | CORRECT | Lifts compose up to site-sign automorphisms; each sector state is invariant under them. |
| 51 | Theorem 8 proof: the bands in the mixture (80) | INCOMPLETE | The evolution step needs the tick to fix the other five sector supports. RC-B. |
| 52 | Theorem 8 proof: ratio range (80) | CORRECT | |
| 53 | Theorem 8 proof: no D5 symmetry exchanges the images (80) | INCOMPLETE | Needs "two bands with one image have one speed set". RC-C. |
| 54 | Remark after Theorem 8 (82) | CORRECT | `E^x_{j0}∈𝒩`, so the image is not orthogonal to `π(𝒩)Ω`. |
| 55 | Theorem 9, first sentence (84) | CORRECT | |
| 56 | Theorem 9, second sentence (84) | ERROR | Omits restriction of the base law (odd `m`, or `L5-O`). E6. |
| 57 | Theorem 9 proof (86) | CORRECT | |
| 58 | Theorem 10 statement (88) | CORRECT | As a conditional. Its two alternatives coincide for this fine list (§4). |
| 59 | Theorem 10 proof: fine-side hypotheses (90) | INCOMPLETE | Holds without spatial blocking. A zoom with two or more fine cells per coarse cell folds the fine momenta and breaks Theorem 9's hypotheses. RC-Z, Theorem 10′. |
| 60 | Theorem 10 proof: conclusion (90) | CORRECT | Given all hypotheses, Theorem 9 gives it. |
| 61 | Theorem 11 statement and proof (94–100) | CORRECT | |
| 62 | Theorem 12 statement and proof (102–104) | CORRECT | |
| 63 | A1 (106) | CORRECT | Quotes checked against main and PR #10125. |
| 64 | A3 (108) | CORRECT | Quotes checked. |
| 65 | A4 (110) | CORRECT | Quotes checked. |
| 66 | §6 four tests and table (114–120) | CORRECT | Judgments, recorded as the draft's. |
| 67 | §6 remark on R-Φ checks (122) | CORRECT | Matches `GA1_5.md` line 61. |
| 68 | LZ1-i[O] (126) | CORRECT | |
| 69 | LZ1-i[odd m] (127) | CORRECT | |
| 70 | LZ1-i[cube] (128) | CORRECT | |
| 71 | LZ1-i[VC1] (129) | CORRECT | |
| 72 | LZ1-i[R-CS^str] (130) | CORRECT | |
| 73 | Inherited items, A2, attempt K (131) | CORRECT | `MT1.md` line 157 checked. |
| 74 | Digest summary (133) | CORRECT | |
| 75 | [check] report (135) | CORRECT | The draft's §8 values; this report's own check agrees (§6.F). |
| 76 | Downstream paragraph (137) | INCOMPLETE | Does not say that the owner's ZM1-I1[a] is a different comparison class. E8. |

---

## 3. Details of the non-CORRECT items

### 3.1 ERRORS

**Item 5 (line 15, citation).** The text reads: "implementability under NN-a (`TOE_ASSEMBLY.md` §3.6)". NN-a is in §3.7 (lines 231–237); its text is line 235. Section 3.6 holds R-CS, the first ZM1-I1 decision and LZ1-SC. Fix: E1.

**Item 23 (line 43, citation).** The text reads: "Let `R_C` be the one-flavour free cube generator of `MT1.md` §2". `MT1.md` §2 is "Lifts and exchange algebra". It mentions `R_T(K)` in Theorem 1 but defines no `R_C`. `LW1.md` line 64 defines `R_T`, and line 65 reads: "Let \(R_C\) be the restriction to a cube." The draft cites `LW1_5.md` inferred definition 4 and `MT1.md` line 37. Fix: E2.

**Item 28 (line 49, definition).** The text reads: "Embed it via the `ev_x` at the corners, with identity on the multiplicity and vertical factors; take zero outside the projection `Π_C^Σ` fixing the six end numbers at every corner. Call this embedded partial unitary `G_C^Σ`." On `Ran Π_C^Σ` the in-plane corner ends carry `⊗_{x∈C}W^{⊗4}`. The image of `⊗_x ev_x` is a proper subspace of it: `W^{⊗4}` also holds the trivial, sign and other isotypic parts of `S₄`. The text defines `G_C^Σ` only on that image. Read as written, `G_C^Σ` vanishes on the rest of `Ran Π_C^Σ`. Then `G_C` (line 53) vanishes there too and is not unitary, against Theorem 5. The draft has the missing term (`LZ1I_DRAFT.md` line 141):
\[
G_C^Σ=\Big[(\otimes_x ev_x)(g_C\otimes1)(\otimes_x ev_x)^*+\big(1-(\otimes_x ev_x)(\otimes_x ev_x)^*\big)\Big]\otimes1_{\rm vertical}\ \text{on }\operatorname{Ran}Π_C^Σ,\qquad G_C^Σ=0\ \text{on its complement.}
\]
With it, `G_C^Σ` is unitary on `Ran Π_C^Σ`, since `ev_x` is isometric and `g_C` is unitary. Nothing else changes. The added term is the identity on a gauge-invariant subspace. Theorem 3 makes it covariant under `𝒢_Σ`. It is zero on the support of `ω_Σ`, where every corner's in-plane factor lies in the image of `ev_x`. Fix: E3.

**Item 56 (line 84, logic).** The text reads: "Any true version must exclude these examples by restricting the layers, the state, or the species prescription." A version can also exclude them by restricting the base law: to odd `m`, or to `L5-O[S_+]` alone. Section 7 names both as open (LZ1-i[odd m], LZ1-i[O]). The draft's Corollary 6.1 has the same omission. Fix: E6.

### 3.2 INCOMPLETE

**Item 31 (line 58).** The text reads: "Thus the coset definitions do not depend on representatives." The step needs `α_{g_kh}=α_{g_k}∘α_h` on link operators, for `h∈𝒢_Σ`. B1-U says only: "The lifts may compose only up to site sign automorphisms" (`LW1_5.md` line 274). The draft supplies the step (`LZ1I_DRAFT.md` line 149). Closure: RC-A. The same step serves the covariance under all of `𝒢` (item 35).

**Item 51 (line 80).** The text reads: "In the mixture, `√6 π̄(E^x_{j0})Ω̄` has exactly the inner products and evolution of `u_x^j`". The inner products follow from the annihilation the text states. The evolution also needs `α(E^x_{j0})P^{(l)}_R=0` for the other five sector supports `P^{(l)}_R`. That needs the tick to fix each of them up to a phase. The draft has the step (`LZ1I_DRAFT.md` line 183); the distillation dropped it. Closure: RC-B.

**Item 53 (line 80).** The text reads: "`LZ1.md` Theorem 4.1 already proves D5 symmetries preserve directional and Clifford speeds, giving the last claim." Theorem 4.1 shows that `S` carries band 1 to a band with image `S(H₁)=H₂` and speed `v₁`. Band 2 also has image `H₂`, with speed `v₂`. The missing step: two bands with one image have one speed set. The draft's version ("the Clifford speed is a property of the image", line 189) states it without proof. Closure: RC-C.

**Item 59 (line 90).** The text reads: "They satisfy the fine-side hypotheses." This holds for the fine data at one fine tick, with translations by one fine cell. It still holds with `M` fine ticks per coarse tick and `L′=1`, since the branches are then `±Mw_j(θ)`. A zoom compares one coarse tick with `M` fine ticks and one coarse-cell step with `L′` fine cells. `ZM1_OBS.md` line 90 reads: "In applications use centered local composites, fine time `L t`, and the induced coarse-cell translations." ZM1-I1 requires `L≥2` (`ZM1_OBS.md` line 50; `TOE_ASSEMBLY.md` line 243). With `L′≥2` the fine symbol folds: `ZM1.md` line 28 describes "the direct sum over `m in (Z/LZ)^3` of the fine fibres at the fine momenta". For the list `u^j_s` the folded symbol is computed in RC-Z(b). Its folded branches have phases `±Mw_j((θ+2πn)/L′)`, `n≢0 mod L′`. Theorem 9 requires, within each side, gaps "at least `g|θ|` modulo `2π`" between all branches, and "phases extending continuously to zero with `λ_{i,k}(0)=0`". Both fail on the fine side.
- *Gaps, for every `M`, every `L′≥2` and every angle.* The folded branches for `n=e₁` and `n=e₂` (same sign) have equal phases on the plane `θ₁=θ₂`: the swap of the first two coordinates exchanges `K_{e₁}(θ)` and `K_{e₂}(θ)` there and fixes `χ`, and `w_j` depends on `K` only through `χ`.
- *Limits.* The folded limits are `±Mw_j(2πn/L′)`. B10 gives `0<w_j<π` off `K=0`, so for `M≤2` they are never `0 mod 2π`. For `M≥3` they are nonzero for all but finitely many `θ_j`.

So, as written, Theorem 10 applies to no zoom with `L′≥2`. Closure: RC-Z and Theorem 10′, which hold for every `M,L′≥1`.

**Item 76 (line 137).** The text reads: "A zoom comparison of the form in Theorem 10 transfers the split; it does not establish that such a comparison exists, nor that the constructed state is the VC1 fine vacuum." This is true. It omits one fact the reader needs. The owner chose ZM1-I1[a] (`TOE_ASSEMBLY.md` line 243), a comparison of separated tails of class (a). Theorem 10 concerns band-limited branch data, the class-(c) form of `ZM1_OBS.md` §5.3. `ZM1_OBS.md` line 176 says of class (a): "it does not by itself prove speed transfer." So no result on file says what a class-(a) comparison does to the two speeds. Fix: E8, and the open name LZ1-i[ZM1a].

### 3.3 Notes on CORRECT items that bear on the freeze

- **Theorem 5 imports unrefereed closures.** Lemma U and Proposition C are "Referee closures, unrefereed" in `GA1_5.md` (line 9). The owner's NN-a check also rests on Proposition C (`TOE_ASSEMBLY.md` line 236). This report rebuilt Lemma U and the disjointness step for `G_C` (§6.B) and found both sound.
- **The base tick under NN-a.** `LZ1I.md` does not discuss the base tick's compilation. It is the law's own: each dressed cube gate is a finite word of even edge-triple gates (`ZM1.md` line 100, citing `LW1.md` "Dressed factorization" and `LW1_5.md` §7.1). Nothing is missing for LZ1-i.
- **Theorem 6 (item 41).** Stationarity uses that the region `R` contains the stars of the corners of every appended gate in the backward cone. "Let `R` contain the supports" gives this, because `L′_C` contains all six links at each corner of `C`. Stars that `R` cuts never meet an appended gate's corners.
- **Theorem 8 (item 50).** `𝒢` permutes the six sector states only up to site-sign automorphisms. Each sector state is invariant under them, because its matter part is a product of number eigenstates. So the average is invariant under every lift.
- **Theorem 10 (item 58).** For the fine list `u^j_s`, `‖ξ₀(f)‖=‖f‖`. So the absolute and relative budgets are equivalent up to a constant once the coarse side is summable (§4). The second alternative of Theorem 10 adds nothing here.
- **The species count is robust.** The two bands are separate light species under `LZ1.md` line 36. Their direct sum is also a band with a node, and it has no single Clifford cone when `v₁≠v₂` (§1, Q2).

---

## 4. The distiller's GAP

**G1. "GAP: relative-budget comparison" (line 7).** The distiller writes: "Draft Corollary C3 invokes `ZM1_OBS.md` Theorem 9′ without expressly requiring its common comparable-weight bounds on *both* fine and coarse branches."

**Verdict: real as a wording defect of the draft; not a missing mathematical step.** Three facts settle it.

1. *The draft's wording already imposes the needed bound.* The draft says: "suppose their branch form meets the same hypotheses" (`LZ1I_DRAFT.md` line 191). The hypotheses just checked there are Theorem 9's, which include `‖W_{i,k}‖≥w>0`. Theorem 9′ asks for one `ρ>0` with `wρ≤‖W_{i,k}‖` and `Σ_k‖W_{i,k}‖≤Sρ` on both sides (`ZM1_OBS.md` lines 131–135). Take `ρ≡1`. The lower bounds are Theorem 9's. The upper bound holds by Lemma S0 (`ZM1_OBS.md` line 276), because both sides are summable. So Theorem 9′ applies under the draft's own words.
2. *For this fine list the two budgets are equivalent.* The fine composites are orthonormal translates: `C₀(β,0)=δ_{β0}1₈` for every translation step, so `c₀(θ,0)=1₈` and `‖ξ₀(f)‖=‖f‖`. Hence `N(f)=max_i‖ξ_i(f)‖≥‖f‖`, and the absolute budget implies the relative one with the same constant. Conversely, coarse summability gives `‖ξ₁(f)‖²≤σ₁‖f‖²` with `σ₁=Σ_β‖C₁(β,0)‖` (Theorem 7: `‖c₁(θ,0)‖≤σ₁`). So `N(f)≤max(1,σ₁)^{1/2}‖f‖`, and the relative budget with constant `C` implies the absolute one with constant `C·max(1,σ₁)`. `ZM1_OBS.md` line 218 records the second direction: "a relative bound implies it under bounded `ξ`."
3. *The comparable-weight bound matters only where weights vanish at zero momentum.* Here the fine weights have norm one (norm `L′^{-3}` after folding). Any admissible `ρ` is then bounded below. So Theorem 9′'s condition is equivalent to a positive lower bound on the coarse weights, which is Theorem 9's condition.

So the two alternatives of Theorem 10 coincide for the constructed bands. The distiller's corrected statement is true but redundant.

**Repaired statement.** Theorem 10′ (§5, RC-Z) replaces Theorem 10. It needs one budget (either form), coarse summability and a coarse branch form with limiting phases. It needs no lower bound on coarse weights and no coarse gap condition for the fine-to-coarse transfer. It also covers zooms with `L′≥2` fine cells per coarse cell, to which Theorem 10 as written does not apply (item 59).

---

## 5. Referee closures

Each closure below is written in full here and is unrefereed. Notation is that of `LZ1I.md`.

### RC-A. Lifts compose exactly on link operators (closes item 31)

**Statement.** For `g,h∈𝒢` and every link-only local operator `X`, `α_g(α_h(X))=α_{gh}(X)`.

*Proof.* By B1-U (`LW1_5.md` line 268), `α_g` acts on the link algebra as conjugation by `Γ_g=⊗_ℓΓ(π_{g,ℓ})`. Here `π_{g,ℓ}` sends each rishon mode at the `z`-end of `ℓ` to the same flavour at the `gz`-end of `gℓ`, and `Γ(π)` is its second quantization on `Λ^mC^{10}`. The end-mode bijection of `gh` is `π_{g,hℓ}∘π_{h,ℓ}`: the `z`-end goes to the `hz`-end of `hℓ`, then to the `ghz`-end of `ghℓ`, with the flavour kept. Second quantization is functorial: `Γ(π′∘π)` and `Γ(π′)Γ(π)` both send `e_{i₁}∧⋯∧e_{i_k}` to `e_{π′π(i₁)}∧⋯∧e_{π′π(i_k)}`. So `Γ_{gh}=Γ_gΓ_h` on the link tensor product, and the conjugations compose exactly. B1-U's caveat, "The lifts may compose only up to site sign automorphisms", concerns the matter signs `d_g`. Link-only operators do not see them. □

*Use.* In Theorem 5, `α_{g_kh}(G^Σ_{h^{-1}C₁})=α_{g_k}(α_h(G^Σ_{h^{-1}C₁}))=α_{g_k}(G^Σ_{C₁})` for `h∈𝒢_Σ`, and `α_g(G^{(k)}_C)=α_{gg_k}(G^Σ_{g_k^{-1}C})` for `g∈𝒢`. The rest of the proof is as written.

### RC-B. The two bands in the mixture `ω̄` (closes item 51)

**Statement.** Let `ω_l=ω_Σ∘α_{g_l}^{-1}` (`l=1,…,6`, `g₁=1`) and `ω̄=(1/6)Σ_lω_l`. Let `A` be local, let `V` be the finite product of the gates of `U` met by the backward cone of `A`, and let the finite region `R` contain the supports of those gates. Let `P^{(l)}_R` be the support projection of the density of `ω_l` on `R`.
- (a) `VP^{(l)}_R=c_lP^{(l)}_R` with `|c_l|=1`.
- (b) For `A=E^x_{j0}` and `l≠1`: `E^x_{j0}P^{(l)}_R=0` and `α(E^x_{j0})P^{(l)}_R=0`.
- (c) The vectors `ū^j_x=√6\,π̄(E^x_{j0})Ω̄` satisfy the orthonormality, translation law and tick law of Theorem 7. Hence Theorem 7's band construction gives, in the GNS space of `ω̄`, two bands with the fibres `V₁,V₂`, in `H̄_phys∩H̄_even∩ker(Ũ̄−1)^⊥`.

*Proof.* (a) `α_{g_l}` commutes with the tick automorphism. It maps each gate of `U` to a gate of the same layer: B1-U maps `H_C` to `H_{gC}` and the electric factor of `ℓ` to that of `gℓ` (`LW1_5.md` line 274), and Theorem 5 maps `G_C` to `G_{gC}`. So `α_{g_l}^{-1}(V)` is the ordered product of the gates met by the backward cone of `α_{g_l}^{-1}(A)`. Also `α_{g_l}^{-1}(P^{(l)}_R)` is the support projection of `ω_Σ` on `g_l^{-1}R`. Theorem 6's argument gives `α_{g_l}^{-1}(V)α_{g_l}^{-1}(P^{(l)}_R)=c_lα_{g_l}^{-1}(P^{(l)}_R)`. Apply `α_{g_l}`.
(b) `E^x_{j0}` contains the projection onto `Σ`'s numbers at the six ends at `x` (Theorem 2). `P^{(l)}_R` lies under the projection onto `Σ_l`'s numbers there. By Theorem 3 they differ at some end at `x`. So the two are spectral projections of commuting end numbers for different values, hence orthogonal, and `E^x_{j0}P^{(l)}_R=0`. Then `α(E^x_{j0})P^{(l)}_R=V^*E^x_{j0}VP^{(l)}_R=c_lV^*E^x_{j0}P^{(l)}_R=0`.
(c) For local `Z` supported in `R`, `6ω̄(Z)=Σ_lω_l(Z)`. The density of `ω_l` on `R` is supported in `Ran P^{(l)}_R`, so `ω_l(Z)=0` whenever `ZP^{(l)}_R=0`. By (b), for `l≠1` this holds for `Z=E^x_{0j}E^y_{j′0}` and for `Z=D^*D`, where `D=α(E^x_{j0})−Σ_y(W_{θ_j}^*)_{yx}E^y_{j0}`. So `⟨ū^j_x,ū^{j′}_y⟩=ω_Σ(E^x_{0j}E^y_{j′0})=δ_{jj′}δ_{xy}`, and `‖Ũ̄ū^j_x−Σ_y(W_{θ_j}^*)_{yx}ū^j_y‖²=ω_Σ(D^*D)=0` by Theorem 7. Translations: `α_{τ_β}(E^x_{j0})=E^{x+2β}_{j0}` and `ω̄` is translation invariant. `E^x_{j0}` is gauge invariant and link-only. The rest of Theorem 7's proof uses only these relations and B10. □

### RC-C. The band images lie in different D5 orbits (closes item 53)

**Lemma M (commutant of the multiplications).** Let `X` be bounded on `L²(T³;C^d)` with `XM_β=M_βX` for every `β∈Z³`. Then `X=M_u` for some `u∈L^∞(T³;M_d(C))`.

*Proof.* Let `X_{ab}` be the `(a,b)` component of `X`, an operator on `L²(T³)`. It commutes with multiplication by every trigonometric polynomial `q`. Put `x=X_{ab}1`. Then `X_{ab}q=qx`. For `f∈L²` take trigonometric polynomials `q_n→f` in `L²`. Then `X_{ab}q_n→X_{ab}f` in `L²`, and `q_nx→fx` in `L¹` by Cauchy–Schwarz. So `X_{ab}f=fx` almost everywhere. If `|x|>‖X‖` on a set `E` of positive measure, then `‖X_{ab}1_E‖=‖1_Ex‖>‖X‖‖1_E‖`, which is impossible. So `x∈L^∞` and `X_{ab}=M_x`. □

**Statement.** If `θ₁≠θ₂`, no D5 symmetry `S` satisfies `S(H₁)=H₂`, where `H_j` is the image of band `j` (in the GNS space of `ω_Σ` or of `ω̄`).

*Proof.* Suppose `S(H₁)=H₂`. By `LZ1.md` Theorem 4.1 (line 94), `S∘F₁`, composed with the coordinate change of its proof, is a band `(8,F′,V′)` with image `H₂`. Its fibre is `V′(K)=V₁(Q^{-1}K)` if `S` is unitary and `\overline{V₁(−Q^{-1}K)}` if `S` is antiunitary. Put `X=F₂^*F′`. Both isometries have range `H₂`, so `X` is unitary. Both satisfy `T_βF=FM_β`, so `X` commutes with every `M_β`. By Lemma M, `X=M_u`, and `u(K)` is unitary for almost every `K`. `H₂` reduces `Ũ`, so `Ũ^*F₂=F₂M_{V₂^*}` and `F₂^*Ũ=M_{V₂}F₂^*`. Hence `F₂^*ŨF′` equals both `M_uM_{V′}` and `M_{V₂}M_u`. So `V₂(K)=u(K)V′(K)u(K)^*` for almost every `K`. By continuity `V₂(K)` and `V′(K)` have the same eigenvalues for every `K`. By B10 every eigenvalue of `V_θ(K)` has real part `1−sin²θ(1−χ(K))`. Complex conjugation, `Ψ₀`, `K↦−K` and `K↦Q^{-1}K` keep this real part, since `χ` is even and invariant under signed permutations. So `sin²θ₂(1−χ(K))=sin²θ₁(1−χ(K))` for every `K`. At any `K` with `χ(K)<1` this gives `sin θ₁=sin θ₂`, so `θ₁=θ₂` on `(0,π/2)`. □

### RC-Z. Theorem 9 with far branches, on a cone of directions (closes item 59)

**Setting.** As in `ZM1_OBS.md` line 90 and Theorem 9. For `i∈{0,1}`: a unitary `U_i`; unitary translations `T^{(i)}_β`, `β∈Z³`, commuting with `U_i`; vectors `v_{i,1},…,v_{i,d}` (the same `d` on both sides); `C_i(β,t)_{ab}=⟨v_{i,a},U_i^tT^{(i)}_βv_{i,b}⟩`; `c_i(θ,t)=Σ_βC_i(β,t)e^{−iθ·β}` where the sum converges absolutely; `ξ_i(f)=Σ_{a,β}f_a(β)T^{(i)}_βv_{i,a}`.

**Hypotheses.**
- (Z0) `p>0`, and `σ_i=Σ_β‖C_i(β,0)‖<∞` for `i=0,1`.
- (Z1) For every `t∈N₀` and all `f,g` with Fourier support in `B_{κ₀}`, `⟨ξ_i(f),U_i^tξ_i(g)⟩=(2π)^{-3}∫\hat f^*c_i(θ,t)\hat g\,dθ`, with `c_i(·,t)` continuous on `B_{κ₀}∖{0}`.
- (Z2) For `0<κ≤κ₀`, every `t∈N₀`, and all `f,g` with Fourier support in `B_κ`: `|⟨ξ₀(f),U₀^tξ₀(g)⟩−⟨ξ₁(f),U₁^tξ₁(g)⟩|≤C(κ^p+tκ^{p+1})‖f‖‖g‖`.
- (Z3) A closed set `Γ` of unit directions and `s₁>0` are given. For `θ=sθ̂`, `θ̂∈Γ`, `0<s<s₁`, and every `t`: `c_i(θ,t)=Σ_{k=1}^{n_i}W_{i,k}(θ)e^{−itλ_{i,k}(θ)}`, with `W_{i,k}(θ)≥0`, real continuous phases, and each `λ_{i,k}(sθ̂)` converging mod `2π` as `s→0`, uniformly in `θ̂∈Γ`. A branch is a *zero branch* if its limit is `0 mod 2π` and a *far branch* otherwise.
- (Z4) A branch `(i₀,k₀)` is *selected*: it is a zero branch, `‖W_{i₀,k₀}(θ)‖≥w>0`, and `|λ_{i₀,k₀}(θ)−λ_{i₀,k}(θ)|_{2π}≥g|θ|` for every other zero branch `k` of side `i₀`, for all `θ` in (Z3).

**Conclusion.** Put `S=max_in_iσ_i` and `K₀=8πCS/w²`. There is `s₂>0` such that, for every `θ=sθ̂` with `θ̂∈Γ` and `0<s<s₂`, some zero branch `k′` of side `1−i₀` satisfies `|λ_{1−i₀,k′}(θ)−λ_{i₀,k₀}(θ)|_{2π}≤K₀s^{p+1}`. Hence, on each ray of `Γ` along which `λ_{i₀,k₀}(sθ̂)=vs+o(s)`, some zero branch of side `1−i₀` equals `vs+o(s)` along a sequence `s→0`; if that branch has a directional derivative along the ray, it is `v`.

*Proof.* Step 1 (pointwise bound). Fix `θ₀=sθ̂` as above with `s` small. Lemma SP(4) (`ZM1_OBS.md` line 212) gives smooth normalized profiles concentrated in the `δ`-ball about `θ₀`, with unit vectors `u,u′`, whose forms tend to `⟨u,c_i(θ₀,t)u′⟩` as `δ→0`. Their Fourier support lies in `B_{s+δ}`. By (Z2), `|⟨u,(c₀−c₁)(θ₀,t)u′⟩|≤C((s+δ)^p+t(s+δ)^{p+1})`. Let `δ→0`: `‖c₀(θ₀,t)−c₁(θ₀,t)‖≤C(s^p+ts^{p+1})`.

Step 2 (weights). At `t=0`, `c_i(θ,0)=Σ_kW_{i,k}(θ)` with each `W_{i,k}≥0`. So `‖W_{i,k}(θ)‖≤‖c_i(θ,0)‖≤σ_i` and `Σ_k‖W_{i,k}(θ)‖≤S` (Lemma S0, `ZM1_OBS.md` line 276).

Step 3 (averaging). Put `λ=λ_{i₀,k₀}(θ₀)` and `γ_T(x)=T^{-1}Σ_{t=0}^{T−1}e^{itx}`. For `x≢0`, `|γ_T(x)|≤π/(T|x|_{2π})`, because `|Σ_{t<T}e^{itx}|=|\sin(Tx/2)/\sin(x/2)|` and `|\sin(x/2)|≥|x|/π` for `|x|≤π`. Put `A_i=Σ_kW_{i,k}(θ₀)γ_T(λ−λ_{i,k}(θ₀))`, the average of `e^{itλ}c_i(θ₀,t)` over `0≤t<T`. Step 1 gives `‖A₀−A₁‖≤C(s^p+Ts^{p+1})`.

Step 4 (far branches). Let `δ_F>0` be the least circular distance from `0` of the far limits on both sides. By (Z3) there is `s₃≤s₁` such that, for `s<s₃`, every zero phase lies within `δ_F/4` of `0` and every far phase at least `δ_F/2` from `0`. Then every far phase at `θ₀` lies at least `δ_F/4` from `λ`.

Step 5 (estimate). By Steps 2–4 and (Z4), `‖A_{i₀}‖≥w−S(π/(Tgs)+4π/(Tδ_F))`. Let `δ` be the circular distance from `λ` to the nearest phase of side `1−i₀` at `θ₀`. If `δ>0`, `‖A_{1−i₀}‖≤Sπ/(Tδ)`. Take `η=w/(4C)` and `T=⌈ηs^{−p−1}⌉`, so `CTs^{p+1}≤w/4+Cs^{p+1}`. Then
\[
w−S\Big(\frac{π}{Tgs}+\frac{4π}{Tδ_F}\Big)−\frac{Sπ}{Tδ}\le \frac w4+C(s^p+s^{p+1}).
\]
The terms `Sπ/(Tgs)≤(Sπ/(gη))s^p`, `4πS/(Tδ_F)≤(4πS/(ηδ_F))s^{p+1}` and `C(s^p+s^{p+1})` sum to at most `w/4` for small `s`. Then `Sπ/(Tδ)≥w/2`, so `δ≤2πS/(Tw)≤K₀s^{p+1}`. If `δ=0` the bound holds trivially.

Step 6 (the partner is a zero branch). Choose `s₂≤s₃` with the smallness of Step 5 and `K₀s₂^{p+1}<δ_F/4`. The phase of side `1−i₀` within `δ` of `λ` then lies within `δ_F/2` of `0`. So it is not far; it belongs to a zero branch `k′`.

Step 7 (rays). Fix `θ̂∈Γ` with `λ_{i₀,k₀}(sθ̂)=vs+o(s)`. Step 6 gives an index `k′(s)` for each `s<s₂`. There are finitely many indices, so one `k′` occurs along a sequence `s_n→0`. Lift the zero phases to real numbers near `0`. Then `λ_{1−i₀,k′}(s_nθ̂)=vs_n+o(s_n)`. If the directional derivative of `λ_{1−i₀,k′}` along `θ̂` exists, it is `v`. □

This is the proof of `ZM1_OBS.md` Theorem 9 (line 112) with one more leakage term (Step 4) and with the gap condition imposed only around the selected branch. Theorem 9 is the case in which every branch is a zero branch and every branch is selected.

### Theorem 10′ (zoom transfer; proposed to replace Theorem 10)

**Statement.** Fix `j∈{1,2}` and integers `M,L′≥1`. Take the fine data `U₀=Ũ^M`, `T^{(0)}_β=T_{L′β}` (translation by `L′` fine cells per coarse step) and the list `u^j_s`, `s∈{0,1}³`. Let a coarse system satisfy (Z0), (Z1) and (Z3) on a punctured neighbourhood of zero. Suppose the comparison meets the absolute budget (Z2), or the relative budget `C(κ^p+tκ^{p+1})N(f)N(g)`; for this fine list the two are equivalent (§4). Then there is a closed cone `Γ` of directions with nonempty interior such that, along every ray of `Γ`, the coarse system has zero branches within `K₀|θ|^{p+1}` of `+Mw_j(θ/L′)` and of `−Mw_j(θ/L′)`, where `Mw_j(θ/L′)=(Mv_j/L′)|θ|+O(|θ|³)`. Where their directional derivatives exist, they are `±(M/L′)v_j`. One may take `Γ=S²` unless `M≥3` and `θ_j` lies in a finite set `E_{M,L′}`. Applied to `j=1` and `j=2`, a coarse system that reproduces both bands carries the two coarse speeds `(M/L′)v₁` and `(M/L′)v₂`.

*Proof.* We check (Z0)–(Z4) on the fine side with `i₀=0` and the two branches `n=0` below selected. The coarse side meets (Z0), (Z1), (Z3) by assumption; the budget gives (Z2).

(a) *Summability.* `C₀(β,0)_{ss′}=⟨u^j_s,u^j_{2L′β+s′}⟩=δ_{ss′}δ_{β0}`, so `σ₀=1` and `c₀(θ,0)=1₈`.

(b) *Folding.* `F_j` maps the constant `e_s` to `u^j_s`, intertwines `T_{L′β}` with `M_{e^{iL′K·β}}` and `Ũ^{Mt}` with `M_{V_j^{Mt}}`. So `C₀(β,t)_{ss′}=(2π)^{-3}∫[V_j(K)^{Mt}]_{ss′}e^{iL′K·β}dK`. `V_j^{Mt}` is a trigonometric polynomial; write `[V_j^{Mt}]_{ss′}(K)=Σ_γa_γe^{iγ·K}`. Then `C₀(β,t)_{ss′}=a_{−L′β}`, a finite family in `β`, and `c₀(θ,t)_{ss′}=Σ_βa_{L′β}e^{iθ·β}`. Since `L′^{-3}Σ_{n∈\{0,…,L′−1\}³}e^{2πiγ·n/L′}` is `1` for `γ∈L′Z³` and `0` otherwise,
\[
c₀(θ,t)=L′^{-3}\sum_{n\in\{0,\dots,L′-1\}^3}V_j(K_n(θ))^{Mt},\qquad K_n(θ)=(θ+2πn)/L′ .
\]
This is (Z1) by `ZM1_OBS.md` Theorem 7, and it is continuous in `θ`.

(c) *Branches.* By B10, for `K∉2πZ³`, `V_j(K)` has the two eigenvalues `e^{±iw_j(K)}`, with `cos w_j=1−sin²θ_j(1−χ(K))` and `0<w_j(K)≤2θ_j<π`. Its spectral projections `P_±(K)` are continuous off `2πZ³`. For `0<|θ|<π` no `K_n(θ)` lies in `2πZ³`. So `c₀(θ,t)=Σ_{n,±}L′^{-3}P_±(K_n(θ))e^{±itMw_j(K_n(θ))}`. These are the branches `(n,±)`, with weights of norm `L′^{-3}` and phase limits `∓Mw_j(2πn/L′)`.

(d) *The selected branches.* Take `n=0`. Their weights have norm `w=L′^{-3}`. From `1−cos w_j=sin²θ_j(1−χ)` and `1−χ(K)=(2/3)Σ_isin²(K_i/2)`, `w_j(K)=v_j|K|+O(|K|³)`. So the two phases are `±(Mv_j/L′)|θ|+O(|θ|³)`. They are `2Mw_j(θ/L′)≥(Mv_j/L′)|θ|` apart for small `|θ|`.

(e) *Other zero branches.* A branch with `n≢0` is a zero branch only if `Mw_j(2πn/L′)∈2πZ`. If `M≤2` this never happens, because `0<Mw_j<2π`; then all such branches are far, and `Γ=S²` works. Let `M≥3` and `n≢0`. Then `χ(2πn/L′)<1`, and `θ_j↦w_j(2πn/L′)` is strictly increasing on `(0,π/2)`. So `Mw_j(2πn/L′)=2πk` has at most one solution for each `k∈\{1,…,⌊M/2⌋\}`. Thus `E_{M,L′}` has at most `(L′³−1)⌊M/2⌋` points. For `θ_j∈E_{M,L′}` a folded zero branch has phase `(M/L′)a_n·θ+O(|θ|²)`, `a_n=∇w_j(2πn/L′)`; `w_j` is smooth there because `0<w_j<π`. Its distance to a selected phase is `(M/L′)|θ|\,|a_n·θ̂∓v_j|+O(|θ|²)`. The directions with `a_n·θ̂=±v_j` form at most two circles or points on `S²`. Let `Γ` be the directions at angular distance at least `ε` from all of them, for a small `ε>0`. On `Γ`, by compactness, every selected branch keeps a gap of at least `c_ε|θ|` from every other zero branch for small `|θ|`.

So (Z0)–(Z4) hold, and RC-Z gives the statement. □

*Remarks.* For `M=L′=1`, Theorem 10′ gives Theorem 10's fine-to-coarse conclusion with fewer coarse hypotheses. If a coarse zero branch is also selected in the sense of (Z4), RC-Z with `i₀=1` matches it to a fine zero branch. The cone `Γ` is needed only for the finitely many angles in `E_{M,L′}`; for ZM1's first step `L=2` (so `M=2`) it is never needed. [check] at `M=L′=4`, `θ_j=π/3`, `K=(π,π/2,π/2)`: `4w_j=2π` to machine precision, so `E_{4,4}` is not empty.

---

## 6. Checks behind the verdicts

### 6.A Sections 0–2 (items 1–22)

- *Provenance (item 4).* `shasum -a 256` on this checkout gives `42ee0a77…b73d` for `LZ1I_DRAFT.md` and the prefixes `8a4abb6e628a6148`, `e5e18302fd535f6d`, `c7be0ddbb9766747`, `c53418ca516e84a2`, `8d1e40accea00ef0`, `78280bd620800eac`, `6fda41c203ac95b5` for the seven files `LZ1I.md` line 11 lists. All match. The `TOE_ASSEMBLY.md` read by the distiller therefore already held §3.8 (ZM1-I1[a]); the draft read an earlier revision (`4e574516aa`).
- *Theorem 1 (items 9–10).* For `ℓ=(x,y)`, the term `c^†_{y,j}r^y_jr^{x†}_kc_{x,k}` is nonzero on an occupation vector only if `x` holds flavour `k`, `y` lacks flavour `j`, the `y`-end holds rishon `j`, and the `x`-end lacks rishon `k`. Its adjoint needs the mirror conditions. Full–full links fail at the target, empty–empty links at the source. On a vertical link the move out of the E-site fails at once. The move into it needs a rishon at the E-end (`n_E≥1`) and a hole at the F-end (`n_F≤4`); `n_E=0` for `m≤4` and `n_F=5` for `m≥6`. On `Σ` the vertical source end carries `n_F` or `n_E`, and `(n_F−m/2)²=(n_E−m/2)²`. None of this depends on `ε,μ,τ_E`.
- *Theorem 2 (items 11–16).* On a fixed `(p,q)` sector the basis map `e_A∧e_B↦e_A⊗e_B` (source modes first) is unitary. An end-number-conserving operator at one end is a sum of products of that end's bilinears. An even bilinear commutes with the other end's creators, so it acts as `X⊗1` (or `1⊗Y`). The character of `B` is `fix(σ)−1`: values `3,1,−1,0,−1` on classes of sizes `1,6,3,8,6`; `(9+6+3+0+6)/24=1`. Schur's lemma makes `f^*f′` scalar. The vectors `w_d` (with `w₁` in slot `d`, `w₀` elsewhere) are orthonormal, and `f₀(b)=Σ_db(d)w_d` is equivariant and injective. The gauge group at `x` acts on `W^{⊗4}` as `Λ^{m/2}(u)^{⊗4}`, which commutes with slot permutations. It therefore acts on `B⊗A_x` as `1⊗(Γ_u∘·)` and preserves the image of `ev_x` and its complement. Gauge transformations at other sites act on other end factors.
- *Theorem 3 (items 17–21).* `Qe₃=±e_i`, `i≠3`, turns vertical ends (numbers `n_F,n_E`) into in-plane ends (number `m/2`); these differ for each even `m`. `Qe₃=−e₃` sends `x₃` to `1−x₃+2β₃` and swaps full and empty planes. The residues `r^k(0)` are `(0,0,0),(1,0,0),(1,1,0),(0,1,0)`, and `r^k(e₃)` the same with third coordinate 1. So the action is free, with the F-sites and the E-sites as orbits. Two sectors with different axes differ at the end along either axis; two with one axis and opposite parity differ at the vertical ends, `n_F≠n_E`. On the label factors B1-U acts as the slot permutation `P_Q` after the identification `J`, times a reordering sign that is constant on each fixed sector. Equivariance gives `P_Qev_x(b⊗f)=ev_x(Λ(Q)b⊗f)`.

### 6.B Section 3 (items 23–37): the walk, the gates and NN-a

- *Theorem 4 (items 24–25).* The sign lift `ρ(Q)` commutes with `R_e,R_o` (`LW1.md` A2: "The signed permutation `D_dP_Q` consequently fixes both `R_e,R_o`"). It is monomial and `R_T` is block diagonal over the cubes of `T`, so `ρ(g)R_Cρ(g)^{-1}=R_{gC}`. `ρ(r)⁴` is a sign lift of the identity; by uniqueness up to a constant phase it is `±1`. The rephased `ρ̃=λ^{-1/4}ρ(r)` has `ρ̃⁴=1` and `ρ̃τ_βρ̃^{-1}=τ_{rβ}`, so `ρ′(β,r^k)=τ_βρ̃^k` is a representation. On one orbit, `ψ(gx_a)=c_g(x_a)` is well defined by freeness, and the cocycle law `c_{hg}(x_a)=c_h(gx_a)c_g(x_a)` gives `Ψπ(h)=ρ′(h)Ψ`. Conjugating gives `π(g)ĥ_Cπ(g)^{-1}=ĥ_{gC}`. [check] on a `4³` torus: `ρ(r)⁴=−1` (as `MT1.md` line 93 states), `Ψπ(g)=ρ′(g)Ψ` for sample `g`, and `π(r)ĥ_Cπ(r)^{-1}=ĥ_{rC}` for all 16 cubes.
- *The gate (items 26–29).* With E3, `G_C^Σ` is unitary on `Ran Π_C^Σ`. The six projections `Π^{(k)}_C` are mutually orthogonal, because two sectors differ at some end at each corner. So `G_C=Σ_kG^{(k)}_C+(1−Σ_kΠ^{(k)}_C)` is unitary on `⊗_{ℓ∈L′_C}H_ℓ`.
- *Covariance (items 31, 35).* For `h∈𝒢_Σ`: `α_h` maps `Π_C^Σ` to `Π_{hC}^Σ`; maps the `ev`-images at the corners of `C` to those of `hC`, acting on `B` factors by `Λ(Q_h)` (Theorem 3); maps the frames `|j⟩_x` to `|j⟩_{hx}` (line 39); and `π(h)ĥ_Cπ(h)^{-1}=ĥ_{hC}` (Theorem 4). So `α_h(G_C^Σ)=G_{hC}^Σ`. With RC-A the coset definitions are independent of representatives and `α_g(G_C)=G_{gC}` for all `g∈𝒢`. `𝒢` preserves each tiling (`LW1.md` A2, line 211), so `s_T` is preserved.
- *Gauge invariance and commutation (items 33–34).* `G_C` is block diagonal in the end numbers at the corners of `C`. In each block it acts on the corner-end factors only. At a corner, a gauge transformation preserves the `ev`-image and its complement, and acts on the image as `1⊗(Γ_u∘·)`, which commutes with `g_C⊗1`. At a non-corner site it acts on far-end factors only. Two cubes of one tiling have disjoint corners. On a link they share, each gate acts on its own end factor inside each link sector `(p,m−p)`, so the two commute.
- *GA1-P-5 and LZ1's class (item 36).* Supports `L′_C` are finite. The family `{L′_C:C∈𝒯_T}` is `𝒢`-invariant and locally finite: a link lies in `L′_C` for at most two cubes of `T`. `L′_C` determines `C`, since it contains the twelve edges of `C` and no edge of another cube of `T`. Gates are link-only, gauge invariant, pairwise commuting, and covariant. These are the conditions of `GA1_5.md` line 50 and `LZ1.md` line 28.
- *Lemma U, rebuilt (item 37).* `𝒢_{w,ℓ}=𝒜_w^+⊗B(H_ℓ)` with `𝒜_w^+≅M_{16}⊕M_{16}`, and `dim H_ℓ=C(10,m)≥45`. Let `𝔤` be the real Lie algebra generated by the skew-Hermitian parts of the `𝒢_{w,ℓ}`, `ℓ∈L′`, `w∈ℓ` shared with another link of `L′`. Step 1: for links `ℓ≠ℓ′` at `w`, `[iA⊗T,iB⊗T′]=i(A⊗B)⊗(i[T,T′])`, and the `i[T,T′]` span the Hermitian elements traceless on each block. Step 2: with `K₀=diag(1,−1,0,…)⊕diag(1,−1,0,…)`, `K₀²=(1/8)1+R` with `R` traceless on each block; then `[i(A⊗B⊗K₀),i(A′⊗K₀)]=−[A,A′]⊗B⊗K₀²`, and Step 1 removes the `R` part. So `i(C⊗B)⊗1∈𝔤` for traceless `C`, and, with the roles exchanged and `i1∈𝔤`, `𝔲(H_ℓ⊗H_{ℓ′})⊗1⊆𝔤`. Step 3: induction over connected subsets, by the two commutator identities of `GA1_5.md` line 250, gives `𝔲(⊗_{ℓ∈L′}H_ℓ)⊗1⊆𝔤`. Step 4: the group of finite products of unitaries of the `𝒢_{w,ℓ}` equals the analytic subgroup with Lie algebra `𝔤`, by `LW1.md` lines 198–205 (words in one-parameter groups; inverse function theorem; an open subgroup of a connected group is the group). Every unitary on `⊗_{ℓ∈L′}H_ℓ` is the exponential of an element of `𝔲(⊗H_ℓ)`. I found no gap. The toy check reported at `GA1_5.md` line 256 agrees; it was not rerun here.
- *Applying Lemma U to `G_C` (item 37).* `L′_C` is connected: each link has an end at a corner, and the twelve edges of `C` join the corners. A site outside `C` is adjacent to at most one corner, so the shared sites are the corners. Each compiled factor lies in some `𝒢_{w,ℓ}` with `ℓ∈L′_C`. It is an even unitary on the edge triple of `ℓ`, and it commutes with `P_xP_y` as NN-a requires. All such triples lie within sup-distance 1 of the corners of `C`. Corners of two cubes of one class (same tiling, same cube index mod 2) lie at sup-distance at least 3 (`|2(b_i−b′_i)+(r_i−r′_i)|≥4−1`). So their compiled factors act on disjoint edge triples. With translated words, the `k`-th factors of one class form one locally finite NN-a layer. The gates of `L_T` commute, so `L_T` is the product of its eight class products. NN-a's remaining clauses hold for the complete update: its automorphism fixes every local gauge generator (each gate commutes with them, `LW1.md` E1) and commutes with every cell lift (Theorem 5 and B1-U).

### 6.C Section 4 (items 38–57): the state and the bands

- *`ω_Σ` (items 38–42).* The star densities are product-consistent because fixed end numbers factorize each link. The matter factor is a number eigenstate, so it is invariant under `U(5)_x` (full: phase `det u`) and under site-sign automorphisms. For stationarity take `R` containing the supports of the gates in the backward cone. These supports contain the full stars of the corners of every appended gate used. On `Ran P_R` those corners carry `|0⟩` in their `B` factor, so `g_C|vac_C⟩=|vac_C⟩` makes `G_C` the identity there; the other five `Π^{(k)}_C` vanish there. Matter gates are the identity by Theorem 1, and `W_E` is a scalar. So `VP_R=cP_R`, hence `Vρ_RV^*=ρ_R`.
- *One excitation (items 43–45).* `E^x_{j0}P_R` maps into the span `𝒦^j_R` of vectors with one corner label `|j⟩_y` and all else as in `Ran P_R`. `𝒦^j_R⊆Ran P^Σ_R`, so matter gates are the identity on it and `W_E` gives the same scalar `c`. A gate `G_C` with no excited corner is the identity. A gate with `y∈C` acts on `|j;y⟩` by `exp(is_Tθ_jĥ_C)` and leaves the multiplicity factors alone. Cubes of one tiling have disjoint corners, so `L_T` acts as `exp(is_Tθ_jĥ_T)`. So `U` acts on `𝒦^j_R` as `c\,e^{iθ_jĥ_o}e^{−iθ_jĥ_e}=cW_{θ_j}`, and `α(E^x_{j0})P_R=Σ_y(W^*_{θ_j})_{yx}E^y_{j0}P_R`.
- *Fibre (item 46).* With `f_s(K)=Σ_bf̂_s(b)e^{iK·b}` and `X|K,r⟩=Σ_{r′}X(K)_{r′r}|K,r′⟩`, translation invariance gives the coefficient map of `Ũ` as convolution with `(W^*)_{2c+s′,s}`. Its symbol is `Σ_c(W^*)_{2c+s′,s}e^{iK·c}`, the Bloch fibre of `W^*` at `−K`. So `V_j(K)=Ψ₀^*V_{θ_j}(−K)^*Ψ₀`, as stated.
- *Node (item 47).* `MT1.md` Theorem 7 (line 103): `V(K)=exp(−ih(K))`, `h(K)=vΣ_jK_jG_j+O(|K|²)`, `v=sin ε/√3`; its proof checks `i\,dV(0)=vΣK_jUΓ_jU^*`. Then `i log V_j(K)=−Ψ₀^*h(−K)Ψ₀=v_jΣ_iK_iΨ₀^*G_iΨ₀+O(|K|²)`.
- *`ker(Ũ−1)^⊥` (item 48).* `ŨF_j=F_jM_{V_j}` and `Ũ^*F_j=F_jM_{V_j^*}`, so `H_j` reduces `Ũ`. A fixed vector's component in `H_j` is `F_jf` with `V_jf=f` a.e. B10 (`LW1.md` line 343) gives every eigenvalue of `V_θ(K)` the real part `1−sin²θ(1−χ(K))`, so eigenvalue 1 needs `χ(K)=1`, i.e. `K=0` on `T³`.
- *Theorem 9 (items 55–57).* Theorems 7–8 give two light species with unequal Clifford speeds in one law and either state. The first sentence follows. The second needs E6.

### 6.D Theorem 10 (items 58–60)

See §4 and RC-Z. The `M=L′=1` check in the proof is right: `C(β,0)=δ_{β0}1₈`; the phases `±w_j(K)` are continuous with limit `0`; the weights are the spectral projections, of norm 1, each of rank 4 (B10 multiplicities); the gap `2w_j(K)` exceeds `v_j|K|` near zero. The folding at `L′≥2` is the new point.

### 6.E Sections 5–7 (items 61–76)

- *Theorem 11.* `Δ′=a(v_B−v_F)−b(v_F−v_B)=−(a+b)Δ`; `Δ(ℓ)e^{∫₀^ℓ(a+b)}` has zero derivative. A nonnegative integrand has a finite or infinite integral; the limit of `Δ` is zero exactly when `Δ(0)=0` or the integral is infinite.
- *Theorem 12.* `∫₀^ℓλκ₀/(1+Wκ₀s)ds=(λ/W)log(1+Wκ₀ℓ)`. With `t=a_lat|k|`, `t^{−p}(1+Wκ₀log(1/t))^{−λ/W}→∞`.
- *Quotes in A1, A3, A4 (items 63–65).* Each quotation the draft makes from the cited notes matches the cited text: B4 note lines 61–68 ("species differences also vanish at the marginal operator level"); exchange-matrix line 76 ("IR-attractive for every positive pair `a,b`"); attractor line 24; spatial-lattice lines 31, 41–43, 455, 471–472, 487–488; soft spin-2 lines 227, 247, 267–270; curvature line 16; cross-sector lines 79 and 94; power-mixing line 65; consolidation lines 11, 83, 87, 101–102, 112, 132, 790. Two of the draft's line numbers are slightly off: the exchange-matrix hypothesis "3. each sector is dragged toward the other with positive coefficients `a,b > 0`" is line 51, not 52, and the cross-sector sentence "the time-fixing symmetry alone does not force equality of these marginal ratios" spans lines 36–37, not 34–36. `LZ1I.md` cites no line numbers there, so it needs no edit. Its paraphrases are accurate. These notes are context, not proof steps.
- *§7 (items 68–75).* `MT1.md` line 157: "fails at the claimed small parameter because the free link replacement is auxiliary". `LZ1.md` line 159 records attempt K as "a failed search, not a no-go". The open names match the draft's FINISH.

### 6.F The [check]

`/tmp/toe-lz1iref/check_lz1iref.py`, run with `python3 -I` after `memory_pressure` showed 52% free; 0.49 s, 56 MB resident; output `/tmp/toe-lz1iref/out.txt`. On a `4³` torus with `LW1`/`MT1` sign conventions it reports: `R_e²=R_o²=1`; a sign lift of `r` that commutes with both generators; `ρ(r)⁴=−1`; a free `𝒢_Σ` action covering all sites; `Ψπ(g)=ρ′(g)Ψ`; `π(r)ĥ_Cπ(r)^{-1}=ĥ_{rC}` for all cubes; eigenvalues of `W_θ` matching B10 to `5×10^{-15}` at `θ=0.4, 1.1`; folded limits `Mw(2πn/L′)` bounded away from `0 mod 2π` on a 400-point angle grid for `M=L′=2`; `4w=2π` at `θ=π/3`, `K=(π,π/2,π/2)`; and `dim A_x=105, 1485` for `dim W=5, 10`. It guides items 15, 19, 25 and RC-Z. It proves nothing.

---

## 7. Required edits

Each edit names the item it fixes. Quoted text is the replacement.

- **E1 (item 5, line 15).** Replace "(`TOE_ASSEMBLY.md` §3.6)" by "(`TOE_ASSEMBLY.md` §3.7, line 235)".
- **E2 (item 23, line 43).** Replace "Let `R_C` be the one-flavour free cube generator of `MT1.md` §2" by "Let `R_C` be the one-flavour free cube generator, the restriction of `R_T` to the cube `C` (`LW1.md` lines 59–65)".
- **E3 (items 27–28, line 49).** Replace "Embed it via the `ev_x` at the corners, with identity on the multiplicity and vertical factors; take zero outside the projection `Π_C^Σ` fixing the six end numbers at every corner. Call this embedded partial unitary `G_C^Σ`." by: "The all-`0` vector and the one-`j` subspaces are taken in the frames `|j⟩_x` of §2, and `ĥ_C` acts on the corner index. Let `Π_C^Σ` fix the six end numbers at every corner. On `Ran Π_C^Σ` put `G_C^Σ=[(⊗_xev_x)(g_C⊗1)(⊗_xev_x)^*+1−(⊗_xev_x)(⊗_xev_x)^*]⊗1_vertical`, with `1` on the multiplicity factors; on its complement put `G_C^Σ=0`. Then `G_C^Σ` is unitary on `Ran Π_C^Σ`."
- **E4 (item 31, line 58).** After "Thus the coset definitions do not depend on representatives." insert: "This uses `α_{gh}=α_g∘α_h` on link operators: B1-U's link part is the second quantization of an end-mode bijection, second quantization is a homomorphism, and B1-U's site-sign freedom acts on matter only (referee closure RC-A, `LZ1I_REFEREE.md`)."
- **E5 (items 51 and 53, line 80).** Replace "In the mixture, `√6 π̄(E^x_{j0})Ω̄` has exactly the inner products and evolution of `u^j_x`; apply Theorem 7." by RC-B's statement and proof. Replace the sentence citing `LZ1.md` Theorem 4.1 by RC-C's statement and proof, with Lemma M. Mark both "(referee closure, `LZ1I_REFEREE.md`)".
- **E6 (item 56, line 84).** Replace "by restricting the layers, the state, or the species prescription" by "by restricting the base law (the register parameter `m`, or the choice of `L5-U`), the appended layers, the state, or the species prescription".
- **E7 (items 2 and 58–60, lines 7 and 88–90).** Replace Theorem 10 and its proof by Theorem 10′ and RC-Z, marked as referee closures. Replace the §0 GAP paragraph by: "The pass-2 GAP on the relative budget is resolved. For these composites the relative and absolute budgets are equivalent, and Theorem 10′ needs no comparable-weight condition (`LZ1I_REFEREE.md` §4). Theorem 10′ also covers zooms, which fold the fine momenta."
- **E8 (item 76, line 137).** After the last sentence add: "The owner's ZM1-I1[a] (`TOE_ASSEMBLY.md` §3.8) is a class-(a) comparison of separated tails. Theorem 10′ concerns band-limited branch data. `ZM1_OBS.md` line 176 says class (a) 'does not by itself prove speed transfer'. So this file does not say what a class-(a) comparison does to the two speeds (LZ1-i[ZM1a])."
- **E9 (item 3, line 9, and §7).** Add LZ1-i[ZM1a] to the open lists. In §0, list RC-A, RC-B, RC-C, RC-Z and Theorem 10′ as imported referee closures, unrefereed.

## 8. Open statements to carry, by name

- **LZ1-i[O]** (`LZ1I.md` line 126): the question on `L5-O[S_+]`, where the Majorana hop does not keep matter number.
- **LZ1-i[odd m]** (line 127): the construction needs `m/2` rishons on every in-plane end.
- **LZ1-i[cube]** (line 128): the base tick with at most GA1-P-5's tiling-cube layer.
- **LZ1-i[VC1]** (line 129): the VC1 vacuum, once VC1 builds it.
- **LZ1-i[R-CS^str]** (line 130): the charged fermion clause.
- **Inherited** (line 131): the rate and one-loop coefficient clauses of LZ1(a); ZM1-i; MT1-S[R-CS]; R-CS; GA1-P-5 as law data.
- **LZ1-i[ZM1a]** (new, from item 76): whether a comparison of class (a) (`ZM1_OBS.md` §5.1), the class the owner chose for ZM1-I1, keeps both speeds when applied to `ω_Σ` or `ω̄`. This report names it and runs no attack on it.

## 9. Freeze recommendation

**Freeze `LZ1I.md` after edits E1–E9.**
- The counterexample is sound on its stated readings. The appended layers are admissible under NN-a, through GA1-5's compilation. Both bands lie in `H_phys∩H_even∩ker(Ũ−1)^⊥` of D1 states, `ω_Σ` and the cell-invariant, half-filled `ω̄`. Their Clifford speeds are `sin θ₁/√3` and `sin θ₂/√3`.
- E3, E4 and E5 restore steps that the draft had and the distillation dropped (RC-A and RC-B), or close a step both left unproved (RC-C).
- E7 replaces Theorem 10 by Theorem 10′. Theorem 10′ is stronger: it covers zooms and asks less of the coarse side.
- E1, E2, E6, E8 and E9 are text fixes.
- No edit changes what Theorems 1–8, 11 or 12 assert. E6 corrects the second sentence of Theorem 9; its first sentence, the counterexample's conclusion, stands.
- RC-Z and Theorem 10′ are new mathematics, unrefereed, like every referee closure in this folder.

---

## Prior work used

Each item is ported with its path. "Extended" means this report proves more than the source, from the source.

- `LZ1.md` §1 (lines 28–40): the update class, D1 states, bands, nodes, light species, D5 symmetries, R-loc. Used throughout.
- `LZ1.md` Theorem 4.1 (line 94). Used in RC-C. **Extended:** RC-C adds that two bands with one image have unitarily equivalent fibres (Lemma M).
- `GA1_5.md` §1: GA1-P-5 (line 50), R-Φ (line 59), its four tests (line 61). Used in Q1 and items 54, 67.
- `GA1_5.md` Lemma U (line 234) and Proposition C (line 262). Used for Q1; Lemma U rebuilt in §6.B; Proposition C(i)'s disjointness argument applied to `G_C`.
- `MT1.md` Theorem 1 (line 58), Theorem 7 (line 103), line 93, line 157. Used in §6.B, §6.C, §6.E.
- `LW1.md` §1 (lines 59–72), A1 (line 186), A2 (lines 209–215), B10 (lines 322–347), E1 (line 401), and the word argument of lines 198–205. Used in §6.
- `LW1_5.md` §2 (lines 81–104) and B1-U (lines 266–274). Used throughout. **Extended:** RC-A records that the lifts compose exactly on link operators.
- `ZM1_OBS.md` Theorem 7 (line 92), Theorem 9 (line 106) with its proof (line 112), Theorem 9′ (line 131), Lemma S0 (line 276), Lemma SP (line 208), and lines 50, 90, 176, 218. Used in §4 and RC-Z. **Extended:** RC-Z extends Theorem 9 to far branches, to a gap condition around the selected branch only, and to cones of directions.
- `ZM1.md` line 28 (folded fine momenta at block factor `L`) and line 100 (edge factorization of the base tick). Used in item 59 and §3.3.
- `TOE_ASSEMBLY.md` §3.6 (line 229), §3.7 (lines 231–237), §3.8 (line 243). Used for the readings and the downstream note.
- `prior/LZ1I.md`, the digest, read in full. Its main-branch and PR #10125 entries were used only to check `LZ1I.md`'s quotations (§6.E).

**Prior work the digest missed.**
- `GA1_5.md` Lemma U, Proposition C and Theorem 6.3. The draft already added them (`LZ1I_DRAFT.md` line 69).
- `ZM1.md` lines 28 and 144 (the folded fine momenta of a block map). Neither the digest nor the draft names them. They decide item 59.
- `ZM1_OBS.md` line 218 ("a relative bound implies it under bounded `ξ`"). It settles the distiller's GAP.
- `ZM1_OBS.md` line 176 (class (a) "does not by itself prove speed transfer"). It bears on the downstream note and on LZ1-i[ZM1a].

---

## FINISH

**Proved** (here; referee closures, unrefereed).
- The answers to Q1–Q3 (§1).
- RC-A (exact composition of lifts on link operators), RC-B (the two bands in `ω̄`), RC-C with Lemma M (no D5 symmetry exchanges the band images when `θ₁≠θ₂`), RC-Z (Theorem 9 with far branches, on a cone), Theorem 10′ (zoom transfer at all block factors `M,L′≥1`, with `Γ=S²` unless `M≥3` and `θ_j` is one of finitely many angles), and the budget equivalence of §4.
- Checked line by line, with E1–E9: Theorems 1–9, 11 and 12 of `LZ1I.md`.

**Counterexamples.**
- `LZ1I.md`'s counterexample stands. On `L5-U[m]`, `m∈{2,4,6,8}`, under NN-a, GA1-P-5, LZ1's D1 and band readings and LZ1-SC, the update `L_oL_eU₀` with the state `ω_Σ` or `ω̄` has two propagating light species in `H_phys∩H_even∩ker(Ũ−1)^⊥`. Their Clifford speeds are `sin θ₁/√3≠sin θ₂/√3` when `θ₁≠θ₂`. So the unrestricted all-species common-speed assertion is false in that reading.
- The fine-side claim in Theorem 10's proof fails for every zoom with `L′≥2`: folded branches meet on planes, and for `M≤2` their phases do not tend to zero. This does not refute Theorem 10's conclusion; Theorem 10′ proves it.

**Open by name.** LZ1-i[O]; LZ1-i[odd m]; LZ1-i[cube]; LZ1-i[VC1]; LZ1-i[R-CS^str]; LZ1-i[ZM1a] (new); inherited: the rate and one-loop coefficient clauses of LZ1(a), ZM1-i, MT1-S[R-CS], R-CS, GA1-P-5 as law data.

**What changes downstream.**
- Under the stated readings, LZ1(a)'s common-speed clause is false for any law with these appended layers, so it cannot be proved for the class as it stands (Theorem 9). Each part that uses that clause (GA2, GR1, GR2) must name its restriction: of the base law, the appended layers, the state, or the species prescription.
- ZM1 and ZM1-OBS: by Theorem 10′, a band-limited comparison of the constructed bands keeps both speeds at every block factor, scaled by `M/L′`. Nothing on file says what the owner's class (a) does to them (LZ1-i[ZM1a]).
- GA1-P-5: an appended class that admits link-only multiplicity walks admits independent light cones. Restricting the class is the owner's question; `LZ1I.md` §6 four-tests three candidates, and none is adopted.
- ST1's signature clause and MT1-S are unaffected. GR2's "two tensor polarisations at speed `c`" still needs a `c` fixed by a mechanism that reaches every light sector.
- This report proposes no new reading or specification. Nothing needs an owner decision beyond the candidates already on file.
