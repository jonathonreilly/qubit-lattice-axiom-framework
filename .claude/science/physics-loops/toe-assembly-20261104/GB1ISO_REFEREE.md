lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1ISO referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 (referee) under PR #10138's method. Claude drafted pass 1 (`GB1ISO_DRAFT.md`). Codex gpt-6.1-terra distilled pass 2 (`GB1ISO.md`). This session wrote neither. This is one check: one whole-part, line-by-line read of `GB1ISO.md`. No review of this review was commissioned.

**Text read.** `GB1ISO.md` as of commit `0df69c033` (the last commit that touches it; branch head `0df69c033` when read), all 150 lines. SHA-256 of the file read: `5875dd4b0166b9742557dbe5604b508656e88715b5f6b9ff8e0fc852b8beb2e1`. Line numbers below refer to that file.

**Sources read, with commits.** All on local branch `claude/toe-assembly` at `0df69c033`, this folder. `GB1ISO_DRAFT.md` (last changed `5beff0f51`; SHA-256 `cbde65e4...32e6c9bba`, the hash `GB1ISO.md` line 15 records), all 352 lines. `prior/GB1ISO.md` (SHA-256 `e35dee0a...2b194c7d`, the hash line 15 records), all 91 lines. `LW1_REFEREE.md` lines 1-80 (format only). `Y2W_DRAFT.md` lines 1-30 (format only). Further source lines are listed where they are used (§2 below gives the full list).

**Method.** Every proof was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-GB1ISOref/`, under a minute and a few MB, started only at 50 percent or more free memory. It guides only and proves nothing. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step. A "referee repair" replaces a false or unproved line by a proved one.

**Working-set entries used.** None as a premise. The objects are the proposed SU(2) test family of `GB1QL.md` §1.3 and its two proposed Euclidean lifts of `GB1E.md` §1, under the readings R-SUM and R-IA (`GB1_GEN_OWNER_CHECK.md`; owner direction `TOE_ASSEMBLY.md` §3.11: probe each, adopt none). Nothing is adopted here. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The test family, R-SUM, R-IA and T0-start[G] are read plainly.

---

## 0. Sources checked, and prior work used

**Source lines checked against `GB1ISO.md`.** This folder at `0df69c033`: `GB1E.md` lines 13 (GAP 2), 21-38 (§1: box, \(\mathcal K\), \(H_k\), \(E^2\), \(P_0\), \(CF\), \(B_p\), the transfer-kernel lift, \(k_t\), \(\mu_{\rm loc}\) with \(W_{xy,r}\), \(\mu_{\rm ex}\)), 60-62 (Theorem 3.1), 72-80 (Theorem 3.2 and proof), 96-99 (§4 grades of R-SUM, R-IA, R-ISO), 131-139 (Theorem 6.1), 145-164 (Theorems 7.1, 7.2 and the sign-field remark), 176-180 (Theorem 7.3 and its scope), 218. `GB1E_REFEREE.md` line 208 (GB1E-ς and its attacks (A)-(C)). `GB1QL.md` lines 60-72 (§1.3, the two ticks and the plaquette ordering). `GB1.md` lines 33 (Definition 5), 41, 59 (Theorem 2.2 proof), 71, 109 (GB1-CF), 231. `GA1_5.md` lines 67 (Theorem 2.1), 77 (Theorem 2.2). `GB1_GEN_OWNER_CHECK.md` lines 21, 27-32, 38-44. `GA2_Y2_DRAFT.md` lines 203-215 (T0-start[G], T0-rate). `GA2_Y2.md` lines 170-178. `TOE_ASSEMBLY.md` lines 233-235 (NN-a text, cell group) and 269. `GB1E.md` lines 135-139 (the crossing-kernel and sign-field steps of Theorem 6.1). `GB1QL.md` lines 299-303 (Proposition 4.11). `GB1.md` lines 172-174. `LW1.md` line 38 (\(c_0=\mathbf1/2\)). YM branch `origin/claude/ym4d-hard-route`, fetched 2026-11-07, head `199af1c7e` (pass 1 read head `db91945e3e`): `.claude/science/physics-loops/ym4d-hard-route-20261030/GOAL.md` lines 20-48 (T0, NT1, NT2). No other branch was read; the consolidation-branch and main-branch lines that `GB1ISO.md` §7 cites are context only and are not used in any verdict below.

**Prior work used** (each with its path; each used at its stated scope, nothing re-derived unless said).

- `GB1E.md` (frozen): §1 definitions; Theorem 2.2 (\(k_t\) continuous, the convolution kernel of \(e^{-tE^2}\)); Theorem 3.1 (\(T_{\rm loc}=Me^{-tA}M\)); Theorem 3.2 (Trotter convergence, the kernel upper bound, existence of \(\mu_{\rm ex}\)); Theorem 6.1 (CF parity under coordinate reflections); Theorem 7.1 (\(z_k\); no heat kernel is a Wilson weight near the identity); Theorem 7.2 (local lift never exchange invariant; exact lift at \(\theta=0\)). Used to check `GB1ISO.md` Theorems 2.2-2.4, 4.1 and 6.1.
- `GB1E_REFEREE.md` §3.2 line 208: the three failed attacks (A)-(C) on GB1E-ς. Used to check that Theorem 4.1's step is new.
- `GB1QL.md` §1.3 and `GB1.md` Definition 5 and Theorem 2.2, with `GA1_5.md` Theorems 2.1-2.2: the cube structure of the tick. Used to check Theorems 2.1 and 3.1.
- `GA2_Y2_DRAFT.md` line 211 (T0-start[G] (i)-(ii)) and line 213 (T0-rate); YM `GOAL.md` lines 30-31 (NT1, NT2). Used in §3 below to decide the class-independent claim.
- `prior/GB1ISO.md` (the digest). Its "Failed attempts on file" list was checked against Theorem 4.1 and ISO-FP: no failed attempt is repeated without a new step.

**Prior work the digest missed.** Nothing beyond what `GB1ISO_DRAFT.md` §1 already adds (its items (1)-(5)), which this referee confirms at the cited lines: `GB1.md` line 33, `GB1.md` line 59, `GA1_5.md` line 77 and `GB1.md` line 109 say what the draft quotes.

---

## 1. Verdict table

**Counts.** 41 items: 37 CORRECT, 0 ERROR, 4 INCOMPLETE. The distiller marked five GAP blocks (items 3, 4, 24, 26, 30). They state three gaps: asymptotic isotropy (items 3, 24), T0 admission (items 3, 30) and maximum-weight configurations (items 4, 26). All three are real. Each gets a ruling and a referee repair in §3. No INCOMPLETE item changes the content of a theorem.

| # | Item (`GB1ISO.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status and scope (5) | CORRECT | Selects no law, reading, vacuum or axiom. |
| 2 | §0 "Proved here" list (7) | INCOMPLETE | The Theorem 5.2 summary drops its state hypothesis. Fix: "... obtained from uniformly bounded-range observables **in equal-sided (volume-first) limit states** ...". |
| 3 | §0 GAP asymptotic isotropy and T0 admission (9) | CORRECT | Gap real. Ruling and referee repair in §3.1-§3.3. |
| 4 | §0 GAP maximum-weight configurations (11) | CORRECT | Gap real. Referee repair in §3.4. |
| 5 | §0 Open by name (13) | CORRECT | Each named item is open below or in a cited file. |
| 6 | §0 provenance (15) | CORRECT | Both recorded SHA-256 values match the files read. |
| 7 | §1 box, gauge action, \(P_0\) (19) | CORRECT | Matches `GB1E.md` lines 21, 25. |
| 8 | §1 cubes, \(B_p\), \(A\), \(k_t\) (21) | CORRECT | Matches `GB1E.md` line 27 and `GB1QL.md` §1.3. |
| 9 | §1 R-SUM, R-IA, R-ISO, transfer-kernel lift (23) | CORRECT | \((\beta,t)=(-2\lambda\theta,\lambda\tau_E)\) gives \(\beta H_B/4=-\lambda\theta H_B/2\), as in `GB1_GEN_OWNER_CHECK.md` lines 38-44. Grades match `GB1E.md` lines 96-99. |
| 10 | §1 \(\mathcal G_\square\), window, \(\widetilde F\), cube support, equal-sided limits (25) | CORRECT | One sentence is vacuous: a gauge-invariant function of temporal links alone, in a window shorter than \(N_t\), is constant (temporal gauge sets those links to 1). Edit E3. |
| 11 | Theorem 2.1, statement (29-35) | CORRECT | `[check]` \(N=4\): 16 cubes, each of 192 links in one cube, each site a corner of two. |
| 12 | Theorem 2.1, proof (37) | INCOMPLETE | The face clause proves that a tiling cube contains each \(CF\) face, not that only one does. \(H_B=\sum_CB_C\) needs uniqueness. Fix: "the parity condition then fixes the third base coordinate, so the cube is unique" (draft Lemma 3.1(b)). `[check]`: each \(CF\) face lies in exactly one cube. |
| 13 | Credits (39) | CORRECT | `GA1_5.md` line 67, `GB1QL.md` §1.3, `GB1.md` line 59, `GA1_5.md` line 77 say what is credited. |
| 14 | Theorem 2.2, heat-kernel positivity (41-47) | CORRECT | Re-derived: \(P(q^2z)=P(z)/(qz)\), \(c_{m+1}=q^{2m+1}c_m\), \(c_0=P(1)/\vartheta(0)>0\), log-derivative formula. The endpoint step needs continuity of \(k_t\); cite `GB1E.md` Theorem 2.2 there (edit E4). `[check]` agrees. |
| 15 | Theorem 2.3, positive cube transfers (49-51) | CORRECT | The exact-kernel lower bound is new; it follows from `GB1E.md` Theorem 3.2's proof with \(e^{-sW/2}\ge e^{-s\Vert W\Vert /2}\). "Real top eigenvector": the top eigenspace is spanned by real vectors because the kernel is real; say so (edit E4). |
| 16 | Theorem 2.4, temporal-gauge formula (53-55, 59) | CORRECT | Checked against `GB1E.md` line 29 and line 36: the density is invariant under \(U_r\mapsto G_r\cdot U_r\), \(V_r\mapsto G_{r+1}^{-1}V_rG_r\); the choice \(g_{r+1}=V_rg_r\) sets the window's temporal links to 1. |
| 17 | Theorem 2.4, slice symmetry commutes with \(TP_0\) (57, 59) | CORRECT | Cycle lemma re-derived: \(f(x,y)=-a(x)-a(y)-(n-3)c\), then \(2a=-(n-2)c\), then \(c=0\). Needs \(N_t\ge3\), given. |
| 18 | Theorem 3.1 (63-65) | INCOMPLETE | "the other cube-face rungs" is unnamed. Fix: name them (draft §8.3: the \(U(1)\) rung of `GB1.md` Theorems 5.1, 5.2, 5U; the \(SU(2)\) rung of Theorem 6.1; `GB1QL.md` \(U_{(s)}\)) and the property used: cube magnetic gates, single-link electric gates, and hop layers that act as the identity on empty matter (`GB1.md` Theorem 2.2). |
| 19 | Theorem 3.2 (67-82) | CORRECT | Re-derived: \(\mathbb EF=(\omega_\infty(F)+e_1)/(1+e_2)\) with \(\lvert e_1\rvert \le\Vert F\Vert _\infty\delta_N\), \(0\le e_2\le\delta_N\), so the error is at most \(2\Vert F\Vert _\infty\delta_N\). Covariance formula and its positivity checked; \(B_C=24\) and \(8\) `[check]`. |
| 20 | Theorem 3.3 (84-86) | CORRECT | The bound of Theorem 3.2 is uniform over \(\Vert F\Vert _\infty\le1\) at fixed window and support, so each finite marginal converges in total variation; this also covers measurable, not only continuous, local functions. |
| 21 | Theorem 4.1 (90-92) | CORRECT | Closes GB1E-ς at the stated finite-torus scope. Details in §2. |
| 22 | Remark on the new step (94) | CORRECT | The step (conjugating the time translation, then the cycle lemma) is none of attacks (A)-(C) of `GB1E_REFEREE.md` line 208. |
| 23 | Theorem 4.2 (96-98) | CORRECT | The sup-distance is in fact at least \(\tau\); \(\tau\ge2\) already suffices. Harmless. |
| 24 | GAP "no restoration at any scale" (100) | CORRECT | Gap real. Ruling and repaired statement in §3.1. |
| 25 | Theorem 5.1 (104-106) | CORRECT | Re-derived; `[check]` \(N=4\): kernels 112 and 66. |
| 26 | GAP draft F(b), global maxima (108) | CORRECT | Gap real; the \(-I\) example is valid. Referee repair in §3.4. |
| 27 | Remark on `GB1E.md` Theorem 7.3 (110) | CORRECT | |
| 28 | Theorem 5.2, statement (112) | CORRECT | |
| 29 | Theorem 5.2, proof (114) | CORRECT | Re-derived. The same proof allows support radius \(r_k\) with \(a_kr_k\to0\) in place of a fixed radius (§3.2). |
| 30 | GAP block and T0 conclusions (116) | CORRECT | Gap real. Referee repair, conditional on named hypotheses, in §3.3. |
| 31 | FP text (120-123) | CORRECT | A candidate, not adopted. |
| 32 | Theorem 6.1 (125-127) | CORRECT | Multiplicity two re-derived; `[check]` \(N=4\): all 192 plaquettes twice. Exchange step re-derived (§2). |
| 33 | FP symmetry, finite register, four tests (129) | CORRECT | Ruling on FP and its admissibility in §2. |
| 34 | ISO-FP and its three attacks (131) | CORRECT | Ruling in §2. Edit E8: write ISO-FP as a statement. |
| 35 | FP classical dictionary (133) | CORRECT | Re-derived from `GB1E.md` Theorem 7.3's matching with stiffness \(\beta=2\lambda\lvert\theta\rvert \) on every spatial plaquette. |
| 36 | T0-start^an[G] and its tests (135) | CORRECT | Ruling in §2. |
| 37 | Y-a to Y-d (137-140) | CORRECT | Obligations, not claims. |
| 38 | D4 and the regrade proposal (142) | CORRECT | Proposals only; `GB1.md` unchanged. |
| 39 | §7 hand-off (146) | INCOMPLETE | "For other action classes ... the first failing step is not determined" is right as written, but §3.3 now decides it under named hypotheses. Edit E6 adds that sentence. |
| 40 | §7 digest results (148) | CORRECT | Context only; no verdict here depends on them. |
| 41 | §7 evidence limits (150) | CORRECT | This referee reran the counts and the heat-kernel figures (`[check]`, §4). |

---

## 2. Rulings on the named items

### 2.1 Theorem D: both lifts factorize over tiling cubes (items 11-20)

**Verdict: CORRECT, at every parameter of both readings.** Theorem D of the draft is split in `GB1ISO.md` into Theorems 2.1, 2.3, 3.1, 3.2 and 3.3. I re-derived each step. The tick, \(e^{-a_0H}\) and \(T_{\rm loc}\) are tensor products over the cubes of one tiling, because each magnetic gate acts on the twelve links of one cube, each electric gate on one link, and the cubes partition the links. Each cube transfer has a kernel between positive constants (Theorem 2.3, which rests on Theorem 2.2). So each has a simple top eigenvalue with a positive, corner-gauge-invariant eigenvector. The product of these eigenvectors is gauge invariant, so the Gauss projection \(P_0\) does not see it. The equal-sided limit is then the product state, with the explicit error \(2\|F\|_\infty\delta_N\).

**"The spatial propagation speed is exactly zero."** `GB1ISO.md` does not use this phrase; the draft does (draft line 214). As a phrase it has no definition. Three precise statements carry it, and all three are proved:

- (S1) *Real time.* For every \(n\in\mathbb Z\) and every operator \(X\) supported on the cube factors \(S\), \(U_{KS}^{-n}XU_{KS}^n\) is supported on \(S\) (Theorem 3.1). The tick moves nothing from one tiling cube to another, at any time. Its Lieb-Robinson velocity is exactly zero.
- (S2) *Euclidean.* In the limit state \(\omega_\infty\) of either lift, \(\operatorname{Cov}(F,G)=0\) whenever \(S(F)\cap S(G)=\varnothing\), at every time separation (Theorem 3.2). Connected correlations end at sup-distance two. In time, \(0<\operatorname{Cov}(B_C(0),B_C(\tau))\le q^\tau\operatorname{Var}(B_C)\) for every \(\tau\ge0\).
- (S3) *Classical.* The linearized cube-face flow has flat bands, so every group velocity is zero (Theorem 5.1).

Edit E5 adds (S1)-(S2) as a named corollary, so that the phrase never stands alone.

### 2.2 Theorem A (Theorem 4.1) and strict heat-kernel positivity (Theorem 2.2) (items 14, 15, 17, 21, 22)

**Verdict: CORRECT. GB1E-ς is closed at its stated scope: even cubic four-torus \(N=N_t\ge4\), every \(\theta\in\mathbb R\), \(\tau_E,a_0>0\).** The proof chain, re-derived:

1. \(\mu_{\rm ex}\) is invariant under the unit time translation, since its density is a cyclic product.
2. If an isometry \(g\) maps time to \(\pm e_i\), invariance under \(g\) gives invariance under \(g\tau_tg^{-1}=\tau_{\pm e_i}\), which acts slice by slice.
3. The kernel of \(e^{-a_0H}\) is a product of cube kernels. Each lies between \(e^{\mp24a_0|\theta|}\prod_{\ell\in C}k_{a_0\tau_E}(U_\ell U_\ell'^{-1})\), and \(k_{a_0\tau_E}\ge m_{a_0\tau_E}>0\) by Theorem 2.2. So the gauge-averaged kernel \(\bar\kappa\) is symmetric and lies between positive constants. Without strict positivity of \(k_t\) (`GB1E.md` Theorem 2.2 gives only "positive near the identity"), \(\log\bar\kappa\) could be unbounded and the cycle lemma would not apply. So Theorem 2.2 is load-bearing here, and its proof is complete.
4. The cycle lemma (Theorem 2.4, second part) turns invariance of the spatial marginal \(\prod_r\bar\kappa(U_r,U_{r+1})\) under the translation into \(\bar\kappa(sx,sy)=\bar\kappa(x,y)\) a.e., that is \([R,TP_0]=0\).
5. On \(P_0\mathcal H\), \(e^{-a_0H}\) is positive and injective, so \(R\) commutes with its spectral projections and hence with \(H|_{P_0\mathcal H}\). \(R\) commutes with \(A\) and fixes the constant function \(1\in D(A)\cap P_0\mathcal H\). Applying \(RHR^{-1}=H\) to \(1\) gives \(\theta(H_B\circ\tau^{-1}-H_B)=0\).
6. A unit translation along \(e_i\) flips the parity of the \(i\)-th base coordinate, so it moves every \(CF\) face in a plane containing \(e_i\) off \(CF\) (`[check]` \(N=4\), all three directions). Distinct plaquette traces lie in orthogonal flux subspaces and are nonzero. So \(H_B\circ\tau^{-1}\ne H_B\) and \(\theta=0\), against the case assumption.

The step is new against `GB1E_REFEREE.md` line 208: it adds no observables (A), uses no convexity (B) and needs no spatial Markov property (C). Theorem 2.2's triple-product proof: I checked \(P(q^2z)=P(z)(1+q^{-1}z^{-1})/(1+qz)=P(z)/(qz)\), the recursion \(c_{m+1}=q^{2m+1}c_m\), and \(\frac{d}{d\psi}\log(1+2r\cos\psi+r^2)=-2r\sin\psi/(1+2r\cos\psi+r^2)\). Each denominator is at least \((1-r_n)^2>0\). Continuity of \(k_t\) (`GB1E.md` Theorem 2.2) carries the formula to \(\psi\in\{0,\pi\}\).

### 2.3 FP, the four-tiling magnetic layer, and its admissibility (items 31-33, 35)

**Verdict: the FP statements of `GB1ISO.md` are CORRECT. Admissibility is established only on the infinite-register target, for gauge invariance and cell covariance. FP is not adopted; only the owner adopts.**

- *Counting.* A face in plane \((i,j)\), third axis \(k\), base \(y\), lies in \(\mathcal C+v\) iff \(y_i-v_i\equiv y_j-v_j\). If \(y_i\equiv y_j\), exactly \(v\in\{0,e_k\}\) qualify; otherwise exactly \(v\in\{e_i,e_j\}\). So every face appears twice, and \(\sum_v\sum_{C\in\mathcal C+v}B_C=2\sum_pB_p\). The four tilings together contain every unit cube exactly once.
- *Target form.* On \(L^2(SU(2))\) links every \(B_C\) is a multiplication operator, so the four layers commute and \(W_B^{FP}=e^{-i\theta\sum_pB_p}\).
- *Exchange.* With one link \(g\) and all others \(1\), the R-IA density is proportional to \(e^{4\beta\operatorname{Tr}g}k_t(g)^2\) for a spatial link and to \(k_t(g)^6\) for a temporal link; the other plaquettes contribute \(g\)-independent constants. Equality of the two continuous densities forces \(k_t(g)^4\propto e^{4\beta\operatorname{Tr}g}\), so \(k_t\) would be a Wilson weight, which `GB1E.md` Theorem 7.1 excludes near the identity. This holds at \(\beta=0\) too.
- *Covariance.* The owner's cell group is \(\mathcal G=2\mathbb Z^3\rtimes O_{c_0}\), \(c_0=\mathbf1/2\) (`TOE_ASSEMBLY.md` line 235, NN-a text). The tiling \(\mathcal C\) alone is already \(\mathcal G\)-invariant: \(O_{c_0}\) fixes it, and its reflections fix each \(\mathcal C+v\). Its coordinate permutations permute \(\mathcal C+e_1,\mathcal C+e_2,\mathcal C+e_3\). So cell covariance does not force any shifted tiling. It forces all three once one of them is used. Then one coupling for all plaquettes forces equal weights: with weight \(w_0\) on \(\mathcal C\) and \(w_s\) on each shift, a \(CF\) face gets \(w_0+w_s\) and any other face \(2w_s\). That is the content of the draft's test-4 reason, and the distiller's caveat ("only an argument within this chosen four-tiling ansatz") is exact.
- *Finite registers.* Gates of different tilings share links. On the finite registers \(R_s\) their plaquette operators need not commute (`GB1.md` line 109). So neither the full-sum form nor the point-group covariance of the ordered product follows. This is GB1-CF, open.
- *NN-a.* The draft announced an NN-a check of FP (draft line 23). Neither pass performs one, and `GB1ISO.md` claims none. No verdict depends on it. It belongs to GB1-CF's "admissible finite-register update".
- *Four tests C P P P.* I agree. Test 1 is C: FP is built so that its target form is the Kogut-Susskind magnetic term, which aligns law data with the bridge's comparison target. It would be F only if FP were used as a premise to settle GB1-CF, and it is not. Tests 2-4 pass for the reasons the text gives, with the covariance reading above.

### 2.4 T0-start^an[G] and its four tests (items 36, 37)

**Verdict: CORRECT as an open request; grades P C P P agreed.** The request asks the YM side for CT1-CT4 uniformly in \(\xi\), convergence of the time-rescaled \(\operatorname{tr}F^2\) sector to T0's theory up to scale, and T0-rate for the rescaled correlations. It claims nothing. Test 2 is C for two reasons, not one: the class is the unpinned hard-core class, and the anisotropy parameter \(\xi\) is never defined (the classical \(\xi_{cl}\) of line 133 is one candidate). Edit E7 asks the text to say so. The proposed symmetry list is what FP lifts are designed to have; for (P8.1) at \(\beta<0\) the sign field of `GB1E.md` line 137 flips every spatial plaquette, so it serves FP as well as \(CF\). That RP argument rests on `GB1E.md` Theorem 6.1, whose crossing-kernel step is cited there from the YM branch as "not independently checked"; this request inherits that scope.

### 2.5 ISO-FP and its three failed attacks (item 34)

**Verdict: correctly carried as an open lemma with three distinct failed attacks.**

1. *Port RO1.* Fails at H-L: under FP the R-IA lift is not exchange invariant (Theorem 6.1), so the time-space diagonal mirrors are not symmetries, and \(D_c\sigma D_c^{-1}\) is not a lattice map for \(c\ne1\).
2. *Tree-level matching plus finite renormalization.* Fails at non-perturbative control: it gives no bound on long-distance correlations.
3. *Sussman-Alpoge Ward route.* Fails at the decay exponent \(c_1>1/2\), recorded on the YM branch as "assumed" with a one-loop law "sketched", and at its unproved use for heat-kernel-in-time starts. The draft's further reason, "An FP lift has an anisotropy of order one", is not established. At the tree-level isotropic FP step, \(c_{\lambda\tau_E}=2\lambda|\theta|\), the classical anisotropy is exactly 1; the crossing exists and is unique for \(\theta\ne0\) by the argument of `GB1E.md` Theorem 7.3 with \(|\theta|\) replaced by \(2|\theta|\) (\(c_{\lambda\tau_E}\) decreases strictly in \(\lambda\), while \(2\lambda|\theta|\) increases). The distiller dropped this reason correctly.

The three attacks use different tools (mirror RP, perturbation theory, Ward identities). None proves impossibility. The R-SUM finite-torus exchange question under FP is correctly placed inside ISO-FP: the cycle-lemma proof of Theorem 4.1 conjugates the time translation to a spatial translation, which is already a symmetry of \(H^{FP}\), so it gives nothing there.

---

## 3. The distiller's GAPs: rulings and repairs

### 3.1 GAP "no restoration at any scale" (items 3, 24): real

The draft's lines quoted: "No rescaling of time, by any factor, makes these two families of correlations match: a vanishing function cannot be rescaled into a positive one. The anisotropy does not shrink with distance." (draft line 214). The first sentence is true at every finite lattice separation. The second has two readings. Read as a ratio of temporal to spatial covariance, it is true: the ratio is \(+\infty\) at every separation. Read as a difference, it is false: by Theorem 3.2, \(\operatorname{Cov}(B_C(0),B_C(\tau))\le q^\tau\operatorname{Var}(B_C)\to0\), so both covariances tend to zero. "No restoration at any scale" therefore needs a definition, and the distiller is right that strict positivity at each finite \(\tau\) proves no nonzero anisotropy at infinite separation.

**What is proved, stated exactly** (referee restatement; each clause is proved in `GB1ISO.md` or in §3.2-§3.3 below).

- (R-a) *Fixed lattice.* At every parameter of either reading, \(\omega_\infty\) is not invariant under any lattice isometry exchanging time and space (Theorem 4.2).
- (R-b) *Ratio.* At every parameter and every \(\tau\ge2\), the temporal covariance of \(B_C\) at \(\tau\) is positive, while every covariance of cube-disjoint observables is zero, at every time separation (Theorem 3.2).
- (R-c) *Continuum, two points.* Take any sequence of parameters and spacings \(a_k\to0\), the volume-first states \(\omega_\infty\), and bounded gauge-invariant local densities of fine spatial support radius \(r_k\) with \(a_kr_k\to0\), with any deterministic normalization. If their separated connected two-point functions converge to a distribution invariant under \(D_cSO(4)D_c^{-1}\) for one \(c\in(0,\infty)\), the limit is zero on all separated tests (Theorem 5.2, with the radius extension of §3.2).
- (R-d) *Continuum, all points.* Under the same hypotheses, every truncated \(n\)-point limit, \(n\ge2\), vanishes at pairwise distinct points (Lemma R2, §3.2).

**What Theorem 5.2 excludes, exactly.** It excludes one thing: a nonzero, \(D_cSO(4)D_c^{-1}\)-invariant limit of separated connected two-point functions, along any parameter sequence, in volume-first limit states, for fine-local bounded gauge-invariant densities with any deterministic normalization. It does not exclude: (i) the zero limit, which is invariant; (ii) nonzero anisotropic limits, for example temporal correlations that survive a tuned \(\lambda_1/\lambda_0\to1\), since these are not restoration; (iii) limits through torus states not close to \(\omega_\infty\) in the normalized sense of §3.3 (P1); (iv) observables whose fine support grows like \(1/a_k\); (v) contact terms supported on coinciding points. So "isotropy is never restored" is proved in the sense (R-c)-(R-d): no nonzero (rescaled-)isotropic separated continuum limit exists under those hypotheses. Edit E1 replaces the status-line wording by (R-a)-(R-d).

### 3.2 Two extensions of Theorem 5.2

**Extension 1 (support radius).** In Theorem 5.2, "spatial support within a fixed number of fine lattice units of \(x\)" can be replaced by "within \(r_k\) fine units, with \(a_kr_k\to0\)". *Proof.* The proof of Theorem 5.2 uses the radius only through the condition that, for test supports whose spatial projections are at distance \(d>0\), every pair \(\rho_k(x),\rho_k(y)\) has spatial supports at sup-distance at least 2. That holds once \(a_k(2r_k+2)<d/\sqrt3\), which is true for large \(k\) when \(a_kr_k\to0\). □ This covers block images after any number \(j_k\) of block steps of side \(L\) with \(L^{j_k}a_k\to0\), and block maps whose block variables are gauge invariant and depend on fine links within a bounded number of blocks. It does not cover blocks of fixed physical size.

**Lemma R2 (all truncated functions).** Fix parameters. If \(F_1,\dots,F_n\) are bounded local gauge-invariant observables with pairwise disjoint cube supports, then \(\omega_\infty(F_1\cdots F_n)=\prod_i\omega_\infty(F_i)\). Hence every joint cumulant \(\omega_\infty^T(F_{i_1},\dots,F_{i_m})\), \(m\ge2\), of distinct members vanishes.

*Proof.* Take one time window containing all \(F_i\). Setting its temporal links to \(1\) gives \((F_1\cdots F_n)^\sim=\widetilde F_1\cdots\widetilde F_n\), because each \(F_i\) depends only on temporal links inside its own window. The chain kernel is a product over cubes (Theorem 2.1) and \(\widetilde F_i\) depends only on cubes in \(S(F_i)\), so the chain operator is \(\bigotimes_i\mathfrak F_{i,S(F_i)}\otimes T^w_{\rm rest}\). Its expectation in \(\Omega=\bigotimes_C\Omega_C\) factorizes, and a longer window changes \(\omega_\infty(F_i)\) by factors \(\lambda_0^{-1}T_C\Omega_C=\Omega_C\) only. Hence the \(F_i\) are independent under \(\omega_\infty\) as a family, and a joint cumulant of \(m\ge2\) independent variables is zero. □

**Corollary R2' (truncated continuum limits).** Under the hypotheses of (R-c), let \(O_k(f)=a_k^4\sum_xf(x)\rho_k(x)\). Suppose that for each \(n\ge2\) the truncated functions \(\omega_\infty^T(O_k(f_1),\dots,O_k(f_n))\), for test functions with pairwise disjoint supports, converge to a distribution \(S_n^T\) on the set \(\Delta_n^c\) of pairwise distinct \(n\)-tuples, and that each \(S_n^T\) is invariant under \(Q\in D_cSO(4)D_c^{-1}\) acting on all points at once. Then \(S_n^T=0\) on \(\Delta_n^c\).

*Proof.* (1) If the spatial projections of the supports of \(f_1,\dots,f_n\) are pairwise at distance \(d>0\), then for large \(k\) every tuple \(\rho_k(x_1),\dots,\rho_k(x_n)\) with \(x_i\in{\rm supp}f_i\) has pairwise disjoint cube supports, by Extension 1. Multilinearity and Lemma R2 give \(\omega_\infty^T(O_k(f_1),\dots,O_k(f_n))=0\) exactly. (2) A partition of unity and density of finite sums of tensor products in \(C_c^\infty\) of a product of open sets show that \(S_n^T\) vanishes on the open set \(W_n\) of tuples whose spatial parts are pairwise distinct. (3) Take \((x_1,\dots,x_n)\in\Delta_n^c\) and put \(v_{ij}=D_c^{-1}(x_i-x_j)\ne0\). For each pair, the rotations \(R\in SO(4)\) with \(Rv_{ij}\) parallel to \(e_t\) form a closed set with empty interior (a union of two cosets of a three-dimensional stabilizer in the six-dimensional group). A finite union of such sets has empty interior, so some \(R\) avoids all of them. With \(Q=D_cR^{-1}D_c^{-1}\), \(Q^{-1}=D_cRD_c^{-1}\), and \(D_c\) fixes spatial parts, so \(Q^{-1}(x_1,\dots,x_n)\in W_n\). Invariance carries the vanishing on \(W_n\) to the open sets \(QW_n\), which cover \(\Delta_n^c\). A distribution that vanishes on each set of an open cover vanishes on the union. □

### 3.3 GAP "block and T0 conclusions" and the class-independent claim (items 3, 30): real; repaired under two named hypotheses

**The claim, quoted.** Draft line 232: "So no family of cube-face lifts, and no family of bounded-range block images of them, can satisfy T0-start's conclusion (ii). T0-rate [...] fails too [...]. This holds for every choice of \(\mathcal A_{k_0}(g)\)". Its argument has two premises it does not prove. (a) It applies Theorem 5.2, a statement about the volume-first states \(\omega_\infty\), to T0-start's measures, which live on tori "of every torus side" (`GA2_Y2_DRAFT.md` line 211), along a trajectory the text does not pin. (b) It uses NT2 with the claim that the leading-order separated action-density two-point function is nonzero; but `GOAL.md` line 31 says "Which correlators, and with what error, is for `parts/witness.md` to propose", and T0-rate's normalization is unpinned. A further point is the distiller's: with \(\operatorname{tr}F^2\) normalized so that its leading two-point value is itself \(O(g^4)\), the error term \(O(g(r)^4)\) of T0-rate would absorb it. **So the unconditional claim is not established, and the GAP is real.**

**The repair removes premise (b) entirely and states premise (a) as a hypothesis.**

- **(P1) State.** The correlations that T0-start (ii) takes "along the hard core's trajectory" are those of states \(\omega_k\), each either the volume-first state \(\omega_\infty[p_k]\) of a cube-face lift (either reading, parameters \(p_k\)), or the equal-sided even torus lift at \(p_k\) with side \(N_k\), such that \(Z_k^n\delta^{(k)}\to0\) for every \(n\). Here \(Z_k=\sup_x\|\rho_k(x)\|_\infty\) and \(\delta^{(k)}\) is the \(\delta_N\) of Theorem 3.2 at \(p_k\), \(N_k\) and the window of the test supports.
- **(P2) Observables.** The \(\operatorname{tr}F^2\) sector is represented by bounded gauge-invariant local densities \(\rho_k(x)\) of fine spatial support radius \(r_k\) with \(a_kr_k\to0\), with any deterministic normalization absorbed into \(\rho_k\).

*Remark on (P1).* At fixed parameters \(p\), Theorem 3.2 gives \(\delta^{(k)}\le\exp\!\big(\tfrac{N_k^3}{4}q^{N_k-w_k-1}\operatorname{Tr}T_C/\lambda_0\big)-1\). So (P1) holds whenever \((N_k-w_k)|\log q|-3\log N_k-n\log Z_k\to\infty\) for each \(n\), for example for \(N_k=L/a_k\), test windows of physical length below \(L\), and any normalization polynomial in \(1/a_k\). (P1) can fail when the parameters move so that \(q_k\to1\) fast; that is why it is a hypothesis.

**Proposition R1 (referee).** Assume (P1) and (P2). Suppose the Euclidean correlations of all orders of \(O_k(f)=a_k^4\sum_xf(x)\rho_k(x)\) in \(\omega_k\) converge on test functions with pairwise disjoint supports to Schwinger functions \(S_n\) that satisfy the Osterwalder-Schrader axioms with Euclidean invariance, where rotation invariance may be weakened to invariance under \(D_cSO(4)D_c^{-1}\) for one \(c\in(0,\infty)\). Then the reconstructed Hilbert space is \(\mathbb C\Omega\). So NT1 fails, T0-start's conclusion (ii) fails for this family, and no class \(\mathcal A_{k_0}(g)\) for which T0-start's conclusion holds along such a trajectory contains the family or its block images of the kind in §3.2.

*Proof.* (1) *Torus case.* For a product \(\rho_k(x_1)\cdots\rho_k(x_m)\), \(m\le n\), Theorem 3.2 bounds the difference between its torus and volume-first expectations by \(2Z_k^m\delta^{(k)}\). The truncated functions are fixed polynomials in these moments, so they differ by at most \(C_nZ_k^n\delta^{(k)}\) (for \(\delta^{(k)}\le1\)), and the smeared ones by at most that times \(\prod_i\|f_i\|_{L^1}(1+o(1))\). By (P1) the torus limits equal the volume-first limits, so it suffices to treat \(\omega_\infty[p_k]\). (2) The moments converge, so the truncated functions converge to the truncated functions \(S_n^T\) of the limit, and these inherit the invariance. Corollary R2' gives \(S_n^T=0\) on pairwise distinct tuples for every \(n\ge2\). (3) Translation invariance makes \(S_1\) a constant \(s\). By the moment-cumulant formula, on pairwise distinct tuples \(S_N=\sum_\pi\prod_{B\in\pi}S^T_{|B|}=s^N\): only the partition into singletons survives. (4) In the OS construction, vectors come from finite sequences \(f=(f_0,f_1,\dots)\) with \(f_n\) supported in \(0<t_1<\dots<t_n\), and \(\langle f,g\rangle=\sum_{n,m}S_{n+m}(\Theta\bar f_n\otimes g_m)\). Every point configuration in these supports has pairwise distinct times, so step (3) applies: \(\langle f,g\rangle=\overline{L(f)}L(g)\) with \(L(f)=\sum_ns^n\int f_n\) (\(s\) is real by the reality axiom). A form of rank at most one gives a Hilbert space spanned by the class of \((1,0,0,\dots)\), the vacuum. The orthocomplement of the vacuum is \(\{0\}\), so "H is not zero on the orthocomplement of the vacuum" (NT1, `GOAL.md` line 30, the same at `db91945e3e` and `199af1c7e`) is false. (ii) asks for a "non-trivial theory (NT1, NT2)", so (ii) fails. □

**Ruling on the class-independent claim.** Its first half, that any rotation-invariant limit (even up to a time rescaling) of these lifts or of their bounded-range block images has a vanishing separated two-point function, is **proved** for volume-first states and fine-local observables (Theorem 5.2 with Extension 1), and extended to all truncated functions (Corollary R2'). Its second half, that T0-start (ii) and T0-rate fail for any class, is **proved under (P1)-(P2)** (Proposition R1). It needs neither NT2 nor any normalization nor the perturbative two-point value. Under (P1)-(P2), T0-rate needs no separate argument: it compares with "the limit in (ii)", which does not exist for this family. Without (P1), the claim is not established. Whether T0-start's pinned trajectory satisfies (P1) for these lifts is part of pinning its class and topology (`GA2_Y2.md` line 178); it is a specification, not an open lemma of this part.

**Status of (P1)-(P2).** They are hypotheses of a conditional proposition. This referee proposes them as no reading and adopts nothing. If the owner or the YM side later pins T0-start, the pinning text gets its own four tests.

### 3.4 GAP "maximum-weight configurations" (items 4, 26): real; repaired

**The draft's line, quoted.** Draft line 218: "In the R-IA Euclidean action with \(\beta>0\), the configurations of maximal weight are, modulo 4D gauge, the static configurations that are pure gauge cube by cube". No proof is given, and temporal holonomy is not mentioned. The distiller's example (spatial links \(1\); temporal links \(1\) except one slice of \(-I\)) has maximal weight and Polyakov loops \(-I\). It is valid.

**Proposition R3 (referee repair).** Let \(\beta>0\), \(t>0\), \(N_t\ge2\). A configuration has maximal \(\mu_{\rm loc}\) density iff \(X_p(U_r)=1\) for every \(p\in CF\) and every \(r\), and \(W_{\ell,r}=1\) for every \(\ell,r\). Modulo 4D gauge transformations, these are exactly the pairs \((U,P)\): a spatial configuration \(U\) that is pure gauge on each tiling cube, and a site field \(P\in SU(2)^\Lambda\) with \(P\cdot U=U\). The representative is \(U_r=U\) for all \(r\), \(V_r=1\) for \(r\le N_t-2\), \(V_{N_t-1}=P\). Two pairs are gauge equivalent iff \((U',P')=(h\cdot U,h^{-1}Ph)\) for some \(h\in SU(2)^\Lambda\) (site-wise products; with this action, \(g\cdot(h\cdot U)=(hg)\cdot U\), so \(h^{-1}Ph\) stabilizes \(h\cdot U\)).

*Proof.* (1) The density is a product of continuous factors, each bounded by its value at the identity, and the identity configuration attains all bounds at once; so the maximum is the product of the maxima, and a configuration is maximal iff each factor is. \(e^{\beta\operatorname{Tr}X}\) is maximal iff \(\operatorname{Tr}X=2\), iff \(X=1\) in \(SU(2)\). \(k_t(g)<k_t(e)\) for \(g\ne e\): from \(z_k(\psi)=(k+1)\sin((k+1)\psi)/\sin\psi\) (`GB1E.md` Theorem 7.1), \(|z_k(\psi)|<(k+1)^2\) for \(k\ge1\) and \(0<\psi<\pi\), and \(z_k(\pi)=(-1)^k(k+1)^2\), so the odd terms make \(k_t(-e)<k_t(e)\). (2) By `GB1E.md` line 36, \(W_{xy,r}=1\) iff \(U_{r+1}=V_r^{-1}\cdot U_r\). (3) Apply the 4D gauge transformation \(G_0=1\), \(G_{r+1}=V_rG_r\) (\(r\le N_t-2\)), under which \(V_r\mapsto G_{r+1}^{-1}V_rG_r\) (item 16). It sets \(V_r=1\) for \(r\le N_t-2\) and \(V_{N_t-1}\) to \(P=V_{N_t-1}\cdots V_0\). Then (2) gives \(U_r=U_0=:U\) for all \(r\), and the wrap-around gives \(P\cdot U=U\). (4) \(X_p(U)=1\) on the six faces of a cube means \(U\) is flat on the cube's boundary, a 2-sphere, which is simply connected; so \(U\) is pure gauge on each cube. (5) The remaining gauge freedom preserving the representative form is a time-independent \(h\), acting as stated. □

For \(\beta<0\), compose with the sign field of `GB1E.md` line 137 (central, time-independent, flips every spatial plaquette, leaves every \(W\) unchanged). For \(\beta=0\), drop the cube condition.

**The strong reading is false.** If "static" means a time-translation-invariant 4D configuration, the claim fails. *Counterexample.* Links in different tiling cubes are independent, so a cube-wise pure-gauge \(U\) can have arbitrary holonomy around non-\(CF\) plaquettes; choose it with holonomy group containing \(i\sigma_1\) and \(i\sigma_2\). Its stabilizer \(\{h:h\cdot U=U\}\) is then \(\{\pm1\}\) (the centralizer of the holonomy group). Take \(P=-1\) and \(N_t\) even. A time-translation-invariant representative would have \(V_r=Q\) for all \(r\), with \(Q\) in the stabilizer of a gauge transform of \(U\), so \(Q=\pm1\) and \(Q^{N_t}=1\), while gauge equivalence requires \(Q^{N_t}\) conjugate to \(P=-1\). So no time-translation-invariant representative exists. Nothing in `GB1ISO.md` depends on either reading; edit E2 replaces the GAP block by Proposition R3.

---

## 4. Checks run by this referee

`[check]` Scripts `/tmp/toe-GB1ISOref/check_ref.py` and `/tmp/toe-GB1ISOref/check_hk.py`, outputs `out_ref.txt` and `out_hk.txt`, run with `python3 -I` at 56 percent free memory; 2.3 s and an 18 MB peak footprint; the largest object is a \(192\times192\) matrix. A check guides and never proves. Results:

- \(N=4\): 16 tiling cubes; each of the 192 links in exactly one; each site a corner of exactly two; the \(CF\) parity rule holds; each \(CF\) face lies in exactly one tiling cube; the flux-map kernels are 112 (\(CF\) faces) and 66 (all plaquettes), matching \(7N^3/4\) and \(N^3+2\).
- FP: all 192 plaquettes have multiplicity 2 in the four tilings.
- A unit translation along \(e_i\) flips \(CF\) membership exactly in the planes containing \(e_i\), for \(i=1,2,3\).
- \(B_C=24\) at the identity configuration and \(8\) with one link \(-1\).
- Heat kernel: the character sum and the product formula of Theorem 2.2 agree to relative \(2\cdot10^{-13}\) or better on \(\psi<1.5\) for \(t=0.2,0.5,1,4\). Evaluated through the triple product, the minimum of \(k_t\) over \([0,\pi]\) is \(3.0\cdot10^{-18}\), \(2.3\cdot10^{-6}\), \(8.8\cdot10^{-3}\), \(0.80\) for those \(t\), and \(4.8\cdot10^{-81}\) at \(t=0.05\), all positive; the Haar integral is \(1.000000\). At \(t=0.05\) the cosine and character sums lose all accuracy where \(k_t\) is tiny, as pass 1 reported; the first-pass script of this referee, which evaluated \(\vartheta\) by its cosine sum, gave \(-1.1\cdot10^{-13}\) at \(t=0.2\) for the same reason. This matches `GB1ISO.md` line 150 and the draft's account. Theorem 2.2 is the proof; the check only agrees with it.

---

## 5. Required edits to `GB1ISO.md`

These are for the lead before freezing. None changes a theorem's content.

- **E1 (line 7 and line 9).** In "Proved here", add the state hypothesis to the Theorem 5.2 summary: "in equal-sided (volume-first) limit states". In the asymptotic-isotropy GAP, replace "no restoration" language by the exact statements (R-a)-(R-d) of §3.1 and the list of what Theorem 5.2 excludes.
- **E2 (lines 11 and 108).** Replace the maximum-weight GAP by Proposition R3 (§3.4), with its \(\beta<0\) and \(\beta=0\) remarks and the counterexample to the time-translation-invariant reading.
- **E3 (line 25).** Replace "Pure temporal local observables may be included after gauge averaging; their temporal-gauge representatives must have finite spatial support." by "A gauge-invariant function of temporal links alone, in a window shorter than \(N_t\), is constant: the temporal gauge sets those links to 1."
- **E4 (lines 37, 47, 51).** Theorem 2.1's proof: add "the parity condition then fixes the third base coordinate, so the cube is unique" (needed for \(H_B=\sum_CB_C\)). Theorem 2.2's proof: cite `GB1E.md` Theorem 2.2 for continuity of \(k_t\) at the endpoint step. Theorem 2.3's proof: add "the kernel is real, so the top eigenspace is spanned by real vectors".
- **E5 (after Theorem 3.2).** Add a corollary stating (S1) and (S2) of §2.1, so that "zero spatial propagation" has a precise meaning: the tick never moves an operator off its cube support, and \(\omega_\infty\) has zero connected correlation between cube-disjoint observables at every time separation.
- **E6 (lines 112-116, 146).** Add Extension 1, Lemma R2, Corollary R2' and Proposition R1 (§3.2-§3.3) with hypotheses (P1)-(P2). Replace the last sentences of line 116 and the sentence "For other action classes and possible RG extensions, the first failing step is not determined" (line 146) by: "Under (P1)-(P2), T0-start's conclusion (ii) fails for these lifts and their block images of §3.2, for every class (Proposition R1). Whether T0-start's pinned trajectory satisfies (P1) is part of pinning its class and topology."
- **E7 (line 135).** State that \(\xi\) is undefined until the class is pinned, as a second reason for the C on test 2.
- **E8 (line 131).** State ISO-FP as a statement, as the draft does: "There are parameter families under FP and either reading, with \(a\to0\), \(c>0\) and \(p>0\), whose volume-first action-density correlations converge to a non-trivial limit invariant under \(D_cSO(4)D_c^{-1}\), at rate \(O((a/r)^p)\)." Keep the three attacks and the distiller's correction of attack (3).
- **E9 (line 129).** Say that the owner's cell group \(2\mathbb Z^3\rtimes O_{c_0}\) already leaves \(\mathcal C\) invariant, so covariance forces the three shifted tilings only once one is used (§2.3); and that no NN-a check of FP was made in either pass.
- **E10 (line 63; table item 18).** Theorem 3.1: name the cube-face rungs and the gate-support property used.

**Required for freeze:** E1, E2, E4, E6, E10 (they close the four INCOMPLETE items and carry the GAP repairs). **Recommended:** E3, E5, E7, E8, E9 (clarity; no proof depends on them).

---

## 6. Open statements to carry by name

- **ISO-FP.** Under FP and either reading, there are parameter families with \(a\to0\), a speed \(c>0\) and an exponent \(p>0\) whose volume-first action-density correlations converge to a non-trivial limit invariant under \(D_cSO(4)D_c^{-1}\), at rate \(O((a/r)^p)\). It includes finite-torus exchange invariance of the R-SUM lift under FP. Three distinct attacks failed, each at a named step (§2.5): (1) RO1 port, at H-L for rescaled diagonal mirrors; (2) tree-level matching plus finite renormalization, at non-perturbative control; (3) the Sussman-Alpoge Ward route, at the unproved decay exponent \(c_1>1/2\) and its unproved use for heat-kernel-in-time starts.
- **T0-start^an[G].** A request to the YM programme, tests P C P P; items Y-a to Y-d. Its \(\xi\) is undefined until its class is pinned.
- **GB1-CF** (carried from `GB1.md` line 109). An admissible finite-register update whose magnetic term is the full plaquette sum. FP answers it only on the infinite-register target; FP's finite-register form and any NN-a check belong here.
- **(H-class) for T0's pinned class.** For the cube-face lifts it is decided negatively, for every class, by Proposition R1 once the pinned trajectory satisfies (P1)-(P2); for a class requiring time-space exchange invariance it is decided by Theorem 4.1 and `GB1E.md` Theorem 7.2. Otherwise it waits for the pinning (`GA2_Y2.md` line 178). This is a specification question, not a lemma of this part.
- Carried unchanged from `GB1ISO.md` line 13, not worked here: the full reflection interface; Y1's local action and selected-state identification; Y2, Y3, E-2, VC1, T0-rate, volume-uniform register convergence.

---

## 7. Freeze recommendation

**Freeze after the required edits E1, E2, E4, E6 and E10.** No item is in ERROR. The four INCOMPLETE items are one-sentence fixes. Every theorem of `GB1ISO.md` is correct as stated: the cube factorization of both lifts (Theorems 2.1-3.3), strict heat-kernel positivity (Theorem 2.2), Theorem 4.1 closing GB1E-ς on the even cubic torus, Theorem 4.2, Theorem 5.1, Theorem 5.2 and Theorem 6.1. The three gaps the distiller marked are real; §3 supplies a repair for each: exact statements for asymptotic isotropy (§3.1), a conditional class-independent theorem (Proposition R1, which uses NT1 only and no normalization), and the maximum-weight classification (Proposition R3). If the lead prefers not to import the referee's results, the part can still freeze with E1-E4 and E10 and with the GAP blocks kept, since the distillation already states the unconditional claims as not established. FP, T0-start^an[G], (P1)-(P2), R-SUM and R-IA remain unadopted; only the owner adopts.

---

## FINISH

**Proved** (checked by this referee, or new here and marked "referee").

- Checked correct, as stated in `GB1ISO.md`: Theorem 2.1 (with the uniqueness line of E4), Theorem 2.2 (strict positivity of the \(SU(2)\) heat kernel, triple-product proof), Theorem 2.3, Theorem 2.4 (temporal gauge; cycle lemma), Theorems 3.1-3.3 (cube-product top state, equal-sided limit with error \(2\|F\|_\infty\delta_N\), factorization of cube-disjoint observables, positive temporal autocovariance, the limit measure), Theorem 4.1 (the exact R-SUM lift is never time-space exchange invariant; GB1E-ς closed on even cubic tori), Theorem 4.2, Theorem 5.1, Theorem 5.2, Theorem 6.1 (FP multiplicity two; full plaquette sum on the infinite-register target; local R-IA lift under FP never exchange invariant).
- Referee, Extension 1: Theorem 5.2 holds with fine support radius \(r_k\), \(a_kr_k\to0\).
- Referee, Lemma R2 and Corollary R2': all truncated \(n\)-point functions of cube-disjoint observables vanish in \(\omega_\infty\), and every \(D_cSO(4)D_c^{-1}\)-invariant truncated continuum limit from fine-local observables vanishes at pairwise distinct points.
- Referee, Proposition R1: under (P1) (volume-first states, or equal-sided tori with \(Z_k^n\delta^{(k)}\to0\)) and (P2) (fine-local densities, \(a_kr_k\to0\), any normalization), every OS limit of these lifts that is rotation invariant up to a time rescaling has a one-dimensional Hilbert space; so NT1 and T0-start's conclusion (ii) fail for every class. No NT2, normalization or perturbative input is used.
- Referee, Proposition R3: the maximum-weight configurations of the R-IA lift are, modulo 4D gauge, the pairs \((U,P)\) with \(U\) cube-wise pure gauge and \(P\cdot U=U\).

**Counterexamples.**

- To the time-translation-invariant reading of draft Proposition F(b) ("static configurations"): at even \(N_t\), a cube-wise pure-gauge \(U\) with stabilizer \(\{\pm1\}\) and \(P=-1\) has maximal weight and no time-translation-invariant gauge representative (§3.4).
- To "the anisotropy does not shrink with distance" read as a difference: \(0<\operatorname{Cov}(B_C(0),B_C(\tau))\le q^\tau\operatorname{Var}(B_C)\to0\) (§3.1). Read as a ratio, the line is true.
- To the draft's "An FP lift has an anisotropy of order one", as a tree-level statement: at the unique \(\lambda\) with \(c_{\lambda\tau_E}=2\lambda|\theta|\) the classical anisotropy is exactly 1 (§2.5).

**Open by name.** ISO-FP (three failed attacks named in §6); T0-start^an[G] (request); GB1-CF; (H-class) for T0's pinned class, decided for the cube-face lifts by Proposition R1 once the pinning satisfies (P1)-(P2); the items carried from `GB1ISO.md` line 13.

**What changes downstream.**

- `GB1E.md`: GB1E-ς is closed on even cubic tori; the exceptional set of its Theorem 7.2 is empty (Theorem 4.1).
- (H-class) for the cube-face lifts, both readings: for a class requiring exchange invariance it fails at every parameter on the torus (Theorem 4.1; `GB1E.md` Theorem 7.2). For any class, it fails under (P1)-(P2) (Proposition R1). The unconditional class-independent claim of the draft is not established; it now reduces to whether T0-start's pinned trajectory satisfies (P1), which is part of the pinning `GA2_Y2.md` line 178 asks for.
- The two readings give the same verdict here, for the same reason: every factor of either transfer lies in one tiling cube. This step does not separate R-SUM from R-IA; R-ISO restores nothing.
- For a pure-gauge route through T0-start under (P1)-(P2), a magnetic layer whose gates leave the cubes of one tiling is necessary; GB1-CF becomes a required input for that route. FP is a candidate (C P P P), not adopted.
- `GB1ISO.md` freezes after edits E1, E2, E4, E6, E10. `docs/MINIMAL_AXIOMS_2026-06-29.md`, the working set and every owner decision are unchanged. Nothing is adopted.
