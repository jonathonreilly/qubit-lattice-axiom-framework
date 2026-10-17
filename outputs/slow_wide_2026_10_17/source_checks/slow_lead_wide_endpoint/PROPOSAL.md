# Wider receiver band: actual endpoint, full emitter and seed matrix mass

Status: new conditional spectral interface requiring a distinct check. The wider-gate source 5b667173 was provisional at initial drafting; its distinct check is now complete and has been read in full. This note does not independently validate that gate argument. Conditional on it and the unchanged exact source premises, the actual full8 endpoint comparison is

    ||G_x-Gref||<8e-18+46000u+290|delta|/g,
    Gref=-Q/j, ||G_x||<550.                           (1)

The complete reference, actual emitter conditioning and two-window matrix density integration are derived below. No outgoing-wave, runtime, finite-success or native-supply theorem is imported. A parameter-dependent mass bound is the final result, without selecting a performance target.

## Domain, physical windows and exposure

Keep the supplied nominal old source, its exact calibration and two converters, input cap, cable and record gate. Let

    .0027<j<.003, 0<kappa<=1e-8,
    0<g<=1e-6, 0<h<=4e-6,
    d=2j sin h, d/g<=.5,
    gamma=kappa^2/j, H=d/gamma.

The sharper emitter/density constants stated below additionally assume H>=100, as in the earlier family. This implies L=g/gamma>=2H>=200. The endpoint and the weaker emitter fallback do not need H>=100. The emitter is attached with the same real structured positive block, retaining its exact diagonal2j. The slow connector and compensations retain every diagonal and c_att.

For ALL old inputs and both record sectors use the SAME physical union

    I=I_1 union I_3,
    I_b=[c_att+b+2j-d,c_att+b+2j+d], b=1,3.

On I_b remove c_att and write lambda=b+2j+delta, delta=-2j cos q, u=|q-pi/2|. Then u<=|delta|/.0053. The selected slow root is open with sin k>=sqrt(15/16), and the seven other channels remain closed with old roots<1/60 and slow roots<1/160000. This is channel classification on I, not an actual seed-mass assertion.

I authored the new wider-gate proposal and earlier derivative/publication material, and previously checked several older components. Root requested this endpoint extension and exposed the desired spectral interface. I refreshed the full fixed emitter proof and reuse the unchanged fully read endpoint, matrix-measure and uniform-source ancestry within its scope. This is author derivation, not independent checking, and the wider-gate dependency is now supported within its local scope by the distinct check pinned below. No sweep, scientific execution, model change, delegation, W/Git/publication/checkpoint or frozen-source edit occurred.

## 1. Ordered background update with the new conditioning margin

Before imposing the record-gate return, the unchanged terminated source supplies

    ||S||<2e8, |S_PP|=1,
    ||B_e||<3e6, ||P B_e||<400,
    ||K_e||<6.3e7, ||K_e P||<2.4, K_e=B_e^T A^-1,
    ||G_free||<400, A=[j(Q-Q^-1)]^-1.

Its selected row satisfies P B_e=ell P+E_L, ||E_L||<1e-23. Its complementary/cross endpoint errors relative to -Q/j are<1e-24, and its selected comparison is

    |(G_free)_PP+w/j|<742*(1e-20+12u)+1e-24.           (2)

These are unloaded source identities; no old loaded endpoint error is reused. The source need not commute with P or K. All matrices act on the complete forcing fiber.

The provisional wider gate (with its checker-requested center-strictness correction preserved in its v1 history) gives selected return r_x at v0 with

    |r_x|<.129,
    |r_x|<=33u+.262|delta|/g,
    |r_+-r_-|<=85u,
    ||C_x||<1e-63, ||C_+-C_-||<2e-63.                (3)

The returns include the actual18-edge cable and its36-power round trip. The closed raw reflection is not assumed bounded before its propagation powers are paid.

Closed elimination in b=S a+B_e and a=(r_x P+C_x)b uses exactly

    N_x=(I-S_CC C_x)^-1,
    S_eff,x=S_PP+S_PC C_x N_x S_CP,
    B_eff,x=P B_e+S_PC C_x N_x C B_e,
    K_eff,x=K_e P+K_e C C_x N_x S_CP,
    F_c,x=K_e C C_x N_x C B_e.

The unchanged coarse full-source norms and new closed return still give ||N_x||<2 and allowances

    |S_eff,x-S_PP|<8e-47,
    ||B_eff,x-P B_e||<2e-48,
    ||K_eff,x-K_e P||<3e-47,
    ||F_c,x||<4e-49.

They do not require the old individual open reflection. The actual endpoint is

    G_x=G_free+K_eff,x f_x B_eff,x+F_c,x,
    f_x=r_x/(1-S_eff,x r_x).                          (4)

Its NEW denominator is>.8709. Consequently

    ||G_x-G_free||<1103|r_x|+4e-49,
    ||G_x||<400+1103*.129+4e-49<550,                 (5)

since (2.4+3e-47)*(400+2e-48)/.8709<1103. The old967 multiplier and407 absolute endpoint ceiling are not reused.

For later record-sensitive use, the exact scalar subtraction is

    f_+-f_-=[Delta r+r_+r_- Delta S_eff]
                     /[(1-S_eff,+r_+)(1-S_eff,-r_-)].

Expanding the full ordered product difference in(4), the coefficient of u is<961*85/.8709^2<108000. The remaining terms are bounded by

    (6e-47)*(.129/.8709)*401
      +2.5*(.129/.8709)*(4e-48)
      +961*.129^2*(1.6e-46)/.8709^2+8e-49<1e-44.

Hence

    ||G_+-G_-||<1e-44+108000u.                       (6)

This is distinct from the larger individual deviation that governs mass.

## 2. Full complements and the calibration floor

The actual selected-row relation and its transpose imply

    ||C K_eff,x||<7e-26, ||B_eff,x C||<2e-23.

Now |f_x|<.129/.8709<.149. Thus the new PC update is<2.5*.149*2e-23+4e-49<7.5e-24, its CP update is<7e-26*.149*401+4e-49<4.2e-24, and the CC update is<7e-26*.149*2e-23+4e-49<7e-49. Adding the unloaded bounds gives

    ||G_PC||,||G_CP||<1e-23,
    ||G_CC+Q_C/j||<2e-24.                            (7)

The old2e-24 CROSS ceiling is not retained. All seven complementary coordinates, including the other prepared vacuum energy, are included.

Combine(2),(3),(5) and the full complementary bounds. The unrounded selected coefficients are

    1103*33+8904=45303<46000,
    1103*.262=288.986<290.

The leading constant is742*1e-20=7.42e-18 from the original supplied source/calibration reflection floor. The additional1e-24 unloaded error, closed-feedback constants and full complementary/cross sums are far smaller than the remaining .58e-18 slack. Thus (1) holds with the SAME nonzero floor8e-18 for an explicit reason, not because an earlier mass theorem was copied. Define

    a=8e-18, b(g)=46000/.0053+290/g.

Then

    ||G_x-Gref||<a+b(g)|delta|.                       (8)

This floor is a supplied original calibration/source allowance, not an error caused by finite output storage or an adjustable phase.

## 3. Actual emitter: separate imaginary and modulus conditioning

Attach the actual emitter and define

    De_x=(lambda-2j)I-B-kappa^2 G_x,
    Dcc_x=C De_x C,
    g_eff,x=G_PP+kappa^2 G_PC Dcc_x^-1 G_CP,
    D_x=delta-kappa^2 g_eff,x,
    Dref=delta+gamma w.

Complementary bare gaps exceed .185. Equation(5), kappa<=1e-8 and the exact block structure give ||Dcc_x^-1||<6. Its selected quadratic correction is<6e-46*kappa^2 by(7). The strict slack in(8) absorbs this into the same a,b(g) envelope for g_eff+ w/j.

First bound the imaginary part without using H>=100. The pre-rounded individual comparison (5) and(2) give

    |g_eff+w/j|<1103*.129+742*(1e-20+12*4e-6)+tiny
                    <142.33.

Since sin q>=cos(4e-6),

    |D_x-Dref|/Im Dref<j*142.33/sin q<.43,
    Im D_x>.57 gamma sin q>189 kappa^2.              (9)

This proves positive actual broadening; relative modulus conditioning alone would not prove it. It also gives the wider-domain fallback |D_x|>.57|Dref|>.569r_delta, where r_delta=sqrt(delta^2+gamma^2). Explicit full Schur reconstruction then gives ||De_x^-1||<=(1+6e-23*kappa^2)^2/(.569r_delta)+6<1.8/r_delta, since r_delta<2.5e-8. This fallback is proved under the same provisional gate and source premises, not independently certified.

For the family with H>=100 a much better MODULUS estimate is available. Do not replace the energy-resolved error by its maximum relative to the small imaginary part. Equation(8) instead gives

    |D_x-Dref|/r_delta
       <theta:=j a+kappa^2 b(g).

Because L=g/gamma>=2H>=200,

    theta <=j a+kappa^2*(46000/.0053)+290j/L
             <.004351.                              (10)

The exact reference modulus satisfies |Dref|^2=(1-kappa^2/j^2)delta^2+gamma^2, hence |Dref|>.9999r_delta. Therefore

    |D_x|>.9955r_delta.                              (11)

Full Schur reconstruction, including both off-diagonal multipliers, gives

    ||De_x^-1||
      <=(1+6e-23*kappa^2)^2/(.9955r_delta)+6
      <1.01/r_delta,                                (12)

using r_delta<2.5e-8. The1.01 is a new derived constant under the explicitly stronger H premise. It does not assert a better imaginary margin than(9).

For completeness, the exact cross inverse blocks satisfy

    T_CP=Dcc^-1*kappa^2 G_CP/D_x,
    T_PC=kappa^2 G_PC Dcc^-1/D_x,
    ||T_CP||,||T_PC||<7e-23*kappa^2/r_delta.

The CC block is Dcc^-1 plus the ordered quadratic Schur correction. The wrong-window prepared vacuum column has a real O(6) complementary reference response; it is NOT claimed uniformly tiny or removed. The full matrix comparison below pays its density error, including every off-diagonal prepared entry.

If desired, expanding the two quadratic effective selfenergies bounds their difference by [1+6600kappa^2+36*550^2*kappa^4]||DeltaG||. A safe record-sensitive consequence of(6) is |g_eff,+-g_eff,-|<2e-44+109000u. It is not substituted for the individual comparison(8).

## 4. Genuine full reference, absolute continuity and density

For algebra use one independent equal-diagonal j emitter chain for EVERY B eigenvalue in each parity, shifted by that eigenvalue and c_att. This is a genuine self-adjoint mathematical comparison operator, not the actual slow lead and not a transmitted packet. Its full emitter denominator is

    Dref,8=(lambda-2j)I-B+kappa^2 Q/j.

Compression to the two prepared vacuum directions per parity gives the four intended reference chains, with old energies1 and3. Their two distinct continuum supports are disjoint. On I_b the opposite old reference density is zero, but its real resolvent remains in the full matrix subtraction. All reference seed measures have total mass one. Let p0 be their exact common mass on I; no old ACTUAL mass is used.

The reference full inverse obeys ||Dref,8^-1||<1.01/r_delta, retaining its seven complementary denominators. The exact noncommuting subtraction is

    T_x-Tref=T_x*kappa^2(G_x-Gref)*Tref.

Equations(8),(12) therefore give on the full8 space

    ||T_x-Tref||
       <1.021*kappa^2*(a+b(g)|delta|)/(delta^2+gamma^2), (13)

since1.01^2=1.0201<1.021. Without H>=100, the fallback from(9) instead supplies the valid looser factor1.82=upper ceiling on1.8*1.01. Both alternatives have explicitly stated hypotheses.

Conditional on the provisional gate result, the complete matching chain is nonzero on each closed window: original source/filter/converters, input deletion, full closed return, selected>.8709 feedback, and full actual emitter Schur inverse. These reconstruct every finite coordinate. The actual selected slow velocity is at least2g*sqrt(15/16)>0 for every fixed positive triple, while all closed roots avoid thresholds. Analytic local root branches and the nonzero finite determinant give continuous boundary values on a neighborhood of every window point, including its cutoffs. The actual seed matrix measure is therefore absolutely continuous there, with

    dM_x/dLambda=-(1/pi) Im[V_vac* T_x V_vac].

This is a finite matching/seed measure argument, not a continuation of the whole infinite resolvent across its spectrum. It excludes hidden in-window seed singular mass under the complete inverse premises. No uniform complex strip or temporal rate follows. Outside I, all spectral types remain possible and are charged below. Failure of the provisional gate proof or an inherited source inverse reopens this conclusion.

## 5. Full four-input matrix mass on the common window union

Operator imaginary part and vacuum compression are norm contractions. Integrating(13) in ENERGY on each physical window yields

    eta=(1.021*kappa^2/pi)*
       [2a atan(H)/gamma+b(g)log(1+H^2)].             (14)

This controls the complete two-vacuum-coordinate matrix in each parity, including the opposite-window input and off-diagonal entries. Parity blocks combine by maximum. There is no slow momentum Jacobian in this energy-density integral and no extra four-column factor.

For an explicit exact reference mass let A0=2j-gamma, alpha=gamma/A0 and y=tan h. The cotangent integral gives

    p0=4kappa^2/[pi A0^2(1-alpha^2)]
                           *[atan(y/alpha)/alpha-h].

Alternatively its exact tail obeys 1-p0<=4kappa^2/[pi A0^2 tan h]. These are new parameter evaluations of the genuine reference, not transmitted mass p_s. They retain its full total normalization and possible actual outside atoms remain separate.

There are TWO physical windows, hence

    M_x(I)>= [p0-2eta] I_4,
    0<=M_x(R outside I)
       <=min{1,1-p0+2eta} I_4,
    ||E_actual(R outside I)V_seed||
       <=sqrt(min{1,1-p0+2eta}).                     (15)

The same common union and same c_att are used in both record-X sectors. Initial record0 has orthogonal sector outputs with weights1/sqrt2, so their squared omitted norms average and preserve (15). Passive references preserve the operator ceiling. This is an actual full-seed mass bound conditional on matching, not a scalar-profile normalization substituted for actual density.

For the domain without H>=100, use1.82 instead of1.021 in(14); the same genuine p0 and matrix argument give a valid, possibly weak fallback. Even on the sharper family, (15) need not meet a desired accuracy at every triple. No numerical operating point or success target is selected here.

## Remaining obligations and check targets

The coherent result is the wider-domain full endpoint comparison, positive emitter imaginary margin, sharpened full emitter modulus bound under H>=100, actual local spectral regularity, and explicit full four-input omitted mass. All are conditional on the pending distinct wider-gate check and unchanged original exact source premises. This source also requires its own distinct check.

Actual outgoing and incoming coefficient estimates must be rederived with the new load, emitter and complement constants, preserving the exact transmitted amplitude, phase and slow Jacobian. The wider scalar contour/profile estimates and parameter-dependent full local recovery/derivative integrals also remain separate. Neither earlier fixed error/runtime, old .9937 feedback, old complementary cross2e-24, nor transmitted reference mass is an input to(15). Exact finite compression remains a structural tool, not a performance theorem for this changed device.

Check especially the ordered closed elimination, constant8e-18 provenance, the increased complementary cross ceiling, separation of positive imaginary conditioning from energy-resolved modulus conditioning, and two-window full matrix integration. A norm bound on individual prepared diagonal entries would not establish the stated result. Literal old aging, complete apparatus outputs and supplied initialization/record identification remain owed in any later temporal theorem. No new physical axiom, native calibration supply, permanent halt, publication or retained audit status is asserted.

## Exact source identities

- `slow_lead_wider_receiver_band/PROPOSAL.md`: `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`.
- `slow_lead_emitter/PROPOSAL.md`: `53916c906eda8cd5a1c8c6228c54002f4f74fe7986bee301d3162124d40544c0`.
- `slow_lead_emitter_check/REVIEW.md`: `23c228886a96e29071beabf5e3ae1f6c9caee8544eee4e5b5ddc38f854fda707`.
- `slow_lead_uniform_endpoint/PROPOSAL.md`: `c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887`.
- `slow_lead_uniform_endpoint_check/REVIEW.md`: `f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0`.
- `record_attached_emitter_bound/PROPOSAL.md`: `2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9`.
- `record_attached_seed_mass/PROPOSAL.md`: `be7ff80c9667e80dd87d104e9bd03766b5fa14265deecab0a9b800278579a3dc`.
- `record_attached_seed_mass_check/REVIEW.md`: `e3e40799fe208c336612c9f35805051f4fde468772cb9f0e7796be1835780999`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
- `bandcenter_reference_measure_check/REVIEW.md`: `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`.

Original canonical source calibration/kernel pin: `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. Source identities are not scientific proof or blanket independent recertification. The completed wider-gate review is local dependency evidence only, not an independent check of this endpoint/emitter/mass argument.

Dependency update: the complete wider-gate check `slow_lead_wider_receiver_band_check/REVIEW.md`, SHA256 `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`, was read after the original endpoint draft. It supports corrected gate source5b667173 without changing its local scope. Earlier provisional/pending wording records drafting exposure; the new endpoint, emitter and mass conclusions still require their own distinct check. Exact initial endpoint source5d927676 is preserved as PROPOSAL_v1.md. No mathematical inequality changed in this update.
