# Full recovery derivative: improved output-port factor, retained old-core bottleneck

Status: new conditional author derivation requiring distinct checking. On the unchanged nominal wide-band background, a safe full-forcing derivative bound is

    ||L'(E)|| <1.00068[7.253e16+1.28e6/g]+30.          (1)

This includes every235 finite background head and every slow closed tail, with the full eight-dimensional endpoint-forcing domain. The improvement is chiefly in the slow-root derivative term, whose previous coefficient was3.31e7. The large old-core direct action remains bounded by its earlier checked estimate. The selected converter derivative5.1e11 is not silently promoted to a bound on that full action.

No runtime, receiver length, complete-output error or physical implementation claim is selected. The source itself is not included in L. Nominal Delta=0 is retained; no common-mode/source-tolerance transfer is made.

## 1. Domain and checked values

Keep .0027<j<.003,0<g<=1e-6,0<h<=4e-6,d=2j sin h,d/g<=1/2 and the original supplied graph, coefficients, internal B, preparation identification and scalar c_att. Work on each original physical window, parity and record-X sector, both lips, and the entire fixed eight-coordinate forcing fiber. All derivatives are PHYSICAL E derivatives; old/new wave-number derivatives require their respective chain rules.

Let U be the211 upstream heads after input deletion:193 old/input heads and18 cable heads. Let G be the24 gate heads. The exact emitter-free recovery F=R V_p has checked disjoint value ceilings

    old172:<7900, input21:<6000, cable18:<9000,
    gate plus all closed slow tails:<3270,
    ||F_U||<14000, ||F_G||<3270, ||F||<14000.          (2)

The last finite norm is obtained from the full square-sum bound190102900<14000², not from summing the separate rounded ceilings. The propagating stationary ray is excluded from L and treated separately in actual Fourier synthesis.

The newly checked converter derivative is

    ||(Phi_old P_new)'||<5.1e11.

Its check explicitly completes the closed coefficient margin with

    ||N_closed||<1.000001,
    ||u||<.490003,
    ||b_C||<1.000001*(6e-12)*.490003<3e-12.

The coarser N<2,u<.5 alone would not prove that last bound. This tightened value step is retained whenever that converter result is reused. Its domain is selected new-port incidence with FULL old finite output, not arbitrary complementary incoming data or endpoint forcing. The original-core derivative1e12 now has its distinct check as well; neither remains provisional. Neither new derivative is needed for the safe numerical full bound (1), for the reason exposed in section5.

## 2. A smaller COMPLETE last-cable Green column

Use the input-terminated, but gate-unloaded, kernel G_D at last cable site a=v17. Its exact noncable block is

    G_D(U_noncable,a)=K_U A_n Q_n^17.

The checked dwell propagation/input-cap result gives ||K_U P||<33, while the complete complementary map retains ||K_U||<2e18. Also ||A_n P||<200,||A_n C||<6.18 and ||Q_n,C||<1/60. Thus

    ||G_D(U_noncable,a)||
       <33*200+(2e18)*6.18*60^-17<6601.              (3)

The second term is below1.1e-11, using60^17>1.2e30. It is not set to zero. Equation (3) covers arbitrary forcing at a: P and C here split its input, and all output coordinates remain.

On cable n=0,...,17, the exact kernel is

    G_D(n,a)=A_n Q_n^(17-n)+Q_n^n S^D A_n Q_n^17.

The already checked full complementary coefficient bound ||S^D||<2e8 and selected bounds |S^D_PP|=1,||S^D_CP||<2 give each block<801 and the entire cable stack<4005. The outgoing closed term near n=0 is included; it is not suppressed there by pretending n=17. Combining disjoint ranges,

    ||G_D(:,a)||=||G_D(a,:)||
        <sqrt(6601²+4005²)<8000=:C_a.                 (4)

Transpose symmetry in the fixed real basis proves the row norm equality. All closed growing powers have already canceled in the exact physical column. The diagonal bound ||G_D(a,a)||<401 remains unchanged. There is no use of a selected scalar bound as a complete inverse.

## 3. Exact gate update and restored output-port column

The actual24-head gate inverse R_g with its slow ray eliminated obeys

    ||R_g||<33/j, j||R_g e_p||<6.28.

At a the update is D_g=-jQ_n-j²G_g, G_g=e_p^T R_g e_p, with ||D_g||<.102. Its exact physical plane is important: the reflection at a is rho=Q_n² r_gate, and the return at v0 is Q_n^36 r_gate. The checked full feedback factorization and closed bounds give

    ||(I+G_D(a,a)D_g)^-1||<4.6,
    ||R_u(:,a)||<4.6 C_a=36800,
    ||R_u(a,a)||<4.6*401<1845.                        (5)

The reversed product has the same norm bound by transpose reciprocity. Closed feedback is retained in these full-fiber estimates; |r_gate,C| is never assumed uniformly small before its propagation factors.

Restoring gate coordinates, with positive off-diagonal j in E-H,

    R_UG=-R_u(:,a)j e_p^T R_g,
    R_GU=-R_g e_p j R_u(a,:),
    R_GG=R_g+R_g e_p j R_u(a,a)j e_p^T R_g.

Therefore

    ||R_UG||=||R_GU||<36800*6.28=231104<240000,
    ||R_GG||<33/.0027+6.28²*1845<86000.              (6)

For the actual slow-output inclusion V_o, its upper component is bounded by231104, since j||e_p^T R_g V_o||<=6.28. Its lower component is bounded by86000. The physical ranges are orthogonal, so

    ||R V_o||<sqrt(231104²+86000²)<250000.             (7)

This is a FULL output column on the full internal forcing domain; no actual input restriction has been imposed. It replaces the previous6.5e6 output-column factor. The value argument, not an unproved derivative of the gate scattering coefficient, supplies the improvement.

## 4. Retain the checked old-core action and bound the full derivative

The exact converter lift and input deletion use

    G2=diag(0,D_n)+J_lift G_c J_lift^T,
    G_D=G2(ret,ret)-G2(ret,b)Z^-1G2(b,ret), b=input21.

The transpose lift, the full deletion block Z and all finite coordinates are retained. With the actual endpoint-forced F_U extended by zero at b, the checked direct-action bounds give

    ||J_lift^T F_U||<163000,
    ||G2 F_U||<6.944e16,
    ||G2(b,:)F_U||<9.84e8,
    ||G_D F_U||<6.944e16+130000*24*(9.84e8)
                     <7.252e16.                     (8)

In (8), G_c acting on the structured lift still uses its arbitrary-forcing norm3e10. This is the retained unresolved component, not a claimed consequence of the selected Phi derivative.

The exact gate update applied to this forcing adds at most C_a²*.102*4.6*||F_U||. With (4),

    ||R_u F_U||<7.252e16+8000²*.102*4.6*14000.

Restoring all gate components and using (6),(2), a safe triangle bound is

    ||R F||<7.252e16+8000²*.102*4.6*14000
                   +240000*(14000+3270)+86000*3270
             <7.253e16.                              (9)

No orthogonality of two physical energy-window error maps is assumed; this is a per-window full forcing-domain norm.

Now differentiate the assembled physical equation, not any value inequality:

    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T,
    M(E)F(E)=V_p,
    F'=-R F-j R V_o Q_slow' V_o^T F.                 (10)

All restored finite coefficients, including the input cap, converters and gate, are energy independent in H_finite. Hence (10) differentiates all their implicit propagation and feedback factors exactly. There are no missing derivatives of those factors; they are descriptions of R, not extra coefficients in M. The slow selfenergy coefficient is j=tau²/g for tau=sqrt(jg).

The checked all-channel slow-root derivative satisfies ||Q_slow'||<1/(1.93g). With ||V_o^T F||<3270 and (7),(9),

    ||F'||<7.253e16+(.003*250000*3270)/(1.93g)
           <7.253e16+1.28e6/g.                       (11)

The closed slow tails have exact lift T_C(E) from the finite output value, built from their nonnegative decaying powers. Its checked norm is <.00068 and derivative norm<.009, obtained by differentiating the powers and summing their geometric square series. It follows directly by the product rule that

    ||L'|| <=||F'||+||T_C V_o^T F'||+||T_C' V_o^T F||
            <1.00068||F'||+.009*3270,

which proves (1). This accounts for every closed tail. The infinite propagating stationary wave has no square-summable recovery norm and is not included in L.

Both physical lips obey these equations separately by fixed real conjugation. The full internal forcing domain includes selected and wrong-window prepared inputs and all other complementary directions. Arbitrary passive-reference tensoring preserves the estimates. No whole-H commutation with K, scalar phase removal or actual spectral normalization is used.

## 5. Why the selected derivative does not yet replace (8)

The existing cap equations are explicit. For endpoint forcing before the gate,

    alpha=A_n Q_n^20 B_br,
    B_br=I-Q_n Z^-1 Q_n(A_n+X),
    X=Q_n^20 T_n,aa Q_n^20,
    Z=A_n+Q_n X Q_n.

The old finite response is Phi_old,in alpha. On selected output incidence the cap instead imposes alpha_in=-Q_n^42 beta_in with beta=S_n alpha. With the actual gate attached, at v0 one has

    b=S^D a+B_e f, a=R_return b,
    b=(I-S^D R_return)^-1 B_e f.

These equations are full fiber and retain their stated order. Differentiating them is legitimate, but requires the actual derivatives of Z, X, B_br, S^D, B_e and R_return. For example,

    (Z^-1)'=-Z^-1 Z' Z^-1,
    alpha'=A_n' Q_n^20 B_br+A_n(Q_n^20)'B_br
                                            +A_n Q_n^20 B_br',
    b'=(I-S^D R_return)^-1
             [B_e' f+(S^D'R_return+S^D R_return')b].

At finite input site n the closed incoming product must remain A_C Q_C^(20-n) C B_br, not Q_C^-n multiplied by an unstructured tiny alpha_C bound. For a cap return it remains -Q_C^(42-n)beta_C. Cable incoming products likewise combine the physical36-step return with Q^-n before differentiation. Derivatives of these canceled products, including their coefficients, are owed even when their real values are tiny.

The checked5.1e11 estimate controls (Phi_old P)' and all its output rows. In (Phi_old alpha)' it pays only

    (Phi_old P)'P alpha +Phi_old P P alpha',

while (Phi_old C)'C alpha+Phi_old C C alpha' remain. The small real C alpha does not alone bound those terms, and P alpha' is not supplied by the value bound400. Similar obligations occur after the gate return. The full assembled estimate(10)–(11) safely pays them via(8); it does not erase them.

Thus the immediate bottleneck for a substantially smaller g-independent constant is still G_c J_lift^T F_U, equivalently a complete structured cap/return derivative analysis with every complementary product retained. The present task does not assign invented numerical ceilings to those missing products. It does provide a complete bound by retaining the existing checked action for precisely that part, while reducing the actual slow-boundary factor through the physical column(4).

The separately checked D3 result concerns the resonant prepared cubic inverse. It neither replaces(8) nor implies a bound on L'. Conversely(1) alone is not a full temporal theorem: any IBP application must include D3, hard endpoints, both physical windows/lips, actual outside state and the traveling pieces. No operating point is chosen here.

## Sources, exposure and verification limits

- prepared_core_recovery/PROPOSAL.md: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9; checks88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 and52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c. Full value and exact-action arguments reused at unchanged identities.
- prepared_core_direct_derivative/PROPOSAL.md: cfca9422163b4f4694a2efddbbff6779bd3c354bbd505e90af4d16189d1e40be; check75563597ec6edd1b688bfd81b51b4dc5b1adab7033d9f78a860f759cf5e70729.
- prepared_converter_direct_derivative/PROPOSAL.md: a444e105c88fcfad8fcae59b7f72d9dd9247e2b83ada73edeb7b97a849b33653; its distinct check, fully read in this task, supplies the sharpened N/u step for b_C<3e-12. Verified check SHA256: 283494e3a50b12b77bf9d4be184452b49b582627fac20c802087e00e4d69e11d. This selected derivative is not a quantitative premise for(1).
- slow_lead_wide_derivative/PROPOSAL.md: c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a; checkc74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79. Full gate update, root derivative, restored block formulas and closed-tail lift scope reused.
- record_attached_recovery_sharp/PROPOSAL.md: 07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11. Complete exact cap/endpoint/cable equations refreshed; its narrower gate constants are not imported as wide bounds.
- bandcenter_converter_endpoint/PROPOSAL.md: 22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a. Complete matching/deletion argument refreshed for order; enlarged-band margins come from the separately checked wide sources, not its historical narrower numerical constants.
- Original physical/calibration source remains71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff, within the inherited matching/B/source premises.

I authored the direct-core/converter and wide-derivative sources and checked several recovery ancestors. Root requested extension to full recovery and explicitly allowed retaining genuinely unresolved components. This is exposed author work, not an independent review of those ancestors. The new column refinement(3)–(7), gate action accounting(9), and full-domain use in(10)–(11) require a distinct check. The old3e10 action is retained honestly, not proved necessary or optimal.

Only this proposal was written. No numerical inverse, solver, integration, sweep, dynamics, scientific runner, W/Git/PR/checkpoint/prompt/model change or delegation occurred. No runtime, new native supplier or permanent halt claim is made.
