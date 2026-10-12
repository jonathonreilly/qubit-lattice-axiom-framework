# Campaign C4, lane RW, probe W3: is there a ghost-free completion of the anomalous theory?

**Who and when.** Claude Opus 5.5 (same family as the supervisor), 2026-10-11, 17:40Z to 18:20Z. Not refereed. No repository file was edited.

**Where things are.** Scratch folder `scratchpad/C4/W3/`. Scripts are in `scripts/`, each with a matching `.out`:

| Script | What it does |
|---|---|
| `w3_lib.py` | Fourier-symbol builder (W2's conventions), det in ω², and the Krein (mode-energy) classifier |
| `w3_a_anomaly_structure.py` | what the anomaly fixes: the trivializing functional F, L_WZ = I − F, and h-local non-triviality |
| `w3_b_khronometric_class.py` | khronometric (BPS) kinetic structure + anomaly, the m4 repair, mistuning, and a 4-derivative term |
| `w3_c_general_local.py` | general h-local completion (5 masses + 13 two-derivative terms): random search |
| `w3_c2_breaking_size.py` | the same symbol (pickled); how small the spatial-diffeo breaking can be; which terms are needed; c_T |
| `w3_d_ir_criterion_and_window.py` | IR sign criterion; static γ and G_eff of the healthy hits; search with c_T = 1 imposed |
| `w3_e_window_optimizer.py` | local optimizer pushing healthy hits toward GR-like statics (weak; see §4) |

**Labels.**
- **proved:** short algebra, complete in its stated class.
- **checked:** computed here (sympy exact or numerics).
- **suggested:** an argument, not computed.
- **reading:** an interpretation.
- **comparator:** literature via F1/W2, not re-fetched.

**Inputs.**
- W2's WZ term and spectrum (refereed: valid particular solution, not unique).
- F1's khronometric window and GSS formulas (refereed: correct).
- W2/I3's vacuum identity ⟨E_c − H⟩ = −(ρ + p).

**Class studied.** The scalar sector of linearized gravity on flat space in the continuum IR (q̂ not included), M_P² = 1, with:
- rotation invariance and time-translation invariance;
- T-even terms;
- **ADM form:** no time derivatives on the lapse h₀₀ or the shift h₀ᵢ. Otherwise π or ζ acquire Ostrogradsky dofs.

Terms up to two derivatives in h-counting, plus one FDiff-invariant four-derivative potential term. The vector and tensor sectors are **not** analysed, apart from c_T.

---

## 0. Bottom line in plain words

1. **What the anomaly actually fixes (proved, checked).** At quadratic order the C3 anomaly is the gauge variation of one functional:

   F = a[−∇Φ·∇E − ½(∇(B − Ė))²].

   - F is local in the scalar–vector–tensor (SVT) variables but **non-local in h_μν**. No h-local mass term reproduces the anomaly (checked: the linear system has no solution). So the anomaly is non-trivial for local metric counterterms, consistent with C3, and is Polyakov-like.
   - W2's WZ term equals I − F, where I = F[U, V, W] is built from the Stückelberg invariants. Since F vanishes at B = E = 0, **W2's gauge-fixed spectrum is exactly that of the unitary-gauge action L_GR + F** (checked: same root).
   - **Answer to the W2 referee's "not unique" point.** The anomaly fixes the coefficient a of one h-non-local structure. Everything else is an arbitrary h-local term, and that is the class W3 scans.
   - In the referee's SVT-local class (arbitrary functions of U, V, W, Ψ), a could be removed altogether (I belongs to that class). Only h-locality makes a physical.
2. **Pure healthy-Hořava (khronometric) completion + anomaly: no healthy region (proved, checked).**
   - E enters only through −a∇Φ·∇E, so it is a Lagrange multiplier that forces ∇²Φ = 0. **The lapse is frozen (projectable) on every mode, so the BPS α-mechanism is dead.** The spectrum is α-independent at every λ, not only at λ = 1.
   - There is one scalar, with ω² = −(ξk² − g₄k⁴)/K_Ψ and K_Ψ = (3 − 9λ)/2 − (1 − 3λ)²k²/(2[(1 − λ)k² − a]) (exact).
   - For a < 0 and ξ > 0:

     | λ | Behaviour |
     |---|---|
     | λ < 1/3 | tachyon at every k |
     | 1/3 < λ ≤ 1 | ghost at every k |
     | λ > 1 | ghost below k\*, tachyon above, with k\*² = \|a\|/(λ − 1) |

   - An FDiff-invariant (∇²Ψ)² term repairs only the UV.
   - This closes W2's open counter-route N7 inside the khronometric class.
3. **One local term repairs the lapse, but not the IR (proved, checked).**
   - Add the lapse–trace mass term m₄h₀₀h_ii with **m₄ = −a/2 exactly**. E then drops out (it appears only in a total derivative). The mode count equals the khronometric one (TT + 1 scalar) in vacuum and in excited states alike, so W2's count jump disappears in this subclass.
   - The scalar is healthy at **all k iff λ < 1/3** (with 0 < α < 2ξ). That is outside the window: G_cos ∝ 1/(2 + 3γ) < 0 (comparator, GSS via F1).
   - For **λ > 1** (the window side) it is healthy only for **k > k\* = μ√(2/(λ − 1))** (μ² = |a|/2M_P²), and unstable (tachyonic, negative kinetic) below.
   - Any mistuning δ = m₄ + a/2 ≠ 0 refreezes the lapse, giving item 2 again (checked at δ = 1e-6, 1e-3 and 0.1).
   - **Mechanism, in plain words.** The anomaly's shift-mass term −(a/2)(∇σ)² acts like a scale-dependent λ in the shift sector: λ_eff(k) = λ − 2μ²/k² for a < 0. It drags λ_eff below 1, Hořava's unhealthy side, at wavelengths longer than 1/k\*. **So the anomaly's physical sign is incompatible with the healthy λ > 1 region in the IR.** This answers the supervisor's question.
4. **The most general h-local completion: healthy completions exist, but only far from GR (checked by search, not proved).** The class is the khronometric terms + F + 5 local masses + 13 two-derivative terms that break spatial diffeos.
   - **Scalar-healthy at every k:** 14 of 2500 random draws with λ − 1 ∈ (0.001, 0.095) and 0 < α < 2, all with 2 scalar modes, the khronon-like one and the longitudinal E/ζ.
   - **Only when the breaking coefficients are O(0.1–1).** 0 of 10,000 draws over the four decades |c| ∈ [1e-5, 1e-1]. With masses only and no two-derivative breaking: 0 of 3000.
   - **Heuristic necessary condition (13 of 14 hits).** The bare IR conformal-mode signs must be overturned: K₀ = (3 − 9λ)/2 + 12c₄ + 36c₅ > 0 and G₀ = ξ + 12c₀ + 36c₁ + 4c₂ + 12c₃ < 0.
   - **Every hit is grossly non-GR at k ≫ μ:**
     - c_T² ranges from −9.4 to 4.4 (several hits are TT-tachyonic, which the scalar-only test misses);
     - static γ ranges from −3.2 to 2.6;
     - G_eff/G_GR ranges from −1.1 to 13.8, often repulsive.
   - With c_T = 1 imposed: 1 healthy hit in 4000 draws (prefiltered on K₀ > 0, G₀ < 0), with γ = −0.55 and G_eff < 0.
   - A local optimizer toward γ = 1, G_eff = G_GR, c_T = 1 found no healthy, GR-like point. It is a weak tool, though, so this is not evidence of absence.
5. **Tunings to land in the window, counted for the best candidate (item 3, robust branch).**
   - F1's khronometric list (supervisor: on top of P0): c_T at 1e-15; cubic TT isotropy at 1e-15 (suggested in F1); α ≲ 8e-7; 0 < λ − 1 ≲ 0.095.
   - **Plus one new exact operator relation:** the h₀₀h_ii contact term must equal −½ × the local anomaly density 𝒜(x) in every matter state. That is a relation between operators, not one number.
   - **Plus** the vacuum c-number absorbed by a preferred-frame pressure counterterm (W2/I3: at least one CC-level tuning).
   - **Plus** exact FDiff for every other term (F1 case A: spatial-diffeo redundancy and time reparametrization, neither supplied by the axioms).
   - Even then, the band k < k\* is unstable. In the robust branch k\* ~ μ/√(λ − 1) with μ ≲ 1e-32 H₀ (W2's unrefereed estimate), so the band is roughly 30 decades outside the Hubble radius (reading: dynamically irrelevant). In the vacuum branch (c-number not absorbed) k\* is Planckian and the whole zone is unstable: excluded.

**W3 reading against the FIXED line: INCONCLUSIVE, leaning FAIL.** Details in §5:
- PASS is not met: there is no explicit ghost- and tachyon-free region inside the window without tuning beyond P0.
- FAIL is met in the khronometric class (proved), and for every window-side completion of the m₄-repaired class (proved).
- But the general h-local class contains all-k scalar-healthy completions whose health needs no fine relation. They are only observationally excluded, which the FIXED FAIL clause does not name. No in-window healthy point was found, but the search was not exhaustive.

---

## 1. What the anomaly fixes (part A: `w3_a_anomaly_structure.out`)

**Conventions.** These follow W2: δΦ = ε̇, δB = −ε + χ̇, δE = χ, δΨ = 0; δπ = −ε, δζ = −χ; σ = B − Ė.

| Statement | Status |
|---|---|
| δF = δS_anom = a∫[∇B·∇ε − ∇χ·∇Φ], with F = a[−∇Φ·∇E − ½(∇σ)²] | checked (Euler operator) |
| U = Φ + π̇, V = B − π + ζ̇, W = E + ζ are invariant; I ≡ F[U, V, W] is invariant | checked |
| L_WZ(W2) = I − F, up to total derivatives | checked |
| F at B = E = 0 is 0, so W2's gauge-fixed theory equals the invariant theory L_GR + I; in unitary gauge, L_GR + F | checked; det reproduces ω² = ak²/(3a − 2M_P²k²) |
| No combination of the 5 h-local mass terms (h₀₀², h₀ᵢh₀ᵢ, h_ijh_ij, h_ii², h₀₀h_ii) has variation δS_anom | checked (empty solution set) |

**Reading.** F contains ∂ᵢE and ∂ᵢĖ, which are non-local in h_ij (E ∝ ∇⁻⁴∂∂h). It is the anomaly's Polyakov-type effective action. Its coefficient a is the one datum the anomaly fixes. Every h-local term is a free completion coefficient. In particular, the W2 referee's U², W² and (∇V)² are such h-local mass terms (graviton masses in unitary gauge, at P0 level).

## 2. Khronometric class (part B: `w3_b_khronometric_class.out`)

**The action.**

L_KH = ½[K_ijK_ij − λK²] + ξ[(∇Ψ)² − 2∇Φ·∇Ψ] + (η/2)(∇Φ)² − g₄(∇²Ψ)²

with K_ij = −Ψ̇δ_ij − ∂_i∂_jσ, in unitary gauge (σ − π → σ, Φ + π̇ → Φ).

**Checks.**
- At λ = ξ = 1, η = g₄ = 0 it equals W2's L_GR (checked).
- At a = 0 the khronon has ω² = ξ(2ξ − η)(λ − 1)k²/(η(3λ − 1)). At ξ = 1 this equals GSS's c_S² exactly (checked), so η ≡ α.

**Adding F (c₄ = 0).**
- Write B = σ + Ė. E then appears only in −a∇Φ·∇E. Varying E gives a∇²Φ = 0, so Φ ≡ 0 (proved). Numerically |Φ|/|v| = 0 on the mode (checked).
- The exact determinant gives one root, ω² = −2k²(g₄k² − ξ)(a + (λ − 1)k²)/((3a − 2k²)(3λ − 1)), independent of η (checked). This equals −(ξk² − g₄k⁴)/K_Ψ with K_Ψ as in §0 (checked).
- **Sign map (proved from the formula; checked on 25 k values in [1e-3, 1e3] and 9 values of λ):**
  - the gradient term is fixed at +ξk² (Φ frozen), so health would need K_Ψ < 0 (ghost) or give a tachyon;
  - K_Ψ < 0 for all k when 1/3 < λ ≤ 1;
  - K_Ψ > 0 for all k when λ < 1/3;
  - for λ > 1, K_Ψ flips through a pole at k\*.
- With g₄ = 1: healthy only for k² > ξ/g₄ (UV); the IR is unchanged (checked).

**Repair: m₄h₀₀h_ii with m₄ = −a/2.**
- The E row and column vanish identically: −a∇Φ·∇E − aΦ∇²E is a divergence (checked).
- One scalar remains (rows (3) in the `.out`, grid λ ∈ {−1, 0, 0.2, 0.5, 0.9, 1.01, 1.1, 2}, η ∈ {1e-3, 1, 2.5}):

| a = −1 | Result (checked) |
|---|---|
| λ < 1/3, 0 < η < 2 | **healthy at every k** |
| λ < 1/3, η > 2 | UV tachyon |
| 1/3 < λ < 1 | tachyon or ghost everywhere |
| λ > 1, 0 < η < 2 | **healthy for k > k\*** (k\* = 10, 3.16, 1 at λ = 1.01, 1.1, 2: matches √(\|a\|/(λ − 1))), tachyonic below |

**Analytic reason (proved).**
- After integrating out Φ, the Ψ potential is ξk²(1 − 2ξ/η) + 6ξa/η − 9a²/(2ηk²) in L. All three terms are negative for a < 0 and 0 < η < 2ξ, which means positive energy.
- The kinetic coefficient K_Ψ is the same as above. For a < 0 it has no zero; for λ > 1 it has a pole at k\*.
- The shift-sector coefficient is (k²/2)[(1 − λ)k² − a]. This is the λ_eff(k) statement.

**Mistuning δ = m₄ + a/2 at 1e-6, 1e-3 and 0.1:** ghost below about 3, tachyon above, i.e. identical to the unrepaired case (checked). The repair needs the exact relation.

## 3. General h-local completion (parts C, C2, D: `w3_c_general_local.out`, `w3_c2_breaking_size.out`, `w3_d_*.out`)

**Terms added to L_KH + F.**
- **Masses (5):** h₀₀², h₀ᵢh₀ᵢ, h_ijh_ij, h_ii², h₀₀h_ii.
- **Two-derivative terms (13; T-even, no time derivatives on h₀₀ or h₀ᵢ):**
  - c₀–c₃: (∂h_ij)², (∂h_ii)², (∂ᵢh_ij)², ∂∂h·h;
  - c₄, c₅: ḣ_ij², ḣ_ii²;
  - c₆, c₇: (∂h₀ⱼ)², (∂·h₀)²;
  - c₈, c₉: h₀ᵢ∂ⱼḣ_ij, h₀ᵢ∂ᵢḣ_jj;
  - c₁₀, c₁₁: ∂h₀₀·∂h_jj, ∂ᵢh₀₀∂ⱼh_ij;
  - c₁₂: (∂h₀₀)².

  This is the full rotation-invariant two-derivative scalar-sector basis under those restrictions (spans checked in my notes; not every redundancy was removed).
- det M is quadratic in ω²: at most 2 scalar modes.
- Health test: every root real and positive with positive Krein energy, on 19–28 values of k in [1e-4, 1e5], a = −1.

**Searches.** In every run, λ − 1 ∈ (0.001, 0.095) and η ∈ (0, 2) unless stated; masses ∈ ±|a|·[1e-3, 10]. Samples are log-uniform.

| Search | Breaking terms | Healthy at every k |
|---|---|---|
| S1 (λ = 1.05, η = 0.5) | masses only | 0 / 3000 |
| S2 (λ = 1.05) | \|c\| ∈ [1e-3, 1] | 7 / 3000 |
| S3 (λ ∈ (1, 2]) | \|c\| ∈ [1e-3, 1] | 4 / 3000 |
| S4 (λ = 1.05, η = 0.5) | masses = 0, \|c\| ∈ [1e-3, 1] | 17 / 2000 |
| S5 | \|c\| ∈ [0.1, 1] | 14 / 2500 |
| S5 | \|c\| ∈ [1e-2, 1e-1], [1e-3, 1e-2], [1e-4, 1e-3], [1e-5, 1e-4] | 0 / 2500 each |

**Which terms are needed (S6, 14 hits; a hit breaks when the term is zeroed).**
- m₁ (shift mass) in 10 of 14;
- c₅ (ḣ_ii²) in 10;
- c₆ in 9;
- c₀, c₁ and c₇ in 6 each.

**IR criterion (suggested; 13 of 14 hits satisfy it).**
- For k ≪ μ the anomaly's shift mass dominates the shift sector, so the momentum constraint is lost and the IR scalar's signs are the bare two-derivative ones.
- Health then needs K₀ > 0 and G₀ < 0, which takes O(0.1–1) coefficients:
  - 12c₄ + 36c₅ > (9λ − 3)/2 ≈ 3;
  - 12c₀ + 36c₁ + 4c₂ + 12c₃ < −ξ.
- This explains the threshold seen in S5.

**Observables of the hits at k = 100 ≫ μ (D).**
- GR reference (checked): Φk² = −2, γ = 1.
- Hits:
  - c_T² = (1 − 8c₀)/(1 + 8c₄) (checked symbolically) ranges over −9.4 to 4.4;
  - γ ranges over −3.2 to +2.6;
  - G_eff/G_GR ranges over −1.1 to +13.8.
- With c₀ = −c₄ (c_T = 1) imposed: 1 hit in 4000 (γ = −0.55, G_eff/G_GR = −1.44).
- Part E (Nelder–Mead on |γ − 1| + |G − 1| + 10|c_T² − 1| + 50 × unhealthy) ended with every start either unhealthy or with c_T² far from 1. The best healthy end point has γ = 1.02 and G = 1.13 but is TT-tachyonic.

**Reading.**
- Healthy completions with the physical sign exist in the general class. They are LV gravity whose spatial-diffeo invariance is broken at O(10–100%) in the two-derivative sector (F1's case B with kinetic breaking), and they carry an extra propagating longitudinal scalar. Their vector sector is unexamined.
- None found is near GR. Whether a healthy point with c_T = 1, γ = 1 and G_eff = G_GR exists is open. The search was too weak to settle it.

## 4. Comparison with healthy Hořava (BPS)

| Theory | Healthy region | With the anomaly (a < 0) |
|---|---|---|
| BPS / khronometric (comparator; GSS formula checked here) | λ > 1 or λ < 1/3, with 0 < α < 2 | with no repair: none (lapse frozen, item 2). With the m₄ = −a/2 repair: λ < 1/3 at all k; λ > 1 only for k > k\* |
| Projectable Hořava (RN L3, F1) | none (ghost for λ < 1, tachyon for λ > 1) | the anomaly forces projectability, the same pattern (item 2) |
| LV massive gravity (Dubovsky; Rubakov–Tinyakov; comparator) | phases with extra healthy modes need mass relations | the general h-local hits sit here: 2 scalars, O(1) breaking |

**Sign question.** The physical a < 0 shifts the shift-sector λ_eff downward at long wavelengths. So it is incompatible with BPS's λ > 1 branch below k\*, and compatible with the λ < 1/3 branch, which observations exclude.

## 5. Against the FIXED W3 line

| FIXED criterion | Result |
|---|---|
| **PASS:** explicit ghost- and tachyon-free region, inside the window, without tuning beyond P0 | **not met.** The window-side candidate (§2 repair, λ > 1) is unstable for k < k\* and needs F1's khronometric tunings + 1 exact operator relation + vacuum pressure tuning + exact FDiff. The all-k-healthy points (λ < 1/3 in §2; the general-class hits in §3) lie outside the window |
| **FAIL:** every completion in the stated class (quadratic, ≤ 2 derivatives, plus the FDiff 4-derivative term) has a ghost or tachyon, or needs tuning beyond P0 | **met** for the khronometric class (proved) and for the m₄-repaired class on the window side (proved). **Not met** for the general h-local class: all-k scalar-healthy completions exist with natural O(1) breaking coefficients (checked). They are observationally excluded, but the FIXED FAIL clause does not name the window |
| **INCONCLUSIVE:** otherwise | **W3 = INCONCLUSIVE, leaning FAIL** |

**Against the supervisor expectation.**
- "A healthy region exists at λ ≠ 1, as in healthy Hořava": **not confirmed** for the khronometric completion. The anomaly freezes the lapse, so there is no healthy point at any λ.
- After the exact m₄ repair, the expectation is **confirmed only in the UV** (k > k\*) for λ > 1, and at all k only for λ < 1/3.
- "Does the anomaly force a sign incompatible with that region?": **yes, in the IR.** λ_eff(k) = λ − 2μ²/k².
- "PASS-for-health but FAIL-for-tuning": for the best candidate, **health is partial (UV only) and tuning is beyond P0**.

**Plain words.** The anomaly fixes one non-local term. In the healthy-Hořava completion that term pins the lapse, and the scalar goes bad at every λ. One extra contact term, set exactly against the anomaly in every matter state, frees the lapse again. Even then, the anomaly's sign drags the theory to the bad side of Hořava's λ at long wavelengths. In the robust branch those wavelengths are absurdly long, so in practice the theory could be fine. Getting there costs F1's khronometric tunings, an exact operator relation, a vacuum pressure tuning and exact FDiff: more than P0. Fully healthy versions exist only by breaking spatial smoothness at the 10–100% level, and none found looks like GR.

## 6. Scope, hypotheses, strong words, negative-claim record

**Hypotheses (H1–H6).**
- **H1:** quadratic order, flat background, continuum IR symbols (no q̂), M_P² = 1.
- **H2:** scalar sector only. TT is touched only via c_T. Vector modes, released by the breaking terms, are not analysed.
- **H3:** T-even terms; ADM (no ∂_t on lapse or shift).
- **H4:** homogeneous constant a, i.e. W2's mean-field representative of C3's Killing coefficient. The referee's caveat that it is only a Taylor coefficient still applies.
- **H5:** h-locality is the criterion for "allowed completion".
- **H6:** health means real ω² > 0 and positive Krein energy on a k grid of 19–28 points over 6–9 decades.

**Outside realizations not covered.**
- O(k⁴) breaking terms beyond the single FDiff g₄ term. Suggested: they cannot change the IR, which is controlled by the lowest-order terms. Checked for g₄.
- T-odd terms; non-ADM terms (extra dofs).
- Inhomogeneous a(x).
- Nonlinear completions.

**Strong words.**
- **proved:**
  - triviality of the SVT-local anomaly and its h-local non-triviality (within the mass-term basis);
  - Φ ≡ 0 in the khronometric class;
  - the sign map of item 2;
  - E-decoupling at m₄ = −a/2;
  - the λ_eff(k) form.
- **checked:** all the tables (sympy exact or numeric).
- **suggested:**
  - the IR criterion K₀ > 0, G₀ < 0 (13 of 14 hits);
  - IR irrelevance of higher-derivative terms;
  - the super-horizon harmlessness of the k < k\* band.
- **reading:** W2's μ estimate (unrefereed) used for k\*.
- **comparators:** GSS/BPS via F1; Dubovsky and RT; G_cos < 0 for λ < 1/3.

**N1–N8.**
- **N1, routes:**
  1. khronometric: dead (proved);
  2. khronometric + exact m₄ relation: UV-healthy, IR band, extra relation;
  3. λ < 1/3: healthy, excluded;
  4. general local with O(1) breaking: healthy, non-GR;
  5. general local with small breaking: none found;
  6. higher derivatives: UV only.
- **N2:** routes 1–3 are one family (FDiff + anomaly), with 3 a branch of 2. Routes 4 and 5 are one family.
- **N3:** H1–H6 above.
- **N4:** the anomaly structure rests on `w3_a_*.out` (a)–(d); the sign map on `w3_b_*.out` (2)–(4); the search claims on `w3_c2_*.out` S4–S6.
- **N5:** scope is quadratic, scalar sector, two derivatives plus g₄.
- **N6:** the escapes need either an exact operator relation (m₄ = −½𝒜) or O(1) spatial-diffeo breaking. Neither is supplied by the axioms.
- **N7, strongest counterargument:** in the robust branch k\* is about 30 decades super-horizon, so route 2 is observationally healthy. It fails the FIXED PASS only through the literal "ghost- or tachyon-free" wording and the tuning count. A second open item: the general class's small in-window region was not searched effectively (the part E optimizer is weak).
- **N8, prior walls:**
  - W2 (λ = 1 case, now a special point of item 2);
  - F1 case A/B (tunings);
  - RN L3 (projectable scalar: the same pattern, because the anomaly forces projectability).
