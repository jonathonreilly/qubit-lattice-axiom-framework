# Gate of `sa-2.8-terms.md` (queue row 107)
Provenance: Codex (GPT-6), xhigh; checkout `7668755cf170a2a01ea6f6b8a1c8e88659627b25`; Sussman–Alpoge source commit `31a47c543775`; research-text check, not an audit, grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the prepared/healed construction and reference law in `YM4_sketch_500.tex`. The outline was fetched once to `/tmp/sa_ym4.tex`, SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. The subject is Claude's row-102 text. I1 is taken conditionally through `library/meet-6c.md`, Theorem M and Corollary 6.1; their proof is not being gated here (row 106). All calculations below are by hand; shell commands only retrieve, locate, hash or write text.

Scope/recovery: only this file is edited. The checkout has no `docs/ai_methodology/SCIENCE_WORKFLOW.md` or repository copy found by filename search; the task-specific instructions in GOAL and FINISH control this check. No audit, execution-branch work, numerical proof, subagent, commit or publication is involved. The report was saved incrementally and now covers every section of the subject.

## 0. Result — WRONG as the full completion claim; repaired real estimate ADVANCE conditionally

First failing assertion: that every step supporting the stated completion is already written or supplied. The exact ten-term identity passes. The real bound (6.1), including its uniform `O(g_k^(1/2))` consequence, survives the explicit local repairs below, conditional on the named inputs and the actual rounded-radius definition. Section 7's stronger interpretation of the retained Gaussian does not follow. Its denominator claim remains conditional as well. None of these conclusions grants scientific status.

Defects, ranked by what they break (details and repairs are in the corresponding sections):

1. **Section 7(b):** no exact decoupling or stated coercivity of the inner/outer Gaussian follows from a plaquette cutoff; retain the full Q.
2. **Section 7(a), linear term:** the scaled/unscaled derivative is confused, losing a factor of `g^(-1)`; the corrected tail still tends to zero.
3. **Section 7(a), cubic term:** TQ counts action-support tops, not b coordinates; its valid larger count still gives an `o(1)` error.
4. **Section 7(a), integral conventions:** the perturbed Gaussian tail needs its actual covariance and colour norm, and a Lebesgue-coordinate formula needs the Haar Jacobian. The relative-Hessian estimate remains an acknowledged open input.
5. **Section 2.2(c):** mild-class admission is missing from the claimed sign of the change of minimum; use the sign-free exact decomposition.
6. **Lemma W(3):** the rounded radius can jump by L, invalidating the factor 2; a fixed factor 2L and a stronger pre-ceiling margin repair the proof.
7. **Section 4 and dependent coefficients:** finest-corner assignment does not justify six plaquettes per pillar site; 24 is a uniform hand bound.
8. **Scope of input use:** LM extends I4's local bound beyond its stated neighbourhood; use EXT/I5 outside. Carry the prescribed Theorem-M collar constants and the radius upper bound into the theorem, and freeze all package/frame constants before the ceiling.

No failure of the repaired conditional real ten-term bound was found. The sign diagnostic and consumer-normalization assertions require the narrower conclusions stated below.

## 1. Setting and identity (1.3) — ADVANCE (algebraic implication)

First failing step: none in the ten-term identity. With the stated nesting of the plaquette cutoffs, `phi = chi - psi`, `phi + psi = chi`, and `(1-chi)+phi = 1-psi`. No criticality, locality, Taylor estimate or Gaussian identification is required for this calculation.

Write `F = F(B)`, `F0 = F(0)`, `D = DF(0)[B]`, `J = D²F(0)[B,B]/2`. Then

- `R1+R2+R3+R4 = A(v,H)-A(w(1-chi),P)-xA(chi,R(b))`;
- `R5+R6+R7 = -A(w phi,P)+xF`;
- `R8+R9 = -x(F-F0-D-J)+x(A(phi,S)-F0-D-J)+Q = -xF+xA(phi,S)+Q`;
- adding `R10=xA(psi,S)` gives exactly the displayed remainder.

In particular the linear and quadratic contributions in R8 and R9 cancel algebraically even if their estimates fail. There is no missing eleventh term. Positivity of Q follows from `phi >= 0` and the squared real Lie-algebra norm; it does not imply coercivity on any specified set of shell variables. The later margin, admission and scale-count claims remain to be checked below.

## 2. Counterexample discussion — WRONG in 2.2(c); useful diagnostics otherwise

First failing inference in the diagnostic argument: the assertion in 2.2(c) that `P_X(0)` is in Proposition 2.4's mild comparison class. I4 concerns continuations with mild **level-k** data near the box. I5 gives regularity in each prepared layer's own units; it does not state admission of `M^k P_X(0)` to that class. The displayed inequality through `U_{k,X}(M^k P_X(0))` assumes precisely this admission. The claim that the signed excess “is large” has no lower-bound proof either. This does not enter the ten-term identity or its estimates.

**Repair (proved algebraically; admission remains unproved if the sign is wanted):** omit the sign and size assertions. At B=0, LM gives T(0)=S, so exactly

`x(m_p-m_0) = x[A(psi,P_X(0))-A(psi,S)] - R7(0) + x[A(1-chi,P_X(0))-A(1-chi,S)]`.

This is the decomposition actually used. It holds for either sign of the difference. Its exterior term can use W3 at B=0, since T(0)=S: `d(y,C)>=d(y,Lambda)`, and BC applies in the localised prepared metric via the outer level-k shell. Thus no new comparison theorem for an extra pair is needed. A proof of `m_p >= m_0` requires the missing mild-class admission and an applicable fibre-minimum comparison; neither is supplied by the cited signed-minimum identity.

Coverage of the other parts:

- **2.1: ADVANCE**, first failure none. Triangle inequality proves the impossibility of the reversal test *as worded*. It proves no individual bound.
- **2.2(a): CORRECT-NO-ADVANCE** for the explicitly unchecked lower-bound heuristic. The literal core cutoff has no many-shell separation at its boundary. The proposed half-depth margin supplies it; the actual upper-bound checks are below. No converse to locality, or lower bound on R7, has been proved.
- **2.2(b): ADVANCE conditional on LM/I3/I4**, first failure none in (2.1). Full-action stationarity removes the full action derivative, leaving precisely the two cutoff-complement terms. Their smallness is checked in 5.8 below. The reason is not that cutoff stationarity follows from full-action stationarity.
- **2.2(d)–(e): CORRECT-NO-ADVANCE as input bookkeeping.** Global regularity is I5; it is not re-proved by this discussion. The counting and rounded-radius details are checked in Sections 4–6. An unsuccessful counterexample discussion does not establish them.
- **2.2(f), 2.3: WRONG insofar as they assert the denominator's small field dependence or completion of all routes.** The relative Hessian estimate is explicitly open in Section 7, and that section has additional implication errors identified below. These statements should remain conditional.

## 3. Inputs — CORRECT-NO-ADVANCE, with the prescribed I1 replacement

First failing step: none when these are *assumptions*, not established conclusions. I2's uniform complex chart, I3's all-weights response at a real critical reference, I4, I5, GEO1–GEO6 and EXT remain necessary inputs. No status for their producers is inferred here.

Read I1 exactly through meet-6c Theorem M: `E=C_E epsilon_1`, with `C_E=C exp(theta(2rho+8+D_L)) C_L`, and decay from `A_i^c`. Thus W3 decays from C, W4 from Lambda, even when the original domain has other holes. Corollary 6.1 changes the R3/R6 distances to `MR/2-mu-2`; its fixed factor `exp(theta(mu+2))` must be included. Read X-minus as the aligned-cube part in that note, not the literal Euclidean erosion. I do not use that corollary's closing sentence as a proof of the consumer's remaining algebra, counting or constants.

The supplied geometry includes an outer level-k shell of Lambda. This is essential in applying BC; Lambda itself need not lie in the prepared Omega_k. The first-entry argument in Section 5.5 below supplies the correct target set.

For the radius, retain the **definition**, not only its lower bound: SA line 17334 defines R_j as the smallest power of L above `(log min_{i<=j} x_i)^r`. This gives `R_k < L (log x_k)^r` (with a non-strict inequality also sufficient). Without this upper bound the stated premises in isolation do not imply the polynomial prefactors of (6.1). GEO5 is an additional condition on the supplied profiles, not a theorem proved by SA's statement that profiles are supplied data. In particular its locality, range `[0,1]`, and deficit count must be retained.

## 4. Lemmas — WRONG literally; the following local repairs suffice for their uses

**Plaquette assignment: WRONG as counted.** First failure: a plaquette assigned to the finest pillar among its corners need not have its *lower* corner in that pillar. Six plaquettes per site counts only lower-corner assignments. An assigned plaquette does have some corner in its pillar; each site belongs to at most `4 binom(4,2)=24` unoriented elementary plaquettes. **Proved repair:** use `24(xi/eta)^4`, not `6(xi/eta)^4`, throughout estimates using this assignment. For example, a one-site fine pillar surrounded on its negative sides by coarser pillars can receive plaquettes whose lower corners lie outside it. More generally the stated tie rule does not constrain equal-scale assignments to lower corners. Fix any deterministic tie rule and use 24. This multiplies the affected displayed constants by four; it changes no rate. The R10 direct volume count does not use this assignment.

**W: items 1, 2, 4 ADVANCE given the profile premises; item 3 WRONG as proved, repair below.** The first two follow respectively from all healed profiles being one inside chi and from equality of their local input regions away from Lambda. In item 4, `|sum b_i(1-varphi_i)| <= B_* #{i:varphi_i<1}` proves even an absolute bound for `v-x`. In particular these uses require profiles in `[0,1]`.

First failing step in item 3: `R_{k_flat} <= 2R`. Power-of-L rounding invalidates this. At a threshold `t=exp(L^{a/r})`, take the two running minima just above and just below t, with their difference within `B_* N`; their radii are `L^{a+1}` and `L^a`. Their ratio is L at arbitrarily small couplings.

**Proved repair:** for all sufficiently large x, the actual radius definition and FLOW give

`R_{k_flat} < L[log(x+B_*R)]^r <= 2L[log(x-c5)]^r <= 2L R`.

Here `R <= L(log x)^r` makes the middle ratio tend to one. Choose the ceiling to ensure this inequality and `L^(n_c-1)>4 C_p L R`. The distance beyond the inner shells is at least `M L^(n_c-1-N)`, while the old profile range is at most `2 C_p L M R L^(-N)`. Consequently every level `i<=k_flat` has profile one there; only N later increments remain. Thus `|w-x|<=B_*N` is recovered. No constant is chosen after the ceiling.

**MJ: ADVANCE as the stated conditional set-and-datum lemma.** First failure: none under its common-tower and complete collar-lift hypotheses. Intersections on a common block partition are block unions. The complement is `Omega_q^c union T_q^c`; distance to that union is the minimum of the two distances, proving the minimum gap. Since `T_q subset W`, equality of the original members on W gives equality of their meets. The joined data agree if the old rows and the layer rows used for each lift are the same; complete collar blocks ensure the latter. This proves equality, not an identification with an arbitrary source localisation. For W3/W4 do not replace `Omega_0 intersect A` by A; use Theorem M. Its tower truncated at the collar level and its separation are supplied inputs here, not consequences of applying MJ's full-tower gap proof to a constant truncated tail.

**SC: ADVANCE with the counting repair.** First failure in its printed constants is the factor six, not its action estimate. Set `t=(eta/xi)^2 E exp(-theta d)`. Expanding the four insertions yields a curl contribution bounded by `Ct`, a quadratic contribution by `CE exp(-theta d)t`, and a curvature-conversion contribution by `C(eta/xi)a t`. Since `eta/xi<=1`, `E,a<=1`, their sum is at most `C' t`. For SU(2), `a(G)=||1-G||²/2`, so

`|a(G)-a(H)| <= (||1-G||+||1-H||)||G-H||/2`.

Substitution gives `C(a+E exp(-theta d))E exp(-theta d)(eta/xi)^4`. Sum at most `24(xi/eta)^4` plaquettes, then the two comparisons through the common reference. The factors of mesh cancel exactly. The reference curvature is supplied by I5 for the admitted meet background.

**BC: ADVANCE.** First failing step: none. For a path to `E subset Omega_k`, take its last exit from `Omega_i^c` before its first entrance into `Omega_{i+1}`. The intervening subpath lies in layer i and costs at least `c_g`; these subpaths have disjoint interiors. Hence `d>=c_g(m-1)_+`, with `m=k-j`, and separately `d>=dist_Euclidean`. Lattice packing gives the stated `16(D+2n+4)^4 L^(4m)` bound (a torus only reduces the available sites). Splitting the exponential proves the displayed double series. Its depth ratio beyond the first layer is at most `L^4 exp(-theta' c_g/2)<=L^(-12)`; multiplication by any fixed power of m preserves convergence. The radial series is a fixed polynomial times a decaying exponential. Taking `exp(-theta d)<=exp(-theta R0/2)exp(-theta d/2)` proves the tail claim. This is a hand counting argument, not enumeration.

**BC2: ADVANCE with “path” read up to first entrance into the surrounding shell.** First failure: none in the bound; the unnecessary assertion that *every entire path* stays in the core and shell should be replaced by this first-entrance statement. At level `k_flat-m` there are at most `vol(C) xi^(-4)` pillars wholly in the block-aligned core. Weighting by xi² gives the series `sum_m L^(2m) exp(-theta c_g(m-1)_+)`. The m=0,1 terms are `1+L²`; the remaining geometric tail is at most 1 under GEO4. Thus the sum is at most `3L² vol(C) xi_kflat^(-2)`. Paths to any shell first hit the innermost one, so this also bounds the response weight used in (9a).

**LM: ADVANCE after correcting the scope of its regularity sentence.** First literal failure: I4's bound near Lambda is invoked “at a top y” without limiting y to that neighbourhood. Outside Lambda, use the common exterior sequence/data (EXT) and the reference regularity in I5; there the prepared and reference scales agree. Inside Lambda the prepared scale is at most one, so I4 gives local curvature at most `C(M) epsilon_k xi²`, which is admissible when the ceiling is small. Together with the converse-regularity input used by the text, S is in the uniqueness class. For the algebra, `Dq D Phi=id` and stationarity of the reduced box action give `lambda_Lambda=0`. Every prepared tangent preserves q_ext, so its pairing with `DA(S)=Dq_ext^T lambda_ext` is zero. I2's uniqueness then gives `T(0)=S` modulo residual gauge. Differentiating the exactly constant q_ext along the shell path proves item 3. No multiplier normalization or complex-reference theorem is used.

**TQ: ADVANCE with the counting repair.** First printed failure is again the factor six. For `G in SL(2,C)`, `det(1-Y)=1` implies `tr Y=det Y`; hence `|a(G)|<=||Y||²/2`. The repaired per-top holomorphic bound is `12 C_R² r_B²`. On the radius `r_B/4` circle, Cauchy gives `6*12*4³ C_R²/r_B=4608 C_R²/r_B`, so item 1 holds with 4608 instead of 1152. For item 2 each of the potential and fixed-reference covariant-gradient norms gives `2!*C_R r_B/(r_B/2)²=8C_R/r_B`; their sum is the stated 16. The one-dimensional disc lies inside the stipulated sup-norm polydisc, so no number-of-bonds factor is hidden.

## 5. Ten estimates — WRONG with the printed constants; ADVANCE after the explicit repairs

The first printed failure is in 5.2: Corollary 6.1 supplies `MR/2-mu-2`, not `MR/2`. Absorb `exp(theta(mu+2))` in the fixed comparison constant. The numerical coefficients based on six plaquettes per pillar also require the Section 4 repair. Neither defect removes smallness. Below C denotes a fixed enlarged constant, and E is the Theorem-M amplitude. The definition `Pi=x(C_P epsilon_1+E)E <= C R^4 p0²` is correct since `x epsilon_k²=p0²`.

**5.1 (R2, R4): ADVANCE**, first failure none, from W(1)–(2).

**5.2–5.3 (R3, R6): ADVANCE after the fixed distance correction.** SC gives respectively `C Pi (n_XMR)^4 exp(-theta MR/2)` and `C Pi K_X exp(-theta MR/2)`. The aligned-part loss is a fixed prefactor. Summing the GEO3 shell counts uses `(a+b)^4<=8(a^4+b^4)` and `sum_{m>=0}L^(-4m)<2`; this gives the stated order `K_X<=C(R^4+NL^4)` plus the level-k portion of X. Boundary plaquettes at the inner cutoff can be carried by the adjacent inner shell; that shell is included in this all-shell upper count, not discarded.

**5.4 (R7): ADVANCE**, first failure none with the prescribed I1. Corollary 6.1 gives at least `M n_c` of distance from C. Thus `|R7|<=C Pi K_X exp(-theta M n_c)`. Since `n_c=floor(N/2)>=N/2-1`, the loss relative to `exp(-theta MN/2)` is the fixed factor `exp(theta M)`. This checks the margin against the core-replacement comparison; bare meshes and any deeper core layers do not reduce the number of surrounding shells crossed.

**5.5 (R1, source D5): ADVANCE**, first failure none once I1 is read through Theorem M. Here is the necessary BC target check. Every path starting outside Lambda first enters it at its outer level-k shell E_k. Stop the path at this first entrance; its earlier length cannot be increased. Conversely `E_k subset Lambda`. Therefore for these starting points `d(y,Lambda)=d(y,E_k)` (or the same bound up to a fixed boundary-cell convention). E_k is contained in the original Omega_k and has diameter at most `2C_Lambda M`. Here BC uses the **original global sequence and metric**, as required by Theorem M; E_k need not belong to the W4 meet, which excludes Lambda. Do not apply BC to the whole Lambda as though it were contained in the prepared Omega_k.

W(4) bounds the absolute weight by `x(1+B_*d0)(1+R)(1+k-j)`. Apply SC with the nonnegative weight `|v|(1-chi)` and BC with s=1 to obtain

`|R1| <= C Pi(1+B_*d0)(1+R) C_BC(1)(2C_Lambda M+4)^4 exp(-theta MR/2)`.

The depth count `L^(4(k-j))` is paid by the layer-crossing decay, not suppressed by saying the component is small. Decay from the *entire complement of the meet domain* would fail near other holes; the replacement decay from Lambda is indispensable. It is supplied conditionally here, not re-proved. The global profile envelope is consistent: `R_j² epsilon_j <= L² A0 x_j^(-1/2)(log x_j)^(p_0+2r)`, and this last function decreases once `log x_j>2(p_0+2r)`. FLOW then yields the stated loose factor `4L²` against `R_k² epsilon_k`, uniformly in depth.

**5.6 (R5): ADVANCE after W(3) and counting repairs.** The bound is `12 B_*N C_P² epsilon_1² K_X`, rather than 3 times these factors. This has order `g² R^9 p0²`; no inverse coupling is present in the weight difference.

**5.7 (R8): ADVANCE after counting repair.** The real segment stays in the complex chart because `||gB||<=r_B/4`. Applying the third derivative bound to the single real function `t -> F(tB)` gives `xg³/6=g/6`, hence

`|R8| <= 768 C_R² g(A1 p1)^3 K_X/r_B`.

The original factor 192 becomes 768. The derivative is a directional derivative in sup norm; the all-top count already accounts for the extent of the support.

**5.8 (R9, source D1): ADVANCE after counting repair.** The exact chain rule is

`D² F_tilde(0)[B,B] = sum phi {D²a_p(S)[eta HB,eta HB]+Da_p(S)[eta tau'']}`.

Gauge invariance removes w(u), not the acceleration tau-double-prime. For four transported insertions, `|X1|<=4|A|`, `|X2|<=8|A|²`, `tr X2=0`. Twice differentiating `a=1-tr/2` gives the stated curl square and an error bounded by `32||1-partial S|| |A|²`. Also `|Da_p(S)[A]|<=||1-partial S|| |d_S A|`. With `xg²=1`, this proves exactly `R9=-x DF(0)[B]-(K1+K2)/2`. Both discrepancy terms are necessary.

For the linear term LM gives

`x DF(0)[B]=-g^(-1){DA(psi,S)[eta HB]+DA(1-chi,S)[eta HB]}`.

The corrected per-top derivative bound is `48 C'_c C4 a_S(y)||B|| exp(-theta d(y,shells))`. On the margin put `j=k_flat+m`. Direct geometric summation gives

`sum_{m=0}^{n_c-1}(C_nM(RL^(-m)+L))^4 L^(2m-2N)`
`<=16 C_n^4 M^4 {R^4 L^(-2N)+L² L^(-2(N-n_c))}`.

BC2 adds at most `3L²(C_nMR)^4 L^(-2N)`. These are bounded by the printed `Sigma_psi=20 C_n^4 M^4 R^4 L² L^(-2(N-n_c))` for the sufficiently large radii in use. On this region I4 gives `a_S=C(M) epsilon_k xi²`. Therefore the repaired (9a) is at most

`48 C'_c C4 C(M) p0 A1 p1 Sigma_psi`.

In particular **there is no residual g^(-1)**: `g^(-1) epsilon_k ||B||<=p0 A1 p1`. It is the resulting polynomial that the factor `L^(-2(N-n_c))` beats.

Outside chi every path to the shell support first reaches E_k; in the **localised/joined metric** its distance is at least MR up to the fixed carrier convention. BC(s=0) counts the collar-tower tops as well as the ordinary ones. Since `g^(-1) epsilon_1=4L²C_F R²p0`, the repaired (9b) is at most

`192 C'_c C4 C_P L²C_F R²p0 A1p1 C_BC(0)(2C_Lambda M+4)^4 exp(-theta MR/2)`.

Using the original metric here instead of the joined one would not pay for the artificial fine tower. This is a different metric use from R1's Theorem-M comparison.

Finally the counting repair gives

`|K1|<=768 C_P epsilon_1 C4²(A1p1)² K_X`,
`|K2|<=384 C'_c C_P epsilon_1 C_R(A1p1)² K_X/r_B`.

The second estimate uses TQ(2) and the fixed-reference curl conversion. Both are `g` times fixed powers of logarithms. This redoes all three parts of R9 without asserting that its linear term vanishes.

**5.9 (R10, source D2): ADVANCE**, first failure none. Z-natural has side at most `C_nM(R+L)L^(n_c-N)`. Counting plaquettes directly by lower corners *within this box* gives at most six per site, so the printed factor 3 is valid here. I4 and `x epsilon_k²=p0²` give

`0<=R10<=3C(M)² C_n^4M^4(R+L)^4 p0² L^(-4(N-n_c))`.

Since `N-n_c=ceil(N/2)`, the retained margin still leaves at least half the depth for volume suppression. This estimate concerns the smooth reference action only, not the retained prepared-core action.

## 6. Theorem and constants — ADVANCE as the repaired conditional asymptotic bound

First failing step of the *printed* proof: it imports the uncorrected estimates of Section 5, then uses the radius upper bound omitted from its displayed FLOW. With the explicit repairs above and the actual radius definition, no step of the following implication fails. This does not establish any input or the consumer normalization of Section 7.

The respective polynomial orders are bounded by: `R^8 p0²` for the local comparisons, `R^5 p0²` for R1, `g² R^9 p0²` for R5, `g R^4 p1³` for R8, `R^4 p0 p1` for (9a), `R² p0 p1` for (9b), `g R^6 p0 p1²` for K1/K2, and `(R+L)^4 p0²` for R10. Fixed L, M, radii and chart constants multiply these expressions. The slightly looser `K_X<=C(1+ell)^(4r+1)` therefore fits the displayed `K_*=9r+2 p_0+3 p_1+4` for the source's positive fixed exponents.

Using `R>=ell^r/2`, `n_c>=R/2-1`, and `N-n_c>=N/2`, all comparison factors are bounded by a fixed multiple of `exp(-theta M ell^r/4)`, all core factors by `L^(-ell^r/2)`, and the remaining terms by `exp(-ell/2)` times their polynomials. Thus (6.1) holds with a larger fixed C_*. For any fixed a>0 and r>=2, `a ell^r >= ell/2` eventually. Also `(1+ell)^K exp(-ell/4)` is bounded: its logarithmic derivative is `K/(1+ell)-1/4`. These two facts give the asserted `C'_* exp(-ell/4)=C'_* g^(1/2)` bound by hand.

**Order check.** There is a valid order without any choice after the coupling ceiling, but the displayed short list must be made explicit as follows:

1. Fix the requested tolerance and an admissible source package. If claiming compatibility with SA (2e), fix the exponents before L, as SA 19465–19485 does; the consumer's abbreviated order is not a proof that this dependency may be reversed. Fix the rate, rho, mu, geometric/profile constants and chart/response constants, with `theta rho>=64 log L`. Fix M with the stated gap and collar floors, then its dependent constants, M0, A0, A1 and the *coupling-independent* flow bounds B_* and c5. Use a pre-ceiling frame bound for B_*, not a bound defined through a later remainder at gamma.
2. Replace C_mu by the fixed C_E of Theorem M and fix the enlarged counting/comparison constants. The condition on rho is a floor at this stage; shrinking g cannot enforce it. The bound `C_R r_B<=1/2`, if retained in TQ, also belongs at this stage. In fact the determinant/Cauchy proof above does not use that numerical smallness once I2 supplies the chart and its bounds.
3. Choose one X0 so that, for every x>=X0, the profile envelope, admission/regularity ceilings, `delta'<=r_B/4`, the source's stated smallness tests, the repaired radius comparison, and `L^(floor(R/2)-1)>4 C_p L R` all hold, and the repaired (6.1) is at most the prescribed tolerance. Such X0 exists: `epsilon_1<=C exp(-ell/2)ell^(p_0+2r)` tends to zero, whereas the logarithm of the left-to-right margin ratio grows as `(R/2)log L-O(log R)`. The other ratios are of the same displayed polynomial/exponential types. A finite maximum of these thresholds suffices. Set `gamma=X0^(-1/2)` once.

Thus neither the torus, k, a history, a collar width, nor the number of shells is allowed to select a new constant after gamma. The row-106 implication may change C_E but must be fixed before this choice. No uniform statement is obtained by letting mu or M depend on g.

## 7. Outside the ten terms — WRONG as written; the conditional repairs are limited

**7(a), linear term: WRONG.** First failure is the displayed derivative identity. Section 1 defines `R(b)=R_tilde(gb)`, so `DR(0)[b]=g D R_tilde(0)[b]`. Full stationarity gives

`x DA(chi,S)[DR(0)b] = -x DA(1-chi,S)[DR(0)b]`
`= -g^(-1) DA(1-chi,S)[D R_tilde(0)b]`.

The source puts DR rather than D R-tilde in the last expression and loses a factor `g^(-1)`. **Proved repair:** use the equation above and the unscaled response estimate. The same exterior BC bound as (9b), now with `||b||<=M0 p0`, is `C R² M0 p0² exp(-theta MR/2)`, which tends to zero.

**7(a), cubic term: WRONG as inferred from TQ.** The first failure is replacing the number of tops carrying chi by the number of b coordinates. TQ sums the action support, not the datum dimension. **Proved sufficient repair:** use `K_chi<=(n_XMR)^4` for the healed reference chart. Its uniform cubic error is `C g(M0p0)^3 K_chi/r_B=o(1)`. A sharper n_b bound needs an additional locality argument, but is unnecessary for this conditional conclusion.

**7(a), determinant: ADVANCE given the stated relative-Hessian input.** First failure none. If the relative symmetric perturbation has norm at most epsilon_h<=1/2, all eigenvalues of `h0^(-1/2) hS h0^(-1/2)` lie in `[1-epsilon_h,1+epsilon_h]`. Integrating `1/t` on this interval gives `|log lambda|<=2 epsilon_h`, and summing proves `|log det(hS h0^(-1))|<=2 n_b epsilon_h`. This establishes no bound on epsilon_h itself. Likewise the small-curvature statement is not an identification of hS with the flat Hessian.

**7(a), tails and conclusion: CORRECT-NO-ADVANCE after specifying their hypotheses.** Let h0>=cI for the *truncated-action* flat Hessian used here, assume the stated relative comparison, and let delta be the repaired uniform linear-plus-cubic error. Then hS>=cI/2. For a normalized Gaussian with this Hessian each real coordinate has variance at most 2/c. Shifting the one-dimensional Gaussian tail integral gives `P(|b_i|>t)<=exp(-ct²/4)`. For a coordinate box this gives a union bound with exponent `-c M0²p0²/4`. For the actual supremum of three-component SU(2) bond norms, leaving a bond ball of radius M0 p0 implies that one of its coordinates exceeds `M0 p0/sqrt(3)`. A bound valid for that cutoff is

`tau <= n_b exp(-c M0² p0²/12)`.

Thus the printed exponent with denominator 2 is not justified with the same c(M) by the stated relative comparison and bond-norm cutoff. A fixed change of the constant suffices. If Z_G(S) is the full Gaussian integral, positivity on the cutoff region gives

`exp(-delta)(1-tau)Z_G(S) <= Z_b(S) <= exp(delta)Z_G(S)`.

For tau<=1/2 this and the determinant estimate imply

`|log Z_b(S)-log Z_b^0| <= delta + 2tau + n_b epsilon_h`.

If I4 only supplies coercivity of the full reduced action, the required flat truncated-action coercivity follows after subtracting its exterior quadratic tail: I3 and BC bound that tail by `C n_b exp(-theta MR)` in operator norm; choose the ceiling so it is below half the full lower bound. This uses the reference response on Lambda rows. The chart and response are required at the flat reference as well.

If db means Lebesgue measure, the original Haar integral additionally has the exponential-coordinate Jacobian. For SU(2) each free bond contributes a field-independent constant times `g^3(sin(g|b|)/(g|b|))²`. On the box, `1-t²/6<=sin(t)/t<=1` gives total log-Jacobian error at most `C n_b g² M0²p0²=o(1)`; put the field-independent factors into Z_b^0. Alternatively explicitly define db to include the pulled-back Haar measure. The unqualified equality with a Lebesgue integral omits this factor.

The estimate `epsilon_h<=C(M)epsilon_1/(c(M)r_B)` and the appropriate flat-to-curved comparison remain **open inputs**, as the text admits. Therefore the denominator is not established to have small field dependence by this section. The conditional integral inequality above is the valid conclusion, with every needed hypothesis retained.

**7(b), inner-shell normalization: WRONG as an implication.** First failure: “Q is coercive only on the outer-shell variables” is not supplied by positivity of Q or I3; the following statement that inner B's are integrated *only* against the core action and chi-prime additionally requires exact decoupling. Write `B=(B_i,B_o)` and `C_i=phi^(1/2)d_S eta H|_inner`, `C_o=phi^(1/2)d_S eta H|_outer`. Exactly,

`Q(B)=||C_i B_i+C_o B_o||²/2`.

Deleting inner *plaquettes* does not prove `C_i=0`, and no input asserts it. I3 is a decay upper bound, not compact support. In particular the last inner shell touches the first retained shell; the half-depth margin separating C from supp(phi) gives no half-depth separation between that shell's sources and supp(phi). Even the elementary quadratic extension minimizing `((x-z)²+z²)/2` at fixed x=b has z=b/2 and nonzero exterior energy b²/8; this illustrates the missing inference, not a counterexample to the YM construction.

**Proved safe repair:** retain the full Q(B_i,B_o), its mixed term, and the B-dependent retained action exactly as in (1.3). The reference-to-prepared decomposition then remains valid without any Gaussian normalization claim for these variables. Factoring or normalizing an outer Gaussian requires a separate lower-bound/Schur-complement argument with the actual tree constraints and cutoff. That repair is visible but **unproved here**. Likewise the asserted replacement of the complex-continuation factor by `L^(-(N-n_c))` is not proved by the real volume estimate; leave it open with its source-support and weight hypotheses. Nothing in this section proves that the change is “only bookkeeping.”

## 8. Defects, consumer changes and open items — WRONG as a completion claim

First failing step: “none breaks the conclusion after its repair,” followed by the assertion that the consumer normalization keeps its claimed interpretation. The repaired ten-term *real bound* does hold conditionally; the Section 7 inference does not follow with the stated inputs. Distinguish them.

The source's D1 linear-tail and D2 margin mechanisms survive the checks above, with the local repairs recorded here. Source D5 is resolved conditionally by the Theorem-M decay set plus the first-entry/BC argument. Source D4 is CORRECT-NO-ADVANCE: a bound on the difference between flat and curved responses would imply the extra quadratic error by `| ||u||²-||v||² |<=||u-v||(||u||+||v||)`; that response bound is still an input, not a consequence of positivity or the Gram identity alone.

The open list must read I1 through meet-6c Theorem M and Corollary 6.1, pending row 106; it must not claim that this check gates that theorem. Keep I2–I5 and GEO/EXT with their stated premise status, and add the Section 7 normalization/coercivity/comparison obligations. The diagnostic sign claim in 2.2(c) either needs its separate admission proof or should be deleted. No counterexample to the repaired real ten-term bound is established here; conversely no Yang–Mills theorem, audit status, or source-geometry discharge follows from this gate.

**Final recovery checkpoint.** Sections 0–8, every lemma in Section 4, every estimate in Section 5, and both consumer subsections have been checked. The original files still match `7668755cf170a2a01ea6f6b8a1c8e88659627b25`; `git status --short` shows only this new report. SHA-256: `library/sa-2.8-terms.md` = `dccd6ff2f1a36818ff2348d5b3c494880262094b275667e7c3000a0a6a62c262`; `library/meet-6c.md` = `b462ad878b3f741e954976f060ef972926c38c1360dab3b4eee6aad011606696`. No source or editable prompt file was changed. The surviving result is the repaired conditional real remainder bound; the failed routes are the unproved mild-class sign inference and exact inner-Gaussian decoupling. The next consumer decision is to retain the full Q or supply the missing factorization/coercivity proof, while keeping the relative-Hessian and complex-continuation obligations open. This checkpoint does not require rerunning or refetching any source.
