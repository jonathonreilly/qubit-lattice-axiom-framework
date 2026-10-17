# Pointwise converted profile and weighted actual mass: selective independent check

Disposition: conditional support for the mass <4.43e-6, outside-band amplitude <.002105, per-column initial comparison <.002110, and arbitrary old/reference initial comparison <.002986 at the fixed kappa=1e-8. No load-bearing mathematical defect found. The initially found minor endpoint notation defect is resolved in the final source: in proposal sections 1–2, the scalar inequalities written `<23s`, `|t_c-i|<3x`, and `|t_c²+1|<6x` are now non-strict at s=x=0. Their left and right sides both vanish there. The converter reflection ceiling ≤1.22x was corrected at the same time. The subsequently retained positive closed-feedback floors make all final strict ceilings valid without changing constants.

Final reviewed source: ../bandcenter_weighted_profile/PROPOSAL.md SHA256 ab3b7cbfb3ff8159541564ca088b23072f42c075149225b34318d11d581a9ed0. Verified the complete diff against preserved PROPOSAL_v1.md at 43fce84f72c529e59ef9d1f7cb369948916d249c5a5639ab675209b1ad2f4093: exactly four zero-floor strict-to-nonstrict corrections and two explanatory sentences. No other argument changed. The unchanged analytical review below transfers to this final source; there are no outstanding requested fixes.

This supports a conditional initial spectral-comparison improvement, not runtime, temporal escape, a finite output window, common-j robustness, physical supply, or retained/audit status.

## Sources, exposure and verification limits

Read the entire frozen ../bandcenter_weighted_profile/PROPOSAL.md at SHA256 43fce84f72c529e59ef9d1f7cb369948916d249c5a5639ab675209b1ad2f4093. Read canonical correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md lines 163–319 at SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. These supply the necessary fixed-band source, calibration, filter, mixer and port-kernel premises. No other current-note changes are endorsed. An initially overbroad path inventory produced truncated output; the required canonical passage was subsequently reread in a separate complete output. No truncated result is counted as completed reading.

Read completely, and verified the exact SHA256 identities of:

- ../bandcenter_converter_composition/PROPOSAL.md: 1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78.
- ../bandcenter_converter_composition_check/REVIEW.md: f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c.
- ../bandcenter_converter_endpoint/PROPOSAL.md: 22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a.
- ../bandcenter_converter_endpoint_check/REVIEW.md: 200268709480f1533050f5d197a4bed7a2acaefa5f4a22a662938ddb504619c6.
- ../bandcenter_reference_measure_check/REVIEW.md: 1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae.

Applicable AGENTS.md identity is febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0; SCIENCE_WORKFLOW.md is 71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3. Read installed physics-claim-reviewer skill 9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455, candidate-worktree freshness instructions, proof-search governance and relevant review-depth/model boundary. Used the tasked local source revision; no Git fetch or claim of remote freshness. The explicit same-model/no-delegation brief governs this bounded check.

I am not the proposal author. The parent supplied its target numbers and requested adversarial checks before reading; the full proposal and prior reviews are exposed inputs. The review reconstructs its new load-bearing inequalities analytically, without claiming independent origin, model diversity, or fresh verification of all ancestry. In particular, original positive central calibration, full finite-core invertibility, fixed real spectral projections, and inherited complementary bounds remain conditional dependencies. No scientific computation, solver, integration script, numerical rerun, delegation, W/Git/checkpoint/prompt/model modification or publication occurred. Deterministic reading/hashing and this report only. No editable prompt file changed.

## Center-plus-derivative reconstruction

The exact common phase r0=-exp(2ik) has derivative magnitude 2. The fixed unit phases zeta and omega do not add derivatives. Integrating the source derivative ceiling 700 from the calibrated center therefore gives d0+702s, retaining d0=1.76e-13. The filter half-sum/half-difference derivatives are bounded by 5, and differentiating b/z adds at most |b|≤1, so the relative transmission derivative is ≤6. Since b(k0)/z0=i, its square differs from -1 by at most 12s using |b/z|≤1.

In the exact scalar concatenation, adding the bare reflector leaves a direct term ≤5s and a reflected numerator bounded by (12+5)s over 1-5s. This is ≤23s for 0≤s≤1e-6. Adding the uniform physical closed correction gives 23s+1e-20, without assuming a vanishing center or a derivative for that correction. The real mixer divides this by two. Thus reflection ≤11.5s+5e-21 and transmission error ≤d0+713.5s+5e-21 justify the relaxed slopes 12 and 714. The d0 term cancels from the sum channel by using the same bare reflection, not by discarding its uncertainty.

The exact nominal converter map places the entire new band inside the old certified band before invoking k'<.24. Integrating that derivative yields s≤.24x. The converter reflection numerator is zero at the center and has derivative <.029, while its denominator has central magnitude >.024 and the same derivative bound. Thus the displayed reflection ratio ≤1.22x is valid. The flux transmission retains exp(iq) and sqrt(S0 sin q/sin k). The inequalities |sin k-S0|≤.24x, sin k>.4 and 1-sin q≤x²/2 yield the pointwise square-root bound used for ≤3x. Unitarity gives the square bound ≤6x.

In the exact multiple-return matrix, the open cost is bounded by rho+6x+rho/(1-rho), below 9x for x>0 and zero at x=0. The independent full closed-feedback correction remains <1e-86 throughout, including the center. Comparing first to the loaded unitary matrix avoids multiplying an uncontrolled full operator by a missing inverse factor. Combining with the mixer bounds gives slopes 11.88 and 180.36 and constants 5e-21+delta_c (plus d0 for transmission); hence r(x)=1e-20+12x and t(x)=d0+1e-20+181x are safe. The common phase uses actual mapped k(q), not four individually fitted phases.

## Full endpoint/emitter profile

The endpoint bounds epsilon_G=1e-24 and epsilon_L=1e-23 remain valid uniform bounds; smaller pointwise open errors do not invalidate their previously checked inverse margins. The full resonant Schur denominator is E-2j-kappa²Gjj-kappa⁴GjC Dcc^-1 GCj, with all seven complementary coordinates and ||Dcc^-1||<6. Dividing its difference from Dref by Im Dref gives exactly the proposal's two contributions 2r/[(1-r)sin q] and j[epsilon_G+6kappa²epsilon_G²]/sin q. Since r<1.21e-5 and j<.003, the ceiling d=2.0001r+4e-27 has margin. It implies positive imaginary denominator control, not merely a modulus estimate.

The reduced outgoing numerator is -kappa[L_j+kappa²L_C Dcc^-1 GCj]. Its plus sign and matrix order follow by solving the complementary emitter equation; no scalar commutation is assumed. L0 has zero complementary columns, so ||L_C||≤epsilon_L. Relative to the reference numerator, the omitted-row bound is at most j epsilon_L+6j kappa²epsilon_L epsilon_G before the near-one denominator conversion. The 1e-25 allowance safely covers it and the 4e-27 denominator allowance.

Writing the leading ratio as (t/(rho_n omega_p))/[(1+R w^(2ell+2))(Dj/Dref)] gives error numerator t_error+r+d+rd and denominator (1-r)(1-d). This directly checks the proposed complex, rather than magnitude-only, comparison. The denominator exceeds .99996. The r² contribution fits the extra .0001r in t+3.0002r+1e-25; the 4e-27(1+r) contribution fits the allowance. The relaxed slope after division is below 220, and the intercept remains below 1.8e-13 while retaining d0. Thus P holds on the full closed band, including its nonzero floor at the center.

## Finite-band moments and actual mass

For u=q-pi/2, Dref=A0 sin u+iB0 cos u, so dividing its squared norm by cos²u gives exactly dmu0/du=2kappa²/[pi(A0²tan²u+B0²)]. This is the angular displacement coordinate, not the cotangent coordinate used for full normalization in the reference review. No Jacobian factor is missing. Evenness and tan u≥u give the first moment by integrating u/(A0²u²+B0²); its antiderivative is log(A0²u²+B0²)/(2A0²). The resulting factor is 2kappa²/(pi A0²), as stated. Bounding u²/(A0²u²+B0²)≤1/A0² gives the second moment ceiling. Both integrals stop at sigma and are unnormalized.

The positive floor contributes a p0 to the first profile integral, not zero. In the checked actual one-channel scattering representation, |F_j|≥(1-e)|Fref| with e<1. Hence p_actual≥p0-2a p0-2b M1, after discarding a nonnegative square term. Total actual seed mass is one, so 1-p_actual≤(1-p0)+2a+2b M1. The inference pays all outside-band spectral mass, including atoms, without assuming global actual absolute continuity. Its essential imported bridge is the full finite-matrix regularity and spectral-jump proof in the endpoint review; an open scattering bound alone would not suffice.

At kappa=1e-8, A0>.0053 and A0 j sigma/kappa²<180000 are safe. The rational comparison using e>8/3, (8/3)^5>130 and 130^5>32400000001 proves the claimed logarithm ceiling 25. The resulting first-moment ceiling <6e-11 and second-moment ceiling <4.75e-18 have margin. Using the separately checked reference tail <4.4e-6, the total mass is below 4.4e-6+3.6e-13+2.64e-8<4.43e-6. The square .002105² exceeds 4.43e-6. No smaller-coupling claim may freeze the logarithm at 25; the proposal correctly restricts these rounded numbers to the fixed coupling.

## Initial comparison and aggregation

Minkowski's inequality in the actual spectral representation gives the in-band vector difference ≤a sqrt(p0)+b sqrt(M2)<4.8e-7. Positive normalization of Fref costs 1-sqrt(p0)≤1-p0<4.4e-6. Adding the outside-band amplitude gives <.002110 per column. The target is a normalized packet in the actual scattering transform, with its actual incoming reflection phase and full finite/source/complement coordinates. It is not a spatially escaped output state.

For the two old-energy columns in a fixed parity, the error operator norm is bounded by its Hilbert–Schmidt column bound sqrt(2) times the largest column error. This does not assume the error vectors are orthogonal. Orthogonal parities combine by a maximum, and tensoring a passive reference preserves the operator norm. Since .002110*1.415<.002986, the stated all-old/reference ceiling follows. Target packet bands are disjoint within parity as recorded in the endpoint check, so normalization does not conceal a nonisometric target map.

The source identities and scope support this selective new result on the corrected final source. Temporal escape, localized derivative/contour estimates, finite M, supplier robustness and comparison objectives remain separate obligations.
