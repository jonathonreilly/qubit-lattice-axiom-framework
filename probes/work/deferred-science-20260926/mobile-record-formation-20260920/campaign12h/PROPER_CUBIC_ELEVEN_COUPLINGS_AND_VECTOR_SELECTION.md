# Removing the extra reflection premise: all eleven proper-cubic couplings

2026-09-21. Provisional author construction, using the same uniform
fifteen-state tangent and positive entropy metric as the independently checked
five-coupling classification. This extension is initially author-checked;
the earlier independent report covers the exact dimension eleven but does
not automatically cover the six explicit additional maps below.

This directly addresses the repository's proper 24-element symmetry. No
spatial reflection symmetry is assumed. The completely specified alphabet,
uniform law, entropy compatibility and first-order restriction remain added
model premises; this does not classify every axiom-admissible theory.

## The six missing couplings

Use the same orthonormal coordinates (E; s1,s2,B,d1,d2,t12,t13,t23,w), diagonal
traceless tensors D_alpha and off-diagonal tensors Q_ij. The previously
displayed five-parameter symmetric symbol A_5(q) remains allowed. Add six
real coefficients b1,b2,b_u,b_v,d,g as follows, always including the transpose
of each displayed off-diagonal block:

    A_(B,s1)=b1 q,       A_(B,s2)=b2 q,
    A_(B,d_alpha)=b_u D_alpha q,
    A_(B,t_ij)=b_v Q_ij q,
    A_(t_ij,d_alpha)=d Tr[Q_ij ([q]_cross D_alpha-D_alpha [q]_cross)],
    A_(t,w)=g (q3,q2,q1)^T.

The first four maps are the E scalar/tensor maps with B in its place. They
are proper-cubic intertwiners because polar and axial vectors have the same
action when det(Q)=1. The fifth uses the infinitesimal rotation commutator:
for diagonal symmetric D and antisymmetric C=[q]_cross, CD-DC is symmetric
and purely off-diagonal. Proper signed permutations preserve the diagonal
and off-diagonal tensor subspaces and send C to QCQ^T, proving covariance.

For the sixth map, w transforms by the sign of the coordinate permutation.
The off-diagonal tensor (t12,t13,t23) transforms with the product of the two
corresponding axis signs. For det(Q)=1, multiplying this product by the
permutation sign gives the sign of the complementary axis. Thus
(q3,q2,q1) has exactly the required T2/A2 covariance. This check uses the
actual discrete triple moment, not an assumed rotational scalar.

The six maps have disjoint blocks and are independent of the original five.
The independently established character count is eleven. Therefore these
eleven independent maps exhaust all real symmetric proper-cubic linear
symbols at this background.

The same formula S_i=(15/2)U A_i U^T realizes every one through the already
proved local positive context-exchange generator. Product stationarity,
content permanence and the exact uniform current derivative do not require
reflection covariance. Four context sites are distinct, as in Z^3 or
periodic sides at least four. This extends the microscopic realization; it
does not add a continuum-limit theorem.

## Which earlier selection conclusions survive

Full closure of the six raw-vector observables for arbitrary other moments
now requires

    a1=a2=u=v=b1=b2=b_u=b_v=0.

The surviving E/B block is again the unique curl coupling m. The two purely
nonvector couplings d,g can remain nonzero without feeding the vectors.
Likewise, invariance of q.E=q.B=0 for arbitrary remaining moments imposes
these same eight zero conditions. Thus the **conditional selection of the
closed vector Maxwell shape does not require spatial reflections**.
It still requires the stated closure or raw-Gauss-preservation premise.

The derivative curl pair (i[q]_cross B,-i[q]_cross E) closes under the weaker
conditions u=v=b_u=b_v=0. The four scalar coefficients drop out because
[q]_cross q=0; d,g also remain allowed. Both statements are for every q and
arbitrary excluded moments, not a single propagation direction or prepared
subset of states.

The full fourteen-field spectrum need not have ten zero speeds after only
the vector sector has been closed. The d,g sector can propagate separately.
For example, its t-versus-(d1,d2,w) block is

    [ 2d q3          0        g q3 ]
    [ -d q2   -sqrt(3)d q2    g q2 ]
    [ -d q1   +sqrt(3)d q1    g q1 ].

Its determinant is -6sqrt(3)d^2 g q1 q2 q3. With all those factors nonzero,
it gives six extra signed speeds. Together with m!=0 the closed-vector
case has ten propagating speeds and four zeros. At special directions or
coefficients degeneracies increase. These extra moments are not identified
with matter, gravity or physical spin-two degrees of freedom.

## Internal reversal can replace the extra reflection assumption

The specified internal A-sign reversal still has T=diag(-I3,I11). Each of
the six newly added maps is entirely within the even block, so T A_extra T
=A_extra. In contrast T A_5 T=-A_5. Independence gives

    T A(q) T=-A(q) for every q  iff  b1=b2=b_u=b_v=d=g=0.

Consequently proper cubic symmetry plus this additional generalized time
reversal selects the same five-dimensional family without adding spatial
reflections. The reversal itself is not a repository axiom. At the local
generator level the earlier exact adjoint construction applies to that
restricted five-dimensional family; it is not claimed for all eleven.

The author checker verifies all eleven proper-group intertwiners, the added
maps' reversal parity, the two closure conditions, and the nonvector block
determinant. The new maps and their implications need their own independent
check before inheriting the earlier classification's review status.
