# Common source detuning: a recentered scalar packet family

Status: new conditional scalar derivation requiring a distinct check. A common potential on the three source sites can be much larger than lambda while a recentered cubic comparison remains controlled by its size relative to j. The resulting target is an explicitly Delta-dependent packet family, not the fixed zero-detuning target. This does not establish actual processor robustness or a native precision supplier.

## 1. A concrete nonoptimized domain

Fix the original j>0; no recalibration of j is allowed. Write the physical source diagonals as 2j+Delta+r_i, while every uniform-ray diagonal remains 2j. The source sites are 0,1,2 and the ray begins at 3. Keep negative real hoppings with

    a1^2=(lambda^2/3)(1+e1), a2^2=(8lambda^2/3)(1+e2),
    kappa^2=3jlambda(1+e3), |e_i|<=epsilon,
    |r_i|<=epsilon lambda.

For an explicit sufficient domain impose

    0<eta=lambda/j<=1/32, |Delta|/j<=1/4,
    0<=epsilon<=1/200.

These deliberately conservative margins are not optimized. Positive bonds and all scalar/identity residuals are supplied. Put

    y=E-2j-Delta, delta=E-2j=Delta+y,
    R=sqrt(y^2+lambda^2),
    B_eps=20epsilon+16epsilon^2+4epsilon^3,
    beta=3(eta+|Delta|/j), alpha=beta+B_eps.

On this domain beta<=.84375, B_eps<=.1004005 and alpha<=.9441505<1. The estimates become useful only when their resulting error ceilings are small; this entire domain is a validity domain, not a high-fidelity guarantee.

The exact physical self-energy remains m_j(delta), never m_j(y):

    m_j(z)=[z-sqrt(z^2-4j^2)]/(2j^2),
    D_eps,Delta(y)=[(y-r0)(y-r1)-a1^2]
                         [y-r2-kappa^2 m_j(Delta+y)]
                                         -a2^2(y-r0).       (1)

This distinction is the main effect of a source-only common potential. Subtracting Delta from the spectral variable does not move the physical lead band or its Weyl function.

## 2. Recentered real-band cubic margin

First set e_i=r_i=0 at the same Delta, and call that determinant D_Delta. The cubic comparison is D_M(y)=(y+i lambda)^3. On the physical band |delta|<=2j, write s(delta)=sqrt(1-delta^2/(4j^2)). Since

    j m_j(delta+i0)=delta/(2j)-i s(delta),
    |j m_j(delta+i0)+i|^2=2(1-s(delta))<=delta^2/j^2,

we have

    |D_Delta-D_M|
       =3lambda |j m_j(Delta+y)+i| |y^2-lambda^2/3|
       <=3lambda(|Delta|+|y|) R^2/j
       <=beta R^3.                                       (2)

Here lambda/R<=1 and lambda|y|/R<=lambda; no assumption |Delta|<=lambda is used. The bound retains both the load's real part and its changed imaginary part. It is a controlled finite-band-to-cubic comparison, not an exact critical pole assertion.

The residual coefficient/detuning perturbation has exactly the previous product estimate, now in y: the two first factors have nominal norm <=R, the last <=4R because |m_j|=1/j, and their perturbations are respectively <=epsilon R and <=4epsilon R. The bond-square terms give the same remaining costs. Hence

    |D_eps,Delta-D_Delta|<=B_eps R^3,
    |D_eps,Delta-D_M|<=alpha R^3,
    |D_Delta|>=(1-beta)R^3,
    |D_eps,Delta|>=(1-alpha)R^3.                           (3)

This holds throughout the actual lead band including both thresholds. No stability theorem for a multiple pole is invoked. Repeated Markov poles may split while (3) remains valid.

## 3. Normalized exact scalar measure, including exterior mass

On the physical band the exact seed density is

    rho_eps,Delta(delta)=kappa^2 a1^2 a2^2
               s(delta)/[pi j |D_eps,Delta(delta-Delta)|^2]. (4)

To establish its normalization, interior/threshold nonzeros from (3) are insufficient by themselves. For |delta|>=2j, y has the same sign as delta and |y|>=7j/4. The physical exterior root is real with |m_j(delta)|<=1/j. For the unperturbed common-Delta determinant, reverse triangle inequalities yield

    |D_Delta(y)|/|y|^3
      >=1-3lambda/|y|-3lambda^2/|y|^2
      >=1-3/56-3/56^2>.945.

The negative side is treated with absolute values, not a false common-Delta oddness. The first factor y^2-lambda^2/3 is positive and |y-3jlambda m_j|>=|y|-3lambda; subtracting the a2^2 y term gives the stated lower bound (and a discarded positive lambda^3 term).

The residual product estimate also applies outside because |m_j|<=1/j. Its relative cost is at most

    B_eps(1+1/56^2)^(3/2)<.101.

Thus no exterior determinant zero is possible. The scalar finite-rank Jacobi resolvent has regular interior boundary values, bounded thresholds, analytic exterior and the seed 1/z asymptotic. Its measure is precisely (4), with total mass one and no hidden point/singular component. Nonzero Jacobi bonds make the seed cyclic. This conclusion is for this isolated source plus uniform ray only.

## 4. Exact common-Delta packet and residual stability

At the first physical lead site the retarded seed coefficient is

    A_eps,Delta(q)=kappa a1a2 exp(iq)/(j D_eps,Delta(delta-Delta)),
    F_eps,Delta(q)=i(2j sin q) A_eps,Delta(q)/sqrt(2pi),
    delta=-2j cos q, 0<q<pi.

The sign follows from the two internal hoppings, then the negative kappa and m_j=-exp(iq)/j. Its full finite-band norm is one by (4), with |F|^2 dq=rho ddelta. The first-site phase i exp(iq) is not dropped.

Let F_0,Delta be the exact packet at the SAME supplied Delta with e_i=r_i=0. From (3), set

    chi_Delta=B_eps/(1-beta)<1,
    nu=(1+epsilon)^(3/2)-1,
    L_Delta=(nu+chi_Delta)/(1-chi_Delta).

The positive numerator ratio lies between (1-epsilon)^(3/2) and (1+epsilon)^(3/2), so

    |F_eps,Delta/F_0,Delta-1|<=L_Delta,
    ||F_eps,Delta-F_0,Delta||_L2(dq)<=min(2,L_Delta).       (5)

This is a full complex-amplitude comparison to a fixed member of the explicitly supplied Delta-family. It is uniform in time for represented outgoing waves on the unchanged uniform lead by Fourier isometry. Real conjugation gives the same coefficient bound for their incoming partners. It is not a comparison of all three local source amplitudes or the full evolved state.

As in the checked relative-coefficient theorem, restricting both coefficients to a common nonempty hard band and normalizing gives at most min(2,2L_Delta). A common fixed transmission multiplier and its correct Jacobian preserve this relative statement. A downstream response that changes with energy or with Delta must be included explicitly before transferring it to another device; its actual feedback is not supplied by (5).

## 5. Explicit recentered cubic comparison with physical phase

A direct comparison to a rational cubic packet makes the common-mode scale visible. Put C=sqrt(8lambda^5/(3pi)). In physical energy delta define the actual normalized amplitude, extended by zero outside [-2j,2j], as

    f_eps,Delta(delta)=p_phase(delta)
       kappa a1a2 sqrt(s(delta)/(pi j))
                                /D_eps,Delta(delta-Delta),
    p_phase(delta)=i exp(iq(delta)) on the physical band.

This is F_eps,Delta/sqrt(2j sin q), not a changed physical normalization. Define p_phase outside the band by its fixed one-sided endpoint values. This gives a specified unit-modulus function independent of Delta and time. The normalized cubic comparison on the whole energy line is

    g_Delta(delta)=p_phase(delta) C/(delta-Delta+i lambda)^3. (6)

The exterior phase convention only defines a comparison-space extension; no physical lead is asserted there. Both the actual first-site phase and complex cubic phase remain explicit.

Inside the physical band, the numerator ratio to C is n sqrt(s), where n=sqrt((1+e1)(1+e2)(1+e3)). Since |n-1|<=nu and 0<=sqrt(s)<=1,

    |n sqrt(s)-1|<=nu+1-sqrt(s),
    1-sqrt(s(delta))<=delta^2/(4j^2).

Use (3) to divide by the complex denominator. The cubic density centered in y has exact moments int y^2 rho_M=lambda^2/3 and int y^4 rho_M=lambda^4. Its symmetry therefore gives

    [int (Delta+y)^4 rho_M(y)dy]^(1/2)=Delta^2+lambda^2.

Minkowski bounds the central full energy-amplitude error by

    E_band=[nu+alpha+(Delta^2+lambda^2)/(4j^2)]/(1-alpha). (7)

The omitted cubic energy tails have |y|>=b=2j-|Delta|>0, so their norm is at most

    V_Delta=sqrt(16/(15pi)) (lambda/b)^(5/2).

Consequently

    ||f_eps,Delta-g_Delta||_L2(R)<=E_band+V_Delta.          (8)

A genuine physical-band cubic comparator is obtained by restricting (6) to [-2j,2j] and normalizing it. Its retained mass p_M is positive, with 1-p_M<=V_Delta^2. On that band the actual amplitude is already normalized, and the normalization cost for the comparator is 1-sqrt(p_M)<=V_Delta^2. Therefore the physical-band complex packet comparison is

    ||f_eps,Delta-1_band g_Delta/sqrt(p_M)||
                           <=min(2,E_band+V_Delta^2).     (9)

The unitary energy-to-q map gives the identical norm bound for physical lattice Fourier coefficients, preserving the phase in (6). Equations (7)–(9) show errors controlled by |Delta|/j, lambda/j and residual epsilon, rather than |Delta|/lambda. They do not assert small error throughout the entire declared domain or an exact cubic time dependence of the physical lattice.

## 6. Carrier, target dependence and physical realization

A common potential Delta on only the three source sites is Delta P_source, not Delta times the identity on the whole source-plus-ray space. It changes the relative source/lead energy and its load m_j(Delta+y). In the spectral integral one may write

    exp[-it(2j+delta)]=exp[-it(2j+Delta)] exp(-ity),

but the first factor must remain in the comparator. This algebra does not remove Delta from the Hamiltonian or prove equivalence to a globally shifted nominal device. A later old-system comparison must likewise retain its actual K and common physical scalar.

The Delta-family distinction is substantive. For the full-line cubic comparison (6), the shared p_phase cancels in inner products. The absolute overlap of g_Delta and g_0 is

    |<g_0,g_Delta>|=[1+(Delta/(2lambda))^2]^(-5/2).         (10)

Indeed the Fourier transform of 1/(y+i lambda)^3 has density proportional to t^4 exp(-2lambda t) on t>=0; its normalized characteristic function is [2lambda/(2lambda-iDelta)]^5. Thus a shift large relative to lambda changes the prescribed waveform substantially even if Delta/j is small. Equations (8)–(9) quantify the finite-band approximation to these explicit targets. They must not be described as a uniform small error against the Delta=0 target. This is an observation about the specified scalar packets, not a general restriction on memory, computation or capture architectures.

For local positivity, use the ordinary source exchange blocks and occupations

    (2j+Delta+r0-a1)n0,
    (2j+Delta+r1-a1-a2)n1,
    (2j+Delta+r2-a2-kappa)n2,
    (j-kappa)n3.

On the declared domain kappa/j<.31, a2/j<.052 and |r_i|/j<=1/6400, so these are strictly positive even at Delta=-j/4. They give the intended source and ray diagonals without a vacuum scalar. If source blocks are later attached by the existing structured j(n2+n_port)-kappa exchange convention, its residual source occupation is j+Delta+r2-a2>0, and compression preserves the background port j n_port. This establishes local realizability only; it does not establish actual processor matching at shifted energies.

## Remaining obligations and exposure

The original processor's narrow calibrated physical energy windows need not contain a pulse centered at Delta. Even with Delta/j small, Delta may exceed those windows by many orders of magnitude. A full actual device theorem would require its background kernel, closed-channel margins, outgoing phase/W calibration, wrong-window coverage, actual omitted mass, all local/core recovery, incoming/halfline concentration and finite-cut comparison on the shifted physical support. None is inherited by recentering this scalar determinant. The exact downstream phase may be evaluated at shifted energies only where its original physical hypotheses are checked. No useful installed tolerance or runtime is selected here.

This separates two precision questions: residual differences between source diagonals are still controlled on the lambda scale, while the scalar packet family can tolerate a larger common source offset relative to j. Such an offset must be supplied or known to specify its target family and carrier. Native coefficient supply, an unknown-offset fixed target, arbitrary hardware-error tolerance and permanent halt remain unproved.

I authored the nominal scalar source and relative-coefficient stability theorem; root requested this new common-mode question. This is author derivation, not independent checking. Reused exact premises are `three_site_product_source/PROPOSAL.md` a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 / distinct check c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b, and `three_site_source_robustness/PROPOSAL.md` 32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6 / root review ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad. The changed load m_j(Delta+y), exterior no-mass argument, weighted numerator and overlap formula are derived here and need their own distinct check.

No parameter sweep, pole simulation, numerical integration, dynamics, scientific runner, W/Git/PR/checkpoint/prompt/model edit or delegation occurred. Only this proposal was created. No full actual-output or performance claim is made.
