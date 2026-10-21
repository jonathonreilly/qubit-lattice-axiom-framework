> Historical exposition/integration record. Mathematical arguments remain inspectable; historical status and execution assertions are not fresh evidence. Exact original recovery: `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`.

## 10. An exactly calibrated mediator with no old-only counterterm

**Status: conditional theorem supported by the distinct check, with no required correction, and accepted by ROOT at its stated supplier scope.** This section presents the frozen exact-spectrum source and check identified in §10.9. It uses a different mediator coupling from the preceding second-order construction. Its conclusion follows from the chain spectrum, eigenprojector estimates and polar dressing proved below, not from extending a finite-order remainder estimate to arbitrary times.

Five supplied real positive blocks on five qubits approximate a specified complete joint evolution with error at most \(41\lambda\), uniformly for every real time. The installed old-only block sum is exactly the literal \(K=2I+Z_1Z_2\). There is no old-only counterterm and no initial mediator-state restriction. The price is an exact functional calibration, a positive mediator gap, a specified effective interaction strength and effective mediator aging. All outputs and phases are retained. This joint Hamiltonian simulation does not by itself supply a common-output W clock or halt.

### 10.1. Physical blocks, exact coefficients and caps

Use old sites \(1=(0,0,0)\), \(2=(1,0,0)\), ancillas \(a=(0,1,0)\), \(b=(1,1,0)\), and mediator \(m=(0,0,1)\). Distinguish the labels a,b from the scalar energies \(a_{\rm eff},b_{\rm eff}\). Set
\[
 \begin{gathered}
 Z=Z_1Z_2,\quad K=2I+Z,\quad
 Q=X_1X_2Y_aY_b,\quad Z_m=I-2n_m,\\
 \ell=\lambda^2,\qquad 0<\lambda\le10^{-3},\qquad
 x=\frac{3\ell(2-\ell)}{1-\ell},\qquad
 g=\sqrt{x},\qquad c=2\lambda+g,\\
 A_0=4+2\ell+x,\qquad
 a_{\rm eff}=\frac{\sqrt{A_0+4\ell}+\sqrt{A_0-4\ell}}2,\qquad
 b_{\rm eff}=\frac{\sqrt{A_0+4\ell}-\sqrt{A_0-4\ell}}2 .
 \end{gathered}
 \tag{EM1}
\]
The actual installed Hamiltonian is
\[
 H=K+\lambda(I+Y_1Y_a)+\lambda(I+Y_2Y_b)
                   +4n_m+g(I+X_1X_m).
 \tag{EM2}
\]
There are four nearest-neighbor pair blocks on four distinct edges and one onsite gap block. The maximum geometric degree is three. All five blocks are real and positive on their full supports, with norms \(3,2\lambda,2\lambda,4,2g\), respectively. No other bond or counterterm is installed. The incident norm sums are
\[
 L_1=3+2\lambda+2g,\quad L_2=3+2\lambda,\quad
 L_a=L_b=2\lambda,\quad L_m=4+2g.
 \tag{EM3}
\]
Every load must satisfy the chosen cap. Since \(x\le7\lambda^2\), a sufficient explicit prescription for any \(\Lambda>4\) is
\[
 \lambda\le\min\left\{10^{-3},
       \frac{\Lambda-3}{2(1+\sqrt7)},
       \frac{\Lambda-4}{2\sqrt7}\right\}.
 \tag{EM4}
\]
The unit coefficient of Z in the given K fixes the energy and time units. The gap 4 and the exact nonlinear g in (EM1) remain suppliers. In particular, \(g\ne\sqrt6\,\lambda\) for positive \(\lambda\). The effective coefficient \(b_{\rm eff}\) also differs from \(\lambda^2\). Neither replacement is permitted in this all-time theorem merely because the differences vanish as \(\lambda\to0\). No immunity to coefficient mistuning or physical calibration mechanism is established.

### 10.2. Conserved sectors and the actual four-state chains

Let \(T_1=Y_1Y_a\), \(T_2=Y_2Y_b\), \(M=X_1X_m\). Then
\[
 H=(4+c)I+A,\qquad
 A=Z-2Z_m+\lambda(T_1+T_2)+gM,\qquad
 R=ZQZ_m .
 \tag{EM5}
\]
R is a selfadjoint involution commuting with A. Each YY term anticommutes with Z and Q and commutes with \(Z_m\). M anticommutes with Z and \(Z_m\) and commutes with Q. The double sign changes therefore preserve R. The YY square is
\[
 [\lambda(T_1+T_2)]^2
       =2\ell(I-ZQ)=2\ell(I-RZ_m).
 \tag{EM6}
\]
Fix \(R=r\). Each simultaneous vertex labeled by \((Z,Z_m)\) has dimension four: fixing old parity leaves dimension two on the old pair, the two ancillas supply dimension four, and fixing \(Q=rZZ_m\) halves their combined space. The mediator occupation is fixed at the vertex. Thus each r sector has dimension sixteen and the two sectors exhaust the full thirty-two-dimensional space.

For \(r=+1\), the YY coupling vanishes when \(Z_m=+1\) and equals \(2\lambda\) times an involution on its active \(Z_m=-1\) subspace. M flips both vertex labels. The nonzero connections form the path
\[
(-,+)\ \longleftrightarrow\ (+,-)\ \longleftrightarrow\ (-,-)\ \longleftrightarrow\ (+,+),
 \tag{EM7}
\]
with diagonal entries \((-3,3,1,-1)\) and edge magnitudes \((g,2\lambda,g)\). Every normalized edge map is an isometry onto the adjacent vertex, because M is an involution and (EM6) makes the normalized active YY map an involution. Choose a real orthonormal basis at one endpoint and propagate it along the path. There is no cycle whose consistency could impose an extra condition. This removes the edge matrices and proves that \(A|_{R=+1}\) is equivalent to four copies of
\[
 C_+=
 \begin{pmatrix}
 -3&g&0&0\\
 g&3&2\lambda&0\\
 0&2\lambda&1&g\\
 0&0&g&-1
 \end{pmatrix}.
 \tag{EM8}
\]
For \(r=-1\), a path ordering has diagonal \((3,-3,-1,1)\) and the same edge magnitudes. Alternating signs along the path reverses every edge sign, so this matrix is orthogonally similar to \(-C_+\). This reduction counts the complete multiplicities and retains every internal fiber.

### 10.3. Exact characteristic matching

The path invariants of \(C_+\) are
\[
 \operatorname{tr}C_+=0,\quad
 \operatorname{tr}C_+^2=20+8\ell+4x,\quad
 \operatorname{tr}C_+^3=48\ell,\quad
 \det C_+=9+10x+x^2-12\ell .
 \tag{EM9}
\]
For the third trace, the diagonal cubes sum to zero; the remaining contribution is three times the sum over edges of their squared weight times the sum of their endpoint diagonals. Only the middle edge contributes, giving \(3(4\ell)(3+1)=48\ell\). The leading principal determinants are \(-3\), \(-9-x\), \(-9-x+12\ell\), then the determinant displayed in (EM9).

Consider the commuting comparison operator
\[
 A_{\rm eff}=Z-a_{\rm eff}Z_m-b_{\rm eff}Q .
 \tag{EM10}
\]
Within \(r=+1\), \(Q=ZZ_m\), so its four eigenvalues in the path order (EM7) are
\[
 -1-a_{\rm eff}+b_{\rm eff},\quad
 1+a_{\rm eff}+b_{\rm eff},\quad
 -1+a_{\rm eff}-b_{\rm eff},\quad
 1-a_{\rm eff}-b_{\rm eff}.
 \tag{EM11}
\]
They sum to zero, and their other three invariants are
\[
 \begin{aligned}
 \operatorname{tr}A_{\rm eff}^2
       &=4(1+a_{\rm eff}^2+b_{\rm eff}^2),\\
 \operatorname{tr}A_{\rm eff}^3&=24a_{\rm eff}b_{\rm eff},\\
 \det A_{\rm eff}
       &=(a_{\rm eff}^2+b_{\rm eff}^2-1)^2
                      -4a_{\rm eff}^2b_{\rm eff}^2 .
 \end{aligned}
 \tag{EM12}
\]
These traces and determinant refer to one four-state copy. Definition (EM1) gives
\[
 a_{\rm eff}^2+b_{\rm eff}^2=A_0,\qquad
 a_{\rm eff}b_{\rm eff}=2\ell.
 \tag{EM13}
\]
The second and third traces therefore match (EM9). The determinant difference reduces to
\[
 24\ell-4x-12\ell^2+4\ell x=0,
 \tag{EM14}
\]
which is exactly the prescribed \(x=3\ell(2-\ell)/(1-\ell)\).
For a trace-zero four-by-four matrix, the characteristic polynomial is
\[
 z^4-\tfrac12(\operatorname{tr}C^2)z^2
       -\tfrac13(\operatorname{tr}C^3)z+\det C.
 \tag{EM15}
\]
Thus the two four-state characteristic polynomials agree. In the \(r=-1\) sector the map \((Z,Z_m)\mapsto(-Z,-Z_m)\) also reverses Q, and reverses the comparison spectrum. Together with the preceding path reduction, this proves matching in both sectors with all multiplicities. Isospectrality alone is not yet a small dynamical error; the matching of eigenvalue labels and projectors is the next step.

### 10.4. Riesz projectors and a uniform all-time bound

For \(0<\ell\le10^{-6}\), \(x\le7\ell\). Initially (EM1) gives \(a_{\rm eff}\ge\sqrt{A_0/2}\ge\sqrt2\) and \(b_{\rm eff}=2\ell/a_{\rm eff}\le\sqrt2\,\ell\). Inserting the latter bound into (EM13) yields
\[
 a_{\rm eff}\ge2,\qquad
 0<b_{\rm eff}\le\ell,\qquad
 0\le a_{\rm eff}-2\le\frac{9\ell}{4}.
 \tag{EM16}
\]
Indeed \(a_{\rm eff}^2\ge4+2\ell+x-2\ell^2\ge4\), while \(a_{\rm eff}^2\le A_0\le4+9\ell\); divide \(a_{\rm eff}^2-4\) by \(a_{\rm eff}+2\).

The four bare energies of \(A_{\rm bare}=Z-2Z_m\) in each r sector are \(-3,-1,1,3\). Each corresponding comparison eigenvalue differs by at most \(13\ell/4<1/2\). The comparison's spectral projectors are therefore exactly the four bare vertex projectors \(P_j^0\), with unambiguous distinct labels.

The actual perturbation of \(A_{\rm bare}\) has norm
\[
 E:=\|\lambda(T_1+T_2)+gM\|
       \le2\lambda+g\le(2+\sqrt7)\lambda<5\lambda.
 \tag{EM17}
\]
The actual eigenvalues likewise lie within E of the bare spectrum, as follows from the selfadjoint resolvent bound. These neighborhoods are disjoint. Combined with exact spectral matching, they identify the actual and target eigenvalues by the same bare labels rather than by an arbitrary permutation.

In either r sector, use the radius-\(1/2\) circle \(\Gamma_j\) about the j-th bare eigenvalue. On it, the bare resolvent norm is at most 2, and the actual resolvent norm is at most \(1/(1/2-E)\) by the Neumann series. The Riesz formula and resolvent identity give
\[
 \begin{aligned}
 P_j-P_j^0
 &=\frac1{2\pi i}\oint_{\Gamma_j}
     \big[(z-A)^{-1}-(z-A_{\rm bare})^{-1}\big]\,dz,\\
 \|P_j-P_j^0\|
 &\le\frac{E}{1/2-E}.
 \end{aligned}
 \tag{EM18}
\]
The circle's length is \(\pi\); its factor \(1/2\) after division by \(2\pi\) cancels the factor 2 from the bare resolvent. These are rank-four projectors, not simple eigenvectors.

Their matching eigenvalues have identical evolution phases for every real t. Hence the four-projector sum in each sector, followed by the direct sum over r, gives
\[
 \|e^{-itA}-e^{-itA_{\rm eff}}\|
 \le\frac{4E}{1/2-E}
 \le41\lambda
 \qquad(t\in\mathbb R).
 \tag{EM19}
\]
The numerical ceiling uses \(E<5\lambda\) and
\(20/(1/2-0.005)<41\).
No time-dependent eigenvalue remainder remains; the two sectors do not introduce another factor of two in the operator norm.

### 10.5. Complete target, effective aging and resource policy

Set
\[
 c_{\rm eff}=c+2-a_{\rm eff}.
 \tag{EM20}
\]
The exact comparison generator identity is
\[
 (4+c)I+A_{\rm eff}
   =c_{\rm eff}I+K-b_{\rm eff}Q+2a_{\rm eff}n_m.
 \tag{EM21}
\]
Equations (EM5) and (EM19) prove the complete bound
\[
 \boxed{\left\|e^{-itH}
   -e^{-ic_{\rm eff}t}
       \left[e^{-it(K-b_{\rm eff}Q)}
          \otimes e^{-it\,2a_{\rm eff}n_m}\right]\right\|
       \le\min\{2,41\lambda\}
       \quad\text{for every }t\in\mathbb R.}
 \tag{EM22}
\]
The tensor product separates old-plus-\(a,b\) from m. Arbitrary passive identities may be appended. The common scalar occurs once, with K's \(2I\) retained inside the old-plus-ancillary exponential. Mixed joint outputs and the unhalved complete channel distance have upper bound \(\min\{2,82\lambda\}\).

No mediator vacancy, purity, basis choice or independence is required for the joint operator comparison. An initially independent mediator has the common evolved output obtained by applying \(e^{-it\,2a_{\rm eff}n_m}\) to its actual input. For initially correlated inputs, the displayed product unitary acts on those same correlations; it does not make the output a product state or reset the mediator.

The installed isolated mediator Hamiltonian is \(4n_m\), whereas its comparison aging is \(2a_{\rm eff}n_m\). Substituting bare aging changes the phase on mediator occupation one by \(e^{-2i(a_{\rm eff}-2)t}\). That phase can become order one at long times. It is retained in (EM22), not absorbed into an input-dependent or freely adjustable common phase.

For \(0<\epsilon\le1\), impose the physical cap (EM3) and \(\lambda\le\min\{10^{-3},\epsilon/41\}\). Then the complete vector error is at most \(\epsilon\) for all t, and the channel upper bound is \(\min\{2,2\epsilon\}\). At a specified positive mediated angle \(\varphi\), use the actual time
\[
 T=\frac{\varphi}{b_{\rm eff}}
   =\frac{\varphi a_{\rm eff}}{2\lambda^2}.
 \tag{EM23}
\]
The target is \(e^{-ic_{\rm eff}T}e^{-iTK}e^{i\varphi Q}\) on old-plus-ancillary space, together with the full mediator factor. By (EM16),
\[
 \frac{\varphi}{\lambda^2}\le T
   \le\frac{\varphi}{\lambda^2}
                       \left(1+\frac{9\lambda^2}{8}\right).
 \tag{EM24}
\]
Thus the supplied small-coupling family has the stated inverse-square mediated timescale. This is a sufficient resource statement, not an optimal runtime or a necessary precision bound. Neither the actual g nor the target \(b_{\rm eff}\) is replaced by its leading asymptotic value in the complete theorem.

### 10.6. Exact polar dressing and weak backgrounds

The same projectors supply an exact dressing. Within each r sector define
\[
 \mathcal S=\sum_jP_jP_j^0,\qquad
 d=41\lambda<1.
 \tag{EM25}
\]
Because \(\mathcal S-I=\sum_j(P_j-P_j^0)P_j^0\), (EM18) gives \(\|\mathcal S-I\|\le d\). Thus \(\mathcal S\) is invertible. Orthogonality of the spectral families gives
\[
 \mathcal S P_j^0=P_j\mathcal S,\qquad
 [\mathcal S^\dagger\mathcal S,P_j^0]=0.
 \tag{EM26}
\]
Its polar factor
\[
 U=\mathcal S(\mathcal S^\dagger\mathcal S)^{-1/2}
 \tag{EM27}
\]
is unitary and intertwines \(P_j^0\) with \(P_j\). Every singular value of \(\mathcal S\) lies in \([1-d,1+d]\), so
\[
 \|U-\mathcal S\|\le d,\qquad
 \|U-I\|\le2d\le82\lambda.
 \tag{EM28}
\]
For the first inequality, write \(\mathcal S=U|\mathcal S|\) and use \(\||\mathcal S|-I\|\le d\). Taking the direct sum over r and using the exactly matching eigenvalues proves
\[
 H=c_{\rm eff}I+UH_{\rm eff}^{(5)}U^\dagger,\qquad
 H_{\rm eff}^{(5)}=K-b_{\rm eff}Q+2a_{\rm eff}n_m.
 \tag{EM29}
\]
All involved projectors are real. Their products and the positive inverse square root may be taken real, making U real orthogonal. U is an analytical transformation, not an installed gate.

Now add any bounded selfadjoint B on the gadget and any declared finite additional system, extending U by identity there. Let \(B'=U^\dagger BU\). The subtraction
\(B'-B=U^\dagger B(U-I)+(U^\dagger-I)B\)
gives
\[
 \|B'-B\|\le2\|U-I\|\,\|B\|.
 \tag{EM30}
\]
The exact conjugation sends \(H+B\) to \(c_{\rm eff}I+H_{\rm eff}^{(5)}+B'\). Paying for both outside U factors and applying Duhamel to \(B'-B\) yields
\[
 \boxed{\|e^{-it(H+B)}
       -e^{-ic_{\rm eff}t}e^{-it(H_{\rm eff}^{(5)}+B)}\|
       \le\min\{2,164\lambda(1+|t|\|B\|)\}.}
 \tag{EM31}
\]
This full-space statement covers arbitrary initial correlations. It is not an exact norm formula and is weaker than (EM22) at \(B=0\). No factorization of the comparison exponential is assumed for general B.

If \(B=b_{\rm eff}B_0\), \(\|B_0\|\le C_B\), and \(|t|\le A/b_{\rm eff}\), the right side is at most \(164\lambda(1+A C_B)\). Choosing
\[
 \lambda\le\frac{\epsilon}{164(1+A C_B)}
 \tag{EM32}
\]
together with the smallness and actual hardware caps gives vector tolerance \(\epsilon\) on this horizon. This weak-background conclusion has a finite prescribed horizon; the base all-time constant does not remove its background charge. If \(B_0\) depends on coupling or volume, its actual uniform norm bound must be supplied.

When \(B_0\) acts trivially on m, the comparison in (EM31) factors exactly into \(e^{-it\,2a_{\rm eff}n_m}\) and
\[
 e^{-ic_{\rm eff}t}
     e^{-it[K+b_{\rm eff}(B_0-Q)]}.
 \tag{EM33}
\]
B may mix old or ancillary states and need not commute with K. In that case the last exponential is not split into separate old and background evolutions.

### 10.7. Physical background inventory and the clock limitation

Bounded selfadjointness alone does not make a physical background real, positive or local. To retain the hardware class, separately supply \(B_0=\sum_\nu b_\nu\) with each \(b_\nu\) positive and real on an allowed nearest-neighbor support of at most two qubits. The device then has five base blocks plus the listed extra blocks, including any additional sites. Every site gains load
\[
 b_{\rm eff}\sum_{\nu:\,v\in\operatorname{supp}b_\nu}\|b_\nu\|.
 \tag{EM34}
\]
Use the full block norms and actual geometries. One sufficient global bound is \(C_B=\sum_\nu\|b_\nu\|\); an expanding collection of locally bounded terms does not imply volume-independent \(C_B\).

For a real symmetric matrix C on the adjacent ancillary pair a,b, define \(d_0=\max\{0,-\lambda_{\min}(C)\}\). The additional block \(b_{\rm eff}(C+d_0I)\) is positive, real and nearest-neighbor. It produces a five-qubit, six-block device, charging \(b_{\rm eff}\|C+d_0I\|\) at both a and b. Use \(C_B=\|C+d_0I\|\) in (EM31)–(EM32). The target scalar becomes \(c_{\rm eff}+b_{\rm eff}d_0\), while its old-plus-ancillary generator is \(K+b_{\rm eff}(C-Q)\), with the full mediator factor still present. Here K commutes with \(C-Q\), so elapsed old aging can be factored exactly in the comparison.

This provides a conditional background interface, not a solution of the clock's common-output equations. Even without C, an ancillary \(|00\rangle_{ab}\) seed has effective output
\[
 e^{i\varphi Q}(\xi\otimes|00\rangle_{ab})
   =\cos\varphi\,\xi\otimes|00\rangle_{ab}
       -i\sin\varphi\,X_1X_2\xi\otimes|11\rangle_{ab}.
 \tag{EM35}
\]
At the literal W angle and \(\xi=|00\rangle_{12}\), this target has two nonzero Schmidt coefficients \(3/5,4/5\). The mediator's independent comparison factor does not remove that old/ancillary entanglement. The statements in this section alone do not select a C solving the common-output equations, supply ancillary preparation, or establish capture, reset, reuse or permanent halt.

### 10.8. What is preserved and what remains supplied

Unlike the four-qubit counterterm construction, the actual old-only block sum in this device is exactly K. Unlike the selected-input second-order statement, the complete operator theorem (EM22) covers arbitrary mediator states. These changes follow from the new exact coefficient prescription and the explicit full-spectrum proof. They do not identify this new apparatus with the original source/contact inventory or derive it from a native microscopic Hamiltonian.

Every listed coefficient, block sign, missing coupling and energy scale remains a supplier. The effective mediator profile is not bare aging or a reset. Correlated input states retain their correlations under the comparison unitary. Exact spectral matching does not justify multiple-gadget assembly, arbitrary untuned coefficient errors or a background whose norm and physical inventory have not been charged.

All-time simulation tracks a nontrivially evolving target. It does not mean the device has finished a logical operation permanently, and does not convert a dynamical comparison into a preparation theorem. The earlier finite-order bounds and their selected-mediator assumptions remain valid for their own frozen Hamiltonian, but are not premises for the exact calibration in this section.

### 10.9. Exact source, history and exposure

The new source is [counterterm_free_gap_mediation/EXACT_ALL_TIME.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/EXACT_ALL_TIME.md), **11261 bytes, 160 lines**, SHA256 `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`. Its complete chain, invariant, projector and dressing argument was read and reconstructed for this exposition.

The distinct [EXACT_ALL_TIME_REVIEW.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/EXACT_ALL_TIME_REVIEW.md), **13928 bytes, 155 lines**, SHA256 `80c09db471dea4542ccfe9b236b91ccd2cd285502ce4b091d59cbcfbfa7e1e70`, gives SUPPORT with no required correction and was fully read by the manuscript writer and ROOT. Its source-exposed, same-model and shared-design limits are explicit. Historical pending-status text in the author source is preserved; current scoped support is provided by this actual check.

The following accepted source/check pairs are historical context, with exact unchanged pins. Their finite-order error constants do not justify (EM22) or (EM31).

| Historical argument | Source SHA256 | Distinct check SHA256 |
|---|---|---|
| [Selected mediator](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/PROPOSAL.md) / [check](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/REVIEW.md) | `739a1961076d52b0e26364bd858f957a89a233bfa72aa652efa193ef54ac2cdd` | `801093a81940a4649a4062a4e5af96bb67734a806b4e56d086d6dadaeb2217c2` |
| [Full mediator space](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/ALL_MEDIATOR_INPUTS.md) / [check](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/ALL_MEDIATOR_INPUTS_REVIEW.md) | `206d91616f9b66da958c73caf2b723733fe850fa03ca7b16b83fd78e955290e9` | `0fbd9c739d0896429f093dee5fe5c897453a7680c1a357da25bf82fe2f0d68cc` |
| [Bounded background](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/BACKGROUND.md) / [check](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation_check/BACKGROUND_REVIEW.md) | `20e79f3fdb1243975efb2165301940eef886d3e75f333ab1f137806c1f3f4c35` | `346d95c179ff2ffc08d134d5374656c602adcd267448fafc27d8ea83f046288e` |

ROOT proposed the characteristic-invariant matching, projector estimate and polar-dressing route. The author and checker disclosed shared design exposure. The present writer read the new exact source, its distinct check and all six historical bodies completely, with shared campaign exposure, and is supplying synthesis rather than a blind or additional independent check. Nothing here asserts retained audit status or a native identification.

Only `APPENDIX_EXACT_MEDIATOR.md` was written for this drafting step. The main `NOTE.md` remains frozen at SHA256 `b0455d70ab5d8e2be293590b14c4d69ab993c4a9dba4fbe4f618b2065eb876bd`. The selected-input historical appendix remains unchanged at SHA256 `f6d4ad5ad5df91797e642d2a874dbd421be62db69de4aad53284f549ed0489b4`, including its historical pending-status text. No scientific executable, numerical simulation, external search, Git/canonical/checkpoint/prompt/axiom edit, delegation, model/effort override or publication was performed. Source links identify proposed packet destinations; ROOT owns the final provenance and integration decisions.
