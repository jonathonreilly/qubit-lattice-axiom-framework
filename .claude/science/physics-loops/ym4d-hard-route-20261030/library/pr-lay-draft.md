# PR-lay, pass 1: the fibre precision at complex layered stage pairs

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, pass 1 (long draft) of the input PR-lay of submanuscript PR1 (propagators on a background) of `library/ym4-assembly.md`. Research text. It is not an audit and grants no status. Nothing here is checked by another model. A later pass (Codex) distils it; a fresh session then reads it line by line; then it is frozen. No computation is a proof step. Every argument is a finite chain of inequalities, convergent series, one-variable holomorphy (Schwarz lemma, identity theorem, uniform limits) and set inclusions, so it is Lean-formalizable in the ordinary sense.

Credit. The setting, the separated sequences, the class of regular pairs, the six propagators, the fibre precision and its walk expansion, the complex site route and the geometry of the operation R are those of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the outline `YM4_sketch_500.tex` (SA), the complete account I (CA-I) and the three-dimensional manuscript `YM3_I.tex` (Y3), all at commit `31a47c543775`. The method is Tadeusz Balaban's: background-field propagators and their positivity (CMP 99 (1985) 389–434), the independent current (CMP 109 (1987), (1.10)–(1.14)), the random-walk expansions on cut-down sequences (CMP 99, pp. 408–410), the stage construction (CMP 122 (1989) 175, (1.24)). Jonathan Dimock's expositions of Balaban's renormalization group are the standard secondary reference. Library notes used, with their authors: `a2-layers.md`, `a2-full.md`, `h-walk.md`, `os-draft.md`, `in1-draft.md`, `nl1-L-draft.md`, `st1-draft3.md`, `a3-close.md` (Claude); `a2-curved.md`, `p82.md`, `st1-r2.md`, `layered-a3.md` (Codex); and their gates in `gates/`.

Line references. SA L = line of `scratchpad/sa/ym4.tex`; CA-I L = line of `scratchpad/sa/ca_I.tex`; Y3 L = line of `scratchpad/sa/YM3_I.tex`. A library reference `name L` is a line of `library/name.md`; `gate name L` is a line of `gates/name.md`. I quote line numbers before I say what a source proves or assumes. "SA states" means the text at those lines says so; it does not mean SA proves it.

Status words. **[P]** proved here, not checked. **[I]** an import: a statement proved elsewhere, with its status there named at the import. **[O]** open. **[SS]** stated or sketched in a source, not proved there. A step marked [P] is proved here *from* the imports it names.

---

## 0. Result in one page

**Theorem PR-lay (consumer form).** [P, as an implication from the imports (I-A)–(I-G) of §4.] Fix L ≥ L₀ and the constants of rows 1–7 of `c4-order.md`. There are numbers a > 0, b, H < ∞, μ₀ > 0, H₁ < ∞ and a ceiling κ_* > 0, all functions of L only (through the walk cube M₁ and gap number R₁ only as lower bounds), with this property. Let σ be any structure of a finite history at which IN1 evaluates the regular (UM) gas or NL1 evaluates (CI-form): a main-step input structure, after any number of stages, outputs and drop-outs. Let 𝐒^σ be the determining sequence in force there, U the actual real background in the step's gauge, and P′ = (U, A′, 𝐉′) an input pair of the step's domain. Then, once the coupling ceiling γ is below a value γ_PR that may depend on M, κ̄ and the radius coefficients:

- (a) 𝖠(P′) is complex symmetric for the bilinear transpose, and 𝖠(U, 0) is real symmetric;
- (b) Re⟨v, 𝖠(P′)v⟩ ≥ a|v|² for every v, hence on every compression to a coordinate subset; ‖𝖠(P′)‖ ≤ b;
- (c) |𝖠(P′)(x, y)| ≤ H e^{−μ₀ d(x,y)}, d the periodic ℓ¹-distance of base sites in level-k units;
- (d) |𝖠(P′)(x, y) − 𝖠(U, 0)(x, y)| ≤ η(P′) e^{−μ₀ d(x,y)} with η(P′) ≤ H₁ κ(P′), where κ(P′) is the largest local-scale size of the complex part (A′, 𝐉′) on the nest in force (Definition 3.3).

The same holds at the real reference (U, 0), with η = 0. (a)–(d) are IN1's (I-1)(a)–(d) (IN1 L57–61) with H_p(M) replaced by the M-free constant H₁, and they are NL1's (CI-form)(ii) at every P′ ∈ 𝒪_σ (NL1-L L518).

**How it is proved.** Two parts.

- *Part A (§5), an operator theorem.* At every complex regular pair, in SA's sense (SA L10129–10137), of every separated sequence, with radii below κ_*, (a)–(d) hold with constants of L only. The gap at the real reference and the kernel expansion on the whole class are imported (a2-layers Theorem A; h-walk Theorem H, (H1)–(H3), in the form that survived their gates). What is new is the perturbation bound (d): a Schwarz-lemma argument along the complex line z ↦ (e^{izηA′}U, z𝐉), which gives η linear in the complex radius with the constant 16H/a_h. The complex gap (b) then follows from the real gap and (d).
- *Part B (§6), admission.* Every pair at which the two consumers evaluate 𝖠 is a regular pair of a separated sequence with radii below κ_* once γ ≤ γ_PR. Separation of every sequence in force is SA Proposition 2.3 and `os-draft.md` Lemma 2.3. The real factor's bound in the units of the nest in force is ST1 Lemma 10, (59)–(60). The complex part's bound is the current-layer radius design of SA L6141–6152. The radii carry lifts λ ≤ C_λ(log θ)^{2r_R} and the table r_ι(m) = C_ι θ_m^{−1/2}(log θ_m)^q (SA L6033); the enlarged radii still tend to zero, as γ(2 log γ^{−1})^Q (Lemma B.4).

**The seam loss does not enter (§7.1).** The loss L^{2v}/L_♭^{2v} > 4^v of `layered-a3.md` (3) arises only when a field is measured in the scale of a *different* nest (a target tower) than the one in which it is controlled. 𝖠(P′) is a function of the pair (𝐔, 𝐉) and of V = M^k𝐔 on the nest in force (SA L14091–14107, L10200–10208). It reads no tower and no datum tube. Inside one separated nest the only scale changes are between adjacent layers, at a fixed L-cost. So no lift has to absorb a loss. The lifts only enlarge radii, and the coupling ceiling pays for that enlargement.

**What is not proved here.** PR1(5) as printed (assembly L187, = `layered-a3.md` (1)): tube distances of tower data along the stage path and the readout derivative bound. It is a statement about towers T_e, not about 𝖠. Its consumer is the stage response (`layered-a3.md` §1: "This is input (B) of `stage-resp.md`"), not (I-1). It stays [O], with `layered-a3.md` Lemma RC (its (51)) as its first open step. I recommend that the assembly split PR1(5) into PR1(5a) = Theorem PR-lay of this file and PR1(5b) = `layered-a3.md` (1).

**First remaining Outstanding on PR-lay's own path.** None inside this file. The imports carry their own status (table in §9). The first one in reading order that is not yet a checked statement is (I-G), the current-layer radius design of the consumer domain; it is a well-posedness requirement of NL1's formation formula, not an estimate (§6.3, §9).

**Line count** is reported in the session reply.

---

## 1. What the two consumers need

### 1.1 IN1

IN1 L57–61 states its import (I-1): "There are a > 0, b < ∞, H < ∞, μ₀ > 0, depending on L and the constants of `c4-order.md` rows 1–7 only, such that for every regular real background U and every complex pair P in its admitted core with radii a₀, a₁ and independent current j₀ below ceilings that may depend on M, the gauge-fixed fibre precision 𝖠(P) of SA L14097–14107 on the fluctuation coordinates satisfies: (a) 𝖠(P) is complex symmetric (bilinear transpose); 𝖠(U, 0) is real; (b) Re⟨v, 𝖠(P)v⟩ ≥ a|v|² for all v (on every compression to a coordinate subset, in particular); (c) |𝖠(P)(x, y)| ≤ H e^{−μ₀ d(x,y)}; (d) |𝖠(P)(x, y) − 𝖠(U, 0)(x, y)| ≤ η(P) e^{−μ₀ d(x,y)}, with η(P) ≤ H_p(M)(a₀ + a₁ + j₀)".

IN1 L62 gives its status: "(b)–(c) at real critical backgrounds [C] (A2 on separated layers, A3 real-critical chain); at complex single-layer pairs [C]; at layered stage pairs ⟦open: PR-lay⟧ (PR1(5))".

IN1 L807 narrows what Part A consumes: "Part A needs only (I-1)(b)–(d) *at the pair P itself and at its real reference (U, 0)*: a uniform gap a, entrywise exponential decay (H, μ₀), and an entrywise-decaying pair perturbation with *any* M-dependent prefactor H_p(M)." IN1 L808 adds the order requirement: "The constants (a, H, μ₀) must be fixed before κ. ... If the layered case could only be proved with constants depending on M or κ̄, the cycle would reappear".

IN1 L800 identifies the pairs: "the pairs of the hereditary core of the ordinary step, which under (D4) include lifted and stage (layered) pairs. At those pairs (I-1)(b)–(d) is the layered complex comparison PR1(5)". I correct the second sentence in §7.3: PR1(5) as printed is a different statement.

The distance in (c)–(d) is fixed in IN1 §A.1: "the positions of the fluctuation coordinates on a torus, d the periodic lattice ℓ¹-distance between their base sites".

### 1.2 NL1's (L) draft

NL1-L L518 states (CI-form): at each fixed complex input pair P′ ∈ 𝒪_σ, the formation formula gives |f(P′)| ≤ b_f whenever "(ii) the fibre precision 𝖠(P′) satisfies (I-1)(a)–(d) (IN1 L57–61) and the Gaussian comparison (I-2) applies at P′". NL1-L L528 names the first open input: "(I-1) at complex layered stage pairs, ⟦PR-lay⟧ ... The ST1 domains contain such pairs at every stage". NL1-L L377 defines 𝒪: "the set of complex input triples P′ = (U, A′, 𝐉′) with the fixed real factor U of the main step, lying in 𝒟_{a|+} with every working core and every ceiling of ST1 hypothesis 2".

NL1 also asks for (I-2) at P′. (I-2)'s hypotheses on the collared matrices are produced by IN1 Proposition A.5 from (I-1) (IN1 L217–266). So (I-1) at P′ is what this file must give.

### 1.3 The assembly, ST1 and OS

The assembly's PR1(5) (assembly L187) reads: "*Layered complex comparison* ⟦open: PR-lay⟧. On the full earlier-parameter and switch domains, along the stage path supplied by ST1, dist_∞(D_e(t), 𝒯_e^c) ≥ η_* and ‖∂_t F_a‖ ≤ C r_a^{lift} Σ_{l∈E_n} u_l √(1+|m−l|) e^{−D|m−l|}, D ≥ log 4 (`library/layered-a3.md` (1)). Its first missing piece is the uniform real target-datum admission and complex bound (8) of layered-a3 for the actual layered stage family."

ST1 r2 L143: "**IN1 requires its precision constants (a, H, μ₀), and the uniform background/tower bounds feeding them, to be fixed before κ, independently of M, κ̄.** ... Neither E_κ̄ nor C(M) may be absorbed into those constants."

`os-draft.md` L160, item (F-4): "PR1(1) at layered pairs (PR-lay, `in1-draft.md:62`, open). **Its final statement must take the same form.**" The form is that of L153–157: a theorem stated for every sequence of 𝒮_sep(ρ₀, M₁) with ρ₀ above a floor, with constants not depending on the particular sequence.

### 1.4 The strongest common form

Both consumers read (I-1)(a)–(d) at the input pair of the main step and at its real reference. IN1 allows an M-dependent prefactor in (d); NL1 inherits IN1's form. OS asks for a floor-type statement over separated sequences. ST1 asks that no constant fed to IN1 depend on M, κ̄. So the strongest form both need, and the form proved here, is:

> **(PR-lay)** For every separated sequence 𝐒 ∈ 𝒮_sep(ρ, M₁) with ρ above a floor fixed with L, for every complex regular pair P of 𝐒 with radii below a ceiling fixed with L, (a)–(d) hold with (a, b, H, μ₀) and η(P) ≤ H₁κ(P), all constants functions of L only. Moreover every pair at which IN1 or NL1 evaluates 𝖠, and its real reference, is such a pair once γ is below a ceiling that may depend on M and κ̄.

This is stronger than IN1 asks in two ways. The prefactor H₁ is independent of M. And (d) is linear in the size of the complex part alone: the real factor is common to P and to its reference, so its size does not enter η.

---

## 2. Source findings

### 2.1 SA (1c): separated sequences and regular pairs

SA L10113–10118: "We work in level-k units, in which 𝕋^{(j)} has spacing ξ_j := L^{j−k}; moreover η = η_k = ξ₀. A sequence Ω₀ ⊃ ⋯ ⊃ Ω_k is called *separated* when every Ω_j is a union of M₁-cubes at level j and dist_∞(Ω_j^c, Ω_{j+1}) > R₁M₁ξ_j." SA L10119: "No further condition is placed on the regions. In particular Ω₀ is arbitrary, and Dirichlet conditions are imposed outside it." SA L10120–10127 define layers ℒ_j = closure(Ω_j ∖ Ω_{j+1}), tops, rows (interior and outward, inward bonds carry no row) and the distance d_𝐁, which "measures each layer in the unit of that layer" (L10127).

SA L10129–10137 define the class: "*Regular pairs* (𝐔, 𝐉) consist of 𝐔 = e^{iηA′}U, with U real, together with an **independent** 𝔤^c-valued 1-form 𝐉 ... Such a pair is required to satisfy, on ℒ_j, |∂U − 𝟏|, |∂𝐔 − 𝟏| < α₀η²ξ_j^{−2}, ξ_j|A′|, ξ_j²|∇_U A′| < α₁, |𝐉| < γ₀ξ_j^{−3}, and, on every cube of side O(M₁ξ_j) contained in ℒ_j ∪ ℒ_{j+1}, to admit a real gauge U = e^{iηA} with ξ_j|A|, ξ_j²|∇A| ≤ α₀. In this condition the bound is α₀ on the entire cube, and not O(M₁)α₀." These conditions are in the local scale of each layer of the nest. SA L9797 stresses: "The regular pairs form a class defined by inequalities (curvature, gauges on cubes, complex part, independent current) that do not mention any critical point."

SA L10307 (statement 4) states: "The ceiling on the radii α₀, α₁, γ₀ is fixed before M₁ and is **independent of M₁**. At every regular pair all the inverses exist, they are holomorphic in (𝐔, 𝐉), and they are real at real pairs." This is SA's statement [SS]; the library proofs are a2-layers and h-walk (§2.8).

### 2.2 SA: the fibre precision reads the pair, not a tower

SA L10200: "For step k+1 we work on the bonds of 𝕋^{(k)} that touch Ω_{k+1}, with V = M^k𝐔. Let 𝖢_V be the elimination of the pivot bonds, and let 𝖦^{(2)}_V be the quadratic part of the soft axial gauge fixing. Let 𝖤^{(2)} be the quadratic part of the one-step constraint". SA L10203: Δ_k = (Q𝖦₁Q^𝖳)^{−1} − a − 𝖤^{(2)}[𝖧₁^𝖳𝐉]. SA L14091–14107 repeat this at the consumer: "Let P = (𝐔, 𝐉) be a regular complex pair. ... put V = M^k𝐔 and Δ_k(P) = (Q𝖦₁Q^𝖳)^{−1} − a − 𝖤^{(2)}[𝖧₁^𝖳𝐉], 𝖠(P) = 𝖢_V^𝖳(GF^{(2)}_V + Δ_k(P))𝖢_V."

So 𝖠(P) is built from the six propagators of SA L10142–10158 at the pair, the many-scale rows Q at 𝐔, and finite local maps of V = M^k𝐔 near Ω_{k+1}. **None of these reads a tower configuration T_e or a datum tube 𝒯_e.** The towers enter only the hereditary core of the activities (SA (R5)–(R6), L5696–5715). This is the basis of §7.

SA L10155: "The operators are defined in this order: 𝖦, then 𝖧 from 𝖦, then 𝖦₁, then 𝖧₁ from 𝖦₁. ... (A, Δ^{(2)}[𝗃]A) = 2(C^{(2)}(A), 𝗃)." The symbol ^𝖳 is "the transpose with respect to bilinear pairings, so that everything remains holomorphic" (SA L10139, the Operators paragraph).

### 2.3 SA: the gap and kernel statement at the consumer

SA L14122–14152 sketch the gap: "The comparison starts with the flat bound 𝖠(𝟏, 0) ≥ γ₀ > 0 ... On each cube of side O(ℓ₀) the real factor has a real gauge in which its potential and first difference are bounded by a_w. The core supplies this gauge with a_w = CLMa₀ ... Re 𝖠(P) ≥ γ₀ − Cℓ₀^{−2} − Ce^{−cℓ₀} − C(a_w + a₀ + a₁) ≥ ½γ₀. Choose ℓ₀, then a_w, then M ≥ Cℓ₀, then the radii with CLMa₀ ≤ a_w. Every compression inherits this gap. The same exponential kernel bounds, by conjugation, give uniform decay of the compressed shifted resolvents." This is a sketch [SS]. It is the source of IN1's H_p(M): SA's comparison at L14186–14191 is ‖C − C₀‖ + ‖Γ − Γ₀‖ ≤ C(e^{−cM} + LMa₀ + a₁).

### 2.4 SA: the complex route on separated layers

SA L10828–10937 give SA's own complex argument on a separated nest. L10857–10860, (PX57): the input is "h = max{‖ξE‖_∞, ‖ξ²∇_U E‖_∞} ≤ h_L", the local-scale size of the complex variation. L10863–10865: "Choose a fixed h_L > 0 so that the same argument holds with E replaced by sE for |s| < h_L/h ... The transport is holomorphic in s on this disc, with a uniform bound. Cauchy's formula on a smaller concentric disc ... yields (PX58) |𝖳_j(e^{iηE}U; y, x) − 𝖳_j(U; y, x)| ≤ C_L h." L10867: "This is a single directional Cauchy argument on an actual admitted physical disc." L10873: at an outward row "its neighborhood uses one adjacent scale, so the input constants change by fixed powers of L." L10875–10898 ((PX60)–(PX62)) give the complex site inverse by relative forms; L10900–10937 ((PX63)–(PX68)) give decay by conjugation with e^{sψ}. My Proposition A.6 is the same directional Cauchy device, applied to 𝖠 itself on the disc that the class admits.

### 2.5 SA: the geometry of the operation R, stage tests and lifts

SA L17398–17407 (Proposition 2.3) state: "Each operation R has stage sequences and prepared sequences ... on which the backgrounds of (2b), (2d) are formed, and drop-outs keep nests. In these sequences and nests the boxes are only unions of M-cubes, and the only lower bound on the gaps is one M-cube of the later level: dist_∞(Z_j, Ω_{j+1}) ≥ LM ... Consequently the estimates of (1b), (1c) must hold with a separation of only one M-cube." [SS]

SA L17624 states the stage tests in the units of the current shell: "After n stages the test requires |∂U^{(n)}_{k,X} − 𝟏| < (1 − β_s(1 − 2^{−(j−i+1)}))ε_iη_i² on that shell. On the outermost shells, where the collars of the stages overlap, this requirement is relaxed by a factor L_♭² for each overlap ... it becomes larger with each successive shell until it reaches Ř_k^c. In the region not covered by the shells, the bound is expressed in the scale j of the stage and equals (1 − ½β_s)c_l L_♭^{2e}ε_jη_j² ... On a layer l < j this bound remains below ε_lη_l², the scale of that layer." [SS]

SA L6141–6152 state the layer radii: "The layer-radius formation data give the original regularity layer and the layer after each stage. Their nonnegative difference is e_σ(x). The lift is L_♭^{2e_σ(x)} for a fixed L_♭ ≥ 1. The layer-m radii are multiplied by this lift and, except for the real-potential gauge bounds, by (R22). ... The space Ũ^c_σ(X) imposes the simple, tower and small-field-core clauses with those layer radii, with one splitting, on every subdomain and every preceding structure." SA L6033 gives the running radii α_{ι,j} = C_ιθ_j^{−1/2}(log θ_j)^q (NL1-L L80, L130 adopt this table).

### 2.6 CA-I

CA-I L46035–46082 (Theorem 4.14, "The operator theorem at free current") is an implication on a class: its hypotheses are the nest conditions (A1)–(A2), floors on M₁, M₁^♯, M, L and ceilings; its conclusion (B) gives, "At every point (U, 0) with U ∈ 𝒰_ℝ, 𝖰 is real symmetric with γ₀/2 ≤ 𝖰 ≤ γ₁ ... On 𝒰(ε₁), Re 𝖰 ≥ γ₀/4", and (A) gives that "𝖰, 𝖠, 𝖢 are complex symmetric". CA-I L45439–45515 define the class 𝒰_ℝ by three gauge clauses on cubes, and L45511–45515 add: "At the levels weighted by an R-operation, the constant α₀ of (u1) and the radii in (4.14:eq-real-backgrounds-b) carry Balaban's factor 𝖫₀^{2e_n} ... this factor satisfies 𝖫₀^{2e_n} ≤ 𝖼₁R_n." CA-I L49495–49502 (Remark 4.14, "Scope of the second gauge clause's supply"): the inclusion of the expansion's real background into these spaces, and the spaces at later steps on drop-out nests, "are conditions that the application has to meet ... and lie outside the implication asserted by" the operator theorem. So CA-I has the same split as this file: an operator theorem on a class (Part A), and admission into the class (Part B), the latter left to the application.

### 2.7 Y3

Y3 has no operation R (`os-draft.md` L72: `grep -c -i 'drop-out\|dropout'` returns 0). Y3 L53314–53321 apply the background theorems on every meet of a stage sequence with a tower: "This sequence is separated and subordinate: the complement of an intersection is the union of the two complements, so its gap is at least the smaller of the two original gaps." The three-dimensional template is thus: every sequence in force is separated, and the separated-sequence theorems apply to it. I follow it.

### 2.8 The library

- `p82.md` (frozen; gate `p82-gate.md`): Theorem P is already a layered theorem. Its geometry (p82 L9–21) is a separated sequence with layers ℒ_j; its hypothesis Reg_α (p82 L132–136) is a real gauge bound on every cube of side c_reg M_Pξ_j in ℒ_j ∪ ℒ_{j+1}; it needs no critical point. Its operator is the constrained inverse S_q° of the A3 response, not the fibre precision 𝖠. So P82 is not on the path of (I-1); it is on the path of PR1(2) (A3). §7.4 says what a P82-based route to Part A would add.
- `a2-layers.md` Theorem A (a2-layers L76–86): for every separated sequence of depth k+1 and every real regular pair (U, J), on shell or not, all inverses in 𝖠 exist and ⟨u, 𝖠u⟩ ≥ c_L‖u‖² on the free coordinates (counting norm, ξ_k = 1), also on every conditioning set; c_L and the ceiling a_* depend on L only. The gate (`gate a2-layers` L110–118) keeps it as "a useful **conditional** theorem for the unweighted operator specified in (1c), on the default separated sequences with inward rows omitted, arbitrary seams/contacts, independent small currents" after "the explicit cap/separation" repairs. a2-layers L73: "U is taken in a gauge in which V is block axial on Ω_{k+1}; gauge covariance of all operators makes this a normalization".
- `a2-full.md` Theorem II (a2-full L111) and Lemma 5.1: the gauge-gradient term −𝖢_V^𝖳𝖤_V^{(2)}[Ĵ_GF(V_c)]𝖢_V is bounded by C_II α₁ in norm, with finite stencils; gate `a2-full` L68: "first failing step none after that convention correction".
- `h-walk.md` Theorem H (h-walk L374–388): "at every regular pair P for (Ω_j)_{j≤k+1} with radii below a_h, real or complex, with independent current": (H1) 𝖠 = Σ_ω 𝖠_ω over tree walks, absolutely convergent, (H2) |𝖠_ω(b, b′)| ≤ C_h(C_hM₁^{−1/3})^{|ω|}e^{−δ_h d_𝐁(ω;b,b′)}, (H3) 𝖠_ω holomorphic on the local class and real at real pairs. The gate (`gate h-walk` L126–145, L204) rejects the region-trace canonicity and the single-term isometry clauses, and keeps: "Kernel decay, left support and fixed-region field-carrier bounds advance conditionally", with the count repaired to C_h^{m+1} and the support reading "A_ω(b, b′) = 0 when dist_𝐁(b, X_root) > C_L"; "Field holomorphy for fixed regions is a distinct, surviving assertion".
- `os-draft.md` Lemma 2.3 (os-draft L90–108) and Corollary 2.4 (L110–112): every stage sequence, ν-sequence, meet with a separated tower, and the old/new pair of a stage is separated by one M-cube of the later level; Theorem 3.1 (L129–137) reduces OS to the separated theorems under (M-sep): M₁ | M and LM ≥ R₁M₁.
- `st1-r2.md` Lemma 10 (st1-r2 L598–640): under the stage tests, the actual regular critical background at a structure satisfies (59), l²η^{−2}|∂U − I|, l³|J°_η(U)| ≤ C_RAλ(x)ε_{m(x)}, with λ(x) ≤ C_λ(log θ_{m(x)})^{2r_R} by (57). `st1-draft3.md` Lemma B1 (ST3 L210) gives (59) for the output background with the same C_RA, for γ ≤ γ_B(M).
- `layered-a3.md`: (3) is the algebraic seam loss; §3 (layered-a3 L138–141) locates it: "At the **same point**, an unlocalised target tower can assign scale ξ_q where the ambient nest assigns ξ_{h_q}"; (44) shows a Ř-level loss cannot be paid by the coupling ceiling; Lemma RC (51) is a real-curvature bound on inherited carriers measured in the target tower's scale ξ_e. All of these concern tower data.
- `a3-close.md` L99 leaves "the layered case (domains meeting seams; layered radii of SA 6(d), second case), for references not covered by Lemma R" open. Lemma R is admission of the real critical background into the hereditary core, including its tower clauses (a3-close L71–80). Again towers.

---

## 3. Definitions

### 3.1 Lattice, units and norms

Work on a finite periodic four-dimensional lattice, L odd, in level-k units: ξ_j = L^{j−k}, η = ξ₀ (SA L10113). G = SU(2). Real configurations take values in SU(2), complex ones in SL(2, ℂ). Lie-algebra values are traceless 2×2 matrices; the real colour space is the traceless Hermitian matrices with pairing ½Tr(XY). All matrix norms are operator norms. Ad(V)X = VXV^{−1}; for unitary V, |Ad(V)X| = |X|. Reversed bonds carry inverted links. For a complex potential B on bonds, the reversed bond carries B(b̄) = −Ad(U(b)^{−1})B(b), so that (e^{iηB}U)(b̄) = e^{iηB(b̄)}U(b̄). The covariant difference is (∇^U_νB)_μ(x) = η^{−1}[Ad(U_ν(x))B_μ(x + ηe_ν) − B_μ(x)] (st1-r2 (1)); |∇_UB| is the maximum of its components.

For a complex B write B = B_R + iB_I with B_R = (B + B^*)/2 and B_I = (B − B^*)/(2i). Both are Hermitian and |B_R|, |B_I| ≤ |B|. Since Ad(U) commutes with X ↦ X^* for unitary U, (∇_UB)_R = ∇_U(B_R) and likewise for B_I (`a3-close.md` Lemma T step 2).

### 3.2 Separated sequences

**Definition 3.1.** For powers M₁, R₁ of L with R₁ ≥ L, put ρ = R₁M₁. 𝒮_sep(ρ, M₁) is the set of sequences 𝐒 = (Ω_j)_{0≤j≤k+1}, Ω_{k+1} possibly empty, such that each Ω_j is a union of aligned level-j cubes of side M₁ξ_j and dist_∞(Ω_j^c, Ω_{j+1}) > ρξ_j for 0 ≤ j ≤ k (SA L10113–10118). Layers, tops, rows and pillars are those of SA L10120–10125, with inward bonds omitted. The local scale l(x) of a site is the scale of its pillar; a bond or plaquette has the largest corner scale (p82 L13). The fluctuation coordinates of the step are the free (non-pivot) coordinates of the level-k bonds of 𝕋^{(k)} that touch Ω_{k+1} (SA L10200). A coordinate has a base site and a colour index.

The floor property (`os-draft.md` L153–157) is automatic for this definition: if ρ′ ≥ ρ then 𝒮_sep(ρ′, M₁) ⊂ 𝒮_sep(ρ, M₁).

### 3.3 Regular pairs and their radii

**Definition 3.2 (SA L10129–10137).** Let 𝐒 ∈ 𝒮_sep(ρ, M₁) and α₀, α₁, γ₀ > 0. ℛ(𝐒; α₀, α₁, γ₀) is the set of triples P = (U, A′, 𝐉), U real on the bonds of Ω₀, A′ and 𝐉 complex Lie-algebra valued 1-forms, with 𝐔 = e^{iηA′}U, such that on each layer ℒ_j:

- (R-c) |∂U(p) − 𝟏| < α₀η²ξ_j^{−2} and |∂𝐔(p) − 𝟏| < α₀η²ξ_j^{−2} at every plaquette p of Ω₀ in ℒ_j;
- (R-a) ξ_j|A′(b)| < α₁ and ξ_j²|∇_UA′(b)| < α₁ at every bond b of Ω₀ in ℒ_j;
- (R-j) |𝐉(b)| < γ₀ξ_j^{−3} at every bond b in ℒ_j;
- (R-g) every cube Z of side at most c_gM₁ξ_j contained in Ω₀ ∩ (ℒ_j ∪ ℒ_{j+1}) carries a real gauge U = e^{iηA} on Z with ξ_j|A| ≤ α₀ and ξ_j²|∇A| ≤ α₀ there.

Here c_g is the class constant of `a2-layers.md` §1 (fixed with L). The pair is *real* if A′ = 0 and 𝐉 is real. The real reference of P is (U, 0, 0), written (U, 0).

A bond or plaquette lying on two layers (at a seam) satisfies the conditions of both; since ξ_j < ξ_{j+1}, the binding one is that of the coarser layer for (R-a), (R-j) and that of the finer layer is weaker. Nothing below depends on which reading is taken, provided it is the same for P and for every member of the families of §5.

**Definition 3.3 (radii of a pair).** For a triple P = (U, A′, 𝐉) on 𝐒:

- α₀^{re}(U) is the least α ≥ 0 such that U satisfies the real half of (R-c) and (R-g) with every strict bound < α replaced by ≤ α; then (R-c), (R-g) hold for every α₀ > α₀^{re}(U).
- κ(P) := max{sup_b l(b)|A′(b)|, sup_b l(b)²|∇_UA′(b)|, sup_b l(b)³|𝐉(b)|}, the local-scale size of the complex part. Here l(b) is the scale of the layer whose condition is read at b (Definition 3.2).

Then P ∈ ℛ(𝐒; α₀, α₁, γ₀) as soon as α₀^{re}(U) < α₀, κ(P) < min{α₁, γ₀}, and the complex half of (R-c) holds; Lemma A.4 gives the latter from the first two.

### 3.4 The fibre precision

**Definition 3.4.** At a pair P ∈ ℛ where all inverses exist, 𝖠(P) := 𝖢_V^𝖳(𝖦_V^{(2)} + Δ_k(P))𝖢_V with Δ_k(P) = (Q𝖦₁Q^𝖳)^{−1} − a − 𝖤^{(2)}[𝖧₁^𝖳𝐉], V = M^k𝐔, exactly as SA L10142–10208 and L14091–14107. It acts on the fluctuation coordinates. Kernels are in counting measure (ξ_k = 1). The real factor is taken in the step's gauge, in which M^kU is block axial on Ω_{k+1} (a2-layers L73; SA PX104). 𝖠^full(P) := 𝖠(P) − 𝖢_V^𝖳𝖤_V^{(2)}[Ĵ_GF(V_c)]𝖢_V is the actual next-fibre operator of `a2-full.md` Theorem II.

IN1 cites 𝖠 (IN1 L57: "the gauge-fixed fibre precision 𝖠(P) of SA L14097–14107"). Theorem A covers both 𝖠 and 𝖠^full (Corollary A.8).

### 3.5 Distances

d_𝐁 is SA's layer distance (SA L10121–10127), taken on the torus. d(x, y) is the periodic ℓ¹-distance of base sites in level-k units (IN1 §A.1). For μ > 0, V(μ) := sup_x Σ_y e^{−μ d(x,y)}, the sum over fluctuation coordinates y.

---

## 4. Imports

Each import is a statement proved, or stated, elsewhere. I give the exact form used and its status there.

**(I-A) Real gap on separated layers.** [I: `a2-layers.md` Theorem A, ungated in its own text; gate `a2-layers-gate.md` keeps it as a conditional theorem after the cap and separation repairs; it rests on `a2-curved.md` §§5, 8 (gate `a2-curved-gate.md`) and on the gated flat inputs of `c0-loc.md`.] There are L₀, c_L > 0, a_*(L) > 0, M_*(L), ρ_*(L) such that for odd L ≥ L₀, M₁ ≥ M_*, ρ ≥ ρ_*, every 𝐒 ∈ 𝒮_sep(ρ, M₁) and every real regular pair (U, J) of 𝐒 with radii ≤ a_* (on shell or not): all inverses in 𝖠 exist and ⟨u, 𝖠(U, J)u⟩ ≥ c_L‖u‖² on the fluctuation coordinates; at J = 0, 𝖠(U, 0) is real symmetric (a2-layers L673: "A(U, 0) is real symmetric and >= c_L by Theorem A"). Used only at J = 0.

**(I-B) The gauge-gradient term.** [I: `a2-full.md` Lemma 4.1 and Theorem II; gate `a2-full-gate.md` L68, "first failing step none after that convention correction".] On the class with α₁ below a ceiling of L, the matrix 𝖤_free := 𝖢_V^𝖳𝖤_V^{(2)}[Ĵ_GF(V_c)]𝖢_V has range at most r_II(L) in d and entries of norm at most C_II(L)κ(P); it vanishes when V_c(y, x) = 1.

**(I-C) The walk expansion on the class.** [I: `h-walk.md` Theorem H, in the form kept by `gate h-walk` §8: kernel decay, left support and fixed-region field holomorphy "advance conditionally" on (I1)–(I3) of h-walk; the canonicity and isometry clauses are *not* used.] There are a_h(L) > 0, C_h(L), δ_h(L) > 0, N_r(L), C_L′(L) and M_h(L) such that, for R₁ ≥ 64L, M₁ ≥ M_h, every 𝐒 ∈ 𝒮_sep(ρ, M₁) and every P ∈ ℛ(𝐒; α₀, α₁, γ₀) with α₀, α₁, γ₀ < a_h, real or complex:

- (H0) all inverses in the definition of 𝖠(P) exist (h-walk's input (I1) is the conjugation package of `a2-layers.md` §7, whose Theorem B states "all inverses exist" on the complex neighbourhood with ceiling a_B ≥ a_h, a2-layers L665–671);
- (H1) 𝖠(P) = Σ_ω 𝖠_ω(P), the sum over tree walks ω, absolutely convergent; for each cell there are at most C_h^{m+1} walks of length m with that root cell;
- (H2) |𝖠_ω(P)(b, b′)| ≤ C_h(C_hM₁^{−1/3})^{|ω|}e^{−δ_h d_𝐁(ω; b, b′)}, where d_𝐁(ω; b, b′) ≥ d_𝐁(b, b′) is the least length of a tree through b, b′ meeting the non-root cells; and 𝖠_ω(b, b′) = 0 unless dist_𝐁(b, X_root(ω)) ≤ C_L′; at most N_r root cells lie within dist_𝐁 ≤ C_L′ of a given b;
- (H3) each 𝖠_ω is a fixed function, holomorphic in the complex variables (A′, 𝐉) at fixed U on the class, and real at real pairs.

h-walk L376 defines a_h := min{a_*, a_T, γ_j/C₀, a_B}. From `a2-layers.md` Theorem B the present file uses only the existence statement (H0); it does not use Theorem B's gap, and it re-derives the complex gap (Theorem A(b)) from the real gap and (d).

**(I-D) Separation of every sequence in force.** [I: SA Proposition 2.3, L17398–17407 [SS]; `os-draft.md` Lemma 2.3 and Corollary 2.4 [P there, Claude pass 1, not checked], for stage sequences, ν-sequences, tower meets and the old/new pair of a stage; label sequences: SA L17398, gaps ≥ cMŘ_j in level-j units.] Every determining sequence in force at a structure of a finite history (label, stage, ν-, prepared and output sequence, and their meets with separated towers) has members that are unions of level-j M-cubes or level-j cells, and gaps dist_∞(Ω_{j+1}, Ω_j^c) ≥ LMξ_j.

**(I-E) The real background in the units of the nest in force.** [I: `st1-r2.md` Lemma 10, (57)–(59), at main steps and stages (Codex pass 2, not refereed), from PROF, AV/CURV, A1/F0/REG, RUN and the stage tests of SA L17624; `st1-draft3.md` Lemma B1 at outputs (Claude round 3, not distilled), for γ ≤ γ_B(M).] At every structure σ the actual regular critical background U satisfies, at every complete element e of Ω₀^σ, l(e)²η^{−2}|∂U(e) − I| ≤ C_RAλ(e)ε_{m(e)} and l(e)³|J°_η(U)(e)| ≤ C_RAλ(e)ε_{m(e)}, with l and m the scale and level of the nest in force, C_RA = 2C_PC_te = 12C_PC_smL⁴, and λ(e) ≤ C_λ(log θ_{m(e)})^{2r_R}.

**(I-F) The local gauge RCG4.** [I: `st1-r2.md` §2, L117, packaging `a1-balaban.md` §3.8 (Balaban CMP 99 (1985) 75–102, Proposition 6), gated in `a1-balaban-gate.md` conditional on F0.] In level-i units: on a cube of side s, if on its side-(s+6) enlargement the curvature is < wL²η_i², the matrix divergence |D_U^𝖳∂U| is < 2L³wη_i², and (s+2)L³w < c_rg, then the cube carries a real gauge with |A|, |∇A| < 4L³B_*(s+2)w. Here c_rg, B_* depend on L only.

**(I-G) Current-layer radii of the consumer domain.** [I: design. Source: SA L6141–6152 ("The layer-m radii are multiplied by this lift ... imposes the simple ... clauses with those layer radii ... on every subdomain and every preceding structure"); ST1's simple radii c_σ(x|m)λ_τ(x)α_ιε_mL^{−pm} (st1-r2 L92); the formation of records at every structure, including on the raised set "On the set raised to level j+1 set the raw exponent ℰ = e_j + 1" (st1-r2 L607) and at outputs (ST3 Lemma B1); the radius table (Tq) of NL1-L L130.] At every main-step input structure σ, every input pair P′ = (U, A′, 𝐉′) of the consumer's domain satisfies, on every bond b of Ω₀^σ, with m = m_σ(b) the level of b in the nest in force,

  l(b)|A′(b)|, l(b)²|∇_UA′(b)| < (1 + β_s)λ_σ(b) r₁(m),  l(b)³|𝐉′(b)| < (1 + β_s)λ_σ(b) r₀(m),

with λ_σ(b) ≤ C_λ(log θ_m)^{2r_R} and r_ι(m) = C_ιθ_m^{−1/2}(log θ_m)^q. The factor 1 + β_s bounds the coefficient (R22) (SA L6148: "The data must ensure c ≤ c_σ ≤ 1 + β_s"). §6.3 discusses this import: it is satisfied by SA's design, and it is needed by the consumer for 𝖠(P′) to be defined at all.

---

## 5. Part A: the operator theorem at complex regular pairs

Throughout Part A fix L ≥ L₀, R₁ ≥ 64L, M₁ ≥ max{M_*, M_h, 8C_h⁶}, ρ = R₁M₁ ≥ ρ_*, and 𝐒 ∈ 𝒮_sep(ρ, M₁). Decrease a_h if needed so that a_h ≤ min{a_*, 1/2}. All constants of Part A are functions of L only; M₁ and R₁ enter only through these lower bounds.

**Lemma A.1 (metric comparison and ball bound).** [P] (i) For fluctuation coordinates x, y, d_𝐁(x, y) ≥ ¼ d(x, y). (ii) For μ > 0, V(μ) ≤ 12((1 + e^{−μ})/(1 − e^{−μ}))⁴ =: V₀(μ).

*Proof.* (i) In level-k units every layer has scale ξ_j ≤ ξ_k = 1, so the metric density 1/ξ_j of d_𝐁 is ≥ 1 on every layer; outside Ω₁ it is 1/η ≥ 1 (SA L10125–10127). Hence the d_𝐁-length of a connected path on the torus is at least its sup-norm arclength (SA uses ds_∞ in (PX1), L10604–10607; a Euclidean or coordinate length is larger). The sup-norm arclength of a path is at least the periodic ℓ^∞-distance of its endpoints, which is at least ¼ of their periodic ℓ¹-distance in four dimensions. Take the infimum over paths. (ii) A coordinate is a bond direction (4) and a colour index (3) at a base site of the level-k lattice. Each torus site has a preimage in ℤ⁴ at the same periodic ℓ¹-distance from a fixed preimage of x, so Σ_y e^{−μd(x,y)} ≤ 12 Σ_{z∈ℤ⁴} e^{−μ|z|₁} = 12(Σ_{n∈ℤ}e^{−μ|n|})⁴, and Σ_{n∈ℤ}e^{−μ|n|} = (1 + e^{−μ})/(1 − e^{−μ}). ∎

**Lemma A.2 (entry bound on the class).** [P from (I-C)] Put μ₀ := δ_h/4 and H := 2N_rC_h². For every P ∈ ℛ(𝐒; α₀, α₁, γ₀) with α₀, α₁, γ₀ < a_h, real or complex, and all fluctuation coordinates x, y,

  Σ_ω |𝖠_ω(P)(x, y)| ≤ H e^{−δ_h d_𝐁(x,y)} ≤ H e^{−μ₀ d(x,y)}.

In particular |𝖠(P)(x, y)| ≤ H e^{−μ₀d(x,y)}, and ‖𝖠(P)‖ ≤ b := H V₀(μ₀).

*Proof.* By (H2), 𝖠_ω(x, y) ≠ 0 only if the root cell of ω lies within dist_𝐁 ≤ C_L′ of x; there are at most N_r such cells. For a fixed root cell there are at most C_h^{m+1} walks of length m (H1). Each term is at most C_h(C_hM₁^{−1/3})^m e^{−δ_hd_𝐁(ω;x,y)} ≤ C_h(C_hM₁^{−1/3})^m e^{−δ_hd_𝐁(x,y)}, since a tree through x and y contains a path from x to y. So the sum is at most N_r Σ_{m≥0} C_h^{m+1}·C_h(C_hM₁^{−1/3})^m e^{−δ_hd_𝐁(x,y)} = N_rC_h² Σ_m (C_h²M₁^{−1/3})^m e^{−δ_hd_𝐁(x,y)}. M₁ ≥ 8C_h⁶ gives C_h²M₁^{−1/3} ≤ ½, and the geometric sum is ≤ 2. The second inequality is Lemma A.1(i). The norm bound is the Schur test for block matrices: ‖K‖ ≤ (sup_x Σ_y‖K(x,y)‖)^{1/2}(sup_y Σ_x‖K(x,y)‖)^{1/2} ≤ H V(μ₀), with Lemma A.1(ii). ∎

**Lemma A.3 (holomorphy along complex families).** [P from (I-C)] Let D ⊂ ℂ^n be open and z ↦ P_z = (U, A′_z, 𝐉_z) a family with fixed real U, with A′_z and 𝐉_z holomorphic in z, and P_z ∈ ℛ(𝐒; α₀(z), α₁(z), γ₀(z)) with all three radii < a_h for every z ∈ D. Then each entry z ↦ 𝖠(P_z)(x, y) is holomorphic on D.

*Proof.* Each z ↦ 𝖠_ω(P_z)(x, y) is holomorphic on D: by (H3) 𝖠_ω is holomorphic in (A′, 𝐉) at fixed U on the class (and on its local class, which contains the class), and z ↦ (A′_z, 𝐉_z) is holomorphic. By Lemma A.2 the series Σ_ω 𝖠_ω(P_z)(x, y) is dominated, uniformly in z ∈ D, by the convergent numerical series of its proof. A uniformly convergent series of holomorphic functions is holomorphic (Weierstrass), separately in each variable and hence jointly by Hartogs' or Osgood's lemma for continuous separately holomorphic functions; continuity holds by uniform convergence. By (H1) its sum is 𝖠(P_z)(x, y). ∎

For the Lean reading it suffices to use one complex variable at a time: every use below restricts to a disc in one variable, with the others fixed.

**Lemma A.4 (curvature of a complex perturbation).** [P] Let U be real, B a complex Lie-algebra valued 1-form, 𝐔 = e^{iηB}U, and p a plaquette in ℒ_j with local scale ξ := ξ_j. Put α := max{ξ|B|, ξ²|∇_UB|} on the bonds of p and α₀^{re} := η^{−2}ξ²|∂U(p) − 𝟏|. If α ≤ 1/16 and α₀^{re} ≤ 1/4, then

  η^{−2}ξ²|∂𝐔(p) − 𝟏| ≤ α₀^{re} + 4α.

*Proof.* Let p = p_{μν}(x), with bonds b₁ = (x, x+ηe_μ), b₂ = (x+ηe_μ, x+ηe_μ+ηe_ν), b₃ the reverse of (x+ηe_ν, x+ηe_μ+ηe_ν), b₄ the reverse of (x, x+ηe_ν). Write U_r = U(b_r) and B̃_r = B(b_r) with the reversal convention of §3.1. Then 𝐔(b_r) = e^{iηB̃_r}U_r. Moving the links to the right, using U e^{X}U^{−1} = e^{Ad(U)X},

  ∂𝐔(p) = e^{iηY₁}e^{iηY₂}e^{iηY₃}e^{iηY₄} ∂U(p),  Y_r := Ad(U₁⋯U_{r−1})B̃_r.

(1) *The linear term.* With W := U_μ(x)U_ν(x+ηe_μ)U_μ(x+ηe_ν)^{−1} = ∂U(p)U_ν(x) one finds Y₁ = B_μ(x), Y₂ = Ad(U_μ(x))B_ν(x+ηe_μ), Y₃ = −Ad(W)B_μ(x+ηe_ν) = −Ad(∂U(p))Ad(U_ν(x))B_μ(x+ηe_ν), Y₄ = −Ad(∂U(p))B_ν(x). Hence

  Σ_r Y_r = [Ad(U_μ(x))B_ν(x+ηe_μ) − B_ν(x)] − [Ad(U_ν(x))B_μ(x+ηe_ν) − B_μ(x)] + (1 − Ad ∂U(p))[Ad(U_ν(x))B_μ(x+ηe_ν) + B_ν(x)]
     = η(∇_μB_ν − ∇_νB_μ)(x) + (1 − Ad ∂U(p))[Ad(U_ν(x))B_μ(x+ηe_ν) + B_ν(x)].

This is the identity of SA PX115/PX117 re-derived in `gate p82` F3. For unitary V and any X, X − VXV^{−1} = [X, V − 𝟏]V^{−1}, so |(1 − Ad V)X| ≤ 2|V − 𝟏||X|. Therefore |Σ_rY_r| ≤ 2η|∇_UB| + 4|∂U(p) − 𝟏| max_r|B̃_r|.

(2) *The remainder.* For matrices X₁, …, X₄ put s = Σ|X_r|. Expanding each exponential in its power series, e^{X₁}⋯e^{X₄} = Σ_{n₁,…,n₄≥0} Π_r X_r^{n_r}/n_r!, absolutely convergent. The terms of total degree 0 and 1 are 𝟏 and ΣX_r. The others are bounded termwise by Π|X_r|^{n_r}/n_r!, whose sum over total degree ≥ 2 is e^s − 1 − s. So |e^{X₁}⋯e^{X₄} − 𝟏 − ΣX_r| ≤ e^s − 1 − s ≤ (e − 2)s² ≤ s² for 0 ≤ s ≤ 1. Apply this with X_r = iηY_r, s ≤ 4η max|B̃_r| ≤ 4(η/ξ)α ≤ 4α ≤ ¼.

(3) *Assembly.* ∂U(p) is unitary, so |∂𝐔(p) − ∂U(p)| = |e^{iηY₁}⋯e^{iηY₄} − 𝟏| ≤ η|ΣY_r| + s² ≤ 2η²|∇_UB| + 4η|∂U(p) − 𝟏||B| + 16η²|B|². Multiply by η^{−2}ξ²:

  η^{−2}ξ²|∂𝐔(p) − ∂U(p)| ≤ 2ξ²|∇_UB| + 4(η^{−2}ξ²|∂U(p) − 𝟏|)(η/ξ)(ξ|B|) + 16(ξ|B|)² ≤ 2α + 4α₀^{re}α + 16α².

With α₀^{re} ≤ ¼ and α ≤ 1/16 the right side is ≤ 2α + α + α = 4α. The triangle inequality gives the claim. At a seam plaquette, apply the same computation with ξ the scale of the layer whose condition is read; the bonds of p in a coarser layer satisfy the finer bound a fortiori. ∎

**Lemma A.5 (the scaled family stays in the class).** [P] Let P = (U, A′, 𝐉) be a triple on 𝐒 with α₀^{re}(U) < a_h/2 and κ := κ(P) > 0. Put R := a_h/(8κ). For z ∈ ℂ with |z| < R define P_z := (U, zA′, z𝐉). Then P_z satisfies all conditions of Definition 3.2 with α₀ = α₀^{re}(U) + 4|z|κ and α₁ = γ₀ = a_h/8; all three are strictly below a_h. So P_z ∈ ℛ(𝐒; a_h, a_h, a_h) with room. Similarly, for (z, w) ∈ ℂ² with |z| + |w| < R, the triple P_{z,w} := (U, zA′_R + wA′_I, z𝐉_R + w𝐉_I) has all radii below a_h.

*Proof.* (R-a), (R-j) for P_z: l(b)|zA′(b)| = |z|l(b)|A′(b)| ≤ |z|κ < a_h/8, and the same for ∇_U(zA′) = z∇_UA′ and for z𝐉. (R-g) and the real half of (R-c) concern U only and hold with α₀^{re}(U) < a_h/2. The complex half of (R-c): Lemma A.4 with B = zA′, α ≤ |z|κ < a_h/8 ≤ 1/16 and α₀^{re} < a_h/2 ≤ 1/4 gives η^{−2}ξ_j²|∂𝐔_z − 𝟏| ≤ α₀^{re}(U) + 4|z|κ < a_h/2 + a_h/2 = a_h. For P_{z,w}: |zA′_R + wA′_I| ≤ (|z| + |w|)|A′| by §3.1, and similarly for ∇_U and 𝐉; repeat with |z| replaced by |z| + |w|. ∎

**Proposition A.6 (the pair perturbation, (d)).** [P] Let P = (U, A′, 𝐉) on 𝐒 with α₀^{re}(U) < a_h/2 and κ(P) < a_h/16. Then for all fluctuation coordinates x, y,

  |𝖠(P)(x, y) − 𝖠(U, 0)(x, y)| ≤ H₁κ(P)e^{−μ₀d(x,y)},  H₁ := 16H/a_h.

*Proof.* If κ(P) = 0 then P = (U, 0) and there is nothing to prove. Otherwise R := a_h/(8κ(P)) > 2. By Lemma A.5, P_z ∈ ℛ with radii < a_h for |z| < R, so by Lemma A.3 each entry is holomorphic on the disc |z| < R, and by Lemma A.2 it is bounded there by He^{−μ₀d(x,y)}. Fix unit vectors u, v in colour space and put f(z) := ⟨u, 𝖠(P_z)(x, y)v⟩ and g(z) := f(z) − f(0). Then g is holomorphic on |z| < R, g(0) = 0 and |g| ≤ 2He^{−μ₀d(x,y)} =: S. The Schwarz lemma applied to g/S on the disc of radius R gives |g(z)| ≤ S|z|/R. At z = 1, P₁ = P and P₀ = (U, 0), so |⟨u, (𝖠(P) − 𝖠(U,0))(x, y)v⟩| ≤ 2He^{−μ₀d}/R = 16Hκ(P)e^{−μ₀d}/a_h. The supremum over unit u, v is the operator norm of the block. ∎

*Remark A.6′.* The real factor U is the same in P and in its reference, so α₀^{re}(U) enters only through the hypothesis α₀^{re}(U) < a_h/2, never through η. This is why no M-dependent gauge constant (SA's a_w = CLMa₀, L14141) enters (d).

**Corollary A.6″ (comparison of two complex pairs).** [P] Let P = (U, A′₁, 𝐉₁) and P̃ = (U, A′₂, 𝐉₂) on 𝐒 with α₀^{re}(U) < a_h/2, κ(P̃) ≤ a_h/32, and κ(P − P̃) := κ((U, A′₁ − A′₂, 𝐉₁ − 𝐉₂)) ≤ a_h/32. Then |𝖠(P)(x, y) − 𝖠(P̃)(x, y)| ≤ (32H/a_h)κ(P − P̃)e^{−μ₀d(x,y)}.

*Proof.* If κ(P − P̃) = 0 there is nothing to prove. Otherwise put R := (3a_h/32)/κ(P − P̃) ≥ 3 and, for |z| < R, P_z := (U, A′₂ + z(A′₁ − A′₂), 𝐉₂ + z(𝐉₁ − 𝐉₂)). Its complex radius is ≤ κ(P̃) + |z|κ(P − P̃) < a_h/32 + 3a_h/32 = a_h/8. The proof of Lemma A.5, with this bound in place of |z|κ, keeps P_z in the class with all radii below a_h. Lemmas A.2 and A.3 apply on the disc. With f, g as in Proposition A.6 but centred at P₀ = P̃, the Schwarz lemma at z = 1 gives |g(1)| ≤ 2He^{−μ₀d}/R = (64H/(3a_h))κ(P − P̃)e^{−μ₀d} ≤ (32H/a_h)κ(P − P̃)e^{−μ₀d}, and P₁ = P. ∎

This is the comparison from a *complex* reference, the first direction in which the brief asks P82 to be extended. Shifts P ↦ P ∔ h of ST1 (10) change the splitting by A″ − A′ with ‖A″ − A′‖ controlled by the shift (st1-r2 Lemma 7); Corollary A.6″ then bounds the change of 𝖠 entrywise with decay.

**Proposition A.7 (symmetry and reality, (a)).** [P] At every pair of the class with radii < a_h, 𝖠(P) is complex symmetric for the bilinear transpose; 𝖠(U, 0) is real symmetric.

*Proof.* *Reality at (U, 0).* By (H3) each 𝖠_ω is real at real pairs, and the absolutely convergent sum of real matrices is real. *Symmetry, by the definitions.* Every quadratic part in Definition 3.4 (the Wilson Hessian Δ^W, Δ′_π[𝐉], Δ^{(2)}[j] of SA L10155, 𝖤^{(2)}[w], 𝖦_V^{(2)}) is by definition the symmetric matrix of a quadratic form; a = a₀ξ_c^{−2} is diagonal. The inverse of an invertible symmetric matrix is symmetric, and C^𝖳XC and QXQ^𝖳 are symmetric when X is. G′ = (D^𝖳D + Q′^𝖳aQ′)^{−1} is symmetric, hence R = 1 − G′Q′^𝖳(Q′G′²Q′^𝖳)^{−1}Q′G′ satisfies R^𝖳 = R and DRD^𝖳 is symmetric; so 𝖦₀, 𝖦 = (𝖦₀^{−1} − Δ′_π[𝐉])^{−1} and 𝖦₁ = (𝖦^{−1} − 𝖲^𝖳Δ^{(2)}[𝖧^𝖳𝐉]𝖲)^{−1} are symmetric (SA L10142–10155), and so are (Q𝖦₁Q^𝖳)^{−1}, Δ_k and 𝖠. This algebra holds at every pair where the inverses exist, real or complex; by (H0) they exist on the class. At (U, 0) it agrees with a2-layers L673. *Remark (a check that does not read the definitions of the quadratic parts at complex pairs).* Suppose only that 𝖠 is symmetric at real pairs. Put F(z, w) := 𝖠(P_{z,w}) − 𝖠(P_{z,w})^𝖳 with P_{z,w} of Lemma A.5, on the bidisc |z|, |w| < R/2. Each entry is holomorphic in each variable (Lemma A.3). For real (t, s), P_{t,s} = (U, tA′_R + sA′_I, t𝐉_R + s𝐉_I) is a real pair (the potential is Hermitian, so e^{iη(tA′_R+sA′_I)}U is unitary, and the current is real), so F(t, s) = 0. For fixed real s, z ↦ F(z, s) vanishes on the real segment, hence on the disc (identity theorem in one variable). For fixed z, w ↦ F(z, w) vanishes for real w by the previous sentence, hence on the disc. So F ≡ 0 on the bidisc; since R > 2, (1, 1) lies in it, and P_{1,1} = P. So symmetry at real pairs alone implies it at P. ∎

**Theorem A (operator theorem at complex regular pairs on separated sequences).** [P, from (I-A) and (I-C).] Put a := c_L/2, μ₀ := δ_h/4, H := 2N_rC_h², b := HV₀(μ₀), H₁ := 16H/a_h, and

  κ_* := min{a_h/16, c_L a_h/(32 H V₀(μ₀))}.

Let 𝐒 ∈ 𝒮_sep(ρ, M₁) with the floors above, and P = (U, A′, 𝐉) a triple on 𝐒 with α₀^{re}(U) < a_h/2 and κ(P) < κ_*. Then all inverses in 𝖠(P) exist and:

- (a) 𝖠(P) is complex symmetric; 𝖠(U, 0) is real symmetric;
- (b) Re⟨v, 𝖠(P)v⟩ ≥ a|v|² for all complex v (Hermitian pairing), and Re⟨v, χ𝖠(P)χv⟩ ≥ a|χv|² for every coordinate projection χ; ‖𝖠(P)‖ ≤ b;
- (c) |𝖠(P)(x, y)| ≤ He^{−μ₀d(x,y)};
- (d) |𝖠(P)(x, y) − 𝖠(U, 0)(x, y)| ≤ H₁κ(P)e^{−μ₀d(x,y)}.

All of a, b, H, μ₀, H₁, κ_* are functions of L only. The same holds at (U, 0), with κ = 0.

*Proof.* By Lemma A.5 (z = 1) P lies in the class with radii < a_h, so (I-C) applies; by (H0) all inverses exist (they are blocks of the finite-range system of h-walk Lemma U, `gate h-walk` §4: "ADVANCE as finite-dimensional algebra"). (a) is Proposition A.7. (c) and the norm bound are Lemma A.2. (d) is Proposition A.6, whose hypothesis κ(P) < a_h/16 holds. (b): (U, 0) is a real regular pair with radii α₀^{re}(U) < a_h/2 ≤ a_*, so by (I-A) 𝖠(U, 0) is real symmetric with ⟨u, 𝖠(U, 0)u⟩ ≥ c_L‖u‖² for real u; for complex v = u + iw with u, w real, ⟨v, 𝖠(U,0)v⟩_H = ⟨u, 𝖠u⟩ + ⟨w, 𝖠w⟩ ≥ c_L|v|² because 𝖠(U,0) is real symmetric (the cross terms cancel). By (d) and the Schur test, ‖𝖠(P) − 𝖠(U, 0)‖ ≤ H₁κ(P)V₀(μ₀) < (16H/a_h)·(c_La_h/(32HV₀))·V₀ = c_L/2. So Re⟨v, 𝖠(P)v⟩ ≥ c_L|v|² − (c_L/2)|v|² = a|v|². For a projection χ, ⟨v, χ𝖠χv⟩ = ⟨χv, 𝖠χv⟩, so the bound holds with |χv|². ∎

**Corollary A.8 (the actual next-fibre operator).** [P, adding (I-B).] Under the hypotheses of Theorem A, with κ(P) also below the ceiling of (I-B) and C_IIe^{μ₀r_II}V₀(μ₀)κ(P) ≤ a/2, the operator 𝖠^full(P) satisfies (a)–(d) with a/2, b + a/2, H + C_IIκ_*e^{μ₀r_II}, μ₀ and H₁ + C_IIe^{μ₀r_II} in place of a, b, H, μ₀, H₁.

*Proof.* 𝖠^full − 𝖠 = −𝖤_free has entries ≤ C_IIκ(P), vanishing for d > r_II (I-B), so |𝖤_free(x, y)| ≤ C_IIκ(P)e^{μ₀r_II}e^{−μ₀d(x,y)}. It vanishes at (U, 0), where V is block axial. It is complex symmetric (it is 𝖢^𝖳X𝖢 with X the symmetric matrix of a quadratic form) and real at real pairs. By the Schur test its norm is ≤ C_IIe^{μ₀r_II}V₀(μ₀)κ(P) ≤ a/2. Add to Theorem A: the gap drops by at most a/2, the norm grows by at most a/2, and the entry and perturbation bounds add. ∎

**Tests of Part A against counterexamples.** [P]

1. *A seam-concentrated complex field.* Try A′ supported in a strip next to a seam between ℒ_j (fine) and ℒ_{j+1} (coarse), small in fine units but of size ≈ 1 in coarse units on the coarse side. Such a pair is not in the class: (R-a) on ℒ_{j+1} is read in coarse units. At the bonds on the shared face the coarse condition binds. The outward rows of level j+1 read fine bonds of their outer block in ℒ_j; these bonds are bounded in fine units, and the row's linear part carries the factor ξ_c of its own length (SA L10139, 𝒬 = 𝗆(Q + C^{(2)} + ⋯)), so their contribution in coarse units is bounded by a fixed power of L (SA L10873). No failure.
2. *Large real curvature with small complex part.* Theorem A asks α₀^{re}(U) < a_h/2, a fixed ceiling. A real factor regular only with α₀^{re} of order one is not covered; (I-A) and (I-C) give nothing there. This is a hypothesis, met in Part B.
3. *Loss of holomorphy at the edge of the disc.* The Schwarz argument needs the bound on the whole open disc |z| < R, not on its closure. Lemma A.5 places every P_z, |z| < R, strictly inside the class. No failure.
4. *Dependence on the pair far away.* (d) is a uniform bound over all entries. It needs κ(P) small on all of Ω₀. A pair whose complex part is small only on a region W is outside the hypothesis. §6.3 shows the consumers' pairs are small everywhere under (I-G).

---

## 6. Part B: the pairs where the consumers evaluate 𝖠 are regular pairs

Fix in addition: ρ = R₁M₁ ≥ 3L² + 2 (used in Lemma B.2); M with M₁ | M (aligned powers of L), LM ≥ 2R₁M₁ (ST1 row 8, L139, "LM ≥ 2ρ₀") and cM ≥ 2ρ (c the constant of SA L17398). These are lower bounds on M.

### 6.1 Separation

**Lemma B.1 (every sequence in force is in 𝒮_sep(ρ, M₁)).** [P from (I-D)] At every structure σ of a finite history, the determining sequence in force, extended by the next step's region, and every meet of it with a separated tower of gap ≥ ρ, lies in 𝒮_sep(ρ, M₁).

*Proof.* By (I-D) each member is a union of level-j M-cubes or level-j cells (cells are unions of M-cubes, `os-draft.md` L106). Since M₁ | M and the partitions are aligned, a level-j M-cube is the union of (M/M₁)⁴ aligned level-j M₁-cubes. The gap is ≥ LMξ_j ≥ 2R₁M₁ξ_j > ρξ_j for stage, ν-, prepared and output sequences, and ≥ cMŘ_jξ_j ≥ cMξ_j ≥ 2ρξ_j > ρξ_j for label sequences. The next region Ω_{k+1} of the step is a member of the label at the next level (SA L17398), with the same gap. A meet of two separated sequences is separated with the smaller gap (Y3 L53314–53321; `os-draft.md` Corollary 2.4(iii)), and its members are unions of cubes of the common refinement. ∎

### 6.2 The real factor

**Lemma B.2 (the actual background is regular in the nest in force).** [P from (I-E), (I-F)] Let σ be a structure, 𝐒 = 𝐒^σ, U the actual background (in any gauge), and put

  ϱ_re := C_RA C_λ sup_m (log θ_m)^{2r_R} ε_m,  C_G := 8L⁴B_*(c_gM₁ + 2L).

Take c_rg ≤ 1 without loss. If 2L⁶(c_gM₁/L + 2)ϱ_re < c_rg and L³ϱ_re ≤ 1/8, then α₀^{re}(U) ≤ C_Gϱ_re.

*Proof.* (R-c), real half. Let p be a plaquette of Ω₀ in ℒ_j. Its largest corner scale l(p) ≥ ξ_j. By (I-E), η^{−2}ξ_j²|∂U(p) − 𝟏| ≤ η^{−2}l(p)²|∂U(p) − 𝟏| ≤ C_RAλ(p)ε_{m(p)} ≤ ϱ_re ≤ C_Gϱ_re. (A plaquette is a complete element for its curvature reading: its stencil is itself.)

(R-g), j ≥ 1. Let Z ⊂ Ω₀ ∩ (ℒ_j ∪ ℒ_{j+1}) be a cube of side at most c_gM₁ξ_j. Work in level-(j+1) units, where ξ_{j+1} = 1, ξ_j = L^{−1}, ξ_{j−1} = L^{−2} and the bare mesh is η_{j+1}; Z has side s ≤ c_gM₁/L. Its side-(s+6) enlargement Z⁺ is Z + 3ξ_{j+1} in sup-norm. Since Z ⊂ Ω_j and dist_∞(Ω_j, Ω_{j−1}^c) > ρξ_{j−1} = ρξ_{j+1}/L² ≥ (3 + 2/L²)ξ_{j+1} by ρ ≥ 3L² + 2, the set Z⁺ together with a margin of two bare meshes lies in Ω_{j−1} ⊂ Ω₀. So every point of Z⁺ has scale ≥ ξ_{j−1}, and every bond of Z⁺ has its six plaquettes in Ω₀ (it is complete). By (I-E), on Z⁺: |∂U − 𝟏| ≤ ϱ_reη²/l² ≤ ϱ_reL⁴η² = wL²η² with w := L²ϱ_re (strictly less after replacing ϱ_re by any larger number; the conclusion is unchanged), and |J°_η(U)| ≤ ϱ_re/l³ ≤ L⁶ϱ_re. The Wilson divergence differs from η²J°_η by at most six quadratic plaquette terms (st1-r2 L650–656), so |D_U^𝖳∂U| ≤ 6η^{−1}(wL²η²)² + η²L⁶ϱ_re = η²(6w²L⁴η + L⁴w). With w′ := Lw = L³ϱ_re this is < 2L³w′η² = 2L⁴wη² because 6wη + 1 < 2 when wη ≤ L²ϱ_re < 1/6. Also curvature < wL²η² ≤ w′L²η². The ceiling (s+2)L³w′ ≤ (c_gM₁/L + 2)L⁶ϱ_re < c_rg holds by hypothesis. (I-F) gives a real gauge on Z with |A|, |∇A| < 4L³B_*(s+2)w′ ≤ 4L⁶B_*(c_gM₁/L + 2)ϱ_re in level-(j+1) units. Converting, ξ_j|A| = L^{−1}|A| and ξ_j²|∇A| = L^{−2}|∇A| are both < 4L⁵B_*(c_gM₁/L + 2)ϱ_re = 4L⁴B_*(c_gM₁ + 2L)ϱ_re ≤ C_Gϱ_re.

(R-g), j = 0. Let Z ⊂ Ω₀ ∩ (ℒ₀ ∪ ℒ₁) be a cube of side nη, n ≤ c_gM₁. In complete axial gauge from a corner of Z, each link is the holonomy of a loop bounding a staircase of at most 3n plaquettes of Z (`a3-close.md` §1(iv)). By unitarity |Π_iV_i − 𝟏| ≤ Σ_i|V_i − 𝟏|, so |U(b) − 𝟏| ≤ 3n sup_p|∂U(p) − 𝟏| ≤ 3nϱ_re (η²/l(p)² ≤ 1). For U(b) = e^{iηA} with eigenvalues e^{±iθ}, |θ| ≤ π, one has |U(b) − 𝟏| = 2|sin(θ/2)| ≥ (2/π)|θ| and |ηA| = |θ|; so η|A| ≤ (3π/2)nϱ_re and η²|∇A| ≤ 2 sup η|A| ≤ 3πnϱ_re. With ξ₀ = η both are ≤ 10c_gM₁ϱ_re ≤ C_Gϱ_re (B_* ≥ 1, L ≥ 2). (3nϱ_re ≤ 3c_gM₁ϱ_re < 2 by the first hypothesis, so the angle is in range.)

The class conditions are gauge invariant (curvature) or existential (gauges), so the conclusion holds for U in the step's gauge. ∎

### 6.3 The complex part

**Lemma B.3 (the complex part of a consumer pair).** [P from (I-G)] Under (I-G), every input pair P′ = (U, A′, 𝐉′) at a main-step input structure σ satisfies

  κ(P′) ≤ ϱ_c := (1 + β_s)C_λ max{C₀, C₁} sup_m θ_m^{−1/2}(log θ_m)^{q+2r_R}.

*Proof.* Insert λ_σ ≤ C_λ(log θ_m)^{2r_R} and r_ι(m) = C_ιθ_m^{−1/2}(log θ_m)^q into the bounds of (I-G), bond by bond, and take the supremum. ∎

**On the import (I-G).** It says two things. First, the consumer's pair is constrained on *every* bond of Ω₀^σ, not only on the reads of the records of one activity. Second, the constraint at b is read in the scale of the layer of b in the nest in force, with the lift. The first is necessary for the consumer's own formula: 𝖠(P′) is a function of the whole pair (Definition 3.4), and on a bond where the complex part is unconstrained 𝖠(P′) need not exist. IN1's quantifier already has this form ("every complex pair P in its admitted core with radii a₀, a₁ and independent current j₀", IN1 L57). SA's consumer has it too (SA L14093–14094: "Let P = (𝐔, 𝐉) be a regular complex pair"). The second is SA's design (SA L6141–6146: the lift is the difference of "the original regularity layer and the layer after each stage", and "The layer-m radii are multiplied by this lift"). It costs nothing at the real reference: A′ = 0, 𝐉′ = 0 meet every clause. It is preserved by the step's shifts with half the room: the shifts of ST1 obey n_b(H, K) = max{l|H|, l²|∇^UH|, l³|K|} ≤ C_DE_κ̄C_Aδ_src e^{−μd(b,S)} (st1-r2 (16)), which is a bound in the same current local units, and δ_src = A₁gℓ^{𝔭₀} (NL1-L L64) is o(r_ι) because q > 𝔭₀ (NL1-L L19, SA L19491).

If a consumer instead imposed only records frozen at their birth layer m_τ(b), a raised bond (m_σ(b) > m_τ(b)) would be bounded in current units only with the factor L^{p(m_σ − m_τ)} ≥ 1 (a potential scales by L^{−(u−v)}, st1-r2 (9)). Such frozen records are *weaker* than the current-layer ones, never stronger, so they do no harm when a current-layer record is also present. A current-layer record is formed at every structure that raises a bond: at stages by st1-r2 Lemma 10 ("On the set raised to level j+1 set the raw exponent ℰ = e_j + 1 ... The pointwise ... records at formation ... are admitted", st1-r2 L607, L630), at outputs by ST3 Lemma B1 ("admit every output record (pointwise, absolute, tower, lifted-core, witness)"). So (I-G) holds as soon as the consumer's domain retains the pointwise records formed at the structures between the last raising of each bond and σ. That is the chain-domain rule of st1-r2 L84 ("𝒟_{a|σ} imposes every record born between a and σ") for chains that start no later than those structures; for a pair at σ itself it is the requirement to carry the records formed at σ and before.

### 6.4 The envelopes vanish with the coupling

**Lemma B.4.** [P] Let Q ≥ 0 and f_Q(θ) := θ^{−1/2}(log θ)^Q. If γ ≤ e^{−Q} and θ_m ≥ γ^{−2} for all m, then sup_m f_Q(θ_m) ≤ γ(2 log γ^{−1})^Q, and the right side tends to 0 as γ → 0.

*Proof.* For θ > 1, f_Q′(θ) = θ^{−3/2}(log θ)^{Q−1}(Q − ½ log θ) ≤ 0 when log θ ≥ 2Q. Since θ_m ≥ γ^{−2} ≥ e^{2Q}, f_Q(θ_m) ≤ f_Q(γ^{−2}) = γ(2 log γ^{−1})^Q. For the limit write t = log γ^{−1} → ∞; then γ(2 log γ^{−1})^Q = e^{−t}(2t)^Q → 0 because e^t ≥ t^{⌈Q⌉+1}/(⌈Q⌉+1)! for t ≥ 0. ∎

Apply it with Q = 𝔭₀ + 2r_R to ϱ_re (ε_m = A₀θ_m^{−1/2}(log θ_m)^{𝔭₀}, IN1 L42) and with Q = q + 2r_R to ϱ_c.

### 6.5 The theorem

**Theorem B (PR-lay).** [P, from (I-A)–(I-G).] Let the constants be as in Theorem A and §6, and let γ_PR > 0 be so small that for γ ≤ γ_PR:

- (γ1) C_G ϱ_re(γ) < a_h/2, 2L⁶(c_gM₁/L + 2)ϱ_re(γ) < c_rg and L³ϱ_re(γ) ≤ 1/8 (Lemma B.2);
- (γ2) ϱ_c(γ) < κ_* (Theorem A), and ϱ_c(γ) is below the ceiling of (I-B) when 𝖠^full is used;
- (γ3) γ ≤ γ_B(M) of ST3 Lemma B1, when σ follows an output.

Such γ_PR exists by Lemma B.4. Then at every main-step input structure σ of every finite history with coupling ceiling γ ≤ γ_PR, for the nest in force 𝐒^σ, the actual real background U in the step's gauge, and every input pair P′ = (U, A′, 𝐉′) obeying (I-G): (a)–(d) of Theorem A hold at P′ and at (U, 0), with

  a = c_L/2, b = HV₀(μ₀), H = 2N_rC_h², μ₀ = δ_h/4, η(P′) ≤ H₁κ(P′) ≤ H₁ϱ_c(γ), H₁ = 16H/a_h.

The same holds for 𝖠^full with the constants of Corollary A.8.

*Proof.* By Lemma B.1, 𝐒^σ ∈ 𝒮_sep(ρ, M₁) with the floors of Part A. By Lemma B.2 and (γ1), α₀^{re}(U) ≤ C_Gϱ_re < a_h/2. By Lemma B.3 and (γ2), κ(P′) ≤ ϱ_c < κ_*. Theorem A applies to P′ and to (U, 0). ∎

**Order of choice in Theorem B.** a, b, H, μ₀, H₁, κ_* are fixed with L (and the lower bounds on M₁, R₁) in rows 1–3 of `c4-order.md`, before κ. They are independent of M and of κ̄. C_G depends on L and M₁ (row 2). M enters only through the lower bounds of §6 (M₁ | M, LM ≥ 2R₁M₁, cM ≥ 2ρ). γ_PR depends on L, M₁, C_RA, C_λ, r_R, A₀, C₀, C₁, q, β_s and, through (γ3), on M; C₀, C₁ are row-16 constants chosen after M and κ̄ (NL1-L L130). So γ_PR is a ceiling on γ chosen last, as IN1 L57 allows ("below ceilings that may depend on M").

### 6.6 What the two consumers receive

**Corollary B.5 (IN1).** [P] IN1's import (I-1) holds at the pairs where the UM gas is evaluated and at their real reference, with a, b, H, μ₀ of Theorem B, depending on L only, and with (d) in the form η(P) ≤ H₁κ(P). In IN1's notation, H_p(M) may be taken equal to the M-free constant H₁, and a₁ + j₀ ≥ κ(P) when IN1's radii are read in the local scale of SA L10129–10137. IN1's row-16 ceiling (IN1 L323) becomes H₀H₁ϱ_c(γ) ≤ ¼ min{ε₀, 1/(3DM⁴)}, again a ceiling on γ after M. Theorem B therefore closes the "one way the cycle could come back" of IN1 L808: no constant fed to Part A depends on M or κ̄.

*Proof.* IN1 Part A reads (I-1) only at the pair P and at (U, 0) (IN1 L807). Theorem B gives both. ∎

**Corollary B.6 (NL1).** [P] (CI-form)(ii) of NL1-L L518 holds at every P′ ∈ 𝒪_σ that obeys (I-G): 𝖠(P′) satisfies (I-1)(a)–(d) with the constants of Theorem B. IN1 Proposition A.5 then supplies (I-2)'s hypotheses at P′ from these constants (IN1 L217–266), so the Gaussian comparison applies at P′.

*Proof.* 𝒪_σ has the fixed real factor U of the main step (NL1-L L377). Theorem B applies. ∎

**Corollary B.7 (stage Gaussians).** [P] If a consumer forms the Gaussian of a stage of level j from the fibre precision of the stage sequence cut at depth j, compressed to the collar's free coordinates, then (a)–(d) hold there with the same constants, with k replaced by j and the conditioning set the collar.

*Proof.* Lemma B.1 places the stage sequence in 𝒮_sep(ρ, M₁). (I-E) holds at the stage structure (st1-r2 Lemma 10 is stated for stages). Theorem A is stated for every separated sequence and every compression. ∎

### 6.7 Tests of Part B against counterexamples

1. *A real factor regular only in the old nest.* At a stage the member j+1 grows, so points move to a coarser layer. If the background were controlled only in the old (finer) units, its curvature in the new units would carry L² per raise, and L^{2v} after v raises. This does not happen: the stage tests are posed in the units of the current shell (SA L17624, §2.5), and each raise is preceded by the test of that stage. st1-r2 Lemma 10's proof (L640–646) records this: "A row raised from j to j+1 pays the conversion 3L²L_♭^{2e_j}ε_j ≤ 6L²L_♭^{−2}L_♭^{2(e_j+1)}ε_{j+1} ... The exponent of a retained shell is no larger than the value assigned at the last stage that raised it". So at most one factor L² is paid per test, and it is a fixed constant inside C_te. No failure.
2. *Healed points raised by Ř levels.* At an output the healed component moves to layer t, which can be ≈ Ř levels above its original layer (the waiting depth, SA L17585). This is the situation of `layered-a3.md` (44), where a loss L^{2Ř} defeats the coupling ceiling. For 𝖠 it does not arise: the output background satisfies (I-E) in output units (ST3 Lemma B1), and the output forms pointwise records at the healed points in output units. The jump of Ř levels is between two different nests (before and after the output); 𝖠 is formed on one of them. No failure.
3. *A complex part bounded only by an inherited tower clause.* Tower clauses bound the tower configuration T_e, not the raw complex part A′. A pair could satisfy every tower clause and have A′ large at some bond. Such a pair violates (I-G), and 𝖠 need not exist there. This is why (I-G) is an import and not a consequence of the tower records. No failure of Theorem B, whose hypothesis excludes it.
4. *Lifts too large.* If λ grew faster than any power of log θ, Lemma B.4 would fail. (I-E) and (I-G) carry λ ≤ C_λ(log θ)^{2r_R} (st1-r2 (57); CA-I L45514 "𝖫₀^{2e_n} ≤ 𝖼₁R_n"). No failure under those inputs.

---

## 7. Part C: seams, lifts, and PR1(5)

### 7.1 Where the seam loss enters, and why 𝖠 does not read it

`layered-a3.md` (3): with 2 ≤ L_♭ < L/2, L^{2v}/L_♭^{2v} > 4^v for v ≥ 1, so a lift L_♭^{2v} cannot absorb a scale loss L^{2v}. layered-a3 L138–141 says where the loss comes from: "At the **same point**, an unlocalised target tower can assign scale ξ_q where the ambient nest assigns ξ_{h_q}. Equation (4) then gives only CL^{2(q−h_q)}P_σ(x) in target curvature units." So the loss is the ratio of two scale assignments at one point: one by the nest in which the field is controlled, one by the nest (a tower) in which it is measured.

𝖠(P) is formed on one nest, the nest in force, and its ingredients are read in that nest's scales (SA L10200–10208, L14091–14107; §2.2). The real factor is controlled in that same nest (I-E); the complex part is constrained in that same nest (I-G). So the two scale assignments coincide at every point, and v = 0. The only scale changes inside 𝖠 are between adjacent layers of the one nest: a row or stencil at a seam reads one adjacent scale, at a fixed L-cost (SA L10873), and the layer barrier d_𝐁 ≥ ρ(|i − j| − 1)₊ (SA PX4, L10626–10630) controls propagation across many layers. Both are inside the constants of (I-A) and (I-C).

### 7.2 What the lifts do here

In this file a lift never has to absorb anything. It only enlarges a radius: the real factor's curvature in current units is up to C_RAλε (I-E), and the complex part is up to (1 + β_s)λr_ι (I-G). Both enlarged radii are still o(1) as γ → 0 (Lemma B.4), because θ^{−1/2} beats every power of log θ and λ ≤ C_λ(log θ)^{2r_R}. So the coupling ceiling pays for the lifts. This is the reverse of the failure in `layered-a3.md` (44), where a factor L^{2Ř} with Ř ≈ (log θ)^r had to be paid and cannot be.

The brief's suggested remedy, "Where the lift factors fail at seams, use the separation and decay instead", is therefore not needed for (I-1). Separation enters only through Lemma B.1 (every sequence in force is separated, so (I-A) and (I-C) apply to it), and decay only through (I-C).

### 7.3 PR1(5) as printed

PR1(5) (assembly L187) and `layered-a3.md` (1) bound dist_∞(D_e(t), 𝒯_e^c) for the data D_e(t) = M_{𝐁′_e}(𝐔(t)) of inherited records e along the stage path, and the derivatives of the seven normalized readouts F_a of `intrinsic-dom.md` (8). Every quantity there is a tower datum or a readout of a tower. Its consumer is named at `layered-a3.md` L9: "This is input (B) of `stage-resp.md`." It is needed for the stage response and, through it, for ST1's admission of substituted pairs into target chain domains (the tower clauses of Theorem 14's first bullet, st1-r2 L855–856, and Theorem V′'s "Π_f(P′; s, ζ) lies in the restricted target chain domain", NL1-L L377).

It is not needed for (I-1). IN1 L800's sentence "At those pairs (I-1)(b)–(d) is the layered complex comparison PR1(5)" should read: "At those pairs (I-1)(b)–(d) is Theorem PR-lay of `pr-lay-draft.md`; PR1(5) as printed is a separate tower statement, consumed by the stage response." PR1(5) as printed stays [O]. Its first open step remains `layered-a3.md` Lemma RC, (51), a real curvature bound on inherited carriers in the target tower's scale; the three attacks on it and their failures are recorded at layered-a3 L1324–1361. This file does not attack Lemma RC, because nothing in (I-1) reads it.

The same split applies to `a3-close.md` L99 ("the layered case ... for references not covered by Lemma R"): Lemma R concerns the tower clauses of the hereditary core; it is not an input of (I-1).

### 7.4 The P82 route

The brief suggests a route through P82: local inverses in each layer, a seam correction from the one-M-cube separation, and a complex Neumann series in the weighted norm. P82 Theorem P is already layered (§2.8): it is stated for real Reg_α backgrounds on every separated sequence, with weights in 𝒲_θ for d_𝐁. Its operator is the A3 constrained inverse S_q°, whose blocks are G, H, T, C₀ of p82 (14). To reach 𝖠 from it one would have to (i) replace q^𝖳q by the Wilson Hessian Δ^W (a curvature-size local correction, SA L11313 ff.), (ii) add the current terms Δ′_π[𝐉] and 𝖲^𝖳Δ^{(2)}[𝖧^𝖳𝐉]𝖲, (iii) form (Q𝖦₁Q^𝖳)^{−1} and 𝖤^{(2)}[𝖧₁^𝖳𝐉], and (iv) carry each step to complex pairs by a Neumann series in the all-weight norms (p82 (6)–(7)). Each step is a relative perturbation of size O(α₀ + α₁ + γ₀). It would give (c) and (d) at complex pairs from real-reference weighted bounds, which is SA's own design at L10875–10937. It is a second route to Part A, independent of the walk expansion (I-C). I did not write it out: (I-C) already gives the entry bound on the whole complex class, and the Schwarz step then gives (d) with no further perturbation theory. If a referee rejects (I-C) at complex pairs, this is the fallback, and its first step is (iv) for G′ = (D^𝖳D + Q′^𝖳aQ′)^{−1}, which SA L10875–10898 sketch.

---

## 8. Order of constants

| Constant | Where fixed | Depends on | Before κ? | Independent of M, κ̄? |
|---|---|---|---|---|
| L, c_g | row 1 | geometry | yes | yes |
| c_L, a_*, M_*, ρ_* | (I-A) | L | yes | yes |
| a_h, C_h, δ_h, N_r, C_L′, M_h | (I-C) | L | yes | yes |
| r_II, C_II | (I-B) | L | yes | yes |
| M₁ ≥ max{M_*, M_h, 8C_h⁶} | row 2 (lower bound) | L | yes | yes |
| R₁ ≥ 64L, ρ = R₁M₁ ≥ max{ρ_*, 3L² + 2} | row 3 (lower bound) | L | yes | yes |
| a = c_L/2, μ₀ = δ_h/4, H = 2N_rC_h², b = HV₀(μ₀) | Theorem A | L | yes | yes |
| H₁ = 16H/a_h, κ_* | Theorem A | L | yes | yes |
| c_rg, B_* | (I-F) | L | yes | yes |
| C_RA, C_λ, r_R | (I-E) | L, profile, RUN | yes | yes |
| C_G = 8L⁴B_*(c_gM₁ + 2L) | Lemma B.2 | L, M₁ | yes | yes |
| M: M₁ \| M, LM ≥ 2R₁M₁, cM ≥ 2ρ | row 8 (lower bounds only) | — | — | — |
| C₀, C₁ (radius table) | row 16 | after M, κ̄ | no | no (used only in γ_PR) |
| γ_PR | last | all of the above, M (γ3), C_ι | no | no (a ceiling on γ) |

No constant in the first eleven rows is read by any choice made before it, and none depends on M or κ̄. M occurs only as a lower bound. The only quantities that depend on M or κ̄ are the radius coefficients C_ι and the coupling ceiling γ_PR, which no earlier constant reads. This is IN1's requirement (IN1 L808) and ST1's (st1-r2 L143).

---

## 9. Status table, imports, and what changes elsewhere

| Item | Statement | Status | Rests on |
|---|---|---|---|
| Lemma A.1 | metric comparison, ball bound | [P] | — |
| Lemma A.2 | entry decay on the class | [P] | (I-C) |
| Lemma A.3 | holomorphy along complex families | [P] | (I-C) |
| Lemma A.4 | curvature of a complex perturbation | [P] | — |
| Lemma A.5 | scaled family stays in the class | [P] | Lemma A.4 |
| Prop. A.6 | (d), η ≤ (16H/a_h)κ | [P] | A.2, A.3, A.5 |
| Cor. A.6″ | complex-reference comparison | [P] | as A.6 |
| Prop. A.7 | (a) symmetry and reality | [P] | (I-A), (I-C), definitions |
| Theorem A | (a)–(d) at complex regular pairs on separated sequences | [P] | (I-A), (I-C) |
| Cor. A.8 | the same for 𝖠^full | [P] | (I-B) |
| Lemma B.1 | every sequence in force is separated | [P] | (I-D) |
| Lemma B.2 | the actual background is regular in the nest in force | [P] | (I-E), (I-F) |
| Lemma B.3 | the complex part is small in current units | [P] | (I-G) |
| Lemma B.4 | envelopes vanish with γ | [P] | — |
| Theorem B | PR-lay, consumer form | [P] | (I-A)–(I-G) |
| Cor. B.5–B.7 | IN1 (I-1); NL1 (CI-form)(ii); stage Gaussians | [P] | Theorem B |
| PR1(5) as printed | tower tube distances, readout derivatives | [O] | `layered-a3.md` Lemma RC first |

Imports, with their status at the time of writing:

| Import | Source | Status |
|---|---|---|
| (I-A) real gap on layers | `a2-layers.md` Theorem A | Claude; checked by Codex (`a2-layers-gate.md`) as a conditional theorem after repairs; rests on `a2-curved.md` (Codex; `a2-curved-gate.md`) |
| (I-B) gauge-gradient term | `a2-full.md` Lemma 4.1, Theorem II | Claude; checked by Codex (`a2-full-gate.md` L68): no failing step after the convention correction |
| (I-C) walk expansion on the class | `h-walk.md` Theorem H (H1)–(H3), kernel part | Claude; checked by Codex (`h-walk-gate.md` §8): kernel decay and fixed-region holomorphy advance conditionally; canonicity and isometry clauses fail and are not used |
| (I-D) separation of sequences in force | SA L17398–17407; `os-draft.md` Lemma 2.3, Cor. 2.4 | SA [SS]; os-draft is a Claude pass-1 draft, not checked |
| (I-E) background in current units | `st1-r2.md` Lemma 10 (59); ST3 Lemma B1 | Codex pass-2 distillation, not refereed; ST3 a Claude round-3 draft |
| (I-F) RCG4 | `a1-balaban.md` §3.8 | checked by Codex (`a1-balaban-gate.md`), conditional on F0 |
| (I-G) current-layer radii | SA L6141–6152; st1-r2 L84, L92, L607; ST3 Lemma B1 | design; §6.3 |

**First not-yet-checked import on the path, in reading order.** (I-A) and (I-C) are checked by the other model, conditionally. (I-D) and (I-E) are drafts in their own lanes (OS, ST1). (I-G) is a design statement. Of these, (I-G) is the one that no library text yet states in the form used: "every input pair of the main step's domain satisfies the simple clauses of SA (R4), at the current layer of every bond of Ω₀^σ, with the lifted current-layer radii". I recommend that NL1 put this clause into its definition of 𝒪_σ (NL1-L L377) and that ST1 state it as a record family in its chain domain. §6.3 shows it is formed at every structure that raises a bond, is met at the real reference, and survives the step's shifts with half the room. It is a definition to adopt, not an estimate to prove.

**What changes elsewhere (recommendations; this file edits nothing else).**

1. `ym4-assembly.md` PR1(5): split into PR1(5a) = Theorem PR-lay [P here] and PR1(5b) = `layered-a3.md` (1) [O]; move PR1(5b)'s consumer to the stage response.
2. `in1-draft.md` L62 and L783: replace "at layered stage pairs ⟦open: PR-lay⟧" by "at layered stage pairs [P] (`pr-lay-draft.md` Theorem B), with H_p(M) = H₁ independent of M". L800: as in §7.3.
3. `nl1-L-draft.md` L528: the first open input of (CI-form) is no longer ⟦PR-lay⟧; add (I-G) to the definition of 𝒪_σ (L377).
4. `os-draft.md` (F-4): satisfied; Theorem A is stated on 𝒮_sep(ρ, M₁) for every ρ above a floor, with constants independent of ρ.

---

## 10. Result

**PR-lay is proved in the form both consumers need**, as an implication from the imports (I-A)–(I-G) (Theorem B; Corollaries B.5, B.6). At every input pair of the main step, after any stages, outputs and drop-outs, and at its real reference, the fibre precision 𝖠 is complex symmetric, has the gap a = c_L/2 on every compression, has entries ≤ He^{−μ₀d}, and differs from its real reference by ≤ H₁κe^{−μ₀d}, with κ the local-scale size of the complex part. The constants a, b, H, μ₀, H₁ depend on L only. They are fixed before κ and are independent of M and κ̄; M enters only as a lower bound, and M, κ̄ enter only through the coupling ceiling γ_PR. The perturbation prefactor H₁ is independent of M, which is stronger than IN1's H_p(M).

The proof has two parts. Part A is an operator theorem on every complex regular pair of every separated sequence. Its new step is a Schwarz-lemma bound along the complex line through the pair (Proposition A.6), which needs only the entry bound on the class from the walk expansion (I-C); the complex gap then follows from the real gap (I-A). Part B admits the consumers' pairs into the class: separation of every sequence in force (I-D), the real background's bound in the units of the nest in force (I-E, I-F), and the current-layer radii of the consumer domain (I-G). The radii carry lifts, and the coupling ceiling pays for them (Lemma B.4).

The seam loss L^{2v}/L_♭^{2v} of `layered-a3.md` (3) does not enter, because 𝖠 is formed on the nest in force and reads no tower (§7.1). PR1(5) as printed, a tower statement, stays [O] with `layered-a3.md` Lemma RC first; it is not on the path of (I-1) (§7.3).

There is no remaining Outstanding statement inside this file. The first import on the path that is not yet stated anywhere in the form used is the design clause (I-G) (§6.3, §9). It is a definition for NL1 and ST1 to adopt, not an open estimate.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the setting, the class of regular pairs, the operators and the geometry of R; Tadeusz Balaban for the method; Jonathan Dimock for its exposition. All new arguments here are written by hand. No run discharges a step. This text is not yet checked by the other model.
