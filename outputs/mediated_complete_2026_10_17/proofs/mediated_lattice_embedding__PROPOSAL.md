# Explicit straight-ray embedding of the mediated source

Status: conditional author geometry derivation requiring a distinct check. For every integer m>=1 the specified mediated path has an explicit collision-free cubic nearest-neighbor embedding attached to the existing input port, with no auxiliary routing heads. This discharges the coordinate-existence premise of the preceding graph inventory under the unchanged supplied lattice and interaction-selection assumptions. It does not establish native coefficient supply, preparation or a complete dynamical theorem.

## 1. Complete inherited coordinate sets relevant to the new ray

Use D=40 and the corrected canonical geometry, not its discarded provisional arm route. The four old/shared-source qubits are

    old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0).

The original head arms are exactly:

- Arm0: (n,1,1), 0<=n<=36, followed by (36,1,2),(36,1,3),(37,1,3),(38,1,3),(38,1,2),(38,1,1),(39,1,1),(40,1,1).
- Arm1: (n,1,-1), 0<=n<=41, followed by (41,2,-1),(41,2,0),(41,2,1).

Each contains45 heads. Their junction port origins are (40,2,1) and (41,1,1). The retained old input buffer is (40,2+k,1), 0<=k<=40, and the new input is (40,43+n,1), 0<=n<=20. Its terminal port is

    p=(40,63,1).

The old output buffer is (41+k,1,1), 0<=k<=40. Its converter enters the retained cable (82+n,1,1), 0<=n<=17. The next head is the record-gate input (100,1,1).

For completeness the gate's local arm0 list is (1,0,0),(2,0,0),(2,1,0),(1,1,0),(1,2,0),...,(1,8,0), and local arm1 is (-1,0,0),(-1,1,0),...,(-1,8,0),(-1,8,1),(0,8,1). The two local ports are (0,8,0),(1,8,1). Apply the actual map F(x,y,z)=(108-y,1+x,1+z). Every gate head then has100<=x<=108, 0<=y<=3, 1<=z<=2. The unique record is F(0,0,0)=(108,1,1), distinct from every head. Its two terminal contacts remain nearest neighbors. The final gate output is o=(100,2,2). The slow sites are

    r_n=(100,3+n,2), n>=0,

or n=0,...,M−1 in the finite receiver. Their connector to o is unchanged. The gate's old output-port vertex is not duplicated as r0.

This list exhausts the inherited head sets and five nonhead qubits. Shared B consists of the fixed old/source-qubit blocks and is not a separate set of spatial copies at each head. Passive reference systems are not placed as apparatus vertices. All other old head-conditioned contacts, source blocks, filter, converter and gate supports retain their previously supplied physical coordinates.

For this replacement REMOVE the nominal three-source heads as labeled source degrees of freedom at (40,64,1),(40,65,1),(40,66,1), together with their six source blocks. Their lattice positions may be reused for different new path roles below; no duplicate physical qubit occupies them. The remaining emitter-free apparatus ends at p on the proposed line. Starting instead with H_bg requires omission of its positive j n_p cap before adding the replacement path. Both descriptions give the same corrected background compression.

## 2. New labels and path lengths for every m

Define an injective coordinate map

    v_r=(40,63+r,1), 0<=r<=10m−1,
    v_0=p,
    s2=v_(2m+1), s1=v_(6m), s0=v_(10m−1).          (1)

All indices are distinct for m>=1: 0<2m+1<6m<10m−1. The internal mediator sets are

    chain3: v_1,...,v_(2m),
    chain2: v_(2m+2),...,v_(6m−1),
    chain1: v_(6m+1),...,v_(10m−2).

Their cardinalities are respectively2m,4m−2,4m−2. Thus n3=m and n1=n2=2m−1 exactly. Their numbers of endpoint-to-endpoint edges are2m+1,4m−1,4m−1, summing to10m−1. No padding or detour changes the mediator exponents.

Install only consecutive path bonds v_r--v_(r+1). On chain l the two endpoint bonds have magnitude gamma_l; between its 2n_l internal vertices use alternating J_m,q,...,q,J_m. Both end internal bonds are strong J_m because the internal count is even. Reversing an even path preserves this endpoint convention, so listing the ray from p toward s0 rather than s0 toward p does not change its exact mediator functions or t_l(0) sign. All hoppings remain physically negative. The endpoint sign gauge used in the analytical Schur formulas is a representation change, not a relocation or a physical positive hopping.

For m=1, s2=v3, s1=v6 and s0=v9. The internal sets are v1,v2; v4,v5; and v7,v8. In particular the former three source positions now contain two mediator heads and s2. They are reused once after removing the old blocks, not treated as additional obstacles or retained old source contacts.

## 3. Collision and adjacency proof, uniform in length

Each new vertex has x=40,z=1,y>=64. The original arms and both old output/cable sets have y<=2. The old and new input segments on x=40,z=1 stop at y=63. The four original nonhead qubits have x=0 or1 and z=0. Every gate head and its record have x>=100. The infinite slow ray has x=100,z=2, regardless of how large its y becomes. Hence none of those retained vertices coincides with any v_r for r>=1. This is uniform in m and in finite receiver length M, and remains true for the infinite receiver.

Distinct new r give distinct y, so the path does not collide with itself. Its consecutive edges have Manhattan distance one. Nonconsecutive v_r have distance at least two; no chord or unintended nearest-neighbor pair arises within the new ray. A new vertex's four transverse neighbors have coordinates (39 or41,63+r,1) or (40,63+r,0 or2); none belongs to the retained apparatus. Its longitudinal neighbors are its predecessor/successor on the ray, with the predecessor of v1 equal to p and the neighbor beyond s0 unused. Thus the ONLY new-to-retained nearest-neighbor pair is v1--p. This is stronger than merely selecting away unintended source-core edges, although the inherited selective-support premise remains necessary elsewhere in the original apparatus.

At p, the existing input neighbor is (40,62,1). The unused +y direction is v1. Its transverse neighbors at y=63 are unoccupied. The new bond therefore extends the existing input in its free outward direction without moving p, its converter, cap plane or old phases. There is no new contact to old/source/record qubits anywhere along the ray.

The finite path occupies a straight segment of the supplied cubic lattice. Its bounding y coordinate is63+(10m−1)=10m+62. This is a spatial extent, not an additional qubit count: unused lattice sites are not installed qubits in this supplied selective-lattice construction. If a different physical model requires material or controls at every intervening ambient site, those are separate resources not established by these proofs.

## 4. Allowed supports, diagonals and unchanged internal system

Use the corrected positive path blocks Q_b=b(n_u+n_v−exchange_uv) on these consecutive nearest-neighbor pairs, and the single-site occupations

    (2j−gamma1)n_s0,
    (2j−gamma1−gamma2)n_s1,
    (2j−gamma2−gamma3)n_s2,
    (j−gamma3)n_p,

plus (2j−sum incident b)n_v on each internal mediator head. Their coefficients are nonnegative under the existing sufficient installation inequalities. They are exactly the already supplied real one-/two-qubit PSD block types. No new nonlocal coupling, three-body controlled hopping, or source-copying operation is required by this layout.

All added source and mediator one-head diagonals are2j. At p the old input bond contributes j; the new gamma3 bond plus (j−gamma3)n_p contribute j, giving the same2j diagonal. Compression off all new path heads leaves precisely j n_p, restoring H_bg. The old cap must not be retained in addition. No added vacancy term supplies a scalar; c_att is unchanged.

The shared old/source Hamiltonian B remains installed once on its original four qubits. Its appearance as I_head tensor B in the invariant one-head description does not require an interaction between each distant mediator and those four qubits. The new path hoppings act as identity on that same internal fiber. No new head-conditioned internal contact is added. Old K, record-X sectors, the prepared old/reference embedding and all original contact supports are unchanged. These are supplied Hamiltonian and initial-state premises, not a derivation of native locality or preparation from a microscopic model.

## 5. Resources and cut interface now supported by an explicit layout

There are10m−4 internal mediator heads and three source heads in addition to the existing p. Therefore the10m-head local path INCLUDES p and contributes10m−1 added heads. It replaces the old nominal three-head source, a net increase10m−4. No routing heads are needed in (1).

Starting from the unchanged nominal M-slow-site inventory gives

    head qubits          M+10m+234,
    physical qubits      M+10m+239,
    head-hopping edges   M+10m+235,
    listed PSD blocks    at most2M+20m+274.

The block formula removes the six nominal source blocks and adds10m−1 Q blocks plus10m occupation blocks. Zero occupation blocks can be omitted. The five nonhead qubits remain the two old, two shared-source and one record qubit; p is never counted twice. These are layout counts, not a physical fabrication or optimality certificate.

The graph distance from s0 to p is10m−1. The inherited p-to-first-slow-site distance125 then gives first omitted r_M distance M+10m+124. The straight physical layout introduces no shortcut. The output-only cut still assigns weight zero to the whole ray (1); its last slow-site weight remains M−1, so no new distance improvement is inserted into that estimate. This note addresses only the earlier embedding premise, not an independent review of the finite-cut analytical source or any time guarantee.

The construction establishes a nearest-neighbor layout for each finite integer m under the supplied unbounded cubic-site availability and selective interaction contract. Exact mass-tuned coefficient correlations, their positivity margins, seed preparation, all dynamical matching/regularity and common-output comparisons remain separate. No native interaction law, all-late finite storage, practical scale or complete runtime is claimed.

## 6. Exact sources, exposure and limits

Refreshed complete relevant coordinate/support passages include the canonical geometry/positive-block section, converted-resource indexing, explicit local gate paths and their actual attached transform, original input extension, and nominal three-source replacement. Exact current hashes were checked:

- Canonical `correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`:71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. Its discarded provisional coordinate route is not used.
- `bandcenter_resources/PROPOSAL.md`:96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7.
- `autonomous_record_route/PROPOSAL.md`:93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56.
- `record_attached_kernel/PROPOSAL.md`:fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457.
- `two_site_actual_attachment/PROPOSAL.md`:2c0e8fe8dac3dd70f50fbc945aa0fd29a5eacbac63468ff5983cc7abd5343f49.
- `three_site_actual_attachment/PROPOSAL.md`:4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006.
- Corrected `mediated_critical_source_interface/PROPOSAL.md`:d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3, with scoped correction recheck2cea5e9a3cd59b63d09bf21c1ddb929fff2251f9044ed3bd7189b3df10062ff8, reused at its unchanged block scope.
- Prior author `mediated_finite_cut_interface/PROPOSAL.md`:5bcb4f17ae54f968a5d7566a2215810309b76351463e5034c5ee50d8cb307822; its separate review is not assumed complete here.

Root supplied the straight-ray candidate and endpoint indices. I reconstructed the path lengths, complete inherited coordinate exclusion and supports rather than treating that suggestion as evidence. I authored resource/recovery ancestors and the preceding cut proposal, and share substantial source exposure. This is new author geometry work requiring a distinct check, not independent ancestral certification. Deterministic source hashes established identity only. No solver, coordinate sweep, dynamics, new operating point, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.
