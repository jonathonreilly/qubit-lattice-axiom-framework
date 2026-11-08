lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SGAP0 referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane (model id `claude-opus-5-5`, max reasoning) on the Mac mini, as pass 3, the referee, under PR #10138's method. (The lane brief's generic format line says "pass 1"; this lane is the pass-3 referee.) This session wrote neither pass 1 (`SGAP0_DRAFT.md`) nor pass 2 (`SGAP0.md`). This is one check: one whole-part, line-by-line read. No review of this review was commissioned, and no other review was read.

**Text read.** `SGAP0.md` as of commit `997ffa30e` (the last commit that touches it; branch head `claude/toe-assembly` when read). SHA-256 of the file read: `0a0c80f69ec902476b08d9d55bd866c649654d923e10a8b1c83d630a22340471`. Line numbers below refer to that file.

**Pass-1 source.** `SGAP0_DRAFT.md` as of commit `f04958033`, SHA-256 `71ee2dd593e9b067ea8333603f5c83641e286668f2234f4df723fef788dc93ca`.

**Method.** Every proof step was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-SGAP0ref/` (under a minute, a few MB, run only with at least 50 percent free memory). It guides or refutes and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step; it is the referee's, not the author's. The standard is the owner's bounded R-GEN choice for SMG1 rungs (`TOE_ASSEMBLY.md` 3.10). Owner guidance applied, verbatim: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The model of `SGAP.md` and `SMG15.md` is read plainly. No reading, specification or definition is adopted here.

**References consulted, at branch head `997ffa30e`.** `SGAP0_DRAFT.md` (all, as the pass-1 source; commit `f04958033`); `prior/SGAP0.md` (all, commit `fa803749e`, SHA-256 `77815dd2…5435`, equal to the hash `SGAP0.md` records); `SGAP.md` (SHA-256 `be026f7c…bdc91`, equal to the recorded hash), lines 1-100 in full and 101-153 to 900 characters per line (only the last paragraph, line 153, is longer); `SMG15.md` (SHA-256 `b65cf2e1…6995`, equal to the recorded hash), lines 36-42 (Theorem 2), 136-140 (Theorem 7) and 155-162 (§8), found by grep; `SMG1.md` line 53; `SGAP_REFEREE.md` line 99; `TOE_ASSEMBLY.md` (SHA-256 `0cdb4965…2ee0`, equal to the recorded hash), §3.10 lines 257-269 found by grep; `LW1_REFEREE.md` lines 1-80 (format only); `Y2W_DRAFT.md` lines 1-30 (head format only). The hashes of `SMG1.md` and `LW1.md` also equal the recorded ones. No other branch was needed: the digest's main-branch items are context in `SGAP0.md`, not proof steps.

**Working-set entries used.** None directly. The model is the frozen finite-ring model of `SGAP.md` §1 (atom of `SMG1.md` Theorem 2.2, Gauss reduction of `SMG15.md` Theorem 2), read plainly, with zero electric coupling and `t=0`. The judged target is S-GAP⁰ of `SGAP.md` Definition 4, under the owner's bounded R-GEN choice (`TOE_ASSEMBLY.md` 3.10).

---

## 0. What was judged

The text judged is `SGAP0.md` (172 lines). Its pass-1 source is `SGAP0_DRAFT.md` (398 lines). Where `SGAP0.md` cites or condenses the draft, the two were compared line by line; section 4 below lists every place where they differ in content.

The judged claims are: S-GAP⁰ of `SGAP.md` Definition 4 (line 20, "**S-GAP⁰** is the same statement with `t=0`. Both include `ε=0`. These are finite-ring questions, not GNS or tick statements."); (G1′) and (HF-alt) of `SGAP.md` lines 93 and 95; and the lemmas that `SGAP0.md` proves on the way. Against the owner's bounded R-GEN (`TOE_ASSEMBLY.md` line 261, "A unique gapped ground state has GNS generator with kernel \(\mathbb C\Omega\) ... Scope: SMG1's rungs only"), S-GAP⁰ is a finite-ring spectral ingredient. `SGAP0.md` claims no GNS-generator gap and no uniqueness (lines 158, 164). That scope is accurate. At `t=0` the half-filled ground level has even multiplicity (`SGAP.md` Corollary 4.4), so this model cannot supply the R-GEN uniqueness clause on finite rings; `SGAP.md` line 151 already records this.

**Counts.** 49 items: 47 CORRECT, 1 ERROR, 1 INCOMPLETE. The six distiller definitions count as six items. No ERROR or INCOMPLETE item changes the content of a theorem or a constant.

## 1. Verdict table

| # | Item (`SGAP0.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Status paragraph (3) | CORRECT | The "GAP corrected" sentence is accurate; see item 22 and section 2. |
| 2 | Provenance (5) | CORRECT | All seven recorded SHA-256 values equal the files at `997ffa30e` `[check: shasum]`. |
| 3 | Definition 1 (11) | CORRECT | Matches `SGAP.md` Definitions 1-2. |
| 4 | Definition 2 (12) | CORRECT | "Both alternating patterns are allowed" holds because `L∈4N` makes `k(p_alt)=L/2` even. |
| 5 | Definition 3 (13) | CORRECT | Matches `SGAP.md` Definition 3 and Theorem 4 (line 66); `e=W+14` on the three line types. |
| 6 | Definition 4 (14) | CORRECT | `Z_p`, `Π_p^⊥` and `Δw^{(2)}` are used later and never defined (edit E3). |
| 7 | Definition 5 (15) | CORRECT | Same quantifiers as `SGAP.md` lines 20, 93, 95. "δ smaller than the sector gap" is Proposition 4.3's condition, not a new target. |
| 8 | Definition 6 (16) | CORRECT | `[check]` `θ=0.0115471`, `16θ=0.184754`; `√u(10⁻⁸τ)=2.0·10⁻⁴<e^{−7}`, so `θ_|ε|=2e^{−7}` there. |
| 9 | Proposed readings, not adopted (18) | CORRECT | Matches `SGAP.md` line 24. Nothing is adopted. |
| 10 | Theorem 1, statement and proof (22-24) | CORRECT | The shift maps `T_{L−1,a}` to `T_{0,a}` and `G_x` to `G_{x+1}`. |
| 11 | Ported results (26) | CORRECT | Each cited result exists as cited. `SGAP.md`'s (HF-alt)⇒(HF′) closure assumes (G1); Theorem 9 does not use that closure, so nothing unproved enters. |
| 12 | Slots and cell graph (30) | CORRECT | Degree four needs `L,n_s≥3`; both hold. |
| 13 | Histories and weight (32-34) | CORRECT | The draft's measure remark (draft line 141) is condensed into Theorem 2's proof; enough. |
| 14 | Shadow, polymers, labels, activities (36) | CORRECT | `m(γ)=0` for contractible `γ` follows from the definition but is not said; Theorem 3 uses it (edit E4). |
| 15 | Theorem 2, statement (38) | CORRECT | |
| 16 | Theorem 2 proof, Dyson step (40) | INCOMPLETE | A term bound proves the series converges, not that its sum is `e^{−β(A+B)}`. Missing: after `n` iterations the remainder has norm at most `(β sup_s‖e^{sA}Be^{−sA}‖)^n sup_s‖F(s)‖/n!→0`. Draft line 129 has it (edit E1). |
| 17 | Theorem 2 proof, factorization (42) | CORRECT | Re-derived. A run's outside neighbour cell is not in the shadow (it would join the component), so it is vacuum; component paths close; the event-set measure factorizes over disjoint bond-slot sets. |
| 18 | Theorem 3, statement (44-52) | CORRECT | |
| 19 | Theorem 3 proof, activity bound (54) | CORRECT | One step is implicit: touched cells number at most `2|J|` and `u≤1`, so `u^{|J|}v^{#untouched}≤(√u)^{#touched}v^{#untouched}≤φ^{|γ|}` (draft line 184). |
| 20 | Theorem 3 proof, parity and two-jump histories (56) | CORRECT | `j_{x−1}+j_x` even at each site, `L` even; the second move must hit the same bond (`L≥8`) and flavour (`ρ_a` distinct). |
| 21 | Theorem 3 proof, counting (56) | CORRECT | Depth-first closed walk of length `2(m−1)`; at most `4^{2(m−1)}` walks. |
| 22 | GAP in pass 1, corrected (58) | CORRECT | The GAP is real and the repair is complete; section 2. |
| 23 | `Z(Q)` (62) | CORRECT | |
| 24 | Theorem 4, statement (64-74) | CORRECT | The hypothesis lacks "for every `γ∈Q`" (edit E5). The ratio bound holds for any polymer, as Theorem 5 needs for winding `γ`. |
| 25 | Theorem 4, proof (76) | CORRECT | Re-derived in full. For `Z(S)≠0` with `S≠∅`, apply the deletion chain with some `γ∈S`, so that `S∩N[γ]≠∅`; draft line 218 says so. |
| 26 | Credit line (78) | CORRECT | Matches draft table row L1 (line 80), Fernández-Procacci eq. (2.13). Not load-bearing. |
| 27 | Theorem 5, statement (80-90) | CORRECT | |
| 28 | Theorem 5 proof, criterion (92) | CORRECT | `[check]` neighbour coefficient `0.0173232<1/50`. |
| 29 | Theorem 5 proof, winding sum and trace bounds (94) | CORRECT | Section 3.3 gives the leading-term computation the stated `ζ` bound needs. `[check]` `32x≤0.37698`. |
| 30 | Theorem 6, statement (98-102) | CORRECT | |
| 31 | Theorem 6, proof (104-108) | CORRECT | `[check]` `(e^{0.1}−1)/(2−e^{0.1})=0.11753`; coefficients `3.33746` and `7.06853`. |
| 32 | Remark after Theorem 6 (110) | CORRECT | At `ε=0` the exact cost is `14τ` (one odd site). |
| 33 | Theorem 7, statement (114) | CORRECT | |
| 34 | Theorem 7 proof, mirror and light parts (116) | CORRECT | Condensed; section 3.4 gives the full computation (draft line 236). |
| 35 | Theorem 7 proof, light sign (118) | CORRECT | Non-wrap hop sign `+1`; wrap hop sign `(−1)^{N−1}`. |
| 36 | Theorem 7 proof, second statement (120) | CORRECT | |
| 37 | Theorem 8, statement (122-126) | CORRECT | Wording: "the inequality is strict" should read "`e_p>e_{p_alt}`" (edit E6). |
| 38 | Theorem 8 proof, interpolation inequality (128-130) | CORRECT | Needs `Δw^{(2)}` defined (edit E3). |
| 39 | Theorem 8 proof, main term (132-134) | CORRECT | Re-derived: per non-wall bond `8βε²∫_0^{β−2d}e^{−28τs}ds`; an arc shorter than `(n_s−2)d` meets at most `n_s−1` slots; dropped pairs have positive weight. |
| 40 | Theorem 8 proof, error terms (136-142) | ERROR | Citation only. "For each anchor Theorems 3 and 4 give" is wrong: Theorem 4 plays no part. The count is in Theorem 3, where the distiller merged the draft's Lemma 4.4. Fix: "Theorem 3 gives" (edit E2). Both bounds hold: `[check]` `0.00523368`, `0.000244314`, sum `0.00547799<1/180`. |
| 41 | Theorem 8 proof, limit and constants (144-148) | CORRECT | `[check]` `τλ⁴/90=0.09216ε²/τ` at `|ε|=2·10⁻¹⁰τ`; `2/7−0.09216=0.19355≥1/6`. This arithmetic allows `c₀` up to `2.27·10⁻¹⁰`. |
| 42 | Theorem 9, statement (150-154) | CORRECT | |
| 43 | Theorem 9, proof (156) | CORRECT | Uses `c₀τ≤10⁻⁸τ≤R` without saying so (draft line 327; edit E7). |
| 44 | Scope paragraph (158) | CORRECT | |
| 45 | §7 scope paragraph (162) | CORRECT | Checked against `SGAP.md` lines 145, 147 and `SMG15.md` lines 158-160. |
| 46 | Open by name (164) | CORRECT | Draft lines 387-392 plus `SGAP.md` line 5's downstream list. |
| 47 | Arithmetic check (166) | CORRECT | Reproduced by this referee's `[check]`. |
| 48 | Recorded check, not reproduced (168) | CORRECT | Matches draft lines 355-372 (`L=4`, `ε=0.05τ,0.2τ`, gaps `13.5679τ`-`14.0200τ`, `9·10⁻¹⁷`, the breach). |
| 49 | Prior and literature scope (170-172) | CORRECT | Matches digest lines 16-19 and 49-53, and draft §2. |

`[check]` = `/tmp/toe-SGAP0ref/arith.py`, floating point, under a second, run at 56 percent free memory. It checks margins only.

## 2. The distiller's GAP: contractible polymers

`SGAP0.md` line 58: "After its Lemma 4.4, the draft says every contractible *polymer* has at least two cells. A singleton is a counterexample to that set-theoretic statement. It has zero activity by Theorem 3. Below `𝒬` contains only contractible polymers with at least two cells."

**The quoted draft text.** Draft line 197, right after Lemma 4.4: "Every contractible polymer has at least two cells (Lemma 4.3(ii): it has a jump, and a jump has two cells)." Draft line 256 repeats it inside the proof of Lemma 5.2(b): "Every contractible polymer has at least two cells. By Lemma 4.4 with `m_0=2`, ...". The distiller's location is right; the second place is not named, and the repair covers it.

**Verdict: the GAP is real.** Draft line 151 makes every nonempty connected cell set a polymer. A singleton `{c}` misses a slot, because `n_s≥4`, so it lies in the draft's `𝒫^c`. Lemma 4.3(ii) shows that a history with contractible shadow has a jump. That proves `w({c})=0`. It does not remove `{c}` from `𝒫^c`.

**What fails in the draft as written.** Lemma 5.2 puts `μ(γ)=λ²(ϑe^{1/8})^{|γ|}` on all of `𝒫^c`. Take `γ={c}`. Then `N[γ]` contains the five singletons at `c` and its four neighbours. They alone give `Σ_{γ′∈𝒫^c∩N[γ]}μ(γ′)≥5λ²ϑe^{1/8}=0.0654λ²`, which exceeds `λ²/50` for every `λ>0` (`ϑe^{1/8}=0.0130847`). So the draft's Lemma 5.2(b) is false as written.

**What survives without repair.** Condition (D) itself survives. Singletons have `w=0`, so (D) holds for them. For the others, the per-cell sum with singletons is at most `(0.01309+0.00347)λ²≤0.0166λ²`, so the sum over `N[γ]` is at most `0.083|γ|λ²≤|γ|/8`, and (D) follows as before. But the constant `λ²/50` enters `x`, every ratio bound `e^{|γ|λ²/50}`, Theorem A's coefficient and Theorem B's error sums. So the draft's chain needs the repair.

**The repair, checked.** Put `𝒬={γ contractible: |γ|≥2}`.

1. A family that contains a singleton has weight `0`. So `Z(S)=Z(S∩𝒬)` for every set `S` of contractible polymers, and Theorem 2's identity holds with `𝒬` in place of all contractible polymers.
2. On `𝒬`, the count of Theorem 3 starts at `m=2` and gives `Σ_{γ′∈𝒬,γ′∋c}μ(γ′)≤(λ²/16)y²/(1−y)≤0.00347λ²`. Five cells per cell of `γ` give the bound `|γ|λ²/50`.

An equivalent repair keeps all contractible polymers and sets `μ=0` on singletons; (D) holds there with both sides zero.

**Repaired statement.** "Every contractible polymer with nonzero activity has at least two cells; a contractible singleton has activity zero." *Proof.* A history whose shadow `γ` is contractible and nonempty has at least one jump: with no jump the path is constant, it is vacuum in the missing slot, so it is vacuum throughout and the shadow is empty. A jump on bond `x` in slot `k` puts the two distinct cells `(x,k)` and `(x+1,k)` in the shadow. `□`

`SGAP0.md` states exactly this (Theorem 3, line 52 and the end of line 56) and uses `𝒬` throughout sections 4-6. The GAP is closed in `SGAP0.md`.

## 3. Decisions on the points the lane names

### 3.1 The polymer expansion in imaginary time: CORRECT

**Slots.** With `d=1/(2τ)`, an excited cell with no jump costs `e^{−τe(χ)d}≤e^{−7}`, since `e≥14` off the vacuum. A bond-slot with at least one event costs, summed over events and eight flavours, `Σ_{n≥1}(8rd)^n/n!=e^{4r/τ}−1=u(r)`. Both numbers are as stated.

**Shadow components.** Distinct components of one cell set are disjoint and non-adjacent, so they form a compatible family. The referee re-derived the factorization (Theorem 2) in four steps.

1. *Restriction closes.* Let a maximal run of slots `k,…,k′` at site `x` lie in a component `Γ`, not the whole circle. The cell `(x,k−1)` is outside the shadow: inside, it would be adjacent to `(x,k)` and lie in `Γ`. So `x` is vacuum on `I_{k−1}` and no jump in that slot touches `x`; the same holds at `k′+1`. The restricted path is `1` at both ends of the run. It changes only at jumps inside the run, and those are jumps of `Γ`, because a jump's two cells are adjacent.
2. *Amplitudes split.* `T^p_{x,a}` acts on the two site factors only; `SGAP.md` line 68: "Products of site-even operators act on the corresponding ordinary tensor factors, including the wrap bond." So `ω_i` depends only on the two site states at the jump, where the restricted and full paths agree.
3. *Energy splits.* `∫H_0=τΣ_x∫e(χ_x(t))dt`, and vacuum contributes zero.
4. *Measure splits.* An event `(t,x,a)` in slot `k` lies in the bond-slot `(x,k)`. Different components own disjoint bond-slot sets. Lebesgue measure on finite event sets in a disjoint union of regions is the product of the measures on the regions.

**Labels.** At each time each non-vacuum site lies in exactly one component's cell. So `q` multiplies and `ν` adds. A contractible component is vacuum on a missing slot, and every active move preserves `(q,ν)`, so its labels are `(1,0)`.

**Cell-by-cell bound.** At most `16^{m(γ)}` configurations at a minimal slice; at most `2^{|γ|}` sets `J` of occupied bond-slots; for each `J`, `u^{|J|}v^{#untouched}≤φ^{|γ|}`. For contractible `γ`, `m(γ)=0`, every history has at least two jumps, and a two-jump history is a vacuum pair at a wall. Its weight is `ε²|⟨ρ_aρ_a|T_{b,a}|11⟩|²e^{−28τs}=ε²e^{−28τs}`, because `T_{b,a}` is Hermitian.

### 3.2 The rebuilt Dobrushin lemma: CORRECT

The induction claim is: for every `S⊂Q`, `Z(S)≠0`, and for every polymer `γ` the ratio bound holds. In the deletion chain `Z(S_{i−1})=Z(S_i)(1+z_i)`, the bound on `z_i` uses the claim for `S_i`, which no longer contains `γ_i`. So the product omits the self-factor. Dividing the hypothesis by `1+μ(γ_i)` gives `|z_i|≤μ(γ_i)/(1+μ(γ_i))<1`. Then `1/(1+z_i)=1+v_i` with `|v_i|≤|z_i|/(1−|z_i|)≤μ(γ_i)`. The derivative identity holds because `Z(Q)=Z(Q∖{γ})+w(γ)Z(Q∖N[γ])` is affine in `w(γ)`. Since `|w_s|≤max(|w_0|,|w_1|)`, the hypothesis holds for every `s` with one `μ`; so `Z_s≠0` on `[0,1]` and `d/ds log|Z_s|=Re(Z_s′/Z_s)`. This is the standard inductive argument. It is rebuilt in full, credited, and imports nothing.

### 3.3 Theorem A and the wrapping-polymer cost: CORRECT

**The cost of winding.** A winding polymer meets every slot, so `|γ|≥n_s` and `m(γ)≤|γ|/n_s`. Each meets slot `0`, which has `L` cells. With `x=θ_|ε|e^{λ²/50}`:

`ζ ≤ L Σ_{m≥n_s} 16^{m−1}·16^{m/n_s}·x^m = L(16x)^{n_s}/(1−16^{1+1/n_s}x) ≤ L(16x)^{n_s}/(1−32x)`.

The first term, `m=n_s`, is `16^{n_s−1}·16·x^{n_s}=(16x)^{n_s}`. The bound `16^{1/n_s}≤2` is used only in the ratio of successive terms. (Using it on every term gives only `(L/16)(32x)^{n_s}/(1−32x)`, which is weaker by `2^{n_s}/16`. The draft, line 258, shows the right form; `SGAP0.md` line 94 is consistent with it but does not show it.) So each slot of winding costs a factor `16x≤0.189`.

**The gap.** With `ζ≤0.1`, `Z_p^⊥/Z_p≤(e^ζ−1)/(2−e^ζ)≤1.2ζ`. With `Z_p^⊥≥e^{−βE_p^⊥}` and `Z_p≤16^Le^{−βe_p}`, dividing the logarithm by `β=n_s/(2τ)` and letting `n_s→∞` at fixed `L` gives `E_p^⊥−e_p≥2τ log(1/(16x))`. The prefactor `1.2·16^L·L/(1−32x)` disappears in the limit. The stated constants follow: `3.3τ` for `|ε|≤τ/120000`, and `7τ` for `|ε|≤10⁻⁸τ` `[check]`. The bound covers every light number, because `𝒱_p^⊥` contains every vector with `ν≠0`. At `ε=0` it gives `7.07τ`, below the exact `14τ`.

### 3.4 Theorem B and the Fock-space identity (draft Lemma 5.1 = `SGAP0.md` Theorem 7): CORRECT

**Lemma 5.1, re-derived.** For a closed sequence, `∏_iω_i=⟨χ⁰|T_n⋯T_1|χ⁰⟩`, because each `T_i` sends a basis vector to `ω_i` times one basis vector. Phases of basis vectors cancel in a closed product. Up to phase, the chain vector is `A_χB_n|0⟩`. Here `A_χ` is a polynomial in mirror modes that does not depend on `p`, and `B_n=∏_{x↑}(c_x†)^{n_x}`. `T_i=M_iΛ_i` with `M_i` even in mirror modes and `Λ_i=hop⁰` even in light modes, so all `M`'s commute with all `Λ`'s. An even operator commutes with every operator on disjoint modes. So the element is `⟨0|A_χ†MA_χ|0⟩·⟨n|Λ|n⟩`: the mirror operator `A_χ†MA_χ` is even and preserves every light occupation. The first factor does not depend on `p`. An active hop swaps unequal occupations with sign `+1` on a non-wrap bond and `(−1)^{N−1}` on the wrap bond. So the light factor is `(−1)^{(N−1)j_wrap}=1` when `j_wrap` is even.

**Why the hypothesis is needed.** In `p_alt` the even-count hypothesis can fail for a contractible history. Create `ρ_a`-pairs at bonds `(0,1),(2,3),…,(L−2,L−1)`, then remove them with flavour `a` at bonds `(1,2),…,(L−1,0)`. Every move is active, because both sites always have equal parity. Every bond is used once, and the wrap bond's light sign `(−1)^{N−1}` enters. The second statement of Theorem 7 excludes such polymers correctly: for `p≠±p_alt`, a polymer that sees no non-wall bond leaves some bond unused, so every bond count is even. Polymers that see a non-wall bond, the spatially wrapping ones included, go into the anchored error sums.

**Theorem B.** The interpolation inequality is exact bookkeeping on Theorem 4. The main term is `|NW(p)|·8βε²∫_0^{β−2d}e^{−28τs}ds`, which tends to `2ε²/(7τ)` per non-wall bond per unit time. That equals `SGAP.md` Proposition 4.2's coefficient. Each error is local at an anchor `(b,k)` and of order `λ⁴`. Per unit time it is at most `τλ⁴/90=(1.2·10⁵)⁴ε⁴/(90τ³)` per non-wall bond. The size of `c₀` comes from this: the error must stay below `(2/7−1/6)ε²/τ`, which holds up to `|ε|=2.27·10⁻¹⁰τ` `[check]`. The stated `2·10⁻¹⁰` is inside that range.

### 3.5 Corollary C (S-GAP⁰ with `Δ=7`): CORRECT

For `|ε|≤2·10⁻¹⁰τ≤10⁻⁸τ`, Theorem 6 puts every ground vector of `H_{p_alt}` in `𝒱_{p_alt}`. There `N=k(p_alt)=L/2` and `q=1`, so `E_1≤e_{p_alt}`. Every `E_σ` is a minimum over subspaces of the blocks, so `E_σ≥min_pe_p=e_{p_alt}` by Theorem 8. Hence `E_0=E_1=e_{p_alt}`. A `σ`-charged vector lies in `𝒱_p^⊥⊗C²` of its block, so `E_σ≥min_p(e_p+7τ)=E_0+7τ`. The quantifiers are those of `SGAP.md` Definition 4 with `t=0`: every `τ>0`, every allowed `L`, `|ε|≤c₀τ` with `ε=0` included, and every `σ≠1`. The extra claim, that for `ε≠0` every half-filled ground vector lies in `K_{p_alt}⊕K_{−p_alt}`, follows from `e_p>e_{p_alt}` for `p≠±p_alt`.

### 3.6 Constants: explicit and uniform in the ring length

Every constant is explicit: `d=1/(2τ)`, `R=τ/120000`, `v=e^{−7}`, `θ≤0.01155`, `μ`, `1/50`, `1/8`, `1/180`, `3.3`, `7`, `2·10⁻¹⁰` and `1/6`. None depends on `L` or `p`, and `τ` enters only by scaling. The `L`-dependent prefactors, `16^L·L` in Theorem 6 and the anchor count `|NW(p)|n_s` in Theorem 8, are removed by the limit `n_s→∞` at fixed `L`, or they appear as the factor `|NW(p)|` on both sides. So S-GAP⁰'s constants are uniform in `L`, as `SGAP.md` Definition 4 requires.

## 4. Check against the pass-1 source

Every result of `SGAP0.md` was matched to its source in `SGAP0_DRAFT.md`. The theorem statements and constants agree. The table lists every difference of content.

| Draft (`SGAP0_DRAFT.md` lines) | `SGAP0.md` | Difference |
|---|---|---|
| Fact 1.1, Fact 1.2 (58, 66) | Theorem 1 | None. |
| Lemma 4.1, Dyson (123-129) | Theorem 2 proof, first paragraph | The remainder estimate is dropped (item 16, edit E1). |
| Definition 4.1 and the measure remark (133-141) | §3, history paragraph; Theorem 2 proof | Condensed; nothing lost. |
| Lemma 4.2, Corollary 4.2′ (157-168) | Theorem 2 | Condensed. The draft's slot-boundary remark (line 163) is not needed: a jump exactly at a slot boundary is a null event. |
| Lemma 4.3, Lemma 4.4 (174-195) | Theorem 3 | Merged. One step left implicit (item 19); `m(γ)=0` not stated (item 14). |
| Line 197, repeated at 256 | GAP note (58) | The GAP; section 2. |
| Lemma 4.5, Corollary 4.6 (201-224) | Theorem 4 | Condensed; the hypothesis lost "for every `γ∈𝒬`" (edit E5). |
| Lemma 5.1, Corollary 5.1′ (230-240) | Theorem 7 | Condensed (item 34; optional edit E8). |
| Lemma 5.2 (250-261) | Theorem 5 | `𝒬` replaces all contractible polymers (the GAP repair). The leading-term step is condensed (optional edit E9). |
| Theorem A, Corollary A′ and remark (265-279) | Theorem 6 and line 110 | None. |
| Theorem B (283-317) | Theorem 8 | Citation slip "Theorems 3 and 4" (item 40, edit E2). Wording of the strict clause (edit E6). |
| Corollary C, Remark C.1 (321-331) | Theorem 9 | Remark C.1 moved into the statement. The step `c₀τ≤10⁻⁸τ≤R` dropped (edit E7). |
| §6.1-6.3 (333-349) | §7 | Condensed; faithful. |
| §6.4, Lean-formalizability (351) | absent | No loss of proof. The referee agrees with draft line 351: the steps are finite-dimensional linear algebra, finite sums, Lebesgue integrals over simplices and boxes, a finite induction, a continuous logarithm on `[0,1]`, and limits `n_s→∞` of explicit bounds. No step is computer-assisted. |
| §7 `[check]` (353-372) | "Recorded check, not reproduced" (168) | Faithful. |
| FINISH (376-398) | Status (3), Open by name (164) | Faithful. |

**Where the distillation added value.** It found the GAP and repaired it. It merged the draft's seventeen numbered facts, lemmas, corollaries, theorems and remark into nine theorems without changing a statement. It added no result and no constant.

**Pass-1 slips not carried into `SGAP0.md`.** None besides the GAP. The draft's other arithmetic was re-checked: `Σ_{m≥2}my^m=y²(2−y)/(1−y)²` (line 311); `2.304·10^{18}` (line 317); `2(7−ln32−3·10⁻⁸)τ≥7.06τ` (line 275).

**Cited source lines confirmed.** `SMG1.md` line 53: "`W` has spectrum `−14` once, `0` eight times in odd parity, and `2` seven times in even parity." This gives `e=0,14,16`. `SGAP_REFEREE.md` line 99 (N26): "Site-even operators at different sites commute, and on the subspace of fixed site parities they act as ordinary tensor factors. No Jordan-Wigner string appears, so the wrap bond needs no sign." This is the amplitude factorization of Theorem 2. It does not conflict with Theorem 7's wrap sign `(−1)^{N−1}`: that sign belongs to the mirror-first factorization of a closed product, not to a chain matrix element. `SMG15.md` line 138: "`PH_4Q(QH_MQ)⁻¹QH_4P=(2/(7τ))Σ_xΛ_x² P`". On `K_p` at `t=0` this is `(2/(7τ))walls(p)P`, the coefficient Theorem 8 recovers.

## 5. Required edits

E1-E7 are required. Each is a one-line text edit; none changes a statement, a constant or a quantifier. E8-E10 are optional; they make condensed steps self-contained.

- **E1 (item 16, line 40).** After "for `F(s)=e^{sA}e^{-s(A+B)}`." insert: "After `n` iterations the remainder is an integral of `B(s_1)⋯B(s_n)F(s_n)`, with `B(s)=e^{sA}Be^{−sA}`, over a simplex of volume `β^n/n!`; its norm is at most `(β sup_{s≤β}‖B(s)‖)^n sup_{s≤β}‖F(s)‖/n!→0`." Replace "The `n`th term has norm at most" by "After multiplication by `e^{−βA}` on the left, the `n`th term has norm at most".
- **E2 (item 40, line 136).** Replace "For each anchor Theorems 3 and 4 give" by "For each anchor Theorem 3 gives".
- **E3 (items 6, 38).** At the end of line 30 add: "Write `Z_p=Tr_𝓗e^{−βH_p}`, and `Π_p^⊥` for the orthogonal projector onto `𝒱_p^⊥`." In line 128, after "put `Δw=w_{p_alt}−w_p`", add "and `Δw^{(2)}=w^{(2)}_{p_alt}−w^{(2)}_p`".
- **E4 (item 14, lines 36 and 56).** After "Let `m(γ)` be the minimum number of cells in one time slice." add "Thus `m(γ)=0` for contractible `γ`." In line 56, end the sentence "The displayed bounds follow by extracting at least two or four powers of `|ε|/r`" with "and using `m(γ)=0`".
- **E5 (item 24, line 64).** Replace "Suppose nonnegative `μ(γ)` obey" by "Suppose nonnegative `μ(γ)`, `γ∈Q`, obey, for every `γ∈Q`,".
- **E6 (item 37, line 126).** Replace "For nonzero `ε` the inequality is strict unless `p=±p_alt`." by "For nonzero `ε`, `e_p>e_{p_alt}` unless `p=±p_alt`."
- **E7 (item 43, line 156).** Begin the proof with: "Since `c₀τ≤10⁻⁸τ≤R`, Theorem 6 applies with the bound `7τ`."
- **E8, optional (item 34, line 116).** Port the draft's computation (draft line 236): the chain vector is, up to phase, `A_χB_n|0⟩`, and the closed element equals `⟨0|A_χ†MA_χ|0⟩·⟨n|Λ|n⟩`.
- **E9, optional (item 29, line 94).** Show the leading term: "`ζ≤LΣ_{m≥n_s}16^{m−1}16^{m/n_s}x^m=L(16x)^{n_s}/(1−16^{1+1/n_s}x)`; then use `16^{1/n_s}≤2` in the denominator."
- **E10, optional (item 19, line 54).** After "At most `2|J|` cells are touched." add "Since `u≤1`, `u^{|J|}≤(√u)^{#touched}`, so each term is at most `φ(r)^{|γ|}`."

## 6. Open statements to carry, by name

- **S-GAP at `t≠0`** (OPEN, unchanged). Parity sectors mix and the light chain is gapless; the expansion needs every excitation gapped.
- **(G1) inside `𝒱_p`** (OPEN): a simple ground eigenvalue of `H_p` with a uniform gap inside `𝒱_p`. Not needed for S-GAP⁰.
- **Sharper constants** (open refinement, not a gap in the proof). This proof's own arithmetic caps `c₀` at `2.27·10⁻¹⁰` (Theorem 8) and gives at most `2τ(7−ln32)≈7.07τ` at `ε=0` (Theorem 6). Larger constants need different estimates.
- **A4's `W_odd≤Kw`** (OPEN; at `t=0` no longer needed).
- **Downstream, unchanged:** R1.5-U, R1.5-D beyond the `t=0` charged-gap subcase, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4.
- **Proposed readings, unchanged:** R15-SPEC and R-COR stay proposed and not adopted.

## 7. Freeze recommendation

**Recommendation: FREEZE `SGAP0.md` after edits E1-E7.** The one ERROR is a citation slip. The one INCOMPLETE item is a missing remainder sentence, supplied by draft line 129. The distiller's GAP is real and its repair is complete. Every theorem and every constant survived a hand re-derivation.

**What the frozen part would state.** All results hold for the frozen `t=0`, zero-electric-coupling ring of `SGAP.md`, conditional, as `SGAP.md` is, on the atom of `SMG1.md` Theorem 2.2 and the Gauss reduction of `SMG15.md` Theorem 2.

- Theorem 6 ((G1′)): `E_p^⊥−e_p≥3.3τ` for `|ε|≤τ/120000`, and `≥7τ` for `|ε|≤10⁻⁸τ`, for every allowed `L`, every `p` and every light number.
- Theorem 8 ((HF-alt) with `δ=0`): `e_p−e_{p_alt}≥(L−walls(p))ε²/(6τ)` for `|ε|≤2·10⁻¹⁰τ`.
- Theorem 9 (S-GAP⁰): `c₀=2·10⁻¹⁰`, `Δ=7`, with `E_0=E_1=e_{p_alt}`.

**Four-test check of the distiller's definitions.** `SGAP0.md` proposes no reading. Its six inferred definitions were still put through the four tests. (1) They fix no part's target: Definition 5 restates the targets of `SGAP.md` lines 20, 93 and 95 with the same quantifiers. (2) They are closed: every quantifier is bounded. (3) They settle no downstream question by premise: the restriction to `t=0` and zero electric coupling is inherited from `SGAP.md` Definition 1, which calls it "a restriction, not a derivation from the working set". (4) They add nothing the proof does not use: Definition 6's constants are proof devices, each used. Result: C, C, C, C. Nothing is adopted here.

**How it enters.** `SGAP.md` is frozen and lists S-GAP⁰, (G1′) and (HF-alt) as open or unproved. A change there goes by a dated amendment, which the lead or owner decides. This referee edits no file but this one.

## 8. Prior work used

| Prior result | Path | Use here |
|---|---|---|
| Prior-work digest | `prior/SGAP0.md` (commit `fa803749e`) | Map of prior work. Every item in it that bears on the proof was read. |
| Definitions 1-6; Theorems 1, 2, 4; Propositions 4.1-4.3; the (G1′) and (HF-alt) closures; Corollary 4.4; A4-A6 | `SGAP.md` lines 13-99 and 135-151 | The model and the targets; checks of `SGAP0.md` line 26 and §7. |
| Atom: spectrum `−14, 0, 2` with multiplicities `1, 8, 7` | `SMG1.md` Theorem 2.2, line 53 | The on-site energies `0, 14τ, 16τ`. |
| Gauss reduction `J:F_even⊗C²→H_G` | `SMG15.md` Theorem 2, lines 36-40 | Chain matrix elements equal Fock matrix elements (Theorem 7). |
| Atomic resolvent, `2/(7τ)` | `SMG15.md` Theorem 7, lines 136-140 | Theorem 8's main-term coefficient. |
| Routes 1-3 that failed | `SMG15.md` lines 155-160 | Check of `SGAP0.md` §7. |
| N26, site-even factorization | `SGAP_REFEREE.md` line 99 | Amplitude factorization in Theorem 2. |
| SMG1-GAP, bounded R-GEN | `TOE_ASSEMBLY.md` §3.10, line 261 | The judging standard. |
| Pass-1 draft | `SGAP0_DRAFT.md` (commit `f04958033`) | Source check, section 4. |
| Report format | `LW1_REFEREE.md` lines 1-80; `Y2W_DRAFT.md` lines 1-30 | Format only. |

**Not read.** The digest's main-branch notes E, Y, S, H (`ref/main/docs/…`) and the consolidation note C (`ref/pr10131/…`) were not read; no branch was fetched. No step of `SGAP0.md` uses them. `SGAP0.md` line 170 says: "Their hypotheses do not by themselves establish this comparison." A check of the proof does not need them.

**Prior work the digest missed.** A grep of this folder for "Dobrushin", "Kotecký", "Kotecky", "cluster expansion" and "polymer" finds mentions in `CN1MOD.md` (line 165, a proposed RG plan), `LW1.md` (line 482, a failed attack that names a missing Dobrushin-type bound), `RCS1_DRAFT.md`, `ZM1.md` and `LIT_HIGGS.md` (line 61, "Native rebuild: 15–30 pages for a controlled toy model", a proposal). None proves a cluster-expansion lemma. Nothing bears on this proof, and nothing needed porting.

**Extended here (referee closures, not new theorems).** The Dyson remainder step (edit E1); the leading-term computation of the winding sum (section 3.3); a contractible history in `p_alt` that uses every bond once, which shows that Theorem 7's even-count hypothesis does real work (section 3.4); the repaired statement for the GAP (section 2); the ceiling `2.27·10⁻¹⁰` on `c₀` set by the proof's own arithmetic.

---

## FINISH

**Proved (as checks of `SGAP0.md`; this report adds no theorem).**
- Theorems 1-9 of `SGAP0.md` are correct as stated, given edits E1-E7, none of which changes a statement. In particular:
  - Theorem 6, (G1′): `E_p^⊥−e_p≥3.3τ` for `|ε|≤τ/120000`, and `≥7τ` for `|ε|≤10⁻⁸τ`, for every allowed `L`, every `p` and every light number.
  - Theorem 8, (HF-alt) with `δ=0`: `e_p−e_{p_alt}≥(L−walls(p))ε²/(6τ)` for `|ε|≤2·10⁻¹⁰τ`.
  - Theorem 9, S-GAP⁰: `c₀=2·10⁻¹⁰`, `Δ=7`, and `E_0=E_1=e_{p_alt}`.
  - Every constant is explicit and uniform in `L`.
- The polymer expansion (Theorems 2-3), the rebuilt Dobrushin lemma (Theorem 4), the winding-polymer cost (Theorem 5), and the Fock-space identity (Theorem 7, draft Lemma 5.1) were each re-derived by hand.
- The distiller's GAP is real, and its repair is complete (section 2).

**Counterexamples.**
- One, to a pass-1 sentence. A contractible singleton polymer refutes draft line 197 ("Every contractible polymer has at least two cells"). With the draft's `μ`, it also refutes draft Lemma 5.2(b): `0.0654λ²>λ²/50` at a one-cell `γ`. The distiller found and repaired this.
- None to any statement of `SGAP0.md`, or to S-GAP⁰, (G1′) or (HF-alt).

**Open by name.**
- S-GAP at `t≠0`.
- (G1) inside `𝒱_p`.
- Sharper constants.
- A4's `W_odd≤Kw`.
- Downstream: R1.5-U, R1.5-D beyond the `t=0` charged-gap subcase, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4.

**What changes downstream.**
- If the lead applies E1-E7 and freezes `SGAP0.md`, then S-GAP⁰ is proved for `c₀=2·10⁻¹⁰`, `Δ=7` on the frozen `t=0` ring. The result is conditional on the atom and the Gauss reduction, as `SGAP.md` is. (G1′) and (HF-alt) are then proved at `t=0` on their ranges. `SGAP.md`'s status lines change only by a dated amendment, which the lead or owner decides.
- `SMG15.md` R1.5-D: the `t=0` charged-gap subcase is settled on that range. Decoupling at `t≠0` is unchanged.
- Under the owner's bounded R-GEN (SMG1-GAP), nothing changes. S-GAP⁰ is a finite-ring ingredient, not a GNS-generator gap, and `t=0` uniqueness already fails (`SGAP.md` Corollary 4.4).
- No axiom, law, frozen part, reading or working-set entry changes. Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
