# Distinct check of independent scalar coefficient errors

Conditional support, with no required mathematical correction found, for `common_product_coefficient_tolerance/PROPOSAL.md`, SHA256 `8934d4f00c5dea01fe26c24a10f67a8b143e180269e1d7e66e11770a5df18260`. The complete source was read. The new residual, independent coefficient box, phase separation, load convention and sensitivity example were reconstructed analytically. The result is a sufficient finite-time full-output theorem for one supplied cell, not network robustness or a necessary accuracy law.

## Exact Hamiltonian and independent perturbations

Expansion of Q_(b_L)(u,m)+Q_(b_R)(m,v) gives b_L n_u+(b_L+b_R)n_m+b_R n_v and hopping coefficients -b_L,-b_R. The two compensation terms give the scalar c_u+c_v and subtract c_u n_u+c_v n_v. On either legal program this proves every coefficient in equation (3), including the actual vacuum scalar C_tilde. No single-head reduction is used; the expansion is a full qubit operator identity, so it retains double occupation.

All eight scalar deviations in equation (2) can be independent. Centering removes only C_tilde, not endpoint error potentials. The triangle bounds are |delta b_L-delta c_u+(1-p)delta a_u|<=2epsilon b+(1-p)epsilon a and its right-end counterpart. Similarly |delta b_L+delta b_R+delta d_p|<=epsilon D_p. These inequalities allow simultaneous adverse signs; no calibration correlation is used. The lower endpoints of all eight intervals remain positive for epsilon<1 because D_p-2b>0. Program and head-number conservation remain exact because only scalar coefficients change.

## Full four-state dressed action

In each nominal program, the parent isometry maps vacuum and antisymmetric one-head input to mediator-vacant vectors. Its symmetric one-head image is alpha_p S+beta_p M, where n_m M=M and n_m S=0. Its double-endpoint image is alpha_p|101>+beta_p B with B=(|110>+|011>)/sqrt(2), where n_m B=B. Thus n_m Jd_p has two nonzero images beta_p M and beta_p B. They are normalized and orthogonal because they lie in different total-number sectors. Its two nonzero singular values are exactly beta_p, proving ||n_m Jd_p||=beta_p on the entire four-state domain.

For enabled p, D0 beta0=sqrt(2)b/sqrt(1+r0^2)<sqrt(2)b. For disabled p, D1 beta1=sqrt(2)b[D1/(D1+epsilon_off)]/sqrt(1+r1^2)<sqrt(2)b. These inequalities do not require D1 to be comparable to D0. On the combined legal program space the mediator perturbation is block diagonal. Its norm is the maximum of |e_m,p| beta_p, not a sum and not D1 times beta0. It is therefore bounded by sqrt(2)epsilon b. Arbitrary coherent program and passive-reference inputs are covered by this operator statement.

Each endpoint occupation has norm one on the full physical space, so the two endpoint terms acting on Jd cost at most 4epsilon b+2epsilon a. Each X_h has one-head eigenvalues +1,-1 and vanishes on pair vacuum and double occupation; its full norm is one. The two hopping errors cost at most 2epsilon b. Adding these estimates proves B_act=(6+sqrt(2))b+2a. The improvement from a full detuning-size operator norm comes from the exact nominal mediator overlap, not from differentiating an eigenvalue or assuming actual perturbed eigenvectors.

## Residual, phase and complete output

The nominal centered intertwiner is H_c Jd=Jd(A_c-P1 epsilon_off Rplus). Subtracting the actual centered Hamiltonian gives the displayed rectangular residual exactly. Its norm is bounded by epsilon B_act+epsilon_off; Rplus has norm one on the full four-state code, including double occupation. Duhamel for that rectangular defect, with two replacements of Jd by J, proves equation (10) for both signs of time. Actual invariance of the dressed space, a perturbed spectral gap and commutation of the perturbation with the nominal generator are unnecessary.

All physical head/program outputs remain in the norm comparison. The cap 2 is valid for two isometries. The code distance kappa_code, rather than the sharper isolated propagation leakage, is the correct endpoint-replacement cost. An all-enabled input removes the nominal disabled residual because that program sector is invariant; no such omission is used for the full legal program domain.

The two proposed targets are distinct vector comparisons. The exact scalar discrepancy between them is 2|sin[t(C_tilde-2b)/2]|, bounded by 2epsilon b|t|. Adding it to (10) proves B_fix=(8+sqrt(2))b+2a in (11). A common scalar is irrelevant for the isolated channel but remains in the specified vector target. The actual-phase estimate has the smaller proved upper envelope; this does not require an ordering of the exact errors to two different targets for each tuple. Relative endpoint or program-dependent shifts are not removable by this scalar accounting.

## Nonzero box and physical load

With mu=eta-2kappa_code-T epsilon_off>0, B_fix>0 and T>0, epsilon_* is positive and at most 1/2. Since epsilon_*<=mu/(2T B_fix), every allowed tuple with epsilon<=epsilon_* satisfies

    2kappa_code+T(epsilon_off+epsilon B_fix)
       <=eta-mu/2<eta.

This includes epsilon=0 without a false strict zero comparison. The certificate requires slack of the displayed nominal upper bound, not merely an unproved claim that the actual nominal error is small. Absence of slack is correctly described as failure of this certificate, not impossibility.

For the combined mediator/program operator, the two positive projector directions are orthogonal, so its norm is max(d0,d1), even if the perturbed ordering reverses. Each is bounded by (1+epsilon)(D1-2b), which proves the stated norm bound. Every other installed block norm grows by at most the same factor. Thus actual incident sums are bounded by (1+epsilon) times the nominal sums. The nominal maximum is D1+2b: endpoint load is 3b+a<4b<D1+2b, and the program loads are a and D1-2b. The condition D1+2b<=2Lambda/3 and epsilon<=1/2 therefore gives actual loads<=Lambda. If the two mediator projectors are counted as separate blocks, their norm contributions add and this maximum cannot be reused; the proposal explicitly preserves that distinction. Eight independent scalar coefficients are consistent with seven combined listed blocks and six physical qubits.

## Gate-time arithmetic and sensitivity

Substitution of T_gate=pi D0/(2b^2) gives exactly

    epsilon T_gate B_fix
      =pi epsilon[(8+sqrt(2))D0/(2b)+2].

Replacing 8 by 6 gives the actual-phase envelope. The nominal certificate is strictly below 2sqrt(2)b/D0+pi D0/D1 by the positive finite mixing and epsilon_off inequalities. The stated sufficient order eta b/D0 requires positive nominal slack of the stated size; when b/D0 is itself proportional to eta it gives the advertised sufficient eta-squared order. This is not a necessary microscopic tolerance theorem. The constants in the explicit box, rather than that order notation, define the actual certificate.

For the proposed sensitivity tuple, only c_u and c_v increase by epsilon b. The antisymmetric one-head state has equal endpoint potentials and zero hopping amplitude into the mediator: the two -b contributions cancel exactly. Its actual centered eigenvalue is a(1-p)-epsilon b, while its target centered eigenvalue is a(1-p). Their evolution difference on that vector is exactly 2|sin(epsilon b t/2)|. Vacuum has no centered shift. Consequently a vacuum/antisymmetric superposition carries a relative phase error that cannot in general be removed by one common rephasing. At special phase-return times the error can vanish; no every-time failure assertion is made. A phase on the antisymmetric vector alone would not establish channel error, and the proposal's vacuum-coherence qualification correctly avoids that confusion.

## Sources, exposure and limits

The unchanged exact parent is `mediated_common_product_program/PROPOSAL.md`, SHA256 `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`, with my earlier full check `809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6`. Its full four-state matrices, dressed intertwiners, phase and block conventions are reused at their checked scope. The separate sector result is not used to prove any full-domain norm here.

ROOT requested the independent-block interface and highlighted endpoint cancellation sensitivity. The present source author authored the base cell and related attachment work. I checked those sources, authored their publication syntheses, and have substantial shared positive-block ancestry. I did not author this tolerance proof. ROOT's provisional favorable assessment was exposed before this check but was not used as a mathematical premise. This is a distinct reconstruction of the new perturbation bridge, not fresh independent certification of my own parent review.

The theorem retains exact block shapes, frames, program directions, omitted interactions and joint literal preparation. It proves neither tolerance to those other errors nor native coefficient supply, network attachment robustness, a processor transfer, capture/reset or permanent finite halt. No numerical tolerance or operating point has been selected.

Only this review was written. No scientific program, symbolic solver, numerical dynamics, parameter sweep, source/canonical/W/Git/checkpoint/prompt/model change or delegation occurred. Source hashing was identity bookkeeping. No retained audit or publication status is assigned.
