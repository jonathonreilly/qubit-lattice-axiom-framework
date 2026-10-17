# One complete common-offset family at the original receiver

Status: authored conditional composition requiring its own distinct check. The shifted scalar reference-time source `646f26bd` has now received its distinct conditional check `0a49ed08`, read in full before this composition was finalized. The numerical conclusion below remains conditional on its explicit scalar hypotheses and the checked physical/inverse/local/traveling premises. No publication or retained-status claim is made.

## Fixed family and target

Keep the exact original calibration .0027<j<.003, physical graph, shared B, source vacuum, converters, record gate and slow receiver. Fix

    lambda=1e-13, g=5e-8, h=4e-6,
    T=2e14, M=50,000,000, epsilon=1e-6.

For every supplied real offset |Delta|<=1e-12 and source tuple

    a1^2=(lambda^2/3)(1+e1), a2^2=(8lambda^2/3)(1+e2),
    kappa^2=3jlambda(1+e3), |e_i|<=epsilon,
    |r_i|<=epsilon lambda=1e-19,

use the checked six-block installation with source occupations

    (j+Delta+r2-a2)n2,
    (2j+Delta+r1-a1-a2)n1,
    (2j+Delta+r0-a1)n0,

in addition to its structured source-port block and two internal source bond blocks. Positive amplitudes, fixed negative exchange signs and full internal identity detunings are essential. Source diagonals become 2j+Delta+r_i, source compression retains j n_p, and c_att is unchanged. All other device coefficients and the product-seed preparation are exactly the supplied ones. This is structured compensation, not arbitrary fabrication error.

The physical energy windows remain I_e=c_att+2j+e+[-d,d], e=1,3, d=2j sin h. They are NOT recentered. Let F_Delta,0 be the exact NOMINAL transmitted hard-band scalar coefficient at the same supplied Delta, with all residuals zero, physical load m_j(delta), original phase 61.5q+.5k+172k_old(q), fixed zeta, flux/Jacobian and physical time evolution. Let p_Delta,0 be its transmitted mass and beta_Delta,0(t) its raw packet on the actual slow halfline m>=0. Put r_Delta,0(t)=||beta_Delta,0(t)||.

For each Delta define the normalized complete target

    T_Delta,0(t)=exp(-it c_att)
       Jout[(beta_Delta,0(t)/r_Delta,0(t)) tensor exp(-itK)W],
    K=2I+Z1Z2,
    W=[(9+12i)I+(-16+12i)X1X2]/25.

The target contains computational record1, source vacuum and blank nonoutput heads. It is fixed across residual tuples at that Delta. It is deliberately a Delta-dependent family, NOT a uniform comparison to Delta=0. The physical scalar packet includes exp[-it(2j+delta)]; writing it in shifted energy includes exp[-it(2j+Delta)] exactly once. Delta is not a removable full-apparatus scalar. Arbitrary old inputs and arbitrary passive references are allowed.

Subject to the checked conditional reference theorem, the proposed conclusion is

    sup_(T<=t<=2T) ||embed exp(-it H_Delta,r,M)V-T_Delta,0(t)||
                  < .000986.                            (1)

This is a complete vector-map/operator-norm estimate on one prescribed finite interval. The comparison space remains infinite; no target-tail projection or actual successful-branch normalization is hidden.

## Actual inverse and one omitted state

Uniform elementary bounds are

    2.15e-8<d<2.4e-8, d/g<.48,
    b0=46000/.0053+290/g<5.81e9, a0=8e-18,
    kappa^2<9.000009e-16, kappa<3.000002e-8,
    beta=3(lambda+|Delta|)/j<1.223e-9,
    B_eps<.000020000017,
    m=1-beta-B_eps>.9999799987,
    A_eps/m<1.333364,
    a_bar=a0+b0|Delta|<.005811.

The checked FULL common-offset criterion gives

    Theta<=kappa^2{(A_eps/m)[a_bar/lambda+b0]
                                           +6(a0+b0d)}<.000077,
    c=(1-Theta)m>.9999029.                              (2)

For a transparent witness, a_bar/lambda+b0<6.392e10; multiply this by 1.333364 and 9.000009e-16. The complementary summand is <7.54e-13. The full complementary 170/6 bounds and both physical lips are retained; no selected inverse is substituted for the full one.

The exact installed shifted sixth moment has the four prefix coefficients in the checked actual interface. Its uniform envelope gives mu6<8.000026e-68. The port diagonal does not enter the third application. To concentrate in the ORIGINAL windows use d-|Delta|>2.1499e-8, or conservatively >2.14e-8. Thus

    eta_actual<=sqrt(2mu6)/(d-|Delta|)^3<4.1e-11.        (3)

This one outside vector includes all actual spectral types and arbitrary old/reference inputs. It is charged once globally. The genuine scalar reference has the same prefix moment, giving a separate reference truncation eta_ref<4.1e-11 for the represented-source estimate.

## Represented source heads and remaining background

At the same Delta the checked residual scalar ratio satisfies

    chi=B_eps/(1-beta)<.00002000002,
    L<.000021501, D_rho=2L+L^2<.000043003.

The unchanged polynomial bounds Bpol<3.414e-6 then give Elocal<.000078 for the full three-site scalar vector. The common-mode scalar-to-cubic bound gives

    Evec_Delta<4.3e-9.                                  (4)

Indeed beta<1.223e-9, sqrt(3)<1.733, and the leading density term 2beta dominates beta^2 and (Delta^2+lambda^2)/(4j^2); their quotient by (1-beta)^2 remains below this ceiling. The cubic vector tail has lambda/(2j-|Delta|)<1.853e-11 and is negligible within the displayed slack. For lambda t in [20,40], the exact cubic joint norm F(lambda t)<8e-7, retaining its common physical carrier.

Use the actual common-offset local/core source with C_eps<1.0000027 and m from (2). Its selected Stone prefactor kappa^2 a1a2/[pi(1-Theta)] is <2.7085e-42. With a_bar<.005811, b0<5.81e9 and C_eps/m^2<1.000044, the selected bracket is <9.715e36+8e24. Therefore

    Dsel<.0000264, Dwrong<2e-37.                         (5)

For the wrong-window bound Dmax=d+|Delta|<2.401e-8, asinh(Dmax/lambda)<14 and its complete bracket is <281. The factor 170 and both lips remain present. These are full-source-output estimates, not only seed return.

Consequently the represented all-three-source contribution obeys

    S_Delta(t)<=F(lambda t)+Evec_Delta+Elocal+eta_ref
                                      +sqrt(2)Dsel+2Dwrong
              <.000117.                                (6)

The unchanged emitter-free recovery covers every other finite coordinate and all closed tails. Its full-forcing bound L0=14000 gives

    B_Delta(t)<=8sqrt(2)(1+epsilon)kappa L0/(3pi c)
              <.000505.                                (7)

Using sqrt(2)<1.415 and pi>3.14 already suffices. The open propagating ray is handled separately. Neither (6) nor (7) includes a second actual omitted-state charge.

## Actual traveling waves versus same-offset nominal waves

The exact perturbed scalar second moment about physical delta is

    m2_phys=(Delta+r0)^2+a1^2,
    sqrt(m2_phys)<1.002e-12.

Thus the physical slope term is <6.11e-6, using 304/(2j cos h)+.302/g<304/.0053+6.04e6. The inverse correction satisfies

    1.384Theta/(1-Theta)<.00010658,
    Esel<.0001127.

The complementary row Bwrong<2e-33 and its Fourier allowance Ewrong<4e-38 follow from the full 170 inverse, kappa a1a2 and row norm461. Hence

    2Eraw=2(sqrt(2)Esel+Ewrong)<.000319.                 (8)

All opposite-window prepared inputs retain their actual physical energies. Record/parity sector aggregation is unchanged. The nominal same-Delta replacement costs L sqrt(p_Delta,0) for each ideal wave, so

    2L sqrt(p_Delta,0)<.00004301.                        (9)

There is no pe normalization and no extra old-energy multiplicity for the common scalar replacement. Incoming conjugation gives W* with the same physical time factor and never conjugates an arbitrary input/reference. The two physical waves share coordinates, so their errors are added rather than assumed orthogonal.

## Checked shifted-reference substitution

Use the new reference-time source at proof cutoff D=g/8=6.25e-9. The uniform condition |Delta|+2D<d holds. Its shifted carrier and velocity satisfy

    kD=acos(-Delta/(2g)), v=2g sin kD>9.999e-8,
    etaD<.000652, omegaD<.001955,
    mD=(1-beta)(1-etaD)^3>.99804,
    bD=(1-etaD)D>6.245e-9,
    P<5.02e6.

The following substitutions into that source's exact functional give conservative ceilings:

    J2<1.126e-24,
    Nerr<4.58e-10,
    Qerr<1.236e-9,
    P lambda/sqrt(3)<2.90156e-7,
    Ecentral<3e-7.

For |t|<=2T the quadratic-curvature term in Edisp is <2.001e-10. Using pi>3, the truncated-sixth-moment term is <2.224e-9; therefore Edisp<2.5e-9. Both U and V are <7e-13, and the conservative shifted alias Z<1e-14. These bounds include both hard sides and the actual first slow coordinate m=0.

The nominal transmitted mass satisfies

    1-p_Delta,0<=mu6_0/(d-|Delta|)^6
                        +(Delta^2+lambda^2/3)/g^2<4.02e-10.

This is a scalar transmission/tail estimate, not a second actual omission. Adding the functional terms gives E(t)<3.1e-7 uniformly on [0,2T]. At lambda t>=20, the shifted sampling tail obeys H_v(lambda t)<8e-7: the coefficient 4lambda/(3v)<1.334e-6 and the remaining polynomial at20 is <119000; with exp(20)>4.8e8 the squared tail is <(8e-7)^2 and decreases thereafter. Thus on [T,2T],

    ||alpha_Delta,0(t)||<=sqrt(p_Delta,0)J_in(t)<3.1e-7,
    C_out(t)<1.2e-6,
    1-r_Delta,0(t)<=1-sqrt(p_Delta,0)+C_out(t)^2<4.04e-10. (10)

In particular r_Delta,0(t)>0. The target's physical-halfline normalization is paid once through (10). The normalization used internally to estimate scalar functionals does not normalize or postselect the actual state. The shifted-reference distinct review supports its derivation without correction; this author substitution does not independently recertify that derivation.

## Complete infinite and finite budgets

The checked actual synthesis, conditional on the checked scalar reference hypotheses, gives

    ||U(t)V-T_Delta,0(t)||
     <=eta_actual+S_Delta(t)+B_Delta(t)+2Eraw
          +2Lsqrt(p_Delta,0)+||alpha_Delta,0(t)||+1-r_Delta,0(t)
     <4.1e-11+.000117+.000505+.000319+.00004301
                                              +3.1e-7+4.04e-10
      =.000984320445 <.000985.                           (11)

All source heads, finite background, closed tails, traveling directions, records, internal outputs and the global outside state are included. Shared B need not commute with full H. Passive references preserve these operator norms.

The exact finite cap with M=50,000,000 retains M+243=50,000,243 physical qubits and 2M+281=100,000,281 positive blocks for this six-block family. Source offsets and all residual changes lie in the output-weight-zero region. The unchanged single-cut comparison gives uniformly on [0,2T]

    ||U_infinity(t)V-embed U_M(t)V||
       <1.2 exp[-M+4gT sinh(1)]
       <1.2 exp(-2,960,000)<1e-10.

This retains returns, reflections and the compression cap diagonal. Combining with (11) proves the conditional proposed .000986 ceiling. No target-tail projection is added.

Optionally the separately checked seven-block identity replaces H_old by H_new=H_old+Csrc(actual)I, Csrc=kappa+a1+a2. The same norm bound would then compare to exp[-it Csrc(actual)]T_Delta,0, with 2M+282 blocks. This scalar is distinct from Delta P_source. This optional identity is not needed for (1), and it cannot justify removing the actual-tuple phase or relaxing diagonal precision.

## Scope and exposure

The offset range extends to ten linewidths and 10^7 times the residual diagonal bound, but the target depends on the supplied Delta. No small complete error against the zero-offset packet is asserted. The theorem would cover only the prescribed identity detunings, relative squared-bond box and compensating installation with exact remaining physical premises. It does not establish native suppliers, arbitrary hardware-error tolerance, physical seconds, early/late guarantees outside [T,2T], repeated monitoring/reset or permanent halt.

I authored the new shifted-reference source and several attachment/traveling/reference ancestors and checked the common-mode scalar, actual, local/core and traveling sources. This is exposed author composition, not an independent check of those sources. Root suggested this one family and rough scale; the displayed .000986 ceiling follows from the explicit bounds and is not an imposed acceptance target. A distinct composition check remains required. The shifted-reference check was read fully and its exact identity is pinned below; it is reused evidence, not a check of this operating-point composition. No numerical sweep, dynamics, integration, scientific runner, Git/PR/checkpoint/prompt/model modification or delegation occurred. Only this proposal was written.

## Exact source pins

- `three_site_common_mode_source/PROPOSAL.md`: `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb`.
- `three_site_common_mode_source_check/REVIEW.md`: `af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb`.
- `three_site_common_mode_actual_interface/PROPOSAL.md`: `9225b6ea6533dea56db4f8b7157deac5c6f52e5927b554052c59299622a13957`.
- `three_site_common_mode_actual_interface_check/REVIEW.md`: `e9b32196906e1d4b5010ac9b30d348e438d6e88fcdac82d51ae107f3f7ba1cea`.
- `three_site_common_mode_local_core/PROPOSAL.md`: `e817e63d7b6e7d1ba7d87db2322b8b5b7dd88b028fdbdd59962d4c3898713dcf`.
- `three_site_common_mode_local_core_check/REVIEW.md`: `644e29302a077f72e940c7396c562bf1ba87a5741f60a66c86dc7f6899972d77`.
- `three_site_common_mode_traveling/PROPOSAL.md`: `0abafe7b46fe6c93df110df8bc1e7a9dbc3a4eca30d38dbdea619337ca75940d`.
- `three_site_common_mode_traveling_check/REVIEW.md`: `4ac2571d63c5c6b4e7d7ea4e490a224b1e3d9d0a34b7ca4d82bce7fcc5038bdd`.
- `three_site_common_mode_reference_time/PROPOSAL.md`: `646f26bdb76fbb0b5c8144d492f094c6ffd191fd7312a6c77373fdc069b9d4de`.
- `three_site_positive_hopping_reexpression/PROPOSAL.md`: `9fa50cd2da480d59765aa5fbd7c556728a08ac4c385234dc055c26220b93a5d4`.
- `three_site_positive_hopping_reexpression_check/REVIEW.md`: `1e9630995e29cea591048983768658b0421b6b5658d3ac7bbbe0fa6dd034b956`.
- `output_lead_weight/PROPOSAL.md`: `58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf`.
- `output_lead_weight_check/REVIEW.md`: `1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd`.
- `slow_lead_resources/PROPOSAL.md`: `84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967`.
- `slow_lead_resources_check/REVIEW.md`: `dd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe`.
- `three_site_common_mode_reference_time_check/REVIEW.md`: `0a49ed087c65465fb6df43783135afdbfe64b0c18d4d280a68bbb0d9a420a39d`.
