# Independent hostile review of HINT2_55

## PRE-STATED

UTC: 2026-10-29T03:49:06.369696Z

Scope: HINT2_55.md; source ranges and named checks needed to assess the eight requested targets. No git commands. Only this file will be written. Exact symbolic reasoning and plain-Python integer/rational checks only. Source locations are found by strings; no cited line number is trusted without checking.

Prior exposure before this registration: the user's description; the target's heading/string-match index, PRE-STATED, errata E1–E9 and §R7; SCIENCE_WORKFLOW.md and the review-loop skill through line 220. An attempted earlier write failed because `python` is unavailable; this successful write uses `python3`. No mathematical derivation or check has yet been performed in this review. I do not independently certify the author's model identity. Review-loop is applied only within the user's narrower, single-deliverable scope.

Targets and pre-stated refutation criteria:

1. ID♮ and the no-one-point-witness assertion: exhibit a gauge-invariant observable without the stated jet, a failure of the identification to follow from theory equivalence, or a free scalar observable whose flowed profile contradicts a universal identification claim.
2. NOBS and the ξ expansion: reconstruct an exact finite-lattice example, track powers and regulators, and test the stated lattice and gauge-invariance quantifiers. A positive ξ² term alone will not certify the asserted ξ¹ logarithm.
3. PAIR and matrix spectral colour: derive the contraction, test PSD and linear-map closure, and distinguish spectral positivity from positivity of a subtracted Euclidean representative.
4. Arbitrarily many KL subtractions, mixtures, exact comparator profiles, T0 and OS: test divergent positive spectral moments, polynomial/contact cancellation, mixture integrability, and existence and survival of a time-zero observable in the reconstructed theory.
5. INT, CONV, zero-charge limits and semicontinuity: check powers of a, t and L, uniformity in volume/cutoff, and the topology and direction of each limiting inequality.
6. The full H_int chain and the slope bracket: verify required hypotheses, parameter quantifiers and source attachments without treating status labels as evidence.
7. TS-up and large fields: derive scale amplification and instanton power counting; distinguish failure of an estimate from an impossibility theorem.
8. Named checks: inspect whether gates could fail, whether controls test the stated property, whether a2 preserves the claim, and what the aborted d run and omitted checks establish.

Finding verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED is restricted to a rebuilt claim. Refuted numbers will receive an exact correction and derivation. The final table will state what can be banked and the most dangerous unverified bridge.

## Findings (appended as checked)

### F1 — ID♮ is a contraction convention, not a reconstructed-observable identification

**CONFIRMED (CONDITIONAL convention); NOT-VERIFIED (physical identification); REFUTED (the literal domain of the definition).** Attachments: `HINT2_55.md:146`, locating `For a gauge-invariant lattice observable O ≥ 0 with O(1) = 0`; `:149`, `A free theory's value`; `:305`, `What no one-point witness can do`; erratum E3 at `:491`.

For a twice differentiable O with a minimum at 1, DO(1)=0 and Taylor expansion gives O(exp(cA))/c² → D²O(1)[A,A]/2. Gauge transformations expanded to first order prove invariance under A→A+dλ. E3 correctly retains harmonic modes on a torus. Scaling the connection in the flow gives B_1[cA]=cB_c[A] and G_1[cB]=cG_c[B], so the energy contraction is the abelian heat composite for the fixed flow normalization.

The stated domain does not assume twice differentiability. Set q(U)=Re tr(1−U_p) and O(U)=sqrt(q(U)). This is gauge invariant, nonnegative and zero at identity, but for dA_p≠0 it behaves as |c|sqrt(−tr((dA_p)²)/2); c⁻²O diverges. Add a C²-at-identity hypothesis (met by the flowed plaquette density). This defect does not invalidate that density’s jet.

More substantively, even on smooth observables this map is not an algebra identification: q(exp(cA))=c²q₂(A)+O(c³), hence (q²)^♮=0 while (q^♮)²=q₂(A)²≠0. An observable-algebra isomorphism must preserve products. On bounded q the contraction can also be unbounded, so it cannot be a unital C*-algebra identification preserving norm/spectrum. ID♮ is a legitimate, preselected associated-graded/tree-level calibration for the specified quadratic sector. No theorem here makes an arbitrary equivalence to a free reconstructed theory respect that calibration. The relative separation theorem is meaningful; absolute reconstructed-theory non-freeness is still GAP.

The scalar obstruction is rebuilt: in four dimensions d⁴p/(2π)⁴=u du/(16π²), u=p². For covariance (p²+M²)⁻¹,

    t² M² E[(K_t*φ)²] = M²t/(16π²) ∫₀∞ v exp(−2v)/(v+M²t) dv.

It is positive and at most M²t/(32π²), hence tends to zero at t↓0 despite being positive at any fixed t. Mapping the family to φ(t)·1 also realizes any prescribed nonnegative profile if no algebraic/covariant identification restrictions are imposed. These examples confirm the need to specify the comparison rule; they do not prove that every legitimate one-point witness must use ID♮, or exclude other structured identification rules.

### F2 — PAIR and the matrix colour repair survive; their coverage remains explicit

**CONFIRMED (PROVEN within the stated spectral class).** Attachments: `HINT2_55.md:198`, `Lemma PAIR`; `:212`, `Definition (𝔊^col)`; `:218`, `Lemma COL`; `:221`, `(N1), corrected`.

Pairing the two smeared linear fields directly gives the displayed expectation, without Wick factorization or a KL representation of the composite. At nonzero momentum the tensor T^I has Gram form (p_μδ_{νλ}−p_νδ_{μλ})(p_ρδ_{σλ}−p_σδ_{ρλ}), summed over λ, and ordered-index trace 6p². Multiplying t²/4 by the four-dimensional radial measure gives exactly (3/(32π²))∫v exp(−2v)h(v/t)dv.

For any v, vᵀΛρΛᵀv=(Λᵀv)ᵀρ(Λᵀv)≥0; Tr(Mρ)=Tr(M^(1/2)ρM^(1/2))≥0. Integrability is retained under fixed finite-dimensional linear maps. These arguments prove closure for all such maps, not just the 60 checked triples. The old two-colour example has the negative mass-1 spectral weight diag(−1,1), so it is excluded. After its unequal rescaling h=1/4+3/(4(1+u)), h′=−3/(4(1+u)²), and the UV coefficient remains 3/(512π²). No new correction to that number is needed.

### F3 — The arbitrary-subtraction repair closes the twice-subtracted gap

**CONFIRMED (PROVEN for 𝔊^col_∞ and its nonnegative mixtures).** Attachments: `HINT2_55.md:230`, `Theorem UV-D_∞`; `:245`, `Theorem SEP^col`.

The finite geometric-series identity gives S_K(u)=(1−u)^K∫dρ/((u+s)(1+s)^K). At minimal K≥1, |S_K|/u^(K−1)→∞ by integration over s≤u, while |S_K|/u^K→0 by dominated convergence. Its sign is (−1)^K. If K is odd, positivity forces a positive polynomial of degree at least K; if K is even, either such a polynomial dominates or S_K itself dominates every polynomial of degree at most K−1. In every allowed case S_K+P≥cu eventually. Consequently f(t)≥(3c/(32π²))[3/(8t²)−t²U₀⁴/4]→∞. For K=0 the Stieltjes part decreases to zero as u→∞, so positivity permits a constant contact only if nonnegative, or forces a positive leading coefficient for a higher-degree contact. The latter also diverges. The constant-contact/unsubtracted case has h′(u)=∫s dρ/(u+s)²+p₀≥0, which makes f non-increasing in t.

The twice-subtracted example is S₂=u log((u+1)/2)−(u−1)/2: it grows faster than u and slower than u², exactly as the repaired proof needs. For a mixture with finite UV liminf, Fatou forces zero mixture mass on every component with infinite UV limit, then bounds ∫f_α(t₀)dν by ∫f_α(0+)dν≤liminf f̄(t). This is a real proof, not a finite-K numerical extrapolation. Extension from this class to all reconstructed theories still needs a correctly stated tensor KL/import and an observable identification; F1 is unaffected.

### F4 — The large-field source and coupling normalization are stale

**REFUTED (source attribution and exponent in the pinned coupling); NOT-VERIFIED (the claimed necessity of LF-inst).** Attachments: `HINT2_55.md:402`, `The large-field factor of Balaban-type estimates`; `:406`, `For the true dilute-instanton weight`; `:549`, `sharper than any Balaban-type factor in the lane`; E7 at `:561`. Source pins: `FLOW.md:24`, `Coupling variable`; `:36`, `Standard coefficient`; `PROOF.md:1494`, `L5. Large-field R-operation`, especially `:1509`, `This is not the p(g)² form of the old paraphrase`.

PROOF L5 does record Dimock’s exp(−c₂p_j²) template, but explicitly distinguishes it from the fixed dimensionless ε₁ cut of CMP 109. The latter has action cost of order ε₁²/g_k². L5 also marks the large-field operation IMPORTED-NOT-YET-REVERIFIED and does not establish a probability bound for flow-surviving concentrations. Thus HINT2’s attribution of a common exp(−cp(g)²) factor to the lane, and its assertion that every lane factor has only that strength, are false readings of the cited source. This does not prove TS-up: the relevant action constant, event, and observable transport still need estimates.

There is an explicit symbol collision. FLOW fixes u_k=1/g_k²=2N/g_std,k² and β₀^std=11N²/(12π²). In these pinned variables the instanton weight is

    exp(−8π²/g_std²) = exp(−(4π²/N)u),

not exp(−8π²/g_k²). The corrected coefficient of u is 4π²/N, smaller by 2N than the literal HINT2 coefficient 8π². Therefore c_inst β₀^std=(4π²/N)(11N²/(12π²))=11N/3. Using the written coefficient with FLOW’s β gives 22N²/3 instead. The quoted physical convergence exponent 11N/3 is correct only after this conversion; it is not the product of the two displayed conventions.

The sufficient geometric estimate, given the event bound and the actual flow bound u_j≥u_k+β₋(k−j)log L−R_F, is

    Σ_{j≤k} L^{4(k−j)} P_j ≤ C exp(c_LF R_F) exp(−c_LF u_k)
                                     × Σ_{r≥0} L^{(4−c_LF β₋)r}.

The constant exp(c_LF R_F) may be absorbed into a new C, but cannot be silently lost. The convergence condition c_LFβ₋>4 is correct. If β₋ is merely positive as allowed by B-BR, that condition does not follow from 11N/3>4; one must additionally have β₋>N/π² for the corrected instanton coefficient. This is consistent with treating TS-up as its own OPEN input, but cannot establish its proposed route from an arbitrary positive slope.

Given the proposed amplification L^{4(k−j)}, inserting only a logarithmic-cutoff upper bound does produce an unbounded upper estimate (and thus fails to prove TS-up). An upper estimate tending to infinity does not prove that the actual probability sum diverges, nor that an exponential bound of this specific form is necessary. Flow survival, the Wilson-lattice shrinking rate, event counting, and a probability estimate for surviving concentrations remain ARGUED/OPEN. The note acknowledges part of this at :412, but its recommendations and repeated “needs LF-inst” wording overstate it. What can be retained is the need to control the transported bare observable, with a demonstrated failure of this particular weak union-bound route.

### F5 — NOBS and the ξ² coefficient: a genuine obstruction with a restricted conclusion

**CONFIRMED (PROVEN for nondegenerate plaquette geometry; formal continuum coefficient); REFUTED (literal “any finite periodic lattice”); NOT-VERIFIED (the blanket exclusion of every free-theory construction).** Attachments: `HINT2_55.md:156`, `Lemma NOBS`; `:166`, `Proposition GC-ξ`; `:190`, `Decision on T1(e)`; E2 and E4.

For a plaquette with four independently assignable corner values 0,X,X+Y,Y, the abelian circulation is zero. Choose exp(cX)=iσ₁ and exp(cY)=iσ₂. Their group commutator is −I, so 2−tr P=4 exactly. An open neighborhood has positive measure under the stated nondegenerate Gaussian law (subtracting the common mean preserves the differences). A finite-dimensional smooth gradient-flow trajectory cannot reach a flat equilibrium at finite time unless it started there, by backward uniqueness. Thus the expected total action is strictly positive at every finite τ. E4 correctly requires translation-invariant covariance to infer equality/positivity at every site.

The literal “any finite periodic lattice” needs a geometry restriction: on a torus with lengths (3,1,1,1), nonconstant, nondegenerate mean-zero λ exists, but A is supported in the sole nontrivial direction and every plaquette holonomy is identity. The same applies vacuously on the one-site torus. The intended four-dimensional boxes with an ordinary four-corner plaquette avoid this edge case. This is a quantifier defect, not a failure of the intended example.

For the formal continuum pure-longitudinal contribution, Ω=exp(cλ) removes dλ at order c⁰ and leaves c[λ,dλ]/2. Taking its exterior derivative gives c[∂_μλ,∂_νλ]. Therefore the ξ² energy coefficient is exactly the mean square in the note. A separate continuum evaluation also fixes its positive constant. Write n=N²−1, r=p−q and ∫_q=d⁴q/(2π)⁴. Antisymmetry replaces q_μr_ν by (q_μp_ν−p_μq_ν)/2; the two Wick contractions and the ordered μν sum give

    Σ_{a,μν} E|[∂_μλ,∂_νλ](p)^a|²
       = Nn (ξe²)² I(p),
    I(p) = ∫_q [q²p²−(q·p)²]/[q⁴(p−q)⁴] = 3/(32π²),   p≠0.

For the last equality use 1/(a²b²)=6∫₀¹x(1−x)[xa+(1−x)b]⁻⁴dx, shift q to l+(1−x)p, and rotational averaging: numerator→(3/4)p²l². The remaining radial integral is

    ∫_l l²/(l²+Δ)⁴ = (1/(16π²Δ))∫₀∞z²/(1+z)⁴ dz = 1/(48π²Δ),
    Δ=x(1−x)p².

Thus I=6(3/4)/(48π²)=3/(32π²), and ∫_p exp(−2tp²)=1/(64π²t²) yields

    κ₂ = 3N(N²−1)/(8192π⁴) > 0.

This is an independently derived additional value, not a correction to a claimed number. The integral is UV/IR finite; the apparent p=0 exception is measure zero. Regulator removal is justified for bounded nonnegative cutoffs tending to 1 by the integrable majorant. The group contraction for general N follows from completeness of an orthonormal traceless matrix basis, which gives Σ_b[T^b,[T^b,X]]=−NX; it is not inferred just from the script’s SU(2)/SU(3) samples. The computation is at formal order c⁴ in t²E₁[cA], with powers as corrected by E2, not a nonperturbative construction.

NOBS proves that the **unprojected** nonabelian-flow functional on A does not descend to the abelian gauge quotient. It does not prohibit composing the nonabelian flow with a chosen reconstruction of A from F. On a finite lattice with harmonic modes removed, A_T=d*Δ⁻¹F is determined by F, so F↦E_nonab(flow(exp(cA_T(F)))) is a perfectly definite, generally nonlocal function of the free gauge-invariant data. That is a different, explicitly specified functional. ID♮ excludes it by convention; NOBS alone cannot exclude it as a possible free-theory observable identification. Keep the decision at the quotient-descent level.

### F6 — The ξ-linear logarithm is correct under a specified regulator, but the script does not certify it

**CONFIRMED (CONDITIONAL formal asymptotic for a smooth heat regulator); NOT-VERIFIED (unspecified regulator/unrenormalized continuum realization).** Attachments: `HINT2_55.md:181`, `The ξ¹ part`; `:187`, `log(t/s₀)`; E2; `checks/h2_55_b.py`, `B4.2 IR`.

Independently expanding Ω(A_T+dλ)Ω⁻¹−c⁻¹(dΩ)Ω⁻¹ gives Y₁=[λ,A_T]+[λ,dλ]/2 and Y₂=[λ,[λ,A_T]]/2+[λ,[λ,dλ]]/3. The ξ-linear term is N∫_q G_λ(q)[K(q)−K(0)]. The mixed cubic-flow contribution vanishes: the terms linear in λ are odd, and E[λ,dλ]=0 by antisymmetry in colour. Completeness gives the relative colour factors +N and −N, so the subtraction cancels the IR constant. Include t² at the end; K(0)=f₀/t².

For r_s(q)=exp(−s₀q²), write the K convolution with transverse covariance e²r_s(k)Π_T(k)/k². It is even and smooth in q: after changing variable to k=p−q, derivatives act on a Schwartz Gaussian times a polynomial, while 1/k² is locally integrable in four dimensions. Thus K(q)−K(0)=O(q²) at the origin. For |q|√t≫1, split |p|≤|q|/2 (where |p−q|⁻²≤4/|q|²) from its complement (a Gaussian tail with an integrable |p−q|⁻² singularity). This gives K(q)≤C e²n/(t³q²) plus an exponentially small tail, uniformly for s₀/t sufficiently small. Its contribution against dq/q is finite at the UV end. The constant subtraction gives

    −Nξe²K(0)/(8π²) ∫_{t^(−1/2)}^{s₀^(−1/2)} dq/q
      = −Nξe²K(0)/(16π²) log(t/s₀).

Multiplying by t² gives exactly E2’s −Nξe²f₀ log(t/s₀)/(16π²), with a bounded remainder for this regulator. This independently resolves the large-q issue for that explicit regulator. The generic phrase “a UV regulator at scale s₀” needs a uniform cutoff class to assert the same remainder. No α₀ enters because only the abelian curvature heat semigroup occurs in these ξ-dependent terms; that is an analytic reason for α₀ independence, not an α₀ test performed by B4. The transverse ξ⁰ coefficient remains uncomputed, and no positive-c unregulated Gaussian-connection realization follows from this formal calculation.

### F7 — Exact free profiles and T0; a second coupling-convention error

**CONFIRMED (PROVEN comparator formulas); REFUTED (magnetic tree coefficient if g retains the file’s FLOW convention); NOT-VERIFIED (continuum Yang–Mills sharp-time survival).** Attachments: `HINT2_55.md:254`, `Exact free values`; `:280`, `Proposition T0`; `:302`, `Tree level`; E8.

For each unsubtracted spectral mass s, the radial contraction gives J(ts), where polynomial division v²/(v+σ)=v−σ+σ²/(v+σ) yields J(σ)=1/4−σ/2+σ²exp(2σ)E₁(2σ). Its derivative is −∫v²exp(−2v)/(v+σ)²dv<0; J(0)=1/4. Thus the displayed Maxwell coefficient 3Tr(MC)/(128π²), the Proca/GFF integral, and their monotonicity are correct in the stated covariance normalization. A contact monomial P_k u^k contributes (3/(32π²))P_k(k+2)!/[2^(k+3)t^(k+1)], by repeated integration by parts. For the CT example at ε=1, direct rational evaluation gives F(1/2)=5/4, F(1)=3/8, F(4)=27/128 and F(8)=115/512, hence the stated differences −7/8 and 7/512 are correct. Mixture expectations are integrals by nonnegativity; no cancellation of divergent positive components is possible.

For T0, the spatial ordered-index trace is 4|p⃗|² and the energy integral of a massive mode is 1/(2sqrt(|p⃗|²+s)). Thus

    f_B(t)=1/(4π²) ∫ρ_M(ds) ∫₀∞ v⁴exp(−2v²)/sqrt(v²+ts) dv.

At s=0, ∫v³exp(−2v²)dv=1/8, giving ρ_M(total)/(32π²). The integrand decreases with s t, and for large s its integral is comparable to s^(−1/2). The precise existence condition is integrability of min(1,s^(−1/2)) against the **observed** spectral measure ρ_M (using Trρ is a sufficient condition for all colours). A divergent unsubtracted spectral integral at infinity forces failure of this sharp-time condition. For M with a kernel, a divergent unobserved colour does not make f_B infinite; apply E8 to ρ_M. Contact-polynomial representatives have no finite Euclidean sharp-time limit in a nonzero observed contact direction. The canonical reconstructed Gaussian value nevertheless has the formula above when its spectral condition holds.

FLOW.md:24–25 pins g_std²=2N g_FLOW². Accordingly the line :302 must either explicitly rename g as g_std, or read

    f_B(tree) = N(N²−1) g_FLOW²/(16π²)
              = (N²−1) g_std²/(32π²).

The written (N²−1)g_FLOW²/(32π²) is smaller by 2N. For SU(2) the coefficient of g_FLOW²/π² is 3/8, not 3/32; for SU(3), 3/2, not 1/4. This normalization is independent of the valid covariance-normalized T0 formula.

At a fixed finite lattice cutoff the spatial flowed observable depends only on one time slice and is bounded, so the site-reflection boundary algebra has the stated vacuum pairing. This does not prove a continuum sharp-time YM observable, its Hilbert-space domain, or the corresponding moment/control bounds. A first-moment bound alone does not give a vector [𝓑] on a time-zero algebra (its norm involves a second moment). T0 honestly leaves continuum YM finiteness OPEN; it does not repair the 4D observable’s OS identification or prove absolute non-freeness. Smooth positive-time smearings can also define reconstructed observables, so the unqualified word “only” in :312/:555 is too broad; the sharp-time construction is one sufficient route for the particular magnetic square with its stated domain.

### F8 — REP needs the missing translation-invariance hypothesis

**REFUTED as literally stated; CONFIRMED (CONDITIONAL repaired polynomial-contact argument).** Attachment: `HINT2_55.md:266`, `If μ ∈ 𝔊^col_∞ and μ′ is any O(4)-invariant, Bianchi`; `:269`, `The difference D ... is translation invariant`.

The hypotheses on μ′ do not state translation invariance. It does not follow from O(4) invariance and equality of separated-point two-point functions. Let F be a stationary Maxwell field and add independent contact noise dA, where A is a Gaussian vector generalized field with covariance

    E[A_μ(x)A_ν(y)] = δ_{μν}(1+|x|²) δ(x−y).

This law is positive, tempered, O(4)-covariant and has finite variances on Schwartz tests; dA is Bianchi. Its covariance and all its derivatives are supported on x=y, so the new field agrees with F on disjoint-support pairings. It is not translation invariant: translating a test changes the weight 1+|x|² in the variance ∫(1+|x|²)|d*φ(x)|²dx. Therefore it cannot have the stationary multiplier T^I(p)S_s(p²) required by 𝔊^col_∞. This refutes the written quantifier while preserving the intended statement for Euclidean-invariant representatives.

With translation invariance added, D is a distribution at the origin in the difference variable and hence a finite delta-derivative sum. Its Fourier polynomial is O(4)-equivariant. Pair antisymmetry leaves only α(u)I+β(u)T^I; contraction with εp kills T^I and detects I, so Bianchi forces α=0. Polynomiality of the 12,13 component β(p²)p₂p₃ then forces polynomial β. Hence the changed representative only changes P and F3 applies. This covers representatives with the same identified separated-point linear-field covariance, not every abstractly equivalent free observable algebra (F1).

### F9 — INT, CONV and semicontinuity work at the stated probability-law level

**CONFIRMED (PROVEN conditional inequalities and countable subsequential compactness); NOT-VERIFIED (identification with a continuum flowed/OS observable).** Attachments: `HINT2_55.md:341`, `Lemma INT`; `:347`, `Lemma CONV`; `:352`, `Theorem H-RED♮`; E9; `:547`, `(CONV-E) and the continuous-time limit are no longer open`.

With tr(T^aT^b)=−δ^{ab}/2, the plaquette expansion gives E_pl=a⁴Σ_{μν,a}(G^a_{μν})²/4+O(a⁶). The flow action is exactly the spatial sum of this lattice density. Differentiating the action along its negative gradient gives −Σ(∂S)². Translation invariance then makes e(τ)=E[S]/|Λ| non-increasing. E9 supplies the correct factor:

    f(t)=τ²e(τ) ≤ τ_m²e(τ_{m+1}) = L⁴ f(t_{m+1}),  τ=t/a².

The factor L⁴ is correct and cannot be replaced by the dimensionless factor 1 solely from energy monotonicity. The proof does not apply verbatim to clover energy. It also needs translation invariance of the law, explicitly assumed in INT and appropriate to the periodic Wilson law.

From F-tune, u_{K−m}≥U₋(m)>0. Since 1−ϑ>0, TS-up gives f_K(t_m)≤C₊U₋(m)^(ϑ−1), while TS-low gives f_K(t₀)≥c₋/U₊(m₀). Thus the least-index condition with 2C₊U₊/c₋ yields W_m≥c₋/(2U₊). INT gives the continuous-time analogue with 2L⁴C₊U₊/c₋ and U₋(m+1). At the lowest admissible grid endpoint use the grid estimate itself rather than an unavailable level below d₀. The statements are uniformly asymptotic in cutoff: at a fixed t the depth condition eventually holds; finitely many smaller cutoffs have bounded plaquette density and cause no tightness obstruction.

For a countable list of coordinates, choose coordinate cutoffs R_i so that P(X_i>R_i)≤ε2^(−i), using each uniform first-moment bound. The product of the compact intervals [0,R_i] is compact in the countable product topology, with probability ≥1−ε. This proves joint tightness and a weakly convergent subsequence, also jointly with any already tight countable H_reg coordinate family. Under weak convergence, E X_t≤liminf E X_{j,t}; at t₀, MOM-E gives uniform integrability and equality of the limiting means. Therefore

    W_m(limit) ≥ limsup W_m(sequence),

which is upper semicontinuity on this uniformly controlled family, not general continuity on all probability measures. This is the right direction. Bounds tend to zero for every t↓0 in the specified countable D, and the grid alone already suffices to contradict a comparator with the SEP property.

What CONV does **not** establish: that the extra limit coordinates are deterministic functionals of the limiting gauge field, that the extension is unique, that a continuum Wilson flow solves the required equation, or that its 4D observables have an OS reconstruction. The generic counterexample is X_j=Z/j with Z∈{−1,1} equiprobable and Y_j=1[X_j>0]. Every Y_j is a deterministic function of X_j, all moments are bounded, and the joint law converges to (0,Bernoulli(1/2)); Y is not a function of the limiting X. This shows exactly why tightness alone cannot provide the missing functional identification. It does not refute the compactness lemma itself. The stronger recommendation that the continuum-time observable problem is now wholly closed is NOT-VERIFIED; the proved result is the joint-law statement on D plus the finite-cutoff bounds.

**Symbol collision confirmed:** :324 defines R as the physical torus side; :352 uses R as FLOW’s additive flow error; :385 says constants depend on R but not on the torus. Restore the PRE-STATED pin R_F for the flow error and use R_box for volume. Literal substitution of R_box into U₊ makes c_W=c₋/[2(g⁻²+β₊m₀log L+R_box)] tend to zero with volume and loses the advertised uniform margin. With R_F, the derivation above is uniform.

### F10 — The positive-slope reduction is sound arithmetic, with upstream and layer-1 conditions retained

**CONFIRMED (CONDITIONAL reduction); NOT-VERIFIED (unconditional H_int and full upstream proof closure).** Attachments: `HINT2_55.md:370`, `Connection to the coupling flow`; rows L3–L10; `FLOW.md:420`, `Theorem F-flow`; `:433`, `Theorem F-tune`; `:459`, `Lemma F-ind`; `FLOW55.md:446`, `Corollary K̄-β`.

Independently, u_j−u_n=B_n−B_j+Σ_{k=j}^{n−1}ρ_k and |ρ_k|≤C_ργ². A two-sided bracket on B_n−B_j therefore gives β₋=β′−C_ργ²/log L and β₊=β″+C_ργ²/log L with the same R_F=R′. Choosing C_ργ²≤β′log L/2 gives β₋≥β′/2>0. No exact one-loop slope is used. The tuning proof also survives: sufficiently small g₀ keeps all u_k≥γ⁻²; continuity gives a first exit where some g_k=γ; the lower flow bound then puts u_K≤γ⁻²+R_F; the intermediate value theorem reaches any target u_K=g⁻²≥γ⁻²+R_F. Constants can be fixed in the stated order, provided the per-level analytic and large-field estimates really hold along the actual chain from flow information on [0,k].

Given the coefficient identity B_n=−β[G^♮_⊥,n]+(β₀^std/22)n log L, subtraction at j,n proves exactly the displayed UIR^♮_br equivalence. Uniform error around the exact slope implies the bracket with R′ twice that error. Hence the restricted witness does not need 21/22 exactly. Merely knowing a positive asymptotic slope B_n/n does **not** replace the uniform interval bracket: long negative/large fluctuation stretches could violate it. The file’s bracket correctly quantifies every j≤n.

The list has to retain the **conditional** coefficient identity and the actual-chain versions of (SF-g)_k and (RLF-δ)_k. FLOW.md:223–228/:466–470 explicitly say that deriving those per-level estimates from (F_R) on [0,k] is a requirement, not a discharged result. FLOW55’s coefficient identity itself is conditional on its regrouping, tadpole/drift removals, locality and ghost calculation. I rebuilt the summation, tuning and substitution, not the entire analytic upstream determinant theory; no author/reviewer label substitutes for those premises here. A weaker slope also changes the admissible flow-constant domain in which any layer-1 bound must be proved. No fixed minima or old rate-domain constants may be silently reused.

The resulting conditional implication for the prescribed joint-law/ID♮ witness is valid with these premises and TS-up/TS-low/MOM-E. It does not establish those YM estimates, H_reg/OS0–OS3, a uniquely identified continuum flow, or non-freeness under an arbitrary free-theory observable equivalence. F1 and F9 remain necessary limits on the advertised conclusion.

### F11 — Check audit: a2 is a valid repair, but the evidence boundaries matter

**CONFIRMED (the recorded results and the mathematical a2 repair); NOT-VERIFIED (historical pre-registration/resource claims beyond the available records).** Attachments: `HINT2_55.md:472`, `Checks`; `:569`, `Addendum`; every named `checks/h2_55_*_criteria.md`, corresponding `.py`, and `_out.txt`; `h2_55_d_run1_abort_out.txt` / `_err.txt`.

I read the criteria, implementations and named output records, and independently rebuilt the decisive mathematics. I did **not** rerun the author’s SymPy programs or claim a new run of their PASS totals. My separate plain-Python checks used only integers/Fraction and wrote no files: exact tensor contractions at p=(1,2,3,4), an integer quaternion commutator, 108 rational remainder-identity instances (K=1,…,9), the radial coefficients, contact differences and coupling conversions. They supplement the general derivations above, not replace them.

| Check/gates | Recorded result and independent assessment | Can the check decide its advertised claim? |
|---|---|---|
| a: A1 | 27/27 total a gates, 6/7 controls; A1 algebra and negative mass-1 colour weight rebuilt | Yes for the specified rational example, not universal colour coverage |
| a: A2 | PSD generated as BBᵀ; finite rational congruence/trace checks; negative diagonal control | Checks implementation on 60 constructed cases; universal closure comes from vᵀΛρΛᵀv≥0, not these samples |
| a: A3, original A3-F | **Registered FAIL retained.** Bi[T′]=0 identically even with the second-term sign flip | The proposed Bianchi control could never fire: each term has a symmetric pair of momentum factors under ε. This was an impossible control, not evidence against the true Bianchi identity |
| a2: G1/G2, C1/C2/C3 | Recorded PASS. Independent integer checks give Bi[T]=Bi[T′]=0, Bi[I]≠0, Gram(T)=true, Gram(T′)=false | Genuine repair: the original Gram/Bianchi gates are unchanged, the bad sign is tested against Gram, and added I is tested against Bianchi. It does not erase a’s FAIL or become a prospective test merely because a2 has a criteria file |
| a: A4 | Remainder identity, S₂ partial fractions, asymptotic limits | Detects wrong exponent; K≤6 checks alone do not prove arbitrary K. F3 supplies that proof |
| a: A5 | Factorials and two CT differences agree | Detects dropped normalization; no continuum-limit or physical-comparator identification tested |
| a: A6 | Equal-time integral, spatial trace, radial Jacobian, massless value, two contact integrals, derivative | Genuine normalization checks. A6.5 tests only two polynomials; general contacts need the leading-term argument. No continuum YM time-zero domain is tested |
| a: A7 | Scalar radial measure and scaling | Correct scalar obstruction algebra; does not choose an allowable theory isomorphism |
| b: B1/B2 | Recorded 15/15 gates and 6/6 controls overall. Scaling jets and noncommutative BCH series are meaningful symbolic comparisons | The original ∂G-only B1 control would also scale correctly; the corrected missing-c commutator control can fail. No ODE/continuum existence theorem is checked |
| b: B3/B4 | Casimirs only for N=2,3; IR cancellation ratios +N and −N | Establishes those algebraic cases, not the general-N theorem or the momentum integral. B4 is not an α₀-independence or logarithmic-coefficient test |
| b: B5/B6 | Exact noncommuting plaquette and antisymmetric vertex | Good local algebra; does not test the universal lattice quantifier, ODE nonattainment of equilibrium or regulator removal |
| c: C1–C4 | Recorded 4 gates and 2 controls, PASS | Characteristic function and Fourier coefficients are independent integrals; C3’s ratio proves decreasing terms; C4’s three signs are redundant spot checks. The general series argument is given below |
| d: D1 | Recorded 43,200 rational inequalities | Meaningful arithmetic sanity test with an increasing-e control; it sets a=1 and cannot catch the missing a⁻⁴ in pre-E9 prose or prove lattice energy dissipation |
| d: D2 | Recorded 200 parameter sets; predecessor fails in 200/200 cases | The threshold is defined by the same predicate checked afterwards. The predecessor control is a search-implementation sanity check by construction, exactly as its criteria admit; it is not independent evidence for the general H-RED implication |
| d: D3 | Recorded bracket checks and zero-slope control | Verifies simple constructed inequalities, not any real one-loop coefficient or layer-1 bound |
| d: D4 | Recorded k_α=4πk_g and symbolic coefficient conversion | Correct conditional algebra. k_g is inserted into the test, so no perturbative integral/source coefficient is independently verified |

The first d run has empty preserved output and error files. The target reports it was killed after roughly ten minutes in a linear search; no first-run success or exact elapsed duration can be certified. The final code’s exact binary search is a legitimate algorithmic repair: the predicate is monotone, the integer bracket doubles until true, then shrinks to the least satisfying integer. It changes no registered gate. The current source/logs support this diagnosis, but do not independently establish that the historical change was **only** that search. The heading “all <20s, <100MB” cannot serve as a measured bound on the aborted run. Header timestamps corrected by the author and same-command criteria/script creation are disclosures, not independently authenticated pre-registration histories.

The omitted rational Proca/GFF sampling is harmless because pointwise integrand monotonicity proves the claim. The omitted α₀/logarithm test is substantive for the original check plan, correctly disclosed in §R7; the author’s b PASS must not promote that claim. F6 independently handles a specified regulator only.

For WN, E cos X=exp(−v/2), and integrating y² cos(ny) twice by parts gives 4π(−1)^n/n². Thus E[2dist(X,2πZ)²]=2π²/3+8Σ_{n≥1}(−1)^n exp(−n²v/2)/n². For v>0 the differentiated series converges absolutely locally uniformly. Pairing consecutive alternating terms gives derivative at least 4[exp(−v/2)−exp(−2v)]>0. The limit as v→∞ is 2π²/3; the cosine observable has limit 2 and derivative exp(−v/2)>0. Hence the Gaussian bounded-observable conclusion follows from variance monotonicity or divergence; for mixtures, each component’s UV limit dominates its finite-scale value and Fatou applies. This is CONFIRMED for the specified one-colour literal observables. It is not a theorem about arbitrary bounded functions or non-Gaussian contacts; ID♮ changes the comparator observable rather than proving such a theorem.

### F12 — Noise inputs and the hard branch remain genuine conditions

**CONFIRMED (logical separation and failure of the old lower-bound inference); NOT-VERIFIED (nonlinear estimates and actual S4c transfer).** Attachments: `HINT2_55.md:423`, `(NOISE-ADD)`; `:430`, `(ANTI-♭)`; `:438`, `The deterministic S4c branch`; E6.

A normalized tower of transition kernels does not change the U₀ marginal: integrate the last auxiliary variable first and repeat. Thus the bare flowed expectation is independent of those auxiliary kernels. An upper estimate on the deterministic observable cannot imply a positive lower estimate after noise subtraction: EΨ_soft=2g², EΨ_det=0 with an exact Gaussian comparison already defeats that inference. A lower comparison such as NOISE-SUB, with an actual noise budget and error smaller than the signal, is a genuinely new requirement. No nonlinear NOISE-ADD/ANTI-♭ bound is proved in this target.

For a hard deterministic RG, the block observable’s law is directly a block marginal, so no independent auxiliary-noise lower-bound transfer is needed. However, the actual hard-scheme flow estimates cannot be imported from the soft chain. Smoothness at identity, convergence of the **plaquette flux** linearization (the curl of the link-map derivative), and nonzero annular smearing weight all remain part of S4c-lin. E6 correctly retracts the original claim that mere continuity of the map supplied differentiability. Even if these hold, they supply the quadratic comparator only relative to ID♮; F1’s algebra-identification gap remains. Locality also requires placement of the whole support in positive time before using the OS algebra; locality alone does not put an arbitrary centered observable in 𝔄₊.

### F13 — Remaining errata/source pins and finite-depth qualifications

**REFUTED (the level-index formula in E5 and a currently stale indirect line citation); CONFIRMED (E2/E3/E4/E9 corrections within their scope).** Attachments: `HINT2_55.md:497`, E5 `since 1/g_j² ≍ j log L`; `FLOW.md:42`, `the β'_B line is PROOF l.4162`; current `PROOF.md:4162`, `What E8** is`; `PROOF.md:4422`, `1/g_B² = 2N/g_std²`.

With the explicitly pinned level j=number of RG steps from the bare lattice, the tuned relation is u_j=g⁻²+Θ((K−j)log L) up to the fixed additive flow error, **not** u_j≍j log L. At j=K the coupling is the fixed renormalized g while j grows with cutoff. A logarithmic-cutoff factor therefore scales as exp[−O((log(K−j))^(2p))] in the deep-UV regime K−j→∞. Taking k=K−m with fixed m and j≈k/2 still makes this too weak against L^{4(k−j)}, so the failed weak-bound route survives the index correction. The incorrect index must not be reused at j≈k with fixed K−k.

FLOW’s already-“repaired” citation to PROOF line 4162 is now stale: that line begins the unrelated `What E8** is` discussion. The LF-count proposition currently starts at 4404 and its β-normalization equation is at 4422. HINT2 itself uses the locating string L5 rather than a PROOF numeric line here; its substantive error is the stale interpretation of that source, F4. These positions were located by string search and checked with bounded sed ranges; none was inferred from an offset.

E2 correctly repairs the c/e powers, E3 the torus harmonic qualification, E4 the sitewise translation-invariance requirement, and E9 the a⁻⁴ factor. E7’s elementary comparison is correct for the stated expression: with x=log(1/g), exp(−cx^(2p))/g²=exp(2x−cx^(2p))→0 iff 2p>1 or (2p=1 and c>2). At equality c=2 the ratio is 1. That algebra does not validate its source attribution to a single lane large-field weight. E8 must be applied to the observed spectral contraction as in F7. The timing errata do not affect a mathematical constant, but exact historical creation order is NOT-VERIFIED.

## Summary table

| Finding | Review verdict | Claim status / disposition |
|---|---|---|
| F1: ID♮ | CONFIRMED as a C² contraction convention; REFUTED on the stated unrestricted domain; physical identification NOT-VERIFIED | PROVEN jet after C² qualification; reconstructed-theory identification GAP |
| F2: PAIR / matrix colours | CONFIRMED | PROVEN for the stated class; old unequal-colour counterexample excluded |
| F3: all finite KL subtractions / mixtures | CONFIRMED | PROVEN conditional on the specified linear-field spectral representation |
| F4: large-field source / instanton units | REFUTED as pinned; actual TS-up route NOT-VERIFIED | Correct exponent is (4π²/N)u; weak union-bound failure PROVEN under the proposed amplification, actual YM input OPEN |
| F5: NOBS / ξ² | CONFIRMED for ordinary plaquette geometry and the formal coefficient; unrestricted lattice quantifier REFUTED | PROVEN restricted quotient-descent obstruction; κ₂=3N(N²−1)/(8192π⁴); alternative observable identifications remain possible |
| F6: ξ-linear logarithm | CONFIRMED for an explicit smooth heat regulator at formal order; generic regulator claim NOT-VERIFIED | CONDITIONAL asymptotic, coefficient −Nξe²f₀/(16π²); ξ⁰ term and nonlinear continuum realization OPEN |
| F7: exact profiles / T0 | CONFIRMED comparator formulas; FLOW-normalized tree coefficient REFUTED; YM sharp-time limit NOT-VERIFIED | PROVEN free spectral calculation; YM reconstruction/domain GAP |
| F8: REP | REFUTED as written without translation invariance | CONDITIONAL polynomial-contact theorem after adding that hypothesis |
| F9: INT / CONV / usc | CONFIRMED at countable joint-law level; continuum functional identification NOT-VERIFIED | PROVEN conditional inequalities; restore R_F versus R_box; observable limit GAP |
| F10: B-BR and full chain | CONFIRMED as conditional summation/tuning/substitution; unconditional closure NOT-VERIFIED | CONDITIONAL restricted H_int; UIR^♮_br, layer-1 and TS/moment inputs remain OPEN |
| F11: checks / WN | CONFIRMED recorded a FAIL and a2/b/c/d-run2 PASS; historical provenance NOT-VERIFIED | Algebraic checks only; a2 repair genuine; WN PROVEN for specified Gaussian functions; aborted run supplies no result |
| F12: noise / Branch D | CONFIRMED logical separation; nonlinear bounds NOT-VERIFIED | OPEN NOISE-ADD, ANTI-♭/NOISE-SUB, hard-scheme flow and S4c-lin obligations |
| F13: errata / source freshness | E5 index and FLOW’s indirect PROOF citation REFUTED; E2/E3/E4/E9 CONFIRMED | Use K−j, not j; current LF-count normalization at PROOF:4422, not :4162 |

## Numerical corrections and provenance

- In FLOW’s pinned coupling, replace **8π²u** by **(4π²/N)u** in the instanton action. The literal mixed-normalization product **22N²/3** becomes **11N/3**. The latter is the correct physical exponent already quoted by the author, now obtained consistently. This is a factor **2N** error in the written action coefficient, not a correction to the physical 11N/3.
- In the magnetic tree line, replace **(N²−1)g_FLOW²/(32π²)** by **N(N²−1)g_FLOW²/(16π²)**, or explicitly use g_std in the original formula. SU(2): **3/32 → 3/8**; SU(3): **1/4 → 3/2**, as coefficients of g_FLOW²/π².
- The indirect numeric source pointer **PROOF:4162 → PROOF:4422** is corrected by string location; LF-count starts at **4404**. This is a source-location correction, not a scientific constant.
- E5’s depth variable is **K−j**, not j. The R collision is repaired by using **R_F** in U_± and c_W, with **R_box** reserved for volume.
- No correction is needed to L⁴, 3/(128π²), 1/(32π²), CT’s 7/512 and −7/8, or the corrected ξ-linear coefficient. The value κ₂ above is new independent symbolic evaluation, not a refuted prior number. The k₁ conversion remains k_g=k_α/(4π); this review did not rederive the imported perturbative value k_α.

Review sources were restricted to the user-named target/dependency files and named checks, plus the required methodology and selected review-loop guidance. Mathematical source reads were string matches and bounded ranges. No snapshots, audit ledgers, whole-PROOF read, git command, source/check edit, external literature lookup, long job or floating-point numerical calculation was used. Only CODEX_REVIEW_HINT2.md was written. Full upstream analytic results and historical run provenance are explicitly unverified, not silently inherited. Review completed 2026-10-29T04:15:20.104656Z.

## Exactly what may be banked

1. **PROVEN mathematics within the explicit comparator realization:** PAIR, PSD matrix-colour closure, the UV dichotomy for every finite KL subtraction order, mixture separation, the listed covariance-normalized free/contact profiles, and the Gaussian wrapped-normal result. REP needs translation invariance explicitly. The free time-zero magnetic formula has its spectral/domain condition.
2. **PROVEN local/formal checks:** the smooth quadratic contraction, the noncommuting pure-gauge lattice example on an ordinary plaquette, the positive ξ² coefficient (including the independent value above), and the ξ-linear logarithm for the explicitly specified regulator at formal order. These do not construct a nonlinear continuum Gaussian-connection theory or exclude every free observable identification.
3. **CONDITIONAL reductions:** the normalized plaquette INT bound, countable joint-law CONV, upper semicontinuity, and H-RED under F-tune + TS-up + TS-low + MOM-E; B-BR’s positive total slope suffices for the summation/tuning argument with the actual-chain layer-1 hypotheses. Exact 21/22 is not needed for that reduction. Every unresolved analytic or observable-identification premise remains attached.
4. **Do not bank:** an established bare Yang–Mills TS bound, a proof that LF-inst is necessary or already available, a continuum sharp-time/4D-flow observable identified in the reconstructed theory, an algebraic/OS justification of ID♮, an unconditional H_int, or a proof of non-free reconstructed Yang–Mills. **The single most dangerous unverified bridge is the claim that an equivalence to a free reconstructed theory must identify the YM observable through ID♮.** The contraction demonstrably fails to preserve products; assigning that rule does not prove the bridge.
