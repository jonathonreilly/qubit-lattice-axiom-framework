# Actual gate load for receiver halfwidth d/g at most one half

Status: new conditional real-band derivation requiring a distinct check. The existing local construction extends to d/g<=.5. Its actual one-output gate inverse is<33/j, complete forced gate/closed-tail recovery is<6.28, source-facing open reflection is<.129 and its record-sector difference is<=85u. Recomputing source feedback gives full endpoint-forcing recovery ||L_x||<4e5 and ||Delta L||<=6541+8.7e9|delta|. These are new local/background bounds, not imported emitter, mass, derivative or temporal conclusions.

## Domain and unchanged physical device

Fix the supplied old source, original two converters, source calibration, input cap,18-edge cable,24-head record gate and .0027<j<.003. Let

    0<g<=1e-6, 0<h<=4e-6,
    |q-pi/2|=u<=h, delta=-2j cos q,
    d=2j sin h, d/g<=.5.                             (1)

The upper bound on g is retained explicitly; no claim for arbitrary large positive hopping is made. Slow momentum k is defined by delta=-2g cos k with k in(0,pi), w=e^(iq), v=e^(ik). The background calculations do not depend on emitter coupling kappa.

The actual connector remains tau_s=sqrt(jg), with positive occupations (j-tau_s)n_o, (2j-tau_s-g)n_first and2(j-g)n_later. Every one-head diagonal remains2j, all original positive source/gate blocks remain installed, and no new vacancy scalar is introduced. The finite old output o and first slow site are distinct. Full8 B fibers, both record sectors and both physical old-energy windows are retained. Literal K/W and c_att are unchanged; no phase or source-system commutation is assumed.

I authored the preceding inverse/derivative refinements and checked several original components. Root proposed widening the ratio and exposed g=5e-8 as a candidate, not an accepted result. This is source-exposed author work, not independent checking or an optimization. I refreshed the complete local scattering/recovery argument and reuse unchanged full source/kernel and uniform upstream premises from the preceding coherent tasks. Exact identities appear below. No sweep, scientific numerical run, model change, delegation, W/Git/publication/checkpoint or frozen-source edit occurred.

## 1. Actual scalar connector on the wider interval

Equation(1) gives

    |k-pi/2|<=asin(1/4)<.252681,
    |k-q|<.252685<.253,
    sin k>=sqrt(15/16)>.968.

The arcsine bound can be verified by the alternating sine series at .252681: sin(.252681)>.25. Chord length is at most angle length, so |v-w|<.253. The exact physical interface is unchanged:

    r_L=(w-v)/(v-w^-1),
    t_L=sqrt(j/g) v(1+r_L),
    r_R=(v-w)/(w-v^-1),
    t_R=sqrt(g/j) w(1+r_R),
    t_f=e^[i(q+k)/2] sqrt(sin q sin k)/sin((q+k)/2).    (2)

The two flux-normalized transmissions equal t_f. Physical first-site transmission is t_L, not t_f. Both formulas retain the output reference-plane phase. Current conservation gives |t_f|^2=1-|r_L|^2, but no such flux identity is assigned to closed channels.

From the exact sine ratio,

    |r_L|=|sin((q-k)/2)|/sin((q+k)/2)<.128.            (3)

For a simple certified bound, the numerator is<=.252685/2 and the denominator exceeds1-(.252685/2)^2/2; their ratio is<.128. An energy-resolved alternative is

    |r_L|<=.261 |delta|/g.                            (4)

Indeed the mean-value theorem on the two arcsines gives

    |q-k| <=|delta|/(2g)
                  [1/sqrt(15/16)+g/(j cos h)].

The denominator in(3) is>.9919, sqrt(15/16)>.968 and g/(j cos h)<1/2699. Thus the coefficient is bounded by (1/.968+1/2699)/(4*.9919)<.261. The non-strict zero-floor inequality(4) includes delta=0. It should be combined with(3), not evaluated at the edge and misreported as a sharper constant.

At center r_L=r_R=0 and t_f=i. The positive transmission amplitude differs from1 by1-sqrt(1-|r_L|^2)<=|r_L|^2. Across the family there is no parameter-independent O(u) upper bound for that loss obtained by squaring(4): g may decrease with h. The exact amplitude and Jacobian must be retained.

## 2. The gate inverse survives without the failed whole-inverse Neumann test

Let R0=(D_x,old^R)^-1 be the actual one-output gate inverse with a j output ray, no artificial input selfenergy, in one selected B channel and record sector x. Its checked real-band bounds are

    ||R0||<26/j,
    ||R0 e_p||,||R0 e_o||<=5/[j(1-75u)],
    |R0_oo|<=b_u/j, |R0_op|<=(1+b_u)/j,
    b_u=75u/(1-75u)<.000301.                          (5)

These follow from the exact center column and R0_oo(center)=0; the latter is essential. The new matrix differs by eta P_o, eta=j(v-w). The naive bound26|v-w| can exceed1 and therefore proves nothing on(1). Instead use the exact rank-one formula

    Rnew=R0-eta R0 e_o e_o^T R0/(1+eta R0_oo).        (6)

The true denominator obeys

    |1+eta R0_oo|>1-.253*.000301>.999923.

Transpose row and column norms agree. Consequently

    ||Rnew||
      <[26+.253*25/(.9997^2*.999923)]/j<33/j.         (7)

Thus the larger surface change is controlled by its small actual output diagonal entry, not by a full inverse perturbation estimate. The corresponding forced input column obeys

    j||Rnew e_p||
      <=5/.9997*[1+.253*(1+.000301)/.999923]<6.28.     (8)

For closed B channels the same actual kinetic gap |delta_l|>60j>.162, old roots<1/60 and slow roots<1/160000 remain valid because g<=1e-6. The gate row bound and physical surface selfenergies give the unchanged inverse<1/(56j). The complete closed-tail multiplier is still<.00068, from |v_l|<=2g/.162 and sqrt(j/g)|v_l|/sqrt(1-|v_l|^2). Hence the closed gate-plus-tail forced norm is<1/55. Orthogonal direct sum over all eight channels proves complete gate-plus-closed-tail forcing<6.28; the selected stationary open ray is not included in this square-summable norm.

## 3. Exact two-port composition and sector difference

Use the unchanged equal-j gate matrix with |r_p,x|,|r_o,x|<=33u, |t_x|<=1 and |t_x-x rho_R|<=33u, rho_R=-i w^22. Reciprocity gives the equal-velocity reverse transmission t_x. At shared physical output plane o, no extra w^2 belongs in the interface load. Set d_x=1-r_o,x r_L. Then exactly

    R_left,x=r_p,x+t_x^2 r_L/d_x,
    T_left,flux,x=t_f t_x/d_x,
    R_right,x=r_R+t_f^2 r_o,x/d_x.                   (9)

The denominator now obeys d_min>1-.000132*.128>.999983. Therefore

    |R_left,x|<=33u+|r_L|/d_min<.129,
    |R_left,x|<=33u+.262|delta|/g.                    (10)

The constant and energy-resolved versions are separate simultaneous bounds. Neither the old .0062 nor the old1540u individual estimate is reused.

The leading common reflection still cancels in the two record sectors. Since |t_++t_-|<=66u and |t_+-t_-|<=2,

    |R_left,+-R_left,-|
      <=66u+132u*.128/d_min+66u*.128^2/d_min^2
      <=85u.                                        (11)

The numerical expression actually has some additional slack;85 is a convenient safe ceiling. This is not twice the individual return bound. The exact transmitted comparison is

    |T_left,flux,x-x rho_R t_f|
       <=33u+33u*.128/d_min<38u.                     (12)

Comparison with x rho_R exp[i(q+k)/2] additionally costs |r_L|^2 and must not hide that amplitude loss. At v0 the input plane moves eighteen edges: reflection gains w^36 and transmission gains w^18. The literal transmitted comparator is consequently

    x w^18 rho_R t_f
      =-i x w^40 e^[i(q+k)/2]
                     sqrt(sin q sin k)/sin((q+k)/2). (13)

Closed-channel generalized composition retains the old separate denominator>.99942, because its proof uses only old/slow closed-root maxima1/60 and1/160000. Alternatively the full one-output closed inverse gives directly the root-dependent reflection bound. At cable position n the incoming closed field must be bounded in the form

    |s|^(36-n)|r_gate,x|
      <=[|s|^(36-n)+|s|^(35-n)/56]/(1-|s|/56)
      <3*60^(-(36-n)), n=0,...,17.                  (14)

The raw closed r_gate can contain1/|s|; it is NOT assumed uniformly<3. Formula(14) pays that factor before taking the bound. In particular the complete closed return at v0 is<e=1e-63. Both root signs and all seven channels are included.

## 4. Recompute the actual source feedback and full recovery

The unloaded source is unchanged. Its complete endpoint-forcing data are

    ||P B_e||<400, ||B_e||<521,
    |S_PP|=1, ||S_CP||<2, ||S||<2e8,
    ||K_U P||<1000, ||K_U||<2e18.

Here U contains193 noncable heads, and P selects the outgoing open channel, not the forcing domain. The exact equations remain b_x=S a_x+B_e, a_x=R_x b_x, with diagonal physical returns at v0. Closed elimination retains its previous allowances<8e-47 in the effective selected reflection and<3e-52 in forcing. The NEW selected denominator is

    |1-S_eff,x r_x|>1-(1+8e-47)*.129>.8709.          (15)

The whole matched background remains invertible on the real band, conditional on the same source inverse premises and new gate proof. In particular

    ||P b_x||<460,
    ||C b_x||<2*(2*.129*460+521)<1280,
    ||P a_x||<59.34, ||C a_x||<1280e.               (16)

All operators act on the entire endpoint-forcing fiber.

For absolute recovery, original arms/buffers and finite input cost240001+4670 as before attaching any load. Actual upstream attachment now costs<1000*59.34+(2e18)*1280e<59341. Each cable site costs<460+1280+59.34 plus its already suppressed returned closed term, hence its18-site norm is<9000. At v17 the closed outgoing amplitude is suppressed by60^-17 and (14) pays the returning part, so its full norm is<520. Equation(8) therefore gives actual gate-plus-closed-tail norm<520*6.28<3270. Summing complete coordinate ranges gives

    ||L_x||<240001+4670+59341+9000+3270<4e5.         (17)

The same4e5 ceiling survives, but only after this new calculation; the earlier fine coordinate ceilings, such as gate2060 and upstream correction2499, do NOT survive unchanged.

For the difference A=||P(a_+-a_-)||, the ordered identity Delta a=R_+ S Delta a+Delta R b_- and(11),(16) give

    A<=.129 A+.129*(2e8)*2560e+(85u)*460,
    A<45000u+1e-52.                                (18)

Here1-.129=.871 is the denominator for this direct estimate. The noncable difference is at most1000A+(2e18)*2560e. Cable outgoing difference costs3A plus the tiny closed-input forcing, open incoming difference costs A, and eighteen-site aggregation costs<5. Equation(14) controls the remaining complete closed return, giving cable difference<20A+1e-28. Thus

    ||Delta L_up||<1e-24+4.6e7u.

Paying the two actual gate-plus-closed-tail norms by3270 each, and using |delta|>=.0053u, proves

    ||Delta L||<=6541+8.7e9|delta|.                 (19)

Both lips follow by fixed real conjugation, without treating a rectangular jump as an adjoint. Parity and record direct sums do not introduce an extra factor eight; the two physical energy windows remain separate in subsequent spectral integration.

## Remaining interfaces and interpretation

This local extension is structurally feasible within the stated exact construction. For orientation only, g=5e-8 at h=4e-6 has d/g<.48 and lies in(1); no mass, success, runtime or resource advantage is inferred for it. The fixed positive blocks and exact finite cap/resource identities still define that device, but their performance premises require new estimates.

The following quantitative contracts MUST be rederived before use:

1. Actual endpoint Schur selfenergy and sector-difference constants, including selected and complementary matrices. The new feedback margin is.8709, not.9937. Neither the old8e-18+41000u+244|delta|/g nor its mass constants are imported.
2. Full emitter inverse, imaginary denominator, wrong-window comparisons, genuine full8 reference density and actual omitted seed mass. A finite background inverse and one open channel alone do not supply those numerical conclusions.
3. Actual transmitted/incoming coefficient comparisons, preserving(13), first-site origin and the slow Jacobian dq/dk=g sin k/(j sin q). The scalar exact formula remains valid, but its old moment, reflection-loss and contour constants were proved on d/g<=.024 and need a changed-domain proof.
4. Recovery derivative and complete temporal composition. Although (17) survives, the previous sharp forcing bounds used gate2060, upstream correction2499, smaller boundary feedback and forcing factor5.064. The new3270/59341/6.28 values must be inserted, together with the changed source endpoint/emitter and scalar estimates. The fixed4.7e18 or2.67e17 derivative ceilings are not inherited.
5. Any actual finite success/error comparison and output-length claim. Exact finite compression still supplies a transfer formula conditional on the new infinite dynamics estimate, but changing g alone does not certify the desired state on a read interval.

The full background's qualitative local regularity follows from the explicit local and feedback inverses above. It is distinct from an emitter spectral or temporal result. No new native supplier, measurement rule, irreversible latch, all-future storage, optimized operating point or phase relaxation is asserted. The failed coarse Neumann test26|v-w|<1 was a proof limitation, resolved here by the actual small R0_oo; it was not a physical obstruction.

Distinct checking should reconstruct the wider scalar bounds, small-entry Sherman denominator, full closed-root handling in(14), source feedback and complete recovery arithmetic. This source does not check itself or replace the independent checks of inherited source premises.

## Exact source identities

- `slow_lead_gate_load/PROPOSAL.md`: `c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d`.
- `slow_lead_gate_load_check/REVIEW.md`: `8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65`.
- `slow_lead_uniform_endpoint/PROPOSAL.md`: `c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887`.
- `slow_lead_uniform_endpoint_check/REVIEW.md`: `f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0`.
- `slow_lead_recovery/PROPOSAL.md`: `f0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f`.
- `slow_lead_recovery_check/REVIEW.md`: `488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195`.
- `slow_lead_uniform_composition/PROPOSAL.md`: `8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e`.
- `slow_lead_uniform_composition_check/REVIEW.md`: `b873ac37d8a327f27491f36e80dfe5e8aeef7eb0d7b405bba6b70a6ffb9e71a7`.
- `record_attached_recovery_sharp/PROPOSAL.md`: `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`.
- `record_attached_recovery_sharp_check/REVIEW.md`: `cbd5dfd29fbe67ad36c3ffc97a896f55ea30b8a5af367930c48a080589523430`.
- `slow_lead_forced_derivative_sharp/PROPOSAL.md`: `662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0`.
- `slow_lead_forced_derivative_sharp_check/REVIEW.md`: `41f8ad9e18d7c1910f8a2c9b7cc70a2cb6b5a89ecbad47d52fd555b694718d4d`.
- `slow_lead_direct_forcing_refinement/PROPOSAL.md`: `f9fdcaa59e3b2d58805d295cb2dd63d4c7c763917ee8099b90afb2ec3c0db909`.

Original source/calibration and exact gate-center ancestry remain those pinned in the unchanged local gate and recovery arguments. Hashes record identity, not proof or new audit status.
