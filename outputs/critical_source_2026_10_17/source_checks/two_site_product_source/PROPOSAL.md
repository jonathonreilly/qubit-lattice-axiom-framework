# Two-site product source: exact lattice measure, cubic band tails and two-site escape

Status: new source-exposed analytical proposal requiring a distinct check. The proposed critical relation kappa²/j=2lambda yields the squared-Lorentzian reference density and return suggested by root. The actual lattice measure is different but has an explicit controlled comparison. On0<lambda/j<=1/8 it is entirely absolutely continuous, and its product-seed mass outside a centered band obeys a cubic linewidth/bandwidth bound without an additive comparison floor. Escape estimates below include BOTH source sites. No interacting-old-core or attached-device theorem is inferred.

## Exposure and model

Root suggested two endpoint couplings and the critical comparison after reading the primary paper by Apollaro, Banchi, Cuccoli, Vaia and Verrucchi, [99%-fidelity ballistic quantum-state transfer through long uniform channels](https://arxiv.org/pdf/1203.5516). I verified its identity and inspected its two-boundary-coupling/mode-density discussion, including Eqs.(22)--(23). Its finite mirror-symmetric transfer setting is not the halfline model below; no paper fidelity or optimized coefficient is transferred. This is original derivation from the displayed Jacobi matrix, with the candidate mechanism exposed, not a novelty claim or independent review.

Let source sites be0,1 and uniform lead sites2,3,... . On the seeded one-head sector set

    h=-lambda(|0><1|+|1><0|)
      -kappa(|1><2|+|2><1|)
      -j sum_(n>=2)(|n><n+1|+|n+1><n|),
    H=E_c I+h, E_c=2j,
    eta=lambda/j, 0<eta<=1/8,
    kappa=sqrt(2j lambda), gamma=kappa²/j=2lambda.     (1)

The initial state is the product head seed|0>, with all other heads blank. There is no supplied extended pulse. The coefficients and real time-independent Hamiltonian remain supplied nominal data. The exact equality in(1) is a coefficient-correlation premise, not a robustness theorem.

Use fullspace positive exchanges Q_01(lambda), Q_12(kappa), Q_n,n+1(j), and occupations

    (2j-lambda)n0,
    (2j-lambda-kappa)n1,
    (j-kappa)n2.

All later occupations vanish. Since kappa/j<=1/2 and lambda/j<=1/8, these are nonnegative. They give diagonal2j at every head. The construction is a straight NN path with ordinary real one-/two-qubit positive blocks. The carrier exp(-i2jt) is retained, not removed from a physical vector comparison. No scientific numerical run, spectral quadrature, sweep, delegation, Git/canonical/checkpoint/prompt or model edit occurred. Only this proposal, source browsing and identity bookkeeping were performed.

## 1. Exact resolvent and density

For Im z>0 use the square-root branch sqrt(z²-4j²) asymptotic to z, with the usual cut[-2j,2j]. The outgoing lead boundary resolvent is

    m_j(z)=[z-sqrt(z²-4j²)]/(2j²).

Eliminating the lead gives the exact source inverse

    R_src(z)=[[z,lambda],[lambda,z-kappa² m_j(z)]]^-1,
    D(z)=z[z-kappa²m_j(z)]-lambda²,
    m0(z)=[z-kappa²m_j(z)]/D(z),
    R10(z)=-lambda/D(z), R11(z)=z/D(z).             (2)

These signs follow from the positive off-diagonal entries in z-h. For real delta in(-2j,2j), put s=sqrt(1-delta²/(4j²)). At the critical relation(1),

    kappa²m_j(delta+i0)=eta delta-i2lambda s,
    D_+(delta)=(1-eta)delta²-lambda²+i2lambda delta s,
    |D_+|²=(1-2eta)delta^4
                  +2(1+eta)lambda²delta²+lambda^4. (3)

The imaginary part in the numerator of m0 cancels against part of the denominator product, leaving the exact product-seed density

    rho0(delta)=2lambda³ s /
       {pi[(1-2eta)delta^4
                       +2(1+eta)lambda²delta²+lambda^4]}. (4)

It is zero outside the band once absence of atoms is established below. Equation(4), not the reference density, is the installed halfline spectral measure.

## 2. No hidden atoms or singular mass on this domain

For x>=2j, 0<m_j(x)<=1/j. Therefore

    D(x)>=x(x-2lambda)-lambda²
          >=j²(4-4eta-eta²)>0.

The last quadratic is increasing in x on this range. For x<=-2j, oddness of the exterior branch gives D(-x)=D(x)>0. At both thresholds the same strictly positive expression applies. Hence there are no exterior poles or threshold atoms.

Inside the band the imaginary part of D is2lambda delta s. It vanishes only at delta=0, where its real part is-lambda², or at the already regular thresholds. Thus every interior boundary value is regular. The explicit algebraic resolvent, its jump and1/z asymptotic imply the Cauchy representation by(4), with total mass one. More explicitly, interior regularity excludes interior singular measure, analytic exterior continuation excludes exterior measure, and bounded threshold limits exclude endpoint atoms. Only those two endpoints remain after the open intervals are covered. No residual singular measure is left.

Every hopping is nonzero, so successive powers of h applied to|0> generate all finite basis vectors. The seed is cyclic; no additional bound subspace is hidden elsewhere in this scalar halfline. A finite capped chain instead has discrete spectrum and recurrence; that case is covered only by a finite-time comparison below.

The entire two-source-site spectral matrix is also explicit. Because h|0>=-lambda|1>,

    dMu_src(delta)=rho0(delta)
       [[1,-delta/lambda],[-delta/lambda,delta²/lambda²]] ddelta. (5)

In particular the cross measure, not just m0, will control the second source site's amplitude. The moment identity integral delta² rho0=lambda² is consistent with the normalization of|1>.

## 3. Critical Markov reference, not actual lattice dynamics

Replacing the lead selfenergy by its center value-i gamma gives the rational reference

    m0,M(z)=(z+i2lambda)/(z+i lambda)^2

on the upper branch. Its positive normalized boundary density on the ENTIRE real line is

    rhoM(delta)=2lambda³/[pi(delta²+lambda²)^2].       (6)

A residue calculation, or differentiating the Cauchy Fourier transform with respect to lambda, gives

    A0,M(t)=(1+lambda|t|)exp(-lambda|t|).

Thus root's conjectured formula is correct for this reference. It is not an exact exponential law for the finite-band lattice. Define the corresponding cross Fourier comparison by -(delta/lambda)rhoM; for t>=0 its amplitude is

    A1,M(t)=i lambda t exp(-lambda t).               (7)

The sign follows either from(5) or from A1=-(i/lambda)A0': its small-time derivative is+i lambda, as the physical negative hopping requires.

## 4. Controlled density and cross-measure comparisons

Let P(delta)=(delta²+lambda²)^2 and D2 be the polynomial in(3). Then

    D2-P=2eta delta²(lambda²-delta²),
    D2>=(1-2eta)P, |D2-P|<=2eta P.

On the physical band, subtraction therefore gives

    |rho0-rhoM|<=rhoM [2eta+(1-s)]/(1-2eta).        (8)

The reference moments are integral rhoM=1, integral delta²rhoM=lambda² and integral |delta|rhoM/lambda=2/pi. Using1-s<=delta²/(4j²) and paying the reference tails outside2j yields the explicit L1 bound

    E0:=[2eta+eta²/4]/(1-2eta)+eta³/(6pi),
    integral_R |rho0-rhoM| <=E0<3eta.              (9)

The outside term follows from rhoM<=2lambda³/(pi delta^4). This is a uniform Fourier error bound, not a relative density approximation at a band edge.

The second source amplitude requires a WEIGHTED comparison. Using the same bound(8), with its own finite-band third moment and outside tail, gives

    E1:= [4eta/pi+eta² log(1+4/eta²)/(2pi)]/(1-2eta)
                       +2eta²/[pi(4+eta²)],
    integral_R |delta|/lambda |rho0-rhoM| <=E1<2eta. (10)

For completeness, the square-root correction comes from

    (eta²/pi) integral_0^(2j) delta³/(delta²+lambda²)^2 ddelta
      =eta²/(2pi)[log(1+4/eta²)+eta²/(4+eta²)-1]
      <=eta² log(1+4/eta²)/(2pi).

The displayed outside weighted tail is its exact reference integral. To check the relaxed2eta ceiling without numerical quadrature, eta log(1+4/eta²) is increasing on(0,1/8], and at1/8 is<6/8. With1-2eta>=3/4 and pi>3 the resulting coefficient is at most(4+.375)/(3*.75)+1/(16*3)<2. Similarly(9) is below3eta throughout the domain. These comparisons keep both source amplitudes; the seed-return error alone would be insufficient.

## 5. Exact cubic outside mass, without an additive eta floor

The direct inequality from(4) is stronger for band tails than integrating(9): rho0<=rhoM/(1-2eta) on its band. Consequently, for0<Delta<=2j,

    Pr_seed(|delta|>Delta)
       <=min{1,4lambda³/[3pi(1-2eta)Delta³]},
    ||E_h(R outside[-Delta,Delta])|0>||
       <=min{1,sqrt[4/(3pi(1-2eta))](lambda/Delta)^(3/2)}. (11)

There is no additional3eta mass floor in(11). It counts the entire actual spectral complement because section2 excluded hidden spectral types. At Delta=2j the true outside mass is zero; the displayed upper bound is merely conservative.

A linewidth scale lambda therefore produces a cubic mass tail, or a three-halves power omitted STATE amplitude. The single-site Cauchy reference instead has leading outside mass proportional to linewidth/Delta. This is a genuine isolated product-source improvement of the spectral-concentration tradeoff. For instance a sufficient omitted amplitude epsilon_sp is obtained by requiring

    lambda/Delta <=[3pi(1-2eta)/4]^(1/3) epsilon_sp^(2/3).

It is not a full apparatus resource comparison. The source width, downstream processor/load, common waveform and residence time must still be matched. No claim that two sites always outperform every other source follows.

## 6. Escape from BOTH source sites

Let Psrc=|0><0|+|1><1| and A_n(t)=<n|exp(-ith)|0>. Equations(9)--(10) give, with x=lambda t>=0,

    ||Psrc exp(-ith)|0>||
      <=exp(-x)sqrt((1+x)^2+x²)+sqrt(E0²+E1²)
      < exp(-x)sqrt(1+2x+2x²)+sqrt(13)eta.          (12)

This is a controlled two-coordinate norm estimate. Neither the intermediary's coherent occupation nor its phase is ignored. For desired escape allowance0<zeta<1, a simple sufficient regime is

    sqrt(13)eta<=zeta/2,
    lambda t>=2log(8/zeta).

Indeed sqrt(1+2x+2x²)<=sqrt2(x+1)<4exp(x/2), so(12) is at most zeta. The first condition is a limitation of this uniform comparison error, not a claim of nonzero late residual mass.

There is also a genuinely decaying bound for every fixed admissible eta, independent of that comparison floor. In(4) the numerator is decreasing for delta>0 and the positive denominator is increasing. The density is even, zero at thresholds and has integrable derivative; hence its total variation is2rho0(0)=4/(pi lambda). Integration by parts gives

    |A0(t)|<=4/(pi lambda t).

For f(delta)=-(delta/lambda)rho0(delta), endpoint values vanish and

    integral |f'| <=[integral rho0+integral |delta||rho0'|]/lambda
                   =2/lambda.

The last equality follows by integration by parts and even monotonicity. Thus

    |A1(t)|<=2/(lambda t),
    ||Psrc exp(-ith)|0>||
       <=sqrt(16/pi²+4)/(lambda t)<2.4/(lambda t). (13)

Take the minimum of1, the nonrelaxed right side of(12), and(13). It tends to zero for every fixed positive lambda. This proves source escape in the isolated model, not arrival at any chosen far output site or a complete W operation. Restoring E_c only multiplies amplitudes by exp(-i2jt).

## 7. Finite heads, internal inputs and exact remaining obligations

Retain M>=1 uniform lead sites2,...,M+1, plus the two source sites. Add the exact cap j n_(M+1). If M=1 it combines with the first-lead occupation j-kappa; this gives final diagonal2j despite no retained ordinary j edge. The finite model has M+2 head qubits, M+1 exchange bonds and, with the cap separately listed, four occupation blocks (some share a site for M=1). It is fullspace positive; the finite one-head restriction is exact compression.

Here ||h||<=2j: source row sums are lambda and lambda+kappa, first-lead sum is kappa+j, and later sums are2j. The first omitted site is M+2 hops from seed0. Therefore the same power-series locality argument gives finite/infinite seed evolution difference at most

    2F_(M+2)(2j|t|), F_d(u)=sum_(k=d)^infinity u^k/k!.

It can be made small on any specified finite horizon. No economical M, all-time finite escape or retained receiver advantage is asserted. Finite reflections and recurrence remain.

If an independently supplied internal generator has an invariant preparation range on which it acts as literal K, the scalar construction tensors that exact old evolution and arbitrary passive references. It does not implement W by itself. An actual attachment to the calibrated interacting processor replaces m_j by an operator-valued downstream surface resolvent, generally with old-dependent returns. Equations(2)--(13) then cannot be reused by calling that surface uniform. Required new work is its exact full-input selfenergy, local regularity, spectral concentration, complete outgoing coefficient/common phase, source/core escape and finite transfer, retaining all closed and wrong-window channels. The product endpoint seed is supplied but no extended input packet is assumed.

The useful result is the exact finite-band source law and its proved concentration/escape interface. The critical Markov reference is controlled, not promoted to the actual Hamiltonian. No old runtime, paper fidelity, native preparation/calibration supply, capture/holding/record theorem, irreversible halt or primary mission closure is inferred. A distinct analytical check is required, particularly for the denominator polynomial, weighted cross-measure comparison and both-source-site escape.
