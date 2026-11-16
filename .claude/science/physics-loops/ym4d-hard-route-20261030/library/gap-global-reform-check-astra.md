# Repo search

OpenAI Codex, GPT-6 (the runtime does not expose a more specific model name or effort). Research check of Claude Fable 5.2's row 1016 at `b82477d39c0b230833d9cf5717ce9d63139ef133`; not an audit and grants no status. No mass gap is claimed. This file checks written mathematics, not GUIDE runs, formal Lean proofs, or the full mass-gap programme.

The target-specific prior file is absent. The November 8 digest was read in full; its searches of main and PRs 10114, 10133, 10134 and 10141 concern earlier ultraviolet and matching targets. They do not establish absence of this November 15 target. Row 1016's own prior-search record (lines 231–265) reports related gauge arguments, auxiliary kernels and samplers, but no AV/BH result in its bounded search. This check reuses the existing arguments rather than opening another proof lane. Searches of `open-registry.md` and `open-core.md` for the target names and pinned-cell/custodial terms found no competing owner of this cross-provider check. Row 1020 is the expressly requested same-provider predecessor, not a reason to repeat its proof work blindly.

| Prior hit checked at source | Closeness and use |
|---|---|
| Row 1011, `gap-pinned-cell-gauge-max.md:131–178,460–485`; row 1013, `gap-invent-selective-max.md:136–173,268–278` | Exact boundary conventions, score and corner algebra, frame identity, and reopen wording. These are credited to Claude Fable 5.2; only the needed mathematical inputs are checked here. |
| Main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | Existing score-integration/Cauchy–Schwarz method, credited to that repository note. Its supplied noncompact Dirichlet Maxwell law is different from AV/BH's compact Wilson pin law; it supplies no BH theorem. |
| PR 10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `agents/ym4d-proof/FINITE_COUPLING_KERNEL_ASTRA.md:1–36` and `UNIFORM_ONE_LOOP_COUPLING_ASTRA.md:179–199,263–290` under `.claude/science/toe-ruleset-20261021/` | Codex/Astra's normalized single-group kernel and colour-invariant jet identities. These are the stiffness/global-colour hits named by row 1011. Different response and observable; no pin-averaged Hessian or custodial reformulation. |
| Sussman–Alpoge outline `394–416`, indexed in chunk 01:45–48 and obligations:14–16 | Already distinguishes preservation of partition functions from identification of observables. Used as the existing scope principle for AUX/MC; not claimed as new here. |
| Outline `13023–13065`, indexed in chunk 12:25–32 | Conditional colour reduction and gauge-Hessian Ward identity at the zero field. Related symmetry algebra, not the arbitrary-pin statement or HW's probe law. |
| CA-I `43997–44065`, indexed in `ca-4.12-4.19/chunk-02.md:12–17` | Conditional covariance of constrained minimizers under gauge changes. Different object; not a global symmetry acting nontrivially on physical observables. |

The outline-index README, matching chunk rows and neighbours, and the relevant obligation rows were read before these bounded source excerpts. The CA-I index README and neighbouring rows were also read. Targeted index searches covered CEN+, AUX/auxiliary kernels, MC/microcanonical rotations, AV/BH/pin averages, Higgs/custodial groups, Hubbard–Stratonovich, Polyakov loops, cube densities, and gauge/Ward identities. These searches are locators, not an exhaustive absence theorem. No source found covers this requested cross-provider check. No Balaban paper is imported. The other branches' unrelated hits in the November 8 digest are not treated as verified premises and were not reopened.

The required FINISH lookup exposed row 1020's summary before this file was written. The full Claude check was kept closed until the independent verdicts below were saved. This is disclosed exposure, not a blind check.

## Working checkpoint

Pinned source: `library/gap-global-reform-max.md`, 1,071 lines. Downloads: `/tmp/sa-gap-global-reform-check-astra.pPcNAZ/`, with outline and CA-I fetched once at Sussman–Alpoge revision `31a47c543775`. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for any reused material. No numerical or symbolic proof run was performed.

1. Complete required rules, prior-work and index reads; fix the scope of W1.
2. Check Identity AV, Theorem BH and their exact finite-volume domains.
3. Check CEN+, AUX and MC, including degeneracies and observables.
4. Check all remaining numbered sections and claims against their proofs.
5. Save independent verdicts and the first failing lines or exact corrections.
6. Read the Claude check; settle every disagreement by an explicit argument.
7. Verify coverage and source citations; finish with one RESULT line.

Completed: independent verdicts, full Claude comparison, source identity, whole-file coverage and final text inspection. The target blob is identical at Opus's `0d3b45d91` and this task's `b82477d39` (`d9211f3efab3c7c9f74601b519c3ee054e3f2852`). No source correction has been applied: the lead's next decision is to carry the explicit repairs into the author file. Only this report is changed, locally on `check/gap-global-reform-astra-b82477d39`; no commit or push is made. No computation discharges a step.

## Independent verdicts, saved before reading the Claude report

Line numbers below refer to `gap-global-reform-max.md` at the pinned commit, unless another file is named.

### 1. Identity AV, §7.1, lines 695–706 — HOLDS

Use the same action, including every `w_p`, in the pinned and fully integrated measures. Write `D` for the fixed left-invariant boundary vector field. Disintegration gives the boundary density `Z/Z_free`, exactly as at line 699. Haar integration gives `∫D²Z=0`. Therefore

\[
\mathbb E_{\rm free}D^2(-\log Z)
=Z_{\rm free}^{-1}\int (DZ)^2/Z
=\mathbb E_{\rm free}(\mathbb E_\omega X)^2.
\]

All derivatives are legitimate on a finite product of compact groups with its smooth Wilson weight. The claimed generality means compact Lie groups with this smooth setup. It does not extend without integrability hypotheses to arbitrary noncompact groups. W1 test (b): YES; using unweighted boundary Haar probability would give the wrong identity.

### 2. Theorem BH, §7.2, lines 721–766 — HOLDS AFTER CORRECTION

The statement (BH), positivity for a boundary plaquette at every `b>0`, the obstruction to a pin-uniform curl bound, and fixed-box growth at least `b/log b` all hold. The following repairs make its written proof complete.

* At lines 733–735, add: the Wilson density is strictly positive everywhere. For a plaquette with four distinct links its Haar holonomy has nonzero imaginary part on an open set. Thus `E(1−t²)>0`, and Step 5 gives `Eψ²=(2/3)E(1−t²)>0` before division.
* Replace line 764's decimal by the exact upper bound
  `e(b) ≤ [16W + 2L log(3π³/8) + 3L log b]/b`.
* At lines 765–766, set `δ(b)=2^(d−2)e(b)` and restrict the last lower bound to `δ(b)<1`. Equivalently, use `3(1−δ)_+²/δ` for every `b≥1`. From `Et≥1−δ` one cannot square the lower bound when `1−δ<0`.

Line-by-line derivation of the load-bearing part: the field is exactly the boundary restriction of `a dλ_z`; its zero interior extension acts on the two indicated edges of `p_0`. Consequently `ψ` is boundary measurable (W1 test (a): YES). For `q=U_1V`, `a'=U_1aU_1⁻¹`,

\[
Dt=-a\cdot\operatorname{Im}q+a'\cdot\operatorname{Im}q,
\quad D^2t=-2t+2(a\cdot a')t+2(a\times a')\cdot\operatorname{Im}q.
\]

Integrating the derivative of `ψ exp(A)` gives `E(Xψ)=−E(Dψ)`. Independent gauge averages at `x` and `z` kill both second-derivative cross terms and the mixed term of `ψ²`. Each remaining square has mean `E|Im q|²/3`. Thus `E(Xψ)=2Et`, `Eψ²=(2/3)E(1−t²)`, and conditional Cauchy–Schwarz gives exactly the factor `6` in line 724.

For Step 6, condition on every link except the corner edge. The radial conditional mean of `Re(UΣ)` is strictly positive whenever `|Σ|>0`. This event contains an open neighbourhood of the trivial remaining links. Positive weights then force at least one of the adjacent boundary plaquettes to have positive mean. No correlation inequality or numerical result is used.

For Step 7, write `E_c=Σw_p(1−t_p)`. Convexity gives `(b/2) E_bE_c≤−φ(b)`. The product of link balls of chordal radius `r=b^(−1/2)` has Haar mass at least `[8r³/(3π³)]^L`, and on it `E_c≤8Wr²`. These facts give the exact bound above. Since the box is fixed, `δ(b)=O(log b/b)→0`. The corrected last display proves the claimed growth. The pure-gradient extension has identically zero scalar curl; positive mean stiffness therefore contradicts every proposed pin-uniform bound by that curl energy. This says nothing about the trivial pin or uniformity as the box grows.

### 3. Corollary AV2, lines 708–717 — HOLDS

Under a gauge change at a boundary site, the conditional score vector at a link tail transforms by the adjoint representation at that tail. Conditional expectation commutes with this change of variables. Distinct tails therefore have zero cross covariance, while the same-tail projection has factor `1/3`. This proves line 711. “No derivative” means no coupling between different sites; same-site differences between link components can still occur. This corollary excludes recovery of intersite colour coherence by this particular pin average, not every possible averaged argument.

### 4. Corollary BH2, lines 768–783 — HOLDS AFTER CORRECTION

At line 770 the corner at `x+ν` is `−θ_3`, not `θ_3`. State the bound for a finite nonempty `Q` with `Σ_Q m_p>0`; if that sum vanishes, the conclusion is the trivial lower bound zero, without division. Positivity of `E(1−t_p²)` follows as in BH. The sign correction does not change any `m_p` or the final lower bound.

For the proof, put `ψ=Σ_Q Dt_p`. The fully free law permits independent gauge averages at every corner. They give `E(Xψ)=Σ_Q (Et_p)m_p`. At a given site, the squared norm of the sum of its at most `n_Q` vectors is at most `n_Q` times their squared norms. Thus `Eψ²≤(n_Q/3) max_Q E(1−t_p²) Σ_Qm_p`. Conditional Cauchy–Schwarz gives line 774. This proof uses the raw corner identity in row 1013, lines 138–144, not its unchecked verdict. No size-uniform lower bound on the resulting ratio has been established.

### 5. Lemma CEN+, §4.1, lines 448–489 — HOLDS AFTER CORRECTION OF SCOPE

The four-independent-link statement HOLDS. At line 460, `M` is arbitrary: take `U_4=M`, `U_3=U_2=1` (W1 test (c): YES). Lines 458–462 then prove an orthogonal extension without any assumed regularity or surjectivity. The proper-case corner relations at lines 469–475 follow by setting two variables to one, then commuting the remaining variable with a constant. The constants must be central. The improper-case relations at lines 476–479 force all pairs of unit quaternions to commute; `i,j` refute this.

An alternative derivation verifies the delicate bridge without assuming the classification of `O(4)`. Set `A=φ_4(1)`, `B=φ_3(1)`, `C=φ_2(1)`, `D=ABC⁻¹=φ_1(1)`, and `f(u)=D⁻¹φ_1(u)`. Substitution in (*) gives

\[
f(abc^{-1})=f(a)f(b)f(c^{-1}).
\]

Thus `f` is multiplicative and fixes 1. Its already proved orthogonal extension restricts to an orthogonal map on imaginary quaternions. Multiplicativity preserves the cross product, so this restriction has determinant `+1`. Every such rotation has an axis and angle and equals conjugation by `cos(θ/2)+n sin(θ/2)`. This proves the proper form and rules out the improper form by a different route. No machine calculation enters.

The lattice deduction at lines 480–482 holds when every participating plaquette has four distinct independent links and the stated corner graphs are connected. Replace line 453's parenthesis by “ordinary boxes with positive side lengths, and nondegenerate periodic lattices (sides at least 3 suffice).” A one-site torus is not covered by the independent-link hypothesis. Replace lines 484–486 by: “Among product maps acting separately on each link and preserving each plaquette trace, the only maps are gauge transformations times closed centre fields.” The lemma does not yet classify every symmetry of the summed action, maps that mix links, or exact reformulations in other variables.

### 6. Lemma AUX, §3.0, lines 276–285 — HOLDS AFTER CORRECTION

Parts (a) and (b) HOLDS: normalization gives the marginal, and an action on `φ` alone fixes the pullback of every function of `U`. This suffices for the stated obstruction to an auxiliary-only action moving the original observable algebra.

Part (c), lines 278–281, does not follow for the measure `P` defined at line 277. A “subset of Φ” supplies neither a split into pinned and free coordinates nor a definition of its twisted ratio. Under the ordinary meaning, conditioning that `P` on a pin changes the `U` marginal. Integrating the remaining `φ` therefore does not give the unweighted `YM` expectation written at line 279.

Explicit finite counterexample: let `U` take two equiprobable values, `Φ={0,1}`, and `K` be trivial. Set `r(U,0)=a(U)`, `r(U,1)=1−a(U)`, with `a=1/4,3/4`, so `N=1`. Pin `φ=0`, and twist it to 1. The expectation of the weight ratio in the conditioned law is

\[
\mathbb E_{P(\cdot\mid\phi=0)}(1-a)/a
=\mathbb E(1-a)/\mathbb Ea=1,
\]

whereas the claimed `YM` expectation of the ratio of pin normalizers is `(3+1/3)/2=5/3`. The same example can be realized by two equal-probability measurable sets of a Wilson configuration space.

Replace (c) by the precise kernel statement: “For specified pinned datum `η`, define a new measure `P_η(dU,dξ)=YM(dU) r(U,η,ξ)dξ/N_η(U)`. If the twisted weight is absolutely continuous with respect to the untwisted weight (strict positivity suffices), then `E_{P_η}[r(U,Tη,ξ)/r(U,η,ξ)]=E_YM[N_{Tη}(U)/N_η(U)]`.” This is not conditioning the original `P` unless its pin likelihood is constant in `U`. For the unpinned positive Higgs kernel, the displayed response at line 348 is well-defined and the same integration argument does hold. No repair of AUX(c) is needed for AUX(a),(b) or BH.

If conditioning the original `P` is intended, the correct right side instead is `E_YM[N_{Tη}/N]/E_YM[N_η/N]`, with the same absolute-continuity proviso. A spectator `SU(2)` coordinate with Haar measure can be added to the finite counterexample, so it also admits a continuous non-abelian auxiliary symmetry.

### 7. Lemma MC, §4.3, lines 508–530 — HOLDS AFTER CORRECTION

(a) HOLDS on `Σ_l≠0`, for a fixed nonzero strength profile and its common positive rescalings. The action is conjugation of `W=U_l Σ̂_l`; the conditional Haar measure and `Re W` are invariant. This is an `SO(3)` action, with the centre of `SU(2)` in its kernel. “For every beta” must not mean that one fixed map preserves every independently varied plaquette strength. One can extend the action by the identity on `Σ_l=0`; it is then measurable globally and continuous in the group parameter, but joint continuity in the link configuration at that zero set is not established.

(b) HOLDS with “changes” at lines 514–515 read as “is not constant as a function of the group element.” Indeed `t_p=w_0q_{p,0}−w·q_{p,vec}` and an `SO(3)` orbit of a nonzero vector is a sphere. A particular nontrivial rotation can still leave that trace fixed. The weighted vector sum vanishes because `Σ β_p q_p=|Σ_l|` is real.

(c) The covariance identity and preservation of gauge invariance by the averaged operator HOLDS. The unrestricted last words “and it is not the identity” at line 517 FAIL: a conjugation-invariant law can be the point mass at the identity. Even Haar averaging can be the identity on observables in a degenerate one-plaquette example where all staples are parallel. Replace them by: “For Haar averaging and a link with a plaquette whose normalized staple has a nonzero imaginary part on a set of positive measure, the averaging operator is nontrivial on gauge-invariant functions.” On that set, applying it to `t_p` removes `w·q_{p,vec}`. This hypothesis is realized by ordinary multi-plaquette Wilson boxes with nonparallel staples; it is not a consequence of `β_p≥0` alone.

An explicit nondegenerate example uses the corner edge `(0,e_1)` of a unit box in `d≥3`, with equal positive strengths. Set all other links to 1 except `U_(e_1,2)=i`. Its staples are `i,1,…,1`, so `Σ/b=m+i`, `m=d−2>0`. Choose `U_l=i Σ̂⁻¹`, hence `W=i`. For the exceptional plaquette, `q=(1+mi)/sqrt(m²+1)` and `t_p=−m/sqrt(m²+1)`, whereas Haar averaging of the MC action gives zero. This difference persists on an open set. No sampling is needed.

At lines 523–530 the physical inference needs a separate restriction. A fixed `R_{l,k}` generally sends a gauge-invariant function to a gauge-dependent function: the displayed covariance relation conjugates `k` by `g_x`. Averaging over `k` restores gauge invariance, but gives a Markov operator, not a group of automorphisms of the gauge-invariant algebra. Thus MC exhibits non-gauge, field-dependent symmetries of the measure; it does not establish a physical global non-abelian symmetry acting on the quotient algebra. W1 test (e): YES only for that weak measure-symmetry reading, NO for the physical global-symmetry reading. The proposed rigid-group filter is a research choice, not a theorem excluding every alternative mechanism.

### 8. Higgs identities H1–H3 and Lemma HW, lines 289–329 — HOLDS

H1 is a product of Haar translations. `U_p` and `V_p` differ by conjugation, and the kernel normalizer is gauge invariant; hence H2 gives both the correct original observables and independence of the residual `φ`. H3's sign is correct with `df=f_y−f_x`: `Re(e^(−df a)V)=t cos(df)+(a·s)sin(df)`.

HW(i) follows from the scalar part of the quaternion products. In HW(ii), differentiate the integral after the successive right translations of the free `φ` variables. The coefficient of the mixed parameter in the energy is

\[
-t(F_x-F_y)\cdot(F'_x-F'_y)
+s\cdot[(F_x+F_y)\times(F'_x-F'_y)].
\]

The integral is constant in the first parameter because `F` vanishes on the pins. Its mixed derivative is zero, giving precisely line 313 and the bracket sign at line 315. For a single axis the cross product vanishes. HW(iii) is `−E A''−Var(A')` for the one-axis twist; `t≤1` gives its blind bound. These are conditional probe identities, not bounds on decay of the original gauge observables. The comparison with OpenAI's numbered identities at lines 326–329 was not independently checked against that external text.

### 9. Proposition LG, lines 331–351 — HOLDS AFTER CORRECTION

The full matching expansion and diamagnetic inequality HOLDS. The moment tensor of uniform `S³` is the Gaussian pairing tensor divided by `4·6···(2m+2)`, obtained by radial integration. Each contraction cycle gives the real trace of `L_{U_γ}R_{exp(−η(γ)a)}`. Left and right multiplication commute, and direct evaluation on `1,i,j,k` gives `4 Re(U_γ) cos η(γ)`. Thus W1 test (d): YES, including the minus sign in the hopping definition. Absolute convergence follows by domination by the corresponding positive scalar contractions at `U=1,η=0`. A doubled edge contributes `κ²/8`; an elementary square contributes `κ⁴/64`.

Line 338 needs a lattice restriction. Replace it by: “On a box, or a periodic lattice with all side lengths at least 6, the following expansion holds.” The opening domain includes short periodic cycles. On a torus of side 3, the three distinct edges of a winding cycle contribute `κ³·4/4³=κ³/16` times its Wilson trace and twist cosine. That term is absent from line 338. Side-4 winding cycles also contribute at order four; side-5 cycles invalidate its `O(κ⁶)` remainder. The full matching series itself already includes all of them and needs no change.

At line 349, write `(κ⁴/64) Σ_p E_YM[t_p](dη)_p²+O(κ⁶)`; a common plaquette mean can be factored out only when the finite-volume law makes those means equal. Lines 348–351 and 637/940 must distinguish the positive combinatorial coefficients of `N^η` from the normalized ratio `N^η/N` and its logarithm. Division and logarithms introduce products and signed subtractions; the displayed proof does not give those responses a power series with nonnegative Wilson-loop coefficients. These corrections do not change the auxiliary-only symmetry obstruction or the diamagnetic inequality.

### 10. Lemma REM, lines 493–504 — HOLDS AFTER CORRECTION

The equality `Z(u^g)=Z(u)` and the sufficient disjoint-component condition at lines 493–497 HOLDS by a change of the integrated links. Replace line 498 by: “A rotation of part of one component can change the gauge orbit; whether it does is determined by the pinned graph's cycle holonomies.” Connectivity is necessary for the relative-colour obstruction stated here, not sufficient.

Counterexample to the unqualified sentence: take two pinned edges forming a tree and rotate only one. Any two assignments on a tree are related by a site gauge transformation, constructed recursively from a root. Their partition functions agree, even though the rotated edge is only part of the connected pinned component. In particular an open pinned path has no gauge-invariant holonomy by itself. Replace lines 501–504 by the precise necessary condition from lines 495–497, retaining that cycle-holonomy data can still make a connected example removable. No nontrivial response follows merely from the existence of a pinned path.

### 11. Identity HAM1, lines 566–575 — HOLDS

Residual time-independent gauge transformations conjugate each `k_x` independently. Expand the smooth resulting central function in the orthonormal product characters of `SU(2)`. The coefficient is `∫ Z(k)∏χ_j(k_x)dk`, with no dimension factor. Undoing temporal gauge identifies this integral with `Z_YM E_YM∏χ_j(P_x)`. Haar volume is normalized to one. Smoothness on the finite compact product supplies convergence of the character series, or the identity may first be read in `L²`. The static-charge-energy claims at lines 578–580 remain conditional physical discussion; HAM1 does not prove them.

### 12. Frame obstruction, §7.4(a), lines 810–829 — HOLDS within its stated pointwise hypothesis

For `λ=1_{x+μ}`, the two nonzero edge coefficients in a plaquette give `δ=n_x−Ad(U_1)n_{x+μ}`. Vanishing of its first trace variation gives `δ·s_p=0`. If those vectors span `R³` for every relevant edge, `δ=0` on every edge. Parallel transport then fixes the axis around every plaquette, contradicting that spanning hypothesis. This checks lines 813–819. The premise requires an actual three-vector span at each edge; it is not asserted for every finite box or every configuration.

For the summed action, gauge invariance gives the divergence identity for the force. Subtracting a genuine infinitesimal gauge variation from the proposed gradient field yields the first-order criterion in line 821 (on a simply connected box). On a torus, “depends only on `dθ`” also requires testing closed non-exact fields; vanishing on gradients alone is insufficient. The second-order equation count and generic impossibility at lines 822–826 are ARGUED, not a proved obstruction. They receive no mathematical confirmation here. A field-dependent flow also requires its derivative and Jacobian in the second variation.

### 13. Lemma GT, §7.4(b), lines 831–855 — mixed verdicts

(i) HOLDS on noncentral loop holonomy: the axis depends only on unmoved loop links, so conditioning on those links makes every other change a fixed Haar translation. The group law follows for the same reason.

(ii) HOLDS as the local insertion rule, with the sign fixed by the traversal direction. Transporting an exponential across an edge of `α` replaces `n_{i+1}` by `n_i`. Two end insertions then cancel or leave their signed difference. A plaquette with more than one such site or segment must retain all its insertions; the rule does not reduce that situation to one insertion.

(iii) The plaquette-trace invariance for a one-sided planar twist HOLDS by this cancellation. The universal non-gauge assertion FAILS at line 842. Let `α` be the boundary of one elementary plaquette of a larger square lattice and choose its inside. There are no off-`α` inward link-ends, so `E` is empty and `τ_t` is the identity, although its loop holonomy can be noncentral. This meets the written hypotheses. The sentence that crossing twists do not commute is also not proved by the cancellation argument. Correct (iii) by keeping the exact-symmetry claim and replacing the rest with an existence claim only after providing a specific non-gauge example and its noncommuting pair. The GUIDE examples do not discharge either assertion.

(iv) HOLDS for the stated single-insertion case, with all links integrated or with the flow avoiding every pinned link: each affected plaquette has exactly one signed insertion of unit magnitude. Then `S''=−Σ_cut β_pt_p`; differentiating the Haar-invariant integral gives `EX=0` and `EX²=−ES''`. This is the asserted identity, with no independent stochastic approximation. “Every partial E cuts corners” additionally presumes the full local lattice neighbourhood; boundary-degenerate corner graphs need that hypothesis explicitly.

The title's “only ... curves” and lines 851–855 do not prove an exclusivity theorem. Reducible backgrounds support a covariantly constant axis on higher-dimensional sets. The local construction proves existence along the selected curve and the stated conditional cost identity.

### 14. Identity CUBE and Lemma SOFT, §7.4(c), lines 857–884 — HOLDS AFTER CORRECTION OF SCOPE

The six-angle density, its value `2/(3π²)`, its vanishing log gradient and its log Hessian `−(1+12/π²)I` HOLDS for one cube. Glue the six character disks along a dual spanning tree, leaving a disk with one boundary, then close it. Orthogonality forces one representation label and gives the sphere factor `k²` with six factors `a_k/k`, hence `k⁻⁴`. Multiplying by the six class Haar densities gives line 860. The series and its derivatives through order two converge uniformly, since their absolute majorants are constant multiples of `Σ k⁻²` or faster. At the centre only odd labels survive. The sums are `Σ_odd k⁻⁴=π⁴/96` and `Σ_odd k⁻²=π²/8`, yielding the printed constants and zero mixed derivatives.

These constants require no numerical evaluation. The sine expansion of 1 on `(0,π)` and Parseval give the odd reciprocal-square sum. The Fourier series `x²=π²/3+4Σ_{n≥1}(−1)^n cos(nx)/n²` on `(−π,π)`, squared and integrated by Parseval, gives `Σ n⁻⁴=π⁴/90`; removing the even terms gives `π⁴/96`.

The candidate density has the same Laplace transform as the pushforward measure on a compact cube. Polynomial density, or uniqueness of the compact moment problem, identifies the measures. Positivity near the centre and Sard's theorem then give a regular value of the smooth six-trace map, hence a point where its differential is onto. This is the finite-cube conclusion in lines 863–874, not a result about all backgrounds.

Replace line 864 by: “For `U(1)`, the oriented face angles sum to zero modulo `2π`; in a fixed local lift they obey one linear equation.” Principal angles globally occupy a union of hyperplane pieces, not one hyperplane.

The rank inference at lines 875–880 is unproved: subtracting `6N` from a `9N` orbit dimension does not establish rank `6N`. The one-cube result supplies no regular point for the full torus map. Keep the torus fibre dimension, arbitrary chosen-plaquette moves and any global entropy-Jacobian description OPEN; do not call them exact at line 880. Even a local angle density must be combined with the conditional fibre measure to control general gauge-invariant observables. None of this is used by BH.

### 15. Remaining numbered claims and whole-file coverage

The whole 1,071-line target was read in bounded ranges. The table separates written identities from proposals, recalled literature and historical run reports. “FAILS as a proof” means the stated deduction is absent or invalid; it is not a counterexample to every possible reformulation.

| Target statement/range | Verdict and reason |
|---|---|
| §§0–1, lines 1–134 | Contract and provenance, not mathematical theorems. The claimed completion marks inherit the corrections above. The `every box or torus` contract must retain the nondegeneracy and short-cycle qualifications. |
| §2.1, I1 | HOLDS as the Wilson/quaternion definition. |
| §2.1, I2–I4 | Citations to earlier lane statements, not newly certified assertions here. The needed Proposition A, WN and TWIST formulas were read directly and their used steps checked above; CEN+ has its own proof. The full earlier B, B', SEAG, EMB and other proof closures were not rechecked. Old check labels supply no evidence. |
| §2.1, I5 | HOLDS for the Haar-averaging fact actually used. No stronger version of Elitzur's theorem is imported. |
| §2.1, I6–I11 | Recalled/comparator literature; not certified here. The report does not rely on Higgs phase diagrams, static-charge energies, or a massless U(1) theorem to establish a new obstruction. |
| §2.1, I12 | A declared belief, not a theorem or premise. No mass gap is checked. |
| §2.2, C1 | HOLDS for one invertible measurable transformation preserving two *distinct* common-coupling Gibbs measures: their Radon–Nikodym ratio forces action preservation almost everywhere, which then forces Haar preservation. No pointwise conclusion for arbitrary noninvertible maps follows. |
| §2.2, C2–C6 | HOLDS AFTER CORRECTION to match MC, CEN+, REM and AUX above. C6 is a necessary-condition/filter proposal, not a classification of all physical symmetries. |
| §2.2, C7 | FAILS as a proved inference at lines 187–190: a dimension count does not imply surjectivity of the full trace differential. Section 7.4(c) correctly marks the torus extension ARGUED; only the one-cube theorem is checked. |
| §2.2, C8 | HOLDS AFTER CORRECTION as BH above. |
| §§2.3–2.5 | Assumptions, candidate list and bounded search history. No novelty theorem or exhaustive no-go follows. Prior statements used are credited in Repo search. |
| §3.2, lines 372–378 | HOLDS for the stated centralizer problem: a map commuting with all rotations sends a point to itself or its antipode by its stabilizer; equivariance and transitivity force one common choice everywhere. Thus the *uniform, background-independent on-site* adjoint-field centralizer is `{±1}`. This does not exclude all field-dependent actions. The imported `κ=∞` comparison is not needed and is not checked here. |
| §3.3, HS1, lines 382–390 | HOLDS for positive coupling: the Gaussian moment-generating function gives the first identity. Apply the second identity once to each triangle; its norm factors are independent of the original links. The remaining link integrals are radial positive Haar integrals. This verifies the identity, not a classification of all symmetries of the new variables. |
| §3.3, lines 391–394 | FAILS as a proof of “no other rigid group”: writing the gauge action does not exclude other actions. Replace with “No additional group meeting the required observable and cost conditions is exhibited here.” Nor has the text identified the conditional radial factor as a Wilson exponential with a random linear coupling. |
| §3.4, lines 398–404 | HOLDS for the limited observation that a connected Lie group has no nontrivial continuous action by permutations on discrete labels, and for invariance of a central plaquette weight under conjugation. The classification of transporter/Bianchi-compatible actions FAILS as a proved conclusion at line 401: no complete variable space, constraints and transformation law are supplied. The formulation's failure is an unsuccessful candidate, not a no-go theorem. |
| §3.5, QL1, lines 408–423 | HOLDS for an open temporal interval: sequential site changes set temporal links to one with Haar Jacobian one, and the temporal plaquette is the displayed quaternion inner product. Residual spatial-site gauges act trivially on the physical algebra. The claimed universal static-charge decay is ARGUED; it is not proved by temporal gauge. No quantum-link comparison inequality is given. |
| §3.6, lines 427–436 | A reading, not a proved lattice identity. The continuum integration-by-parts statement needs the usual vanishing boundary term; the lattice/abelian comparison and arbitrary-reformulation conclusions are not supplied by HS1. No theorem is accepted from it. |
| §4.4, tree-gauge and conjugation-field remark, lines 534–545 | HOLDS on the unfixed, fully integrated model. Put the same coefficient at both ends of a link in WN: the cost is the corner sum of squared differences between adjacent links. The no-pin partition response remains exactly zero by Haar invariance. Do not use this unfixed law as if it were a tree-fixed conditional law. |
| §4.4, lines 547–558 | HOLDS for the residual-group/gauge-invariant-algebra observation on a time interval. The gauge-fixing procedure and plaquette factors give the stated two-direction picture. Landau-gauge determinant and Gribov claims are recalled literature, not proved or imported here. Calling its soft form exactly the Higgs kernel needs the chosen gauge functional; the different divergence-squared kernel is not the same identity. |
| §4.5, lines 562–564 | HOLDS: the physical subspace is invariant pointwise under the gauge group, including its constant subgroup. HAM1 is checked separately above. |
| §4.6, lines 586–599 | HOLDS for the diamagnetic partition inequality. HOLDS for the lab-frame complex-twist plaquette average at distinct free corners: independent conjugation averages replace each insertion by its scalar `cosh`. These facts alone give neither a correlation inequality nor a universal no-go for complex methods. The layer-ordering/comparison statements remain conditional on their recalled inputs. |
| §5, tests, lines 608–629 | HOLDS AFTER CORRECTION as a test ledger, not a collection of new proofs. The d=5 claim is explicitly belief-level; PT is conditional on the cited U(1) theorem. The HS/CH classifications and MC “global” interpretation need the repairs above. No tests against NP or D2 were actually completed where the cells say “not reached” or merely cite a comparison. |
| §§6.1–6.2, lines 635–664 | HOLDS AFTER CORRECTION as the proposed rigid/charged-pin/physical-algebra filter. It is not forced by a classification of all mechanisms. Restrict CEN+ to plaquette-wise product maps and distinguish the normalizer's series from the response. |
| §6.3, lines 668–671 | FAILS at line 669 as written: a general Gibbs sampler is a Markov kernel, not a deterministic invertible measure-preserving map of orbit space; fixed MC rotations do not descend to that space either. Replace with “Measure-preserving Markov kernels on observables do not by themselves supply the required physical group action.” The absence of a general no-go remains correct. |
| §§7.0,7.3,7.5,7.6 | GUIDE reports only. No scripts, samples, timings, lock records, numerical errors or reported passes were verified or used. Their source paths lie outside the permitted scratch folders. |
| §8.1; §8.2 items 1–4 | HOLDS AFTER CORRECTION as an account of unsuccessful candidates, not ten exhaustive symmetry-classification theorems. AUX(c), LG, REM, CEN+ and MC qualifications apply. |
| §8.2 item 5 | HOLDS AFTER CORRECTION: BH gives the homogeneous-strength obstruction with the explicit fixed-box lower bound. Run claims remain unchecked. |
| §8.2 item 6 | HOLDS AFTER CORRECTION: the spanning-hypothesis pointwise obstruction and one-cube trace theorem hold. “Only curves” and full-torus single-angle moves are not established. The Wilson part of angle costs still depends on `β`; only the proposed entropy factor is independent of it. |
| §§8.3–8.7 | HOLDS AFTER CORRECTION with those exact scopes. The work supplies no bound for (W), no decay theorem, and no mass gap. Advice retiring *all* auxiliary reformulations or *all* averaged strategies exceeds AUX and AV2. |
| §8.8 W1 | Completed here. Its stop rule applies to WRONG in AV/BH; neither core theorem is refuted after the explicit proof repairs. Independent later failures are recorded, not hidden. |
| §8.8 W2 and “not proposed” | Instructions for the lead, not performed here. No other file, row, registry or status was edited. |
| §8.9 F1–F6 and final RESULT | HOLDS AFTER CORRECTION as a bounded search registry. F2 requires plaquette-wise trace preservation; F3 requires the corrected REM; F5 states only the proved fixed-colour obstruction; F6 keeps the torus-rank question open. The abstracts and recalled classical theorems in the literature table were not independently verified. |

Independent pass complete. The conclusions above were saved before opening `gap-global-reform-check-opus.md`. The earlier FINISH-summary exposure remains disclosed at the top.

## Comparison with Claude Opus 5.5, row 1020

The full 531-line report was read only after the independent pass was saved. Its source is `gap-global-reform-check-opus.md` at the pinned checkout. Before opening it, the present report's SHA-256 was `8e65ba771e1b1cf1880d5c0a7d098b34137d3fbb3ac326e9976707ea54d1288c`; the target's SHA-256 is `3683d37a58b70237670929dcdfbd865c587506ed13046962ea8137c74191af78`. This ordering is a provenance record, not mathematical evidence or a claim of complete blindness. Cross-provider authorship also does not make every repeated algebraic derivation independent.

We agree on AV, AV2, the factor 6 and positivity in BH, the two BH proof repairs, BH2's corner sign, the four-link CEN+ theorem, HW's mixed coefficient, the full LG matching identity, HAM1, GT's insertion/single-insertion identities, and the one-cube density and Hessian. We also agree that the physical-global-symmetry reading excludes MC and that CEN+'s stronger summary needs its plaquette-preservation hypothesis.

Every difference in the overlapping checks is listed here. References `O:` are lines of the Opus report; `T:` are lines of the target.

| Claim | Opus finding | Resolution and who is right |
|---|---|---|
| AUX(c), `T:278–281`; `O:346,509–512` | All three parts are correct by integrating at fixed U. | **The present correction is right; the blanket Opus approval is wrong.** Conditioning the original measure biases the U marginal. The explicit `1` versus `5/3` counterexample in §6 proves failure of that reading. The corrected separately normalized pinned kernel makes the intended identity true. Parts (a),(b) are agreed. |
| MC(c), `T:516–517`; `O:284,296–304,496` | MC(a)–(c) HOLDS; the proof of nonidentity switches to Haar averaging “in general.” | **The present literal-scope correction is right.** The statement quantifies over a conjugation-invariant law; the identity point mass is one and makes the operator exactly the identity. Haar averaging is nontrivial only with nonparallel staple data as stated in §7. Opus's *restricted* Haar/generic calculation is correct, but does not prove the printed universal clause. |
| LG's low-order expansion, `T:338,345–349`; `O:402–409,499` | The printed expansion is correct on finite lattices, with torus sides at least 3 for the edge argument. | **The present correction is right; this part of the Opus verdict is wrong.** A side-3 winding cycle gives a `κ³/16` Wilson-loop term. A side-4 winding cycle gives an additional `κ⁴/64` term. Neither is a tree term, and neither is included in the elementary-plaquette sum. This is exact finite pairing arithmetic, not a numerical test. Both reports agree on the individual doubled-link and elementary-square coefficients and on the need to keep `Et_p` inside the sum. |
| BH2's domain, `T:769–774`; `O:193–216,493` | Only the harmless corner sign needs correction. | **The present added zero-case correction is right.** For `θ=0`, both numerator and denominator are zero; empty Q also leaves `max_Q` undefined. The displayed formula needs the nonzero domain or the explicitly assigned trivial bound. Opus's argument is correct on that nonzero domain. No substantive positive-field lower bound is lost. |
| Gibbs samplers as “void group solutions,” `T:669`; `O:317–318` | Any Gibbs-sampler step is also admitted by the weak wording. | **The present distinction is right.** A general heat-bath step is a stochastic, noninvertible kernel, not a group element or deterministic orbit-space map. MC gives actual measure symmetries before quotienting; its averaged kernel does not give a physical group action. Opus correctly excludes MC in the physics sense, but the added sampler example is not justified. |

The following apparent verdict differences are not mathematical disagreements, and the additional coverage must not be attributed to Opus:

* CEN+ lattice domain: `O:263–272` already supplies sides at least 3 and distinct links. Opus is right on that restricted domain. My “after correction” label merely carries those hypotheses into `T:453`. Both reports reject the broader summary unless its premise or a further bridge is supplied. Opus's proposed bridge at `O:331–342` is explicitly unchecked and is not adopted here.
* BH's decimal: `O:159–160` rounds the exact logarithmic constant upward. I use the exact logarithm to avoid needing a decimal certificate; this is a presentation change, not a counterexample to `4.92`. Both reports impose the same large-b sign condition. The small-b and GUIDE illustrations at `O:165–169` are not used here.
* GT: `O:427–451` checks only (ii),(iv), adds the turning-plaquette wording and the all-links-integrated/no-moved-pin condition. These additions are correct and are adopted: the measure identity in §13(iv) requires exactly that condition. Opus never checks the universal non-gauge part of (iii); the elementary-plaquette counterexample at `T:842` is new check coverage, not a disagreement with an Opus verdict on (iii). The assertion about a partial E requires the full local corner graph used at `O:441–445`.
* REM: `O:278–280` checks only the sufficient gauge-change statement. That statement is correct. The tree counterexample addresses the further assertion at `T:498–504`, which Opus explicitly did not check.
* CUBE: `O:473–475` already uses the correct modulo-`2π` U(1) relation and leaves the torus-rank discussion unchecked. We agree. My correction makes those limits explicit in the target itself.
* Positive coefficients for the *normalized response*, HS/CH symmetry classifications, the summed-action torus claim, filter necessity, and the broad retirement language are outside Opus's checked scope (`O:514–521`). My qualifications address the full-file request; they are not evidence that Opus reached contrary results on those statements.

The central consumer is unchanged: BH rules out the specified all-pin, fixed-colour classical-curl upper bound at homogeneous positive coupling. It supplies no upper bound at the trivial pin, no size-uniform estimate, no control of typical covariant frames, and no route to (W). No status, registry ownership or audit record is changed.

RESULT: Cross-provider research check of row 1016 at b82477d39: AV and AV2 HOLD; BH HOLDS AFTER CORRECTION with constant 6, positivity for every homogeneous b>0 and fixed-box b/log b growth intact; CEN+, AUX, MC, BH2, LG and REM need the explicit scope/domain/text corrections above; HW, HAM1 and the one-cube density/Hessian HOLD; GT(iii)'s universal non-gauge assertion FAILS at line 842; the full-torus rank claim and broader reformulation no-go claims are not proved; five differences with the Opus check are resolved above; no computer-assisted proof, no mass gap, no status grant.
