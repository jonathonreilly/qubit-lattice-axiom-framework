# Independent base reconstruction, before author checker/results

2026-09-21. The complete 187-line source note was read at SHA-256
58bb81005b17fe6a699a23e1a3b77acaa00b3f2d65aefb46f9053729639e6f26.
No author classification checker, result or log has been opened.

## Representation and completeness

At the uniform fifteen-label law, the probability tangent is 1-perp and
the entropy Hessian is 15I. A real entropy-compatible principal symbol is
therefore a symmetric matrix-valued linear function of a polar covector q.
The six polar axis labels give A1g+Eg+T1u; the eight axial cube vertices
give A1g+A2g+T1g+T2g. Vacancy contributes another trivial representation;
removing the constant leaves 2A1g+Eg+T1u+A2g+T1g+T2g, dimension fourteen.

This decomposition was checked directly, without importing an irrep table.
Generate all signed permutation matrices Q and their fifteen-label actions,
using det(Q)Q on B. Form the orthogonal projectors from the displayed
observable basis. Their six distinct character vectors have exact character
inner-product matrix I; two copies of the trivial character are present.
Their sum with multiplicity reproduces fixed-label-count minus one for
every group element. The complete basis is orthonormal and orthogonal to 1.

Inversion changes only the E block. An odd-in-q symmetric symbol thus has
only E/even blocks. The exact character projection
average tr(Q)[chi(Q)^2+chi(Q^2)]/2 equals 5 for all 48 matrices and 11 for
the proper 24. Direct pair-tensor covariance under every species permutation
verifies the five explicit maps q*s1, q*s2, q cross B, D_alpha q*d_alpha,
and Q_ij q*t_ij. They have disjoint even input supports and are independent.
They exhaust the five-dimensional full48 family. The proper24 count is a
strictly larger classification; the reflection assumption cannot be silently
dropped. There is no w coupling in the full48 family.

## Gram matrix, isotropy and closure

For K with the columns in the note, scalar columns give (a1^2+a2^2)qq^T,
the cross block gives m^2(|q|^2I-qq^T), and the two tensor sums give

    sum_alpha D_alpha q q^T D_alpha = diag(q_i^2)-qq^T/3,
    sum_ij Q_ij q q^T Q_ij = |q|^2 I/2+qq^T/2-diag(q_i^2).

These establish the displayed Gram formula exactly. Since K is 3 by 11,
rank r gives 2r nonzero signed speeds and 14-2r zero speeds. Generic rank
three gives six/eight. Pure diagonal coupling has rank one on a coordinate
axis and rank two at q=(1,2,3): rank two does not alone mean isotropic
transverse propagation.

A noncubic rotation taking e1 to (3/5,4/5,0) produces off-diagonal covariance
residual -12(u^2-v^2)/25. Thus rotational covariance of the Gram matrix for
all q requires u^2=v^2. That condition is sufficient and gives c_T^2=m^2+u^2/2
and c_L^2=a1^2+a2^2+2u^2/3. This is a Gram/isotropic-speed statement, not
full continuous-rotation covariance of the finite microscopic alphabet.

Full closure of all six vector coordinates for arbitrary other moments
requires a1=a2=u=v=0, by independent variation of the excluded inputs.
The remaining symbol has characteristic polynomial
lambda^10(lambda^2-m^2|q|^2)^2. Four nonzero speeds require m!=0 and q!=0;
otherwise degeneracies increase. Scalar gradients alone do not force the
transverse E/B sector, so that sector can remain invariant while extra
longitudinal sound is present. Full vector closure is the stronger premise.

The exact nonnegative longitudinal Gram form is the sum of squared scalar
and tensor contractions shown in the note. At q=e1 its vanishing already
forces a1=a2=u=0, for real coefficients. Then q=(1,1,0) forces v=0. Hence
an E-longitudinal null direction for every q selects the same member.

## Microscopic realization and normalization

For U the orthonormal species-observable matrix, S_i=(15/2)UA_iU^T is
symmetric, tangent (S_i1=0), and a polar vector of pair tensors under the
species permutation. On a four-site context use h=S(l,a)+S(a,r)-S(l,b)-S(b,r).
The central exchange changes h to -h. Summing h on a periodic line cancels
both nearest and distance-two pair sums. Since homogeneous product weights
are invariant under central exchange and c(h)-c(-h)=h, the product adjoint
balance defect vanishes. Every homogeneous product is stationary.

When a spatial signed permutation reverses the bond orientation, the
transformed ordered context is (Qr,Qb,Qa,Ql) in label-action notation.
The polar S sign and reversal of the symmetric-argument expression each
contribute a minus sign, leaving h and c invariant. Reflection covariance
therefore holds for these actual positive-part rates, not merely for their
mean current. Fixed finite S gives kappa <= c <= kappa+4 max|S|.

For distinct endpoint/context sites (in particular Z^3 or tori of periods
at least four), central-swap symmetrization yields

    J_a = E[c(1_left=a-1_right=a)]
        = (1/2)E[h(1_left=a-1_right=a)]
        = 2p_a[(Sp)_a-p^TSp].

The two outside labels contribute twice Sp after conditional averaging.
No independent-current factorization is being assumed for a correlated
future law. At p*=1/15, Sp*=0, and the exact tangent derivative is
DJ=2S/15=UA_iU^T. Thus the factor 15/2 is correct.

This normalization was checked by an actual exact sum over all 15^4 four-label
contexts for each of three directions, with nonuniform rational p_a=(a+1)/120,
kappa=1 and nonzero coefficients (sqrt(21),sqrt(105),2,3,sqrt(2)). These choices
produce rational embedded S. The sum uses the positive-part rate itself,
not a finite-difference approximation or only the averaged h expression.
All fifteen exact currents match the formula, and the uniform derivative
normalization is exact. Independent pointwise periodic balance and all48
orientation-reversed rate controls also pass.

For arbitrary interior p, write p as a softmax of entropy variables theta.
Since D_theta p=diag(p)-pp^T, the gradient of Phi_i=p^TS_i p is exactly J_i.
Its entropy-variable Jacobian is therefore symmetric; this supplies the
claimed nonlinear entropy compatibility. It is not a new hydrodynamic
limit proof. The realization remains a supplied finite-range exchange model
of unchanged labels, with occupied/occupied exchanges included.

## Status and remaining scope

The independently written exact checker passed all fourteen groups on its
first execution. No substantive base-classification defect was found.
Local-current formulas use the conventional distinct four-site footprint;
aliased tiny tori are outside that use unless separately evaluated. All
new construction and continuum/physical interpretations retain the note's
stated conditional boundaries. This initial evidence is sealed before the
author checker/results and before examining the proposed dependent addendum.
