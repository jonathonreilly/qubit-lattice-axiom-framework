# Supporting mathematical source

Scope of this supporting source: exact constructive identities retain their stated mathematical validity. Any terminal exclusion developed below is preserved as deferred science, pending its required promotion packet; it is not promoted by this extract or used to strengthen the active canonical claim.

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_RUNG_HIGHER_CHECK.md`, SHA256 `f1955f8c9a8f5b753cba080b9bef7df0774c1ac25611e88100dffe38140b4143`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Independent higher-order native rung check

No formal audit, repository edit or new route. Root retains authorship.

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
