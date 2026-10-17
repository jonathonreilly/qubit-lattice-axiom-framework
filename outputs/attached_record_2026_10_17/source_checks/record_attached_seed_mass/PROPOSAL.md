# Attached record device: full seed matrix omitted-mass bound

Status: authored conditional attached-device estimate, awaiting distinct checking. It depends on the provisional full attached endpoint bounds specified below, whose separate review was active during this derivation. No prior unattached actual mass or runtime is imported.

For the actual fixed attachment, kappa=1e-8 and q halfwidth h=4e-6, let I be the UNION of the two physical energy windows centered at c_att+1+2j and c_att+3+2j. The proposed full four-old-input seed estimate, including supplied record0 and arbitrary passive reference, is

    ||E_Hatt(R\I) V_seed|| < .001057.                  (1)

The corresponding full seed matrix omitted mass is<1.116e-6. This includes ALL outside spectral types. Local absence of singular seed mass is derived from the complete finite inverse chain, not assumed from a small reflection coefficient. The estimate establishes the omitted-state component for a later herald interface; it does not supply that interface's outgoing profile, returned rays, full local record1 norm or success claim.

## Sources, exposure and exact scope

The new endpoint source is ../record_attached_emitter_bound/PROPOSAL.md, verified SHA2562b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9. I authored it; its mathematical conclusions remain provisional pending a different checker. Its attachment dependency is ../record_attached_kernel/PROPOSAL.md fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457. Those files freeze the eighteen-edge cable, source/endpoint partition, gate/load reference planes, full eight-coordinate background bounds and actual emitter Schur formulas. No alternative cable or cap is inserted here.

Read the complete corrected matrix-measure interface ../record_seed_matrix_mass/PROPOSAL.md at e1abe3233bfe4b0e3d5e623240df9df9e80a35f7f3d081ab3e41944f06c6dd5d. Its review ../record_seed_matrix_mass_check/REVIEW.md at825c69bad1436e83523b2d901325ee2661c6128cd6fd73d4ee77a1bf2b6f5712 was authored by me; its valid reference-regularity hypothesis and proof are reused, not independently rechecked by their own checker here. The exact reference measure proof/check1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae was previously read completely and its hash reverified unchanged. Its scope is the uniform half-line emitter chain with equal2j diagonals,0<kappa<j and emitter-basis seed.

The current converter construction and necessary source packet were completely read during the endpoint derivation at canonical converter note f8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311. Original full finite-core inverses, fixed real B projections, exact calibration and supplied coefficients remain conditional inherited premises. Temporal conclusions and the old attached/unattached mass numbers are not proof inputs.

Parent requested this actual full-matrix normalization step and exposed the suggested four-chain reference. This is author work after that exposure, not independent discovery or independent checking of my prior endpoint bounds. Applicable previously read workflow/proof discipline is reused. No scientific execution, numerical integration/sweep/solver, delegation, W/Git/checkpoint/prompt/model change or publication occurred. Only source reading/hashing and this deliverable; no editable prompt file changed.

## 1. Physical windows and parity organization

Use the physical energy Lambda and remove only the COMMON scalar c_att, writing lambda=Lambda-c_att. For b in{1,3}, set

    I_b=[c_att+b+2j-d,c_att+b+2j+d],
    d=2j sin h, h=4e-6, I=I_1 union I_3.

These are common physical spectral sets for ALL old inputs. They are disjoint because d<2.4e-8 and their centers differ by2. For Lambda in I_b, define delta=lambda-b-2j and the unique q in[pi/2-h,pi/2+h] satisfying lambda-b=2j(1-cos q). Then |delta|=2j sin u with u=|q-pi/2|, and u≤|delta|/.0053.

The old parity X1X2 commutes with literal K, B, the source contacts and all head couplings; the new record contact acts only on the separate record. Thus each conserved record-X sector further decomposes into the same two old-parity sectors. In each parity the full old/source fiber has dimension8, with two vacuum old vectors of energies1 and3 and six excited-source directions. The vacuum input has one old vector of each energy in each parity. The seed matrix on the complete four-dimensional old space is consequently the orthogonal sum of its two2-by-2 parity blocks. No commutation of H_att with K or independent phase fitting is used.

All estimates below are uniform over b, parity and record-X sector. Off-diagonal logical entries BETWEEN old energies within a parity are controlled by a matrix inverse comparison, not set to zero. Cross-parity entries vanish because of the actual exact symmetry.

## 2. Genuine reference operator and its support

Define a reference consisting of FOUR independent copies of the uniform half-line emitter chain: emitter and every lead site have kinetic diagonal2j, emitter-to-first-site hopping-kappa, all later hoppings-j. Shift each copy by its literal old energy b=1 or3 and the same c_att. Embed the old basis vector in the emitter basis of its own copy. This direct sum defines an actual bounded self-adjoint reference with normalized positive four-by-four seed spectral measure.

The independently proved scalar reference identity applies because j>.0027>kappa=1e-8. Its emitter measure has total mass1, no atoms or singular component, and support exactly in the translated band [c_att+b,c_att+b+4j]. In momentum q its density is

    dmu_ref/dq=2kappa² sin²q/[pi |Dref(q)|²],
    Dref=delta+(kappa²/j)exp(iq).

Since4j<.012<2, the b=1 and b=3 continuum supports are disjoint. On I_b, the OTHER old-energy reference channel therefore has identically zero spectral density, not merely a small tail. Its resolvent is a nonzero REAL function there and must still be kept in a matrix inverse comparison. The reference phase of a scattering packet is irrelevant to this seed measure and is not used to alter the actual device's phases.

For computing full8 matrix inverses, extend the reference in each parity to one independent identical chain for EACH B eigenvalue beta_l, including all six excited directions. Its background endpoint Green matrix is exactly

    G_ref(lambda)=-Q(lambda)/j,
    D_ref,8=(lambda-2j)I-B+kappa² Q(lambda)/j,

where Q=wP+Q_C is the same selected open/closed root function as in the actual source calculation on I_b. Compressing the inverse D_ref,8^-1 to its two vacuum coordinates gives precisely the two-reference-chain emitter resolvent in that parity. The extra six chains are a mathematical comparison extension; they neither alter the desired four-chain seed measure nor duplicate any physical source qubit in the actual apparatus.

The reference restricted to I is absolutely continuous including cutoffs, satisfying the corrected matrix-mass theorem's reference hypothesis. Let p0 be its scalar mass on q=pi/2±h. Every old basis copy gives the SAME p0 in its own physical window and no mass in the other window. Thus

    M_ref(I)=p0 I_4,
    ||M_ref(R\I)||=1-p0.                               (2)

This is a maximum/eigenvalue statement, not a sum of four scalar tails.

For an explicit bound, A0=2j-kappa²/j>.00539 and the exact scalar tail obeys

    1-p0<=4kappa²/[pi A0² tan h]<1.1e-6.              (3)

The last inequality uses pi>3.14, tan h>h and the supplied j>.0027. It is a new reference-tail substitution for this window, not an import of actual attached mass.

## 3. Full endpoint matrix difference, including complements

From the provisional attached endpoint derivation, in every selected eight-fiber sector,

    ||G_att,s||<401,
    ||(G_att,s)_PC||,||(G_att,s)_CP||<2e-24,
    ||Dcc_s^-1||<6,
    |D_s|>.99 sqrt(delta²+gamma²), gamma=kappa²/j.

Here D_s is the selected scalar AFTER full emitter Schur elimination; Dcc_s is its actual seven-coordinate emitter complement. The stronger reference comparison below is made BEFORE that elimination, to avoid replacing a full matrix by one selected element.

The original endpoint scalar approximation and attachment update give

    |(G_att,s)_jj+w/j|
      <7.42e-18+40904u+1e-24+1e-48.                  (4)

For the CC block, the original free endpoint obeys ||G_free,CC+Q_C/j||<1e-24. The attachment update is the ordered product

    K_eff r(1-S_eff r)^-1 B_eff+F_closed,

with ||C K_eff||<7e-26, ||B_eff C||<2e-23, |r|≤.000132, inverse denominator<1/.99986 and ||F_closed||<4e-49. Therefore its CC norm is<5e-49 and

    ||G_att,CC+Q_C/j||<2e-24.                       (5)

This retains both the other vacuum coordinate and ALL six excited-source coordinates. The reference has zero PC/CP blocks in the fixed real B basis. Summing the four block norm bounds (a safe operator-norm triangle bound) using(4),(5) and the two actual cross ceilings proves

    ||G_att,s-G_ref||<8e-18+41000u
                       <=a0+b0|delta|,
    a0=8e-18, b0=7.74e6.                            (6)

There is slack between40904 and41000 and between7.420007e-18 and8e-18. Thus the additional cross/complement blocks are paid explicitly without inventing a zero floor. The exact matrix emitter denominator difference is kappa² times(6).

## 4. Energy-resolved FULL inverse bounds

Let r_delta=sqrt(delta²+gamma²). Throughout I_b, r_delta<2.5e-8, since d<2.4e-8 and gamma<1e-16/.0027. The actual block inverse can be written as its rank-one resonant Schur term plus the complementary inverse. The cross multipliers have norm at most6kappa²*2e-24. Therefore

    ||De_s^-1||
      <=(1+12e-24 kappa²)²/(.99 r_delta)+6
      <1.02/r_delta.                              (7)

The bound is on the complete8-by-8 matrix, not just its vacuum diagonal or its maximum at the band center. The additive complement6 is absorbed using6r_delta<1.5e-7.

For the reference8 matrix the selected denominator is Dref. Its real part is delta[1-kappa²/(2j²)] and imaginary part gamma sin q; both scale coefficients exceed.999. Its seven closed denominators have inverses<6 from the same bare gap>.185 and |G_ref,C|<1/[.0027(60-1/60)]<6.18. Since the reference is diagonal,

    ||D_ref,8^-1||<=max{1/(.999 r_delta),6}
                   <1.01/r_delta.                 (8)

These are simultaneous estimates of the actual and reference full emitter inverses. No squared center-only1/kappa bound replaces their energy dependence.

The exact noncommuting resolvent identity gives

    De_s^-1-D_ref,8^-1
       =De_s^-1 [D_ref,8-De_s] D_ref,8^-1.

Combining(6)--(8) and1.02*1.01<1.04 yields

    ||De_s^-1-D_ref,8^-1||
       <1.04 kappa²(a0+b0|delta|)/(delta²+gamma²).    (9)

Let V_vac be the isometric inclusion of the two vacuum old coordinates. Actual and reference seed resolvents in that parity are exactly V_vac*De_s^-1 V_vac and V_vac*D_ref,8^-1 V_vac. Compression is contractive, so(9) bounds their full2-by-2 difference, including old-energy off-diagonals. Combining the two orthogonal parity blocks costs a MAXIMUM, not a sum or sqrt(2). Hence(9) holds for the full FOUR-BY-FOUR seed resolvent difference in each record sector on each I_b.

## 5. Actual local spectral regularity

For each fixed record sector and parity, the graph consists of a finite interaction region attached to one final uniform lead with eight internal channels. On either specified physical window exactly one channel is propagating and all others are separated from threshold with signed decaying roots |s_l|<1/60. The open velocity is>.0053. Each selected outgoing root therefore has an analytic continuation on a complex neighborhood of any real point of the CLOSED window on its retarded sheet; threshold branch points are absent.

The following COMPLETE inverse chain is an explicit dependency of the endpoint derivation: the original source's finite matching inverse and converter/Dirichlet inverses; both-port gate inverse, its one-output load inverse, all closed return inverses, the selected source/load feedback denominator>.99986; and the full emitter inverse controlled in(7). These permit recovery of every finite source, cable, gate and emitter coordinate. A putative dark finite-region eigenvector would be a kernel vector of this full finite matching system, not an omitted scalar scattering channel. Its invertibility rules that out at every real point of the windows.

Because the finite matrix entries are analytic in the local root branches and its determinant is nonzero on the real windows, its inverse extends analytically near each such point. Compactness supplies a finite cover and bounded continuous boundary limits for the full seed matrix, including at both cutoffs. This uses only local complex neighborhoods from determinant nonvanishing; it asserts no quantitative wide strip or temporal contour bound.

Stone's formula, with these uniform upper-boundary limits, identifies the actual matrix seed measure on the windows with the continuous density -Im F_s/pi. There are no atoms, singular-continuous seed components or hidden cutoff atoms there. Outside I no spectral-type assertion is needed or made. If any inherited full finite-core inverse premise fails, this regularity argument and the mass conclusion must be reopened; small open reflection alone would not prove them.

## 6. Integrated density comparison on BOTH physical windows

Since imaginary part is norm-contractive, the full matrix density difference on I_b has integrated norm eta_b bounded by1/pi times the integral of(9). With delta in[-d,d],

    eta_b < (1.04 kappa²/pi)
       [2a0 arctan(d/gamma)/gamma
        +b0 log(1+d²/gamma²)].                      (10)

This controls all logical entries on the physical window, even though the reference's other energy-channel density there is zero. Its real resolvent was still included in(8),(9); nothing was discarded by comparing only to a scalar line shape.

At the actual kappa=1e-8,

    d/gamma=2j² sin h/kappa²<720000,
    log(1+d²/gamma²)<28.

An elementary witness for the latter uses e>8/3, (8/3)^5>130, (8/3)^3>18 and130^5*18>1+720000². Thus the a0 term in(10) is at most1.04 j a0<2.496e-20, while its b0 term is less than

    (1.04/3)*1e-16*(7.74e6)*28=7.51296e-9.

Hence eta_b<7.6e-9. There are TWO disjoint physical windows, so the integrated full matrix comparison on their union is

    eta=eta_1+eta_3<1.52e-8.                        (11)

No extra factor for the two parity blocks or four input columns is taken, because(9) is already a full operator norm, but the two integration domains must indeed be added. This retains floor-plus-slope integration instead of paying the entire worst-band.0005 relative discrepancy as a missing-mass term.

## 7. Actual mass, coherent record0 and references

For each record-X sector, the actual normalized seed measure M_s satisfies M_s(R)=I_4. The reference measure is normalized and locally absolutely continuous with(2),(3). Integrating the full density comparison and using the Loewner argument of the corrected matrix-mass interface gives

    0<=M_s(R\I)<(1.1e-6+1.52e-8) I_4
                         <1.116e-6 I_4.            (12)

All outside point and other spectral components are automatically charged by exact total normalization. Since .001057²=1.117249e-6>1.116e-6,

    ||E_Hs(R\I)V_s||<.001057.

The physical supplied record0 embeds as (V_+⊗|+>+V_-⊗|->)/sqrt(2). For each common old/reference input, the two omitted sector vectors are orthogonal before any record projection, so their squared norms average. The common operator ceilings in(12) then give the SAME .001057 amplitude for the full record0 seed, with no additional sqrt(2) factor and no assumed interference cancellation. The physical windows use the same c_att in both sectors. A later record1 projection is a contraction.

Passive reference tensoring preserves all these full map norms. The amplitude is an unconditional omitted STATE norm, not a scalar return amplitude or a postselected error. No old target aging has been factored through noncommuting dynamics. This supplies one actual conditional input epsilon_sp for the all-time interface only; the attached outgoing complex profile, all other open rays, complete record1 local kernel and quantitative success remain unproved here.

## Next check and limitations

The most consequential checks are the full CC comparison(5), energy-resolved full inverse bounds(7)--(9), exact four-chain reference identification/support, the actual finite-matrix regularity implication and the TWO-window integration. They are new steps beyond the scalar endpoint bound. The original endpoint/source calibration and full finite inverses remain conditional; both preceding attached kernel and emitter estimates are provisional dependencies awaiting their distinct reviews. No theorem status is manufactured from this composition.

This work does not revalidate or transfer an unattached mass/runtime certificate, select a finite device, extend a contour, establish a heralded output map or assert native record supply. It is the proposed normalization/missing-mass leg of that larger attachment analysis.
