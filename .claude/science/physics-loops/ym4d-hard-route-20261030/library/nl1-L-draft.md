# NL1 input (L): the walk-interpolated presentation of the step-i exponent in the free complex fluctuation — pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, pass 1 of input (L) of submanuscript NL1 (the exact nonlinear step) in our proof of T0. Research text. It is not an audit, it grants no status, and no other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

No step rests on a computation. Every argument is a composition of holomorphic maps between open sets of finite-dimensional complex spaces, a one-variable Schwarz lemma (with a zero of order k), the triangle inequality for seminorms, a finite geometric count, or a comparison of explicit powers of log θ. Each is meant to be Lean-formalisable.

Credit. The substitution design (real factor fixed, stored coordinates fixed, pinned regional response, half-gap admission, localisation by cube switches) is ST1's (`library/st1-r2.md`, Codex distillation of Claude drafts). The architecture it serves is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the outline `ym4.tex` ("SA"), with its radius system, response brackets, window formation and walk localisation; the complete account ("CA-II"); and the three-dimensional manuscript `YM3_I.tex` ("Y3"), whose field polydisc and s̄-product are the 3D analogues used here. The renormalisation-group step, the operator 𝐂, the windows, the δ-elimination factors and the strip are Tadeusz Balaban's (CMP 109 (1987) 249; 116 (1988) 1; 119 (1988) 243; 122 (1989) 175, 355). Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions.

Line references. **PAN L** = `library/pan-draft.md`; **ST1 L** = `library/st1-r2.md` (the distilled ST1; its definitions are binding here); **ST1d2 L** = `library/st1-draft2.md`; **IN1 L** = `library/in1-draft.md`; **C4 L** = `library/c4-order.md`; **AS L** = `library/ym4-assembly.md`; **TT L** = `library/ag1-tt-draft.md`; **SA L** = `scratchpad/sa/ym4.tex`; **CA-II L** = `scratchpad/sa/ca_II.tex`; **Y3 L** = `scratchpad/sa/YM3_I.tex`. **ST3 L** = `library/st1-draft3.md` (ST1 round 3, pass-1 long draft by Claude, not distilled; it amends `st1-r2.md` and arrived during this session). Every cited range was read in this session, in bounded ranges; a few SA ranges are cited as PAN or ST1 read them, and are marked so. Source text is paraphrased with line numbers; quotations are a few words. ST1 here means `st1-r2.md` with the round-3 amendments of ST3 §6 (ST3 L394–410); its Theorem 14 is the round-2 form of ST1d2 Theorem 1 (ST1d2 L40–62).

Status words: **[proved]** = proved here by hand from the stated inputs; **[input: NAME, owner]** = a statement another submanuscript must supply, stated exactly; **[reading]** = my reading of an owner's text, flagged for the owner; **[design]** = a choice of the construction; **[Outstanding]** = not proved.

---

## 0. Result

**(L) is proved, as an implication** (Theorem L, §8), for all seven kinds of PAN §3, from named inputs: the hypotheses of ST1 Theorem 14 at the main step; ST1's regional response DR read on its complex source ball (DR-ζ) with its component splitting stated row by row (DR-loc); Balaban's main-step change of variables (FL-main); NL1/LF1's activity interface on ST1's domains; Balaban's non-quadratic remainder (W-in); and LF1's island bound (I-8). Nothing of (L)'s own is left Outstanding.

**One design change is needed, and it is necessary.** ST1 uses the simplified radius table r_ι(m) = α_ιε_m (ST1 L92, L99; ST1d2 L130), whose radii scale like θ^{−1/2}(log θ)^{𝔭₀}, the scale of the fluctuation threshold. Under that table the radius claim of (L) is not available from the interface: Proposition C (§3.2) exhibits an activity that satisfies every clause of ST1's activity interface and whose presentation cannot extend beyond |ζ|_∞ ≈ C(log θ)^{𝔭₀+2r}, which is below c_R(log θ)^q. The fix is SA's own table (Tq): r_ι(m) := α_{ι,m} = C_ιθ_m^{−1/2}(log θ_m)^q (SA L6033; IN1 L44). Lemma T (§3.3) proves that every lemma and theorem of ST1 holds verbatim under (Tq), after one floor of row 5 becomes a ceiling on γ.

**The extension (task 2).** Theorem V (§5) extends ST1 Theorem 14 at the main step from the scalar z on the actual source to the free complex fluctuation ζ, coordinate by coordinate, with complex walk parameters. The real factor and the stored coordinates stay fixed. The argument goes through the proof of Theorem 14, not its statement: the response is nonlinear in its source, so a scalar multiple of the actual response is not the response to a complex fluctuation (§11, route A1).

**Two construction points (§4).** (i) The source is *masked*: the fluctuation on a cube Δ enters as s_Δζ. This makes the locality (L3) exact, at a cost e^{κ̄} in the radius. (ii) The main-step source also contains the stored part ŷ of the old fluctuation, which is a function of R. To have F_f(s, 0) = f₀ for every s (L5), the response to ŷ is subtracted at the same switches and added back at s = 𝟏 (the difference construction (4.3)).

**The radius (task 3).** Lemma R (§6): R_f ≥ R := c_R(log θ_{i−1})^q for every f, with **c_R := 1**. That is a number fixed at row 1, before κ, independent of M and κ̄. All dependence on κ̄ (the factors e^{κ̄} and E_κ̄) goes into one floor on the radius coefficient C₀, at row 16 after M and κ̄ (C4 L40). All dependence on g goes into ceilings on γ. M enters only as lower bounds. §9 lists each constant.

**By-products.**
- (a) PAN Lemma 7.4 (PAN L279–289) is not correct as stated. A screened radius cannot exceed the source-domain cap R_cap ≍ e^{−Cκ̄}/g, and Lemma 4 of ST1 halves the decay rate. Proposition S (§6.2) gives the corrected bound R/R_f ≤ e^{−μD_f/4} + R/R_cap. Both terms still beat every power of log θ, so PAN Theorem P survives once its ℓ₃ is redefined. The age factor of PAN Lemma 7.4 disappears: the layer separation already absorbs it inside Q_X.
- (b) Under (Tq), ST1's **Outstanding R** (minimum-lift cores, ST1 L678–686) reduces to a ceiling on γ, because the radius gains (log θ)^{q−𝔭₀} on the lift's (log θ)^{2r} (Proposition R°, §3.4; proved as an implication from ST1 (56)–(57) and q > 𝔭₀ + 2r; not checked).
- (c) PAN §4.1 says (L) is no more than what the step's own cluster expansion needs (PAN L145, citing SA L14314–14315). That is too strong. Y3's field polydisc has radius C_𝒜𝔟, the window scale (Y3 L39236–39241). SA's own amplification is a scalar ν with |ν| < c_ν/𝗌_k = c_να_k/δ_k (SA L15721–15726, L15806–15812; SA L15150–15163). (L) is the vector form of the latter.

**On ST1's round-3 domains (the coordinator's second obligation).** ST1 round 3 (ST3) repairs M, R, B, F and leaves one statement Outstanding, the consumer interface CI (ST3 L254–266): every carried activity of NL1/LF1 is bounded on the ST1 chain domain built from the ledger coefficient c*, the smoothed lifts λ_τ, the lifted cores of Definition R1 and the witness bounds g_QΛ_Qα₀ε_i. My results on these domains:
- (L) holds on the round-3 domains. Theorem V uses only Lemmas 4, 5, 8, 11 (with 11′ for lifted cores), 12 and 13, and these survive (Tq) with the round-3 items (Lemma T3, §3.5). So Theorem L is proved there, with CI as an input through ST1 hypothesis 4.
- (L) does not imply CI, and CI is not a corollary of (L). (L) bounds an activity only along the image of the fluctuation substitution, a thin subset of the chain domain.
- What (L) does give is the analytic half of CI's inductive step. Theorem V holds at every complex input pair P' of the chain domain, not only at the physical one, and jointly in P' (Theorem V′, §5.4). That is exactly what the step's cluster expansion needs to form the new activities on the new chain domain ("potentials holomorphic on their declared complex fluctuation boxes and external cores", SA L14314–14315). Proposition CI-ind (§8.1) reduces CI, by induction over structures, to one statement, (CI-form): NL1's and LF1's formation estimates hold pointwise in the complex input pair of the ST1 domain. The first open input inside (CI-form) is (I-1) (precision gap and decay of the fibre precision) at complex *layered stage* pairs, ⟦PR-lay⟧ (IN1 L62).
- Under (Tq) the lift is not needed at all (Proposition U, §3.5). The radius gains (log θ)^{q−𝔭₀}, which dominates the lift's ceiling C_λ(log θ)^{2r_R}. With λ ≡ 1, ST3's Attacks 1 and 3 on CI (raw-lift excess; α₀ fixed before κ) lose their object, and ST3's Proposition R0 (made under (Tε)) does not apply. What remains of CI is the intrinsic-versus-(R5) rebuild that the assembly already names (AS L236): NL1/LF1 must build their activities on intrinsic domains.
- *On the order of b_f.* CI asks that the constants of b_f be fixed before κ and independent of M (ST3 L256). SA's own class bounds E₀ and 𝖡 come after M (SA L19469–19470; C4 rows 17). Read literally, CI is false for SA's class. But no choice before κ reads b_f: Theorem 14 uses b_f only in its output bound (77) (ST1 L864–866), and Theorem V only in |F_f| ≤ b_f. The requirement that is needed is the weaker one: **no constant fixed before κ reads b_f**. That holds (§9).

**First remaining Outstanding on (L)'s path** (not of (L) itself): **CI**, through ST1 hypothesis 4 (ST3 L401). ST3 §6 discharges hypotheses 1–3 and 5 at every transition from its inputs (ST3 L396–408). By Proposition CI-ind, CI at the structures before step i, together with (CI-form), gives everything (L) needs; the first open item inside (CI-form) is ⟦PR-lay⟧.

**Line count**: at the end of the file.

---

## 1. The target and the notation

### 1.1 The statement

(L) (PAN L134–141). For each term f ∈ 𝔉 of the step-i exponent there are a nonempty connected cube set X_f, a radius R_f ≥ R and a function F_f : 𝕊_{X_f} × 𝔻_{R_f} → ℂ with:

- (L1) F_f is holomorphic.
- (L2) F_f(𝟏, y) is the f-term of the step-i exponent at every y ∈ 𝒲.
- (L3) *Locality.* F_f(s, ζ) = F_f(s', ζ') whenever K_{X_f}(s) = K_{X_f}(s') =: K, s = s' on K, and ζ = ζ' on the bonds of I in K.
- (L4) *Reality.* F_f(s, ζ) is real when s and ζ are real.
- (L5) F_f(s, 0) = f₀ := F_f(𝟏, 0) for every s ∈ 𝕊_{X_f}.
- (L6) *Bound.* Either (two-sided) |F_f − f₀| ≤ ω_f, or (one-sided) Re F_f ≤ f₀ + ω_f, on 𝕊_{X_f} × 𝔻_{R_f}.

*On (L6).* PAN L141 states the two-sided case as |F_f| ≤ ½ω_f. That implies |F_f − f₀| ≤ ω_f. PAN's only use is Lemma 5.3(a), whose proof uses only |φ| ≤ ω with φ = F_f(tu) − f₀ (PAN L198). So the oscillation form above is weaker and suffices for PAN unchanged. It is the natural form for the kept forms, whose size is large but whose oscillation is controlled (SA L17564). [design]

### 1.2 Notation

As PAN §1.2 (PAN L47–57), with the following additions and one change.

- *The main step.* Step i is ST1's main-step transition (i − 1, out) → (i, in), so ST1's t is i, and the source level is t − 1 = i − 1 (ST1 L800; ST1d2 L700–707, Lemma SL(ii)). Write ℓ := log θ_{i−1} and g := g_{i−1} = θ_{i−1}^{−1/2}. By IN1 L42–43, ε_{i−1} = A₀gℓ^{𝔭₀} and the main-step threshold is δ_src = δ_{i−1} = (A₁/A₀)ε_{i−1} = A₁gℓ^{𝔭₀} (ST1 L800). The window radius is 𝔟 = A₁ℓ^{𝔭₀} in scaled units, so δ_src = g𝔟.
- *The input triple.* P = (U, A', 𝐉) is the input point of the main step in ST1's sense (ST1 L59–68): U is the new real background, a function of R; P ∈ 𝒟_{a|+} is ST1 Theorem 14's hypothesis 2 (ST1 L841).
- *The fluctuation.* I is the set of free bonds of level i − 1 in Λ_i^{pre} (PAN L49). For ζ ∈ E_ℂ = (ℂ³)^I put u(ζ)(b) := gΣ_aζ_{b,a}T_a, with (T_a) the orthonormal basis of PAN L49. In the matrix operator norm |u(ζ)(b)| ≤ c_Tg|ζ|_∞ with **c_T := 3** (each |T_a| ≤ 1 for the pairing ½Tr; three terms). ŷ denotes the stored part of the old fluctuation on Ω_i ∖ Λ_i; it is a function of R (TT (CL)(0), TT L113–117).
- *Cells and switches.* ST1 Theorem 14 localises over "finitely many cells 𝒞" (ST1 L846). **[design]** These cells are the M-cubes of level i − 1, the walk cubes of SA L14294–14296 and PAN L51. ST1's switch polydisc |s_Δ| < e^{κ̄} (ST1 L855) is then PAN's 𝕊 (PAN L54). For s ∈ ℂ^𝒞 and ζ ∈ E_ℂ, the *masked fluctuation* is (s ⊙ ζ)_{b,a} := s_{Δ_b}ζ_{b,a}, with Δ_b the cube of the midpoint of b (PAN L51).
- *Rows to cubes.* A source row is assigned to the cube that contains its initial site (ST1 L30: "A bond or stencil is read at its initial or base site").
- *Radius table.* r_ι(m) denotes ST1's base radius of index ι at level m (ST1 L92, L99). §3 compares (Tε): r_ι(m) = α_ιε_m with (Tq): r_ι(m) = α_{ι,m} = C_ιθ_m^{−1/2}(log θ_m)^q.
- *Exponent names.* ST1 uses q also as a level index (ST1 L94). Here q is always the radius exponent of IN1 L44 and C4 row 2; level indices are m, j, n.

---

## 2. What the sources say

### 2.1 SA: radii, the product box, response brackets, windows, walks

- *B4 is a source box* (SA L4006–4012). The "ordinary source box" allows a separate Euclidean regular member at each base point, its own scalar counterterm, a variable Wilson weight and small defects. The obligation is holomorphy "on this product box with a majorant independent of the number of labels". The product box of NL1(3) is a box in source and coupling parameters. It is not the free-fluctuation polydisc. So (L) is not literally NL1(3); it is the fluctuation analogue that PAN needs.
- *Norms on radius domains* (SA L4870–4873). ‖E‖_{j,κ} is a supremum over pairs 𝐩 ∈ 𝒰_j(X; r_{0,j}, r_{1,j}). The class activities are bounded on domains of the running radii.
- *The radius system* (SA L5999–6013, L6033). Admissible systems need CMa_{0,j} < a_{1,j}, a_{1,j}² ≤ Ca_{0,j}, adjacent ratios, a fixed small upper bound on the absolute radii, and 𝗌 := δ(θ_k)/a_{0,k+1} ≤ c. The running radii are α_{ι,j} = C_ιθ_j^{−1/2}(log θ_j)^q (L6033).
- *Order* (SA L19469–19470). (A₁, A₀, C₀, C₁, α₁, α₀, E₀, M₀, α', 𝖡) come after M, after κ̄ and after κ. SA L19491: "q − 𝔭₀ > Cr, so that 𝖭_k𝗌_k → 0".
- *The gas potentials* (SA L14304–14317). (UM1) is *assumed* ("For the actual local potentials assume", L14304); the potentials "are holomorphic on their declared complex fluctuation boxes" (L14314–14315). The box radius is not fixed at these lines.
- *The response bracket* (SA L15150–15172). For a plaquette function F_p, Φ_{p,Y}(s, ν) = F_p(P|_{X₀(p)} ∔ ν𝔥_Y(s; B)) is to be holomorphic on |s_Δ| < e^{κ̄}, |ν| < ρ, "uniformly in the allowed complex external fields and fluctuation box", with ρ ≥ c_Rα/δ > 1 (L15161), and "c_R > 0 can contain the fixed loss e^{−Cκ̄}" (L15163). L15170–15171: these are "quantitative background and membership hypotheses; the following Cauchy argument does not prove them". So SA amplifies the response to a fluctuation in its box by a scalar ν up to ≍ α/δ, and its c_R may depend on κ̄.
- *Window formation* (SA L15721–15745, L15784–15812). (WF1): 𝗌_k = δ_k/α_k, "δ_k is the tested fluctuation amplitude, whereas α_k is the analytic field radius" (L15739–15740). (WF5): the ν-term changes every datum, chart and core norm by at most C_R|ν|δ_kσ_j/α_j, with C_R including "the fixed loss from the enlarged fine-parameter discs" (L15797–15798). (WF6): all substitutions are admissible on |ν| < c_ν/𝗌_k (L15806–15807). Again a scalar ν, at radius α/δ.
- *Walks* (SA L17903–17920). Each walk carries s(Δ), |s(Δ)| < e^{κ̄}, for every cube it visits; "Setting a parameter to zero prevents a walk from crossing that cube" (L17905–17906). The interpolation is analytic on |λ| < 𝖺^{−1}, where 𝖺 is "the size of the response divided by the room in the domain of f" (L17909–17911). L17927–17929: at a stage the amplitude is at most C𝖭_kδ_j/min_ια_{ι,j}. This is SA's (Tq) arithmetic: threshold over the ℓ^q radius.
- *Kept forms* (SA L17562–17564). The forms Δ^{loc}_𝔨 and the factors z^{(j)} are functions of a pair near 𝔨, evaluated at the current background. A kept-form piece with carrier R has oscillation in the pair at most Cp₀(g_j)²e^{−κd^♮_{j+1}(R)}.
- *Strip* (SA L17518–17526). The strip substitution has a Jacobian that "contributes to the action as a boundary term" (L17526); the strip quantities depend on the background average V^{bg}_j (L17518–17522).

### 2.2 CA-II: Balaban's main step

- CA-II L79920–79938 (Balaban CMP 119 (3.15)). The brace evaluates 𝐄_k + 𝐑_k + 𝐁_k at U_k(exp i[g_kCA_k − hD̃(g_kCA_k)]V^{(k)}) and subtracts the value at U_{k+1}; it also holds the coupling-profile difference A((1/g_k²)(·) − 1/g_k², ·) at the two configurations. So the carried terms depend on the fluctuation through the old background U_k evaluated at the old datum exp i[gCA − hD̃(gCA)]V^{(k)}. That datum is the new background's datum times a pivot-completed exponential of the fluctuation. This is the form of ST1 Lemma 12's (68), D_old = e^{ia_V(u)}V (ST1 L750–757).
- CA-II L79979–80013 (Balaban (3.25)). z^{(k)} stands outside the integral over A; inside are the quadratic form, the linear term, 𝐏^{(k)}(g_k, (A_k, A)), the brace and V^{(k)}(S_{k+1}, (A_k, A)). "A_k denotes the fluctuation field on Ω_{k+1} ∩ Λ^c_{k+1}, and A denotes this field on Λ_{k+1}" (L80003–80006).

### 2.3 Y3: the three-dimensional analogue

- Y3 L39236–39241. The field polydisc is 𝔻^f(Y) = {B : |B(b)| < 𝖢_𝒜𝔟 for every b ∈ J_Y}, with 𝖢_𝒜 ≥ 3. Potentials are holomorphic on these polydiscs (L39304). The radius is a fixed multiple of the window 𝔟.
- Y3 L53557–53561. If C_𝒜 ≥ 2C_xt, then g_k^{−1}𝒜_k|_Y lies in half the field polydisc.
- Y3 L52579–52583. The conditional Gaussian puts s̄ = 1 on Z°^♯, s on the other big cubes of R and 0 outside R, and multiplies a coefficient or string by the product of s̄ over its big-cube hull. This is the locality pattern (L3).

So the 3D analogue of product-box holomorphy in the free fluctuation is holomorphy on a polydisc of radius 𝖢_𝒜𝔟, not (log θ)^q. PAN's mechanism needs more: its recentring factor 𝖺 = 4(r_out + ρ)/R must tend to 0 (PAN L381), and with R ≍ 𝔟 it is a fixed number.

### 2.4 ST1 (the distilled text, binding)

- *Substitution* (ST1 L63–68). P ∔ h = (U, A'', 𝐉 + K), A'' = (iη)^{−1}Log(e^{iηH}e^{iηA'}). "The real factor stays fixed."
- *Records and radii* (ST1 L92, L99). Simple radii c_σ(x|m)λ_τ(x)α_ιε_mL^{−pm}; tower bounds (14) with α₀ε_ℓ; core radii b_ι = α_ιε_i inf_X[c_σλ]; witness bounds g_QΛ_Qα₀ε_i. ST1d2 L130: "The formation table is r_ι(m) = α_ιε_m ... (distil's simplified design)".
- *Activities* (ST1 L101). A carried activity f is bounded by b_f on its declared domain, holomorphic in (A', 𝐉) with U fixed, Borel in U and near stored variables, jointly holomorphic in far variables and switches, with real gauge covariance.
- *DR* (ST1 L119–124). An actual regional response (H, K), "holomorphic in its complex input pair, datum and |s_Δ| < e^{κ̄}", with reality, covariance, restriction consistency and "splitting over face-connected components"; for source S it obeys (16): n_b(H, K) ≤ C_DE_{κ̄}C_Aδ_src e^{−μd(b,S)}. E_{κ̄} ≥ 1 is a parameter factor, "for example e^{C_Eκ̄}" (L124); a source-domain threshold "ε_De^{−c_Dκ̄}" is to be written explicitly (L124).
- *Order* (ST1 L128). All constants in rows 1–6 precede κ and are independent of M, κ̄. Row 5 (L136): α₁ ≥ α₀ ≥ 16max(1, C_mb)C_RA/c_min². Row 3 (L134): ρ₀min(δ_T, μ/2) ≥ log 16. Row 8 (L139): M ≥ L⁴M'₁, M ≥ C_dec κ̄. Row 10 (L141): γ small for adjacent radius ratios, analytic ceilings, M supλα₁ε ≪ 1, 2(b₀ + b₁) < a^♯.
- *Lemma 4 (LEV)* (ST1 L240–253). If n_b(h) ≤ Ae^{−μd(b,S)}, then n_b(h^δ) ≤ C_levAe^{−μd(b,S)/2} and ε̂_y ≤ K_pinAe^{−μd(y,S)/2} (27); "These constants are independent of depth and M, κ̄"; holomorphy holds where every relevant endpoint top is levelled (L253, L286).
- *Lemma 11* (ST1 L692–743). If ‖h‖_w ≤ r_* then P ∈ 𝒟_{a|+} ⇒ P ∔ h ∈ 𝒟_{a|−} with half of every gap left; "This holds also for a pinned shift" (L707).
- *Lemma 12* (ST1 L745–773). Physical identification given the actual datum map (68).
- *Lemma 13* (ST1 L782–834). Q_X = max_{b∈ℛ_X}e^{−μd_+(b,S)/2}/w(m_+(b)), E_X, a_X, ρ_X = (2a_X)^{−1}; levelling forced on |z| < ρ_X; the one-sided main-step separation (74) d_+(b, S) ≥ ρ₀(|m − j| − 3)_+ − C_car at j = t − 1 (L818–822).
- *Theorem 14* (ST1 L838–886). Hypotheses 1–5 (L840–844); Φ_Y(s, z) = f(ρ_X^{res}(P ∔ (zh_Y(s; P, ξ))^δ); 𝔮_X) (75), "All stored coordinates 𝔮_X remain fixed" (L853); holomorphic on |z| < ρ_X, |s_Δ| < e^{κ̄}, bounded by b_f (L855); exact at s = 𝟏, z = 1 on the physical locus (L856); component vanishing (L868). Proof L878–886.
- *Outstanding* M (L172), R (L678–686), B (L688–690), F (L775–780). L876: the drafts do not establish the premises at M, R, B and F.

### 2.5 IN1 and the order of constants

- IN1 L44: α_{ι,j} = C_ιθ_j^{−1/2}(log θ_j)^q. IN1 L347: q > 𝔭₀ + 2r. IN1 L673 (Lemma D.1): θ_j/θ_n ≤ 1 + (n − j) for j ≤ n under B̄γ² ≤ 1, and θ_n ≤ θ_j + c₅.
- C4 row 16 (C4 L40): "Test amplitudes A₁ → A₀ with A₀ ≫ A₁; radius coefficients C₀ → C₁; absolute radii α₁ → α₀ ... Take C₁ ≫ MC₀." IN1's modification of row 16 (IN1 L328) adds ceilings on the radii from (I-1); for the running radii these are ceilings on γ, since α_{ι,j} → 0 with g.

---

## 3. The radius table

### 3.1 The two tables

ST1's base radii enter through r_ι(m) only (ST1 L92, L94–96, L99, L166). Two choices:

  (Tε)  r_ι(m) = α_ιε_m = α_ιA₀θ_m^{−1/2}(log θ_m)^{𝔭₀}  (ST1d2 L130; α_ι fixed at ST1 row 5, before κ);
  (Tq)  r_ι(m) = α_{ι,m} = C_ιθ_m^{−1/2}(log θ_m)^q  (SA L6033; IN1 L44; C_ι at C4 row 16, after M and κ̄).

The ratio is r_ι^{(Tq)}(m)/r_ι^{(Tε)}(m) = (C_ι/(α_ιA₀))(log θ_m)^{q−𝔭₀}, which tends to ∞ with θ_m since q > 𝔭₀.

### 3.2 Under (Tε) the interface does not give the radius

**Proposition C.** [proved] Assume (Tε), the main step of level i, and ST1 Lemma 12's identification (68) at the main step with u = u(y) on the free rows (FL-main, §4.1). Let c₀ be a free row of level i − 1 in Λ_i^{pre} whose double block meets no lifted point, so λ = 1 on its read set. There is an activity f, read on the double block of c₀, satisfying every clause of ST1 L101 with bound b_f > 0, such that every holomorphic F on a polydisc 𝔻_{R'} with F(𝟏, y) = f-term for real y near 0 satisfies R' ≤ 2ρ_D/g, where ρ_D := C_QLc_maxr₁(i − 1) is the datum bound of the domain at c₀ (C_Q from AV/CURV, ST1 L108; c_max := 1 + β_s). Under (Tε), 2ρ_D/g = 2C_QLc_maxα₁A₀ℓ^{𝔭₀}. Hence (L) with R_f ≥ c_Rℓ^q fails for f once ℓ^{q−𝔭₀} > 2C_QLc_maxα₁A₀/c_R.

*Proof.* Let B(c₀)(P') := i^{−1}Log(𝓜(𝐔')(c₀)𝓜(U)(c₀)^{−1}) be the raw datum coordinate (6) of the pair of a triple P' = (U, A'', 𝐉'), relative to its real factor (ST1 L45–47). By AV/CURV, |B(c₀)| ≤ C_Qξ sup_{D(c₀)}|A''| (ST1 L108). On the declared domain the simple reads give η|A''| < c_σλr₁(i − 1)L^{−(i−1)} (ST1L92), so in level-(i − 1) units |B(c₀)| < ρ_D. Define

  w(P') := Tr(B(c₀)(P')²)/(8ρ_D²),  f(P') := b_f·w(P')/(1 − w(P')).

Since |Tr(X²)| ≤ 2|X|² for a 2 × 2 traceless matrix, |w| < 1/4 on the domain, and |f| ≤ b_f(1/4)/(3/4) < b_f. The function f is holomorphic in A'' at fixed U (composition of the average, the logarithm on its small branch, the trace and a Möbius map regular on |w| < 1). It is Borel in U. It is real at real triples, since B(c₀) is then Hermitian and Tr(B²) is real. Under a simultaneous real gauge g, B(c₀) is conjugated by g at the initial site of c₀ (covariance of (5), ST1 L284–285), so Tr(B(c₀)²) is invariant. It has no stored slots. So f satisfies ST1 L101.

At the physical old pair of a real fluctuation y in the window, (68) gives D_old = e^{ia_V(u)}V with u the free-row datum (ST1 L752–753). At the free row c₀ this is B(c₀) = u(c₀) = gΣ_ay_{c₀,a}T_a. Take y = te_{c₀,3} with T₃ = σ₃ and t real small. Then Tr(B(c₀)²) = 2g²t², so the f-term is ψ(t) := b_fw/(1 − w) with w = g²t²/(4ρ_D²). Let F be holomorphic on 𝔻_{R'} with F(𝟏, y) equal to the f-term for real y near 0, and put φ(z) := F(𝟏, ze_{c₀,3}) on |z| < R'. Then φ and ψ are holomorphic on |z| < min(R', 2ρ_D/g) and agree on a real interval, so they agree on that disc (identity theorem). If R' > 2ρ_D/g, φ is bounded near z₀ := 2ρ_D/g, while ψ(z) → ∞ as z → z₀ inside the disc, since w(z₀) = 1. This is a contradiction. So R' ≤ 2ρ_D/g. Under (Tε), r₁(i − 1) = α₁A₀gℓ^{𝔭₀}, which gives the stated value. ∎

*What C shows.* C refutes the implication "ST1 interface with (Tε) ⇒ (L)". It does not say anything about NL1's actual activities, which may extend further. But (L) is an input that PAN uses for all activities of the class at once. The class only gives bounds on declared domains. So the domains themselves must have the ℓ^q radius. Under (Tq) the same example has its pole at 2ρ_D/g ≍ C₁ℓ^q, which is consistent with (L).

### 3.3 ST1 under (Tq)

**Lemma T.** [proved, by inspection of every occurrence of r_ι in ST1] Replace (Tε) by (Tq) in ST1 (ST1 L92, L94–96, L99, L166), and replace the floor of row 5 on α₀ (ST1 L136) by the following conditions:

- (T1) for all θ ≥ γ^{−2}: 16max(1, C_mb)C_RAA₀(log θ)^{𝔭₀} ≤ c_min²C₀(log θ)^q;
- (T2) the adjacent ratios r_ι(m + 1)/r_ι(m) lie in [1/2, 2] for every frame;
- (T3) the absolute ceilings of ST1 row 10 (ST1 L141) hold with r_ι(m) from (Tq): (1 + β_s)C_λ(log θ_m)^{2r_R}C₁θ_m^{−1/2}(log θ_m)^q·M below the fixed small ceilings (Lemma 7's value ball, a_T of Lemma 8, a^♯/4 of Lemma 9, a_♭/4 for natural witnesses).

Each of (T1)–(T3) is a ceiling on γ. Then every lemma and Theorem 14 of ST1 hold with the same proofs, and every constant of ST1 rows 1–4, 6 is unchanged.

*Proof.* (T1): q > 𝔭₀, so (log θ)^{𝔭₀−q} → 0, and the condition reads sup_{θ≥γ^{−2}}h(θ) ≤ c with h → 0: a ceiling on γ in the supremum form (SA L19485; IN1 L334). (T2): r_ι(m)/r_ι(m + 1) = (θ_{m+1}/θ_m)^{1/2}(log θ_m/log θ_{m+1})^q, and the frame (F) bounds θ_m − θ_{m+1} between −c₅ and B̄ (IN1 L49), so the ratio tends to 1 uniformly as γ → 0. (T3): λ ≤ C_λ(log θ)^{2r_R} by ST1 (57) (ST1 L616), and θ^{−1/2}(log θ)^{q+2r_R} → 0. So all three are ceilings on γ.

Now every occurrence of the table in ST1 (located by searching ST1 for α_ι, α₀, α₁ and ε_m):

1. *Definitions* (L92, L94–96, L99): replaced by (Tq). Nothing is proved there.
2. *Lemma 1* (L147–170): the table enters only through w(m) = ½d_*(m)α₀ε_m (L166) and the claims w(m') ≤ 4^{|m'−m|}w(m), L^{−pν}w(m + ν) ≤ w(m) (L168). Their proof uses only 1/2 ≤ ε_{m+1}/ε_m ≤ 2 (L170). Under (Tq) this is (T2).
3. *Lemma 7* (L443–482): a fixed small value ball, absolute. (T3).
4. *Lemma 8* (L484–571): hypotheses E_U^0, sup n(w) ≤ a_T (L498), absolute; (T3). The conclusion (49) has no table.
5. *Lemma 9* (L573–594): 2(b₀ + b₁) ≤ a^♯ (L573), absolute; (T3). The arithmetic s = τb₀/(18K^♯(1 + c_♮)) is homogeneous in b₀.
6. *Lemma 10, pointwise formation* (L670): needs C_RAλε_m ≤ c_min²λr₀(m)/16. Under (Tq) this is C_RAA₀(log θ_m)^{𝔭₀} ≤ c_min²C₀(log θ_m)^q/16, which is (T1). The witness families (L660–664): the real gauge bound (60) has no table; it is compared with g_QΛ_Qr₀(i), which under (T1) is at least the (Tε) value g_QΛ_Qα₀ε_i with α₀ at its row-5 floor. (61) has no table.
7. *Lemma 10, tower formation* (L673–676): needs r₀(m)L^{−2m} ≤ r₀(ℓ)L^{−2ℓ} and r₀(m)L^{−3m} ≤ r₀(ℓ)L^{−2ℓ−min(q,ℓ)} for ℓ = min(m, i) ≤ m. By (T2), r₀(m)/r₀(ℓ) ≤ 2^{m−ℓ} ≤ L^{m−ℓ}, which suffices. The real tower is compared with c_min²r₀(ℓ)/16 through (T1).
8. *Lemma 11* (L692–743): the shift norm (63) divides by w(m_+(b)); the gaps are 2w(m°); the increment bound is K_ptrw(m°). All homogeneous of degree one in the table. (66) uses item 2. The core midpoint b₀^{mid} ≥ c_minr₀(i) (L729) is homogeneous. The witness drift (L738) is C r_*d_*(i)r₀(i), compared with g_QΛ_Qr₀(i): homogeneous; for natural witnesses the extra ceiling relative to a_♭ is (T3).
9. *Lemma 12* (L745–773): no table.
10. *Lemma 13* (L782–834): Q_X ∝ 1/r₀; the main-step and stage bounds (73) improve by the factor (α₀A₀/C₀)(log θ)^{𝔭₀−q} ≤ 1 (by (T1)). The finiteness of sup_ν4^νe^{−(μρ₀/2)(ν−3)_+} (L828) uses item 2.
11. *Theorem 14* (L838–886): its proof cites Lemmas 4, 5, 8, 11, 12, 13 only (L878–886).
12. *Outstanding R and B* (L678–690): these are not proved in ST1 and are not claimed here; §3.4 treats R.

No other occurrence exists. The constants K_pt, K_tw, K_core, r_* of row 6 (L137, L699–700) do not contain α_ι. So rows 1–4 and 6 are unchanged. ∎

*Remark (what (Tq) costs).* (Tq) enlarges every declared domain by (C_ι/(α_ιA₀))(log θ)^{q−𝔭₀}. The cost falls on the activity interface: NL1 and LF1 must supply their activities, with their bounds, on the larger domains (ST1 Theorem 14 hypothesis 4, L843; ST1d2 hypothesis 6). This is SA's own class requirement: its norms are suprema over 𝒰_j with the running radii α_{ι,j} (SA L4870–4873, L6033). So (Tq) returns ST1 to SA's design, which ST1's simplification had left (ST1d2 L130 calls (Tε) the "simplified design").

### 3.4 A by-product: Outstanding R under (Tq)

ST1's Outstanding R (L678–686): the core radius is α_ιε_i inf_X(c_σλ), while the real background obeys the pointwise bound (59) ≤ C_RAλ(x)ε_{m(x)}; a sufficient repair is (62), λ(x)ε_{m(x)}L^{−a(m(x)−i)} ≤ C_cε_i inf_Xλ with C_c fixed before κ, together with its enlarged-cube form.

**Proposition R°.** [proved, as an implication from ST1 (56)–(57), IN1 Lemma D.1 and q > 𝔭₀ + 2r_R; not checked by another model] Under (Tq), for x in a core address X ⊂ Ω_i (so m(x) ≥ i) and a ∈ {2, 3}:

  C_RAλ(x)ε_{m(x)}L^{−a(m(x)−i)} ≤ (c_min²/16)·r₀(i)·inf_Xλ,   (3.1)

and on an enlarged gauge cube Q of side s ≤ C_boxLM in layers ≥ i − 1,

  16L³B_*(s + 2)C_RAΛ_Qε_i ≤ C_potM·c_min·r₀(i)·inf_Xλ,   (3.2)

provided the following ceilings on γ hold: ℓ_i^{q−𝔭₀−2r_R} ≥ 2^{8+2r_R+𝔭₀}C_RAC_λA₀/(c_min²C₀) and ℓ_i^{q−𝔭₀−2r_R} ≥ 2^{10+2r_R}L⁴B_*C_boxC_RAC_λA₀/(C_potc_minC₀), with ℓ_i := log θ_i.

*Proof.* Put ν := m(x) − i ≥ 0. By IN1 Lemma D.1 with j = i, n = m(x): θ_i/θ_{m(x)} ≤ 1 + ν and θ_{m(x)} ≤ θ_i + c₅, so g_{m(x)} ≤ (1 + ν)^{1/2}g_i and ℓ_{m(x)} ≤ ℓ_i + 1 ≤ 2ℓ_i. By (57), λ(x) ≤ C_λℓ_{m(x)}^{2r_R} ≤ C_λ2^{2r_R}ℓ_i^{2r_R}. Hence

  C_RAλ(x)ε_{m(x)}L^{−aν} ≤ C_RAC_λ2^{2r_R}ℓ_i^{2r_R}A₀(1 + ν)^{1/2}g_i2^{𝔭₀}ℓ_i^{𝔭₀}L^{−2ν} ≤ C_RAC_λA₀2^{2r_R+𝔭₀}g_iℓ_i^{𝔭₀+2r_R},

since (1 + ν)^{1/2}L^{−2ν} ≤ 1. The right side of (3.1) is at least (c_min²/16)C₀g_iℓ_i^q, because inf_Xλ ≥ 1 by (57). The first ceiling gives (3.1). For (3.2): Λ_Q ≤ C_λ2^{2r_R}ℓ_i^{2r_R} by the same argument (the points of Q lie in layers ≥ i − 1, and ℓ_{i−1} ≤ 2ℓ_i), s + 2 ≤ 2C_boxLM, and the right side is at least C_potMc_minC₀g_iℓ_i^q. The factor M cancels, and the second ceiling gives (3.2). ∎

*Relation to ST3 Proposition R0.* ST3 L109–130 proves that (62) is false and that the scalar-infimum core is not formable, by a datum whose curvature is v ≥ (3/2)C_smL⁴L_♭^{2E₀}ε_t on a core whose radius is b₀ ≤ (5/4)Kα₀ε_t (ST3 L126–128). That argument is made under (Tε). Under (Tq) the radius is b₀ ≥ c_minC₀g_tℓ_t^q, while v ≤ C(log θ_t)^{2r_R}ε_t by the ceiling (56) (ST3 L122 uses it). So the inequality v > b₀ that R0 needs fails for small γ, and R0 does not apply. There is no conflict: R0 refutes the scalar core under (Tε), and (3.1) admits it under (Tq). Round 3's lifted core (ST3 Definition R1) is also admissible under (Tq) (§3.5); either repair may be used.

*Consequence.* With (3.1)–(3.2), ST1's own sufficient route (L681–686: "(59)–(60), restriction and a fixed increase of the radius floor prove core formation") applies. The comparison constant is not a number fixed before κ, as (62) asked; it is replaced by a ceiling on γ, which the IN1 order allows (IN1 Lemma A.8). This needs only that the lift ceiling (57) holds on core addresses. ST1 states (57) as a consequence of (56) for inherited exponents that obey (56) (L607–616). I do not claim the rest of ST1 Outstanding R's discussion (the consumer-domain remark, L686). This is the same mechanism as IN1 Lemma C.10 (IN1 L614–620: "radii dominate support bounds", from q > 𝔭₀ + 2r).

### 3.5 ST1 round 3 under (Tq), and the lift

ST3 amends st1-r2 by a mark ledger c* (Definition M1, ST3 L56–62), lifted cores (Definition R1, ST3 L134–149), output admission (Lemmas B1–B4, ST3 L210–252) and the stage map (§5, ST3 L270–392). The chain domain of ST3 §4.3 (ST3 L256) is built from c*, the smoothed lifts λ_τ of ST1 (56) (ST1 L610), the lifted cores, and the witness bounds g_QΛ_Qα₀ε_i.

**Lemma T3 (round 3 under (Tq)).** [proved for the items whose statements and proofs I read: ST3 L52–268, L394–410; for ST3 §5 from its statements only] Under (Tq) with (T1)–(T3), the round-3 items hold with the same proofs.

*Proof, item by item.*
1. Definition M1, Lemmas M2, 1′, M3 (ST3 L56–99): no table. Lemma 1′'s drop claims use Lemma 1's ratio arithmetic, which is (T2) (Lemma T item 2).
2. Definition R1 (ST3 L134–147): b_ι(e) = r_ι(i)inf_{Rd(e)}[c*λ_τ] with the (Tq) table; the witness clause (c) has bound C_potMΛ_Qr₀(i).
3. Lemma R2 (ST3 L151–153): ratios of λ_τ and c* only; no table.
4. Lemma 9′ (ST3 L157–178): homogeneous of degree one in b(e); its absolute hypothesis sup 2(b₀ + b₁) ≤ a^♯ is (T3).
5. Lemma 10′ (ST3 L180–190): (a) needs C_RAλ(x)ε_i ≤ (c_min²/4)r₀(i)e^{−δ/4}λ(x); under (Tq) it reads 4e^{δ/4}C_RAA₀ℓ_i^{𝔭₀} ≤ c_min²C₀ℓ_i^q, which follows from (T1) because δ ≤ 1 and 4e^{1/4} < 16. (b), (d) are the same comparison. (c) is (60) with the row-5 quotient, compared with C_potMΛ_Qr₀(i): (T1).
6. Lemma 11′ (ST3 L192–198): b₀^{mid}(e) ≥ c_minr₀(i) and the shift bound 4L³rw(i) = 2L³rd_*(i)r₀(i) are homogeneous.
7. Lemma B1 (ST3 L210–221): (B1) is an inequality between tests and C(M), with no table; formation is through (59) and Lemmas 10, 10′, item 5.
8. Lemma B2 (ST3 L225–238): Q_X ≤ 16/(θ_sβ_sr₀(t)), homogeneous. Under (Tq) the output amplitude is a_X ≤ 16C_levC(M)E_{κ̄}δ'_t/(θ_sβ_sr_*r₀(t)) + (pinning term), with δ'_t/r₀(t) = A₁ℓ_t^{𝔭₁−q}/C₀ → 0: still a ceiling on γ after M.
9. Lemma B4 (ST3 L248–252): the upper ceilings on W_Q = g_QΛ_Qr₀(i) are (T3); the lower bound absorbing Cr_*d_*(i)r₀(i) is homogeneous.
10. ST3 §5 (Lemma F1, F2, Proposition F3, Theorem F4, Lemmas F5–F7, ST3 L289–390): their statements involve the thresholds δ'_j, the chart radii c_chL^{−9}, C_A, C'_A and the tube, not r_ι. I did not reread their proofs line by line. ∎

**Proposition U (the lift is not needed under (Tq)).** [proved by inspection of every occurrence of the lift in ST1 and ST3; not checked] Use (Tq) and set **λ_τ ≡ 1** in every record (so Λ_Q = 1 and b_ι(e) = r_ι(i)inf_{Rd(e)}c*). Call this table (Tq0). Assume q > 𝔭₀ + 2r_R and the ceilings on γ:

  (U1) C_U(log θ)^{2r_R+𝔭₀}A₀ ≤ (c_min²/64)C₀(log θ)^q for θ ≥ γ^{−2};
  (U2) 32L³B_*C_boxC_U(log θ)^{2r_R+𝔭₀}A₀ ≤ C_potc_minC₀(log θ)^q/4 for θ ≥ γ^{−2};
  (U3) C_PC_{bx}C(M)A₀(log θ)^{𝔭₀} ≤ (c_min²/64)C₀(log θ)^q for θ ≥ γ^{−2} (after M),

with C_U := C_PC_teC_R²·2·sup_{D≥0}C'(1 + D)^{2r_R}e^{−(δ_P−δ/4)D}, a constant fixed before κ (C_P, C_te, C_R, r_R, δ_P, δ from ST1 rows 2–3). Then every formation statement of ST1 and ST3 (Lemmas 10, 10′, B1) holds for the records of (Tq0), and every other lemma holds unchanged.

*Proof.* *Where the lift is used.* Searching ST1 and ST3 for λ_τ, λ(x), Λ_Q and inf_Xλ finds it only in: the record definitions (ST1 L82, L92–99; ST3 L134–141); the formation lemmas through (59) and (60)–(61) (ST1 L610–676; ST3 L180–190, L221); Outstanding R (ST1 L678–686, replaced in ST3); the core paragraph of Lemma 11 and Lemma 11′ (ST1 L726–731; ST3 L192–198), through the ratio of infima; Lemma R2 (ST3 L151–153); Lemma B4 and the CI attacks (ST3 L248, L256–264). (λ_p = L^{−(i−p)} in Lemmas 9 and 9′ is a different symbol.) With λ_τ ≡ 1: the ratio of infima in Lemma 11′ is 1 ≥ its needed bound; Lemma R2 holds with λ-variation 1; Lemma B4's upper ceilings improve and its lower bound uses only Λ_Q ≥ 1. So only formation needs a new proof.

*Formation without the lift.* The only role of the lift is to dominate the real background near raised points: (58) lets a tested datum loop τ reach C_teL_♭^{2𝓔(τ)}ε_{m(τ)} (ST1 L620–622), and PROF spreads it at rate δ_P (ST1 L117). By PROF, (58), the ceiling (56) L_♭^{2𝓔(τ)} ≤ C_R²(log θ_{m(τ)})^{2r_R} (ST1 L610), the comparison (log θ_{m(τ)})^{2r_R} ≤ C'(log θ_{m(x)})^{2r_R}(1 + d(x, τ))^{2r_R} (ST1 L632–638) and ε_{m(τ)}/ε_{m(x)} ≤ 2e^{δd(x,τ)/4} (ST1 L646), the actual real background satisfies at complete elements

  l²η^{−2}|∂U − I|, l³|J°_η(U)| ≤ C_U(log θ_{m(x)})^{2r_R}ε_{m(x)}.   (59′)

The supremum in C_U is finite because δ ≤ δ_P (ST1 L133: δ = min(1, δ_P, θ₄)), so δ_P − δ/4 ≥ 3δ_P/4 > 0. Pointwise and tower formation need (59′) ≤ (c_min²/16)r₀(m(x)) (ST1 L670 with λ = 1): this is (U1), since ε_m = A₀θ_m^{−1/2}(log θ_m)^{𝔭₀} and r₀(m) = C₀θ_m^{−1/2}(log θ_m)^q. Lifted-core formation (ST3 Lemma 10′(a), (b), (d)) is the same comparison at radius (c_min/4)r₀(i)c_min, with the level conversion of ST3 L184; it follows from (U1). The cube-gauge witnesses: (60) with C_RAΛ_Q replaced by C_U(log θ)^{2r_R} gives |A|, |∇A| < 16L³B_*(s + 2)C_U(log θ_i)^{2r_R}ε_i with s ≤ C_boxLM; compared with (c_min/4)C_potMr₀(i), the factor M cancels and (U2) suffices; (61) holds for small γ as before. Output formation (ST3 Lemma B1): by BOX-bg (ST3 L29), output loops near the box obey |∂D_out(τ) − I| ≤ C_bxC(M)ε_t, so PROF gives a real background at most C_PC_bxC(M)ε_t there, and (U3) gives formation; loops elsewhere are as before. Each of (U1)–(U3) has the supremum form with h → 0, because q > 𝔭₀ + 2r_R, so each is a ceiling on γ; (U3) is chosen after M, which the order allows (ST3 L47). ∎

*What Proposition U changes for CI.* Under (Tq0) the chain domain carries no lift. ST3's Attack 1 (ST3 L260) compares λ with SA's raw lift L_♭^{2e_σ}: now λ = 1 ≤ L_♭^{2e_σ}, so the lift no longer obstructs the inclusion of the ST1 domain in SA's lifted domain (SA L6143–6145). Attack 2 (ST3 L262) compares Λ_Q with CA-I's printed exponents: now Λ_Q = 1 ≤ L_♭^{2e(Q)}. Attack 3(a) (ST3 L264) asks to absorb a polylogarithmic excess into a constant fixed before κ: under (Tq) the excess is absorbed by (log θ)^{q−𝔭₀}, not by a constant, and C₀ is a row-16 constant. Attack 3(b) concerns the smoothing rate, which is moot. So under (Tq0) the lift part of CI disappears. *What does not disappear:* ST1's tower and core clauses are intrinsic (ST1 L75–80, (8)), not SA's (R5) old-chart clauses, and the assembly already records that "NL1 and LF1 must construct their activities on D^int and reproduce their bounds there" (AS L236). The witness-family constants g_Q (ST1 L99) must also be at most the corresponding printed constants for an inclusion in SA's or CA-I's domain. So CI does not reduce to SA's printed bounds even under (Tq0); §8.1 states what remains.

*Design recommendation.* (Tq0) is simpler than (Tε) with smoothed lifts and lifted cores, and it is SA's radius table. Its cost is that every activity must be bounded on domains of radius ≍ C₁g(log θ)^q, which SA's class already requires (SA L4870–4873). Whether ST1 adopts (Tq0), or keeps its lifts under (Tq), is ST1's decision; Theorem L holds in either case (§8).

---

## 4. The main-step data and the family of shifts

### 4.1 Inputs at the main step

**(FL-main)** [input: ST1 Lemma 12 (68) at the main step, read with Balaban's (3.15) as CA-II L79920–79938 quotes it; owner ST1/NL1; reading]. At the main step of level i there are a real fixed datum V = M_−(U) (U the new background) and a map v ↦ S(v), the *completed source*, defined for v = gŷ ⊕ w on the rows of level i − 1 in Ω_i, with w a complex potential on the free rows I, on the chart ball ‖v‖_∞ < c_chL^{−9} (ST1 L754), such that:

- (a) S(v) = b_V(a_V(v)) (ST1 L757: "Feed B' = b_V(a_V(u)) ... to DR"), holomorphic, real at real v, S(0) = 0;
- (b) for the actual real fluctuation y ∈ 𝒲, S(gŷ ⊕ u(y)) is the actual completed source of the main step, and the old physical datum is D_old = e^{ia_V(gŷ⊕u(y))}V;
- (c) ‖S(v) − S(v')‖_src ≤ C_A‖v − v'‖_∞ on the chart ball, with C_A the chart and completion constant of ST1 L125, L798 (fixed at ST1 row 2);
- (d) ‖S(gŷ ⊕ 0)‖_src ≤ C_Aδ_src: this is ST1 Theorem 14 hypothesis 3 ("the actual completed source has the FL bound", L842) at y = 0, which lies in 𝒲 because 𝒲 is a product of symmetric convex sets containing balls (TT (W), TT L120);
- (e) *range*: S(v) on a row c depends only on v on rows within lattice distance R_σ of c, with R_σ fixed with L (the pivot completion acts within the block of its equation, ST1 L767; b_V reads one adjacent endpoint block, ST1 L51–53, L818).

*Status after ST1 round 3.* ST3 Remark F8 (ST3 L390) now supplies this map at main steps: "Define D_old by (F5) with u = gB on integrated free rows and u = f_H(A') (Lemma F1) on stored free rows", with Theorem F4's items 1–3, 5, 6 "with the same proofs", holomorphy in the integrated variables, and cutoff-zone stored variables held fixed. In the notation here, gŷ is the stored part u = f_H(A'), a function of R, and u(y) = gB on the integrated free rows. So (FL-main)(a)–(c), (e) are F8 with Theorem F4, and (d) is Lemma 13's main-step hypothesis that δ_src dominates the removed-row thresholds (ST3 L390, last sentences). I keep the label (FL-main) for this package.

*Why it was a reading.* At a stage, ST1's actual fluctuation map is Outstanding F in round 2 (ST1 L775–780). At the main step, Balaban's own formula writes the old datum as exp i[gCA − hD̃(gCA)]V^{(k)} with A the fluctuation (CA-II L79920–79938). That is (68) with a_V(v) = 𝐂v − hD̃(𝐂v) in Balaban's notation. I read this as (FL-main)(a)–(b). The identification of Balaban's V^{(k)} with ST1's M_−(U) and of his U_k(·) with ST1's background map is the reading flagged.

**(DR-ζ)** [input: ST1 DR, L119–124, read on its complex source ball; owner ST1 (the actual decoupled DR construction, ST1 L939); reading]. Let s_D := ε_De^{−c_Dκ̄} be DR's source-domain threshold (ST1 L124). For every s in the switch polydisc |s_Δ| < e^{κ̄} and every complex completed source S with ‖S‖_src < s_D, DR's response h(s; P, S) is defined, jointly holomorphic in (s, S), real at real (s, S), zero at S = 0, and

  n_b(h(s; P, S)) ≤ C_DE_{κ̄}‖S‖_src e^{−μd_+(b, supp S)}  (b any bond),   (4.1)

in the input metric d_+ (ST1 L794: if DR is stated in the old metric, (16) holds in d_+). *Reading:* ST1 (16) is written with δ_src, "the threshold at the actual source level" (ST1d2 L192), and with C_A, which converts the raw size to the completed one. I read (16) as the linear bound (4.1) for every complex completed source in the source ball. This is how Lemma 13 uses it: its proof applies Lemma 4 to zh at |z| < ρ_X, i.e. to sources of size |z|δ_src (ST1 L816). PAN §13.4 already asks ST1 to confirm "(S) for complex sources of sup norm < R" (PAN L560).

**(DR-loc)** [input: ST1 DR "splitting over face-connected components" (L119) and Theorem 14's component vanishing (L868), stated row by row; owner ST1; new statement]. For every s and S as in (DR-ζ), and every face-connected component K' of supp s, the restriction of h(s; P, S) to the bonds whose initial site lies in a cube of K' depends only on P, on s|_{K'} and on the values of S on the rows assigned to the cubes of K'.

*Why stated.* ST1 says the response splits over face-connected components (L119) and that a switched component that misses every source contributes nothing (L868, L886). It does not say which source rows a component reads. (DR-loc) is the natural statement: a walk that cannot leave K' cannot read a source row outside K'.

**(ST-main)** [input: ST1 Theorem 14 hypotheses 1, 2, 4, 5 at the main step, with (Tq); owner ST1 for 1, 2, 5 and NL1/LF1 for 4]. GEO, AV/CURV, A1/F0/REG, P82°–M1, PROF/RCG4, OPS/SLICE/UNQ hold on every system used (hyp. 1, L840); the actual gaps (13) hold and P ∈ 𝒟_{a|+} with every working core and every absolute, logarithm, gauge and source-domain ceiling (hyp. 2, L841); each activity f, supported on X, has its bound b_f and the interface of ST1 L101, and every relevant endpoint pillar is among the reads (hyp. 4, L843); the identification hypotheses of Lemma 12 hold at the actual source (hyp. 5, L844).

### 4.2 The family of shifts

Fix an activity f with support X and stored coordinates 𝔮_X, and a connected cube set X_f ⊃ X^↑, where X^↑ is the set of cells meeting X and its read carriers, endpoint pillars included (ST1 L846, L843). For s ∈ 𝕊_{X_f} and ζ ∈ E_ℂ define

  v(s, ζ) := gŷ ⊕ u(s ⊙ ζ),  v₀ := gŷ ⊕ 0,   (4.2)
  𝐡(s, ζ) := h(𝟏; P, S(v₀)) + h(s; P, S(v(s, ζ))) − h(s; P, S(v₀)),   (4.3)
  Π_f(s, ζ) := ρ_X^{res}(P ∔ 𝐡(s, ζ)^δ),  F_f(s, ζ) := f(Π_f(s, ζ); 𝔮_X).   (4.4)

Here h^δ is ST1's pinned shift (Lemma 4, ST1 L243–247) applied to the total shift, and ρ_X^{res} is restriction and change of units (ST1 L798). For an activity without stored slots the unpinned shift may be used (ST1 L853); the pinned one is used throughout here.

*Why (4.3).* At s = 𝟏 the last two terms of (4.3) combine with the first to give h(𝟏; P, S(v(𝟏, ζ))), the specified response to the full source (ST1 L119: "At s = 1 it uses the reduced action and multiplier formulas"). At ζ = 0 the last two terms cancel for every s, so 𝐡(s, 0) = h(𝟏; P, S(v₀)) does not depend on s. Without the subtraction, F_f(s, 0) would be the localised response to the stored part ŷ, which depends on s, and (L5) would fail. The term h(𝟏; P, S(v₀)) is a fixed function of R. **[design]**

*Why the mask.* A source row assigned to a cube Δ reads v on rows within R_σ of it ((FL-main)(e)). For M > R_σ + 2 these lie in Δ or in cubes *-adjacent to Δ. A *-adjacent cube outside K_{X_f}(s) has s = 0, so the mask kills the fluctuation there. This makes (L3) exact rather than true up to one cube layer. The price is |s ⊙ ζ|_∞ < e^{κ̄}|ζ|_∞. **[design]**

---

## 5. Theorem V: the main-step substitution in the free complex fluctuation

### 5.1 A main-step bound on Q_X under (Tq)

**Lemma Q.** [proved from ST1 (18), (74), row 3 and (T2)] At the main step, for any read set ℛ_X,

  Q_X := max_{b∈ℛ_X}e^{−μd_+(b,𝒮)/2}/w(m_+(b)) ≤ C_Q/((1 − θ_s)β_sr₀(i − 1)),  C_Q := 256e^{μC_car/2},

where 𝒮 is the main-step source set (the changed determining rows with their carriers, ST1 L782), and w(m) = ½d_*(m)r₀(m) with the main-step profile d_*(m) = (1 − θ_s)β_s2^{−(i−m)} (ST1 L162–166), extended to m = i by the same formula. If moreover d_+(b, 𝒮) ≥ D for every b ∈ ℛ_X, then Q_X ≤ C_Qe^{−μD/4}/((1 − θ_s)β_sr₀(i − 1)).

*Proof.* Let b ∈ ℛ_X have input layer m := m_+(b) and put ν := i − 1 − m ≥ −1. For ν ≥ 0, w(m) = (1 − θ_s)β_s2^{−ν−2}r₀(m), and r₀(m) ≥ 2^{−ν}r₀(i − 1) by (T2); so 1/w(m) ≤ 4·4^ν/((1 − θ_s)β_sr₀(i − 1)). For ν = −1, w(i) = ½(1 − θ_s)β_sr₀(i) ≥ ¼(1 − θ_s)β_sr₀(i − 1), so 1/w(i) ≤ 4/((1 − θ_s)β_sr₀(i − 1)). In all cases 1/w(m) ≤ 4·4^{ν_+}/((1 − θ_s)β_sr₀(i − 1)).

By (74) at the main step, one-sided at j = i − 1 (ST1 L818–822), d_+(b, 𝒮) ≥ ρ₀(ν − 3)_+ − C_car. By row 3 (ST1 L134), μρ₀/2 ≥ log 16. Hence e^{−μd_+/2} ≤ e^{μC_car/2}16^{−(ν−3)_+}. The product 4^{ν_+}16^{−(ν−3)_+} is at most 4³ = 64 for ν ≤ 3, and equals 4^{6−ν} ≤ 16 for ν ≥ 4. So Q_X ≤ 4·64e^{μC_car/2}/((1 − θ_s)β_sr₀(i − 1)).

For the second claim write e^{−μd_+/2} = e^{−μd_+/4}e^{−μd_+/4} ≤ e^{−μD/4}e^{μC_car/4}4^{−(ν−3)_+}, using μρ₀/4 ≥ log 4. Then 4^{ν_+}4^{−(ν−3)_+} ≤ 64, and e^{μC_car/4} ≤ e^{μC_car/2}. ∎

### 5.2 The statement

Put R_V := c_Rℓ^q. Consider the conditions, for ℓ = log θ_{i−1} with θ_{i−1} ≥ γ^{−2}:

- (V1) C₀ ≥ C₀^{(L)} := 5c_TC_levC_DC_AC_Qe^{κ̄}E_{κ̄}c_R/((1 − θ_s)β_sr_*);
- (V2) 15C_levC_DE_{κ̄}C_AC_QA₁ℓ^{𝔭₀−q} ≤ (1 − θ_s)β_sr_*C₀;
- (V3) 2K_pinC_DE_{κ̄}C_A(3δ_src + c_Tge^{κ̄}R_V) < ε_lev;
- (V4) C_A(δ_src + c_Tge^{κ̄}R_V) < s_D;
- (V5) ‖gŷ‖_∞ + c_Tge^{κ̄}R_V < c_chL^{−9};
- (V6) M ≥ R_σ + 3.

**Theorem V.** [proved from (ST-main), (FL-main), (DR-ζ), (DR-loc), Lemma T, Lemma Q and ST1 Lemmas 4, 5, 8, 11, 12] Assume (Tq) with (T1)–(T3) and (V1)–(V6). Let f be an activity as in (ST-main) hypothesis 4, with support X, and X_f ⊃ X^↑ connected. Then for all (s, ζ) ∈ 𝕊_{X_f} × 𝔻_{R_V}:

- (a) *Admission.* Every endpoint top of X is levelled; ‖ρ_X^{res}𝐡(s, ζ)^δ‖_w < r_*/2; Π_f(s, ζ) lies in the target chain domain 𝒟_{a|−} restricted to the reads of X, with at least half of every gap left; every tower datum keeps distance at least δ_B/8 from the complement of its tube. The real factor of Π_f(s, ζ) is U, and 𝔮_X is unchanged.
- (b) *Holomorphy and bound.* F_f is holomorphic on 𝕊_{X_f} × 𝔻_{R_V} and |F_f| ≤ b_f there.
- (c) *Locality.* F_f satisfies (L3).
- (d) *Reality.* F_f satisfies (L4).
- (e) *No fluctuation.* F_f(s, 0) = F_f(𝟏, 0) for every s ∈ 𝕊_{X_f}.
- (f) *Identification.* For every y ∈ 𝒲, F_f(𝟏, y) is the old activity at the actual reconstructed background, with its stored transports; that is, the f-term of the step-i exponent at y.

### 5.3 Proof

*Step 0: the fixed data.* By (10) (ST1 L65–68), P ∔ h has real factor U for every shift h. The stored coordinates 𝔮_X are a separate argument of f in (4.4) and are not touched by 𝐡. The base triple P, the stored part ŷ and the shift h(𝟏; P, S(v₀)) are functions of R.

*Step 1: the source.* Let (s, ζ) ∈ 𝕊_{X_f} × 𝔻_{R_V}. Since |s_Δ| < e^{κ̄}, |s ⊙ ζ|_∞ < e^{κ̄}R_V and ‖u(s ⊙ ζ)‖_∞ ≤ c_Tge^{κ̄}R_V. By (V5), v(s, ζ) and v₀ lie in the chart ball, so S(v(s, ζ)) and S(v₀) are defined, and holomorphic in (s, ζ), since v is a polynomial in (s, ζ) and S is holomorphic ((FL-main)(a)). By (FL-main)(c)–(d),

  ‖S(v(s, ζ))‖_src ≤ C_Aδ_src + C_Ac_Tge^{κ̄}R_V,  ‖S(v₀)‖_src ≤ C_Aδ_src.

By (V4) both are below s_D.

*Step 2: the response.* By (DR-ζ), the three responses in (4.3) are defined and jointly holomorphic in (s, ζ) on 𝕊_{X_f} × 𝔻_{R_V} (the first is constant). The supports of S(v(s, ζ)) and S(v₀) lie in 𝒮, so d_+(b, supp S) ≥ d_+(b, 𝒮) and e^{−μd_+(b,supp S)} ≤ e^{−μd_+(b,𝒮)}. By (4.1) and the triangle inequality for the seminorm n_b,

  n_b(𝐡(s, ζ)) ≤ A_Ve^{−μd_+(b,𝒮)},  A_V := C_DE_{κ̄}C_A(3δ_src + c_Tge^{κ̄}R_V).   (5.1)

(The first term of (4.3) is at s = 𝟏, in the switch polydisc, so (4.1) applies to it with the same E_{κ̄}.)

*Step 3: levelling is forced.* By Lemma 4 (27) (ST1 L251), ε̂_y(𝐡(s, ζ)) ≤ K_pinA_Ve^{−μd(y,𝒮)/2} ≤ K_pinA_V for every top y. By (V3), K_pinA_V < ε_lev/2. So every endpoint top is levelled at every point of 𝕊_{X_f} × 𝔻_{R_V}. The levelling decision is constant on the whole polydisc; no non-holomorphic cutoff is varied there (as in ST1 L816, L878). By Lemma 4 the pinned shift 𝐡^δ is then a holomorphic function of the shift (ST1 L253, L286: "the formulas are holomorphic on each forced-levelled set"), hence of (s, ζ).

*Step 4: the pinned norm.* By (27) and (5.1), n_b(𝐡^δ) ≤ C_levA_Ve^{−μd_+(b,𝒮)/2}. Divide by w(m_+(b)) and take the maximum over the reads of X: by Lemma Q,

  ‖ρ_X^{res}𝐡^δ‖_w ≤ C_levA_VQ_X ≤ C_levC_DE_{κ̄}C_AC_Q(3δ_src + c_Tge^{κ̄}R_V)/((1 − θ_s)β_sC₀gℓ^q),

using r₀(i − 1) = C₀gℓ^q under (Tq). With δ_src = A₁gℓ^{𝔭₀}, the first part is 3C_levC_DE_{κ̄}C_AC_QA₁ℓ^{𝔭₀−q}/((1 − θ_s)β_sC₀) ≤ r_*/5 by (V2). The second part is c_TC_levC_DE_{κ̄}C_AC_Qe^{κ̄}c_R/((1 − θ_s)β_sC₀) ≤ r_*/5 by (V1). So ‖ρ_X^{res}𝐡^δ‖_w ≤ 2r_*/5 < r_*/2.

*Step 5: inclusion.* By (ST-main) hypothesis 2, P ∈ 𝒟_{a|+}, with every absolute and logarithm ceiling. By Lemma T these ceilings are (T3) and the ceilings already in ST1 row 10. Lemma 11 (65), for pinned shifts (ST1 L707), gives P ∔ 𝐡^δ ∈ 𝒟_{a|−} with at least half of every gap left, since ‖𝐡^δ‖_w ≤ r_*. Restriction commutes with (10) (ST1 L733), so Π_f(s, ζ) lies in the restricted target domain.

*Step 6: continuation domains.* As in ST1 L878: Lemmas 5 and 8 supply the continuation domain of every tower datum read, with tube room δ_B/8 (ST1 L503, L570). This is the same argument at the point Π_f(s, ζ), which by Step 5 is a point of the target chain domain.

*Step 7: composition.* f is holomorphic on the fixed-U fibre of its declared domain (ST1 L101), and Π_f maps 𝕊_{X_f} × 𝔻_{R_V} holomorphically into that fibre (Steps 2–5; the logarithm in (10) is holomorphic on the small chart, ST1 L697). So F_f = f ∘ Π_f is holomorphic, and |F_f| ≤ b_f. Borel dependence on the real and near variables is as in ST1 L880: finitely many algebraic maps, fixed branches and the Borel interface. This proves (a) and (b).

*Step 8: identification.* Let y ∈ 𝒲. At s = 𝟏, (4.3) gives 𝐡(𝟏, y) = h(𝟏; P, S(gŷ ⊕ u(y))), the specified response at s = 1 to the actual completed source ((FL-main)(b)). This is Theorem 14's shift at s = 𝟏, z = 1 with the actual source. Theorem 14's second assertion (ST1 L856), under its hypothesis 5, says that the value is exactly the old activity at the actual reconstructed background, with its stored transports. This proves (f).

*Step 9: zero fluctuation.* u(s ⊙ 0) = 0, so v(s, 0) = v₀ and the last two terms of (4.3) cancel: 𝐡(s, 0) = h(𝟏; P, S(v₀)) for every s. Hence Π_f(s, 0) and F_f(s, 0) do not depend on s, and F_f(s, 0) = F_f(𝟏, 0). This proves (e).

*Step 10: locality.* Let s, s' ∈ 𝕊_{X_f} with K_{X_f}(s) = K_{X_f}(s') = K, s = s' on K, and ζ = ζ' on the bonds of I in K. Since s = 1 on X_f, X_f ⊂ supp s, so K is the *-component of supp s that contains X_f. No cube *-adjacent to K and outside K lies in supp s; likewise for s'. Hence supp s ∩ N₁(K) = K = supp s' ∩ N₁(K), with N₁ the one-cube *-neighbourhood.

(i) *Masked fluctuation.* On the bonds b with Δ_b ∈ K, (s ⊙ ζ)_b = (s' ⊙ ζ')_b. On the bonds with Δ_b ∈ N₁(K) ∖ K, s_{Δ_b} = s'_{Δ_b} = 0, so both are 0.

(ii) *Sources on rows of K.* A row c assigned to a cube Δ ∈ K reads v on rows within R_σ of c ((FL-main)(e)). By (V6) those rows have their bonds in cubes of N₁(Δ) ⊂ N₁(K). By (i), S(v(s, ζ))(c) = S(v(s', ζ'))(c). The stored part gŷ is common.

(iii) *Responses on cubes of X_f.* Let Δ ∈ X_f and let K' be the face-connected component of supp s that contains Δ. K' is face-connected, hence *-connected, and contains a cube of X_f, so K' ⊂ K. K' is a face component of K regarded as a set, and K ∩ supp s = K ∩ supp s', so K' is also the face component of supp s' that contains Δ. By (DR-loc), the response on bonds with initial site in K' depends only on P, s|_{K'} and the source on the rows of K'. By (ii) and s|_{K'} = s'|_{K'}, h(s; P, S(v(s, ζ))) = h(s'; P, S(v(s', ζ'))) on those bonds; and h(s; P, S(v₀)) = h(s'; P, S(v₀)) there. The first term of (4.3) is common. So 𝐡(s, ζ) = 𝐡(s', ζ') on every bond with initial site in a cube of X_f.

(iv) *Reads.* The pin at an endpoint top depends on the shift on its read set Rd(y) and on the real frames (ST1 L241, L255–275); these read sets are among the reads of X (hypothesis 4, ST1 L843) and lie in cubes of X^↑ ⊂ X_f. The restriction ρ_X^{res} keeps only the reads of X, whose stencils have their initial sites in cubes of X^↑ ⊂ X_f. So Π_f(s, ζ) = Π_f(s', ζ'), and F_f(s, ζ) = F_f(s', ζ'). This proves (c).

*Step 11: reality.* For real (s, ζ), v(s, ζ) is real, S is real at real arguments ((FL-main)(a)), DR is real at real data ((DR-ζ)), and the pin of a real shift is a real gauge built from real frames and real logarithms (ST1 L255–275). So Π_f(s, ζ) is a real triple. An activity is real at real triples (class clause; SA L6205–6207: "All entries are real on real arguments"; IN1 L78: reality preserved). This proves (d). ∎

### 5.4 Why this is not a corollary of Theorem 14's statement

Theorem 14 (75) has the shift zh_Y(s; P, ξ): a scalar multiple of one fixed response (ST1 L848–851). For a vector ζ, the response h(s; P, S(v(s, ζ))) is a nonlinear function of ζ. It is not zh for any fixed h and scalar z, because DR's response is nonlinear in its source (the background map solves a nonlinear critical equation, ST1 L292–311). What Theorem 14's proof uses of zh is only the bound n_b(zh) ≤ |z|D_srce^{−μd} and holomorphy in z (ST1 L816, L878). Theorem V replaces these by (5.1) and joint holomorphy in (s, ζ), which (DR-ζ) supplies. Every other step is Theorem 14's, verbatim.

### 5.5 Theorem V′: uniformity in the complex input pair

The physical input pair P is used only in Step 8. This matters for CI (§8.1).

**Theorem V′.** [proved, from the same inputs as Theorem V] Let 𝒪 be the set of complex input triples P' = (U, A', 𝐉') with the fixed real factor U of the main step, lying in 𝒟_{a|+} with every working core and every ceiling of ST1 hypothesis 2 (round-3 form, ST3 L399). Define 𝐡(P'; s, ζ), Π_f(P'; s, ζ) and F_f(P'; s, ζ) by (4.2)–(4.4) with P' in place of P. Then on 𝒪 × 𝕊_{X_f} × 𝔻_{R_V}: Π_f(P'; s, ζ) lies in the restricted target chain domain with half of every gap left; F_f is jointly holomorphic in (A', 𝐉', s, ζ) on the fixed-U fibre and |F_f| ≤ b_f (for (I): Re F_f ≤ C_ΨV°); (L3), (L4) (at real P'), and (L5) hold for each fixed P'.

*Proof.* Steps 0–7 and 9–11 of §5.3 do not use that P is physical. They use: P' ∈ 𝒟_{a|+} with the ceilings (Step 5); DR at the input pair P', which is holomorphic "in its complex input pair, datum and |s_Δ| < e^{κ̄}" (ST1 L119) with (4.1) on its domain ((DR-ζ) is stated for every input pair in DR's pair domain, which contains 𝒪 by ST1 hypothesis 3, L842); Lemma 4 at the shift; Lemma 11 at the input point P'. Joint holomorphy in (A', 𝐉') follows because every map in the composition is jointly holomorphic in its complex arguments at fixed U (DR in its input pair; (10) in (A', H); f on the fixed-U fibre). The term h(𝟏; P', S(v₀)) now depends holomorphically on P', and the subtraction in (4.3) still cancels at ζ = 0 for each P'. ∎

*Reading.* The source S(v) of (FL-main) depends on V = M_−(U), the datum of the real factor, which is fixed on 𝒪. So the same completed source is fed to DR at every P' ∈ 𝒪. This is how ST1 Theorem 14 treats the input pair (its h_Y(s; P, ξ) is evaluated at a general P of the input domain, ST1 L850).

---

## 6. The radius

### 6.1 The radius lemma

**Lemma R.** [proved from Theorem V, Lemma W (§7.1) and Lemma T] Put R := c_Rℓ^q with **c_R := 1**. Under (Tq), (T1)–(T3), (V1)–(V6) and (W0) of §7.1, every f ∈ 𝔉 admits the data of (L) with R_f := R. That is, R_f ≥ c_R(log θ_{i−1})^q.

*Proof.* For the kinds (S), (Z), (E, R), (B), (K), (I), Theorem V gives holomorphy on 𝕊_{X_f} × 𝔻_{R_V} with R_V = R (§7.2–§7.7). For (W), Lemma W gives holomorphy on 𝔻_R under (W0) (§7.1). ∎

*Each condition, by kind.* (V1) is a floor on C₀. (V2)–(V5), (T1)–(T3) and (W0) are ceilings on γ: each has the form sup_{θ≥γ^{−2}}h(θ) ≤ c with h → 0, because δ_src = A₁gℓ^{𝔭₀}, gℓ^q, ℓ^{𝔭₀−q} and ‖gŷ‖ ≤ C_Aδ_src all tend to 0 (SA L19485). (V6) is a floor on M. §9 places each constant in the order.

*Remark (SA's c_R and ours).* SA's response bracket asks ρ ≥ c_Rα/δ with c_R allowed to contain e^{−Cκ̄} (SA L15161–15163). In scaled units this is a fluctuation radius 𝔟ρ ≥ c_R^{SA}C₀ℓ^q/A₁·A₁ = c_R^{SA}C₀ℓ^q. Our R = ℓ^q is SA's radius with the κ̄-loss c_R^{SA} ≍ e^{−Cκ̄} compensated by the floor (V1) on C₀. This is admissible because C₀ comes after κ̄ (SA L19469–19470; C4 L40).

### 6.2 The screened radius, and a correction to PAN Lemma 7.4

PAN Lemma 7.4 (PAN L279–289) defines, for an object attached to the live region, R_f as "the largest radius such that ... the regional shift caused by the source ζ stays within half the room", and claims R/R_f ≤ C_scr(ℓ/ℓ_m)^qe^{−5μLMŘ_i}. Two points of that claim fail. (i) The source must stay in DR's source ball and in the chart ball, so R_f ≤ s_D/(C_Ac_Tge^{κ̄}) ≍ e^{−Cκ̄}/g whatever the distance. Since Ř_i ≍ (log θ)^r with r ≥ 2 (C4 row 2), e^{5μLMŘ_i}ℓ^q is much larger than g^{−1} = e^{ℓ/2}, so the claimed R_f exceeds the cap. (ii) PAN applies (S) directly with rate μ; after pinning the rate is μ/2 (ST1 Lemma 4 (27)), and the layer argument costs another factor 2.

**Proposition S (screened radius).** [proved from Theorem V's proof and Lemma Q] Let f be an activity of kind (S), (Z), (E, R), (B), (K) or (I), and let D_f := min_{b∈ℛ_X}d_+(b, 𝒮). Put

  c_cap := min{s_D/2, C_Ac_chL^{−9}/2, ε_lev/(4e^{μ}K_pinC_DE_{κ̄})},  R_cap := c_cap/(c_TC_Ae^{κ̄}g),
  R_f^{scr} := min{c_Rℓ^qe^{μD_f/4}, R_cap}.

Assume (V1)–(V6) and, in addition, the ceilings on γ: 3K_pinC_DE_{κ̄}C_Aδ_src < ε_lev/(4e^{μ}), C_Aδ_src < s_D/2 and ‖gŷ‖_∞ < c_chL^{−9}/2. Then the conclusions of Theorem V hold on 𝕊_{X_f} × 𝔻_{R_f^{scr}}. Consequently

  R/R_f^{scr} ≤ e^{−μD_f/4} + c_Rc_TC_Ae^{κ̄}gℓ^q/c_cap.   (6.1)

*Proof.* Repeat Theorem V's proof with R_V replaced by R_f^{scr}. Step 1: c_Tge^{κ̄}R_f^{scr} ≤ c_cap/C_A, so ‖S(v)‖ ≤ C_Aδ_src + c_cap < s_D, and v is in the chart ball. Step 3: the endpoint tops y of X lie within weighted distance 2 of reads (ST1 L186: a site-to-top path has weighted length less than 2), so ε̂_y ≤ K_pinA_Ve^{μ}e^{−μD_f/2} ≤ e^{μ}K_pinC_DE_{κ̄}(3C_Aδ_src + c_cap) < ε_lev/2. Step 4: by the second part of Lemma Q, ‖𝐡^δ‖_w ≤ C_levA_VC_Qe^{−μD_f/4}/((1 − θ_s)β_sC₀gℓ^q). The δ_src part is at most r_*/5 by (V2). The fluctuation part is at most c_TC_levC_DE_{κ̄}C_AC_Qe^{κ̄}R_f^{scr}e^{−μD_f/4}/((1 − θ_s)β_sC₀ℓ^q) ≤ r_*/5 by R_f^{scr} ≤ c_Rℓ^qe^{μD_f/4} and (V1). Steps 5–11 are unchanged. (6.1) is 1/min{a, b} ≤ 1/a + 1/b. ∎

*Consequence for PAN.* For f attached to the live region, PAN (G-gap) gives D_f ≥ 10LMŘ_i − C' in the input metric (PAN L163, L277; passing through layers of lower level only increases d_+). So (6.1) gives R/R_f ≤ e^{μC'/4}e^{−(5/2)μLMŘ_i} + Cgℓ^qe^{κ̄}/c_cap. The age factor C_scr(ℓ/ℓ_m)^q of PAN Lemma 7.4 does not appear: the layer separation is already inside Lemma Q (4^ν·4^{−(ν−3)_+} ≤ 64). Both terms of the corrected bound tend to 0 faster than every power of ℓ (r ≥ 2 for the first; g = e^{−ℓ/2} for the second). In PAN Lemmas 7.5, 7.6 and Step 5 of Theorem P (PAN L295–297, L335–337, L391–397), replace C_scr2^q(ℓ/ℓ_m)^qe^{−5μLMŘ_i} by e^{μC'/4}e^{−(5/2)μLMŘ_i} + Cgℓ^qe^{κ̄}/c_cap; the polylogarithmic prefactors ℓ^{2𝔭₀+τ_B}, ℓ^{τ_I} are then still killed, and only ℓ₃ in PAN L395 changes. [proved, for PAN's use; PAN's other steps not rechecked here]

---

## 7. The seven kinds

For each kind: the set X_f, the function F_f, and (L1)–(L6) with the size ω_f. Throughout R_f := R = c_Rℓ^q (Lemma R).

### 7.1 (W) Wilson and Jacobian remainder, and the coupling-profile difference

These are functions of the fluctuation directly, at the fixed new background. They do not pass through the response.

**(W-in)** [input: NL1(3), Balaban CMP 119 (3.15) and (3.25) as CA-II L79920–79938, L79979–80013 quote them; reading]. The sum 𝐏^{(i−1)}(g, (ŷ, y)) plus the coupling-profile part of the brace equals a constant, plus a part of −½⟨y, Ay⟩ − ⟨𝐅, y⟩ (TT (3.1), TT L118), plus Σ_{f∈𝔉_W}[f(w_f(y)) − f(w_f(0))]. Here each f ∈ 𝔉_W has a base p_f (a plaquette or a block of the linearised constraint), and w_f(y) := g(ŷ ⊕ Σ_ay_{·,a}T_a) restricted to the bonds within lattice distance R_𝐂 of p_f (R_𝐂 the range of Balaban's 𝐂 and of the nonlinear correction hD̃; TT (ℓ), TT L124). Each f is holomorphic on the polydisc {w : |w|_∞ < c_W}, with c_W > 0 fixed with L, real at real w, with |f| ≤ B_f there, and with all partial derivatives of order < k_f vanishing at w = 0, in the joint variable w. The expected values, from the structure of the terms:

- (W1) cubic Wilson remainder per plaquette, at the constant weight x_{i−1} ≤ (5/4)θ_{i−1}: B_f ≤ 3C_ax_{i−1}, k_f = 3 (a_p is entire and |a_p| ≤ C_a on the polydisc; the Taylor part of degree ≤ 2 is moved to the Gaussian part, and by Cauchy it is at most 2C_a on the half-polydisc);
- (W2) Haar density and constraint Jacobian remainders per block: B_f ≤ C_J, k_f = 1;
- (W3) coupling-profile difference per plaquette, weight |x(p) − x_{i−1}| ≤ C_x(1 + Ř_i) on the plaquettes near Λ_i^{pre} (SA L17886–17888 as PAN L105 reads it): B_f ≤ 2C_aC_x(1 + Ř_i), k_f = 1;
- (W4) cross terms of the nonlinear correction hD̃ with the background current: B_f ≤ C_hx_{i−1}ε_{i−1}, k_f = 2.

Condition (W0): c_Tg(‖ŷ‖_∞/g + R) ≤ c_W/2, a ceiling on γ.

**Lemma W (Schwarz with a zero of order k).** [proved; classical] Let φ be holomorphic on {w ∈ ℂ^n : |w|_∞ < c}, with |φ| ≤ B and all partial derivatives of order < k zero at 0. Then |φ(w)| ≤ B(|w|_∞/c)^k.

*Proof.* Fix w ≠ 0 and put e := w/|w|_∞. The function t ↦ φ(te) is holomorphic on |t| < c, bounded by B, and has a zero of order ≥ k at 0, since its t-derivatives at 0 are sums of partial derivatives of φ of the same order. So ψ(t) := φ(te)/t^k extends holomorphically to t = 0. On |t| = c' < c, |ψ| ≤ B/c'^k; by the maximum principle this holds on |t| ≤ c'. Let c' ↑ c, and take t = |w|_∞. ∎

*Presentation.* X_f := the set of cubes that meet the R_𝐂-neighbourhood of p_f. By (V6), M > 2R_𝐂 + 2 once R_σ ≥ R_𝐂, so this neighbourhood has diameter < M and meets at most 2 consecutive cubes in each direction: |X_f| ≤ 2⁴, and X_f is *-connected. F_f(s, ζ) := f(w_f(ζ)), independent of s.

- (L1) |w_f(ζ)|_∞ ≤ ‖gŷ‖_∞ + c_Tg|ζ|_∞ < c_W/2 on 𝔻_R by (W0); f ∘ w_f is a holomorphic function of ζ (w_f is affine). No s-dependence.
- (L2) by (W-in).
- (L3) F_f depends only on ζ on the bonds within R_𝐂 of p_f, whose cubes lie in X_f ⊂ K_{X_f}(s) for every s, and not on s.
- (L4) f real at real w, and w_f real at real ζ.
- (L5) F_f(s, 0) = f(w_f(0)) =: f₀ for every s.
- (L6) two-sided. By Lemma W in the joint variable, on 𝔻_R, |F_f − f₀| ≤ |f(w_f(ζ))| + |f(w_f(0))| ≤ 2B_f(c_Tg(‖ŷ‖_∞/g + R)/c_W)^{k_f} =: ω_f. With ‖ŷ‖_∞ ≤ C𝔟 ≤ R (a ceiling on γ, since 𝔟/R = A₁ℓ^{𝔭₀−q}), this gives:
  (W1) ω_f ≤ 6C_a(5/4)θ(2c_TgR/c_W)³ = C_{W1}gR³ = C_{W1}gℓ^{3q};
  (W2) ω_f ≤ C_{W2}gℓ^q; (W3) ω_f ≤ C_{W3}(1 + Ř_i)gℓ^q; (W4) ω_f ≤ C_{W4}ε_{i−1}ℓ^{2q}·θg² = C_{W4}A₀gℓ^{𝔭₀+2q}.
  The constants C_{W·} depend on L, C_a, c_W, C_J, C_x, C_h and c_T only; they do not depend on M or κ̄. Each ω_f is ≤ C(L)(1 + Ř_i)gℓ^{3q} ≤ C(L)gℓ^{3q+r}, which is PAN's (L-W) (PAN L151) with an M-independent constant.

The step's own δ-elimination factor z^{(i−1)} and Gaussian normaliser stand outside the integral (CA-II L79990) and do not depend on y; they are constants and are not in 𝔉.

### 7.2 (S) Strip

**(S-in)** [input: NL1(3), LF1(4); SA L17518–17526, L17541]. The strip part V^{(i−1)}(S_i, (ŷ, y)) of (3.25) (CA-II L80001) is, up to a constant, Σ_{f∈𝔉_S}[f(P_old(y)) − f(P_old(0))], where each f is a carried pair function (ST1 L101) of the old background near the strip, with support X near S_i, bound b_f on its declared domain under (Tq), and the interface of (ST-main) hypothesis 4. *Reason:* the strip quantities depend on the fluctuation through the background average V^{bg} (SA L17518–17522), i.e. through the old background, which is the pair P_old(y) = P ∔ h(𝟏; P, S(gŷ ⊕ u(y)))^δ.

*Presentation.* X_f := X^↑ (connected because X is connected and the read carriers are neighbourhoods of X). F_f := (4.4). By Theorem V: (L1) (b); (L2) (f); (L3) (c); (L4) (d); (L5) (e); (L6) two-sided with ω_f := 2b_f, since both F_f(s, ζ) and f₀ are values of f on its domain (Theorem V(a)).

### 7.3 (Z) δ-elimination factors

Two subkinds.

- *The step's own factors* z^{(i−1)}(c), c in Λ_i: they stand outside the conditional integral (CA-II L79990: z^{(k)} before ∫dA) and depend on the new background only. So f is constant in y. Take X_f := the cube of c, F_f :≡ f₀. (L1)–(L6) hold trivially with ω_f = 0; these terms drop out of P.
- *Carried factors* (SA L17534–17537, L17562; drop-outs SA L17654). **(Z-in)** [input: NL1(5) (R-cov: elimination factors covariant, `kept-cov.md` (8), AS L278), LF1(4)]. log z^{(j)}(c) is a carried pair function on its declared domain under (Tq), with bound b_z(c), and the interface of hypothesis 4. *Note:* the logarithm is well defined because z^{(j)}(c) is a Jacobian of the δ-elimination at a background near a regular one; the input states the bound directly for the logarithm.
  Presentation as in §7.2, with ω_f := 2b_z(c).

### 7.4 (E, R) Regular terms of every level, healed Mayer terms included

**(E,R-in)** [input: IN1 (I-5) (IN1 L70–78), NL1(3), ST1 hypothesis 4]. Each term E^{(j)}(X), R^{(j)}(X), j ≤ i − 1, carried to the main step of level i, is a carried pair function of the current (old-level) pair on its declared domain under (Tq), with bound b_f from the class (‖E^{(j)}‖_{j,κ} ≤ E₀, ‖R^{(j)}‖ ≤ g_j^{κ₀}, with forgetting and radius-ratio weights, IN1 L76, SA L4870–4873). This includes the healed-family terms 𝐑'_♯(Y) that entered R^{(k)} at a healing level k (SA L17996–17997), whose domain 𝒟_ext contains the chain domain by LF1(5) (PAN Theorem D1, PAN L341–347).

*Presentation.* X_f := X^↑; F_f := (4.4) minus nothing: the brace subtracts the value at U_i, a function of R, which cancels in P. By Theorem V, (L1)–(L5) hold, and (L6) is two-sided with ω_f := 2b_f.

### 7.5 (B) Boundary terms of every origin, drop-out terms included

**(B-in)** [input: (R23) = SA L6200–6202 with NL1(1); ST1 hypothesis 4]. Each boundary term B_{𝒮}(j, X, o), of any origin of SA L6185–6188, including drop-out terms (SA L17654) and healed Mayer terms with a standing object in their domain (SA L17997), is a carried pair function on its declared domain under (Tq), with |B| ≤ 𝖡e^{−κd^♮_j(𝒮;X)}.

*Presentation.* Fix a minimising exempt tree T with family 𝖥 for X (SA L6191–6195). X_f := X^↑ ∪ T ∪ ∪𝖥. This is connected: X^↑ is connected and contains X; the tree graph on T and the members of 𝖥 is connected and meets X (PAN L154). F_f := (4.4). By Theorem V, (L1)–(L5) hold, and (L6) is two-sided with ω_f := 2𝖡e^{−κd^♮(𝒮;X)} (PAN (L-B), PAN L154). Enlarging X_f beyond X^↑ is allowed by Theorem V (X_f ⊃ X^↑ connected), and it only weakens (L3).

### 7.6 (K) Kept forms of standing operations, drop-outs included

**(K-in)** [input: SA L17562–17564; LF1(4); NL1(5) (A^rel pair functions, `gates/kept-cov-check.md` Defect 1, AS L278)]. For each component 𝔨 of a live large-field region or of a drop-out, f(𝐩) := −½⟨A', Δ^{loc}_𝔨(𝐩)A'⟩, with A' the stored field (an entry of 𝔮_X, fixed) and Δ^{loc}_𝔨 a carried pair function, is holomorphic on its declared domain under (Tq), real at real pairs, and its oscillation there is at most osc_f := C_Kp₀(g_{j_f})²e^{−κd^♮(𝒮;X_f)} (SA L17564).

*Presentation.* X_f as in §7.5 (exempt convention, PAN L157). F_f := (4.4); the stored A' enters through 𝔮_X and stays fixed (Theorem V(a)). By Theorem V, (L1)–(L5) hold. (L6) is two-sided in oscillation form: F_f(s, ζ) and f₀ are both values of f at points of its domain, so |F_f − f₀| ≤ osc_f =: ω_f. A bound on |f| itself would be of order p₀² per bond (SA L17558: |A'(b)| ≤ Cp₀(g_j)), which is why the oscillation form of (L6) (§1.1) is used.

### 7.7 (I) Standing islands

**(I-in)** [input: IN1 (I-8) (IN1 L90–94) = LF1(4); SA L17822–17826; ST1 hypothesis 4 with the island's records]. For a standing island X formed at level m with frame r, internal record ω and stored variables ξ (all in R), Ψ_ω(ξ; 𝐩) := Φ_ω(ξ; 𝐩) − Φ°_ω(ξ) is holomorphic in 𝐩 on U^c_m(X^~, α_{0,m}, α_{1,m}), real at real pairs, and Re Ψ_ω ≤ C_ΨV°(ω) there. Moreover the island's read records are among the chain records, so the chain domain restricted to X^~ is contained in U^c_m(X^~, α_{0,m}, α_{1,m}). *Note:* under (Tq) the island's domain U^c_m has SA's radii α_{ι,m} (SA L17274, L17804), so this inclusion is the statement that the island's formation records are SA's U^c_m clauses; under (Tε) it would compare two different tables.

*Presentation.* X_f := X^↑ (the read set X^~ with carriers; connected). F_f(s, ζ) := Ψ_ω(ξ; Π_f(s, ζ)). Theorem V applies with the one-sided bound in place of b_f: Steps 1–6 do not use b_f, Step 7 uses only holomorphy of the activity on its domain, and Steps 8–11 are unchanged. So (L1)–(L5) hold. (L6) is one-sided: Re F_f ≤ C_ΨV°(ω) = f₀ + ω_f with ω_f := C_ΨV°(ω) − f₀. Here f₀ = F_f(𝟏, 0) = Ψ_ω(ξ; 𝐩₀) is real (reality, (L4)) and ≤ C_ΨV° because 𝐩₀ := Π_f(𝟏, 0) lies in U^c_m. So ω_f ≥ 0. PAN Lemma Q and Theorem D2 (PAN L301–331) then bound ω_f ≤ C_I(M)ℓ_m^{τ_I}.

---

## 8. The theorem

**Theorem L ((L)).** [proved from the inputs listed] Assume:

- (Tq) with (T1)–(T3) [design; Lemma T];
- (ST-main), (FL-main), (DR-ζ), (DR-loc) (§4.1);
- (W-in), (S-in), (Z-in), (E,R-in), (B-in), (K-in), (I-in) (§7);
- (V1)–(V6) and (W0) (§5.2, §7.1).

Then for every history, every level i, every value of R and every term f of each of the seven kinds of PAN §3, there are a nonempty connected cube set X_f, the radius R_f := c_R(log θ_{i−1})^q with c_R = 1, and a function F_f : 𝕊_{X_f} × 𝔻_{R_f} → ℂ satisfying (L1)–(L6) of §1.1. The sizes are: ω_f = 2b_f for (S), (Z), (E, R), (B); ω_f = osc_f for (K); ω_f = C_ΨV° − f₀, one-sided, for (I); ω_f ≤ 2B_f(2c_TgR/c_W)^{k_f} for (W); ω_f = 0 for the step's own z-factors. For the kinds other than (W), Proposition S gives the larger radius R_f^{scr} with (6.1).

*Proof.* §7.1 for (W) (Lemma W); §7.2–§7.7 for the other kinds (Theorem V). The radius is Lemma R. The conditions are uniform in the history, the level, R and the volume, because each is a statement about constants or a ceiling on γ in the supremum form, and the bounds of Theorem V are suprema of local quantities. ∎

*Use in PAN.* Theorem L is PAN's (L) (PAN L134–141) with (L6) in its oscillation form, which PAN's Lemma 5.3(a) accepts (§1.1). PAN's §1.2 definition c_R := C₁/(4C_𝐂C_H) (PAN L55) is replaced by c_R := 1, and the corresponding row of PAN's order table (PAN L432, "no: after M and κ̄") becomes "yes: fixed at row 1". PAN Lemma 7.4 is replaced by Proposition S (§6.2).

*On the round-3 domains.* Theorem L holds with ST1's round-3 domains (c*, smoothed lifts, lifted cores, witness bounds g_QΛ_Qr₀(i)), and also with (Tq0) of Proposition U. Theorem V's proof cites ST1 Lemmas 4, 5, 8, 11, 12, 13 and Theorem 14; ST3 replaces Lemma 9 by 9′ and Lemma 11's core paragraph by 11′ (ST3 L200), and Lemma T3 puts all of them under (Tq). The physical identification of Step 8 uses Lemma 12 with ST3 Theorem F4's main-step clause (ST3 L392, L402). [proved]

### 8.1 The consumer interface CI

**What CI says** (ST3 L256). For every carried activity f supplied by NL1/LF1 at a structure σ, its declared domain contains the ST1 chain domain 𝒟_{a|σ}, and |f| ≤ b_f there, with the interface of ST1 L101.

**(L) does not imply CI.** Theorem L bounds F_f = f ∘ Π_f, i.e. f on the set Π_f(𝕊 × 𝔻_R) of pairs reached by the fluctuation substitution. That set has the dimension of (s, ζ), while 𝒟_{a|σ} is open in the space of all complex pairs (A', 𝐉) on the support. A bound on the smaller set says nothing about f elsewhere in the domain. In the other direction, Theorem L *uses* CI: it needs f bounded on the target chain domain (Theorem V Step 7). So CI is an input of (L), not a consequence.

**What (L) gives towards CI.** CI is an induction over structures, and (L) in the form of Theorem V′ is one half of its inductive step.

**Proposition CI-ind.** [proved, as a reduction] Order the structures of a finite history. Suppose:
- (CI-old) CI holds for every activity formed at a structure before σ;
- (CI-form) at σ, each newly formed activity f is given by NL1's or LF1's formation formula (for the regular gas: the cutoff Gaussian integral and Mayer expansion of SA L14276–14810; for the large-field terms: the operation of LF1), and that formula, at each fixed complex input pair P' ∈ 𝒪_σ (the input domain of σ, as in Theorem V′), gives |f(P')| ≤ b_f whenever (i) every old factor of its integrand, as a function of the free fluctuation and switches, satisfies the conclusions of Theorem V′ at P' with radius R, and (ii) the fibre precision 𝖠(P') satisfies (I-1)(a)–(d) (IN1 L57–61) and the Gaussian comparison (I-2) applies at P'.

Then CI holds at σ for the activities formed there.

*Proof.* Let f be formed at σ and P' ∈ 𝒪_σ. The old factors of f's integrand are activities formed before σ. By (CI-old) they are bounded on their chain domains, which is ST1 hypothesis 4 for them. ST3 §6 supplies hypotheses 1–3 and 5 (ST3 L396–408). So Theorem V′ applies to each old factor at P', with radius R = c_Rℓ^q, uniformly in P' ∈ 𝒪_σ: (i) of (CI-form) holds. (ii) is a hypothesis. (CI-form) then gives |f(P')| ≤ b_f at every P' ∈ 𝒪_σ. Holomorphy of f on the fixed-U fibre: the formation formula is a locally normally convergent series of integrals of integrands that are jointly holomorphic in P' (Theorem V′), with a majorant uniform in P' (the bound of (CI-form) at each P' is uniform); Lemma 5.5 of PAN (PAN L208–210) and Weierstrass give holomorphy. Reality and covariance are those of the integrands. So f satisfies the interface of ST1 L101 on 𝒪_σ, which is its declared domain. ∎

The induction starts at the bare measure, whose activities are Wilson plaquette terms, entire in the pair and bounded on any domain under the absolute ceilings (T3).

**Exactly what is missing for CI.** (CI-form). It is NL1's and LF1's own content (B1, B4 and the UM argument for NL1; the prepared-structure bounds for LF1), stated *pointwise in the complex input pair of the ST1 domain* instead of on SA's printed domains. The inputs that (CI-form) itself names are:

1. **(I-1) at complex layered stage pairs**, ⟦PR-lay⟧ (IN1 L62: "(b)–(c) at real critical backgrounds [C] ... at complex single-layer pairs [C]; at layered stage pairs ⟦open: PR-lay⟧"). The ST1 domains contain such pairs at every stage, so (CI-form)(ii) needs it. This is the first open item on CI's path that I can name from the library.
2. The structural identities of the actual gas (heredity, normalised functional, wall factorisation), (I-3) (IN1 L66): [SS].
3. The rebuild of activities on intrinsic rather than (R5) tower domains (AS L236), which is the content of "declared domain = ST1 domain".

Under (Tq0) (Proposition U) the lift adds nothing to this list; under (Tq) with ST1's smoothed lifts, (CI-form) must also be proved with the lift factors in the domain radii.

**On the order of the constants of b_f.** CI asks that the constants of b_f be fixed before κ and independent of M and κ̄, except declared amplitude factors entering later ceilings (ST3 L256). For the class activities, b_f is E₀, g_j^{κ₀}, 𝖡e^{−κd^♮}, C_Kp₀²e^{−κd^♮}, C_ΨV° (IN1 L76, L92; SA L17564). SA chooses E₀ and 𝖡 after M (SA L19469–19470; C4 L42, row 17). So CI as worded would contradict SA's order. What ST1 and (L) need is weaker and true: **no constant fixed before κ reads b_f.** In Theorem 14, b_f enters only the output bound (77) (ST1 L864–866). In Theorem V it enters only |F_f| ≤ b_f. In PAN it enters only N^♮ and hence the final ceiling X_P (PAN L433–436). I recommend that CI be restated with this reading.

---

## 9. The order of constants

The IN1 constraint (IN1 L310–336; C4): every constant read by a choice before κ must be fixed before κ, be independent of M and κ̄, and contain M only as a lower bound.

| Constant or condition | Where | Fixed at | Before κ? Independent of M, κ̄? |
|---|---|---|---|
| c_R = 1 | Lemma R | row 1 (a number) | **yes; yes** |
| q, 𝔭₀, r; q > 𝔭₀ + 2r | (T1), Prop. R° | C4 row 2 | yes; yes (IN1 L347) |
| c_T = 3 | §1.2 | absolute (SU(2) basis) | yes; yes |
| (1 − θ_s)β_s | Lemma Q | ST1 row 1 | yes; yes |
| μ, C_car, ρ₀ with μρ₀/2 ≥ log 16 | Lemma Q | ST1 rows 2–3 (L133–134) | yes; yes |
| C_Q = 256e^{μC_car/2} | Lemma Q | determined after ST1 row 3 | yes; yes |
| C_lev, K_pin, ε_lev | Lemma 4 | ST1 row 2 ("independent of depth and M, κ̄", L253) | yes; yes |
| C_D, C_A, R_σ, c_ch | (DR-ζ), (FL-main) | ST1 row 2 (L133) | yes; yes |
| r_* | Lemma 11 | ST1 row 6 (L137) | yes; yes |
| C_a, c_W, C_J, C_x, C_h, R_𝐂, C_{W1}–C_{W4} | §7.1 | with L (Lie-group charts, Balaban's 𝐂) | yes; yes. C_x reads the profile rule, fixed with L and β_s [reading of SA L17886–17888] |
| E_{κ̄} | (DR-ζ) | after κ̄ (ST1 L124) | no: depends on κ̄. Read only by (V1), (V2)–(V4), c_cap, i.e. by the floor on C₀ and by ceilings on γ |
| s_D = ε_De^{−c_Dκ̄} | (DR-ζ) | after κ̄ | no. Read only by ceilings on γ and by c_cap |
| **(V1)** C₀ ≥ 5c_TC_levC_DC_AC_Qe^{κ̄}E_{κ̄}c_R/((1 − θ_s)β_sr_*) | §5.2 | floor on C₀, C4 row 16 (after M, κ̄) | C₀ is a row-16 constant; the floor reads only constants before it. C₁ ≫ MC₀ (C4 L40) then follows it upward |
| (T1), (T2), (T3), (V2)–(V5), (W0), Prop. S ceilings, Prop. R° ceilings | §3–§7 | ceilings on γ, C4 rows 21–22 | supremum form (SA L19485) |
| (V6) M ≥ R_σ + 3; M > 2R_𝐂 + 2 | §5.2, §7.1 | floor on M, C4 row 12 | M only as a lower bound; already implied by M ≥ L⁴M'₁ (ST1 L139) |
| c_cap, R_cap | Prop. S | determined after κ̄ | read only by ceilings on γ (PAN's ℓ₃) |
| ω_f for (W): C(L)gℓ^{3q+r} | §7.1 | — | M-independent; read only by PAN's ceiling X_P |
| b_f of the carried kinds (E₀, g^{κ₀}, 𝖡, C_Kp₀², C_ΨV°) | §7, §8.1 | E₀, 𝖡 at C4 row 17 (after M), as SA L19469–19470 | **not** before κ, and not needed before κ: read only by |F_f| ≤ b_f, Theorem 14's (77), and PAN's X_P. See §8.1 on CI's wording |
| C_U (Prop. U); (U1)–(U3) | §3.5 | C_U before κ (ST1 rows 2–3); (U1)–(U3) ceilings on γ, (U3) after M | yes for C_U; ceilings otherwise |

*No cycle.* No constant chosen before γ reads E_{κ̄}, s_D, c_cap or R_cap, except through the floor (V1) on C₀, which is assigned to C₀ at row 16, after κ̄ and M (SA L19469–19470). The constants introduced here that precede κ (c_R, c_T, C_Q) depend on nothing chosen at or after κ. The floor of ST1 row 5 on α₀ is no longer needed for formation under (Tq); it is replaced by the ceiling (T1) (Lemma T, item 6). ST1 row 9 (A₁/A₀ small for the main-step bound, ST1 L140) becomes a ceiling on γ, (V2), because the main-step amplitude now carries ℓ^{𝔭₀−q}.

---

## 10. Inputs, owners, and whether the owner states them in this form

| Input | Owner | Where stated | In this form? |
|---|---|---|---|
| (Tq) | ST1 (design), SA | SA L6033; IN1 L44 | **No: ST1 uses (Tε) (ST1L92, ST1d2 L130).** Lemma T shows ST1 runs under (Tq); Prop. C shows (Tε) does not give (L) |
| (ST-main) hyp. 1, 2, 5 | ST1 | ST1 L840–844 | yes, as hypotheses; hyp. 2 at every transition is **Outstanding** at M, R, B, F (ST1 L876) |
| (ST-main) hyp. 4 on (Tq) domains | NL1, LF1 | ST1 L843; ST1d2 hyp. 6 | yes as an interface; the activities on the (Tq) domains are SA's class requirement (SA L4870–4873) |
| (FL-main) | ST1 | ST3 Remark F8 (L390), with Theorem F4; CA-II L79920–79938 | yes, in round 3 (F8); the Lipschitz form (c) is F4's (70) bound |
| CI (activities bounded on the round-3 chain domain) | NL1, LF1 | ST3 L254–266 | **Outstanding**; reduced here to (CI-form) by Proposition CI-ind (§8.1); first open item ⟦PR-lay⟧ |
| (DR-ζ) | ST1 (DR construction) | ST1 L119–124 | in substance; the complex source ball and the linear bound (4.1) [reading]; PAN L560 asks for it |
| (DR-loc) | ST1 | ST1 L119, L868 | **new statement** (which rows a component reads) |
| (W-in) | NL1(3) | CA-II L79920–80013 (Balaban (3.15), (3.25)) | no explicit holomorphy/size statement found [reading] |
| (S-in), (Z-in) | NL1(3), NL1(5), LF1(4) | SA L17518–17537, L17562 | as pair functions, in substance; bounds not stated |
| (E,R-in) | IN1 (I-5), NL1(3) | IN1 L70–78 | yes, as class bounds; status NL1 [O] through (D4) (AS L288) |
| (B-in) | NL1(1), class | SA L6200–6202 | yes |
| (K-in) | LF1(4), NL1(5) | SA L17562–17564 | yes (oscillation bound) |
| (I-in) | LF1(4) | IN1 L90–94; SA L17822–17826 | yes for the bound; the inclusion of the chain domain in U^c_m is natural under (Tq) and not stated |

---

## 11. Routes considered, and why the ones that fail fail

The radius claim is the only hard point of (L). Before settling on (Tq), I tried three routes that keep ST1's table (Tε). Each fails for an exact reason.

- **A1. Derive the vector statement from Theorem 14's scalar statement.** For a fixed real direction e, apply Theorem 14 to the source of y = te and continue in t. *Failure:* Theorem 14 is holomorphic in z for the shift zh_Y with h_Y the response to one fixed source (ST1 L848–851). The response to the source of ζ is not zh_Y for any scalar z, because DR's response is nonlinear in its source. Holomorphy along the line z ↦ zh_Y says nothing about ζ ↦ h(S(ζ)) away from ζ = 0 at the scale where nonlinearity matters. And in any case the scalar radius ρ_X > 1 times the actual source δ_src gives only |ζ| ≲ ρ_X𝔟 ≍ (A₀/A₁)ℓ^{𝔭₀}, not ℓ^q. Replaced by Theorem V, which goes through the proof.
- **A2. Keep (Tε) and enlarge α₁.** Under (Tε), the room in field units is ≍ α₀ε = α₀A₀gℓ^{𝔭₀}, so R_f ≍ (α₀A₀/(C_DE_{κ̄}C_A))ℓ^{𝔭₀}. To reach ℓ^q one would need α₀ ≳ ℓ^{q−𝔭₀}. *Failure:* α₀ is a constant fixed at ST1 row 5, before κ (ST1 L136), so it cannot grow with ℓ. Proposition C shows the bound R_f ≤ 2ρ_D/g ≍ α₁ℓ^{𝔭₀} is attained by an interface activity, so no argument inside the interface can do better.
- **A3. Use the lift λ.** ST1's radii carry the lift λ(x) ≤ C_λ(log θ)^{2r_R} (ST1 L616), which is a power of log θ. *Failure:* λ ≥ 1 is large only near operations, where formation exponents are positive (ST1 L598–616). In the bulk of Λ_i^{pre}, away from large-field regions, λ = 1 (Proposition C uses such a row c₀). And even where λ is maximal, ℓ^{𝔭₀+2r} < ℓ^q since q > 𝔭₀ + 2r. So (L) cannot hold uniformly on Λ_i^{pre} by the lift.
- **The route taken.** SA's own table (Tq) (SA L6033) makes the room ≍ C₀gℓ^q. Lemma T shows ST1 is homogeneous in the table, apart from formation floors (which become easier) and absolute ceilings (which stay ceilings on γ). Then Theorem V and Lemma R give R_f ≥ ℓ^q.

Two smaller routes were also met and replaced. **A4.** Leaving the stored part ŷ inside the localised source: then F_f(s, 0) is the localised response to ŷ, which depends on s, and (L5) fails; replaced by the difference construction (4.3). **A5.** An unmasked source: then F_f depends on ζ also on the one-cube layer around K_{X_f}(s), because a source row reads a neighbourhood of radius R_σ; (L3) then holds only with N₁(K), which would cost PAN Proposition 6.1(c) one shell. Replaced by the mask, at a cost e^{κ̄} paid by the floor (V1).

---

## 12. Status

### 12.1 Statements of this draft

| Statement | Where | Status |
|---|---|---|
| Proposition C ((Tε) does not give (L)) | §3.2 | [proved] |
| Lemma T (ST1 under (Tq)) | §3.3 | [proved], by inspection of every occurrence |
| Proposition R° (Outstanding R under (Tq)) | §3.4 | [proved] as an implication from ST1 (56)–(57); a by-product |
| (FL-main), (DR-ζ), (DR-loc) | §4.1 | [input], readings flagged |
| Construction (4.2)–(4.4): mask and difference | §4.2 | [design] |
| Lemma Q (main-step Q_X under (Tq)) | §5.1 | [proved] |
| Theorem V (vector main-step substitution) | §5 | [proved] from (ST-main), (FL-main), (DR-ζ), (DR-loc), Lemma T, Lemma Q |
| Lemma R (R_f ≥ c_Rℓ^q, c_R = 1) | §6.1 | [proved] |
| Proposition S (screened radius, cap) and the correction of PAN Lemma 7.4 | §6.2 | [proved] |
| Lemma W | §7.1 | [proved; classical] |
| The seven kinds | §7 | [proved] from the kind inputs |
| Theorem L = (L) | §8 | [proved] from the inputs listed, on round-2 and round-3 ST1 domains |
| Lemma T3 (round 3 under (Tq)) | §3.5 | [proved]; ST3 §5 from statements only |
| Proposition U (no lift needed under (Tq)) | §3.5 | [proved] by inspection; not checked |
| Theorem V′ (uniform in the complex input pair) | §5.5 | [proved] |
| Proposition CI-ind (CI reduced to (CI-form)) | §8.1 | [proved], as a reduction |
| CI itself | §8.1 | **[Outstanding]**: (CI-form) is NL1/LF1's formation content on ST1 domains |
| Order of constants | §9 | [proved] admissible (IN1 Lemma A.8) |

### 12.2 The first remaining Outstanding statement on (L)'s path

(L) has no Outstanding statement of its own. In round 2 the first open input on its path was ST1 Theorem 14 hypothesis 2 (chain admission, Outstanding at M, R, B, F; ST1 L876). ST1 round 3 claims M, R, B and F (ST3 L13–18; pass-1, not distilled), and its Corollary 14′ applies Theorem 14 at every transition "except CI" (ST3 L406). So the first open input on (L)'s path is now **CI** (ST3 L256), entering through ST1 hypothesis 4:

> For every carried activity f supplied by NL1/LF1 at a structure σ, its declared domain contains the ST1 chain domain 𝒟_{a|σ}, and on it |f| ≤ b_f with the interface of ST1 §1.

It is NL1's own obligation, and (L) is one half of its inductive step (Proposition CI-ind). Exactly what remains is (CI-form): NL1's and LF1's formation estimates, pointwise in the complex input pair of the ST1 domain. The first open item inside (CI-form) is ⟦PR-lay⟧, (I-1) at complex layered stage pairs (IN1 L62). Two corrections to CI as stated: the order requirement on b_f should read "no constant fixed before κ reads b_f" (§8.1); and under (Tq0) the lift part of CI disappears (Proposition U), leaving the intrinsic-domain rebuild (AS L236).

I did not attack (CI-form) here. It is the bulk of NL1 (B1, B4, UM) and of LF1(4), restated on the ST1 domains, and it is a separate submanuscript-sized task, not one lemma.

The new input statements of this draft, for their owners: (DR-loc) for ST1; the main-step reading (FL-main) for ST1/NL1; (W-in) for NL1(3); the adoption of (Tq) by ST1.

### 12.3 Checks this draft needs

- One check, by another model, of Lemma T: that the list of occurrences of r_ι in ST1 is complete, and that each is homogeneous, a formation floor, or an absolute ceiling.
- One check of Theorem V Steps 1–11, especially Step 10 (locality through (DR-loc) and the mask) and Step 4 (the arithmetic with (V1)–(V2)).
- One check of Proposition C (the interface example and the identity-theorem argument).
- ST1 to confirm (DR-ζ) and (DR-loc), and to decide on (Tq) or (Tq0).
- One check of Proposition U: that the lift enters ST1 and ST3 only at the places listed, and that (59′) follows from PROF, (56) and (58) as written.

*RAM and method.* No computation was run. Every source was read in bounded ranges, cited above.

End of pass 1 (L).

This file has 650 lines.
