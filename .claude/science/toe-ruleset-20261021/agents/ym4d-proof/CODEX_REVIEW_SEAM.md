# PRE-STATED — independent hostile review of SEAM55

UTC: 2026-10-29 05:01:34. Written before derivation or execution of the checks. Preliminary exposure: the task, the project methodology, and a heading/locating-string search of SEAM55; no claimed PASS is accepted as evidence.

Scope: SEAM55, with its append-only errata overriding the earlier text; targeted ranges of the named sphere and assembly reviews/source and sm55_1/sm55_2 criteria/scripts. No git, no snapshots or audit ledgers, no whole-file PROOF read. This is the only file written. Exact rational/symbolic arithmetic only.

Refutation targets, stated in advance:

1. W0: rederive the variable-coefficient summation by parts, trace coefficient kappa, and uncancellable traceless term. A sign, missing derivative, missing uniform bound, or ODE domain assumption that invalidates cancellation or the claimed vanishing rate refutes the corresponding implication as stated. Separate the Ward, trajectory, and two-loop profiles.
2. Rates: multiply the purported small coefficients by the actual insertion bounds, with their quantifiers. A logarithmic insertion loss that defeats an asserted o(1), or a stale fixed input promoted to an output, is a refutation.
3. N5: rederive total covariance, the multilevel sum, and its rate. Test whether conditional decay alone leaves top-scale/coarse covariance. Distinguish a conditional estimate from proof of transparency; examine rough-field and defect-dimension assumptions.
4. Nonvacuity: rebuild the finite exact model and its normalization, including 26/9 and 70/27. Determine whether Lemma 3.5-prime repairs the inequality, the model, and/or the actual Yang–Mills existence problem.
5. Assembly/DIAG: test countability, tightness, fixed-R limits, scale selection, and whether all claimed inputs suffice. Compare the explicit hypotheses with CODEX_REVIEW_ASSEMBLY R2.
6. Discriminating checks: inspect both criteria and implementations, including controls. A gate that only repeats its own definition, cannot fail, ignores a required quantifier, or tests a weaker claim cannot certify the advertised result.
7. Rebuild the five inherited refutations. Verify symbol identity and actual locating strings before every load-bearing comparison; record stale citations.

Review findings use only CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses use only PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. A confirmed conditional implication never promotes its unproved inputs. Findings will be appended during the review, followed by a summary table and an exact statement of what may be banked.

# Findings

## Finding 1 — Lemma 3.5′ is valid; its exact nonvacuity witness survives

**Verdict: CONFIRMED. Claim status: PROVEN for the inequality and the model; OPEN for Yang–Mills nonvacuity.** Attachments: `SEAM55.md:334–350`, locating strings “Lemma 3.5′” and “Exact model (sm55_2”; `checks/sm55_2_criteria.md`, “Erratum to these criteria”; `CODEX_REVIEW_SPHERE.md`, “Finding 12”.

Put f(V)=E[F|V], j(V)=E[J|V]. Total covariance gives Cov(F,J)=E Cov(F,J|V)+E[(f−Ef)(j−c)] for every GLOBAL constant c. Cauchy–Schwarz gives the displayed bound with ||f−Ef||₂ inf_c ||j−c||∞. Also Var(f)=inf_d E|f−d|²≤inf_d ||f−d||∞². No fine-field variance is needed. For complex observables use complex constants and the corresponding absolute-value inequality (or real and imaginary parts); the printed real-constant form suffices for the real model.

Independent plain-Python Fraction arithmetic, rebuilt from moments rather than the author's routines, gives the following. Write Y=X²−5/3, with X uniform on {0,1,2}. Then EY²=26/9, EY³=70/27, and Var(Y²)=338/81. For each block, E[O|X]=Y and Var(O|X)=2n⁴+4X². Independence of blocks gives

    E[F|X]=Y²,
    Var F = E[(2n⁴+4X²+Y²)²] − (26/9)²
          = 4n⁸ + (344/9)n⁴ + 12482/81,
    ||E[F|X]−EF||₂ = 13√2/9,
    Cov(F,J_tau|X)=0,   Cov(F,J_tau)=70 tau/27,
    Var J_1 = 2n⁴ + 86/9.

The optimal coarse radius is inf_c sup_X |tau Y−c|=2 tau for tau≥0. The corrected upper bound is (26√2/9)tau, whereas the old variance bound is at least **4n⁴ tau**. The source's weaker (7/3)n⁴ tau lower bound is true. Squaring the corrected-bound comparison gives positive slack 7268 tau²/729. The criteria's original **14/9 is wrong; 26/9 is correct**, as its pre-script erratum already records; this is not a new uncorrected arithmetic error.

This resolves the *inequality/model* part of Sphere Finding 12. It does not prove SRC-E′_∞ for the actual Yang–Mills measure, or compatibility of the limiting observable algebra with positivity/contact extensions. In particular, “no fine-field moment” is not a proof that a collection of matching hypotheses is simultaneously satisfiable.

## Finding 2 — conditional decay does not imply transparency; the N5 sum is correct

**Verdict: CONFIRMED. Claim status: PROVEN for the Markov/covariance implication; CONDITIONAL for N5.** Attachments: `SEAM55.md:356–383`, “Proposition B on the sphere chain” and “For each FIXED j”; `:413–429`, “Theorem N5”; E8 and E9.

For a Markov chain U_0→…→U_n, set F_i=E[F|U_i], J_i=E[J|U_i]. The reverse conditional law of U_0,…,U_i given U_{i+1},…,U_n depends only on U_{i+1}. Therefore conditional total covariance gives, at each i, the preceding conditional covariance plus Cov(F_i,J_i|U_{i+1}); iteration telescopes to the stated sum. Normalized nonnegative forward kernels supply this Markov property; generic non-nested sigma-fields without that property would not suffice.

With j=n−1−i, ell_{i+1}=ell_0 L^(−j), so the decay factor is exp[−m_1 d_0 L^j/(2ell_0)]. For fixed j it has no a-dependence. The coarse covariance has no such factor. The exact model of Finding 1 has zero conditional covariance and nonzero total covariance 70/27. Thus the negative statement is decisive, not an inference from a failed search.

Applying Finding 1 and N5-C yields exactly the displayed sum plus C_F tau_*(a). If tau(r)→0, dominated convergence applies: each summand tends to zero and is bounded by L^{p(j+1)} exp(−cL^j), a summable sequence for c=m_1d_0/(2ell_0)>0. If, ADDITIONALLY, tau(r)≤C r^theta and tau_*≤C(a/ell_0)^theta_*, pull out (a/ell_0)^theta and obtain the exponent min(theta,theta_*). The printed S_{p+theta} is correct. The factor at the finest level is exp[−m_1 d_0/(2La)], not the top-level factor. E8 correctly withdraws the earlier unsupported “iff”.

## Finding 3 — the headline N5 exponent 1/2 is not a consequence of the three named qualitative inputs

**Verdict: REFUTED for the advertised rate from those inputs alone. Claim status: GAP; the explicitly power-assumed theorem remains CONDITIONAL and valid.** Attachments: `SEAM55.md:415–421` (input definitions), `:424` (“If tau…”), `:430–432` (“Rate (ARGUED…”), `:446–448` (“CONDITIONAL theorem with a rate”), and `:684–686` (“N5 (owned here)”).

N5-T* requires only tau_*(a)→0. N5-C requires only tau(r)→0. These do not specify the exponents used in the summary. An exact counterexample to this rate inference is V=X∈{−1,1} with equal weights, F=X, J_k=X/(k+1), and all fine one-step conditional covariances zero. Set a_k/ell_0=3^(−2k), Z_e=1. Then SRC-E′_∞ holds with C_F=1, N5-C holds with any positive constants and tau(r)=r^(1/2), and N5-T* holds with tau_*=1/(k+1), but

    |Cov(F,J_k)| = 1/(k+1),

which is not O(3^(−k) k^p) for any fixed logarithmic power p. This is a logical covariance-model counterexample, not a Yang–Mills counterexample. **Correction: o(1), with no universal positive power**, unless both power estimates are added as hypotheses. In the general power-assumed theorem the correct exponent is min(theta,theta_*); the value 1/2 is currently tree-level ARGUED input, not a proved consequence of the three qualitative clauses.

## Finding 4 — E1's Ward cancellation and derivative correction are algebraically right

**Verdict: CONFIRMED. Claim status: PROVEN for the algebra, CONDITIONAL on LCS-a for its matching interpretation.** Attachments: `SEAM55.md:182–227`, “Exact linearity” and “Consequence”; `:229–257`, “LCS-a” / “Theorem W0”; `:551–577`, E1; `:709–713`, E12.

The action is linear in plaquette weights, while the link vector field and its Haar divergence are coupling-independent. Thus W=W^(u0)+Xi S_eta is exact before matching. Put f_1(u)=u(1+vartheta_1^p(u)) and f_R(u)=u vartheta_R^p(u). Integration by parts of the full, variable-coefficient action contribution gives

    2N ∫ f_1(u) v·∂sbar
      = −2N ∫ [f_1(u) div v + f_1′(u) v·∂u] sbar + boundary,
    2N ∫ f_R(u) v^nu ∂_mu S^R_mu,nu
      = −2N ∫ [(f_R′(u)∂_mu u)v^nu + f_R(u)∂_mu v^nu] S^R_mu,nu + boundary.

The second term in the last bracket vanishes for symmetric traceless S and a conformal Killing v. Combining the scalar divergence with 2Nu(div v/4)(4+vartheta_D^p)sbar and the measure contribution gives

    2N(div v/4) [B_loc − kappa B_T] sbar,
    kappa = f_1′ = 1 + vartheta_1^p + u (vartheta_1^p)′,
    B_loc = u(vartheta_D^p − 4vartheta_1^p) + m_tilde,
    B_tl = −2N ∫ chi (∂_mu u)v^nu Σ_R (u vartheta_R^p)′ S^R_mu,nu.

Independently, div v=8c·x and x·v=(R²+|x|²)c·x imply v·∂log Omega=−2c·x=−div v/4. Consequently B_T=−T′ and T′=−B_loc/kappa give **c_4=0** identically. Both the measure term and any a^(−2) mixing of an a² dimension-six operator must be included in this matched B_loc; the profile supplies no proof of their values or matching.

At x=r e_1 choose J e_1=e_2 and S_12=S_21=1. Then v=Jx=r e_2 and ∂u=u_r e_1 give (∂_mu u)v^nu S_mu,nu=r u_r≠0 when u_r≠0, although v·∂u=0. This proves the nonzero geometric weight for a pole rotation. A scalar trace adjustment cannot cancel this independent tensor for arbitrary fields. It does not prove the coefficient (u vartheta_R^p)′ is nonzero; E12 correctly narrows that assertion. A constant profile or identically zero matching derivative can eliminate the term, but a nonzero-slope Ward profile cannot generically do so while retaining its scalar cancellation.

A bound |vartheta_R|≤C/u alone gives no derivative estimate: vartheta_R=sin(u²)/u has bounded u vartheta_R but derivative 2u cos(u²). If u vartheta_R is analytic and bounded by M on a complex disc of radius rho u, Cauchy's formula gives |(u vartheta_R)′|≤M/(rho u). For a differentiable perturbative Laurent expansion vartheta_R=c_R/u+d_R/u²+…, the derivative is −d_R/u²+…; the one-loop constant cancels. Thus E1's analytic **O(g²)** and formal perturbative **O(g⁴)** coefficient orders are right, with their distinct hypotheses.

LCS-a itself, its all-background source matching, contact estimates, and a profile that remains in the allowed coefficient domain are still OPEN. Lipschitz positivity gives local ODE existence; reaching the entire log interval [log a,log a+log 2] inside the prescribed weak-coupling/source domain also needs a uniform bound on B_loc/kappa and an adequate domain margin. The quoted numerical profile size in §1.5 uses an additional perturbative value and is not derived from LCS-a's positivity/Lipschitz clauses alone.

## Finding 5 — a small coefficient does not by itself imply a vanishing Ward insertion; “iff” is false

**Verdict: REFUTED for the automatic-vanishing and necessity claims. Claim status: GAP; the upper bound is PROVEN conditionally.** Attachments: `SEAM55.md:175–180`, “vanish … iff”; `:252–264`, “which is O(g_bare²)·W” and “The rate is irrelevant”; `:298–299`, “not an obstruction … (o(1))”; `:315–323`, W0 verdict; `:600–603`, E11; `:681–683`, “It vanishes”.

After E1 the actual sufficient tensor condition is

    sup |(u vartheta_R^p)′| · sup(|∂u||v|) · W(F,S^R)/Z_e^q → 0,

with the analogous scalar condition and controlled remainders. If t=log(ell_0/a), u is comparable to t, the profile gradients are bounded at fixed R, and normalized W=O(t^p), the available separate bound is **O(t^(p−1))**, or formally **O(t^(p−2))** with the stronger perturbative derivative control. It guarantees vanishing only when p<1, respectively p<2 (or when a sharper little-o product is proved). With uniform normalized W it does vanish, at O(1/t) or O(1/t²). The source correctly says this in §1.2, then drops the qualification in its conclusions.

For an exact symbolic obstruction to the inference “coefficient→0, therefore insertion→0”, take (u vartheta_R)′=−u^(−2), realized by vartheta_R=u^(−2), and a normalized insertion covariance equal to u². Their product is exactly **−1**. These coefficient bounds even satisfy the formal perturbative order and the weaker analytic bound. A finite two-point probability space realizes the covariance by F=X, S=u²X, X=±1 with equal weights. This tests the inequality logic, not the Yang–Mills coefficients. W1 must explicitly supply the product-smallness or a sufficient normalized insertion bound; if W1 is defined to assume product-smallness, the implication is valid but its vanishing is assumed there, not proved by LCS-a.

There is a second, independent error in “iff”: absolute-value/triangle bounds are sufficient, not necessary. Take two sites with J_1=X and J_2=−X, F=X, and unit weights. The integrated insertion is identically zero, while the sum of absolute covariance bounds is 2. No positive lower estimate forbidding cancellations is supplied. Correct “iff” to **“is ensured if”**. E8 repairs the same error in §2.3 but does not repair this occurrence.

## Finding 6 — trajectory matching has two different quantifiers; E7 repairs an asymptotic symbol substitution

**Verdict: NOT-VERIFIED for the unconditional trajectory-rate wording; CONFIRMED for the corrected algebraic bound. Claim status: CONDITIONAL / GAP.** Attachments: `SEAM55.md:243–245` (“+ o(1) relative”), `:266–284` (“flow's error terms cancel identically”), E1 item 1, and E7 (`:585–593`); `PROOF.md:4569–4570`, locating string “E7.3 (tuning stability)”.

Write B_eff=B_loc/kappa and let A_a be the actually used profile slope. Then exactly c_4=(B_eff−A_a)/B_eff. If A_a log L=b^W+rho_0+Delta_K and Delta_K has a limit, the triangle inequality gives precisely E7's corrected bound with leading mismatch B_eff−(b^W+Delta_infinity)/log L. The denominator requires B_eff>0; an estimate of its size requires more than that. E7.3 is an OPEN tuning-stability statement, not a proof of Delta_K convergence or its value.

The original §1.4 LCS-b has only a relative o(1) error, whereas E1 abbreviates it as the exact equality B_eff=A. Only the latter equality cancels the full running errors identically. Under the former, let A(u)=1+1/u and B_eff(u)=1+2/u. The relative mismatch tends to zero, but **c_4=1/(u+2)=O(u^(−1))**, not O(u^(−2)); an O(u^(−2)) interpolation error does not remove it. Therefore the O(g⁴) statement needs exact/quantitatively stronger LCS-b plus the specified smooth two-loop interpolation. Read E1 as imposing that stronger equality, or retain the matching error explicitly. No rate may be assigned to an unspecified o(1).

For the separate two-loop comparison, if B_eff,infinity=(11/10)(2 beta_0), the relative scalar mismatch is (11/10−1)/(11/10)=**1/11**. This number is correct. Matching the leading coefficient only removes the constant term; matching the next coefficient removes the 1/u term. The “value needed” is that of B_loc/kappa, not automatically the effective-trajectory b_infinity/log L. E7 explicitly says the first Wilson step b^W does NOT approach b_infinity. Neither sm55_1 nor the profile definition proves an identification of those quantities.

## Finding 7 — the slab classification does not prove either transparency exponent

**Verdict: CONFIRMED for the single-connection parity/counting statements; NOT-VERIFIED for the all-background estimates. Claim status: PROVEN for parity, ARGUED for tree-level scaling, OPEN for N5-T* and the transparency factor of N5-C.** Attachments: `SEAM55.md:386–407`, “Once the field is single-valued”, “theta = 1”, and “two-sided mode”; E2, E3, E9; `SPHERE55.md`, “Chern-Simons on the seam” and “No jump mode survives the first RG step”.

For one SU(N) connection, curvature has dimension 2 and a single curvature trace or differentiated single trace vanishes. Two curvatures have dimension 4. The exceptional dimension-3 CS form varies under a small gauge transformation by dQ; a variable coefficient would leave −∫dc wedge Q, so its coefficient must be constant in this local class. A coordinate reflection theta_mu reverses the orientation of the seam S³ and changes the sign of the constant-coefficient CS integral. The equatorial reflection restricts to the identity on tangential data and does NOT do that. Conversely, the four-dimensional pseudoscalar tr(F F-tilde) changes sign under theta_eq's normal reflection. These exclusions survive a reflection-even radial profile. They do not classify two-sided fields or nonlocal defect degrees of freedom.

After a single-connection description is justified, a dimension-d seam action operator has coefficient of dimension 3−d, hence tree-level size a^(d−3); displacement differentiates it once. For d=4 the displacement density has dimension 5 and coefficient a. This explains theta_*=1 for bounded smooth coarse backgrounds at fixed reference scale. It does not give a uniform supremum over arbitrary coarse fields, and absence of lower engineering dimensions does not bound anomalous dimensions or a strongly fluctuating interface flow.

Before that justification, a transporter h between two boundary connections permits tr((D_i h)^dagger D_i h), dimension 2. A jump J smooth on scale ell costs (beta_cross/a)|J|² ell³ at the seam, versus beta_bulk |J|² ell² in the bulk. Their ratio is lambda=(beta_cross/beta_bulk)(ell/a). A Gaussian/equipartition comparison gives relative RMS lambda^(−1/2), hence (a/ell)^(1/2) for comparable weights. The mean/correlation response can be O(a/ell) in that Gaussian calculation. Neither statement proves a nonperturbative exponent for every coarse V. N5-C is itself a covariance estimate; whether it carries an RMS exponent or the stronger correlation exponent must be supplied by its producer.

For finite couplings the Wilson density and the stated soft kernels are positive on all link configurations. Integrating them leaves positive density on every open set of coarse mismatches. Thus a finite RG step cannot literally delete the jump mode. The **a^(1/2) rate is an additional suppression estimate**, not a consequence of full support, positivity, or operator counting. E3 correctly withdraws the separate profile-current shell term: the chosen local current already contains that divergence part.

## Finding 8 — the diagonal selection works; the displayed paired quantifier does not imply invariance

**Verdict: CONFIRMED for diagonal selection under (A); REFUTED for full invariance from §3.3's displayed H1 alone. Claim status: PROVEN for the repaired implication; GAP in its displayed quantifier.** Attachments: `SEAM55.md:512–532`, “DIAG”, “for each k”, and “an E(4)-invariant limit”; `CODEX_REVIEW_ASSEMBLY.md`, R2 “Iterated convergence already gives the requested diagonal”.

With a COMMON countable test family and all tested observable/group pairs, H2 supplies a cutoff- and radius-uniform bound and equicontinuity. A uniform bound follows by replacing just one test factor by zero in H2; the comparison product vanishes. The contraction error is O_k(R^(−2)) in the stated compact-support seminorms. For each R_j→infinity choose an admissible cutoff a_j<1/j small enough for the finitely many pair-errors indexed ≤j to be ≤1/j and for H2 to apply. Then every fixed pair has total error O_k(R_j^(−2))+1/j→0. Boundedness gives a further pointwise convergent subsequence on a countable family; H2 extends the result within the separated test domain. No rate uniform in R is required. This is the same finite-list diagonal mechanism as ASSEMBLY R2 (whose iterated-convergence error bound is 2^(1−j)).

However, §3.3 independently enumerates {F_k} and {g_k} and assumes only the **paired** errors e_{R,k}(a). That is weaker than all (F_i,g_j). Vanishing paired errors cannot establish invariance of every F_i under every g_j.

Here is a concrete counterexample to that last inference. Let a bounded random scalar X take ±1 equally, and define a centred smooth random field Phi(z)=X z_1, independent of a and R on the pole chart. Its q-point moments are zero for odd q and are products of ∫z_1 f_i for even q. H2 follows by the product telescoping identity with p(f)=∫(1+|z_1|)|f(z)| dz. Choose a dense countable Euclidean subgroup containing infinitely many rotations fixing the z_1 axis. Pair a dense family of arbitrary products with distinct such rotations; pair every remaining group element with a distinct odd product. Every displayed H1 error is then zero (axis-fixing sphere rotations act exactly; odd moments remain zero under every transport). Yet for two separated unit-integral tests with first z_1 moment zero, the two-point function is **0**, while translation by e_1 makes it **1**. The limit is not translation invariant.

Repair: enumerate the countable CARTESIAN PRODUCT of observables and group elements, including the needed transported tests, or assume (A) explicitly for every pair. The main tree's (A) already supplies this stronger quantifier, so this repair adds no new analytic rate requirement. DIAG must not be re-dispatched as a uniform-in-R Yang–Mills estimate.

## Finding 9 — separated products do not determine the full observable algebra

**Verdict: REFUTED for identifying the stated separated family with Sphere Finding 7's complete determining-algebra repair. Claim status: GAP for full-algebra H_Euc; CONDITIONAL for separated-domain symmetry.** Attachments: `SEAM55.md:328–332`, “finite products … mutually separated supports”; `:465–476`, “determining family” and the U-sep replacement; `:541`, “agree CODEX_REVIEW_SPHERE F7”; `CODEX_REVIEW_SPHERE.md`, Finding 7 “including contact configurations”; `CODEX_REVIEW_ASSEMBLY.md`, R1 “positive-half polynomial”.

All q with mutually separated supports is a real improvement over q=2, but it still omits repeated/overlapping supports. On two-point tests the distribution h(x) delta(x−y), with smooth nonconstant h, is invisible on every separated pair and is not translation invariant. Positivity does not eliminate this ambiguity: add an independent centred Gaussian white noise of covariance h(x)delta(x−y), h>0, to an invariant field. In a product with mutually disjoint supports, no noise pair can contract, so every such moment is unchanged. Its ordinary coincident-support moments do change. The example can preserve nonzero separated correlations by choosing a nontrivial invariant base field.

Similarly, the RP quadratic form for the positive-time polynomial Phi(f)² uses S_4 on (theta f)⊗(theta f)⊗f⊗f. Positive time separates the two halves but not the repeated supports inside a half. Neither U-sep nor countable diagonal selection provides the missing contact values or their positivity-compatible extension.

The source honestly leaves “U-sep + a ^0S contraction lemma” OPEN in row 12. That leaf must include the actual observable domain, extension/regularity, multiplication and RP bridge if H_Euc is meant for the full OS algebra. Calling the separated family determining cannot replace those hypotheses. Thus the fixed-R coarse-image repair resolves one source of vacuity, not the whole nonvacuity problem identified in Sphere Finding 12. Nothing in this review proves or disproves an eventual OS construction on a properly specified alternative test algebra.

## Finding 10 — four inherited refutations survive; H10's sphere-level grade is not established

**Verdict: CONFIRMED for the scoped refutations H5, H6, H15, H19; NOT-VERIFIED for H10 on K_a. Claim status: PROVEN / CONDITIONAL as specified below; OPEN for the sphere variance lower bound.** Attachments: `SEAM55.md:615–629`, H5/H6/H10/H15/H19; `SPHERE55.md`, T2–T4, “No jump mode survives”, “beta^ = (beta/4) k_e”, and “U-mom”; `CODEX_REVIEW_ASSEMBLY.md`, R8.

| Inherited item | This review's verdict on the refutation | Independent reason and precise scope |
|---|---|---|
| H5: only dimension ≥6 rotation breaking | CONFIRMED as an incomplete classification | Finding 4 exhibits an allowed dimension-4 traceless insertion with nonzero rotation weight. E12 is essential: its actual coefficient is not computed. |
| H6: sup|c_4|→0 is the complete condition | CONFIRMED as an incomplete sufficient-input list | The independent tensor insertion remains; coefficient times its normalized insertion bound must vanish. Finding 5 also corrects the claimed necessity of the absolute bounds. |
| H10: U-mom is refuted for the sphere | NOT-VERIFIED on K_a | The incompatibility argument needs an actual variance lower bound for this regulator and normalization. The named prior reviews explicitly leave the sphere transfer open. A torus result or the exact non-YM model does not by itself establish it. |
| H15: no jump survives one step | CONFIRMED literally | The exponential soft kernel at `SPHERE55.md`, “Kernel”, is strictly positive and Haar-normalized. Together with the positive Wilson density it gives full coarse support after every finite step. Concentration is a separate asymptotic claim. |
| H19: crossing weight equals k_e beta/4 | CONFIRMED for a single fixed bulk beta | The cube action gives a sum of the incident cells' distinct beta_Q, not a fixed beta times the count. Exact local counterexample below. |

For H10, the conditional contradiction is elementary: if Var(O_a(f))≥c a^(−4)/log^r(1/a) and separated |Cov(O_a(f),O_a(g))|≤C log^s(1/a), a bounded normalized variance forces Z_e²≥c′ a^(−4)/log^r. The normalized separated covariance is then O(a⁴ log^(r+s))→0. This refutes simultaneous bounded variance and nonzero separated normalization **given those two actual bounds**. Neither the precise sphere lower bound nor its transfer from the torus is proved in the material read; ASSEMBLY R8 specifically warns about that transfer. Hence a fifth unconditional sphere refutation cannot be banked here. For a product variance one additionally needs a joint estimate; divergent factor variances alone do not suffice.

For H19 I independently enumerated the eight possible cubes incident to the edge with doubled midpoint (−3,−3,−1,0), along coordinate 4, at R/a=23/10. The inclusion rule Σ_i(|q_i|+1/2)²<(23/10)² admits only q=(−1,−1,0,0). Its three boundary faces containing the edge have centres (−3/2,−1,0,0), (−1,−3/2,0,0), (−1,−1,−1/2,0). Their squared radii are 13/4,13/4,9/4 and Omega values are 529/427,529/427,529/377, exactly. Thus

    beta_hat = [2 beta(529a/427) + beta(529a/377)]/4,

strictly less than 3 beta(a)/4 for a strictly decreasing inverse-coupling profile. Generally the correct bounds are (k_e/4) beta_min≤beta_hat≤(k_e/4) beta_max. With the supplied 3≤k_e≤6 geometry and a decreasing profile they give (3/4)beta(2a)≤beta_hat≤(3/2)beta(a). This confirms the correction without reusing the prior review's enumeration code.

## Finding 11 — the scripts reproduce and discriminate their narrow arithmetic claims; they do not test the missing inputs

**Verdict: CONFIRMED for the observed check output and the stated arithmetic scope; NOT-VERIFIED for historical pre-registration order. Claim status: PROVEN for the independently rebuilt algebra/model, OPEN for all Yang–Mills matching estimates.** Attachments: `checks/sm55_1_criteria.md`, C1–C9/X1–X5; `checks/sm55_1_chart.py:101–131`; `checks/sm55_2_criteria.md:18,48–53`; `checks/sm55_2_model.py:127–147`; `SEAM55.md:665`, “Checks”.

Observed reruns used `python3 -B` (no bytecode files). The full model check had a 45-second resource limit and completed within it. sm55_1 printed C1–C9 PASS, X1–X5 FIRED, VERDICT PASS. sm55_2 printed its eight result labels PASS, Y1–Y4 FIRED, VERDICT PASS. These are actual observed outputs, not inferred from an existing output file. Independent Fraction calculations and the local cube enumeration were run directly in memory; no check artifact was written.

The gates were examined as follows:

- C1/C2/C3/C5 compare independently differentiated chart expressions with the geometric identities; wrong profile, translation field and north sign are detected. Directly, Dphi=(R²/r²)I−2R²xx^T/r⁴ and x·v=(R²+r²)c·x yield Dphi v=−v(phi). C4's two chart factors are 1±cos t, with derivatives −1,+1 at the equator; X5 is discriminating.
- C6 is the exact inversion of d(log f)/du. C7 tests the relative slope arithmetic once B_lat is SUPPLIED. X4's 1/11 is a genuine nonzero control, but cannot decide which coefficient B_loc/kappa the lattice supplies.
- For C8, independently write B=b+c/u and h=log L. Integrating du/dh=B gives Delta=bh+ch/u−bc h²/(2u²)+O(u^(−3)); hence Delta/h−B(u+t Delta)=bc h(t−1/2)/u²+O(u^(−3)). This proves the displayed interpolation order in that model, not exact/asymptotic LCS-b for the actual trajectory.
- C9 checks rational exponent division from stipulated powers. Adding the assumed two-density coarse norm s^(−4) gives a s^(−15/2), a²s^(−8), c_4s^(−6), hence thresholds a^(2/15), a^(1/4), |c_4|^(1/6). The arithmetic is right. The gate cannot test the power count, the coarse norm, logarithmic margins, or all-q versions.
- For sm55_2, expanding a centred cell square gives A²(xi²−1)+2AXxi+Y. Its conditional variance is 2A⁴+4A²X², because E xi⁴=3 and E xi³=0. Dividing by M and using block independence proves the general formulas; finite enumerations are cross-checks. Y3 yields conditional covariances **−10/3,−4,42**, independently reproduced. Y4 changes the A⁴ coefficient from 2 to 0, so the fourth-moment test genuinely can fail.
- Y1 and Y2 are **the same nonzero-covariance witness** written twice: their tested inequalities both reduce to |70/27|>0. They are useful logical controls but are not two independent validations of the covariance mechanism. T2/T3 use the supplied closed forms; the enumeration and independent derivation supply the noncircular check of those forms.
- Both scripts merely print VERDICT and end; neither sets a nonzero process exit on a false result. A caller that treats exit status zero alone as mathematical PASS would have a non-discriminating gate. I read the printed verdicts. No such faulty outer caller is asserted to exist here.

No gate here checks LCS-a, its derivative/matching bounds for every V, the logarithmic insertion losses, N5's power exponents, the rough-field interface suppression, or the OS-domain extension. Thus all checks can pass while Findings 3, 5, 8 and 9 remain. The criteria record an erratum before script creation, but the historical creation order is NOT-VERIFIED from the permitted evidence; the present corrected criteria and code agree.

## Finding 12 — symbol and citation audit: distinguish three kappas and the two meanings of ell_0

**Verdict: CONFIRMED for the located ambiguities; NOT-VERIFIED for any numerical consequence beyond the explicit corrections above. Claim status: GAP in notation, with the intended estimates repaired as stated.** Attachments: `SEAM55.md:90–97`, symbol paragraph; E1 at `:557`; E7 at `:585–593`; `SPHERE55.md:224–230`, hierarchy/kernel; `PROOF.md:4555–4570`, E7/E7.3.

| Printed symbol | Actual object used in this review | Required separation |
|---|---|---|
| kappa in E1 | derivative d[u(1+vartheta_1^p)]/du | Call it kappa_W(u); it is a matching coefficient, not a contraction exponent. |
| kappa in L^(−kappa K), even inside E7's same paragraph | positive tuning/contraction exponent from PROOF E7 | Call it kappa_flow. No comparison with kappa_W was used. |
| kappa in the SPHERE soft kernel | fixed strength of the normalized exponential block kernel | Call it kappa_K. Positivity uses finite positive strength; no Ward matching follows from it. |
| ell_0 at SEAM55:91 | terminal reference CHART spacing | Call it ell_ref. Its physical spacing varies up to 2 ell_ref. |
| ell_i=L^(i−n)ell_0 in the same sentence | level-i chart spacing | As written, i=0 reuses ell_0 for the fine spacing. Write h_i=aL^i, h_n=ell_ref; then h_0=a. All factors in Finding 2 use this intended interpretation. |
| n in the exact model / n in the RG sum | model cell count parameter / number of RG steps | They are different integers. The model has a=1/n_model; the hierarchy has a/ell_ref=L^(−n_RG). |
| vartheta_R^p / observable-side vartheta_R | plaquette action-source coefficients / clover-observable coefficients | Distinct matching problems; W3 does not follow just by copying W0's values. R as representation label is distinct from sphere radius R. |
| B_loc/kappa, b^W, b_infinity/log L | local Ward slope, first Wilson-step running, asymptotic effective-step running | E7 repairs the substitution of the last for the second. A slope/value identification is an input, not a notation choice. |
| S, S^R, mathfrak S | action, dimension-4 tensor, seam flux | Only mathfrak S enters N5. C1–C9 are check labels, not comparison constants. |

The historical read range `SEAM55.md:67`, “PROOF.md … lines 4545–4562 at read time”, cannot locate the whole current E7 package: the current E7 heading is **4555**, and E7.3 is **4569–4570**, outside that interval. The textual E7.3 locator still resolves and states an OPEN estimate. I used those strings and the actual current range, not the old numbers. This is a locator/coverage warning, not evidence that the mathematical tuning statement changed.

The stale-input risks are substantive at three places: §1.4's o(1) LCS-b versus E1's exact equality; §2.5's merely vanishing tau/tau_* versus the half-power summaries; and §3.3's paired H1 versus (A)'s all-pairs quantifier. The scripts decide none of those transitions.

# Summary table

| Finding | Review verdict | What is established / what remains |
|---|---|---|
| 1: Lemma 3.5′ and model | CONFIRMED | PROVEN inequality; 26/9, 70/27 and all printed corrected model moments independently rebuilt. Actual YM compatibility OPEN. |
| 2: decay versus transparency; multilevel sum | CONFIRMED | PROVEN Markov/covariance algebra; N5 CONDITIONAL on its uniform inputs. |
| 3: N5 half-power summary | REFUTED as a consequence of the qualitative inputs | Only o(1) follows; min(theta,theta_*) requires explicit power bounds. |
| 4: E1 Ward algebra | CONFIRMED | PROVEN scalar cancellation and tensor structure given the stated matching; LCS-a and coefficient nonvanishing OPEN. |
| 5: W0 automatic vanishing / “iff” | REFUTED | Coefficient times normalized insertion bound must vanish; absolute upper bounds are sufficient, not necessary. |
| 6: trajectory matching | NOT-VERIFIED for the advertised unconditional rate | Exact E1 matching and §1.4 relative-o(1) matching differ; E7's corrected algebra is valid. |
| 7: seam operator/field content | CONFIRMED for parity; NOT-VERIFIED for suppression | Single-connection parity is PROVEN; theta=1, theta≥1/2 are tree-level ARGUED, not all-V estimates. |
| 8: DIAG | CONFIRMED under (A); REFUTED under displayed paired H1 alone | Enumerate all observable/group pairs; no radius-uniform cutoff rate is required. |
| 9: full H_Euc algebra | REFUTED as supplied by separated products alone | Contact/positivity/regularity extension remains an OPEN additional bridge. |
| 10: five inherited refutations | CONFIRMED for H5/H6/H15/H19; NOT-VERIFIED for H10 on K_a | H10 needs an actual sphere variance lower bound at the relevant normalization. |
| 11: checks | CONFIRMED within arithmetic/model scope | Both actual reruns PASS with controls; no analytic input is certified. Historical pre-script chronology NOT-VERIFIED. |
| 12: symbols and citations | CONFIRMED ambiguities | Separate kappas and level/reference spacings; use current E7.3 string, not the historical read interval. |

Numerical/rate corrections, with no corrected item silently counted as a new discovery:

- **14/9 → 26/9** for Var(X²), already corrected by the author's pre-script erratum. The values **70/27**, **13√2/9**, **4n⁸+(344/9)n⁴+12482/81**, and **2n⁴+86/9** survive. The weaker **(7/3)n⁴ tau** bound is not false; a sharper proved lower bound is **4n⁴ tau**.
- **N5 exponent 1/2 → no guaranteed positive power** under just tau→0 and tau_*→0. The proved conclusion is o(1). With explicit power hypotheses it is min(theta,theta_*); the exact slow counterexample is 1/(k+1) at a/ell_ref=3^(−2k).
- **Trajectory O(g⁴) does not follow from relative o(1) matching.** The admissible matching example has c_4=1/(u+2), of order g². There is no universal replacement power without quantifying the matching error. Under the stronger exact E1 matching, the two-loop interpolation calculation itself is correct.
- **A W0 coefficient order is not a covariance rate.** For normalized insertion growth t^p, t=log(ell_ref/a), the separate bounds are t^(p−1), or formally t^(p−2), not automatically a vanishing t^(−1) or t^(−2). The exact counterexample product is −1. Scalar c_4=0 for the Ward ODE and the two-loop mismatch value **1/11** are not refuted.
- **k_e beta/4 → (1/4) sum of incident beta_c.** The exact k_e=3 counterexample is [2 beta(529a/427)+beta(529a/377)]/4, not 3 beta(a)/4. The valid extrema bounds are (3/4)beta(2a) and (3/2)beta(a) under the stated geometry/monotonicity assumptions.

Coverage: only the user-named science/check files and the two procedure files `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md` were read. PROOF was searched by string and only the small 4540–4580 range was opened. No snapshots, ledgers, git commands, external searches, source edits, extra deliverables, or non-exact numerical jobs were used. SEAM55's E12 remained its last erratum at the final locator check. The review does not authenticate model-family metadata or historical creation order from prose assertions.

**Single most dangerous unverified bridge:** a nontrivial, positivity-compatible observable algebra extending the separated products. The coarse-image replacement removes the invalid fine-variance dependency from the local covariance proof, but it does not supply contact extensions or the RP forms needed for a full OS algebra. A proof of separated Ward identities and a successful diagonal can coexist with failure to establish that bridge. Within the seam estimate itself, N5-T* and N5-C's transparency factor for rough coarse fields also remain OPEN.

# Exactly what may be banked

1. **PROVEN:** Lemma 3.5′, its n-uniform exact model, and the exact counterexample “perfect conditional decay does not imply zero total covariance”. This repairs the covariance-inequality part of Sphere Finding 12.
2. **PROVEN algebra / CONDITIONAL matching implication:** the E1-corrected source summation by parts, kappa_W=d[u(1+vartheta_1^p)]/du, scalar c_4=0 for T′=−B_loc/kappa_W, and the remaining independent traceless structure. Analytic relative-disc bounds give coefficient O(g²); a differentiable perturbative expansion gives formal O(g⁴). Ward restoration additionally needs the actual normalized insertion products to vanish, uniformly along each path.
3. **PROVEN implication / CONDITIONAL application:** the multilevel N5 sum and its qualitative o(1) conclusion from the three uniform hypotheses. The min(theta,theta_*) rate is bankable only with the explicit power hypotheses. No actual Yang–Mills transparency exponent is banked.
4. **PROVEN within the single-connection local class:** CS exclusion by theta_mu and the pseudoscalar exclusion by theta_eq. **ARGUED only:** the associated engineering exponents and Gaussian jump suppression. Finite-step jump elimination is refuted.
5. **PROVEN conditional selection:** (A) for every observable/group pair, the common normalized observable identifications, and H2 yield a joint lattice diagonal and invariance on the controlled separated domain. Enumerate the Cartesian product. This uses no new radius-uniform Ward rate; it is the same finite-list selection mechanism as ASSEMBLY R2.
6. **CONDITIONAL assembly only:** after adding a precise positivity/regularity/contact-domain bridge, the requisite all-product W1/W3/coarse-image estimates, L1-sphere, LCS-a and the two seam-transparency inputs, one may assemble the intended full-algebra H_Euc implication. The present review banks none of those unproved Yang–Mills inputs, no full OS state, no mass gap, no flat-torus identification, and no unconditional constructive Yang–Mills theorem.
