> Historical exposition/integration record. Mathematical arguments remain inspectable; historical status and execution assertions are not fresh evidence. Exact original recovery: `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`.

# Counterterm-free selected-mediator simulation on a finite horizon

**Proof status: proposed conditional theorem; distinct check pending.** This appendix presents the frozen five-qubit argument identified in §7. It does not modify the separately frozen exact-counterterm manuscript or infer acceptance from that earlier result. The new estimate has an explicit time-dependent remainder.

The actual old-only block sum is exactly the given \(K=2I+Z_1Z_2\): no old-only counterterm is added. A fifth qubit, initially supplied in \(|0\rangle\), instead provides a compensating virtual shift. The costs are a positive mediator gap, a calibrated extra coupling, selected mediator preparation and a finite-horizon error budget. The two other ancillary qubits may have arbitrary states and correlations with the old system. Every output, including the mediator, is retained.

## 1. Actual device and resources

Use old sites \(1=(0,0,0)\), \(2=(1,0,0)\), ancillary sites \(a=(0,1,0)\), \(b=(1,1,0)\), and mediator \(m=(0,0,1)\). Write
\[
 Z=Z_1Z_2,\qquad Q=X_1X_2Y_aY_b,\qquad
 n_m=|1\rangle\langle1|_m,\qquad
 g=\sqrt6\,\lambda,\qquad 0<\lambda\le10^{-3}.
 \tag{CF1}
\]
Install precisely
\[
 H=K+\lambda(I+Y_1Y_a)+\lambda(I+Y_2Y_b)
          +4n_m+g(I+X_1X_m).
 \tag{CF2}
\]
The four pair blocks occupy four distinct nearest-neighbor edges, and \(4n_m\) is an onsite block. Thus the device has five qubits, five positive blocks, and maximum geometric degree three. All matrices are real and positive on their full supports. Their respective norms are \(3,2\lambda,2\lambda,4,2g\). No unlisted coupling is installed.

The full-support incident norm sums are
\[
 \begin{array}{c|c}
 \text{site}&\text{incident load}\\ \hline
 1&3+2(1+\sqrt6)\lambda\\
 2&3+2\lambda\\
 a,b&2\lambda\\
 m&4+2\sqrt6\,\lambda .
 \end{array}
 \tag{CF3}
\]
For a supplied cap \(\Lambda>4\), it suffices to impose
\[
 \lambda\le\lambda_{\rm cap}^{(5)}
 :=\min\left\{
   \frac{\Lambda-3}{2(1+\sqrt6)},
   \frac{\Lambda-4}{2\sqrt6}\right\}.
 \tag{CF4}
\]
The unit coefficient of Z in K fixes the energy and time units. The gap 4 and relation \(g=\sqrt6\,\lambda\) are actual supplied coefficients in those units. They are not obtained by rescaling time, removing an old term or assuming an uncharged calibration. The gap block does not establish a procedure that prepares the coupled device in the selected mediator input.

## 2. Complete selected-input theorem and policy

Let \(J_0\) append \(|0\rangle_m\) to the full old-plus-\(a,b\) input, with any passive reference carried by an identity. Thus the mediator is initially independent and fixed; the other inputs may be arbitrarily correlated. Define
\[
 H_{\rm eff}=K-\lambda^2Q,\qquad
 c_*=2\lambda+g-2\lambda^2 .
 \tag{CF5}
\]
The proposed bound, for every real t, is
\[
 \boxed{\left\|e^{-itH}J_0-e^{-ic_*t}J_0e^{-itH_{\rm eff}}\right\|
 \le \min\{2,\ 62\lambda+10^6|t|\lambda^3\}.}
 \tag{CF6}
\]
This is an operator norm between two isometries on the entire selected input space. It includes the actual final mediator; no projection or postselection is performed. In particular, leakage and correlations involving m are charged in the same complete norm. The ideal mediator is again \(|0\rangle\), while the actual mediator is only controlled approximately by (CF6).

For \(0<\epsilon\le1\), a prescribed \(A\ge0\), and
\[
 0<\lambda\le
 \min\left\{10^{-3},\lambda_{\rm cap}^{(5)},
             \frac{\epsilon}{62+10^6A}\right\},
 \tag{CF7}
\]
the complete vector error is at most \(\epsilon\) throughout \(|t|\le A/\lambda^2\). The two channels that append the mediator and perform the actual or ideal evolution have unhalved diamond distance at most \(\min\{2,2\epsilon\}\) on this horizon. This follows from the standard two-term expansion of their output density operators and is preserved after tensoring any passive identity.

Although (CF6) is an inequality for every t, it is not a uniform small-error theorem over all times. Its useful accuracy statement is the explicitly budgeted finite horizon (CF7). The comparison target varies with t; this horizon is not a dwell interval for a fixed old-only W operation.

## 3. Two finite-dimensional conjugations with a paid remainder

Strip only the exact positive-block scalar \(c=2\lambda+g\):
\[
 H-cI=H_0+\lambda V,\qquad
 H_0=K+4n_m,\qquad
 V=Y_1Y_a+Y_2Y_b+\sqrt6\,X_1X_m.
 \tag{CF8}
\]
The four distinct eigenvalues of \(H_0\) are \(1,3,5,7\), each with an eight-dimensional fiber on the five-qubit space. Let \(P_j\) be the corresponding spectral projectors and \(E_j\) their energies. Then
\[
 \|H_0\|=7,\qquad \|V\|\le2+\sqrt6<5,\qquad
 P_jVP_j=0.
 \tag{CF9}
\]
Indeed, both YY terms flip old Z while leaving m fixed. The XX term flips old Z and m. None connects equal \(H_0\) energies, including within the degenerate fibers.

Define
\[
 S=\sum_{j\ne k}\frac{P_jVP_k}{E_j-E_k}.
 \tag{CF10}
\]
Since \(H_0,V\) are real symmetric, S is real antisymmetric and hence anti-Hermitian. Directly,
\[
 [S,H_0]=-V,\qquad
 \|S\|\le6\|V\|<30.
 \tag{CF11}
\]
The norm estimate sums the twelve ordered off-diagonal blocks and uses every energy denominator's magnitude at least two. It does not require an unstated sharp block-matrix estimate.

Expanding the finite-dimensional conjugation and using (CF11),
\[
 e^{\lambda S}(H_0+\lambda V)e^{-\lambda S}
 =H_0+\lambda^2W_2+R_3,\qquad
 W_2=\tfrac12[S,V],\qquad \|W_2\|\le150 .
 \tag{CF12}
\]
The linear term cancels, and the sign and factor of \(W_2\) follow from
\(\tfrac12[S,[S,H_0]]+[S,V]=\tfrac12[S,V]\).
For any bounded operator C, \(\|\operatorname{ad}_S^k C\|\le(2\|S\|)^k\|C\|\). Applying
\(\sum_{k\ge r}x^k/k!\le x^re^x/r!\) separately to the \(H_0\) series from order three and the \(\lambda V\) series from order two gives
\[
 \begin{aligned}
 \|R_3\|
 &\le e^{60\lambda}
    \left[\frac{7(60\lambda)^3}{6}
              +\frac{5\lambda(60\lambda)^2}{2}\right]\\
 &=261000e^{60\lambda}\lambda^3
 <600000\lambda^3 .
 \end{aligned}
 \tag{CF13}
\]
Here \(60\lambda\le0.06\), so even \(e^{60\lambda}<2\) suffices.

Now pinch the second-order term into the four exact energy blocks:
\[
 D_2=\sum_jP_jW_2P_j,\qquad
 S_2=\sum_{j\ne k}\frac{P_jW_2P_k}{E_j-E_k}.
 \tag{CF14}
\]
Pinching has norm at most \(\|W_2\|\), since the blocks act on orthogonal subspaces. Thus \(\|D_2\|\le150\), \(\|S_2\|\le900\), and \(S_2\) is anti-Hermitian. Its commutator obeys
\[
 [S_2,H_0]=-(W_2-D_2).
 \tag{CF15}
\]
The second conjugation consequently gives
\[
 F(H-cI)F^\dagger=H_0+\lambda^2D_2+R,\qquad
 F=e^{\lambda^2S_2}e^{\lambda S}.
 \tag{CF16}
\]
Conjugation preserves \(\|R_3\|\). The additional remainder is bounded by the \(H_0\) series from order two and the \(\lambda^2W_2\) series from order one:
\[
 \begin{aligned}
 &e^{1800\lambda^2}
  \left[\frac{7(1800\lambda^2)^2}{2}
                   +150\lambda^2(1800\lambda^2)\right]\\
 &\hspace{1cm}<23220000\lambda^4
       \le23220\lambda^3 .
 \end{aligned}
 \tag{CF17}
\]
For \(\lambda\le10^{-3}\), \(e^{1800\lambda^2}<2\); the coefficient before this exponential is \(11610000\lambda^4\). Combining (CF13) and (CF17) yields the conservative bound
\[
 \|R\|\le10^6\lambda^3.
 \tag{CF18}
\]
Every series here is a convergent finite-dimensional matrix series. The estimate is an explicit remainder bound, not a formal second-order approximation assumed valid at long times.

Anti-Hermiticity and the integral formula for \(e^A-I\) give
\[
 \|F-I\|\le30\lambda+900\lambda^2.
 \tag{CF19}
\]
Apply Duhamel to (CF16), and pay for both outside F factors. On the complete five-qubit space,
\[
 \begin{aligned}
 &\left\|e^{-itH}
       -e^{-it(cI+H_0+\lambda^2D_2)}\right\|\\
 &\qquad\le2(30\lambda+900\lambda^2)
                   +10^6|t|\lambda^3\\
 &\qquad\le62\lambda+10^6|t|\lambda^3 .
 \end{aligned}
 \tag{CF20}
\]
The entire \(D_2\), including the unselected mediator sector, remains in this intermediate full-space comparison.

## 4. Selected-band cancellation and complete phase

The diagonal second-order blocks can be evaluated without an imported perturbation formula. Multiplying the commutator in (CF12) gives
\[
 P_jW_2P_j
   =\sum_{k\ne j}
       \frac{P_jVP_kVP_j}{E_j-E_k}.
 \tag{CF21}
\]
Select \(m=0\) and old parity \(Z=z\), where \(z=\pm1\). Put \(V_Y=Y_1Y_a+Y_2Y_b\). The Pauli signs imply
\[
 V_Y^2=2(I-ZQ),\qquad [Z,Q]=0.
 \tag{CF22}
\]
The YY intermediate states have energy denominator \(2z\), so their combined contribution in (CF21) is
\[
 \frac{2(I-ZQ)}{2z}=zI-Q.
 \tag{CF23}
\]
The mediator term has squared matrix element 6. Its intermediate state has the opposite old parity and \(m=1\), giving denominator \(2z-4\). Its contribution is
\[
 \frac{6}{2z-4}=-2-z .
 \tag{CF24}
\]
Each mixed YY/XX term flips m once. It cannot return to the same \(H_0\) block because the \(m=0\) energies \(1,3\) and the \(m=1\) energies \(5,7\) are disjoint. All such diagonal mixed terms vanish. Adding (CF23) and (CF24) therefore gives
\[
 D_2J_0=J_0(-2I-Q).
 \tag{CF25}
\]
The \(+\lambda^2Z\) self-energy from the YY interactions is canceled by a \(-\lambda^2Z\) virtual-mediator contribution. The remaining \(-2\lambda^2I\) is a selected-band scalar, not an omitted physical block.

Because \(D_2\) is block diagonal in \(H_0\), the selected \(m=0\) subspace is invariant under the comparison generator. Equation (CF25) implies the exact intertwining identity
\[
 e^{-it(cI+H_0+\lambda^2D_2)}J_0
   =e^{-it(c-2\lambda^2)}J_0e^{-it(K-\lambda^2Q)}.
 \tag{CF26}
\]
Restricting (CF20) to \(J_0\), and using that the difference of two isometries has norm at most two, proves (CF6). Restriction applies to the comparison input only; it discards no component of the actual output.

At a prescribed angle \(\varphi\ge0\) and \(T=\varphi/\lambda^2\), the comparison becomes
\[
 e^{-ic_*T}J_0e^{-iTK}e^{i\varphi Q},\qquad
 c_*T=\frac{(2+\sqrt6)\varphi}{\lambda}-2\varphi .
 \tag{CF27}
\]
The complete elapsed old aging and this common scalar are retained. The scalar \(2I\) already in K is counted inside \(e^{-iTK}\), once. The physical evolution is only approximately this product; (CF27) does not assert exact commutation of the actual couplings with K.

## 5. Accuracy, outputs and changed assumptions

For a fixed positive angle \(\varphi\le A\), (CF7) bounds the complete error at T and throughout the stated comparison horizon. For fixed \(A>0\) and fixed \(\Lambda>4\), sufficiently small \(\epsilon\) allows the explicit choice \(\lambda=\epsilon/(62+10^6A)\). Then
\[
 T=\varphi(62+10^6A)^2\epsilon^{-2}.
 \tag{CF28}
\]
This is only the deliberately conservative sufficient resource family following from (CF6). It is not an optimized exponent, a necessary runtime, a coefficient-precision theorem or a claim about a supplied real laboratory scale. The qubit and block counts remain five; the actual coefficients and incident loads are those in (CF1)–(CF4).

The fifth qubit replaces the previous old-only counterterm but introduces a selected product input and a calibrated gap/coupling pair. Unlike the earlier four-qubit exact-counterterm theorem, (CF6) does not cover an arbitrary unknown mediator state and does not give a uniform small error at arbitrarily late times. The old-plus-\(a,b\) input can still be arbitrary and entangled with passive references. Its effective dynamics retain both ancillary outputs.

In particular, the effective interaction remains the complete Q, not an old-only \(X_1X_2\) gate. For an ancillary \(|00\rangle_{ab}\) seed,
\[
 e^{i\varphi Q}(\xi\otimes|00\rangle_{ab})
 =\cos\varphi\,\xi\otimes|00\rangle_{ab}
    -i\sin\varphi\,X_1X_2\xi\otimes|11\rangle_{ab}.
 \tag{CF29}
\]
For \(\xi=|00\rangle_{12}\) and the literal angle \(\cos\theta=3/5,\ \sin\theta=4/5\), this target is entangled across old and ancillary systems. Appending the mediator, old aging and a common phase does not turn it into \(W\xi\) times a common ancillary output. The comparison estimate follows this joint target, not a different clock operation.

## 6. Scope of further composition

The new construction uses the actual Hamiltonian (CF2), including its missing unlisted bonds, selected preparation and calibrated coefficients as suppliers. There is no native microscopic derivation, cooling/loading procedure, or autonomous preparation assertion.

No additional clock background, assembly of overlapping gadgets, receiving device, reset, reuse, capture or permanent halt follows. In particular, the prior weak-background argument used an exact rotation for a different physical Hamiltonian. It cannot be transferred to (CF2) by citation: any added background changes the present conjugation and selected-band calculation and needs its own bound. All constants in this appendix are for the fixed mediator gap 4; no varying-gap limit or near-degeneracy extrapolation is being used.

The F transformations are analytical devices. They are not installed gates and require no uncharged physical implementation. Conversely, they do not remove the need to supply the actual initial mediator state or any of the five blocks.

## 7. Exact sources and exposure

The new proof source is [counterterm_free_gap_mediation/PROPOSAL.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/counterterm_free_gap_mediation/PROPOSAL.md), **8977 bytes, 123 lines**, SHA256
`739a1961076d52b0e26364bd858f957a89a233bfa72aa652efa193ef54ac2cdd`.
The link is the proposed frozen packet location; this appendix does not itself copy or publish that body.

The distinct check is **pending**. No check receipt, acceptance status or final check hash is inferred or fabricated.

The previously accepted construction supplies notation and comparison context through [real_two_body_gap_mediation_probe/PROPOSAL.md](../outputs/real_two_body_gap_mediation_2026_10_18/source_checks/real_two_body_gap_mediation_probe/PROPOSAL.md), **9250 bytes, 116 lines**, SHA256 `d683b07790c9da2d9bf5a27d8045fa19309b918877e31e15431daa74f43d7258`. Its exact-rotation performance theorem is not a premise of the new remainder proof. All load-bearing new spectral and Pauli calculations are displayed above.

The manuscript writer fully read the new source, had already fully read that unchanged context source and its checks, and reconstructed the algebra for this exposition. ROOT proposed the auxiliary cancellation and two-conjugation proof route; the source author disclosed that design exposure. This appendix is source-exposed synthesis, not a blind or additional independent check. It claims no retained audit status.

Only this appendix was written for the task. The frozen main manuscript `NOTE.md`, SHA256 `b0455d70ab5d8e2be293590b14c4d69ab993c4a9dba4fbe4f618b2065eb876bd`, was left unchanged. Work consists of full source reading, analytical exposition and deterministic metadata/readback checks; no scientific executable, simulation, external search, Git/canonical/checkpoint/prompt/axiom change, delegation, model/effort override or publication was performed.
