# Original Q=0 readout on the first winding term: independent check

Disposition: PASS for the exact finite-L recurrence and its identification with the leading effective observable in a real native word-preserving block gauge. The proposed elementary closed form remains a conjecture here; finite checks do not prove it. No repository/shared edits.

Let H(h)=H+h C0 be a formal differentiating family, with C0=V^-1/2 sum Z_z Z_(z+2), and retain the original H at h=0. Every aligned-column configuration has the same zeroth-order value Cvac=sqrt(V), so the unperturbed block stays the same and its h-dependent energy is scalar. On a minimal two-column winding path, each column's occupation subset S changes each distance-two product by -2 when its two endpoints disagree. There are two columns; hence

 Delta C(S)=-4 d2(S)/sqrt(V),
 d2(S)=#{z:1_S(z)!=1_S(z+2)}.

This counts exactly the diagnostic as defined, including repeated oriented distance-two pairs at small circumference. The energy denominator is -[8Jz c(S)+h Delta C(S)]. Differentiating the product at h=0 therefore multiplies the unperturbed negative amplitude by

 -sum_steps Delta C/(8Jz c)
 =sum_steps d2/c /(2Jz sqrt(V)).

The effective source coefficient is consequently negative:

 (C0_eff)_(flipped two columns,initial)
 =-gamma_L A_L/(2Jz sqrt(V)),

with A_L the weighted path average stated by root. No additional derivative of the native transverse numerator is present: h couples only to the diagonal diagnostic in this bookkeeping family.

The recurrence is exact. F(S) is the accumulated product of inverse cluster counts. Multiplying by the additive path statistic gives

 T(S)=[sum_(i in S)T(S\{i})]/c(S)+[d2(S)/c(S)]F(S).

The final full-set step has no intermediate denominator and no extra statistic, so A_L=sum_i T(full\{i})/S_L. I independently implemented rational subset enumeration for L=4,6,8,10. It gives respectively 36/5,40/3,252/13,432/17 and verifies S_L=binomial(2L-2,L-1). These agree with 6(L-1)(L-2)/(2L-3), but I have not derived that formula for arbitrary L. The recurrence itself is already a rigorous finite-L coefficient specification.

## Why this derivative is the original effective observable

Choose an analytic REAL orthogonal block reduction U(h,lambda) based on the fixed N=0 reference block and built from native insertion words with diagonal unperturbed projectors/resolvents. It can be taken as the canonical real Kato/direct-rotation reduction. Since H0+hC0 is diagonal, the reference projector is independent of h in a sufficiently small fixed-L neighborhood. For an exactly block-diagonalized family,

 partial_h H_eff = C_eff + [A_PP,H_eff],
 A=(partial_h U)U^dagger,
 C_eff=P U C0 U^dagger P.

The same equality holds to the retained perturbative order for a finite-order reduction. A_PP is real antisymmetric. Its diagonal entries therefore vanish exactly. Any off-diagonal matrix element between different aligned-column configurations still requires at least L native transverse insertions: differentiating a diagonal denominator does not flip spins or reduce that count. Thus A_PP has no coefficient below order L. The zeroth-order effective Hamiltonian, including h Cvac, is scalar. All lower-order effective terms are diagonal; their first nonconstant aligned-column coefficient begins at order four. Consequently the connection commutator contributes no off-diagonal term at order L (indeed its first possible such contribution is order L+4 in this gauge).

This establishes that the differentiated winding amplitude equals the ORIGINAL transformed C0 matrix element at leading winding order. It is not only a derivative of an arbitrarily relabeled effective energy. Folded/normalization contributions cannot evade the spin-count bound, just as in the Hamiltonian coefficient check.

The real native word-preserving gauge must be stated. An externally chosen h-dependent nonlocal rotation within the aligned-column block can produce an earlier connection and change matrix entries unless observables and basis labels are transformed consistently. Complex diagonal phase gauges also require keeping their connection terms. The claimed simple coefficient is valid in the specified real canonical class, rather than in every possible effective basis.

The h family is a derivative device, not an added physical interaction or source fit. All statements are fixed even L (with the native minimal-winding assumptions). They do not establish uniform leading dominance when L grows with lambda, an exact finite-lambda transition amplitude, a tunneling lifetime, or convergence of the perturbation series.
