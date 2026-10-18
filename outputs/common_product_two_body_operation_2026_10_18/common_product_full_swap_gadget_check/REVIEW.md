# Distinct check of twelve simultaneous square gadgets

Disposition: SUPPORT for the joint gadget core with passive data, supplied twelve-cat initialization, known scalar, full-vector bound and stated finite-range inventory. No required correction found. This is not yet a simulation of the full entrance bonds plus router background. In particular the residual direct terms of the entrance decomposition are not part of the proved propagator.

Complete reviewed source: `common_product_full_swap_gadget/PROPOSAL.md`, SHA256 `b54c6f29ea780efdcad7f33def048a0b5f9436fe8125ce3c2b2b416cabde4436`. All paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. I read the entire changed argument and reconstructed its general normalized graph expansion, cross terms, contour estimates and physical bookkeeping.

This is source-exposed same-model checking. ROOT supplied the candidate and reported a matching, unreviewed cross-path note. That report is design exposure, not evidence of correctness; I did not use the note as a premise or distinct check. I reviewed the preceding isolated gadget and authored/reviewed several router/finite/preparation ancestors. I did not author this joint derivation. The exact enumeration retained below corroborates the ordered Pauli coefficients without using the author's aggregate pair-count formula, but is not blind replication or evidence for missing physical interfaces.

## 1. Actual joint model and the correct degenerate expansion

There are twelve separate ancillary squares,48 ancillary qubits, and six shared data qubits. Each square X_all commutes with every term, even when data Pauli operators from different squares fail to commute. In the common plus sector the ancillary zero state is exactly the product of twelve cat+ states; arbitrary six-qubit data and passive references supply the low-space degeneracy. Every complementary penalty state has at least2Delta. Outside that reducing sector the additional cat-sign ground states remain. Neither uniqueness on the full ancillary space nor preparation by this penalty is established.

Let the low invariant graph have inclusion P+X, with PX=0. Projecting H(P+X)=(P+X)B yields B=xPVX and the stated graph equation. Its order-one, order-two and order-three terms give, in order,

    X1=-RVP,
    X2=RVRVP,
    X3=-RVRVRVP+R^2VP A,
    A=PVRVP.

Thus B2=-A and B4=-PVRVRVRVP+(PVR^2VP)A, with the indicated ordering. No common data eigenbasis was used. The normalized graph inclusion is (P+X)S^-1/2, S=P+X*X. It induces S^1/2 B S^-1/2. Its fourth correction relative to B4 is [S2,B2]/2, with S2=PVR^2VP. Here single-flip energy2Delta and48 involutory data factors give

    A=24nu^2/Delta I, S2=12nu^2/Delta^2 I.

The commutator is zero, while S2 A=288nu^4/Delta^3 I is retained in B4. This establishes the normalized coefficient in a genuinely degenerate, potentially noncommuting data problem. The fact that a subset of target Pauli products may commute would not by itself justify a column reduction of the elementary V, and none is needed.

## 2. Ordered fourth terms and exact enumeration evidence

A final ancillary parity pattern in the cat-product low space must be, in each square, either all zero or all four bits flipped. At four operations this leaves precisely: four distinct flips in one square; two different bits each flipped twice; or one bit flipped four times. The last class returns to P after the second operation and is killed by R. The two-bit class splits according to whether the bits belong to one or two squares. This exhausts the four-step contributions.

Within one square, the distinct-four paths give(5/2)Omega_l; the allowed repeated-pair paths give(5/2)I, in units nu^4/Delta^3. This gives30I from the latter class over twelve squares. Intermediate low returns are excluded, including when they are complementary cat configurations, as required by the operator R.

Across two squares a single excited bit in each gives energy4Delta at the middle step. The two alternating orders contribute the Pauli commutation sign chi, and the two nested orders contribute1. Their sum divided by16 is(1+chi)/8. Thus anticommuting pairs give zero, while commuting pairs give1/4. There are1056 cross-square elementary pairs. Unlike Paulis on Q give48 anticommuting pairs, P gives48, and the four distinct heads give4*9=36. Supports are distinct for all other elementary pairs, so no pair is counted twice. The total is132 anticommuting and924 commuting, producing231I.

I also built a bounded exact enumeration in this review folder. It uses the actual48 elementary data operators; enumerates the complete possible four-step final ancillary parity patterns; computes all intermediate domain-wall energies from48-bit masks; discards a path on an intermediate zero energy; and contracts data Paulis in their actual applied order with exact phases and rational denominators. It does not call a huge Hilbert-space eigensolver or use numerical fitting. The result is:

    Allowed paths:576 within one square,4224 across two squares.
    Second coefficient:-24I; second inverse moment:12I.
    Raw fourth scalar:261I; normalization correction:288I.
    Final fourth scalar:27I.
    All twelve intended Omega_l coefficients:-5/2.
    No other Pauli word survives.

The contraction therefore confirms s=-24nu^2/Delta+27nu^4/Delta^3 and g=5nu^4/(2Delta^3). The scalar is not twelve copies of the isolated scalar. The increase33 relative to -6 equals132/4, consistent with the noncommuting cross terms.

Reproducible files, all under the allowed review folder:

- `exact_paths.py`, SHA2568edbbd017adad9e2c9061e4f64eb94f9bf795bf9e042092294c33781a6942f7e.
- `exact_paths.txt`, SHA256e462e64e99d32afccf96e1f0ebf93708409c7369dd045d63fc546b0b5f67ce13.

Running `python3 exact_paths.py` uses only standard-library integer Pauli phases and Fraction arithmetic. Its final assertions test the proposed result; they are not inputs to the contraction. This is a separate exact bookkeeping check, not an independent physical realization or an audit tally.

## 3. Riesz operator, evenness and full literal-state error

The joint gap remains2Delta while ||V||<=48nu by triangle inequality, regardless of data commutation. On |z|=Delta/2 the unperturbed resolvent is bounded by2/Delta. For complex |x|<=Delta/(8v), Neumann ratio<=1/4 gives perturbed norm<=8/(3Delta). Contour integration gives ||Pi-P||<=1/3, ||H Pi||<=2Delta/3, and the analytic inverse-square-root series gives ||C||^2<=3/2. Consequently the explicitly defined analytic E has norm<=Delta throughout the disk.

For real x, the orthogonal graph projection satisfies Pi P=(P+X)S^-1 and P Pi P=S^-1. Hence W=Pi P C=(P+X)S^-1/2 and E=W*HW equals exactly the normalized graph operator used above. For complex x the source uses an analytic formula without taking x-dependent adjoints, so Cauchy bounds are legitimate. The real graph identity fixes its Taylor coefficients by analytic continuation.

The product of all48 ancillary Z operators sends V to -V, commutes with H0, preserves every plus sector and fixes P pointwise (each four-qubit cat has even parity). Thus E(-x)=E(x) as an operator. The analytic radius is at least1/(384alpha), which is at least2 for alpha<=1/768. Cauchy bounds and summation of the even tail from order six give precisely

    R6=Delta(384alpha)^6/[1-(384alpha)^2].

There is no data or reference dimension prefactor. This remains a bound on the full six-qubit data space, rather than only a prepared head sector.

At x=1 the projection difference is <=96alpha/(1-96alpha)<=1/7. The real positive inverse-square-root estimates apply without commuting columns and imply

    ||W-J||<=2deltaPi
       <=192alpha/(1-96alpha)<220alpha.

Paying both literal endpoints and applying self-adjoint effective-space Duhamel gives440alpha+|t|R6. Independently, the difference of two isometries is at most2; taking the minimum is valid. Restoring48nu and the computed scalar s gives exactly the source's phase exp[-it(48nu+s)] and propagator exp[+itg sum Omega_l]. Higher scalar corrections are paid in R6. Nothing is phase-fitted or physically projected/normalized.

The error statement is therefore a complete vector bound with all ancillary outputs retained. Supplying the exact product cat state is essential; joint preparation error can be added by unitary/channel contraction, but correct separate marginals would not establish that premise. The inequalities440alpha+T R6<=epsilon and g=j0/4 are conditions to verify together, not a promise of feasibility for arbitrary fixed strength, cap and accuracy.

## 4. Geometry, norms and prospective count

The four entrance heads and P,Q retain the coordinates from the fully read c97b source. The proposed ancillary sites occupy x=24 or25,y=4 or5,z=2,4,...,24. They are distinct within and between squares. They avoid the retained input rays at x=19,23, the final rays at y=+/-8,z=1, near-core cables at z=0, the central x=20..22 region and the writer regions near x=0. The unchanged geometry premises were fully inspected in earlier core/c97b work and are reused here, rather than inferred from a generic diagram.

Each square penalty is nearest-neighbor. A uniform conservative coordinate difference for a data/ancilla pair is(6,5,24), giving Manhattan bound35 and squared Euclidean bound637. These bounds are independent of ell and cover the actual assignments. The couplers are therefore finite-range two-body supports, explicitly NOT a nearest-neighbor construction. Allowing those edges changes the supplied interaction class; it does not solve a cubic nearest-neighbor degree constraint by rearrangement.

There are48 added ancillary qubits and96 positive blocks. Each ancilla sees two norm-Delta penalties and one norm-2nu data coupler. Each of the four heads has six such couplers, giving12nu; P and Q each have twelve, giving24nu. With Delta=Lambda/4,alpha<=1/768 the gadget-only loads are below Lambda. Existing data loads must still be added upon attachment. All are full-support norms, not state-dependent expectations.

Two residual Q_(j0/2) terms and four residual occupation terms make six additional direct positive blocks. Replacing two old conditional entrance blocks with these six plus96 changes the listed count by100 and adds48 ancillas. That arithmetic is correct, but it is prospective: neither the residual terms nor the remaining router Hamiltonian are in the propagator just checked. The old two norm-2j0 supports must be removed before computing the installed data loads; a new dynamic and cap proof remains necessary.

## 5. Evidence and scope limits

The isolated source7e6769927d3138b2812e0b4a0db62df1ef4d1d7096b10acfa2269a5ca8a98d39 and my complete checkf71cdc4e4039f923f99c8ed1f2abab9baedee9f8f9456c1d77ed6a9978b9fd58 were fully read in the immediately preceding task. Only their generic contour and literal-isometry estimates are reused with the new norm48nu; their commuting-column perturbation calculation is not substituted for the new graph proof.

The exact target sourcec97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e and review7a98f648e21cf63b70d481b2cbaba8fac86376763cec0f50678f0ed49e9bd68f were completely read in that task. Single-control76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 and corec91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729 retain prior complete scoped reads. Their interfaces are unchanged; this review does not re-audit their entire scattering or finite-runtime proofs.

The accepted result supplies the joint twelve-term passive-data component. A noncommuting background can change the graph expansion, energy denominators and low-subspace correspondence. The residual entrance terms themselves belong to that missing attachment problem. No router-runtime approximation follows simply by adding them to both sides of this isolated theorem.

Arbitrary positive Pauli couplers, complex Hermitian Y terms, finite interaction range and twelve supplied entangled cat states remain additional physical premises. None is derived from the earlier nearest-neighbor exchange/control/record inventory. No complete loader, endpoint injection, old-P/environment release, cooling, native supplier, practical simulation cost, capture/reset or permanent halt is certified.

Only this review and its expressly authorized bounded exact enumeration/output were written, all under N. No source, W, Git, canonical/checkpoint, axiom, editable prompt or model setting was changed; no delegation, numerical simulation or publication occurred.
