# Refined combined resource family: distinct check

No required mathematical correction was found. For the prescribed family, the nine ideal contributions sum to less than 9epsilon/16 and the second-order cell allowance, including both literal-map endpoint replacements, is less than 35epsilon/256. Their sum is therefore less than 179epsilon/256. The Theta(epsilon^-4) site/count scaling, Theta(Lambda^-1 epsilon^-14) duration and Theta(Lambda epsilon^11) smallest positive coefficient are correct sufficient scalings of this family.

## Exact sources and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

New complete reads and SHA-256 verification:

* `common_product_refined_resource_family/PROPOSAL.md`: `79f5bd9c07fe0eb0f37d051446f69759a32559ba7ce9e8bb835db01287188bb3`.
* `common_product_second_order_attachment/PROPOSAL.md`: `a322e3689a5b58cd56c173d22df93c68199ead8cf04af88cb101af305798468c`.
* `common_product_second_order_attachment_check/REVIEW.md`: `a12914c8b15d73836f93d0472f94ddfbf4a63b9eff5f9191e4ed483b7cdcf2af`.

Previously fully read sources and checks, reused after their hashes were refreshed unchanged:

* `common_product_launch_derivative_bounds/PROPOSAL.md`: `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`.
* `common_product_launch_derivative_bounds_check/REVIEW.md`: `aadee4cd02baeef710662631401aef613c1bd353252d7f75d499289991bcf341`.
* `common_product_finite_seed_scaling/PROPOSAL.md`: `0e21dae83a8449f03276b4099ea6a6ae23e08afa5b4a1297122e67e7b9095f6e`.
* `common_product_finite_seed_scaling_check/REVIEW.md`: `751c97d5cabdf08f12f1c1852f0fbcf2bfc5fdcfe3179b6cc033ad23f36c91e5`.
* `common_product_finite_seed_router/PROPOSAL.md`: `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.
* `common_product_finite_window/PROPOSAL.md`: `1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b`.

My preceding composition/window checks, `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9` and `1337df4d94e3d6b555a88167945e5e8490e9df978b1fbc3e140db17622e36cbb`, are reused at their already recorded scopes. I also authored the derivative and baseline checks listed above. This is shared exposure, not previous verification of the new combined certificate. ROOT suggested the recipe and expected exponents; I read the full candidate before checking the algebra. No favorable summary was used as evidence. The check is source-exposed and same-model, not blind or model-diverse. No microscopic-scattering result is imported. Existing workflow snapshots are reused; this is not a formal audit and confers no retained status.

## 1. Derivative premise and fixed cutoff

The quintic cutoff is exactly the previously checked C2 cutoff: Q',Q'' vanish at both endpoints, Q decreases from one to zero, and its support ends at pi/8 inside the conservative pi/6 band. Thus K1<7.5 and K2<240 apply without changing the source amplitude or target phase.

For sigma=pi/24, `pi tan(sigma)>=pi²/24>3/8`, so the integrated-derivative theorem's sufficient domain includes rho<=1/8. The eventual rho<=1/256 is safely inside it, and p>=1-11rho²>1/2 holds.

With L<1, S<2 and pi<4, the derivative constants satisfy C1<2(17+4)=42. For C2 the bracket is less than `2*256+17*4+4+16=600`, so C2<1200. Therefore G1<=100rho^-1 and G2<=2000rho^-3 are valid. G0<=sqrt(pi/3)<2 follows from the conservative support interval and exact normalization. The exact raw-input identity B_minus=sqrt(p)[G1+(2/cmin)G0] gives B_minus<=100rho^-1+4<=200rho^-1. There is no extra normalization factor or dropped phase derivative.

## 2. Simultaneous ideal choices and all error terms

The prescribed u0=10^12rho^-2epsilon^-2 and ell=ceil(100u0) are positive and enormous for every 0<epsilon<=1. In particular ell>8, so the strict upper-window inequality `7ell/4<2ell-2` is valid. The alpha values 3/4 and 7/8 are between 1/sqrt(3) and one. Direct substitution gives the claimed late, outgoing and early margins, with u0/A_early<=1/50. No limit is needed to make the geometric hypotheses true for this family.

For A>=1, the tail simplification follows by squaring: `(A^-2+A^-1)/(2pi)<=A^-1`. The right early bound has numerator at most 100rho^-1+4. The early matching bound, after its sqrt(2) multiplier and A>=ell/2, is at most `2(100rho^-1+4/50)/sqrt(ell)`. At the two observation endpoints, numerators are at most 100rho^-1+12 and 100rho^-1+14, and the square-root gap factor is at most 2/sqrt(ell). These give 104, a ceiling below 300, 224 and 228, respectively, validating the stated rounded constants.

Since sqrt(u0)=10^6rho^-1/epsilon and sqrt(ell)>=10sqrt(u0), the five square-root allocations are bounded by

    2L0 <= 400epsilon/10^6,
    2d_right <= 208epsilon/10^6,
    sqrt(2)T_early <= 300epsilon/10^7,
    2d_L <= 460epsilon/10^7,
    2d_O <= 920epsilon/10^7.

Here d_L<1/2 first establishes d_O<=2n_O; this does not assume quotient monotonicity. Every listed allocation is below epsilon/16. The source residual is 2R0<=2epsilon²/10^12, likewise below epsilon/16. The spectral term is below epsilon/16 because `4sqrt(11)/256<1/16`. Thus the launch normalization condition is established before using the launch target, and both final window normalizations are also legitimate.

For the early Taylor tail, the first possibly unequal power remains d=ell+2. Successive tail terms have ratio <=1/25. The elementary factorial bound gives `(4eu0/d)^d<(1/8)^d` because d>=100u0 and e<3. Multiplying by the geometric-tail factor 2*25/24 gives e_early<3*8^-d<=3/d<=3/(100u0)<epsilon/16. The improved u0 has not invalidated the power-agreement distance or its factorial budget.

For the boundary constants, the terms after factoring rho^-3 have ceilings 2000+1200+104<4000 and 2000+2100+308<5000. Lower powers of rho^-1 may be bounded by rho^-3 because rho<=1. The combined Duhamel prefactor is less than j; incoming qi(t0)>=u0/2 and outgoing qo(tplus)=ell/4 yield

    e_boundary <=8000rho^-3/u0+10000rho^-3/ell
                <=8100rho^-3/u0
                =(8100*256/10^12)epsilon <epsilon/16.

The surviving inverse rho after substituting u0 has explicitly been paid by rho=epsilon/256. This is the important compatibility check between the improved first- and second-derivative estimates. Together the nine nonnegative allocations give the uniform ideal error below 9epsilon/16, with no hidden cancellation or omitted source/projection error.

## 3. Second-order residual and its actual applicability

The new dependency uses exactly this finite one-head operator. Removing only the common scalar 2b leaves blocks `h=[[A,B],[B*,D]]` with B=-b(|u>+|v>), scalar D=D_p, and A=K+a_p(P_u+P_v). K includes the finite equal-diagonal emitter blocks and vanishes on the mediator column. Hence its hypotheses are satisfied by the constructed device, not inferred from a generic attachment slogan.

For hbar=A-BB*/D, the enabled sector is exactly h_F. In the disabled sector its difference from h_F is -j zeta UU*, with U=|u>+|v>, and norm 2j zeta. The disabled endpoint absolute row sum is `j(1-zeta)+j+j zeta=2j`; all other row/column sums are at most 4j. Thus ||hbar||<=4j without presuming positivity of hbar.

For T=(I,X)^T and X=-B*/D-B*hbar/D², direct block multiplication gives residual `(-BB*hbar/D², B*hbar²/D²)^T`, in exactly that order. It is an exact polynomial identity. The endpoint distance is <=sqrt(2)eta(1+4eta²), while the residual is <=j(8eta²+16sqrt(2)eta³). Rectangular Duhamel does not require T to be an isometry and introduces no missing ||T|| factor. The two replacements by the literal J cost twice that endpoint distance. Ordinary Duhamel to h_F adds 2s zeta. Restoring the common scalar and taking the direct sum over legal programs preserves the full operator bound and passive-reference extension.

For eta<=1/8, the resulting literal-map error is bounded by 4eta+11s eta²+2s zeta. The cap two is applied to actual isometries, not to the non-isometric auxiliary T. This verifies the reused dependency's relevant scope and why it may replace the earlier whole-time cell allowance without changing the prepared state or target. It remains a one-head, scalar-mediator, specific finite-K result, not arbitrary attachment protection.

## 4. Endpoint mismatch and accumulated physical error

The new choices give eta²=epsilon/[256(1+s)] and zeta=4eta². Their positive roots obey eta<=1/16 and zeta<=1/64. The complete time used is s=uplus from the initial seed.

The endpoint term is `4eta=sqrt(epsilon)/(4sqrt(1+s))`. It is below epsilon/16 exactly when 1+s>16/epsilon. Here s>=87.5u0 and u0>=10^12epsilon^-2, so the inequality holds throughout 0<epsilon<=1. This checks the nonaccumulating mismatch independently of the order-s eta² term; simply balancing the latter would not have sufficed in general.

The accumulated terms are <11epsilon/256 and <epsilon/32. Therefore the full physical allowance is <(16+11+8)epsilon/256=35epsilon/256. Adding the ideal allowance gives 179epsilon/256 exactly. The estimates are nondecreasing in time where required, so evaluation at tplus covers the entire interval. The common scalar phase, literal input, complete physical output and moving normalized packet are unchanged. Conversion to unhalved channel error costs at most a factor two; using epsilon/2 as the parameter gives a channel-accuracy prescription with the same exponents.

## 5. Cap, exact formulas, counts and comparison

D1=Lambda/2, D0=zeta Lambda/2 and b=eta zeta Lambda/2 give j=Lambda eta²zeta/2 exactly. The incident loads listed in the proposal follow directly from the unchanged full positive blocks. For example the mediator load is Lambda(1/2+eta zeta)<=Lambda(1/2+1/1024)<Lambda. The central endpoint load is Lambda zeta(3eta+4eta²)/2, and its stated parameter maxima leave it far below Lambda. Program, 4j, 5j and 3j loads are also strictly below the cap. The combined mediator and emitter-block convention is unchanged.

Substitution yields D0=Lambda epsilon/[128(1+s)], b=Lambda epsilon^(3/2)/[2048(1+s)^(3/2)], j=Lambda epsilon²/[32768(1+s)²], and gamma=Lambda epsilon³/[8388608(1+s)²]. Consequently tplus=32768s(1+s)²/(Lambda epsilon²), and tminus=(6/7)tplus. The ceiling does not alter Theta orders: ell and s are Theta(epsilon^-4), giving eta order epsilon^(5/2), zeta and D0 order epsilon^5, b order epsilon^(15/2), j order epsilon^10, gamma order epsilon^11 and time order epsilon^-14 with the stated Lambda factors.

The exact counts remain 8+2ell qubits and 9+2ell combined positive blocks. Their scaling is Theta(epsilon^-4). Relative observation width is exactly 1/6. Each compared family uses the same full-output induced-isometry accuracy argument, supplied architecture, moving target convention, reference scope and incident-cap convention. The baseline's -8 count and -35 duration exponents and +28 smallest-coefficient exponent are those already checked for its different parameter recipe. Thus the table fairly compares two sufficient families, while proving neither a fixed-device speedup nor smaller actual physical error, optimality, or a lower bound.

Gamma is the smallest positive scalar coefficient in the displayed decomposition. The inequalities gamma<j, j-gamma>gamma and 2j-gamma>gamma follow from rho<=1/256. Also a0=2j, b/j=1/eta>1 and `(D0-2b)/j=(1-2eta)/eta²>1`; D1-2b is larger. These are coefficient magnitudes, including subterms inside combined blocks. They are not spectral gaps, tolerances, precision costs or a mechanism for manufacturing exact correlations.

## Limits and work record

This is an explicit conservative sufficient family for the exact supplied positive finite Hamiltonian. Native-law identification, coefficient production/tolerance, coherent-input preparation, practical performance, capture/reset, permanent output, stationary readout and old processor transfer remain outside scope. No microscopic-scattering result was used to strengthen it.

Only this report was written. No scientific executable, numerical integration, symbolic solver, parameter sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. All checks above were analytical; hashing and directory creation were bookkeeping. No retained or formal audit status is assigned.
