lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1Z2L5 referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). The lane brief calls it a pass-1 lane; its job here is pass 3, the referee, of the part GB1Z2L5 under PR #10138's method. Claude drafted the part (`GB1Z2L5_DRAFT.md`). Codex gpt-6.1-terra distilled it (`GB1Z2L5.md`). This session wrote neither. This is one check: one whole-part, line-by-line read of `GB1Z2L5.md`. No review of this review was commissioned.

**Text read.** `GB1Z2L5.md` at commit `a986b585a` (the last commit that touches it; it is also the branch head when read). SHA-256 of the file read: `0ce94a3e6d4e44670acc72ad7ca127c6c2999da0026e3c9416c14c28950a5eb5`. It has 113 lines. Line numbers below refer to that file. Pass 1, `GB1Z2L5_DRAFT.md`, at the same commit has SHA-256 `1406ac26626239adcdc70c13df879d4e75125fa04951570f9048e01442474a3b`; this equals the hash that `GB1Z2L5.md` line 13 records.

**Method.** Every proof in `GB1Z2L5.md` was re-derived by hand, then checked against the pass-1 text it distils and against the sources it cites, quoted by line. A `[check]` is a small scratch computation in `/tmp/toe-GB1Z2L5ref/` (under a minute, a few MB, started only with at least 50 percent free memory). It guides only and proves nothing. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. The lane brief names the results by their pass-1 labels; the distillation renumbers them. The map is: pass-1 Lemma 1 = Theorem 1; Lemma 2 = Theorem 2; Lemma 3 = Theorem 3; Theorem A = Theorem 4; Corollary B = Theorem 5; Proposition C = Theorem 6; Proposition D(i) = Theorem 7; Proposition D(ii), D(iii) = Theorem 8(a), 8(b); the R-SEC section 2.8 = §7 with Theorem 9.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The two named laws, NN-a and ZM1-INV are read plainly. No hostile meaning is read into them. Where a word admits two plain readings, both are stated and the verdict says which one the theorem covers.

**Working set used, by name.** PS-5 (five modes per site) and PS-6r (finite link registers), through the two named laws `L5-U[m]` and `L5-O[S_+]` of `LW1_5.md` section 2. The owner decisions NN-a (`TOE_ASSEMBLY.md` 3.7) and ZM1-INV (3.9), only as GB1Z2L5 quotes them. Nothing else. `docs/MINIMAL_AXIOMS_2026-06-29.md` was not needed and was not read.

**Inputs from outside the working set.** Standard mathematics, rebuilt in this report where a verdict rests on it: characters of C*-algebras; averaging over a compact group; joint eigenspaces of commuting Hermitian matrices; the centre of a full matrix algebra; the relations of the symmetric group `S_3`; the Gram matrix of a positive functional. No literature is used.

**Sources read, by line.** All at commit `a986b585a` of this checkout unless a branch is named.

- `GB1Z2L5.md` lines 1-113 (all), line by line.
- `GB1Z2L5_DRAFT.md` lines 1-273 (all).
- `prior/GB1Z2L5.md` (all).
- `LW1_REFEREE.md` lines 1-80 and `Y2W_DRAFT.md` lines 1-25 (format only).
- `LW1_5.md` lines 24, 36-44, 89-100, 132-145, 155-160, 171, 228-244 (premises, site algebra, both laws, Q and G, R, U, the centre elements, `Q_x`, Z-U).
  Quotes used: line 37, `c_j=(\gamma_{2j-1}+i\gamma_{2j})/2`; line 39, "\(n_j-1/2=M^{2j-1,2j}\)"; line 42, "Links commute with matter and are ordinary tensor factors"; line 44, "Gauge invariance means invariance under conjugation, not necessarily a zero Gauss-charge sector"; line 89, `T_{ij}=i\eta_i\eta_j/2` and "The proposed register is its 512-dimensional half-spin representation \(S_+\)"; line 96, the `L5-U` Gauss generator `\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}`; line 171, "The site factors are respectively \(-1\) and \(-iP_x\)"; line 228, "Let \(Q_x=N_x+\sum_{\ell\ni x}p_{\ell,x}\)".
  Line 151: "Let \(S_+(g)\) be the half-spin representation on \(H_+\)"; line 157: "On \(H_+\), where \(P=1\)". Line 208: "\(R=S_+\oplus S_-\), the full Fock space of \(\mathrm{Cl}(20)\)".
  Line 143, proof of R: "On \(S_+\), the product of the ten commuting \(2T_{2j-1,2j}\) is chirality \(+1\)". With `T_{ij}=i\eta_i\eta_j/2` and `f_j=(\eta_{2j-1}+i\eta_{2j})/2`, `2T_{2j-1,2j}=2f_j^\dagger f_j-1`, so the chirality is `(-1)^{10-N}=(-1)^N` and `S_+` is the even-number subspace. The empty link vector lies in it.
- `ZM1INV.md` lines 1-8 (status), 40-66 (Theorem 2.1, Theorem 2.2, R1), 88-100 (Theorem 3.2 to R5). Quotes used: line 5, "R1–R6 are referee closures, unrefereed"; line 42, "Each locked U witness for even `m` and each locked O witness is a character on `𝔄^G`"; line 46, "The all-empty vector uniquely minimizes every charge ... both link vectors lie in `S_+`"; line 56, R1: "(a) `ω` restricts to a character on `𝔄^G`; (b) `ω` is invariant under the base tick for every allowed constant; (c) `ω` is invariant under cell translations", with `ω=ψ∘E`.
  Line 96, R5: "Let `𝔅` be a unital C*-algebra with no character ... On `L5-U[m]` with even `m`, and on `L5-O`, there is no unital `*`-homomorphism `𝔅→𝔄^G`. *Proof.* Compose with the character of Theorem 2.1." Line 98: "Such characters exist for every `m₁` (Theorem 2.1, R1)". So R5's one-line proof, with R1's character, covers odd `m`; GB1Z2L5 credits this correctly.
- `GB1.md` lines 5-13 (status, open list), 20-35 (Definitions 1-7), 160-195 (R-GB1Φ, 5M, 5U, attacks, summary). Quotes used: line 23, Definition 1, "A **readout** is a unital injective *-homomorphism from the named source invariant quasi-local algebra into the named law's invariant algebra, covariant under the named cell lifts. Exponential locality means that for each input support radius \(R_0\) there are common \(C_{R_0},\xi_{R_0}\), independent of the input, such that its image is within \(C_{R_0}e^{-R/\xi_{R_0}}\|A\|\) of the finite algebra in the \(R\)-neighbourhood of its block"; line 24, Definition 2, "**Sector-level equality** means equality of all integer-time expectations \(\omega(\alpha^t\Phi(A))=\omega(\Phi\alpha_1^t(A))\) for every input and every state in a specified class ... The class is fixed before the comparison"; line 9, "Theorem 5U gives the \(U(1)\) rung at \(S=1/2\) inside \(L5\)-U\([m]\) for odd \(m\), at sector level"; line 13, the open list.
  Line 165, Theorem 5M: "The Gauss operators are \(G_x=P_x\prod_{\ell\ni x}X_\ell\), resp. \(\mathcal G_x=N_x+\sum_{\rm out}E_\ell-\sum_{\rm in}E_\ell\)". Line 176, Theorem 5U: "Let \(\mathfrak B_5\) be the unital C*-algebra generated by the \(U^{55}_\ell\) and \(n^{(5)}_{\ell,v}\) ... Then for every \(\omega\) in the class, every \(B\in\mathfrak B_5\) and every \(t\ge0\), \(\omega(\alpha^t(B))=\omega(\alpha_5^t(B))\)". Line 185, (Z-c): "Tests: 1 F (it fixes the target by naming); 4 F (\(\dim\Lambda^m\mathbb C^{10}\ge10\ne2\))". Line 187: "These are failures of routes. None proves that no ZM1-INV readout realizes the \(\mathbb Z_2\) rung inside \(L5\)-U or `L5-O`". Line 191, the rung table: \(U(1)\) on \(L5\)-U, "sector level at \(S=1/2\), \(m\) odd (Theorem 5U)".
- `GB1_REFEREE.md` line 233: "**GB1-Z2[L5].** Some ZM1-INV readout realizes a named \(\mathbb Z_2\) lattice gauge theory inside \(L5\)-U or `L5-O`, at algebra or sector level."
- `TOE_ASSEMBLY.md` line 235 (NN-a, ends "Gauge invariance and cell covariance are required of the complete update only") and line 252 (ZM1-INV: "Replace the full-algebra map by a unital injective *-homomorphism \(\Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G\). Retain cell covariance. Require exponential locality for every local invariant input, with support-radius-dependent constants ... Impose no map on charged fields or Gauss generators").
- `TOE_ASSEMBLY.md` line 445, GB1(a): "Fix a gauge group `G` and a framework law `L` with an exact local `G` frame group (PS-6, PS-6r; GA1). There are a zoom rung `n` and a readout `Φ` of the owner's ZM1-INV form (a unital injective cell-covariant exponentially local *-homomorphism on gauge-invariant observables) such that the framework's link sector, restricted to the gauge-invariant algebra, equals a named lattice gauge theory `LGT_G` on `Z^3` with its time step". (The draft cites this as line 435 at its checkout `4a0c580d67`; at `a986b585a` it is line 445. The distillation cites no line for it.) Lines 236, 244, 254: the four-test grades in use are P, C and F; the owner's ZM1-INV text itself carries "P P C P".
- `GA15PHI.md` line 40, Theorem 2: "For `1≤p≤4`, the multiplicity of some type `μ₀` in `(Λ^p C⁵)^{⊗3}` contains a standard two-dimensional `S₃` module `q`". `GA2_Y2.md` line 49: "**Theorem 2.3 (N4).** If \(K=\rho(G)\) is finite, \(L^2(K)\) carries an entrywise-commuting unitary link with covariance at both ends."
- `GA15PHI.md` line 129, Theorem 8: "(oriented sector frozen at `m=1,9`) ... If a finite link region `R` contains the support of a link-only gauge-invariant operator `A`, and `P_R` projects onto `σ→` on all links of `R`, then `AP_R=P_RAP_R`".
- `origin/docs/consolidate-gauge-matter-registers` at `7086189d1` (fetched, read with `git show` only), `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 262-266: "U is nilpotent (U^2 = 0), not unitary: this is a quantum link, not a group-valued clock."
- `docs/ai_methodology/SCIENCE_WORKFLOW.md` line 202: "Use the existing N1-N8 negative-claim packet contract honestly where required." `docs/ai_methodology/skills/no-go-discipline/SKILL.md` lines 49-75 (the N1-N8 checklist), read to check `GB1Z2L5.md` §8.
- `LW1_5.md` line 242, Z-U: "A local operator with definite \(Q_x\) charges has total charge equal to its matter-number change, and its matter parity is \((-1)^{\sum q_x}\). Thus no fermion-odd local operator is invariant under all \(U(5)_x\)." `TOE_ASSEMBLY.md` line 225: "on both five-mode laws fermion parity is a product of local centre elements ... (`LZ1.md` Theorems 2.1-2.2), and no gauge-invariant odd composite exists (`RCS1.md` Theorem 4)".
- `RCS1.md` line 5 (status: "FROZEN 2026-11-06 after pass 3") and line 68, Theorem 4: "Every `A∈𝔄^G` is matter-even." Line 8 credits "Theorem 4's evenness is `MT1.md`'s local evenness, extended here to the whole fixed algebra".
- `ZM1INV.md` line 124: "Extending this local good-sector action by zero is not unital". `TOE_ASSEMBLY.md` line 610: "both live laws".

## Prior work used

| Prior result | Path | Use here |
|---|---|---|
| Theorem 2.1 (C1, C1-O), R1(a)-(b), Theorem 3.2 (N), R5 | `ZM1INV.md` lines 42-66, 92-98 (frozen; R1 and R5 are referee closures, unrefereed) | Checked against Theorems 2 and 4 and against their credit lines |
| Definitions 1-2; Theorems 5M and 5U; attacks (Z-a)-(Z-c); line 187 | `GB1.md` lines 23-24, 165-191 (frozen) | Fix the target, the sources and the scope of "sector level" |
| The two laws; `n_j-1/2=M^{2j-1,2j}`; proof of R (chirality); centre factors; `Q_x`; Z-U | `LW1_5.md` lines 37-44, 89-96, 143, 151-157, 171, 228, 242 | Conventions under Theorems 2 and 6 |
| Theorem 4, "Every `A∈𝔄^G` is matter-even" | `RCS1.md` line 68 (frozen) | **Missed by the digest and by both passes.** It proves the first clause of `GB1Z2L5.md` Theorem 6 on both laws; `LW1_5.md` Z-U (line 242) proves the `L5-U` case |
| Theorems 2 and 8; Theorem 2.3 (N4); consolidated note lines 262-266 | `GA15PHI.md` lines 40, 129; `GA2_Y2.md` line 49; PR #10126 branch at `7086189d1` | Citation checks only |

## Referee `[check]`

`/tmp/toe-GB1Z2L5ref/check_ref.py` (numpy, floating point; 4.4 s, 53 MB peak; started at 57 percent free memory; largest matrix 125 x 125). It guides only and proves nothing.

- **Theorem 8(a).** Three link ends at one vertex, each restricted to end number `q`, with `E^e_{ab}=r^\dagger_{e,a}r_{e,b}` built by Jordan-Wigner on five modes. For `q=1` and `q=4`: `T_12-c_q` and `T_23-c_q` equal the factor swaps exactly (`c_1=0`, `c_4=3`); `T_12` commutes with every `\sum_eE^e_{ab}`; `P_std` has rank 80 of 125; `X^2=Z^2=P_std` and `XZ+ZX=0` to `2e-16`; `X`, `Z` are Hermitian.
- **Theorem 2, `L5-U`.** One plaquette, matter at all four sites, links oriented lower to upper. The number of occupation basis vectors with the witness's torus weights is 1 for every `m=1,…,9`. This repeats pass 1's plaquette count by a different method (meet in the middle over link pairs).

---

## 1. Verdict table

**Counts.** 48 items: 44 CORRECT, 1 ERROR, 3 INCOMPLETE. The seven distiller definitions count as seven items. No ERROR or INCOMPLETE item changes the content of a theorem.

| # | Item (`GB1Z2L5.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status sentence (5) | CORRECT | |
| 2 | §0 "Proved" (7) | CORRECT | Each listed result is proved below. Credit for Theorem 6's first clause is missing; see item 31. |
| 3 | §0 GAP — R-SEC covariance (9) | CORRECT | The GAP is real and the repair is right. §3.1 gives the repaired reading. |
| 4 | §0 "Open by name" (11) | INCOMPLETE | It names no frozen-class reading. GB1 records its named-law U(1) rung in that sense (Theorem 5U), and (Z-a) attacked Z₂ in that sense. "other readings remain open" names nothing. Edit E1. |
| 5 | §0 Provenance (13) | CORRECT | Both SHA-256 values match the files at `a986b585a`. |
| 6 | Definition 1 (17) | CORRECT | |
| 7 | Definition 2 (18) | CORRECT | Matches `LW1_5.md` lines 44, 89, 96, 132-135. |
| 8 | Definition 3 (19) | CORRECT | |
| 9 | Definition 4 (20) | CORRECT | Matches `GB1.md` Definition 6 and Theorem 5M. |
| 10 | Definition 5 (21) | CORRECT | `GB1.md` Definition 2 uses the readout Φ of Definition 1; "It still requires this readout" is exact. |
| 11 | Definition 6 (22) | CORRECT | Read "disjoint" as "with no common factor"; optional edit E6. |
| 12 | Definition 7 (23) | CORRECT | |
| 13 | Scope paragraph (25) | CORRECT | "both live laws": `TOE_ASSEMBLY.md` line 610. |
| 14 | Theorem 1, statement (29) | CORRECT | |
| 15 | Theorem 1, proof (31) | CORRECT | The average acts on all of 𝔄 and fixes invariant A, so ‖A−E(B)‖=‖E(A−B)‖≤‖A−B‖. |
| 16 | Theorem 2, statement and witnesses (33-37) | CORRECT | Ranges: m=2k with 1≤k≤4; m=2k+1 with 0≤k≤4. |
| 17 | Theorem 2, proof: O vector in S₊; weight spaces preserved (39) | CORRECT | `LW1_5.md` line 143 makes S₊ the even-number subspace. |
| 18 | Theorem 2, proof: even m (41) | CORRECT | |
| 19 | Theorem 2, proof: odd m (43) | CORRECT | Same argument as `ZM1INV.md` R1(a). `[check]` agrees on a plaquette. |
| 20 | Theorem 2, proof: O; extension to a character (45) | CORRECT | |
| 21 | Remark after Theorem 2 (47) | ERROR | "not a selected vacuum, a singlet or a stationary state" denies stationarity. The next sentence cites R1(b), which proves base-tick invariance. Edit E2. |
| 22 | Theorem 3, statement (51) | CORRECT | |
| 23 | Theorem 3, proof (53) | CORRECT | |
| 24 | Theorem 4, statement (55) | CORRECT | |
| 25 | Theorem 4, proof (57) | CORRECT | |
| 26 | Paragraph after Theorem 4 (59) | CORRECT | Theorem 5U compares the algebra 𝔅₅, which is not inside 𝔄^G (`GB1.md` line 176), as stated. |
| 27 | Theorem 5, statement (61) | CORRECT | |
| 28 | Theorem 5, proof (63) | CORRECT | The Gauss operator puts X on outgoing and X⁻¹ on incoming links (pass 1 line 178). |
| 29 | Routes paragraph (65) | CORRECT | `GB1.md` line 185 lists only tests 1 and 4 for (Z-c), both F. |
| 30 | Theorem 6, statement (69) | CORRECT | |
| 31 | Theorem 6, proof: evenness (71) | INCOMPLETE | The mathematics is complete. The clause is `RCS1.md` Theorem 4 (frozen), and on `L5-U` also `LW1_5.md` Z-U; neither is credited. Edit E3. |
| 32 | Theorem 6, proof: the unit (73) | CORRECT | |
| 33 | Remark (75) | CORRECT | |
| 34 | Theorem 7, statement (79) | CORRECT | |
| 35 | Theorem 7, proof (81) | CORRECT | Gauss sign as in `GB1.md` line 165. |
| 36 | Theorem 8, statement (83) | CORRECT | |
| 37 | Theorem 8(a), proof (85) | CORRECT | `[check]` agrees for q=1 and q=4. "central projection" means central in the image of the group algebra of S₃; optional edit E7. |
| 38 | Theorem 8(b), proof (87) | CORRECT | |
| 39 | Remark after Theorem 8 (89) | CORRECT | Quote verified at the consolidated note, line 262. |
| 40 | §6 prior work (93) | CORRECT | R5, R1 and `ZM1INV.md` line 124 verified. |
| 41 | §6 literature and pass-1 checks (95) | CORRECT | Matches pass 1 lines 67 and 244. |
| 42 | R-SEC text (99) | INCOMPLETE | The operation-stability clause omits "B∈𝔄^G" (pass 1 line 228 has it). Edit E4. |
| 43 | Four-test paragraph (101) | CORRECT | C C P P is right for the original and the repaired reading. The reason given for test 4 is incomplete; §3.2. |
| 44 | Theorem 9, statement (103) | CORRECT | |
| 45 | Theorem 9, proof (105) | CORRECT | |
| 46 | Paragraph after Theorem 9 (107) | CORRECT | |
| 47 | §8 routes and N1 (111) | CORRECT | N1 asks for "at least **5 distinct attack routes**"; the text claims no PASS. |
| 48 | §8 N2-N8 (113) | CORRECT | |

## 2. Decisions on the results the lane brief names

**Theorem A (distilled Theorem 4): CORRECT.** The proof is one composition. If `Φ:𝔅→𝔄^G` is a unital *-homomorphism and `χ` is a character of `𝔄^G`, then `χ∘Φ` is a *-homomorphism with `χ∘Φ(1)=1`, so it is a character of `𝔅`. Both inputs hold (Theorems 2 and 3). The theorem uses no update, zoom, block map, state or constant. `GB1.md` Definition 2 compares `ω(α^tΦ(A))` with `ω(Φα_1^t(A))`, so sector-level equality in that definition needs the same `Φ`. Hence GB1-Z2[L5], as stated at `GB1_REFEREE.md` line 233 ("Some ZM1-INV readout realizes ..."), fails at algebra level and at sector level, at the clause "unital". The theorem says nothing about maps that do not land unitally in `𝔄^G`. GB1 itself uses such maps for its named-law rungs: Theorem 5U compares the algebra `𝔅₅`, generated by the non-invariant `U^{55}_ℓ` (`GB1.md` line 176). Item 4 and edit E1 carry that reading by name.

**Lemma 2 (distilled Theorem 2): CORRECT.** I re-derived the three weight counts. Even `m` and O rebuild `ZM1INV.md` Theorem 2.1 (frozen). Odd `m` rebuilds R1(a), a referee closure that is still unrefereed. The rebuild is complete, so Theorem 4 does not rest on R1's status. The orientation step is sound: the two orientations have equal in-degrees, so the links where they differ form a balanced digraph; a nonempty one has a directed cycle; every positive lattice link raises the coordinate sum, so there is none. For O, `LW1_5.md` line 143 fixes `S₊` as chirality `+1`, and `2T_{2j-1,2j}=2f_j^†f_j-1` makes that the even-number subspace. The empty link vector lies in it.

**Lemma 3 (distilled Theorem 3): CORRECT.** `X_ℓ` and `Z_p` are invariant: at a corner of `p`, `G_x` meets two links of `∂p`, and the two signs cancel. They anticommute because `Z_ℓ` occurs once in `Z_p`. A character sends both to `±1`, which contradicts `χ(X)χ(Z)=-χ(Z)χ(X)`. Nonzero unital images and nonzero quotients keep the relation.

**Corollary B (distilled Theorem 5): CORRECT, with its reach.** A character sends invertible elements to nonzero numbers, so `ab=λba` forces `λ=1`. For `Z_N`, with `G_x=∏_{out}X_ℓ∏_{in}X_ℓ^{-1}`, the oriented clock plaquette is invariant: at each corner the path enters on one link and leaves on another, and the two phases are `ω` and `ω^{-1}`. Then `X_ℓZ_p=ω^{±1}Z_pX_ℓ` with both unitary, so the source has no character. **Referee closure (finite abelian `G≠1`).** On `L^2(G)` let `X_ℓ` be translation by `h` and `Z_ℓ` multiplication by a character `ψ` of `G` with `ψ(h)≠1`; such a pair exists for `G≠1`. Translations commute, so `X_ℓ` is invariant. The oriented product of `Z^{±1}` around `p` is invariant because gauge translations at a corner multiply it by `ψ(g)ψ(g)^{-1}`. Then `X_ℓZ_p=ψ(h)^{∓1}Z_pX_ℓ` for `ℓ∈∂p`. This is the distilled proof's "choose a nontrivial factor", written out.

**Proposition C (distilled Theorem 6): CORRECT mathematics; one credit missing (item 31).** The unit argument holds as written: `P=Φ(1)` is a nonzero projection; uniform constants for the unit give approximants `A`, `A'` in algebras with no common factor; the parity average makes `A'` even, so it commutes with `𝔄(B)`; the unitary average sends `A` to `tr(A)1` and fixes `A'`; so `‖P-tr(A)1‖≤3δ<1/2`, and a projection that close to a scalar is `0` or `1`. If one reads the unit as having empty support, its image is within `δ` of `𝔄(∅)=ℂ1` directly, and the conclusion is the same.

**Proposition D (distilled Theorems 7 and 8): CORRECT.** (i) The U(1) witness `E_ℓ=S` works because `N'_x=∑_{out}δ-∑_{in}δ` sums to zero over `S(R)`, nonnegative matter then vanishes, and a nonzero balanced nonnegative flow on positive links would contain a directed cycle. So the character obstruction says nothing about the U(1) rung. (ii) The corner computation is right, and `[check]` agrees for `q=1` and `q=4`. `X`, `Z` are unitaries of the corner `P_std𝔄^GP_std`, not of `𝔄^G`; this matches Theorem 5. (iii) Theorem 2 uses only the torus, so any closed `H` containing it keeps the character.

**R-SEC and its four tests.** The distiller's GAP is real (§3.1). Pass 1's grades C C P P are right, for the original text and for the repaired one (§3.2).

## 3. Notes and referee closures

### 3.1 GAP — R-SEC covariance: real; repaired reading

Pass 1 (line 228) asks for a "cell covariant" map into `𝔄^G/𝔍_S`. A cell lift `β` acts on that quotient only if `β(𝔍_S)=𝔍_S`. Pass 1 assumes nothing that gives this. Pass 1 line 230 also says "Tick invariance of \(\mathcal S\) gives \(\alpha(\mathfrak J_{\mathcal S})=\mathfrak J_{\mathcal S}\)". That holds when `S∘α=S` as sets. If only `S∘α⊆S`, it gives `α(𝔍_S)⊆𝔍_S`, since `ω(α(A)^*α(A))=(ω∘α)(A^*A)`. The distiller's GAP and its two repairs are right.

**Repaired reading (referee closure; proposed, not adopted).** "Fix in advance a nonempty class `S` of states of `𝔄^G`, with `S∘β=S` for every cell lift `β` and `S∘α=S` for the tick `α`. Let `π_S=⊕_{ω∈S}π_ω`, the direct sum of the GNS representations of `𝔄^G`, and `𝔍_S=ker π_S`. The readout is a unital injective *-homomorphism `Φ:𝔄_1^G→𝔄^G/𝔍_S`, covariant under the induced cell action and exponentially local in the quotient norm with the images of the local algebras. Sector-level equality is `GB1.md` Definition 2 with `α` acting on the quotient."

**Lemma R (well defined).** (a) `𝔍_S` is a closed two-sided ideal and `1∉𝔍_S`. (b) If `S` is closed under `ω↦ω(B^*·B)/ω(B^*B)` for `B∈𝔄^G` with `ω(B^*B)>0`, then `𝔍_S={A:ω(A^*A)=0 for all ω∈S}`, the ideal of `GB1Z2L5.md` line 99. (c) If `β` is an automorphism of `𝔄^G` with `S∘β=S`, then `β(𝔍_S)=𝔍_S`. (d) `𝔄^G/𝔍_S≅π_S(𝔄^G)`.

*Proof.* (a) A kernel of a representation is a closed two-sided ideal; `π_S(1)=1≠0` since `S` is nonempty. (b) If `π_ω(A)=0`, then `ω(A^*A)=‖π_ω(A)Ω_ω‖²=0`. Conversely, let `ω(A^*A)=0` for all `ω∈S`. Fix `ω∈S` and `B∈𝔄^G`. If `ω(B^*B)>0`, the normalized state `ω(B^*·B)/ω(B^*B)` lies in `S`, so `‖π_ω(A)π_ω(B)Ω_ω‖²=ω(B^*A^*AB)=0`. If `ω(B^*B)=0`, then `π_ω(B)Ω_ω=0`. So `π_ω(A)` vanishes on the dense subspace `π_ω(𝔄^G)Ω_ω`, and `π_ω(A)=0`. (c) `β` maps `𝔄^G` onto itself, so `(π_ω∘β,H_ω,Ω_ω)` is a GNS triple of `ω∘β`. Hence `ker π_{ω∘β}=β^{-1}(ker π_ω)`. Intersect over `ω∈S` and use `S∘β=S`: `𝔍_S=β^{-1}(𝔍_S)`. (d) The image of a *-homomorphism of C*-algebras is closed, and the first isomorphism theorem applies. □

**Theorem 9 in this form.** If `ω∈S` and `ω≥λχ̃` on `𝔄^G`, with `λ>0` and `χ̃` a character there, then each `A∈𝔍_S` has `ω(A^*A)=0`, so `λ|χ̃(A)|²=λχ̃(A^*A)=0`. Thus `χ̃` induces a character of the quotient, and the proof of Theorem 4 applies. The distilled proof (line 105) is this argument with the ideal of (b).

The GNS-kernel form needs no stability clause. By (b) it agrees with the distilled ideal whenever that clause holds. By (d), R-SEC asks for a readout into the representation that `S` generates.

### 3.2 Four tests of R-SEC, fresh, on the repaired text

- **Test 1: C.** It does not state that a Z₂ rung exists; GB1-Z2[L5,SEC] stays open. It does replace the codomain `𝔄^G` in the owner's ZM1-INV text (`TOE_ASSEMBLY.md` line 252), the clause at which Theorem 4 fails. So it proposes a change to an owner text, made for this part's target. GB1 graded R-GB1Φ the same way: "1 C (it reads GB1's own target text, as R-EQ does)" (`GB1.md` line 163).
- **Test 2: C.** By Lemma R(d), choosing `S` chooses the representation in which the readout lands. A lane can tailor that choice; Theorem 9 shows some choices that fail. The test would pass if `S` were fixed outside the part, for example as the class of VC1's state.
- **Test 3: P.** It decides neither VC1 membership (GB1-SC) nor a Euclidean or continuum question. The invariance clauses restrict `S`; they say nothing about the VC1 state.
- **Test 4: P.** Each clause serves the construction. `S∘β=S` makes covariance defined. `S∘α=S` makes the tick an automorphism of the quotient. The distilled stability clause makes its ideal two-sided. No constant enters. Pass 1's stated reason ("It removes a requirement and uses the class that GB1 Definition 2 already has") does not mention these clauses; the grade stands on the reason given here.

Result: C C P P, as in pass 1. This answers line 101's "it has not received a fresh four-test review".

### 3.3 Line 47 (item 21)

Quote: "The witness is a state, not a selected vacuum, a singlet or a stationary state." `ZM1INV.md` R1(b) states that the oriented state "is invariant under the base tick for every allowed constant", and `ZM1INV.md` line 7 calls it "also a stationary character". So the sentence is false for odd `m` under the base tick. Its intent is that Theorem 2 does not use these properties. Replacement: "Theorem 2 uses the witness only as a state. It does not use, and this file does not claim, that the witness is a selected vacuum, a singlet or a stationary state."

### 3.4 Credit for evenness (item 31)

`RCS1.md` Theorem 4 (frozen): "Every `A∈𝔄^G` is matter-even." It credits `MT1.md`'s local evenness. `LW1_5.md` Z-U proves the `L5-U` case. The distilled proof rebuilds the result in full, so only a credit line is missing.

### 3.5 The frozen-class reading (item 4)

GB1 records its named-law U(1) rung "at sector level" through Theorem 5U. That theorem compares `ω(α^t(B))` with `ω(α_5^t(B))` for `B` in `𝔅₅`, an algebra generated by non-invariant link operators. GB1's Z₂ attack (Z-a) used the same kind of comparison. Theorem 4 does not reach it: these maps land in `𝔄`, not unitally in `𝔄^G`, and `𝔄` has no character. The distilled text says so in substance ("neither is a readout into full A^G", line 59; "other readings remain open", line 11) but gives the reading no name. A name is proposed in §5. It names GB1's own usage; it adds no reading.

### 3.6 Definition 6 (item 11)

The proof of Theorem 6 needs `𝔄(B)` and `𝔄(B')` to share no factor. If a neighbourhood holds every link with one end in it, two disjoint site sets at distance one share a link. Reading "disjoint" as "sharing no matter or link factor" removes the doubt. Every cube zoom meets that reading, since the two source sites can be taken far apart.

## 4. Required edits

Required before freeze (E1-E4). None changes a theorem.

- **E1 (item 4, line 11).** Add to "Open by name" the statement GB1-Z2[L5,5U] of §5. At line 59, after "neither is overturned", add: "The Z₂ analogue of Theorem 5U is GB1-Z2[L5,5U], open; (Z-a) and (Z-b) are failed instances."
- **E2 (item 21, line 47).** Replace the first sentence by the text of §3.3.
- **E3 (item 31, line 71; also §6, line 93).** Add: "The evenness clause is `RCS1.md` Theorem 4 (frozen), which credits `MT1.md`'s local evenness; `LW1_5.md` Z-U proves the `L5-U` case. It is rebuilt here."
- **E4 (item 42, line 99).** After "ω(B* · B)/ω(B*B)" insert "for `B∈A^G` with `ω(B*B)>0`". Alternatively, define `J_S` as the kernel of the direct sum of the GNS representations of the states in `S`, as in §3.1; that form needs no stability clause.

Optional (E5-E8).

- **E5 (item 43, line 101).** Replace "it has not received a fresh four-test review" by "A fresh four-test of the repaired text gives C C P P (`GB1Z2L5_REFEREE.md` §3.2)". Give test 4's reason as in §3.2.
- **E6 (item 11, line 22).** Replace "are disjoint" by "share no matter or link factor".
- **E7 (item 37, line 85).** Replace "the central projection onto its standard component" by "the projection onto the standard isotypic component of this S₃ action".
- **E8 (status block).** Add one line on the downstream change, as in §6.

## 5. Open statements to carry by name

- **GB1-Z2[L5,SEC].** The Z₂ rung under R-SEC, in the repaired form of §3.1, or under a similar quotient reading. It exists as a question only if the owner adopts such a reading. Theorem 9 bounds it: no class that dominates a multiple of a character state works.
- **GB1-Z2[L5,5U]** (name proposed here; it names GB1's own usage and adopts nothing). "Some admissible update of `L5-U[m]` or `L5-O[S_+]`, some algebra `𝔅⊂𝔄`, some class of states fixed in advance, and an identification of `𝔅` on that class with the Z₂ link-and-matter operators, give `ω(α^t(B))=ω(α_{Z₂}^t(B))` for every `t≥0`, every `B∈𝔅` and every `ω` in the class, in the sense of `GB1.md` Theorem 5U." (Z-a) fails at the tick (`GB1.md` line 183). (Z-b) fails at the matter layer (line 184). Theorem 4 does not reach this statement.
- **The centre-Z₂ subgroup reading of (Z-c).** Theorem 8(b) needs a torus; the centre is finite. `GB1.md` line 185 records its test failures "1 F" and "4 F".
- The rest of `GB1.md` line 13, unchanged: GB1-O; GB1-U1 and GB1-SU2 beyond the proved sectors; GB1-H with the hand-off GAP; E-1, E-2, E-3, E-4 = Y3; GB1-SC; GB1-CF; T0-QLR[G], T0-start[G], T0-rate; Y1, Y2, Y2-W, VC1, TM1, ZM1-G, the observable dictionary.

The distiller's GAP (R-SEC covariance) is closed by Lemma R as a repair of a proposed reading. It is not carried as open.

## 6. Freeze recommendation

**Freeze after E1-E4.** The mathematics is sound. Every theorem holds as stated. The one ERROR is a sentence about the witness, not a step of a proof. The three INCOMPLETE items are a missing open-statement name, a missing credit and a missing domain clause.

What the frozen part proves: for every `L5-U[m]`, `1≤m≤9`, and for `L5-O[S_+]`, the full invariant algebra `𝔄^G` has a character, so no unital *-homomorphism from any characterless unital C*-algebra lands in it. Every Z₂ source, every `Z_N` source with `N≥2` and every finite nontrivial abelian source is characterless. Hence GB1-Z2[L5], as stated at `GB1_REFEREE.md` line 233, fails at algebra level and at sector level in the sense of `GB1.md` Definitions 1-2. The first failing step is the clause "unital" of the readout. Under uniform locality with a separating block map, dropping "unital" does not help (Theorem 6). Status after freeze: author-side mathematics with one referee check. It is not an audit result.

**Downstream, for the lead's amendment to `GB1.md`.** The Z₂ row for both named laws becomes: "ZM1-INV readout (Definitions 1-2): none, `GB1Z2L5.md` Theorem 4; first failing step, the unit. Frozen-class reading GB1-Z2[L5,5U]: open; (Z-a) fails at the tick, (Z-b) at matter." The U(1) and SU(2) rows do not change; the U(1) source has a character (Theorem 7). In `ZM1INV.md`, R5's conclusion holds for every `m`, by R1; K-INV is not affected. R-SEC is a candidate change of the owner's ZM1-INV codomain, graded C C P P; only the owner adopts. No axiom, law, reading or working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

---

## FINISH

**Proved** (this referee, one check).
- Verdicts on all 48 items of `GB1Z2L5.md`: 44 CORRECT, 1 ERROR, 3 INCOMPLETE. Theorem A (distilled Theorem 4), Lemma 2 (Theorem 2), Lemma 3 (Theorem 3), Corollary B (Theorem 5) with its `Z_N` and finite-abelian reach, Proposition C (Theorem 6), Proposition D(i)-(iii) (Theorems 7, 8) and Theorem 9 are correct.
- Referee closure, Lemma R: the repaired R-SEC is well defined. Its ideal is a closed two-sided ideal; cell lifts and the tick act on the quotient by automorphisms when `S∘β=S` and `S∘α=S`; the quotient is `π_S(𝔄^G)`; Theorem 9 holds in this form.
- Referee closure: the finite-abelian case of Corollary B, written out.
- Fresh four tests of the repaired R-SEC: C C P P.
- `[check]`, guide only: the S₃ corner relations for `q=1,4`; the plaquette weight count is 1 for `m=1,…,9`.

**Counterexamples.**
- `GB1Z2L5.md` line 47, "not ... a stationary state": false for odd `m` under the base tick, by `ZM1INV.md` R1(b).

**Open by name.** GB1-Z2[L5,SEC]; GB1-Z2[L5,5U] (name proposed here); the centre-Z₂ subgroup reading of (Z-c); and the list of `GB1.md` line 13 without GB1-Z2[L5].

**What changes downstream.** GB1: the Z₂ row splits as in §6; GB1-Z2[L5] as stated is refuted, and its frozen-class sibling GB1-Z2[L5,5U] stays open. ZM1INV: R5's conclusion extends to every `m` through R1. GB1Z2L5: edits E1-E4, then freeze. Nothing is adopted.
