lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GA1-5 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as the pass-3 referee under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. The lane ran under the pass-1 lane rules. This session wrote neither pass 1 (`GA1_5_DRAFT.md`) nor pass 2 (`GA1_5.md`). This is one check: one line-by-line read of the whole part. It reviews no other review.

**What this file is.** A referee report. It grants no status. It adopts no law, reading or class, and it changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Referee closure" marks a complete argument written here for a missing step; such closures are themselves unrefereed. "[check]" marks a scratch computation in `/tmp/toe-ga15ref/` (script `check_ga15ref.py`, output `out.txt`; 1.8 s, 250 MB, floating point, largest space 1024-dimensional). A check guides and never proves.

**Sources read, with commits.** Checkout `/Users/jonBridger/toe-worker/repo`, branch `claude/toe-assembly`, HEAD `777739d1a087c2fd641c55403d29a6a87fb1c4b0` throughout. Folder `.claude/science/physics-loops/toe-assembly-20261104/`.

| File | Last commit touching it | SHA-256 (prefix) | Lines read |
|---|---|---|---|
| `GA1_5.md` (refereed text) | `777739d1a` | `eb7d6719ee5473a001587d76ae4b37eb07d532df40aa29cd44971718354d775e` (full) | 1-163, all |
| `GA1_5_DRAFT.md` (pass 1) | `f1c70bdd4` | `de808c9dfd74fcd5` (equals the hash `GA1_5.md` records) | 1-253, all |
| `LW1.md` | `4b65c608f` | `78280bd620800eac` (equals the draft's) | 1-100, 184-215, 399-406, 484-494 |
| `LW1_5.md` | `271c868a4` | `7afb7ee2a52d91cd` (equals the draft's) | 1-110, 119-135, 253-268, 287-289 |
| `LZ1.md` | `13389a568` | `f6171c950bc65c7c` (the draft read `8dc59d4d`; the difference is Amendment 1, as `GA1_5.md` line 11 says) | 1-62, 126-136 |
| `GA2_Y2.md` | `bf403a16a` | `25db8a18aff1d30f` (equals the draft's) | 24-34, 76-92 |
| `TOE_ASSEMBLY.md` | `8e442c884` | `a69284d6505b837b` (the draft read `abf241e1`) | 17-19, 75-104, 125-137, 180-236, 379-399 |
| `EW1.md` | `91faafb18` | `ed5f5c30b837c6a8` | 318-327 |
| `ZM1.md`, `LIT_QLM.md` | | `123684581f2023f4`, `0a77dfad3a0c59e3` (equal to the draft's) | hashed only, to check line 11 |
| `LW1_REFEREE.md`, `Y2W_DRAFT.md` | | | 1-80 and 1-40, format only |

Line numbers below refer to `GA1_5.md` unless a file is named. No other branch was read.

**Working-set entries used, by name.** PS-1 read by PS-1c (its nearest-neighbour clause and cell covariance); PS-5 (five modes per site); PS-6 read by PS-6r (finite link registers); through the laws `L5-U[m]` and `L5-O[S_+]` of `LW1_5.md` §2, both live under `TOE_ASSEMBLY.md` §3.5. Results used by name: `LW1.md` E1, A1a, A2, the dressed factorization (its analytic-subgroup argument) and GA1-P; `LW1_5.md` Q, B1-U (the lift), R (the `S_+` convention, line 134) and B8b-5; `LZ1.md` §1 (D1 state, band, node, propagation) and Theorem 2.2; `GA2_Y2.md` Theorems 2.1, 3.2, 3.4 and Corollary 2.2. The owner decision LZ1-SC is used once, under "What changes downstream".

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-1 is read plainly. Where its words leave a choice that decides GAP (2), this report states two readings, four-tests both, and leaves the choice to the owner.

**Method.** Every proof in `GA1_5.md` was re-derived by hand, and checked against the draft where the distillation shortens it. Every citation of another file was checked against that file's text. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step, closed here where possible). §2 judges the six GAPs the distiller marked. §3 holds the new arguments.

**Counts.** 54 items: 49 CORRECT, 1 ERROR, 4 INCOMPLETE. No ERROR or INCOMPLETE item changes a theorem's content. Six distiller GAPs: all six are real. GAP (2) is decided, conditional on one owner reading. GAPs (4) and (5) are closed. GAP (6) is partly repaired. GAPs (1) and (3) stay open.

---

## 0. Outcome

**GAP (2) is decided; the answer turns on one owner reading.** PS-1 asks for "a unitary map built from finitely many layers of nearest-neighbour gates". Read plainly, a nearest-neighbour gate is an even unitary on two adjacent sites and their link, and gauge invariance and cell covariance are asked of the whole update (reading NN-a). Under NN-a the swap layer `W^{swap}` of Theorem 6.3 is a product of finitely many nearest-neighbour layers, each a `2Z³`-periodic product of disjoint gates (Lemma U, Proposition C). It is covariant under the lift of every element of the cell group, including the rotations about the cell centre (Lemma S1′). So under NN-a the layer of Theorem 6.3 meets all three conditions of `LW1.md` GA1-P. If instead every nearest-neighbour gate must itself be gauge invariant (reading NN-b; equivalently every nearest-neighbour layer), the swap layer cannot be built, and neither can the tiling-cube layer at generic angles (Proposition N). Under NN-b no layer has a propagating physical band in any empty-matter D1 state of `L5-U`. NN-a passes all four tests. NN-b fails tests 3 and 4.

**Other closures.** Theorem 6.3 extends to every `m`, odd included, with a translation identification in place of point reflection (Proposition S-odd). On `L5-O[S_+]` the coherent link symbol has determinant `−1`, so its coset excludes the identity (Lemma D); a site-staggered relabelling turns it exactly into the `SO(10)` Wilson form (Proposition O). The hop kernel `K_ℓ` of `LW1_5.md` B8b-5 is not `Spin(10)`-invariant (Lemma K).

**Recommendation.** Freeze `GA1_5.md` after the required edits of §4. Put GA1-P-NN (the nearest-neighbour reading) to the owner.

---

## 1. Verdict table

Each row is one statement or proof step of `GA1_5.md`, with its line numbers. The six GAPs of line 7 are judged separately in §2. "R*n*" points to a required edit in §4.

| # | Item (`GA1_5.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved below" (5) | CORRECT | Each listed result is proved in §§2–6 of `GA1_5.md`. R13 adds the referee closures. |
| 2 | §0 GAP list (7) | CORRECT | As a record of pass 2. Each GAP is judged in §2 below. |
| 3 | §0 Open by name (9) | CORRECT | As a record of pass 2. R1 adds the owner reading GA1-P-NN; R8 removes the odd-`m` item. |
| 4 | §0 Provenance (11) | CORRECT | The draft hash matches. The hashes of `LW1.md`, `LW1_5.md`, `GA2_Y2.md`, `ZM1.md` and `LIT_QLM.md` match the draft's; `TOE_ASSEMBLY.md` and `LZ1.md` differ, as stated. |
| 5 | §1 laws, gauges, tick, `α` (15) | CORRECT | Matches `LW1.md` line 72 and `LW1_5.md` lines 74–95. |
| 6 | §1 sites, link parity, tilings, `𝒢`, `ε_i`, `s`, plaquette types (17) | CORRECT | |
| 7 | §1 traversal matrices, `W(c)`, `B_p` (19) | CORRECT | The warning about cyclicity for walks that repeat a link is right. |
| 8 | §1 class GA1-P-5 and `W^{cube}` (21–24) | CORRECT | A proposed definition. See row 12 on its four tests. |
| 9 | §1 sectors, `A_R^G`, `𝒩_R`, `𝒩`, `E^v_{ab}` (26) | CORRECT | |
| 10 | §1 D1 state, `H_phys`, band, node, propagation (28) | CORRECT | Same content as `LZ1.md` lines 29–31. |
| 11 | §1 reading R-Φ (30) | CORRECT | A proposed reading, not a theorem. |
| 12 | §1 four-test results (32) | CORRECT | Two notes. Test 4's compilation clause is settled under NN-a (§3.3). Test 2: the class is a fixed list of conditions, but as law data it is a family of laws; PS-6r's "each gate class carries its own named free constant" is met by a member, such as `W^{cube}` with `θ_e, θ_o`, not by the class. R10. |
| 13 | Theorem 2.1 statement (36) | CORRECT | |
| 14 | The pairings `P_0, P_{±1}` (38) | CORRECT | |
| 15 | Proof: incidences (40) | CORRECT | "Transverse" means the in-plane coordinate normal to the link. |
| 16 | Proof: stabilizers and orbits (42) | CORRECT | Checked against draft Lemma G2; the base-parity bookkeeping holds for `δ_i=±1`. |
| 17 | Proof: covariance and the `P₊` curve (44) | CORRECT | `ε_{π(i)}(gx)=δ_iε_i(x)` and `s(gx)=sign(π)s(x)` re-derived. The six steps from the origin were re-traced by hand; the pattern recurs at `(2,2,−2)`. |
| 18 | Theorem 2.2 statement (46) | CORRECT | |
| 19 | Theorem 2.2 proof: star intersections (48) | CORRECT | The members of `ℱ` need not cover every link; the argument never uses covering. |
| 20 | Theorem 2.2 proof: parity-split charges (50) | CORRECT | |
| 21 | Theorem 3.1 statement (54) | CORRECT | |
| 22 | Theorem 3.1 proof (56) | CORRECT | The lift formulas match `LW1_5.md` B1-U (line 261) and A2-5 (line 257). |
| 23 | Remark on mixed plaquettes (58) | CORRECT | Its last sentence changes by R1. |
| 24 | Theorem 4.1 (62–74) | CORRECT | |
| 25 | Theorem 4.2 (76–78) | CORRECT | Links commute with matter (`LW1_5.md` line 33), so slot operators of different links commute rather than anticommute. A direct computation still gives `[E_{ab},E_{ba}]=E_{aa}−E_{bb}` and `[E_{aa}−E_{bb},E_{ab}]=2E_{ab}`. |
| 26 | Theorem 4.3 statement (80) | CORRECT | The symbol `𝒢_R` clashes with the cell group `𝒢`. R11. |
| 27 | Theorem 4.3 proof: corner form (82) | CORRECT | |
| 28 | Theorem 4.3 proof: commutants (84) | CORRECT | |
| 29 | `L5-O` neutral factorization (86) | CORRECT | `S_+=(16,16)⊕(16′,16′)` is the standard branching of a half-spinor of `Spin(20)` to `Spin(10)×Spin(10)`. |
| 30 | Region-wise counterexample (88) | CORRECT | Valid in the star-support convention, as the text says. |
| 31 | CONN attacks A1–A3 (90) | CORRECT | See §2, G1 and G6. R9. |
| 32 | Theorem 5.1 statement (94–98) | CORRECT | `c_m`, `ω_ref(U^{jk})=−c_mδ_{jk}`, `(m/10)tr T`, `C_2(Λ^pC⁵)=3p(5−p)/5` and `(p−5/2)²=25/4−(5/3)C_2` recomputed. |
| 33 | Theorem 5.1 proof (100–102) | CORRECT | |
| 34 | Small-field paragraph (104–109) | CORRECT | The coefficient `−θc_m^4(a/2)` recomputed. In each orientation, even faces, odd faces and each of the two mixed classes make up a quarter of the plaquettes. |
| 35 | Theorem 5.2 (111–113) | INCOMPLETE | It omits `det D`. That determinant is forced: `det D=−1` on `S_+` (Lemma D, §3.7). R2. |
| 36 | Line 115, last sentence | ERROR | Quote: "In both laws, exact symbols do not make the operators unitary or their fluctuations small; `GA2_Y2.md` Theorems 2.1 and 3.2 give the stated finite-register obstructions under their hypotheses." On `L5-O` each entry `U^{ab}` is a Hermitian involution (`GA2_Y2.md` Theorem 3.4: "(U^{ab})^2=1"), hence a unitary operator. Theorem 3.2's link floor is stated for `L5-U` only. Fix in R4. |
| 37 | Theorem 6.1 statement (119–123) | CORRECT | |
| 38 | Theorem 6.1 proof: span (125) | CORRECT | The region must contain both ends of every supported link; "containing the relevant supports" covers this. |
| 39 | Theorem 6.1 proof: dynamics and existence (127) | CORRECT | |
| 40 | Theorem 6.2 statement (129) | CORRECT | |
| 41 | Theorem 6.2 proof (131–133) | CORRECT | The same countable-value argument as `LZ1.md` Theorem 2.2. |
| 42 | Theorem 6.3 statement (135–139) | CORRECT | Its conclusion holds for every `m` with `W^{swap,T}` in place of `W^{swap}` (Proposition S-odd). Under NN-a its layer meets GA1-P (§§3.3–3.4). R1, R8. |
| 43 | Theorem 6.3 proof: the gate (141, up to "twelve incident links") | INCOMPLETE | "their stars" must mean the link-end stars `⊗_{ℓ∋v}Λ^{p_{ℓ,v}}C⁵`. With matter included, as in §4's `Star_v`, the gate is not link-only. The draft says this (`GA1_5_DRAFT.md` line 181). R6. |
| 44 | Theorem 6.3 proof: commutation and covariance (141, rest) | INCOMPLETE | Quote: "Point reflection is carried to point reflection by the cell group, so the gate family is covariant." This omits the form of the lift on links and the phase convention of the identification. Lemma S1′ (§3.4) closes it. R6. |
| 45 | Theorem 6.3 proof: multiplicity (143) | CORRECT | |
| 46 | Theorem 6.3 proof: state and stationarity (145) | CORRECT | The state is also cell invariant: each local density is the normalized isotypic projection, which every lift preserves. |
| 47 | Theorem 6.3 proof: the band (147) | INCOMPLETE | Quote: "swap conjugation moves `A_v` to `A_{a_e(a_o(v))}`". This needs one fixed identification of `a` across sites. Closure in §3.9. R7. |
| 48 | Remark on odd `m` (149) | CORRECT | True as stated. A different identification closes odd `m` (Proposition S-odd). |
| 49 | Theorem 6.4 statement (151) | CORRECT | |
| 50 | Theorem 6.4 proof (153) | CORRECT | Checked: the odd-tiling monomial shift, trace invariance, the inverse-transpose case through the symplectic pairing, and the three-fold rotation step. |
| 51 | GA1-5-Φ and its attacks (157) | CORRECT | Open; the attacks are recorded accurately. |
| 52 | GA1-5-O and its attacks (159) | CORRECT | Open. Attack 2's kernel claim is now proved (Lemma K). R5. |
| 53 | Closing paragraph (161) | CORRECT | |
| 54 | Literature paragraph (163) | CORRECT | The draft's quantum-link core also lists Orland–Rohrlich. R12. |

---

## 2. The distiller's GAPs

**G1 = GAP (1), CONN. Real; open.** Theorem 4.3 is an equivalence: with the neutral algebra and hops added, completeness holds if and only if CONN_R holds. It does not prove CONN_R. The region-wise counterexample (row 30) is valid in its convention. On the attacks: A1's one-site connectivity claim would follow from skew `(U(5),U(7))` Howe duality, which neither `GA1_5.md` nor this report rebuilds. A1 still fails at the step the text names: four plaquette corners move at once. A2's chain decomposition holds on induced boxes (referee closure, §3.9). A2 still fails at its named step: the intermediate sectors must keep every type. A3 uses two standard facts (skew Howe duality, and the exchange property of the weight set of an irreducible `gl(7)`-module). They are not rebuilt and not used here; A3 fails at synchronization whether or not they hold. CONN stays open after A1–A3.

**G2 = GAP (2), nearest-neighbour implementation. Real at pass 2; decided here, conditional on one owner reading.** `LW1.md` line 486 (GA1-P) asks to "Prove that the resulting full layer is gauge invariant, cell covariant and implementable in finitely many allowed nearest-neighbour layers." The word "allowed" is not defined in `LW1.md`. §3.1 states two readings. Under NN-a: every swap gate, and the whole layer `W^{swap}=S_oS_e`, is a finite product of nearest-neighbour layers, each `2Z³`-periodic (Lemma U, Proposition C). The layer is covariant under every lift, including rotations about the cell centre (Lemma S1′). So the pass-2 sentence "the swap band is a counterexample within the *proposed* class, not yet an admissibility result for the law" becomes, under NN-a: Theorem 6.3's layer meets all three conditions of GA1-P. Under NN-b: `W^{swap}` cannot be built, `W^{cube}` cannot be built outside a closed discrete set of angles, and no NN-b layer has a propagating physical band in any empty-matter D1 state (Proposition N). So under NN-b no nearest-neighbour version of the swap layer propagates in an empty-matter D1 state. Whether the class GA1-P-5 is the right plaquette class stays the owner's choice.

**G3 = GAP (3), electric energy and continuum. Real; open.** The text is right. The coherent symbol gives a Wilson quadratic form `−θc_m^4(a/2)∫Σtr F²+O(a²)` at fixed `a`. Every end-number function has a constant symbol on the family (line 98), so the family carries no electric field. GA1(a)(4) is shown for the magnetic half only, in the coherent-symbol sense. The electric half and any continuum statement belong to GA2's Y2-W. Nothing here repairs it.

**G4 = GAP (4), the `L5-O` coset. Real; closed.** The coset is determined. On `S_+` as `LW1_5.md` fixes it, `det D=−1` for every joint eigenvector (Lemma D, §3.7; [check] agrees). So the family `{DRᵀ}` is the whole coset `O(10)∖SO(10)` and does not contain the identity. A site-staggered relabelling `𝐕′_ℓ=Φ_{head}ᵀ𝐕_ℓΦ_{tail}` maps the family bijectively onto `SO(10)` link fields with the same plaquette symbols (Proposition O, §3.7). The smooth-field expansion of lines 104–109 then applies to `𝐕′`. The pass-1 claim "item 4 holds with `c = 1`" (`GA1_5_DRAFT.md` line 153) is true after this relabelling, not before it.

**G5 = GAP (5), the hop kernel. Real; first sentence closed.** The draft's reason was insufficient, as the distiller says. Its conclusion is true: `K_ℓ=(|0_y⟩⊗F_x+F_y⊗|0_x⟩)∩S_+` is not invariant under `Spin(10)_x`, so it is not a sum of multiplicity blocks (Lemma K, §3.8; [check]: dimension 31, and an `so(10)_x` rotation outside `u(5)_x` moves it). The second sentence stands: no covariant multiplicity swap on `L5-O` is checked. That question stays inside GA1-5-O.

**G6 = GAP (6), attacks A2 and A3. Real; A2 repaired.** On an induced box (sites of a rectangular box and the links with both ends in it), two sectors with the same site types differ by hop paths plus plaquette boundaries (§3.9). Without a named box the claim had no definite region; with one it holds. A3's two facts are standard and unused (G1). CONN stays open.

---

## 3. Referee closures

### 3.1 What "nearest-neighbour gate" can mean with link registers

The texts, quoted.
- PS-1 (`TOE_ASSEMBLY.md` line 100): "It acts on the joint possibilities of all sites as a unitary map built from finitely many layers of nearest-neighbour gates, covariant under lattice translations and proper cubic rotations."
- PS-1c (line 180): "the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre".
- PS-6 (line 133): "The update is unchanged when the frame at one site and the registers on its links are changed together."
- `LW1.md` line 190 (A1a): "Each free half-tick is exactly a finite product of nearest-neighbour gate layers repeated over its cell lattice."
- `LW1.md` line 196: "Each dressed cube gate is an exact finite product of even gates on individual edge triples. These factors can be chosen gauge invariant. Hence the base tick has finite depth in nearest-neighbour edge-triple gates."
- `LW1.md` line 28: "with the CAR reading of one site mode and parity superselection".

What they say. PS-1 and PS-6 put covariance and gauge invariance on the update. In `LW1.md` a nearest-neighbour gate is an even gate on one edge triple: the matter of two adjacent sites and the register of the link between them. "Can be chosen gauge invariant" reports an extra property; it does not state a requirement. A1a's layers are periodic under the cell lattice; its fixed corner order is not rotation invariant, so `LW1.md` asks covariance of the composite, not of each layer.

**Reading NN-a (proposed, not adopted).** "For a law with link registers, a nearest-neighbour gate in PS-1 is an even unitary on the matter of two nearest-neighbour sites and the register of the link between them. Gauge invariance (PS-6) and cell covariance (PS-1c) are required of the update, not of each gate or layer."

**Reading NN-b (proposed, not adopted).** NN-a, plus: "each nearest-neighbour gate commutes with every local gauge transformation."

**Remark (layers).** For a layer of pairwise disjoint edge-triple gates, gauge invariance of the layer is equivalent to gauge invariance of each gate. A local gauge transformation at `x` acts on the matter at `x` and on the `x`-ends of the links at `x`. A triple that contains a link at `x` contains `x`. So disjointness lets at most one gate of the layer meet the transformation's support, and conjugation fixes the layer exactly when it fixes that gate. So "every nearest-neighbour layer is gauge invariant" is NN-b.

**Four tests.**

| Reading | 1 target | 2 open-ended | 3 settles physics | 4 unneeded structure |
|---|---|---|---|---|
| NN-a | pass: it states no part's target | pass: support and parity are fixed | pass: the class keeps flat members (Theorem 6.2) and propagating members (Theorem 6.3) | pass: it uses only PS-1's words, `LW1.md`'s edge triples and parity superselection |
| NN-b | pass | pass | **fail**: by Proposition N it fixes in advance that every plaquette layer acts on empty-matter links by end-number phases, and that no physical band propagates in any empty-matter D1 state | **fail**: gauge invariance gate by gate is structure that PS-6's reason, invariance of the update, does not need |

NN-b's failure of test 3 has the shape the owner's check of PS-6r recorded for `LW1.md`'s old text (`TOE_ASSEMBLY.md` line 183): "That closed list banned plaquette gates by premise, which settles in advance part GA1's question". Under NN-a, GA1-P's implementability clause holds for every finite-support member of the class (Proposition C(ii)). That is a consequence, not a premise about physics. The choice is the owner's.

### 3.2 Lemma U (compiling link-only unitaries)

**Setting.** A finite region carries the matter Fock spaces `F_w=ΛC⁵` of its sites (CAR, graded across sites) and the registers `H_ℓ` of its links. `LW1_5.md` line 33: "Links commute with matter and are ordinary tensor factors." `dim H_ℓ≥2` (`C(10,m)≥10` on `L5-U`; 512 on `L5-O[S_+]`). Let `𝒜_w^+` be the even part of the site-`w` CAR algebra. `LW1_5.md` line 33: "The site algebra is `M_{32}(C)`, with even and odd Fock spaces of dimension 16." So `𝒜_w^+≅M_{16}⊕M_{16}`, with central projections `Π_±` onto the two parity spaces. Even site operators commute with every operator at other sites. For a site `w` and a link `ℓ∋w` put `𝒢_{w,ℓ}=𝒜_w^+⊗B(H_ℓ)`. Every unitary in `𝒢_{w,ℓ}` is an even gate supported inside the edge triple of `ℓ`: a nearest-neighbour gate in the sense of NN-a.

**Lemma U.** Let `L′` be a finite set of links that is connected: any two of its links are joined by a chain in `L′` whose consecutive links share a site. Let `S′` be the set of sites shared by two links of `L′`. Then for every unitary `G` on `⊗_{ℓ∈L′}H_ℓ`, the operator `G⊗1` (identity on all matter and all other links) is a finite product of unitaries, each in some `𝒢_{w,ℓ}` with `ℓ∈L′`, `w∈S′∩ℓ`. (If `|L′|=1`, `G⊗1` is itself a gate.)

*Proof.* Let `𝔤` be the real Lie algebra generated by the skew-Hermitian elements of the algebras `𝒢_{w,ℓ}`, `ℓ∈L′`, `w∈S′∩ℓ`. All operators below carry the identity on unnamed factors.

*Step 1.* Let `ℓ≠ℓ′` in `L′` share `w`. Take Hermitian `A` on `H_ℓ`, `B` on `H_{ℓ′}` and Hermitian `T,T′∈𝒜_w^+`. `A` and `B` act on different tensor factors, so
\[
[\,iA\otimes T,\ iB\otimes T'\,]=-(A\otimes B)\otimes[T,T'] = i\,(A\otimes B)\otimes\big(i[T,T']\big).
\]
The real span of `{i[T,T′]}` is `𝔰={K∈𝒜_w^+: K=K^*, tr(KΠ_+)=tr(KΠ_−)=0}`, because the commutators of `M_{16}⊕M_{16}` span `sl_{16}⊕sl_{16}`. So `i(A⊗B⊗K)∈𝔤` for every `K∈𝔰`.

*Step 2.* Choose `K_0=K_+⊕K_−∈𝔰` with `K_±=diag(1,−1,0,…,0)` in each block. Then `K_0²=\tfrac18 1+R` with `R∈𝔰`. For Hermitian `A′` on `H_ℓ`, `i(A′⊗K_0)∈𝒢_{w,ℓ}`, and
\[
[\,i(A\otimes B\otimes K_0),\ i(A'\otimes K_0)\,]=-[A,A']\otimes B\otimes K_0^2 .
\]
The part with `R` lies in `𝔤` by Step 1. So `i(C⊗B)⊗1_w∈𝔤` for `C=i[A,A′]`. These `C` span the traceless Hermitian operators on `H_ℓ`. Exchanging the roles of `ℓ,ℓ′` gives `i(A⊗C′)` for traceless `C′`. With `i·1∈𝔤`, every Hermitian operator on `H_ℓ⊗H_{ℓ′}` is reached: `𝔲(H_ℓ⊗H_{ℓ′})⊗1⊆𝔤`.

*Step 3.* Induct on connected subsets `J⊆L′`. Claim: `i(⊗_{ℓ∈J}A_ℓ)∈𝔤` for all Hermitian `A_ℓ`. Step 2 gives `|J|≤2`. Let `k∉J` share a site with `j∈J`, and write `X′` for a product over `J∖{j}`. (i) For traceless `A_j`: with Hermitian `P,Q` on `H_j`, `[iX′⊗P,\ iQ⊗A_k]=iX′⊗(i[P,Q])⊗A_k`, and the `i[P,Q]` span the traceless operators. The first factor is a product over `J`; the second lies in `𝔲(H_j⊗H_k)`. (ii) For `A_j=1`: with traceless `P≠0`, `[iX′⊗P⊗A_k,\ iP⊗B_k]=iX′⊗P²⊗D`, `D=i[A_k,B_k]`. Write `P²=c1+P_0`, `c>0`, `P_0` traceless; the `P_0` part lies in `𝔤` by (i). So `iX′⊗1⊗D∈𝔤` for every traceless `D`; for `D=1` the operator is a product over `J`. Products span, so the claim holds for `J∪{k}`. Hence `𝔲(⊗_{ℓ∈L′}H_ℓ)⊗1⊆𝔤`.

*Step 4.* Let `𝖧` be the group of finite products of unitaries from the `𝒢_{w,ℓ}`. Each such unitary is the exponential of a skew-Hermitian element of the same finite-dimensional algebra (spectral theorem inside the algebra). So `𝖧` is generated by the one-parameter groups `exp(tX_j)` of a finite basis `X_j` of these skew-Hermitian parts. `LW1.md` lines 198–205 prove, for exactly this situation (finitely many skew-Hermitian generators and the group of their finite words), that this group is the connected analytic subgroup `𝖫` of the Lie algebra they generate. Its last step reads (LaTeX symbols rendered): "The inverse function theorem on the analytic group 𝖫 gives a neighbourhood of its identity contained in 𝖧. Thus 𝖧 is an open subgroup of connected 𝖫, and 𝖧=𝖫." Here `𝖫` has Lie algebra `𝔤`. Write `G=exp(iΘ)` with `Θ` Hermitian. Step 3 gives `iΘ⊗1∈𝔤`, so `G⊗1∈𝖫=𝖧`. □

The gates of the word are not gauge invariant and do not conserve matter number. The circuit passes through gauge-variant intermediate states and returns to `G⊗1` exactly. Only NN-a allows such gates.

[check] A toy version (two 2-dimensional links sharing a site whose even algebra is `M_2⊕M_2`) has Lie closure of real dimension 128, the whole skew part of `B(H⊗H)⊗(M_2⊕M_2)`. `i(A⊗B⊗1)` lies in it for five random Hermitian pairs.

### 3.3 Proposition C (finite nearest-neighbour depth under NN-a)

**Proposition C.** (i) On `L5-U[m]`, every `1≤m≤9`, the automorphism of `W^{swap}=S_oS_e` is a composition of finitely many layers. Each layer is a product of pairwise disjoint gates taken from the algebras `𝒢_{w,ℓ}`, and each layer is invariant under the translations `2Z³`. The same holds for `W^{cube}` at every `θ_e,θ_o`, and for `W^{swap,T}` of §3.6. (ii) Every member of GA1-P-5, on either law, is a composition of finitely many such layers, each invariant under `2kZ³` for some `k≥1` that depends on the member.

*Proof of (i).* Fix a tiling `T` and a cube `C` of it. Its four antipodal pairs `{v,a(v)}` are labelled by the body diagonal `±(a(v)−v)∈{±1}³/±`. Call (tiling, diagonal) the *class* of a pair; there are eight classes. For a pair `X={v,a(v)}`, choose a path of three edges of `C` from `v` to `a(v)`, and let `μ_X` be its middle edge. The link set `L_X=star(v)∪star(a(v))∪{μ_X}` is connected: the links of a star share its centre, and consecutive path edges share a site. Lemma U writes the gate `S_X⊗1` as a word of gates in the algebras `𝒢_{w,ℓ}` with `ℓ∈L_X` and `w` among `v`, `a(v)` and the two inner path sites, all in `C`. Fix one word per class and translate it.

Two pairs of one class differ by `2β`, `β≠0`. Their compiled supports are disjoint. Their sites lie in `C` and `C+2β`, which are disjoint. A common link is of one of three kinds. (α) It joins one of `v,a(v)` to one of `v+2β,a(v)+2β`: impossible, since `2β` is a nonzero even vector and `a(v)+2β−v`, `v+2β−a(v)` have three odd entries, so none is a unit vector. (β) It is `μ_X`, with both ends in `C`, and ends at `v+2β` or `a(v)+2β`, which lie outside `C`: impossible. (γ) The same with `X` and `X+2β` exchanged: impossible. So the words of one class run in parallel: their `j`-th gates form one `2Z³`-invariant layer of disjoint gates. The gates of `S_T` commute pairwise (line 141), so `S_T` is the product of its four class products in any order. On each local observable only finitely many gates act, so the operator identities of Lemma U give the identity of automorphisms (`LW1.md` E1). The depth of `W^{swap}` is the sum of the eight word lengths. For `W^{cube}`: the gate `e^{−iθB_C}` acts on the twelve links of `C`, a connected set; Lemma U uses sites of `C`; distinct cubes of one tiling have disjoint sites and links. `W^{swap,T}` has the same supports as `W^{swap}`. □

*Proof of (ii).* Take a sublayer `W_s=∏_{X∈ℱ_s}g_X`. `ℱ_s` is cell invariant and locally finite, so it has finitely many orbits under `2Z³`: every member meets some link with an end in some cell, a translate of the base cell, and only finitely many members meet the finitely many links with an end in the base cell. For each orbit pick a representative `X_0` and a connected finite link set `X̂_0⊇X_0`; give `X_0+2β` the set `X̂_0+2β`. Lemma U compiles each gate on its `X̂`. Let `δ` bound the diameters of the compiled supports and choose `k` with `2k>δ`. Two members of one orbit with `β≡β′ (mod k)`, `β≠β′`, are translates by a vector of length at least `2k`, so their compiled supports are disjoint. Run each class (orbit, `β mod k`) in parallel; there are finitely many classes; the gates of `W_s` commute, so any order of classes gives `W_s`. Do this for each of the finitely many sublayers. □

So under NN-a GA1-P's implementability clause holds for every member of the class. Under NN-a GA1-P therefore reduces to the owner's choice of a class or member, and to gauge invariance and covariance of the full layer.

### 3.4 Lemma S1′ (covariance of the swap layer)

**Lemma S1′.** Let `g∈𝒢`, and let `α_g` be its lift (`LW1_5.md` B1-U). For each tiling `T` and each antipodal pair `{v,a_T(v)}`, `α_g(S_{\{v,a_T(v)\}})=S_{\{gv,a_T(gv)\}}`. Hence `α_g(S_T)=S_T` and `α_g(W^{swap})=W^{swap}`. This includes the rotations about each cell centre. The same holds for `W^{swap,T}` of §3.6.

*Proof.* (a) `𝒢` preserves each tiling. `LW1.md` A2's proof, line 211: "It sends even cube centres to even cube centres. It sends an odd centre ... to ..., again an odd centre". Its elements are isometries, so `g` carries the cube `C∋v` to the cube `gC∋gv` of the same tiling, and `g(a_T(v))=a_T(gv)`.

(b) For an isometry `g` and a point reflection `P_C` through the centre of `C`, `gP_Cg^{-1}=P_{gC}`, the point reflection through `g`(centre). For the translation identification of §3.6, `gτ_tg^{-1}=τ_{Qt}` with `Q` the linear part of `g`, and `Qt=a_T(gv)−gv`.

(c) The lift on links, quoted from `LW1_5.md` line 261: "On each link send every rishon mode at its `z`-end to the same flavour at the `gz`-end of the image link. This is a permutation of ten rishon modes." The same proof sends `c_{x,j}↦d_g(gx)c_{gx,j}`; matter signs do not act on link operators. So on the twelve links of the gate, `α_g` is implemented by the tensor product `Φ` of the second-quantized rishon permutations. `Φ` sends `v`-end modes to `gv`-end modes of the same colour. Hence `Φ` sends each end-number sector `σ` of the two stars to the transported sector `gσ`. And `ΦΓ_v(u)Φ^{-1}=Γ_{gv}(u)` on the ends for every `u∈U(5)`: both sides act on the end modes by the same matrix `u` and fix the empty vector. So `Φ` maps each isotypic summand `V_λ⊗M_λ` to the summand of the same type `λ`.

(d) `Φι_vΦ^{-1}` and `ι_{gv}` are both induced by the same mode bijection, by (b). On a sector of fixed end numbers two such induced maps agree up to a sign, which comes from reordering creation operators.

(e) On a matched summand of equal type, the gate built from an identification `ι` is `1_V⊗1_V⊗(x⊗y↦ι^{-1}y⊗ιx)` on the multiplicity factors. Replacing `ι` by `cι`, with `c` a unit scalar on that sector, leaves this map unchanged. So `ΦS_{\{v,a(v)\}}Φ^{-1}=S_{\{gv,a(gv)\}}`.

(f) The gates of `S_T` commute, and `g` permutes them, so `α_g(S_T)=S_T`. A rotation about a cell centre is an element of `𝒢` (`LW1.md` line 43: "Write `𝒢=2Z^3⋊O_{c_0}` for these spatial transformations"), so (a)–(e) apply to it. □

In particular the six elements that fix the pair `{v,a(v)}` (the two turns about its diagonal and the three half-turns exchanging `v` and `a(v)`, with the identity) fix the gate. With the base tick's covariance (`LW1_5.md` B1-U), the tick `U_B=W^{swap}W_EM_oM_e` is covariant under each lift. `LW1_5.md` line 267 notes: "The lifts may compose only up to site sign automorphisms; covariance under each lift and site transitivity do not require an exact representation of `𝒢`."

### 3.5 Proposition N (what NN-b allows on empty matter)

Call a unitary on the matter of `x`, `y` and the register of `ℓ=(x,y)` an *NN-b gate* if it commutes with every local gauge transformation.

**Proposition N.** On `L5-U[m]`, `1≤m≤9`:
1. An NN-b gate `g` on `(x,ℓ,y)` commutes with `N_x+N_y`. It maps `E_{xy}=\{N_x=N_y=0\}` into itself and acts there as `Σ_pφ_pΠ_p`, where `|φ_p|=1` and `Π_p` projects on `p_{ℓ,x}=p`.
2. Every finite product of NN-b gates maps the empty-matter subspace `𝒦` of a finite region into itself, and acts on `𝒦` as a function of the end numbers.
3. No finite-depth composition of locally finite layers of NN-b gates induces the automorphism of `W^{swap}` (`m` even) or of `W^{swap,T}` (every `m`, §3.6). None induces the automorphism of `W^{cube}` unless both `θ_e` and `θ_o` lie in a closed discrete set `Θ_m⊂R`.
4. Let `W_B` be a finite-depth composition of locally finite layers of pairwise commuting NN-b gates. In every D1 state of `U_B=W_BW_EM_oM_e` with `ω(N_x)=0` for all `x`, every band with image in `H_phys` is identically `1` on every connected `C¹` neighbourhood of a node. No such band propagates.

*Proof.* (1) `LW1_5.md` line 90 gives the generators `𝒢_x^T=c_x^†Tc_x+Σ_{ℓ′∋x}r_{ℓ′,x}^†Tr_{ℓ′,x}`. The terms of links `ℓ′≠ℓ` act on factors that `g` does not touch. So `g` commutes with `c_x^†Tc_x+r_{ℓ,x}^†Tr_{ℓ,x}` for every Hermitian `T`, and likewise at `y`. With `T=1`: `[g,N_x+p_{ℓ,x}]=0=[g,N_y+p_{ℓ,y}]`. On the register `p_{ℓ,x}+p_{ℓ,y}=m`, so `[g,N_x+N_y]=0`. Both numbers are nonnegative, so `E_{xy}=ker(N_x+N_y)` is invariant. On `E_{xy}` both `c^†Tc` vanish, so `g|_{E_{xy}}` commutes with the end actions of `U(5)_x×U(5)_y`. `E_{xy}≅H_ℓ=⊕_pΛ^pC⁵⊗Λ^{m−p}C⁵`; each summand is irreducible for the product group, and the summands are pairwise inequivalent, since the centre of `U(5)_x` acts on the `p`-th by `e^{ipθ}`. Schur's lemma gives the form.

(2) A gate on `(x,ℓ,y)` acts as the identity on the matter of other sites, so by (1) it maps `𝒦` into itself and acts there as `φ(p_{ℓ,x})`. Products of functions of end numbers are functions of end numbers.

(3) Let `V` be the product of the NN-b gates that act on a given local observable, on a finite region with empty-matter projection `P_0`. By (2), `VP_0=fP_0` and `V^*P_0=f^*P_0`, with `f` a function of the end numbers; so `P_0V=P_0f`. For a link-only `A` (which commutes with `P_0`), `V^*AVP_0=f^*AfP_0`. If `A` commutes with every end number, this is `AP_0`. Now take `A=A_v` of Theorem 6.3 (or of §3.6). The swap automorphism moves it. Let `W` be the product of the gates of `W^{swap}W_E` that act on `A_v`. For `v=2b`, on the support `Q` of the state of Theorem 6.3, `W^*A_vWQ=A_{v−2(1,1,1)}Q≠A_vQ`, since the two operators act as a nonzero traceless `a` on different stars. A link-only operator `X` satisfies `XP_0=X⊗P_0`, and `X⊗P_0=Y⊗P_0` forces `X=Y`. So the two automorphisms differ on `A_v`. For `W^{cube}`, take `A=p_{ℓ,x}` for a link `ℓ` of a cube `C` of tiling `T`. The NN-b composition fixes it on `𝒦`; `W^{cube}` sends it to `e^{iθ_TB_C}p_{ℓ,x}e^{−iθ_TB_C}`. The entire function `θ↦[p_{ℓ,x},e^{−iθB_C}]` has derivative `−i[p_{ℓ,x},B_C]` at `0`. That commutator is `Σ_{q∋ℓ}±(W(∂q)−W(∂q)^†)` over the two faces `q` of `C` that contain `ℓ`, since only their corner moves change `p_{ℓ,x}` (line 82). The four operators shift the end numbers of `C`'s links by four distinct vectors, so they are linearly independent once each is nonzero. Each `W(∂q)` is nonzero on a basis vector whose arriving ends hold colour 1 and whose leaving ends lack it; such vectors exist for `1≤m≤9`. So the function is not identically zero, and its zero set `Θ_m` is closed and discrete. For `θ_T∉Θ_m` the two automorphisms differ on `p_{ℓ,x}`.

(4) Each layer of `W_B` is a product of NN-b gates. By (2) and its adjoint form, `W_BP_0=P_0W_B=fP_0` on each finite region, with `f` a product of single-link functions `φ(p_ℓ)`. The matter gates act as the identity on empty matter, from both sides (`GA1_5.md` line 127). So `U_BP_0=P_0U_B=𝕍′P_0` with `𝕍′=fW_E`, and the computation of line 127 gives `Ũπ(A)Ω=π(𝕍′^*A𝕍′)Ω` for link-only `A`. Line 125's span argument uses only `ω(N_x)=0` and gauge invariance, so `H_phys` is the closed span of `π(A)Ω` over link-only gauge-invariant local `A`. For a finite link set `Y`, the gauge-invariant operators on the registers of `Y` form a finite-dimensional space. It is invariant under `A↦𝕍′^*A𝕍′`: the factors of `𝕍′` on links outside `Y` commute with `A`, and the rest is a gauge-invariant function of end numbers on `Y`. From here the proof of Theorem 6.2 (lines 131–133) applies word for word: pure point spectrum on `H_phys` in a countable set, then the countable-value argument of `LZ1.md` Theorem 2.2. □

The same proof works on `L_cube` with `E_ℓ` in place of `p_{ℓ,x}`, since `LW1.md` line 55 gives `𝒢_x=n_x+Σ_{out}E_ℓ−Σ_{in}E_ℓ`. So under NN-b no plaquette layer of `LW1.md` GA1-P acts on empty-matter links beyond phases in `E`.

### 3.6 Proposition S-odd (the swap band for every `m`)

Line 149 states: "For odd m, no cell-invariant *sharp uniform end-number sector* of this form exists". That is true. But a D1 state need not be rotation invariant, and the gate can use a translation in place of the point reflection.

**Proposition S-odd.** For a tiling `T` and a pair `{v,a_T(v)}`, put `t=a_T(v)−v∈{±1}³`. Build the gate of line 141 with the identification `ι^T_v` induced by the translation `τ_t` in place of point reflection. Call the sublayers `S^T_T` and put `W^{swap,T}=S^T_oS^T_e`. Let `σ^→` be the sector with `p_{ℓ,tail}=⌈m/2⌉` and `p_{ℓ,head}=⌊m/2⌋` on every link. For every `1≤m≤9`:
1. `W^{swap,T}` belongs to GA1-P-5. Under NN-a it meets all three conditions of GA1-P (Proposition C, Lemma S1′).
2. For all allowed `ε,μ,τ_E` there is a locally gauge-invariant D1 state, carried by empty matter and `σ^→`, with a band in `H_phys∩H_even` whose fibre is `V(K)=e^{−iK·(1,1,1)}`. Every `N_j=1`, so the band propagates.
3. The average of this state over the proper rotations is a cell-invariant D1 state with a band of the same fibre.

*Proof.* *Gate.* `τ_t` maps `star(v)` onto `star(a(v))`: the link `(v,v±e_i)` goes to `(a(v),a(v)±e_i)` with its stored orientation kept. So `τ_t` sends tail ends to tail ends and keeps colour. Line 141's construction needs only a colour-preserving bijection of the two stars' end modes, which intertwines the site `U(5)` actions; `ι^T_v` is one, and `ι^T_{a(v)}=(ι^T_v)^{-1}`. Unitarity, gauge invariance, the twelve-link support and commutation within a sublayer follow as in line 141, because the end factors of different pairs are disjoint. Covariance is Lemma S1′ with step (b).

*Sector.* `σ^→` is invariant under every translation, so every pair is matched under `τ_t`. On `σ^→`, `(p_{ℓ,x}−m/2)²` is `1/4` for odd `m` and `0` for even `m` on every link, so `W_E` is a scalar there.

*Multiplicity.* At each site the three outgoing links carry the tail number `p_+=⌈m/2⌉` and the three incoming links carry the head number `p_−=⌊m/2⌋`. The link-end star is `(Λ^{p_+}C⁵)^{⊗3}⊗(Λ^{p_−}C⁵)^{⊗3}`. For `m=1,…,9`, `(p_+,p_−)` runs through `(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(4,4),(5,4)`, so one of them lies in `{1,…,4}`. Line 143's exchange argument, on the three ends that carry it, makes the star commutant noncommutative. So some type `λ_0` has multiplicity `d≥2`. All stars are translates of one another, so one `λ_0` serves every site.

*State.* Take empty matter, the sector `σ^→`, and at each site the normalized projection onto the `λ_0`-isotypic summand of the link-end star. As in line 145 this is a product over stars, invariant under local gauge transformations and under all translations. It is stationary: the matter gates act as the identity on empty matter (line 127), `W_E` is a scalar, and each swap gate preserves the product of equal maximally mixed multiplicity states on a matched summand of equal type. `LZ1.md` line 29: "A **D1 state** `ω` is stationary, even-translation invariant and invariant under each `Ad c_z`." So it is a D1 state. For odd `m` it is not rotation invariant: a rotation reverses some links and sends `σ^→` to another sector.

*Band.* Choose a traceless `a∈End(M_{λ_0})` with `tr a^*a=d`. Let `A_0` be `1⊗a` on the `λ_0` summand of the star at `0` in `σ^→`, zero elsewhere, and put `A_{2b}=τ_b(A_0)` with the translation lift. As in line 147, the vectors `u_b=π(A_{2b})Ω` are orthonormal. On the support of the state the odd swap at `{v,a_o(v)}` conjugates `A_v` to `τ_{t_o}(A_v)`, and the even swap then to `τ_{t_o+t_e}(A_v)`; `W_E` commutes with both. (The induced map `ι^T` and the translation lift agree on each sector up to a sign, which conjugation removes, as in Lemma S1′(d).) For `v=2b`, `a_e(a_o(2b))=2b−2(1,1,1)`, so `t_o+t_e=−2(1,1,1)`, and Theorem 6.1 gives `Ũu_b=u_{b−(1,1,1)}`. Line 147's isometry `F` then gives the band `(1,F,e^{−iK·(1,1,1)})` in `H_phys∩H_even`, with `N_j=1`.

*Average.* For `s∈{±1}³` let `σ^s` put the number `⌈m/2⌉` on the lower end of each `i`-link if `s_i=+1`, and on the upper end if `s_i=−1`; so `σ^→=σ^{(+,+,+)}`. A rotation with `Qe_i=δ_ie_{π(i)}` sends `σ^s` to `σ^{s′}` with `s′_{π(i)}=δ_is_i`. Because `det Q=sign(π)∏_iδ_i=1` and both parities of `π` occur, the proper rotations reach all eight `s`. Each `σ^s` is translation invariant, so the construction applies to each with the same `λ_0` (lifts preserve types). The lifts permute the eight product states, so their average is cell invariant; it is gauge invariant and stationary. On one star the eight sectors are pairwise orthogonal. So with `Ā_v=Σ_sA^s_v` the vectors `π(Ā_{2b})Ω` are orthonormal and move by `−(1,1,1)` per tick. □

For even `m` all `σ^s` equal the sector `σ^*` of line 143, and both `W^{swap}` and `W^{swap,T}` work. The band is neutral in every case: each `A_v` commutes with every end number (line 147). So Proposition S-odd does not touch GA1-5-Φ.

### 3.7 The `L5-O` symbol: Lemma D and Proposition O

`LW1_5.md` line 80 fixes the notation: "`T_{ij}=iη_iη_j/2`, and `U^{ab}=2T_{a,10+b}`, with `η_a=η^y_a` and `η_{10+b}=η^x_b`". Line 134 fixes the register: "On `S_+`, the product of the ten commuting `2T_{2j-1,2j}` is chirality `+1`".

**Lemma D.** `∏_{a=1}^{10}U^{aa}=−∏_{j=1}^{10}2T_{2j−1,2j}` as operators. Hence `∏_aU^{aa}=−1` on `S_+`, every joint eigenvector of the ten `U^{aa}` in `S_+` has `∏_as_a=−1`, and the matrix `D=diag(s_a)` of Theorem 5.2 has `det D=−1`.

*Proof.* `U^{aa}=iη_aη_{10+a}`. Sorting the word `(η_1η_{11})(η_2η_{12})⋯(η_{10}η_{20})` into `η_1⋯η_{20}` takes `9+8+⋯+1=45` transpositions of anticommuting factors. So `∏_a(iη_aη_{10+a})=i^{10}(−1)^{45}η_1⋯η_{20}=η_1⋯η_{20}`. Also `∏_j(iη_{2j−1}η_{2j})=i^{10}η_1⋯η_{20}=−η_1⋯η_{20}`. The factors in each product commute, so the order is immaterial. □

[check] On a 1024-dimensional Jordan–Wigner module the operator identity holds; all 512 joint eigenvectors in `S_+` have `∏_as_a=−1`.

So the family `{DRᵀ:R∈SO(10)}` of Theorem 5.2 is the whole coset `O(10)∖SO(10)`. It does not contain the identity, and no link symbol is `exp(X)` with `X∈so(10)`.

**Proposition O (staggered dictionary).** Let `π(z)=z_1+z_2+z_3 mod 2`, and `Φ_z=D` if `π(z)=1`, `Φ_z=1` if `π(z)=0`. For a link `ℓ` with tail `x` and head `y` and family symbol `𝐕_ℓ=DR_ℓᵀ`, put `𝐕′_ℓ=Φ_yᵀ𝐕_ℓΦ_x`. Then:
1. `𝐕′_ℓ∈SO(10)`, and `𝐕↦𝐕′` is a bijection from the family onto `SO(10)^{links}`.
2. For every plaquette, the symbol of `W(∂p)` equals `tr` of the ordered holonomy of `𝐕′` (`𝐕′` forward, `𝐕′ᵀ` backward). So `ω(B_p)=2 tr H′_p`, with `H′_p∈SO(10)`.
3. Local `SO(10)` rotations `g_z` act on `𝐕′` as ordinary gauge transformations by `Φ_zᵀg_zΦ_z∈SO(10)`.
4. Hence lines 104–109 apply to `𝐕′_ℓ=exp(iaA_ℓ)` with `A_ℓ` Hermitian and `iA_ℓ∈so(10)`: `Σ_p(10−tr H′_p)=(a/2)∫d³xΣ_{i<j}tr F_{ij}²+O(a²)` on a fixed box.

*Proof.* (1) Every link joins sites of opposite `π`, so exactly one of `Φ_x,Φ_y` is `D`; `det 𝐕′=(−1)(−1)=1`. The inverse map is `𝐕=Φ_y𝐕′Φ_xᵀ`, and `R_ℓ` ranges over all of `SO(10)`. (2) Line 111: "product-state plaquette symbols are the ordered products of these matrices, with two backward minus signs". A backward traversal has symbol `−𝐕ᵀ`; the two signs cancel, so the symbol is `tr(𝐕_4ᵀ𝐕_3ᵀ𝐕_2𝐕_1)` for forward links `ℓ_1,ℓ_2` and backward `ℓ_3,ℓ_4`. Insert `𝐕_ℓ=Φ_y𝐕′_ℓΦ_xᵀ`; at each intermediate corner `ΦᵀΦ=1` cancels, leaving `Φ_x H′_p Φ_xᵀ`, whose trace is `tr H′_p`. `B_p=2W(∂p)` because `W(∂p)` is Hermitian on `L5-O` (Theorem 3.1). (3) Direct substitution. (4) For a real antisymmetric `X`, `tr(1−e^X)=−tr(X²)/2+O(X⁴)`, which is line 109's expansion with `X=ia²F`. □

Four tests for this dictionary, a definition: (1) it states no target, pass; (2) it is fixed, pass; (3) it computes a symbol and decides no coupling or continuum question, pass; (4) it uses only the bipartite parity of `Z³` and the given `D`, pass.

### 3.8 Lemma K (the `L5-O` hop kernel)

`LW1_5.md` line 287 (B8b-5): "Let `d^x_j,d^y_k` be the auxiliary annihilators and `K_ℓ` the joint kernel of the represented `d^y_kd^x_j`." Take, at each end, the complex structure that pairs `η_{2k−1}` with `η_{2k}`, as for matter in `LW1_5.md` line 29 (`c_j=(γ_{2j-1}+iγ_{2j})/2`): `d_k=(η_{2k−1}+iη_{2k})/2`. Let `F_y,F_x` be the five-mode Fock spaces of the two ends. Then `iη_{2k−1}η_{2k}=2d_k^†d_k−1`, so `∏_j2T_{2j−1,2j}=(−1)^{N_y+N_x}` and `S_+` is the sum of the blocks `(N_y,N_x)=(n,n′)` with `n+n′` even.

**Lemma K.** `K_ℓ=(|0_y⟩⊗F_x+F_y⊗|0_x⟩)∩S_+`, of dimension 31. `K_ℓ` is not invariant under `Spin(10)_x`. So it is not a sum of `Spin(10)_y×Spin(10)_x` multiplicity blocks.

*Proof.* Each `d^y_kd^x_j` maps block `(n,n′)` into block `(n−1,n′−1)`, so `K_ℓ` is the sum of its parts in the blocks. In a block with `n,n′≥1`, up to block signs from the fermion order, the 25 operators act as `d_k⊗d_j` on `Λ^nC⁵⊗Λ^{n′}C⁵`. The map `ψ↦(d_kψ)_k` from `Λ^n` to `C⁵⊗Λ^{n−1}` is injective for `n≥1`, since `ψ=n^{-1}Σ_ke_k∧d_kψ`. A tensor product of injective maps is injective, so the joint kernel in such a block is `0`. Blocks with `n=0` or `n′=0` lie in the kernel. In `S_+` these give `16+16−1=31` dimensions. For non-invariance, `LW1_5.md` line 123 gives `L_x^{cd}=T_{10+c,10+d}`; take `L=T_{11,13}=iη^x_1η^x_3/2`. Then `e^{−iθL}=cos(θ/2)+sin(θ/2)η^x_1η^x_3`, and `η^x_1η^x_3|0_x⟩=d^{x†}_1d^{x†}_2|0_x⟩`. For `ψ=d^{y†}_1d^{y†}_2|0_y⟩⊗|0_x⟩∈K_ℓ∩S_+`, `e^{−iθL}ψ` has a nonzero component in block `(2,2)` when `θ∉2πZ`, so it leaves `K_ℓ`. A sum of multiplicity blocks would be invariant. □

[check] `dim K_ℓ=31` on `S_+`; `‖(1−P_K)e^{−0.7iT_{11,13}}P_K‖_F≈1.33`; the control `T_{11,12}`, inside `u(5)_x`, gives `0`.

The same proof works for any complex structure at the ends, because `SO(10)` does not preserve a complex structure on `R^{10}`. Lemma K proves the draft's conclusion (`GA1_5_DRAFT.md` line 220). It does not decide GA1-5-O: a covariant swap that preserves the hop-inert vectors is still neither built nor excluded.

### 3.9 Two smaller closures

**A2 on an induced box (for G6).** Let `R` be an induced box: the sites of a rectangular box and the links with both ends in it. Let `σ,σ′∈S(λ⃗)`. The centre of `U(5)_v` acts on the type `λ_v` by `e^{iQ_vθ}`, so `Q_v(σ)=Q_v(σ′)` at every site. Put `j_ℓ=p_{ℓ,head}(σ′)−p_{ℓ,head}(σ)`; the register fixes `p_{ℓ,tail}+p_{ℓ,head}=m`, so `p_{ℓ,tail}` changes by `−j_ℓ`. Equal `Q_v` then gives `N_v(σ′)−N_v(σ)=−(∂j)_v` with `∂` the boundary of the 1-chain `j`, so `Σ_v(N_v(σ′)−N_v(σ))=0`. Join the sites where `N` rises to those where it falls by lattice paths in `R`; these are hop paths. Subtracting them leaves a 1-cycle in `R`. Every closed walk in `R` is a sum of plaquette boundaries in `R`: `LW1.md` line 213 shows that "commuting adjacent coordinate steps and cancelling backtracks reduces any closed lattice path to elementary face loops", and in a box each such step stays in the box, since a box is a product of intervals. An integer 1-cycle is a sum of closed walks. So `σ′−σ` is a sum of hop paths and plaquette boundaries. A2 still fails where `GA1_5.md` line 90 says: the intermediate sectors need not stay in `S(λ⃗)`.

**The identification in Theorem 6.3's band (row 47).** Define `A_{2b}=τ_b(A_0)` with the translation lift. At the odd antipode `a_o(v)` define the transported operator through `ι_{o,v}`. For `v=2b`, the odd cube containing `v` has centre `2b−c_0` and the next even cube has centre `2b−3c_0`. So `P_{C_e}P_{C_o}` is the translation by `2((2b−3c_0)−(2b−c_0))=−2(1,1,1)`. Hence `ι_eι_o` is induced by the same mode bijection as the translation lift `τ_{−(1,1,1)}`; on each sector they agree up to a sign, which conjugation removes (Lemma S1′(d)). Every swap gate commutes with the projections onto site types and sectors, so the support `Q` of the state is preserved at each step. Therefore `𝕍^*A_{2b}𝕍Q=A_{2b−2(1,1,1)}Q`, and the GNS vectors agree.

---

## 4. Required edits

Each edit marks its new text "(referee closure, GA1_5_REFEREE.md)" where it imports a closure from §3. Only R1, R2 and R8 change what a statement says; the rest add a missing step or fix wording.

- **R1 (GAP 2; lines 7, 9, 58, 139).** Replace GAP (2) by: "(2) Nearest-neighbour implementation is decided relative to the owner reading GA1-P-NN (referee closure, GA1_5_REFEREE.md §3). Under NN-a, every member of GA1-P-5 has a finite-depth implementation in even nearest-neighbour gates; for `W^{swap}`, `W^{swap,T}` and `W^{cube}` each nearest-neighbour layer is `2Z³`-periodic (Lemma U, Proposition C). `W^{swap}` is covariant under every lift, including rotations about the cell centre (Lemma S1′). Under NN-b, neither `W^{swap}` nor `W^{cube}` at generic angles can be built, and no NN-b layer has a propagating physical band in any empty-matter D1 state (Proposition N)." In line 58 replace "Nearest-neighbour compilation remains GAP 2." by "Nearest-neighbour compilation: see GAP (2)." In line 139 replace "or the nearest-neighbour admissibility required by GA1-P" by "; under NN-a the layer meets GA1-P, under NN-b it does not (GAP (2))". In line 9 add "the owner reading GA1-P-NN".
- **R2 (Theorem 5.2, line 111).** Add after "`s_a=±1`": "On `S_+`, `∏_aU^{aa}=−∏_j2T_{2j−1,2j}=−1`, so `∏_as_a=−1` and `det D=−1`; the family `DRᵀ` is the coset `O(10)∖SO(10)` (referee closure, GA1_5_REFEREE.md, Lemma D)."
- **R3 (GAP 4; line 7 item (4) and line 115, first three sentences).** Replace by Proposition O: "The site-staggered relabelling `𝐕′_ℓ=Φ_{head}ᵀ𝐕_ℓΦ_{tail}`, `Φ_z=D` on sites with odd coordinate sum and `1` otherwise, maps the family bijectively onto `SO(10)` link fields with the same plaquette symbols; lines 104–109 then apply to `𝐕′` (referee closure, GA1_5_REFEREE.md)." Keep its four-test line.
- **R4 (line 115, last sentence; row 36).** Replace by: "In both laws the exact symbols do not make the link matrix `𝐔` invertible and covariant (`GA2_Y2.md` Theorem 2.1, Corollary 2.2: `‖𝐔^†𝐔/c−1‖≥1`), nor its fluctuations small (`GA2_Y2.md` Theorem 3.2 for `L5-U`; Theorem 3.4: `κ≤1/2` on `L5-U`, `κ≤1/10` on `L5-O`). On `L5-O` each entry `U^{ab}` is itself a Hermitian involution."
- **R5 (GAP 5; line 7 item (5) and line 159, Attack 2).** Replace "The draft's claimed non-invariance of the kernel does not follow merely from the complex structure used to define it." by "The kernel is `K_ℓ=(|0_y⟩⊗F_x+F_y⊗|0_x⟩)∩S_+` and is not invariant under `Spin(10)_x` (referee closure, GA1_5_REFEREE.md, Lemma K); whether a covariant multiplicity swap preserves it is not established."
- **R6 (line 141; rows 43–44).** Write "decompose their link-end stars `⊗_{ℓ∋v}Λ^{p_{ℓ,v}}C⁵` (matter excluded) into `V_λ⊗M_λ`". Replace "Point reflection is carried to point reflection by the cell group, so the gate family is covariant." by a pointer to Lemma S1′: the lift acts on links as a colour-preserving rishon permutation (`LW1_5.md` B1-U), `g∘a_T=a_T∘g`, `gP_Cg^{-1}=P_{gC}`, and the gate does not depend on sector phases of the identification.
- **R7 (line 147; row 47).** Add: "Put `A_{2b}=τ_b(A_0)`; at odd antipodes transport by `ι_o`. Since `P_{C_e}P_{C_o}` is the translation by `−2(1,1,1)`, `ι_eι_o` agrees with the translation lift up to a sector sign, which conjugation removes (referee closure, GA1_5_REFEREE.md §3.9)."
- **R8 (Theorem 6.3 scope; lines 135, 149, 9).** Add after Theorem 6.3: "For every `1≤m≤9` the same holds with `W^{swap,T}` (translation identification) and the sector `σ^→` (`p_{tail}=⌈m/2⌉`); averaging over rotations gives a cell-invariant D1 state with the same band (referee closure, GA1_5_REFEREE.md, Proposition S-odd)." Remove "the odd-`m` extension of the swap construction" from line 9. In line 149 add: "A translation identification with an oriented sector does it (Proposition S-odd)."
- **R9 (GAP 6; line 90).** After A2 add: "On an induced box, `σ′−σ` is a sum of hop paths and plaquette boundaries (referee closure, GA1_5_REFEREE.md §3.9); the failing step is the one named." After A3 add: "Its two facts are standard (skew Howe duality; the exchange property of weight sets); they are not rebuilt and not used."
- **R10 (line 32; row 12).** For the class, write test 4 as "pass under NN-a: compilation holds for every member (Proposition C)". For test 2 add: "the class is a fixed list of conditions; as law data it is a family, and PS-6r's named free constant belongs to a chosen member".
- **R11 (lines 80, 84).** Rename the generated algebra `𝒢_R` (for example to `𝔅_R`); `𝒢` is the cell group.
- **R12 (line 163).** Add Orland–Rohrlich to the quantum-link credits, as the draft lists them (`GA1_5_DRAFT.md` line 33).
- **R13 (line 5).** Add to "Proved below": the referee closures Lemma U, Proposition C, Lemma S1′, Proposition N, Proposition S-odd, Lemma D, Proposition O and Lemma K, each marked as a referee closure.

---

## 5. Open statements to carry by name

- **GA1-P-NN (owner reading).** For laws with link registers, does PS-1's "nearest-neighbour gate" require gauge invariance gate by gate? NN-a (no) passes the four tests; NN-b (yes) fails tests 3 and 4 (§3.1). Under NN-a, Proposition C and Lemma S1′ apply; under NN-b, Proposition N applies.
- **GA1-P-5 (owner's choice).** Which class or member the law adopts. Under NN-a every member of the proposed class meets GA1-P's three conditions (Theorem 3.1 and Proposition C), so the choice rests on physics, not admissibility.
- **CONN, with CONN_R.** Open after A1 (site saturation; fails because four corners move at once), A2 (homology; the box decomposition holds, but intermediate sectors need not keep every type) and A3 (exchange; detours are not synchronized).
- **GA1-5-Φ.** Open after attacks 1 (tiling-cube gates; Theorem 6.2), 2 (disjoint covariant supports; Theorem 2.2) and 3 (one-qubit Clifford flux automaton; Theorem 6.4). Under NN-b, Proposition N(4) answers it negatively for every empty-matter D1 state; other states stay open.
- **GA1-5-O.** Open after attacks 1 (empty matter is not fixed), 2 (hop kernels; now with Lemma K) and 3 (tracial state).
- **The `L5-O` corner lemma** (the analogue of Theorem 4.2). Carried from `GA1_5.md`; not attacked here.
- **Generation of the neutral algebra by plaquettes, hops and numbers on larger regions.** Carried; not attacked here.
- **The electric half of GA1(a)(4).** Carried to GA2's Y2-W (G3).

Closed here and to be removed from `GA1_5.md`'s open list: GAP (4); the first sentence of GAP (5); the odd-`m` extension of the swap construction.

## 6. Freeze recommendation

**Freeze `GA1_5.md` after R1–R13.** No ERROR changes a theorem's content. R2 adds a determinant that was already forced. R8 extends Theorem 6.3 from even `m` to every `m`. R1 records GAP (2) as decided relative to GA1-P-NN; the theorems themselves do not change. The referee closures enter marked as such and stay unrefereed. GA1-P-NN goes to the owner. `TOE_ASSEMBLY.md` line 229 records the owner's request "that every owner question be checked by Codex `gpt-6-astra` at max effort before it is put to them", so the lead routes it through that check first.

---

## FINISH

**Proved here (referee closures; unrefereed).**
- Lemma U: under NN-a, every unitary on a connected finite set of link registers is an exact finite product of even gates, each on one site and one incident link.
- Proposition C: `W^{swap}`, `W^{swap,T}` and `W^{cube}` have finite depth in even nearest-neighbour gates with `2Z³`-periodic layers; every member of GA1-P-5 has finite depth with `2kZ³`-periodic layers.
- Lemma S1′: `W^{swap}` and `W^{swap,T}` are covariant under the lift of every element of `𝒢`, including the rotations about each cell centre.
- Proposition N: on `L5-U`, products of gauge-invariant edge-triple gates act on empty matter as functions of the end numbers. So `W^{swap}` (even `m`), `W^{swap,T}` (every `m`) and `W^{cube}` (outside a closed discrete set of angles) are not such products, and no layer of such gates has a propagating physical band in any empty-matter D1 state. The same holds on `L_cube` with `E_ℓ`.
- Proposition S-odd: for every `1≤m≤9`, a member of GA1-P-5 and a D1 state (also a cell-invariant one) carry a band in `H_phys∩H_even` with fibre `e^{−iK·(1,1,1)}`.
- Lemma D: on `L5-O[S_+]`, `det D=−1`; the coherent link symbols fill the coset `O(10)∖SO(10)`.
- Proposition O: a site-staggered relabelling maps that family onto `SO(10)` link fields with the same plaquette symbols, so the Wilson small-field expansion applies.
- Lemma K: the hop kernel `K_ℓ` has dimension 31 on `S_+` and is not `Spin(10)_x`-invariant.
- On an induced box, two sectors with equal site types differ by hop paths and plaquette boundaries.
- Re-derived and found correct: Theorems 2.1, 2.2, 3.1, 4.1–4.3, 5.1, 6.1, 6.2, 6.4; Theorem 5.2 with Lemma D; Theorem 6.3 with the closures of rows 43, 44 and 47.

**Counterexamples.**
- Under NN-a, for every `m`, a layer that meets all three conditions of `LW1.md` GA1-P (gauge invariant, cell covariant, finitely many nearest-neighbour layers) has a propagating band in the physical sector of a D1 state of `L5-U[m]`. This refutes "no admissible finite-register plaquette layer gives a propagating physical band". The band is neutral: it carries colour multiplicity, not electric flux.
- Under NN-b, `W^{swap}` and `W^{cube}` refute "every member of GA1-P-5 is a finite circuit of gauge-invariant nearest-neighbour gates".
- `GA1_5.md`'s star-region counterexample to region-wise completeness stands.

**Open by name.** GA1-P-NN (owner reading); GA1-P-5 (owner's choice); CONN with CONN_R (A1–A3); GA1-5-Φ (attacks 1–3; negative in empty-matter D1 states under NN-b); GA1-5-O (attacks 1–3); the `L5-O` corner lemma; neutral generation on larger regions; the electric half of GA1(a)(4) (GA2/Y2-W).

**What changes downstream.**
- `LW1.md` GA1-P: under NN-a its implementability clause holds for every finite-support member of the class; under NN-b it excludes every plaquette layer that moves empty-matter links beyond number phases, on `L5-U` and on `L_cube`. GA1-P's open content is the owner reading plus the class choice.
- LZ1 under LZ1-SC: the swap band's image lies in `ker(Ũ−1)^⊥`, because `V(K)=1` only on the null set `K·(1,1,1)∈2πZ`. So the static class does not absorb it. It bears on LZ1(a) only if VC1's vacuum carries such a band; R-loc reads species in the vacuum.
- `EW1.md` Lemma 6.4(2): under NN-b its stationarity statement carries over to every plaquette layer (Proposition N(2)). Under NN-a the analogue fails for `W^{cube}` and `W^{swap}`.
- GA2's Y2-W: on `L5-O[S_+]` the coherent start is the `SO(10)` Wilson form after Proposition O. The `L5-U` start is unchanged.
- No law is eliminated. Both five-mode laws remain live. No axiom, working-set entry, reading or class is adopted.
