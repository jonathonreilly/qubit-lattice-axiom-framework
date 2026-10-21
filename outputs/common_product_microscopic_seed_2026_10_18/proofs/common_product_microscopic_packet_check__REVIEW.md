# Microscopic packet bridge: distinct bounded check

No required mathematical correction was found. The displayed packet is an exact strong solution and is normalized by its remote-past incoming limit. The Q/R derivative constants, early/late comparisons and microscopic outer-contact residual are valid on the stated band and parameter domain. This normalizes the constructed packet family without claiming a complete scattering transform or absence of bound states. It does not yet identify the packet with a finite evolved emitter seed or establish a new runtime certificate.

## Exact pins and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, completely read and SHA-256 verified: `common_product_microscopic_packet/PROPOSAL.md`, `c105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e`.
* Previously fully read scattering source, hash refreshed unchanged: `common_product_microscopic_scattering/PROPOSAL.md`, `59b59ea3fc51e6ae364716a63ff4b9e001390cba112f48f0b4214c01318865a6`.
* My completed scattering check, hash refreshed unchanged: `common_product_microscopic_scattering_check/REVIEW.md`, `3e1dc92540af46ec3a20b928001c7796795bf6c6a6b8580fe307c3e3ca3f8eb6`.

The physical cell, ideal convention and finite-geometry sources identified in that check were previously fully read in this coherent session and are reused only at their stated scopes. The source's pending-check description reflects its assignment chronology; the now-completed scattering check is available. It does not itself check this packet bridge.

ROOT suggested the packet normalization approach and derivative calculations. I read the proposed packet formulas before reconstructing them. My earlier component checks are shared exposure, not prior verification of the new bridge. This is a distinct same-model source-exposed check with inherited effort, not blind or model-diverse replication. No separately developing finite-seed integration was read or used. Existing workflow snapshots are reused, and no formal audit or retained status is assigned.

## 1. Band derivatives of the exact columns

The exact source gives v_0=-2E/(D0-E), v_1=-2D0/(D1-E), E'=2j sin k and E''=2j cos k. With x=eta²<=1/64 and y=x zeta<1/128, the enabled derivative coefficients after factoring x are bounded by `4/(1-3x)²` for v_0' and `4/(1-3x)²+16x/(1-3x)³` for v_0''. These are below 5 and 6 on the domain. The analogous disabled coefficients, after factoring eta²zeta², are `4/(1-3y)²` and `4/(1-3y)²+16y/(1-3y)³`, also below 5 and 6. The value bounds follow from 6x/(1-3x)<7x and 2zeta/(1-3y)<3zeta. Thus (2) is valid, including the extra disabled powers of zeta.

These imply both the delta-scaled bounds and the absolute bounds |v|<=2, |v'|<=1, |v''|<=1. In particular the largest value ceiling from the separate program bounds is below 3/2, so the absolute value bound is conservative.

Multiplying the Robin denominator by z gives W=1-z+vz, hence q=1-v(1+z)/W exactly. Its modulus equals that of the source denominator and is at least sin k>1/2. Differentiation of W=1+z(v-1) gives |W'|<=|v-1|+|v'|<=4 and |W''|<=|v-1|+2|v'|+|v''|<=6. For N=1+z, |N|<=2 and |N'|=|N''|=1. Quotient differentiation therefore gives the claimed F bounds 4, 34 and 594<600. The factors 2 in the second derivative terms are present.

Then q'=-v'F-vF' is bounded by (20+238)delta<260delta. The second derivative -v''F-2v'F'-vF'' is bounded by (24+340+4200)delta<4600delta. Antisymmetric Q entries are constant; controlled program sums use a maximum. Thus Q is unitary and its first two derivative bounds hold as operator norms, including passive references. The sharper ||Q-C|| bound is exactly the source scattering discrepancy after multiplication by exp(-ik).

The H0,H1,H2 bounds follow directly from differentiating Qg: the mixed term in the second derivative has coefficient 2*260. No derivative of the large translation phase is hidden in these constants; that factor is retained in the oscillatory exponent.

For R, write f=b/(D-E). Uniformly f<=eta/(1-3eta²)<2eta and |f'|<=2eta³/(1-3eta²)²<3eta³. Since s=zq, |s'|<=1+260delta and |1+s|<=2. Thus |R'|<=sqrt(2)[6eta³+2eta(1+260delta)]. Using sqrt(2)<3/2 gives this divided by eta at most 9eta²+3+780delta<4+780delta. As delta<33/64, this is below 420. The value bound 2sqrt(2)eta/(1-3eta²)<3eta is also valid. The J0,J1 product-rule bounds consequently hold. R is a map to the mediator/program/reference coordinate, so no extra path multiplicity is needed.

## 2. Strong evolution and normalization

The lead maps are restrictions of full-integer Fourier transforms with the source's 1/sqrt(2pi) convention. They are bounded contractions on spectral L2. Multiplication by Q is bounded and pointwise unitary. The finite mediator integral is bounded because g is compactly supported and R is uniformly bounded. Thus Psi(t) lies in the complete one-head Hilbert space, including mediator output.

Multiplication by E is bounded, so the lead integrals are strongly differentiable in t in ell². Dominated differentiation gives the mediator derivative. The bounded Hamiltonian can be applied to the integrals; the bulk recurrence and exact boundary/mediator equations give iPsi'=hPsi at every coordinate. Equality is in Hilbert space, so uniqueness for a bounded self-adjoint generator gives Psi(t)=exp[-i(t-s)h]Psi(s), with constant norm. No generalized-column orthogonality is used in this step.

For t=-tau, the full-integer incoming vector has norm one by Parseval and ||g||_2=1. Its missing negative-coordinate tail has phase derivative gap ell+1+tau vmin. The outgoing half-line has the same gap, and the mediator has gap ell+tau vmin. Single integration by parts gives exactly (8) for the half-line and (9) for the mediator. The half-line bounds tend to zero as tau^-1/2 and the mediator bound as tau^-1 for fixed parameters and ell; tau divided by each gap stays bounded. This works also for ell=0 because tau>0.

Embedding the full-integer incoming vector and Psi(-tau) into a common space makes their difference consist of that incoming missing tail, outgoing vector and mediator coordinate. Its norm tends to zero. Hence ||Psi(-tau)|| tends to one. The exact constant norm then equals one at every finite time. The construction is linear in xi; the same proof for every unit xi and homogeneity preserve all input norms, and polarization preserves inner products. Thus it is an isometry on the full legal input space, not just normalized on basis columns. Passive-reference tensors are included throughout.

This proof constructs a normalized incoming continuum packet family and does not show that it spans the entire physical space. The bound states established in the scattering check are not erased. In particular no claim about a generic seed's bound-state weight follows from the normalization argument.

## 3. Early and late full-output estimates

At early nonnegative t, the negative-coordinate incoming tail and nonnegative-coordinate outgoing difference both have gap ell+1-tvmax. The mediator gap is ell-tvmax. The stronger hypothesis ell-tvmax>0 is explicitly required. These discrepancies occupy disjoint coordinate sectors in the common comparison space, so their squared norm bounds add. This proves the square-root expression in (11) without assuming xi and Qxi are orthogonal. The incoming terms on n>=0 cancel exactly.

At late t with A_late=tvmin-ell>0, both the unwanted incoming term and mediator integral have the stated derivative gap. The outgoing difference from B tensor Cxi is Fourier synthesis of (Q-C)gxi; contraction bounds it by d_S because g has L2 norm one. The sufficient sum defining d_packet bounds the entire physical difference. Since Psi(t) is normalized, q_B>=1-d_packet; if d_packet<1, the common outgoing target can be positively normalized at cost at most another d_packet.

For the excluded coordinates n=ell+1+m, the ideal outgoing phase derivative is at least 2ell+2-tvmax+m. Therefore the unnormalized discarded tail is bounded by N_out. Dividing by the lower bound for q_B gives the normalized tail allowance. If this is below one, the finite projection has positive norm and costs at most twice that allowance. This proves (12), with all source/mediator locations excluded from the target but retained in the error. Normalization is independent of logical input because B is scalar and C is unitary. The translation, scattering and physical scalar phases remain those of the construction.

## 4. Outer-contact residual

The fixed-diagonal perturbation acts on radial sites ell,ell+1,ell+2 in each port and annihilates the mediator coordinate. Its three-site matrix has off-diagonal entries j-gamma and j, hence norm sqrt((j-gamma)²+j²). Port copies and program/reference identities do not multiply that norm.

At those sites the incoming derivative is negative with magnitude at least tvmin-1, and the outgoing derivative is positive with magnitude at least 2ell-tvmax. These lower bounds are conservative for the specified sites. The window assumptions give the positive margins required for two integrations by parts. Differentiating `((a/phi')'/phi')'` gives a''/(phi')², -3a'phi''/(phi')³, -a phi'''/(phi')³ and +3a(phi'')²/(phi')⁴. Bounding the two dispersion derivatives by 2j yields H_A exactly.

The incoming amplitude uses G0,G1,G2 while the outgoing amplitude must use H0,H1,H2. The latter correctly charges all Q derivatives. Applying t/qi<=2/vmin and t/qo<=tf/qo(tf) gives A_i and A_o. Integrating the positive inverse-square envelopes gives the two bracket differences in (14) with their stated signs and velocity denominators. Three radial sites give sqrt(3), each already containing all internal components. No mediator term is missing because Delta has no mediator column.

Ordered Duhamel uses the exact normalized Psi(t) on the residual side and a unitary propagator for h+Delta on the other side. Its norm is bounded by E_outer, with cap two for the two normalized endpoints. This is an auxiliary infinite-space comparison. It does not assert that Psi(t0) belongs to the finite summand or that an actual emitter seed has been prepared as this packet.

## Scope and work record

The new bridge supplies exact normalized microscopic packets and quantitative complete-output estimates for them. A finite-seed theorem still needs the early literal-seed comparison, exact finite/exterior Hamiltonian identification, combined target errors and simultaneous parameter/resource choices. A full-vector match would charge omitted bound-state components; they cannot instead be declared absent. No such integration or runtime promotion is made here.

Only this report was written. No scientific executable, numerical integration, symbolic solver, sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. The calculations were checked analytically; hashing and directory creation were bookkeeping. No retained or formal audit status is assigned.
