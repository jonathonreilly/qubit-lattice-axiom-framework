# Direct microscopic finite-seed composition: distinct check

No required mathematical correction was found in the frozen complete proposal. The early microscopic contact comparison, exact packet evolution, finite boundary residual and common-target normalization compose as stated. Each of the twelve prescribed allowances is below epsilon/16, giving uniform complete-output isometry error below 3epsilon/4. The Theta(Lambda^-1 epsilon^-6) duration is valid for this explicit sufficient parameter family, with Theta(epsilon^-4) size and smallest positive supplied coefficient Theta(Lambda epsilon^3). It is not an optimality, practical-performance or fixed-device speedup claim.

## Source identities and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

New complete source read and SHA-256 verified:

* `common_product_microscopic_finite_seed/PROPOSAL.md`: `452231afa993c7a14e1b55c0b302d499e0284ce02266f8a1039a75474053392a`.

Previously fully read sources and checks in this same session, reused after their hashes were refreshed unchanged:

* `common_product_microscopic_scattering/PROPOSAL.md`: `59b59ea3fc51e6ae364716a63ff4b9e001390cba112f48f0b4214c01318865a6`.
* `common_product_microscopic_scattering_check/REVIEW.md`: `3e1dc92540af46ec3a20b928001c7796795bf6c6a6b8580fe307c3e3ca3f8eb6`.
* `common_product_microscopic_packet/PROPOSAL.md`: `c105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e`.
* `common_product_microscopic_packet_check/REVIEW.md`: `c27e7a93c6d76e8261d5a081c3af6ad94438aa803a69354dfb7d2e762e6e0234`.
* `common_product_refined_resource_family/PROPOSAL.md`: `79f5bd9c07fe0eb0f37d051446f69759a32559ba7ce9e8bb835db01287188bb3`.
* `common_product_refined_resource_family_check/REVIEW.md`: `5999fccf27396704e010049ee62fd5c342afcbc5fbd8f335ee11dd46783bb575`.

The earlier complete reads of the launch `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`, derivative source `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`, physical cell `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`, and finite composition `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b` are reused at their recorded scopes. The final source, rather than the preserved preclarification revision, is the object checked here.

I authored the listed component checks. They are shared exposure, not prior verification of this composition. ROOT suggested the contact route and parameters, read the complete proposal, and requested notation/projection qualifications; that preliminary assessment is not evidence for the conclusions here. I read the frozen formulas before reconstructing their interfaces and budget. This is a distinct source-exposed same-model check with inherited effort, not blind or model-diverse replication. Existing workflow snapshots are reused; no formal audit or retained status is assigned.

## 1. Early common-space operators and invariant reference sector

On each port the reversed standalone launcher has all one-head diagonals 2j and uniform hopping -j down through n=0 into n=-1. The extended finite microscopic operator instead has endpoint diagonal j+a_p, no connection from 0 to -1, and the actual hopping -b from each n=0 endpoint to the mediator. The negative exterior begins at -1 with Dirichlet diagonal 2j; its internal coefficients otherwise agree. Both operators have the same decoupled positive exterior at n>=M+1 and the same mediator diagonal D_p. Therefore the only diagonal change is a_p-j=+j enabled or -j disabled at n=0. No mediator diagonal change or effective endpoint-to-endpoint bond is missing.

The two port contact matrices are [[±j,j],[j,0]]. Their exact norm is (1+sqrt(5))j/2<2j. As orthogonal port copies their combined norm is their maximum. The additional endpoint/mediator coupling has norm sqrt(2)b. The triangle bound ||V||<=2j+sqrt(2)b is consequently valid. Its support is exactly inside the specified contact projector, so V=V P_contact.

The reference emitter seed never enters the mediator or the disconnected positive exterior. Its invariant subspace is the direct sum of the two checked standalone launchers, each bounded by 4j. This remains true for coherent program input because the only program-dependent reference term acts on the unused mediator. The full reference or actual operator need not have norm 4j; both are bounded for fixed parameters, and their possibly large D_p is allowed in their unitary propagators.

From n=M, reaching contact site 0 takes at least M hopping steps. Diagonal factors cannot decrease that distance. Thus P_contact h_ref^r E_seed=0 for r<M, including the mediator row. Taylor expansion restricted to the invariant reference subspace gives the tail starting at M with frequency bound 4j. Ordered Duhamel puts the actual unitary on the left and V times this reference evolution on the right. Bounding the integral by t0 times the terminal positive Taylor envelope yields exactly u0(2+sqrt(2)/eta) times the tail, because b/j=1/eta. The cap two applies to the normalized evolved seed maps. This correctly avoids applying a false 4j norm bound to the physical microscopic generator.

## 2. Launch-to-microscopic packet interface

The standalone launch estimate applies to the reference evolution with the decoupled mediator vacant. Under x=ell-n, its outgoing Fourier phase becomes `(ell-n)k-t0E`, so the translation is exp(ik ell), not exp(ikM). Dividing chi g_+ by the positive sqrt(p) does not change the normalized projected target. The full-integer Fourier continuation has norm one; its projection n<=ell excludes the reference source at M=ell+1. Delta_launch<1 establishes that the normalized projection is nonzero. The right-tail replacement costs 2d_right with gap 1+t0vmin.

For the microscopic packet, the negative-coordinate discrepancy is the missing incoming tail, the nonnegative-coordinate discrepancy is the exact Q-dependent outgoing wave, and the mediator discrepancy is its R integral. Their coordinate spaces are orthogonal, giving exactly the square root in (6). The two lead gaps are ell+1-t0vmax, while the mediator gap is ell-t0vmax; the stronger positivity condition is explicitly supplied. The source spectral phase, Q phase, normalization and dispersion are retained throughout.

The triangle inequality then proves (7). Both its final compared states are zero at negative coordinates, so the auxiliary integer-line embedding creates no uncharged tail. This comparison does not equate finite and infinite spectral projections. It bounds the entire actual vector, including any component absent from the constructed microscopic packet. Thus it does not need a false assertion that the seed or either Hamiltonian has no bound-state contribution.

## 3. Exact finite exterior identification and output normalization

On the infinite microscopic leads, adding (j-gamma) adjacency on (ell,ell+1) changes hopping -j to -gamma. Adding j adjacency on (ell+1,ell+2) removes the next hopping. No onsite diagonal changes. The finite block at its outer end is exactly `Q_gamma+(j-gamma)n_ell+(2j-gamma)n_(ell+1)` plus the preceding j bond, giving diagonal 2j at both outer sites. The exterior first site retains its own Dirichlet diagonal 2j. The actual mediator and both microscopic couplings remain unchanged. Hence h^mic+Delta is precisely the finite microscopic device direct-summed with that exterior generator, not a zero extension or an effective-cell model.

The contact matrix norm is d_hop, with no factor for program, port or reference copies. The incoming contact amplitude uses G derivatives; the outgoing amplitude uses H derivatives and therefore pays Q' and Q''. The twice-IBP expression and integrated coefficients are those checked for the microscopic packet. The mediator contributes no extra contact residual because Delta annihilates its coordinate. Positive integrated envelopes through tplus bound all shorter durations. Propagating the initial full-vector error by the perturbed unitary proves (9) without assuming that actual contact amplitudes are independently negligible.

For q=tvmin-ell>0, q increases while t/q and t/q² decrease: the latter derivative is `-(tvmin+ell)/q³<0`. Therefore both the late lead and mediator envelopes are maximal at tminus. The outgoing scalar tail envelope is maximal at tplus. The fixed scattering discrepancy d_S applies uniformly. These facts give d_packet=d_L+d_S+m_L and the mixed-endpoint denominator 1-d_packet without assuming monotonicity of its quotient.

Exact microscopic packet normalization implies q_B>=1-d_packet. If d_packet<1 and d_O<1, positive normalization and ordinary-site truncation cost at most 2d_packet+2d_O. The retained interval 0<=n<=ell excludes both emitters, while the target sets the mediator vacant. All their actual amplitudes remain in the norm. B is a common scalar packet and C is unitary, so normalization and target phase are independent of the logical input and passive reference. Restoring exp(-i2bt) gives (10) on the entire encoded domain.

There is no omitted accumulated effective-cell term: the proof has changed its comparator to an exact physical packet and explicitly paid the initial match. Adding the old term is unnecessary, and declaring it zero for the old comparator would have been incorrect.

## 4. Simultaneous parameters and the twelve allowances

The fixed cutoff and exact normalized launch spectrum satisfy the checked bounds G0<2, G1<=100rho^-1, G2<=2000rho^-3 and B_minus<=200rho^-1. With rho=epsilon/256, eta²=zeta=epsilon/1024, eta<=1/32 and delta=epsilon/512, every scattering/packet coefficient hypothesis holds. The large u0 and ell satisfy the strict geometric conditions, including the stronger early mediator gap.

For the changed coefficients, H1<=100rho^-1+520/512<=200rho^-1. Also H2<=2000rho^-3+(52000/512)rho^-1+9200/512<3000rho^-3. Finally J0<=6eta and J1<=300eta/rho+840eta<=1140eta/rho. These bounds preserve all Q and R derivative terms.

The microscopic early prefactor needs more than the old loose inverse-distance factorial bound. Since M>=100u0, the tail ratio is <=1/25 and its first term is bounded using M!>=(M/e)^M. Thus the sum is <2*8^-M<=2/M²; the latter follows from 8^M>=M² for integer M>=1. Multiplication by the full u0(2+sqrt(2)/eta) gives

    E_early^mic <=(2+sqrt(2)/eta)/(5000u0)
                <1/(100u0 sqrt(epsilon))<epsilon/16.

The middle inequality uses eta=sqrt(epsilon)/32 and `2sqrt(epsilon)+32sqrt(2)<50`. Thus the large 1/eta contact strength is explicitly paid rather than dropped.

For launch and right-tail terms, sqrt(u0)=10^6rho^-1/epsilon yields the stated bounds 2R0<=2epsilon²/10^12, 2L0<=400epsilon/10^6, 2d_right<=208epsilon/10^6. Also 4sqrt(P)<=4sqrt(11)epsilon/256<epsilon/16. Each is below epsilon/16, and delta_launch<1 follows before using its normalized target.

The early lead match has combined derivative numerator at most 300rho^-1+8/50. Its gap is at least ell/2, giving a coefficient less than 500rho^-1/sqrt(ell). As sqrt(ell)>=10sqrt(u0), this is <=500epsilon/10^7. For the mediator, `J1+(2u0/q)J0<=1141eta/rho` and q>=ell/2 give <2300eta/(rho ell). At the late endpoint, uminus/q<3 gives numerator <=1176eta/rho and q>ell/4, hence <5000eta/(rho ell). The identity `1/(rho ell)<=rho epsilon²/10^14` makes both mediator allocations tiny; in particular m_early<epsilon/64, m_L<epsilon/64 and 2m_L<epsilon/16.

The lead bounds d_L,n_O<=230epsilon/10^7 still use the scalar G amplitude. Here d_S=max(13eta²,5zeta)=13epsilon/1024<epsilon/64. Consequently d_packet<3epsilon/64<1/2. Thus d_O<=2n_O<1, proving target normalization, and 2d_L<=460epsilon/10^7, 2d_S=26epsilon/1024, 2d_O<=920epsilon/10^7 are each below epsilon/16.

The boundary incoming coefficient is <=4000rho^-3. The changed outgoing coefficient is bounded by `3000+21*200+154*2=7508` times rho^-3, below 8000rho^-3. With the common prefactor below j, qi(t0)>=u0/2 and qo(tplus)=ell/4, the integrated allowance is <=8000rho^-3/u0+16000rho^-3/ell<=8160rho^-3/u0. Substituting u0 and rho gives less than `(8200*256/10^12)epsilon<epsilon/16`.

This separately verifies all twelve nonnegative allocations: microscopic early contact; two source residual/remainder terms; spectral tail; right-tail normalization; early lead match; early mediator; outer residual; late lead; scattering distortion; late mediator; final projection normalization. Their sum is strictly below 12epsilon/16=3epsilon/4. No cancellation or partial trace is used. Uniform isometry and unhalved channel conclusions follow with the stated factor two.

## 5. Exact scale, cap, counts and comparative meaning

The selected ratios give D0=Lambda epsilon/2048 and b=Lambda epsilon^(3/2)/65536. Computing b²/D0 gives j=Lambda epsilon²/2097152, and multiplying by rho gives gamma=Lambda epsilon³/536870912. These reproduce every constant in (18). D1>D0>2b and gamma<j hold strictly.

The physical terms are unchanged. Under the same combined-block convention, the mediator load is Lambda(1/2+eta zeta)<Lambda, central endpoints have Lambda zeta(3eta+4eta²)/2<Lambda, and the program, lead, source-adjacent and source loads listed in the source are also strictly below Lambda for eta<=1/32 and zeta<=1/1024. No auxiliary negative/exterior comparison sites count as physical qubits or blocks. Counts remain 8+2ell qubits and 9+2ell combined positive blocks.

At fixed Lambda, u0=10^12*256²epsilon^-4 and its rounded ell are Theta(epsilon^-4). Both dimensionless observation times have that order. Dividing by j of order Lambda epsilon² gives Theta(Lambda^-1 epsilon^-6), with tminus=(6/7)tplus and relative width 1/6. Gamma has order Lambda epsilon³. It is the smallest positive scalar coefficient: j-gamma and 2j-gamma exceed gamma, a0=2j exceeds it, b/j=1/eta>1, and `(D0-2b)/j=(1-2eta)/eta²>1`; D1-2b is larger still. This concerns exact coefficient magnitudes, not tolerance, eigenvalue gaps or supply cost.

Comparison to the checked epsilon^-14 refined sufficient family is on the same induced complete-output isometry convention, relative-width window, architecture and incident-load convention. The mathematical proof route and parameter family differ. The comparison does not establish optimality, actual-error reduction for a fixed device, practical speed, or an inherited old apparatus theorem. All enormous constants and supplied exact correlations remain real premises of the certificate.

## Limits and work record

The conditional result now supplies a full finite-seed comparison through exact microscopic packets, while retaining actual bound-state-related mismatch in the initial norm error. It does not identify spectral projections of different generators or assert vanishing seed bound-state weight. Supplied positive interactions, coefficient relations, site roles, occupation basis, absent couplings, legal programs and encoded input remain assumptions. There is no native-law derivation, fabrication-tolerance claim, capture/reset, permanent halt, stationary readout or practical resource guarantee.

Only this report was written. No scientific executable, numerical simulation, integration, symbolic solver, sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. All checks were analytical; hashing and directory creation were bookkeeping. No retained or formal audit status is assigned.
