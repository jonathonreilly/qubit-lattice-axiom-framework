# Uniform finite-clock realization of the exact loader

ROOT integration derivation, pending distinct check. This alternative uses the exact matched loader and a weak endpoint emitter with uniform ordinary propagation. It does not require the position-dependent engineered square-root clock profile of PR9737. Equal arm/rail coefficients, the fixed sqrt2 ratios, supplied endpoint coherence, blank apparatus and freely degenerate data/passive references remain premises. No active-system, preparation, permanent halt or generic precision claim follows.

## Pinned premises

Paths below are relative to /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

1. exact_two_body_gate_matched_extension/PROPOSAL.md a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e, distinct review36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f. This is the corrected single-mu convention, not the historical ambiguous draft.
2. exact_two_body_direct_loader_composition/PROPOSAL.md f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946, review41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6. It supplies the exact ordered physical gauge, finite selected-source installation, actual record projection and resource counts.
3. exact_uniform_chain_finite_launch/PROPOSAL.md bda916e331d0bf3863feac8e0b7dce279df6f2eaa94f0dd17daf651cad51545a, review0ef35c231f3550f196bd1f8df8b5b3773ebfa6314232931ea9470ca1f00a5bac. It supplies the literal normalized weak-source scalar theorem, constants, cut, complete output profile and sufficient length prescription. Its scalar positive-block geometry is not imported as physical loader geometry.

All three pairs have been fully read and accepted by ROOT at their stated scopes. The new obligation here is the explicit physical-to-scalar transfer on the actual selected input subspace, including unequal unused left boundaries, phase, cap and counts. The earlier approximate scattering/runtime results and engineered-clock finite bound are not premises.

## Actual finite installation

Choose J=Lambda/40, mu=(sqrt2-1)J. Retain the exact26-layer matched network, with74 virtual positions x=0,...,73, four rails and shared ordinary Q,P,R. Its internal inventory is296 heads,3 data qubits,468 positive blocks. Its arm rotations A and ordered gauge W transform the full infinite one-head operator into a scalar uniform clock with diagonal2J+mu and hopping-J, tensored with the rail/data fiber. W is identity on the left extensions and -U_f on the right, U_f=I_a X_R C_P^(b) SWAP_QP.

At each of eight origins attach ell ordinary heads and ell Q_J bonds. For the two left a=1 rails, attach one extra source s at distance ell+1 by the combined positive source block

 B=Q_gamma(s,v_ell)+(2J-gamma)n_s+(J-gamma)n_(v_ell),
 gamma=rho J, 0<rho<=1/2.

The other six rays end at v_ell with positive cap J n_(v_ell). Add mu n_v at EVERY exterior head, including the two sources, but not again on the internal diamond/mixer heads. The eight internal permutation potentials are already included in the468-block inventory. All source, cap and ordinary one-head diagonals are2J+mu; B has full norm3J before the separate mu terms. The old cell mediator/penalty construction is absent.

The supplied input E has a single head coherently encoded in the two a=1 source endpoints, with arbitrary b,Q,P/passive-reference input and blank R. The a=0 left rays are capped and remain physical apparatus, not deleted coordinates.

## Selected-sector scalar identity

Apply the exact finite A,W from the global source to this installation, including all boundaries. In the transformed space the internal links and diagonals are scalar on the four-rail/data fiber. On left exterior coordinates W=I, so the a-dependent terminations remain diagonal in a. On right exterior coordinates W=-U_f is constant, and the identical caps/bonds on all four right rays commute through that same gauge. There is no inter-rail term remaining after the transformation.

Thus the transformed finite Hamiltonian is a direct sum of scalar clocks indexed by a,b. The two a=1 clocks have identical weak source and right cap. The a=0 clocks have different left caps but are not populated by the transformed supplied input. The a=1 virtual subspace is invariant under this transformed Hamiltonian, even though its physical image under AW has mixed internal rail/data prefixes. It is this invariant image, not the subspace of physically a=1 internal heads, on which the comparison is made.

For each selected b clock set n=x+ell, so the first ordinary left head at x=-ell is n=0. Its source at x=-ell-1 is s. The ordinary finite interval ends at x=73+ell, hence

 K=74, N=2ell+73,
 F={ell+74,...,2ell+73}.

These are exactly the scalar theorem's coordinates, with its literal H_fin including mu I. The right external output x=74,...,73+ell is precisely F. On those heads A is identity and W=-U_f. At the source AW is identity. Consequently the selected-space identity required by scalar theorem(30) is exact, with the actual input and complete external output maps fixed, including the minus sign. No equality of the two unused left clocks is asserted or needed.

## Explicit policy and complete theorem

Use the scalar theorem's constants P_star,Q_star,D_star from its equation(10), unchanged, and set for0<epsilon<=1

 h=10^-3, rho=epsilon sqrt(h)/1024,
 ell=ceil max{
 1000, 7500,
 192rho Q_star/(h^2 epsilon),
 [128rho D_star/(h^2 epsilon)]^(2/3),
 [32768rho Q_star/(h^2 epsilon^2)]^(2/3),
 (10/rho^2) log[512sqrt(h)/(rho epsilon)] },
 t_minus=3ell/(4J), t_plus=7ell/(8J).

The7500 term is exactly100(K+1), not a new constant. All cutoff normalization, finite-source residual, incoming component, interior coordinates and far-cap errors are those of the accepted scalar proof. No new estimate on them is substituted.

Let z(t) be that theorem's positively normalized finite F restriction of its full outgoing Fourier profile. Its integrand includes exp[-iJt*2(1-cos k)] and the actual normalized source F(k) with its exp(ik) factor. Define the complete physical target by placing -exp(-i mu t)z(t) on the right external a=1 rails with the encoded operation U_f on the input fiber. Retain all Q,P,R and passive-reference outputs; all other heads are vacant in the target. There is only ONE extra mu phase. The2J phase is already inside the scalar profile, and no arbitrary phase matching is performed.

The scalar error is the same on both selected b channels, so their orthogonal sum has the same operator norm, not a sqrt2 multiplier. Applying the exact physical unitary AW preserves that norm. Therefore

 sup_(t_minus<=t<=t_plus) ||exp(-itH)E-V(t)||
                        <13epsilon/256<epsilon/16.

The unhalved stabilized complete-output channel distance is below13epsilon/128, in particular belowepsilon/4. The probability of the external right output AND R1 exceeds1-(13epsilon/256)^2, because the target lies wholly in that event and projection of the full vector error onto its complement contracts norm. The looser1-epsilon^2/64 bound is also valid. This is not postselection of the actual state.

Independently, the exact current R1 branch from the global gauge remains valid for this same scalar finite dynamics, whenever its probability is nonzero. It includes virtual72 in the antisymmetric final arms and x>=73, whereas external output begins at74. The record branch's exact logical factorization is not a claim that the internal head is vacant there. The finite evolution can return and undo the operation; only the stated window has the high-success guarantee.

## Physical counts, load and scope

The eight ordinary extensions add8ell heads; the two sources add2. Total heads=298+8ell and qubits=301+8ell. Exterior blocks comprise8ell ordinary Q bonds,2 combined source blocks,6 caps, and8ell+2 separate mu occupations. Adding the468 internal blocks gives478+16ell positive blocks. The combined-source counting convention is retained; splitting B into its three summands changes block counts and perturbation bookkeeping but not the operator.

The full support loads of the internal network are at most40J on Q/P,16J on R, and below5J on internal heads. At an exterior source the load is3J+mu, at its ordinary neighbor5J+mu, at an ordinary exterior site4J+mu, and at a cap3J+mu. These are all below40J=Lambda. The source neighbor has the combined B plus its preceding ordinary Q bond and one mu occupation; no source bond is counted twice. These are full physical support norms, not scalar probabilities.

Reuse the exact range18 embedding of the299 internal qubits in the7^3 cube, with eight distinct vertical rays. Ordinary ray bonds, source attachment and caps add only range1 or onsite terms; the two longer source rays do not intersect any other ray. Data degree20 and supplied selective interactions remain. This is not cubic nearest-neighbor hardware.

For fixed K74 and epsilon tending to zero, the accepted explicit scalar prescription has ell=Theta(epsilon^-2 log(1/epsilon)). Counts and physical times therefore have sufficient-recipe ordersTheta(epsilon^-2 log(1/epsilon)) andTheta(Lambda^-1 epsilon^-2 log(1/epsilon)), respectively. Gamma=Theta(Lambda epsilon). Uniform interior coefficients and fixed matching ratios replace the engineered position-dependent profile, but exact coefficient/state supplies remain. The large fixed scalar constants remain visible in the source; these asymptotic orders are not practical times, optimal lower bounds or a manufacturing-tolerance result.

ROOT authored this transfer after reading the full global finite installation and scalar proof/check. This is new source-exposed integration requiring a distinct check of the selected-sector identity, boundary coordinates, phase, count and cap. No scientific executable, numerical approximation, model override, Git change, retained audit or editable prompt change is claimed.
