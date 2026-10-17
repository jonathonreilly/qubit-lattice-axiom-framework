# Slow-output attached device: full endpoint comparison and seed mass

Status: new authored conditional derivation, requiring a distinct check. The gate/load dependency's separate review arrived during drafting and supports its unchanged source; this new endpoint/mass composition remains unchecked. At the fixed kappa=1e-8, slow hopping g=1e-6 and unchanged q halfwidth h=4e-6, the proposed actual modified-device bounds are

    ||G_slow,x-G_free||<1e-48+1.5e6 u,
    ||G_slow,x||<407,
    ||G_slow,x-G_ref||<8e-18+1.51e6 u,
    u=|q-pi/2|, G_ref=-Q/j.                        (1)

These are FULL eight-coordinate background endpoint matrices in every old parity, physical energy window and conserved record-X sector x. The emitter selected Schur denominator and full inverse obey

    |D_x|>.98 sqrt(delta^2+gamma^2),
    Im D_x>326 kappa^2,
    ||De_x^-1||<1.03/sqrt(delta^2+gamma^2),
    delta=E(q)-2j, gamma=kappa^2/j.                 (2)

For the actual four-old-input seed, including supplied coherent record0 and arbitrary passive references, the resulting omitted spectral bounds on the common union of both physical windows are

    0<=M_actual(R outside I)<1.66e-6 I_4,
    ||E_Hslow(R outside I)V_seed||<.00129.          (3)

The old actual mass/runtime constants are not inputs. The comparison uses a genuine mathematical reference of independent j chains, not the transmitted slow scalar packet's norm. Outgoing/incoming slow profiles, full record1 recovery and any temporal or finite theorem remain separate obligations.

## Sources, exposure and provisional dependency

Read the complete new `../slow_lead_gate_load/PROPOSAL.md`, SHA256 `c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d`. Its distinct review was not available at this drafting stage. Its full real-band gate inverses, old-plane open return, sector-difference bound, signed closed roots and finite recovery are explicit PROVISIONAL premises here. A downstream use must qualify this dependency; this composition does not independently validate that author's new gate argument.

Dependency update before finalization: I then read COMPLETE `../slow_lead_gate_load_check/REVIEW.md`, SHA256 `8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65`. It supports the unchanged c1e1fe95 source without correction, including its actual finite inverse, both-origin scattering, closed return and .9937 feedback-interface margin. References below to the provisional gate premises identify the original drafting exposure; they are now separately checked conditional inputs, not unreviewed assumptions. This update does not independently validate the new endpoint, density or mass argument written here.

Refreshed complete earlier `record_attached_emitter_bound/PROPOSAL.md`, SHA256 `2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9`, and complete mass source `record_attached_seed_mass/PROPOSAL.md`, SHA256 `be7ff80c9667e80dd87d104e9bd03766b5fa14265deecab0a9b800278579a3dc`. I authored both; they are used for exact unchanged upstream formulas and reference identities, not as independent checks of the new result. Their distinct reviews `30bb3f38752c5d6fc2b036042315c7ccb82f2f932805e04476e9a886822b6fa3` and `e3e40799fe208c336612c9f35805051f4fde468772cb9f0e7796be1835780999` were previously completely read and remain the qualification of that unchanged material.

Reuse the completely read corrected matrix-measure interface `e1abe3233bfe4b0e3d5e623240df9df9e80a35f7f3d081ab3e41944f06c6dd5d`, its review `825c69bad1436e83523b2d901325ee2661c6128cd6fd73d4ee77a1bf2b6f5712`, exact scalar reference check `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`, and wider source `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`. The original calibration, finite source inverses, exact correlated coefficients and real B basis remain inherited conditional premises at canonical note `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff` and converter note `f8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311` through those sources.

Root requested actual changed-device endpoint and mass estimates after the scalar and gate work. The task and proposed premises were exposed. This is author mathematics, not independent review of itself. Applicable unchanged workflow is reused. No scientific execution, numerical sweep, dynamics, solver, delegation, W/Git, checkpoint, prompt, model, audit or publication change occurred. Only this deliverable was written; no editable prompt file changed.

## 1. Common physical windows and unchanged upstream objects

The modified slow path preserves one-head onsite diagonal 2j and introduces no vacancy scalar, so c_att is unchanged. Define the SAME physical windows for all inputs and both record sectors:

    I_b=[c_att+b+2j-d,c_att+b+2j+d], b=1,3,
    d=2j sin h<2.4e-8, I=I_1 union I_3.

Remove only c_att from physical energy, writing lambda=Lambda-c_att. On I_b let delta=lambda-b-2j=-2j cos q with q in pi/2+[-h,h]. Then u<=|delta|/.0053. These disjoint windows remain strictly inside the selected slow continuum because d<2g. The seven other B channels have old roots |Q_C|<1/60 and slow roots |v_C|<1/160000 by the provisional gate source. This is a classification on chosen windows, not a prior mass assertion.

At v0=(82,1,1), the upstream apparatus ends in the same free j-lead reference before the new gate load is imposed. The whole input-terminated, emitter-free upstream objects are unchanged:

    S=T^D A^-1, ||S||<2e8, |S_PP|=1,
    B_e=T_ba Q^20[I-QZ^-1Q(A+X)], ||B_e||<3e6,
    ||P B_e||<400,
    K_e=B_e^T A^-1, ||K_e||<6.3e7,
    ||K_e P||=E'_q||P B_e||<2.4,
    ||G_free||<400.

Here A=[j(Q-Q^-1)]^-1, P is the selected real B projection and C=I-P. Right multiplication in S and the transpose in K_e retain their actual order; P is not commuted through upstream matrices. The selected row has scalar approximation P B_e=ell P+E_L, ||E_L||<1e-23. The free endpoint has complementary and cross errors <1e-24 relative to -Q/j, and selected comparison

    |(G_free)_PP+w/j|
       <742(1e-20+12u)+1e-24.                    (4)

These are properties BEFORE attaching either record load. No former loaded endpoint estimate is substituted for the new one.

## 2. Ordered new load feedback

Move the new gate's input reflection back along its unchanged eighteen-edge cable. Write its selected return r_x=w^36 R_left,x and its closed return C_x. The new gate source supplies

    |r_x|<=1540u<=.00616<.0062,
    |r_+-r_-|<=68u,
    ||C_x||<1e-63,
    ||C_+-C_-||<2e-63.                            (5)

The selected sector difference is genuinely smaller than twice the individual reflection, but the individual bound is needed for conditioning. No closed-sector cancellation is asserted. The full boundary equations are b=S a+B_e f, a=(r_x P+C_x)b. Define

    N_x=(I-S_CC C_x)^-1,
    S_eff,x=S_PP+S_PC C_x N_x S_CP,
    B_eff,x=P B_e+S_PC C_x N_x C B_e,
    K_eff,x=K_e P+K_e C C_x N_x S_CP,
    F_c,x=K_e C C_x N_x C B_e.

Closed elimination first gives ||N_x||<2 and the same controlled closed allowances

    |S_eff,x-S_PP|<8e-47,
    ||B_eff,x-P B_e||<2e-48,
    ||K_eff,x-K_e P||<3e-47,
    ||F_c,x||<4e-49.

These follow from the unchanged source norms and the newly supplied closed return, not from equal old/new closed matrices. The exact new endpoint is

    G_slow,x=G_free+K_eff,x f_x B_eff,x+F_c,x,
    f_x=r_x/(1-S_eff,x r_x).                      (6)

Only the selected f_x is scalar. Its denominator has NEW margin

    |1-S_eff,x r_x|>1-(1+8e-47)*.0062>.9937.

The former .99986 margin is not retained. Since (2.4+3e-47)(400+2e-48)/.9937<967, equations (5)–(6) give

    ||G_slow,x-G_free||<967*1540u+4e-49
                         <1.5e6u+1e-48.

The old absolute endpoint401 ceiling is not reused: the new bound is ||G_slow,x||<407 on this band.

For later sector-sensitive applications, keep the exact identity

    f_+-f_-=[r_+-r_-+r_+r_-(S_eff,+-S_eff,-)]
                      /[(1-S_eff,+r_+)(1-S_eff,-r_-)].

The closed allowances give sector differences bounded by twice their listed ceilings. Expand the product difference in (6) as DeltaK f_+ B_+ + K_- Deltaf B_+ + K_- f_- DeltaB, plus DeltaF_c. The linear contribution is below 961*68u/.9937^2<67000u. The remaining terms are bounded by

    (6e-47)*(.0062/.9937)*401
    +2.5*(.0062/.9937)*(4e-48)
    +961*(.0062^2)*(1.6e-46)/.9937^2+8e-49
       <1e-45.

Hence the ACTUAL full sector endpoint difference obeys

    ||G_slow,+-G_slow,-||<1e-45+67000u.             (7)

This smaller sector comparison is separate from the larger individual deviation relevant to seed mass.

## 3. Full reference comparison, complements and emitter

The real selected-row relation gives

    ||C K_eff,x||<7e-26, ||B_eff,x C||<2e-23.

Using |r_x|<.0062 and denominator>.9937 in (6), its PC correction is below 4e-25 and its CP correction below 2e-25. Its CC correction is below 5e-49. Adding the unchanged free errors therefore preserves

    ||(G_slow,x)_PC||,||(G_slow,x)_CP||<2e-24,
    ||(G_slow,x)_CC+Q_C/j||<2e-24.                 (8)

These are full block norms for all seven complementary directions, including the other vacuum old energy. They are not single-entry bounds. Combining (4), the individual update in (1), and all blocks in (8) gives

    ||G_slow,x+Q/j||<a+b_u u,
    a=8e-18, b_u=1.51e6.

Indeed the unrounded selected slope is at most 1.5e6+8904=1508904, and the full constant including complement/cross allowances is below 8e-18. In energy coordinates this gives

    ||G_slow,x-G_ref||<a+b_delta |delta|,
    G_ref=-Q/j, b_delta=2.85e8,                   (9)

since 1.51e6/.0053<2.85e8. The nonzero floor is retained. No worst-band relative error is substituted for this integrable profile.

Attach the unchanged emitter. Its exact full inverse matrix is

    De_x=(lambda-2j)I-B-kappa^2 G_slow,x.

Complementary bare distances exceed .185, so (1) yields ||Dcc_x^-1||<6. The selected Schur selfenergy and denominator are

    g_eff,x=G_PP+kappa^2 G_PC Dcc_x^-1 G_CP,
    D_x=delta-kappa^2 g_eff,x.

The complementary correction is below 24kappa^2*1e-48 by (8). The unused slack in (9) covers it without changing the displayed a,b_u. Consequently

    |D_x-Dref|<kappa^2(8e-18+1.51e6u),
    Dref=delta+gamma w.

Relative to Im Dref=gamma sin q this is less than

    j(8e-18+1.51e6u)/sin q<.019.                  (10)

The original .0005 relative bound is not reused. Since Dref=delta[1-kappa^2/(2j^2)]+i gamma sin q and both real scaling factors exceed .9999, (10) implies

    |D_x|>.981|Dref|>.98 sqrt(delta^2+gamma^2),
    Im D_x>.981 gamma sin q>326kappa^2.

The full block inverse, retaining all off-diagonal multipliers, then obeys

    ||De_x^-1||
      <=(1+12e-24 kappa^2)^2/[.98 sqrt(delta^2+gamma^2)]+6
      <1.03/sqrt(delta^2+gamma^2),                 (11)

using sqrt(delta^2+gamma^2)<2.5e-8. This proves the new real-band emitter margins without substituting a center-only inverse into an energy integral.

If needed, the exact complementary inverse difference is kappa^2 Dcc_+^-1(DeltaG)_CC Dcc_-^-1. Expanding the two ordered quadratic selfenergies and using ||G_x||<407 bounds the effective sector difference by [1+4884kappa^2+36*407^2*kappa^4]||DeltaG||. Thus a safe consequence of (7) is |g_eff,+-g_eff,-|<2e-45+68000u. It is not used to replace the individual comparison (9).

## 4. Genuine reference and actual density

The comparison reference remains four independent equal-diagonal j emitter chains, one for each old vacuum vector, shifted by literal b=1,3 and common c_att. It is a real self-adjoint comparison operator, not a claim that the changed actual lead still has hopping j. Each reference seed measure has mass one, is purely absolutely continuous, and has support [c_att+b,c_att+b+4j]. The b=1 and b=3 reference supports are disjoint. Thus on I_b the other old-energy reference density is zero, while its real resolvent is still included.

For algebra extend this reference to one j chain for each B eigenvalue within each parity. Its exact endpoint matrix is -Q/j and its full emitter denominator is

    Dref,8=(lambda-2j)I-B+kappa^2 Q/j.

Compression to the two vacuum coordinates in each parity gives exactly the four intended reference seed chains. Their mass on the COMMON union I is M_ref(I)=p0 I_4, with 1-p0<1.1e-6 from the exact reference integral. The six extra reference channels per parity are mathematical comparison coordinates, not extra physical source qubits. Neither the transmitted slow scalar mass p_s nor an old actual mass certificate is used.

The reference full inverse still obeys ||Dref,8^-1||<1.01/r_delta, r_delta=sqrt(delta^2+gamma^2): its selected denominator has the factors above and its seven closed diagonal inverses remain <6. The exact noncommuting identity

    De_x^-1-Dref,8^-1
       =De_x^-1[Dref,8-De_x]Dref,8^-1

combined with (9),(11), and 1.03*1.01=1.0403<1.05 yields

    ||De_x^-1-Dref,8^-1||
       <1.05 kappa^2(a+b_delta|delta|)
                                  /(delta^2+gamma^2). (12)

Compress to the full two-vacuum-coordinate seed space in each parity; contractivity preserves (12), including its off-diagonal old-energy entries. The two exact parity blocks combine by a maximum. Therefore (12) is a full four-input seed-resolvent comparison on each common physical window, not four disconnected scalar comparisons.

Local spectral regularity is established conditionally by the NEW full inverse chain: unchanged original source/converter/input-deletion matrices, provisional changed gate/load inverses, closed-return inverse, selected new feedback margin>.9937 and full emitter inverse (11). They recover every finite source, cable, gate and emitter coordinate. The one actual infinite slow path has selected velocity 2g sin k>1.99e-6 and seven closed roots separated from thresholds; the entire closed window lies inside its one open band.

At every real point through both cutoffs the actual root branches have analytic local continuations and the full finite matching determinant is nonzero. Its inverse therefore extends locally; compactness gives bounded continuous boundary values for the seed matrix. This excludes hidden in-band finite kernel modes and yields the actual absolutely continuous matrix seed density

    dM_x/dLambda=-(1/pi) Im[V_vac* De_x^-1 V_vac]

on I, with no seed atoms or singular-continuous component there, including cutoffs. This relies on complete recovery/nonzero matching, not on an open reflection alone. No quantitative complex strip or temporal bound is asserted. If the provisional gate argument or an inherited complete source inverse fails, this regularity and the mass result must be reopened. Outside I all spectral types remain possible and are charged below.

## 5. Full matrix integration and omitted state

The genuine reference is also absolutely continuous on I, including endpoints. Operator imaginary part is norm-contractive, so integrating (12) gives a full four-input density error on EACH physical window bounded by

    eta_b <(1.05kappa^2/pi)
        [2a arctan(d/gamma)/gamma
                   +b_delta log(1+d^2/gamma^2)].   (13)

This pays the opposite vacuum input and every off-diagonal seed entry on the same physical interval. No additional velocity Jacobian belongs in this ENERGY integral. The slow k Jacobian is needed for outgoing wave synthesis, not for this resolvent-density formula.

At the fixed parameters d/gamma<720000 and log(1+d^2/gamma^2)<28. The existing elementary logarithm witness applies unchanged because d and gamma are defined by the original input/emitter j. The constant part of (13) is below 1.05 j a<2.52e-20. Using pi>3, the slope part is less than

    (1.05/3)*1e-16*(2.85e8)*28=2.793e-7.

Thus eta_b<2.8e-7. There are TWO physical integration windows, so eta_I<5.6e-7. No extra parity or four-column factor is needed because the integrand is already a complete matrix norm; taking only one window would be invalid.

Exact total seed normalization and the Loewner density comparison give, in each record-X sector,

    M_x(I)>=p0 I_4-eta_I I_4,
    0<=M_x(R outside I)<(1.1e-6+5.6e-7)I_4
                              =1.66e-6 I_4.

The squared norm of the omitted seed embedding equals the norm of this positive matrix. Since .00129^2=1.6641e-6, its amplitude is strictly below .00129. For initial record0 the sector embeddings have weights 1/sqrt(2) and their output ranges are orthogonal; their omitted squared norms average, preserving the same operator ceiling. This is not a cancellation assumption. Both sectors use identical physical windows and c_att. Passive reference tensoring preserves the bound, and later record projection is contractive.

The conclusion (3) charges all actual outside mass, including possible bound states. It does not equate actual density to a transmitted reference wave or drop opposite-window inputs. The larger mass allowance relative to the previous device is a derived consequence of the changed common reflection and full density integral, not a transfer of an old constant.

## Scope and next check

This candidate establishes real-band endpoint/emitter bounds and an actual conditional full seed-matrix mass estimate for the changed infinite device. Its load-bearing gate/load dependency is now qualified by the distinct review pinned above; this new composition itself still requires checking. The next checker should inspect the ordered feedback, improved sector subtraction separately from individual conditioning, survival of tiny complementary blocks, full reference identification and local regularity, and two-window integration.

No actual slow-ray W profile, incoming comparison, complete record1 local estimate, all-time herald theorem, concentration onset, finite resource success guarantee or native supplier claim follows here. The independently derived scalar slow packet and its onset are not actual-device premises in this mass proof. Original old aging and source interactions remain inside the exact matrices throughout.
