# Independent three-channel phase-quotient result v1

Reviewer: `/root/force_energy_bridge_check`; main author: `/root`. This report and its complete derivation were frozen before exposure to the new author working derivation or program. The only new root source read was `channel_quotient/TARGET_CONTRACT_v1.json`, SHA256 `979c4d60a83329ed4781279ac36a4d1e9d24989bbcb2102f03eada3b201030ae`. The source contract is preserved byte-for-byte here. Instrument ratios, phase-transfer law and nuisance independence are supplied premises. No raw data, network source, literature confirmation, actual residual, carrier schedule, empirical error budget or author implementation was accessed.

The full proof and qualifications are in `PRECHECK_v1.md`, SHA256 `fad46dbd5407d5bc3b9f77d002cae9c33f2b8a1753dad457c25a32fd01c82760`; its pre-execution freeze is `4fec7e9cba861ef30d5815beaa5924162037ca6e08448a617e8d7e5b273037dd`. The result is a conditional character classification, with constructive surviving cases and explicit shortcut failures. It is not a formal audit or a no-go for full radio tracking.

## Mathematical result

Write r_i=fK_i/fX_i and x_i=fX_i>0. The complete family of continuous torus characters is

    exp(2 pi i sum_i w_i dot Phi_i), w_i in Z^3.

Integer history invariance requires exactly those integer weights. Independent arbitrary real uplink/downlink plasma requires w_i dot a_i=w_i dot d_i=0 separately at each endpoint. Arbitrary constant receiver vector b requires sum_i w_i=0 as a real vector. There is no averaging or rounding in these conditions, and cross-endpoint cancellation cannot remove independently variable plasma.

For the supplied exact k ratios, define

    p=3007586755, q=-305348069, c=-2325375360.

The direct null line of the two endpoint plasma columns is lambda_i(p,q,c r_i). Because gcd(p,q)=1, integer weights force lambda_i integer. The third coordinate adds lambda_i c r_i integer. Thus irrational r_i permits only zero weight. For r_i=P_i/Q_i in reduced positive terms, put h_i=gcd(Q_i,|c|), L_i=Q_i/h_i. Every endpoint weight is an integer multiple of the primitive vector

    v_i=(L_i p,L_i q,c P_i/h_i).

Only the relative ratio must be exactly rational; no rationality of the common absolute scale x_i is required. A common absolute chirp with fixed r does not destroy this endpoint annihilator. Instrument commensurability still needs an actual physical supplier. A finite decimal encoding is not that supplier.

After discarding irrational-ratio endpoints, all receiver-free characters are exactly the integer choices satisfying

    w_i=lambda_i(p,q,c r_i), lambda_i in L_i Z,
    sum_i lambda_i=0, sum_i lambda_i r_i=0.

Equivalently they form the integer kernel of the two-row integer matrix with columns (L_i,cP_i/h_i). For K rational endpoints, its character rank is K-1 if all ratios agree and K-2 if at least two distinct ratios occur; K=0 has rank zero. This is a classification of the lattice, not a claim that arbitrary separately cleared rational nullspace vectors form a saturated integer basis.

Two endpoints therefore retain a nonzero character only at the same exact rational ratio. Three distinct rational ratios do allow a nonzero character: scale (r3-r2,r1-r3,r2-r1) to meet the stated divisibility restrictions. When there are only two distinct ratio groups, receiver cancellation separately annihilates the total lambda in each group. A repeated ratio can support an internal endpoint difference even if another singleton ratio contributes no weight.

Every surviving character is count-derived. Set integer count weights t_j=-sum_{i<=j}w_i. Then sum_i w_i dot Phi_i=sum_j t_j dot(Phi_{j+1}-Phi_j). Frequency-average data must first carry their supplied duration-to-cycle map; ordinary real frequency normalization does not preserve the same unit lattice. Separate receiver segments require separate cancellation conditions.

## Signal sensitivity is an additional condition

The surviving coefficient of G_i is

    s_i=lambda_i c k3 x_i(r_i^2-1), c k3=-2170350336.

The history functional is nonzero precisely when some participating endpoint has r_i!=1. At r_i=1, g_i is proportional to the uplink plasma column, so plasma removal also removes G_i. A nonzero character rank alone is insufficient: the ratios (1,1,2) leave a nonzero invariant supported on the first two endpoints, but it has zero G sensitivity.

More generally, a rational endpoint can participate if there is a second endpoint with the same ratio, or two remaining endpoints with distinct ratios. Thus a nonzero G history functional exists for one ratio group only when that group is nonunit and has at least two endpoints; for two groups only when a nonunit group has multiplicity at least two; and for at least three distinct groups through a triple construction. Irrational endpoints cannot rescue these conditions under independent per-endpoint plasma.

A fixed time-independent G0 is a narrower target. It survives some character exactly when the vector x_i(r_i^2-1) is not in the row span of the vectors (1) and (r_i), on rational endpoints. Fixed x and fixed r cancel constant G0; they can still retain changes in G. Fixed x and three distinct r values can retain constant G0 because a quadratic in r is not affine at three distinct points. These sensitivity claims are conditional derivatives/linear functionals, not claims about an actually observed signal.

An explicit successful construction uses r=(2,3,4), lambda=(1,-2,1), and x_i=1. The three signal coefficients are c k3 times (3,-16,15), with nonzero sum 2c k3. The corresponding count weights are -w0 and w2. This proves a concrete alternative to a broad changing-uplink obstruction.

## Failure witnesses and finite-error obligations

The exact controls and proof preserve four important failures:

1. **Integer-incompatible real projection.** At irrational r the real plasma-free row exists, but its projected integer ambiguity contains an integer generator and an irrational generator, hence is dense. It gives no nonconstant continuous scalar invariant. This is narrower than impossibility for the original data or a restricted nuisance family.
2. **Two different endpoint ratios.** Plasma-free rows at r=2 and r=3 cannot form a receiver-free two-endpoint character. Their uncancelled receiver coefficient can generate a half-cycle change from a constant real receiver offset while G and plasma vanish.
3. **Rounding a near-rational ratio.** Weights designed for r0 leave exact nuisance coefficients lambda c k3/x*(r0/r-1) and lambda c/(k3x)*(r0/r-1). For any r!=r0, arbitrary plasma amplitude can turn the first leakage into exactly half a cycle. The control uses r=2+sqrt(2)/10^9 in exact algebraic arithmetic. There is no uniform approximate cancellation from small ratio error alone.
4. **Uncarried normalization.** Dividing a primitive integer row by B produces period 1/B, not period one. A unit slip changes the incorrectly normalized quantity. Carrying the actual period restores the original error-to-period ratio and does not create precision.

For a separately supplied endpoint error box, the sharp scalar error radius is eta_W=sum_ij |w_ij|epsilon_ij after shared endpoints have been combined. If eta_W>=1/2, that box projects onto the whole unit output circle; the scalar character supplies no phase exclusion. Other correlated sets must retain their actual projection. No physical error bound is available in the task premise.

For the primitive r=2 two-endpoint character, the exact l1 weight norm is 15927371088. With a common independent per-coordinate box radius epsilon, the whole circle is covered once epsilon reaches 1/31854742176 cycles. This is a synthetic algebraic threshold and not an observed receiver limit, a precision claim from storage, or a proof that the route fails physically. Large coefficients also amplify G, but the quotient still has unit period. The correct physical uncertainty must be supplied before judging usefulness.

With no quantitative restriction on real e, an arbitrary phase representative is compatible with zero signal by assigning it to e. This shows that algebraic cancellation alone cannot support a positive physical residual or energy bound; it does not claim actual instrument errors are unbounded. If a physical supplier provides a bounded field functional L_W, dual norm sigma_W and error radius eta_W, then the conditional norm floor is max(dist(theta,Z)-eta_W,0)^2/sigma_W^2, with the zero-response compatibility case and separately positive energy conversion. None of those physical suppliers is chosen here.

## Independent implementation and result

`independent_channel_controls_v1.py`, SHA256 `d1c79707eca7140f6ebc53a41f78920358f420411d4f5c2a218766f2772d917f`, was frozen after the proof and before execution. The script neither imports nor reads any author implementation. It constructs an independent direct cross-product oracle from the original rational columns, clears denominators and primitive gcds, and compares it with the derived integer classification at nine rational ratios. It directly substitutes weights into both plasma columns and the signal column.

The irrational controls split exact Q(sqrt(2)) columns into rational and irrational coordinates and establish rank three. This supplies an exact check at three quadratic-irrational fixtures; the general irrational result rests on the proof, not on those finite fixtures. Ten endpoint configurations test receiver-kernel rank, actual nullspace samples, zero/nonzero history sensitivity and the independent constant-G row-span test. Sample integer vectors span the real kernel but the program does not claim they enumerate a full integer-lattice basis.

A separate forward phase fixture supplies unrelated rational U_i,D_i, arbitrary rational receiver offsets, large independent integer histories and wrapped native M=2^32 representations. The successful three-ratio character agrees exactly with its G-only response modulo one. The exact count rewrite and six independent plasma perturbations preserve it. The fixture's signal phase modulo one is -5/13 for its declared x=(1,2,3) and G values; it is synthetic and not a physical data comparison.

The remaining controls demonstrate the failure witnesses, sharp endpoint-box support and circle coverage, rescaling of the correct error/period pair, unrestricted-error compatibility, and an explicitly supplied one-coordinate Hilbert norm example. Float and symbolic-irrational values are rejected by the function intended only for exact rational premises. It does not pretend to decide rationality of arbitrary measured input.

The single execution exited 0, with **126 of 126 controls passing** and empty stderr. No failed code execution or repair occurred. The exact results file is `INDEPENDENT_RESULTS_v1.json`, SHA256 `ab81224aad175c6cacddbb86fb2c67edb08370196786c380db916f8b6f2cad64`; stdout is `51bdfeba7d51e06b3b549abcc7a6e4a79e6363f9992c9849a3aab28da5c15b3d`. Finite-control counts are supporting checks, not a substitute for the general proof or an independent empirical experiment.

## Exposure and remaining scope

All new writes are confined to `channel_quotient/independent_math_v1`. The full immutable inventory and source identities are in `INDEPENDENT_IDENTITY_v1.json`. No branch, Git/index, lock, campaign status, canonical source, PR, main repository state, raw-data file, cache, or formal audit record was modified. No other agent was delegated and no external messages or network calls were made.

The remaining physical obligations are the actual carrier/phase-transfer law and ratios, matching of emission events and retarded rays, common plasma identifications, receiver segmentation, quantitative errors and any restrictions on histories or plasma. Exact common synthesis, a calibrated restricted nuisance family, or another measurement channel could supply routes outside the stated character problem. No initial scalar state, error magnitude, noise distribution, or selection rule was introduced to close these obligations.
