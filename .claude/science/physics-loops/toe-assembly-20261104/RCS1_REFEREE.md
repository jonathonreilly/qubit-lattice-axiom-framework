lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# RCS1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3, the referee, under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. This session wrote neither pass 1 (`RCS1_DRAFT.md`) nor pass 2 (`RCS1.md`). This is one check: one whole-part, line-by-line read. No review of this review was commissioned, and this report reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged and was not read. Every proof in `RCS1.md` was re-derived by hand. Verdicts: CORRECT; ERROR (a false or misjudged line, quoted, with a fix); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. Referee closures are themselves unrefereed. Only the owner adopts.

**Text read.** `RCS1.md` at commit `bec8f2606` on `claude/toe-assembly` (the commit that adds it; the lane brief names it). SHA-256 of the file read: `2ff6b119297bf6f1d72aae86939515989b7a5a5240b9c425d971187902c777bb`. Line numbers below refer to that file.

**Sources read, with commits.** All files are in this folder and were read at `bec8f2606`. The second column gives the lines read.

| File | Lines read | SHA-256 prefix |
|---|---|---|
| `RCS1.md` | 1-155 (all) | `2ff6b119297bf6f1` |
| `RCS1_DRAFT.md` (pass 1) | 1-283 (all) | `36420fe9ef5b1664` (the hash `RCS1.md` records) |
| `LZ1.md` | 1-208 (all) | `8dc59d4d4894fbd4` |
| `LW1_5.md` | 1-100 (definitions, the two laws), 121-251 (§4 Q and G, U; §5 centre, F and K, SC, Σ; §6 Z-U) | `7afb7ee2a52d91cd` |
| `VC1_5.md` | 1-70 (definitions, Theorems 2.1-4.1), 111-118 (Theorem 5.5), 158-180 (R1) | `7461113c411eeda4` |
| `CH1_5UQ.md` | 52-70 (Theorem 3.1), 86-117 (Theorems 3.3, 4.1, 4.2) | `674c2ef458aac936` |
| `MT1.md` | 1-40 (status, amendment, definitions), 186-212 (C4); grep hits at 83, 87, 128, 142-148, 226-228, 246, 252 | `28328ed4c9224387` |
| `EW1.md` | 240-242 and 376 (grep for "coherence" and "1/10") | `ed5f5c30b837c6a8` |
| `TOE_ASSEMBLY.md` | 200-235 (§§3.4-3.5); grep for "R-CS" (no hits) | `8027d9d44eb5fcaf` |
| `LW1_REFEREE.md` | 1-238 (format) | — |
| `Y2W_DRAFT.md` | 1-40 (head format) | — |

Every source hash except `EW1.md` equals the prefix that `RCS1_DRAFT.md` records. The draft read `EW1.md` at `c6adaf987` (prefix `57a8bea50f7f0ea8`); `EW1.md` was frozen at `91faafb18` before the draft was committed. The sentence the draft cites is unchanged; it moved from line 234 to line 242. No other branch was read.

**Working-set entries used, by name.** PS-5 and PS-6r, through the laws `L5-U[m]` and `L5-O[S_+]` of `LW1_5.md` §2. PS-1c, through the cell translations. Results used by name, each with its own hypotheses: `LZ1.md` §1 (update class, `c_z`, D1 states, bands), Theorem 2.1 and RC2 (the tracial state of `L5-U` is a locally gauge-invariant D1 state); `VC1_5.md` Theorem 2.1 (gauge average `E`, density of local invariant elements) and Theorem 4.1 (the tracial state of `L5-O[S_+]`); `LW1_5.md` §§1, 2, 4, 5; `CH1_5UQ.md` Theorems 3.3 and 4.2; `MT1.md` C4; `EW1.md` line 242.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: the GNS construction; the conjugation `J` of a tracial state (rebuilt in R1); polar decomposition of an intertwiner; Zorn's lemma; strong convergence of uniformly bounded nets on a dense set. The spectral theorem for finitely many commuting unitaries and Riesz projections enter only through `RCS1.md`'s own Lemma 5.1. No citation carries a proof step.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The two five-mode laws are read plainly as `LW1_5.md` §2 states them. Where `RCS1.md` needs a specification, this report states one candidate exactly, gives it the four-test check, and adopts nothing.

**Check.** One scratch computation, marked [check] where used: `/tmp/toe-rcs1ref/check_rcs1.py` (SHA-256 prefix `8b48be95b111ae35`), output `out.txt`. Part A tests the Majorana centre factors of Theorem 2 on one `L5-O` site and one `S_+` link (A1-A4). Part B computes `‖B_{r,b}Φ‖²` on `L5-U` for `2r=2,4` ray links and `k=1,2`, in `ω_AB` (B1) and in a flavour-locked state (B2). Dense Jordan-Wigner matrices, double precision, largest space 1024. It ran in 35 s with peak memory 0.8 GB, started at 67% free memory. It guides only and proves nothing.

**Counts.** 75 items: 70 CORRECT, 4 ERROR, 1 INCOMPLETE. The seven distiller definitions count as seven items. The distiller's two GAP paragraphs hold five gaps; all five are real (section 2). The main GAP is decided in section 2.1: it is real in general, by a counterexample (R1), and it closes for the state in which `RCS1.md` proves its counterexample (R2). No ERROR or INCOMPLETE item changes the content of a theorem.

---

## 1. Verdict table

| # | Item (RCS1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved" list (5) | CORRECT | Each listed result is proved below in `RCS1.md`. |
| 2 | §0 GAP, odd-sector identification (7) | CORRECT | The gap is real in general (R1). It closes in `ω_AB` (R2), so Theorem 8 is about odd sectors. Section 2.1. |
| 3 | §0 GAP, localization scope (9, sentence 1) | CORRECT | Real. Repaired statement R3. Section 2.2. |
| 4 | §0 GAP, non-disjointness versus equivalence (9, sentence 2) | CORRECT | Real. Repair under a factor hypothesis. Section 2.3. |
| 5 | §0 GAP, Dirac-cloud obstruction (9, sentence 3) | CORRECT | Real. A concrete reason in section 2.4. |
| 6 | §0 GAP, deconfinement (9, sentences 4-5) | CORRECT | Real as a caution against draft line 280. Section 2.5. |
| 7 | §0 Open by name (11) | CORRECT | |
| 8 | §0 Provenance (13) | CORRECT | Draft hash and HEAD `22dfc60d8…` verified. |
| 9-15 | §1 definitions 1-7 (17-23) | CORRECT (7) | Definition 1 cites `LZ1.md` §1 for `𝔄`; the algebra itself is `VC1_5.md` definition 1, to which LZ1 points. Definition 2: [check A]. |
| 16 | Theorem 1, statement (27) | CORRECT | |
| 17 | Theorem 1, proof (29) | CORRECT | |
| 18 | Theorem 2, statement (31-37) | CORRECT | [check A] |
| 19 | Theorem 2, proof on U (39) | CORRECT | |
| 20 | Theorem 2, proof on O (39) | CORRECT | [check A] |
| 21 | Theorem 2, invariance and factor consequence (39) | CORRECT | |
| 22 | Remark after Theorem 2 (41) | CORRECT | |
| 23 | Theorem 3, statement (45-49) | CORRECT | |
| 24 | Theorem 3, proof: exterior values (51) | CORRECT | |
| 25 | Theorem 3, proof: boundary links and ratio (51) | CORRECT | |
| 26 | Theorem 3, proof: disjointness (51) | CORRECT | |
| 27 | Pattern paragraph (53) | CORRECT | |
| 28 | Theorem 4, statement (55) | CORRECT | |
| 29 | Theorem 4, proof (57) | CORRECT | |
| 30 | Lemma 5.1, statement (61) | CORRECT | |
| 31 | Lemma 5.1, proof: boosted bands (63) | CORRECT | |
| 32 | Lemma 5.1, proof: a monotone eigenvalue branch (65) | CORRECT | |
| 33 | Lemma 5.1, proof: orthogonal ranges against separability (65) | CORRECT | Uses the spectral intertwining of draft Lemma B, Step 2; the distillation should state it. |
| 34 | Lemma 5.1, proof: Newton identities and conclusion (65) | CORRECT | |
| 35 | Theorem 5, statement (67) | CORRECT | "Flat along `n`" needs its definition: `V(K₀+sn)=1` for small `s`. |
| 36 | Theorem 5, proof (69) | CORRECT | |
| 37 | Corollary 5.2 (71) | CORRECT | |
| 38 | String operators and string states (75-79) | CORRECT | [check B] |
| 39 | R-CS^str(e) and MT1-S[R-CS^str(e)] (80) | INCOMPLETE | The quantifiers over the choice of limit points and over the axis are not stated. |
| 40 | Centre values of string states (82) | CORRECT | |
| 41 | Lemma 6, statement (84) | CORRECT | |
| 42 | Lemma 6, proof (86) | CORRECT | |
| 43 | Theorem 7, statement (88) | CORRECT | [check B2] |
| 44 | Theorem 7, proof (90) | CORRECT | |
| 45 | Theorem 8(a), statement (94) | CORRECT | |
| 46 | Theorem 8(b), statement (96) | CORRECT | [check B1] |
| 47 | Theorem 8(c), statement (98) | CORRECT | |
| 48 | Theorem 8(d), statement (100) | CORRECT | It can be strengthened: every such band is odd in the sense of R2. |
| 49 | Theorem 8, proof of (a) (102) | CORRECT | |
| 50 | Theorem 8, proof of (b) (104) | CORRECT | |
| 51 | Theorem 8, proof of (c): tick implementer (106-110) | CORRECT | |
| 52 | Theorem 8, proof of (c): disjointness and tick equivalence (112) | CORRECT | |
| 53 | Theorem 8, proof of (d) (114) | CORRECT | |
| 54 | Corollary 9, statement (116) | CORRECT | |
| 55 | Corollary 9, proof (118) | CORRECT | |
| 56 | Paragraph after Corollary 9 (120) | CORRECT | No band with a node is shown to exist; the counterexample is to existence of a Clifford-node band. |
| 57 | §6, global gauge action trivial on `𝔄^G` (124) | CORRECT | |
| 58 | §6, conditional route through `MT1.md` C4 (124) | CORRECT | |
| 59 | §6, no rotation implementer inside one axis family (124) | CORRECT | |
| 60 | §7, test legend (128) | CORRECT | |
| 61 | §7, R-loc row (132) | CORRECT | Agree with P P P P. |
| 62 | §7, R-CS^str(e) row (133) | ERROR | Test 2 is C, not P. Section 3.1. |
| 63 | §7, R-CS^FMS row (134) | ERROR | Test 3: the stated reason is emptiness, which is a theorem, not a premise. Section 3.1. |
| 64 | §7, R-CS^pair row (135) | CORRECT | Agree with P F F F; the test-3 reason should be the draft's. |
| 65 | §7, R-CS^Dirac row (136) | CORRECT | Agree with P F P C. |
| 66 | §7, R-CS^KR row (137) | CORRECT | Agree with P P P F. |
| 67 | §7, R-CS^BR row (138) | ERROR | Test 1 is C, not P. Section 3.1. |
| 68 | §7, automorphism-form row (139) | CORRECT | Referee closure R4: the displayed strings are not scalar multiples of unitaries. |
| 69 | §7, four tests of the inferred definitions (141) | CORRECT | |
| 70 | §8, RCS-P (145) | CORRECT | One phrase needs rewording (section 3.3). |
| 71 | §8, A1 (147) | ERROR | "near the endpoint" must read "near `x`". The argument is otherwise correct. Section 3.1. |
| 72 | §8, A2 (149) | CORRECT | |
| 73 | §8, A3 (151) | CORRECT | |
| 74 | §8, K (153) | CORRECT | |
| 75 | §8, Downstream (155) | CORRECT | |

---

## 2. The distiller's GAPs

`RCS1.md` marks two GAP paragraphs (lines 7 and 9). Line 9 holds four separate gaps. All five are real. Section 4 gives the referee closures R1-R4 in full.

### 2.1 The main GAP: odd-sector identification (line 7). Decided.

`RCS1.md` line 7: "The open-string operators are odd in the *field-algebra vacuum GNS representation*, when that representation and its parity implementer are specified. Their limit states are representations of the even algebra `𝔄^G`, which has no intrinsic odd subspace. The draft's expression `π(B_{r,b})Ω` is undefined for `π` a representation only of `𝔄^G`. Thus “odd string sector” needs an additional sector/charge identification; the prescription below is a proposal, not a derivation of MT1's odd species. Theorems 7–9 concern the defined representations, without that identification."

The draft line it corrects, `RCS1_DRAFT.md` line 170: "Each is odd in the sense of LZ1: `π(B_{r,b})Ω ∈ H_odd`."

**Verdict.** The gap is real in general. It closes in the state `ω_AB` of Theorem 8. Eight points decide it.

1. **The typing point is right.** By Theorem 4, matter parity `θ` fixes every element of `𝔄^G`. So a representation of `𝔄^G` carries no parity operator of its own. LZ1's `H_odd` is the `−1` eigenspace of `U_θ` on the field GNS space of the vacuum (`LZ1.md` line 27: "Matter parity has implementer `U_θ`; write `H_even`, `H_odd` for its eigenspaces"). The sign convention `U_θΩ=Ω` is the one under which LZ1 Theorem 2.1's "The trivial-pattern subspace is even" holds, since `Ω` lies in that subspace. The limit representations `π_x` are not, in general, subrepresentations of that space. So draft line 170 has no meaning as written.

2. **What holds at finite `r`.** Let `ω` be a locally gauge-invariant D1 state with field GNS data `(H,π,Ω,U_θ)`. Then `ξ_{r,b}=π(B_{r,b})Ω` lies in `H_odd`. It also lies in LZ1's pattern subspace whose pattern flips at `y_{2r}` alone. Proof: `B_{r,b}` is carried at `y_{2r}` in the sense of definition 6, by line 80: "The index is contracted at every site except the far end." It is also `θ`-odd. Theorem 4 gives `Ad c_{y_{2r}}(B_{r,b})=θ(B_{r,b})=−B_{r,b}`; for `z≠y_{2r}`, `Ad c_z` is a gauge automorphism at `z` and fixes `B_{r,b}`. Also `U_θπ(B)Ω=π(θ(B))Ω=−π(B)Ω`. The restriction of `ω_r^{(x)}` to `𝔄^G` is the mixture over `b` of the normalized vector states of the `ξ_{r,b}`, with weights proportional to `‖ξ_{r,b}‖²`. So every approximating string state is an R-loc odd state pinned at the far end. The limit `r→∞` moves the pin to infinity.

3. **The configuration never labels a string sector odd.** Line 82: "Thus the limiting state has the same centre values wherever the background is sharp." Since `c_z` is central in `𝔄^G` and sharp in the cyclic state, `π_x(c_z)` is the background scalar `κ₀(z)` at every sharp site. A parity read from configuration ratios, as Theorem 3's `χ` is, therefore gives `+1`.

4. **Approximants do not label the limit** (R1(b)). In `ω_AB` the restriction `ω_AB|𝔄^G` is the weak-* limit of the vector states of the `θ`-odd vectors `π(c†_{y,1})Ω` as `y→∞`. So "is a limit of `θ`-odd vector states" is not a property of the limit representation.

5. **No equivalence-invariant label extends LZ1's in every D1 state** (R1(a)). In the tracial state of either law, a nonzero subrepresentation of `𝔄^G` on `H_phys` is unitarily equivalent to a subrepresentation on `H_odd`. So no labelling of representations of `𝔄^G` that is invariant under unitary equivalence and passes to subrepresentations can call the first even and the second odd. Hence no identification intrinsic to representations of `𝔄^G` works in every D1 state. This proves line 7's "needs an additional sector/charge identification" for D1 states in general.

6. **Where the configuration does label** (R1(c)). If `ω` is sharp in every `c_z`, then `H_phys` and `H_odd` carry disjoint representations of `𝔄^G`. In such states the configuration labels R-loc's odd sector. String sectors keep the background configuration (point 3), so the configuration cannot label them. R2 uses the region parities instead, which Theorem 2 ties to the boundary flux.

7. **Closure where region parities are sharp** (R2). Call a D1 state `ω₀` *parity-sharp* if `ω₀(P_Λ)=ε_Λ∈{±1}` for every finite `Λ`. For a representation `π` of `𝔄^G` put
\[
 χ_{\rm tot}(π:ω₀)=\operatorname*{s-lim}_{Λ\uparrow\mathbb Z^3}\,ε_Λ\,π(P_Λ),
\]
the strong limit along finite site sets ordered by inclusion, when it exists and equals `±1`. R2 proves four facts. `χ_tot` is invariant under quasi-equivalence (definition 3) and under direct sums. On the field GNS space of `ω₀` the limit is `U_θ`, so `χ_tot` agrees with LZ1's even/odd split. On factor sectors localized relative to the vacuum sector, when that sector is a factor representation, it equals Theorem 3's `χ`. In `ω_AB` it is `−1` on every string sector of Theorem 8 and on every covariant representation of Theorem 8(d). So in `ω_AB` the odd identification needs nothing beyond the background state. Theorem 8 is a counterexample for odd sectors in this sense, not only for "the defined representations".

8. **What remains is a specification, not a lemma.** In backgrounds that are not parity-sharp, `χ_tot` is undefined; the tracial state has `τ(P_Λ)=0` for `Λ≠∅`. There, which representations of `𝔄^G` count as MT1's odd species is part of the owner's R-CS. `χ_tot` is one candidate for parity-sharp backgrounds; section 5 gives its four tests (P, P, C, P). Nothing is proposed for adoption.

Parity-sharp backgrounds on file include `ω_AB`, the witnesses of `VC1_5.md` Theorem 5.5 and `CH1_5UQ.md` Theorem 3.3 (sharp `N_z`), and on `L5-O[S_+]` the witness `ω_0` of `VC1_5.md` Theorem 4.2: `P_Λ` is gauge invariant (Theorem 2), so `ω_0(P_Λ)=Φ_0(P_Λ)=1`, although `ω_0` is half filled.

### 2.2 Localization scope (line 9, sentence 1). Real.

Line 9: "The draft's localization theorem does not show that *every* translation-covariant odd sector retains the vacuum configuration: it assumes finite localization and its defined relative parity." The draft line in question, `RCS1_DRAFT.md` line 127: "An R-CS whose odd sectors carry translations must therefore keep the vacuum configuration everywhere and carry the odd parity in the boundary flux of arbitrarily large regions (Theorem 2)."

The gap is real. Theorem 3 needs finite localization. An implemented translation makes the configuration periodic under it (Theorem 1), and nothing more. Repaired statement, R3: *let `π`, `π₀` be factor representations with `κ₀` cell-periodic, and let `π` be quasi-equivalent to `π∘τ_β` for one `β≠0`. Then the set `D={z: κ_π(z)≠κ₀(z)}` is empty or infinite. If `π` is also localized in a finite region relative to `π₀`, then `D` is empty and `χ(π:π₀)=+1`.* The second sentence is Theorem 3. For a sector that is not localized, the word "odd" needs R2's `χ_tot` or another specification.

### 2.3 Non-disjointness versus equivalence (line 9, sentence 2). Real.

Line 9: "Nor does failure of pairwise disjointness imply equivalence without further hypotheses." The draft lines in question: `RCS1_DRAFT.md` line 218, "rays at different transverse positions must give equivalent sectors (Fredenhagen–Marcu's free-charge situation)", and line 205, "Rays that become equivalent are Fredenhagen–Marcu's "free charge" condition".

The gap is real. The negation of Corollary 9's first hypothesis is non-disjointness. Repair: if the string sectors are factor representations, non-disjointness of two of them is quasi-equivalence (definition 3, last sentence). Theorem 8 does not show that the `π_x` are factors. `RCS1.md` line 145 already states the correct form.

### 2.4 Dirac-cloud obstruction (line 9, sentence 3). Real.

Line 9: "The suggested Dirac-cloud obstruction in A2 needs a defined representation and label decomposition." The draft line in question, `RCS1_DRAFT.md` line 245: "A Dirac-type superposition over rays replaces one label by a distribution of labels; in any state where flux far from matter is frozen, each ray in the superposition is again a tick-conserved label, and the cloud does not remove the obstruction of Theorem 5 without a dynamical mechanism that moves rays."

The gap is real, and Theorem 5 alone cannot close it. Consider sectors built from rays parallel to `e_j`. Their tick-conserved label is the position transverse to `e_j`, and translations shift it by `2β_k`, `k≠j`, only. Theorem 5 with a nonzero `n` needs a label `q` with `q(β·c)=q(c)+n·β`; the transverse label of these components can supply one only if `n_j=0`. So for a cloud with rays along all three axes, the transverse labels supply no `n` for every component at once, and Theorem 5 needs some other tick-conserved label, which the draft does not supply. Whether such a cloud carries a Clifford-node band is not decided here.

### 2.5 Deconfinement (line 9, sentences 4-5). Real, as a caution.

Line 9: "Neither a coherence bound nor an absent specified plaquette layer rules out deconfinement." The draft's A2 and A3 claim only failed steps, which is within what they prove. The draft line the caution applies to is `RCS1_DRAFT.md` line 280: "That is a property of VC1's vacuum, close to Fredenhagen–Marcu's free-charge condition, and it needs dynamics that move flux far from matter (A3, GA1-P-5)." That last clause is unproved. Corollary 9 says only that its hypothesis (i) or (ii) must fail. K (line 153) notes that matter hops act on ray links without any plaquette layer. `RCS1.md` already omits the clause.

### 2.6 Distiller corrections not marked GAP

- Lines 80 and 133, existence of limit points. Correct. Sectors exist if and only if the string norms are positive along an unbounded sequence of lengths. The draft's "Exists exactly when the string norms are positive" is a sufficient condition when read for every length.
- Line 19, "nonzero" in quasi-equivalence. Correct. Without it the draft's definition 7 holds for every pair of representations, through zero subrepresentations.
- Lines 149, 151 and 153. Correct; see 2.4 and 2.5.

---

## 3. Details of the non-CORRECT items

### 3.1 ERRORS

**Item 62 (line 133, R-CS^str(e), test 2).** `RCS1.md`: "| R-CS^str(e): straight strings and covariant limit family of §5 | P | P | C | C |". Test 2 asks whether a reading is open-ended so a part can add to it. Line 7 of the same file says "“odd string sector” needs an additional sector/charge identification". A prescription that needs an identification some part must add is open in exactly test 2's sense. Also, when the limit is not unique, line 80 says "choose one limit point" without saying whether MT1-S[R-CS^str(e)] asks for some choice or every choice (item 39). Fix: test 2 is C, "closed once the odd identification (R2's `χ_tot` in parity-sharp backgrounds; an owner specification elsewhere) and the quantifiers over limit points and axis are fixed".

**Item 63 (line 134, R-CS^FMS, test 3).** `RCS1.md`: "| R-CS^FMS: gauge-invariant odd composites `Φ*ψ` or odd elements of `𝔄^G` | P | P | F | P | Empty as a class of odd field-algebra elements by Theorem 4; it cannot by itself select an odd species. |". Test 3 asks whether a reading settles a downstream question by premise. This reading assumes nothing about dynamics. Its class is empty by Theorem 4, a proved kinematic fact. "It cannot by itself select an odd species" describes emptiness, not a premise. The R-loc row uses the other convention: under R-loc, `LZ1.md` Corollary 2.3 decides MT1-S negatively in every D1 state by a theorem, and the file gives R-loc P on test 3. Fix: test 3 is P, with the limitation "empty on both laws by Theorem 4, so it supplies no candidate". If the owner instead counts "decides MT1-S in every state before any dynamics" as a test-3 failure, then R-loc fails test 3 too. The two rows must use one convention.

**Item 67 (line 138, R-CS^BR, test 1).** `RCS1.md`: "| R-CS^BR: light-cone charge classes | P | P | C | F |". The draft's literature record (`RCS1_DRAFT.md` line 59) quotes Buchholz–Roberts: covariant classes give a representation "satisfying the relativistic spectrum condition". Their light cone is the Minkowski light cone. LZ1's target is a common light cone at long distance. A reading built on a relativistic light cone presupposes that target; that is test 1. If "light cone" means the exact causal cone of the finite-depth tick instead, test 1 passes. The row does not say which. Fix: test 1 is C, "passes only with the tick's causal cone; with the relativistic light cone it presupposes LZ1's target". Test 4 stays F.

**Item 71 (line 147, A1).** `RCS1.md`: "The electric layer is therefore a common phase; only cubes near the endpoint act in the inverse matter layers." Elsewhere the file uses "endpoint" for the far end (line 82: "For `z` different from the far endpoint"). Near the far end the matter is empty, so no cube acts there. The cubes that act are the odd cube containing `x` and the eight even cubes meeting it, as in line 106. Fix: "only the odd cube containing `x` and the eight even cubes meeting it act in the inverse matter layers". With that fix the A1 extension is correct; section 6 re-derives it.

### 3.2 INCOMPLETE

**Item 39 (line 80, R-CS^str(e)).** `RCS1.md`: "For each site residue modulo `2Z³`, choose one limit point and translate it covariantly." And: "The proposed MT1-S[R-CS^str(e)] asks for a Clifford node in a covariant direct sum of subrepresentations quasi-equivalent to these GNS representations". Two quantifiers are missing. (a) Does MT1-S[R-CS^str(e)] hold when some covariant choice of limit points has the node, or only when every choice has it? (b) The same question for the axis `e`. RCS-P (line 145) is existential in `e` and, read plainly, in the choice. Fix: state "for some axis `e` and some covariant choice of limit points", matching RCS-P, or state the universal form and adjust RCS-P. In `ω_AB` the limit exists (Theorem 8(b)), so Theorem 8 is unaffected.

### 3.3 Notes on CORRECT items that bear on the freeze

- **Items 2 and 48 (lines 7 and 100).** By R2, Theorem 8(d) can say more: every band of every covariant representation built from the `ω_AB` string sectors lies in a representation with `χ_tot=−1`, so it is odd in that sense. Line 7's last sentence, "Theorems 7–9 concern the defined representations, without that identification", should be limited to Corollary 9 and to backgrounds that are not parity-sharp.
- **Item 9 (line 17).** "Use `LZ1.md` §1 for the quasi-local field algebra `𝔄`". LZ1 §1 uses the algebra and points to `LW1.md`, `LW1_5.md` and `MT1.md` for it. The definition the draft cites is `VC1_5.md` definition 1. Cite that.
- **Item 33 (line 65).** "The joint spectral measure of the commuting unitaries `(T_1,T_2,T_3,Ũ)` assigns its nonzero range to the graph of `e^{-iλ(K+tn)}`." This needs the intertwining fact of draft Lemma B, Step 2: if a bounded `X` satisfies `T_βX=XM_β` and `ŨX=XM_w` for a scalar `w`, then `P(Γ)X=XM_{1_Γ(K,w(K))}` for every Borel `Γ`. Restore that sentence. The draft's proof of it (polynomials, Stone–Weierstrass, regular measures) is complete.
- **Item 35 (line 67).** "Every band is flat along `n` at each node". LZ1 defines "flat" on a neighbourhood. Define "flat along `n` at `K₀`" as `V(K₀+sn)=1` for all small real `s`, which is what Lemma 5.1 proves.
- **Item 56 (line 120), and Theorem 8.** No band with a node is shown to exist. In the representation built in Theorem 8(c), the labels `x` are shifted freely by all translations, so Theorem 5 with `q(x)=x_j/2`, `j=1,2,3`, already gives `N_1=N_2=N_3=0` there. The phrase "It does not rule out motion along the ray" therefore concerns other covariant representations built from these sectors. The counterexample of line 120 stands: it is to the existence of a Clifford-node band.
- **Item 64 (line 135).** The verdicts P F F F are right. The test-3 reason should be the draft's (`RCS1_DRAFT.md` line 231): any rule that reads one-particle bands from pair spectra "presupposes that separated pairs factorize, which is the deconfinement question".
- **Item 68 (line 139).** "The displayed contracted quantum-link strings are not shown unitary". R4 shows more: they are not scalar multiples of unitaries. The row's verdicts (none) stand until a unitary string is specified.
- **Item 70 (line 145).** "any example must violate transverse pairwise disjointness or tick quasi-equivalence of every sector". The scope of "every" is ambiguous. Reword: "any example must have two non-disjoint sectors at distinct transverse positions, or a sector that is not quasi-equivalent to its tick transform".
- **Labels.** For traceability add the draft numbers: Lemma 5.1 is draft Lemma B, Corollary 5.2 is draft Corollary 5.1, Lemma 6 is draft Lemma D. Theorems 1-5 keep the draft's numbers.
- **Provenance (line 13).** It may note that the draft read `EW1.md` before EW1 was frozen; the cited sentence is unchanged (see "Sources read" above).

---

## 4. Referee closures

These are short complete arguments. They use only `RCS1.md`'s own theorems, the named results, and standard mathematics rebuilt in the text. They are unrefereed.

### R1. Odd labels from representations of `𝔄^G` alone

**R1(a) (tracial state; both laws).** Let `τ` be the tracial state of the quasi-local algebra `𝔄` of `L5-U[m]` or `L5-O[S_+]`. Let `(H,π,Ω)` be its GNS representation, `U_θ` the unitary with `U_θπ(A)Ω=π(θ(A))Ω`, `H_odd` its `−1` eigenspace and `H_phys` the closure of `π(𝔄^G)Ω`. Then there is a nonzero bounded `W:H_phys→H_odd` with `Wπ(A)=π(A)W` on `H_phys` for every `A∈𝔄^G`. So a nonzero subrepresentation of `𝔄^G` on `H_phys` is unitarily equivalent to a subrepresentation on `H_odd`.

`τ` is a locally gauge-invariant D1 state: `LZ1.md` RC2 for `L5-U` ("`τ` is stationary for every update in §1. It is invariant under every lift of the cell group and under every local gauge transformation") and `VC1_5.md` Theorem 4.1 for `L5-O[S_+]` ("`τ` satisfies (i)–(iii)").

*Proof.* `𝔄` is the norm closure of an increasing union of full matrix algebras (the proof of `LZ1.md` RC2), and `τ(AB)=τ(BA)` for all `A,B∈𝔄`. `τ∘θ=τ`, because `τ` is invariant under every automorphism (same proof), so `U_θ` exists. Define `J` on `π(𝔄)Ω` by `Jπ(A)Ω=π(A^*)Ω`. It is well defined and isometric, since `‖π(A^*)Ω‖²=τ(AA^*)=τ(A^*A)=‖π(A)Ω‖²`. It is antilinear, so it extends to an antiunitary on `H` with `J²=1`. For `B,C∈𝔄`, `Jπ(B)Jπ(C)Ω=Jπ(BC^*)Ω=π(CB^*)Ω`. Hence for `A∈𝔄`, `π(A)Jπ(B)Jπ(C)Ω=π(ACB^*)Ω=Jπ(B)Jπ(A)π(C)Ω`, and by density `Jπ(B)J` commutes with `π(𝔄)`. Take `ψ=c_{x,1}` on `L5-U` and `ψ=γ_{x,1}` on `L5-O`. Let `W` be `Jπ(ψ)J` restricted to `H_phys`. It commutes with `π(𝔄^G)`. `WΩ=Jπ(ψ)Ω=π(ψ^*)Ω`, and `‖π(ψ^*)Ω‖²=τ(ψψ^*)`, which is `1/2` on `L5-U` and `1` on `L5-O`. For `A∈𝔄^G`, `Wπ(A)Ω=π(A)WΩ=π(Aψ^*)Ω`. `A` is even by Theorem 4, so `Aψ^*` is odd and `U_θ` negates `π(Aψ^*)Ω`. So `W` maps a dense subset of `H_phys`, hence all of it, into `H_odd`, and `W≠0`. In the polar decomposition `W=V|W|` on `H_phys`, `|W|` commutes with `π(𝔄^G)` there and `V` intertwines. `V` restricted to `(\ker W)^⊥` is the unitary equivalence. ∎

*Consequence.* Suppose a rule assigns "even" or "odd" to representations of `𝔄^G`, is constant on unitary-equivalence classes, and gives every nonzero subrepresentation the label of the representation that contains it. Then in `τ` it cannot label the representation on `H_phys` even and the one on `H_odd` odd: the two equivalent subrepresentations of R1(a) would carry both labels.

*Remark, cited and not used.* Tomita–Takesaki theory gives the same intertwiner, `Jπ(ψ)J` with `J` the modular conjugation, in every D1 state whose GNS vector is separating for `π(𝔄)''`. A state that is pure on `𝔄` is not of this kind.

**R1(b) (approximants do not label the limit).** In `ω_AB` of Theorem 8, for every local `A∈𝔄^G` and every site `y` outside the support of `A`,
\[
 \frac{ω_{AB}(c_{y,1}A\,c^\dagger_{y,1})}{ω_{AB}(c_{y,1}c^\dagger_{y,1})}=ω_{AB}(A).
\]
So `ω_AB|𝔄^G` is the weak-* limit, as `y→∞`, of the restrictions of the vector states of the `θ`-odd vectors `π(c^\dagger_{y,1})Ω`.

*Proof.* `A` is even (Theorem 4) and its support avoids `y`, so `A` commutes with `c_{y,1}`. Then `c_{y,1}Ac^\dagger_{y,1}=A(1−n_{y,1})`. The gauge average `E` of `VC1_5.md` Theorem 2.1 fixes `A` and is a Haar average, so `E(A(1−n_{y,1}))=A\,E(1−n_{y,1})=A(1−N_y/5)`. `Φ_AB` is a product state, `A` and `N_y` are even with disjoint supports, and matter is empty, so `Φ_AB(A(1−N_y/5))=Φ_AB(A)`. Also `ω_AB(A)=Φ_AB(E(A))=Φ_AB(A)`. The case `A=1` gives the denominator `1`. ∎

**R1(c) (sharp configuration separates R-loc's sectors).** Let `ω` be a D1 state of either law with field GNS data `(H,π,Ω,U_θ)`, and let `π(c_z)Ω=κ₀(z)Ω` for every `z`. Then no nonzero bounded `S:H_phys→H_odd` intertwines the two representations of `𝔄^G`.

*Proof.* `c_z` is central in `𝔄^G` (Theorem 1), so `π(c_z)=κ₀(z)` on `H_phys`. Let `A∈𝔄` be local and odd. The proof of `LZ1.md` Theorem 2.1 writes `A=Σ_εA_ε` over sign patterns `ε` on a finite set, with `Ad c_z(A_ε)=ε_zA_ε`, and every nonzero `A_ε` has `∏_zε_z=−1`. Fix such an `ε` and a site `z` with `ε_z=−1`, and put `v=π(A_ε)Ω`. Then `π(c_z)v=ε_zκ₀(z)v`, so `π(c_z)^*v=\overline{ε_zκ₀(z)}\,v`. For `ξ∈H_phys`, `ε_zκ₀(z)⟨v,Sξ⟩=⟨π(c_z)^*v,Sξ⟩=⟨v,Sπ(c_z)ξ⟩=κ₀(z)⟨v,Sξ⟩`. So `⟨v,Sξ⟩=0`. These `v` span a dense subspace of `H_odd`, because `(1−U_θ)/2` maps `π(A)Ω` to `π((A−θ(A))/2)Ω`. Hence `Sξ⊥H_odd`; since `Sξ∈H_odd`, `Sξ=0`. ∎

### R2. Relative total parity in parity-sharp backgrounds

**Setting.** A D1 state `ω₀` is *parity-sharp* if `ω₀(P_Λ)=ε_Λ∈{±1}` for every finite `Λ`; then `ω₀((P_Λ−ε_Λ)²)=0`, since `P_Λ` is a self-adjoint unitary. For a representation `π` of `𝔄^G` write `χ_tot(π:ω₀)=s` if `ε_Λπ(P_Λ)→s·1` strongly along the net of finite site sets ordered by inclusion, with `s∈{±1}`.

**R2(a) (invariance).** If `χ_tot(π:ω₀)=s` and `σ` is quasi-equivalent to `π` in the sense of definition 3, then `χ_tot(σ:ω₀)=s`. If every `σ_i` has `χ_tot(σ_i:ω₀)=s`, so does `⊕_iσ_i`.

*Proof.* Direct sums: every `ε_Λσ(P_Λ)` has norm at most one. Strong convergence on each summand gives it on finite sums of summand vectors. These are dense, and a uniformly bounded net that converges strongly on a dense set converges strongly everywhere. Quasi-equivalence: on a closed `π`-invariant `L⊂H_π` the restricted net still converges to `s`. If a unitary `U:K→L` carries `σ|_K` to `π|_L`, then `ε_Λσ(P_Λ)|_K=U^*(ε_Λπ(P_Λ)|_L)U→s`. By Zorn's lemma choose a maximal family `{K_j}` of mutually orthogonal nonzero closed `σ`-invariant subspaces, each unitarily equivalent to a subrepresentation of `π`. Its orthogonal complement is `σ`-invariant. If it were nonzero, definition 3 would give it a nonzero subrepresentation equivalent to a subrepresentation of `π`, against maximality. So `H_σ=⊕_jK_j`, and the direct-sum case applies. ∎

**R2(b) (agreement with LZ1's grading).** Let `(H₀,π₀,Ω₀)` be the GNS representation of `ω₀` on `𝔄` and `U_θ` as in `LZ1.md` line 27. Then `ε_Λπ₀(P_Λ)→U_θ` strongly. So `χ_tot=+1` on every `π₀(𝔄^G)`-invariant subspace of `H_even`, including the vacuum sector on `H_phys`, and `χ_tot=−1` on every such subspace of `H_odd`.

*Proof.* Sharpness gives `π₀(P_Λ)Ω₀=ε_ΛΩ₀`. Let `A∈𝔄` be local with its matter in `Λ`. `P_Λ` implements parity on the modes of `Λ` and fixes links, so `P_ΛA=θ(A)P_Λ`. Then `ε_Λπ₀(P_Λ)π₀(A)Ω₀=ε_Λπ₀(θ(A))π₀(P_Λ)Ω₀=π₀(θ(A))Ω₀=U_θπ₀(A)Ω₀`. Local vectors are dense and the net is uniformly bounded. ∎

**R2(c) (agreement with Theorem 3).** Let `π,π'` be factor representations of `𝔄^G`, with `π` localized in a finite `Λ` relative to `π'` via `V`. If `χ_tot(π':ω₀)=s'`, then `χ_tot(π:ω₀)=χ(π:π')s'`.

*Proof.* Theorem 3 gives `ε_{Λ'}π(P_{Λ'})=χ\,V^{-1}(ε_{Λ'}π'(P_{Λ'}))V` for every finite `Λ'⊇Λ̂`. These `Λ'` form a tail of the net. Conjugation by a fixed unitary preserves strong convergence. ∎

With `π'` the vacuum sector (assumed a factor representation; `s'=+1` by R2(b)), `χ_tot` is Theorem 3's `χ`.

**R2(d) (the string sectors of Theorem 8).** `ω_AB` is parity-sharp with `ε_Λ=1`. Every string sector `π_x` of Theorem 8 has `χ_tot(π_x:ω_AB)=−1`. So does every covariant representation `(H',π',T',Ũ')` of Theorem 8(d).

*Proof.* Matter is empty in `Φ_AB` and `P_Λ` is gauge invariant, so `ω_AB(P_Λ)=1` sharply. By Theorem 8(b), `N_x=1` and `N_z=0` (`z≠x`) are sharp in `ω_∞^{(x)}`. So `π_x(P_Λ)Ω_x=−Ω_x` whenever `x∈Λ`. Let `A∈𝔄^G` be local and let `Λ` contain `x` and the matter of `A`. `A` is even, so `P_ΛAP_Λ=θ(A)=A`. Then `π_x(P_Λ)π_x(A)Ω_x=π_x(A)π_x(P_Λ)Ω_x=−π_x(A)Ω_x`. Density and uniform boundedness give `χ_tot(π_x:ω_AB)=−1`. Each summand of `π'` is quasi-equivalent to some `π_x`, so R2(a) gives `χ_tot(π':ω_AB)=−1`. ∎

*Consequence.* With `χ_tot` as the odd label, Theorem 8(d) is a statement about odd bands. Under R-CS^str(e), for each axis `e`, MT1-S's asserted odd Clifford node does not exist in `ω_AB`. This holds for the base `L5-U[m]` tick, `m∈{2,4}`, at all constants.

### R3. Configurations of translation-covariant factor sectors

**Statement.** Let `π,π₀` be factor representations of `𝔄^G` with `κ₀` cell-periodic, and let `π` be quasi-equivalent to `π∘τ_β` for one `β≠0`. Then `D={z:κ_π(z)≠κ₀(z)}` is empty or infinite. If `π` is also localized in a finite region relative to `π₀`, then `D=∅` and `χ(π:π₀)=+1`.

*Proof.* Theorem 1 gives `κ_π(z+2β)=κ_π(z)` for every `z`. With `κ₀` periodic, `z∈D` exactly when `z+2β∈D`. A nonempty finite subset of `Z³` is not invariant under a nonzero translation. Under localization in a finite `Λ`, Theorem 3 gives `D⊂Λ̂`, a finite set, so `D=∅` and every ratio in `χ` is `1`. ∎

### R4. The displayed strings are not multiples of unitaries

**Statement.** For every `x`, axis `e`, `r≥1` and `b`, neither `B_{r,b}(x)` nor its dipole variant is a scalar multiple of a unitary; in particular neither is an isometry. So no rescaling of `Ad B_{r,b}(x)` is an automorphism of `𝔄`, and the displayed strings give no instance of the automorphism form.

*Proof.* It suffices that `B^*B` is not a scalar. On `L5-U`, `B_{r,b}=Σ_a(T_1⋯T_{2r})_{ab}c^\dagger_{x,a}`, since link operators commute with matter. It is nonzero (Theorem 8(b) gives a vector it does not annihilate, for suitable `b`; relabel flavours for the others) and it annihilates every vector with all five modes at `x` occupied. So `B^*B` has a nontrivial kernel and is not a scalar. The dipole variant also annihilates every vector with empty matter at `y_{2r}`. On `L5-O[S_+]`, each `(T_i)_{ac}` is `±iη^{\rm far}_cη^{\rm near}_a`, with one sign for all indices; it is a self-adjoint unitary. Write `B_{r,b}=Σ_sW_s` over index sequences `s=(a_0,…,a_{2r−1})`, each `W_s` a product of commuting unitaries on matter and on the ray links. Equal sequences give `W_s^*W_s=1`, so `B^*B=10^{2r}+Y`. Two sequences that differ only in `a_0`, say `a≠a'`, give `W_s^*W_{s'}=γ_{x,a}γ_{x,a'}\,η^{ℓ_1,x}_aη^{ℓ_1,x}_{a'}`, whatever the common tail. Every other pair of different sequences gives a monomial with a Majorana of `ℓ_1`'s far end or of a later link. So `Y` contains `10^{2r−1}Σ_{a≠a'}γ_{x,a}γ_{x,a'}η^{ℓ_1,x}_aη^{ℓ_1,x}_{a'}`, which is not cancelled and is nonzero on `S_+`, since even bilinears act faithfully there. Hence `B^*B` is not a scalar. The dipole variant has the same `a_0`-terms. ∎

---

## 5. The eight candidate prescriptions: four-test verdicts checked

The tests ask whether a reading (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. `RCS1.md` line 128 reports the pass-1 judgments as P, C or F. The table gives the file's verdicts, this referee's verdicts, and the reason for each referee verdict that differs or needs a reason. Agreement is the default; differences are in bold.

| Candidate (line) | File: 1 2 3 4 | Referee: 1 2 3 4 | Reasons |
|---|---|---|---|
| R-loc (132) | P P P P | P P P P | (1) It says where species are read, not what they do. (2) The vacuum fixes its own field GNS representation. (3) LZ1 Corollary 2.3 decides MT1-S under R-loc by a theorem, not by premise. (4) It uses only the law's field algebra. |
| R-CS^str(e) (133) | P P C C | P **C** C C | (2) It needs the odd identification (section 2.1; R2 supplies it in parity-sharp backgrounds) and the quantifiers of item 39. (3) A straight single-ray dressing carries a tick-conserved asymptotic position in frozen backgrounds (Theorem 8); another dressing might not, so a negative verdict in one state can come from the choice. (4) The axis and the end variant are choices the cubic law does not need. |
| R-CS^FMS (134) | P P F P | P P **P** P | Empty on both laws by Theorem 4. (3) Emptiness is a theorem, not a premise; this is R-loc's convention. Its defect is that it supplies no candidate. If the owner counts "decides MT1-S in every state before any dynamics" as a test-3 failure, R-loc fails test 3 too. |
| R-CS^pair (135) | P F F F | P F F F | (2) No fixed inference rule. (3) Any rule that reads one-particle bands from pair spectra presupposes that separated pairs factorize, which is the deconfinement question (the draft's reason, line 231). (4) The rule is structure the law does not supply. |
| R-CS^Dirac (136) | P F P C | P F P C | (2) Weights and representation are unspecified. (3) Like R-CS^str, it supplies no sector where the dressed norms vanish, so it assumes no phase. (4) Weights on rays are added structure. |
| R-CS^KR (137) | P P P F | P P P F | (4) A finite box with external links is absent from the law on `Z³`. |
| R-CS^BR (138) | P P C F | **C** P C F | (1) Built on the relativistic light cone, it presupposes LZ1's common-cone target; built on the tick's exact causal cone, it does not. (3) Its relativistic hypotheses are not shown to apply to the tick. (4) Poincaré covariance and the relativistic spectrum condition are structure the law lacks. |
| Automorphism form (139) | — — — — | — — — — | No instance: the displayed strings are not scalar multiples of unitaries (R4). The tests apply once a unitary string is specified. |

**The referee's own specification.** R2 uses `χ_tot` as the odd label of representations of `𝔄^G` over a parity-sharp background. It is not proposed for adoption. Its four tests:

| Specification | 1 | 2 | 3 | 4 | Reasons |
|---|---|---|---|---|---|
| `χ_tot(π:ω₀)=s-lim ε_Λπ(P_Λ)` over a parity-sharp `ω₀`, odd meaning `−1` | P | P | C | P | (1) It labels sectors and says nothing about nodes or speeds. (2) It is one fixed strong limit of the law's own observables, relative to the stated background. (3) Over parity-sharp backgrounds it decides nothing by premise: Theorem 8's sectors are proved odd, not assumed. It is undefined over other backgrounds; adopted as the general definition, it would leave MT1-S without odd species there by premise. (4) It uses only `P_Λ` and the background's values. |

**The file's inferred definitions (line 141).** The covariant representation, factor representation and configuration, localization, link flux, `Λ̂` and `χ` pass all four tests. This referee agrees. Definition 5 adds only what bands need: `T`, `Ũ`, and separability, which Lemma 5.1 uses. Definition 6 ("carried at") fixes nothing and adds nothing.

---

## 6. Checks behind the verdicts, section by section

### 6.A Section 0 and section 1

- **Provenance.** The SHA-256 of `RCS1_DRAFT.md` at `bec8f2606` is `36420fe9…f94707f`, as line 13 records. The HEAD `22dfc60d8…` is the commit that adds the draft. Every source the draft lists has the hash prefix it records, except `EW1.md` (see "Sources read").
- **Definition 2.** On `L5-U`, `c_z=P_z∏_{ℓ∋z}(−1)^{p_{ℓ,z}}`, since `Q_z` is a sum of commuting number operators. On `L5-O`, `f_{ℓ,z}=Γ^z_ℓ=i^5η^z_1⋯η^z_{10}` is the end chirality of `LW1_5.md` line 85. [check A4]: `(Γ^x)²=1` and `Γ^x=Γ^y` on `S_+`, the eigenspace where `η_1⋯η_{20}=−1`; `LW1_5.md` line 199: "Their product is `η_1⋯η_20=−Γ`, which is `−1` on `S_+`".
- **Definition 3.** The equivalence of the normal-isomorphism form with the subrepresentation form is the standard one. For factor representations, every nonzero subrepresentation is quasi-equivalent to the whole, so non-disjoint factor representations are quasi-equivalent.
- **Definitions 4-7.** They match their uses below. Definition 5 matches `LZ1.md` line 29 for bands; `V` is continuous on `T³` by LZ1's definition, which definition 5 imports.

### 6.B Section 2

- **Theorem 1.** On `L5-U`, `Q_z=𝒢^{1}_z` and `[𝒢^1_z,𝒢^T_z]=𝒢^{[1,T]}_z=0`, so `c_z=e^{iπQ_z}` commutes with every `e^{i𝒢^T_z}`; no group-level integration is needed. On `L5-O`, `LW1_5.md` §4 Q and G: "the Lie algebra representation integrates to its simply connected cover", so `c_z` is the image of a central element of `Spin(10)` and commutes with the group. At a neighbour `w`, the two end actions on the shared link are even bilinears in disjoint modes and commute. So `c_z∈𝔄^G`, and `Ad c_z`, a gauge automorphism at `z`, fixes `𝔄^G`. Gates commute with `c_z` (`LZ1.md` line 25), so `α(c_z)=c_z`. Both `α` and `τ_β` map `𝔄^G` onto itself, because they commute with, or permute, the local gauge automorphisms; so `π∘α` and `π∘τ_β` are factor representations with the stated configurations. `κ²`: `Q_z` has integer spectrum; on `L5-O`, `LW1_5.md` §5 gives `ω_x²=z_x` and Σ gives `z_x=−ε⁶=−1`.
- **Theorem 2 on `L5-O`.** With `X=(i/2)χ_aχ_b`, `X²=1/4`, so `e^{iπX}=2iX=−χ_aχ_b`. The five commuting factors give `−χ_1⋯χ_{10}`. On matter `P=(−i)^5γ_1⋯γ_{10}=−iγ_1⋯γ_{10}`, so the site factor is `−iP`. On a link end, `η_1⋯η_{10}=−iΓ`, so the end factor is `iΓ`. An interior link gives `(iΓ^x)(iΓ^y)=−1` on `S_+`. A boundary link gives `iΓ^{\rm in}`. The scalars collect to `(−i)^{|Λ|}(−1)^{|L_{int}|}i^{|∂Λ|}`. [check A1-A4] agree. All factors commute: matter and links are tensor factors, and the two end products on one link are even in disjoint Majoranas.
- **Theorem 2, invariance.** `Γ^z_ℓ` commutes with each even end bilinear `η^z_cη^z_d`: each of `η_c`, `η_d` anticommutes with nine of the ten factors. `P_z` and `(−1)^{p_{ℓ,z}}` commute with the bilinear generators at `z` and at every other site.

### 6.C Section 3

- **Theorem 3.** (a) For `z∉Λ̂`, no neighbour of `z` lies in `Λ`, so `c_z∈𝔄^G_{Λ^c}` and `V` equates the scalars. (b) A boundary link of `Λ'⊇Λ̂` has its outer end outside `Λ̂`, at distance at least 2 from `Λ`, so its inner end is not in `Λ`. Hence `F_{∂Λ'}∈𝔄^G_{Λ^c}`. `F_{∂Λ'}` is a self-adjoint unitary, so dividing the two instances of Theorem 2 is legitimate. (c) `D` is finite (by (a)) and nonempty (since `χ=−1`). `π∘τ_β` differs from `κ₀` exactly on `D−2β≠D`, so its configuration differs from `κ_π`; Theorem 1 and the factor property give disjointness. An implementer of `τ_β` would be a unitary intertwiner of `π` and `π∘τ_β`.
- **Pattern paragraph.** `ω(|c_z−κ₀(z)|²)=2−2Re(\overline{κ₀(z)}ω(c_z))=0`, so `π(c_z)Ω=κ₀(z)Ω`, and `π(c_z)π(A)Ω=ε_zκ₀(z)π(A)Ω`.
- **Theorem 4.** For local `A` with matter and both link ends in `Λ`, Theorem 2 gives `Ad(∏_{z∈Λ}c_z)(A)=Ad(P_Λ)(A)=θ(A)`, because `F_{∂Λ}` acts on links outside the support of `A`. For carried quasi-local `A` and local `A_n→A`: `‖Ad(∏_{Λ_n}c_z)(A)−θ(A)‖≤2‖A−A_n‖`, and the left side equals `‖Ad c_x(A)−θ(A)‖` once `x∈Λ_n`.

### 6.D Section 4

- **Lemma 5.1.** `M_βS_t=e^{itn·β}S_tM_β` and `M_VS_t=S_tM_{V_t}` with `V_t(K)=V(K+tn)`. With `T_βB_t=e^{−itn·β}B_tT_β`, `G_t=B_tFS_t` satisfies `T_βG_t=G_tM_β` and `ŨG_t=G_tM_{V_t}`. The number of distinct eigenvalues of a continuous Hermitian family is lower semicontinuous, so it is constant on a smaller ball, where the Riesz projections and eigenvalues are `C¹`. If every `n·∇λ_r` vanished there, so would `n·∇tr h^p=Σ_r rank(P_r)pλ_r^{p−1}n·∇λ_r`. With `X_t=G_tM_{Q_t}`, `Q_t=1_BP_r(·+tn)`, Step 2 of draft Lemma B gives `P(Γ_t)X_t=X_t` and `P(Γ_t)X_{t'}=0` for `t≠t'`. The graphs `Γ_t` are disjoint because both eigenvalues lie in `(−π/2,π/2)` and `s↦λ_r(K+sn)` is strictly monotone on `[0,s_1]`. Then `n·∇tr h^p=0`, Newton's identities give a constant characteristic polynomial along `n`, and a nilpotent Hermitian matrix is zero.
- **Theorem 5.** `Ũ` maps each `H_c` onto itself and is unitary, so it commutes with `Π_c` and with `B_t`. `T_βΠ_cT_β^{-1}=Π_{β·c}` gives `T_βB_tT_β^{-1}=e^{−itn·β}B_t`. A Clifford triple gives `(Σ_jn_jN_j)²=v²|n|²`.
- **Corollary 5.2.** A nonempty finite pattern has no nonzero translation stabilizer, so `q_j(τ_βκ_{\rm rep})=β_j` is well defined and shifts by `β_j`.

### 6.E Section 5

- **String operators.** From `LW1_5.md` line 87, `U^{jk}_ℓ=r^y_jr^{x†}_k` for `ℓ=(x,y)`, so `(U^{ba}_{ℓ_i})^*=r^{y_{i−1}}_ar^{y_i†}_b`, as line 75 says. Under `e^{i𝒢^T_z}`, `c^†` and `r^†` transform as the fundamental and `c`, `r` as its dual. So `Σ_ac^†_{x,a}r^{ℓ_1,x}_a` is invariant at `x`, `Σ_ar^{ℓ_i,y_i†}_ar^{ℓ_{i+1},y_i}_a` is invariant at `y_i`, and the open index transforms at `y_{2r}`. For `A∈𝔄^G`, `Σ_bB^*_{r,b}AB_{r,b}` is invariant at `y_{2r}` by unitarity of the transformation. On `L5-O` the contraction is the vector contraction of the hop. Translation covariance: `τ_β(B_{r,b}(x))=B_{r,b}(x+2β)`, so `ω_r^{(x+2β)}=ω_r^{(x)}∘τ_β^{-1}` in a D1 state.
- **Centre values (line 82).** For `z≠y_{2r}`, `Ad c_z` fixes `B_{r,b}`, so `ω_r^{(x)}(c_z)=ω(Σ_bB^*_{r,b}B_{r,b}c_z)/ω(Σ_bB^*_{r,b}B_{r,b})=κ₀(z)` when `π(c_z)Ω=κ₀(z)Ω`.
- **Lemma 6.** For `η=Σ_nπ^{(n)}(Y_n)Ω^{(n)}` with local `Y_n∈𝔄^G`, `X_t` commutes with every `Y_n` once supports are disjoint (both even), so `π_i(X_t)η=c_iη` for large `t`. Uniform boundedness extends this to `π_i(X_t)→c_i` strongly. An intertwiner `S` then satisfies `aS=bS`.
- **Theorem 7.** At `y_1` each term creates flavour `a_1` at the `y_1`-end of `ℓ_1` (needs `a_1∉S(y_1)`) and annihilates `a_1` at the `y_1`-end of `ℓ_2` (needs `a_1∈S(y_1)`). [check B2] gives zero norms for `k=1,2`. Hypotheses: `VC1_5.md` Theorem 5.5, "On every link occupy flavours `1,...,k` at each end", and its full-matter partner; `CH1_5UQ.md` Theorem 3.3, "occupy it in the matter and all six link ends at `x`". Both are flavour-locked and satisfy (i)-(iii), so both are D1.
- **Theorem 8(a).** Each hop term ends in a matter annihilator. `W_E`'s exponent is `(k−m/2)²=0`. The lifts of `VC1_5.md` Theorem 2.2 send `r^{ℓ,z}_j` to `r^{gℓ,gz}_j`, preserve each tiling (`LW1_5.md` line 209), and both ends of a link carry one set, so `Φ_AB` is preserved up to a phase. `E` commutes with `α` and the lifts (`VC1_5.md` Theorem 2.1).
- **Theorem 8(b).** A term with indices `a_0,…,a_{2r−1},b` is nonzero exactly when `a_{i−1}∈S(ℓ_i)` and `a_i∉S(ℓ_i)` for every `i`. Links along `e_1` alternate tilings (`LW1_5.md` line 209: a direction-1 link's tiling is "the parity of its base coordinate `x_1`"), and `S_e∩S_o=∅`. So the conditions reduce to `a_i∈S(ℓ_{i+1})`, `0≤i<2r`, and `b∉S(ℓ_{2r})`. Distinct sequences give distinct occupation vectors with coefficients `±1`. So `‖B_{r,b}Φ_AB‖²=k^{2r}` for `5−k` values of `b`, and `0` otherwise. [check B1] agrees for `k=1,2` and `2r=2,4`. For a local `A` whose last ray link is `ℓ_M`, links `ℓ_{M+1},…` lie outside its support. Then `Σ_b⟨B_{r,b}Φ,AB_{r,b}Φ⟩=(5−k)k^{2r−1−M}Σ_{a_M}⟨v_{a_M},Av_{a_M}⟩`, with `v_{a_M}` independent of `r`; the sign of each link factor is fixed by that link's two indices. The normalized ratio does not depend on `r` once `2r>M`.
- **Theorem 8(c).** `U_0^*=M_e^*M_o^*W_E^*`. `W_E^*` gives one phase, since every term has the same end numbers. In `M_o^*` only the odd cube `C_o(x)` meets matter. Afterwards matter lies in `C_o(x)`, whose eight sites lie in eight distinct even cubes; only those act in `M_e^*`. So `U_0^*B_{r,b}Φ=e^{iφ_r}G_x^*B_{r,b}Φ` with `G_x^*=(∏_se^{ia_eH_{C_s}})e^{−ia_oH_{C_o(x)}}`. This gives `ω_r^{(x)}∘α^{-1}=ω_r^{(x)}∘Ad G_x` on local elements, for every `r≥1`, and in the limit. The map `π_x(A)Ω_x↦π_x(α(A))π_x(G_x^*)Ω_x` is isometric, since `ω_∞(G_xα(A^*A)G_x^*)=ω_∞(A^*A)`, and has dense range. `Ũ_{x+2β}T_β=T_βŨ_x` follows from `τ_β(G_x)=G_{x+2β}` and `ατ_β=τ_βα`. For disjointness, `X_t=(p_{ℓ_t,y_{t−1}}−k)²` is sharp at `1` in `ω_∞^{(x)}` and at `0` in `ω_∞^{(x')}`.
- **Theorem 8(d).** A summand's transverse label is unique, because sectors at distinct labels are disjoint. If `Y` is a summand with label `c`, then `Ũ'Y` carries a representation equivalent to `π'|_Y∘α^{-1}`, quasi-equivalent to `π_x∘α^{-1}≅π_x`. Its projection onto `H'_{c'}`, `c'≠c`, is an intertwiner into a representation disjoint from `π_x`, hence zero. The same holds for `Ũ'^{-1}`. `T'_βH'_c=H'_{c+2(β_2,β_3)}` because `π_x∘τ_β^{-1}` is the GNS representation of `ω_∞^{(x+2β)}`. Theorem 5 with `q(c)=c_2/2` and `c_3/2` finishes. For the other axes: a cell-rotation lift maps `e_1`-strings to strings along the rotated axis (up to matter signs), commutes with `α`, and preserves `Φ_AB`.
- **Corollary 9.** The proof of Theorem 8(d) uses exactly its hypotheses (i), (ii) and translation covariance.

### 6.F Section 6

- A global gauge transformation acts on a local `A∈𝔄^G` as the product of the finitely many local transformations at the sites of its support; each fixes `A`.
- The conditional route is `MT1.md` C4, whose four conditions are (R), (I), (Θ), (σ) on `8×8` Hermitian triples; `Θ_d` is the dressed antiunitary of `MT1.md` line 226 (C6).
- No rotation implementer: `X_t` on the far links of an `e_1`-ray from `x` is sharp at `1` in `π_x`. It is `0` in every sector built on a ray along another axis or along `−e_1`, since such a ray shares at most finitely many links with the `e_1`-ray. Lemma 6 gives disjointness.

### 6.G Section 8

- **A1 extension (with the fix of item 71).** Let `ω=Φ∘E` be a D1 state of the base `L5-U` tick, with `Φ` a product state, empty matter, and sharp end numbers. If `‖B_{r,b}Φ‖>0`, each nonzero term lowers every ray link's near-end number by one and raises its far-end number by one, and changes nothing else. So every term has the same end numbers, `W_E^*` gives one phase, and the cube computation of Theorem 8(c) applies verbatim: `ω_r^{(x)}∘α^{-1}=ω_r^{(x)}∘Ad G_x`. This passes to every covariantly chosen limit point. For transverse disjointness use `X_t=(p_{ℓ_t,y_{t−1}}−p^0_t)²`, with `p^0_t` the background value; it is sharp at `1` in `π_x` and at `0` in `π_{x'}`. Corollary 9 then gives transverse flatness. On `L5-O`, `LZ1.md` line 132: "The `L5-O` Majorana hop need not preserve empty matter."
- **A2.** `CH1_5UQ.md` Theorem 4.2: "the matrices `u_{jk}=λ(U^{jk})` and `v_{jk}=λ(U^{jk*})` obey `||u||,||v||≤1/2`". `EW1.md` line 242: "This matches `GA2_Y2.md`'s coherence bound `κ ≤ 1/10` for `S_±`". Both quotations match the file's use.
- **A3.** `LW1_5.md` line 95: "a plaquette class and its constants are **OPEN law data**, GA1-P-5". The file's use matches.
- **K.** The step that fails is the one named: Theorem 8(c) uses that cube gates away from `x` meet no matter. In a matter-filled state, hops act on ray links.
- **Three attacks.** RCS-P carries three distinct failed attacks, A1 (frozen backgrounds), A2 (free links and Dirac clouds) and A3 (loop condensation), and one failed kill attempt, K. Each names its failing step. This meets the closure rule for an open lemma.

**Lean-formalizability.** Every argument in `RCS1.md` and in R1-R4 has finitely many steps and uses named standard results: the GNS construction, the spectral theorem for finitely many commuting unitaries, Riesz projections of a `C¹` Hermitian family, Newton's identities, polar decomposition, Zorn's lemma, Haar averaging, and the conjugation of a tracial state (rebuilt in R1(a)). No numerical check is used as a proof.

---

## 7. Required edits, open statements, freeze recommendation

### 7.1 Required edits

1. **Line 7 (main GAP).** Keep the first three sentences. Replace the last two by the decision of section 2.1: the identification is not intrinsic to representations of `𝔄^G` in every D1 state (R1(a)); over a parity-sharp background, `χ_tot` gives an odd label that agrees with LZ1's grading and with Theorem 3 (R2); Theorem 8's bands are odd in that sense (R2(d)); Corollary 9 and backgrounds that are not parity-sharp still need the owner's specification. Import R1 and R2 as referee closures.
2. **Theorem 8(d) (line 100) and line 120.** Add: "every such band lies in a representation with `χ_tot(·:ω_AB)=−1` (R2(d))". In line 120, say that Theorem 8 is a counterexample for odd sectors in that sense. Keep "These conclusions do not identify the constructed representation with a physical charged particle."
3. **Line 133.** R-CS^str(e), test 2: C, with the reason of item 62.
4. **Line 134.** R-CS^FMS, test 3: P, with the limitation "empty on both laws by Theorem 4, so it supplies no candidate". Or state the other convention and apply it to R-loc as well.
5. **Line 138.** R-CS^BR, test 1: C, with the reason of item 67.
6. **Line 147.** Replace "only cubes near the endpoint act in the inverse matter layers" by "only the odd cube containing `x` and the eight even cubes meeting it act in the inverse matter layers".
7. **Line 80.** State the quantifiers: MT1-S[R-CS^str(e)] asks for some axis `e` and some covariant choice of limit points, as RCS-P does, or state the universal form and adjust RCS-P.
8. **Line 9.** Add R3 as the repaired localization statement. Add the factor-hypothesis form of the non-disjointness remark. Add the reason of section 2.4 to the Dirac-cloud sentence.
9. **Line 139.** Replace "are not shown unitary" by "are not scalar multiples of unitaries (R4)".
10. **Minor.** Line 17: cite `VC1_5.md` definition 1 for `𝔄`. Line 65: restore the spectral-intertwining sentence of draft Lemma B, Step 2. Line 67: define "flat along `n`". Line 145: reword as in section 3.3. Add the draft numbers of Lemma 5.1, Corollary 5.2 and Lemma 6. Line 135: give the draft's test-3 reason. Line 13: note that `EW1.md` changed after the draft read it, with the cited sentence unchanged.

### 7.2 Open statements to carry, by name

- **R-CS**, the owner's choice. It now includes, for backgrounds that are not parity-sharp, which representations of `𝔄^G` count as MT1's odd species. By R1(a), no label that is invariant under unitary equivalence works in every D1 state.
- **RCS-P** (line 145), with its failed attacks A1, A2, A3 and failed kill attempt K.
- **MT1-S[R-CS^str] in the VC1 vacuum**, with VC1.
- The inherited open lists of `LZ1.md` and `MT1.md` are unchanged.

### 7.3 Freeze recommendation

`RCS1.md` can be frozen with its open statements named, after edits 1-9; edit 10 is minor. Every result it marks as proved was re-derived and holds: Theorems 1-5, 7 and 8, Lemma 5.1, Corollary 5.2, Lemma 6, Corollary 9, the statements of §6, and the extension in A1. The four ERRORs are three four-test judgments and one wording slip. The INCOMPLETE item is a missing pair of quantifiers. None changes a theorem. With edits 1-2, Theorem 8 is a counterexample for odd sectors, in the sense of `χ_tot`, in the state `ω_AB`. The frozen `RCS1.md` will not settle MT1-S or R-CS. It records what is proved toward them and names what is open.

---

## FINISH

**Proved here (referee closures, unrefereed).**
- R1(a): in the tracial state of either law, a nonzero intertwiner of `𝔄^G`-representations maps the even physical sector `H_phys` into the odd sector `H_odd`. So no label of representations of `𝔄^G` that is invariant under unitary equivalence extends LZ1's odd grading in every D1 state.
- R1(b): in `ω_AB`, the vacuum restriction to `𝔄^G` is a weak-* limit of vector states of `θ`-odd vectors.
- R1(c): in a D1 state sharp in every `c_z`, `H_phys` and `H_odd` carry disjoint representations of `𝔄^G`. Under VC1's reading P, `VC1_5.md` Theorem 3.1(a) makes every `c_z` sharp (on `L5-O` apply it to `ic_z`), so this applies there.
- R2: over a parity-sharp background, the relative total parity `χ_tot` is invariant under quasi-equivalence and direct sums, equals `U_θ` on the background's field representation, equals Theorem 3's `χ` on localized factor sectors, and equals `−1` on every string sector of Theorem 8 and on every covariant representation of Theorem 8(d).
- R3: a factor sector quasi-equivalent to its translate by a nonzero cell translation differs from a cell-periodic background configuration on an empty or infinite set.
- R4: the displayed string operators and their dipole variants are not scalar multiples of unitaries.
- Re-derived and confirmed: every theorem, lemma and corollary of `RCS1.md`.

**Counterexamples.**
- To "fermion parity is a unitary-equivalence invariant of representations of `𝔄^G` in every D1 state": the tracial state (R1(a)).
- To "a weak-* limit of `θ`-odd vector states has an odd GNS representation": `ω_AB` with the charge sent to infinity. The limit is the vacuum sector, whose `χ_tot` is `+1` (R1(b), R2(b)).
- To "an R-CS^str(e) family of odd sectors with implemented translations and tick carries an odd Clifford node": `ω_AB` with `χ_tot` as the odd label (Theorem 8 with R2(d)), for each axis.
- From `RCS1.md` itself, confirmed: to "R-CS^str has sectors in every D1 state", the locked states of Theorem 7.

**Open, by name.**
- **R-CS** (owner), including the odd specification over backgrounds that are not parity-sharp.
- **RCS-P**: attacks A1 (frozen backgrounds), A2 (free links and Dirac clouds) and A3 (loop condensation) failed at their named steps; kill attempt K failed.
- **MT1-S[R-CS^str] in the VC1 vacuum**, with VC1. Whether the VC1 vacuum is parity-sharp is part of VC1.

**What changes downstream.**
- `RCS1.md`: edits 1-10 of section 7.1, then freeze.
- MT1-S and LZ1: over a parity-sharp background, the odd label of a charged sector is intrinsic to `𝔄^G` relative to that background (`χ_tot`), and under it Theorem 8 rules out the asserted odd Clifford node in `ω_AB`. Over other backgrounds, an R-CS has to specify what "odd" means for representations of `𝔄^G`; by R1(a), no label invariant under unitary equivalence does this in every D1 state.
- CH1's charged-correlator prescription meets the same point, since it is the same owner question.
- No law, axiom, working-set entry or frozen result changes. Both five-mode laws stay live; neither fails at a named step here.
