# Perturbed three-source attachment: full inverse and actual seed moment

Status: new authored conditional interface requiring a distinct check. This extends the checked scalar perturbation parameters to the actual installed background, proving an explicit full-fiber loaded-inverse criterion and an actual prepared-seed sixth moment. It does not transfer scalar packet/time stability to complete apparatus robustness or choose a useful numerical tolerance.

## Physical construction and retained domain

Use the exact three-site installed geometry and its original calibrated .0027<j<.003. Intersect the scalar perturbation domain with the installed source domain:

    0<lambda<=1e−8, eta=lambda/j<=1/16,
    a1²=(lambda²/3)(1+e1),
    a2²=(8lambda²/3)(1+e2),
    kappa²=3jlambda(1+e3),
    |e_i|<=epsilon, |d_i|<=epsilon lambda,
    B_eps=20epsilon+16epsilon²+4epsilon³,
    q=1−3eta, chi=B_eps/q<1, epsilon>=0.

All couplings are positive real with the same negative hopping signs. The condition implies epsilon<1/20. The detunings d_i are real multiples of the FULL internal identity at source site s_i. They cannot depend on old energy, record, parity or source excitation.

Retain 0<g<=1e−6, 0<h<=4e−6, d=2j sin h, d/g<=1/2 and the unchanged two windows I_e=c_att+2j+e+[−d,d], e=1,3. The port is p=(40,63,1), s2=(40,64,1), s1=(40,65,1), s0=(40,66,1). Replace the source blocks by

    j(n_s2+n_p)−kappa exchange_(s2,p),
    Q_a2(s1,s2), Q_a1(s0,s1),
    (j+d2−a2)n_s2,
    (2j+d1−a1−a2)n_s1,
    (2j+d0−a1)n_s0,
    Q_a(u,v)=a(n_u+n_v−exchange_uv).

These six blocks are positive. Indeed kappa/j<=sqrt(3eta(1+epsilon))<1/2, a2/j<.13 and |d_i|/j<1/320 already follow on the larger scalar domain, while a1+a2<3lambda sqrt(1+epsilon). The occupations therefore have strict positive margins even for negative d_i. The structured port block has eigenvalues 0,j−kappa,j+kappa,2j.

The source diagonals are exactly 2j+d_i, and p retains diagonal 2j. Principal compression off ALL three source heads leaves j n_p, independent of the changed kappa. Hence the emitter-free background operator and its complete kernel G are identical to the nominal installed background. There is no new vacuum scalar: all new terms vanish on blank heads. Shared B is still included once and c_att is unchanged. The identity detunings stay in the source-site operator, not in a discarded or old-input-dependent global phase. Geometry and block counts remain those of the nominal three-site installation.

## Explicit closed and selected reference estimates

On either physical window let D=(E−c_att−2j)I−B, A_i=D−d_i I, and

    P_eps=A0 A1−a1² I,
    Q_ref,eps=P_eps(A2−kappa² m_j(D))−a2² A0.

This is a scalar function of the self-adjoint D, using the outgoing physical j root on the selected open channel and signed real decaying roots on complementary channels. Write delta for the selected D eigenvalue and v=delta²+lambda². The checked scalar perturbation proof gives

    |q_ref,eps(delta)| >= m_eps v^(3/2),
    m_eps=q−B_eps=q(1−chi)>0.                             (1)

Put A_eps=(1+epsilon)²+(1+epsilon)/3. Since |delta−d_i|<=(1+epsilon)sqrt(v), the selected numerator satisfies

    |P_eps(delta)|<=A_eps v,
    |P_eps/q_ref,eps|(delta)<=A_eps/[m_eps sqrt(v)].         (2)

This is not yet a full-fiber assertion. Here is the independent complementary margin. For |x|>=rho=.185 let t_x=lambda/|x|<6e−8 and use |m_j(x)|<=1/j. Then

    |P_eps(x)| >= |x|²[(1−epsilon t_x)²
                                      −(1+epsilon)t_x²/3],
    |x−d2−kappa²m_j(x)| >= |x|[1−(3+4epsilon)t_x].

Both lower factors are positive. Subtracting the other determinant term gives

    |q_ref,eps(x)|/|x|³ >=
      [(1−epsilon t_x)²−(1+epsilon)t_x²/3]
                         [1−(3+4epsilon)t_x]
           −(8/3)(1+epsilon)t_x²(1+epsilon t_x) > .99.      (3)

For an explicit witness, epsilon<.05 and t_x<6e−8 give the first factor >1−6e−9−1.3e−15, the second >1−1.92e−7, and the last subtracted term <1.1e−14. Their product minus that term exceeds .9999997. These estimates hold for both signs of x and do not assume perturbed oddness.

Likewise |P_eps(x)|<1.000001|x|². Consequently the FULL complementary subspace obeys

    ||Q_ref,eps^{-1} C||<170,
    ||Q_ref,eps^{-1}P_eps C||<6.                            (4)

For example 1/(.99*.185³)<170 and 1.000001/(.99*.185)<6. Thus no selected scalar inverse has been promoted to a full inverse. The same bounds hold on either lip; the complementary reference roots there are real.

## Ordered actual loaded inverse

Retain the unchanged emitter-free bound

    ||G−m_j(D)||<=a0+b0|delta|,
    a0=8e−18, b0=46000/.0053+290/g.

Only the background statement is reused, not a nominal-emitter inverse or temporal theorem. The perturbed source Schur matrix and denominator are

    S_eps=[[A0,a1 I,0],[a1 I,A1,a2 I],
                                   [0,a2 I,A2−kappa²G]],
    A=A2−kappa²G,
    Q_eps=P_eps A−a2² A0.

For seed forcing (f,0,0), direct substitution yields

    psi2=a1a2 Q_eps^{-1} f,
    psi1=−a1 A Q_eps^{-1} f,
    psi0=(A1 A−a2² I)Q_eps^{-1} f.                         (5)

A0 and A1 commute because their detunings are scalar identities, but G is not commuted through either. Homogeneous elimination proves that Q_eps invertible implies S_eps invertible, using only a1,a2>0, not inverses of possibly resonant A_i.

The exact factorization is

    Q_eps=Q_ref,eps [I−kappa² Q_ref,eps^{-1}P_eps
                                      (G−m_j(D))].         (6)

A useful energy-resolved bound for its bracket perturbation is

    theta_eps(delta)=kappa²(a0+b0|delta|)
                           [A_eps/(m_eps sqrt(v))+6].

An explicit sufficient uniform criterion is

    Theta_eps=kappa²[(A_eps/m_eps)(a0/lambda+b0)
                                      +6(a0+b0d)] <1.     (7)

It follows by 1/sqrt(v)<=1/lambda and |delta|/sqrt(v)<=1. This criterion is conservative; at epsilon=0 it need not reproduce the sharper nominal Theta3. Its failure is not proof of an actual resonance or impossibility.

Since the selected envelope in (1) exceeds 170 throughout |delta|<=d<=2.4e−8, (1),(4),(6) prove

    ||Q_eps^{-1}|| <=1/[(1−Theta_eps)m_eps v^(3/2)],
    ||Q_eps^{-1}P|| <=1/[(1−Theta_eps)m_eps v^(3/2)],
    ||Q_eps^{-1}C|| <170/(1−Theta_eps).                    (8)

These are full output-row bounds on their indicated input spaces. In (8), Q_eps^{-1}=(I−K_eps)^{-1}Q_ref,eps^{-1}; applying Q_ref first to C is essential. No commutation of the actual load is used. The lower-lip factorization is reapplied in its own order; its Q need not be the adjoint of upper Q.

Together with complete background matching and real root continuation, strict chi<1 and Theta_eps<1 give regular seed boundary values on neighborhoods of the retained closed windows, hence no hidden singular seed mass inside them. This spectral regularity conclusion requires those physical matching premises, not solely an abstract scalar determinant. Both physical windows, both record-X/parity sectors and wrong-window prepared columns are included.

## Actual installed sixth moment with detunings

Let V prepare the head at s0, blank all other heads, source vacuum and computational record0, with arbitrary old input/reference. Let Pi_e be the old K-energy projection, e=1,3, and E_e=c_att+2j+e, exactly the ORIGINAL window center. Shared B obeys B iota=iota K. On the three source sites the centered diagonal on the prepared vacuum is d_i, with no new head-dependent contacts.

Write H_e=H−E_e. Direct application to V Pi_e gives, with the common internal vector iota Pi_e implicit,

    H_e|s0> = d0|s0>−a1|s1>,
    H_e²|s0> = (d0²+a1²)|s0>
                    −a1(d0+d1)|s1>+a1a2|s2>,
    H_e³|s0> = c0|s0>+c1|s1>+c2|s2>+cp|p>,
    c0=d0³+a1²(2d0+d1),
    c1=−a1(d0²+d0d1+d1²+a1²+a2²),
    c2=a1a2(d0+d1+d2),
    cp=−a1a2 kappa.                                      (9)

The third application first reaches p. No downstream diagonal, record interaction, old-source contact or return has acted on that newly reached port component yet. These four head supports are orthogonal. Hence the actual installed spectral sixth moment is exactly

    mu6_eps=c0²+c1²+c2²+(a1a2kappa)²,
    Pi_e V*(H−E_e)^6 V Pi_e=mu6_eps Pi_e.                  (10)

As usual this equality denotes the third-power quadratic form if H is unbounded. In the present bounded one-head lattice it is an ordinary bounded-operator identity. It includes negative detunings and uses the unchanged centers rather than shifting each input energy to a fitted resonance.

A uniform explicit upper envelope is

    mu6_eps <= lambda^6 T(epsilon)
                        +(8/3)jlambda^5(1+epsilon)^3,
    T(epsilon)=[epsilon^3+epsilon(1+epsilon)]²
          +3(1+epsilon)(1+epsilon+epsilon²)²
          +8epsilon²(1+epsilon)².                        (11)

Indeed the absolute coefficients in (9) are bounded respectively by lambda³[epsilon³+epsilon(1+epsilon)], a1*3lambda²(1+epsilon+epsilon²), and 3epsilon lambda a1a2, with a1²a2²<=8lambda^4(1+epsilon)²/9. The port term gives the displayed jlambda^5 contribution. At epsilon=0 this reduces to 3lambda^6+(8/3)jlambda^5, providing a consistency check without replacing the perturbed identity by the nominal one.

## All-input actual concentration and limits

Let I=I_1 union I_3 with the unchanged radius d. The spectral theorem and (10) give

    ||E_H(I_e^c)V Pi_e||<=sqrt(mu6_eps)/d³.

For arbitrary coherent old-energy inputs, triangle inequality and Cauchy–Schwarz on the two orthogonal INPUT projections yield

    ||E_H(I^c)V||<=min{1,sqrt(2mu6_eps)/d³},
    0<=V*E_H(I^c)V<=min{1,2mu6_eps/d^6} I_old.             (12)

One may insert (11) for a uniform parameter envelope. No commutation [H,K]=0 and no orthogonality of the omitted output images are assumed. Record0 is retained coherently and tensoring passive references preserves these operator inequalities. All output coordinates and all outside spectral types, including atoms, are included. This is the ACTUAL installed prepared measure, not the isolated scalar reference density or a seed-return compression.

The local moment requires the physical prefix and domain conditions but does not require Theta_eps<1 or successful emission. It remains true with a compatible finite downstream cap, without transferring infinite-ray inverse estimates to that finite apparatus. In a complete-state synthesis its outside-state allowance must be charged once globally. A source detuning/contact depending on old input or internal direction, an extra edge from the prefix, or nonvacuum internal preparation would require a new moment calculation.

No actual outgoing-row stability, common waveform/time bound, local escape, complete success, useful tolerance, finite receiver performance or native coefficient supply is established here. The scalar robustness theorem is not promoted into such claims. The sufficient inverse inequality (7) and concentration formula (12) are explicit obligations for any later perturbed operating point; none is numerically selected or optimized in this artifact. All actual old aging, W and c_att remain literal in any future output target.

## Exact sources and exposure

Read completely the new scalar robustness source `three_site_source_robustness/PROPOSAL.md`, SHA256 `32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6`, and its root distinct check `three_site_source_robustness_check/REVIEW.md`, `ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad`.

Unchanged scoped premises: nominal attachment `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006` / my review `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`; loaded inverse conventions `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672` / my review `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`; emitter-free wide endpoint `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3` / my review `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5`. Their already-read arguments are reused only for unchanged geometry, background and root scope, not old emitter rates or independent revalidation of my checks.

I authored this new extension and previously checked the nominal inverse/attachment, while root requested the extension and authored nominal ancestors. The scalar robustness author and root check were exposed. This is source-exposed author derivation, not independent certification. A distinct check must reconstruct the complementary determinant margins, ordered full-fiber criterion, positive diagonal realization and all four components of (9), especially the unchanged global scalar and port term. No scientific run, numerical spectrum, parameter sweep, dynamics, external search, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was created.
