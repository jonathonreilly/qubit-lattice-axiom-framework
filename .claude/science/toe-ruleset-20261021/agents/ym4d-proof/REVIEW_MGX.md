# Independent hostile review of MGX

**Disposition: LAND as a bounded conditional research note. No binding defect
was found in the reviewed revision.** The actual RG crossover and the direct
uniform physical-transfer estimate remain **UNDECIDED**. This disposition does
not establish continuum existence, a continuum mass gap, an audit verdict or
retained status, and performs no landing.

Reviewer: Codex, fresh context, 2026-10-29. This is same-family review, not
cross-family replication. I did not author MGX or delegate this review.
Earlier source reviews were available and were checked against the underlying
arguments. I read the earlier `checks/mgx_review.md` after checking MGX's
derivations; its verdict is not evidence for this verdict.

The reviewed [MGX.md](MGX.md) has 388 lines and SHA256
`c4a4f5f95f3b499e1c4f7a9a69a24bd2e94b1fb19ee53ceca48e9cc78393c8bb`.
All MGX line references below refer to those bytes. Worktree HEAD is
`f401d825dcdaac36b13f0aee885f16099d066abb`. The 16 input identities in
[checks/mgx_sources.sha256](checks/mgx_sources.sha256), manifest SHA256
`6b64f65db1bbdc97c1c0888a6b12eb3ef04ab8ba307c6e7dd8b0fc9d596508f9`,
all match the current files. Cached `origin/main` is
`01589af3faf806b736c42dc2f3bd625e9edead9f`; remote freshness was not established.
The checked workflow, repository reviewer skill and proof-search reference
match that cached revision. The installed reviewer skill's complete diff from
that source was inspected; the cached-main procedure governs this review.

**Item verdicts and fixes**

| Item and MGX lines | Verdict | Fix / exact boundary |
|---|---|---|
| Target and reflected spectral criterion, 18–37 | LAND, conditional | None. Reconstruction, complete dense family, normalized physical time and a nonzero excited space remain premises. SU(N) does not cover the full compact-simple-group target. |
| Available Wilson endpoint, 39–63 | LAND, fixed-spacing scope | None. The actual magnetic/Perron factors and the infinite-volume injectivity argument support the cited endpoint; no cutoff-uniform crossover follows. |
| Normalization and weak-window comparison, 65–117; table row 352 | LAND, conditional comparison | None. The guaranteed tuned nodes are weak. Equation (2) does not prohibit an uncontrolled final output; equation (3) is expressly a formal continuation. |
| Exact coarse action and source weights, 121–135 | LAND on the stated domain | None. Bounded finite-cutoff insertions and finite complex sources repair the earlier integrability issue. No uniform locality or source analyticity radius is supplied. |
| Zero-Hessian example and complete covariance decomposition, 137–171 | LAND, exact controls | None. The example refutes control by the Hessian alone; it is not a counterexample to Yang–Mills crossover. Both terms in (5) are needed. |
| Non-Wilson weighted interaction criterion, 173–249 | LAND, conditional finite-volume theorem | None. All-field summability, positive weight and a uniform strict row bound are explicit. Failure of (7) rejects this certificate only. |
| Option A transport and continuum passage, 251–308; row 354 | LAND as an implication; actual producer OPEN | None. Localization, the full conditional remainder, common rates/onset, same-sequence matching and MG4 are not proved for the proposed trajectory. |
| Option B physical-transfer criterion and diagnostics, 310–346; row 355 | LAND as an implication; actual producer OPEN | None. Ground-state/finite-time-circle matching is expressly required. Auxiliary stochastic contraction is insufficient. |
| Overall decision, plausibility, attribution and status, 3–16, 348–388 | LAND as a bounded UNDECIDED report | None. The note establishes neither GO nor a global NO-GO and closes no MG row. “Plausibility” is limited to consistency of a proposed mechanism. |

**Independent derivations and source checks**

1. **Coupling and control interval.** FLOW lines 24–26 define the Wilson
   coefficient as `u=1/g_flow^2=2N/g_std^2`. One can also check the conversion
   directly: with `tr(T^a T^b)=delta_ab/2`, a plaquette contributes
   `a^4 sum_a(F_mu,nu^a)^2/(4N)` to `1-Re tr(U_p)/N` at leading order.
   Summing unoriented planes gives coefficient `beta_W/(8N)` on the
   fully contracted `F_mu,nu^a F_mu,nu^a`, hence the stated convention.
   Thus `beta_W<=1/32` requires `g_flow^2>=32` and `g_std^2>=64N`.
   The local-block source's `g_K` is not FLOW's `g` under that identification.

   Given the named one-loop premise, `du/d log(mu)=4N b_0` with
   `b_0=11N/(48 pi^2)` gives `b=11N^2/(12 pi^2)`. This is conversion of a
   supplied coefficient, not an independent loop calculation. Telescoping
   `u_(k+1)=u_k-b_k-rho_k`, bounding the one-loop partial sums by `R`, and
   using `sum |rho_k|<=C_rho gamma^2(n-j)` gives exactly (2). FLOW
   409–424 absorbs `g_k^6` into `g_k^2` only for `g_k<=1`. Its tuning
   statement and proof, 433–455, keep all nodes through K inside gamma.
   Shrinking gamma to at most one therefore gives `u_k>=1`, disjoint from
   the literal Wilson endpoint interval. The input-only quantifier through
   `n-1` in FLOW 420–424 does not assert a no-overshoot theorem. MGX
   97–102 preserves that distinction. Integrating the formal one-loop line
   gives (3); its finite formal length ratio proves no infrared continuation.
   The final disposition in REVIEW_UNIFORM_ONE_LOOP_COUPLING_ASTRA 372–378
   explicitly leaves nonlinear finite-u flow and the physical gap open.

2. **The endpoint is the physical transfer, with its full environment.**
   Integrating temporal vertex links gives `k P_gauge`; splitting each
   magnetic plaquette between consecutive slabs gives `T=A k P_gauge A`.
   The omitted constant per temporal layer cancels in eigenvalue ratios.
   Expanding `exp[(beta/(2N))(chi_f+chi_fbar)]` into tensor characters gives
   strictly positive coefficients for every SU(N) irrep at beta>0. Its
   convolution multipliers are `c_R/d_R`, so the finite operator is positive
   and injective on the invariant space. The positive continuous kernel has
   a simple positive Perron vector. These are the actual arguments in
   MASS_GAP_CONSTRUCTION_ASTRA 88–162, not a heat-bath substitution.

   In the open temporal-gauge slab the interaction row is `12 beta+2 beta`:
   four spatial plaquettes with three other edges, plus two temporal pairs.
   Changing a bottom edge inserts a first-layer function of oscillation at
   most `4 beta`. Its mixed logarithmic response is an integrated covariance,
   bounded by `4 beta^2 D^+`. Adding the half-magnetic factor gives the
   physical Doob output majorant
   `Q=12 beta+beta^2/(1-14 beta)`; changing its input contributes a single-site
   TV defect at most beta. The comparison inequality then contracts summed
   oscillations by `r=beta/(1-Q)`. At `beta=1/32`,
   `14 beta=7/16`, `beta^2/(1-14 beta)=1/576`,
   `Q=217/576`, and `r=18/359`. Each term increases on the stated interval.
   This reproduces MASS_GAP_LOCAL_BLOCK_ASTRA 178–346 and MGX's constant.

   The unfixed four-dimensional row `18 beta<1` gives boundary-uniform
   convergence of local laws and the same thermodynamic state. The local
   physical-time covariance bound survives at each fixed integer time;
   positivity and cylinder density exclude transfer spectrum above r on
   the centered invariant space. Crucially, infinite-volume injectivity
   is not inherited from finite-volume injectivity: the supplement constructs
   the half-space kernel for every bottom field, proves its bounded
   finite-boundary tilt, uses conditional Haar domination and a countable
   exhaustion to control null sets, and then annihilates each finite-block
   signed measure using nonzero Peter–Weyl multipliers. Martingale exhaustion
   followed by stationarity forces a putative kernel vector to vanish.
   Thus the logarithm is densely defined on the full invariant slice space.

   The separate nonzero witness is also valid. For a simple loop,
   `v_2=1/4` and `v_N=1/(2N^2)` for N>=3 follow from character orthogonality.
   Cauchy–Schwarz in the positive convolution form gives
   `kbar_B >= |F><F|/(1+v_N/r_f^b)`. Tensoring retains the exterior operator;
   only afterward does pointwise kernel positivity compare the block
   integrals with `u_min`. The result is
   `v_N^2 exp[-4 beta(p_B+b)]/(1+v_N/r_f^b)>0`.
   For a plaquette, `b=4`, `p_B=4*4-3=13`, giving `exp(-68 beta)`.
   This supplies a finite-energy excited sector at fixed spacing. Neither
   this witness nor continuous Hamiltonian interpolation removes that spacing.
   The review's sections 1–6 and the injectivity supplement match the claims
   and locators in MGX 39–57. The older all-beta minorization is
   `exp(-2 beta |E_s|)`; its vanishing with volume weakens a lower bound,
   and is not an upper bound on the actual gap (MGX 60–63).

3. **Action projection and sources.** At fixed cutoff, the source factor in
   (4) has absolute value at most `exp(sum_i |J_i| ||F_i||_infinity)`.
   Compactness and the positive continuous supplied density/kernel therefore
   justify the finite integrals on the revised domain. Their existence gives
   no uniform estimates under cutoff removal. FLOW's Def F-g, 146–153,
   explicitly uses a small-field representation and a marginal Hessian;
   it is not an all-field Wilson-action identification.

   For SU(2), `s_p=O(B^2)` makes `c s_p^2` start at fourth order. Its Hessian
   is zero, whereas the four center-valued assignments give `0,4c,4c,0`
   and mixed difference `-8c`. Choosing the two adjacent edges in one
   plaquette also preserves this test in the translation sum: terms depending
   on only one of the two varied edges cancel from the mixed difference.

   For square-integrable centered fine variables, decompose each into its
   conditional mean given V and its orthogonal residual in L2. The cross
   inner products vanish. The remaining two inner products are precisely
   the two terms of the sesquilinear law of total covariance (5).
   At `K=1`, conditional means are constant and the entire fine covariance
   stays in the residual term. For bounded sources the exact weight is
   `W(V;J)=Z_a(J)`; its source derivatives cannot be discarded with a
   source-independent vacuum normalization. Equations (21)–(23) in
   MASS_GAP_CONSTRUCTION_ASTRA 393–413 have exactly this meaning. Repeated
   source products are not recoverable from first conditional moments alone.

4. **Weighted Gibbs comparison.** Write a normalized likelihood ratio r
   between m and M, with `E r=1`. Convexity of `(r-1)_+` gives
   `TV <= (M-1)(1-m)/(M-m)`; at `M/m=exp(L)` the maximum occurs at
   `m=exp(-L/2)`, `M=exp(L/2)`, giving `tanh(L/4)<=L/4`.
   The constant case has TV zero. Changing coordinate j therefore perturbs
   the conditional at i by at most the mixed action oscillation divided by
   four, which is bounded by C in (6).

   I also checked the covariance factor by a different route from the
   author's integrated-generator proof. For bounded real g, tilt the law by
   `exp(hg)`. The conditional specification defect at i is at most
   `b_i=|h| delta_i g/4`. Couple random single-coordinate updates of the two
   stationary marginal laws using maximal conditional couplings. With M
   coordinates, their disagreement probabilities satisfy
   `p_(k+1) <= [(1-1/M)I+C/M]p_k+b/M`.
   The strict row bound makes iteration give `limsup p_k <= (I-C)^(-1)b`.
   Telescoping f across differing coordinates bounds the difference of its
   expectations by `delta(f)^T (I-C)^(-1)b`. Divide by |h| and differentiate
   at zero to obtain the real covariance estimate with factor `1/4`.
   Boundedness justifies differentiation. This also verifies the comparison
   inequality used in the endpoint check above.

   For every path contributing to `C^k`, its endpoint time distance is at
   most the sum of its edge distances. Thus the exponentially weighted row
   of `C^k` is at most `q_*^k`, and the resolvent entry is at most
   `exp(-nu |tau_i-tau_j|)/(1-q_*)`. Four real/imaginary covariance terms
   give the conservative factor one in (8) for complex observables.
   Each four-dimensional link has `6*3=18` other-edge plaquette incidences,
   each with mixed Wilson oscillation at most `4 beta_W` and time distance
   at most one. Hence (7) and the allowance
   `epsilon_nu<1-(9/16)exp(nu)` follow exactly. The note explicitly requires
   `nu>0`, all boundary terms and cyclic distance at a periodic seam.
   This is a static Euclidean estimate; it needs no coarse transfer and
   proves no equality between auxiliary update time and physical time.

5. **Option A's limiting argument.** Put `e_R=D_F exp(-kappa R)`.
   Since the conditional means and approximants are centered,
   their covariance difference is at most
   `M_F e_R+(M_F+e_R)e_R <= (2M_F+D_F)D_F exp(-kappa R)`.
   With `R=floor(n/4)`, separation is at least `n/2-d_F` and
   `exp(-kappa R)<=exp(kappa)exp(-kappa n/4)`.
   Adding the localized covariance, localization error and full conditional
   remainder gives exactly (9), with
   `c=min(nu/2,kappa/4,sigma)` and the printed A_F.
   Nonnegativity is supplied by the matched fine reflected correlation,
   not by an arbitrary coarse covariance.

   Fix n first. The uniform onset and growing safe window eventually admit
   this n. The same-sequence matching, including moving-time continuity,
   passes the bound to `C_F(n ell)` while `eta_a,F(n)` tends to zero.
   For `0<=b<c/ell`, positivity of the spectral measure gives
   `||E_H([0,b])v_F||^2 <= A_F exp[-(c-b ell)n]`.
   Only now send n to infinity. A bounded spectral projection that kills
   the dense spanning family kills all of `Omega-perp`; increasing b to
   `c/ell` excludes `[0,c/ell)` on that space, including extra vacuum
   vectors. MG4 supplies nontriviality. Strong convergence of finite-energy
   spectral projections supplies finite excited infimum. A common rate is
   essential; prefactors and onset need not be uniform over F. The argument
   makes no illicit exchange of the cutoff and large-time limits.

6. **Option B and physical units.** Self-adjointness and `P Omega=Omega`
   make the centered space reducing. For `m=n b_a+s`, positivity and
   contraction bound its diagonal matrix element by `M_F r_*^n`.
   Since `n>=t/(a b_a)-1>=t/ell_+-1`, for `0<r_*<1` this is at most
   `(M_F/r_*) exp[-(-log r_*)t/ell_+]`, as in (11).
   The zero case is covered by replacing r_* with any positive larger
   bound below one. Fixed-time matching and the same spectral-projection
   proof give the claimed implication; the dense diagonal alternative uses
   the fixed-n matching explicitly borrowed from section 5.
   Finite-time-circle traces are not automatically ground-state forms,
   and lines 321–323 correctly retain that obligation.
   The exact diagnostic `P_a=diag(1,exp(-a^2))` has
   `H_a=diag(0,a)`, so cutoff-wise positivity does not give a positive
   limiting rate. Conversely, holding the Wilson strong-coupling endpoint
   fixed and sending its own spacing to zero sends its lower energy bound
   to infinity. Neither operation produces the stated nontrivial continuum
   hierarchy.

**Status, attribution and verification limits**

The current source claims no audited status. AUDIT 160–194 describes MG0,
MG1, MG2, MG4 and MG5 as OPEN and MG3 as AT-RISK; MGX's statement that none
closes is accurate. The endpoint's prior review is bounded support, not
landing or continuum certification. Option A's interaction/localization/
remainder package is a stronger sufficient condition than a physical mass
gap. Option B's norm bound is already a uniform cutoff physical-gap estimate
in transfer language. Merely stating either is not near-completion evidence.
The note correctly marks both actual producers open.

The claims and locators in MGX were checked against the complete mass-gap
target and its review, both complete fixed-spacing construction/review units,
and the complete injectivity supplement. FLOW coverage was 1–237, 392–458
and 4824–4851; the one-loop review was checked at 353–378, AUDIT at 160–194,
and HANDOFF at 350–400. Unrelated FLOW sessions, coordinator proofs and
historical numerical runners were not independently re-audited.
Initially truncated read output was recovered with smaller complete ranges.

Primary attribution checks confirm the stated limited scope: the
[Balaban institutional record](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Renormalization-group-approach-to-lattice-gauge/991031665200104646)
identifies the 1987 effective-action/coupling paper; the
[Dimock v2 abstract](https://arxiv.org/abs/1108.1335v2) treats the scalar
three-dimensional phi4 ultraviolet problem; and the
[Shen–Zhu–Zhu v1 abstract](https://arxiv.org/abs/2204.12737v1) describes
strong-coupling lattice results. Only those records/abstracts were checked,
not imported as analytic theorems. The finite positive threshold and
compact-simple-group quantifier also agree with section 4 of the
[official Jaffe–Witten statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
No cited primary source supplies MGX's missing crossover estimate.

No numerical or symbolic experiment was run. The author's saved resource
record documents the rejected `nice` adjustment; its historical checker
counts are not independent evidence here. The proofs above are analytic.
All 15 local Markdown links in MGX resolve after excluding code spans and
indented code. An initial naive parser falsely treated `exp[...](C^n)` as
a link; that was a bookkeeping false positive, not a source defect.

**Binding fixes: none for this frozen revision.** The bounded-source domain
at 121–128 and positive weight at 186 are already present and sufficient;
the previous review's repaired findings were not reopened as defects.
The remaining scientific work is the actual uniform all-field coarse action,
localized conditional means and full source remainder on one continuum
sequence, or the direct physical-transfer estimate, together with matching
reconstruction and a surviving excited sector. Weak-window extrapolation,
a small marginal coefficient and a source-free Haar endpoint do not provide
those estimates. None of these failed shortcuts rules out the live routes.

Only `REVIEW_MGX.md` was created. No scientific source, editable prompt,
ledger, audit file or Git history was changed. The author's existing review
and recovery files are preserved. This report's LAND applies only to the
identified conditional note; its actual continuum-gap decision remains
UNDECIDED.

VERDICT: LAND
