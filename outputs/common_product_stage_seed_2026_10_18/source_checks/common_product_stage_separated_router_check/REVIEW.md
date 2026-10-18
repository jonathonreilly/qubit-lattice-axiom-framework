# Four-port positive core: distinct bounded check

No required mathematical correction was found. The literal four-cell layout, legal twelve-bit encoding, shared-endpoint scalar and potential accounting, exact reciprocal scattering matrix, central-band error, mediator norm and packet-normalization extension are valid. The min-max argument proves at least four above-band eigenvalues counting multiplicity. This remains an infinite-ray core and normalized packet result, not a finite-seed, record, halt or resource-performance theorem.

## Pins and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, read completely and SHA-256 verified: `common_product_stage_separated_router/PROPOSAL.md`, `60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182`.
* Previously fully read cell source, hash refreshed unchanged: `mediated_common_product_program/PROPOSAL.md`, `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.
* Previously fully read packet source, hash refreshed unchanged: `common_product_microscopic_packet/PROPOSAL.md`, `c105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e`.

The previous two-port results and my packet check `c27e7a93c6d76e8261d5a081c3af6ad94438aa803a69354dfb7d2e762e6e0234` are reused for their exact definitions and normalization mechanism, not as prior checking of this new architecture. ROOT suggested the architecture and Schur algebra and had a favorable full reading; that is exposure, not mathematical evidence. I read the candidate before reconstructing the steps below. This is distinct source-exposed same-model checking with inherited effort, not blind/model-diverse replication or retained audit. Existing workflow snapshots are reused.

## Literal geometry, programs and positive support

The four endpoint coordinates are the corners of a side-two square. Straight cells occupy the horizontal south and north sides, and cross cells the vertical west and east sides. Each midpoint mediator has unit lattice distance from its two endpoints. Putting all three controls of a straight cell one unit in +z and those of a cross cell one unit in -z makes every program/head pair nearest-neighbor. At a shared endpoint the two controls are different physical sites. At distinct mediators the controls are also distinct. This gives twelve control qubits without collisions; each cell is an actual rigidly oriented copy of the given six-site support pattern.

The four stated outward rays are mutually disjoint. None passes through a mediator, another endpoint, or a control site. Each endpoint uses two mediator neighbors, two separate control neighbors and one ray neighbor, hence five of the six cubic neighbors. Other geometrical adjacencies are harmless only because their interactions are explicitly absent as a supplied condition.

Each endpoint occurs in one straight and one cross cell. The two legal twelve-bit strings therefore enable exactly one of its cells. Complementing all local legal assignments exchanges the matchings. Distinct strings are orthogonal and every program occupation commutes with the Hamiltonian, so coherent legal input is preserved as encoded. No equality of distinct physical program qubits is assumed as an operator identity; their correlated preparation is an input premise.

Every individual cell term is positive on its full qubit support, including the double-occupation part of Q_b. Summing overlapping positive terms preserves positivity; commutativity or disjointness is unnecessary. There are four distinct endpoints and four mediators, hence eight heads, plus twelve controls: twenty core qubits. No dressed input or three-body controlled hopping has been substituted for these literal terms.

## Shared endpoint and common scalar

At any endpoint, two Q_b diagonals contribute 2b n_v and the two positive compensations contribute 2b-2b n_v. Their sum is 2bI at that site. Summing all eight compensations gives 8bI globally, independently of head location and legal program. At each mediator the two Q_b diagonals and its programmed onsite correction give exactly D_e n_m. The single enabled local endpoint projector contributes a=2j at every endpoint. Thus, after subtracting only 8bI, A=K_lead+2jP_endpoints and B_e=-b(|u_e>+|v_e>) exactly. The inactive cell's raw diagonal cannot be separately discarded; its compensation cancellation is already included here.

These identities also hold when the one head is in a lead: every cell then has its head vacuum compensation energy 2b. There is no location-dependent scalar convention or imported two-port phase 2b. The physical phase for this core is exp(-i8bt).

## Schur complement and all four scattering channels

Within each matching, its two disjoint endpoint-sum projectors add to I plus its matching permutation. Elimination of the four scalar mediators gives `2I-alpha(I+R_p)-beta(I+S_p)` as V, with alpha=b²/[j(D0-E)]=D0/(D0-E) and beta=D0/(D1-E). The endpoint lead diagonal contributes the additional jI in the boundary equation. The ideal active matching is V_ideal=I-R_p.

In port order I0,I1,O0,O1, the two matching matrices are the stated off-diagonal blocks I and X. They are real symmetric involutions and commute; their product is diag(X,X). The group they generate acts regularly on the four ports, giving one joint eigenvector for each (r,s) in {±1}². Thus no incoming channel or repeated eigenvalue multiplicity has been omitted.

Substitution of z^-n f+z^n S f into the matrix boundary equation gives equation (4) with denominator `z^-1 I-I+V`. Its imaginary part is -sin(k)I. In the joint basis, each scalar amplitude is `(1-v-z)/(z^-1-1+v)`, with v=2-alpha(1+r)-beta(1+s). For real v its numerator and denominator have equal modulus, proving unitarity. The matrix is diagonalized by a real orthogonal basis, hence it is symmetric and reciprocal. Ideal v=1-r is 0 or 2 and gives z or -z, respectively, so the entire comparator is zR_p. This includes incidence from both I and O rays; it does not create a one-way element.

The cell condition D0>2b implies D0>4j already, and the central-band domain makes the margin stronger. On that band the eigenvalue displacement is bounded by 2(alpha-1)+2beta. Direct fractional subtraction gives `2sin(k)|v-w|/(|z^-1-1+v||z^-1-1+w|)`. For ideal w=0 or 2 the second denominator is at least one; the first is at least sin k. Thus the scalar Lipschitz ceiling is 2|v-w|. Since actual and ideal share the joint basis, applying this channelwise requires no general operator-Lipschitz theorem.

This proves the full matrix error <=4(alpha-1)+4beta, and the central E<=3j margins give <=13eta²+5zeta. Both corrections are simultaneously present in the r=s=+1 channel, so the earlier two-port maximum would not be justified. The common z phase, undesired I reflection and wrong O channel all remain in the matrix comparison. Program direct sums and passive references introduce no dimension factor.

## Four mediator coordinates and normalized packets

The mediator equation gives each amplitude in (8), with the same endpoint sum, positive b/(D_e-E), and incoming 1/sqrt(2pi) convention. Let N be the endpoint-edge incidence matrix with columns e_u+e_v. Then NN*=2I+R_p+S_p has eigenvalues 4,2,2,0 in the joint basis, so ||N||=2. The coefficient map before the Fourier factor is `b(D-E)^-1 N^T(I+S_phys)`, whose norm is at most 4b/(D0-E). With eta<=1/8 and E<=3j, this is at most 4eta/(1-3eta²)<5eta. It bounds the whole mediator vector; no extra factor counting four mediators is needed. The source correctly does not convert this generalized amplitude into a smaller finite-time physical output error.

For fixed compact-band C2 data, matrix inversion and the nonzero band denominator make S and the mediator coefficient maps smooth with finite derivatives. Lead synthesis is bounded by full-integer Fourier analysis, and the finite mediator integral is bounded. Multiplication by bounded E permits strong time differentiation. The exact bulk, boundary and mediator equations therefore imply strong evolution and constant norm for the integrated packet.

In the remote past, each incoming half-line approaches its full-integer norm-one incoming vector, while the outgoing components vanish by nonstationary phase. Each of the four mediator components also vanishes by integration by parts; finite dimension and bounded coefficient derivatives suffice. Consequently the constant norm is one. The construction is linear for all four-port/program/reference inputs, so homogeneity and polarization establish an isometry. This is a valid dimensional extension of the previous mechanism, not a numerical reuse of its Q/R derivative constants. It asserts neither global completeness nor absence of omitted bound-state sectors.

## High bound states

A has endpoint diagonal 3j with one radial hopping -j, and all internal lead rows have diagonal 2j with two hoppings -j. Its absolute row and column sums are at most 4j; it is positive from its displayed terms. The full operator differs from four free half-lines plus a finite mediator block by finite-rank terms, hence has essential spectrum [0,4j].

On the four-dimensional pure-mediator trial subspace, every unit vector has Rayleigh quotient at least D0>4j. By the upper-edge variational/min-max principle, the spectral subspace above 4j must have dimension at least four; otherwise that trial space would intersect its orthogonal complement in a nonzero vector with quotient at most 4j. Above essential spectrum these are discrete eigenvalues counting multiplicity. This proves the stated lower count. It does not prove exactly four, classify lower eigenvalues, compute weights, or make any finite seed orthogonal to them.

## Counts, full-space loads and boundaries

Four seven-block cells give 28 listed positive blocks. Listing the repeated endpoint compensation blocks separately is consistent, and combining them changes bookkeeping but not their summed incident norm. Adding N new sites and N uniform bonds per ray gives the displayed 20+4N qubit and 28+4N block inventories before emitter or record modifications.

A shared endpoint meets two full cell incident sums 3b+a and one lead bond of norm 2j. Its safe load is 6b+2a+2j=6b+6j, even though only one endpoint program projector is enabled on a particular legal state. The cap uses full-support norms, so counting only that enabled projector would be wrong. Mediator, program and ray loads follow as stated from the distinct source terms. A degenerate finite ray with N=0 would simply lack its added lead bond, leaving the displayed endpoint figure a conservative ceiling.

With D1=Lambda/2, D0=zeta D1, b=eta D0, mediator load is Lambda(1/2+eta zeta)<Lambda. Endpoint load is 3Lambda zeta(eta+eta²), whose allowed-domain ceiling is below 27Lambda/128<Lambda. The other loads are smaller. This proves a core load-cap choice, not a finite source/record load or duration theorem.

The distinct physical O rays do allow a different placement question for a later writer, but no writer is installed or checked here. Quantitative four-port derivatives, finite emitters/caps, seed matching, bound-state-related mismatch, uniform finite output and any record recovery remain open interfaces. Previous two-port resource and phase statements do not transfer automatically.

Only this report was written. No scientific executable, numerical derivative calculation, simulation, sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. Checks were analytical; hashing and directory creation were bookkeeping. No retained or formal audit status is assigned.
