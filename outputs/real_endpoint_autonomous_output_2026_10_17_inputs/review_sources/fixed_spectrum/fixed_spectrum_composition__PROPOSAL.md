# Fixed-spectrum endpoint orientation: proposed complete conditional composition

Proposed result, requiring a selective independent check: holding the complete local block spectrum fixed and varying only its small real orientation so that r=kappa_a/kappa0 lies in [1-10^-6,1] gives complete fixed-nominal operator error <.000347 for every t>=4e21. One fixed device with M=2e23 output sites gives <.001347 on [4e21,8e21]. The original delivered product seed is unchanged. This is a supplied fixed-spectrum error-direction contract, not a native control mechanism or robustness to generic block errors. The newer nominal T=10^19 refinement is NOT transferred.

## Sources and exposure

All proposal/review paths below are under /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. The four newly assigned sources were read completely and their hashes refreshed:

| Source | SHA256 |
|---|---|
| endpoint_precision_root_notes/FIXED_EIGENVALUE_INTERFACE.md | 548c8579d603200db45c7c7f4fdd3f2cef08aee53846efe524ef94591b692057 |
| endpoint_fixed_spectrum_interface_check/REVIEW.md | d370f70e5232904389368434a18a88407d30474b98b030a03c96e4d2e24fc7ce |
| endpoint_background_perturbation/PROPOSAL.md | 8c308e8d699122318f41fc0195028f3626ba3bd14558d589b3271f16a6c7d32e |
| endpoint_background_perturbation_check/REVIEW.md | a7fd6b54e1be5fe21e2001d8509bf8961247ee47c506968ae0eed46db08906fd |

Current canonical note /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md has refreshed SHA2567b59fd7cf2b8d524b4f1478d883c71070856e9377f08b901864a44867ebc3d78. Root supplied commit dcb635da85dc22809a14ba815c2219431219c9e5; no Git verification occurred. Its new nominal disk refinement was read fully; earlier necessary nominal and compensated-precision arguments are reused from preceding complete reads. The checked positive-precision source/review are 233364359dc3e79b54debf331eb75e6454f093cdbec36c36e1ba4fe17acc1381 and40f7649071bc0eeb192a7832c64510c4185d39d31b6c27e9064a77fd5fa6a5f5.

Root supplied the fixed-spectrum candidate; this is source-exposed development, not independent discovery. I authored older weighted and disk work and reviewed the positive compensated contract and other components. The fixed-background perturbation report is used only within its stated scope, with simultaneous changes proved below rather than attributed to that report. No scientific execution, parameter search, new agent, model/effort change, W/Git/checkpoint/prompt edit occurred. Only reads, hashes and this proposal write occurred.

## 1. Exact physical family and parameter domain

Let kappa0=10^-8 and g=J-E0>.0239. The original local one-excitation block is [[E0,-kappa0],[-kappa0,J]], with vacuum value0 and double-occupation value E0+J. Preserve all four eigenvalues and choose the real rotation branch connected to the original block, with negative off-diagonal -kappa_a. Its entries are

    [[E0+Delta,-kappa_a],[-kappa_a,J-Delta]],
    Delta=2s/[g+sqrt(g^2-4s)], s=kappa_a^2-kappa0^2.

For r in [1-10^-6,1], Delta<=0 and

    |Delta|<=kappa0^2(1-r^2)/g<8.4e-21,
    |Delta|/alpha0<2.6e-6, alpha0=kappa0^2/J.

Here J/g<.031/.0239<1.3. The endpoint's retained ordinary J bond makes its total diagonal2J-Delta. Therefore the ACTUAL background perturbation is delta_b=-Delta>=0, bounded by10^-20; the emitter diagonal is E0+Delta. Neither is zero. Positivity, reality, excitation conservation and nearest-neighbor locality hold on all four qubit states by the fixed spectrum. The vacuum value is unchanged, so there is no extra common scalar. The same literal old/source system and original product emitter seed are retained.

At these small orientations the equivalent occupation coefficients E0+Delta-kappa_a and J-Delta-kappa_a are positive, but they are an algebraic decomposition of the supplied block, not independently adjustable controls in this contract. The whole block is static after delivery.

## 2. Auxiliary reference and exact changed-background identities

It is convenient to introduce an AUXILIARY compensated device C_a with the same kappa_a and emitter energy E0+Delta, but endpoint diagonal2J. This lies within the already checked compensated contract. Its scalar reference is

    F_a=i kappa_a E' z^21 rho_g/[sqrt(2pi)J D_a],
    D_a=E-E0-Delta+(kappa_a^2/J)z,
    p_a=integral_I |F_a|^2 dk, f_a=F_a/sqrt(p_a).

The actual fixed-spectrum device differs from C_a by delta_b at the background endpoint. The auxiliary f_a will be a comparison packet, not falsely called the exact scalar reference for that changed background. The FINAL target remains the original nominal f0 and positive-normalized beta0, with its full common phase.

Let R,G,L,x_bg be nominal pre-emitter objects (independent of kappa_a and Delta), P the real eight-coordinate endpoint inclusion and H_b=(I-delta_b G)^-1. The actual objects satisfy

    R_b=R+delta_b RP H_b P^T R,
    G_b=G H_b, L_b=L H_b,
    R_bP=RP H_b,
    x_bg,b=x_bg+delta_b RP H_b P^T x_bg.           (1)

These exact identities include the complete outgoing complex row at its original plane and every background source coordinate. Transpose is not replaced by adjoint. With |delta_b|<=10^-20 and disk ||G||<36, ||H_b||<1+10^-18 and ||G_b-G||<1.3e-17. No real-axis whole-space resolvent norm is asserted.

For clarity, the actual scalar reference would contain

    A_b=1+(delta_b/J)z,
    D_b,ref=E-E0-Delta+(kappa_a^2/J)z/A_b,
    F_b,ref/F_a=D_a/(A_b D_b,ref).

The complex A_b factor is real physics, not a disposable phase. We do not omit it: the full L_b and Schur comparisons below charge the background effect directly against F_a, making it unnecessary to introduce another normalized target and contour.

## 3. Simultaneous real Schur and complex-profile estimates

Relative to C_a, both complementary blocks now already include Delta and kappa_a. Their bare gap is at least .18-|Delta|. With G or G_b the inverses remain<6 on the real band and disks, since .18-|Delta|-.062rho-36.000001 kappa_a^2>1/6. Thus the fixed-emitter perturbation algebra applies with these SAME shifted complementary blocks. It does not require setting Delta back to zero.

Writing s_b and s_c for the exact complementary Schur self-energies at these fixed (kappa_a,Delta), product subtraction gives, with e_G=1.3e-17,

    |s_b-s_c|<=e_G[1+432kappa_a^2+46656kappa_a^4]<1.4e-17.

The real Green derivative is <35001 and the full Schur derivative is

    |ds_b/dE|<=35001+kappa_a^2[2*35001*6*36+72*36^2]<36000.

The constant Delta has derivative zero. These conservative formulas retain all seven complementary coordinates; tiny cross blocks need not be set to zero.

For the profile let c_a=kappa_a^2 Dcc,c^-1 Gcj and c_b its changed-background counterpart. The same subtraction gives ||c_b-c_a||<7kappa_a^2 e_G. Since ||L_b-L||<1.2e-17, the emitted numerator changes by<1.3e-17. Real Delta cancels when comparing each actual Dj to D_a, so the compensated relative denominator bound<1/40000 remains valid. The background change adds at most

    |Dj,b-Dj,c|/|D_a|< (J/sin k)*1.4e-17<1.1e-18.

It follows that the full emitted coefficient of the actual device obeys

    |Fj,b/F_a-Fj,c/F_a|<2e-18.                   (2)

All kappa_a factors cancel in this relative comparison; no singular loss is hidden at r near1. The original ratio calculation has unrounded intercept<1.761e-13 and slope<750. Its retained coupling corrections are maximal at kappa0, and Delta cancels in the relevant comparison. Adding(2) leaves the advertised bound

    |Fj,b/F_a-omega_p|<2e-13+750|k-k0|.           (3)

This does not assert the old epsilon_G/epsilon_L separately unchanged against their untransformed nominal approximations. The change larger than those floors is charged by(2).

## 4. Mass, synthesis and complete static cost

The actual seed mean is c_new+b_j+E0+Delta and its variance is kappa_a^2. Recenter u=E-E0-Delta and take d_a=v sigma-|Delta|. The interval [Delta-d_a,Delta+d_a] lies inside [-v sigma,v sigma], and d_a>d(1-2e-12). Real center bounds A=35,B=17,b_min=12 persist by the explicit comparison to -z/J, the compensated shift bounds and the additional1.4e-17 self-energy change. They are not inferred merely from the coarse ||G_b||<35.000001.

The exact finite-interval mass lemma now uses kappa_a and s_b centered at Delta. With L=10^6 supplied by the derivative above, the same denominator smallness<4e-10, logarithm<18 and H<46 apply. The worst tail is<4.534e-8 and regularity term<3.067e-9. Hence actual omitted spectral mass<4.85e-8 and amplitude<.000221. All exterior point/singular/continuum mass remains charged. The auxiliary reference has its own normalized global seed measure and derivative<1334, yielding1-p_a<4.54e-8 independently of the actual background's spectral measure.

Actual real matching invertibility follows from the complementary inverse and resonant imaginary margin: the unrounded compensated factor>(1-1/40000)*.4/.031 is reduced by only1.4e-17 and remains>12. The unchanged open boundary supplies the rank-one Stone jump; smooth finite-support densities and nonsingular matching give local multiplicity-one synthesis by the same canonical argument. No global scattering completeness is assumed.

For the auxiliary restricted moment, |Delta|/alpha_a<2.600006e-6, safely within the positive-contract bound1.000021e-5. Thus |k-k0||f_a|<145kappa_a, ||(k-k0)f_a||<.21kappa_a, and(3) gives complex mismatch<1.6e-6. The preparation cost includes actual exterior amplitude, the reference normalization deficit, and the within-parity factor sqrt2<1.415. Actual real-seed reciprocity and unit-modulus actual reflection give outgoing cost<2delta, on orthogonal old output fibers. Therefore

    static error to auxiliary packet
      <1.415*(.000221+.0000016+.0000000454)+.0000032
      =.000318243241<.000319.                    (4)

Input coefficients on the old system/reference are never conjugated. Only the fixed scalar a0,j=conjugate(omega_p f_a) is used.

## 5. Complete source and contour at the conservative old onset

Use h=10^-18 and T=4e21, not the new nominal disk onset. Background perturbation formula(1), with the unrounded source bounds in its checked interface, gives uniformly

    ||R_bP||<4.1e11, ||x_bg,b||<2e9.

These background estimates depend on delta_b alone, not the emitter detuning or hopping. On the radius rho disks ||G_b||<36.000001. Cauchy and both complementary corrections give exact self-energy oscillation<.000038. Meanwhile .062h/kappa_a^2<.000621. Combining these with the real margin leaves ImDj,b>6kappa_a^2 throughout the strip. Dcc analyticity precedes this conclusion; no off-real unitarity is used.

The full eight-coordinate emitter inverse is<.18/kappa_a^2 on the bottom. Both cutoff sides retain

    |Dj,b|>=v sigma-|Delta|-.061h^2
             -kappa_a^2*36.000001-6kappa_a^4*(36.000001)^2
             >2.49e-8,

so there the inverse is<5e7. The source solve with V_b=[-kappa_a R_bP;I] keeps all904 coordinates. Its bottom C estimate is at most the nominal expression with1/kappa multiplied by1/r<1.000002, and remains<5e20 with ample margin. Its side estimate is<1.4e13. Actual R_inst=u^T x-1 is used in subtracting the open waves. The complete closed tails have the unchanged Qc roots<1/6, hence a holomorphic fixed-Hilbert-space tail map and ||C||<=3||x||+4.

The auxiliary a0 has the detuned conjugate denominator of the positive contract. Its imaginary sign remains exact with exp(-y), its bottom bound is .088/kappa_a and side bound44kappa_a/sigma. At T the complete localized bottom is<6.601e-9 and both sides together<=9.24e-8, including old-column aggregation. Thus localized error<1e-7.

The auxiliary incoming scalar contour retains h_i=sigma/2, and outgoing target h_o=kappa_a^2/(4J^2)>2.5e-14. Real detuning leaves the imaginary signs unchanged; cutoff margins survive subtraction of |Delta|. Phase113 remains in the outgoing decay rate. The checked positive-contract estimates give incoming<1e-10 and auxiliary target q_a<1e-10, including both edges; positive target normalization costs<1e-20. The nominal q0 also remains<1e-10. These scalar contours apply to the auxiliary packet; we do not pretend that the unneeded changed-background reference D_b,ref has the same simple denominator.

Consequently actual device error against auxiliary beta_a is<.000320 for t>=T. All background effects were included in actual synthesis, emitted ratio and C; using an auxiliary reference has not discarded an output term.

## 6. Fixed nominal target, radius and finite device

The compensated reference ratio is exactly F_a/F0=rD0/D_a, with full common rho_g and phase113. The crude ratio bound suffices without exploiting cancellation against delta_b:

    eta<=2.5[(1-r^2)+|Delta|/alpha0]<1.15e-5,
    ||f_a-f0||<=2[(1-r)+eta]/(1-eta)<.000026.

The fixed nominal beta0 is never redefined. Fourier evolution and half-line restriction are contractions; two positive-normalization adjustments cost at most q_a^2+q0^2<2e-20. Therefore

    actual complete infinite error against beta0
       <.000320+.000026+2e-20<.000347.

The comparator includes exp(-ic_new t), blank emitter/other-clock/source and exp(-itK)W on the literal old system with arbitrary passive reference. The common waveform difference introduces no extra sqrt2.

The physical one-head perturbation relative to nominal has two-site matrix [[Delta,-(kappa_a-kappa0)],[-(kappa_a-kappa0),-Delta]], with norm sqrt(Delta^2+(kappa_a-kappa0)^2)<1.1e-14. Vacuum and double occupation are unchanged. Hence the radius retains its large margin below18. The graph and first omitted distance M+23 are unchanged. For M=50T=2e23 the canonical transfer adds<.001 on[T,2T], so complete finite error<.001347 with M+116 total qubits and the SAME embedded infinite nominal target. No finite target renormalization or permanent storage is asserted. Unhalved trace ceilings are .000694 and .002694.

## Interpretation and outstanding review

The useful structural change is that a single supplied positive block with fixed eigenvalues enforces correlated hopping and both diagonal changes through one orientation parameter. Independent tuning of the two compensation occupations is no longer an additional datum within that family. However the two eigenvalues, especially the emitter-like low eigenvalue, remain precise supplied energy data. The product seed is not rotated with the block. Common scaling or eigenvalue drift generally produces first-order emitter detuning and is outside this theorem; no supplier or calibration mechanism is derived.

This proposal closes the simultaneous analytical chain at the conservative old T through explicit extension of the fixed-emitter interface, but that extension and the final composition still require independent checking. The crucial point is(2) at the shifted Dcc, retaining its unrounded ratio slack, and the distinction between the auxiliary compensated reference and actual changed-background scalar reference. Nothing here transfers the nominal shorter onset without additional proof. No native identification, general coefficient robustness, empirical performance, audit status or full-device numerical execution is claimed.

Orientation-domain clarification: the proved parameter condition is on the actual hopping ratio r, on the small branch connected to nominal. Equivalently theta_a=asin(r sin(2theta0))/2 with theta0=atan(2kappa0/g)/2. It does not grant an arbitrary absolute angular-error radius of order10^-13. An upper estimate on the width of this angular interval cannot be used as a sufficient error radius; a supplier must enforce the exact interval or a separately justified contained interval. No unfinished angular-tolerance calculation is used as evidence here.
