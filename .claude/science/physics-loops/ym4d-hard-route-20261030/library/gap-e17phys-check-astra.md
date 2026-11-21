# Repo search

Codex, FINISH row 848, checking Claude Opus 5.5 row 844 at `261ef7fb5c3e4d82ad6bcc332a9b8707f82ca1e9`. Requested lane configuration: GPT-6-astra / xhigh; runtime variant and effort are not independently exposed here. Research text, not an audit; no status is granted.

The task-specific prior digest is absent. The lead's `prior/repo-search-2026-11-08.md` records searches of main and PRs 10114, 10133, 10134 and 10141. Its relevant hit is `MASS_GAP_LOCAL_BLOCK_ASTRA.md` in the older soft-route folder, §§1–2: a one-lattice-step Wilson-loop witness, explicitly not a fixed-physical-time witness. I fetched PR 10114 and read lines 90–179. Its beta-dependent bound does not supply this target; it is credited as prior work by Codex GPT-6-astra. The digest's other targets concern RG formation and covariance, not this check. This is reuse of the lead's search, not a new exhaustive absence claim.

The local `open-registry.md` has no match for `e17phys`, `E17-phys`, `SD-cyl`, `gap-assume`, `gap-finishline` or `gap-e17`. Row 848 assigns this check; row 844 is the authored text being checked, not a duplicate check. Main's workflow map and current rules were read at `bb4ec020d5ada57c630dd89acc98a68397ade423`. The lane content stays pinned at the supplied commit. No other target is attacked. A later targeted source search found the existing complex chessboard proof in P8 and SR1; Section 9 reuses it and checks only the rectangular match.

Sources: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, are credited for the outline and complete account. Each requested file was downloaded once from `31a47c543775` into the new directory `/tmp/sa-gap-e17phys-check-astra.GgsEz5/`. SA denotes `sa_ym4.tex`; CA-I denotes `sa_ca_I.tex`. Source reads use bounded ranges selected through `library/sa-index/`. No numerical or computer-assisted proof step is used.

## Checkpoint

Completed: every requested statement at the pinned source. The load-bearing inequalities hold with their named premises. The complete-account identification fails; the FL summary needs its exact endpoint. The existing P8 chessboard proof is reused. Remaining obligations are the actual analytic inputs for (SD-cyl), the complete-account match, (E17-phys), and the glue estimates. No source statement, registry or status record is changed. The report is saved locally, uncommitted and unpushed, on research/gap-e17phys-check-astra-261ef7fb5.

## 1. Lemma W(i), including the cylinder limit — HOLDS

Target lines 62–82. Inputs are (TM), its simple positive top eigenvector, the commuting flips, and the stated slab symmetry. The source contracts are `gap-crux-restate.md` §1 and `gap-transfer.md` Statement (4). This checks the implication from those inputs, not the entire earlier transfer construction.

Write R=T/lambda_0 and P=|Omega><Omega|. Compactness and simplicity give q=||R-P||<1. For m>=1,

    ||R^m-P||_1 <= q^(m-1) Tr(R-P) -> 0.

For a slab insertion, pointwise kernel domination implies
`|K_F v| <= ||F||_infinity T^w |v|`, hence boundedness on L2. Thus the trace-norm limit can be paired with `K_X T^(t-w) K_Y`. Dividing numerator and denominator by lambda_0^n gives exactly the target's cylinder formula, including the factor lambda_0^(-(t+w)). The same argument gives the one-point mean. Reflection makes K_F self-adjoint; centering `lambda_0^(-w) K_F Omega` subtracts c Omega. The mixed terms vanish. Therefore the connected cylinder correlation at separation u+w is `<psi,R^u psi>`.

The simple positive ground state is flip invariant, since a flip preserves positivity and its normalized eigenspace. The slab operator preserves that subspace. Consequently psi is even and perpendicular to Omega. No uniform rate in B or the cutoff is needed for this fixed-cutoff cylinder limit.

## 2. Lemma W(ii), log-convexity and zeros — HOLDS

Target line 84. The spectral measure of psi for R is positive and supported in [0,1). Thus `G(u)=integral x^u dnu(x)`. Cauchy–Schwarz applied to `x^((u-1)/2)` and `x^((u+1)/2)` proves the displayed inequality, including u=1 and a possible atom at zero. A zero moment at any positive integer forces nu to be supported at zero. All positive moments then vanish. This proves precisely the stated zero alternative; it need not force G(0)=0.

## 3. Lemma W(iii), even-sum lower bound — HOLDS

Target line 86. Positivity at u_2 makes G(u_1)>0. Tilt the spectral measure by `x^u_1/G(u_1)` to obtain a probability measure P (at u_1=0 this retains the zero atom). Put h=u_2-u_1. For a>=h, Jensen's inequality for the convex function `y^(a/h)` gives

    G(u_1+a)/G(u_1) = E_P[(x^h)^(a/h)]
                        >= (E_P[x^h])^(a/h)
                         = (G(u_2)/G(u_1))^(a/h).

This is a different derivation of the load-bearing extrapolation. The tilted unit vector is even and orthogonal to Omega, so its R^a expectation is at most the trace of R^a on that subspace, namely S_ev(a;B). All sums are finite or absolutely convergent since a>=1 and R is trace class. The equality case a=h is included.

## 4. Lemma W(iv), even-gap upper bound — HOLDS

Target lines 80,88. Since 0<=x<1, G decreases. Under the tilt above, `G(u_2)/G(u_1)=E_P[x^h]<=mu_1^h`. Positivity of this ratio ensures a nonzero even excitation and mu_1>0. Compactness makes the largest nonvacuum even eigenvalue exist. Taking logarithms gives exactly `m_ev<=log(G(u_1)/G(u_2))/h`. This is an upper bound on an even-sector gap, not a mass-gap lower bound.

## 5. Tent witness and Proposition W-phys — HOLDS GIVEN (SD-cyl)

Target lines 32–42,110–130. The tent meets the outline's exact Lipschitz test class (SA 6953–6960,26002–26012). Its mass is pi^2 r^5/10; with d=4r, the required mass is 256r^5/300. Already pi>3 gives pi^2/10>9/10>256/300. Thus no decimal calculation is needed. Time reflection preserves the barycentric observable, including temporal plaquettes. A spatial centre flip changes either zero or two edges of each plaquette. F is bounded at each fixed cutoff, real, gauge invariant, flip invariant and reflection symmetric.

Write h=a_K, t=ceil(3d/(2h)), w=2ceil(d/(4h)+1/2). Then wh<=d/2+3h<=7d/8<3d/2<=th. The two slab gaps t-w and 2t-w are nonnegative. The support distances are th-d/2 and 2th-d/2, lying respectively in [d,d+h) and [5d/2,5d/2+2h). Since h<=d/8, both pairs are admissible. Their union fits in a ball of radius at most 15d/8<2d.

Let I be the tent's integral and s=th. Direct support bounds give

    K_free(f,tau_2t f)/K_free(f,tau_t f)
      >= ((s-d/2)/(2s+d/2))^8 >= (2/7)^8.

The second ratio increases with s. The common class parameter d makes both running factors identical; they cancel. Positivity and the two half-error bounds give `G(2t-w)/G(t-w)>=rho_*=(2/7)^8/3>0`. Lemma W also bounds this ratio by 1. Finally a>=t follows from A>=2d and th<13d/8. Since a/t<=2A/(3d), Lemma W gives exactly `S_ev(a;B)>=rho_*^(2A/(3d))`.

The byproduct also holds: dividing the lattice gap bound by h gives `m_ev/h<=2 log(1/rho_*)/(3d)`. This conclusion stays conditional on the cylinder law. No cutoff-dependent bound on ||F|| is used in the final ratio.

## 6. The four corrections to AS §3.2 — HOLDS AFTER CORRECTION

Target line 54, compared with `gap-assume-opus.md` §3.2 and SA 6953–6960,25976–26012.

1. **HOLDS:** the required interval is the distance between supports, [d,6d]. A centre separation d with two radius-d/4 tents fails it. The new separations t h and 2t h repair this.
2. **HOLDS:** gamma=1 for these two pairs because their class parameter d is identical. This does not assume equality of running couplings evaluated at two different scales.
3. **HOLDS AFTER CORRECTION:** replace “off the account's tori the account asserts only |eps|<=1/2” by “the outline asserts that bound for its periodic full-lattice Gibbs states; (SD-cyl) separately assumes it on cylinders.” No cited theorem asserts it on every off-family geometry. The factor 1/3 is valid once (SD-cyl) is supplied.
4. **HOLDS:** the separation increment t h is at least 3d/2. After taking the square root, the sufficient exponent is A/(3d). Rounding improves the bound because the base is below 1.

These are repairs of the conditional witness construction. They establish no flux estimate. AS §3.2(a)'s positive continuum flux premise is not checked here and is not used.

## 7. (E17-phys) and the FQ corollary — HOLDS GIVEN (SD-cyl)

Target lines 44–52,132–138; consumer `gap-ext-astra.md` (FQ), lines 115–127. (E17-phys) is a hypothesis, not an estimate proved here. Its constants are fixed before K. With A=2L^m>=max(ell_star,2d), the three physical boxes have sides A or 2A, all multiples of ell_star=2L^m_star. Section 5 gives

    8 Q_F <= K_F rho_*^(A/(3d)) <= K_F sqrt(S_ev(a;B)).

The strict bound Q_F<1/192 is assumed separately. The allowed polynomial bound on K(a) holds with p_1=0 and C_1=K_F. This proves the stated corollary, uniformly over its first-passage data and shapes. It neither supplies (E17-phys) nor the six small even sums required by the glue consumer.

## 8. Lemma A and Lemma F — HOLDS

Target lines 166–172; Lemma A is `gap-crux-restate.md` §1. For positive trace-class S, write `p_i=lambda_i^k/Tr(S^k)` when S is nonzero. For l>=k,

    Tr(S^l)/(Tr(S^k))^(l/k) = sum_i p_i^(l/k) <= sum_i p_i = 1.

This proves the trace-root monotonicity used in F. The S=0 case of this inequality is immediate. For A(b), `sum lambda_i^(2k)<=lambda_0^k sum lambda_i^k` proves its stated ratio bound for S!=0. No integrality relation between the two compared side lengths is needed for monotonicity.

In each coordinate the transverse transfer operator stays fixed while that coordinate length increases. Dividing by the other three lengths preserves the inequality for the logarithmic partition density. Raising the four sides successively to one admissible cubic side N' therefore gives

    log Z_tau/|tau| >= log Z_ell'/ell'^4
                    >= V_ell'/ell'^4-C_-
                    >= V_star/ell_star^4-delta_vac-C_-.

The physical conversion is multiplication of the lattice density by a_K^(-4), as in the target. SA 26947–26962 supplies the two final *hypotheses*. Thus F needs no rectangular vacuum expansion and no rectangular analogue of ET9. It is a valid conditional floor lemma, not a proof of those supplied cubic floors.

## 9. Four-direction complex chessboard — HOLDS AFTER CORRECTION

Target lines 174–176,192,246,255. The inequality is valid. The claim that it is an unwritten new input needs correction: the complex proof already exists in `port/p8-positivity.md` §§3.2–3.3 (lines 212–281), and in `sr1.md` Lemma 2. The registry assigns P8 to `port-p8`; no new attack on that result is made here. The complete account proves `6.2:lem-chessboard-estimate`, CA-II 61205–61415, including complex conjugation and zero chessboard norms. I fetched CA-II once into the separate new directory `/tmp/sa-gap-e17phys-check-astra-ca2.Q4MW7G/` to verify this primary text. Credit remains Sussman and Alpoge, with Claude and Codex, and Codex (GPT-6 family), the author of P8 and SR1; the source credits Fröhlich, Israel, Lieb and Simon for the method.

The rectangular match is the following direct specialization of that existing proof. Replace the common cell count n_c by n_mu in direction mu and J by product_mu n_mu. Its reflection map is still `k_mu -> 2a-1-k_mu`; the two halves contain n_mu/2 cells in that coordinate. The coordinate spreading step and its zero-norm branch use only this evenness. Reflections in different coordinates commute and preserve directions already filled. No step equates different n_mu. The normalized filling proof is otherwise unchanged. The rectangular Wilson reflection input is also explicitly stated at CA-II 108696–108742; SA's split-torus proof permits arbitrary tangential periods.

Use the cell observable `exp(O(w_z))` in one cell and 1 elsewhere. Its support has a fixed margin from faces, so every plaquette edge it reads is in the cell for sufficiently fine cutoff. Reflections conjugate z in odd cells. The product of all reflected copies is `exp(O(W_z))`, and its expectation is nonnegative by reflection positivity. Hence exactly

    |M_tau(z)| <= (Z_tau(W_z)/Z_tau(0))^(1/J),
    J=|tau|/l_c^4.

This is the required four-direction complex bound. “Positive slab functions” in AM6 alone would not justify omitting the conjugations; the existing complex proof does. The known lemma should be cited, not queued again.

## 10. P2, the common normalizer on rectangular tori — HOLDS

Target lines 177–181, conditional on the named outline source-energy inputs. SA 26934–27058 was checked at the actual formulas. In a fixed coordinate, W_z has period 2l_c and is conjugated by reflection in every cell face. The two half-reference slabs are adjoints. Including the positive Wilson crossing kernel symmetrically gives a positive trace-class operator Y for a full reference period. Length q ell_star therefore gives Tr(Y^q), with the other sides held fixed. Lemma A gives `Tr(Y^q)<=(Tr Y)^q`. Applying this coordinate by coordinate proves the stated rectangular pressure comparison, including nonnegativity. No sourced RG construction on a rectangular torus is being presumed.

Using Section 9 and Lemma F cancels V_star exactly and leaves

    log |M_tau(z)| <= n_star^(-4) Re E_star(W_z)
                     +(C_++C_-+delta_vac) l_c^4.

The remaining interior energy and face series live solely on T_star. Odd-cell double conjugation makes each interior summand holomorphic; its real part is unchanged. The cutoff-uniform face bound then gives the same E° and Q as SA 27044–27058. The factor-two source-radius loss is already paid in SA 26967–26978. This proves ET5 for the reference and rectangular targets, provided the ordinary-source, vacuum-density and face-series hypotheses hold. It does not prove those analytic hypotheses.

## 11. P3, ET5–ET7 — HOLDS

Target line 183, against SA 26765–26846. The normalized functions h_omega are holomorphic, equal 1 at zero, and bounded by Q. For c_i=||F_i||_sharp/r_0, raywise Schwarz gives `|h_omega-1|<=(Q+1) sum c_i|z_i|`. On the bidisc of radii 1/[4(Q+1)c_i], the logarithm series is bounded by log 2. Its mixed derivative equals the covariance minus the same mixed derivative of E for both measures. Cauchy's estimate therefore yields exactly the factor `32 log(2)(Q+1)^2 r_0^(-2)` in ET6. A zero test is handled separately.

The signed packing uses actual common lattice translates in a nonwrapping unit ball. For sufficiently small d and a_K<=d, its disjoint radius-5d balls have N>=c d^(-4). A signed sum preserves each test's supremum and Lipschitz bound: for points in different balls the connecting segment exits both balls, at zeros of the corresponding terms. Shared independent signs in the two arguments cancel every off-diagonal pair. Translation invariance then gives N D(f,h), so division by N proves ET7 with its d^2 gain. Both torus measures have the needed joint translation invariance. Their different configuration spaces cause no problem.

The quantitative hypotheses remain “d sufficiently small” and “the unit ball embeds,” as in the source. Choose the fixed d_0 to meet them. This is already part of the outline's threshold construction, not a limit in n or a numerical check.

## 12. P4–P5 and (SD-cyl), as an outline implication — HOLDS

Target lines 185–187, conditional on the outline's *reference extraction and error budget*, not merely its final reference-torus theorem. SA 26054–26066 explicitly allocates the half-error among extraction, free-kernel/Riemann comparison and transfer. P2 supplies the identical Q, r_0 and c_M, so P3 uses that same transfer constant on rectangular tori. There is no shape or n loss. Thus the same choice of sufficiently small d_0 works; if d_0 denotes an unspecified earlier threshold, choose or shrink it once before fixing d and K_0. The relative transfer cost tends to zero because its bound is C_theta d^2 x_s^2 and x_s grows at most logarithmically in 1/d, up to the stated room factors.

At fixed cutoff, the product and each single local observable are bounded. The trace-norm argument in Section 1 therefore passes all three terms of the covariance to the cylinder. The common positive prefactor is independent of n. The closed interval [1/2,3/2] for the normalized covariance survives this limit. This proves (SD-cyl) from the named outline premises. It requires no rate of cylinder convergence uniform in K, no twisted measure, and no uniqueness assertion for an RG block law.

The geometric distinction in target §4.2 also holds. A periodically lifted finite-cylinder state on the full lattice is supported on configurations satisfying exact remote link equalities. A Wilson DLR conditional law in a sufficiently small bond region has a strictly positive density against Haar measure and does not preserve those imposed equalities. Thus it is not automatically one of the full-lattice periodic Gibbs states covered by the cited outline theorem.

## 13. Identification with the complete account — FAILS

This verdict concerns the advertised *complete-account port*, not a counterexample to (SD-cyl). Target §§4.1–4.4 repeatedly call the outline's statements “the account.” Every displayed source locator there is in SA, and target line 15 explicitly says CA-I was not fetched. Theorem 0(c)(3), Theorem 7.1 and Lemma 7.6/ET5–ET7 are the outline locators verified above.

CA-I's actual Theorem 0 has a different witness clause: (iv), lines 2715–2826. It states

    S_2 = zeta'_(K-s)^2 b_0 g_(K-s)^4 K_s^star (1+R), |R|<=1/2,

with a *lattice background-curvature kernel on the reference torus*, specified depth floors, and two cutoff-independent kernel constants bounding that kernel. It calls the Euclidean inverse-eighth-power kernel its continuum counterpart (2735–2746); it does not make that replacement with the same half-error in the displayed theorem. It also expressly excludes a claim zeta'->1 beyond its displayed range (2818–2819). This is materially different from target line 152 and its continuum-kernel error budget.

Consequently, reading CA-I (iv) alone does not supply the exact rho_* of this note: the support-distance argument in Section 5 bounds K_free, not K_s^star. For example, even a separate relative kernel approximation by delta would combine with a half-error as `(1+R)(1+delta)-1`; its positive endpoint is `1/2+3delta/2`, exceeding 1/2 for delta>0. The required reserve must be supplied by the stronger extraction/comparison argument, not inferred from the final half-error theorem. The outline explicitly retains that argument; the new note does not identify its complete-account version.

Repair: describe §§4.1–4.4 as a conditional port of the **outline** with its source-energy, density, reference-extraction and free-comparison hypotheses. Delete “exactly this conditionality, and no more” as a claim about the complete account. Alternatively identify the complete account's actual kernel comparison, depth and error reserves; this check does not invent that missing match. The exact cylinder law is not discharged for the construction by the present note. Separately, the assertion that the complete account has no complex chessboard proof is false, as Section 9 records.

## 14. Lemma FL itself — HOLDS

Target lines 205–211; `gap-finishline-opus.md` 128–132; `gap-phys-seed.md` Lemma Z'; `gap-seed-shape.md` Theorem SH and its rho>=24 row were read. T_0 is an integer, as required by the lattice setting and Z'.

The initial bound follows directly from Lemma A:

    log(1+S(T_0;b^3))
      <= 2 F(T_0,b,b,b)-F(2T_0,b,b,b)
      <= 2 rho^3 F(T_0^4)-(2/rho)F(b^4)
       = (2/rho) Phi_rho(T_0) <= log(1+s_0).

Thus the initial thermal sum is at most s_0. All SH hypotheses hold for (j,p,q)=(6,6,12), since rho>=25>12. Here C<=7/2. The case x=0 is immediate. To verify the threshold by hand, for 0<x<=3/10 put

    u=216[log(1+x^6)+C log(1+x^12)].

Then `u<=216 x^6(1+(7/2)x^6)`, `1+(7/2)x^6<1003/1000`, and `u<4/25`. The exponential series gives

    exp(4/25) <= 1+4/25+[(4/25)^2/2]/[1-(4/25)/3]
               =29/25+24/1775 <47/40.

The tail estimate uses n!>=2*3^(n-2) for n>=2. Consequently

    exp(u)-1 <= u exp(u)
       <216*(1003/1000)*(47/40) x^6
       <255 x^6 <(303/100)^5 x^6.

For the last inequality the first two binomial terms already give `(3+3/100)^5>=243+405*(3/100)>255`. Also `(303/100)*(3/10)=909/1000<1`. This verifies K=3.03 without a computed exponential or an unsupported decimal rounding.

The multiplicative recursion gives the stated s_k and its decrease. For k(2N) chosen as in SH, k(2N)>=k. SH(ii) gives the exponent `E=(6rho/(rho-1))^3`; monotonicity in time applies since `N>=6^{k(2N)} rho T_0/2>=6^{k(2N)} T_0`. Hence the FL conclusion holds for every N in its stated range. Moreover `E<=15625/64<244.2` at rho>=25. This is a composition from the named Z'/SH inputs, not a new proof of the full SH theorem.

## 15. Lemma FL's limsup application — HOLDS AFTER CORRECTION

Target line 213 has the correct exact repair. Target lines 239 and 257 replace its upper endpoint by 0.131 L; that replacement is false under the stated SEED-L hypothesis.

Use precisely

    phi_* < phi' < (L/2) log(13/10),
    s_0=exp(2phi'/L)-1 <3/10.

The uniform limsup over first-passage data gives one K_0 for Phi_L<=phi' at every admitted datum with K>=K_0. Choose k_1, independent of the cutoff, with E s_k1<=1/6000. Then the exact elementary estimate

    (1+s_k1)^E-1 <= exp(1/6000)-1
                       <=1/5999 <1/5041

supplies the strict seed margin. Here `exp(x)<=1/(1-x)` for 0<=x<1 follows term by term from its series. The physical side is 6^k1 L ell, and its half-side has lattice length `6^k1 L^(m+K+1)`, an integer. The seed's size need not be an account torus. SA 6863–6869 verifies the dilation identity at fixed beta; (K+1,beta) need not be first passage.

Explicit failure of the rounded interval: take `phi_*=(131/1000)L`. It satisfies the exact hypothesis, because the alternating logarithm series through its sixth term gives

    log(13/10) > 3/10-9/200+9/1000-81/40000
                         +243/500000-243/2000000
                  =524679/2000000 >262/1000.

But `(phi_*,0.131L)` is empty. The exact logarithmic endpoint, not that rounded decimal, must be used in the summary and RESULT. This does not change Lemma FL or its constants.

## Scope and source record

The checks above cover target §§1–5, with §§6's summary claims compared against them. Target §§3.3's area-law/correlation-length estimates are marked GUIDE and are not verified or used. The microscopic eta(beta) estimate is outside this check. Earlier TM, SH and RG analytic constructions are retained as explicitly named inputs, not re-certified. No mass gap, confinement estimate, complete-account kernel match, or status upgrade is claimed.

Bounded primary reads were SA 6844–6869,6909–6915,6953–6962,25970–26012,26054–26066,26765–26846,26868–27086,2885–2942; CA-I 2715–2826; and CA-II 61205–61415,108690–108756. The outline chunk rows and neighbouring obligations were consulted first. The account's 4.12–4.19 index was not needed: none of the checked statements refers to that tranche. Source hashes (retrieval identity only):

| Source | SHA-256 |
|---|---|
| SA | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |

RESULT: HOLDS — Lemma W(i)–(iv), the tent witness and W-phys given (SD-cyl), the FQ corollary given (SD-cyl), Lemmas A/F, ET5–ET7 and the cylinder passage under the named outline inputs, and Lemma FL; HOLDS AFTER CORRECTION — scope of the four AS repairs, reuse of the already proved complex chessboard lemma with the rectangular dictionary, and the FL application using phi_*<phi'<(L/2)log(13/10); FAILS — identification of this outline-based continuum-kernel argument as a matched complete-account port. The actual analytic premises, complete-account match, (E17-phys) and glue estimates remain unsupplied here; no mass gap or scientific status is granted.
