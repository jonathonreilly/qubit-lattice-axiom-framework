# A literal old-system attachment in a finite compass family

Claim type: bounded_theorem.
Primary runner: `scripts/product_reference_attachment_controls_2026_10_18.py`.

Publication evidence boundary: The complete arguments below and their supporting derivations remain the mathematical basis, with exactly their stated suppliers and hypotheses. Original review dispositions, author-time statuses and old hashes record history; they are not fresh execution evidence or authority. Current live source identities are listed in `outputs/product_reference_attachment_review_2026_10_18/INPUT_CLOSURE.json`. The shared primary supplies finite matrix and budget controls, not a simulation of the enormous apparatus or a proof of physical supply.

## Result and status

A given two-qubit old Hamiltonian can remain installed inside a finite open compass lattice, with every lattice bond present, while the complete evolution approximates its freely aged target gate on a calibrated observation window. The comparison retains the actual isolated-environment Hamiltonian and every environment output. It is a full-space operator estimate: no basis state, pure state, internal product state or endpoint eigenstate is required of the environment. Initially correlated states are compared with the same state acted on by the stated joint local unitary; they are not converted into product states.

This is a conditional positive-block construction. The old block is supplied explicitly once, the compass coefficients are supplied, and their small ratios are measured against the fixed old splitting. The result does not derive the old block or those coefficients from microscopic axioms. It is not the original source/clock inventory, an infinite-volume theorem, a preparation mechanism, or a permanent halt.

The interior source and actual-environment addendum received a distinct same-model, source-exposed mathematical check, accepted by ROOT. The larger-finite-box extension below is the explicit derivation in §8 of that review. The cube comparison and full-space corollary also received their own accepted distinct check. This manuscript integrates those arguments; it is not another independent check or a retained audit. Exact evidence identities appear at the end.

Frozen evidence and exact source identities are recorded in the publication manifest (`outputs/native_compass_literal_attachment_2026_10_18/SOURCES.json`).

## 1. Installed model and complete comparator

Put old sites 1 and 2 at (0,0,0) and (1,0,0). Install the literal block

\[
 K=2I+Z_1Z_2
\]

once, in addition to the compass bond on their edge. Its spectrum is {1,3}, its norm is 3, and its ZZ coefficient fixes the energy unit. Write X=X₁X₂ and choose θ in (π/4,π/2) with cos θ=3/5 and sin θ=4/5. The target is exactly

\[
 W=e^{i\theta}e^{i\theta X}
   =\frac{9+12i}{25}I+\frac{-16+12i}{25}X.                 \tag{1}
\]

In particular [K,X]=0. The old target at elapsed time t is e⁻ⁱᵗᴷW, with the entire elapsed old evolution and its scalar 2I retained.

For each nearest-neighbor lattice edge in direction a=x,y,z install

\[
 Q^a_{uv}=J_a(I-\sigma_u^a\sigma_v^a),\qquad J_a>0.
                                                               \tag{2}
\]

Every block is real, positive, at most two-body, and has full-support norm 2Jₐ. In particular Y⊗Y is a real matrix. Set J=Jₓ and s=Jᵧ+J_z. The physical Hamiltonian is

\[
 H=K+\sum_{\text{all internal edges}}Q^a_{uv}.             \tag{3}
\]

Only the raw directional compass interaction and its finite-open convention are imported from the microscopic source snapshots. No periodic-ensemble result, conserved-scalar conclusion, z-dominant normal form, dressing estimate, or truncation is used.

First take

\[
 \Omega=\{-2,-1,0,1,2,3\}\times\{-1,0,1\}^{2}.
\]

Let E be its 52 non-old sites and let H_E be the sum of **all** installed blocks whose two endpoints lie in E. For t≥0 define the phase-pinned joint comparator

\[
 T(t)=e^{-i[(3J+4s)t+\theta]}
       [e^{-itK}W]\otimes e^{-itH_E}.                    \tag{4}
\]

Then

\[
 \boxed{\|e^{-itH}-T(t)\|
 \le d(t):=2J+2J^2t+J|t-\theta/J|+12st.}                \tag{5}
\]

H_E is the actual *isolated* environment Hamiltonian, meaning the actual E-only block sum. It is not asserted to generate the exact reduced environment dynamics while the old/E couplings remain active. Equation (5) pays those coupling effects. There is no input-dependent or fitted phase in (4).

The same bound holds for every larger finite open rectangular box containing Ω, with its own actual H_E and its own counts. The constants do not depend on that volume. Sections 2–5 prove this statement without an extensive norm bound on H_E.

## 2. Physical inventory and local caps

The displayed box has 54 qubits and 45 x, 36 y, and 36 z edges. Thus (3) has 117 compass blocks and K once: 118 positive blocks on 117 distinct edges. The maximum graph degree is six. The full-support incident norm sum is at most 4(J+s) away from the old sites, and at most

\[
 3+4(J+s)=3+4J(1+r),\qquad r=s/J,                        \tag{6}
\]

at either old site. These counts include the compass block and K separately even though they share the old edge.

Let L=(-1,0,0), R=(2,0,0), and S={L,1,2,R}. Exactly eight y and eight z edges touch S. None joins two sites of S. For each direction, four are old/E edges and four are E/E edges incident on L or R. The actual H_E contains 42 x, 32 y and 32 z blocks, or 106 blocks. Define H_E,ref by deleting only the latter four y and four z E/E blocks. It has 98 blocks, with directional counts 42,28,28. This deletion is a proof comparison, not a physical removal.

The retained terms touching L or R are all x terms. Consequently H_E,ref commutes with X_L and X_R. Its other terms need not commute among themselves. Introduce

\[
 H_4=K+J(3I-X_LX_1-X_1X_2-X_2X_R).
                                                               \tag{7}
\]

H_E,ref commutes with H₄, and the following decomposition is exact:

\[
 H=H_4+H_{E,\mathrm{ref}}+8sI+V,
 \quad V=-J_y\sum_{8\ y}YY-J_z\sum_{8\ z}ZZ,
 \quad \|V\|\le8s.                                      \tag{8}
\]

All sixteen transverse blocks are installed in H; their identity parts supply 8sI. The reference identity coefficient is

\[
 (2+3J)+(42J+28s)+8s=2+45J+36s,
\]

exactly the actual coefficient. No vacancy scalar or bond identity has been dropped.

## 3. Full-space detuning calculation

The operators X_L,X_R commute with H₄. In their eigenvalue sectors a,b=±1, further decompose by p=±1, the eigenvalue of X₁X₂. On that two-dimensional old sector set Z=Z₁Z₂ and X'=X₁. They anticommute, square to I, and X₂=pX'. Thus

\[
 H_{ab,p}=(2+3J-Jp)I+Z-d_pX',
 \qquad d_p=J(a+bp)\in\{0,2J,-2J\}.                    \tag{9}
\]

For any real d let Ω_d=√(1+d²) and N_d=(Z-dX')/Ω_d. Direct Pauli algebra gives

\[
 \|N_d-Z\|^2=2-2/\Omega_d
   =\frac{2d^2}{\Omega_d(\Omega_d+1)}\le d^2.
\]

Using the exact sine/cosine formula for each exponential,

\[
 \begin{aligned}
 \|e^{-it(Z-dX')}-e^{-it\Omega_d Z}\|
   &=|\sin(\Omega_dt)|\,\|N_d-Z\|\le |d|,\\
 \|e^{-it\Omega_d Z}-e^{-itZ}\|
   &\le(\Omega_d-1)t\le d^2t/2 \qquad(t\ge0).
 \end{aligned}                                                   \tag{10}
\]

Therefore the detuning cost is at most |d|+d²t/2. Taking the maximum over all a,b,p costs at most 2J+2J²t. Separately, the commuting XX angle mismatch obeys

\[
 \|e^{iJtX_1X_2}-e^{i\theta X_1X_2}\|
   =2|\sin[(Jt-\theta)/2]|\le J|t-\theta/J|.
\]

Combining these identities, including the scalar from (7), proves

\[
 \left\|e^{-itH_4}
 -e^{-i(3Jt+\theta)}[e^{-itK}W]\otimes I_{LR}\right\|
 \le2J+2J^2t+J|t-\theta/J|.                            \tag{11}
\]

The direct sum covers the entire sixteen-dimensional four-qubit space. In particular (11) applies to superpositions of endpoint signs and to arbitrary old/endpoint correlations. Endpoint X eigenstates are a calculation basis, not an initialization premise. The estimate is not a truncated perturbation expansion.

## 4. Restoring every transverse bond and the actual environment

Finite-dimensional Duhamel applied to (8), followed by the exact commuting factorization of H₄ and H_E,ref, gives

\[
 \begin{aligned}
 T_{\mathrm{ref}}(t)
 &=e^{-i[(3J+8s)t+\theta]}[e^{-itK}W]
           \otimes e^{-itH_{E,\mathrm{ref}}},\\
 \|e^{-itH}-T_{\mathrm{ref}}(t)\|
 &\le2J+2J^2t+J|t-\theta/J|+8st.                       \tag{12}
 \end{aligned}
\]

Now restore the eight omitted E/E blocks in the comparator. With B_E their signed Pauli sum,

\[
 H_E=H_{E,\mathrm{ref}}+4sI-B_E,\qquad
 B_E=J_y\sum_{4\ E/E\ y}YY+J_z\sum_{4\ E/E\ z}ZZ,
 \quad\|B_E\|\le4s.                                    \tag{13}
\]

There is no assumption that H_E commutes with X_L or X_R. A second Duhamel bound gives

\[
 \|e^{-it(H_{E,\mathrm{ref}}+4sI)}-e^{-itH_E}\|\le4st.
\]

The scalar transfer is exactly

\[
 e^{-i[(3J+8s)t+\theta]}e^{-itH_{E,\mathrm{ref}}}
 =e^{-i[(3J+4s)t+\theta]}
       e^{-it(H_{E,\mathrm{ref}}+4sI)}.                 \tag{14}
\]

Equations (12)–(14) prove (4)–(5). The resulting identity coefficient is again

\[
 2+(3J+4s)+(42J+32s)=2+45J+36s.
\]

Neither Duhamel step requires commuting perturbations, a special environment state, or a small norm of the full environment Hamiltonian.

## 5. Uniform extension over larger finite open boxes

Let Ω′ be any finite open rectangular box containing Ω, with side lengths nₓ,nᵧ,n_z and all its compass bonds installed. Define

\[
 \begin{aligned}
 Q&=n_xn_yn_z,\\
 M_x&=(n_x-1)n_yn_z,\quad M_y=n_x(n_y-1)n_z,\quad
 M_z=n_xn_y(n_z-1),\quad M=M_x+M_y+M_z.
 \end{aligned}                                                   \tag{15}
\]

There are Q physical qubits and M+1 positive blocks on M distinct edges. The actual environment has Q−2 qubits and M−11 blocks: removing old-incident edges removes three x, four y and four z edges. The reference environment has M−19 blocks after the additional four y and four z omissions at L/R.

S and all its immediate neighbors are already in Ω. Hence the same sixteen transverse edges, eight E/E correction edges and three four-site x bonds occur in every Ω′. All additional environment terms either act away from L/R or are retained x terms there. The commutation with H₄, both local perturbation bounds, and the incident cap (6) remain valid. In particular no bound proportional to M or to ‖H_E‖ enters (5).

For explicit scalar bookkeeping, the reference and actual environment identity coefficients are

\[
 \begin{aligned}
 C_{E,\mathrm{ref}}&=(M_x-3)J+(M_y-8)J_y+(M_z-8)J_z,\\
 C_E&=(M_x-3)J+(M_y-4)J_y+(M_z-4)J_z.
 \end{aligned}                                                   \tag{16}
\]

Adding K's scalar and the corresponding scalar in (12) or (4) recovers 2+MₓJ+MᵧJᵧ+M_zJ_z. This proves the stated finite-volume-uniform result with the actual volume's environment comparator. It removes any requirement to cut the lattice exactly at the 54-site boundary; it does not retain the counts 54 and 118 for a larger system.

No infinite-volume global phase, Hamiltonian, complete state norm, unitary or limiting dynamics is constructed here. The extensive identity coefficients in (16) are finite-volume quantities. A limiting local-observable statement would require its own formulation and proof.

## 6. Complete outputs and arbitrary initial correlations

Tensor (5) with identity on any passive reference F. For every normalized pure vector on old⊗E⊗F the full, phase-pinned vector error is at most d(t). For every joint density operator ρ, including arbitrary old/E/F correlations,

\[
 \| (U\otimes I_F)\rho(U^*\otimes I_F)
      -(T\otimes I_F)\rho(T^*\otimes I_F)\|_1\le2d(t),
 \quad U=e^{-itH}.                                     \tag{17}
\]

Indeed expand the difference as (U−T)ρU*+Tρ(U*−T*). The same bound holds for the unhalved diamond distance of the joint unitary channels. Every environment output is retained in (17); no conditioning or tracing out repairs the main estimate.

If the initial state is ρ_OF⊗σ_E with σ_E independent of the old/passive input, the target factors with the common environment output e⁻ⁱᵗᴴᴱσ_Eeⁱᵗᴴᴱ. The supplied σ_E can be mixed and internally entangled. The estimate is uniform over σ_E, but its target contains that actual evolved state, not one state shared across different σ_E choices.

For correlated inputs the target is generally correlated. The result preserves those correlations approximately under the displayed joint local unitary; it does not productize them. As an optional consequence, partial trace over E in (17) bounds the distance from (e⁻ⁱᵗᴷW⊗I_F)ρ_OF(e⁻ⁱᵗᴷW⊗I_F)* by 2d(t), since the partial trace is invariant under the environment unitary. This does not define a universal exact reduced old channel for arbitrary correlated preparation assignments.

Thus a pure product collar is only an initial special case of the original cube presentation. It is not a premise of the full-space interior or cube theorem. No cooling, reset, preparation of independence, or erasure of environment information follows.

## 7. Accuracy window, physical cap and sufficient resource policy

For 0<ε≤1 and any incident norm cap Λ>3 choose positive coefficients with

\[
 J\le\frac{\epsilon}{128(\theta+1)},\qquad
 0<r=\frac{J_y+J_z}{J}\le\frac{\epsilon}{384(\theta+1)},
 \qquad3+4J(1+r)\le\Lambda.                            \tag{18}
\]

Set

\[
 \tau=\theta/J,\qquad w=\epsilon/(32J),\qquad
 t\in[\tau-w,\tau+w].                                  \tag{19}
\]

The lower endpoint is positive. Throughout the interval, Jt≤θ+ε/32<θ+1, and the four terms of (5) obey

\[
 2J<\epsilon/64,\qquad 2J^2t<\epsilon/64,\qquad
 J|t-\tau|\le\epsilon/32,\qquad12st<\epsilon/32.
\]

Consequently d(t)<3ε/32<ε/8 uniformly on the entire interval, and the unhalved complete channel bound is <3ε/16<ε/4. All times and phases are those of the same static installed Hamiltonian. There is no timed removal of its contacts.

The constraints are simultaneous and nonempty: choose r under its ceiling and

\[
 0<J\le\min\{(\Lambda-3)/8,\epsilon/[128(\theta+1)]\},
\]

then split s=rJ into positive Jᵧ and J_z. Since r<1, this suffices for (18). At fixed Λ>3, for sufficiently small ε the saturated choice J=ε/[128(θ+1)] gives

\[
 \tau=128\theta(\theta+1)/\epsilon,\qquad
 w=4(\theta+1),\qquad w/\tau=\epsilon/(32\theta).       \tag{20}
\]

Thus this chosen family has sufficient observation time of order ε⁻¹ in the fixed old energy unit, constant absolute half-window, and relative half-width of order ε. At fixed transverse split and saturated r, Jₓ is of order ε and Jᵧ,J_z are of order ε². These are supplied coefficient ratios, not derived fabrication accuracy or preparation costs. Choosing smaller J lengthens both τ and w. Fixed positive J and r do not satisfy this sufficient policy for arbitrarily small ε; This homogeneous policy asserts no optimality; §10 separately treats independent scalar edge variations.

The minimal displayed volume always has 54 qubits and 118 positive blocks. For larger boxes the physical counts are (15), while the accuracy and cap bounds remain uniform. The old coefficient has not been rescaled away: small J is required relative to the unit ZZ coefficient of K.

## 8. Boundary cube comparison

The earlier cube is a simpler special geometry, not an assertion that interior exterior-x contacts can be omitted. On {0,1}³ with the same old edge, all twelve compass bonds are present: four per direction. Together with K once this gives eight qubits, thirteen positive blocks, twelve distinct edges and degree three. There are no old/E x edges. The six-qubit isolated environment contains three x, two y and two z blocks.

With H_E,cube that actual seven-block sum, the exact comparison split is

\[
 H_{\mathrm{cube}}=[K+J(I-X_1X_2)]+H_{E,\mathrm{cube}}+2sI+V_c,
 \quad\|V_c\|\le2s,
\]

where V_c is the signed sum of two old/E y and two old/E z Pauli bonds. The first two displayed Hamiltonians commute because they have disjoint support. The complete comparator and error are therefore

\[
 \begin{aligned}
 T_c(t)&=e^{-i[(J+2s)t+\theta]}[e^{-itK}W]
                       \otimes e^{-itH_{E,\mathrm{cube}}},\\
 \|e^{-itH_{\mathrm{cube}}}-T_c(t)\|
 &\le2st+2|\sin[(Jt-\theta)/2]|\le2st+J|t-\theta/J|.
 \end{aligned}                                                   \tag{21}
\]

The scalar is checked by 2+(J+2s)+(3J+2s)=2+4J+4s. The incident cap is 3+2J(1+r)≤Λ. For r≤ε/[32(θ+1)] and |t−θ/J|≤ε/(16J), the right side of (21) is <ε/8, with complete channel bound <ε/4. The full-space conclusions of §6 apply unchanged. Unlike the interior proof, this geometry needs no small-J detuning condition relative to K, because there are no exterior x contacts on the old sites.

## 9. Scope and evidence record

The milestone is a finite, static, real, positive, nearest-neighbor compass-family attachment with the given literal K installed once. It retains the exact W of (1), complete elapsed old aging, all environment outputs, arbitrary initial correlations in the joint comparison, calibrated observation timing, and every internal lattice bond. The proof uses a fixed old spectral splitting to control exterior x contacts and weak transverse bonds to control the remaining local comparisons.

It does not identify this family with a fully derived native microscopic model, derive K from compass couplings, preserve the original A/B-source or clock apparatus, supply coefficient calibration, or establish preparation, capture, release, reset, record writing, reuse or permanent halt. The Hamiltonian keeps acting after the observation window. The finite-volume-uniform statement is not an infinite-system statement. The exact four-site diagnostics in the frozen source are not repackaged here as a no-go result.

The following frozen sources and reviews are the mathematical evidence. Links point into the frozen publication packet. Their source text may retain historical pending-review labels; the dated sequence is resolved by the actual subsequent reviews, not by editing those sources.

| Evidence | SHA256 | Status used here |
|---|---|---|
| Interior source (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_exterior_x_contacts/NOTE.md`) | `1d27903b2dbe3041bc76f8cf52085dc59a6bf0d3463a65c377e166f82a416af8` | Frozen author derivation |
| Actual-environment addendum (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_exterior_x_contacts/ACTUAL_ENVIRONMENT_ADDENDUM.md`) | `ab9a2d00dbf10754235adad790a6ba0d6bd67fd273aab1a7a5f0ab96a273d08f` | Frozen author derivation |
| Interior distinct review (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_exterior_x_contacts_check/REVIEW.md`) | `b5bbc7a528244cd95ad4efa55b6ca4ac63584ea0dfd35e785ff1818b180b91d4` | SUPPORT, ROOT full-read acceptance; §8 derives the larger finite-box extension |
| Cube source (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_weak_transverse_attachment/PROPOSAL.md`) | `323817300ff86682cca410da69aca9e99b484474e972bab0d263c9448c1297ed` | Frozen author derivation |
| Full-space corollary (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_weak_transverse_publication_draft/COROLLARY.md`) | `4c557bf1dbfbc68378d6b600319be84ae074dd20dd39bb007649771e526c9e73` | Frozen author derivation |
| Cube and corollary review (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_weak_transverse_attachment_check/REVIEW.md`) | `4b2d7042321a21d3a55420a92b8496e076b215146da1be4353912dcd70b3dbb6` | SUPPORT, ROOT full-read acceptance |
| Raw compass definition (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_microscopic_source_snapshots/NATIVE_CONSERVED_SCALAR_NOTE_2026-10-18.md`) | `1b579ec1901f2389b4fb058649b8ea78f0d0d0c4737e36c54af1c400bf4f795e` | PR9752, head `33f0af206df4897744a9d5e248c2889fdd6ed1e7`; definition only |
| Finite-open convention (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_microscopic_source_snapshots/NATIVE_LOCAL_NORMALFORM_NOTE_2026-10-18.md`) | `debd8448a97a982d23074582e983438cebc880a86cb03f44bfe9be57921d4d3d` | PR9747, head `e161fcef330a7cad87a19e3ffcb2fc3b03691083`; no normal-form theorem imported |

The [direct benchmark](LITERAL_DIRECT_GENERATOR_BOUNDED_THEOREM_NOTE_2026-10-18.md), canonical SHA256 `1ba5a1d12cc728172144cd0c2b0f563523f009770f11cbe12db09fecef182bbc`, records the exact K/W convention. Its underlying evidence is `literal_direct_generator/PROPOSAL.md`, SHA `c0cc65e615bb6bdb7466c01c68ce53d6647c75e73a322bd88fff97580428f7d6`, and its review, SHA `e58d3fd82b27d94ae862a528707e3eb279ad5964dd5ca4641fb0e7e4fbfe3e38`. Equation (1) is reproduced explicitly rather than importing a benchmark performance statement.

The manuscript writer fully read the cube source, corollary, cube review, interior source, actual-environment addendum, interior review and the two microscopic snapshot bodies; unchanged readings were reused at the listed identities. ROOT proposed the attachment designs, arbitrary-environment strengthening, actual-environment comparison and larger-box question. The reviewers had disclosed shared campaign ancestry and design exposure; their checks were distinct from the corresponding author derivations, same-model and not blind. This editorial integration adds no independent evidentiary weight.

All earlier cube drafts, the initial review-pending manuscript, corollary, and pending interior appendix are preserved. The author draft is preserved unchanged in the packet. Sections1–9 retain the author argument with provenance and link updates; §10 adds the separately checked independent-edge extension. The integration record identifies both steps. This publication applies no retained-audit disposition and changes no editable prompt.

## 10. Independent edge coefficients and a nominal observation time

Exact lattice homogeneity is unnecessary for a corresponding local estimate. Assign every installed directional edge its own positive coefficient j_e, keeping its exact Pauli matrix form. Let J_0 be the old x-bond coefficient and J_L,J_R the two adjacent exterior x coefficients. Put g=J_L+J_R. Let b be the sum of coefficients of the eight old/E transverse edges and c the sum of the eight E/E transverse edges incident on L,R. All other coefficients may vary independently, subject to their physical incident caps.

With the actual E-only Hamiltonian H_E, the full-space estimate is

\[
\begin{aligned}
T_j(t)&=e^{-i[(J_L+J_0+J_R+b)t+\theta]}
 [e^{-itK}W]\otimes e^{-itH_E},\\
\|e^{-itH}-T_j(t)\|&\le g+\tfrac12g^2t+|J_0t-\theta|+(b+2c)t.
\end{aligned}                                                    \tag{22}
\]

To verify it, replace (7) by

\[
H_4=K+(J_L+J_0+J_R)I-J_LX_LX_1-J_0X_1X_2-J_RX_2X_R.
\]

In endpoint signs a,d and old XX sign p, the detuning in (9) becomes q=J_La+J_Rdp, hence |q|≤g. Equation (10) bounds its cost by g+g²t/2. Delete the same eight E/E transverse edges only in H_E,ref. Its retained endpoint contacts still commute with X_L,X_R, regardless of their coefficients. The exact physical decomposition has scalar b+c and signed perturbation norm at most b+c; restoring the actual environment transfers scalar c and costs at most ct. This proves (22), including its phase. Remote environment terms remain unchanged in both evolutions and incur no extensive error penalty.

For an explicit sufficient policy with 0<ε≤1, choose a nominal J>0 and

\[
\begin{gathered}
J_0\in[J(1-\eta),J(1+\eta)],\quad 0<J_L,J_R\le2J,\\
J\le\frac{\epsilon}{512(\theta+1)},\quad
0\le\eta\le\frac{\epsilon}{64(\theta+1)},\quad
b+2c\le\frac{\epsilon J}{64(\theta+1)},\\
|t-\theta/J|\le\frac{\epsilon}{64J}.
\end{gathered}                                                    \tag{23}
\]

Since Jt<θ+1, the four terms in (22) are respectively <ε/128, <ε/64, <ε/32, and <ε/64. For the third term use
|J_0t−θ|≤J|t−θ/J|+ηJt. Thus the vector bound is <9ε/128<ε/8, and the unhalved complete channel bound is <9ε/64<ε/4. The interval center uses the nominal J, rather than fitting the actual J_0.

The old incident cap is at most 3+2[J_0+max(J_L,J_R)+b]<3+8J. Impose also J≤(Λ−3)/8 for Λ>3. All non-old incident caps must be enforced separately. A simultaneous nonempty coefficient box is obtained by choosing every remaining x coefficient in (0,J] and every transverse coefficient in (0,εJ/[1536(θ+1)]]. Then b+2c has 24 weighted coefficient slots, so its bound in (23) holds; the non-old loads are <8J. Larger remote coefficients are permitted by (22) when their local hardware caps hold. No uniform smallness of all remote transverse coefficients is required by that theorem.

The common phase in (22) uses the actual coefficients. It is not a guarantee relative to an unknown nominal apparatus phase. The inventory, all-output comparison and finite-volume qualifications of §§2,5,6 remain unchanged. This result covers independent positive edge weights within the exact directional Pauli family, not arbitrary matrix errors, errors in K, graph changes, or a native mechanism supplying calibrated coefficients. It still gives an observation window, not a release or halt.

The inhomogeneous source (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_inhomogeneous_attachment/PROPOSAL.md`) and its distinct check (`outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_inhomogeneous_attachment_check/REVIEW.md`) are frozen in the publication manifest. ROOT authored this extension; the checker reconstructed it with source exposure and shared campaign ancestry. Editorial integration is not an additional independent check.

## Finite execution boundary

The primary retains all sectors of its declared small matrices, the scalar phases and complete outputs, and checks explicit sufficient coefficient/count budgets. It does not dynamically execute the proof texts. Uniform-in-volume estimates follow from the displayed arguments under their hypotheses; finite controls alone do not establish them. Infinite-lead scattering is not a finite product-seed launcher, and none of these controls supplies capture, reset or permanent halt.
