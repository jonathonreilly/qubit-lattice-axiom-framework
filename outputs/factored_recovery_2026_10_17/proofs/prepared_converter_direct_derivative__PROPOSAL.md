# Prepared converter recovery: differentiated physical feedback

Status: conditional author derivation requiring distinct checking. Conditional also on the PROVISIONAL original-core derivative source cfca9422, the actual two-converter-loaded OLD finite recovery satisfies

    ||d[Phi_old(E)P_new]/dE|| < 5.1e11.                 (1)

This map has the full172-head old output, including every internal and closed coordinate, for selected incoming amplitudes on either new port. It is not a bound on arbitrary complementary NEW-port incidence, the input-terminated source, the gate-loaded complete recovery L, or the resonant three-source derivative D3. No runtime or device improvement is asserted.

## 1. Domain and exact physical planes

Keep the original nominal converter, its exact supplier values, fixed record/parity sector and two old-energy windows. The new wave number obeys |q-pi/2|<=h<=4e-6, with the ORIGINAL physical map E=2j(1-cos q)=2J(1-cos k), .0027<j<.003 and .03<J<.031. The checked mapping gives |k-k0|<.96e-6, E_k'>.025 and E_q'>.0053. Thus

    |dk/dE|<40, |dq/dE|<189.

All derivatives below are PHYSICAL E derivatives unless a k subscript is written. Both ports have the SAME roots, fixed B projectors and converter. Old source scattering coefficients refer to origins m=0; the converter interfaces are at m=40. The old finite recovery Psi_B refers to incoming amplitudes at those OUTER planes. No reference-plane factors are discarded.

Use P,C for the two-port selected/complementary old channels. The checked source coefficients at the origins obey

    b=S_gen a, S_gen=T A^-1,
    ||S_PC||,||S_CP||<6e-12, ||S_CC||<6e-32.

The open S is unitary. The complete original-open scattering matrix moved to the outer planes is S_B=z^80 S, z=exp(ik), with ||(S_B)_k'||<894. Consequently ||S_B'||<35760<36000. This is the actual first scattering derivative, with both40-step phases and the original90-step phase already paid.

The exact closed converter return at the ORIGINAL origins is

    E_c=R_c Q_C^80,
    N=(I-S_CC E_c)^-1,
    b_C=N S_CP a_P,
    S_tilde=S+S_PC E_c N S_CP.                         (2)

Here R_c and Q_C are diagonal fixed-projector functions; S_gen need not commute with either. Keep the ordered products in (2).

## 2. Coarse derivative bounds justified by an actual complex domain

The canonical source provides analytic old-k disks |w-k|<=rho=1e-12 at EVERY real k in its certified interval. On these disks its explicit finite equations give

    ||M16^-1||<167, ||A||<41, ||A^-1||<22,
    ||T_g||<208, ||Q_C||<.15, ||z||<exp(rho),
    ||(I-G_filter V)^-1||<2100, ||V||<.05,
    ||Ttilde||<2e7.

These are proved complex-domain bounds, not extrapolations from small real reflection. Closed projectors are fixed and their signed physical roots continue analytically. The open continuation need not be unitary.

The physical original two-port T at the origins is the fixed real junction transform of the arm image coefficients propagated24 steps from the filter. All powers on these finite disks have norm at most exp(48rho)<1.001; closed powers only shrink. Even allowing a two-port block factor gives ||T||<4.1e7, hence

    ||S_gen(w)||=||T(w)A(w)^-1||<1e9.

Operator Cauchy on that disk, followed by the real physical chain rule, gives

    ||S_gen'(E)||< (1e9/rho)*40 =4e22.                 (3)

It applies to all its blocks, with no channel-count factor. This is intentionally extremely coarse: its only use will multiply tiny closed propagation factors. It is NOT used for the open scattering derivative.

We also need an analytic bound for the physical original recovery from CLOSED incidence at the outer planes,

    H_C(E)=G_old(O,B;E) A(E)^-1 C,

where B comprises the two outer sites. On these same disks the bare free/image blocks across the finite86-site unfolded arm range have norm<300. Contact-to-free rows follow from M16^-1 and the finite decaying/propagating powers and fit that ceiling. Each two-filter-column row therefore has norm<sqrt(2)*300<500. Woodbury gives a filtered physical block ceiling

    300+500²*.05*2100<2.7e7.

After the constant real junction mixing even a block factor2 leaves <1e8. Stacking the172-by2 boundary column costs at most sqrt(344)<19. Thus ||G_old(O,B;w)||<2e9, and

    ||H_C(w)||<5e10, ||H_C'(E)||<2e24.                 (4)

These statements concern finite physical coordinates, not infinite growing open waves off the real axis. They also do not apply Cauchy to an unspecified whole-space resolvent. The real value remains the much sharper checked ||H_C||<160. All powers have been combined before the finite-coordinate norm; (4) introduces no growing closed-incidence propagation.

## 3. Differentiate closed feedback without dropping it

For a closed old root a and new root w, the exact converter has

    R_c=-N_c/D_c,
    N_c=J-j-Ja+J S0 w,
    D_c=J-j-J/a+J S0 w.

The alternative denominator expression D_c=epsilon-J-j+J S0 w+Ja is used to differentiate: epsilon'=1. The unchanged real bounds are |a|<=1/7, |w|<1/60, |D_c|>.1797 and |N_c|<1.152J<.0358. Canonical |a_k'|<.125 and dk/dE<40 give |a'|<5. For the new closed root,

    |w'|=|w|²/[j(1-|w|²)]<.104.

Therefore |N_c'|<.157, |D_c'|<1.157, and quotient differentiation proves

    ||R_c'|| < .157/.1797+.0358*1.157/.1797²<3.         (5)

Both signs of the closed roots are covered. No inverse-root derivative is bounded separately by a potentially huge norm.

Since 7^40>1e32, and derivatives of fixed-projector powers have their usual exact scalar form,

    ||E_c||<2e-65,
    ||E_c'|| <=3*7^-80+.2*80*5*7^-79<6e-62.           (6)

The inverse N in (2) has ||N||<2, and

    N'=N(S_CC' E_c+S_CC E_c')N,
    ||N'||<4[(4e22)(2e-65)+(6e-32)(6e-62)]<4e-42.    (7)

Differentiate all four factors in S_PC E_c N S_CP. Equations (3),(6),(7) and the real cross values in section1 bound its derivative by <1e-51 (the first and last terms are each <1e-53). Its real value is <1e-86. Moving it to the outer open planes adds at most80*40*1e-86. Thus

    S_tilde,B=z^80 S_tilde,
    ||S_tilde,B'||<36001,
    ||S_tilde,B||=1.                                  (8)

The real unitarity in (8) follows from exact flux conservation with real closed loads, not from deleting the closed correction. A bound 1+1e-86 would yield the same constants.

## 4. Differentiate the OPEN incidence with the velocity factor

For a fixed selected two-new-port input alpha, write u=z^-40 a_P, its old OPEN incoming amplitude at the outer planes. Exact converter composition gives

    u=(I-r_o S_tilde,B)^-1 eta_c alpha,
    eta_c=t_c sqrt(v_new/v_old),
    eta_c=e^(iq) sqrt(j S0/J) [sin q/sin k](1+r_o).     (9)

Equation (9) follows from the physical flux transmission. It retains the first-new-site phase exp(iq); it is not an amplitude obtained by setting both velocities equal. The original factor z^40 in the origin equation cancels when forming u, whereas the round-trip z^80 remains in S_tilde,B.

On the enlarged band |r_o|<4.88e-6, and the exact converter numerator/denominator have q derivatives <.029, denominator >.024-.029h>.0239998. Thus

    |r_o'| < [.029*189/(.0239998)](1+4.88e-6)<230.    (10)

The multiplier eta_base=e^(iq)sqrt(jS0/J) sin q/sin k has norm<.5. Its logarithmic derivative is i q'+cot(q)q'-cot(k)k'. With |cot q|<5e-6, |cot k|<2.5, q'<189 and k'<40,

    ||eta_base'||<.5(189+.001+100)<145,
    ||eta_c'||<145(1+4.88e-6)+.5*230<300.             (11)

Flux conservation gives |t_c|<=1, so ||eta_c||<.49. Hence ||u||<.49/(1-4.88e-6)<.5. Differentiate (9) with alpha fixed:

    u'=(I-r_o S_tilde,B)^-1
       [eta_c' alpha+(r_o' S_tilde,B+r_o S_tilde,B')u].

By (8)–(11),

    ||u'||<1.000005[300+(230+4.88e-6*36001)*.5]<500.  (12)

There is no arbitrary inverse3e10 in this estimate.

For the origin coefficients a_P=z^40 u,

    ||a_P'||<40*40*.5+500=1300.                       (13)

This explicit phase derivative matters in the closed equation (2).

## 5. Closed outer incidence and its recovered derivative

From (2), the real values give ||b_C||<3e-12 for ||alpha||<=1. Differentiating b_C=N S_CP a_P using (3),(7),(13) gives

    ||b_C'|| <=||N'|| ||S_CP|| ||a_P||
               +||N|| ||S_CP'|| ||a_P||
               +||N|| ||S_CP|| ||a_P'|| <4.1e22.     (14)

This very large coefficient derivative is harmless only after its physical propagation is retained. The actual complementary incoming amplitude at the OUTER plane is

    v=R_c Q_C^40 b_C,
    v'=R_c' Q_C^40 b_C+R_c(Q_C^40)'b_C
                                        +R_c Q_C^40 b_C'.

Indeed the origin incoming coefficient is R_c Q_C^80 b_C, and evaluating its growing wave at m=40 cancels exactly40 powers. We never norm these two factors separately. Since ||(Q_C^40)'||<=200*7^-39=1400*7^-40,

    ||v||<.2*7^-40*3e-12<1e-44,
    ||v'||<3*7^-40*3e-12
           +.2*1400*7^-40*3e-12
           +.2*7^-40*(4.1e22)<8.3e-11.              (15)

Paying the real value ||H_C||<160 and the actual complex-domain derivative (4) now yields

    ||(H_C v)'||
      <=(2e24)(1e-44)+160*(8.3e-11)<1.4e-8.          (16)

Thus the closed contribution is bounded, not declared zero. Equations (14)–(16) include every complementary direction and all output rows of the original physical recovery.

## 6. Actual prepared old finite recovery and remaining scope

At the same outer planes the exact decomposition is

    Phi_old P_new=Psi_B u+H_C v.                      (17)

The provisional direct original-core source supplies ||Psi_B'||<1e12; the separately checked dwell bound gives ||Psi_B||<30. Combining (12),(16),(17) proves

    ||(Phi_old P_new)'||
        <(1e12)*.5+30*500+1.4e-8<5.1e11.

This proves (1) conditional on that pending direct-core check. All bounds are ordinary operator norms on the selected incoming domain, with full finite-output fiber. They hold separately on both physical windows and each parity/record sector; fixed real conjugation gives the other lip, and arbitrary passive-reference tensoring preserves the estimate. No derivative of input vectors is taken.

Wrong-window and other complementary OUTPUT coordinates are retained in (17). Arbitrary COMPLEMENTARY incident new-port columns are NOT covered by (1). They cannot be silently replaced by this prepared bound in an endpoint-forced map. Any subsequent use on full endpoint forcing must retain its complementary coefficient and derivative and a separate full complementary recovery bound. Similarly this task does not impose the input cap or wide-gate feedback; their coefficient derivatives remain necessary to obtain a full L'. The three-source resonant D3 is a distinct remaining obligation.

No complex-domain calibration of converters was assumed: their derivatives were obtained directly from real physical equations. Cauchy was used only for explicitly bounded original finite matching/Green quantities on the canonical disk. No small real-axis reflection, closed value or dwell norm was converted into a derivative without that step.

## Exact sources and exposure

- PROVISIONAL prepared_core_direct_derivative/PROPOSAL.md: cfca9422163b4f4694a2efddbbff6779bd3c354bbd505e90af4d16189d1e40be. Its original-core derivative1e12 is an explicit open dependency pending distinct check, not certified by this composition.
- prepared_core_recovery/PROPOSAL.md: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9, with selective dwell check88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 and composition check52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c. Unchanged value scope reused.
- bandcenter_converter_composition/PROPOSAL.md: 1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78, with checkf1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c. Complete source refreshed for both directions, physical flux, closed feedback and reference planes.
- bandcenter_bandwidth_extension/PROPOSAL.md: d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2. Complete source refreshed for the enlarged band, converter inverse1.000005 and unchanged original certification.
- Original canonical endpoint note: 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. Physical/filter and actual complex-disk passages175–319 and1386–1518 were fully refreshed in the preceding direct-core task; those exact premises are reused. No whole-note recalibration or new independent audit is asserted.

I authored the preceding direct-core derivative and checked several shared ancestors. Root requested this exact continuation and read the preceding artifact, whose distinct check is still pending. The new converter differentiation is author work requiring its own check, particularly complex finite-coordinate bounds (3)–(4), origin/outer phase conversion, the actual velocity factor in (9), and the closed40-power derivative in (15).

Only this proposal was written. No sweep, numerical inverse, dynamics, solver, scientific runner, W/Git/PR/checkpoint/prompt/model change or delegation occurred. No full-device derivative, runtime, permanent halt or native coefficient-supply result is claimed.
