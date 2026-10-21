> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Cubic nearest-neighbor reference gap and active-energy operation

ROOT candidate, 2026-10-18. Distinct check pending. This changes the reference interaction graph from a line to a cubic grid while retaining the supplied product state and all positive two-body interactions. It aims to improve the sufficient runtime exponent. It does not provide reference preparation or permanent halt. The autonomous full-loader corollary additionally depends on the separately pending delayed-suffix candidate; no acceptance is inherited from authorship.

## 1. Concrete reference and gap target

Let n>=2 be an integer, V={0,...,n-1}^3, N=n^3, and E the nearest-neighbor grid edges. Each vertex carries an ordinary equal-gap qubit with free energy omega n_v. The ferromagnetic reference Hamiltonian is

 H_F = kappa sum_{e in E}(I-SWAP_e),   kappa>0.

Every block is positive real two-body with full norm2kappa. The connected grid has |E|=3n²(n-1), maximum degree6, and its zero eigenspace is the completely symmetric N-qubit subspace Pi. Each edge must fix a zero vector because its block is positive; adjacent swaps on a connected graph generate all permutations. The proposed explicit full-space inequality is

 H_F >= Delta (I-Pi),  Delta=kappa/(3n²).             (1)

No one-magnon-only gap or unproved many-body lifting is used.

## 2. Complete-graph comparison proof

For normalized psi define E_ij=<psi,(I-SWAP_ij)psi> and E_e analogously. For each ORDERED pair u,v choose the axis-ordered shortest path: first change x, then y, then z. It is simple, has length d<=3(n-1), and connects u to v. The transposition of its endpoints is a palindrome of adjacent swaps of length2d-1; each path edge appears at most twice.

For unitaries U_1,...,U_l,

 (U_1...U_l-I)psi = sum_{r=1}^l U_1...U_{r-1}(U_r-I)psi.

Cauchy–Schwarz and ||(SWAP_e-I)psi||²=2E_e give

 2E_uv <= (2d-1) sum_r 2E_{edge(r)}
        <=4(2d-1) sum_{e in path(u,v)}E_e,

so E_uv <=(4d-2)sum_path E_e <=12n sum_path E_e. For u=v the energy is0 and no path is needed.

The number of ORDERED canonical paths using any fixed grid edge is at most n^4/2. To verify, an x-edge across the coordinate cut k|k+1 at fixed y,z requires source y,z to be that edge's coordinates; there are 2(k+1)(n-k-1) choices of source/target x on opposite sides and n² free choices of target y,z. The product is <=n^4/2. For a y-edge, target x and source z are fixed, source/target y straddle the cut, and source x/target z are free. For a z-edge, target x,y are fixed, source/target z straddle the cut, and source x,y are free. The same ceiling follows in each case. This counts both directions, not just unordered pairs.

Therefore

 sum_{u<v} E_uv = (1/2) sum_{u!=v}E_uv
 <= (1/2)(12n)(n^4/2) sum_{e in E}E_e
 = 3n^5 sum_{e in E}E_e.                            (2)

For spin1/2 qubits the exact complete-graph identity is

 H_complete=sum_{u<v}(I-SWAP_uv)
           =N(N+2)/4-S_total².

The symmetric spinN/2 sector is its kernel; every other allowed total spin is at most N/2-1, so H_complete>=N(I-Pi). Combining this operator inequality with the quadratic-form inequality(2), valid for every psi, gives H_F>=kappa N/(3n^5)(I-Pi)=Delta(I-Pi). The spin identity and full-sector implication are the same checked elementary premise used in the line-reference proof, with no graph-specific spectral theorem imported.

## 3. Local exchange, effective operation and preserved hypotheses

Attach the active P qubit by a single exchange g exchange_(P,B_corner). Keep Q freely degenerate, H_E=omega(n_P+sum_B n_B), H_S=a X_Q+b(Z_Q+Z_P)+c Z_Q Z_P, and the same five positive data/exchange blocks:

 a=lambda/sqrt2, b=sqrt5 lambda/4, c=3lambda/4,
 g=sqrt2 lambda, s=a+2b+c+g,
 H_loc=H_E+sI+H_F+W, W=H_S+g exchange_(P,B_corner).

Every term still commutes with H_E. The product reference beta=|+>^N belongs to Pi and has H_F beta=0. Permutation symmetry of Pi, not of the entire graph Hamiltonian, gives

 Pi exchange_(P,B_corner) Pi=(1/N)Pi sum_v exchange_(P,B_v)Pi.

The projected star preserves Pi. The local-reference elimination proof uses only H_F Pi=0, H_F>=Delta(I-Pi), ||W||<=4lambda and ||(I-Pi)W Pi||<=sqrt2 lambda. All remain true. The actual grid can break permutation symmetry outside Pi; that is already charged by the finite-dimensional elimination argument. For lambda<=Delta/8 and 0<=t<=2pi/lambda it gives the same error<512lambda/Delta. No extra scalar phase is assigned to the positive ferromagnetic identities.

The star comparison, arbitrary QP/passive-reference inputs, effective gate spectrum and complete reference output are unchanged: residual g/(2sqrtN), effective norm9lambda/4, and exp[-i(pi/lambda)H_eff]=exp(-i pi/4)SWAP. A free revival lambda=omega/(2m) retains the exact phase convention. The earlier line theorem is not copied as a graph theorem without a gap proof; equations(1),(2) supply the changed premise.

## 4. Standalone explicit finite-window prescription

Let M=Lambda-omega>0, 0<epsilon<=1, C_P=(sqrt5+3)/2+2sqrt2. Choose

 n=ceil[(512pi²/epsilon²)^(1/3)], N=n³,
 kappa=M/32, Delta=kappa/(3n²),
 lambda_max=min{omega/2, M/(2C_P), epsilon Delta/16384},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m), tau=pi/lambda,
 w=epsilon/[32(omega+9lambda/4)].                    (3)

N>=512pi²/epsilon² and lambda<=Delta/8. These are exactly the local comparison accuracy hypotheses, with the new gap. Consequently, for the prescribed free-evolved beta(t), all outputs retained and every t in[tau-w,tau+w], the previous complete comparison yields vector<epsilon/8 and unhalved stabilized channel<epsilon/4, with target exp[-i(st+pi/4)]SWAP tensor beta(t). No stronger current-record or permanent-dwell statement is introduced.

Full-support loads are P<=omega+C_P lambda<=omega+M/2, Q<=C_P lambda<=M/2, an unattached grid site<=omega+12kappa=omega+3M/8, and the attached corner<=omega+6kappa+2g. Since 2g<=sqrt2 M/C_P<M/2, the corner load is <omega+11M/16<Lambda. Corner degree is3 within the grid, not6. The same conclusion follows with a conservative12kappa charge and this exchange allowance. Geometry: put B_(i,j,k)=(-1-i,-j,-k), P=(0,0,0), Q=(0,0,-1). All reference bonds, PB_corner and PQ are distinct nearest-neighbor edges; Q is not a reference site. The standalone complete graph has maximum degree6, all installed interactions nearest-neighbor, and no site collisions.

Counts: N+2 physical qubits; N+1 free occupation blocks, 5 data/exchange blocks and 3n²(n-1) reference blocks, total N+6+3n²(n-1). At fixed omega and positive M, n=Theta(epsilon^-2/3), Delta=Theta(M epsilon^4/3), lambda=Theta(M epsilon^7/3) asymptotically. The integer revival rounding changes lambda by at most a factor2. Thus this explicit family has sizeTheta(epsilon^-2) and sufficient timeTheta(M^-1 epsilon^-7/3), versus the checked line prescription's epsilon^-5 time. This compares sufficient prescriptions, not an optimality bound. The product coherence and coefficients remain supplied.

## 5. Conditional delayed-suffix full-loader corollary

This paragraph is conditional on the distinct validation of active_energy_loader_interface/PROPOSAL.md SHA4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570. It does NOT transfer the uniform-output-ray dwell result.

Replace its reference line by the cubic graph and choose

 n=ceil[(8192pi²/epsilon²)^(1/3)], N=n³, kappa=M/32,
 Delta=kappa/(3n²), L=ceil max{16,(2^20/epsilon)^2}, J_budget=M/64,
 lambda_max=min{omega/2, M/(4C_P),epsilon Delta/65536,4J_budget/(L+1)},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m).

Use exactly that candidate's alpha=lambda/2, tau=pi/lambda, three-entry w minimum, five-layer late suffix, physical blocks and target phase. Its proof sees H_F only through its symmetric kernel/gap, commutation with the prefixes and local W bounds, so these replacements preserve each calculation if that proof is valid. The complete conditional conclusion remains vector<7epsilon/128/channel<7epsilon/64 on its finite window, with full U_f and all reference/head outputs. Its nonzero gauge defect still prevents importing the old all-time exact record identity.

The suffix cube {0,1,2,3}³, P=(0,0,0), R=(1,0,0), Q=(0,0,-1), eight upward rays and cubic reference B_(i,j,k)=(-1-i,-j,-k) are pairwise disjoint. All reference interactions are nearest-neighbor and suffix interactions retain range<=9. The whole graph's maximum degree remains8 at R; grid sites have degree<=6 and its attached corner degree4. This is bounded-range, not an all-nearest-neighbor full loader.

The full-support cap for Q/P/R/head is unchanged. The corner has omega+6kappa+2g, with 2g<=sqrt2 M/(2C_P)<M/4, and every other grid site has at most omega+12kappa. Thus all fit Lambda. Total qubits are4L+N+7. The head blocks remain8L+34; adding the new local inventory gives8L+N+40+3n²(n-1). At fixed omega,M the new weak-coupling constraint behaves as epsilon^7/3 and eventually dominates the clock cap epsilon², so total sizeTheta(epsilon^-2), runtimeTheta(M^-1 epsilon^-7/3). Enormous constants in L remain. No practical-time assertion or new halt mechanism follows from the better exponent.

## 6. Evidence/exposure limits

ROOT derived the grid canonical-path comparison after complete reads of the checked local-reference line proof9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70/checkbc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b and product-reference static SWAP1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825, and the pending delayed-suffix source4adb0. The elementary gap is a new self-contained calculation in this campaign; no originality relative to general ferromagnetic spectral-gap literature is asserted. No scientific executable or simulation was run. Both the new grid proof and the interface application require selective distinct checks. Native initial product coherence, selective couplings/equal gaps, arbitrary H_PE, stable capture and reuse remain open. No editable prompt or physical axiom changed.
