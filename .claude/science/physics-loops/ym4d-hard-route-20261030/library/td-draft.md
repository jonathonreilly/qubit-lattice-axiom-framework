# Lemma TD and its input (DR-row): row-resolved response, composition along exempt supports, and the exempt potentials of the regular gas — pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, pass 1 of Lemma TD (the first open item of `ci-form-draft.md`, §9) and of the input (DR-row) that §9.3 there proposes. Research text. It is not an audit, it grants no status, and no other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

No step rests on a computation. Every argument is a finite sum, a Möbius inversion over subsets of a finite set, the fundamental theorem of calculus in finitely many variables, a Cauchy estimate on a polycircle, a one-variable Schwarz lemma (repeated), the Borel–Carathéodory inequality (proved here from Schwarz), the cut property of minimum spanning trees, a layer-cake identity for step functions, a depth-first encoding of finite trees, or a comparison of explicit numbers. Each is meant to be Lean-formalisable.

Credit. The regular polymer gas (UM1)–(UM30), the coarse decoupling, the class (R23) with its exempt tree length d^♮, the island and kept-form operations and their localisation are the work of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the outline `ym4.tex` ("SA"), the complete account `ca_II.tex` ("CA-II"), and the three-dimensional manuscript `YM3_I.tex` ("Y3"), whose per-string hull products (Y3 L52582–52585) are the device behind §5. The renormalisation-group step, the operator 𝐂, the windows, the localisation in small gauges and the large-field method are Tadeusz Balaban's (CMP 99, 109, 116, 119, 122). Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. The allocation rule of Lemma 3.3 is J. C. Bird's (Networks 6 (1976) 335–350); the proof here is a self-contained layer-cake proof. Our own notes used: `ci-form-draft.md`, `nl1-L-draft.md`, `st1-r2.md`, `st1-draft3.md`, `p81-crit-draft.md`, `p82.md` (frozen), `pr-lay-draft.md`, `in1.md` (frozen), `pan-draft.md`, `ym4-assembly.md`.

Line references. SA L = `scratchpad/sa/ym4.tex`; Y3 L = `scratchpad/sa/YM3_I.tex`; CI L, NL1-L L, ST1 L, ST3 L, P82 L, PR L, IN1 L, PAN L, AS L = lines of `library/ci-form-draft.md`, `nl1-L-draft.md`, `st1-r2.md`, `st1-draft3.md`, `p82.md`, `pr-lay-draft.md`, `in1.md`, `pan-draft.md`, `ym4-assembly.md`. I quote the lines before I say what a source proves or assumes. "SA states" means that the text at those lines says so; it does not mean that SA proves it.

Status words: **[P]** proved here, not checked; **[I]** import, with owner and the owner's status; **[R]** reading of a source, flagged; **[O]** Outstanding; **[design]** a choice; **[CE]** counterexample to an implication.

---

## 0. Result

**What is proved.**

1. **(DR-row)** [P, from DR's interface]. Theorem 4.1: for sources S = Σ_{c∈W}S_c with S_c on the rows of the fine cube c, the cube-Möbius pieces of DR's response at s = 𝟏 obey, at every bond b,

  n_b(h_W) ≤ A_row e^{−μd_+(b, supp S)} ∏_{c∈W}(4‖S_c‖_src/s_D) · q^{St(W ∪ {Δ_b})},  q := 6400/(e^{κ̄} − 1),

 with St the Steiner length in the cube graph and A_row := C_DE_κ̄s_D(e^{κ̄} − 1)^{15}. Corollary 4.2 gives the same bound for the main-step shift as a function of the free complex fluctuation. The inputs are ST1's DR on its full switch polydisc with (16) (ST1 L119–124, L842), read as NL1-L's (DR-ζ) and (DR-loc) (NL1-L L259–267). The constants C_D, C_A, μ that are fixed before κ are DR's own (ST1 row 2, L133) and are independent of M and κ̄. The κ̄-dependent quantities E_κ̄, s_D, q enter only amplitudes and rates read by ceilings on γ and floors on κ̄ (§4.3).
2. **Composition lemma** [P]. Lemma 5.1: if Φ is holomorphic and bounded on a room ball of shifts, and the shift is h₀ + Σ_U 𝐠_U with row-resolved pieces 𝐠_U, then the cube-Möbius piece of Φ in W decays like e^{−(a−6)·MST_X(W ∪ ∗)}, where X is the set of read cubes collapsed to one point ∗. There is no factor in |X|, in |∂X| or in the number of reads. The device is Y3's hull product: each piece 𝐠_U carries the product ∏_{c∈U}t_c of its cube parameters, and the radii are Bird's cost shares of the collapsed spanning tree (Lemma 3.3).
3. **Per-term multi-point bound (TD′)** [P]. Proposition 6.2: for every exempt term f, every P′ ∈ 𝒪_σ and every nonempty W of gas cubes, |f_W| ≤ ω̃_f ∏_{c∈W}(2β_c/δ) · e^{−(a−6)MST_{X(f)}(W∪∗)}.
4. **Lemma TD as stated is not implied by its inputs** [CE]. Proposition 7.1: the class bounds (R23), the interface of Theorem V′, and the geometry facts (G-gap), (G-isl), (G-sep) admit exempt terms for which no rate λ_T allowed by (UM19) gives (TD). The reason: (R23) allows no decay across an exempt island (SA L6198), and the d_f length that (UM1) uses pays for each island crossing.
5. **Lemma TD^♮** [P]. Theorem 8.4: (TD) holds with d_f replaced by the island-exempt gas length ℓ^♮ (the Steiner length in the cube graph with each standing-island hub contracted), with λ_T = λ_V and a^{ex} → 0 as γ → 0 after M and κ̄.
6. **Theorem UM^♮(P′)** [P, as an implication]. §9: SA's regular gas at P′ with exempt potentials of length ℓ^♮. The polymers become *linked* coarse sets: wall-components joined through exempt potentials. The counts (UM7^♮), (UM9^♮), the factorisation over compatible linked polymers, the activity bound, the Kotecký–Preiss criterion and the logarithm bound all hold uniformly in P′ ∈ 𝒪_σ.
7. **CI in the remaining cases** [P, as a reduction]. Theorem 10.2: at every main-step structure, also those that carry exempt terms, CI holds for the regular-gas logarithms. The proof goes through Proposition CI-ind of NL1-L with its hypothesis (i) strengthened to (i′) (§10.1), which CI-old, ST1 and DR supply.

**What is not proved here.** This draft adds no Outstanding statement of its own. Its conclusions are conditional on the imports and readings of §12.2. The main ones are: DR's actual decoupled construction (ST1's declared supply, ST1 L939); the stencil form of (DR-loc); the reading (Adm) of Theorem V′'s proof; the projection reading (Proj) of SA's d^♮; the per-cube sums (N-B), (N-K) of PAN; the wall factorisation (I-3) [SS]; and the filing reading (File^♮), that islands standing at σ stay exempt at the output label. **Design amendment needed** [design, §11]: Theorem UM^♮ needs a larger floor on L than frozen IN1 row 2 (IN1 L228), and a floor on κ that depends on L. Both are admissible in the order. Because IN1 is frozen, the lead decides.

**Line count**: reported in the session reply.

---

## 1. Sources, quoted

### 1.1 ST1 and NL1-L: the response and the substitution

- *DR* (ST1 L119–124): "An actual regional response (H, K), holomorphic in its complex input pair, datum and |s_Δ| < e^{κ̄}, is given, with reality, covariance, restriction consistency, common-lift transport and splitting over face-connected components. ... For source S, it obeys n_b(H, K) := max{l|H|, l²|∇^UH|, l³|K|} ≤ C_DE_κ̄C_Aδ_src e^{−μd(b,S)} (16). Here C_D, μ are fixed constants; E_κ̄ ≥ 1 is a specified parameter factor ... It is not an IN1 precision constant." ST1 L842 (hypothesis 3 of Theorem 14): "DR is given on the full switch polydisc, with (16), specification at one, restriction and component splitting. Its component response vanishes when there is no source and at zero switches." ST1 L939: DR's "actual decoupled DR construction" is among the declared supplies. So DR is an input of ST1, not a result.
- *Order* (ST1 L133, row 2): "Take AV/CURV, profile, derivative and DR base constants and rates uniform for all larger separation gaps, including C_E, c_D ..."; L128: "all constants in rows 1–6 precede κ and are independent of M, κ̄". L139 (row 8): "M ≥ C_dec κ̄ for the DR construction".
- *(DR-ζ)* (NL1-L L259–263): for every s with |s_Δ| < e^{κ̄} and every complex completed source S with ‖S‖_src < s_D := ε_De^{−c_Dκ̄}, h(s; P, S) is "defined, jointly holomorphic in (s, S), real at real (s, S), zero at S = 0, and n_b(h(s; P, S)) ≤ C_DE_κ̄‖S‖_src e^{−μd_+(b, supp S)} (4.1)". NL1-L flags this as a reading of (16).
- *(DR-loc)* (NL1-L L265): "For every s and S as in (DR-ζ), and every face-connected component K′ of supp s, the restriction of h(s; P, S) to the bonds whose initial site lies in a cube of K′ depends only on P, on s|_{K′} and on the values of S on the rows assigned to the cubes of K′." NL1-L L267 calls this a "new statement", owner ST1.
- *The shift* (NL1-L L275–277): v(s, ζ) := gŷ ⊕ u(s ⊙ ζ), 𝐡(s, ζ) := h(𝟏; P, S(v₀)) + h(s; P, S(v(s, ζ))) − h(s; P, S(v₀)), F_f(s, ζ) := f(ρ_X^{res}(P ∔ 𝐡(s, ζ)^δ); 𝔮_X). (FL-main)(c), (e) (NL1-L L251, L253): ‖S(v) − S(v′)‖_src ≤ C_A‖v − v′‖_∞, and S(v) on a row c depends only on v on rows within lattice distance R_σ of c.
- *Theorem V′* (NL1-L L377) and its proof (NL1-L L379, referring to Steps 0–7, 9–11 of L325–367). Step 2 (L333–335): n_b(𝐡(s, ζ)) ≤ A_Ve^{−μd_+(b,𝒮)}, A_V := C_DE_κ̄C_A(3δ_src + c_Tge^{κ̄}R_V). Steps 3–7 (L339–351) turn this bound into levelling, the pinned norm, inclusion in the target domain and composition with f.
- *ST1 Lemma 4* (ST1 L248–253): "If n_b(h) ≤ Ae^{−μd(b,S)}, then n_b(h^δ) ≤ C_lev A e^{−μd(b,S)/2}, ε̂_y ≤ K_pin A e^{−μd(y,S)/2}. These constants are independent of depth and M, κ̄. Holomorphy at specified output bonds holds where every relevant endpoint top is levelled." Its proof (ST1 L281): "n_b(h^δ) ≤ C_m max_{y′∈nb(y(b))}‖h‖_{y′}". So the pinned shift at b reads h only near b.
- *Theorem 14's localisation* (ST1 L884): "Cauchy in the distinct switch variables bounds its mixed derivative along [0, 1]^K by 2b_f(e^{κ̄} − 1)^{−|K|}". This is the switch Möbius that ci-form's attack A1 used.
- *Proposition S* (NL1-L L399–404): the screened radius is capped by R_cap ≍ e^{−Cκ̄}/g "whatever the distance".

### 1.2 P82 and PR-lay: where the decay comes from

- *P82 Theorem P* (P82 L203–218): for every 0 ≤ θ ≤ θ₀ and every weight w ∈ 𝒲_θ = {w > 0 : w(y)/w(z) ≤ e^{θd(y,z)}} (P82 L90), ‖a‖_{X,w} + ‖ℓ‖_{Y,w} + ... ≤ C°(‖f‖_{F,w} + ‖b‖_{Y,w}); "Every block of this inverse ... has (7)" (P82 L218), the row bound sup_i Σ_jμ_j(σ_j/σ_i)‖A_{ij}‖e^{θd(y_i,y_j)} ≤ C (P82 L95–99). P82 L188: "All bounds and ceilings in (11)–(12) are functions of L, α_H only ... The later construction size M and decoupling radius κ̄ do not occur."
- *PR-lay Theorem A* (PR L276–287): |𝖠(P)(x, y)| ≤ He^{−μ₀d(x,y)}, |𝖠(P)(x, y) − 𝖠(U, 0)(x, y)| ≤ H₁κ(P)e^{−μ₀d(x,y)}, with μ₀ = δ_h/4 and "All of a, b, H, μ₀, H₁, κ_* are functions of L only."

### 1.3 SA: the gas, the class, the localisation

- *(UM1)* (SA L14304–14318): "For the actual local potentials assume |V(Y; P, B)| ≤ a_Ye^{−λ_Vd_f(Y)}(1 + M^{−4}Σ_{b⊂Y}|B(b)|²), a_Y ≤ a"; L14295–14296: "Lengths d_f and d_c are tree lengths in fine and coarse cube units."
- *Polymers* (SA L14365–14371): "Polymers Z are nonempty wall-connected coarse domains. ... Disconnected regions factor into their wall-components rather than being counted again as single polymers."
- *(UM7)* (SA L14422–14437): #Y^♯ ≤ C_h(1 + d_f(Y)/L), proved by a closed walk along a covering tree cut into segments of length ≤ L; "All neighborhood widths are fixed independently of L".
- *The exempt length and the class* (SA L6191–6203): "For a finite exempt family 𝖧 of nonempty regions, define d^♮_{j,𝖧}(X) by minimizing M^{−1} times tree length also over subfamilies 𝖥 ⊂ 𝖧 contained in X: the tree meets each cube outside ∪𝖥 and each member of 𝖥, but need not fill those members. For a label use the level-j hulls of its standing islands as 𝖧. ... It is at most d_j(X) and asserts no decay across an exempt island." Then (R23): |B_𝒮(j, X, o)| ≤ 𝖡e^{−κd^♮_j(𝒮;X)}. SA L6185–6188 (as PAN L108 quotes them) list the boundary origins, among them "a step remainder beside an island".
- *Kept forms* (SA L17564, the paragraph beginning "Carriage"): "For a piece of a kept form whose carrier is R, the oscillation with respect to the pair is bounded by Cp₀(g_j)²e^{−κd^♮_{j+1}(R)}, measured in the hull length of the carrier".
- *Localisation* (SA L17903–17920): "Each walk in the response carries a parameter s(Δ), |s(Δ)| < e^{κ̄}, for every cube it visits. Setting a parameter to zero prevents a walk from crossing that cube. ... Brackets in the s variables and Schwarz's lemma in λ then give f(U^{old}) − f(U^{new}) = Σ_{Y⊃X}f_Y, |f_Y| ≤ 2𝖺b_fe^{−(κ̄−1)𝔪(X,Y)}."

### 1.4 Y3: the hull product

Y3 L52582–52585: "Complete the parameter family by s̄ = 1 on Z°^♯, by s on the other big cubes of R, and by zero outside R. Multiply a coefficient or string by the product of s̄ over its big-cube hull, omitting terms with zero product." Parameters are attached term by term, not to a black-box function. §5 attaches the product ∏_{c∈U}t_c to the response piece 𝐠_U, whose hull is U.

### 1.5 IN1 (frozen) and PAN

- *The rate window* (IN1 L353–360): "Θ = C_h^{UM}{3 + c_ℓ[(1 + 4β_s)κ + g_*]}, λ₀ + σ₀ + Θ/L ≤ λ < κ/(2C_h^{WF}) − ε_rate (24). The floor on L makes the upper endpoint grow faster in κ than the lower endpoint, so the window is nonempty for large κ. Next choose κ̄ above the response/bracket floors and with log(e^{κ̄} − 1) ≥ Θ, then M." IN1 L228 (row 2): "choose odd L with L > 4C_h^{WF}C_h^{UM}c_ℓ(1 + 4β_s)".
- *PAN geometry* (PAN L163–165): (G-gap) "Every cube of Λ_i^{pre} is at d_c ≥ G = 10LŘ_i from the live region 𝒵_{i−1}", with the proof "Λ_i^c = Z_i ⊃ ... ⊃ Ŷ^{~10}, in level-i cells", Ŷ the hull. (G-isl) "A standing island's level-(i − 1) hull lies in a cube of C₀ level-i cells." (G-sep) "Distinct standing-island hulls are at d_c ≥ Ř_i." PAN L65: S(a) := Σ_{n≥0}(2n + 1)⁴e^{−an} ≤ 2 for a ≥ 6.
- *PAN inputs* (PAN L154–158): (L-B) with X_f := T ∪ ∪𝖥 and (N-B) N_B^{ent} := sup_ΔΣ_{f∈𝔉_B: X_f∋Δ}e^{−(κ/2)d^♮(𝒮;X_f)} ≤ C_B^{ent}(M)ℓ^{τ_B}; (L-K) the analogue; (L-I) Re F_f ≤ C_ΨV°(ω).

### 1.6 ci-form

CI L472–480 states Lemma TD (quoted in §7). CI L310–312 defines the cube-Möbius candidate (5.5) and proves it exact, local, holomorphic and real. CI L488–498 gives the three failed attacks. CI L504: "(DR-row) [proposed input for ST1's DR; not stated by ST1]".

---

## 2. Setting and notation

Fix a main-step input structure σ of level i and P′ ∈ 𝒪_σ (CI Definition 1.1). Notation as in CI §1–§2: ℓ := log θ_{i−1}, g := θ_{i−1}^{−1/2}, 𝔟 := A₁ℓ^{𝔭₀}, R := c_Rℓ^q with c_R = 1, R_V = R.

- *Cubes.* 𝒞 is the set of fine cubes (level-(i − 1) M-cubes) of the torus, and 𝒞_Λ ⊂ 𝒞 the gas cubes. d_c is the sup-norm distance of cube indices. It equals the graph distance in the *-adjacency graph, in which each cube has 3⁴ − 1 = 80 neighbours. For a bond b, Δ_b is the cube that contains the initial site of b, and B_b is the set of cubes that contain initial sites of bonds in the stencil of n_b (the bonds that n_b reads: b and its neighbours for ∇^U). For M ≥ 4 the stencil has diameter < M, so |B_b| ≤ 2⁴ = 16, Δ_b ∈ B_b, and B_b is *-connected.
- *Lengths.* For a finite nonempty A ⊂ 𝒞, St(A) is the least number of edges of a tree in the cube graph whose vertex set contains A, and MST(A) is the weight of a minimum spanning tree of (A, d_c). For X ⊂ 𝒞 nonempty and W ⊂ 𝒞 finite, MST_X(W ∪ ∗) is the minimum spanning tree weight of the complete graph on W ∪ {∗} with weights w(c, c′) := d_c(c, c′) and w(c, ∗) := d_c(c, X) (X collapsed to ∗). Convention (as CI §5.4): SA's d_f, d_c, d_j, d^♮_j are read as cube-graph tree lengths in their cube units. If SA counts edges with another fixed length, every rate below is multiplied by that fixed factor. **[R: CI L260]**
- *Sums.* S(a) := sup_Δ Σ_{Δ′∈𝒞}e^{−ad_c(Δ,Δ′)} ≤ Σ_{n≥0}(2n + 1)⁴e^{−an} ≤ 2 for a ≥ 6 (PAN L65).
- *Fluctuation.* ζ ∈ E_ℂ is a complex fluctuation on the free bonds I (all in gas cubes). For U ⊂ 𝒞, ζ𝟏_U is ζ on the bonds of I in cubes of U and 0 elsewhere. |ζ|_c := max of |ζ_{b,a}| over bonds b of I in c. 𝔻_r := {|ζ|_∞ < r}.
- *Hubs.* 𝖧 is the family of level-(i − 1) hulls of the standing islands of σ (the exempt family of PAN (L-B)). For H ∈ 𝖧, the hub is H̃ := {Δ : d_c(Δ, H) ≤ 2}. Define

  G₀ := G − 2 = 10LŘ_i − 2,  s₀ := Ř_i − 4,  D_H := C₀LŘ_i + 6,  r_H := ⌊(s₀ − 3)/2⌋.

 By (G-gap) (its proof gives the distance from the gas to the hulls Ŷ), d_c(𝒞_Λ, H̃) ≥ G₀. By (G-sep), distinct hubs are at d_c ≥ s₀. By (G-isl), each hub lies in a box of side D_H. **[I: LF1(2) via PAN L163–165]** For s₀ ≥ 3, a cube is at d_c = 1 from at most one hub.
- *The contracted graph Γ^♮.* Its vertices are the cubes outside ∪H̃ and one vertex [H̃] per hub. Edges: *-adjacency between cubes, and Δ ~ [H̃] iff d_c(Δ, H̃) = 1. π : 𝒞 → V(Γ^♮) maps a hub cube to its hub and fixes the other cubes. For A ⊂ 𝒞, St^♮(A) is the least number of edges of a tree in Γ^♮ whose vertex set contains π(A). For W ⊂ 𝒞_Λ put ℓ^♮(W) := St^♮(W). Since π does not increase path lengths, ℓ^♮(W) ≤ St(W).
- *Ř ceiling.* (Ř) r_H ≥ 257L, 4log(D_H + 3) ≤ r_H, 8log(D_H + 3) ≤ s₀ − 2. Since Ř_i ≥ (ℓ − 1)^r → ∞ (PAN L395) and D_H is linear in Ř_i, (Ř) holds for γ below a ceiling fixed after L and C₀. **[P, as a ceiling]**

---

## 3. Combinatorial lemmas

**Lemma 3.1 (animals).** For Δ ∈ 𝒞 and n ≥ 1, the number of *-connected Y ⊂ 𝒞 with Δ ∈ Y and |Y| = n is at most 6400^{n−1}. The same bound holds for *-connected sets of coarse cubes.

*Proof.* Choose a spanning tree of Y rooted at Δ. Its depth-first closed walk has 2(n − 1) steps, and each step moves to one of 80 neighbours. The walk determines Y. So the count is at most 80^{2(n−1)} = 6400^{n−1}. ∎

**Lemma 3.2 (Steiner and spanning trees).** For finite nonempty A ⊂ 𝒞: St(A) ≤ MST(A) ≤ 2St(A). The same holds in Γ^♮ with its graph distance.

*Proof.* Realise each edge of a minimum spanning tree by a geodesic. The union is connected, contains A and has at most MST(A) edges, so St(A) ≤ MST(A). Conversely, double the edges of a Steiner tree τ. Its Euler tour is a closed walk of length 2St(A) through every point of A. List A in order of first visit. The consecutive distances sum to at most 2St(A), and the path through A in this order is a spanning tree. ∎

**Lemma 3.3 (Bird's allocation is a cost sharing below every coalition).** Let K be a complete graph on a finite vertex set 𝒱 with weights w ≥ 0, r ∈ 𝒱 a root, and V := 𝒱 ∖ {r}. Let τ be a minimum spanning tree of K, rooted at r. For v ∈ V let ℓ_v := w(v, p(v)), with p(v) the τ-parent. Then Σ_{v∈V}ℓ_v = MST(K), and for every U ⊂ V,

  Σ_{v∈U}ℓ_v ≤ MST(K[U ∪ {r}]),

with K[·] the induced complete subgraph.

*Proof.* The first identity holds because v ↦ (v, p(v)) is a bijection from V to the edges of τ.

*Cut property.* Let S_v be the vertex set of the τ-subtree of v (v and its τ-descendants). Every pair x ∈ S_v, y ∉ S_v has w(x, y) ≥ ℓ_v. Otherwise, replacing the edge (v, p(v)) by (x, y) gives a spanning tree of smaller weight, since removing (v, p(v)) splits τ into S_v and its complement.

*Layer cake.* For a finite weighted complete graph K′ on 𝒱′ and t ≥ 0, let κ_{K′}(t) be the number of components of the graph on 𝒱′ with edges {w ≤ t}. Let τ′ be a minimum spanning tree of K′. The edges of τ′ with weight ≤ t form a forest F_t with #{e ∈ τ′ : w(e) > t} + 1 components. Its components are those of the threshold graph, because each threshold edge (x, y) not in τ′ closes a τ′-cycle whose other edges weigh at most w(x, y) ≤ t (the cycle property, proved like the cut property). So #{e ∈ τ′ : w(e) > t} = κ_{K′}(t) − 1, and

  MST(K′) = Σ_{e∈τ′}w(e) = ∫₀^∞#{e : w(e) > t}dt = ∫₀^∞(κ_{K′}(t) − 1)dt,

an integral of a step function, which is a finite sum.

*Pointwise inequality.* Fix t ≥ 0 and U ⊂ V. Let V_t := {v ∈ U : ℓ_v > t}. For v ∈ V_t, the cut property shows that no threshold edge of K[U ∪ {r}] joins S_v ∩ (U ∪ {r}) to its complement. So the component C_v of v in the threshold graph of K[U ∪ {r}] lies in S_v, and r ∉ C_v because r ∉ S_v. If C_v = C_{v′} for v ≠ v′ in V_t, then v′ ∈ S_v and v ∈ S_{v′}. Subtrees of a rooted tree are nested or disjoint, so S_v = S_{v′} and v = v′, a contradiction. Hence v ↦ C_v is injective from V_t into the components other than that of r, and #V_t ≤ κ_{K[U∪{r}]}(t) − 1.

*Integration.* Σ_{v∈U}ℓ_v = ∫₀^∞#V_t dt ≤ ∫₀^∞(κ_{K[U∪{r}]}(t) − 1)dt = MST(K[U ∪ {r}]). ∎

**Lemma 3.4 (the collapsed tree).** Let X ⊂ 𝒞 be nonempty and W ⊂ 𝒞 finite. Then:
(a) for every U ⊂ W and every x ∈ X, MST_X(U ∪ ∗) ≤ MST(U ∪ {x});
(b) for every c ∈ W, MST_X(W ∪ ∗) ≥ d_c(c, X);
(c) there is a subgraph Q of the cube graph with at most MST_X(W ∪ ∗) edges in which every cube of W is joined to a cube of X.

*Proof.* (a) Take a spanning tree of U ∪ {x} in d_c. Replace the vertex x by ∗ (if x ∈ U, add the edge (x, ∗) of weight d_c(x, X) = 0). An edge (c, x) becomes (c, ∗), of weight d_c(c, X) ≤ d_c(c, x). The other edges keep their weights. (b) The tree path from c to ∗ visits c = v₀, …, v_m = ∗. Its weight is Σ_{k<m−1}d_c(v_k, v_{k+1}) + d_c(v_{m−1}, X) ≥ d_c(c, X) by the triangle inequality. (c) Realise each tree edge (c, c′) by a cube-graph geodesic and each edge (c, ∗) by a geodesic from c to a nearest cube of X. Follow tree paths to ∗. ∎

**Lemma 3.5 (tree sums).** For x ∈ 𝒞, n ≥ 1 and a ≥ 6,

  Σ_{U⊂𝒞, |U|=n}e^{−aMST(U∪{x})} ≤ 2(2e)^n.

*Proof.* First let x ∉ U. Since e^{−aMST} ≤ Σ_T∏_{e∈T}e^{−aw(e)} over all spanning trees T, and each U arises from n! ordered tuples, the sum is at most (1/n!)Σ_{(c₁,…,c_n)}Σ_T∏_e e^{−ad_c(e)}. Encode a tree on {x = c₀, c₁, …, c_n} by its parent map p : {1, …, n} → {0, …, n}. There are at most n^n parent maps. For a fixed tree, sum the positions c_k in order of decreasing depth. Each sum Σ_{c_k}e^{−ad_c(c_k, c_{p(k)})} is at most S(a) ≤ 2. So the sum is at most (n^n/n!)2^n ≤ (2e)^n, using n^n/n! ≤ Σ_mn^m/m! = e^n. If x ∈ U, the sum is the same sum over U ∖ {x} of size n − 1, which is at most (2e)^{n−1}. Add the two cases. ∎

**Lemma 3.6 (repeated Schwarz; PAN Lemma 5.4, PAN L202–204).** Let g be holomorphic on the polydisc ∏_{c∈W}{|t_c| < r_c}, with values in a normed space, |g| ≤ A, and g = 0 whenever some t_c = 0. Then |g(t)| ≤ A∏_c|t_c|/r_c.

*Proof.* Schwarz's lemma in one variable at a time: t_c ↦ g(t) vanishes at 0 and is bounded by A, so |g(t)| ≤ A|t_c|/r_c, and g(t)/t_c is holomorphic, bounded by A/r_c and vanishes when another variable vanishes. Induct on |W|. For a vector-valued g, apply this to each bounded linear functional of norm ≤ 1. ∎

**Lemma 3.7 (Borel–Carathéodory).** Let φ be holomorphic on {|z| < 2}, with Re φ ≤ A and φ(0) real. Then |φ(1) − φ(0)| ≤ 2(A − φ(0)).

*Proof.* Put ψ := φ − φ(0) and A′ := A − φ(0) ≥ 0. If A′ = 0, then Re ψ ≤ 0 with Re ψ(0) = 0, so by the maximum principle for the harmonic function Re ψ, Re ψ ≡ 0, and ψ is constant 0. If A′ > 0, then χ(z) := ψ(2z)/(2A′ − ψ(2z)) is holomorphic on the unit disc (the denominator has real part ≥ A′ > 0), satisfies |χ| < 1 (since |w| < |2A′ − w| iff Re w < A′), and χ(0) = 0. Schwarz gives |χ(½)| ≤ ½. So |ψ(1)| ≤ ½|2A′ − ψ(1)| ≤ A′ + ½|ψ(1)|, hence |ψ(1)| ≤ 2A′. ∎

**Lemma 3.8 (hub structure).** Assume (Ř). Let W ⊂ 𝒞_Λ be nonempty and τ a tree in Γ^♮ whose vertex set contains W, minimal (every leaf lies in W), with n edges. Remove the hub vertices. The rest is a forest of cube trees C₁, …, C_m. Then Σ_{hubs [H̃]∈τ}deg_τ([H̃]) ≤ n/r_H, and m ≤ 1 + n/r_H.

*Proof.* For a component C, let k_C be the number of τ-edges from C to hubs. They go to distinct hubs, since two edges from the connected C to one hub would close a cycle. Let x₁, …, x_{k_C} ∈ C be their cube ends, with d_c(x_p, H̃_p) = 1. For p ≠ p′, d_c(x_p, x_{p′}) ≥ d_c(H̃_p, H̃_{p′}) − 2 ≥ s₀ − 2.

If k_C ≥ 2, the balls B(x_p, r_H) are pairwise disjoint, since 2r_H ≤ s₀ − 3. The tree C contains a path from x_p to x_{p′}, which leaves B(x_p, r_H). So C has at least r_H edges with both ends in B(x_p, r_H), for each p, and these edge sets are disjoint. So |E(C)| ≥ k_Cr_H.

If k_C = 1, C hangs on one hub. By minimality C contains a leaf y ∈ W ⊂ 𝒞_Λ. Then |E(C)| ≥ d_c(y, x₁) ≥ d_c(y, H̃) − 1 ≥ G₀ − 1 ≥ r_H.

So in all cases k_C ≤ |E(C)|/r_H. The sets E(C) are disjoint and contain no hub edge. Hence Σ_{hubs}deg = Σ_Ck_C ≤ n/r_H. If there is at least one hub, every C has k_C ≥ 1, so m ≤ Σ_Ck_C ≤ n/r_H. If there is no hub, m = 1. ∎

**Lemma 3.9 (Γ^♮ balls from gas cubes).** Assume (Ř). For x ∈ 𝒞_Λ and t ≥ 0, the number of cubes y ∈ 𝒞_Λ with dist_{Γ^♮}(x, y) = t is at most (81e)^t. Hence 𝔈(β′) := sup_{x∈𝒞_Λ}Σ_{y∈𝒞_Λ}e^{−β′dist_{Γ^♮}(x,y)} ≤ 2 for β′ ≥ log(162e).

*Proof.* Each such y is the endpoint of a geodesic of length t from x. Encode the geodesic by its moves. From a cube there are at most 81 moves (80 cubes, at most one hub). From a hub there are at most (D_H + 2)⁴ moves (the cubes at distance 1 from a box of side D_H). Along a geodesic between gas cubes, the first hub is at least G₀ − 1 steps from x, and consecutive hubs are at least s₀ − 2 steps apart. So the number h of hub visits is 0 if t < G₀ − 1, and at most 1 + (t − G₀ + 1)/(s₀ − 2) ≤ 2t/(s₀ − 2) otherwise (G₀ − 1 ≥ s₀ − 2). So the count is at most 81^t(D_H + 2)^{8t/(s₀−2)} ≤ 81^te^t by (Ř). Sum the geometric series. ∎

---

## 4. (DR-row): the row-resolved response

### 4.1 Statement and proof

Write h(s; S) := h(s; P′, S) for DR's response at the fixed input pair P′ ∈ 𝒪_σ. P′ lies in DR's pair domain by ST1 hypothesis 3 (ST1 L842), as Theorem V′'s proof uses (NL1-L L379). A *row-local source family* is a family (S_c)_{c∈W}, W ⊂ 𝒞 finite, such that S_c is supported on the rows assigned to the cube c. ‖·‖_src is a maximum over rows of row sizes, so ‖Σ_cτ_cS_c‖_src = max_c|τ_c|‖S_c‖_src for such families. **[R: the source norm is a row-wise maximum, as NL1-L (FL-main)(c) uses it]**

*(DR-loc′), the stencil form* **[R: of (DR-loc), NL1-L L265, and ST1 L842]**. For s in the switch polydisc and S as in (DR-ζ), and for every bond b, the vector of values of h(s; S) on the stencil of n_b depends only on s and S restricted to the union of the face-connected components of supp s that meet B_b, provided B_b ⊂ supp s.

This follows from (DR-loc) applied to each stencil bond, whose initial-site cube lies in B_b ⊂ supp s.

**Theorem 4.1 ((DR-row), source form).** [P from (DR-ζ), (DR-loc′)] Let e^{κ̄} − 1 ≥ 12800, put q := 6400/(e^{κ̄} − 1) ≤ ½, and let (S_c)_{c∈W} be a row-local source family with ‖S_c‖_src < s_D/2 for every c. For ∅ ≠ U ⊂ W put S_U := Σ_{c∈U}S_c and

  h_U := Σ_{U′⊂U}(−1)^{|U∖U′|}h(𝟏; S_{U′})  (with h(𝟏; 0) = 0).

Then for every bond b,

  n_b(h_U) ≤ A_row e^{−μd_+(b, supp S_W)} ∏_{c∈U}(4‖S_c‖_src/s_D) · q^{St(U∪{Δ_b})},  A_row := C_DE_κ̄s_D(e^{κ̄} − 1)^{15}.   (DR-row)

*Proof.* Fix b. Let 𝕊 be the switch polydisc {|s_Δ| < e^{κ̄} for all Δ}.

*Step 1 (the sup bound).* For ζ ∈ ℂ^W with |τ_c| := |ζ_c| < s_D/(2‖S_c‖_src), put S(τ) := Σ_cτ_cS_c. Then ‖S(τ)‖_src < s_D/2, and by (DR-ζ) the map (s, τ) ↦ h(s; S(τ)) is holomorphic on 𝕊 × ∏_c{|τ_c| < s_D/(2‖S_c‖)}. By (4.1),

  n_b(h(s; S(τ))) ≤ C_DE_κ̄(s_D/2)e^{−μd_+(b, supp S_W)},

because supp S(τ) ⊂ supp S_W.

*Step 2 (switch expansion with base B_b).* For a finite Y ⊃ B_b and t ∈ [0, 1]^{Y∖B_b}, let s^Y(t) be 1 on B_b, t on Y ∖ B_b and 0 off Y. Define

  g_Y(τ) := ∫_{[0,1]^{Y∖B_b}}∏_{Δ∈Y∖B_b}∂_{t_Δ}h(s^Y(t); S(τ)) dt,  g_{B_b}(τ) := h(s^{B_b}; S(τ)).

Let T := 𝒞 ∖ B_b and G(t) := h(s(t); S(τ)) with s(t) = 1 on B_b and t on T. Apply G(1_A ∪ 0) − G(0_A ∪ 0) = ∫₀¹∂_{t_Δ}G dt_Δ once in each variable of T and expand. This gives the finite identity h(𝟏; S(τ)) = Σ_{Y⊃B_b}g_Y(τ), as in CI Lemma 5.2(a).

*Step 3 (locality).* For t ∈ [0, 1]^{Y∖B_b}, supp s^Y(t) ⊂ Y and B_b ⊂ supp s^Y(t). By (DR-loc′), the stencil values of h(s^Y(t); S(τ)) depend only on the source on rows of cubes of Y. This holds for every t, hence also for the t-derivatives and their integral. So g_Y(τ) does not depend on τ_c for c ∉ Y.

*Step 4 (connectivity).* Let Δ ∈ Y ∖ B_b lie outside the *-component Y₀ of Y that contains B_b (B_b is *-connected). For every t, the face components of supp s^Y(t) that meet B_b are face-connected, hence *-connected, and so lie in Y₀. Changing t_Δ in [0, 1], including t_Δ = 0, changes neither these components nor s on them. By (DR-loc′) the stencil values do not change, so ∂_{t_Δ} = 0 and g_Y = 0. Hence g_Y ≠ 0 only for *-connected Y ⊃ B_b.

*Step 5 (switch Cauchy).* Fix t ∈ [0, 1]^{Y∖B_b} and 0 < ρ < e^{κ̄} − 1. On the polycircle |u_Δ − t_Δ| = ρ, |u_Δ| ≤ 1 + ρ < e^{κ̄}, so s^Y(u) ∈ 𝕊. Cauchy's formula, applied to each linear functional in n_b, and Step 1 give n_b(∏∂_{t_Δ}h(s^Y(t); S(τ))) ≤ C_DE_κ̄(s_D/2)e^{−μd_+(b,supp S_W)}ρ^{−|Y∖B_b|}. Integrate over the unit cube and let ρ ↑ e^{κ̄} − 1:

  n_b(g_Y(τ)) ≤ C_DE_κ̄(s_D/2)e^{−μd_+(b, supp S_W)}(e^{κ̄} − 1)^{−|Y∖B_b|}.

*Step 6 (source Möbius).* For ∅ ≠ U ⊂ W, h_U = Σ_{Y⊃B_b}(g_Y)_U(𝟏) with (g_Y)_U(τ) := Σ_{U′⊂U}(−1)^{|U∖U′|}g_Y(τ𝟏_{U′}), a finite rearrangement. If some c ∈ U lies outside Y, then g_Y(τ𝟏_{U′}) = g_Y(τ𝟏_{U′∪{c}}) for U′ ∌ c by Step 3, and the pairing U′ ↔ U′ ∪ {c} gives (g_Y)_U = 0. If U ⊂ Y, then τ ↦ (g_Y)_U(τ) is holomorphic on ∏_{c∈U}{|τ_c| < s_D/(2‖S_c‖)}, vanishes when some τ_c = 0 (by the same pairing), and is bounded by 2^{|U|} times the bound of Step 5. Lemma 3.6 at τ = 𝟏 gives

  n_b((g_Y)_U(𝟏)) ≤ C_DE_κ̄(s_D/2)e^{−μd_+(b,supp S_W)}(e^{κ̄} − 1)^{−|Y∖B_b|}∏_{c∈U}(4‖S_c‖/s_D).

(If ‖S_c‖ = 0 then (g_Y)_U = 0.)

*Step 7 (the sum over Y).* The nonzero terms have Y *-connected, Y ⊃ B_b ∪ U, so Δ_b ∈ Y and |Y| ≥ St(U ∪ B_b) + 1 ≥ St(U ∪ {Δ_b}) + 1. Also |Y ∖ B_b| ≥ |Y| − 16. By Lemma 3.1, with n₀ := St(U ∪ {Δ_b}) + 1,

  Σ_Y(e^{κ̄} − 1)^{−|Y∖B_b|} ≤ Σ_{n≥n₀}6400^{n−1}(e^{κ̄} − 1)^{16−n} = 6400^{−1}(e^{κ̄} − 1)^{16}Σ_{n≥n₀}q^n ≤ 2·6400^{−1}(e^{κ̄} − 1)^{16}q^{n₀} = 2(e^{κ̄} − 1)^{15}q^{St(U∪{Δ_b})}.

Multiply the bound of Step 6 by this sum: C_DE_κ̄(s_D/2)·2(e^{κ̄} − 1)^{15} = A_row. This is (DR-row). ∎

### 4.2 The main-step form

At the main step the source is the completed source of the fluctuation, which is not row-local in ζ: S(v) on a row c reads v on rows within R_σ of c ((FL-main)(e)). The mask s ⊙ ζ of NL1-L (4.2) makes the dependence local, as in Theorem V's Step 10. Define the response increment

  𝐆(s, ζ) := h(s; S(v(s, ζ))) − h(s; S(v₀)),  so 𝐡(P′; s, ζ) = 𝐡₀ + 𝐆(s, ζ) with 𝐡₀ := h(𝟏; S(v₀)),

and for ∅ ≠ U ⊂ 𝒞_Λ the cube-Möbius pieces 𝐆_U(ζ) := Σ_{U′⊂U}(−1)^{|U∖U′|}𝐆(𝟏, ζ𝟏_{U′}).

Put ϱ := min{s_D/2, C_Ac_chL^{−9}/2}/(c_TC_Ae^{κ̄}g), and assume the ceilings C_Aδ_src < s_D/2 and ‖gŷ‖_∞ < c_chL^{−9}/2 of Proposition S (NL1-L L406).

**Corollary 4.2 ((DR-row), main-step form).** [P from Theorem 4.1's proof, (FL-main), (V6)] For every ζ ∈ 𝔻_ϱ, every ∅ ≠ U ⊂ 𝒞_Λ and every bond b,

  n_b(𝐆_U(ζ)) ≤ A′_row e^{−μd_+(b,𝒮)}∏_{c∈U}(2|ζ|_c/ϱ)·q^{St(U∪{Δ_b})},  A′_row := 4C_DE_κ̄s_D(e^{κ̄} − 1)^{15},

with 𝒮 the main-step source set (NL1-L L295).

*Proof.* Repeat Steps 1–7 with g(s) := 𝐆(s, ζ) in place of h(s; S(τ)), and with ζ = Σ_cτ_cζ_c, ζ_c := ζ𝟏_{{c}}, |τ_c| < ϱ/|ζ|_c.

Step 1: for s ∈ 𝕊, |s ⊙ ζ|_∞ < e^{κ̄}ϱ. By (FL-main)(c)–(d), ‖S(v(s, ζ))‖_src ≤ C_Aδ_src + C_Ac_Tge^{κ̄}ϱ < s_D/2 + s_D/2 = s_D and ‖S(v₀)‖_src ≤ C_Aδ_src < s_D/2, and v(s, ζ) lies in the chart ball by the choice of ϱ. So both responses in g are defined and holomorphic, and by (4.1), n_b(g(s)) ≤ C_DE_κ̄(s_D + s_D/2)e^{−μd_+(b,𝒮)} ≤ 2C_DE_κ̄s_De^{−μd_+(b,𝒮)}. In Step 6 the polydisc is |τ_c| < ϱ/|ζ|_c, so repeated Schwarz gives the factor ∏_c(2|ζ|_c/ϱ). Step 7 gives the factor 2(e^{κ̄} − 1)^{15}q^{St}. The product of the constants is 2C_DE_κ̄s_D·2(e^{κ̄} − 1)^{15} = A′_row.

Step 3 (locality): for s = s^Y(t), the face components K′ of supp s that meet B_b lie in Y. The source rows of cubes of K′ read v on rows within R_σ, whose bonds lie in N₁(K′) by (V6) (M ≥ R_σ + 3). There the masked fluctuation is s_Δζ, which vanishes on cubes outside supp s ⊂ Y. So g_Y depends on ζ only on cubes of Y. Steps 2, 4–7 are unchanged. At s = 𝟏 the mask is trivial, so g(𝟏) = 𝐆(𝟏, ζ). The source-Möbius in τ at τ = 𝟏 is 𝐆_U(ζ). ∎

### 4.3 The order of the constants in (DR-row)

| Quantity | Origin | Fixed at | Read by |
|---|---|---|---|
| C_D, μ, C_A | DR base constants, chart constant (ST1 L119–124, L133, row 2) | before κ, independent of M, κ̄ | the room budget A_V and the decay e^{−μd_+}, as in Theorem V |
| 6400, 16 = \|B_b\| bound | Lemma 3.1, M ≥ 4 | geometric | everything below |
| E_κ̄ = e^{C_Eκ̄}, s_D = ε_De^{−c_Dκ̄} | DR's parameter factor and source threshold (ST1 L124; C_E, ε_D, c_D in row 2) | after κ̄ | amplitudes only: A_row, ϱ, K₁ (§6) |
| q = 6400/(e^{κ̄} − 1); rate a := ½log(1/q) per cube of MST | Theorem 4.1 | after κ̄ | floors on κ̄ only (§6, §8) |
| ϱ | Corollary 4.2 | after κ̄, before γ | the per-cube ratio 𝔟/ϱ → 0, a ceiling on γ |

No IN1 precision constant (a, b, H, μ₀, H₁) and no constant fixed before κ reads A_row, q, ϱ, E_κ̄ or s_D. This is ST1's rule (ST1 L143): "Neither E_κ̄ nor C(M) may be absorbed into those constants. They enter only the later amplitude and coupling ceilings."

### 4.4 Where the decay comes from, and the route not taken

*The decay.* Theorem 4.1 uses two decays of DR. (i) The factor e^{−μd_+(b, supp S)} is (16). (ii) The switch radius e^{κ̄} on the full polydisc gives q^{St} per cube. Both are properties of DR's construction, which is ST1's declared supply (ST1 L939). That construction is expected to obtain them from the weighted inverse of P82 (Theorem P: one constant C° for *all* weights in 𝒲_θ, P82 L203–218), with the row floor M ≥ C_dec κ̄ (ST1 L139), so that a walk across an M-cube gains enough to pay the switch value e^{κ̄}. P82's constants are functions of L and α_H only (P82 L188), so they are fixed before κ and independent of M and κ̄. PR-lay's entry decay He^{−μ₀d} (PR L19, L284; functions of L only, PR L287) is the decay of the fibre precision 𝖠, not of the response. It enters Lemma TD only through the Gaussian bounds of Theorem UM^♮ (CI Proposition 4.2, unchanged in §9). I have not re-proved DR's construction. Theorem 4.1 is conditional on it.

*The route not taken (Route P).* One can try to prove (DR-row) from CRIT's specification at one (ST1 L405–416: A = −𝔊W₁(A_•), A_• = ℓ₁B′ + A, H = 𝓛(A_•)) and P82 alone, without switches. The single-cube pieces work: with the weight w = e^{θd(·, c)} ∈ 𝒲_θ, the weighted contraction gives n_b(h_{{c}}) ≲ ‖S_c‖e^{−θd(b,c)}. For |U| ≥ 2, the Möbius piece of the fixed point is 𝒦N_U, where N_U is the Möbius piece of a local analytic nonlinearity evaluated at the pieces h_{U′}, U′ ⊂ U. Bounding N_U at a point y by a polydisc in the pieces needs a sum over U′ ⊂ U, and that sum converges only with spare decay. So each generation of the recursion loses a fixed part of the rate, and the recursion has unbounded depth. Expanding the Taylor series instead gives the covering sums of §9.3 of CI with factorial growth. The switch route avoids both. The switch Möbius is applied to the response alone, at a single output bond, where the decoration count of attack A1 does not arise (the base is the stencil B_b of at most 16 cubes, not an island hull).

---

## 5. The composition lemma

**Lemma 5.1 (composition along a hull product).** [P] Let 𝔈 be a finite-dimensional complex vector space, ℬ a finite set, and for b ∈ ℬ let n_b be a seminorm on 𝔈, A_b > 0 and Δ_b ∈ 𝒞. Put X := {Δ_b : b ∈ ℬ}. Let h₀ ∈ 𝔈 and let Φ be holomorphic on h₀ + 𝒪, 𝒪 := {g ∈ 𝔈 : n_b(g) < A_b/4 for all b ∈ ℬ}, with |Φ − Φ(h₀)| ≤ ω there. Let W ⊂ 𝒞 be finite and nonempty, δ := (8e)^{−1}, and 0 < β_c < δ for c ∈ W. Let a ≥ 12 and let 𝐠_U ∈ 𝔈 (∅ ≠ U ⊂ W) satisfy

  n_b(𝐠_U) ≤ (A_b/4)∏_{c∈U}β_c · e^{−aMST(U∪{Δ_b})}  for every b ∈ ℬ.   (5.1)

Define F(t) := Φ(h₀ + Σ_{∅≠U⊂W}t^U𝐠_U), t^U := ∏_{c∈U}t_c. Then

  |Σ_{W′⊂W}(−1)^{|W∖W′|}F(𝟏_{W′})| ≤ ω∏_{c∈W}(2β_c/δ)·e^{−(a−6)MST_X(W∪∗)}.   (5.2)

*Proof.* *Radii.* Let (ℓ_c)_{c∈W} be Bird's allocation (Lemma 3.3) for the complete graph on W ∪ {∗} with the collapsed weights of §2 and root ∗. Put r_c := (δ/β_c)e^{(a−6)ℓ_c}. Then r_c > 1.

*Admission on the polydisc.* Let |t_c| < r_c for c ∈ W. For b ∈ ℬ and ∅ ≠ U ⊂ W, Lemma 3.3 and Lemma 3.4(a) (with x = Δ_b ∈ X) give Σ_{c∈U}ℓ_c ≤ MST_X(U ∪ ∗) ≤ MST(U ∪ {Δ_b}). Hence by (5.1)

  |t^U|n_b(𝐠_U) < (A_b/4)δ^{|U|}e^{(a−6)Σ_{c∈U}ℓ_c − aMST(U∪{Δ_b})} ≤ (A_b/4)δ^{|U|}e^{−6MST(U∪{Δ_b})}.

Sum over U by Lemma 3.5 with a = 6: Σ_{U≠∅}δ^{|U|}e^{−6MST(U∪{Δ_b})} ≤ 2Σ_{n≥1}(2eδ)^n = 2Σ_{n≥1}4^{−n} = 2/3. So n_b(Σ_Ut^U𝐠_U) < A_b/4 for every b, the argument of Φ lies in h₀ + 𝒪, and F is holomorphic on ∏_c{|t_c| < r_c} with |F − Φ(h₀)| ≤ ω.

*Möbius as a function vanishing on the axes.* For t in the polydisc put g(t) := Σ_{W′⊂W}(−1)^{|W∖W′|}F(t𝟏_{W′}), where t𝟏_{W′} is t on W′ and 0 on W ∖ W′. Since Σ_{W′}(−1)^{|W∖W′|} = 0 for W ≠ ∅, g = Σ_{W′}(−1)^{|W∖W′|}[F(t𝟏_{W′}) − Φ(h₀)], so |g| ≤ 2^{|W|}ω. If t_c = 0 for some c ∈ W, the terms W′ and W′ ∪ {c} (c ∉ W′) cancel, so g = 0. At t = 𝟏, (t𝟏_{W′})^U = 1 iff U ⊂ W′, so g(𝟏) is the left side of (5.2).

*Schwarz.* Lemma 3.6 gives |g(𝟏)| ≤ 2^{|W|}ω∏_cr_c^{−1} = ω∏_c(2β_c/δ)·e^{−(a−6)Σ_{c∈W}ℓ_c}, and Σ_{c∈W}ℓ_c = MST_X(W ∪ ∗) by Lemma 3.3. ∎

*Why this avoids the three failures of CI §9.2.* A1: no switch acts on Φ, so there are no decorations around the read set. The room check is made read by read (a supremum over b ∈ ℬ), and for each read the sum over U is the tree sum of Lemma 3.5 rooted at one cube. Neither |X| nor |∂X| enters. A2: there are no shells. A3: the complexification is on the shift side. The room of Φ is a per-read seminorm ball, available independently at each read. The source never leaves DR's source ball: the vectors 𝐠_U are fixed responses to real or small sources, and only their coefficients t^U are complex. The graded radii r_c grow with ℓ_c, which is what the sup-norm interface could not supply.

**Corollary 5.2 (products).** [P] If Φ = ∏_{k=1}^mΦ_k, each Φ_k holomorphic on h₀ + 𝒪 with |Φ_k| ≤ B_k, then (5.2) holds with ω := 2∏_kB_k. *Proof:* |Φ − Φ(h₀)| ≤ 2∏B_k on h₀ + 𝒪. ∎

So products of exempt factors along a common exempt support (for example a kept form times an island exponent read on overlapping sets) keep the multi-point decay with the product of their bounds and the collapsed tree of the union of their reads.

---

## 6. The admission reading, and the multi-point bound for one exempt term

### 6.1 The room of an activity as a function of the shift

For f of a kind other than (W), with support X and reads, let ℬ_f be the finite set of bonds that Steps 3–7 of Theorem V read: the reads ℛ_X, the read sets Rd(y) of the endpoint tops of X, and the neighbourhoods nb(y(b)) of ST1 L281 for b ∈ ℛ_X. All lie in cubes of X^↑ (ST1 hypothesis 4, L843; NL1-L Step 10(iv), L365). Put X(f) := {Δ_b : b ∈ ℬ_f} ⊂ X^↑ ⊂ X_f, and A_b := A_Ve^{−μd_+(b,𝒮)}.

**(Adm)** [R: Theorem V′'s proof, NL1-L L339–351 and L379, with ST1 Lemma 4's locality, ST1 L281]. The map Φ_f(h) := f(ρ_X^{res}(P′ ∔ h^δ); 𝔮_X) is defined and holomorphic in h (jointly with (A′, 𝐉′) on the fixed-U fibre) on 𝒜_f := {h : n_b(h) < A_b for all b ∈ ℬ_f}. There it obeys the bound of its kind: |Φ_f| ≤ b_f for (B), (E, R), (Z); oscillation ≤ osc_f for (K); Re Φ_f ≤ C_ΨV°(ω) for (I). Moreover Φ_f(𝐡(P′; s, ζ)) = F_f(P′; s, ζ).

*Why this is what Theorem V′ proves.* Steps 3–7 use the shift only through the bound (5.1) of NL1-L, n_b(𝐡) ≤ A_Ve^{−μd_+(b,𝒮)}, and only at the bonds of ℬ_f: Lemma 4 bounds the pinned shift at b by the shift on nb(y(b)) (ST1 L281) and the levelling quantity ε̂_y by the shift on Rd(y) (ST1 L241). Levelling is forced on all of 𝒜_f by (V3), so the pinned shift is holomorphic there (ST1 L253, L286). Lemma Q and (V1)–(V2) give the pinned norm < r_*/2, Lemma 11 gives inclusion, and f is holomorphic on the target domain by CI before σ. None of these steps uses that h is a response. What I add is the observation that they apply to an arbitrary shift with the same bound.

**Lemma 6.1 (two-sided form).** [P from (Adm), Lemma 3.7] Let 𝒪_f := {g : n_b(g) < A_b/4 for b ∈ ℬ_f} and h₀ := 𝐡₀. Then n_b(h₀) ≤ A_b/3, h₀ + 𝒪_f ⊂ 𝒜_f, and |Φ_f − Φ_f(h₀)| ≤ ω̃_f on h₀ + 𝒪_f, where ω̃_f := 2b_f for (B), (E, R), (Z); ω̃_f := osc_f for (K); ω̃_f := 2(C_ΨV°(ω) − f₀) for (I).

*Proof.* By (4.1), n_b(h₀) ≤ C_DE_κ̄C_Aδ_src e^{−μd_+(b,𝒮)} ≤ A_b/3. So for g ∈ 𝒪_f, n_b(h₀ + g) < A_b/3 + A_b/4 < A_b, and h₀ + 𝒪_f ⊂ 𝒜_f. For (B), (E, R), (Z), |Φ_f(h) − Φ_f(h₀)| ≤ 2b_f. For (K) both values are values of f on its domain, so their difference is at most osc_f (NL1-L L481). For (I), let g ∈ 𝒪_f and φ(z) := Φ_f(h₀ + zg) for |z| < 2. Since n_b(h₀ + zg) < A_b/3 + A_b/2 < A_b, φ is holomorphic with Re φ ≤ C_ΨV°, and φ(0) = f₀ is real (NL1-L L487). Lemma 3.7 gives |φ(1) − φ(0)| ≤ 2(C_ΨV° − f₀). ∎

### 6.2 The multi-point bound (TD′)

For f ∈ 𝔉^{ex} (CI Definition 5.1) and ∅ ≠ W ⊂ 𝒞_Λ, f_W is the cube-Möbius piece (CI (5.5)): f_W(P′; ζ) := Σ_{W′⊂W}(−1)^{|W∖W′|}F_f(P′; 𝟏, ζ𝟏_{W′}).

Put a := ½log(1/q) = ½log((e^{κ̄} − 1)/6400), K₁ := max{1, 4A′_row/A_V}, and β_c(ζ) := K₁·2|ζ|_c/ϱ.

**Proposition 6.2 ((TD′)).** [P from Corollary 4.2, Lemma 5.1, Lemma 6.1] Assume a ≥ 12 and β_c(ζ) < δ for c ∈ W. Then for every f ∈ 𝔉^{ex}, every P′ ∈ 𝒪_σ and every ζ ∈ 𝔻_ϱ (in particular every real B in the box),

  |f_W(P′; ζ)| ≤ ω̃_f ∏_{c∈W}(2β_c(ζ)/δ)·e^{−(a−6)MST_{X(f)}(W∪∗)}.   (TD′)

*Proof.* By Corollary 4.2 and Lemma 3.2, for b ∈ ℬ_f,

  n_b(𝐆_U(ζ)) ≤ A′_row e^{−μd_+(b,𝒮)}∏_{c∈U}(2|ζ|_c/ϱ)q^{MST(U∪{Δ_b})/2} ≤ (A_b/4)∏_{c∈U}β_c(ζ)·e^{−aMST(U∪{Δ_b})},

using 4A′_row/A_V ≤ K₁ ≤ K₁^{|U|}. By Möbius inversion and 𝐆(𝟏, 0) = 0, 𝐆(𝟏, ζ𝟏_{W′}) = Σ_{∅≠U⊂W′}𝐆_U(ζ) for W′ ⊂ W, since 𝐆_U(ζ) depends on ζ only through ζ𝟏_U. So F_f(P′; 𝟏, ζ𝟏_{W′}) = Φ_f(𝐡₀ + Σ_{U⊂W}(𝟏_{W′})^U𝐆_U(ζ)) = F(𝟏_{W′}) in the notation of Lemma 5.1, with 𝐠_U := 𝐆_U(ζ), Φ := Φ_f, ω := ω̃_f (Lemma 6.1). Lemma 5.1 gives (TD′). ∎

---

## 7. Lemma TD as stated is not implied by its inputs

Lemma TD (CI L472–478) asks: "There are a rate λ_T ≥ λ_V and an amplitude a^{ex}, with a^{ex} → 0 as γ → 0 after M, and for every main-step input structure σ and every P′ ∈ 𝒪_σ an exact local decomposition ... such that for every real B in the box on W, |V^{ex}(W; P′, B)| ≤ a^{ex}e^{−λ_Td_f(W)}." The rate must also fit (UM19), λ_T − λ₀ ≥ Θ/L + σ₀, since the exempt potentials enter the same hull payment as the others (CI L341, L391). By IN1 (24) (IN1 L356), Θ = C_h^{UM}{3 + c_ℓ[(1 + 4β_s)κ + g_*]}. Here C_h^{UM} ≥ 1 (a single fine cube has a nonempty collar, so (UM7) at d_f = 0 forces C_h ≥ 1), and c_ℓ ≥ 5 ((UM17) ℓ(Z) ≤ c_ℓN with ℓ(Z) = d_c(Z) + 5 ≥ 5 at N = 1). So every admissible rate has

  λ_T > Θ/L > 5κ/L.   (7.1)

**Proposition 7.1 (counterexample at the level of the inputs).** [CE] The inputs from which Lemma TD is to be derived are: the class bound (R23) for exempt boundary terms (SA L6199–6203; (B-in), NL1-L L473); the presentation (L1)–(L6) of Theorem V′; the geometry (G-gap), (G-isl), (G-sep). These inputs admit, for every γ, a main-step structure, a term f ∈ 𝔉^{ex} and a two-cube set W = {c₁, c₂} ⊂ 𝒞_Λ for which (TD) fails for every rate λ_T with

  λ_T > κs/(s + D),

where s ≥ Ř_{i−1} is the gap between consecutive hulls and D ≤ C₀LŘ_i − 1 their side. With s = Ř_{i−1} and D = C₀LŘ_i − 1 this threshold is κ/(1 + C₀L·Ř_i/Ř_{i−1}·(1 − o(1))), which is below κ/L for γ small, because Ř_i/Ř_{i−1} → 1 (bounded adjacent frame increments, ST1 L126, and Ř ≍ (log θ)^r) and C₀ ≥ 1. By (7.1) no admissible rate survives.

*Construction.* Take m standing-island hulls H₁, …, H_m, boxes of side D, placed along one coordinate axis with consecutive gaps s, and two gas cubes c₁, c₂ on the axis at d_c = G from H₁ and from H_m. (G-isl) allows each hull (one island in a cube of C₀ level-i cells), (G-sep) allows the gaps, and (G-gap) allows c₁, c₂ in the gas. The torus is taken large enough. Let T be the set of cubes on the axis outside ∪H_k between c₁ and c₂, and X_f := T ∪ ∪_kH_k ∪ {c₁, c₂}, which is connected. Its exempt tree length is d^♮(X_f) ≤ 2G + (m − 1)s + 2. Put ω := 2𝖡e^{−κd^♮(X_f)}, choose free bonds b_k ∈ c_k, and define

  F_f(P′; s, ζ) := (ω/4)·(ζ_{b₁,1}/R)(ζ_{b₂,1}/R).

It satisfies (L1)–(L6) of PAN L134–141 with X_f and R_f = R: it is holomorphic; it reads ζ only on bonds of X_f; it is real at real arguments; it vanishes at ζ = 0; and |F_f| ≤ ω/4 ≤ ½ω on 𝕊_{X_f} × 𝔻_R. Its size is the (B-in) size 2𝖡e^{−κd^♮}. All other exempt terms are set to zero.

*Failure.* For W = {c₁, c₂}, V^{ex}(W) = f_W = F_f(𝟏, B), the only cross term. At B(b_k) = (𝔟/2, 0, 0), |V^{ex}(W)| = (ω/16)(𝔟/R)². But d_f(W) = d_c(c₁, c₂) = 2G + (m − 1)s + mD + 1. So (TD) requires

  (𝖡/8)(𝔟/R)²e^{−κ(2G+(m−1)s+2)} ≤ a^{ex}e^{−λ_T(2G+(m−1)s+mD+1)}  for all m.

At fixed γ, let m → ∞. The inequality forces λ_T(s + D) ≤ κs. ∎

*What the counterexample shows, and what it does not.* It shows that Lemma TD with the gas length d_f cannot be derived from the class bounds and the interface: (R23) "asserts no decay across an exempt island" (SA L6198), while d_f charges every island crossing in full, and one island crossing is a factor C₀L longer than the gap that (R23) charges. It does not show that the actual exempt terms of a Yang–Mills history violate (TD): I have not exhibited an actual boundary term of this shape. The same obstruction is in SA's own chapter: SA's (UM1) uses d_f (SA L14295–14306), and SA's class allows exactly these boundary terms.

*The repair.* The gas does not need d_f. It needs, for each potential type, a length with three properties: the collar count (UM7), the entropy (UM9)–(UM10), and the decay (UM1). §8 proves (UM1) for the exempt type with the island-exempt length ℓ^♮. §9 proves (UM7) and (UM9) for ℓ^♮, and rebuilds the gas with polymers linked through exempt potentials.

---

## 8. Lemma TD^♮: the exempt potentials in the island-exempt length

### 8.1 Inputs for the exempt kinds

For f ∈ 𝔉^{ex} let X_f be its presentation set (NL1-L §7.5–§7.7: X_f := X^↑ ∪ T ∪ ∪𝖥 for (B), (K); X_f := X^↑ for (I)), and d^♮_f its exempt length: d^♮_f := d^♮_j(𝒮; X) for (B) and (K); d^♮_f := 0 for (I); d^♮_f := d_j(X) for exempt (E, R) and for the drop-out factors (Z), whose class norms carry full decay. Let ω̂_f be the amplitude with ω̃_f ≤ ω̂_fe^{−κd^♮_f}: ω̂_f := 4𝖡 for (B); 2C_Kp₀(g_{j_f})² for (K); 2(C_ΨV° − f₀) ≤ 2C_I(M)ℓ^{τ_I} for (I) (NL1-L L487); 2b_fe^{κd^♮_f} for (E, R), (Z).

- **(Proj)** [R: SA L6191–6198, projected to level-(i − 1) cubes; owner NL1(1)/LF1]. π(X_f) is connected in Γ^♮, and St^♮(X_f) ≤ C_pr(1 + d^♮_f), with C_pr a geometric constant independent of L, M, κ, κ̄. *Reason.* SA's minimising tree meets each cube of X outside ∪𝖥 and each member of 𝖥. Members of 𝖥 are level-j hulls of standing islands of the current label. A level-j hull lies in the level-(i − 1) hull of the same island (coarser cells, aligned geometry), hence in a hub. A lattice tree of length ℓ in level-j units meets at most 16(ℓ/M + 1) level-(i − 1) cubes of side ≥ M. The carriers of X^↑ add a bounded number of layers, absorbed by the two-layer hubs and a fixed factor. For (I), X^↑ = X^~ ⊂ H̃ (the read set is the hull plus one layer, PAN L165), so St^♮(X_f) = 0. For exempt (E, R) and (Z), X_f is connected with |X_f| ≤ 1 + d_j(X) up to the same projection factor.
- **(EX-meet)** [CI Definition 5.1]. X_f meets 𝒵 or ∪_HH̃.
- **(N^{ex})** [I: (N-B), (N-K), (L-I), (L-Z), (L-reg) of PAN L147–158, restricted to 𝔉^{ex}; owners NL1(1), NL1(3), LF1(4)]. N^{ex} := sup_{Δ∈𝒞}Σ_{f∈𝔉^{ex}: X(f)∋Δ}ω̂_fe^{−(κ/2)d^♮_f} ≤ C_{ex}(M)ℓ^{τ_{ex}}, with C_{ex}(M) fixed after M and before γ and τ_{ex} a fixed exponent. For (I): a cube lies in at most one hub (distinct hubs are disjoint), so the island part is at most 2C_I(M)ℓ^{τ_I}.

### 8.2 Two geometric lemmas

**Lemma 8.1 (spanning W through an exempt support).** [P] For f ∈ 𝔉^{ex} and ∅ ≠ W ⊂ 𝒞_Λ,

  ℓ^♮(W) ≤ MST_{X(f)}(W ∪ ∗) + St^♮(X_f).

*Proof.* Let Q be the subgraph of Lemma 3.4(c) for X = X(f), with at most MST_{X(f)}(W ∪ ∗) edges, and τ_f a tree in Γ^♮ with St^♮(X_f) edges whose vertex set contains π(X_f). The image π(Q) is a subgraph of Γ^♮ with at most as many edges as Q (an edge inside a hub disappears, an edge into a hub becomes a cube–hub edge). In π(Q) every cube of W is joined to a vertex of π(X(f)) ⊂ π(X_f) ⊂ V(τ_f). So π(Q) ∪ τ_f is connected and contains π(W) = W. A spanning tree of it has at most MST_{X(f)}(W∪∗) + St^♮(X_f) edges. ∎

**Lemma 8.2 (the gap is paid).** [P from (G-gap), (EX-meet)] For f ∈ 𝔉^{ex} and ∅ ≠ W ⊂ 𝒞_Λ,

  MST_{X(f)}(W ∪ ∗) + St^♮(X_f) ≥ G₀ − 1.

*Proof.* In the connected graph π(Q) ∪ τ_f of Lemma 8.1, take c ∈ W and, by (EX-meet), a vertex z ∈ π(X_f) that is a hub or a cube of 𝒵. Follow a path from c to z, and stop at the first vertex that is a hub or a cube of 𝒵. Up to that vertex the path uses only cube vertices, so it is a cube-graph path. It ends at a cube of 𝒵 or at a cube at d_c = 1 from a hub. Its length is at least min{d_c(c, 𝒵), d_c(c, ∪H̃) − 1} ≥ G₀ − 1. ∎

### 8.3 The statement and the proof

**Definition 8.3.** The exempt potential is CI's cube-Möbius form (5.5): for ∅ ≠ W ⊂ 𝒞_Λ, V^{ex}(W; P′, B) := Σ_{f∈𝔉^{ex}}f_W(P′; B). CI §5.7 (CI L312) proves: Σ_{W}V^{ex}(W) = Σ_{f∈𝔉^{ex}}[F_f(P′; 𝟏, B) − f₀(P′)] exactly; each V^{ex}(W) reads B only on the bonds of I in W; it is holomorphic in (A′, 𝐉′) on 𝒪_σ(U) and real at real arguments. (The sum over f is finite in finite volume.)

**Theorem 8.4 (Lemma TD^♮).** [P from Proposition 6.2, Lemmas 8.1–8.2, (Proj), (EX-meet), (N^{ex})] Let λ_T := λ_V, and assume

  λ_V ≤ κ/(4C_pr),  a − 6 ≥ λ_V + 12,  β_c ≤ β^{max} := K₁·2𝔟/ϱ < δ/2.   (8.1)

Then for every σ, P′ ∈ 𝒪_σ, ∅ ≠ W ⊂ 𝒞_Λ and B in the box on W,

  |V^{ex}(W; P′, B)| ≤ a^{ex}e^{−λ_Vℓ^♮(W)},  a^{ex} := 2e^{κ/4}N^{ex}ϑe^{−ν(G₀−1−C_pr)},   (TD^♮)

with ϑ := 2β^{max}/δ ≤ 1 and ν := min{κ/(8C_pr), (a − 6 − λ_V)/2}. Moreover a^{ex} → 0 as γ → 0 after M and κ̄.

*Proof.* Fix W and f ∈ 𝔉^{ex}. Write 𝔪_f := MST_{X(f)}(W ∪ ∗) and a′ := a − 6. By Proposition 6.2 and β_c ≤ β^{max}, |f_W| ≤ ω̂_fe^{−κd^♮_f}ϑ^{|W|}e^{−a′𝔪_f}. By Lemma 8.1 and (Proj), ℓ^♮(W) ≤ 𝔪_f + C_pr(1 + d^♮_f). Hence, using λ_VC_pr ≤ κ/4,

  e^{λ_Vℓ^♮(W)}|f_W| ≤ ω̂_fϑ^{|W|}e^{κ/4}·e^{−(3κ/4)d^♮_f − (a′−λ_V)𝔪_f}.

Split (3κ/4)d^♮_f = (κ/2)d^♮_f + (κ/4)d^♮_f and (a′ − λ_V)𝔪_f = ½(a′ − λ_V)𝔪_f + ½(a′ − λ_V)𝔪_f. By Lemma 8.2 and (Proj), 𝔪_f + C_prd^♮_f ≥ G₀ − 1 − C_pr. Since κ/4 ≥ νC_pr and ½(a′ − λ_V) ≥ ν,

  (κ/4)d^♮_f + ½(a′ − λ_V)𝔪_f ≥ ν(C_prd^♮_f + 𝔪_f) ≥ ν(G₀ − 1 − C_pr).

So e^{λ_Vℓ^♮(W)}|f_W| ≤ ϑe^{κ/4}e^{−ν(G₀−1−C_pr)}·ω̂_fe^{−(κ/2)d^♮_f}·e^{−½(a′−λ_V)𝔪_f} (ϑ ≤ 1, |W| ≥ 1).

*Sum over f.* Fix c₀ ∈ W. By Lemma 3.4(b), 𝔪_f ≥ d_c(c₀, X(f)) = d_c(c₀, Δ_f) for a cube Δ_f ∈ X(f) nearest to c₀. Charge f to Δ_f. Then

  Σ_{f∈𝔉^{ex}}ω̂_fe^{−(κ/2)d^♮_f}e^{−½(a′−λ_V)𝔪_f} ≤ Σ_{Δ∈𝒞}e^{−½(a′−λ_V)d_c(c₀,Δ)}Σ_{f: X(f)∋Δ}ω̂_fe^{−(κ/2)d^♮_f} ≤ S(6)N^{ex} ≤ 2N^{ex},

since ½(a′ − λ_V) ≥ 6 by (8.1). Multiply.

*Size.* N^{ex} ≤ C_{ex}(M)ℓ^{τ_{ex}} is polylogarithmic. ν is fixed after κ̄ and positive. G₀ − 1 − C_pr ≥ 10LŘ_i − 3 − C_pr with Ř_i ≥ (ℓ − 1)^r, r ≥ 2 (PAN L395). So e^{−ν(G₀−1−C_pr)} beats every power of ℓ. Also ϑ = 16e·K₁·2𝔟/ϱ ≤ C(κ̄)𝔟/R = C(κ̄)A₁ℓ^{𝔭₀−q} → 0. Here ϱ ≍ e^{−Cκ̄}/g, and K₁ ≤ C(κ̄)/(gℓ^q) because A_V ≥ C_DE_κ̄C_Ac_Tge^{κ̄}R_V. Hence a^{ex} → 0 as γ → 0, after M and κ̄. ∎

*The three conditions (8.1).* The first is a ceiling on λ_V inside IN1's window. It requires the window amendment of §11, since IN1's upper endpoint is κ/(2C_h^{WF}) − ε_rate, not κ/(4C_pr). The second is the floor log(e^{κ̄} − 1) ≥ 2λ_V + 36 + log 6400 on κ̄, admissible because κ̄ is chosen after λ_V (IN1 L360). The third is a ceiling on γ after κ̄.

---

## 9. Theorem UM^♮(P′): the regular gas with island-exempt potentials

This section rebuilds CI §6 (SA L14276–14811 at P′) with one change: the exempt potentials have the length ℓ^♮, so their collars can be disconnected. I write only the steps that change and cite CI §6.3 for those that do not.

### 9.1 Potential types and lengths

The potential types are those of CI §6.1: (W), (cl), (ins), (ex). Each type has its length ℓ_type: ℓ_W = ℓ_cl = ℓ_ins := d_f, on connected domains (CI Definition 5.2, Lemma 5.4); ℓ_ex := ℓ^♮, on domains W ⊂ 𝒞_Λ. **[R: (Ins-conn) the inserted potentials of SC1 have *-connected domains; CI needs zero insertion, CI L302]**

**(A1^♮)** |V(Y; P′, B)| ≤ a_Ye^{−λ_Vℓ_type(Y)} on the box, a := Σ_types sup_Ye^{λ_Vℓ_type(Y)}sup_B|V(Y)|. For (W), (cl): CI Lemma 5.4 and Proposition 5.3. For (ex): Theorem 8.4. For (ins): (Ins).

Collars. A domain Y of type (W), (cl) or (ins) is *-connected, so its collar Y^♯ is *-connected. **[R: (R-wall) SA's "wall-connected" (SA L14365) is read as *-connected for coarse cubes, which is the reading under which SA's factorisation (SA L14370) holds for the collars of *-connected domains]** An exempt domain W can have a disconnected collar.

### 9.2 The counts

**Lemma 9.1 ((UM7^♮)).** [P from (UM7), Lemma 3.8, (Ř)] For ∅ ≠ W ⊂ 𝒞_Λ, #W^♯ ≤ 2C_h(1 + ℓ^♮(W)/L).

*Proof.* Let τ be a minimal Γ^♮-tree for W, with n = ℓ^♮(W) edges, and C₁, …, C_m its cube components (Lemma 3.8). W ⊂ ∪_kV(C_k). The collar preserves unions (SA L14347), and (UM7) applies to V(C_k) with d_f(V(C_k)) ≤ |E(C_k)|. So #W^♯ ≤ Σ_kC_h(1 + |E(C_k)|/L) ≤ C_h(m + n/L) ≤ C_h(1 + n/r_H + n/L) ≤ C_h(1 + 2n/L), using r_H ≥ L. ∎

**Lemma 9.2 ((UM9^♮), (UM10^♮)).** [P from Lemmas 3.8, (Ř)] Put κ_f^♮ := log(4·82²·e). For ξ ≥ κ_f^♮,

  S^♮_ξ := sup_{q∈𝒞_Λ}Σ_{W⊂𝒞_Λ: W∋q}e^{−ξℓ^♮(W)} ≤ 4,  and  Σ_{W⊂𝒞_Λ: W^♯⊂Z}e^{−ξℓ^♮(W)} ≤ c_fL⁴S^♮_ξ·#Z.

*Proof.* Encode W ∋ q by a minimal Γ^♮-tree τ with n = ℓ^♮(W) edges, rooted at q, together with the flags that mark which cube vertices lie in W (at most 2^{n+1}). Encode τ by its depth-first walk of 2n steps. From a cube vertex there are at most 82 options (80 cube children, at most one hub, or back). From a hub there are at most (D_H + 2)⁴ + 1 ≤ (D_H + 3)⁴ options, and the number of departures from hubs equals Σ_{hubs}deg ≤ n/r_H (Lemma 3.8). So the number of trees is at most 82^{2n}(D_H + 3)^{4n/r_H} ≤ 82^{2n}e^n by (Ř). Hence S^♮_ξ ≤ Σ_{n≥0}2^{n+1}82^{2n}e^ne^{−ξn} ≤ 2Σ_n4^{−n} < 4. For the second bound, charge W to one of its cubes; the cubes of W lie in the fine cubes of Z, at most c_fL⁴#Z of them. ∎

The counts (UM8), (UM11) and the local dimension (UM5) are unchanged (CI §6.3 Step 1, Proposition 4.2(iv)), with C_h replaced by C_h^♮ := 2C_h in (UM8).

### 9.3 Linked polymers

**Definition 9.3.** A *polymer* is a nonempty set Z of coarse cubes, not necessarily wall-connected. For an index ι = (𝐃, P₀) with Z₀^♯(ι) ⊂ Z, the *link graph* has the wall-components of Z as vertices, with an edge between two of them when some Y ∈ 𝐃 has Y^♯ meeting both. (Z, ι) is *linked* if the link graph is connected. Put

  H^♮(Z; P′) := Σ_{ι≠(∅,∅): Z₀^♯(ι)⊂Z, (Z,ι) linked}T(Z, ι; P′),

with T as in CI (UM3). Two polymers are *compatible* if no cube of one equals or is *-adjacent to a cube of the other.

The *link length* Λ^♮(Z) is 0 if Z is wall-connected. Otherwise it is the least Σ_{W∈𝐃_l}ℓ^♮(W) over finite families 𝐃_l of exempt domains W ⊂ 𝒞_Λ with W^♯ ⊂ Z whose link graph on the wall-components of Z is connected, and ∞ if there is none. In a linked (Z, ι) only exempt domains link distinct components (§9.1), so Σ_{Y∈𝐃 exempt}ℓ^♮(Y) ≥ Λ^♮(Z).

**(I-3w)** [I: SA L14370–14371 and the structural identities (I-3) of the actual gas, IN1 L66, status [SS]]. If Z = Z₁ ⊔ Z₂ with Z₁, Z₂ compatible, and ι = ι₁ ⊔ ι₂ with Z₀^♯(ι_k) ⊂ Z_k, then T(Z, ι) = T(Z₁, ι₁)T(Z₂, ι₂). (At s = 0 between Z₁ and Z₂ the decoupled functional splits: IN1 L300, "Zero walls separate this covariance into blocks"; the integrand F_ι is the product of F_{ι₁} and F_{ι₂}, which read disjoint bond sets; the s-derivatives act on one factor each.)

**Lemma 9.4 (factorisation over linked polymers).** [P from (I-3w)] At P′, the normalised gas equals Σ_{n≥0}Σ_{{Z₁,…,Z_n} pairwise compatible}∏_{g=1}^nH^♮(Z_g; P′).

*Proof.* By SA's Mayer and decoupling expansion (CI (UM2)–(UM3); SA L14324–14369), the normalised gas is Σ_ιΣ_{Z⊃Z₀^♯(ι)}T(Z, ι), where Z runs over all sets of coarse cubes (not only wall-connected ones) and T(∅, (∅, ∅)) = 1, T(Z, (∅, ∅)) = 0 for Z ≠ ∅ (CI L405: 𝒥[1] = 1). Fix Z ≠ ∅ and ι. The components of the link graph give a partition of the wall-components of Z into groups Z_g. Every element of ι has its collar in one group: a domain of type (W), (cl), (ins) or a failed bond has a *-connected collar, inside one wall-component; an exempt domain's collar meets only linked components. Let ι_g be the elements with collar in Z_g. If some group has ι_g = ∅, T(Z, ι) = 0 by (I-3w) and T(Z_g, ∅) = 0. Otherwise T(Z, ι) = ∏_gT(Z_g, ι_g) by (I-3w), and each (Z_g, ι_g) is linked. Conversely, a family of pairwise compatible polymers with linked indices determines Z = ∪Z_g, its wall-components (those of the Z_g) and ι = ∪ι_g. This is a bijection between pairs (Z, ι) with T ≠ 0 and families {(Z_g, ι_g)} of pairwise compatible linked pairs. Sum. ∎

### 9.4 The activity bound

Let (A2) be CI's (UM4)–(UM6) at P′ (CI Proposition 4.2), unchanged. Let σ₁ > max{κ_f, κ_f^♮}, σ₂ > 0, and

  σ₀ := σ₁ + σ₂,  λ_V − λ₀ ≥ Θ^♮/L + σ₀,  log(e^{κ̄} − 1) ≥ Θ^♮,  Θ^♮ := C_h^♮(1 + K_*^♮),   (UM19^♮)

with K_*^♮ fixed in (9.3) below.

**Proposition 9.5.** [P, as CI §6.3 Steps 2–7 with the changes stated] Under (A1^♮), (A2), (UM19^♮), and a ≤ a^♮_* := min{W₀/2, 1/(4e^{Θ^♮}A^♮_a)}, p_⋆ ≤ 1/(4e^{Θ^♮}), with A^♮_a := 2c_fL⁴max{S_{σ₁}, S^♮_{σ₁}}/W₀, for every polymer Z with N := #Z and every P′ ∈ 𝒪_σ,

  |H^♮(Z; P′)| ≤ τe^{−(K_*^♮−2)N}e^{−σ₂Λ^♮(Z)},  τ := e^{Θ^♮}[A^♮_aa + p_⋆] ≤ ½.   (9.1)

*Proof.* Steps 2–4 of CI §6.3 are unchanged, with ℛ_Y := (W₀/a)e^{(λ_V−λ₀)ℓ_type(Y)} and (UM10^♮) in (UM13); they do not use that Z is wall-connected. (The constant P of IN1 (22) absorbs the factor max{S_{λ₀}, S^♮_{λ₀}} ≤ 4; W₀ is then determined, IN1 L340–345.) They give (UM16):

  |T(Z, ι)| ≤ e^{C₀^{UM}N}(2a/W₀)^{|𝐃|}e^{−(λ_V−λ₀)Σ_{Y∈𝐃}ℓ_type(Y)}p^{|P₀|}(e^{κ̄} − 1)^{−h}.

Step 5: by (UM8) with C_h^♮ and Lemma 9.1, (C₀^{UM} + K_*^♮)N ≤ Θ^♮[|𝐃| + L^{−1}Σ_Yℓ_type(Y) + |P₀| + h]. With (UM19^♮),

  |T(Z, ι)| ≤ e^{−K_*^♮N}∏_{Y∈𝐃}[(2a/W₀)e^{Θ^♮}e^{−σ₀ℓ_type(Y)}]·∏_{P₀}[pe^{Θ^♮}].

For linked (Z, ι), Σ_{Y∈𝐃}ℓ_type(Y) ≥ Λ^♮(Z), so the product over 𝐃 is at most e^{−σ₂Λ^♮(Z)}∏_Yũ_Y with ũ_Y := (2a/W₀)e^{Θ^♮}e^{−σ₁ℓ_type(Y)}. Step 6: drop the linkedness and the constraint P₀ ∩ Y₀ = ∅, which only enlarges the nonnegative sum: Σ_ι ≤ e^{−σ₂Λ^♮}(∏_{Y∈𝒴(Z)}(1 + ũ_Y)∏_{b^♯⊂Z}(1 + q) − 1) ≤ e^{−σ₂Λ^♮}(e^{τN} − 1), with Σ_Yũ_Y ≤ A^♮_aae^{Θ^♮}N by (UM10) and (UM10^♮). Step 7: e^{τN} − 1 ≤ τe^{2N}. And τ ≤ ½ by the ceilings. ∎

### 9.5 The coarse length and the counting of linked polymers

Coarse hubs: for H ∈ 𝖧, H^c is the set of coarse cubes meeting H. Γ^{♮c} is the coarse cube graph with each H^c contracted to a vertex. For a set Z of coarse cubes, d^{♮c}(Z) is its Steiner length in Γ^{♮c}, and 𝓁(Z) := d^{♮c}(Z) + 5.

**Lemma 9.6 (coarse length of a linked polymer).** [P from Lemma 3.8, Lemma 9.1, (Ř), L ≥ 4] For every polymer Z with Λ^♮(Z) < ∞,

  d^{♮c}(Z) ≤ c^♮_1N + c^♮_2Λ^♮(Z)/L,  c^♮_1 := 257 + 2C_h,  c^♮_2 := 513 + 2C_h.

*Proof.* Let A₁, …, A_k be the wall-components and 𝐃_l a linking family attaining Λ^♮(Z); minimality gives |𝐃_l| ≤ k − 1 ≤ N. A spanning tree of each A_p has #A_p − 1 edges. For W ∈ 𝐃_l take a minimal Γ^♮-tree τ_W with n_W = ℓ^♮(W) edges and project it to Γ^{♮c}. Remove the hubs of τ_W. A cube component C with e_C edges has a closed depth-first walk of 2e_C steps; cut it into at most 2e_C/L + 1 pieces of at most L steps. Each piece lies in a fine ball of radius L, whose fine cubes lie in at most 4⁴ = 256 coarse cubes. Consecutive fine cubes lie in equal or *-adjacent coarse cubes. So the coarse cubes met by C form a *-connected set of at most 256(2e_C/L + 1) cubes. A fine cube at d_c ≤ 1 from H̃ is at fine distance ≤ 3 < L from H, so its coarse cube equals or is *-adjacent to a cube of H^c. So each hub edge of τ_W costs at most one coarse edge. With Lemma 3.8 (Σdeg ≤ n_W/r_H, number of components ≤ 1 + n_W/r_H) and r_H ≥ 257L, the projection of τ_W lies in a connected subgraph of Γ^{♮c} with at most 512n_W/L + 256(1 + n_W/r_H) + n_W/r_H ≤ 513n_W/L + 256 edges. W's collar meets r_W ≤ #W^♯ ≤ 2C_h(1 + n_W/L) components (Lemma 9.1), each joined to the projection by at most one coarse edge (a collar cube of W is a coarse cube within coarse distance 1 of the coarse cube of a cube of W). Summing: d^{♮c}(Z) ≤ N + Σ_{W∈𝐃_l}[(513 + 2C_h)n_W/L + 256 + 2C_h] ≤ (257 + 2C_h)N + (513 + 2C_h)Λ^♮(Z)/L. ∎

**Lemma 9.7 (counting linked polymers).** [P from Lemmas 3.1, 3.2, 3.9] Let α ≥ α₀ := log 12800 + 2592L⁴ and β ≥ β₀ := 13. Then

  sup_{q coarse}Σ_{Z∋q, Λ^♮(Z)<∞}e^{−α#Z − βΛ^♮(Z)} ≤ 1.

*Proof.* *A tree of links.* Let Z have wall-components A₁, …, A_k and let 𝐃_l attain Λ^♮(Z). For W ∈ 𝐃_l meeting components A_{p₁}, …, A_{p_r}, choose witnesses x_1, …, x_r ∈ W with N_f(x_j) meeting a coarse cube of A_{p_j}. A minimum spanning tree of {x_j} in dist_{Γ^♮} has weight ≤ 2ℓ^♮(W) (Lemma 3.2 in Γ^♮), and gives r − 1 links. The union over W ∈ 𝐃_l of these links connects the components. Choose a spanning tree 𝒯 of components. Each edge e ∈ 𝒯 carries witnesses x_e, y_e ∈ 𝒞_Λ with t_e := dist_{Γ^♮}(x_e, y_e) and Σ_{e∈𝒯}t_e ≤ 2Λ^♮(Z). So e^{−α#Z−βΛ^♮(Z)} ≤ ∏_pe^{−α#A_p}∏_{e∈𝒯}e^{−(β/2)t_e}.

*Enumeration.* Root 𝒯 at the component containing q. A rooted structure is a component A ∋ (root cube), and for each child an attachment (x, y, q″, child structure): x ∈ 𝒞_Λ with N_f(x) meeting a coarse cube of A (at most 81L⁴#A choices), y ∈ 𝒞_Λ at Γ^♮-distance t from x (weight Σ_ye^{−(β/2)t} ≤ 𝔈(β/2) ≤ 2 by Lemma 3.9, β/2 ≥ log(162e)), q″ a coarse cube meeting N_f(y) (at most 16 for L ≥ 3), and a rooted structure at q″. Let 𝔚_d be the supremum over root cubes of the total weight of rooted structures of depth ≤ d, with children unordered (a k-tuple divided by k!). Every linked Z with Λ^♮ < ∞ is counted at least once at some finite depth. 𝔚_0 ≤ sup_qΣ_{A∋q}e^{−α#A} ≤ Σ_n6400^{n−1}e^{−αn} ≤ 1. If 𝔚_d ≤ 1, then by Lemma 3.1

  𝔚_{d+1} ≤ sup_{q′}Σ_{A∋q′}e^{−α#A}Σ_k(1/k!)(81L⁴#A·2·16·𝔚_d)^k ≤ Σ_{n≥1}6400^{n−1}e^{−(α−2592L⁴)n} ≤ Σ_{n≥1}2^{−n} ≤ 1.

By induction 𝔚_d ≤ 1 for all d. ∎

### 9.6 The Kotecký–Preiss criterion and the logarithm

Fix the output rate μ (μ ≥ κ, as CI §10; μ := (1 + 4β_s)κ is admissible). Put

  K_*^♮ := 3 + (c^♮_1 + 5)μ + log 81 + α₀,  σ₂ := μc^♮_2/L + β₀,   (9.3)

and ŵ_Z := sup_{P′∈𝒪_σ}|H^♮(Z; P′)|e^{μ𝓁(Z)}.

**Theorem 9.8 (Theorem UM^♮(P′)).** [P, as an implication] Under the hypotheses of Proposition 9.5 with (9.3):

- (a) |H^♮(Z; P′)| ≤ τe^{−μ𝓁(Z)}e^{−(K_*^♮−2−μ(c^♮_1+5))#Z} for every polymer Z and P′ ∈ 𝒪_σ;
- (b) sup_qΣ_{Z∋q}ŵ_Ze^{#Z} ≤ τ/81;
- (c) (Kotecký–Preiss) Σ_{Z′≁Z}ŵ_{Z′}e^{#Z′} ≤ τ#Z ≤ #Z/2;
- (d) for the logarithms E(X; P′) of the connected-cluster expansion (CI (UM29), with polymers now linked), e^{μ𝓁(X)}|E(X; P′)| ≤ τ/81.

*Proof.* (a) By (9.1) and Lemma 9.6, μ𝓁(Z) ≤ μ(c^♮_1N + 5) + μc^♮_2Λ^♮/L, and N ≥ 1 gives 5μ ≤ 5μN. So |H^♮|e^{μ𝓁} ≤ τe^{−(K_*^♮−2−μ(c^♮_1+5))N}e^{−(σ₂−μc^♮_2/L)Λ^♮}, and σ₂ − μc^♮_2/L = β₀ ≥ 0. (b) By (a), ŵ_Ze^{#Z} ≤ τe^{−(K_*^♮−3−μ(c^♮_1+5))N}e^{−β₀Λ^♮} = (τ/81)e^{−α₀N−β₀Λ^♮(Z)} by (9.3). Lemma 9.7 gives (b). If Λ^♮(Z) = ∞, H^♮(Z) = 0 (no linked index exists). (c) A polymer incompatible with Z contains a coarse cube equal or *-adjacent to a cube of Z, at most 81#Z cubes. Use (b) and τ ≤ ½. (d) For an incompatibility-connected list Z₁, …, Z_n, d^{♮c}(∪Z_k) ≤ Σd^{♮c}(Z_k) + (n − 1) (join the trees by edges of length ≤ 1), so 𝓁(∪Z_k) ≤ Σ𝓁(Z_k) (UM28^♮). The rooted tree bound (SA L1305–1319), applied as in CI §6.3 Step 8 with the majorants ŵ and a(Z) := #Z, gives e^{μ𝓁(X)}|E(X)| ≤ Σ_{Z∋q}ŵ_Ze^{#Z} ≤ τ/81. There is no factor #X or volume. ∎

*Where P′ entered.* Only through (A1^♮) and (A2), as in CI §6. Lemmas 9.1–9.7 are statements about cubes.

**Theorem 9.9 (B1^♮(P′), B4^♮(P′)).** [P, as CI §7 with Theorem 9.8 in place of Theorem UM(P′)] (a) The criterion of Theorem 9.8(c) holds at every P′ ∈ 𝒪_σ with room factor 2, uniformly in |s_Δ| < e^{κ̄}. (b) The connected-cluster series converges absolutely and locally normally on 𝒪_σ(U). Each E(X; ·) is holomorphic there and real at real P′. Each H^♮(Z; ·) is a finite sum of T's, which are holomorphic by CI Lemma 4.3, Lemma 5.2(e) and Definition 8.3, and the series is dominated by the P′-independent majorant of (b), so Weierstrass applies. (c) Cauchy estimates for derivatives in (A′, 𝐉′) as in CI Theorem B1(P′)(c). (d) The bounds hold uniformly on SA's ordinary product box, under the same assumptions as CI Theorem B4(P′). ∎

---

## 10. CI in the remaining cases

### 10.1 What CI-ind needs at an exempt structure

NL1-L's Proposition CI-ind (NL1-L L516–522) reduces CI at σ to (CI-form) at σ, whose hypothesis (i) reads "every old factor of its integrand, as a function of the free fluctuation and switches, satisfies the conclusions of Theorem V′ at P′ with radius R". CI §0 (CI L41) already records that (i) is not enough for the exempt kinds, and §7 above shows why: no localisation built on a sup-norm presentation alone gives (UM1). Replace (i) by

- **(i′)** every old factor f of a kind other than (W) has the form F_f = Φ_f ∘ 𝐡 with Φ_f as in (Adm), and the response increment satisfies Corollary 4.2 at P′.

**Proposition 10.1 (CI-ind′).** [P, as NL1-L's proof with (i′)] Proposition CI-ind holds with (i′) in place of (i).

*Proof.* (i′) is supplied at P′ ∈ 𝒪_σ as follows. (Adm) needs ST1 hypothesis 4 for f, which CI-old gives (f is bounded on its chain domain), and hypotheses 1–3 and 5, which ST3 §6 supplies (ST3 L396–408), as in NL1-L's proof. Corollary 4.2 needs (DR-ζ), (DR-loc′) at P′ (DR is holomorphic in its complex input pair, ST1 L119) and the ceilings of Proposition S. The rest of NL1-L's proof is unchanged. ∎

### 10.2 The theorem

**Theorem 10.2 (CI(σ), all main-step structures).** [P, as a reduction] Let σ be a main-step structure of a finite history. Assume (CI-old); the hypotheses of NL1-L Theorem V′ at σ; the ceilings of CI Theorem CI(σ) and of (8.1), (Ř), Proposition S; the rate conditions (UM19^♮), (9.3) and the window amendment of §11; and the imports (Size), (W-in′), (Ins), (Ins-conn), (I-3), (I-3w), (R-wall), (Adm), (DR-loc′), (Proj), (N^{ex}), (Size-isl), (Loc-isl), (File^♮). Then CI holds for every activity formed at σ by the regular gas, with

  b_E(X) := (τ/81)e^{−μ𝓁(X)}

for the logarithms E(X) of Theorem 9.8(d), filed by the rule of §10.3.

*Proof.* By Proposition 10.1 it suffices to prove (CI-form) at σ with (i′). (F1^♮): Theorem 9.8, with (A1^♮) from CI Propositions 5.3, 5.4, (Ins) and Theorem 8.4 (here (i′) enters: Proposition 6.2 uses (Adm) and Corollary 4.2), and (A2) from CI Proposition 4.2. (F2^♮), (F3^♮): Theorem 9.9. Holomorphy, Borel dependence, reality and covariance as in CI Theorem CI(σ)'s proof. ∎

The island exponents at their formation are covered by CI Theorem CI(σ)(c), unchanged.

### 10.3 Filing the new logarithms

- If X meets the boundary of Λ_i^{pre} or a standing object, or if d^{♮c}(X) < d_c(X) (its shortest tree uses a hub), E(X) is a boundary term of origin "step". SA lists "a step remainder beside an island" among the origins (SA L6185–6188, as PAN L108 quotes them). Its bound is |E(X)| ≤ (τ/81)e^{−μ(d^{♮c}(X)+5)} ≤ 𝖡e^{−κd^♮_i(𝒮′;X)} once 𝖡 ≥ τ/81, by μ ≥ κ and (File^♮).
- Otherwise X is wall-connected with d^{♮c}(X) = d_c(X), and E(X) enters the new regular family as in CI §10 (CI L531).

**(File^♮)** [R: SA's label update at the main step; owner LF1]. Every hub H^c of σ lies inside a member of the exempt family of the output label 𝒮′ (the level-i hull of the same standing island), so d^♮_i(𝒮′; X) ≤ d^{♮c}(X). Under the units reading of §2 there is no extra factor. When an island is later healed, the terms filed beside it are re-filed by LF1's healing, like every existing boundary term exempted by that island (SA L17996–17997). That obligation is LF1's for all exempt boundary terms; this draft adds only new members to it.

No constant fixed before κ reads b_E: τ is a ceiling quantity, μ is after κ. This is CI's order clause as CI §1.4 restates it.

---

## 11. The order of constants, and the amendment of IN1's window

| Constant or condition | Where | Fixed at | Before κ? independent of M, κ̄? |
|---|---|---|---|
| C_D, μ, C_A | Theorem 4.1, Corollary 4.2 | ST1 row 2 | yes; yes |
| 6400, 16, 81, 256, 4·82²e, log(162e), 2592L⁴, 12800 | §3, §9 | geometric (with L) | yes; yes |
| C_h, c_f, c_ℓ, c_adj = 81, κ_f; C_pr | (UM7), §9; (Proj) | geometric | yes; yes |
| c^♮_1, c^♮_2, C_h^♮ = 2C_h, κ_f^♮ | Lemmas 9.1, 9.2, 9.6 | geometric | yes; yes |
| E_κ̄, s_D, A_row, A′_row, q, a = ½log(1/q) | §4 | after κ̄ | read only by floors on κ̄ and ceilings on γ |
| ϱ, K₁, β^{max}, ϑ | §4.2, §6.2, §8.3 | after κ̄, before γ | ceilings on γ |
| λ_V with λ₀ + σ₁ + σ₂ + Θ^♮/L ≤ λ_V ≤ min{κ/(2C_h^{WF}) − ε_rate, κ/(4C_pr), κ − 1} | (UM19^♮), (8.1) | after κ | **window amendment** below |
| μ ≥ κ; K_*^♮, σ₂ by (9.3); Θ^♮ = 2C_h(1 + K_*^♮) | §9.6 | after κ | read by nothing before κ |
| κ̄: log(e^{κ̄} − 1) ≥ max{Θ^♮, 2λ_V + 36 + log 6400, log 12801}; κ̄ ≥ λ_V + 2 | (UM19^♮), (8.1), Theorem 4.1 | floors on κ̄ | admissible (IN1 L360) |
| (Ř): r_H ≥ 257L, 4log(D_H + 3) ≤ r_H, 8log(D_H + 3) ≤ s₀ − 2 | §2 | ceiling on γ after L, C₀ | Ř_i → ∞ |
| β^{max} < δ/2, a^♮ ≤ a^♮_*, p_⋆ ≤ 1/(4e^{Θ^♮}), a^{ex} small | §8, §9 | ceilings on γ after M, κ̄ | each → 0 |
| N^{ex} | (N^{ex}) | after M, before γ | read only by a^{ex} |

**The window amendment** [design]. IN1's window (IN1 L356–358) has upper endpoint κ/(2C_h^{WF}) − ε_rate and row-2 floor L > 4C_h^{WF}C_h^{UM}c_ℓ(1 + 4β_s) (IN1 L228). Theorem UM^♮ needs:

1. the lower endpoint λ₀ + σ₁ + σ₂ + Θ^♮/L, whose slope in κ is [c^♮_2 + 2C_h(c^♮_1 + 5)](1 + 4β_s)/L when μ = (1 + 4β_s)κ, and whose κ-free part contains 2C_h(4 + log 81 + α₀)/L + β₀ with α₀ ≍ 2592L⁴;
2. the extra upper endpoint κ/(4C_pr), from (8.1).

So the window is nonempty when

  L > L₀^♮ := max{4C_h^{WF}, 8C_pr}·[c^♮_2 + 2C_h(c^♮_1 + 5)](1 + 4β_s)  and  κ ≥ κ₀^♮(L),

where κ₀^♮(L) makes the κ-free part of the lower endpoint smaller than the gap between the slopes. Both are admissible: L is chosen in row 2, before κ, and all the constants in L₀^♮ are geometric and independent of L; κ is chosen in row 7, after L. They change frozen IN1 row 2 (a larger floor on L) and add a floor on κ that depends on L. Because IN1 is frozen, this needs the lead's decision. Nothing else in IN1's order moves.

---

## 12. Status

### 12.1 Statements of this draft

| Statement | Where | Status |
|---|---|---|
| Lemmas 3.1–3.9 (animals, Steiner/MST, Bird's allocation, collapsed tree, tree sums, repeated Schwarz, Borel–Carathéodory, hub structure, Γ^♮ balls) | §3 | [P] |
| Theorem 4.1 ((DR-row), source form) | §4.1 | [P] from (DR-ζ), (DR-loc′) |
| Corollary 4.2 ((DR-row), main-step form) | §4.2 | [P] from Theorem 4.1's proof, (FL-main), (V6) |
| Order of the (DR-row) constants | §4.3 | [P]: the before-κ constants are C_D, μ, C_A and geometric numbers, independent of M, κ̄ |
| Lemma 5.1 (composition along a hull product), Corollary 5.2 (products) | §5 | [P] |
| Lemma 6.1 (two-sided form), Proposition 6.2 ((TD′)) | §6 | [P] from (Adm) |
| Proposition 7.1 (Lemma TD with d_f not implied by its inputs) | §7 | [CE] at the level of the inputs |
| Lemmas 8.1–8.2, Theorem 8.4 (Lemma TD^♮) | §8 | [P] from (Proj), (EX-meet), (N^{ex}) |
| Lemmas 9.1, 9.2, 9.4, 9.6, 9.7; Proposition 9.5; Theorems 9.8–9.9 (UM^♮, B1^♮, B4^♮) | §9 | [P], as implications from (I-3w), (R-wall), (Ins-conn) |
| Proposition 10.1 (CI-ind′), Theorem 10.2 (CI at all main-step structures) | §10 | [P], as a reduction |
| Window amendment | §11 | [design], needs the lead's decision (IN1 frozen) |

### 12.2 Imports and readings, with owners and status

| Item | Owner | Status there | Used in |
|---|---|---|---|
| DR on the full switch polydisc with (16), zero at zero switches | ST1 | declared supply, construction open (ST1 L842, L939) | §4 |
| (DR-ζ) | NL1-L/ST1 | reading of (16) (NL1-L L263) | §4 |
| (DR-loc′), stencil form of (DR-loc) | ST1 | (DR-loc) is a new statement (NL1-L L265–267); stencil form [R] here | §4 |
| (FL-main) | ST3 F8/F4 | supplied at main steps (NL1-L L255) | Corollary 4.2 |
| (Adm) | NL1-L | [R] of Theorem V′'s proof (§6.1) | §6 |
| Source norm is a row-wise maximum | ST1 | [R] | §4 |
| (Proj) | NL1(1)/LF1 | [R] of SA L6191–6198 | §8 |
| (N^{ex}): (N-B), (N-K), (L-I), (L-Z), (L-reg) | NL1(1), NL1(3), LF1(4) | PAN inputs (PAN L147–158); (L-reg) contains (OSF3) [SS] | §8 |
| (G-gap), (G-isl), (G-sep) | LF1(2) | PAN L163–165 | §2, §7, §8, §9 |
| (I-3), (I-3w) wall factorisation | NL1(1) | [SS] (IN1 L66; SA L14370) | Lemma 9.4 |
| (R-wall) wall-connected = *-connected | SA | [R] | §9 |
| (Ins), (Ins-conn) | SC1 | [O] through NL1 (AS L316); connectivity [R] | §9.1 (not needed at zero insertion) |
| (File^♮) | LF1 | [R] of the label update | §10.3 |
| Everything CI §12.2 lists | as there | as there | via CI §4–§7 |

### 12.3 The first remaining Outstanding statement

This draft contains no Outstanding statement of its own. Lemma TD in the form CI L472–478 states it, with the gas length d_f, is not implied by its inputs (Proposition 7.1). The form the gas needs, Lemma TD^♮ with the island-exempt length ℓ^♮, is proved (Theorem 8.4), and the gas is rebuilt for it (Theorem 9.8). CI then holds at every main-step structure as a reduction (Theorem 10.2).

The conclusions are conditional on §12.2. The first item there whose owner status is open is DR's actual decoupled construction (ST1 L939), which ST1 already lists. The new readings this draft creates are (DR-loc′), (Adm), (Proj) and (File^♮); each is a reading of an owner's text, flagged where it is stated. The window amendment of §11 is a design decision.

### 12.4 Checks this draft needs

1. Theorem 4.1, Steps 6–7: the constants 16 and 6400, the per-cube factor 4‖S_c‖/s_D, and the use of the stencil base B_b instead of a single cube.
2. Lemma 3.3 (Bird's allocation): the cut property, the layer cake, the injectivity of v ↦ C_v.
3. Lemma 5.1: that the room check needs only Σ_{c∈U}ℓ_c ≤ MST(U ∪ {Δ_b}) at each read, and that no factor of |X| enters.
4. (Adm): that Steps 3–7 of Theorem V′ use the shift only through n_b on ℬ_f.
5. Proposition 7.1: that the geometry (hull side C₀LŘ_i, gap Ř_{i−1}) is allowed by (G-isl), (G-sep), and the bound (7.1) on Θ/L.
6. Lemmas 3.8, 9.1, 9.2, 9.6: the hub bookkeeping under (Ř).
7. Lemma 9.4: the bijection between linked index pairs and compatible families, and the reading (R-wall).
8. Lemma 9.7: the tree-of-links construction (Σt_e ≤ 2Λ^♮) and the depth induction.
9. §11: the window amendment against IN1 L228 and L353–360.
