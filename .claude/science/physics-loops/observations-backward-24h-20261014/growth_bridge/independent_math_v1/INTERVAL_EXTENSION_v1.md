# Independently derived interval ambiguity and tensor-ratio discriminator

This supplements the frozen proof `PRECHECK_v1.md`. Root's qualitative notice of multiple admissible finite-epoch roots was known; no root growth note, code, values, or derivation has been read. The following explicit family and tensor inverse were derived directly from equation (8) of that proof. No author implementation is used.

Write b_i=alpha_i^2 and v_i=Fc_i/B_i. Suppose two candidate solutions on a connected interval have distinct b1,b2 and satisfy

    I+d_i=v_i L r_bi(q),
    r_b(q)=b(1-3q)/(b-q),
    1/4<b_i<1/3, v_i>0, 0<q<min(b1,b2).

Their quotient gives, with lambda=v1 b1/(v2 b2)>0,

    (I+d1)(b1-q)=lambda (I+d2)(b2-q).

Consequently

    q(I)=[(lambda b2-b1)I+lambda b2 d2-b1 d1]
         /[(lambda-1)I+lambda d2-d1].                         (A)

On a subinterval with R=I' nowhere zero and nonconstant q, the denominator does not vanish and this is a nonconstant fractional-linear (Möbius) function of I. If the coefficient of q vanished at an isolated point, the numerator would have to vanish too; for distinct b and nonzero I+d_i (forced by L and positive F), this is impossible. The denominator cannot vanish identically either unless lambda=1,d1=d2, in which case distinct b would require I+d1=0 identically, contradicting R!=0. Formula (A), together with the original closure and strict domains, is therefore necessary for two distinct shapes. It is not sufficient for an arbitrary L: L must also equal (I+d1)/(v1 r_b1(q)).

Conversely, choose b1,b2,d1,d2,v1,v2 satisfying the strict gates, define q by (A), and define L by either original closure. Wherever denominators are nonzero and the gates hold, both shapes then satisfy the entire reduced lensing/conservation system. Deriving q from the growth quotient additionally requires the supplied H history to obey the growth equation; it cannot be inferred from just this manufactured algebraic construction. There is no full background-action solution claim.

A decisive varying-q interval fixture on I>=0 is

    b1=2/7, d1=1, v1=1,
    b2=3/10, d2=2, v2=20/9,
    lambda=3/7,
    q=(11I+2)/(40I+10),
    L=3(I+1)(I+2)/(2(7I+4)).                                 (B)

Here q rises from 1/5 toward 11/40, which is below both b1 and b2. Both relative histories are positive and strictly above their own positive Fc/B:

    F1/B1=2(7I+4)/(3(I+2)),
    F2/B2=2(7I+4)/(3(I+1)).

This is exact ambiguity across every epoch, not a failed numerical fit or just a three/four-point interpolation. It illustrates why rank-four is a genuine gate and why an additional sampled epoch need not remove an already exact interval ambiguity.

A sufficient interval uniqueness criterion for b is that q as a function of I is not of the fractional-linear form (A), in a varying-q nonzero-R interval, provided a candidate solution exists. A fractional-linear q is a necessary exceptional condition for nonuniqueness, not by itself a proof of nonuniqueness: L, positive constants and strict candidate domains must also admit both solutions. The linear-lift rank condition is a separate convenient sufficient finite-row gate. The exact interval admission set is all (b,d,v) satisfying the original identity with domains, not one root selected by an optimizer.

## A supplied tensor ratio can distinguish the exceptional pair

Suppose an independently calibrated tensor propagation/endpoint measurement provides T=F(N2)/F(N1)>0. This is an additional physical supplier; no actual tensor observation or calibration is asserted here. The candidate gives

    T=[(1-3q2)/(1-3q1)] [(b-q1)/(b-q2)].

If q2!=q1, define Y=T(1-3q1)/(1-3q2). Then

    b=(Y q2-q1)/(Y-1).                                     (C)

For a valid finite b, Y!=1 when q2!=q1. The inferred b must still satisfy 1/4<b<1/3 and q_i<b. At fixed distinct q1,q2 the tensor ratio is strictly monotone in b because the derivative of (b-q1)/(b-q2) is (q1-q2)/(b-q2)^2, so a valid ratio distinguishes the two shapes. If q is constant at those endpoints, the candidate gives T=1 for every b; that pair supplies no shape information. A value Y=1 with q2!=q1 gives no finite solution, not an infinite-precision identification.

For fixture (B) between I=0 and I=1, q1=1/5, q2=13/50. The two predicted tensor ratios are 11/6 and 11/8, respectively, and (C) returns 2/7 and 3/10. The ratio removes neither the overall F normalization nor the need for a physical tensor-to-F map. It does not select an initial scalar state or establish full action membership.
