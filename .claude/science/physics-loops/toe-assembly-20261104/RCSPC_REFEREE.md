lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# RCS-PC referee (pass 3): Clifford nodes on spinor-class charged sectors

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini as
pass 3 (referee) under PR #10138's method. The object of review is
`RCSPC.md` (pass 2, Codex gpt-6.1-terra distillation of `RCSPC_DRAFT.md`,
which a Claude lane wrote as pass 1). This referee does not edit
`RCSPC.md`.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort,
headless on the Mac mini. This session wrote neither pass 1
(`RCSPC_DRAFT.md`) nor pass 2 (`RCSPC.md`). This is one check: one
whole-part, line-by-line read. It reviews no other review.

**Text read.** `RCSPC.md` at commit `f47023bbb` (the commit that last
touches it and the branch head). SHA-256
`c4f56b002fb74af771cb2a87920896ac9e795a7fc275de35490072c9cbe6cbb1`.
It has 241 lines. Line numbers below refer to that file.

**Sources read**, all at `f47023bbb` in this folder unless stated:

| File | Lines read | Use |
|---|---|---|
| `prior/RCSPC.md` | all | prior-work digest |
| `RCSPC_DRAFT.md` (SHA-256 `be9a2549…e896`, commit `014c1a8ad`) | 40-60, 237-239, 275-279, 342-343 | pass-1 statements behind both GAPs and the live-law remark |
| `RCS1.md` | 30-34, 72-79, 86-91, 95, 99-131, 165-167, 191-197, 221 | definitions 3 and 5, Lemma 5.1, Theorem 5, §5 strings, Lemma 6, Theorems 7-8, Corollary 9, R2(a), R4, RCS-P |
| `RCSP16.md` | 19-24, 28-32, 42-48, 86, 92-100 | definitions 1-6, Theorems 1-3, 8-10 |
| `RCSP16_REFEREE.md` | 22, 34, 43, 53, 78, 94-122 | notes N1, N3, N6, N7, N9 |
| `CG16B.md` | 27, 35-57 (headings), 84-96, 130-150 | D1, Theorem 4.1, Theorem 6.2, Proposition L, Example S |
| `CG16D.md` | 75, 95-136 | Lemma N Step 2, D-reg, Theorems 8-9 |
| `CG16S.md` | 23, 96, 140 | Weyl point, setting F, RC-W scope |
| `LZ1.md` | 36-46 | band, node, D1 |
| `LW1_REFEREE.md` 1-80, `Y2W_DRAFT.md` 1-20 | format only | |
| `origin/main` at `f5af11cd0` (fetched, read with `git show`) | rotor note line 32; three-axis note lines 46-48; clock note line 4; `docs/MINIMAL_AXIOMS_2026-06-29.md` (line count only, unchanged) | quotes in `RCSPC.md` lines 7 and 160 |

**Working-set entries used.** None directly. The file uses the frozen
parts above and the owner's candidate readings R-CS^str and R-16^str′
only as `RCSPC.md` names them. The axioms are read plainly, per the
owner's guidance: "just keep in mind our axioms may not be right, and we
dont need to do some super hard core adversarial reads of them, we can
specify if needed".

**Method.** Every proof step was rebuilt by hand. No numeric check was
run; none was needed. Verdicts: CORRECT; ERROR (a false line, quoted,
with a fix or counterexample); INCOMPLETE (a named missing step, with
the step). A "referee closure" is a complete short argument written
here. Notes N1-N14 in §2 carry the details.

**Counts.** 76 items: 64 CORRECT, 4 ERROR, 8 INCOMPLETE. One ERROR item
is a GAP text whose example is wrong; the GAP itself is real. No ERROR or
INCOMPLETE item changes the content of a corrected theorem. Three referee
closures are counterexamples (N1, N2, N3). N1 shows that the draft's
uncorrected Theorem 7 is false, not only unproved. One proposed
restatement is offered, not adopted: the weaker open lemma RCSPC-CL′
(§3.7).

---

## 1. Verdict table

| # | Item (`RCSPC.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | Status paragraph (3) | CORRECT | Matches the body. |
| 2 | Provenance (5) | CORRECT | |
| 3 | Target paragraph (7) | CORRECT | Main-branch quotes checked at `f5af11cd0`. |
| 4 | Distiller conventions (11) | CORRECT | |
| 5 | D1, law (13) | CORRECT | Wording: "gauge-fixed subalgebra" should read "local-gauge fixed subalgebra", as `RCSP16.md:19` has it (the fixed-point algebra, not a gauge fixing). Matter-evenness is `CG16B.md:87` under (F) and link-purity. |
| 6 | D2, lines and target numbers (15) | CORRECT | |
| 7 | D3, strings and ray sectors (17) | CORRECT | The covariance sentence holds for translation-invariant `ω` (`RCS1.md:91`); see item 25. |
| 8 | D4 (19) | CORRECT | Same class as `RCSP16.md:92` and `RCS1.md:32`. |
| 9 | D5 (21) | CORRECT | |
| 10 | D6 (23) | CORRECT | Matches `LZ1.md:42`, including continuity of `V` on `T³`, which Lemma 1.1 needs. |
| 11 | D7 and its three derived facts (25-29) | CORRECT | Stabilizers constant on orbits; `σ` bijective; `σ(β·κ)=β·σ(κ)`. |
| 12 | D8 (31) | CORRECT | |
| 13 | D9 (33) | CORRECT | |
| 14 | §4.1 lead (39) | CORRECT | |
| 15 | Theorem 1, statement (41) | CORRECT | |
| 16 | Lemma 1.1 and proof (45-47) | CORRECT | Quote matches `RCS1.md:76`. |
| 17 | Lemma 1.2 and proof (49-51) | CORRECT | Quote matches `CG16D.md:75`. |
| 18 | Lemma 1.3 and proof (53-55) | CORRECT | The displayed bound is true, but not term by term; N7. |
| 19 | Theorem 1, Step 0 (57) | CORRECT | |
| 20 | Step 1 (59) | CORRECT | |
| 21 | Step 2 (61) | CORRECT | Sign convention `M_β=e^{iK·β}` (`LZ1.md:42`). |
| 22 | Step 3 (63) | CORRECT | |
| 23 | Step 4 (65) | CORRECT | "Circles or empty" also allows single points; harmless. |
| 24 | Remark 1.4 (67) | ERROR | "their slopes along each `n_O` take finitely many values" is false with two or more orbits; N3. |
| 25 | Corollary 2, statement (71) | INCOMPLETE | Needs `ω` translation invariant with covariant choice, or `Γ_x` defined through `π_x∘τ_β^{-1}`; N4. |
| 26 | Corollary 2, proof (a) (73) | CORRECT | Quote matches `RCS1.md:30`. |
| 27 | Corollary 2, proof (b) (75) | CORRECT | Given item 25's hypothesis. |
| 28 | Corollary 2, proof (c) (77) | CORRECT | |
| 29 | Remark 2.1 (79) | CORRECT | Quotes match `RCS1.md:127` and `RCS1.md:221`. |
| 30 | Remark 2.2 (81) | CORRECT | |
| 31 | (S1) (87) | INCOMPLETE | Index `s∈N` with covariance for all `β∈Z³`: `s+β_1` can leave `N`; N8. |
| 32 | (S2) and its quasi-local extension (88-90) | CORRECT | The bound `2ε‖Y‖+ε²` checked. |
| 33 | Proposition 3, statement (92) | CORRECT | |
| 34 | Proposition 3, proof (a) (94) | CORRECT | The Zorn argument is `RCS1.md:167`. |
| 35 | Proposition 3, proof (b) (96) | CORRECT | |
| 36 | Proposition 3, proof (c) (98) | CORRECT | |
| 37 | Remark 3.1 (100) | CORRECT | "Repeat periodically" must mean period one cell along the ray for a single limit; Lemma 4.1(c) proves (S2) directly. |
| 38 | Backgrounds `ω′`, `ω_Φ`, `ω_8` (104-108) | CORRECT | Symbol `σ` also names the label map of D7; N14. |
| 39 | `Ψ_λ` and the pattern `𝒫` (109) | CORRECT | Partition of sites checked; `W_p` is the plaquette loop up to sign. |
| 40 | Lemma 4.1, statement (111-121) | CORRECT | The base tick itself also fixes all four backgrounds; N11. |
| 41 | Lemma 4.1, proof (a) (123) | CORRECT | Quotes match `RCSP16_REFEREE.md:118` and `:122`. |
| 42 | Proof (b), positivity (125) | CORRECT | `Jσ_8≠0`, head and tail `8`, corner norm `4` rebuilt. |
| 43 | Proof (b), product structure (126) | CORRECT | |
| 44 | Proof (c) (128) | CORRECT | Quote matches `RCSP16.md:48`. |
| 45 | Proof (d) (130) | CORRECT | Proposition L's hypotheses checked against `CG16B.md:137`. |
| 46 | Proof (e) (132) | CORRECT | |
| 47 | Corollary 4 and proof (134-136) | CORRECT | |
| 48 | Attack A3 paragraph (138) | ERROR | "this extends `RCSP16.md` Theorem 9 … to all updates" overstates: only the no-Clifford-node clause extends; N5. |
| 49 | Lemma 5 and proof (142-144) | CORRECT | |
| 50 | Lemma 6 and proof (146-150) | CORRECT | |
| 51 | Theorem 7 (corrected), statement (152) | CORRECT | |
| 52 | Theorem 7, proof (154) | CORRECT | |
| 53 | GAP on draft Theorem 7 (156) | CORRECT | Gap real. Referee closure: the uncorrected statement is false; N1. |
| 54 | Scope of Theorem 7 (158) | CORRECT | |
| 55 | Remark 5.2 (160) | CORRECT | Quotes checked. "Link by link" is the right qualifier; N1 shows absorption in aggregate over non-invariant backgrounds. |
| 56 | Lemma 8 and proof (164-166) | CORRECT | |
| 57 | Proposition 9 and proof (168-174) | CORRECT | |
| 58 | Remark 9.1 (176) | CORRECT | |
| 59 | Remark 9.2 (178) | INCOMPLETE | Symbol `(s,L)` is undefined; N9. |
| 60 | RCSPC-CL and the paragraph after it (182-184) | CORRECT | |
| 61 | Attack A (186) | CORRECT | Two-qubit example checked. |
| 62 | Attack B (188) | CORRECT | Wording: "can vanish asymptotically" should be "is not excluded by these relations". |
| 63 | Attack C (190) | CORRECT | |
| 64 | Rigid-plane GAP (192) | ERROR | Its example does not refute the draft's sentence; the GAP is real for another reason; N2. |
| 65 | Status of RCSPC-CL (194) | CORRECT | |
| 66 | "Also outside the results above" (196) | INCOMPLETE | RCSPC-NF is not named or stated here, though line 236 says it is; N12. |
| 67 | Corollary 10, statement and proof (200-202) | CORRECT | The restriction to LZ1's class is not needed; N10. |
| 68 | Corollary 10, quotation (202) | ERROR | "a product of even pure states on disjoint finite blocks" is not verbatim; N10. |
| 69 | Paragraph after Corollary 10 (204) | CORRECT | |
| 70 | Corollary 11 and proof (206-208) | INCOMPLETE | Step 3's spectral window fails at a Weyl point; N6 gives the fix. |
| 71 | RC-W paragraph (210) | CORRECT | Quotes match `CG16S.md:140`. |
| 72 | R-16^str′ paragraph (212) | INCOMPLETE | Proposition L assumes D1; Theorem 7 does not. Referee closure in N11. |
| 73 | §5 table and closing sentence (216-232) | CORRECT | Recorded verdicts match `RCSP16_REFEREE.md:78`. |
| 74 | §6 open items (236-239) | INCOMPLETE | Drops the draft's carry-over to `L5-U[m]` and the reason for `L5-O[S_+]`; referee closure N12. |
| 75 | §6 closing (241) | CORRECT | |
| 76 | Whole file: no "Prior work used" section; numbering starts at §3 | INCOMPLETE | N13. |

---

## 2. Notes

### N1. GAP on draft Theorem 7 (item 53): real, and the uncorrected statement is false

The draft (`RCSPC_DRAFT.md:237`) reads: "Let `ω` be any state of `𝔄`
that agrees with `Φ` on `𝔄^G` … Let `ω_x`, `ω_{x′}` be ray states along
`e_1` with `|x_⊥−x′_⊥|≥D`. Then `π_x` and `π_{x′}` are disjoint." The
distiller's GAP (line 156) says the proof's constancy of `j₀` and `q`
needs more than an invariant partition. That is right. Its example
(alternating link states) breaks the proof step but not the conclusion.
The following referee closure shows the conclusion itself fails.

**Counterexample.** Witness at `m=16`. Fix a flavour `a*`. On one link
let `|F⟩` have the target end full and the source end empty, and let
`|F_{a*}⟩=r^{\rm src†}_{a*}r^{\rm tgt}_{a*}|F⟩` (flavour `a*` moved to the
source end). Both have 16 rishons and the same parity. Partition the
modes into single sites (matter) and single links (both ends). This
partition is `2Z³`-invariant, with block diameter `1<D:=2`. Let `Φ` be
the product state with block vectors:

- matter `|i_0⟩∈H_-` at every site;
- on each direction-1 link `ℓ_{c,s}`: `ψ_s=\sqrt{1−ε_s}|F⟩+\sqrt{ε_s}|F_{a*}⟩`, where `ε_s∈(0,1)` depends only on `s` and `Σ_{s∈Z}ε_s<∞` (say `ε_s=2^{−|s|−1}`);
- on each direction-2 and direction-3 link: `ψ_⊥=\sqrt{1−η}|F⟩+\sqrt{η}|F_{a*}⟩` with a fixed `η∈(0,1)`.

Take `ω=Φ`. Take `x=(x_1,c)` and `x′=x+2e_2`, so `|x_⊥−x′_⊥|=2=D`.

*Step 1 (ray states exist and are product states).* Expand
`B_{r,b}(x)=Σ E_{x,a_0i_0}∏_k(T_k)_{a_{k−1}a_k}`, `a_{2r}=b`. Each
`(T_k)_{ab}=r^{ℓ_k,y_{k−1}}_ar^{ℓ_k,y_k†}_b` acts on the block `ℓ_k`
alone. The annihilator kills `|F⟩` (empty source) and kills `|F_{a*}⟩`
unless `a=a*`. The creator then needs `b=a*`, the only hole. And
`(T)_{a*a*}|F_{a*}⟩=±|F⟩`. So only `a_0=⋯=b=a*` survives:
`B_{r,a*}(x)Φ=±(∏_{k=1}^{2r}\sqrt{ε_{x_1+k−1}})\,u^{(r)}`, where `u^{(r)}`
is the product vector with matter `|a*⟩` at `x`, `|F⟩` on `ℓ_1,…,ℓ_{2r}`
and `Φ`'s block vectors elsewhere. The denominator is positive. A local
observable sees a fixed vector once `2r` passes its support. Hence
`ω_x=Φ_x|_{𝔄^G}`, where `Φ_x` is the product state with matter `|a*⟩`
at `x`, `|F⟩` on every `ℓ_{c,s}`, `s≥x_1`, and `Φ`'s block vectors
elsewhere. The same holds at `x′`.

*Step 2 (`Φ_{x′}` is a vector state in the GNS space of `Φ_x`).* Let
`(K,ρ,Ω)` be the GNS triple of `Φ_x` on `𝔄`. Order all modes so that
the blocks enter an increasing exhausting sequence of finite block sets
`Λ_N` (all containing the blocks of `x` and `x′`) in that order; then
`𝔄(Λ_N)` is the full matrix algebra of the Fock space of `Λ_N`, and
`Φ_x`, `Φ_{x′}` restrict to the vector states of the product vectors
`u_{Λ_N}`, `u′_{Λ_N}`. Put `V_N=|u′_{Λ_N}⟩⟨u_{Λ_N}|∈𝔄(Λ_N)`. Then
`⟨ρ(V_N)Ω,ρ(A)ρ(V_N)Ω⟩=Φ_{x′}(A)` for `A∈𝔄(Λ_N)`, and for `M≥N`,
`⟨ρ(V_N)Ω,ρ(V_M)Ω⟩=∏_{i∈Λ_M∖Λ_N}⟨u_i,u′_i⟩`. The block vectors of
`Φ_x` and `Φ_{x′}` differ only at the matter of `x` and `x′` (inside
every `Λ_N`) and on the links `ℓ_{c,s}`, `s≥x_1`, and `ℓ_{c′,s}`,
`s≥x′_1`, where the overlap is `\sqrt{1−ε_s}>0`. As `Σε_s<∞`, the tail
products tend to `1`, so `‖ρ(V_N)Ω−ρ(V_M)Ω‖^2→0`. The limit `Ω′` is a
unit vector whose vector state is `Φ_{x′}`.

*Step 3 (a local gauge-invariant `C` with `⟨Ω′,ρ(C)Ω⟩≠0`).* Let `λ_1`
be the direction-2 link from `w_1=x′−e_2` to `x′` and `λ_2` the one from
`x` to `w_1`. Put `(S_k)_{ab}=r^{λ_k,w_{k−1}}_ar^{λ_k,w_k†}_b` with
`w_0=x′`, `w_2=x` (annihilate at the target end, create at the source
end), and `C=Σ_{a,b}E_{x′,ai_0}(S_1S_2)_{ab}E^*_{x,bi_0}`. Its indices are
contracted fundamental against conjugate at `x′`, `w_1` and `x`, as in
`CG16B.md:133` ("fundamental and conjugate indices are contracted;
unitarity cancels each local transformation"); so `C∈𝔄^G` and `C` is
local. On `ψ_⊥` the factor `(S)_{a'a*}` kills `|F_{a*}⟩` (source already
holds `a*`) and maps `|F⟩` to a vector whose overlap with `ψ_⊥` is
nonzero only for `a'=a*`, where it is `±\sqrt{η(1−η)}`. The matter
factors map `|a*⟩_x↦|i_0⟩_x` and `|i_0⟩_{x′}↦|a*⟩_{x′}`, which match
`Φ_{x′}`. So `⟨u′_{Λ_N},Cu_{Λ_N}⟩=±η(1−η)∏_{i∈Λ_N∖{\rm supp}\,C}⟨u′_i,u_i⟩`,
and `⟨Ω′,ρ(C)Ω⟩=\lim_N⟨u′_{Λ_N},Cu_{Λ_N}⟩=±η(1−η)P` with
`P=∏_{s≥x_1}\sqrt{1−ε_s}∏_{s≥x′_1}\sqrt{1−ε_s}>0`.

*Step 4 (non-disjointness).* Let `P_1`, `P_2` project onto the closures
of `ρ(𝔄^G)Ω` and `ρ(𝔄^G)Ω′`. Both commute with `ρ(𝔄^G)`. By GNS
uniqueness the subrepresentations on them are unitarily equivalent to
`π_x` and `π_{x′}`. The operator `P_2P_1` intertwines them, and it is
nonzero, since `⟨Ω′,P_2P_1ρ(C)Ω⟩=⟨Ω′,ρ(C)Ω⟩≠0`. So `π_x` and `π_{x′}`
are not disjoint, although `|x_⊥−x′_⊥|≥D`. □

**What it shows.** The corrected hypothesis (cell-translation invariance
of `ω`) is needed, not only convenient. Under it the lowest-level
weight `q` is constant along the ray, so it is not summable. In the
counterexample the weights `ε_s` are summable, and the string is
absorbed in aggregate although Lemma 5 empties a level on every single
link. The corrected Theorem 7 (line 152) and its proof (line 154) are
correct.

### N2. Rigid-plane GAP (item 64): real; its example is wrong; rigid planes give no node

**The distiller's example.** Line 192 says: "For `m=16`, if `n_s=0` and
`n_{s+1}=16`, then the source end of the next link is empty. The
interior transfer … annihilates that configuration even though the
incoming target number is 0, not 16." The draft's sentence is "the
weight `Σ_bB^*_bB_b` vanishes only where its line cannot be raised
(`n_s=16`, the top level)" (`RCSPC_DRAFT.md:275`). At `m=16` the source
end of `ℓ_k` holds `16−n_k` rishons. The string's two factors on `ℓ_k`
annihilate at its source end and create at its target end; both need
`n_k≤15`. In the example, `n_{s+1}=16`, so the ray link `ℓ_{s+1}` cannot
be raised. The weight vanishes for exactly the reason the draft allows.
The example does not refute the sentence.

**Why the GAP is still real.** The weight depends on which flavours are
occupied, not only on the numbers. Referee counterexample to the
draft's sentence, with fluctuating rigid planes: on every direction-1
link with target number `n`, occupy flavours `{1,…,n}` at the target end
and `{1,…,16−n}` at the source end. At a ray site `y_k` the factor
`J_{y_k}=Σ_ar^{ℓ_k,y_k†}_ar^{ℓ_{k+1},y_k}_a` needs a flavour that is a
hole at the target of `ℓ_k` and occupied at the source of `ℓ_{k+1}`:
`\{n_k+1,…,16\}∩\{1,…,16−n_{k+1}\}≠∅`, that is `n_k+n_{k+1}≤15`. Let each
plane value `n_s` be `8` or `10`, independently over `s` and equal on all
lines of the plane, with fixed even numbers on transverse links and
matter `|i_0⟩`. Take the gauge average of this mixture. Then
`n_k+n_{k+1}≥16` everywhere, so every term of `B_{r,b}` annihilates every
configuration, and the gauge-invariant weight is `0`, although no link
has `n=16`. The state is gauge and translation invariant, sharp in every
`P_x` and `z_x` (all end numbers even), and fixed by the base tick
(matter-activated: `RCSP16.md:28`, `RCSP16_REFEREE.md:118`). So the
draft's positivity sentence fails without state assumptions, as the
distiller says.

**Referee closure: exact rigid relations always separate the lines.**
The draft's second argument does not need the positivity sentence.

*Lemma RL.* Let `ω` be any state of `𝔄` on the witness (any `m`). Let
`x`, `x′` lie on distinct lines `c≠c′` and let their ray states exist.
Suppose there are fixed lines `c_1,…,c_q` and fixed integers
`κ_1,…,κ_q` (independent of `s`), with `c=c_1`, `κ_1=1` and
`c′∉\{c_1,…,c_q\}`, such that for all large `s` the state `ω` is sharp
in `L_s=Σ_iκ_in_{c_i,s}`, with value `k_s`. Then `π_x` and `π_{x′}` are
disjoint.

*Proof.* `B_b^*B_b` commutes with every target number: `n_ℓB=B(n_ℓ+1)`
on ray links (Lemma 5) gives `B^*Bn_ℓ=n_ℓB^*B`, and off the ray they
commute. Let `g_s` be the spectral projection of `L_s` off `k_s`; then
`ω(g_s)=0` and `0≤ω(B_b^*B_bg_s)=ω(g_sB_b^*B_bg_s)≤‖B_b‖^2ω(g_s)=0`. By
functional calculus `f(n)B=Bf(n+1_c)`, where `1_c` adds one on the ray
links. For `s` on the ray, `L_s(n+1_c)=L_s(n)+1`, so the spectral
projection of `L_s` off `k_s+1`, evaluated in `ω^{(x)}_r`, equals
`Σ_bω(B_b^*B_bg_s)/Σ_bω(B_b^*B_b)=0`. Hence `L_s−k_s` is sharply `1` in
`ω_x`. The ray of `x′` touches none of the lines `c_i`, so `L_s−k_s` is
sharply `0` in `ω_{x′}`. These are uniformly bounded, self-adjoint,
gauge-invariant local elements with escaping supports, and each cyclic
vector is eventually an eigenvector of them. `RCS1.md` Lemma 6
(line 95) gives disjointness. □

Rigid planes are the case `L_s=n_{c,s}−n_{c″,s}`, with a third line
`c″∉\{c,c′\}` and `k_s=0`. The draft's "complementary variant" is
`L_s=n_{c,s}+n_{c_B,s}`, `k_s=16`. In both cases Lemma RL gives disjoint
sectors on distinct lines. So `Γ_x⊆Ze_1`; no two sectors on distinct
lines are quasi-equivalent; and with factor sectors Corollary 2 excludes
a Clifford node. No translation invariance is needed.

**What Lemma RL does not decide.** Disjointness does not by itself make
the limit in Proposition 9 positive. Proposition 9 derives the cone lift
from quasi-equivalence; the converse is not proved. So a rigid-plane
state could, in principle, meet the bare limit condition while its
sectors stay disjoint. Such a state would refute RCSPC-CL as worded
(line 182) and still give no Clifford node. Line 184 already says that a
failure of RCSPC-CL need not give a node. This suggests carrying the
weaker lemma that Corollary 2 actually needs (§3.7, RCSPC-CL′).

**Outcome.** Rigid planes, and every background with an exact linear
number relation that ties the ray's line to lines a displaced ray does
not touch, cannot give quasi-equivalent sectors on distinct lines, so
they give no Clifford node. This is proved whenever the ray states
exist. Whether such a state can meet the bare cone-lift limit is not
decided. RCSPC-CL stays open (§3.7).

### N3. Remark 1.4 (item 24)

Line 67: "their slopes along each `n_O` take finitely many values". Step 3
proves less: at each point of `U`, some orbit `O` has
`n_O·∇λ=−θ_O`; that is, `∇λ` lies on one of finitely many affine planes
`\{k:n_O·k=−θ_O\}`. With two orbits the slope along one `n_O` can vary
continuously. Example: `H=ℓ²(Z³)⊕ℓ²(Z³)`, `T` the shift on both. Label
the first summand by lines along `e_1` (`Γ=Ze_1`, `n_{O_1}=e_2`), the
second by lines along `e_2` (`Γ=Ze_2`, `n_{O_2}=e_1`). Let `Ũ` act on the
first summand as the Fourier multiplier `e^{−if(K_1)}` with `f` smooth
and non-affine, and as `1` on the second. Then `σ=\mathrm{id}`. The band
`V=e^{−if(K_1)}` on the first summand has slope `0` along `n_{O_1}`
(consistent with Theorem 1) and slope `f′(K_1)` along `n_{O_2}`, which
takes a continuum of values. *Fix:* replace the sentence by "at each
point of `U`, `∇λ` lies on one of finitely many affine planes
`n_O·k=−θ_O`; a Clifford cone needs slopes `ε_iv′(ν·n_O)` that avoid all
of them for some open set of directions `ν` (Step 4)".

### N4. Corollary 2 (item 25)

The proof of (b) uses `π_x∘τ_β^{-1}≅π_{x+2β}`. D3 gives this only for a
translation-invariant `ω` with the covariant choice (`RCS1.md:91`: "For
each site residue modulo `2Z³`, choose one limit point and translate it
covariantly"). *Fix:* add "Let `ω` be translation invariant and choose
the ray sectors covariantly (D3)". Proposition 9 already says this.
Every later use (Corollary 4, Theorem 7 corrected, Proposition 9)
satisfies it.

### N5. Attack A3 paragraph (item 48)

Line 138: "this extends `RCSP16.md` Theorem 9 from matter-activated
updates to all updates." Theorem 9 proves more than "no Clifford node":
"every band satisfies `V(K₀+se_j)=1` for small `s` and each transverse
axis `j` at every node `K₀`" (`RCSP16.md:92`). That clause uses tick
equivalence. For a general update the tick may move lines (`θ_O≠0`), and
Corollary 4 gives no transverse flatness. *Fix:* "this extends the
no-Clifford-node clause of `RCSP16.md` Theorem 9 to all updates; its
transverse-flatness clause is not extended."

### N6. Corollary 11 (item 70)

At a Weyl point `V(K₀)≠1` in general (`CG16S.md:96`: "assume
`dim ker(V(K₀)−1)=2`"). So Step 3's ball, "on which `V` is `C¹` and
`h=i\log V` has spectrum in `(−π/2p,π/2p)`", need not exist, and the
equality `1_Γ(K,W(K))=1_{B_3}(K)P_i(K)` can fail when another
eigenvalue of `V^p` meets `e^{−iλ_i}`. *Repair (referee closure):* use
the smooth local logarithm `H` that the Weyl-point definition supplies,
put `g=pH`, `W=V^p=e^{−ig}`. The frame branches `p(a±|b|)` are simple
eigenvalues of `g` near `K₀`, `K≠K₀`, because the other eigenvalues of
`H` stay away from `0`. In Step 3 replace the equality by
`1_Γ(K,W(K))≥1_{B_3}(K)P_i(K)`, which holds because `e^{−iλ_i(K)}` is an
eigenvalue of `W(K)` whose eigenprojection contains `P_i(K)`. Then
`FM_{1_Γ}=E(Γ)F=0` still forces `1_Γ=0` almost everywhere on `B_3`,
against `P_i≠0`. The graph, the disjoint shifts and the separability step
are unchanged. The quote at line 206 stops before "and `|∇a·n|<|Nn|` for
every unit `n`"; the proof does not use the tilt bound, so Corollary 11
holds for the wider class.

### N7. Lemma 1.3 (item 18), optional

Expanding `u=Q_+u+Q_-u` gives
`|⟨u,(n·M)u⟩−v′(ν·n)|≤2v′|n|‖Q_-u‖^2+2‖n·M‖‖Q_-u‖≤2|n|ε^2/v′+2‖n·M‖ε/v′`.
The text writes `v′|n|ε²/v′^2+3‖n·M‖ε/v′`. That bound is still true,
since `‖n·M‖=v′|n|≥ε|n|`, but the first term is not the expansion's.
Optional edit: print the two-term bound.

### N8. (S1) (item 31)

`X_{c,s}` is indexed by `s∈N`, while `τ_β(X_{c,s})=X_{c+2β_⊥,s+β_1}` is
asserted for all `β∈Z³`. *Fix:* index by `s∈Z`, or assert the covariance
whenever `s,s+β_1∈N`. Every proof uses only large `s`.

### N9. Remark 9.2 (item 59)

"every bounded function `f` of finitely many target numbers near
`(s,L)`": `L` is not defined. *Fix:* "for every uniformly bounded family
`f_s∈𝔄^G` whose supports escape every finite set". The conclusion
`ω_x(f_s)−ω_x(τ_γ^{-1}f_s)→0` then follows from Lemma 8 and covariance.

### N10. Corollary 10 (items 67-68)

The quoted phrase "a product of even pure states on disjoint finite
blocks" is not in `CG16D.md`. The source sentence is "The product is
therefore of even pure states on disjoint finite blocks"
(`CG16D.md:134`). *Fix:* quote it verbatim. The other quotes in line
200-202 match `CG16D.md:132`. On the math: D-reg's `𝔄^G` contains a
fermion-odd element (`CG16D.md:107`, Theorem 8(iv)), so D1's commutation
claim is false there. Proposition 3's proof needs commutation only with
the even `X_{c,s}`, which holds. Its (S2) step needs only factorization
in a product of even block states, which holds for all operators, not
only even ones. So the restriction to LZ1's class (even gates) is not
needed; Corollary 10 holds for every update in the sense of D5. This is
optional.

### N11. Lemma 4.1(a) and the R-16^str′ paragraph (items 40, 72)

(a) The base tick itself fixes all four backgrounds: "Every base cube
gate and its inverse is matter-activated" (`RCSP16.md:28`), and a
matter-activated gate "fixes every vector whose support sites carry
`P=−1`, whatever the links hold" (`RCSP16_REFEREE.md:118`). Optional
edit: add the base tick to the list.

(b) Line 212 applies Proposition L to "every ray sector of Theorem 7's
backgrounds that are sharp in every `P_x` and `z_x`". Proposition L
assumes "`ω` be a D1 state" (`CG16B.md:137`), and Theorem 7 does not
assume stationarity. *Referee closure:* the proofs of L(i)-(iii)
(`CG16B.md:143-145`) never use the tick. (i) uses Cauchy-Schwarz and the
centrality of `z_y` in `𝔄^G`; (ii) uses `P_Λ∈𝔄^G`, `P_ΛB=−BP_Λ` and
matter-evenness of `𝔄^G`, which is a property of the algebra under (F)
and link-purity (`CG16B.md:87`); (iii) uses the identity of Theorem 6.1.
So L(ii)-(iii) hold for every gauge-invariant background sharp in every
`P_x` and `z_x`. *Fix:* add this sentence, or require D1.

### N12. RCSPC-NF and the live laws (items 66, 74)

(a) Line 236 says RCSPC-NF is "stated in §4.7", but §4.7 never names
it. *Fix:* in line 196 write: "**RCSPC-NF (open).** Over a D1 witness
background sharp in every `P_x` and `z_x`, whose `e_1`-ray sectors are
not factor representations and fail (S1)-(S2): does some update and some
covariant representation built from them have a Clifford-node band?"

(b) The draft says the proofs "carry over to `L5-U[m]`" and that on
`L5-O[S_+]` "Lemma 5's mechanism is absent" (`RCSPC_DRAFT.md:342`). The
distillation replaced this with "requires verifying the corresponding
hypotheses" (line 238). The referee closure in §3.8 below verifies the
carry-over and the absence. *Fix:* restore the bullet in the form of
§3.8.

### N13. Prior work used (item 76)

`RCSPC.md` has no "Prior work used" section and starts at §3. The draft
has one (`RCSPC_DRAFT.md:40-60`), with the two inputs the digest missed
(`RCSP16_REFEREE.md` N9; `CG16D.md` Lemma N Step 2). *Fix:* restore it,
with the additions in §4 below, or renumber.

### N14. Wording (items 5, 38), optional

D1's "gauge-fixed subalgebra" should read "local-gauge fixed subalgebra" (`RCSP16.md:19`).
The letter `σ` names both the label map (D7) and the pairing vector
(line 104); rename one, for example `ς` for the pairing vector. Attack B
(line 188): "can vanish asymptotically" should read "is not excluded by
these relations".

---

## 3. Decisions on the named results

### 3.1 Theorem 1 (rigid labels): holds

Every step was rebuilt (items 15-23). Lemma 1.1 is `RCS1.md` Lemma 5.1
with a matrix `W`. Lemma 1.2 is `CG16D.md` Lemma N Step 2 with the
derivative formula added; the formula `m_i∇λ_i=\mathrm{tr}(P_i∇g)`
follows from `\mathrm{tr}((∂P_i)P_k)=0`. Lemma 1.3 holds (N7). Steps
0-4 are complete: the boosts `B_t` shift the joint spectrum by
`(tn_O,tθ_O)`, the shifted graphs are pairwise disjoint when a slope
avoids every `−θ_O`, and separability then kills the spectral weight. The
argument uses finite-dimensional linear algebra, the spectral theorem
for commuting unitaries and Stone-Weierstrass; it is Lean-formalizable.
Only Remark 1.4's gloss is wrong (N3).

### 3.2 Corollaries 2 and 4: hold

Corollary 2 holds once `ω` is translation invariant with the covariant
choice (N4). Its key step is sound: for factor ray sectors the
quasi-equivalence classes give minimal central projections, which the
tick and translations permute, so Theorem 1 applies with stabilizers
`Γ_x`. Corollary 4 holds for `ω′`, `ω_Φ`, `ω_8` and `Ψ_λ` and every
update in the sense of D5, without factoriality, through Proposition 3.
I rebuilt Proposition 3(b)-(c): the image `ŨΠ_cŨ^*` is a strong limit of
`π(τ_{se_1}Y)`; on each summand it pulls back, through the normal
isomorphism, to a central projection `R_x` of `π_x(𝔄^G)″` whose
expectation in `Ω_x` equals its own square by (S2); cyclicity and
centrality then give `R_x∈\{0,1\}`. No factoriality is used. Exactly
one line block results because the inverse tick does the same. Lemma 4.1(b)-(d) was checked line by line. `Jσ_8≠0` follows
because `J^{16}σ_0≠0` and every `J^qσ_0` is the unique invariant of
`Λ^q⊗Λ^{16−q}`. The corner norm `4` follows from the maximally mixed
reduced state of `σ_8`. Proposition L applies (N11 for the general
case). The sectors are spinor class under R-16^str′, which stays an
owner candidate.

### 3.3 Attack A3 on `Ψ_λ`: fails at the named step, correctly

`Ψ_λ` is a product over the corner-star quadruples of `𝒫`. Its loops
change only the ends of plaquette links; on direction-1 lines these are
the links `ℓ_{c,2s}`.
The links `ℓ_{c,2s+1}` join two blocks and lie in no plaquette, so their
target numbers are sharply `8`. The string raises them to a sharp `9` on
its own line and leaves `8` elsewhere. That is (S1), and Proposition 3
excludes a Clifford node for every update. The named step at line 138 is
right. Two remarks. First, the three updates of Lemma 4.1(a) act
trivially on every all-`H_-` vector, so stationarity of `Ψ_λ` is cheap;
this does not weaken Corollary 4, which needs no stationarity. Second,
loops that reach every ray link do not escape either while the state is
a cell-invariant block product of bounded blocks: Theorem 7 covers them,
because Lemma 5 holds in every state.

### 3.4 Lemma 5 and Theorem 7: hold; the GAP is real

Lemma 5 holds for every state and every `m` (item 49): only the creator
of `T_k` touches the target end of `ℓ_k`, so `n_{ℓ_k}B=B(n_{ℓ_k}+1)`,
and Cauchy-Schwarz kills the lowest level. The corrected Theorem 7 holds
(items 51-52). The distiller's GAP is real. The draft's uncorrected
statement is false: N1 gives a block-product background with summable
lowest-level weights along the ray in which sectors on lines at
distance `D` are not disjoint.

### 3.5 Proposition 9 (cone lift): holds

Lemma 8 is the easy direction of Powers' criterion, rebuilt correctly:
a weak cluster point of an escaping bounded family commutes with the
local algebra, so it is a scalar in a factor, and a normal state
evaluates it the same way. Proposition 9 then follows from Corollary 2
and Lemma 5. It is a necessary condition only; no cone-lifting state is
built or excluded.

### 3.6 Corollary 10 (D-reg half-column defects): holds

(S1) holds with the two-arrow projector on the shifted far link, which
is even and gauge invariant. (S2) holds because `CG16D.md` Theorem 9
gives product states of even pure block states. Proposition 3's proof
transfers, although D-reg's `𝔄^G` has odd elements (N10). The quotation
must be corrected (N10). The restriction to LZ1's class can be dropped.
This settles the Clifford form of CG16D-NLP over that state, negatively;
the longitudinal part, the energy question and base-gate compilation
remain open, as line 204 says.

### 3.7 RCSPC-CL, its three attacks and the rigid-plane attempt

The statement at line 182 is well posed. The three attacks are distinct
and each fails where the file says.

- **A (decoupling).** The proof of Theorem 7 needs
  `Φ(XZ_s)=Φ(X)Φ(Z_s)` for the string weight `X` and the level projector
  `Z_s`. `X` runs beside line `c` over its whole length, so clustering in
  distance does not separate them, and the two-qubit example shows that
  no positivity bound holds in general.
- **B (asymptotic flux).** The exact shift `ω_x(f(n))=ν_x(f(n+1_c))`
  moves a transverse dipole by exactly `c_2` relative to the weighted
  background `ν_x`, but nothing controls `ν_x` beyond its support.
- **C (stacking).** Seventeen strings on one line vanish, but quasi-
  equivalence of two single-string limits gives only a normal
  isomorphism, not a local intertwiner that moves a second string. (The
  citation of `RCS1.md` R4 concerns the `L5` laws; on the witness the same
  conclusion follows from Lemma 5, since `B` kills the top level, so
  `B^*B` has a kernel.)

Lemma RL (N2) settles the rigid-plane attempt for the Clifford
question: an exact linear number relation that ties the ray's line to
untouched lines makes sectors on distinct lines disjoint. It does not
decide the bare cone-lift limit (N2). RCSPC-CL stays open, as a lemma on
which three distinct attacks (A, B, C) failed.

**A weaker open lemma suffices.** RCSPC-CL denies the cone lift, which
Proposition 9 derives from quasi-equivalence. The no-node conclusion
needs only the following (proposed wording, not adopted):

> **RCSPC-CL′.** On the witness at `m=16`, no D1 state sharp in every
> `P_x` and `z_x` has covariantly chosen factor `e_1`-ray sectors with
> `π_x` quasi-equivalent to `π_{x+2β}` for every `β` in a subgroup of
> finite index of `Z³`.

RCSPC-CL implies RCSPC-CL′ (Proposition 9). RCSPC-CL′ suffices for "no
update gives a Clifford node on factor spinor-class `e_1`-ray sectors"
(Corollary 2). Each of attacks A, B and C, had it succeeded, would have
proved RCSPC-CL′, so they also count as three failed attacks on it.
RCSPC-CL′ is proved for cell-invariant block products (Theorem 7) and
for states with an exact line-tying number relation (Lemma RL). Four
tests: it fixes no part's target (it is the negated hypothesis of
Corollary 2); it is closed; it settles nothing by premise, being open;
it adds no structure, since it drops the cone-lift condition. P, P, P, P.

### 3.8 `L5-U[m]` and `L5-O[S_+]` (referee closure for N12(b))

*Law-independent results.* Theorem 1, Lemmas 1.1-1.3, Corollary 2 (with
N4), Proposition 3, Lemmas 6 and 8, and Corollary 11 (with N6) use only a
separable covariant representation of a quasi-local `𝔄^G` in which even
local elements commute with local elements of disjoint support. Both
`L5` laws are fermionic quasi-local algebras, where even local elements
commute with every local element on disjoint modes; `RCS1.md:32` gives
the representation class.

*`L5-U[m]`: the mechanism is present.* `RCS1.md:86`: "On U, for a
positively oriented link, `(T_i)_{ab}=(U^{ba}_{ℓ_i})*=r^{ℓ_i,y_{i−1}}_a
r^{ℓ_i,y_i*}_b`", and `B_{r,b}=Σ_a(T_1⋯T_{2r})_{ab}c^†_{x,a}`
(`RCS1.md:195`). The far-end number of `ℓ_i` is bounded (five flavours: "`5−k` for the last index", `RCS1.md:115`),
even and gauge invariant, and only `T_i`'s creator acts on that end. So
`nB=B(n+1)` and Lemma 5's proof applies word for word. Theorem 7
(corrected) and Proposition 9 follow on `L5-U[m]`, since their proofs use
only Lemma 5, Lemmas 6 and 8, Corollary 2 and product factorization.

*`L5-U[2k]`, `k=1,2`, over `ω_AB`: every update.* (S1) holds with
`X_{c,s}` the far-end number of `ℓ_{c,s}` minus `k`, since "each ray link
has end numbers `(k−1,k+1)` from near to far, and every other link has
`(k,k)`" (`RCS1.md:107`). (S2) holds: in each index term the interior
index `a_i` occurs only at `y_i` (far end of `ℓ_i`, near end of
`ℓ_{i+1}`), and the head pairs `c^†_{x,a_0}` with the near end of `ℓ_1`
at `x`. So `B_{r,b}` is a product of factors each inside one site star,
`Φ_AB` is a product of Fock vectors, and the ray state is a product over
site stars with period one cell along the ray, independent of the head,
as in Lemma 4.1(c). Proposition 3 gives: for every update in the sense
of D5, no covariant representation built from these `χ_tot=−1` sectors
(`RCS1.md` R2(d)) has a Clifford-node band. This extends the
no-Clifford-cone clause of `RCS1.md` Theorem 8(d) from the base tick to
every update. Its transverse-flatness clause is not extended, because it
uses tick equivalence (`RCS1.md:125`: "the tick equivalence in (c) make each group invariant").

*`L5-O[S_+]`: the mechanism is absent.* `RCS1.md:195`: "each `(T_i)_{ac}`
is `±iη^{\rm far}_cη^{\rm near}_a`, with one sign for all indices; it is a
self-adjoint unitary." Lemma 5 needs a bounded self-adjoint link
observable `n` with `nW=W(n+1)` for the link factor `W`. For unitary `W`
this reads `W^*nW=n+1`, so `\max\mathrm{spec}(n)+1=\max\mathrm{spec}(n)`,
which is impossible. So no bounded observable is raised by a link
factor, and Lemma 5, Theorem 7 and Proposition 9 do not transfer as
proved. The law-independent results still apply there wherever their
hypotheses are verified. No A3 obstruction for `L5-O[S_+]` follows from
this file, as line 238 says.

---

## 4. Prior work used

Each item is used as cited, with its path; nothing here is re-derived
unless the note says "rebuilt".

- `prior/RCSPC.md` (digest): the list of frozen inputs and failed attempts. Used to check what `RCSPC.md` ports.
- `RCS1.md` definition 3 (line 30), definition 5 (line 32), Lemma 5.1 (lines 72-76), Theorem 5 (line 78), §5 strings and covariant choice (lines 86-91), Lemma 6 (line 95), Corollary 9 and RCS-P (lines 127, 221), R2(a) (lines 165-167). Used to check items 7, 8, 16, 26, 29, 34. **Extended:** Lemma 6 is the last step of Lemma RL (N2).
- `RCS1.md` Theorem 8 (lines 103-125) and R4 (lines 191-195). Used in §3.8 for the `L5-U[2k]` carry-over and for the absence of the mechanism on `L5-O[S_+]`. **Extended:** the no-Clifford-cone clause of Theorem 8(d) to every update (§3.8). *The digest does not cite these two items.*
- `RCSP16.md` definitions 1-6 and Theorems 1, 3, 9, 10 (lines 19-24, 28, 42-48, 92-100). Used to check items 5, 41, 44, 48, 71.
- `RCSP16_REFEREE.md` N1, N7, N9 (lines 106, 118, 122). Used to check items 41, 43 and N11(a).
- `CG16B.md` D1 (line 27), Theorem 4.1(b) (line 87), Theorem 6.2 (lines 130-133), Proposition L (lines 137-146), Example S (line 148). Used to check item 45. **Extended:** Proposition L(ii)-(iii) without stationarity (N11(b)). Theorem 6.2's contraction pattern gives the gauge invariance of `C` in N1.
- `CG16D.md` Lemma N Step 2 (line 75), Theorem 8(iv) (line 107), Theorem 9 (lines 132-134). Used to check items 17, 67, 68. *The digest does not cite Theorem 8(iv), which N10 needs.*
- `CG16S.md` Weyl point (line 96) and RC-W scope (line 140). Used for N6 and item 71.
- `LZ1.md` band and node (line 42). Used for items 10 and 21.
- `RCSPC_DRAFT.md` lines 40-60 (its Prior work used), 237 (uncorrected Theorem 7), 275 (rigid planes), 342 (live laws). Used for N1, N2, N12, N13.
- `origin/main` at `f5af11cd0`: the rotor note (line 32, "explicitly constructed isometry"), the three-axis note (line 46, "a single Z on qubit a moves a vertex charge by 2 e_a"; line 48, "The charges are bosons"), the clock note (line 4). Quote checks only; nothing depends on them.

**Prior work the digest missed.** `RCS1.md` R4's `L5-O[S_+]` sentence,
"each `(T_i)_{ac}` is `±iη^{\rm far}_cη^{\rm near}_a` … it is a
self-adjoint unitary" (line 195), which decides §3.8. `RCS1.md` Theorem
8(b) (line 107), which supplies (S1) on `L5-U[2k]`. `CG16D.md` Theorem
8(iv) (line 107), which shows that D-reg's `𝔄^G` has odd elements.

---

## 5. Required edits to `RCSPC.md`

Required (each is a local text change; no corrected theorem changes):

- **E1** (N4, line 71). Corollary 2: add "Let `ω` be translation invariant and choose the ray sectors covariantly (D3)."
- **E2** (N3, line 67). Remark 1.4: replace "their slopes along each `n_O` take finitely many values" by "at each point of `U`, `∇λ` lies on one of finitely many affine planes `n_O·k=−θ_O`".
- **E3** (N5, line 138). Replace "this extends `RCSP16.md` Theorem 9 from matter-activated updates to all updates" by "this extends the no-Clifford-node clause of `RCSP16.md` Theorem 9 to all updates; its transverse-flatness clause is not extended".
- **E4** (N1, line 156). After "The uncorrected general statement is not established by that proof", add: "It is false: a single-link block product with lowest-level weights `ε_s` summable along `e_1` has non-disjoint ray sectors on lines at distance `D` (`RCSPC_REFEREE.md` N1)."
- **E5** (N2, line 192). Replace the example `n_s=0`, `n_{s+1}=16` (it is a case the draft's sentence allows) by the flavour-mismatch example of N2. Add Lemma RL with its proof, and change the outcome to: "rigid planes, and every exact linear number relation that ties the ray's line to untouched lines, give disjoint sectors on distinct lines, hence no Clifford node; whether such a state can meet the bare cone-lift limit is not decided". Line 194 then reads "the rigid-plane attempt gives no node (Lemma RL) and leaves the bare cone-lift limit undecided".
- **E6** (N6, lines 206-208). Corollary 11: use the Weyl point's own local logarithm, and replace Step 3's equality by `1_Γ(K,W(K))≥1_{B_3}(K)P_i(K)`.
- **E7** (N8, line 87). (S1): index `s∈Z`, or restrict the covariance to `s,s+β_1∈N`.
- **E8** (N9, line 178). Remark 9.2: replace "every bounded function `f` of finitely many target numbers near `(s,L)`" by "every uniformly bounded family `f_s∈𝔄^G` whose supports escape every finite set".
- **E9** (N10, line 202). Quote `CG16D.md:134` verbatim: "The product is therefore of even pure states on disjoint finite blocks".
- **E10** (N11(b), line 212). Add: "Proposition L(i)-(iii) do not use stationarity (`CG16B.md:143-145`), so they apply to every gauge-invariant background sharp in every `P_x` and `z_x`."
- **E11** (N12(a), line 196). Name and state RCSPC-NF there, in the wording of N12(a).
- **E12** (N12(b), line 238). Restore the live-law bullet in the form of §3.8: the carry-over to `L5-U[m]` (Lemma 5, corrected Theorem 7, Proposition 9; every update over `ω_AB` on `L5-U[2k]`, `k=1,2`), and the reason the mechanism is absent on `L5-O[S_+]`.
- **E13** (N13). Restore a "Prior work used" section from `RCSPC_DRAFT.md:40-60`, adding the items §4 marks as missed by the digest.
- **E14** (§3.7, line 182). Add RCSPC-CL′ next to RCSPC-CL, with the two implications stated in §3.7, and carry both by name.

Optional:

- **O1** (N7, line 55). Print the two-term bound of Lemma 1.3.
- **O2** (N10, line 200). Drop "in LZ1's class" from Corollary 10.
- **O3** (N11(a), line 113). Add the base tick itself to the updates for which the four backgrounds are D1.
- **O4** (N14, lines 13, 104, 188). "Local-gauge fixed subalgebra"; rename the pairing vector; "is not excluded by these relations".
- **O5** (item 37, line 100). "Repeat periodically" → "repeat with period one cell along the ray".
- **O6** (item 63, line 190). Attack C: note that `RCS1.md` R4 treats the `L5` laws; on the witness, Lemma 5 shows directly that `B^*B` has a kernel.

---

## 6. Open statements to carry by name

- **RCSPC-CL** (open). On the U(16)-rishon witness at `m=16`, no D1 state sharp in every `P_x` and `z_x` has covariantly chosen factor `e_1`-ray sectors with the cone lift. Three distinct attacks failed: A (decoupling: the string weight runs beside the level projector along its whole length), B (asymptotic flux: the weighted background `ν_x` is not controlled), C (stacking: limit sectors have no composition law). A cone-lifting state is not a cell-invariant block product (Theorem 7's proof gives the limit `q>0`). For rigid planes the bare cone-lift limit is not decided (N2).
- **RCSPC-CL′** (open; proposed wording in §3.7, not adopted). The weaker lemma that Corollary 2 needs: no such state has factor `e_1`-ray sectors quasi-equivalent across a finite-index subgroup of translations. Implied by RCSPC-CL. The same three attacks A, B, C failed on it. Proved for cell-invariant block products (Theorem 7) and for states with an exact line-tying number relation (Lemma RL).
- **RCSPC-NF** (open). Non-factor ray sectors that fail (S1)-(S2); to be stated in §4.7 per E11.
- **RCS-P, Clifford form** (inherited from `RCS1.md`). Narrowed on the witness by Corollaries 2 and 4 and Theorem 7. On `L5-U[2k]`, `k=1,2`, it is narrowed over `ω_AB` to every update (§3.8). On `L5-O[S_+]`, nothing here narrows it.
- **MT1-S[R-CS^str]** in the VC1 vacuum, **R-CS**, **R-16^str′** (owner candidate, not adopted), **RCSP16-BT**, **CG16D-NLP** (longitudinal motion, energy, base-gate compilation), the owner question on cancelling base layers, and the `χ_sp`-to-`χ_tot` bridge on D-reg. All unchanged.

## 7. Freeze recommendation

Freeze `RCSPC.md` after E1-E14. The required edits are local; none
changes the content of Theorem 1, Corollaries 2, 4, 10, 11, Proposition 3,
Lemma 5, the corrected Theorem 7 or Proposition 9. No second referee
pass is needed. When the edits import referee closures (N1, Lemma RL in
N2, N6, N11(b), §3.8), the frozen file should mark them "referee closure,
`RCSPC_REFEREE.md`, unrefereed", as `CG16B.md` and `CG16D.md` do for
theirs.

---

## FINISH

**Proved (this referee; referee closures marked).**

1. Confirmed by line-by-line rebuild: Theorem 1 with Lemmas 1.1-1.3; Corollary 2 (with E1); Proposition 3; Lemma 4.1 and Corollary 4 for `ω′`, `ω_Φ`, `ω_8`, `Ψ_λ` and every update; Lemma 5 (every state, every `m`); Lemma 6; the corrected Theorem 7; Lemma 8; Proposition 9; Corollary 10; Corollary 11 (with E6).
2. Referee closure, N2 (Lemma RL): if a state is sharp in an integer combination of target numbers that has coefficient `1` on the ray's line and `0` on a displaced ray's line, the two ray sectors are disjoint. So rigid planes give no Clifford node; their bare cone-lift limit is not decided. With Theorem 7, this proves the weaker open lemma RCSPC-CL′ (§3.7) for two classes of states.
3. Referee closure, N6: Corollary 11's proof repaired at a Weyl point, where `V(K₀)≠1`.
4. Referee closure, N11(b): `CG16B.md` Proposition L(ii)-(iii) hold without stationarity.
5. Referee closure, §3.8: Lemma 5, the corrected Theorem 7 and Proposition 9 hold on `L5-U[m]`; over `ω_AB` on `L5-U[2k]`, `k=1,2`, no update gives a Clifford node on the `χ_tot=−1` straight-string sectors. On `L5-O[S_+]` no bounded link observable is raised by a link factor, because each link factor is unitary, so Lemma 5's mechanism is absent.

**Counterexamples.**

1. N1: the draft's uncorrected Theorem 7 (`RCSPC_DRAFT.md:237`) is false. A single-link block product with lowest-level weights summable along `e_1` has non-disjoint ray sectors on lines at distance `D`.
2. N2: the draft's sentence "the weight `Σ_bB^*_bB_b` vanishes only where its line cannot be raised" is false. Rigid planes with values in `{8,10}` and nested flavour sets give weight `0` with no link at `16`.
3. N3: Remark 1.4's "slopes along each `n_O` take finitely many values" is false with two orbits.
4. N2 also shows that the distiller's example in the rigid-plane GAP does not refute the draft's sentence: there the weight vanishes because a ray link sits at `16`.

**Open by name.** RCSPC-CL (three failed attacks: A decoupling, B
asymptotic flux, C stacking); RCSPC-CL′ (the weaker form Corollary 2
needs; the same three attacks failed); RCSPC-NF; RCS-P (Clifford form); MT1-S[R-CS^str]
in the VC1 vacuum; R-CS; R-16^str′; RCSP16-BT; CG16D-NLP (longitudinal,
energy, base gates); the owner question on cancelling base layers; the
D-reg `χ_sp`-`χ_tot` bridge.

**What changes downstream.**

- `RCSPC.md`: freeze after E1-E14 (§7).
- MT1-S in the VC1 vacuum: on `L5-U[m]`, with factor ray sectors, an odd Clifford node needs ray sectors quasi-equivalent across a finite-index subgroup, and hence a cone-lifting vacuum (Proposition 9 carried over). A cell-invariant block-product vacuum has no cone lift (Theorem 7). A vacuum with an exact line-tying number relation has disjoint sectors on distinct lines (Lemma RL; its proof uses only the shift relation of Lemma 5 and `RCS1.md` Lemma 6, so it holds on `L5-U[m]`). On `L5-O[S_+]` this part gives no constraint.
- CG16D-NLP: its Clifford form over the columnar state is answered negatively for every update (Corollary 10 with N10).
- RC-W: no node in the classes treated triggers it.
- R-CS and R-16^str′: no reading is adopted or changed. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
