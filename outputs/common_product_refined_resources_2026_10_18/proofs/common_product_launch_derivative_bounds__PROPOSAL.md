# Integrated derivative bounds for the exact launch profile

New bounded author derivation requiring a distinct check. For the exact checked launch profile and a fixed central C2 cutoff, direct integration across its resonance proves normalized bounds G1=O(rho^-1), G2=O(rho^-3), and B_minus=O(rho^-1), where rho=gamma/j. All constants and a sufficient normalization domain are explicit below. These improve a pointwise-denominator derivative estimate without changing the supplied physical Hamiltonian or target. ROOT suggested the cancellation and possible exponents; they were hypotheses reconstructed here, not independent verification.

No runtime or resource exponent is extrapolated. A later resource certificate must substitute these bounds into every actual launch, boundary, finite-tail and microscopic-cell term with its own simultaneous parameter proof.

## 1. Exact cancellation and fixed cutoff contract

Use the exact amplitudes of common_product_endpoint_launch/PROPOSAL.md, SHAfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4, and their use in common_product_finite_seed_router/PROPOSAL.md, SHA3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b. Both were fully read in the preceding coherent tasks and their hashes were refreshed unchanged for this task.

Let j>0, 0<gamma<j, rho=gamma/j, A=2-rho^2 and delta=rho^2. The original source has a_src=jA, d_src=j delta. Its outgoing amplitude simplifies EXACTLY to

    F(k):=g_+(k)
       =-i sqrt(2/pi) gamma sin(k)e^{ik}
                          /[a_src cos(k)-i d_src sin(k)]
       =-i c rho e^{ik}/[A cot(k)-i delta],
    c=sqrt(2/pi), 0<k<pi.                         (1)

To verify the phase, the original numerator is d_src sin(k)-i a_src cos(k)=-i[a_src cos(k)+i d_src sin(k)]; multiplying by the positive source square-root density cancels its quadratic denominator against that conjugate factor. Thus (1) retains the original complex phase, not merely the original modulus. The incoming amplitude is g_-=conjugate(F), since the source square-root density is real. The common overall j scale cancels from F.

Fix 0<sigma<sigma'<pi/2, independent of rho. Choose one real chi in C_c^2((0,pi)), with 0<=chi<=1, chi=1 on |k-pi/2|<=sigma, and support contained in |k-pi/2|<sigma'. Set

    K1=||chi'||_infinity, K2=||chi''||_infinity,
    L=tan(sigma'), S=sec^2(sigma'),
    p=||chi F||_2^2, g=chi F/sqrt(p),
    G_r=||g^(r)||_1, r=0,1,2.                    (2)

The constants K1,K2,sigma,sigma' are fixed. No narrowing cutoff depending on rho is covered by a claimed rho-independent constant. The finite-router application may retain its stronger sigma'<pi/3 restriction; these derivative calculations themselves need only sigma'<pi/2.

The checked reference has ||F||_2=1 and gives

    p>=1-4rho^2/[pi A^2 tan(sigma)], p<=1.        (3)

Indeed chi=1 throughout the central band and the exact exterior spectral probability has the displayed upper bound. A convenient sufficient uniform domain is

    0<rho<=rho_*:=min{1/2,sqrt[pi tan(sigma)/8]}.

Then A>=7/4>1, the subtracted quantity in (3) is <=1/2, and p>=1/2. The positive sqrt(p) fixes exactly the source's target normalization. These estimates do not replace the true p by a fitted number.

## 2. Resonance integrals

On the cutoff interval put x=cot(k), h(k)=1/(Ax-i delta). Then |x|<=L, dk has absolute value dx/(1+x^2), and

    h'=A(1+x^2)/(Ax-i delta)^2,
    h''=-2Ax(1+x^2)/(Ax-i delta)^2
                       +2A^2(1+x^2)^2/(Ax-i delta)^3. (4)

All norms in this section are integrals over |k-pi/2|<=sigma', which also bound the corresponding integrals over the actual cutoff support. The following explicit envelopes follow:

    ||h||_1 <= H0=(2/A)asinh(AL/delta),
    ||h'||_1 = H1=(2/delta)arctan(AL/delta)<=pi/delta,
    ||h''||_1 <= H2=(2/A)log[1+(AL/delta)^2]
                                      +4A S/delta^2. (5)

For H0, discard only the factor 1/(1+x^2)<=1 and integrate (A^2x^2+delta^2)^-1/2 on [-L,L]. For H1 the Jacobian cancels the factor 1+x^2 exactly, leaving A integral dx/(A^2x^2+delta^2), which evaluates to the stated arctangent. This cancellation is why a uniform pointwise denominator estimate is unnecessarily costly.

For the first term of h'', the integrated absolute value is

    2A integral_(-L)^L |x|/(A^2x^2+delta^2) dx
       =(2/A)log[1+(AL/delta)^2].

For the second term, use 1+x^2<=S after its Jacobian cancellation:

    2A^2 integral_(-L)^L (1+x^2)/(A^2x^2+delta^2)^(3/2) dx
       <=4A^2 S L/[delta^2 sqrt(A^2L^2+delta^2)]
       <=4A S/delta^2.

The triangle in H2 need not be sharp; every term in the differentiated denominator is present. These are ordinary finite analytic integrals, not a linewidth substitution or a numerical fit.

## 3. Normalized derivative bounds

Since F=-ic rho e^{ik}h, multiplication by e^{ik} and the product rule give

    ||chi F||_1 <= c rho H0,
    ||(chi F)'||_1 <= c rho[(K1+1)H0+H1],
    ||(chi F)''||_1 <= c rho[(K2+2K1+1)H0
                                  +(2K1+2)H1+H2]. (6)

For example F''=-ic rho e^{ik}(-h+2ih'+h''), so both phase derivatives have been retained. Terms involving chi' and chi'' are charged by their supplied fixed supremum norms, not suppressed because the cutoff is constant near resonance.

Dividing (6) by the SAME positive sqrt(p) yields the precise useful bounds

    G1 <= (c rho/sqrt(p))[(K1+1)H0+H1],
    G2 <= (c rho/sqrt(p))[(K2+2K1+1)H0
                                      +(2K1+2)H1+H2]. (7)

For G0 it is often better to use normalization and support length directly:

    G0<=sqrt(2sigma'),

or the smaller of that value and c rho H0/sqrt(p). All formulas preserve the actual p; (3) supplies a fully explicit denominator lower bound when needed.

As rho tends to zero with the cutoff fixed, H0=O(log(1/rho)), H1=O(rho^-2), and H2=O(rho^-4). Since p>=1/2 in the stated domain, (7) proves

    G1=O(rho^-1), G2=O(rho^-3).                  (8)

These are upper bounds, not asserted asymptotic equalities or optimal constants.

For readers needing pure powers with no hidden big-O constants, use H0<=2L/delta, H1<=pi/delta, A<=2, and log(1+y^2)<=2y for y>=0. Hence

    H2<=4L/delta+8S/delta^2.

Because rho<=rho_*<=1/2, delta<=1 and p>=1/2, one obtains the explicit uniform certificate

    G1 <= C1/rho,
    C1=(2/sqrt(pi))[2L(K1+1)+pi],

    G2 <= C2/rho^3,
    C2=(2/sqrt(pi))[2L(K2+2K1+1)
                                +(2K1+2)pi+4L+8S]. (9)

The H0 bound used to simplify constants is deliberately loose. It does not spoil either exponent because only the higher differentiated resonance controls the dominant allowed power. Equation (7) is available when smaller constants or logarithmic dependence matter.

## 4. Incoming launch coefficient B_minus

The finite composition uses vmin=2j cos(sigma') and

    B_minus=||(chi g_-)'||_1+(2j/vmin)||chi g_-||_1.

Since chi is real and g_-=conjugate(F), conjugation preserves all L1 derivative norms. Therefore the exact relation is

    B_minus=sqrt(p)[G1+sec(sigma')G0].            (10)

There is no extra reciprocal sqrt(p), separate incoming spectral normalization or phase derivative cost. Directly from (6) and Cauchy-Schwarz,

    B_minus <= c rho[(K1+1)H0+H1]
                              +sec(sigma')sqrt(2sigma'). (11)

Here ||chi F||_2=sqrt(p)<=1 was used only for the second term. A simple explicit uniform bound on the same rho-domain is

    B_minus<=C_minus/rho,
    C_minus=c[2L(K1+1)+pi]+sec(sigma')sqrt(2sigma'). (12)

Equations (7),(9),(11),(12) can be substituted for precisely the G1,G2 and B_minus coefficients in the pinned launch/composition estimates. The exact target amplitude F, its phase, p, the cutoff and all physical interactions are unchanged. This is improved analytical bookkeeping of the actual profile, not a different source or a new preparation assumption.

## 5. Use and limits

The checked scalar source measure and phase formula are adopted at their stated scopes. The cancellation, resonance-integrated derivative estimates, pure-power constants and B_minus relation above are new author calculations requiring a distinct check. Particularly load-bearing checks are: the complex denominator sign in (1); the Jacobian cancellation in H1; both h'' terms and their integrals; positive cutoff normalization; every cutoff/phase product-rule term; and use of the raw incoming amplitude in B_minus.

The old crude pointwise estimates remain valid upper bounds if independently established; these tighter estimates do not falsify them. No claim is made that the complete device's runtime or size automatically improves by a particular power. Such a conclusion would require recomputing the simultaneous choices of rho, early time, distance, observation window, microscopic detuning ratios and fixed load cap, while keeping all tails and full physical output errors. No unproved scaling from another author's file is imported and that file is not edited.

The two pinned primary sources were previously fully read and their SHA-256 values were rechecked unchanged in this task. Their recorded independent checks qualify those premises, not the new estimates here. ROOT suggested the cancellation and scaling question. This author reconstructed the exact amplitudes and every displayed integral analytically after that exposure; the result is not blind or independent verification.

Only common_product_launch_derivative_bounds/PROPOSAL.md was created. No scientific executable, numerical integration, symbolic solver, sweep, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation occurred. No retained status, runtime certificate or independent acceptance is assigned.
