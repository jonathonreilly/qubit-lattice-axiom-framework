Reviewer model: claude-opus-5-5

# ALIGN2_55 — regularity of the hierarchical Coulomb-detail alignment Λ_HC, and whether (R2) on 𝒞_glob needs it

## PRE-STATED (written 2026-10-29T04:30Z, before any derivation in this file)

Role: worker (Opus 5.5). Write-set: this file and `checks/a2_55_*` only. No git. Read so far: the task brief (queue/align2.md),
REVIEW_BRIEF_55.md, ALIGN55.md in full (565 lines, ends "UTC end stamp (final): 2026-10-29T04:24:28Z"). The lead's mid-task message
(received 04:30Z) puts a new target first: decide whether OFFGLOB55's Theorem GP / Corollary GP-R2 / Proposition L2 take the alignment
off the critical path for (R2) on 𝒞_glob in the form BFT-5 clause (b)'s consumers need. CODEX_REVIEW_ALIGN.md exists on disk (seen
04:29Z); it is read before anything of ALIGN55 is built on, and nothing it refutes is used.

### Targets (in the order the lead set)
- T0. OFFGLOB55 first: does (R2) on 𝒞_glob, in the form BFT-5 clause (b)'s consumers use (weighted, transport-norm), follow from
  Theorem GP / Corollary GP-R2 or Proposition L2 without any alignment? If yes: what exactly closes NE/CONV and the σ-pair vs ALIGN55's
  pair. If no: the precise statement GP/L2 do not cover.
- T1. Rebuild the d = 4 lattice Green's-function bounds DET cites, from primitives, with explicit constants (or show which bound DET
  actually needs and prove that one).
- T2. Prove DET and HB with explicit k-, T-uniform constants, giving (P1′) with exponent θ.
- T3. Subdivision input: certify a scheme for every odd L ≥ 3 the lane uses, or show L = 3 suffices for the whole proof.
- T4. Completion bounds (A), (B) for (P2-tw); decide whether r^{−7} decay suffices for the weighted consumers or whether a detail rule
  with exponential (or finite-range) decay keeping the exact left-inverse property exists.
- T5. Re-derive the Hessian-difference term list ((HD), (NC), (NS), (FW), (AC𝒞)) from the true linearisation.
- T6. Assemble (R2) on 𝒞_glob via Theorem GA as an implication, every input named with its status.

### What would count as a refutation (stated in advance)
- R0. For T0: a consumer of BFT-5 (b) whose required inequality (norm, weight, quantifier over sources/backgrounds) is not the one GP/L2
  prove — or a step of GP/L2 that fails (a counterexample, a k- or T-dependent constant, a norm mismatch that is not closed).
- R1. A d = 4 lattice function where a claimed Green's-function bound fails (exact rational evaluation at small |n| or a decay exponent
  that is wrong).
- R2. A level-l 1-form x_l with ‖x_l‖_{C^{1,α}} ≤ 1 (coarse units) whose Coulomb detail μ_l has sup|μ_l| ≫ ρ_{l+1}^{2+α}, or a k- or
  T-dependence of C_D (e.g. through the torus zero mode / periodisation of G, or the harmonic 1-forms).
- R3. A chain x with ‖Λ_HC x‖_𝒞 / |||x|||_{1,♯} growing with k, T, or the depth k − l; or a failure of the uniform discrete
  C^{1,β} bounds of the iterated subdivision basis functions (the HB input) at finite depth.
- R4. For T3: an odd L used by the lane for which no certified C^{1,β>θ}, Π_1-reproducing interpolatory L-adic scheme is exhibited, with
  L = 3 not sufficient for some consumer.
- R5. For T4: a twisted charge whose Λ_HC^T-completion has N_1-size not ≤ Cη N_ℛ; or a weighted consumer for which r^{−7} tails cost a
  factor growing in k, T or the distance, with no exponentially local replacement.
- R6. Any constant claimed uniform that depends on k, T or volume; any use of a refuted input (BGT55's BCH factorisation, S_E as the
  alignment, literal (β), (GAP-Z) as input, TRANSP slot transport), or of anything CODEX_REVIEW_ALIGN refutes.

### Gate discipline
Any numeric check: `checks/a2_55_<id>_criteria.md` with pre-registered PASS/FAIL written before the script; exact rational arithmetic
(python fractions/ints) only, no floats for verdicts; rigorous rational interval arithmetic for logarithms.

---

# FINDINGS (appended from 2026-10-29T04:5xZ; everything below was written after the PRE-STATED block)

## 0. Read record, inputs, symbols pinned

**Read (located by string; line numbers as of 04:25-04:50Z).** ALIGN55.md (all 565 lines); CODEX_REVIEW_ALIGN.md as on disk at 04:39Z
(156 lines, findings F1-F7 and the F1 witness supplement, last line "Incremental checkpoint UTC: 2026-10-29 04:39:26 UTC" — **still being
written: no banking list yet**); OFFGLOB55.md (all 800 lines, final status line 04:26Z); CODEX_REVIEW_OFFGLOB.md as on disk at 04:41Z
(F1-F4 only; its target 6, "Derive L1/L2 and determine whether the no-alignment conclusion reaches ALIGN55's actual Hessian pair", **not yet
reached**); HANDOFF.md (all); REVIEW_S22.md l.385-433 (the BFT statement, "BFT-5 (linear stability at the background)"); BGT55.md §2 (l.73-136),
§6-§8 (l.317-460); KFACTOR_OFF55.md §1 (l.66-130), §3 (l.208-327); CODEX_REVIEW_KOFF §5.3 (l.491-540), the CCP-constant passage (l.145-160)
and "Exactly what may be banked" (l.714-760); CODEX_REVIEW_GV §1 (l.27-92) and its banking list (l.422-428); CODEX_REVIEW_BFT34 banking list
(l.255-261); BFT34_55.md §1 (l.96-228); GSHARP55.md §4 (l.296-388); SF.md §6.2 (l.676-725); COFUN_CC.md §1 (l.110-140); BFT_A.md §1.3-§1.4
(l.30-46), §7.2 (l.454-473); ASSEMBLY55.md N19-N20, F7, F12 and Tier-1 list; PROOF.md l.791 ("Balaban takes L sufficiently large") and
l.4023-4040 (Lemma H1, the only "L ≥ 5" requirement found by grep). No Balaban CMP paper was available; the arXiv corpus was not needed for §1.

**Symbol pins (systemic defect 1).**
- **Λ_* vs Λ_0 — a live collision.** KFACTOR_OFF55 §1.1: Λ_0 := functions *constant* on the level-k roots, **Λ_* := functions vanishing on the
  level-k roots**. BGT55/ALIGN55: **Λ_0 := functions vanishing at the level-k roots** (= KFACTOR's Λ_*). Below I write **Λ_*** for the
  root-vanishing gauge functions in every formula, whichever file it comes from.
- **θ** = the class exponent (COFUN_CC's θ_c; CC-INV/RT-cc), never θ_w. **σ** = KFACTOR_OFF55's transport exponent, 0 < α < θ ≤ σ ≤ 1.
- **N** = COFUN_CC §1's source functional (P0 + Pc + Y + R slots); **N^{(σ)}** = KFACTOR_OFF55 §1.2's (G_0 + J + R(σ)); **N_Z** = BGT55's
  covariant N. **‖·‖_{(σ)}** = KFACTOR_OFF55's 𝔐^{(σ)}; **|||·|||_♯** = BGT55 §6.2's (= 𝔐^∇ + L^{(1+θ)q}-weighted residual sup + N_res).
- **ȳ** = the K^{(σ)} critical point in the global log chart of 𝒞_glob (OFFGLOB55's ȳ; BGT55's z); **η** := ‖ȳ‖_{(σ)}; n := L^k; q := k − 1 − l.
- **K_y** (log-chart infinitesimal gauge action, K_y = −Ξ + K′_y, KFACTOR_OFF55 §1.1); never ALIGN55's K (detail kernel).
- **C_CV** below is my completion constant (§1.4), not OFFGLOB55's (which it replaces on 𝒞_glob). **M_γ** = L^{d−1}(L−1)/2 (= 27 at d = 4,
  L = 3; KFACTOR_OFF55 HR, Codex KOFF item 1).

## 1. T0 — does (R2) on 𝒞_glob need an alignment? **No.** Proposition L2 (with its weighted form) delivers what the consumers use

### 1.1 What the consumers of BFT-5 (b) at Z ≠ 1 actually need (located, quoted, not re-judged)
REVIEW_S22 "BFT-5 (linear stability at the background)": "The composite slice Hessian at Z(V_k) satisfies (G♯) in the 𝔐-pair". BGT55 §2.4
lists the consumers at Z ≠ 1: **SF (a5-G♯) → HIST Theorem A5**, **B-NA-red**, **BFT-3 locality / (N-bg) at V ≠ 1**; GSHARP55 §4.1 adds
G-pert/(G♯-patch) (the transfer itself). What they read:
- **SF (a5-G♯)** (SF.md §6.2, "(a5-G♯) [restated; OPEN; = B-NA's (G♯) at non-trivial chains]"): (G♯) of the slice Hessian at a real critical
  chain, unweighted **and with weights e^{±md}, 0 ≤ m ≤ m_G**. SF's own correction ("[RSF2-fix GP-1/GP-2: reading withdrawn. Correct reading:
  (a5-G♯) on B-NA-red's class (chains X_c-small in one global gauge, ||B_k||_D ≤ ε_0), stated in the TRIVIAL slice at x^r, ⇐ (G♯_0-field) +
  (R♯_ω) + (FP♯') (Lemma G-pert, which is NA-IFT's Neumann step …)") says: **on the global-small class the consumer is posed in the global
  chart's slice, and a Neumann step from the trivial-chain inverse is the intended mechanism.** What blocked G-pert historically was that the
  trivial-chain inverse is bounded on cc sources only (CODEX_REVIEW_TOPCC item 5; GSHARP55 §8), while a Hessian perturbation produces non-cc
  sources.
- **B-NA-red** (GSHARP55 §4.1 item 2): (G♯) = ‖𝓛^{-1}‖_{Y→X}, ‖𝓛^{-1}N‖_{D→X} "plus their weighted forms"; any linear slice with (FP♯′).
- **BFT-3 at V ≠ 1 on 𝒞_glob** no longer consumes (R2): BFT34_55 Theorem BFT3-glob (route C) differentiates the cc-projected fixed point
  (Lemma WD), banked conditionally (CODEX_REVIEW_BFT34 item 1: "Conditional WD and route-C locality … with fixed μ, explicit
  (H1)/(H2)_μ/(H3)_μ").
- ASSEMBLY55 F12: all these consumers are still posed in old slices/pairs and must be restated "in S_E or the orbit norm" (bookkeeping).
**So the form consumed on 𝒞_glob is: the response, in one fixed slice of the global chart (S_E), to the sources a Neumann/IFT step generates,
bounded in a transport-weighted pair, unweighted and with exponential weights.** BGT55's literal (R2)(b) (covariant orbit norm 𝔐^∇_Z,
covariant N_Z) is a frame-free restatement of that; on 𝒞_glob no consumer needs the covariant form (a global chart exists).

### 1.2 Lemma L1 and Proposition L2 (OFFGLOB55 §4.1-§4.2), re-derived
Setting: 𝒞_glob, global chart, F(y) := 𝔉_k∘exp(y; B), H := Hessian at 0, 𝔑^0(y) := Hy − NB − ∇F(y), P_cc := 1 − P^TD^⊥ (HR routing),
S̃(y) := NB + 𝔑^0(y) − P^TD^⊥𝔑^0(y), Γ = Γ_E (ΓΞ = −1 on Λ_*; CODEX_REVIEW_GV item 3), 𝓛_Γ := H + Γ^TΓ.
- **L1 (a) (identity).** D^⊥(NB) = 0 and D^⊥(Hy) = ((HΞ)^Ty)^⊥ = 0, so S̃(y) = P_cc(NB + Hy − ∇F(y)) = Hy + NB − P_cc∇F(y) − NB + NB … exactly:
  S̃(y) = NB + Hy − ∇F(y) − P^TD^⊥(Hy − NB − ∇F(y)) = Hy − P_cc∇F(y) + [NB − P^TD^⊥(−NB)] − … ; the clean form is **D_yS̃(y)u = Hu −
  P_ccH^{log}_yu**, hence **𝓛_Γ − D_yS̃(y) = P_ccH^{log}_y + Γ^TΓ =: 𝒦_y**. CONFIRMED (two lines; the only facts used are D^⊥(Hu) = 0 and
  linearity of P_cc).
- **L1 (b) (invertibility).** For cc f, solve u = 𝓛_Γ^{-1}(f + D_yS̃(y)u). Every value of D_yS̃(y) is cc (CCP (a), Codex KOFF item 2), and
  𝓛_Γ^{-1} maps cc sources into Ker Γ with ‖𝓛_Γ^{-1}g‖_{(σ)} ≤ G·N^{(σ)}(g) (GV-E + LIN^{(σ)}: CODEX_REVIEW_GV item 2, CODEX_REVIEW_KOFF item 5,
  "let G bound the full cc response in 𝔐^(σ)"). With Codex KOFF §5.3's corrected source bound **N^{(σ)}(S̃(x) − S̃(x′)) ≤ K(η + η′ + s)‖x − x′‖_{(σ)}**
  the map T := 𝓛_Γ^{-1}D_yS̃(y) has norm ≤ GK(2η + s) ≤ ½ for η, s small. **Scope remark (resolves OFFGLOB55's "full ball vs slice ball" note):
  L2 never needs T off the slice.** At the slice critical point ȳ ∈ Ker Γ, the fixed-point problem u = 𝓛_Γ^{-1}(f + D_ȳS̃(ȳ)u) is posed on
  Ker Γ (𝓛_Γ^{-1} lands there), and D_ȳS̃(ȳ)u for u ∈ Ker Γ is the limit of slice differences (ȳ + tu ∈ the slice ball). So L1 (b) restricted to
  Ker Γ follows from the slice-ball Lipschitz bound alone, whichever ball Codex's §5.3 bound covers. **CONFIRMED** (as an implication of the
  banked conditional inputs: lane-A linear package, GV-E, corrected Theorem K, CCP), on Ker Γ: **for every cc f there is exactly one u ∈ Ker Γ
  with P_ccH^{log}_ȳu = f, and ‖u‖_{(σ)} ≤ 2G·N^{(σ)}(f).**
- **L2 (a) (exact solution of the Hessian equation).** Let K_ȳ^Tf = 0. Take u := 𝒦_ȳ^{-1}P_ccf ∈ Ker Γ, so g := H^{log}_ȳu − f has P_ccg = 0,
  i.e. g = P^TD^⊥g. At a critical point K_ȳ^TH^{log}_ȳ = 0 (differentiate ⟨∇F(y), K_yλ⟩ ≡ 0 at ȳ; the term with ∇F(ȳ) vanishes), so K_ȳ^Tg = 0,
  i.e. Ξ^Tg = K′^T_ȳg and D^⊥g = (K′^T_ȳg)^⊥. Put j := P^TD^⊥g (a plain-current representation of the functional g). Then j = P^T(K′^T_ȳj)^⊥
  (K′^T acts on the functional), and CCP (c) gives J(j) ≤ 2dc_BernL^{d−1}η·J(j) with 2dc_BernL^{d−1} ≤ 127.44 at d = 4, L = 3 (c_Bern ≤ 59/100,
  Codex KOFF l.145-157: η′ < 25/3186 certified). So J(j) = 0, j = 0, g = 0: **H^{log}_ȳu = f exactly**, and ‖u‖_{(σ)} ≤ 2G·N^{(σ)}(P_ccf).
  **CONFIRMED.** (The step "J is a norm on representations, apply CCP (c) to the representation P^TD^⊥g" is the point; it is exactly CCP (d)'s
  argument, Codex KOFF item 2.)
- **L2 (c) (plain-current completion).** For a plain-current f with K_ȳ^Tf = 0: J(P^TD^⊥f) = J(P^T(K′^T_ȳf)^⊥) ≤ 127.44η·J(f). **CONFIRMED**
  (CCP (c) verbatim). Its G- and s-slot analogues are OFFGLOB55's ARGUED "CONV"; they are proved in §1.4 below.

### 1.3 (N1-nd) at ȳ needs no Faddeev–Popov hypothesis — a shorter proof of L2 (b). PROVEN-HERE
> **Lemma N1-L.** In the setting of §1.2 (𝒦_ȳ invertible on Ker Γ), **Ker H^{log}_ȳ = K_ȳΛ_*** (on tangent vectors with u_k = 0). Equivalently
> (H_Z = J^TH^{log}_ȳJ and Ξ_Z = ∓J K_ȳ at a critical point) **Ker H_Z = Ran Ξ_Z: (R2)(a)**.

*Proof.* (i) K_ȳΛ_* ⊆ Ker H^{log}_ȳ (KER at a critical point, the symmetric form of K_ȳ^TH^{log}_ȳ = 0). (ii) **K_ȳ is injective on Λ_*** with no
smallness: K_ȳλ = 0 says the configuration e^ȳ is infinitesimally fixed by λ, i.e. λ(head b) = Ad_{U(b)}^{−1}λ(tail b) on every link of every level;
the level-0 links connect the torus, so λ is determined by its value at one level-k root, where it is 0. So dim K_ȳΛ_* = dim Λ_*. (iii) Ker H^{log}_ȳ
∩ Ker Γ = {0}: such a u has 𝒦_ȳu = P_cc0 + Γ^T0 = 0, so u = 0 (L1 (b)). Hence Γ is injective on Ker H^{log}_ȳ and dim Ker H^{log}_ȳ ≤ rank Γ =
dim Λ_* (Γ: tangent space → Λ_* is onto, since ΓΞ = −1). With (i)-(ii): equality of dimensions, so Ker H^{log}_ȳ = K_ȳΛ_*. ∎
**Consequence:** OFFGLOB55 L2 (b)'s extra hypothesis ("If ΓK_ȳ is invertible on Λ_* (NSL55 (f) … Codex pending; or directly …)") is
**unnecessary**; invertibility of ΓK_ȳ is a *corollary* (ΓK_ȳ is injective because Ker Γ ∩ K_ȳΛ_* ⊆ Ker Γ ∩ Ker H = 0). NSL is not an input of
(R2)(a) on 𝒞_glob.

*Erratum to §1.2, L1 (a) bullet (written 04:5xZ, on re-reading; text above unchanged).* The displayed chain "S̃(y) = P_cc(NB + Hy − ∇F(y)) =
Hy + NB − … ; the clean form is" is garbled. Correct one-line derivation: S̃(y) = NB + P_cc𝔑^0(y) (P_cc linear, D^⊥(NB) = 0), and
D_y𝔑^0(y)u = Hu − H^{log}_yu, so **D_yS̃(y)u = P_cc(Hu − H^{log}_yu) = Hu − P_ccH^{log}_yu** (D^⊥(Hu) = ⟨u, HΞ·⟩ = 0). The conclusion
𝓛_Γ − D_yS̃(y) = 𝒦_y is unchanged.

### 1.4 Lemma CONV-P (the cc-completion of a background-cc source costs O(η) in N^{(σ)}, every slot). PROVEN-HERE
This is OFFGLOB55 Lemma CONV restricted to what L2 consumes on 𝒞_glob: no chart change (the consumers' sources are log-chart sources), only
the completion P_cc. OFFGLOB55 proved the plain-current slot (L2 (c)) and ARGUED the G- and s-slots.
> **Lemma CONV-P.** Let ȳ ∈ Ker Γ be the critical point of §1.2 with η := ‖ȳ‖_{(σ)} ≤ η_CV (own |ȳ_j| ≤ ½, 127.44η < 1, and ȳ inside the local
> analyticity polydisc of the soft residual). Let f = (G_0; s_0..s_{k−1}; j_0..j_{k−1}) be a log-chart source, f(u) = ⟨G_0, du_0⟩ +
> Σ_l⟨s_l, r_l(u)⟩ + Σ_l⟨j_l, u_l⟩, with **K_ȳ^Tf = 0**. Then
>   **J(P^TD^⊥f) ≤ η·[ c_j·J(j) + c_G·(‖G^c_0‖_∞ + [G^c_0]^∞_α) + c_s·‖s‖_{R(σ)} ]**, hence **N^{(σ)}(P_ccf) ≤ (1 + C_CVη)·N^{(σ)}(f)**,
> with c_j = 2dc_BernL^{d−1} (≤ 127.44 at d = 4, L = 3), **c_G = 2d(d−1)M_γ/(L − 1) + 4d(d−1)M_γ/(L^α − 1) + 4.1dM_γη** (= 324 + 1296/(3^α − 1) +
> 443η at d = 4, L = 3), c_s = (2dM_γ/(L−1))(1 + C_ρη)/(1 − L^{−2σ}) + 2dM_γC_Ψ(n_ovL³ + 1)/(1 − L^{−σ})² + O(η), and
> C_CV := max(c_j, C_CH·c_G, c_s), C_CH = C_CH(d, α) the Campanato→pointwise constant (step 0). All constants are independent of k, T.

*Proof.* **Step 0 (which charge is routed).** D(f)(λ) = f(Ξλ) = ⟨G_0, ddλ⟩ + Σ_l⟨s_l, r_l(Ξλ)⟩ + Σ_l⟨j_l, d ev^{(l)}λ⟩ = Σ_l⟨j_l, d ev^{(l)}λ⟩ (dd = 0;
root covariance r_l∘Ξ = 0). And K_ȳ^Tf = 0 with K_ȳ = −Ξ + K′_ȳ gives Ξ^Tf = K′^T_ȳf. So **D^⊥f = (K′^T_ȳf_G)^⊥ + (K′^T_ȳf_s)^⊥ + (K′^T_ȳf_j)^⊥**
(f_G, f_s, f_j the three slot parts), and P^TD^⊥f is the sum of the three routed pieces; I bound each by Lemma HR (Codex KOFF item 1:
(iii) sup route J ≤ 2dM_γ(k − l)π_l(w) for u = ev^{(l)T}d*w; (iv) Hölder route J ≤ dM_γ[w^c]^∞_α/(L^α − 1) for a level-0 divergence, w^c = n^{d−1}w;
(v) bare charges J ≤ (M_γ/(L−1))L^{d(k−j)}sup|v| for u = ev^{(j)T}v). Campanato→pointwise: N^{(σ)}'s [G^c_0]_α is BFT_A §7.2's Campanato
seminorm and HR (iv) uses the pointwise one; on the lattice, telescoping box averages B_i (side 2^iρ_0, one site at i = 0) gives
|avg_{B_i} − avg_{B_{i+1}}| ≤ 2^{d/2}Osc_2(B_{i+1}), hence [g]^∞_α ≤ C_CH[g]_α with C_CH ≤ 4·2^{1+d/2}·2^α(1 + 1/(2^α − 1)) (separations ≤ 1/4
directly through a common box of side ≤ 1; up to 1 by a chain of four steps). Standard; constant not optimised.
**Step 1 (the exact gauge-action identity).** For a link with log X and endpoint values a = λ(tail), c = λ(head), the left-trivialised
generator is K_X(a, c) = ψ_−(ad_X)a − ψ_+(ad_X)c, ψ_−(z) = z/(e^z − 1), ψ_+(z) = z/(1 − e^{−z}) (KFACTOR_OFF55 CCP (c), Codex KOFF item 2; re-derived:
d/dt e^{Y(t)} = e^Y((1 − e^{−ad_Y})/ad_Y)Y′ applied to e^{ta}e^Xe^{−tc}, and ψ_+(z)e^{−z} = ψ_−(z)). Since **ψ_−(z) − ψ_+(z) = −z exactly** and
ψ_−(z) + ψ_+(z) = z·coth(z/2), with λ̄ := (a + c)/2 and δ := c − a:
  **K′_X(a, c) := K_X(a, c) − (a − c) = −[X, λ̄] − ½Φ(ad_X)δ,  Φ(z) := z·coth(z/2) − 2 = 2Σ_{n≥1}B_{2n}z^{2n}/(2n)!**,
and ‖Φ(ad_X)‖ ≤ 2(1 − (r/2)cot(r/2)) ≤ (r²/6)/(1 − r²/(4π²)) for r := ‖ad_X‖ ≤ 2|X| ≤ 1 (1 − x cot x = 2Σζ(2n)(x/π)^{2n} ≤ (x²/3)/(1 − x²/π²)).
This exact split (a commutator with the link mean, plus an even remainder acting on dλ) is new; it is what makes the G-slot k-uniform.
**Step 2 (j-slot).** CCP (c) verbatim: J(P^T(K′^T_ȳf_j)^⊥) ≤ c_jη·J(j).
**Step 3 (G_0-slot).** K′^T_ȳf_G(λ) = ⟨G_0, d(K′_ȳλ)_0⟩. Insert Step 1 on each level-0 link and write, for a plaquette P = (z; μ < ν) with ∂P = b1 + b2 −
b3 − b4 (b1 = (z, μ), b2 = (z + e_μ, ν), b3 = (z + e_ν, μ), b4 = (z, ν)), λ̄(b) = λ(z) + (λ̄(b) − λ(z)) with λ̄(b1) − λ(z) = ½dλ(b1),
λ̄(b2) − λ(z) = dλ(b1) + ½dλ(b2), λ̄(b3) − λ(z) = dλ(b4) + ½dλ(b3), λ̄(b4) − λ(z) = ½dλ(b4). Using ⟨G, [Y, λ]⟩ = ⟨[G, Y], λ⟩:
  **K′^T_ȳf_G(λ) = −Σ_P⟨[G_0(P), (dȳ_0)(P)], λ(z_P)⟩ + ⟨w_A, dλ_0⟩ + ⟨w_B, dλ_0⟩,**
  w_A(b′) := −Σ_{(P,b)}c_{P,b→b′}ε_{P,b}[G_0(P), ȳ_0(b)] (coefficients c ∈ {½, 1} read off the four lines above),
  w_B(b) := −½Σ_{P∋b}ε_{P,b}Φ(ad_{ȳ_0(b)})G_0(P) (Φ(ad) is symmetric).
(3a) *Point charges.* Each site is the base of d(d−1)/2 plaquettes; own |G_0| = n^{−2}|G^c_0| (BFT_A §1.3: 2-forms H^c = L^{2(k−j)}H); own
|(dȳ_0)(P)| ≤ |ȳ_0(b1) − ȳ_0(b3)| + |ȳ_0(b2) − ȳ_0(b4)| ≤ 2n^{−2}‖∇^cȳ^c_0‖ ≤ 2n^{−2}η; |[A, B]| ≤ 2|A||B|. So the charges are ≤ 2d(d−1)n^{−4}η‖G^c_0‖ and
HR (v) at j = 0 routes them for J ≤ (M_γ/(L − 1))n^4·2d(d−1)n^{−4}η‖G^c_0‖ = **2d(d−1)M_γη‖G^c_0‖/(L − 1)** (= 324η‖G^c_0‖).
(3b) *The w_A divergence.* Per plaquette the coefficient mass is 1.5 on b1 and b4 and 0.5 on b2 and b3; a level-0 link lies in d − 1 plaquettes
in a "1.5" position and d − 1 in a "0.5" position, so Σ|c| ≤ 2(d − 1) per link. Hence w^c_A := n³w_A = Σc·ε·[G^c_0(P), ȳ^c_0(b)] (n³·n^{−2}·n^{−1} = 1)
obeys, for translates along an axis by coarse distance r ≤ 1, [w^c_A]^∞_α ≤ 2·2(d − 1)(‖ȳ^c_0‖[G^c_0]^∞_α + ‖G^c_0‖[ȳ^c_0]^∞_α) ≤ 4(d − 1)η(‖G^c_0‖ +
[G^c_0]^∞_α) (‖ȳ^c_0‖_∞ ≤ η; [ȳ^c_0]^∞_α ≤ ‖∇^cȳ^c_0‖ ≤ η at separations ≤ 1). HR (iv): J ≤ **4d(d − 1)M_γη(‖G^c_0‖ + [G^c_0]^∞_α)/(L^α − 1)**
(= 1296η(…)/(3^α − 1)). **No factor k**: this is why the divergence must go by the Hölder route; the sup route (iii) would give 2dM_γ·k·π_0(w_A) =
2dM_γk·4(d−1)η‖G^c_0‖, not uniform — the k-dependence OFFGLOB55's CONV paragraph avoided by the same choice.
(3c) *The Φ remainder.* own |w_B| ≤ ½·2(d − 1)·‖Φ‖·n^{−2}‖G^c_0‖ with ‖Φ‖ ≤ (4n^{−2}η²/6)(1.01), i.e. ≤ 2.04n^{−4}η²‖G^c_0‖ at d = 4, so
π_0(w_B) ≤ 2.04η²‖G^c_0‖/n and HR (iii) gives J ≤ 2dM_γk·2.04η²‖G^c_0‖/n ≤ **4.1dM_γ(k/L^k)η²‖G^c_0‖** (k/L^k ≤ 1/3).
**Step 4 (s-slot).** K′^T_ȳf_s(λ) = Σ_l⟨s_l, r_l(K′_ȳλ)⟩ and r_l(K′λ) = r_l(K_ȳλ) (r_l∘Ξ = 0). Write Dρ_l(ȳ) for the log-chart linearisation of the
soft residual at ȳ and δ_l(ȳ) := Dρ_l(ȳ) − r_l. Exact covariance of the soft residual (ρ(U^g)(c) = Ad_{g(c_Y)}ρ(U)(c); CODEX_REVIEW_BGT §4 in actual-generator
form, sign immaterial here) gives Dρ_l(ȳ)[K_ȳλ] = ±[λ(c_Y), ρ_l(ȳ)]. Hence
  r_l(K′_ȳλ) = ±[λ(c_Y), ρ_l(ȳ)] + δ_l(ȳ)[Ξλ] − δ_l(ȳ)[K′_ȳλ].
*Local analytic input (LA-loc).* ρ_l(c) = Ψ(local log-chart variables on the S4′ contour support N(c) and c), one fixed analytic Ψ for all c, l, k, T
(translation- and level-invariance of the S4′ map); Dρ_l(0) = r_l. By Cauchy on a fixed polydisc, ‖DΨ(v) − DΨ(0)‖_{ℓ^∞→su(N)} ≤ C_Ψ|v|_∞ there, C_Ψ =
C_Ψ(d, L, N). With own |ȳ_l| ≤ L^{−(q+1)}η, |ȳ_{l+1}| ≤ L^{−q}η (KFACTOR_OFF55 §1.4 (1c); Codex KOFF item 5): |δ_l(ȳ)[v](c)| ≤ C_ΨL^{−q}η|v_loc|_∞.
n_ov := the largest number of coarse links whose N(c) contains a given level-l link (finite, depends on d, L). Own |s_l| = L^{−q}‖s^c_l‖ ≤
L^{−(2+σ)q}‖s‖_{R(σ)}.
(4a) *Point charges ±[ρ_l(c), s_l(c)] at level-(l+1) sites*: ≤ 2d|ρ_l||s_l| with own |ρ_l(ȳ)| ≤ L^{−(2+σ)q}(η + C_ρη²) (KFACTOR_OFF55 §1.4 (1b)). HR (v) at
j = l + 1: J ≤ (M_γ/(L−1))L^{4q}·2dL^{−2(2+σ)q}(η + C_ρη²)‖s‖_{R(σ)} = (2dM_γ/(L−1))L^{−2σq}(η + C_ρη²)‖s‖_{R(σ)}; Σ_q ≤ (1 − L^{−2σ})^{−1}.
(4b) *δ_l(ȳ)[Ξλ]* = ⟨ω_l, dλ_l⟩ + ⟨ω_{l+1}, dλ_{l+1}⟩ with own |ω_l| ≤ n_ovC_ΨL^{−q}η·max|s_l|, |ω_{l+1}| ≤ C_ΨL^{−q}η·max|s_l|. So π_l(ω_l) ≤
n_ovC_ΨL³L^{−σq}η‖s‖_{R(σ)} and π_{l+1}(ω_{l+1}) ≤ C_ΨL^{−σq}η‖s‖_{R(σ)}; HR (iii): J ≤ 2dM_γ[(q + 1)π_l(ω_l) + qπ_{l+1}(ω_{l+1})] ≤
2dM_γC_Ψ(n_ovL³ + 1)(q + 1)L^{−σq}η‖s‖; Σ_q(q + 1)L^{−σq} = (1 − L^{−σ})^{−2}. (Here the factor k − l of the sup route is harmless: it is beaten by L^{−σq}.)
(4c) *δ_l(ȳ)[K′_ȳλ]*: K′λ carries λ itself (−[ȳ, λ̄]), so these are point charges at level-l/(l+1) sites of size ≤ 2n_ovC_ΨL^{−2q}η²max|s_l|; HR (v) at j = l:
J ≤ (2n_ovC_ΨM_γL⁴/(L − 1))L^{−σq}η²‖s‖_{R(σ)}, summable (the Φ-part is O(η³) and divergence-form). This is the O(η) in c_s.
Sum Steps 2-4 and use N^{(σ)}(P_ccf) ≤ N^{(σ)}(f) + J(P^TD^⊥f). ∎
**Status.** j- and G_0-slots PROVEN-HERE with explicit constants (inputs: Lemma HR, CCP (c) — Codex KOFF items 1-2; BFT-1 sizes — KOFF item 5).
s-slot PROVEN-HERE with constants C_Ψ, n_ov that exist by local analyticity (Cauchy on one fixed polydisc) and are independent of k, T, but whose
numerical values I did not compute. The identity of Step 1 and the G-slot decomposition of Step 3 are checked exactly in a2_55_conv (§1.11).

### 1.5 The σ-pair against ALIGN55's pair (|||·|||_♯ → N): what L2 at σ = θ gives in ALIGN55's currency. PROVEN-HERE (norm algebra)
Take **σ = θ** (allowed: Codex KOFF item 5 "for each fixed 0<α<θ≤σ≤1"; GV-E item 2 "choose θ_0 ≤ σ"; ROW^{(σ)} needs only σ > 0).
- **Sources.** For representations (G_0; s; j) (no positive-level divergence slot): J = π_0(j_0) + Σ_{l≥1}π_l(j_l) ≤ π_0(j_0) + ‖j‖_Pc/(L^θ − 1)
  (COFUN_CC §1 "|j|_Σ ≤ ‖j^c_0‖_∞ + ‖j‖_Pc/(L^θ − 1)"), and ‖s‖_{R(θ)} = max_lL^{(1+θ)q}‖s^c_l‖ = L^{−θ}‖s‖_R exactly. Hence
  **N^{(θ)}(f) ≤ C_N·N(f), C_N := max(1, (L^θ − 1)^{−1})** (= 1.366 at L = 3, θ = ½). The reverse fails: CODEX_REVIEW_GV item 1's exact witness
  (one level-1 constant cc current, N/N^{(σ)} = L^{θ(k−1)}). **So a response bound in N^{(θ)} is stronger than one in N**; L2 at σ = θ implies
  ‖u‖_{(θ)} ≤ 2G(1 + C_CVη)C_N·N(f).
- **Fields.** ‖u‖_{(θ)} = max_j[‖u^c_j‖ + ‖∇^cu^c_j‖ + [∇^cu^c_j]_α + L^{(1+θ)(k−1−j)}‖r^c_j‖] dominates both ‖u‖_{𝔐^∇} (whose residual weight is
  L^{k−1−j} ≤ L^{(1+θ)(k−1−j)}) and the ♯ residual leg max_{i≤k−2}L^{(1+θ)(k−1−i)}‖r^c_i‖. It does **not** contain N_res(u) = Σ_i‖r_i(u)‖_{C^{1,α}}
  (BFT_B §15.0). So **L2 at σ = θ gives every component of |||u|||_♯ except N_res**, and it gives the field half *in the slice* (stronger than the
  orbit norm: ‖[u]‖ ≤ ‖u‖ for the slice representative).
- **N_res** is needed by ALIGN55's GA bookkeeping ((FW), RW♯), not by any consumer located in §1.1. For responses it is a gauge-invariant
  residual-Hölder quantity (RHT-cc type), not supplied by K^{(σ)}; if a consumer needs it, it is a separate (NOT-VERIFIED) item at Z ≠ 1.
- **Positive-level divergence slots.** N has ‖G‖_Y over all levels; N^{(σ)} has G_0 only. TOWER-VAR's Hessian and the IFT sources of the
  consumers carry curvature at level 0 only (KFACTOR_OFF55 §1.2, citing CODEX_REVIEW_C2 §5), so the comparison above covers them. A source
  with G_l, l ≥ 1, can be rewritten via s_i = −(Q^{(i+1→l)})^Td*G_l plus a level-0 source (𝒬^{(0→l)})^TG_l (BFT_A l.689-691) with uniform sup
  bounds, but the level-0 Campanato seminorm is then **not** controlled (BFT_A l.536-537): such sources are outside what L2 covers (scope
  limit, stated).

### 1.6 The weighted form L2_m. PROVEN as an implication of (H2)_m + (H3)_m (the inputs Codex banked Lemma WD on)
For m > 0 and a weight centre X_0, let ‖·‖_{(σ),m} and N^{(σ)}_m be the e^{m·dist(·,X_0)}-weighted norms (COFM55 §1's convention, as in BFT34_55
Lemma WD). Assume **(H2)_m** ‖𝓛_Γ^{-1}g‖_{(σ),m} ≤ G(m)N^{(σ)}_m(g) for cc g, and **(H3)_m** ‖D_yS̃(y)u‖_{N^{(σ)}_m} ≤ e^{c_rm}Λ(s)‖u‖_{(σ),m} on the ball
(BFT34_55 §1.2's statements, verbatim). Then:
(i) the Neumann series of §1.2 runs in the weighted norms: for G(m)e^{c_rm}Λ(s) ≤ ½, u = 𝒦_ȳ^{-1}P_ccf obeys ‖u‖_{(σ),m} ≤ 2G(m)N^{(σ)}_m(P_ccf);
(ii) CONV-P holds weighted with c_• replaced by e^{c′m}c_•, c′ an absolute constant: every routing path of P^T stays in the level-k block of its
charge (coarse diameter ≤ d/2 = 2, KFACTOR_OFF55 HR "it stays in the block"; BFT34_55 §1.5 (H3)_m row "total coarse length ≤ d/2 = 2"), and every
charge of Steps 2-4 sits within one plaquette, one link or one contour support (coarse size ≤ 2) of the source value producing it;
(iii) Lemma N1-L is weight-free (an algebraic statement).
So **‖u‖_{(σ),m} ≤ 2G(m)(1 + e^{c′m}C_CVη)N^{(σ)}_m(f)**, the weighted (R2)(b) in slice form, for 0 < m ≤ m_Y. **Status of the inputs** (as
recorded on disk): (H2)_m's gauge-invariant half CC-INV_m — Codex COFM items 2-4 CONFIRMED (BFT34_55 §1.5 table); its gauge-variant half
GV-E_m — CODEX_REVIEW_GV item 6 CONFIRMED conditionally in N_{Σ,m} (N_Σ ≤ (1 + L^θ)N^{(σ)} on (G_0, s, j) representations, so it transfers);
the σ-weighted residuals — BFT34_55 "PROVEN as an implication, modulo reading COFUN_CC §6.1's weighted (a)-bound"; **(H3)_m — ARGUED**
(BFT34_55 §1.5: "the localised form of each unweighted bound … is not written anywhere; plausible, standard"). CODEX_REVIEW_BFT34 item 1 banked
Lemma WD "with fixed μ, explicit (H1)/(H2)_μ/(H3)_μ" — **L2_m consumes exactly those premises and nothing else.** The rate is the route-C rate
(m ≤ m_Y ≤ 1.666·10⁻⁴ per coarse unit, BFT34_55 §1.3): positive, k-, T-uniform, small.

### 1.7 Lemma NE / the covariant restatement: not on the critical path on 𝒞_glob
BGT55's literal (R2)(b) is stated in the covariant orbit norm 𝔐^∇_Z with covariant sources N_Z. Converting L2's global-chart statement into it
needs (i) the chart map J (H_Z = J^TH^{log}_ȳJ, S = J^{−T}f) and (ii) flat-vs-covariant norm comparisons at Z = e^ȳ — OFFGLOB55's Lemma NE and the
chart part of CONV, ALIGN55's (NC)/(NS). These are ARGUED in both files and **are needed equally by the GA route** (ALIGN55 §7 item 12). No
consumer located in §1.1 is posed in covariant norms on 𝒞_glob (SF's corrected reading is the trivial slice of the global chart; B-NA-red is
posed in a linear slice at the trivial chain). **Verdict: NE is not on the critical path for (R2) on 𝒞_glob; it is needed only off 𝒞_glob, where
no global chart exists (GP's frame-local norms), and there only to compare with covariant norms.** One fact I can add without NE: the *source
class* matches exactly — S ∈ cc_Z ⟺ f := J^TS has K_ȳ^Tf = 0 (Ξ_Z = ∓JK_ȳ at Z = e^ȳ, a chart identity), so L2 (a) covers all of (R2)'s sources.

### 1.8 Item 5 of the brief ((HD), Codex ALIGN's "most dangerous" gap) on this route: discharged by banked inputs, in the σ-pair
**Finding.** On the L2 route the Hessian difference enters only through **D_ȳS̃(ȳ)u = −P_cc(H^{log}_ȳ − H)u**, and its all-order bound
  **N^{(σ)}(P_cc(H^{log}_y − H)u) ≤ K(2η + s)‖u‖_{(σ)}**  (y in the slice ball, u in slice directions)
is the derivative of Codex's corrected source-map Lipschitz bound "N^(σ)(difference) ≤ K(η+η′+s)||x−x′||_(σ)" (CODEX_REVIEW_KOFF §5.3), which rests
on "the SG identity and its exact factor Θ, and the uniform full-source bounds after replacing the false LA-1 by LA-1′" (item 3), CB "with the
corrected full-source constants" (item 4) and corrected Theorem K (item 5) — **CONFIRMED, conditionally** on the lane-A linear package and GV.
That is an all-order Hessian-difference estimate in the actual chart of the route (the global log chart at trivial-chain centring) and in the
route's own pair. The un-projected difference at the critical point follows from CONV-P: (H^{log}_ȳ − H)u = P_cc(…)u + P^T(K′^T_ȳH^{log}_ȳu)^⊥
(D^⊥(Hu) = 0, D^⊥(H^{log}_ȳu) = (K′^T_ȳH^{log}_ȳu)^⊥ at a critical point), so N^{(σ)}((H^{log}_ȳ − H)u) ≤ [K(2η + s) + C_CVηC_H]‖u‖_{(σ)}/(1 − C_CVη),
C_H := ‖H‖_{𝔐^{(σ)}→N^{(σ)}} (≤ 2 + 2[·]-Hölder terms + κ_+: Wilson part G_0 = du_0 has ‖G^c_0‖ = ‖f_0(u)‖ ≤ 2‖u‖; soft part s_l = κ_lr_l(u) has ‖s‖_{R(σ)} ≤
κ_+‖u‖_{(σ)}). **Verdict on item 5: CONFIRMED-by-banked-input on the L2 route** (σ-pair, global chart, all orders).
**On the GA route ((♯ → N) pair, chart J at Z, covariant r^Z, N_res) it stays NOT-VERIFIED**, and it is not needed. What it would need, located:
(a) the Pc slot of N — CB's proof sums *per-level* row bounds π_l(R^B_l) ≤ A_BL^{−σ(k−1−l)}η² (KFACTOR_OFF55 Proposition CB), and L^{θ(k−l)}·L^{−σ(k−1−l)}
is bounded for θ ≤ σ, so this part looks routine (ARGUED); (b) the chart/covariant residual comparison r^Z_l = Dρ_l(z) vs r_l, which is ♯-small only
through CEN2-type cancellation (without it own |δ_l(z)u| ≍ |z_l||u_l| and the ♯ weight leaves L^{θq}: ALIGN55 §4's (AC𝒞) mechanism, whose printed
prefactor Codex corrected to L^{−4}); (c) N_res of (H_Z − H_1)w's response. The GA route needs these because GA works in the orbit norm where the
unprojected difference must be fed to the flat inverse; L2 never forms it (OFFGLOB55 §4.2's own "mechanism differs" paragraph — CONFIRMED).

### 1.9 Theorem R2-glob-L (assembly). PROVEN as an implication; inputs and statuses
> **Theorem R2-glob-L.** Fix d = 4, odd L ≥ 3, N ≥ 2, κ_±, 0 < α < θ ≤ σ ≤ 1 (σ = θ allowed). There are ε_L > 0 and C_L < ∞ depending only on
> (N, L, κ_±, α, θ, σ) — not on k, T — such that for every k ≥ 1, T ≥ 3 and data B ∈ 𝒞_glob(ε), ε ≤ ε_L (real, or on BFT-2's complex polydisc), at
> the composite critical point ȳ = x(B) ∈ Ker Γ_E of Theorem BFT-E (Z = e^ȳ):
> **(a)** Ker H^{log}_ȳ = K_ȳΛ_*, i.e. Ker H_Z = Ran Ξ_Z on {x_k = 0} — (R2)(a), (N1-nd);
> **(b)** for every log-chart source f with K_ȳ^Tf = 0 (equivalently S = J^{−T}f ∈ cc_Z) and a (G_0; s; j) representation, the equation H^{log}_ȳu = f has
> exactly one solution u ∈ Ker Γ_E = S_E, all solutions are u + K_ȳΛ_*, and **‖u‖_{(σ)} ≤ C_L·N^{(σ)}(f)**; at σ = θ also **‖u‖_{(θ)} ≤ C_LC_N·N(f)**,
> so every component of |||u|||_♯ except N_res is bounded by C_LC_N·N(f), and the orbit norm ‖[u]‖_{𝔐^∇} ≤ ‖u‖_{(θ)};
> **(c)** if (H2)_m and (H3)_m hold for some 0 < m ≤ m_Y, the same in the e^{m·dist}-weighted pair with C_L(m) = 2G(m)(1 + e^{c′m}C_CVη).
> Here C_L = 2G(1 + C_CVη), G := the bound of 𝓛_Γ^{-1} on cc sources in 𝔐^{(σ)} (GV-E + LIN^{(σ)}).

| # | input | status (file, locating string) |
|---|---|---|
| 1 | BFT-0/1/2 on 𝒞_glob: the slice critical point ȳ, ‖ȳ‖_{(σ)} ≤ C_0s, BFT-1 sizes (2, 2+σ, 1) | CODEX_REVIEW_GV item 4 + CODEX_REVIEW_KOFF item 5: **CONFIRMED, conditionally** (lane-A linear package; "GV itself … NOT-VERIFIED" in KOFF, supplied by GV-E, GV item 2) |
| 2 | 𝓛_Γ^{-1} on cc sources, bound G (GV-E + LIN^{(σ)}) | CODEX_REVIEW_GV item 2, CODEX_REVIEW_KOFF item 5: **CONFIRMED, conditionally** |
| 3 | source-map Lipschitz bound N^{(σ)}(S̃(x) − S̃(x′)) ≤ K(η + η′ + s)‖x − x′‖ (all orders) | CODEX_REVIEW_KOFF §5.3 + items 3-5: **CONFIRMED, conditionally** |
| 4 | Lemma HR (i)-(v), CCP (a)-(d) incl. c_Bern ≤ 59/100 | CODEX_REVIEW_KOFF items 1-2: **CONFIRMED** |
| 5 | Lemma L1 on Ker Γ, Proposition L2 (a), (c) | re-derived §1.2: **CONFIRMED** as implications of 1-4 (slice-ball scope suffices) |
| 6 | Lemma N1-L ((N1-nd) without ΓK-invertibility) | §1.3: **PROVEN-HERE** (dimension count; injectivity of K_ȳ by connectivity) |
| 7 | Lemma CONV-P (G_0-, s-, j-slots) | §1.4: **PROVEN-HERE** (G, j explicit; s via a fixed-polydisc Cauchy constant C_Ψ); exact identities a2_55_conv PASS |
| 8 | norm comparison σ = θ vs (♯ → N) | §1.5: **PROVEN-HERE** (N^{(θ)} ≤ C_N N; ‖·‖_{(θ)} ⊇ 𝔐^∇ + ♯ residual leg; N_res not included) |
| 9 | weighted (c): (H2)_m, (H3)_m | (H2)_m: CC-INV_m Codex COFM items 2-4, GV-E_m CODEX_REVIEW_GV item 6 (conditional); **(H3)_m ARGUED** (BFT34_55 §1.5) |
*Proof.* (a) Lemma N1-L. (b) L2 (a) with CONV-P for N^{(σ)}(P_ccf), and §1.5 for σ = θ. (c) §1.6. ∎
**Not claimed:** the covariant orbit-norm form in (𝔐^∇_Z, N_Z) (needs NE/chart comparisons, §1.7); N_res; sources with positive-level
divergence slots; anything off 𝒞_glob; any item above beyond its recorded status.

### 1.10 Answer to the lead's question, and what GP/L2 do not cover
**Answer: YES on 𝒞_glob.** (R2) in the form its consumers use — the S_E-slice response in the global chart, transport-weighted field norm
(residual weight L^{(1+θ)q}, i.e. ALIGN55's ♯ weight at σ = θ), sources in N (or the weaker N^{(θ)}), unweighted and (given (H2)_m, (H3)_m) with
e^{m·dist} weights — follows from Proposition L2 + Lemma N1-L + Lemma CONV-P, **with no alignment, no Λ_HC, no (AC𝒞), and no (HD) beyond the
banked K^{(σ)} Lipschitz bound.** The GA route (ALIGN55 + Λ_HC) is therefore a **backup** on 𝒞_glob; §2 below records its status at backup depth.
**What GP/L2 do not cover (precise):**
1. *Covariant orbit form.* (𝔐^∇_Z, N_Z) restatement needs Lemma NE + the chart part of CONV — ARGUED (OFFGLOB55 §4.3); not needed on 𝒞_glob.
2. *N_res* is not in ‖·‖_{(θ)} (§1.5).
3. *Positive-level divergence sources* G_l (l ≥ 1) — outside L2's source functional; not generated by TOWER-VAR consumers (§1.5).
4. *Weights:* L2_m needs (H3)_m (ARGUED) and the (H2)_m pieces at their Codex-conditional status; rate m ≤ m_Y.
5. *Off 𝒞_glob:* GP-R2 is m = 0 only and frame-local (OFFGLOB55: "weighted versions would follow from the weighted local estimates … — not
   done"); its local inputs (W-comm)^σ, W-mult^σ, CONV (frame/chart part), (ND), RG/FP are ARGUED; CODEX_REVIEW_OFFGLOB (as on disk 04:41Z) has
   corrected CCL_U's G-slot sign and its constant's domain (F4: "C_loc ≤ 221 + (324√2/n)η_F + 2592η_ρ" — the printed 221 + O(n^{−1}) silently set
   η_F = 2, valid only on a small frame ball) and has not yet reached L1/L2. **On 𝒞_glob, L2 does not depend on GP or on any frame lemma.**
6. *Inputs 1-3 are conditional on the lane-A linear package* (N24 of ASSEMBLY55) — shared by every route, including GA.

### 1.11 Check a2_55_conv (record)
Criteria `checks/a2_55_conv_criteria.md` written 04:52:47Z, before the script `checks/a2_55_conv.py` (written 04:53:39Z). **One run**, 04:53:39-
04:53:43Z, `nice -n 10 python3 -I -B`, Fractions/ints only, 0.34 s, 17.4 MB (`checks/a2_55_conv_out.txt`; `checks/a2_55_conv_err.txt` = start stamp +
/usr/bin/time report). No criterion edited. **I1, I2, II1, II2 PASS; CI1-CI3 and CII1-CII3 all FIRE; OVERALL PASS.** Part I verifies the exact split
K′_X(a, c) = −[X, λ̄] − ½Φ(ad_X)δ against the definition d/dt log(e^{ta}e^Xe^{−tc}) in a nilpotent Lie algebra (strictly upper-triangular 6×6, where
exp/log are finite and the identity is the universal formal one); Part II verifies the G_0-slot decomposition (point charges [G, dȳ] at plaquette
bases + ⟨w_A, dλ⟩) exactly on the d = 4, side-3 torus with su(2) ≅ (ℝ³, ×), and the coefficient mass 2(d − 1) = 6 per link (min = max = 6). *Cannot
decide* (stated before running): any norm or routing bound, k/T-uniformity, the s-slot, su(N) beyond the universal formula.

*Erratum to §1.8 (constant C_H).* Read **C_H := ‖H‖_{𝔐^{(σ)}→N^{(σ)}} ≤ 2 + κ_+** (Wilson part: G_0 = du_0, G^c_0 = f_0(u), ‖f_0‖ + [f_0]_α ≤ 2‖u‖_{(σ)};
soft part: s_l = κ_lr_l(u), ‖s‖_{R(σ)} ≤ κ_+‖u‖_{(σ)}); the printed "≤ 2 + 2[·]-Hölder terms + κ_+" is garbled. Nothing else changes.

### 1.12 Reconciliation with CODEX_REVIEW_OFFGLOB F5/F11 and the lead's 05:0xZ instruction (read 05:03Z; the file now ends with its banking list)
CODEX_REVIEW_OFFGLOB item 4 banks L1/L2 "CONDITIONAL … from the corrected full-ball K/GV estimates, CCP and Faddeev–Popov transversality. This is
a genuine limited no-alignment mechanism. It does not supply the missing covariant/full-source comparisons", and F11 ("This does not retire
ALIGN55"). **I agree with F5 and F11**, and the lead's instruction stands: the alignment programme stays on the critical path (§3 below). To avoid
duplication, the exact division of labour is:
- **Covered by the L2 route (§1.2-§1.9), nothing more to do there:** (R2)(a) (N1-nd) on 𝒞_glob — with Lemma N1-L it needs **no** Faddeev–Popov
  transversality (Codex F5's third premise is removable; F5's sign correction ΓK_y = +1 + ΓK′_y is then moot); (R2)(b) in slice form, global log
  chart, σ-pair, for sources with (G_0; s; j) representations — with CONV-P (§1.4) the G_0- and s-slot completions are now proved, which Codex F11
  noted L2 (c) did not supply; at σ = θ the bound is also in terms of N (§1.5: N^{(θ)} ≤ C_NN on such representations — Codex F11's own
  inequality); m > 0 conditional on (H2)_m, (H3)_m.
- **Not covered by L2 — the complement the alignment programme must deliver (or a separate lemma):** (i) sources whose N-representations need
  **positive-level divergence slots G_l (l ≥ 1)**; (ii) **N_res** of the response; (iii) the **covariant** restatement (𝔐^∇_Z/N_Z) — needs a chart
  comparison; (iv) anything off 𝒞_glob. Codex F11 lists (i)-(iii) in the same words.
- **One correction to the division, found below (§3.1):** the alignment programme *as ALIGN55 set it up* (GA in the left-trivialised chart, flat
  ♯ on the input side, covariant ♯ on the output side) **cannot** deliver (iii) or anything else: its chart comparison (NC) is false and t_+ grows
  like L^{θ(k−1)}η for Λ_HC. The repaired programme runs GA in the **log chart** (§3.2), where (HD) holds at all orders in the full (♯ → N) pair from
  banked per-level estimates (§3.3) — and there it covers (i)-(ii) through RW♯ (which is in the full pair), which is the non-duplicating job.

## 2. The alignment programme (critical path, per the lead's 05:0xZ message): a chart obstruction, its repair, (HD), and a local alignment

### 2.1 Proposition CW (chart witness). PROVEN-HERE — (NC) is false in ALIGN55's pair, and t_+(Υ_HC) grows like L^{θ(k−1)}η
ALIGN55 runs Theorem GA with the **left-trivialised** chart at Z: Υ_W = 1 − (Ξ_Z − Ξ_1)Λ_W, input norm the flat |||·|||_{1,♯} (residuals r_l),
output norm the covariant |||·|||_{Z,♯} (ALIGN55 §1: "the covariant versions (transported differences, r^Z)", r^Z_l = the linearisation at Z of
the soft residual, BFT_B §12.0), and (NC) |||w|||_{Z,♯} ≤ (1 + C_NCη)|||w|||_{1,♯} is assumed (ALIGN55 §2, "(NC)"; §4, "(NC), (HD) on
S_E-representatives"; §7 row 12).
> **Proposition CW.** Let k ≥ 2, θ > 0, N ≥ 2; fix a direction ν and unit ŷ, ĉ ∈ su(N) with [ŷ, ĉ] ≠ 0, and η ∈ (0, η_W]. Data: B := ηŷ on every
> level-k ν-link, 0 on the others (V := e^B; flat, in 𝒞_glob(η) ∩ 𝒦(ε) for every ε > 0). Let Z = Z(V) be the BFT-E critical point (the S_E
> representative of the constant configuration ȳ^{const}_j := L^{j−k}ηŷ on level-j ν-links). Let w be the **constant chain** w_j := L^{j−k}ĉ on
> level-j ν-links (j < k), 0 elsewhere, w_k = 0. Then:
> (a) |||w|||_{1,♯} = 2 and [w]_{1,♯} ≤ 2 (all flat residuals r_j(w), j ≤ k − 2, vanish; N_res(w) = 0; ‖w^c_j‖ = 1; top residual 1);
> (b) **[w]_{Z,♯} ≥ |||(r^Z_0 leg)||| ≥ ((L − 1)/(2L))·L^{θ(k−1)}·η·|[ŷ, ĉ]|·(1 − C_Lη)**, C_L depending only on L (and on EP-bd's C_Π);
> (c) Λ_HCw = 0 and Λ_LPw = 0 (§2.4), so Υ_HCw = Υ_LPw = w and **t_+(Υ_HC), t_+(Υ_LP) ≥ ((L − 1)/(4L))·L^{θ(k−1)}·η·|[ŷ, ĉ]|·(1 − C_Lη)**;
> (d) in particular **(NC) fails** (on w itself, and on its S_E representative Π_Ew, by the cycle argument in the proof), for every θ > 0.

*Proof.* **Step 1 (the background).** All plaquettes of ȳ^{const} are 1 (only ν-links are nontrivial and they are constant) and every S4′ average
equals its link (M̄ = e^{Lȳ_j} on ν-links, 1 on others: §2.1 Step 3 below), so ρ ≡ 0: ȳ^{const} is a global minimiser, hence critical. Everything
lies in the abelian subalgebra ℝŷ, where the composite gauge action is additive; so the S_E representative is ȳ_E := ŷ⊗Π_Eφ (φ the scalar
constant chain, Π_E the abelian S_E projection; λ_E ∈ Λ_* leaves the data unchanged), ‖ȳ_E‖_{𝔐^∇} ≤ C_Πη (EP-bd, CODEX_REVIEW_GSHARP item 1), and
by BFT-E's uniqueness in its slice ball (C_0 ≥ C_Π) Z = e^{ȳ_E}. ρ(Z) = 0 (gauge covariance of ρ). Write ȳ_E = ŷ⊗(φ + dλ) with λ the scalar
gauge function (own |dλ| ≤ C_Πρ_jη on level-j links, coarse C^{1,α}-bounded).
**Step 2 (the exact linearisation at Z).** For a coarse level-(l+1) link c with S4′ contours T = T^σ_y (LINEAR_PACKAGE §1.2), let P_T(t) be the
contour product of the perturbed links e^{tw(b)}Z(b). By a2_55_nc N1, (d/dt P_T)(0)P_T(0)^{−1} = Σ_{b∈T}±Ad_{A_b}w(b) with A_b the prefix
holonomy (times Z(b)^{−1} for reversed links). Since all P_T(0) are equal (ρ(Z) = 0 and Z is gauge-equivalent to the constant field, whose
contour products coincide), M̄(t) = (1 + t·avg_TΣ±Ad_{A_b}w(b) + O(t²))P(0); its SU(N) maximiser moves by the anti-Hermitian first-order part
(Codex KOFF §4.2: "δW₀ = Qδx" at M ∈ SU(N)), and V(t) = (1 + tw_{l+1}(c))P(0). Hence, exactly to first order in t,
  **r^Z_l(w)(c) = Ad_{P(0)^{−1}}[ avg_T Σ_{b∈T} ± Ad_{A_b}w(b) − w_{l+1}(c) ] = Ad_{P(0)^{−1}}[ r_l(w)(c) + avg_TΣ_{b∈T}±(Ad_{A_b} − 1)w(b) ].**
**Step 3 (the first contour moment).** The background is abelian, so Ad_{A_b} = e^{a_b·ad_ŷ} with a_b the scalar holonomy of the prefix; for the
constant part a_b = h_b·φ_l (h_b the lower ν-height of b relative to c_X, own φ_l = ρ_lη), and the pure-gauge part telescopes:
a_b = h_bφ_l + λ(x_b) − λ(c_X) (x_b the prefix endpoint). By a2_55_nc N2 (exact, all σ and y, (d, L) ∈ {(2,3), (2,5), (4,3)}; the identity is the
three-line sum below for every d, L): **Σ_{ν-steps of T}(±1)·h_b = L(L−1)/2 for every contour of a ν-link, and the (sign, h) multiset cancels exactly
on contours of μ-links, μ ≠ ν** (leg 1 forward over heights 0..d−1 gives d(d−1)/2, the straight leg Ld + L(L−1)/2, the reversed translated leg
−(dL + d(d−1)/2); d < 0 likewise). Since w is supported on ν-links and constant there,
  r^Z_l(w)(c) = Ad[ Σ_p (1/p!)·(avg_TΣ_{ν-steps}±a_b^p)·ad_ŷ^p(w_l) ],  the p = 1 term being **(L(L−1)/2)·(φ_l + ∂λ)·[ŷ, w_l]** + O(L³ρ_l²‖∇²λ‖)
on ν-links c (∂λ := the local value of dλ_ν), and 0 on μ ≠ ν links when λ ≡ 0.
**Step 4 (the cycle average; this handles the S_E representative).** Along any level-l ν-cycle the λ-terms telescope, so the average over the
cycle's coarse links C of the p = 1 coefficient equals (L(L−1)/2)φ_l exactly, up to the smoothness error O(L³ρ_l‖∇^cλ^c‖·ρ_l) (relative O(Lρ_lC_Π)).
Hence **sup_C|r^Z_l(w)(C)| ≥ (L(L−1)/2)·ρ_lη·|[ŷ, w_l]|·(1 − C_Lη)** (p ≥ 2 terms are relatively O(Lρ_lη)). At l = 0 with |w_0| = ρ_0 (own):
own ≥ (L(L−1)/2)ρ_0²η|[ŷ,ĉ]|; coarse ×L^{k−1}; ♯ weight ×L^{(1+θ)(k−1)}; with ρ_0 = L^{−k} the product is ((L−1)/(2L))L^{θ(k−1)}η|[ŷ,ĉ]|(1 − C_Lη).
**Step 5 (gauge invariance of the bound).** r^Z_l(Ξ_Zμ) = ±[μ(c_Y), ρ_l(Z)] = 0 (ρ(Z) = 0; CODEX_REVIEW_BGT §4's covariance), so every element of
the covariant class [w]_Z has the same r^Z_0-leg: (b). (a) is direct. (c): d*w_l = 0 so μ_l = −(1 − S_0R)Δ_l^{−1}d_l^*w_l = 0 (Λ_HC); w is affine, so
M_lw_l = 0 (Λ_LP, §2.4, checked a2_55_lp B1); thus Υ_Ww = w and t_+ ≥ [w]_{Z,♯}/[w]_{1,♯}. (d): (b) with |||w|||_{Z,♯} ≥ [w]_{Z,♯}; for x_E := Π_Ew the
flat class is the same and the same cycle-average argument applies to every representative with bounded coarse gradient (EP-bd). ∎
**Reading.** A chain that is constant in the left-trivialised chart is *rotating* relative to the background's parallel transport; its residual —
a second-order quantity in the RG sense — is ρ_{l+1}²η in own units, which the flat ♯ norm does not see and the covariant ♯ norm weights by
L^{(2+θ)q}. The same witness in the **log chart** has *zero* covariant residual: in log coordinates the constant chain u gives contour products
e^{L(ȳ+tu)} = e^{ȳ_{l+1}+tu_{l+1}} exactly, so Dρ(ȳ)u = 0. **The defect is the chart, not GA and not (R2)** — (R2) itself holds at this Z by local
gauge covariance. At σ = 0 (plain 𝔐^∇ weights L^{k−1−j}) the same computation gives ((L−1)/(2L))η, bounded: the obstruction is specific to the ♯
weight that BGT55 §6.3 (F-♯) introduced to tame the S2 term — **the left-trivialised GA route is squeezed between S2's level count at θ = 0 and CW's
L^{θ(k−1)} at θ > 0.**
**Consequences.** (i) ALIGN55 §2/§4/§7 row 12's (NC) is REFUTED; (ii) RED′'s t_+ cannot be realised with Λ_HC (or Λ_LP, or any Λ_W that kills the
constant chain) in that chart; (iii) ALIGN55 Theorem R2-glob♯ — banked by CODEX_REVIEW_ALIGN item 5 "as the repaired implication from its full uniform
inputs" — has a false input (row 12, (NC)), so as an implication it stands but **cannot be instantiated**; BGT55 Theorem R2-glob (same chart) likewise.
(iv) Whether some other Λ_W (one that does not kill harmonic constant chains, at the cost of roughness) rescues the left-trivialised t_+ is
NOT-VERIFIED; the residual/curvature trade-off sketched in my notes suggests not, but I did not prove it.

### 2.2 Lemma RED″ (GA in the log chart). PROVEN-HERE (exact algebra; it is RED′ with Codex ALIGN F1's correction, transplanted)
Chart map: a left-trivialised tangent vector w at Z = e^ȳ ↦ log-chart vector 𝒥w, 𝒥 := ψ_−(ad_ȳ) link-wise (d/dt log(e^{tw}e^ȳ) = ψ_−(ad_ȳ)w, the c = 0
case of §1.4 Step 1). Then **𝒥Ξ_Z = −K_ȳ** and, at a critical point, **H_Z = 𝒥^TH^{log}_ȳ𝒥**. Put D′ := −K_ȳ − Ξ_1 = −K′_ȳ, **Υ′ := 1 − D′Λ_W = 1 + K′_ȳΛ_W**,
**Υ := 𝒥^{−1}Υ′**, and for a log-chart source f the **log twisted charge τ′(f) := Ξ_1^Tf** (= K′^T_ȳf when K_ȳ^Tf = 0).
> **RED″.** Assume (P1′) ‖Λ_Wx‖_𝒞 ≤ C_𝒞|||x|||_{1,♯}; (E); **(AC)_log** |||K′_ȳμ|||_{1,♯} ≤ C_ACη‖μ‖_𝒞; **(P2-tw)_log** N_1(Λ_W^Tτ′(f)) ≤ C_twη·N_1(f) for
> every log-chart f with K_ȳ^Tf = 0; **(HD)_log** N_1((H^{log}_ȳ − H)x) ≤ C_HDη|||x|||_{1,♯}; **(FW)_log** N_1(H^{log}_ȳx) ≤ C_FW|||x|||_{1,♯}; and, only
> to express the output in covariant norms, **(NC)_log** |||𝒥^{−1}v|||_{Z,♯} ≤ (1 + C_NCη)|||v|||_{1,♯} and **(CV)_log** N_1(𝒥^{−T}S) ≤ (1 + C_CVη)N_Z(S).
> If C_𝒞C_ACη < 1, then Υ is invertible, ΥΞ_1 = Ξ_Z, Υ^TH_ZΥ = Υ′^TH^{log}_ȳΥ′, and Theorem GA's hypotheses hold with
>   **t_+ ≤ (1 + C_NCη)C_E(1 + C_ACC_𝒞η),  t_* ≤ (1 + C_CVη)(1 + C_twη),  δ_Υ ≤ ηC_E[C_HD + C_twC_FW + C_FWC_ACC_𝒞(1 + C_twη)].**
*Proof.* Υ′Ξ_1 = Ξ_1 + K′_ȳΛ_WΞ_1 = Ξ_1 − K′_ȳ = −K_ȳ, so ΥΞ_1 = 𝒥^{−1}(−K_ȳ) = Ξ_Z; Υ^TH_ZΥ = Υ′^T𝒥^{−T}𝒥^TH^{log}𝒥𝒥^{−1}Υ′ = Υ′^TH^{log}Υ′. For any source g,
Υ′^Tg = g + Λ_W^TK′^T_ȳg, and K′^T_ȳ = Ξ_1^T + K^T_ȳ, so **Υ′^Tg = Π_W^Tg whenever K_ȳ^Tg = 0** — in particular for g = 𝒥^{−T}S (S ∈ cc_Z: ⟨𝒥^{−T}S, K_ȳλ⟩ =
−⟨S, Ξ_Zλ⟩ = 0) and for g = H^{log}_ȳv (K^T_ȳH^{log}_ȳ = 0 at a critical point). (t_+) As in RED′ with u := K′_ȳΛ_Wx_E: [Υx]_Z = [𝒥^{−1}(x_E + u)]_Z.
(t_*) Υ^TS = Π_W^T(𝒥^{−T}S) = 𝒥^{−T}S + Λ_W^Tτ′(𝒥^{−T}S). (δ_Υ) E_Υ := Υ′^TH^{log}Υ′ − H kills Ran Ξ_1 (H^{log}K_ȳ = 0, HΞ_1 = 0), so E_Υx = E_Υx_E =
Π_W^TH^{log}(x_E + u) − Hx_E = (H^{log} − H)x_E + Λ_W^Tτ′(H^{log}x_E) + H^{log}u + Λ_W^Tτ′(H^{log}u), using Ξ_1^TH = 0 and Ξ_1^TH^{log}x_E = τ′(H^{log}x_E) — the
four terms of Codex ALIGN F1 with the charge correctly attached to H^{log}x_E (not to (H^{log} − H)x_E). Invertibility: Υ′ = 1 + K′Λ_W with
‖Λ_WK′_ȳμ‖_𝒞 ≤ C_𝒞C_ACη‖μ‖_𝒞 < ‖μ‖_𝒞 (Codex ALIGN F1's direct argument). ∎
**What changes against RED′:** (NC) and (CV) move to the *last* step (output conversion) and are needed in their log-chart form, which CW does not
touch (§2.1 Reading: Dρ(ȳ)u = 0 on the witness in log coordinates); (HD) becomes (HD)_log, which §2.3 proves from banked estimates.
**Status of the conversion lemmas.** (NC)_log: the covariant residual of 𝒥^{−1}v is Dρ_l(ȳ)v = r_l(v) + δ_l(ȳ)v, and the CEN2 structure (BA-4, PROVEN)
gives |δ_l(ȳ)v| ≲ p_L²[|ȳ_l|osc_N(v_l) + osc_N(ȳ_l)|v_l|] + O(L³|ȳ|²|v|), i.e. ♯-weighted ≲ p_L²L^{(θ−1)q−2}η‖v‖ (the computation of §2.5 (ii) below with
μ ↦ v) — **ARGUED**; the transported-difference legs are O(η) rotations along axial paths of coarse length ≤ 1 — ARGUED; covariant N_res — ARGUED.
(CV)_log: the chart part of OFFGLOB55's CONV in the N pair — **ARGUED**.

### 2.3 (HD)_log at all orders, in the full (♯ → N) pair — PROVEN as an implication of CODEX_REVIEW_KOFF §4.3 (Codex ALIGN's "most dangerous" item)
(H^{log}_y − H)x = −D𝔑^0(y)x (𝔑^0 = Hy − NB − ∇F). Codex KOFF §4.3 proves, at all orders and with the homogeneous-data difference norm δ = ‖x − x′‖_{(σ)},
the per-level bounds (its (1)-(3) and the Wilson paragraph): Wilson ‖G^c_0‖_∞ + [G^c_0]_α ≤ Cη², π_0(j_W) + [(j_W)^c]^∞_α ≤ Cη²; soft plain rows
**π_l(κ_lE_l|_l) + π_{l+1}(κ_lE_l|_{l+1}) ≤ C′L^{−σm}η²** (m = k − 1 − l); residual-type L^{(2+σ)m}|κ_l(Ψ_l − r_l)| ≤ Cη²; each with the difference
bound "Cηδ" (resp. C′L^{−σm}ηδ). Letting x′ → x along a direction (δ → 0) gives the same bounds for D𝔑^0(y)u with η² → η‖u‖_{(σ)}. Read these in N:
G_0 slot ✓; P0 slot π_0 ✓; **Pc slot** max_{l≥1}L^{θ(k−l)}π_l ≤ 2C′L^σ·max_lL^{(θ−σ)(k−l)}η‖u‖ ≤ 2C′L^ση‖u‖ for **θ ≤ σ** (both E_l|_l and E_{l−1}|_l land
at level l); **R slot** ‖s‖_R = L^θmax_lL^{(1+θ)m}‖s^c_l‖ ≤ L^θ‖s‖_{R(σ)} ≤ L^θCη‖u‖ (θ ≤ σ); Y slot: G at level 0 only. With σ = θ and ‖u‖_{(θ)} ≤
|||u|||_{1,♯} (§1.5): **N_1((H^{log}_y − H)u) ≤ C_HD·η·|||u|||_{1,♯}, C_HD := C + 2C′L^θ + L^θC, all orders, k-, T-uniform.** The constants are Codex's
"finite constants C" (existence proved there; values not computed). **Verdict:** Codex ALIGN's most dangerous unverified item — "row 12's all-order
(HD) estimate in the actual sharp/source norms and background chart" — is **CONFIRMED-by-banked-input in the log chart**; in the left-trivialised
chart it is not needed (that chart is already obstructed by CW at t_+), and there the chart term (𝒥^TH^{log}𝒥 − H^{log})w carries CW's residual: on the
constant chain its natural s-slot representation costs ≍ L^θ·L^{θ(k−1)}η (a lower bound for the infimum N_1 is NOT-VERIFIED).
(FW)_log: H^{log} = H + (H^{log} − H); N_1(Hv) ≤ ‖f_0(v)‖ + [f_0(v)]_α + κ_+L^θ·max_lL^{(1+θ)m}‖r^c_l(v)‖ ≤ (2 + κ_+L^θ)|||v|||_{1,♯} (the s-slot needs the ♯
residual leg: ALIGN55 §2's remark, CONFIRMED). So **C_FW ≤ 2 + κ_+L^θ + C_HDη — PROVEN** (given §2.3).

### 2.4 Λ_LP — the hierarchical local-path alignment (a finite-range replacement for Λ_HC's Coulomb detail). Algebra PROVEN-HERE; detail bound PROVEN-HERE
*Definition.* S_0 = the tensor product of a 1D L-adic interpolatory scheme (RS_0 = 1, weights a(y, Y), Σ_Ya = 1). For each level-l site y and each Y with
a(y, Y) ≠ 0 fix the **axial lattice path γ(Y → y)** (coordinates in the fixed order 1, …, d). **M_lx_l(y) := Σ_Y a(y, Y)·∫_{γ(Y→y)}x_l**, μ_l := −M_lx_l,
λ_k := 0, λ_l := S_0λ_{l+1} + μ_l, **Λ_LPx := λ_0** — ALIGN55's Λ_HC with the Coulomb detail −(1 − S_0R)Δ_l^{−1}d_l^*x_l replaced by a path average.
> **Lemma LP-1 (algebra).** (i) **M_l∘d = 1 − S_0R** on level-l functions, for ANY choice of paths (∫_γdν = ν(y) − ν(Y), Σ_Ya = 1); (ii) M_lx vanishes at
> level-(l+1) sites (a(y, ·) = δ_y there, empty path), so Rλ_l = λ_{l+1}: nested restriction ev^{(l)}Λ_LPx = λ_l, Λ_LPx ∈ Λ_*; (iii) (H): λ_l depends on
> x_l, …, x_{k−1} only; (iv) **Λ_LPΞ_1 = −1** (as HC-1 (iii), using (i)); (v) transpose: c_m = −M_m^TS^{(m→0)T}q, and M_m^TR^T = (RM_m)^T = 0, so level-l
> charges are completed at levels ≥ l only; (vi) **finite range**: M_lx(y) reads x_l only on links within ℓ^∞-distance D_s of y, D_s := the largest
> |y − Y|_∞ with a(y, Y) ≠ 0 (= 6 level-l steps for s3, L = 3), so the response of λ_0 to x_m is supported within coarse distance
> 6ρ_m·L/(L − 1) (s3) — **uniformly in k**.
*Proof.* One line each as indicated (HC-1's proof verbatim for (ii)-(v), with (i) in place of "Δ^{−1}d*dν = ν − mean"). ∎
> **Lemma LP-2 (detail bound — the DET of the brief, with no Green's function).** Let s reproduce polynomials of degree ≤ p per coordinate (s3: p = 3).
> (a) **M_l annihilates every 1-form whose components are polynomials of degree ≤ p − 1** in the base-point coordinates (exactly; with axial paths in
> a fixed order and tensor-product weights). (b) Hence, for every level-l 1-form with coarse gradient Hölder seminorm [∇^cx^c_l]^∞_α,
>   **sup|μ_l| ≤ C_D·ρ_{l+1}^{2+α}·[∇^cx^c_l]^∞_α,  C_D := A_s·(D_1/L)^{2+α}**, A_s := sup_yΣ_Y|a(y, Y)| (= (11/9)^d for s3), D_1 := max|y − Y|_1 + 1 (≤ 6d + 1);
> and if x^c_l ∈ C^{2,α}, sup|μ_l| ≤ C′_Dρ_{l+1}^{3+α}[∇²x^c]_α (p = 3).
*Proof.* (a) Along the axis-μ segment of γ(Y→y) (other coordinates fixed at (y_<μ, Y_>μ)), the discrete sum of a degree-(p−1) polynomial is a polynomial of
degree ≤ p in Y_μ and ≤ p − 1 in each Y_ν, ν > μ; so ∫_{γ(Y→y)}x =: Φ(Y) has per-coordinate degree ≤ p, and Σ_Ya(y, Y)Φ(Y) = Φ(y) (tensor reproduction) =
∫ over the empty path = 0. (b) Subtract the first-order Taylor field P_y of x^c at y (componentwise, discrete gradients at the links of y); M_lP_y = 0 by (a);
for every link b of γ(Y→y), |x(b) − P_y(b)| ≤ ρ_l(|b − y|_1ρ_l)^{1+α}[∇^cx^c]^∞_α (telescoping along an ℓ¹ path, each step's gradient within
[·]^∞_α·dist^α of the one at y); sum over ≤ D_1 links and over Y with weights |a|: sup|μ_l| ≤ A_sD_1(D_1ρ_l)^{1+α}ρ_l[∇]^∞_α = A_s(D_1/L)^{2+α}ρ_{l+1}^{2+α}[∇]^∞_α. ∎
At d = 4, L = 3 (s3): A_s = (11/9)⁴ = 14641/6561, D_1/L ≤ 25/3: C_D ≤ 2.24·(25/3)^{2+α}. Campanato → pointwise as in §1.4 step 0 (factor C_CH).
**Comparison with Λ_HC (ALIGN55 Lemma DET).** Same order ρ_{l+1}^{2+α} — but proved by Taylor expansion alone: **no lattice Green's-function bound,
no periodisation or zero-mode bookkeeping, no harmonic-remainder limit** (Codex ALIGN F7's three DET obligations do not arise), and **finite
range** instead of r^{−7} tails (Codex ALIGN F7: the weighted conclusion "correctly stays OPEN" for Λ_HC; for Λ_LP it is not an issue).
**Check a2_55_lp (record).** Criteria `checks/a2_55_lp_criteria.md` written 04:59:12Z; **Amendment A1** (05:00:40Z) written **before the script existed**
(reason in the file: the pre-registered A5 asserted a k-independent radius, contradicting the geometric down-propagation tail, and miscounted R_pred
with T = 4 < 2R_pred; replaced by "radius ≤ 6ρ_mL/(L − 1) on T = 8"). Script `checks/a2_55_lp.py` written 05:01:46Z; **one run** 05:01:5x-05:02:25Z,
`nice -n 10 python3 -I -B`, Fractions only, 10.5 s, 63 MB (`checks/a2_55_lp_out.txt`, `checks/a2_55_lp_err.txt`). Results: **A1, A2, A3, A4, A1r PASS;
A5 PASS (radii 20/9 at k = 2, 65/27 at k = 3, bound 3); B1 PASS; B2 FAIL; C1, C2, C3 PASS; CB1, CB2, CB3, CC1 all FIRE; OVERALL FAIL (by the
registered rule, because of B2).** **B2's failure, exactly:** the pre-registered expectation was a nonzero ρ_1³ detail for a quadratic coarse field
with ratio 1/27 between depths; the measured detail is **0 at both depths** (ratio undefined). The prediction was wrong in the favourable direction:
Lemma LP-2 (a) — written after the run, from this outcome — shows s3's per-coordinate *cubic* reproduction makes M_l annihilate all polynomial
fields of degree ≤ 2, so the first nonzero detail is the cubic one (ρ_{l+1}^{4}). I record B2 as a FAIL of the gate as registered and do **not**
re-register it; the conclusion drawn from it (degree-2 annihilation) is supported by the proof of LP-2 (a), not by a passing gate. With linear
interpolation (CB3) the ratio is 1211/8073 (≠ 1/27): the gate does discriminate. What the PASSes decide: exact left inverse (for axial and for
random paths), nested restriction, (H), transpose locality, k-uniform finite range (two depths), exact affine annihilation and its dependence on
cubic reproduction (CB1) and on axial-in-fixed-order paths (CB2); spline nesting (C1) and its non-triviality (CC1).

### 2.5 (AC)_log and (P2-tw)_log for Λ_LP — mechanisms and power counts (ARGUED, with the one new identity PROVEN-HERE)
**(AC)_log** |||K′_ȳμ|||_{1,♯} ≤ C_ACη‖μ‖_𝒞. By §1.4 Step 1, (K′_ȳμ)_l(b) = −[ȳ_l(b), μ̄(b)] − ½Φ(ad_{ȳ_l(b)})dμ(b) exactly. (i) 𝔐^∇ legs: coarse
|(K′μ)^c_l| ≤ 2‖ȳ^c_l‖‖μ‖_∞ ≤ 2η‖μ‖_𝒞, gradient/Hölder legs by the product rule (ȳ ∈ C^{1,α}, μ ∈ C^{1,θ} ⊂ C^{1,α}) — routine. (ii) residual leg:
r_l(K′μ) = r_l(K_ȳμ) = ±[μ(c_Y), ρ_l(ȳ)] + δ_l(ȳ)[Ξ_1μ] − δ_l(ȳ)[K′μ]. The first is ≤ 2‖μ‖L^{−(2+σ)q}(η + C_ρη²) own (♯-bounded for θ ≤ σ); the last is
second order. The middle term is ALIGN55 §4's delicate one: by CEN2 (BA-4, polarised) |δ_l(ȳ)[dμ]| ≤ Cp_L²[|ȳ_l|osc_N(dμ_l) + osc_N(ȳ_l)|dμ_l|] + O(L³|ȳ|²|dμ|),
with own |ȳ_l| ≤ ρ_lη, osc_N(ȳ_l) ≤ 2ρ_lρ_{l+1}η, |dμ_l| ≤ ρ_l‖μ‖_𝒞, osc_N(dμ_l) ≤ ρ_l(2ρ_{l+1})^θ‖μ‖_𝒞; coarse ×L^q, ♯ weight ×L^{(1+θ)q}:
**≤ 3·2^θCp_L²L^{−2}η‖μ‖_𝒞, uniform in q exactly because the Hölder exponent of ∇μ is θ** (ALIGN55's observation, re-derived; Codex ALIGN F4's L^{−4}
vs L^{−2} prefactor bookkeeping only changes the constant). (iii) N_res(K′μ): the residual above has coarse size ≲ L^{−(1+θ)q−2}η‖μ‖, varies at scale
ρ_{l+1}, so its coarse C^{1,α} norm is ≲ L^{(α−θ)q−2}η‖μ‖, summable over q **because α < θ**. **Status: ARGUED** (power counts complete; the CEN2
polarised remainder and the level-(l+1) part are the lane's BA-4/Codex-KOFF §4.3 local analytic constants).
**(P2-tw)_log** N_1(Λ_LP^Tτ′(f)) ≤ C_twη N_1(f). The charge τ′(f) = K′^T_ȳf decomposes slot by slot exactly as in §1.4 Steps 2-4 (point charges of
own size ≤ a at level-l sites; divergences d^Tw of level-l currents). Completion c_m = −M_m^TQ_m, Q_m := S^{(m→0)T}q, m ≥ l (LP-1 (v)).
(A) *Point charges.* own |Q_m| ≤ A_1L^{d(m−l)}a (A_1 := sup‖S^{(m→l)}‖_{1→1}L^{−d(m−l)}), |M_m^TQ| ≤ A_M·max|Q| (A_M := sup_bΣ_{(y,Y): b∈γ(Y→y)}|a(y,Y)| <
∞, finite range), so π_m(c_m) ≤ A_MA_1L^{3(k−m)}L^{d(m−l)}a. With §1.4's sizes (G_0: a ≤ 2d(d−1)n^{−4}η‖G^c_0‖, l = 0; j: a ≤ 4dρ_lη·L^{−3(k−l)}π_l(j_l);
s: at level l + 1, a ≤ 2d|ρ_l||s_l|) the weighted costs are ≤ C·L^{−(1−θ)(k−m)}η×(the slot's N-size), and the sum over input levels l ≤ m is geometric
(Codex ALIGN F7's "sums over all input levels", e.g. Σ_{l≤m}L^{−(1−θ)(k−m)}L^{−θ(k−l)}‖j‖_Pc ≤ ‖j‖_Pc/(1 − L^{−θ})). ARGUED-routine.
(B) *Divergences — the representation that avoids Pc growth (new identity, PROVEN-HERE).* For q = d^Tw at level l: by the commuting pair
(S_0^Td^T = d^TS_1^T, BFT_B Construction CP; al55_hcg H8), Q_m = d^Tw_m with **w_m := S_1^{(m→l)T}w**. On exact forms dM_m = d(1 − S_0R) = 1 − S_1Q_m (root
covariance Q∘d = d∘ev); M_m and 1 − S_1Q_m both annihilate constant 1-forms; hence **dM_m = 1 − S_1Q_m + Ñ_m∘d** with Ñ_m local (it vanishes on closed
forms). Transposing and using S_1^Tw_m = w_{m+1}:
  **Σ_{m≥l}c_m = −w_l + Σ_{m=l}^{k−1}(Q_m^Ts_m − s_m) − Σ_{m≥l}d^TG′_m,  s_m := w_{m+1},  G′_m := Ñ_m^Tw_m,**
i.e. as a source x ↦ −⟨w, x_l⟩ + Σ_m⟨s_m, r_m(x)⟩ − Σ_m⟨G′_m, dx_m⟩ (the m = k − 1 pairing with x_k = 0 drops). **The completion of a divergence is one plain
current at its own level plus residual-type and positive-level divergence slots** — not plain currents at every level m ≥ l (whose Pc weights
L^{θ(k−m)} would grow: e.g. a level-0 divergence routed upward costs L^{θ(k−1)}π_0 in Pc). Sizes: with own |w_m| ≤ C_{S1}L^{(d−1)(m−l)}|w|,
‖s‖_R = max_mL^{θ(k−m)}L^{k−1−m}‖s^c_m‖ ≤ C_{S1}L^θπ_l(w) and ω_m‖G′^c_m‖ ≤ A_ÑC_{S1}L^{−(1−θ)(k−m)}π_l(w): **k-uniform**. Status: the identity is exact
(PROVEN-HERE; the three facts used are CP, root covariance and LP-1 (i)); the size bounds need C_{S1} := sup_n‖S_1^{(n)}‖_{1→1}L^{−(d−1)n} < ∞ (uniform
stability of the derived scheme — Codex ALIGN F7's named missing bound; for spline subdivision it is the total variation of the spline interpolant of
a step, finite) and the Campanato seminorm of G′_m (ARGUED). **(P2-tw)_log(Λ_LP): ARGUED, every mechanism named, no k-growth found.**
**(P1′)(Λ_LP)** = LP-2 + HB (§2.6).

### 2.6 SUB for every odd L, and HB with explicit constants (spline instance)
**SUB for every L, without computation: periodic cubic-spline subdivision.** S_0^{spl}v := samples at the level-l sites of the periodic tensor-product
cubic-spline interpolant (knots at the level-(l+1) sites) of v. Since splines with coarser knots are splines with finer knots and periodic cubic
interpolation is unique (circulant (1/6, 4/6, 1/6), eigenvalues (2 + cos θ)/3 ≥ 1/3 > 0), **S^{(m→l)} = samples at level l of the level-m interpolant**
(nesting; exact check a2_55_lp C1 for (L, M) = (3, 4), (5, 3), (3, 3); C3 invertibility M = 1..8; CC1 shows DD-type schemes do not nest). It is
interpolatory, reproduces cubics per coordinate (locally; on the torus up to wrap terms O(N³r^{N/2}), r := 2 − √3, N = the level-(m+1) side ≥ T, hence
k-uniform and → 0 as T → ∞ — ARGUED bookkeeping), and its basis functions are samples of one C² function: the cardinal spline L(t) = Σ_ic_iB_3(t − i),
c_i = √3(√3 − 2)^{|i|}, Σ|c_i| = 3 exactly. With Σ_jB_3 ≡ 1, Σ_j|B_3′| ≤ 2, Σ_j|B_3″| ≤ 4: the 1D Lebesgue constants are **Λ_0 ≤ 3, Λ_1 ≤ 6, Λ_2 ≤ 12**
(units of the knot spacing); in d dimensions Λ_0 ≤ 3^d, first partials ≤ 6·3^{d−1}, second ≤ 12·3^{d−1} (pure), 36·3^{d−2} (mixed): **81, 162, 324, 324 at d = 4**.
Exponential locality: |c_i| decays like (2 − √3)^{|i|}, i.e. rate ln(2 + √3) = 1.3169 per knot spacing ≥ 1.3169 per coarse unit at every level.
> **Lemma HB (spline). PROVEN-HERE** (on the infinite lattice; torus wrap terms as stated above). If sup|μ_m| ≤ Mρ_{m+1}^{2+α} for all m ≥ l, then
> λ_l := Σ_{m≥l}S^{(m→l)}μ_m obeys, uniformly in k and l:
>   **sup|λ_l| ≤ 3^dM·L^{2+α}/(L^{2+α} − 1),  ‖∇^cλ_l‖_∞ ≤ 6·3^{d−1}M·L^{2+α}/(L^{1+α} − 1),  [∇^cλ_l]^∞_θ ≤ M·L^{2+α}[12·3^{d−1}/(1 − L^{−α}) + 12·3^{d−1}/(1 − L^{−1−α})]**
> for every θ ∈ (0, 1].
*Proof.* λ_l = samples of Λ := Σ_{m≥l}Σ_Yμ_m(Y)L^{⊗d}((x − Y)/ρ_m); discrete gradients are segment averages of ∂Λ and discrete Hölder quotients are
bounded by continuum ones. ‖∂Λ‖ ≤ Σ_mMρ_{m+1}^{2+α}·6·3^{d−1}ρ_m^{−1} = 6·3^{d−1}ML^{2+α}Σ_mρ_m^{1+α}; at separation h ≤ 1: the levels with ρ_m ≥ h contribute
≤ Mρ_{m+1}^{2+α}·Λ_2ρ_m^{−2}h, summing to ≤ ML^{2+α}Λ_2h/(1 − L^{−α}); those with ρ_m < h contribute ≤ 2Mρ_{m+1}^{2+α}Λ_1ρ_m^{−1}, summing to
≤ 2ML^{2+α}Λ_1h^{1+α}/(1 − L^{−1−α}); divide by h^θ ≤ 1·h^{θ}… (h^{1−θ} ≤ 1, h^{1+α−θ} ≤ 1) and use Λ_1 ≤ 6·3^{d−1}, Λ_2 ≤ 12·3^{d−1}. ∎
> **Proposition P1′(LP). PROVEN** for the spline instance on the infinite-lattice model (LP-2 + HB), **ARGUED** on the torus (wrap terms), every odd L ≥ 3,
> every 0 < α < θ ≤ 1: ‖Λ_LPx‖_𝒞 ≤ C_D·C_HB·C_CH·max_m[∇^cx^c_m]_α ≤ C_𝒞·|||x|||_{1,♯}, C_𝒞 explicit from the displays (k-, T-uniform).
(LP-2 with spline weights: A_s ≤ 3^d, and the |y − Y| moments Σ|a|·|y − Y|^{2+α} are finite by the exponential decay; the finite-range statement LP-1 (vi)
becomes exponential locality.) **The s3 instance (L = 3, finite range)** needs HB from the certified contraction ‖S_c^7‖ (β ≥ 289/500, Codex ALIGN F5) plus the
stable finite-level reconstruction bounds Codex F7 lists as missing — NOT-VERIFIED here. **L = 5 with the 4-point DD scheme**: Codex ALIGN F5's exact
values (norm²·5^5 = 51447766041/30517578125 at n = 5) give ‖S_c^5‖^{1/5} ≤ 5^{−0.4676}, i.e. a certified C^{1,β} with β ≥ 0.4676 — enough for θ < 0.4676;
P3 failed only because it asked β > 1/2 (my reading of the registered numbers; the β value is my arithmetic: β = (1/5)·log_5(5^{20}/51447766041)/2·… —
NOT re-run as a check). **"Show L = 3 suffices":** a grep of PROOF.md, PLAN_S26.md, HANDOFF.md, SMALLNESS_DAG.md, FLOW55.md, UIR55.md found one L-largeness
requirement, PROOF.md "Lemma H1 (one step from i.i.d. Haar)" ("The range L ≥ 5 below is for SU(2) only … it is vacuous at L = 3"), a session-4 strong-coupling
bound, and the remark "Balaban takes L sufficiently large [m]" (PROOF "S1 Lattice"); whether Lemma H1 is on the live route I did not determine
(NOT-VERIFIED). With the spline instance the question is moot for the alignment: SUB holds for every odd L.

### 2.7 Λ_HC itself — status
ALIGN55's Λ_HC: algebra banked (CODEX_REVIEW_ALIGN item 3). Its DET needs the d = 4 lattice Green's-function derivative bounds with periodisation and
the affine-annihilation limit (Codex ALIGN F7) — **I did not rebuild them (NOT-VERIFIED)**: Λ_LP has the same algebra, the same ρ^{2+α} detail bound by
Taylor expansion alone, and finite range, so on the repaired (log-chart) route Λ_HC is dominated by Λ_LP. **In ALIGN55's left-trivialised formulation
Λ_HC fails (A1) outright** (Proposition CW (c)). The brief's items 1-2 for Λ_HC proper therefore stay open but are off the critical path.

*Errata to §2.6 (written 05:2xZ).* (1) The L = 5 sentence's formula "β = (1/5)·log_5(5^{20}/51447766041)/2·…" is garbled; the correct statement, now
checked exactly (a2_55_beta, below): with ‖S_c^5‖² = 51447766041/5^{20} (Codex ALIGN F5's value), **β = 23/50 is certified** (51447766041^5 < 5^{77}) and
β = 47/100 is not (51447766041^{10} > 5^{153}); so the 5-adic 4-point DD scheme is certified C^{1,β} for β ≥ 0.46 (not 0.4676), enough for θ < 0.46.
(2) In the HB proof, "divide by h^θ ≤ 1·h^{θ}…" should read: divide by h^θ and use h^{1−θ} ≤ 1 and h^{1+α−θ} ≤ 1 for h ≤ 1.

### 2.8 Theorem R2-full-log (the alignment route, repaired). PROVEN as an implication; inputs and statuses
> **Theorem R2-full-log.** Fix d = 4, odd L ≥ 3, N, κ_±, 0 < α < θ ≤ 1, σ := θ. On 𝒞_glob(ε), ε ≤ ε_b, at the BFT-E critical point ȳ (Z = e^ȳ): with
> Λ_W = Λ_LP (spline or s3 instance), Theorem GA applied to Υ := 𝒥^{−1}(1 + K′_ȳΛ_LP) gives (N1-nd) at Z and **[x]_{Z,♯} ≤ t_+t_*C_♯(1 − C_♯δ_Υ)^{−1}·N_Z(S)**
> for every S ∈ cc_Z — the full (R2)(b) in ALIGN55's pair, **including N's positive-level divergence slots and the N_res leg** (through RW♯, which is in that
> pair) — provided the inputs below hold, with t_±, δ_Υ from RED″.

| # | input | status (file, locating string) |
|---|---|---|
| 1 | BFT-E critical point, BFT-1 sizes | CODEX_REVIEW_GV item 4 + KOFF item 5: CONFIRMED, conditionally (lane-A package) |
| 2 | (B_1♯) = Corollary RW♯ | CODEX_REVIEW_BGT banked item 5 (as used by CODEX_REVIEW_ALIGN item 5): CONFIRMED |
| 3 | Theorem GA | CODEX_REVIEW_BGT item 1: CONFIRMED |
| 4 | RED″ (§2.2) | PROVEN-HERE (exact algebra; Codex ALIGN F1's corrected four terms) |
| 5 | (E) S_E reference | CODEX_REVIEW_GSHARP item 1 (as in CODEX_REVIEW_ALIGN F9 row 5): CONDITIONAL input |
| 6 | (HD)_log, (FW)_log | §2.3: PROVEN as an implication of CODEX_REVIEW_KOFF §4.3 (1)-(3) + Wilson (items 3-5, conditional) |
| 7 | Λ_LP algebra, finite range | §2.4 LP-1: PROVEN-HERE (a2_55_lp A1-A5, A1r PASS) |
| 8 | (P1′)(Λ_LP) | §2.4 LP-2 PROVEN-HERE + §2.6 HB(spline) PROVEN-HERE on the infinite lattice; torus wrap terms ARGUED; s3 instance's HB NOT-VERIFIED |
| 9 | (AC)_log | §2.5: ARGUED (CEN2 power count; Codex ALIGN F4 prefactor) |
| 10 | (P2-tw)_log(Λ_LP) | §2.5: ARGUED (slot charges PROVEN-HERE in §1.4; divergence-representation identity PROVEN-HERE; C_{S1} and G′ Campanato ARGUED) |
| 11 | (NC)_log, (CV)_log (output conversion only) | §2.2: ARGUED |
| 12 | TR-1 at ȳ (enters (AC)_log through ρ(ȳ)) | as CODEX_REVIEW_ALIGN F9 row 10: CONDITIONAL input |
| 13 | smallness C_𝒞C_ACη < 1, C_♯δ_Υ < 1 | holds for ε ≤ ε_b once 1-12 hold (Codex ALIGN F9's parameter choice, verbatim) |
**Not claimed:** any ARGUED row as proven; weighted versions (the GA route with m > 0 needs weighted RW♯ = (R3) and weighted rows 6-11; Λ_LP's finite
range makes every *local* row weight-stable, but this was not written); anything off 𝒞_glob.
**Division of labour with §1 (no duplication):** for sources with (G_0; s; j) representations and the σ = θ field norm without N_res, Theorem
R2-glob-L (§1.9) already gives (R2) on 𝒞_glob with **only banked inputs + CONV-P** and no alignment; Theorem R2-full-log is needed **only** for (i)
positive-level G_l slots, (ii) N_res, (iii) the covariant restatement — and it shares (iii)'s conversion lemmas (row 11) with any covariant reading of §1.
Rows 9-11 are the remaining analytic work of the alignment programme; rows 6 and 8 are closed at the level stated.

### 2.9 Checks a2_55_nc and a2_55_beta (records)
- **a2_55_nc.** Criteria `checks/a2_55_nc_criteria.md` written 05:13:51Z, before the script `checks/a2_55_nc.py`; one run 05:14:2xZ, `nice -n 10 python3 -I -B`,
  Fractions/ints only, 0.15 s, 16.4 MB (`checks/a2_55_nc_out.txt`, `_err.txt`). **N1 PASS, N2 PASS (d, L) ∈ {(2,3), (2,5), (4,3)}, CN1 and CN2 FIRE; OVERALL
  PASS.** Disclosure: the criteria file's CN2 paragraph contains a struck-through first idea ("… is NOT used as a pass/fail control; instead **CN2:** …"); the
  operative CN2 is the upper-height variant, as the script implements. Decides: the prefix rule of left-trivialised path derivatives (incl. reversed
  links) and the exact first contour moment L(L−1)/2 / exact cancellation for the S4′ family. Cannot decide: W_0's first-order variation (taken from Codex
  KOFF §4.2), any norm, any k-dependence.
- **a2_55_beta.** Criteria `checks/a2_55_beta_criteria.md` written 05:22:36Z, then the 6-line script; one run; **B1 PASS, CB FIRES, OVERALL PASS** (exact
  integers). Its input (51447766041/5^{20}) is Codex ALIGN F5's value, not recomputed.

## 3. Findings on prior claims (verdict; file + locating string; reason)
- **G1. OFFGLOB55 "4.1 Lemma L1" — CONFIRMED** on Ker Γ (§1.2): the slice-ball Lipschitz bound suffices; the "full ball vs slice ball" scope note is moot for L2.
- **G2. OFFGLOB55 "4.2 Proposition L2" (a) — CONFIRMED** (§1.2; CCP (d)'s argument applied to the representation P^TD^⊥g).
- **G3. OFFGLOB55 L2 (b) "If ΓK_ȳ is invertible on Λ_* (NSL55 (f) …)" — conclusion CONFIRMED, hypothesis unnecessary** (Lemma N1-L, §1.3: dimension count +
  injectivity of K_ȳ by connectivity). Agree with CODEX_REVIEW_OFFGLOB F5's sign correction (+1 + ΓK′), which N1-L no longer needs.
- **G4. OFFGLOB55 L2 (c) — CONFIRMED** (CCP (c) verbatim; 127.44 = 3186/25 as Codex certified).
- **G5. OFFGLOB55 "Lemma CONV … G- and s-slots ARGUED" — completion part PROVEN-HERE (Lemma CONV-P, §1.4); chart part (J_y^T) NOT-VERIFIED.**
- **G6. OFFGLOB55 "Lemma NE … ARGUED" — NOT-VERIFIED**, and not needed for (R2) on 𝒞_glob (§1.7).
- **G7. OFFGLOB55 §4.2 "(a)-(b) are (R2)(a)-(b) in slice form … with no alignment Υ" — CONFIRMED in scope** (σ = θ pair, (G_0; s; j) sources, no N_res, no
  covariant form; §1.5, §1.10, §1.12).
- **G8. OFFGLOB55 §10 item 2 "ALIGN55's GA route … is not superseded — the two pairs differ" — CONFIRMED**, and sharpened by CW (§2.1).
- **G9. ALIGN55 §2 "(NC) |||w|||_{Z,♯} ≤ (1 + C_NCη)|||w|||_{1,♯} (all w)" and §4/§7 row 12 "(NC) … on S_E representatives" — REFUTED** (Proposition CW:
  ratio ≥ ((L−1)/(4L))L^{θ(k−1)}η|[ŷ,ĉ]|(1 − C_Lη) on the constant chain at the S_E representative of a flat abelian-direction background). Correct
  statement: (NC) holds in the **log chart** ((NC)_log, ARGUED via CEN2) and fails in the left-trivialised chart for every θ > 0.
- **G10. ALIGN55 "Lemma RED′ … t_+ ≤ (1 + C_NCη)C_E + C_ACC_𝒞C_Eη" instantiated with Λ_HC — REFUTED** (CW (c): t_+(Υ_HC) ≥ c·L^{θ(k−1)}η). RED′ as an algebraic
  implication stays (CODEX_REVIEW_ALIGN item 1; agree); its hypothesis (NC) is false. Correct route: RED″ (§2.2, log chart).
- **G11. ALIGN55 "Theorem R2-glob♯ … PROVEN-HERE as a reduction" — CONFIRMED as an implication (agree CODEX_REVIEW_ALIGN item 5); NOT instantiable** (row 12's
  (NC) false). Replaced by Theorem R2-full-log (§2.8) and, for its σ-pair part, Theorem R2-glob-L (§1.9).
- **G12. ALIGN55 "Lemma DET (detail size). ARGUED (complete except the cited lattice Green's-function bounds)" — NOT-VERIFIED** (Green bounds not rebuilt;
  Codex ALIGN F7's periodisation/zero-mode/affine-limit obligations stand). The same bound for Λ_LP: PROVEN-HERE (LP-2).
- **G13. ALIGN55 "Lemma HB … ARGUED-standard" — CONFIRMED for spline subdivision** (PROVEN-HERE with explicit constants, §2.6; torus wrap terms ARGUED);
  NOT-VERIFIED for s3 (needs the stable reconstruction bounds Codex F7 lists).
- **G14. ALIGN55 "Proposition P1′(HC). ARGUED" — NOT-VERIFIED** (DET missing). For Λ_LP: PROVEN (spline, infinite lattice), ARGUED (torus).
- **G15. ALIGN55 "Proposition P2-tw(HC)" G-slot line "the weighted cost is ≤ CL^{θ(k−l)}|z^c_l||G^c_l| ≤ Cη‖G‖_Y" — REFUTED at l = 0 as printed**: ω_0 = 1 (BFT_A §7.2
  "ω_0 := 1"), while completing a level-0 divergence into plain currents at level 1 costs Pc weight L^{θ(k−1)}. Correct statement: complete it in the
  representation of §2.5 (B) (one plain current at its own level + residual-type s_m = w_{m+1} + positive-level G′_m), cost ≤ C_{S1}(1 + L^θ + A_Ñ)π_l(w).
- **G16. ALIGN55 §6.3 (v) "an exponentially local detail rule that keeps the exact left-inverse property is OPEN" — REFUTED as open**: Λ_LP (§2.4) keeps the
  exact left inverse and has finite range (s3) or exponential range (spline). ALIGN55's reasons ("(Δ + M)^{−1} breaks Λ_HCΞ_1 = −1; a partition-of-unity
  interpolation loses Π_1 reproduction") are correct for those two candidates only (agree with Codex ALIGN F7's remark).
- **G17. ALIGN55 §6.1 "For odd L ≠ 3 the scheme input (SUB) is not certified here" — CONFIRMED as recorded status; superseded**: spline SUB for every L (exact
  nesting, a2_55_lp C1-C3) and the 5-adic DD scheme certified β ≥ 23/50 from Codex's own numbers (a2_55_beta).
- **G18. ALIGN55 §4 "(AC𝒞) is ARGUED (power count, every input named) … uniform in q exactly because the Hölder exponent of ∇μ equals θ" — CONFIRMED in mechanism**
  (re-derived in log form, §2.5), NOT-VERIFIED as a proof; agree with Codex ALIGN F4's prefactor correction.
- **G19. ALIGN55 §11 item 4 "HANDOFF critical path for (R2) on 𝒞_glob: rebuild DET's d = 4 lattice Green's-function bounds; write HB's constants; prove the
  completion bounds (A)-(B); re-derive (HD)'s term list" — superseded** (§6 below): DET not needed (LP-2), HB written (spline), (HD) from banked inputs in the
  log chart, and a prior step — the chart — was wrong.
- **G20. BGT55 §6.1 "H_Z = J(z)^TH(z)J(z) … absorbed into Υ" — CONFIRMED as the necessary move**; ALIGN55's Υ_W = 1 − (Ξ_Z − Ξ_1)Λ_W does not absorb J, which is
  exactly CW's defect.

## 4. Codex verdicts used — agree or disagree, explicitly (files as on disk: CODEX_REVIEW_ALIGN complete at 05:0xZ with banking list; CODEX_REVIEW_OFFGLOB complete
## at 05:03Z with banking list; KOFF, GV, BFT34, BGT complete)
- **CODEX_REVIEW_ALIGN** items 1 (RED′ algebra, corrected identity), 2 (DW/LC/NEC), 3 (HC-1), 4 (L = 3 certificate, axial facts): **agree.** Item 5 (R2-glob♯ as an
  implication): **agree as an implication; I add that its row-12 input (NC) is false (G9), so it cannot be instantiated.** "Most dangerous unverified item: row
  12's all-order (HD)": **agree it was unverified; disagree on the ranking** — row 12's (NC) is false, and (HD) itself follows from banked KOFF estimates once the
  chart is the log chart (§2.3). F7's G_l line: **disagree at l = 0** (G15). F7's weights remark and F5: **agree.** F4 (AC prefactor L^{−4}): **agree.**
- **CODEX_REVIEW_OFFGLOB** F5 (L1/L2 confirmed as matched-input implication; ΓK sign): **agree; the FP-transversality premise is removable (G3).** F11 (does not retire
  ALIGN55; pairs differ; positive-level G_l and N_res not supplied): **agree**, with CONV-P now supplying the G_0/s completion F11 says L2 (c) did not. Banking item 4:
  **agree.** F4 (CCL_U sign; C_loc's η_F): **agree** (not used on 𝒞_glob).
- **CODEX_REVIEW_KOFF** items 1-5 and §4.3 (1)-(3): **agree**; they are the inputs of §1 and §2.3 (I did not re-prove them).
- **CODEX_REVIEW_GV** items 1, 2, 4, 6: **agree**; used. **CODEX_REVIEW_BFT34** item 1: **agree**; L2_m uses exactly its premises.
- **CODEX_REVIEW_BGT** items 1, 4, 5: **agree**; used (GA, KER_Z, RW♯).

## 5. Summary tables

### 5.1 Results of this file (status words; none has had a Codex check)
| id | statement (section) | status |
|---|---|---|
| R1 | Lemma L1 on Ker Γ; Prop. L2 (a), (c) re-derived (§1.2) | CONFIRMED as implications of banked conditional inputs |
| R2 | Lemma N1-L: (N1-nd) at ȳ without Faddeev–Popov transversality (§1.3) | PROVEN-HERE |
| R3 | Lemma CONV-P: cc-completion of G_0-, s-, j-slots costs O(η) in N^{(σ)}; exact split K′_X(a,c) = −[X, λ̄] − ½Φ(ad_X)δ (§1.4) | PROVEN-HERE (G, j explicit; s via fixed-polydisc Cauchy constant); a2_55_conv PASS |
| R4 | N^{(θ)} ≤ C_N·N on (G_0; s; j) representations; ‖·‖_{(θ)} ⊇ 𝔐^∇ + ♯ residual leg, ⊉ N_res (§1.5) | PROVEN-HERE |
| R5 | L2_m: weighted slice response from (H2)_m + (H3)_m (§1.6) | PROVEN as an implication ((H3)_m ARGUED upstream) |
| R6 | (HD) on the L2 route = banked K^{(σ)} Lipschitz bound; un-projected form via CONV-P (§1.8) | CONFIRMED-by-banked-input |
| R7 | **Theorem R2-glob-L**: (R2)(a)-(b) on 𝒞_glob, slice form, σ = θ pair, (G_0; s; j) sources, no alignment (§1.9) | PROVEN as an implication (inputs: banked conditional + R2, R3, R4) |
| R8 | **Proposition CW**: (NC) false; t_+(Υ_HC), t_+(Υ_LP) ≥ ((L−1)/(4L))L^{θ(k−1)}η\|[ŷ,ĉ]\|(1 − C_Lη) in ALIGN55's left-trivialised ♯ pair (§2.1) | PROVEN-HERE (a2_55_nc PASS for its two algebraic facts) |
| R9 | **Lemma RED″**: GA in the log chart, Υ = 𝒥^{−1}(1 + K′_ȳΛ_W), explicit t_±, δ_Υ (§2.2) | PROVEN-HERE (algebra) |
| R10 | **(HD)_log** at all orders in the full (♯ → N) pair; (FW)_log (§2.3) | PROVEN as an implication of CODEX_REVIEW_KOFF §4.3 |
| R11 | Λ_LP: exact hierarchical left inverse, nested restriction, (H), level-local transpose, finite range (§2.4 LP-1) | PROVEN-HERE (a2_55_lp A1-A5, A1r PASS) |
| R12 | LP-2: M_l annihilates polynomial 1-forms of degree ≤ p − 1; sup\|μ_l\| ≤ C_Dρ_{l+1}^{2+α}[∇^cx^c_l]_α with no Green's function (§2.4) | PROVEN-HERE (B1 PASS; B2 FAIL as registered — the detail is 0, stronger than predicted) |
| R13 | divergence-completion identity: Σc_m = −w_l + Σ(Q^Ts_m − s_m) − Σd^TG′_m (§2.5 (B)) | PROVEN-HERE (identity); sizes ARGUED |
| R14 | (AC)_log, (P2-tw)_log for Λ_LP (§2.5) | ARGUED (mechanisms and power counts complete) |
| R15 | spline SUB for every L (nesting), Lebesgue constants 3, 6, 12 (§2.6) | PROVEN-HERE (a2_55_lp C1-C3 PASS, CC1 FIRES) |
| R16 | Lemma HB (spline), explicit constants; P1′(LP) (§2.6) | PROVEN-HERE (infinite lattice); torus wrap terms ARGUED |
| R17 | 5-adic 4-point DD scheme certified C^{1,β}, β ≥ 23/50 (§2.6 errata) | CERTIFIED from Codex's numbers (a2_55_beta PASS) |
| R18 | **Theorem R2-full-log**: full (R2)(b) in ALIGN55's pair via the log-chart GA with Λ_LP (§2.8) | PROVEN as an implication; rows 9-11 ARGUED |
| R19 | d = 4 lattice Green's-function bounds; DET for Λ_HC (brief items 1-2 for Λ_HC proper) | NOT ATTEMPTED → NOT-VERIFIED (off the critical path: R12) |

### 5.2 Verdicts on prior claims (§3)
| id | claim (file, locating string) | verdict |
|---|---|---|
| G1 | OFFGLOB55 "4.1 Lemma L1" | CONFIRMED (slice scope) |
| G2 | OFFGLOB55 "4.2 Proposition L2" (a) | CONFIRMED |
| G3 | OFFGLOB55 L2 (b) "If ΓK_ȳ is invertible" | CONFIRMED (hypothesis unnecessary) |
| G4 | OFFGLOB55 L2 (c) | CONFIRMED |
| G5 | OFFGLOB55 "Lemma CONV … G- and s-slots ARGUED" | completion part CONFIRMED (proved: CONV-P); chart part NOT-VERIFIED |
| G6 | OFFGLOB55 "Lemma NE … ARGUED" | NOT-VERIFIED (not needed on 𝒞_glob) |
| G7 | OFFGLOB55 §4.2 "(a)-(b) are (R2)(a)-(b) in slice form" | CONFIRMED in scope |
| G8 | OFFGLOB55 §10 item 2 "GA route … not superseded" | CONFIRMED |
| G9 | ALIGN55 "(NC) \|\|\|w\|\|\|_{Z,♯} ≤ (1 + C_NCη)\|\|\|w\|\|\|_{1,♯}" (§2, §4, §7 row 12) | **REFUTED** (Prop. CW) |
| G10 | ALIGN55 RED′ t_+ bound instantiated with Λ_HC | **REFUTED** (CW (c)) |
| G11 | ALIGN55 "Theorem R2-glob♯" | CONFIRMED as implication; not instantiable (input false) |
| G12 | ALIGN55 "Lemma DET" | NOT-VERIFIED |
| G13 | ALIGN55 "Lemma HB … ARGUED-standard" | CONFIRMED for spline subdivision; NOT-VERIFIED for s3 |
| G14 | ALIGN55 "Proposition P1′(HC)" | NOT-VERIFIED |
| G15 | ALIGN55 P2-tw(HC) G-slot "weighted cost ≤ CL^{θ(k−l)}\|z^c_l\|\|G^c_l\| ≤ Cη‖G‖_Y" at l = 0 | **REFUTED** as printed (ω_0 = 1); corrected via §2.5 (B) |
| G16 | ALIGN55 §6.3 (v) "an exponentially local detail rule … is OPEN" | **REFUTED** as open (Λ_LP) |
| G17 | ALIGN55 "(SUB) is not certified here" for L ≠ 3 | CONFIRMED as status; superseded |
| G18 | ALIGN55 §4 (AC𝒞) power count | CONFIRMED in mechanism; NOT-VERIFIED as proof |
| G19 | ALIGN55 §11 item 4 critical-path list | superseded |
| G20 | BGT55 §6.1 "J(z) … absorbed into Υ" | CONFIRMED (and ALIGN55 did not implement it) |
**Counts (§5.2): CONFIRMED 11 (G1, G2, G3, G4, G7, G8, G11, G13, G17, G18, G20), NOT-VERIFIED 4 (G6, G12, G14, and G5's chart part — counted with G5 as
CONFIRMED for its completion part), REFUTED 4 (G9, G10, G15, G16), superseded 1 (G19).** (G5 is split: completion CONFIRMED/proved, chart NOT-VERIFIED;
I count it under CONFIRMED and list its NOT-VERIFIED half in the text.)

### 5.3 Outcome against the PRE-STATED targets and refutation tests
- **T0:** answered in two passes. First (§1, before the lead's 05:0xZ message): L2 + N1-L + CONV-P give (R2) on 𝒞_glob in slice form without alignment.
  Second (§1.12, after Codex OFFGLOB F5/F11): that is exactly the *limited* mechanism Codex banks; the complement (positive-level G_l sources, N_res,
  covariant form) needs the alignment route, which stays on the critical path — in its repaired log-chart form (§2.2-§2.8).
- **T1:** the d = 4 Green's-function bounds were **not** rebuilt (NOT-VERIFIED); they are not needed for the local-path alignment (LP-2).
- **T2:** DET's bound is proved for Λ_LP by Taylor expansion (LP-2); HB is proved with explicit constants for spline subdivision; (P1′) follows (R16).
- **T3:** SUB holds for every odd L via spline subdivision (exact nesting), and the 5-adic DD scheme is certified β ≥ 23/50; "L = 3 suffices" not settled
  (one L ≥ 5 requirement found in PROOF's session-4 Lemma H1; its liveness not checked).
- **T4:** completion bounds: point charges routine; divergences need the residual-type representation (R13), which removes the Pc growth that sinks
  ALIGN55's printed G-slot line at l = 0 (G15); weighted: Λ_LP is finite-range/exponentially local — the weighted obstruction of Λ_HC's r^{−7} tail does not arise.
- **T5:** (HD) in the log chart follows at all orders from banked per-level estimates (R10); in ALIGN55's left-trivialised chart the decisive failure is
  earlier, at (NC)/t_+ (R8).
- **T6:** Theorem R2-glob-L (σ-pair, banked inputs) and Theorem R2-full-log (full pair, rows 9-11 ARGUED).
- **Refutation tests:** R2 (a C^{1,α} field with large Coulomb detail) — not found; R3 (‖Λx‖_𝒞 growing) — not found for Λ_LP; **R6-type finding:** a k-dependence
  where uniformity was claimed — **found**: (NC)/t_+ in ALIGN55's chart (R8). R1, R4, R5: no counterexample found.

*Erratum to §5.2's count line (the printed line is self-contradictory).* Clean count of the 20 rows: **CONFIRMED 12** (G1, G2, G3, G4, G5, G7, G8, G11, G13,
G17, G18, G20 — of which G5, G13, G18 have a NOT-VERIFIED half stated in their rows), **NOT-VERIFIED 3** (G6, G12, G14), **REFUTED 4** (G9, G10, G15, G16),
**superseded 1** (G19).

## 6. For the lead (nothing here is banked; Codex first)
1. **The alignment route as ALIGN55 set it up is obstructed (first-class, PROVEN-HERE):** Proposition CW — at the BFT-E critical point of flat
   abelian-direction data (B = ηŷ on level-k ν-links) the constant chain has flat ♯ norm 2 and covariant ♯ norm ≥ ((L−1)/(2L))L^{θ(k−1)}η|[ŷ,ĉ]|, so (NC)
   is false and t_+(Υ_HC) ≥ ((L−1)/(4L))L^{θ(k−1)}η|[ŷ,ĉ]|. **PROOF/HANDOFF should not list "ALIGN55 R2-glob♯ (Codex item 5)" as an instantiable route**: it is a
   valid implication with a false input (row 12). The cause is the chart (left-trivialised Υ without the dexp map), not GA or (R2).
2. **Repair (PROVEN-HERE as algebra): run GA in the log chart** — Υ = 𝒥^{−1}(1 + K′_ȳΛ_W) (Lemma RED″). There Codex ALIGN's "most dangerous" item (HD) is
   **CONFIRMED-by-banked-input at all orders in the full (♯ → N) pair** from CODEX_REVIEW_KOFF §4.3's per-level estimates (σ = θ).
3. **Use Λ_LP (local-path detail) instead of Λ_HC:** same algebra (exact left inverse, (H), level-local transpose — checked exactly), the DET bound by Taylor
   expansion alone (no Green's functions: brief items 1-2 dissolve for the alignment), finite range (s3) / exponential range (spline) — the weighted
   question is answered positively — and SUB for every odd L via spline subdivision (exact nesting; HB with explicit constants).
4. **Division of labour (Codex OFFGLOB F11 + this file):** the L2 route already gives (R2)(a)-(b) on 𝒞_glob for (G_0; s; j) sources in the σ = θ pair with
   banked inputs + N1-L + CONV-P (no alignment, no NSL, no FP transversality). The alignment route is needed only for positive-level G_l sources, N_res and
   the covariant restatement. **Remaining analytic work on the alignment route: (AC)_log, (P2-tw)_log [mechanisms complete, ARGUED], (NC)_log/(CV)_log
   [output conversion, ARGUED], the torus wrap terms of spline HB, C_{S1}.**
5. **Suggested Codex order:** (a) Proposition CW (short; decisive for ALIGN55's route); (b) Lemmas N1-L and CONV-P (they upgrade Codex OFFGLOB item 4);
   (c) RED″ + §2.3; (d) LP-1/LP-2 + HB(spline).
6. **Tally:** PROOF's 105-item tally not read or changed. HANDOFF row "BFT-5 (b) background transfer": replace "needs an actual alignment with uniform
   quotient/source/defect bounds" by "σ-pair (R2) on 𝒞_glob: L2 + N1-L + CONV-P (ALIGN2_55 §1.9, pending Codex); full-pair (R2): log-chart GA with Λ_LP (ALIGN2_55
   §2.8; rows 9-11 ARGUED); ALIGN55's left-trivialised GA is obstructed (ALIGN2_55 Prop. CW)".

Files written by this worker: ALIGN2_55.md; checks/a2_55_conv_criteria.md, a2_55_conv.py, a2_55_conv_out.txt, a2_55_conv_err.txt; checks/a2_55_lp_criteria.md
(with Amendment A1), a2_55_lp.py, a2_55_lp_out.txt, a2_55_lp_err.txt; checks/a2_55_nc_criteria.md, a2_55_nc.py, a2_55_nc_out.txt, a2_55_nc_err.txt;
checks/a2_55_beta_criteria.md, a2_55_beta.py, a2_55_beta_out.txt, a2_55_beta_err.txt. No git command was run. The arXiv corpus was not consulted (not needed for
any step above; nothing attributed to Dimock or Balaban here).
UTC end stamp: 2026-10-29T05:25:57Z

*Erratum to §2.1 "Reading" (final read, 05:2xZ).* "(R2) itself holds at this Z by local gauge covariance" is stronger than what I proved. What is proved:
this Z is a BFT-E critical point on 𝒞_glob, so **Theorem R2-glob-L (§1.9) gives (R2)(a)-(b) there in the σ = θ slice form** (as an implication of its
inputs); the covariant-norm form at this Z is not proved here. The witness shows only that ALIGN55's *chart comparison* fails, not that (R2) fails.
UTC stamp of this erratum: 2026-10-29T05:27Z.
