# Distinct check: conditional entrance-SWAP interface

Disposition: **supported at the stated enlarged-block, supplied-one-head-input scope; no required mathematical correction found.** The exact conjugacy transfers the existing finite operating and absolute-branch bounds without an added error or time cost. It does not construct a nearest-neighbor two-body SWAP bond, endpoint head injection, or the separately isolated complete-loader channel. Those remain explicit premises/obligations rather than consequences of this check.

Reviewed complete source: `common_product_autonomous_loader_interface/PROPOSAL.md`, SHA256 `c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e`.

All paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

## 1. Full-support positive block

For an arbitrary vector pair `(x,y)` on the Q/P fiber the one-head quadratic form is `a||x-W* y||^2`. Unitarity of W gives eigenvalues 0 and 2a, each with the full fiber multiplicity. The head-vacuum block is zero and the double-head block is 2aI because both hopping terms annihilate |11>. Thus the entire four-qubit operator is positive with norm exactly 2a. This is not a compressed norm. It conserves head number and permits program transfer. The sign/orientation of W is consistent with the declared head ordering; here W=W* so reversing the physical entrance orientation cannot introduce a different gate.

These conclusions depend on supplying this four-qubit operator. Its factorization as a positive matrix is not a decomposition into the old one-/two-qubit inventory. The source makes that distinction correctly.

## 2. Exact partition identity, including large program terms

On the finite one-head Hilbert space write `G=sum_x |x><x| tensor U_x`, where U_x=I on the two input prefixes n=1,...,M and U_x=W elsewhere. Direct multiplication sends a hopping matrix element x,y to U_x H_xy U_y*. The only edges crossing this partition are I0,1--I0,0 and I1,1--I1,0. Both get exactly the proposed SWAP hopping. Source blocks connect ell to ell+1 entirely inside the pre region; final caps and every other head edge lie within a single region.

The necessary program premise is verified from single-control76b5 equations (1)--(3): the ONLY program-dependent blocks are `f(n_P)n_m` at the four core mediator heads. Their scalar/vacancy terms and fixed endpoint occupations are program independent. On a pre head these mediator occupations vanish. On a post head conjugation changes `f(n_Q)` to `f(n_P)` exactly. A program-only potential or a program-dependent vacuum scalar would invalidate this step, but neither is in the pinned inventory. The large mediator energies are consequently included, not treated perturbatively.

Writer record contacts commute with W and stay within post. The sole record bias commutes with G globally. Head-diagonal caps, occupations and vacancies commute with G; mu N is mu I on this sector. These facts prove `H_new=G H_ref,Q G*` and its propagator identity for every real t, with the identical physical scalar. This check does not extend the conjugacy to arbitrary head occupations: full-support positivity and one-head conjugacy are separate statements.

## 3. Old-program/environment relocation and physical comparator

One can purify the arbitrary fixed sigma_PE with another passive reference. The initial head is at an emitter M in pre, so G acts as identity on the entire initial input space, including arbitrary entangled Q/path/Z input and old P/E purification. The reference generator operates on Q/path/heads/R and as identity on old P/E. Its ideal F target is entirely post, where G swaps Q and P. Therefore the final ideal tensor factors are precisely the parent's controlled program/path output in physical P and F, and the unchanged old sigma_PE relocated to Q/E. This works coherently for superposed programs; it is not a classical mixture argument. No inaccessible E operation or discarded register is required.

More formally, tensor the parent error operator with identity on old P/E and multiply it on the left by G. Its operator norm is unchanged, also after any further passive-reference extension. Mixed-state channel comparisons follow by purification/contraction. The common physical factor is exactly exp[-i(c+mu)t] when mu is installed; the parent's -i, incoming translation, q-dependent outgoing phase/Jacobian and positive normalization are untouched. No separate record phase is added.

Because G commutes with the record-1 projector, the same calculation applies to the parent's single UNNORMALIZED branch comparator on its whole certified horizon. G also preserves the head support, so the F support restriction is consistent. This neither divides by small success probability nor changes the target before matching. It transfers exactly the parent's existing branch estimate, not an all-late guarantee.

## 4. Geometry, resources and all-head energy

The detailed translated geometry in stage-record-core c913 and its single-control replacement has near-core cable segments at x=20 or 22, z=0; input rays at x=19 or 23; final rays at y=+/-8,z=1; and writers near the origin. The new Q=(21,1,1) is not among those heads or P/R. The removed old controls are not physical qubits in the single-control device. The +/-z neighbors of P were explicitly unused. Thus no inherited site is identified or duplicated.

For either entrance support the largest coordinate separation has squared Euclidean length 6 and Manhattan length 4. The support is constant-range but is not a nearest-neighbor pair; the two head endpoints themselves remain nearest neighbors. No additional installed edge follows merely from an incidental lattice adjacency.

Replacing two norm-2j blocks changes neither their head incident loads nor the listed block count. It adds 4j to old P and gives Q load 4j. The inequalities `4(D1-2b)<Lambda/2` and `j<Lambda/1024` imply the claimed new P load `<129Lambda/256` and Q load `<Lambda/256`. Other loads, including the optional head penalties and the single record bias, remain those of the parent tuple. The counts follow directly: parent `126+4ell` qubits becomes `127+4ell`; `165+4ell` blocks stays unchanged; adding the unchanged `124+4ell` head penalties yields `289+8ell`. No four-body simulation resources are covered by these counts.

The all-head lower bound does not use one-head conjugacy. After subtraction of c the only negative terms in the positive-block decomposition are the old vacancy occupation pieces, at most 2b per head. Both replacement bonds are positive on all occupations and have zero vacuum action. Hence `H_new-cI >= -2bN`, and with penalties/bias the bound is `(mu-2b)N+kappa n_R`, including arbitrary Q/P/reference fibers. Enlarging vacuum degeneracy does not prepare Q or supply an excitation. The energy argument does not establish a loader.

## 5. Scope, evidence and exposure

The narrow invariant `[H,n_P]=0` for the UNCHANGED operating device follows from its displayed blocks. Its inability by itself to overwrite an arbitrary independent program is not promoted to a universal positive-interaction obstruction. The four-plus-four terminal-neighbor count concerns direct pasting of the two displayed gadgets, not all redesigned embeddings. I do not certify any broader impossibility claim.

The new Q remains physically coupled at the entrances; returning heads can undo its relocation. Thus the direct integrated-operation theorem does not satisfy an exactly decoupled spectator interface during operation. Section 6 correctly retains this distinction. Likewise the path input is already encoded as a supplied endpoint head, whereas preparation9979 starts from head vacuum. The conditional preparation cost `2sqrt(q)+eta_inj` requires an additional complete injection interface. It is not obtained from the gauge lemma. Unknown old R in the weaker head-only comparator remains a separate issue.

Exact identities refreshed for the source premises:

- `common_product_biased_record_preparation/PROPOSAL.md`: `9979b614d77b98bf8bc63b6b87b69305beb7cf7607adf5722ae57b759728627e`.
- `common_product_energy_blank_interface/PROPOSAL.md`: `e6df21d39a9673b7e396390b64986a9e0deb74223540c975c14675a7f6fec668`.
- `common_product_single_control_router/PROPOSAL.md`: `76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01`.
- `common_product_biased_record_finite_seed/PROPOSAL.md`: `532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123`.
- `common_product_biased_record_packet/PROPOSAL.md`: `cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf`.
- `common_product_stage_record_core/PROPOSAL.md`: `c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729`.
- `mediated_common_product_program/PROPOSAL.md`: `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.

I fully read the changed source and single-control source; inspected the exact preparation, energy, geometry, finite comparator/count and packet phase/normalization premises needed above; and fully read the existing biased finite-seed distinct review. An aggregate ancestor read truncated, so affected necessary passages were read separately; no complete read of every ancestral packet calculation is claimed. The new transfer relies on the scoped checked parent operation, not on a fresh recertification of its scattering/time estimates.

I authored the original common-product cell and later attachment/sector/tolerance work and checked the related network. I did not author this entrance-SWAP proposal. ROOT supplied the review brief and exposed the proposed route. This is same-model, shared-source analytical review of the new identities and transfer, not blind replication, native validation or retained audit. The reviewer skill is applied only at this bounded scope. No scientific program, simulation, numerical sweep, new parameter choice, delegation, model change, W/Git/canonical/checkpoint/editable-prompt change or publication occurred. Only this review was created.
