# Transition-localized derivatives for the shrinking source cutoff

New bounded author derivation requiring a distinct check. The exact source profile with the stated shrinking quintic cutoff obeys G2<=600/rho^3 uniformly when0<rho<=1/2, rho^2<=h<=10^-3 and the actual cutoff mass is at least1/2. This removes the artificial h^-1 in the older sufficient ceiling1200/(h rho^3). The proof retains cutoff derivatives, source phase and positive normalization. A conditional interface substitution into resource sourcec4086aec is spelled out below; that older source is not edited and its sufficient bound remains valid.

ROOT proposed the transition-support estimates and possible resource consequences. They are design exposure. Every inequality below is reconstructed, and the new derivative and combined-family claims require a distinct review. No actual dynamics, matrix solver or numerical parameter sweep is used.

## 1. Exact profile, cutoff and domain

Let q=k-pi/2, a=2-rho^2 and c=sqrt(2/pi). The exact outgoing source amplitude, including its phase, is

    F(k)=-i c rho exp(ik)/D(q),
    D(q)=-a tan(q)-i rho^2.                    (1)

This is the cancellation established in derivative378086 from the complete normalized standalone sourcefb72f4ed; it is not merely a modulus approximation. Fix the real cutoff chi(q) as follows. It equals1 for |q|<=h/2, equals Q(s) for h/2<|q|<3h/4 with s=(|q|-h/2)/(h/4), and equals0 thereafter, where

    Q(s)=1-10s^3+15s^4-6s^5.

Q(0)=1,Q(1)=0, and Q',Q'' vanish at both endpoints, so this is a C_c^2 cutoff. Its derivatives are supported only on the TWO transition intervals, whose total length is h/2. Direct differentiation gives

    Q'=-30s^2(1-s)^2, ||Q'||_infinity=15/8,
    ||Q''||_infinity=10/sqrt(3),
    ||chi'||_infinity<=8/h,
    ||chi''||_infinity<=100/h^2.               (2)

For Q'', the extrema are at s=(3+/-sqrt(3))/6 and have magnitude10/sqrt(3). Multiplication by(4/h)^2 gives160/(sqrt(3)h^2)<100/h^2. The corresponding first-derivative factor is4/h, giving15/(2h)<8/h. The absolute-value coordinate creates no cusp at q=0 because chi is constant there.

Assume

    0<rho<=1/2, rho^2<=h<=10^-3,
    p_chi=||chi F||_2^2>=1/2,
    g=chi F/sqrt(p_chi), G_r=||g^(r)||_1.       (3)

All integrals below use k or equivalently q with dq=dk. The normalization is the actual positive square root p_chi, never a fitted replacement. The mass condition is an explicit premise for the standalone derivative statement; the two resource policies verify it from their spectral measure below. It need not follow from rho^2<=h alone.

## 2. Raw resonance derivative over the central interval

On |q|<=h, a>=7/4>1 and |tan q|>=|q|, hence

    |D(q)|>=sqrt(q^2+rho^4).

Also sec^2(q)<=2 and |tan q|<=2h on this small interval, so

    |D'|=a sec^2(q)<=4,
    |D''|=2a sec^2(q)|tan q|<=16h<=16.          (4)

These are ordinary real-axis inequalities. No contour continuation of the nonanalytic compact cutoff is involved.

Set I_m=integral_(|q|<=h)|D(q)|^-m dq. The following sufficient estimates have their domains and measures explicit:

    I_1<=2h/rho^2<=2/rho^2,
    I_2<=integral_R dq/(q^2+rho^4)=pi/rho^2,
    I_3<=integral_R dq/(q^2+rho^4)^(3/2)=2/rho^4. (5)

The last two follow by an arctangent and the primitive q/[rho^4 sqrt(q^2+rho^4)], respectively. They integrate the resonance instead of taking a worst-case denominator over the full support.

Differentiating exp(ik)/D twice, retaining BOTH phase derivatives, gives

    F''=-i c rho exp(ik)
       [-D^-1-2i D' D^-2-D'' D^-2+2(D')^2 D^-3].

Thus, since0<=chi<=1,

    ||chi F''||_1
       <=c rho[I_1+(2*4+16)I_2+2*4^2 I_3]
       <=c[(2+24pi)/rho+64/rho^3]
       <=c(66+24pi)/rho^3.                    (6)

The final step uses rho<=1. The deliberately loose replacement16h<=16 remains legitimate; it introduces no inverse h. In particular the raw source phase exp(ik) has not been discarded in this estimate.

## 3. Cutoff derivative terms only on their actual support

On either transition interval |q|>=h/2, so |D|>=h/2. Equation(1), its first derivative and(4) imply

    |F|<=2c rho/h,
    |F'|<=c rho(2/h+16/h^2).                  (7)

Use the TOTAL transition length h/2, not the full central interval, in the terms carrying chi' or chi''. Equations(2),(7) give

    2||chi' F'||_1
       <=2(8/h)(h/2)c rho(2/h+16/h^2)
       =c(16rho/h+128rho/h^2),
    ||chi'' F||_1
       <=(100/h^2)(h/2)(2c rho/h)
       =100c rho/h^2.                         (8)

Because h>=rho^2, one has rho/h<=rho^-1<=rho^-3 and rho/h^2<=rho^-3. Therefore

    2||chi' F'||_1<=144c/rho^3,
    ||chi'' F||_1<=100c/rho^3.                 (9)

This is the load-bearing localization. Bounding chi'' by h^-2 across the entire resonant region would ignore that it vanishes near q=0 and would restore the unnecessary inverse h.

The product rule and positive normalization now yield

    G2<=sqrt(2)c[(66+24pi)+144+100]/rho^3
       =(2/sqrt(pi))(310+24pi)/rho^3
       <600/rho^3.                            (10)

For a purely coarse numerical check, pi<4 and sqrt(pi)>3/2 give the prefactor less than(4/3)*406<600. No numerical integration or fitted constant enters. The bound600 is sufficient and not claimed optimal.

## 4. Other source bounds retained

The same general-cutoff derivative estimate of378086, with L=tan h<=2h and K1<=8/h, gives

    G1<=(2/sqrt(pi))[2L(K1+1)+pi]/rho
       <=2[4h(8/h+1)+pi]/rho<80/rho.           (11)

This formula uses p_chi>=1/2 directly; no stronger rho restriction is required here beyond(3). Its derivation is the same explicit integrals for |D|^-1 and |(D^-1)'|, and does not differentiate the normalization with respect to k: p_chi is a fixed scalar for the chosen profile. The exact p_chi is not k-dependent.

Normalization and support length give G0<=sqrt(2h)<1. For real chi, the raw incoming amplitude is conjugate(F), so the source launch coefficient remains

    B_minus=sqrt(p_chi)[G1+sec(h)G0]<=82/rho.    (12)

The final upper bound uses p_chi<=1 from the complete source measure, sec(h)<=2 and rho<=1. This upper mass condition is part of using the actual source cutoff0<=chi<=1. The new result does not change its spectral phase, cutoff profile, measure, physical launcher or comparator normalization.

## 5. Conditional substitution into the complete split-budget families

Use the exact supplied staged positive device and both source policies F and A from frozen resource sourcec4086aec. Retain h=epsilon/10^5, eta^2=zeta=epsilon/10^5, j=Lambda epsilon^2/(2*10^10),0<epsilon<=1. Policy F uses rho=epsilon sqrt(h)/1024 and its fixed valid local writer bound; policy A uses the valid B=10 packet constants20,800,56000, recomputed through all feedback/internal formulas, then

    rho=min{epsilon sqrt(h)/1024,
                    [epsilon/(4096(1+T0))]^2}.

Here T0 is the recomputed internal-map ceiling, independent of rho and ell. For both policies rho^2<=epsilon^2 h/1024^2<h, rho<=1/2, and the exact source probability estimate P<=3rho^2/h gives p_chi>=1-P>1/2. Thus every premise of(10)--(12) is actually satisfied. No source probability or normalization condition is inferred from small h alone.

Replace ONLY the sufficient G2 coefficient by

    g2_new=600/rho^3,

while keeping g1=80/rho, bminus=82/rho, and the correctly recomputed q1,q2,T0,T1. Define anew

    H1bar=g1+q1,
    H2bar_new=g2_new+2q1 g1+q2,
    J0bar=T0, J1bar=T0 g1+T1,
    A_i_new=g2_new+(12j/v_min)g1
                              +(4j/v_min+48j^2/v_min^2),
    A_o_new=H2bar_new+21H1bar+154,
    L=max{1,bminus,g1+1,H1bar+1,g1+7},
    Q_new=max{1,eta^-1,rho^-2,J1bar+J0bar,A_i_new+A_o_new},
    u0_new=10^12 max{1,(L/epsilon)^2,Q_new/epsilon},
    ell_new=ceil(100u0_new), M_new=ell_new+1,
    t0_new=u0_new/j,
    t_minus_new=3ell_new/(4j), t_plus_new=7ell_new/(8j). (13)

All expressions are explicit and noncircular. In particular changing the derivative ceiling does not change rho in either policy: T0 is a stationary internal coefficient bound and is independent of g2. New ell and times describe a new shorter sufficient device family; the output Fourier sequence is recalculated with that same new ell, not borrowed from the old-length comparator. Its phase remains -i exp(i[n+ell_new+57]k-itE), with common physical scalar8b+2c_R.

## 6. All twelve allocations and the flag interface remain paid

Equation(13) gives L/sqrt(u0_new)<=epsilon/10^6, Q_new/u0_new<=epsilon/10^12 and ell_new>=100u0_new. All strict early, late and outer-return gaps are unchanged in form and positive because u0_new>=10^12. The new physical F caps still retain diagonal2j, and all I source, core, writer, cable and record blocks retain their definitions and incident-load conventions.

The complete finite-output allowances are bounded as follows, with u=u0_new and ell=ell_new:

| Allowance | Sufficient new ceiling |
|---|---|
| Actual/reference early contact | Q_new/u |
| Source residual2R0 | 2Q_new/u |
| Incoming launch2L0 | 2L/sqrt(u) |
| Spectral tails4sqrt(P) | 4sqrt(3)epsilon/1024 |
| Right early projection | 8L/sqrt(u) |
| Early lead match | 4L/sqrt(ell) |
| Early internal match | 3Q_new/ell |
| Integrated finite boundary | 2Q_new/u |
| Late incoming | 6L/sqrt(ell) |
| Complete scattering | epsilon/256 |
| Late internal | 56Q_new/ell |
| Final F truncation | 28L/sqrt(ell) |

Every ceiling is below epsilon/32. The ONLY changed analytic input to the boundary term is the now-proved g2_new in A_i_new,A_o_new. The twice-integration-by-parts formula retains all source, Q(k) derivative and phase terms through H2bar_new. The source residual remains controlled by rho^-2 inside Q_new, and the actual early contact still pays eta^-1 there. Internal norms remain in J0bar,J1bar; they are not presumed smaller because G2 improved. The other terms do not require a second derivative and retain their previous proof with the new distances/times.

These inequalities reestablish launch normalization, D_L<1/2 and final outgoing truncation positivity before use. Thus the complete normalized final-output error remains<3epsilon/8 throughout the positive-width window[t_minus_new,t_plus_new], whose relative width is1/6. Counts remain137+4ell_new qubits and168+4ell_new positive blocks. Every full-space incident sum remains below Lambda. The complete actual outputs, coherent programs and arbitrary passive references are retained, including residual emitters, all writer/cable/mediator heads and wrong-record components.

For policy A the entire-horizon branch proof also survives explicitly. Its source L1 estimate G0<=epsilon/[256(1+T0)] is unchanged. After t0_new the first eight allowances sum to less than epsilon/4; the strict internal flagged norm and F-origin omission together cost at most epsilon/256, scattering costs less than epsilon/512, and the far-F tail costs3L/sqrt(ell_new)<=3epsilon/10^7. Before t0_new, the reference is recordblank, actual contact costs Q_new/u0_new, and the SAME unnormalized outgoing target costs2L/sqrt(ell_new). Hence the absolute branch error remains<epsilon/2 on[0,t_plus_new], with unhalved subnormalized-channel discrepancy<epsilon. The target is never switched to zero or redefined at the matching time.

The separate final normalized-output theorem still implies record1 and joint record1/F-support success probability greater than1-(3epsilon/8)^2 on the final window. No accuracy conditioned on a rare early flag is inferred, and no bound is extended past the new finite horizon. Policy F alone has no newly asserted all-horizon flag guarantee.

## 7. New sufficient orders and comparison scope

Keep the chosen valid writer inverse B fixed independently of epsilon. As in c4086aec, all stationary packet coefficient ceilings q1,q2,T0,T1 have finite limits as epsilon tends to zero; T0 has a positive finite limit. This follows from their explicit algebraic formulas and nonzero denominator margins, not a fitted numerical operating point.

For policy F, rho=Theta(epsilon^(3/2)). Thus g1=Theta(epsilon^(-3/2)), g2_new=Theta(epsilon^(-9/2)), L=Theta(epsilon^(-3/2)), and Q_new=Theta(epsilon^(-9/2)). The last order has matching lower bound because A_i_new+A_o_new>=g2_new, while every other term has no larger order. The squared lead term(L/epsilon)^2 has order epsilon^-5, whereas Q_new/epsilon has order epsilon^(-11/2), which dominates. Therefore

    F: size,jt_plus_new=Theta(epsilon^(-11/2)),
       t_plus_new=Theta(Lambda^-1 epsilon^(-15/2)),
       gamma=Theta(Lambda epsilon^(7/2)).       (14)

For policy A, the second term in the rho minimum eventually dominates, so rho=Theta(epsilon^2). Then g1=Theta(epsilon^-2), g2_new=Theta(epsilon^-6), L=Theta(epsilon^-2), Q_new=Theta(epsilon^-6). The respective time terms have orders epsilon^-6 and epsilon^-7, giving

    A: size,jt_plus_new=Theta(epsilon^-7),
       t_plus_new=Theta(Lambda^-1 epsilon^-9),
       gamma=Theta(Lambda epsilon^4).          (15)

The ceilings and finite core addends do not affect these orders. For each fixed policy, the same accuracy convention, architecture, cap and relative window are compared:

| Policy | Prior split size/jt | New size/jt | Prior split physical time | New physical time |
|---|---|---|---|---|
| F: normalized final output | Theta(epsilon^(-13/2)) | Theta(epsilon^(-11/2)) | Theta(Lambda^-1 epsilon^(-17/2)) | Theta(Lambda^-1 epsilon^(-15/2)) |
| A: absolute branch plus eventual output | Theta(epsilon^-8) | Theta(epsilon^-7) | Theta(Lambda^-1 epsilon^-10) | Theta(Lambda^-1 epsilon^-9) |

These are sufficient analytical families, not optimal exponents, measured speedups, lower bounds or practical resource claims. No claim is made that600 is optimal. Prefactors, supplied exact coefficients and logical/record preparation remain real premises; the smallest coefficient magnitude is not a fabrication tolerance or coefficient-production cost.

## 8. Source identities, exposure and limits

The exact profile/general-cutoff source is common_product_launch_derivative_bounds/PROPOSAL.md,378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8, with standalone launchfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4. Both were authored/full-read and checked at their stated scopes in this coherent campaign. Their exact phase and complete measure are reused; the new localized cutoff bound is derived here.

The substitution target is unchanged common_product_stage_record_resource_split/PROPOSAL.md,c4086aec4d338da11dcea256367e34ceea496044ca7ff1bc30ca55ee5489f977. Its frozen parent sources are finite7286105ffd9b6b6d0caa97b121c5e79d37dfcf638128d63c6bbc144e9aa2a995 and flage7b53eeda3fc7df96986d3b55f68d9e5af4f1b6657ba068b6f33d03e18a37ee0. Their complete proofs and the packet/stationary/writer component pins are reused at their recorded scopes. No new distinct review is presumed complete merely because this followup was assigned. The new resource claims are conditional on those component/finite/branch premises and the new localized derivative calculation; they require their own check.

ROOT supplied the proposed localization inequalities and tentative new exponents. This author reconstructed the derivative product rules, transition integrals, p_chi dependence and every interface allocation. This is source-exposed author work, not independent checking. Review should verify the transition widths and quintic derivative constants, D derivatives, resonance integral powers, both source phase derivatives, the p_chi premise, all new maxima, and the two different source-policy asymptotics.

No native Record, physical readout, old literal processor, indefinite flagged correctness, irreversible latch, permanent halt, capture/reset or new interaction law is inferred. Only common_product_narrow_cutoff_derivative/PROPOSAL.md was created. No scientific executable, solver/simulation, sweep, source/W/Git/publication/checkpoint/axiom/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
