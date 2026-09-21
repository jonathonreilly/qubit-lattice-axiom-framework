# What cubic symmetry actually selects in the fifteen-state record model

2026-09-21. Provisional, author-reconstructed finite classification. An
independent check is requested separately; this file does not confer retained
status. This is a statement about a specified classical model, not a deduction
of electromagnetism from the repository axioms.

The result is constructive: full cubic covariance and entropy compatibility
allow five independent first-order couplings at the completely uniform
fifteen-state product. Each can be realized by positive bounded local moves
of unchanged records. Requiring the six vector observables to form a closed
linear marginal selects the Maxwell-shaped member of this family. Closure
is an additional premise; symmetry and entropy alone do not supply it.

## 1. Precisely specified premises

The alphabet has vacancy, six polar axis labels e=+/-e_i, and eight axial
cube labels b=(+/-1,+/-1,+/-1). Inactive features vanish. A signed permutation
Q acts by e -> Qe and b -> det(Q)Qb. There are 48 such Q. The repository's
proper 24-element symmetry does not imply this extra reflection symmetry.

Linearize at p_*=1/15 on the probability tangent V=1-perp, dimension 14.
The multinomial entropy Hessian on this Euclidean tangent is 15 I. Thus an
entropy-compatible real first-order symbol A(q)=sum_i q_i A_i is symmetric.
Write R(Q) for the orthogonal species action restricted to V. Covariance is

    R(Q) A(q) R(Q)^T = A(Qq).

No Gauss constraint, elimination of other moments, continuum rotational
symmetry, dissipation or quantum interpretation is built into this definition.

## 2. Complete five-dimensional family

The representation decomposes as

    V = 2 A1g + Eg + T1u + A2g + T1g + T2g.

Here T1u is the polar e vector and T1g the axial b vector. This identification
can be reconstructed from the following orthonormal species observables:

    E_i=e_i/sqrt(2);                   B_i=b_i/sqrt(8);
    s1=(4 1_A - 3 1_B)/sqrt(168);
    s2=(14 1_vac - 1_occupied)/sqrt(210);
    d_alpha=e^T D_alpha e/sqrt(2), alpha=1,2;
    t_ij=b_i b_j/sqrt(8), i<j;
    w=b_1 b_2 b_3/sqrt(8).

D1=diag(1,-1,0)/sqrt(2), D2=diag(1,1,-2)/sqrt(6), and
Q_ij=(unit_ij+unit_ji)/sqrt(2). The symbol uses the coordinate order
(E; s1,s2,B,d1,d2,t12,t13,t23,w). All vectors here are linear perturbations
of expectations of these observables, not additional microscopic labels.

Inversion acts negatively only on E. A polar symbol therefore has only
off-diagonal E/even blocks. Every allowed symbol is

    A(q) = [0 K(q); K(q)^T 0],
    K(q) = [a1 q, a2 q, m [q]_cross,
            u D1 q, u D2 q,
            v Q12 q, v Q13 q, v Q23 q, 0].

The five coefficients a1,a2,m,u,v are arbitrary real numbers. The displayed
maps transform covariantly: the two scalar maps are vectors, the cross
product maps axial to polar, and the two tensor blocks are respectively
the diagonal and off-diagonal traceless pieces under signed permutations.
They are independent because their even input blocks are disjoint.

For completeness, their number can be proved without assuming a table of
irreducible representations. Let chi(g)=number of fixed species of g minus
one. The symmetric-square character is (chi(g)^2+chi(g^2))/2. The exact
finite sum

    (1/48) sum_g tr(Q_g) [chi(g)^2+chi(g^2)]/2 = 5

counts Hom(T1u,Sym^2 V), the space of the required symbol families. The
five independent intertwiners therefore exhaust it. The same exact sum
over the proper 24-element group is **11**, not five. No complete formula
for that larger family is asserted here. The attached script reconstructs
all permutations and both integer counts from the alphabet itself.

## 3. Spectrum, isotropy, and what closure adds

The nonzero characteristic speeds are plus/minus the singular values of K.
Direct polynomial multiplication gives

    K K^T = (m^2+v^2/2)|q|^2 I
      + (a1^2+a2^2-m^2-u^2/3+v^2/2) q q^T
      + (u^2-v^2) diag(q_1^2,q_2^2,q_3^2).

At a generic nonzero q and generic coefficients K has rank three, giving
six nonzero speeds and eight zero speeds. Degenerate cases can have lower
rank. A rank-two symbol by itself does not identify transverse Maxwell
polarizations: for example, the pure diagonal-tensor coupling has rank at
most two and need not be isotropic.

The displayed Gram matrix is rotationally covariant for every real q iff
u^2=v^2. In that case its transverse and longitudinal eigenvalues divided
by |q|^2 are respectively

    c_T^2=m^2+u^2/2,
    c_L^2=a1^2+a2^2+2u^2/3.

Thus cubic symmetry does not require isotropy. Even isotropy permits scalar
and tensor propagation. These additional modes are not automatically
unphysical; their presence could be appropriate in a theory with matter.

The full six-vector marginal (E,B) is closed for arbitrary perturbations
of all fourteen fields iff a1=a2=u=v=0. Necessity follows by independently
varying each excluded moment and q in the E equation. Sufficiency follows
from the displayed block. For m!=0 this leaves

    A_EB(q)=[0 m[q]_cross; -m[q]_cross 0],
    det(lambda I-A)=lambda^10(lambda^2-m^2|q|^2)^2.

There are four transverse propagating modes and ten zero speeds. This is
the Maxwell-shaped classical principal symbol in normalized coordinates,
up to the sign convention for m. It is not physical electromagnetism.
Scalar couplings alone can leave the transverse E/B subsector invariant
while adding longitudinal sound. Hence full marginal closure is stronger
than the existence of a transverse wave subsector.

The nonnegative identity

    q^T K K^T q = (a1^2+a2^2)|q|^4
      + u^2 sum_alpha(q^T D_alpha q)^2
      + v^2 sum_ij(q^T Q_ij q)^2

also shows that an exactly zero E-longitudinal Gram direction for every q
forces those four coefficients to vanish. No probability distribution on
coefficients or naturalness measure is assumed.

## 4. All five possibilities have local immutable-record realizations

Let U be the 15 by 14 matrix of the orthonormal observables above. For each
coordinate i embed the desired symbol into species space and set

    S_i=(15/2) U A_i U^T.

Then S_i is real symmetric and S_i 1=0. On a positive-i bond let l,a,d,r
be the four consecutive labels and choose

    h_i=S_i(l,a)+S_i(a,r)-S_i(l,d)-S_i(d,r),
    c_i=kappa+max(h_i,0), kappa>0.

Exchange the two entire central labels, including occupied/occupied pairs.
This preserves every record's content and site capacity. All coefficients
are fixed and the alphabet is finite, so the rates have a fixed positive
floor and finite ceiling. The h sum telescopes pointwise on each periodic
line. Under a central swap h reverses sign. Consequently every homogeneous
product measure is invariant. The signed-permutation covariance of S and
its symmetry under exchanging arguments also give covariance of the rates
when coordinate orientation reverses.

Symmetrizing the exact product current under the central exchange gives

    J_a,i(p)=2 p_a[(S_i p)_a-p^T S_i p].

This holds for every homogeneous product; it is not a mean-field factorization
of an evolving correlated law. At p_*, S_i p_*=0, so on the tangent

    D J_i(p_*) = (2/15) S_i = U A_i U^T.

Thus the complete five-dimensional family is microscopically realizable by
these supplied local generators. The entropy compatibility away from p_* also
follows from the potential p^T S_i p in multinomial entropy variables. The
construction is the general pair-potential version of the context-exchange
mechanism in PR 8560. It supplies no new hydrodynamic proof here; any use as
a macroscopic limit must retain the previously stated limit hypotheses.

## 5. Verification and consequence for the research decision

`cubic_entropy_symbol_check.py` computes the two exact character counts and
the symbolic Gram identity. It checks orthonormality, all five intertwiners
under all 48 group elements and three directions, the two spectra, the
microscopic product-current derivative, swap antisymmetry and telescoping.
The finite-difference derivative is explicitly an approximate control;
the proof of that derivative is the exact identity above. Output records
actual errors and tolerances. No production simulation or new continuum
limit is claimed. The current source and result should be read alongside
the separate independent report when that exists.

The highest-value new obligation is a reason why the observable vector
sector is closed, or a controlled explanation of its coupling to the other
moments. Merely imposing cubic covariance or entropy stability cannot supply
that reason in this specified alphabet. A successful selection principle
would have to come from an additional justified premise, an emergent
decoupling limit, or evidence matching the observed interactions. The result
does not rule out the record programme or other alphabets and backgrounds.
