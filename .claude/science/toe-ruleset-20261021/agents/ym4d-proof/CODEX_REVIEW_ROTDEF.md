# PRE-STATED

Independent hostile review of `ROTDEF.md`, initiated 2026-10-28. This section was written before reading the target or its proposed checks. Prior exposure: the user's six-claim synopsis, the repository science workflow, and review procedure. No git operations; the only authorized written artifact is this file. Exact symbolic and integer/rational arithmetic only. Literature recollections, if used, will be marked `[m]`; unverified recollections will not supply proof.

The decision rules are **CONFIRMED** (a proof or exhaustive exact check covers the stated domain), **NOT-VERIFIED** (the supplied argument does not discharge a necessary obligation), and **REFUTED** (an explicit contradiction or counterexample covers the actual quantified claim). A narrower correct statement will be separated from a stronger unsupported one. Every finding will identify its source file and a locating string.

Pre-stated attacks:

1. Derive the finite-lattice change-of-variables/IBP identity independently, including Haar divergence, the action variation, observable variation, torus seams, cutoff support, and connected/normalized terms. Distinguish pointwise identities from identities after integration. A nonzero omitted term refutes the advertised exact formula.
2. Independently classify local gauge-invariant dimension-4 and dimension-5 candidates and the relevant signed-permutation representations. Check what a representation exclusion actually proves about derivatives, external sources, contact terms, nonlocal structures, and the existence/nonvanishing of dimension-6 terms.
3. Re-derive total covariance with the reference-scale sigma-algebra; track all conditional means, contact terms, source factors, denominators, and cutoff errors. Check that the actual CD/SRC hypotheses bound every discarded term uniformly and imply the claimed single-covariance remainder.
4. Test the exact implication between a vanishing defect derivative, vanishing coarse covariance, and pairwise rotation invariance, including limiting, angular-uniformity, and normalization requirements.
5. Derive the radial/cutoff estimate behind the log-Cesaro decay claim. Try narrow-shell and sign/angular counterexamples, distinguish ordinary decay from averaged decay, and examine invariant-mixture cross terms and the scope of uniqueness comparisons.
6. Re-derive the tensor statement at ranks 0 through 4, with the exact discrete symmetry group stated. Rerunning author code alone will not count as independence.

The review will end with exactly the statements that may be banked and the hypotheses they still require.

## Scope and source identity

The target was read in full, including §12's requested checking order and all E1–E10 corrections. In particular, the verdicts below incorporate **E4's centered product**, **E5's support collar**, and **E6's uniform convergence on derivative-test families**. Findings already repaired by these errata are not presented as outstanding discoveries.

All paths below are relative to this review's directory, unless stated otherwise. Reviewed target SHA-256:

    413261674aaafa7c68793e9f10ebc1421fdf92871bd583f7c654981511104bf2  ROTDEF.md

Both rd55 scripts, their criteria, and their supplied output were read. Both scripts were run with Python's bytecode writing disabled. Each captured stdout agrees exactly with its supplied output. Independence is supplied by the separate signed-orbit calculation and component arguments below, not by rerunning author code.

Necessary dependency excerpts were checked: REVIEW_S22.md, “Statement (BFT)”; RLARGE.md, “The exact chain”, “Flow hypothesis (F_R)”, and “Theorem RLF, v3”; PROOF.md, “Decision 4: the RG kernel” and “Lemma D4-norm”. Those reads verify what is being assumed and the kernel definition; they do not verify BFT, RLF, the flow, or the broader project. The local science workflow and review-loop procedure were used within the user's narrower review-only scope. No git, source fixes, additional output files, subagents, or literature-based premises were used. Literature recollections in the target remain unverified [m].

## Verdict on the six requested claims

| Claim | Verdict | Exact scope and source locator |
|---|---|---|
| 1. Exact identity and radius independence | **CONFIRMED** | ROTDEF.md, “Proposition 3.2”, “Corollary 3.4”, E4–E5: the Wilson-expectation identity, including Haar divergence, and cutoff independence of its covariance. This is not a pointwise Ward equality or an identity for arbitrary configuration laws. |
| 2. Dimension and counterterms | **CONFIRMED** for the local representation exclusions; **NOT-VERIFIED** for a nonzero dimension-6 coefficient of this particular insertion; **REFUTED** as a claim that R2 and parity exclude every finite contact structure | ROTDEF.md, “R2 (CHECKED, C5)”, “has operator dimension exactly 6 (C7)”, “No O(1) or power-divergent contact counterterm is needed”. The vector part allows a finite contact with a dimension-5 divergence; see Finding 3. |
| 3. Source renormalization | **CONFIRMED** as centered algebra and a conditional use of SRC-O; **NOT-VERIFIED** as a derived estimate | ROTDEF.md, “The complete list of source counterterms”, “SRC-O”, E4. Three possible dimension-5 vector structures are correctly identified. Their O(g_bare²) coefficients and the useful, nonvacuous normalization remain inputs. |
| 4. One-covariance conditional reduction and equivalence | **CONFIRMED**, conditional on the actual CD/SRC inequalities and E6 | ROTDEF.md, “Theorem 7.1”, “Corollary 7.2”, “Corollary 7.3”, E6. The necessary quantity is TQ/Z_e². Strict locality of its conditional factors is **NOT-VERIFIED**. |
| 5. Log-Cesàro criterion, mixtures, uniqueness | **NOT-VERIFIED** as the complete claim stated | ROTDEF.md, “Proposition 8.1”, “Proposition 8.2”, “Remark 8.5”. The averaging mechanism is correct, but the lattice-to-integral estimate needs an envelope/sampling hypothesis. Fixed-observable fine torque is affine; state-by-state centering changes that formula. Logical independence from uniqueness under the same YM premises is not established. |
| 6. Low-rank tensors | **CONFIRMED** | ROTDEF.md, “Every H(4)-invariant symmetric tensor of rank ≤ 3”; checks/rd55_tens.py. The subsequent scale-separation estimate remains **NOT-VERIFIED**, conditional on the additional SRC-iso statement. |

The central conditional reduction survives hostile checking. Its proposed algebraic justification for all contact bounds does not. The result is an exact Ward decomposition plus a useful conditional reduction, not a proof of the asserted UV estimates or rotation invariance.

## Finding 1 — The finite-volume Ward calculation retains the measure term

**CONFIRMED.** Source: ROTDEF.md, “Lemma 3.1”, “Proposition 3.2”, “Lemma 3.3”, “Corollary 3.4”; PROOF.md, “Decision 4: the RG kernel”.

On the compact product of SU(N) groups, a left- or right-invariant derivative has zero Haar divergence. For a smooth vector field with variable coefficients,

    0 = ∫ div(F exp(−S) Ξ) dU
      = ∫ exp(−S) [ΞF + F div Ξ − F ΞS] dU.

Consequently W = ΞS − div Ξ, ω(W) = 0, and

    ω(ΞF) = ω(FW) = Cov_ω(F,W).

There is no configuration-space boundary, and the coefficient derivatives are included in div Ξ. The projection π of plaquette holonomies is smooth on the whole group; no logarithm chart or small-field restriction is needed for this step. Combining left and right vector fields does not omit an additional Jacobian.

For two cutoffs which agree at all bond midpoints on which F depends, their vector-field difference annihilates F **pointwise**, even though its coefficients can depend on other links. Applying the preceding identity gives equality of the two **expectation covariances**. This is a strong and correct locality statement. It does not require decay.

For the centered observable, set A_f = O_a(f) − ω(O_a(f)) and F̃_s = A_{f_s}A_{g_s}. The exact source term should be read as

    C(s) = ω(Ξ F̃_s) − dω(F̃_s)/ds.

The derivative of each centering constant multiplies a centered observable of mean zero. Thus the expectation identity and the connected version of §4.2 are exact with this definition. No Poisson-summation remainder is needed when the defect itself is defined using F̃, as requested here.

The spatial shell formula is also correct. The forward product rule has ψ(x+a μ̂) multiplying J, and pairing the μν and νμ terms gives precisely

    J_{νμ}[ψ(x+a μ̂) − ψ(x+a ν̂)] T_{μν}(x),  μ<ν.

This second term must be kept; the target keeps it. Periodic summation by parts is valid when the cutoff is embedded as prescribed. Use the conservative E5 range r ≤ R/4 − a throughout. Tori with no admissible radius do not furnish an instance of the proposed cutoff construction.

**REFUTED as an unrestricted-law extension.** Source: ROTDEF.md, “Its r-independence is exact … for every configuration law” in Remark 3.5. For a changed law proportional to q exp(−S)dU, the Ward functional is

    W_q = W − Ξ log q.

One cannot keep W from the Wilson density and assert the same covariance identity for arbitrary laws. The correct confirmed statement is for the Wilson measure, or for another density with its own corresponding Ward functional. Likewise, “every configuration” can mean that the integrands are globally defined, not that integration by parts holds separately at each configuration.

## Finding 2 — The representation exclusion is genuine; C7 has a narrower conclusion

**CONFIRMED.** Sources: ROTDEF.md, “R1”, “R2”, “P (inversion parity)”, “Lemma 4.1”, “Lemma 4.2”; checks/rd55_rep.py, “def chiS2A” and “C6 control”.

Here H(4) is the full signed-permutation group, including reflections. The operator class is local, gauge-invariant continuum polynomials in F and covariant derivatives, with constant equivariant contraction tensors. Canonical dimension, not an already established nonperturbative scaling dimension, is being counted.

An independent component proof of R2 avoids the author's character formula. Fix an output component A_pq, p≠q. Under independent axis sign changes it has character s_p s_q. A quadratic monomial in two curvature components has this character only if its two edges share a third index k: it is proportional to

    tr(F_pk F_qk),  k ≠ p,q.

Transposition of the p and q axes fixes each of these products, because the trace bilinear is symmetric. The target antisymmetric component A_pq changes sign. Every coefficient therefore vanishes. This proves Hom_H(A,Sym² A)=0. No equation of motion is used.

Similarly, sign invariance permits only the squares of the six curvature components in a scalar quadratic invariant, and axis permutations identify their coefficients. There is one scalar. The determinant-twisted scalar is the alternating contraction of complementary curvature pairs. The Hodge map intertwines A with A⊗det.

Total inversion gives parity (−1)^δ to a polynomial of canonical dimension δ. It acts as +1 on A, excluding odd-dimensional A-valued polynomials. For SU(N), traces of a single curvature or its covariant derivatives vanish, so no nonconstant gauge-invariant field polynomial of dimensions 1–3 supplies an exception. The identity operator of dimension zero must still be treated separately in contact expansions; it does not disappear from the operator algebra.

The dimension-5 vector enumeration also checks out within this polynomial class. The invariant six-index contractions have even-multiplicity partitions 2+2+2, 4+2, or 6. The last vanishes because of curvature antisymmetry. The first two give exactly the contractions listed in Lemma 4.1. Independently,

    I_ν = Σ_{μλ} tr(F_{μλ} D_μ F_{νλ})
        = (1/2) ∂_ν tr F² − I_ν,

by the Bianchi identity and μ↔λ interchange, hence I_ν = (1/4)∂_ν tr F². The surviving vectors are divergences of the scalar, diagonal traceless, and off-diagonal symmetric dimension-4 tensors. This confirms the three structures, not their quantum coefficients.

The independent signed-orbit calculation under one axis reflection and the three adjacent axis transpositions returned:

| Representation | Exact invariant dimension |
|---|---:|
| Sym² A | 1 |
| A ⊗ Sym² A | 0 |
| A ⊗ Λ² A | 1 |
| A ⊗ A | 1 |

Thus the positive control detects an A in the antisymmetric product, while the symmetric product has none. The independent implementation is included below.

**CONFIRMED, existence of an allowed dimension-6 anisotropy.** Source: checks/rd55_rep.py, “C7”; ROTDEF.md, “A dimension-6 H(4)-invariant that is not O(4)-invariant exists”.

For polarization e=(0,0,1,0), use equal-length wave vectors k=(5,0,0,0) and k′=(3,4,0,0), related by the exact rational rotation with cosine 3/5 and sine 4/5. The cubic density Σ_{μν} k_μ²F_{μν}² is respectively **625** and **337**; the rotational control Σ_{μν}|k|²F_{μν}² is **1250** in both cases. These are integer calculations. The normalized cubic values are 1 and 337/625.

**NOT-VERIFIED, “exactly 6” for this specific Ward remainder.** Source: ROTDEF.md, “has operator dimension exactly 6 (C7)”, §4.3. An allowed nonzero operator in an operator space does not establish a nonzero matching coefficient in the particular W+T constructed from the stated lattice vector field. C7 evaluates an example polynomial, not the expansion of that W+T. No explicit matching calculation for the identity's own current is supplied. Nor does a representation calculation establish the a² times logarithms estimate in rough-field quantum correlations.

What follows without that missing matching calculation is: **dimension 6 is the first allowed nontrivial local A-valued canonical dimension, and dimension-6 hypercubic anisotropy exists.** The analytic suppression is separately assumed in SRC-W. This review has not shown that the particular coefficient vanishes.

## Finding 3 — The blanket contact exclusion loses derivatives of the source

**REFUTED as a selection-rule assertion; the actual coefficient is NOT-VERIFIED.** Source: ROTDEF.md, §4.2, “The total-derivative part produces only J·X_[μν] = 0 plus shell terms” and “No O(1) or power-divergent contact counterterm is needed”; compare its own preceding formula “−Σ(∂_μf)(Jx)^νX_{μν}”.

R2 excludes a dimension-4 **field polynomial by itself** in A. It does not classify an entire contact distribution with vector-field factors, derivatives, and test functions.

The target explicitly retains a vector dimension-7 part in the bulk:

    a² ∫ v^ν(x) R_{7,ν}(x) dx.

In its product with the dimension-4 scalar insertion e(y), the following finite contact is allowed by gauge invariance, H(4), inversion parity, and engineering dimension:

    a² R_{7,ν}(x)e(y)  ⊃  c δ⁽⁴⁾(x−y) ∂_μ X⁽⁴⁾_{μν}(y),

where X is any of the symmetric dimension-4 tensors in Lemma 4.1. Before multiplication by a², this is an a⁻² mixing. Both sides displayed have dimension 9: 7+4−2 = 4+5. Both carry V, not A. Parity permits dimension 5 in V.

Insert this contact with the observable's weight f(y). In the region where v=Jy,

    c ∫ f(y)(Jy)^ν ∂_μX_{μν}(y) dy
      = −c ∫ (∂_μ f)(Jy)^ν X_{μν} dy
        −c ∫ f J^ν_μ X_{μν} dy
      = −c ∫ (∂_μ f)(Jy)^ν X_{μν} dy.

Symmetry kills only the second integral. The first generally survives and is supported at the observable, not at the far shell. For X_{μν}=δ_{μν}e, it is c O(Jf). Paired with the other centered observable it contributes

    c Cov_ω(O_a(Jf), O_a(g)),

which is not removed by centering. The traceless diagonal and off-diagonal choices give the other two source structures. The target already recognizes precisely these terms on the observable side. Its contact paragraph drops them on the insertion side.

This is an explicit symmetry-allowed finite contact structure, not a claim that its coefficient has been computed for Wilson YM. It refutes “R2 and P remove every O(1) contact”; it does not prove that this particular coefficient is nonzero or disprove the assumed SRC-W inequality. The three source mixings and contact matchings must be analyzed together, with coefficients or exact Ward cancellations established.

For the isolated A-valued dimension-6 part, R2 does exclude a zeroth-source-jet contact into a dimension-4 field polynomial. That narrower useful exclusion survives. Identity contacts and derivatives of contact distributions still require their own connectedness/source-jet analysis.

The same limitation applies to nonlocal/coarse structures. At fixed U_K the conditioning field is not H(4)-invariant; it transforms as additional data. An equivariant coefficient depending on that data can carry the required indices. The local polynomial calculation alone says nothing about such coefficients or nonlocal functionals. Source: ROTDEF.md, SRC-W, “the conditional measure, where H(4)_y holds only up to a positive power”. No quantitative estimate proving that last claim is supplied.

## Finding 4 — Renormalization cancellation is algebraic; SRC-E is stronger than coarse moments

**CONFIRMED as algebra; NOT-VERIFIED as an analytic construction.** Source: ROTDEF.md, “The complete list of source counterterms”, “SRC-E (local moments)”, “SRC-O”, E4.

An additive constant cancels exactly from A_f. Dividing the centered two-point function by a common, state-independent Z_e² defines its multiplicatively normalized version. These statements do not prove existence of a useful Z_e or smallness of the remaining finite coefficients. SRC-O explicitly assumes the needed bound, so Theorem 7.1 may use it. Classical smooth-field consistency alone does not prove nonperturbative O(g_bare²) matching uniformly through K RG steps.

There is a further nonvacuity issue in SRC-E. For any real G, exactly,

    ν_K[(E_K G)²] + ν_K[Var(G|U_K)] = ω(G²).

Thus the proposed “local moments” assumption bounds the **full fine-field second moment**, not merely the conditional mean at reference scale. For centered O_a(f), it bounds Var_ω(O_a(f))/Z_e². For F̃ it bounds its full second moment, whose square repeats each test support. Separation of f and g does not remove those repeated-support coincidences. The clause for point densities of T is stronger still.

The target itself says, at “Normalizing by Var(O_a(f)) would be wrong”, that this variance has an a⁻⁴ divergence by its short-distance power counting. Centering does not change a variance. The supplied text does not reconcile that assertion with SRC-E and a normalization that preserves a nonzero separated correlator. This is a real additional proof obligation, not a deduction here that the Wilson assumptions are inconsistent. A plausible repair is to formulate the moments actually needed for conditional/coarse observables and separated inserted correlations, rather than silently asserting finite fine-field L² norms.

No lower bound excluding a zero normalized correlator is supplied. The target acknowledges this. Therefore none of this normalization work banks non-freeness or a nontrivial continuum observable.

## Finding 5 — Exactly one coarse covariance remains, if the full bounds are assumed

**CONFIRMED.** Source: ROTDEF.md, “Lemma 5.1”, “Lemma 5.2”, “Lemma 5.3”, “Theorem 7.1”.

The normalized soft kernels give the Wilson U_0 marginal by successive integration. Conditional covariance is taken under this full joint chain. Write Γ_v = Ξ_v log K_0(U_1,U_0). Differentiating the **normalized** K_0 includes differentiation of its normalizing factor. Conditional integration by parts gives

    E_K[Ξ_v G] = E_K[G(W−Γ_v)],
    E_K[W−Γ_v] = 0.

Hence the conditional covariance form in Lemma 5.3 and E_K W = E_K Γ_v follow. Combining this with total covariance gives, with the sign in the target,

    Cov_ν(E_KG,E_KW) = −ν_K Cov(G,Γ_v|U_K).

No additional coarse-measure Jacobian is missing; its response is represented by Γ_v.

Now set B_r=W(v_r)+T_r and J_r=E_K T_r. Independently of any expansion,

    dω(F̃_s)/ds + Cov_ν(E_KF̃_s,J_r)
      = −ν_K Cov(F̃_s,T_r|U_K)
        + Cov_ω(F̃_s,B_r) − C(s).

This is the exact identity that should be banked. There are no missing mean products. The entire bulk covariance is bounded by SRC-W as stated, so it need not be split again and does not leave another uncontrolled coarse covariance **under that hypothesis**.

The shell coefficients are bounded independently of r; its volume is O(r⁴). CD therefore bounds the first term by Z_e² times O(r⁴ exp(−m_c r)), with the fixed support collar absorbed in the constant/exponent shift. SRC-W bounds the second by Z_e² a² L(a)r⁵, and SRC-O bounds the third by Z_e²[g_bare²+a²L(a)]. These are precisely the dependencies of Theorem 7.1.

Two scope distinctions matter:

1. The formal CD statement at §6 allows a prefactor C_G(U_K) with a uniform **ν_K-average** bound. It does not assert a pointwise U_K-independent prefactor. This averaged version is sufficient for the displayed proof. BFT locality and RLF probability estimates do not themselves supply it.
2. SRC-W is already the desired full bulk-covariance estimate, including contact regions. Theorem 7.1 is a valid implication when this is assumed, even though Finding 3 invalidates the asserted automatic symmetry justification for it. One cannot report those contact estimates as independently derived.

The existence of a tensor called the “identity's own current” with this estimate is also part of SRC-W. W=−T+B by definition for any chosen symmetric T; that identity does not construct or bound the special current.

**NOT-VERIFIED, strict coarse locality.** Source: ROTDEF.md, §5.2, “a local functional of U_K” and “an explicit sum … of local coarse functionals”.

Conditional expectation of a local observable need not be a function of only nearby coarse variables. A normalized, strictly positive local observation kernel does not change this fact. An exact two-site illustration is:

    P(X=x,Y=y) = (1+xy/2)/4,
    K(V=v|X=x) = (1+vx/2)/2,
    K(W=w|Y=y) = (1+wy/2)/2.

All variables take values ±1 and all probabilities are positive rationals. Then

    E[X|V=v,W=w] = (v/2+w/4)/(1+vw/8),
    E[X|V=1,W=1] = 2/3,
    E[X|V=1,W=−1] = 2/7.

The conditional image depends on the second coarse variable. Longer interacting chains give the analogous issue at greater distances. This is a counterexample to the proposed general locality inference, not a Wilson-YM counterexample. A separate conditional response/quasilocality estimate would be needed for the particular chain. The algebraic one-covariance reduction does not need strict locality.

## Finding 6 — The equivalence is valid with E6 and the normalized torque

**CONFIRMED with the amended hypotheses.** Source: ROTDEF.md, “Corollary 7.2”, “Corollary 7.3”, E5–E6.

Subtracting the exact identities at two radii cancels C(s), including its finite source mixings. This justifies the absence of g_bare² in ε′. In reference units use

    r_j = min{R_j/4 − a_j, a_j^(−1/3)}

for sufficiently large j. Then r_j tends to infinity and a_j²r_j⁵L(a_j) ≤ a_j^(1/3)L(a_j) tends to zero. Together with the flow assumption and CD this gives the diagonal estimate.

For necessity, E6 is essential to the proof as written: convergence on both the original test pairs and their derivative-test pairs permits passage to dS(f_s,g_s)/ds, uniformly in s. Mere convergence of functions to a continuous constant would not do this; sin(js)/j is an elementary counterexample to that inference. E6 explicitly repairs it.

Consequently, for the amended centered correlators,

    S(f_s,g_s) = S(f,g) on the tested orbit
        ⇔ lim_{r→∞} limsup_j sup_s |TQ_{ν_j}(s;r)|/Z_e(a_j)² = 0.

It is the **normalized** torque that occurs in the equivalence. Replacing it by unnormalized TQ→0 requires additional bounds on Z_e. The tested one-parameter rotation orbit is also a narrower conclusion than OS1 for the full observable algebra. Extending the statement to all generators and test pairs requires the corresponding families of hypotheses.

## Finding 7 — The Cesàro mechanism works, but literal DEC misses lattice sampling

**CONFIRMED, cutoff averaging.** Source: ROTDEF.md, Proposition 8.1, “Since h′(t) ≠ 0 only for t ∈ [1,2]”.

For H=log(r₂/r₁) and ψ̄=H⁻¹∫_{r₁}^{r₂}ψ_ρ dρ/ρ, the exact radial estimate is

    |∂ψ̄(y)| ≤ ||h′||∞ H⁻¹ ∫_{|y|/2}^{|y|} dρ/ρ²
              = ||h′||∞/(|y|H).

The forward differences satisfy the corresponding bound by integration along their bonds. Thus the averaged shell coefficients are O(1/H). Quasi-independence of the radius is the ingredient that lets a small averaged torque control a particular large-radius torque. Without it, sparse large torques would defeat a Cesàro argument.

**REFUTED, the displayed sum-to-integral bound for arbitrary ε; NOT-VERIFIED, Proposition 8.1 under literal DEC alone.** Source: ROTDEF.md, line 447, “|∫TQ_ν dλ| ≤ … ∫ … ε(ρ)dρ/ρ”.

The preceding exact bound at finite lattice spacing is a lattice sum:

    |∫ TQ_ν dλ|/Z_e²
      ≤ C/H Σ_{x in the enlarged shell} a_j⁴ ε(|x|)|x|⁻⁴.

No monotonicity, radial regularity, cell-majorant estimate, or discrete Cesàro hypothesis on ε is stated. Its ordinary radial integral need not control this sum.

Here is an exact obstruction to that inference. For the countable sequence of fine tori define the countable set

    D = { |x| : x is a fine-lattice site of any torus in the sequence, |x|≥r₀ }.

Let ε(ρ)=1 on D and 0 elsewhere. Its Lebesgue integral on every finite radial interval is exactly zero, so the written log-Cesàro integral condition holds with value zero. Yet at every sampled site ε(|x|)=1. Any bound of the form C|x|⁻⁴ at lattice sites satisfies this version of DEC, with no improvement whatever at those sites. The positive lattice sum cannot be bounded by a constant times the zero radial integral.

This is a precise counterexample to the estimate used in the proof. It is **not** a constructed Wilson measure satisfying all inputs and violating OS1. Consequently I do not label the full YM proposition refuted. If the author intends a Riemann-integrable or regular decay envelope, that condition must be included; the present statement does not say it.

A direct repair is to assume the actually needed discrete averaged bound, uniformly in j and s:

    (1/log(r₂/r₁)) Σ_{r₁−a_j ≤ |x| ≤ 2r₂+a_j}
        a_j⁴ Σ_{μν}|Cov_ν(E_KF̃_s,E_KT_{μν}(x))|/Z_e² → 0,

with the relevant sequential limits/admissible tori. Alternatively require a suitable radial cell majorant, or a locally Riemann-integrable envelope and take j→∞ for each fixed r₁,r₂ before sending r₂/r₁→∞. Fixed annuli then admit ordinary Riemann-sum convergence; Corollary 7.2 supplies the comparison with r₁. The logarithmic averaging argument is confirmed under either justified replacement.

**CONFIRMED, the stated ordinary examples as sufficient estimates.** Sources: ROTDEF.md, Proposition 8.1, “ε=1/log ρ”; Remark 8.4, “|x|⁻⁸”.

For these regular monotone envelopes there is no sampling defect. A uniform |x|⁻⁸ bound gives a shell sum O(r⁻⁴), and a uniform |x|⁻⁴/log|x| bound gives O(1/log r). Either sends the normalized torque to zero. Exponential decay is unnecessary for these estimates. The powers and integrals used here are exact; no numerical asymptotics were fitted.

The free massless comparator's Wick-counting mechanism is consistent: for a separated product of centered quadratic observables and a quadratic stress insertion, a connected contraction has two propagators crossing to the distant stress. If each curvature propagator decays as |x|⁻⁴, the result is O(|x|⁻⁸). This is a comparator, not a gapless nonabelian YM construction, and no literature recollection is needed to infer the two-crossing power from Wick contraction.

## Finding 8 — E4 changes the mixture statement; uniqueness remains unresolved

**CONFIRMED for a fixed observable.** Source: ROTDEF.md, Proposition 8.2, “ω_i(T_r) … tr J = 0”.

For translation- and H(4)-invariant component states and a common tensor T, its mean is τ_iδ_{μν}. Summation by parts with the cutoff gives ω_i(T_r)=0 exactly. Therefore, for a **single fixed** G used in every component,

    Cov_ω(G,T_r) = Σ_i p_i Cov_{ω_i}(G,T_r).

That is the correct affine identity.

**NOT-VERIFIED for the state-centered TQ after E4; the omitted-term calculation is REFUTED.** Source: ROTDEF.md, Proposition 8.2, “TQ^fine_ω … exactly”; E4, “Throughout §3–§8 … centered product”.

Let A=O_a(f_s), B=O_a(g_s), a_i=ω_i(A), b_i=ω_i(B), a=Σp_i a_i, and b=Σp_i b_i. With ω_i(T_r)=0 the exact formula is

    TQ^fine_ω
      = Σ_i p_i TQ^fine_{ω_i}
        + Σ_i p_i [(a_i−a) Cov_{ω_i}(B,T_r)
                    +(b_i−b) Cov_{ω_i}(A,T_r)].

Here each component's TQ uses its own centered pair, as E4 prescribes. The final line is absent from the target's proof. Neither the mean-zero torque nor the stated CD/SRC hypotheses for the centered pair set these one-observable covariances to zero. E4 itself warns that single-observable shell and bulk pieces need not be small enough after multiplication by the divergent means.

This is not merely a distinction between connected and disconnected notation. A simple rational algebra diagnostic has two equally weighted components. In component 1 take X=±1 equiprobably and A=B=1+X, T=X. In component 2 take A=B=−1, T=0. Each component has mean-zero T and zero centered-pair torque. The mixture has means a=b=0 and centered-pair torque **1**. This diagnostic tests the missing covariance terms; it is not a YM state.

Nor does translation/H(4) invariance alone repair the missing-term inference. An exact spatial diagnostic can be made on (Z/64Z)⁴. Take independent symmetric signs η_z and

    φ_x = η_x + (1/2)Σ_{μ=1}⁴[η_{x+12e_μ}+η_{x−12e_μ}].

In two equally weighted invariant component laws set e_x=m_i+σ_iφ_x with (m_1,σ_1)=(1,1) and (m_2,σ_2)=(−1,2), and choose the local symmetric tensor T_{μν}(x)=δ_{μν}e_x. Use Jx=(−x₂,x₁,0,0), r=10, and a radial cutoff whose sampled values are 1 for |x|²≤100, (400−|x|²)/300 for 100<|x|²<400, and 0 for |x|²≥400. A smooth cutoff can match these finitely many values, with flattening between the sampled radii at the endpoints.

For A=e_(1,2,0,0) and B=e_(0,1,0,0), the torque is exactly the target's discrete shell functional. Writing C(d)=E[φ_0φ_d] and q(y)=Σ_μ(Jy)^μ[ψ(y+e_μ)−ψ(y)], direct rational sums give

    Σ_d C(d)q((1,2,0,0)+d) = 1/150,
    Σ_d C(d)q((0,1,0,0)+d) = 1/15.

Global sign symmetry makes both component-centered pair torques zero. The mixture-centered torque is

    (1/2)(1−4)(1/150+1/15) = −11/100.

The fields and tensor in this diagnostic are scalar lattice fields, not the Wilson clover/current. Its role is precise: it disproves the assertion that the two stated spatial symmetries plus mean-zero torque suffice for centered-pair additivity. The special Wilson claim would need an additional cancellation, not supplied here.

Coarse TQ itself is also not generally affine, even with fixed G, because conditional expectations and the posterior mixture weights change with the state. The fine affine formula may be transferred only with a separately controlled conditional-covariance error for the mixture.

A safer continuum statement is that rotation invariance of full correlators is preserved by mixtures with the required integrability; scalar translation-invariant one-point means contribute only rotation-invariant disconnected terms. With the conditional theorem also valid for the mixture, this can imply its limiting normalized torque vanishes. That is a different argument, with hypotheses for the mixture and for exchanging limits and infinite mixtures.

**NOT-VERIFIED under the same YM premises, logical independence from uniqueness.** Source: ROTDEF.md, Remark 8.5 and “It is logically independent of bare uniqueness”.

The text correctly labels the supporting discussion ARGUED and acknowledges that its rotator analogy is [m], unverified, and not a YM counterexample. A generic anisotropic Gaussian need not satisfy this Wilson action, SRC-W, and the other amended inputs. “Uniqueness gives no quantitative decay rate” is not a proof that uniqueness cannot imply rotation invariance by another argument. For example, if rotations preserve a limiting Gibbs specification, uniqueness can force rotational invariance by mapping the unique state to itself, without a clustering-rate estimate. Establishing that action/specification bridge is exactly additional information.

Likewise, closure of a property under mixtures alone does not exhibit multiple states of the same specified theory. No matching pair of YM witnesses establishing either logical non-implication is supplied. What is confirmed is that **the conditional reduction and the sufficient decay estimate do not assume uniqueness**. The stronger logical-independence claim remains unproved here.

## Finding 9 — Tensor facts do not establish the scale-separation estimate

**CONFIRMED, tensor facts.** Sources: ROTDEF.md, §8.4, “Fact”; checks/rd55_tens.py.

Individual sign flips force each axis index in an invariant tensor to occur an even number of times. Thus ranks 1 and 3 have no invariant tensor. Rank 2 is a multiple of δ, since axis permutations identify the diagonal entries. These statements also hold without assuming tensor symmetry.

For symmetric rank 4 there are two invariant polynomials:

    Σ_i x_i⁴,       Σ_{i<j}x_i²x_j².

Only their rotational combination (Σ_i x_i²)² spans the O(4)-invariant subspace. For example Σ_i x_i⁴ takes values 1 and 337/625 at the unit vectors (1,0,0,0) and (3/5,4/5,0,0). Independent signed-orbit enumeration gives invariant counts **1,0,1,0,2** at ranks 0–4.

**NOT-VERIFIED, physical scale-separation conclusion.** Source: ROTDEF.md, §8.4, “Call this input SRC-iso” and “The IR obstruction is confined to observation scales comparable to or beyond the reference scale”.

A tensor classification does not supply a uniformly controlled short-distance expansion of the conditional composite kernel, its singular leading term, or its remainder after averaging over large fields. SRC-iso explicitly assumes leading isotropy and a quartic remainder, which already contain the decisive analytic assertion. The small-field formulation and cell-average argument do not independently prove the uniform estimate for the full coarse law. Keep the tensor fact; keep the scale assertion conditional and unverified.

## Exact-check evidence and reproducibility

Author-script reproduction:

    rd55_rep:  stdout equals checks/rd55_rep_out.txt exactly
    rd55_tens: stdout equals checks/rd55_tens_out.txt exactly

Two in-memory mutations were also run without writing modified scripts:

- Replacing the plus in the author's Sym²A character formula by a minus produced dimension 15 instead of 21, failed C3 and C4, and made C6 report BROKEN; C5 was not evaluated.
- Replacing the signed-cycle coefficient eps**m by 1 in the tensor script made T0 report BROKEN and T1 report FAIL, with counts 1,1,2,3,5.

These controls establish that the displayed checks respond to these specific corruptions. They are not a claim of exhaustive software verification.

The independent representation certificate below constructs signed actions on basis elements and solves invariance by signed orbit propagation. It never uses χ_Sym²=(χ²+χ(g²))/2 or the author's cycle generating function.

~~~python
from itertools import combinations, combinations_with_replacement

A = list(combinations(range(4), 2))
S = list(combinations_with_replacement(range(6), 2))
W = list(combinations(range(6), 2))
generators = [((0, 1, 2, 3), (-1, 1, 1, 1))]
for i in range(3):
    p = list(range(4))
    p[i], p[i+1] = p[i+1], p[i]
    generators.append((tuple(p), (1, 1, 1, 1)))

def exterior_action(p, signs):
    result = []
    for i, j in A:
        u, v = p[i], p[j]
        sign = signs[i]*signs[j]*(1 if u < v else -1)
        result.append((A.index(tuple(sorted((u, v)))), sign))
    return result

def square_action(action, basis, antisymmetric=False):
    result = []
    for i, j in basis:
        u, si = action[i]
        v, sj = action[j]
        sign = si*sj*(-1 if antisymmetric and u > v else 1)
        result.append((basis.index(tuple(sorted((u, v)))), sign))
    return result

def tensor_action(a, b):
    return [(u*len(b)+v, si*sj)
            for u, si in a for v, sj in b]

def invariant_dimension(actions, size):
    edges = [[] for _ in range(size)]
    for action in actions:
        for i, (j, sign) in enumerate(action):
            edges[i].append((j, sign))
            edges[j].append((i, sign))
    assigned = {}
    dimension = 0
    for start in range(size):
        if start in assigned:
            continue
        assigned[start] = 1
        pending = [start]
        consistent = True
        while pending:
            i = pending.pop()
            for j, sign in edges[i]:
                value = sign*assigned[i]
                if j in assigned:
                    if assigned[j] != value:
                        consistent = False
                else:
                    assigned[j] = value
                    pending.append(j)
        dimension += int(consistent)
    return dimension

AA = [exterior_action(*g) for g in generators]
SS = [square_action(a, S) for a in AA]
WW = [square_action(a, W, True) for a in AA]
assert invariant_dimension(SS, 21) == 1
assert invariant_dimension(
    [tensor_action(a, s) for a, s in zip(AA, SS)], 126) == 0
assert invariant_dimension(
    [tensor_action(a, w) for a, w in zip(AA, WW)], 90) == 1
assert invariant_dimension([tensor_action(a, a) for a in AA], 36) == 1

counts = []
for rank in range(5):
    basis = list(combinations_with_replacement(range(4), rank))
    actions = []
    for p, signs in generators:
        action = []
        for indices in basis:
            sign = 1
            for i in indices:
                sign *= signs[i]
            target = tuple(sorted(p[i] for i in indices))
            action.append((basis.index(target), sign))
        actions.append(action)
    counts.append(invariant_dimension(actions, len(basis)))
assert counts == [1, 0, 1, 0, 2]
print("independent invariant counts:", counts)
~~~

Script/input hashes:

    18f107a8bf7e998b4a064bf7404ededeb6c67aa859fa66fa8fb1b7fec950e23a  checks/rd55_rep.py
    556d52c9be7b1fcb88894f3a6b5aefd64f60a5b2e83132e8af4454f90b2d680a  checks/rd55_rep_criteria.md
    0054f9f901ef4a4661ec7f960710357c7f1badca0577d59805d8599a583741d8  checks/rd55_rep_out.txt
    d7e894c885779cee8ccbcb73ba79aa0225572b230980a34a44cf341304504b73  checks/rd55_tens.py
    928a8268357a347c4cc168e5d3adeb6ac21423df02cdcdf30b7a6013528b7ca3  checks/rd55_tens_criteria.md
    5e6222c223f37ffe889c79cfb8bfd3ca1461647320407699b4786cb23107ab7e  checks/rd55_tens_out.txt

## Exactly what may be banked

Final same-session verification: all seven target/check hashes listed above remained unchanged, and the independent certificate was extracted from this review and executed successfully with bytecode writing disabled. No source correction is represented as having been applied.

1. **CONFIRMED:** the finite-torus Wilson Ward identity with W=ΞS−div Ξ, exact cutoff independence of Cov(F̃_s,W(v_r)), the centered source decomposition, and the exact discrete shell formula, within the embedded-cutoff domain.
2. **CONFIRMED:** the normalized-kernel identities and the exact total-covariance equation in Finding 5. No measure term or extra coarse mean product is missing.
3. **CONFIRMED:** for local pure-gauge field polynomials with full H(4) covariance, Hom_H(A,Sym² A)=0, the inversion-parity exclusions, the three dimension-5 vector divergences, the absence of a dimension-4 antisymmetric tensor, and the existence of allowed dimension-6 anisotropy. This does **not** bank its nonzero coefficient in this insertion or exclusion of all source contacts.
4. **CONFIRMED conditionally:** assuming the full CD, SRC-O, and SRC-W bounds, the stated vanishing-error reduction to the single **normalized** coarse torque. With the specified scale sequence and E6 convergence, vanishing of that torque is equivalent to rotation invariance on the tested pair's orbit.
5. **CONFIRMED conditionally:** the logarithmic-cutoff averaging argument with a valid lattice-sampling/envelope hypothesis, and in particular sufficiency of uniform |x|⁻⁸ or |x|⁻⁴/log|x| stress-channel decay. The literal unrestricted DEC statement, state-centered mixture additivity, and logical independence from uniqueness are not banked.
6. **CONFIRMED:** invariant tensor counts 1,0,1,0,2 at ranks 0–4 and absence of hypercubic anisotropy below rank 4. SRC-iso's analytic estimate is not banked.

**Nothing here banks CD/SRC for Wilson YM, nonvacuous source normalization, TQ→0, full OS1, OS0–OS3, or non-freeness.**

