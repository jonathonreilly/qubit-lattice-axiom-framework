# IN1, pass 1: the closed induction, the order of constants, the flow, first passage, and the C3 mass bound

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, pass 1 (long draft) of submanuscript IN1 of `library/ym4-assembly.md`. Research text. It is not an audit and grants no status. Nothing here is checked by the other model. A later pass (Codex) distils it; a fresh session then reads it line by line.

Credit. The architecture of the induction, the class of presentations, the frame device, the cycle cuts and the mass induction are those of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the outline `YM4_sketch_500.tex` (SA), the complete account (CA-I/II/III) and the three-dimensional manuscript `YM3/YM3_I.tex` (Y3), all at commit `31a47c543775`. The renormalisation-group method is Tadeusz Balaban's (CMP 89, 95, 96, 98, 99, 102, 109, 116, 119, 122a, 122b); the ledger and the credit of Part C are his (CMP 122 (1989) 355, (1.79)–(1.81), (1.89)), in the global form of SA Proposition 2.6. Jonathan Dimock's expositions ("The renormalization group according to Balaban" I–III) are the readable reference for the small-field step. Our own notes used here: `c4-order.md` and `um-envelope.md` (Codex), which isolated the cycle and its missing matrix input; `b-value.md`, `prefactor-loc.md` (OL1); `geo-*.md` (C2 geometry).

Line references. SA L = line of `scratchpad/sa/ym4.tex`; Y3 L = line of `scratchpad/sa/YM3_I.tex` (fetched 2026-11-04 from the pinned commit, 89,144 lines). I quote line numbers before saying what a source proves or assumes. Where I say "SA states", I mean the text at those lines says so; it does not mean SA proves it.

Status words (as in `ym4-assembly.md` §0): **[P]** proved here, not checked; **[C]** checked elsewhere (check file named in the assembly); **[SP]** proved in a source; **[SS]** sketched in a source; **[O]** open. Imports are named `(I-…)` and are stated once, in Section 1, with their owner submanuscript and their status there.

---

## 0. What this draft proves, in one page

**Main theorem (IN1), as an implication.** Under the imports (I-1)–(I-14) of Section 1, with the order of constants of Part A:

1. **(C4)** One class 𝔆_k(θ) of presentations, with constants independent of k, contains the bare measure and is mapped into 𝔆_{k+1}(θ) by the exact step (Theorem D.6; along the actual run, Theorem D.8).
2. **(Order)** All constants admit one simultaneous order of choice; the cycle κ̄ → M → C₀^UM → Θ → κ̄ of `c4-order.md` is broken by a proof (Theorem A.7, resting on Proposition A.5 and Theorem A.6).
3. **(E1)** The flow x_j = β − Σ_{i≤j} b_i obeys λ_♯(j − i) − c₅ ≤ x_i − x_j ≤ B_♯(j − i), with increments independent of torus and finer cutoff (Theorem B.1).
4. **(First passage)** Every run from β ≥ g^{−2} + B_♯ reaches first passage; the bounds on K(β, g), the window, the infinitude of nonempty 𝒲_K(g) and β/log(1/a_K) → 11N²/(12π²) hold (Theorem B.2).
5. **(C3)** Every component that has passed the tests of an R-operation at level i has mass 𝖬(i, X) ≤ e^{−(2−c′)p₀(g_i)}; every created component at level j keeps exp[−c p₀(g_j) − κ|X|_j] with κ above the entropy rate; drop-outs obey the same bound over their evaluation fibres; the bound reproduces itself at later levels (Theorem C.8, Theorem C.9, Lemma C.11, Corollary C.12).

**Status of the parts.** Every step written inside this draft is [P]. Nothing inside IN1 is left outstanding as a statement of IN1. What IN1 does not prove is listed as imports: the small-field step (NL1, through (D4) of ST1), the large-field geometry and entropy (LF1(2)), the prepared/healed structure (LF1(4)–(5)), the one-step averaging estimate (BG1(1)), the matrix bounds at complex pairs (PR1(1)–(2)), and OL1(2)–(3). Section E lists each with its present status and names the first open one on IN1's path.

**The constants cycle (decided first, Part A).** The cycle is not real. It breaks with a proof: the UM cost C₀^UM is bounded by a constant B₀ = 1 fixed *before* κ and κ̄, uniformly in M and κ̄. The missing input that `um-envelope.md` §4 named (the decoupled inverse-root matrix Γ, its (6)) is proved here (Proposition A.5) from the gap, norm and exponential kernel decay of the fibre precision, by a Combes–Thomas estimate (Lemma A.1), an inverse-root kernel lemma (Lemma A.2), and an explicit path-cube decoupling (Definition A.3, Lemma A.4). The same cut is the one YM3 makes: Y3 fixes its Gaussian cost envelope c̄_P with L (Y3 L63134–63137), chooses κ̄ after it (Y3 L63196–63199), takes the tilt γ₂ = (LM)^{−3} (Y3 L63446–63448) and requires (LM)³ε_dc ≤ 1 for the matrix defect (Y3 L52685, L63239–63241). In four dimensions the power is (LM)⁴; the marginal coupling plays no role in this cycle. Downstream cost: the failed-bond cutoff of the regular gas must satisfy 𝔟² ≥ C(LM)⁴(Θ + log(LM)), which is a ceiling on g after M; the Gaussian budget W₀ is smaller than a free choice would give, which lowers the final ceiling on g. Nothing chosen before M changes.

**Where four dimensions differ from YM3 (the induction).** (i) The energy of averages: Y3's bootstrap (Y3 L7880–8040, Proposition II-6-57) carries a factor L^t and uses the decay ϖ_j ≤ L^{−(t−j)/2} of intermediate curvatures; in four dimensions the averaging kernel has ‖P‖_{2→2} ≤ 1 (scale invariance of the action, the same fact that makes the coupling marginal), the intermediate curvatures do not decay, and the bootstrap must run on ℓ¹-control of the quadratic errors with ‖P‖_{1→1} ≤ L^{−2} (Proposition C.2). (ii) The flow: the increments b_j are O(1) and the coupling moves only logarithmically, so thresholds are frame-indexed powers of log θ_j, and the step needs the tube, the weak triple and the telescoping bound (Part B). (iii) The ledger has only polylogarithmic margins: gain p₀(g) = A₀(log g^{−2})^{𝔭₀} against an event cost C M⁴ Ř⁶ ≈ (log g^{−2})^{6r}; this forces 𝔭₀ > 6r (the same exponent conditions as Y3 L63118–63121).

**Line count** of this file is reported in the session reply.

---

## 1. Setting, notation and imports

### 1.1 Notation

As in `ym4-assembly.md` §0. G = SU(2), d = 4, L odd, a_k = L^{−k}. For a real configuration W and a plaquette p, f_W(p) = |∂W(p) − 1| in the matrix operator norm; for SU(2), f_W(p)² = 2a_p(W) (SA L18210–18215: the eigenvalues of ∂W(p) are e^{±iφ}, |e^{iφ} − 1|² = 2 − 2cos φ and a_p = 1 − cos φ).

The exponents r, 𝔭₀, 𝔭₁, q, κ₀ and the frame quantities are those of SA L19469–19470 and `c4-order.md` row 25:

- Ř_j = the least power of L that is ≥ (log min_{i≤j} θ_i)^r; N_j = Ř_j (waiting depth);
- ε_j = θ_j^{−1/2} A₀ (log θ_j)^{𝔭₀} = g_j p₀(g_j) with g_j = θ_j^{−1/2} and p₀(g) = A₀(log g^{−2})^{𝔭₀} (SA L17257);
- δ_j = (A₁/A₀) ε_j; δ′_j = A₁ θ_j^{−1/2} (log θ_j)^{𝔭₁};
- α_{ι,j} = C_ι θ_j^{−1/2} (log θ_j)^q (radii, ι = 0, 1);
- 𝗌_k = (A₁/C₀)(log θ_k)^{𝔭₀ − q} (Cauchy factor of a first difference in the fluctuation field; `c4-order.md` hand check, "WF6").

A **frame** of length k is a sequence θ₀, …, θ_k with θ_j ≥ γ^{−2} and the **weak triple** bounds

  λ̲(j − i) − c₅ ≤ θ_i − θ_j ≤ B̄(j − i)  (i ≤ j ≤ k),  (F)

with λ̲ = c₀/4, c₅ = 2c₂, B̄ = C_β + 1, C_β = c₀ + 2c₂ + 1, fixed with L (SA L19485 for the cut; SA L20729–20736 (RF22) for the values; `c4-order.md` row 3a). Here c₀ = 11N² log L/(12π²) and c₂ = c₂(L) are the constants of OL1(3).

### 1.2 The imports

Each import is a statement proved, or to be proved, in another submanuscript. The owner and present status are from `ym4-assembly.md` §5.

**(I-1) Flat and background gap, norm and decay (FP1, PR1(1)–(2)).** There are a > 0, b < ∞, H < ∞, μ₀ > 0, depending on L and the constants of `c4-order.md` rows 1–7 only, such that for every regular real background U and every complex pair P in its admitted core with radii a₀, a₁ and independent current j₀ below ceilings that may depend on M, the gauge-fixed fibre precision 𝖠(P) of SA L14097–14107 on the fluctuation coordinates satisfies:
  (a) 𝖠(P) is complex symmetric (bilinear transpose); 𝖠(U, 0) is real;
  (b) Re⟨v, 𝖠(P)v⟩ ≥ a|v|² for all v (on every compression to a coordinate subset, in particular);
  (c) |𝖠(P)(x, y)| ≤ H e^{−μ₀ d(x,y)};
  (d) |𝖠(P)(x, y) − 𝖠(U, 0)(x, y)| ≤ η(P) e^{−μ₀ d(x,y)}, with η(P) ≤ H_p(M)(a₀ + a₁ + j₀) for a function H_p of M and earlier constants.
Status: (b)–(c) at real critical backgrounds [C] (A2 on separated layers, A3 real-critical chain); at complex single-layer pairs [C]; at layered stage pairs ⟦open: PR-lay⟧ (PR1(5)). SA states (b) with the gap ½γ₀ after choosing ℓ₀, a_w, M and then the radii (SA L14141–14149) and (c) as "the same exponential kernel bounds" (SA L14150–14152).

**(I-2) Local Gaussian comparison (SA Theorem, L13904–14056).** For complex symmetric C and complex Γ with real references (C₀ = C₀^T > 0, Γ₀) and ‖C₀‖ + ‖C₀^{−1}‖ + ‖Γ₀‖ ≤ K, ‖C − C₀‖ + ‖Γ − Γ₀‖ ≤ ε ≤ ε₀(K), ρ ≤ ρ₀(K), the functional 𝒥_{C,Γ} of (FG4) satisfies (FG6) and (FG11), with A_K, ε₀(K), ρ₀(K) depending on K only and not on the local or auxiliary dimension. Status [SP]: SA L13973–14056 gives a complete proof (accretivity of the joint precision (FG7)–(FG8), integration of the auxiliary variable, the determinant identity (FG9), and the local-dimension estimate (FG10)–(FG11)). I read the proof; every constant in it is a function of K. Its check waits for the hardening pass.

**(I-3) The UM machinery (NL1(1)).** The unmarked-majorant argument of SA L14276–14810: the formulas (UM1)–(UM3), the counts (UM7)–(UM11), the budget (UM12)–(UM16), the activity bound (UM17)–(UM24) and the logarithm (UM25)–(UM30), *given* (UM4)–(UM6) with constants (K, ε) and the structural identities (heredity, normalised functional, wall factorisation; SA L14406–14413). Status: the deductions are written in SA; the structural identities for the actual gas are NL1's [SS].

**(I-4) One-loop coefficient (OL1(2)–(3)).** b_k⁰ = A_k − A_{k−1} with A_k = b[Ψ_k], and |A_k − k c₀| ≤ c₂. Status: (2) [C], (3) [P] (`b-value.md` Theorem V).

**(I-5) The small-field step and its error bounds (NL1(3) with (D4) of ST1, OL1(5)).** For 𝔓 ∈ 𝔆_k(θ) (Part D) and a frame prolongation θ_{k+1}, the regular family Ê^{(k+1)} is formed at the pair (θ_k, x_k) before any level-(k+1) choice, and its coefficient b_{k+1} = b[Ê^{(k+1)}] obeys (SA L20683–20696, (RF20)):

  b_{k+1} = b_{k+1}⁰ + f_{k+1} + q_{k+1},  |f_{k+1}| ≤ C_f θ_k^{−1/2}(log θ_k)^{𝔭₀},  |q_{k+1}| ≤ C_v θ_k^{−p_R},  p_R = (κ₀ − 4)/2,

with C_f, C_v fixed before γ (they depend on the weak triple, not on γ). Moreover, under the tube for x_{k+1}, the exact small-field step is defined, preserves every sourced integral, and returns E^{(k+1)}, R^{(k+1)}, B^{(k+1)} with

  ‖E^{(k+1)}‖_{k+1,κ} ≤ E_𝖭 + C_E(|1 − τ_k| + δ_k + 𝗌_k N_⋆ + e^{−c p₀(g_k)²}),  ‖R^{(k+1)}‖ ≤ g_{k+1}^{κ₀},  |B^{(k+1)}(X)| ≤ 𝖡 e^{−κ d^♮(X)},

whenever its input satisfies the uniformity bound (D.3) below with N_⋆; here E_𝖭 is the localised Gaussian normaliser bound and C_E depends neither on E₀ nor on N_⋆ (SA L19513–19515); 𝖡 is the maximum of the origin bounds, none of which depends on 𝖡 (SA L19515–19521). Analyticity, reality, gauge invariance, identification (iii), covariance (iv) and coherence (v) of SA (2e) are preserved. Status: NL1 whole [O] through (D4); one-level implication of B4 [C]; the error bounds (RF20) are SA's statement [SS].

**(I-6) Exact large-field operations (LF1(1) = C1).** Every move is a Borel kernel, change of variables or partition of unity; tests are total (a test is the indicator of the set where every object it reads exists and its inequalities hold); every stored variable is integrated or retained once; sourced integrals are preserved; for real inputs every weight is a nonnegative measure. Status [C] (`c1-repr.md`).

**(I-7) Geometry, the genealogy and the waiting rule (LF1(2) = C2).** The regions, hulls S(Z), components, created cells, marks, genealogies Gen(u_*) and the "occupied cells" of SA L17719–17760 are defined, and:
  (G1) |C(u)|_{n(u)} ≤ C_g (1 + 𝗈(u)), where 𝗈(u) is the number of occupied cells of u;
  (G2) for a fixed s₀ (geometric), 𝗈_n ≤ ½ 𝗈_{n−s₀} + C_g l_{n−s₀} + Σ_{n−s₀<t≤n} 𝗇_t^cr, where 𝗈_n, l_n are the numbers of occupied cells and of light components of level n in Gen(u_*) (SA L17744–17753);
  (G3) a stretch (maximal chain of members with one predecessor and nothing new, started by an event) that starts at level t has at most 𝖳_t = C Ř_t light members (SA L17753, "once a further N_t quiet levels have passed it has entered the class");
  (G4) a member with no predecessor contains a created cell of its own level; predecessors have lower level;
  (G5) the entropy of outer records: for each component X and volume V°, Σ_{ω° with V°(ω°) = V} 1 ≤ e^{c_e V} (SA L18672–18715).
Status: GEO1–GEO6, EXT, W3 [C] under three supplied rules; (G1)–(G5) for the actual histories [O] (rest of C2).

**(I-8) Prepared structure (LF1(4), 2.8).** For a component X that has passed every test of R at level i, the exponent of its operation has the form Φ_ω(ξ; 𝐩) = Φ°_ω(ξ) + Ψ_ω(ξ; 𝐩) with Φ°_ω real Borel and

  Re Ψ_ω(ξ; 𝐩) ≤ C_Ψ V°(ω)  for every 𝐩 ∈ U^c_i(X^~, α_{0,i}, α_{1,i}),

where V°(ω) counts the stored sites of the outer record, each at its own level. (SA L17824–17828: Ψ = −½q_X + V(X^~), q_X ≥ 0 formed at a real background, |V(X^~)| ≤ C #{stored sites}.) e^{Φ°_ω} contains the core Wilson factor exp[−A(x″_i φ_c, U″(ξ))], the weights 𝗐_{t,D} of the pieces (gauge-fixing factors with normalisers, pivot Jacobians, conditional Gaussians) and the factors of inner islands. Status: [C] conditional (`gates/sa-2.8-terms-gate.md`), open items I1 and the Gaussian comparison of 2.8-T^C ⟦open: LF-2.8⟧.

**(I-9) Shares (SA L17695–17700, "One action and many claimants" (1)–(2)).** The action splits into shares owned by pieces (t, D); distinct pieces have disjoint shares; on a share x_k(·) = x_{t−1}; every other plaquette contributes ≥ 0; the stored averages of the configuration in the Wilson term are the averages V_t read by the tests. Status [SS].

**(I-10) One-step averaging estimate (BG1(1)).** For a coarse plaquette p′ of level n + 1 with corner blocks 𝖸 = ∪_i B(y_i) and a real W on the fine bonds in 𝖸 with ϖ = max_{p ⊂ 𝖸} f_W(p) ≤ ϖ′_L,

  f_{𝓜W}(p′) ≤ Σ_p 𝖶(p′, p) f_W(p) + C^{SO} ϖ_{p′}²,  ϖ_{p′} = max_{p ⊂ 𝖸} f_W(p),

with the kernel 𝖶(p′, p) = L^{−4}#{x ∈ B(y₁) : p ∈ S_x(p′)}, S_x(p′) = {p_{μν}(x + ie_μ + je_ν) : 0 ≤ i, j < L}; and the globally defined average agrees with its regular branch there. Status: proved in three dimensions (Y3 Lemma I-10-97, L6862–6885, with the kernel (I-10-95), L6785, and Lemma I-10-96); in four dimensions [SS] (SA L18216–18222, (average-one-step)). The kernel counts in d = 4 are proved here (Lemma C.1).

**(I-11) Test certificates other than plaquette tests (BG1(2), PR1(1), (2b)).**
  (a) *Linear regularity*: if every plaquette of V_t in the test neighbourhood of a cube □ satisfies f_{V_t} < c_lin ε_t, the localised background exists and the plaquette test at □ passes (SA L18281–18286; BG1(2)).
  (b) *Approximate fluctuation test*: failure implies A_{𝔠^~}(U) + GF_{t−1}(𝔠^~; V_{t−1}) ≥ c δ_{t−1}² for every real U with the stored averages (SA L18287–18301).
  (c) *Kept forms*: the complete conditional form satisfies ⟨a, Δ a⟩ ≥ κ_pos‖a‖² in the stored scaled coordinates, and the kept truncated form has the same lower bound (SA L18303–18327; PR1(1) and the cut-form comparison of (2b)); a failed fluctuation, collar or rim test forces a stored scaled coordinate of size ≥ c δ_{t−1}/g_{t−1}.
  (d) *Renewed mark*: a failed test of an operation R at level m, inside a patch, gives the gain p₀(g_m) from action outside the floor (SA L17709, item (4); L18334–18415).
  (e) *Chart Jacobians*: each pivot chart and elimination determinant costs at most J₀ per owning coordinate (SA L18751–18755).
Status: (a) [C] as A1 on separated sequences plus the test definitions; (b), (d) [SS]; (c) [C] for A2, [SS] for the cut-form comparison; (e) [C] for the pivot chart (BG1(1)).

**(I-12) Layer-by-layer support bounds (class clause; ST1).** On the supports, for a term of level k and the layer Ω_j ∖ Ω_{j+1}: |∂U_k − 1| < C_sup Ř_j² ε_j η_j², |J(U_k)| < C_sup Ř_j² ε_j (SA L17829–17830). Status [SS]; it is part of what (D4) must deliver.

**(I-13) Sources (SC1).** Source discs are among the interpolation discs; the step is holomorphic in the source; constant-source slopes as SA (3c). Used only through (I-5). Status [O] through NL1.

**(I-14) Large-field sums (LF1(5)–(6)).** Healed deletion (2.10) and the loaded-label sum (2.13), used only to state the class conclusions (stability floor, UV1 input), not in the proofs of Parts A–C. Status [O] for the remaining items.

---

## Part A. The order of constants, and the cycle κ̄ → M → C₀^UM → Θ → κ̄

### A.0 The cycle as the sources state it

`c4-order.md` (Codex, [P]) found one cycle that its order did not cut. Its two ends, read in SA:

- SA L19477: "$\delta_0M\gg\bar\kappa\gg L\kappa$: rates are chosen before the cube sizes $M_1'$, $M_2$, $M$. These are floors on $\bar\kappa$ and then on $M$." The same requirement appears where the coarse parameters are paid: "For independent $|s_\Delta|\le e^{\bar\kappa}$, a carrier that meets $m$ parameter cubes contributes at most $e^{m\bar\kappa}$ … Every further cube requires length proportional to $M$, whose exponential decay pays for its parameter once $cM\ge C\bar\kappa$" (SA L14177–14182).
- SA L14576–14584, (UM18)–(UM19): Θ = C_h(C₀ + K_*), and log(R_s − 1) ≥ Θ with R_s = e^{κ̄}. And C₀ is (SA L14526–14528, (UM15))

  C₀ = C_p W₀ L⁴ + A_K c_m (LM)⁴ (ε + C_p W₀ M^{−4} + γ/2).  (A.0)

So κ̄ ≥ Θ(C₀), C₀ depends on M through (LM)⁴(ε + γ/2), and M ≥ Cκ̄. If C₀ had to grow with M, no order could exist. SA L14779–14788 says what would suffice: "it suffices that the matrix package control $A_Kc_m(LM)^4\varepsilon$ by a fixed constant on the chosen decoupling discs. Choose $W_0$ so its two contributions to $C_0$ are bounded, and choose positive $\gamma$ of order at most $(LM)^{-4}$ … Then $C_0$ is bounded independently of exterior volume." SA L14789–14791 adds that this "does not assert them for a matrix family whose constants have not been controlled on the required enlarged discs". `um-envelope.md` §§3–5 (Codex) proved the budget allocation and the resulting order *conditionally* on a matrix estimate, its (6)–(7), and found that (6), the bound for the decoupled inverse-root matrix Γ, had no proof in our notes (`h-walk.md:440` excludes it).

**Decision.** The cycle is not real. It breaks with a proof: Proposition A.5 proves `um-envelope.md` (6)–(7) from (I-1), with every constant fixed before κ. Theorem A.6 then fixes C₀^UM ≤ 1 before κ and κ̄. Theorem A.7 gives the full order.

**The YM3 template.** Y3 makes the same cut in three dimensions, explicitly. After L and the Gaussian reserve: "$N_{\rm gs}=64B_{\rm nm}^5\gamma_0^{-2}+c_{\rm r}+2$, $\bar c_P=\mathsf C_{\rm mn}^3\lambda_{\rm r}^{-1}N_{\rm gs}$. These numbers depend only on $L$ and the Gaussian reserve" (Y3 L63134–63137). κ̄ is chosen after this envelope: "$\bar\kappa\ge1+\mathsf C_{\rm cs}\bar r_H+\log\mathsf C_{\rm cs}$" with r̄_H containing C_cs(c̄_P + 2) (Y3 L63190–63198). Then M last among the lengths, and "The small radii are subsequently reduced so that the complex perturbation of the historical Gaussian form is bounded by its available gap … $B_{\rm nm}\varepsilon_{\rm dc}\le\gamma_0/2$, $(LM)^3\varepsilon_{\rm dc}\le1$. The exponentially small part of $\varepsilon_{\rm dc}$ is controlled by the choice of $M$" (Y3 L63236–63247). The tilt is "$\gamma_2=(LM)^{-3}$" and then "$c_P=\mathsf C_{\rm mn}^2\lambda_{\rm r}^{-1}(LM)^3u_0\le\bar c_P$" (Y3 L63446–63458). The port to four dimensions replaces (LM)³ by (LM)⁴ (the number of scalar coordinates per coarse cube grows like the volume); nothing about the marginal coupling enters. What our notes lacked is the uniform matrix defect. Y3 states its defect condition as a hypothesis of its historical-Gaussian theorem (Y3 L52685: "If also $(LM)^3\varepsilon_{\rm dc}\le1$") and splits the defect into a part controlled by M and a part controlled by the radii (Y3 L63246–63249); I did not read Y3's proof of that split. In four dimensions we prove the corresponding bound in A.1–A.5.

### A.1 Combes–Thomas for accretive matrices

Let Λ be a finite set with a metric d (here: the positions of the fluctuation coordinates on a torus, d the periodic lattice ℓ¹-distance between their base sites). Assume the ball bound

  #{y ∈ Λ : d(x, y) ≤ ρ} ≤ n_c (2ρ + 1)⁴  for all x ∈ Λ, ρ ≥ 0,  (A.1)

with n_c the number of coordinates per site (bonds per site times dim su(2)). For ν > 0 put V(ν) := Σ_{ρ=0}^∞ n_c(2ρ + 1)⁴ e^{−νρ} < ∞.

**Lemma A.0 (volume sum).** sup_x Σ_y e^{−ν d(x,y)} ≤ V(ν).

*Proof.* d takes integer values. Write N(ρ) = #{y : d(x, y) ≤ ρ}. Then Σ_y e^{−νd(x,y)} = Σ_{ρ≥0} (N(ρ) − N(ρ − 1)) e^{−νρ} = Σ_{ρ≥0} N(ρ)(e^{−νρ} − e^{−ν(ρ+1)}) ≤ Σ_ρ N(ρ) e^{−νρ} ≤ V(ν), by Abel summation (all sums finite since Λ is finite) and (A.1). □ [P]

For a complex matrix B on ℂ^Λ and μ ≥ 0, put ‖B‖_μ := max{sup_x Σ_y |B(x,y)| e^{μ d(x,y)}, sup_y Σ_x |B(x,y)| e^{μ d(x,y)}}. By the Schur test, the operator norm satisfies ‖B‖ ≤ ‖B‖₀ ≤ ‖B‖_μ. If |B(x,y)| ≤ h e^{−ν d(x,y)} entrywise, then ‖B‖_μ ≤ h V(ν − μ) for μ < ν (Lemma A.0). Conversely every entry satisfies |B(x,y)| ≤ ‖B‖_μ e^{−μ d(x,y)}.

**Lemma A.1 (resolvent decay).** Let B satisfy Re⟨v, Bv⟩ ≥ a|v|² for all v ∈ ℂ^Λ, with a > 0, and ‖B‖_{μ′} ≤ H′ for some μ′ > 0. Put μ₁ := min{μ′/2, e a μ′/(4H′)}. Then for every ζ ≥ 0 the matrix ζ + B is invertible and, for 0 ≤ μ ≤ μ₁,

  |(ζ + B)^{−1}(x, z)| ≤ e^{−μ d(x,z)} / (ζ + a/2)  for all x, z ∈ Λ.

*Proof.* (1) For any matrix T with Re⟨v, Tv⟩ ≥ c|v|², c > 0: |v||Tv| ≥ |⟨v, Tv⟩| ≥ Re⟨v, Tv⟩ ≥ c|v|², so T is injective, hence invertible (Λ finite), and ‖T^{−1}‖ ≤ 1/c.
(2) Fix z and put φ(w) = d(w, z); φ is 1-Lipschitz for d. Let D_± = diag(e^{±μφ}) and B_μ = D_+ B D_−, with entries B(x, y) e^{μ(φ(x) − φ(y))}. Since |e^t − 1| ≤ |t| e^{|t|} and |φ(x) − φ(y)| ≤ d(x, y),

  |B_μ(x,y) − B(x,y)| ≤ |B(x,y)| μ d(x,y) e^{μ d(x,y)} = |B(x,y)| e^{μ′ d(x,y)} · μ d(x,y) e^{−(μ′−μ) d(x,y)} ≤ |B(x,y)| e^{μ′d(x,y)} · μ/(e(μ′ − μ)),

using t e^{−αt} ≤ 1/(eα) for t ≥ 0, α > 0. By the Schur test ‖B_μ − B‖ ≤ μH′/(e(μ′ − μ)) ≤ 2μH′/(eμ′) ≤ a/2 for μ ≤ μ₁ (μ ≤ μ′/2 gives μ′ − μ ≥ μ′/2).
(3) Hence Re⟨v, (ζ + B_μ)v⟩ ≥ (ζ + a)|v|² − (a/2)|v|² = (ζ + a/2)|v|², and by (1) ‖(ζ + B_μ)^{−1}‖ ≤ 1/(ζ + a/2). Also ζ + B is invertible by (1) (Re ≥ ζ + a), and (ζ + B)^{−1} = D_−(ζ + B_μ)^{−1}D_+ because ζ + B_μ = D_+(ζ + B)D_−.
(4) The (x, z) entry: (ζ + B)^{−1}(x, z) = e^{−μφ(x)} (ζ + B_μ)^{−1}(x, z) e^{μφ(z)} = e^{−μ d(x,z)} (ζ + B_μ)^{−1}(x, z), and an entry of a matrix is at most its operator norm. □ [P]

### A.2 The inverse square root

**Lemma A.2 (inverse-root kernel).** Under the hypotheses of Lemma A.1, the integral

  R(B) := (1/π) ∫₀^∞ ζ^{−1/2} (ζ + B)^{−1} dζ

converges absolutely, and:
  (a) |R(B)(x, z)| ≤ (2/a)^{1/2} e^{−μ₁ d(x,z)};
  (b) if B^T = B then R(B)^T = R(B), and R(B)² = B^{−1};
  (c) if B′ satisfies the same hypotheses with the same (a, μ′, H′), then |R(B)(x,z) − R(B′)(x,z)| ≤ ½(2/a)^{3/2} V(μ₁/2)² ‖B − B′‖_{μ′} e^{−(μ₁/2) d(x,z)}.

*Proof.* (a) By Lemma A.1 with μ = μ₁, the integrand's (x, z) entry is at most ζ^{−1/2} e^{−μ₁ d(x,z)}/(ζ + a/2), and (1/π)∫₀^∞ ζ^{−1/2}(ζ + c)^{−1} dζ = c^{−1/2} (substitute ζ = c t²: ∫₀^∞ 2c^{1/2}·c^{−1}(1 + t²)^{−1} dt = π c^{−1/2}). With c = a/2 this is (2/a)^{1/2}.
(b) Transposition is linear and continuous, and ((ζ + B)^{−1})^T = (ζ + B^T)^{−1} = (ζ + B)^{−1}, so R(B)^T = R(B). For R(B)² = B^{−1}: let 𝒜 be the set of complex symmetric matrices with Re⟨v, Bv⟩ > 0 for all v ≠ 0. 𝒜 is open and convex in the complex vector space Sym_ℂ of complex symmetric matrices. On 𝒜, B ↦ R(B) is holomorphic in the entries (the integrand is holomorphic and the integral converges locally uniformly by the bound in (a), uniform on compact subsets of 𝒜 where a is bounded below), and so is F(B) := R(B)² − B^{−1}. For real symmetric positive definite B = O diag(λ_i) O^T, R(B) = O diag((1/π)∫ζ^{−1/2}(ζ + λ_i)^{−1}dζ) O^T = O diag(λ_i^{−1/2}) O^T, so F(B) = 0. Real symmetric positive definite matrices form an open subset of the real form Sym_ℝ of Sym_ℂ; a holomorphic function on a connected open set of Sym_ℂ vanishing on a nonempty open subset of Sym_ℝ vanishes identically (identity theorem, applied one entry at a time as in SA L14024–14031). Hence F ≡ 0 on 𝒜.
(c) (ζ + B)^{−1} − (ζ + B′)^{−1} = (ζ + B)^{−1}(B′ − B)(ζ + B′)^{−1}. Its (x, z) entry is at most Σ_{u,v} e^{−μ₁ d(x,u)} |(B′ − B)(u, v)| e^{−μ₁ d(v,z)} (ζ + a/2)^{−2}. Use |(B′ − B)(u,v)| ≤ ‖B′ − B‖_{μ′} e^{−μ′ d(u,v)} ≤ ‖B′ − B‖_{μ′} e^{−μ₁ d(u,v)} (μ₁ ≤ μ′) and d(x,z) ≤ d(x,u) + d(u,v) + d(v,z):

  e^{−μ₁(d(x,u) + d(u,v) + d(v,z))} ≤ e^{−(μ₁/2) d(x,z)} e^{−(μ₁/2) d(x,u)} e^{−(μ₁/2) d(v,z)}.

Summing over u and v with Lemma A.0 gives the factor V(μ₁/2)². Finally (1/π)∫₀^∞ ζ^{−1/2}(ζ + c)^{−2}dζ = ½ c^{−3/2} (differentiate the identity in (a) in c), and c = a/2. □ [P]

### A.3 An explicit decoupling

Let the fluctuation coordinates Λ live on the level-k lattice, partitioned into the coarse cubes Δ of side ℓ = LM (lattice units). Let Z₀ ⊂ Λ be the fine support of an integrand, χ = 1_{Z₀}, and Z₀^♯ ⊃ Z₀ its coarse collar (SA L14338–14347): the union of the coarse cubes containing a fine cube of 𝒩_f(Z₀). Then

  dist(Z₀, Λ ∖ Z₀^♯) ≥ w := M,  (A.2)

since every site at lattice distance < M from Z₀ lies in a fine cube of 𝒩_f(Z₀) (a fine cube has side M, and 𝒩_f adds the full first layer of neighbouring fine cubes in the cubical adjacency, which contains every fine cube within ℓ^∞-distance < M).

**Definition A.3 (path-cube decoupling).** For each unordered pair {x, y} ⊂ Λ fix a lattice geodesic π(x, y) between the base sites of x and y (any fixed rule, symmetric: π(y, x) is π(x, y) reversed). Let D(x, y) be the set of coarse cubes Δ ⊄ Z₀^♯ that meet π(x, y). For parameters s = (s_Δ) ∈ ℂ^{cubes} and s^D := Π_{Δ∈D} s_Δ (s^∅ = 1), and any matrix B on ℂ^Λ, define

  B^s(x, y) := B(x, y) s^{D(x,y)}.

For the precision use B = 𝖠(P); for the inverse root use B = R(𝖠(P)). Then define

  C(s; P) := (χ 𝖠(P)^s χ)^{−1},  r(s; P) := (1 − χ) R(𝖠(P))^s,  Γ(s; P) := −χ 𝖠(P)^s (1 − χ) r(s; P).  (A.3)

At s ≡ 1 these are C = (χ𝖠χ)^{−1} and Γ = −χ𝖠(1 − χ)·(1 − χ)𝖠^{−1/2}. The references are C₀ := C(0; ref), Γ₀ := Γ(0; ref) with ref = (U, 0), where s = 0 means s_Δ = 0 for every Δ ⊄ Z₀^♯ (the s_Δ with Δ ⊂ Z₀^♯ do not occur).

**Lemma A.4 (properties of the decoupling).** (a) |D(x, y)| ≤ 16(1 + d(x, y)/ℓ).
(b) If x ∈ Z₀ and D(x, y) ≠ ∅, then d(x, y) ≥ w. If x ∈ Z₀ and D(x, y) ∪ D(y, z) ≠ ∅, then d(x, y) + d(y, z) ≥ w.
(c) Each entry of B^s is a polynomial in s; C, r, Γ are holomorphic in s wherever χ𝖠^sχ is invertible.
(d) At s ≡ 1: C + CΓΓ^T C = χ 𝖠^{−1} χ (on the χ-block).
(e) (Wall factorisation of the Gaussian data.) Let Z₀ = Z₀′ ⊔ Z₀″ and suppose every lattice path from a site of Z₀′ to a site of Z₀″ meets a cube Δ with s_Δ = 0. Then χ𝖠^sχ, C and the matrix D := C + CΓΓ^TC are block diagonal for Z₀′ ⊔ Z₀″.

*Proof.* (a) Cut the geodesic, which has d(x, y) + 1 sites, into ⌈(d + 1)/ℓ⌉ ≤ 1 + d/ℓ consecutive pieces of at most ℓ sites. A piece has ℓ^∞-diameter < ℓ, so it meets at most 2⁴ = 16 cubes of side ℓ.
(b) If Δ ∈ D(x, y), π(x, y) contains a site p ∉ Z₀^♯, so d(x, p) ≥ w by (A.2), and d(x, y) = d(x, p) + d(p, y) ≥ w because π is a geodesic. For the second claim, if D(x, y) ≠ ∅ use the first; if Δ ∈ D(y, z), take p ∈ π(y, z) ∖ Z₀^♯; then w ≤ d(x, p) ≤ d(x, y) + d(y, p) ≤ d(x, y) + d(y, z).
(c) Immediate; inversion is holomorphic on invertible matrices.
(d) Write the χ-block and its complement c-block: 𝖠 = [[𝖠_χχ, X], [X^T, 𝖠_cc]] (𝖠 symmetric). By Lemma A.2(b), r r^T = (1 − χ)𝖠^{−1/2}𝖠^{−1/2}(1 − χ) = [𝖠^{−1}]_cc, so ΓΓ^T = X [𝖠^{−1}]_cc X^T. Block inversion gives [𝖠^{−1}]_cc = S^{−1} with S = 𝖠_cc − X^T 𝖠_χχ^{−1} X and [𝖠^{−1}]_χχ = 𝖠_χχ^{−1} + 𝖠_χχ^{−1} X S^{−1} X^T 𝖠_χχ^{−1} = C + CΓΓ^TC. (Both 𝖠_χχ and S are invertible: 𝖠 is accretive, so its compressions are accretive, and S^{−1} is a compression of 𝖠^{−1}, which exists.)
(e) An entry 𝖠^s(x, x′) with x ∈ Z₀′, x′ ∈ Z₀″ vanishes, because π(x, x′) is a lattice path from Z₀′ to Z₀″ and so meets a cube with s_Δ = 0; that cube is not in Z₀^♯ (collar cubes have no parameter by definition; in the polymer use of SA L14363–14365, s_Δ = 0 only off Z). So χ𝖠^sχ is block diagonal, and so is its inverse C. For ΓΓ^T(x, x′) = Σ_z Γ(x, z)Γ(x′, z), a nonzero term needs y, y′ with 𝖠^s(x, y) R^s(y, z) 𝖠^s(x′, y′) R^s(y′, z) ≠ 0; then the concatenation π(x, y)π(y, z)π(z, y′)π(y′, x′) is a lattice path from Z₀′ to Z₀″ meeting no cube with s_Δ = 0, a contradiction. So ΓΓ^T, hence D, is block diagonal. □ [P]

*Remark on the polymer use.* In (UM3) the parameters are s_Δ ∈ ℂ on cubes of Z ∖ Z₀^♯ and s_Δ = 0 off Z (SA L14363–14365). Two wall-components of a coarse domain Z are separated in the sense of (e) because a lattice path passes between two cubes only through a shared wall (a nearest-neighbour step changes one coordinate). So (e) gives the factorisation of the Gaussian data over wall-components. The other structural identities of (I-3) (heredity, the normalised functional on general local cores) concern the assigned operators and supports and stay with NL1.

### A.4 The uniform matrix envelope

**Proposition A.5 (uniform envelope; `um-envelope.md` (6)–(7)).** Assume (I-1) with (a, b, H, μ₀). Put μ′ = μ₀/2, H′ = H V(μ₀/2), μ₁ = min{μ′/2, e a μ′/(4H′)} (Lemma A.1), μ₂ := μ₁/2, and

  K₀ := max{1, 4/a + 2HV(μ₀/2) + H V(μ₀/2)(2/a)^{1/2} V(μ₁/2)},  H₀ := explicit in (A.8) below.

These depend on (a, H, μ₀, n_c) only. Let κ̄ ≥ 1 and suppose

  M ≥ 128κ̄/μ₂  and  2H V(μ₀/2) e^{16κ̄ − μ₀M/4} ≤ a/4.  (A.4)

Then for every complex pair P in the core and every s with |s_Δ| ≤ e^{κ̄}:
  (i) Re χ𝖠(P)^sχ ≥ (3a/4); C(s; P) exists and ‖C(s; P)‖ ≤ 4/(3a);
  (ii) the reference is real, C₀ = C₀^T > 0, and ‖C₀‖ + ‖C₀^{−1}‖ + ‖Γ₀‖ ≤ K₀;
  (iii) ‖C(s; P) − C₀‖ + ‖Γ(s; P) − Γ₀‖ ≤ H₀ (e^{32κ̄ − μ₂M/4} + η(P)).

*Proof.* Throughout, w = M by (A.2) and ℓ = LM ≥ M. By (A.4), 16κ̄/ℓ ≤ μ₂/8 ≤ μ₂/4, and μ₂M/4 ≥ 32κ̄.

*Step 1 (decoupled entries).* For any B with |B(x,y)| ≤ h e^{−ν d(x,y)}, ν ≥ μ₂, and |s_Δ| ≤ e^{κ̄}: by Lemma A.4(a), |s^{D(x,y)}| ≤ e^{16κ̄(1 + d/ℓ)} ≤ e^{16κ̄} e^{(μ₂/4)d}. If D(x, y) = ∅, s^D = 1.

*Step 2 (proof of (i)).* For x, y ∈ Z₀, 𝖠^s(x, y) − 𝖠(x, y) = 𝖠(x, y)(s^D − 1) vanishes unless D ≠ ∅, in which case d(x, y) ≥ w (Lemma A.4(b)). So |entry| ≤ H e^{−μ₀d}(e^{16κ̄}e^{(μ₀/4)d} + 1) 1[d ≥ w] ≤ 2H e^{16κ̄} e^{−(3μ₀/4)d} 1[d ≥ w] ≤ 2H e^{16κ̄ − μ₀w/4} e^{−(μ₀/2) d} (using μ₂ ≤ μ₀). By Lemma A.0 and the Schur test, ‖χ(𝖠^s − 𝖠)χ‖ ≤ 2HV(μ₀/2) e^{16κ̄ − μ₀M/4} ≤ a/4 by (A.4). Since Re⟨v, χ𝖠χ v⟩ ≥ a|v|² on the χ-block (I-1)(b), Re χ𝖠^sχ ≥ 3a/4, and Lemma A.1 step (1) gives ‖C‖ ≤ 4/(3a).

*Step 3 (proof of (ii)).* At ref, 𝖠(ref) is real symmetric and so is 𝖠(ref)^0 (D is symmetric). By Step 2 at s = 0, χ𝖠(ref)^0χ ≥ 3a/4 > 0, so C₀ = C₀^T > 0 is real with ‖C₀‖ ≤ 4/(3a). Also ‖C₀^{−1}‖ = ‖χ𝖠(ref)^0χ‖ ≤ H V(μ₀) by the entrywise bound and the Schur test. Γ₀ = −χ𝖠(ref)^0(1 − χ)·(1 − χ)R(𝖠(ref))^0 is real. Entrywise |𝖠(ref)^0(x,y)| ≤ H e^{−μ₀d} and |R(𝖠(ref))^0(y,z)| ≤ (2/a)^{1/2} e^{−μ₁ d} (Lemma A.2(a) with B = 𝖠(ref), which satisfies Lemma A.1's hypotheses with (a, μ′, H′) because ‖𝖠(ref)‖_{μ₀/2} ≤ H V(μ₀/2)); the weight 1[D = ∅] is ≤ 1. Hence ‖Γ₀‖ ≤ H V(μ₀)(2/a)^{1/2} V(μ₁). Since V is decreasing in ν, ‖C₀‖ + ‖C₀^{−1}‖ + ‖Γ₀‖ ≤ 4/a + 2HV(μ₀/2) + HV(μ₀/2)(2/a)^{1/2}V(μ₁/2). We define K₀ as the maximum of 1 and this number (the comparison theorem (I-2) is stated for K ≥ 1).

*Step 4 (C).* χ𝖠(P)^sχ − χ𝖠(ref)^0χ = χ(𝖠(P)^s − 𝖠(ref)^s)χ + χ(𝖠(ref)^s − 𝖠(ref)^0)χ. The first has entries (𝖠(P) − 𝖠(ref))(x,y) s^D, bounded by η e^{−μ₀ d}·max{1, e^{16κ̄}e^{(μ₀/4)d}1[d ≥ w]} ≤ η e^{−(μ₀/2)d}·max{1, e^{16κ̄ − μ₀w/4}} ≤ η e^{−(μ₀/2)d}, using (I-1)(d) and M ≥ 128κ̄/μ₂ ≥ 64κ̄/μ₀ (so μ₀M/4 ≥ 16κ̄). The second is bounded as in Step 2 by 2H e^{16κ̄ − μ₀w/4}e^{−(μ₀/2)d}. Hence ‖χ𝖠(P)^sχ − χ𝖠(ref)^0χ‖ ≤ V(μ₀/2)(η + 2H e^{16κ̄ − μ₀M/4}), and by the resolvent identity C − C₀ = C(χ𝖠(ref)^0χ − χ𝖠(P)^sχ)C₀,

  ‖C(s; P) − C₀‖ ≤ (4/(3a))² V(μ₀/2)(η + 2H e^{16κ̄ − μ₀M/4}).  (A.5)

*Step 5 (Γ).* For x ∈ Z₀ and z ∈ Λ,

  −Γ(s;P)(x, z) + Γ₀(x, z) = Σ_{y ∉ Z₀} [𝖠(P)(x,y)R_P(y,z) σ(x,y,z) − 𝖠(ref)(x,y)R_ref(y,z) σ₀(x,y,z)],

with R_P = R(𝖠(P)), R_ref = R(𝖠(ref)), σ = s^{D(x,y)} s^{D(y,z)} and σ₀ = 1[D(x,y) = D(y,z) = ∅]. Split the bracket as

  (I) [𝖠(P)R_P − 𝖠(ref)R_ref](x, y, z) σ  and  (II) 𝖠(ref)(x,y) R_ref(y,z) (σ − σ₀),

where [·](x,y,z) means the product of the (x,y) and (y,z) entries. Put d₁ = d(x, y), d₂ = d(y, z).

(II): σ − σ₀ = 0 unless D(x,y) ∪ D(y,z) ≠ ∅, in which case d₁ + d₂ ≥ w (Lemma A.4(b)) and |σ − σ₀| ≤ |σ| + 1 ≤ 2 e^{32κ̄} e^{(μ₂/4)(d₁ + d₂)} (Step 1 twice). With |𝖠(ref)(x,y)| ≤ H e^{−μ₀ d₁} ≤ He^{−μ₂ d₁} and |R_ref(y,z)| ≤ (2/a)^{1/2} e^{−μ₁ d₂} ≤ (2/a)^{1/2}e^{−μ₂ d₂}:

  |(II)| ≤ 2H(2/a)^{1/2} e^{32κ̄} e^{−(3μ₂/4)(d₁+d₂)} 1[d₁ + d₂ ≥ w] ≤ 2H(2/a)^{1/2} e^{32κ̄ − μ₂ w/4} e^{−(μ₂/2)(d₁ + d₂)}.

(I): |𝖠(P)R_P − 𝖠(ref)R_ref| ≤ |𝖠(P) − 𝖠(ref)||R_P| + |𝖠(ref)||R_P − R_ref| (entrywise in (x,y),(y,z)). By (I-1)(d) and Lemma A.2(a), the first is ≤ η(2/a)^{1/2} e^{−μ₀d₁ − μ₁d₂}. For the second, Lemma A.2(c) with ‖𝖠(P) − 𝖠(ref)‖_{μ₀/2} ≤ η V(μ₀/2) gives |R_P − R_ref|(y,z) ≤ ½(2/a)^{3/2}V(μ₁/2)² V(μ₀/2) η e^{−(μ₁/2)d₂}. So |(I)/σ| ≤ η H₁ e^{−μ₂(d₁ + d₂)} with H₁ := (2/a)^{1/2} + ½ H (2/a)^{3/2} V(μ₁/2)² V(μ₀/2). And |σ| ≤ 1 if both D are empty, while otherwise d₁ + d₂ ≥ w and |σ| ≤ e^{32κ̄}e^{(μ₂/4)(d₁+d₂)}; in both cases |σ| e^{−(μ₂/2)(d₁+d₂)} ≤ max{1, e^{32κ̄ − μ₂w/4}} ≤ 1 by (A.4) (M ≥ 128κ̄/μ₂ gives μ₂M/4 ≥ 32κ̄). So |(I)| ≤ η H₁ e^{−(μ₂/2)(d₁ + d₂)}.

Summation: Σ_y e^{−(μ₂/2)(d₁ + d₂)} ≤ e^{−(μ₂/4) d(x,z)} Σ_y e^{−(μ₂/4) d(x,y)} ≤ V(μ₂/4) e^{−(μ₂/4) d(x,z)} (triangle inequality). The Schur test in (x, z) gives another factor V(μ₂/4). Therefore

  ‖Γ(s; P) − Γ₀‖ ≤ V(μ₂/4)² [2H(2/a)^{1/2} e^{32κ̄ − μ₂M/4} + H₁ η].  (A.6)

*Step 6.* Add (A.5) and (A.6). Since e^{16κ̄ − μ₀M/4} ≤ e^{32κ̄ − μ₂M/4} (μ₂ ≤ μ₀, κ̄ ≥ 0), (iii) holds with

  H₀ := (4/(3a))² V(μ₀/2)(1 + 2H) + V(μ₂/4)² (2H(2/a)^{1/2} + H₁).  (A.8)

All constants depend on (a, H, μ₀, n_c) only. □ [P]

*Remarks.* (1) SA's coefficient ratio τ (SA L14196–14199: "A complex coefficient ratio $\tau$ changes the structure to $(\tau^{-1}C,\tau^{1/2}\Gamma)$ and adds $C|\tau-1|$ to the perturbation") adds C_{K₀}|τ − 1| to (iii), with C_{K₀} = 2K₀² for |τ − 1| ≤ ½ (|τ^{−1} − 1| ≤ 2|τ − 1| and |τ^{1/2} − 1| ≤ |τ − 1|, multiplied by ‖C‖, ‖Γ‖ ≤ 2K₀). (2) The proof uses (I-1) only at the actual pair P and at ref; no global gap off Z₀ is used, as SA L14202–14205 requires ("Far from $Z_0$ the mutilated form need not have a gap"). The inverse root is taken of the full 𝖠(P), which is accretive everywhere by (I-1)(b); the mutilation enters only through the weights s^D. (3) The decoupling of Definition A.3 is a choice we make. Any decoupling with Lemma A.4(a)–(b), and with the identities (d)–(e), gives the same proposition. SA's own "decoupled inverse-root series" (SA L14161–14170) is not written out in SA; we do not claim to have reproduced it.

### A.5 The UM budget fixed before κ̄ and M

**Theorem A.6 (UM envelope).** Fix B₀ := 1. Let K₀, H₀, μ₂ be as in Proposition A.5 and put A := A_{K₀}, ε₀ := ε₀(K₀), ρ₀ := ρ₀(K₀) (I-2), P := C_p (the rooted-sum constant of (UM13), geometric), c_m the coordinate count of (UM5), and D := A c_m L⁴. Choose

  W₀ := min{ 1/(3PL⁴(1 + Ac_m)), ρ₀/(2P) },  (A.9)

independent of M and κ̄. For any κ̄ ≥ 1 and any M satisfying (A.4) and

  H₀ e^{32κ̄ − μ₂M/4} ≤ ½ min{ε₀, 1/(3DM⁴)},  (A.10)

put γ_tilt := min{2/(3DM⁴), ρ₀}, and suppose the radii, current and coefficient ratio obey

  H₀ η(P) + 2K₀²|τ − 1| ≤ ½ min{ε₀, 1/(3DM⁴)}.  (A.11)

Then (UM4)–(UM6) hold with K = K₀ and ε ≤ min{ε₀, 1/(3DM⁴)} on the discs |s_Δ| < R_s = e^{κ̄}; (UM14) holds; and

  C₀^UM ≤ 1.

Consequently Θ := C_h(1 + K_*) with K_* = 2 + c_ℓΛ (UM18 with C₀ replaced by its bound 1) satisfies (UM20) unchanged, and depends on κ (through Λ = (1 + 4β_s)κ + g_*) and on fixed geometry only.

*Proof.* (UM4)–(UM5): Proposition A.5 with Remark (1) and (A.10)–(A.11) gives ε ≤ min{ε₀, 1/(3DM⁴)} and K ≤ K₀, uniformly on |s_Δ| ≤ e^{κ̄} ⊃ |s_Δ| < R_s. (UM6) is (I-2) at K₀. (UM14): P W₀ M^{−4} ≤ P W₀ ≤ ρ₀/2 and γ_tilt/2 ≤ ρ₀/2. By (A.0),

  C₀^UM = P L⁴ W₀ (1 + A c_m) + D M⁴ (ε + γ_tilt/2) ≤ 1/3 + 1/3 + 1/3 = 1.

Every later use of C₀ in SA L14583–14660 is through the upper bound e^{(C₀ + K_*)N} in (UM16) → (UM20), so replacing C₀ by 1 in (UM18) keeps (UM19)–(UM24) valid. □ [P]

*Costs downstream (stated, not hidden).* (1) The failed-test tail is p = e^{−γ_tilt 𝔟²/2} per bond with γ_tilt ≍ (LM)^{−4}; the condition p_⋆ = n_b p ≤ e^{−Θ}/4 of SA L14795–14799 becomes 𝔟² ≥ (2/γ_tilt)(Θ + log(4c_b(LM)⁴)) (`um-envelope.md` (3)). The cutoff 𝔟 is the regular-gas field box in scaled units, of size ≍ δ_k/g_k = (A₁/A₀)p₀(g_k) → ∞ as g → 0; so this is a ceiling on g after M. (2) The insertion amplitude a_* = min{W₀/2, (4e^Θ A_a)^{−1}}, A_a = 2c_f L⁴ S_{σ₀}/W₀ (SA L14793–14797), is smaller than for a free W₀. The potentials enter the gas through first differences in the fluctuation field (SA L19517: "with $C\mathsf{B}\mathsf{s}_k\le1$"), of size O(𝗌_k) → 0; so a ≤ a_* is again a ceiling on g. Nothing chosen before M changes.

### A.6 The order lemma

SA L19445–19468 states the principle; we state and prove it as a lemma so that it can be formalised.

**Definition.** A *choice scheme* is a finite list of constants c₁ ≺ c₂ ≺ … ≺ c_n, each with a kind: *up* (range [m_i, ∞) or the powers of L above m_i), *down* (range (0, m_i]), *determined* (a fixed function of c₁, …, c_{i−1}), or *window* (an interval with endpoints functions of earlier constants). A *condition* is a predicate on finitely many constants. A condition is *assigned* to the last constant c_i it involves; it is *admissible at c_i* if, for every value of c₁, …, c_{i−1} satisfying the conditions assigned to them, the set of values of c_i satisfying it is: a final segment of the range (a floor) if c_i is up; an initial segment (0, t] with t > 0 (a ceiling) if c_i is down; a subinterval of the window whose intersection with the other subintervals assigned to c_i is nonempty (window endpoints) if c_i is a window; and all of them hold automatically if c_i is determined.

**Lemma A.8 (simultaneous choice).** If every condition of a choice scheme is admissible at the constant it is assigned to, there are values of c₁, …, c_n satisfying all conditions simultaneously. Moreover, any values of c₁, …, c_i satisfying the conditions assigned to them extend to a full solution.

*Proof.* Induction on i. Given c₁, …, c_{i−1} satisfying their assigned conditions, the conditions assigned to c_i are finitely many floors (whose intersection is a final segment: take the maximum threshold), or finitely many ceilings (intersection (0, min t] with min t > 0), or window conditions with nonempty intersection by admissibility, or automatic. So a value of c_i exists. Conditions assigned to later constants do not involve c_i's admissibility. □ [P]

A condition that involves a number *returned* by an estimate is admissible only if that number is a function of constants strictly before the one it bounds (SA L19485, "Any such number must be fixed before the constant that it bounds").

### A.7 The order of IN1

**Theorem A.7 (one order).** The rows of `c4-order.md`, modified as follows, form a choice scheme in which every condition used in IN1 and in its imports (as stated in Section 1) is admissible.

*Modifications.*

- **Row 8 (the flagged input) is replaced by row 8′**: after row 7, fix B₀ = 1; compute μ′, H′, μ₁, μ₂, K₀, H₀ from (a, H, μ₀, n_c) (Proposition A.5); compute A = A_{K₀}, ε₀ = ε₀(K₀), ρ₀ = ρ₀(K₀) (I-2); fix W₀ by (A.9). All are *determined* constants. Then κ (up), then Θ := C_h^UM(1 + 2 + c_ℓ((1 + 4β_s)κ + g_*)) (determined), then λ = λ_V in the window (8) of `um-envelope.md`:

  λ₀ + σ₀ + Θ/L ≤ λ < κ/(2C_h^WF) − ε_rate.  (A.12)

- **Row 9**: κ̄ (up) with the floors κ̄ ≫ Lκ (SA L19477), β_br = κ̄ − 1 > C_h^WF(λ + ε_rate), β_br > C_geo λ + 2, log(e^{κ̄} − 1) ≥ Θ, and κ̄ ≥ 1.
- **Row 12**: M (up, powers of L) receives the floors (A.4) and (A.10) in addition to its listed floors.
- **Row 14**: γ_tilt := min{2/(3DM⁴), ρ₀} (determined, after M). The UM entries W₀, C₀^UM ≤ 1 are no longer chosen here.
- **Row 16**: the radii (down) receive the ceilings H₀ H_p(M)(a₀ + a₁ + j₀) ≤ ¼ min{ε₀, 1/(3DM⁴)} and CLMa₀ ≤ a_w of (I-1).
- **Rows 21–22**: the coupling ceiling γ (down) receives: 2K₀² sup_{x≥γ^{−2}}|1 − τ(x)| ≤ ¼ min{ε₀, 1/(3DM⁴)} (via the tube, |1 − τ_k| ≤ c(log θ_k)^{−C}); the failed-test floor 𝔟² ≥ (2/γ_tilt)(Θ + log(4c_b(LM)⁴)) (via 𝔟 ≍ p₀(g)); a ≤ a_*; and the ceilings of Parts B–C listed in A.8 below.

*Proof of admissibility for the conditions in the former cycle.*

1. (A.9) and row 8′: determined from rows 1–7 only. The inputs (a, b, H, μ₀) are row 7 package constants (A2 gap and A3 kernel constants, `c4-order.md` row 7), fixed before κ. P, c_m, C_h^UM, c_ℓ, g_* are geometric (row 2a). So Θ is a function of κ and earlier constants: determined.
2. (A.12): a window on λ. Its nonemptiness is the floor on κ: κ(1/(2C_h^WF) − C_h^UM c_ℓ(1 + 4β_s)/L) > λ₀ + σ₀ + ε_rate + C_h^UM(3 + c_ℓ g_*)/L, which is a floor on κ (up) because row 3's floor L > 4C_h^WF C_h^UM c_ℓ(1 + 4β_s) makes the bracket positive (`c4-order.md` hand check "WF's output rate must also feed UM"; `um-envelope.md` §5 (8)).
3. log(e^{κ̄} − 1) ≥ Θ: a floor on κ̄ (up) after κ, since Θ is determined by then. The other row 9 floors are floors on κ̄ after L, κ, λ.
4. (A.4) and (A.10): floors on M after κ̄. Indeed M ↦ 2HV(μ₀/2)e^{16κ̄ − μ₀M/4} and M ↦ M⁴ e^{−μ₂M/4} decrease to 0 for M ≥ 16/μ₂; precisely, e^{μ₂M/4} ≥ (μ₂M/4)⁵/5! gives M⁴e^{−μ₂M/4} ≤ 5!(4/μ₂)⁵/M → 0 (`um-envelope.md` §5 (9)). So each holds from some power of L on.
5. γ_tilt: determined after M.
6. Radius ceilings: ceilings (down) after M, since H_p(M), D, M are fixed by then.
7. The ceilings on γ: each has the supremum form sup_{x ≥ γ^{−2}} h(x) ≤ c with h → 0 as x → ∞ (SA L19485: "a condition imposed on all couplings of all runs reduces to a single ceiling on $\gamma$"), so each is a ceiling on γ (down) after all fixed constants.

No condition in the list bounds a constant chosen before one of its inputs. In particular C₀^UM, which was the returned number in the cycle, is now bounded by the determined constant 1 fixed at row 8′, before κ, κ̄ and M; the actual C₀^UM is never used as an input to a choice. □ [P]

*The cuts already in the sources (kept).* (1) The flow cycle γ → (λ_♯, B_♯) → γ is cut by the weak triple (λ̲, c₅, B̄) fixed before γ (SA L19485, "The cycle that is cut"; `c4-order.md` row 3a); Part B uses exactly this. (2) The 2.8 order conflict r → d₀ → r is removed by placing d₀ = 5 + log_L C₄^GC after r and B̄ (`c4-order.md` row 19, `gates/geo5c-gate.md`). (3) The radius window (α₁ = t, α₀ = t/(2D_r), D_r > CM, then t small) is nonempty (`c4-order.md` hand check).

### A.8 Conditions contributed by Parts B–D

Each is admissible at the named constant; the proofs are in the parts.

| Condition | Assigned to | Kind | Where used |
|---|---|---|---|
| ς(γ) := sup_{x≥γ^{−2}}[C_f x^{−1/2}(log x)^{𝔭₀} + C_v x^{−p_R}] ≤ min{c₀/4, 1} | γ | ceiling | B.1 |
| 𝔭₀ ≥ 6r + 1; 2𝔭₁ − Cr > 𝔭₀; q > 𝔭₀ + 2r; κ₀ > 8 | exponents | window / floors in row 2 | C.5, C.9, B.1 |
| (C.5): c_G p₀(g)² ≥ 2p₀(g) + C_cnt 𝖳 r̂ and ½p₀(g) ≥ C_cnt 𝖳 r̂ for all g ≤ γ, r̂ = 2Cc₁M⁴Ř⁵ + κ₁ | γ (after M, c₁, κ₁) | ceiling | C.5, C.7 |
| x_{t−1}ε_t²·c ≥ c_G p₀(g_t)² and x_{t−1}e_* ≥ p₀(g_t)² | γ | ceiling | C.3 |
| (2 C_sup A₀/C₀) L² sup_{x≥γ^{−2}} (log x)^{2r+𝔭₀−q} < 1 | γ | ceiling | C.9 |
| B̄γ² ≤ 1 and e^{2qc₅γ²/log γ^{−2}} ≤ 2 (so w_{n,j} ≤ 2(n + 2 − j)); ρ_R(γ) ≤ 1 | γ | ceiling | D.1–D.3 |
| N_⋆ := E₀ Σ_ν 𝖿_ν + 1 (determined); C_E(|1−τ_k| + δ_k + 𝗌_k N_⋆ + e^{−cp₀²}) ≤ 1 | γ (after N_⋆) | ceiling | D.3–D.4 |
| E₀ := E_𝖭 + 1 | determined after E_𝖭 | determined | D.4 |
| κ₁ ≥ κ_ent + 1 | κ₁ (row 9) | floor | C.12 |
| c₁ := c_r + C_Ψ + C₅ + C₇ + c_e + 2 (determined; c_r the reserve weight) | before γ | determined | C.8 |


---

## Part B. The flow (E1) and first passage

The flow statements are arithmetic once the increments are formed. The only analytic inputs are (I-4) and the error bounds of (I-5). SA gives the same arithmetic at SA L20760–20800, (RF23)–(RF25); Y3 obtains first passage "from a coefficient-determined recursion" (Y3 L64306–64316; its `sec:canonical-flow` was not read here). We write it out because it fixes the order in which the class and the flow are proved (Theorem D.8 is a joint induction).

**Setting.** A run is a sequence x₀ = β, x_k = x_{k−1} − b_k, where b_k = b[Ê^{(k)}] is the coefficient produced by the step at the pair (θ_{k−1}, x_{k−1}) with θ = x (I-5). Write s_k := k c₀ − Σ_{l≤k} b_l⁰ and e_l := f_l + q_l, so b_l = b_l⁰ + e_l.

**Lemma B.0 (telescoping).** Put s_k := k c₀ − (A_k − A₀). Then |s_k| ≤ 2c₂, |s_i − s_j| ≤ 2c₂ for all i, j, and for i ≤ j, Σ_{i<l≤j} b_l⁰ = (j − i)c₀ + s_i − s_j.

*Proof.* By (I-4), Σ_{l≤k} b_l⁰ = A_k − A₀ = kc₀ − s_k. Since |A_k − kc₀| ≤ c₂ for every k ≥ 0 (including k = 0, |A₀| ≤ c₂), |s_k| ≤ 2c₂; and s_i − s_j = (A_j − jc₀) − (A_i − ic₀), so |s_i − s_j| ≤ 2c₂ = c₅. The identity is the difference of two partial sums. □ [P]

*Remark.* SA L20760 states: "Put \(s_k=kc_0-\sum_{l\le k}b_l^0\); then \(|s_k|\le c_2\)." Our s_k differs by A₀ and we use the bound 2c₂ only through differences, which is all (RF23) needs. The per-step increment law OL1(4) (|b_j⁰ − c₀| ≤ CL^{−σj}) is *not* needed for E1, first passage or the asymptotics: Lemma B.0 controls every sum that occurs. This removes ⟦open: OL-incr⟧ from IN1's path. (Where OL1(4) is read elsewhere — for instance in TP1's running normalisation — it stays an input there.)

**Theorem B.1 (E1).** Let γ satisfy ς(γ) ≤ min{c₀/4, 1} (A.8, first row), and put

  λ_♯ := c₀ − ς(γ) ≥ 3c₀/4,  B_♯ := c₀ + 2c₂ + ς(γ) ≤ C_β,  c₅ = 2c₂.

Suppose x₀, …, x_k are formed and x_l ≥ γ^{−2} for l < k. Then for i ≤ j ≤ k:

  λ_♯(j − i) − c₅ ≤ x_i − x_j ≤ B_♯(j − i).  (B.1)

In particular b_l ≤ B_♯ for each l, and the run (θ = x) satisfies the weak triple (F) with λ̲ = c₀/4 ≤ λ_♯ and B̄ = C_β + 1 ≥ B_♯. The increments b_l are the same on every admissible torus and for every unused finer cutoff.

*Proof.* x_i − x_j = Σ_{i<l≤j} b_l = (j − i)c₀ + s_i − s_j + Σ_{i<l≤j} e_l (Lemma B.0). By (I-5), |e_l| ≤ C_f x_{l−1}^{−1/2}(log x_{l−1})^{𝔭₀} + C_v x_{l−1}^{−p_R} ≤ ς(γ) because x_{l−1} ≥ γ^{−2} for l ≤ k. So

  x_i − x_j ≥ (j − i)(c₀ − ς) − 2c₂,  x_i − x_j ≤ (j − i)(c₀ + ς) + 2c₂ ≤ (j − i)(c₀ + 2c₂ + ς) for j > i,

and for j = i both sides of (B.1) hold trivially (0 ≥ −c₅, 0 ≤ 0). With j = i + 1 this gives b_{i+1} ≤ B_♯. The weak triple follows since c₀/4 ≤ λ_♯ and B_♯ ≤ c₀ + 2c₂ + 1 = C_β < B̄. The independence of torus and finer cutoff holds because b_l = b[Ê^{(l)}] is computed from the single family Ê^{(l)} on ℤ⁴ (clause (iii) and the ℤ⁴-family convention of SA L19410, part of (I-5)). □ [P]

*Order remark.* C_f and C_v are fixed before γ (they depend on the weak triple, not on γ; SA L20701–20703: "Constants are independent of the frame length, torus, cutoff and admitted parameter; the weak triple affects their threshold"). ς(γ) → 0 as γ → 0 since x^{−1/2}(log x)^{𝔭₀} → 0 and x^{−p_R} → 0. So the condition on γ is a ceiling (A.8). This is SA's cut of the flow cycle.

**Theorem B.2 (first passage).** Let h := g^{−2} with g ≤ γ, and β ≥ h + B_♯. Define K(β, g) := min{k ≥ 0 : x_k ≤ h + B_♯}. Then, assuming the class step (Theorem D.6) is available at every level k < K:
  (a) K(β, g) is finite, and (β − h)/B_♯ − 1 ≤ K ≤ 1 + (β − h − B_♯ + c₅)/λ_♯;
  (b) h < x_K ≤ h + B_♯;
  (c) the set {K(β, g) : β ≥ h + B_♯} is infinite, so 𝒲_K(g) := {β : K(β, g) = K} is nonempty for infinitely many K;
  (d) β / log(1/a_K) → 11N²/(12π²) as K → ∞, uniformly over β ∈ 𝒲_K(g), for fixed g.

*Proof.* Every x_l with l < K satisfies x_l > h + B_♯ ≥ γ^{−2}, so Theorem B.1 applies on [0, K] as long as the run is formed, which Theorem D.8 supplies level by level.
(a) If x_k > h + B_♯ for all k ≤ k₀, then by (B.1) h + B_♯ < x_{k₀} ≤ β − λ_♯k₀ + c₅, so k₀ < (β − h − B_♯ + c₅)/λ_♯. Hence K exists and K ≤ 1 + (β − h − B_♯ + c₅)/λ_♯. Also x_K ≥ x₀ − B_♯K = β − B_♯K by (B.1), and x_K ≤ h + B_♯, so K ≥ (β − h − B_♯)/B_♯ = (β − h)/B_♯ − 1.
(b) If K = 0 then β ≤ h + B_♯ ≤ β, so x₀ = h + B_♯ > h. If K ≥ 1, x_{K−1} > h + B_♯ and b_K ≤ B_♯ (Theorem B.1), so x_K = x_{K−1} − b_K > h.
(c) By (a), K(β, g) ≥ (β − h)/B_♯ − 1 → ∞ as β → ∞, and each K(β, g) is finite. A set of natural numbers that is unbounded is infinite.
(d) Let β ∈ 𝒲_K(g). From x_K = β − Kc₀ + s_K − Σ_{l≤K} e_l (Lemma B.0) and (b),

  |β − Kc₀| ≤ h + B_♯ + 2c₂ + Σ_{l≤K} |e_l|.

By (B.1) with j = K, x_{l−1} ≥ x_K + λ_♯(K − l + 1) − c₅ ≥ h + λ_♯(K − l + 1) − c₅. Put y_m := max{γ^{−2}, h + λ_♯m − c₅} for m = K − l + 1 ∈ {1, …, K}. The function u(x) := C_f x^{−1/2}(log x)^{𝔭₀} + C_v x^{−p_R} is eventually decreasing (for x ≥ x_u, a constant fixed with C_f, C_v; take γ^{−2} ≥ x_u, a further ceiling on γ). So

  Σ_{l≤K} |e_l| ≤ Σ_{m=1}^{K} u(y_m) ≤ Σ_{m=1}^{K} u(max{γ^{−2}, λ_♯m − c₅}).

For m ≥ m₀ := ⌈(γ^{−2} + c₅)/λ_♯⌉, u(λ_♯m − c₅) ≤ C(m)^{−1/2}(log m + C)^{𝔭₀} + C m^{−p_R}, and Σ_{m≤K} m^{−1/2}(log m + C)^{𝔭₀} ≤ C K^{1/2}(log K + C)^{𝔭₀} (compare with ∫₁^K t^{−1/2}(log t + C)^{𝔭₀} dt ≤ 2K^{1/2}(log K + C)^{𝔭₀}); Σ m^{−p_R} converges since p_R > 2. The first m₀ terms contribute at most m₀ ς(γ). Hence Σ_{l≤K}|e_l| = O_g(K^{1/2}(log K)^{𝔭₀} + 1) = o(K). Therefore |β/K − c₀| ≤ (h + B_♯ + 2c₂ + o(K))/K → 0 uniformly over 𝒲_K(g), and β/log(1/a_K) = β/(K log L) → c₀/log L = 11N²/(12π²). □ [P]

*Remark.* (d) uses only the telescoped one-loop value (I-4) and the error bounds; it does not use per-step convergence b_j⁰ → c₀. The constant 11N²/(12π²) = 11/(3π²) for N = 2 is the one-loop coefficient c₀/log L of OL1(3).

---

## Part C. The mass bound C3

### C.0 What C3 asks, and the objects

SA L4063–4074 (Obligation C3): "For each created large-field component $X$ at level $j$, we must prove a mass bound $\mathfrak M_j(X)\le \exp[-c p_0(g_j)-\kappa |X|_j]$ with the stated supremum over external complex data inside its internal integral when component majorants are multiplied. Here $p_0(g)=(\log g^{-2})^p$, and $\kappa$ exceeds the entropy rate of C2. The bound must include the Wilson factor actually available to pay for that component, all stored Jacobians and gauge factors, and the designated insertion weights. A failure of existence of a background … must also be covered. Drop-outs without their own Wilson factor need a separate bound after attachment to their carrying term."

SA's route is Lemma 2.5 (SA L17676–17693), Proposition 2.6 (SA L17719–17792) and Proposition 2.7 (SA L17794–17839), expanded at SA L18206–18876. We follow that route, prove every step that does not belong to another submanuscript, and name the inputs (I-6)–(I-12) that do.

**Objects (from LF1, SA (2a)–(2c)).** A *history* h of depth k records the regions Ω_j, Λ_j, the created cells, the marks (islands and drop-outs) and the operations R. A *component* u = (n(u), C(u)) is a component of the large-field region Z_{n(u)} of level n(u); |C(u)|_n is its number of level-n cells and #_n(C(u)) its number of level-n sites. The genealogy Gen(u_*) is the tree of u_* and its iterated predecessors (SA L17732). 𝗇_t^cr(u_*) is the number of created cells of level t in Gen(u_*), 𝗇_t^mk(u_*) the number of its marked components of level t other than u_*.

For a component X that has passed every test of the operation R of level i before its last decomposition 1 = χ_i + χ_i^c (healed, or an island), its operation is (SA L17794–17799)

  𝐓′_i(X)F(𝐩) = |W₄|^{−1} Σ_ω ∫ e^{Φ_ω(ξ;𝐩)} F μ_ω(dξ),

where ω runs over the local histories of X with a frame in W₄, ξ over the stored variables, μ_ω is a positive Borel measure (I-6), and 𝐩 over the pairs on X^~. Its **mass** is (SA L17259–17280, Theorem 2.1)

  𝖬(i, X) := |W₄|^{−1} Σ_ω e^{c 𝗏(ω)} ∫^* sup_{𝐩 ∈ U^c_i(X^~, α_{0,i}, α_{1,i})} |e^{Φ_ω(ξ;𝐩)}| μ_ω(dξ),  (C.0)

with the upper integral ∫^* (the infimum of the integrals of Borel majorants; SA L17825), and the weighted volume 𝗏(ω) = Σ_{u listed by ω} log x_{n(u)} #_{n(u)}(C(u)) (SA L17800–17801). Each local history ω splits as ω = (ω°, (ω_y)_y), an *outer record* ω° (the genealogy of X cut at its inner islands y = (m, Y), SA L17839 item (v)) and the local histories ω_y of the inner islands; correspondingly ξ = (ξ°, (ξ_y)_y) and μ_ω = μ° ⊗ ⊗_y μ_{ω_y}, with ξ_in := (ξ_y)_y, because the pieces have disjoint variables (I-6), (I-9). 𝗏 is additive: 𝗏(ω) = 𝗏°(ω°) + Σ_y 𝗏(ω_y). We write V°(ω°) := Σ_{u outer} (1 + log x_{n(u)}) #_{n(u)}(C(u)) ≥ 𝗏°(ω°), the log-weighted stored-site count of the outer record; V° ≥ 1 because X is nonempty.

### C.1 The averaging kernel in four dimensions

For a plaquette p′ = p_{μν}(y₁) of the level-(n+1) lattice and x ∈ B(y₁), let S_x(p′) = {p_{μν}(x + ie_μ + je_ν) : 0 ≤ i, j < L} and 𝖶(p′, p) := L^{−4} #{x ∈ B(y₁) : p ∈ S_x(p′)} (the four-dimensional form of Y3 (I-10-95), L6785, whose prefactor is L^{−3}).

**Lemma C.1 (kernel counts, d = 4).** (a) Σ_p 𝖶(p′, p) = L²; (b) Σ_{p′} 𝖶(p′, p) = L^{−2}; (c) ‖𝖶‖_{2→2} ≤ 1 and ‖𝖶‖_{1→1} ≤ L^{−2}; for a product 𝖶^{(l,m)} = 𝖶_{m−1}⋯𝖶_{l+1} of such kernels (identity if l = m − 1), ‖𝖶^{(l,m)}h‖_2 ≤ L^{−2(m−1−l)}‖h‖_1. (d) For t > l, a level-l plaquette lies in the cones 𝒩_l(p′) of at most 24 plaquettes p′ of level t, where 𝒩_l(p′) is the set of level-l plaquettes whose four corners lie in ∪_{y corner of p′} B^{t−l}(y).

*Proof.* (a) Σ_p 𝖶(p′, p) = L^{−4} Σ_{x∈B(y₁)} #S_x(p′) = L^{−4}·L⁴·L², since the L² plaquettes of S_x(p′) are distinct. (b) Fix p = p_{μν}(z) (a plaquette in a different plane is in no S_x(p′) of a μν-plaquette p′). For each (i, j) ∈ [0, L)², the point z − ie_μ − je_ν lies in exactly one block B(y₁) (the blocks partition the fine sites), and then p ∈ S_x(p′) for x = z − ie_μ − je_ν and p′ = p_{μν}(y₁); no other x ∈ B(y₁) works for this (i, j). So Σ_{p′} 𝖶(p′, p) = L^{−4}·L² = L^{−2}. (c) The Schur test: ‖𝖶‖_{2→2} ≤ (max row sum · max column sum)^{1/2} = 1, and ‖𝖶‖_{1→1} = max column sum = L^{−2}. For the product, ‖·‖_2 ≤ ‖·‖_1 and ‖𝖶^{(l,m)}‖_{1→1} ≤ L^{−2(m−1−l)}. (d) The base point of a level-l plaquette p lies in a unique level-t block B^{t−l}(y); if p ∈ 𝒩_l(p′), all corners of p, in particular its base point, lie in blocks of corners of p′, so y is a corner of p′. A level-t site is a corner of 4 plaquettes in each of the 6 coordinate planes: 24. □ [P]

*Cone recursion.* 𝒩_t(S) = S and 𝒩_l(S) = ∪_{p″ ∈ 𝒩_{l+1}(S)} 𝒩_l(p″) for l < t, where on the right the cones are one-step cones. Y3 proves this in three dimensions (Y3 L7915–7947: the cone of p′ is a box with 2r sites in the two plaquette directions and r sites in the remaining direction, r = L^{t−l}, and the coordinatewise choice q*_ρ = min{⌊s_ρ/L⌋, R_ρ − 2} for the plaquette directions, ⌊s_ρ/L⌋ otherwise). The proof is coordinatewise, so it holds verbatim in four dimensions with "remaining direction" replaced by "remaining two directions" (each treated by q*_ρ = ⌊s_ρ/L⌋). [P, by port]

### C.2 The energy of block averages in four dimensions

**Proposition C.2 (energy of averages, d = 4).** Assume (I-10) with constants (C^SO, ϖ′_L). Put

  e_L := min{(ϖ′_L)²/4, (108 C^SO)^{−2}},  e_* := e_L/2.

For every real configuration U (no regularity assumed), every t ≥ 1 and every set S of level-t plaquettes,

  Σ_{p ∈ 𝒩_0(S)} a_p(U) ≥ min{ (1/8) Σ_{p′∈S} |∂𝓜^tU(p′) − 1|², e_* },  (C.1)

with the convention that the first entry is +∞ if the regular branch of 𝓜^lU is unavailable at some plaquette of some 𝒩_l(S). If the left side is < e_*, the regular branch is available on every 𝒩_l(S), 0 ≤ l ≤ t, and max_{𝒩_l(S)} f_{𝓜^lU} ≤ 2(2Σ_{𝒩_0(S)}a_p(U))^{1/2}. The constants depend on L only, not on t.

*Proof.* Write f_l := f_{𝓜^lU}, E_l := Σ_{p∈𝒩_l(S)} f_l(p)², ϖ_l := max_{𝒩_l(S)} f_l ≤ E_l^{1/2}. Then E₀ = 2Σ_{𝒩_0(S)} a_p(U) (§1.1) and E_t = Σ_{p′∈S} f_t(p′)².

*One step on cones.* Let 0 ≤ l < t and suppose ϖ_l ≤ ϖ′_L. For p′ ∈ 𝒩_{l+1}(S), its one-step cone 𝒩_l(p′) ⊂ 𝒩_l(S) (cone recursion), so (I-10) applies on it and gives f_{l+1}(p′) ≤ (𝖶_l f_l)(p′) + r_l(p′) with r_l(p′) := C^SO ϖ_{l,p′}², ϖ_{l,p′} := max_{𝒩_l(p′)} f_l, and only p ∈ 𝒩_l(p′) ⊂ 𝒩_l(S) enter 𝖶_l f_l. By Lemma C.1(d) (applied one level up),

  ‖r_l‖_{ℓ¹(𝒩_{l+1}(S))} ≤ C^SO Σ_{p′} Σ_{p ∈ 𝒩_l(p′)} f_l(p)² ≤ 24 C^SO E_l.

*Iteration.* If ϖ_j ≤ ϖ′_L for all j < m, then, since all kernels are nonnegative, induction on m gives pointwise on 𝒩_m(S)

  f_m ≤ 𝖶^{(−1,m)} f₀ + Σ_{l<m} 𝖶^{(l,m)} r_l,

where 𝖶^{(−1,m)} := 𝖶_{m−1}⋯𝖶₀. Taking ℓ²(𝒩_m(S)) norms with Lemma C.1(c):

  E_m^{1/2} ≤ E₀^{1/2} + Σ_{l<m} L^{−2(m−1−l)} · 24 C^SO E_l.  (C.2)

*Bootstrap.* Suppose E₀ ≤ e_L. We show E_m ≤ 4E₀ for 0 ≤ m ≤ t by induction. m = 0 is trivial. If E_l ≤ 4E₀ for all l < m, then ϖ_l ≤ 2E₀^{1/2} ≤ ϖ′_L for l < m (first entry of e_L), so (C.2) applies:

  E_m^{1/2} ≤ E₀^{1/2} + 96 C^SO E₀ Σ_{j≥0} L^{−2j} ≤ E₀^{1/2} + 108 C^SO E₀ ≤ 2E₀^{1/2}

(L ≥ 3 gives Σ_j L^{−2j} ≤ 9/8; the last step uses E₀^{1/2} ≤ (108C^SO)^{−1}). So E_m ≤ 4E₀. In particular all ϖ_l ≤ 2E₀^{1/2} ≤ ϖ′_L, which keeps every intervening plaquette in the chart of (I-10), so the regular branch is available.

*Conclusion.* If E₀ ≤ e_L, then Σ_S f_t² = E_t ≤ 4E₀ = 8Σ_{𝒩_0(S)}a_p, which is (C.1) with the first entry. If E₀ > e_L, then Σ_{𝒩_0(S)}a_p = E₀/2 > e_L/2 = e_*. In either case (C.1) holds. If Σ a_p < e_*, then E₀ < e_L and the bootstrap gives the last assertion. □ [P]

**Where four dimensions differ from YM3 (exactly).** Y3 Proposition II-6-57 (Y3 L7893–7911) has L^t Σ a_p on the left, and its proof uses ‖𝖶f‖ ≤ √L‖f‖ (row sums L², column sums L^{−1} in three dimensions; Y3 Lemma I-10-96) and the multiplicative form E_l^{1/2} ≤ L^{l/2} exp(C_en Σ_{j<l} ϖ_j) E₀^{1/2} (Y3 (II-6-82), L8008–8011), closed by the decay ϖ_j ≤ (2𝖾_L)^{1/2} L^{−(t−j)/2} (Y3 L8013–8024). In four dimensions ‖𝖶‖_{2→2} ≤ 1: the ℓ² curvature energy is preserved under averaging (the action is scale invariant; this is the same fact that makes the coupling marginal). The intermediate curvatures then do not decay, Σ_j ϖ_j grows like t E₀^{1/2}, and the multiplicative form would give a factor exp(C t E₀^{1/2}), not uniform in t. The four-dimensional proof above replaces it by the additive form (C.2), in which the quadratic errors are measured in ℓ¹ and carried by ‖𝖶‖_{1→1} ≤ L^{−2}; this is SA's route (SA L18217–18257, (average-one-step)–(average-bootstrap)), written here with explicit constants. The left side of (C.1) carries no L^t: in four dimensions a failed test at level t is paid by the bare action at the *same* coupling scale, which is why the creation gain is c x_{t−1} ε_t² = c p₀(g_t)² with no volume factor.

### C.3 Certificates for failed tests

**Lemma C.3 (one factor per creation; SA Lemma 2.5).** Assume (I-9), (I-10), (I-11)(a)–(d) and the tube |x_j − θ_j| ≤ θ_j/4. There are c_G > 0 (depending on L, A₁/A₀, κ_pos, c_lin) and a ceiling on γ such that, on the support of a term, at step t, for every real configuration U whose averages are the stored ones:
  (i) if the plaquette test fails at □, the share of □ satisfies x_{t−1} Σ_{p ∈ share} a_p(U) ≥ 2c_G p₀(g_t)²;
  (ii) if the approximate fluctuation test fails at 𝔠, x_{t−1}(A_{𝔠^~}(U) + GF_{t−1}(𝔠^~; V_{t−1})) ≥ 2c_G p₀(g_t)²;
  (iii) if a fluctuation, collar or rim test fails, the stored Gaussian exponent satisfies ½⟨𝒜^s, Δ𝒜^s⟩ ≥ 2c_G p₀(g_t)²;
  (iv) if a test of an operation R at level m fails inside a patch, the action outside the floor gives p₀(g_m) (this is (I-11)(d), recorded for the ledger).
These hold also where an object read by the test does not exist.

*Proof.* (i) By totality (I-6) the test is the indicator of the set where the localised background exists and its inequalities hold. By (I-11)(a) in contrapositive form, failure (including non-existence) implies f_{V_t}(p′) ≥ c_lin ε_t for some level-t plaquette p′ in the test neighbourhood S_□ of □. By (I-9)(2), V_t = 𝓜^tU on Γ_t for every U with the stored averages. Proposition C.2 with S = {p′} gives Σ_{𝒩_0(p′)} a_p(U) ≥ min{c_lin²ε_t²/8, e_*} = c_lin²ε_t²/8 once ε_t² ≤ 8e_*/c_lin², a ceiling on γ (ε_t → 0). 𝒩_0(p′) lies in the share of □ ((I-9)(1): the share contains the bare plaquettes within one cell of the failing cell, and 𝒩_0(p′) lies in the four level-t blocks at the corners of p′). Multiply by x_{t−1}: x_{t−1}ε_t² = (x_{t−1}/θ_t) p₀(g_t)². By the frame bound (F) with j − i = 1, θ_{t−1} ≥ θ_t − c₅; with the tube, x_{t−1} ≥ ¾θ_{t−1} ≥ ¾(θ_t − c₅) ≥ θ_t/2 once γ^{−2} ≥ 3c₅. So the left side of (i) is ≥ (c_lin²/16) p₀(g_t)².
(ii) By (I-11)(b), failure (including non-existence) gives A + GF ≥ c δ_{t−1}² for every compatible U. With the tube, x_{t−1} ≥ ¾θ_{t−1}, and θ_{t−1}δ_{t−1}² = (A₁/A₀)² p₀(g_{t−1})², so x_{t−1}δ_{t−1}² ≥ ¾(A₁/A₀)² p₀(g_{t−1})²; and p₀(g_{t−1}) ≥ ½p₀(g_t) for γ small (log x_{t−1} ≥ log(x_t − c₅) by (B.1)).
(iii) By (I-11)(c), failure forces a stored scaled coordinate of size ≥ cδ_{t−1}/g_{t−1} = c(A₁/A₀)p₀(g_{t−1}), and the form gives ½⟨𝒜^s, Δ𝒜^s⟩ ≥ ½κ_pos c²(A₁/A₀)² p₀(g_{t−1})². Where the tested logarithm is undefined, (I-11)(c) states the same implication (SA L18323–18327: a small integration variable would put the logarithm in its chart and make the test pass).
Take 2c_G as the minimum of the three constants (with the factor ¼ from p₀(g_{t−1}) ≥ ½p₀(g_t)). (iv) is (I-11)(d). □ [P]

The energy pieces used by distinct certificates lie in disjoint shares, or overlap boundedly on the cell neighbourhoods fixed in (2a) (SA L18329–18332); the bounded overlap is absorbed in c_G before gains are summed. [import (I-9)]

### C.4 Local prices

**Lemma C.4 (gauge normaliser on SU(2)).** For ε ≤ 1 and θε² ≥ 1,

  z(θ, ε) := ∫_{SU(2)} 1{|u − 1| < ε} e^{−θ(1 − ½tr u)} du  satisfies  (8/(3π³)) e^{−1/2} θ^{−3/2} ≤ z(θ, ε) ≤ C_z θ^{−3/2},

with C_z = (2/π)(√π/4)(π²/2)^{3/2}; and ∫_{SU(2)} e^{−(θ/2)(1 − ½tr u)} du ≤ 2^{3/2} C_z θ^{−3/2} ≤ C′ z(θ, ε) with C′ = 2^{3/2}C_z (8/(3π³))^{−1} e^{1/2}.

*Proof.* Write u = cos φ + i sin φ (n·σ), φ ∈ [0, π], n ∈ S². The normalised Haar measure has the class-function density (2/π) sin²φ dφ (it integrates to 1). Here ½tr u = cos φ and the operator norm |u − 1| = |e^{iφ} − 1| = 2 sin(φ/2). *Upper bound.* sin²φ ≤ φ² and 1 − cos φ = 2sin²(φ/2) ≥ 2(φ/π)² for φ ∈ [0, π] (since sin x ≥ 2x/π on [0, π/2]). So z ≤ (2/π)∫₀^∞ φ² e^{−2θφ²/π²} dφ = (2/π)(√π/4)(π²/(2θ))^{3/2} = C_z θ^{−3/2}, using ∫₀^∞ φ² e^{−αφ²}dφ = (√π/4)α^{−3/2}. The same computation with θ/2 gives the second claim's first inequality. *Lower bound.* On 0 ≤ φ < θ^{−1/2} (≤ ε ≤ 1): 2sin(φ/2) ≤ φ < ε, sin φ ≥ 2φ/π, and θ(1 − cos φ) ≤ θφ²/2 ≤ ½. So z ≥ (2/π)∫₀^{θ^{−1/2}} (4φ²/π²) e^{−1/2} dφ = (8/(3π³)) e^{−1/2} θ^{−3/2}. □ [P]

This is SA's (gauge-normalizer) display (SA L18736–18748), with explicit constants. It shows that a gauge-fixing factor, integrated against half of its own exponent, costs a bounded factor per site against its normaliser.

**Lemma C.5 (stored Gaussian blocks in a triangular chart).** Let ξ° = (b₁, …, b_n) be stored free blocks, b_j ∈ ℝ^{d_j}, and suppose that for each j and each value of the later blocks and of ξ_in, the map b_j ↦ A_j(b_j; b_{j+1}, …, b_n; ξ_in) ∈ ℝ^{d_j} is injective, C¹, with |det ∂_{b_j}A_j|^{−1} ≤ J₀^{d_j} ((I-11)(e)). Let κ_pos > 0. Then for every ξ_in,

  ∫ exp(−(κ_pos/2) Σ_j |A_j|²) db₁ ⋯ db_n ≤ J₀^{Σd_j} (2π/κ_pos)^{½Σd_j}.

*Proof.* Integrate b₁ first at fixed later variables: the change-of-variables inequality for an injective C¹ map, ∫ F(A₁(b₁)) db₁ = ∫_{A₁(ℝ^{d₁})} F(A) |det ∂A₁|^{−1}∘A₁^{−1} dA ≤ J₀^{d₁}∫_{ℝ^{d₁}} F(A) dA for F ≥ 0, gives the factor J₀^{d₁}(2π/κ_pos)^{d₁/2}, independent of the later variables. Repeat for b₂, …, b_n (Tonelli). □ [P]

With the coercivity (I-11)(c), the complete kept forms dominate (κ_pos/2)Σ|A_j|² after half of the exponent is reserved for payment; the number of coordinates Σ d_j is at most C times the stored site count. Together with Lemma C.4 and the rescaling costs (C log x_j per level-j site, SA L18754–18755), this gives the envelope bound

  sup_{ξ_in} ∫ g_{ω°}(ξ°; ξ_in) dμ°(ξ°) ≤ e^{C₅ V°(ω°)},  (C.3)

for the Borel envelope g_{ω°} defined in C.6 below. [P, given (I-11)(c),(e)]

### C.5 The count and the ledger

**Proposition C.6 (the count; SA Proposition 2.6, global form).** Assume (I-7)(G1)–(G4). Let r̂₁ ≥ r̂₂ ≥ … ≥ 0 be non-increasing costs and 𝖳_t = CŘ_t (non-increasing in t, since Ř_t is built from the running minimum of θ; SA L19410). Then for every history and component u_*,

  Σ_{u ∈ Gen(u_*)} r̂_{n(u)} |C(u)|_{n(u)} ≤ C_cnt [Σ_t 𝗇_t^cr(u_*) 𝖳_t r̂_t + Σ_t 𝗇_t^mk(u_*) 𝖳_t r̂_t],  (C.4)

with C_cnt depending on C_g, s₀ only.

*Proof.* (1) *Reduction to occupied and light counts.* By (G1), |C(u)| ≤ C_g(1 + 𝗈(u)). A member is *light* if 𝗈(u) ≤ C_g and heavy otherwise (the same constant C_g, enlarged once, serves in (G1)–(G3)); for a heavy member 1 + 𝗈(u) ≤ 2𝗈(u). Hence Σ_u r̂_{n(u)}|C(u)| ≤ C_g Σ_n r̂_n (2𝗈_n + (C_g + 1) l_n).
(2) *Contraction.* Multiply (G2) by r̂_n and use r̂_n ≤ r̂_{n−s₀}, r̂_n ≤ r̂_t for t ≤ n:

  Σ_n r̂_n 𝗈_n ≤ ½ Σ_n r̂_{n−s₀}𝗈_{n−s₀} + C_g Σ_n r̂_{n−s₀} l_{n−s₀} + s₀ Σ_t r̂_t 𝗇_t^cr.

All sums are finite (finitely many levels). The first sum on the right is at most ½ of the left side; subtract: Σ_n r̂_n 𝗈_n ≤ 2C_g Σ_n r̂_n l_n + 2s₀ Σ_t r̂_t 𝗇_t^cr.
(3) *Stretches.* Call a member an *event* if it contains a created cell of its own level, or comes immediately after a marked component, or has at least two predecessors (a joining). A non-event has exactly one predecessor: it has at most one (else it is a joining), and at least one (a member with none is a leaf, which contains a created cell of its own level by (G4) and so is an event). Every member has exactly one successor in Gen(u_*) unless it is u_*. For a member u, follow predecessors from u through non-events; since levels decrease, this stops at an event σ(u). The *stretch* of an event v is {u : σ(u) = v}; it is a chain (successors are unique), it starts at v, and the stretches partition Gen(u_*). By (G3) a stretch starting at level t has at most 𝖳_t light members, all at levels ≥ t, so Σ_n r̂_n l_n ≤ Σ_{stretches σ} 𝖳_{t(σ)} r̂_{t(σ)} (r̂ non-increasing).
(4) *Paying for events (injective assignment).* Assign to each event v a created cell or a mark: if v contains a created cell of its own level, that cell; else if v comes after a mark, that mark; else v is a joining: select at every member with predecessors one *first predecessor*; from a predecessor of v other than the first, follow first predecessors down to a leaf λ(v), and assign a created cell of λ(v) (one exists by (G4)). *Injectivity on joinings:* from λ(v) walk up through successors; every step up to the chosen predecessor of v enters a member from its first predecessor, and the step into v does not. So v is the first member on the upward path from λ(v) entered from a non-first predecessor, and λ determines v. Hence each created cell is assigned at most twice (once as an own-level cell, once as a leaf cell), each mark at most once (a mark has one successor). Each assigned cell or mark lies at a level ≤ t(σ) of the stretch it pays for, where 𝖳 r̂ is no smaller. So Σ_σ 𝖳_{t(σ)}r̂_{t(σ)} ≤ 2Σ_t 𝗇_t^cr 𝖳_t r̂_t + Σ_t 𝗇_t^mk 𝖳_t r̂_t.
Combining (1)–(4): Σ_u r̂|C(u)| ≤ C_g Σ_n r̂_n(2𝗈_n + (C_g + 1)l_n) ≤ C_g(5C_g + 1) Σ_n r̂_n l_n + 4C_g s₀ Σ_t r̂_t 𝗇_t^cr, which gives (C.4) with C_cnt := 2C_g(5C_g + 1) + 4C_g s₀ (using 𝖳_t ≥ 1). □ [P]

**Corollary C.7 (ledger and reserve).** Let 𝗀_t := c_G p₀(g_t)² (creation gain), 𝗆_t := ½p₀(g_t) (mark gain), 𝗉_t := p₀(g_t) (reserved number), and costs r^c_n := c₁(1 + log x_n)(MŘ_n)⁴ + κ₁ for constants c₁, κ₁. If, for all levels n,

  𝗀_n ≥ 2𝗉_n + C_cnt 𝖳_n r̂_n,  𝗆_n ≥ C_cnt 𝖳_n r̂_n,  with r̂_n := 2C c₁ M⁴Ř_n⁵ + κ₁,  (C.5)

then for every history and component u_*,

  𝖥(u_*) := Σ_t 𝗀_t 𝗇_t^cr + Σ_t 𝗆_t 𝗇_t^mk − Σ_{u∈Gen(u_*)} r^c_{n(u)} |C(u)|_{n(u)} ≥ 2Σ_t 𝗉_t 𝗇_t^cr ≥ 2(1 − c′/2) p₀(g_{n(u_*)}).

*Proof.* log x_n ≤ (log x_n)^r ≤ Ř_n ≤ CŘ_n for r ≥ 1, so 1 + log x_n ≤ 2CŘ_n and r^c_n ≤ r̂_n; r̂ is non-increasing because Ř is. By (C.4), 𝖥 ≥ Σ_t (𝗀_t − C_cnt𝖳_t r̂_t)𝗇_t^cr + Σ_t(𝗆_t − C_cnt𝖳_t r̂_t)𝗇_t^mk ≥ 2Σ_t 𝗉_t 𝗇_t^cr. Gen(u_*) has a leaf, which contains a created cell at a level t ≤ n(u_*) (G4). By (B.1), x_t ≥ x_{n(u_*)} − c₅, so log x_t ≥ log x_{n(u_*)} − 2c₅γ² and 𝗉_t ≥ (1 − c′/2)𝗉_{n(u_*)} for γ small. □ [P]

*Order of (C.5).* With 𝖳_n r̂_n ≤ C c₁M⁴ (log x_n)^{6r}·L⁶ + Cκ₁L(log x_n)^r, 𝗆_n = ½A₀(log x_n)^{𝔭₀} and 𝗀_n − 2𝗉_n = c_G A₀²(log x_n)^{2𝔭₀} − 2A₀(log x_n)^{𝔭₀}, (C.5) holds for all x_n ≥ γ^{−2} once 𝔭₀ > 6r (row 2: 𝔭₀ ≥ 6r + 1) and γ is below a ceiling depending on M, κ₁, c₁, C_cnt, c_G, A₀. This is SA L17757–17762 ("Since $\mathfrak{p}_0\ge6r+1$, the quantity $p_0(g_n)=A_0(\log x_n)^{\mathfrak{p}_0}$ exceeds this cost"), and the same exponent condition as Y3 L63118–63121 ("$\mathfrak p_0\ge6r+1$").

### C.6 The envelope of a component

Fix X passed at level i and an outer record ω°. On the support of the term, write the integrand with (I-8):

  |e^{Φ_ω(ξ;𝐩)}| = e^{Φ°_ω(ξ)} e^{Re Ψ_ω(ξ;𝐩)} ≤ e^{Φ°_ω(ξ)} e^{C_Ψ V°(ω°)}  for all 𝐩 ∈ U^c_i(X^~, α_{0,i}, α_{1,i}),  (C.6)

and e^{Φ°_ω(ξ)} = e^{−A_cr(ξ)} Π_{(t,D) outer} 𝗐_{t,D}(ξ) · χ_ω(ξ) · Π_y e^{Φ_{ω_y}(ξ_y; 𝐩_y(ξ))}, where A_cr is the Wilson action over the outer shares (I-9), χ_ω the product of the test indicators recorded by ω° (all of them, including the failed ones, except the last decomposition of X itself, which is not part of its mass), and 𝐩_y(ξ) the real pair at which the outer term reads the inner island y. By (I-8) for y at its own level m and the reproduction Lemma C.11 below, 𝐩_y(ξ) ∈ U^c_m(Y^~, α_{0,m}, α_{1,m}); hence

  |e^{Φ_{ω_y}(ξ_y; 𝐩_y(ξ))}| ≤ m_{ω_y}(ξ_y) := sup_{𝐩 ∈ U^c_m(Y^~,α_{0,m},α_{1,m})} |e^{Φ_{ω_y}(ξ_y;𝐩)}|.  (C.7)

*Splitting.* Split A_cr = ½A_cr + ½A_cr and each gauge-fixing exponent and Gaussian exponent in 𝗐_{t,D} in halves (SA L17702, item (3)). On the support of χ_ω, by Lemma C.3, the first halves of the shares, gauge exponents and stored Gaussian exponents of the outer pieces are at least Σ_e Γ_e(ω°), where e runs over the outer created cells, with Γ_e := c_G p₀(g_t)² (half of the 2c_G p₀(g_t)² of Lemma C.3(i)–(iii)), and over the outer renewed marks, with Γ_e := ½p₀(g_t) (half of Lemma C.3(iv)); the root's own mark is excluded. The second halves, with the normalisers of the gauge factors, the pivot Jacobians and the conditional Gaussian normalisations, define

  g_{ω°}(ξ°; ξ_in) := e^{−½A_cr(ξ)} Π_{(t,D) outer} 𝗐^{(1/2)}_{t,D}(ξ),

a nonnegative Borel function of ξ (the indicator χ_ω is dropped after the gains are taken, which only enlarges it). By Lemmas C.4 and C.5 and the rescaling costs, (C.3) holds: sup_{ξ_in} ∫ g_{ω°}(ξ°; ξ_in) dμ°(ξ°) ≤ e^{C₅V°(ω°)}. [The bound on the Wilson half: ½A_cr ≥ 0 on the shares and every other plaquette contributes ≥ 0 (I-9)(1), so e^{−½A_cr} ≤ 1 and it is kept only as part of the envelope.] Collecting, for every ξ on the support and every 𝐩:

  |e^{Φ_ω(ξ;𝐩)}| ≤ e^{C_Ψ V° + C₇V° − Σ_e Γ_e(ω°)} g_{ω°}(ξ°; ξ_in) Π_y m_{ω_y}(ξ_y),  (C.8)

where C₇V° absorbs the costs per site of the normalisations that are not integrated in (C.3) (each O(1 + log x_j) per level-j site; SA L18754–18755). The right side does not depend on 𝐩; so (C.8) bounds the supremum over 𝐩 *pointwise in ξ*, before any integration. [P, given (I-8), (I-9), (I-11)]

### C.7 The mass induction

**Theorem C.8 (mass of passed components).** Assume (I-6)–(I-12) and the order of Part A. For every small c′ > 0 and every c ≥ 0 in the weight e^{c𝗏}, there is a ceiling on γ (depending on c, c′) such that for every history and every component X that has passed every test of R at a level i ≤ k (healed, or an island),

  𝖬(i, X) ≤ e^{−(2 − c′) p₀(g_i) − κ₁ |X|_i}.  (C.9)

*Proof.* Induction on the nesting depth of inner islands (the maximal length of a chain X ⊋ Y₁ ⊋ Y₂ ⊋ … of islands). At depth 0 the product over inner islands is empty.

*Step 1 (Borel majorants).* Fix η > 0. For each inner island y and each ω_y, by the definition of the upper integral choose a Borel function m̃_{ω_y} ≥ m_{ω_y} with ∫ m̃_{ω_y} dμ_{ω_y} ≤ ∫^* m_{ω_y} dμ_{ω_y} + η_{ω_y}, with Σ over all inner records of η_{ω_y} e^{c𝗏(ω_y)} ≤ η (finitely many records in finite volume). No measurable maximiser of the supremum is selected, and no supremum is moved through an integral (SA L18829–18846).

*Step 2 (Tonelli).* Off the support of χ_ω the integrand vanishes; on it, by (C.8), sup_𝐩 |e^{Φ_ω(ξ;𝐩)}| ≤ G_ω(ξ) := e^{(C_Ψ + C₇)V° − ΣΓ_e} g_{ω°}(ξ°; ξ_in) Π_y m̃_{ω_y}(ξ_y), a nonnegative Borel function. Hence ∫^* sup_𝐩 |e^{Φ_ω}| dμ_ω ≤ ∫ G_ω dμ_ω, and by Tonelli for μ_ω = μ° ⊗ ⊗_y μ_{ω_y}, integrating ξ° first at fixed ξ_in and using (C.3),

  ∫ G_ω dμ_ω ≤ e^{(C_Ψ + C₅ + C₇)V° − ΣΓ_e} Π_y ∫ m̃_{ω_y} dμ_{ω_y}.

*Step 3 (sum over inner records).* The operation of an inner island y enters the outer integrand with its own frame normalisation |W₄|^{−1} (SA L18797–18804: the factor Π_y m^ℝ_{ω′_y}(ξ′_y)/|W₄| of the complete envelope). So the inner frame sums appear as |W₄|^{−1}Σ_{ω_y}. Multiply by e^{c𝗏(ω)} = e^{c𝗏°(ω°)} Π_y e^{c𝗏(ω_y)} (additivity) and sum over the inner records at fixed ω°. The inner sums separate:

  Π_y [ |W₄|^{−1} Σ_{ω_y} e^{c𝗏(ω_y)} ∫ m̃_{ω_y} dμ_{ω_y} ] ≤ Π_y (𝖬(m_y, Y) + η) ≤ (1 + η)^{#inner},

by the induction hypothesis 𝖬(m_y, Y) ≤ 1 (C.9 at smaller depth). The outer frame sum |W₄|^{−1}Σ_{r∈W₄} is an average of quantities bounded uniformly in r, so it is bounded by that uniform bound. Let η → 0 at the end.

*Step 4 (reserve).* Apply Corollary C.7 to the outer genealogy (cut at the inner islands) with c₁ := c + C_Ψ + C₅ + C₇ + c_e + 2. The cut leaves are inner islands, whose O(1) cells count as created cells of their level (SA L17839, item (v)): the factor χ^c_m of the new field on Y less a margin is present in the outer term, so a step test χ_m fails at V_m(ξ), and Lemma C.3(i) extracts 𝗀_m from the core Wilson factor of X on plaquettes used by no other gain. Then Σ_e Γ_e = Σ_t 𝗀_t 𝗇_t^cr + Σ_t 𝗆_t 𝗇_t^mk = 𝖥 + Σ_u r^c_{n(u)}|C(u)|. Since the sites of a level-n cell number at most (MŘ_n)⁴, V° ≤ Σ_u (1 + log x_{n(u)})(MŘ_{n(u)})⁴|C(u)|, and the root u_* = X has |C(u_*)| = |X|_i. Hence

  Σ_e Γ_e ≥ 2(1 − c′/2)p₀(g_i) + c₁ V°(ω°) + κ₁|X|_i.

*Step 5 (entropy).* Combining Steps 2–4 (and e^{c𝗏°} ≤ e^{cV°}), the contribution of each outer record ω° to 𝖬(i, X) is at most e^{(c + C_Ψ + C₅ + C₇)V° − ΣΓ_e} ≤ e^{−(2−c′)p₀(g_i) − κ₁|X|_i − (c_e + 2)V°(ω°)}. By (G5) the number of outer records with n ≤ V° < n + 1 is at most e^{c_e(n+1)}, so

  Σ_{ω°} e^{−(c_e+2)V°(ω°)} ≤ Σ_{n≥1} e^{c_e(n+1) − (c_e+2)n} = e^{c_e} Σ_{n≥1} e^{−2n} ≤ e^{c_e}/(e² − 1).

Absorb the constant e^{c_e}/(e² − 1) into e^{(c′/2)p₀(g_i)}, a further ceiling on γ, and rename c′. This gives (C.9). The constants are independent of i, k, the history, the torus and the cutoff. □ [P, given the imports]

*What the induction does not use.* It does not use any bound on the exponent Φ°_ω itself, which is large and negative (SA L19424, clause (vi)), and it uses no inductive hypothesis at drop-outs (SA L18872–18875). Restricting the supremum to real pairs returns the real form of the induction hypothesis.

### C.8 Drop-outs

**Theorem C.9 (drop-outs).** Let X be a drop-out created at level i, carried by a term of level k ≥ i. Define its mass with the supremum over *evaluations at ξ* (SA L17834–17838 item (iv): real U on X, compatible with ξ, regular layer by layer as on the supports, at which each test listed by ω except the one whose failure made X a drop-out takes its recorded value, with each inner island's pair in its own domain), and over the one-sided free parameters: the Wilson weight υ ≥ c x_t on Z_t, kept forms ≥ c, Jacobians ≤ C. Then, with the Wilson weight of the carrying term over X^+ counted with the operation,

  𝖬_do(i, X) := |W₄|^{−1} Σ_ω e^{c𝗏(ω)} ∫^* sup_{evaluations at ξ} e^{−A(υ1_X, U)} (kept factors) μ_ω(dξ) ≤ e^{−(2−c′)p₀(g_i) − κ₁|X|_i}.

*Proof.* The envelope (C.8) was built from: Lemma C.3, which holds for *every* real U with the stored averages (Proposition C.2 has no regularity hypothesis, and (I-11)(b)–(c) are stated for all compatible U and all backgrounds); the kept forms and Jacobians only through their one-sided bounds (I-11)(c),(e); and the inner islands through (C.7), whose pairs lie in their own domains by the fourth property of an evaluation. With υ ≥ cx_t in place of x_t, Lemma C.3's gains are multiplied by c, which is absorbed in c_G. So (C.8) holds at every evaluation, with a right side that depends on ξ only; it therefore bounds the fibre supremum pointwise, and Steps 1–5 of Theorem C.8 apply verbatim. The test whose failure made X a drop-out is not used: its gain p₀(g_i) is reserved for the renewed wait and is spent when X occurs as a mark in a later component (Corollary C.7, the 𝗉_t 𝗇^mk term). □ [P, given the imports]

*Why the fibre, not a product set.* SA L17838 gives the toy case Φ = −T(1 − cos p) with the test |ξ| ≥ ε: over the graph p = ξ the mass is e^{−cTε²}, over a product set it is ≈ 1. Our proof uses the fibre only through Lemma C.3's validity at every compatible configuration, which is exactly what Proposition C.2 supplies.

### C.9 Reproduction at later levels

**Lemma C.10 (radii dominate support bounds).** Assume q > 𝔭₀ + 2r. There is a ceiling on γ such that for every frame and every j,

  C_sup Ř_j² ε_j < α_{0,j}.  (C.10)

*Proof.* Ř_j ≤ L(log min_{i≤j}θ_i)^r ≤ L(log θ_j)^r, because the running minimum is ≤ θ_j and Ř_j is the least power of L above (log min θ)^r. So C_sup Ř_j² ε_j / α_{0,j} ≤ C_sup L² (log θ_j)^{2r} · A₀θ_j^{−1/2}(log θ_j)^{𝔭₀} / (C₀θ_j^{−1/2}(log θ_j)^q) = (C_sup A₀ L²/C₀)(log θ_j)^{2r + 𝔭₀ − q}. The exponent is negative and log θ_j ≥ log γ^{−2}, so the ratio is < 1 once (C_sup A₀L²/C₀)(log γ^{−2})^{2r+𝔭₀−q} < 1, a ceiling on γ after L, A₀, C₀, C_sup. □ [P]

(SA L17829–17831 states (C.10) with "the quotient is a negative power of $\log x_j$, since $q>\mathfrak{p}_0+2r$".)

**Lemma C.11 (the fixed set contains every later argument).** Let X be a component passed at level i (or an inner island read by an outer term). For every term of level k ≥ i in which X occurs, and every point of its support, the pair (U_k, J(U_k))|_{X^~} lies in U^c_i(X^~, α_{0,i}, α_{1,i}). Consequently the mass of X seen at level k is at most 𝖬(i, X), and a step 𝐑𝐓 returns the mass bound with unchanged constants.

*Proof.* U^c_i(X^~, α_{0,i}, α_{1,i}) is defined layer by layer: on Ω_j ∖ Ω_{j+1} the pair must satisfy |∂𝐔 − 1| < α_{0,j}η_j² and |𝐉| < α_{0,j} (and the α₁ conditions on the fluctuation side, which are void at a real background pair with A′ = 0). By (I-12), on the supports |∂U_k − 1| < C_sup Ř_j² ε_j η_j² and |J(U_k)| < C_sup Ř_j²ε_j on that layer, with no loss in the age k − j. By Lemma C.10 these are < α_{0,j}η_j² and < α_{0,j}. So the pair lies in the set. The mass at level k is an upper integral of a supremum over a subset of the set used in 𝖬(i, X), with the same integrand; monotonicity of sup and of ∫^* gives the inequality. □ [P, given (I-12)]

### C.10 C3 in the catalogue's form

**Corollary C.12 (C3).** Assume the imports and the order. Choose κ₁ ≥ κ_ent + 1, where κ_ent is the entropy rate of the rooted connected cell sets of C2 (the number of connected sets of n cells containing a given cell is ≤ e^{κ_ent n}). Then:
  (a) for each created large-field component X at level j that has passed the tests of an R-operation (healed or island), 𝔐_j(X) := 𝖬(j, X) ≤ exp[−(2 − c′)p₀(g_j) − κ₁|X|_j] ≤ exp[−c p₀(g_j) − κ|X|_j] with c = 1 and κ = κ₁ > κ_ent;
  (b) the supremum over external complex data stands inside the internal integral (definition (C.0)), so majorants of distinct components multiply under Tonelli (Step 2 of Theorem C.8);
  (c) the bound includes the Wilson factor of the component's own shares, all stored Jacobians and gauge factors (through (C.3)), and the insertion weight e^{c𝗏} for every fixed c ≥ 0 chosen before γ (in particular the reserve constant c_r of SA (2e)(vi));
  (d) failure of existence of a background is covered, because every certificate of Lemma C.3 is a contrapositive statement about the total test indicator (I-6);
  (e) drop-outs, which have no Wilson factor of their own, obey the same bound after attachment to the carrying term (Theorem C.9);
  (f) the bound reproduces itself at every later level with unchanged constants (Lemma C.11).

*Proof.* (a) is Theorem C.8 with c′ ≤ 1. The rest has been proved in the places named. □ [P, given the imports]

### C.11 Components on which no R has acted, and the label sum

**Proposition C.13 (SA Proposition 2.7(b)–(c)).** (a) For a single history and a component Z of Z_k on which no R has acted, for every value of the exterior variables, ‖𝐓_k(Z)[χ_{k,𝒮} e^{−A(x_k(·),U_k)}]‖ ≤ Π_{created cells (t,𝔠) ⊂ Z} e^{−c_G p₀(g_t)²} · exp[C Σ_{t≤k} #_t(Z_t ∩ Z)]. (b) In the sum over labels, with the costs paid by Corollary C.7, every component C of Z_k keeps the factor exp[−c p₀(g_k) − κ₁ #_k(C)].

*Proof.* (a) Lemma C.3 on the support of the recorded failed tests, the halving of exponents, and Lemmas C.4–C.5 for the remaining halves, exactly as in C.6 but without inner islands and with fixed exterior variables (so no supremum is needed). (b) Apply Corollary C.7 to the genealogy of C with κ₁ added at the root, as in Step 4 of Theorem C.8; marked components inside contribute their masses ≤ 1 (Theorem C.8, C.9); the per-site factor e^{−κ₁#_k(C)} is obtained by adding κ₁(MŘ_k)⁴ per cell at the root, a cost covered by (C.5) after lowering γ. Since d_k(C) ≤ #_k(C), this contains e^{−κ₁ d_k(C)} (SA L17814–17820). □ [P, given the imports]

---

## Part D. The class and the closed induction (C4)

### D.1 The class 𝔆_k(θ)

We adopt SA's class (SA L19410–19425) with one change of wording and one added clause, both stated.

Let θ = (θ₀, …, θ_k) be a frame (§1.1). Every level-j choice that depends on the coupling (thresholds ε_j, δ_j, δ′_j, radii α_{ι,j}, the scaling 𝒜_j = θ_j^{−1/2}𝒜_j^s, the gauge-fixing weight, the Gaussian forms of the stages of 𝐑, the reference laws) is made with θ_j; the cube size and the waiting depth Ř_j = N_j are made with min_{i≤j}θ_i (SA L19410). So tests, regions, histories, analyticity domains and the measures of the integral operations depend on θ only, not on the density. This breaks the circle "regions depend on couplings, couplings on activities, activities on regions" (SA L19410).

An element of 𝔆_k(θ) is a presentation, an array specified simultaneously on every admissible torus and cutoff,

  𝔓 = ((x_j); (E^{(j)}, Ê^{(j)}, b_j); (R^{(j)}, R̂^{(j)}); (B^{(j)}_𝒮(X)); (Φ_ω))_{j≤k},  b_j = x_{j−1} − x_j = b[Ê^{(j)}],

whose density ρ[𝔓] has the form of SA Theorem 2.1 (SA L17259–17274), satisfying:

- (i) *tube*: |z_j| ≤ 𝗍_j ≤ c θ_j (log θ_j)^{−C}, z_j = θ_j − x_j, and |z_j| α_{0,j} δ_j ≤ c (log θ_j)^{−c};
- (ii) *bounds*: ‖E^{(j)}‖_{j,κ} ≤ E₀, ‖R^{(j)}‖_{j,κ} ≤ g_j^{κ₀}, |B^{(j)}(X, ·)| ≤ 𝖡 e^{−κ d^♮_j(𝒮; X)}, with analyticity, reality, gauge invariance, splitting independence, and the background triple (U, 0, J(U)) in each domain when the tests take the value 1;
- (ii′) *structure of the regular terms* (added as a separate clause; SA states it in the text after the clauses, L19426–19432): each regular member satisfies the hypotheses of the pointed extraction OL1(1) (Ward identities, hypercubic covariance, response hypotheses), so that its own extracted coefficient b_j and its own tent action remove its marginal part, and the regular terms gain the forgetting weight 𝖿_{n+1−j} ≈ (n+1−j)^C L^{−c(n+1−j)} when evaluated at level n;
- (iii) *identification*: E^{(j)} is the family produced from the earlier entries by the small-field step at (θ_{j−1}, x_{j−1}), on the whole lattice;
- (iv) *lattice covariance*, including unit translations of the pointed totals;
- (v) *coherence* (locality in the history, translation covariance, independence of the torus);
- (vi) *islands*: μ_ω positive Borel, Φ_ω Borel in ξ, analytic in 𝐩, real at real pairs, gauge invariant pointwise; the **mass bound** 𝖬(i, X) ≤ e^{−(2−c′)p₀(g_i) − κ₁|X|_i} with reserve weight e^{c_r 𝗏}, and the oscillation bound of (2d), at the level of creation;
- (vii) *positivity*: each term with its stored variables is a nonnegative measure.

*Why (ii′) is a clause, not a consequence.* SA L19426–19432 shows that the bounds (ii) alone do not give a class preserved by the step: the tent activities 𝖰_z = c α_{0,j}^{−2} A(h_z^{(j)}, ·) have norm ≤ 1 and sum to c α_{0,j}^{−2}A(U) = c θ_j(log θ_j)^{−2q}A(U), a marginal action term; arrays obeying (ii) can add at least this much at every level with no age decay. Our clause (ii′) names the structural hypothesis that excludes this. It is supplied by OL1(1) (B2, [SS]) and NL1, and is part of (I-5).

### D.2 The input uniformity

**Lemma D.1 (radius ratio).** Let w_{n,j} := (α_{0,n}/α_{0,j})² = (θ_j/θ_n)(log θ_n/log θ_j)^{2q}, the square of the ratio of the radius at which step n + 1 evaluates a level-j term to the radius at which it was created (SA L19502–19506). If θ is a frame with θ_i ≥ γ^{−2}, B̄γ² ≤ 1 and exp(2q c₅ γ²/log γ^{−2}) ≤ 2, then w_{n,j} ≤ 2(n + 2 − j) for j ≤ n.

*Proof.* By (F) with (i, j) ↦ (j, n): θ_j − θ_n ≤ B̄(n − j), so θ_j/θ_n ≤ 1 + B̄(n − j)/θ_n ≤ 1 + (n − j) (θ_n ≥ γ^{−2}, B̄γ² ≤ 1). Also θ_j − θ_n ≥ λ̲(n − j) − c₅ ≥ −c₅, so θ_n ≤ θ_j + c₅ and log θ_n ≤ log θ_j + c₅/θ_j, whence (log θ_n/log θ_j)^{2q} ≤ (1 + c₅/(θ_j log θ_j))^{2q} ≤ exp(2qc₅γ²/log γ^{−2}) ≤ 2. Multiply. □ [P]

(SA L19509: "The two factors in the approximation above are never unfavourable at the same time"; the proof is the two frame bounds, as written.)

**Lemma D.2 (remainder sum).** If κ₀ > 8, γ ≤ 1, γ^{−2} ≥ 2c₅ and θ is a frame with all θ_i ≥ γ^{−2}, then for every n,

  Σ_{j≤n} w_{n,j} g_j^{κ₀} ≤ ρ_R(γ) := 2^{1+κ₀/2} Σ_{m≥0} (m + 2)(γ^{−2} + λ̲m)^{−κ₀/2},

and ρ_R(γ) → 0 as γ → 0.

*Proof.* With m = n − j, θ_j ≥ θ_n + λ̲m − c₅ ≥ γ^{−2} − c₅ + λ̲m ≥ ½(γ^{−2} + λ̲m) (γ^{−2} ≥ 2c₅; and θ_j ≥ γ^{−2} anyway). So g_j^{κ₀} = θ_j^{−κ₀/2} ≤ 2^{κ₀/2}(γ^{−2} + λ̲m)^{−κ₀/2}, and w_{n,j} ≤ 2(m + 2) by Lemma D.1. The series converges because κ₀/2 > 2: (m + 2)(γ^{−2} + λ̲m)^{−κ₀/2} ≤ (m+2)(λ̲ m)^{−κ₀/2} for m ≥ 1. For γ ≤ 1 each term is at most (m + 2)(1 + λ̲m)^{−κ₀/2}, a γ-independent summable sequence, and each term tends to 0 as γ → 0; by dominated convergence ρ_R(γ) → 0. □ [P]

**Lemma D.3 (input of the next step).** Put N_⋆ := E₀ Σ_{ν≥1} 𝖿_ν + 1 (finite: 𝖿_ν ≈ ν^C L^{−cν}). If 𝔓 ∈ 𝔆_n(θ) and ρ_R(γ) ≤ 1, then

  Σ_{j≤n} 𝖿_{n+1−j} ‖E^{(j)}‖_{j,κ} + Σ_{j≤n} w_{n,j}‖R^{(j)}‖_{j,κ} ≤ N_⋆,  (D.3)

uniformly in n and in the frame. This is "everything that the small-field step requires of its input" (SA L19509).

*Proof.* The first sum is ≤ E₀Σ_ν 𝖿_ν by clause (ii); the second is ≤ ρ_R(γ) ≤ 1 by clause (ii) and Lemma D.2. □ [P]

**Lemma D.4 (the regular bound returns without a circle).** Put E₀ := E_𝖭 + 1. If γ is below the ceiling C_E sup_{x≥γ^{−2}}(|1 − τ(x)| + δ(x) + 𝗌(x)N_⋆ + e^{−cp₀(x^{−1/2})²}) ≤ 1, then the step's output satisfies ‖E^{(k+1)}‖ ≤ E₀.

*Proof.* (I-5) gives ‖E^{(k+1)}‖ ≤ E_𝖭 + C_E(|1 − τ_k| + δ_k + 𝗌_kN_⋆ + e^{−cp₀(g_k)²}), with C_E independent of E₀ and N_⋆. In the tube |1 − τ_k| = |z_k|/θ_k ≤ c(log θ_k)^{−C}; δ_k, 𝗌_k and e^{−cp₀²} tend to 0 with θ_k ≥ γ^{−2}. The order is: E_𝖭 (from the Gaussian normaliser, fixed before γ) → E₀ (determined) → N_⋆ (determined) → ceiling on γ. □ [P]

(SA L19513–19515: "so $E_0$ is determined by the one-loop normaliser alone, and $C$ depends neither on $E_0$ nor on $N_\star$".)

**Lemma D.5 (boundary terms).** 𝖡 := the maximum of the origin bounds of (I-5); each origin bound is independent of 𝖡, because data bounded by 𝖡 enter the step only (a) through differences in the fluctuation field, with C𝖡𝗌_k ≤ 1; (b) through stage collar differences, each switched block contributing a negative power of log θ_k; (c) as undifferenced level-j functions spread over cŘ_kL^{k−j} cubes, with 𝖡e^{−cŘ_k} ≤ 1; (d) inside an enlarged component, through the volume bound C Σ_j #_j(Z_j ∩ X), whose constant is chosen after 𝖡 and paid by the ledger (SA L19515–19521). Each of (a)–(c) is a ceiling on γ after 𝖡; (d) is a cost per site added to c₁ in Corollary C.7, chosen after 𝖡 and before γ. □ [P, as an order statement; the four entry routes are (I-5)]

### D.3 The step theorem

**Theorem D.6 (C4: the step preserves the class; SA Theorem 2.11).** Assume the imports (I-1)–(I-14) and the order of Part A. Suppose
  (1) 𝔓 ∈ 𝔆_k(θ);
  (2) θ_{k+1} prolongs the frame (θ₀, …, θ_{k+1} is a frame);
  (3) all g_j ≤ γ;
  (4) the next weight x_{k+1} := x_k − b[Ê^{(k+1)}] lies in the tube, where Ê^{(k+1)} is formed first at (θ_k, x_k) (its formation uses no level-(k+1) choice, (I-5)).
Then each move of step k + 1 is defined; 𝐑𝐓ρ[𝔓] = ρ[𝔓′] separately for each standing part; 𝔓′ ∈ 𝔆_{k+1}(θ) with the same constants; 𝔓′ prolongs 𝔓; and an array is in 𝔆_{k+1} exactly when its cut at k is in 𝔆_k and it satisfies the level-(k+1) conditions. The tube hypothesis (4) is not returned.

*Proof.* We verify each clause at level k + 1; clauses at levels ≤ k are unchanged because carried terms are literally unchanged (same function, domain and tree length; SA L19523), and the bounds of a standing island refer to its creation level.
- *Definedness and identity.* By (I-5), (I-6) and hypothesis (4), each move is a specified exact operation; the small-field step is defined on its box because its input satisfies (D.3) (Lemma D.3) and its pairs lie in the admitted domains ((D4), part of (I-5)). The measure identity holds part by part by (I-6) and the standing-history kernel identity (SA L20726–20730).
- *(i)* is hypothesis (4) at k + 1.
- *(ii)* E^{(k+1)}: Lemma D.4. R^{(k+1)}: ‖R^{(k+1)}‖ ≤ g_{k+1}^{κ₀} by (I-5). B^{(k+1)}: Lemma D.5. Analyticity, reality, gauge invariance and splitting independence: (I-5).
- *(ii′), (iii)–(v)*: preserved by (I-5) (OL1(1) for the pointed members; identification by construction; covariance by (R-cov) and (R-inv) of NL1; coherence by the chart rule of (2a)).
- *(vi)*: for components that pass the tests of an R-operation at level k + 1, the mass bound is Theorem C.8 (healed, islands), with the reserve weight c = c_r; drop-outs obey Theorem C.9 (not a clause); for islands standing from earlier levels, Lemma C.11 shows the bound at the creation level still controls them. Borel, analytic, real and gauge-invariance properties: (I-6), (I-8).
- *(vii)*: (I-6).
The constants are those fixed by Part A; no clause returns a constant that an earlier choice used. The "exactly when" statement is the definition of the class by levelwise conditions. □ [P, given the imports]

**Lemma D.7 (base case).** The array with the single entry x₀ = β, |β − θ₀| ≤ 𝗍₀ ≤ cθ₀(log θ₀)^{−C}, belongs to 𝔆₀(θ).

*Proof.* (i) is the hypothesis. (ii), (ii′), (iii)–(v) are vacuous at level 0 (no regular, remainder or boundary terms; the density is Wilson's e^{−βΣa_p} with product Haar measure, which is gauge invariant, real, translation and lattice covariant, and the same function on every torus). (vi) is vacuous (no islands). (vii): the Wilson measure is a nonnegative measure. □ [P]

### D.4 The closed induction along the run, and IN1

**Theorem D.8 (joint induction for the actual run).** Let g ≤ γ, h = g^{−2}, β ≥ h + B_♯, and θ := x (the frame equal to the computed weights). Then for every k ≤ K(β, g) the presentation 𝔓_k = (𝐑𝐓)^k 𝔓₀ is defined, lies in 𝔆_k(x), and x₀, …, x_k satisfy (B.1).

*Proof.* Induction on k. k = 0: Lemma D.7 with θ₀ = x₀ = β (z₀ = 0); (B.1) is trivial. Step k → k + 1 for k < K: by the induction hypothesis 𝔓_k ∈ 𝔆_k(x) and (B.1) holds up to k; and x_l > h + B_♯ ≥ γ^{−2} for l ≤ k (definition of K). Form Ê^{(k+1)} at (x_k, x_k) by (I-5); this defines b_{k+1} and x_{k+1}. Theorem B.1 applied to x₀, …, x_{k+1} gives (B.1) up to k + 1 and the weak triple (F) for (x₀, …, x_{k+1}); x_{k+1} > h ≥ γ^{−2} by Theorem B.2(b) if k + 1 = K, and x_{k+1} > h + B_♯ if k + 1 < K. So θ_{k+1} := x_{k+1} prolongs the frame (hypothesis (2)); g_j ≤ γ (3); and z_{k+1} = 0 is in the tube (4). The cube sizes Ř_j, built from running minima, are non-increasing automatically. Theorem D.6 gives 𝔓_{k+1} ∈ 𝔆_{k+1}(x). □ [P, given the imports]

(For θ = x the deviation is 0, and the tube requirement reduces to the frame prolongation, which is the content of the flow inequalities — SA L19443, "For $\theta=x$ the deviation is $0$". For other frames — the reference line used by sources — the tube is supplied by the drift bound of SA (3c); that belongs to SC1.)

**Theorem IN1.** Assume the imports (I-1)–(I-14) and the order of Part A. Then:
1. *(C4)* The class 𝔆_k(θ) contains the bare measure (Lemma D.7) and is mapped into 𝔆_{k+1}(θ) by the exact step under the increment and tube conditions (Theorem D.6), with constants independent of k; its conclusions include the analytic polymer bounds (clause (ii)), C1 (clause (vii) and (I-6)), C3 (Corollary C.12), boundary bounds (Lemma D.5), covariance (clause (iv)), and, through (I-14), the stability floor.
2. *(Order)* All constants admit one simultaneous order (Theorem A.7, Lemma A.8); in particular the cycle κ̄ → M → C₀^UM → Θ → κ̄ is cut by Theorem A.6.
3. *(E1)* Theorem B.1 along the run (Theorem D.8).
4. *(First passage)* Theorem B.2.
5. *(C3)* Corollary C.12, Theorem C.9, Lemma C.11. □ [P, given the imports]

---

## Part E. Status, what is outstanding, and what changed

### E.1 Status of every statement in this draft

| Statement | Content | Status | Inputs |
|---|---|---|---|
| Lemma A.0 | volume sum | [P] | — |
| Lemma A.1 | Combes–Thomas for accretive matrices | [P] | — |
| Lemma A.2 | inverse-root kernel, symmetry, R² = B^{−1}, perturbation | [P] | — |
| Def. A.3, Lemma A.4 | path-cube decoupling; counts; Schur identity; wall factorisation | [P] | — |
| Prop. A.5 | uniform matrix envelope (`um-envelope.md` (6)–(7)) | [P] | (I-1) |
| Thm. A.6 | C₀^UM ≤ 1 fixed before κ̄, M | [P] | (I-1), (I-2), (I-3) |
| Lemma A.8 | simultaneous choice | [P] | — |
| Thm. A.7 | one order for IN1 and its imports | [P] | `c4-order.md` rows (as [P] there) |
| Lemma B.0, Thm. B.1 | telescoping; E1 | [P] | (I-4), (I-5) error bounds |
| Thm. B.2 | first passage, window, 𝒲_K ≠ ∅ infinitely often, β/log(1/a_K) → 11N²/(12π²) | [P] | B.1, D.8 |
| Lemma C.1 | 4D averaging kernel counts, cone multiplicity 24 | [P] | — |
| Cone recursion | port of Y3 L7915–7947 | [P, by port] | — |
| Prop. C.2 | 4D energy of block averages, no regularity, uniform in t | [P] | (I-10) |
| Lemma C.3 | certificates for failed tests (incl. non-existence) | [P] | (I-6), (I-9), (I-11) |
| Lemma C.4 | SU(2) gauge normaliser, explicit constants | [P] | — |
| Lemma C.5 | triangular Gaussian | [P] | (I-11)(c),(e) |
| Prop. C.6 | genealogy count (injective joining assignment) | [P] | (I-7)(G1)–(G4) |
| Cor. C.7 | ledger and reserve | [P] | C.6 |
| Thm. C.8 | mass of passed components, induction on island depth | [P] | (I-6)–(I-12) |
| Thm. C.9 | drop-outs over evaluation fibres | [P] | as C.8 |
| Lemma C.10 | C_sup Ř²ε < α₀ | [P] | order |
| Lemma C.11 | fixed set contains later arguments | [P] | (I-12) |
| Cor. C.12 | C3 in the catalogue's form | [P] | as C.8 |
| Prop. C.13 | unhealed components and the label sum | [P] | as C.8 |
| Lemmas D.1–D.5 | radius ratio, remainder sum, input uniformity, no circle for E₀ and 𝖡 | [P] | (I-5) |
| Thm. D.6 | step preserves the class (SA 2.11) | [P] | (I-1)–(I-14) |
| Lemma D.7 | base case | [P] | — |
| Thm. D.8, Thm. IN1 | joint induction along the run; IN1 | [P] | (I-1)–(I-14) |

**Inside IN1 nothing is outstanding.** Every step written here is proved (not checked). IN1 is therefore complete *as an implication from its imports*. It is not unconditional.

### E.2 The imports and their status

| Import | Owner | Status in `ym4-assembly.md` |
|---|---|---|
| (I-1) gap, norm, decay of 𝖠(P) | PR1(1)–(2) | real critical and complex single-layer [C]; layered stage pairs ⟦open: PR-lay⟧ |
| (I-2) local Gaussian comparison | SA L13904–14056 | [SP] |
| (I-3) UM machinery and structural identities | NL1(1) | deductions written in SA; identities [SS] |
| (I-4) OL1(2)–(3) | OL1 | (2) [C], (3) [P] |
| (I-5) the small-field step and (RF20) | NL1 with (D4) of ST1; OL1(1),(5) | [O] through ⟦open: D4⟧ |
| (I-6) exact operations | LF1(1) | [C] |
| (I-7) genealogy and entropy (G1)–(G5) | LF1(2) | GEO1–GEO6 [C]; (G1)–(G5) for actual histories [O] |
| (I-8) prepared structure | LF1(4) | [C] conditional; ⟦open: LF-2.8⟧ |
| (I-9) shares | LF1(1)/(2) | [SS] |
| (I-10) one-step averaging in d = 4 | BG1(1) | 3D proved (Y3 I-10-97); 4D [SS] |
| (I-11) other certificates | BG1(2), PR1(1), (2b) | (a) [C]; (b), (d) [SS]; (c) A2 [C], cut-form [SS]; (e) [C] |
| (I-12) support bounds | class/ST1 | [SS]; part of (D4) |
| (I-13) sources | SC1 | [O] |
| (I-14) 2.10, 2.13 | LF1(5)–(6) | [O] remaining items |

### E.3 The first outstanding statement on IN1's path

In the order in which IN1's proof reads its inputs, the first import that is open is (I-1) at the pairs where the UM gas is actually evaluated. Those are the pairs of the hereditary core of the ordinary step, which under (D4) include lifted and stage (layered) pairs. At those pairs (I-1)(b)–(d) is the layered complex comparison PR1(5), ⟦open: PR-lay⟧ of `ym4-assembly.md` (its line 187):

> On the full earlier-parameter and switch domains, along the stage path supplied by ST1, dist_∞(D_e(t), 𝒯_e^c) ≥ η_* and ‖∂_t F_a‖ ≤ C r_a^{lift} Σ_{l∈E_n} u_l √(1+|m−l|) e^{−D|m−l|}, D ≥ log 4. Its first missing piece is the uniform real target-datum admission and complex bound (8) of layered-a3 for the actual layered stage family.

This statement belongs to PR1/ST1, not to IN1. I did not attack it here: the brief for this draft is IN1, and the (D4) lanes own it (`library/layered-a3.md` rounds 2–4 were running at the time of the assembly). For single-layer complex pairs, (I-1) is [C], and with it Part A is unconditional on that class of pairs.

Two remarks on what IN1 needs from (I-1), which narrow the open statement:
1. Part A needs only (I-1)(b)–(d) *at the pair P itself and at its real reference (U, 0)*: a uniform gap a, entrywise exponential decay (H, μ₀), and an entrywise-decaying pair perturbation with *any* M-dependent prefactor H_p(M). It needs no gap of the mutilated form off Z₀, no global square root of a mutilated operator, and no bound uniform in M on the pair perturbation. So the layered statement that IN1 actually consumes is weaker than PR1(5) as written: a gap, an exponential kernel bound and a decaying perturbation bound for 𝖠(P) at layered stage pairs, with constants fixed before κ.
2. The constants (a, H, μ₀) must be fixed before κ. For the real critical and single-layer complex cases they are row-7 constants of `c4-order.md`. If the layered case could only be proved with constants depending on M or κ̄, the cycle would reappear (Θ would depend on them through K₀, A_{K₀}). This is the one way the cycle could come back; it is a requirement on PR-lay, recorded here so that the (D4) lanes prove the layered bounds with row-7 constants.

### E.4 The constants cycle: resolution and its costs

- **Resolution.** The cycle κ̄ → M → C₀^UM → Θ → κ̄ is not real. Proposition A.5 proves the matrix envelope that `um-envelope.md` §4 left open, from (I-1) alone, with constants (K₀, H₀, μ₂) depending on (a, H, μ₀, n_c). Theorem A.6 then fixes C₀^UM ≤ 1 before κ, κ̄ and M, and Theorem A.7 gives one order.
- **Source of the cut.** It is SA's sufficient condition (SA L14779–14788), made into a proof, and it is the cut Y3 makes in three dimensions (Y3 L63134–63137, L63190–63198, L63236–63247, L63446–63458), with (LM)³ replaced by (LM)⁴.
- **What changed in the order.** Row 8's flagged input is replaced by determined constants (row 8′). M gets two new floors (A.4), (A.10), both after κ̄. γ_tilt is determined after M. The radii get one new ceiling. The coupling ceiling gets the |1 − τ| ceiling, the failed-test cutoff floor 𝔟² ≥ C(LM)⁴(Θ + log(LM)), and a ≤ a_*.
- **Downstream costs.** (1) The regular gas's failed-bond gain per bond is weaker, e^{−c(LM)^{−4}𝔟²} instead of e^{−c𝔟²}; compensated by the ceiling on g (𝔟 ≍ p₀(g) → ∞). (2) The Gaussian budget W₀ is O(L^{−4}) instead of free; the insertion amplitude a_* shrinks accordingly, again compensated by the ceiling on g. (3) No constant chosen before M changes; no estimate in NL1 or LF1 changes form. (4) The new decoupling (Definition A.3) is a choice; NL1 must use it (or any decoupling with Lemma A.4(a)–(e)) in its structural identities.

### E.5 Two consequences for other submanuscripts

1. **OL1(4) is off IN1's path.** E1, first passage and the asymptotics need only the telescoped one-loop value OL1(3) (Lemma B.0). The increment law ⟦open: OL-incr⟧ is not read by IN1. (It may still be read by TP1's running normalisation F3; that is TP1's question.)
2. **The 4D energy of averages is written.** Proposition C.2 is the four-dimensional form of Y3 Proposition II-6-57, with explicit constants, from the one-step estimate (I-10). The four-dimensional port of the one-step estimate itself (Y3 Lemma I-10-97) remains BG1's item; the kernel counts it needs are Lemma C.1.

### E.6 Credits restated

The induction, the class, the frames, the weak-triple cut, the ledger, the fibred supremum and the mass induction are Sussman and Alpoge's (with Claude and Codex as authors of their text), built on Balaban's CMP 119 (Theorem 1, Corollary 3), CMP 122a and 122b (the ledger (1.79)–(1.81), (1.89); the operation R). The budget-first cut is the one their YM3 manuscript makes. The Combes–Thomas estimate is classical (Combes and Thomas, CMP 34 (1973)); its use for exponential decay of lattice resolvents is standard and also appears in Balaban's and Dimock's random-walk expansions. What is ours: the proof of the matrix envelope (Proposition A.5) through an explicit path-cube decoupling, the resulting unconditional order (Theorem A.7), the observation that OL1(4) is not on IN1's path, and the written four-dimensional energy-of-averages proof with constants.
