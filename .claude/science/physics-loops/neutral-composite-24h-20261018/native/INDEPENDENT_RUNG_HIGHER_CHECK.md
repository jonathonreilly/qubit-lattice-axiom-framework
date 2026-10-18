# Independent higher-order native rung check

Disposition: PASS for the canonical fourth-order coefficient, finite linked-cluster checks and restricted charge diagnostic. No formal audit, repository edit or new route. Root retains authorship.

For PVP=0, R=Q(E0-H0)^(-1)Q and a degenerate unperturbed band, the canonical Hermitian fourth-order Hamiltonian coefficient is

K4=PVRVRVRVP-(1/2){PVR²VP,K2}, K2=PVRVP.

This is the appropriate polar/direct-rotation gauge normalization, not the unnormalized Bloch effective Hamiltonian. Terms involving PVP vanish. The rung parity symmetry removes odd orders. The script uses the correct signs and both orderings of the anticommutator. The linked implementation y=VRVP gives y†Ry=PVRVRVRVP and rx†rx=PVR²VP, so its alternative contraction is equivalent.

Independent computation reused the separately built physical local matrices and bordered inverse R=(E0I-H0+P)^(-1)-P from the previous check, without source tensor-eigenvalue denominators. On three rungs it reproduces

sqrt(2) K4=-(3/16)I-(5/32)(tau3_1 tau3_2+tau3_2 tau3_3)-(3/16)(tau1_1 tau1_3+tau2_1 tau2_3)

to maximum entry error6.5e-15. Direct spectral-projector canonical isometry gives errors divided by lambda^6 of .19464856,.19514536,.19719692 at lambda .04,.08,.16. This independently confirms the fourth-order cancellation and local sixth-order remainder behavior; it is not an interval-certified error bound.

## Linked support

The exact local G=X0X1X2 commutes with h, anticommutes with every longitudinal D and is +I on the low doublet. Each V edge therefore toggles precisely its two endpoint rung parities; resolvents preserve these parities. A nonzero path returning to P has even incidence at every rung. On an OPEN CHAIN this forces every used edge to have even multiplicity (strip endpoints inductively). Four V insertions therefore use at most two distinct edges.

Disconnected two-edge contributions cancel in the canonical effective H. One way to see this without assuming a diagrammatic convention is to turn on only disconnected bonds: both the low spectral projector and its overlap metric factor over the separated clusters, so the canonical isometry is a tensor product and its effective H is an additive sum. The mixed coefficient must vanish. Thus only a single edge repeated four times or two adjacent edges each used twice contribute. Their connected coefficients are determined by L2 and by L3 minus its embedded L2 terms. Root's L4 check then validates assembly in the presence of both overlapping and separated edge placements.

The stated linked formula is consequently supported for the finite open-chain perturbative coefficients:

single bond: [ -I/32+XY_ij/16-5 tau3_i tau3_j/32 ]/sqrt(2);
adjacent bond pair: [ -I/8-(XY_ij+XY_jk)/16-3XY_ik/16 ]/sqrt(2),

where XY_ij=tau1_i tau1_j+tau2_i tau2_j. The code counts each existing bond and each consecutive triple once. This support argument uses the chain graph; loops on other geometries can permit different parity-even paths and must not inherit it without checking. It does not establish a volume-uniform remainder or criticality.

## U(1) inference

Each displayed K2/K4 term commutes with Q0=sum tau3: XY is invariant under its simultaneous rotations and tau3tau3 commutes directly. This establishes that perturbative symmetry through fourth order. The finite four-rung probe computes Q^T diag(E_low)Q in the same polar gauge and directly tests its commutator with Q0. Its nonzero norms, beginning6.17e-8 at lambda .05 and3.98e-6 at .1, are far above the reported eigenpair residual scale. Dividing by lambda^6 tends numerically toward approximately3.94; this is evidence of a sixth-order breaking coefficient, not an exact extracted coefficient or outward-rounded theorem.

The measured statement is nonconservation of the UNDEFORMED Q0 in this canonical finite-band representation. A lambda-dependent dressed charge or a different gauge changes the operator being tested; this calculation alone does not exclude every possible exact dressed symmetry. Arbitrary spectral projectors of a finite Hamiltonian also supply formal conserved operators without proving a local U1 symmetry. The source's explicit finite polar-gauge scope is therefore appropriate. No exact all-orders U1, gapless phase, bulk criticality, equal-coupling validity or bulk3D scalar should be inferred from leading XY form.

The four-rung low-subspace calculation has a positive displayed gap and overlap singular value over its test points. It is a numerical band identification, not a complete interval enclosure; no large-volume claim follows. This reviewer independently reran the512-dimensional three-rung control, inspected the4096-dimensional contractions and supplied JSON, and did not independently repeat the four-rung ARPACK solve.

## SHA256 snapshot

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_fourth.py`: `980d9c4df8ab66385662290ecc9234b8589bfd19c103d47e48ff49b4e6e175bb`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_fourth.json`: `4619b18167326466e732427b7b240f97abdf580cdf877f4e1a66179817b8a9bc`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_linked_fourth.py`: `5825000db955302a7efd3911d6ae9690e8a5df25e9a91c5b785573b098707cdd`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_linked_fourth.json`: `3f0067794a6995f89a12128b44834d394dcd87bff79ba9b392ff9396e19fd173`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_u1_probe.py`: `f26f167e0f2ccbaf686c2f5ed1ea3be540e9fbfefff530502e06757e9edd3b04`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_u1_probe.json`: `514f4aeaadcee93b22c84214377fafe026509d15e5e8d0e0afbec61a58419162`
- `/private/tmp/native-rung-fourth-independent.py`: `f1d59797417f116760d61ad755d4296b536867c8b6bf33df9c3003acc828d57f`
- `/private/tmp/native-rung-fourth-independent.json`: `a911e658e4be56ad7019e54ec0d33e8f619deebae6fb62a98682b4a0c5594356`
