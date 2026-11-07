lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane
# B5(b) referee report (pass 3)

Written 2026-11-06 (UTC) by a Claude Opus 5.5 headless lane on the Mac mini, as pass 3 (referee) of item B5(b) of part LW1 of the TOE assembly, under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**Referee.** Claude Opus 5.5 (model id `claude-opus-5-5`), max effort, headless. This session wrote neither pass 1 (`B5B_DRAFT.md`) nor pass 2 (`B5B.md`). This is one check: one line-by-line read of `B5B.md`. It reviews no other review. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged; this report did not need it. A "referee closure" (RC) is a short complete argument, written here, for a step the text omits. A `[check]` is a tiny scratch computation (`/tmp/toe-b5bref/check_b5bref.py`, output `/tmp/toe-b5bref/out.txt`; 0.5 s, a few MB, floating point). A check guides and never proves.

**Text read.** `B5B.md` at commit `5d1409d92`, the last commit that touches it. SHA-256 `aac119a36a31b7bc5fe732a53e3e24b63117b9ef7e6e0cefd2205e0c08cf13e9`. Line numbers below refer to this file (138 lines).

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` at session start | `5d1409d92` |
| the same branch when this report was finished | `b05ee6430`. Its two new commits touch `CH1.md`, `LW1_5.md` and `TM1_DRAFT.md` only; `B5B.md`, `B5B_DRAFT.md` and `LW1.md` are unchanged `[check: git diff --quiet 5d1409d92 b05ee6430]`. |

Files read, by line. This folder: `B5B.md` lines 1-138 (all). `B5B_DRAFT.md` lines 1-428 (all); last changed `6d27df284`; SHA-256 `3bf103d2…ac456a`, the hash `B5B.md` records. `LW1.md` (last changed `da0ec1934`; SHA-256 `66d67e66…bb5505`, the hash `B5B.md` records): lines 14-70 (premises, free data, section 1), 170-250 (A1, A1a, dressed factorization, A2, A3, B2, B3, B4, gauged covariance, B5(a), B5(b), GAP B5(b)), 388-402 (E1), and grep hits at lines 7, 9, 16, 476 and 492. `LW1_REFEREE.md` lines 1-100 and its section headings (format only). `Y2W_DRAFT.md` lines 1-40 (head format only). For the downstream paragraph only, grep hits for "B5(b)" and "B5b": `CH1_DRAFT.md` lines 23, 25 and 414, and `CH1.md` line 73 at `b05ee6430`. Repository root: `CLAUDE.md`, `AGENTS.md`. No other branch was read.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The definitions of `B5B.md` section 1 are read plainly, as the distiller states them. No hostile meaning is read into them.

**Working set used, by name.** None as a premise of this report. The results of `B5B.md` are conditional on its section 1 definitions. Those definitions read PS-6 and PS-6r (frames, registers) on LW1's law `L_cube`, whose two tilings come from PS-1c. This report checks the mathematics under those definitions.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: the Jordan–Wigner representation; uniqueness of simple tensors; inner automorphisms of `M_n(ℂ)` (the matrix case of the Skolem–Noether theorem, rebuilt in RC2); joint diagonalization of commuting unitaries; spin rotation by `π`; irrationality of `√2`. No literature result is load-bearing.

**Method.** Every proof was re-derived by hand. Verdicts: CORRECT; ERROR (a line that is false or carries a wrong meaning, quoted, with a fix); INCOMPLETE (a named missing step or definition, with the step). A note on a CORRECT item does not change its verdict.

**Counts.** 68 items: 60 CORRECT, 2 ERROR, 6 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a theorem.

---

## 0. Outcome in one paragraph

Every theorem of `B5B.md` holds as stated under its definitions. Theorem 3.1 (odd gates), Corollary 3.2, Theorem 3.3 (whole tick), Proposition 3.4 (odd half-step), Theorem 4.1 (reading R-M), Theorem 4.2 (reading R-E, odd gates) and Lemma 4.3 were re-derived step by step. The two ERRORs are wording. The first makes a definition ambiguous: "links outside \(A\)" must read "links not internal to \(A\)". The second misstates the open link value at a target end in Lemma 2.3. The six INCOMPLETE items are missing text, not missing mathematics: the definition of \(F\)-charge; the two block identities of Lemma 2.4, which four proofs use; the rank-one step in Lemma 2.2; the symbol \(g_{vx}\); the even-layer GAP, absent from the Open list; and the four-test results for the section 1 readings. Each has a fix below; four come with a referee closure (RC1-RC4). A fifth closure strengthens the text: the set of R-E compatible frames is not closed under composition, so it is not a group (RC5, section 2.4). Recommendation: freeze after the required edits of section 4.

---

## 1. Verdict table

| # | Item (B5B line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 Status paragraph (5) | CORRECT | Each claim is proved below: odd gates (3.1), whole tick (3.3), odd half-step (3.4), every tuple occurs (3.1 converse). LW1's B5(b) hypothesis implies the odd-gate hypothesis, so the answer to LW1's question holds a fortiori. |
| 2 | §0 Open paragraph (7) | INCOMPLETE | Omits the body's "GAP: even-layer mode image" (102). Does not say that the register factors and the exceptional angles are not needed for the mode image. |
| 3 | §0 Provenance (9) | CORRECT | Both recorded hashes equal the files read `[check: shasum -a 256]`. |
| 4 | §1 notation: \(S\), \(a_o>0\), \(\operatorname{Ad}V\), even cell (13) | CORRECT | \(a_o=\varepsilon+\mu/2>0\) follows from \(0\le\mu<2\varepsilon\). "Even cell" means \(b\in2\mathbb Z^3\), as in LW1's \(\mathcal T_e\). |
| 5 | §1 definitions of \(\mathcal A_A\) and \(\mathcal O_A\) (13) | ERROR | "all links outside \(A\)" must read "all links not internal to \(A\)". Also state that \(\mathcal A_A\) and \(\mathcal O_A\) generate the quasi-local algebra. |
| 6 | §1 grading sentence (13, last) | CORRECT | |
| 7 | §1 frame (15) | CORRECT | |
| 8 | §1 register change; split; link-by-link and odd-cube changes are split (15) | CORRECT | The last claim uses Lemma 2.1 (a forward reference). |
| 9 | §1 odd-gate hypothesis (17-20) | CORRECT | |
| 10 | §1 "weaker than invariance of all cube gates …"; "The law uses \(a_x=a_o\)" (21) | CORRECT | An odd cube's own links are not internal to \(A\), and \(a_o\ne0\). |
| 11 | §1 readings R-M, R-E, R-T named (21) | CORRECT | Names only. |
| 12 | §1 layer automorphisms and \(\alpha\) (23) | CORRECT | \(\gamma_e\gamma_o\gamma_E(z)=M_e^*M_o^*W_E^*zW_EM_oM_e=U_0^*zU_0\), LW1's \(\alpha\) (LW1 line 64). |
| 13 | §1 Hypothesis T and its finite-torus equivalence (23) | CORRECT | The stated reason is the right one. The one-line computation is draft line 264. |
| 14 | §1 \(D_\lambda\) (25) | CORRECT | \(e^{-i\theta n}ce^{i\theta n}=e^{i\theta}c\). |
| 15 | §1 mode image (25) | CORRECT | |
| 16 | §1 \(F\)-charge (missing) | INCOMPLETE | Used in 2.4, 3.3, 3.4 and 4.1, never defined. Its sign convention fixes the values \(-1,-1,-2,0\) in 3.3. RC3. |
| 17 | §1 four-test results (missing) | INCOMPLETE | Section 1 states readings with no four-test result; the draft's checks (draft 1.3, 7.8) were dropped. RC4 gives the results. |
| 18 | Lemma 2.1 and proof (29-31) | CORRECT | Self-contained; it does not need LW1's A1. |
| 19 | Lemma 2.2 statement (33) | CORRECT | Note: name the algebras (\(a_j,a,a'\in\mathcal C_1\); \(b_j,b,b'\in\mathcal C_2\)). Move into the statement the two general facts its proof contains, which 3.1 and 3.3 cite "by Lemma 2.2". |
| 20 | Lemma 2.2 proof: parity (35, sentences 1-2) | CORRECT | |
| 21 | Lemma 2.2 proof: inner automorphisms (35, sentence 3) | INCOMPLETE | "the rank-one range of the image of \(e_{11}\)": rank one is not shown, and the check that \(V\) is unitary and implements the automorphism is missing. RC2. |
| 22 | Lemma 2.2 proof: uniqueness, homogeneity, extension (35, sentences 4-6) | CORRECT | The extension for odd \(V\) is \(\operatorname{Ad}V\circ\theta_{\rm out}\) (section 2.3). |
| 23 | Lemma 2.2 proof: splitting and commutant (37) | CORRECT | |
| 24 | Lemma 2.3 statement (39-43) | CORRECT | |
| 25 | Lemma 2.3 proof: block construction (45, sentences 1-2) | ERROR | "one weight below the appropriate extremum" is wrong at a target end, where the open value is \(-S+1\). |
| 26 | Lemma 2.3 proof: invariant blocks, amplitudes, \(\sqrt2\) (45, rest) | CORRECT | `[check A]` agrees. |
| 27 | Lemma 2.3 proof: the two displayed inequalities (47) | INCOMPLETE | \(g_{yx}\), \(g_{xx}\) are undefined. Define \(g_{vx}=\langle v\vert G\vert x\rangle\) in the block. The mathematics is right; `[check A]` agrees. |
| 28 | Lemma 2.4 statement (49-53) | INCOMPLETE | The algebra containing \(z\) is not named. The block identities \((1-n_x)zn_x=c_xY\) and \(n_xz(1-n_x)=c_x^\dagger X\) are missing; 3.1, 3.3 (twice), 3.4 and 4.1 use them. "Charge" is undefined (item 16). RC1. |
| 29 | Lemma 2.4 proof (55) | CORRECT | The block identities follow in one line (RC1). |
| 30 | Theorem 3.1 statement, direct part (59-63) | CORRECT | |
| 31 | Theorem 3.1 proof: the inflow block (66) | CORRECT | Cite Lemma 2.4 for the form \(c_x^\dagger X\). |
| 32 | Theorem 3.1 proof: \(\varphi(c_x^\dagger)\operatorname{Ad}L_x^{\rm out}(X)=c_x^\dagger X\) and the phase (66-70) | CORRECT | |
| 33 | Theorem 3.1 proof: the commutant step giving \(W\) (70) | CORRECT | |
| 34 | Theorem 3.1 converse (64, 72) | CORRECT | Note: a plaquette monomial is fixed with the factors on its own links, which can lie in two odd cubes (section 2.3). |
| 35 | Theorem 3.1, compact groups and the full compatible set (64) | CORRECT | \(\lambda\) is a continuous homomorphism; a compact image is closed. |
| 36 | Corollary 3.2 and proof (74-76) | CORRECT | One site has no internal link, so every register change is split. |
| 37 | Gate versus generator (78) | CORRECT | |
| 38 | Theorem 3.3 statement (80) | CORRECT | |
| 39 | Theorem 3.3 proof: absorbing \(L^{\rm in}\) (82) | CORRECT | |
| 40 | Theorem 3.3 proof: identities (3.1) (83-87) | CORRECT | |
| 41 | Theorem 3.3 proof: \(\gamma_e,\gamma_E\) preserve \(\mathcal A_A\) and \(\mathcal O_A\) (88) | CORRECT | |
| 42 | Theorem 3.3 proof: \(\psi'=\varphi'\operatorname{Ad}L'\), \(\chi=\varphi_1\operatorname{Ad}R\) (88) | CORRECT | Note: write out \(\varphi'=\gamma_E\varphi\gamma_E^{-1}\), \(L'=W_E^*LW_E\), \(\varphi_1=\gamma_e^{-1}\varphi\gamma_e\), \(R=M_eLM_e^*\) (draft line 312). |
| 43 | Step 1: \(\chi\) fixes \(Z=G^*c_yG\) (90) | CORRECT | Note: "a neighbour \(y\in O_x\)" means a neighbour of \(x\). |
| 44 | Step 1: charges of \(P,Q,X,Y\); \(Y\ne0\) (90) | CORRECT | Uses the block identity of RC1. |
| 45 | Step 1: slice functional; \(c_x\in\operatorname{span}\{d,d^\dagger\}\) (90) | CORRECT | Implicit: one finite region holds every term, and the hat map commutes with \(\operatorname{Ad}e^{i\theta N_F}\) for \(F\) outside \(A\). |
| 46 | Step 1: \(d=uc_x+vc_x^\dagger\); \(\varphi_1(n_x)\in\{n_x,1-n_x\}\) (90) | CORRECT | Implicit: both spans have dimension two, so they are equal. |
| 47 | Step 2: \(\psi'(Z')\in\{Z',1-Z'\}\) (92) | CORRECT | |
| 48 | Step 2: charge \(-1\) projection; \(\varphi'(c_x)=\lambda_xc_x\) (92-96) | CORRECT | |
| 49 | Theorem 3.3 proof: all corners, electric layer, converse (96) | CORRECT | |
| 50 | Proposition 3.4 statement (98) | CORRECT | |
| 51 | Proposition 3.4 proof: the phase (100) | CORRECT | |
| 52 | Proposition 3.4 proof: an even-half-step invariant frame beyond site phases (100) | CORRECT | Uses \(a_e\ne0\); LW1's window gives \(a_e=\varepsilon-\mu/2>0\). |
| 53 | GAP: even-layer mode image (102) | CORRECT | The gap is real. No result of `B5B.md` needs it. |
| 54 | Theorem 4.1 statement (106) | CORRECT | Note: "local" in "graded local automorphism" is undefined (section 2.3). |
| 55 | Theorem 4.1 proof: a phase or a particle-hole map at each corner (108) | CORRECT | |
| 56 | Theorem 4.1 proof: all corners or none (110) | CORRECT | |
| 57 | Theorem 4.1 proof: realization; \(U(1)^8\rtimes\mathbb Z_2\) (112) | CORRECT | `[check B]` agrees. |
| 58 | R-M remark (114) | CORRECT | |
| 59 | Theorem 4.2 statement (116-120) | CORRECT | \(\varphi(c_x)=c_xW_0e^{ih_x}W_0^*\) checked. |
| 60 | Theorem 4.2 proof (i)⇒(ii), first paragraph (122) | CORRECT | Implicit: \(k\) lies in the span of the outside coefficients, and one coefficient is nonzero (draft line 223). |
| 61 | Theorem 4.2 proof (i)⇒(ii), second paragraph (124) | CORRECT | |
| 62 | Theorem 4.2 proof (ii)⇒(i) (126-130) | CORRECT | |
| 63 | Example; "This closes B5b-E for the odd gates"; no mode image (132) | CORRECT | |
| 64 | "The set of R-E compatible frames need not itself be a group" (132) | CORRECT | RC5 strengthens it: the set is not closed under composition. |
| 65 | Lemma 4.3 and proof (134-136) | CORRECT | |
| 66 | Closing paragraph (138) | CORRECT | |
| 67 | Fidelity to `B5B_DRAFT.md` (whole text) | CORRECT | Every draft result appears. Each change is a correction or a narrowing; none adds an unproved claim (section 3.F). |
| 68 | Fidelity to the `LW1.md` citations (whole text) | CORRECT | B3, B4, E1 and the law (LW1 lines 45, 62, 64) are cited correctly (section 3.G). |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 5 (line 13, the definition of \(\mathcal O_A\)).** `B5B.md`: "Let \(\mathcal O_A\) be the algebra generated by all outside modes and all links outside \(A\)." A link with exactly one end in \(A\) is not internal to \(A\). The text does not say whether it is "outside \(A\)". The proofs need it in \(\mathcal O_A\). In Theorem 3.1 the inflow coefficient \(X\) lives on the links of \(O_x\), and three of those links end at \(x\in A\); the proof then uses "the frame fixes its outside factor" (line 70). Theorem 3.3, Step 2, and Theorem 4.2 use the same fact. If these 24 links were not in \(\mathcal O_A\), a frame would not have to fix them, and those steps would fail as written. The draft's definition (draft line 59) reads "all links not internal to `A`". Lines 82 and 88 of `B5B.md` already use "outside-link unitary" in that sense. Fix: "Let \(\mathcal O_A\) be the algebra generated by all modes outside \(A\) and all links not internal to \(A\). Then \(\mathcal A_A\) and \(\mathcal O_A\) generate the quasi-local algebra." Under this reading every proof of `B5B.md` holds. Four-test of the fix: it names no target, it is closed, it settles nothing downstream, and it adds no structure; it restates the draft's definition. Pass.

**Item 25 (line 45, the block construction of Lemma 2.3).** `B5B.md`: "Put each path link one weight below the appropriate extremum, so the next hop has magnitude \(\sqrt{2S}\)." A particle leaves a path site through a link's source by \(J\), which raises \(m\), or through its target by \(J^\dagger\), which lowers \(m\). The values that give the hop magnitude \(\sqrt{2S}\) are \(m=S-1\) at a source end, since \(J|S-1\rangle=\sqrt{2S}\,|S\rangle\), and \(m=-S+1\) at a target end, since \(J^\dagger|{-S}+1\rangle=\sqrt{2S}\,|{-S}\rangle\). At a target end, \(-S+1\) is one weight above the extremum \(-S\), not below it. Fix: "Put each path link one step inside the extremum that its first hop moves toward: \(m=S-1\) if the path leaves through the link's source, \(m=-S+1\) if it leaves through the link's target" (draft line 120). The rest of the proof uses only the magnitude \(\sqrt{2S}\), which holds for both values. `[check A]` builds every block with these values.

### 2.2 INCOMPLETE, with referee closures

**Item 2 (line 7, the Open paragraph).** Missing: (a) the body's "GAP: even-layer mode image" (line 102); (b) for the register factors and the exceptional angles, the fact that no result of `B5B.md` needs them. `B5B.md` line 7 says: "The allowed **register factors** for a given phase tuple remain unclassified" and "Exceptional gate angles and their full compensation groups remain open." The draft says the mode image does not depend on either (draft lines 197, 377 and 421). Fix: add "the even-layer mode image (GAP, section 3)" to the list, and add "None of these three is needed for the mode image."

**Item 16 (\(F\)-charge, used and not defined).** Lemma 2.4 (line 53), Theorem 3.3 (lines 90-92), Proposition 3.4 (line 100) and Theorem 4.1 (line 108) use charges. RC3, to add to section 1 (draft line 280): "For a finite set \(F\) of sites, \(z\) has \(F\)-charge \(k\) if \(\operatorname{Ad}e^{i\theta N_F}(z)=e^{ik\theta}z\) for all real \(\theta\). Thus \(c_y\) has \(\{y\}\)-charge \(-1\) and \(c_y^\dagger\) has \(+1\)." With this convention Lemma 2.4's values are right: \(\operatorname{Ad}e^{i\theta n_x}(c_x^\dagger)=e^{i\theta}c_x^\dagger\), so the total charge of \(c_x^\dagger X\) is \(1\) plus the \(F\)-charge of \(X\), and \(X\) has \(F\)-charge \(k-1\); likewise \(Y\) has \(k+1\). Theorem 3.3's values \(-1,-1,-2,0\) follow from the total charge \(-1\) of \(Z=G^*c_yG\).

**Item 17 (four-test results, missing).** Section 1 is headed "Definitions inferred by the distiller". It states readings of a cell frame, of a split register change, of the odd-gate and whole-tick hypotheses and of a mode image, and Theorem 4.1 adds a requirement on the R-M compensation. None carries a four-test result. The draft's checks (draft sections 1.3 and 7.8) were dropped in distillation. RC4 (section 3.H) runs the four tests. All pass as stated hypotheses. The split condition passes test 3 only because `B5B.md` states its results as conditional and treats R-E separately; as an adopted meaning of PS-6 it would await the owner (B5b-E′).

**Item 21 (line 35, inner automorphisms in Lemma 2.2).** `B5B.md`: "choose a unit vector \(w\) in the rank-one range of the image of \(e_{11}\), and send basis vector \(i\) to the image of \(e_{i1}\) applied to \(w\)." Missing: why the range has rank one, and why the map is a unitary that implements the automorphism. RC2 (draft Lemma G3, line 112). Let \(\psi\) be a \(*\)-automorphism of \(M_n\) and \(f_{ij}=\psi(e_{ij})\). Then \(f_{11}\) is a projection with \(f_{11}M_nf_{11}=\psi(e_{11}M_ne_{11})=\mathbb Cf_{11}\). A projection of rank \(r\) has corner algebra \(M_r\), so \(r=1\). Take a unit vector \(w\) with \(f_{11}w=w\) and set \(Ve_i=f_{i1}w\). Then \(\langle Ve_i,Ve_j\rangle=\langle w,f_{1i}f_{j1}w\rangle=\delta_{ij}\), so \(V\) is unitary. Also \(Ve_{ij}V^*(Ve_k)=\delta_{jk}f_{i1}w=f_{ij}f_{k1}w=f_{ij}(Ve_k)\), so \(Ve_{ij}V^*=f_{ij}\), and \(\psi=\operatorname{Ad}V\) because the \(e_{ij}\) span \(M_n\).

**Item 27 (line 47, the symbol \(g_{vx}\)).** `B5B.md`: "the relevant block matrix element of \(Gn_xG^*\) is \(g_{yx}\overline{g_{xx}}\)." The symbols \(g_{yx}\) and \(g_{xx}\) are not defined. Fix: "Write \(g_{vx}=\langle v|G|x\rangle\) for states \(v\) of the block." The mathematics is right. In a block \(n_x\) acts as \(|x\rangle\langle x|\), so \(\langle y|Gn_xG^*|x\rangle=g_{yx}\overline{g_{xx}}\). In the two-site block \(g_{xx}=\cos a\beta\) and \(g_{yx}=i\sigma\sin a\beta\); the product vanishes only if \(\sin2a\beta=0\). In the three-site block \(\langle x|H^2|x\rangle=\beta^2\) and \(\omega^2=2\beta^2\), so \(g_{xx}=1+(\cos a\omega-1)/2=(1+\cos a\omega)/2\); the product vanishes only if \(\sin a\omega=0\). Both would give \(\omega/(2\beta)=1/\sqrt2\in\mathbb Q\). `[check A]` agrees.

**Item 28 (lines 49-53, the statement of Lemma 2.4).** `B5B.md`: "For an algebra \(\mathcal C\) of finitely many other modes and links, each element has a unique expansion". Missing: (a) the algebra that contains \(z\); (b) the two block identities that four later proofs use; (c) the definition of charge (item 16). Fix of the statement: "Each element \(z\) of the algebra generated by \(c_x\) and \(\mathcal C\) has a unique expansion … Moreover \((1-n_x)zn_x=c_xY\) and \(n_xz(1-n_x)=c_x^\dagger X\)." RC1, proof of the identities. The projection \(n_x\) is even and supported at \(x\), so it commutes with \(\mathcal C\). Also \(n_xc_x=0\), \(c_xn_x=c_x\), \(c_x^\dagger n_x=0\) and \(n_xc_x^\dagger=c_x^\dagger\). Hence \((1-n_x)Pn_x=(1-n_x)n_xP=0\), \((1-n_x)n_xQn_x=0\), \((1-n_x)c_x^\dagger Xn_x=(1-n_x)c_x^\dagger n_xX=0\) and \((1-n_x)c_xYn_x=(1-n_x)c_xY=c_xY\). So \((1-n_x)zn_x=c_xY\). The same four lines with the projections exchanged give \(n_xz(1-n_x)=c_x^\dagger X\) (draft Lemma D, line 288). Uses: Theorem 3.1 (\(n_xG(1-n_x)=c_x^\dagger X\)); Theorem 3.3, Step 1 (\(c_xY=(1-n_x)Zn_x\ne0\)) and Step 2 (\(c_x^\dagger X'=n_xZ'(1-n_x)\ne0\)); Proposition 3.4 (\(Y\ne0\)); Theorem 4.1 (both off-diagonal coefficients nonzero).

### 2.3 Notes on CORRECT items that bear on the freeze

- **Item 19 (Lemma 2.2 statement).** Name the algebras: \(a_j,a,a'\in\mathcal C_1\) and \(b_j,b,b'\in\mathcal C_2\). Add to the statement the two general facts its proof contains: every automorphism of a full matrix algebra is inner, and the commutant of \(M_n\otimes1\) in \(M_n\otimes M_k\) is \(1\otimes M_k\). Theorem 3.1 (line 70) and Theorem 3.3 (line 96) cite them "by Lemma 2.2".
- **Item 22 (the extension of a homogeneous \(V\)).** `B5B.md`: "A homogeneous implementer preserves the grading and hence extends over the graded tensor product." An explicit extension: for even \(V\), take \(\operatorname{Ad}V\) itself, which fixes \(\mathcal O_A\) because even elements of \(\mathcal A_A\) commute with \(\mathcal O_A\). For odd \(V\), let \(\theta_{\rm out}\) be the automorphism with \(c_y\mapsto-c_y\) for \(y\notin A\) that fixes the modes of \(A\) and all links. Then \(\operatorname{Ad}V\circ\theta_{\rm out}\) acts as \(\operatorname{Ad}V\) on \(\mathcal A_A\) and fixes \(\mathcal O_A\): \(\operatorname{Ad}V(-c_y)=-Vc_yV^*=c_y\), since \(V\) anticommutes with \(c_y\).
- **Item 34 (plaquette monomials in the converse of Theorem 3.1).** `B5B.md`: "Conversely every tuple in \(U(1)^8\) occurs with cube-local compensations and leaves every base gate and each plaquette monomial invariant." For base gates the compensation is cube-local. For a face that crosses the cut it is not. Take corners \(x,x+e_1\in A\) with \(x+e_2\notin A\). The face has the internal link \((x,x+e_1)\), the link \((x,x+e_2)\) of \(O_x\), the link \((x+e_1,x+e_1+e_2)\) of \(O_{x+e_1}\), and a link of the even cube containing \(x+e_2\). The frame alone multiplies \(J_p\) by \(e^{-i(\theta_x-\theta_{x+e_1})}\). The factors of \(\prod_{z\in A}e^{-i\theta_z\mathcal G_z}\) on the two odd links restore it, and those links lie in two different odd cubes. Suggested wording: "The gauge unitary \(\prod_{x\in A}e^{-i\theta_x\mathcal G_x}\) commutes with every base gate and every plaquette monomial (B4). Its factors on a gate's own links compensate that gate, and are cube-local; its factors on a plaquette's own links compensate that plaquette monomial." No result uses plaquettes; the plaquette class is open (GA1-P).
- **Item 42 (Theorem 3.3, line 88).** Write out \(\varphi'=\gamma_E\varphi\gamma_E^{-1}\), \(L'=W_E^*LW_E\), \(\varphi_1=\gamma_e^{-1}\varphi\gamma_e\) and \(R=M_eLM_e^*\). The text says "Consequently" and "Likewise" and leaves them implicit.
- **Items 43, 45, 46 and 60.** Implicit steps, each one line: \(y\) is a neighbour of \(x\); one finite region holds every term, and the hat map commutes with \(\operatorname{Ad}e^{i\theta N_F}\) because \(N_F\) is even and lies outside \(A\); \(\operatorname{span}\{c_x,c_x^\dagger\}\) and \(\operatorname{span}\{d,d^\dagger\}\) both have dimension two, so one inclusion gives equality; and in Theorem 4.2, if \(k\) had a component outside the span of the \(e_r\), the coefficient of that component would be \(0\) on the left and \(c_x^\dagger\ne0\) on the right.
- **Item 52 (Proposition 3.4).** The last assertion uses Lemma 2.3 at angle \(-a_e\), so it needs \(a_e\ne0\). LW1's window gives \(a_e=\varepsilon-\mu/2>0\). At \(a_e=0\) the assertion holds trivially, since every frame commutes with \(\gamma_e=\mathrm{id}\).
- **Item 54 (Theorem 4.1, "graded local automorphism").** `B5B.md`: "Require the outside compensation to extend jointly with the frame as a graded local automorphism." The proof needs this: the map equal to \(\varphi\) on \(\mathcal A_A\) and to \(\kappa_x\) on \(\mathcal O_A\) extends to an automorphism of the quasi-local algebra. Given Lemma 2.2, that holds exactly when \(\kappa_x\) preserves parity. If \(\kappa_x\) preserves parity, the graded commutation relations across the cut are preserved. Conversely, an odd \(b\in\mathcal O_A\) anticommutes with \(c_x\), so \(\kappa_x(b)\) anticommutes with \(\varphi(c_x)\) and \(\varphi(c_x)^\dagger\); the CAR of \(\varphi(c_x)\) then kill the even part of \(\kappa_x(b)\), as in the parity step of Lemma 2.2. The word "local" is undefined and not needed. Bounded slice maps suffice at infinite volume: the hat map \(b\mapsto P_A^{q}b\) sends \(\mathcal O_A\) into the relative commutant of \(\mathcal A_A\cong M_n\), and the functional can be \(g\circ E_{-1}\), with \(E_{-1}\) the charge projection and \(g\) a bounded functional equal to \(1\) on \(\widehat X\). Suggested wording: "Require each \(\kappa_x\) to preserve parity, so that \(\varphi\) on \(\mathcal A_A\) and \(\kappa_x\) on \(\mathcal O_A\) together define an automorphism of the quasi-local algebra."

### 2.4 Referee closure RC5: the R-E compatible frames are not closed under composition

`B5B.md` line 132: "The set of R-E compatible frames need not itself be a group." This is true. The stronger statement also holds.

**Proposition RC5.** Let \(x\ne x'\) be corners of \(A\) and \(m\) an internal link. Put \(\varphi_1=\operatorname{Ad}e^{-i\theta n_xE_m}\) and \(\varphi_2=\operatorname{Ad}e^{-i\theta' n_{x'}S^x_m}\), with \(S^x_m=(J_m+J_m^\dagger)/2\) and \(\theta=\theta'=\pi/2\). Each \(\varphi_j\) is R-E compatible for the odd gates. The composite \(\varphi_1\circ\varphi_2\) is not. So the set of R-E compatible frames is not closed under composition, and it is not a group.

*Proof.* Each \(\varphi_j\) has the form (ii) of Theorem 4.2, with \(W_0=1\) and one nonzero operator: \(h_x=\theta E_m\) for \(\varphi_1\) and \(h_{x'}=\theta'S^x_m\) for \(\varphi_2\). By (ii)⇒(i), each is R-E compatible. The composite \(\varphi=\varphi_1\circ\varphi_2\) is a frame on \(A\). Theorem 4.2 gives \(\operatorname{Ad}e^{in_xh}(c_x)=c_xe^{-ih}\), so \(\varphi_1^{-1}(c_x)=c_xe^{-i\theta E_m}\). The unitary \(e^{i\theta'n_{x'}S^x_m}=(1-n_{x'})+n_{x'}e^{i\theta'S^x_m}\) is even, so \(\varphi_2^{-1}\) fixes \(c_x\). Hence
\[
\varphi^{-1}(c_x)=\varphi_2^{-1}\big(c_xe^{-i\theta E_m}\big)=c_x\big[(1-n_{x'})A+n_{x'}B\big],\qquad
A=e^{-i\theta E_m},\quad B=e^{i\theta'S^x_m}e^{-i\theta E_m}e^{-i\theta'S^x_m}.
\]
Suppose \(\varphi\) were R-E compatible. The first paragraph of the proof of Theorem 4.2 gives \(\varphi^{-1}(c_x)=c_xu\) with \(u\) an internal-link operator. Then \(c_x(1-n_{x'})\otimes(A-u)+c_xn_{x'}\otimes(B-u)=0\) in \(\mathfrak A^m_A\otimes\mathfrak L_A\). The matter elements \(c_x(1-n_{x'})\) and \(c_xn_{x'}\) are nonzero and linearly independent, so \(A=u=B\). But \(A\ne B\). The rotation identity \(e^{i\theta'S^x}S^ze^{-i\theta'S^x}=S^z\cos\theta'+S^y\sin\theta'\) gives \(B=e^{-i(\pi/2)S^y}\) and \(A=e^{-i(\pi/2)S^z}\), where \(S^z=E_m\). The operator \(A\) is diagonal in the basis \(|m\rangle\). The operator \(B\) is not: it maps \(S^z\) to \(\pm S^x\) under conjugation, while a diagonal operator commutes with \(S^z\). This holds for every \(S\). ∎

`[check C]`: for \(S=1/2\), \(\max|A-B|=0.707\), and the blocks of \(\varphi^{-1}(c_x)\) at \(n_{x'}=0,1\) equal \(A\) and \(B\) to \(10^{-16}\).

*Consequence.* Under R-E, "the frame group" of the odd gates is undefined until more structure is specified. The draft said this without proof (draft line 367); RC5 proves it.

---

## 3. Checks behind the verdicts, section by section

### 3.A Sections 0 and 1

- **Item 1.** Line 5 claims four results. "the odd gates force independent site phases" is Theorem 3.1. "The same conclusion holds for the whole base tick and for its odd half-step" is Theorem 3.3 and Proposition 3.4. "Each phase tuple occurs" is the converse of Theorem 3.1. LW1 asks (LW1 line 492): "Determine the image of compact mode-linear frame groups on an even cell under the stated invariance of every dressed cube gate." Invariance of every gate implies the odd-gate hypothesis, so Theorem 3.1 answers it: a compact group of such frames has a closed image in \(U(1)^8\), and a mode-linear \(\Gamma(g)\) qualifies only for diagonal \(g\).
- **Item 3.** `shasum -a 256` gives `3bf103d2…ac456a` for `B5B_DRAFT.md` and `66d67e66…bb5505` for `LW1.md`, the values on line 9.
- **Item 4.** \(0\le\mu<2\varepsilon<\pi\) gives \(\varepsilon>0\) and \(a_o=\varepsilon+\mu/2\in(0,2\varepsilon)\subset(0,\pi)\).
- **Items 8 and 10.** A link-by-link unitary is a product over internal links times a product over the other links, so it is split. By Lemma 2.1 an odd cube has no internal link of \(A\), so a change on its links is split. If every cube gate is invariant after a change on its own links, then each odd gate \(e^{ia_oH_{O_x}}\) is, with a split change and \(a_o\ne0\). So the odd-gate hypothesis is weaker.
- **Item 12.** \(\alpha(z)=\gamma_e(\gamma_o(\gamma_E(z)))=M_e^*M_o^*W_E^*zW_EM_oM_e=U_0^*zU_0\), with \(U_0=W_EM_oM_e\) (LW1 lines 62 and 64).
- **Item 13.** On a finite torus the algebra is a full matrix algebra and \(\alpha=\operatorname{Ad}U_0^*\). Every automorphism satisfies \(\psi\circ\operatorname{Ad}U_0^*=\operatorname{Ad}\psi(U_0)^*\circ\psi\). So \(\psi\alpha=\alpha\psi\) holds exactly when \(\operatorname{Ad}(U_0\psi(U_0)^*)=\mathrm{id}\), that is, when \(U_0\psi(U_0)^*\) is a central unitary, a scalar of modulus one. At even side \(2k\ge4\) the intervals \(\{2j,2j+1\}\) and \(\{2i+1,2i+2\}\) mod \(2k\) meet in at most one point, so Lemma 2.1 holds; at side \(2\) they coincide.
- **Item 14.** \(nc=c(n-1)\) gives \(e^{-i\theta n}c\,e^{i\theta n}=e^{i\theta}c\).

### 3.B Section 2

- **Lemma 2.1.** The two interval families meet in at most one point per coordinate, so \(O_x\cap A=\{x\}\), and distinct corners have distinct odd cubes. A link of \(O_x\) has both ends in \(O_x\); if both were in \(A\), then \(|O_x\cap A|\ge2\). This replaces the draft's appeal to LW1's A1 and is valid.
- **Lemma 2.2, parity.** Let \(a\in\mathcal A_A\) be odd and \(b=\varphi(a)=b_++b_-\). The frame fixes \(c_y\) for \(y\notin A\). From \(ac_y=-c_ya\) we get \(bc_y=-c_yb\). Since \(b_+\) commutes and \(b_-\) anticommutes with \(c_y\), this gives \(c_yb_+=0\); likewise \(c_y^\dagger b_+=0\); so \(b_+=(c_y^\dagger c_y+c_yc_y^\dagger)b_+=0\). Even \(a\) is the same with signs exchanged.
- **Lemma 2.2, homogeneity.** \(\varphi\) commutes with \(\operatorname{Ad}P_A\), so \(P_AVP_AV^*\) is central: \(P_AVP_A=\zeta V\). Applying it twice gives \(\zeta^2=1\).
- **Lemma 2.2, splitting.** In a Jordan–Wigner order with the modes of \(\mathcal C_1\) first, \(c_v=P_1\otimes\hat c_v\) for modes \(v\) of \(\mathcal C_2\). A product of generators shows \(b=P_1^p\otimes\hat b\) for \(b\in\mathcal C_2\) of parity \(p\), with \(b\mapsto\hat b\) linear and injective. So \(ab=(aP_1^p)\otimes\hat b\). Independence and the uniqueness of nonzero simple tensors give (d) and (e). For (e): \(a'=\kappa a\) and \(b'=\kappa^{-1}b\), as stated.
- **Lemma 2.3.** A one-particle state carries no fermion sign: \(c_v^\dagger c_uc_u^\dagger|0\rangle=c_v^\dagger|0\rangle\). With the open values of item 25 and the blocking values (\(m=S\) at a source end, \(m=-S\) at a target end), only the path hops act. Each hop has amplitude \(\eta\sqrt{2S}/\sqrt3\), so the block Hamiltonians are \(\sigma\beta\sigma^x\) and the tridiagonal matrix with entries \(\sigma_1\beta,\sigma_2\beta\). For the second, \(H^3=\omega^2H\) with \(\omega^2=2\beta^2\), and \(\langle y|H^2|x\rangle=0\) because the cube graph is bipartite. Both amplitudes vanish only if \(a\beta=k\pi\) and \(a\omega=k'\pi\) with \(k,k'\ne0\), which gives \(\sqrt2=k'/k\). For the first display: \(c_yG|x\rangle=g_{yx}|\varnothing;m_y\rangle\), and \(G^*\) and \(1-n_x\) fix matter-empty states because every term of \(H_C\) contains an annihilator. `[check A]`: 2400 cases (\(S\in\{1/2,1,3/2,2,3\}\); every corner, edge and third site of one cube; ten angles including \(a\beta\in\{\pi/4,\pi/2,\pi\}\) and \(a\omega\in\{\pi,2\pi\}\)). Every block closed. The amplitudes matched \(|\sin a\beta|\) and \(\beta|\sin a\omega|/\omega\), and \(g_{xx}\) matched \((1+\cos a\omega)/2\), with no mismatch. The larger of the two block values was at least \(0.103\) in every case.
- **Lemma 2.4.** With \(x\) first, \(c_x=e_{01}\otimes1\), and \(b\in\mathcal C\) of parity \(q\) is \(P_x^q\otimes\hat b\). The four maps \(P\mapsto(1-n_x)P\), \(Q\mapsto n_xQ\), \(X\mapsto c_x^\dagger X\), \(Y\mapsto c_xY\) are bijections onto \(e_{00}\otimes\widehat{\mathcal C}\), \(e_{11}\otimes\widehat{\mathcal C}\), \(e_{10}\otimes\widehat{\mathcal C}\), \(e_{01}\otimes\widehat{\mathcal C}\); the parity factor only changes the sign of odd parts. Parity and \(\operatorname{Ad}e^{i\theta N_F}\) preserve each block, so they act term by term. RC1 adds the block identities.

### 3.C Theorem 3.1, Corollary 3.2, and line 78

- **Direct part.** \(G=e^{ia_xH_{O_x}}\) commutes with \(n_x+N_{\rm out}\), since each hop moves one particle inside \(O_x\). A block that lowers \(N_{\rm out}\) by one raises \(n_x\) from \(0\) to \(1\). So \(\sum_k\Pi_{k-1}G\Pi_k=n_xG(1-n_x)=c_x^\dagger X\) (RC1), with \(X\) odd, supported on \(O_x\setminus\{x\}\) and the links of \(O_x\), and \(X\ne0\) (Lemma 2.3). The automorphism \(\psi=\varphi\circ\operatorname{Ad}L_x\) fixes each \(\Pi_k\) and \(G\), so it fixes \(c_x^\dagger X\). Since \(L_x^{\rm in}\) commutes with \(X\) and \(\varphi\) fixes \(\mathcal O_A\) (item 5's reading), \(\psi(c_x^\dagger X)=\varphi(c_x^\dagger)\,L_x^{\rm out}XL_x^{{\rm out}*}\). Lemma 2.2(e) gives \(\varphi(c_x^\dagger)=\kappa c_x^\dagger\), and \(\{\varphi(c_x),\varphi(c_x)^\dagger\}=1\) gives \(|\kappa|=1\). Then \(\operatorname{Ad}D_\lambda^{-1}\circ\varphi\) fixes \(\mathfrak A^m_A\), maps its commutant \(1\otimes\mathfrak L_A\) onto itself, and equals \(\operatorname{Ad}W\) there. An automorphism is fixed by its values on generators, so it is \(\operatorname{Ad}(1\otimes W)\).
- **Converse.** With \(\theta=0\) outside \(A\), \(\prod_{x\in A}e^{-i\theta_x\mathcal G_x}=D_\lambda\prod_{\ell=(s,t)\subset A}e^{-i(\theta_s-\theta_t)E_\ell}\prod_{x}\prod_{\ell\in O_x,\ \ell\ni x}e^{\mp i\theta_xE_\ell}\), with the minus sign when \(x\) is the source. The first two factors form an even unitary of \(\mathcal A_A\), so their \(\operatorname{Ad}\) is a frame. For the odd gate of \(O_x\), the link factors at other corners lie in other odd cubes and commute with it; so the frame with the factors on its own three links acts on it as the whole gauge unitary does, which fixes it (B4).
- **Compact groups.** Phases compose, so \(\varphi\mapsto\lambda\) is a homomorphism on any group of such frames. It is continuous when the action is, so a compact group has a compact, hence closed, image.
- **Corollary 3.2.** One site has no internal link, so every register change is split, and the first paragraph of Theorem 3.1 applies with \(\mathcal A\) the algebra of \(x\).
- **Line 78.** If \(t\mapsto e^{iat}\) is injective on the finite spectrum of \(H_C\), a polynomial \(f\) with \(f(e^{iat})=t\) there gives \(H_C=f(e^{iaH_C})\), and an automorphism fixing the gate fixes \(f\) of it. Theorem 3.1 uses only the gate.

### 3.D Theorem 3.3 and Proposition 3.4

- **Identity (3.1).** From \(\psi\gamma_e\gamma_o\gamma_E=\gamma_e\gamma_o\gamma_E\psi\), compose with \(\gamma_e^{-1}\) on the left and \(\gamma_E^{-1}\) on the right: \(\chi\gamma_o=\gamma_o\psi'\).
- **The layers respect the cut.** By E1's local definition (LW1 line 395), \(\gamma_e(z)=G_A^*zG_A\) for local \(z\in\mathcal A_A\), since only \(G_A\) meets its support. For \(z\in\mathcal O_A\), \(G_A\) commutes with \(z\), and every other even gate \(G_B\) lies in \(\mathcal O_A\). The same holds for \(\gamma_e^{-1}\) and for the electric layer, whose gates lie on single links.
- **The outside factors.** \(\gamma_E\operatorname{Ad}L\gamma_E^{-1}=\operatorname{Ad}(W_E^*LW_E)\), a unitary on the links of \(\operatorname{supp}L\). \(\gamma_e^{-1}\operatorname{Ad}L\gamma_e=\operatorname{Ad}(M_eLM_e^*)\), and \(M_eLM_e^*\) uses only even gates \(G_B\) with a link of \(\operatorname{supp}L\) in \(B\). After absorbing \(L^{\rm in}\), no such \(B\) is \(A\), so \(R\in\mathcal O_A\) is even.
- **Step 1.** For \(a\in\mathcal A_A\) and \(b\in\mathcal O_A\), \(\chi(ab)=\varphi_1(a)\,RbR^*\), because \(R\) commutes with \(a\). In a Jordan–Wigner order with \(A\) first, on one finite region that holds every term, \(ab=(aP_A^q)\otimes\hat b\) for \(b\) of parity \(q\). Here \(P,Q\) are odd and \(X,Y\) even. With \(f\) equal to \(1\) on \(\widehat Y\) and \(0\) on the \(F\)-charge \(-1\) and \(-2\) subspaces (line 90), applying \(\mathrm{id}\otimes f\) to \(\chi(Z)=Z\) gives \(c_x\) on the right. On the left the terms with \(\varphi_1(1-n_x)P_A\) and \(\varphi_1(n_x)P_A\) are even, so the odd part is \(td^\dagger+sd\).
- **Step 2.** \(\psi'(Z')=\gamma_o^{-1}(\chi(n_x))=\gamma_o^{-1}(\varphi_1(n_x))\), because \(R\) commutes with \(n_x\). The charge projection \(E_{-1}\) on \(F=O_x\setminus\{x\}\) fixes \(\mathcal A_A\) pointwise, satisfies \(E_{-1}(ab)=aE_{-1}(b)\), and commutes with \(\operatorname{Ad}L'\) because \(L'\) acts on links only. In \(\psi'(Z')\) only the term \(\varphi'(c_x^\dagger)L'X'L'^*\) has \(F\)-charge \(-1\); in \(\pm Z'+\{0,1\}\) only \(\pm c_x^\dagger X'\) has it.
- **End and converse.** On \(\mathcal A_A\), \(\gamma_E=\operatorname{Ad}W_A^*\) with \(W_A=\prod_{\ell\subset A}e^{-i\tau_EE_\ell^2}\), and \(W_A\) commutes with \(D_\lambda\). For the converse, \(\psi=\operatorname{Ad}\prod_{x\in A}e^{-i\theta_x\mathcal G_x}\) on the relevant finite region; this unitary commutes with every gate (B4), so \(\psi\) commutes with each layer and with \(\alpha\). Its outside part is link by link, hence split.
- **Proposition 3.4.** \(\psi_o\) fixes \(c_y\), so it fixes \(\gamma_o\gamma_E(c_y)=G^*c_yG=Z\). Only \(c_xY\) has \(F\)-charge \(0\) in \(Z\), and \(\operatorname{Ad}L\) preserves \(F\)-charge. So \(\varphi(c_x)\,LYL^*=c_xY\), with \(Y\) even and nonzero. The last assertion: \(G_A\) commutes with \(M_e\), so \(\operatorname{Ad}G_A\) commutes with \(\gamma_e\). If \(\operatorname{Ad}G_A(c_x)=\lambda c_x\) held, \(G_A\) would commute with \(n_x\), against Lemma 2.3.

### 3.E Section 4

- **Theorem 4.1.** \(G=(1-n_x)P+n_xQ+c_x^\dagger X+c_xY\) with \(F\)-charges \(0,0,-1,+1\); \(X,Y\ne0\) by RC1 and Lemma 2.3. Parity preservation of \(\kappa_x\) (section 2.3, item 54) gives \((\varphi\circ\kappa_x)(G)=\varphi(1-n_x)\kappa_x(P)+\varphi(n_x)\kappa_x(Q)+\varphi(c_x^\dagger)\kappa_x(X)+\varphi(c_x)\kappa_x(Y)\). A slice functional equal to \(1\) on \(\widehat X\) and \(0\) on charges \(0\) and \(+1\) leaves \(c_x^\dagger P_A\) on the right; removing \(P_A\) and taking odd parts gives \(c_x^\dagger\in\operatorname{span}\{d,d^\dagger\}\). The flip argument: \(\psi_A(N_A)=N_{A\setminus F}+|F|-N_F\) commutes with \(G_A\), and so does \(N_A\); so \(N_F\) does, and Lemma 2.3 on an edge across the boundary of \(F\) forbids it. Realization: \(R=e^{-i\pi S^x}\) gives \(RJR^*=J^\dagger\) and \(RER^*=-E\). The map \(c\mapsto sc^\dagger\) with \(s_xs_y=-1\) sends \(c_y^\dagger Jc_x\) to \(-c_yJ^\dagger c_x^\dagger=c_x^\dagger J^\dagger c_y\). `[check B]`: for \(S\in\{1/2,1,3/2\}\), these identities and the image of one dressed edge term hold to \(4\cdot10^{-16}\). Semidirect product: \(C_A\Gamma_\lambda C_A^{-1}(c_x)=\overline{\lambda_x}c_x\).
- **Theorem 4.2.** \(e^{-in_xh}=1-n_x+n_xe^{-ih}\) gives \(e^{-in_xh}c_xe^{in_xh}=c_xe^{ih}\). In (i)⇒(ii), \(X=\sum_jm_jk_j\) with \(m_j\) odd and independent; \(\psi\) fixes the \(m_j\); Lemma 2.2(d) with \(\mathcal C_2\) the modes of \(O_x\setminus\{x\}\) gives \(\psi(c_x^\dagger k_j)=c_x^\dagger k_j\). The CAR give \((1-n_x)\iota^\dagger\iota+n_x\iota\iota^\dagger=1\), so \(\iota\) is unitary. For \(x\ne x'\), \(\{c_xu_x,(c_{x'}u_{x'})^\dagger\}=c_xc_{x'}^\dagger(u_xu_{x'}^*-u_{x'}^*u_x)\), so the \(u_x\) commute. Since \(P_\sigma\) is a minimal projection of the matter algebra, \(P_\sigma\mathcal A_AP_\sigma=P_\sigma\otimes\mathfrak L_A\), and \(P_{\sigma-e_x}c_xP_\sigma\ne0\) gives \(V_{\sigma-e_x}V_\sigma^*=u_x\). In (ii)⇒(i), every factor of \(W_0\prod_{z\ne x}e^{-in_zh_z}e^{-ih_x(n_x+E^o_x)}\) commutes with the odd gate: \(h_x\) and \(n_x+E^o_x\) commute with each other and with the gate.
- **Lemma 4.3.** \([O,H_A]=3^{-1/2}\sum_\ell\eta\,(c_y^\dagger c_x\otimes[O,J_\ell]+c_x^\dagger c_y\otimes[O,J_\ell^\dagger])\). The \(c_y^\dagger c_x\) for distinct ordered pairs are independent. \([J_\ell,J_\ell^\dagger]=2E_\ell\) has simple spectrum, and \(J_\ell\) has nonzero ladder coefficients, so \(J_\ell,J_\ell^\dagger\) generate the full matrix algebra of the link.

### 3.F Fidelity to `B5B_DRAFT.md`

| `B5B.md` | `B5B_DRAFT.md` | Change |
|---|---|---|
| §1 definitions | 1.2, 7.1 | Four-tests (1.3, 7.8) dropped (item 17). "not internal to `A`" became "outside \(A\)" (item 5). |
| Lemma 2.1 | Lemma 2.1 | New proof (both ends of an internal link lie in \(A\)); valid. |
| Lemma 2.2 | G1, G2, G3 | Merged; G3's rank-one step dropped (item 21). |
| Lemma 2.3 | T, T′ | Merged; \(g_{vx}\) dropped (item 27); open values misworded (item 25). |
| Lemma 2.4 | D | Block identities dropped (item 28). |
| Theorem 3.1, Corollary 3.2, line 78 | Theorem B5b, Corollary B5b.1, section 4 | Same content. |
| Theorem 3.3 | Theorem B5b-T | Same; (H1)-(H3) folded in. |
| Proposition 3.4 and the GAP | Proposition 7.2 | Last assertion corrected. The draft's "Invariance of `M_e` alone does not restrict the mode image" (draft line 342) is quoted exactly on line 102. |
| Theorem 4.1 | Theorem 5.1 | Joint-extension requirement added. The draft asks only that "there is an automorphism `κ_x` of `𝒪_A`" (draft line 205). Its proof says "Lemma G1 applies to `κ_x` on `𝒪_A` as well" (draft line 207); that needs \(\kappa_x\) to extend with \(\mathcal A_A\) fixed. The added requirement supplies this. |
| Theorem 4.2 | Proposition 5.2, Theorem 7.3 | Merged; same content. |
| Line 132 | Section 7.6 | "not closed under composition" (draft line 367, unproved) became "need not itself be a group". RC5 proves the draft's form. |
| Lemma 4.3, line 138 | Lemma 7.4, sections 7.6-7.7 | Same. |
| none | 3.1 (sketch), 5.3 (attacks), 6 (downstream), FINISH | Dropped. |

### 3.G Fidelity to the `LW1.md` citations

- Line 9, "LW1 supplies the CAR, finite-spin links, cube Hamiltonians, B3, B4 and the layer automorphisms E1": LW1 lines 35-47 (CAR, links, \(\mathcal G_x\)), 57-62 (cube Hamiltonians, layers), 227 (B3), 231 (B4) and 391 (E1) hold them.
- Line 21, "The law uses \(a_x=a_o\)": LW1 line 62, "\(M_o=\prod_{C\in\mathcal T_o}e^{ia_oH_C}\)".
- Line 23, "At infinite volume these mean LW1 E1's automorphisms": LW1 line 62, "Products at infinite volume mean the local automorphisms of E1."
- Line 98, the odd half-step: LW1 line 64, "\(W_{2n+1}=W_EM_o\)".
- Line 74, "The particle-hole branch of LW1 B3": LW1 line 227, "sends \(c_x\) to \(u c_x\) or \(v c_x^\dagger\)".
- Lines 72 and 130, B4: LW1 line 231, "Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\). So does each oriented quantum-link plaquette monomial."
- Line 126, \(\mathcal G_x\): LW1 line 45.
- Line 5, "the rejected scalar conclusion": LW1 line 245, "Thus the scalar conclusion is false under the stated hypotheses."

### 3.H Four-test results (RC4)

Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its reasons do not need. A reading passes when every answer is no.

| Reading (line) | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| Frame on \(A\) (15) | No: names no group; the group is derived. | No: one closed class of automorphisms. | No: the widest local class; parity, number and mixing with internal links are not assumed. | No. | Pass |
| Split register change (15) | No. | No. | Not as used: the results are stated as conditional (line 5), and R-E is treated separately (Theorem 4.2, B5b-E′). Adopted as the meaning of PS-6's register change, it would decide the R-E case by premise; only the owner adopts. | No. | Pass as a stated hypothesis |
| Odd-gate hypothesis (17-21) | No. | No. | No: LW1's B5(b) hypothesis implies it, so its conclusions hold under LW1's. | No: it uses only the law's gates. | Pass |
| Hypothesis T (23) | No. | No: one automorphism identity. | No: on every finite even torus of side at least four it equals \(\psi(U_0)=cU_0\); at infinite volume it is the meaning LW1 line 62 gives to gate products. | No. | Pass |
| Mode image (25) | No. | No. | No: it only limits when the phrase is used; Theorem 4.2 reports its frames without one. | No. | Pass |
| R-M with the joint extension (21, 106) | No. | No, once "local" is replaced (item 54). | No: an alternative hypothesis, with its answer derived. | No: the extension is needed for \(\varphi\circ\kappa_x\) to act on the gate. | Pass |
| R-E (21, 116) | No. | No: any unitary on finitely many links. | No: an alternative hypothesis. | No. | Pass |

---

## 4. Required edits

Required before freeze. Each is short. None changes a theorem.

1. **Line 13 (item 5).** Replace "all links outside \(A\)" with "all links not internal to \(A\)". Add: "Then \(\mathcal A_A\) and \(\mathcal O_A\) generate the quasi-local algebra."
2. **Line 45 (item 25).** Replace "one weight below the appropriate extremum" with "one step inside the extremum that its first hop moves toward: \(m=S-1\) when the path leaves through the link's source, \(m=-S+1\) when it leaves through the link's target".
3. **Section 1 (item 16).** Add the definition of \(F\)-charge (RC3, section 2.2).
4. **Section 1 (item 17).** Add the four-test results of section 3.H, or a pointer to them.
5. **Line 35 (item 21).** Add RC2: \(\psi(e_{11})\) has rank one because its corner algebra is \(\mathbb C\); \(Ve_i=f_{i1}w\) is unitary and \(Ve_{ij}V^*=f_{ij}\).
6. **Line 47 (item 27).** Add: "Write \(g_{vx}=\langle v|G|x\rangle\) for states \(v\) of the block."
7. **Lines 49-55 (item 28).** State that \(z\) lies in the algebra generated by \(c_x\) and \(\mathcal C\). Add the identities \((1-n_x)zn_x=c_xY\) and \(n_xz(1-n_x)=c_x^\dagger X\), with RC1's proof line.
8. **Line 7 (item 2).** Add the even-layer mode image (the GAP on line 102) to the Open list. Say that the register factors, the exceptional angles and the even-layer mode image are not needed for the mode image results.

Recommended, not required:

9. **Line 33 (item 19).** Name the algebras of \(a_j,a,a'\) and \(b_j,b,b'\). Move the two general facts of the proof (inner automorphisms; the commutant of \(M_n\otimes1\)) into the statement.
10. **Lines 64 and 72 (item 34).** Use the plaquette wording of section 2.3.
11. **Line 66 (item 31).** Cite Lemma 2.4 for \(n_xG(1-n_x)=c_x^\dagger X\).
12. **Line 88 (item 42).** Write out \(\varphi'\), \(L'\), \(\varphi_1\) and \(R\).
13. **Line 90 (item 43).** Write "a neighbour \(y\) of \(x\) in \(O_x\)".
14. **Line 106 (item 54).** Replace "graded local automorphism" with the wording of section 2.3.
15. **Line 132 (item 64).** If the lead imports RC5, write "is not closed under composition (RC5), so it is not a group" in place of "need not itself be a group".
16. **Line 35 (item 22).** Optionally give the explicit extension \(\operatorname{Ad}V\circ\theta_{\rm out}\) for odd \(V\).

---

## 5. Open statements to carry, by name

These are the open statements of `B5B.md`. This report is one check of the proof and attempted no closure of them. The last three are not needed for any mode-image result.

1. **B5b-E′** (`B5B.md` lines 7 and 138). Reading R-E with the even gate added, and reading R-T with register changes not split at \(A\). Facts that bear on it: Lemma 4.3; the step that puts \(M_eLM_e^*\) in \(\mathcal O_A\) fails for an unsplit \(L\) (line 138); and RC5, which shows that the R-E compatible frames of the odd gates are not closed under composition.
2. **Plaquette layer** (lines 7 and 138). An added layer \(W_B\) whose gates join internal links of \(A\) to outside links. The whole-tick proof does not cover it, because \(\gamma_B\) would not respect the cut. It waits on GA1-P (LW1 line 476).
3. **Register factors** (line 7). Which \(W\) and \(L\) go with a given \(\lambda\) under Hypothesis T. Not needed for the mode image.
4. **Exceptional gate angles** (line 7). Whether \(t\mapsto e^{ia_ot}\) fails to be injective on the spectrum of \(H_{O_x}\) inside LW1's window, and the full compensation group at such angles. Not needed for the mode image (line 78).
5. **Even-layer mode image** (line 102). Classify the mode-linear frames compatible with the even layer. Not needed for the mode image results.

---

## 6. Freeze recommendation

Freeze `B5B.md` after the eight required edits of section 4. Every theorem keeps its content. The recommended edits make the text more exact and can go in at the same time. Carry the five statements of section 5 by name. RC5 is a new result of this report; importing it into the frozen text is the lead's choice.

---

## FINISH

**Proved here (referee closures, each written out above).**
- RC1 (section 2.2): the block identities \((1-n_x)zn_x=c_xY\) and \(n_xz(1-n_x)=c_x^\dagger X\) of Lemma 2.4.
- RC2 (section 2.2): every \(*\)-automorphism of \(M_n(\mathbb C)\) is \(\operatorname{Ad}V\) for a unitary \(V\), with the rank-one step and the implementation check.
- RC3 (section 2.2): the \(F\)-charge convention, and with it the charge values of Lemma 2.4 and Theorem 3.3.
- RC4 (section 3.H): every reading of `B5B.md` section 1, and the R-M requirement of Theorem 4.1, passes the four tests as a stated hypothesis.
- RC5 (section 2.4): the set of frames compatible with the odd gates under reading R-E is not closed under composition, so it is not a group.
- Section 2.3: the explicit extension \(\operatorname{Ad}V\circ\theta_{\rm out}\) of an odd implementer; and, given Lemma 2.2, the R-M joint extension holds exactly when each \(\kappa_x\) preserves parity.
- Checked by re-derivation, not new: Lemmas 2.1-2.4, Theorem 3.1, Corollary 3.2, Theorem 3.3, Proposition 3.4, Theorem 4.1, Theorem 4.2 and Lemma 4.3 of `B5B.md` hold as stated under the definitions of section 1, read as in item 5.

**Counterexamples.**
- RC5: \(\varphi_1=\operatorname{Ad}e^{-i(\pi/2)n_xE_m}\) and \(\varphi_2=\operatorname{Ad}e^{-i(\pi/2)n_{x'}S^x_m}\), with \(x\ne x'\) corners of \(A\) and \(m\) an internal link. Each is R-E compatible for the odd gates; \(\varphi_1\circ\varphi_2\) is not, for every \(S\).
- No counterexample to any theorem of `B5B.md` was found.

**Open, by name.** B5b-E′; the plaquette layer (waits on GA1-P); the register factors, the exceptional gate angles and the even-layer mode image, none needed for the mode image (section 5).

**What changes downstream.**
- `B5B.md` can be frozen after the eight required edits; no theorem changes.
- `CH1_DRAFT.md` line 414 records the owner's D1 decision "on the named step of `B5B_DRAFT.md` (Theorems B5b and B5b-T)". These are Theorems 3.1 and 3.3 of `B5B.md`. This referee pass finds both correct, under register changes split at the cell.
- `CH1.md` line 73 (at `b05ee6430`) says "its cell-frame B5(b) remains open in the frozen text. The stronger B5B draft has its own hypotheses." After the freeze it can cite the frozen `B5B.md` for cell frames under the split readings. Reading R-E stays open as B5b-E′.
- `CH1_DRAFT.md` line 25 names reading R-E as what remains open. RC5 adds that under R-E the compatible frames of the odd gates form no group. So a frame-group statement under R-E needs an owner specification first.
- No axiom, reading or working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
