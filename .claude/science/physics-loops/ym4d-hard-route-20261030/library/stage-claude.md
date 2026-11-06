lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T12:30Z

# stage-claude: hereditary holomorphic continuation for H-STAGE

Queue row 346 of `FINISH.md`. Pinned commit b977aba9d. Work in progress; sections are added as they are written.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, branch `claude/ym4d-hard-route` at b977aba9d. Research text, not an audit; grants no status. Written arguments only; source searches are navigation, not proof. Not yet checked by the other model.

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
2. The account's own stage route (Chapters 4.24–4.26, 5.2) does not supply a proved replacement. Its stage lemma "is not written out here; parts of its proof are printed below" (CA-I 118758–118760, Remark 4.26:lem-stage-expansion). The survivor-block theorem assumes "the normalisation lemma at the full stage and the fluctuation cluster expansion at the full stage" (CA-I 104740–104743, (h3)); these are H-STAGE's own lemmas. Its norm conversion is "Proof outstanding" (4.24:prop-norm-conversion, CA-I 106533), and so is its holonomy bound (4.24:prop-holonomy-bound, CA-I 107073). The arrest theorem is incomplete (CA-I 137628). Its constant is C_0^♯ = 3c_G + 1, not c_G + 1 (CA-I 104794–104804).
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
