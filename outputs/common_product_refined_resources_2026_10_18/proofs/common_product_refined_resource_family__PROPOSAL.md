# A refined explicit accuracy/resource family for the finite seeded router

New authored combined certificate requiring a distinct check. For 0<epsilon<=1 and supplied incident-norm cap Lambda>0, the exact finite positive seeded-router family below has uniform complete-output isometry error below 179epsilon/256<epsilon on the same relative-width observation window as the checked baseline. Its qubit count and dimensionless duration are Theta(epsilon^-4), its physical duration is Theta(Lambda^-1 epsilon^-14), and its smallest supplied positive scalar coefficient is Theta(Lambda epsilon^11).

These are sufficient exponents of the displayed family, not optimal exponents, lower bounds, practical performance, coefficient tolerances or a claim about actual error. The improved integral derivative bounds and second-order microscopic comparison each now have distinct checks at the pinned revisions below. Their combination, all allocations and exponents here are new author work, not already checked by those reports. ROOT supplied the candidate choices and expected exponents; the inequalities below reconstruct them rather than treating that suggestion as evidence.

## 1. Fixed device, cutoff and metric

Use precisely the finite positive Hamiltonian and literal endpoint seed of composition3a195efc, with its equal-diagonal weak emitter blocks and microscopic six-qubit central program cell. No interaction or target is changed. The output is the fixed encoding of beta_F(t) tensor Cxi, with

    C=P0 tensor X+P1 tensor I,

both emitters and mediator vacant in the target, unchanged legal program contents, and physical scalar exp(-i2bt). The error is induced isometry norm on all encoded program/path inputs and arbitrary passive references, retaining every actual output. The uniform-window theorem1ea1943e supplies the common moving normalized packet and mixed-endpoint error aggregation.

Use the checked baseline's fixed cutoff, restated to fix every derivative constant. With x=|k-pi/2|, h=pi/12 and Q(s)=1-10s^3+15s^4-6s^5, set

    chi=1 for x<=pi/24,
    chi=Q((x-pi/24)/h) for pi/24<x<pi/8,
    chi=0 for x>=pi/8.

Then chi is real C_c^2, 0<=chi<=1, and is supported strictly inside the conservative band sigma'=pi/6. Set sigma=pi/24. Its plateau and endpoint derivatives match, and

    K1=||chi'||_infinity<7.5,
    K2=||chi''||_infinity<240,
    vmin/j=sqrt(3)=cmin, vmax/j=2=cmax.

The raw exact launch amplitude is unchanged:

    F(k)=-i sqrt(2/pi)rho e^{ik}/[(2-rho^2)cot(k)-i rho^2],
    rho=gamma/j, g_+=F, g_-=conjugate(F),
    p=||chi F||_2^2, g=chi F/sqrt(p).

The positive sqrt(p) fixes the source phase. For 0<rho<=1/8, the checked tail bound gives P<=11rho^2 and p>=1-P>1/2. There is no surrogate profile or fitted phase.

## 2. Improved numerical derivative bounds for this cutoff

Apply the checked integrated derivative result378086fd. Its constants use L=tan(sigma')=1/sqrt(3)<1 and S=sec^2(sigma')=4/3<2. Its sufficient rho-domain contains 0<rho<=1/8: pi tan(pi/24)>=pi^2/24>3/8, so sqrt[pi tan(pi/24)/8]>1/8. The eventual choice rho=epsilon/256 lies well inside it.

The explicit source constants are

    C1=(2/sqrt(pi))[2L(K1+1)+pi],
    C2=(2/sqrt(pi))[2L(K2+2K1+1)+(2K1+2)pi+4L+8S].

Using pi<4, 2/sqrt(pi)<2 and the displayed K bounds gives C1<42<100 and C2<1200<2000. Cauchy-Schwarz gives G0=||g||_1<=sqrt(pi/3)<2. Consequently

    G0<2, G1<=100rho^-1, G2<=2000rho^-3.          (1)

The raw incoming coefficient is exactly B_minus=sqrt(p)[G1+(2/cmin)G0]. Since p<=1 and 2/cmin<2,

    B_minus<=100rho^-1+4<=200rho^-1.              (2)

These constants come from integrating the exact resonance and retain all cutoff and phase derivatives. They replace only the looser rho^-3/rho^-5 derivative ceilings in the baseline, not its Hamiltonian, normalization or physical scope.

## 3. Explicit geometric and time choices

For 0<epsilon<=1 set

    rho=epsilon/256,
    u0=10^12 rho^-2 epsilon^-2,
    ell=ceil(100u0), M=ell+1,
    uminus=3ell/4, uplus=7ell/8,
    t0=u0/j, tminus=uminus/j, tplus=uplus/j.        (3)

All times here are from the original emitter seed. There is no switching at t0 or either observation endpoint. Since sqrt(3)>5/3,

    tminus vmin-ell>ell/4,
    2ell-tplus vmax=ell/4,
    2ell+2-tplus vmax=ell/4+2,
    A_early=ell+1-2u0>=ell/2,
    u0/A_early<=1/50.

Also t0vmin>2, tminus>t0, tplus vmax<2ell-2 and ell>=100u0. Thus every strict geometry and window hypothesis holds. M is much greater than the minimum required by the finite construction.

For the source tail function, the elementary inequality

    sqrt(A^-2+A^-1)/sqrt(2pi)<=A^-1/2, A>=1,

gives T(t,A)<=[G1+(2jt/A)G0]/sqrt(A). Substitution of (1) yields

    d_right<=104rho^-1/sqrt(u0),
    sqrt(2)T(t0,A_early)<=300rho^-1/sqrt(ell),
    d_L<=230rho^-1/sqrt(ell),
    n_O<=230rho^-1/sqrt(ell).                    (4)

For the late tail, uminus/(tminus vmin-ell)<3; for the outgoing tail, uplus/(2ell+2-tplus vmax)<7/2. These give the intermediate constants224 and228, respectively, rounded up to230. The right early gap is at least u0. No monotonicity of the normalized quotient is assumed.

Because sqrt(u0)=10^6rho^-1/epsilon and sqrt(ell)>=10sqrt(u0), d_L<=230epsilon/10^7<1/2. Therefore the window's normalized outgoing allowance satisfies

    d_O=n_O/(1-d_L)<=2n_O<=460epsilon/10^7<1.      (5)

This verifies the finite target normalization for every time in the interval.

## 4. All nine ideal-error allocations

The checked launch bound gives

    R0<=rho^-2/u0=epsilon^2/10^12,
    L0<=200rho^-1/sqrt(u0),
    2delta_launch<=2R0+2L0+4sqrt(P).

The spectral term satisfies 4sqrt(P)<=4sqrt(11)epsilon/256<epsilon/16. The other two launch terms obey

    2R0<=2epsilon^2/10^12<epsilon/16,
    2L0<=400epsilon/10^6<epsilon/16.

In particular delta_launch<3epsilon/32<1, proving launch normalization before invoking it. The remaining square-root terms have the explicit ceilings

    2d_right<=208epsilon/10^6,
    sqrt(2)T_early<=300epsilon/10^7,
    2d_L<=460epsilon/10^7,
    2d_O<=920epsilon/10^7.                        (6)

Each is strictly below epsilon/16.

For the early factorial term let d=ell+2, the exact first possibly unequal Hamiltonian power. Consecutive Taylor terms have ratio <=1/25 since d>=100u0. With d!>=(d/e)^d and e<3,

    e_early<=2(25/24)(4eu0/d)^d
             <3*8^-d<=3/d<=3/(100u0)<epsilon/16. (7)

No asymptotic factorial approximation or numerical evaluation is used.

For the fixed-diagonal boundary comparison, (1) and cmin>1 imply

    A_i<=4000rho^-3,
    A_o(tplus)<=5000rho^-3.

In detail, A_i coefficients are at most12 on G1 and52 on G0, giving 2000+1200+104<4000 after factoring rho^-3. At the right endpoint uplus/qo(tplus)=7/2, A_o coefficients are21 on G1 and154 on G0, giving 2000+2100+308<5000. The source prefactor sqrt(3)d_hop/sqrt(2pi) is <j because d_hop<=sqrt(2)j and pi>3. Dropping only favorable terminal subtractions from its closed integral bound gives

    e_boundary<=8000rho^-3/u0+10000rho^-3/ell
                 <=8100rho^-3/u0
                 =(8100*256/10^12)epsilon
                 <epsilon/16.                   (8)

Here qi(t0)>=u0/2, qo(tplus)=ell/4, cmin>1 and cmax=2 supply the denominators. The crucial inverse rho left after the improved u0 choice has been paid using the exact rho=epsilon/256; it is not silently dropped.

Thus each of these nine NONNEGATIVE contributions is below epsilon/16:

    e_early, 2R0, 2L0, 4sqrt(P), 2d_right,
    sqrt(2)T_early, e_boundary, 2d_L, 2d_O.

Their sum bounds the complete ideal window allowance by 9epsilon/16. This includes source residual, every projection/normalization cost and the boundary evolution comparison. The actual output is not projected or normalized.

## 5. Second-order physical-cell allowance and exact load scale

Put s=uplus and choose independently specified ratios

    eta^2=epsilon/[256(1+s)], eta>0,
    zeta=epsilon/[64(1+s)]=4eta^2,
    D1=Lambda/2, D0=zeta D1, b=eta D0,
    j=b^2/D0=Lambda eta^2 zeta/2,
    a0=2j, gamma=rho j.                          (9)

Then eta<=1/16<1/8 and zeta<=1/64<1/2, so D1>D0>2b and all checked local incident-cap conditions hold. The actual cell and emitter positive blocks remain those of the composition.

The checked second-order comparisona322e368, applied for the entire interval through tplus, gives the sufficient envelope

    e_cell_second<=min{2,4eta+11s eta^2+2s zeta}.  (10)

Its non-isometric polynomial comparison map is only a proof device; the prepared and final maps are still literal isometries. No additional physical preparation or normalization is introduced.

The initially nonaccumulating term is explicitly paid. Since s>=87.5u0 and u0>=10^12epsilon^-2, one has 1+s>16/epsilon throughout 0<epsilon<=1. Therefore

    4eta=sqrt(epsilon)/[4sqrt(1+s)]<epsilon/16.

The two accumulated terms satisfy

    11s eta^2<11epsilon/256,
    2s zeta<epsilon/32.

Combining them gives e_cell_second<35epsilon/256. In particular it is not enough merely to choose eta proportional to sqrt(epsilon/s); the endpoint requirement has also been verified. With the ideal allowance,

    E_window_refined <9epsilon/16+35epsilon/256
                      =179epsilon/256<epsilon.   (11)

This is uniform induced isometry error over the entire interval for arbitrary encoded program/path/reference input, with every output retained and the common phase exp(-i2bt). The corresponding unhalved channel bound is <2epsilon. If the requested metric is channel error epsilon, use accuracy argument epsilon/2 throughout; this changes constants but none of the exponents below.

For clarity the local load check can also be made directly. The combined-block incident sums are D1+2b=Lambda(1/2+eta zeta), central endpoint3b+4j=Lambda zeta(3eta+4eta^2)/2, program loads2j and D1-2b, lead interior4j, emitter-adjacent5j, and emitter3j. With eta<=1/16 and zeta<=1/64 every displayed sum is strictly below Lambda. The norm convention is the same as the checked composition and baseline: one combined mediator/program block and one combined B block at each emitter. No bound on a local sum is confused with a bound on each scalar coefficient or the whole many-qubit Hamiltonian.

## 6. Exact prescriptions and comparison on the same metric

Let s=7ell/8 and retain the ceiling in ell. Equations (3),(9) yield

    u0=10^12*256^2*epsilon^-4,
    ell=ceil(100u0),
    eta=sqrt(epsilon)/[16sqrt(1+s)],
    zeta=epsilon/[64(1+s)],
    D0=Lambda epsilon/[128(1+s)],
    b=Lambda epsilon^(3/2)/[2048(1+s)^(3/2)],
    j=Lambda epsilon^2/[32768(1+s)^2],
    gamma=Lambda epsilon^3/[8388608(1+s)^2],
    tplus=32768 s(1+s)^2/(Lambda epsilon^2),
    tminus=(6/7)tplus.                           (12)

These large constants are part of the sufficient certificate, not concealed by asymptotic notation. The device has 6+2M=8+2ell qubits and 7+2M=9+2ell combined positive blocks. The relative window width is exactly1/6 in both families. At fixed Lambda, as epsilon decreases to zero:

| Quantity | Refined family | Checked baseline0e21dae8 |
|---|---|---|
| Qubits and positive blocks | Theta(epsilon^-4) | Theta(epsilon^-8) |
| Dimensionless time endpoints j tminus, j tplus | Theta(epsilon^-4) | Theta(epsilon^-8) |
| eta | Theta(epsilon^(5/2)) | Theta(epsilon^9) |
| zeta | Theta(epsilon^5) | Theta(epsilon^9) |
| D0 | Theta(Lambda epsilon^5) | Theta(Lambda epsilon^9) |
| b | Theta(Lambda epsilon^(15/2)) | Theta(Lambda epsilon^18) |
| j and a0 | Theta(Lambda epsilon^10) | Theta(Lambda epsilon^27) |
| gamma | Theta(Lambda epsilon^11) | Theta(Lambda epsilon^28) |
| Physical time endpoints | Theta(Lambda^-1 epsilon^-14) | Theta(Lambda^-1 epsilon^-35) |

The comparison uses the same accuracy argument as an induced complete-output isometry ceiling, the same relative-width window, the same physical block architecture and incident-load convention, and the same supplied-input premises. It compares two sufficient parameter families. It does not prove optimal exponents, a lower bound on apparatus requirements, a fixed-device speedup, smaller actual error, or practical physical performance.

The smallest nonzero supplied positive scalar coefficient in the displayed block decomposition is gamma. Indeed rho<=1/256 implies gamma<j, j-gamma>gamma and 2j-gamma>gamma; a0=2j>gamma; b/j=1/eta>1; and (D0-2b)/j=(1-2eta)/eta^2>1, with D1-2b larger still. This statement is about exact coefficient MAGNITUDES, including the subterms defining combined blocks. It is not an allowed fabrication error, a precision tolerance, a minimal eigenvalue, or a cost of producing exact correlations. No coefficient-tolerance theorem is imported.

## 7. Sources, checks and limits

New complete source/report reads and hash verification for this task:

* Baseline common_product_finite_seed_scaling/PROPOSAL.md — 0e21dae83a8449f03276b4099ea6a6ae23e08afa5b4a1297122e67e7b9095f6e; distinct check common_product_finite_seed_scaling_check/REVIEW.md — 751c97d5cabdf08f12f1c1852f0fbcf2bfc5fdcfe3179b6cc033ad23f36c91e5.
* Second-order common_product_second_order_attachment/PROPOSAL.md — a322e3689a5b58cd56c173d22df93c68199ead8cf04af88cb101af305798468c; distinct check common_product_second_order_attachment_check/REVIEW.md — a12914c8b15d73836f93d0472f94ddfbf4a63b9eff5f9191e4ed483b7cdcf2af.
* Derivative distinct check common_product_launch_derivative_bounds_check/REVIEW.md — aadee4cd02baeef710662631401aef613c1bd353252d7f75d499289991bcf341. Its source common_product_launch_derivative_bounds/PROPOSAL.md — 378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8 was authored and fully read in the preceding task.

The complete composition3a195efc and uniform window1ea1943e, previously fully read, supply the fixed device, target and error aggregation. Their exact complete hashes and checked status are recorded in the baseline and second-order sources above. The component checks are accepted only at their stated scopes; none checked this combined family in advance. ROOT suggested the combined choices and potential exponents. I reconstructed the cutoff constants, nine allocations, endpoint cell budget, cap conditions, exact formulas and exponents here as exposed author work. A distinct combined check remains required.

This is a conditional exact supplied-Hamiltonian, one-head result. Coherent encoded input and legal program preparation are supplied. No native microscopic law, coefficient-production mechanism, timing controller, stationary output, capture/reset, permanent halt, old literal processor transfer or practical runtime is established. The target remains a time-dependent common packet and phase.

Only common_product_refined_resource_family/PROPOSAL.md was created. No scientific executable, numerical integration, simulation, symbolic solver, sweep, upstream source edit, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation occurred. No retained status or independent acceptance of this new combined certificate is assigned.
