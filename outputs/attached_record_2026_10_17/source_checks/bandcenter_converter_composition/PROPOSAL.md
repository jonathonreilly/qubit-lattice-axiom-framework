# Nominal two-converter full-fiber composition, F=40

Status: proposed analytical stationary scattering lemma, requiring separate checking. This closes the nominal seven-closed-channel interface of the preceding converter proposal, conditional on the original certified source bounds. It does not transfer an emitter spectral-mass theorem, preparation contract, runtime, or finite-window theorem. No scientific execution, parameter search, delegation, Git/W/checkpoint/prompt edit, or model change was performed. I authored the predecessor and am source-exposed.

## Sources, revision and scope

The predecessor is `../bandcenter_after_two_attempts/ASSESSMENT.md`, SHA256 `5fb537b04ee42624bb24c8efef6f2d1c9e1f2edd52d28adb8f05ff864f381e71`, reread completely. Its old source pin was endpoint-note SHA256 `d17d5e32f3f44f162aff15ced734238ba1543212525d618d36dc95511095c4be`, associated with Git commit `7dcc98203477cf9868dc9b7f7dd2aeccffeda9a3` (a Git identity, not a file hash). For this lemma I read the relevant original source, filter, port-kernel and finite-block arguments in `correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`. An initial read/hash exposed snapshot `9d493f2c67525f89fc32cc1201888a8729b64a2ce5522a7ad46dc9d473b2aae3`; root then switched the worktree and reports that snapshot recoverable at commit `7e3d991496`. The subsequent relevant-body reread was on root-reported current note hash `99a16de7d111bc0d3ab87ecb566db80b3a678c534cecc86ae7fe2d4dd9625639`; root says this change only updates landing-link presentation. The present proof uses the explicitly reproduced bounds below, not a silently refreshed whole-note endorsement.

Root reports a separate scalar converter review with SHA256 `205ed6a7442d7a6a438a36ac3a1e2473ac40d65c0b13d00beb1926c867204294`; I did not read or import its conclusions as proof. Scalar algebra is reproduced here. Applicable previously read AGENTS/workflow identities are respectively `febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0` and `71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`. The previously read physics-claim-reviewer identity is `9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455`. This is an authored proposal, not an independent audit.

Only nominal j and tau are considered. No common-j perturbation family is included. In such a future family the correct map would be cos(k)=1-(j_a/J)(1-cos(q)); retaining nominal C0 would be wrong.

## 1. Fixed apparatus and inherited bounds

Keep the literal original B, K, W, source contacts, phase filter at arm position 20, junction and arm endpoint N=44. Do not use either failed contact attempt. Set

    sigma=10^-6, F=40,
    k0=2 atan(1/4.510351185997098),
    C0=cos(k0), S0=sin(k0),
    j=J(1-C0), tau=sqrt(j J S0), gamma=tau-j>0.

Here J=.030021107107032 exactly. The exact rational half-angle data give

    .03<J<.031, .4<S0<.5, .0027<j<.003, tau<.007.

For example 4.5<q0<4.6 gives .09<2/(q0^2+1)<8/85, proving the j bounds; S0>.41 follows from the same rational formula. These are analytical rational bounds, not sampled estimates.

The original exterior port origin is m=0. Retain each old-J port through m=F, replace its next bond by -tau, and use a new-j tail thereafter. There are TWO converters, on the input and output exterior ports, not four arm converters. At each interface the old site has diagonal J+j and first new site diagonal 2j. The positive realization is Q(-tau) and two positive vacancies gamma(I-n), with scalar 2gamma per converter. The total added scalar is 4gamma, in addition to all original scalars. The source and its internal degrees of freedom are shared exactly as before.

For each of four selected old/parity columns, on I_old=k0+[-sigma,sigma], the inherited source supplies one open direction P and seven closed directions Pc, with fixed real B spectral projections. Write

    Q=zP+Qc, z=exp(ik), A=[J(Q-Q^-1)]^-1,
    ||Qc||<=r=1/7, ||A||<=40, ||A^-1||<20.

The 1/7 bound is the explicit original note's fixed-band root premise, not a substitution of 1/7 for an earlier .15 estimate. The source-excited invariant sector obeys B_exc>=1+min(DeltaA,DeltaB)>3.186, because the remaining displayed source interactions are positive. Thus B_exc-b>.186 for b=1,3; the other vacuum channel differs by +/-2.

The old two-port Green kernel is

    G_ab(m,n)=delta_ab A Q^|m-n|+Q^m T_ab Q^n,
    T_ab,PP=A_open S_ab,
    ||T_ab,PC||,||T_ab,CP||<=Ktail r^24,
    ||T_ab,CC||<=Ktail r^48, Ktail=1.3e7.

The old open matrix is S=[[R,t],[t,R]], exactly unitary, with

    |R|<12 sigma,
    |t-rho_g(k) omega_p|<d0+714 sigma,
    d0=1.76e-13, rho_g=-zeta z^(2N+4).

The full original finite Green blocks before endpoint deletion are <3e7, as follows from the note's bare <250, filter update <1.3e7 and physical port mixing. Its finite old core has at most 113 head sites, a deliberately conservative subset count using the note's larger endpoint construction. None of the emitter inverse bounds is used.

## 2. Entire new band lies inside the inherited band

For q in pi/2+[-sigma,sigma], put E=2j(1-cos(q)) and choose k by E=2J(1-cos(k)). Exactly,

    cos(k)=C0+(1-C0)cos(q).

Since |E-E0|<=2j sigma<.006 sigma and the old interval has edge-energy margin at least v sigma=.025 sigma, monotonicity places k strictly inside I_old. The mean-value bound gives |k-k0|<.24 sigma and k'=2j sin(q)/E'_old<.24. In particular sin(k)>.4. No inherited band is enlarged.

All seven new complementary roots remain closed. For an excited channel,

    X_new=(beta-b)/j+2 cos(q)>.186/.003-2 sigma>61.99.

For the other vacuum channel |X_new|>2/.003-2 sigma>666. Thus the real decaying root w of w+w^-1=X_new has |w|<1/60 in every closed direction, including the negative root for the lower vacuum channel. This follows by comparing |X_new| with 60+1/60. The new tail therefore still has exactly one open channel.

## 3. Open converter, including phase and velocity factors

At the interface let old incidence be psi_F=1+r_o and psi_(F-1)=z^-1+r_o z. With outgoing new wave psi_1=A_new, psi_2=exp(iq) A_new, elimination gives

    D=E-J-j+J S0 exp(iq),
    r_o=-(D+J/z)/(D+Jz),
    A_new=(tau/j) exp(iq)(1+r_o).

At q=pi/2, r_o=0. The flux-normalized transmission in either direction is i. Reciprocity supplies equality of the two flux-normalized transmissions throughout the band; flux conservation gives |t_c|<=1 and |r_n|=|r_o| for reverse reflection r_n.

The numerator and denominator derivatives of r_o each have magnitude <.029: use 2j+J S0+J|k'|<.006+.0155+.00744. The central denominator magnitude is 2J S0>.024. Consequently

    |r_o|=|r_n|<=rho:=.029 sigma/(.024-.029 sigma)<1.22 sigma.

With v_old=2J sin(k), v_new=2j sin(q), the flux transmission is

    t_c=exp(iq) sqrt(S0 sin(q)/sin(k)) (1+r_o).

Writing the square root as w0, |w0^2-1|<.61 sigma, |w0-1|<.62 sigma and w0<1.000001. Therefore |t_c-i|<3 sigma and |t_c^2+1|<6 sigma. The reference plane at the first new site matters: it supplies exp(iq). Neither the phase nor the velocity conversion is dropped.

## 4. Every closed converter is uniformly invertible

In one closed B channel let a=q_old, w=q_new and epsilon=lambda-beta. Both are signed real decaying roots. At m=F put

    D_c=epsilon-J-j+J S0 w,
    R_c=-(D_c+J/a)/(D_c+Ja).

Using epsilon=2J-J(a+a^-1), the denominator and numerator become

    D_c+Ja=J-j-J/a+J S0 w,
    D_c+J/a=J-j-Ja+J S0 w.

Since 0<j<J, |a|<=1/7, |w|<1/60 and S0<1/2,

    |D_c+Ja|>J(7-1-1/120)>5.99J,
    |D_c+J/a|<J(1+1/7+1/120)<1.152J,
    |R_c|<1/5.

These absolute inequalities cover all seven channels and both signs; no closed interface pole is assumed absent. The eliminated new boundary diagonal is -j/w, so it too is nonzero. They prove invertibility of the corresponding two-site interface matrix by its Schur complement.

At the original port reference plane, write the old-buffer closed wave as

    psi_m=a^m b_c+a^-m a_c, 0<=m<=F.

The boundary equation D_c psi_F+J psi_(F-1)=0 gives the ACTUAL return

    a_c=R_c a^(2F) b_c.

Thus the two-port closed return operator E_c is diagonal in the fixed B basis and satisfies ||E_c||<(1/5)7^-80<2e-65. The last loose bound follows from 7^10>10^8. F is measured from the original exterior port origin; the original filter-to-junction distance 24 is a separate factor.

## 5. Exact source feedback and its quantitative cost

Use physical old-port incoming/outgoing coefficients a,b, including formal growing closed coefficients. Their generalized source relation is

    b=S_gen a, S_gen=T A^-1.

The RIGHT multiplication is essential when closed components mix. It follows from the displayed Green kernel: a source at port n has incoming coefficient A Q^n and outgoing coefficient T Q^n. Equivalently, a finite-core solution is G(core,ports0) A^-1 a; adding the prescribed incoming wave on the exterior cancels its boundary forcing.

Combining two ports costs a block factor 2, so

    ||S_gen,PC||,||S_gen,CP||<=epsilon_c=5.2e8 r^24<5.2e-12,
    ||S_gen,CC||<=c_c=5.2e8 r^48<5.2e-32.

For the rounded inequalities use 7^24>10^20. The complete closed feedback is

    b_C=(I-S_CC E_c)^-1 S_CP a_P,
    a_C=E_c b_C,
    S_tilde=S+S_PC E_c(I-S_CC E_c)^-1 S_CP.

It follows that

    ||S_tilde-S||<delta_c=1e-86,
    ||b_C||<6e-12 ||a_P||,
    ||a_C||<1.2e-76 ||a_P||.

All inverses here have explicit Neumann margins. S_tilde is the open scattering matrix of the real finite old device with the closed decaying converter loads installed; current conservation makes it unitary. Closed loads carry zero current. Alternatively the displayed estimate ||S_tilde||<=1+delta_c suffices for the following bounds with imperceptible extra margins.

## 6. Open multiple returns and literal old W

Let alpha,beta be physical incoming/outgoing coefficients on the two NEW ports, and chi=sqrt(v_new/v_old)<sqrt(.006/.025)<.49. The old coefficients satisfy

    a_P=r_o z^(2F) b_P+t_c z^F chi alpha,
    b_P=S_tilde a_P,
    beta=r_n alpha+t_c z^F chi^-1 b_P.

These equations explicitly pay the velocity factors, which cancel in the new open scattering matrix:

    S_new=r_n I+t_c^2 z^(2F) S_tilde
                    (I-r_o z^(2F) S_tilde)^-1.

The return inverse exists because rho<1.22e-6. Comparing with -z^(2F)S gives

    ||S_new+z^(2F)S||
      <=rho+6 sigma+rho/(1-rho)+delta_c <9 sigma.

Hence in EACH of all four old/parity columns,

    ||S_new-[-z^(2F)rho_g(k)omega_p] X_port||
       <d0+735 sigma <.000736.

The target contains the literal inherited W eigenvalue omega_p, one common scalar phase -z^(2F)rho_g(k), and the actual nonconstant mapped k(q). No per-column rephasing or new source calibration occurs. The added known scalar is 4gamma; total physical aging remains exp[-it(c_old+4gamma)] exp(-itK). The selected physical energy is b+2j(1-cos(q)) plus that scalar. At the exact center the open converters are transparent, but the exponentially small closed feedback is still present: it is not called exactly zero.

This is a uniform stationary column/port bound. It is not automatically a complete-output operator bound on arbitrary superpositions of the two old energies: later spectral integration must retain the established possible error overlap and corresponding aggregation factors. Orthogonal parities remain orthogonal.

## 7. Full source and evanescent amplitudes are retained

For ||alpha||<=1, the open feedback gives ||a_P||<=chi/(1-rho)<1 and the previous bounds supply a_C and b_C. Every original finite coordinate is recovered EXACTLY by

    psi_core=G_old(core,ports0) A^-1(a_P+a_C).

Using the inherited <3e7 block bound, <20 for A^-1, two ports and at most 113 old finite head sites gives ||psi_core||<2e10. This is intentionally a loose complete finite-coordinate bound, not a whole-space real-resolvent norm. No source or complementary coordinate is projected away.

On each old buffer the exact field is Q^-m a+Q^m b. In the closed sector, a_C=R_c Qc^(2F)b_C, so throughout 0<=m<=F its norm is at most (1+1/5)||b_C||, including the otherwise growing term. The combined finite open buffers have a simple conservative norm <40 for unit alpha. Coordinate counting can overlap the port origins; an overcount only enlarges this bound.

For the new closed tail the first site is

    psi_new,1=(tau/j) Q_new,C psi_old,F,
    psi_new,n=Q_new,C^(n-1) psi_new,1.

Since tau/j=sqrt(J S0/j)<2.4, its complete geometric l2 norm on both new tails is bounded by

    [2.4/60]/sqrt(1-1/3600) * (6/5) r^F ||b_C||
       <.05 r^F ||b_C||.

The open waves on the new tails are the explicit alpha,beta scattering waves, not discarded localized mass. Subtracting them leaves all finite buffers, all old source/core coordinates, and the complete new closed tails just described. These formulas provide recoverability and finite stationary bounds; they do not assert a differentiated packet estimate or absence of out-of-band point spectrum.

## 8. Remaining decisive interface

The nominal full-fiber stationary bridge is quantitatively plausible with substantial margins: new conversion costs <9e-6 and closed return feedback <1e-86 on the inherited band. Its separate check should focus on T A^-1 orientation, the reference planes/chi factors, and the old finite-block premise as applied before endpoint deletion.

The NEXT proof obligation for an actual autonomous device is to close the NEW input tail and attach the proposed equal-diagonal emitter block, derive its full endpoint Green matrix and outgoing row on this new band, then prove mass, profile, complementary emitter, localized escape and finite-window estimates with the slower velocity. Neither the older runtime nor any old complete-output tolerance is inherited. Out-of-band/point mass must still be controlled. An eventual common-j robustness claim needs a separately specified converter supplier family, the corrected actual band map, and comparison to a fixed nominal waveform; this nominal lemma does not supply it. No global Lorentzian, native precision removal, or finite permanent halt is claimed.
