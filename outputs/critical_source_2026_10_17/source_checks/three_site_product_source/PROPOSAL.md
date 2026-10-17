# Three-site critical product source and an installed-seed sixth moment

Status: new conditional author derivation, requiring a distinct check. Root proposed the couplings, critical determinant and sixth-moment expression as conjectures to test. They are derived below, not assumed. The isolated scalar source has an exact normalized finite-band measure and a controlled three-coordinate escape comparison. Independently, its first three hops give an actual installed-seed moment insensitive to the subsequent load. Neither statement supplies the interacting processor's common output waveform or runtime.

## 1. Scalar model and positive realization

Let j>0, 0<lambda/j=eta<=1/16, and set

    a=lambda/sqrt(3), b=lambda sqrt(8/3),
    kappa=sqrt(3j lambda).

The three source heads are 0,1,2. A uniform lead begins at 3. The carrier-subtracted one-head Hamiltonian has hoppings −a on 0–1, −b on 1–2, −kappa on 2–3, and −j thereafter, with zero diagonal. The physical carrier is 2j.

Use positive exchanges on these bonds and occupations

    (2j−a)n0, (2j−a−b)n1,
    (2j−b−kappa)n2, (j−kappa)n3.

All later occupations vanish. They are nonnegative on the declared domain: a+b<3lambda, b<2lambda and kappa/j<=sqrt(3/16)<1/2, so b+kappa<5j/8. Thus all head diagonals are exactly 2j and no vacancy scalar is introduced. These are real NN one-/two-qubit positive blocks on a straight path. The endpoint seed is the product head state |0>, not an extended supplied pulse. Coupling correlations and preparation remain supplied premises.

## 2. Exact determinant, density and normalization

For the outgoing halfline Weyl function m_j(z)=[z−sqrt(z²−4j²)]/(2j²), with branch asymptotic to z, the source Schur matrix is

    [[z,a,0],[a,z,b],[0,b,z−kappa²m_j(z)]].

Its determinant and first forcing column are

    D(z)=(z²−a²)(z−kappa²m_j(z))−b²z,
    R00=[z(z−kappa²m_j)−b²]/D,
    R10=−a(z−kappa²m_j)/D, R20=ab/D.             (1)

The signs follow from z−h. Replacing only the lead self-energy by its center value −i3lambda gives

    D_M(z)=(z²−lambda²/3)(z+i3lambda)
                         −(8lambda²/3)z
          =(z+i lambda)^3.                       (2)

Thus the proposed cubic critical determinant is exact for this rational comparison, not for the actual lattice.

On |delta|<2j put s_delta=sqrt(1−delta²/(4j²)). The actual self-energy is (3eta/2)delta−i3lambda s_delta. The seed density follows from the imaginary boundary load and R20:

    rho0(delta)=3lambda s_delta |ab/D_+(delta)|²/pi
              =8lambda^5 s_delta/(3pi |D_+(delta)|²).        (3)

It is the actual endpoint measure once absence of other spectral mass is established. On the physical band,

    D_+−D_M=[−(3eta/2)delta+i3lambda(s_delta−1)]
                                      (delta²−lambda²/3).

Use |delta²−lambda²/3|<=delta²+lambda² and 1−s_delta<=delta²/(4j²). Dividing by |D_M|=(delta²+lambda²)^(3/2), the real correction is at most 3eta/2. The remaining correction is at most 3lambda|delta|/(4j²)<=3eta/2. Therefore

    |D_+−D_M|<=3eta |D_M|,
    |D_+|>=(1−3eta)|D_M|>0.                     (4)

This includes the two thresholds. Outside the band, for x>=2j, 0<m_j(x)<=1/j and x²>a², so

    D(x)>=(x²−a²)(x−3lambda)−b²x
         =x³−3lambda x²−3lambda²x+lambda³>0.

Indeed x/lambda>=32 and 1−3/32−3/32²>0. The exterior Weyl function is odd, hence D(−x)=−D(x), also nonzero. There are no exterior poles or threshold atoms. The explicit algebraic resolvent has regular interior boundary values by (4), analytic exterior continuation, bounded thresholds and 1/z seed asymptotic. Its Cauchy representation is therefore exactly (3), with total mass one and no residual singular measure. Nonzero Jacobi bonds make |0> cyclic; there is no hidden scalar bound sector elsewhere.

## 3. Controlled reference for all three source amplitudes

The rational comparison seed density is

    rho_M(delta)=8lambda^5/[3pi(delta²+lambda²)^3]

on the full real line. Its integral is one. Its return and the two associated polynomial-weighted Fourier amplitudes, for x=lambda t>=0, are

    A0,M=e^(−x)(1+x+x²/3),
    A1,M=i e^(−x)(x+x²)/sqrt(3),
    A2,M=−e^(−x) sqrt(2)x²/3.                    (5)

These follow by differentiating the Cauchy Fourier integral twice, or directly from (2). The polynomial weights are dictated by the ACTUAL source path:

    |1>=−h|0>/a,
    |2>=(h²−a²)|0>/(ab).

Consequently the exact amplitudes use weights 1, −delta/a and (delta²−a²)/(ab) against rho0. In particular the second intermediary is not omitted, and its negative short-time amplitude −ab t²/2 agrees with (5).

Here are explicit conservative comparison errors. Set

    q=1−3eta, C=6eta+9eta²,
    E0=(C+eta²/12)/q²+eta^5/(30pi),
    E1=[4sqrt(3)C/(3pi)+sqrt(3)eta²/(3pi)]/q²
                                      +sqrt(3)eta^4/(12pi),
    E2=[C/sqrt(2)+5eta²/(12sqrt(2))]/q²
                     +eta³/(3pi sqrt(2))+eta^5/(60pi sqrt(2)). (6)

Then the full-line weighted density errors for the respective three weights are bounded by E0,E1,E2. To verify these constants, (4) gives on the physical band

    |rho0−rho_M|<=rho_M[C+(1−s_delta)]/q².

The needed reference moments are

    E_M(delta²)=lambda²/3, E_M(delta^4)=lambda^4,
    E_M|delta|=4lambda/(3pi),
    E_M|delta|³=4lambda³/(3pi).

For the third weight use |delta²−a²|<=delta²+a². Its unweighted moment is at most 1/sqrt(2), and its square-root correction is at most 5eta²/(12sqrt(2)). The analogous correction moments for weights 1 and |delta|/a are eta²/12 and sqrt(3)eta²/(3pi). Finally, integrating the majorant rho_M<=8lambda^5/(3pi delta^6) over |delta|>2j, with the three absolute weights, yields exactly the outside terms in (6). Thus physical band corrections and reference tails are both paid; no Markov model is promoted to exact evolution.

For Psrc projecting onto sites 0,1,2, define

    F(x)=e^(−x) sqrt[(1+x+x²/3)²+(x+x²)²/3+2x^4/9],
    Evec=sqrt(E0²+E1²+E2²).

The complete three-source escape bound is

    ||Psrc exp(−ith)|0>||<=min{1,F(lambda t)+Evec}.             (7)

All three phases and occupations enter this vector norm. The E_i are O(eta), so this gives a quantitative small-residual regime as lambda/j decreases. For example, if Evec<=zeta/2 and lambda t>=2log(18/zeta), then (7)<=zeta. A sufficient elementary witness is F(x)<=e^(−x)(1+2x+2x²)<=9e^(−x/2), using x e^(−x/2)<=1 and x²e^(−x/2)<=3.

For any fixed positive admissible eta the exact three weighted densities are integrable, so their Fourier transforms tend to zero by the Riemann–Lebesgue lemma. Thus the exact source norm tends to zero even when the comparison floor Evec is not small. This last qualitative statement has no additional quantitative onset. Escape from these three sites is not arrival at a chosen distant site or a complete old-gate operation.

## 4. Exact sixth central moment of the ACTUAL installed seed

Now replace the uniform lead beyond site 2 by an arbitrary actual self-adjoint downstream apparatus. Its port is site 3, connected only to site 2 by −kappa. Retain the three source diagonals c+2j+B, their scalar bonds −a,−b, and no head-dependent contacts on source sites 0,1,2. The shared source vacuum satisfies B iota=iota K. The seed has head 0, source vacuum, initial record0 and arbitrary old input. Existing head-dependent downstream contacts, branches and reflected returns are permitted after the port; no source approximation is made.

For old-energy projection Pi_e, e=1 or 3, put E_e=c+2j+e and V for this product preparation. On that prepared range (H−E_e) has zero source-site diagonal and the three physical hopping steps specified above. Direct application gives

    (H−E_e)V Pi_e=−a |1> iota Pi_e,
    (H−E_e)²V Pi_e=(a²|0>+ab|2>) iota Pi_e,
    (H−E_e)³V Pi_e=
       [−a(a²+b²)|1>−ab kappa|3>] iota Pi_e.       (8)

The two terms have orthogonal head support. Therefore the exact sixth moment is

    Pi_e V*(H−E_e)^6 V Pi_e=mu6 Pi_e,
    mu6=a²(a²+b²)²+a²b²kappa²
       =3lambda^6+(8/3)j lambda^5.               (9)

This verifies root's proposed formula. A sixth-moment expectation equals the squared norm of the THIRD-power vector, so no downstream action after first arrival at site 3 enters it. Port diagonals and port contacts would act on the fourth application, not on (8). The physical construction should still retain its intended port diagonal via compensation; that value is not an extra hidden requirement of the moment identity itself. Contacts on any of source sites 0,1,2, an additional edge from these sites, or a nonvacuum initial internal state can invalidate (8) and must not be included without a new calculation.

For bounded lattice apparatus the power/domain conditions are automatic. More generally (9) requires the prepared vectors in the domain of the third power so the spectral sixth moment is their squared norm; a formal walk expansion does not waive this condition.

Let d>0 and I_e=[E_e−d,E_e+d], I=I_1 union I_3. The spectral theorem gives

    ||E_H(I_e^c)V Pi_e||<=sqrt(mu6)/d³.

For arbitrary superpositions of the two old-energy inputs, triangle inequality followed by Cauchy–Schwarz gives

    ||E_H(I^c)V||<=min{1,sqrt(2mu6)/d³},
    0<=V*E_H(I^c)V<=min{1,2mu6/d^6} I_old.        (10)

No commutation of actual H with K or orthogonality of the omitted output ranges is assumed. This includes all outside spectral types, wrong-window leakage and passive references. Initial record0 is retained coherently. The moment estimate needs no downstream small-reflection premise and remains valid even if the actual source never emits appreciably.

The leading moment cost at small lambda/j is proportional to j lambda^5, not lambda^6 alone. Dropping the port-reaching term would give a false stronger concentration estimate. For a desired omitted amplitude epsilon_sp, the actual sufficient condition supplied here is 2[3lambda^6+(8/3)jlambda^5]<=epsilon_sp² d^6; no operating point or optimized scaling is selected.

## 5. Attachment, finite realization and remaining obligations

For an isolated finite scalar model retain M>=1 uniform lead sites 3,...,M+2 and add the exact cap j n_(M+2). At M=1 this cap shares site 3 with its occupation j−kappa. There are M+3 heads, M+2 exchange bonds and five separately listed occupation/cap blocks, hence M+7 positive blocks before merging coincident occupations. The one-head compression is exact. Source row sums are below 2j and the first/later lead rows are at most 2j. The first omitted head is M+3 hops from seed 0, giving the conservative evolution comparison 2F_(M+3)(2j|t|). This is a finite-horizon existence tool, not an economical receiver count or all-time escape theorem.

At an actual old port, replacing a j edge by kappa<=j requires the positive (j−kappa)n_port compensation to preserve its diagonal. Real NN placement, collision avoidance and selective removal/replacement of the correct edge remain installation obligations. The old/source fiber is shared once. The new source blocks add no vacancy scalar, so actual old aging and all existing physical scalars remain present.

Equations (3)–(7) describe the ISOLATED uniform-ray scalar source. Equation (10), in contrast, describes the ACTUAL installed seed under its local structural premises. It is invalid to combine them into an actual escape theorem merely because they use the same first three couplings. The downstream operator-valued kernel can alter in-band residence, phases, outgoing amplitudes and record dependence without altering the finite moment. Complete outgoing rows, both physical windows/lips, wrong-window input, finite/core/closed-tail decay, one common waveform times literal W, and finite-time transfer remain open for the attached device.

## Exposure and verification status

Root supplied the candidate couplings, cubic determinant and moment as hypotheses, after the two-site work. I authored this derivation, not an independent check. The conventions and qualified source interfaces are reused from `two_site_product_source/PROPOSAL.md` (`8892741e6a14bca4565aef77d5913a3afca43a850c202c43dc2afb8ed3d9e303`), the inverse source (`33b4f11058bd8953f6ea1cc03e85fde8f884f2ac2cf2eadd22f509f0b390ca4d`) and the slow-source moment/feedback proposal (`17785cc71bf41eb0fbca7c4bcccadb94631199994002a013799299d7d66a65a3`). Their actual output/runtime conclusions are not premises of this new scalar calculation. I previously checked several of those interfaces and related capture work; source exposure is not independence.

A distinct check is required, especially for all three weighted density comparison constants, threshold/exterior normalization, the exact third-power support and the distinction between isolated escape and installed concentration. No scientific execution, numerical spectrum, quadrature, sweep, Git/canonical edit, publication, checkpoint, prompt, model or delegation change occurred. No general-n theorem, native supplier, permanent halt, reset/reuse, or actual apparatus improvement is claimed.
