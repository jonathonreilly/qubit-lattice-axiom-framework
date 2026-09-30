# Independent precomparison: occupation monitoring of actual H0

Frozen before opening native-monitoring-energy-route/WORKING_PROOF.md or any candidate runner/results. Parent brief named the target and candidate hash but exposed no formula, sign, constant or proof. Prior role: I authored the preceding sharp-readout energy proof, including its diagonal constant c_read=min(mu,mu/3+2tau), and other native proof packets. This is an independent reconstruction of the new monitoring composition, not external peer review or a formal grade.

Actual input: mainfb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7 native density-onset source7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0, freshly reread literal operators and full SOS. Complete source was read in the preceding route and remains unchanged. Full qubit carrier, L>=5, mu,tau>0. Set H0=S+mu Ddiag+W as actually defined. The positive diagonal term must not disappear from the final energy inequality merely because monitoring fixes it.

## First-principles calculation

Choose the conventional dissipator D[n](rho)=n rho n-(n rho+rho n)/2 for projection n. Its adjoint is -[n,[n,O]]/2. A factor-of-two convention change rescales every monitoring budget.

For a quadratic lowering row R=sum_e a_e b_xb_y, define R_v as its terms incident to v. Then [n_v,R]=-R_v, sum_v D[n_v]^*(R)=-R (two distinct endpoints per pair), and the product rule gives

    sum_v D[n_v]^*(R^dagger R)=-2R^dagger R+sum_v R_v^dagger R_v.

Therefore, on the literal full carrier,

    M(H0):=sum_v D[n_v]^*(H0)=-2(S+W)+J,
    M(H0)+2H0=J+2mu Ddiag,

where J is the positive sum of every incident restriction of every S/W square, with its original coefficient. No independent-removal-fiber minimization is used.

## Complete incident-neighbor matrix, including W

Fix v=0 and use the eighteen ordinary pair annihilators b_0 b_y as Hilbert-space-valued components. The incident quadratic form is an18x18 numerical matrix M_pin. It separates into six axial coordinates and three four-coordinate plane blocks. For S, an axial word is alone among incident words in its singlet row, giving diagonal2mu/3. In a plane, two of the four signed words are incident at each of four neighboring centers. Their sign products are opposite, so each row restriction gives positive offdiagonal mu/4. Each plane edge appears twice. Thus its matrix is (3mu/2)I+(mu/4)A_C4, where C4 joins sign pairs differing in exactly one sign.

The centers at which a word incident to0 may occur are the six nearest neighbors of0. No two of these centers are nearest neighbors for L>=5. Hence an actual gradient row has incident terms at only one of its two centers: its cross-center pin term is zero. This fact does not rely on global bipartiteness on odd tori. Summing the six gradient appearances of each center yields axial contribution4tau I. In a plane it gives3tau I-(3tau/2)A_C4. Consequently

    M_pin = (2mu/3+4tau) I_6
            direct-sum three copies of
            [(3mu/2+3tau)I_4+(mu/4-3tau/2)A_C4].

The plane eigenvalues are2mu (constant sign-pattern vector),3mu/2+3tau (multiplicity2), and mu+6tau (alternating sign-pattern vector). The minimum over all blocks is

    lambda=min(2mu/3+4tau,2mu)=2c_read>0.

Thus J>=lambda sum_v n_v m_v as an operator: the numerical matrix inequality is valid on Hilbert-space-valued components regardless of their dependence. The full J kernel is exactly the subspace with no occupied graph edge (span of independent occupation sets); the18x18 matrix itself has no kernel. These two uses of kernel must be distinguished.

Since lambda<=2mu, the integer degree estimate

    2mu f(m)+lambda m>=lambda, m=0,...,18

proves

    M(H0)>=lambda N-2H0.                                  (PRE1)

The constant lambda with damping coefficient2 is sharp on an isolated monomer or axial dimer. It is not a claim that M(H0) is positive on all states; a nonzero traceless Hermitian adjoint output cannot be globally positive. The original diagonal attraction coefficients alone would not prove this all-state bound.

## Dynamics and budget to check

Supply d rho/dt=-i[H0-nu N,rho]+gamma(t)sum_v D[n_v](rho), fixed nu and gamma>=0 locally integrable. Finite-dimensional existence is elementary and E(t),nbar are absolutely continuous. Number is conserved. Since [H0,N]=0 the Hamiltonian part contributes zero to dE/dt. Equation(PRE1) gives, with Gamma(t)=integral_0^t gamma,

    E(t)>=exp(-2Gamma) E(0)+c_read nbar[1-exp(-2Gamma)].     (PRE2)

This is all-state, not only a low-energy-ground estimate. It need not imply monotonic heating above c_read nbar. For nbar>0, e0=E(0)/nbar and e0<=epsilon<c_read, a necessary condition for E(t)<=epsilon nbar is

    Gamma(t)<= (1/2) log[(c_read-e0)/(c_read-epsilon)].       (PRE3)

If E(t)/V<=C rho_density^2 with fixed rho_density=nbar/V and C rho_density<c_read, initial positivity alone implies Gamma(t)<=-(1/2)log(1-C rho_density/c_read)=O(rho_density). This does not derive that low-energy target, a physical time, sharp measurement trajectories, an apparatus, or permanent Records. A Lindblad unravelling is not uniquely selected by the unconditional master equation. Energy supply has the same endpoint-interaction caveat as the previous readout result.

## Adversarial checks still required

Read candidate fully after this freeze; check dissipator convention, all row signs, plane multiplicities, absence of adjacent incident centers on odd and even tori, literal full-carrier product rule, sharpness, and arbitrary-state integration including nbar0, gamma0 and large initial E. In particular test for omitted W offdiagonals, confusing matrix kernel with full-carrier kernel, losing2mu Ddiag, reversing the monitoring-budget inequality, or claiming pathwise/permanent/physical readout from the average equation. No computation has yet been run. A small independently assembled rational matrix/operator control may be useful; it must be separately priced and guarded before launch. No candidate code will be executed or imported.

Original deadline2026-09-30T22:41:00.557005Z and runtime STOP checked at16:27UTC. Writes only this new directory; no source/authority/git/PR/audit mutation.
