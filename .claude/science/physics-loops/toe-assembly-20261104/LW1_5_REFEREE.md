lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW1-5 referee report (pass 3)

Written 2026-11-06 (UTC; 2026-11-05 local time) by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, maximum effort). It is pass 3, the referee, of part LW1-5 under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen. This session wrote none of the three pass-1 drafts and neither pass-2 session. It read `LW1_5.md` line by line, once. No review of this review was commissioned, and this report reviews no other review.

**What this file is.** One check of the distilled part `LW1_5.md`. It grants no status. It adopts no law, no reading and no specification. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "[check]" marks a tiny scratch computation in `/tmp/toe-lw15ref/` (`check_quotes.py`, `check_lw15.py`; together about 11 s and at most 0.6 GB resident, each started after `memory_pressure` showed 62 and 65 percent free). A check guides and never proves.

**Text refereed.** `LW1_5.md` at commit `b05ee6430` (its last change; the branch head when read). SHA-256 `8a9a7683bcc31bb197d81d4e2b72ab6e1555fd2a424ef9524f4272dfe41c3a2b`. Line numbers below refer to that file unless a file is named.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse) | `b05ee6430` |

No other branch was read. Files read at that commit, with the commit that last changed each and the start of its SHA-256:

| File | Lines read | Last change | SHA-256 (start) |
|---|---|---|---|
| `LW1_5.md` | 1-319 (all) | `b05ee6430` | `8a9a7683bcc31bb1` |
| `LW1_5_DRAFT.md` (pass 1) | 1-510 (all) | `e648fa3e0` | `ff2f7b51da584c25` |
| `LW1_5U_DRAFT.md` (pass 1) | 1-309 (all) | `c721a3507` | `b510f6f67eb47ced` |
| `LW1_5O_DRAFT.md` (pass 1) | 1-328 (all) | `c721a3507` | `992096e18a3fdbfe` |
| `VC1_5_DRAFT.md` | 1-30 (head), 60-99 (law, gauge average, Lemma C, Lemma S2′); lines 218, 294, 322, 351 by grep | `2d0adc0c0` | `bd72037fe5a705f0` |
| `LW1.md` | 14-100 (status, definitions), 176-208 (A1, A1a, dressed factorization, UALL, A2), 289-298 (B8b); theorem and GAP statement lines by grep | `da0ec1934` | `66d67e6609ee9627` |
| `TOE_ASSEMBLY.md` | 100-145 (PS-1 to PS-7), 169-222 (sections 3.2-3.5) | `7d2b20d29` | `8027d9d44eb5fcaf` |
| `B5B_DRAFT.md` | 63 (Definition F), by grep | `6d27df284` | `3bf103d255a1bc92` |
| `LW1_REFEREE.md` | 1-80 and section headings (format only) | `5a2a0affe` | `f252954767393db5` |
| `Y2W_DRAFT.md` | 1-40 (format only) | `92e03055c` | `f9d8db9c15b4b101` |

All six SHA-256 values that `LW1_5.md` records at lines 15 and 17 check out in full [check: `shasum -a 256`]. Five equal those of the files read: the three pass-1 drafts and `LW1.md` (line 15), and `VC1_5_DRAFT.md` (line 17). The sixth, the starting `LW1_5.md` of the completion session (line 17), equals that of `LW1_5.md` at its previous commit `beb68f037`, read with `git show`.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The working set and the proposed readings are read plainly. No hostile reading is used. Where a verdict depends on a reading, the reading is named and left to the owner.

**Working set used, by name.** PS-5, PS-6 and PS-6r; PS-1 read by PS-1c; PS-3 read by PS-3c; PS-7r; PS-11c; PS-Ar; LW1's conjugation reading of local gauge invariance (`LW1.md` section 1: "Gauge invariance of a state means invariance under these conjugations, not support in the sector \(\mathcal G_x=0\)."). The proposed readings PS-3g and PS-3h5 (not in the working set) appear only where `LW1_5.md` uses them. PS-2 and PS-4 are not used.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text where used: Jordan-Wigner, Clifford monomial bases, Schur's lemma, commutant arguments, the reversal anti-automorphism of a Clifford algebra, simplicity of \(\mathfrak{so}(10)\) (section 2.2), Cauchy-Schwarz for states, character sums over \((\mathbb Z_2)^S\). Standard facts that `LW1_5.md` itself cites and that this report does not rebuild: integration of a Lie algebra representation to the simply connected group, existence of Haar measure, the inverse function theorem. No literature is load-bearing.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step, supplied where possible). A "referee closure" is a short complete argument for a missing step. For each GAP that the distiller marked, section 3 says whether it is real and gives the repaired statement.

**Counts.** 99 items: 93 CORRECT, 2 ERROR, 4 INCOMPLETE. Each GAP label counts as one item. No ERROR or INCOMPLETE item changes the content of a theorem of `LW1_5.md`. Two GAP verdicts change the open list: the referee closure Theorem SC (section 3.1) shows that no spinor-class charge moves, so LW1-5-16 closes negatively for spinor class defined by the local centre.

---

## 1. Verdict table

| # | Item (`LW1_5.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 gaps paragraph (7) | CORRECT | It summarizes the GAPs as marked. Update it after edits R8-R11 (section 5). |
| 3 | §0 open list (9) | CORRECT | Restate LW1-5-16 after Theorem SC (section 3.1). |
| 4 | §0 premises (11) | CORRECT | |
| 5 | §0 scope of later work (13) | CORRECT | |
| 6 | §0 provenance and completion session (15, 17) | CORRECT | Recorded hashes match [check]. |
| 7 | §1 five modes, \(P\), \(M^{ab}\), \(n_j-1/2=M^{2j-1,2j}\), the \([M,\gamma]\) bracket (21-26) | CORRECT | Expanded by hand. |
| 8 | §1 site algebra, links, site frame, register change, compatibility (27) | INCOMPLETE | The site-frame definition omits "maps its site algebra onto itself" (section 2.2). |
| 9 | §1 exceptional set \(\mathcal E(H)\), finiteness on bounded intervals (29) | CORRECT | |
| 10 | §1 conventions; gauge invariance by conjugation (29) | CORRECT | |
| 11 | Inferred definition 1 (33) | ERROR | PS-3g read plainly gives the full partition (section 2.1). |
| 12 | Inferred definition 2 (34) | CORRECT | The "could" is supported by an abstract instance (section 4.A). |
| 13 | Inferred definition 3 (35) | CORRECT | |
| 14 | Inferred definition 4 (36) | CORRECT | It corrects `LW1_5_DRAFT.md` line 318, "Its free tick is the same as `L5-O`'s". |
| 15 | Inferred definition 5 (37) | CORRECT | |
| 16 | Inferred definition 6 (38) | CORRECT | |
| 17 | Inferred definition 7 (39) | CORRECT | Matches the end-pure and link-pure conditions of `LW1_5O_DRAFT.md` (K4), (K5). |
| 18 | Inferred definition 8 (40) | CORRECT | On a vector summand the formula of line 79 is not Hermitian; see item 45. |
| 19 | §2 six premise quotations (44-62) | CORRECT | Exact match with `TOE_ASSEMBLY.md` lines 177-182 [check: string comparison]. |
| 20 | §2 other LW1 qualifications (64) | CORRECT | |
| 21 | §2 proposed PS-3g and PS-3h5, four-test result (66) | CORRECT | Quotes match `LW1_5_DRAFT.md` lines 322 and 324 [check]. |
| 22 | §2 angles, cube generator, layers, base tick (68-72) | CORRECT | |
| 23 | §2 `L5-O` (74-79) | CORRECT | The end convention for \(L^{cd}_{\ell,z}\) is implicit (edit R3). "Nontrivial" is a correct addition. |
| 24 | §2 `L5-U` and its one-mode equivalence with `L_cube` (81-87) | CORRECT | [check] of the rishon sign; hand check of \(\mathcal G_x=Q_x-3\). |
| 25 | §2 law clauses: gates, plaquette class, initial state, transport, records (89) | CORRECT | |
| 26 | §2 free data and choice checks (91) | CORRECT | Match `LW1_5_DRAFT.md` section 8.3. |
| 27 | §3 C and C1, statement (95-99) | CORRECT | |
| 28 | §3 C and C1, proof (101) | CORRECT | Given the clause restored in item 8. |
| 29 | §3 C2, statement and proof (103-105) | CORRECT | Proves equality for \(U(5)\); pass 1 had only "contains". |
| 30 | §3 M and M.1, statement (107) | CORRECT | |
| 31 | §3 M, proof (109) | CORRECT | Independence of the \(X_j\) is one line (section 4.B). |
| 32 | §3 independence for the specified hops (111) | CORRECT | |
| 33 | §3 exceptional angles (113) | CORRECT | |
| 34 | §4 Q and G, statement (117-122) | CORRECT | |
| 35 | §4 Q and G, proof (124) | CORRECT | Both ends checked. |
| 36 | §4 R, statement (126) | CORRECT | |
| 37 | §4 R, proof (128) | CORRECT | Target-end links need the other-end reflection; one line (section 4.C). |
| 38 | §4 U, statement and proof (130-132) | CORRECT | |
| 39 | §4 closed subgroups; \(SU(2)\) blocks of the `L5-U` link operators (134) | CORRECT | |
| 40 | §4 S′, statement (136) | CORRECT | |
| 41 | §4 S′, proof (138) | INCOMPLETE | Three steps missing; referee closure in section 2.2. |
| 42 | §4 full-frame alternative A (140-144) | CORRECT | |
| 43 | §5 centre elements and their site factors (148) | CORRECT | |
| 44 | §5 F and K, statement and proof (150-152) | CORRECT | |
| 45 | §5 mixed registers (154) | INCOMPLETE | The electric gate on \(S_+\oplus\mathbb C^{20}\) is not specified (section 2.2). |
| 46 | §5 one-ended construction: register and tensor (156-162) | CORRECT | |
| 47 | §5 one-ended construction: \(X\), its orbit, \(\gamma_{y,a}X\), the swap family (164) | CORRECT | |
| 48 | §5 GAP: scope of the pass-1 no-16 conclusion (166) | INCOMPLETE | Real as a scope note; misses Theorem SC (section 3.1). |
| 49 | §5 Σ (168) | CORRECT | |
| 50 | §5 GAP: vector-class claim for reducible registers (170) | CORRECT | Real. The referee adds a counterexample to Lemma Z(iii) (section 3.2). |
| 51 | §5 S1-S4, statement (172) | CORRECT | The electric-gate hypothesis of item 45 applies to the reducible register. |
| 52 | §5 S1-S4, proof (174) | CORRECT | |
| 53 | §5 singlet criterion and the duality \(H_+^*\simeq H_-\) (176) | CORRECT | |
| 54 | §5 two link orbits and the reversal maps (178) | CORRECT | Both maps checked by hand. |
| 55 | §5 lattice states, recorded options, isotypic construction (180) | CORRECT | |
| 56 | §5 H (182-184) | CORRECT | |
| 57 | §6 \(Q_x\) and (6.1) (188-190) | CORRECT | |
| 58 | §6 pure local-invariance criterion (192) | CORRECT | |
| 59 | §6 Σ-U, statement (194-198) | CORRECT | Table checked. |
| 60 | §6 Σ-U, proof (200) | CORRECT | |
| 61 | §6 Z-U (202-204) | CORRECT | |
| 62 | §6 H-U and F-U (206-208) | CORRECT | |
| 63 | §6 exterior-power embeddings (210) | CORRECT | |
| 64 | §6 LW1-5U-PS7 (212) | CORRECT | Arithmetic checked. |
| 65 | §6 D: the five-mode selector (214-218) | CORRECT | All sums checked by hand. |
| 66 | §7 carry-over list (222) | CORRECT | |
| 67 | §7 A2-5 and B1-5, statement (224) | CORRECT | |
| 68 | §7 A2-5 and B1-5, proof (226) | CORRECT | |
| 69 | §7 B1-U, statement (228) | CORRECT | |
| 70 | §7 B1-U, proof, against `VC1_5_DRAFT.md` Lemma C (230-236) | CORRECT | Covers Lemma C (i)-(iv) for `L5-U`. |
| 71 | §7 resolution of the earlier `L5-U` covariance GAP (238) | CORRECT | |
| 72 | §7 B2-5 (240-242) | CORRECT | |
| 73 | §7 B8-5 and B8a-5, statement with (7.1) (244-251) | CORRECT | [check] |
| 74 | §7 GAP in pass 1: the number-copy formula (252) | CORRECT | Real. |
| 75 | §7 free-sea copy conclusion (252) | CORRECT | |
| 76 | §7 B8-5, proof (254) | CORRECT | |
| 77 | §7 B8b-5 (256-258) | CORRECT | Pair-creation identity checked. |
| 78 | §7 B11-5 (260-262) | CORRECT | |
| 79 | §7 E2b-5 (264-266) | CORRECT | |
| 80 | §7 records and open transport items (268) | CORRECT | |
| 81 | §7.1 preamble (273) | CORRECT | |
| 82 | §7.1 finite transport, B6-B7 (275-279) | CORRECT | |
| 83 | §7.1 support factorization and E1 (281) | CORRECT | |
| 84 | §7.1 edge factorization (283) | CORRECT | The inclusion of the span in the Lie algebra is left implicit (section 4.G). |
| 85 | §7.1 infinite supported couplings (285) | CORRECT | |
| 86 | §7.1 invariant optimizers, E6 (287) | CORRECT | |
| 87 | §7.1 records, B9 and B11 (289) | CORRECT | |
| 88 | §7.1 free-sea carry-over and the momentum shift (291) | CORRECT | |
| 89 | §7.1 two-valued record witness (293) | CORRECT | |
| 90 | §7.1 GAP: pass-1 centre conclusion (294) | ERROR | Misnamed source; and not real under inferred definition 7 (sections 2.1, 3.1). |
| 91 | §7.1 subgroup singlet with corrected expansion (295) | CORRECT | [check] |
| 92 | §7.1 finite-region S5 bound (296) | CORRECT | |
| 93 | §7.1 GAP: exceptional-angle probe, Lemma X1 (297) | CORRECT | Real; pass 1 says the same (`LW1_5U_DRAFT.md` line 185). |
| 94 | §7.1 GAP: four-test option inventory (298) | CORRECT | A scope note; the referee read the rows (section 3.6). |
| 95 | §7.1 GAP: optional subgroup selector, Remark D.2 (299) | CORRECT | Real; referee closure (section 3.7). |
| 96 | §7.1 closing paragraph (301) | CORRECT | |
| 97 | §8 downstream paragraph (305) | CORRECT | |
| 98 | §8 open decisions and obligations (307-317) | CORRECT | Restate the LW1-5-16 entry (edit R13). |
| 99 | §8 closing paragraph (319) | CORRECT | |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 11, inferred definition 1 (line 33).** The line reads: "PS-3g alone does not require this maximal choice: the scalar observable is also invariant. Thus PS-3h5 is a further proposal, not a consequence of PS-3g alone."

*What is wrong.* PS-3g, quoted at line 66, reads: "The actual value of a site is a joint value of the site observables that every exact frame at that site leaves unchanged." The noun phrase "the site observables that every exact frame at that site leaves unchanged" names all invariant site observables, that is, the whole fixed site algebra. A joint value of all of them is a joint eigenvalue of that algebra. C2 (line 103) gives the algebra: \(\operatorname{span}\{1,P_x\}\) for the exact group \(SO(10)\) of `L5-O[S_+]`, and the span of the six spectral projections of \(N_x\) for \(U(5)\). Its joint values are exactly \(P_x=\pm1\) and \(N_x\in\{0,\ldots,5\}\). The scalars alone are a sub-collection, not "the site observables that every exact frame leaves unchanged". So PS-3g, read plainly, with C2 gives the full partition. Pass 1 says this at `LW1_5_DRAFT.md` line 324: "It follows from PS-3g and Lemma C2."

*Fix.* Replace definition 1 by: "For PS-3h5, the actual value of a site is the joint value of the whole fixed site algebra of C2: \(P_x=\pm1\) under `L5-O[S_+]` and \(N_x\) under `L5-U`. This follows from PS-3g, read plainly, and C2. PS-3h5 remains a proposal: PS-3g is a proposal, and PS-3h5 also carries PS-3h's existence-and-motion clause." No theorem changes; §7 already uses these alphabets.

**Item 90, GAP: pass-1 centre conclusion (line 294).** The line reads: "`LW1_5O_DRAFT.md` Proposition P proves conservation of the centre projections, but its further claim that no propagating spinor excitation can exist requires a definition and analysis of excitations within a fixed centre sector; conservation alone does not give it."

*What is wrong.* (a) `LW1_5O_DRAFT.md` has no Proposition P. Its line 123 is "**Theorem P (spinor-class Gauss charges are static probes).**" (b) The definition is already in `LW1_5.md`. Inferred definition 7 (line 39) reads: "A spinor-class operator anticommutes with the local centre implementer." With it, conservation does give the claim after one elementary step. Every local operator splits into parts that are spinor class on fixed site sets. A part that is spinor class on a nonempty set \(T\) maps each joint centre sector to the sector that differs from it exactly on \(T\). The tick fixes every \(z_x\). So the set of sites where an excited state differs from its reference in centre class is the same at every tick. Within one joint centre sector every local operator is tensor class at every site, so an excitation inside a fixed sector is not a spinor excitation in this sense. Theorem SC (section 3.1) writes this out.

*Fix.* Cite Theorem P. Replace the GAP by Theorem SC, or by a pointer to it. Keep open only the reading question that pass 1 already names: which notion of "16" CG1 needs (reading R-CG1, `LW1_5O_DRAFT.md` line 271).

### 2.2 INCOMPLETE

**Item 8, the site-frame definition (line 27).** The line reads: "A site frame fixes the algebra of every other site and every link pointwise." *Missing:* "and maps the algebra of its site onto itself". `B5B_DRAFT.md` line 63, Definition F, reads: "A frame on `A` is an automorphism `φ` of `𝔄` with `φ(𝒜_A) = 𝒜_A` and `φ(z) = z` for every `z ∈ 𝒪_A`." `LW1_5_DRAFT.md` line 66 (Definition F1) has the same clause. The proof of C (line 101) needs it: "Every automorphism of a matrix algebra is inner" is applied to the frame restricted to \(M_{32}(\mathbb C)\). *Fix:* restore the clause.

**Item 41, the proof of S′ (line 138).** The proof reads: "the half-spin representation is faithful because none of the three nonidentity elements of the Spin(10) centre acts trivially", and later "a nontrivial one has dimension-45 image \(SO(10)\), and an injective one would identify groups with centres of orders four and two." *Missing:* (i) why the kernel of \(S_+\) is central; (ii) why the centre is \(\{\pm1,\pm\omega\}\); (iii) why a homomorphism with \(f(-1)\neq1\) has trivial kernel.

*Referee closure.* Read \(\operatorname{Spin}(10)\) as the group generated by the \(e^{i\theta M^{ab}}\) on the site space \(H=H_+\oplus H_-\). It is the image of the simply connected group in the site representation, and it is all that S′ uses.

1. *Vector map.* Each generator acts on \(\operatorname{span}_{\mathbb R}\{\gamma_a\}\) by a plane rotation, by the bracket of line 26. So \(g\gamma_ag^{-1}=\sum_bR(g)_{ba}\gamma_b\) with \(R(g)\in SO(10)\), and \(R\) is onto \(SO(10)\). If \(R(g)=I\), then \(g\) commutes with every \(\gamma_a\), so \(g=\lambda1\). Let \(t\) be the reversal anti-automorphism, \((\gamma_{a_1}\cdots\gamma_{a_k})^t=\gamma_{a_k}\cdots\gamma_{a_1}\). Then \((M^{ab})^t=-M^{ab}\), so \(g^tg=1\) on generators and hence on the group. For \(g=\lambda1\) this gives \(\lambda^2=1\). So \(\ker R=\{\pm1\}\), and \(-1=e^{2\pi iM^{12}}\) lies in the group.
2. *Centre.* A central \(g\) has \(R(g)\) central in \(SO(10)\), so \(R(g)=\pm I\): a matrix commuting with every \(E_{ab}-E_{ba}\) is scalar. Put \(\omega=e^{i\pi\sum_jM^{2j-1,2j}}\). Then \(R(\omega)=-I\), so \(\omega\) anticommutes with every \(\gamma_a\) and commutes with the even algebra, which contains the group. Since \(R(\omega)=-I\neq I\), \(\omega\notin\{\pm1\}\). So the centre is \(\{\pm1,\pm\omega\}\), of order four, and \(\omega^2=\prod_je^{2\pi iM^{2j-1,2j}}=(-1)^5=-1\).
3. *\(S_+\) is faithful.* Restriction to \(H_+\) maps the even algebra onto \(\operatorname{End}(H_+)\) (C2) with a kernel of dimension 256. It sends \(\gamma_{S^c}\) to a multiple of the image of \(\gamma_S\), since \(\gamma_SP\) is a multiple of \(\gamma_{S^c}\). So even monomials with at most one member of each pair \(\{S,S^c\}\) stay independent on \(H_+\). Quadratic monomials have octic complements, so the 45 quadratic monomials and \(1\) stay independent. If \(g\vert_{H_+}=1\), then \((g\gamma_a\gamma_bg^{-1})\vert_{H_+}=(\gamma_a\gamma_b)\vert_{H_+}\) for \(a\neq b\). Expanding gives \(\Lambda^2R(g)=1\). Then \(R(g)\) maps each coordinate plane onto itself, hence each axis onto itself, with equal signs: \(R(g)=\pm I\). So \(g\in\{\pm1,\pm\omega\}\). On \(H_+\), where \(P=1\), these act as \(1,-1,-i,i\). So \(g=1\).
4. *\(f\) is injective.* \(f(g)=\mathrm{id}\) makes \(S_+(g)\oplus1\) a scalar, so \(S_+(g)=1\) and \(g=1\).
5. *\(f\) is not Bogoliubov.* Suppose every \(f(g)\) is a Bogoliubov frame \(\varphi_{R_f(g)}\). The map \(R_f\) is a smooth homomorphism into \(O(10)\), since \(R_f(g)_{bc}=\tfrac1{32}\operatorname{tr}(\gamma_bf(g)(\gamma_c))\). Also \(R_f(-1)=-I\), because \(f(-1)=\operatorname{Ad}P=\varphi_{-I}\). The kernel of \(dR_f\) is an ideal of \(\mathfrak{so}(10)\). The algebra \(\mathfrak{so}(10)\) is simple. *Rebuilt:* let \(I\neq0\) be an ideal and \(X\in I\) have a nonzero \(E_{ab}\)-coefficient. Each \(-\operatorname{ad}(E_{ac})^2\) is the projection onto \(\operatorname{span}\{E_{pq}:\lvert\{p,q\}\cap\{a,c\}\rvert=1\}\). The product of these projections over the eight \(c\notin\{a,b\}\) is the projection onto \(\mathbb CE_{ab}\). So \(E_{ab}\in I\), and the brackets \([E_{ab},E_{bc}]=E_{ac}\) give all of \(\mathfrak{so}(10)\). The kernel of \(dR_f\) is not everything, since \(R_f(-1)\neq I\) and the group is generated by exponentials. So \(dR_f\) is injective. Then \(\ker R_f\) is discrete and normal in a connected group, hence central. It omits \(-1\), and it omits \(\pm\omega\) because \((\pm\omega)^2=-1\). So \(R_f\) is an isomorphism onto \(SO(10)\) (connected, dimension 45). The centres then have equal order. But they have orders four and two. This contradiction proves the claim.

**Item 45, mixed registers (line 154).** The line reads: "The hop and electric gate conserve each link's centre class." *Missing:* the electric gate on \(R=S_+\oplus\mathbb C^{20}\) is not specified. Line 79 defines \(W_E\) only "For \(S_+\)". The formula \(\Gamma^x=i^5\rho(\eta^x_1\cdots\eta^x_{10})\) is not Hermitian on \(\mathbb C^{20}\). There \(\rho(\eta^x_1\cdots\eta^x_{10})\) is the rotation that is \(+1\) on the ten \(y\)-coordinates and \(-1\) on the ten \(x\)-coordinates; it squares to \(1\), so \(i^5\) times it squares to \(-1\), and \(e^{-i\tau_E\Gamma^x}\) is not unitary on that summand. *Referee closure:* \(\epsilon_{\ell,x}=e^{2\pi iL^{12}_{\ell,x}}\) is a function of an end generator. So it commutes with every operator that commutes with the end actions. The hop commutes with it because \(\rho(-1_{\operatorname{Spin}(20)})\) is central in \(\rho(\operatorname{Spin}(20))\). *Fix:* "The hop, and any electric gate whose generator commutes with both end actions, conserve each link's centre class." The same hypothesis belongs in S4 (line 172). It also belongs in `LW1_5O_DRAFT.md` Proposition S4 (line 213), which names "the electric gate of `LW1_5_DRAFT.md` section 8.1".

**Item 48, GAP: scope of the pass-1 no-16 conclusion (line 166).** The line reads: "Conservation of a local centre charge rules out dynamically changing its eigenvalue, but by itself does not exclude every possible propagating excitation within a fixed charge sector or every nonlocal construction." The GAP is real as a scope note. Pass 1's conclusion is `LW1_5O_DRAFT.md` line 165: "**Answer to item 1 (LW1-5-16).** Refuted for what CG1 needs." It rests on reading R-CG1, which pass 1 records at line 271 with test 3 conditional. *Missing:* (i) the centre argument proves more than "rules out dynamically changing its eigenvalue": no spinor-class charge moves, and the joint law of all centre classes is the same at every tick for every state (Theorem SC); (ii) an excitation within a fixed centre sector is tensor class at every site (Corollary SC.1), so it is no spinor excitation under inferred definition 7; (iii) "every nonlocal construction" is covered by part (d) of Theorem SC, which holds for every state however it was prepared. *Repaired statement:* section 3.1.

---

## 3. The distiller's GAPs: real or not, with repaired statements

`LW1_5.md` marks these GAP labels: line 166 (no-16 scope), 170 (vector class), 238 (an earlier covariance GAP, now resolved), 252 (pass-1 number formula), 294 (centre conclusion), 297 (Lemma X1), 298 (four-test inventory), 299 (Remark D.2). It also inherits the LW1 GAPs UALL and B12(ii-iii) (lines 7, 222, 301). Lines 166 and 294 share one repair.

### 3.1 Lines 166 and 294: real as a scope note at 166; not real at 294. Repaired by Theorem SC.

**Theorem SC (static spinor class).** Take finite link registers with commuting endpoint \(\operatorname{Spin}(10)\) actions, as at line 150, and a law whose gates commute with every \(\mathcal G^{cd}_x\). Let \(\alpha\) be its tick automorphism (LW1 E1 form) and \(z_x=e^{2\pi i\mathcal G^{12}_x}\) as at line 148.
(a) The \(z_x\) are pairwise commuting self-adjoint unitaries, and \(\alpha(z_x)=z_x\).
(b) Let \(O\) be local. Let \(S\) be a finite site set that contains every site where \(O\) has matter and both ends of every link in its support. For \(T\subseteq S\) put
\[
O_T=2^{-\lvert S\rvert}\sum_{t\subseteq S}(-1)^{\lvert t\cap T\rvert}\Big(\prod_{x\in t}z_x\Big)O\Big(\prod_{x\in t}z_x\Big).
\]
Then \(O=\sum_{T\subseteq S}O_T\), each \(O_T\) is spinor class exactly at the sites of \(T\), and \(\operatorname{Ad}z_x\) fixes \(O\) for \(x\notin S\).
(c) For \(s\in\{\pm1\}^S\) put \(\Pi^s=\prod_{x\in S}(1+s_xz_x)/2\). Then \(O_T\Pi^s=\Pi^{s\circ T}O_T\), where \(s\circ T\) flips the signs of \(s\) on \(T\).
(d) For every state \(\omega\), every \(n\ge0\) and every \(s\): \(\omega\circ\alpha^n(\Pi^s)=\omega(\Pi^s)\). So the joint law of the centre classes is the same at every tick, whatever local operator, limit or initial choice prepared \(\omega\).
(e) Let \(\omega(\Pi^s)=1\) and \(\omega(O_T^*O_T)>0\), and put \(\omega'=\omega(O_T^*\,\cdot\,O_T)/\omega(O_T^*O_T)\). Then \(\omega'\circ\alpha^n(\Pi^{s\circ T})=1\) and \(\omega\circ\alpha^n(\Pi^s)=1\) for every \(n\). So \(\omega'\circ\alpha^n\) and \(\omega\circ\alpha^n\) differ in centre class exactly on \(T\) at every tick. A spinor-class charge does not move.

*Proof.* (a) \(z_x\) is a product of commuting unitaries: the site factor \(-1\) and the six end factors \(\epsilon_{\ell,x}\) (line 148). Each \(\epsilon_{\ell,x}\) is \(\rho_{\ell,x}(-1)\), so \(\epsilon_{\ell,x}^2=1\) and \(\epsilon_{\ell,x}\) is self-adjoint. Two of the \(z\)'s share at most one link, where they act through commuting end actions. Every gate commutes with \(\mathcal G^{12}_x\), hence with \(z_x\). E1 computes \(\alpha(z_x)\) from the finitely many gates near \(x\), so \(\alpha(z_x)=z_x\). (b) The \(\operatorname{Ad}z_x\), \(x\in S\), are commuting involutive automorphisms. The displayed \(O_T\) are the joint eigencomponents, by the character sum over \((\mathbb Z_2)^S\): \(\operatorname{Ad}z_x(O_T)=-O_T\) for \(x\in T\) and \(O_T\) for \(x\in S\setminus T\). For \(x\notin S\) the site factor of \(z_x\) is a scalar, and its end factors act on links outside the support of \(O\). (c) From (b) and \(z_x^2=1\), \(O_Tz_x=\pm z_xO_T\), with \(-\) exactly for \(x\in T\). So \(O_T(1+s_xz_x)/2=(1\pm s_xz_x)/2\,O_T\). (d) \(\alpha(\Pi^s)=\Pi^s\) by (a). (e) \(\omega'(\Pi^{s\circ T})=\omega(O_T^*\Pi^{s\circ T}O_T)/\omega(O_T^*O_T)=\omega(O_T^*O_T\Pi^s)/\omega(O_T^*O_T)\) by (c). By Cauchy-Schwarz, \(\lvert\omega(Y(1-\Pi^s))\rvert^2\le\omega(YY^*)\,\omega(1-\Pi^s)=0\) for every \(Y\), so the quotient is 1. Then apply (d) to \(\omega'\) and to \(\omega\). ∎

**Corollary SC.1.** A local operator that commutes with every \(\Pi^s\) is tensor class at every site: commuting with \(z_x\) forces \(O_T=0\) for every \(T\ni x\). With one end-pure class on all links, every \(z_x\) is the scalar \(-1\) (line 168), every local operator is tensor class everywhere, and (e) is vacuous.

*Four-test check of the word "moves".* Theorem SC uses "moves" for "the set of sites where the excited and reference states differ in centre class changes with the tick". This is a definition used to state a proved theorem, not a reading of an axiom. (1) It names no part's target. (2) It is closed. (3) It settles nothing by premise; (e) is proved. (4) It adds no structure. It passes all four. The step from Theorem SC to CG1 still needs the pass-1 reading R-CG1, which this report does not adopt.

**Repaired statement for line 166.** "F and K hold as stated. They do not make every fermion-odd operator tensor class when registers are end-mixed: \(\gamma_{y,a}X\) above is spinor class at \(y\). Theorem SC shows that every such operator changes a joint centre sector that the tick conserves. So no spinor-class charge, in the sense of inferred definition 7, moves under any finite-register \(\operatorname{Spin}(10)\)-exact law. LW1-5-16 is therefore answered no for that notion. Whether CG1's '16' needs a different notion of spinor excitation is the reading R-CG1 of `LW1_5O_DRAFT.md` section 5, an owner question."

**Repaired statement for line 294.** "`LW1_5O_DRAFT.md` Theorem P proves conservation of the centre projections. With inferred definition 7, Theorem SC completes its 'static probe' claim: no spinor-class charge moves."

### 3.2 Line 170 (vector class for reducible registers): real

The pass-1 hypothesis is `LW1_5_DRAFT.md` line 231: "every link register is a representation on which `−1 ∈ Spin(20)` acts as one scalar `ε = ±1`". The proof of Lemma Z(ii), line 242, then says the lifts of \(-1_{20}\) "on an irreducible register ... act as scalars". The hypothesis does not give irreducibility. The distiller's example \(S_+\oplus S_-\) is right. The referee adds an explicit counterexample to the parity clause of Lemma Z(iii).

*Counterexample.* Let a link \(\ell=(x,y)\) with both ends in \(\Lambda\) carry \(R=S_+\oplus S_-\), the full Fock space of \(\mathrm{Cl}(20)\). Here \(\rho(-1_{\operatorname{Spin}(20)})=-1\) on both summands, so the register is end-pure and link-pure. The \(x\)-end factor of \(\omega_x\) is \(\prod_j e^{i\pi T_{10+2j-1,10+2j}}=-\eta_{11}\cdots\eta_{20}\), and the \(y\)-end factor of \(\omega_y\) is \(-\eta_1\cdots\eta_{10}\). Their product is \(\eta_1\cdots\eta_{20}=-\Gamma\), which is \(-1\) on \(S_+\) and \(+1\) on \(S_-\). Take a nonzero link operator \(X\) from \(S_+\) to \(S_-\). Then \(\operatorname{Ad}(\prod_{z\in\Lambda}\omega_z)(X)=-X\), though \(X\) is fermion even. Put \(O=\gamma_{x,a}X\). Then \(\operatorname{Ad}(\prod_{z\in\Lambda}\omega_z)(O)=(-\gamma_{x,a})(-X)=O\), though \(O\) is fermion odd. So Lemma Z(ii) fails, and so does the clause "if it is fermion odd, `−1_{10}` acts on it as `−1`" of Lemma Z(iii). \(O\) is still tensor class at every site, as (K4) requires.

*Repaired statement.* "Z(i) holds when every end at the sites concerned is end-pure. Under end-purity every local operator is tensor class at every site (K4). If, in addition, the lift of \(-I_{20}\) acts as a scalar on every link register inside \(\Lambda\), then \(-1_{10}\) at every site of \(\Lambda\) acts as fermion parity on operators supported with all their links in \(\Lambda\), and fermion-odd ones are class 2. The additional hypothesis holds for every irreducible register: the lift is central in \(\operatorname{Spin}(20)\), so Schur's lemma makes it a scalar."

### 3.3 Line 252 (pass-1 number formula): real

`LW1_5_DRAFT.md` line 400 reads: "`ω((N_x − N_y)^2) = 5[G_{xx}(1−G_{yy}) + G_{yy}(1−G_{xx}) + 2|G_{xy}|^2] ≥ 5/2` at half filling". The cross-flavour terms \(\sum_{j\neq k}\omega(d_jd_k)\), with \(d_j=n_{x,j}-n_{y,j}\), equal \(20(G_{xx}-G_{yy})^2\) because the flavours factor. The pass-1 formula omits them, and the distiller's example (25, not 5) is right. At half filling the omitted term vanishes, so the pass-1 copy conclusion stands. The repaired statement is (7.1) at line 250 [check: three random two-site five-flavour quasi-free states; (7.1) matched to six digits, the pass-1 formula did not].

### 3.4 Line 238 (earlier `L5-U` covariance GAP): resolution correct

B1-U (lines 228-236) proves what `VC1_5_DRAFT.md` Lemma C claims for `L5-U` at its lines 80-86. Lemma C(i): the hop goes to \(d_g(gx)d_g(gy)h^U_{g\ell}\) in both orientations; the LW1 A2 sign identity then maps \(H_C\) to \(H_{gC}\); the tilings are preserved; \((m-p-m/2)^2=(p-m/2)^2\) preserves the electric layer. Lemma C(ii): the matter map and the rishon relabelling are as stated. Lemma C(iii): the Gauss generators, \(N_x\), \(Q_x\) and \(p_{\ell,z}\) go to their images. Lemma C(iv): the lifts compose up to site signs. The reversed-orientation step is the adjoint identity \((c^\dagger_{y'}r^{y'}_jr^{x'\dagger}_kc_{x'})^\dagger=c^\dagger_{x'}r^{x'}_kr^{y'\dagger}_jc_{y'}\), which holds with no sign. The GAP stays open only for a separately supplied plaquette layer, as line 238 says.

### 3.5 Line 297 (Lemma X1 probe): real, and no claimed result rests on it

Lemma X1 (`LW1_5U_DRAFT.md` line 179) proves that \(D=\varphi(N_x)-N_x\) commutes with the gate. Pass 1 already records the limits that the GAP names, at line 185: "Lemma X1 gives at most "φ preserves `N_x`", a group of dimension 251 ... Its hypothesis, a trivial even commutant of W in 𝒜_x, is itself a spectral condition at the exceptional angle, and it is not verified." The GAP is accurate. LW1-5-X stays open with the three attacks recorded in `LW1_5_DRAFT.md` lines 449-451 and `LW1_5U_DRAFT.md` lines 185-187. The dimension 251 checks: the even unitaries commuting with \(N_x\) form \(\prod_kU(\binom5k)\), of dimension \(1+25+100+100+25+1=252\), less one for the common phase.

### 3.6 Line 298 (four-test option inventory): a scope note, not a defect

The referee read every row: u1-u8 of `LW1_5U_DRAFT.md` section 8 and c10, c12-c15, R-VC1, R-CG1 of `LW1_5O_DRAFT.md` section 5. Each verdict follows from the reason stated in its row. None is adopted, and `LW1_5.md` uses none as a premise; it uses LW1's own conjugation reading (u1, R-VC1), which is not a new choice. *Repaired statement:* "The four-test rows of `LW1_5U_DRAFT.md` section 8 and `LW1_5O_DRAFT.md` section 5 are interpretive. Each verdict follows from its stated reason. None is adopted or used here as a premise."

### 3.7 Line 299 (Remark D.2): real; closed for the two criteria that the remark uses

Remark D.2 (`LW1_5U_DRAFT.md` line 218) reads: "If the `SU(N)` singlets are removed from `S+`, then under `SU(5)` the content `10 ⊕ 5bar` is anomaly free and protected ... `N = 3` (`3bar`, anomalous) and `N = 4` (`6`, real) fail. So `N = 5` would again be the smallest." It does not treat \(N=1,2\). Of #10014's four criteria it checks two: anomaly freedom and protection from an invariant mass.

*Referee closure.* Remove from \(S_+=\bigoplus_{k\,\mathrm{even}}\Lambda^k\mathbb C^N\) its \(SU(N)\)-invariant summands, \(\Lambda^0\) and, for even \(N\), \(\Lambda^N\). For \(N=1,2\) nothing remains. For \(N=3\) the remainder is \(\Lambda^2\mathbb C^3\), with cubic anomaly \((N-4)p_3=-p_3\neq0\). The expansion \(\sum_{i<j}(x_i+x_j)^3=(N-4)p_3\) for traceless diagonal \(X\) holds for every \(N\); line 218 states its \(N=5\) case, and `LW1_5U_DRAFT.md` line 212 the general one. For \(N=4\) the remainder is \(\Lambda^2\mathbb C^4\), with the symmetric invariant pairing \((\alpha,\beta)\mapsto\alpha\wedge\beta\in\Lambda^4\mathbb C^4\simeq\mathbb C\), so it is massable. For \(N=5\) the remainder is \(\Lambda^2\oplus\Lambda^4\), with cubic anomaly \(p_3-p_3=0\). It has no invariant bilinear: \(\zeta=e^{2\pi i/5}\) acts on \(\Lambda^a\otimes\Lambda^b\) as \(\zeta^{a+b}\), and \(a+b\in\{4,6,8\}\) is never \(0\bmod5\).

*Repaired statement.* "With the \(SU(N)\)-invariant summands removed, \(N=5\) is the smallest \(N\) whose content is nonempty, has zero \(SU(N)\) cubic anomaly and has no \(SU(N)\)-invariant bilinear. #10014's other two criteria (Witten's \(SU(2)\) anomaly and the mod-16 centre criterion) are not checked; `LW1_5U_DRAFT.md` line 220 notes that the second does not apply as written. The content change fails test 4 (row u7) and is recorded, not proposed."

### 3.8 Lines 7, 222, 301 (inherited LW1 GAPs): unchanged

UALL is a counterexample in LW1 (`LW1.md` line 197) and is not used here; the edge factorization at line 283 avoids it. B12(ii) and B12(iii) stay open (`LW1.md` lines 494 and 496). `LW1_5.md` inherits them as stated.

---

## 4. Checks behind the verdicts, section by section

### 4.A Sections 0-2

- *Hashes and quotes.* The recorded SHA-256 values match [check]. The six premise texts at lines 47-62 occur verbatim in `TOE_ASSEMBLY.md` lines 177-182, and the two proposed readings at line 66 occur verbatim in `LW1_5_DRAFT.md` lines 322 and 324 [check: `check_quotes.py`].
- *Inferred definition 2.* The line says "a different number-based cost could select a different coupling". An abstract instance supports it. Take two sites, input configurations \((2,0)\) and \((1,1)\) with probability \(1/2\) each, outputs \((0,2)\) and \((1,1)\) with probability \(1/2\) each, and all four pairs allowed. The site-change cost of the coupling with weight \(t\) on \((2,0)\to(0,2)\) and on \((1,1)\to(1,1)\) is \(2-2t\), so the rule selects \(t=1/2\). The cost \(\sum_x\lvert N_x-N'_x\rvert\) equals 2 for every \(t\), so the entropy step selects \(t=1/4\). Whether `L5-U`'s dynamics realizes such an instance is not shown; the remark does not need it.
- *One-mode `L5-U`.* In the sector \(m=1\), \(\lvert x\rangle=r_x^\dagger\lvert0\rangle\), \(\lvert y\rangle=r_y^\dagger\lvert0\rangle\): \(r_yr_x^\dagger\lvert y\rangle=-\lvert x\rangle\) and \(r_yr_x^\dagger\lvert x\rangle=0\) [check]. With \(E=p_x-1/2\), \(\lvert x\rangle\) has \(E=1/2\), so LW1's \(J=\lvert x\rangle\langle y\rvert\), and the register unitary \(\lvert y\rangle\mapsto-\lvert y\rangle\) sends \(-\lvert x\rangle\langle y\rvert\) to \(J\); it commutes with \(p_x\). On an in-link \(\ell=(w,x)\), \(-E_\ell=p_{\ell,x}-1/2\). So LW1's \(\mathcal G_x=n_x+\sum_{\rm out}E-\sum_{\rm in}E=Q_x-3\), and the conjugations agree.
- *`L5-O` notation.* \(U^{ab}=2T_{a,10+b}=i\eta_a\eta_{10+b}\) fixes \(\eta_a=\eta^y_a\), \(\eta_{10+b}=\eta^x_b\). The Gauss law uses the end generator at \(x\): \(L_x\) if \(x\) is the source of \(\ell\), \(L_y\) if it is the target. Both conventions are implicit (edit R3). On \(S_+\), \(\Gamma=\Gamma^y\Gamma^x\), \((\Gamma^x)^2=1\), so \(\Gamma^x=\Gamma^y\) [check: the \(\mathrm{Cl}(8)\) analogue].

### 4.B Section 3

- *C.* \(\dim G_{\rm full}=256+256-1\). The grading argument shows that a frame maps even site elements to elements commuting with an odd mode elsewhere, hence to even ones. Given item 8's clause, \(\varphi\vert_{\mathcal A_x}=\operatorname{Ad}V\), and \(VPV^*=\lambda P\) with \(\lambda^2=1\) makes \(V\) homogeneous.
- *C2.* The even part of \(\mathrm{Cl}(10)\) has dimension \(2^9=16^2+16^2\), so it equals \(\operatorname{End}(H_+)\oplus\operatorname{End}(H_-)\). For \(U(5)\), the \(n_i\) separate the basis of \(\Lambda^k\), the \(c^\dagger_ic_j\) connect all \(k\)-subsets, and distinct \(k\) have distinct characters \(e^{ik\theta}\).
- *M.* Number conservation gives \(\sum_b\gamma_{x,b}B_b=\sum_j(c^\dagger_{x,j}X_j-c_{x,j}X^\sharp_j)\), so \(B_{2j-1}=(X_j-X^\sharp_j)/2\) and \(B_{2j}=-i(X_j+X^\sharp_j)/2\). This change of basis is invertible. So the ten \(B_b\) are independent exactly when the ten \(X_j,X^\sharp_j\) are, and then the \(X_j\) are. The charge \(-1\) projection is fixed by \(\psi\) because \(\varphi\) fixes \(N_{\mathfrak M}\) and \(\operatorname{Ad}L\) fixes matter.
- *Exceptional angles.* \(a_e\in(0,\pi/2)\) and \(a_o\in(0,\pi)\) on the window, and \((\varepsilon,\mu)\mapsto(a_e,a_o)\) is a linear bijection. So the bad set is finite.

### 4.C Section 4

- *Q and G.* With \(L^{cd}_x=\tfrac i2\eta^x_c\eta^x_d\), \([L^{cd}_x,\eta^x_b]=i(\delta_{db}\eta^x_c-\delta_{cb}\eta^x_d)\) gives the first bracket; the second is the same at the other end. At the source, \(\sum_b\{[L^{cd}_x,U^{ab}]\gamma_{x,b}+U^{ab}[M^{cd}_x,\gamma_{x,b}]\}=i(U^{ac}\gamma_{x,d}-U^{ad}\gamma_{x,c})+i(U^{ad}\gamma_{x,c}-U^{ac}\gamma_{x,d})=0\). At the target the same cancellation runs on the first index.
- *R.* A reflection at \(x\) negates \(\gamma_{x,10}\). On a link with \(x\) as source it needs \(U^{a,10}\mapsto-U^{a,10}\), the twist \(\sigma\); with \(x\) as target it needs the twist \(\sigma'\) of the other end. With \(s\) the end swap and \(\tilde s\) a lift, \(\sigma'=\operatorname{Ad}_s\sigma\operatorname{Ad}_s^{-1}\). If \(Q\) intertwines \(R\) with \(R\circ\sigma\), then \(Q'=\rho(\tilde s)Q\rho(\tilde s)^{-1}\) intertwines \(R\) with \(R\circ\sigma'\), and conversely. This covers both directions of "exactly when" on every cube. On \(S_+\), \(\prod_k2\rho(T_{2k-1,2k})=i^{10}\eta_1\cdots\eta_{20}=\Gamma=1\), and the twist negates exactly one factor.
- *U.* \([\sum c^\dagger Tc,c_k]=-\sum_jT_{kj}c_j\) and \([\sum r^\dagger Tr,r^\dagger_k]=\sum_jT_{jk}r^\dagger_j\), so \(\sum_kr^{x\dagger}_kc_{x,k}\) is invariant; the \(y\)-end is the same.
- *\(SU(2)\) blocks.* \(U^{jk}\) transforms by \(u_y\) on \(j\) and by \(\bar u_x\) on \(k\); for \(SU(2)\), \(\bar{\mathbf2}\simeq\mathbf2\).
- *A.* \(\sum_i\pi_{ki}\bar\pi_{li}=\delta_{kl}\) fixes \(\sum_iO_{x,i}\otimes\lvert i,x\rangle\) and hence each hop term. Under a reversal, the image of \(O_{x,i}O^*_{y,j}\otimes\lvert i,x\rangle\langle j,y\rvert\) is \(O_{y',i}O^*_{x',j}\otimes\lvert i,y'\rangle\langle j,x'\rvert\), the Hermitian-conjugate term at the image link, so no sign arises beyond the site signs \(d_g\).

### 4.D Section 5

- *Centre elements.* \(e^{i\pi(n-1/2)}=-i(-1)^n\), so the site factor of \(\omega_x\) is \((-i)^5P_x=-iP_x\); \(e^{2\pi i(n-1/2)}=-1\). The five Cartan factors of \(\omega_x^2\) each implement the same central \(-1\), so \(\omega_x^2=z_x^5=z_x\).
- *Mixed register.* On \(S_+\oplus\mathbb C^{20}\), \(\epsilon=(-1)\oplus(+1)\) at both ends, so \(X=\lvert v\rangle\langle s\rvert\) is negated by both \(\operatorname{Ad}\epsilon\)'s.
- *One-ended register.* On \(V\oplus\mathbb C\) with \(L^{cd}=i(E_{cd}-E_{dc})\oplus0\), \([L^{cd},A_a]=i(\delta_{da}A_c-\delta_{ca}A_d)\), the same law as \([M^{cd},\gamma_a]\). So \(U^{ab}\) obeys both Q brackets. \(\epsilon_{\ell,x}=-1\) on all of \(R\); \(\epsilon_{\ell,y}\) is \(+1\) on \(V\oplus\mathbb C\) and \(-1\) on \(H^y\). On \(R\oplus R^{\rm swap}\) with tensor \(U^{ab}\oplus(-U^{ba})\), the summand swap \(S\) gives \(S(U^{ab}\oplus-U^{ba})S^{-1}=(-U^{ba})\oplus U^{ab}\), which is \(-\) the total tensor with indices exchanged, and it exchanges the end actions.
- *Singlet criterion.* The classes \(3,1,2,0\) come from \(\omega_x\)'s site factor \(-iP_x\) and from \(-1_{10}\) on \(V\). The reduction terminates: vector-spinor pairs first, then opposite spinors and vector pairs, then identical spinors in fours. The charge conjugation \(C\gamma_aC^{-1}=\gamma_a^T\) gives \(CM^{ab}C^{-1}=-(M^{ab})^T\) and \(P^TC=-CP\), from \((-1)^{45}=-1\).
- *Reversals.* For \(x_2\equiv x_3\): \(y\mapsto(1-y_1+2x_1,\,y_3+x_2-x_3,\,y_2+x_3-x_2)\) sends \(x\) to \(x+e_1\) and back, with an even translation and \(\det Q=1\). For \(x_2\not\equiv x_3\): \(y\mapsto(1-y_1+2x_1,\,x_2+x_3-y_3,\,x_2+x_3-y_2)\) does the same. The quarter turn \((y_1,y_2,y_3)\mapsto(y_1,1-y_3,y_2)\) cycles \((x_2,x_3)\bmod2\) through all four classes.
- *S5 and H.* With one end-pure class, every interior \(z_x\) is \(-1\) on the region space, so each irreducible factor is nontrivial at each interior site, and \(\operatorname{Spin}(10)\) has no nontrivial character. For H, invariance at one site suffices: the Haar average of the adjoint action on \(\operatorname{span}\{M^{ab}_x\}\) projects onto the centre of \(\mathfrak{so}(10)\), which is zero.

### 4.E Section 6

- *Pure invariance.* A vector state of a full matrix algebra fixes its vector up to a phase, so the vector carries a continuous character of \(U(5)_x\). Its restriction to \(SU(5)\) is trivial (a connected perfect group), and its restriction to the centre makes the vector a \(Q_x\)-eigenvector. \(\zeta\in SU(5)\) then forces the eigenvalue into \(5\mathbb Z\).
- *Σ-U table.* \(n_m+3m\equiv0\pmod5\) gives \(2,4,1,3,\{0,5\},2,4,1,3\) for \(m=1,\ldots,9\). Each site has end numbers \(\alpha,\alpha,\alpha,m-\alpha,m-\alpha,m-\alpha\), total \(3m\). Local factors have definite parity, so the translation maps the product vector to \(\pm\) itself.
- *Z-U.* Rishon pairs on a supported link contribute the constant \(m\) to \(\sum Q_x\), so the commutator is that of \(N_\Lambda\). \(\Lambda^3(V^*)\simeq\Lambda^2V\otimes\det^{-1}\) is the \(\mathbf{10}\) of \(SU(5)\).
- *H-U and F-U.* \(\omega(N_x)=5/(e^t+1)\) for the Gibbs product with traced links; empty and full matter give 0 and 5. Applying \(\omega\) to (6.1) gives \(qV=\bar nV+3mV\).
- *LW1-5U-PS7.* Per cell, \(\sum q_x=20+24m\in5\mathbb Z\) forces \(5\mid m\). For two tiling classes, \(q=5/2+3(m+m')/2\in5\mathbb Z\) forces \(m+m'\equiv5\pmod{10}\).
- *D.* \(-c+10(2-c)+5(4-c)=40-16c\); \((3/2)(2-c)+(1/2)(4-c)=5-2c\); at \(c=5/2\), \(-125/8-10/8+135/8=0\). \(\sum_{k\,\mathrm{even}}k\binom Nk=N2^{N-2}\) for \(N\ge2\), because \(\sum_k(-1)^kk\binom Nk=0\) there. \(\sum_{i<j}(x_i+x_j)^2=(N-2)p_2=3p_2\) at \(N=5\).

### 4.F Section 7

- *Free hops.* \(\tfrac i2\sum_a\gamma_{y,a}\gamma_{x,a}=i\sum_j(c^\dagger_{y,j}c_{x,j}-c^\dagger_{x,j}c_{y,j})\) by direct expansion. \((WR_TW^*)_{yx}=i\eta_i(x)\) and \((WR_TW^*)_{xy}=-i\eta_i(x)\). A lift \(D_gP_g\) of \(V\) conjugates to \(WD_g(P_gW^*P_g^{-1})P_g\), a diagonal phase times \(P_g\).
- *Dressed `L5-O`.* The swap \(\eta_a\leftrightarrow\eta_{10+a}\) is ten transpositions, so it lies in \(SO(20)\). It sends \(U^{ab}\) to \(i\eta^x_a\eta^y_b=-U^{ba}\). Reversing the matter order gives the second sign, so \(h_\ell\mapsto d_g(gx)d_g(gy)h_{g\ell}\) in both orientations.
- *B8-5.* Per flavour, \(\omega((1-2n_x)(1-2n_y))=(1-2G_{xx})(1-2G_{yy})-4\lvert G_{xy}\rvert^2\). Both formulas matched a direct computation on two five-flavour sites [check].
- *B8b-5.* On empty matter \(\gamma_{x,2j-1}\) and \(\gamma_{x,2j}\) act as \(c^\dagger_{x,j}\) and \(ic^\dagger_{x,j}\), so \(h_\ell\) acts as \(-\tfrac i2\sum_{j,k}c^\dagger_{x,j}c^\dagger_{y,k}\otimes\mathcal U^{++}_{kj}\) with \(\mathcal U^{++}_{kj}=U^{2k-1,2j-1}+iU^{2k-1,2j}+iU^{2k,2j-1}-U^{2k,2j}\). Each \(\mathcal U^{++}_{kj}\) lowers the grading element \(Q=\sum_k(T_{2k-1,2k}+T_{10+2k-1,10+2k})\) by 2 in every representation, so a lowest-weight vector lies in \(K_\ell\).
- *B11-5 and E2b-5.* Hadamard's inequality bounds \(\det G_A\) and \(\det(1-G)_{F\setminus A}\) by \(2^{-\lvert A\rvert}\) and \(2^{-\lvert F\setminus A\rvert}\). The Cesàro limits keep gauge and cell invariance because the tick commutes with both (G, U, B1-5, B1-U).

### 4.G Section 7.1

- *B6.* \(P_AW(1-P_{N(A)})=\sum_{\zeta\in A,\xi\notin N(A)}P_\zeta WP_\xi=0\), and \(\lVert P_AW\rVert\le1\).
- *Edge factorization.* The span of the \(\operatorname{Ad}_hX_j\) contains the generators and is \(\operatorname{ad}X_j\)-invariant, so it contains the generated Lie algebra. The reverse inclusion holds because \(\operatorname{Ad}_h\), \(h\in H\subseteq L\), preserves that Lie algebra; line 283 leaves this implicit. `LW1.md` line 188 states both inclusions.
- *E6.* Dyadic subadditivity gives a non-increasing sequence \(H(Q_m)/\lvert Q_m\rvert\). Mixing two measures changes block entropy by at most \(\log2\), so the limit is affine. An upper semicontinuous function attains its maximum on a compact face.
- *Free sea.* \(W_{2b+r}=i^{2(b_1+b_2+b_3)}i^{r_1+r_2+r_3}\), and \((-1)^{b_1+b_2+b_3}=e^{i(\pi,\pi,\pi)\cdot b}\) shifts cell momentum. LW1 C1 places the massless node at \(K=0\) (`LW1.md` line 361), so the `L5-O` node sits at \((\pi,\pi,\pi)\).
- *Witness.* The output state \(\tfrac12(\lvert000\rangle\langle000\rvert+\lvert111\rangle\langle111\rvert)_{xyz}\) is even, gives zero disagreement for both pairs and both alphabets, and \(\omega_0=\rho\circ\alpha^{-1}\) is a state with tick-one image \(\rho\).
- *Subgroup singlet.* Direct CAR expansion gives \(M^{13}+M^{24}=i(c_1^\dagger c_2-c_2^\dagger c_1)\) and \(M^{14}-M^{23}=c_1^\dagger c_2+c_2^\dagger c_1\). So \(J_2=i(A-A^\dagger)/2\), \(J_3=(A+A^\dagger)/2\), and the brackets close [check: four-dimensional Jordan-Wigner matrices; the pass-1 assignment \(J_2=(A+A^\dagger)/2\) fails]. \(e^{2\pi iJ_1}=(-1)^{n_1+n_2}\) on the site is not a scalar, so the order-two central element of this \(SU(2)\) is not \(-1\in\operatorname{Spin}(10)\).

### 4.H Section 8

The open list at lines 309-317 matches line 9 and the open items of the three drafts. Lines 305 and 319 claim nothing beyond the sections above.

---

## 5. Required edits

Required for freeze: R1, R2, R6, R7, R8, R9, R10, R11, R13. Optional, for clarity: R3, R4, R5, R12, R14, R15. No edit changes a theorem's content.

- **R1 (line 27).** After "fixes the algebra of every other site and every link pointwise", add "and maps the algebra of its site onto itself (B5B Definition F)".
- **R2 (line 33).** Replace inferred definition 1 by the text of section 2.1, item 11.
- **R3 (lines 74-77 or 117).** State the conventions \(\eta_a=\eta^y_a\), \(\eta_{10+b}=\eta^x_b\), and \(L^{cd}_{\ell,z}=L^{cd}_x\) if \(z\) is the source of \(\ell\), \(L^{cd}_y\) if it is the target.
- **R4 (line 109).** After "with independent \(X_j\)", add: "the \(B_b\) and the pairs \((X_j,X^\sharp_j)\) are related by an invertible change of basis".
- **R5 (line 128).** Add: "On a link with \(x\) as target the needed twist is \(\sigma'=\operatorname{Ad}_s\sigma\operatorname{Ad}_s^{-1}\), and \(\rho(\tilde s)Q\rho(\tilde s)^{-1}\) intertwines \(R\) with \(R\circ\sigma'\)."
- **R6 (line 138).** Insert the referee closure of section 2.2, item 41, or an equivalent proof.
- **R7 (lines 154 and 172).** Replace "The hop and electric gate conserve" by "The hop, and any electric gate whose generator commutes with both end actions, conserve". Note at line 79 that \(W_E\) is defined for \(S_+\) only, and that \(i^5\rho(\eta^x_1\cdots\eta^x_{10})\) is anti-Hermitian on a vector summand.
- **R8 (line 166).** Replace the GAP by the repaired statement of section 3.1, with Theorem SC and Corollary SC.1 stated in §5 or §7.1.
- **R9 (line 170).** Add the counterexample and the repaired Z(ii)-(iii) statement of section 3.2.
- **R10 (line 294).** Change "Proposition P" to "Theorem P". Replace the GAP by the repaired statement of section 3.1.
- **R11 (line 299).** Replace the GAP by the repaired statement of section 3.7.
- **R12 (line 298).** Replace the GAP label by the repaired statement of section 3.6.
- **R13 (lines 7, 9, 312).** Update the gaps paragraph and the open list. Restate the LW1-5-16 entry: "LW1-5-16: answered no for spinor class defined by the local centre (Theorem SC). Open only as the owner reading R-CG1: which notion of '16' CG1 needs."
- **R14 (line 283).** Add the inclusion "\(\operatorname{Ad}_h\), \(h\in H\subseteq L\), preserves the Lie algebra", as in `LW1.md` line 188.
- **R15 (line 34).** Optionally add the abstract instance of section 4.A.

## 6. Open statements to carry by name

These are `LW1_5.md`'s own open items. This report adds no new open statement; it widens the scope of GA1-P-5 by one specification (R7).

- **LW1-5-X.** Exceptional cube-gate frames at the finitely many parameter points where both angles are exceptional. Three attacks recorded in pass 1: `LW1_5_DRAFT.md` lines 449-451 (Lemma T route, charge projection, gate commutant) and `LW1_5U_DRAFT.md` lines 185-187 (charge commutant, probe products, spectral).
- **LW1-5-T.** Site frames commuting with the whole update. Three attacks recorded: `LW1_5_DRAFT.md` lines 454-456.
- **LW1-5-Σ.** Whether VC1 needs a pure Gauss singlet, and which sector supplies it (owner and VC1).
- **LW1-5-BG.** The long-distance effect of the fixed centre background and the absent flux-free link state. Three attacks recorded: `LW1_5O_DRAFT.md` lines 284-286. It waits on GA1-P-5.
- **LW1-5U-PS7.** The meaning and existence of a half-filled interacting vacuum under `L5-U` (owner-level reading).
- **LW1-5U-Σc.** Point-group symmetry and stationarity of the pure finite-box construction. `VC1_5_DRAFT.md` claims more; that claim lies outside this check.
- **GA1-P-5.** A covariant gauge-invariant plaquette gate class for each register family. The electric layer on reducible registers (R7) needs a specification too.
- **LW1-U_f, LW1-U_sea, LW1-N** on the parity and number alphabets.
- **The transport cost reading** (inferred definition 2) and **the formation domain** (LW1-R, TM1-i), as at line 9.
- **LW1-5-16, restated.** No longer an open mathematical statement for spinor class defined by the local centre (Theorem SC). It remains as the owner reading R-CG1.
- **LW1-5-RQ.** Owner decision on file: both laws live (`TOE_ASSEMBLY.md` section 3.5).
- **Inherited from LW1.** B12(ii) and B12(iii) (open); UALL (a counterexample in LW1, not used).

## 7. Freeze recommendation

`LW1_5.md` is fit to freeze after the required edits of section 5. Its theorems stand as stated. The two ERROR items are a reading slip in an inferred definition and a GAP that misnames its source and understates what the centre argument proves. The four INCOMPLETE items each have a closure in this report. Theorem SC belongs in the frozen text, because it answers LW1-5-16 for spinor class defined by the local centre and replaces two GAP labels.

---

## FINISH

**Proved here (referee closures; this report is itself unrefereed).**
- Theorem SC and Corollary SC.1 (section 3.1). Under any finite-register \(\operatorname{Spin}(10)\)-exact law, every local operator splits into parts that are spinor class on fixed site sets. Each part shifts the joint centre sector exactly on its set. The joint law of all centre classes is the same at every tick, for every state. So no spinor-class charge moves, and within one centre sector every local operator is tensor class.
- The S′ closure (section 2.2, item 41): \(S_+\) is faithful, the centre of \(\operatorname{Spin}(10)\) is \(\{\pm1,\pm\omega\}\), \(f\) is injective, and \(f\) is not Bogoliubov. Simplicity of \(\mathfrak{so}(10)\) is rebuilt there.
- The repaired Lemma Z(ii)-(iii) (section 3.2). The parity identification holds when the lift of \(-I_{20}\) is a scalar on every link inside the region, in particular for irreducible registers.
- The electric-gate lemma (section 2.2, item 45): each \(\epsilon_{\ell,x}\) commutes with every operator that commutes with the end actions.
- The repaired Remark D.2 (section 3.7), for the cubic-anomaly and invariant-bilinear criteria.
- Inferred definition 1 corrected (section 2.1): PS-3g, read plainly, with C2 gives the alphabets of PS-3h5.
- One-line closures: independence of the \(X_j\) in M; the target-end twist in R; the second inclusion in the edge factorization.
- Re-derivation by hand of the 93 items marked CORRECT.

**Counterexamples.**
- To `LW1_5_DRAFT.md` Lemma Z(ii), and to the clause of Z(iii) that fermion-odd operators are negated by \(-1_{10}\), on end-pure reducible registers: \(R=S_+\oplus S_-\), \(X\) from \(S_+\) to \(S_-\), \(O=\gamma_{x,a}X\) (section 3.2).
- To unitarity of the electric gate formula of `LW1_5_DRAFT.md` section 8.1 on \(S_+\oplus\mathbb C^{20}\), which `LW1_5O_DRAFT.md` Proposition S4 uses: \(i^5\rho(\eta^x_1\cdots\eta^x_{10})\) is anti-Hermitian on the vector summand (section 2.2, item 45).
- To the GAP at line 294 as stated: Theorem SC gives the claim it calls unsupported.
- Confirmed here, as found by the distiller: the pass-1 number-copy formula fails for unequal diagonals (25, not 5); the pass-1 \(J_2\) expansion is \(J_3\)'s; the two free walks differ by the phase \(W\), so `LW1_5_DRAFT.md` line 318's "Its free tick is the same as `L5-O`'s" is false as written.

**Open, by name.** LW1-5-X and LW1-5-T (three attacks each, recorded in pass 1); LW1-5-Σ; LW1-5-BG (three attacks recorded in pass 1; waits on GA1-P-5); LW1-5U-PS7; LW1-5U-Σc; GA1-P-5, now also for an electric layer on reducible registers; LW1-U_f, LW1-U_sea and LW1-N on the new alphabets; the transport cost reading and the formation domain; the owner reading R-CG1, to which LW1-5-16 reduces; LW1-5-RQ (owner, both live); B12(ii) and B12(iii), inherited from LW1.

**What changes downstream.**
- CG1 and MT1-ii: on `L5-O`, for every finite register choice, a spinor-class charge never moves. A moving 16 would need a notion of "16" beyond the local centre class (the owner reading R-CG1), or a law beyond `L5-O`, such as one that keeps \(f(\operatorname{Spin}(10))\) of S′. This report proposes neither.
- LW1-5-16 leaves the list of open mathematical statements and stays only as an owner reading.
- VC1: the joint law of the centre classes is a constant of the motion for every state. With reducible registers, \(\omega_0\) fixes the sector pattern for all time.
- PS-3h5: its alphabets follow from PS-3g and C2. Both remain proposals.
- GA1-P-5: an electric layer on reducible registers needs its own specification.
- No change to the `L5-U` results of section 6, to the carry-over results of section 7, or to B1-U's check of `VC1_5_DRAFT.md` Lemma C.
