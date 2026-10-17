# Proposed scalar background-endpoint perturbation interface

Status: new exploratory analytical proposal, not independently checked. A real scalar endpoint onsite change |delta_b|<=10^-20 can be propagated through the pre-emitter matching inverse, selected endpoint column, actual unit-incoming source and outgoing resolvent row by finite-rank identities. The explicit bounds below are sufficient candidates for reusing the main source-specific Schur/contour machinery. This document does not assert a full-device perturbation theorem or silently include a separately changed emitter energy/coupling.

## Sources, exposure and conventions

Nominal canonical note: `docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md` at supplied commit `97ccd9f9bee7e69af123395fcb04d40812885ac4` in `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree`, previously read and verified SHA256 `bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5`. This task reuses those verified nominal definitions; no later W appendix is used as evidence, and no Git command was run.

Root fixed-spectrum proposal: `../endpoint_precision_root_notes/FIXED_EIGENVALUE_INTERFACE.md`, SHA256 `548c8579d603200db45c7c7f4fdd3f2cef08aee53846efe524ef94591b692057`; independent local-algebra report, reread in full: `../endpoint_fixed_spectrum_interface_check/REVIEW.md`, SHA256 `d370f70e5232904389368434a18a88407d30474b98b030a03c96e4d2e24fc7ce`.

The unchanged source-specific strip estimates were refreshed from `../schur_strip_interface/PROPOSAL.md`, SHA256 `16cc6ce85dd6bd40cf9ca6084274fd9b9d438134b39b35af21646a3af4f82a39`, previously checked in `../schur_strip_interface_check/REVIEW.md`, SHA256 `11346d3c20ca4ae749b3c55750e8e0ec4144a9b4e9f82b3018c093f3a9516f18`, and subsequently composed in the pinned canonical note. Their formerly conditional scalar complex and normalization inputs are taken only in the form established by that nominal note.

This author proposed the earlier background-regularity route and checked several other interfaces. This is exposed follow-up development, not an independent check of this proposal. No scientific execution, simulation, inherited program, parameter scan, Git operation, W edit, checkpoint, prompt or prior-report modification occurred. Only read/hash evidence and this single new document are produced.

Write epsilon=10^-20 and delta=delta_b, real and constant in momentum. Use P for the real isometric inclusion of the eight-dimensional endpoint fiber into the 896-coordinate pre-emitter core, so P^T P=I. This reverses the restriction-map notation of the earlier short interface; all formulas below consistently use inclusion. Let

    A(z)=lambda_j(z)I-H_bg+outgoing boundary self-energy,
    R(z)=A(z)^-1, G(z)=P^T R(z)P,
    H_delta(z)=(I-delta G(z))^-1.

These are finite matching inverses/retarded endpoint kernels, not bounded whole-space resolvents at a continuum energy. The perturbed matrix is A_delta=A-delta PP^T. The single output boundary and its source RHS are unchanged.

## 1. Exact rank-eight identities

Finite-rank inversion gives, with the displayed order,

    R_delta=R+delta R P H_delta P^T R,
    R_delta P=R P H_delta,
    P^T R_delta=H_delta P^T R,
    G_delta=G H_delta,
    G_delta-G=delta G² H_delta.                         (1)

Since delta is scalar, H_delta commutes with G. No commutation of P, R, B or other internal matrices is assumed. Complex symmetry supplies ||P^T R||=||R P||; transpose is not adjoint. The resolvent sign is positive in the update because the Hamiltonian shift enters A_delta with a minus sign.

For a common disk/strip bound ||G||<=K and epsilon K<1, put h_K=(1-epsilon K)^-1. Then

    ||H_delta||<=h_K,
    ||G_delta-G||<=epsilon K² h_K,
    ||R_delta-R||<=epsilon ||RP||² h_K,
    ||R_delta P||<=||RP||h_K.                         (2)

The certified disks have radius rho=10^-12 and ||G||<36. Thus H_delta is holomorphic throughout every such disk, with

    h_36<1+10^-18,
    ||G_delta-G||<1.3e-17,
    ||G_delta||<36.000001.                           (3)

The lower strip h=10^-18 lies inside the disks. Importantly, this uses the small endpoint norm36, not the generic full inverse norm in the Neumann denominator. It remains valid for either sign of delta.

## 2. Actual incoming source column and its reference plane

Let u=P_out u_j be the unchanged physical open output-port source vector and

    x_bg=R iE'(z)u.

The incoming wave fixes this RHS; an endpoint onsite shift changes neither E'(z) nor the incoming wave's reference plane. Therefore

    x_bg,delta=R_delta iE'u
       =x_bg+delta R P H_delta P^T x_bg.              (4)

This is an identity for the entire 896-coordinate source column, including all shared internal coordinates. It does not replace it by a scalar endpoint solution. Consequently

    ||x_bg,delta-x_bg||
       <=epsilon ||RP||h_36 ||x_bg||,
    ||x_bg,delta||<=||x_bg||(1+epsilon ||RP||h_36).   (5)

On the source strip use the unrounded established bounds

    theta=.224,
    B_raw=2.24e18/(1-theta),
    P_raw²=1.008e23/(1-theta)²,
    X_raw=(1.5e9+.062*2.24e18*10^-18)/(1-theta).

These yield explicitly

    B_raw+epsilon P_raw² h_36<2.89e18,
    P_raw h_36<4.1e11,
    X_raw(1+epsilon P_raw h_36)<2e9.                 (6)

For a transparent margin check, X_raw<1.934e9, P_raw<4.1e11 and epsilon P_raw h_36<4.2e-9, so the last line is <1.935e9<2e9. The selected-column squared bound is <1.675e23 before perturbation, below (4.1e11)²=1.681e23; multiplying by h_36² does not close that explicit margin. The full inverse update is <1700, whereas B_raw<2.887e18. No appeal to unspecified continuity is needed.

The real positive-jump identity could also be reproved for A_delta, since delta PP^T is real symmetric and leaves the open boundary imaginary part unchanged. It is not necessary to reuse the old diagonal-block norm or assert that it is exactly unchanged: (4)–(6) already continue the source directly from its established nominal bound.

## 3. Exact outgoing row, including its complex phase

Let L(z) be the source's row mapping a forcing at the background endpoint to the outgoing open coefficient at the fixed output origin. This is the coefficient extracted from the corresponding retarded kernel column. Applying that same coefficient extraction to (1) gives

    L_delta=L+delta L H_delta G=L H_delta.           (7)

Extraction is performed before any off-axis spatial norm: a growing outgoing free wave is not bounded uniformly as an infinite Hilbert vector. No new propagation factor, origin shift or adjustable scalar phase is introduced. Equation (7) is a row identity, not only a statement about its modulus.

On the real band the original scalar approximation has

    L0=−(tau/J) z^(ell+1)/(1+R_bg z^(2ell+2)) P_j,
    ||L-L0||<10^-21.

Flux unitarity of the PRE-emitter two-port scattering matrix gives |tau|<=1, so ||L||<34. The nominal ||G||<35 then implies

    ||L_delta-L||<=epsilon*34*35/(1-35epsilon)<1.2e-17. (8)

This new perturbation is larger than the old epsilon_L=10^-21; the old epsilon_L must NOT simply be asserted for L_delta against the old L0. An exact alternative is to update the diagonal comparison too. With G0=gP_j−Qc/J and H0=(I-delta G0)^-1,

    H_delta-H0=H_delta delta(G-G0)H0,
    L_delta-L0 H0=(L-L0)H_delta+L0(H_delta-H0).

The old real epsilon_G=10^-22 makes the second term negligible, giving ||L_delta-L0H0||<2e-21. The leading open row is now L0/(1-delta g). This factor is complex and must be retained. Both forms are exact enough to feed an updated ratio calculation; (8) is simpler for a direct comparison below.

## 4. Real Green derivative and complex oscillation

Differentiate the exact identity G_delta=G(I-delta G)^-1 at fixed delta. Matrix multiplication need not commute with G':

    dG_delta/dE=H_delta (dG/dE) H_delta.              (9)

Thus the established real ||dG/dE||<35000 implies

    ||dG_delta/dE||<35000/(1-35epsilon)²<35001.

The old strict ceiling35000 is not automatically preserved; the slightly larger explicit35001 is harmless for the downstream 10^6 mass allowance. On the disks (3) and operator Cauchy imply, for y<=10^-18,

    ||G_delta(x-iy)-G_delta(x)||
       <=36.000001*(y/rho)/(1-y/rho)<.000037.       (10)

This is a complex-domain bound obtained from a separately supplied analytic disk; it is not inferred from the real derivative. All seven complementary coordinates remain present.

## 5. Full eight-coordinate emitter after the background change

Keep kappa fixed while comparing delta with zero. For the real interface take 0<kappa<=10^-8. Define

    De_delta=(b_j+E(z)-E0)I-B-kappa² G_delta,
    Dcc_delta=(De_delta)_cc,
    s_delta=(G_delta)_jj+kappa²(G_delta)_jc Dcc_delta^-1(G_delta)_cj,
    Dj_delta=E(z)-E0-kappa² s_delta.

These are the actual eight-coordinate Schur blocks. Since ||G_delta||<35.000001 on the real band, the bare .18 complementary gap gives ||Dcc_delta^-1||<6. The same statement on the rho disks uses .18−.062rho−36.000001 kappa²>1/6. Every inverse exists before its use in s_delta.

Let e_G=1.3e-17 bound ||G_delta-G||. Resolvent subtraction gives

    ||Dcc_delta^-1-Dcc^-1||<=36 kappa² e_G.

Using Green norms <=36 for the real comparison and the product rule for the complementary term therefore gives

    |s_delta-s|<=e_G[1+432 kappa²+46656 kappa^4]<1.4e-17. (11)

No cross term is declared zero. This coarse estimate deliberately avoids pretending that the old off-diagonal error ceiling remains numerically identical. In energy derivative estimates a correspondingly coarse bound suffices:

    ||Dcc_delta'||<=1+kappa²*35001<2,
    ||(Dcc_delta^-1)'||<72,
    |s_delta'|<=35001+kappa²[2*35001*6*36+72*36²]<36000.

This still supplies the accepted mass-lemma allowance L<=10^6, without relying on tiny off-diagonal values. The center values A=35, B=17 and b_min=12 can be retained by comparing to the explicit nominal −z/J approximation and (11), rather than by mistaking ||G_delta||<35.000001 for a proof of A=35. The nominal real/imaginary margins have much more than1.4e-17 slack.

On the narrow strip the disk argument gives

    |s_delta(x-iy)-s_delta(x)|
       <.000037+2*kappa²*(36.000001)²*6<.000038.

For kappa=10^-8, the nominal unrounded real imaginary margin is >(1−1/40000)*.4 kappa²/.031. Subtracting kappa²*1.4e-17 still leaves Im Dj_delta>12kappa² on the real line. Subtracting .062h+kappa²*.000038 then leaves >6kappa² on the strip. Thus the full Schur inverse is holomorphic there by its exact factorization, not by extending a scalar estimate to an unsupported full inverse.

## 6. Direct complex profile comparison without redefining Fref

This section keeps the same kappa and E0 and the same reference Fref, including rho_g and phase113. It compares the actual perturbed emitted coefficient F_{j,delta} with F_j; it does not absorb the endpoint shift into a new target.

Put c=kappa²Dcc^-1Gcj and c_delta=kappa²Dcc_delta^-1(G_delta)cj. The same estimates give ||c_delta-c||<7kappa² e_G, while ||c||<6kappa²*10^-22. Let N=L(u_j+c) and N_delta=L_delta(u_j+c_delta). Equations (8) and these bounds give

    |N_delta-N|<1.3e-17.

The Stone prefactor is unchanged, so F_j/Fref differs from −J N Dref/Dj only by the same known unit-modulus reference factor. Using |Dj|,|Dj_delta|>=(1−.000026)|Dref| and

    |Dj_delta-Dj|/|Dref|
       <=(J/sin k)|s_delta-s|<1.1e-18

gives the explicit perturbation estimate

    |F_{j,delta}/Fref-F_j/Fref|
       < J*1.3e-17/(1-.000026)
          +1.001*1.1e-18/(1-.000026)<2e-18.         (12)

Here |F_j/Fref|<1.001 follows from the nominal ratio estimate. The real lower bounds compare directly with Im Dref, so resonance does not invalidate (12). The fixed common phase is not optimized or conjugated away.

Adding2e-18 to the already rounded bound2e-13+750s would NOT alone preserve that rounded bound. The underlying nominal calculation supplies intercept<1.761e-13 and slope<750. Hence the perturbed intercept is <1.762e-13<2e-13, so the same advertised pointwise ceiling remains valid after this explicit slack check. The uniform .000752 ceiling also retains margin. This is a candidate recalculation, not a declaration that every old intermediate epsilon_G/epsilon_L remained unchanged.

## 7. Complete source and closed-tail continuation at the installed coupling

Reassemble the full matching solution using the perturbed background objects:

    V_delta=[-kappa R_delta P; I8],
    x_e,delta=-kappa De_delta^-1 P^T x_bg,delta,
    x_delta=[x_bg,delta;0]+V_delta x_e,delta.

Equations (6) and the full Schur estimates therefore retain the source ceilings used previously, at kappa=10^-8:

    ||x_bg,delta||<2e9, ||R_delta P||<4.1e11,
    ||De_delta^-1||<.18/kappa² on the bottom,
    ||De_delta^-1||<5e7 on the cutoff sides.

For the side bound one may now use ||G_delta||<36.000001 throughout the strip, which is stronger than the old generic13100. Thus

    |Dj_delta(edge-iy)|
       >=v sigma−.061h²−kappa²*36.000001
                           −6kappa^4*(36.000001)²>2.49e-8.

Consequently the unchanged coarse complete C ceilings follow by the same explicit solve:

    C_bottom<3*2e9[1+kappa*4101*.18/kappa²]+4<5e20,
    C_side<3*2e9[1+kappa*4101*5e7]+4<1.4e13.

C_delta is formed by subtracting the ACTUAL open incoming and reflected waves from the actual perturbed generalized column. The exterior dispersion and fixed internal B projectors are unchanged. Its remaining closed tail is Qc^m Pc x_out,delta, with the same uniform root bound<1/6. It is therefore holomorphic into the fixed Hilbert space by geometric convergence, and ||C_delta||<=3||x_delta||+4 remains valid. This is a complete source/core/closed-tail statement, not merely an endpoint Green estimate. No off-real unit-modulus assertion about the installed reflection is used.

For the unchanged reference parameters, a0=conjugate(omega_p f), its scalar contours and positive target normalization are unchanged. The actual emitted profile error is still separately paid through (12); it is not assumed equal to the reference. These are the matching interfaces needed to attempt the same full-device machinery.

## 8. What has and has not been supplied

The calculations propose preservation of useful loose ceilings for source continuation, outgoing complex ratio, actual self-energy regularity/oscillation and complete localized C under a scalar background endpoint perturbation of either sign with magnitude<=10^-20. The positivity/radius changes from a literal added onsite coefficient can be checked directly against the original positive occupation compensation; a negative perturbation should be combined with that existing positive term, not asserted itself PSD.

No full-device error budget is concluded here. Independent review must check the row extraction in (7), the full Schur comparisons (11)–(12), and the use of explicit unrounded nominal margins. The actual local spectral synthesis after perturbation follows the same single-open-boundary proof once real invertibility is accepted, but its complete application and mass/static/finite-time composition should be stated separately rather than hidden under continuity.

In particular a fixed-eigenvalue rotation ALSO changes emitter energy and usually kappa. For that application delta_b=-Delta_e, and the present comparison at fixed kappa/E0 is not by itself the full result. The emitter shift must enter Dcc and Dj, cutoff bounds and the centered mass interval; the reference/target comparison must use the specified actual or fixed nominal waveform. For a simultaneous |Delta_e|<=10^-20 the displayed gap and side margins have room after explicitly subtracting it, but no correlated-rotation tolerance or complete contract is claimed from that observation. A range approaching kappa=0 would require a new strip prescription; the h=10^-18 complete-core conclusions above are only at the installed kappa=10^-8. Those are the remaining integration obligations, not evidence of a failed route.
