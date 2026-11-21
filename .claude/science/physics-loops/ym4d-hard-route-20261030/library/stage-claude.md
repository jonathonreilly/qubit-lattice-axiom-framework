lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T12:30Z

# stage-claude: hereditary holomorphic continuation for H-STAGE

Queue row 346 of `FINISH.md`. Pinned commit b977aba9d. Complete; the Result is §7.

Moves: the open lemma of FINISH row 335 (`stage.md`, AD-ST(2)), which sits inside H-STAGE, the first input of A10 (`port/p10-stability.md` §2) and `port-map.md` rows 5 (DOM) and 7 (FCON), on the T0 chain through A17.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, branch `claude/ym4d-hard-route` at b977aba9d. Research text, not an audit; grants no status. Written arguments only; source searches are navigation, not proof. No numeric job was run (none was needed), so the memory rule did not arise. Not yet checked by the other model.

Credit: Tadeusz Balaban for the stage theorem, CMP 122a (1.60)–(1.70), and the spaces of CMP 109, 119, 122a. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account and outline at commit `31a47c543775`; in particular for 5.2:cor-response-dilation and 4.26:lem-family-consumption, which this note finds to treat the open lemma. Codex for `stage.md` (AD-ST(2), Lemmas 1–2) and ST1.

## 1. Scope and sources

**Item.** Queue row 346, `stage-claude`: attack the open lemma of `stage.md`, AD-ST(2), the hereditary holomorphic continuation of the stage response into the old stage space. First run the consumer check of `l17c.md`.

**Read.** `stage.md` in full. `st1-r4.md` Theorem 14, Lemmas 7–8, Result. `dom.md`, `pda.md`, `open-core.md`: headings and Results. `l17c.md` §§1–2, 7, Result. `port/p10-stability.md` §2 (A10). Source lines read, by file (CA-I, CA-II, CA-III = the three `theorem_0_complete_account_raw_*.tex`; SA = `YM4_sketch_500.tex`; all at `31a47c543775`, fetched once into a scratch folder):

* CA-I 9800–9960 (layered spaces), 34040–34300 (small pairs), 48455–48540, 49490–49670 (supply scope, stage-space factors), 53625–53830 (stage geometry), 54200–54500 (recursion, required bound), 54860–55240 (stage theorem quoted, A10 and its proof, decay-rate remark), 56123–56340 (action domain), 104684–104925 (survivor block), 116525–116800 (regularity radius, recorded stage-construction bounds), 117492–117700 (family consumption), 118700–118800 (stage systems), 119813–119990 (inherited expansion), 120610–120800 (raised cubes), 128962–129160 (source inclusions).
* CA-II 2200–2370 (admitted inputs), 10602–10700 (response containment), 12900–13010 (two-slot preparation), 13860–14131 (all-blocks response dilation, with proof).
* CA-III 50630–50730 (inheritance theorem's containment step).
* `~/ym4d-papers/cmp109.txt` pp. 262–263 ((1.11)–(1.18)); `cmp119.txt` p. 261 ((2.34)–(2.39)).

Name searches for "bump lemma", "response-layer theorem", "second-slot lemma", "setting of the response map", "recursive (stage-)layer", "layer theorem" were run over CA-I/II/III, SA, `YM4_sketch_draft.tex`, `YM3/YM3_I.tex` and `YM3/YM3_II.tex` at the pin. §2.4 reports what they found.

**Kind of result.** A check of their proof (§2), then proof work on the inputs their proof cites but does not contain (§§3–5).

## 2. Consumer check (the `l17c.md` strategy)

### 2.1 Who reads H-STAGE, and what each reads

| Consumer | Source | What it reads from H-STAGE |
|---|---|---|
| A10 = 4.18:thm-preparatory-boundary | CA-I 54985–55192 | Representation (1.63); holomorphy and locality on Ũ^{(n+1)c,Σ}_k(X); ‖C‖ ≤ C_0 = c_G+1 with the rates a_m and (F_m); the cumulation clause 3(N_0+3)C_0; the split C_G + C_I with ϑ and K'_S(N_0+8)C_0ϑ ≤ 1; the per-cube inequality (A10.7) "≤ ϑ"; (K), (Q⁺), γ ≤ γ_0. |
| 4.18:rem-decay-rates | CA-I 55194–55225 | The rates a_m and the companion statements on level-m terms. |
| 4.18:thm-action-domain (iii) | CA-I 56123–56330 | Passes A10's (a)–(d) on; its γ_W includes the stage theorem's γ_0. |
| 4.6:rem-widened-support | CA-I 23092–23170 | (1.60)–(1.70) re-run on a wider support. Its own heading says "Proof outstanding". |
| 4.38:thm-torus-independence and the clause-(0) list | CA-I 3133, 3470, 58200–58215 | "the convergence and analytic extension of the expansions on the joined localization domains", cited from CMP 122a p. 192, (1.70), "printed without proof". |
| 4.28:prop-kernel-membership (V) | CA-I 145011 | The stage theorem's three smallness hypotheses on γ_0, at a replaced γ_0. |
| A17 (our port) REP-BOUNDARY, REP-STAGE, REP-INHERIT | `port/p10-stability.md` §4.2 | A10 through "stored domain ... in its kind's analyticity space" and the stage norms. |

Every consumer reads conclusions on the stage spaces, at the constants C_0, ϑ and the rates. No consumer reads the response map directly. The response admission is an input of the *proof* of H-STAGE.

### 2.2 No weaker proved version of H-STAGE exists

1. The account assumes H-STAGE (CA-I 54989–54998). Its central display (1.70), with the convergence on joined localization domains, is cited "as printed" and "printed without proof" in CMP 122a p. 192 (CA-I 3133, 3470, 58211).
2. The account's own stage route (Chapters 4.24–4.26, 5.2) does not supply a proved replacement. Its stage lemma "is not written out here; parts of its proof are printed below" (CA-I 118758–118760, Remark 4.26:lem-stage-expansion). The survivor-block theorem assumes "the normalisation lemma at the full stage and the fluctuation cluster expansion at the full stage" (CA-I 104740–104743, (h3)); these are H-STAGE's own lemmas. Its norm conversion is "Proof outstanding" (4.24:prop-norm-conversion, CA-I 106533), and so is its holonomy bound (4.24:prop-holonomy-bound, CA-I 107073). The arrest theorem is incomplete (CA-I 137628). Its constant is C_0^♯ = 3c_G + 1, not c_G + 1 (CA-I 104801, 104856).
3. ST1 is a different theorem (finite substitution, no Gaussian or cluster bound; `stage.md` §3).

So the literal `l17c.md` move (replace an open statement by a weaker proved one that every consumer accepts) is not available for H-STAGE. **Verdict on H-STAGE: no change.**

### 2.3 Who reads the open lemma AD-ST(2), and what that reader needs

AD-ST(2) is `stage.md`'s formulation of the substitution step inside the proof of H-STAGE. Its reader is the stage argument's bound on the interaction bracket 𝔎^{(n)} of (S2). The account records how the stage argument reads an old term: its fluctuation dependence "is controlled by the Cauchy estimate of the stage argument" (CA-I 54970–54972), and an old term of size τ contributes τ·ϑ, times K_S e^{C_2κ_1} 6^d, to the local sums (CA-I 54976–54984, 4.18:rem-extra-term). So the reader needs the fluctuation dependence of an old term of size B to be at most a constant times ϑB.

**Lemma A (radius two gives no smallness).** Let f be holomorphic on |z| < ρ with |f| ≤ B there. Then |f(1) − f(0)| ≤ 2B/ρ. For ρ = 2 this gives only B, and f(z) = Bz/2 attains B/2.

*Proof.* Put g = (f − f(0))/(2B). Then g is holomorphic on |z| < ρ, g(0) = 0 and |g| ≤ 1. Schwarz's lemma applied to g(ρw), |w| < 1, gives |g(z)| ≤ |z|/ρ. At z = 1 this is |f(1) − f(0)| ≤ 2B/ρ. For f(z) = Bz/2 on |z| < 2, |f| < B and f(1) − f(0) = B/2. ∎

Hence the reader needs AD-ST(ρ) with ρ ≥ 2/(c ϑ) for the stage argument's fixed constant c, that is, a z-disc of radius of order ϑ^{-1} ∝ (log g_k^{-2})^{q_*−p_1}. AD-ST(2) is too weak for its only reader. `stage.md` §5 already calls radius two "a deliberately modest first target"; Lemma A fixes the size that is actually read.

### 2.4 Check their proof first: the account proves the admission, as an implication

Searching the account for the shifted family, not for the word "stage theorem", finds two statements that treat exactly AD-ST.

**(i) 5.2:cor-response-dilation, "The all-blocks response dilation" (CA-II 13933–14131; index: PROVED; heading unqualified).** Setting: stage n+1 of the preparatory integrations, frame 𝔅 := 𝔅^{(n)}_k, pair (𝕌,𝕁) ∈ 𝔎_P ⊃ Ũ^{(n+1)c,Σ♭}_k(X̂), complex collar datum b with sup|b| ≤ 1.1 C_1δ'_j, decoupling |σ| ≤ e^{κ_1}, ℍ the layer of "the response-layer theorem". For block amplitudes |t_□| ≤ r^♯_□ = R_0 e^{δd^-_□/2}, with R_0 = e^{−C_2κ_1}/(2𝖪_rϑ) ≥ 2, the map

  Φ_t = (e^{iηχ_tℍ}𝕌, 𝕁 + χ_t 𝒥^♯[1]),  χ_t = Σ_□ t_□ζ_□, Σ_□ ζ_□ = 1,

satisfies: (i) Φ_t ∈ Ũ^{(n)c,Σ♭}_k(X̂), holomorphically in (𝕌,𝕁,b,σ,t); (ii) every entry of Φ_t exceeds its stage-(n+1) bound by at most ⅛e^{−δd^∧/4} of its room; (iv) Φ_t = Φ^1 at t ≡ 1, Φ_0 = id; (v) r^♯_□ ≥ 2. Its proof treats entries 5 and the cube entry (unmoved), 1, 6, 7 (first-order lines), 2, 4 (bump lemma, closing estimate), 3 (second-slot bound) — CA-II 14004–14115. The text after it identifies Φ_t with the response-dilation hypothesis of 5.2:prop-two-slot-preparation (CA-II 14117–14131).

Taking t_□ ≡ z gives χ_t ≡ z, so Φ_t = E_z of `stage.md` (S11) with H = ℍ, K = 𝒥^♯[1], on the whole disc |z| ≤ R_0 = c_M/ϑ. This covers AD-ST(2) (radius two, by (v)) and also the radius ϑ^{-1} that §2.3 shows the reader needs.

**(ii) 4.26:lem-family-consumption, "Room consumed by the proof family, point by point" (CA-I 117492–117700; PROVED).** The same estimate in the inherited-domain setting of CA-I: on the fat space 𝔑(Y) ⊂ 𝔎_P, entries 5, 8 do not move; entries 1, 3, 6, 7 move by at most ι_l(y)r_a(y); composite entries 2, 4 move by at most π_×Q_a + πr_a with π ≤ ι_l/3 in every frame; and on Z^on Balaban's stage-l clauses go to his stage-(l−1) clauses "using at most ⅙𝗐_0 of each one-step room", the room being exactly the one-term difference β2^{−|ℓ−ℓ_l−1|} of the schedule sums (CA-I 117668–117678). 4.26:thm-inherited-expansion uses it to verify its stability hypothesis (CA-I 119917–119990).

**Comparison with AD-ST(2).**

| AD-ST(2) (`stage.md` (S10)–(S11)) | 5.2:cor-response-dilation |
|---|---|
| Source Ũ^{(n+1)c,Σ}_k(X̂), Balaban's stage-(n+1) space | Ũ^{(n+1)c,Σ♭}_k(X̂), "defined by the same entries with the stage-(n+1) bounds" as the stage-n space of the setting (CA-II 13931) |
| Target Ũ^{(n)c,Σ}_k(X) | Ũ^{(n)c,Σ♭}_k(X̂); Σ = Σ♭ is part of hypothesis (h) |
| Response germ at real admitted data, real φ | Layer ℍ(σ;b) at complex b; at real points "the layer of Balaban's construction" (CA-I 72411) |
| \|z\| < 2 | \|t_□\| ≤ r^♯_□, all blocks, R_0 = c_M/ϑ ≥ 2 |
| All seven entries and the gauge clauses | Entries 1–7 and the cube entry |

**Classification (FINISH rule 9).** The admission AD-ST(2) asks for is *proved in the account as an implication* (CA-I 27–76 convention). It is not an open statement of the account. Under the porting rule it becomes a cited input. Proof work then goes to the corollary's antecedents.

**What the antecedents cite.** Hypotheses (a)–(h) of the corollary, and the "bounds of the stage construction ... used in the form stated" of CA-I 116656–116717, name: the setting of the response map; the response-layer theorem (holomorphy of Φ^χ, the layer bound N_y(ℍ), N^Δ_y(A') ≤ B_♯p(y), the product estimate, ℍ independent of t at b = 0); the second-slot lemma (clauses (a), (c)–(e)); the absorption inequality; the weight-class lemma; the entry estimate's first-order lines; the bump lemma in the frame, with its general form and closing estimate; the two lemmas on the Σ♭-weighted space; the identification of the Σ and Σ♭ spaces. **The name searches of §1 found none of these as statements anywhere in the repository at the pin** (CA-I/II/III, SA, the SA draft, YM3_I/II). They occur only as citations. The bump lemma's hypotheses (D0)–(D2) and (S^b) are named (CA-I 116704–116706) but nowhere defined. So the account's proved corollary rests on a "stage construction" that is cited but absent.

### 2.5 Verdict of the consumer check

* H-STAGE: no weaker proved version; every consumer reads its conclusions as stated. No change for A10's consumers.
* AD-ST(2): superseded. Its content, at the radius its reader needs, is 5.2:cor-response-dilation (proved implication; credit Sussman and Alpoge). The open items are its absent antecedents. Two of them carry the substance:
  * **(L)** the response-layer theorem with the layer bound N_y(ℍ) ≤ B_♯ p(y), p(y) = sup|b|·e^{−δd^∧(y,𝒞_j)}, on the fat class 𝔎_P (this is `stage.md`'s premise (S19)–(S20));
  * **(B)** the bump lemma: composite entries 2, 4 under e^{iη𝒦} in a frame, CA-I (4.26:eq-regularity-radius-10).
  The others are either elementary given (L) (first-order lines, second slot: `stage.md` Lemma 2 is the first-order line argument) or identifications (Σ = Σ♭; the frame 𝔅^{(n)}_k for both stages, §5).
* What we would do differently: stop attacking AD-ST(2) as a new statement; port 5.2:cor-response-dilation; put proof work on (B), (L) and the frame identification. §§3–5 do that.

## 3. Attack 7 (new): the bump lemma from ST1 Lemmas 7–8

**Target.** Antecedent (h) of 5.2:cor-response-dilation, in its displayed form CA-I (4.26:eq-regularity-radius-10): for a frame, a pair 𝕎 in the fat class and a complex 1-form 𝒦 with N_y(𝒦) ≤ ϰ(y),

  E_e(e^{iη𝒦}𝕎)(x) ≤ (1+π_×)E_e(𝕎)(x) + π r_e(x),  π = K_{S^b} ϰ(x)/α̃_{0,m},  π_× ≤ π,  e ∈ {2,4}.

This is the composite-entry (auxiliary-configuration) increment. Both rounds of `stage.md` stopped here ("It supplies neither entry 2 nor entry 4", §7.1). The account cites it as "the bump lemma of the stage construction" with hypotheses (D0)–(D2), (S^b) that are not defined anywhere in the repository (§2.4).

**Why ST1 Lemma 8 is the right supplier.** ST1 Lemma 8 (`st1-r4.md` lines 539–600; frozen, refereed in `gates/st1-r4-gate.md`) is a localized Lipschitz bound for tower quantities at fixed real factor, on an absolute ball, uniform in depth, volume, M and κ̄:

  |G(U,w_1;e) − G(U,w_0;e)| ≤ K_T E^{δ_T}_{w_1−w_0}(x),  E^{δ_T}_w(x) = max_b e^{−δ_T d(x,b_−)} n(w;b),  n(w;b) = max{l(b)|w(b)|, l(b)²|∇^U w(b)|},   (ST1-49)

for E^0_U, sup n(w_0), sup n(w_1) ≤ a_T, at settled tower elements; G = l(x)²η^{−2}(∂T_e − I) for curvature and l(x)²ξ'(x)J_bare(T_e) for current. The towers exist on open continuation domains, are holomorphic at fixed real U, and equal the real canonical backgrounds at real w.

**Matching premises (stated, not proved here).**

* (M-tower) At every sited point x of the frame, each composite entry E_e is, up to the fixed normalization of the next line, the ST1 tower quantity |G(U,w;e)| of a settled tower element of a separated subordinate sequence of a separated ambient sequence in the sense of ST1 §1 (3). The ambient sequence is the structure's own frame; for Balaban's towers B_p(X) ∪ {Γ_i}_{i<p} on a nest obeying (A1) (CA-I 45569–45585; PDA, refereed, supplies (A1) for the prepared nest) every element is settled: below level p the tower uses the nest's rows, and at level ≥ p it has reached its final level p.
* (M-norm) E_2(x)/r_2(x) = |G|/α̃_{0,m} and E_4(x)/r_4(x) = |G|/α̃_{0,m} at the level m of the triple, with r_2(m) = α_{0,m}ℓ_m^{−2}, r_4(m,l') = α_{0,m}ℓ_m^{−2}ℓ_{l'}^{−1} (CA-I 128975–128980), α̃ carrying the same weight as r_e.
* (M-rate) δ/2 ≤ δ_T, where δ is the rate of the weight class 𝔐^∧_{δ/2} (CA-I 116540: δ := δ_0/8) and δ_T is ST1's rate; and the frame's scaled distance obeys d^∧ ≤ d with d ST1's layer-scaled metric (CA-I 116546: "d^∧ ≤ d"). If δ_0/16 > δ_T, use δ := min{δ_0/8, 2δ_T}; the account's conditions on δ are a floor δw ≥ 16 ln L + 4 on w = M/M_1 and decay statements at rate δ, so a smaller δ costs only a larger M, chosen later (CA-I 1468–1649 order).

**Lemma BL.** Assume (M-tower), (M-norm), (M-rate), ST1 Lemma 8 with its imports, and ST1 Lemma 7. Let 𝕎 = e^{iηw_0}U with U real, E^0_U ≤ a_T/2 and sup n(w_0) ≤ a_T/2. Let 𝒦 be a complex 1-form with N_b(𝒦) ≤ ϰ(b) at every bond, ϰ(b) ≤ ϰ(x)e^{(δ/2)d^∧(x,b)}, and sup ϰ ≤ a_T/218, all values inside ST1 Lemma 7's fixed ball. Then at every sited x and e ∈ {2,4},

  E_e(e^{iη𝒦}𝕎)(x) ≤ E_e(𝕎)(x) + π r_e(x),  π := 109 K_T ϰ(x)/α̃_{0,m}.   (BL)

So (4.26:eq-regularity-radius-10) holds with π_× = 0 and K_{S^b} := 109 K_T, a constant of ST1 fixed before κ.

*Proof.* Step 1 (the shifted pair has the same real factor). Define w_1 by e^{iηw_1} := e^{iη𝒦}e^{iηw_0} bond by bond, with the principal logarithm on ST1 Lemma 7's fixed ball. Then e^{iη𝒦}𝕎 = e^{iηw_1}U, and U is unchanged.

Step 2 (size of the change of potential). ST1 Lemma 7 (45), with H = 𝒦 and A' = w_0, gives on the fixed ball, at each bond b and with stencil maxima,

  l(b)|w_1 − w_0|(b) ≤ 5 l(b)|𝒦|,  l(b)²|∇^U(w_1 − w_0)|(b) ≤ 13 l(b)²|∇^U𝒦| + 96 (η/l(b)) l(b)|𝒦| l(b)²|∇^U w_0|.

Since η ≤ l(b) and l(b)²|∇^U w_0| ≤ sup n(w_0) ≤ 1, the right sides are at most 109 N_b(𝒦). Hence n(w_1 − w_0; b) ≤ 109 ϰ(b).

Step 3 (both potentials stay in ST1's ball). sup n(w_1) ≤ sup n(w_0) + 109 sup ϰ ≤ a_T/2 + a_T/2 = a_T. With E^0_U ≤ a_T, ST1 Lemma 8 applies at w_0 and at w_1.

Step 4 (the weight). By Step 2, the weight-class property of ϰ, d^∧ ≤ d and (M-rate),

  E^{δ_T}_{w_1−w_0}(x) ≤ 109 max_b e^{−δ_T d(x,b)} ϰ(b) ≤ 109 ϰ(x) max_b e^{−(δ_T − δ/2) d(x,b)} ≤ 109 ϰ(x).

Step 5 (conclusion). (ST1-49) gives |G(U,w_1;e)| ≤ |G(U,w_0;e)| + 109 K_T ϰ(x) at the settled element at x. Divide by α̃_{0,m} and use (M-norm): E_e(e^{iη𝒦}𝕎)(x)/r_e(x) ≤ E_e(𝕎)(x)/r_e(x) + 109K_Tϰ(x)/α̃_{0,m}. Multiply by r_e(x). ∎

**Use in the corollary (closing estimate for entries 2, 4).** In the corollary's proof (CA-II 14067–14077), φ_γ(x) ≤ (11B_♯𝖼_□/𝖪_r) ρ_m α_{·,m} e^{−δd^∧/4} (its (5.2:eq-response-dilation-9)), with 𝖪_r ≥ 2^9 𝖼_□ K_{S^b} B_♯. Put ϰ := φ_γ. Then π ≤ (11K_{S^b}B_♯𝖼_□/𝖪_r) ρ_m (α_{·,m}/α̃_{0,m}) ≤ (11/2^9) ρ_m, using α_{·,m} ≤ α̃_{0,m}. By (BL), entries 2 and 4 rise by at most (11/2^9) ρ_m r_e < ⅛ ρ_m r_e. When the room of a composite clause at x is ρ_m w r_e with weight w ≥ 1 (the factor L_0^{2e} of (1.64), (1.66)), this is at most ⅛ of the room. With π_× = 0 no 2^Δ weighting has to be paid.

**What Attack 7 does and does not give.**
* It supplies the analytic content of antecedent (h), the composite increment, for every frame satisfying (M-tower), from a refereed lemma of ours. The constant is K_{S^b} = 109K_T, fixed before κ, so 𝖪_r and R_0 keep the account's order.
* It does not supply the "general form" and the "two lemmas on the weighted space" of (h), which concern the Σ♭ weighting of structures born at earlier stages. When the room of an older structure carries a factor below one, (BL)'s additive increment must be compared with it; that comparison needs the definition of the Σ♭ weights, which is absent (§2.4).
* (M-tower) is a reading of the stage spaces' composite entries. §5 shows where that reading carries the real difficulty.

## 4. Attack 8 (new): the layer bound from the account's response chart

**Target.** Antecedent (b) of 5.2:cor-response-dilation: N_y(ℍ) ≤ B_♯ p(y), p(y) = sup|b| e^{−δd^∧(y,𝒞_j)}, the product estimate, and Φ_t independent of t at b = 0; and antecedent (c) at χ ≡ 1. This is `stage.md`'s premise (S19)–(S20), assumed there.

**Supplier.** 4.5:thm-chart-existence, "Existence, uniqueness and analyticity of the response chart" (CA-I 14496–14560; index PROVED, an implication from 4.5:lem-free-current-operators and 4.5:lem-nonlinear-correction, which take Balaban sentences "stated … without proof", and from the printed CMP 99b (3.132) through 4.5:prf-chart-linear-bounds; `port-map.md` row 1). For (U,J) ∈ 𝔖 and a block field B with |B| < c_9, clause (K1) gives existence, uniqueness and joint analyticity of the chart in (B,𝔞,J), and 4.5:prf-chart-variation-decay (CA-I 14803–14899, PROVED) gives (K4) for |B| ≤ c_9/2 and (K8):

  |δℋ^J(x)/δB(c)| ≤ C^K_{190} ℓ_j^{−1}ℓ_{j'}^{−d}𝔈,  |∇_U δℋ^J(x)/δB(c)| ≤ C^K_{190} ℓ_j^{−2}ℓ_{j'}^{−d}𝔈,  |δ𝔍(x)/δB(c)| ≤ C^K_{190} ℓ_j^{−3}ℓ_{j'}^{−d}𝔈,

with 𝔈 = e^{−c_*δ_0 d(y,y')}, x ∈ Δ(y), y ∈ Λ_j, c a block bond at y' ∈ Λ_{j'}, and "sums over y' carry the measure ℓ_{j'}^d".

**Matching premise.** (M-chart) The frame 𝔅 = 𝔅^{(n)}_k is an admissible sequence for the chart (Balaban's CMP 102b (1); (A1) of CA-I 45569 is the geometric part, supplied for the stage nest by PDA and by "the lemma asserting that Balaban's stage nests are admissible", CA-I 48585–48590). The stage layer at datum (0,b) is the chart's ℋ^J at the block field b supported on the collar bonds 𝒞_j (CA-I 116567–116575 applies "the theorem that constructs the stage layer" at (𝔅; 𝕌,𝕁; σ; (0,b)) on 𝔎_P). The fat class lies in 𝔖. For the radii this is a γ-ceiling: γ_0^{(k)} ≤ γ̄_0(t_k) → 0 (CA-I 116610–116640, 4.26:def-regularity-radius (b), proved), while 𝔖's radii a_1, a_γ are (d,L)-numbers (CA-I 12935–12977); the cube-gauge clause of 𝔖 must be implied by (D0) of the fat class.

**Lemma L.** Assume (M-chart) and the chart's clauses (K1), (K4), (K8). Put δ_L := c_*δ_0/2 and C_Σ := sup_y Σ_{y'} e^{−(c_*δ_0/2) d(y,y')}, the sum over block points of all levels. Let sup|b| ≤ c_9/2, and let the decoupling parameter be σ ≡ 1. Then, at every cell y of level j(y),

  N_y(ℋ^J(b)) := max{ℓ_{j(y)}|ℋ^J(b)|, ℓ_{j(y)}²|∇_Uℋ^J(b)|} ≤ B_♯ sup|b| e^{−δ_L d(y,𝒞_j)},  ℓ_{j(y)}³|𝔍(b)| ≤ B_♯ sup|b| e^{−δ_L d(y,𝒞_j)},

with B_♯ := n_b C^K_{190} C_Σ, n_b the number of block bonds at a block point. Moreover ℋ^J(0) = 0 and 𝔍(0) = 0, so at b = 0 the map Φ_t is the identity for every t. Since d^∧ ≤ d, the bound holds with d^∧ in place of d.

*Proof.* Step 1 (the segment). For 0 ≤ t ≤ 1 the field tb has |tb| ≤ c_9/2, so (K1), (K4) and (K8) hold at B = tb. By (K1), t ↦ ℋ^J(tb) is analytic, hence

  ℋ^J(b) − ℋ^J(0) = ∫_0^1 δℋ^J(tb)[b] dt,  δℋ^J(tb)[b](x) = Σ_c ℓ_{j'(c)}^d (δℋ^J(x)/δB(c))|_{tb} b(c).

Step 2 (the value at zero). At B = 0 the map 𝒜 ↦ G̃_0[Θ_J𝒜 − 𝕍'^J(𝒜)] fixes 𝒜 = 0, because Θ_J is linear and 𝕍'^J(0) = 0 by the quadratic gradient bound (4.5:lem-gradient-bound). By uniqueness in (K1), 𝒜^J_0(0) = 0, so A_G = 0. The nonlinear correction vanishes at zero (4.5:lem-nonlinear-correction), so X_G = 0 and ℋ^J(0) = 𝔏^J(0) = 0. Then Ξ = 0, Λ^J(0) = 0 and F(U,0) = 0 by 4.5:eq-curvature-remainder-2, so 𝔍(0) = 0 (Definition 4.5:def-response-chart).

Step 3 (the sum). By (K8), with b supported on 𝒞_j,

  |δℋ^J(tb)[b](x)| ≤ C^K_{190} ℓ_{j(y)}^{−1} sup|b| Σ_{c ∈ 𝒞_j} e^{−c_*δ_0 d(y,y'_c)} ≤ n_b C^K_{190} ℓ_{j(y)}^{−1} sup|b| e^{−(c_*δ_0/2) d(y,𝒞_j)} Σ_{y'} e^{−(c_*δ_0/2) d(y,y')},

using d(y,y') ≥ d(y,𝒞_j) for y' on 𝒞_j and splitting the exponent in halves. The last sum is at most C_Σ. Integrating over t gives the first bound for ℓ_{j(y)}|ℋ^J(b)|. The second and third bounds follow in the same way from the ∇_U member and the 𝔍 member of (K8). ∎

*On C_Σ.* It is finite and depends on (d,L) only: in the layer-scaled metric each block point occupies a cell of unit scaled size, so at most C(d)r^{d} points lie within scaled distance r, and Σ_r r^{d−1}e^{−cr/2} converges. The account's 4.5:lem-kernel-algebra (PROVED) contains sums of this kind.

**What Attack 8 does and does not give.**
* It supplies the layer bound, the vanishing at b = 0, and the second-slot bound at χ ≡ 1 (antecedent (c) at χ ≡ 1, which is the only case the corollary's proof uses, CA-II 14079–14093), at σ ≡ 1 and rate δ_L = c_*δ_0/2; and, by the next bullet, at |σ| ≤ e^{κ_1}. If c_*δ_0/2 < δ_0/8, the account's δ must be lowered to δ_L; this is the convention of (M-rate).
* **The decoupled layer.** Clause (K10), 4.5:prf-chart-walk-localisation (CA-I 15265–15345, PROVED, from the walk expansion of 𝗊_0 printed in CMP 99b after Theorem 3.9), states that (K1), (K3)–(K5) and (K8), with ℋ^J(s)(0) = 𝔍(s)(0) = 0, hold at complex decoupling parameters |s(Δ)| ≤ e^{κ_1} with B_0 replaced by B_0e^{c_𝕂κ_1}, under δ_1M ≥ κ_1 and the ceiling e^{2c_𝕂κ_1}|B| ≤ c_9. The proof of Lemma L then runs unchanged at |σ| ≤ e^{κ_1}, with B_♯ replaced by e^{c_𝕂κ_1}B_♯ and sup|b| ≤ e^{−2c_𝕂κ_1}c_9/2, a γ-ceiling since κ_1 is fixed before γ. This assumes that the corollary's decoupling cubes are the chart's family σ_0 of CMP 116 (part of (M-chart)), and that C^K_{190} scales with B_0 as (K10) says of "B_0"; the second point was read from (K10)'s wording, not re-derived. The factor e^{c_𝕂κ_1} enters 𝖪_r and is the kind of factor the corollary's e^{−C_2κ_1} carries.
* It does not discharge the chart's own printed input, CMP 99b (3.132) (`port-map.md` row 1, open there). Our P82 and CP12 Theorem 3 rebuild the real layered case.

## 5. Attack 9 (new): which frame reads the composite entries

### 5.1 The question

The corollary reads its source and its target with "the same entries" (CA-II 13931): one family of composite clauses, the index set 𝓛_n of pairs (n',p) of hypothesis (h), in the frame 𝔅 = 𝔅^{(n)}_k (CA-II 13888). Its last antecedent is "the identification of the spaces written with Σ and with Σ♭" (CA-II 13982–13983). H-STAGE's source is Balaban's stage-(n+1) space. So the port needs

  (SRC) every point of H-STAGE's stage-(n+1) space lies in the corollary's source, that is, satisfies the composite clauses of 𝓛_n at the stage-(n+1) bounds.

The target side needs nothing: the corollary's target is the stage-n space with the 𝓛_n clauses. Two readings of the stage spaces decide (SRC).

* **(R♭), birth frames.** The stage-l space carries a composite clause for every structure born at a stage l' ≤ l, each read in its own birth frame, with a bound fixed by (structure, point, stage). This is the account's ♭ design: "(Σ^♭)-structure with birth level m_ref", "every entry is compared with the entry of the same kind" (CA-I 117660–117668). The corollary's index set 𝓛_n of pairs (n',p) is defined nowhere in the repository; reading n' as a birth stage is this note's interpretation, consistent with CA-I 117660–117668.
* **(R1), one frame.** The stage-l space carries the composite clauses of the towers B_p(X'') ∪ {Γ̂^{(l)}_i}_{i<p} of its own stage nest 𝒩^{(l)} only, for every admissible X''. This is the layered-space form (CA-I 9843–9846) read on the stage nest of CA-I 48555–48565.

### 5.2 Under (R♭), (SRC) is free

**Lemma F.** Under (R♭), 𝓛_n ⊂ 𝓛_{n+1}, and every clause of the corollary's source is a clause of the stage-(n+1) space with the same bound. Hence (SRC) holds and no room is spent.

*Proof.* A structure born at a stage n' ≤ n is born at a stage ≤ n+1, so 𝓛_n ⊂ 𝓛_{n+1}. Under (R♭) the bound of the clause of a structure at a point and stage depends on the structure, the point and the stage, not on the latest frame. The corollary's source imposes the 𝓛_n clauses at the stage-(n+1) bounds; the stage-(n+1) space imposes the 𝓛_{n+1} clauses at the same bounds. ∎

**Fact (the frames are nested).** Under the stage-nest reading, λ_{𝔅^{(n)}} ≤ λ_{𝔅^{(n+1)}} pointwise, so 𝔅^{(n)}_k ≼ 𝔅^{(n+1)}_k in the refinement order of CA-I 127213. *Proof.* The level of a frame built on a nest is λ(x) = max{i : x ∈ Ω̂_i}. The nests 𝒩^{(n)} and 𝒩^{(n+1)} differ only at level j+1, where Ω_{j+1} is replaced by Ω''_{j+1} ⊇ Ω_{j+1} (the collar R_n = Z_{j+1} ∖ Z''_{j+1} becomes small field at level j+1, CA-I 53800–53815). So Ω̂^{(n)}_i ⊆ Ω̂^{(n+1)}_i for every i, and the maximum can only increase. ∎ The older frame is the finer one. This is why, under (R♭), the bump lemma of §3 is applied to each structure in its own (finer, older) frame, where its elements are settled.

### 5.3 Under (R1), (SRC) is a frame change; the direct proof fails

Under (R1), only the towers with p ≥ j+1 change between the two frames: Γ̂_i depends on (Ω̂_i, Ω̂_{i+1}), and the nests differ only at level j+1, so Γ̂_j and Γ̂_{j+1} change on the collar and Γ̂_i, i ≤ j−1, do not (ST1 §1's definition of rows; CA-I 9843–9846). For p ≥ j+1 the old tower D (with the collar's level-j rows) is finer than the new tower D' (with the collar's level-(j+1) rows): the D'-data are functions of the D-data. Write Ψ_D, Ψ_{D'} for the critical branches.

**Step 1 (nested criticality; `stage.md` Attack 3; 4.26:prf-nested-criticality, CA-I 128485, proved).** For a point P of the new space put Q := Ψ_{D'}(M_{D'}P), the new auxiliary configuration. Then Q = Ψ_D(M_D Q). The data M_D P and M_D Q agree off the collar's level-j rows and differ there by δd := M^j(P) − M^j(Q).

**Step 2 (the old auxiliary configuration is a collar response).** Ψ_D(M_D P) − Q = Ψ_D(M_D Q + δd) − Ψ_D(M_D Q). This is the response of the finer frame to a collar datum δd, the object of Lemma L, taken at the pair Q.

**Step 3 (size of δd).** On the collar, P's simple entries and Q's composite entries obey the stage-(n+1) clause, which is advanced: its radius index is one higher and its weight exponent at most one higher than the stage-n clause, so in stage-n units its curvature bound is at most (1+β_0)L_0^2L^{−2} times the stage-n bound (the computation of CA-I 120617–120660 for entries 6, 7, with p_e = 2 for curvature; α_{·,j+1} ≤ (1+β_0)α_{·,j}, CA-I 127217–127219; L_0^2 ≤ L/3, CA-I 45849). The persistent tower R := Ψ_{D_j}(M_{D_j}P), with p = j, carries P's level-j data and obeys the same advanced clause. R and Q have the same level-(j+1) averages on the collar. In a common axial gauge on each level-(j+1) block (side L in level-j steps), two fields with level-j plaquettes at most κ have potentials at most C_ax Lκ. Hence

  |δd| ≤ 2C_ax L κ ≤ 2C_ax (1+β_0) L_0^2 L^{−1} τ_1,  κ := (1+β_0)L_0^2L^{−2}τ_1,

where τ_1 is the stage-n curvature threshold on the collar, in level-j units.

**Step 4 (what closes and what does not).** By Lemma L at the frame D and the pair Q, the old composite curvature at a point y differs from Q's by at most C_fc |δd| e^{−δ_L d(y,𝒞_j)}, C_fc a (d,L)-number made of B_♯ and ST1 Lemma 7's curvature constant. Next to the collar, on the persistent layer j, the room is the stage gap β2^{−1} times the threshold (CA-I 117668–117678). So the direct proof needs

  2 C_fc C_ax (1+β_0) L_0^2 L^{−1} ≤ β/4,  i.e. C_fc C_ax ≤ 21/256 ≈ 0.08 for β = 1/4, β_0 = 1/7, L_0^2 = L/3.   (FC-num)

Here β/4 is half of the stage gap β2^{−1} at the layer m = j next to the collar, and (1+β_0)L_0^2/L = 8/21 at the extreme L_0^2 = L/3.

If one uses instead that δd is slowly varying (R and Q are both smooth), the response's curvature is of order κ rather than Lκ, and the condition becomes

  C'_fc (1+β_0) L_0^2 L^{−2} ≤ β/4,  i.e. C'_fc ≤ 21L/128 ≈ 0.16 L,   (FC-L)

with C'_fc the curvature-to-curvature collar constant (the Hölder member of (K8) enters here).

**Failure 9 (exact reason).** In the zone I_M = {k_0+1,…,k} the weight L_0^{2e} of (1.64) and (1.66) takes back the scale gain L^{−1} of the advanced clause up to the fixed factor L_0^2/L ≤ 1/3. So (FC-num) is a numerical condition on uncomputed constants, and (FC-L) asks for a collar constant that grows slower than L. All the constants involved (C^K_{190}, B_0, C_ax, ST1 Lemma 7's 2^{12}) are (d,L)-numbers, which the account places after L (CA-II 2277–2278: "(d,L)-numbers. They are placed immediately after (L,δ)"). A floor on L therefore cannot beat them, and M, κ, γ do not enter. Outside I_M (no L_0 weight) the factor is (1+β_0)L^{−1} or (1+β_0)L^{−2} and the same obstruction applies. Neither inequality is shown false; neither is supplied by any choice in the account's order. No counterexample to (SRC) was attempted beyond this estimate. The obstruction found is quantitative: it is a missing constant bound, not evidence that (SRC) fails.

## 6. Assembly: AD-ST at the reader's radius on the birth-frame reading

**Theorem S.** Fix an ordinary preparatory stage n+1 (no live arrest), j = h+n, frame 𝔅 = 𝔅^{(n)}_k, and decoupling parameters σ ≡ 1 (or |σ| ≤ e^{κ_1}, with (K10) added to item 2). Read the stage spaces in the birth-frame form (R♭). Assume:

1. 5.2:cor-response-dilation (CA-II 13933–14115), a proved implication (port; credit Sussman and Alpoge);
2. (M-chart) and the response chart's clauses (K1), (K4), (K8) (CA-I 14496–14899, proved implications resting on the printed CMP 99b (3.132));
3. (M-tower), (M-norm), (M-rate), and ST1 Lemmas 7–8 with ST1's imports (AV/CURV, PROF, (15), Lemmas 2–3, P81);
4. (Z) the cover's profile bound, sup_{Δ̃(y)} max{|ζ_□|, ℓ|∇ζ_□|, ℓ²|∇∇ζ_□|} ≤ 5 summed over the cubes with □^ζ ∩ Δ̃(y) ≠ ∅, and the triangle inequality and d^∧ ≤ d for the scaled distance;
5. (f) the absorption inequality (5.2:eq-response-dilation-6), a parameter condition (a γ-ceiling when q > q_*);
6. (W♭) the room of every composite clause of 𝓛_n at a point of level m is at least ρ_m r_e, r_e the unweighted shell radius at the level of the triple (CA-I 116712–116713).

Then for every P in the stage-(n+1) space on X̂, every complex collar datum b with sup|b| ≤ 1.1C_1δ'_j, and every |z| ≤ R_0 = e^{−C_2κ_1}/(2𝖪_rϑ) (so R_0 ≥ 2 and R_0 ≍ ϑ^{−1}), the pair E_z(P) = (e^{izηℍ}𝕌, 𝕁 + z𝒥^♯[1]) lies in the stage-n space on X̂, holomorphically in (P,b,z). Every entry of E_z(P) exceeds its stage-(n+1) bound by at most ⅛ of its room. Restriction to X ⊂ X̂ keeps this (the spaces are hereditary). In particular AD-ST(2) of `stage.md` holds, and so does the radius ϑ^{−1} that its reader needs (§2.3), on the (R♭) spaces.

*Proof.* Lemma F gives (SRC). Take t_□ ≡ z; then χ_t ≡ z and |t_□| ≤ R_0 ≤ r^♯_□. Run the corollary's proof (CA-II 14004–14115) with these suppliers of its antecedents:

* (a) holomorphy: (K1) gives joint analyticity of ℋ^J and 𝔍 in (B,𝔞,J); χ_t enters linearly.
* (b) layer bound, b = 0 case: Lemma L, with B_♯ = n_bC^K_{190}C_Σ and rate δ_L. The product estimate N_y(χℍ) ≤ 2a(y)N_y(ℍ) is the lattice Leibniz rule: ∇(χℍ) = (shifted χ)∇ℍ + (∇χ)ℍ, so ℓ²|∇(χℍ)| ≤ a(y)(ℓ²|∇ℍ| + ℓ|ℍ|) ≤ 2a(y)N_y(ℍ), and ℓ|χℍ| ≤ a(y)N_y(ℍ).
* (c) at χ ≡ 1, the only case used (CA-II 14079–14093): Lemma L's current bound, with K_χ := B_♯/2. The second slot 𝒥^♯[1] is the chart's 𝔍(b) (CA-II 14121–14125).
* (d), (e): elementary from (Z), d^∧ ≤ d and the triangle inequality. For (d): if □^ζ meets Δ̃(y), pick y' in both; then d(y,y') ≤ D_0, the scaled diameter of Δ̃(y), so p(y) ≤ e^{δD_0}p(y') ≤ e^{3δD_0}q_□(y); with (Z), a(y)p(y) ≤ 5e^{3δD_0}Σ_□|c_□|q_□(y) ≤ q(y) once e^{3δD_0} ≤ 2, a smallness condition on δ of the kind (M-rate) already allows; and q ∈ 𝔐_{2δ} by the triangle inequality for d. For (e): for y' ∈ □^ζ, d^∧(y',𝒞_j) ≥ d^∧(□,R_n) = d^-_□ because 𝒞_j ⊂ R_n; so |c_□|p(y') ≤ R_0 sup|b| e^{−(1−θ)δd^∧(y',𝒞_j)}; then move from y' to y with the triangle inequality and use e^{−2δd(y,y')} ≤ e^{−(1+θ)δd(y,□̃)}e^{−(1−θ)δd(y,y')}.
* (f): assumed.
* (g): the weight claim is the triangle inequality for d^∧. The first-order lines come from ST1 Lemma 7 (46): |D|, |∇D| ≤ 2s and the curvature increment ≤ 4sη², under its fixed smallness conditions (met after γ-ceilings, with η/ℓ ≤ 1/13 from L ≥ 13). Constant 4 replaces the corollary's 3; its arithmetic becomes 4·11/2^9 = 44/2^9 < ⅛, so the conclusion is unchanged.
* (h): Lemma BL with ϰ := φ_γ and the closing comparison of §3, which needs only (W♭), because π_× = 0.

Entries 5 and the cube entry are unmoved because the real factor is kept (CA-II 14062–14063). The identification of Φ_{t≡z} with E_z: H = ℍ and K = 𝒥^♯[1]; at real points the chart is Balaban's construction (4.5:lem-true-pair-reduction, 4.5:prf-diagonal-exactness, proved; CA-I 72411), and two holomorphic maps that agree at the real points of a connected domain agree on it. The real passing support |B_j| < δ'_j/g_j lies in the disc sup|b| ≤ 1.1C_1δ'_j (CA-I 81839). ∎

**Order of constants.** No new choice is made after γ except γ-ceilings. K_{S^b} = 109K_T and K_χ, B_♯ come from ST1 and the chart, both fixed before κ; 𝖪_r and R_0 are then the corollary's. (M-rate) may lower δ to min{δ_0/8, 2δ_T, c_*δ_0/2}; this enlarges M through the floor δw ≥ 16 ln L + 4, and M is chosen after the rates.

## 7. Result

**Proof**

Kind: check of their proof (the account proves the admission as an implication, and `stage.md`'s open lemma is a special case of it), plus proof of the two substantive inputs that their proof cites but the repository does not contain. It is an implication from named premises, not a discharge. Proved by Claude, not yet checked by Codex.

1. **Consumer check (§2).** No weaker proved version of H-STAGE exists. Every consumer (A10, 4.18:rem-decay-rates, 4.18:thm-action-domain, 4.6:rem-widened-support, the torus-independence list, 4.28:prop-kernel-membership, our A17) reads its conclusions as stated, and the account's own route leaves its stage lemma unwritten. The only reader of AD-ST(2) is the stage argument's Cauchy step. It needs a z-disc of radius of order ϑ^{−1}; radius two gives no smallness (Lemma A).
2. **Check their proof first (§2.4).** AD-ST(2), and the radius ϑ^{−1}, are the all-blocks response dilation 5.2:cor-response-dilation (CA-II 13933–14131), proved in the account as an implication. 4.26:lem-family-consumption (CA-I 117492) is the same estimate in CA-I. So `stage.md`'s open lemma is not an open statement of the account. The corollary's antecedents cite a "stage construction" (the response-layer theorem, the second-slot lemma, the bump lemma with (D0)–(D2), (S^b), the Σ♭ weighting lemmas) that is stated nowhere in the repository at `31a47c543775`.
3. **The two substantive antecedents, supplied.** Lemma BL (§3): the bump lemma's composite-entry increment (entries 2 and 4, the auxiliary configurations on which both rounds of `stage.md` stopped), from our refereed ST1 Lemmas 7–8, in additive form with K_{S^b} = 109K_T. Lemma L (§4): the layer bound, its b = 0 case and the second slot, from the account's response chart (K1), (K4), (K8), at σ ≡ 1 and, through (K10), at |σ| ≤ e^{κ_1}; rate c_*δ_0/2.
4. **Theorem S (§6).** On the stage spaces read with birth frames (R♭), AD-ST holds on the whole disc |z| ≤ R_0 = e^{−C_2κ_1}/(2𝖪_rϑ) ≍ ϑ^{−1}, for all seven entries and the cube entry, using at most ⅛ of each room, holomorphically, uniformly, with constants in the account's order. (R♭) is the account's own reading as far as the repository shows: it calls the Σ♭ space "Balaban's space" (CA-I 119865–119866) and compares entries structure by structure with birth levels (CA-I 117660–117668). The corollary's index set 𝓛_n is not defined in the repository; its reading as birth pairs is ours. Under (R♭) the source inclusion is free (Lemma F).

**Premises the implication keeps.** (M-tower), (M-norm), (M-rate) (§3); (M-chart) (§4); (Z), (f), (W♭) (§6). Each is a reading of a definition the repository does not contain, or a parameter condition; each is stated where it is used. Imports: ST1 Lemma 8's inputs (AV/CURV, PROF, (15), Lemmas 2–3, P81); the chart's inputs (the printed CMP 99b (3.132) and the Balaban sentences of 4.5:lem-free-current-operators and 4.5:lem-nonlinear-correction).

**One precise open lemma, for the other reading (FC, frame change at one stage).** If Balaban's stage spaces are read in the one-frame form (R1), where the stage-l space carries only the composite clauses of the towers B_p(X'') ∪ {Γ̂^{(l)}_i}_{i<p} of its own stage nest, then (SRC) needs: every point P of the stage-(n+1) space satisfies, for every tower D of the stage-n frame with p ≥ j+1 and every sited point y of level m, D's composite clauses at the stage-(n+1) bound plus at most ½β2^{−|m−j−1|} times the clause's unit, uniformly and with constants in the account's order. This is the last clause of the corollary's (h), "the identification of the spaces written with Σ and with Σ♭", at the source. Attack 9 (§5.3) is the direct proof: nested criticality writes the old auxiliary configuration as a collar response of the finer frame. It closes only under (FC-num) C_fcC_ax ≤ 21/256 or (FC-L) C'_fc ≤ 21L/128, because in I_M the L_0^{2e} weights take back the scale gain up to L_0^2/L ≤ 1/3 and all constants involved are (d,L)-numbers fixed after L. CMP 122a p. 190 is not available here, so which reading is Balaban's is not settled by a source.

**What we would do differently.** Port 5.2:cor-response-dilation (credit Sussman and Alpoge) in place of `stage.md`'s AD-ST(2), with Lemmas L and BL as its suppliers, and read the stage spaces as the account does, (R♭). Then A10 (b) is read on the ♭ spaces; A10's consumers in the account already work there (4.26:thm-inherited-expansion (b): D^♭_n ⊇ Ũ^{(n)c,Σ♭}_k ∩ 𝔑^{(n)} at unweighted c = 1 locations). FC becomes a side question, needed only to match a one-frame reading of CMP 122a.

**What stays open.** The rest of H-STAGE: Gaussian normalization, cluster expansion, (1.70) and cumulation; the account's stage lemma is unwritten and (1.70) is printed without proof. For the decoupled layer, |σ| ≤ e^{κ_1}, Lemma L reads (K10) as stated (§4); its proof was not re-checked here. The chart's printed inputs CMP 99b (3.132) and the walk expansion after its Theorem 3.9. ST1's imports. The premises listed above. FC under (R1).

**Defects found in earlier text (for the lead).**
* `stage.md` §§5–7: its open lemma is treated by the account (FINISH rule 9). Its Attack 6 found 4.26:prop-source-image but not 5.2:cor-response-dilation or 4.26:lem-family-consumption. Its radius two is too small for its only reader (Lemma A).
* The account (not a correction of a stated proof): 5.2:cor-response-dilation and CA-I 116656–116717 cite statements absent at `31a47c543775`. That is a missing reference, which FINISH item 6 excludes from contributions. Lemmas BL and L could become a contribution only after a Codex check and the five-step test.
* `port-map.md` row 5 (DOM) and FINISH row 335 should name 5.2:cor-response-dilation (proved implication) as the account's treatment of stage admission.
