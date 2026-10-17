# Nominal converted apparatus: selective resource and finite-transfer check

Disposition: no load-bearing defect found in the stated inventory, positive-block realization or finite-output transfer. For integer M>=1 the supplied construction has M+194 head qubits, M+198 physical qubits, M+194 head edges and M+223 positive blocks in the explicitly chosen decomposition. The new radius-18 estimate and distance M+105 support the displayed finite/infinite operator bound. This is a source-exposed analytical check, not a temporal escape proof, selected onset/window, native realization result, or audit verdict.

## Source identities and exposure

Read the complete ../bandcenter_resources/PROPOSAL.md at SHA256 96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7. Verified the cited composition proposal/check identities 1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78 and f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c, and endpoint proposal/check identities 22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a and 200268709480f1533050f5d197a4bed7a2acaefa5f4a22a662938ddb504619c6. Read their construction/parameter and emitter sections needed here. A combined ancestor read was truncated; I do not claim complete review of those ancestors. Necessary construction passages were separately read without truncation. Their stationary spectral conclusions are not required for the polynomial-transfer proof.

The canonical source is correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md, verified SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. Read lines 1–210, 210–265, 275–325, 350–426 and 570–675, including the actual coefficient table, source/contact definitions, filter, junction and full coordinate paths. Unrelated canonical theorem claims are not endorsed. In particular no old emitter, onset or finite-window theorem is imported.

Read local AGENTS.md (febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0), SCIENCE_WORKFLOW.md (71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3), installed physics-claim-reviewer skill (9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455), and local freshness guidance. Used the explicitly assigned frozen/local sources; no Git refresh or audit/backlog workflow was performed. This applies the reviewer skill to the bounded requested check. No separate agent, scientific program, solver, parameter sweep, temporal proposal, external literature, Git/W/checkpoint/prompt/model edit or publication was used. File reading, hashes and this report are the only operations. Independence consists of the analytical reconstruction below after exposure to the proposal, not independent origin or blind numerical verification.

## Geometry and counts

The canonical arm0 has 37 straight vertices plus eight listed detour/endpoint vertices; arm1 has 42 straight vertices plus three listed vertices. Consecutive displacements are unit cubic steps. Their z coordinates and final coordinates separate them from each other, the old/source square and the two exterior port rays. Each arm end is adjacent to both port origins, yielding the four-edge square. The old port endpoints are (81,1,1) and (40,42,1), with first new vertices (82,1,1) and (40,43,1). The input n=20 endpoint is (40,63,1), adjacent to emitter (40,64,1). The outward rays introduce no overlap. Uninstalled geometric adjacency creates no Hamiltonian edge under the supplied selective-coupling premise.

Thus 90+82+21+1+M=M+194 head sites and four shared old/source qubits give M+198. The edge sum is 88+4+80+2+20+1+(M-1)=M+194. The shared B is not copied on either arm or port: I_head tensor B describes the restriction of one physical old/source operator, not a sum of physical copies. Source hopping does not count as a head edge.

The emitter-to-input-origin path has 1+20+1+40=62 edges. The square requires two further edges to output origin; output origin to first omitted n=M requires 40+1+M. This proves d_M=M+105. Neither contact projectors nor B move the head. The arm ends have no cross-connection through their common internal fiber, so a putative shortcut through the source is invalid.

## Full-qubit positivity, scalar and incident loads

On a pair, Q(h) has eigenvalues 0,0,2|h|,2|h|. The structured emitter block has 0,j-kappa,j+kappa,2j. Thus both are PSD with the stated norms for nominal 0<kappa<j. All seven internal blocks and eight contact blocks are positive; K has eigenvalues 1 and 3, and n_source(I+X_old) is positive because its factors commute on distinct qubits. The beta, gamma_J and gamma_c vacancy coefficients are positive: C0>0, S0>0 and S0>1-C0 imply tau>j.

Expanding a converter on the full four-state pair gives exactly 2gamma_c I+j(n0+n1)-tau(exchange); this identity also checks the vacuum and double-occupation sectors. Two converters add 4gamma_c, two filter vacancies add 2beta, four junction vacancies add 4gamma_J, and the two contact nu vacancies add 2nu. The emitter and cap add no scalar. B still includes K. Hence c_total in the proposal is the correct common scalar; physical comparison still requires its phase and full elapsed K aging.

There are 167 old ordinary hopping blocks, one filter, four junction, two converters, M+19 new ordinary blocks and one emitter block, totaling M+194. The remaining onsite count is 2+2+4+4+1+1=14. Adding seven internal and eight contact blocks gives M+223. This is a decomposition count, not an invariant minimal number of terms.

Independent source-load reconstruction gives A load DeltaA+2h+u_AB+2gA+4lambdaA and B load DeltaB+2h+u_AB+2gB+4lambdaB, reproducing respectively 27.936224853155858 and 22.228906875353305 from the exact coefficients. These large shared-source loads are retained. Old converter load is 2J+2tau+gamma_c<.083; first-new load is at most 2j+2tau+gamma_c<.027. Emitter load is 3j, input endpoint load 4j, and ordinary new load 4j. For M=1, the new-output cap contributes only j, making the stated first-new ceiling conservative. No all-site cap 2 follows.

## Fresh one-head bound and exact compression

Head number is conserved by every block. In the one-head sector, removing c_total leaves B, a real scalar clock matrix and four contacts on mutually orthogonal head projectors. Independently, positivity gives B>=I and the sum of block norms gives

    ||B|| <=3+DeltaA+DeltaB+2h+u_AB+2gA+2gB <20.

Therefore ||B-10.5I||<=9.5. The larger contact norm is ||VA||=2lambdaA+mu0=7.925057370220605<7.926; VB has eigenvalues -nu and 2lambdaB-nu, both smaller in absolute value. Orthogonal head supports make the combined contact norm the maximum, even with one shared internal system.

A row check independently gives the clock ceiling. Ordinary old rows have sum 4J; junction rows have sum (3+sqrt(2))J. The filter's actual relative diagonal is 2J-J/C0 and its off-diagonal magnitudes are J and JS0/C0, so the conservative bound 3J+J/C0+JS0/C0 used in the proposal is valid even without exploiting its subtraction. Converter rows are 2J+j+tau and 3j+tau. Ordinary new rows have sum 4j, input endpoint 3j+kappa, emitter 2j+kappa; the arm entrances and capped output obey the same larger .15 ceiling. C0>.9, S0<.5, J<.031, j<.003 and tau<.007 establish all claimed loose ceilings. Symmetry gives both row and column bounds, hence the infinite scalar clock operator is bounded by .15.

Consequently ||H_infinity^(1)-(c_total+10.5)I||<9.5+7.926+.15=17.576<18. This uses the newly specified diagonals and weights. It is not a norm bound on the full physical many-head Hamiltonian.

Compressing a removed Q(-j) bond onto blank omitted head sites leaves precisely j n_last. The prescribed cap therefore makes the finite one-head operator exactly P H_infinity^(1) P on the retained space, with unchanged internal fiber and scalar. This works also for M=1. Compression contracts the centered operator norm, proving the same center and radius for every finite apparatus.

## Polynomial and Chebyshev transfer

Every factor either preserves head position or traverses one installed head edge. Starting at the emitter, a length-n word with n<d_M cannot enter an omitted site. Thus all powers, and therefore all polynomials of degree less than d_M, agree on the entire old/reference seed subspace after finite embedding. This argument retains arbitrary internal evolution and does not rely on four scalar scattering columns or parity aggregation. The same statement holds under common affine centering/rescaling.

For A=(H^(1)-c_star)/18, both spectra lie in [-1,1], so ||T_n(A)||<=1. The generating function exp[(18t/2)(z-z^-1)] on |z|=e gives |J_n(18t)|<=exp(18|t|sinh(1)-n). The Chebyshev coefficient magnitude is 2|J_n| for n>=1; the difference of the two operator terms has norm at most 2. Cancellation below d_M and the geometric series therefore give

    ||U_infinity(t)V_seed-embed U_M(t)V_seed||
      <=min{2,4 exp[-(M+105)+18|t|sinh(1)]/(1-exp(-1))}.

The common phase cancels only within this comparison. For 0<=t<=2T the proposed logarithmic condition on M is sufficient for error <=epsilon_tr. T remains an independently specified parameter; there is no derived temporal escape or selected resource instance here. Adding a separately established complete infinite-output operator error uses only the triangle inequality with the same normalized infinite target. Tensoring passive references preserves this bound; unhalved pure-state trace distance, and the corresponding channel distance with references, are bounded by twice the sum. No packet projection or finite-output renormalization is inserted.

## Scope of the conclusion

The finite-transfer interface is supported for the exact supplied static graph and pure one-emitter/blank-head seed. It remains useful independently of any stationary scattering proof. Turning it into a concrete successful finite operation still requires an independently established complete infinite-output error and its onset/window, including all localized and complementary coordinates. Physical units, native Hamiltonian/state supply, fabrication precision, resource optimization, all-future halting, reset and reuse remain outside this check. No editable prompt file was changed.
