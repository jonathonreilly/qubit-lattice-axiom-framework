# Nominal converted device: physical inventory and finite-output transfer

Status: proposed analytical resource/transfer interface, not independently checked. With the explicit indexing below the finite apparatus has M+194 head qubits, M+198 total physical qubits and M+194 head-hopping edges. Its first omitted output vertex is distance M+105 from the seed. A fresh one-head radius18 bound yields finite/infinite evolution error at most

    4 exp[-(M+105)+36 T sinh(1)]/(1-exp(-1))

uniformly for0<=t<=2T. T is an unspecified parameter, not a new onset claim. Temporal escape and any complete-output infinite-device error are separate inputs.

## Exact inputs and exposure

Use nominal F40 converter composition1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78 and checked review f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c; ell20 terminated new input and equal-diagonal emitter from endpoint proposal22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a and check200268709480f1533050f5d197a4bed7a2acaefa5f4a22a662938ddb504619c6. Set nominal kappa=1e-8. No old emitter compensation or endpoint theorem is silently carried over.

Read necessary canonical note passages at SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff: exact B/source/contact coefficients (lines90–145), original emitter/scalar comparison (350–426), complete geometry/positive-block/load/finite-polynomial derivation (570–675), together with the source/filter passages already read in this coherent task. Source path is correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md. The quoted ancestry stays conditional; unrelated note content is not endorsed.

This is source-exposed original derivation based on checked stationary inputs, not an independent review of itself. No unfinished temporal proposal was read. No scientific/numerical execution, sweep, solver, delegation, Git/W/checkpoint/prompt/model change occurred. Only source reading/hash checks and this deliverable were performed. Applicable unchanged workflow is reused. There is no new physical-unit, native-supply or all-future halt claim.

## 1. Explicit sites, indexing and graph count

Retain the canonical D=40 cubic geometry: old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0). Retain both45-site arm paths, their source contacts, the arm1 filter at arm positions20/21, and the four junction-square edges. Arm endpoints remain at N=44. Port origins are out=(D+1,1,1) and in=(D,2,1).

On EACH port retain old-J vertices m=0,...,F with F=40. These coordinates are out_old(m)=(D+1+m,1,1) and in_old(m)=(D,2+m,1). Connect m=F by the converter bond to the first new vertex n=0. Continue straight outward:

    out_new(n)=(D+F+2+n,1,1), n=0,...,M-1,
    in_new(n)=(D,3+F+n,1), n=0,...,ell, ell=20,
    emitter=(D,4+F+ell,1).

All installed edges are cubic nearest neighbors and all listed vertices are distinct. The added extensions point away from the original arms/junction. As in the supplied original graph, unused geometric NN adjacency does not imply an installed Hamiltonian interaction. Require integer M>=1.

Head vertices are90 arm sites+82 old-port sites+21 new-input sites+1 emitter+M new-output sites, totaling M+194. Add the SAME two old and two shared-source qubits, giving M+198 physical qubits; passive reference systems are not apparatus qubits.

Head edges:88 arm edges+4 junction edges+80 old-port edges+2 converters+20 new-input edges+1 emitter edge+(M-1) new-output edges=M+194. The source A--B hopping and old/source/contact interactions are not head-graph edges and are counted separately as physical blocks. Relative to the original M+112-head inventory, the two retained old-port segments add82 vertices; the input and output conventions here refer M to NEW output sites only. No emitter or source is duplicated.

The shortest emitter-to-input-origin distance is1+ell+1+F=62. Junction input-to-output origins have distance2 through either arm endpoint. From output origin to the first omitted new vertex n=M isF+1+M. Thus

    d_M=62+2+40+1+M=M+105.                          (1)

A route through the source contacts does not move the head to another clock site. The source/internal couplings therefore do not shorten this graph distance. The one square cycle is already included in the two-edge junction route.

## 2. Complete positive block inventory and scalar

Use Q(h)=|h|(nx+ny)+h(exchange), PSD on the full four-state pair with norm2|h|. Define gamma_J=(sqrt(2)-1)J and beta=J[(1+S0)/C0-1] for the unchanged junction/filter. Define gamma_c=tau-j for converters, with tau²=jJ S0 and j=J(1-C0). These symbols distinguish the two unrelated vacancy coefficients.

The retained internal positive blocks, occurring ONCE on the shared old/source fiber, are K=2I+Z1Z2; DeltaA nA; DeltaB nB; Q_AB(-h); u_AB nA nB; gA nA(I+X1); gB nB(I+X2). Their sum is the canonical B. There are seven such blocks in this chosen decomposition.

For each of the two arms retain lambdaA n_c0(I+XA), mu0 n_c0, lambdaB n_c1(I+XB), and nu(I-n_c1), all positive and at most two-local. These eight blocks reproduce the canonical head-conditioned VA/VB and total common scalar2nu. Their occurrence on two clock arms does not duplicate B or its source qubits.

Head hopping blocks comprise167 ordinary old-J Q bonds (87 nonfilter arm bonds and80 port bonds), one filter Q(-t_filter), four junction Q bonds of magnitude J/sqrt(2) with the prescribed signs, two converter Q(-tau), M+19 ordinary new-j Q bonds, and one STRUCTURED emitter bond B_end=j(ne+nend)-kappa(exchange). The count is M+194, agreeing with the head-edge inventory. B_end is PSD on all four states, with eigenvalues0,j-kappa,j+kappa,2j and norm2j. It is not replaced by the old Q(-kappa) compensation family.

Additional positive onsite blocks are two entrance J n_c0, two filter beta(I-n), four junction gamma_J(I-n), four converter gamma_c(I-n), one emitter j ne, and one finite-output cap j n_out_new(M-1). This gives14 onsite blocks in this chosen decomposition. Together with seven internal and eight contact blocks, the total chosen positive-block inventory is M+223. Merging onsite terms could change that bookkeeping count, not the supplied Hamiltonian.

At each converter the exact FULL-space identity is

    Q(-tau)+gamma_c[(I-n0)+(I-n1)]
       =2gamma_c I+j(n0+n1)-tau(exchange).

The ordinary neighboring J/j bonds then give the required relative diagonals J+j and2j. The emitter bond plus j ne and retained j endpoint bond gives2j at both emitter and input endpoint. The finite cap preserves output endpoint diagonal2j after deleting the next new-j bond; it is not an absorbing boundary.

The full physical scalar, separated from the unchanged B containing K, is

    c_total=2nu+2beta+4gamma_J+4gamma_c.             (2)

Emitter occupations and finite cap add no vacancy scalar. This identity holds on the entire qubit space, including vacuum and double occupation, not just the one-head sector. The intended physical comparison must retain exp(-it c_total) and exp(-itK) with the literal W. No scalar or old aging is removed by redefining the zero of a target after delivery.

All terms are static, so modeled slew is zero. Original old/source/contact loads remain as supplied; in particular source A/B loads27.936224853155858 and22.228906875353305 are unchanged. Conservative changed-site incident-block norm sums are: old converter site<=2J+2tau+gamma_c<.083; first new converter site<=2j+2tau+gamma_c<.027; emitter<=3j<.009; terminated input endpoint<=4j<.012; ordinary new sites<=4j<.012. For M=1 the output cap replaces its missing new-j bond and the first-site bound remains safe. Old ordinary/filter/junction loads retain their canonical ceilings. There is no all-site cap2 assertion; the shared-source loads dominate.

## 3. Fresh bounded one-head Hamiltonian estimate

The physical Hamiltonian preserves head excitation number. The delivered seed lies in the invariant ONE-head sector, while all old/source/reference coordinates remain present. Only this sector is used below; the total many-head Hamiltonian norm is not bounded by18 and can grow with M.

After removing c_total, the one-head operator is I_head tensor B plus the head clock matrix and the four head-conditioned VA/VB contacts. B in[1,20] gives ||B-10.5I||<=9.5. Because the contact head supports are orthogonal, their combined norm is their maximum, not the sum over arms: ||V_contacts||<7.926.

A direct absolute row-sum bound for the NEW clock matrix is<.15. Ordinary old rows have sum<=4J<.124. Junction rows have diagonal2J and incident magnitudes J+sqrt(2)J, so sum=(3+sqrt(2))J<.137. With C0>.9 and S0<.5, a filter row is bounded by3J+J/C0+JS0/C0<(3+5/3)J<.145, including the diagonal shift without relying on its cancellation. Old converter rows have sum2J+j+tau<.072; new converter rows have sum3j+tau<.016. Ordinary new, input endpoint and emitter rows are smaller. Arm entrance rows and the finite cap also satisfy this ceiling. These bounds apply to the real symmetric operator on the infinite graph by the Schur row/column test, as well as to every finite compression.

Consequently, with c_star=c_total+10.5,

    ||H_infinity^(1)-c_star I||
       <9.5+7.926+.15<18.                          (3)

The finite compensated one-head Hamiltonian is the compression of the infinite one-head Hamiltonian to retained head sites, with the same internal fiber. The cap j n_last supplies exactly the diagonal contribution of the removed Q(-j) edge, so compression preserves that boundary diagonal. Its spectrum is contained in the SAME radius18 interval about c_star. This is a new check for the changed weights/diagonals, not an invocation of the old endpoint theorem.

## 4. Polynomial locality and finite transfer

Let V_seed embed arbitrary old/reference input into the fixed emitter-occupied/source-vacuum seed. Embed the finite one-head Hilbert space into the infinite one by blank omitted head qubits. Internal B and contacts do not change head location; a product of n Hamiltonian factors moves the head at most n graph edges. The first omitted head vertex is distance d_M in(1). Therefore for every polynomial p of degree<d_M,

    p(H_infinity^(1)) V_seed
       = embed[p(H_M^(1)) V_seed].                 (4)

The same holds after the common affine rescaling by c_star and18. It holds as an operator on the entire old/reference seed subspace, not only for four scalar columns. No extra sqrt(2) aggregation is needed for this finite-transfer estimate.

For the rescaled selfadjoint operators with spectra in[-1,1], ||T_n||<=1. The Chebyshev expansion of exp(-i18t x) has nonconstant coefficients2(-i)^n J_n(18t). The standard generating contour of radius exp(1) bounds |J_n(18t)|<=exp(18|t|sinh(1)-n). Canceling the common terms below d_M using(4), bounding the two remaining Chebyshev operators by2, and summing the geometric tail yields

    ||U_infinity(t)V_seed-embed[U_M(t)V_seed]||
       <= min{2, 4 exp[-d_M+18|t|sinh(1)]/
                                     (1-exp(-1))}. (5)

The common c_star phase has modulus one in this difference; that cancellation does not authorize deleting the physical scalar or K aging from a separately specified output comparator. The proof uses neither scattering completeness nor absence of point spectrum. Finite point spectrum and recurrences are fully compatible with this bounded-time estimate.

For any independently chosen T>=0 and all0<=t<=2T, a sufficient explicit transfer ceiling epsilon_tr>0 is

    M+105 >=36 T sinh(1)
                 +log[4/((1-exp(-1))epsilon_tr)].   (6)

Choose an integer M>=1 satisfying(6) BEFORE delivery. This is a relation between the requested horizon and graph size, not selection of a new time or a claim that escape occurs by T. All physical coefficients and blocks are independent of elapsed time.

If a separately proved complete infinite-output operator error is epsilon_infinity(t), then the same finite device, embedded into the infinite output comparison space, has error at most epsilon_infinity(t)+the right side of(5). Passive-reference tensoring preserves this bound; the corresponding unhalved pure-state/channel trace-distance ceiling is at most twice that sum. The comparator here is the same normalized INFINITE output packet with the same full scalar and old aging. No finite-packet renormalization, projection/postselection, capture or hidden branch deletion is substituted.

## Remaining obligations

The inventory and polynomial estimate require selective independent checking. They do not derive the supplied Hamiltonian/initial product state from native framework physics, assign physical time/energy units, prove fabrication precision, optimize resources or establish an infinite-device temporal error. The separate temporal argument must retain every source/emitter/converter/buffer/closed coordinate and give its own onset/window before(6) becomes a concrete finite apparatus choice. No old runtime or window has been transferred, and no claim of all-future finite halting, reset or reuse is made.
