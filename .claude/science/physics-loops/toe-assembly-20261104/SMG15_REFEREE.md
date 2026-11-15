lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SMG15 referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane (model id `claude-opus-5-5`, max effort) on the Mac mini, as pass 3 (the referee) under PR #10138's method. The lane brief's opening line calls the lane "pass-1"; its body assigns pass 3. This file is pass 3. Claude wrote pass 1 (`SMG15_DRAFT.md`). Codex gpt-6.1-terra wrote pass 2 (`SMG15.md`). This session wrote neither. This is one check: one whole-part, line-by-line read. No review of this review was commissioned. It grants no status, adopts no law, reading or axiom, and changes no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Text read.** `SMG15.md` at branch `claude/toe-assembly`, commit `a986b585a` (the last commit that touches it). SHA-256 `9064aa58866c09aba3eed0c73cf50a58928d189566854d4441b80eff58a14b17`. Line numbers below refer to that file.

**References consulted.** Listed in section 0 with commits and line ranges, as they were read.

**Method.** Every proof step was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-SMG15ref/` (under a minute, a few MB, dense matrices at most `2^{12}`, started only with at least 50 percent free memory). It guides and never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. The owner's choices of 2026-11-07 (`TOE_ASSEMBLY.md` section 3.10) are the frame: gap is read through bounded R-GEN for SMG1 rungs, W2.1 is kept, W2-LIGHT stays open. Owner guidance, verbatim: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms are read plainly.

**Counts.** 73 items: 61 CORRECT, 6 ERROR, 6 INCOMPLETE. Items 1-64 follow `SMG15.md`: 57 CORRECT, 4 ERROR, 3 INCOMPLETE. Items 65-73 are pass-1 claims the lane brief names, checked against `SMG15_DRAFT.md`: 4 CORRECT, 2 ERROR, 3 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. Referee closures: sections 2.5, 2.6 and 2.8.

---

## 0. Sources, working set and prior work

**Files read, at branch `claude/toe-assembly`, commit `a986b585a`.** Last-change commit in brackets.

| File | Commit | Lines read |
|---|---|---|
| `SMG15.md` | `a986b585a` | 1-170, all |
| `SMG15_DRAFT.md` | `6d1d35a49` | 1-318, all (SHA-256 `a58725e34b7637de294ed891ca607d347e43e79e1d64a03e77a7d2681b928125`) |
| `prior/SMG15.md` | `3bbb4ada7` | 1-84, all |
| `TOE_ASSEMBLY.md` | `47e819786` | 231-266 (sections 3.7-3.10) |
| `SMG1.md` | `24b2eca8a` | 3-9, 17-31, 39-79, 94, 106, 108, 120, 131-137, 141, 147-151 |
| `SMG1_REFEREE.md` | `40568088d` | 228-255 (sections 2.5-2.7) |
| `SMG1_OUTLINE.md` | `494ffe935` | 178-192 |
| `CH1.md` | `777e071c3` | 60, 80-84 |
| `CG16S.md` | `ea997b5c8` | 118-121 |
| `VC1_5.md` | `727ad9884` | 40-56 |
| `LW1_REFEREE.md`, `Y2W_DRAFT.md` | `5a2a0affe`, `92e03055c` | 1-80 and 1-25, for the format only |

Other branches are listed in section 0.1 as they were read. Long lines were read to their first 500-2500 characters.

**Working set used, by name.** GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` section 3.7). The three owner decisions of 2026-11-07 in section 3.10 are the frame: SMG1-GAP (bounded R-GEN), SMG1-W2.1 and SMG1-W2-LIGHT. PS-5 and PS-6r enter only through the rung-1 carrier of `SMG1.md`. The four smuggle tests are those of the lane brief. No other entry is used.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: finite-dimensional spectral theorem and min-max, geometric sums, Wick's rule and the determinant formula for quasi-free states, the GNS construction, Schur's lemma, weak convergence of asymptotically orthogonal unit vectors. Credited, never load-bearing: the Shale-Stinespring and Araki criteria for implementing Bogoliubov automorphisms. They are named in section 2.5 as one route to an open step. They are not used.

**The frame, quoted.** `TOE_ASSEMBLY.md` line 261: "For SMG1, fix the certified gate decomposition as part of the supplied data. Write \(g=e^{-iX_g}\), with \(X_g=X_g^*\) and \(\|X_g\|<\pi\). Set \(H_U=\sum_gX_g\) [...] A ground state satisfies \(\omega(A^*[H_U,A])\ge0\) for every local \(A\). A unique gapped ground state has GNS generator with kernel \(\mathbb C\Omega\) and spectrum contained in \(\{0\}\cup[\Delta,\infty)\) [...] Tick stationarity remains a separate requirement." Line 263 keeps W2-LIGHT open: "Require a fully stated replacement before claiming exclusion of every additional light sector." `SMG1.md` line 108 states owner question Q1: "Whether R-GEN is the intended notion of gap is owner question Q1." `SMG1.md` line 148 states Q2, on W2.1's protection of the whole 16. Section 3.10 answers both.

### Prior work used

| Prior result | Path | Use here |
|---|---|---|
| Code `C`, group `S`, atom spectrum `−14, 0, 2`, `ψ` even and `S`-fixed, `ρ_a` distinct | `SMG1.md` Lemma 2.1, Theorem 2.2 (lines 47-53) | Checks of Theorems 1, 3 and 7 |
| R-GEN, Definition 1.3, now adopted for SMG1's rungs as SMG1-GAP | `SMG1.md` line 21; `TOE_ASSEMBLY.md` line 261 | The frame; items 8, 45, 59; sections 2.1, 2.8 |
| Lemma G0, principal generators | `SMG1.md` line 27 | Items 28, 45; sections 2.2, 2.6 |
| Theorem 3.1 and its one-site-translation remark | `SMG1.md` lines 61-65 | Item 39 |
| Theorem 4.1: zero-hop uniqueness uses `τ_E > 0` | `SMG1.md` lines 75-77 | Item 71 and section 2.10 (a pass-1 sentence that pass 2 dropped) |
| Lemma M | `SMG1.md` line 137; `SMG1_REFEREE.md` §2.6 | Items 44, 49; section 2.6 |
| Fröhlich-Pizzo hypotheses (1.4), (1.6), (1.7), quoted | `SMG1_REFEREE.md` §2.5 | Item 57; section 2.9 |
| The conjugated tick and decomposition dependence | `SMG1_REFEREE.md` §2.7 | Item 45; section 2.6 |
| F3 (1D clause) and K1's limits | `CH1.md` lines 60, 84 | Item 60 |
| RC-W, stated on `ℓ²(Z³)⊗C^n` | `CG16S.md` lines 118-120 | Items 60, 73 |
| Gauge average `E`; purity on invariants is equivalent to extremality among gauge-invariant states | `VC1_5.md` Theorem 2.1 (line 48) | Section 2.5 |

**Missed by the digest.** (i) `VC1_5.md` Theorem 2.1. It restates the purity GAP as extremality among gauge-invariant states on the full algebra. (ii) `TOE_ASSEMBLY.md` section 3.10. It postdates the digest. It answers SMG1's Q1 and Q2, which `SMG15.md` still lists as open.

### 0.1 Other branches and checks

`origin/main` at `f5af11cd0` (`git fetch -q origin main`; read with `git show` only). Note `S` (`docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`, last changed `4d0cd77bd`): lines 7, 30, 32, 235, 239, 256, 293, 297, 443, 484, found by grep for the phrases `SMG15.md` line 140 and line 152 report. They match: line 256 "At this order the induced term is a constant"; line 293 "a nonzero attractive density interaction"; line 32 "Its coefficient is not imported into the refined atom"; line 235 "the bound retains v's volume dependence"; line 7 "conditional-support". Notes `H` and `C` were not read. `SMG15.md` cites them only as digest reports, and no step rests on them.

`[check]` `/tmp/toe-SMG15ref/check.py`, run with 59 percent free memory, 1.3 s, peak 109 MB, largest matrix 1024 x 1024. (A) Theorem 4: `cos ε(q)` formula to `6·10⁻¹⁶`; `r|G(r)|` at `r=25,50,100,200` is `0.1491, 0.1505, 0.1513, 0.1517` against `|cos t₀|/2π = 0.1521` for `t₀=0.3`, and agrees likewise for `t₀=0.7, 1.2`. (B) Theorem 7 on one open bond with the `SMG1.md` generators: `W` spectrum `−14, 0, 2` with multiplicities `1, 8, 7` per site; `PH₄P=0`; the identity holds to `10⁻¹⁶` in case I and in case II for both `Λ`. Case II was run without its link factor; this changes no product, since `Z_ℓ²=1` and `Z_ℓ` commutes with every other factor. (C) Theorem 3: `E₀`, the `w=+1` minimum, both gaps and the two-point function agree to `3·10⁻¹⁵` for `L=8,12,16,24`. (D) The half-filled sea's parity string `det(1−2C_I)` is `0.208, 0.104, 0.052, 0.026` for `|I|=8,32,128,512`, below the bound `exp(−2 tr(C_I−C_I²))` of section 2.5. These guide only.

---

## 1. Verdict table

Items 1-64 follow `SMG15.md` line by line. Items 65-73 are pass-1 claims the lane brief asks about, checked against `SMG15_DRAFT.md`.

| # | Item (`SMG15.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Status (3) | ERROR | "Theorems 1–6 prove [...] second-order identities": the second-order identity is Theorem 7 and the tick result is Theorem 4. Fix: "Theorems 1–7". |
| 2 | GAPs paragraph (5) | CORRECT | Each GAP is real (items 11, 35, 38, 48, 52, 56). |
| 3 | Open list (7) | ERROR | Q1 and Q2 were answered on 2026-11-07 (`TOE_ASSEMBLY.md` lines 261-262). Fix in E2. |
| 4 | Provenance (9) | CORRECT | Matches the draft's cap-breach report (draft line 7). |
| 5 | Definition 1 (15) | CORRECT | |
| 6 | Definition 2 (16) | CORRECT | Matches `SMG1.md` lines 39-53. `[check B]` |
| 7 | Definition 3 (17) | CORRECT | The reflection's sign needs even `L` (`SMG1.md` line 77); `L∈4N` gives it. |
| 8 | Definition 4 (18) | ERROR | "Q1 asks whether to accept it" is out of date: the owner adopted bounded R-GEN for SMG1's rungs (SMG1-GAP). Fix in E3. |
| 9 | Definition 5 (19) | CORRECT | |
| 10 | Definition 6 (20) | CORRECT | |
| 11 | R15-SPEC and its caveats (24) | INCOMPLETE | Both caveats are right. The four tests must be re-read against section 3.10 (section 2.8). |
| 12 | R-COR (26) | INCOMPLETE | Under SMG1-GAP its clause (C2) is a second meaning of "gapped" (section 2.8). |
| 13 | Theorem 1, statement (30) | CORRECT | |
| 14 | Theorem 1, proof (32) | CORRECT | The local-group average equals `Σ P^χ H P^χ` by character orthogonality. |
| 15 | Theorem 2, statement (34-40) | CORRECT | |
| 16 | Theorem 2, proof (42) | CORRECT | Wrap case re-derived: the base label flips. |
| 17 | Paragraph after Theorem 2 (44) | CORRECT | Wording: "undressed charged bilinear" should read "undressed gauge-variant bilinear"; "charged" means `S`-charged elsewhere. |
| 18 | Data of section 3 (48-58) | CORRECT | `R(K_x)=K_{−x}` uses `t(χ,χ′)=t(χ′,χ)`; `t₀=t−14ε`, `δ≤16\|ε\|` checked. |
| 19 | Theorem 3: conservation, block form (60) | CORRECT | |
| 20 | Theorem 3: `E₀`, the `w=+1` minimum (62) | CORRECT | `[check C]` |
| 21 | Theorem 3: bound `E₀+m(14τ−2δ)` (64) | CORRECT | |
| 22 | Theorem 3: the `δ<7τ` clauses (64) | CORRECT | Canonical (fixed `N`); see section 2.8 for the grand-canonical reading of SMG1-GAP. |
| 23 | Theorem 3: `J²` levels, two gaps (64) | CORRECT | No threshold condition is needed: free eigenvectors of the trivial block are eigenvectors of `H_A`. |
| 24 | Theorem 3: symmetry, two-point function, charged correlations (66) | CORRECT | `[check C]` |
| 25 | Theorem 3, proof, first paragraph (68) | CORRECT | |
| 26 | Theorem 3, proof, second paragraph (70) | CORRECT | Order mirror modes before light modes; even light operators then act as `1⊗ℓ` on every configuration, so the reduced light space and hop do not depend on `χ⃗`. |
| 27 | Paragraph (72) | CORRECT | |
| 28 | Tick set-up (76) | CORRECT | `L_site` puts a gate on every site; with pairwise disjoint edge triples it is two NN-a layers, as in `SMG1.md` line 45. R-GEN is unchanged. |
| 29 | Theorem 4: conservation, trivial block (78) | CORRECT | |
| 30 | Theorem 4: bands and range (78-80) | CORRECT | `[check A]` |
| 31 | Theorem 4: touching only at `q=π` (82) | CORRECT | `q=π` needs `L/4+1/2∈Z`. |
| 32 | Theorem 4: `Ω_tick`, stationarity, symmetry (82) | CORRECT | `N=L/2` is even, so the reduced vector lies in `F_even`. |
| 33 | Theorem 4: modulus `\|cos t₀\|/(2πr)+O(r⁻²)` (82) | CORRECT | Jump and integration by parts re-derived. `[check A]` |
| 34 | Theorem 4, proof (84-86) | CORRECT | |
| 35 | GAP R-COR-purity (88) | CORRECT | The GAP is real. Referee reduction and a counterexample to the missing inference in section 2.5. |
| 36 | Theorem 5, statement (92-96) | CORRECT | |
| 37 | Theorem 5, proof (98) | CORRECT | `TUT*=Ue^{−2πiN/L}`, the window identity, `d_r=⌊(r+1)²/4⌋` and `C_h` re-derived. |
| 38 | Corollary 5.1 and proof (100-102) | CORRECT | |
| 39 | Remark after Theorem 5 (104) | INCOMPLETE | "are essential hypotheses" asserts necessity, which is not shown. Fix: "The proof uses". The rest is right; `SMG1.md` Theorem 3.1 is as described. |
| 40 | Operators `D_x` (108) | CORRECT | `D_x` is anti-Hermitian, commutes with every `P_y`, needs no link string; `R(D_x)=D_{−x}`. |
| 41 | Theorem 6: support, symmetries, sector spectra (110) | CORRECT | Six sites: a bond term on `(x,x+1)` with `x` odd grows to `[x−2,x+3]`. |
| 42 | Theorem 6: "S1–S3 hold with the same constants" (110) | CORRECT | True of the operator `H^ε`. Scope: `H^ε` is not the R-GEN generator of any NN-a decomposition for small `ε≠0` (referee closure, section 2.6). |
| 43 | Theorem 6: tick, stationary ray, charged correlations (110) | CORRECT | |
| 44 | First-order degree-four part (112-116) | CORRECT | Commutator re-derived; the three-site monomials are independent. |
| 45 | R-GEN assigns `H_A` (116) | CORRECT | Wording: drop "proposed" (E3). |
| 46 | Theorem 6, proof (118-120) | CORRECT | |
| 47 | Small-`ε` persistence of the `1/r` law (122) | CORRECT | Charge counting forces an odd number of cross contractions, so every correction carries a `1/r` factor. |
| 48 | Correction to pass 1 (124) | CORRECT | Section 2.6. |
| 49 | Set-up of section 7 (128) | CORRECT | |
| 50 | Theorem 7, statement (130-134) | CORRECT | `[check B]` |
| 51 | Theorem 7, proof (136) | CORRECT | Distinct configurations need `L≥3`; rings have `L≥8`. |
| 52 | Paragraph (138) | CORRECT | |
| 53 | Paragraph (140) | CORRECT | Quotes verified at `f5af11cd0` (section 0.1). |
| 54 | S-GAP (144-148) | CORRECT | A well-posed open statement in `t/τ`, `ε/τ`. The `t=0` remark is right. |
| 55 | Route 1, local Schrieffer-Wolff (152) | CORRECT | Fails at the named step (section 2.9). |
| 56 | Route 2, absolute polymer expansion (153) | CORRECT | Fails for the named representation (section 2.9). |
| 57 | Route 3, Fröhlich-Pizzo (154) | CORRECT | Fails at hypothesis (1.4) (section 2.9). |
| 58 | R1.5-U, R1.5-D (156) | CORRECT | |
| 59 | Other open items (158) | ERROR | Q1, Q2 as in item 3. W2-LIGHT stays open (owner). |
| 60 | Prior results (162) | CORRECT | `SMG1.md` Theorem 4.1 has `\|0⟩_{5,x}`; F3 has the 1D clause; RC-W is stated on `ℓ²(Z³)⊗C^n`. |
| 61 | Digest paragraph (164) | CORRECT | A report. |
| 62 | Literature paragraph (166) | CORRECT | A report; no step rests on it. |
| 63 | Even-separation remark (168) | CORRECT | `sin(πr/2)=0` for even `r`. |
| 64 | Pass-1 checks (170) | CORRECT | A report; items 30, 33, 50 rerun here. |
| 65 | Draft Theorem A (A1)-(A6) | CORRECT | Pass 2 is faithful. Pass-1 slip not carried: (A2) writes `Ω_A=J(ψ^{⊗L}⊗Φ_F⊗e_{−1})`, but `e_{−1}` is Lemma 2's `s=−1` vector; the `w=−1` vector is `(e_{+1}−e_{−1})/√2`. |
| 66 | Draft Proposition A′ (e), "(C1) holds" | INCOMPLETE | Purity in infinite volume is missing (item 35). |
| 67 | Draft Theorem B scope: "What remains open for generic mixing is (S1) and (S3), not (S2)" | ERROR | Theorem B gives one low state, not S2's growing count; the draft's own previous sentence says so. Pass 2 line 104 is right. |
| 68 | Draft Theorem C (c), (e) and the two counterexamples | CORRECT | With the scope of item 42. |
| 69 | Draft Proposition D (D1)-(D3) and its reading | CORRECT | (D1)-(D3) re-derived. "Marginal" is power counting, not proved, and no step uses it. "all induced terms vanish to every order" is not implied by unitary equivalence (item 48); it holds through order `ε³` and is open beyond (section 2.6). |
| 70 | Draft attacks 1-3 on S-GAP | CORRECT | As narrowed by pass 2: the draft's "no Kotecký–Preiss-type criterion holds" and "no reduction of this kind can exist" overreach (section 2.9). |
| 71 | Draft: "R1.5's light chain should take `τ_E=0`" (0.1, line 123) | INCOMPLETE | Not proved (section 2.10). The draft's sentence on `SMG1.md` Theorem 4.1 is false; pass 2 dropped it. |
| 72 | Draft: Golterman-Shamir "bites first at R2" (0.1, 3.7) | INCOMPLETE | Not proved (section 2.10). Pass 2 line 166 states the defensible part. |
| 73 | Draft: "RC-W (`CG16S.md` line 120) gives it zero winding" (3.7) | ERROR | RC-W is a `W₃` statement on `ℓ²(Z³)⊗C^n`. The 1D fact follows from `det u(q)=1`. Pass 2 line 162 is right. |

---

## 2. Decisions, GAPs and referee closures

### 2.1 The owner decisions of 2026-11-07 (items 1, 3, 8, 45, 59)

`TOE_ASSEMBLY.md` section 3.10 adopts three texts for SMG1's rungs. SMG1-GAP adopts bounded R-GEN (line 261, quoted in section 0). SMG1-W2.1 keeps W2.1 (line 262). SMG1-W2-LIGHT keeps W2-LIGHT open (line 263). `SMG1.md` line 108 asks Q1: "Whether R-GEN is the intended notion of gap". SMG1-GAP answers it for SMG1's rungs, and R1.5 is one of them. `SMG1.md` line 148 asks Q2, whether W2.1 protects the whole 16 by exact `G`. SMG1-W2.1 answers it. `SMG15.md` still lists Q1 and Q2 as open (lines 7, 158) and calls R-GEN "proposed" (lines 18, 24, 76, 116). Edits E2 and E3 update these lines. W2-LIGHT stays open, as `SMG15.md` says.

### 2.2 Theorem 3, pass 1's Theorem A: decision

**Decision: CORRECT.** Every clause was re-derived (items 19-27) and checked numerically on `L=8,12,16,24` (`[check C]`). The R-GEN status is exact. Each gate of `U_A` is principal when `16τ<π` and `max‖κ_x(χ,χ′)‖<π`: `K_x` is block-diagonal in configurations, so `‖K_x‖=max‖κ_x(χ,χ′)‖`, and Lemma G0 applies. The R-GEN sum is `H_A`. So Theorem 3 is a statement about SMG1-GAP's generator, on finite rings, at the fixed filling `N=L/2`. Section 2.8 gives its infinite-volume and grand-canonical reading.

One point in the proof (item 26) deserves a sentence. On a configuration with odd mirror lines, one might fear configuration-dependent signs on the reduced light hop. There are none. Order all mirror modes before all light modes. Then an even light operator `ℓ` acts on `m⊗φ` as `m⊗ℓφ`, for every mirror vector `m`. So the reduced light space and the reduced hop are the same on every configuration, as the proof states.

### 2.3 Theorem 4, pass 1's Proposition A′: decision

**Decision: CORRECT on finite rings, and for the thermodynamic limit of the dressed two-point function.** The band formula, the touching at `q=π`, the exclusion of `π` at `w=−1`, the eigenvector property and the jump `|cos t₀|` were re-derived (items 29-34). The coefficient `|cos t₀|/(2π)` agrees with `[check A]`. Pass 1's further claim that `(U_A, Ω_tick)` meets R-COR (draft line 188) is not established, because purity of the infinite-volume state is missing (section 2.5). The light walk's one-dimensional winding is zero for a direct reason: `det u(q)=1` for every `q`. This replaces the draft's appeal to RC-W (item 73).

### 2.4 GAP "R15-SPEC does not itself exclude all extra light fields": real

**The GAP is real.** S1-S3 count levels and bound the `S`-charged spectrum. None of them speaks about the field content of the `S`-trivial low-energy sector. The target's phrase "exclude all extra light fields" has no fixed meaning while W2-LIGHT is open. The owner's text says: "Require a fully stated replacement before claiming exclusion of every additional light sector" (`TOE_ASSEMBLY.md` line 263). So no reading of "gapped" and "gapless" can discharge it.

**Repaired statement, for `SMG15.md` line 24.** "R15-SPEC reads 'gapped' and 'gapless' only. For the family of Theorem 3, every level below `E₀+14τ−2δ` is a level of the free half-filled ring, with both holonomies (Theorem 3, exact on finite rings). Whether this counts as 'no extra light fields' is W2-LIGHT, which the owner keeps open."

The GAP's last sentence, "Uniqueness at finite `L` alone does not rule out thermodynamic symmetry breaking", is a correct non-implication. Section 2.5 gives a mechanism in this carrier: a holonomy eigenvector averages two link sectors, and its infinite-volume limit can be a mixture.

### 2.5 GAP R-COR-purity (item 35): real; referee reduction to one named statement

**The GAP is real, and not a formality.** `SMG15.md` line 88: "Finite-volume purity alone does not imply purity of a weak limit." Here is a counterexample in this carrier. Take the zero-hop terms of `SMG1.md` with `τ_E=0` and the light mode empty. On `Z_L` put `Ψ_w := J(ψ^{⊗L}⊗|0⟩⊗(e_{+1}+we_{−1})/√2)`, `w=±1`. Each `Ψ_w` is a unit vector in `H_G`, an eigenvector of the holonomy, invariant as a ray under `S`, `U(1)_5`, `T²` and `R`, and fixed by `L_site`. All site parities are `+1`, so `J(Φ⊗e_s)` has `X_ℓ=s` on every link. For a local `A∈𝔄^G` away from the wrap, `J*AJ=A₀⊗1+A₁⊗σᶻ` (step 1 below), and `⟨σᶻ⟩=0` in `(e_{+1}+we_{−1})/√2`. So the limit state is `(ω_{+}+ω_{−})/2`, where `ω_s` is the product state with `X_ℓ=s` on every link. Each `ω_s` satisfies Gauss's law, and `ω_{+}(X_0)=1≠−1=ω_{−}(X_0)`. So the limit is not pure. The same averaging occurs for every holonomy eigenvector. Purity of the limit of `Ω_tick` therefore needs an argument that uses the gapless light state.

**Notation.** `𝔄` is the quasi-local algebra on `Z`; `𝔄^G` its elements commuting with every `G_x`. `G′_x := P^5_xX_{x−1}X_x` is the light-and-link Gauss operator, and `𝔄^{G′}_5` the light-and-link elements commuting with every `G′_x`. `Π` is the infinite-volume lower-band projector on `ℓ²(Z)`, the Fourier multiplier of Theorem 4. It is a projection, because `Π(q)` is a rank-one projection for every `q≠π`. `ω_Π` is the quasi-free state on the light CAR algebra with `ω_Π(a*(f)a(g))=⟨g,Πf⟩`; `CAR⁺` is its even part. For a light monomial `μ` of even degree, `a_ℓ(μ)` is its number of factors at sites `≤ℓ`, mod 2, and `D(μ):=μ∏_ℓZ_ℓ^{a_ℓ(μ)}` is the dressed monomial. `Θ_L` is the automorphism of `CAR⁺` that multiplies `μ` by `(−1)^{a_0(μ)}`: conjugation by the parity of the left half-line.

**Step 1 (referee closure): the limit exists, is stationary and is invariant.** Expand a local `A∈𝔄^G` in matter Majorana monomials times link Pauli monomials `∏Z_ℓ^{a_ℓ}X_ℓ^{b_ℓ}`. Conjugation by `G_x` multiplies a term by `(−1)^{deg_x+a_{x−1}+a_x}`. Invariance forces `a_ℓ=Σ_{y≤ℓ}deg_y` mod 2 and even total degree. So `A=Σc_{μ,b}D(μ)X^b`, now with `μ` a matter monomial. Place `A` on `Z_L` with its support far from the wrap bond. Lemma 2 gives `J*D(μ)J=μ⊗1` and `J*X_ℓJ=(∏_{base<y≤ℓ}P_y)⊗σᶻ`. A product of an even number of `X`s is a local product of parities. So `J*AJ=A₀⊗1+A₁⊗σᶻ`, with `A₀` a local matter operator independent of `L`. At holonomy `w=−1`, `⟨σᶻ⟩=0`. Hence `ω_L(A)=⟨ψ^{⊗L}⊗Φ_L,A₀ψ^{⊗L}⊗Φ_L⟩`. The mirror factor is a product. The light factor is a finite determinant of two-point values, and these converge as Riemann sums on a grid avoiding `π` (item 33). So `ω(A):=lim_Lω_L(A)` exists and defines a state on `𝔄^G`. For `L` large the tick acts on `A` through bulk gates only, so `ω∘α=ω` follows from `U_AΩ_tick∝Ω_tick`. Invariance under `S`, `U(1)_5`, `T²` and `R` follows the same way. In particular `ω(X_0C)=0` for every `C` built from dressed monomials.

**Step 2 (referee closure): the mirror factors out.** `P^1_x` is an even mirror operator, so it lies in `𝔄^G`, and `ω(P^1_x)=1`. Let `φ≤λ^{−1}ω` be a state. Then `φ(P^1_x)=1`, and Cauchy-Schwarz gives `φ(A)=φ(P_FAP_F)` for `P_F:=∏_{x∈F}P^1_x`, `F⊇supp A`. Since `P^1_x` has rank one on the mirror, `P_FAP_F=P_F𝔼(A)`, where `𝔼` replaces each mirror factor on `F` by its `ψ^{⊗F}`-expectation. `ψ` is even, so `𝔼(A)` commutes with every `G′_x` and lies in `𝔄^{G′}_5⊂𝔄^G`. Hence `φ=φ∘𝔼`. Also `φ(G′_x)=φ(P^1_xG_x)=1`. So `ω` is pure on `𝔄^G` if `ω|𝔄^{G′}_5` is pure.

**Step 3 (referee closure): structure under Gauss's law.** `D(μ)D(ν)=D(μν)` and `D(μ)*=D(μ*)`, because link `Z`s commute with matter and `a_ℓ` is additive. Let `𝒞` be the C*-algebra generated by the `D(μ)`. On each finite-dimensional local algebra of `CAR⁺`, the map `μ↦D(μ)` is a *-homomorphism, and it is injective because distinct monomials stay linearly independent. An injective *-homomorphism of C*-algebras is isometric, so the map extends to an isomorphism `CAR⁺≅𝒞`. `X_0` anticommutes with `Z_0` only, so `X_0D(μ)X_0=(−1)^{a_0(μ)}D(μ)`: conjugation by `X_0` is `Θ_L` on `𝒞`. Next, `∏_{ℓ<y≤ℓ′}G′_y=(∏_{ℓ<y≤ℓ′}P^5_y)X_ℓX_{ℓ′}`. In any state `φ` with `φ(G′_x)=1`, Cauchy-Schwarz gives `φ((G′_x−1)B)=0`. So every `X`-monomial may be replaced by `X_0^{0 or 1}` times a product of parities in `𝒞`. Hence such a `φ` is fixed by its values on `𝒞` and on `X_0𝒞`.

**Step 4 (referee closure): `ω_Π|CAR⁺` is pure.** Let `𝒦:={a(g):g∈ran(1−Π)}∪{a*(h):h∈ranΠ}`. In the Fock representation of `Π` every `k∈𝒦` annihilates the vacuum. The elements of `𝒦` anticommute pairwise, and `{k,k′*}` is a scalar. Every `a(f)` is a sum of an element of `𝒦` and one of `𝒦*`. So even polynomials in `𝒦∪𝒦*` are dense in `CAR⁺`, and normal ordering writes them as combinations of `k′₁*⋯k′_p*k₁⋯k_q` with `p+q` even. Let `φ≤λ^{−1}ω_Π` be a state on `CAR⁺`. For odd `Y` and `k∈𝒦`, `Yk∈CAR⁺` and `φ((Yk)*(Yk))≤λ^{−1}ω_Π(k*Y*Yk)=0`. So `π_φ(Yk)Ω_φ=0`. If `q≥1`, the monomial is `Yk_q` with `Y` odd, and its `φ`-value is `0`. If `q=0<p`, take the adjoint. So `φ=ω_Π` on a dense set, hence everywhere.

**Step 5 (referee reduction).** *Lemma P-red.* If `Θ_L` is not unitarily implementable in the GNS representation `(K,π₊,Ω)` of `ω_Π|CAR⁺`, then `ω` is pure on `𝔄^G`.

*Proof.* Let `ω=λφ₁+(1−λ)φ₂`. By step 2 and `φ_i(G′_x)=1`, it suffices to show `φ_i=ω` on `𝒞` and on `X_0𝒞`. Step 4 and step 3 give `φ_i|𝒞=ω|𝒞`. Suppose `φ_i(X_0C)≠0` for some `C∈𝒞`. In the GNS space of `φ_i`, let `K_i` be the closure of `π(𝒞)Ω_i`; it carries a copy of `π₊`, irreducible by step 4. Put `T:=P_{K_i}π(X_0)|_{K_i}`. Then `Tπ(C)=π(Θ_L(C))T` for `C∈𝒞`, and `φ_i(X_0C)=⟨Ω_i,Tπ(C)Ω_i⟩`, so `T≠0`. Taking adjoints gives `π(C)T*=T*π(Θ_L(C))`. So `T*T` and `TT*` commute with `π(𝒞)`. By Schur's lemma both are the same positive scalar `c`. Then `T/√c` is a unitary implementing `Θ_L` in `π₊`, a contradiction. So `φ_i(X_0C)=0=ω(X_0C)`. ∎

**The remaining step, named P3.** *P3:* `Θ_L` is not unitarily implementable in the GNS representation of `ω_Π|CAR⁺`. It is not proved here. Two facts bear on it. (i) A necessary condition for purity holds. A pure state on a quasi-local algebra clusters (Powers), so purity needs `ω(X_0X_n)→0`. Here `ω(X_0X_n)=ω_Π((−1)^{N_{(0,n]}})=det(1−2C_I)`, with `C_I` the compression of `Π` to `I=(0,n]`. Each eigenvalue `λ∈[0,1]` of `C_I` obeys `|1−2λ|≤e^{−2λ(1−λ)}`. So `|det(1−2C_I)|≤exp(−2Σ_{u∈I,v∉I}|Π(u,v)|²)`. The `1/r` tail of item 33 makes the sum grow like `log n`. So the strings decay (`[check D]`). (ii) The same tail gives `Σ_{x≤0<y}|Π(x,y)|²=∞`, because `y−x=d` occurs for `d` pairs, each of size about `d^{−2}`. By the Shale-Stinespring criterion, and Araki's version for the even part, this divergence is the obstruction to implementability. Those theorems are credited and not rebuilt, so P3 stays open. `VC1_5.md` Theorem 2.1 gives an equivalent form of the target: purity on `𝔄^G` is extremality of `ω∘E` among gauge-invariant states on `𝔄`.

**Repaired text for `SMG15.md` line 88.** "GAP R-COR-purity. The infinite-volume limit of `Ω_tick` exists on the gauge-invariant algebra, is stationary, and is `S`-, `U(1)_5`- and cell-invariant. It is pure if P3 holds (`SMG15_REFEREE.md` §2.5, Lemma P-red). P3 is open. Finite-ring purity does not suffice: holonomy eigenvectors of the empty light chain have a mixed limit."

### 2.6 Theorem 6, pass 1's Theorem C: decision, and what R-GEN sees

**Decision: CORRECT as mathematics (items 40-48), with a scope edit under SMG1-GAP.** The gates `e^{εD_x}` are even, commute with every `P_y` and need no link string. Each conjugation layer grows a support by one site per side. The degree-four part at order `εt₀` and the commutator `[hop⁰_x,hop_{x+1}]=Z_{x+1}(c_x†c_{x+2}−c_{x+2}†c_x)` were re-derived. Sector spectra agree because `V_ε` commutes with `N`, every `G_y` and every `U_g`. The R-GEN cancellation is exact: the principal generators of `e^{εD_x}` and `e^{−εD_x}` are `iεD_x` and `−iεD_x` when `8|ε|<π`.

**Referee closure: `H^ε` is not an R-GEN generator.** *Claim.* Let `t₀≠0`. For each ring there is `ε₀>0` such that, for `0<|ε|<ε₀`, `H^ε` is not of the form `Σ_gX_g` with every `X_g` in the algebra of one edge triple. So no certified NN-a decomposition of any tick has R-GEN generator `H^ε`.

*Proof.* Each `X_g` is the principal logarithm of its gate (Lemma G0), a function of the gate, so it lies in the algebra of the gate's triple. Let `𝒱` be the span of these triple algebras. Expand operators in the basis of matter Majorana monomials times link Pauli monomials. `𝒱` is spanned by the basis elements supported in one triple. Let `π_⊥` be the coordinate projection onto the other basis elements. `f(ε):=π_⊥(H^ε)` is entire, and `f(0)=0` because `H_A∈𝒱`. Its derivative `f′(0)=π_⊥(Σ_x[D_x,H_A])` contains the basis elements of `−t₀γ_{x,a}γ_{x+1,a}Z_{x+1}(c_x†c_{x+2}−c_{x+2}†c_x)`, supported on three sites. No other first-order term contains them (item 44). So one coordinate of `f` is an entire function with a simple zero at `0`, and it has no other zero near `0`. ∎

**Consequence under the owner's frame.** SMG1-GAP fixes the certified decomposition, and the generator is its R-GEN sum. The displayed decomposition of `U^ε` gives `H_A` (item 45). No decomposition gives `H^ε`. So Theorem 6's clause "S1–S3 hold" is a true statement about an operator outside the R-GEN class. It is not an R1.5 instance at the generator level. What Theorem 6 gives in the owner's frame is a tick statement: an NN-a tick with genuine degree-four gates, whose R-GEN generator is the configuration-conserving `H_A`, has an exactly stationary symmetric finite-ring state. That state has vanishing charged correlations beyond four sites and, for small `ε`, the `1/r` light law (item 47). Pass 1's second counterexample stands in a stronger form: no decomposition sees the gates. The degree-four terms of `H^ε` at order `ε` span three sites, while the degree-four mixing terms of R-GEN generators span one bond. So Theorem 6 does not reach generic degree-four mixing of R-GEN form, as `SMG15.md` line 124 already says.

**Referee closure on induced terms (items 48, 69).** Pass 1 claimed that "in Theorem C's class all induced terms vanish to every order". `SMG15.md` line 124 says unitary equivalence does not imply this. That is right. Here is what does hold. Fix `L` and let `P:=P^{1⃗}`; `H_A` commutes with `P`. For small `|ε|`, `‖V_εPV_ε*−P‖<1`, so the direct rotation `e^S` (`S=−S*`, `PSP=QSQ=0`) with `e^SV_εPV_ε*e^{−S}=P` exists. When `ran P` carries an isolated part of the spectrum of `H_A`, this is the canonical Schrieffer-Wolff transformation for the perturbation `H^ε−H_A`. Then `W:=e^SV_ε` commutes with `P`, and the effective Hamiltonian is

`H_eff=Pe^SH^εe^{−S}P=W_P(PH_AP)W_P*`, with `W_P:=PWP` unitary on `ran P`.

So `H_eff` is a unitary conjugate of the free chain. It has the free spectrum, which is what unitary equivalence gives. Its induced terms vanish exactly when `W_P` commutes with the free chain. *Through order `ε³` they vanish:* `W_P=P+O(ε⁴)`. Proof: every order-`k` term of `S` and of `log W` is a combination of products of `k` operators `D_x`, with `P`s and `Q`s between them. Each `D_x` multiplies the characters at `x` and `x+1` by one `ρ_a`. A product of an odd number of `ρ_a` is odd, hence nontrivial. So returning to `1⃗` needs an even number of flips at every site. On a ring with `L≥8` this forces the bonds of the product to pair up. In particular `P(D_{x₁}⋯D_{x_k})P=0` for odd `k`. Write `log V_ε=εD+(ε²/2)[D_o,D_e]+O(ε³)`, `D:=D_e+D_o`. The order-one terms are `S₁=−(PDQ+QDP)` and `K₁=QDQ`, so `PK₁=K₁P=0`. At order two, `PK₂P=(1/2)P[D_o,D_e]P+(1/2)P[S₁,D]P`. The first term is zero because the two factors sit on different bonds. The second is `−(1/2)(PDQDP−PDQDP)=0`. At order three every term is odd or contains `PK₁` or `K₁P`. Order four is not settled here. So pass 1's second-order use is right; "to every order" is open.

### 2.7 Theorem 5, pass 1's Theorem B: decision

**Decision: CORRECT (items 36-38).** Every step was re-derived. The identity `TUT*=Ue^{−2πiN/L}`, with `e^{2πin₀}=1`, gives `TUT*=−U` on `N=L/2`. A generator term `h` commutes with `N` and with every `n_y` outside its window, so it commutes with the window number `N_w`. The wrap term in the window identity is an integer multiple of `2π`. On `N_w=k` the operator `D_x` ranges over an interval of length `k(r+1−k)≤⌊(r+1)²/4⌋`. Averaging the two twists, `1−cos z≤z²/2` and the sum over `L` translates give `C_h/L`. Corollary 5.1 follows by the variational principle in the sector. Under S1 the unique ground vector cannot be `S`-charged, so it is `S`-trivial.

Three scope notes. (i) The theorem covers every one-site-translation-invariant generator of fixed range that commutes with `N`, `S` and the Gauss operators. That includes the electric term `τ_E(1−X_ℓ)/2`, so Theorem 5 itself does not need `τ_E=0`. (ii) Under SMG1-GAP it applies to the R-GEN generator when that sum is one-site invariant, as `H_A` is; the tick is only cell covariant. `SMG15.md` line 104 says so. (iii) It gives one further state in the ground vector's sector. It gives neither S2's growing count, nor S1, nor uniqueness. Pass 1's sentence "What remains open for generic mixing is (S1) and (S3), not (S2)" is wrong (item 67); pass 2 corrected it. Item 39: "essential hypotheses" claims necessity without proof; the fix is "The proof uses".

### 2.8 R15-SPEC and R-COR under SMG1-GAP (items 11, 12, 22)

**R15-SPEC, pass 1's tests `C, P, C, P`.** Test 1, C: right. The reading fixes the meaning of R1.5's own words, so it passes only as the owner's specification for this rung. Test 2, P: right; every quantifier is fixed. Test 3, C: the stated reason, "it inherits R-GEN's status (Q1)", is out of date, since SMG1-GAP adopts R-GEN for SMG1's rungs. Re-tested, R15-SPEC asserts no existence and settles no downstream question; its finite-`L` weakness is a question of adequacy, not a smuggle. Referee mark: P. Test 4, P: the reason covers `L∈4N` and `N=L/2`. But R15-SPEC also replaces two pieces of SMG1-GAP. It uses finite rings instead of the GNS generator. It restricts to `H_{1/2}` instead of SMG1-GAP's ground-state condition, which ranges over "every local \(A\)". Referee mark: C. The reading passes as a finite-volume form only if its infinite-volume reading is stated beside it. The next two closures supply that reading for Theorem 3.

**Referee closure: canonical against grand-canonical.** Keep the data of Theorem 3 with `δ<7τ`, and let `ω_A` be the infinite-volume limit of `Ω_A` on `𝔄^G` (it exists as in section 2.5, step 1).

(i) *If `μ(1,1)=0`, then `ω_A(A*[H_A,A])≥0` for every local `A∈𝔄^G`, so `ω_A` is an R-GEN ground state in SMG1-GAP's sense.* On `ran P^{1⃗}` and any `N`, `H_A=−t₀Σhop_x`. Its minimum over all `N` and both holonomies is `E₀`, at `N=L/2` and `w=−1`, because then every negative one-body level is filled and no level is zero. On `ran P^{χ⃗}` with `m≥1`, Theorem 3's bound uses only the free minimum and `2m` bond changes of norm `≤δ`, so it holds for every `N`: the energy is at least `E₀+m(14τ−2δ)`. Hence `Ω_A` minimizes `H_A` on all of `H_G`. For gauge-invariant `A`, `AΩ_A∈H_G`, so `⟨Ω_A,A*[H_A,A]Ω_A⟩=⟨AΩ_A,(H_A−E₀)AΩ_A⟩≥0`. For `L` large, `[H_A,A]` is local and independent of `L`. Take the limit.

(ii) *If `μ(1,1)≠0`, some local `A∈𝔄^G` gives `ω_A(A*[H_A,A])<0`.* Say `μ:=μ(1,1)<0`. On the trivial configuration `H_A` is `dΓ(h)` plus a constant, with `h=h₀+2μ` and `h₀` the hopping matrix, and the light state is the Fock state of `Π=1_{(−∞,0)}(h₀)`. For `A=D(c†(f)c†(g))`, Wick's rule with `ω(c(u)c†(v))=⟨u,(1−Π)v⟩` gives

`ω_A(A*[H_A,A])=⟨f,(1−Π)hf⟩⟨g,(1−Π)g⟩+⟨f,(1−Π)f⟩⟨g,(1−Π)hg⟩−⟨f,(1−Π)g⟩⟨g,(1−Π)hf⟩−⟨f,(1−Π)hg⟩⟨g,(1−Π)f⟩`.

`h₀` commutes with `Π`, and `h₀(1−Π)` has `0` in its spectrum. So for each `η>0` there is a finitely supported `f` with `⟨f,(1−Π)h₀f⟩≤η‖(1−Π)f‖²`. Let `g` be `f` translated by `d`. The last two terms tend to `0` as `d→∞`, because the kernels of `1−Π` and `(1−Π)h` decay. The first two equal `2‖(1−Π)f‖²(⟨f,(1−Π)h₀f⟩+2μ‖(1−Π)f‖²)≤2‖(1−Π)f‖⁴(η+2μ)`. Choose `η<2|μ|` and `d` large. For `μ>0` remove two particles instead. ∎

So R15-SPEC's restriction to `H_{1/2}` and SMG1-GAP's ground-state condition agree on Theorem 3's family exactly when `μ(1,1)=0`. Theorem 3 should say so (edit E7).

**Referee closure: the charged gap in form.** With `μ(1,1)=0` and `δ<7τ`, every `S`-charged vector of `H_G`, of any `N`, has energy at least `E₀+14τ−2δ`, by (i). For a local `S`-charged `A∈𝔄^G`, `AΩ_A` is `S`-charged. So `ω_A(A*[H_A,A])≥(14τ−2δ)ω_A(A*A)` for every such `A`, by the limit as in (i). This is SMG1-GAP's sector gap in quadratic-form form on the local vectors of the charged GNS subspace. The spectral statement on the GNS space needs the local vectors to be a core for the GNS generator. That is standard for finite-range interactions through analytic vectors. It is not rebuilt here.

**R-COR, pass 1's tests `C, P, C, P`.** Tests 1, 2 and 4: right. Test 3: pass 1 notes that "correlation decay is not a spectral gap, and the two readings can differ". After SMG1-GAP that difference is decisive. Clause (C2) would let correlation decay count as "mirror gapped" without an R-GEN gap. That settles by premise what the owner has decided otherwise. As a reading of "gapped", R-COR now fails test 3. Clauses (C1) and (C3) do not use (C2). (C1) is the separate requirement SMG1-GAP names: "Tick stationarity remains a separate requirement." (C3) names the light field the target names. So (C1) with (C3) can serve as R1.5's tick part, and (C2) as a diagnostic. This is a recommendation; nothing is adopted.

**Q-R15, narrowed.** Under SMG1-GAP, Q-R15 asks only three things. (a) The sector-resolved form of the R-GEN gap beside a gapless remainder: finite-ring S1, or the GNS form above. (b) Whether "half filling" is canonical (`H_{1/2}`) or a property of the R-GEN ground state. (c) Whether R1.5 requires the tick part (C1) with (C3).

### 2.9 Lemma S-GAP and its three failed attacks (items 54-57, 70)

**Decision: S-GAP is a well-posed open statement, and three distinct attacks fail at named steps, as `SMG15.md` lines 150-154 state them.** `H_ε/τ` depends only on `t/τ` and `ε/τ`, so the quantifiers make sense. The `t=0` remark (line 148) was checked: on `N=L/2`, `−(2ε²/7τ)Σ_x(hop⁰_x)²=−(2ε²/7τ)(L−2Σ_xn_xn_{x+1})`, minimized exactly when no two neighbours are occupied, that is, by the two alternating configurations.

1. *Local Schrieffer-Wolff (Abanin-De Roeck-Ho-Huveneers).* The failing step is real. The remainder `V̂` is a sum of `L` local terms; a norm bound by the sum of local norms grows with `L`, and Weyl's inequality then gives no `L`-uniform sector gap. Treating `V̂` as a local perturbation needs a gap of `τN+D̂`, whose `N=0` block is the gapless light chain. Pass 1's bound on `τN+D̂` was "plausible", not proved; line 152 says so.
2. *Absolute polymer expansion.* The failing step is real for the representation the draft uses: integrate the free light field exactly and sum polymer weights absolutely. Two distant vacuum polymers are then linked by a truncated light correlation. Such correlations have nonzero `|z|⁻²` tails. One equal-time instance, re-derived here: for the bond operator `B_x=hop⁰_x`, `⟨B_0;B_r⟩=2(−1)^r/(π²r²)+O(r⁻⁴)`. The absolute sum of `|z|⁻²` over one space and one time dimension diverges logarithmically. Pass 1's "no Kotecký–Preiss-type criterion holds" claims more: other representations or resummations are not excluded. Line 153 states the narrower claim, which is right.
3. *Fröhlich-Pizzo.* The failing step is real. (1.4) needs a one-dimensional on-site kernel. At `τ₅=τ_E=0` the on-site kernel, with its link, is `ψ⊗{|0⟩,|1⟩}⊗{|+⟩,|−⟩}`, four-dimensional. Splitting it with `τ₅n_x` empties the light chain. Pass 1's "no reduction of this kind can exist" holds only for reductions that keep one-site translation of the generator and half filling, where Corollary 5.1 forbids the conclusion. Line 154 states the narrower claim, which is right.

So S-GAP qualifies as the stopping lemma under the three-attack rule, with pass 2's narrowings. The open-list entries R1.5-U and R1.5-D (line 156) are right.

### 2.10 The claims that `τ_E=0` is needed and that Golterman-Shamir first bites at R2 (items 71, 72)

**`τ_E=0` is not shown to be needed.** Pass 1 (draft line 66) writes "so R1.5's light chain should take `τ_E = 0`", and (line 123) "with `τ_E > 0` its single light fermion is not expected to be light". Three facts decide the claim. (i) The algebra is right: `τ_EΣ_x(1−X_{ℓ_x})/2` reduces to `τ_EΣ_x[1−(∏_{y≤x}P_y)⊗σᶻ]/2`, a string term in the reduced matter description (Theorem 2). (ii) Theorem 5 holds with `τ_E>0`, because the electric term is a one-link term commuting with `N`, `S` and the Gauss operators. So the weak form of S2 does not need `τ_E=0`. (iii) Exponential decay of the dressed two-point function at `τ_E>0` (confinement) is proved neither in `SMG15.md` nor in the sources it cites; L19 is numerical context. So `τ_E=0` is a choice of model class. Pass 2 says exactly this: "this is a restriction, not a derivation from the working set" (line 20).

One pass-1 sentence is false, and pass 2 dropped it. Draft line 123: "`SMG1.md` Theorem 4.1 uses `τ_E > 0` for uniqueness on the full algebra; in `H_G` the links are fixed by Lemma 2 and `τ_E` is not needed for it." *Counterexample.* At `θ=0` and `τ_E=0` no term of `H₀` acts on links. By Theorem 2, `J*H₀J=H_matter⊗1` on `F_even⊗C²`. So every eigenvalue of `H₀` on `H_G` has even multiplicity, and the ground vector is not unique. At `τ_E=0` the holonomy doublet is split only by hopping: in Theorem 3 by `2|t₀|tan(π/(2L))`, which closes as `L→∞`.

**"Golterman-Shamir first bites at R2" is not proved.** Pass 1 (draft lines 66 and 260) argues that the theorem's conclusion holds at R1.5 and that "The test bites first at R2". The first half is right and is all that `SMG15.md` line 166 keeps: the light content of Theorem 3 is vector-like, with Fermi points `±π/2` of the same `U(1)_5` charge, consistent with the theorem's conclusion. The second half needs the theorem's hypotheses at R2: a fermion-only Hamiltonian, a free relativistic continuum limit and the interpolating-field condition. Their status for an NN-a tick with links is not checked anywhere in the sources. So it is an expectation about where the theorem becomes relevant, not a result. Pass 1's "no such partner exists in these classes (proved, (A4) and (C-c))" covers `S`-charged light states only. `S`-trivial partners fall under W2-LIGHT, which is open.

### 2.11 The distiller's GAP list, one by one (`SMG15.md` line 5)

| GAP sentence | Real? | Where decided | Repair |
|---|---|---|---|
| Purity of the infinite-volume limit for R-COR is not proved | Real | §2.5 | Existence, stationarity and invariance closed; purity reduced to P3 (Lemma P-red); the missing inference fails in this carrier |
| R15-SPEC does not itself exclude all extra light fields | Real | §2.4 | Repaired statement of §2.4; the criterion is W2-LIGHT, open by the owner's choice |
| The twist theorem closes one gap, not S2 | Real | §2.7 | None needed: Theorem 5 yields one state; S2's growing count holds for Theorem 3's family by direct count |
| "All induced terms vanish" is not implied by unitary equivalence | Real | §2.6 | Effective Hamiltonian is `W_P(PH_AP)W_P*`; induced terms vanish through order `ε³`; open beyond |
| The polymer failure and the RG imports are narrower than stated | Real | §2.9; item 52 | Route 2 fails for the absolutely summed representation only; the Benfatto-Mastropietro hypotheses are unchecked, and no step uses them |

---

## 3. Required edits to `SMG15.md`

Each edit names its line and its replacement. None changes the content of a theorem; E7 and E11 add scope that the owner's frame requires.

- **E1** (line 3). "Theorems 1–6 prove" → "Theorems 1–7 prove".
- **E2** (lines 7 and 158). Remove Q1 and Q2 from the open lists. Add: "Q1 and Q2 were answered on 2026-11-07 (`TOE_ASSEMBLY.md` §3.10: SMG1-GAP adopts bounded R-GEN for SMG1's rungs; SMG1-W2.1 keeps W2.1). W2-LIGHT stays open." Add P3 to the open list of line 7.
- **E3** (lines 18, 24, 76, 116). Replace "proposed R-GEN" by "R-GEN (SMG1-GAP)". In line 18 replace "Q1 asks whether to accept it" by "SMG1-GAP fixes the certified decomposition as part of the data".
- **E4** (line 24). Replace the sentence "S1–S3 do **not** mathematically exclude [...]" by the repaired statement of section 2.4. Replace the four-test report by: "Pass 1 marked `C, P, C, P`. After SMG1-GAP the referee marks `C, P, P, C`: test 3 no longer turns on R-GEN's status; test 4 is conditional because the reading uses finite rings and the canonical sector `H_{1/2}` where SMG1-GAP uses the GNS generator and a ground-state condition over every local `A` (`SMG15_REFEREE.md` §2.8)."
- **E5** (line 26). Add: "After SMG1-GAP, R-COR fails test 3 as a reading of 'gapped': (C2) would make correlation decay count as a gap. (C1) with (C3) can serve as the separate tick-stationarity requirement that SMG1-GAP names; (C2) as a diagnostic." Replace "Q-R15 asks which reading, if any, to use" by the narrowed Q-R15 (a)-(c) of section 2.8.
- **E6** (line 44). "An undressed charged bilinear" → "An undressed gauge-variant bilinear".
- **E7** (after line 72). Add: "Under SMG1-GAP, whose ground-state condition ranges over every local `A`: if `μ(1,1)=0`, `Ω_A` minimizes `H_A` on all of `H_G`, its infinite-volume limit is an R-GEN ground state, and `ω_A(A*[H_A,A])≥(14τ−2δ)ω_A(A*A)` for local `S`-charged `A`; if `μ(1,1)≠0`, the limit is not an R-GEN ground state (`SMG15_REFEREE.md` §2.8). The spectral form of the charged gap on the GNS space needs the local vectors to be a core (R15-GNS, open)."
- **E8** (line 76). Add: "With pairwise disjoint edge triples, `L_site` is two NN-a layers (even and odd sites); R-GEN is unchanged."
- **E9** (line 88). Replace the GAP by the repaired text of section 2.5.
- **E10** (line 104). "are essential hypotheses" → "are hypotheses the proof uses". Add: "Theorem 5 covers the electric term, so it does not need `τ_E=0`."
- **E11** (after line 116). Add: "For small `ε≠0`, `H^ε` is not the R-GEN generator of any certified NN-a decomposition (`SMG15_REFEREE.md` §2.6). Under SMG1-GAP the generator of `U^ε` is `H_A`, and Theorem 6 is a statement about the tick and its stationary state. Its clause on S1–S3 concerns the operator `H^ε`."
- **E12** (line 124). Add: "The canonical Schrieffer–Wolff effective Hamiltonian of `H^ε` relative to `P^{1⃗}` is `W_P(PH_AP)W_P*` with `W_P=P+O(ε⁴)`: induced terms vanish through order `ε³`; higher orders are not settled (`SMG15_REFEREE.md` §2.6)."

## 4. Open statements to carry, by name

- **S-GAP.** The stopping lemma. Three distinct attacks failed, each at a named step (section 2.9): (1) local Schrieffer-Wolff, at the extensive remainder under Weyl's inequality; (2) the absolute polymer expansion with the free light field, at the log-divergent absolute sum of `|z|⁻²` links; (3) Fröhlich-Pizzo, at hypothesis (1.4).
- **R1.5-U** and **R1.5-D**, as in `SMG15.md` line 156.
- **P3** (new). The left half-parity automorphism `Θ_L` of the even light CAR algebra is not unitarily implementable in the GNS representation of the even part of the band state `ω_Π`. With Lemma P-red it gives purity of the infinite-volume tick state, hence R-COR's (C1) for `Ω_tick`. The same statement for the Fermi-sea projector gives purity of `ω_A`.
- **R15-GNS** (new). The spectral form, on the GNS space of `ω_A`, of the charged gap proved in quadratic-form form in section 2.8.
- **The tick/generator state comparison**: whether `Ω_tick` and `Ω_A` agree to `O(t₀)` on local observables.
- **Q-R15**, narrowed to (a)-(c) of section 2.8.
- Inherited and unchanged: **W2-LIGHT** (owner: open), **R1-H**, **FLQ** for a hopping mirror.
- No longer open: Q1 and Q2 (answered 2026-11-07).

## 5. Freeze recommendation

**Freeze `SMG15.md` after edits E1-E12.** Its seven theorems are correct as stated: Theorems 1-5 and 7 without change, Theorem 6 with the scope sentence of E11. The four `SMG15.md` ERRORs are three out-of-date owner-status lines (items 3, 8, 59) and a theorem count (item 1). The three INCOMPLETE items are the four-test reports of the two readings (items 11, 12) and one unproved word (item 39). Every GAP the distiller marked is real. The R-COR-purity GAP is now reduced to the single statement P3, and the referee shows that the missing inference fails in this carrier. The pass-1 claims the lane brief names were decided: Theorems A, B, C and Proposition D hold as `SMG15.md` states them; `τ_E=0` is a choice, not a necessity; "Golterman-Shamir first bites at R2" is an expectation. No new proof obligation blocks the freeze. P3 and R15-GNS enter later by dated amendment.

---

## FINISH

**Proved (pass 3; referee closures, each written out above).**
- The infinite-volume limit of `Ω_tick` exists on the gauge-invariant algebra, is tick-stationary, and is `S`-, `U(1)_5`- and cell-invariant (§2.5, step 1).
- Lemma P-red: that limit is pure if P3 holds. Its steps: the mirror factors out; the dressed even light algebra is isomorphic to `CAR⁺`, with `X_0` acting as `Θ_L`; the even band state is pure; Schur's lemma turns a non-pure decomposition into an implementer of `Θ_L` (§2.5).
- `|ω(X_0X_n)|≤exp(−2Σ_{u∈I,v∉I}|Π(u,v)|²)→0`, a necessary condition for purity (§2.5).
- For small `ε≠0`, `H^ε` is not the R-GEN generator of any NN-a decomposition (§2.6).
- The canonical Schrieffer-Wolff effective Hamiltonian of `H^ε` is `W_P(PH_AP)W_P*` with `W_P=P+O(ε⁴)` (§2.6).
- For Theorem 3's family with `δ<7τ`: the limit state is an R-GEN ground state in SMG1-GAP's sense if and only if `μ(1,1)=0`; with `μ(1,1)=0` the charged gap `14τ−2δ` holds in quadratic-form form (§2.8).
- One-bond `[check]`s agree with Theorems 3, 4 and 7 (§0.1); they prove nothing.

**Counterexamples.**
- To "finite-ring purity, stationarity and symmetry imply purity of the infinite-volume limit", in this carrier: holonomy eigenvectors of the empty light chain at `τ_E=0` (§2.5).
- To pass 1's "in `H_G` the links are fixed by Lemma 2 and `τ_E` is not needed for it" (`SMG1.md` Theorem 4.1): at `θ=τ_E=0` every eigenvalue on `H_G` has even multiplicity (§2.10).
- To "the canonical half-filled ground state of Theorem 3 is an R-GEN ground state for every `μ`": `μ(1,1)≠0` (§2.8).
- To pass 1's "What remains open for generic mixing is (S1) and (S3), not (S2)": Theorem 5 gives one low state, not S2 (item 67).

**Open by name.** S-GAP (three named attacks failed: local Schrieffer-Wolff, absolute polymer expansion, Fröhlich-Pizzo), R1.5-U, R1.5-D, P3, R15-GNS, the tick/generator state comparison, Q-R15 (narrowed), W2-LIGHT, R1-H, FLQ for a hopping mirror. The order-`ε⁴` induced terms of Theorem 6 are unsettled; nothing downstream uses them.

**What changes downstream.**
- **SMG1, R1.5-D.** Theorem 3 is an R1.5 instance under SMG1-GAP on finite rings at fixed filling. In infinite volume it is an R-GEN ground state when `μ(1,1)=0`, with the charged gap in form. Its purity, and R-COR for the tick, reduce to P3. Theorem 6 is a tick-level example: the R-GEN generator of its tick is `H_A`, and its degree-four generator terms lie outside the R-GEN class.
- **Q-R15.** Narrowed to the sector-resolved gap, the meaning of "half filling", and whether the tick part is required (§2.8).
- **R2.** Golterman-Shamir's hypotheses must be checked for R2's tick before it is cited as an obstruction or a test. The dressing template of Theorem 6 is a tick-level template.
- **Frozen parts, axioms, working set.** None changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. No law, reading or definition is adopted.
