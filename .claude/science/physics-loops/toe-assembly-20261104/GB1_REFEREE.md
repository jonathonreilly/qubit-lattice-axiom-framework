lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1 referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 under PR #10138's method. Claude drafted GB1 (`GB1_DRAFT.md`). Codex gpt-6.1-terra distilled it (`GB1.md`). This session wrote neither. This is one check: one line-by-line read of `GB1.md`. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status, adopts no law, reading or definition, and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. A `[check]` is a tiny scratch computation in `/tmp/toe-GB1ref/` (under a minute, a few MB). It guides and never proves.

**Text read.** `GB1.md` at commit `d6d2136f2` (the last commit that touches it; branch head when read). SHA-256 of the file read: `bb7bd34d9859759c0e353fc9d4e8f65532a167269eefbaedc38a431bd5324310`. It has 144 lines. Line numbers below refer to that file.

**Sources read, with commits.** All in this checkout at `d6d2136f2` unless marked. `GB1_DRAFT.md` (pass 1, commit `7f4e4dc37`, SHA-256 `370a6c67…31bb6bb`, the hash `GB1.md` line 13 records); `prior/GB1.md` (all); `TOE_ASSEMBLY.md` section headings, lines 83-84, 183, 203-205, 212-220, 233-236 and 246-252 (PS-5, PS-6r, sections 3.4-3.9; NN-a at 235, ZM1-INV at 252), and 433-443 (GB1); `LW1_REFEREE.md` lines 1-80 (format only); `Y2W_DRAFT.md` lines 1-12 (format only). Further sources are listed in the next paragraph, with the lines read.

**Working-set entries used.** PS-1 (read by PS-1c, cell covariance), PS-5 (fallback text, `TOE_ASSEMBLY.md` 3.4), PS-6 and PS-6r (link registers), NN-a (3.7), ZM1-INV with R-form (3.9). The owner guidance is applied: the working set is read plainly, and where a rung needs a reading it is stated as a candidate and four-tested, never adopted.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step.

**References consulted, with lines.** In this folder at `d6d2136f2`: `LW1.md` 36-75 (definitions, `L_cube`) and 146-180 (law statement) in full, and the labelled lines of 186-255 (A1, dressed factorization at 196 and 205, A2, B3, B4, gauged covariance at 245-247); `GA1_5.md` 7 (Amendment 1), 44-90 (definitions, GA1-P-5, Theorems 2.1, 2.2, 3.1), 236-272 (Lemma U, Proposition C); `GA2_Y2.md` 37-73 (Theorem 2.1 to Theorem 2.5, Corollary Y2-0 and its Scope), 118 (Theorem 4.2), 159-160 (§5 rows (a1), (a2)); `LW1_5.md` 34-107 (definitions, both laws), 149 (subgroups, Proposition T, found by grep in §4), 268-272 (B1-U); `ZM1.md` 56 ((Z-a)); `ZM1INV.md` 1-19 (status, the R-form setting); `LIT_QLM.md` 3, 15. On `origin/claude/ym4d-hard-route` at `fda786822` (fetched with `git fetch -q`, read with `git show`): `library/t0-tree.md` 13-15, 36; `library/port/p8-positivity.md` 31-49; `library/sa-index/ca-full/README.md` 1-8 and `index.tsv` (grep: no row for `3.1:thm-main`, as pass 1 reported). The seven context hashes on `GB1.md` line 13 equal, in order, the SHA-256 of `TOE_ASSEMBLY.md`, `prior/GB1.md`, `GA2_Y2.md`, `LW1_5.md`, `GA1_5.md`, `ZM1I1A.md` and `LW1.md` at `d6d2136f2` [check: `shasum -a 256`]. So the distiller's context has not changed since pass 2.

**Counts.** 57 items: 53 CORRECT, 0 ERROR, 4 INCOMPLETE (items 1, 13, 39, 49). Of the distiller's GAPs, SU2-B is closed here by a referee closure. The working-set GAP is closed for five-mode test laws and, at \(S=1/2\), inside \(L5\)-U\([m]\) for odd \(m\); the \(\mathbb Z_2\) rung inside the named laws stays open. The hand-off GAP stands. No item changes a theorem of `GB1.md`.

---

## 1. Verdict table, part A: status, definitions and the time step (GB1 lines 1-59)

| # | Item (GB1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved below" list (5) | INCOMPLETE | Theorem 6.2 (SU2-O, limited) is proved below but missing from the list. Edit E1. |
| 2 | GAP working-set bridge (7) | CORRECT | Gap real. Settled in §4 below: closed for five-mode rung test laws and, at `S=1/2`, inside `L5-U[m]` for odd `m`; open by name for `Z_2` inside the named laws. |
| 3 | GAP SU2-B and GAP hand-off (9) | CORRECT | Both gaps real. SU2-B is closed by the referee closure in §4.3. The hand-off gap stands: CA-I's text is not in the repository; the branch index has no row for `3.1:thm-main`. |
| 4 | §0 Open by name (11) | CORRECT | Add the names of §6 (edit E12). |
| 5 | §0 Provenance (13) | CORRECT | Draft hash and the seven context hashes checked (see head). |
| 6 | Def 1, readout and uniform exponential locality (19) | CORRECT | Matches the owner text "with support-radius-dependent constants" (`TOE_ASSEMBLY.md` 252) and `ZM1INV.md` line 19 ("constants allowed to depend on its support radius"). |
| 7 | Def 2, algebra and sector level (20) | CORRECT | |
| 8 | Def 3, tilings, signs, cell group, `Ad` (21) | CORRECT | Same conventions as `LW1.md` §1, including \(\alpha(A)=U^*AU\). |
| 9 | Def 4, one-mode sites, R-NN1 (22) | CORRECT | |
| 10 | Def 5, the general tick and the cube-face layer (23) | CORRECT | Each link lies in exactly one tiling cube (`GA1_5.md` Theorem 2.1). A plaquette in the \((i,j)\) plane with base \(x\) is an even (odd) cube face iff \(x_i,x_j\) are both even (odd); that is half the plaquettes of each plane. |
| 11 | Def 6, \(L_{\mathbb Z_2}\) (24-31) | CORRECT | |
| 12 | Def 7, \(L^{cf}_{\rm cube}[S]\) (32) | CORRECT | |
| 13 | Def 8, \(L5\)-U\([m]\), block, \(\mathcal S_J\) (33) | INCOMPLETE | \(\mathfrak B_2\) must be the *unital* C*-algebra so generated; the inclusion of item 42 is called unital. A suitable \(J\) exists for every \(m\): \(m=1,2\): \(k=0\); \(3\): \(k\in\{0,1\}\); \(4\): \(1\); \(5\): \(1,2\); \(6\): \(2\); \(7\): \(2,3\); \(8,9\): \(3\). Edit E2. |
| 14 | Theorem 2.1 (F1-F2), statement (37) | CORRECT | `H` commutes with \(U=e^{-iH}\), hence with each spectral projection \(P_k\) (a polynomial in \(U\)); so the draft's hypothesis \(HP_k=P_kH\) is redundant, as the distiller saw. \(T_H^{\,i}=e^{-iH}=U\). |
| 15 | Proof of 2.1 (39) | CORRECT | Example re-derived: \(\langle e_1,\sigma_xe^{-tH_j}\sigma_xe_1\rangle=e^{-t(\theta+2\pi j)}\). |
| 16 | Remark after 2.1 (41) | CORRECT | Example re-derived (\(U^2\) eigenvalues \(1\) and \(e^{-2i\tau_E}\)). The sentence "Self-adjointness is only a necessary condition for a literal self-adjoint unitary transfer" is circular. Edit E3. |
| 17 | Theorem 2.2 (F3, F3′), statement (43-47) | CORRECT | Cube gates of one tiling have disjoint sites and links; all cube-face gates have disjoint links. The two-factor bound is the one used. |
| 18 | Proof of 2.2 (49) | CORRECT | Duhamel: \(X(1)-Y(1)=\int_0^1Y(1-r)(e^{rA}Be^{-rA}-B)X(r)\,dr\), middle factor at most \(r\|[A,B]\|\). |
| 19 | Theorem 2.3 (F4), statement (51-55) | CORRECT | `[check]` below. |
| 20 | Proof of 2.3 (57) | CORRECT | Re-derived: the gauge-fixing map is a bijection onto (new \(\sigma\), \(s\), old \(\tau_x(t)\), \(t\le N_t-2\)); \(A\cosh h^*=e^{\beta_t}\), \(A\sinh h^*=e^{-\beta_t}\) give \(\tanh h^*=e^{-2\beta_t}\), \(A^2=2\sinh2\beta_t\); \(\sum_sG_s=2^{|V|}P_0\); \(P_0\) commutes with \(D\), so cyclicity gives \(T^{N_t}\). |
| 21 | Check report, GB1-FORM, E-1 to E-4 (59) | CORRECT | See the GB1-FORM decision in §4.1. |

`[check]` F4 (`/tmp/toe-GB1ref/check_f4.py`, under a second, a few MB, run after `memory_pressure` showed 58% free): brute-force sums agree with \(2^{|V|N_t}\operatorname{Tr}(P_0T^{N_t})\) to relative \(10^{-13}\) on a square at \(N_t=2\), \((\beta_s,\beta_t)=(0.37,0.81)\), and on a triangle at \(N_t=3\), \((-0.52,0.44)\). It guides only.

## 2. Verdict table, part B: `Z_2`, the obstruction and `U(1)` (GB1 lines 61-109)

| # | Item (GB1 line) | Verdict | Note |
|---|---|---|---|
| 22 | Theorem 3.1 (U1), statement (63) | CORRECT | |
| 23 | Proof of 3.1 (65) | CORRECT | Re-derived: \([\gamma_x\gamma_y,\gamma_y\gamma_z]=2\gamma_x\gamma_z\), so \([iAT,iBT']=-2i(A\otimes B\otimes S)\); \(S^2=1\) and \(S\) commutes with link operators, so \([i(M\otimes S),i(M'\otimes S)]=-[M,M']\). Steps 3-4 of `GA1_5.md` Lemma U use only link-only brackets and the word theorem; they carry over unchanged. |
| 24 | Check report and scheduling remark (67) | CORRECT | |
| 25 | Theorem 3.2 (Z2-A, Z2-F, Z2-B), statement (69) | CORRECT | "Generator-level" frames agree with the repository's gate-wise notion (`LW1_5.md` distiller definition 5: "'Exact frame group' below means gate-wise at a site"). |
| 26 | Proof of 3.2 (71) | CORRECT | Re-derived: \(G_x\) flips \(c_x\) and \(Z_\ell\) together; \(Z_p\) meets each corner twice. Frames: \(\operatorname{Ad}L\varphi(h_\ell)=Z'\otimes(uc_y^*c_x+\bar uc_x^*c_y)\); independence of \(c_y^*c_x,c_x^*c_y\) in the tensor product gives \(uZ'=Z_\ell=\bar uZ'\), so \(u=\pm1\); the case \(vc_x^*\) gives \(vc_y^*c_x^*+\bar vc_xc_y\), independent of both. The six single-link electric layers are needed because NN-a's edge triples include the endpoint sites. |
| 27 | Theorem 3.3 (Z2-C, Z2-D), statement (73) | CORRECT | |
| 28 | Proof of 3.3 (75) | CORRECT | Re-derived: \(\operatorname{tr}(\rho N_\Lambda)=0\) forces \(\rho=|0_\Lambda\rangle\langle0_\Lambda|\otimes\rho_L\); odd cube gates and other even cube gates commute with \(X_\ell\); \(f'(0)=i[H_C,X_\ell]=-\tfrac{2\eta}{\sqrt3}Y_\ell\otimes(c_y^*c_x+c_x^*c_y)\ne0\). The window gives \(a_e\in(0,\pi/2)\). |
| 29 | Prior-work paragraph (77) | CORRECT | `GA2_Y2.md` Theorem 2.3 checked. |
| 30 | Theorem 4.1 (R), statement (81) | CORRECT | |
| 31 | Proof of 4.1 and the trace count (83) | CORRECT | Re-derived in full. \(X_{ij}=\sum_ke_{ki}Xe_{jk}\in\mathfrak B'\cap\mathfrak A\), \(\sum e_{ij}X_{ij}=X\); \(E\) is unital, positive, and fixes \(\mathfrak B\). With \(R=X-b_h\), \(-\delta\le R\le\delta\) gives \(\|E(R)\|\le\delta\) and \(\|X-E(X)\|\le2\delta\). Count: \(\sum_kQ_{j_k}\le E(1)=1\) and \(\operatorname{Tr}Q\ge\|Q\|\) for \(Q\ge0\) give \(N(1-2\delta)\le D\). Orthogonal positive norm-one elements: their finite sums have norm one, and an injective *-homomorphism is isometric. |
| 32 | Corollary 4.2 (R1), statement (85) | CORRECT | Under Def 1's uniform quantifier, which is the owner's text. Under an element-dependent locality R1 does not follow: each \(\Phi(Q_\pi)\) could then use its own radius. GB1 says so at line 19. |
| 33 | Proof of 4.2 (87) | CORRECT | For infinite compact \(G\), \(L^2(G)\) is infinite-dimensional and each isotypic block finite-dimensional, so there are infinitely many blocks. Each block projection is convolution by \(d_\pi\overline{\chi_\pi}\) and commutes with left and right translations, hence with every gauge transformation; it is supported on one link. A finite region of a finite-register law has a full matrix algebra. |
| 34 | Scope paragraph (89) | CORRECT | \(C^*(e^{i\theta E})\cong C(S^1)\) for irrational \(\theta/2\pi\); bumps with disjoint supports supply the elements. |
| 35 | Theorem 5.1 (U1-QL), statement (93) | CORRECT | |
| 36 | Proof of 5.1 (95) | CORRECT | Rotations about \(c_0\) send odd-cube centres \(c_0+\mathbf1+2b\) to \(c_0+(\pm1,\pm1,\pm1)+2b'\), again odd centres; so both tilings are preserved. \(i[H_C,E_\ell]=\tfrac{i\eta}{\sqrt3}(-c_y^*J_\ell c_x+c_x^*J_\ell^*c_y)\ne0\). |
| 37 | Cube-face remark, GB1-CF (97) | CORRECT | The geometric half of `GA1_5.md` Theorem 2.2 is register-free, so it applies to `L_cube`. |
| 38 | Theorem 5.2 (U1-LS), statement (99-103) | CORRECT | The display is a valid, slightly loose bound: the proof gives \((M+nK)^2\) where the display has \((M+(n+1)K)^2\). |
| 39 | Proof of 5.2 (105) | INCOMPLETE | All steps re-derived. One step is too terse: the truncated series \(T_C\) of a gate has norm up to \(e^{16\tau}\), so the leak bound \(N_Ct_K\) cannot come from telescoping truncated series. Referee closure: with \(P_C,Q_C\) the flux projections of cube \(C\) at cutoffs \(M'\) and \(M'+K\), \(g_CP_C=A_C+D_C\), \(A_C=Q_Cg_CP_C\), \(D_C=(1-Q_C)R_CP_C\), \(\|D_C\|\le t_K\). Factors on different cubes act on disjoint links and commute; \(\|A_C+D_C\|\le1\), \(\|A_C\|\le1\). Telescoping gives \(\|\prod_C g_CP_C-\prod_CA_C\|\le N_Ct_K\), and \(\prod_CA_C\) has range in the cutoff \(M'+K\). Edit E4. |
| 40 | Cutoff remark (107) | CORRECT | The norm-one defect is in the paragraph after `GA2_Y2.md` Corollary 2.2 (a referee closure), stated for the link operator. For one gate it gives a defect of order \(\tau\) uniformly in \(S\) at small \(\tau\). Edit E5 (citation). |
| 41 | D-theory count (109) | CORRECT | `LIT_QLM.md` line 15: "Reducing the repo's three spatial directions plus time by one direction would leave three Euclidean dimensions." D-theory's reduced direction is the quantum-link model's own Euclidean time, so a four-dimensional target needs a four-dimensional spatial lattice. A count for that route only. |

## 3. Verdict table, part C: `SU(2)`, `GB1-H` and readings (GB1 lines 111-144)

| # | Item (GB1 line) | Verdict | Note |
|---|---|---|---|
| 42 | Theorem 6.1 (S, SU2-C), statement (113-115) | CORRECT | With \(\mathfrak B_2\) unital (item 13). On \(\mathcal S_J\), \(p_{\ell,x}=N^{\mathsf B}_{\ell,x}+k\), so \((p_{\ell,x}-m/2)^2=(N^{\mathsf B}_{\ell,x}-m'/2)^2\). |
| 43 | Proof of 6.1 (117) | CORRECT | Re-derived. In a plaquette trace the arrival-end index of each link is annihilated and the departure-end index created, also for backward traversal: \((U^\dagger)^{jk}=r^x_jr^{y\dagger}_k\). So a corner index is removed from one link end at the corner and added to the other. Since \(r_j=r_jn_j\), \(r^\dagger_j=r^\dagger_j(1-n_j)\), and the other factors commute with \(n_j\), the monomial kills empty-empty and full-full corners. The `B1-U` lifts map each rishon mode to the same flavour, so they preserve \(\mathfrak B_2\) and each \(\mathcal S_J\). |
| 44 | Paragraph on Theorem U and Proposition T (119) | CORRECT | `LW1_5.md` line 149 checked. |
| 45 | GAP SU2-B (121) | CORRECT | Gap real in the draft's proof. Closed by the referee closure of §4.3: Proposition SU2-B holds as the draft states it. |
| 46 | Theorem 6.2 (SU2-O, limited), statement (123) | CORRECT | |
| 47 | Proof of 6.2 (125) | CORRECT | \((i\eta_a\eta_b)^2=\eta_a\eta_a\eta_b\eta_b=1\) for distinct Majoranas. The identity is in the *proof* of `GA2_Y2.md` Theorem 2.5 ("\(U^{ca}U^{cb}=\eta^x_a\eta^x_b\)", at \(a=b\)), not its statement. The draft's citation, "Theorem 3.4", is wrong: that theorem is the `L5-U` statement \((U^{jk})^2=0\); the distiller corrected it. Edit E6. |
| 48 | Scope paragraph (127) | CORRECT | GB1 rightly does not claim that freezing is impossible on `L5-O`; see §4.4. |
| 49 | GB1-H paragraph (131) | INCOMPLETE | GB1(e) asks, for each CA-I hypothesis, whether the bridge delivers it, cannot deliver it, or needs a named input. The paragraph gives a collective answer. The per-hypothesis table is §4.6. The YM-branch quotations behind H1-H7 were re-read at `fda786822` and match. |
| 50 | Readings introduction (133) | CORRECT | |
| 51 | R-NN1 row (137) | CORRECT | Not needed by the five-mode rung laws of §4.5, which use NN-a's own text. |
| 52 | R-FORM row (138) | CORRECT | Test 1 is C because GB1(a) delegates the form: "The target form is chosen by the lane and justified". |
| 53 | R-EQ row (139) | CORRECT | |
| 54 | R-SUB row (140) | CORRECT | |
| 55 | \(L_{\mathbb Z_2}\) row (141) | CORRECT | |
| 56 | \(L^{cf}_{\rm cube}[S]\) row (142) | CORRECT | |
| 57 | Closing paragraph (144) | CORRECT | |

**Tally.** INCOMPLETE: items 1, 13, 39, 49. ERROR: none. CORRECT: the other 53.

---

## 4. Decisions on the named items

### 4.1 GB1-FORM

**The exact Trotter identity holds.** F3 is exact for every law \(U=W_BW_EM_oM_e\) whose cube gates of one tiling are disjoint and whose magnetic sublayers have commuting gates. One addition: the equal-angle hypothesis is not needed for the magnetic layer to be one exponential. Each link lies in exactly one tiling cube of either tiling (`GA1_5.md` Theorem 2.1), so *all* cube gates commute, and \(W^{cube}=\exp(-i\sum_C\theta_{T(C)}B_C)\) for any \(\theta_e,\theta_o\). Equal angles are needed only so that the target has one magnetic coupling.

**No positive transfer is fixed by the law.** F1: a positive unitary is \(1\). F2: the positive \(T\) with \(T^{\,i}=U\) correspond one-to-one to the Hermitian logarithms of \(U\). Integer-tick data do not distinguish them; imaginary-time correlators do. One working-set text bears on E-1 and is not cited: PS-7r reads the one-body quasi-energy "in `(-pi, pi]`". That is a branch convention for the one-body modes of a quasi-free tick, used to define the sea. It does not supply a many-body logarithm with a state relation, so it does not discharge E-1 or E-2. GB1 should say so (edit E7).

**Decision.** GB1-FORM = the Hamiltonian (Trotterized) target is justified, as the lane's choice that GB1(a) delegates. The Euclidean target needs E-1 to E-4. Following GB1 line 59, these are inputs of one route, not shown necessary for every route.

### 4.2 GB1-Z2, R and R1, U1-QL and U1-LS, D-theory

**GB1-Z2.** Theorems Z2-A to Z2-C and Proposition Z2-D are correct as stated, for the one-mode test law \(L_{\mathbb Z_2}\) under R-NN1. The frame group is \(\mathbb Z_2\) in the repository's gate-wise sense. The algebra-level equality with the Trotterized \(\mathbb Z_2\) theory with one fermion is an identity map onto a target defined by the same operators. Its content is admissibility (Z2-A), which is a real theorem. Proposition Z2-D is correct: the pure-gauge inclusion does not intertwine for \(a_e\notin D\), \(D\) discrete with \(0\in D\). The five-mode version is §4.5.

**R and R1.** Correct, with the trace count \(N(1-2\delta)\le\sum_k\operatorname{Tr}Q_{j_k}\le D\). The uniform quantifier is the owner's own ("support-radius-dependent constants"). R1 fails without it, and GB1 says so.

**U1-QL.** Correct. **U1-LS.** Correct, with the leak closure of item 39. The rate \(O((\log S)^4/S^2)\) holds for fixed box, \(n\), \(M\), \(\tau_B\), once \(M+(n+1)K+1\le S/4\) and \(K+1\ge16e^2\tau\). Then \(t_K\le e^{16\tau}e^{-(\log S)^2}=e^{16\tau}S^{-\log S}\).

**D-theory.** The count is correct for that route: the reduced direction is the quantum-link model's own Euclidean time, so three spatial directions give a three-dimensional theory.

### 4.3 SU2-C, and Proposition SU2-B repaired (referee closure)

**SU2-C** is correct as stated (items 42-43). It is a sector-level statement for the restricted-subgroup invariants. Its target is the specified \(U(2)\) rishon quantum-link model on the frozen summand.

**GAP SU2-B is real.** The draft asserts, without proof, that distinct plaquette monomials are linearly independent on \(\Lambda^m\mathbb C^{10}\). The closure below proves it with end-number charges. The rest of the draft's argument then goes through unchanged.

**Proposition SU2-B (repaired statement).** Fix \(1\le m\le9\), \(L5\)-U\([m]\) with the cube-face layer at angles \(\theta_e,\theta_o\), and any other constants. Let \(\ell\) lie in an even cube \(C\) and let \(v\) be an endpoint of \(\ell\). There is a discrete set \(D_m\subset\mathbb R\) with \(0\in D_m\) such that for each \(\theta_e\notin D_m\) there are matter-empty states \(\omega,\omega'\) that agree on \(\mathfrak B_2\) and satisfy \(\omega(\alpha(N^{\mathsf B}_{\ell,v}))\ne\omega'(\alpha(N^{\mathsf B}_{\ell,v}))\). Hence no map \(\beta:\mathfrak B_2\to\mathfrak B_2\) satisfies \(\omega\circ\alpha=\omega\circ\beta\) on \(\mathfrak B_2\) for all matter-empty \(\omega\). In particular \(\alpha\) does not restrict to an automorphism of \(\mathfrak B_2\).

*Proof.* Let \(K\) be the Hilbert space of the twelve links of \(C\). For each rishon mode \(\mu=(\ell',w,i)\) of these links put \(\delta_\mu=[n_\mu,\cdot\,]\) on \(B(K)\). The \(\delta_\mu\) commute. Each is diagonalizable with integer eigenvalues and self-adjoint for the Hilbert–Schmidt inner product. So \(B(K)\) is the orthogonal sum of joint eigenspaces \(B_q\), labelled by charge vectors \(q\).

*Step 1 (charges of monomials).* A monomial \(t\) of \(B_C\) is a product of one entry per link of a face \(p\subset C\). An entry with arrival-end index \(a\) and departure-end index \(b\) is \(r^{\rm arr}_ar^{{\rm dep}\dagger}_b\): forward, \(U^{ab}=r^y_ar^{x\dagger}_b\); backward, \((U^\dagger)^{ab}=r^x_ar^{y\dagger}_b\). At a corner \(w\) with index \(i\), \(t\) annihilates \(i\) on the arriving link's \(w\)-end and creates \(i\) on the departing link's \(w\)-end. So \(t\in B_{q(t)}\), where \(q(t)\) is \(-1\) and \(+1\) on those two modes at each corner and \(0\) elsewhere. Then \(q(t)\) determines the face (its support), the orientation and every corner index. Distinct monomials lie in distinct \(B_q\).

*Step 2 (monomials are nonzero).* On \(\Lambda^m\mathbb C^{10}\), \(1\le m\le9\), each entry \(r^{\rm arr}_ar^{{\rm dep}\dagger}_b\) is nonzero. Take a basis vector with the arrival mode full and the departure mode empty; the other \(m-1\le8\) rishons fill any of the remaining eight modes. Link registers are ordinary tensor factors, so a product of nonzero entries on four distinct links is nonzero.

*Step 3 (the derivative).* Let \(\Pi\) be the orthogonal projection onto the sum of the \(B_q\) with \(q_\mu\ne0\) for some spectator mode \(\mu\) (flavour in \(\{1,2,3\}\)). Every element of \(\mathfrak B_2|_C\) commutes with all spectator numbers, so \(\Pi(\mathfrak B_2|_C)=0\). Put \(f(\theta)=e^{i\theta B_C}N^{\mathsf B}_{\ell,v}e^{-i\theta B_C}\) and \(g=\Pi f\). Then \(g\) is entire and \(g(0)=0\). For a monomial \(t\), \([t,N^{\mathsf B}_{\ell,v}]=\mp t\) if its corner index at \(v\) lies in \(\mathsf B\), and \(0\) otherwise. Hence \(g'(0)=\sum_{t\in T^*}\pm i\,t\). Here \(T^*\) is the set of monomials of the two faces of \(C\) through \(\ell\) whose index at \(v\) lies in \(\mathsf B\) and some other corner index lies in \(\{1,2,3\}\). \(T^*\) is not empty (index \(4\) at \(v\), index \(1\) at the other end of \(\ell\)). By Steps 1-2 its members are nonzero and lie in distinct eigenspaces, so \(g'(0)\ne0\). The real zero set \(D_m\) of \(g\) is discrete and contains \(0\).

*Step 4 (two states).* On matter-empty states, \(\alpha\) acts on link operators as \(\operatorname{Ad}(W_BW_E)\) (proof of Theorem 3.3). Other cube gates commute with \(N^{\mathsf B}_{\ell,v}\). So \(\omega(\alpha(N^{\mathsf B}_{\ell,v}))=\omega(X)\) with \(X=W_E^*f(\theta_e)W_E\). \(W_E\) is a function of end numbers, so \(\operatorname{Ad}W_E\) preserves each \(B_q\), and \(X_c:=\Pi X=W_E^*g(\theta_e)W_E\ne0\) for \(\theta_e\notin D_m\). Also \(X_c\) is self-adjoint (\(B_q^*=B_{-q}\)), traceless and Hilbert–Schmidt orthogonal to \(\mathfrak B_2|_C\). Let \(d=\dim K\). Put \(\rho=1/d\) and \(\rho'=1/d+sX_c\) with \(0<s\le1/(d\|X_c\|)\). Take the matter vacuum and one fixed state on all other links for both. For \(b\in\mathfrak B_2|_C\), \(\operatorname{tr}((\rho'-\rho)b)=s\langle X_c,b\rangle_{HS}=0\). \(\mathfrak B_2\) is the closed span of products \(b_Cb_{\rm out}\), so the two states agree on \(\mathfrak B_2\). But \(\operatorname{tr}((\rho'-\rho)X)=s\|X_c\|_{HS}^2>0\). If \(\beta\) existed, \(\omega(\beta(N))=\omega'(\beta(N))\) since \(\beta(N)\in\mathfrak B_2\), a contradiction. □

The same proof works for any block \(\mathsf B\subseteq\{1,\dots,5\}\) with nonempty complement. It is used for \(\mathsf B=\{5\}\) in §4.5.

### 4.4 `L5-O`: the claim that freezing is impossible

GB1's Theorem 6.2 is correct: each `L5-O` plaquette monomial is unitary, so no monomial kills a vector. GB1 line 127 rightly declines the broader claim. The draft's FINISH line, "'Spectators can be frozen on `L5-O`': Lemma SU2-O (every plaquette monomial is unitary)", is wrong in its reason. Pair sums of monomials do kill frozen vectors (Lemma O1). The frozen-spectator route does fail on `L5-O`, but at the matter layer (Lemma O2).

Notation: for a link end \(E\) and \(j=1,\dots,5\), put \(f_{E,j}=(\eta^E_{2j-1}+i\eta^E_{2j})/2\), \(n_{E,j}=f^\dagger_{E,j}f_{E,j}\); at a site, \(g_{x,j}=c_{x,j}=(\gamma_{x,2j-1}+i\gamma_{x,2j})/2\) (`LW1_5.md` §1). Computations use the Clifford algebra of all link-end Majoranas and matter Majoranas. Every physical gate is even on each link factor and even in matter. On such elements the graded and the ordinary tensor products agree, so the identities hold for the law's operators on matter \(\otimes\bigotimes_\ell S_+\).

**Lemma O1 (corner factorization; referee).** For a plaquette \(p\), \(W(\partial p)=\epsilon\prod_wK_w\), with \(\epsilon=\pm1\) independent of the indices, and
\[K_w=\sum_{a=1}^{10}\eta^{B_w}_a\eta^{A_w}_a=2\sum_{j=1}^5\big(f_{B_w,j}f^\dagger_{A_w,j}+f^\dagger_{B_w,j}f_{A_w,j}\big),\]
where \(A_w,B_w\) are the arriving and departing link ends at the corner \(w\). Hence every term with a spectator pair \(j\) at some corner kills each vector with \(n_{A_w,j}=n_{B_w,j}\) there. In particular, the frozen classes "pairs \(j\in J\) full and pairs in \(\{1,2,3\}\setminus J\) empty at every link end" are killed by every spectator term, and \(B_p=2W(\partial p)\) acts on them as its block part.

*Proof.* An entry with arrival index \(a\) and departure index \(b\) is \(i\eta^{\rm arr}_a\eta^{\rm dep}_b\): forward, \(U^{ab}=i\eta^y_a\eta^x_b\); backward, \((-U^T)^{ab}=-i\eta^y_b\eta^x_a=i\eta^x_a\eta^y_b\). The eight Majoranas of a monomial sit at eight distinct link ends and anticommute pairwise. Regrouping them by corners therefore costs a sign that does not depend on the indices. With \(\eta_{2j-1}=f+f^\dagger\), \(\eta_{2j}=-i(f-f^\dagger)\): \(\eta^B_{2j-1}\eta^A_{2j-1}+\eta^B_{2j}\eta^A_{2j}=2(f_Bf_A^\dagger+f_B^\dagger f_A)\). Factors at other corners act on other ends and commute with \(n_{A_w,j},n_{B_w,j}\). □

**Lemma O2 (the matter step fails; referee).** \(h_\ell=-\tfrac12\big(\sum_a\gamma_{y,a}\eta^y_a\big)\big(\sum_b\eta^x_b\gamma_{x,b}\big)\), and each factor is a number-conserving exchange between the matter and the rishon end at one site: \(\sum_b\eta^x_b\gamma_{x,b}=2\sum_k(f_{x,k}g^\dagger_{x,k}+f^\dagger_{x,k}g_{x,k})\), with \(f_{x,k}\) the pair modes of the end \((\ell,x)\). So for empty matter, \(h_\ell(|0\rangle\otimes\phi)=\sum_{j,k}\pm2\,g^\dagger_{y,j}g^\dagger_{x,k}|0\rangle\otimes f_{y,j}f_{x,k}\phi\). This is nonzero, with matter number two, whenever some pair is full at both ends of \(\ell\). That holds on every frozen class with \(J\ne\varnothing\), and on frozen states with block rishons at both ends when \(J=\varnothing\). So the matter-empty frozen class is not invariant. The first-order term of the matter gate leaves it, so the gate leaves it for \(a_e\) outside a discrete set. □

`[check]` (`/tmp/toe-GB1ref/check_l5o.py`; Jordan–Wigner, one pair per end and per site, 16 dimensions): the corner identity holds exactly. The hop maps (empty matter, both ends full) to a vector of norm 2 and matter number 2, and it commutes with matter plus rishon number at \(x\).

**Decision.** On `L5-O` the route of Theorem 6.1 fails first at the matter layer, not at the plaquette layer. Whether `L5-O` has some other class on which a subgroup block evolves on its own stays open: **GB1-O**. Three attacks on GB1-O failed. (O-a) Matter empty: Lemma O2. (O-b) Matter pair numbers equal to the rishon pair numbers at every end of the site, which kills each hop factor: block plaquette terms move block fermions between ends at a corner and break the equality. (O-c) Matter filled: the factor \(f^\dagger_{x,k}g_{x,k}\) moves matter into empty rishon ends, so the class with empty spectator ends is not invariant.

### 4.5 The working-set GAP: can each rung live on five-mode sites?

**The GAP is real.** \(L_{\mathbb Z_2}\) and \(L^{cf}_{\rm cube}[S]\) have one-mode sites. PS-5's working-set text reads: "Each site has the possibilities of five fermion modes; its full algebra is `Cl(10)`, presented as `M_32(C)`." NN-a is stated "For the named five-mode laws, let `F_x=ΛC⁵`". R-NN1 replaces \(F_x\) by \(\Lambda\mathbb C^1\).

**What R-form constrains.** ZM1-INV reads: "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form)." GB1(a) asks for "a readout `Φ` of the owner's ZM1-INV form (a unital injective cell-covariant exponentially local *-homomorphism on gauge-invariant observables)". Suppose R-form also bound GB1's source. Then the source would be a five-mode construction, and no named \(LGT_G\) with \(L^2(G)\) or spin-\(S\) links could be a source at any rung. The ladder would be empty by premise. Candidate reading **R-GB1Φ** (not adopted): "In GB1(a), 'of the owner's ZM1-INV form' means the map properties in the parenthetical; R-form fixes the zoom's coarse sites, not GB1's source." Tests: 1 C (it reads GB1's own target text, as R-EQ does); 2 P; 3 P; 4 P. Under R-GB1Φ the GAP is exactly this: the rung's law must have five-mode sites. A zoom rung does not help: under R-form every coarse law is again a five-mode construction, so rung \(n\ge1\) supplies no \(\mathbb C^2\) or spin-\(S\) coarse register. The rung only sets the block scale of \(\Phi\).

**Theorem 5M (five-mode rung laws; referee construction).** Let \(L5[\mathbb Z_2]\) and \(L5[U(1),S]\) be Defs 6 and 7 with each site replaced by \(F_x=\Lambda\mathbb C^5\) (modes \(c_{x,j}\), \(N_x=\sum_jn_{x,j}\), \(P_x=(-1)^{N_x}\)). The hop is \(h_\ell=V_\ell\otimes\sum_{j=1}^5c^\dagger_{y,j}c_{x,j}+\text{h.c.}\), with \(V=Z\) or \(J\). The Gauss operators are \(G_x=P_x\prod_{\ell\ni x}X_\ell\), resp. \(\mathcal G_x=N_x+\sum_{\rm out}E_\ell-\sum_{\rm in}E_\ell\). Every other datum is unchanged. Then:
1. Both laws are gauge invariant and cell covariant. They have finite depth under NN-a's own gate text with \(F_x=\Lambda\mathbb C^5\) and the chosen \(H_\ell\).
2. Every gate-wise compatible site frame \(\varphi\) at \(x\) has \(\varphi(c_{x,j})=\lambda c_{x,j}\) for one \(\lambda\) with \(|\lambda|=1\). Here \(\lambda=\pm1\) for \(\mathbb Z_2\), and \(\lambda\) is arbitrary for \(U(1)\). So the exact frame group is \(\mathbb Z_2\), resp. \(U(1)\): the centre of \(U(5)\) acting on \(F_x\).
3. The identity readout gives algebra-level equality with the Trotterized \(\mathbb Z_2\) gauge theory, resp. the \(U(1)\) quantum link model, with five fermion flavours.
4. Theorem 3.3 and the sector clauses of Theorem 5.1 hold with \(n_x\) replaced by \(N_x\). "Filled" means \(N_x=5\), a static charge \(P_x=-1\), resp. \(5\). The inclusion fails to intertwine for \(a_e\) outside a discrete set: \(i[H_C,X_\ell]=-\tfrac{2\eta}{\sqrt3}Y_\ell\otimes\sum_j(c^\dagger_{y,j}c_{x,j}+\text{h.c.})\ne0\).
5. Theorem 5.2 (U1-LS) holds unchanged; it involves no matter.

*Proof.* (1) \(P_x\) flips all five \(c_{x,j}\) and \(X_\ell\) flips \(Z_\ell\), so hops are invariant; plaquettes and electric terms are as before. A2's signs act on all flavours alike: \(c_{x,j}\mapsto d_g(gx)c_{gx,j}\). Each \(V_\ell\otimes c^\dagger_{y,j}c_{x,j}+\text{h.c.}\) is even and lies in one edge triple, so `LW1.md`'s dressed factorization (lines 196-205) applies. Electric layers use six matchings. Magnetic gates use `GA1_5.md` Lemma U, which holds for five-mode sites and any finite registers (its Step 1 uses \(\mathcal A_w^+=M_{16}\oplus M_{16}\)), with Proposition C for scheduling. Theorem 3.1 and R-NN1 are not needed. (2) Gate-wise compatibility with a cube gate \(e^{-iaH_C}\), \(a\) outside its exceptional set (`LW1_5.md` §1), fixes \(H_C\). The three hops of \(C\) at \(x\) go to three different neighbours, and their parts are separated by the neighbours' number charges. So each such \(h_\ell\) is fixed. Suppose then that \(\operatorname{Ad}L\circ\varphi\) fixes \(h_\ell\), \(\ell=(x,y)\). Compare the parts that raise the \(y\)-number by one: \(\sum_jc^\dagger_{y,j}(V'\otimes\varphi(c_{x,j}))=\sum_jc^\dagger_{y,j}(V\otimes c_{x,j})\), with \(V'=\operatorname{Ad}L(V)\). On vectors with empty \(y\)-modes, distinct \(j\) give orthogonal vectors, so \(V'\otimes\varphi(c_{x,j})=V\otimes c_{x,j}\) for each \(j\). Equal nonzero elementary tensors give \(\varphi(c_{x,j})=\lambda_jc_{x,j}\) and \(V'=\lambda_j^{-1}V\); one \(V'\) forces one \(\lambda\). \(\varphi\) is isometric, so \(|\lambda|=1\). For \(\mathbb Z_2\), \(V'=\operatorname{Ad}L(Z)\) is Hermitian, so \(\lambda\) is real. Conversely, \(G_x\) implements \(\lambda=-1\), and \(e^{i\theta\mathcal G_x}\) implements \(\lambda=e^{i\theta}\). Non-linear and particle-hole frames are covered, because \(\varphi(c_{x,j})\) was arbitrary. (3)-(5) Repeat §§3 and 5 with the flavour sum. □

Tests for \(L5[\mathbb Z_2]\) and \(L5[U(1),S]\) as rung test laws: 1 C (as a framework law each would fix the gauge group, GA1-i's target; as a rung law the group is the ladder's premise); 2 P; 3 P; 4 P (the flavour-blind hop is exactly what makes the frame group the rung's group). The reading **R-NN5**: "NN-a's gate text applies to a five-mode rung test law with its chosen link register." It replaces R-NN1 here. Tests 1-4: P P P P (it changes no factor of NN-a's text; it only drops the word "named"). Not adopted.

**Theorem 5U (the \(U(1)\) rung at \(S=1/2\) inside the named law \(L5\)-U\([m]\), \(m\) odd; referee).** Take block \(\{5\}\) and spectators \(\{1,2,3,4\}\). Take \(J\subseteq\{1,2,3,4\}\) with \(|J|=k=(m-1)/2\), and the cube-face layer at one angle \(\theta\). Let \(\mathcal S^{(5)}_J\) be the states with empty matter and, at every link end, the flavours in \(J\) full and the other spectators empty. For \(m=1\) let \(\mathcal C_1\) be the larger class with empty spectator matter and empty spectator rishons; flavour-5 matter is free. Let \(\mathfrak B_5\) be the unital C*-algebra generated by the \(U^{55}_\ell\) and \(n^{(5)}_{\ell,v}\), together with the \(c_{x,5}\) on \(\mathcal C_1\). Then for every \(\omega\) in the class, every \(B\in\mathfrak B_5\) and every \(t\ge0\), \(\omega(\alpha^t(B))=\omega(\alpha_5^t(B))\). Here \(\alpha_5\) is \(\operatorname{Ad}\) of the flavour-5 tick. On the summand with one flavour-5 rishon per link, change the sign of \(|y,5\rangle\) on each link. Then \(U^{55}\mapsto J=S^+\), \(n^{(5)}_{\ell,x}-\tfrac12\mapsto E_\ell\), and the flavour-5 tick is the tick of \(L^{cf}_{\rm cube}[1/2]\): with its fermion \(c_{x,5}\) on \(\mathcal C_1\), with empty matter on \(\mathcal S^{(5)}_J\). For \(\theta\) outside a discrete set, \(\alpha\) does not restrict to an automorphism of \(\mathfrak B_5\) (§4.3 with \(\mathsf B=\{5\}\)).

*Proof.* This is the proof of Theorem 6.1 with \(\mathsf B=\{5\}\). Lemma S kills every spectator-index plaquette monomial on the class. On it, \(p_{\ell,x}=N^{(5)}_{\ell,x}+k\), so \((p_{\ell,x}-m/2)^2=(N^{(5)}_{\ell,x}-\tfrac12)^2=\tfrac14\), and the electric layer is a phase. For \(\mathcal C_1\), take a hop term \(c^\dagger_{y,j}r^y_jr^{x\dagger}_kc_{x,k}\). If \(k\ne5\), it starts with \(c_{x,k}\) on empty spectator matter. If \(k=5\ne j\), it needs \(r^y_j\) on an empty spectator rishon. The adjoint terms are alike. Only \((5,5)\) survives, and it preserves \(\mathcal C_1\). `LW1_5.md` §2 gives the basis change ("a phase change of one basis vector sends this to the spin-raising operator") and the charge: \(n_{x,5}+\sum_{\ell\ni x}n^{(5)}_{\ell,x}\) is `LW1`'s \(\mathcal G_x\) plus 3. □

So Theorem 5.1 at \(S=1/2\) holds inside \(L5\)-U at sector level, with its fermion when \(m=1\), for classes fixed in advance. This agrees with `TOE_ASSEMBLY.md` 3.5: "At one mode the law is `L_cube` with `S = 1/2`". For even \(m\), a one-flavour block is frozen: \(N^{(5)}_{\ell,x}+N^{(5)}_{\ell,y}=m-2k\) is even, hence \(0\) or \(2\). The family \(S\to\infty\) of Theorem 5.2 does not fit inside one named law, because \(m\) is fixed (`GA2_Y2.md` §5, row (a1)).

**The \(\mathbb Z_2\) rung inside the named laws: open, GB1-Z2[L5].** Three attacks failed.
- (Z-a) *A frozen one-flavour block of \(L5\)-U.* On its \(\mathbb C^2\) links put \(X_\ell=2n^{(5)}_{\ell,x}-1\) and \(Z_\ell=U^{55}_\ell+U^{55\dagger}_\ell\). The block tick \(\operatorname{Ad}(e^{-i\theta H^{(5)}_B})\) commutes with every \(Q^{(5)}_w=\sum_{\ell\ni w}n^{(5)}_{\ell,w}\), by \(U(5)\) gauge invariance. \(Q^{(5)}_w\) equals \(\sum_{\ell\ni w}s_\ell X_\ell\) plus a constant, with signs \(s_\ell=\pm\tfrac12\). The \(\mathbb Z_2\) tick gives \(\alpha_{\mathbb Z_2}(X_\ell)=X_\ell\,W_E^*\exp(2i\tau_B\sum_{p\ni\ell}Z_p)W_E\), since \(e^{-i\tau Z_p}X_\ell e^{i\tau Z_p}=X_\ell e^{2i\tau Z_p}\) for \(\ell\in p\). The four \(Z_p\) are independent commuting involutions, so their sum takes the values \(0,\pm2,\pm4\). So \(\alpha_{\mathbb Z_2}(X_\ell)=X_\ell\) iff \(\tau_B\in\tfrac\pi2\mathbb Z\). After conjugating back by \(W_E\), the term for \(\ell\) is a combination of Pauli strings whose only off-diagonal factor sits on \(\ell\). So terms with distinct \(\ell\) are linearly independent. So \(\alpha_{\mathbb Z_2}\) moves \(Q^{(5)}_w\) whenever \(\tau_B\notin\tfrac\pi2\mathbb Z\). On the same algebra the two ticks differ: the frozen block is the spin-1/2 \(U(1)\) model, not the \(\mathbb Z_2\) theory.
- (Z-b) *`L5-O` with frozen spectator pairs.* The plaquette step holds (Lemma O1). The matter step fails (Lemma O2).
- (Z-c) *The identity readout with the centre \(\mathbb Z_2\subset U(5)\) and R-SUB.* The result is a \(\mathbb Z_2\) gauge theory with link register \(\Lambda^m\mathbb C^{10}\) (or \(S_+\)) and \(U(5)\) (or \(\operatorname{Spin}(10)\)) traces as plaquettes. To call it \(LGT_{\mathbb Z_2}\) names the law as its own target. Tests: 1 F (it fixes the target by naming); 4 F (\(\dim\Lambda^m\mathbb C^{10}\ge10\ne2\)).

These are failures of routes. None proves that no ZM1-INV readout realizes the \(\mathbb Z_2\) rung inside \(L5\)-U or `L5-O`.

**`SU(2)`.** Theorem 6.1 already lives on \(L5\)-U. On `L5-O` the same route fails at the matter layer (Lemma O2).

| Rung | Five-mode test law (Theorem 5M) | Named law \(L5\)-U | Named law `L5-O` |
|---|---|---|---|
| \(\mathbb Z_2\) | algebra level, five flavours; pure gauge at sector level | open, GB1-Z2[L5]; (Z-a) fails at the tick | open; frozen route fails at matter (O2) |
| \(U(1)\) | algebra level, every \(S\); the family of Theorem 5.2 | sector level at \(S=1/2\), \(m\) odd (Theorem 5U); with fermion at \(m=1\) | frozen route fails at matter (O2) |
| \(SU(2)\) | not attempted | sector level, \(U(2)\) target (Theorem 6.1) | frozen route fails at matter (O2) |

### 4.6 GB1-H, hypothesis by hypothesis

The hand-off GAP (GB1 line 9) stands. CA-I's text is not in the repository; the YM branch at `fda786822` has only the structural index, with no row for `3.1:thm-main`. So the list below is the hypotheses as the branch records them, not CA-I's complete list. Sources: `library/port/p8-positivity.md` 31-49 ("\(G=SU(N_{\rm col})\)", "\(d\mu=Z_{\rm bare}^{-1}e^{-x_0A(U)}dU\)", (P8.1), "the Wilson measure is invariant under every torus isometry preserving the bare lattice"); `library/t0-tree.md` 13 and 36 ("separated tests and diagonal-flat Schwartz functions"; "A0 + AI: actual first-passage trajectory and exact Wilson RG").

| Hypothesis | Decision | Reason or named input |
|---|---|---|
| H1a. Gauge group \(SU(2)\), acting locally | Delivered, as an exact subgroup with its restricted Gauss law | `LW1_5.md` line 149 (Proposition T), on both five-mode laws; read by R-SUB. The full law group stays \(U(5)\) or \(\operatorname{Spin}(10)\). |
| H1b. Group-valued bond variables, normalized Haar measure | Cannot be delivered through a ZM1-INV readout of the full link algebra into any finite-register law, at any rung | Corollary 4.2 (R1). Correlator-level and Euclidean-variable routes are not excluded. |
| H2. The Wilson measure on \(\mathbb R^4/N\mathbb Z^4\) | Not delivered | Needs E-1, E-2, E-3, and for \(SU(2)\) a route that avoids R1. For \(\mathbb Z_2\), F4 shows the Wilson transfer is the tick at imaginary angles, which is not law data. |
| H3. Reflection positivity (P8.1) | Not delivered | Needs E-1 and E-2: by F1 the tick is not positive, and by F2 the law fixes no lift. |
| H4. Invariance under the bare-lattice isometries | Not delivered | Needs E-4 = Y3. The law's exact symmetries are \(\mathscr G\) and the tick; none exchanges time with a space direction. |
| H5. The first-passage trajectory (A0) | Not delivered | Needs a family of laws, or the requests T0-start[G] and T0-rate (`GA2_Y2.md` §5). One law has fixed constants. |
| H6. The scalar-curvature observable class | Not delivered | Needs the observable dictionary with errors (ZM1-G). |
| H7. A four-dimensional Euclidean form | Not delivered | Needs E-1 to E-3. |

The bridge does deliver, outside CA-I's list: exact local gauge invariance, finite NN-a depth, cell covariance, and the exact Trotter Hamiltonian form, on every rung where a law is given. At \(\mathbb Z_2\) it also delivers the exact link \(L^2(\mathbb Z_2)\) (Theorems 3.2 and 5M).

---

## 5. Required edits to `GB1.md`

- **E1** (line 5). Add Theorem 6.2 to the proved list. If the lead accepts the closures, also add Proposition SU2-B (repaired), Theorems 5M and 5U, and Lemmas O1 and O2, each marked "(referee closure, `GB1_REFEREE.md`)".
- **E2** (line 33). "Let \(\mathfrak B_2\) be the *unital* C*-algebra generated by …".
- **E3** (line 41). Replace "Self-adjointness is only a necessary condition for a literal self-adjoint unitary transfer; \(U^2=1\) is not enough for positivity" with: "A unitary tick is a self-adjoint transfer only if \(U=U^*\), which forces \(U^2=1\); and \(U^2=1\) does not give positivity."
- **E4** (line 105). Insert the leak closure of item 39. The truncated series is not a contraction, so the leak bound must come from the unitary gates.
- **E5** (line 107). "this defect is already in the paragraph after `GA2_Y2.md` Corollary 2.2 (a referee closure), stated for the link operator".
- **E6** (line 125). "as already shown in the proof of `GA2_Y2.md` Theorem 2.5". Do not restore the draft's citation "Theorem 3.4".
- **E7** (§2, after line 59). Add: PS-7r's branch "quasi-energy read in `(-pi, pi]`" is a one-body convention for the sea and does not discharge E-1 or E-2. Optionally add: the cube layer is one exponential for any \(\theta_e,\theta_o\) (§4.1).
- **E8** (lines 9, 121). Replace GAP SU2-B with the repaired Proposition SU2-B and the proof of §4.3.
- **E9** (line 7). Replace the working-set GAP with §4.5: Theorem 5M, Theorem 5U, and GB1-Z2[L5] open with attacks (Z-a) to (Z-c). Add R-GB1Φ and R-NN5 to the readings table, with their tests, marked proposed.
- **E10** (lines 123-127). Add Lemmas O1 and O2 and the decision of §4.4. The frozen route on `L5-O` fails at the matter layer; GB1-O is open. Do not carry the draft's FINISH line "'Spectators can be frozen on `L5-O`': Lemma SU2-O".
- **E11** (line 131). Replace the GB1-H paragraph with the table of §4.6, and keep the hand-off GAP.
- **E12** (line 11). Add GB1-Z2[L5] and GB1-O to "Open by name".

## 6. Open statements to carry, by name

- **GB1-Z2[L5].** Some ZM1-INV readout realizes a named \(\mathbb Z_2\) lattice gauge theory inside \(L5\)-U or `L5-O`, at algebra or sector level. Attacks (Z-a), (Z-b), (Z-c) failed (§4.5).
- **GB1-O.** `L5-O` has a class, fixed in advance, on which a subgroup block evolves on its own. Attacks (O-a), (O-b), (O-c) failed (§4.4).
- **GB1-U1 and GB1-SU2 beyond the proved sectors.** Inside the named laws, only sector-level statements are proved: \(S=1/2\) for \(U(1)\) and a \(U(2)\) target for \(SU(2)\). Block closure at algebra level fails (§4.3). The family \(S\to\infty\) exists only across test laws.
- **GB1-H**, with the hand-off GAP (CA-I's text unchecked); **E-1, E-2, E-3, E-4 = Y3**.
- The rest of `GB1.md` line 11 unchanged: GB1-SC, GB1-CF, T0-QLR[G], T0-start[G], T0-rate, Y1, Y2, Y2-W, VC1, TM1, ZM1-G, the observable dictionary.

## 7. Freeze recommendation

**Freeze `GB1.md` after edits E1-E12.** No item is an ERROR. Four items are INCOMPLETE, and each is closed here by a local edit or closure. Every theorem of `GB1.md` stands as stated. The new results (Proposition SU2-B repaired, Theorems 5M and 5U, Lemmas O1 and O2, the leak step) are referee closures. They have had this one check only and should be marked so. The readings R-NN1, R-FORM, R-EQ, R-SUB, R-GB1Φ and R-NN5, and the test laws \(L_{\mathbb Z_2}\), \(L^{cf}_{\rm cube}[S]\), \(L5[\mathbb Z_2]\) and \(L5[U(1),S]\), stay proposals. Nothing is adopted; only the owner adopts.

## Prior work used

Each item was read at the commit in the head. Each result is credited to its file and ported, not re-derived, except where a check needed the step.

| Prior result | Path | Use here |
|---|---|---|
| Pass 1: Lemma U1, Lemma Z2-F, Proposition SU2-B (its analytic-zero and two-state steps), Lemma SU2-O, the GB1-H table | `GB1_DRAFT.md` (Claude Opus 5.5) | Checked against `GB1.md`; SU2-B's steps 3-4 are the draft's, repaired by Steps 1-2 of §4.3 |
| Distillation, Defs 1-8, the GAPs | `GB1.md` (Codex gpt-6.1-terra) | The text refereed |
| §1 conventions, dressed factorization (196-205), A2, B3, B4, gauged covariance, E1 | `LW1.md` | Items 8-36; Theorem 5M(1) |
| Theorem 2.1 (G1), Theorem 2.2, Theorem 3.1, Lemma U, Proposition C, Amendment 1 | `GA1_5.md` | Items 10, 23, 37; §4.1 (unequal angles); Theorem 5M(1) |
| Theorem 2.3 (N4), Corollary 2.2 and the referee paragraph after it, proof of Theorem 2.5, §5 row (a1) | `GA2_Y2.md` | Items 29, 40, 47; Theorem 5U |
| §1-2 (both laws; "At one mode and m=1, it is unitarily equivalent to `L_cube`, S=1/2"; the basis change; charge plus 3), line 149 (Proposition T), B1-U, distiller definition 5 (gate-wise frames) | `LW1_5.md` | Items 25, 42-44; §4.4; Theorem 5U |
| (Z-a) locality | `ZM1.md` line 56 | Item 6 |
| ZM1-INV and R-form; PS-5; NN-a; the one-mode `L_cube` remark | `TOE_ASSEMBLY.md` 3.4, 3.5, 3.7, 3.9 | §4.5 |
| D-theory dimension count | `LIT_QLM.md` line 15 | Item 41 |
| CA-I hypotheses as recorded | YM branch `library/port/p8-positivity.md` 31-49, `library/t0-tree.md` 13-15, 36 | §4.6 |

**Prior work the digest missed.** `ZM1INV.md` (pass 2 of ZM1-I1[INV], in this folder) states the R-form setting and the support-radius-dependent constants (line 19) that Def 1 reads. Its Theorem 3.4, "A good sector of an `m=1` path carries an exact coarse link algebra", bears on a coarse \(U(1)\) link at a zoom rung. It is unrefereed and is not used here. `LW1_5.md` §2's one-mode equivalence sentence is the base of Theorem 5U; the digest lists `LW1_5.md` only for subgroups.

## FINISH

**Proved** (here, as referee closures; one check only).
- Proposition SU2-B, repaired: for \(1\le m\le9\) and \(\theta_e\) outside a discrete set, two matter-empty states agree on \(\mathfrak B_2\) and differ on \(\alpha(N^{\mathsf B}_{\ell,v})\). The missing step is closed by end-number charges: distinct monomials lie in distinct joint eigenspaces, and each is nonzero.
- The leak step of U1-LS. With it, the bound and the rate \(O((\log S)^4/S^2)\) hold as stated.
- Theorem 5M: the \(\mathbb Z_2\) and \(U(1)\) rungs on five-mode sites. They are gauge invariant and cell covariant, have finite depth under NN-a's own gate text, have exact frame group the centre \(\mathbb Z_2\) or \(U(1)\) of \(U(5)\), give algebra-level equality with five fermion flavours, and give sector-level pure gauge. R-NN1 is not needed.
- Theorem 5U: on classes fixed in advance, \(L5\)-U\([m]\) with \(m\) odd equals the Trotterized spin-1/2 \(U(1)\) quantum link model with cube faces at sector level. With its fermion when \(m=1\).
- Lemmas O1 and O2 on `L5-O`: plaquettes factor into number-conserving corner exchanges, so pair sums kill frozen vectors; the Majorana hop turns a rishon at each end of a link into a matter pair.
- Every theorem of `GB1.md` was re-derived and is correct: F1-F4, U1, Z2-A to Z2-D, R and R1 with the trace count, U1-QL, U1-LS, SU2-C, SU2-O (limited), and the D-theory count. `[check]` agrees for F4 and for Lemmas O1-O2.

**Counterexamples.**
- The draft's FINISH line "'Spectators can be frozen on `L5-O`': Lemma SU2-O" fails in its reason: by Lemma O1, pair sums of unitary monomials kill frozen vectors. The frozen route on `L5-O` fails instead at the matter layer (Lemma O2).
- Route (Z-a): the frozen one-flavour block of \(L5\)-U is not the \(\mathbb Z_2\) theory on the same links. Its tick conserves \(Q^{(5)}_w\); the \(\mathbb Z_2\) tick does not when \(\tau_B\notin\tfrac\pi2\mathbb Z\).

**Open by name.** GB1-Z2[L5] (attacks Z-a, Z-b, Z-c failed); GB1-O (attacks O-a, O-b, O-c failed); GB1-U1 and GB1-SU2 beyond the proved sectors; GB1-H with the hand-off GAP; E-1, E-2, E-3, E-4 = Y3; GB1-SC; GB1-CF; T0-QLR[G], T0-start[G], T0-rate; Y1, Y2, Y2-W, VC1, TM1, ZM1-G, the observable dictionary.

**What changes downstream.**
- GB1 can freeze after edits E1-E12.
- The \(U(1)\) rung at \(S=1/2\) holds inside the named law \(L5\)-U\([m]\), \(m\) odd, at sector level, with its fermion at \(m=1\). The \(\mathbb Z_2\) and all-\(S\) \(U(1)\) rungs hold on five-mode test laws, which are not working-set laws.
- Any `L5-O` bridge by frozen spectators must handle the matter layer first. The plaquette layer is not the obstacle.
- GB1-H: of the recorded CA-I hypotheses, only H1a (an exact local \(SU(2)\)) is delivered. H1b cannot be delivered through a ZM1-INV readout. H2-H7 need the named inputs.
