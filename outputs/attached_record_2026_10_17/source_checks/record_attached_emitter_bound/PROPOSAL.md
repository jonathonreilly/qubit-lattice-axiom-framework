# Real-band attached endpoint bounds with full closed feedback

Status: new authored conditional estimate, awaiting independent checking. For the frozen eighteen-edge record-gate attachment, each selected old-energy/parity band q=pi/2+[-h,h], h=4e-6, and each conserved record-X sector s=±, the FULL eight-coordinate background endpoint Green matrix obeys

    ||G_att,s-G_free|| < 1e-48+32000u,
    ||G_att,+-G_att,-|| < 1e-47+64000u,
    ||G_att,s||<401,                 u=|q-pi/2|.       (1)

These are at the input endpoint where the emitter is subsequently attached. The background includes the original source, both converters, terminated input, eighteen-edge output cable, full record gate and infinite final output, but NO emitter. All seven complementary source coordinates remain. The strictly positive floors are closed-return bounds, not zero-center assertions.

For the actual supplied emitter kappa=1e-8, its seven-coordinate complementary inverse remains<6. The exact selected emitter Schur denominator D_s satisfies

    |D_s-Dref|<.0005 Im Dref,
    Im D_s>329kappa²,
    |D_s|>.99 sqrt(delta²+(kappa²/j)²),
    delta=E(q)-2j, Dref=delta+(kappa²/j)exp(iq).        (2)

The full emitter inverse is<1/(300kappa²). Its selected effective self-energy g_eff,s, including complementary Schur correction, has sector difference

    |g_eff,+-g_eff,-|<2e-47+65000u
                       <=2e-47+1.23e7|delta|.        (3)

These supply concrete real-band denominator and difference inputs. They do not transfer an old actual mass, temporal escape, complete output or herald theorem to the attached device. In particular, scalar selected estimates alone do not establish the complete four-input matrix spectral comparison.

## Sources, exposure and inherited premises

Read COMPLETE ../record_attached_kernel/PROPOSAL.md at the tasked identity fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457. Its attachment/interface check was pending during this derivation, so its frozen geometry and exact load formulas are explicitly provisional dependencies. The formulas needed below are also reconstructed sufficiently to expose their reference-plane and matrix-order uses. No favorable status label substitutes for them.

Read COMPLETE W/docs/NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md at verified SHA256f8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311. Here W is the correlation_worktree. Its portable source packet at outputs/bandcenter_converter_2026_10_17/source_checks contains the previously completely read endpoint proposal22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a, endpoint check200268709480f1533050f5d197a4bed7a2acaefa5f4a22a662938ddb504619c6 and final wider-band proofd79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2. These exact packet identities were verified; the necessary full-kernel, input deletion and outgoing-row passages were refreshed. PR9674 is provenance supplied by root, not remotely verified here.

The unchanged original source calibration, fixed real B spectral projections, full finite-core inverse/recovery, original k band and wider-band inclusion remain conditional inherited premises. No old mass or runtime conclusion is used. The local record proposal93445d7d and checkc5f3e1d7 were completely read previously and remain the source of the literal mixer/phase-cell coefficients and |r_s|≤33u.

I authored earlier weighted-profile checks, the initial wider-band extension and the isolated gate positivity proposal; I did not author the attachment kernel. This is a new exposed derivation, not an independent check of itself or blanket recertification of that ancestry. Root supplied the target self-energy question and later mentioned a separate provisional center-inverse/recovery bound26/j; that result is NOT used below. Applicable unchanged workflow is reused. No scientific execution, numerical sweep/solver, delegation, W/Git/checkpoint/prompt/model edit or publication occurred. Only source reads/hashes and this deliverable; no editable prompt file changed.

## 1. Common reference plane and background partition

Use the SAME new-output origin v0=(82,1,1) as the converter's new-port kernel. The gate input p=(100,1,1) is eighteen ordinary-j edges from v0. The retained cable consists of v0,...,v17, with p the next vertex. The record-gate reflection moved to the v0 plane is

    R_s=Q^18 r_gate,s Q^18,

diagonal in the fixed B eigenbasis. In the selected open direction P, R_s has scalar entry r_s^load=w^36 r_gate,s, w=exp(iq), and |r_s^load|≤rho=33u≤1.32e-4. In the seven complementary directions C=I-P the return is the signed decaying-root power s_l^36 times its actual gate reflection. This is a boundary incoming/outgoing relation a=R_s b at v0, not a second added free input lead or an extra cable self-energy on top of the same partition.

On the source side retain the complete original two-converter apparatus with input deleted after ell=20 but emitter removed. Its remaining output is free when defining the comparison kernel. This is exactly the inherited background with endpoint diagonal2j. The emitter structured block allows that background diagonal independent of kappa. The common added c_R is already removed from the complete spectral parameter; it is not present again in this old core. The physical comparison still owes c_att=c_total+c_R.

Write the inherited two-port kernel using A=[j(Q-Q^-1)]^-1 and coefficients T_ab. On the full selected eight-dimensional fiber,

    ||A||<200, ||A^-1||<21, ||T||<600,
    ||Q||<=1, ||Q_C||<1/60,
    X=Q^ell T_aa Q^ell, Z=A+QXQ,
    ||A+X||<201, ||Z^-1||<24.

These constants survive the4e-6 band by the final wider-domain proof. All matrices are complex symmetric in the fixed REAL internal basis, but generally do not commute.

## 2. Original one-output source blocks after input termination

Dirichlet deletion at the input vertex ell+1 gives the remaining output image coefficient

    T^D=T_bb-T_ba Q^(ell+1) Z^-1 Q^(ell+1) T_ab.

Thus ||T^D||<600+600²*24<9e6. Its generalized source scattering matrix at v0 is

    S=T^D A^-1,                  ||S||<2e8.           (4)

RIGHT multiplication follows by comparing the incoming coefficient A Q^n and outgoing coefficient T^D Q^n of a remote forcing column. It is not permissible to replace this by A^-1 T^D. With all external closed components decaying and exactly one output propagating channel, real-axis flux conservation gives |S_PP|=1. The inherited full finite inverse excludes a singular background solution; this unit-modulus statement is not inferred for S_CC or the full generalized S.

Let B_e be the FULL outgoing output coefficient produced by unit endpoint forcing in any of its eight coordinates:

    B_e=T_ba Q^ell [I-Q Z^-1 Q(A+X)],
    ||B_e||<600(1+24*201)<3e6.                        (5)

It is the full endpoint-to-output Green block at output origin v0. Its selected outgoing row is the previously bounded L=P B_e; the exact scalar approximation and epsilon_L=1e-23 give

    ||P B_e|| < 1/[j(1-4.81e-5)]+1e-23 <400.        (6)

This norm uses real-axis |t|≤1, j>.0027 and the unchanged endpoint inverse margin; it does not assume exact source transmission/calibration.

For prescribed incoming amplitude a at v0, the recovered endpoint amplitude is K_e a with

    K_e=B_e^T A^-1,                ||K_e||<6.3e7.

The transpose is justified by the complex-symmetric retarded Green kernel in a fixed real basis. Since P is real and A^-1 P=iE'(q)P,

    ||K_e P||=E'(q)||P B_e||<.006*400=2.4.           (7)

This small SELECTED-column bound is crucial. Using the crude6.3e7 on the open channel would produce an unusable estimate. It neither deletes the complementary columns nor assumes they obey the selected bound.

The unperturbed full endpoint matrix has ||G_free||<400 and the previously established scalar approximation g_ref=-w/j with

    |(G_free)_jj-g_ref|*j/sin q <1e-4.               (8)

For (8), the direct bound is2r0/[(1-r0)sin q]+j epsilon_G/sin q, r0=1e-20+12u and epsilon_G=1e-24. The positive original reflection/closed floor is retained; no exact center calibration is invoked.

## 3. Gate real inverses and the small CLOSED return

The provisional attachment formula supplies the literal24-site gate h_s, the two-lead Schur matrix D2=z-h_s+js(z)(P_p+P_o), and the one-output load matrix DR=z-h_s+js(z)P_o. The closed-channel row bound is elementary on the inherited gap:

    ||h_s-2jI||<=(2+sqrt(2))j,
    |z_l-2j|>60j, |s_l|<1/60,
    ||DR(z_l)^-1||, ||D2(z_l)^-1||<1/(56j).

This bounds all seven channels, including the signed root above the lead band. It does not rely only on below-band positivity. In particular g_s=e_p^T DR^-1 e_p has |g_s|<1/(56j). The exact matching reflection

    r_gate,s=(-1-j s_l^-1 g_s)/(1+j s_l g_s)

then gives, writing a_l=|s_l|,

    |a_l^36 r_gate,s|
       <=[a_l^36+a_l^35/56]/(1-a_l/56)
       <3*60^-36<1e-63.                             (9)

For the last loose bound,60^6>4*10^10 gives60^36>4^6*10^60>4*10^63. This pays the1/a_l factor BEFORE the cable attenuation. Define r_C,s as the full diagonal closed return at v0; (9) gives ||r_C,s||<e_C=1e-63. It is a nonzero uniform ceiling even at q=pi/2.

On the selected open channel, existence of D2^-1 follows directly from the literal graph. If D2 v=0 at real0<q<pi, its imaginary part forces both port components to vanish. The two port equations and invertible mixer U then force both arm-end components to vanish. The terminal-arm recurrences have nonzero nearest-neighbor hoppings and successively force all remaining components to vanish. Thus the finite D2 has no kernel.

Removing the input self-energy from D2 gives DR=D2-jwP_p. Its Sherman denominator equals

    1-jw (D2^-1)_pp=-(1+w² r_gate,s)/(w²-1).

Here r_gate,s=j(w-w^-1)(D2^-1)_pp-1. Since |r_gate,s|≤33u<1, the denominator is nonzero. Thus the actual open load exists throughout this real band as well. This is an existence argument, not an invented uniform whole-gate recovery norm. The new provisional26/j estimate is unnecessary for (1).

## 4. Ordered full-fiber source/load elimination

For endpoint forcing f, the background equations at v0 and the recovered endpoint are exactly

    b=S a+B_e f,
    a=R_s b,
    response_endpoint=G_free f+K_e a.

All8 source/closed coordinates are present. Write r=r_s^load, C_s=r_C,s and

    N_s=(I-S_CC C_s)^-1.

By (4),(9), ||S_CC C_s||<2e-55, hence ||N_s||<2. Eliminating closed b_C BEFORE selected open b_P gives

    S_eff,s=S_PP+S_PC C_s N_s S_CP,
    B_eff,s=P B_e+S_PC C_s N_s (C B_e),
    K_eff,s=K_e P+(K_e C) C_s N_s S_CP,
    F_closed,s=(K_e C) C_s N_s (C B_e),

and the EXACT endpoint update

    G_att,s-G_free
      =K_eff,s r(1-S_eff,s r)^-1 B_eff,s+F_closed,s.  (10)

The order follows from b_C=N_s(S_CP r b_P+C B_e). No source/load matrices are commuted; only the selected open r and S_eff are scalars.

The bounds above imply

    |S_eff,s-S_PP|<8e-47,
    ||B_eff,s-P B_e||<2e-48,
    ||K_eff,s-K_e P||<3e-47,
    ||F_closed,s||<4e-49.

Thus the selected return denominator has explicit margin

    |1-S_eff,s r| >=1-(1+8e-47)rho>.99986.           (11)

Using (6),(7),

    ||G_att,s-G_free||
      <[(2.4+3e-47)(400+2e-48)/.99986]rho+4e-49
      <962rho+4e-49 <32000u+1e-48.

This proves the first inequality of(1) including its center floor. Taking the difference of the two exact attached matrices by triangle inequality proves the sector ceiling1e-47+64000u. It is deliberately conservative and assumes no sector phase cancellation in the closed floor. Each sector update is<.129 on the band, so ||G_att,s||<401. No enormous source norm multiplies the open return; the sharp selected endpoint row and its dual are what make this useful.

The construction gives actual full background endpoint matching in both sectors, conditional on the original core and frozen attachment formulas. It does not attempt to certify real-axis regularity merely by bounding an open scattering probability: closed inverses, gate inverses and the selected return denominator have all been retained.

## 5. Actual emitter denominator and sector effective self-energy

Reattach the supplied equal-diagonal emitter with kappa=1e-8. In either sector,

    De_s=(lambda-2j)I-B-kappa² G_att,s.

The seven complementary bare distances exceed .185 on the real band. Perturbation norm is<401kappa², so ||Dcc_s^-1||<6. Define the exact scalar self-energy and denominator

    g_eff,s=(G_att,s)_jj
         +kappa²(G_att,s)_jC Dcc_s^-1(G_att,s)_Cj,
    D_s=delta-kappa² g_eff,s, delta=E(q)-2j.

The plus sign and matrix order in g_eff follow from the full emitter Schur complement; none of its seven complementary coordinates is dropped. Comparing with Dref=delta+(kappa²/j)w and using(8),(1) gives

    |D_s-Dref|/Im Dref
       <1e-4
        +j(1e-48+32000u)/sin q
        +6j kappa² 401²/sin q
       <.0005.                                    (12)

Indeed the middle term is<.000385 and the last<3e-13 on u≤4e-6, j<.003 and sin q≥cos(4e-6). This leaves explicit margin rather than relying on old unattached emitter constants. It proves Im D_s>329kappa² and the relative modulus bound |D_s|>.9995|Dref|.

Writing gamma=kappa²/j, one has exactly

    Dref=delta[1-kappa²/(2j²)]+i gamma sin q.

The bracket and sin q are each>.999 on this band, hence |D_s|>.99 sqrt(delta²+gamma²). Full block inversion, with off-diagonal norm≤401kappa² and complementary inverse<6, gives

    ||De_s^-1||
       <=(1+2406kappa²)²/(329kappa²)+6
       <1/(300kappa²).

This retains all emitter directions and makes the weak-coupling resonance explicit.

For the sector effective self-energy difference, let DeltaG=G_att,+-G_att,-. The complement inverse difference is exactly

    Dcc_+^-1-Dcc_-^-1
       =kappa² Dcc_+^-1 (DeltaG)_CC Dcc_-^-1.

Expanding the two ordered quadratic products yields

    |g_eff,+-g_eff,-|
       <=[1+4812kappa²+36*401²*kappa^4] ||DeltaG||
       <2e-47+65000u.

Since |delta|=2j|sin(q-pi/2)|≥.0053u, the last energy-coordinate bound in(3) follows. It provides a concrete floor/linear numerator and the common denominator lower bound for a scalar sector-resolvent comparison. It does not supply the full seed matrix-measure comparison or total outside mass needed for the complete herald interface.

## 6. Energy-resolved reference comparison without a resonance-sized floor

Retain the selected/complement structure of the inherited outgoing row, rather than using the whole401 ceiling in its complementary Schur numerator. Write

    P B_e=ell_scalar P+E_L, ||E_L||<1e-23.

Because P is real and K_e P=(P B_e)^T iE',

    ||C K_eff,s||<.006*1e-23+3e-47<7e-26,
    ||B_eff,s C||<1e-23+2e-48<2e-23.

Using(10), rho≤.000132, the denominator>.99986, ||K_eff||<2.5, ||B_eff||<401 and ||F_closed||<4e-49 gives both off-diagonal attachment corrections<7e-27. The unattached off-diagonal blocks are<epsilon_G=1e-24. Hence conservatively

    ||(G_att,s)_PC||, ||(G_att,s)_CP||<2e-24.

All seven complementary directions are included; this is a block norm, not one entry. The effective self-energy's complementary numerator is therefore bounded by

    kappa² ||G_jC|| ||Dcc_s^-1|| ||G_Cj||
       <24 kappa²*1e-48.

The scalar endpoint comparison before emitter elimination gives, pointwise,

    |(G_free)_jj+w/j|
       <=2r0/[j(1-r0)]+epsilon_G
       <742(1e-20+12u)+1e-24.

Combining with(1) and the just-refined complementary numerator proves

    |g_eff,s+w/j|<8e-18+41000u
                 <=8e-18+7.74e6|delta|,
    |D_s-Dref|<kappa²(8e-18+41000u).                 (13)

This retains the nonzero source/closed floor explicitly and avoids replacing its spectral integral by the worst-band relative bound. The constants in(13) are for the same actual fixed kappa=1e-8 and band, not a new parameter optimization. They can serve a later scalar resolvent comparison with the denominator margin(2). They still do not establish the full old-input spectral matrix measure or omitted mass.

This refinement was added after root requested preservation of energy-resolved bounds for subsequent mass work. The preceding authored version is preserved as PROPOSAL_v1.md at SHA25628b0c2d15284b1edc3026063c234c55eef4eb1dba0b3a17b421d99f78e1eca46. It changes no earlier estimate or dependency and has not been independently checked.

## Remaining limits and decisive check

No cable phase is set to zero: w^36 acts in return, while the transmitted phase includes the distinct eighteen-edge one-way propagation. This proof bounds endpoint responses and does not define a new output waveform. It keeps the actual source calibration and finite-core premises but does not import their unattached mass or runtime conclusions.

The highest-risk steps for separate review are (4)--(7) at the same v0 plane, the ordered elimination(10), the use of selected-row norm rather than full-row norm, and the open-load existence argument. The attachment source itself is a provisional dependency pending its own distinct check. The full actual spectral density, global omitted mass, other-energy reference tails, complete local record1 columns, all-time herald success and temporal/finite-output statements remain separate obligations. These real-band numbers should not be silently extended to a complex disk or new physical parameter family.
