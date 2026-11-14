lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# MT1 referee report (pass 3)

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (the referee) of part MT1 under the method of open PR #10138. In that method Claude drafts at length and runs to closure, Codex distils, a fresh session referees, and then the part is frozen.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max reasoning effort, headless lane `mac-mini-toe-lane`. This session wrote neither pass 1 (`MT1_DRAFT.md`) nor pass 2 (`MT1.md`). It ran no subagents. This is one check: one whole-part, line-by-line read of `MT1.md`. It read no other review of MT1. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status. It adopts no law, reading, definition or specification. It changes no axiom and no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A "referee closure" is a complete argument, written here, for a step that `MT1.md` leaves out. Referee closures are themselves unrefereed. A "[check]" is a small scratch computation. It guides or refutes; it never proves.

**Text read.** `MT1.md` at commit `c2bfcd143`, the last commit that touches it and the branch head when read. SHA-256 of the file read: `c8263124f7df9beacc8c96876998bef91e8ed6d5a6e4beab9afaec68a986a1bd`. Line numbers below refer to that file.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), as given in the lane brief | `c2bfcd143` |

No other branch was read.

**Files read, by line, at `c2bfcd143`.** In this folder: `MT1_DRAFT.md` lines 1-343 (all); `TOE_ASSEMBLY.md` lines 195-222 (D1 and LW1-5-RQ), 264 and 277 (ZM1-i), 316-334 (LZ1) and 352-367 (MT1); `LW1.md` lines 36-112 (definitions and distiller definitions 1-28), 184-230 (A1, A1a, dressed factorization, A2, A3), 241-247 (B4 and gauged covariance) and 320-389 (B10, B11, C1); `LW1_5.md` lines 1-353 (all); `CH1.md` lines 1-17 (amendments and open list), 33 (inferred definition 7), 49 (F3), 79 (S1), 113 (S1-5), 163-167 (O-A and the paragraph after it) and 195-237 (end of the U-T′ proof, Corollary U-T″, GAP U-T, AM-5, section 5). For format only: `LW1_REFEREE.md` lines 1-80 and its section headers, and `Y2W_DRAFT.md` lines 1-40. `CH1_5U.md` was not read; only its hash was recomputed.

**Hashes.** `MT1.md` line 13 records six SHA-256 values: the draft, the assembly, LW1, LW1_5, CH1 and CH1_5U. All six equal the hashes of those files at `c2bfcd143` [check: `shasum -a 256`].

**Working set used, by name.** PS-5 (the D1 text: five fermion modes per site, full algebra `Cl(10)`). PS-6 and PS-6r, only through the two laws of `LW1_5.md` section 2. PS-1c, only through the cell lifts. The owner decision LW1-5-RQ (both laws live). Nothing else from the working set is used.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws, the working set and the proposed readings are read plainly.

**Method.** I re-derived every proof in `MT1.md` by hand. I compared each item with its pass-1 source in `MT1_DRAFT.md` and with each cited line of `LW1.md`, `LW1_5.md`, `CH1.md` and `TOE_ASSEMBLY.md`. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix); INCOMPLETE (a named missing step, with what is missing). The checks are three scripts in `/tmp/toe-mt1ref/`: `check_mt1ref.py`, `check_olift.py` and `check_witness.py`, with outputs `out.txt`, `out_olift.txt` and `out_witness.txt`. They use floating point on 8 by 8 matrices and on a torus of 64 sites. Each ran in under 1 s and under 177 MB, after `memory_pressure` showed 66 percent free.

**Counts.** 93 items: 81 CORRECT, 3 ERROR, 9 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem. All four GAPs that the distiller marked are real, and the distiller's correction at line 92 is right. Section 3 gives eight referee closures. One of them, C4, proves the classification that `MT1.md` line 120 leaves unproved.

**Credits.** As in `MT1.md` and `MT1_DRAFT.md`: Levin and Wen (the three-hop identity); Bravyi and Kitaev, Zohar and Cirac, and Brower, Chandrasekharan and Wiese (the cluster comparison); Golterman, and Catterall, Pradhan and Samlodia (spin-taste factorization); Anber and Donoghue (attack A3). This report adds no citation. No citation is a proof step here.

---

## 1. Verdict table

| # | Item (MT1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status sentence (5) | CORRECT | |
| 2 | §0 "Proved" list (7) | ERROR | "A symmetry-allowed linear perturbation splits the cone" overstates the scope. At `μ=0`, the only value with a free node, the free symmetry `σ` forbids the term (C4). Fix: edit E1. The list also omits Theorems 1 and 6 and Corollary 9.1. |
| 3 | §0 GAP, MT1-i clause (9) | CORRECT | Gap real; see G3. |
| 4 | §0 GAP, R-X clause (9) | CORRECT | Gap real; see G2. |
| 5 | §0 GAP, ER clause (9) | CORRECT | Real. It is an open bridge, not a gap in a proof; see G1. |
| 6 | §0 GAP, chirality clause (9) | ERROR | "see Theorem 5" points to the wrong item. The correction is the paragraph after Theorem 7 (line 92). |
| 7 | §0 GAP, checks and interacting use (9) | CORRECT | Real for the interacting use. The quoted numbers are reproduced [check]. C1 and C4 replace the load-bearing checks by proofs. |
| 8 | §0 open list (11) | CORRECT | CH1-5O-i is listed open, as in `CH1.md` line 17. `CH1.md` Amendment 2 says CH1-5O-i "as worded ... fails in that reading", with a residual case open. |
| 9 | §0 provenance, HEAD and hashes (13) | CORRECT | All six hashes equal [check]. |
| 10 | §0 provenance, effort and session (13) | ERROR | The line gives "reasoning effort high ... session `01a1af61-...`" and later "reasoning effort and session ID not visible". The two clauses contradict each other. Fix: edit E3. |
| 11 | §1 Setting: site content, laws, free tick (17) | CORRECT | Matches PS-5 (D1), LW1-5-RQ and `LW1_5.md` inferred definition 4. |
| 12 | §1 Setting: the L5-O shift (17) | INCOMPLETE | The transfer rule is missing. Statements about `V` at `K` hold for the O walk at `K+(π,π,π)` after conjugation by `D=diag(i^{r_1+r_2+r_3})` (`LW1_5.md` line 322). Theorems 9 and 11 use this rule. For L5-O the internal generator is `DSD*`, and `DSD*≠S` [check]. Fix: edit E4. |
| 13 | §1 cell notation, `A_j`, `Z_j`, `Γ_j` (19-24) | CORRECT | Matches draft §1.1. |
| 14 | §1 `O`, lifts, `Γ_F`, `θ` (26) | CORRECT | |
| 15 | §1 reading R-X (28) | CORRECT | Proposed, not adopted. Four tests in section 4. |
| 16 | §1 spinor-class label (30) | CORRECT | From `u_1²u_2=λ²u_2u_1²` and `u_1²` scalar, `λ²=1`. |
| 17 | §1 ER formula (32) | CORRECT | `Σ_{ij}ε_{kij}[K_i,K_j]=−2iv²(L_k+S^N_k)`, so `J_k=L_k+S^N_k`. |
| 18 | §1 ER status sentences (32) | CORRECT | |
| 19 | §1 readings M1-M3 (34) | CORRECT | The draft's M1 also allows 15 fields (no right-handed neutrino); the omission is harmless. |
| 20 | Thm 1, existence (38, 40) | CORRECT | LW1 A2 gives a sign lift. |
| 21 | Thm 1, uniqueness and five-flavour form (38, 40) | CORRECT | Every edge lies in one tiling (LW1 A1), so a diagonal unitary commuting with `R_e, R_o` is constant on the connected lattice. |
| 22 | Thm 1, cell-periodicity (40) | CORRECT | `f(x)f(x+2e_k)=ε(e)ε(e')=1` follows directly from the consecutive-edge sentence. The sentence on periodicity of the ratios is not needed. |
| 23 | Thm 1, fibre covariance (38, 40) | CORRECT | `ρ(Q)` maps the fibre vector `(K,r)` to `f(r)` times the fibre vector `(QK,g_Q r)`. |
| 24 | Thm 2, statement (42-46) | CORRECT | |
| 25 | Thm 2, proof for U (48) | CORRECT | `c_{i,e}c†_{i,e}=1−n_{i,e}`, `c†_{i,e}n_{i,e}=0`, and reversing three anticommuting factors gives `(−1)³`. |
| 26 | Thm 2, proof for O (48) | CORRECT | |
| 27 | GAP (draft §2.1) (50) | CORRECT | Gap real; see G2. C1 proves both sides nonzero for the law's own link components. |
| 28 | Thm 3, Hilbert-space equivalence (52) | CORRECT | Before the constraints both sides have dimension `2^{35V}` on a torus of `V` sites and `3V` links. |
| 29 | Thm 3, "35 complex modes per site" on a finite box (52) | INCOMPLETE | No boundary convention for a box is stated, and boundary sites have fewer links. The count is exact on every even torus. Fix: edit E5. |
| 30 | Thm 3, site values, Gauss generators and hops local (52) | CORRECT | |
| 31 | Thm 3, centre element equals cluster parity (52) | CORRECT | [check]: the product of ten Majoranas is `i` times the parity of five modes; the site factor of `ω_x` is `−iP_x`. |
| 32 | Thm 3, centre-even locality (52) | INCOMPLETE | Missing: every law operator is the restriction of a mode polynomial, and a parity average gives a cluster-even extension. Closure C2. |
| 33 | Thm 3 proof, Klein step (54) | CORRECT | |
| 34 | Thm 3 proof, grouping into cluster-even factors (54) | CORRECT | The O grouping drops the hop's scalar `i/2`; harmless. |
| 35 | Thm 3 proof, Gauss generators, Jordan-Wigner, constraints (54) | CORRECT | |
| 36 | Thm 3 proof, the U and O centres (54) | CORRECT | `LW1_5.md` lines 162 and 199. |
| 37 | Thm 3 proof, "centre-even local monomials ... map locally" (54) | INCOMPLETE | The step covers monomials, not general operators. Closure C2. |
| 38 | GAP (draft Corollary 2.3) (56) | CORRECT | Gap real; see G3. |
| 39 | Thm 4, Clifford relations (60, 67) | CORRECT | [check] |
| 40 | Thm 4, basis of 64 monomials (60, 67) | CORRECT | |
| 41 | Thm 4, fibres of `R_e`, `R_o` (61-64, 67) | CORRECT | [check] |
| 42 | Thm 4, rotation rules (65, 67) | CORRECT | [check], all 24 rotations. |
| 43 | Thm 5, one-body anticommutation (69, 71) | CORRECT | |
| 44 | Thm 5, five flavours (69, 71) | CORRECT | The step uses that 5 is odd. With an even number of flavours a twist can remove the sign. |
| 45 | Thm 5, Fock identity (69, 71) | INCOMPLETE | `Γ_F` acts on a finite torus. The statement that lifts exist and anticommute on every even torus is missing. Fix: edit E6. |
| 46 | Thm 5, dressed automorphisms (69, 71) | CORRECT | The dressed L5-O lift acts on matter by the sign lift of `V`, not of `WVW*` (C7). The commutator is `−1` either way. |
| 47 | Edge-axis anticommutation (73) | CORRECT | Five transpositions; [check]. |
| 48 | `ρ̂(C_4)⁴=−1` and the phase redefinition (73) | CORRECT | [check] |
| 49 | Thm 6, `θ` equals conjugation by the product of centres (75, 77) | INCOMPLETE | The centre elements are not named: `e^{iπ𝒢_x}` (L_cube), `Γ_x(−1)` (U), `ω_x` (O). "Multiply to the identity" should read "multiply to a scalar". Fix: edit E7. |
| 50 | Thm 6, gauge-invariant local operators are `θ`-even (75, 77) | CORRECT | |
| 51 | Thm 6, product of all centres on a torus (75, 77) | INCOMPLETE | For O the site factors contribute `(−i)^V`, which the proof omits. C8 shows that all three scalars equal 1 on every even torus. |
| 52 | Spinor-label paragraph (79) | CORRECT | |
| 53 | Thm 7, expansion and `v` (83-87, 90) | CORRECT | Duhamel gives `i dV(0)=vΣ_jK_je^{iεR}Γ_j`; [check]. |
| 54 | Thm 7, leading eigenvalues `±v‖K‖`, fourfold (88, 90) | CORRECT | |
| 55 | Thm 7, `K=0` is the only node (88, 90) | CORRECT | LW1 B10 at `μ=0`: `1−cos w=sin²ε(1−χ)`. |
| 56 | Thm 7, the `μ>0` identity (88, 90) | CORRECT | |
| 57 | Correction (92) | CORRECT | `UχU*=e^{iεR_e}χ≠χ` for every `ε` in the window, not only for generic `ε`; [check]. |
| 58 | Thm 8, two commuting spin-1/2 triples; `[S,R_e]=0` (94, 96) | CORRECT | |
| 59 | Thm 8, `C²_spin⊗C²_taste` on each `χ=±1` space (94, 96) | CORRECT | |
| 60 | Thm 8, `ρ̂(Q)=S(Q̃)T(Q)` (94, 96) | INCOMPLETE | `S(Q̃)` is used but not defined. Missing: `S(±e^{−iφn·σ/2})=±e^{−iφn·S}`. Fix: edit E8. |
| 61 | Thm 8, the classes of `T` (94, 96) | CORRECT | |
| 62 | Thm 8, irreducibility of taste and of each chirality (94, 96) | CORRECT | |
| 63 | Character moduli `4,1,0,0,0` (98) | CORRECT | [check] |
| 64 | Thm 9, boost commutator (100-103, 106) | CORRECT | Re-derived term by term. |
| 65 | Thm 9, `J`, `[J,h_1]=0`, spin 1/2 (102-104, 106) | CORRECT | |
| 66 | Thm 9, free nodes satisfy ER; internal generator `S` (104, 106) | CORRECT | For L5-O, read in the frame of item 12. |
| 67 | Thm 9, the `μ>0` clause (104, 106) | CORRECT | Scope: this is the action of `S`. At `μ>0` there is no node, and ER gives no group there. |
| 68 | Cor 9.1, first two assertions (108, 110) | CORRECT | `T(Q)` commutes with `R_e`, so `UT(Q)U*=T(Q)`; the conjugation is redundant [check]. |
| 69 | Cor 9.1, pure spin rotation exactly for the identity and face half-turns (108, 110) | CORRECT | |
| 70 | Cor 9.1, no continuous extension of taste (108, 110) | CORRECT | The argument does not need continuity. |
| 71 | Choice of spin combination (112) | CORRECT | |
| 72 | Thm 10, inversion lift `±A_1A_2A_3` (118) | CORRECT | [check] |
| 73 | Thm 10, covariance of `G` and `Z^G` (116, 118) | CORRECT | [check] |
| 74 | Thm 10, antiunitary condition (116, 118) | CORRECT | `D_rŪD_r=U` because `D_rA_jD_r=−A_j`. |
| 75 | Thm 10, axial speeds (118) | CORRECT | `{Γ_3,Z_3}=0`. |
| 76 | Thm 10, first-order splitting on the diagonal (118) | CORRECT | `Y` has eigenvalues `±2√3` (twice each) and `0` (four times) [check]. The speeds at `u=0.05` match the draft to its printed digits; the largest is `1.05815`, which the draft prints as `1.0581`. The eigenvalue step is Weyl's inequality, rebuilt from Courant-Fischer. |
| 77 | Thm 10, finite range (116, 118) | CORRECT | The proof treats the added term. "It" should read "the added term", or the `G` part should be added (its fibre `Σ_j sin K_jΓ_j` is also finite range). |
| 78 | `σ` is a free symmetry at `μ=0` (120) | CORRECT | LW1 A2, last paragraph. |
| 79 | `σ=M_e^{-1}τ` for the dressed tick at `τ_E=0` (120) | CORRECT | `τH_Cτ^{-1}=−H_{C+𝟙}`. |
| 80 | GAP after `σ` (120) | CORRECT | Gap real; see G5. C3 and C4 prove the classification. |
| 81 | Thm 11, 20 Weyl fields, ten of each chirality (124, 126) | CORRECT | Uses `χ_G`. |
| 82 | Thm 11, U content `2(5⊕5bar)` (124, 126) | CORRECT | |
| 83 | Thm 11, O content, two vectors (124, 126) | CORRECT | |
| 84 | Thm 11, no SU(5) `10`, no `16`; four fields on L_cube (124, 126) | CORRECT | |
| 85 | §6.1, M1 and M2 verdicts (130) | CORRECT | |
| 86 | §6.1, M3 on U (130) | CORRECT | Matches `CH1.md` Corollary U-T″ and GAP U-T. |
| 87 | §6.1, M3 on O (130) | INCOMPLETE | For one-site content on L5-O[S_+], the support is `LW1_5.md` F and K with Corollary SC.1. Theorem SC is about motion. Fix: edit E9. |
| 88 | §6.1, Amendments 1 and 4, R-CG1, scope (130) | CORRECT | Quotations match `CH1.md` lines 7 and 13. |
| 89 | MT1-S (134) | CORRECT | Open. "Leading generator" of an interacting state is not yet specified. |
| 90 | Attack A1 (136) | CORRECT | Correct as written. C4-C6 move its failure point; see section 6. |
| 91 | Attack A2 (137) | CORRECT | C7 adds a second failing step for L5-O. |
| 92 | Attack A3 (138) | CORRECT | |
| 93 | Closing paragraph (140) | CORRECT | |

## 2. The distiller's GAPs: real or not, and the repairs

The distiller marked four GAPs: the summary paragraph at line 9 (G1), and the GAPs at lines 50 (G2), 56 (G3) and 120 (G5). Line 92 is a correction, not a GAP; it is checked here as G4.

**G1 (line 9, the summary paragraph).** It has five clauses.
- *MT1-i.* Real. This is G3.
- *R-X.* Real. This is G2.
- *ER.* Real. `TOE_ASSEMBLY.md` line 354 asks for spin 1/2 "under the rotation group that emerges at long distance". The target does not define that group. ER is one proposed definition of it. No proof inside MT1 can supply the identification. It is a specification question for the owner. Repair: none needed in `MT1.md`; the clause states the limit correctly.
- *Chirality.* Real, and the correction at line 92 repairs it (G4). The clause points to the wrong item; see item 6.
- *Checks and the interacting use of the free symmetry action.* Real for the interacting use, which stays part of MT1-S. The quoted numbers are reproduced [check]: at `u=0.05`, speed `1.0012` along `e_3` and speeds `0.9427, 1.0004, 1.05815` along the diagonal (the draft prints the last as `1.0581`, truncated); eigenvalues of `Y`; real dimensions `8, 4, 3, 1` of the allowed triples; and `σ` acting at the node as a phase times the chirality of the leading generator. C1 and C4 replace the load-bearing checks by proofs.

**G2 (line 50, draft §2.1).** Real. Theorem 2 proves the algebraic identity in full. Two facts block the step from the identity to a physical exchange statistic. First, a colour-resolved term is not gauge invariant; only the colour sum is. So the resolved terms are not operators that the law applies. Second, the O bilinear `iγ_{y,a}U^{ab}γ_{x,b}` does not conserve matter number, so it need not move a particle. Inside R-X the draft's sentence "every excitation that the law's hops move has exchange sign −1" only restates the reading. **Repaired statement:** Theorem 2 as written. **Closure C1** proves that both sides of the identity are nonzero for the law's own link components, so the identity is not `0=0`.

**G3 (line 56, draft Corollary 2.3).** Real for the literal target. `TOE_ASSEMBLY.md` line 367 names the open input: "MT1-i (one law that produces the superlattice role pattern and the BKSF embedding together; the 2026-09-03 sweep reported the law "DESIGNED" there)". Theorem 3 produces neither a superlattice role pattern nor a BKSF embedding. It also constructs no excitation of the VC1 vacuum, which `TOE_ASSEMBLY.md` line 354 requires. One clause of the GAP needs a precision. "not a local representation of individual odd matter operators" holds for every local qubit encoding. Two operators on disjoint factors of an ordinary tensor product commute. Single modes `c_x`, `c_y` at distinct sites anticommute and have a nonzero product. So they cannot both be local on disjoint factors in such an encoding. That clause therefore marks no shortfall of Theorem 3 against BKSF. **Repaired statement:** Theorem 3 with closure C2. Each five-mode law has a local encoding of its centre-even algebra in clusters of 35 modes, with one constraint per link, built from modes that the link registers already carry. Whether the literal MT1-i still applies after D1 changed the site content is a question for the owner. This report proposes no restatement.

**G4 (line 92, the correction).** Verified. `χ=−iΓ_1Γ_2Γ_3` anticommutes with `R_e`, so `UχU*=e^{iεR_e}χ`. Here `sin ε≠0` throughout the window, so `UχU*≠χ` for every `ε`, not only generic `ε`. Since `G_j=e^{iεR_e}Γ_j`, `[χ,G_j]=−2i sin ε R_eΓ_jχ≠0` [check]. The chirality of the leading generator is `χ_G=UχU*`. `χ` commutes with every `ρ̂(Q)` because `ρ̂(Q)χρ̂(Q)*=det(Q)χ`. `U` commutes with every `ρ̂(Q)` because `ρ̂(Q)` permutes the `A_j`. So `U` carries the rotation-invariant `χ` eigenspaces to the `χ_G` eigenspaces, and the count of Theorem 11 is right.

**G5 (line 120).** Real: `MT1.md` gives no proof that `σ`, with the listed symmetries, leaves only the free direction. **Closure C3** computes the node form of `σ`: a phase times `χ_G`. **Closure C4** then proves the classification by hand. Every Hermitian triple on `C^8` that satisfies the node forms of the rotations, inversion, `Θ` and `σ` is a real multiple of `(G_1,G_2,G_3)`. Each of inversion, `Θ` and `σ` is needed, with an explicit first-order counterexample for each. The GAP's second sentence stays true for the interacting laws. The open step is now one step: whether the light fermion-odd node of the interacting state carries these symmetries in their free node forms.

## 3. Referee closures

Each closure uses only the definitions of `MT1.md` §1, Theorems 1 and 4 of `MT1.md` (both checked CORRECT above), and the quoted lines. Standard facts used are rebuilt in place.

### C1. Theorem 2 is not vacuous

**Statement.** Take for each `X` the colour component of the law's own link operator in the hop term that moves matter along that link: `r^y_jr^{x†}_k` or its adjoint on `Λ^mC^{10}` for L5-U, and `U^{ab}=iη_aη_{10+b}` for L5-O. Then both sides of Theorem 2's identity are nonzero operators.

**Proof.** `LW1_5.md` line 33: "Links commute with matter and are ordinary tensor factors." So `t_{il}t_{ki}t_{ij}=(X_{il}⊗X_{ki}⊗X_{ij})⊗F`, where `F` is the matter factor found in the proof of Theorem 2 and identities act on the other factors. A tensor product of operators is nonzero when each factor is nonzero.
- *L5-U links.* Fix `1≤m≤9`. Choose a basis vector `e_S` of `Λ^mC^{10}` whose set `S` contains the `y`-end mode `j` and omits the `x`-end mode `k`; such `S` exists because `1≤m≤9`. Then `r^y_jr^{x†}_ke_S=±e_{(S∖{j})∪{k}}≠0`. The adjoint is nonzero too.
- *L5-O links.* `(iη_aη_{10+b})²=−η_aη_{10+b}η_aη_{10+b}=1`, so `U^{ab}` is invertible.
- *Matter.* For U, `F=c†_{i,e}c_{l,b}c†_{k,c}c_{j,f}` maps the occupation vector with `(l,b)` and `(j,f)` filled and `(i,e)`, `(k,c)` empty to plus or minus an occupation vector. For O, `F=γ_{i,e}γ_{l,b}γ_{k,c}γ_{j,f}` is a product of four unitaries.

So the left side is nonzero, and the right side is its negative. ∎ [check: one colour, four sites, random link matrices; the left side equals minus the right side and is nonzero.]

### C2. Theorem 3, the locality of centre-even operators

**Statement.** On an even torus, let `O` be an operator of the law supported on finitely many sites and links. Suppose `O` commutes with the centre element at every site. Let `T` be the set of sites that carry matter of `O` or are endpoints of its links. Then `JOJ^{-1}` is the restriction to `𝔉_c` of a finite sum of products of operators on the factors `F_x`, `x∈T`.

**Proof.** *Step 1: every link operator is the restriction of a link-even polynomial.* For L5-U, take `|A|=|B|=m` and ordered products `r†_A`, `r_B`. Then `r†_Ar_B` maps `e_B` to `±e_A` and kills every other basis vector `e_{B'}` of `Λ^mC^{10}`, because `r_B` kills `e_{B'}` unless `B⊆B'`, and `|B'|=|B|`. So every matrix unit on `Λ^mC^{10}` is the restriction of a number-conserving, hence even, monomial. For L5-O, write `d_c` for the ten link modes and `P_0=∏_c(1−d†_cd_c)` for the projector onto their vacuum. Then `|e_A⟩⟨e_B|=d†_AP_0d_B`. The chirality is `Γ=−η_1⋯η_{20}=(−1)^{p_x+p_y}`, because the product of the ten Majoranas of one end is `i(−1)^p` [check]. So `S_+` is the even sector of the total link number. For `e_A,e_B∈S_+` the monomial `d†_AP_0d_B` is even. Matter operators on finitely many modes are sums of monomials. So `O` is the restriction of an element `Õ` that is a finite sum of products of matter monomials and link-even polynomials. By Step 1 of Theorem 3's proof, `Õ` is the same element of the graded algebra.

*Step 2: parity average.* The cluster parities `Π_x` and the link constraints are diagonal in the occupation basis, so each `Π_x` preserves `𝔉_c`. By Theorem 3 the centre element at `x` is a scalar times `Π_x`, so `JOJ^{-1}` commutes with each `Π_x` on `𝔉_c`. Put `Π_t=∏_{x∈t}Π_x` and `Õ'=2^{−|T|}Σ_{t⊆T}Π_tÕΠ_t`. On `𝔉_c` each term restricts to `Π_t(JOJ^{-1})Π_t=JOJ^{-1}`, so `Õ'` restricts to `JOJ^{-1}`. `Õ'` commutes with every `Π_x`, `x∈T`, and it contains no mode of a cluster outside `T`.

*Step 3: cluster-even monomials.* Normal-ordered monomials form a basis of the mode algebra, and conjugation by `Π_x` multiplies each by `(−1)^{(its degree in C_x)}`. So every monomial of `Õ'` is even in every cluster. Step 3 of Theorem 3's proof maps each such monomial to a product of operators on the factors `F_x` of the clusters it involves. ∎

### C3. The node form of `σ`

**Statement.** At `μ=0`, the fibre of `σ=V_e^{-1}τ` at `K=0` is `cχ_G` for a phase `c`, where `χ_G=−iG_1G_2G_3=UχU*`.

**Proof.** LW1 A2, last paragraph: "Finally translation by \(\mathbf1\) swaps the tilings, with a sign correction obtained by the same face argument. Conjugation by \(D_s\) reverses both hop operators. The resulting operation sends \(V_e\) to \(e^{ia_eR_o}\) and \(V_o\) to \(e^{-ia_oR_e}\)." So `τ=D_sD_dT_𝟙` with `τR_eτ^{-1}=−R_o` and `τR_oτ^{-1}=−R_e`. The sign gauge obeys `d(x)d(y)=η(e)η(e−𝟙)` on every edge `e={x,y}`. Two consecutive edges in one direction have equal `η` and equal shifted `η`, so `d(x+2e_k)=d(x)`. `D_s` is cell-periodic as well. `T_𝟙` maps `2b+r` to `2(b+r)+(𝟙−r)`. Hence `τ` commutes with cell translations, and its fibre is `τ̂(K)=τ_0E(K)`, with `E(K)=diag(e^{−iK·r})=exp(−iΣ_jK_j(1−Z_j)/2)` and `τ_0` a signed permutation.

Fix `j` and put `K=te_j`. `Z_j` anticommutes with `A_j` and commutes with `A_k`, `k≠j`. So `e^{itZ_j/2}A_je^{−itZ_j/2}=e^{itZ_j}A_j=cos t A_j+sin t Γ_j`, and `E(K)R_eE(K)^{-1}=3^{−1/2}(Σ_{k≠j}A_k+cos t A_j+sin t Γ_j)`. In fibres, `τR_eτ^{-1}=−R_o` reads `τ_0E(K)R_eE(K)^{-1}τ_0^{-1}=−3^{−1/2}(Σ_{k≠j}A_k+cos t A_j−sin t Γ_j)` for all `t`. The functions `1`, `cos t`, `sin t` are independent. So `τ_0A_kτ_0^{-1}=−A_k` for every `k` and `τ_0Γ_jτ_0^{-1}=Γ_j`. The unitary `χ` induces the same map. By Theorem 4 the six generators span `M_8(C)` as an algebra, so `τ_0=cχ` with `|c|=1`. Finally `σ̂(0)=e^{iεR_e}τ_0=c e^{iεR_e}χ=cUχU*`, because `χ` anticommutes with `R_e`. ∎ [check: `τ̂(0)` is proportional to `χ` and `σ̂(0)` to `χ_G` on a torus of side 4.]

**Node forms.** Near `K=0` put `h=i log V`; conjugation commutes with the analytic logarithm. Each symmetry of `V` gives a condition on the linear term `h_1(K)=Σ_jK_jN_j`, read off at first order in `K`. Rotations: `ρ̂(Q)N_jρ̂(Q)*=Σ_iQ_{ij}N_i`. Inversion: `ρ̂(I)N_jρ̂(I)*=−N_j`. `Θ`: `D_rN̄_jD_r=N_j` (Theorem 10's proof). `σ`: `σ̂(K)=σ̂(0)+O(K)` and `h=O(K)`, so `σ̂(0)N_jσ̂(0)^{-1}=N_j`, that is, `N_jχ_G=χ_GN_j`.

### C4. Proposition C: the four free symmetries force one cone at the node

**Statement.** Let `N_1,N_2,N_3` be Hermitian `8×8` matrices with
- (R) `ρ̂(Q)N_jρ̂(Q)*=Σ_iQ_{ij}N_i` for every `Q∈O`;
- (I) `ρ̂(I)N_jρ̂(I)*=−N_j`, with `ρ̂(I)=±A_1A_2A_3`;
- (Θ) `D_rN̄_jD_r=N_j`, with `D_r=Z_1Z_2Z_3`;
- (σ) `N_jχ_G=χ_GN_j`.

Then `N_j=aG_j` for one real `a`. For `a≠0` this is one isotropic Clifford cone with speed `|a|`. Each of (I), (Θ), (σ) is needed. Write `{j,k,l}={1,2,3}`. The triples
- `G_j+uU(iS_jA_j(A_k+A_l))U*`, which satisfies (R), (Θ), (σ) and not (I);
- `G_j+uUZ_j(A_k+A_l)U*`, which satisfies (R), (I), (σ) and not (Θ);
- `G_j+uZ^G_j` (Theorem 10), which satisfies (R), (I), (Θ) and not (σ);

have no isotropic cone for small `u≠0`.

**Proof.** `U=e^{iεR_e/2}` commutes with every `ρ̂(Q)` and with `ρ̂(I)`, since both commute with `R_e=Σ_jA_j/√3`. Also `D_rŪD_r=U`, since `D_rA_jD_r=−A_j`. So `M_j=U*N_jU` satisfies (R), (I), (Θ) and (σ′) `M_jχ=χM_j`.

Expand `M_j` in the basis `Γ^SA^R` of Theorem 4, with ordered products over subsets `S,R⊆{1,2,3}`. Conjugation by `χ` multiplies `Γ^SA^R` by `(−1)^{|R|}`. Conjugation by `ρ̂(I)` multiplies it by `(−1)^{|S|}`. Conjugation by `ρ̂(h_1)=λ_1Γ_2Γ_3` multiplies it by `(−1)^{|S∩{2,3}|}`; `h_2` and `h_3` act likewise with `{1,3}` and `{1,2}`. These maps act coefficient by coefficient. So (σ′) keeps only even `|R|`, and (I) keeps only odd `|S|`. (R) for `h_1, h_2, h_3` requires, in `M_1`, that `|S∩{2,3}|` be even and `|S∩{1,3}|`, `|S∩{1,2}|` be odd. With `|S|` odd this leaves `S={1}`. The same holds for `M_2`, `M_3` with their own index. So `M_j=Γ_jP_j` with `P_j∈span{1,A_1A_2,A_1A_3,A_2A_3}`.

Write `P_1=a+b_{12}A_1A_2+b_{13}A_1A_3+b_{23}A_2A_3`. Let `C` be the 3-fold turn with `Ce_1=e_2`, `Ce_2=e_3`, `Ce_3=e_1`. (R) for `C` gives `M_2=ρ̂(C)M_1ρ̂(C)*=Γ_2(a+b_{12}A_2A_3−b_{13}A_1A_2+b_{23}A_3A_1)`. Let `C_4` be the quarter-turn with `C_4e_1=e_2`, `C_4e_2=−e_1`, `C_4e_3=e_3`. (R) for `C_4` requires `ρ̂(C_4)M_1ρ̂(C_4)*=M_2`. The left side is `Γ_2(a−b_{12}A_1A_2+b_{13}A_2A_3−b_{23}A_3A_1)`. Comparing coefficients gives `b_{12}=b_{13}=:b` and `b_{23}=0`. So `M_j=Γ_j(a+bA_j(A_k+A_l))`.

`Γ_j` is Hermitian and `Γ_jA_jA_k` (`k≠j`) is anti-Hermitian. So `a` is real and `b` is imaginary. With `Γ_jA_j=iZ_j`, `M_j=aΓ_j+b′Z_j(A_k+A_l)` with `b′=ib` real. (Θ) sends `Z_jA_k` to `Z_j(D_rA_kD_r)=−Z_jA_k`, so `b′=0`. Hence `M_j=aΓ_j` and `N_j=aG_j`. Conversely `aG_j` satisfies all four conditions: (R), (I) and (Θ) by Theorem 10's proof, and (σ) because each `G_j` commutes with `G_1G_2G_3`.

*The witnesses.* Each witness satisfies the three conditions claimed [check: `check_witness.py`]. By hand, the parities of `|S|` and `|R|` and the action of `D_r` decide (I), (σ) and (Θ) as above. (R) holds for the second witness because it lies in the family `Γ_j(a+bA_j(A_k+A_l))`. It holds for the first because `S_j` and `Γ_j` transform alike under rotations, so the computation above applies with `Γ_j` replaced by `S_j`. For `Z^G` the failure of one cone is Theorem 10. Work in the frame of `M_j` for the other two. Without (Θ): `M_1=Γ_1+uZ_1(A_2+A_3)` gives `M_1²=1−2iu(A_1A_2+A_1A_3)+O(u²)`. Since `(A_1A_2+A_1A_3)²=−2`, the squared speeds along `e_1` are `1±2√2u+O(u²)`. Without (I): `iS_1=Γ_2Γ_3/2`, so `M_1=Γ_1+(u/2)Γ_2Γ_3A_1(A_2+A_3)`. `Γ_1` commutes with `Γ_2Γ_3A_1A_k`, so `M_1²=1+u·iχA_1(A_2+A_3)+O(u²)`. Since `(iχA_1(A_2+A_3))²=2`, the squared speeds along `e_1` are `1±√2u+O(u²)`. One isotropic cone has equal speeds in every direction. Both split at first order. ∎ [check: the real dimensions of the solution spaces are 8 (R), 4 (R, I), 3 (R, I, Θ), 1 (R, I, Θ, σ), 2 (R, I, σ), 2 (R, Θ, σ); squared-speed spreads along `e_1` at `u=0.01` are `0.0566` and `0.0283`.]

**Remark (L5-U at `μ=0=τ_E`).** The four symmetries are symmetries of the dressed L5-U tick there: rotations by `LW1_5.md` B1-U, inversion by C5, `Θ` by C6 and `σ` by `MT1.md` line 120. On matter one-body operators the first three act as the free ones, tensored with flavour. A Hermitian triple on `C^8⊗C^5` that commutes with `1⊗U(5)` has the form `N_j′⊗1_5`, because the commutant of `U(5)` on `C^5` is the scalars. So: if the leading generator of the light fermion-odd excitations of an invariant state is a Hermitian triple on `C^8⊗C^5`, invariant under `U(5)` and under these four symmetries in their free node forms, then it is `aG_j⊗1_5`. The hypothesis is not proved. In particular `σ=M_e^{-1}τ` contains the interacting gate `M_e`, so its action on an interacting node is not one-body.

### C5. Inversion is a symmetry of the dressed base ticks

**Statement.** Let `I(x)=𝟙−x`, the inversion through `c_0`. For `L_cube`, for L5-U with every `m`, and for L5-O[S_+], and for all `ε, μ, τ_E`, there is an automorphism of the quasi-local algebra that moves sites and links by `I`. It maps each cube gate to the gate of the image cube and fixes `W_E`. So it commutes with the tick automorphism.

**Proof.** `I` maps the even centres `c_0+2b` to `c_0−2b` and the odd centres `c_0+𝟙+2b` to `c_0+𝟙+2(−b−𝟙)`. So it preserves both tilings, maps links to links and reverses every link. Every face has sign product `−1` (LW1 A1) and `I` maps faces to faces. So LW1 A2's argument applies: "Their ratio has product one on every face. Fix its value at one site and define a site sign by multiplying the ratios along an edge path to that site." It gives signs `d` with `d(Ix)d(Iy)=η(e)η(Ie)` on every edge. The three covariance proofs treat reversed links explicitly. They use only that the map preserves both tilings, maps links to links and has such signs; none uses `det Q=1`.
- *L_cube.* LW1, gauged covariance: "If it reverses an oriented link, conjugation by the spin rotation \(e^{-i\pi S^x}\) sends \(E\) to \(-E\) and \(J\) to \(J^\dagger\)." The electric squares are preserved.
- *L5-U.* `LW1_5.md` B1-U: each rishon at the `z`-end goes to the same flavour at the `Iz`-end. On a reversed link the image of `Σ_{jk}c†_{y,j}r^y_jr^{x†}_kc_{x,k}` is the adjoint of the image link's summand after exchanging `j,k`, because link factors commute with matter. So the hop maps to `d(Ix)d(Iy)` times the image hop. The electric term is kept: "On a reversed link \(p_x\mapsto p_y=m-p_x\), and \((m-p_x-m/2)^2=(p_x-m/2)^2\)".
- *L5-O.* The exchange of the two sets of ten link Majoranas is ten transpositions, with determinant `(−1)^{10}=1`. It lifts to Spin(20) and preserves `S_+`. The hop transforms as computed in C7(a). "The end chiralities agree on \(S_+\), so the electric layer is preserved" (`LW1_5.md` A2-5).

In each case the sign identity maps `H_C` to `H_{IC}`, and both layers are kept because each tiling is. ∎

### C6. An antiunitary symmetry of the dressed L5-U and L_cube ticks at `τ_E=0`

**Statement.** On a finite even torus, let `𝒦` be complex conjugation in the product occupation basis. That basis is the matter Fock basis in a fixed Jordan-Wigner order, tensored with the occupation basis of each `Λ^mC^{10}` (L5-U) or the `|m⟩` basis of each spin-`S` link (L_cube). Let `D_s` send `c_{x,j}` to `(−1)^{x_1+x_2+x_3}c_{x,j}`. Then `Θ_d=D_s𝒦` satisfies `Θ_dU_0Θ_d^{-1}=U_0` for all `ε, μ` when `τ_E=0`. When `τ_E≠0` it maps `W_E` to `W_E^{-1}`.

**Proof.** In this basis `c_{x,j}`, `c†_{x,j}`, the rishon operators, `J` and `E` are real matrices. So each dressed hop `h_ℓ` is real and `𝒦h_ℓ𝒦=h_ℓ`. Its two matter factors sit at sites of opposite parity of `x_1+x_2+x_3`, so `D_sh_ℓD_s=−h_ℓ`. This is the dressed form of LW1 B10: "Each \(R_T\) is real and satisfies \(D_sR_TD_s=-R_T\)." Hence `Θ_dH_CΘ_d^{-1}=−H_C` and `Θ_de^{−iaH_C}Θ_d^{-1}=e^{(+ia)(−H_C)}=e^{−iaH_C}`. So `Θ_d` fixes `M_e` and `M_o`. At `τ_E=0`, `W_E=1`. For `τ_E≠0` the generator of `W_E` is real and fixed by `D_s`, so `W_E` goes to `W_E^{-1}`. ∎ On matter one-body operators `Θ_d` acts as LW1's `Θ=D_s𝒦`, tensored with conjugation on flavour. The argument does not apply to L5-O: its Majorana hop is not real in this basis, since `γ_{2j}=−i(c_j−c†_j)`.

### C7. The dressed L5-O lifts at the free O node

**Statement.**
- (a) The dressed L5-O[S_+] lift of `Q∈O` (`LW1_5.md` A2-5 and B1-5) acts on matter by `γ_{x,a}↦d(gx)γ_{gx,a}`, where `d(gx)d(gy)=η(e)η(ge)` on every edge. So it acts by the sign lift `ρ(Q)` of `V`, tensored with the identity on the ten labels.
- (b) `ρ(Q)` is a lift of the free O walk `WVW*` exactly when `Qe_j=e_{π(j)}` for every `j`: the identity and the two turns about `(1,1,1)`.
- (c) In the frame where the free O walk is `V`, the fibre of the dressed matter lift at the node is a phase times `ρ̂(Q)∏_{j:s_j=−1}Z_j`. It acts by `Γ_k↦Γ_{π(k)}` and `A_k↦s_kA_{π(k)}`. The `A`-triple rotates as a vector and the `Γ`-triple is permuted without signs.
- (d) The free O walk's own lift is `Wρ(Q)W*=c̄_Qρ(Q)D_Q`, with `|c_Q|=1` and `D_Q(x)=∏_{j:s_j=−1}(−1)^{x_j}`. On matter, `D_Q` is the action of the centre gauge transformation `∏_{x:D_Q(x)=−1}ω_x`.

**Proof.** (a) `LW1_5.md` line 257: "A geometric symmetry of the dressed Majorana law acts on a reversed link by exchanging the two sets of ten auxiliary Majoranas. ... it sends \(U^{ab}\) to \(-U^{ba}\), while reversing the two matter Majoranas gives the other minus sign. Site parity implements LW1's sign lift." In detail, let `e=(x,y)` with `y=x+e_i`, and let `g` reverse it, so the image link is `e′=(gy,gx)`. The `y`-end Majoranas `η_{e,a}` go to the source end `η_{e′,10+a}`, and the `x`-end Majoranas `η_{e,10+b}` go to the target end `η_{e′,b}`. So `U_e^{ab}=iη_{e,a}η_{e,10+b}↦iη_{e′,10+a}η_{e′,b}=−U_{e′}^{ba}`. With `γ_{z,a}↦d(gz)γ_{gz,a}`, `h_e=(i/2)Σγ_{y,a}U_e^{ab}γ_{x,b}` goes to `−(i/2)d(gx)d(gy)Σγ_{gy,a}U_{e′}^{ba}γ_{gx,b}`. `U` commutes with matter and `γ_{gy,a}γ_{gx,b}=−γ_{gx,b}γ_{gy,a}`, so this equals `d(gx)d(gy)h_{e′}`. On a link whose orientation is kept, `h_e↦d(gx)d(gy)h_{ge}` directly. So `η(e)h_e↦η(ge)h_{ge}` exactly when `d(gx)d(gy)=η(e)η(ge)`. That is Theorem 1's condition for `V`.

(b) With `W_x=i^{x_1+x_2+x_3}` and `gx=Q(x−c_0)+c_0`, `Σ_k(gx)_k−Σ_kx_k=Σ_j(s_j−1)x_j+(3−Σ_js_j)/2`. Hence `W*ρ(Q)W=c_Qρ(Q)D_Q`. So `ρ(Q)` commutes with `WR_eW*` and `WR_oW*` exactly when `ρ(Q)D_Q` is a lift of `V`. By Theorem 1 this holds exactly when `ρ(Q)D_Q` is a phase times `ρ(Q)`, that is, when `D_Q` is constant, that is, when no `s_j=−1`. A proper rotation with all `s_j=1` has even `π`. [check: exactly 3 of the 24 sign lifts commute with `WVW*`.]

(c) `D_Q` is cell-periodic, with fibre `∏_{s_j=−1}Z_j`. `Z_j` anticommutes with `Γ_j` and `A_j` and commutes with `Γ_k`, `A_k` for `k≠j`. So this fibre maps `Γ_k↦s_kΓ_k` and `A_k↦s_kA_k`. Theorem 4 then gives `Γ_k↦s_k·s_kΓ_{π(k)}=Γ_{π(k)}` and `A_k↦s_kA_{π(k)}`. [check]

(d) The computation in (b) with `W` and `W*` exchanged gives `Wρ(Q)W*=c̄_Qρ(Q)D_Q`. The site factor of `ω_x` is `−iP_x` (`LW1_5.md` line 162), and conjugation by `P_x` negates the Majoranas at `x`. ∎

**Consequence.** On L5-O the free walk's lifts and the dressed lifts differ by a centre gauge transformation that is not constant in space. It acts as the identity on gauge-invariant operators, but not on fermion-odd ones. At the free node the two actions exchange the roles of the velocity triple `Γ` and the taste triple `A`. So the rotation action on a fermion-odd excitation of L5-O depends on its gauge dressing. `MT1.md` line 79 already says that "a physical charged state and its boundary dressing still need specification". L5-U has no such difference: its free hop `c†_yc_x+h.c.` is symmetric under reversal, so the free walk and the dressed lifts of B1-U use the same sign lift `ρ(Q)`.

### C8. The product of all centres on a torus

**Statement.** On every even torus, the product of all local centre elements equals `(−1)^N` exactly, on `L_cube`, L5-U and L5-O[S_+].

**Proof.** The centre elements at different sites commute: two share at most one link, where they act through commuting end factors. Multiply the factors as in Theorem 6. For L5-O the `V` site factors give `(−i)^V(−1)^N`. The links give `(−1)^{#links}`, by `LW1_5.md` line 199: "Their product is \(\eta_1\cdots\eta_{20}=-\Gamma\), which is \(-1\) on \(S_+\)". For L5-U the links give `(−1)^{m·#links}`; for `L_cube` they give 1. LW1 §1: "Tori have even site side length \(L\)". So `V=L³` is divisible by 8, `(−i)^V=1`, and `#links=3V` is even. ∎

## 4. Four-test checks of the readings `MT1.md` uses

The tests: a reading fails if it (1) states or fixes a part's target, (2) is open-ended so that a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. `MT1.md` proposes six readings and adopts none. This report proposes no reading, specification or definition; the closures in section 3 are theorems.

| Reading (MT1 line) | (1) | (2) | (3) | (4) | Note |
|---|---|---|---|---|---|
| R-X (28) | pass | pass | pass | pass | The identity can return `+1` (bosonic hops) or `−1`. Under the working CAR premise, every colour-resolved hop of a law with CAR matter returns `−1`. So R-X checks the premise and the form of the hop, not the dynamics. It decides nothing downstream. |
| Spinor class (30) | pass | pass | pass | pass | It names a computed invariant, and both values occur. It is defined for every projective action of `O`, because commutators of commuting elements are scalars there. |
| ER (32) | pass, with a condition | pass | pass | pass | ER does not assert spin 1/2. On its domain, linear generators with the Clifford condition, it always returns 1/2 (Theorem 9). Off that domain it returns no group. So under ER all content of MT1(a)(2) lies in the domain condition, MT1-S. ER gives no spin to linear generators outside the Clifford condition, such as spin-1 generators. `MT1.md` already treats the identification with the physical rotation group as an open bridge. |
| M1 (34) | pass | pass | pass | pass | A count; it fails on `L_cube`. It counts the auxiliary free node, not a vacuum. |
| M2 (34) | pass | pass | pass | pass | It restates the target's own parenthesis "(a 16 of `Spin(10)`, or the Standard Model multiplet)" at the free node. It fails on both laws. |
| M3 (34) | pass | pass | pass | pass | It is `CH1.md`'s inferred definition 7; the frozen results decide it. |

## 5. Required edits

Each edit fixes one ERROR or INCOMPLETE item. None changes the content of a theorem.

- **E1 (item 2, line 7).** Replace "A symmetry-allowed linear perturbation splits the cone." by "A linear perturbation allowed by the cell rotations, inversion and the free antiunitary symmetry splits the cone; at `μ=0` the free symmetry `σ` forbids it." Add Theorems 1 and 6 and Corollary 9.1 to the list.
- **E2 (item 6, line 9).** Replace "see Theorem 5" by "see the correction after Theorem 7".
- **E3 (item 10, line 13).** Delete "reasoning effort and session ID not visible", or mark it as superseded by the lead's run-log line.
- **E4 (item 12, line 17).** After "changes the residue basis by a fixed unitary" add: "Statements below about `V` at cell momentum `K` hold for the L5-O free walk at `K+(π,π,π)` after conjugation by `D=diag(i^{r_1+r_2+r_3})` (`LW1_5.md` line 322). In particular the L5-O internal generator in Theorem 9 is `DSD*`."
- **E5 (item 29, line 52).** Restrict Theorem 3 to an even torus, or say "35 complex modes at each site whose six links lie in the region".
- **E6 (item 45, line 38 or 69).** Add: "Theorem 1 holds on every even torus: `g_Q(x+Lb)=g_Q(x)+LQb`, and the sign function is cell-periodic, hence `L`-periodic. So the one-body lifts anticommute on every even torus, as the `Γ_F` identity needs."
- **E7 (item 49, lines 75 and 77).** Name the centre elements: `e^{iπ𝒢_x}` on `L_cube`, `Γ_x(−1)` on U, `ω_x` on O[S_+]. Replace "multiply to the identity on the link algebra" by "multiply to a scalar, so their joint action on the link algebra is the identity".
- **E8 (item 60, line 94).** Define `S(Q̃)`: for `Q` the rotation by `φ` about the unit axis `n` and a lift `Q̃=±e^{−iφn·σ/2}`, put `S(Q̃)=±e^{−iφn·S}`.
- **E9 (item 87, line 130).** Add: "On L5-O[S_+], one-site operator content is tensor class (`LW1_5.md` F and K, and Corollary SC.1: "With one end-pure class on all links, every \(z_x\) is the scalar \(-1\) (Σ below), every local operator is tensor class everywhere, and (e) is vacuous."). So M3 fails there for the 16. Theorem SC adds that no spinor-class charge moves under any finite register."
- **E10 (item 51, lines 75 and 77).** Add the site phase: "For O the site factors give `(−i)^V`. On every even torus `V=L³` is divisible by 8 and the number of links `3V` is even, so all three scalars equal 1." (Closure C8.)
- **E11 (items 32 and 37, lines 52 and 54).** Add closure C2: every link operator is the restriction of a link-even mode polynomial, and the average over the cluster parities gives a cluster-even extension of a centre-even law operator.

**Recommended, not required.**
- R1. Add C1 to the GAP after Theorem 2: the identity holds with both sides nonzero.
- R2. Replace "no proof of this classification is supplied here" (line 120) by C3 and C4.
- R3. Update attack A1 (line 136) as in section 6.
- R4. Add C7 to attack A2 (line 137) and to line 79: on L5-O the free walk's lifts and the dressed lifts differ by a centre gauge transformation that is not constant in space. It acts as the identity on gauge-invariant operators, but not on fermion-odd ones.
- R5. Wording: line 92, "for generic `ε`" can read "for every `ε` in the window". Line 108: `UT(Q)U*=T(Q)`, so the conjugation can be dropped. Line 116: "It is the leading term" can read "The added term is the leading term". Line 40: the sentence on periodicity of the edge-sign ratios can be dropped.
- R6. Line 56: note that no local qubit encoding represents single odd operators locally (section 2, G3), so that clause marks no shortfall against BKSF.

## 6. Open statements to carry by name

- **MT1-S** (`MT1.md` line 134), statement unchanged. Open after three named attacks. Closures C4-C7 move the failing step of A1 and add one to A2.
  - *A1 (symmetry).* On L5-U at `μ=0=τ_E`, the rotations, inversion, `Θ` and `σ` are symmetries of the dressed tick (B1-U, C5, C6, `MT1.md` line 120). Their free node forms allow only the free direction (C4). So A1 now fails at one step: "the light fermion-odd node of an invariant interacting state carries these four symmetries in their free node forms". `σ=M_e^{-1}τ` contains an interacting gate, so this step is not one-body. Where `σ` is absent (`τ_E≠0`), A1 fails at Theorem 10. On L5-O two more steps fail: no antiunitary symmetry of the dressed tick is known (C6 does not apply), and the dressed lifts act on bare matter in the exchanged form of C7.
  - *A2 (continuity).* Fails at "a small parameter", as `MT1.md` says. On L5-O it also fails at "the free walk carries the dressed symmetry action": by C7 it carries that action only up to a centre gauge transformation that is not constant in space.
  - *A3 (renormalization).* Fails at "a controlled flow exists"; ZM1-i is open.

  No counterexample to MT1-S is known. One specification is missing: neither the working set nor `MT1.md` defines "the leading generator of the light fermion-odd excitations" of an interacting state. On L5-O the gauge dressing of those excitations also needs a specification (C7). The owner may specify both; this report proposes neither.
- **MT1-i** (`TOE_ASSEMBLY.md` line 367). Open under its literal text (G3). Whether the literal text still applies after D1 is a question for the owner.
- **Carried unchanged from `MT1.md` line 11:** MT1-ii as a physical family claim; VC1; ZM1-i; LZ1-i; CH1-5U-i; CH1-5O-i; CH1-5O-E; LW1-5-T; GA1-P-5; the owner reading R-CG1 of the 16.

## 7. Freeze recommendation

Freeze `MT1.md` after edits E1-E11. None of them changes a theorem. The three ERRORs are a scope phrase, a cross-reference and a provenance contradiction. Each of the nine INCOMPLETE items needs one or two sentences, given in section 5 or in closures C2 and C8. All four distiller GAPs are real, and `MT1.md` states each one correctly. Record C1-C8 as referee closures; they are unrefereed. Folding C1 and C3-C7 into `MT1.md` (R1-R4) sharpens attack A1 and adds the L5-O dressing point; it changes no conclusion of `MT1.md`. MT1 stays open, with MT1-S and MT1-i carried by name. R-X, the spinor-class label, ER and M1-M3 stay proposals; nothing here adopts them.

---

## FINISH

**Proved** (referee closures in this file; written out in section 3; unrefereed).
- C1: both sides of Theorem 2's identity are nonzero for the law's own link components.
- C2: every centre-even operator of either five-mode law is local on the 35-mode clusters it touches (the last sentence of Theorem 3).
- C3: at `μ=0` the free symmetry `σ` acts at the node as a phase times `χ_G`, the chirality of the leading generator.
- C4 (Proposition C): the node forms of the rotations, inversion, `Θ` and `σ` allow exactly the real multiples of the free velocity triple `G_j`. Each of inversion, `Θ` and `σ` is needed, with an explicit first-order counterexample for each. On L5-U at `μ=0=τ_E` this reduces the symmetry route to MT1-S to hypotheses about an invariant interacting state and its node.
- C5: inversion through `c_0` is a symmetry of the dressed base ticks of `L_cube`, L5-U and L5-O[S_+], for all constants.
- C6: `Θ_d=D_s𝒦` is an antiunitary symmetry of the dressed `L_cube` and L5-U ticks at `τ_E=0`, for all `ε, μ`.
- C7: the dressed L5-O lifts act on matter by the sign lift of `V`. Only 3 of the 24 are lifts of the free O walk. At the free O node they exchange the roles of the `Γ`- and `A`-triples. The free walk's lifts are the dressed lifts composed with a centre gauge transformation that is not constant in space.
- C8: on every even torus the product of all centre elements is `(−1)^N` on all three laws.
- Checked: every theorem of `MT1.md` (re-derived by hand); the distiller's chirality correction (G4); the six hashes `MT1.md` records.

**Counterexamples.**
- To "the rotations, inversion and `σ` force one cone at the node": the triple `G_j+uUZ_j(A_k+A_l)U*`, small `u≠0` (C4).
- To "the rotations, `Θ` and `σ` force one cone at the node": the triple `G_j+uU(iS_jA_j(A_k+A_l))U*`, small `u≠0` (C4).
- To `MT1.md` line 7 read without qualification, "A symmetry-allowed linear perturbation splits the cone": at `μ=0` the free symmetry `σ` forbids `uZ^G` (C3, C4).
- To "the dressed L5-O lifts are lifts of the free O walk": each of the 21 rotations with some `s_j=−1` (C7(b)).

**Open by name.**
- **MT1-S.** Three attacks failed. A1 (symmetry) now fails at "the light fermion-odd node of an invariant interacting state carries the rotations, inversion, `Θ` and `σ` in their free node forms"; where `σ` is absent it fails at Theorem 10. A2 (continuity) fails at "a small parameter", and on L5-O also at the mismatch between the dressed and free lifts (C7). A3 (renormalization) fails at "a controlled flow exists"; ZM1-i is open. No counterexample is known. "The leading generator" of an interacting state, and on L5-O the gauge dressing, need a specification.
- **MT1-i**, under its literal text in `TOE_ASSEMBLY.md` line 367; whether it applies after D1 is an owner question.
- Carried from `MT1.md`: MT1-ii as a physical family claim; VC1; ZM1-i; LZ1-i; CH1-5U-i; CH1-5O-i; CH1-5O-E; LW1-5-T; GA1-P-5; R-CG1.

**What changes downstream.**
- `MT1.md`: edits E1-E11 before freezing. MT1 stays open.
- `TOE_ASSEMBLY.md` MT1(e): no change from this report. MT1-i stays open under its literal text. MT1-ii is decided only per proposed reading. MT1(a)(2) reduces to MT1-S.
- LZ1: at `μ=0=τ_E` the four free symmetries exclude every linear one-body anisotropy of the free node (C4). Dropping any one of inversion, `Θ` or `σ` admits a first-order anisotropy; C4 gives the three terms. Where `σ` is absent (`τ_E≠0`), Theorem 10's term stays allowed.
- L5-O (MT1, CH1, CG1): on fermion-odd operators the dressed lifts and the free walk's lifts differ by a centre gauge transformation that is not constant in space. At the free node this exchanges the velocity and taste triples (C7). So the spin and taste labels of fermion-odd states on L5-O depend on the gauge dressing. That dressing needs a specification before MT1-S can be posed on L5-O.
- No working-set entry, axiom, law or reading changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
