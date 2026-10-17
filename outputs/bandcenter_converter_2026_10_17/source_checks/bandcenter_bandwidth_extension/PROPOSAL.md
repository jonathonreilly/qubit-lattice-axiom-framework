# Fixed fourfold new-band extension at unchanged coupling

Status: authored conditional analytical proposal, requiring a separate selective check. Keep the physical nominal device and kappa=1e-8 unchanged. Replace only the spectral comparison halfwidth on the NEW q lead by h=4e-6. The original source certification remains exactly k0±1e-6. Energy margins put the whole new band inside that original band; the original source domain is not enlarged. With revised intermediate inverse/error margins, the pointwise profile ceiling a+b|q-pi/2| survives with a=1.8e-13 and b=220. The proposed consequences are actual outside-band mass <1.13e-6, amplitude <.001064, per-column initial spectral comparison <.001067, and arbitrary old/reference initial comparison <.001510. These are not runtime or escaped-output bounds.

This is one specified width, not a sweep or an optimization. The already checked h=1e-6 result remains independently useful, including for the separate temporal investigation.

## Sources, exposure and conditional premises

Reuse complete argument and source readings recorded in ../bandcenter_weighted_profile_check/REVIEW.md SHA256 d2ac8183a6531cce4ed96da1b841b99d31e1340de4b9422507b82f5da7bb9071, and corrected ../bandcenter_weighted_profile/PROPOSAL.md SHA256 ab3b7cbfb3ff8159541564ca088b23072f42c075149225b34318d11d581a9ed0. Both identities were reverified before this extension. I authored that selective review, not its weighted-profile proposal; I am now the author of this extension and cannot independently review it.

The necessary canonical source passages at correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md lines163–319 were previously read completely at SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff; its identity was reverified unchanged. Original finite-core and source premises remain conditional, with no blanket recertification of unrelated note content. Reused complete previously read dependencies are:

- ../bandcenter_converter_composition/PROPOSAL.md: 1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78.
- ../bandcenter_converter_composition_check/REVIEW.md: f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c.
- ../bandcenter_converter_endpoint/PROPOSAL.md: 22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a.
- ../bandcenter_converter_endpoint_check/REVIEW.md: 200268709480f1533050f5d197a4bed7a2acaefa5f4a22a662938ddb504619c6.
- ../bandcenter_reference_measure_check/REVIEW.md: 1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae.

Parent suggested the fixed width4e-6 and the energy-map mechanism. Prior targets/reviews are exposed inputs. This is a new proposed extension, not independent discovery or its own independent validation. Applicable unchanged AGENTS/workflow and proof discipline were reused from the review. No scientific execution, solver, numerical integration, parameter search, delegation, Git/W/checkpoint/prompt/model change or publication occurred. Deterministic source hashing and this deliverable only; no editable prompt file changed.

## 1. Domain before derivative estimates

Retain J=.030021107107032, j=J(1-C0), tau²=jJS0, .0027<j<.003 and all original shared-source/filter/junction data, two exterior converters at F=40, and input stub ell=20. Let

    I_h=[pi/2-h,pi/2+h], h=4e-6,
    x=|q-pi/2|, E(q)=2j(1-cos q).

The nominal center obeys E(pi/2)=E0. Throughout I_h,

    |E(q)-E0|<=2j h<.006*(4e-6)=2.4e-8.

The two ORIGINAL k-band edge-energy margins are each at least v sigma_old=.025*1e-6=2.5e-8. Monotonicity therefore places k(q) strictly in that original band before using any derivative bound there. Consequently

    cos k=C0+(1-C0)cos q,
    k'=2j sin q/E'_old<.24,
    |k-k0|<.24x<=.96e-6<1e-6    (x>0),

with k=k0 at x=0. The old derivative, central calibration, filter, source inverse, kernel and root premises are applicable everywhere on I_h. In particular sin k>.4, ||Qc||≤1/7, ||Aold||≤40 and ||Aold^-1||<20 remain original-band statements. No source estimate has been extrapolated.

The new velocity is E'=2j sin q≥2j cos h>.0053. For each excited channel,

    X_new=(beta-b)/j+2cos q>.186/.003-2h>61.99,

and the other vacuum satisfies |X_new|>2/.003-2h>666. These still exceed60+1/60, hence all seven signed decaying new roots have magnitude <1/60. Exactly one propagating channel remains at each selected energy. The fixed real B projections do not move with q.

## 2. Converter, feedback and retained finite coordinates

The converter numerator/denominator derivative bound remains

    2j+JS0+J|k'|<.006+.0155+.00744=.02894<.029.

Its central denominator is >.024 and numerator zero. Thus on this larger interval

    |r_o|=|r_n|<=rho(x)=.029x/(.024-.029x)<=1.22x,
    rho(h)<4.88e-6.

At x=0 the zero-floor inequalities are non-strict. The transmission square-root calculation still has margin: its square differs from1 by at most (.24x+.5*x²/2)/.4=(.6+.625x)x<=.61x. The previously used .62x root bound and <1.000003 root magnitude are safe. With exp(iq) retained, |t_c-i|≤3x and |t_c²+1|≤6x follow from the exact flux transmission and unitarity.

Closed-converter estimates depend on the unchanged old root1/7 and new root1/60 bounds, not on h directly. The closed two-site Schur denominator is still >5.99J, inverse norm<7, and |R_c|<1/5 for both root signs. Therefore E_c=R_c Qc^(2F) has norm<2e-65. Original generalized source cross and closed blocks still satisfy epsilon_c<5.2e-12 and c_c<5.2e-32. Their ordered full feedback gives correction delta_c<1e-86, closed outgoing norm<6e-12||a_P|| and incoming norm<1.2e-76||a_P||. No center cancellation of that uniform correction is claimed.

The open inverse ceiling1.000002 from the old width is NOT reused. The enlarged-band inverse is

    ||(I-r_o z^(2F)S_loaded)^-1||<=1/(1-rho(h))<1.000005.

In the full generalized converter formula the full So norm differs from1 by less than2(5.2e-12)+5.2e-32; including that factor still leaves the same1.000005 ceiling. The channel coefficient estimates |U|<.49, |V|<2.5 and closed |R_n|<.002 remain valid. For V, sin k<.500001 suffices, since |k-k0|<.96e-6. Hence the complete generalized Sn norm remains<1.3, Tn=Sn An has norm<260<600, ||An||<200 and ||An^-1||<21. These are full internal matrices, not inferred from open unitarity.

Comparing new open scattering with -z^(2F)S_old costs

    rho(x)+6x+rho(x)/(1-rho(x))+delta_c<=9x+delta_c.

The displayed comparison is non-strict at x=0 and strict for x>0. The ACTUAL scattering error is strictly below 9x+delta_c also at x=0 because its closed correction is strictly less than delta_c. The unchanged source/filter center-plus-derivative argument then gives

    |R_new|<r(x)=1e-20+12x,
    |t_new-rho_n(q)omega_p|<t(x)=d0+1e-20+181x,
    d0=1.76e-13, rho_n(q)=-exp(2iF k(q))rho_g(k(q)).

The pre-rounding slopes remain11.88 and180.36. Both positive closed-feedback floors and the calibration floor remain. The common phase is unchanged and includes actual k(q).

The original finite-coordinate recovery formula G_old(core,ports0)Aold^-1(a_P+a_C), with its original predeletion blocks, still applies at every mapped energy. chi/(1-rho)<1 still holds. Thus the loose finite-core norm2e10, buffer norm40 and complete geometric closed-tail estimate from the composition remain valid for unit new incidence. No coordinate has been deleted by changing the spectral cutoff.

## 3. Endpoint and all emitter coordinates

Use eta_h=4.81e-5, so r(x)<eta_h. The old uniform eta=21e-6 is no longer the chosen margin. The full stub correction is unchanged:

    ||X-X0||<3*600*60^-20<1e-32.

Now ||X0||<200 eta_h=.00962, which still gives ||An+X||<201. The diagonal inverse is bounded by21/(1-eta_h), and its perturbation still gives ||Z^-1||<24. Thus the same exact ordered Dirichlet formula and its Lipschitz ceiling3e7 yield epsilon_G=1e-24. The complementary endpoint block is still -Qn,c/j, and the selected g has magnitude bounded by (1+eta_h)/[j(1-eta_h)]<400. The output-row proof uses ||Y0||≤200 from |t|≤1 and the same bracket estimates; epsilon_L=1e-23 survives.

The seven complementary emitter bare gaps are now bounded below by .186-.006h>.185, so ||Dcc^-1||<6 remains valid for0<kappa≤1e-8. Retain exactly

    Dj=E-2j-kappa²Gjj-kappa⁴GjC Dcc^-1 GCj,
    outgoing numerator=-kappa[L_j+kappa²L_C Dcc^-1 GCj].

For the pointwise comparison to Dref=E-2j+(kappa²/j)exp(iq), use

    |Dj-Dref|/Im Dref
      <=2r(x)/[(1-r(x))sin q]
         +j[epsilon_G+6kappa²epsilon_G²]/sin q
      <d(x)=2.0001r(x)+4e-27.

The coefficient2.0001 still has margin at this specified width: r(x)<4.8000001e-5 gives 2/[(1-r)cos h]<2.0001. Consequently d(x)<1e-4. The old epsilon_D=5e-5 is NOT valid as the chosen uniform ceiling here; replace it by1e-4. This still yields Im Dj>(1-1e-4)Im Dref>329kappa² and full ||De^-1||<1/(300kappa²), including its complementary and cross blocks.

The complete finite-core, converter, Dirichlet and emitter inverse chain therefore remains regular over I_h. Branch separation and nonzero open velocity hold through both cutoffs. The same finite-tail resolvent-jump argument applies on the enlarged interval: actual seed density is |F_j(q)|²dq and there is no singular in-band component. This conclusion uses the full finite-coordinate inverse premises, not just S unitarity. Out-of-band point spectrum is not excluded.

## 4. Pointwise full complex profile survives with changed product margin

The exact scalar ratio still obeys

    |F_j/Fref-omega_p|
      <=[t(x)+r(x)+d(x)+r(x)d(x)]/
          [(1-r(x))(1-d(x))]+tiny_row_term.

L0 has no complementary columns, so the extra numerator allowance is bounded using j epsilon_L+6j kappa²epsilon_L epsilon_G. The same1e-25 allowance covers this and the constant4e-27 term. Since r≤4.8000001e-5, the r*d contribution satisfies the same safe numerator bound

    t(x)+3.0002r(x)+1e-25.

Here 2.0001r<.0001 is the needed check for absorbing the quadratic term into the extra .0001r. The product denominator is now>.99985; the old .99996 margin is NOT reused. Its pre-division slope217.0024 divided by .99985 is still below220. Its constant divided by .99985 remains below1.8e-13 with positive d0 retained. Therefore

    |F_j/Fref-omega_p|<a+b x,
    a=1.8e-13, b=220, 0<=x<=4e-6.

In particular e(x)<.000881<1. The profile is complex, includes the common propagation phase, and retains all source/emitter complements. No derivative of closed corrections or exact center calibration is asserted.

## 5. Reference moments, actual mass and initial comparison

The scalar reference measure is unchanged. Put u=q-pi/2, A0=2j-kappa²/j and B0=kappa²/j. On the enlarged finite band its exact density is

    dmu0/du=2kappa²/[pi(A0²tan²u+B0²)].

With p0=mu0(I_h), the UNNORMALIZED moments satisfy

    M1<=2kappa²/(pi A0²)*log(1+(A0 h/B0)²),
    M2<=4kappa² h/(pi A0²).

The full reference measure has mass one, and its exact hard-band tail is bounded by4kappa²/[pi A0² tan h]. At kappa=1e-8, A0>.00539 follows from j>.0027 and kappa²/j<1e-16/.0027. With pi>3.14 and tan h>h, the tail is<1.1e-6. This bound is recomputed for h, not inherited as an unchanged numerical tail.

For conservative moment ceilings use A0>.0053 and

    A0 j h/kappa²<720000.

The logarithm is<28. An elementary rational witness is e>8/3, (8/3)^5>130, (8/3)^3>18, and130^5*18>1+720000². These imply e^28>(8/3)^28>1+720000². Therefore

    M1< [2*1e-16/(3*.0053²)]*28 <6.7e-11,
    M2< [4*1e-16*(4e-6)/(3*.0053²)] <1.9e-17.

The actual spectral identity and complex profile bound yield

    p_actual>=integral_Ih (1-a-bx)² dmu0
             >=p0-2a p0-2b M1,
    1-p_actual<1.1e-6+3.6e-13+440*(6.7e-11)
                <1.13e-6.

This pays ALL actual outside-band mass, including point spectrum. It does not substitute the reference tail for actual mass, and the central floor remains2a. Since .001064²>1.13e-6,

    ||outside-band actual seed||<.001064.

The in-band coefficient difference in the actual scattering transform is at most a sqrt(p0)+b sqrt(M2)<9.6e-7; for example sqrt(1.9e-17)<4.36e-9. Positive reference normalization costs1-sqrt(p0)≤1-p0<1.1e-6. Thus

    ||seed_j-normalized_actual_scattering_packet_j||
        <.001064+9.6e-7+1.1e-6<.001067.

The target packet uses the actual incoming reflection phase, common Fref/sqrt(p0), and full physical source/emitter/closed coordinates. Two selected old-energy bands remain disjoint, but their error vectors need not be orthogonal. Paying sqrt(2)<1.415 per parity gives<.001510 on arbitrary old/reference inputs; parities remain orthogonal and passive-reference tensoring preserves the bound.

## Scope and next decision

The proposed improvement comes from a larger admissible spectral cutoff in the same device at the same coupling. It does not alter physical W, original source bandwidth, old aging, scalar c_old+4gamma, converter supplier values, or the shared source. It asserts no broader source calibration and no extrapolation into a second propagating channel. It is not a precision-removal or common-j family result.

The exact changed-domain claims requiring separate review are the preliminary energy-margin inclusion, revised open-return1.000005 and endpoint margins, survival of coefficient2.0001 and profile slope220 at h=4e-6, and new finite-band mass/comparison arithmetic. No unchanged ancestry needs blanket recertification, but all inherited finite-core premises remain conditional. No temporal escape, contour/derivative localization, finite output window, resource count or runtime follows. The separate old-width temporal work must not silently import this new cutoff; a future temporal extension would need its own changed-domain estimates.
